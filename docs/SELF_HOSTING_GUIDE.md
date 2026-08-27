# 🌐 Self-Hosting & 0€ Deployment Guide

L'Universal AI Brain è stato progettato per operare a **costo zero (0€)** in modo permanente, sfruttando:
- **FastAPI** (Python 3.10+) per l'API ad alte prestazioni.
- **SQLite in WAL Mode + FTS5** per persistenza robusta, concorrenza e ricerca testuale istantanea senza database esterni a pagamento.
- **Render.com Free Tier** (oppure Fly.io, Railway, VPS, Raspberry Pi, Docker).

---

## 🚀 Deploy in 1-Click su Render.com (Gratis)

1. Esegui il **Fork** di questa repository sul tuo account GitHub.
2. Vai su **[dashboard.render.com](https://dashboard.render.com/)**.
3. Clicca su **New +** ➜ **Web Service**.
4. Seleziona il tuo repository GitHub appena forkkato.
5. Render rileverà automaticamente il file `render.yaml` pre-configurato:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan:** `Free`
6. Clicca su **Create Web Service**.

Il tuo cervello artificiale sarà online in meno di 2 minuti con HTTPS gratuito e interfaccia interattiva!

---

## 💻 Esecuzione in Locale

```bash
# 1. Clona la repository
git clone https://github.com/PierfrancescoAmendola/Universal-AI-Brain.git
cd Universal-AI-Brain

# 2. Crea l'ambiente virtuale
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Avvia il server
uvicorn main:app --reload --port 8000
```

Apri `http://localhost:8000` nel browser per vedere la mappa del cervello interattiva.
