# 🚀 Guida al Deploy Gratuito su Hugging Face Spaces (16GB RAM · 2 vCPU · 0,00€)

Dato che Koyeb è stata recentemente acquisita da Mistral AI e ha congelato la creazione di nuovi servizi self-service, **Hugging Face Spaces** è oggi la **migliore piattaforma cloud gratuita al mondo** per ospitare il tuo Cervello Artificiale:

- 🟢 **100% Gratuito per sempre** (nessuna carta di credito richiesta).
- ⚡ **Risorse Enormi:** 2 vCPU e **16 GB di RAM** (32 volte la RAM di Render!).
- 🔑 **Accesso con 1 Clic tramite GitHub:** usi direttamente il tuo account GitHub su Hugging Face.
- 🐳 **Supporto Docker Nativo:** legge automaticamente il nostro `Dockerfile`.
- 🌐 **URL Pubblico HTTPS Diretto:** `https://<tuo-username>-universal-ai-brain.hf.space`.

---

## 📋 Passaggio 1: Crea lo Space su Hugging Face (1 Minuto)

1. Vai su **[huggingface.co](https://huggingface.co)** e accedi cliccando su **"Log In"** ➔ **"Continue with GitHub"**.
2. Una volta dentro, vai direttamente su **[huggingface.co/new-space](https://huggingface.co/new-space)** (o clicca sulla tua foto profilo in alto a destra ➔ **"New Space"**).
3. Compila i campi:
   - **Space name:** `universal-ai-brain`
   - **License:** `mit`
   - **Select the Space SDK:** Seleziona **Docker** (scegli il template **Blank**).
   - **Space hardware:** Lascia selezionato **CPU basic · 2 vCPU · 16 GB · FREE**.
   - **Visibility:** Seleziona **Public** (necessario per far raggiungere le API dal bot Telegram e dalle scorciatoie Apple).
4. Clicca sul pulsante in basso **"Create Space"**.

---

## 💻 Passaggio 2: Invia il Codice allo Space dal Tuo Terminale

Hugging Face Spaces ti mostrerà una pagina con l'indirizzo Git del tuo Space.

Apri il terminale del tuo Mac ed esegui questi comandi (sostituendo `<TUO-USERNAME-HF>` con il tuo username Hugging Face):

```bash
cd /Users/pierfrancesco/Desktop/CervelloArtificiale

# 1. Aggiungi il remote di Hugging Face (sostituisci il tuo username)
git remote add space https://huggingface.co/spaces/<TUO-USERNAME-HF>/universal-ai-brain

# 2. Invia il codice (quando chiede la password, usa un Access Token di Hugging Face)
git push space main
```

> [!TIP]
> **Come creare l'Access Token su Hugging Face (se richiesto da Git):**
> Su Hugging Face, vai su **Settings** ➔ **Access Tokens** ➔ **Create new token** (Ruolo: `Write`), copialo e incollalo come password quando Git te lo richiede.

---

## 🌐 Passaggio 3: Il Tuo Nuovo URL Cloud

In circa 60 secondi Hugging Face compilerà il container Docker e lo stato passerà a **Running (Verde)**.

L'URL pubblico del tuo server sarà:
```text
https://<TUO-USERNAME-HF>-universal-ai-brain.hf.space
```

Puoi verificare subito:
- Dashboard 3D: `https://<TUO-USERNAME-HF>-universal-ai-brain.hf.space`
- Swagger Docs: `https://<TUO-USERNAME-HF>-universal-ai-brain.hf.space/docs`
- Healthcheck: `https://<TUO-USERNAME-HF>-universal-ai-brain.hf.space/health`
- Grafo JSON: `https://<TUO-USERNAME-HF>-universal-ai-brain.hf.space/brain.json`

---

## 🍏 Passaggio 4: Riconnetti il Demone Locale Mac

Sul tuo Mac esegui il comando per ricollegare il demone di sincronizzazione automatica al nuovo URL:

```bash
cd /Users/pierfrancesco/Desktop/CervelloArtificiale
./install_daemon.sh "https://<TUO-USERNAME-HF>-universal-ai-brain.hf.space"
```

---

## 📱 Passaggio 5: Aggiorna il Webhook Telegram

Esegui da terminale per reindirizzare il bot Telegram:

```bash
curl "https://api.telegram.org/bot8615414934:AAEGBkrHPQaEestCzHMDSEB6iKyYYTOK7LY/setWebhook?url=https://<TUO-USERNAME-HF>-universal-ai-brain.hf.space/api/telegram/webhook"
```
