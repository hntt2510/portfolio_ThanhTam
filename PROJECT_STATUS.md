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
| 02D — Profile Gallery Visual Fidelity Pass | **Technical delivery complete; owner visual sign-off pending** | Sculpted arch portal, botanical multi-scale trees, 3.5cm ultra-slim silver mullions, polished travertine floor sheen, high-contrast brand typography (#111827), 12 Playwright screenshots, report in erification-report.md | Independent review found remaining fidelity gap vs approved V2 reference; owner visual sign-off pending. Scene 03 design planning may proceed. |
| 03 — Core Expertise Design & Visual Planning | **V1 reviewed and rejected; V2 redesign pending** | design-handoff/milestone-03/ complete design handoff: 6 specification documents, 3D blend model, 10 high-resolution visual boards & keyframes in isual-references/, verified acceptance matrix | Owner feedback: too similar to Scene 01/02; revise architecture, choreography and UI composition before any 03A/03B implementation |

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

## Milestone 03 Delivery Summary (2026-11-04) — Core Expertise Design & Visual Planning

- **Design Scope Boundary (Design Only):** Full creative direction, visual specifications, architectural blueprints, camera trajectory, copywriting, and 3D asset implementation plan completed without modifying runtime website code.
- **Architectural Concept: The Expertise Rotunda:**
  - A bright, expansive circular hall ($R = 12.0\text{m}$, diameter $24.0\text{m}$, perimeter height $6.8\text{m}$, dome peak $8.2\text{m}$) connected directly to the Scene 02 K08 arched portal at $(43.24, 0.00, -19.98)$ without spatial or orientation discontinuity.
  - Three distinct architectural zones articulated along the perimeter:
    - **Zone A:** Business Analysis Alcove (recessed curved wall niche, soft diffused cove wash).
    - **Zone B:** SAP & Enterprise Systems Colonnade (18 vertical brushed-aluminum fins $4\text{cm} \times 12\text{cm}$ with high clerestory glass apertures).
    - **Zone C:** Solution Consulting & Exit Threshold (grand sculpted arched portal $W = 4.0\text{m}$, $H = 5.0\text{m}$ leading into future Scene 04 Project Exhibition).
  - Soaring central oculus skylight ($R = 4.0\text{m}$) admitting pure natural zenith daylight onto polished travertine floor paving with radial brushed-aluminum inlay joints.
- **Camera Spline Trajectory (K08 → K12):**
  - Fully reconciled desktop ($46^\circ$–$48^\circ$ FOV) and mobile ($48^\circ$–$50^\circ$ FOV) camera ledger.
  - Verified $C_0$ positional continuity and $C_1$ tangent velocity continuity across the K08 transition seam ($\Delta \theta = 5.2^\circ$).
  - Narrative beats: K09 Entrance ($p = 0.00 \to 0.22$), K10 Business Analysis ($p = 0.22 \to 0.48$), K11 SAP/Enterprise ($p = 0.48 \to 0.74$), K12 Solution Consulting ($p = 0.74 \to 1.00$).
- **Editorial DOM Overlay & Anti-Patterns:**
  - 100% of narrative copy, competencies, and metadata remain in the unboxed HTML/CSS DOM overlay.
  - Strictly **zero 3D text panels, zero glass cards on meshes, and zero floating skill labels**.
  - Grounded, authentic copywriting tailored specifically for **Hoàng Nguyễn Thành Tâm**.
  - Fixed vertical navigation dynamically highlights `03 Expertise`.
- **Visual Reference Package Deliverables (`design-handoff/milestone-03/visual-references/`):**
  - `scene03-visual-board-master.png`: Comprehensive master creative director board ($1920 \times 1080$).
  - `01-scene03-hero-visual.png`: Wide establishing perspective of the Expertise Rotunda.
  - `02-architecture-and-spatial-layout.png`: Orthographic architectural blueprint with coordinates, dimensions, and camera trajectory.
  - `03-ui-composition-board.png`: Unboxed editorial typography overlay validation.
  - `04-camera-storyboard-k09-k12.png`: 4-keyframe scrollytelling storyboard with mathematical camera poses.
  - `05-material-and-lighting-board.png`: PBR material swatches, daylight strategy, and WCAG AAA contrast matrix.
  - Individual keyframes `keyframe-K09-visual-reference.png` through `keyframe-K12-visual-reference.png`.
  - Archival 3D blend file: `expertise-rotunda-design.blend`.
  - Complete documentation index & licensing: `REFERENCE-INDEX.md`.

## Next task — Milestone 03A: Core Expertise Blender Architecture

1. Await portfolio owner review and visual approval of Milestone 03 design handoff package.
2. Upon approval, proceed to Milestone 03A:
   - Procedural Blender generation script `generate_expertise_rotunda.py`.
   - Export production `expertise-rotunda.glb` ($\le 1.50\text{ MB}$, target $\approx 9,400$ triangles).
   - Headless proof renders from Blender.
3. Automatically commit and push per `AGENTS.md`.

## GitHub publishing rules

After each successfully verified completed unit of work, the implementation agent must commit and push to GitHub automatically without a separate approval prompt, subject to safe Git practices and repository protection. Never assert remote success without confirming the remote SHA. See `AGENTS.md`.

## Independent visual QA — 2026-11-04

- Reviewed commit `e8ba349` screens (desktop K05, K07, K08; mobile K05) against approved Scene 02 corridor reference.
- **Improved:** unboxed text, name contrast, K08 portal, richer vegetation meshes.
- **Still open:** low-poly canopy shape, flat overbright architectural materials, mullions overlapping text at K07/K08, limited photoreal museum quality.
- Technical delivery completed; **not yet signed off for final visual fidelity**. See `design-handoff/milestone-02/REVIEW-02D-INDEPENDENT.md`.
- Recommendation: plan Scene 03 art direction while tracking an optimized cross-scene quality pass rather than indefinite procedural graybox iteration. Scene 03 implementation requires its own approved design.

## Scene 03 visual design feedback — 2026-11-04

- **Owner rejected V1 visual direction** because the interface and environmental experience look too similar to Scenes 01/02. The V1 design package at `eefc3a4` is not approved for code.
- See `design-handoff/milestone-03/REVIEW-V1-NOT-APPROVED.md` for the redesign brief. Require multiple distinct architectural concepts, keyframe images, and side-by-side comparison against current Scene 02 screenshot.
- New target: distinct spatial storytelling per competency, while skill information remains direct, readable HTML UI synchronized with reversible scroll. Preserve continuous K08 entry and fixed side navigation.
- **Do not code Milestone 03A/03B** until V2 design with images has been explicitly approved. Continue automatic commit/push of design artifacts as usual.
