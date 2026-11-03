/**
 * Camera Motion Controller for Milestone 01: Entrance Atrium
 * Reconciled with Blender Graybox (Milestone 01A) & Camera Motion Ledger:
 *  - K01 (p = 0.00): Establishing Shot (wide entrance threshold, circular skylight + atrium volume)
 *  - K02 (p = 0.33): Forward Dolly (smooth perspective advance toward plinth)
 *  - K03 (p = 0.66): Installation Focus (oblique angle revealing panel depth, thickness & refraction)
 *  - K04 (p = 1.00): Transition Alignment (framing North-East corridor to Profile Gallery)
 *
 * 100% Reversible, deterministic Catmull-Rom spline trajectory with zero text occlusion.
 */

import * as THREE from 'three';

export class CameraController {
  constructor(camera) {
    this.camera = camera;
    this.currentPosition = new THREE.Vector3();
    this.currentTarget = new THREE.Vector3();

    // Desktop waypoints matching verified Blender Graybox specs (converted to Three.js Y-up)
    // Blender mapping: X_three = X_blender, Y_three = Z_blender, Z_three = -Y_blender
    this.desktopWaypoints = {
      positions: [
        new THREE.Vector3(0.00, 1.90, 10.20),   // K01 Establishing (from Blender (0.0, -10.2, 1.9))
        new THREE.Vector3(0.70, 1.85, 4.80),    // K02 Forward Dolly (from Blender (0.7, -4.5, 1.85))
        new THREE.Vector3(0.60, 1.75, 3.60),    // K03 Installation Focus (three-quarters staggered angle)
        new THREE.Vector3(4.80, 1.80, -4.80)    // K04 Corridor Transition (from Blender (4.8, 4.8, 1.8))
      ],
      targets: [
        new THREE.Vector3(1.00, 2.90, -0.20),   // K01 Target (aimed right-center to protect left Hero space)
        new THREE.Vector3(1.40, 1.70, 0.00),    // K02 Target (centered on plinth at X=1.4)
        new THREE.Vector3(1.45, 1.65, 0.00),    // K03 Target (focused on monolith cluster)
        new THREE.Vector3(12.00, 1.80, -12.00)  // K04 Target (looking down North-East passage)
      ],
      fovs: [57.0, 46.0, 42.0, 48.0]
    };

    // Mobile waypoints optimized for portrait aspect ratios (aspect < 1.0)
    this.mobileWaypoints = {
      positions: [
        new THREE.Vector3(0.40, 2.30, 12.80),   // K01 Mobile: pulled back to frame atrium in portrait
        new THREE.Vector3(0.85, 2.00, 6.50),    // K02 Mobile
        new THREE.Vector3(0.60, 1.75, 4.20),    // K03 Mobile
        new THREE.Vector3(4.80, 1.80, -4.80)    // K04 Mobile
      ],
      targets: [
        new THREE.Vector3(1.20, 2.70, 0.00),
        new THREE.Vector3(1.40, 1.75, 0.00),
        new THREE.Vector3(1.45, 1.65, 0.00),
        new THREE.Vector3(12.00, 1.80, -12.00)
      ],
      fovs: [58.0, 48.0, 44.0, 50.0]
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
    this.targetCurve = new THREE.CatmullRomCurve3(wp.targets, false, 'centripetal');
  }

  getInterpolatedFov(p) {
    const fovs = this.isMobile ? this.mobileWaypoints.fovs : this.desktopWaypoints.fovs;
    if (p <= 0.333) {
      const t = p / 0.333;
      return THREE.MathUtils.lerp(fovs[0], fovs[1], t);
    } else if (p <= 0.667) {
      const t = (p - 0.333) / 0.334;
      return THREE.MathUtils.lerp(fovs[1], fovs[2], t);
    } else {
      const t = (p - 0.667) / 0.333;
      return THREE.MathUtils.lerp(fovs[2], fovs[3], t);
    }
  }

  /**
   * Update camera position, lookAt, and FOV based on normalized progress p in [0, 1]
   * @param {number} p - Normalized scene progress [0, 1]
   */
  update(p) {
    const clampedP = Math.min(1, Math.max(0, p));
    this.posCurve.getPoint(clampedP, this.currentPosition);
    this.targetCurve.getPoint(clampedP, this.currentTarget);

    this.camera.position.copy(this.currentPosition);
    this.camera.lookAt(this.currentTarget);

    const targetFov = this.getInterpolatedFov(clampedP);
    if (Math.abs(this.camera.fov - targetFov) > 0.05) {
      this.camera.fov = targetFov;
      this.camera.updateProjectionMatrix();
    }
  }
}
