"""Streamlit UI for ePrint Summary tool."""

import sys
from datetime import datetime
from pathlib import Path

import streamlit as st

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from eprint_summary.config_manager import load_config, load_state, save_config, save_state
from eprint_summary.fetcher import backfill_papers, fetch_new_papers
from eprint_summary.keyword_matcher import is_excluded, match_keywords
from eprint_summary.models import AppConfig, LLMConfig, PaperWithSummary, Summary
from eprint_summary.report import append_to_report
from eprint_summary.summarizer import summarize_paper
from eprint_summary.utils import setup_logging

PROJECT_ROOT = Path(__file__).parent


def init_session_state():
    """Initialize Streamlit session state."""
    if "config" not in st.session_state:
        st.session_state.config = load_config()
    if "results" not in st.session_state:
        st.session_state.results = []
    if "fetch_status" not in st.session_state:
        st.session_state.fetch_status = ""


def get_reports_dir() -> Path:
    return PROJECT_ROOT / st.session_state.config.reports_dir


def get_data_dir() -> Path:
    return PROJECT_ROOT / st.session_state.config.data_dir


def display_paper_card(pws: PaperWithSummary, highlight: bool = False):
    """Display a single paper as an expandable card."""
    paper = pws.paper
    prefix = "**[推荐]** " if highlight else ""
    icon = "⭐" if highlight else "📄"

    with st.expander(f"{icon} {prefix}[{paper.paper_id}] {paper.title}"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**作者:** {', '.join(paper.authors)}")
            st.markdown(f"**分类:** {paper.category}")
            if pws.matched_keywords:
                st.markdown(f"**匹配关键字:** `{'`, `'.join(pws.matched_keywords)}`")
        with col2:
            st.markdown(f"[论文]({paper.url}) | [PDF]({paper.pdf_url})")

        if paper.keywords:
            st.markdown(f"**关键词:** {', '.join(paper.keywords)}")

        st.markdown("---")

        summary = pws.summary
        if summary.background:
            st.markdown(f"**研究背景:** {summary.background}")
        if summary.contributions:
            st.markdown(f"**主要贡献:** {summary.contributions}")
        if summary.results:
            st.markdown(f"**达到效果:** {summary.results}")
        if summary.techniques:
            st.markdown(f"**技术梗概:** {summary.techniques}")


def render_sidebar():
    """Render the sidebar with configuration and actions."""
    config = st.session_state.config

    with st.sidebar:
        st.title("ePrint Summary")
        st.caption("AI-powered cryptography paper tracker")

        # --- LLM Settings ---
        st.subheader("LLM Settings")

        provider = st.selectbox(
            "Provider",
            ["ollama", "groq", "openrouter", "deepseek", "custom"],
            index=["ollama", "groq", "openrouter", "deepseek", "custom"].index(
                config.llm.provider
            )
            if config.llm.provider in ["ollama", "groq", "openrouter", "deepseek", "custom"]
            else 0,
        )

        # Suggest model names based on provider (use config value if provider matches)
        model_suggestions = {
            "ollama": "ollama/llama3.2",
            "groq": "groq/llama-3.3-70b-versatile",
            "openrouter": "openrouter/deepseek/deepseek-chat-v3-0324:free",
            "deepseek": "deepseek/deepseek-chat",
            "custom": config.llm.model_name,
        }
        default_model = (
            config.llm.model_name
            if provider == config.llm.provider
            else model_suggestions.get(provider, config.llm.model_name)
        )

        model_name = st.text_input(
            "Model",
            value=default_model,
        )

        api_base = st.text_input(
            "API Base URL",
            value=config.llm.api_base or ("http://localhost:11434" if provider == "ollama" else ""),
            help="Required for Ollama, optional for cloud providers",
        )

        api_key = st.text_input(
            "API Key",
            value=config.llm.api_key or "",
            type="password",
            help="Not needed for Ollama. For cloud providers, you can also set EPRINT_LLM_API_KEY env var",
        )

        if st.button("Test Connection"):
            with st.spinner("Testing LLM connection..."):
                try:
                    test_config = LLMConfig(
                        provider=provider,
                        model_name=model_name,
                        api_base=api_base if api_base else None,
                        api_key=api_key if api_key else None,
                    )
                    import litellm
                    litellm.suppress_debug_info = True
                    resp = litellm.completion(
                        model=test_config.model_name,
                        messages=[{"role": "user", "content": "Say hello in one word."}],
                        max_tokens=10,
                        api_base=test_config.api_base,
                        api_key=test_config.api_key,
                    )
                    st.success(f"Connected! Response: {resp.choices[0].message.content}")
                except Exception as e:
                    st.error(f"Connection failed: {e}")

        st.divider()

        # --- Keywords ---
        st.subheader("感兴趣的关键字")
        st.caption("匹配这些关键字的论文会被推荐")

        keywords_text = st.text_area(
            "每行一个关键字",
            value="\n".join(config.keywords),
            height=120,
        )

        st.subheader("屏蔽关键字")
        st.caption("匹配这些关键字的论文会被过滤掉")

        exclude_keywords_text = st.text_area(
            "每行一个屏蔽词",
            value="\n".join(config.exclude_keywords),
            height=80,
        )

        if st.button("Save Settings"):
            new_keywords = [k.strip() for k in keywords_text.split("\n") if k.strip()]
            new_exclude = [k.strip() for k in exclude_keywords_text.split("\n") if k.strip()]
            config.keywords = new_keywords
            config.exclude_keywords = new_exclude
            config.llm.provider = provider
            config.llm.model_name = model_name
            config.llm.api_base = api_base if api_base else None
            config.llm.api_key = api_key if api_key else None
            st.session_state.config = config
            save_config(config)
            st.success("Settings saved!")

        st.divider()

        # --- Actions ---
        st.subheader("Actions")

        target_year = st.number_input(
            "Year",
            value=config.target_year or datetime.now().year,
            min_value=2000,
            max_value=datetime.now().year + 1,
        )

        no_summary = st.checkbox(
            "Skip LLM summarization",
            value=False,
            help="Fetch papers without generating AI summaries (faster)",
        )

        col1, col2 = st.columns(2)
        with col1:
            fetch_btn = st.button("Fetch New", type="primary", use_container_width=True)
        with col2:
            backfill_btn = st.button("Backfill", use_container_width=True)

        st.divider()

        # --- Status ---
        st.subheader("Status")
        state = load_state(get_data_dir())
        if state:
            for year, last_num in sorted(state.items(), reverse=True):
                st.metric(f"Year {year}", f"Last: #{last_num}")
        else:
            st.info("No papers processed yet")

    return fetch_btn, backfill_btn, target_year, no_summary


def process_papers(papers, config, no_summary, target_year):
    """Process fetched papers: filter, match keywords, summarize, save report."""
    if not papers:
        st.info("没有发现新论文。")
        return

    # Filter out excluded papers
    if config.exclude_keywords:
        before_count = len(papers)
        papers = [p for p in papers if not is_excluded(p, config.exclude_keywords)]
        excluded_count = before_count - len(papers)
        if excluded_count > 0:
            st.warning(f"已过滤 {excluded_count} 篇不感兴趣的论文")

    if not papers:
        st.info("所有新论文都被屏蔽关键字过滤了。")
        return

    st.success(f"发现 {len(papers)} 篇新论文！")

    progress_bar = st.progress(0, text="正在处理论文...")
    results = []

    for i, paper in enumerate(papers):
        is_match, matched_kws = match_keywords(paper, config.keywords)

        if no_summary:
            summary = Summary(background=paper.abstract)
        else:
            progress_bar.progress(
                (i) / len(papers),
                text=f"正在总结 [{paper.paper_id}] ({i + 1}/{len(papers)})...",
            )
            summary = summarize_paper(paper, config.llm)

        results.append(
            PaperWithSummary(
                paper=paper,
                summary=summary,
                is_keyword_match=is_match,
                matched_keywords=matched_kws,
            )
        )

    progress_bar.progress(1.0, text="完成！")

    # Save report
    reports_dir = get_reports_dir()
    report_path = append_to_report(results, target_year, reports_dir)

    # Update state
    state = load_state(get_data_dir())
    max_number = max(r.paper.number for r in results)
    state[target_year] = max(state.get(target_year, 0), max_number)
    save_state(state, get_data_dir())

    st.session_state.results = results
    st.session_state.fetch_status = (
        f"已处理 {len(results)} 篇论文，报告已保存到 `{report_path.name}`。"
    )

    return results


def render_latest_tab(fetch_btn, backfill_btn, target_year, no_summary):
    """Render the Latest Papers tab."""
    config = st.session_state.config

    if fetch_btn:
        with st.spinner("Fetching from RSS feed..."):
            state = load_state(get_data_dir())
            papers = fetch_new_papers(state, target_year)
        process_papers(papers, config, no_summary, target_year)

    if backfill_btn:
        with st.spinner("Backfilling from year listing page (this may take a while)..."):
            state = load_state(get_data_dir())
            papers = backfill_papers(target_year, state)
        process_papers(papers, config, no_summary, target_year)

    # Display status
    if st.session_state.fetch_status:
        st.info(st.session_state.fetch_status)

    # Display results
    results = st.session_state.results
    if results:
        recommended = [r for r in results if r.is_keyword_match]
        others = [r for r in results if not r.is_keyword_match]

        if recommended:
            st.subheader(f"推荐论文 ({len(recommended)})")
            for r in recommended:
                display_paper_card(r, highlight=True)

        if others:
            st.subheader(f"其他新论文 ({len(others)})")
            for r in others:
                display_paper_card(r)
    else:
        st.markdown(
            "点击侧栏的 **Fetch New** 获取新论文，"
            "或点击 **Backfill** 补齐本年度遗漏的论文。"
        )


def render_reports_tab():
    """Render the Reports tab."""
    reports_dir = get_reports_dir()

    if not reports_dir.exists():
        st.info("No reports generated yet. Fetch some papers first!")
        return

    report_files = sorted(reports_dir.glob("eprint_*.md"), reverse=True)
    if not report_files:
        st.info("No reports generated yet. Fetch some papers first!")
        return

    selected_file = st.selectbox(
        "Select report",
        report_files,
        format_func=lambda f: f.stem.replace("eprint_", "Year "),
    )

    if selected_file:
        content = selected_file.read_text(encoding="utf-8")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.download_button(
                "Download Markdown",
                content,
                file_name=selected_file.name,
                mime="text/markdown",
                use_container_width=True,
            )
        with col2:
            # Count papers in report
            import re
            paper_count = len(re.findall(r"\[(\d{4}/\d+)\]", content))
            st.metric("Papers in report", paper_count)

        st.divider()
        st.markdown(content)


def render_about_tab():
    """Render the About tab."""
    st.markdown("""
## About ePrint Summary

A tool to help cryptography researchers track and summarize the latest papers
from the [IACR ePrint Archive](https://eprint.iacr.org/).

### Features

- **Automatic fetching** of new papers via RSS feed
- **AI-powered summaries** of paper abstracts (supports local and cloud LLMs)
- **Keyword-based recommendations** to highlight papers of interest
- **Markdown reports** organized by year
- **Backfill mode** for catching up on missed papers

### How it works

1. Configure your preferred LLM in the sidebar (Ollama for local, or cloud APIs)
2. Set your research interest keywords
3. Click "Fetch New" to check for new papers
4. Papers matching your keywords are highlighted as recommended
5. Reports are saved as Markdown files in the `reports/` directory

### CLI Usage

```bash
python cli.py                    # Fetch new papers for current year
python cli.py --year 2025        # Specific year
python cli.py --backfill         # Backfill missed papers
python cli.py --dry-run          # Preview without processing
python cli.py --no-summary       # Skip AI summarization
```

### Supported LLM Providers

| Provider | Model Example | API Key |
|----------|--------------|---------|
| Ollama (local) | `ollama/llama3.2` | Not needed |
| Groq | `groq/llama-3.3-70b-versatile` | Required |
| OpenRouter | `openrouter/deepseek/deepseek-chat-v3-0324:free` | Required |
| DeepSeek | `deepseek/deepseek-chat` | Required |
    """)


def main():
    st.set_page_config(
        page_title="ePrint Summary",
        page_icon="📚",
        layout="wide",
    )

    setup_logging("WARNING")  # Reduce noise in Streamlit
    init_session_state()

    # Render sidebar and get action states
    fetch_btn, backfill_btn, target_year, no_summary = render_sidebar()

    # Main content area with tabs
    tab_latest, tab_reports, tab_about = st.tabs(
        ["📄 Latest Papers", "📊 Reports", "ℹ️ About"]
    )

    with tab_latest:
        render_latest_tab(fetch_btn, backfill_btn, target_year, no_summary)

    with tab_reports:
        render_reports_tab()

    with tab_about:
        render_about_tab()


if __name__ == "__main__":
    main()
