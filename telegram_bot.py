#!/usr/bin/env python3
"""
Telegram Bot Engine for Universal AI Brain.
Supports long-polling and webhook dispatching for omniscient mobile knowledge access.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
import sqlite3
from typing import Dict, Any, Optional, List
from collections import deque

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "8615414934:AAEGBkrHPQaEestCzHMDSEB6iKyYYTOK7LY").replace(" ", "")
DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def send_telegram_message(chat_id: int, text: str, parse_mode: str = "HTML", reply_markup: Optional[Dict[str, Any]] = None) -> bool:
    """Send a message to Telegram via Bot API."""
    if not TELEGRAM_BOT_TOKEN:
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"[Telegram Bot Error] Failed to send message: {e}", file=sys.stderr)
        return False


def get_main_keyboard() -> Dict[str, Any]:
    """Returns the quick-access keyboard for Telegram mobile clients."""
    return {
        "keyboard": [
            [{"text": "📊 Statistiche Cervello"}, {"text": "🌳 Albero Gerarchico"}],
            [{"text": "🔍 Ricerca Progetti"}, {"text": "⚡ Corpo Calloso"}]
        ],
        "resize_keyboard": True,
        "persistent": True
    }


def process_telegram_message(chat_id: int, user_name: str, text: str) -> str:
    """Process incoming command or natural language thought and generate response."""
    cmd = text.strip()

    # 1. /start or /help
    if cmd in ("/start", "/help", "help"):
        return (
            f"🧠 <b>Benvenuto nel tuo Universal AI Brain, {user_name}!</b>\n\n"
            f"Sei connesso al tuo Grafo di Conoscenza Cognitiva bi-emisferico.\n\n"
            f"<b>Comandi disponibili:</b>\n"
            f"• <code>/stats</code> - Metriche globali (nodi, sinapsi, ponti)\n"
            f"• <code>/search &lt;parola&gt;</code> - Ricerca BM25 istantanea\n"
            f"• <code>/tree</code> - Albero gerarchico per macro-aree\n"
            f"• <code>/path &lt;id1&gt; &lt;id2&gt;</code> - Cammino minimo tra concetti\n"
            f"• <code>/node &lt;id&gt;</code> - Dettaglio nodo e connessioni\n"
            f"• <code>/add &lt;titolo&gt; | &lt;sintesi&gt;</code> - Inserisci nuova memoria\n\n"
            f"<i>Oppure scrivi semplicemente un'idea o appunto per salvarlo al volo!</i>"
        )

    # 2. /stats
    if cmd in ("/stats", "📊 Statistiche Cervello"):
        with get_db() as conn:
            tot = conn.execute("SELECT COUNT(*) AS c FROM nodes").fetchone()["c"]
            left = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere = 'LEFT'").fetchone()["c"]
            right = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere = 'RIGHT'").fetchone()["c"]
            edges = conn.execute("SELECT COUNT(*) AS c FROM edges").fetchone()["c"]
            callosum = conn.execute("SELECT COUNT(*) AS c FROM edges WHERE relation = 'CORPUS_CALLOSUM_LINK'").fetchone()["c"]

            return (
                f"📊 <b>STATO DEL CERVELLO COGNITIVO</b>\n"
                f"────────────────────────\n"
                f"🧠 <b>Nodi Totali:</b> {tot}\n"
                f"⚡ <b>Emisfero Sinistro (Logica/Tech):</b> {left}\n"
                f"🌸 <b>Emisfero Destro (Arte/Emozioni):</b> {right}\n"
                f"🔗 <b>Sinapsi Totali:</b> {edges}\n"
                f"🌌 <b>Ponti Corpo Calloso:</b> {callosum}\n"
                f"────────────────────────\n"
                f"🌐 <i>Web Dashboard:</i> https://universal-ai-brain.onrender.com"
            )

    # 3. /search <query>
    if cmd.startswith("/search") or cmd.startswith("🔍 Ricerca"):
        query = cmd.replace("/search", "").replace("🔍 Ricerca Progetti", "").replace("🔍 Ricerca", "").strip()
        if not query:
            return "⚠️ <i>Uso:</i> <code>/search &lt;termine o tecnologia&gt;</code>\nEsempio: <code>/search flutter</code>"

        with get_db() as conn:
            terms = [f'"{t.replace(chr(34), "")}"*' for t in query.split() if t.strip()]
            match_query = " ".join(terms) if terms else query
            try:
                cursor = conn.execute("""
                    SELECT id FROM nodes_fts
                    WHERE nodes_fts MATCH ?
                    ORDER BY rank
                    LIMIT 5
                """, (match_query,))
                matched_ids = [r["id"] for r in cursor.fetchall()]
            except Exception:
                search_like = f"%{query.lower()}%"
                cursor = conn.execute("""
                    SELECT id FROM nodes
                    WHERE lower(id) LIKE ? OR lower(label) LIKE ? OR lower(summary) LIKE ? OR lower(tags) LIKE ?
                    LIMIT 5
                """, (search_like, search_like, search_like, search_like))
                matched_ids = [r["id"] for r in cursor.fetchall()]

            if not matched_ids:
                return f"🔍 Nessun nodo trovato per <b>'{query}'</b>."

            placeholders = ",".join("?" for _ in matched_ids)
            nodes = conn.execute(f"SELECT * FROM nodes WHERE id IN ({placeholders})", matched_ids).fetchall()

            res_lines = [f"🔍 <b>Risultati per '{query}':</b>\n"]
            for n in nodes:
                hemi_icon = "⚡" if n["hemisphere"] == "LEFT" else "🌸"
                tags = json.loads(n["tags"]) if n["tags"] else []
                tags_str = " ".join(f"#{t}" for t in tags[:3])
                res_lines.append(
                    f"{hemi_icon} <b>{n['label']}</b> (<code>{n['id']}</code>)\n"
                    f"📂 <i>{n['primary_label']}</i> | {tags_str}\n"
                    f"📝 {n['summary']}\n"
                )
            return "\n".join(res_lines)

    # 4. /tree
    if cmd in ("/tree", "🌳 Albero Gerarchico"):
        with get_db() as conn:
            left_tax = conn.execute("SELECT primary_label, COUNT(*) AS c FROM nodes WHERE hemisphere = 'LEFT' GROUP BY primary_label ORDER BY c DESC").fetchall()
            right_tax = conn.execute("SELECT primary_label, COUNT(*) AS c FROM nodes WHERE hemisphere = 'RIGHT' GROUP BY primary_label ORDER BY c DESC").fetchall()

            lines = ["🌳 <b>ALBERO GERARCHICO DI CONOSCENZA</b>\n"]
            lines.append("⚡ <b>Emisfero Sinistro (Logica & Tech):</b>")
            for t in left_tax:
                lines.append(f"  📂 <code>{t['primary_label']}</code>: {t['c']} nodi")
            lines.append("\n🌸 <b>Emisfero Destro (Design, Valori, Emozioni):</b>")
            for t in right_tax:
                lines.append(f"  📂 <code>{t['primary_label']}</code>: {t['c']} nodi")
            lines.append("\n<i>Consulta l'albero completo su:</i>\nhttps://universal-ai-brain.onrender.com/brain.md?view=tree")
            return "\n".join(lines)

    # 5. /path <from> <to>
    if cmd.startswith("/path") or cmd.startswith("⚡ Corpo Calloso"):
        args = cmd.replace("/path", "").replace("⚡ Corpo Calloso", "").strip().split()
        if len(args) < 2:
            return "⚠️ <i>Uso:</i> <code>/path &lt;id_sorgente&gt; &lt;id_destinazione&gt;</code>\nEsempio: <code>/path proj-caretrack lesson-stoic-resilience</code>"
        
        src, tgt = args[0].lower(), args[1].lower()
        with get_db() as conn:
            nodes_rows = conn.execute("SELECT id, label, hemisphere FROM nodes").fetchall()
            nodes_map = {r["id"]: dict(r) for r in nodes_rows}
            if src not in nodes_map or tgt not in nodes_map:
                return f"❌ Uno o entrambi i nodi non esistono: <code>{src}</code>, <code>{tgt}</code>"

            edges_rows = conn.execute("SELECT source, target, relation FROM edges").fetchall()
            adj: Dict[str, List[Dict[str, str]]] = {}
            for r in edges_rows:
                adj.setdefault(r["source"], []).append({"neighbor": r["target"], "rel": r["relation"]})
                adj.setdefault(r["target"], []).append({"neighbor": r["source"], "rel": r["relation"]})

            queue = deque([[src]])
            visited = {src}
            found_path = None
            while queue:
                p = queue.popleft()
                c = p[-1]
                if c == tgt:
                    found_path = p
                    break
                for nbr_info in adj.get(c, []):
                    nbr = nbr_info["neighbor"]
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(p + [nbr])

            if not found_path:
                return f"❌ Nessun percorso sinaptico trovato tra <code>{src}</code> e <code>{tgt}</code>."

            chain = " ➜\n".join(f"• <b>{nodes_map[nid]['label']}</b> (<code>{nid}</code>)" for nid in found_path)
            return (
                f"⚡ <b>CAMMINO SINAPTICO TROVATO (Distanza: {len(found_path)-1})</b>\n"
                f"────────────────────────\n"
                f"{chain}\n"
                f"────────────────────────"
            )

    # 6. /add or free thought insertion
    note_content = cmd.replace("/add", "").strip()
    if not note_content:
        return "⚠️ Invia un testo per registrarlo come nuova memoria nel cervello."

    parts = note_content.split("|")
    title = parts[0].strip()
    summary = parts[1].strip() if len(parts) > 1 else title

    slug = "tg-" + "".join(c if c.isalnum() else "-" for c in title.lower())[:30].strip("-")
    now_iso = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    with get_db() as conn:
        conn.execute("""
            INSERT OR REPLACE INTO nodes
            (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, created_at, updated_at)
            VALUES (?, ?, 'RIGHT', 'CREATIVE_IDEA', 'Telegram Note', ?, ?, ?, 'EXTRACTED', ?, ?)
        """, (
            slug, title,
            json.dumps(["telegram", "mobile-note", "quick-thought"]),
            summary,
            json.dumps({"source": "telegram-bot", "user": user_name}),
            now_iso, now_iso
        ))
        
        # Link to person-pierfrancesco
        if conn.execute("SELECT 1 FROM nodes WHERE id = 'person-pierfrancesco'").fetchone():
            conn.execute("""
                INSERT OR REPLACE INTO edges (source, target, relation, confidence, reasoning, created_at)
                VALUES ('person-pierfrancesco', ?, 'CAPTURED_VIA_TELEGRAM', 'EXTRACTED', 'Mobile thought capture', ?)
            """, (slug, now_iso))

        conn.commit()
        tot = conn.execute("SELECT COUNT(*) AS c FROM nodes").fetchone()["c"]

    return (
        f"✅ <b>MEMORIA SALVATA CON SUCCESSO!</b>\n"
        f"────────────────────────\n"
        f"📌 <b>Titolo:</b> {title}\n"
        f"🔑 <b>ID:</b> <code>{slug}</code>\n"
        f"📂 <b>Categoria:</b> CREATIVE_IDEA (Right Hemisphere)\n"
        f"📝 <b>Sintesi:</b> {summary}\n"
        f"🧠 <b>Nodi totali nel Cervello:</b> {tot}\n"
        f"────────────────────────"
    )


def run_telegram_polling():
    """Run long-polling loop for local interaction."""
    if not TELEGRAM_BOT_TOKEN:
        print("[Telegram Bot] Error: No TELEGRAM_BOT_TOKEN specified.", file=sys.stderr)
        return

    print(f"[Telegram Bot] Starting long-polling service for @pier_brain_ai_bot...")
    last_update_id = 0

    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates?offset={last_update_id + 1}&timeout=30"
            req = urllib.request.urlopen(url, timeout=35)
            data = json.loads(req.read().decode("utf-8"))

            if data.get("ok"):
                for update in data.get("result", []):
                    last_update_id = update["update_id"]
                    msg = update.get("message")
                    if not msg or "text" not in msg:
                        continue

                    chat_id = msg["chat"]["id"]
                    user_name = msg.get("from", {}).get("first_name", "Pierfrancesco")
                    text = msg["text"]

                    print(f"[Telegram Update] From {user_name} ({chat_id}): {text}")
                    reply_text = process_telegram_message(chat_id, user_name, text)
                    send_telegram_message(chat_id, reply_text, reply_markup=get_main_keyboard())

        except Exception as e:
            print(f"[Telegram Polling Loop] Error: {e}", file=sys.stderr)
            time.sleep(3)


if __name__ == "__main__":
    run_telegram_polling()
