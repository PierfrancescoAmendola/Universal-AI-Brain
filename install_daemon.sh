#!/usr/bin/env bash
# =============================================================================
# Universal AI Brain - macOS LaunchAgent Installer
# Configures sync_daemon.py to run automatically at user login / system boot.
# =============================================================================
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLIST_DIR="$HOME/Library/LaunchAgents"
PLIST_NAME="com.universalbrain.sync.plist"
PLIST_PATH="$PLIST_DIR/$PLIST_NAME"
PYTHON_BIN="$REPO_DIR/.venv/bin/python3"

if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="$(which python3)"
fi

echo "🚀 Installazione macOS LaunchAgent per Universal AI Brain..."

mkdir -p "$PLIST_DIR"

# Scarica eventuale servizio attivo precedente
launchctl bootout "gui/$(id -u)/com.universalbrain.sync" 2>/dev/null || true
launchctl unload "$PLIST_PATH" 2>/dev/null || true

# Genera il file .plist
cat << EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.universalbrain.sync</string>
    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON_BIN</string>
        <string>$REPO_DIR/sync_daemon.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>$REPO_DIR</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>$REPO_DIR/sync_daemon.out.log</string>
    <key>StandardErrorPath</key>
    <string>$REPO_DIR/sync_daemon.err.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$HOME/.local/bin</string>
    </dict>
</dict>
</plist>
EOF

chmod 644 "$PLIST_PATH"

# Carica e avvia il LaunchAgent
launchctl bootstrap "gui/$(id -u)" "$PLIST_PATH" 2>/dev/null || launchctl load "$PLIST_PATH"

echo "✅ Demone Universal Brain installato e avviato con successo!"
echo "📄 File LaunchAgent: $PLIST_PATH"
echo "🪵 Log Demone:       $REPO_DIR/sync_daemon.log"
echo "🔍 Stato servizio:   launchctl list | grep universalbrain"
