#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Aggiungi al Cervello
# @raycast.mode compact

# Optional parameters:
# @raycast.icon ➕
# @raycast.packageName Universal AI Brain
# @raycast.argument1 { "type": "text", "placeholder": "Titolo del concetto..." }
# @raycast.argument2 { "type": "text", "placeholder": "Sintesi / Dettagli (opzionale)", "optional": true }
# @raycast.argument3 { "type": "text", "placeholder": "Emisfero (LEFT/RIGHT, default auto)", "optional": true }

# Documentation:
# @raycast.description Inserimento rapido di nodi e sinapsi nel connettoma cognitivo via Raycast.
# @raycast.author Pierfrancesco Amendola


import sys
import os
import re
import json
import sqlite3
from datetime import datetime, timezone
from typing import Dict, Any, Tuple, Optional

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.expanduser("~/Desktop/CervelloArtificiale/brain.db"))


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'[^a-z0-9-]', '', text)
    return text[:60].strip('-')


def infer_hemisphere_and_domain(title: str, summary: str) -> Tuple[str, str, str]:
    """Determina automaticamente Emisfero, Primary Label e Macro-Dominio."""
    combined = f"{title} {summary}".lower()
    
    # Keyword Emisfero Sinistro (Tech, Architettura, Logica, Algoritmi, Produttività)
    left_tech_keywords = ["fastapi", "python", "sql", "api", "architettura", "database", "mcp", "algoritmo", "git", "codice", "frontend", "backend", "sistema", "linux", "mac", "rete", "test", "docker"]
    left_math_keywords = ["matematica", "calcolo", "statistica", "formula", "finanza", "investimento", "economia", "budget", "costo", "revenue"]
    
    # Keyword Emisfero Destro (Design, Creatività, Filosofia, Emozioni, Relazioni)
    right_design_keywords = ["design", "ui", "ux", "colore", "palette", "layout", "tipografia", "estetica", "brand", "grafica", "arte", "musica"]
    right_valori_keywords = ["valore", "filosofia", "morale", "vita", "crescita", "relazione", "emozione", "lezione", "obiettivo", "abitudine", "stoicismo"]

    if any(k in combined for k in right_design_keywords):
        return "RIGHT", "DESIGN_TOKEN", "domain-design-creativita"
    elif any(k in combined for k in right_valori_keywords):
        return "RIGHT", "PERSONAL_VALUE", "domain-filosofia-valori"
    elif any(k in combined for k in left_math_keywords):
        return "LEFT", "BUSINESS_LOGIC", "domain-finanza-economia"
    elif any(k in combined for k in left_tech_keywords):
        return "LEFT", "ARCHITECTURE", "domain-software-engineering"
    else:
        # Default bilanciato
        return "LEFT", "COGNITIVE_RULE", "domain-ai-cognitive-systems"


def main():
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("❌ Specifica almeno il titolo del nodo.")
        sys.exit(1)

    title = sys.argv[1].strip()
    summary = sys.argv[2].strip() if len(sys.argv) > 2 and sys.argv[2].strip() else title
    hemi_arg = sys.argv[3].strip().upper() if len(sys.argv) > 3 and sys.argv[3].strip() else None

    # Determinazione metadati
    auto_hemi, primary_label, domain = infer_hemisphere_and_domain(title, summary)
    hemisphere = hemi_arg if hemi_arg in ("LEFT", "RIGHT") else auto_hemi

    now = datetime.now(timezone.utc).isoformat()
    slug_id = f"node-{slugify(title)}"

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
            # 1. Inserimento Nodo
            tags_json = json.dumps(["raycast-quick-add", hemisphere.lower(), domain.replace("domain-", "")])
            details_json = json.dumps({"source": "raycast_quick_add", "created_by": "Pierfrancesco Amendola"})

            conn.execute("""
                INSERT OR REPLACE INTO nodes
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'EXTRACTED', ?, 2, ?, ?)
            """, (
                slug_id, title, hemisphere, primary_label, primary_label,
                tags_json, summary, details_json, domain, now, now
            ))

            # 2. Inserimento Archi Fondativi
            conn.execute("""
                INSERT OR REPLACE INTO edges
                (source, target, relation, confidence, reasoning, created_at)
                VALUES (?, 'person-pierfrancesco', 'EXPRESSED_BY', 'EXTRACTED', 'Inserito da Pierfrancesco via Raycast', ?)
            """, (slug_id, now))

            # Verifica esistenza del dominio prima di collegarlo
            cur = conn.cursor()
            cur.execute("SELECT id FROM nodes WHERE id = ?", (domain,))
            if cur.fetchone():
                conn.execute("""
                    INSERT OR REPLACE INTO edges
                    (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, 'BELONGS_TO_DOMAIN', 'EXTRACTED', 'Collegato al macro-dominio tematico', ?)
                """, (slug_id, domain, now))

        hemi_icon = "⚡" if hemisphere == "LEFT" else "🌸"
        print(f"✅ {hemi_icon} Salvato nel Cervello: \"{title}\" ({hemisphere} | {domain})")

    except Exception as e:
        print(f"❌ Errore durante l'inserimento: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
