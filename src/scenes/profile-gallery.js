/**
 * Milestone 02C: Profile Gallery Scene (Glass & Light Museum)
 * High-fidelity WebGL realization:
 *  - Luminous double-height architectural curtain glazing with horizontal transoms and slim silver mullions.
 *  - Polished warm travertine stone floor with soft daylight highlights.
 *  - Warm white plaster walls, curved ceiling vault, and glowing LED cove light wash.
 *  - Sunlit botanical garden terrace outside with manicured hedges, canopy trees, and lawn.
 *  - Flush arched exit portal to Scene 03 (no hanging obstruction).
 *  - 100% background architecture: strictly zero 3D text or floating info plaques.
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
      warmWhite: 0xF8F9F6,
      ivoryPlaster: 0xF7F7F4,
      pureWhite: 0xFFFFFF,
      lightSilver: 0xE8EFF5,
      iceBlue: 0xD7E8F6,
      steelBlue: 0x6F9EC8,
      graphite: 0x263640,
      lightStone: 0xF2F1EC,
      aluminum: 0xE4EBF0,
      skyLight: 0xE2EEFA,
      hedgeGreen: 0x547A4A,
      treeGreen: 0x6E9160,
      lawnGreen: 0x82A374,
      trunkBrown: 0x584E44
    };
  }

  setupGalleryLighting() {
    // 1. Natural sunlight streaming obliquely through the glazed facade
    const gallerySun = new THREE.DirectionalLight(0xFFFAF0, 2.4);
    gallerySun.position.set(28.0, 18.0, -34.0);
    gallerySun.target.position.set(26.0, 0, -22.0);
    gallerySun.castShadow = true;
    gallerySun.shadow.mapSize.width = 2048;
    gallerySun.shadow.mapSize.height = 2048;
    gallerySun.shadow.camera.near = 1.0;
    gallerySun.shadow.camera.far = 48.0;
    gallerySun.shadow.camera.left = -18;
    gallerySun.shadow.camera.right = 18;
    gallerySun.shadow.camera.top = 18;
    gallerySun.shadow.camera.bottom = -18;
    gallerySun.shadow.bias = -0.0003;
    gallerySun.shadow.normalBias = 0.02;
    this.group.add(gallerySun);
    this.group.add(gallerySun.target);

    // 2. Soft sky daylight hemisphere ambient
    const galleryHemi = new THREE.HemisphereLight(this.colors.skyLight, 0xF5F2EB, 1.25);
    galleryHemi.position.set(26.0, 14.0, -22.0);
    this.group.add(galleryHemi);

    // 3. Warm cove fill lights placed along the gallery curve for soft architectural ceiling wash
    const coveLight1 = new THREE.PointLight(0xFFF7EC, 0.85, 20);
    coveLight1.position.set(20.0, 4.6, -18.0);
    this.group.add(coveLight1);

    const coveLight2 = new THREE.PointLight(0xFFF7EC, 0.85, 20);
    coveLight2.position.set(30.0, 4.6, -22.0);
    this.group.add(coveLight2);

    const coveLight3 = new THREE.PointLight(0xFFF7EC, 0.85, 20);
    coveLight3.position.set(38.0, 4.6, -20.5);
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

    // Premium Architectural Clear Glazing
    const curtainGlassMat = new THREE.MeshPhysicalMaterial({
      color: new THREE.Color(0xF2F7FC),
      transparent: true,
      opacity: 0.28,
      roughness: 0.02,
      metalness: 0.05,
      transmission: 0.96,
      ior: 1.52,
      clearcoat: 1.0,
      clearcoatRoughness: 0.04,
      reflectivity: 0.92,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.materials.push(curtainGlassMat);

    // Bright Brushed Silver Aluminum for Mullions & Transoms
    const aluminumMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.aluminum),
      roughness: 0.18,
      metalness: 0.85
    });
    this.materials.push(aluminumMat);

    // Warm Plaster Wall & Ceiling Material
    const plasterMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.warmWhite),
      roughness: 0.88,
      metalness: 0.0
    });
    this.materials.push(plasterMat);

    // Polished Warm Travertine/Stone Floor & Benches
    const stoneFloorMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.lightStone),
      roughness: 0.26,
      metalness: 0.02
    });
    this.materials.push(stoneFloorMat);

    // Glowing Architectural Cove Light Channel
    const coveGlowMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(0xFFF8EE),
      emissive: new THREE.Color(0xFFF8EE),
      emissiveIntensity: 3.2,
      toneMapped: false
    });
    this.materials.push(coveGlowMat);

    // Outdoor Garden Landscape Materials
    const hedgeMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.hedgeGreen),
      roughness: 0.82,
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
      roughness: 0.76,
      metalness: 0.0
    });
    this.materials.push(treeMat);

    const trunkMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.trunkBrown),
      roughness: 0.85,
      metalness: 0.0
    });
    this.materials.push(trunkMat);

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
        } else if (name.includes('InnerWall') || name.includes('Ceiling') || name.includes('Portal')) {
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
        } else if (name.includes('TreeCanopy') || name.includes('Sphere')) {
          node.material = treeMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('TreeTrunk') || name.includes('Cylinder')) {
          node.material = trunkMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else {
          // Mullions, Transoms, Sills, Trims
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
