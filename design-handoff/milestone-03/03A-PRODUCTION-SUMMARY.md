# Milestone 03A — Production Summary & Final QA Report

**Project:** Project Museum Portfolio for **Hoàng Nguyễn Thành Tâm**  
**Milestone:** 03A — Blender 3D Production (Candidate A: Expertise in Motion / Asymmetric Sawtooth Pavilion)  
**Date:** 2026-11-04  
**Audit Status:** **TECHNICAL & GEOMETRIC QA PASSED · VISUAL CONTACT SHEET COMMITTED · AWAITING OWNER VISUAL ACCEPTANCE**

---

## 1. Executive Summary & Verification State

This document addresses all findings from [`REVIEW-03A-INDEPENDENT.md`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/REVIEW-03A-INDEPENDENT.md) and completes the rigorous final geometry and visual verification of the Milestone 03A production asset.

### Key Verification Metrics
| Parameter | Measured Production Value | Target / Budget | Status |
|---|:---:|:---:|:---:|
| **GLB File Size** | **48.28 KB** (49,440 bytes) | $\le 1,200\text{ KB}$ | ✅ **96.0% under budget** |
| **Exact Triangle Count** | **906 Triangles** | $\le 6,800\text{ Triangles}$ | ✅ **86.7% under budget** |
| **Mesh Count** | **15 Meshes** (all `EXPM_` prefix) | $\ge 8\text{ Meshes}$ | ✅ Validated |
| **PBR Materials** | **6 Materials** (glTF-compliant) | Standard PBR | ✅ Validated |
| **Preview Cameras in GLB** | **0** | 0 | ✅ Clean |
| **Preview Lights in GLB** | **0** | 0 | ✅ Clean |
| **Embedded 3D Text / UI** | **0** | 0 | ✅ Clean |
| **Minimum Camera Clearance** | **1.078 m** (101 samples tested) | $\ge 0.50\text{ m}$ | ✅ **FULL PASS** |
| **Floor Elevation Delta at Seam** | **0.000 m** (Flush Travertine) | $< 0.01\text{ m}$ | ✅ **WATERTIGHT** |
| **Physical Seam Overlap** | **0.20 m** along $-25^\circ$ tangent | $\ge 0.15\text{ m}$ | ✅ **WATERTIGHT** |

---

## 2. Side-by-Side Visual Comparison (Approved V2 vs Actual Production Renders)

A dedicated full-scale contact sheet has been generated directly from the newly produced Blender model renders and the approved V2 concept references:
👉 **[`design-handoff/milestone-03/production/renders/contact-sheet-v2-vs-production.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/renders/contact-sheet-v2-vs-production.png)**

| Narrative Beat | Approved V2 Reference | Actual 03A Production Model Render | Mean Absolute Pixel Difference | Visual Alignment Assessment |
|---|---|---|:---:|---|
| **K09 — Volumetric Reveal** | `keyframe-K09-v2-reveal.png` | `camera-K09-reveal.png` | **3.8 / 255** | **Fully Aligned:** Soaring 4-monitor sawtooth roof, north daylight wash, vestibule arch threshold opening. |
| **K10 — Business Analysis Paths** | `keyframe-K10-v2-process-paths.png` | `camera-K10-process-paths.png` | **1.9 / 255** | **Fully Aligned:** Inlaid dark basalt paths and silver center rails visibly branching As-Is to To-Be across travertine floor. |
| **K11 — SAP / ERP Modular Spine** | `keyframe-K11-v2-system-spine.png` | `camera-K11-system-spine.png` | **1.9 / 255** | **Fully Aligned:** 4x2x3 bay modular aluminum structural matrix with 10 nested frosted glass volumes. |
| **K12 — Consulting Suspended Bridge** | `keyframe-K12-v2-bridge-portal.png` | `camera-K12-bridge.png` | **1.3 / 255** | **Fully Aligned:** 14m elevated bridge deck with low-iron glass balustrades and forward Scene 04 portal threshold. |

---

## 3. Combined Scene 02 + Scene 03 Physical Seam Verification

Both `profile-gallery.glb` (Scene 02) and `expertise-in-motion.glb` (Scene 03) were imported into a unified Blender inspection scene ([`design-handoff/milestone-03/qa_combined_verification.py`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/qa_combined_verification.py)).

### 3.1 Quantitative Seam Geometry Analysis
- **Junction Anchor:** Three.js $(43.24, 0.00, -19.98)$ / Blender $(43.24, 19.98, 0.00)$.
- **Floor Alignment:**
  - Scene 02 floor travertine top surface: $Z = 0.000\text{m}$.
  - Scene 03 floor travertine top surface: $Z = 0.000\text{m}$.
  - Measured vertical offset: **$0.000\text{m}$** (zero vertical step, 100% coplanar).
- **Aperture & Collar Overlap:**
  - Scene 02 arched bulkhead (`PRG_Portal_ArchedWall`): Arch span $W = 3.60\text{m}$, spring height $H_{\text{spring}} = 3.00\text{m}$, crown height $H_{\text{crown}} = 4.50\text{m}$, thickness $0.45\text{m}$.
  - Scene 03 entry collar (`EXPM_Portal_EntryVestibule`): Width $3.60\text{m}$, height $4.50\text{m}$, overlapping Scene 02 by $0.20\text{m}$ along the corridor exit tangent vector $(\cos(-25^\circ), \sin(-25^\circ), 0)$.
  - Overlap bounding box: $X\text{-overlap} = 1.838\text{m}$, $Y\text{-overlap} = 0.857\text{m}$, $Z\text{-overlap} = 4.500\text{m}$.
  - **Result: Watertight mechanical overlap. Zero floating gaps or light leaks.**

### 3.2 Runtime Integration Finding: Temporary Backdrop Culling
The combined geometric audit revealed that in Milestone 02D, a temporary backdrop wall (`PRG_Vestibule_BackdropWall`) and bench (`PRG_Portal_AlcoveBench`) were added at $u = 4.20\text{m}$ past the archway to prevent Scene 02 from looking into an empty void.
- **Action for Milestone 03B:** When Scene 03 is loaded, `world.js` / `src/scenes/profile-gallery.js` must set `PRG_Vestibule_BackdropWall.visible = false` and `PRG_Portal_AlcoveBench.visible = false`. This opens up the unbroken daylight vista from Scene 02 straight through the archway into Scene 03's sawtooth pavilion.
- Verification render showing the open archway transition:
  👉 [`design-handoff/milestone-03/production/renders/combined-scene02-scene03-k08.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/renders/combined-scene02-scene03-k08.png)
  👉 [`design-handoff/milestone-03/production/renders/seam-joint-exterior.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/renders/seam-joint-exterior.png)

---

## 4. Camera Trajectory Spline & BVH Clearance Check

To verify collision-free passage, a continuous Catmull-Rom spline trajectory was sampled at **101 discrete points** ($s \in [0, 100]$) from K08 to K12. A spatial BVH tree was constructed from all 5,904 triangles of the combined scene.

### 4.1 Defect Identified and Fixed in 03A Model
During initial BVH sampling, a defect was identified in `EXPM_Walls_Sawtooth`: the West connection wall had been modeled as a solid quad across the entrance, creating a $0.154\text{m}$ near-clip collision at sample 20.
- **Fix Applied:** Cut out the entrance portal aperture ($W=3.60\text{m}, H=4.50\text{m}$) in the West Wall, and cut out the forward exit portal aperture ($W=4.20\text{m}, H=5.20\text{m}$) in the East Wall.
- **Re-Verification Result:** After cutting the apertures, the minimum clearance jumped from $0.154\text{m}$ to **$1.078\text{m}$**!

### 4.2 Clearance Ledger Summary
- **Total Points Sampled:** 101 intermediate camera poses.
- **Minimum Clearance Across Entire Path:** **$1.078\text{m}$** (well above the $0.50\text{m}$ comfort threshold).
- **Location of Minimum Clearance:** Sample 100 ($K12$ bridge terminus at $[63.20, 8.20, 4.05]$, where the camera sits $1.078\text{m}$ laterally from the bridge glass guardrail).
- **Clearance Status:** **FULL PASS** (101 / 101 samples strictly clear).

---

## 5. Architectural Detail & Triangulated Mesh Inventory

The 03A production model was enriched with museum-grade architectural details to prevent an overly simplified graybox appearance:
1. **Clerestory Aluminum Mullions (`EXPM_Clerestory_Mullions`):** 5 vertical mullions and transoms dividing each clerestory monitor into 6 glazed panels.
2. **Bridge Suspension Tension Rods (`EXPM_Bridge_SuspensionRods`):** 8 vertical tension rods suspending the bridge deck from the ceiling beams.
3. **Perimeter Reveal Baseboards (`EXPM_Trim_Baseboards`):** Recessed 6cm brushed aluminum baseboard reveals along South and North walls.

### Exact Mesh Inventory (`expertise-in-motion.glb`)
| Mesh Name | Vertices | Polygons | Triangles | Assigned Material |
|---|:---:|:---:|:---:|---|
| `EXPM_Portal_EntryVestibule` | 16 | 8 | 8 | `MAT_EXPM_WhitePlaster` |
| `EXPM_Floor_Travertine` | 190 | 324 | 324 | `MAT_EXPM_TravertineStone` |
| `EXPM_Floor_BasaltPaths` | 44 | 22 | 22 | `MAT_EXPM_BasaltPath` |
| `EXPM_Floor_SilverInlays` | 8 | 4 | 4 | `MAT_EXPM_BrushedAluminum` |
| `EXPM_Walls_Sawtooth` | 46 | 26 | 26 | `MAT_EXPM_WhitePlaster` |
| `EXPM_Clerestory_Glass` | 16 | 8 | 8 | `MAT_EXPM_ClearGlass` |
| `EXPM_Clerestory_Mullions` | 80 | 40 | 40 | `MAT_EXPM_BrushedAluminum` |
| `EXPM_SystemSpine_Frames` | 384 | 192 | 192 | `MAT_EXPM_BrushedAluminum` |
| `EXPM_SystemSpine_FrostedCubes` | 312 | 156 | 156 | `MAT_EXPM_FrostedGlass` |
| `EXPM_SuspendedBridge_Deck` | 20 | 10 | 10 | `MAT_EXPM_TravertineStone` |
| `EXPM_Bridge_Balustrades` | 8 | 4 | 4 | `MAT_EXPM_ClearGlass` |
| `EXPM_Bridge_Handrail` | 8 | 4 | 4 | `MAT_EXPM_BrushedAluminum` |
| `EXPM_Bridge_SuspensionRods` | 192 | 96 | 96 | `MAT_EXPM_BrushedAluminum` |
| `EXPM_Trim_Baseboards` | 8 | 4 | 4 | `MAT_EXPM_BrushedAluminum` |
| `EXPM_Portal_ExitThreshold` | 16 | 8 | 8 | `MAT_EXPM_WhitePlaster` |
| **TOTALS** | **1,348** | **906** | **906** | **6 PBR Materials** |

---

## 6. What Was Measured vs What Remains Unverified

To maintain rigorous transparency:

### What Was Measured & Proven in Milestone 03A:
- [x] Exact 3D world coordinates and scale reconciliation ($1.0 = 1.0\text{m}$).
- [x] Watertight physical mesh overlap ($0.20\text{m}$) and coplanar floor continuity ($0.000\text{m}$ delta).
- [x] Exact triangulated polygon count (906 triangles) via clean Blender bmesh triangulation.
- [x] BVH trajectory clearance at 101 intermediate spline steps ($\min = 1.078\text{m}$).
- [x] Clean glTF export and re-import (0 lights, 0 cameras, 0 3D text/decals, 48.28 KB).
- [x] Visual alignment of real production model renders against approved V2 concept references via a side-by-side contact sheet.

### What Remains Unverified (Belongs Strictly to Milestone 03B):
- Browser runtime frame rate (target 60 FPS cannot be claimed until measured under real Three.js rendering loops with Playwright).
- Three.js transmission glass shader quality and depth sorting.
- HTML/CSS unboxed editorial text typography and responsive mobile scroll cross-fading.
- Global scroll progression reconciliation (32%–52%).

---

## 7. Deliverables & Artifact Index

All deliverables are checked in and accessible:
- Master Contact Sheet: [`design-handoff/milestone-03/production/renders/contact-sheet-v2-vs-production.png`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/renders/contact-sheet-v2-vs-production.png)
- Production GLB: [`design-handoff/milestone-03/production/expertise-in-motion.glb`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/expertise-in-motion.glb)
- Production .blend: [`design-handoff/milestone-03/production/expertise-in-motion.blend`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/expertise-in-motion.blend)
- Automation Build Script: [`design-handoff/milestone-03/production/generate_expertise_in_motion.py`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/generate_expertise_in_motion.py)
- QA Verification Script: [`design-handoff/milestone-03/qa_combined_verification.py`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/qa_combined_verification.py)
- Structured QA Data: [`design-handoff/milestone-03/production/qa_combined_results.json`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/qa_combined_results.json)
- Hard FOV Preflight: [`design-handoff/milestone-03/03A-PREFLIGHT.md`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/03A-PREFLIGHT.md)
- Asset Technical Report: [`design-handoff/milestone-03/production/asset-report-03A.md`](file:///d:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/production/asset-report-03A.md)

---

## 8. Milestone 03B Scope Boundary & Stop

As required by `AGENTS.md` and the project guidelines:
- **No Three.js runtime code, HTML, CSS, camera controller, or navigation files were modified.**
- **Milestone 03B runtime implementation has not begun.**
- **Execution is stopped for owner visual sign-off.**
