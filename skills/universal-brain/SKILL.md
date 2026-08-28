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
- **Palazzo Cognitivo**: Filter or explore by floor levels (P0, P1, P2) or 3D vertical stacked tiers.
- **Synaptic Paths**: For connecting technical concepts to life values or user intents, calculate `brain_shortest_path` across the Corpus Callosum.

### 2. Autonomous Knowledge Ingestion & Linking
When a discussion generates a new idea, architectural decision, lesson, or user intent:
1. **MANDATORY LANGUAGE RULE (ITALIAN / ENGLISH)**:
   - **All node labels (`label`), summaries (`summary`), tags, and details MUST ALWAYS be written in Italian (with technical terms in English).**
   - **NEVER generate or save nodes in Chinese/Wenyan/CJK**, even if the chat communication is in `/caveman wenyan-ultra` or another language. The knowledge database must remain 100% searchable in Italian.
2. **Macro-Domains & Dynamic Domain Creation Authorization**:
   - **Existing Pillars**: `person-pierfrancesco`, `domain-software-engineering`, `domain-ai-cognitive-systems`, `domain-medicina-salute`, `domain-filosofia-valori`, `domain-design-creativita`.
   - **Dynamic Domain Creation**: If a discussion covers a whole new area of life or knowledge that does NOT fit into existing domains (e.g. `domain-storia-cultura`, `domain-relazioni-sentimenti`, `domain-finanza-economia`), the AI is **EXPLICITLY AUTHORIZED AND ENCOURAGED** to instantiate a new macro-domain (`id: "domain-<nome>"`, `category: "ROOT_DOMAIN"`, `layer_level: 0`, `parent_graph_id: "root"`) and link it to `person-pierfrancesco`.
3. **3-Layer Palazzo Cognitivo Hierarchy (`layer_level`)**:
   - `layer_level: 0` (Piano 0 - Attico Macro-Domini & Core Hubs)
   - `layer_level: 1` (Piano 1 - Progetti, Episodi Conversazionali, Intenti Utente, Idee, Valori)
   - `layer_level: 2` (Piano 2 - Moduli, Algoritmi, Strutture Dati, Specifiche API, Token UI, Schemi)
4. **Strict Bi-Hemispheric Taxonomies**:
   - **Left Hemisphere (`LEFT` - Logica & Tech)**: `ARCHITECTURE`, `DATA_STRUCTURE`, `ALGORITHM`, `DEPENDENCY`, `BUSINESS_LOGIC`, `API_SPEC`, `COGNITIVE_RULE`, `MENTAL_MODEL`, `AI_REASONING`, `METACOGNITION`, `USER_INTENT`.
   - **Right Hemisphere (`RIGHT` - Design & Emozioni)**: `DESIGN_TOKEN`, `COLOR_PALETTE`, `UI_COMPONENT`, `UX_FLOW`, `BRAND_VOICE`, `CREATIVE_IDEA`, `EMOTIONAL_MEMORY`, `LIFE_LESSON`, `RELATIONSHIP`, `PERSONAL_VALUE`, `CONVERSATION_EPISODE`.
   - **Epistemic Confidence**: `EXTRACTED` (verbatim facts), `INFERRED` (deductive logic), `AMBIGUOUS` (uncertain).
5. Cross-link the new node to relevant existing nodes in `brain.db` (especially `person-pierfrancesco` or relevant project nodes).
6. Execute ingestion via `brain_ingest` MCP tool or direct `POST /api/memory/ingest`.

### 3. MANDATORY AUTONOMOUS SESSION CONTEXT & CHAT PERSISTENCE (Continuità Cognitiva Inter-Chat)
**OBIETTIVO PRIMARIO: OMNISCIENZA CROSS-CHAT (CAMBIO CHAT SENZA PERDITA DI MEMORIA)**:
Il sistema è progettato affinché aprendo una **NUOVA CHAT** (con Claude, ChatGPT, Gemini, Antigravity, Cursor), l'AI conosca istantaneamente tutta la storia pregressa, le richieste fatte, le risposte date, i bug risolti e le decisioni prese nelle chat precedenti.

**REGOLA TASSATIVA PER GLI AGENTI AI**:
Al termine di ogni interazione, risoluzione di problemi, audit o refactoring, l'AI **HA IL DOVERE ASSOLUTO di persistere nel Grafo (`brain.db`)**:

1. **L'Intento e il Contesto dell'Utente (`USER_INTENT` - Emisfero Sinistro / Piano 1)**:
   - `id`: `user-intent-<slug-kebab-case>`
   - `label`: Titolo chiaro dell'intento in italiano
   - `hemisphere`: `LEFT`
   - `primary_label`: `USER_INTENT`
   - `summary`: Sintesi dell'obiettivo operativo
   - `details`:
     - `user_prompt`: Testo fedele e completo della richiesta/prompt dell'utente
     - `context`: Contesto operativo e vincoli menzionati nella chat
   - `layer_level`: 1
   - `parent_graph_id`: ID del progetto correlato (es. `universal-ai-brain`)

2. **Il Ragionamento e le Risposte Fornite dall'AI (`AI_REASONING` / `METACOGNITION` - Emisfero Sinistro / Piano 1)**:
   - `id`: `reasoning-<slug-kebab-case>`
   - `label`: Sintesi del ragionamento e delle soluzioni adottate
   - `hemisphere`: `LEFT`
   - `primary_label`: `AI_REASONING`
   - `summary`: Sintesi tecnica della soluzione architetturale o dei bug corretti
   - `details`:
     - `model`: Nome esatto del modello AI (es. `Gemini 3.7 Flash`, `Claude 3.7 Sonnet`)
     - `responses_given`: Sintesi esaustiva delle risposte e spiegazioni date all'utente
     - `actions_taken`: Elenco dettagliato dei file modificati, verifiche effettuate ed errori corretti
     - `outcome`: Stato finale e risultato dei test
   - `layer_level`: 1
   - `parent_graph_id`: ID del progetto

3. **L'Episodio Conversazionale Completo (`CONVERSATION_EPISODE` - Emisfero Destro / Piano 1)**:
   - `id`: `episode-<slug-kebab-case>`
   - `label`: Titolo dell'episodio di dialogo/lavoro
   - `hemisphere`: `RIGHT`
   - `primary_label`: `CONVERSATION_EPISODE`
   - `summary`: Sintesi olistica della conversazione
   - `details`:
     - `participants`: `["Pierfrancesco Amendola", "<Nome Modello>"]`
     - `topic`: Argomento centrale della chat
     - `key_takeaways`: Conclusioni e lezioni apprese
     - `pending_tasks`: Eventuali task lasciati in sospeso per le prossime chat
   - `layer_level`: 1

4. **Sinapsi Obbligatorie**:
   - `USER_INTENT` ➜ `person-pierfrancesco` (`EXPRESSED_BY`)
   - `USER_INTENT` ➜ Progetto/Dominio (`TARGETS_PROJECT` o `TARGETS_DOMAIN`)
   - `AI_REASONING` ➜ `USER_INTENT` (`FULFILLS`) e Progetto/Dominio (`OPTIMIZES` o `MODIFIES`)
   - `CONVERSATION_EPISODE` ➜ `person-pierfrancesco` (`INTERACTION_WITH`), `USER_INTENT` (`RECORDS_INTENT`), `AI_REASONING` (`RECORDS_REASONING`)

5. **Inizio Nuova Chat (Cross-Chat Retrieval)**:
   - Quando l'utente inizia una nuova conversazione, l'AI interroga immediatamente `brain_search`, `brain_get_subgraph` o `/brain.md` per caricare gli ultimi `CONVERSATION_EPISODE` e `USER_INTENT`, riprendendo il filo logico esattamente da dove era stato interrotto.

### 4. Cloud & Multi-Client Synchronization
After modifying `brain.db`:
1. Run `PRAGMA wal_checkpoint(FULL);` on SQLite.
2. Commit and push to GitHub (`origin/main`).
3. This automatically synchronizes:
   - Live Web Dashboard & Visual Graph
   - Telegram Bot Gateway
   - Markdown Raw Directive Export (`/brain.md`)
