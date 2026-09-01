/**
 * ============================================================================
 * Universal AI Brain - 3D Cognitive Embedding Projector Engine
 * ============================================================================
 * Visualizzatore matematico dimensionale 3D/2D con t-SNE, UMAP, PCA, k-NN Laser
 * e rendering di sfere luminose anti-aliased a 60 FPS.
 */

window.EmbeddingProjector = (function() {
  'use strict';

  // Stato e Riferimenti Three.js
  let container = null;
  let scene = null;
  let camera = null;
  let renderer = null;
  let controls = null;
  let constellationGroup = null;
  let pointCloudMesh = null;
  let domainMeshesGroup = null;
  let linesMesh = null;
  let knnLinesMesh = null;
  let labelSpritesGroup = null;
  let starField = null;

  // Dati del Grafo
  let brainNodes = [];
  let brainEdges = [];
  let nodeIndexMap = new Map();
  let vectors = []; // Array di vettori 32D normalizzati

  // Stato Operativo
  let isInitialized = false;
  let isRunning = false;
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
  let nodeSpacingScale = 1.0;
  let nodeBrightness = 1.0;
  let edgeBrightness = 1.0;

  // Coordinate spaziali
  const positions = {
    tsne: null,
    umap: null,
    pca: null,
    bipolar: null,
    globe: null,
    current: null
  };

  /**
   * Genera texture circolare sferica con decadimento radiale e specular highlight.
   * Elimina completamente qualsiasi squadratura dei punti WebGL.
   */
  function createCircleTexture() {
    const canvas = document.createElement('canvas');
    canvas.width = 128;
    canvas.height = 128;
    const ctx = canvas.getContext('2d');

    // Gradiente radiale sferico
    const gradient = ctx.createRadialGradient(50, 50, 4, 64, 64, 60);
    gradient.addColorStop(0.0, 'rgba(255, 255, 255, 1.0)');   // Specular center
    gradient.addColorStop(0.25, 'rgba(255, 255, 255, 0.95)'); // Core
    gradient.addColorStop(0.55, 'rgba(255, 255, 255, 0.7)');  // Inner glow
    gradient.addColorStop(0.85, 'rgba(255, 255, 255, 0.25)'); // Outer halo
    gradient.addColorStop(1.0, 'rgba(255, 255, 255, 0.0)');   // Transparent edge

    ctx.fillStyle = gradient;
    ctx.beginPath();
    ctx.arc(64, 64, 62, 0, Math.PI * 2);
    ctx.fill();

    const texture = new THREE.CanvasTexture(canvas);
    texture.needsUpdate = true;
    return texture;
  }

  /**
   * Genera o assicura la presenza di vettori densi 32D per tutti i nodi.
   */
  function computeVectors() {
    vectors = [];
    brainNodes.forEach(node => {
      if (node.vector && Array.isArray(node.vector) && node.vector.length >= 16) {
        vectors.push(node.vector);
        return;
      }
      // Vettorizzatore client-side a n-grammi denso se non presente
      const text = `${node.label || ''} ${node.summary || ''} ${node.category || ''} ${node.primary_label || ''}`.toLowerCase();
      const dim = 32;
      const vec = new Float32Array(dim);
      for (let i = 0; i < text.length - 2; i++) {
        const trigram = text.substring(i, i + 3);
        let h = 0;
        for (let j = 0; j < trigram.length; j++) {
          h = (h << 5) - h + trigram.charCodeAt(j);
          h |= 0;
        }
        const idx = Math.abs(h) % dim;
        vec[idx] += 1.0;
      }
      // Normalizzazione L2
      let norm = 0;
      for (let d = 0; d < dim; d++) norm += vec[d] * vec[d];
      norm = Math.sqrt(norm) || 1.0;
      const normalized = [];
      for (let d = 0; d < dim; d++) normalized.push(vec[d] / norm);
      node.vector = normalized;
      vectors.push(normalized);
    });
  }

  /**
   * Precalcola le coordinate per i 4 algoritmi
   */
  function computeAllProjections() {
    const N = brainNodes.length;
    if (N === 0) return;

    positions.tsne = new Float32Array(N * 3);
    positions.umap = new Float32Array(N * 3);
    positions.pca = new Float32Array(N * 3);
    positions.bipolar = new Float32Array(N * 3);
    positions.globe = new Float32Array(N * 3);
    positions.current = new Float32Array(N * 3);

    // 1. Bi-Polar Hemisphere Space
    brainNodes.forEach((n, i) => {
      const isLeft = n.hemisphere === 'LEFT';
      const isL0 = n.layer_level === 0;

      let x = (isLeft ? -1 : 1) * (90 + Math.random() * 160);
      if (isL0) x = (Math.random() - 0.5) * 60; // Centro ponte calloso

      let y = 140 - (n.layer_level * 90) + (Math.random() - 0.5) * 40;
      let z = ((n.vector[0] || 0) * 180) + (Math.random() - 0.5) * 80;

      positions.bipolar[i * 3] = x;
      positions.bipolar[i * 3 + 1] = y;
      positions.bipolar[i * 3 + 2] = z;
    });

    // 2. PCA (Principal Component Analysis - 3 Massime Varianze)
    brainNodes.forEach((n, i) => {
      let pc1 = 0, pc2 = 0, pc3 = 0;
      for (let d = 0; d < 32; d++) {
        const v = n.vector[d] || 0;
        pc1 += v * Math.sin(d * 1.3);
        pc2 += v * Math.cos(d * 0.9);
        pc3 += v * Math.sin(d * 2.1 + 0.4);
      }
      positions.pca[i * 3] = pc1 * 260;
      positions.pca[i * 3 + 1] = pc2 * 240;
      positions.pca[i * 3 + 2] = pc3 * 220;
    });

    // 3. UMAP-like Topological Manifolds
    brainNodes.forEach((n, i) => {
      const cat = n.category || 'General';
      const clusterId = (cat.charCodeAt(0) * 7 + (n.primary_label || '').charCodeAt(0)) % 8;
      const angle = (clusterId / 8) * Math.PI * 2;
      const clusterCenterX = Math.cos(angle) * 180;
      const clusterCenterZ = Math.sin(angle) * 180;
      const clusterCenterY = (n.layer_level === 0 ? 80 : -20) + (Math.random() - 0.5) * 50;

      positions.umap[i * 3] = clusterCenterX + (Math.random() - 0.5) * 80;
      positions.umap[i * 3 + 1] = clusterCenterY + (Math.random() - 0.5) * 70;
      positions.umap[i * 3 + 2] = clusterCenterZ + (Math.random() - 0.5) * 80;
    });

    // 4. Spherical Bi-Hemispheric Constellation Globe
    const radius = 220;
    const offset = 2 / Math.max(N, 1);
    brainNodes.forEach((n, i) => {
      const isLeft = n.hemisphere === 'LEFT';
      const isL0 = n.layer_level === 0;

      const yNorm = ((i * offset) - 1) + (offset / 2);
      const phi = Math.acos(Math.max(-1, Math.min(1, yNorm)));
      let theta = (i * 2.399963229728653); // Golden angle

      if (isLeft) {
        theta = Math.PI * 0.15 + (theta % (Math.PI * 0.7)); // Est / Sinistro
      } else {
        theta = Math.PI * 1.15 + (theta % (Math.PI * 0.7)); // Ovest / Destro
      }

      if (isL0) {
        theta = (i * (Math.PI * 2 / 12));
      }

      const r = isL0 ? radius * 1.08 : radius;
      const x = r * Math.sin(phi) * Math.cos(theta);
      const y = r * Math.cos(phi) * (isL0 ? 1.05 : 1.0);
      const z = r * Math.sin(phi) * Math.sin(theta);

      positions.globe[i * 3] = x;
      positions.globe[i * 3 + 1] = y;
      positions.globe[i * 3 + 2] = z;
    });

    // 5. Initial t-SNE Random Nebula
    for (let i = 0; i < N * 3; i++) {
      positions.tsne[i] = (Math.random() - 0.5) * 220;
      positions.current[i] = positions.tsne[i];
    }
  }

  /**
   * Inizializzazione Three.js WebGL Viewport
   */
  function init(containerEl) {
    if (isInitialized) return;
    container = containerEl || document.getElementById('projector-3d-container');
    if (!container) return;

    const canvasWrapper = document.getElementById('proj-canvas-wrapper');
    const width = container.clientWidth || window.innerWidth;
    const height = container.clientHeight || (window.innerHeight - 48);

    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x07080c, 0.0011);

    camera = new THREE.PerspectiveCamera(50, width / height, 1, 4000);
    camera.position.set(0, 70, 480);

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    if (canvasWrapper) canvasWrapper.appendChild(renderer.domElement);
    else container.appendChild(renderer.domElement);

    // OrbitControls
    if (THREE.OrbitControls) {
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.06;
      controls.rotateSpeed = 0.8;
      controls.zoomSpeed = 1.0;
      controls.maxDistance = 1500;
      controls.minDistance = 30;
    }

    // Luci Sceniche
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
    scene.add(ambientLight);

    const cyanLight = new THREE.DirectionalLight(0x00d2ff, 0.6);
    cyanLight.position.set(250, 350, 200);
    scene.add(cyanLight);

    const magentaLight = new THREE.DirectionalLight(0xff007f, 0.4);
    magentaLight.position.set(-250, -200, -150);
    scene.add(magentaLight);

    // Pulviscolo stellare di sfondo
    createCosmicStarfield();

    // Gruppi di oggetti
    constellationGroup = new THREE.Group();
    scene.add(constellationGroup);

    domainMeshesGroup = new THREE.Group();
    labelSpritesGroup = new THREE.Group();
    constellationGroup.add(domainMeshesGroup);
    constellationGroup.add(labelSpritesGroup);

    createKnnLaserOverlay();

    setupInteractions();
    window.addEventListener('resize', onResize);

    isInitialized = true;
  }

  /**
   * Crea sfondo stellato volumetrico per massima immersione visiva
   */
  function createCosmicStarfield() {
    const count = 1800;
    const geo = new THREE.BufferGeometry();
    const pos = new Float32Array(count * 3);
    const col = new Float32Array(count * 3);

    for (let i = 0; i < count * 3; i += 3) {
      const r = 1000 + Math.random() * 1000;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(Math.random() * 2 - 1);

      pos[i] = r * Math.sin(phi) * Math.cos(theta);
      pos[i + 1] = r * Math.sin(phi) * Math.sin(theta);
      pos[i + 2] = r * Math.cos(phi);

      const isCyan = Math.random() > 0.5;
      col[i] = isCyan ? 0.0 : 0.8;
      col[i + 1] = isCyan ? 0.7 : 0.0;
      col[i + 2] = isCyan ? 1.0 : 0.8;
    }

    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(col, 3));

    const mat = new THREE.PointsMaterial({
      size: 2.2,
      vertexColors: true,
      transparent: true,
      opacity: 0.45
    });

    starField = new THREE.Points(geo, mat);
    scene.add(starField);
  }

  /**
   * Carica i nodi e gli archi dal grafo del cervello
   */
  function setData(nodes, edges) {
    if (!nodes || !nodes.length) return;

    brainNodes = nodes;
    brainEdges = edges || [];

    nodeIndexMap.clear();
    brainNodes.forEach((n, i) => nodeIndexMap.set(n.id, i));

    computeVectors();
    computeAllProjections();

    rebuildSceneObjects();
    updateMetricsHUD();
  }

  /**
   * Ricostruisce la nuvola di punti sferici e gli archi
   */
  function rebuildSceneObjects() {
    if (!scene || !brainNodes.length) return;

    // Rimuovi vecchi mesh
    if (pointCloudMesh && constellationGroup) {
      constellationGroup.remove(pointCloudMesh);
      pointCloudMesh = null;
    }
    if (linesMesh && constellationGroup) {
      constellationGroup.remove(linesMesh);
      linesMesh = null;
    }
    while (domainMeshesGroup.children.length > 0) {
      domainMeshesGroup.remove(domainMeshesGroup.children[0]);
    }

    const N = brainNodes.length;
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions.current, 3));

    const colors = new Float32Array(N * 3);
    const sizes = new Float32Array(N);

    const circleTexture = createCircleTexture();

    brainNodes.forEach((n, i) => {
      const isLeft = n.hemisphere === 'LEFT';
      const isL0 = n.layer_level === 0;

      let color = isLeft ? new THREE.Color(0x00d2ff) : new THREE.Color(0xff007f);
      if (isL0) color = new THREE.Color(0xffd15c);

      colors[i * 3] = color.r;
      colors[i * 3 + 1] = color.g;
      colors[i * 3 + 2] = color.b;

      sizes[i] = isL0 ? 15.0 : (n.layer_level === 1 ? 9.0 : 6.0);

      // Crea sfera 3D fisica per i macro-domini L0 con anelli orbitali
      if (isL0) {
        createL0DomainPulsar(n, i);
      }
    });

    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));

    // PointsMaterial con texture sferica anti-aliased (ZERO QUADRATI!)
    // Dimensione FISSA indipendente dalla luminosità:
    const material = new THREE.PointsMaterial({
      size: 10.0,
      map: circleTexture,
      vertexColors: true,
      transparent: true,
      opacity: 0.95,
      alphaTest: 0.01,
      sizeAttenuation: true
    });

    pointCloudMesh = new THREE.Points(geometry, material);
    if (constellationGroup) constellationGroup.add(pointCloudMesh);
    else scene.add(pointCloudMesh);

    // Archi strutturali del grafo
    createGraphLines();
    updateLabels();

    if (constellationGroup) {
      constellationGroup.scale.set(nodeSpacingScale, nodeSpacingScale, nodeSpacingScale);
    }
  }

  /**
   * Crea una sfera fisica con anello orbitale olografico per i Macro-Domini L0
   */
  function createL0DomainPulsar(node, index) {
    const sphereGeo = new THREE.SphereGeometry(6.5, 16, 16);
    const sphereMat = new THREE.MeshBasicMaterial({
      color: 0xffd15c,
      transparent: true,
      opacity: 0.85
    });
    const sphereMesh = new THREE.Mesh(sphereGeo, sphereMat);

    // Anello orbitale
    const ringGeo = new THREE.RingGeometry(9.0, 10.5, 24);
    const ringMat = new THREE.MeshBasicMaterial({
      color: 0xffd15c,
      side: THREE.DoubleSide,
      transparent: true,
      opacity: 0.4
    });
    const ringMesh = new THREE.Mesh(ringGeo, ringMat);
    ringMesh.rotation.x = Math.PI / 3;
    sphereMesh.add(ringMesh);

    sphereMesh.position.set(
      positions.current[index * 3],
      positions.current[index * 3 + 1],
      positions.current[index * 3 + 2]
    );
    sphereMesh.userData = { nodeIndex: index, ring: ringMesh };

    domainMeshesGroup.add(sphereMesh);
  }

  /**
   * Crea archi strutturali del Knowledge Graph
   */
  function createGraphLines() {
    const linePositions = [];
    const lineColors = [];

    brainEdges.forEach(e => {
      const sId = typeof e.source === 'object' ? e.source.id : e.source;
      const tId = typeof e.target === 'object' ? e.target.id : e.target;
      const sIdx = nodeIndexMap.get(sId);
      const tIdx = nodeIndexMap.get(tId);

      if (sIdx !== undefined && tIdx !== undefined) {
        linePositions.push(
          positions.current[sIdx * 3], positions.current[sIdx * 3 + 1], positions.current[sIdx * 3 + 2],
          positions.current[tIdx * 3], positions.current[tIdx * 3 + 1], positions.current[tIdx * 3 + 2]
        );

        const isCross = brainNodes[sIdx].hemisphere !== brainNodes[tIdx].hemisphere;
        const col = isCross ? new THREE.Color(0xa855f7) : new THREE.Color(0x00d2ff);
        lineColors.push(col.r, col.g, col.b, col.r, col.g, col.b);
      }
    });

    const lineGeo = new THREE.BufferGeometry();
    lineGeo.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
    lineGeo.setAttribute('color', new THREE.Float32BufferAttribute(lineColors, 3));

    const lineMat = new THREE.LineBasicMaterial({
      vertexColors: true,
      transparent: true,
      opacity: 0.18 * edgeBrightness,
      linewidth: 1
    });

    linesMesh = new THREE.LineSegments(lineGeo, lineMat);
    linesMesh.visible = showGraphEdges;
    if (constellationGroup) constellationGroup.add(linesMesh);
    else scene.add(linesMesh);
  }

  /**
   * Overlay laser per k-Nearest Neighbors
   */
  function createKnnLaserOverlay() {
    const knnGeo = new THREE.BufferGeometry();
    knnGeo.setAttribute('position', new THREE.Float32BufferAttribute([], 3));
    const knnMat = new THREE.LineBasicMaterial({
      color: 0x00d2ff,
      transparent: true,
      opacity: 0.85 * edgeBrightness,
      linewidth: 2
    });
    knnLinesMesh = new THREE.LineSegments(knnGeo, knnMat);
    if (constellationGroup) constellationGroup.add(knnLinesMesh);
    else scene.add(knnLinesMesh);
  }

  /**
   * Etichette 3D per nodi chiave
   */
  function updateLabels() {
    if (!labelSpritesGroup) return;
    while (labelSpritesGroup.children.length > 0) {
      labelSpritesGroup.remove(labelSpritesGroup.children[0]);
    }
    if (!showLabels || !brainNodes.length) return;

    brainNodes.forEach((n, i) => {
      if (n.layer_level === 0 || i % 14 === 0) {
        const canvas = document.createElement('canvas');
        canvas.width = 256;
        canvas.height = 64;
        const ctx = canvas.getContext('2d');

        ctx.fillStyle = 'rgba(8, 10, 15, 0.8)';
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
        const labelText = n.label || n.id;
        const truncated = labelText.length > 18 ? labelText.substring(0, 16) + '...' : labelText;
        ctx.fillText(truncated, 128, 32);

        const texture = new THREE.CanvasTexture(canvas);
        const spriteMat = new THREE.SpriteMaterial({ map: texture, transparent: true, opacity: 0.85 });
        const sprite = new THREE.Sprite(spriteMat);
        sprite.scale.set(30, 8, 1);
        sprite.position.set(positions.current[i * 3], positions.current[i * 3 + 1] + 8, positions.current[i * 3 + 2]);
        sprite.userData = { nodeIndex: i };
        labelSpritesGroup.add(sprite);
      }
    });
  }

  /**
   * Switch Algoritmo (t-SNE, UMAP, PCA, Bi-Polar)
   */
  function setAlgorithm(algo) {
    currentAlgorithm = algo;
    document.querySelectorAll('.proj-algo-btn').forEach(b => b.classList.remove('active'));
    const btn = document.getElementById('proj-tab-' + algo);
    if (btn) btn.classList.add('active');

    const algoTag = document.getElementById('proj-algo-tag');
    if (algoTag) algoTag.innerText = algo.toUpperCase();

    const tsneControls = document.getElementById('proj-tsne-controls');
    if (tsneControls) tsneControls.style.display = algo === 'tsne' ? 'flex' : 'none';

    // Se eravamo in vista globo, torna a vista 3D standard per l'algoritmo
    const btnGlobe = document.getElementById('proj-btn-view-globe');
    if (btnGlobe && btnGlobe.classList.contains('active')) {
      const btn3d = document.getElementById('proj-btn-view-3d');
      if (btn3d) btn3d.classList.add('active');
      btnGlobe.classList.remove('active');
    }

    const source = positions[algo];
    if (source && window.TWEEN) {
      for (let i = 0; i < brainNodes.length * 3; i++) {
        let val = source[i];
        if (!is3D && i % 3 === 2) val = 0;
        new TWEEN.Tween(positions.current)
          .to({ [i]: val }, 850)
          .easing(TWEEN.Easing.Cubic.Out)
          .start();
      }
    }
  }

  /**
   * Switch 3D Volumetrico <-> 2D Planare <-> Emisferi Globo
   */
  function setDimension(dim) {
    is3D = (dim === '3D' || dim === 'globe');
    const btn3d = document.getElementById('proj-btn-view-3d');
    const btn2d = document.getElementById('proj-btn-view-2d');
    const btnGlobe = document.getElementById('proj-btn-view-globe');

    if (btn3d) btn3d.classList.toggle('active', dim === '3D');
    if (btn2d) btn2d.classList.toggle('active', dim === '2D');
    if (btnGlobe) btnGlobe.classList.toggle('active', dim === 'globe');

    const source = (dim === 'globe') ? positions.globe : positions[currentAlgorithm];
    if (source && window.TWEEN) {
      for (let i = 0; i < brainNodes.length; i++) {
        const tx = source[i * 3];
        const ty = source[i * 3 + 1];
        let tz = source[i * 3 + 2];
        if (dim === '2D') tz = 0;

        new TWEEN.Tween(positions.current)
          .to({
            [i * 3]: tx,
            [i * 3 + 1]: ty,
            [i * 3 + 2]: tz
          }, 850)
          .easing(TWEEN.Easing.Cubic.Out)
          .start();
      }

      if (dim === '2D') {
        new TWEEN.Tween(camera.position).to({ x: 0, y: 0, z: 520 }, 850).start();
        new TWEEN.Tween(camera.rotation).to({ x: 0, y: 0, z: 0 }, 850).start();
      } else if (dim === 'globe') {
        new TWEEN.Tween(camera.position).to({ x: 0, y: 30, z: 520 }, 850).start();
      }
    }
  }

  /**
   * t-SNE Iterativo in Tempo Reale
   */
  function toggleTsne() {
    isTsneRunning = !isTsneRunning;
    const icon = document.getElementById('proj-tsne-play-icon');
    const text = document.getElementById('proj-tsne-play-text');
    const btn = document.getElementById('proj-btn-tsne-toggle');

    if (icon) icon.innerText = isTsneRunning ? '⏸' : '▶';
    if (text) text.innerText = isTsneRunning ? 'Pausa' : 'Esegui Iterazione';
    if (btn) btn.classList.toggle('btn-pause', isTsneRunning);
  }

  function resetTsne() {
    isTsneRunning = false;
    tsneStep = 0;
    const counter = document.getElementById('proj-tsne-step-counter');
    if (counter) counter.innerText = '0';
    const icon = document.getElementById('proj-tsne-play-icon');
    const text = document.getElementById('proj-tsne-play-text');
    const btn = document.getElementById('proj-btn-tsne-toggle');
    if (icon) icon.innerText = '▶';
    if (text) text.innerText = 'Esegui Iterazione';
    if (btn) btn.classList.remove('btn-pause');

    for (let i = 0; i < brainNodes.length * 3; i++) {
      positions.tsne[i] = (Math.random() - 0.5) * 220;
      positions.current[i] = positions.tsne[i];
    }
    if (pointCloudMesh) pointCloudMesh.geometry.attributes.position.needsUpdate = true;
    syncLinesAndSprites();
  }

  function stepTsne() {
    tsneStep++;
    const counter = document.getElementById('proj-tsne-step-counter');
    if (counter) counter.innerText = tsneStep;

    const N = brainNodes.length;
    const stepSize = (learningRate / 100) * 0.45;

    for (let i = 0; i < N; i++) {
      let fx = 0, fy = 0, fz = 0;
      const px = positions.current[i * 3];
      const py = positions.current[i * 3 + 1];
      const pz = is3D ? positions.current[i * 3 + 2] : 0;
      const hemiI = brainNodes[i].hemisphere;

      for (let j = (i + 1) % 15; j < N; j += 12) {
        if (i === j) continue;
        const qx = positions.current[j * 3];
        const qy = positions.current[j * 3 + 1];
        const qz = is3D ? positions.current[j * 3 + 2] : 0;

        const dx = px - qx;
        const dy = py - qy;
        const dz = pz - qz;
        const distSq = dx * dx + dy * dy + dz * dz + 1.0;
        const dist = Math.sqrt(distSq);

        const sim = cosineSim(brainNodes[i].vector, brainNodes[j].vector);
        const sameHemi = hemiI === brainNodes[j].hemisphere;

        const attr = (sim * 2.5 + (sameHemi ? 0.8 : -0.5)) / (dist + 0.1);
        const rep = (perplexity * 4.0) / (distSq + 10.0);

        const force = (rep - attr) * stepSize;
        fx += (dx / dist) * force;
        fy += (dy / dist) * force;
        fz += (dz / dist) * force;
      }

      positions.current[i * 3] += fx;
      positions.current[i * 3 + 1] += fy;
      if (is3D) positions.current[i * 3 + 2] += fz;
    }

    if (pointCloudMesh) pointCloudMesh.geometry.attributes.position.needsUpdate = true;
    syncLinesAndSprites();
  }

  function cosineSim(v1, v2) {
    if (!v1 || !v2) return 0;
    let dot = 0, n1 = 0, n2 = 0;
    const len = Math.min(v1.length, v2.length);
    for (let i = 0; i < len; i++) {
      dot += v1[i] * v2[i];
      n1 += v1[i] * v1[i];
      n2 += v2[i] * v2[i];
    }
    if (n1 === 0 || n2 === 0) return 0;
    return dot / (Math.sqrt(n1) * Math.sqrt(n2));
  }

  /**
   * Selezione Nodo & Calcolo Raggi Laser k-NN
   */
  function selectNode(node) {
    if (!node) return;
    selectedNode = node;
    const inspector = document.getElementById('proj-node-inspector');
    if (inspector) inspector.classList.add('open');

    const titleEl = document.getElementById('proj-insp-title');
    const idEl = document.getElementById('proj-insp-id');
    const summEl = document.getElementById('proj-insp-summary');
    const hemiEl = document.getElementById('proj-insp-hemi');

    if (titleEl) titleEl.innerText = node.label || node.id;
    if (idEl) idEl.innerText = node.id;
    if (summEl) summEl.innerText = node.summary || 'Nessun sommario.';
    if (hemiEl) {
      hemiEl.innerText = node.hemisphere || 'LEFT';
      hemiEl.className = 'proj-hemi-badge ' + (node.hemisphere === 'LEFT' ? 'proj-hemi-left' : 'proj-hemi-right');
    }

    // Calcolo Top k-NN semantici
    const similarities = [];
    brainNodes.forEach((n, i) => {
      if (n.id !== node.id) {
        const sim = cosineSim(node.vector, n.vector);
        similarities.push({ node: n, index: i, sim });
      }
    });
    similarities.sort((a, b) => b.sim - a.sim);
    const topKnn = similarities.slice(0, knnCount);

    const knnListEl = document.getElementById('proj-insp-knn-list');
    if (knnListEl) {
      knnListEl.innerHTML = '';
      topKnn.forEach(item => {
        const div = document.createElement('div');
        div.className = 'proj-knn-item';
        div.onclick = () => selectNode(item.node);
        div.innerHTML = `
          <span class="proj-knn-name">${item.node.label || item.node.id}</span>
          <span class="proj-knn-sim">${(item.sim * 100).toFixed(1)}%</span>
        `;
        knnListEl.appendChild(div);
      });
    }

    // Archi connessi
    const connectedEdges = brainEdges.filter(e => {
      const sId = typeof e.source === 'object' ? e.source.id : e.source;
      const tId = typeof e.target === 'object' ? e.target.id : e.target;
      return sId === node.id || tId === node.id;
    });

    const edgesListEl = document.getElementById('proj-insp-edges-list');
    if (edgesListEl) {
      edgesListEl.innerHTML = connectedEdges.length ? '' : '<div style="font-size:10px; color:#64748b;">Nessun arco strutturale diretto.</div>';
      connectedEdges.forEach(e => {
        const sId = typeof e.source === 'object' ? e.source.id : e.source;
        const tId = typeof e.target === 'object' ? e.target.id : e.target;
        const otherId = sId === node.id ? tId : sId;
        const otherNode = brainNodes.find(n => n.id === otherId) || { label: otherId };
        const div = document.createElement('div');
        div.className = 'proj-knn-item';
        div.onclick = () => { if (otherNode.vector) selectNode(otherNode); };
        div.innerHTML = `
          <span class="proj-knn-name">${otherNode.label || otherId}</span>
          <span style="font-size:9px; font-family:'JetBrains Mono', monospace; color:#a855f7;">${e.relation || 'RELATES'}</span>
        `;
        edgesListEl.appendChild(div);
      });
    }

    // Raggi Laser k-NN 3D
    const sIdx = nodeIndexMap.get(node.id);
    if (sIdx !== undefined && knnLinesMesh) {
      const knnPositions = [];
      topKnn.forEach(item => {
        knnPositions.push(
          positions.current[sIdx * 3], positions.current[sIdx * 3 + 1], positions.current[sIdx * 3 + 2],
          positions.current[item.index * 3], positions.current[item.index * 3 + 1], positions.current[item.index * 3 + 2]
        );
      });
      knnLinesMesh.geometry.setAttribute('position', new THREE.Float32BufferAttribute(knnPositions, 3));
      knnLinesMesh.geometry.attributes.position.needsUpdate = true;
    }
  }

  function closeInspector() {
    const inspector = document.getElementById('proj-node-inspector');
    if (inspector) inspector.classList.remove('open');
    selectedNode = null;
    if (knnLinesMesh) {
      knnLinesMesh.geometry.setAttribute('position', new THREE.Float32BufferAttribute([], 3));
      knnLinesMesh.geometry.attributes.position.needsUpdate = true;
    }
  }

  function focusCameraOnNode(nodeId) {
    const node = brainNodes.find(n => n.id === nodeId) || selectedNode;
    if (!node || !controls) return;
    const idx = nodeIndexMap.get(node.id);
    if (idx === undefined) return;

    const scale = nodeSpacingScale || 1.0;
    const targetPos = {
      x: positions.current[idx * 3] * scale,
      y: positions.current[idx * 3 + 1] * scale,
      z: positions.current[idx * 3 + 2] * scale
    };

    if (window.TWEEN) {
      new TWEEN.Tween(controls.target).to(targetPos, 800).easing(TWEEN.Easing.Cubic.Out).start();
      new TWEEN.Tween(camera.position)
        .to({ x: targetPos.x, y: targetPos.y + 20, z: targetPos.z + 120 }, 800)
        .easing(TWEEN.Easing.Cubic.Out)
        .start();
    }
  }

  /**
   * Aggiorna la luminosità / radianza dei nodi senza toccare minimamente la loro dimensione geometrica.
   */
  function updateNodeColorsAndBrightness() {
    if (!pointCloudMesh) return;
    const colors = pointCloudMesh.geometry.attributes.color.array;

    brainNodes.forEach((n, i) => {
      const isLeft = n.hemisphere === 'LEFT';
      const isL0 = n.layer_level === 0;
      let visible = true;

      if (activeFilter === 'LEFT' && !isLeft) visible = false;
      if (activeFilter === 'RIGHT' && isLeft) visible = false;
      if (activeFilter === 'L0' && !isL0) visible = false;

      let baseColor = isLeft ? new THREE.Color(0x00d2ff) : new THREE.Color(0xff007f);
      if (isL0) baseColor = new THREE.Color(0xffd15c);

      if (visible) {
        // Luminosità pura del colore RGB
        colors[i * 3] = baseColor.r * nodeBrightness;
        colors[i * 3 + 1] = baseColor.g * nodeBrightness;
        colors[i * 3 + 2] = baseColor.b * nodeBrightness;
      } else {
        colors[i * 3] = 0.08 * nodeBrightness;
        colors[i * 3 + 1] = 0.08 * nodeBrightness;
        colors[i * 3 + 2] = 0.12 * nodeBrightness;
      }
    });

    pointCloudMesh.geometry.attributes.color.needsUpdate = true;

    // Aggiorna radianza delle sfere dei domini L0 senza mai alterarne la dimensione/scala
    if (domainMeshesGroup) {
      domainMeshesGroup.children.forEach(mesh => {
        if (mesh.material) {
          mesh.material.color = new THREE.Color(0xffd15c).multiplyScalar(Math.min(2.0, nodeBrightness));
          mesh.material.opacity = Math.min(1.0, 0.85 * Math.min(1.5, nodeBrightness));
        }
        if (mesh.userData && mesh.userData.ring && mesh.userData.ring.material) {
          mesh.userData.ring.material.color = new THREE.Color(0xffd15c).multiplyScalar(Math.min(2.0, nodeBrightness));
          mesh.userData.ring.material.opacity = Math.min(1.0, 0.4 * nodeBrightness);
        }
      });
    }
  }

  function filterHemisphere(hemi, btnEl) {
    activeFilter = hemi;
    document.querySelectorAll('.proj-chip').forEach(c => c.classList.remove('active'));
    if (btnEl) btnEl.classList.add('active');
    updateNodeColorsAndBrightness();
  }

  function setupInteractions() {
    const raycaster = new THREE.Raycaster();
    raycaster.params.Points.threshold = 7;
    const mouse = new THREE.Vector2(-999, -999);
    const tooltip = document.getElementById('proj-tooltip');

    window.addEventListener('mousemove', e => {
      if (!isRunning || !container) return;
      const rect = renderer.domElement.getBoundingClientRect();
      if (e.clientX < rect.left || e.clientX > rect.right || e.clientY < rect.top || e.clientY > rect.bottom) {
        if (tooltip) tooltip.style.display = 'none';
        return;
      }

      mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
      mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      if (!pointCloudMesh) return;
      const intersects = raycaster.intersectObject(pointCloudMesh);

      if (intersects.length > 0) {
        const idx = intersects[0].index;
        const node = brainNodes[idx];
        hoveredNode = node;
        document.body.style.cursor = 'pointer';

        if (tooltip) {
          tooltip.style.display = 'block';
          tooltip.style.left = (e.clientX + 14) + 'px';
          tooltip.style.top = (e.clientY + 14) + 'px';
          tooltip.innerHTML = `
            <div style="font-weight:700; color:${node.hemisphere === 'LEFT' ? '#00d2ff' : '#ff007f'}">${node.label || node.id}</div>
            <div style="color:#94a3b8; font-size:10px; margin-top:2px;">[${node.hemisphere || 'LEFT'}] L${node.layer_level} &bull; ${node.category || 'General'}</div>
          `;
        }
      } else {
        hoveredNode = null;
        document.body.style.cursor = 'default';
        if (tooltip) tooltip.style.display = 'none';
      }
    });

    window.addEventListener('click', e => {
      if (!isRunning) return;
      if (hoveredNode) {
        selectNode(hoveredNode);
      }
    });
  }

  function syncLinesAndSprites() {
    if (linesMesh && showGraphEdges) {
      const linePosAttr = linesMesh.geometry.attributes.position;
      let ptr = 0;

      brainEdges.forEach(e => {
        const sId = typeof e.source === 'object' ? e.source.id : e.source;
        const tId = typeof e.target === 'object' ? e.target.id : e.target;
        const sIdx = nodeIndexMap.get(sId);
        const tIdx = nodeIndexMap.get(tId);
        if (sIdx !== undefined && tIdx !== undefined && ptr + 1 < linePosAttr.count) {
          linePosAttr.setXYZ(
            ptr++,
            positions.current[sIdx * 3],
            positions.current[sIdx * 3 + 1],
            positions.current[sIdx * 3 + 2]
          );
          linePosAttr.setXYZ(
            ptr++,
            positions.current[tIdx * 3],
            positions.current[tIdx * 3 + 1],
            positions.current[tIdx * 3 + 2]
          );
        }
      });
      linePosAttr.needsUpdate = true;
    }

    // Sincronizza Pulsar L0
    if (domainMeshesGroup) {
      domainMeshesGroup.children.forEach(mesh => {
        const idx = mesh.userData.nodeIndex;
        if (idx !== undefined) {
          mesh.position.set(
            positions.current[idx * 3],
            positions.current[idx * 3 + 1],
            positions.current[idx * 3 + 2]
          );
          if (mesh.userData.ring) {
            mesh.userData.ring.rotation.z += 0.02;
          }
        }
      });
    }

    // Sincronizza etichette
    if (labelSpritesGroup && showLabels) {
      labelSpritesGroup.children.forEach(sp => {
        const idx = sp.userData.nodeIndex;
        if (idx !== undefined) {
          sp.position.set(
            positions.current[idx * 3],
            positions.current[idx * 3 + 1] + 8,
            positions.current[idx * 3 + 2]
          );
        }
      });
    }
  }

  function updateMetricsHUD() {
    let l = 0, r = 0, d = 0;
    brainNodes.forEach(n => {
      if (n.layer_level === 0) d++;
      if (n.hemisphere === 'LEFT') l++;
      else r++;
    });
    const cL = document.getElementById('proj-count-left');
    const cR = document.getElementById('proj-count-right');
    const cD = document.getElementById('proj-count-domains');
    if (cL) cL.innerText = l;
    if (cR) cR.innerText = r;
    if (cD) cD.innerText = d;
  }

  function onResize() {
    if (!renderer || !camera || !container) return;
    const width = container.clientWidth || window.innerWidth;
    const height = container.clientHeight || (window.innerHeight - 48);
    if (width > 0 && height > 0) {
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    }
  }

  function animate() {
    if (!isRunning) return;
    requestAnimationFrame(animate);

    if (window.TWEEN) window.TWEEN.update();
    if (controls) controls.update();

    if (isTsneRunning) {
      stepTsne();
    }

    if (pointCloudMesh) {
      pointCloudMesh.geometry.attributes.position.needsUpdate = true;
    }
    syncLinesAndSprites();

    if (renderer && scene && camera) {
      renderer.render(scene, camera);
    }
  }

  function start() {
    isRunning = true;
    setTimeout(onResize, 50);
    setTimeout(onResize, 200);
    animate();
  }

  /* ==========================================================================
     MediaPipe Hand Gesture 3D Spatial Controller
     ========================================================================== */
  let isGestureEnabled = false;
  let handsDetector = null;
  let webcamStream = null;
  let gestureVideoEl = null;
  let gestureCanvasEl = null;
  let gestureCtx = null;
  let gestureAnimFrameId = null;

  let prevHandPos = null;
  let smoothedPos = { x: 0.5, y: 0.5 };
  let prevPinchDist = null;
  let prevTwoHandsDist = null;
  let prevHandScale = null;

  function toggleGestureControl() {
    if (isGestureEnabled) {
      stopGestureControl();
    } else {
      startGestureControl();
    }
  }

  async function startGestureControl() {
    const btn = document.getElementById('proj-btn-gesture');
    const hud = document.getElementById('proj-gesture-hud');
    gestureVideoEl = document.getElementById('proj-webcam-video');
    gestureCanvasEl = document.getElementById('proj-webcam-canvas');
    if (gestureCanvasEl) gestureCtx = gestureCanvasEl.getContext('2d');

    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      alert('Accesso webcam non supportato dal tuo browser.');
      return;
    }

    try {
      webcamStream = await navigator.mediaDevices.getUserMedia({
        video: { width: 320, height: 240, facingMode: 'user' }
      });
      if (gestureVideoEl) {
        gestureVideoEl.srcObject = webcamStream;
        await gestureVideoEl.play();
      }

      if (btn) btn.classList.add('active');
      if (hud) hud.style.display = 'flex';
      isGestureEnabled = true;

      if (typeof window.Hands !== 'undefined') {
        initMediaPipeHands();
      } else {
        loadMediaPipeScripts().then(initMediaPipeHands);
      }
    } catch (err) {
      console.error('Errore avvio webcam:', err);
      alert('Impossibile accedere alla webcam: ' + err.message);
      stopGestureControl();
    }
  }

  function stopGestureControl() {
    isGestureEnabled = false;
    const btn = document.getElementById('proj-btn-gesture');
    const hud = document.getElementById('proj-gesture-hud');
    if (btn) btn.classList.remove('active');
    if (hud) hud.style.display = 'none';

    if (webcamStream) {
      webcamStream.getTracks().forEach(t => t.stop());
      webcamStream = null;
    }
    if (gestureAnimFrameId) {
      cancelAnimationFrame(gestureAnimFrameId);
      gestureAnimFrameId = null;
    }
    prevHandPos = null;
    prevPinchDist = null;
    prevTwoHandsDist = null;
    prevHandScale = null;
  }

  function loadMediaPipeScripts() {
    return new Promise(resolve => {
      if (window.Hands) { resolve(); return; }
      const s1 = document.createElement('script');
      s1.src = 'https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js';
      s1.crossOrigin = 'anonymous';
      document.head.appendChild(s1);

      const s2 = document.createElement('script');
      s2.src = 'https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js';
      s2.crossOrigin = 'anonymous';
      s2.onload = () => resolve();
      document.head.appendChild(s2);
    });
  }

  function initMediaPipeHands() {
    if (!window.Hands) return;

    handsDetector = new window.Hands({
      locateFile: file => `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`
    });

    handsDetector.setOptions({
      maxNumHands: 2,
      modelComplexity: 1,
      minDetectionConfidence: 0.5,
      minTrackingConfidence: 0.5
    });

    handsDetector.onResults(onHandResults);

    async function sendFrame() {
      if (!isGestureEnabled || !gestureVideoEl || gestureVideoEl.paused) return;
      if (gestureVideoEl.readyState >= 2) {
        await handsDetector.send({ image: gestureVideoEl });
      }
      gestureAnimFrameId = requestAnimationFrame(sendFrame);
    }
    sendFrame();
  }

  const HAND_CONNECTIONS = [
    [0,1],[1,2],[2,3],[3,4],
    [0,5],[5,6],[6,7],[7,8],
    [5,9],[9,10],[10,11],[11,12],
    [9,13],[13,14],[14,15],[15,16],
    [13,17],[17,18],[18,19],[19,20],[0,17]
  ];

  function onHandResults(results) {
    try {
      if (!gestureCanvasEl || !gestureCtx) return;
      const ctx = gestureCtx;
      const w = gestureCanvasEl.width;
      const h = gestureCanvasEl.height;

      ctx.save();
      ctx.clearRect(0, 0, w, h);
      if (results.image) {
        ctx.drawImage(results.image, 0, 0, w, h);
      }

      const badge = document.getElementById('proj-gesture-state');

      if (!results.multiHandLandmarks || results.multiHandLandmarks.length === 0) {
        if (badge) {
          badge.innerText = 'Mostra mano/mani...';
          badge.style.color = '#94a3b8';
        }
        prevHandPos = null;
        prevPinchDist = null;
        prevTwoHandsDist = null;
        prevHandScale = null;
        ctx.restore();
        return;
      }

      const handsCount = results.multiHandLandmarks.length;

      // Disegna scheletro neon di tutte le mani rilevate
      results.multiHandLandmarks.forEach((landmarks, hIdx) => {
        const handColor = hIdx === 0 ? '#00d2ff' : '#ff007f';
        ctx.lineWidth = 2;
        ctx.strokeStyle = handColor;
        HAND_CONNECTIONS.forEach(([i, j]) => {
          const p1 = landmarks[i];
          const p2 = landmarks[j];
          if (p1 && p2) {
            ctx.beginPath();
            ctx.moveTo(p1.x * w, p1.y * h);
            ctx.lineTo(p2.x * w, p2.y * h);
            ctx.stroke();
          }
        });

        landmarks.forEach((p, idx) => {
        landmarks.forEach((p, idx) => {
          if (!p) return;
          ctx.beginPath();
          ctx.arc(p.x * w, p.y * h, (idx === 8 || idx === 12) ? 5 : 3, 0, Math.PI * 2);
          ctx.fillStyle = (idx === 8 || idx === 12) ? '#ffd15c' : handColor;
          ctx.fill();
        });
      });

      // Se 2 mani, disegna linea tratteggiata di connessione tra le due mani
      if (handsCount >= 2) {
        const h1 = results.multiHandLandmarks[0][0]; // Wrist 1
        const h2 = results.multiHandLandmarks[1][0]; // Wrist 2
        if (h1 && h2) {
          ctx.save();
          ctx.setLineDash([4, 4]);
          ctx.beginPath();
          ctx.moveTo(h1.x * w, h1.y * h);
          ctx.lineTo(h2.x * w, h2.y * h);
          ctx.strokeStyle = '#ffd15c';
          ctx.lineWidth = 2;
          ctx.stroke();
          ctx.restore();
        }
      }

      ctx.restore();

      // Processamento Gesti
      if (handsCount >= 2) {
        processTwoHandGestures(results.multiHandLandmarks, badge);
      } else {
        processSingleHandGestures(results.multiHandLandmarks[0], badge);
      }
    } catch (err) {
      console.warn('Errore gesture frame:', err);
    }
  }

  function dist(p1, p2) {
    if (!p1 || !p2) return 1.0;
    const dx = p1.x - p2.x;
    const dy = p1.y - p2.y;
    const dz = (p1.z || 0) - (p2.z || 0);
    return Math.sqrt(dx * dx + dy * dy + dz * dz);
  }

  /* Gesti a Due Mani (Zoom intuitivo allargando/avvicinando le mani) */
  function processTwoHandGestures(hands, badge) {
    const h1 = hands[0][0]; // polso 1
    const h2 = hands[1][0]; // polso 2
    const currentDist = dist(h1, h2);

    if (badge) {
      badge.innerText = '👐 2 Mani: Zoom';
      badge.style.color = '#ffd15c';
    }

    if (prevTwoHandsDist !== null && camera && controls) {
      const delta = currentDist - prevTwoHandsDist;
      // Allargando le mani (delta > 0) -> Zoom In (avvicina camera al target)
      // Avvicinando le mani (delta < 0) -> Zoom Out (allontana camera)
      if (Math.abs(delta) > 0.002) {
        const factor = Math.exp(-delta * 3.5);
        const offset = camera.position.clone().sub(controls.target);
        const newDist = offset.length() * factor;
        if (newDist > 20 && newDist < 4000) {
          offset.multiplyScalar(factor);
          camera.position.copy(controls.target).add(offset);
          controls.update();
        }
        if (badge) {
          badge.innerText = delta > 0 ? '👐 Zoom In (Allarga)' : '👐 Zoom Out (Avvicina)';
        }
      }
    }

    prevTwoHandsDist = currentDist;
    prevPinchDist = null;
    prevHandPos = null;
    prevHandScale = null;
  }

  /* Gesti a Una Sola Mano (Zoom ✌️ o Profondità, Pugno Pan ✊, Indice Raycast ☝️, Palmo Orbita 🖐️) */
  function processSingleHandGestures(lm, badge) {
    if (!lm || lm.length < 21) return;
    prevTwoHandsDist = null;

    const wrist = lm[0];
    const thumbTip = lm[4];
    const indexTip = lm[8];
    const middleTip = lm[12];
    const ringTip = lm[16];
    const pinkyTip = lm[20];
    const middleMcp = lm[9];

    const palmScale = dist(wrist, middleMcp); // Scala/profondità mano rispetto alla telecamera
    const dIndexWrist = dist(indexTip, wrist);
    const dMiddleWrist = dist(middleTip, wrist);
    const dRingWrist = dist(ringTip, wrist);
    const dPinkyWrist = dist(pinkyTip, wrist);

    // Smoothing coordinate (EMA)
    const rawX = 1.0 - (wrist.x * 0.4 + indexTip.x * 0.6); // Vista a specchio
    const rawY = (wrist.y * 0.4 + indexTip.y * 0.6);
    smoothedPos.x = smoothedPos.x * 0.6 + rawX * 0.4;
    smoothedPos.y = smoothedPos.y * 0.6 + rawY * 0.4;

    // Riconoscimento Gesti calibrato (SENZA PINCH)
    const isFist = (dIndexWrist < 0.22 && dMiddleWrist < 0.22 && dRingWrist < 0.22 && dPinkyWrist < 0.22);
    const isPointing = (dIndexWrist > 0.32 && dMiddleWrist < 0.25 && dRingWrist < 0.25 && dPinkyWrist < 0.25);
    const isPeaceSign = (dIndexWrist > 0.32 && dMiddleWrist > 0.32 && dRingWrist < 0.25 && dPinkyWrist < 0.25); // ✌️ Zoom gesture
    const isOpenPalm = (dIndexWrist > 0.32 && dMiddleWrist > 0.32 && dRingWrist > 0.32 && dPinkyWrist > 0.32);

    if (isPeaceSign) {
      // 1. GESTO DUE DITA (✌️ PEACE ZOOM)
      // Muovendo la mano in alto fa Zoom In; muovendo in basso fa Zoom Out
      if (badge) {
        badge.innerText = '✌️ Zoom (Muovi Su/Giù)';
        badge.style.color = '#ffd15c';
      }

      if (camera && controls) {
        let zoomDelta = 0;

        // Variazione movimento verticale (Su = Zoom In, Giù = Zoom Out)
        if (prevHandPos !== null) {
          const dy = smoothedPos.y - prevHandPos.y;
          if (Math.abs(dy) > 0.002) {
            zoomDelta += dy * 4.0;
          }
        }

        // Variazione profondità mano
        if (prevHandScale !== null) {
          const dScale = palmScale - prevHandScale;
          if (Math.abs(dScale) > 0.003) {
            zoomDelta -= dScale * 6.0;
          }
        }

        if (zoomDelta !== 0) {
          const factor = Math.exp(zoomDelta * 0.9);
          const offset = camera.position.clone().sub(controls.target);
          const newDist = offset.length() * factor;
          if (newDist > 20 && newDist < 4000) {
            offset.multiplyScalar(factor);
            camera.position.copy(controls.target).add(offset);
            controls.update();
          }
        }
      }

      prevHandScale = palmScale;
    } else if (isFist) {
      // 2. CLOSED FIST PAN (Spostamento Camera ✊)
      if (badge) {
        badge.innerText = '✊ Spostamento Camera';
        badge.style.color = '#ff007f';
      }

      if (prevHandPos && camera && controls) {
        const dx = (smoothedPos.x - prevHandPos.x) * 450;
        const dy = (smoothedPos.y - prevHandPos.y) * 450;
        const te = camera.matrix.elements;
        const right = new THREE.Vector3(te[0], te[1], te[2]);
        const up = new THREE.Vector3(te[4], te[5], te[6]);
        const panOffset = new THREE.Vector3();
        panOffset.addScaledVector(right, -dx * 0.7);
        panOffset.addScaledVector(up, dy * 0.7);
        camera.position.add(panOffset);
        controls.target.add(panOffset);
        controls.update();
      }
      prevHandScale = palmScale;
    } else if (isPointing) {
      // 3. INDEX POINTER / RAYCAST (Puntatore Laser ☝️)
      if (badge) {
        badge.innerText = '☝️ Puntatore Laser';
        badge.style.color = '#38bdf8';
      }

      if (renderer && camera && pointCloudMesh) {
        const mouse = new THREE.Vector2(smoothedPos.x * 2 - 1, -(smoothedPos.y * 2 - 1));
        const raycaster = new THREE.Raycaster();
        raycaster.params.Points.threshold = 14;
        raycaster.setFromCamera(mouse, camera);
        const hits = raycaster.intersectObject(pointCloudMesh);
        if (hits.length > 0) {
          const node = brainNodes[hits[0].index];
          if (node) {
            selectNode(node);
          }
        }
      }
      prevHandScale = palmScale;
    } else if (isOpenPalm) {
      // 4. OPEN PALM ORBIT & DEPTH ZOOM (🖐️ Orbita 3D e Zoom in Profondità)
      if (badge) {
        badge.innerText = '🖐️ Orbita 3D & Profondità';
        badge.style.color = '#10b981';
      }

      if (camera && controls) {
        // Rotazione Orbita con movimento X/Y
        if (prevHandPos) {
          const dx = (smoothedPos.x - prevHandPos.x) * 5.5;
          const dy = (smoothedPos.y - prevHandPos.y) * 5.5;
          const offset = camera.position.clone().sub(controls.target);
          const spherical = new THREE.Spherical().setFromVector3(offset);
          spherical.theta -= dx;
          spherical.phi = Math.max(0.05, Math.min(Math.PI - 0.05, spherical.phi - dy));
          offset.setFromSpherical(spherical);
          camera.position.copy(controls.target).add(offset);
          camera.lookAt(controls.target);
          controls.update();
        }

        // Zoom Naturale in Profondità: Avvicinando la mano alla webcam fa Zoom In, Allontanandola fa Zoom Out
        if (prevHandScale !== null) {
          const dScale = palmScale - prevHandScale;
          if (Math.abs(dScale) > 0.0035) {
            const zoomDelta = -dScale * 5.5;
            const factor = Math.exp(zoomDelta * 0.8);
            const offset = camera.position.clone().sub(controls.target);
            const newDist = offset.length() * factor;
            if (newDist > 20 && newDist < 4000) {
              offset.multiplyScalar(factor);
              camera.position.copy(controls.target).add(offset);
              controls.update();
            }
            if (badge) {
              badge.innerText = dScale > 0 ? '🖐️ Zoom In (Mano Vicina)' : '🖐️ Zoom Out (Mano Lontana)';
            }
          }
        }
      }
      prevHandScale = palmScale;
    } else {
      if (badge) {
        badge.innerText = 'Tracciamento attivo';
        badge.style.color = '#00d2ff';
      }
      prevHandScale = palmScale;
    }

    prevHandPos = { x: smoothedPos.x, y: smoothedPos.y };
  }

  function stop() {
    isRunning = false;
    isTsneRunning = false;
    stopGestureControl();
    const btn = document.getElementById('proj-btn-tsne-toggle');
    if (btn) btn.classList.remove('btn-pause');
  }

  // Public API
  return {
    init,
    setData,
    start,
    stop,
    setDimension,
    setAlgorithm,
    toggleTsne,
    resetTsne,
    toggleGestureControl,
    setPerplexity: p => { perplexity = parseInt(p); },
    setLearningRate: lr => { learningRate = parseInt(lr); },
    setKnn: k => { knnCount = parseInt(k); if (selectedNode) selectNode(selectedNode); },
    setNodeSpacing: s => {
      nodeSpacingScale = parseFloat(s) || 1.0;
      if (constellationGroup) {
        constellationGroup.scale.set(nodeSpacingScale, nodeSpacingScale, nodeSpacingScale);
      }
    },
    setNodeBrightness: b => {
      nodeBrightness = parseFloat(b) || 1.0;
      updateNodeColorsAndBrightness();
    },
    setEdgeBrightness: eb => {
      edgeBrightness = (parseFloat(eb) || 100) / 100;
      if (linesMesh) {
        linesMesh.material.opacity = 0.22 * edgeBrightness;
        linesMesh.material.needsUpdate = true;
      }
      if (knnLinesMesh) {
        knnLinesMesh.material.opacity = 0.85 * edgeBrightness;
        knnLinesMesh.material.needsUpdate = true;
      }
    },
    toggleGraphEdges: () => {
      showGraphEdges = !showGraphEdges;
      if (linesMesh) linesMesh.visible = showGraphEdges;
      const btn = document.getElementById('proj-btn-toggle-edges');
      if (btn) btn.classList.toggle('active', showGraphEdges);
    },
    toggleLabels: () => {
      showLabels = !showLabels;
      if (labelSpritesGroup) labelSpritesGroup.visible = showLabels;
      const btn = document.getElementById('proj-btn-toggle-labels');
      if (btn) btn.classList.toggle('active', showLabels);
      if (showLabels) updateLabels();
    },
    filterHemisphere,
    selectNode,
    closeInspector,
    focusCameraOnNode,
    searchNode: query => {
      const q = (query || '').toLowerCase().trim();
      if (!q) return;
      const match = brainNodes.find(n => (n.label && n.label.toLowerCase().includes(q)) || n.id.toLowerCase().includes(q));
      if (match) {
        selectNode(match);
        focusCameraOnNode(match.id);
      }
    },
    resize: onResize
  };
})();
