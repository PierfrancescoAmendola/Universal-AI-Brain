# 🛠️ IDE & Terminal Auto-Hooks - Universal AI Brain

Questa cartella contiene gli hook automatici per integrare il connettoma in **Cursor**, **Claude Code**, **Antigravity** e nel **Terminale di macOS**.

---

## 📦 Script Inclusi

1. **🚀 `session_start_context.py` (Pre-Session Hook)**
   - Ispeziona il progetto attivo e stampa il contesto essenziale (<400 token) con preferenze storiche e decisioni pregresse.
   - **Utilizzo rapido:**
     ```bash
     python3 ide_hooks/session_start_context.py
     ```

2. **💾 `session_end_ingest.py` (Post-Session Hook)**
   - Ispeziona il `git status` / `diff` della cartella ed esegue l'ingestione automatica della **Triade di Sessione** (`USER_INTENT`, `AI_REASONING`, `CONVERSATION_EPISODE`) con le 7 sinapsi obbligatorie.
   - **Utilizzo rapido:**
     ```bash
     python3 ide_hooks/session_end_ingest.py "Implementazione Web Clipper e Raycast" "Aggiunti script e testati con successo."
     ```
