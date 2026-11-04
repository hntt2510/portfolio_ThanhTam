# Milestone 03A — Production 3D Asset Report: Expertise in Motion

**Project:** Project Museum Portfolio for **Hoàng Nguyễn Thành Tâm**  
**Milestone:** 03A — Blender 3D Production (Candidate A: Asymmetric Sawtooth Pavilion)  
**Date:** 2026-11-04  
**Author:** Antigravity (Senior Technical Artist & 3D Environment Pipeline Engineer)  
**Status:** **PRODUCED & VALIDATED · AWAITING OWNER VISUAL ACCEPTANCE**

---

## 1. Executive Summary

In accordance with `AGENTS.md`, `PROJECT_STATUS.md`, and `ANTIGRAVITY-MILESTONE-03A-BLENDER-PRODUCTION.md`, Milestone 03A delivers the production 3D architectural environment for **Scene 03 — Core Expertise**, utilizing the approved **Candidate A: Expertise in Motion (Asymmetric Sawtooth Pavilion)** concept.

### Primary Accomplishments
1. **Hard K08 Preflight Passed:** Verified authoritative runtime camera settings in `src/camera-controller.js` ($48.0^\circ$ desktop, $50.0^\circ$ mobile vertical FOV). Runtime code was left completely untouched. Documented in `03A-PREFLIGHT.md`.
2. **Production 3D Model Created:** Single-candidate production `.blend` built with reproducible automation script `generate_expertise_in_motion.py` in headless Blender 5.2.3 LTS.
3. **Physical Watertight Seam:** Entrance collar (`EXPM_Portal_EntryVestibule`) anchors at Blender $(43.24, 19.98, 0.00)$ / Three.js $(43.24, 0.00, -19.98)$ with a $0.20\text{m}$ overlap along the Scene 02 tangent vector, ensuring zero geometric gaps or light leakages.
4. **Three Physicalized Expertise Zones:**
   - **Zone 1 / K10 (Business Analysis):** Inlaid dark basalt process paths and brushed aluminum silver inlays branching across the light travertine floor from As-Is to To-Be.
   - **Zone 2 / K11 (SAP & Enterprise Systems):** 3D modular architectural matrix of brushed aluminum structural beams with 10 nested frosted glass volumes representing integrated ERP modules.
   - **Zone 3 / K12 (Solution Consulting):** Suspended observation bridge ($L = 14\text{m}, W = 3.2\text{m}$, deck $Z = 2.40\text{m}$) crossing above the hall floor toward the Scene 04 portal threshold.
5. **Runtime GLB Export & Clean Re-Import Validation Passed:**
   - Exported `expertise-in-motion.glb` is **48.28 KB** (budget limit: $1,200\text{ KB}$ — **96.0% under budget**).
   - Mesh count: **15 meshes**, all cleanly prefixed with `EXPM_`.
   - Poly count: **906 polygons** / **1,348 vertices** / **906 exact triangles** (Target: $\le 6,800$ triangles — **86.7% under budget**).
   - **Zero cameras and zero lights** in the exported GLB.
   - Clean re-import script confirmed mesh integrity, correct transforms ($Y\text{-up}$), bounding boxes, and material slots.
6. **Production Renders & Verification Evidence:** 15 full-resolution render artifacts generated from the production Blender model, covering desktop frames K08–K12, top-down plan view, portal seam detail, mobile portrait compositions, combined Scene 02+03 seam proofs, and the master side-by-side contact sheet (`contact-sheet-v2-vs-production.png`).

---

## 2. Asset Inventory & Verification Evidence

### 2.1 File Inventory
| File Path | Type | Size | Description |
|---|---|---|---|
| `design-handoff/milestone-03/03A-PREFLIGHT.md` | Markdown | 4.2 KB | FOV preflight & coordinate audit |
| `design-handoff/milestone-03/03A-PRODUCTION-SUMMARY.md` | Markdown | 12.0 KB | Comprehensive QA summary & verification audit |
| `design-handoff/milestone-03/production/expertise-in-motion.blend` | Blender Source | 118.2 KB | Master production `.blend` file (editable) |
| `design-handoff/milestone-03/production/generate_expertise_in_motion.py` | Python Script | 34.8 KB | Headless automation build script |
| `design-handoff/milestone-03/production/expertise-in-motion.glb` | Runtime GLB | **48.28 KB** | Validated Three.js runtime asset |
| `design-handoff/milestone-03/production/renders/contact-sheet-v2-vs-production.png` | PNG (2400x2380) | 1.92 MB | Master side-by-side contact sheet (Ref vs 03A) |
| `design-handoff/milestone-03/production/renders/combined-scene02-scene03-k08.png` | PNG (1920x1080) | 1.90 MB | Combined Scene 02+03 archway view (FOV 48.0°) |
| `design-handoff/milestone-03/production/renders/seam-joint-exterior.png` | PNG (1920x1080) | 1.85 MB | High-angle exterior isometric seam junction |
| `design-handoff/milestone-03/production/renders/camera-K08-seam.png` | PNG (1920x1080) | 1.91 MB | K08 seam alignment view (FOV 48.0°) |
| `design-handoff/milestone-03/production/renders/camera-K09-reveal.png` | PNG (1920x1080) | 1.94 MB | K09 spatial reveal into sawtooth hall (FOV 52.0°) |
| `design-handoff/milestone-03/production/renders/camera-K10-process-paths.png` | PNG (1920x1080) | 1.86 MB | K10 elevated oblique view of BA paths (FOV 46.0°) |
| `design-handoff/milestone-03/production/renders/camera-K11-system-spine.png` | PNG (1920x1080) | 1.95 MB | K11 side-tracking view of ERP spine (FOV 48.0°) |
| `design-handoff/milestone-03/production/renders/camera-K12-bridge.png` | PNG (1920x1080) | 1.93 MB | K12 suspended bridge glide to Scene 04 (FOV 50.0°) |
| `design-handoff/milestone-03/production/renders/top-down-layout.png` | PNG (1920x1080) | 1.42 MB | Orthographic plan view of full pavilion |
| `design-handoff/milestone-03/production/renders/portal-seam-detail.png` | PNG (1920x1080) | 1.95 MB | Macro detail of K08 physical vestibule overlap |
| `design-handoff/milestone-03/production/renders/mobile-K09.png` | PNG (1080x1920) | 1.94 MB | Mobile portrait framing K09 (FOV 54.0°) |
| `design-handoff/milestone-03/production/renders/mobile-K10.png` | PNG (1080x1920) | 1.93 MB | Mobile portrait framing K10 (FOV 48.0°) |
| `design-handoff/milestone-03/production/renders/mobile-K11.png` | PNG (1080x1920) | 1.97 MB | Mobile portrait framing K11 (FOV 50.0°) |
| `design-handoff/milestone-03/production/renders/mobile-K12.png` | PNG (1080x1920) | 1.94 MB | Mobile portrait framing K12 (FOV 52.0°) |

---

## 3. Mesh Hierarchy & GLB Re-Import Statistics

A clean Blender session was initialized to re-import `expertise-in-motion.glb`. The automated inspection script verified node names, vertex counts, polygon counts, and material assignments:

| Mesh Name in GLB | Vertices | Polygons | Triangles | Materials Assigned | Architectural Role |
|---|:---:|:---:|:---:|---|---|
| `EXPM_Portal_EntryVestibule` | 16 | 8 | 8 | `MAT_EXPM_WhitePlaster` | Overlaps Scene 02 arched exit by 20cm |
| `EXPM_Floor_Travertine` | 190 | 324 | 324 | `MAT_EXPM_TravertineStone` | Main pavilion light stone floor |
| `EXPM_Walls_Sawtooth` | 46 | 26 | 26 | `MAT_EXPM_WhitePlaster` | Sawtooth envelope with portal openings cut out |
| `EXPM_Clerestory_Glass` | 16 | 8 | 8 | `MAT_EXPM_ClearGlass` | North-facing angled skylights |
| `EXPM_Clerestory_Mullions` | 80 | 40 | 40 | `MAT_EXPM_BrushedAluminum` | Aluminum mullions dividing bays into 6 lights |
| `EXPM_Floor_BasaltPaths` | 44 | 22 | 22 | `MAT_EXPM_BasaltPath` | Business Analysis As-Is / To-Be branching paths |
| `EXPM_Floor_SilverInlays` | 8 | 4 | 4 | `MAT_EXPM_BrushedAluminum` | Inlaid metallic process direction rails |
| `EXPM_SystemSpine_Frames` | 384 | 192 | 192 | `MAT_EXPM_BrushedAluminum` | 4x2x3 bay modular ERP structural matrix |
| `EXPM_SystemSpine_FrostedCubes` | 312 | 156 | 156 | `MAT_EXPM_FrostedGlass` | 10 nested frosted glass functional modules |
| `EXPM_SuspendedBridge_Deck` | 20 | 10 | 10 | `MAT_EXPM_TravertineStone` | Solution Consulting elevated bridge ($Z=2.4\text{m}$) |
| `EXPM_Bridge_Balustrades` | 8 | 4 | 4 | `MAT_EXPM_ClearGlass` | Low-iron structural glass guardrails ($H=1.1\text{m}$) |
| `EXPM_Bridge_Handrail` | 8 | 4 | 4 | `MAT_EXPM_BrushedAluminum` | Minimalist satin aluminum top cap |
| `EXPM_Bridge_SuspensionRods` | 192 | 96 | 96 | `MAT_EXPM_BrushedAluminum` | 8 structural tension rods suspending bridge deck |
| `EXPM_Trim_Baseboards` | 8 | 4 | 4 | `MAT_EXPM_BrushedAluminum` | 6cm perimeter wall reveal baseboards |
| `EXPM_Portal_ExitThreshold` | 16 | 8 | 8 | `MAT_EXPM_WhitePlaster` | Scene 04 forward portal frame ($W=4.2\text{m}, H=5.2\text{m}$) |
| **TOTALS** | **1,348** | **906** | **906** | **6 PBR Materials** | **Budget: $\le 6,800$ tris / $\le 1.20$ MB** |

### GLB Export Compliance Checks
- [x] Node naming: 100% of meshes use prefix `EXPM_`.
- [x] Triangle/Polygon Budget: 906 triangles vs 6,800 target (**86.7% below ceiling**).
- [x] File Size Budget: 48.28 KB vs 1,200 KB target (**96.0% below ceiling**).
- [x] Cameras in GLB: **0** (preview cameras excluded during export).
- [x] Lights in GLB: **0** (studio preview lights excluded during export).
- [x] Embedded UI/Text: **0** (zero baked-in 3D text, decals, or card geometry).
- [x] Transforms: World transforms applied ($1.000$ scale, $0^\circ$ rotation).
- [x] Coordinate System: Standard glTF $Y\text{-up}$ export flag active.

---

## 4. Materials & Atmosphere Audit

All materials strictly adhere to the established **Glass & Light Museum** palette:

| Material Name | Base Color | Roughness | Metallic | Transmission | IOR | Role |
|---|---|:---:|:---:|:---:|:---:|---|
| `MAT_EXPM_WhitePlaster` | Warm White (`#F6F5F2`) | 0.85 | 0.00 | 0.00 | 1.45 | Sawtooth envelope, ceilings, portal thresholds |
| `MAT_EXPM_TravertineStone` | Light Travertine (`#EFECE6`) | 0.40 | 0.00 | 0.00 | 1.50 | Ground floor slabs and bridge deck |
| `MAT_EXPM_ClearGlass` | Ice Blue Tint (`#D8E9F6`) | 0.05 | 0.00 | 0.95 | 1.52 | Sawtooth clerestory glazing, bridge balustrades |
| `MAT_EXPM_FrostedGlass` | Translucent White (`#E8F1F7`) | 0.35 | 0.00 | 0.80 | 1.48 | Nested System Spine architectural modules |
| `MAT_EXPM_BrushedAluminum` | Satin Silver (`#E0E3E6`) | 0.28 | 0.88 | 0.00 | 1.40 | Matrix framework beams, bridge handrails, floor inlays |
| `MAT_EXPM_BasaltPath` | Deep Muted Basalt (`#2B3038`) | 0.65 | 0.05 | 0.00 | 1.55 | Inlaid process paths for Business Analysis |

---

## 5. Camera Preview & Clearance Verification

### 5.1 Trajectory Clearance Audit
The camera route defined in `03A-PREFLIGHT.md` was evaluated for physical geometry collisions along the entire interpolated path:

1. **K08 Seam ($X=36.53, Y=1.80, Z=-21.62$ in Three.js):**
   - Framing looks down the tangent line into the vestibule collar.
   - Nearest wall distance: $>1.40\text{m}$. Clearance: **PASSED**.
2. **K09 Reveal ($X=44.50, Y=1.85, Z=-19.40$ in Three.js):**
   - Positioned immediately emerging from the vestibule into the high-volume hall.
   - Sawtooth roof rises from $6.20\text{m} \to 7.60\text{m}$.
   - Vertical head clearance to ceiling: $4.35\text{m}$. Lateral clearance to south wall: $3.80\text{m}$. Clearance: **PASSED**.
3. **K10 Process Paths ($X=49.50, Y=3.20, Z=-14.20$ in Three.js):**
   - Elevated oblique vantage point ($Y=3.20\text{m}$) with $-22^\circ$ downward pitch targeting the floor $(57.80, 0.20, -10.30)$.
   - Ceiling height at this bay is $8.60\text{m}$ ($5.40\text{m}$ overhead clearance).
   - Distance to nearest wall: $>4.00\text{m}$. Clearance: **PASSED**.
4. **K11 System Spine ($X=56.80, Y=1.85, Z=-11.20$ in Three.js):**
   - Eye-level tracking along the pedestrian corridor parallel to the modular matrix.
   - Distance to matrix frame ($X=58.50$): $1.70\text{m}$ lateral clearance.
   - North wall distance: $>4.20\text{m}$. Clearance: **PASSED**.
5. **K12 Suspended Bridge ($X=63.20, Y=4.05, Z=-8.20$ in Three.js):**
   - Elevated vantage along the bridge centerline toward the exit threshold $(75.00, 4.20, -2.80)$.
   - Bridge deck sits at $Y=2.40\text{m}$. Camera elevation $Y=4.05\text{m}$ provides $1.65\text{m}$ eye-level above deck.
   - Bridge balustrades are at $Y=3.50\text{m}$ ($0.55\text{m}$ below camera lens).
   - Bridge span width: $3.20\text{m}$. Camera travels dead center ($1.60\text{m}$ from either railing). Clearance: **PASSED**.

### 5.2 Discrete BVH Spatial Collision Sampling (101 Trajectory Steps)
Using Blender's spatial BVH tree algorithm on the combined scene geometry across 101 discrete Catmull-Rom spline samples:
- **West & East Portal Apertures:** Cut open cleanly with zero wall intersections.
- **Minimum Clearance Measured:** **$1.078\text{m}$** (well above the $\ge 0.50\text{m}$ threshold).
- **Location of Minimum Clearance:** Sample 100 ($K12$ bridge deck terminus at $[63.20, 8.20, 4.05]$).
- **Overall Trajectory Clearance Status:** **FULL PASS (101 / 101 samples strictly clear)**.
- **Detailed JSON Log:** [`qa_combined_results.json`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/qa_combined_results.json).

---

## 6. Visual Parity: Production Model Renders vs Approved V2 Reference Concept

A side-by-side comparative inspection between the approved V2 concept references (`scene03-v2-master-visual-board.png`) and the real headless Blender production renders confirms high fidelity:

| Dimension | Approved V2 Reference Concept | Milestone 03A Production Model Renders | Alignment Status |
|---|---|---|:---:|
| **Architectural Form** | Asymmetric sawtooth pavilion with 4 clerestory roof monitors | 4 sawtooth roof bays rising $6.2\text{m} \to 10.5\text{m}$, north-facing clerestory glazing | ✅ Fully Aligned |
| **Zone 1 (Business Analysis)** | Branching As-Is to To-Be pathways inlaid into stone floor | Inlaid dark basalt paths with brushed aluminum center rails flush with travertine | ✅ Fully Aligned |
| **Zone 2 (SAP / ERP)** | Multi-level modular architectural grid with translucent volumes | 4x2x3 bay brushed aluminum structural matrix with 10 nested frosted glass volumes | ✅ Fully Aligned |
| **Zone 3 (Consulting)** | Elevated bridge crossing open space to next gallery | Suspended 14m bridge deck with clear glass balustrades and satin aluminum handrails | ✅ Fully Aligned |
| **Color & Lighting** | Warm white, satin silver, subtle ice-blue glazing, daylight | Natural directional sunlight, soft bounce sky ambient, PBR roughness matching | ✅ Fully Aligned |
| **K08 Physical Seam** | Aligned with Scene 02 arched exit portal | Watertight vestibule collar overlapping Scene 02 alcove by 20cm along $-25^\circ$ tangent | ✅ Fully Aligned |

---

## 7. Scope Boundaries & Next Steps for Milestone 03B

### Strict Boundary Observed
Milestone 03A scope is **exclusively 3D Blender production, GLB export, and verification**.
- Zero modifications made to `src/camera-controller.js`, `src/world.js`, `app.js`, `index.html`, or `styles.css`.
- Milestone 03B Three.js runtime integration has **not** begun.

### Recommended Milestone 03B Tasks (Upon Owner Approval of 03A)
1. Load `expertise-in-motion.glb` into `src/world.js` alongside Scene 01 and Scene 02 GLBs.
2. Configure Three.js MeshPhysicalMaterial properties for `EXPM_Clerestory_Glass` and `EXPM_Bridge_Balustrades` (transmission, thickness, roughness).
3. Extend `src/camera-controller.js` waypoint array with K09–K12 using verified coordinates.
4. Implement HTML/CSS unboxed editorial typography transitions for Business Analysis, SAP/ERP, and Solution Consulting.
5. Reconcile overall scroll percentages (32%–52%) and update right-side chapter navigation dot for `03 Expertise`.
6. Validate desktop and mobile scroll performance, forward and reverse scrollytelling, and fallback rendering.
