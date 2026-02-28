"""Keyword matching and paper recommendation/exclusion logic."""

from .models import Paper


def _get_searchable_text(paper: Paper) -> str:
    """Build a lowercase searchable string from paper metadata."""
    return " ".join([
        paper.title,
        paper.abstract,
        paper.category,
        " ".join(paper.keywords),
    ]).lower()


def match_keywords(paper: Paper, keywords: list[str]) -> tuple[bool, list[str]]:
    """Check if a paper matches any of the user's interest keywords.

    Args:
        paper: The paper to check.
        keywords: List of keywords to match against.

    Returns:
        Tuple of (is_match, list_of_matched_keywords).
    """
    if not keywords:
        return False, []

    searchable_text = _get_searchable_text(paper)
    matched = []
    for kw in keywords:
        if kw.strip().lower() in searchable_text:
            matched.append(kw.strip())

    return len(matched) > 0, matched


def is_excluded(paper: Paper, exclude_keywords: list[str]) -> bool:
    """Check if a paper should be excluded based on exclude keywords.

    Args:
        paper: The paper to check.
        exclude_keywords: Keywords that mark a paper as uninteresting.

    Returns:
        True if the paper matches any exclude keyword.
    """
    if not exclude_keywords:
        return False

    searchable_text = _get_searchable_text(paper)
    for kw in exclude_keywords:
        if kw.strip().lower() in searchable_text:
            return True
    return False
