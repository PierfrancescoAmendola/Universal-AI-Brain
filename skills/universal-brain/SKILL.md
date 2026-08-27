---
name: universal-brain
description: >
  Connects AI assistants (Antigravity, Claude, Cursor, Gemini) directly to a Persistent Bi-Hemispheric Knowledge Graph.
  Use when user says "/brain", "cerca nel cervello", "salva nel cervello", "collega al cervello", "ricorda nel cervello",
  "chiedi al cervello", "universal brain", or whenever querying, cross-referencing, or ingesting new ideas, architectural
  decisions, project state, values, or emotional memories.
---

# Universal AI Brain Skill (`/brain`)

Operates directly on the Persistent Bi-Hemispheric Knowledge Graph (`brain.db`).

## Core Capabilities & Agent Directives

Whenever the user invokes `/brain` or asks to query/save thoughts in their brain:

### 1. Automatic Search & Context Retrieval (GraphRAG)
Before formulating an answer or generating a new proposal, search what the brain already knows:
- **Search**: Run BM25 FTS5 search on `brain.db` or invoke MCP `brain_search` with relevant keywords.
- **Hierarchy Zoom**: For broad topics, query `brain_get_tree` to see the macro-taxonomies.
- **Synaptic Paths**: For connecting technical concepts to life values or user intents, calculate `brain_shortest_path` across the Corpus Callosum.

### 2. Autonomous Knowledge Ingestion & Linking
When a discussion generates a new idea, architectural decision, lesson, or user intent:
1. **MANDATORY LANGUAGE RULE (ITALIAN / ENGLISH)**:
   - **All node labels (`label`), summaries (`summary`), tags, and details MUST ALWAYS be written in Italian (with technical terms in English).**
   - **NEVER generate or save nodes in Chinese/Wenyan/CJK**, even if the chat communication is in `/caveman wenyan-ultra` or another language. The knowledge database must remain 100% searchable in Italian.
2. Formulate the JSON ingestion payload with strict taxonomies:
   - **Left Hemisphere (`LEFT`)**: `ARCHITECTURE`, `DATA_STRUCTURE`, `ALGORITHM`, `DEPENDENCY`, `BUSINESS_LOGIC`, `API_SPEC`, `COGNITIVE_RULE`, `MENTAL_MODEL`, `AI_REASONING`, `METACOGNITION`, `USER_INTENT`.
   - **Right Hemisphere (`RIGHT`)**: `DESIGN_TOKEN`, `COLOR_PALETTE`, `UI_COMPONENT`, `UX_FLOW`, `BRAND_VOICE`, `CREATIVE_IDEA`, `EMOTIONAL_MEMORY`, `LIFE_LESSON`, `RELATIONSHIP`, `PERSONAL_VALUE`, `CONVERSATION_EPISODE`.
   - **Epistemic Confidence**: `EXTRACTED` (verbatim facts), `INFERRED` (deductive logic), `AMBIGUOUS` (uncertain).
3. Cross-link the new node to relevant existing nodes in `brain.db` (especially `person-pierfrancesco` or relevant project nodes).
4. Execute ingestion via `brain_ingest` MCP tool or direct `POST /api/memory/ingest`.

### 3. Cloud & Multi-Client Synchronization
After modifying `brain.db`:
1. Run `PRAGMA wal_checkpoint(FULL);` on SQLite.
2. Commit and push to GitHub (`origin/main`).
3. This automatically synchronizes:
   - Live Web Dashboard & Visual Graph
   - Telegram Bot Gateway
   - Markdown Raw Directive Export (`/brain.md`)
