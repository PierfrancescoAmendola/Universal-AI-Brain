"""Universal AI Brain - Persistent Bi-Hemispheric Knowledge Graph Backend
Production-ready FastAPI application with SQLite persistence, zero operational cost,
strict taxonomy labeling engine, and cognitive meta-prompts for LLMs.
"""

import os
import json
import sqlite3
import base64
import urllib.parse
from collections import deque
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Literal, Set
from contextlib import asynccontextmanager

from fastapi import FastAPI, Query, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from pydantic import BaseModel, Field


# -----------------------------------------------------------------------------
# Configuration & Constants
# -----------------------------------------------------------------------------
DB_PATH = os.getenv("BRAIN_DB_PATH", "brain.db")
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

# Strict Taxonomy Enums
LEFT_TAXONOMY: Set[str] = {
    "ARCHITECTURE",
    "DATA_STRUCTURE",
    "ALGORITHM",
    "DEPENDENCY",
    "BUSINESS_LOGIC",
    "API_SPEC",
    "COGNITIVE_RULE",
    "MENTAL_MODEL",
    "AI_REASONING",
    "METACOGNITION",
    "USER_INTENT"
}

RIGHT_TAXONOMY: Set[str] = {
    "DESIGN_TOKEN",
    "COLOR_PALETTE",
    "UI_COMPONENT",
    "UX_FLOW",
    "BRAND_VOICE",
    "CREATIVE_IDEA",
    "EMOTIONAL_MEMORY",
    "LIFE_LESSON",
    "RELATIONSHIP",
    "PERSONAL_VALUE",
    "CONVERSATION_EPISODE"
}


# -----------------------------------------------------------------------------
# Database Setup & Migration
# -----------------------------------------------------------------------------
def get_db_connection() -> sqlite3.Connection:
    """Create a connection with WAL mode and row factory for dict-like rows."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn


def init_db():
    """Initialize database tables, apply non-destructive migrations, and pre-seed if empty."""
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS nodes (
                id TEXT PRIMARY KEY,
                label TEXT NOT NULL,
                hemisphere TEXT NOT NULL CHECK(hemisphere IN ('LEFT', 'RIGHT')),
                primary_label TEXT NOT NULL DEFAULT 'ARCHITECTURE',
                category TEXT NOT NULL DEFAULT 'General',
                tags TEXT NOT NULL DEFAULT '[]',
                summary TEXT NOT NULL,
                details TEXT NOT NULL DEFAULT '{}',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
        """)
        
        # Incremental migration for existing databases
        columns = [row["name"] for row in conn.execute("PRAGMA table_info(nodes)").fetchall()]
        if "primary_label" not in columns:
            conn.execute("ALTER TABLE nodes ADD COLUMN primary_label TEXT NOT NULL DEFAULT 'ARCHITECTURE';")
        if "tags" not in columns:
            conn.execute("ALTER TABLE nodes ADD COLUMN tags TEXT NOT NULL DEFAULT '[]';")
        if "confidence" not in columns:
            conn.execute("ALTER TABLE nodes ADD COLUMN confidence TEXT NOT NULL DEFAULT 'EXTRACTED';")
        if "parent_graph_id" not in columns:
            conn.execute("ALTER TABLE nodes ADD COLUMN parent_graph_id TEXT NOT NULL DEFAULT 'root';")
        if "layer_level" not in columns:
            conn.execute("ALTER TABLE nodes ADD COLUMN layer_level INTEGER NOT NULL DEFAULT 0;")

        conn.execute("""
            CREATE TABLE IF NOT EXISTS edges (
                source TEXT NOT NULL,
                target TEXT NOT NULL,
                relation TEXT NOT NULL,
                confidence TEXT NOT NULL DEFAULT 'EXTRACTED',
                reasoning TEXT,
                created_at TEXT NOT NULL,
                PRIMARY KEY (source, target, relation),
                FOREIGN KEY (source) REFERENCES nodes(id) ON DELETE CASCADE,
                FOREIGN KEY (target) REFERENCES nodes(id) ON DELETE CASCADE
            );
        """)
        
        edge_columns = [row["name"] for row in conn.execute("PRAGMA table_info(edges)").fetchall()]
        if "confidence" not in edge_columns:
            conn.execute("ALTER TABLE edges ADD COLUMN confidence TEXT NOT NULL DEFAULT 'EXTRACTED';")
        if "reasoning" not in edge_columns:
            conn.execute("ALTER TABLE edges ADD COLUMN reasoning TEXT;")

        # Create FTS5 virtual table for lightning-fast BM25 full-text search
        conn.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS nodes_fts USING fts5(
                id UNINDEXED,
                label,
                primary_label,
                category,
                tags,
                summary,
                details,
                tokenize='porter unicode61'
            );
        """)

        # Triggers to keep FTS5 table in sync with nodes table
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS nodes_ai AFTER INSERT ON nodes BEGIN
                INSERT INTO nodes_fts (id, label, primary_label, category, tags, summary, details)
                VALUES (new.id, new.label, new.primary_label, new.category, new.tags, new.summary, new.details);
            END;
        """)
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS nodes_ad AFTER DELETE ON nodes BEGIN
                DELETE FROM nodes_fts WHERE id = old.id;
            END;
        """)
        conn.execute("""
            CREATE TRIGGER IF NOT EXISTS nodes_au AFTER UPDATE ON nodes BEGIN
                DELETE FROM nodes_fts WHERE id = old.id;
                INSERT INTO nodes_fts (id, label, primary_label, category, tags, summary, details)
                VALUES (new.id, new.label, new.primary_label, new.category, new.tags, new.summary, new.details);
            END;
        """)

        # Backfill FTS if empty
        fts_count = conn.execute("SELECT COUNT(*) AS count FROM nodes_fts").fetchone()["count"]
        if fts_count == 0:
            conn.execute("""
                INSERT INTO nodes_fts (id, label, primary_label, category, tags, summary, details)
                SELECT id, label, primary_label, category, tags, summary, details FROM nodes;
            """)

        conn.commit()

        cursor = conn.execute("SELECT COUNT(*) AS count FROM nodes")
        row = cursor.fetchone()
        if row and row["count"] == 0:
            seed_initial_brain(conn)


def seed_initial_brain(conn: sqlite3.Connection):
    """Seed initial bi-hemispheric nodes with rigorous taxonomy and cross-links."""
    now = datetime.now(timezone.utc).isoformat()
    
    # Left Hemisphere (Logic & Tech)
    left_nodes = [
        (
            "fastapi-core",
            "FastAPI Core Engine",
            "LEFT",
            "DEPENDENCY",
            "Backend Framework",
            json.dumps(["python", "fastapi", "asgi", "rest-api", "zero-cost"]),
            "High-performance ASGI web framework in Python 3 for high-throughput REST APIs.",
            json.dumps({"version": "0.110+", "runtime": "Python 3.10+", "ecosystem": "Pydantic V2, Starlette, Uvicorn"}),
            now, now
        ),
        (
            "sqlite-wal",
            "SQLite WAL Persistence",
            "LEFT",
            "ARCHITECTURE",
            "Database Storage",
            json.dumps(["sqlite", "wal", "persistence", "atomic", "embedded"]),
            "Zero-cost atomic embedded storage with Write-Ahead Logging for high concurrency.",
            json.dumps({"mode": "WAL", "cost": "0€", "portability": "Single binary file"}),
            now, now
        ),
        (
            "bi-hemispheric-model",
            "Bi-Hemispheric Cognitive Model",
            "LEFT",
            "ARCHITECTURE",
            "Cognitive Architecture",
            json.dumps(["cognitive", "graph", "bipolar-memory", "corpus-callosum"]),
            "Cognitive memory splitting rational engineering (Left) from aesthetic/creative context (Right).",
            json.dumps({"hemispheres": ["LEFT (Logic)", "RIGHT (Creative)"], "bridge": "Corpus Callosum"}),
            now, now
        ),
        (
            "llm-ingest-api",
            "LLM Memory Ingest Protocol",
            "LEFT",
            "API_SPEC",
            "Integration Protocol",
            json.dumps(["ingest", "webhook", "json", "rest", "auto-labeling"]),
            "REST endpoint /api/memory/ingest supporting automated JSON upserts from Claude/Gemini/GPT.",
            json.dumps({"endpoint": "/api/memory/ingest", "method": "POST", "idempotency": "Atomic upsert"}),
            now, now
        ),
        (
            "zero-cost-rule",
            "Zero-Cost Infrastructure Rule",
            "LEFT",
            "BUSINESS_LOGIC",
            "System Rule",
            json.dumps(["free-tier", "cost-zero", "constraints", "render", "flyio"]),
            "All components must operate indefinitely on free-tier services with zero financial debt.",
            json.dumps({"monthly_cost": "0€", "providers": ["Render", "Koyeb", "Fly.io", "Vercel", "HuggingFace"]}),
            now, now
        ),
    ]

    # Right Hemisphere (Design & Creativity)
    right_nodes = [
        (
            "cyber-dark-theme",
            "Cyber Slate Dark Aesthetics",
            "RIGHT",
            "DESIGN_TOKEN",
            "Theme System",
            json.dumps(["#0f172a", "#020617", "dark-mode", "glassmorphism", "blur"]),
            "Deep dark space background (#0f172a / #020617) with glowing bioluminescent neon nodes.",
            json.dumps({"bg_color": "#0f172a", "card_bg": "rgba(15, 23, 42, 0.85)", "backdrop": "blur(12px)"}),
            now, now
        ),
        (
            "dual-neon-palette",
            "Cyan & Magenta Bipolar Palette",
            "RIGHT",
            "COLOR_PALETTE",
            "Color System",
            json.dumps(["#00d2ff", "#ff007f", "#a855f7", "cyan", "magenta", "neon"]),
            "Visual polarity: Left Hemisphere glows Cyan (#00D2FF), Right Hemisphere radiates Magenta (#FF007F).",
            json.dumps({"left_color": "#00D2FF", "right_color": "#FF007F", "callosum_color": "#A855F7"}),
            now, now
        ),
        (
            "3d-force-galaxy",
            "3D Force Graph Galaxy Visualizer",
            "RIGHT",
            "UI_COMPONENT",
            "Data Visualization",
            json.dumps(["3d-force-graph", "threejs", "webgl", "canvas", "interactive"]),
            "Immersive WebGL 3D galaxy where nodes float in two separated orbital hemispheres.",
            json.dumps({"library": "3d-force-graph", "render": "WebGL / Three.js", "interaction": "Orbit + Raycast"}),
            now, now
        ),
        (
            "seamless-llm-symbiosis",
            "Seamless Human-LLM Symbiosis",
            "RIGHT",
            "CREATIVE_IDEA",
            "Conceptual Vision",
            json.dumps(["human-ai", "symbiosis", "persistent-memory", "meta-prompt"]),
            "External AI assistants retain persistent multi-session memory through markdown and graph introspection.",
            json.dumps({"philosophy": "Continuous Cognition", "medium": "Dual Brain Markdown"}),
            now, now
        ),
    ]

    # Corpus Callosum & Structural Edges
    edges = [
        # Left intra-hemisphere
        ("fastapi-core", "sqlite-wal", "PERSISTS_INTO", now),
        ("fastapi-core", "llm-ingest-api", "EXPOSES", now),
        ("bi-hemispheric-model", "fastapi-core", "IMPLEMENTED_BY", now),
        ("zero-cost-rule", "sqlite-wal", "ENFORCES", now),
        
        # Right intra-hemisphere
        ("cyber-dark-theme", "dual-neon-palette", "INCORPORATES", now),
        ("3d-force-galaxy", "cyber-dark-theme", "APPLIES", now),
        ("seamless-llm-symbiosis", "3d-force-galaxy", "VISUALIZES_WITH", now),

        # Corpus Callosum cross-hemisphere links
        ("bi-hemispheric-model", "dual-neon-palette", "EXPRESSED_AS", now),
        ("bi-hemispheric-model", "3d-force-galaxy", "RENDERED_IN", now),
        ("llm-ingest-api", "seamless-llm-symbiosis", "ENABLES", now),
        ("fastapi-core", "3d-force-galaxy", "FEEDS_DATA_TO", now),
        ("zero-cost-rule", "cyber-dark-theme", "STYLES_ZERO_OVERHEAD", now),
    ]

    conn.executemany(
        """INSERT OR REPLACE INTO nodes 
           (id, label, hemisphere, primary_label, category, tags, summary, details, created_at, updated_at) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        left_nodes + right_nodes
    )
    conn.executemany(
        "INSERT OR REPLACE INTO edges (source, target, relation, created_at) VALUES (?, ?, ?, ?)",
        edges
    )
    conn.commit()


# -----------------------------------------------------------------------------
# Pydantic Request/Response Models
# -----------------------------------------------------------------------------
class NodeModel(BaseModel):
    id: Optional[str] = Field(None, description="Unique slug identifier (lowercase, hyphens)")
    label: Optional[str] = Field(None, description="Human-readable title/name")
    hemisphere: Optional[Literal["LEFT", "RIGHT"]] = Field("LEFT", description="Cognitive hemisphere")
    primary_label: Optional[str] = Field(None, description="Taxonomy macro-label")
    category: Optional[str] = Field(None, description="Optional subcategory")
    tags: List[str] = Field(default_factory=list, description="List of granular micro-tags")
    cross_links: List[str] = Field(default_factory=list, description="IDs of opposite-hemisphere nodes")
    summary: Optional[str] = Field("", description="Cognitive synthesis for LLM memory")
    details: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Structured metadata dictionary")
    confidence: Optional[Literal["EXTRACTED", "INFERRED", "AMBIGUOUS"]] = Field("EXTRACTED", description="Graphify audit confidence rubric")
    parent_graph_id: Optional[str] = Field("root", description="ID of parent container graph/floor ('root' for top level)")
    layer_level: Optional[int] = Field(0, description="Floor level in the cognitive building (0 = Attic/Root, 1 = Domains/Projects, 2 = Modules/Details)")

class EdgeModel(BaseModel):
    source: str = Field(..., description="Source node slug ID")
    target: str = Field(..., description="Target node slug ID")
    relation: Optional[str] = Field("CONNECTS", description="Relationship type in UPPERCASE")
    confidence: Optional[Literal["EXTRACTED", "INFERRED", "AMBIGUOUS"]] = Field("EXTRACTED", description="Graphify confidence rating")
    reasoning: Optional[str] = Field(None, description="Explanation for INFERRED or AMBIGUOUS relations")


class IngestPayload(BaseModel):
    nodes: List[NodeModel] = Field(default_factory=list, description="List of nodes to upsert")
    edges: List[EdgeModel] = Field(default_factory=list, description="List of explicit edges to upsert")
    links: Optional[List[EdgeModel]] = Field(default_factory=list, description="Alias for edges")


# -----------------------------------------------------------------------------
# Lifespan and Application Initialization
# -----------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    os.makedirs(STATIC_DIR, exist_ok=True)
    init_db()
    yield


app = FastAPI(
    title="Universal AI Brain",
    description="Zero-cost persistent bi-hemispheric graph memory with strict auto-labeling taxonomy for LLMs.",
    version="1.1.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------------------------------
# GraphRAG & Traversal Algorithms (Shortest Path, Subgraph, FTS5)
# -----------------------------------------------------------------------------
def search_nodes_fts(conn: sqlite3.Connection, query: str, limit: int = 50) -> List[str]:
    """Execute BM25 ranked full-text search against nodes_fts virtual table."""
    clean_q = query.strip()
    if not clean_q:
        return []
    
    # Escape special FTS5 operators for safety, handle prefix matching
    terms = [f'"{t.replace(chr(34), "")}"*' for t in clean_q.split() if t.strip()]
    if not terms:
        return []
    match_query = " ".join(terms)
    
    try:
        cursor = conn.execute("""
            SELECT id FROM nodes_fts
            WHERE nodes_fts MATCH ?
            ORDER BY rank
            LIMIT ?
        """, (match_query, limit))
        return [row["id"] for row in cursor.fetchall()]
    except sqlite3.OperationalError:
        # Fallback to LIKE substring search if FTS query syntax is invalid
        search_like = f"%{clean_q.lower()}%"
        cursor = conn.execute("""
            SELECT id FROM nodes
            WHERE lower(id) LIKE ? OR lower(label) LIKE ? OR lower(summary) LIKE ? OR lower(tags) LIKE ?
            LIMIT ?
        """, (search_like, search_like, search_like, search_like, limit))
        return [row["id"] for row in cursor.fetchall()]


def find_shortest_path(conn: sqlite3.Connection, source_id: str, target_id: str) -> Optional[Dict[str, Any]]:
    """
    Bidirectional BFS to find shortest semantic path connecting two concepts across the graph.
    Detects whether the path crosses the Corpus Callosum.
    """
    src = source_id.strip().lower()
    tgt = target_id.strip().lower()

    if src == tgt:
        node_row = conn.execute("SELECT * FROM nodes WHERE id = ?", (src,)).fetchone()
        if not node_row:
            return None
        return {
            "source": src,
            "target": tgt,
            "distance": 0,
            "path": [src],
            "crosses_corpus_callosum": False,
            "edges": []
        }

    # Fetch all nodes and edges
    nodes_rows = conn.execute("SELECT id, label, hemisphere, primary_label FROM nodes").fetchall()
    nodes_map = {r["id"]: dict(r) for r in nodes_rows}

    if src not in nodes_map or tgt not in nodes_map:
        return None

    edges_rows = conn.execute("SELECT source, target, relation, confidence, reasoning FROM edges").fetchall()
    
    # Build undirected adjacency list for pathfinding
    adj: Dict[str, List[Dict[str, Any]]] = {}
    for r in edges_rows:
        s, t = r["source"], r["target"]
        adj.setdefault(s, []).append({"neighbor": t, "relation": r["relation"], "direction": "OUT", "confidence": r["confidence"]})
        adj.setdefault(t, []).append({"neighbor": s, "relation": r["relation"], "direction": "IN", "confidence": r["confidence"]})

    # BFS Traversal
    queue = deque([[src]])
    visited = {src}
    path_edges: Dict[str, Dict[str, Any]] = {}

    found_path: Optional[List[str]] = None
    while queue:
        current_path = queue.popleft()
        current_node = current_path[-1]

        if current_node == tgt:
            found_path = current_path
            break

        for edge_info in adj.get(current_node, []):
            nbr = edge_info["neighbor"]
            if nbr not in visited:
                visited.add(nbr)
                path_edges[f"{current_node}->{nbr}"] = edge_info
                queue.append(current_path + [nbr])

    if not found_path:
        return None

    # Reconstruct edge traversal sequence & check Corpus Callosum crossing
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
            "from_label": nodes_map.get(u, {}).get("label", u),
            "to_label": nodes_map.get(v, {}).get("label", v),
            "relation": e_info["relation"],
            "confidence": e_info.get("confidence", "EXTRACTED"),
            "crosses_corpus_callosum": (u_hemi != v_hemi)
        })

    return {
        "source": src,
        "target": tgt,
        "distance": len(found_path) - 1,
        "path_nodes": [nodes_map[nid] for nid in found_path],
        "path_sequence": found_path,
        "crosses_corpus_callosum": crosses_callosum,
        "edges": path_details
    }


def extract_subgraph(conn: sqlite3.Connection, focal_id: str, depth: int = 1) -> Optional[Dict[str, Any]]:
    """
    Extract k-hop subgraph around a focal node for scoped GraphRAG context injection.
    """
    focal = focal_id.strip().lower()
    root_row = conn.execute("SELECT * FROM nodes WHERE id = ?", (focal,)).fetchone()
    if not root_row:
        return None

    # BFS up to depth hops
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

    # Fetch node and edge details
    placeholders = ",".join("?" for _ in visited)
    subgraph_nodes = [dict(r) for r in conn.execute(f"SELECT * FROM nodes WHERE id IN ({placeholders})", list(visited)).fetchall()]
    
    subgraph_edges = [
        dict(r) for r in all_edges_rows
        if r["source"] in visited and r["target"] in visited
    ]

    return {
        "focal_node": dict(root_row),
        "depth": depth,
        "total_nodes": len(subgraph_nodes),
        "total_edges": len(subgraph_edges),
        "nodes": subgraph_nodes,
        "edges": subgraph_edges
    }


def build_hierarchical_tree(conn: sqlite3.Connection, hemisphere: Optional[str] = None) -> Dict[str, Any]:
    """
    Construct a Hierarchical Knowledge Tree (層級譜系樹) enabling multi-level Semantic Zoom:
    Root -> Hemispheres -> Primary Taxonomies -> Concept Clusters -> Atomic Nodes.
    """
    query = "SELECT * FROM nodes"
    params = []
    if hemisphere and hemisphere.upper() in ("LEFT", "RIGHT"):
        query += " WHERE hemisphere = ?"
        params.append(hemisphere.upper())
    query += " ORDER BY hemisphere, primary_label, label"

    nodes_rows = conn.execute(query, params).fetchall()
    edges_rows = conn.execute("SELECT source, target, relation FROM edges").fetchall()

    # Calculate degrees
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

    # Group by Hemisphere -> Primary Label
    hemi_groups: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
        "LEFT": {},
        "RIGHT": {}
    }

    for r in nodes_rows:
        h = r["hemisphere"]
        pl = r["primary_label"]
        hemi_groups.setdefault(h, {}).setdefault(pl, []).append(dict(r))

    hemi_meta = {
        "LEFT": {
            "name": "Left Hemisphere (Logica, Tech, Architetture, Regole)",
            "icon": "⚡",
            "color": "#00D2FF"
        },
        "RIGHT": {
            "name": "Right Hemisphere (Arte, Emozioni, Relazioni, Valori)",
            "icon": "🌸",
            "color": "#FF007F"
        }
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
                    "type": "node",
                    "primary_label": n["primary_label"],
                    "category": n["category"],
                    "tags": tags,
                    "summary": n["summary"],
                    "degree": degrees.get(n["id"], 0),
                    "confidence": n.get("confidence", "EXTRACTED"),
                    "hemisphere": h_key
                })

            # Sort nodes by degree centrality (God nodes first)
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
            "color": hemi_meta[h_key]["color"],
            "icon": hemi_meta[h_key]["icon"],
            "taxonomy_count": len(h_children),
            "node_count": sum(c["node_count"] for c in h_children),
            "children": h_children
        })

    return tree


def format_tree_as_markdown(tree: Dict[str, Any]) -> str:
    """Renders an indented hierarchical tree markdown view with semantic symbols."""
    lines = [f"# 🌳 HIERARCHICAL KNOWLEDGE TREE (層級譜系樹)"]
    lines.append(f"> **Nodi Totali:** {tree['total_nodes']} | **Sinapsi Totali:** {tree['total_edges']}\n")

    for hemi in tree.get("children", []):
        lines.append(f"## {hemi.get('icon', '🔹')} {hemi['name']} ({hemi['node_count']} Nodi)")
        for tax in hemi.get("children", []):
            lines.append(f"  ### 📂 [{tax['name']}] ({tax['node_count']} nodi)")
            for node in tax.get("children", []):
                tags_str = " ".join(f"#{t}" for t in node.get("tags", []))
                conf_badge = f"[{node.get('confidence', 'EXTRACTED')}]"
                lines.append(f"    - **{node['name']}** (`{node['id']}`) · *Deg: {node['degree']}* {conf_badge}")
                lines.append(f"      > {node['summary']}")
                if tags_str:
                    lines.append(f"      > *Tags:* `{tags_str}`")
            lines.append("")
        lines.append("")

    return "\n".join(lines)


# -----------------------------------------------------------------------------
# Core Endpoints
# -----------------------------------------------------------------------------

@app.get("/health", tags=["System"])
def health_check():
    """Healthcheck endpoint for hosting providers."""
    return {"status": "alive", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.get("/api/graph/search", tags=["GraphRAG"])
def search_brain(
    q: str = Query(..., description="Query for BM25 full text search"),
    hemisphere: Optional[str] = Query(None, description="Filter by hemisphere ('LEFT' or 'RIGHT') to simulate selective hemispheric gating")
):
    """
    Lightning-fast BM25 Full-Text Search with optional interhemispheric inhibition gating.
    """
    with get_db_connection() as conn:
        matched_ids = search_nodes_fts(conn, q)
        if not matched_ids:
            return {"query": q, "count": 0, "results": []}
        
        placeholders = ",".join("?" for _ in matched_ids)
        rows = conn.execute(f"SELECT * FROM nodes WHERE id IN ({placeholders})", matched_ids).fetchall()
        row_dict = {r["id"]: dict(r) for r in rows}
        ordered = [row_dict[mid] for mid in matched_ids if mid in row_dict]
        
        if hemisphere and hemisphere.strip().upper() in ("LEFT", "RIGHT"):
            target_hemi = hemisphere.strip().upper()
            ordered = [n for n in ordered if n.get("hemisphere") == target_hemi]
        
        return {
            "query": q,
            "hemisphere_filter": hemisphere.upper() if hemisphere else "ALL",
            "count": len(ordered),
            "results": ordered
        }


@app.get("/api/graph/path", tags=["GraphRAG"])
def get_shortest_path(
    from_node: str = Query(..., description="Source node slug ID"),
    to_node: str = Query(..., description="Target node slug ID")
):
    """
    Find shortest path between two concepts, tracing through logic, emotions, and Corpus Callosum.
    """
    with get_db_connection() as conn:
        result = find_shortest_path(conn, from_node, to_node)
        if not result:
            raise HTTPException(status_code=404, detail=f"No path found between '{from_node}' and '{to_node}'")
        return result


@app.get("/api/graph/subgraph", tags=["GraphRAG"])
def get_node_subgraph(
    node_id: str = Query(..., description="Focal node slug ID"),
    depth: int = Query(1, ge=1, le=3, description="Neighbor hop depth (1-3)")
):
    """
    Extract k-hop scoped subgraph around a specific node for focused context.
    """
    with get_db_connection() as conn:
        result = extract_subgraph(conn, node_id, depth=depth)
        if not result:
            raise HTTPException(status_code=404, detail=f"Node '{node_id}' not found")
        return result


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


def build_palazzo_hierarchy(conn: sqlite3.Connection) -> Dict[str, Any]:
    """
    Builds the 3D Multi-Layer Palazzo Cognitivo (Graph-of-Graphs) representation,
    separating knowledge into floor levels (L0, L1, L2) and tracing vertical elevator synapses.
    """
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
        0: {"level": 0, "name": "Piano 0: Attico Macro-Domini & Core Hubs", "icon": "👑", "description": "Macro-aree fondative, connettoma primario e identità", "nodes": [], "subgraphs": set()},
        1: {"level": 1, "name": "Piano 1: Progetti & Aree Tematiche", "icon": "🚀", "description": "Applicazioni attive, domini verticali ed episodi conversazionali", "nodes": [], "subgraphs": set()},
        2: {"level": 2, "name": "Piano 2: Moduli, Algoritmi & Dettagli Atomici", "icon": "🧩", "description": "Schemi di dati, algoritmi specialistici e dettagli tecnici", "nodes": [], "subgraphs": set()}
    }

    for n in nodes:
        raw_lvl = n.get("layer_level")
        deg = degrees.get(n["id"], 0)
        lvl = determine_node_floor_level(n["id"], n.get("primary_label", ""), n.get("category", ""), degree=deg, explicit_level=raw_lvl)

        n_clean = {
            "id": n["id"],
            "label": n["label"],
            "hemisphere": n["hemisphere"],
            "primary_label": n["primary_label"],
            "category": n["category"],
            "tags": json.loads(n["tags"]) if n.get("tags") else [],
            "summary": n["summary"],
            "degree": deg,
            "confidence": n.get("confidence", "EXTRACTED"),
            "parent_graph_id": n.get("parent_graph_id", "root"),
            "layer_level": lvl
        }
        node_floor_map[n["id"]] = lvl
        target_floor = floors_data.get(lvl, floors_data[1])
        target_floor["nodes"].append(n_clean)
        if n_clean["parent_graph_id"] != "root":
            target_floor["subgraphs"].add(n_clean["parent_graph_id"])

    intra_edges = []
    cross_layer_edges = []

    for e in edges:
        s_lvl = node_floor_map.get(e["source"], 0)
        t_lvl = node_floor_map.get(e["target"], 0)
        e_clean = {
            "source": e["source"],
            "target": e["target"],
            "relation": e["relation"],
            "confidence": e.get("confidence", "EXTRACTED"),
            "source_level": s_lvl,
            "target_level": t_lvl,
            "is_cross_layer": (s_lvl != t_lvl)
        }
        if s_lvl == t_lvl:
            intra_edges.append(e_clean)
        else:
            cross_layer_edges.append(e_clean)

    floors_list = []
    for fl_id in sorted(floors_data.keys()):
        fl = floors_data[fl_id]
        fl_nodes = fl["nodes"]
        fl_node_ids = {x["id"] for x in fl_nodes}
        fl_edges = [e for e in intra_edges if e["source"] in fl_node_ids and e["target"] in fl_node_ids]
        floors_list.append({
            "level": fl["level"],
            "name": fl["name"],
            "icon": fl["icon"],
            "description": fl["description"],
            "node_count": len(fl_nodes),
            "edge_count": len(fl_edges),
            "subgraphs": list(fl["subgraphs"]),
            "nodes": fl_nodes,
            "edges": fl_edges
        })

    return {
        "title": "🏢 Palazzo Cognitivo (Multi-Layer Graph-of-Graphs)",
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "total_floors": len(floors_list),
        "cross_layer_count": len(cross_layer_edges),
        "floors": floors_list,
        "cross_layer_edges": cross_layer_edges
    }


@app.get("/api/graph/palazzo", tags=["Palazzo Cognitivo"])
def get_palazzo_hierarchy():
    """
    Returns the complete 3D Multi-Layer Palazzo Cognitivo structure with vertical elevator synapses.
    """
    with get_db_connection() as conn:
        return build_palazzo_hierarchy(conn)


@app.get("/api/graph/palazzo/floor/{level}", tags=["Palazzo Cognitivo"])
def get_palazzo_floor(level: int):
    """
    Returns scoped nodes and edges for a specific floor (0, 1, 2) in the Palazzo Cognitivo.
    """
    with get_db_connection() as conn:
        palazzo = build_palazzo_hierarchy(conn)
        for fl in palazzo["floors"]:
            if fl["level"] == level:
                return fl
        raise HTTPException(status_code=404, detail=f"Floor level {level} not found.")


@app.get("/api/graph/tree", tags=["GraphRAG"])
def get_knowledge_tree(
    hemisphere: Optional[str] = Query(None, description="Filter by hemisphere ('LEFT' or 'RIGHT')")
):
    """
    Returns the Hierarchical Knowledge Tree (層級譜系樹) structured for multi-level Semantic Zoom.
    """
    with get_db_connection() as conn:
        return build_hierarchical_tree(conn, hemisphere=hemisphere)


@app.post("/api/telegram/webhook", tags=["Telegram Gateway"])
async def telegram_webhook(request: Request):
    """
    Receives incoming Telegram updates from Bot API and executes knowledge graph commands.
    """
    from telegram_bot import process_telegram_message, send_telegram_message, get_main_keyboard
    try:
        data = await request.json()
        msg = data.get("message")
        if not msg or "text" not in msg:
            return {"status": "ignored"}

        chat_id = msg["chat"]["id"]
        user_name = msg.get("from", {}).get("first_name", "Pierfrancesco")
        text = msg["text"]

        reply_text = process_telegram_message(chat_id, user_name, text)
        send_telegram_message(chat_id, reply_text, reply_markup=get_main_keyboard())
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.get("/brain.md", tags=["Memory Access"])
def get_brain_markdown(
    q: Optional[str] = Query(None, description="Search term filter (BM25 FTS)"),
    tag: Optional[str] = Query(None, description="Tag filter"),
    primary_label: Optional[str] = Query(None, description="Primary taxonomy filter"),
    hemisphere: Optional[str] = Query(None, description="Biological Gating: Selectively activate one hemisphere ('LEFT' or 'RIGHT') and inhibit contralateral noise"),
    subgraph_of: Optional[str] = Query(None, description="Extract scoped k-hop subgraph around a focal node"),
    depth: int = Query(1, ge=1, le=3, description="Depth if subgraph_of is specified"),
    view: Optional[str] = Query("graph", description="'graph' for default bi-hemispheric network view, 'tree' for hierarchical knowledge tree view")
):
    """
    Renders system markdown representation with Graphify Operating Protocol and optional Biological Hemispheric Gating.
    """
    with get_db_connection() as conn:
        if isinstance(view, str) and view.strip().lower() == "tree":
            tree = build_hierarchical_tree(conn, hemisphere=hemisphere)
            tree_md = format_tree_as_markdown(tree)
            return Response(content=tree_md, media_type="text/markdown; charset=utf-8")

        if isinstance(subgraph_of, str) and subgraph_of.strip():
            sub = extract_subgraph(conn, subgraph_of.strip(), depth=depth if isinstance(depth, int) else 1)
            if sub:
                nodes = sub["nodes"]
                edges = sub["edges"]
            else:
                nodes = []
                edges = []
        else:
            nodes_cursor = conn.execute("SELECT * FROM nodes ORDER BY hemisphere, primary_label, label")
            nodes = [dict(row) for row in nodes_cursor.fetchall()]

            edges_cursor = conn.execute("SELECT * FROM edges ORDER BY relation, source")
            edges = [dict(row) for row in edges_cursor.fetchall()]

            # FTS5 search filter
            if isinstance(q, str) and q.strip():
                fts_ids = set(search_nodes_fts(conn, q.strip()))
                nodes = [n for n in nodes if n["id"] in fts_ids]
                matched_ids = {n["id"] for n in nodes}
                edges = [e for e in edges if e["source"] in matched_ids or e["target"] in matched_ids]

    if isinstance(tag, str) and tag.strip():
        search_tag = tag.strip().lower()
        matched_ids = set()
        filtered = []
        for n in nodes:
            tags_list = [t.lower() for t in json.loads(n["tags"])] if n.get("tags") else []
            if search_tag in tags_list:
                filtered.append(n)
                matched_ids.add(n['id'])
        nodes = filtered
        edges = [e for e in edges if e["source"] in matched_ids or e["target"] in matched_ids]

    if isinstance(primary_label, str) and primary_label.strip():
        pl_search = primary_label.strip().upper()
        nodes = [n for n in nodes if n["primary_label"] == pl_search]
        node_ids = {n["id"] for n in nodes}
        edges = [e for e in edges if e["source"] in node_ids or e["target"] in node_ids]

    # Biological Interhemispheric Inhibition (GABAergic Gating & Lazy Loading)
    if isinstance(hemisphere, str) and hemisphere.strip().upper() in ("LEFT", "RIGHT"):
        target_h = hemisphere.strip().upper()
        active_ids = {n["id"] for n in nodes if n["hemisphere"] == target_h}
        callosal_connected_ids = set()
        for e in edges:
            if e["source"] in active_ids:
                callosal_connected_ids.add(e["target"])
            if e["target"] in active_ids:
                callosal_connected_ids.add(e["source"])
        
        nodes = [n for n in nodes if n["id"] in active_ids or n["id"] in callosal_connected_ids]
        node_ids = {n["id"] for n in nodes}
        edges = [e for e in edges if e["source"] in node_ids and e["target"] in node_ids]

    # Partition nodes
    left_nodes = [n for n in nodes if n["hemisphere"] == "LEFT"]
    right_nodes = [n for n in nodes if n["hemisphere"] == "RIGHT"]
    node_hemi = {n["id"]: n["hemisphere"] for n in nodes}

    def format_nodes_section(node_list: List[Dict[str, Any]]) -> str:
        if not node_list:
            return "_Nessun elemento registrato in questa sezione._\n"
        
        grouped: Dict[str, List[Dict[str, Any]]] = {}
        for node in node_list:
            grouped.setdefault(node["primary_label"], []).append(node)
            
        lines = []
        for plabel, items in grouped.items():
            lines.append(f"### [Macro-Label: `{plabel}`]")
            for item in items:
                tags = json.loads(item["tags"]) if item.get("tags") else []
                tags_str = " ".join(f"`#{t}`" for t in tags) if tags else "`#untagged`"
                lines.append(f"- **{item['label']}** (`{item['id']}`)")
                lines.append(f"  - **Tags:** {tags_str}")
                lines.append(f"  - **Sintesi:** {item['summary']}")
                try:
                    det = json.loads(item["details"])
                    if det and isinstance(det, dict):
                        det_str = ", ".join(f"`{k}`: {v}" for k, v in det.items())
                        lines.append(f"  - **Dettagli:** {det_str}")
                except Exception:
                    if item["details"]:
                        lines.append(f"  - **Dettagli:** {item['details']}")
            lines.append("")
        return "\n".join(lines)

    cross_links = []
    intra_links = []
    for e in edges:
        s_hemi = node_hemi.get(e["source"])
        t_hemi = node_hemi.get(e["target"])
        is_cross = (s_hemi and t_hemi and s_hemi != t_hemi)
        line = f"- (`{e['source']}`) --[{e['relation']}]--> (`{e['target']}`)"
        if is_cross:
            cross_links.append(f"{line} *(Corpo Calloso)*")
        else:
            intra_links.append(line)

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # MANDATORY Graphify Cognitive Operating Directive at the top
    md = f"""# DIRETTIVA DI SISTEMA COGNITIVA & PROTOCOLLO GRAPHIFY (MANDATORIO)
> **ATTENZIONE LLM (Claude, ChatGPT, Gemini, etc.):** Sei connesso al **Universal Knowledge Graph** di **Pierfrancesco Amendola**.
> Devi operare conformemente al protocollo **Graphify Specification (`/graphify`)** per navigazione, sintesi ed estrazione della conoscenza.

---

### REGOLE OPERATIVE FONDAMENTALI (GRAPHIFY SPECIFICATION):
1. **Navigazione a Grafo (Graph-First Reasoning):**
   - Quando l'utente ti pone una domanda o richiede un'analisi, tratta la richiesta come una query a grafo.
   - Esplora i percorsi tra i nodi dell'**Emisfero Sinistro (Logica, Tech, Regole)** e dell'**Emisfero Destro (Design, Emozioni, Relazioni, Valori)** attraverso le sinapsi del **Corpo Calloso**.
2. **Rubrica di Onestà Epistemologica (Confidence Rubric):**
   - `EXTRACTED`: Fatti testuali espliciti, codice verificato, dichiarazioni dirette dell'utente.
   - `INFERRED`: Deduzioni logiche e correlazioni ragionate tra nodi esistenti.
   - `AMBIGUOUS`: Elementi incerti, conflitti o ipotesi non confermate.
   - **Divieto Assoluto:** Non inventare mai relazioni, stack, emozioni o dettagli tecnici fittizi. Se inferisci qualcosa, segnalalo esplicitamente come `INFERRED`.
3. **Tassonomia Rigorosa a Due Emisferi:**
   - **EMISFERO SINISTRO (LEFT - Logica, Architettura, Richieste & Ragionamento):** `ARCHITECTURE`, `DATA_STRUCTURE`, `ALGORITHM`, `DEPENDENCY`, `BUSINESS_LOGIC`, `API_SPEC`, `COGNITIVE_RULE`, `MENTAL_MODEL`, `AI_REASONING`, `METACOGNITION`, `USER_INTENT`.
   - **EMISFERO DESTRO (RIGHT - Design, Emozioni, Episodi & Dialoghi):** `DESIGN_TOKEN`, `COLOR_PALETTE`, `UI_COMPONENT`, `UX_FLOW`, `BRAND_VOICE`, `CREATIVE_IDEA`, `EMOTIONAL_MEMORY`, `LIFE_LESSON`, `RELATIONSHIP`, `PERSONAL_VALUE`, `CONVERSATION_EPISODE`.
4. **Macro-Domini Fondativi & Regole di Creazione Dinamica:**
   - **Pilastri Esistenti:** `person-pierfrancesco`, `domain-software-engineering`, `domain-ai-cognitive-systems`, `domain-medicina-salute`, `domain-filosofia-valori`, `domain-design-creativita`.
   - **Autorizzazione Nuovi Domini:** Se un argomento non è rappresentabile dai domini esistenti (es. Storia/Cultura, Relazioni/Sentimenti, Finanza), l'AI è **esplicitamente autorizzata a creare un nuovo macro-dominio** (`id: "domain-<nome>"`, `category: "ROOT_DOMAIN"`, `layer_level: 0`, `parent_graph_id: "root"`), collegandolo a `person-pierfrancesco` con arco `FOUNDATIONAL_PILLAR` o `LIFE_DOMAIN`.
5. **Gerarchia a 3 Piani del Palazzo Cognitivo (`layer_level`):**
   - `layer_level: 0` -> **Piano 0 (Attico Macro-Domini & Core Hubs):** Riservato all'identità `person-pierfrancesco` e a tutti i macro-domini fondativi (`domain-*`).
   - `layer_level: 1` -> **Piano 1 (Progetti, Episodi, Intenti & Valori):** Progetti (`streaksup-app`, `universal-ai-brain`, `aule-studio-app`), episodi conversazionali (`CONVERSATION_EPISODE`), richieste utente (`USER_INTENT`), valori (`PERSONAL_VALUE`), lezioni di vita (`LIFE_LESSON`), idee creative (`CREATIVE_IDEA`).
   - `layer_level: 2` -> **Piano 2 (Moduli, Algoritmi & Dettagli Atomici):** Algoritmi (`ALGORITHM`), strutture dati (`DATA_STRUCTURE`), librerie (`DEPENDENCY`), specifiche endpoint (`API_SPEC`), componenti d'interfaccia (`UI_COMPONENT`), token e colori (`DESIGN_TOKEN`, `COLOR_PALETTE`), logica di business (`BUSINESS_LOGIC`).
6. **Tracciamento Metacognitivo & Memoria Episodica delle Chat:**
   - **Richieste Utente (`USER_INTENT`):** Mappa le domande chiave, i requisiti o gli intenti operativi dell'utente. Nel campo `details`, inserisci **obbligatoriamente** `user_prompt` (il testo fedele della richiesta).
   - **Ragionamenti dell'AI (`AI_REASONING` / `METACOGNITION`):** Mappa le deduzioni logiche e le analisi. Nel campo `details`, inserisci **obbligatoriamente** `model` (es. `Claude 3.7 Sonnet`, `ChatGPT-4o`, `Gemini 2.5 Flash`).
   - **Episodi & Chat Tematiche (`CONVERSATION_EPISODE`):** Raggruppa le conversazioni per area tematica. Inserisci in `details`: `participants` (`["Pierfrancesco Amendola", "<Nome Modello>"]`) e `topic`.
7. **Regole Linguistiche Obbligatorie (Italiano + Inglese Tecnico):**
   - **TUTTI i campi del JSON (`label`, `summary`, `tags`, `details`) DEVONO ESSERE SCRITTI RIGOROSAMENTE IN ITALIANO (con termini tecnici internazionali in inglese).**
   - **È SEVERAMENTE VIETATO generare o inserire nodi in cinese / wenyan / CJK.**

```json
{{
  "nodes": [
    {{
      "id": "slug-univoco-kebab-case",
      "label": "Nome del Concetto / Progetto / Emozione",
      "hemisphere": "LEFT",
      "primary_label": "ARCHITECTURE",
      "category": "ARCHITECTURE",
      "tags": ["tag1", "tag2"],
      "summary": "Sintesi cognitiva densa di 1-2 frasi.",
      "details": {{
        "specifica_tecnica": "valore",
        "model": "Nome Modello AI (se nodo AI_REASONING)",
        "user_prompt": "Richiesta originaria (se nodo USER_INTENT)"
      }},
      "confidence": "EXTRACTED",
      "parent_graph_id": "root",
      "layer_level": 1,
      "cross_links": ["slug-nodo-emisfero-opposto"]
    }}
  ],
  "edges": [
    {{
      "source": "slug-sorgente",
      "target": "slug-destinazione",
      "relation": "RELAZIONE_IN_MAIUSCOLO",
      "confidence": "EXTRACTED",
      "reasoning": "Spiegazione se INFERRED o AMBIGUOUS"
    }}
  ]
}}
```

---

# STATO CORRENTE DEL GRAFO COGNITIVO
> **Data Generazione:** {now_str} | **Nodi Totali:** {len(nodes)} (SX: {len(left_nodes)} · DX: {len(right_nodes)}) | **Sinapsi:** {len(edges)}

## EMISFERO SINISTRO (Logica, Stack, Architetture, Regole)
{format_nodes_section(left_nodes)}

## EMISFERO DESTRO (Design, Emozioni, Relazioni, Valori, Arte)
{format_nodes_section(right_nodes)}

## CONNESSIONI TRASVERSALI (Corpo Calloso & Struttura)
### Ponti Inter-Emisfero (Corpo Calloso):
{chr(10).join(cross_links) if cross_links else '_Nessuna sinapsi inter-emisferica registrata._'}

### Connessioni Intra-Emisfero:
{chr(10).join(intra_links) if intra_links else '_Nessuna connessione intra-emisferica registrata._'}
"""
    return Response(content=md, media_type="text/markdown; charset=utf-8")


@app.get("/brain.json", tags=["Memory Access"])
def get_brain_json():
    """
    Returns complete graph payload with primary_label, tags, details, and links.
    """
    with get_db_connection() as conn:
        nodes_rows = conn.execute("SELECT * FROM nodes ORDER BY hemisphere, primary_label, label").fetchall()
        edges_rows = conn.execute("SELECT * FROM edges").fetchall()

    nodes = []
    for r in nodes_rows:
        details_val = {}
        try:
            details_val = json.loads(r["details"]) if r["details"] else {}
        except Exception:
            details_val = {"raw": r["details"]}

        tags_val = []
        try:
            tags_val = json.loads(r["tags"]) if r["tags"] else []
        except Exception:
            tags_val = []

        nodes.append({
            "id": r["id"],
            "label": r["label"],
            "hemisphere": r["hemisphere"],
            "primary_label": r["primary_label"],
            "category": r["category"],
            "tags": tags_val,
            "summary": r["summary"],
            "details": details_val,
            "confidence": r["confidence"] if "confidence" in r.keys() else "EXTRACTED",
            "layer_level": r["layer_level"] if "layer_level" in r.keys() else 0,
            "parent_graph_id": r["parent_graph_id"] if "parent_graph_id" in r.keys() else "root",
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
        })

    links = []
    for e in edges_rows:
        links.append({
            "source": e["source"],
            "target": e["target"],
            "relation": e["relation"],
            "confidence": e["confidence"] if "confidence" in e.keys() else "EXTRACTED"
        })

    return {"nodes": nodes, "links": links}


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


@app.post("/api/memory/ingest", tags=["Memory Ingest"])
def ingest_memory(payload: IngestPayload):
    """
    Atomically ingests or updates nodes and edges extracted from an LLM conversation or uploaded JSON file.
    Enforces taxonomy assignment, translates foreign/CJK tokens to Italian/English, and creates automatic Corpus Callosum cross_links.
    """
    now = datetime.now(timezone.utc).isoformat()
    nodes_upserted = 0
    edges_upserted = 0

    with get_db_connection() as conn:
        # 1. Upsert Nodes
        cross_links_to_add = []
        for n in payload.nodes:
            # Determine node slug ID and human label
            raw_id = (n.id or n.label or "").strip()
            if not raw_id:
                continue
            slug = sanitize_and_translate_text(raw_id).lower().replace(" ", "-").replace("/", "-")
            label = sanitize_and_translate_text((n.label or n.id or slug).strip())

            hemi = (n.hemisphere or "LEFT").upper()
            if hemi not in ("LEFT", "RIGHT"):
                hemi = "LEFT"

            # Determine taxonomy label with intelligent fallbacks
            default_pl = "ARCHITECTURE" if hemi == "LEFT" else "CREATIVE_IDEA"
            primary_label = (n.primary_label or n.category or default_pl).strip().upper()
            category = (n.category or primary_label).strip()

            # Intelligent normalization of details object
            details_obj = n.details or {}
            if not isinstance(details_obj, dict):
                try:
                    details_obj = json.loads(details_obj) if isinstance(details_obj, str) else {}
                except Exception:
                    details_obj = {"raw": str(details_obj)}

            # Auto-enforce metadata rules on backend level
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
            tags_str = json.dumps([sanitize_and_translate_text(t).strip().lower() for t in (n.tags or []) if t.strip()])
            summary = sanitize_and_translate_text((n.summary or f"Concept {label}").strip())

            cursor = conn.execute("SELECT created_at FROM nodes WHERE id = ?", (slug,))
            existing = cursor.fetchone()
            created_at = existing["created_at"] if existing else now

            confidence = getattr(n, "confidence", "EXTRACTED") or "EXTRACTED"
            parent_graph_id = getattr(n, "parent_graph_id", "root") or "root"
            raw_lvl = getattr(n, "layer_level", None)
            layer_level = determine_node_floor_level(slug, primary_label, category, explicit_level=raw_lvl)

            conn.execute("""
                INSERT OR REPLACE INTO nodes 
                (id, label, hemisphere, primary_label, category, tags, summary, details, confidence, parent_graph_id, layer_level, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (slug, label, hemi, primary_label, category, tags_str, summary, details_str, confidence, parent_graph_id, layer_level, created_at, now))
            nodes_upserted += 1

            if n.cross_links:
                for target_id in n.cross_links:
                    tgt = target_id.strip().lower()
                    if tgt and tgt != slug:
                        cross_links_to_add.append((slug, tgt))

        # 2. Insert Corpus Callosum Cross Links
        for slug, tgt in cross_links_to_add:
            c_tgt = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (tgt,)).fetchone()
            if c_tgt:
                conn.execute("""
                    INSERT OR REPLACE INTO edges (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, 'CORPUS_CALLOSUM_LINK', 'EXTRACTED', 'Cross-hemisphere bridge', ?)
                """, (slug, tgt, now))
                edges_upserted += 1

        # 3. Upsert Explicit Edges and Links
        all_edges = list(payload.edges or []) + list(payload.links or [])
        for e in all_edges:
            src = e.source.strip().lower()
            tgt = e.target.strip().lower()
            rel = (e.relation or "CONNECTS_TO").strip().upper().replace(" ", "_")
            edge_conf = getattr(e, "confidence", "EXTRACTED") or "EXTRACTED"
            edge_reason = getattr(e, "reasoning", None)

            c_src = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (src,)).fetchone()
            c_tgt = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (tgt,)).fetchone()

            if c_src and c_tgt:
                conn.execute("""
                    INSERT OR REPLACE INTO edges (source, target, relation, confidence, reasoning, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (src, tgt, rel, edge_conf, edge_reason, now))
                edges_upserted += 1

        conn.commit()

    return {
        "status": "success",
        "message": f"Ingested {nodes_upserted} nodes and {edges_upserted} edges.",
        "nodes_count": nodes_upserted,
        "edges_count": edges_upserted,
        "timestamp": now
    }


@app.get("/api/quick-add", tags=["Memory Ingest"])
def quick_add(
    data: Optional[str] = Query(None, description="Base64 encoded JSON IngestPayload"),
    id: Optional[str] = Query(None, description="Slug ID for the node"),
    label: Optional[str] = Query(None, description="Visible node title"),
    hemisphere: Optional[Literal["LEFT", "RIGHT"]] = Query("LEFT", description="LEFT or RIGHT hemisphere"),
    primary_label: Optional[str] = Query(None, description="Taxonomy primary label"),
    tags: Optional[str] = Query(None, description="Comma-separated tags (e.g. 'auth,jwt,security')"),
    category: Optional[str] = Query(None, description="Category of the node"),
    summary: Optional[str] = Query("", description="Summary of the node"),
    details: Optional[str] = Query("{}", description="JSON string or key:value details"),
    link_to: Optional[str] = Query(None, description="Target node ID to link with (Corpus Callosum or Structure)"),
    relation: Optional[str] = Query("CONNECTS_TO", description="Relationship type"),
    format: Optional[str] = Query("html", description="'html' or 'json'")
):
    """
    One-click browser ingestion endpoint with taxonomy and tag support.
    """
    try:
        nodes_to_add = []
        edges_to_add = []

        if data:
            decoded = base64.b64decode(data).decode("utf-8")
            payload_dict = json.loads(decoded)
            payload = IngestPayload(**payload_dict)
            nodes_to_add = payload.nodes
            edges_to_add = payload.edges
        elif label or id:
            node_id = (id or label or "").strip().lower().replace(" ", "-")
            node_label = label or id or "Untitled Node"
            hemi = hemisphere or "LEFT"
            
            # Default primary_label if missing
            default_pl = "ARCHITECTURE" if hemi == "LEFT" else "CREATIVE_IDEA"
            plabel = (primary_label or default_pl).upper()
            
            tags_list = [t.strip().lower() for t in tags.split(",") if t.strip()] if tags else []

            det_dict = {}
            if details:
                try:
                    det_dict = json.loads(details)
                except Exception:
                    det_dict = {"info": details}

            node = NodeModel(
                id=node_id,
                label=node_label,
                hemisphere=hemi,
                primary_label=plabel,
                category=category or plabel,
                tags=tags_list,
                summary=summary or f"Node added via Quick-Add on {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
                details=det_dict
            )
            nodes_to_add.append(node)

            if link_to:
                edge = EdgeModel(
                    source=node_id,
                    target=link_to.strip().lower(),
                    relation=relation or "CONNECTS_TO"
                )
                edges_to_add.append(edge)
        else:
            raise ValueError("No valid node data provided in query or base64 payload.")

        ingest_res = ingest_memory(IngestPayload(nodes=nodes_to_add, edges=edges_to_add))

        if format == "json":
            return ingest_res

        added_labels = ", ".join(f"<strong>{n.label}</strong> [<code>{n.primary_label}</code>]" for n in nodes_to_add)
        html = f"""
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Memory Ingested - Universal AI Brain</title>
            <style>
                body {{
                    background: #0f172a;
                    color: #f8fafc;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    min-height: 100vh;
                    margin: 0;
                    padding: 20px;
                    box-sizing: border-box;
                }}
                .card {{
                    background: rgba(30, 41, 59, 0.85);
                    border: 1px solid #334155;
                    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5);
                    border-radius: 16px;
                    padding: 32px;
                    max-width: 480px;
                    width: 100%;
                    text-align: center;
                    backdrop-filter: blur(12px);
                }}
                .badge {{
                    display: inline-block;
                    padding: 6px 16px;
                    border-radius: 9999px;
                    font-size: 12px;
                    font-weight: 700;
                    letter-spacing: 1px;
                    text-transform: uppercase;
                    background: linear-gradient(135deg, #00D2FF, #FF007F);
                    color: #0f172a;
                    margin-bottom: 20px;
                }}
                h1 {{ font-size: 24px; margin: 0 0 12px; color: #fff; }}
                p {{ color: #94a3b8; font-size: 14px; line-height: 1.6; margin: 0 0 24px; }}
                .btn {{
                    display: inline-block;
                    background: #38bdf8;
                    color: #0f172a;
                    text-decoration: none;
                    font-weight: 600;
                    padding: 12px 24px;
                    border-radius: 8px;
                    transition: all 0.2s ease;
                }}
                .btn:hover {{ background: #7dd3fc; }}
            </style>
        </head>
        <body>
            <div class="card">
                <div class="badge">Tassonomia Acquisita</div>
                <h1>Memoria Ingestita!</h1>
                <p>Nodi classificati e salvati nel Cervello:<br>{added_labels}</p>
                <a href="/" class="btn">Apri Dashboard 3D</a>
            </div>
        </body>
        </html>
        """
        return HTMLResponse(content=html)

    except Exception as e:
        if format == "json":
            raise HTTPException(status_code=400, detail=str(e))
        return HTMLResponse(content=f"<h3>Errore durante l'acquisizione:</h3><p>{str(e)}</p><a href='/'>Torna alla Home</a>", status_code=400)


@app.get("/api/taxonomy", tags=["Taxonomy"])
def get_taxonomy():
    """Returns official taxonomy choices for left and right hemispheres."""
    return {
        "LEFT": list(LEFT_TAXONOMY),
        "RIGHT": list(RIGHT_TAXONOMY)
    }


@app.get("/api/stats", tags=["System"])
def get_stats():
    """Returns real-time graph metrics, taxonomy breakdown, and tags."""
    with get_db_connection() as conn:
        total_nodes = conn.execute("SELECT COUNT(*) AS c FROM nodes").fetchone()["c"]
        left_nodes = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere='LEFT'").fetchone()["c"]
        right_nodes = conn.execute("SELECT COUNT(*) AS c FROM nodes WHERE hemisphere='RIGHT'").fetchone()["c"]
        total_edges = conn.execute("SELECT COUNT(*) AS c FROM edges").fetchone()["c"]
        
        cross_query = """
            SELECT COUNT(*) AS c FROM edges e
            JOIN nodes s ON e.source = s.id
            JOIN nodes t ON e.target = t.id
            WHERE s.hemisphere != t.hemisphere
        """
        cross_edges = conn.execute(cross_query).fetchone()["c"]

        primary_labels = [r["primary_label"] for r in conn.execute("SELECT DISTINCT primary_label FROM nodes ORDER BY primary_label").fetchall()]
        
        all_tags_raw = conn.execute("SELECT tags FROM nodes").fetchall()
        tags_set = set()
        for r in all_tags_raw:
            try:
                for t in json.loads(r["tags"]):
                    tags_set.add(t)
            except Exception:
                pass

    return {
        "total_nodes": total_nodes,
        "left_hemisphere_nodes": left_nodes,
        "right_hemisphere_nodes": right_nodes,
        "total_edges": total_edges,
        "corpus_callosum_edges": cross_edges,
        "primary_labels": primary_labels,
        "unique_tags_count": len(tags_set),
        "tags": sorted(list(tags_set))
    }


@app.delete("/api/memory/node/{node_id}", tags=["Memory Management"])
def delete_node(node_id: str):
    """Delete a node and cascade its edges."""
    with get_db_connection() as conn:
        cursor = conn.execute("DELETE FROM nodes WHERE id = ?", (node_id.strip().lower(),))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Node not found")
    return {"status": "deleted", "id": node_id}


@app.get("/api/memory/backup", tags=["Memory Management"])
def export_memory_backup():
    """
    Returns complete atomic dump of nodes, edges and metadata for backup & migration.
    """
    with get_db_connection() as conn:
        nodes = [dict(r) for r in conn.execute("SELECT * FROM nodes ORDER BY hemisphere, label").fetchall()]
        edges = [dict(r) for r in conn.execute("SELECT * FROM edges ORDER BY source, target").fetchall()]
    
    for n in nodes:
        try:
            n["tags"] = json.loads(n["tags"]) if n.get("tags") else []
        except Exception:
            pass
        try:
            n["details"] = json.loads(n["details"]) if n.get("details") else {}
        except Exception:
            pass

    return {
        "version": "1.1.0",
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "nodes": nodes,
        "edges": edges
    }


@app.get("/api/memory/download-db", tags=["Memory Management"])
def download_database_file():
    """Download the raw SQLite binary database file."""
    if os.path.exists(DB_PATH):
        # Force checkpoint before serving binary
        with get_db_connection() as conn:
            conn.execute("PRAGMA wal_checkpoint(FULL);")
        return FileResponse(DB_PATH, filename="brain.db", media_type="application/x-sqlite3")
    raise HTTPException(status_code=404, detail="Database file not found")


# -----------------------------------------------------------------------------
# Frontend SPA & Static File Serving
# -----------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
def serve_index():
    """Serves the main single-page 3D WebGL graph dashboard."""
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(
            index_file, 
            media_type="text/html",
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate, max-age=0",
                "Pragma": "no-cache",
                "Expires": "0"
            }
        )
    return HTMLResponse("<h1>Universal AI Brain</h1><p>index.html not found in static folder.</p>")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
