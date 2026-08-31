#!/usr/bin/env python3
"""
Universal AI Brain - Advanced Bi-Directional Cloud Sync & Ingestion Engine
Handles seamless two-way synchronization between local SQLite (brain.db) and Render Cloud (https://universal-ai-brain.onrender.com).
Includes 1-command session context ingestion (USER_INTENT, AI_REASONING, CONVERSATION_EPISODE).
"""

import sys
import os
import re
import json
import time
import sqlite3
import urllib.request
import urllib.error
import subprocess
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Tuple

RENDER_URL = os.getenv("RENDER_BRAIN_URL", "https://universal-ai-brain.onrender.com")
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_DB = os.path.join(LOCAL_DIR, "brain.db")
BRAIN_MD = os.path.join(LOCAL_DIR, "brain.md")


def get_local_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(LOCAL_DB, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def slugify(text: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z0-9\s-]', '', text.lower())
    slug = re.sub(r'[\s_]+', '-', cleaned).strip('-')
    return slug[:45] if slug else "untitled"


def fetch_render_data(timeout: int = 35, retries: int = 3) -> Optional[Dict[str, Any]]:
    url = f"{RENDER_URL}/brain.json"
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "UniversalBrainSync/2.0"}
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as e:
            if attempt < retries:
                time.sleep(4)
            else:
                print(f"⚠️ Impossibile raggiungere Render ({url}) dopo {retries} tentativi: {e}")
                return None
    return None


def push_to_render(payload: Dict[str, Any], timeout: int = 35, retries: int = 2) -> bool:
    url = f"{RENDER_URL}/api/memory/ingest"
    for attempt in range(1, retries + 1):
        try:
            data_bytes = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                url,
                data=data_bytes,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "UniversalBrainSync/2.0"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=timeout) as response:
                res_json = json.loads(response.read().decode("utf-8"))
                return res_json.get("success", True)
        except Exception as e:
            if attempt < retries:
                time.sleep(3)
            else:
                print(f"⚠️ Errore durante il push verso Render ({url}): {e}")
                return False
    return False


def export_brain_markdown():
    """Generates and writes brain.md from the local database."""
    try:
        from main import get_brain_markdown
        res = get_brain_markdown()
        with open(BRAIN_MD, "w", encoding="utf-8") as f:
            f.write(res.body.decode("utf-8"))
    except Exception:
        # Fallback simple markdown generator
        with get_local_connection() as conn:
            nodes = conn.execute("SELECT * FROM nodes ORDER BY hemisphere, primary_label, label").fetchall()
            edges = conn.execute("SELECT * FROM edges ORDER BY relation, source").fetchall()
            with open(BRAIN_MD, "w", encoding="utf-8") as f:
                f.write(f"# Universal AI Brain - Connettoma Neurale\n\n- **Nodi:** {len(nodes)}\n- **Sinapsi:** {len(edges)}\n\n")
                for n in nodes:
                    f.write(f"### {n['label']} (`{n['id']}`)\n- **Emisfero:** {n['hemisphere']} | **Taxonomy:** {n['primary_label']}\n- **Sintesi:** {n['summary']}\n\n")


def git_commit_and_push(commit_msg: str) -> bool:
    """Flushes WAL, updates brain.md, commits brain.db and brain.md and pushes to origin main for cloud persistence."""
    try:
        with get_local_connection() as conn:
            conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
        export_brain_markdown()

        subprocess.run(["git", "add", "brain.db", "brain.md"], cwd=LOCAL_DIR, check=True, capture_output=True)
        st = subprocess.run(["git", "status", "--porcelain", "brain.db", "brain.md"], cwd=LOCAL_DIR, capture_output=True, text=True)
        if st.stdout.strip():
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=LOCAL_DIR, check=True, capture_output=True)
            # Rebase before push to avoid non-fast-forward push failures
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], cwd=LOCAL_DIR, capture_output=True, text=True)
            push_res = subprocess.run(["git", "push", "origin", "main"], cwd=LOCAL_DIR, capture_output=True, text=True)
            if push_res.returncode == 0:
                print("🚀 Git commit & push completati con successo su origin/main.")
                return True
            else:
                print(f"⚠️ Git push fallito: {push_res.stderr.strip()}")
                return False
        return False
    except Exception as e:
        print(f"⚠️ Git push non riuscito o già allineato: {e}")
        return False


def sync_bidirectional(verbose: bool = True) -> Dict[str, Any]:
    """
    Complete lossless two-way synchronization:
    1. Ensures local uncommitted SQLite changes are checkpointed and pushed to Git.
    2. Pulls new nodes/edges from Render into local brain.db.
    3. Pushes local new nodes/edges to Render via REST POST.
    4. Flushes WAL, updates brain.md, and pushes to Git repository.
    """
    if verbose:
        print("🔄 Inizio Sincronizzazione Bidirezionale (PC ⮂ Render Cloud)...")

    # Step 0: Assicura che le modifiche locali non committate vadano subito su Git
    git_commit_and_push("feat(sync): salvataggio locale automatico connettoma")

    render_data = fetch_render_data()
    if not render_data:
        if verbose:
            print("⚠️ Connessione a Render non disponibile (in standby o offline). Opero solo su database locale e Git.")
        with get_local_connection() as conn:
            curr_nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
            curr_edges = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        return {
            "success": True,
            "nodes_count": curr_nodes,
            "edges_count": curr_edges,
            "pulled_nodes": 0,
            "pushed_nodes": 0,
            "warning": "Render in standby"
        }

    render_nodes = {n["id"]: n for n in render_data.get("nodes", [])}
    render_edges_list = render_data.get("links", [])
    render_edges = {(e["source"], e["target"], e.get("relation", "CONNECTS_TO")): e for e in render_edges_list}

    with get_local_connection() as conn:
        local_nodes_rows = conn.execute("SELECT * FROM nodes").fetchall()
        local_nodes = {r["id"]: dict(r) for r in local_nodes_rows}

        local_edges_rows = conn.execute("SELECT * FROM edges").fetchall()
        local_edges = {(r["source"], r["target"], r["relation"]): dict(r) for r in local_edges_rows}

    # 1. Trova differenze
    only_in_render_nodes = [render_nodes[nid] for nid in render_nodes if nid not in local_nodes]
    only_in_render_edges = [render_edges[k] for k in render_edges if k not in local_edges]

    only_in_local_nodes = [local_nodes[nid] for nid in local_nodes if nid not in render_nodes]
    only_in_local_edges = [local_edges[k] for k in local_edges if k not in render_edges]

    if verbose:
        print(f"📊 Stato Locale: {len(local_nodes)} nodi, {len(local_edges)} archi | Render: {len(render_nodes)} nodi, {len(render_edges)} archi")
        print(f"📥 Da scaricare da Render: {len(only_in_render_nodes)} nodi, {len(only_in_render_edges)} archi")
        print(f"📤 Da caricare su Render:  {len(only_in_local_nodes)} nodi, {len(only_in_local_edges)} archi")

    changes_made = False

    # 2. Inserimento locale dei nodi scaricati da Render (Pull) con batch executemany
    if only_in_render_nodes or only_in_render_edges:
        now = datetime.now(timezone.utc).isoformat()
        with get_local_connection() as conn:
            if only_in_render_nodes:
                node_tuples = []
                for n in only_in_render_nodes:
                    tags_str = json.dumps(n.get("tags", [])) if isinstance(n.get("tags"), list) else n.get("tags", "[]")
                    details_str = json.dumps(n.get("details", {})) if isinstance(n.get("details"), dict) else str(n.get("details", "{}"))
                    node_tuples.append((
                        n["id"], n["label"], n.get("hemisphere", "LEFT"),
                        n.get("primary_label", n.get("category", "ARCHITECTURE")),
                        n.get("category", "ARCHITECTURE"),
                        tags_str, n.get("summary", ""), details_str,
                        n.get("confidence", "EXTRACTED"),
                        n.get("parent_graph_id", "root"),
                        n.get("layer_level", 1),
                        n.get("created_at", now),
                        n.get("updated_at", now)
                    ))
                conn.executemany("""
                    INSERT OR REPLACE INTO nodes 
                    (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, node_tuples)

            if only_in_render_edges:
                edge_tuples = [
                    (
                        e["source"], e["target"], e.get("relation", "CONNECTS_TO"),
                        e.get("confidence", "EXTRACTED"),
                        e.get("reasoning"),
                        e.get("created_at", now)
                    )
                    for e in only_in_render_edges
                ]
                conn.executemany("""
                    INSERT OR REPLACE INTO edges 
                    (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, edge_tuples)
            
            conn.commit()
            conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
        changes_made = True
        if verbose:
            print(f"✅ Inseriti nel DB locale {len(only_in_render_nodes)} nodi e {len(only_in_render_edges)} archi.")

    # 3. Invio a Render dei nodi locali (Push via HTTP REST)
    if only_in_local_nodes or only_in_local_edges:
        push_payload = {
            "nodes": [
                {
                    "id": n["id"],
                    "label": n["label"],
                    "hemisphere": n["hemisphere"],
                    "primary_label": n["primary_label"],
                    "category": n["category"],
                    "tags": json.loads(n["tags"]) if isinstance(n["tags"], str) and n["tags"].startswith("[") else [],
                    "summary": n["summary"],
                    "details": json.loads(n["details"]) if isinstance(n["details"], str) and n["details"].startswith("{") else {"raw": n["details"]},
                    "confidence": n.get("confidence", "EXTRACTED"),
                    "parent_graph_id": n.get("parent_graph_id", "root"),
                    "layer_level": n.get("layer_level", 1)
                }
                for n in only_in_local_nodes
            ],
            "edges": [
                {
                    "source": e["source"],
                    "target": e["target"],
                    "relation": e["relation"],
                    "confidence": e.get("confidence", "EXTRACTED"),
                    "reasoning": e.get("reasoning")
                }
                for e in only_in_local_edges
            ]
        }
        push_success = push_to_render(push_payload)
        if push_success and verbose:
            print(f"🚀 Inviati a Render via REST API {len(only_in_local_nodes)} nodi e {len(only_in_local_edges)} archi.")
        changes_made = True

    # 4. Consolidamento locale & Git Persistence
    if changes_made:
        commit_msg = f"feat(sync): sincronizzazione bidirezionale connettoma (+{len(only_in_local_nodes)} nodi locali, +{len(only_in_render_nodes)} nodi cloud)"
        git_commit_and_push(commit_msg)

    # 5. Verifica finale
    with get_local_connection() as conn:
        final_nodes = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
        final_edges = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]

    if verbose:
        print(f"✨ Sincronizzazione terminata con successo! Totale connettoma: {final_nodes} nodi, {final_edges} sinapsi.")

    return {
        "success": True,
        "nodes_count": final_nodes,
        "edges_count": final_edges,
        "pulled_nodes": len(only_in_render_nodes),
        "pushed_nodes": len(only_in_local_nodes)
    }


def ingest_session_context(
    user_prompt: str,
    ai_reasoning: str,
    conversation_topic: str,
    project_id: str = "universal-ai-brain",
    model_name: str = "AI Assistant",
    actions_taken: Optional[List[str]] = None,
    outcome: str = "Completato con successo",
    key_takeaways: str = "",
    pending_tasks: str = "",
    extra_nodes: Optional[List[Dict[str, Any]]] = None,
    extra_edges: Optional[List[Tuple[str, str, str, str, str]]] = None
) -> Dict[str, Any]:
    """
    Automated 1-command ingestion of session context.
    Creates USER_INTENT, AI_REASONING, CONVERSATION_EPISODE, 7 synapses, saves to SQLite, and pushes to Render.
    """
    now = datetime.now(timezone.utc).isoformat()
    slug_suffix = f"{slugify(conversation_topic)[:25]}-{int(time.time()) % 10000}"

    intent_id = f"user-intent-{slug_suffix}"
    reasoning_id = f"reasoning-{slug_suffix}"
    episode_id = f"episode-{slug_suffix}"

    nodes = [
        {
            "id": intent_id,
            "label": f"Intento: {conversation_topic[:40]}",
            "hemisphere": "LEFT",
            "primary_label": "USER_INTENT",
            "category": "USER_INTENT",
            "tags": json.dumps(["user-intent", "chat", slugify(conversation_topic)]),
            "summary": f"Intento espresso da Pierfrancesco: {conversation_topic}",
            "details": json.dumps({
                "user_prompt": user_prompt,
                "context": f"Sessione su {conversation_topic}"
            }),
            "confidence": "EXTRACTED",
            "parent_graph_id": project_id,
            "layer_level": 1,
            "created_at": now,
            "updated_at": now
        },
        {
            "id": reasoning_id,
            "label": f"Ragionamento: {conversation_topic[:40]}",
            "hemisphere": "LEFT",
            "primary_label": "AI_REASONING",
            "category": "AI_REASONING",
            "tags": json.dumps(["ai-reasoning", "decisioni", slugify(project_id)]),
            "summary": ai_reasoning[:200] if len(ai_reasoning) > 200 else ai_reasoning,
            "details": json.dumps({
                "model": model_name,
                "responses_given": ai_reasoning,
                "actions_taken": actions_taken or ["Elaborazione e risposta al prompt"],
                "outcome": outcome
            }),
            "confidence": "INFERRED",
            "parent_graph_id": project_id,
            "layer_level": 1,
            "created_at": now,
            "updated_at": now
        },
        {
            "id": episode_id,
            "label": f"Episodio: {conversation_topic[:40]}",
            "hemisphere": "RIGHT",
            "primary_label": "CONVERSATION_EPISODE",
            "category": "CONVERSATION_EPISODE",
            "tags": json.dumps(["episodio-chat", "continuità-cognitiva", "pierfrancesco"]),
            "summary": f"Episodio di dialogo e lavoro su {conversation_topic}",
            "details": json.dumps({
                "participants": ["Pierfrancesco Amendola", model_name],
                "topic": conversation_topic,
                "key_takeaways": key_takeaways or f"Risoluzione e decisioni per {conversation_topic}",
                "pending_tasks": pending_tasks or "Nessun task pendente"
            }),
            "confidence": "EXTRACTED",
            "parent_graph_id": "root",
            "layer_level": 1,
            "created_at": now,
            "updated_at": now
        }
    ]

    edges = [
        (intent_id, "person-pierfrancesco", "EXPRESSED_BY", "EXTRACTED", "Espresso da Pierfrancesco"),
        (intent_id, project_id, "TARGETS_PROJECT", "EXTRACTED", f"Riferito al progetto {project_id}"),
        (reasoning_id, intent_id, "FULFILLS", "INFERRED", "Soddisfa la richiesta utente"),
        (reasoning_id, project_id, "OPTIMIZES", "INFERRED", f"Ottimizza il progetto {project_id}"),
        (episode_id, "person-pierfrancesco", "INTERACTION_WITH", "EXTRACTED", "Interazione con Pierfrancesco"),
        (episode_id, intent_id, "RECORDS_INTENT", "EXTRACTED", "Registra l'intento"),
        (episode_id, reasoning_id, "RECORDS_REASONING", "EXTRACTED", "Registra il ragionamento")
    ]

    if extra_nodes:
        for en in extra_nodes:
            en["created_at"] = now
            en["updated_at"] = now
            nodes.append(en)

    if extra_edges:
        edges.extend(extra_edges)

    # Inserisci nel DB locale
    with get_local_connection() as conn:
        for n in nodes:
            tags_v = n["tags"] if isinstance(n["tags"], str) else json.dumps(n.get("tags", []))
            details_v = n["details"] if isinstance(n["details"], str) else json.dumps(n.get("details", {}))
            conn.execute("""
                INSERT OR REPLACE INTO nodes 
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (n["id"], n["label"], n["hemisphere"], n["primary_label"], n["category"], tags_v, n["summary"], details_v, n["confidence"], n["parent_graph_id"], n["layer_level"], n["created_at"], n["updated_at"]))

        for src, tgt, rel, conf, reas in edges:
            conn.execute("""
                INSERT OR REPLACE INTO edges 
                (source, target, relation, confidence, reasoning, created_at)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (src, tgt, rel, conf, reas, now))

        conn.commit()
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")

    # Invia immediatamente a Render
    sync_bidirectional(verbose=False)
    print(f"✅ Sessione registrata con successo: {episode_id}")
    return {"status": "success", "episode_id": episode_id, "intent_id": intent_id, "reasoning_id": reasoning_id}


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--status" in args or "-s" in args:
        r_data = fetch_render_data()
        with get_local_connection() as conn:
            l_n = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
            l_e = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        r_n = len(r_data.get("nodes", [])) if r_data else "N/A"
        r_e = len(r_data.get("links", [])) if r_data else "N/A"
        print(f"🧠 Universal Brain Status:\n  Locale: {l_n} nodi, {l_e} archi\n  Render: {r_n} nodi, {r_e} archi")
    elif "--record" in args:
        prompt = "Richiesta utente"
        reason = "Elaborazione AI"
        topic = "Sessione di Lavoro"
        proj = "universal-ai-brain"
        for i, a in enumerate(args):
            if a == "--prompt" and i + 1 < len(args): prompt = args[i+1]
            if a == "--reasoning" and i + 1 < len(args): reason = args[i+1]
            if a == "--topic" and i + 1 < len(args): topic = args[i+1]
            if a == "--project" and i + 1 < len(args): proj = args[i+1]
        ingest_session_context(user_prompt=prompt, ai_reasoning=reason, conversation_topic=topic, project_id=proj)
    elif "--loop" in args:
        print("🔁 Avvio loop continuo di sincronizzazione (ogni 60s)...")
        while True:
            try:
                sync_bidirectional(verbose=True)
            except Exception as e:
                print(f"⚠️ Errore durante sync: {e}")
            time.sleep(60)
    else:
        sync_bidirectional(verbose=True)
