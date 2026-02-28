"""Configuration and state management."""

import json
import logging
import os
from pathlib import Path

import yaml

from .models import AppConfig

logger = logging.getLogger(__name__)

# Project root is two levels up from this file (src/eprint_summary/ -> project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def load_config(path: str | Path | None = None) -> AppConfig:
    """Load configuration from YAML file.

    Falls back to config.example.yaml if config.yaml doesn't exist.
    API key can be overridden by EPRINT_LLM_API_KEY environment variable.
    """
    if path is None:
        path = PROJECT_ROOT / "config.yaml"
    else:
        path = Path(path)

    if not path.exists():
        # Fall back to example config
        example_path = PROJECT_ROOT / "config.example.yaml"
        if example_path.exists():
            logger.info("config.yaml not found, using config.example.yaml")
            path = example_path
        else:
            logger.warning("No config file found, using defaults")
            return AppConfig()

    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    config = AppConfig(**raw)

    # Override API key from environment if not set in config
    if config.llm.api_key is None:
        env_key = os.environ.get("EPRINT_LLM_API_KEY")
        if env_key:
            config.llm.api_key = env_key

    # Override email password from environment if not set in config
    if config.email.password is None:
        env_pwd = os.environ.get("EPRINT_EMAIL_PASSWORD")
        if env_pwd:
            config.email.password = env_pwd

    return config


def save_config(config: AppConfig, path: str | Path | None = None) -> None:
    """Save configuration to YAML file."""
    if path is None:
        path = PROJECT_ROOT / "config.yaml"
    else:
        path = Path(path)

    data = config.model_dump()
    # Remove None values for cleaner YAML
    _clean_none(data)

    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    logger.info("Configuration saved to %s", path)


def _clean_none(d: dict) -> None:
    """Recursively remove None values from a dict."""
    keys_to_remove = [k for k, v in d.items() if v is None]
    for k in keys_to_remove:
        del d[k]
    for v in d.values():
        if isinstance(v, dict):
            _clean_none(v)


def load_state(data_dir: str | Path | None = None) -> dict[int, int]:
    """Load processing state (last paper ID per year).

    Returns:
        Dict mapping year (int) to last processed paper number (int).
        e.g., {2026: 392, 2025: 2340}
    """
    if data_dir is None:
        data_dir = PROJECT_ROOT / "data"
    else:
        data_dir = Path(data_dir)

    state_path = data_dir / "state.json"
    if not state_path.exists():
        return {}

    with open(state_path, encoding="utf-8") as f:
        raw = json.load(f)

    # JSON keys are strings, convert to int
    return {int(k): v for k, v in raw.items()}


def save_state(state: dict[int, int], data_dir: str | Path | None = None) -> None:
    """Save processing state."""
    if data_dir is None:
        data_dir = PROJECT_ROOT / "data"
    else:
        data_dir = Path(data_dir)

    data_dir.mkdir(parents=True, exist_ok=True)
    state_path = data_dir / "state.json"

    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    logger.info("State saved: %s", state)
