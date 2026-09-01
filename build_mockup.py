import os, json, sqlite3
import brain_vectors

DB_PATH = 'brain.db'
OUTPUT_HTML = 'mockup_embedding_projector.html'

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('SELECT id, label, hemisphere, primary_label, category, tags, summary, layer_level FROM nodes')

vec_engine = brain_vectors.LightweightDenseVectorizer(dim=32)
nodes = []

for row in c.fetchall():
    nid, label, hemi, prim, cat, tags_str, summ, layer = row
    corpus = f"{label} {summ or ''} {cat or ''} {prim or ''}"
    vec = vec_engine.embed(corpus)
    try:
        tags = json.loads(tags_str) if tags_str else []
    except:
        tags = []
    nodes.append({
        'id': nid,
        'label': label or nid,
        'hemisphere': hemi if hemi in ['LEFT', 'RIGHT'] else 'LEFT',
        'primary_label': prim or 'NODE',
        'category': cat or 'General',
        'tags': tags,
        'summary': summ or 'Nessun sommario disponibile.',
        'layer_level': int(layer) if layer is not None else 1,
        'vector': [round(float(v), 4) for v in vec]
    })

c.execute('SELECT source, target, relation FROM edges')
edges = [{'source': r[0], 'target': r[1], 'relation': r[2] or 'RELATES_TO'} for r in c.fetchall()]
conn.close()

data_json = json.dumps({'nodes': nodes, 'edges': edges}, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>Universal AI Brain - 3D Cognitive Embedding Projector</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/tween.js/18.6.4/tween.umd.js"></script>
  <style>
    :root {{
      --bg-dark: #07080c;
      --bg-panel: rgba(14, 17, 24, 0.86);
      --border-glow: rgba(0, 210, 255, 0.25);
      --border-subtle: rgba(255, 255, 255, 0.09);
      --cyan-left: #00d2ff;
      --magenta-right: #ff007f;
      --gold-domain: #ffd15c;
      --purple-callosum: #a855f7;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      background: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Inter', -apple-system, sans-serif;
      overflow: hidden;
      width: 100vw;
      height: 100vh;
      user-select: none;
    }}

    /* Master Topbar */
    .topbar {{
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 52px;
      background: rgba(8, 10, 15, 0.92);
      backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 1000;
    }}
    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .brand-icon {{
      font-size: 20px;
      filter: drop-shadow(0 0 8px rgba(0,210,255,0.6));
    }}
    .brand-title {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      color: #fff;
    }}
    .brand-sub {{
      font-size: 11px;
      color: var(--text-dim);
      margin-left: 4px;
    }}
    .badge {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(0, 210, 255, 0.12);
      color: var(--cyan-left);
      border: 1px solid rgba(0, 210, 255, 0.3);
    }}

    .hud-metrics {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .metric-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      border-radius: 6px;
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border-subtle);
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
    }}
    .dot {{ width: 7px; height: 7px; border-radius: 50%; }}
    .dot-cyan {{ background: var(--cyan-left); box-shadow: 0 0 8px var(--cyan-left); }}
    .dot-magenta {{ background: var(--magenta-right); box-shadow: 0 0 8px var(--magenta-right); }}
    .dot-gold {{ background: var(--gold-domain); box-shadow: 0 0 8px var(--gold-domain); }}

    /* Canvas Viewport */
    #viewport-container {{
      width: 100vw;
      height: 100vh;
      position: absolute;
      top: 0; left: 0;
    }}

    /* Left Control Sidebar */
    .projector-controls {{
      position: absolute;
      top: 68px;
      left: 20px;
      width: 320px;
      max-height: calc(100vh - 88px);
      background: var(--bg-panel);
      backdrop-filter: blur(24px);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      z-index: 900;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
      overflow-y: auto;
    }}
    .panel-section-title {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}

    /* Algorithm Picker Tabs */
    .algo-tabs {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 4px;
      background: rgba(0,0,0,0.4);
      padding: 3px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
    }}
    .algo-btn {{
      background: transparent;
      border: none;
      color: var(--text-dim);
      padding: 6px 0;
      font-family: 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 600;
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.15s ease;
      text-align: center;
    }}
    .algo-btn:hover {{ color: #fff; }}
    .algo-btn.active {{
      background: rgba(0, 210, 255, 0.18);
      color: var(--cyan-left);
      border: 1px solid rgba(0, 210, 255, 0.35);
      box-shadow: 0 0 10px rgba(0,210,255,0.2);
    }}

    /* Dimension Switch (3D vs 2D) */
    .dim-switch-wrap {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
    }}
    .dim-btn {{
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 7px;
      font-size: 11px;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.15s;
    }}
    .dim-btn:hover {{ border-color: rgba(255,255,255,0.2); color: #fff; }}
    .dim-btn.active {{
      background: rgba(168, 85, 247, 0.16);
      border-color: var(--purple-callosum);
      color: #fff;
    }}

    /* t-SNE Live Simulation Box */
    .tsne-box {{
      background: rgba(0,0,0,0.3);
      border: 1px solid rgba(0,210,255,0.15);
      border-radius: 8px;
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .tsne-status-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
    }}
    .tsne-actions {{
      display: flex;
      gap: 6px;
    }}
    .btn-action {{
      flex: 1;
      background: rgba(0, 210, 255, 0.14);
      border: 1px solid rgba(0, 210, 255, 0.3);
      color: var(--cyan-left);
      padding: 6px 8px;
      font-size: 11px;
      font-weight: 600;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
    }}
    .btn-action:hover {{ background: rgba(0, 210, 255, 0.25); }}
    .btn-action.btn-pause {{
      background: rgba(255, 0, 127, 0.14);
      border-color: rgba(255, 0, 127, 0.35);
      color: var(--magenta-right);
    }}

    /* Sliders */
    .slider-row {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}
    .slider-header {{
      display: flex;
      justify-content: space-between;
      font-size: 10px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-dim);
    }}
    input[type="range"] {{
      -webkit-appearance: none;
      width: 100%;
      height: 4px;
      background: rgba(255,255,255,0.1);
      border-radius: 2px;
      outline: none;
    }}
    input[type="range"]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--cyan-left);
      cursor: pointer;
      box-shadow: 0 0 6px var(--cyan-left);
    }}

    /* Search Box */
    .search-box {{
      position: relative;
    }}
    .search-input {{
      width: 100%;
      background: rgba(0,0,0,0.5);
      border: 1px solid var(--border-subtle);
      padding: 8px 10px 8px 30px;
      border-radius: 8px;
      color: #fff;
      font-size: 12px;
      font-family: 'Inter', sans-serif;
      outline: none;
      transition: all 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--cyan-left);
      box-shadow: 0 0 12px rgba(0,210,255,0.25);
    }}
    .search-icon {{
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 12px;
      color: var(--text-dim);
    }}

    /* Right Node Inspector */
    .node-inspector {{
      position: absolute;
      top: 68px;
      right: 20px;
      width: 360px;
      max-height: calc(100vh - 88px);
      background: var(--bg-panel);
      backdrop-filter: blur(24px);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 18px;
      display: none;
      flex-direction: column;
      gap: 14px;
      z-index: 900;
      box-shadow: -10px 20px 40px rgba(0,0,0,0.6);
      overflow-y: auto;
    }}
    .inspector-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 10px;
    }}
    .node-title {{
      font-size: 14px;
      font-weight: 700;
      color: #fff;
      line-height: 1.3;
    }}
    .node-hemi-tag {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 9px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
    }}
    .hemi-left {{ background: rgba(0,210,255,0.15); color: var(--cyan-left); border: 1px solid rgba(0,210,255,0.3); }}
    .hemi-right {{ background: rgba(255,0,127,0.15); color: var(--magenta-right); border: 1px solid rgba(255,0,127,0.3); }}
    .node-summary {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.5;
      background: rgba(0,0,0,0.25);
      padding: 10px;
      border-radius: 6px;
      border-left: 2px solid var(--cyan-left);
    }}
    .knn-list {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .knn-item {{
      background: rgba(255,255,255,0.03);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 6px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .knn-item:hover {{
      background: rgba(0, 210, 255, 0.1);
      border-color: rgba(0, 210, 255, 0.3);
    }}
    .knn-name {{ font-size: 11px; color: #fff; max-width: 220px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .knn-sim {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; color: var(--cyan-left); }}

    /* Filter Chips */
    .filter-chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }}
    .chip {{
      font-size: 10px;
      padding: 3px 8px;
      border-radius: 20px;
      background: rgba(255,255,255,0.04);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.15s;
    }}
    .chip:hover, .chip.active {{
      background: rgba(255,255,255,0.12);
      color: #fff;
      border-color: rgba(255,255,255,0.3);
    }}

    /* Tooltip */
    #tooltip {{
      position: absolute;
      display: none;
      pointer-events: none;
      background: rgba(10, 13, 20, 0.94);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-glow);
      padding: 6px 12px;
      border-radius: 6px;
      font-family: 'Inter', sans-serif;
      font-size: 11px;
      color: #fff;
      z-index: 2000;
      box-shadow: 0 8px 24px rgba(0,0,0,0.8);
      max-width: 260px;
    }}
    
    .hud-crosshair {{
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      width: 16px; height: 16px;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 50%;
      pointer-events: none;
    }}
  </style>
</head>
<body>

  <!-- Master Topbar -->
  <header class="topbar">
    <div class="brand-wrap">
      <span class="brand-icon">🧠</span>
      <div>
        <span class="brand-title">UNIVERSAL AI BRAIN</span>
        <span class="brand-sub">Bi-Hemispheric Embedding Projector</span>
      </div>
      <span class="badge">TensorFlow Projector Architecture</span>
    </div>

    <div class="hud-metrics">
      <div class="metric-pill" title="Emisfero Sinistro: Logica, Architettura, Codice">
        <span class="dot dot-cyan"></span>
        <span>SX (Tech): <strong id="count-left">0</strong></span>
      </div>
      <div class="metric-pill" title="Emisfero Destro: Visione, Emozioni, Episodi">
        <span class="dot dot-magenta"></span>
        <span>DX (Creative): <strong id="count-right">0</strong></span>
      </div>
      <div class="metric-pill" title="Macro Domini di Livello 0">
        <span class="dot dot-gold"></span>
        <span>Domini L0: <strong id="count-domains">0</strong></span>
      </div>
    </div>
  </header>

  <!-- 3D WebGL Canvas Container -->
  <div id="viewport-container"></div>
  <div class="hud-crosshair"></div>
  <div id="tooltip"></div>

  <!-- Left Control Sidebar -->
  <div class="projector-controls">
    
    <!-- Search Box -->
    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="search-input" class="search-input" placeholder="Cerca concetto o memoria (es. 'CareTrack', 'Telegram', 'SQLite')...">
    </div>

    <!-- Dimension View Switcher -->
    <div>
      <div class="panel-section-title">Visualizzazione Spaziale</div>
      <div class="dim-switch-wrap">
        <button class="dim-btn active" id="btn-view-3d" onclick="switchDimension('3D')">
          <span>🌐</span> 3D Volumetrico
        </button>
        <button class="dim-btn" id="btn-view-2d" onclick="switchDimension('2D')">
          <span>🗺️</span> 2D Planare
        </button>
      </div>
    </div>

    <!-- Projection Algorithm -->
    <div>
      <div class="panel-section-title">
        <span>Algoritmo di Riduzione</span>
        <span id="algo-tag" style="color:var(--cyan-left);">t-SNE</span>
      </div>
      <div class="algo-tabs">
        <button class="algo-btn active" id="tab-tsne" onclick="setAlgorithm('tsne')">t-SNE</button>
        <button class="algo-btn" id="tab-umap" onclick="setAlgorithm('umap')">UMAP</button>
        <button class="algo-btn" id="tab-pca" onclick="setAlgorithm('pca')">PCA</button>
        <button class="algo-btn" id="tab-bipolar" onclick="setAlgorithm('bipolar')">Bi-Polar</button>
      </div>
    </div>

    <!-- t-SNE Live Simulation Box -->
    <div class="tsne-box" id="tsne-controls">
      <div class="tsne-status-row">
        <span style="color:var(--text-muted);">Iterazione (Epoch):</span>
        <strong id="tsne-step-counter" style="color:var(--cyan-left);">0</strong>
      </div>
      <div class="tsne-actions">
        <button class="btn-action" id="btn-tsne-toggle" onclick="toggleTsneSimulation()">
          <span id="tsne-play-icon">▶</span> <span id="tsne-play-text">Esegui Iterazione</span>
        </button>
        <button class="btn-action" style="flex:0.6; background:rgba(255,255,255,0.06); border-color:var(--border-subtle); color:var(--text-muted);" onclick="resetTsneSimulation()">
          <span>↺</span> Reset
        </button>
      </div>
      <div class="slider-row" style="margin-top:4px;">
        <div class="slider-header">
          <span>Perplessità (Perplexity)</span>
          <span id="perp-val">18</span>
        </div>
        <input type="range" id="slider-perp" min="5" max="50" value="18" oninput="updatePerplexity(this.value)">
      </div>
      <div class="slider-row">
        <div class="slider-header">
          <span>Learning Rate (Passo)</span>
          <span id="lr-val">120</span>
        </div>
        <input type="range" id="slider-lr" min="10" max="300" value="120" oninput="updateLearningRate(this.value)">
      </div>
    </div>

    <!-- Synaptic Overlays -->
    <div>
      <div class="panel-section-title">Sinapsi e Relazioni</div>
      <div class="slider-row">
        <div class="slider-header">
          <span>k-Nearest Neighbors (k-NN)</span>
          <span id="knn-val">6</span>
        </div>
        <input type="range" id="slider-knn" min="0" max="15" value="6" oninput="updateKnn(this.value)">
      </div>
      <div style="margin-top:8px; display:flex; gap:6px;">
        <button class="dim-btn active" id="btn-toggle-graph-edges" style="flex:1;" onclick="toggleGraphEdges()">
          <span>🕸️</span> Archi Grafo
        </button>
        <button class="dim-btn active" id="btn-toggle-labels" style="flex:1;" onclick="toggleLabels()">
          <span>🏷️</span> Etichette
        </button>
      </div>
    </div>

    <!-- Hemisphere & Domain Filters -->
    <div>
      <div class="panel-section-title">Filtri Emisferici</div>
      <div class="filter-chips">
        <span class="chip active" onclick="filterHemisphere('ALL', this)">Tutti (585)</span>
        <span class="chip" onclick="filterHemisphere('LEFT', this)">Sinistro (Tech)</span>
        <span class="chip" onclick="filterHemisphere('RIGHT', this)">Destro (Vision)</span>
        <span class="chip" onclick="filterHemisphere('L0', this)">Domini L0</span>
      </div>
    </div>

  </div>

  <!-- Right Node Inspector -->
  <div class="node-inspector" id="node-inspector">
    <div class="inspector-header">
      <div>
        <div class="node-title" id="insp-title">Titolo Concetto</div>
        <div style="font-size:11px; font-family:'JetBrains Mono', monospace; color:var(--text-dim); margin-top:2px;" id="insp-id">id-del-nodo</div>
      </div>
      <span class="node-hemi-tag hemi-left" id="insp-hemi">LEFT</span>
    </div>

    <div>
      <div class="panel-section-title">Sommario Cognitivo</div>
      <div class="node-summary" id="insp-summary">Descrizione del concetto...</div>
    </div>

    <div>
      <div class="panel-section-title">
        <span>Vicini Semantici Più Prossimi (k-NN)</span>
        <span style="color:var(--cyan-left);">Cos-Sim</span>
      </div>
      <div class="knn-list" id="insp-knn-list">
        <!-- Dinamico -->
      </div>
    </div>

    <div>
      <div class="panel-section-title">Archi Strutturali Connessi</div>
      <div class="knn-list" id="insp-edges-list">
        <!-- Dinamico -->
      </div>
    </div>

    <div style="display:flex; gap:6px; margin-top:4px;">
      <button class="btn-action" onclick="focusCameraOnSelected()">
        <span>🎯</span> Centra Camera
      </button>
      <button class="btn-action" style="background:rgba(255,255,255,0.06); border-color:var(--border-subtle); color:var(--text-muted);" onclick="closeInspector()">
        <span>✕</span> Chiudi
      </button>
    </div>
  </div>

  <script>
    const RAW_DATA = {data_json};
    const nodes = RAW_DATA.nodes;
    const edges = RAW_DATA.edges;

    let leftCount = 0, rightCount = 0, domainCount = 0;
    nodes.forEach(n => {{
      if (n.layer_level === 0) domainCount++;
      if (n.hemisphere === 'LEFT') leftCount++;
      else rightCount++;
    }});
    document.getElementById('count-left').innerText = leftCount;
    document.getElementById('count-right').innerText = rightCount;
    document.getElementById('count-domains').innerText = domainCount;

    let scene, camera, renderer, controls;
    let pointCloudMesh, linesMesh, knnLinesMesh, labelSpritesGroup;
    let is3D = true;
    let currentAlgorithm = 'tsne';
    let isTsneRunning = false;
    let tsneStep = 0;
    let perplexity = 18;
    let learningRate = 120;
    let knnCount = 6;
    let showGraphEdges = true;
    let showLabels = true;
    let activeFilter = 'ALL';
    let selectedNode = null;
    let hoveredNode = null;

    const positions = {{
      tsne: new Float32Array(nodes.length * 3),
      umap: new Float32Array(nodes.length * 3),
      pca: new Float32Array(nodes.length * 3),
      bipolar: new Float32Array(nodes.length * 3),
      current: new Float32Array(nodes.length * 3),
      target: new Float32Array(nodes.length * 3)
    }};

    function initProjections() {{
      const N = nodes.length;

      // 1. Bi-Polar Projection
      nodes.forEach((n, i) => {{
        const isLeft = n.hemisphere === 'LEFT';
        const isL0 = n.layer_level === 0;
        let x = (isLeft ? -1 : 1) * (90 + Math.random() * 160);
        if (isL0) x = (Math.random() - 0.5) * 60;
        let y = 140 - (n.layer_level * 90) + (Math.random() - 0.5) * 40;
        let z = ((n.vector[0] || 0) * 180) + (Math.random() - 0.5) * 80;

        positions.bipolar[i * 3] = x;
        positions.bipolar[i * 3 + 1] = y;
        positions.bipolar[i * 3 + 2] = z;
      }});

      // 2. PCA
      nodes.forEach((n, i) => {{
        let pc1 = 0, pc2 = 0, pc3 = 0;
        for (let d = 0; d < 32; d++) {{
          const v = n.vector[d] || 0;
          pc1 += v * Math.sin(d * 1.3);
          pc2 += v * Math.cos(d * 0.9);
          pc3 += v * Math.sin(d * 2.1 + 0.4);
        }}
        positions.pca[i * 3] = pc1 * 260;
        positions.pca[i * 3 + 1] = pc2 * 240;
        positions.pca[i * 3 + 2] = pc3 * 220;
      }});

      // 3. UMAP-like Clusters
      nodes.forEach((n, i) => {{
        const clusterId = (n.category.charCodeAt(0) * 7 + n.primary_label.charCodeAt(0)) % 8;
        const angle = (clusterId / 8) * Math.PI * 2;
        const clusterCenterX = Math.cos(angle) * 180;
        const clusterCenterZ = Math.sin(angle) * 180;
        const clusterCenterY = (n.layer_level === 0 ? 80 : -20) + (Math.random() - 0.5) * 50;

        positions.umap[i * 3] = clusterCenterX + (Math.random() - 0.5) * 80;
        positions.umap[i * 3 + 1] = clusterCenterY + (Math.random() - 0.5) * 70;
        positions.umap[i * 3 + 2] = clusterCenterZ + (Math.random() - 0.5) * 80;
      }});

      // 4. Initial t-SNE Random Cloud
      for (let i = 0; i < N * 3; i++) {{
        positions.tsne[i] = (Math.random() - 0.5) * 220;
        positions.current[i] = positions.tsne[i];
        positions.target[i] = positions.tsne[i];
      }}
    }}

    function initThree() {{
      const container = document.getElementById('viewport-container');
      const width = window.innerWidth;
      const height = window.innerHeight;

      scene = new THREE.Scene();
      scene.fog = new THREE.FogExp2(0x07080c, 0.0012);

      camera = new THREE.PerspectiveCamera(50, width / height, 1, 3000);
      camera.position.set(0, 60, 480);

      renderer = new THREE.WebGLRenderer({{ antialias: true, alpha: true }});
      renderer.setSize(width, height);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      container.appendChild(renderer.domElement);

      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.06;
      controls.rotateSpeed = 0.8;
      controls.zoomSpeed = 1.0;
      controls.maxDistance = 1400;
      controls.minDistance = 30;

      const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
      scene.add(ambientLight);

      const dirLight = new THREE.DirectionalLight(0x00d2ff, 0.5);
      dirLight.position.set(200, 300, 200);
      scene.add(dirLight);

      createPointCloud();
      createGraphLines();
      createKnnLines();
      createLabels();

      window.addEventListener('resize', onWindowResize);
      setupRaycasting();
      
      animate();
    }}

    function createPointCloud() {{
      const N = nodes.length;
      const geometry = new THREE.BufferGeometry();
      geometry.setAttribute('position', new THREE.BufferAttribute(positions.current, 3));

      const colors = new Float32Array(N * 3);
      const sizes = new Float32Array(N);

      nodes.forEach((n, i) => {{
        const isLeft = n.hemisphere === 'LEFT';
        const isL0 = n.layer_level === 0;

        let color = isLeft ? new THREE.Color(0x00d2ff) : new THREE.Color(0xff007f);
        if (isL0) color = new THREE.Color(0xffd15c);

        colors[i * 3] = color.r;
        colors[i * 3 + 1] = color.g;
        colors[i * 3 + 2] = color.b;

        sizes[i] = isL0 ? 14.0 : (n.layer_level === 1 ? 8.5 : 5.5);
      }});

      geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
      geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));

      const material = new THREE.PointsMaterial({{
        size: 9.0,
        vertexColors: true,
        transparent: true,
        opacity: 0.9,
        sizeAttenuation: true
      }});

      pointCloudMesh = new THREE.Points(geometry, material);
      scene.add(pointCloudMesh);
    }}

    function createGraphLines() {{
      const linePositions = [];
      const lineColors = [];

      const nodeIndexMap = new Map();
      nodes.forEach((n, i) => nodeIndexMap.set(n.id, i));

      edges.forEach(e => {{
        const sIdx = nodeIndexMap.get(e.source);
        const tIdx = nodeIndexMap.get(e.target);

        if (sIdx !== undefined && tIdx !== undefined) {{
          linePositions.push(
            positions.current[sIdx * 3], positions.current[sIdx * 3 + 1], positions.current[sIdx * 3 + 2],
            positions.current[tIdx * 3], positions.current[tIdx * 3 + 1], positions.current[tIdx * 3 + 2]
          );

          const isCross = nodes[sIdx].hemisphere !== nodes[tIdx].hemisphere;
          const col = isCross ? new THREE.Color(0xa855f7) : new THREE.Color(0x00d2ff);
          lineColors.push(col.r, col.g, col.b, col.r, col.g, col.b);
        }}
      }});

      const lineGeo = new THREE.BufferGeometry();
      lineGeo.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
      lineGeo.setAttribute('color', new THREE.Float32BufferAttribute(lineColors, 3));

      const lineMat = new THREE.LineBasicMaterial({{
        vertexColors: true,
        transparent: true,
        opacity: 0.18,
        linewidth: 1
      }});

      linesMesh = new THREE.LineSegments(lineGeo, lineMat);
      linesMesh.userData = {{ nodeIndexMap }};
      scene.add(linesMesh);
    }}

    function createKnnLines() {{
      const knnGeo = new THREE.BufferGeometry();
      knnGeo.setAttribute('position', new THREE.Float32BufferAttribute([], 3));
      const knnMat = new THREE.LineBasicMaterial({{
        color: 0x00d2ff,
        transparent: true,
        opacity: 0.8,
        linewidth: 2
      }});
      knnLinesMesh = new THREE.LineSegments(knnGeo, knnMat);
      scene.add(knnLinesMesh);
    }}

    function createLabels() {{
      labelSpritesGroup = new THREE.Group();
      scene.add(labelSpritesGroup);
      updateLabels();
    }}

    function updateLabels() {{
      while (labelSpritesGroup.children.length > 0) {{
        labelSpritesGroup.remove(labelSpritesGroup.children[0]);
      }}
      if (!showLabels) return;

      nodes.forEach((n, i) => {{
        if (n.layer_level === 0 || i % 14 === 0) {{
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          canvas.width = 256;
          canvas.height = 64;

          ctx.fillStyle = 'rgba(8,10,15,0.75)';
          ctx.strokeStyle = n.hemisphere === 'LEFT' ? '#00d2ff' : '#ff007f';
          ctx.lineWidth = 2;
          ctx.beginPath();
          if (ctx.roundRect) ctx.roundRect(4, 4, 248, 56, 8);
          else ctx.rect(4, 4, 248, 56);
          ctx.fill();
          ctx.stroke();

          ctx.font = 'bold 20px "JetBrains Mono", monospace';
          ctx.fillStyle = '#ffffff';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          const truncated = n.label.length > 18 ? n.label.substring(0, 16) + '...' : n.label;
          ctx.fillText(truncated, 128, 32);

          const texture = new THREE.CanvasTexture(canvas);
          const spriteMat = new THREE.SpriteMaterial({{ map: texture, transparent: true, opacity: 0.85 }});
          const sprite = new THREE.Sprite(spriteMat);
          sprite.scale.set(30, 8, 1);
          sprite.position.set(positions.current[i * 3], positions.current[i * 3 + 1] + 8, positions.current[i * 3 + 2]);
          sprite.userData = {{ nodeIndex: i }};
          labelSpritesGroup.add(sprite);
        }}
      }});
    }}

    function setAlgorithm(algo) {{
      currentAlgorithm = algo;
      document.querySelectorAll('.algo-btn').forEach(b => b.classList.remove('active'));
      document.getElementById('tab-' + algo).classList.add('active');
      document.getElementById('algo-tag').innerText = algo.toUpperCase();

      const tsneControls = document.getElementById('tsne-controls');
      tsneControls.style.display = algo === 'tsne' ? 'flex' : 'none';

      const source = positions[algo];
      if (source) {{
        for (let i = 0; i < nodes.length * 3; i++) {{
          let val = source[i];
          if (!is3D && i % 3 === 2) val = 0;
          new TWEEN.Tween(positions.current)
            .to({{ [i]: val }}, 800)
            .easing(TWEEN.Easing.Cubic.Out)
            .start();
        }}
      }}
    }}

    function switchDimension(dim) {{
      is3D = (dim === '3D');
      document.getElementById('btn-view-3d').classList.toggle('active', is3D);
      document.getElementById('btn-view-2d').classList.toggle('active', !is3D);

      const source = positions[currentAlgorithm];
      for (let i = 0; i < nodes.length; i++) {{
        const targetZ = is3D ? source[i * 3 + 2] : 0;
        new TWEEN.Tween(positions.current)
          .to({{ [i * 3 + 2]: targetZ }}, 700)
          .easing(TWEEN.Easing.Quadratic.Out)
          .start();
      }}

      if (!is3D) {{
        new TWEEN.Tween(camera.position).to({{ x: 0, y: 0, z: 500 }}, 700).start();
        new TWEEN.Tween(camera.rotation).to({{ x: 0, y: 0, z: 0 }}, 700).start();
      }}
    }}

    function toggleTsneSimulation() {{
      isTsneRunning = !isTsneRunning;
      const btn = document.getElementById('btn-tsne-toggle');
      document.getElementById('tsne-play-icon').innerText = isTsneRunning ? '⏸' : '▶';
      document.getElementById('tsne-play-text').innerText = isTsneRunning ? 'Pausa' : 'Esegui Iterazione';
      btn.classList.toggle('btn-pause', isTsneRunning);
    }}

    function resetTsneSimulation() {{
      isTsneRunning = false;
      tsneStep = 0;
      document.getElementById('tsne-step-counter').innerText = '0';
      document.getElementById('tsne-play-icon').innerText = '▶';
      document.getElementById('tsne-play-text').innerText = 'Esegui Iterazione';
      document.getElementById('btn-tsne-toggle').classList.remove('btn-pause');

      for (let i = 0; i < nodes.length * 3; i++) {{
        positions.tsne[i] = (Math.random() - 0.5) * 220;
        positions.current[i] = positions.tsne[i];
      }}
      pointCloudMesh.geometry.attributes.position.needsUpdate = true;
      syncLinesAndLabels();
    }}

    function stepTsne() {{
      tsneStep++;
      document.getElementById('tsne-step-counter').innerText = tsneStep;

      const N = nodes.length;
      const stepSize = (learningRate / 100) * 0.45;

      for (let i = 0; i < N; i++) {{
        let fx = 0, fy = 0, fz = 0;
        const px = positions.current[i * 3];
        const py = positions.current[i * 3 + 1];
        const pz = is3D ? positions.current[i * 3 + 2] : 0;
        const hemiI = nodes[i].hemisphere;

        for (let j = (i + 1) % 15; j < N; j += 12) {{
          if (i === j) continue;
          const qx = positions.current[j * 3];
          const qy = positions.current[j * 3 + 1];
          const qz = is3D ? positions.current[j * 3 + 2] : 0;

          const dx = px - qx;
          const dy = py - qy;
          const dz = pz - qz;
          const distSq = dx * dx + dy * dy + dz * dz + 1.0;
          const dist = Math.sqrt(distSq);

          const sim = cosineSim(nodes[i].vector, nodes[j].vector);
          const sameHemi = hemiI === nodes[j].hemisphere;

          const attr = (sim * 2.5 + (sameHemi ? 0.8 : -0.5)) / (dist + 0.1);
          const rep = (perplexity * 4.0) / (distSq + 10.0);

          const force = (rep - attr) * stepSize;
          fx += (dx / dist) * force;
          fy += (dy / dist) * force;
          fz += (dz / dist) * force;
        }}

        positions.current[i * 3] += fx;
        positions.current[i * 3 + 1] += fy;
        if (is3D) positions.current[i * 3 + 2] += fz;
      }}

      pointCloudMesh.geometry.attributes.position.needsUpdate = true;
      syncLinesAndLabels();
    }}

    function cosineSim(v1, v2) {{
      let dot = 0, n1 = 0, n2 = 0;
      for (let i = 0; i < v1.length; i++) {{
        dot += v1[i] * v2[i];
        n1 += v1[i] * v1[i];
        n2 += v2[i] * v2[i];
      }}
      if (n1 === 0 || n2 === 0) return 0;
      return dot / (Math.sqrt(n1) * Math.sqrt(n2));
    }}

    function updatePerplexity(v) {{
      perplexity = parseInt(v);
      document.getElementById('perp-val').innerText = v;
    }}
    function updateLearningRate(v) {{
      learningRate = parseInt(v);
      document.getElementById('lr-val').innerText = v;
    }}
    function updateKnn(v) {{
      knnCount = parseInt(v);
      document.getElementById('knn-val').innerText = v;
      if (selectedNode) selectNode(selectedNode);
    }}

    function toggleGraphEdges() {{
      showGraphEdges = !showGraphEdges;
      document.getElementById('btn-toggle-graph-edges').classList.toggle('active', showGraphEdges);
      linesMesh.visible = showGraphEdges;
    }}

    function toggleLabels() {{
      showLabels = !showLabels;
      document.getElementById('btn-toggle-labels').classList.toggle('active', showLabels);
      labelSpritesGroup.visible = showLabels;
      if (showLabels) updateLabels();
    }}

    function filterHemisphere(hemi, btn) {{
      activeFilter = hemi;
      document.querySelectorAll('.filter-chips .chip').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');

      const colors = pointCloudMesh.geometry.attributes.color.array;
      const sizes = pointCloudMesh.geometry.attributes.size.array;

      nodes.forEach((n, i) => {{
        let visible = true;
        if (hemi === 'LEFT' && n.hemisphere !== 'LEFT') visible = false;
        if (hemi === 'RIGHT' && n.hemisphere !== 'RIGHT') visible = false;
        if (hemi === 'L0' && n.layer_level !== 0) visible = false;

        const isLeft = n.hemisphere === 'LEFT';
        const isL0 = n.layer_level === 0;
        let baseColor = isLeft ? new THREE.Color(0x00d2ff) : new THREE.Color(0xff007f);
        if (isL0) baseColor = new THREE.Color(0xffd15c);

        if (visible) {{
          colors[i * 3] = baseColor.r;
          colors[i * 3 + 1] = baseColor.g;
          colors[i * 3 + 2] = baseColor.b;
          sizes[i] = isL0 ? 14.0 : 7.0;
        }} else {{
          colors[i * 3] = 0.15;
          colors[i * 3 + 1] = 0.18;
          colors[i * 3 + 2] = 0.22;
          sizes[i] = 2.0;
        }}
      }});

      pointCloudMesh.geometry.attributes.color.needsUpdate = true;
      pointCloudMesh.geometry.attributes.size.needsUpdate = true;
    }}

    function setupRaycasting() {{
      const raycaster = new THREE.Raycaster();
      raycaster.params.Points.threshold = 8;
      const mouse = new THREE.Vector2(-999, -999);
      const tooltip = document.getElementById('tooltip');

      window.addEventListener('mousemove', (e) => {{
        mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;

        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObject(pointCloudMesh);

        if (intersects.length > 0) {{
          const idx = intersects[0].index;
          const node = nodes[idx];
          hoveredNode = node;
          document.body.style.cursor = 'pointer';

          tooltip.style.display = 'block';
          tooltip.style.left = (e.clientX + 14) + 'px';
          tooltip.style.top = (e.clientY + 14) + 'px';
          tooltip.innerHTML = `
            <div style="font-weight:700; color:${{node.hemisphere === 'LEFT' ? '#00d2ff' : '#ff007f'}}">${{node.label}}</div>
            <div style="color:#94a3b8; font-size:10px; margin-top:2px;">[${{node.hemisphere}}] L${{node.layer_level}} &bull; ${{node.category}}</div>
          `;
        }} else {{
          hoveredNode = null;
          document.body.style.cursor = 'default';
          tooltip.style.display = 'none';
        }}
      }});

      window.addEventListener('click', () => {{
        if (hoveredNode) {{
          selectNode(hoveredNode);
        }}
      }});
    }}

    function selectNode(node) {{
      selectedNode = node;
      const inspector = document.getElementById('node-inspector');
      inspector.style.display = 'flex';

      document.getElementById('insp-title').innerText = node.label;
      document.getElementById('insp-id').innerText = node.id;
      document.getElementById('insp-summary').innerText = node.summary;
      
      const hemiTag = document.getElementById('insp-hemi');
      hemiTag.innerText = node.hemisphere;
      hemiTag.className = 'node-hemi-tag ' + (node.hemisphere === 'LEFT' ? 'hemi-left' : 'hemi-right');

      const similarities = [];
      nodes.forEach((n, i) => {{
        if (n.id !== node.id) {{
          const sim = cosineSim(node.vector, n.vector);
          similarities.push({{ node: n, index: i, sim }});
        }}
      }});
      similarities.sort((a, b) => b.sim - a.sim);
      const topKnn = similarities.slice(0, knnCount);

      const knnListEl = document.getElementById('insp-knn-list');
      knnListEl.innerHTML = '';
      topKnn.forEach(item => {{
        const div = document.createElement('div');
        div.className = 'knn-item';
        div.onclick = () => selectNode(item.node);
        div.innerHTML = `
          <span class="knn-name">${{item.node.label}}</span>
          <span class="knn-sim">${{(item.sim * 100).toFixed(1)}}%</span>
        `;
        knnListEl.appendChild(div);
      }});

      const connectedEdges = edges.filter(e => e.source === node.id || e.target === node.id);
      const edgesListEl = document.getElementById('insp-edges-list');
      edgesListEl.innerHTML = connectedEdges.length ? '' : '<div style="font-size:11px; color:#64748b;">Nessun arco diretto nel grafo.</div>';
      connectedEdges.forEach(e => {{
        const otherId = e.source === node.id ? e.target : e.source;
        const otherNode = nodes.find(n => n.id === otherId) || {{ label: otherId }};
        const div = document.createElement('div');
        div.className = 'knn-item';
        div.onclick = () => {{ if (otherNode.vector) selectNode(otherNode); }};
        div.innerHTML = `
          <span class="knn-name">${{otherNode.label}}</span>
          <span style="font-size:9px; font-family:'JetBrains Mono', monospace; color:#a855f7;">${{e.relation}}</span>
        `;
        edgesListEl.appendChild(div);
      }});

      const nodeIndexMap = linesMesh.userData.nodeIndexMap;
      const sIdx = nodeIndexMap.get(node.id);
      const knnPositions = [];

      topKnn.forEach(item => {{
        knnPositions.push(
          positions.current[sIdx * 3], positions.current[sIdx * 3 + 1], positions.current[sIdx * 3 + 2],
          positions.current[item.index * 3], positions.current[item.index * 3 + 1], positions.current[item.index * 3 + 2]
        );
      }});

      knnLinesMesh.geometry.setAttribute('position', new THREE.Float32BufferAttribute(knnPositions, 3));
      knnLinesMesh.geometry.attributes.position.needsUpdate = true;
    }}

    function closeInspector() {{
      document.getElementById('node-inspector').style.display = 'none';
      selectedNode = null;
      knnLinesMesh.geometry.setAttribute('position', new THREE.Float32BufferAttribute([], 3));
      knnLinesMesh.geometry.attributes.position.needsUpdate = true;
    }}

    function focusCameraOnSelected() {{
      if (!selectedNode) return;
      const nodeIndexMap = linesMesh.userData.nodeIndexMap;
      const idx = nodeIndexMap.get(selectedNode.id);
      const targetPos = {{
        x: positions.current[idx * 3],
        y: positions.current[idx * 3 + 1],
        z: positions.current[idx * 3 + 2]
      }};

      new TWEEN.Tween(controls.target).to(targetPos, 800).easing(TWEEN.Easing.Cubic.Out).start();
      new TWEEN.Tween(camera.position)
        .to({{ x: targetPos.x, y: targetPos.y + 20, z: targetPos.z + 120 }}, 800)
        .easing(TWEEN.Easing.Cubic.Out)
        .start();
    }}

    document.getElementById('search-input').addEventListener('input', (e) => {{
      const query = e.target.value.toLowerCase().trim();
      if (!query) {{
        filterHemisphere(activeFilter, document.querySelector('.filter-chips .chip.active'));
        return;
      }}

      const matchedNode = nodes.find(n => n.label.toLowerCase().includes(query) || n.id.toLowerCase().includes(query));
      if (matchedNode) {{
        selectNode(matchedNode);
        focusCameraOnSelected();
      }}
    }});

    function syncLinesAndLabels() {{
      const nodeIndexMap = linesMesh.userData.nodeIndexMap;
      const linePosAttr = linesMesh.geometry.attributes.position;
      let ptr = 0;

      edges.forEach(e => {{
        const sIdx = nodeIndexMap.get(e.source);
        const tIdx = nodeIndexMap.get(e.target);
        if (sIdx !== undefined && tIdx !== undefined) {{
          linePosAttr.setXYZ(ptr++, positions.current[sIdx * 3], positions.current[sIdx * 3 + 1], positions.current[sIdx * 3 + 2]);
          linePosAttr.setXYZ(ptr++, positions.current[tIdx * 3], positions.current[tIdx * 3 + 1], positions.current[tIdx * 3 + 2]);
        }}
      }});
      linePosAttr.needsUpdate = true;

      labelSpritesGroup.children.forEach(sp => {{
        const idx = sp.userData.nodeIndex;
        sp.position.set(positions.current[idx * 3], positions.current[idx * 3 + 1] + 8, positions.current[idx * 3 + 2]);
      }});
    }}

    function onWindowResize() {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }}

    function animate() {{
      requestAnimationFrame(animate);
      TWEEN.update();
      controls.update();

      if (isTsneRunning) {{
        stepTsne();
      }}

      pointCloudMesh.geometry.attributes.position.needsUpdate = true;
      syncLinesAndLabels();

      renderer.render(scene, camera);
    }}

    initProjections();
    initThree();
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_template)
print('SUCCESS: Created', OUTPUT_HTML)
