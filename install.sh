#!/usr/bin/env bash
# =============================================================================
# Universal AI Brain - 1-Click Universal Installer & MCP Configurator
# =============================================================================
set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="$HOME/.local/bin"
SKILLS_DIR="$HOME/.agents/skills/universal-brain"
GEMINI_SKILLS_DIR="$HOME/.gemini/config/skills/universal-brain"
RULES_DIR="$HOME/.agents/rules"

echo "🧠 Starting Universal AI Brain Global Installation..."

# 1. Setup Virtualenv & Dependencies
echo "📦 Setting up Python virtual environment..."
if [ ! -d "$REPO_DIR/.venv" ]; then
    python3 -m venv "$REPO_DIR/.venv"
fi
"$REPO_DIR/.venv/bin/pip" install -q -r "$REPO_DIR/requirements.txt"

# 2. Install CLI tool
echo "⚡ Installing global 'brain' CLI command in $BIN_DIR..."
mkdir -p "$BIN_DIR"
cp "$BIN_DIR/brain" "$BIN_DIR/brain.bak" 2>/dev/null || true

cat << 'EOF' > "$BIN_DIR/brain"
#!/usr/bin/env python3
import sys, os, json, sqlite3, time, subprocess

BRAIN_DIR = os.path.expanduser("~/Desktop/CervelloArtificiale")
DB_PATH = os.path.join(BRAIN_DIR, "brain.db")
PYTHON_BIN = os.path.join(BRAIN_DIR, ".venv", "bin", "python3")
if not os.path.exists(PYTHON_BIN):
    PYTHON_BIN = sys.executable

def get_db():
    if not os.path.exists(DB_PATH):
        print(f"❌ Error: Database not found at {DB_PATH}", file=sys.stderr)
        sys.exit(1)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def cmd_stats():
    with get_db() as conn:
        tot = conn.execute("SELECT COUNT(*) AS c FROM nodes").fetchone()["c"]
        left = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere = 'LEFT'").fetchone()["c"]
        right = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere = 'RIGHT'").fetchone()["c"]
        edges = conn.execute("SELECT COUNT(*) AS c FROM edges").fetchone()["c"]
        callosum = conn.execute("SELECT COUNT(*) AS c FROM edges WHERE relation = 'CORPUS_CALLOSUM_LINK'").fetchone()["c"]
        print("🧠 UNIVERSAL AI BRAIN - STATISTICHE GLOBALI")
        print("─" * 50)
        print(f"• Nodi Totali (Locale):     {tot}")
        print(f"• Emisfero Sinistro (⚡):    {left} nodi")
        print(f"• Emisfero Destro   (🌸):    {right} nodi")
        print(f"• Sinapsi Totali:           {edges}")
        print(f"• Ponti Corpo Calloso:      {callosum}")
        print("─" * 50)
        print("🌐 Web Cloud: https://universal-ai-brain.onrender.com")

def cmd_search(query: str):
    if not query:
        print("Uso: brain search <parola>")
        return
    with get_db() as conn:
        terms = [f'"{t.replace(chr(34), "")}"*' for t in query.split() if t.strip()]
        match_query = " ".join(terms) if terms else query
        try:
            cursor = conn.execute("SELECT id FROM nodes_fts WHERE nodes_fts MATCH ? ORDER BY rank LIMIT 8", (match_query,))
            matched_ids = [r["id"] for r in cursor.fetchall()]
        except Exception:
            search_like = f"%{query.lower()}%"
            cursor = conn.execute("SELECT id FROM nodes WHERE lower(id) LIKE ? OR lower(label) LIKE ? OR lower(summary) LIKE ? OR lower(tags) LIKE ? LIMIT 8", (search_like, search_like, search_like, search_like))
            matched_ids = [r["id"] for r in cursor.fetchall()]

        if not matched_ids:
            print(f"🔍 Nessun nodo trovato per '{query}'.")
            return

        placeholders = ",".join("?" for _ in matched_ids)
        nodes = conn.execute(f"SELECT * FROM nodes WHERE id IN ({placeholders})", matched_ids).fetchall()
        print(f"🔍 Risultati per '{query}' ({len(nodes)} trovati):\n" + "─" * 60)
        for n in nodes:
            icon = "⚡" if n["hemisphere"] == "LEFT" else "🌸"
            tags = json.loads(n["tags"]) if n["tags"] and n["tags"].startswith("[") else []
            tags_str = " ".join(f"#{t}" for t in tags[:4])
            print(f"{icon} {n['label']} ({n['id']})\n   📂 [{n['primary_label']}]  {tags_str}\n   📝 {n['summary']}\n")

def cmd_tree(hemisphere=None):
    with get_db() as conn:
        query = "SELECT primary_label, hemisphere, COUNT(*) AS c FROM nodes"
        params = []
        if hemisphere and hemisphere.upper() in ("LEFT", "RIGHT"):
            query += " WHERE hemisphere = ?"
            params.append(hemisphere.upper())
        query += " GROUP BY hemisphere, primary_label ORDER BY hemisphere, c DESC"
        rows = conn.execute(query, params).fetchall()
        print("🌳 HIERARCHICAL KNOWLEDGE TREE\n" + "─" * 60)
        curr_h = None
        for r in rows:
            if r["hemisphere"] != curr_h:
                curr_h = r["hemisphere"]
                h_name = "⚡ Emisfero Sinistro (Logica & Tech)" if curr_h == "LEFT" else "🌸 Emisfero Destro (Arte & Valori)"
                print(f"\n{h_name}:")
            print(f"  📂 [{r['primary_label']}] ➜ {r['c']} nodi")
        print("\n🌐 Visualizza albero: https://universal-ai-brain.onrender.com/brain.md?view=tree")

def cmd_sync():
    sync_script = os.path.join(BRAIN_DIR, "sync_brain.py")
    subprocess.run([PYTHON_BIN, sync_script], cwd=BRAIN_DIR)

def cmd_record(args):
    sync_script = os.path.join(BRAIN_DIR, "sync_brain.py")
    cmd = [PYTHON_BIN, sync_script, "--record"] + args
    subprocess.run(cmd, cwd=BRAIN_DIR)

def cmd_daemon(action="status"):
    if action in ("status", "info"):
        out = subprocess.run(["launchctl", "list"], capture_output=True, text=True)
        found = False
        for line in out.stdout.splitlines():
            if "universalbrain" in line:
                print(f"🟢 Daemon Status: ATTIVO ({line})")
                found = True
        if not found:
            print("🔴 Daemon Status: NON ATTIVO. Avvialo con: brain daemon start")
    elif action == "start":
        subprocess.run([os.path.join(BRAIN_DIR, "install_daemon.sh")])
    elif action == "stop":
        subprocess.run([os.path.join(BRAIN_DIR, "uninstall_daemon.sh")])
    elif action == "restart":
        subprocess.run([os.path.join(BRAIN_DIR, "install_daemon.sh")])
    elif action in ("logs", "log"):
        log_file = os.path.join(BRAIN_DIR, "sync_daemon.log")
        if os.path.exists(log_file):
            subprocess.run(["tail", "-n", "30", "-f", log_file])
        else:
            print(f"Nessun file di log trovato in {log_file}")
    else:
        print("Uso: brain daemon [status|start|stop|restart|logs]")

def cmd_add(title: str, summary: str, hemisphere="LEFT", primary_label="ARCHITECTURE"):
    if not title:
        print("Uso: brain add \"Titolo\" \"Sintesi\"")
        return
    slug = "".join(c if c.isalnum() else "-" for c in title.lower())[:30].strip("-")
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with get_db() as conn:
        conn.execute("""
            INSERT OR REPLACE INTO nodes
            (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'EXTRACTED', 'root', 1, ?, ?)
        """, (slug, title, hemisphere.upper(), primary_label.upper(), primary_label, json.dumps(["cli-add"]), summary or title, json.dumps({"source": "cli"}), now_iso, now_iso))
        conn.commit()
        tot = conn.execute("SELECT COUNT(*) AS c FROM nodes").fetchone()["c"]
    print(f"✅ Nodo salvato: {title} ({slug}) | Nodi totali: {tot}")
    # Trigger auto-sync
    cmd_sync()

def main():
    if len(sys.argv) < 2:
        print("🧠 Universal AI Brain CLI")
        print("Uso:")
        print("  brain stats                 - Statistiche del connettoma")
        print("  brain search <query>        - Ricerca GraphRAG FTS5")
        print("  brain sync                  - Sincronizzazione bidirezionale immediata con Render")
        print("  brain record --topic ...    - Registrazione veloce sessione di chat")
        print("  brain daemon [status|logs]  - Gestione del demone in background macOS")
        print("  brain tree [LEFT|RIGHT]     - Visualizza albero di conoscenza")
        print("  brain add <titolo> <sintesi>- Aggiungi nuovo nodo")
        print("  brain open                  - Apri Web Dashboard")
        return
    cmd = sys.argv[1].lower()
    if cmd in ("stats", "-s"): cmd_stats()
    elif cmd in ("search", "find", "s"): cmd_search(" ".join(sys.argv[2:]))
    elif cmd in ("sync", "pull", "push"): cmd_sync()
    elif cmd in ("record", "save-session"): cmd_record(sys.argv[2:])
    elif cmd in ("daemon", "service", "d"): cmd_daemon(sys.argv[2] if len(sys.argv) > 2 else "status")
    elif cmd in ("tree", "t"): cmd_tree(sys.argv[2] if len(sys.argv) > 2 else None)
    elif cmd in ("add", "save", "a"): cmd_add(sys.argv[2] if len(sys.argv) > 2 else "", sys.argv[3] if len(sys.argv) > 3 else "")
    elif cmd in ("open", "web"):
        import webbrowser
        webbrowser.open("https://universal-ai-brain.onrender.com")
    else: cmd_search(" ".join(sys.argv[1:]))

if __name__ == "__main__":
    main()
EOF

chmod +x "$BIN_DIR/brain"

# 3. Install Skill Files
echo "🤖 Installing /universal-brain skill in global agent paths..."
mkdir -p "$SKILLS_DIR" "$GEMINI_SKILLS_DIR" "$RULES_DIR"
cp "$REPO_DIR/skills/universal-brain/SKILL.md" "$SKILLS_DIR/SKILL.md"
cp "$REPO_DIR/skills/universal-brain/SKILL.md" "$GEMINI_SKILLS_DIR/SKILL.md"

# 4. Install Background Daemon
echo "🚀 Configuring Background LaunchAgent Daemon..."
"$REPO_DIR/install_daemon.sh"

echo "✅ Universal AI Brain successfully installed and configured!"
echo "👉 Prova subito nel terminale: brain stats"
