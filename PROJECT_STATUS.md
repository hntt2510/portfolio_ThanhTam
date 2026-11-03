# Project Museum — Progress Tracker

**Updated:** 2026-11-03 (Asia/Ho_Chi_Minh)  
**Repository:** https://github.com/hntt2510/portfolio_ThanhTam  
**Integration branch:** `main`  

## Current milestone status

| Milestone | State | Evidence | Remaining validation |
|---|---|---|---|
| 01 — Initial Entrance Atrium Three.js | Committed | `ed69536`, `index.html`, `app.js`, `src/world.js`, `src/scenes/entrance-atrium.js`, `src/camera-controller.js` | Procedural prototype superseded by Milestone 01B GLB integration |
| 01A — Blender graybox & GLB export | Committed | `9e50764`, `design-handoff/milestone-01A/` contains `.blend`, `.glb`, generator, K01–K04 PNGs, top-down render and report | Fully verified & exported 70-mesh GLB (1.18 MB) |
| 01B — Import Blender GLB into website | **Committed & Verified** | `entrance-atrium.glb` integrated in `src/scenes/entrance-atrium.js`, `src/camera-controller.js` waypoints K01–K04 aligned, 8 automated Playwright screenshots in `design-handoff/milestone-01B/screenshots/`, report in `verification-report.md` | Ready for Milestone 02 (Profile Gallery) |

## Approved design constraints

- Glass & Light Museum; Circular Atrium and circular skylight.
- Three staggered frosted-glass panels, subtle highlights and restrained reflections.
- Bright warm-white / silver / pale blue palette; no dark navy or neon.
- Hero content left; fixed scroll-aware vertical navigation right.
- Camera beats K01 Establishing, K02 Approach, K03 Focus, K04 Transition.
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

## Next task — Milestone 02: Profile Gallery (About Scene)

1. Design & block Profile Gallery extending from the North-East corridor portal (K04).
2. Create seamless camera path continuing past K04 into the gallery space.
3. Transition HTML overlay from Hero to biographical and academic background.

## GitHub publishing rules

After each successfully verified completed unit of work, the implementation agent must commit and push to GitHub automatically without a separate approval prompt, subject to safe Git practices and repository protection. Never assert remote success without confirming the remote SHA. See `AGENTS.md`.
