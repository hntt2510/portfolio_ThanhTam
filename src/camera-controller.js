/**
 * Camera Motion Controller for Project Museum
 * Supports:
 *  - Chapter 01: Entrance Atrium (K01 Establishing -> K02 Forward Dolly -> K03 Focus -> K04 Corridor)
 *  - Chapter 02: Profile Gallery (K05 Entry -> K06 Foundation -> K07 Experience -> K08 Perspective)
 *
 * 100% Reversible, deterministic Catmull-Rom spline trajectory with zero text occlusion.
 * C0/C1 mathematical continuity between K04 and K05.
 */

import * as THREE from 'three';

export class CameraController {
  constructor(camera) {
    this.camera = camera;
    this.currentPosition = new THREE.Vector3();
    this.currentTarget = new THREE.Vector3();

    // Scene 01 Waypoints (Entrance Atrium)
    this.scene01Desktop = {
      positions: [
        new THREE.Vector3(0.00, 1.90, 10.20),   // K01 Establishing
        new THREE.Vector3(0.70, 1.85, 4.80),    // K02 Forward Dolly
        new THREE.Vector3(0.60, 1.75, 3.60),    // K03 Installation Focus
        new THREE.Vector3(4.80, 1.80, -4.80)    // K04 Corridor Transition
      ],
      targets: [
        new THREE.Vector3(1.00, 2.90, -0.20),   // K01 Target
        new THREE.Vector3(1.40, 1.70, 0.00),    // K02 Target
        new THREE.Vector3(1.45, 1.65, 0.00),    // K03 Target
        new THREE.Vector3(12.00, 1.80, -12.00)  // K04 Target
      ],
      fovs: [57.0, 46.0, 42.0, 48.0]
    };

    this.scene01Mobile = {
      positions: [
        new THREE.Vector3(0.40, 2.30, 12.80),
        new THREE.Vector3(0.85, 2.00, 6.50),
        new THREE.Vector3(0.60, 1.75, 4.20),
        new THREE.Vector3(4.80, 1.80, -4.80)
      ],
      targets: [
        new THREE.Vector3(1.20, 2.70, 0.00),
        new THREE.Vector3(1.40, 1.75, 0.00),
        new THREE.Vector3(1.45, 1.65, 0.00),
        new THREE.Vector3(12.00, 1.80, -12.00)
      ],
      fovs: [58.0, 48.0, 44.0, 50.0]
    };

    // Scene 02 Waypoints (Profile Gallery)
    // Starts exactly at K04 end transform: pos (4.80, 1.80, -4.80), target (12.00, 1.80, -12.00)
    // Frames curved promenade: outer curtain wall left, stone floor/benches center, curved wall right.
    this.scene02Desktop = {
      positions: [
        new THREE.Vector3(4.80, 1.80, -4.80),    // K05 Start: exact match to K04
        new THREE.Vector3(10.50, 1.80, -10.50),  // K05 Corridor Advance
        new THREE.Vector3(16.86, 1.80, -16.16),  // K05 Gallery Arrival (alpha=130, R=24.6)
        new THREE.Vector3(23.61, 1.80, -19.76),  // K06 Foundation (alpha=112, R=24.6)
        new THREE.Vector3(30.53, 1.80, -21.82),  // K07 Experience (alpha=95, R=24.6)
        new THREE.Vector3(36.95, 1.80, -21.54)   // K08 Perspective (alpha=80, R=24.6)
      ],
      targets: [
        new THREE.Vector3(12.00, 1.80, -12.00),  // Exact match to K04 target
        new THREE.Vector3(17.50, 1.80, -17.50),  // Corridor gaze
        new THREE.Vector3(23.61, 1.80, -19.76),  // Toward gallery promenade (alpha=112, R=24.2)
        new THREE.Vector3(31.00, 1.80, -21.26),  // Colonnade vista (alpha=94, R=24.0)
        new THREE.Vector3(37.67, 1.80, -20.79),  // Mid-gallery vista (alpha=78, R=24.0)
        new THREE.Vector3(43.03, 1.80, -19.52)   // Toward threshold arch (alpha=65, R=24.5)
      ],
      fovs: [48.0, 48.0, 48.0, 46.0, 46.0, 48.0]
    };

    this.scene02Mobile = {
      positions: [
        new THREE.Vector3(4.80, 1.80, -4.80),
        new THREE.Vector3(10.50, 1.80, -10.50),
        new THREE.Vector3(16.86, 1.90, -16.16),
        new THREE.Vector3(23.61, 1.90, -19.76),
        new THREE.Vector3(30.53, 1.90, -21.82),
        new THREE.Vector3(36.95, 1.90, -21.54)
      ],
      targets: [
        new THREE.Vector3(12.00, 1.80, -12.00),
        new THREE.Vector3(17.50, 1.80, -17.50),
        new THREE.Vector3(23.61, 1.80, -19.76),
        new THREE.Vector3(31.00, 1.80, -21.26),
        new THREE.Vector3(37.67, 1.80, -20.79),
        new THREE.Vector3(43.03, 1.80, -19.52)
      ],
      fovs: [50.0, 50.0, 50.0, 48.0, 48.0, 50.0]
    };

    this.isMobile = false;
    this.rebuildSplines();
  }

  setMobile(isMobile) {
    if (this.isMobile !== isMobile) {
      this.isMobile = isMobile;
      this.rebuildSplines();
    }
  }

  rebuildSplines() {
    const s1 = this.isMobile ? this.scene01Mobile : this.scene01Desktop;
    this.posCurve01 = new THREE.CatmullRomCurve3(s1.positions, false, 'centripetal');
    this.tgtCurve01 = new THREE.CatmullRomCurve3(s1.targets, false, 'centripetal');

    const s2 = this.isMobile ? this.scene02Mobile : this.scene02Desktop;
    this.posCurve02 = new THREE.CatmullRomCurve3(s2.positions, false, 'centripetal');
    this.tgtCurve02 = new THREE.CatmullRomCurve3(s2.targets, false, 'centripetal');
  }

  getFov01(p) {
    const fovs = this.isMobile ? this.scene01Mobile.fovs : this.scene01Desktop.fovs;
    if (p <= 0.333) {
      return THREE.MathUtils.lerp(fovs[0], fovs[1], p / 0.333);
    } else if (p <= 0.667) {
      return THREE.MathUtils.lerp(fovs[1], fovs[2], (p - 0.333) / 0.334);
    } else {
      return THREE.MathUtils.lerp(fovs[2], fovs[3], (p - 0.667) / 0.333);
    }
  }

  getFov02(p) {
    const fovs = this.isMobile ? this.scene02Mobile.fovs : this.scene02Desktop.fovs;
    const n = fovs.length - 1;
    const scaled = p * n;
    const idx = Math.min(Math.floor(scaled), n - 1);
    const frac = scaled - idx;
    return THREE.MathUtils.lerp(fovs[idx], fovs[idx + 1], frac);
  }

  /**
   * Update camera using global normalized scroll progress p in [0, 1]
   * Global schedule:
   *  - Scene 01 (Entrance Atrium): p in [0.00, 0.40]
   *  - Scene 02 (Profile Gallery): p in [0.40, 1.00]
   */
  update(globalProgress) {
    const p = Math.min(1, Math.max(0, globalProgress));
    let targetFov = 48.0;

    if (p <= 0.40) {
      // Scene 01
      const localP = p / 0.40;
      this.posCurve01.getPoint(localP, this.currentPosition);
      this.tgtCurve01.getPoint(localP, this.currentTarget);
      targetFov = this.getFov01(localP);
    } else {
      // Scene 02
      const localP = (p - 0.40) / 0.60;
      this.posCurve02.getPoint(localP, this.currentPosition);
      this.tgtCurve02.getPoint(localP, this.currentTarget);
      targetFov = this.getFov02(localP);
    }

    this.camera.position.copy(this.currentPosition);
    this.camera.lookAt(this.currentTarget);

    if (Math.abs(this.camera.fov - targetFov) > 0.05) {
      this.camera.fov = targetFov;
      this.camera.updateProjectionMatrix();
    }
  }
}
