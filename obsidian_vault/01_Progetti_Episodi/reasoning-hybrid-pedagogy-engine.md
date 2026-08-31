---
id: reasoning-hybrid-pedagogy-engine
label: Design Pedagogico Ibrido (Busuu Grammar + Duolingo Micro-Drill)
hemisphere: LEFT
primary_label: AI_REASONING
category: AI_REASONING
layer_level: 1
parent_graph_id: domain-design-creativita
tags: [pedagogical-engine, cloze-test, word-bank, cefr-schema, sqlite-schema]
confidence: EXTRACTED
updated_at: "2026-08-29T20:50:00Z"
---

# Design Pedagogico Ibrido (Busuu Grammar + Duolingo Micro-Drill)

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `AI_REASONING` | **Piano:** 1 | **Padre:** [[domain-design-creativita]]

## 📝 Sintesi
Progettazione di un motore a 6 tipologie di esercizio con schede grammaticali preparatorie (stile Busuu) e micro-lezioni a bolle interattive (stile Duolingo) supportate da SQLite e batch generation da corpora di frequenza.

## 📋 Dettagli Strutturati
- **raw:** `exercise_types`: ['Word Bank', 'Cloze Test', 'Matching Pairs', 'Audio Listen', 'Active Recall', 'Grammar Spotlight'], `penalty_rule`: Re-queue on failure without blocking energy, `model`: AI Assistant

## 🔗 Connessioni Uscenti
- [[episode-language-app-architecture]] (`CORPUS_CALLOSUM_LINK`) — _Restored from history_
- [[intent-personal-language-app-structure]] (`SOLVES`) — _Restored from history_
