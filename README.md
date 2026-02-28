# ePrint Summary

AI-powered tool for tracking and summarizing the latest cryptography papers from the [IACR ePrint Archive](https://eprint.iacr.org/).

## Features

- **Automatic paper fetching** via RSS feed, with backfill mode for catching up
- **AI-powered structured summaries** (research background, contributions, results, techniques)
- **Keyword-based recommendations** to highlight papers matching your interests
- **Markdown reports** organized by year, suitable for reading or sharing
- **Flexible LLM support**: local models (Ollama) or free cloud APIs (Groq, OpenRouter, DeepSeek)
- **Streamlit web UI** + command-line interface

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure

```bash
cp config.example.yaml config.yaml
# Edit config.yaml to set your LLM provider and keywords
```

### 3. Run

**Web UI (Streamlit):**

```bash
streamlit run app.py
```

**Command line:**

```bash
python cli.py                    # Fetch new papers for current year
python cli.py --year 2025        # Specific year
python cli.py --backfill         # Backfill missed papers
python cli.py --dry-run          # Preview without processing
python cli.py --no-summary       # Skip AI summarization
```

## LLM Configuration

The tool supports multiple LLM backends via [litellm](https://github.com/BerriAI/litellm):

| Provider | Model Example | API Key |
|----------|--------------|---------|
| Ollama (local) | `ollama/llama3.2` | Not needed |
| Groq (free tier) | `groq/llama-3.3-70b-versatile` | [Get key](https://console.groq.com/) |
| OpenRouter (free) | `openrouter/deepseek/deepseek-chat-v3-0324:free` | [Get key](https://openrouter.ai/) |
| DeepSeek | `deepseek/deepseek-chat` | [Get key](https://platform.deepseek.com/) |

### Using Ollama (local, no API key needed)

1. Install [Ollama](https://ollama.ai/)
2. Pull a model: `ollama pull llama3.2`
3. Set in `config.yaml`:
   ```yaml
   llm:
     provider: ollama
     model_name: ollama/llama3.2
     api_base: http://localhost:11434
   ```

### Using cloud APIs

Set the API key in `config.yaml` or via environment variable:

```bash
export EPRINT_LLM_API_KEY=your-api-key
```

## Keywords

Configure keywords in `config.yaml` or via the Streamlit UI to highlight papers of interest:

```yaml
keywords:
  - lattice
  - post-quantum
  - homomorphic encryption
  - zero knowledge
  - MPC
```

Papers matching any keyword (case-insensitive, in title/abstract/category) will be marked as **Recommended**.

## Project Structure

```
ePrintSummary/
├── app.py                  # Streamlit web UI
├── cli.py                  # Command-line interface
├── config.example.yaml     # Configuration template
├── requirements.txt        # Python dependencies
├── src/eprint_summary/     # Core library
│   ├── models.py           # Data models (Paper, Summary, Config)
│   ├── fetcher.py          # RSS parsing and paper fetching
│   ├── summarizer.py       # LLM abstraction layer
│   ├── keyword_matcher.py  # Keyword matching logic
│   ├── report.py           # Markdown report generation
│   ├── config_manager.py   # Config and state management
│   └── utils.py            # Shared utilities
├── reports/                # Generated Markdown reports (per year)
└── data/                   # Processing state (state.json)
```

## License

MIT
