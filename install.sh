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
        print("─" * 45)
        print(f"• Nodi Totali:              {tot}")
        print(f"• Emisfero Sinistro (⚡):    {left} nodi")
        print(f"• Emisfero Destro   (🌸):    {right} nodi")
        print(f"• Sinapsi Totali:           {edges}")
        print(f"• Ponti Corpo Calloso:      {callosum}")
        print("─" * 45)
        print("🌐 Web: https://universal-ai-brain.onrender.com")

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
            tags = json.loads(n["tags"]) if n["tags"] else []
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
        print("🌳 HIERARCHICAL KNOWLEDGE TREE (層級譜系樹)\n" + "─" * 60)
        curr_h = None
        for r in rows:
            if r["hemisphere"] != curr_h:
                curr_h = r["hemisphere"]
                h_name = "⚡ Emisfero Sinistro (Logica & Tech)" if curr_h == "LEFT" else "🌸 Emisfero Destro (Arte & Valori)"
                print(f"\n{h_name}:")
            print(f"  📂 [{r['primary_label']}] ➜ {r['c']} nodi")
        print("\n🌐 Visualizza albero: https://universal-ai-brain.onrender.com/brain.md?view=tree")

def cmd_add(title: str, summary: str, hemisphere="LEFT", primary_label="ARCHITECTURE"):
    if not title:
        print("Uso: brain add \"Titolo\" \"Sintesi\"")
        return
    slug = "".join(c if c.isalnum() else "-" for c in title.lower())[:30].strip("-")
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with get_db() as conn:
        conn.execute("""
            INSERT OR REPLACE INTO nodes
            (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'EXTRACTED', ?, ?)
        """, (slug, title, hemisphere.upper(), primary_label.upper(), primary_label, json.dumps(["cli-add"]), summary or title, json.dumps({"source": "cli"}), now_iso, now_iso))
        conn.commit()
        tot = conn.execute("SELECT COUNT(*) AS c FROM nodes").fetchone()["c"]
    print(f"✅ Nodo salvato: {title} ({slug}) | Nodi totali: {tot}")

def main():
    if len(sys.argv) < 2:
        print("Uso: brain [search|stats|tree|add|open] <argomenti>")
        return
    cmd = sys.argv[1].lower()
    if cmd in ("stats", "-s"): cmd_stats()
    elif cmd in ("search", "find", "s"): cmd_search(" ".join(sys.argv[2:]))
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
echo "🤖 Installing /brain skill in global agent paths..."
mkdir -p "$SKILLS_DIR" "$GEMINI_SKILLS_DIR" "$RULES_DIR"
cp "$REPO_DIR/skills/universal-brain/SKILL.md" "$SKILLS_DIR/SKILL.md"
cp "$REPO_DIR/skills/universal-brain/SKILL.md" "$GEMINI_SKILLS_DIR/SKILL.md"

# 4. Install Global Rule
cat << 'EOF' > "$RULES_DIR/universal-brain.md"
## Universal AI Brain Integration (/universal-brain)
This workstation is connected to the Universal AI Brain at ~/Desktop/CervelloArtificiale/brain.db.
- Prior Context: Before designing code or architectures, query the brain with `brain_search` or `brain search <query>`.
- Knowledge Capture: Ingest new insights using `brain_ingest` with strict taxonomies (USER_INTENT, AI_REASONING, CONVERSATION_EPISODE, ARCHITECTURE).
EOF

echo "✅ Universal AI Brain successfully installed!"
echo "👉 Prova subito nel terminale: brain stats"
EOF
