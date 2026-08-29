#!/usr/bin/env bash
# =============================================================================
# Universal AI Brain - macOS LaunchAgent Uninstaller
# =============================================================================
set -e

PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_NAME="com.universalbrain.sync.plist"
PLIST_PATH="$PLIST_DIR/$PLIST_NAME"

echo "🛑 Disattivazione LaunchAgent Universal AI Brain..."

launchctl bootout "gui/$(id -u)/com.universalbrain.sync" 2>/dev/null || true
launchctl unload "$PLIST_PATH" 2>/dev/null || true

if [ -f "$PLIST_PATH" ]; then
    rm -f "$PLIST_PATH"
    echo "🗑️ Rimosso $PLIST_PATH"
fi

echo "✅ Demone rimosso con successo."
