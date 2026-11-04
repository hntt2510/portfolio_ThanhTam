# Milestone 03 V2 — Independent Design & Engineering Review

**Date:** 2026-11-04  
**Baseline V2 design commit:** `17f2a224e20d04a0cf1525ad8a6b821910ae395f`  
**Status:** CONCEPT DIRECTION RECOMMENDED; OWNER VISUAL APPROVAL PENDING. This is a review, not approval of production implementation.

## Verified in repository

- V2 committed on `main` with three design candidates, comparison board, recommended Candidate A, four keyframe PNG references, Blender exploration file, design/motion/copy/asset specifications.
- Candidate A introduces a 36m × 18m asymmetrical sawtooth pavilion with distinctive spatial moments: process-path floor (K10), SAP system spine (K11), suspended bridge (K12). This is meaningfully different in **documented concept** from prior Scene 01 circular atrium and Scene 02 curved corridor.
- Camera and copy remain authored as scroll-driven, reversible, HTML/CSS text outside 3D geometry.
- **Image limitation:** This review confirmed file presence but could not decode/inspect the actual V2 PNG pixels via the available GitHub connector. Do not claim screenshot pixel-level or rendered aesthetic validation in this review.

## Important corrections before implementation

1. **K08 FOV mismatch:** `src/camera-controller.js` currently has desktop K08 FOV **48°** and mobile K08 FOV **50°** (`desktopWaypoints.fovs` and `mobileWaypoints.fovs`). But `design-handoff/milestone-03/03-CAMERA-LEDGER-V2.md` specifies desktop **46°** and mobile **48°**. Match the actual existing runtime at the boundary; do not introduce a 2° snap or silently alter previously accepted K08 framing. Reconcile ledger and all downstream K09+ camera FOVs accordingly.
2. **C1 not proven:** The K08 outgoing chord's angular difference from an incoming tangent does **not** mathematically establish C1 continuity or no jerk. After extending the existing master spline, compute finite difference derivatives of camera **position, look direction, FOV** on both sides of chapter seam, compare against stated numerical thresholds, and test actual visual scrubbing.
3. **Preserve existing shots:** Extending camera control from 9 to 13 waypoints must preserve Scene 01 / Scene 02 cinematic compositions and chapter-local timings. Do not indiscriminately remap global progress to a larger spline and shift K01–K08; use chapter-aware mapping or equivalent controlled segmentation with measured continuity.
4. **Model/story feasibility:** Verify the floor-branching shape is legible at K10 and does not read as decorative strips; structural SAP installation clearly shows integration rather than glowing sci-fi cubes; bridge elevation transitions physically and cinematographically without traversing railings, ceiling or architecture. Confirm bridge deck height and camera eye clearance in actual 3D.
5. **Artistic consistency and risk:** Silver, warm-white, travertine and ice-blue elements should relate to the existing Glass & Light Museum but must not reproduce the same editorial composition in every beat. Candidate A is a suitable concept, subject to visible owner approval.
6. **Unsupported performance claims:** Estimate of ~6,800 triangles and GLB <=1.2MB is a budget, **not evidence of guaranteed 60 FPS**. Establish total-scene draw calls, transparent-material cost, device pixel ratio and actual browser/mobile performance separately. Do not assert a PASS without measured evidence.
7. **Files and visual artifacts:** Use true original PNGs under `design-handoff/milestone-03/visual-references/`. Ensure filenames and paths are grounded. Do not invent final runtime GLB or mark 03A/03B delivered based on an exploration `.blend`.

## Approval gate

- Before production code or GLB export, owner should inspect:
  - `visual-references/01-three-concept-candidates.png`
  - `visual-references/02-scene02-vs-scene03-comparison.png`
  - `visual-references/05-ui-varied-compositions-board.png`
  - `visual-references/keyframe-K09-v2-reveal.png` through `keyframe-K12-v2-bridge-portal.png`.
- Scene 03 V2 is **ready for owner visual approval**, **not yet approved**. Do not launch 03A or 03B until owner approves. Once approved: 03A Blender production asset & GLB, verify and auto push; 03B Three.js integration, camera/nav/DOM, test and auto push per `AGENTS.md`.
