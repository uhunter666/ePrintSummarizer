"""LLM abstraction layer for paper summarization."""

import json
import logging
import re
import time

from .models import LLMConfig, Paper, Summary

logger = logging.getLogger(__name__)

SUMMARY_SYSTEM_PROMPT = """你是一位密码学专家。根据论文的标题、作者和摘要，用中文生成一个结构化的总结，以JSON对象格式输出，包含以下4个键："background"（研究背景）、"contributions"（主要贡献）、"results"（达到的效果）、"techniques"（技术梗概）。每个值1-2句话，使用专业术语。只输出JSON对象，不要输出其他内容。

输出示例:
{"background": "...", "contributions": "...", "results": "...", "techniques": "..."}\n"""


def _format_paper_for_llm(paper: Paper, max_abstract_chars: int = 1500) -> str:
    """Format paper metadata as input for the LLM."""
    abstract = paper.abstract
    if len(abstract) > max_abstract_chars:
        abstract = abstract[:max_abstract_chars] + "..."
    return (
        f"Title: {paper.title}\n"
        f"Authors: {', '.join(paper.authors)}\n"
        f"Category: {paper.category}\n"
        f"\nAbstract:\n{abstract}"
    )


def _parse_summary_response(raw_text: str) -> Summary:
    """Parse LLM response into a Summary, with multiple fallback strategies."""
    # Strategy 1: direct JSON parse
    try:
        data = json.loads(raw_text)
        return Summary(**data)
    except (json.JSONDecodeError, Exception):
        pass

    # Strategy 2: extract JSON from markdown code block
    match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw_text, re.DOTALL)
    if match:
        try:
            data = json.loads(match.group(1))
            return Summary(**data)
        except (json.JSONDecodeError, Exception):
            pass

    # Strategy 3: find first { to last }
    start = raw_text.find("{")
    end = raw_text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            data = json.loads(raw_text[start : end + 1])
            return Summary(**data)
        except (json.JSONDecodeError, Exception):
            pass

    # Strategy 4: try to repair truncated JSON
    if start != -1:
        fragment = raw_text[start:]
        # Try to extract whatever key-value pairs we can find
        extracted = {}
        for key in ("background", "contributions", "results", "techniques"):
            pattern = rf'"{key}"\s*:\s*"((?:[^"\\]|\\.)*)(?:"|$)'
            m = re.search(pattern, fragment, re.DOTALL)
            if m:
                extracted[key] = m.group(1).replace('\\"', '"').replace("\\n", " ").strip()
        if extracted:
            logger.warning("Repaired truncated JSON, extracted %d fields", len(extracted))
            return Summary(**extracted)

    # Strategy 5: fallback with raw text
    logger.warning("Could not parse LLM response as JSON, using raw text")
    return Summary(
        background=raw_text[:300],
        contributions="[Summary generation failed - see abstract]",
        results="",
        techniques="",
    )


def summarize_paper(paper: Paper, config: LLMConfig) -> Summary:
    """Summarize a paper's abstract using the configured LLM.

    Args:
        paper: The paper to summarize.
        config: LLM configuration (model, API key, etc.).

    Returns:
        Structured Summary of the paper.
    """
    try:
        import litellm

        # Suppress litellm's verbose logging
        litellm.suppress_debug_info = True

        kwargs = {
            "model": config.model_name,
            "messages": [
                {"role": "system", "content": SUMMARY_SYSTEM_PROMPT},
                {"role": "user", "content": _format_paper_for_llm(paper)},
            ],
            "temperature": config.temperature,
            "max_tokens": config.max_tokens,
        }

        if config.api_base:
            kwargs["api_base"] = config.api_base
        if config.api_key:
            kwargs["api_key"] = config.api_key

        response = litellm.completion(**kwargs)
        raw = response.choices[0].message.content
        return _parse_summary_response(raw)

    except ImportError:
        logger.error("litellm is not installed. Install with: pip install litellm")
        return Summary(
            background="[litellm not installed]",
            contributions="[Cannot generate summary]",
        )
    except Exception as e:
        logger.error("LLM call failed for paper %s: %s", paper.paper_id, e)
        return Summary(
            background=f"[LLM error: {e}]",
            contributions="[Summary generation failed - see abstract]",
        )


def summarize_papers(
    papers: list[Paper],
    config: LLMConfig,
    progress_callback=None,
) -> list[Summary]:
    """Summarize a list of papers with rate limiting.

    Args:
        papers: Papers to summarize.
        config: LLM configuration.
        progress_callback: Optional callable(current, total) for progress.

    Returns:
        List of Summary objects (same order as input papers).
    """
    summaries = []
    for i, paper in enumerate(papers):
        logger.info(
            "Summarizing paper %d/%d: %s", i + 1, len(papers), paper.paper_id
        )
        summary = summarize_paper(paper, config)
        summaries.append(summary)

        if progress_callback:
            progress_callback(i + 1, len(papers))

        # Rate limiting between API calls
        if i < len(papers) - 1 and config.request_delay > 0:
            time.sleep(config.request_delay)

    return summaries
