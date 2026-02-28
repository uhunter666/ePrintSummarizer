"""Daily scheduler for ePrint Summary tool.

Runs the paper fetching and summarization pipeline once daily at a configured time,
then sends HTML report to the specified email addresses.

Usage:
    python scheduler.py                 # Start the scheduler
    nohup python scheduler.py &         # Run in background
    python scheduler.py --run-now       # Run once immediately, then start scheduling
"""

import argparse
import logging
import sys
import time
from datetime import datetime
from pathlib import Path

import schedule

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from eprint_summary.config_manager import load_config
from eprint_summary.utils import setup_logging

logger = logging.getLogger(__name__)


def daily_job(config_path: str | None = None):
    """Execute the daily paper fetching and email pipeline."""
    # Re-load config each run so changes take effect without restart
    config = load_config(config_path)

    logger.info("=== Daily job started at %s ===", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # Import here to avoid circular imports and ensure fresh state
    from cli import run_pipeline

    try:
        results = run_pipeline(
            config=config,
            send_email=True,
            quiet=False,
        )
        if results:
            logger.info("Daily job completed: %d papers processed", len(results))
        else:
            logger.info("Daily job completed: no new papers")
    except Exception as e:
        logger.error("Daily job failed: %s", e, exc_info=True)

    logger.info("=== Daily job finished ===\n")


def main():
    parser = argparse.ArgumentParser(
        description="ePrint Summary Scheduler - Run daily paper fetching and email"
    )
    parser.add_argument(
        "--run-now",
        action="store_true",
        help="Run the pipeline once immediately before starting the scheduler",
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to config.yaml (default: ./config.yaml)",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    setup_logging(config.log_level)

    schedule_time = config.schedule.time

    print(f"ePrint Summary Scheduler")
    print(f"========================")
    print(f"Schedule: daily at {schedule_time}")
    print(f"Email enabled: {config.email.enabled}")
    if config.email.enabled:
        print(f"Recipients: {', '.join(config.email.recipients)}")
    print(f"LLM: {config.llm.model_name}")
    print(f"Keywords: {', '.join(config.keywords)}")
    if config.exclude_keywords:
        print(f"Exclude: {', '.join(config.exclude_keywords)}")
    print()

    if args.run_now:
        print("Running pipeline now...")
        daily_job(args.config)

    # Schedule the daily job
    schedule.every().day.at(schedule_time).do(daily_job, config_path=args.config)

    next_run = schedule.next_run()
    print(f"Next scheduled run: {next_run}")
    print(f"Waiting... (Ctrl+C to stop)\n")

    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


if __name__ == "__main__":
    main()
