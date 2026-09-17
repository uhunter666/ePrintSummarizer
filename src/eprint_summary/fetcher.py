"""RSS parsing and paper fetching from IACR ePrint archive."""

import logging
import time
from datetime import datetime

import feedparser
import requests
from bs4 import BeautifulSoup

from .models import Paper
from .utils import format_paper_id, parse_paper_id_from_url

logger = logging.getLogger(__name__)

EPRINT_RSS_URL = "https://eprint.iacr.org/rss/rss.xml"
EPRINT_BASE_URL = "https://eprint.iacr.org"

# ePrint rate-limits aggressive scrapers (HTTP 429); stay polite.
REQUEST_HEADERS = {
    "User-Agent": "ePrintSummary/1.0 (personal research digest; +https://eprint.iacr.org)",
}
LISTING_FALLBACK_DELAY = 3.0


def _get(url: str, timeout: int = 20, retries: int = 3) -> requests.Response:
    """GET with a polite delay and exponential backoff on HTTP 429.

    ePrint throttles bursts of requests, so a fixed pace plus backoff keeps the
    scraper usable without hammering the archive.
    """
    for attempt in range(retries):
        resp = requests.get(url, timeout=timeout, headers=REQUEST_HEADERS)
        if resp.status_code != 429:
            resp.raise_for_status()
            return resp
        wait = 20 * (attempt + 1)
        logger.warning("Rate-limited on %s; retrying in %ds (%d/%d)", url, wait, attempt + 1, retries)
        time.sleep(wait)

    resp = requests.get(url, timeout=timeout, headers=REQUEST_HEADERS)
    resp.raise_for_status()
    return resp


def fetch_new_papers(
    state: dict[int, int],
    target_year: int | None = None,
    listing_fallback: bool = True,
) -> list[Paper]:
    """Fetch new papers from the ePrint RSS feed.

    The RSS feed is rebuilt roughly once a day and can lag behind the archive,
    so by default we also consult the year listing page (which is updated as
    soon as papers are published) and scrape any papers the feed has missed.

    Args:
        state: Dict mapping year to last processed paper number.
        target_year: If set, only return papers from this year.
                     If None, return papers from all years.
        listing_fallback: Also check the year listing for papers missing from RSS.

    Returns:
        List of new Paper objects, sorted by (year, number).
    """
    logger.info("Fetching RSS feed from %s", EPRINT_RSS_URL)
    feed = feedparser.parse(EPRINT_RSS_URL)

    if feed.bozo and not feed.entries:
        logger.error("Failed to parse RSS feed: %s", feed.bozo_exception)
        return []

    papers = []
    for entry in feed.entries:
        try:
            year, number = parse_paper_id_from_url(entry.link)
        except ValueError:
            logger.warning("Skipping entry with unparseable link: %s", entry.get("link"))
            continue

        if target_year and year != target_year:
            continue

        last_processed = state.get(year, 0)
        if number <= last_processed:
            continue

        # Extract authors from dc:creator elements
        authors = []
        if hasattr(entry, "authors"):
            authors = [a.get("name", "").strip() for a in entry.authors if a.get("name")]
        elif hasattr(entry, "author"):
            authors = [entry.author.strip()]

        # Extract category
        category = "Unknown"
        if entry.get("tags"):
            category = entry.tags[0].get("term", "Unknown")

        # Extract abstract from description/summary
        abstract = entry.get("summary", "").strip()

        # Parse publication date
        published_date = None
        if hasattr(entry, "published"):
            try:
                published_date = datetime(*entry.published_parsed[:6])
            except (TypeError, AttributeError):
                pass

        paper = Paper(
            paper_id=format_paper_id(year, number),
            year=year,
            number=number,
            title=entry.title.strip(),
            authors=authors,
            abstract=abstract,
            category=category,
            keywords=[],
            url=entry.link,
            pdf_url=f"{entry.link}.pdf",
            published_date=published_date,
        )
        papers.append(paper)

    if listing_fallback and target_year:
        papers.extend(_papers_missing_from_rss(target_year, state, papers))

    papers.sort(key=lambda p: (p.year, p.number))
    logger.info("Found %d new papers", len(papers))
    return papers


def _papers_missing_from_rss(
    year: int,
    state: dict[int, int],
    rss_papers: list[Paper],
) -> list[Paper]:
    """Scrape papers that are already in the archive but absent from the RSS feed.

    ePrint's RSS is regenerated on a schedule, so a morning run can miss the
    batch published later that day. The year listing page reflects the archive
    immediately (latest ~100 entries), so it is used as a safety net.
    """
    last = state.get(year, 0)
    try:
        numbers = fetch_all_paper_ids_for_year(year)
    except Exception as exc:  # noqa: BLE001 - never let the fallback break a run
        logger.warning("Listing fallback unavailable for %d: %s", year, exc)
        return []

    known = {p.number for p in rss_papers}
    missing = [n for n in numbers if n > last and n not in known]
    if not missing:
        return []

    visible_from = min(numbers)
    if last and visible_from > last + 1:
        logger.warning(
            "Gap detected for %d: state=%d but listing only shows %d..%d; "
            "run `cli.py --backfill` to fill older papers.",
            year, last, visible_from, max(numbers),
        )

    logger.warning(
        "RSS missed %d paper(s) present in the archive: %s", len(missing), missing
    )
    scraped: list[Paper] = []
    for i, number in enumerate(missing):
        try:
            scraped.append(scrape_paper_page(year, number))
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to scrape %d/%d: %s", year, number, exc)
        if i < len(missing) - 1:
            time.sleep(LISTING_FALLBACK_DELAY)
    return scraped


def fetch_all_paper_ids_for_year(year: int) -> list[int]:
    """Scrape the year listing page to get all paper numbers.

    Used for backfill mode when RSS feed doesn't cover all missed papers.
    """
    url = f"{EPRINT_BASE_URL}/{year}/"
    logger.info("Fetching paper listing for year %d from %s", year, url)

    resp = _get(url, timeout=30)

    soup = BeautifulSoup(resp.text, "html.parser")
    paper_ids = set()

    # Find all links matching /YYYY/NNN pattern
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        try:
            y, n = parse_paper_id_from_url(href)
            if y == year:
                paper_ids.add(n)
        except ValueError:
            continue

    result = sorted(paper_ids)
    logger.info("Found %d papers for year %d", len(result), year)
    return result


def scrape_paper_page(year: int, number: int) -> Paper:
    """Scrape an individual paper page for full metadata.

    Used for backfill mode and keyword enrichment.
    """
    url = f"{EPRINT_BASE_URL}/{year}/{number}"
    logger.info("Scraping paper page: %s", url)

    resp = _get(url, timeout=20)

    soup = BeautifulSoup(resp.text, "html.parser")

    def meta(name: str) -> list[str]:
        return [
            m.get("content", "").strip()
            for m in soup.find_all("meta", attrs={"name": name})
            if m.get("content")
        ]

    # Title: Highwire meta tag first, then the page heading.
    title = (meta("citation_title") or [""])[0]
    if not title:
        heading = soup.find("h3", class_="paper-title") or soup.find("h3") or soup.find("h2")
        title = heading.get_text(strip=True) if heading else f"Paper {year}/{number}"

    # Authors: meta tags first, then the author spans on the page.
    authors = meta("citation_author")
    if not authors:
        authors = [
            s.get_text(" ", strip=True)
            for s in soup.find_all("span", class_="authorName")
            if s.get_text(strip=True)
        ]

    # Abstract: the page renders it as the first pre-wrapped paragraph.
    abstract = ""
    abstract_p = soup.find("p", style=lambda v: v and "pre-wrap" in v)
    if abstract_p:
        abstract = abstract_p.get_text(" ", strip=True)
    if not abstract:
        abstract_box = soup.find(class_="paper-abstract")
        if abstract_box:
            abstract = abstract_box.get_text(" ", strip=True)
    if abstract.lower().startswith("abstract"):
        abstract = abstract[8:].lstrip(":").strip()

    # Category: first category badge (the keyword badges share the class).
    category = "Unknown"
    category_tag = soup.find("small", class_=lambda c: c and "category" in c)
    if category_tag:
        category = category_tag.get_text(strip=True)

    # Keywords: link badges inside the metadata list.
    keywords = []
    kw_section = soup.find("dd", class_="keywords")
    if kw_section:
        keywords = [a.get_text(strip=True) for a in kw_section.find_all("a") if a.get_text(strip=True)]
        if not keywords:
            kw_text = kw_section.get_text(strip=True)
            keywords = [k.strip() for k in kw_text.split(",") if k.strip()]

    return Paper(
        paper_id=format_paper_id(year, number),
        year=year,
        number=number,
        title=title,
        authors=authors,
        abstract=abstract,
        category=category,
        keywords=keywords,
        url=url,
        pdf_url=f"{url}.pdf",
    )


def backfill_papers(
    year: int,
    state: dict[int, int],
    delay: float = 1.5,
    progress_callback=None,
) -> list[Paper]:
    """Fetch papers that RSS might have missed.

    Args:
        year: Target year.
        state: Current processing state.
        delay: Seconds to wait between requests (polite scraping).
        progress_callback: Optional callable(current, total) for progress updates.

    Returns:
        List of newly fetched Paper objects.
    """
    all_ids = fetch_all_paper_ids_for_year(year)
    last = state.get(year, 0)
    missing = [n for n in all_ids if n > last]

    if not missing:
        logger.info("No missing papers to backfill for year %d", year)
        return []

    logger.info("Backfilling %d papers for year %d", len(missing), year)
    papers = []
    for i, number in enumerate(missing):
        try:
            paper = scrape_paper_page(year, number)
            papers.append(paper)
        except Exception as e:
            logger.error("Failed to scrape paper %d/%d: %s", year, number, e)

        if progress_callback:
            progress_callback(i + 1, len(missing))

        if i < len(missing) - 1:
            time.sleep(delay)

    papers.sort(key=lambda p: p.number)
    return papers
