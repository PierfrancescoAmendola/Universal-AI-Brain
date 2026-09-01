/**
 * Universal AI Brain - Interactive Cyberpunk Developer CLI Terminal Engine
 * Provides live command execution, network inspection, pathfinding, and log capture.
 */

window.TerminalEngine = (function () {
  'use strict';

  let logs = [];
  let commandHistory = [];
  let historyIndex = -1;
  let currentTab = 'cli'; // 'cli', 'all', 'http', 'nodes'
  let searchTerm = '';
  let isMinimized = false;
  let isExpanded = false;

  const COMMANDS = [
    'help', 'status', 'stats', 'search', 'find', 'node', 'inspect',
    'links', 'edges', 'path', 'tensions', 'resurface', 'firmware',
    'view', 'filter', 'clear', 'cls', 'ping', 'export'
  ];

  /**
   * Log an event into the Terminal
   */
  function log(type, category, message, data = null) {
    const entry = {
      id: 'log-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5),
      timestamp: new Date(),
      type: type || 'info', // 'cmd', 'info', 'success', 'warning', 'error', 'http', 'node'
      category: category || 'SYS',
      message: message || '',
      data: data
    };
    logs.push(entry);
    if (logs.length > 500) logs.shift();

    if (currentTab === 'all' || (currentTab === 'http' && entry.category === 'HTTP') || (currentTab === 'nodes' && entry.category === 'NODE')) {
      renderNewLogEntry(entry);
    }
    updateCounters();
    updateMiniTicker(entry);
  }

  /**
   * Dedicated HTTP request log entry
   */
  function logHttp(httpEntry) {
    const entry = {
      id: httpEntry.id || ('http-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5)),
      timestamp: httpEntry.timestamp || new Date(),
      type: 'http',
      category: 'HTTP',
      method: httpEntry.method || 'GET',
      url: httpEntry.url || '',
      statusCode: httpEntry.statusCode || 200,
      statusText: httpEntry.statusText || 'OK',
      durationMs: httpEntry.durationMs || 0,
      payload: httpEntry.payload || null,
      responseSnippet: httpEntry.responseSnippet || null,
      message: `${httpEntry.method} ${httpEntry.url} ➔ ${httpEntry.statusCode || 200} (${httpEntry.durationMs || 0}ms)`
    };

    const existingIdx = logs.findIndex(l => l.id === entry.id);
    if (existingIdx !== -1) {
      logs[existingIdx] = entry;
    } else {
      logs.push(entry);
      if (logs.length > 500) logs.shift();
    }

    if (currentTab === 'all' || currentTab === 'http') {
      renderAllLogs();
    }
    updateCounters();
    updateMiniTicker(entry);
  }

  /**
   * Dedicated Node / Synapse log entry
   */
  function logNode(actionType, nodeData) {
    const entry = {
      id: 'node-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5),
      timestamp: new Date(),
      type: 'node',
      category: 'NODE',
      actionType: actionType || 'ISPEZIONE',
      nodeId: nodeData.id || '',
      label: nodeData.label || nodeData.id || 'Nodo',
      hemisphere: nodeData.hemisphere || 'LEFT',
      primaryLabel: nodeData.primary_label || nodeData.category || '',
      tags: Array.isArray(nodeData.tags) ? nodeData.tags : [],
      summary: nodeData.summary || '',
      details: nodeData.details || {},
      message: `[${actionType}] ${nodeData.label || nodeData.id} (${nodeData.hemisphere || 'LEFT'})`
    };

    logs.push(entry);
    if (logs.length > 500) logs.shift();

    if (currentTab === 'all' || currentTab === 'nodes') {
      renderNewLogEntry(entry);
    }
    updateCounters();
    updateMiniTicker(entry);
  }

  function formatTime(d) {
    if (!(d instanceof Date)) d = new Date(d);
    return d.toTimeString().split(' ')[0] + '.' + String(d.getMilliseconds()).padStart(3, '0');
  }

  function updateMiniTicker(entry) {
    const tickerEl = document.getElementById('terminal-mini-ticker-text');
    if (!tickerEl) return;

    let icon = '⚡';
    let color = '#38bdf8';
    let text = entry.message || '';

    if (entry.category === 'HTTP') {
      const isOk = entry.statusCode >= 200 && entry.statusCode < 300;
      icon = isOk ? '🟢' : '🔴';
      color = isOk ? '#10b981' : '#ef4444';
      text = `[HTTP ${entry.statusCode || 200}] ${entry.method || 'GET'} ${entry.url || ''} (${entry.durationMs || 0}ms)`;
    } else if (entry.category === 'NODE') {
      icon = '🧠';
      color = entry.hemisphere === 'RIGHT' ? '#ff007f' : '#00d2ff';
      text = `[${entry.actionType || 'NODO'}] ${entry.label || entry.nodeId || ''} (${entry.primaryLabel || entry.hemisphere || 'SX'})`;
    } else if (entry.category === 'CLI') {
      icon = '💻';
      color = '#a855f7';
    } else if (entry.category === 'WARN') {
      icon = '⚠️';
      color = '#f59e0b';
    } else if (entry.category === 'ERR') {
      icon = '❌';
      color = '#ef4444';
    }

    tickerEl.innerHTML = `<span style="color:${color}; font-weight:700;">${icon} [${formatTime(entry.timestamp)}]</span> <span style="color:#f8fafc;">${escapeHtml(text)}</span>`;
    
    // Quick pulse animation
    tickerEl.classList.remove('pulse-update');
    void tickerEl.offsetWidth; // trigger reflow
    tickerEl.classList.add('pulse-update');
  }

  function renderNewLogEntry(entry) {
    const body = document.getElementById('terminal-body');
    if (!body) return;

    if (!matchesFilter(entry)) return;

    // If body contains empty state, clear it
    const emptyState = body.querySelector('.term-empty-state');
    if (emptyState) body.innerHTML = '';

    const line = document.createElement('div');
    line.className = 'term-line-wrapper';
    line.innerHTML = formatLogHtml(entry);
    body.appendChild(line);
    body.scrollTop = body.scrollHeight;
  }

  function matchesFilter(entry) {
    if (currentTab === 'http' && entry.category !== 'HTTP') return false;
    if (currentTab === 'nodes' && entry.category !== 'NODE') return false;

    if (searchTerm) {
      const q = searchTerm.toLowerCase();
      const txt = (entry.message + ' ' + (entry.category || '') + ' ' + (entry.label || '') + ' ' + (entry.url || '')).toLowerCase();
      if (!txt.includes(q)) return false;
    }
    return true;
  }

  function formatLogHtml(entry) {
    const time = formatTime(entry.timestamp);

    if (entry.category === 'HTTP') {
      const method = (entry.method || 'GET').toUpperCase();
      const methodClass = method.toLowerCase();
      const isOk = (entry.statusCode >= 200 && entry.statusCode < 300) || !entry.statusCode;
      const statusClass = isOk ? 's-200' : 's-err';
      const statusText = entry.statusCode ? `${entry.statusCode} ${entry.statusText || 'OK'}` : '200 OK';
      const durationText = entry.durationMs ? `${entry.durationMs}ms` : '12ms';

      let payloadHtml = '';
      if (entry.payload) {
        payloadHtml = `
          <div class="term-payload-toggle" onclick="TerminalEngine.toggleDetail('${entry.id}-req')">▶ Mostra Payload Inviato (JSON)</div>
          <div id="${entry.id}-req" class="term-payload-box" style="display:none;">
            <pre>${escapeHtml(typeof entry.payload === 'object' ? JSON.stringify(entry.payload, null, 2) : entry.payload)}</pre>
          </div>
        `;
      }

      let resHtml = '';
      if (entry.responseSnippet) {
        resHtml = `
          <div class="term-payload-toggle" onclick="TerminalEngine.toggleDetail('${entry.id}-res')">▶ Risposta Server (Preview)</div>
          <div id="${entry.id}-res" class="term-payload-box" style="display:none;">
            <pre>${escapeHtml(typeof entry.responseSnippet === 'object' ? JSON.stringify(entry.responseSnippet, null, 2) : entry.responseSnippet)}</pre>
          </div>
        `;
      }

      return `
        <div class="term-entry type-${methodClass}">
          <div class="term-entry-header">
            <div class="term-entry-left">
              <span class="term-time">[${time}]</span>
              <span class="term-badge-method ${methodClass}">${method}</span>
              <span class="term-entry-url">${escapeHtml(entry.url || '/api')}</span>
            </div>
            <div class="term-entry-right">
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
    }

    if (entry.category === 'NODE') {
      const isLeft = entry.hemisphere === 'LEFT';
      const hemiClass = isLeft ? 'left' : 'right';
      const hemiLabel = isLeft ? 'SX (Tech)' : 'DX (Vision)';
      const tagsStr = entry.tags && entry.tags.length ? entry.tags.map(t => `#${t}`).join(' ') : '';

      return `
        <div class="term-entry type-node">
          <div class="term-entry-header">
            <div class="term-entry-left">
              <span class="term-time">[${time}]</span>
              <span class="term-badge-method node">${escapeHtml(entry.actionType || 'CONCETTO')}</span>
              <span class="term-node-title" onclick="TerminalEngine.focusGraphNode('${escapeHtml(entry.nodeId)}')" style="cursor:pointer;" title="Clicca per evidenziare nel grafo">
                ${escapeHtml(entry.label || entry.nodeId)}
              </span>
              <span class="term-hemi-tag ${hemiClass}">${hemiLabel}</span>
              ${entry.primaryLabel ? `<code class="term-primary-badge">[${escapeHtml(entry.primaryLabel)}]</code>` : ''}
            </div>
            <span class="term-badge-status s-200">SINAPSI ATTIVA</span>
          </div>
          <div class="term-entry-detail">
            <div style="color:#cbd5e1; font-size:11.5px; margin-bottom:4px;">${escapeHtml(entry.summary || 'Nessun sommario disponibile.')}</div>
            ${tagsStr ? `<div style="color:#38bdf8; font-size:10.5px; margin-bottom:4px;">${escapeHtml(tagsStr)}</div>` : ''}
            <div class="term-payload-toggle" onclick="TerminalEngine.toggleDetail('${entry.id}-det')">▶ Dettagli e Attributi JSON</div>
            <div id="${entry.id}-det" class="term-payload-box" style="display:none;">
              <pre>${escapeHtml(JSON.stringify({ id: entry.nodeId, hemisphere: entry.hemisphere, primary_label: entry.primaryLabel, tags: entry.tags, details: entry.details }, null, 2))}</pre>
            </div>
          </div>
        </div>
      `;
    }

    // Default System / CLI / Info / Warn / Error log formatting
    let badgeColor = '#94a3b8';
    if (entry.category === 'CLI') badgeColor = '#a855f7';
    else if (entry.category === 'WARN') badgeColor = '#f59e0b';
    else if (entry.category === 'ERR') badgeColor = '#ef4444';
    else if (entry.category === 'SYS') badgeColor = '#00d2ff';
    else if (entry.category === 'STATS' || entry.category === 'SEARCH' || entry.category === 'PATH') badgeColor = '#10b981';

    return `
      <div class="term-line">
        <span class="term-time">[${time}]</span>
        <span style="color:${badgeColor}; font-weight:700; flex-shrink:0;">[${entry.category}]</span>
        <div style="flex:1;">${entry.message}</div>
      </div>
    `;
  }

  function updateCounters() {
    const cCli = document.getElementById('count-cli');
    const cAll = document.getElementById('count-all');
    const cHttp = document.getElementById('count-http');
    const cNodes = document.getElementById('count-nodes');
    const hudBadge = document.getElementById('hud-terminal-badge');

    const httpCount = logs.filter(l => l.category === 'HTTP').length;
    const nodeCount = logs.filter(l => l.category === 'NODE').length;
    const cliCount = logs.filter(l => l.category === 'CLI' || l.category === 'SYS' || l.category === 'STATS' || l.category === 'SEARCH' || l.category === 'PATH').length;

    if (cCli) cCli.innerText = cliCount;
    if (cAll) cAll.innerText = logs.length;
    if (cHttp) cHttp.innerText = httpCount;
    if (cNodes) cNodes.innerText = nodeCount;
    if (hudBadge) hudBadge.innerText = logs.length;
  }

  function renderAllLogs() {
    const body = document.getElementById('terminal-body');
    if (!body) return;
    body.innerHTML = '';

    let list = [];

    if (currentTab === 'cli') {
      list = logs.filter(l => l.category === 'CLI' || l.category === 'SYS' || l.category === 'STATS' || l.category === 'SEARCH' || l.category === 'PATH' || l.type === 'cmd');
    } else if (currentTab === 'http') {
      list = logs.filter(l => l.category === 'HTTP');
    } else if (currentTab === 'nodes') {
      list = logs.filter(l => l.category === 'NODE');
    } else {
      list = logs;
    }

    if (searchTerm) {
      const q = searchTerm.toLowerCase();
      list = list.filter(entry => {
        const txt = (entry.message + ' ' + (entry.category || '') + ' ' + (entry.label || '') + ' ' + (entry.url || '')).toLowerCase();
        return txt.includes(q);
      });
    }

    if (list.length === 0) {
      let emptyMsg = 'Nessun log registrato.';
      if (currentTab === 'cli') {
        emptyMsg = `
          <div class="term-empty-state">
            <span style="font-size:24px; display:block; margin-bottom:8px;">💻</span>
            <strong style="color:#00d2ff;">Terminale Interattivo Developer CLI</strong><br>
            <span style="color:#94a3b8; font-size:11px;">Digita un comando nel prompt in basso (es. <code style="color:#00d2ff;">help</code>, <code style="color:#00d2ff;">stats</code>, <code style="color:#00d2ff;">search swift</code>, <code style="color:#00d2ff;">path a b</code>, <code style="color:#00d2ff;">ping</code>).</span>
          </div>
        `;
      } else if (currentTab === 'http') {
        emptyMsg = `
          <div class="term-empty-state">
            <span style="font-size:24px; display:block; margin-bottom:8px;">🌐</span>
            <strong style="color:#38bdf8;">HTTP & REST API Network Inspector</strong><br>
            <span style="color:#94a3b8; font-size:11px;">In ascolto delle chiamate API in tempo reale (GET /api/stats, POST /api/memory/ingest, GET /api/tensions, ecc.). Tutte le richieste appariranno qui con status code, durata in millisecondi e payload JSON.</span>
          </div>
        `;
      } else if (currentTab === 'nodes') {
        emptyMsg = `
          <div class="term-empty-state">
            <span style="font-size:24px; display:block; margin-bottom:8px;">🧠</span>
            <strong style="color:#10b981;">Nodi & Sinapsi Live Feed</strong><br>
            <span style="color:#94a3b8; font-size:11px;">In ascolto degli eventi del connettoma neurale. Clicca sui nodi nel grafo o esegui ricerche per visualizzare le interazioni e le sinapsi in tempo reale.</span>
          </div>
        `;
      } else {
        emptyMsg = `
          <div class="term-empty-state">
            <span style="font-size:24px; display:block; margin-bottom:8px;">📋</span>
            <strong style="color:#f8fafc;">Tutti i Log del Sistema</strong><br>
            <span style="color:#94a3b8; font-size:11px;">Timeline unificata di tutti gli eventi di sistema, comandi CLI, richieste HTTP e sinapsi neurali.</span>
          </div>
        `;
      }

      body.innerHTML = emptyMsg;
      return;
    }

    list.forEach(entry => {
      const line = document.createElement('div');
      line.className = 'term-line-wrapper';
      line.innerHTML = formatLogHtml(entry);
      body.appendChild(line);
    });

    body.scrollTop = body.scrollHeight;
  }

  /**
   * Switch between console tabs: 'cli', 'all', 'http', 'nodes'
   */
  function setTab(tabName) {
    currentTab = tabName || 'cli';
    
    // Update active tab buttons in UI
    document.querySelectorAll('.term-tab').forEach(btn => {
      if (btn.dataset.tab === currentTab) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    // Update search placeholder
    const searchInput = document.getElementById('term-search');
    if (searchInput) {
      if (currentTab === 'cli') searchInput.placeholder = 'Filtra output comandi...';
      else if (currentTab === 'http') searchInput.placeholder = 'Filtra per URL, metodo (GET/POST), status 200...';
      else if (currentTab === 'nodes') searchInput.placeholder = 'Filtra per nome nodo, tag, emisfero...';
      else searchInput.placeholder = 'Filtra tutti i log...';
    }

    renderAllLogs();
  }

  /**
   * Interactive CLI Command Dispatcher
   */
  async function executeCommand(cmdLine) {
    const raw = (cmdLine || '').trim();
    if (!raw) return;

    commandHistory.push(raw);
    historyIndex = commandHistory.length;

    // Echo command in terminal
    const body = document.getElementById('terminal-body');
    if (body) {
      const echo = document.createElement('div');
      echo.className = 'term-cmd-echo';
      echo.innerHTML = `<span class="prompt">synapse:~$</span> <span>${escapeHtml(raw)}</span>`;
      body.appendChild(echo);
    }

    const parts = raw.split(/\s+/);
    const cmd = parts[0].toLowerCase();
    const args = parts.slice(1);

    switch (cmd) {
      case 'help':
        execHelp();
        break;
      case 'status':
      case 'stats':
        await execStats();
        break;
      case 'search':
      case 'find':
        await execSearch(args.join(' '));
        break;
      case 'node':
      case 'inspect':
        await execInspectNode(args[0]);
        break;
      case 'links':
      case 'edges':
        await execLinks(args[0]);
        break;
      case 'path':
        await execPath(args[0], args[1]);
        break;
      case 'tensions':
      case 'tension':
        execTensions();
        break;
      case 'resurface':
        execResurface();
        break;
      case 'firmware':
        execFirmware(args[0]);
        break;
      case 'view':
        execView(args[0]);
        break;
      case 'filter':
        execFilter(args[0]);
        break;
      case 'clear':
      case 'cls':
        clearLogs();
        break;
      case 'ping':
        execPing();
        break;
      case 'export':
        execExport(args[0]);
        break;
      default:
        printOutput(`Comando non riconosciuto: <strong style="color:#ef4444;">${escapeHtml(cmd)}</strong>. Digita <strong style="color:#00d2ff;">help</strong> per la lista dei comandi.`, 'CLI');
        break;
    }

    if (body) body.scrollTop = body.scrollHeight;
  }

  function printOutput(htmlMessage, category = 'CLI') {
    const entry = {
      id: Date.now() + Math.random(),
      timestamp: new Date(),
      type: 'info',
      category: category,
      message: htmlMessage
    };
    logs.push(entry);
    renderNewLogEntry(entry);
    updateCounters();
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  async function ensureBrainData() {
    if (window.rawNodes && Array.isArray(window.rawNodes) && window.rawNodes.length > 0) {
      return { nodes: window.rawNodes, edges: window.rawEdges || [] };
    }
    try {
      const res = await fetch('/brain.json');
      if (res.ok) {
        const data = await res.json();
        window.rawNodes = data.nodes || [];
        window.rawEdges = data.links || [];
        return { nodes: window.rawNodes, edges: window.rawEdges };
      }
    } catch (e) {
      console.warn('Terminal Engine unable to fetch /brain.json:', e);
    }
    return { nodes: window.rawNodes || [], edges: window.rawEdges || [] };
  }

  /* Command Implementations */

  function execHelp() {
    const html = `
      <div class="term-res-block">
        <strong style="color:#00d2ff;">=== SYNAPSE DEVELOPER CLI - GUIDA COMANDI ===</strong>
        <table class="term-table">
          <thead>
            <tr><th>Comando</th><th>Descrizione</th><th>Esempio</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>help</strong></td><td>Mostra questa guida</td><td>help</td></tr>
            <tr><td><strong>stats</strong></td><td>Metriche e statistiche del connettoma</td><td>stats</td></tr>
            <tr><td><strong>search &lt;query&gt;</strong></td><td>Cerca concetti ed evidenzia nel grafo</td><td>search swift</td></tr>
            <tr><td><strong>node &lt;id&gt;</strong></td><td>Ispeziona dettagli e attributi atomici</td><td>node person-pierfrancesco</td></tr>
            <tr><td><strong>links &lt;id&gt;</strong></td><td>Elenca tutte le sinapsi e relazioni</td><td>links person-pierfrancesco</td></tr>
            <tr><td><strong>path &lt;from&gt; &lt;to&gt;</strong></td><td>Trova cammino minimo nel Corpo Calloso</td><td>path person-pierfrancesco project-streaksup</td></tr>
            <tr><td><strong>tensions</strong></td><td>Visualizza tensioni cognitive e contraddizioni</td><td>tensions</td></tr>
            <tr><td><strong>resurface</strong></td><td>Briefing delle memorie (Daily Resurface)</td><td>resurface</td></tr>
            <tr><td><strong>firmware</strong></td><td>Visualizza i 9 modelli mentali cognitivi</td><td>firmware</td></tr>
            <tr><td><strong>view &lt;mode&gt;</strong></td><td>Cambia vista (areas, full, 2d, projector, globe)</td><td>view areas</td></tr>
            <tr><td><strong>filter &lt;hemi&gt;</strong></td><td>Filtra emisfero (all, left, right, l0)</td><td>filter left</td></tr>
            <tr><td><strong>clear / cls</strong></td><td>Pulisce l'output del terminale</td><td>clear</td></tr>
            <tr><td><strong>ping</strong></td><td>Verifica latenza e stato del backend</td><td>ping</td></tr>
            <tr><td><strong>export &lt;tipo&gt;</strong></td><td>Esporta dati (json, prompt, md)</td><td>export json</td></tr>
          </tbody>
        </table>
      </div>
    `;
    printOutput(html, 'CLI');
  }

  async function execStats() {
    const { nodes, edges } = await ensureBrainData();
    let sx = 0, dx = 0, callosum = 0, l0 = 0, l1 = 0, l2 = 0;

    nodes.forEach(n => {
      if (n.hemisphere === 'LEFT') sx++;
      else dx++;
      if (n.layer_level === 0) l0++;
      else if (n.layer_level === 1) l1++;
      else l2++;
    });

    edges.forEach(e => {
      const sId = typeof e.source === 'object' ? e.source.id : e.source;
      const tId = typeof e.target === 'object' ? e.target.id : e.target;
      const sNode = nodes.find(n => n.id === sId);
      const tNode = nodes.find(n => n.id === tId);
      if (sNode && tNode && sNode.hemisphere !== tNode.hemisphere) callosum++;
    });

    const html = `
      <div class="term-res-block">
        <div style="font-weight:700; color:#00d2ff; margin-bottom:4px;">📊 STATO CONNETTOMA NEURALE</div>
        <div>Nodi Totali: <strong>${nodes.length}</strong> (<span class="term-badge-sx">SX: ${sx}</span> <span class="term-badge-dx">DX: ${dx}</span>)</div>
        <div>Sinapsi Totali: <strong>${edges.length}</strong> (<span class="term-badge-callosum">Ponti Corpo Calloso: ${callosum}</span>)</div>
        <div>Gerarchia Palazzo: <span class="term-badge-gold">L0 Macro-Domini: ${l0}</span> · <strong>L1 Progetti/Episodi: ${l1}</strong> · <span>L2 Moduli: ${l2}</span></div>
        <div style="margin-top:4px; color:var(--text-muted);">Piano Attivo: <strong>${window.currentPalazzoFloor || 'all'}</strong> · Vista: <strong>${window.graphViewMode || '2d'}</strong></div>
      </div>
    `;
    printOutput(html, 'STATS');
  }

  async function execSearch(query) {
    if (!query) {
      printOutput('Specificare un termine di ricerca. Es: <strong style="color:#00d2ff;">search swift</strong>', 'CLI');
      return;
    }
    const { nodes } = await ensureBrainData();
    const q = query.toLowerCase().trim();
    const matches = nodes.filter(n => {
      return (n.label && n.label.toLowerCase().includes(q)) ||
             (n.id && n.id.toLowerCase().includes(q)) ||
             (n.category && n.category.toLowerCase().includes(q)) ||
             (n.tags && Array.isArray(n.tags) && n.tags.some(t => t.toLowerCase().includes(q))) ||
             (n.summary && n.summary.toLowerCase().includes(q));
    });

    if (matches.length === 0) {
      printOutput(`Nessun nodo trovato per la query: <strong>"${escapeHtml(query)}"</strong>`, 'SEARCH');
      return;
    }

    let rows = matches.slice(0, 15).map(n => {
      const badge = n.hemisphere === 'LEFT' ? '<span class="term-badge-sx">SX</span>' : '<span class="term-badge-dx">DX</span>';
      const lBadge = n.layer_level === 0 ? '<span class="term-badge-gold">L0</span>' : `L${n.layer_level}`;
      return `
        <tr>
          <td><span class="term-link-item" onclick="TerminalEngine.inspectFromCli('${n.id}')">${n.id}</span></td>
          <td>${escapeHtml(n.label)}</td>
          <td>${badge} ${lBadge}</td>
          <td>${escapeHtml(n.primary_label || n.category || '')}</td>
        </tr>
      `;
    }).join('');

    const html = `
      <div class="term-res-block">
        <strong style="color:#00d2ff;">🔍 Risultati ricerca per "${escapeHtml(query)}" (${matches.length} trovati):</strong>
        <table class="term-table">
          <thead><tr><th>ID</th><th>Label</th><th>Emisfero / Livello</th><th>Categoria</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
        ${matches.length > 15 ? `<div style="color:var(--text-muted); font-size:10px;">Mostrati primi 15 di ${matches.length} nodi.</div>` : ''}
      </div>
    `;
    printOutput(html, 'SEARCH');

    // Seleziona ed evidenzia nel grafo Vis.js
    if (matches.length > 0 && typeof window.selectNodeInGraph === 'function') {
      window.selectNodeInGraph(matches[0].id);
    }
  }

  async function execInspectNode(nodeId) {
    if (!nodeId) {
      printOutput('Specificare un ID nodo. Es: <strong style="color:#00d2ff;">node person-pierfrancesco</strong>', 'CLI');
      return;
    }
    const { nodes } = await ensureBrainData();
    const n = nodes.find(item => item.id === nodeId || (item.label && item.label.toLowerCase() === nodeId.toLowerCase()));
    if (!n) {
      printOutput(`Nodo non trovato: <strong style="color:#ef4444;">${escapeHtml(nodeId)}</strong>`, 'INSPECT');
      return;
    }

    const badge = n.hemisphere === 'LEFT' ? '<span class="term-badge-sx">SX (Tech/Logica)</span>' : '<span class="term-badge-dx">DX (Vision/Design)</span>';
    const tags = Array.isArray(n.tags) ? n.tags.join(', ') : (n.tags || 'Nessuno');
    const detailsStr = typeof n.details === 'object' ? JSON.stringify(n.details, null, 2) : (n.details || '{}');

    const html = `
      <div class="term-res-block">
        <div style="font-size:14px; font-weight:700; color:#00d2ff;">${escapeHtml(n.label || n.id)}</div>
        <div style="font-size:11px; color:var(--text-muted); margin-bottom:6px;">ID: <code>${n.id}</code> · Emisfero: ${badge} · Piano: <strong>L${n.layer_level}</strong></div>
        <div style="margin:4px 0;"><strong>Sommario:</strong> ${escapeHtml(n.summary || 'Nessun sommario disponibile.')}</div>
        <div style="margin:4px 0;"><strong>Tag:</strong> <code>${escapeHtml(tags)}</code></div>
        ${detailsStr !== '{}' ? `<div style="margin-top:6px;"><details><summary style="cursor:pointer; color:var(--accent-cyan);">Dettagli Strutturati (JSON)</summary><pre style="background:rgba(0,0,0,0.5); padding:6px; border-radius:4px; font-size:10px; max-height:120px; overflow-y:auto;">${escapeHtml(detailsStr)}</pre></details></div>` : ''}
        <div style="margin-top:6px; display:flex; gap:8px;">
          <button class="term-btn" onclick="TerminalEngine.inspectLinks('${n.id}')">🕸️ Mostra Connessioni</button>
          <button class="term-btn" onclick="TerminalEngine.focusGraphNode('${n.id}')">🎯 Centra nel Grafo</button>
        </div>
      </div>
    `;
    printOutput(html, 'INSPECT');

    if (typeof window.showNodeDetails === 'function') {
      window.showNodeDetails(n);
    }
  }

  async function execLinks(nodeId) {
    if (!nodeId) {
      printOutput('Specificare un ID nodo. Es: <strong style="color:#00d2ff;">links person-pierfrancesco</strong>', 'CLI');
      return;
    }
    const { nodes, edges } = await ensureBrainData();
    const n = nodes.find(item => item.id === nodeId || (item.label && item.label.toLowerCase() === nodeId.toLowerCase()));
    if (!n) {
      printOutput(`Nodo non trovato: <strong style="color:#ef4444;">${escapeHtml(nodeId)}</strong>`, 'LINKS');
      return;
    }

    const connectedEdges = edges.filter(e => {
      const sId = typeof e.source === 'object' ? e.source.id : e.source;
      const tId = typeof e.target === 'object' ? e.target.id : e.target;
      return sId === n.id || tId === n.id;
    });

    if (connectedEdges.length === 0) {
      printOutput(`Il nodo <strong>${n.id}</strong> non ha sinapsi collegate (nodo orfano).`, 'LINKS');
      return;
    }

    let rows = connectedEdges.map(e => {
      const sId = typeof e.source === 'object' ? e.source.id : e.source;
      const tId = typeof e.target === 'object' ? e.target.id : e.target;
      const otherId = sId === n.id ? tId : sId;
      const otherNode = nodes.find(item => item.id === otherId) || { label: otherId, hemisphere: 'LEFT' };
      const isOut = sId === n.id;
      const dir = isOut ? '<span style="color:#10b981;">➔ OUT</span>' : '<span style="color:#38bdf8;">⬅ IN</span>';
      const isCross = (n.hemisphere !== otherNode.hemisphere);
      const crossBadge = isCross ? '<span class="term-badge-callosum">Corpo Calloso</span>' : '';

      return `
        <tr>
          <td>${dir}</td>
          <td><span class="term-link-item" onclick="TerminalEngine.inspectFromCli('${otherId}')">${otherId}</span></td>
          <td><strong>${escapeHtml(otherNode.label || otherId)}</strong></td>
          <td><code style="color:#a855f7;">${escapeHtml(e.relation || 'CONNECTS_TO')}</code></td>
          <td>${crossBadge}</td>
        </tr>
      `;
    }).join('');

    const html = `
      <div class="term-res-block">
        <strong style="color:#00d2ff;">🕸️ Connessioni Sinaptiche per "${escapeHtml(n.label || n.id)}" (${connectedEdges.length} archi):</strong>
        <table class="term-table">
          <thead><tr><th>Dir</th><th>Target ID</th><th>Nome Target</th><th>Relazione</th><th>Ponte</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
    `;
    printOutput(html, 'LINKS');
  }

  async function execPath(fromId, toId) {
    if (!fromId || !toId) {
      printOutput('Specificare nodo di partenza e di arrivo. Es: <strong style="color:#00d2ff;">path person-pierfrancesco project-streaksup</strong>', 'CLI');
      return;
    }

    const { nodes, edges } = await ensureBrainData();
    const sNode = nodes.find(n => n.id === fromId || (n.label && n.label.toLowerCase() === fromId.toLowerCase()));
    const tNode = nodes.find(n => n.id === toId || (n.label && n.label.toLowerCase() === toId.toLowerCase()));

    if (!sNode || !tNode) {
      printOutput(`Impossibile trovare uno o entrambi i nodi (${fromId} -> ${toId})`, 'PATH');
      return;
    }

    // BFS Shortest Path
    const adj = new Map();
    nodes.forEach(n => adj.set(n.id, []));
    edges.forEach(e => {
      const s = typeof e.source === 'object' ? e.source.id : e.source;
      const t = typeof e.target === 'object' ? e.target.id : e.target;
      if (adj.has(s)) adj.get(s).push({ target: t, rel: e.relation || 'CONNECTS' });
      if (adj.has(t)) adj.get(t).push({ target: s, rel: e.relation || 'CONNECTS' });
    });

    const queue = [[sNode.id]];
    const visited = new Set([sNode.id]);
    let shortestPath = null;

    while (queue.length > 0) {
      const path = queue.shift();
      const curr = path[path.length - 1];

      if (curr === tNode.id) {
        shortestPath = path;
        break;
      }

      const nbrs = adj.get(curr) || [];
      for (const nbr of nbrs) {
        if (!visited.has(nbr.target)) {
          visited.add(nbr.target);
          queue.push([...path, nbr.target]);
        }
      }
    }

    if (!shortestPath) {
      printOutput(`Nessun cammino sinaptico trovato tra <strong>${sNode.id}</strong> e <strong>${tNode.id}</strong> (nodi disconnessi).`, 'PATH');
      return;
    }

    let stepsHtml = shortestPath.map((id, idx) => {
      const node = nodes.find(n => n.id === id) || { label: id };
      return `<span class="term-link-item" onclick="TerminalEngine.inspectFromCli('${id}')">${escapeHtml(node.label || id)}</span>`;
    }).join(' <span style="color:#00d2ff;">➔</span> ');

    const html = `
      <div class="term-res-block">
        <strong style="color:#10b981;">⚡ Cammino Sinaptico Minimo (${shortestPath.length - 1} salti):</strong>
        <div style="margin-top:8px; font-size:12px; line-height:1.8;">${stepsHtml}</div>
      </div>
    `;
    printOutput(html, 'PATH');
  }

  function execTensions() {
    if (typeof window.openTensionsModal === 'function') {
      window.openTensionsModal();
      printOutput('Apertura matrice delle Tensioni Cognitive...', 'CLI');
    }
  }

  function execResurface() {
    if (typeof window.openResurfaceModal === 'function') {
      window.openResurfaceModal();
      printOutput('Avvio briefing cognitivo 90s Daily Resurface...', 'CLI');
    }
  }

  function execFirmware(fId) {
    if (typeof window.openFirmwareModal === 'function') {
      window.openFirmwareModal();
      printOutput('Apertura pannello 9 Firmware Cognitivi...', 'CLI');
    }
  }

  function execView(mode) {
    if (!mode) {
      printOutput('Specificare modalità di visualizzazione: <strong style="color:#00d2ff;">areas</strong>, <strong style="color:#00d2ff;">full</strong>, <strong style="color:#00d2ff;">projector</strong>, <strong style="color:#00d2ff;">globe</strong>', 'CLI');
      return;
    }
    const m = mode.toLowerCase();
    if (m === 'projector' || m === '3d') {
      if (typeof window.setGraphViewMode === 'function') window.setGraphViewMode('projector');
      printOutput('Attivazione 3D Cognitive Embedding Projector.', 'VIEW');
    } else if (m === 'globe' || m === 'emisferi') {
      if (typeof window.setGraphViewMode === 'function') window.setGraphViewMode('projector');
      if (window.EmbeddingProjector) window.EmbeddingProjector.setDimension('globe');
      printOutput('Attivazione Proiezione Emisferi Globo.', 'VIEW');
    } else if (m === 'areas' || m === 'aree' || m === '2d') {
      if (typeof window.setGraphViewMode === 'function') window.setGraphViewMode('areas');
      printOutput('Attivazione Grafo 2D ad Aree / Hub.', 'VIEW');
    } else if (m === 'full' || m === 'completo') {
      if (typeof window.setGraphViewMode === 'function') window.setGraphViewMode('full');
      printOutput('Attivazione Grafo 2D Rete Completa.', 'VIEW');
    } else {
      printOutput(`Modalità sconosciuta: ${mode}`, 'VIEW');
    }
  }

  function execFilter(filter) {
    if (!filter) {
      printOutput('Specificare filtro: <strong style="color:#00d2ff;">all, left, right, l0</strong>', 'CLI');
      return;
    }
    const f = filter.toLowerCase();
    if (f === 'left' || f === 'sx') {
      if (typeof window.applyRadarFilter === 'function') window.applyRadarFilter('bridges', 'Ponti SX/DX');
      printOutput('Applicato filtro Emisfero Sinistro.', 'FILTER');
    } else if (f === 'right' || f === 'dx') {
      printOutput('Applicato filtro Emisfero Destro.', 'FILTER');
    } else {
      if (typeof window.applyRadarFilter === 'function') window.applyRadarFilter('all', 'Tutti');
      printOutput('Ripristinati tutti i filtri.', 'FILTER');
    }
  }

  function execPing() {
    const t0 = performance.now();
    fetch('/api/stats')
      .then(res => res.json())
      .then(() => {
        const dt = Math.round(performance.now() - t0);
        printOutput(`PONG! Backend SQLite online. Latenza: <strong style="color:#10b981;">${dt}ms</strong>`, 'PING');
      })
      .catch(err => {
        printOutput(`Errore Ping: ${err.message}`, 'PING');
      });
  }

  function execExport(type) {
    const t = (type || 'json').toLowerCase();
    if (t === 'prompt' && typeof window.copyAIPrompt === 'function') {
      window.copyAIPrompt();
      printOutput('Prompt di contesto AI copiato negli appunti!', 'EXPORT');
    } else if (t === 'md' && typeof window.copyMarkdownExport === 'function') {
      window.copyMarkdownExport();
      printOutput('Markdown esportato negli appunti!', 'EXPORT');
    } else {
      window.open('/api/export/backup', '_blank');
      printOutput('Download del backup JSON avviato!', 'EXPORT');
    }
  }

  function clearLogs() {
    logs = [];
    renderAllLogs();
    updateCounters();
    const tickerEl = document.getElementById('terminal-mini-ticker-text');
    if (tickerEl) tickerEl.innerHTML = '<span style="color:#94a3b8;">Buffer terminale pulito.</span>';
  }

  function toggleDetail(elementId) {
    const el = document.getElementById(elementId);
    if (!el) return;
    el.style.display = (el.style.display === 'none' || !el.style.display) ? 'block' : 'none';
  }

  /* Drawer UI Helpers */
  function toggleDrawer() {
    const drawer = document.getElementById('light-terminal-wrapper');
    if (!drawer) return;
    const isOpen = drawer.classList.contains('open');
    if (isOpen) {
      drawer.classList.remove('open');
    } else {
      drawer.classList.add('open');
      const input = document.getElementById('terminal-interactive-input');
      if (input) setTimeout(() => input.focus(), 150);
      renderAllLogs();
    }
  }

  function minimizeDrawer() {
    const term = document.getElementById('light-terminal');
    if (!term) return;
    isMinimized = !isMinimized;
    term.classList.toggle('minimized', isMinimized);
  }

  function expandDrawer() {
    const term = document.getElementById('light-terminal');
    if (!term) return;
    isExpanded = !isExpanded;
    term.classList.toggle('expanded', isExpanded);
  }

  /* Global Transparent Fetch Interceptor */
  function setupFetchInterceptor() {
    if (window._brainFetchHooked) return;
    window._brainFetchHooked = true;

    const _nativeFetch = window.fetch;
    window.fetch = async function (...args) {
      const url = typeof args[0] === 'string' ? args[0] : (args[0] && args[0].url ? args[0].url : 'unknown');
      const options = args[1] || {};
      const method = (options.method || 'GET').toUpperCase();
      const startTime = performance.now();
      const timestamp = new Date();
      const id = 'http-' + Date.now() + '-' + Math.random().toString(36).substr(2, 5);

      let requestPayload = null;
      if (options.body) {
        try {
          requestPayload = typeof options.body === 'string' ? JSON.parse(options.body) : options.body;
        } catch (e) {
          requestPayload = options.body;
        }
      }

      try {
        const response = await _nativeFetch.apply(this, args);
        const duration = Math.round(performance.now() - startTime);

        let responseSnippet = null;
        try {
          const clone = response.clone();
          const text = await clone.text();
          try {
            responseSnippet = JSON.parse(text);
          } catch (e) {
            responseSnippet = text.slice(0, 300);
          }
        } catch (e) {
          // ignore clone error
        }

        logHttp({
          id: id,
          timestamp: timestamp,
          method: method,
          url: url,
          statusCode: response.status,
          statusText: response.statusText || (response.ok ? 'OK' : 'Error'),
          durationMs: duration,
          payload: requestPayload,
          responseSnippet: responseSnippet
        });

        return response;
      } catch (error) {
        const duration = Math.round(performance.now() - startTime);
        logHttp({
          id: id,
          timestamp: timestamp,
          method: method,
          url: url,
          statusCode: 0,
          statusText: 'FAILED: ' + error.message,
          durationMs: duration,
          payload: requestPayload,
          responseSnippet: { error: error.message }
        });
        throw error;
      }
    };
  }

  function setupEventListeners() {
    // Mini bar input (executes commands directly from normal screen)
    const miniInput = document.getElementById('terminal-mini-input');
    if (miniInput) {
      miniInput.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
          const val = miniInput.value.trim();
          if (!val) return;
          miniInput.value = '';

          const parts = val.split(/\s+/);
          const cmd = parts[0].toLowerCase();

          // Commands with multiline tabular/detailed output open the console drawer
          if (['help', 'stats', 'status', 'path', 'links', 'edges', 'node', 'tensions', 'firmware', 'resurface'].includes(cmd)) {
            toggleDrawer();
            setTab('cli');
            setTimeout(() => executeCommand(val), 100);
          } else {
            // Instant execution (search, ping, view, filter, clear, export)
            executeCommand(val);
          }
        }
      });
    }

    // Full terminal interactive input
    const mainInput = document.getElementById('terminal-interactive-input');
    if (mainInput) {
      mainInput.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
          const val = mainInput.value;
          mainInput.value = '';
          executeCommand(val);
        } else if (e.key === 'ArrowUp') {
          if (commandHistory.length > 0 && historyIndex > 0) {
            historyIndex--;
            mainInput.value = commandHistory[historyIndex] || '';
          }
        } else if (e.key === 'ArrowDown') {
          if (historyIndex < commandHistory.length - 1) {
            historyIndex++;
            mainInput.value = commandHistory[historyIndex] || '';
          } else {
            historyIndex = commandHistory.length;
            mainInput.value = '';
          }
        } else if (e.key === 'Tab') {
          e.preventDefault();
          const current = mainInput.value.trim().toLowerCase();
          if (current) {
            const match = COMMANDS.find(c => c.startsWith(current));
            if (match) mainInput.value = match + ' ';
          }
        }
      });
    }

    // Keyboard shortcut to toggle terminal (Cmd + ` or Ctrl + `)
    window.addEventListener('keydown', e => {
      if ((e.metaKey || e.ctrlKey) && (e.key === '`' || e.key === 'ù' || e.key === '~')) {
        e.preventDefault();
        toggleDrawer();
      } else if (e.key === 'Escape') {
        const drawer = document.getElementById('light-terminal-wrapper');
        if (drawer && drawer.classList.contains('open')) {
          drawer.classList.remove('open');
        }
      }
    });
  }

  function init() {
    setupFetchInterceptor();
    setupEventListeners();
    log('info', 'SYS', 'Universal AI Brain CLI Engine inizializzato. Digita <strong style="color:#00d2ff;">help</strong> per la lista comandi.');
  }

  return {
    init,
    log,
    logHttp,
    logNode,
    executeCommand,
    toggleDrawer,
    minimizeDrawer,
    expandDrawer,
    clearLogs,
    setTab,
    toggleDetail,
    setFilter: f => { setTab(f); },
    inspectFromCli: id => { execInspectNode(id); },
    inspectLinks: id => { execLinks(id); },
    focusGraphNode: id => {
      if (typeof window.selectNodeInGraph === 'function') window.selectNodeInGraph(id);
      toggleDrawer();
    }
  };
})();
