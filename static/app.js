/**
 * Universal AI Brain - Clean Knowledge Graph (vis-network engine matching graphify aesthetic)
 */

let network = null;
let nodesDS = null;
let edgesDS = null;
let rawNodes = [];
let rawEdges = [];
// Progressive Area & Cluster View Modes
let graphViewMode = 'areas'; // 'areas' (macro clusters) or 'full' (all nodes)
let expandedNodeIds = new Set(['person-pierfrancesco']);
let allExpanded = false;

// Palazzo Cognitivo Multi-Layer State
let currentPalazzoFloor = 'all'; // 'all', 'vertical', 0, 1, 2
let cachedPalazzo = null;

const CORE_MACRO_HUBS = new Set([
  'person-pierfrancesco',
  'domain-software-engineering',
  'domain-ai-cognitive-systems',
  'domain-medicina-salute',
  'domain-filosofia-valori',
  'domain-design-creativita',
  'proj-streaksup-app',
  'universal-ai-brain',
  'aule-studio-app',
  'proj-caretrack'
]);

// Terminal and Activity Logger State
const terminalLogs = [];
let terminalFilter = 'all';
let terminalSearchQuery = '';
let terminalIsOpen = false;
let isTerminalMinimized = false;
let isTerminalExpanded = false;
let seenNodeIds = new Set();
let isInitialLoad = true;

// Transparent Network Interceptor (logs all requests and posts)
const _nativeFetch = window.fetch;
window.fetch = async function(...args) {
  const url = typeof args[0] === 'string' ? args[0] : (args[0] && args[0].url ? args[0].url : 'unknown');
  const options = args[1] || {};
  const method = (options.method || 'GET').toUpperCase();
  const startTime = performance.now();
  const timestamp = new Date();
  
  let requestBody = null;
  if (options.body) {
    try {
      requestBody = typeof options.body === 'string' ? JSON.parse(options.body) : options.body;
    } catch(e) {
      requestBody = options.body;
    }
  }

  const logEntry = {
    id: 'log-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5),
    type: 'http',
    method: method,
    url: url,
    timestamp: timestamp,
    timeStr: timestamp.toLocaleTimeString() + '.' + String(timestamp.getMilliseconds()).padStart(3, '0'),
    payload: requestBody,
    status: 'pending',
    statusCode: null,
    durationMs: 0,
    responseSnippet: null
  };

  addTerminalLog(logEntry);

  try {
    const response = await _nativeFetch.apply(this, args);
    const duration = Math.round(performance.now() - startTime);
    
    logEntry.durationMs = duration;
    logEntry.statusCode = response.status;
    logEntry.status = response.ok ? 'success' : 'error';

    try {
      const clone = response.clone();
      const text = await clone.text();
      try {
        logEntry.responseSnippet = JSON.parse(text);
      } catch(e) {
        logEntry.responseSnippet = text.slice(0, 300);
      }
    } catch(e) {
      // response stream not readable
    }

    updateTerminalLog(logEntry);
    return response;
  } catch (error) {
    const duration = Math.round(performance.now() - startTime);
    logEntry.durationMs = duration;
    logEntry.status = 'error';
    logEntry.statusCode = 0;
    logEntry.error = error.message;
    updateTerminalLog(logEntry);
    throw error;
  }
};

const LEFT_COLOR = '#00D2FF';
const RIGHT_COLOR = '#FF007F';
const CALLOSUM_COLOR = '#A855F7';

const CATEGORY_COLORS = {
  // Left Hemisphere (Logic, Code, Cognitive Rules, AI Reasoning, User Intent)
  'ARCHITECTURE': '#00D2FF',
  'DATA_STRUCTURE': '#38bdf8',
  'ALGORITHM': '#0284c7',
  'DEPENDENCY': '#6366f1',
  'BUSINESS_LOGIC': '#4E79A7',
  'API_SPEC': '#06b6d4',
  'COGNITIVE_RULE': '#10b981',
  'MENTAL_MODEL': '#14b8a6',
  'AI_REASONING': '#818cf8',
  'METACOGNITION': '#a78bfa',
  'USER_INTENT': '#3b82f6',
  
  // Right Hemisphere (Design, Emotions, Relationships, Philosophy, Episodic Chat)
  'DESIGN_TOKEN': '#FF007F',
  'COLOR_PALETTE': '#f43f5e',
  'UI_COMPONENT': '#fb7185',
  'UX_FLOW': '#e11d48',
  'BRAND_VOICE': '#F28E2B',
  'CREATIVE_IDEA': '#d946ef',
  'EMOTIONAL_MEMORY': '#ec4899',
  'LIFE_LESSON': '#f59e0b',
  'RELATIONSHIP': '#f43f5e',
  'PERSONAL_VALUE': '#8b5cf6',
  'CONVERSATION_EPISODE': '#e879f9'
};

const TAXONOMY = {
  LEFT: ['ARCHITECTURE', 'DATA_STRUCTURE', 'ALGORITHM', 'DEPENDENCY', 'BUSINESS_LOGIC', 'API_SPEC', 'COGNITIVE_RULE', 'MENTAL_MODEL', 'AI_REASONING', 'METACOGNITION', 'USER_INTENT'],
  RIGHT: ['DESIGN_TOKEN', 'COLOR_PALETTE', 'UI_COMPONENT', 'UX_FLOW', 'BRAND_VOICE', 'CREATIVE_IDEA', 'EMOTIONAL_MEMORY', 'LIFE_LESSON', 'RELATIONSHIP', 'PERSONAL_VALUE', 'CONVERSATION_EPISODE']
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
      const clickedId = params.nodes[0];
      showInfo(clickedId);
      
      // If in Areas mode, clicking expands/toggles its neighbors
      if (graphViewMode === 'areas') {
        toggleNodeExpansion(clickedId);
      }
    } else {
      clearInfo();
    }
  });

  network.on('doubleClick', (params) => {
    if (params.nodes.length > 0) {
      const clickedId = params.nodes[0];
      const n = rawNodes.find(x => x.id === clickedId);
      if (n) {
        const lvl = n.layer_level !== undefined ? n.layer_level : 0;
        if (lvl === 0) {
          selectPalazzoFloor(1);
        } else if (lvl === 1) {
          selectPalazzoFloor(2);
        } else {
          selectPalazzoFloor('all');
        }
      }
    } else {
      selectPalazzoFloor('all');
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
 * Palazzo Cognitivo Multi-Layer & Floor Selectors
 */
async function loadPalazzoData() {
  try {
    const res = await fetch('/api/graph/palazzo');
    if (!res.ok) return;
    cachedPalazzo = await res.json();
    if (cachedPalazzo && cachedPalazzo.floors) {
      cachedPalazzo.floors.forEach(fl => {
        const countEl = document.getElementById(`fl-count-${fl.level}`);
        if (countEl) countEl.textContent = `${fl.node_count} nodi`;
      });
    }
  } catch (e) {
    console.error('Failed to load palazzo hierarchy:', e);
  }
}

function selectPalazzoFloor(floorOption) {
  currentPalazzoFloor = floorOption;
  
  // Update button active state
  ['all', 'vertical', 0, 1, 2].forEach(opt => {
    const btn = document.getElementById(`fl-btn-${opt}`);
    if (btn) {
      if (opt === floorOption) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    }
  });

  const statusText = document.getElementById('elevator-status-text');
  if (statusText) {
    if (floorOption === 'all') statusText.textContent = 'Piano: Tutti';
    else if (floorOption === 'vertical') statusText.textContent = 'Vista: 3D Verticale';
    else if (floorOption === 0) statusText.textContent = 'Piano: 0 (Attico Domini)';
    else if (floorOption === 1) statusText.textContent = 'Piano: 1 (Progetti & Aree)';
    else if (floorOption === 2) statusText.textContent = 'Piano: 2 (Moduli Atomici)';
  }

  // Adjust layout engine: Hierarchical Top-Down Tree for Vertical view, Force-directed for Flat
  if (network) {
    if (floorOption === 'vertical') {
      network.setOptions({
        layout: {
          hierarchical: {
            enabled: true,
            direction: 'UD', // Up-Down (Top to bottom tree)
            sortMethod: 'directed',
            levelSeparation: 220,
            nodeSpacing: 180,
            treeSpacing: 250,
            blockShifting: true,
            edgeMinimization: true,
            parentCentralization: true
          }
        },
        physics: {
          enabled: false
        }
      });
    } else {
      network.setOptions({
        layout: {
          hierarchical: {
            enabled: false
          }
        },
        physics: {
          enabled: true,
          solver: 'forceAtlas2Based',
          forceAtlas2Based: {
            gravitationalConstant: -50,
            centralGravity: 0.01,
            springLength: 80,
            springConstant: 0.08,
            damping: 0.4
          }
        }
      });
    }
  }

  renderGraphData();
}

/**
 * Progressive Areas View Mode Switchers
 */
function setGraphViewMode(mode) {
  graphViewMode = mode;
  
  const btnAreas = document.getElementById('mode-btn-areas');
  const btnFull = document.getElementById('mode-btn-full');
  const actionsPill = document.getElementById('areas-action-pill');

  if (btnAreas && btnFull) {
    if (mode === 'areas') {
      btnAreas.classList.add('active');
      btnFull.classList.remove('active');
      if (actionsPill) actionsPill.style.display = 'flex';
    } else {
      btnFull.classList.add('active');
      btnAreas.classList.remove('active');
      if (actionsPill) actionsPill.style.display = 'none';
    }
  }

  renderGraphData();
}

function toggleNodeExpansion(nodeId) {
  if (expandedNodeIds.has(nodeId)) {
    // If already expanded, collapse it (unless it is the only root)
    if (expandedNodeIds.size > 1) {
      expandedNodeIds.delete(nodeId);
    }
  } else {
    expandedNodeIds.add(nodeId);
  }
  
  renderGraphData();
  
  // Smoothly center or relax physics
  if (network) {
    network.setOptions({ physics: { enabled: true } });
    setTimeout(() => {
      if (network) network.setOptions({ physics: { enabled: false } });
    }, 1200);
  }
}

function resetToMacroAreas() {
  expandedNodeIds = new Set(['person-pierfrancesco']);
  allExpanded = false;
  const labelEl = document.getElementById('expand-all-label');
  const iconEl = document.getElementById('expand-all-icon');
  if (labelEl) labelEl.textContent = 'Espandi Tutto';
  if (iconEl) iconEl.textContent = '➕';
  
  renderGraphData();
}

function toggleExpandAll() {
  if (!allExpanded) {
    rawNodes.forEach(n => expandedNodeIds.add(n.id));
    allExpanded = true;
    const labelEl = document.getElementById('expand-all-label');
    const iconEl = document.getElementById('expand-all-icon');
    if (labelEl) labelEl.textContent = 'Ricompatta';
    if (iconEl) iconEl.textContent = '➖';
  } else {
    resetToMacroAreas();
  }
  renderGraphData();
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

    // Track nodes in terminal feed
    if (rawNodes.length > 0) {
      const sorted = [...rawNodes].sort((a, b) => {
        const timeA = new Date(a.created_at || 0).getTime();
        const timeB = new Date(b.created_at || 0).getTime();
        return timeB - timeA;
      });

      if (isInitialLoad) {
        sorted.forEach(n => {
          seenNodeIds.add(n.id);
          recordNodeActivity(n, 'INGESTED / PERSISTED');
        });
        isInitialLoad = false;
      } else {
        sorted.forEach(n => {
          if (!seenNodeIds.has(n.id)) {
            seenNodeIds.add(n.id);
            recordNodeActivity(n, 'NEWLY ADDED');
          }
        });
      }
    }

    await loadPalazzoData();
    renderGraphData();
    updateStatsHUD();
    buildLegend();
    populateLinkDropdown();
    updateTerminalStats();
  } catch (err) {
    console.error('Failed to load brain data:', err);
  }
}

/**
 * Transform & Render Vis-Network Datasets with Progressive Areas & Multi-Layer Palazzo Support
 */
function renderGraphData() {
  // Helper to determine floor level of a node
  // Helper to determine floor level of a node directly from database
  const getFloor = (n) => {
    if (!n) return 1;
    if (n.layer_level !== undefined && n.layer_level !== null) return Number(n.layer_level);
    return 1;
  };

  // Count degrees (connections per node) and adjacency
  const degrees = {};
  const adjacency = {};
  rawNodes.forEach(n => {
    degrees[n.id] = 0;
    adjacency[n.id] = new Set();
  });
  
  rawEdges.forEach(e => {
    const s = typeof e.source === 'object' ? e.source.id : e.source;
    const t = typeof e.target === 'object' ? e.target.id : e.target;
    if (degrees[s] !== undefined) degrees[s]++;
    if (degrees[t] !== undefined) degrees[t]++;
    if (adjacency[s]) adjacency[s].add(t);
    if (adjacency[t]) adjacency[t].add(s);
  });

  const nodeMap = {};
  rawNodes.forEach(n => nodeMap[n.id] = n);

  // Determine Visible Nodes based on View Mode and Palazzo Floor Selection
  let visibleNodeIds = new Set();

  if (currentPalazzoFloor === 0 || currentPalazzoFloor === 1 || currentPalazzoFloor === 2) {
    // Specific Floor Filter: only show nodes belonging to that floor
    rawNodes.forEach(n => {
      if (getFloor(n) === currentPalazzoFloor) {
        visibleNodeIds.add(n.id);
      }
    });
  } else if (graphViewMode === 'full' || currentPalazzoFloor === 'vertical') {
    // Full view or Vertical 3D view: show all nodes
    rawNodes.forEach(n => visibleNodeIds.add(n.id));
  } else {
    // Areas Mode: show macro hubs and all nodes connected to expanded nodes
    CORE_MACRO_HUBS.forEach(hubId => {
      if (nodeMap[hubId]) visibleNodeIds.add(hubId);
    });
    
    if (nodeMap['person-pierfrancesco']) visibleNodeIds.add('person-pierfrancesco');

    expandedNodeIds.forEach(expId => {
      if (nodeMap[expId]) {
        visibleNodeIds.add(expId);
        if (adjacency[expId]) {
          adjacency[expId].forEach(nbrId => visibleNodeIds.add(nbrId));
        }
      }
    });
  }

  const visNodes = [];
  rawNodes.forEach(n => {
    if (!visibleNodeIds.has(n.id)) return;

    const isLeft = n.hemisphere === 'LEFT';
    const catColor = CATEGORY_COLORS[n.primary_label] || (isLeft ? LEFT_COLOR : RIGHT_COLOR);
    const degree = degrees[n.id] || 1;
    let size = Math.min(26, Math.max(13, 11 + degree * 1.4));
    
    // Count hidden neighbors
    const totalNeighbors = adjacency[n.id] ? adjacency[n.id].size : 0;
    let hiddenCount = 0;
    if (adjacency[n.id]) {
      adjacency[n.id].forEach(nbrId => {
        if (!visibleNodeIds.has(nbrId)) hiddenCount++;
      });
    }

    const isExpanded = expandedNodeIds.has(n.id);
    let label = n.label;
    const floorLvl = getFloor(n);

    if (currentPalazzoFloor === 'vertical') {
      label = `[P${floorLvl}] ${n.label}`;
    } else if (graphViewMode === 'areas' && currentPalazzoFloor === 'all') {
      if (hiddenCount > 0) {
        label = `${n.label} ⊕${hiddenCount}`;
      } else if (isExpanded && totalNeighbors > 1) {
        label = `${n.label} ⊖`;
      }
    }

    const isHub = CORE_MACRO_HUBS.has(n.id) || n.id === 'person-pierfrancesco' || floorLvl === 0;
    if (isHub) {
      size += 4;
    }

    const nodeObj = {
      id: n.id,
      label: label,
      title: `${n.label} [Piano ${floorLvl}: ${n.primary_label || n.category}]${hiddenCount > 0 ? ` (Clicca per espandere +${hiddenCount} nodi collegati)` : ''}`,
      size: size,
      color: {
        background: catColor,
        border: floorLvl === 0 ? '#38bdf8' : (isHub ? '#ffffff' : (isLeft ? '#00D2FF' : '#FF007F')),
        highlight: { background: '#ffffff', border: catColor }
      },
      borderWidth: isHub ? 3 : (hiddenCount > 0 ? 2.5 : 1.5),
      shadow: isHub ? { enabled: true, color: catColor, size: 8 } : false,
      _data: n,
      _degree: degree,
      _floor: floorLvl,
      _hiddenCount: hiddenCount,
      _isExpanded: isExpanded
    };

    if (currentPalazzoFloor === 'vertical') {
      nodeObj.level = floorLvl;
    }

    visNodes.push(nodeObj);
  });

  const visEdges = [];
  rawEdges.forEach((e, idx) => {
    const sId = typeof e.source === 'object' ? e.source.id : e.source;
    const tId = typeof e.target === 'object' ? e.target.id : e.target;
    
    if (!visibleNodeIds.has(sId) || !visibleNodeIds.has(tId)) return;

    const sNode = nodeMap[sId];
    const tNode = nodeMap[tId];
    const isCross = (sNode && tNode && sNode.hemisphere !== tNode.hemisphere);
    
    const sFloor = getFloor(sNode);
    const tFloor = getFloor(tNode);
    const isCrossFloor = (sFloor !== tFloor);

    let edgeColor = isCross ? CALLOSUM_COLOR : 'rgba(148, 163, 184, 0.45)';
    let edgeWidth = isCross ? 2.2 : 1.2;
    let isDashed = isCross;
    let edgeTitle = `${e.relation || 'CONNECTS_TO'}${isCross ? ' (Corpo Calloso)' : ''}`;

    if (currentPalazzoFloor === 'vertical' && isCrossFloor) {
      edgeColor = '#38bdf8';
      edgeWidth = 2.8;
      isDashed = [6, 4];
      edgeTitle = `⚡ Ascensore Sinaptico [Piano ${sFloor} ↔ Piano ${tFloor}] · ${e.relation || 'CONNECTS'}`;
    }

    visEdges.push({
      id: idx,
      from: sId,
      to: tId,
      title: edgeTitle,
      width: edgeWidth,
      dashes: isDashed,
      color: {
        color: edgeColor,
        highlight: '#ffffff',
        hover: isCross ? '#e9d5ff' : '#38bdf8'
      }
    });
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
    <button class="btn" style="width:100%; margin-top:8px; font-size:11px; padding:5px 10px; background:rgba(0,210,255,0.12); border-color:rgba(0,210,255,0.35); color:#38bdf8;" onclick="toggleNodeExpansion('${esc(nodeId)}')">
      <span>${expandedNodeIds.has(nodeId) ? '⊖ Ricompatta questo ramo' : '⊕ Espandi nodi collegati'}</span>
    </button>
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
  if (graphViewMode === 'areas' && !expandedNodeIds.has(nodeId)) {
    expandedNodeIds.add(nodeId);
    renderGraphData();
  }
  setTimeout(() => {
    if (network) {
      try {
        network.focus(nodeId, { scale: 1.3, animation: { duration: 600, easingFunction: 'easeInOutQuad' } });
        network.selectNodes([nodeId]);
      } catch (e) {}
    }
  }, 100);
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

/**
 * AI Directive & Sync Prompt Copy Management
 */
const AI_SYNC_PROMPT = `Leggi il mio Universal Knowledge Graph all'indirizzo: https://universal-ai-brain.onrender.com/brain.md
Segui rigorosamente la Direttiva Graphify in cima alla pagina.
Dopo aver analizzato la nostra conversazione, genera in calce il blocco JSON per aggiornare il mio grafo tramite POST /api/memory/ingest (oppure esegui direttamente il POST se possiedi tool di rete): mappa le richieste dell'utente (USER_INTENT), i tuoi ragionamenti e deduzioni logiche (AI_REASONING) e raggruppa il tema della chat nell'episodio conversazionale (CONVERSATION_EPISODE).

# DIRETTIVA DI SISTEMA COGNITIVA & PROTOCOLLO GRAPHIFY (MANDATORIO)
> **ATTENZIONE LLM (Claude, ChatGPT, Gemini, etc.):** Sei connesso al **Universal Knowledge Graph** di **Pierfrancesco Amendola**.
> Devi operare conformemente al protocollo **Graphify Specification (\`/graphify\`)** per navigazione, sintesi ed estrazione della conoscenza.

---

### REGOLE OPERATIVE FONDAMENTALI (GRAPHIFY SPECIFICATION):
1. **Navigazione a Grafo (Graph-First Reasoning):**
   - Quando l'utente ti pone una domanda o richiede un'analisi, tratta la richiesta come una query a grafo.
   - Esplora i percorsi tra i nodi dell'**Emisfero Sinistro (Logica, Tech, Regole)** e dell'**Emisfero Destro (Design, Emozioni, Relazioni, Valori)** attraverso le sinapsi del **Corpo Calloso**.
2. **Rubrica di Onestà Epistemologica (Confidence Rubric):**
   - \`EXTRACTED\`: Fatti testuali espliciti, codice verificato, dichiarazioni dirette dell'utente.
   - \`INFERRED\`: Deduzioni logiche e correlazioni ragionate tra nodi esistenti.
   - \`AMBIGUOUS\`: Elementi incerti, conflitti o ipotesi non confermate.
   - **Divieto Assoluto:** Non inventare mai relazioni, stack, emozioni o dettagli tecnici fittizi. Se inferisci qualcosa, segnalalo esplicitamente come \`INFERRED\`.
3. **Tassonomia Rigorosa a Due Emisferi:**
   - **EMISFERO SINISTRO (LEFT - Logica, Architettura, Richieste & Ragionamento):** \`ARCHITECTURE\`, \`DATA_STRUCTURE\`, \`ALGORITHM\`, \`DEPENDENCY\`, \`BUSINESS_LOGIC\`, \`API_SPEC\`, \`COGNITIVE_RULE\`, \`MENTAL_MODEL\`, \`AI_REASONING\`, \`METACOGNITION\`, \`USER_INTENT\`.
   - **EMISFERO DESTRO (RIGHT - Design, Emozioni, Episodi & Dialoghi):** \`DESIGN_TOKEN\`, \`COLOR_PALETTE\`, \`UI_COMPONENT\`, \`UX_FLOW\`, \`BRAND_VOICE\`, \`CREATIVE_IDEA\`, \`EMOTIONAL_MEMORY\`, \`LIFE_LESSON\`, \`RELATIONSHIP\`, \`PERSONAL_VALUE\`, \`CONVERSATION_EPISODE\`.
4. **Tracciamento Metacognitivo & Memoria Episodica delle Chat:**
   - **Richieste Utente (\`USER_INTENT\`):** Mappa le domande chiave, i requisiti, i desideri o gli intenti operativi espressi dall'utente.
   - **Ragionamenti dell'AI (\`AI_REASONING\` / \`METACOGNITION\`):** Mappa le deduzioni logiche, le analisi architetturali, i perché e le proposte avanzate dall'AI.
   - **Episodi & Chat Tematiche (\`CONVERSATION_EPISODE\`):** Conserva le conversazioni per aree di argomento (es. sport/calcio, tennis, nutrizione/cucina, architettura software, carriera) come cluster tematici autonomi, collegando le richieste utente e i ragionamenti AI all'episodio con \`BELONGS_TO_EPISODE\` o \`DISCUSSED_IN\`.
5. **Protocollo di Risposta & Ingestione della Memoria:**
   - Comunica secondo il protocollo **Caveman / Alta Densità Informativa**: chirurgico, diretto, privo di convenevoli, 100% sostanza tecnica e concettuale.
   - **Obbligo di Aggiornamento Grafo (Doppia Modalità):**
     1. **Se possiedi Tool di Rete o Esecuzione (Agenti con Bash, Python, Fetch o REST):** Esegui **DIRETTAMENTE** la chiamata \`POST https://universal-ai-brain.onrender.com/api/memory/ingest\` con il payload JSON contenente fatti utente, nodi di intenzione, ragionamento AI ed episodi di chat.
     2. **Se operi in sola chat testuale (senza esecuzione di rete):** **DEVI obbligatoriamente allegare in calce alla risposta** il blocco JSON formattato qui sotto, così che l'utente possa inviarlo con un click tramite la dashboard web.

\`\`\`json
{
  "nodes": [
    {
      "id": "slug-univoco",
      "label": "Nome del Concetto / Progetto / Emozione",
      "hemisphere": "LEFT" | "RIGHT",
      "primary_label": "VALORE_TASSONOMIA",
      "tags": ["tag1", "tag2"],
      "cross_links": ["id-nodo-emisfero-opposto"],
      "summary": "Sintesi cognitiva densa di 1-2 frasi.",
      "details": { "chiave": "valore_specifico" },
      "confidence": "EXTRACTED" | "INFERRED" | "AMBIGUOUS"
    }
  ],
  "edges": [
    {
      "source": "slug-sorgente",
      "target": "slug-destinazione",
      "relation": "RELAZIONE_IN_MAIUSCOLO",
      "confidence": "EXTRACTED" | "INFERRED" | "AMBIGUOUS",
      "reasoning": "Spiegazione se INFERRED o AMBIGUOUS"
    }
  ]
}
\`\`\`
`;

async function copyFullBrainMarkdown() {
  const btn = document.getElementById('btn-copy-full-md');
  const originalText = btn ? btn.innerHTML : '📄 Copia .md';
  try {
    if (btn) btn.innerHTML = `<span>⏳</span> Carico...`;
    const res = await fetch('/brain.md');
    if (!res.ok) throw new Error("Errore nel recupero di brain.md");
    const mdText = await res.text();

    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(mdText);
    } else {
      const textarea = document.createElement('textarea');
      textarea.value = mdText;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
    }

    if (btn) {
      btn.innerHTML = `<span>✅</span> .md Copiato!`;
      btn.classList.add('copied');
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.classList.remove('copied');
      }, 2500);
    }

    addTerminalLog({
      id: 'copy-md-' + Date.now(),
      type: 'node',
      method: 'GET',
      actionType: 'EXPORT_MARKDOWN',
      nodeId: 'brain-md-export',
      label: 'File brain.md Copiato Interamente negli Appunti',
      hemisphere: 'LEFT',
      primaryLabel: 'COGNITIVE_RULE',
      tags: ['markdown', 'export', 'clipboard', 'gemini-paste'],
      summary: `Copiati ${mdText.length} caratteri di brain.md negli appunti. Pronto da incollare in qualsiasi chat Gemini/ChatGPT.`,
      timestamp: new Date(),
      timeStr: new Date().toLocaleTimeString(),
      details: { size_bytes: mdText.length, lines: mdText.split('\n').length }
    });
  } catch (err) {
    if (btn) btn.innerHTML = originalText;
    alert("Errore nella copia del markdown: " + err.message);
  }
}

async function copyAIPrompt() {
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(AI_SYNC_PROMPT);
    } else {
      const textarea = document.createElement('textarea');
      textarea.value = AI_SYNC_PROMPT;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
    }

    // Visual Feedback
    const buttons = document.querySelectorAll('.btn-copy-prompt, .btn-hud-prompt');
    buttons.forEach(btn => {
      const originalHTML = btn.innerHTML;
      btn.innerHTML = `<span>✅</span> Copiato!`;
      btn.classList.add('copied');
      setTimeout(() => {
        btn.innerHTML = originalHTML;
        btn.classList.remove('copied');
      }, 2000);
    });

    // Record in Terminal Log
    addTerminalLog({
      id: 'prompt-' + Date.now(),
      type: 'node',
      method: 'PROMPT',
      actionType: 'COPIED TO CLIPBOARD',
      nodeId: 'ai-prompt-directive',
      label: 'Prompt per AI Copiato negli Appunti',
      hemisphere: 'LEFT',
      primaryLabel: 'COGNITIVE_RULE',
      tags: ['prompt', 'ai-sync', 'graphify', 'clipboard'],
      summary: 'Prompt copiato per ChatGPT / Claude / Gemini: istruzioni di lettura brain.md e aggiornamento grafo.',
      timestamp: new Date(),
      timeStr: new Date().toLocaleTimeString(),
      details: {
        target_endpoint: 'https://universal-ai-brain.onrender.com/brain.md',
        ingest_endpoint: 'POST /api/memory/ingest'
      }
    });
  } catch (err) {
    alert("Impossibile copiare il prompt negli appunti: " + err.message);
  }
}

/**
 * AI JSON Ingest Modal Management
 */
function openUploadModal() {
  const modal = document.getElementById('upload-json-modal');
  if (!modal) return;
  modal.style.display = 'flex';
  const statusEl = document.getElementById('json-upload-status');
  if (statusEl) statusEl.style.display = 'none';
  const pasteInput = document.getElementById('json-paste-input');
  if (pasteInput) {
    if (pasteInput.value.trim()) {
      validateAndPreviewJson(pasteInput.value);
    } else {
      updateJsonPreviewBadge(0, 0, false);
    }
  }
}

function closeUploadModal() {
  const modal = document.getElementById('upload-json-modal');
  if (!modal) return;
  modal.style.display = 'none';
  const fileNameEl = document.getElementById('json-file-name');
  if (fileNameEl) fileNameEl.textContent = '';
  const fileInput = document.getElementById('json-file-input');
  if (fileInput) fileInput.value = '';
}

function handleJsonFileSelect(event) {
  const file = event.target.files && event.target.files[0];
  if (!file) return;
  readJsonFile(file);
}

function readJsonFile(file) {
  const fileNameEl = document.getElementById('json-file-name');
  if (fileNameEl) fileNameEl.textContent = `File caricato: ${file.name} (${(file.size / 1024).toFixed(1)} KB)`;

  const reader = new FileReader();
  reader.onload = (e) => {
    const content = e.target.result;
    const pasteInput = document.getElementById('json-paste-input');
    if (pasteInput) {
      pasteInput.value = content;
      validateAndPreviewJson(content);
    }
  };
  reader.onerror = () => {
    alert("Errore nella lettura del file.");
  };
  reader.readAsText(file);
}

function setupDropzone() {
  const dropzone = document.getElementById('json-dropzone');
  if (!dropzone) return;

  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.add('dragover');
    }, false);
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.remove('dragover');
    }, false);
  });

  dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files && files.length > 0) {
      readJsonFile(files[0]);
    }
  }, false);
}

function cleanJsonString(raw) {
  let str = (raw || '').trim();
  // Strip Markdown code block indicators
  str = str.replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();
  return str;
}

function parseFlexibleJson(raw) {
  const cleaned = cleanJsonString(raw);
  if (!cleaned) return null;

  const parsed = JSON.parse(cleaned);

  let nodes = [];
  let edges = [];

  if (Array.isArray(parsed)) {
    // Array of nodes
    nodes = parsed;
  } else if (typeof parsed === 'object' && parsed !== null) {
    if (Array.isArray(parsed.nodes)) {
      nodes = parsed.nodes;
    } else if (parsed.id || parsed.label) {
      nodes = [parsed];
    }

    if (Array.isArray(parsed.edges)) {
      edges = parsed.edges;
    } else if (Array.isArray(parsed.links)) {
      edges = parsed.links;
    }
  }

  return { nodes, edges, raw: parsed };
}

function updateJsonPreviewBadge(nodesCount, edgesCount, isValid, errorMsg = '') {
  const badge = document.getElementById('json-preview-badge');
  if (!badge) return;

  if (!isValid && errorMsg) {
    badge.textContent = `⚠ ${errorMsg}`;
    badge.style.color = '#ef4444';
    badge.style.borderColor = '#ef4444';
  } else {
    badge.textContent = `✓ ${nodesCount} nodi · ${edgesCount} archi rilevati`;
    badge.style.color = nodesCount > 0 ? '#10b981' : '#38bdf8';
    badge.style.borderColor = nodesCount > 0 ? '#10b981' : '#3a3a5e';
  }
}

function validateAndPreviewJson(text) {
  if (!text || !text.trim()) {
    updateJsonPreviewBadge(0, 0, false);
    return null;
  }

  try {
    const payload = parseFlexibleJson(text);
    if (!payload || (payload.nodes.length === 0 && payload.edges.length === 0)) {
      updateJsonPreviewBadge(0, 0, false, "Nessun nodo/arco trovato nel JSON");
      return null;
    }
    updateJsonPreviewBadge(payload.nodes.length, payload.edges.length, true);
    return payload;
  } catch (err) {
    updateJsonPreviewBadge(0, 0, false, "Sintassi JSON non valida");
    return null;
  }
}

async function submitJsonUpload() {
  const pasteInput = document.getElementById('json-paste-input');
  const rawText = pasteInput ? pasteInput.value : '';
  const statusEl = document.getElementById('json-upload-status');
  const btn = document.getElementById('btn-submit-json');

  if (!rawText.trim()) {
    alert("Seleziona un file .json o incolla il payload JSON prima di inviare.");
    return;
  }

  let payload = null;
  try {
    payload = parseFlexibleJson(rawText);
  } catch (err) {
    if (statusEl) {
      statusEl.className = 'upload-status-box error';
      statusEl.style.display = 'block';
      statusEl.textContent = `Errore sintassi JSON: ${err.message}`;
    }
    return;
  }

  if (!payload || (payload.nodes.length === 0 && payload.edges.length === 0)) {
    if (statusEl) {
      statusEl.className = 'upload-status-box error';
      statusEl.style.display = 'block';
      statusEl.textContent = "Il JSON non contiene nodi o relazioni valide.";
    }
    return;
  }

  if (btn) {
    btn.disabled = true;
    btn.textContent = "⏳ Invio in corso...";
  }

  try {
    const res = await fetch('/api/memory/ingest', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        nodes: payload.nodes,
        edges: payload.edges
      })
    });

    const data = await res.json();

    if (res.ok) {
      if (statusEl) {
        statusEl.className = 'upload-status-box success';
        statusEl.style.display = 'block';
        statusEl.innerHTML = `<strong>✅ Memoria Ingestita con successo!</strong><br>${esc(data.message || `Aggiunti ${payload.nodes.length} nodi e ${payload.edges.length} archi.`)}`;
      }

      await fetchBrainData();

      // Focus first ingested node if available
      if (payload.nodes.length > 0) {
        const firstId = (payload.nodes[0].id || payload.nodes[0].label || '').toLowerCase().replace(/[^a-z0-9]+/g, '-');
        if (firstId) {
          setTimeout(() => focusNode(firstId), 300);
        }
      }

      setTimeout(() => {
        closeUploadModal();
        if (btn) {
          btn.disabled = false;
          btn.textContent = "🚀 Invia POST & Aggiorna Grafo";
        }
      }, 1200);

    } else {
      if (statusEl) {
        statusEl.className = 'upload-status-box error';
        statusEl.style.display = 'block';
        statusEl.textContent = `Errore server (${res.status}): ${data.detail || 'Impossibile salvare i nodi'}`;
      }
      if (btn) {
        btn.disabled = false;
        btn.textContent = "🚀 Invia POST & Aggiorna Grafo";
      }
    }
  } catch (err) {
    if (statusEl) {
      statusEl.className = 'upload-status-box error';
      statusEl.style.display = 'block';
      statusEl.textContent = `Errore connessione: ${err.message}`;
    }
    if (btn) {
      btn.disabled = false;
      btn.textContent = "🚀 Invia POST & Aggiorna Grafo";
    }
  }
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

/**
 * ==========================================================================
 * Light Terminal & Activity Logger Functions
 * ==========================================================================
 */

function recordNodeActivity(node, actionType = 'ADDED') {
  const ts = node.created_at ? new Date(node.created_at) : new Date();
  const logEntry = {
    id: 'node-' + node.id + '-' + (ts.getTime() || Date.now()),
    type: 'node',
    method: 'NODE',
    actionType: actionType,
    nodeId: node.id,
    label: node.label,
    hemisphere: node.hemisphere,
    primaryLabel: node.primary_label || node.category,
    tags: Array.isArray(node.tags) ? node.tags : [],
    summary: node.summary,
    timestamp: ts,
    timeStr: ts.toLocaleTimeString() + '.' + String(ts.getMilliseconds()).padStart(3, '0'),
    details: node.details || {}
  };
  addTerminalLog(logEntry);
}

function addTerminalLog(entry) {
  terminalLogs.unshift(entry);
  if (terminalLogs.length > 500) terminalLogs.pop();
  updateTerminalStats();
  renderTerminalLogs();
}

function updateTerminalLog(entry) {
  const idx = terminalLogs.findIndex(l => l.id === entry.id);
  if (idx !== -1) {
    terminalLogs[idx] = { ...entry };
  }
  updateTerminalStats();
  renderTerminalLogs();
}

function updateTerminalStats() {
  const allCount = terminalLogs.length;
  const httpCount = terminalLogs.filter(l => l.type === 'http').length;
  const nodesCount = terminalLogs.filter(l => l.type === 'node').length;

  const countAllEl = document.getElementById('count-all');
  const countHttpEl = document.getElementById('count-http');
  const countNodesEl = document.getElementById('count-nodes');
  const hudBadgeEl = document.getElementById('hud-terminal-badge');
  const totalReqsEl = document.getElementById('term-total-reqs');
  const totalNodesEl = document.getElementById('term-total-nodes');

  if (countAllEl) countAllEl.textContent = allCount;
  if (countHttpEl) countHttpEl.textContent = httpCount;
  if (countNodesEl) countNodesEl.textContent = nodesCount;
  if (hudBadgeEl) hudBadgeEl.textContent = allCount;
  if (totalReqsEl) totalReqsEl.textContent = `${httpCount} chiamate API`;
  if (totalNodesEl) totalNodesEl.textContent = `${rawNodes.length} nodi attivi`;
}

function setTerminalFilter(filter) {
  terminalFilter = filter;
  document.querySelectorAll('.term-tab').forEach(tab => {
    if (tab.dataset.filter === filter) {
      tab.classList.add('active');
    } else {
      tab.classList.remove('active');
    }
  });
  renderTerminalLogs();
}

function filterTerminalLogs(query) {
  terminalSearchQuery = (query || '').toLowerCase().trim();
  renderTerminalLogs();
}

function renderTerminalLogs() {
  const container = document.getElementById('terminal-body');
  if (!container) return;

  let filtered = terminalLogs;

  if (terminalFilter === 'http') {
    filtered = filtered.filter(l => l.type === 'http');
  } else if (terminalFilter === 'nodes') {
    filtered = filtered.filter(l => l.type === 'node');
  }

  if (terminalSearchQuery) {
    filtered = filtered.filter(l => {
      if (l.type === 'http') {
        const urlMatch = (l.url || '').toLowerCase().includes(terminalSearchQuery);
        const methodMatch = (l.method || '').toLowerCase().includes(terminalSearchQuery);
        const statusMatch = String(l.statusCode || '').includes(terminalSearchQuery);
        return urlMatch || methodMatch || statusMatch;
      } else {
        const labelMatch = (l.label || '').toLowerCase().includes(terminalSearchQuery);
        const idMatch = (l.nodeId || '').toLowerCase().includes(terminalSearchQuery);
        const sumMatch = (l.summary || '').toLowerCase().includes(terminalSearchQuery);
        const tagMatch = l.tags && l.tags.some(t => t.toLowerCase().includes(terminalSearchQuery));
        return labelMatch || idMatch || sumMatch || tagMatch;
      }
    });
  }

  if (filtered.length === 0) {
    container.innerHTML = `<div class="term-empty-state">Nessun evento o richiesta registrata con i filtri correnti.</div>`;
    return;
  }

  const html = filtered.map(item => {
    if (item.type === 'http') {
      const methodClass = item.method.toLowerCase();
      const statusClass = (item.statusCode >= 200 && item.statusCode < 300) ? 's-200' : 's-err';
      const statusText = item.statusCode ? `${item.statusCode} ${item.status.toUpperCase()}` : 'PENDING';
      const durationText = item.durationMs ? `${item.durationMs}ms` : '...';

      let payloadHtml = '';
      if (item.payload) {
        payloadHtml = `
          <div class="term-payload-toggle" onclick="toggleLogPayload('${item.id}-req')">▶ Mostra Payload Inviato (JSON)</div>
          <div id="${item.id}-req" style="display:none;">
            <pre>${esc(JSON.stringify(item.payload, null, 2))}</pre>
          </div>
        `;
      }

      let resHtml = '';
      if (item.responseSnippet) {
        resHtml = `
          <div class="term-payload-toggle" onclick="toggleLogPayload('${item.id}-res')">▶ Risposta Server (Preview)</div>
          <div id="${item.id}-res" style="display:none;">
            <pre>${esc(typeof item.responseSnippet === 'object' ? JSON.stringify(item.responseSnippet, null, 2) : item.responseSnippet)}</pre>
          </div>
        `;
      }

      return `
        <div class="term-entry type-${methodClass}">
          <div class="term-entry-header">
            <div class="term-entry-left">
              <span class="term-time">${item.timeStr}</span>
              <span class="term-badge-method ${methodClass}">${item.method}</span>
              <span class="term-entry-url">${esc(item.url)}</span>
            </div>
            <div style="display:flex; align-items:center; gap:6px;">
              <span class="term-duration">${durationText}</span>
              <span class="term-badge-status ${statusClass}">${statusText}</span>
            </div>
          </div>
          <div class="term-entry-detail">
            ${payloadHtml}
            ${resHtml}
          </div>
        </div>
      `;
    } else {
      // Node Entry
      const isLeft = item.hemisphere === 'LEFT';
      const hemiClass = isLeft ? 'left' : 'right';
      const tagsStr = item.tags && item.tags.length ? item.tags.map(t => `#${t}`).join(' ') : '';

      return `
        <div class="term-entry type-node">
          <div class="term-entry-header">
            <div class="term-entry-left">
              <span class="term-time">${item.timeStr}</span>
              <span class="term-badge-method node">CONCETTO</span>
              <span class="term-node-title" onclick="focusNode('${esc(item.nodeId)}')" style="cursor:pointer;" title="Clicca per evidenziare nel grafo">
                ${esc(item.label)}
              </span>
              <span class="term-hemi-tag ${hemiClass}">${item.hemisphere}</span>
              <code style="font-size:10px; color:#8b5cf6;">[${esc(item.primaryLabel)}]</code>
            </div>
            <span class="term-badge-status s-200">${esc(item.actionType)}</span>
          </div>
          <div class="term-entry-detail">
            <div style="color:#1e293b; font-size:11px;">${esc(item.summary || 'Nessuna sintesi')}</div>
            ${tagsStr ? `<div style="color:#0284c7; font-size:10px; margin-top:2px;">${esc(tagsStr)}</div>` : ''}
            <div class="term-payload-toggle" onclick="toggleLogPayload('${item.id}-det')">▶ Dettagli e Metadati</div>
            <div id="${item.id}-det" style="display:none;">
              <pre>${esc(JSON.stringify({ id: item.nodeId, hemisphere: item.hemisphere, primary_label: item.primaryLabel, tags: item.tags, details: item.details }, null, 2))}</pre>
            </div>
          </div>
        </div>
      `;
    }
  }).join('');

  container.innerHTML = html;
}

function toggleLogPayload(elementId) {
  const el = document.getElementById(elementId);
  if (!el) return;
  el.style.display = el.style.display === 'none' ? 'block' : 'none';
}

function toggleTerminal() {
  const wrapper = document.getElementById('light-terminal-wrapper');
  if (!wrapper) return;
  terminalIsOpen = !terminalIsOpen;
  if (terminalIsOpen) {
    wrapper.classList.add('open');
    renderTerminalLogs();
    const searchInput = document.getElementById('term-search');
    if (searchInput) searchInput.focus();
  } else {
    wrapper.classList.remove('open');
  }
}

function minimizeTerminal() {
  const term = document.getElementById('light-terminal');
  if (!term) return;
  isTerminalMinimized = !isTerminalMinimized;
  if (isTerminalMinimized) {
    term.classList.add('minimized');
  } else {
    term.classList.remove('minimized');
  }
}

function expandTerminal() {
  const term = document.getElementById('light-terminal');
  if (!term) return;
  isTerminalExpanded = !isTerminalExpanded;
  if (isTerminalExpanded) {
    term.classList.add('expanded');
  } else {
    term.classList.remove('expanded');
  }
}

function clearTerminalLogs() {
  terminalLogs.length = 0;
  updateTerminalStats();
  renderTerminalLogs();
}

function exportTerminalLogs() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(terminalLogs, null, 2));
  const downloadAnchor = document.createElement('a');
  downloadAnchor.setAttribute("href", dataStr);
  downloadAnchor.setAttribute("download", `brain-activity-logs-${new Date().toISOString().slice(0, 10)}.json`);
  document.body.appendChild(downloadAnchor);
  downloadAnchor.click();
  downloadAnchor.remove();
}

// ============================================================================
// Hierarchical Knowledge Tree Controller (層級譜系樹)
// ============================================================================
let currentTreeData = null;

async function openTreeModal() {
  const backdrop = document.getElementById('tree-modal-backdrop');
  if (!backdrop) return;
  backdrop.style.display = 'flex';
  
  const container = document.getElementById('tree-container');
  if (container) {
    container.innerHTML = '<div style="text-align:center; padding:40px; color:var(--text-muted);">Caricamento albero gerarchico in corso...</div>';
  }

  try {
    const res = await fetch('/api/graph/tree');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    currentTreeData = await res.json();
    renderTree(currentTreeData);
    
    const statsEl = document.getElementById('tree-footer-stats');
    if (statsEl) {
      statsEl.textContent = `Totale: ${currentTreeData.total_nodes} nodi · ${currentTreeData.total_edges} sinapsi organizzati in ${currentTreeData.children.length} emisferi`;
    }
  } catch (err) {
    if (container) {
      container.innerHTML = `<div style="color:#ef4444; padding:20px;">Errore nel caricamento dell'albero: ${err.message}</div>`;
    }
  }
}

function closeTreeModal() {
  const backdrop = document.getElementById('tree-modal-backdrop');
  if (backdrop) {
    backdrop.style.display = 'none';
  }
}

function renderTree(treeData, filterQuery = "") {
  const container = document.getElementById('tree-container');
  if (!container || !treeData) return;

  const q = filterQuery.toLowerCase().trim();
  let html = '';

  treeData.children.forEach(hemi => {
    let hemiMatches = false;
    let hemiChildrenHtml = '';

    hemi.children.forEach(tax => {
      let taxMatches = false;
      let nodesHtml = '';

      tax.children.forEach(node => {
        const matchTitle = node.name.toLowerCase().includes(q);
        const matchSlug = node.id.toLowerCase().includes(q);
        const matchSummary = (node.summary || '').toLowerCase().includes(q);
        const matchTags = (node.tags || []).some(t => t.toLowerCase().includes(q));

        if (!q || matchTitle || matchSlug || matchSummary || matchTags) {
          taxMatches = true;
          hemiMatches = true;
          const tagsHtml = (node.tags || []).map(t => `<span style="color:#38bdf8; margin-right:4px;">#${t}</span>`).join('');
          nodesHtml += `
            <div class="tree-node-item" onclick="focusAndCloseTree('${node.id}')">
              <div style="flex:1;">
                <div>
                  <span class="tree-node-title">${esc(node.name)}</span>
                  <span class="tree-node-slug">(${esc(node.id)})</span>
                </div>
                <div class="tree-node-desc">${esc(node.summary)}</div>
                ${tagsHtml ? `<div style="font-size:10px; margin-top:3px;">${tagsHtml}</div>` : ''}
              </div>
              <div style="display:flex; align-items:center;">
                <span class="tree-badge deg" title="Connessioni sinaptiche">${node.degree} sinapsi</span>
                <span class="tree-badge extracted">${node.confidence || 'EXTRACTED'}</span>
              </div>
            </div>
          `;
        }
      });

      if (!q || taxMatches) {
        hemiChildrenHtml += `
          <div class="tree-branch tax-branch">
            <div class="tree-tax-header" onclick="toggleTreeBranch(this)">
              <span>📂 <strong>[${esc(tax.name)}]</strong> (${tax.node_count} nodi)</span>
              <span class="branch-arrow">▼</span>
            </div>
            <div class="branch-content" style="padding-left:8px;">
              ${nodesHtml}
            </div>
          </div>
        `;
      }
    });

    if (!q || hemiMatches) {
      html += `
        <div class="tree-branch hemi-branch">
          <div class="tree-hemi-header" style="border-left:4px solid ${hemi.color || '#38bdf8'};" onclick="toggleTreeBranch(this)">
            <span>${hemi.icon || '🧠'} <strong>${esc(hemi.name)}</strong> (${hemi.node_count} nodi)</span>
            <span class="branch-arrow">▼</span>
          </div>
          <div class="branch-content">
            ${hemiChildrenHtml}
          </div>
        </div>
      `;
    }
  });

  if (!html) {
    html = `<div style="text-align:center; padding:30px; color:var(--text-muted);">Nessun nodo corrisponde alla ricerca "${esc(filterQuery)}".</div>`;
  }

  container.innerHTML = html;
}

function toggleTreeBranch(headerEl) {
  const content = headerEl.nextElementSibling;
  const arrow = headerEl.querySelector('.branch-arrow');
  if (!content) return;

  if (content.style.display === 'none') {
    content.style.display = 'block';
    if (arrow) arrow.textContent = '▼';
  } else {
    content.style.display = 'none';
    if (arrow) arrow.textContent = '▶';
  }
}

function expandAllTreeNodes() {
  document.querySelectorAll('.branch-content').forEach(el => el.style.display = 'block');
  document.querySelectorAll('.branch-arrow').forEach(el => el.textContent = '▼');
}

function collapseAllTreeNodes() {
  document.querySelectorAll('.branch-content').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.branch-arrow').forEach(el => el.textContent = '▶');
}

function filterTreeView(q) {
  if (currentTreeData) {
    renderTree(currentTreeData, q);
    if (q) expandAllTreeNodes();
  }
}

function focusAndCloseTree(nodeId) {
  closeTreeModal();
  focusNode(nodeId);
}

async function copyTreeMarkdown() {
  try {
    const res = await fetch('/brain.md?view=tree');
    const text = await res.text();
    await navigator.clipboard.writeText(text);
    alert("Copiato l'intero Albero di Conoscenza in Markdown negli appunti!");
  } catch (err) {
    alert("Errore copia: " + err.message);
  }
}

// Global Keyboard shortcuts & Backdrop click handlers
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const treeModal = document.getElementById('tree-modal-backdrop');
    if (treeModal && treeModal.style.display === 'flex') {
      closeTreeModal();
    }
    const wrapper = document.getElementById('light-terminal-wrapper');
    if (wrapper && wrapper.classList.contains('open')) {
      toggleTerminal();
    }
    const addModal = document.getElementById('add-modal');
    if (addModal && addModal.style.display === 'flex') {
      closeAddModal();
    }
    const uploadModal = document.getElementById('upload-json-modal');
    if (uploadModal && uploadModal.style.display === 'flex') {
      closeUploadModal();
    }
  } else if ((e.ctrlKey || e.metaKey) && e.key === '`') {
    e.preventDefault();
    toggleTerminal();
  }
});

function setupBackdropClicks() {
  const treeModal = document.getElementById('tree-modal-backdrop');
  if (treeModal) {
    treeModal.addEventListener('click', (e) => {
      if (e.target === treeModal) {
        closeTreeModal();
      }
    });
  }

  const terminalWrapper = document.getElementById('light-terminal-wrapper');
  if (terminalWrapper) {
    terminalWrapper.addEventListener('click', (e) => {
      if (e.target === terminalWrapper) {
        toggleTerminal();
      }
    });
  }

  const addModal = document.getElementById('add-modal');
  if (addModal) {
    addModal.addEventListener('click', (e) => {
      if (e.target === addModal) {
        closeAddModal();
      }
    });
  }

  const uploadModal = document.getElementById('upload-json-modal');
  if (uploadModal) {
    uploadModal.addEventListener('click', (e) => {
      if (e.target === uploadModal) {
        closeUploadModal();
      }
    });
  }
}

window.addEventListener('DOMContentLoaded', () => {
  initNetwork();
  fetchBrainData();
  setupSearch();
  setupDropzone();
  setupBackdropClicks();
});
