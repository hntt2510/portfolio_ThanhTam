# Milestone 03A — Hard Preflight & Coordinate Reconciliation Audit

**Date:** 2026-11-04  
**Auditor:** Antigravity (Milestone 03A Technical Modeling & Asset Pipeline Agent)  
**Status:** **PREFLIGHT PASSED · PROCEED TO 03A MODELING**

---

## 1. Runtime K08 Anchor Verification (`src/camera-controller.js`)

A direct audit of the live runtime source code at `src/camera-controller.js` was conducted prior to executing any 3D modeling scripts:

| Parameter | Live Runtime Value in `src/camera-controller.js` | Status | Notes |
|---|---|:---:|---|
| **Desktop K08 Position (W8)** | `THREE.Vector3(36.53, 1.80, -21.62)` | ✅ Verified | Preserved from Milestone 02D |
| **Desktop K08 Target (W8)** | `THREE.Vector3(43.24, 2.20, -19.98)` | ✅ Verified | Center of arched exit portal opening |
| **Desktop K08 FOV (Index 8)** | **`48.0°`** (vertical FOV) | ✅ Verified | **Reconciled:** Matches runtime. 46° draft value rejected. |
| **Mobile K08 Position (W8)** | `THREE.Vector3(36.53, 1.88, -21.62)` | ✅ Verified | Preserved from Milestone 02D |
| **Mobile K08 Target (W8)** | `THREE.Vector3(43.24, 2.20, -19.98)` | ✅ Verified | Identical target vector |
| **Mobile K08 FOV (Index 8)** | **`50.0°`** (vertical FOV) | ✅ Verified | **Reconciled:** Matches runtime. 48° draft value rejected. |

### Strict Rule Observed
**Zero edits were or will be made to `src/camera-controller.js` or any runtime code in Milestone 03A.**  
The live K08 FOV is the authoritative truth for the existing scene's exit. All preview cameras in Blender will render K08 at exactly $48.0^\circ$ (desktop) and $50.0^\circ$ (mobile).

---

## 2. Physical Junction & Coordinate Reconciliation

### 2.1 Coordinate Mapping Convention
Metric scale ($1\text{ Blender Unit} = 1.0\text{ meter}$):
$$\begin{aligned}
X_{\text{Three.js}} &= X_{\text{Blender}} \\
Y_{\text{Three.js}} &= Z_{\text{Blender}} \quad (\text{Vertical Elevation Up}) \\
Z_{\text{Three.js}} &= -Y_{\text{Blender}} \quad (\text{North / Forward})
\end{aligned}$$

### 2.2 Scene 02 Exit Portal Geometry Anchor
Inspected from `design-handoff/milestone-02/generate_profile_gallery.py` and `profile-gallery.glb`:
- **Portal Center Anchor:**
  - Blender: $(43.24, 19.98, 0.00)$
  - Three.js: $(43.24, 0.00, -19.98)$
- **Corridor Exit Tangent Angle:**
  - $\alpha_{\text{exit}} = 65.0^\circ$
  - $\theta_{\text{tangent}} = \alpha_{\text{exit}} - 90^\circ = -25.0^\circ$
  - Tangent unit vector in Blender: $(\cos(-25^\circ), \sin(-25^\circ), 0) = (0.9063, -0.4226, 0.0)$
  - Tangent unit vector in Three.js: $(0.9063, 0.00, 0.4226)$
- **Portal Opening Aperture:**
  - Arched portal `PRG_Portal_ArchedWall`: Arch span $W = 3.60\text{m}$, Arch spring height $H_{\text{spring}} = 2.70\text{m}$, Arch crown height $H_{\text{top}} = 4.50\text{m}$.
  - Vestibule alcove extends $4.20\text{m}$ along tangent vector to:
    $$\begin{aligned}
    X_{\text{vestibule}} &= 43.24 + 4.20 \times 0.9063 = 47.05\text{m} \\
    Y_{\text{vestibule}} &= 19.98 + 4.20 \times (-0.4226) = 18.20\text{m} \quad (\text{Three.js } Z = -18.20\text{m})
    \end{aligned}$$

### 2.3 Watertight Seam Connection Strategy for 03A
To guarantee a physically watertight junction with zero light leakage, floating gaps, or geometry clipping:
- Scene 03's entrance collar (`EXPM_Portal_EntryVestibule`) will overlap the Scene 02 alcove opening by $20\text{cm}$ ($0.20\text{m}$) along the tangent vector, aligning vertex profiles at the outer perimeter of the archway.
- Floor paving transitions seamlessly with light travertine slabs at $Z = 0.00\text{m}$.

---

## 3. Waypoint Ledger for 03A Preview Cameras

The 03A production Blender file will incorporate dedicated review cameras with correct sensor sizes and vertical FOVs:

| Waypoint | Three.js Position | Three.js Target | Blender Pos $(X, Y, Z)$ | Blender Tgt $(X, Y, Z)$ | FOV (Desk / Mob) | Camera Purpose |
|---|---|---|---|---|:---:|---|
| **K08** | `(36.53, 1.80, -21.62)` | `(43.24, 2.20, -19.98)` | `(36.53, 21.62, 1.80)` | `(43.24, 19.98, 2.20)` | **$48.0^\circ$ / $50.0^\circ$** | Seam verification vs Scene 02 |
| **K09** | `(44.50, 1.85, -19.40)` | `(55.80, 3.80, -14.10)` | `(44.50, 19.40, 1.85)` | `(55.80, 14.10, 3.80)` | $52.0^\circ$ / $54.0^\circ$ | Volumetric reveal of sawtooth hall |
| **K10** | `(49.50, 3.20, -14.20)` | `(57.80, 0.20, -10.30)` | `(49.50, 14.20, 3.20)` | `(57.80, 10.30, 0.20)` | $46.0^\circ$ / $48.0^\circ$ | Elevated oblique view of process paths |
| **K11** | `(56.80, 1.85, -11.20)` | `(58.50, 2.20, -4.50)` | `(56.80, 11.20, 1.85)` | `(58.50, 4.50, 2.20)` | $48.0^\circ$ / $50.0^\circ$ | Side-tracking view of modular System Spine |
| **K12** | `(63.20, 4.05, -8.20)` | `(75.00, 4.20, -2.80)` | `(63.20, 8.20, 4.05)` | `(75.00, 2.80, 4.20)` | $50.0^\circ$ / $52.0^\circ$ | Elevated bridge glide to Scene 04 portal |

---

## 4. Verification Checkpoint

- [x] K08 desktop FOV verified as **$48.0^\circ$** in `src/camera-controller.js`.
- [x] K08 mobile FOV verified as **$50.0^\circ$** in `src/camera-controller.js`.
- [x] Runtime code confirmed untouched and locked.
- [x] Geometry coordinates, tangent angles, and vestibule offsets verified against Scene 02 generator script.
- [x] Preflight complete. Ready to proceed to production 3D asset generation in Blender 5.2.3 LTS.