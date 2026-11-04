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
| 02B — Profile Gallery Three.js Integration & UI | Committed & Verified | `dca778b`, `profile-gallery.glb` integrated in `src/scenes/profile-gallery.js`, `src/world.js` dual-scene manager, `src/camera-controller.js` continuous K01–K08 spline, 4 narrative beats in `index.html` & `styles.css`, chapter schedule in `app.js`, 9 Playwright verification screenshots in `design-handoff/milestone-02/screenshots/`, report in `verification-report.md` | Superseded by visual polish in Milestone 02C & 02D |
| 02C — Profile Gallery Visual Polish & C1 Motion | Committed & Verified | `7ff7a5e`, unboxed editorial UI, 11 bays with slim mullions, master spline C1 continuity | Superseded by visual fidelity pass in Milestone 02D |
| 02D — Profile Gallery Visual Fidelity Pass | Committed & Verified | Sculpted arch portal, botanical multi-scale trees, 3.5cm ultra-slim silver mullions, polished travertine floor sheen, high-contrast brand typography (`#111827`), 12 Playwright screenshots, report in `verification-report.md` | Ready for portfolio owner visual review. Scene 03 design planning may proceed. |

## Approved design constraints

- Glass & Light Museum; Circular Atrium and circular skylight.
- Three staggered frosted-glass panels, subtle highlights and restrained reflections.
- Bright warm-white / silver / pale blue palette; no dark navy or neon.
- Hero content left; fixed scroll-aware vertical navigation right.
- Camera beats K01 Establishing, K02 Approach, K03 Focus, K04 Transition, K05 Entry, K06 Foundation, K07 Experience, K08 Perspective.
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

## Milestone 02C Delivery Summary (2026-11-04)

- **Unboxed Editorial UI:** Eliminated frosted-glass card containers on desktop with full-height vertical gradient wash; unboxed upward wash on mobile. Full Vietnamese diacritics (**Hoàng Nguyễn Thành Tâm**).
- **Glazing & Mullions:** 11 bays with slim mullions and horizontal transoms.
- **Spline Motion:** Unified master Catmull-Rom spline with knot ratio compensation ($1.0792$); numerical finite-difference velocity relative error $0.153\%$ across $p = 0.40$.

## Milestone 02D Delivery Summary (2026-11-04) — Visual Fidelity Pass

- **Museum Architecture & Material Depth:**
  - Implemented a **sculpted architectural exit portal** (`PRG_Portal_ArchedWall`) with a smooth semicircular archway ($W = 3.60\text{m}$, $H = 4.50\text{m}$) and daylit vestibule alcove with rear vista window and stone plinth bench (`PRG_Portal_AlcoveBench`), introducing the architectural opening to Scene 03.
  - Rebalanced ambient scene lighting ($1.25 \to 0.45$) to allow $2.8\text{ lux}$ directional sunlight to cast crisp, soft daylight shadows across the floor.
  - Upgraded floor to physical polished travertine (`MeshPhysicalMaterial`, roughness 0.18, clearcoat 0.50, reflectivity 0.70) catching natural window specular highlights.
- **Exterior Landscaping Overhaul:**
  - Replaced low-poly UV-spheres with **multi-scale botanical garden trees** featuring tapered branching trunks (`PRG_Tree_XX_Trunk`) and multifaceted organic leaf crowns (`PRG_Tree_XX_Canopy_X`) with two-tone sunlight materials (`#58883E` and `#365922`).
  - Added manicured boxwood hedge row (`PRG_BoxwoodHedge`), crisp stone garden curb (`PRG_GardenCurb`), curved lawn turf, and daylight sky backdrop dome.
- **Ultra-Slim Silver Mullions & Negative Space:**
  - Reduced mullion dimensions from $5\text{cm} \times 10\text{cm}$ to ultra-slim $3.5\text{cm} \times 7\text{cm}$ and transom profile to $3\text{cm}$.
  - Assigned bright brushed silver aluminum PBR material (`#EEF3F8`, metallic 0.75, roughness 0.22).
  - Tuned camera waypoint W7 (K07) to maintain $3.0\text{m}$ clearance from the glazed facade, opening up generous negative space for the headline with zero mullions crossing through the text.
- **Brand Contrast & Unboxed Editorial UI:**
  - Strengthened brand header styling: icon in deep rich graphite (`#111827`), title in bold `#111827`, and owner subtitle **Hoàng Nguyễn Thành Tâm / 2026** in prominent `#1F2937` with crisp multi-layer white text shadow, achieving 100% legibility.
  - Preserved unboxed full-height column gradient wash on desktop and upward natural wash on mobile.
- **Verification Evidence:**
  - Automated Playwright suite `test_and_capture_02D.py` captured 12 high-resolution screenshots covering desktop K01–K08, reverse scroll, navigation click, mobile K01/K05/K07, and 2D canvas fallback.
  - Strict console audit: **0 console errors, 0 console warnings, 0 failed network requests**.
  - Detailed report: `design-handoff/milestone-02/verification-report.md`.

## Next task — Milestone 03: Core Expertise Scene

1. Await owner visual review of Milestone 02D before proceeding to Scene 03.
2. Prepare design specification and handoff package for Scene 03 (Core Expertise) extending from the sculpted exit threshold archway of Profile Gallery.
3. As instructed by project scope sequence, do not build Scene 03 geometry until design handoff is approved.

## GitHub publishing rules

After each successfully verified completed unit of work, the implementation agent must commit and push to GitHub automatically without a separate approval prompt, subject to safe Git practices and repository protection. Never assert remote success without confirming the remote SHA. See `AGENTS.md`.
