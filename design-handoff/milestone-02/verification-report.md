# Milestone 02C — Profile Gallery Visual Polish & C1 Motion Verification Report

**Date:** 2026-11-04  
**Subject:** Milestone 02C Visual Polish (Unboxed Editorial UI, Slim Mullion Architectural Refinement, Flush Ceiling Arch, Natural Garden Terrace, C1 Mathematical Motion Continuity, Console Hygiene)  
**Target Repository:** `hntt2510/portfolio_ThanhTam`  
**Integration Branch:** `main`  
**Portfolio Owner:** Hoàng Nguyễn Thành Tâm  

---

## 1. Executive Summary

Milestone 02C brings the Profile Gallery into full visual and architectural alignment with the approved Glass & Light Museum design direction (`SCENE02-V2-APPROVED.md` and `REVIEW-02C-VISUAL-ACCEPTANCE.md`).

All four core priorities have been implemented and verified:
1. **Editorial UI:** Completely eliminated frosted-glass boxed card styling, borders, corner radii, and box-shadows. The About typography floats directly over the 3D museum environment supported by a seamless full-height vertical gradient wash on desktop and an unboxed upward wash on mobile. Full Vietnamese diacritics (**Hoàng Nguyễn Thành Tâm**) are applied across all text layers.
2. **Architectural Visual Quality:** Upgraded Blender and Three.js models from graybox to daylight museum architecture: 11 glazed bays with slim silver aluminum mullions (5cm × 10cm) and horizontal transoms at 1.6m and 3.6m; replaced low-hanging ceiling threshold beam with a flush arched portal at ceiling height ($Z = 4.98\text{m}$); polished warm travertine floor with daylight highlights; layered garden terrace outside with manicured lawn, curved hedge row, and 5 organic canopy tree clusters. Strictly zero 3D text or floating plaques in the 3D scene.
3. **Scroll Motion & Mathematical Continuity:** Upgraded camera spline to a unified master Catmull-Rom spline with Hermite cubic time mapping and centripetal knot ratio compensation ($1.0792$). First-derivative ($C^1$) velocity discontinuity across the $p = 0.40$ seam was numerically proven to be $\le 0.153\%$ ($< 2\%$ target threshold). About copy transitions evaluate directly from chapter-local scroll progress via algebraic Hermite easing with zero CSS delay.
4. **Verification:** Automated Playwright Chromium suite captured desktop K01–K08, reverse scroll K01, navigation clicks, mobile K01/K05/K07, and 2D canvas fallback. Console audit verified **0 console errors, 0 console warnings, and 0 failed network requests**.

---

## 2. Deliverables & Modified Artifacts

| Component | Path / Location | Description |
|---|---|---|
| Source Blender 3D Model | `design-handoff/milestone-02/profile-gallery.blend` | 11 window bays, slim mullions, flush exit arch, organic garden trees |
| Blender Generation Script | `design-handoff/milestone-02/generate_profile_gallery.py` | Parametric procedural generator for Profile Gallery architecture |
| Runtime 3D Model (GLB) | `design-handoff/milestone-02/profile-gallery.glb` & `assets/models/profile-gallery.glb` | GLTF binary asset (129.7 KB, 63 modular meshes) |
| Blender Render Proofs | `design-handoff/milestone-02/camera-K05.png` to `camera-K08.png`, `top-down-layout.png`, `seam-continuity.png` | Native Blender Cycles renders confirming materials, mullions, and lighting |
| Three.js Scene Module | `src/scenes/profile-gallery.js` | Material tuning: clear architectural glass (`MeshPhysicalMaterial`), travertine floor, plaster walls, cove LED strip |
| Camera Spline Controller | `src/camera-controller.js` | Unified master Catmull-Rom spline with knot ratio compensated Hermite cubic time mapping |
| Editorial Interface Overlay | `index.html` | Unboxed HTML narrative beats with full Vietnamese diacritics: **Hoàng Nguyễn Thành Tâm** |
| Design System & Layout | `styles.css` | Unboxed full-height column gradient wash on desktop, upward natural wash on mobile, text-shadow contrast |
| Scroll & Chapter Engine | `app.js` | Algebraic progress evaluation for copy opacity & translateY ($12\text{px} \to 0 \to -12\text{px}$), chapter syncing |
| Automated QA Test Suite | `design-handoff/milestone-02/test_and_capture_02C.py` | Headless Chromium automated verification runner and screenshot recorder |
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
3. **K05 About Entry Beat 1** (`desktop-03-k05-about-entry.png`): "From Software Engineering to Enterprise Problem Solving"; `02 About` nav active at 48%; unboxed full-height column wash; slim silver mullions.
4. **K06 Foundation Beat 2** (`desktop-04-k06-about-foundation.png`): "Built on a Technical Foundation"; academic focus at FPT University; glazed colonnade framing lawn and canopy trees.
5. **K07 Experience Beat 3** (`desktop-05-k07-about-experience.png`): "Turning Requirements into Solutions"; practical analysis and consulting; zero box boundaries around typography.
6. **K08 Perspective Beat 4** (`desktop-06-k08-about-perspective.png`): "Connecting Business & Technology"; flush ceiling archway at $Z = 4.98\text{m}$; zero intruding foreground ceiling beams.
7. **Reverse Scroll Reversibility** (`desktop-07-reverse-scroll-k01.png`): Full reverse scroll from 1.0 back to 0.0 smoothly restores K01 hero state with zero visual drift.
8. **Navigation Jump Interaction** (`desktop-08-nav-click-about.png`): Clicking `02 About` scrolls smoothly to progress 0.41, activating Chapter 02 and transitioning camera.

### Mobile Viewport (390 × 844)
1. **Mobile K01 Establishing** (`mobile-01-k01-establishing.png`): Portrait framing of atrium plinth and hero sheet.
2. **Mobile K05 Entry Beat** (`mobile-02-k05-about-entry.png`): Unboxed natural upward gradient wash displaying Beat 1 text; borderless bottom edge.
3. **Mobile K07 Experience Beat** (`mobile-03-k07-about-experience.png`): Beat 3 text with clean typography, 0 horizontal overflow, touch-friendly padding.

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

## 6. Known Limitations & Next Steps

- **Scene 03 Preparation:** The exit threshold portal archway is structurally complete and positioned at $(43.24, 4.98, -19.98)$ in Three.js coordinates, ready to connect directly into Scene 03 (Core Expertise) when authorized.
- **Approved Scope Stop:** As instructed, Scene 03 has not been implemented. Work stops after Milestone 02C.
