#!/usr/bin/env python3
"""
Kindle & Local Reading Sync Engine - Universal AI Brain
======================================================
Importa in modo trasparente e a costo zero (0,00€) le sottolineature e le note
dai libri Kindle (file 'My Clippings.txt') all'interno del Connettoma Cognitivo.

Caratteristiche:
1. Parsing ad alte prestazioni del formato standard Amazon Kindle.
2. Deduplicazione idempotente tramite hash MD5 della sottolineatura.
3. Classificazione automatica in Emisfero Sinistro / Destro e Macro-Dominio.
4. Generazione automatica di sinapsi fondative verso 'person-pierfrancesco' e i domini.
"""

import sys
import os
import re
import json
import sqlite3
import hashlib
import argparse
from datetime import datetime, timezone
from typing import List, Dict, Any, Tuple, Optional

DEFAULT_DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))
DEFAULT_KINDLE_LOCATIONS = [
    "/Volumes/Kindle/documents/My Clippings.txt",
    os.path.expanduser("~/Documents/My Clippings.txt"),
    os.path.expanduser("~/Downloads/My Clippings.txt"),
    os.path.expanduser("~/Desktop/My Clippings.txt")
]


def parse_clippings_text(raw_text: str) -> List[Dict[str, Any]]:
    """Analizza il contenuto di My Clippings.txt e restituisce una lista di citazioni strutturate."""
    entries = []
    raw_blocks = raw_text.split("==========")

    for block in raw_blocks:
        lines = [line.strip() for line in block.strip().split("\n") if line.strip()]
        if len(lines) < 2:
            continue

        # Linea 1: Titolo e Autore
        header = lines[0]
        match_author = re.search(r'\((.*?)\)$', header)
        if match_author:
            author = match_author.group(1).strip()
            title = header[:match_author.start()].strip().strip('-–—')
        else:
            author = "Autore Sconosciuto"
            title = header.strip()

        # Linea 2: Metadati (Evidenziazione / Posizione / Data)
        meta_line = lines[1] if len(lines) > 1 else ""
        
        # Linee successive: Testo evidenziato
        content = " ".join(lines[2:]).strip() if len(lines) > 2 else (lines[1] if len(lines) == 2 else "")
        if not content or len(content) < 8:
            continue

        # Genera hash univoco per deduplicazione
        digest = hashlib.md5(f"{title}|{author}|{content}".encode("utf-8")).hexdigest()[:12]

        entries.append({
            "hash": digest,
            "title": title,
            "author": author,
            "meta": meta_line,
            "quote": content
        })

    return entries


def infer_book_category(title: str, author: str, quote: str) -> Tuple[str, str, str]:
    """Inferisce Emisfero, Primary Label e Macro-Dominio dal contenuto del libro."""
    combined = f"{title} {author} {quote}".lower()

    left_keywords = ["programmazione", "software", "architettura", "computer", "algoritmo", "python", "sistema", "finanza", "economia", "investing", "management", "produttività", "matematica", "scienza"]
    right_keywords = ["filosofia", "morale", "stoicismo", "marco aurelio", "seneca", "epitteto", "psicologia", "arte", "design", "vita", "emozione", "relazione", "meditazione", "storia", "cultura"]

    if any(k in combined for k in right_keywords):
        domain = "domain-filosofia-valori" if ("filosofia" in combined or "stoic" in combined or "seneca" in combined) else "domain-crescita-personale"
        return "RIGHT", "LIFE_LESSON", domain
    elif any(k in combined for k in left_keywords):
        domain = "domain-software-engineering" if ("software" in combined or "code" in combined) else "domain-produttivita-sistemi"
        return "LEFT", "MENTAL_MODEL", domain
    else:
        return "RIGHT", "LIFE_LESSON", "domain-crescita-personale"


def sync_kindle_clippings(file_path: str, db_path: str = DEFAULT_DB_PATH, verbose: bool = True) -> Dict[str, Any]:
    """Importa le evidenziazioni Kindle in SQLite con transazione atomica e protezione da duplicati."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File Kindle Clippings non trovato in: {file_path}")

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    clippings = parse_clippings_text(content)
    if not clippings:
        return {"status": "empty", "inserted": 0, "total": 0}

    now = datetime.now(timezone.utc).isoformat()
    inserted_count = 0

    conn = sqlite3.connect(db_path, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")

    with conn:
        for c in clippings:
            slug = f"kindle-{c['hash']}"
            
            # Controllo se già esistente
            exists = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (slug,)).fetchone()
            if exists:
                continue

            hemi, primary_label, domain = infer_book_category(c["title"], c["author"], c["quote"])
            node_label = f"{c['title']} ({c['author']}) - Estratto"
            summary = c["quote"][:300] + ("..." if len(c["quote"]) > 300 else "")
            
            tags_str = json.dumps(["kindle", "lettura", "libro", hemi.lower(), domain.replace("domain-", "")])
            details_str = json.dumps({
                "book_title": c["title"],
                "author": c["author"],
                "full_quote": c["quote"],
                "kindle_meta": c["meta"],
                "imported_by": "kindle_sync_engine"
            })

            # 1. Inserimento Nodo
            conn.execute("""
                INSERT OR REPLACE INTO nodes
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'EXTRACTED', ?, 2, ?, ?)
            """, (
                slug, node_label, hemi, primary_label, "KINDLE_HIGHLIGHT",
                tags_str, summary, details_str, domain, now, now
            ))

            # 2. Archi di collegamento
            conn.execute("""
                INSERT OR REPLACE INTO edges
                (source, target, relation, confidence, reasoning, created_at)
                VALUES (?, 'person-pierfrancesco', 'READ_BY', 'EXTRACTED', 'Evidenziato durante la lettura da Pierfrancesco', ?)
            """, (slug, now))

            domain_exists = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (domain,)).fetchone()
            if domain_exists:
                conn.execute("""
                    INSERT OR REPLACE INTO edges
                    (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, 'BELONGS_TO_DOMAIN', 'EXTRACTED', 'Collegato al macro-dominio del libro', ?)
                """, (slug, domain, now))

            inserted_count += 1

    if verbose:
        print(f"📖 Sincronizzazione Kindle: {inserted_count} nuove sottolineature importate (su {len(clippings)} totali).")

    return {
        "status": "success",
        "inserted": inserted_count,
        "total_in_file": len(clippings)
    }


def find_kindle_file() -> Optional[str]:
    """Cerca automaticamente il file My Clippings.txt nei percorsi noti."""
    for p in DEFAULT_KINDLE_LOCATIONS:
        if os.path.exists(p):
            return p
    return None


def main():
    parser = argparse.ArgumentParser(description="Kindle & Local Reading Sync Engine")
    parser.add_argument("--file", "-f", help="Percorso del file My Clippings.txt")
    parser.add_argument("--db", default=DEFAULT_DB_PATH, help="Percorso database brain.db")
    args = parser.parse_args()

    target_file = args.file or find_kindle_file()
    if not target_file:
        print("❌ Nessun file 'My Clippings.txt' trovato automaticamente.")
        print("Specifica il percorso manualmente con: python3 kindle_sync.py --file /percorso/a/My\\ Clippings.txt")
        sys.exit(1)

    print(f"🔍 File individuato: {target_file}")
    res = sync_kindle_clippings(target_file, db_path=args.db)
    print(f"✅ Completato: {res['inserted']} nodi inseriti nel connettoma.")


if __name__ == "__main__":
    main()
