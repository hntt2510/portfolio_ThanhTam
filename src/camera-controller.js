/**
 * Camera Motion Controller for Milestone 01: Entrance Atrium
 * Faithful to Camera Motion Ledger V1 & Spatial Blueprint:
 *  - K01 (0.00 - 0.25): Establishing Shot (wide entrance, circular skylight + atrium volume)
 *  - K02 (0.25 - 0.50): Forward Dolly (smooth perspective advance toward pedestal)
 *  - K03 (0.50 - 0.75): Installation Focus (side arc revealing thickness, depth & refraction)
 *  - K04 (0.75 - 1.00): Transition Alignment (framing top-right curved corridor to Profile Gallery)
 *
 * 100% Reversible, deterministic Catmull-Rom spline path with zero text occlusion.
 */

import * as THREE from 'three';

export class CameraController {
  constructor(camera) {
    this.camera = camera;
    this.currentPosition = new THREE.Vector3();
    this.currentTarget = new THREE.Vector3();

    // Desktop waypoints matching reference board:
    // Installation is centered at X = 1.8, perfectly balancing the screen between left Hero and right Nav.
    this.desktopWaypoints = {
      positions: [
        new THREE.Vector3(0.0, 2.3, 13.5),   // K01 Establishing Shot
        new THREE.Vector3(0.8, 1.9, 8.5),    // K02 Forward Dolly
        new THREE.Vector3(4.2, 1.8, 5.0),    // K03 Installation Focus (Right arc)
        new THREE.Vector3(7.2, 2.2, -5.2)    // K04 Corridor Transition (aligned with doorway)
      ],
      targets: [
        new THREE.Vector3(1.8, 2.6, 0.0),    // K01 Target
        new THREE.Vector3(1.8, 2.1, 0.0),    // K02 Target
        new THREE.Vector3(1.8, 1.8, 0.0),    // K03 Target
        new THREE.Vector3(12.5, 2.2, -12.0)  // K04 Target (looking through arched portal)
      ]
    };

    // Mobile waypoints (centered on X = 1.8)
    this.mobileWaypoints = {
      positions: [
        new THREE.Vector3(1.8, 4.8, 14.5),   // K01 Mobile
        new THREE.Vector3(1.8, 3.6, 9.5),    // K02 Mobile
        new THREE.Vector3(3.2, 2.8, 6.0),    // K03 Mobile
        new THREE.Vector3(6.2, 2.4, -4.0)    // K04 Mobile
      ],
      targets: [
        new THREE.Vector3(1.8, 1.8, 0.0),
        new THREE.Vector3(1.8, 1.6, 0.0),
        new THREE.Vector3(1.8, 1.6, 0.0),
        new THREE.Vector3(11.5, 2.2, -11.0)
      ]
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

  /**
   * Update camera position and lookAt based on normalized progress p in [0, 1]
   * @param {number} p - Normalized scene progress [0, 1]
   */
  update(p) {
    const clampedP = Math.min(1, Math.max(0, p));
    this.posCurve.getPoint(clampedP, this.currentPosition);
    this.targetCurve.getPoint(clampedP, this.currentTarget);

    this.camera.position.copy(this.currentPosition);
    this.camera.lookAt(this.currentTarget);
  }
}
