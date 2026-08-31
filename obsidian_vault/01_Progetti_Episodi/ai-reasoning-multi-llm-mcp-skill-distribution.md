---
id: ai-reasoning-multi-llm-mcp-skill-distribution
label: "Deduzione AI: Architettura di Distribuzione MCP + System Directives Cross-Modello"
hemisphere: LEFT
primary_label: AI_REASONING
category: AI_REASONING
layer_level: 1
parent_graph_id: domain-ai-cognitive-systems
tags: [ai-reasoning, mcp-distribution, cognitive-prompting]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# Deduzione AI: Architettura di Distribuzione MCP + System Directives Cross-Modello

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `AI_REASONING` | **Piano:** 1 | **Padre:** [[domain-ai-cognitive-systems]]

## 📝 Sintesi
Claude Desktop e Antigravity usano JSON-RPC stdio MCP; ChatGPT usa OpenAPI Actions HTTPS su Render; tutti condividono il protocollo /universal-brain.

## 📋 Dettagli Strutturati
- **raw:** `claude_config`: ~/Library/Application Support/Claude/claude_desktop_config.json, `gemini_antigravity`: ~/.gemini/antigravity/mcp_config.json, `chatgpt_actions`: https://universal-ai-brain.onrender.com/openapi.json, `model`: Claude

## 🔗 Connessioni Uscenti
- [[skill-universal-brain-installed]] (`VALIDATES_IMPLEMENTATION`) — _Restored from history_

## 📥 Connessioni Entranti (Backlinks)
- [[domain-ai-cognitive-systems]] (`BELONGS_TO_DOMAIN`) — _Restored from history_
- [[user-intent-connect-gemini-claude-chatgpt-mcp]] (`GENERATES_REASONING`) — _Restored from history_
