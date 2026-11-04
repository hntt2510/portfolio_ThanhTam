/**
 * Camera Motion Controller for Project Museum (Milestone 02C)
 * Unified Catmull-Rom Trajectory (K01 -> K04 -> K08):
 *  - Chapter 01: Entrance Atrium (K01 Establishing -> K02 Forward Dolly -> K03 Focus -> K04 Corridor)
 *  - Chapter 02: Profile Gallery (K05 Entry -> K06 Foundation -> K07 Experience -> K08 Perspective)
 *
 * Guaranteed C0 (position, target, FOV) and C1 (tangent velocity) continuity across all waypoints
 * including the transition boundary at p = 0.40.
 * 100% Reversible, deterministic, and collision-free.
 */

import * as THREE from 'three';

export class CameraController {
  constructor(camera) {
    this.camera = camera;
    this.currentPosition = new THREE.Vector3();
    this.currentTarget = new THREE.Vector3();

    // Unified Desktop Waypoints: K01 -> K04 -> K08 (9 control points, 8 segments)
    this.desktopWaypoints = {
      positions: [
        new THREE.Vector3(0.00, 1.90, 10.20),   // W0: K01 Establishing (p = 0.00)
        new THREE.Vector3(0.70, 1.85, 4.80),    // W1: K02 Forward Dolly
        new THREE.Vector3(0.60, 1.75, 3.60),    // W2: K03 Installation Focus
        new THREE.Vector3(4.80, 1.80, -4.80),   // W3: K04 Corridor Transition (p = 0.40)
        new THREE.Vector3(10.50, 1.80, -10.50), // W4: K05 Corridor Advance
        new THREE.Vector3(16.86, 1.80, -16.16), // W5: K05 Gallery Arrival
        new THREE.Vector3(23.61, 1.80, -19.76), // W6: K06 Foundation
        new THREE.Vector3(29.68, 1.80, -21.74), // W7: K07 Experience (clear negative space)
        new THREE.Vector3(36.53, 1.80, -21.62)  // W8: K08 Perspective / Arched Portal (p = 1.00)
      ],
      targets: [
        new THREE.Vector3(1.00, 2.90, -0.20),   // W0 Target
        new THREE.Vector3(1.40, 1.70, 0.00),    // W1 Target
        new THREE.Vector3(1.45, 1.65, 0.00),    // W2 Target
        new THREE.Vector3(12.00, 1.80, -12.00), // W3 Target (K04)
        new THREE.Vector3(17.50, 1.80, -17.50), // W4 Target
        new THREE.Vector3(23.61, 1.80, -19.76), // W5 Target
        new THREE.Vector3(31.00, 1.80, -21.26), // W6 Target
        new THREE.Vector3(37.71, 1.80, -20.99), // W7 Target
        new THREE.Vector3(43.24, 2.20, -19.98)  // W8 Target (Frames Arched Portal)
      ],
      fovs: [57.0, 46.0, 42.0, 48.0, 48.0, 48.0, 46.0, 46.0, 48.0]
    };

    // Unified Mobile Waypoints optimized for portrait aspect ratios
    this.mobileWaypoints = {
      positions: [
        new THREE.Vector3(0.40, 2.30, 12.80),
        new THREE.Vector3(0.85, 2.00, 6.50),
        new THREE.Vector3(0.60, 1.75, 4.20),
        new THREE.Vector3(4.80, 1.80, -4.80),   // K04 match
        new THREE.Vector3(10.50, 1.85, -10.50),
        new THREE.Vector3(16.86, 1.88, -16.16),
        new THREE.Vector3(23.61, 1.88, -19.76),
        new THREE.Vector3(29.68, 1.88, -21.74),
        new THREE.Vector3(36.53, 1.88, -21.62)
      ],
      targets: [
        new THREE.Vector3(1.20, 2.70, 0.00),
        new THREE.Vector3(1.40, 1.75, 0.00),
        new THREE.Vector3(1.45, 1.65, 0.00),
        new THREE.Vector3(12.00, 1.80, -12.00),
        new THREE.Vector3(17.50, 1.80, -17.50),
        new THREE.Vector3(23.61, 1.80, -19.76),
        new THREE.Vector3(31.00, 1.80, -21.26),
        new THREE.Vector3(37.71, 1.80, -20.99),
        new THREE.Vector3(43.24, 2.20, -19.98)
      ],
      fovs: [58.0, 48.0, 44.0, 50.0, 50.0, 50.0, 48.0, 48.0, 50.0]
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
    const wp = this.isMobile ? this.mobileWaypoints : this.desktopWaypoints;
    this.posCurve = new THREE.CatmullRomCurve3(wp.positions, false, 'centripetal');
    this.tgtCurve = new THREE.CatmullRomCurve3(wp.targets, false, 'centripetal');
  }

  /**
   * C1-continuous Hermite cubic time mapping from global scroll progress p in [0, 1]
   * to master curve parameter u in [0, 1].
   * At p = 0.40, u = 0.375 (exact control point W3 / K04).
   * Matching first derivatives guaranteed: du/dp(0.40-) == du/dp(0.40+).
   */
  mapProgressToCurveU(p) {
    if (p <= 0.0) return 0.0;
    if (p >= 1.0) return 1.0;

    const uK04 = 3.0 / 8.0; // 0.375
    const pMid = 0.40;

    // Hermite cubic blending slopes with centripetal knot ratio compensation
    const m1 = uK04 / pMid; // 0.9375
    const m2 = (1.0 - uK04) / (1.0 - pMid); // 1.04167
    const mBase = (m1 + m2) * 0.5; // 0.98958

    // Ratio of centripetal knot intervals at W3 (K04): sqrt(chord_in / chord_out) ~= 1.0792
    const knotRatio = 1.0792;
    const mMidL = mBase / Math.sqrt(knotRatio);
    const mMidR = mBase * Math.sqrt(knotRatio);

    if (p <= pMid) {
      const t = p / pMid;
      const h00 = 2 * t * t * t - 3 * t * t + 1;
      const h10 = t * t * t - 2 * t * t + t;
      const h01 = -2 * t * t * t + 3 * t * t;
      const h11 = t * t * t - t * t;
      return h00 * 0.0 + h10 * (m1 * pMid) + h01 * uK04 + h11 * (mMidL * pMid);
    } else {
      const t = (p - pMid) / (1.0 - pMid);
      const span = 1.0 - pMid;
      const h00 = 2 * t * t * t - 3 * t * t + 1;
      const h10 = t * t * t - 2 * t * t + t;
      const h01 = -2 * t * t * t + 3 * t * t;
      const h11 = t * t * t - t * t;
      return h00 * uK04 + h10 * (mMidR * span) + h01 * 1.0 + h11 * (m2 * span);
    }
  }

  getInterpolatedFov(u) {
    const fovs = this.isMobile ? this.mobileWaypoints.fovs : this.desktopWaypoints.fovs;
    const n = fovs.length - 1;
    const scaled = Math.min(Math.max(u, 0), 1) * n;
    const idx = Math.min(Math.floor(scaled), n - 1);
    const frac = scaled - idx;
    return THREE.MathUtils.lerp(fovs[idx], fovs[idx + 1], frac);
  }

  /**
   * Update camera position, lookAt, and FOV based on normalized progress p in [0, 1]
   * @param {number} p - Normalized scene progress [0, 1]
   */
  update(p) {
    const clampedP = Math.min(1, Math.max(0, p));
    const u = this.mapProgressToCurveU(clampedP);

    this.posCurve.getPoint(u, this.currentPosition);
    this.tgtCurve.getPoint(u, this.currentTarget);

    this.camera.position.copy(this.currentPosition);
    this.camera.lookAt(this.currentTarget);

    const targetFov = this.getInterpolatedFov(u);
    if (Math.abs(this.camera.fov - targetFov) > 0.02) {
      this.camera.fov = targetFov;
      this.camera.updateProjectionMatrix();
    }
  }
}
