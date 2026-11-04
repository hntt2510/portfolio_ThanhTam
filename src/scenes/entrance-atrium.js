/**
 * Milestone 01B: Entrance Atrium Scene
 * Integrates Blender GLB model (entrance-atrium.glb) into Three.js world:
 *  - Native GLB architecture: circular floor, double-height curved walls, perimeter pilasters,
 *    mezzanine balcony with glass railing, stepped ceiling soffits, and 12-mullion oculus skylight.
 *  - Central installation: low circular pedestal plinth, blue LED halo ring, and three staggered
 *    frosted-glass monoliths with physical transmission, thickness, and aluminum frames.
 *  - Top-right curved corridor with cove lighting leading to future Profile Gallery.
 *  - High-resolution typography decals for Business Analysis, Enterprise Systems, and Technology Solutions.
 *  - Preserves approved Glass & Light Museum aesthetic and lighting language.
 */

import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

export class EntranceAtriumScene {
  constructor(onLoadedCallback = null) {
    this.group = new THREE.Group();
    this.materials = [];
    this.geometries = [];
    this.textures = [];
    this.onLoaded = onLoadedCallback;
    this.isLoaded = false;

    this.initColors();
    this.setupNaturalLighting();
    this.loadGlbModel();
  }

  initColors() {
    this.colors = {
      warmWhite: 0xF7F8F6,
      ivoryPlaster: 0xF3F4F1,
      pureWhite: 0xFFFFFF,
      lightSilver: 0xE8EBED,
      iceBlue: 0xD7E8F6,
      steelBlue: 0x6F9EC8,
      graphite: 0x263640,
      lightStone: 0xEDEDE9,
      aluminum: 0xD4DBE0,
      skyLight: 0xDCEBFA
    };
  }

  setupNaturalLighting() {
    // 1. Ambient baseline light for pristine, non-muddy architectural surfaces
    const ambientLight = new THREE.AmbientLight(0xFFFDF8, 0.45);
    this.group.add(ambientLight);

    // 2. Natural sunlight pouring through circular oculus skylight
    const daylight = new THREE.DirectionalLight(0xFFFFFF, 2.6);
    daylight.position.set(3.0, 18.0, 5.0);
    daylight.castShadow = true;
    daylight.shadow.mapSize.width = 2048;
    daylight.shadow.mapSize.height = 2048;
    daylight.shadow.camera.near = 1.0;
    daylight.shadow.camera.far = 32.0;
    daylight.shadow.camera.left = -9;
    daylight.shadow.camera.right = 9;
    daylight.shadow.camera.top = 9;
    daylight.shadow.camera.bottom = -9;
    daylight.shadow.bias = -0.0003;
    daylight.shadow.normalBias = 0.02;
    this.group.add(daylight);

    // 3. Soft sky ambient fill
    const hemiLight = new THREE.HemisphereLight(this.colors.skyLight, 0xF5F2ED, 0.50);
    hemiLight.position.set(0, 14, 0);
    this.group.add(hemiLight);

    // 4. Subtle accent point light near monolith installation for soft glass specular highlights
    const glassLight = new THREE.PointLight(this.colors.iceBlue, 0.9, 14);
    glassLight.position.set(1.4, 3.2, 2.2);
    this.group.add(glassLight);

    // 5. Warm ambient fill light inside corridor for transition vista (K04)
    const corridorLight = new THREE.PointLight(0xFDF7EE, 0.8, 14);
    corridorLight.position.set(8.5, 2.5, -8.5);
    this.group.add(corridorLight);

    // 6. Sky backdrop disc above circular skylight
    const skyGeo = new THREE.CircleGeometry(9.0, 32);
    this.geometries.push(skyGeo);
    const skyMat = new THREE.MeshBasicMaterial({ color: 0xCFE5F8, side: THREE.DoubleSide });
    this.materials.push(skyMat);
    const skyDisc = new THREE.Mesh(skyGeo, skyMat);
    skyDisc.rotation.x = Math.PI / 2;
    skyDisc.position.set(0, 13.0, 0);
    this.group.add(skyDisc);
  }

  loadGlbModel() {
    const loader = new GLTFLoader();
    const primaryPath = './design-handoff/milestone-01A/entrance-atrium.glb';
    const fallbackPath = './assets/models/entrance-atrium.glb';

    const loadAsset = (url, isFallback = false) => {
      loader.load(
        url,
        (gltf) => {
          this.processLoadedModel(gltf);
          this.isLoaded = true;
          if (this.onLoaded) {
            this.onLoaded();
          }
        },
        undefined,
        (err) => {
          console.warn(`Failed loading GLB from ${url}:`, err);
          if (!isFallback) {
            console.info(`Attempting fallback from ${fallbackPath}...`);
            loadAsset(fallbackPath, true);
          } else {
            console.error('All GLB loading attempts failed. Retaining basic lighting.');
          }
        }
      );
    };

    loadAsset(primaryPath);
  }

  processLoadedModel(gltf) {
    const root = gltf.scene;

    // Premium Frosted Glass Material:
    // Uses physical clearcoat + translucency for bright, luminous architectural frosted glass
    const frostedGlassMat = new THREE.MeshPhysicalMaterial({
      color: new THREE.Color(0xF0F7FD),
      transparent: true,
      opacity: 0.65,
      roughness: 0.22,
      metalness: 0.06,
      clearcoat: 1.0,
      clearcoatRoughness: 0.12,
      reflectivity: 0.85,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.materials.push(frostedGlassMat);

    const skylightGlassMat = new THREE.MeshPhysicalMaterial({
      color: new THREE.Color(0xEEF6FD),
      transparent: true,
      opacity: 0.70,
      roughness: 0.12,
      metalness: 0.05,
      clearcoat: 1.0,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.materials.push(skylightGlassMat);

    const railingGlassMat = new THREE.MeshPhysicalMaterial({
      color: new THREE.Color(0xEDF5FB),
      transparent: true,
      opacity: 0.60,
      roughness: 0.10,
      metalness: 0.05,
      clearcoat: 1.0,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.materials.push(railingGlassMat);

    const coveLightMat = new THREE.MeshBasicMaterial({
      color: new THREE.Color(0xFFFDF8)
    });
    this.materials.push(coveLightMat);

    const haloMat = new THREE.MeshBasicMaterial({
      color: new THREE.Color(0x6F9EC8),
      transparent: true,
      opacity: 0.80
    });
    this.materials.push(haloMat);

    // Panel configs for typography decals
    const panelConfigs = {
      'ATR_GlassPanel_01': {
        w: 2.20,
        h: 1.35,
        d: 0.14,
        num: '01',
        title: 'BUSINESS ANALYSIS',
        subtitle: 'REQUIREMENTS · AS-IS / TO-BE · WORKFLOWS'
      },
      'ATR_GlassPanel_02': {
        w: 1.90,
        h: 3.00,
        d: 0.14,
        num: '02',
        title: 'ENTERPRISE SYSTEMS',
        subtitle: 'SAP ABAP · ARCHITECTURE · AUDIT TRAIL'
      },
      'ATR_GlassPanel_03': {
        w: 1.60,
        h: 2.10,
        d: 0.14,
        num: '03',
        title: 'TECHNOLOGY SOLUTIONS',
        subtitle: 'FULL-STACK · CLOUD · INTEGRATION'
      }
    };

    const pendingDecals = [];

    root.traverse((child) => {
      if (!child.isMesh) return;

      const name = child.name;

      // 1. Frosted Glass Monoliths
      if (name === 'ATR_GlassPanel_01' || name === 'ATR_GlassPanel_02' || name === 'ATR_GlassPanel_03') {
        child.material = frostedGlassMat;
        child.castShadow = false; // Translucent glass does not cast solid black shadow
        child.receiveShadow = true;

        const cfg = panelConfigs[name];
        if (cfg) {
          pendingDecals.push({ mesh: child, cfg });
        }
      }
      // Hide solid blocking frame cubes from graybox (delicate frame is rendered via decal & shoes)
      else if (name.includes('_Frame')) {
        child.visible = false;
      }
      // 2. Skylight Glass Dome
      else if (name === 'ATR_SkylightGlass') {
        child.material = skylightGlassMat;
      }
      // 3. Mezzanine Railing Glass
      else if (name === 'ATR_MezzanineRailingGlass') {
        child.material = railingGlassMat;
      }
      // 4. Floor Halo Accent Ring
      else if (name === 'ATR_FloorHalo') {
        child.material = haloMat;
      }
      // 5. Architectural Cove Lights
      else if (name === 'ATR_CeilingCoveLight' || name === 'ATR_CorridorCoveLight') {
        child.material = coveLightMat;
      }
      // 6. Floor & Pedestal
      else if (name === 'ATR_Floor' || name === 'ATR_CorridorFloor') {
        child.receiveShadow = true;
        if (child.material) {
          child.material.color.setHex(0xF4F5F2);
          child.material.roughness = 0.40;
          child.material.metalness = 0.04;
        }
      }
      else if (name === 'ATR_Pedestal') {
        child.receiveShadow = true;
        child.castShadow = true;
        if (child.material) {
          child.material.color.setHex(0xF7F8F5);
          child.material.roughness = 0.42;
          child.material.metalness = 0.04;
        }
      }
      // 7. Brushed Aluminum Trims, Rings, Mullions & Shoes (tuned for web PBR without dark reflection)
      else if (
        name.includes('Trim') ||
        name.includes('Mullion') ||
        name.includes('Ring') ||
        name.includes('MountShoe') ||
        name.includes('Joint') ||
        name.includes('Handrail') ||
        name.includes('Portal')
      ) {
        child.castShadow = true;
        child.receiveShadow = true;
        if (child.material) {
          child.material.color.setHex(0xE2E7EC);
          child.material.metalness = 0.25;
          child.material.roughness = 0.35;
        }
      }
      // 8. Architecture (Walls, Pilasters, Soffits, Portals)
      else {
        child.castShadow = true;
        child.receiveShadow = true;
        if (child.material) {
          child.material.color.setHex(0xF8F9F7);
          child.material.roughness = 0.85;
          child.material.metalness = 0.02;
        }
      }
    });

    this.group.add(root);
    this.group.updateMatrixWorld(true);

    // Build unscaled decals attached to world scene to preserve exact typography aspect ratio
    pendingDecals.forEach(({ mesh, cfg }) => {
      const worldPos = new THREE.Vector3();
      const worldQuat = new THREE.Quaternion();
      mesh.getWorldPosition(worldPos);
      mesh.getWorldQuaternion(worldQuat);

      // Front Decal
      const frontDecal = this.buildDecal(cfg);
      frontDecal.position.copy(worldPos);
      frontDecal.quaternion.copy(worldQuat);
      frontDecal.translateZ(cfg.d / 2 + 0.006);
      this.group.add(frontDecal);

      // Back Decal (for reverse inspection)
      const backDecal = this.buildDecal(cfg);
      backDecal.position.copy(worldPos);
      backDecal.quaternion.copy(worldQuat);
      backDecal.translateZ(-(cfg.d / 2 + 0.006));
      backDecal.rotateY(Math.PI);
      this.group.add(backDecal);
    });
  }

  buildDecal(cfg) {
    const canvas = document.createElement('canvas');
    canvas.width = 1024;
    canvas.height = Math.round(1024 * (cfg.h / cfg.w));
    const ctx = canvas.getContext('2d');

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Clean subtle frame line
    ctx.strokeStyle = 'rgba(111, 158, 200, 0.38)';
    ctx.lineWidth = 3;
    ctx.strokeRect(36, 36, canvas.width - 72, canvas.height - 72);

    // Number tag
    ctx.fillStyle = '#4D82AF';
    ctx.font = '600 36px "IBM Plex Mono", monospace';
    ctx.fillText(`— ${cfg.num} —`, 72, 120);

    // Title
    ctx.fillStyle = '#202E38';
    ctx.font = '700 44px "Manrope", sans-serif';
    ctx.fillText(cfg.title, 72, 195);

    // Divider line
    ctx.strokeStyle = 'rgba(38, 54, 64, 0.28)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(72, 230);
    ctx.lineTo(canvas.width - 72, 230);
    ctx.stroke();

    // Subtitle
    ctx.fillStyle = '#4B5E6B';
    ctx.font = '500 23px "IBM Plex Mono", monospace';
    ctx.fillText(cfg.subtitle, 72, 280);

    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    texture.anisotropy = 8;
    this.textures.push(texture);

    const planeGeo = new THREE.PlaneGeometry(cfg.w * 0.90, cfg.h * 0.90);
    this.geometries.push(planeGeo);
    const planeMat = new THREE.MeshBasicMaterial({
      map: texture,
      transparent: true,
      opacity: 0.95,
      depthWrite: false
    });
    this.materials.push(planeMat);

    return new THREE.Mesh(planeGeo, planeMat);
  }

  dispose() {
    this.textures.forEach(t => t.dispose());
    this.geometries.forEach(g => g.dispose());
    this.materials.forEach(m => m.dispose());
  }
}
