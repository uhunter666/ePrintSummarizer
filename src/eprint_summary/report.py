"""Markdown report generation and file management."""

import logging
import re
from datetime import datetime
from pathlib import Path

from .models import PaperWithSummary

logger = logging.getLogger(__name__)


def _generate_report_header(year: int) -> str:
    """Generate the header for a new year's report file."""
    return (
        f"# IACR ePrint 论文摘要 - {year}\n\n"
        f"> 密码学论文自动摘要，来源：[IACR ePrint Archive](https://eprint.iacr.org/{year}/)\n"
        f"> 由 [ePrint Summary Tool](https://github.com/lym/ePrintSummary) 生成\n\n"
        f"---\n"
    )


def _format_paper_entry(pws: PaperWithSummary) -> str:
    """Format a single paper entry as Markdown."""
    paper = pws.paper
    summary = pws.summary

    lines = []

    # Title with optional recommendation marker
    if pws.is_keyword_match:
        lines.append(
            f"### [推荐] [{paper.paper_id}] {paper.title}\n"
        )
        lines.append(
            f"- **匹配关键字:** {', '.join(pws.matched_keywords)}\n"
        )
    else:
        lines.append(f"### [{paper.paper_id}] {paper.title}\n")

    # Metadata
    lines.append(f"- **作者:** {', '.join(paper.authors)}\n")
    lines.append(f"- **分类:** {paper.category}\n")
    if paper.keywords:
        lines.append(f"- **关键词:** {', '.join(paper.keywords)}\n")
    lines.append(
        f"- **链接:** [论文]({paper.url}) | [PDF]({paper.pdf_url})\n"
    )

    # Summary
    lines.append("")
    if summary.background:
        lines.append(f"> **研究背景:** {summary.background}\n>")
    if summary.contributions:
        lines.append(f"> **主要贡献:** {summary.contributions}\n>")
    if summary.results:
        lines.append(f"> **达到效果:** {summary.results}\n>")
    if summary.techniques:
        lines.append(f"> **技术梗概:** {summary.techniques}")

    lines.append("\n---\n")

    return "\n".join(lines)


def get_existing_paper_ids(report_path: Path) -> set[str]:
    """Scan a report file for paper IDs already written.

    Used to prevent duplicate entries in case of crashes.
    """
    if not report_path.exists():
        return set()
    content = report_path.read_text(encoding="utf-8")
    return set(re.findall(r"\[(\d{4}/\d+)\]", content))


def append_to_report(
    papers_with_summaries: list[PaperWithSummary],
    year: int,
    reports_dir: str | Path = "reports",
) -> Path:
    """Append new paper summaries to the year's report file.

    Args:
        papers_with_summaries: Papers with their summaries to append.
        year: Target year for the report file.
        reports_dir: Directory containing report files.

    Returns:
        Path to the report file.
    """
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / f"eprint_{year}.md"

    # Check for existing paper IDs to avoid duplicates
    existing_ids = get_existing_paper_ids(report_path)
    new_papers = [
        pws for pws in papers_with_summaries
        if pws.paper.paper_id not in existing_ids
    ]

    if not new_papers:
        logger.info("No new papers to add to report (all already present)")
        return report_path

    # Build the new batch content
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    numbers = [pws.paper.number for pws in new_papers]
    min_num, max_num = min(numbers), max(numbers)

    batch_lines = []
    batch_lines.append(f"\n## 更新: {now}\n\n")
    batch_lines.append(f"*新增 {len(new_papers)} 篇论文 (编号 {min_num}--{max_num})*\n\n")

    # Write recommended papers first
    recommended = [p for p in new_papers if p.is_keyword_match]
    others = [p for p in new_papers if not p.is_keyword_match]

    for pws in recommended:
        batch_lines.append(_format_paper_entry(pws))
    for pws in others:
        batch_lines.append(_format_paper_entry(pws))

    new_content = "".join(batch_lines)

    # Insert new batch right after the header so newest papers are on top
    if not report_path.exists():
        header = _generate_report_header(year)
        report_path.write_text(header + new_content, encoding="utf-8")
    else:
        existing = report_path.read_text(encoding="utf-8")
        # Find the end of header (after the first "---\n")
        header_end = existing.find("---\n")
        if header_end != -1:
            header_end += len("---\n")
            updated = existing[:header_end] + new_content + existing[header_end:]
        else:
            updated = existing + new_content
        report_path.write_text(updated, encoding="utf-8")

    logger.info(
        "Appended %d papers to %s", len(new_papers), report_path
    )

    # Generate HTML version from the full Markdown report
    generate_html_report(report_path)

    return report_path


def generate_html_report(md_path: Path) -> Path:
    """Convert a Markdown report file to HTML and save alongside it.

    Args:
        md_path: Path to the .md report file.

    Returns:
        Path to the generated .html file.
    """
    from .emailer import convert_md_to_html

    md_content = md_path.read_text(encoding="utf-8")
    html_content = convert_md_to_html(md_content)

    html_path = md_path.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")

    logger.info("HTML report generated: %s", html_path)
    return html_path
