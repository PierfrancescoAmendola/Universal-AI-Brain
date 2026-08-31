// Web Clipper Client Logic - Universal AI Brain
const CLOUD_URL = "https://universal-ai-brain.onrender.com/api/memory/ingest";
const LOCAL_URL = "http://localhost:8000/api/memory/ingest";

let currentEndpoint = CLOUD_URL;

document.addEventListener("DOMContentLoaded", async () => {
  const form = document.getElementById("clipForm");
  const titleInput = document.getElementById("clipTitle");
  const urlInput = document.getElementById("clipUrl");
  const summaryInput = document.getElementById("clipSummary");
  const domainSelect = document.getElementById("clipDomain");
  const taxonomySelect = document.getElementById("clipTaxonomy");
  const endpointToggle = document.getElementById("endpointToggle");
  const endpointLabel = document.getElementById("endpointLabel");
  const statusBox = document.getElementById("statusMessage");
  const saveBtn = document.getElementById("saveBtn");
  const btnText = saveBtn.querySelector(".btn-text");
  const btnLoader = saveBtn.querySelector(".btn-loader");

  // 1. Setup Endpoint Toggle
  endpointToggle.addEventListener("click", () => {
    if (currentEndpoint === CLOUD_URL) {
      currentEndpoint = LOCAL_URL;
      endpointLabel.textContent = "Locale (8000)";
    } else {
      currentEndpoint = CLOUD_URL;
      endpointLabel.textContent = "Cloud";
    }
  });

  // 2. Setup Hemisphere Radio Sync
  const hemiButtons = document.querySelectorAll(".hemi-btn");
  hemiButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      hemiButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const hemi = btn.querySelector("input").value;
      updateTaxonomyAndDomain(hemi);
    });
  });

  function updateTaxonomyAndDomain(hemi) {
    if (hemi === "RIGHT") {
      domainSelect.value = "domain-filosofia-valori";
      taxonomySelect.value = "CREATIVE_IDEA";
    } else {
      domainSelect.value = "domain-software-engineering";
      taxonomySelect.value = "ARCHITECTURE";
    }
  }

  // 3. Extract Active Tab Metadata & Selection
  try {
    if (typeof chrome !== "undefined" && chrome.tabs && chrome.tabs.query) {
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      if (tab) {
        titleInput.value = tab.title || "";
        urlInput.value = tab.url || "";

        // Tenta di estrarre il testo selezionato dall'utente
        if (chrome.scripting && chrome.scripting.executeScript) {
          try {
            const results = await chrome.scripting.executeScript({
              target: { tabId: tab.id },
              func: () => window.getSelection().toString()
            });
            if (results && results[0] && results[0].result) {
              summaryInput.value = results[0].result.trim();
            }
          } catch (e) {
            console.log("Selezione diretta non disponibile:", e);
          }
        }

        // Auto-Infer Hemisfero
        const combined = `${tab.title || ""} ${urlInput.value || ""} ${summaryInput.value || ""}`.toLowerCase();
        const rightKeywords = ["design", "ui", "ux", "filosofia", "valore", "psicologia", "arte", "musica", "cultura", "ispirazione"];
        const isRight = rightKeywords.some(k => combined.includes(k));

        if (isRight) {
          document.querySelector("input[value='RIGHT']").checked = true;
          document.querySelector(".right-btn").classList.add("active");
          document.querySelector(".left-btn").classList.remove("active");
          updateTaxonomyAndDomain("RIGHT");
        }
      }
    }
  } catch (err) {
    console.warn("Estrazione tab fallita:", err);
  }

  // 4. Form Submission & Ingest
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    btnText.style.display = "none";
    btnLoader.style.display = "inline";
    saveBtn.disabled = true;
    statusBox.style.display = "none";

    const title = titleInput.value.trim();
    const url = urlInput.value.trim();
    const summary = summaryInput.value.trim() || `Risorsa web: ${title} (${url})`;
    const hemisphere = document.querySelector("input[name='hemisphere']:checked").value;
    const domain = domainSelect.value;
    const taxonomy = taxonomySelect.value;

    const slug = "web-" + title.toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .substring(0, 45) + "-" + (Date.now() % 10000);

    const now = new Date().toISOString();

    const payload = {
      nodes: [
        {
          id: slug,
          label: title,
          hemisphere: hemisphere,
          primary_label: taxonomy,
          category: taxonomy,
          tags: ["web-clipper", hemisphere.toLowerCase(), domain.replace("domain-", "")],
          summary: summary,
          details: {
            source_url: url,
            clipped_at: now,
            clipped_by: "Pierfrancesco Amendola"
          },
          confidence: "EXTRACTED",
          parent_graph_id: domain,
          layer_level: 2
        }
      ],
      edges: [
        {
          source: slug,
          target: "person-pierfrancesco",
          relation: "EXPRESSED_BY",
          confidence: "EXTRACTED",
          reasoning: "Catturato da Pierfrancesco via Web Clipper"
        },
        {
          source: slug,
          target: domain,
          relation: "BELONGS_TO_DOMAIN",
          confidence: "EXTRACTED",
          reasoning: "Collegato al macro-dominio tematico"
        }
      ]
    };

    try {
      const response = await fetch(currentEndpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!response.ok) {
        throw new Error(`HTTP Error ${response.status}: ${response.statusText}`);
      }

      const resData = await response.json();
      statusBox.className = "status-box success";
      statusBox.innerHTML = `✅ <b>Salvato nel Cervello!</b><br>Nodo: <code>${slug}</code>`;
      statusBox.style.display = "block";

      setTimeout(() => {
        window.close();
      }, 1800);

    } catch (error) {
      statusBox.className = "status-box error";
      statusBox.innerHTML = `❌ <b>Errore di Salvataggio:</b> ${error.message}<br><small>Verifica se l'endpoint è raggiungibile.</small>`;
      statusBox.style.display = "block";
    } finally {
      btnText.style.display = "inline";
      btnLoader.style.display = "none";
      saveBtn.disabled = false;
    }
  });
});
