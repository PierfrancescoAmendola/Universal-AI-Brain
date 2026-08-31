#!/usr/bin/env bash
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"
export HOME="/Users/pierfrancesco"
export USER="pierfrancesco"
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$HOME/.local/bin"
export RENDER_BRAIN_URL="https://universal-ai-brain.onrender.com"
export PYTHONUNBUFFERED="1"

PYTHON_BIN="$REPO_DIR/.venv/bin/python3"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="$(which python3)"
fi

exec "$PYTHON_BIN" "$REPO_DIR/sync_daemon.py"
