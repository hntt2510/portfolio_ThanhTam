# Project Museum — Progress Tracker

**Updated:** 2026-11-03 (Asia/Ho_Chi_Minh)
**Repository:** https://github.com/hntt2510/portfolio_ThanhTam
**Integration branch:** `main`

## Current milestone status

| Milestone | State | Evidence | Remaining validation |
|---|---|---|---|
| 01 — Initial Entrance Atrium Three.js | Committed | `ed69536`, `index.html`, `app.js`, `src/world.js`, `src/scenes/entrance-atrium.js`, `src/camera-controller.js` | Browser visual/interaction tests and mobile performance still require independent review |
| 01A — Blender graybox & GLB export | Assets committed | `9e50764`, `design-handoff/milestone-01A/` contains `.blend`, `.glb`, generator, K01–K04 PNGs, top-down render and report | Verify actual Blender model and rendered fidelity; file presence alone does not equal approved visual quality |
| 01B — Import Blender GLB into website | **Not yet integrated** | Current `src/world.js` still constructs `new EntranceAtriumScene()` with procedural JS geometry; no GLTFLoader use seen in runtime | Integrate `design-handoff/milestone-01A/entrance-atrium.glb` into a persistent scene, reconcile coordinates and camera, test web behavior |

## Approved design constraints

- Glass & Light Museum; Circular Atrium and circular skylight.
- Three staggered frosted-glass panels, subtle highlights and restrained reflections.
- Bright warm-white / silver / pale blue palette; no dark navy or neon.
- Hero content left; fixed scroll-aware vertical navigation right.
- Camera beats K01 Establishing, K02 Approach, K03 Focus, K04 Transition.
- One persistent 3D world, reversible normalized scroll, HTML overlays for readable content.
- Incremental development: design/approve/handoff/build/verify each milestone before the next.

## Audit observations (2026-11-03)

- The Blender export exists in `design-handoff/milestone-01A/entrance-atrium.glb` (1,178,968 bytes).
- The initial procedural Three.js scene is in `src/scenes/entrance-atrium.js`, and uses geometry dimensions different from those described in the Blender report. Do not assume either version's camera coordinates will transfer unchanged.
- The Blender report claims a successful export/re-import and render validation; these results are agent-reported, not independently verified in this audit.
- The current project uses native ES modules and a vendored `three` module; check compatibility when adding GLTFLoader.
- A CV PDF is tracked in this **public** repository; review whether that public exposure is intentional before expanding public assets.

## Next task — Milestone 01B

1. Read `AGENTS.md`, this status file, and the Milestone 01A asset report.
2. Check project health and actual GLB coordinate/bounding-box details.
3. Load the GLB into the existing persistent WebGL world, replacing (not duplicating) the procedural atrium geometry after visual comparison.
4. Align camera K01–K04 and the Profile Gallery corridor transition to Blender asset coordinates; verify hero and navigation are not occluded.
5. Test reverse/fast scroll, viewport resize, reduced motion, WebGL fallback, and browser console errors.
6. Produce genuine screenshot/video evidence and an integration report with unresolved problems.
7. Update this tracker; automatically commit and push verified work to GitHub following `AGENTS.md`, then report the remote SHA/link.

## GitHub publishing rules

After each successfully verified completed unit of work, the implementation agent must commit and push to GitHub automatically without a separate approval prompt, subject to safe Git practices and repository protection. Never assert remote success without confirming the remote SHA. See `AGENTS.md`.
