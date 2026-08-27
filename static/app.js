/**
 * Universal AI Brain - Clean Knowledge Graph (vis-network engine matching graphify aesthetic)
 */

let network = null;
let nodesDS = null;
let edgesDS = null;
let rawNodes = [];
let rawEdges = [];
let selectedNodeId = null;

const LEFT_COLOR = '#00D2FF';
const RIGHT_COLOR = '#FF007F';
const CALLOSUM_COLOR = '#A855F7';

const CATEGORY_COLORS = {
  // Left Hemisphere (Logic, Code, Cognitive Rules)
  'ARCHITECTURE': '#00D2FF',
  'DATA_STRUCTURE': '#38bdf8',
  'ALGORITHM': '#0284c7',
  'DEPENDENCY': '#6366f1',
  'BUSINESS_LOGIC': '#4E79A7',
  'API_SPEC': '#06b6d4',
  'COGNITIVE_RULE': '#10b981',
  'MENTAL_MODEL': '#14b8a6',
  
  // Right Hemisphere (Design, Emotions, Relationships, Philosophy)
  'DESIGN_TOKEN': '#FF007F',
  'COLOR_PALETTE': '#f43f5e',
  'UI_COMPONENT': '#fb7185',
  'UX_FLOW': '#e11d48',
  'BRAND_VOICE': '#F28E2B',
  'CREATIVE_IDEA': '#d946ef',
  'EMOTIONAL_MEMORY': '#ec4899',
  'LIFE_LESSON': '#f59e0b',
  'RELATIONSHIP': '#f43f5e',
  'PERSONAL_VALUE': '#8b5cf6'
};

const TAXONOMY = {
  LEFT: ['ARCHITECTURE', 'DATA_STRUCTURE', 'ALGORITHM', 'DEPENDENCY', 'BUSINESS_LOGIC', 'API_SPEC', 'COGNITIVE_RULE', 'MENTAL_MODEL'],
  RIGHT: ['DESIGN_TOKEN', 'COLOR_PALETTE', 'UI_COMPONENT', 'UX_FLOW', 'BRAND_VOICE', 'CREATIVE_IDEA', 'EMOTIONAL_MEMORY', 'LIFE_LESSON', 'RELATIONSHIP', 'PERSONAL_VALUE']
};

function esc(s) {
  return String(s || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
}

/**
 * Initialize vis-network Graph
 */
function initNetwork() {
  const container = document.getElementById('graph');
  if (!container) return;

  nodesDS = new vis.DataSet([]);
  edgesDS = new vis.DataSet([]);

  const data = { nodes: nodesDS, edges: edgesDS };

  const options = {
    physics: {
      enabled: true,
      solver: 'forceAtlas2Based',
      forceAtlas2Based: {
        gravitationalConstant: -70,
        centralGravity: 0.006,
        springLength: 130,
        springConstant: 0.08,
        damping: 0.45,
        avoidOverlap: 0.85
      },
      stabilization: { iterations: 200, fit: true }
    },
    interaction: {
      hover: true,
      tooltipDelay: 120,
      hideEdgesOnDrag: false,
      navigationButtons: false,
      keyboard: false
    },
    nodes: {
      shape: 'dot',
      borderWidth: 1.5,
      font: {
        size: 11,
        color: '#f8fafc',
        face: '-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
        strokeWidth: 3,
        strokeColor: '#0f0f1a'
      }
    },
    edges: {
      smooth: { type: 'continuous', roundness: 0.2 },
      arrows: { to: { enabled: true, scaleFactor: 0.5 } },
      selectionWidth: 2.5
    }
  };

  network = new vis.Network(container, data, options);

  network.once('stabilizationIterationsDone', () => {
    network.setOptions({ physics: { enabled: false } });
  });

  network.on('click', (params) => {
    if (params.nodes.length > 0) {
      showInfo(params.nodes[0]);
    } else {
      clearInfo();
    }
  });

  network.on('hoverNode', () => {
    container.style.cursor = 'pointer';
  });

  network.on('blurNode', () => {
    container.style.cursor = 'default';
  });
}

/**
 * Fetch Graph Data from FastAPI Backend
 */
async function fetchBrainData() {
  try {
    const res = await fetch('/brain.json');
    if (!res.ok) throw new Error(`HTTP error: ${res.status}`);
    const data = await res.json();
    
    rawNodes = data.nodes || [];
    rawEdges = data.links || [];

    renderGraphData();
    updateStatsHUD();
    buildLegend();
    populateLinkDropdown();
  } catch (err) {
    console.error('Failed to load brain data:', err);
  }
}

/**
 * Transform & Render Vis-Network Datasets
 */
function renderGraphData() {
  // Count degrees (connections per node)
  const degrees = {};
  rawNodes.forEach(n => degrees[n.id] = 0);
  rawEdges.forEach(e => {
    const s = typeof e.source === 'object' ? e.source.id : e.source;
    const t = typeof e.target === 'object' ? e.target.id : e.target;
    if (degrees[s] !== undefined) degrees[s]++;
    if (degrees[t] !== undefined) degrees[t]++;
  });

  const nodeMap = {};
  rawNodes.forEach(n => nodeMap[n.id] = n);

  const visNodes = rawNodes.map(n => {
    const isLeft = n.hemisphere === 'LEFT';
    const catColor = CATEGORY_COLORS[n.primary_label] || (isLeft ? LEFT_COLOR : RIGHT_COLOR);
    const degree = degrees[n.id] || 1;
    const size = Math.min(22, Math.max(12, 10 + degree * 1.5));

    return {
      id: n.id,
      label: n.label,
      title: `${n.label} [${n.primary_label || n.category}]`,
      size: size,
      color: {
        background: catColor,
        border: isLeft ? '#00D2FF' : '#FF007F',
        highlight: { background: '#ffffff', border: catColor }
      },
      _data: n,
      _degree: degree
    };
  });

  const visEdges = rawEdges.map((e, idx) => {
    const sId = typeof e.source === 'object' ? e.source.id : e.source;
    const tId = typeof e.target === 'object' ? e.target.id : e.target;
    const sNode = nodeMap[sId];
    const tNode = nodeMap[tId];
    const isCross = (sNode && tNode && sNode.hemisphere !== tNode.hemisphere);

    return {
      id: idx,
      from: sId,
      to: tId,
      title: `${e.relation || 'CONNECTS_TO'}${isCross ? ' (Corpo Calloso)' : ''}`,
      width: isCross ? 2.2 : 1.2,
      dashes: isCross,
      color: {
        color: isCross ? CALLOSUM_COLOR : 'rgba(148, 163, 184, 0.45)',
        highlight: '#ffffff',
        hover: isCross ? '#e9d5ff' : '#cbd5e1'
      }
    };
  });

  nodesDS.clear();
  edgesDS.clear();
  nodesDS.add(visNodes);
  edgesDS.add(visEdges);

  if (network) {
    network.setOptions({ physics: { enabled: true } });
  }
}

/**
 * Display Node Details in Sidebar
 */
function showInfo(nodeId) {
  selectedNodeId = nodeId;
  const node = rawNodes.find(n => n.id === nodeId);
  if (!node) return;

  const isLeft = node.hemisphere === 'LEFT';
  const hemiBadge = isLeft 
    ? `<span style="color:#00D2FF; font-weight:700;">SINISTRO (LOGICA)</span>`
    : `<span style="color:#FF007F; font-weight:700;">DESTRO (DESIGN)</span>`;

  // Neighbor nodes
  const connectedEdges = rawEdges.filter(e => {
    const s = typeof e.source === 'object' ? e.source.id : e.source;
    const t = typeof e.target === 'object' ? e.target.id : e.target;
    return s === nodeId || t === nodeId;
  });

  const neighborItems = connectedEdges.map(e => {
    const s = typeof e.source === 'object' ? e.source.id : e.source;
    const t = typeof e.target === 'object' ? e.target.id : e.target;
    const otherId = s === nodeId ? t : s;
    const otherNode = rawNodes.find(n => n.id === otherId);
    const isOutgoing = s === nodeId;
    const otherColor = otherNode ? (otherNode.hemisphere === 'LEFT' ? LEFT_COLOR : RIGHT_COLOR) : '#888';

    return `
      <div class="neighbor-link" style="border-left-color:${otherColor}" onclick="focusNode('${esc(otherId)}')">
        <span>${isOutgoing ? '➜' : '⬅'} <b>${esc(otherNode ? otherNode.label : otherId)}</b></span>
        <span class="neighbor-rel">${esc(e.relation || 'CONNECTS')}</span>
      </div>
    `;
  }).join('');

  // Render Tags
  const tags = Array.isArray(node.tags) ? node.tags : [];
  const tagsHtml = tags.map(t => `<span class="tag-badge">#${esc(t)}</span>`).join('');

  document.getElementById('info-content').innerHTML = `
    <div class="node-title">${esc(node.label)}</div>
    <div class="field"><b>Emisfero:</b> ${hemiBadge}</div>
    <div class="field"><b>Macro-Label:</b> <code style="color:#a855f7">${esc(node.primary_label || node.category)}</code></div>
    ${tags.length ? `<div class="tag-list">${tagsHtml}</div>` : ''}
    <div class="summary-box">${esc(node.summary || 'Nessuna descrizione')}</div>
    <div class="field" style="margin-top:10px; color:#aaa; font-size:11px;">
      <b>Sinapsi Connesse (${connectedEdges.length}):</b>
    </div>
    <div id="neighbors-list">${neighborItems || '<span class="empty">Nessun collegamento</span>'}</div>
  `;

  document.getElementById('btn-delete-node').style.display = 'inline-block';
}

function clearInfo() {
  selectedNodeId = null;
  document.getElementById('info-content').innerHTML = `<span class="empty">Clicca su un nodo nel grafo per ispezionarlo</span>`;
  document.getElementById('btn-delete-node').style.display = 'none';
}

function focusNode(nodeId) {
  if (!network) return;
  network.focus(nodeId, { scale: 1.3, animation: { duration: 600, easingFunction: 'easeInOutQuad' } });
  network.selectNodes([nodeId]);
  showInfo(nodeId);
}

/**
 * Live Search & Auto-Suggest
 */
function setupSearch() {
  const searchInput = document.getElementById('search');
  const searchResults = document.getElementById('search-results');

  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase().trim().replace(/^#/, '');
    searchResults.innerHTML = '';
    if (!q) {
      searchResults.style.display = 'none';
      return;
    }

    const matches = rawNodes.filter(n => {
      const inLabel = (n.label || '').toLowerCase().includes(q);
      const inPl = (n.primary_label || '').toLowerCase().includes(q);
      const inTags = Array.isArray(n.tags) && n.tags.some(t => t.toLowerCase().includes(q));
      return inLabel || inPl || inTags;
    }).slice(0, 15);

    if (matches.length === 0) {
      searchResults.innerHTML = `<div style="padding:6px; font-size:11px; color:#64748b;">Nessun nodo trovato</div>`;
    } else {
      matches.forEach(n => {
        const item = document.createElement('div');
        item.className = 'search-item';
        const color = n.hemisphere === 'LEFT' ? LEFT_COLOR : RIGHT_COLOR;
        item.innerHTML = `
          <span><span style="color:${color}; font-weight:700;">●</span> ${esc(n.label)}</span>
          <span style="font-size:10px; color:#94a3b8; font-family:monospace;">[${esc(n.primary_label)}]</span>
        `;
        item.onclick = () => {
          focusNode(n.id);
          searchResults.style.display = 'none';
          searchInput.value = '';
        };
        searchResults.appendChild(item);
      });
    }
    searchResults.style.display = 'block';
  });

  document.addEventListener('click', (e) => {
    if (!searchResults.contains(e.target) && e.target !== searchInput) {
      searchResults.style.display = 'none';
    }
  });
}

/**
 * Build Legend & Filter Checklist
 */
const hiddenCategories = new Set();

function buildLegend() {
  const legendEl = document.getElementById('legend');
  if (!legendEl) return;
  legendEl.innerHTML = '';

  const catCounts = {};
  rawNodes.forEach(n => {
    const cat = n.primary_label || 'GENERAL';
    catCounts[cat] = (catCounts[cat] || 0) + 1;
  });

  Object.keys(catCounts).sort().forEach(cat => {
    const item = document.createElement('div');
    item.className = 'legend-item';
    const color = CATEGORY_COLORS[cat] || '#888';

    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.className = 'legend-cb';
    cb.checked = !hiddenCategories.has(cat);

    cb.addEventListener('change', (e) => {
      e.stopPropagation();
      if (cb.checked) {
        hiddenCategories.delete(cat);
        item.classList.remove('dimmed');
      } else {
        hiddenCategories.add(cat);
        item.classList.add('dimmed');
      }
      applyCategoryFilters();
    });

    item.innerHTML = `
      <div class="legend-dot" style="background:${color}"></div>
      <span class="legend-label">${esc(cat)}</span>
      <span class="legend-count">${catCounts[cat]}</span>
    `;
    item.prepend(cb);

    item.onclick = (e) => {
      if (e.target === cb) return;
      cb.checked = !cb.checked;
      cb.dispatchEvent(new Event('change'));
    };

    legendEl.appendChild(item);
  });
}

function toggleAllCommunities(hide) {
  document.querySelectorAll('.legend-item').forEach(item => {
    hide ? item.classList.add('dimmed') : item.classList.remove('dimmed');
  });
  document.querySelectorAll('.legend-cb').forEach(cb => {
    cb.checked = !hide;
  });

  Object.keys(CATEGORY_COLORS).forEach(cat => {
    if (hide) hiddenCategories.add(cat); else hiddenCategories.delete(cat);
  });

  applyCategoryFilters();
}

function applyCategoryFilters() {
  const updates = rawNodes.map(n => ({
    id: n.id,
    hidden: hiddenCategories.has(n.primary_label)
  }));
  nodesDS.update(updates);
}

/**
 * Topbar HUD Statistics
 */
function updateStatsHUD() {
  const leftCount = rawNodes.filter(n => n.hemisphere === 'LEFT').length;
  const rightCount = rawNodes.filter(n => n.hemisphere === 'RIGHT').length;

  const nodeMap = {};
  rawNodes.forEach(n => nodeMap[n.id] = n);

  let callosumCount = 0;
  rawEdges.forEach(e => {
    const s = typeof e.source === 'object' ? e.source.id : e.source;
    const t = typeof e.target === 'object' ? e.target.id : e.target;
    if (nodeMap[s] && nodeMap[t] && nodeMap[s].hemisphere !== nodeMap[t].hemisphere) {
      callosumCount++;
    }
  });

  document.getElementById('hud-left').textContent = leftCount;
  document.getElementById('hud-right').textContent = rightCount;
  document.getElementById('hud-callosum').textContent = callosumCount;
  document.getElementById('stat-nodes-edges').textContent = `${rawNodes.length} nodi · ${rawEdges.length} archi`;
}

/**
 * Add Node Modal Management
 */
function updateTaxonomyOptions() {
  const hemi = document.querySelector('input[name="new-hemi"]:checked').value;
  const select = document.getElementById('new-primary-label');
  select.innerHTML = '';
  TAXONOMY[hemi].forEach(item => {
    const opt = document.createElement('option');
    opt.value = item;
    opt.textContent = item;
    select.appendChild(opt);
  });
}

function openAddModal() {
  updateTaxonomyOptions();
  populateLinkDropdown();
  document.getElementById('add-modal').style.display = 'flex';
}

function closeAddModal() {
  document.getElementById('add-modal').style.display = 'none';
  document.getElementById('new-label').value = '';
  document.getElementById('new-summary').value = '';
  document.getElementById('new-tags').value = '';
}

function populateLinkDropdown() {
  const select = document.getElementById('new-link-target');
  if (!select) return;
  select.innerHTML = '<option value="">-- Nessun collegamento immediato --</option>';
  rawNodes.forEach(n => {
    const opt = document.createElement('option');
    opt.value = n.id;
    opt.textContent = `[${n.hemisphere}] ${n.label} (${n.primary_label || n.category})`;
    select.appendChild(opt);
  });
}

async function submitNewNode() {
  const label = document.getElementById('new-label').value.trim();
  const primaryLabel = document.getElementById('new-primary-label').value;
  const tagsRaw = document.getElementById('new-tags').value;
  const summary = document.getElementById('new-summary').value.trim();
  const hemisphere = document.querySelector('input[name="new-hemi"]:checked').value;
  const targetId = document.getElementById('new-link-target').value;

  if (!label || !summary) {
    alert("Inserisci almeno il titolo e la sintesi del nodo.");
    return;
  }

  const id = label.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
  const tags = tagsRaw.split(',').map(t => t.trim().toLowerCase()).filter(t => t.length > 0);

  const payload = {
    nodes: [{
      id: id,
      label: label,
      hemisphere: hemisphere,
      primary_label: primaryLabel,
      category: primaryLabel,
      tags: tags,
      cross_links: targetId ? [targetId] : [],
      summary: summary,
      details: { created_via: "Web Dashboard", timestamp: new Date().toISOString() }
    }],
    edges: []
  };

  try {
    const res = await fetch('/api/memory/ingest', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      closeAddModal();
      await fetchBrainData();
      focusNode(id);
    } else {
      const err = await res.json();
      alert("Errore salvataggio: " + (err.detail || "Errore sconosciuto"));
    }
  } catch (err) {
    alert("Errore di connessione: " + err.message);
  }
}

async function deleteSelectedNode() {
  if (!selectedNodeId) return;
  const node = rawNodes.find(n => n.id === selectedNodeId);
  if (!confirm(`Sei sicuro di voler eliminare il nodo "${node ? node.label : selectedNodeId}"?`)) return;

  try {
    const res = await fetch(`/api/memory/node/${selectedNodeId}`, { method: 'DELETE' });
    if (res.ok) {
      clearInfo();
      await fetchBrainData();
    } else {
      alert("Errore durante l'eliminazione.");
    }
  } catch (err) {
    alert("Errore di connessione: " + err.message);
  }
}

window.addEventListener('DOMContentLoaded', () => {
  initNetwork();
  fetchBrainData();
  setupSearch();
});
