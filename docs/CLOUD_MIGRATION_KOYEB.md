# 🚀 Guida Rapida: Deploy Gratuito 24/7 su Koyeb

Questa guida ti accompagna nel deploy del tuo **Universal AI Brain** su **Koyeb**, una piattaforma cloud moderna e gratuita che sostituisce Render offrendo:
- 🟢 **100% Gratuito per sempre** (Piano *Free Nano*: 512MB RAM, 0.1 vCPU).
- ⚡ **Zero Standby / Sleep:** il server rimane **attivo 24 ore su 24, 7 giorni su 7** (non si addormenta dopo 15 minuti come Render).
- 🔄 **Deploy Automatico da GitHub:** a ogni `git push` su `main`, Koyeb aggiorna l'istanza cloud in pochi secondi.
- 🔒 **HTTPS & Dominio Gratuito:** es. `https://universal-ai-brain-<username>.koyeb.app`.

---

## 📋 Passaggio 1: Creazione del Servizio su Koyeb (2 Minuti)

1. Accedi alla tua dashboard su **[app.koyeb.com](https://app.koyeb.com/)** (con l'account GitHub appena creato).
2. Clicca sul pulsante verde **"Create Service"** (oppure **"Deploy"**).
3. Seleziona **GitHub** come sorgente di deploy.
4. Seleziona il repository: **`PierfrancescoAmendola/Universal-AI-Brain`**.
5. Configura le opzioni di build:
   - **Deployment method:** Lascia selezionato **Dockerfile** (Koyeb rileverà automaticamente il `Dockerfile` incluso nel repository) oppure **Buildpack**.
   - **Branch:** `main`.
   - **Region:** Scegli **Frankfurt (fra)** per avere la latenza più bassa possibile dall'Italia.
   - **Instance type:** Scegli **Nano (Free)** (512 MB RAM, 0.1 vCPU, 0.00€/mese).
6. **Porta:**
   - Verifica che la porta esposta sia **8000** (Protocol: HTTP).
7. *(Facoltativo)* **Environment Variables:**
   Puoi aggiungere le variabili d'ambiente utili per il bot Telegram e la persistenza:
   - `TELEGRAM_BOT_TOKEN`: `8615414934:AAEGBkrHPQaEestCzHMDSEB6iKyYYTOK7LY` (o il tuo token)
   - `GITHUB_TOKEN`: tuo token GitHub (se desideri che il cloud faccia auto-push quando riceve ingestion web/telegram)
8. Assegna un nome all'app (es. `universal-ai-brain`) e clicca su **"Deploy"**.

---

## 🌐 Passaggio 2: Recupera il Tuo Nuovo URL Cloud

In circa 60-90 secondi lo stato passerà a **Healthy (Green)**.
Koyeb ti mostrerà il tuo nuovo URL pubblico sicuro, ad esempio:
`https://universal-ai-brain-pierfrancesco.koyeb.app`

Puoi verificare subito nel browser che risponda:
- Web Dashboard: `https://<tuo-servizio>.koyeb.app`
- Healthcheck: `https://<tuo-servizio>.koyeb.app/health`
- Grafo JSON: `https://<tuo-servizio>.koyeb.app/brain.json`

---

## 🍏 Passaggio 3: Collega il Demone di Sincronizzazione Locale (Mac)

Una volta ottenuto il nuovo URL da Koyeb, aggiorna il demone di background del tuo Mac con **1 solo comando**:

```bash
cd /Users/pierfrancesco/Desktop/CervelloArtificiale
./install_daemon.sh "https://<IL-TUO-URL-KOYEB>.koyeb.app"
```

Questo comando:
1. Imposta la variabile `CLOUD_BRAIN_URL` nel runner e nel `LaunchAgent`.
2. Riavvia istantaneamente il servizio di background.
3. Esegue la prima sincronizzazione bidirezionale tra il tuo `brain.db` locale e il nuovo server Koyeb.

---

## 📱 Passaggio 4: Aggiorna il Webhook del Bot Telegram (1-Click)

Per far ricevere al bot Telegram i comandi sul nuovo server online, esegui questo comando da terminale sostituendo l'URL:

```bash
curl "https://api.telegram.org/bot8615414934:AAEGBkrHPQaEestCzHMDSEB6iKyYYTOK7LY/setWebhook?url=https://<IL-TUO-URL-KOYEB>.koyeb.app/api/telegram/webhook"
```

Telegram risponderà:
`{"ok":true,"result":true,"description":"Webhook was set"}`

---

## 📲 Passaggio 5: Aggiorna Apple Shortcuts & Web Clipper (Se Usati)

- **Apple Shortcuts (Note Vocali):**
  Nel tuo flusso Rapido su iPhone/Mac, aggiorna l'URL della chiamata POST da `https://universal-ai-brain.onrender.com/api/memory/voice-note` a:
  `https://<IL-TUO-URL-KOYEB>.koyeb.app/api/memory/voice-note`

- **Web Clipper Chrome/Safari:**
  Se usi l'estensione, l'endpoint per salvare articoli e note è ora:
  `https://<IL-TUO-URL-KOYEB>.koyeb.app/api/memory/ingest`
