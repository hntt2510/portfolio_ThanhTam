/**
 * Milestone 02D: Profile Gallery Scene (Glass & Light Museum)
 * High-fidelity WebGL realization:
 *  - Luminous double-height architectural curtain glazing with slim silver mullions (3.5cm) and transoms.
 *  - Polished warm travertine stone floor with soft ambient sheen and daylight highlights.
 *  - Sculpted architectural threshold portal at exit with semicircular archway and daylit vestibule alcove.
 *  - Multi-scale botanical garden terrace outside: organic branching trees, multifaceted leaf lobes,
 *    manicured boxwood hedges, stone curbs, lawn, and distant sky backdrop.
 *  - Warm white plaster walls, curved ceiling vault, and glowing LED cove wash.
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
      warmWhite: 0xF9F9F6,
      ivoryPlaster: 0xF7F7F4,
      pureWhite: 0xFFFFFF,
      lightSilver: 0xEEF3F8,
      iceBlue: 0xD7E8F6,
      steelBlue: 0x6F9EC8,
      graphite: 0x263640,
      lightStone: 0xF6F5F0,
      aluminum: 0xEEF3F8,
      skyLight: 0xDCEBFA,
      hedgeGreen: 0x3D662E,
      foliageSun: 0x58883E,
      foliageDeep: 0x365922,
      lawnGreen: 0x689448,
      curbStone: 0xE8E7E2,
      trunkBrown: 0x4E4237,
      skyBackdrop: 0xBCE0FD
    };
  }

  setupGalleryLighting() {
    // 1. Natural sunlight streaming obliquely through the glazed facade
    const gallerySun = new THREE.DirectionalLight(0xFFFAF0, 2.8);
    gallerySun.position.set(28.0, 22.0, -36.0);
    gallerySun.target.position.set(26.0, 0, -22.0);
    gallerySun.castShadow = true;
    gallerySun.shadow.mapSize.width = 2048;
    gallerySun.shadow.mapSize.height = 2048;
    gallerySun.shadow.camera.near = 1.0;
    gallerySun.shadow.camera.far = 52.0;
    gallerySun.shadow.camera.left = -22;
    gallerySun.shadow.camera.right = 22;
    gallerySun.shadow.camera.top = 22;
    gallerySun.shadow.camera.bottom = -22;
    gallerySun.shadow.bias = -0.0003;
    gallerySun.shadow.normalBias = 0.02;
    this.group.add(gallerySun);
    this.group.add(gallerySun.target);

    // 2. Soft sky daylight hemisphere ambient
    const galleryHemi = new THREE.HemisphereLight(this.colors.skyLight, 0xF5F2EB, 0.65);
    galleryHemi.position.set(26.0, 14.0, -22.0);
    this.group.add(galleryHemi);

    // 3. Warm cove fill lights placed along the gallery curve for soft architectural ceiling wash
    const coveLight1 = new THREE.PointLight(0xFFF7EC, 0.90, 18);
    coveLight1.position.set(20.0, 4.7, -18.0);
    this.group.add(coveLight1);

    const coveLight2 = new THREE.PointLight(0xFFF7EC, 0.90, 18);
    coveLight2.position.set(30.0, 4.7, -22.0);
    this.group.add(coveLight2);

    const coveLight3 = new THREE.PointLight(0xFFF7EC, 0.90, 18);
    coveLight3.position.set(38.0, 4.7, -20.5);
    this.group.add(coveLight3);

    // 4. Inviting daylight accent radiating from the sculpted exit vestibule alcove (K08)
    const portalDaylight = new THREE.PointLight(0xFFFBF2, 1.4, 16);
    portalDaylight.position.set(43.5, 3.2, -19.8);
    this.group.add(portalDaylight);
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

    // 1. Premium Architectural Clear Glazing
    const curtainGlassMat = new THREE.MeshPhysicalMaterial({
      color: new THREE.Color(0xF2F7FC),
      transparent: true,
      opacity: 0.22,
      roughness: 0.02,
      metalness: 0.02,
      transmission: 0.98,
      ior: 1.52,
      clearcoat: 1.0,
      clearcoatRoughness: 0.03,
      reflectivity: 0.94,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.materials.push(curtainGlassMat);

    // 2. Bright Brushed Silver Aluminum for Mullions & Transoms
    const aluminumMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.aluminum),
      roughness: 0.22,
      metalness: 0.75
    });
    this.materials.push(aluminumMat);

    // 3. Warm Plaster Wall & Ceiling Material
    const plasterMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.warmWhite),
      roughness: 0.85,
      metalness: 0.0
    });
    this.materials.push(plasterMat);

    // 4. Polished Warm Travertine Stone Floor with Soft Daylight Specular Sheen
    const stoneFloorMat = new THREE.MeshPhysicalMaterial({
      color: new THREE.Color(this.colors.lightStone),
      roughness: 0.18,
      metalness: 0.02,
      clearcoat: 0.50,
      clearcoatRoughness: 0.20,
      reflectivity: 0.70
    });
    this.materials.push(stoneFloorMat);

    // 5. Glowing Architectural Cove Light Channel
    const coveGlowMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(0xFFF7EC),
      emissive: new THREE.Color(0xFFF7EC),
      emissiveIntensity: 4.2,
      toneMapped: false
    });
    this.materials.push(coveGlowMat);

    // 6. Outdoor Garden Landscape Materials
    const foliageSunMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.foliageSun),
      roughness: 0.65,
      metalness: 0.0
    });
    this.materials.push(foliageSunMat);

    const foliageDeepMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.foliageDeep),
      roughness: 0.70,
      metalness: 0.0
    });
    this.materials.push(foliageDeepMat);

    const hedgeMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.hedgeGreen),
      roughness: 0.75,
      metalness: 0.0
    });
    this.materials.push(hedgeMat);

    const lawnMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.lawnGreen),
      roughness: 0.85,
      metalness: 0.0
    });
    this.materials.push(lawnMat);

    const curbMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.curbStone),
      roughness: 0.35,
      metalness: 0.05
    });
    this.materials.push(curbMat);

    const trunkMat = new THREE.MeshStandardMaterial({
      color: new THREE.Color(this.colors.trunkBrown),
      roughness: 0.85,
      metalness: 0.0
    });
    this.materials.push(trunkMat);

    const skyBackdropMat = new THREE.MeshBasicMaterial({
      color: new THREE.Color(this.colors.skyBackdrop),
      side: THREE.DoubleSide
    });
    this.materials.push(skyBackdropMat);

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
        } else if (name.includes('InnerWall') || name.includes('Ceiling') || name.includes('Portal') || name.includes('Vestibule')) {
          node.material = plasterMat;
          node.receiveShadow = true;
          node.castShadow = true;
        } else if (name.includes('CoveLight')) {
          node.material = coveGlowMat;
          node.castShadow = false;
          node.receiveShadow = false;
        } else if (name.includes('Bench')) {
          node.material = stoneFloorMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('BoxwoodHedge') || name.includes('Hedge')) {
          node.material = hedgeMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('GardenCurb') || name.includes('Curb')) {
          node.material = curbMat;
          node.receiveShadow = true;
          node.castShadow = false;
        } else if (name.includes('GardenLawn') || name.includes('LandscapeGround') || name.includes('Lawn')) {
          node.material = lawnMat;
          node.receiveShadow = true;
          node.castShadow = false;
        } else if (name.includes('Canopy_0')) {
          node.material = foliageDeepMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('Canopy')) {
          node.material = foliageSunMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('Trunk')) {
          node.material = trunkMat;
          node.castShadow = true;
          node.receiveShadow = true;
        } else if (name.includes('SkyBackdrop')) {
          node.material = skyBackdropMat;
          node.castShadow = false;
          node.receiveShadow = false;
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
