# 📱 Telegram Bot Gateway Setup Guide

Il modulo Telegram permette di avere un'interfaccia mobile ovunque ti trovi per interrogare il cervello, cercare progetti, vedere i log e salvare nuove idee al volo a **0,00€ di costo operativo**.

---

## 🚀 Configurazione in 3 Passaggi

### 1. Crea il Bot con @BotFather
1. Apri Telegram e cerca **`@BotFather`**.
2. Invia il comando `/newbot`.
3. Scegli un nome e un username che finisca con `bot` (es. `mio_cervello_bot`).
4. Copia il **Token API** generato.

### 2. Imposta le Variabili d'Ambiente
Sul tuo server di hosting (es. **Render.com**), aggiungi le seguenti *Environment Variables*:
- `TELEGRAM_BOT_TOKEN`: Il token ottenuto da BotFather.
- `TELEGRAM_ADMIN_ID`: (Opzionale) Il tuo ID numerico Telegram per consentire l'accesso solo a te.
- `RENDER_EXTERNAL_URL`: L'URL pubblico del tuo servizio (es. `https://universal-ai-brain.onrender.com`).

### 3. Registra il Webhook
Esegui una richiesta GET via browser o terminale:
```bash
curl "https://api.telegram.org/bot<TUO_TOKEN>/setWebhook?url=https://TUA-APP-RENDER.onrender.com/api/telegram/webhook"
```

---

## 💬 Comandi Supportati su Telegram

- `/start` o `/menu`: Mostra il menu con la tastiera rapida.
- `/stats`: Statistiche globali su nodi, emisferi e sinapsi.
- `/search <termine>`: Ricerca BM25 istantanea nei nodi.
- `/tree`: Visualizzazione dell'albero gerarchico delle categorie.
- `/terminal` o `/logs`: Console live con gli ultimi nodi inseriti e le sinapsi create.
- `/path <id1> <id2>`: Calcolo del percorso minimo tra due concetti.
- **Incolla JSON di ChatGPT / Claude**: Incollando qualsiasi blocco JSON, il bot lo convalida e lo inserisce all'istante nel database!
- **Messaggio libero**: Qualsiasi testo inviato viene automaticamente salvato come nuova memoria (`CREATIVE_IDEA`).
