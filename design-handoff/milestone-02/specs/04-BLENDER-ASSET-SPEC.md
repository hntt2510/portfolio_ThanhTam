# Milestone 02A — Blender / GLB Architectural Handoff

## Task
Extend the approved Scene 01 Entrance Atrium via its north-east K04 corridor into a broad, gently curved **Profile Gallery**; background architecture only. Keep the scene as a **connected set in one 3D world**.

## Source model and coordinates
- Read existing `design-handoff/milestone-01A/entrance-atrium.blend`, `entrance-atrium.glb`, `asset-report.md`, and the current K04 camera pose in the GitHub repo.
- Reuse same world units and coordinate conventions: metric scale; Blender Z-up; Three.js Y-up after GLTF transform.
- Make corridor joins physically contiguous: no wall seam, floor jump, or closed passage.
- Keep old Entrance Atrium geometry and baked elements unchanged except unavoidable seam corrections.

## Model only
- Curved walls/ceiling/stone floor, large glazed façade with thin mullions; soft architectural cove, subtle seating if composition benefits.
- Natural surroundings behind clear windows may be optimized geometry or texture, with open rights to use.
- **No information displays, freestanding caption panels, typography, screens, UI cards, or other narrative labels in the GLB.**
- Minimal safe PBR materials compatible with Three.js (warm plaster, matte light stone, clear architectural glass, brushed aluminum).
- Avoid heavy geometry and expensive glass layers; keep runtime asset trim and performance-friendly.

## Deliverables
- Editable `profile-gallery.blend` (or updated shared `.blend` plus a source model link).
- Export `profile-gallery.glb` with named meshes (prefix `PRG_`) and consistent scale/axes.
- Reproducible Blender Python script if procedural generation is used.
- K05–K08 proof renders from the **same geometry** and a top-down connection diagram.
- Technical report listing dimensions, object hierarchy, mesh/triangle estimates, material assumptions, bounding box, K04→K05 seam, and export validation.

## Verification & GitHub
- Open/re-import the GLB and verify integrity; confirm all exported assets load without private Windows paths.
- Update `PROJECT_STATUS.md`; **commit and push after 02A verified**, under existing repo `AGENTS.md` (no extra push approval).
- Do not claim browser runtime verification in Blender-only milestone.
