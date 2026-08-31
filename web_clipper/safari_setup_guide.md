# 🧭 Guida all'Installazione del Web Clipper su Safari (macOS)

Questa guida spiega come abilitare il **Web Clipper di Universal AI Brain** direttamente all'interno di **Apple Safari** su macOS a **costo zero (0,00€)**.

---

## Metodo Rapido: Abilitazione Sviluppatore Safari (Senza Xcode)

1. Apri **Safari**.
2. Nella barra dei menu in alto, clicca su **Safari** $\rightarrow$ **Impostazioni...** (oppure `Cmd + ,`).
3. Vai nella scheda **Avanzate** e spunta l'opzione:
   - ✅ **"Mostra funzionalità per sviluppatori web"** (o *"Mostra menu Sviluppo nella barra dei menu"*).
4. Nel nuovo menu **Sviluppo** comparso in alto, seleziona:
   - ✅ **"Consenti estensioni non firmate"** (Allow Unsigned Extensions).
5. In alternativa, puoi convertire l'estensione con il comando nativo Apple built-in:
   ```bash
   xcrun safari-web-extension-converter /Users/pierfrancesco/Desktop/CervelloArtificiale/web_clipper
   ```
   Questo comando creerà in 5 secondi un progetto Xcode compatto che potrai avviare premendo `Cmd + R`, registrando l'estensione direttamente in Safari!

---

## ⚡ Come Usarlo su Safari

1. Naviga su un articolo, un post o una documentazione tecnica.
2. Evidenzia la frase o il paragrafo che desideri salvare.
3. Clicca sull'icona **🧠 Universal Brain** nella barra degli strumenti di Safari.
4. Il clipper compilerà automaticamente:
   - Titolo della pagina
   - URL sorgente
   - Testo selezionato
   - Emisfero stimato (`LEFT` ⚡ o `RIGHT` 🌸)
   - Macro-Dominio di appartenenza
5. Clicca **"Salva nel Connettoma"**: il nodo e i collegamenti verranno inseriti istantaneamente nel tuo database SQLite WAL e su Render!
