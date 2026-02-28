"""Shared utilities."""

import logging
import re
from datetime import datetime


def setup_logging(level: str = "INFO") -> None:
    """Configure logging for the application."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def parse_paper_id_from_url(url: str) -> tuple[int, int]:
    """Extract year and paper number from an ePrint URL.

    Args:
        url: e.g., "https://eprint.iacr.org/2026/380"

    Returns:
        Tuple of (year, number), e.g., (2026, 380)
    """
    match = re.search(r"/(\d{4})/(\d+)", url)
    if not match:
        raise ValueError(f"Cannot parse paper ID from URL: {url}")
    return int(match.group(1)), int(match.group(2))


def format_paper_id(year: int, number: int) -> str:
    """Format a paper ID string."""
    return f"{year}/{number}"


def parse_rfc3339_date(date_str: str | None) -> datetime | None:
    """Parse various date formats from RSS feeds."""
    if not date_str:
        return None
    try:
        # feedparser provides time_struct, but we handle string fallback
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(date_str)
    except (ValueError, TypeError):
        pass
    try:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None
