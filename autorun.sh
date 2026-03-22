#!/bin/bash
# ePrint Summary: fetch new papers and push reports to GitHub
# Runs cli.py to fetch/summarize papers, then git pushes updated reports.

set -euo pipefail

PROJECT_DIR="/home/lym/ClaudeProjects/ePrintSummary"
LOG_FILE="$PROJECT_DIR/logs/autorun.log"

mkdir -p "$PROJECT_DIR/logs"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

cd "$PROJECT_DIR"

log "=== autorun started ==="

# Wait for network (max 60s)
for i in $(seq 1 12); do
    if ping -c1 -W2 eprint.iacr.org &>/dev/null; then
        break
    fi
    sleep 5
done

# Run the pipeline
log "Running cli.py ..."
if python cli.py >> "$LOG_FILE" 2>&1; then
    log "cli.py finished successfully"
else
    log "cli.py failed with exit code $?"
fi

# Push updated reports to GitHub
if git -C "$PROJECT_DIR" diff --quiet reports/; then
    log "No report changes to push"
else
    log "Pushing updated reports to GitHub ..."
    git -C "$PROJECT_DIR" add reports/
    git -C "$PROJECT_DIR" commit -m "Auto-update reports $(date '+%Y-%m-%d')"
    if git -C "$PROJECT_DIR" push origin main >> "$LOG_FILE" 2>&1; then
        log "Push succeeded"
    else
        log "Push failed with exit code $?"
    fi
fi

log "=== autorun finished ==="
