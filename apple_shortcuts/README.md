# 🎙️ Apple Shortcuts & Siri Voice Capture per Universal AI Brain

Questa cartella contiene le istruzioni per impostare il comando vocale con **Siri**, **iPhone**, **Apple Watch** e **Mac** per salvare pensieri, idee e riflessioni nel connettoma cognitivo in mobilità.

---

## ⚡ Come Creare il Comando Rapido su iPhone / Mac (In 1 Minuto)

1. Apri l'app **Comandi Rapidi** (Shortcuts) su iPhone o Mac.
2. Clicca su **"+"** per creare un nuovo comando rapido e nominalo:
   ```
   Appunto per il Cervello
   ```
3. Aggiungi le seguenti 3 azioni in sequenza:

   - **Azione 1: "Dettatura testo" (Dictate Text)**
     - Lingua: *Italiano (Italia)*.
     - Interrompi ascolto: *Dopo una pausa*.

   - **Azione 2: "Ottieni contenuti da URL" (Get Contents of URL)**
     - URL: `https://universal-ai-brain.onrender.com/api/memory/voice-note` (oppure `http://localhost:8000/api/memory/voice-note` se esegui solo in locale)
     - Metodo: **POST**
     - Intestazioni (Headers):
       - `Content-Type`: `application/json`
     - Corpo della richiesta (Request Body): **JSON**
       - Chiave `transcript` (Tipo: *Testo*) $\rightarrow$ Valore: Seleziona la variabile **"Testo dettato"** dello Step 1.
       - Chiave `source` (Tipo: *Testo*) $\rightarrow$ Valore: `siri_voice`

   - **Azione 3: "Mostra notifica" (Show Notification)**
     - Testo: *"🧠 Nota registrata nel cervello!"*

---

## 🗣️ Come Usarlo in Mobilità

- Su iPhone o Apple Watch: *"Ehi Siri, appunto per il cervello"*
- Parla liberamente: *"Oggi ho capito che per scalare un'architettura software la cosa più importante è mantenere il database privo di lock bloccanti..."*
- Siri trascrive l'audio, chiama la tua API gratuita e classifica automaticamente l'idea nell'Emisfero e Macro-Dominio pertinenti!
