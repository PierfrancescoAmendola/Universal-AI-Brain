---
id: reasoning-risoluzione-residui-ollama-mac
label: Identificazione Percorsi Storage e Pulizia Ollama macOS
hemisphere: LEFT
primary_label: AI_REASONING
category: AI_REASONING
layer_level: 1
parent_graph_id: domain-system-administration
tags: [ollama, filesystem, bash, diagnosi]
confidence: INFERRED
updated_at: "2026-08-31T10:47:07.048247+00:00"
---

# Identificazione Percorsi Storage e Pulizia Ollama macOS

> **Emisfero:** ⚡ Sinistro (Logic & Tech)  
> **Categoria:** `AI_REASONING` | **Piano:** 1 | **Padre:** [[domain-system-administration]]

## 📝 Sintesi
Analisi dell'architettura di storage di Ollama su macOS: identificati i percorsi ~/.ollama/models/blobs e ~/Library/Application Support/Ollama con relativi comandi di rimozione sicura.

## 📋 Dettagli Strutturati
- **model:** Gemini
- **actions_taken:**
  - Mappatura directory predefinita modelli Ollama (~/.ollama/models/blobs)
  - Fornitura comando di verifica dimensione disco (du -sh)
  - Fornitura comando di eliminazione ricorsiva sicura (rm -rf)
- **outcome:** Istruzioni fornite per il recupero immediato di 7GB di spazio su disco.

## 🔗 Connessioni Uscenti
- [[user-intent-rimozione-modello-ollama-mac]] (`FULFILLS`)

## 📥 Connessioni Entranti (Backlinks)
- [[episode-bonifica-storage-ollama-mac]] (`RECORDS_REASONING`)
