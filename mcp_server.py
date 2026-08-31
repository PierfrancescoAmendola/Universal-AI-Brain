#!/usr/bin/env python3
"""
Model Context Protocol (MCP) Server for Universal AI Brain.
Implements the JSON-RPC 2.0 stdio transport protocol for seamless integration
with Claude Desktop, Cursor, Antigravity, and AI Agents.
"""

import sys
import json
import sqlite3
import os
from typing import Dict, Any, List, Optional
from collections import deque

DB_PATH = os.getenv("BRAIN_DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "brain.db"))

from optimized_brain_db import create_optimized_brain_db
from obsidian_vault_sync import sync_bidirectional, export_brain_to_vault, import_vault_to_brain
from brain_tensions import get_tensions, create_or_update_tension, resolve_tension, detect_candidate_tensions
from brain_weave import compute_weave_proposals, apply_weave_links
from brain_resurface import get_daily_resurface_packet
from brain_firmware import list_available_firmware, apply_firmware_lens, seed_firmware_nodes_in_brain
from brain_library import list_available_lenses, build_lens_dialogue_prompt, extract_lens_subgraph

brain_db = create_optimized_brain_db(DB_PATH)


def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=5.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


# -----------------------------------------------------------------------------
# Tool Implementations
# -----------------------------------------------------------------------------

def tool_brain_search(query: str, limit: int = 15, hemisphere: Optional[str] = None) -> Dict[str, Any]:
    """Search knowledge graph via BM25 Full-Text Search with optional biological hemispheric gating."""
    with get_db() as conn:
        clean_q = query.strip()
        if not clean_q:
            return {"results": []}
        
        terms = [f'"{t.replace(chr(34), "")}"*' for t in clean_q.split() if t.strip()]
        match_query = " ".join(terms) if terms else clean_q
        
        try:
            cursor = conn.execute("""
                SELECT id FROM nodes_fts
                WHERE nodes_fts MATCH ?
                ORDER BY rank
                LIMIT ?
            """, (match_query, limit))
            matched_ids = [row["id"] for row in cursor.fetchall()]
        except sqlite3.OperationalError:
            search_like = f"%{clean_q.lower()}%"
            cursor = conn.execute("""
                SELECT id FROM nodes
                WHERE lower(id) LIKE ? OR lower(label) LIKE ? OR lower(summary) LIKE ? OR lower(tags) LIKE ?
                LIMIT ?
            """, (search_like, search_like, search_like, search_like, limit))
            matched_ids = [row["id"] for row in cursor.fetchall()]

        if not matched_ids:
            return {"results": [], "count": 0}

        placeholders = ",".join("?" for _ in matched_ids)
        rows = conn.execute(f"SELECT * FROM nodes WHERE id IN ({placeholders})", matched_ids).fetchall()
        row_dict = {r["id"]: dict(r) for r in rows}
        ordered = [row_dict[mid] for mid in matched_ids if mid in row_dict]
        
        # Apply biological hemispheric inhibition gating if requested
        if hemisphere and hemisphere.strip().upper() in ("LEFT", "RIGHT"):
            target_h = hemisphere.strip().upper()
            ordered = [n for n in ordered if n.get("hemisphere") == target_h]

        # Parse JSON fields
        for item in ordered:
            try:
                item["tags"] = json.loads(item["tags"])
            except Exception:
                pass
            try:
                item["details"] = json.loads(item["details"])
            except Exception:
                pass

        return {"count": len(ordered), "results": ordered}


def tool_brain_get_node(node_id: str) -> Dict[str, Any]:
    """Retrieve full details of a specific node along with all connected incoming and outgoing synapses."""
    nid = node_id.strip().lower()
    with get_db() as conn:
        row = conn.execute("SELECT * FROM nodes WHERE id = ?", (nid,)).fetchone()
        if not row:
            return {"error": f"Node '{nid}' not found in brain."}
        
        node_data = dict(row)
        try:
            node_data["tags"] = json.loads(node_data["tags"])
        except Exception:
            pass
        try:
            node_data["details"] = json.loads(node_data["details"])
        except Exception:
            pass

        # Fetch connected edges using strategic indices
        edges_out = [dict(r) for r in conn.execute("SELECT target, relation, confidence, reasoning FROM edges WHERE source = ?", (nid,)).fetchall()]
        edges_in = [dict(r) for r in conn.execute("SELECT source, relation, confidence, reasoning FROM edges WHERE target = ?", (nid,)).fetchall()]

        return {
            "node": node_data,
            "outgoing_edges": edges_out,
            "incoming_edges": edges_in,
            "total_connections": len(edges_out) + len(edges_in)
        }


def tool_brain_shortest_path(source: str, target: str) -> Dict[str, Any]:
    """Find the shortest relational chain connecting two concepts across Left and Right hemispheres."""
    src = source.strip().lower()
    tgt = target.strip().lower()
    
    path_res = brain_db.shortest_path(src, tgt)
    if not path_res:
        return {"found": False, "message": f"No path exists between '{src}' and '{tgt}'."}

    return {
        "found": True,
        "distance": path_res["distance"],
        "path_sequence": path_res["path_sequence"],
        "crosses_corpus_callosum": path_res["crosses_corpus_callosum"],
        "edges": path_res["edges"]
    }


def tool_brain_get_subgraph(node_id: str, depth: int = 1) -> Dict[str, Any]:
    """Extract a focused k-hop neighborhood graph around a specific topic using Recursive CTE."""
    focal = node_id.strip().lower()
    sub_res = brain_db.bfs_subgraph_cte(focal, max_depth=depth)
    if not sub_res:
        return {"error": f"Node '{focal}' not found"}

    return {
        "focal_node": focal,
        "depth": depth,
        "nodes_count": sub_res["total_nodes"],
        "edges_count": sub_res["total_edges"],
        "nodes": sub_res["nodes"],
        "edges": sub_res["edges"]
    }


def sanitize_and_translate_text(text: str) -> str:
    """Translates common Chinese/Wenyan terms to Italian/English to guarantee pure FTS5 search."""
    if not text:
        return text
    replacements = {
        "層級譜系樹": "Albero Gerarchico (Hierarchical Tree)",
        "譜系樹": "Albero Gerarchico",
        "樹狀結構技術評析": "Valutazione Tecnica Strutture ad Albero",
        "知識圖譜": "Knowledge Graph",
        "神經符號": "Neuro-Simbolico",
        "胼胝體": "Corpo Calloso",
        "雙半球": "Bi-Emisferico",
        "半球": "Emisfero",
        "左半球": "Emisfero Sinistro",
        "右半球": "Emisfero Destro",
        "突觸": "Sinapsi",
        "節點": "Nodo",
        "路徑": "Percorso",
        "檢索": "Ricerca FTS",
        "認知": "Cognitivo",
        "架構": "Architettura",
        "意圖": "Intento Utente",
        "推演": "Deduzione AI",
        "對話": "Episodio Conversazionale",
        "通透無礙，極佳之策": "Strategia ottimale approvata",
        "冠絕群策者": "Migliore Soluzione Eletta",
        "已全面構建完成": "Completamente rilasciato e verificato"
    }
    cleaned = text
    for k, v in replacements.items():
        cleaned = cleaned.replace(k, v)
    return cleaned


def determine_node_floor_level(node_id: str, primary_label: str, category: str, degree: int = 0, explicit_level: Optional[int] = None) -> int:
    """
    Classifica il piano nel Palazzo Cognitivo:
    - Piano 0: Attico Macro-Domini & Core Hubs (SOLO Identità person-pierfrancesco e Macro-Domini domain-*)
    - Piano 1: Progetti & Applicazioni (StreaksUp, AuleStudio, CareTrack, Brain, Episodi, Intenti, Valori)
    - Piano 2: Moduli, Algoritmi & Dettagli Atomici (Schemi dati, Algoritmi specialistici, Token UI)
    """
    if explicit_level is not None and explicit_level in (0, 1, 2):
        return explicit_level
    nid = (node_id or "").lower()
    pl = (primary_label or "").upper()
    cat = (category or "").lower()
    
    # Floor 0: Attico Macro-Domini & Core Hubs (SOLO IDENTITÀ E MACRO-DOMINI)
    if nid == 'person-pierfrancesco' or nid.startswith('domain-') or cat in ('domain', 'root_domain', 'macro_domain'):
        return 0
    # Floor 2: Moduli Atomici, Algoritmi, Token, Schemi (NON progetti)
    if cat != 'application_project' and not nid.startswith('proj-') and not nid.endswith('-app') and nid not in ('universal-ai-brain', 'aule-studio-app'):
        if pl in ['ALGORITHM', 'DATA_STRUCTURE', 'DEPENDENCY', 'API_SPEC', 'UI_COMPONENT', 'DESIGN_TOKEN', 'COLOR_PALETTE', 'BUSINESS_LOGIC'] or 'schema' in cat or 'token' in cat or 'dettaglio' in cat:
            return 2
    # Floor 1: Progetti, Applicazioni, Episodi, Intenti, Valori, Idee
    return 1


def tool_brain_ingest(nodes: List[Dict[str, Any]], edges: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Atomically ingest new knowledge nodes and synapses following the Graphify Protocol."""
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    nodes_upserted = 0
    edges_upserted = 0
    edges = edges or []

    with get_db() as conn:
        cross_links_to_add = []
        for n in nodes:
            raw_id = (n.get("id") or n.get("label") or "").strip()
            if not raw_id:
                continue
            slug = sanitize_and_translate_text(raw_id).lower().replace(" ", "-").replace("/", "-")
            label = sanitize_and_translate_text((n.get("label") or n.get("id") or slug).strip())
            hemisphere = n.get("hemisphere", "LEFT").strip().upper()
            if hemisphere not in ("LEFT", "RIGHT"):
                hemisphere = "LEFT"
            default_pl = "ARCHITECTURE" if hemisphere == "LEFT" else "CREATIVE_IDEA"
            primary_label = (n.get("primary_label") or n.get("category") or default_pl).strip().upper()
            category = (n.get("category") or primary_label).strip()

            summary = sanitize_and_translate_text((n.get("summary") or f"Concept {label}").strip())
            tags_str = json.dumps([sanitize_and_translate_text(t).strip().lower() for t in n.get("tags", []) if t.strip()])
            
            details_obj = n.get("details") or {}
            if not isinstance(details_obj, dict):
                try:
                    details_obj = json.loads(details_obj) if isinstance(details_obj, str) else {}
                except Exception:
                    details_obj = {"raw": str(details_obj)}

            if primary_label == "USER_INTENT":
                if "user_prompt" not in details_obj or not details_obj["user_prompt"]:
                    details_obj["user_prompt"] = summary or label
            elif primary_label in ("AI_REASONING", "METACOGNITION"):
                if "model" not in details_obj or not details_obj["model"]:
                    details_obj["model"] = "AI Assistant"
            elif primary_label == "CONVERSATION_EPISODE":
                if "participants" not in details_obj or not details_obj["participants"]:
                    details_obj["participants"] = ["Pierfrancesco Amendola", "AI Assistant"]
                if "topic" not in details_obj or not details_obj["topic"]:
                    details_obj["topic"] = label

            details_str = json.dumps(details_obj)
            confidence = n.get("confidence", "EXTRACTED")
            parent_graph_id = n.get("parent_graph_id", "root") or "root"
            raw_lvl = n.get("layer_level", None)
            layer_level = determine_node_floor_level(slug, primary_label, category, explicit_level=raw_lvl)

            existing = conn.execute("SELECT created_at FROM nodes WHERE id = ?", (slug,)).fetchone()
            created_at = existing["created_at"] if existing else now

            conn.execute("""
                INSERT OR REPLACE INTO nodes 
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (slug, label, hemisphere, primary_label, category, tags_str, summary, details_str, confidence, parent_graph_id, layer_level, created_at, now))
            nodes_upserted += 1

            for tgt in n.get("cross_links", []):
                tgt_slug = sanitize_and_translate_text(str(tgt)).strip().lower()
                if tgt_slug and tgt_slug != slug:
                    cross_links_to_add.append((slug, tgt_slug))

        # Insert Corpus Callosum bridges
        for s, t in cross_links_to_add:
            if conn.execute("SELECT 1 FROM nodes WHERE id = ?", (t,)).fetchone():
                conn.execute("""
                    INSERT OR REPLACE INTO edges (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, 'CORPUS_CALLOSUM_LINK', 'EXTRACTED', 'Cross-hemisphere bridge', ?)
                """, (s, t, now))
                edges_upserted += 1

        # Insert explicit edges
        for e in edges:
            src = e["source"].strip().lower()
            tgt = e["target"].strip().lower()
            rel = e.get("relation", "CONNECTS").strip().upper().replace(" ", "_")
            conf = e.get("confidence", "EXTRACTED")
            reason = e.get("reasoning", None)

            if conn.execute("SELECT 1 FROM nodes WHERE id = ?", (src,)).fetchone() and \
               conn.execute("SELECT 1 FROM nodes WHERE id = ?", (tgt,)).fetchone():
                conn.execute("""
                    INSERT OR REPLACE INTO edges (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (src, tgt, rel, conf, reason, now))
                edges_upserted += 1

        conn.commit()
        brain_db.invalidate_cache()

        # Aggiornamento istantaneo del Vault Obsidian
        try:
            from obsidian_vault_sync import export_brain_to_vault
            vault_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "obsidian_vault")
            export_brain_to_vault(DB_PATH, vault_dir)
        except Exception:
            pass

    return {
        "status": "success",
        "nodes_upserted": nodes_upserted,
        "edges_upserted": edges_upserted
    }


def tool_brain_get_stats() -> Dict[str, Any]:
    """Get global brain metrics (node count, hemisphere split, edges, Corpus Callosum links)."""
    with get_db() as conn:
        total_nodes = conn.execute("SELECT COUNT(*) AS c FROM nodes").fetchone()["c"]
        left_nodes = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere = 'LEFT'").fetchone()["c"]
        right_nodes = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere = 'RIGHT'").fetchone()["c"]
        total_edges = conn.execute("SELECT COUNT(*) AS c FROM edges").fetchone()["c"]
        callosum_edges = conn.execute("SELECT COUNT(*) AS c FROM edges WHERE relation = 'CORPUS_CALLOSUM_LINK'").fetchone()["c"]
        
        return {
            "total_nodes": total_nodes,
            "left_hemisphere_nodes": left_nodes,
            "right_hemisphere_nodes": right_nodes,
            "total_edges": total_edges,
            "corpus_callosum_edges": callosum_edges
        }


def tool_brain_get_tree(hemisphere: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve the complete Hierarchical Knowledge Tree (層級譜系樹) for multi-level semantic zoom."""
    with get_db() as conn:
        query = "SELECT * FROM nodes"
        params = []
        if hemisphere and hemisphere.upper() in ("LEFT", "RIGHT"):
            query += " WHERE hemisphere = ?"
            params.append(hemisphere.upper())
        query += " ORDER BY hemisphere, primary_label, label"

        nodes_rows = conn.execute(query, params).fetchall()
        edges_rows = conn.execute("SELECT source, target FROM edges").fetchall()

        degrees: Dict[str, int] = {}
        for e in edges_rows:
            degrees[e["source"]] = degrees.get(e["source"], 0) + 1
            degrees[e["target"]] = degrees.get(e["target"], 0) + 1

        tree: Dict[str, Any] = {
            "id": "brain-root",
            "name": "🧠 Universal AI Brain",
            "type": "root",
            "total_nodes": len(nodes_rows),
            "total_edges": len(edges_rows),
            "children": []
        }

        hemi_groups: Dict[str, Dict[str, List[Dict[str, Any]]]] = {"LEFT": {}, "RIGHT": {}}
        for r in nodes_rows:
            hemi_groups.setdefault(r["hemisphere"], {}).setdefault(r["primary_label"], []).append(dict(r))

        hemi_meta = {
            "LEFT": {"name": "Left Hemisphere (Logic & Tech)", "icon": "⚡"},
            "RIGHT": {"name": "Right Hemisphere (Art, Emotions & Values)", "icon": "🌸"}
        }

        for h_key in ["LEFT", "RIGHT"]:
            if hemisphere and hemisphere.upper() != h_key:
                continue
            pl_dict = hemi_groups.get(h_key, {})
            h_children = []
            for pl_key, node_list in pl_dict.items():
                pl_children = []
                for n in node_list:
                    tags = json.loads(n["tags"]) if n.get("tags") else []
                    pl_children.append({
                        "id": n["id"],
                        "name": n["label"],
                        "primary_label": n["primary_label"],
                        "category": n["category"],
                        "tags": tags,
                        "summary": n["summary"],
                        "degree": degrees.get(n["id"], 0),
                        "confidence": n.get("confidence", "EXTRACTED")
                    })
                pl_children.sort(key=lambda x: x["degree"], reverse=True)
                h_children.append({
                    "id": f"tax-{h_key.lower()}-{pl_key.lower()}",
                    "name": pl_key,
                    "type": "taxonomy",
                    "hemisphere": h_key,
                    "node_count": len(pl_children),
                    "children": pl_children
                })
            h_children.sort(key=lambda x: x["node_count"], reverse=True)
            tree["children"].append({
                "id": f"hemi-{h_key.lower()}",
                "name": hemi_meta[h_key]["name"],
                "type": "hemisphere",
                "hemisphere": h_key,
                "icon": hemi_meta[h_key]["icon"],
                "node_count": sum(c["node_count"] for c in h_children),
                "children": h_children
            })

        return tree


def tool_brain_get_palazzo() -> Dict[str, Any]:
    """Retrieve the complete 3D Multi-Layer Palazzo Cognitivo (Graph-of-Graphs) structure."""
    with get_db() as conn:
        nodes_rows = conn.execute("SELECT * FROM nodes ORDER BY layer_level, hemisphere, primary_label, label").fetchall()
        edges_rows = conn.execute("SELECT * FROM edges").fetchall()
        nodes = [dict(r) for r in nodes_rows]
        edges = [dict(r) for r in edges_rows]
        
        degrees: Dict[str, int] = {}
        for e in edges:
            degrees[e["source"]] = degrees.get(e["source"], 0) + 1
            degrees[e["target"]] = degrees.get(e["target"], 0) + 1

        node_floor_map: Dict[str, int] = {}
        floors_data: Dict[int, Dict[str, Any]] = {
            0: {"level": 0, "name": "Piano 0: Attico Macro-Domini", "icon": "👑", "nodes": []},
            1: {"level": 1, "name": "Piano 1: Progetti & Aree", "icon": "🚀", "nodes": []},
            2: {"level": 2, "name": "Piano 2: Moduli & Dettagli", "icon": "🧩", "nodes": []}
        }

        for n in nodes:
            lvl = int(n.get("layer_level", 0)) if n.get("layer_level") is not None else 0
            if lvl not in (0, 1, 2):
                lvl = 1

            n_clean = {
                "id": n["id"],
                "label": n["label"],
                "hemisphere": n["hemisphere"],
                "primary_label": n["primary_label"],
                "degree": degrees.get(n["id"], 0),
                "layer_level": lvl
            }
            node_floor_map[n["id"]] = lvl
            floors_data.get(lvl, floors_data[1])["nodes"].append(n_clean)

        cross_layer_count = sum(1 for e in edges if node_floor_map.get(e["source"], 0) != node_floor_map.get(e["target"], 0))

        return {
            "title": "Palazzo Cognitivo (Graph-of-Graphs)",
            "total_nodes": len(nodes),
            "total_edges": len(edges),
            "cross_layer_elevators": cross_layer_count,
            "floors": [floors_data[0], floors_data[1], floors_data[2]]
        }


def tool_brain_sync_obsidian(action: str = "sync", vault_dir: Optional[str] = None) -> Dict[str, Any]:
    """Sync, export or import Markdown notes with Obsidian Vault."""
    v_dir = vault_dir or os.getenv("OBSIDIAN_VAULT_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "obsidian_vault"))
    if action == "export":
        return export_brain_to_vault(DB_PATH, v_dir)
    elif action == "import":
        return import_vault_to_brain(v_dir, DB_PATH)
    else:
        return sync_bidirectional(v_dir, DB_PATH)


def tool_brain_get_tensions(status: Optional[str] = None, limit: int = 50) -> Dict[str, Any]:
    """Retrieve active or resolved cognitive tensions and contradictions."""
    tensions = get_tensions(status=status, limit=limit, db_path=DB_PATH)
    return {"count": len(tensions), "tensions": tensions}


def tool_brain_create_tension(node_a_id: str, node_b_id: str, tension_type: str = "CONTRADICTION", description: str = "") -> Dict[str, Any]:
    """Create a cognitive tension or trade-off between two nodes."""
    return create_or_update_tension(node_a_id, node_b_id, tension_type, description, db_path=DB_PATH)


def tool_brain_resolve_tension(tension_id: str, strategy: str, resolution_notes: str) -> Dict[str, Any]:
    """Resolve a tension using a strategy (MERGE_AI, RECONCILE_MANUAL, STEELMAN, FALSE_POSITIVE, IGNORED)."""
    return resolve_tension(tension_id, strategy, resolution_notes, db_path=DB_PATH)


def tool_brain_detect_tensions(limit: int = 15) -> Dict[str, Any]:
    """Detect candidate contradictions or dialectical trade-offs across nodes."""
    candidates = detect_candidate_tensions(db_path=DB_PATH, limit=limit)
    return {"count": len(candidates), "candidate_tensions": candidates}


def tool_brain_get_weave_proposals(max_proposals: int = 15, max_degree: int = 2) -> Dict[str, Any]:
    """Generate link proposals and Callosal bridges for orphan or low-degree nodes."""
    proposals = compute_weave_proposals(max_proposals=max_proposals, max_degree=max_degree, db_path=DB_PATH)
    return {"count": len(proposals), "proposals": proposals}


def tool_brain_apply_weave_links(proposals: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Atomically apply accepted weave link proposals to the graph."""
    return apply_weave_links(proposals, db_path=DB_PATH)


def tool_brain_get_daily_resurface() -> Dict[str, Any]:
    """Get the 90-second Daily Cognitive Resurface packet (dormant nodes, tension, daily mental model)."""
    return get_daily_resurface_packet(db_path=DB_PATH)


def tool_brain_list_firmware() -> Dict[str, Any]:
    """List the 9 cognitive mental models / firmware thinking lenses."""
    models = list_available_firmware()
    return {"count": len(models), "firmware_models": models}


def tool_brain_apply_firmware(mode: str, problem: str, context: Optional[str] = None) -> Dict[str, Any]:
    """Apply a cognitive firmware thinking lens (Inversion, Antifragility, First Principles, etc.) to a problem."""
    return apply_firmware_lens(mode, problem, context)


def tool_brain_list_lenses() -> Dict[str, Any]:
    """List available authors, books, and mentor lenses in the knowledge graph."""
    lenses = list_available_lenses(db_path=DB_PATH)
    return {"count": len(lenses), "lenses": lenses}


def tool_brain_query_library_lens(lens_id_or_keyword: str, question: str) -> Dict[str, Any]:
    """Generate a grounded persona dialogue prompt with strict node citations for an author, book, or mentor."""
    return build_lens_dialogue_prompt(lens_id_or_keyword, question, db_path=DB_PATH)


# -----------------------------------------------------------------------------
# MCP JSON-RPC 2.0 Server Protocol Dispatcher
# -----------------------------------------------------------------------------

MCP_TOOLS = [
    {
        "name": "brain_get_palazzo",
        "description": "Retrieve the 3D Multi-Layer Palazzo Cognitivo (Graph-of-Graphs) floor layout and vertical elevator synapses.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "brain_get_tree",
        "description": "Retrieve the Hierarchical Knowledge Tree to explore macro-areas, taxonomies, and atomic nodes hierarchically.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "hemisphere": {"type": "string", "description": "Optional filter: 'LEFT' or 'RIGHT'"}
            }
        }
    },
    {
        "name": "brain_search",
        "description": "Perform high-precision BM25 Full-Text Search on Pierfrancesco's Universal Knowledge Graph with optional biological hemispheric gating.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search term or concept keywords"},
                "limit": {"type": "integer", "description": "Max results to return (default: 15)"},
                "hemisphere": {"type": "string", "description": "Optional biological gating filter: 'LEFT' (Logic & Tech) or 'RIGHT' (Design & Values)"}
            },
            "required": ["query"]
        }
    },
    {
        "name": "brain_get_node",
        "description": "Retrieve deep structured profile, details, tags, and all connected synapses for a single node ID.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string", "description": "Unique slug ID of the node"}
            },
            "required": ["node_id"]
        }
    },
    {
        "name": "brain_shortest_path",
        "description": "Find the shortest relational chain of thought connecting two arbitrary concepts or memories across Left and Right hemispheres.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "source": {"type": "string", "description": "Source node slug ID"},
                "target": {"type": "string", "description": "Target node slug ID"}
            },
            "required": ["source", "target"]
        }
    },
    {
        "name": "brain_get_subgraph",
        "description": "Extract scoped k-hop neighborhood graph around a specific topic for focused GraphRAG memory context.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_id": {"type": "string", "description": "Focal node slug ID"},
                "depth": {"type": "integer", "description": "Hop distance (1 to 3, default: 1)"}
            },
            "required": ["node_id"]
        }
    },
    {
        "name": "brain_ingest",
        "description": "Atomically upsert new memory nodes and relational edges conforming to the Cognitive Memory Protocol.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "nodes": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "List of node definitions with id, label, hemisphere, primary_label, tags, summary, details, confidence"
                },
                "edges": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "List of edge definitions with source, target, relation, confidence, reasoning"
                }
            },
            "required": ["nodes"]
        }
    },
    {
        "name": "brain_get_stats",
        "description": "Get real-time statistics and health metrics of the Universal Knowledge Graph.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "brain_sync_obsidian",
        "description": "Bi-directional synchronization between SQLite graph and Obsidian Vault Markdown notes.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "description": "Action: 'sync', 'export', or 'import' (default: 'sync')"},
                "vault_dir": {"type": "string", "description": "Optional custom Obsidian vault path"}
            }
        }
    },
    {
        "name": "brain_get_tensions",
        "description": "Get active or resolved cognitive tensions, paradoxes, and contradictions between ideas.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "status": {"type": "string", "description": "Filter by status: 'OPEN', 'RESOLVED', 'FALSE_POSITIVE', 'IGNORED'"},
                "limit": {"type": "integer", "description": "Max results to return (default: 50)"}
            }
        }
    },
    {
        "name": "brain_create_tension",
        "description": "Record a contradiction or trade-off between two nodes in the brain.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "node_a_id": {"type": "string", "description": "First node ID"},
                "node_b_id": {"type": "string", "description": "Second node ID"},
                "tension_type": {"type": "string", "description": "Type: 'CONTRADICTION', 'TRADE_OFF', 'PARADOX', 'DIALECTIC'"},
                "description": {"type": "string", "description": "Explanation of the tension"}
            },
            "required": ["node_a_id", "node_b_id", "description"]
        }
    },
    {
        "name": "brain_resolve_tension",
        "description": "Resolve a cognitive tension using Hegelian synthesis, steelmanning, or manual reconciliation.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "tension_id": {"type": "string", "description": "Unique tension ID"},
                "strategy": {"type": "string", "description": "Strategy: 'MERGE_AI', 'RECONCILE_MANUAL', 'STEELMAN', 'FALSE_POSITIVE', 'IGNORED'"},
                "resolution_notes": {"type": "string", "description": "Detailed resolution notes or synthesis"}
            },
            "required": ["tension_id", "strategy", "resolution_notes"]
        }
    },
    {
        "name": "brain_detect_tensions",
        "description": "Scan the knowledge graph for uncataloged semantic contradictions and trade-offs.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer", "description": "Max candidates to return (default: 15)"}
            }
        }
    },
    {
        "name": "brain_get_weave_proposals",
        "description": "Find orphan nodes and propose high-value intra-domain and Corpus Callosum synaptic links.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "max_proposals": {"type": "integer", "description": "Max proposals (default: 15)"},
                "max_degree": {"type": "integer", "description": "Max degree of target orphan nodes (default: 2)"}
            }
        }
    },
    {
        "name": "brain_apply_weave_links",
        "description": "Atomically apply accepted weave link proposals into SQLite WAL.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "proposals": {
                    "type": "array",
                    "items": {"type": "object"},
                    "description": "List of accepted link proposal objects (source, target, relation, reasoning)"
                }
            },
            "required": ["proposals"]
        }
    },
    {
        "name": "brain_get_daily_resurface",
        "description": "Retrieve the 90-second Daily Cognitive Briefing: 3 dormant nodes (Ebbinghaus curve), 1 tension, 1 mental model.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "brain_list_firmware",
        "description": "List the 9 cognitive mental models / thinking lenses (Inversion, Antifragility, First Principles, Pareto, etc.).",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "brain_apply_firmware",
        "description": "Apply a specific mental model lens to analyze a problem or architectural decision.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "mode": {"type": "string", "description": "Firmware mode (e.g., 'inversion', 'antifragility', 'first_principles', 'second_order', 'pareto', 'feynman', 'circle_of_competence', 'opportunity_cost', 'bayesian_updating')"},
                "problem": {"type": "string", "description": "Problem statement or decision to analyze"},
                "context": {"type": "string", "description": "Optional context or constraints"}
            },
            "required": ["mode", "problem"]
        }
    },
    {
        "name": "brain_list_lenses",
        "description": "List available author, book, and mentor lenses for grounded dialogue.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "brain_query_library_lens",
        "description": "Generate a grounded persona prompt with exact node citations to talk directly with an author, book, or mentor.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "lens_id_or_keyword": {"type": "string", "description": "ID or keyword of the book/author (e.g., 'marcus-aurelius', 'taleb', 'hormozi')"},
                "question": {"type": "string", "description": "Question to ask the mentor/book"}
            },
            "required": ["lens_id_or_keyword", "question"]
        }
    }
]


def handle_json_rpc(req: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    method = req.get("method")
    req_id = req.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": "universal-ai-brain-mcp",
                    "version": "2.0.0"
                }
            }
        }

    elif method == "notifications/initialized":
        return None

    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": MCP_TOOLS
            }
        }

    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})

        try:
            if tool_name == "brain_get_palazzo":
                res = tool_brain_get_palazzo()
            elif tool_name == "brain_get_tree":
                res = tool_brain_get_tree(args.get("hemisphere"))
            elif tool_name == "brain_search":
                res = tool_brain_search(args.get("query", ""), args.get("limit", 15), args.get("hemisphere"))
            elif tool_name == "brain_get_node":
                res = tool_brain_get_node(args.get("node_id", ""))
            elif tool_name == "brain_shortest_path":
                res = tool_brain_shortest_path(args.get("source", ""), args.get("target", ""))
            elif tool_name == "brain_get_subgraph":
                res = tool_brain_get_subgraph(args.get("node_id", ""), args.get("depth", 1))
            elif tool_name == "brain_ingest":
                res = tool_brain_ingest(args.get("nodes", []), args.get("edges", []))
            elif tool_name == "brain_get_stats":
                res = tool_brain_get_stats()
            elif tool_name == "brain_sync_obsidian":
                res = tool_brain_sync_obsidian(args.get("action", "sync"), args.get("vault_dir"))
            elif tool_name == "brain_get_tensions":
                res = tool_brain_get_tensions(args.get("status"), args.get("limit", 50))
            elif tool_name == "brain_create_tension":
                res = tool_brain_create_tension(args.get("node_a_id", ""), args.get("node_b_id", ""), args.get("tension_type", "CONTRADICTION"), args.get("description", ""))
            elif tool_name == "brain_resolve_tension":
                res = tool_brain_resolve_tension(args.get("tension_id", ""), args.get("strategy", ""), args.get("resolution_notes", ""))
            elif tool_name == "brain_detect_tensions":
                res = tool_brain_detect_tensions(args.get("limit", 15))
            elif tool_name == "brain_get_weave_proposals":
                res = tool_brain_get_weave_proposals(args.get("max_proposals", 15), args.get("max_degree", 2))
            elif tool_name == "brain_apply_weave_links":
                res = tool_brain_apply_weave_links(args.get("proposals", []))
            elif tool_name == "brain_get_daily_resurface":
                res = tool_brain_get_daily_resurface()
            elif tool_name == "brain_list_firmware":
                res = tool_brain_list_firmware()
            elif tool_name == "brain_apply_firmware":
                res = tool_brain_apply_firmware(args.get("mode", ""), args.get("problem", ""), args.get("context"))
            elif tool_name == "brain_list_lenses":
                res = tool_brain_list_lenses()
            elif tool_name == "brain_query_library_lens":
                res = tool_brain_query_library_lens(args.get("lens_id_or_keyword", ""), args.get("question", ""))
            else:
                return {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}
                }

            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(res, indent=2, ensure_ascii=False)}
                    ]
                }
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "isError": True,
                    "content": [{"type": "text", "text": f"Error executing tool '{tool_name}': {str(e)}"}]
                }
            }

    elif method == "ping":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method '{method}' not found"}
        }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_json_rpc(req)
            if resp:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except Exception as e:
            err = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {str(e)}"}
            }
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
