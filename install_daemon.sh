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

RUNNER_BIN="$HOME/.local/bin/universal-brain-daemon"
mkdir -p "$HOME/.local/bin"

cat << EOF > "$RUNNER_BIN"
#!/usr/bin/env bash
REPO_DIR="$REPO_DIR"
cd "\$REPO_DIR" || exit 1
export HOME="$HOME"
export USER="\$(whoami)"
export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:\$HOME/.local/bin"
export RENDER_BRAIN_URL="https://universal-ai-brain.onrender.com"
export PYTHONUNBUFFERED="1"

PYTHON_BIN="\$REPO_DIR/.venv/bin/python3"
if [ ! -f "\$PYTHON_BIN" ]; then
    PYTHON_BIN="\$(which python3)"
fi

exec "\$PYTHON_BIN" "\$REPO_DIR/sync_daemon.py"
EOF

chmod +x "$RUNNER_BIN"

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
        <string>/bin/bash</string>
        <string>$RUNNER_BIN</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>ThrottleInterval</key>
    <integer>10</integer>
    <key>StandardOutPath</key>
    <string>/tmp/sync_daemon.out.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/sync_daemon.err.log</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>HOME</key>
        <string>$HOME</string>
        <key>USER</key>
        <string>$(whoami)</string>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:$HOME/.local/bin</string>
        <key>RENDER_BRAIN_URL</key>
        <string>https://universal-ai-brain.onrender.com</string>
        <key>PYTHONUNBUFFERED</key>
        <string>1</string>
    </dict>
</dict>
</plist>
EOF

chmod 644 "$PLIST_PATH"

# Carica e avvia il LaunchAgent
launchctl bootstrap "gui/$(id -u)" "$PLIST_PATH" 2>/dev/null || launchctl load -w "$PLIST_PATH" 2>/dev/null || true

echo "✅ Demone Universal Brain installato e avviato con successo!"
echo "📄 File LaunchAgent: $PLIST_PATH"
echo "🪵 Log Demone:       $REPO_DIR/sync_daemon.log"
echo "🔍 Stato servizio:   launchctl list | grep universalbrain"
