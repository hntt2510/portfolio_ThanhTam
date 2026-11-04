/**
 * Milestone 02B: Profile Gallery Scene
 * Integrates Blender GLB model (profile-gallery.glb) into Three.js world:
 *  - Native GLB architecture: curved stone promenade floor, continuous plaster inner wall,
 *    curved double-height glass curtain wall with vertical aluminum mullions, cove ceiling,
 *    threshold portal archway to Scene 03, and exterior garden landscape.
 *  - Seamless physical continuity with Scene 01's north-east corridor portal at (15, 0, -15).
 *  - Premium MeshPhysicalMaterial for clear architectural glazing with subtle sky reflections.
 *  - PBR stone floor, white plaster, brushed aluminum, and soft LED cove glow.
 *  - Strictly background architecture: zero 3D text/panels in WebGL. All biographical copy
 *    lives in the HTML/CSS DOM layer.
 */

import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

export class ProfileGalleryScene {
  constructor(onLoadedCallback = null) {
    this.group = new THREE.Group();
    this.materials = [];
    this.geometries = [];
    this.textures = [];
    this.onLoaded = onLoadedCallback;
    this.isLoaded = false;

    this.initColors();
    this.setupGalleryLighting();
    this.loadGlbModel();
  }

  initColors() {
    this.colors = {
      warmWhite: 0xF7F8F6,
      ivoryPlaster: 0xF4F5F2,
      pureWhite: 0xFFFFFF,
      lightSilver: 0xE8EBED,
      iceBlue: 0xD7E8F6,
      steelBlue: 0x6F9EC8,
      graphite: 0x263640,
      lightStone: 0xF0EFEA,
      aluminum: 0xD8DFE5,
      skyLight: 0xDCEBFA,
      hedgeGreen: 0x6E8569,
      treeGreen: 0x8FA489,
      lawnGreen: 0x9CB396
    };
  }

  setupGalleryLighting() {
    // 1. Natural sunlight streaming through curtain wall glazing
    const gallerySun = new THREE.DirectionalLight(0xFFFDF8, 2.0);
    gallerySun.position.set(28.0, 16.0, -32.0);
    gallerySun.target.position.set(26.0, 0, -22.0);
    gallerySun.castShadow = true;
    gallerySun.shadow.mapSize.width = 2048;
    gallerySun.shadow.mapSize.height = 2048;
    gallerySun.shadow.camera.near = 1.0;
    gallerySun.shadow.camera.far = 45.0;
    gallerySun.shadow.camera.left = -18;
    gallerySun.shadow.camera.right = 18;
    gallerySun.shadow.camera.top = 18;
    gallerySun.shadow.camera.bottom = -18;
    gallerySun.shadow.bias = -0.0003;
    gallerySun.shadow.normalBias = 0.02;
    this.group.add(gallerySun);
    this.group.add(gallerySun.target);

    // 2. Soft sky daylight hemisphere ambient
    const galleryHemi = new THREE.HemisphereLight(this.colors.skyLight, 0xF5F2ED, 1.1);
    galleryHemi.position.set(26.0, 12.0, -22.0);
    this.group.add(galleryHemi);

    // 3. Warm cove fill lights placed along the gallery curve for soft architectural wash
    const coveLight1 = new THREE.PointLight(0xFFF9EE, 0.75, 18);
    coveLight1.position.set(20.0, 4.5, -18.0);
    this.group.add(coveLight1);

    const coveLight2 = new THREE.PointLight(0xFFF9EE, 0.75, 18);
    coveLight2.position.set(30.0, 4.5, -22.0);
    this.group.add(coveLight2);

    const coveLight3 = new THREE.PointLight(0xFFF9EE, 0.75, 18);
    coveLight3.position.set(38.0, 4.5, -20.5);
    this.group.add(coveLight3);
  }

  loadGlbModel() {
    const loader = new GLTFLoader();
    const primaryPath = './design-handoff/milestone-02/profile-gallery.glb';
    const fallbackPath = './assets/models/profile-gallery.glb';

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
            console.error('All Profile Gallery GLB loading attempts failed.');
          }
        }
      );
    };

    loadAsset(primaryPath);
  }

  processLoadedModel(gltf) {
    const root = gltf.scene;

    // Premium Architectural Clear Glazing Material
    const curtainGlassMat = new THREE.MeshPhysicalMaterial({
      color: new THREE.Color(0xF0F6FB),
      transparent: true,
      opacity: 0.35,
      roughness: 0.05,
      metalness: 0.05,
      clearcoat: 1.0,
      clearcoatRoughness: 0.08,
      reflectivity: 0.90,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.materials.push(curtainGlassMat);

    // Brushed Aluminum for Mullions, Sills, and Threshold Arch
    const aluminumMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.aluminum),
      roughness: 0.28,
      metalness: 0.85
    });
    this.materials.push(aluminumMat);

    // Warm Plaster Wall & Ceiling Material
    const plasterMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.ivoryPlaster),
      roughness: 0.88,
      metalness: 0.0
    });
    this.materials.push(plasterMat);

    // Polished Light Stone Floor & Benches
    const stoneFloorMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.lightStone),
      roughness: 0.35,
      metalness: 0.02
    });
    this.materials.push(stoneFloorMat);

    // Glowing Architectural Cove Light Channel
    const coveGlowMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(0xFFFBF2),
      emissive: new THREE.Color(0xFFFBF2),
      emissiveIntensity: 2.2,
      toneMapped: false
    });
    this.materials.push(coveGlowMat);

    // Outdoor Garden Landscape Materials
    const hedgeMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.hedgeGreen),
      roughness: 0.80,
      metalness: 0.0
    });
    this.materials.push(hedgeMat);

    const lawnMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.lawnGreen),
      roughness: 0.88,
      metalness: 0.0
    });
    this.materials.push(lawnMat);

    const treeMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.treeGreen),
      roughness: 0.78,
      metalness: 0.0
    });
    this.materials.push(treeMat);

    // Traverse and assign materials with shadow configuration
    root.traverse((node) => {
      if (node.isMesh) {
        this.geometries.push(node.geometry);
        const name = node.name || '';

        if (name.includes('OuterCurtainWall_Glass')) {
          node.material = curtainGlassMat;
          node.castShadow = false;
          node.receiveShadow = false;
        } else if (name.includes('Floor')) {
          node.material = stoneFloorMat;
          node.receiveShadow = true;
          node.castShadow = false;
        } else if (name.includes('InnerWall') || name.includes('Ceiling')) {
          node.material = plasterMat;
          node.receiveShadow = true;
          node.castShadow = false;
        } else if (name.includes('CoveLight')) {
          node.material = coveGlowMat;
          node.castShadow = false;
          node.receiveShadow = false;
        } else if (name.includes('Bench')) {
          node.material = stoneFloorMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('HedgeRow')) {
          node.material = hedgeMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('LandscapeGround')) {
          node.material = lawnMat;
          node.receiveShadow = true;
          node.castShadow = false;
        } else if (name.includes('Icosphere')) {
          node.material = treeMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else {
          // Framing: Mullions, Sills, Threshold Posts & Header
          node.material = aluminumMat;
          node.castShadow = true;
          node.receiveShadow = true;
        }
      }
    });

    this.group.add(root);
  }

  dispose() {
    this.materials.forEach(m => m.dispose && m.dispose());
    this.geometries.forEach(g => g.dispose && g.dispose());
    this.textures.forEach(t => t.dispose && t.dispose());
  }
}
