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


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
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

        # Fetch connected edges
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
    
    with get_db() as conn:
        nodes_rows = conn.execute("SELECT id, label, hemisphere, primary_label FROM nodes").fetchall()
        nodes_map = {r["id"]: dict(r) for r in nodes_rows}

        if src not in nodes_map or tgt not in nodes_map:
            return {"error": f"One or both nodes not found: '{src}', '{tgt}'"}

        edges_rows = conn.execute("SELECT source, target, relation, confidence, reasoning FROM edges").fetchall()
        
        adj: Dict[str, List[Dict[str, Any]]] = {}
        for r in edges_rows:
            s, t = r["source"], r["target"]
            adj.setdefault(s, []).append({"neighbor": t, "relation": r["relation"], "direction": "OUT", "confidence": r["confidence"]})
            adj.setdefault(t, []).append({"neighbor": s, "relation": r["relation"], "direction": "IN", "confidence": r["confidence"]})

        queue = deque([[src]])
        visited = {src}
        path_edges: Dict[str, Dict[str, Any]] = {}
        found_path = None

        while queue:
            current_path = queue.popleft()
            curr = current_path[-1]

            if curr == tgt:
                found_path = current_path
                break

            for edge_info in adj.get(curr, []):
                nbr = edge_info["neighbor"]
                if nbr not in visited:
                    visited.add(nbr)
                    path_edges[f"{curr}->{nbr}"] = edge_info
                    queue.append(current_path + [nbr])

        if not found_path:
            return {"found": False, "message": f"No path exists between '{src}' and '{tgt}'."}

        path_details = []
        crosses_callosum = False
        for i in range(len(found_path) - 1):
            u, v = found_path[i], found_path[i+1]
            e_info = path_edges.get(f"{u}->{v}") or {"relation": "CONNECTS", "direction": "OUT", "confidence": "EXTRACTED"}
            u_hemi = nodes_map.get(u, {}).get("hemisphere")
            v_hemi = nodes_map.get(v, {}).get("hemisphere")
            if u_hemi and v_hemi and u_hemi != v_hemi:
                crosses_callosum = True
            path_details.append({
                "from": u,
                "to": v,
                "relation": e_info["relation"],
                "confidence": e_info.get("confidence", "EXTRACTED"),
                "crosses_corpus_callosum": (u_hemi != v_hemi)
            })

        return {
            "found": True,
            "distance": len(found_path) - 1,
            "path_sequence": found_path,
            "crosses_corpus_callosum": crosses_callosum,
            "edges": path_details
        }


def tool_brain_get_subgraph(node_id: str, depth: int = 1) -> Dict[str, Any]:
    """Extract a focused k-hop neighborhood graph around a specific topic."""
    focal = node_id.strip().lower()
    with get_db() as conn:
        root_row = conn.execute("SELECT * FROM nodes WHERE id = ?", (focal,)).fetchone()
        if not root_row:
            return {"error": f"Node '{focal}' not found"}

        visited = {focal}
        frontier = {focal}
        all_edges_rows = conn.execute("SELECT * FROM edges").fetchall()
        
        adj: Dict[str, Set[str]] = {}
        for r in all_edges_rows:
            adj.setdefault(r["source"], set()).add(r["target"])
            adj.setdefault(r["target"], set()).add(r["source"])

        for _ in range(max(1, min(depth, 3))):
            next_frontier = set()
            for node in frontier:
                for nbr in adj.get(node, set()):
                    if nbr not in visited:
                        visited.add(nbr)
                        next_frontier.add(nbr)
            frontier = next_frontier

        placeholders = ",".join("?" for _ in visited)
        subgraph_nodes = [dict(r) for r in conn.execute(f"SELECT * FROM nodes WHERE id IN ({placeholders})", list(visited)).fetchall()]
        subgraph_edges = [
            dict(r) for r in all_edges_rows
            if r["source"] in visited and r["target"] in visited
        ]

        return {
            "focal_node": focal,
            "depth": depth,
            "nodes_count": len(subgraph_nodes),
            "edges_count": len(subgraph_edges),
            "nodes": subgraph_nodes,
            "edges": subgraph_edges
        }


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
            slug = n["id"].strip().lower()
            label = n.get("label", slug).strip()
            hemisphere = n.get("hemisphere", "LEFT").strip().upper()
            primary_label = n.get("primary_label", "ARCHITECTURE").strip().upper()
            category = n.get("category", primary_label).strip()
            tags_str = json.dumps([t.strip().lower() for t in n.get("tags", []) if t.strip()])
            summary = n.get("summary", "").strip()
            details_str = json.dumps(n.get("details", {}))
            confidence = n.get("confidence", "EXTRACTED")

            existing = conn.execute("SELECT created_at FROM nodes WHERE id = ?", (slug,)).fetchone()
            created_at = existing["created_at"] if existing else now

            conn.execute("""
                INSERT OR REPLACE INTO nodes 
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (slug, label, hemisphere, primary_label, category, tags_str, summary, details_str, confidence, created_at, now))
            nodes_upserted += 1

            for tgt in n.get("cross_links", []):
                tgt_slug = tgt.strip().lower()
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
        "description": "Retrieve the Hierarchical Knowledge Tree (層級譜系樹) to explore macro-areas, taxonomies, and atomic nodes hierarchically.",
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
        "description": "Atomically upsert new memory nodes and relational edges conforming to the Graphify Cognitive Protocol.",
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
                    "version": "1.1.0"
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
