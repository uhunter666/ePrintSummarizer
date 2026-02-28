"""Markdown to HTML conversion and email sending."""

import logging
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import markdown

from .models import EmailConfig

logger = logging.getLogger(__name__)

# HTML email template with inline CSS for email client compatibility
HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
}}
h1 {{
    color: #1a5276;
    border-bottom: 2px solid #1a5276;
    padding-bottom: 8px;
}}
h2 {{
    color: #2c3e50;
    margin-top: 30px;
    border-bottom: 1px solid #ddd;
    padding-bottom: 6px;
}}
h3 {{
    color: #34495e;
    margin-top: 20px;
}}
blockquote {{
    border-left: 4px solid #3498db;
    margin: 10px 0;
    padding: 8px 16px;
    background-color: #eaf2f8;
    border-radius: 0 4px 4px 0;
}}
blockquote strong {{
    color: #2c3e50;
}}
a {{
    color: #2980b9;
    text-decoration: none;
}}
a:hover {{
    text-decoration: underline;
}}
hr {{
    border: none;
    border-top: 1px solid #ddd;
    margin: 20px 0;
}}
ul {{
    padding-left: 20px;
}}
li {{
    margin: 4px 0;
}}
em {{
    color: #7f8c8d;
}}
code {{
    background-color: #f0f0f0;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
}}
.recommended {{
    background-color: #fef9e7;
    border-left: 4px solid #f39c12;
    padding: 4px 12px;
    margin: 4px 0;
}}
</style>
</head>
<body>
{content}
</body>
</html>
"""


def convert_md_to_html(md_content: str) -> str:
    """Convert Markdown content to styled HTML for email.

    Args:
        md_content: Markdown text to convert.

    Returns:
        Full HTML document string with inline styles.
    """
    html_body = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "nl2br"],
    )

    # Highlight recommended papers with special styling
    html_body = html_body.replace(
        "[推荐]",
        '<span style="background:#f39c12;color:#fff;padding:2px 6px;border-radius:3px;font-size:0.85em;">推荐</span>',
    )

    return HTML_TEMPLATE.format(content=html_body)


def send_report_email(
    html_content: str,
    subject: str,
    config: EmailConfig,
) -> None:
    """Send an HTML email via SMTP.

    Args:
        html_content: Full HTML document to send as email body.
        subject: Email subject line.
        config: Email configuration (SMTP host, port, sender, etc.).

    Raises:
        ValueError: If email config is incomplete.
        smtplib.SMTPException: If email sending fails.
    """
    if not config.sender:
        raise ValueError("Email sender not configured")
    if not config.recipients:
        raise ValueError("No email recipients configured")
    if not config.password:
        raise ValueError(
            "Email password not configured. "
            "Set it in config.yaml or via EPRINT_EMAIL_PASSWORD env var"
        )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = config.sender
    msg["To"] = ", ".join(config.recipients)

    # Attach HTML content
    msg.attach(MIMEText(html_content, "html", "utf-8"))

    logger.info(
        "Sending email to %s via %s:%d",
        config.recipients,
        config.smtp_host,
        config.smtp_port,
    )

    context = ssl.create_default_context()

    if config.smtp_port == 465:
        # SSL connection
        with smtplib.SMTP_SSL(config.smtp_host, config.smtp_port, context=context) as server:
            server.login(config.sender, config.password)
            server.sendmail(config.sender, config.recipients, msg.as_string())
    else:
        # STARTTLS connection (port 587 or others)
        with smtplib.SMTP(config.smtp_host, config.smtp_port) as server:
            server.starttls(context=context)
            server.login(config.sender, config.password)
            server.sendmail(config.sender, config.recipients, msg.as_string())

    logger.info("Email sent successfully")
