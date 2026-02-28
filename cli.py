"""Command-line entry point for ePrint Summary tool.

Usage:
    python cli.py                    # Fetch new papers for current year
    python cli.py --year 2025        # Fetch new papers for specific year
    python cli.py --backfill         # Backfill missed papers
    python cli.py --dry-run          # Show what would be processed
    python cli.py --no-summary       # Fetch without LLM summarization
    python cli.py --send-email       # Fetch and send HTML report via email
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from eprint_summary.config_manager import load_config, load_state, save_state
from eprint_summary.fetcher import backfill_papers, fetch_new_papers
from eprint_summary.keyword_matcher import is_excluded, match_keywords
from eprint_summary.models import AppConfig, PaperWithSummary, Summary
from eprint_summary.report import append_to_report
from eprint_summary.summarizer import summarize_paper
from eprint_summary.utils import setup_logging

PROJECT_ROOT = Path(__file__).parent


def run_pipeline(
    config: AppConfig,
    target_year: int | None = None,
    backfill: bool = False,
    no_summary: bool = False,
    send_email: bool = False,
    quiet: bool = False,
) -> list[PaperWithSummary]:
    """Core pipeline: fetch → filter → summarize → report → email.

    This is the shared logic used by both cli.py and scheduler.py.

    Args:
        config: Application configuration.
        target_year: Year to fetch papers for (None = current year).
        backfill: If True, use backfill mode instead of RSS.
        no_summary: If True, skip LLM summarization.
        send_email: If True, send HTML report via email after generating.
        quiet: If True, suppress print output (for scheduler use).

    Returns:
        List of processed PaperWithSummary objects, or empty list.
    """
    def log(msg):
        if not quiet:
            print(msg)

    target_year = target_year or config.target_year or datetime.now().year
    reports_dir = PROJECT_ROOT / config.reports_dir
    data_dir = PROJECT_ROOT / config.data_dir

    # Load state
    state = load_state(data_dir)
    last_num = state.get(target_year, 0)
    log(f"Target year: {target_year}")
    log(f"Last processed paper: {target_year}/{last_num}" if last_num else f"No papers processed yet for {target_year}")

    # Fetch papers
    if backfill:
        log("Running in backfill mode (scraping year listing page)...")
        papers = backfill_papers(
            target_year,
            state,
            progress_callback=lambda cur, total: print(
                f"  Scraping paper {cur}/{total}...", end="\r"
            ) if not quiet else None,
        )
    else:
        log("Fetching from RSS feed...")
        papers = fetch_new_papers(state, target_year)

    if not papers:
        log("No new papers found.")
        return []

    # Filter out excluded papers
    excluded_count = 0
    if config.exclude_keywords:
        filtered = []
        for p in papers:
            if is_excluded(p, config.exclude_keywords):
                excluded_count += 1
                logger.info("Excluded: [%s] %s", p.paper_id, p.title)
            else:
                filtered.append(p)
        papers = filtered

    log(f"\nFound {len(papers)} new papers" + (f" (filtered out {excluded_count} excluded)" if excluded_count else "") + ":")
    for p in papers:
        log(f"  [{p.paper_id}] {p.title}")

    if not papers:
        log("All papers were excluded by exclude_keywords filter.")
        return []

    # Match keywords and summarize
    results = []
    for paper in papers:
        is_match, matched_kws = match_keywords(paper, config.keywords)

        if no_summary:
            summary = Summary(background=paper.abstract)
        else:
            log(f"\nSummarizing [{paper.paper_id}]... ")
            summary = summarize_paper(paper, config.llm)
            log("done.")

        pws = PaperWithSummary(
            paper=paper,
            summary=summary,
            is_keyword_match=is_match,
            matched_keywords=matched_kws,
        )
        results.append(pws)

        if is_match:
            log(f"  ** Keyword match: {', '.join(matched_kws)}")

    # Generate report
    report_path = append_to_report(results, target_year, reports_dir)
    log(f"\nReport updated: {report_path}")

    # Update state
    max_number = max(pws.paper.number for pws in results)
    state[target_year] = max(state.get(target_year, 0), max_number)
    save_state(state, data_dir)
    log(f"State updated: last processed = {target_year}/{max_number}")

    # Send email if requested
    if send_email or config.email.enabled:
        _send_email_report(results, target_year, config)

    # Show recommended
    recommended = [r for r in results if r.is_keyword_match]
    if recommended:
        log(f"\nRecommended papers ({len(recommended)}):")
        for r in recommended:
            log(f"  [{r.paper.paper_id}] {r.paper.title}")
            log(f"    Matched: {', '.join(r.matched_keywords)}")

    return results


def _send_email_report(
    results: list[PaperWithSummary],
    year: int,
    config: AppConfig,
) -> None:
    """Generate HTML from this batch of results and send via email."""
    from eprint_summary.emailer import convert_md_to_html, send_report_email
    from eprint_summary.report import _format_paper_entry

    if not config.email.sender or not config.email.recipients:
        logger.warning("Email not configured (missing sender or recipients), skipping")
        return

    # Build Markdown for just this batch
    recommended = [r for r in results if r.is_keyword_match]
    others = [r for r in results if not r.is_keyword_match]

    md_lines = []
    md_lines.append(f"# ePrint 论文更新 - {datetime.now().strftime('%Y-%m-%d')}\n")
    md_lines.append(f"*共 {len(results)} 篇新论文*\n")

    if recommended:
        md_lines.append(f"\n## 推荐论文 ({len(recommended)} 篇)\n")
        for pws in recommended:
            md_lines.append(_format_paper_entry(pws))

    if others:
        md_lines.append(f"\n## 其他论文 ({len(others)} 篇)\n")
        for pws in others:
            md_lines.append(_format_paper_entry(pws))

    md_content = "\n".join(md_lines)
    html_content = convert_md_to_html(md_content)

    subject = f"ePrint 论文更新 - {datetime.now().strftime('%Y-%m-%d')} ({len(results)}篇新论文)"

    try:
        send_report_email(html_content, subject, config.email)
        print(f"Email sent to {', '.join(config.email.recipients)}")
    except Exception as e:
        logger.error("Failed to send email: %s", e)
        print(f"Email sending failed: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="ePrint Summary - Fetch and summarize IACR ePrint papers"
    )
    parser.add_argument(
        "--year", type=int, default=None,
        help="Target year (default: current year)",
    )
    parser.add_argument(
        "--backfill", action="store_true",
        help="Backfill mode: scrape year listing page for missed papers",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be processed without actually summarizing",
    )
    parser.add_argument(
        "--no-summary", action="store_true",
        help="Fetch papers without LLM summarization",
    )
    parser.add_argument(
        "--send-email", action="store_true",
        help="Send HTML report via email after generating",
    )
    parser.add_argument(
        "--config", type=str, default=None,
        help="Path to config.yaml (default: ./config.yaml)",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    setup_logging(config.log_level)

    if args.dry_run:
        # Dry run: just fetch and display, no summarize/report/email
        target_year = args.year or config.target_year or datetime.now().year
        data_dir = PROJECT_ROOT / config.data_dir
        state = load_state(data_dir)
        print(f"Target year: {target_year}")
        papers = fetch_new_papers(state, target_year)

        if config.exclude_keywords:
            before = len(papers)
            papers = [p for p in papers if not is_excluded(p, config.exclude_keywords)]
            excluded = before - len(papers)
        else:
            excluded = 0

        print(f"\nFound {len(papers)} new papers" + (f" (filtered out {excluded} excluded)" if excluded else "") + ":")
        for p in papers:
            print(f"  [{p.paper_id}] {p.title}")
            print(f"    Authors: {', '.join(p.authors)}")
            print(f"    Category: {p.category}")
        print("\n[Dry run] No changes made.")
        return

    run_pipeline(
        config=config,
        target_year=args.year,
        backfill=args.backfill,
        no_summary=args.no_summary,
        send_email=args.send_email,
    )


if __name__ == "__main__":
    main()
