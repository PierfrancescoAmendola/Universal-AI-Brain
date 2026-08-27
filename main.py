"""Universal AI Brain - Persistent Bi-Hemispheric Knowledge Graph Backend
Production-ready FastAPI application with SQLite persistence, zero operational cost,
strict taxonomy labeling engine, and cognitive meta-prompts for LLMs.
"""

import os
import json
import sqlite3
import base64
import urllib.parse
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
    "MENTAL_MODEL"
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
    "PERSONAL_VALUE"
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

        conn.execute("""
            CREATE TABLE IF NOT EXISTS edges (
                source TEXT NOT NULL,
                target TEXT NOT NULL,
                relation TEXT NOT NULL,
                created_at TEXT NOT NULL,
                PRIMARY KEY (source, target, relation),
                FOREIGN KEY (source) REFERENCES nodes(id) ON DELETE CASCADE,
                FOREIGN KEY (target) REFERENCES nodes(id) ON DELETE CASCADE
            );
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
    id: str = Field(..., description="Unique alphanumeric slug, e.g. 'auth-jwt-system'")
    label: str = Field(..., description="Human readable title")
    hemisphere: Literal["LEFT", "RIGHT"] = Field(..., description="'LEFT' for logic/tech, 'RIGHT' for design/creative")
    primary_label: str = Field(
        ...,
        description="Mandatory taxonomy label. LEFT: ARCHITECTURE, DATA_STRUCTURE, ALGORITHM, DEPENDENCY, BUSINESS_LOGIC, API_SPEC. RIGHT: DESIGN_TOKEN, COLOR_PALETTE, UI_COMPONENT, UX_FLOW, BRAND_VOICE, CREATIVE_IDEA."
    )
    category: Optional[str] = Field(None, description="Optional subcategory or alias; defaults to primary_label")
    tags: List[str] = Field(default_factory=list, description="Array of atomic micro-tags (e.g. ['python', 'fastapi'])")
    cross_links: List[str] = Field(default_factory=list, description="Opposite hemisphere node IDs to automatically connect across the Corpus Callosum")
    summary: str = Field(..., description="Concise summary for LLM context")
    details: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Key-value object with structured details")


class EdgeModel(BaseModel):
    source: str = Field(..., description="Source node ID")
    target: str = Field(..., description="Target node ID")
    relation: str = Field(default="CONNECTS_TO", description="Relationship label in UPPER_SNAKE_CASE")


class IngestPayload(BaseModel):
    nodes: List[NodeModel] = Field(default_factory=list, description="List of nodes to upsert")
    edges: List[EdgeModel] = Field(default_factory=list, description="List of explicit edges to upsert")


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
# Core Endpoints
# -----------------------------------------------------------------------------

@app.get("/health", tags=["System"])
def health_check():
    """Healthcheck endpoint for hosting providers."""
    return {"status": "alive", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.get("/brain.md", tags=["Memory Access"])
def get_brain_markdown(
    q: Optional[str] = Query(None, description="Search term filter"),
    tag: Optional[str] = Query(None, description="Tag filter"),
    primary_label: Optional[str] = Query(None, description="Primary taxonomy filter")
):
    """
    Returns complete bi-hemispheric graph memory formatted with the mandatory
    System Cognitive Meta-Directive at the very top.
    """
    with get_db_connection() as conn:
        nodes_cursor = conn.execute("SELECT * FROM nodes ORDER BY hemisphere, primary_label, label")
        nodes = [dict(row) for row in nodes_cursor.fetchall()]

        edges_cursor = conn.execute("SELECT * FROM edges ORDER BY relation, source")
        edges = [dict(row) for row in edges_cursor.fetchall()]

    # Filter logic
    if q and q.strip():
        search = q.strip().lower()
        matched_ids = set()
        filtered = []
        for n in nodes:
            combined = f"{n['id']} {n['label']} {n['primary_label']} {n['category']} {n['tags']} {n['summary']} {n['details']}".lower()
            if search in combined:
                filtered.append(n)
                matched_ids.add(n['id'])
        nodes = filtered
        edges = [e for e in edges if e["source"] in matched_ids or e["target"] in matched_ids]

    if tag and tag.strip():
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

    if primary_label and primary_label.strip():
        pl_search = primary_label.strip().upper()
        nodes = [n for n in nodes if n["primary_label"] == pl_search]
        node_ids = {n["id"] for n in nodes}
        edges = [e for e in edges if e["source"] in node_ids or e["target"] in node_ids]

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

    # MANDATORY Cognitive System Directive at the top
    md = f"""# DIRETTIVA DI SISTEMA COGNITIVA (MANDATORIA)
Sei connesso al cervello artificiale universale. Ogni informazione, codice, stile o idea che produrrai in questa sessione DEVE essere categorizzata prima del salvataggio.
Regole di smistamento:
1. Emisfero Sinistro (LEFT): Logica pura, algoritmi, codice, architettura, regole deterministiche.
   - Primary Labels ammesse: ARCHITECTURE, DATA_STRUCTURE, ALGORITHM, DEPENDENCY, BUSINESS_LOGIC, API_SPEC.
2. Emisfero Destro (RIGHT): Design system, palette colori, componenti UI/UX, memorie, creatività.
   - Primary Labels ammesse: DESIGN_TOKEN, COLOR_PALETTE, UI_COMPONENT, UX_FLOW, BRAND_VOICE, CREATIVE_IDEA.
3. Obbligo Label: Ogni nuovo elemento deve includere 'primary_label' (macro-categoria) e 'tags' (micro-etichette atomiche).
4. A fine sessione, restituisci sempre il blocco JSON formattato per l'endpoint /api/memory/ingest.

---

# STATO CORRENTE DEL GRAFO COGNITIVO
> **Data Generazione:** {now_str} | **Nodi:** {len(nodes)} | **Sinapsi:** {len(edges)}

## EMISFERO SINISTRO (Logica, Tech, Architetture)
{format_nodes_section(left_nodes)}

## EMISFERO DESTRO (Design, Stili, Idee)
{format_nodes_section(right_nodes)}

## CONNESSIONI TRASVERSALI (Corpo Calloso & Struttura)
### Ponti Inter-Emisfero (Corpo Calloso):
{chr(10).join(cross_links) if cross_links else '_Nessuna sinapsi inter-emisferica registrata._'}

### Altre Connessioni di Struttura:
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
            "created_at": r["created_at"],
            "updated_at": r["updated_at"]
        })

    links = []
    for e in edges_rows:
        links.append({
            "source": e["source"],
            "target": e["target"],
            "relation": e["relation"]
        })

    return {"nodes": nodes, "links": links}


@app.post("/api/memory/ingest", tags=["Memory Ingest"])
def ingest_memory(payload: IngestPayload):
    """
    Atomically ingests or updates nodes and edges extracted from an LLM conversation.
    Enforces taxonomy assignment and creates automatic Corpus Callosum cross_links.
    """
    now = datetime.now(timezone.utc).isoformat()
    nodes_upserted = 0
    edges_upserted = 0

    with get_db_connection() as conn:
        # 1. Upsert Nodes
        cross_links_to_add = []
        for n in payload.nodes:
            slug = n.id.strip().lower()
            details_str = json.dumps(n.details or {})
            tags_str = json.dumps([t.strip().lower() for t in n.tags if t.strip()])
            primary_label = n.primary_label.strip().upper()
            category = (n.category or primary_label).strip()

            cursor = conn.execute("SELECT created_at FROM nodes WHERE id = ?", (slug,))
            existing = cursor.fetchone()
            created_at = existing["created_at"] if existing else now

            conn.execute("""
                INSERT OR REPLACE INTO nodes 
                (id, label, hemisphere, primary_label, category, tags, summary, details, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (slug, n.label.strip(), n.hemisphere, primary_label, category, tags_str, n.summary.strip(), details_str, created_at, now))
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
                    INSERT OR REPLACE INTO edges (source, target, relation, created_at)
                    VALUES (?, ?, 'CORPUS_CALLOSUM_LINK', ?)
                """, (slug, tgt, now))
                edges_upserted += 1

        # 3. Upsert Explicit Edges
        for e in payload.edges:
            src = e.source.strip().lower()
            tgt = e.target.strip().lower()
            rel = e.relation.strip().upper().replace(" ", "_")

            c_src = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (src,)).fetchone()
            c_tgt = conn.execute("SELECT 1 FROM nodes WHERE id = ?", (tgt,)).fetchone()

            if c_src and c_tgt:
                conn.execute("""
                    INSERT OR REPLACE INTO edges (source, target, relation, created_at)
                    VALUES (?, ?, ?, ?)
                """, (src, tgt, rel, now))
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


# -----------------------------------------------------------------------------
# Frontend SPA & Static File Serving
# -----------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
def serve_index():
    """Serves the main single-page 3D WebGL graph dashboard."""
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file, media_type="text/html")
    return HTMLResponse("<h1>Universal AI Brain</h1><p>index.html not found in static folder.</p>")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
