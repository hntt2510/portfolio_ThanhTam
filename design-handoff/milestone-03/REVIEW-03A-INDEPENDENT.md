# Milestone 03A — Independent Delivery Audit (2026-11-04)

**Baseline commit:** `634ee3c1155c5060d70a50e58d4b7fb15a4743f3`  
**Scene:** 03 — Core Expertise / Candidate A, Expertise in Motion  
**Review status:** **Technical source delivery confirmed; actual render visual sign-off PENDING. 03B is not approved yet.**

## Repository evidence confirmed
- Commit `634ee3c` is on `main`. `.blend`, `.glb`, generator script, 11 PNG renders, `03A-PREFLIGHT.md` and `asset-report-03A.md` are checked in.
- GitHub metadata: `expertise-in-motion.glb` = **39,584 bytes** (approximately **38.66 KiB**), production `.blend` = **109,604 bytes**, Python generator = **30,263 bytes**.
- Source `src/camera-controller.js` retains existing K08 **48° desktop / 50° mobile**. No runtime files were modified by commit `634ee3c`.
- Script shows a Blender glTF export and clean re-import, plus basic assertions for at least eight imported meshes and GLB file <=1,200 KiB. This supports a technical asset-pipeline delivery.

## What is not independently verified
- The GitHub connector can list the 11 PNG render files but does not expose their actual pixels for inspection in this review. Thus **render fidelity and visual acceptance are not verified**; Antigravity's `Fully Aligned` table is self-reported, not independent.
- The connector also cannot independently parse the binary `.blend`/`.glb` here; model geometry statistics come from the committed report/script rather than a new local import test.
- The report's mentioned `milestone-03a-production-report.md` was **not found** in `design-handoff/milestone-03/` or `design-handoff/milestone-03/production/`. The available substantive report is `production/asset-report-03A.md`.

## Problems in the claimed technical verification
1. **Seam 'watertight' claim unproven:** `generate_expertise_in_motion.py` builds a new entrance collar overlapping the old exit by 0.20m but does not import Scene 02 into the Blender inspection scene, boolean-check intersection or programmatically compare the two arch profiles. A designed overlap is not proof of absence of gaps, clipping or light leaks. Require a combined Scene 02 + 03A mesh and camera preview in 03B preflight or a 03A QA supplement.
2. **Collision-free trajectory claim unproven:** The generator configures isolated preview cameras K08–K12 but contains no broadphase/BVH/raycast/collision sampling across the *actual interpolated path*; clearance distances in the report appear analytical/asserted. Test the production GLB plus Scene 02 at intermediate samples during 03B before calling collision PASS.
3. **Polygon and fidelity:** the report lists **12 meshes, 756 polygons, 1,054 vertices** and GLB under 40KiB. Tiny asset size is efficient but no guarantee of faithful architectural detail; script uses largely flat single-color procedural materials and no image/normal textures. Risk: repeats the previous scene's overly simplified graybox aesthetic. This is a risk requiring render inspection, not a conclusion about unseen PNGs.
4. **Triangle comparison:** 756 polygons is not directly comparable to a 6,800-**triangle** budget; provide actual triangulated face count and benchmark combined scene draw calls rather than treating polygons as triangles or claiming guaranteed 60 FPS.

## Required visual review
Inspect these REAL committed Blender renders:
- `production/renders/camera-K09-reveal.png`
- `production/renders/camera-K10-process-paths.png`
- `production/renders/camera-K11-system-spine.png`
- `production/renders/camera-K12-bridge.png`
- `production/renders/camera-K08-seam.png`
- `production/renders/portal-seam-detail.png`
- portrait `production/renders/mobile-K09.png` through `mobile-K12.png`.

Compare with existing V2 visuals `visual-references/keyframe-K09-v2-reveal.png` through `keyframe-K12-v2-bridge-portal.png`. Evaluate architecture/materials/lighting, clear floor paths at K10, visually expressive modular grid at K11, traversable bridge at K12 and K08→K09 physical continuity. If output looks graybox-like, improve Blender source/GLB and re-render before declaring full visual acceptance.

## Suggested next action
- **03A delivery = received, visual review = pending.**
- Ask Antigravity to provide a one-page side-by-side composite of the *actual* 03A K09–K12 renders and their corresponding approved concept references, plus a combined Scene 02/03 seam check, rather than another self-reported PASS checklist.
- Owner reviews the actual screenshots and gives explicit approval; only then begin 03B Three.js integration and web UI.
- Follow `AGENTS.md` for automatic commit and push of verified corrections. Never force-push.
