#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Cattura Appunti nel Cervello
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 📋
# @raycast.packageName Universal AI Brain
# @raycast.argument1 { "type": "text", "placeholder": "Titolo personalizzato (opzionale)", "optional": true }

# Documentation:
# @raycast.description Cattura il contenuto degli appunti di sistema e lo salva nel connettoma cognitivo.
# @raycast.author Pierfrancesco Amendola


import sys
import os
import re
import json
import sqlite3
import subprocess
from datetime import datetime, timezone
from typing import Dict, Any, Tuple

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.expanduser("~/Desktop/CervelloArtificiale/brain.db"))


def get_clipboard_text() -> str:
    """Legge il contenuto testuale della clipboard di macOS via pbpaste."""
    try:
        res = subprocess.check_output(["pbpaste"], text=True, timeout=3.0)
        return res.strip()
    except Exception as e:
        return ""


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^a-z0-9-]', '', text)
    return text[:60].strip('-')


def infer_metadata(text: str) -> Tuple[str, str, str, str]:
    """Estrae titolo sintetico, riassunto, emisfero e macro-dominio."""
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    if not lines:
        return "Appunto Catturato", "Nessun contenuto.", "LEFT", "domain-produttivita-sistemi"
    
    first_line = lines[0]
    title = first_line[:70] if len(first_line) > 70 else first_line
    summary = text[:300] + ("..." if len(text) > 300 else "")

    combined = text.lower()
    left_keywords = ["def ", "class ", "function", "http", "api", "const ", "import ", "sql", "git", "bash", "curl", "json", "python", "javascript", "docker"]
    right_keywords = ["design", "colore", "valore", "ispirazione", "filosofia", "idea", "creatività", "pensiero", "obiettivo", "abitudine"]

    if any(k in combined for k in right_keywords):
        return title, summary, "RIGHT", "domain-filosofia-valori"
    elif any(k in combined for k in left_keywords):
        return title, summary, "LEFT", "domain-software-engineering"
    else:
        return title, summary, "LEFT", "domain-ai-cognitive-systems"


def main():
    custom_title = sys.argv[1].strip() if len(sys.argv) > 1 and sys.argv[1].strip() else None
    clipboard_content = get_clipboard_text()

    if not clipboard_content:
        print("❌ Gli appunti di macOS sono vuoti. Copia del testo prima di eseguire.")
        sys.exit(1)

    inferred_title, summary, hemisphere, domain = infer_metadata(clipboard_content)
    final_title = custom_title if custom_title else inferred_title
    primary_label = "ARCHITECTURE" if hemisphere == "LEFT" else "CREATIVE_IDEA"

    now = datetime.now(timezone.utc).isoformat()
    slug_id = f"clip-{slugify(final_title)}-{int(datetime.now().timestamp()) % 10000}"

    if not os.path.exists(DEFAULT_DB_PATH):
        print(f"❌ Database non trovato in `{DEFAULT_DB_PATH}`")
        sys.exit(1)

    try:
        conn = sqlite3.connect(DEFAULT_DB_PATH, timeout=5.0)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA busy_timeout=5000;")
        conn.execute("PRAGMA foreign_keys=ON;")

        with conn:
            tags_json = json.dumps(["clipboard-capture", hemisphere.lower(), domain.replace("domain-", "")])
            details_json = json.dumps({
                "source": "macos_clipboard",
                "raw_text": clipboard_content[:2000],
                "created_by": "Pierfrancesco Amendola"
            })

            # Inserimento Nodo
            conn.execute("""
                INSERT OR REPLACE INTO nodes
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'EXTRACTED', ?, 2, ?, ?)
            """, (
                slug_id, final_title, hemisphere, primary_label, primary_label,
                tags_json, summary, details_json, domain, now, now
            ))

            # Archi di collegamento
            conn.execute("""
                INSERT OR REPLACE INTO edges
                (source, target, relation, confidence, reasoning, created_at)
                VALUES (?, 'person-pierfrancesco', 'EXPRESSED_BY', 'EXTRACTED', 'Catturato dagli appunti di Pierfrancesco', ?)
            """, (slug_id, now))

            cur = conn.cursor()
            cur.execute("SELECT id FROM nodes WHERE id = ?", (domain,))
            if cur.fetchone():
                conn.execute("""
                    INSERT OR REPLACE INTO edges
                    (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, 'BELONGS_TO_DOMAIN', 'EXTRACTED', 'Collegato al macro-dominio tematico', ?)
                """, (slug_id, domain, now))

        hemi_icon = "⚡" if hemisphere == "LEFT" else "🌸"
        print(f"✅ {hemi_icon} Appunti Catturati: \"{final_title}\" ({len(clipboard_content)} caratteri)")

    except Exception as e:
        print(f"❌ Errore durante la cattura: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
