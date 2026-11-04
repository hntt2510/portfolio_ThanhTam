# Project Museum — Progress Tracker

**Updated:** 2026-11-04 (Asia/Ho_Chi_Minh)  
**Repository:** https://github.com/hntt2510/portfolio_ThanhTam  
**Integration branch:** `main`  

## Current milestone status

| Milestone | State | Evidence | Remaining validation |
|---|---|---|---|
| 01 — Initial Entrance Atrium Three.js | Committed | `ed69536`, `index.html`, `app.js`, `src/world.js`, `src/scenes/entrance-atrium.js`, `src/camera-controller.js` | Procedural prototype superseded by Milestone 01B GLB integration |
| 01A — Blender graybox & GLB export | Committed | `9e50764`, `design-handoff/milestone-01A/` contains `.blend`, `.glb`, generator, K01–K04 PNGs, top-down render and report | Fully verified & exported 70-mesh GLB (1.18 MB) |
| 01B — Import Blender GLB into website | Committed & Verified | `75e8452`, `entrance-atrium.glb` integrated in `src/scenes/entrance-atrium.js`, `src/camera-controller.js` waypoints K01–K04 aligned, 8 automated Playwright screenshots in `design-handoff/milestone-01B/screenshots/`, report in `verification-report.md` | Ready for Milestone 02 (Profile Gallery) |
| 02A — Profile Gallery Blender Architecture & GLB | Committed & Verified | `956746b`, `design-handoff/milestone-02/` contains `profile-gallery.blend`, `profile-gallery.glb` (126.66 KB), `generate_profile_gallery.py`, proof renders `camera-K05.png`–`K08.png`, `top-down-layout.png`, `seam-continuity.png`, `asset-report-02A.md` | Ready for Milestone 02B (Three.js integration) |
| 02B — Profile Gallery Three.js Integration & UI | **Committed & Verified** | `profile-gallery.glb` integrated in `src/scenes/profile-gallery.js`, `src/world.js` dual-scene manager, `src/camera-controller.js` continuous K01–K08 spline, 4 narrative beats in `index.html` & `styles.css`, chapter schedule in `app.js`, 9 Playwright verification screenshots in `design-handoff/milestone-02/screenshots/`, report in `verification-report.md` | Ready for Milestone 03 (Core Expertise) design handoff |

## Approved design constraints

- Glass & Light Museum; Circular Atrium and circular skylight.
- Three staggered frosted-glass panels, subtle highlights and restrained reflections.
- Bright warm-white / silver / pale blue palette; no dark navy or neon.
- Hero content left; fixed scroll-aware vertical navigation right.
- Camera beats K01 Establishing, K02 Approach, K03 Focus, K04 Transition.
- One persistent 3D world, reversible normalized scroll, HTML overlays for readable content.
- Incremental development: design/approve/handoff/build/verify each milestone before the next.

## Milestone 01B Delivery Summary (2026-11-03)

- **Source Asset:** Loaded `design-handoff/milestone-01A/entrance-atrium.glb` into `src/scenes/entrance-atrium.js`, completely replacing procedural geometry.
- **Vendor Tooling:** Packaged offline `GLTFLoader.js` and `BufferGeometryUtils.js` in `assets/vendor/` and linked via import map in `index.html`.
- **Coordinate Reconciliation:** Mapped Blender $Z$-up to Three.js $Y$-up ($X = X, Y = Z, Z = -Y$).
- **Camera Motion:** Catmull-Rom spline trajectory with dynamic FOV interpolation across K01 (22mm / 57°), K02 (35mm / 46°), K03 (~45mm / 42°), K04 (32mm / 48°).
- **Material Tuning:** Luminous frosted glass (`MeshPhysicalMaterial`) catching subtle daylight highlights, transparent skylight dome, brushed aluminum trims, and stone plinth with LED halo.
- **Decals & Typography:** Applied high-resolution, unskewed canvas decals ("01 Business Analysis", "02 Enterprise Systems", "03 Technology Solutions").
- **Verification Evidence:**
  - Automated tests via Playwright in `design-handoff/milestone-01B/test_and_capture.py`.
  - Desktop 1440x900 screenshots (K01, K02, K03, K04, Reverse Scroll).
  - Mobile 390x844 responsive screenshots (K01, K03).
  - 2D Canvas fallback screenshot.
  - Console hygiene: 0 errors, 0 warnings.
  - Detailed report: `design-handoff/milestone-01B/verification-report.md`.

## Milestone 02A Delivery Summary (2026-11-04)

- **Blender Generator Script:** Created `design-handoff/milestone-02/generate_profile_gallery.py` building a curved gallery architecture with 39 modular meshes adhering to the `PRG_` prefix.
- **Physical Seam Continuity:** Connects cleanly to Scene 01's north-east corridor portal at $(15.0, 15.0, 0.0)$ with zero floor or wall discontinuity.
- **Curved Layout:** Radius $R = 25.0\text{m}$, gallery width $W = 5.20\text{m}$, sweeping from $\alpha = 135^\circ$ to $\alpha = 65^\circ$.
- **Asset Verification:** Exported `design-handoff/milestone-02/profile-gallery.glb` (126.66 KB, 3,280 vertices, 1,646 polygons, 7 safe glTF PBR materials, 0 lights, 0 cameras).
- **Proof Renders:** Headless Blender 5.2.3 LTS renders for K05, K06, K07, K08, top-down overview, and corridor seam check.
- **Spec Adherence:** 100% background architecture. Zero 3D text/panels inside GLB. Detailed technical report in `design-handoff/milestone-02/asset-report-02A.md`.

## Milestone 02B Delivery Summary (2026-11-04)

- **Runtime Asset Integration:** Integrated `profile-gallery.glb` into `src/scenes/profile-gallery.js` within the single persistent Three.js world managed by `src/world.js`.
- **Material Realization:** Applied `MeshPhysicalMaterial` clear architectural glazing with subtle sky specular highlights, brushed aluminum mullions/trims, polished stone floor/benches, warm plaster walls, and warm cove LED illumination.
- **Camera Spline Trajectory:** Implemented continuous Catmull-Rom spline path in `src/camera-controller.js` seamlessly continuing from K04 $(4.80, 1.80, -4.80)$ into K05 $\to$ K06 $\to$ K07 $\to$ K08 $(36.95, 1.80, -21.54)$ with zero jump, pop, or teleport.
- **Editorial DOM Overlay:** Built 4 narrative beats in `index.html` & `styles.css` (Entry, Foundation, Experience, Perspective) in screen-fixed frosted glass card overlay with smooth sequential cross-fading and zero blank gaps. Strictly zero 3D text on meshes.
- **Navigation & Chapter Schedule:** Centralized global-to-local chapter scheduler in `app.js` with active state indicator switching between `01 Introduction` and `02 About` and two-way jump click navigation.
- **Verification Evidence:**
  - Automated tests via Playwright in `design-handoff/milestone-02/test_and_capture_02B.py`.
  - Desktop 1440x900 screenshots (K01, K04 seam, K05 Beat 1, K06 Beat 2, K07 Beat 3, K08 Beat 4, Reverse Scroll, Nav Click Jump).
  - Mobile 390x844 responsive screenshots (K01, K05, K07).
  - 2D Canvas fallback screenshot.
  - Console hygiene: 0 errors, 0 warnings.
  - Detailed report: `design-handoff/milestone-02/verification-report.md`.

## Next task — Milestone 03: Core Expertise Scene

1. Prepare design specification and handoff package for Scene 03 (Core Expertise) extending from the exit threshold archway of Profile Gallery.
2. Review and obtain user approval on Scene 03 visual direction and content copy before commencing 3D grayboxing.

## GitHub publishing rules

After each successfully verified completed unit of work, the implementation agent must commit and push to GitHub automatically without a separate approval prompt, subject to safe Git practices and repository protection. Never assert remote success without confirming the remote SHA. See `AGENTS.md`.
