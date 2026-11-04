# ANTIGRAVITY IMPLEMENTATION PROMPT — MILESTONE 03A
## Project Museum / Scene 03 V2: Expertise in Motion — Blender Production Asset

**Owner:** Hoàng Nguyễn Thành Tâm  
**Approved concept:** Candidate A — **Asymmetric Sawtooth Pavilion / Expertise in Motion**  
**Scope:** Milestone **03A ONLY** — production-ready Blender scene, editable sources, exported GLB, camera preview renders, asset validation, progress report, automatic GitHub push.  
**Status:** Owner has approved Candidate A. This is NOT approval to implement Scene 03B Three.js, HTML UI, or future scenes.

### ROLE AND SUCCESS TARGET
Act as a senior Blender technical artist / architectural environment modeler and asset pipeline engineer. Build a visually credible, optimized architectural environment in real mesh geometry, not a graybox and not an AI illustration. The production scene must communicate three distinct physical narratives at first glance: branching BA process pathways, the modular SAP system spine, and a suspended Solution Consulting bridge. It must physically connect to Scene 02, offer clean camera views K09–K12, and export a valid GLB. Do not confuse generating a screenshot with meeting a visual-quality standard.

## 0. READ / RECONCILE BEFORE RUNNING BLENDER

First inspect the actual repository, active branch, and latest remote SHA, then read ALL:

1. `AGENTS.md`
2. `PROJECT_STATUS.md`
3. `design-handoff/milestone-03/01-DESIGN-SPEC-V2.md`
4. `design-handoff/milestone-03/02-VISUAL-DIRECTION-V2.md`
5. `design-handoff/milestone-03/03-CAMERA-LEDGER-V2.md` **(corrected K08 FOV values)**
6. `design-handoff/milestone-03/04-CONTENT-COPY-V2.md` **(UI reference only, do NOT embed text in GLB)**
7. `design-handoff/milestone-03/05-BLENDER-ASSET-PLAN-V2.md`
8. `design-handoff/milestone-03/06-ACCEPTANCE-CHECKLIST-V2.md`
9. `design-handoff/milestone-03/REVIEW-V2-INDEPENDENT.md`
10. `src/camera-controller.js` (read only; do not edit)
11. `design-handoff/milestone-02/profile-gallery.glb` and its Blender generator/report, especially the K08 exit portal geometry.

**Mandatory hard preflight gate: K08 camera FOV.**
- Live `src/camera-controller.js` at handoff has **K08 DESKTOP FOV 48.0° and MOBILE FOV 50.0°**, not the outdated 46° / 48° stated in earlier Scene 03 drafts.
- K08 desktop position: `(36.53, 1.80, -21.62)`, look-at target `(43.24, 2.20, -19.98)`; K08 mobile position `(36.53, 1.88, -21.62)`, same target.
- Verify those values in the current runtime BEFORE generating the production model. The corrected `03-CAMERA-LEDGER-V2.md` must agree with runtime. If the runtime has changed, report the mismatch, amend Scene 03 documentation only as needed to preserve the live K08 view, and explain the decision in your 03A report.
- **Never change `src/camera-controller.js` or Scene 01/02 code to force a match.** K08 FOV is the existing scene's anchor. K09+ draft FOV may be adapted for smooth preview; preserve source evidence. The 03B agent will handle live multi-chapter camera integration.
- Check entry-portal geometry and World coordinate map before making a new mesh. Do not assume matching anchor numbers alone proves a seam is physically watertight.
- First document the verified K08 values and scene anchor in `design-handoff/milestone-03/03A-PREFLIGHT.md`. **Do not proceed to modeling until this preflight is complete.**

## 1. REFERENCE IMAGE REQUIREMENTS — READ THE REAL FILES
Use the already committed reference images in:

`design-handoff/milestone-03/visual-references/`

Primary image inputs to visually inspect (do not merely read filenames):
- `01-three-concept-candidates.png` (selected Candidate A, reject B/C)
- `02-scene02-vs-scene03-comparison.png`
- `03-recommended-concept-hero.png`
- `04-camera-storyboard-k09-k12-v2.png`
- `05-ui-varied-compositions-board.png`
- `06-spatial-route-and-topdown-v2.png`
- `07-material-lighting-feasibility-v2.png`
- `keyframe-K09-v2-reveal.png`
- `keyframe-K10-v2-process-paths.png`
- `keyframe-K11-v2-system-spine.png`
- `keyframe-K12-v2-bridge-portal.png`

Also inspect **the real Scene 02 K08 screenshot** at:
`design-handoff/milestone-02/screenshots/desktop-06-k08-about-perspective.png`

These are actual existing repository paths. Visual assets are art-direction targets, not texture maps to be pasted onto geometry. Do not copy 3D wording, interface elements or labels from the images into the model.

If an input is missing/corrupt, report that and continue only using verified sources; do not invent an image or claim that it was inspected.

## 2. PRODUCTION GEOMETRY: THE SELECTED CONCEPT

Build a **36m × 18m asymmetric sawtooth daylight pavilion**, physically connected to Scene 02 K08 through a compatible vestibule. Relative roof height approximately **6.2m → 10.5m** and four north-facing clerestory bays (check their exact orientation in Blender/Three.js coordinates). Avoid another circular rotunda, repetitive white corridor or game-like sci-fi hall.

### Zone 1: K09 — Pavilion reveal
- An architectural compression→expansion moment from the existing curved Scene 02 portal.
- Credible warm-white plaster, sculpted wall reveals, restrained brushed metal joints, large sawtooth roof.
- Frame the big change of volume, negative space for later HTML headings, daylight falling into the space.
- No scene reload or independent floating building unrelated to the physical portal.

### Zone 2: K10 — Business Analysis process pathways
- Thin **INLAID** basalt-and-silver physical paths in light travertine floor, with meaningful branching and convergence.
- Ground pattern must read visually from the proposed elevated oblique camera without text or colored neon lines.
- Integrate pathways flush with the floor (avoid floating strips / z-fighting).
- Preserve a calm reading region for future bottom-left editorial UI.

### Zone 3: K11 — SAP / Enterprise Systems system spine
- Refined, structurally credible **4 × 2 × 3 bay modular matrix** made from brushed aluminum framework and restrained frosted glass.
- Architecture and proportions should communicate systems connectivity, modularity, and integration; no random glowing cubes, billboard textures, 3D skill labels, or signage.
- Create rich, believable parallax for a side-tracking camera, with safe clearance from frames.
- Transparent materials must be optimized and may require final web-side calibration in 03B.

### Zone 4: K12 — Solution Consulting bridge
- Physically modeled suspended pedestrian bridge about **14m long / 3.2m wide**, with nominal deck elevation **2.4m**, credible support/connection and glass guardrails.
- Bridge crosses an articulated interior void toward Scene 04's exit threshold; model only the Scene 03 exit opening, **NOT** Scene 04 space.
- Verify the camera can move above the deck at approx **Y=4.05m eye position**, with reasonable clearance to railings and ceiling.
- Make the forward destination architecturally legible.

Use metric scale. Preserve world position and the Blender-to-Three mapping:
`X_three=X_blender; Y_three=Z_blender; Z_three=-Y_blender`.
Keep the entry threshold near Three.js `(43.24,0,-19.98)`; inspect and fit existing geometry rather than using that one point as the only fitting condition.

## 3. ASSET ART DIRECTION / QUALITY BAR

Maintain the shared Glass & Light Museum identity with scene-specific architecture:
- warm white matte plaster (~`#F8F8F5`)
- light natural travertine (~`#F4F2EC`)
- honed basalt paths (~`#52565C`)
- brushed silver aluminum (~`#EEF3F8`)
- restrained ice-blue glazing (~`#D7E8F6`)
- natural north-facing daylight and physically plausible shadows

Avoid:
- flat graybox walls / blown-out uniformly white surfaces
- chrome mirror floors / intense bloom / dark navy
- massive unchamfered primitives, low-poly placeholder architecture
- glowy sci-fi cubes or floating installations
- baked-in text, decals, UI cards, labels, icons or badges
- replacing geometry with static 2D pictures just to imitate references

Create quality using restrained bevels, reveal lines, plausible surface roughness, controlled ambient and directional lighting, clean hierarchy and detailed-but-efficient architecture. Render previews with actual Blender lights/cameras; **exclude preview cameras/lights from exported runtime GLB**.

Budget is a target, not a guarantee: aim GLB `<=1.2MB`, approx `6,800 tris` or justify exceeding it if required for visibly better results. Optimize duplicate geometry/materials; avoid heavy transparent overdraw. **Never claim 60 FPS without measuring an actual browser integration** (03B owns runtime verification). Preserve quality if a budget is impractical and report the compromise.

## 4. CAMERA PREVIEW AND COLLISION CHECKS

Create separate Blender-only preview cameras positioned using the approved Scene 03 V2 coordinates converted consistently:
- K09 Three.js pos `(44.50,1.85,-19.40)`, target `(55.80,3.80,-14.10)`, provisional FOV 52°
- K10 pos `(49.50,3.20,-14.20)`, target `(57.80,0.20,-10.30)`, FOV 46°
- K11 pos `(56.80,1.85,-11.20)`, target `(58.50,2.20,-4.50)`, FOV 48°
- K12 pos `(63.20,4.05,-8.20)`, target `(75.00,4.20,-2.80)`, FOV 50°

Preview the K08 seam at **48° desktop / 50° mobile**, anchored to actual Scene 02 end framing. Use vertical FOV carefully; do not confuse lens length, horizontal FOV and vertical FOV.

Inspect geometry along the **ENTIRE interpolated path**, not only endpoints. Report if any waypoint must be adjusted due to wall, frame, bridge, floor, railing or ceiling collision. Preserve K08; proposed downstream waypoints may change for justified art/collision reasons and must be documented for 03B.

Produce and inspect actual rendered images:
- `camera-K08-seam.png` (existing end view aligned against Scene 02)
- `camera-K09-reveal.png`
- `camera-K10-process-paths.png`
- `camera-K11-system-spine.png`
- `camera-K12-bridge.png`
- `top-down-layout.png`
- `portal-seam-detail.png`
- optionally `mobile-K09.png`, `mobile-K10.png`, `mobile-K11.png`, `mobile-K12.png` for portrait composition review

Render these **from the production Blender model**, not from previous V2 exploration concept images. If visual quality is obviously below the reference, improve the asset and rerender before declaring completion. Provide side-by-side references vs actual model renders in the report.

## 5. BUILD AND EXPORT

Expected file organization:
`design-handoff/milestone-03/production/`
- `expertise-in-motion.blend` — editable single-candidate production file
- `generate_expertise_in_motion.py` — reproducible Blender generation/build script if applicable
- `expertise-in-motion.glb` — runtime asset, correct scale/transforms/materials
- `renders/` — K08–K12, top-down and seam visual evidence
- `asset-report-03A.md` — asset inventory, mesh/triangle counts, material/texture stats, scale, dimensions, transformations, GLB test, collision checks, known limitations
- `03A-PREFLIGHT.md` — K08 FOV/coordinate reconciliation

Do not overwrite or delete the approved V2 reference board files. Keep the original `scene03-v2-exploration.blend` as design evidence; the new production `.blend` is separate.

Export GLB with:
- consistent world transforms and meter scale
- predictable `EXPM_` node naming / hierarchy
- only real geometry and compatible PBR materials
- correct normals, UVs and mesh winding
- **no baked text/info cards, preview lights or preview cameras**

Re-import exported GLB into a clean Blender scene and verify geometry/material count, bounds, normals, scale, portal placement and basic visual parity with source. Use any available GLB inspection script to validate binary integrity, required nodes, and no accidental animation/camera/light payloads. Do not claim validation for a check not run.

## 6. STRICT ACCEPTANCE GATES

- [ ] **K08 preflight verified first**: runtime FOV desktop 48°, mobile 50°, actual coordinates/target documented; previous 46°/48° mistake not copied forward.
- [ ] K08 portal seamless in physical geometry with existing Scene 02, not merely numerically close as a single point.
- [ ] Scene 03 is visually distinct from prior circular atrium / curved gallery.
- [ ] K09 reveal shows roof and sense of sudden spatial expansion.
- [ ] K10 branching floor paths clearly readable from high-angle view.
- [ ] K11 structural system spine strongly recognizable, believable and non-neon.
- [ ] K12 elevated bridge and forward exit framed cleanly with no camera collision.
- [ ] Preview cameras do not intersect model during travel, verified with samples/intermediate points.
- [ ] Render artifacts reflect actual newly built production model.
- [ ] GLB re-import validation passes; source .blend remains editable.
- [ ] No information labels, 3D text, portfolio copy or UI components inside GLB.
- [ ] File sizes, triangle counts, draw-call implications, materials and limitations documented accurately.
- [ ] No edits to old runtime camera, Scene 01/02, app, CSS, HTML or navigation.

If any major quality/collision/export criterion fails, fix it before claiming completed. State blockers truthfully if unavailable.

## 7. AUTOMATIC GITHUB COMMIT + PUSH

Follow `AGENTS.md`; this owner has explicitly authorized routine automatic pushes.

1. Recheck current `main` and remote before making changes; do not overwrite newer work.
2. Add only production source assets, intended reports, actual render evidence and necessary corrected design notes. No private files, credentials or unintended large stock assets.
3. Update `PROJECT_STATUS.md` to **03A asset produced, awaiting visual owner review / 03B not implemented**. Do not mark Scene 03 fully implemented.
4. Run validations; inspect staged diff and binary asset sizes.
5. Commit with message such as `feat(blender): produce Scene 03 Expertise in Motion GLB and evidence (03A)`.
6. **Automatically push to `origin/main` after verified completion; do NOT ask for a separate push permission.** Respect branch protection; no force-push.
7. Verify remote HEAD SHA; provide exact commit URL. If push fails, clearly say so.

## 8. STOP / DELIVERABLE REPORT

Stop after 03A, with:
- FOV preflight result (desktop/mobile) and any corrected doc files
- exact file paths to .blend, .glb, builder script and render PNGs
- a contact sheet or direct links showing K09–K12 real production renders
- scale/geometry counts, file sizes, material issues and portal seam evidence
- Blender CLI/export/re-import verification logs or factual results
- camera collision findings and any proposed waypoint changes for 03B
- verified GitHub remote commit SHA/link
- open defects and specific recommended 03B integration tasks

**Do not implement 03B Three.js, add DOM copy/navigation, deploy, or create Scene 04. Wait for the owner to review visual Blender output first.**
