/**
 * Milestone 01: Entrance Atrium Scene
 * Faithful to Glass & Light Museum Specification & Reference Boards:
 *  - Circular Atrium with stepped ceiling cove lighting
 *  - Grand circular domed skylight overhead casting natural daylight
 *  - Curved two-tier architectural walls with rhythmic vertical pilasters
 *  - Polished light-stone floor with soft reflections and ambient expansion joints
 *  - Central installation: low circular stone pedestal, subtle LED halo ring,
 *    and three monolithic frosted-glass blocks with crystal-clear refractive edges
 *  - Top-right curved corridor leading to future Profile Gallery (Wayfinding 04)
 */

import * as THREE from 'three';

export class EntranceAtriumScene {
  constructor() {
    this.group = new THREE.Group();
    this.materials = [];
    this.geometries = [];
    this.textures = [];

    this.initColors();
    this.buildAtriumStructure();
    this.buildSkylightAndCeiling();
    this.buildCentralInstallation();
    this.buildCorridorPortal();
    this.setupNaturalLighting();
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

  buildAtriumStructure() {
    // 1. Polished light-stone floor
    const floorR = 22;
    const floorGeo = new THREE.CylinderGeometry(floorR, floorR, 0.4, 64);
    this.geometries.push(floorGeo);
    const floorMat = new THREE.MeshStandardMaterial({
      color: this.colors.lightStone,
      roughness: 0.38, // Realistic soft stone sheen
      metalness: 0.08
    });
    this.materials.push(floorMat);
    const floor = new THREE.Mesh(floorGeo, floorMat);
    floor.position.y = -0.2;
    floor.receiveShadow = true;
    this.group.add(floor);

    // Subtle concentric stone joint rings on the floor
    const jointMat = new THREE.MeshBasicMaterial({ color: 0xD9DDD7 });
    this.materials.push(jointMat);
    [5.5, 9.0, 13.0, 17.0].forEach(r => {
      const ringGeo = new THREE.RingGeometry(r - 0.02, r + 0.02, 64);
      this.geometries.push(ringGeo);
      const ringMesh = new THREE.Mesh(ringGeo, jointMat);
      ringMesh.rotation.x = -Math.PI / 2;
      ringMesh.position.y = 0.005;
      this.group.add(ringMesh);
    });

    // 2. Curved Atrium Walls (Double-height museum cylinder)
    const atriumR = 15.5;
    const wallH = 10.5;
    const wallMat = new THREE.MeshStandardMaterial({
      color: this.colors.ivoryPlaster,
      roughness: 0.85,
      metalness: 0.02,
      side: THREE.BackSide
    });
    this.materials.push(wallMat);

    // Wall with opening for exit corridor at angle ~30° to 55° (top-right)
    const wallGeo = new THREE.CylinderGeometry(
      atriumR, atriumR, wallH, 64, 1, true,
      0.95, Math.PI * 2 - 0.55
    );
    this.geometries.push(wallGeo);
    const wall = new THREE.Mesh(wallGeo, wallMat);
    wall.position.y = wallH / 2;
    wall.receiveShadow = true;
    this.group.add(wall);

    // 3. Rhythmic architectural vertical pilasters around the perimeter
    const pilasterGeo = new THREE.BoxGeometry(0.55, wallH, 0.45);
    this.geometries.push(pilasterGeo);
    const pilasterMat = new THREE.MeshStandardMaterial({
      color: this.colors.warmWhite,
      roughness: 0.75,
      metalness: 0.04
    });
    this.materials.push(pilasterMat);

    for (let i = 0; i < 16; i++) {
      const angle = (i / 16) * Math.PI * 2;
      // Skip doorway angle range
      if (angle > 0.45 && angle < 1.0) continue;

      const pMesh = new THREE.Mesh(pilasterGeo, pilasterMat);
      pMesh.position.set(
        Math.cos(angle) * (atriumR - 0.2),
        wallH / 2,
        Math.sin(angle) * (atriumR - 0.2)
      );
      pMesh.rotation.y = -angle + Math.PI / 2;
      pMesh.receiveShadow = true;
      pMesh.castShadow = true;
      this.group.add(pMesh);
    }

    // 4. Curved upper gallery / mezzanine band
    const mezR = atriumR - 0.3;
    const mezGeo = new THREE.TorusGeometry(mezR, 0.18, 16, 64);
    this.geometries.push(mezGeo);
    const mezMat = new THREE.MeshStandardMaterial({
      color: this.colors.aluminum,
      metalness: 0.6,
      roughness: 0.3
    });
    this.materials.push(mezMat);
    const mezMesh = new THREE.Mesh(mezGeo, mezMat);
    mezMesh.rotation.x = Math.PI / 2;
    mezMesh.position.y = 5.2;
    this.group.add(mezMesh);
  }

  buildSkylightAndCeiling() {
    const wallH = 10.5;

    // 1. Stepped circular ceiling soffits (Pantheon / Guggenheim inspired)
    const stepMat = new THREE.MeshStandardMaterial({
      color: this.colors.warmWhite,
      roughness: 0.8,
      side: THREE.DoubleSide
    });
    this.materials.push(stepMat);

    // Lower ceiling ring: from atrium wall (15.5) in to radius 7.2
    const ceil1Geo = new THREE.RingGeometry(7.2, 15.6, 64);
    this.geometries.push(ceil1Geo);
    const ceil1 = new THREE.Mesh(ceil1Geo, stepMat);
    ceil1.rotation.x = Math.PI / 2;
    ceil1.position.y = wallH;
    this.group.add(ceil1);

    // Stepped riser 1
    const riser1Geo = new THREE.CylinderGeometry(7.2, 7.2, 0.6, 64, 1, true);
    this.geometries.push(riser1Geo);
    const riser1 = new THREE.Mesh(riser1Geo, stepMat);
    riser1.position.y = wallH + 0.3;
    this.group.add(riser1);

    // Middle ceiling ring: radius 5.4 to 7.2 at height +0.6
    const ceil2Geo = new THREE.RingGeometry(5.4, 7.2, 64);
    this.geometries.push(ceil2Geo);
    const ceil2 = new THREE.Mesh(ceil2Geo, stepMat);
    ceil2.rotation.x = Math.PI / 2;
    ceil2.position.y = wallH + 0.6;
    this.group.add(ceil2);

    // Stepped riser 2 with hidden architectural cove light
    const riser2Geo = new THREE.CylinderGeometry(5.4, 5.4, 0.6, 64, 1, true);
    this.geometries.push(riser2Geo);
    const riser2 = new THREE.Mesh(riser2Geo, stepMat);
    riser2.position.y = wallH + 0.9;
    this.group.add(riser2);

    // Glowing architectural cove light ring
    const coveLightGeo = new THREE.TorusGeometry(5.35, 0.05, 16, 64);
    this.geometries.push(coveLightGeo);
    const coveMat = new THREE.MeshBasicMaterial({ color: 0xFFFDF8 });
    this.materials.push(coveMat);
    const coveMesh = new THREE.Mesh(coveLightGeo, coveMat);
    coveMesh.rotation.x = Math.PI / 2;
    coveMesh.position.y = wallH + 0.7;
    this.group.add(coveMesh);

    // 2. Grand Circular Skylight Dome & Mullions
    const skylightR = 5.4;
    const skylightH = wallH + 1.2;

    const frameMat = new THREE.MeshStandardMaterial({
      color: this.colors.aluminum,
      metalness: 0.85,
      roughness: 0.22
    });
    this.materials.push(frameMat);

    // Outer structural ring of skylight
    const skylightRimGeo = new THREE.TorusGeometry(skylightR, 0.1, 16, 64);
    this.geometries.push(skylightRimGeo);
    const skylightRim = new THREE.Mesh(skylightRimGeo, frameMat);
    skylightRim.rotation.x = Math.PI / 2;
    skylightRim.position.y = skylightH;
    this.group.add(skylightRim);

    // Inner concentric ring
    const innerRimGeo = new THREE.TorusGeometry(skylightR * 0.52, 0.06, 16, 64);
    this.geometries.push(innerRimGeo);
    const innerRim = new THREE.Mesh(innerRimGeo, frameMat);
    innerRim.rotation.x = Math.PI / 2;
    innerRim.position.y = skylightH + 0.35;
    this.group.add(innerRim);

    // Radial mullions (12 ribs)
    for (let i = 0; i < 12; i++) {
      const angle = (i / 12) * Math.PI * 2;
      const ribGeo = new THREE.BoxGeometry(skylightR, 0.06, 0.05);
      this.geometries.push(ribGeo);
      const rib = new THREE.Mesh(ribGeo, frameMat);
      rib.position.set(
        Math.cos(angle) * (skylightR / 2),
        skylightH + 0.2,
        Math.sin(angle) * (skylightR / 2)
      );
      rib.rotation.y = -angle;
      rib.rotation.z = 0.07;
      this.group.add(rib);
    }

    // Domed skylight glass showing soft blue daylight sky
    const glassGeo = new THREE.SphereGeometry(skylightR, 32, 16, 0, Math.PI * 2, 0, Math.PI * 0.28);
    this.geometries.push(glassGeo);
    const glassMat = new THREE.MeshPhysicalMaterial({
      color: 0xEEF6FD,
      transmission: 0.90,
      opacity: 0.85,
      transparent: true,
      roughness: 0.08,
      ior: 1.48
    });
    this.materials.push(glassMat);
    const glassDome = new THREE.Mesh(glassGeo, glassMat);
    glassDome.position.y = skylightH - 0.2;
    this.group.add(glassDome);

    // Sky backdrop disc above skylight
    const skyGeo = new THREE.CircleGeometry(skylightR * 1.5, 32);
    this.geometries.push(skyGeo);
    const skyMat = new THREE.MeshBasicMaterial({ color: 0xCFE5F8, side: THREE.DoubleSide });
    this.materials.push(skyMat);
    const skyDisc = new THREE.Mesh(skyGeo, skyMat);
    skyDisc.rotation.x = Math.PI / 2;
    skyDisc.position.y = skylightH + 2.5;
    this.group.add(skyDisc);
  }

  buildCentralInstallation() {
    const installGroup = new THREE.Group();

    // 1. Low circular exhibition pedestal in polished light stone/porcelain
    const pedestalR = 3.6;
    const pedestalH = 0.32;
    const pedGeo = new THREE.CylinderGeometry(pedestalR, pedestalR + 0.08, pedestalH, 64);
    this.geometries.push(pedGeo);
    const pedMat = new THREE.MeshStandardMaterial({
      color: 0xF4F5F2,
      roughness: 0.35,
      metalness: 0.06
    });
    this.materials.push(pedMat);
    const pedestal = new THREE.Mesh(pedGeo, pedMat);
    pedestal.position.y = pedestalH / 2;
    pedestal.receiveShadow = true;
    pedestal.castShadow = true;
    installGroup.add(pedestal);

    // Subtle brushed aluminum base trim on the pedestal
    const pedTrimGeo = new THREE.TorusGeometry(pedestalR + 0.06, 0.025, 16, 64);
    this.geometries.push(pedTrimGeo);
    const pedTrimMat = new THREE.MeshStandardMaterial({
      color: this.colors.aluminum,
      metalness: 0.85,
      roughness: 0.25
    });
    this.materials.push(pedTrimMat);
    const pedTrim = new THREE.Mesh(pedTrimGeo, pedTrimMat);
    pedTrim.rotation.x = Math.PI / 2;
    pedTrim.position.y = 0.03;
    installGroup.add(pedTrim);

    // Subtle blue LED halo ring around the pedestal on the floor (Reference Board feature)
    const haloGeo = new THREE.RingGeometry(pedestalR + 0.25, pedestalR + 0.32, 64);
    this.geometries.push(haloGeo);
    const haloMat = new THREE.MeshBasicMaterial({
      color: this.colors.steelBlue,
      transparent: true,
      opacity: 0.55
    });
    this.materials.push(haloMat);
    const halo = new THREE.Mesh(haloGeo, haloMat);
    halo.rotation.x = -Math.PI / 2;
    halo.position.y = 0.006;
    installGroup.add(halo);

    // 2. Three monolithic frosted-glass blocks with crystal-clear refractive edges
    const glassMat = new THREE.MeshPhysicalMaterial({
      color: 0xF0F7FD,
      transmission: 0.90,
      opacity: 0.98,
      transparent: true,
      roughness: 0.16,
      ior: 1.52,
      thickness: 1.1,
      specularIntensity: 1.0,
      specularColor: 0xFFFFFF
    });
    this.materials.push(glassMat);

    // Frosted core material inside each slab for depth
    const coreMat = new THREE.MeshStandardMaterial({
      color: 0xDDF0FC,
      transparent: true,
      opacity: 0.45,
      roughness: 0.65
    });
    this.materials.push(coreMat);

    const frameMat = new THREE.MeshStandardMaterial({
      color: this.colors.aluminum,
      metalness: 0.9,
      roughness: 0.2
    });
    this.materials.push(frameMat);

    // 3 Staggered Panels matching spatial reference
    const configs = [
      {
        id: 'ba',
        title: 'BUSINESS ANALYSIS',
        subtitle: 'REQUIREMENTS · AS-IS / TO-BE · WORKFLOWS',
        num: '01',
        w: 2.1,
        h: 2.0,
        d: 0.45,
        pos: new THREE.Vector3(-0.75, pedestalH + 2.0 / 2, 0.65),
        rotY: 0.08
      },
      {
        id: 'es',
        title: 'ENTERPRISE SYSTEMS',
        subtitle: 'SAP ABAP · ARCHITECTURE · AUDIT TRAIL',
        num: '02',
        w: 2.4,
        h: 3.6, // Tallest center-rear
        d: 0.45,
        pos: new THREE.Vector3(0.12, pedestalH + 3.6 / 2, -0.42),
        rotY: -0.06
      },
      {
        id: 'ts',
        title: 'TECHNOLOGY SOLUTIONS',
        subtitle: 'FULL-STACK · CLOUD · INTEGRATION',
        num: '03',
        w: 1.9,
        h: 2.6,
        d: 0.45,
        pos: new THREE.Vector3(1.05, pedestalH + 2.6 / 2, 0.45),
        rotY: 0.14
      }
    ];

    configs.forEach(cfg => {
      const pGroup = new THREE.Group();
      pGroup.position.copy(cfg.pos);
      pGroup.rotation.y = cfg.rotY;

      // Outer glass block
      const blockGeo = new THREE.BoxGeometry(cfg.w, cfg.h, cfg.d);
      this.geometries.push(blockGeo);
      const blockMesh = new THREE.Mesh(blockGeo, glassMat);
      blockMesh.castShadow = true;
      blockMesh.receiveShadow = true;
      pGroup.add(blockMesh);

      // Inner volumetric frosted core
      const coreGeo = new THREE.BoxGeometry(cfg.w * 0.92, cfg.h * 0.92, cfg.d * 0.85);
      this.geometries.push(coreGeo);
      const coreMesh = new THREE.Mesh(coreGeo, coreMat);
      pGroup.add(coreMesh);

      // Delicate aluminum perimeter frame
      const borderThickness = 0.03;
      const tGeo = new THREE.BoxGeometry(cfg.w + borderThickness * 2, borderThickness, cfg.d + 0.01);
      const sGeo = new THREE.BoxGeometry(borderThickness, cfg.h, cfg.d + 0.01);
      this.geometries.push(tGeo, sGeo);

      const topBar = new THREE.Mesh(tGeo, frameMat);
      topBar.position.y = cfg.h / 2 + borderThickness / 2;
      const leftBar = new THREE.Mesh(sGeo, frameMat);
      leftBar.position.x = -cfg.w / 2 - borderThickness / 2;
      const rightBar = new THREE.Mesh(sGeo, frameMat);
      rightBar.position.x = cfg.w / 2 + borderThickness / 2;
      pGroup.add(topBar, leftBar, rightBar);

      // Pedestal mounting shoes
      const shoeGeo = new THREE.BoxGeometry(0.3, 0.1, cfg.d + 0.08);
      this.geometries.push(shoeGeo);
      const s1 = new THREE.Mesh(shoeGeo, frameMat);
      s1.position.set(-cfg.w * 0.32, -cfg.h / 2 + 0.05, 0);
      const s2 = new THREE.Mesh(shoeGeo, frameMat);
      s2.position.set(cfg.w * 0.32, -cfg.h / 2 + 0.05, 0);
      pGroup.add(s1, s2);

      // High-res label decal
      const label = this.buildDecal(cfg);
      label.position.set(0, 0, cfg.d / 2 + 0.005);
      pGroup.add(label);

      installGroup.add(pGroup);
    });

    installGroup.position.set(1.8, 0, 0);
    this.group.add(installGroup);
  }

  buildDecal(cfg) {
    const canvas = document.createElement('canvas');
    canvas.width = 1024;
    canvas.height = Math.round(1024 * (cfg.h / cfg.w));
    const ctx = canvas.getContext('2d');

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Subtle framing
    ctx.strokeStyle = 'rgba(111, 158, 200, 0.3)';
    ctx.lineWidth = 2;
    ctx.strokeRect(50, 50, canvas.width - 100, canvas.height - 100);

    // Number tag
    ctx.fillStyle = '#6F9EC8';
    ctx.font = '600 36px "IBM Plex Mono", monospace';
    ctx.fillText(`— ${cfg.num} —`, 90, 140);

    // Title
    ctx.fillStyle = '#263640';
    ctx.font = '700 48px "Manrope", sans-serif';
    ctx.fillText(cfg.title, 90, 225);

    // Divider
    ctx.strokeStyle = 'rgba(38, 54, 64, 0.25)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(90, 260);
    ctx.lineTo(canvas.width - 90, 260);
    ctx.stroke();

    // Subtitle
    ctx.fillStyle = '#5A6C78';
    ctx.font = '500 24px "IBM Plex Mono", monospace';
    ctx.fillText(cfg.subtitle, 90, 315);

    const texture = new THREE.CanvasTexture(canvas);
    texture.colorSpace = THREE.SRGBColorSpace;
    texture.anisotropy = 8;
    this.textures.push(texture);

    const planeGeo = new THREE.PlaneGeometry(cfg.w * 0.94, cfg.h * 0.94);
    this.geometries.push(planeGeo);
    const planeMat = new THREE.MeshBasicMaterial({
      map: texture,
      transparent: true,
      opacity: 0.94,
      depthWrite: false
    });
    this.materials.push(planeMat);

    return new THREE.Mesh(planeGeo, planeMat);
  }

  buildCorridorPortal() {
    // Portal position at top-right (corresponds to waypoint 04 in spatial plan)
    const portalGroup = new THREE.Group();
    // Angle ~40° (X ~ 10, Z ~ -10.5)
    portalGroup.position.set(10.2, 0, -10.2);
    portalGroup.rotation.y = -Math.PI / 4;

    const frameMat = new THREE.MeshStandardMaterial({
      color: this.colors.aluminum,
      metalness: 0.8,
      roughness: 0.25
    });
    this.materials.push(frameMat);

    const wallMat = new THREE.MeshStandardMaterial({
      color: this.colors.warmWhite,
      roughness: 0.85,
      side: THREE.DoubleSide
    });
    this.materials.push(wallMat);

    // Portal archway
    const pW = 4.0;
    const pH = 6.2;
    const pD = 0.4;
    const lPost = new THREE.Mesh(new THREE.BoxGeometry(0.2, pH, pD), frameMat);
    lPost.position.set(-pW / 2, pH / 2, 0);
    const rPost = new THREE.Mesh(new THREE.BoxGeometry(0.2, pH, pD), frameMat);
    rPost.position.set(pW / 2, pH / 2, 0);
    const topPost = new THREE.Mesh(new THREE.BoxGeometry(pW + 0.2, 0.2, pD), frameMat);
    topPost.position.set(0, pH, 0);
    portalGroup.add(lPost, rPost, topPost);

    // Curved corridor walls extending into distance
    const len = 12;
    const lWall = new THREE.Mesh(new THREE.PlaneGeometry(len, pH), wallMat);
    lWall.position.set(-pW / 2, pH / 2, -len / 2);
    lWall.rotation.y = Math.PI / 2 + 0.18;

    const rWall = new THREE.Mesh(new THREE.PlaneGeometry(len, pH), wallMat);
    rWall.position.set(pW / 2, pH / 2, -len / 2);
    rWall.rotation.y = -Math.PI / 2 + 0.18;

    // Continuous architectural cove light in corridor
    const stripMat = new THREE.MeshBasicMaterial({ color: 0xFDFBF7 });
    this.materials.push(stripMat);
    const strip = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.06, len - 1), stripMat);
    strip.position.set(0, pH - 0.05, -len / 2);

    portalGroup.add(lWall, rWall, strip);
    this.group.add(portalGroup);
  }

  setupNaturalLighting() {
    // 1. Natural daylight pouring through circular skylight
    const daylight = new THREE.DirectionalLight(0xFFFFFF, 2.4);
    daylight.position.set(2.0, 18.0, 3.0);
    daylight.castShadow = true;
    daylight.shadow.mapSize.width = 2048;
    daylight.shadow.mapSize.height = 2048;
    daylight.shadow.camera.near = 1.0;
    daylight.shadow.camera.far = 30.0;
    daylight.shadow.camera.left = -7;
    daylight.shadow.camera.right = 7;
    daylight.shadow.camera.top = 7;
    daylight.shadow.camera.bottom = -7;
    daylight.shadow.bias = -0.0004;
    this.group.add(daylight);

    // 2. Soft sky ambient fill
    const hemiLight = new THREE.HemisphereLight(this.colors.skyLight, 0xF2EFEB, 1.25);
    hemiLight.position.set(0, 12, 0);
    this.group.add(hemiLight);

    // 3. Subtle glass edge refraction light
    const glassLight = new THREE.PointLight(this.colors.iceBlue, 0.9, 12);
    glassLight.position.set(0.2, 2.5, 1.2);
    this.group.add(glassLight);

    // 4. Warm ambient fill in corridor
    const corridorLight = new THREE.PointLight(0xFDF7EE, 0.7, 10);
    corridorLight.position.set(9.0, 3.0, -9.0);
    this.group.add(corridorLight);
  }

  dispose() {
    this.textures.forEach(t => t.dispose());
    this.geometries.forEach(g => g.dispose());
    this.materials.forEach(m => m.dispose());
  }
}
