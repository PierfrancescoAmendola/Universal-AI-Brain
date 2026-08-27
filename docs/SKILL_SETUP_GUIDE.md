# 🧠 Universal Brain Skill (`/brain`) Setup Guide

Questa guida spiega come installare e utilizzare la skill **`universal-brain`** (richiamabile con **/brain**) su qualsiasi ambiente di sviluppo, assistente AI (Antigravity, Claude Code, Cursor, Windsurf) o terminale.

---

## ⚡ Installazione Rapida (1 Click)

Se hai clonato questa repository sul tuo computer, esegui semplicemente:

```bash
chmod +x install.sh
./install.sh
```

Questo script installerà automaticamente:
1. Il comando globale **`brain`** nel tuo terminale (`~/.local/bin/brain`).
2. La skill **`universal-brain`** in `~/.agents/skills/universal-brain/SKILL.md`.
3. Le regole globali per gli agenti in `~/.agents/rules/universal-brain.md`.

---

## 🛠️ Come Utilizzare la Skill negli Agenti AI

Quando conversi con **Antigravity**, **Claude Code** o qualsiasi agente abilitato:

### 1. Consultazione del Cervello (GraphRAG)
Digita semplicemente:
> **/brain cosa sappiamo sui progetti SwiftData e sulle architetture iOS?**

L'agente cercherà nel tuo database locale `brain.db` con BM25 FTS5 e recupererà tutte le nozioni correlate, collegando l'Emisfero Sinistro (tecnologia) all'Emisfero Destro (valori, design).

### 2. Salvataggio e Connessione di Nuove Idee
Quando hai un'idea o concludi una sessione di architettura:
> **/brain Ho pensato a un nuovo modulo di cache per l'app. Salvalo e collegalo al progetto principale.**

L'agente estrarrà i concetti, assegnerà le tassonomie corrette (`ARCHITECTURE`, `CREATIVE_IDEA`, `USER_INTENT`), salverà il nodo in `brain.db` e sincronizzerà il grafo su GitHub e sul Web.

---

## 💻 Comandi CLI da Terminale

Puoi interagire con il tuo cervello anche direttamente dal tuo terminale:

```bash
# Mostra le metriche globali
brain stats

# Cerca un concetto con BM25
brain search flutter

# Mostra la gerarchia delle categorie (層級譜系樹)
brain tree

# Aggiungi una nota o idea al volo
brain add "Idea per Bot AI" "Descrizione sintetica del progetto"

# Apri la Web Dashboard nel browser
brain open
```
