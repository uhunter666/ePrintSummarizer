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


def fetch_new_papers(
    state: dict[int, int],
    target_year: int | None = None,
) -> list[Paper]:
    """Fetch new papers from the ePrint RSS feed.

    Args:
        state: Dict mapping year to last processed paper number.
        target_year: If set, only return papers from this year.
                     If None, return papers from all years.

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

    papers.sort(key=lambda p: (p.year, p.number))
    logger.info("Found %d new papers", len(papers))
    return papers


def fetch_all_paper_ids_for_year(year: int) -> list[int]:
    """Scrape the year listing page to get all paper numbers.

    Used for backfill mode when RSS feed doesn't cover all missed papers.
    """
    url = f"{EPRINT_BASE_URL}/{year}/"
    logger.info("Fetching paper listing for year %d from %s", year, url)

    resp = requests.get(url, timeout=30)
    resp.raise_for_status()

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

    resp = requests.get(url, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract title
    title_tag = soup.find("h3", class_="paper-title")
    if not title_tag:
        title_tag = soup.find("h2")
    title = title_tag.get_text(strip=True) if title_tag else f"Paper {year}/{number}"

    # Extract authors
    authors = []
    author_section = soup.find("p", class_="paper-author")
    if author_section:
        for a_tag in author_section.find_all("a"):
            name = a_tag.get_text(strip=True)
            if name:
                authors.append(name)
    if not authors:
        # Fallback: look for author names in meta tags
        for meta in soup.find_all("meta", attrs={"name": "citation_author"}):
            name = meta.get("content", "").strip()
            if name:
                authors.append(name)

    # Extract abstract
    abstract = ""
    abstract_section = soup.find("div", class_="paper-abstract")
    if abstract_section:
        # Remove the "Abstract:" label if present
        abstract = abstract_section.get_text(strip=True)
        if abstract.lower().startswith("abstract"):
            abstract = abstract[8:].lstrip(":").strip()
    if not abstract:
        abstract_meta = soup.find("meta", attrs={"name": "citation_abstract"})
        if abstract_meta:
            abstract = abstract_meta.get("content", "").strip()

    # Extract category
    category = "Unknown"
    category_tag = soup.find("a", class_="badge")
    if category_tag:
        category = category_tag.get_text(strip=True)

    # Extract keywords
    keywords = []
    kw_section = soup.find("p", class_="keywords")
    if kw_section:
        kw_text = kw_section.get_text(strip=True)
        if kw_text.lower().startswith("keywords:"):
            kw_text = kw_text[9:].strip()
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
