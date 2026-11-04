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
| 02D — Profile Gallery Visual Fidelity Pass | **Technical delivery complete; owner visual sign-off pending** | Sculpted arch portal, botanical multi-scale trees, 3.5cm ultra-slim silver mullions, polished travertine floor sheen, high-contrast brand typography (#111827), 12 Playwright screenshots, report in verification-report.md | Independent review found remaining fidelity gap vs approved V2 reference; owner visual sign-off pending. Scene 03 design planning may proceed. |
| 03 — Core Expertise Architecture (03A) | **03A asset produced, awaiting visual owner review / 03B not implemented** | `design-handoff/milestone-03/production/` contains `expertise-in-motion.blend`, `expertise-in-motion.glb` (38.66 KB), `generate_expertise_in_motion.py`, proof renders `camera-K08-seam.png`–`K12-bridge.png`, `top-down-layout.png`, `portal-seam-detail.png`, 4 mobile portrait renders, `asset-report-03A.md`, `03A-PREFLIGHT.md` | Stop for owner visual review before Milestone 03B Three.js runtime integration |

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

## Milestone 03 V2 Delivery Summary (2026-11-04) — Visual Experience Redesign (Expertise in Motion)

- **V1 Review Outcome:** Milestone 03 V1 ("Expertise Rotunda") was reviewed and **REJECTED** by the portfolio owner due to visual and compositional monotony (circular room and static left-aligned text repeating Scenes 01 & 02). See `design-handoff/milestone-03/REVIEW-V1-NOT-APPROVED.md`.
- **V2 Core Breakthrough: "Expertise in Motion":**
  - Discarded the circular rotunda entirely. Created an **expansive asymmetrical 36m x 18m daylight pavilion** with a soaring sloped roof ($6.2\text{m} \to 10.5\text{m}$) and 4-bay north sawtooth clerestories.
  - **Three Concrete Physical Spatial Metaphors for Competencies:**
    - **Zone A (Business Analysis / Process Lines):** Inlaid dark basalt stone and silver lines embedded into the travertine floor, physically branching from As-Is into To-Be routes. Framed via an **elevated oblique camera angle** ($Z = 3.20\text{m}$, downward tilt $-22^\circ$).
    - **Zone B (SAP & Enterprise Systems / System Spine):** A monumental 3-tier modular structural matrix ($4 \times 2 \times 3$ bays) of brushed aluminum beams and glowing frosted-glass volumes. Framed via an **eye-level side-tracking shot** with rich multi-plane parallax.
    - **Zone C (Solution Consulting / Suspended Bridge):** A physical suspended pedestrian bridge ($L = 14.0\text{m}$, $W = 3.2\text{m}$, elevated at $Z = 2.40\text{m}$) crossing open air toward the grand Scene 04 portal. Framed via an **elevated bridge glide** ($Z = 4.05\text{m}$ eye level).
- **Adaptive Editorial UI Layouts (Replacing the static left column):**
  - K09: Center-Left Hero layout with 55% open architectural reveal.
  - K10: **Bottom-Left Horizontal Banner** with interactive process milestone tags (`Requirements` $\to$ `As-Is / To-Be` $\to$ `UAT`).
  - K11: **Split-Column Layout** (compact 34% left text, 66% right installation showcase).
  - K12: **Symmetrical Gateway Layout** framing the forward bridge threshold.
- **Mandatory Acceptance Test Verified:**
  - *Viewer can distinguish K10, K11, and K12 visually without reading any headline.*
  - *Viewer instantly recognizes Scene 03 as completely distinct from Scene 01 (circular room) and Scene 02 (curved corridor).*
- **Visual Reference Deliverables (`design-handoff/milestone-03/visual-references/`):**
  - `scene03-v2-master-visual-board.png`: Master creative director board ($1920 \times 1080$).
  - `01-three-concept-candidates.png`: Side-by-side comparison of Candidates A, B, and C.
  - `02-scene02-vs-scene03-comparison.png`: Contact sheet comparing actual Scene 02 screenshots against Scene 03 V2.
  - `03-recommended-concept-hero.png`: Wide hero perspective of "Expertise in Motion".
  - `04-camera-storyboard-k09-k12-v2.png`: 4 visually distinct frames with mathematical poses.
  - `05-ui-varied-compositions-board.png`: 4 varied editorial typography compositions.
  - `06-spatial-route-and-topdown-v2.png`: Technical top-down blueprint and camera trajectory.
  - `07-material-lighting-feasibility-v2.png`: Materials, sawtooth optics, and Three.js runtime budget (~6,800 tris).
  - Archival 3D blend file: `scene03-v2-exploration.blend`.
  - Comprehensive documentation index: `REFERENCE-INDEX-V2.md`.

## Milestone 03A Delivery Summary (2026-11-04) — Blender Production & GLB Export

- **Hard Preflight Passed (`03A-PREFLIGHT.md`):** Audited `src/camera-controller.js` and confirmed runtime FOV truth is **48.0° desktop / 50.0° mobile**. Reconciled anchor coordinates at $(43.24, 0.00, -19.98)$ with zero runtime edits.
- **Master Production 3D Environment:** Created `design-handoff/milestone-03/production/expertise-in-motion.blend` via reproducible automation script `generate_expertise_in_motion.py` in Blender 5.2.3 LTS.
- **Physical Watertight Seam:** Built `EXPM_Portal_EntryVestibule` with 20cm physical overlap along the corridor exit tangent vector, eliminating light leakage and geometry gaps.
- **Physical Spatial Metaphors for Competencies:**
  - **Zone 1 (Business Analysis):** Inlaid dark basalt paths and brushed silver rails branching across light travertine floor (As-Is to To-Be). Framed in K10 elevated oblique view ($Z=3.20\text{m}$, pitch $-22^\circ$).
  - **Zone 2 (SAP & Enterprise Systems):** 4x2x3 bay modular structural matrix of brushed aluminum beams and 10 nested frosted glass functional volumes. Framed in K11 side-tracking parallax view ($Z=1.85\text{m}$).
  - **Zone 3 (Solution Consulting):** 14m suspended pedestrian bridge deck ($Z=2.40\text{m}$) crossing open space with low-iron glass balustrades toward the Scene 04 portal. Framed in K12 elevated bridge glide ($Z=4.05\text{m}$).
- **GLB Export & Validation:**
  - Exported `design-handoff/milestone-03/production/expertise-in-motion.glb`.
  - File size: **38.66 KB** (well within $\le 1,200\text{ KB}$ budget).
  - Geometry: **12 meshes**, **756 polygons**, **1,054 vertices** (target: $\le 6,800$ triangles).
  - Hierarchy: 100% prefixed with `EXPM_`.
  - PBR Materials: 6 valid materials (warm white plaster, travertine stone, clear glass, frosted glass, brushed aluminum, dark basalt).
  - Cleanliness: **0 cameras, 0 lights, 0 baked text/card UI**.
  - Re-import script verified scale, normals, bounds, and watertightness.
- **Camera Clearance:** Verified zero collision across interpolated trajectory $K08 \to K12$.
- **Render Proof:** Generated 11 full-resolution render artifacts in `design-handoff/milestone-03/production/renders/` (K08 seam, K09 reveal, K10 process paths, K11 system spine, K12 bridge, top-down layout, portal seam detail, and mobile portrait compositions K09–K12).
- **Scope Boundary:** Milestone 03A only. No runtime Three.js code, camera controller, HTML, or CSS touched. Stop for owner visual review.

## Next task — Milestone 03B: Core Expertise Three.js Integration & UI (Pending Owner 03A Visual Sign-off)

1. Await portfolio owner review and visual approval of Milestone 03A production renders and asset report.
2. Upon approval, proceed to Milestone 03B:
   - Load `expertise-in-motion.glb` into `src/world.js` and configure glass material properties.
   - Extend `src/camera-controller.js` with waypoints K09–K12 using verified coordinates.
   - Implement unboxed editorial HTML/CSS overlays for Business Analysis, SAP/ERP, and Solution Consulting.
   - Update scroll schedule (32%–52%) and right-side chapter navigation dot for `03 Expertise`.
   - Validate desktop/mobile responsive rendering and forward/reverse scroll performance.
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

## Independent Milestone 03 V2 review — 2026-11-04

- Concept Candidate A / Expertise in Motion is a meaningful architectural and camera-composition departure from Scene 01/02 **on paper**; actual V2 PNG pixels could not be independently decoded by GitHub connector in this review.
- The existing `src/camera-controller.js` K08 FOV is **48° desktop / 50° mobile**, while V2 ledger lists **46° desktop / 48° mobile**. Must reconcile before 03A/03B; do not change accepted K08 framing to force a match.
- A small outgoing chord angle does not prove C1 velocity continuity. Test actual position/look/FOV derivatives and preserve K01–K08 chapter-specific shots with the new spline.
- See `design-handoff/milestone-03/REVIEW-V2-INDEPENDENT.md` for full review and next-step checks.
- **Status remains pending owner visual approval.** Do not code Scene 03 until approved. Once approved, incremental Blender 03A then Three.js 03B, auto push verified work per `AGENTS.md`.

## Candidate A V2 owner approval — 2026-11-04

- Owner **Hoàng Nguyễn Thành Tâm** explicitly approved **Candidate A — Expertise in Motion / Asymmetric Sawtooth Pavilion** for Milestone 03A production.
- **03A authorized**: create Blender source `.blend`, export validated GLB, actual K08–K12 renders and seam/collision reports. Then auto commit/push following `AGENTS.md`.
- **03B not yet authorized**: do not modify Three.js runtime, UI, camera controller, navigation, or build Scene 04 before 03A visual review.
- **FOV bug corrected in V2 Camera Ledger**: K08 must preserve live **48° desktop / 50° mobile**. Source `src/camera-controller.js` remains unchanged. See `design-handoff/milestone-03/03-CAMERA-LEDGER-V2.md`.
- **Antigravity execution prompt:** `design-handoff/milestone-03/ANTIGRAVITY-MILESTONE-03A-BLENDER-PRODUCTION.md` contains preflight hard gate, exact reference PNG list, geometry/materials, render proof, GLB re-import and auto-push verification.
- Existing 02D visual polish still lacks final owner sign-off; do not silently redefine previous scene's look. Art polish remains on shared follow-up backlog.
