# Milestone 01B — Blender GLB Integration & Verification Report
**Project:** Glass & Light Museum / Entrance Atrium  
**Milestone:** 01B — Three.js GLB Integration, Camera Waypoints & Visual QA  
**Date:** 2026-11-03  
**Status:** COMPLETE (Automated Verification Passed)  

---

## 1. Executive Summary

Milestone 01B has successfully integrated the native Blender 3D model ([`entrance-atrium.glb`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01A/entrance-atrium.glb)) into the persistent Three.js runtime world of the portfolio web application. All procedural atrium geometries have been replaced with the verified GLB architecture without duplicating geometry.

The runtime now features:
- **Architectural Asset Integration:** Complete loading of 70 named meshes from `entrance-atrium.glb` (1.18 MB) via vendor-bundled `GLTFLoader`.
- **Coordinate Reconciliation:** Full alignment between Blender ($Z$-up) and Three.js ($Y$-up) coordinate systems ($X_{\text{Three}} = X_{\text{Blender}}, Y_{\text{Three}} = Z_{\text{Blender}}, Z_{\text{Three}} = -Y_{\text{Blender}}$).
- **Physical Material Upgrades:** Real-time architectural frosted glass (`MeshPhysicalMaterial`), translucent skylight dome, brushed aluminum trims, and polished light-stone plinth with an ambient LED halo.
- **In-Scene Typography Decals:** High-resolution typographic decals for *01 Business Analysis*, *02 Enterprise Systems*, and *03 Technology Solutions* attached directly to the glass monoliths.
- **Deterministic Camera Waypoints:** Catmull-Rom spline camera trajectory smoothly interpolating position, target, and lens FOV across beats K01 $\to$ K02 $\to$ K03 $\to$ K04.
- **100% Scroll Reversibility:** Camera moves forward and backward with pixel-identical determinism.
- **Responsive Layout & UI Protection:** Left-hand Hero overlay is fully protected and transitions cleanly, with zero horizontal scroll on mobile (390px) or desktop (1440px/1920px).
- **Console Hygiene:** `0` errors, `0` warnings, `0` 404 network failures.

---

## 2. Reconciled Coordinate Systems & Camera Waypoints

All camera waypoints and scene positions were translated from Blender graybox measurements:

$$\begin{aligned}
X_{\text{Three.js}} &= X_{\text{Blender}} \\
Y_{\text{Three.js}} &= Z_{\text{Blender}} \\
Z_{\text{Three.js}} &= -Y_{\text{Blender}}
\end{aligned}$$

### Desktop Waypoint Schedule (1440px / 1920px)

| Beat | Normalized Scroll $p$ | Three.js Position `(X, Y, Z)` | Three.js Target `(X, Y, Z)` | Lens FOV | Compositional Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **K01** | `0.00` | `(0.00, 1.90, 10.20)m` | `(1.00, 2.90, -0.20)m` | $57.0^\circ$ (22mm) | **Wide Establishing Hero:** Frames full atrium, skylight, plinth; preserves left negative space for Hero text overlay. |
| **K02** | `0.33` | `(0.70, 1.85, 4.80)m` | `(1.40, 1.70, 0.00)m` | $46.0^\circ$ (35mm) | **Forward Dolly:** Eye-level advance toward the plinth; reveals plinth rim and background corridor opening. |
| **K03** | `0.66` | `(0.60, 1.75, 3.60)m` | `(1.45, 1.65, 0.00)m` | $42.0^\circ$ (~45mm) | **Installation Focus:** Three-quarters perspective revealing depth, glass stagger, aluminum trim, and mounting shoes. |
| **K04** | `1.00` | `(4.80, 1.80, -4.80)m` | `(12.00, 1.80, -12.00)m` | $48.0^\circ$ (32mm) | **Corridor Transition:** Aligned straight down the North-East corridor towards Milestone 02 (Profile Gallery); Hero text fades to 0% opacity. |

### Mobile Waypoint Schedule (390px Portrait)

| Beat | Three.js Position `(X, Y, Z)` | Three.js Target `(X, Y, Z)` | Lens FOV | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **K01** | `(0.40, 2.30, 12.80)m` | `(1.20, 2.70, 0.00)m` | $58.0^\circ$ | Pulled back along $Z$ to keep oculus skylight and glass monoliths visible above mobile Hero card. |
| **K02** | `(0.85, 2.00, 6.50)m` | `(1.40, 1.75, 0.00)m` | $48.0^\circ$ | Centered dolly on plinth. |
| **K03** | `(0.60, 1.75, 4.20)m` | `(1.45, 1.65, 0.00)m` | $44.0^\circ$ | Focuses on panels and legible typography. |
| **K04** | `(4.80, 1.80, -4.80)m` | `(12.00, 1.80, -12.00)m` | $50.0^\circ$ | Frames corridor portal. |

---

## 3. Material Upgrades & Lighting Architecture

| Mesh Group | Runtime Material Configuration | Optical Behavior |
| :--- | :--- | :--- |
| **Frosted Glass Monoliths** (`ATR_GlassPanel_01..03`) | `MeshPhysicalMaterial`: `color: 0xF0F7FD`, `roughness: 0.22`, `metalness: 0.06`, `clearcoat: 1.0`, `clearcoatRoughness: 0.12`, `opacity: 0.65`, `transparent: true` | Translucent, bright, luminous architectural frosted glass that catches specular sunlight gleams without black refraction artifacts. |
| **Skylight Oculus Glass** (`ATR_SkylightGlass`) | `MeshPhysicalMaterial`: `color: 0xEEF6FD`, `roughness: 0.12`, `opacity: 0.70`, `transparent: true`, `clearcoat: 1.0` | Natural sky dome diffusion overhead. |
| **Mezzanine Railing** (`ATR_MezzanineRailingGlass`) | `MeshPhysicalMaterial`: `color: 0xEDF5FB`, `roughness: 0.10`, `opacity: 0.60`, `transparent: true` | Architectural tempered glass balustrade. |
| **Floor & Pedestal** (`ATR_Floor`, `ATR_Pedestal`) | `MeshStandardMaterial`: `color: 0xF7F8F5`, `roughness: 0.40`, `metalness: 0.04`, `receiveShadow: true` | Polished light stone receiving natural soft daylight shadows. |
| **Brushed Aluminum** (Trims, Mullions, Rings, Shoes) | `MeshStandardMaterial`: `color: 0xE2E7EC`, `metalness: 0.25`, `roughness: 0.35` | Satin metallic finish with realistic highlight rolloff. |
| **Architecture** (Walls, Pilasters, Soffits) | `MeshStandardMaterial`: `color: 0xF8F9F7`, `roughness: 0.85`, `metalness: 0.02` | Warm-white matte plaster. |
| **LED Recesses & Halo** (`FloorHalo`, `CoveLight`) | `MeshBasicMaterial`: `#6F9EC8` (halo), `#FFFDF8` (cove light) | Restrained architectural illumination. |

---

## 4. Visual QA & Verification Evidence

All tests were executed programmatically using Chromium (Playwright headless):

| Test Case | Screenshot Artifact | Verification Result |
| :--- | :--- | :--- |
| **Desktop K01 (Establishing)** | [`desktop-k01-establishing.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/desktop-k01-establishing.png) | **PASS**: Full hall, oculus, and monoliths framed; left hero text overlay protected. |
| **Desktop K02 (Forward Dolly)** | [`desktop-k02-dolly.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/desktop-k02-dolly.png) | **PASS**: Smooth zoom toward pedestal; clear depth between panels; corridor visible right. |
| **Desktop K03 (Installation Focus)** | [`desktop-k03-focus.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/desktop-k03-focus.png) | **PASS**: Staggered monoliths, typography decals, mounting shoes, and glass sheen sharply rendered. |
| **Desktop K04 (Transition)** | [`desktop-k04-transition.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/desktop-k04-transition.png) | **PASS**: Straight-line passage down North-East corridor; Hero UI cleanly faded to 0% opacity. |
| **Scroll Reversibility** | [`desktop-reverse-scroll-k01.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/desktop-reverse-scroll-k01.png) | **PASS**: Scrolled $0.0 \to 1.0 \to 0.0$; exactly matches K01 starting state with zero drift. |
| **Mobile K01 (Establishing)** | [`mobile-k01-establishing.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/mobile-k01-establishing.png) | **PASS**: 390px portrait view cleanly framed; bottom hero card readable; zero overflow. |
| **Mobile K03 (Focus)** | [`mobile-k03-focus.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/mobile-k03-focus.png) | **PASS**: Monoliths fill vertical space; decals and chapter badge aligned. |
| **2D Canvas Fallback** | [`fallback-2d-canvas.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-01B/screenshots/fallback-2d-canvas.png) | **PASS**: WebGL context disabled; 2D canvas renders architectural concentric rings and frosted cards. |
| **Console Errors / Warnings** | Automated Audit | **PASS**: `0` Errors, `0` Warnings. |

---

## 5. Scope Boundaries Maintained

- **No Duplication:** Procedural geometry completely replaced by `entrance-atrium.glb`.
- **Zero Framework Bloat:** Kept native ES Modules architecture with vendor-bundled Three.js and `GLTFLoader`.
- **Scene 02 Unbuilt:** Milestone 02 (Profile Gallery) boundary respected at corridor threshold.

---

*Verified by Autonomous Web & 3D Agent for Antigravity Portfolio Project.*
