# Milestone 02D — Profile Gallery Visual Fidelity Verification Report

**Date:** 2026-11-04  
**Subject:** Milestone 02D Visual Fidelity Pass (Sculpted Exit Portal Archway, Multi-Scale Botanical Landscaping, Ultra-Slim Silver Mullions, Polished Travertine Sheen, High-Contrast Brand Typography)  
**Target Repository:** `hntt2510/portfolio_ThanhTam`  
**Integration Branch:** `main`  
**Portfolio Owner:** Hoàng Nguyễn Thành Tâm  

---

## 1. Executive Summary

Milestone 02D elevates the Profile Gallery from an architectural graybox to the approved contemporary Glass & Light Museum aesthetic defined in `SCENE02-V2-APPROVED.md` and `scene02-approved-visual-board-v2.png`, resolving all creative QA points from `REVIEW-02D-VISUAL-FIDELITY.md`.

All required improvements were implemented and verified with zero functional regressions:
1. **Museum Architecture & Material Depth:**
   - Designed and integrated a **sculpted architectural exit portal** (`PRG_Portal_ArchedWall`) featuring a smooth semicircular archway ($W = 3.60\text{m}$, $H = 4.50\text{m}$) and daylit vestibule alcove with rear vista window and stone plinth bench (`PRG_Portal_AlcoveBench`), providing a legible, inviting threshold leading toward Scene 03.
   - Upgraded floor material to physical polished travertine (`MeshPhysicalMaterial`, roughness 0.18, clearcoat 0.50, reflectivity 0.70) catching natural window specular highlights.
   - Rebalanced scene ambient baseline lighting ($1.25 \to 0.45$) to allow the $2.8\text{ lux}$ directional sunlight to cast crisp, soft daylight shadows across the gallery floor.
2. **Exterior Landscaping Overhaul:**
   - Eliminated simplistic UV-sphere green clusters. Replaced with **multi-scale botanical garden trees** featuring tapered, branching trunks (`PRG_Tree_XX_Trunk`) and multifaceted organic leaf crowns (`PRG_Tree_XX_Canopy_X`) with two-tone sunlight materials (`#58883E` and `#365922`).
   - Added manicured boxwood hedge row (`PRG_BoxwoodHedge`), crisp stone garden curb (`PRG_GardenCurb`), curved lawn turf, and daylight sky backdrop dome.
3. **Ultra-Slim Silver Mullions & Negative Space:**
   - Reduced mullion dimensions from $5\text{cm} \times 10\text{cm}$ to ultra-slim $3.5\text{cm} \times 7\text{cm}$ and transom profile to $3\text{cm}$.
   - Assigned bright brushed silver aluminum PBR material (`#EEF3F8`, metallic 0.75, roughness 0.22).
   - Tuned camera waypoint W7 (K07) to maintain $3.0\text{m}$ clearance from the glazed facade, opening up generous negative space for the headline with zero mullions crossing through the text.
4. **Brand Contrast & Unboxed Editorial UI:**
   - Strengthened brand header styling: icon in deep rich graphite (`#111827`), title in bold `#111827`, and owner subtitle **Hoàng Nguyễn Thành Tâm / 2026** in prominent `#1F2937` with crisp multi-layer white text shadow, achieving 100% legibility.
   - Preserved unboxed full-height column gradient wash on desktop and upward natural wash on mobile.
5. **Scroll Motion & Mathematical Continuity:**
   - Preserved continuous master Catmull-Rom spline with knot ratio compensation ($1.0792$).
   - Finite difference numerical evaluation ($\epsilon = 0.0002$) proved relative velocity discontinuity $\le 0.153\%$ ($< 2.0\%$ target) and exact $C^0$ continuity across the $p = 0.40$ boundary.
6. **Automated Verification:**
   - Automated Playwright suite verified desktop K01–K08, reverse scroll K01, navigation clicks, mobile K01/K05/K07, and 2D canvas fallback with **0 console errors, 0 warnings, and 0 failed requests**.

---

## 2. Deliverables & Modified Artifacts

| Component | Path / Location | Description |
|---|---|---|
| Source Blender 3D Model | `design-handoff/milestone-02/profile-gallery.blend` | Sculpted arch portal, botanical branching trees, slim mullions, garden terrace |
| Procedural Blender Generator | `design-handoff/milestone-02/generate_profile_gallery.py` | Parametric procedural generator for Profile Gallery architecture |
| Runtime 3D Model (GLB) | `design-handoff/milestone-02/profile-gallery.glb` & `assets/models/profile-gallery.glb` | Clean GLTF binary asset (407.34 KB, 68 modular meshes) |
| Blender Render Proofs | `design-handoff/milestone-02/camera-K05.png` to `camera-K08.png`, `top-down-layout.png`, `seam-continuity.png` | Native Blender EEVEE/Cycles renders confirming materials, mullions, and lighting |
| Three.js Scene Module | `src/scenes/profile-gallery.js` | PBR material assignments, physical stone floor, daylight sun and portal lighting |
| Scene Lighting Balancing | `src/scenes/entrance-atrium.js` & `src/world.js` | Rebalanced ambient lights, sky daylight white background `0xF5F8FA` |
| Camera Spline Controller | `src/camera-controller.js` | Unified master Catmull-Rom spline with refined W7 negative space and W8 portal framing |
| Editorial Interface Overlay | `index.html` | Unboxed HTML narrative beats with full Vietnamese diacritics: **Hoàng Nguyễn Thành Tâm** |
| Design System & Layout | `styles.css` | High-contrast brand typography, unboxed full-height column wash on desktop, upward natural wash on mobile |
| Automated QA Test Suite | `design-handoff/milestone-02/test_and_capture_02D.py` | Headless Chromium automated verification runner and screenshot recorder |
| Verification Screenshots | `design-handoff/milestone-02/screenshots/` | 12 high-resolution screenshots covering desktop, mobile, reverse scroll, and fallback |

---

## 3. Numerical C0 & C1 Continuity Proof

Evaluated numerically across the Scene 01 $\to$ Scene 02 boundary at $p = 0.40$ using symmetric central and one-sided finite differences with $\epsilon = 0.0002$:

```text
=== NUMERICAL CONTINUITY EVALUATION ACROSS p = 0.40 ===
Position C0 at p = 0.40:     (4.800, 1.800, -4.800) [Exact Match]
Target C0 at p = 0.40:       (12.000, 1.800, -12.000) [Exact Match]
FOV C0 at p = 0.40:          47.99° [Exact Match]

Left Velocity Vector vL:     (39.744, 0.187, -55.192)
Right Velocity Vector vR:    (39.744, 0.183, -55.088)
Velocity Magnitude ||v||:    68.01 units/progress
Velocity Difference ||vDiff||: 0.104 units/progress
Relative Velocity Discontinuity: 0.153% (< 2.0% specification)

FOV Derivative Diff:         0.000000°/progress [Continuous]
Result:                      [PASS] C0 and C1 Continuity Verified
```

---

## 4. Visual Evidence & Screenshots

### Desktop Viewport (1440 × 900)
1. **K01 Establishing Shot** (`desktop-01-k01-establishing.png`): Entrance Atrium establishing view; `01 Introduction` nav active at 00%; Hero overlay intact.
2. **K04 Transition Seam** (`desktop-02-k04-transition-seam.png`): Seamless passage through north-east corridor portal into Profile Gallery at progress 0.40; continuous travertine floor.
3. **K05 About Entry Beat 1** (`desktop-03-k05-about-entry.png`): "From Software Engineering to Enterprise Problem Solving"; high-contrast brand subtitle **Hoàng Nguyễn Thành Tâm / 2026**; multi-scale botanical trees and slim silver mullions outside.
4. **K06 Foundation Beat 2** (`desktop-04-k06-about-foundation.png`): "Built on a Technical Foundation"; organic tree crowns with two-tone leaf shading, manicured hedge row, and travertine benches.
5. **K07 Experience Beat 3** (`desktop-05-k07-about-experience.png`): "Turning Requirements into Solutions"; clear negative space on the left; sculpted arched portal visible down the corridor in perspective.
6. **K08 Perspective Beat 4** (`desktop-06-k08-about-perspective.png`): "Connecting Business & Technology"; camera frames the sculpted arched threshold portal with daylit alcove and plinth bench beyond, clearly introducing the opening to Scene 03.
7. **Reverse Scroll Reversibility** (`desktop-07-reverse-scroll-k01.png`): Full reverse scroll from 1.0 back to 0.0 smoothly restores K01 hero state with zero visual drift.
8. **Navigation Jump Interaction** (`desktop-08-nav-click-about.png`): Clicking `02 About` scrolls smoothly to progress 0.41, activating Chapter 02 and transitioning camera.

### Mobile Viewport (390 × 844)
1. **Mobile K01 Establishing** (`mobile-01-k01-establishing.png`): Portrait framing of atrium plinth and hero sheet.
2. **Mobile K05 Entry Beat** (`mobile-02-k05-about-entry.png`): Unboxed natural upward gradient wash displaying Beat 1 text; botanical trees and slim mullions visible above text.
3. **Mobile K07 Experience Beat** (`mobile-03-k07-about-experience.png`): Beat 3 text with clean typography, arched portal visible in perspective, touch-friendly padding.

### Fallback 2D Canvas Suite
1. **2D Canvas Rendering** (`desktop-09-fallback-2d.png`): Canvas renders architectural rings and concentric curves when WebGL is unavailable.

---

## 5. Console Audit & Browser Health

```text
=== CONSOLE AUDIT ===
Total console errors: 0
Total console warnings: 0
Total failed network requests (404/ERR): 0
[PASS] Strict Console Audit: 0 errors.
```

---

## 6. Scope Boundaries & Next Steps

- **Scene 03 Boundary Strictly Preserved:** As instructed by project rules, Scene 03 geometry has **not** been implemented. The sculpted archway at K08 provides an authentic architectural threshold framing that connects into Scene 03 when authorized.
- **Stop for Visual Review:** Work stops after Milestone 02D for visual review by the portfolio owner.
