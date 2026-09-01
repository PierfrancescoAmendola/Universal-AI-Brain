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
  'domain-design-creativita'
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
 * Andrew's Monotone Chain Convex Hull Algorithm (da Graphify)
 * Calcola l'involucro convesso dei nodi di un cluster in coordinate di rete
 */
function convexHull(pts) {
  const p = pts.slice().sort((a, b) => (a.x - b.x) || (a.y - b.y));
  if (p.length < 3) return p;
  const cross = (o, a, b) => (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
  const build = seq => {
    const out = [];
    for (const q of seq) {
      while (out.length >= 2 && cross(out[out.length - 2], out[out.length - 1], q) <= 0) out.pop();
      out.push(q);
    }
    out.pop();
    return out;
  };
  const hull = build(p).concat(build(p.slice().reverse()));
  return hull.length >= 3 ? hull : p;
}

let hoveredNodeId = null;

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
        gravitationalConstant: -100,
        centralGravity: 0.003,
        springLength: 140,
        springConstant: 0.06,
        damping: 0.5,
        avoidOverlap: 1.0
      },
      stabilization: {
        enabled: true,
        iterations: 120,
        updateInterval: 25,
        fit: true
      }
    },
    interaction: {
      hover: true,
      tooltipDelay: 80,
      hideEdgesOnDrag: true,
      navigationButtons: false,
      keyboard: false
    },
    nodes: {
      shape: 'dot',
      borderWidth: 2,
      borderWidthSelected: 3.5,
      shadow: {
        enabled: true,
        color: 'rgba(0, 210, 255, 0.4)',
        size: 10,
        x: 0,
        y: 0
      },
      font: {
        size: 11,
        color: '#f8fafc',
        face: "'JetBrains Mono', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
        strokeWidth: 2.5,
        strokeColor: '#07080c',
        vadjust: 2
      }
    },
    edges: {
      smooth: { type: 'continuous', roundness: 0.2 },
      arrows: { to: { enabled: true, scaleFactor: 0.4 } },
      selectionWidth: 2.5,
      hoverWidth: 1.8,
      shadow: {
        enabled: true,
        color: 'rgba(0, 210, 255, 0.2)',
        size: 6,
        x: 0,
        y: 0
      }
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

  network.on('hoverNode', (params) => {
    hoveredNodeId = params.node;
    container.style.cursor = 'pointer';
  });

  network.on('blurNode', () => {
    hoveredNodeId = null;
    container.style.cursor = 'default';
  });
}

/**
 * Palazzo Cognitivo Multi-Layer & Floor Selectors
 */
async function loadPalazzoData() {
  try {
    const res = await fetch('/api/graph/palazzo');
    if (res.ok) {
      cachedPalazzo = await res.json();
      if (cachedPalazzo && cachedPalazzo.floors) {
        cachedPalazzo.floors.forEach(fl => {
          const countEl = document.getElementById(`fl-count-${fl.level}`);
          if (countEl) countEl.textContent = `${fl.node_count} nodi`;
        });
      }
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

  renderGraphData();

  setTimeout(() => {
    if (network) {
      try {
        network.fit({ animation: false });
      } catch (e) {}
    }
    if (window.innerWidth <= 900 && typeof switchMobileTab === 'function') {
      switchMobileTab('graph');
    }
  }, 50);
}

/**
 * Progressive Areas & 3D Celestial Globe View Mode Switchers
 */
function setGraphViewMode(mode) {
  graphViewMode = mode;
  
  const btnAreas = document.getElementById('mode-btn-areas');
  const btnFull = document.getElementById('mode-btn-full');
  const btnGlobe = document.getElementById('mode-btn-globe');
  const btnProjector = document.getElementById('mode-btn-projector');
  const actionsPill = document.getElementById('areas-action-pill');
  const palazzoElevator = document.getElementById('palazzo-elevator');
  const graphContainer = document.getElementById('graph');
  const globeContainer = document.getElementById('globe-3d-container');
  const projectorContainer = document.getElementById('projector-3d-container');

  [btnAreas, btnFull, btnGlobe, btnProjector].forEach(b => b && b.classList.remove('active'));

  if (mode === 'projector') {
    if (btnProjector) btnProjector.classList.add('active');
    if (actionsPill) actionsPill.style.display = 'none';
    if (palazzoElevator) palazzoElevator.style.display = 'none';
    if (graphContainer) graphContainer.style.display = 'none';
    if (globeContainer) {
      globeContainer.style.display = 'none';
      isGlobeLoopRunning = false;
    }
    if (projectorContainer) {
      projectorContainer.style.display = 'block';
    }

    if (window.EmbeddingProjector) {
      window.EmbeddingProjector.init(projectorContainer);
      window.EmbeddingProjector.setData(rawNodes, rawEdges);
      window.EmbeddingProjector.start();
    }
  } else if (mode === 'globe') {
    if (window.EmbeddingProjector) window.EmbeddingProjector.stop();
    if (projectorContainer) projectorContainer.style.display = 'none';
    if (btnGlobe) btnGlobe.classList.add('active');
    if (actionsPill) actionsPill.style.display = 'none';
    if (palazzoElevator) palazzoElevator.style.display = 'none';
    if (graphContainer) graphContainer.style.display = 'none';
    if (globeContainer) {
      globeContainer.style.display = 'block';
    }
    
    initOrUpdateGlobe3D();
    if (!isGlobeLoopRunning) {
      isGlobeLoopRunning = true;
      animateGlobe3D();
    }
  } else {
    if (window.EmbeddingProjector) window.EmbeddingProjector.stop();
    if (projectorContainer) projectorContainer.style.display = 'none';
    isGlobeLoopRunning = false;
    if (globeContainer) globeContainer.style.display = 'none';
    if (graphContainer) graphContainer.style.display = 'block';
    if (palazzoElevator) palazzoElevator.style.display = 'flex';
    
    if (mode === 'areas') {
      if (btnAreas) btnAreas.classList.add('active');
      if (actionsPill) actionsPill.style.display = 'flex';
    } else {
      if (btnFull) btnFull.classList.add('active');
      if (actionsPill) actionsPill.style.display = 'none';
    }
    renderGraphData();
  }
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

    renderGraphData();
    if (graphViewMode === 'projector' && window.EmbeddingProjector) {
      window.EmbeddingProjector.setData(rawNodes, rawEdges);
    }
    updateStatsHUD();
    buildLegend();
    populateLinkDropdown();
    updateTerminalStats();
    loadPalazzoData(); // In background senza bloccare il primo frame
  } catch (err) {
    console.error('Failed to load brain data:', err);
  }
}

/**
 * Transform & Render Vis-Network Datasets with Progressive Areas & Multi-Layer Palazzo Support
 */
function renderGraphData() {
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

  // Helper to determine floor level of a node directly and deterministically
  const getFloor = (n) => {
    if (!n) return 1;
    const rawLvl = (n.layer_level !== undefined && n.layer_level !== null) ? Number(n.layer_level) : null;
    if (rawLvl === 0 || rawLvl === 1 || rawLvl === 2) return rawLvl;
    
    const nid = (n.id || '').toLowerCase();
    const pl = (n.primary_label || '').toUpperCase();
    const cat = (n.category || '').toLowerCase();

    // Floor 0: Attico Macro-Domini & Core Hubs (SOLO IDENTITÀ E MACRO-DOMINI)
    if (nid === 'person-pierfrancesco' || nid.startsWith('domain-') || ['domain', 'root_domain', 'macro_domain'].includes(cat)) {
      return 0;
    }
    
    // Floor 2: Moduli, Algoritmi & Dettagli Atomici (NON progetti o applicazioni)
    if (cat !== 'application_project' && !nid.startsWith('proj-') && !nid.endsWith('-app') && nid !== 'universal-ai-brain' && nid !== 'aule-studio-app') {
      if (['ALGORITHM', 'DATA_STRUCTURE', 'DEPENDENCY', 'API_SPEC', 'UI_COMPONENT', 'DESIGN_TOKEN', 'COLOR_PALETTE', 'BUSINESS_LOGIC'].includes(pl) || cat.includes('schema') || cat.includes('token') || cat.includes('dettaglio') || cat.includes('modul')) {
        return 2;
      }
    }
    
    // Floor 1: Progetti, Applicazioni, Episodi, Intenti, Valori, Idee
    return 1;
  };

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
    let rawLabel = n.label || n.id;
    let label = rawLabel;
    const floorLvl = getFloor(n);
    const isHub = CORE_MACRO_HUBS.has(n.id) || n.id === 'person-pierfrancesco' || floorLvl === 0;

    if (currentPalazzoFloor === 'vertical') {
      label = `[P${floorLvl}] ${rawLabel.length > 20 ? rawLabel.substring(0, 18) + '…' : rawLabel}`;
    } else if (graphViewMode === 'areas' && currentPalazzoFloor === 'all') {
      const cleanName = rawLabel.length > 22 ? rawLabel.substring(0, 20) + '…' : rawLabel;
      if (hiddenCount > 0) {
        label = `${cleanName} ⊕${hiddenCount}`;
      } else if (isExpanded && totalNeighbors > 1) {
        label = `${cleanName} ⊖`;
      } else {
        label = cleanName;
      }
    } else if (graphViewMode === 'full') {
      label = rawLabel.length > 22 ? rawLabel.substring(0, 20) + '…' : rawLabel;
    }

    let nodeSize = isHub ? Math.min(30, Math.max(18, 16 + degree * 1.5)) : Math.min(22, Math.max(12, 10 + degree * 1.2));
    let nodeBorderColor = floorLvl === 0 ? '#ffe082' : (isLeft ? '#38bdf8' : '#f43f5e');
    let nodeBgColor = floorLvl === 0 ? '#ffd15c' : catColor;
    let nodeShadow = floorLvl === 0 
      ? { enabled: true, color: 'rgba(255, 209, 92, 0.75)', size: 16, x: 0, y: 0 }
      : { enabled: true, color: isLeft ? 'rgba(0, 210, 255, 0.45)' : 'rgba(255, 0, 127, 0.45)', size: 10, x: 0, y: 0 };

    const nodeObj = {
      id: n.id,
      label: label,
      title: `${n.label} [Piano ${floorLvl}: ${n.primary_label || n.category}]${hiddenCount > 0 ? ` (Clicca per espandere +${hiddenCount} nodi collegati)` : ''}`,
      size: nodeSize,
      color: {
        background: nodeBgColor,
        border: nodeBorderColor,
        highlight: { background: '#ffffff', border: isLeft ? '#00D2FF' : '#FF007F' }
      },
      borderWidth: isHub ? 3 : (hiddenCount > 0 ? 2.5 : 1.8),
      borderWidthSelected: 3.5,
      shadow: nodeShadow,
      _data: n,
      _degree: degree,
      _floor: floorLvl,
      _hiddenCount: hiddenCount,
      _isExpanded: isExpanded
    };

    if (currentPalazzoFloor === 'vertical') {
      const yTier = floorLvl === 0 ? -320 : (floorLvl === 1 ? 0 : 320);
      nodeObj.y = yTier + (Math.random() * 50 - 25);
      nodeObj.fixed = { y: true, x: false };
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
    const isLeftEdge = (sNode && sNode.hemisphere === 'LEFT') && (tNode && tNode.hemisphere === 'LEFT');

    let edgeColor = isCross ? CALLOSUM_COLOR : (isLeftEdge ? 'rgba(0, 210, 255, 0.25)' : 'rgba(255, 0, 127, 0.25)');
    let edgeWidth = isCross ? 2.2 : 1.2;
    let isDashed = isCross ? [5, 4] : false;
    let edgeTitle = `${e.relation || 'CONNECTS_TO'}${isCross ? ' (Corpo Calloso)' : ''}`;
    let edgeShadow = isCross ? { enabled: true, color: 'rgba(168, 85, 247, 0.6)', size: 8 } : false;

    if (currentPalazzoFloor === 'vertical' && isCrossFloor) {
      edgeColor = '#38bdf8';
      edgeWidth = 2.8;
      isDashed = [6, 4];
      edgeShadow = { enabled: true, color: 'rgba(56, 189, 248, 0.7)', size: 10 };
      edgeTitle = `⚡ Ascensore Sinaptico [Piano ${sFloor} ↔ Piano ${tFloor}] · ${e.relation || 'CONNECTS'}`;
    }

    visEdges.push({
      id: idx,
      from: sId,
      to: tId,
      title: edgeTitle,
      width: edgeWidth,
      dashes: isDashed,
      shadow: edgeShadow,
      color: {
        color: edgeColor,
        highlight: '#ffffff',
        hover: isCross ? '#e9d5ff' : '#00d2ff'
      }
    });
  });

  nodesDS.clear();
  edgesDS.clear();
  nodesDS.add(visNodes);
  edgesDS.add(visEdges);

  if (network) {
    if (currentPalazzoFloor === 'vertical') {
      network.setOptions({ physics: { enabled: false } });
    } else {
      network.setOptions({
        physics: {
          enabled: true,
          solver: 'forceAtlas2Based',
          forceAtlas2Based: {
            gravitationalConstant: -100,
            centralGravity: 0.003,
            springLength: 140,
            springConstant: 0.06,
            damping: 0.5,
            avoidOverlap: 1.0
          },
          stabilization: {
            enabled: true,
            iterations: 120,
            updateInterval: 25,
            fit: true
          }
        }
      });
      network.stabilize(120);
      network.once('stabilized', () => {
        network.setOptions({ physics: { enabled: false } });
      });
      setTimeout(() => {
        if (network) network.setOptions({ physics: { enabled: false } });
      }, 300);
    }
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

  // Epistemic confidence badge
  const conf = node.confidence || 'EXTRACTED';
  const confBadge = conf === 'EXTRACTED'
    ? `<span style="font-family:var(--font-mono); font-size:10px; font-weight:700; color:#10b981; background:rgba(16,185,129,0.12); border:1px solid rgba(16,185,129,0.3); padding:1px 6px; border-radius:4px;">● EXTRACTED</span>`
    : `<span style="font-family:var(--font-mono); font-size:10px; font-weight:700; color:#38bdf8; background:rgba(56,189,248,0.12); border:1px solid rgba(56,189,248,0.3); padding:1px 6px; border-radius:4px;">✦ INFERRED</span>`;

  const tags = Array.isArray(node.tags) ? node.tags : (node.tags ? [node.tags] : []);
  const tagsHtml = tags.map(t => `<span class="tag-badge">#${esc(t)}</span>`).join('');

  document.getElementById('info-content').innerHTML = `
    <div class="node-title">${esc(node.label)}</div>
    <div class="node-meta-row">
      ${hemiBadge}
      <span style="font-family:var(--font-mono); font-size:10px; color:#c084fc; background:rgba(168,85,247,0.12); border:1px solid rgba(168,85,247,0.3); padding:1px 6px; border-radius:4px;">${esc(node.primary_label || node.category)}</span>
      ${confBadge}
    </div>
    ${tags.length ? `<div style="display:flex; flex-wrap:wrap; gap:4px; margin-bottom:10px;">${tagsHtml}</div>` : ''}
    <div class="summary-card">${esc(node.summary || 'Nessuna descrizione')}</div>
    <button class="btn btn-primary" style="width:100%; margin-bottom:12px;" onclick="toggleNodeExpansion('${esc(nodeId)}')">
      <span>${expandedNodeIds.has(nodeId) ? '⊖ Ricompatta questo ramo' : '⊕ Espandi nodi collegati'}</span>
    </button>
    <div class="neighbors-box">
      <div class="neighbors-box-title">Sinapsi Connesse (${connectedEdges.length})</div>
      <div id="neighbors-list">${neighborItems || '<span class="empty">Nessun collegamento immediato</span>'}</div>
    </div>
  `;

  document.getElementById('btn-delete-node').style.display = 'inline-block';
}

function clearInfo() {
  selectedNodeId = null;
  document.getElementById('info-content').innerHTML = `
    <div class="empty-state-box">
      <span class="empty-icon">📍</span>
      <span class="empty-text">Clicca su un nodo nel grafo per ispezionarlo</span>
      <span class="empty-sub">oppure premi <kbd>⌘K</kbd> per cercare</span>
    </div>
  `;
  document.getElementById('btn-delete-node').style.display = 'none';
}

function focusNode(nodeId) {
  if (!network) return;
  if (graphViewMode === 'areas' && !expandedNodeIds.has(nodeId)) {
    expandedNodeIds.add(nodeId);
    renderGraphData();
  }
  if (network) {
    try {
      network.focus(nodeId, { scale: 1.3, animation: false });
      network.selectNodes([nodeId]);
    } catch (e) {}
  }
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
      searchResults.innerHTML = `<div style="padding:8px; font-size:11px; color:#64748b; font-family:var(--font-mono);">Nessun nodo trovato</div>`;
    } else {
      matches.forEach(n => {
        const item = document.createElement('div');
        item.className = 'search-item';
        const color = CATEGORY_COLORS[n.primary_label] || (n.hemisphere === 'LEFT' ? LEFT_COLOR : RIGHT_COLOR);
        item.style.borderLeft = `3px solid ${color}`;
        item.style.paddingLeft = '8px';
        item.style.display = 'flex';
        item.style.alignItems = 'center';
        item.style.justifyContent = 'space-between';
        item.innerHTML = `
          <span><b>${esc(n.label)}</b></span>
          <span style="font-size:10px; color:#94a3b8; font-family:var(--font-mono);">[${esc(n.primary_label || n.category)}]</span>
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
 * Build Legend & Filter Checklist (Stile Graphify con 3-State Select All)
 */
const hiddenCategories = new Set();

function updateSelectAllState() {
  const selectAllCb = document.getElementById('select-all-cb');
  if (!selectAllCb) return;
  const totalCategories = Object.keys(CATEGORY_COLORS).length;
  const hiddenCount = hiddenCategories.size;
  
  selectAllCb.checked = (hiddenCount === 0);
  selectAllCb.indeterminate = (hiddenCount > 0 && hiddenCount < totalCategories);
}

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
      updateSelectAllState();
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

  updateSelectAllState();
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
  updateSelectAllState();
}

function applyCategoryFilters() {
  const updates = rawNodes.map(n => ({
    id: n.id,
    hidden: hiddenCategories.has(n.primary_label)
  }));
  nodesDS.update(updates);
  if (network) network.redraw();
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
Dopo aver analizzato la nostra conversazione, genera in calce il blocco JSON per aggiornare il mio grafo tramite POST https://universal-ai-brain.onrender.com/api/memory/ingest (oppure esegui direttamente il POST se possiedi tool di rete/REST): mappa le richieste dell'utente (USER_INTENT), i tuoi ragionamenti e deduzioni logiche (AI_REASONING) e raggruppa il tema della chat nell'episodio conversazionale (CONVERSATION_EPISODE).

# DIRETTIVA DI SISTEMA COGNITIVA & PROTOCOLLO GRAPHIFY (MANDATORIO)
> **ATTENZIONE LLM (Claude, ChatGPT, Gemini, etc.):** Sei connesso al **Universal Knowledge Graph** di **Pierfrancesco Amendola**.
> Devi operare conformemente al protocollo **Graphify Specification (\`/graphify\`)** per navigazione, sintesi ed estrazione della conoscenza.

---

### REGOLE OPERATIVE FONDAMENTALI:
1. **Navigazione a Grafo (Graph-First Reasoning):**
   - Tratta la memoria come una rete viva. Collega i nodi tecnici dell'Emisfero Sinistro con i valori, il design e le preferenze di Pierfrancesco nell'Emisfero Destro attraverso il Corpo Calloso.
2. **Rubrica di Onestà Epistemologica (Confidence Rubric):**
   - \`EXTRACTED\`: Fatti testuali espliciti, codice verificato, dichiarazioni dirette dell'utente.
   - \`INFERRED\`: Deduzioni logiche e correlazioni ragionate tra nodi esistenti.
   - \`AMBIGUOUS\`: Elementi incerti o ipotesi non confermate.
   - **Divieto:** Non inventare mai dettagli fittizi. Se deduci qualcosa, segnalalo come \`INFERRED\`.
3. **Tassonomia Rigorosa a Due Emisferi:**
   - **EMISFERO SINISTRO (LEFT - Logica, Tech, Requisiti):** \`ARCHITECTURE\`, \`DATA_STRUCTURE\`, \`ALGORITHM\`, \`DEPENDENCY\`, \`BUSINESS_LOGIC\`, \`API_SPEC\`, \`COGNITIVE_RULE\`, \`MENTAL_MODEL\`, \`AI_REASONING\`, \`METACOGNITION\`, \`USER_INTENT\`.
   - **EMISFERO DESTRO (RIGHT - Design, Emozioni, Valori, Chat):** \`DESIGN_TOKEN\`, \`COLOR_PALETTE\`, \`UI_COMPONENT\`, \`UX_FLOW\`, \`BRAND_VOICE\`, \`CREATIVE_IDEA\`, \`EMOTIONAL_MEMORY\`, \`LIFE_LESSON\`, \`RELATIONSHIP\`, \`PERSONAL_VALUE\`, \`CONVERSATION_EPISODE\`.
4. **Palazzo Cognitivo a 3 Piani (\`layer_level\`):**
   - \`0\`: Attico Macro-Domini & Identità (\`person-pierfrancesco\`, \`domain-*\`).
   - \`1\`: Progetti Attivi, Applicazioni, Episodi Chat (\`CONVERSATION_EPISODE\`), Richieste (\`USER_INTENT\`), Ragionamenti (\`AI_REASONING\`), Valori (\`PERSONAL_VALUE\`).
   - \`2\`: Moduli Atomici, Algoritmi, Strutture Dati, Componenti UI, Token Colori.
5. **Lingua Obbligatoria:**
   - Tutti i testi (\`label\`, \`summary\`, \`tags\`, \`details\`) devono essere in **Italiano** (mantenendo i termini tecnici internazionali in inglese).
6. **Obbligo di Ingestione a Fine Sessione (Triade di Memoria):**
   - Genera sempre la triade \`USER_INTENT\` + \`AI_REASONING\` + \`CONVERSATION_EPISODE\` collegata a \`person-pierfrancesco\` e al progetto di riferimento.

\`\`\`json
{
  "nodes": [
    {
      "id": "user-intent-titolo-kebab",
      "label": "Titolo Intento Utente",
      "hemisphere": "LEFT",
      "primary_label": "USER_INTENT",
      "category": "USER_INTENT",
      "tags": ["tag1", "tag2"],
      "summary": "Sintesi chiara della richiesta dell'utente.",
      "details": {
        "user_prompt": "Testo fedele della richiesta utente",
        "context": "Vincoli o contesto specificato"
      },
      "confidence": "EXTRACTED",
      "parent_graph_id": "id-progetto-o-root",
      "layer_level": 1
    },
    {
      "id": "reasoning-titolo-kebab",
      "label": "Titolo Ragionamento AI",
      "hemisphere": "LEFT",
      "primary_label": "AI_REASONING",
      "category": "AI_REASONING",
      "tags": ["architettura", "analisi"],
      "summary": "Sintesi tecnica delle decisioni e deduzioni svolte.",
      "details": {
        "model": "Nome Modello (es. Claude 3.7 / ChatGPT-4o / Gemini 3.7)",
        "actions_taken": ["Azione 1", "Azione 2"],
        "outcome": "Risultato ottenuto"
      },
      "confidence": "INFERRED",
      "parent_graph_id": "id-progetto-o-root",
      "layer_level": 1
    },
    {
      "id": "episode-titolo-kebab",
      "label": "Titolo Episodio Conversazione",
      "hemisphere": "RIGHT",
      "primary_label": "CONVERSATION_EPISODE",
      "category": "CONVERSATION_EPISODE",
      "tags": ["chat", "sessione"],
      "summary": "Sintesi olistica dell'interazione avvenuta.",
      "details": {
        "participants": ["Pierfrancesco Amendola", "Nome Modello"],
        "topic": "Argomento trattato",
        "key_takeaways": "Punti chiave concordati"
      },
      "confidence": "EXTRACTED",
      "parent_graph_id": "root",
      "layer_level": 1
    }
  ],
  "edges": [
    {"source": "user-intent-titolo-kebab", "target": "person-pierfrancesco", "relation": "EXPRESSED_BY", "confidence": "EXTRACTED"},
    {"source": "user-intent-titolo-kebab", "target": "id-progetto-target", "relation": "TARGETS_PROJECT", "confidence": "EXTRACTED"},
    {"source": "reasoning-titolo-kebab", "target": "user-intent-titolo-kebab", "relation": "FULFILLS", "confidence": "INFERRED"},
    {"source": "episode-titolo-kebab", "target": "person-pierfrancesco", "relation": "INTERACTION_WITH", "confidence": "EXTRACTED"},
    {"source": "episode-titolo-kebab", "target": "user-intent-titolo-kebab", "relation": "RECORDS_INTENT", "confidence": "EXTRACTED"},
    {"source": "episode-titolo-kebab", "target": "reasoning-titolo-kebab", "relation": "RECORDS_REASONING", "confidence": "EXTRACTED"}
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
  const files = event.target.files;
  if (!files || files.length === 0) return;
  readJsonFiles(Array.from(files));
}

function readJsonFiles(files) {
  if (!files || files.length === 0) return;
  const fileNameEl = document.getElementById('json-file-name');
  if (fileNameEl) {
    if (files.length === 1) {
      fileNameEl.textContent = `File caricato: ${files[0].name} (${(files[0].size / 1024).toFixed(1)} KB)`;
    } else {
      fileNameEl.textContent = `${files.length} file selezionati`;
    }
  }

  const pasteInput = document.getElementById('json-paste-input');
  const readPromises = files.map(file => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = (e) => resolve(e.target.result);
      reader.onerror = () => reject(new Error(`Errore nella lettura del file ${file.name}`));
      reader.readAsText(file);
    });
  });

  Promise.all(readPromises).then(contents => {
    const combined = contents.join('\n\n');
    if (pasteInput) {
      pasteInput.value = combined;
      validateAndPreviewJson(combined);
    }
  }).catch(err => {
    alert(err.message);
  });
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
      readJsonFiles(Array.from(files));
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

  let nodes = [];
  let edges = [];

  // 1. Prova prima il parsing standard di un singolo JSON
  try {
    const parsed = JSON.parse(cleaned);
    if (Array.isArray(parsed)) {
      nodes = parsed;
    } else if (typeof parsed === 'object' && parsed !== null) {
      if (Array.isArray(parsed.nodes)) nodes = parsed.nodes;
      else if (parsed.id || parsed.label) nodes = [parsed];

      if (Array.isArray(parsed.edges)) edges = parsed.edges;
      else if (Array.isArray(parsed.links)) edges = parsed.links;
    }
    return { nodes, edges, raw: parsed };
  } catch (singleErr) {
    // 2. Se fallisce, estrai blocchi JSON multipli concatenati
    let depth = 0;
    let inString = false;
    let escape = false;
    let startIndex = -1;
    const blocks = [];

    for (let i = 0; i < cleaned.length; i++) {
      const char = cleaned[i];
      if (escape) {
        escape = false;
        continue;
      }
      if (char === '\\') {
        escape = true;
        continue;
      }
      if (char === '"') {
        inString = !inString;
        continue;
      }
      if (!inString) {
        if (char === '{') {
          if (depth === 0) startIndex = i;
          depth++;
        } else if (char === '}') {
          depth--;
          if (depth === 0 && startIndex !== -1) {
            blocks.push(cleaned.substring(startIndex, i + 1));
            startIndex = -1;
          }
        }
      }
    }

    let foundAny = false;
    if (blocks.length > 0) {
      blocks.forEach(blockStr => {
        try {
          const parsed = JSON.parse(blockStr);
          if (Array.isArray(parsed.nodes)) {
            nodes.push(...parsed.nodes);
            foundAny = true;
          } else if (parsed.id || parsed.label) {
            nodes.push(parsed);
            foundAny = true;
          }
          if (Array.isArray(parsed.edges)) edges.push(...parsed.edges);
          else if (Array.isArray(parsed.links)) edges.push(...parsed.links);
        } catch (e) {}
      });
    }

    if (foundAny) {
      return { nodes, edges, raw: { nodes, edges } };
    }

    throw singleErr;
  }
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
// Hierarchical Knowledge Tree Controller
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
  } else if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
    e.preventDefault();
    const searchInput = document.getElementById('search');
    if (searchInput) {
      searchInput.focus();
      searchInput.select();
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

// -----------------------------------------------------------------------------
// Cognitive Enhancements & Obsidian Vault Frontend Handlers
// -----------------------------------------------------------------------------

// 1. Daily Resurface
async function openResurfaceModal() {
  const modal = document.getElementById('resurface-modal-backdrop');
  if (!modal) return;
  modal.style.display = 'flex';
  const body = document.getElementById('resurface-modal-body');
  body.innerHTML = `<div style="text-align:center; padding:30px; color:var(--text-muted);">Caricamento briefing...</div>`;
  
  try {
    const res = await fetch('/api/cognitive/resurface');
    if (!res.ok) throw new Error("Errore nel recupero del Daily Resurface");
    const data = await res.json();
    
    let html = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; background:rgba(0,210,255,0.06); padding:10px 14px; border-radius:8px; border:1px solid rgba(0,210,255,0.2);">
        <div>
          <span style="font-weight:700; color:#00D2FF;">📅 Data: ${data.date}</span>
          <span style="color:var(--text-muted); font-size:12px; margin-left:10px;">Tempo stimato: ${data.duration_seconds}s</span>
        </div>
        <span style="font-size:12px; background:rgba(255,255,255,0.1); padding:3px 8px; border-radius:4px;">Spaced Repetition Active</span>
      </div>
      <h4 style="margin:10px 0 8px 0; color:#00D2FF; font-size:14px;">📜 3 Nodi Dormienti da Riattivare (Curva di Ebbinghaus)</h4>
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:10px; margin-bottom:15px;">
    `;
    
    data.resurface_nodes.forEach(n => {
      const isLeft = n.hemisphere === 'LEFT';
      const color = isLeft ? '#00D2FF' : '#FF007F';
      html += `
        <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-left:3px solid ${color}; border-radius:6px; padding:10px; cursor:pointer;" onclick="focusNode('${n.id}'); closeResurfaceModal();">
          <div style="font-size:11px; color:${color}; font-weight:600; text-transform:uppercase;">${n.primary_label} · ${n.days_dormant}g fa</div>
          <div style="font-weight:700; font-size:13px; margin:4px 0;">${n.label}</div>
          <div style="font-size:12px; color:var(--text-muted); line-height:1.4;">${(n.summary || '').substring(0, 100)}...</div>
        </div>
      `;
    });
    
    html += `</div>`;
    
    if (data.tension_of_the_day) {
      const t = data.tension_of_the_day;
      html += `
        <h4 style="margin:10px 0 8px 0; color:#FFB800; font-size:14px;">⚡ Tensione Aperta del Giorno</h4>
        <div style="background:rgba(255,184,0,0.06); border:1px solid rgba(255,184,0,0.25); border-radius:6px; padding:12px; margin-bottom:15px;">
          <div style="font-weight:700; font-size:13px; color:#FFD15C;">${t.node_a_label} ⚔️ ${t.node_b_label}</div>
          <div style="font-size:12px; color:var(--text-muted); margin-top:4px;">${t.description}</div>
        </div>
      `;
    }
    
    if (data.firmware_of_the_day) {
      const f = data.firmware_of_the_day;
      html += `
        <h4 style="margin:10px 0 8px 0; color:#A78BFA; font-size:14px;">🧭 Firmware / Modello Mentale del Giorno</h4>
        <div style="background:rgba(167,139,250,0.06); border:1px solid rgba(167,139,250,0.25); border-radius:6px; padding:12px;">
          <div style="font-weight:700; font-size:13px; color:#C4B5FD;">${f.name} <span style="font-weight:400; font-size:11px; color:var(--text-muted);">(${f.author})</span></div>
          <div style="font-size:12px; color:#EDE9FE; margin-top:4px; font-style:italic;">"${f.question}"</div>
        </div>
      `;
    }
    
    body.innerHTML = html;
  } catch (err) {
    body.innerHTML = `<div style="color:#FF4C4C; padding:20px;">Errore: ${err.message}</div>`;
  }
}

function closeResurfaceModal() {
  const modal = document.getElementById('resurface-modal-backdrop');
  if (modal) modal.style.display = 'none';
}

// 2. Tensions Matrix
async function openTensionsModal() {
  const modal = document.getElementById('tensions-modal-backdrop');
  if (!modal) return;
  modal.style.display = 'flex';
  renderTensionsList();
}

function closeTensionsModal() {
  const modal = document.getElementById('tensions-modal-backdrop');
  if (modal) modal.style.display = 'none';
}

async function renderTensionsList() {
  const body = document.getElementById('tensions-modal-body');
  body.innerHTML = `<div style="text-align:center; padding:30px; color:var(--text-muted);">Caricamento tensioni...</div>`;
  try {
    const res = await fetch('/api/cognitive/tensions');
    const tensions = await res.json();
    
    if (!tensions || tensions.length === 0) {
      body.innerHTML = `
        <div style="text-align:center; padding:40px; color:var(--text-muted);">
          <span style="font-size:32px;">🧘</span>
          <div style="margin-top:10px; font-weight:600;">Nessuna tensione aperta registrata nel connettoma.</div>
          <p style="font-size:12px;">Clicca su 'Rileva Nuove Tensioni' per scansionare idee polarizzanti.</p>
        </div>
      `;
      return;
    }
    
    let html = `<div style="display:flex; flex-direction:column; gap:12px;">`;
    tensions.forEach(t => {
      html += `
        <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:8px; padding:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <span style="font-size:11px; background:rgba(255,184,0,0.15); color:#FFB800; padding:2px 8px; border-radius:4px; font-weight:600;">${t.tension_type} · ${t.status}</span>
            <span style="font-size:11px; color:var(--text-muted);">${t.id}</span>
          </div>
          <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:10px; align-items:center; margin:10px 0;">
            <div style="background:rgba(0,210,255,0.05); border:1px solid rgba(0,210,255,0.2); padding:8px; border-radius:6px;">
              <strong style="color:#00D2FF; font-size:12px;">${t.node_a_label || t.node_a_id}</strong>
              <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">${(t.node_a_summary || '').substring(0, 70)}...</div>
            </div>
            <span style="font-size:18px;">⚡</span>
            <div style="background:rgba(255,0,127,0.05); border:1px solid rgba(255,0,127,0.2); padding:8px; border-radius:6px;">
              <strong style="color:#FF007F; font-size:12px;">${t.node_b_label || t.node_b_id}</strong>
              <div style="font-size:11px; color:var(--text-muted); margin-top:2px;">${(t.node_b_summary || '').substring(0, 70)}...</div>
            </div>
          </div>
          <div style="font-size:12px; color:var(--text-main); margin-bottom:10px;">${t.description}</div>
          <div style="display:flex; gap:8px; flex-wrap:wrap;">
            <button class="btn btn-sm" onclick="promptResolveTension('${t.id}', 'STEELMAN')">🛡️ Steelman</button>
            <button class="btn btn-sm" onclick="promptResolveTension('${t.id}', 'MERGE_AI')">🧬 Sintesi AI</button>
            <button class="btn btn-sm" onclick="promptResolveTension('${t.id}', 'FALSE_POSITIVE')">✕ Falso Positivo</button>
          </div>
        </div>
      `;
    });
    html += `</div>`;
    body.innerHTML = html;
  } catch (err) {
    body.innerHTML = `<div style="color:#FF4C4C; padding:20px;">Errore: ${err.message}</div>`;
  }
}

async function scanCandidateTensions() {
  const body = document.getElementById('tensions-modal-body');
  body.innerHTML = `<div style="text-align:center; padding:30px; color:var(--text-muted);">Scansione automatica in corso...</div>`;
  try {
    const res = await fetch('/api/cognitive/tensions/detect?limit=5');
    const candidates = await res.json();
    if (!candidates || candidates.length === 0) {
      alert("Nessuna nuova tensione rilevata.");
      renderTensionsList();
      return;
    }
    for (const c of candidates) {
      await fetch('/api/cognitive/tensions/create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          node_a_id: c.node_a_id,
          node_b_id: c.node_b_id,
          tension_type: c.tension_type,
          description: c.description
        })
      });
    }
    renderTensionsList();
  } catch (err) {
    alert("Errore scansione: " + err.message);
  }
}

async function promptResolveTension(tensionId, strategy) {
  const notes = prompt(`Inserisci note di risoluzione per la strategia ${strategy}:`, `Risoluzione applicata con strategia ${strategy}`);
  if (!notes) return;
  try {
    const res = await fetch('/api/cognitive/tensions/resolve', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        tension_id: tensionId,
        strategy: strategy,
        resolution_notes: notes
      })
    });
    if (res.ok) {
      alert("Tensione risolta e archiviata con successo!");
      renderTensionsList();
    }
  } catch (err) {
    alert("Errore risoluzione: " + err.message);
  }
}

// 3. Weave Link Engine
let currentWeaveProposals = [];
async function openWeaveModal() {
  const modal = document.getElementById('weave-modal-backdrop');
  if (!modal) return;
  modal.style.display = 'flex';
  const body = document.getElementById('weave-modal-body');
  body.innerHTML = `<div style="text-align:center; padding:30px; color:var(--text-muted);">Ricerca nodi orfani e generazione ponti...</div>`;
  
  try {
    const res = await fetch('/api/cognitive/weave/proposals?max_proposals=12');
    currentWeaveProposals = await res.json();
    
    if (!currentWeaveProposals || currentWeaveProposals.length === 0) {
      body.innerHTML = `
        <div style="text-align:center; padding:40px; color:var(--text-muted);">
          <span style="font-size:32px;">🕸️</span>
          <div style="margin-top:10px; font-weight:600;">Tutti i nodi sono densamente connessi!</div>
        </div>
      `;
      return;
    }
    
    let html = `<div style="display:flex; flex-direction:column; gap:10px;">`;
    currentWeaveProposals.forEach((p, idx) => {
      const isCross = p.is_cross_hemisphere;
      const tagBg = isCross ? 'rgba(255,0,127,0.15)' : 'rgba(0,210,255,0.15)';
      const tagCol = isCross ? '#FF007F' : '#00D2FF';
      html += `
        <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:12px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span style="font-size:11px; background:${tagBg}; color:${tagCol}; padding:2px 8px; border-radius:4px; font-weight:600;">${p.relation}</span>
            <span style="font-size:11px; color:var(--text-muted);">${p.confidence}</span>
          </div>
          <div style="margin:8px 0; font-size:13px; font-weight:600;">
            <span style="color:#00D2FF;">${p.source_label}</span> ➔ <span style="color:#FF007F;">${p.target_label}</span>
          </div>
          <div style="font-size:12px; color:var(--text-muted);">${p.reasoning}</div>
        </div>
      `;
    });
    html += `</div>`;
    body.innerHTML = html;
  } catch (err) {
    body.innerHTML = `<div style="color:#FF4C4C; padding:20px;">Errore: ${err.message}</div>`;
  }
}

function closeWeaveModal() {
  const modal = document.getElementById('weave-modal-backdrop');
  if (modal) modal.style.display = 'none';
}

async function applyAllWeaveProposals() {
  if (!currentWeaveProposals || currentWeaveProposals.length === 0) return;
  try {
    const res = await fetch('/api/cognitive/weave/apply', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ proposals: currentWeaveProposals })
    });
    const data = await res.json();
    alert(`Successo: ${data.message}`);
    closeWeaveModal();
    fetchBrainData();
  } catch (err) {
    alert("Errore applicazione link: " + err.message);
  }
}

// 4. Firmware Mental Models
async function openFirmwareModal() {
  const modal = document.getElementById('firmware-modal-backdrop');
  if (!modal) return;
  modal.style.display = 'flex';
  const body = document.getElementById('firmware-modal-body');
  body.innerHTML = `<div style="text-align:center; padding:30px; color:var(--text-muted);">Caricamento 9 firmware...</div>`;
  
  try {
    const res = await fetch('/api/cognitive/firmware/list');
    const models = await res.json();
    
    let html = `<div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px;">`;
    models.forEach(m => {
      html += `
        <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:8px; padding:14px; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="font-size:11px; color:#A78BFA; font-weight:600; text-transform:uppercase;">${m.author}</div>
            <div style="font-weight:700; font-size:14px; margin:4px 0; color:#EDE9FE;">${m.name}</div>
            <div style="font-size:12px; color:var(--text-muted); line-height:1.4; margin-bottom:12px;">${m.tagline}</div>
          </div>
          <button class="btn btn-sm btn-primary" onclick="promptApplyFirmware('${m.key}')">🧭 Applica a Problema</button>
        </div>
      `;
    });
    html += `</div>`;
    body.innerHTML = html;
  } catch (err) {
    body.innerHTML = `<div style="color:#FF4C4C; padding:20px;">Errore: ${err.message}</div>`;
  }
}

function closeFirmwareModal() {
  const modal = document.getElementById('firmware-modal-backdrop');
  if (modal) modal.style.display = 'none';
}

async function promptApplyFirmware(mode) {
  const problem = prompt("Inserisci il problema o decisione da esaminare con questo firmware:");
  if (!problem) return;
  try {
    const res = await fetch('/api/cognitive/firmware/apply', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ mode: mode, problem: problem })
    });
    const data = await res.json();
    if (data.directive) {
      await navigator.clipboard.writeText(data.directive);
      alert(`Direttiva di pensiero ${data.firmware_name} generata e COPIATA negli appunti! Incollala in qualsiasi chat AI.`);
    }
  } catch (err) {
    alert("Errore: " + err.message);
  }
}

// 5. Obsidian Vault Bridge
async function openObsidianModal() {
  const modal = document.getElementById('obsidian-modal-backdrop');
  if (!modal) return;
  modal.style.display = 'flex';
  renderObsidianStatus();
}

function closeObsidianModal() {
  const modal = document.getElementById('obsidian-modal-backdrop');
  if (modal) modal.style.display = 'none';
}

async function renderObsidianStatus() {
  const body = document.getElementById('obsidian-modal-body');
  body.innerHTML = `<div style="text-align:center; padding:30px; color:var(--text-muted);">Verifica vault...</div>`;
  try {
    const res = await fetch('/api/obsidian/status');
    const st = await res.json();
    body.innerHTML = `
      <div style="background:rgba(0,210,255,0.05); border:1px solid rgba(0,210,255,0.2); border-radius:8px; padding:15px; margin-bottom:12px;">
        <div style="font-size:13px; font-weight:700; color:#00D2FF; margin-bottom:6px;">💎 Percorso Vault:</div>
        <div style="font-family:'JetBrains Mono', monospace; font-size:11px; color:var(--text-muted); word-break:break-all;">${st.vault_dir}</div>
        <div style="margin-top:12px; font-size:14px;">
          Note Markdown sincronizzate: <strong style="color:#00D2FF;">${st.markdown_notes_count}</strong>
        </div>
      </div>
      <div style="font-size:12px; color:var(--text-muted); line-height:1.5;">
        Puoi aprire direttamente questa cartella come <strong>Vault in Obsidian</strong> su macOS/iOS per sfogliare il connettoma con grafi 3D e note atomiche.
      </div>
    `;
  } catch (err) {
    body.innerHTML = `<div style="color:#FF4C4C; padding:20px;">Errore: ${err.message}</div>`;
  }
}

async function triggerObsidianSync(action) {
  try {
    const res = await fetch('/api/obsidian/sync', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ action: action })
    });
    const data = await res.json();
    alert(`Sincronizzazione Obsidian completata: ${JSON.stringify(data)}`);
    renderObsidianStatus();
  } catch (err) {
    alert("Errore sync Obsidian: " + err.message);
  }
}

// -----------------------------------------------------------------------------
// 🌌 3D Celestial Constellation Globe Engine (Three.js WebGL)
// -----------------------------------------------------------------------------

let globeScene, globeCamera, globeRenderer, globeNodesGroup, globeEdgesGroup, globeGridGroup;
let isGlobeInitialized = false;
let isGlobeSpinning = true;
let globeRaycaster, globeMouse, globeIntersectedNode = null;
let selectedGlobeNodeId = null;
let currentRadarFilter = 'all';
let globeNodeMeshMap = new Map();
let globeTargetRotationX = 0, globeTargetRotationY = 0;
let globeRotationX = 0, globeRotationY = 0;
let globeIsDragging = false, globePreviousMousePosition = { x: 0, y: 0 };
let globeCameraDistance = 850;
let isGlobeLoopRunning = false;

function initOrUpdateGlobe3D() {
  const container = document.getElementById('globe-3d-container');
  if (!container) return;

  if (!isGlobeInitialized) {
    initGlobe3D(container);
  } else {
    rebuildGlobeGeometry();
  }
  setTimeout(resizeGlobe3D, 50);
  setTimeout(resizeGlobe3D, 250);
}

function initGlobe3D(container) {
  if (typeof THREE === 'undefined') {
    container.innerHTML = `<div style="color:#FF4C4C; padding:40px; text-align:center;">Errore: Libreria Three.js non disponibile.</div>`;
    return;
  }

  const rect = container.getBoundingClientRect();
  const width = rect.width || container.clientWidth || (window.innerWidth - 380);
  const height = rect.height || container.clientHeight || (window.innerHeight - 48);

  globeScene = new THREE.Scene();

  globeCamera = new THREE.PerspectiveCamera(45, width / height, 1, 5000);
  globeCamera.position.set(0, 0, globeCameraDistance);
  globeCamera.lookAt(0, 0, 0);

  // Luci
  const ambientLight = new THREE.AmbientLight(0xffffff, 1.4);
  globeScene.add(ambientLight);

  const centerLight = new THREE.PointLight(0x00D2FF, 2.0, 1000);
  centerLight.position.set(0, 0, 0);
  globeScene.add(centerLight);

  globeRenderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  globeRenderer.setSize(width, height);
  globeRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  
  // Rimuovi vecchi canvas se presenti
  const oldCanvas = container.querySelector('canvas');
  if (oldCanvas) oldCanvas.remove();

  container.appendChild(globeRenderer.domElement);

  // 1. Starfield Dust
  createGlobeStarfield();

  // 2. Griglia Olografica del Globo & Anelli
  globeGridGroup = new THREE.Group();
  globeScene.add(globeGridGroup);
  createGlobeGridAndCore();

  // 3. Gruppi Nodi e Archi
  globeNodesGroup = new THREE.Group();
  globeEdgesGroup = new THREE.Group();
  globeScene.add(globeNodesGroup);
  globeScene.add(globeEdgesGroup);

  // Raycaster per hover e click
  globeRaycaster = new THREE.Raycaster();
  globeRaycaster.params.Points = { threshold: 8 };
  globeMouse = new THREE.Vector2(-999, -999);

  setupGlobeInteractions(container);
  rebuildGlobeGeometry();

  isGlobeInitialized = true;
  if (!isGlobeLoopRunning) {
    isGlobeLoopRunning = true;
    animateGlobe3D();
  }
}

function createGlobeGridAndCore() {
  if (!globeGridGroup) return;

  while (globeGridGroup.children.length > 0) {
    globeGridGroup.remove(globeGridGroup.children[0]);
  }

  const radius = 330;

  // Sfera a griglia olografica sottile
  const sphereGeo = new THREE.SphereGeometry(radius, 24, 16);
  const sphereMat = new THREE.MeshBasicMaterial({
    color: 0x0c2038,
    wireframe: true,
    transparent: true,
    opacity: 0.18
  });
  const sphereMesh = new THREE.Mesh(sphereGeo, sphereMat);
  globeGridGroup.add(sphereMesh);

  // Anello equatoriale (Pianeta / Corpo Calloso)
  const ringGeo = new THREE.RingGeometry(radius - 2, radius + 2, 64);
  const ringMat = new THREE.MeshBasicMaterial({
    color: 0x00D2FF,
    side: THREE.DoubleSide,
    transparent: true,
    opacity: 0.28
  });
  const ringMesh = new THREE.Mesh(ringGeo, ringMat);
  ringMesh.rotation.x = Math.PI / 2;
  globeGridGroup.add(ringMesh);

  // Anello meridiano (Separazione Emisferi)
  const meridianMat = new THREE.MeshBasicMaterial({
    color: 0xFF007F,
    side: THREE.DoubleSide,
    transparent: true,
    opacity: 0.2
  });
  const meridianMesh = new THREE.Mesh(ringGeo, meridianMat);
  meridianMesh.rotation.y = Math.PI / 2;
  globeGridGroup.add(meridianMesh);

  // Pulsar Core centrale
  const coreGeo = new THREE.SphereGeometry(24, 16, 16);
  const coreMat = new THREE.MeshBasicMaterial({
    color: 0x38bdf8,
    transparent: true,
    opacity: 0.6
  });
  const coreMesh = new THREE.Mesh(coreGeo, coreMat);
  globeGridGroup.add(coreMesh);
}

function resizeGlobe3D() {
  const container = document.getElementById('globe-3d-container');
  if (!container || !globeRenderer || !globeCamera) return;
  const rect = container.getBoundingClientRect();
  const width = rect.width || container.clientWidth || (window.innerWidth - 380);
  const height = rect.height || container.clientHeight || (window.innerHeight - 48);
  if (width > 0 && height > 0) {
    globeCamera.aspect = width / height;
    globeCamera.updateProjectionMatrix();
    globeRenderer.setSize(width, height);
  }
}

function createGlobeStarfield() {
  const starGeo = new THREE.BufferGeometry();
  const starCount = 2000;
  const positions = new Float32Array(starCount * 3);
  const colors = new Float32Array(starCount * 3);

  for (let i = 0; i < starCount * 3; i += 3) {
    const radius = 1200 + Math.random() * 900;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(Math.random() * 2 - 1);

    positions[i] = radius * Math.sin(phi) * Math.cos(theta);
    positions[i + 1] = radius * Math.sin(phi) * Math.sin(theta);
    positions[i + 2] = radius * Math.cos(phi);

    colors[i] = 0.4 + Math.random() * 0.6;
    colors[i + 1] = 0.6 + Math.random() * 0.4;
    colors[i + 2] = 1.0;
  }

  starGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
  starGeo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

  const starMat = new THREE.PointsMaterial({
    size: 2.2,
    vertexColors: true,
    transparent: true,
    opacity: 0.6
  });

  const starField = new THREE.Points(starGeo, starMat);
  globeScene.add(starField);
}

function rebuildGlobeGeometry() {
  if (!globeNodesGroup || !rawNodes || !rawNodes.length) return;

  // Pulisci gruppi precedenti
  while (globeNodesGroup.children.length > 0) {
    const obj = globeNodesGroup.children[0];
    globeNodesGroup.remove(obj);
  }
  while (globeEdgesGroup.children.length > 0) {
    const obj = globeEdgesGroup.children[0];
    globeEdgesGroup.remove(obj);
  }
  globeNodeMeshMap.clear();

  const radius = 330;
  const nodeCount = rawNodes.length;

  // Calcola gradi
  const degreeMap = new Map();
  rawEdges.forEach(e => {
    const sId = typeof e.source === 'object' ? e.source.id : e.source;
    const tId = typeof e.target === 'object' ? e.target.id : e.target;
    degreeMap.set(sId, (degreeMap.get(sId) || 0) + 1);
    degreeMap.set(tId, (degreeMap.get(tId) || 0) + 1);
  });

  // Mappa coordinate sferiche bi-emisferiche
  rawNodes.forEach((node, idx) => {
    const isLeft = (node.hemisphere || 'LEFT') === 'LEFT';
    const isDomain = parseInt(node.layer_level) === 0;
    const deg = degreeMap.get(node.id) || 1;

    // Fibonacci sphere segmentata per emisfero
    const offset = 2 / Math.max(nodeCount, 1);
    const y = ((idx * offset) - 1) + (offset / 2);
    const r = Math.sqrt(Math.max(0, 1 - y * y));

    // Phi e Theta
    const phi = Math.acos(Math.max(-1, Math.min(1, y)));
    let theta = (idx * 2.399963229728653); // Golden angle

    // Separazione Bi-Emisferica
    if (isLeft) {
      theta = Math.PI * 0.15 + (theta % (Math.PI * 0.7)); // East hemisphere (Cyan)
    } else {
      theta = Math.PI * 1.15 + (theta % (Math.PI * 0.7)); // West hemisphere (Magenta)
    }

    if (isDomain) {
      // Posiziona i macro-domini sulla corona polare superiore
      theta = (idx * (Math.PI * 2 / 12));
    }

    const xPos = radius * Math.sin(phi) * Math.cos(theta);
    const yPos = radius * Math.cos(phi) * (isDomain ? 1.05 : 1.0);
    const zPos = radius * Math.sin(phi) * Math.sin(theta);

    // Colore
    let colorHex = isLeft ? 0x00D2FF : 0xFF007F;
    if (isDomain) colorHex = 0xFFD15C;

    const baseSize = isDomain ? 9.5 : Math.max(3.0, Math.min(7.5, 2.2 + Math.sqrt(deg) * 0.75));
    const sphereGeo = new THREE.SphereGeometry(baseSize, 14, 14);
    const sphereMat = new THREE.MeshBasicMaterial({
      color: colorHex,
      wireframe: false
    });

    const mesh = new THREE.Mesh(sphereGeo, sphereMat);
    mesh.position.set(xPos, yPos, zPos);
    mesh.userData = { node: node, baseColor: colorHex, baseSize: baseSize, degree: deg };

    globeNodesGroup.add(mesh);
    globeNodeMeshMap.set(node.id, mesh);
  });

  // Disegna Archi Normali (Costellazione)
  drawGlobeStandardEdges();

  // Se c'era un nodo selezionato, ripristina il suo spotlight
  if (selectedGlobeNodeId && globeNodeMeshMap.has(selectedGlobeNodeId)) {
    selectGlobeNode(selectedGlobeNodeId);
  } else {
    applyRadarFilter(currentRadarFilter);
  }
}

function drawGlobeStandardEdges() {
  while (globeEdgesGroup.children.length > 0) {
    globeEdgesGroup.remove(globeEdgesGroup.children[0]);
  }

  const intraLinePositions = [];
  const intraLineColors = [];
  const bridgeLinePositions = [];
  const bridgeLineColors = [];

  rawEdges.forEach(edge => {
    const sId = typeof edge.source === 'object' ? edge.source.id : edge.source;
    const tId = typeof edge.target === 'object' ? edge.target.id : edge.target;
    const srcMesh = globeNodeMeshMap.get(sId);
    const tgtMesh = globeNodeMeshMap.get(tId);

    if (srcMesh && tgtMesh) {
      const isCross = (srcMesh.userData.node.hemisphere || 'LEFT') !== (tgtMesh.userData.node.hemisphere || 'LEFT');
      const p1 = srcMesh.position;
      const p2 = tgtMesh.position;

      if (isCross) {
        bridgeLinePositions.push(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z);
        bridgeLineColors.push(1.0, 0.75, 0.1, 1.0, 0.75, 0.1); // Gold amber
      } else {
        intraLinePositions.push(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z);
        if (srcMesh.userData.node.hemisphere === 'LEFT') {
          intraLineColors.push(0.0, 0.7, 0.95, 0.0, 0.7, 0.95);
        } else {
          intraLineColors.push(0.95, 0.1, 0.55, 0.95, 0.1, 0.55);
        }
      }
    }
  });

  // Intra Lines
  if (intraLinePositions.length > 0) {
    const intraGeo = new THREE.BufferGeometry();
    intraGeo.setAttribute('position', new THREE.Float32BufferAttribute(intraLinePositions, 3));
    intraGeo.setAttribute('color', new THREE.Float32BufferAttribute(intraLineColors, 3));
    const intraMat = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.22,
      blending: THREE.AdditiveBlending
    });
    const intraLines = new THREE.LineSegments(intraGeo, intraMat);
    globeEdgesGroup.add(intraLines);
  }

  // Bridge Lines (Corpo Calloso)
  if (bridgeLinePositions.length > 0) {
    const bridgeGeo = new THREE.BufferGeometry();
    bridgeGeo.setAttribute('position', new THREE.Float32BufferAttribute(bridgeLinePositions, 3));
    bridgeGeo.setAttribute('color', new THREE.Float32BufferAttribute(bridgeLineColors, 3));
    const bridgeMat = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.85,
      linewidth: 2,
      blending: THREE.AdditiveBlending
    });
    const bridgeLines = new THREE.LineSegments(bridgeGeo, bridgeMat);
    globeEdgesGroup.add(bridgeLines);
  }
}

/**
 * 🎯 Spotlight & Synaptic Relational Inspector on Node Click
 */
function selectGlobeNode(nodeId) {
  selectedGlobeNodeId = nodeId;
  const centerMesh = globeNodeMeshMap.get(nodeId);
  if (!centerMesh) return;

  const node = centerMesh.userData.node;
  const isLeft = (node.hemisphere || 'LEFT') === 'LEFT';

  // 1. Trova tutte le relazioni dirette (entranti e uscenti)
  const outgoing = [];
  const incoming = [];
  const connectedNodeIds = new Set([nodeId]);

  rawEdges.forEach(e => {
    const sId = typeof e.source === 'object' ? e.source.id : e.source;
    const tId = typeof e.target === 'object' ? e.target.id : e.target;

    if (sId === nodeId) {
      connectedNodeIds.add(tId);
      const targetNode = rawNodes.find(n => n.id === tId);
      outgoing.push({
        targetId: tId,
        label: targetNode ? targetNode.label : tId,
        relation: e.relation || 'CONNECTS_TO',
        hemisphere: targetNode ? targetNode.hemisphere : 'LEFT',
        reasoning: e.reasoning
      });
    }
    if (tId === nodeId) {
      connectedNodeIds.add(sId);
      const sourceNode = rawNodes.find(n => n.id === sId);
      incoming.push({
        sourceId: sId,
        label: sourceNode ? sourceNode.label : sId,
        relation: e.relation || 'CONNECTS_TO',
        hemisphere: sourceNode ? sourceNode.hemisphere : 'LEFT',
        reasoning: e.reasoning
      });
    }
  });

  // 2. Aggiorna Nodi 3D: illumina e ingrandisci i connessi, oscura il resto
  globeNodeMeshMap.forEach((mesh, id) => {
    if (id === nodeId) {
      mesh.scale.set(2.4, 2.4, 2.4);
      mesh.material.color.setHex(0xFFFFFF); // Bianco brillante supernova
    } else if (connectedNodeIds.has(id)) {
      mesh.scale.set(1.6, 1.6, 1.6);
      mesh.material.color.setHex(mesh.userData.baseColor);
    } else {
      mesh.scale.set(0.45, 0.45, 0.45);
      mesh.material.color.setHex(0x0a1424); // Dark-matter dim
    }
  });

  // 3. Disegna SOLO i raggi laser delle sinapsi connesse
  while (globeEdgesGroup.children.length > 0) {
    globeEdgesGroup.remove(globeEdgesGroup.children[0]);
  }

  const laserPositions = [];
  const laserColors = [];

  connectedNodeIds.forEach(otherId => {
    if (otherId === nodeId) return;
    const otherMesh = globeNodeMeshMap.get(otherId);
    if (!otherMesh) return;

    const p1 = centerMesh.position;
    const p2 = otherMesh.position;
    const isCross = (node.hemisphere || 'LEFT') !== (otherMesh.userData.node.hemisphere || 'LEFT');

    laserPositions.push(p1.x, p1.y, p1.z, p2.x, p2.y, p2.z);

    if (isCross) {
      laserColors.push(1.0, 0.8, 0.1, 1.0, 0.8, 0.1); // Oro corpo calloso
    } else if (isLeft) {
      laserColors.push(0.0, 0.95, 1.0, 0.0, 0.95, 1.0); // Cyan laser
    } else {
      laserColors.push(1.0, 0.1, 0.6, 1.0, 0.1, 0.6); // Magenta laser
    }
  });

  if (laserPositions.length > 0) {
    const laserGeo = new THREE.BufferGeometry();
    laserGeo.setAttribute('position', new THREE.Float32BufferAttribute(laserPositions, 3));
    laserGeo.setAttribute('color', new THREE.Float32BufferAttribute(laserColors, 3));
    const laserMat = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.95,
      linewidth: 3,
      blending: THREE.AdditiveBlending
    });
    const laserLines = new THREE.LineSegments(laserGeo, laserMat);
    globeEdgesGroup.add(laserLines);
  }

  // 4. Popola e Mostra la Card Olografica Relazioni
  const card = document.getElementById('globe-rel-card');
  const titleEl = document.getElementById('globe-rel-title');
  const iconEl = document.getElementById('globe-rel-icon');
  const metaEl = document.getElementById('globe-rel-meta');
  const summaryEl = document.getElementById('globe-rel-summary');
  const countEl = document.getElementById('globe-rel-count');
  const listEl = document.getElementById('globe-rel-list');
  const pathWrap = document.getElementById('globe-rel-path-wrap');
  const pathLink = document.getElementById('globe-rel-path-link');
  const isolateBtn = document.getElementById('btn-globe-isolate');

  if (card && titleEl) {
    titleEl.textContent = node.label || node.id;
    iconEl.textContent = isLeft ? '⚡' : '🌸';
    metaEl.textContent = `${isLeft ? '⚡ EMISFERO SINISTRO' : '🌸 EMISFERO DESTRO'} · ${node.primary_label || 'CONCEPT'} · PIANO ${node.layer_level || 1}`;
    summaryEl.textContent = node.summary || 'Nessuna sintesi disponibile nel grafo.';
    countEl.textContent = outgoing.length + incoming.length;

    // Gestione link file Mac
    const details = typeof node.details === 'object' ? node.details : {};
    const localUri = details?.file_uri || (details?.local_path ? `file://${details.local_path}` : null);
    if (localUri && pathWrap && pathLink) {
      pathLink.href = localUri;
      pathLink.textContent = `📂 ${details.local_path || localUri}`;
      pathWrap.style.display = 'block';
    } else if (pathWrap) {
      pathWrap.style.display = 'none';
    }

    // Costruisci lista relazioni
    if (listEl) {
      listEl.innerHTML = '';

      if (outgoing.length === 0 && incoming.length === 0) {
        listEl.innerHTML = `<div style="color:#64748b; font-size:11px; padding:6px 0;">Nessuna sinapsi diretta collegata.</div>`;
      }

      outgoing.forEach(rel => {
        const isBridge = rel.hemisphere !== node.hemisphere;
        const item = document.createElement('div');
        item.className = 'globe-rel-item';
        item.onclick = () => selectGlobeNode(rel.targetId);
        item.innerHTML = `
          <div class="globe-rel-item-name" title="${rel.label}">${rel.hemisphere === 'LEFT' ? '⚡' : '🌸'} ${rel.label}</div>
          <span class="globe-rel-item-badge ${isBridge ? 'bridge' : ''}">${rel.relation}</span>
        `;
        listEl.appendChild(item);
      });

      incoming.forEach(rel => {
        const isBridge = rel.hemisphere !== node.hemisphere;
        const item = document.createElement('div');
        item.className = 'globe-rel-item';
        item.onclick = () => selectGlobeNode(rel.sourceId);
        item.innerHTML = `
          <div class="globe-rel-item-name" title="${rel.label}">📥 ${rel.label}</div>
          <span class="globe-rel-item-badge ${isBridge ? 'bridge' : ''}">← ${rel.relation}</span>
        `;
        listEl.appendChild(item);
      });
    }

    card.style.display = 'flex';
    if (isolateBtn) isolateBtn.style.display = 'inline-block';
  }

  // 5. Ruota dolcemente il mappamondo verso il nodo selezionato
  const p = centerMesh.position;
  const targetTheta = Math.atan2(p.x, p.z);
  const targetPhi = Math.atan2(p.y, Math.sqrt(p.x * p.x + p.z * p.z));

  globeTargetRotationY = -targetTheta;
  globeTargetRotationX = targetPhi;

  // Sincronizza anche la sidebar laterale
  showInfo(nodeId);
}

function clearGlobeSelection() {
  selectedGlobeNodeId = null;

  const card = document.getElementById('globe-rel-card');
  const isolateBtn = document.getElementById('btn-globe-isolate');
  if (card) card.style.display = 'none';
  if (isolateBtn) isolateBtn.style.display = 'none';

  // Ripristina dimensioni e colori di tutti i nodi
  globeNodeMeshMap.forEach(mesh => {
    mesh.scale.set(1, 1, 1);
    mesh.material.color.setHex(mesh.userData.baseColor);
  });

  // Ridisegna archi standard
  drawGlobeStandardEdges();
  applyRadarFilter(currentRadarFilter);
}

function openSidebarDossierFromGlobe() {
  if (selectedGlobeNodeId) {
    showInfo(selectedGlobeNodeId);
    if (window.innerWidth <= 900) {
      switchMobileTab('sidebar');
    }
  }
}

function setupGlobeInteractions(container) {
  const canvas = globeRenderer.domElement;

  canvas.addEventListener('mousedown', (e) => {
    globeIsDragging = true;
    globePreviousMousePosition = { x: e.clientX, y: e.clientY };
  });

  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    globeMouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    globeMouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

    if (globeIsDragging) {
      const deltaX = e.clientX - globePreviousMousePosition.x;
      const deltaY = e.clientY - globePreviousMousePosition.y;

      globeTargetRotationY += deltaX * 0.005;
      globeTargetRotationX += deltaY * 0.005;

      globePreviousMousePosition = { x: e.clientX, y: e.clientY };
    }
  });

  window.addEventListener('mouseup', () => {
    globeIsDragging = false;
  });

  canvas.addEventListener('wheel', (e) => {
    e.preventDefault();
    globeCameraDistance = Math.max(350, Math.min(1600, globeCameraDistance + e.deltaY * 0.8));
    globeCamera.position.z = globeCameraDistance;
  }, { passive: false });

  canvas.addEventListener('click', (e) => {
    if (globeIntersectedNode) {
      const node = globeIntersectedNode.userData.node;
      if (node) {
        selectGlobeNode(node.id);
      }
    } else if (!globeIsDragging) {
      // Cliccato nello spazio vuoto: resetta focus se aperto
      if (selectedGlobeNodeId && e.target === canvas) {
        clearGlobeSelection();
      }
    }
  });

  window.addEventListener('resize', resizeGlobe3D);
}

function animateGlobe3D() {
  if (graphViewMode !== 'globe' || !globeRenderer || !globeScene) {
    isGlobeLoopRunning = false;
    return;
  }

  isGlobeLoopRunning = true;
  requestAnimationFrame(animateGlobe3D);

  if (isGlobeSpinning && !globeIsDragging && !selectedGlobeNodeId) {
    globeTargetRotationY += 0.0018;
  }

  // Smooth rotation damping
  globeRotationX += (globeTargetRotationX - globeRotationX) * 0.08;
  globeRotationY += (globeTargetRotationY - globeRotationY) * 0.08;

  if (globeNodesGroup && globeEdgesGroup && globeGridGroup) {
    globeNodesGroup.rotation.x = globeRotationX;
    globeNodesGroup.rotation.y = globeRotationY;
    globeEdgesGroup.rotation.x = globeRotationX;
    globeEdgesGroup.rotation.y = globeRotationY;
    globeGridGroup.rotation.x = globeRotationX;
    globeGridGroup.rotation.y = globeRotationY;
  }

  // Raycasting hover check
  if (globeRaycaster && globeCamera && globeNodesGroup) {
    globeRaycaster.setFromCamera(globeMouse, globeCamera);
    const intersects = globeRaycaster.intersectObjects(globeNodesGroup.children);

    if (intersects.length > 0) {
      const hit = intersects[0].object;
      if (globeIntersectedNode !== hit) {
        if (globeIntersectedNode && globeIntersectedNode.userData.node.id !== selectedGlobeNodeId) {
          globeIntersectedNode.scale.set(1, 1, 1);
          globeIntersectedNode.material.color.setHex(globeIntersectedNode.userData.baseColor);
        }
        globeIntersectedNode = hit;
        if (hit.userData.node.id !== selectedGlobeNodeId) {
          globeIntersectedNode.scale.set(1.9, 1.9, 1.9);
          globeIntersectedNode.material.color.setHex(0xFFFFFF);
        }

        const node = globeIntersectedNode.userData.node;
        const statusEl = document.getElementById('terminal-status-text');
        if (statusEl && node) {
          statusEl.innerHTML = `🪐 <strong>${node.label}</strong> [${node.primary_label || 'NODE'}] · ${node.hemisphere === 'LEFT' ? '⚡ Sinistro' : '🌸 Destro'}`;
        }
      }
    } else {
      if (globeIntersectedNode) {
        if (globeIntersectedNode.userData.node.id !== selectedGlobeNodeId) {
          globeIntersectedNode.scale.set(1, 1, 1);
          globeIntersectedNode.material.color.setHex(globeIntersectedNode.userData.baseColor);
        }
        globeIntersectedNode = null;
      }
    }
  }

  globeRenderer.render(globeScene, globeCamera);
}

function toggleGlobeSpin() {
  isGlobeSpinning = !isGlobeSpinning;
  const btn = document.getElementById('btn-globe-spin');
  if (btn) {
    btn.classList.toggle('active', isGlobeSpinning);
    btn.textContent = isGlobeSpinning ? '🔄 Auto-Spin ON' : '⏸️ Auto-Spin OFF';
  }
}

function resetGlobeCamera() {
  globeTargetRotationX = 0;
  globeTargetRotationY = 0;
  globeCameraDistance = 850;
  if (globeCamera) globeCamera.position.set(0, 0, globeCameraDistance);
  clearGlobeSelection();
}

// -----------------------------------------------------------------------------
// 📡 Radar Tech & Theme Filter Engine
// -----------------------------------------------------------------------------

function applyRadarFilter(filterKey) {
  currentRadarFilter = filterKey;

  // Aggiorna pulsanti UI
  document.querySelectorAll('.radar-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.radar === filterKey);
  });

  const filterLower = filterKey.toLowerCase();

  // 1. Aggiorna 3D Constellation Globe
  if (globeNodeMeshMap.size > 0 && !selectedGlobeNodeId) {
    globeNodeMeshMap.forEach((mesh, nodeId) => {
      const node = mesh.userData.node;
      const tagsStr = (Array.isArray(node.tags) ? node.tags.join(' ') : (node.tags || '')).toLowerCase();
      const labelStr = (node.label || '').toLowerCase();
      const idStr = (node.id || '').toLowerCase();
      const combined = `${tagsStr} ${labelStr} ${idStr}`;

      let matches = false;
      if (filterLower === 'all') {
        matches = true;
      } else if (filterLower === 'swift') {
        matches = combined.includes('swift') || combined.includes('ios') || combined.includes('widgetkit');
      } else if (filterLower === 'python') {
        matches = combined.includes('python') || combined.includes('fastapi') || combined.includes('ai') || combined.includes('torch');
      } else if (filterLower === 'web') {
        matches = combined.includes('typescript') || combined.includes('react') || combined.includes('javascript') || combined.includes('web');
      } else if (filterLower === 'cpp') {
        matches = combined.includes('cpp') || combined.includes('c++') || combined.includes('algo') || combined.includes('lasd') || combined.includes('c-lang');
      } else if (filterLower === 'medical') {
        matches = combined.includes('medicina') || combined.includes('salute') || combined.includes('datamed') || combined.includes('caretrack') || combined.includes('alcool');
      } else if (filterLower === 'bridges') {
        matches = (mesh.userData.degree || 0) >= 4;
      }

      if (matches) {
        mesh.material.color.setHex(mesh.userData.baseColor);
        mesh.scale.set(1.4, 1.4, 1.4);
      } else {
        mesh.material.color.setHex(0x1a2638);
        mesh.scale.set(0.6, 0.6, 0.6);
      }
    });
  }

  // 2. Aggiorna 2D Vis Network (se in modalità 2D)
  if (network && typeof nodesDS !== 'undefined' && nodesDS && graphViewMode !== 'globe') {
    const allNodes = nodesDS.get();
    const updates = [];

    allNodes.forEach(node => {
      const tagsStr = (Array.isArray(node.tags) ? node.tags.join(' ') : (node.tags || '')).toLowerCase();
      const labelStr = (node.label || '').toLowerCase();
      const idStr = (node.id || '').toLowerCase();
      const combined = `${tagsStr} ${labelStr} ${idStr}`;

      let matches = false;
      if (filterLower === 'all') {
        matches = true;
      } else if (filterLower === 'swift') {
        matches = combined.includes('swift') || combined.includes('ios');
      } else if (filterLower === 'python') {
        matches = combined.includes('python') || combined.includes('fastapi') || combined.includes('ai');
      } else if (filterLower === 'web') {
        matches = combined.includes('typescript') || combined.includes('react') || combined.includes('javascript');
      } else if (filterLower === 'cpp') {
        matches = combined.includes('cpp') || combined.includes('lasd');
      } else if (filterLower === 'medical') {
        matches = combined.includes('medicina') || combined.includes('salute') || combined.includes('datamed');
      } else if (filterLower === 'bridges') {
        matches = true;
      }

      updates.push({
        id: node.id,
        opacity: matches ? 1.0 : 0.15
      });
    });

    nodesDS.update(updates);
  }
}

/**
 * Mobile Navigation & Responsive Routing (Exclusive for Mobile Screens <= 900px)
 */
function switchMobileTab(tab) {
  document.body.classList.remove('mob-view-graph', 'mob-view-sidebar', 'mob-view-palazzo');
  document.body.classList.add('mob-view-' + tab);

  document.querySelectorAll('.mobile-nav-btn').forEach(btn => btn.classList.remove('active'));
  const activeBtn = document.getElementById('mob-tab-' + tab);
  if (activeBtn) activeBtn.classList.add('active');

  if (tab === 'graph' && network) {
    setTimeout(() => {
      try {
        network.redraw();
        network.fit({ animation: { duration: 300, easingFunction: 'easeInOutQuad' } });
      } catch (e) {}
    }, 80);
  }
}

window.addEventListener('DOMContentLoaded', () => {
  if (window.innerWidth <= 900) {
    switchMobileTab('graph');
  }
  initNetwork();
  fetchBrainData();
  setupSearch();
  setupDropzone();
  setupBackdropClicks();
});

