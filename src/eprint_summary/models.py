"""Pydantic data models for ePrint Summary."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Paper(BaseModel):
    """Represents a single ePrint paper."""

    paper_id: str  # e.g., "2026/380"
    year: int
    number: int
    title: str
    authors: list[str]
    abstract: str
    category: str = "Unknown"
    keywords: list[str] = Field(default_factory=list)
    url: str  # https://eprint.iacr.org/2026/380
    pdf_url: str  # https://eprint.iacr.org/2026/380.pdf
    published_date: Optional[datetime] = None


class Summary(BaseModel):
    """Structured summary of a paper's abstract."""

    background: str = ""
    contributions: str = ""
    results: str = ""
    techniques: str = ""


class PaperWithSummary(BaseModel):
    """A paper combined with its AI-generated summary and keyword match info."""

    paper: Paper
    summary: Summary
    is_keyword_match: bool = False
    matched_keywords: list[str] = Field(default_factory=list)


class LLMConfig(BaseModel):
    """Configuration for the LLM backend."""

    provider: str = "ollama"
    model_name: str = "ollama/qwen2.5:7b"
    api_base: Optional[str] = "http://localhost:11434"
    api_key: Optional[str] = None
    temperature: float = 0.3
    max_tokens: int = 1024
    request_delay: float = 1.0


class EmailConfig(BaseModel):
    """Email sending configuration."""

    enabled: bool = False
    smtp_host: str = "smtp.qq.com"
    smtp_port: int = 465
    sender: str = ""
    password: Optional[str] = None
    recipients: list[str] = Field(default_factory=list)


class ScheduleConfig(BaseModel):
    """Daily scheduling configuration."""

    enabled: bool = False
    time: str = "09:00"


class AppConfig(BaseModel):
    """Application-level configuration."""

    llm: LLMConfig = Field(default_factory=LLMConfig)
    keywords: list[str] = Field(default_factory=list)
    exclude_keywords: list[str] = Field(default_factory=list)
    target_year: Optional[int] = None
    reports_dir: str = "reports"
    data_dir: str = "data"
    enrich_keywords: bool = False
    log_level: str = "INFO"
    email: EmailConfig = Field(default_factory=EmailConfig)
    schedule: ScheduleConfig = Field(default_factory=ScheduleConfig)
