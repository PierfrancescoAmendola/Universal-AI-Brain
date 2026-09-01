---
id: concept-llm-indirect-injection-safeguard
label: "Regola Cognitiva: Gestione dei Filtri Anti-Injection nei Modelli Web"
hemisphere: LEFT
primary_label: COGNITIVE_RULE
category: COGNITIVE_RULE
layer_level: 1
parent_graph_id: domain-ai-cognitive-systems
tags: [cognitive-rule, prompt-injection, llm-safety, claude-ai-guardrails, memory-ingestion]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# Regola Cognitiva: Gestione dei Filtri Anti-Injection nei Modelli Web

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `COGNITIVE_RULE` | **Piano:** 1 | **Padre:** [[domain-ai-cognitive-systems]]

## 📝 Sintesi
Protocollo di interazione con modelli web: evitare comandi imperativi di rete esterna (es. ordini di POST verso URL terzi) nei file allegati, preferendo il formato standard di blocco JSON in calce.

## 📋 Dettagli Strutturati
- **raw:** `cause_of_refusal`: I filtri di Anthropic/OpenAI rilevano istruzioni di esfiltrazione dati se un prompt/file ordina chiamate POST o fetch verso siti terzi., `recommended_protocol`: Allegare brain.md e chiedere la generazione del blocco di codice JSON da incollare con 1-click nella Web Dashboard.

## 🔗 Connessioni Uscenti
- [[ai-reasoning-hybrid-cloud-local-symbiosis]] (`PREVENTS_FALSE_POSITIVES_IN`) — _Disegnato su Obsidian Canvas_
- [[domain-ai-cognitive-systems]] (`COGNITIVE_RULE_OF`) — _Disegnato su Obsidian Canvas_
- [[ep-20260827-render-cloud-vs-local-hybrid-architecture]] (`BELONGS_TO_EPISODE`) — _Disegnato su Obsidian Canvas_
- [[intent-clarify-render-cloud-utility-and-llm-web-refusal]] (`RESOLVES_ISSUE_OF`) — _Disegnato su Obsidian Canvas_
- [[universal-ai-brain]] (`GOVERNS_INGESTION_FOR`) — _Disegnato su Obsidian Canvas_
