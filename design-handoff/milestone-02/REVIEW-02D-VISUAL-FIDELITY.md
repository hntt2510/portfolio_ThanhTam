# Milestone 02D — Visual Fidelity Review (Design QA)

**Review date:** 2026-11-04  
**Baseline commit:** `7ff7a5ee85c54062b49073b26a81e7473199332a`  
**Status:** Milestone 02C implemented and pushed; **visual fidelity NOT YET accepted by independent design review**. Scene 03 design may be planned, but do not implement it until the owner approves Scene 02's visual outcome.

## Inspected actual output
- `design-handoff/milestone-02/screenshots/desktop-03-k05-about-entry.png`
- `design-handoff/milestone-02/screenshots/desktop-05-k07-about-experience.png`
- `design-handoff/milestone-02/screenshots/desktop-06-k08-about-perspective.png`
- `design-handoff/milestone-02/screenshots/mobile-02-k05-about-entry.png`
- `src/camera-controller.js`, `app.js`, `styles.css`, `design-handoff/milestone-02/test_and_capture_02C.py`.
- Approved visual target: `design-handoff/milestone-02/visual-references/scene02-approved-visual-board-v2.png` and `SCENE02-V2-APPROVED.md`.

## Confirmed improvements
1. Large frosted rectangle around About content is removed; text is now direct DOM overlay on desktop and appears unboxed on mobile.
2. Full display name `Hoàng Nguyễn Thành Tâm` is present.
3. Four DOM narrative states are implemented and opacity/translation derive from progress.
4. Commit `7ff7a5e` is present on `main` with new Blender/GLB and screenshot artifacts. Automated console and derivative tests are agent-reported (not independently re-executed in this review).

## Remaining visual deviations (must fix before user acceptance)
1. **Gallery still resembles a white graybox rather than approved Glass & Light Museum.** Strongly flat/off-white walls and floor, nearly blank sky/background, minimal soft-shadows or material separation, not enough sense of natural skylight and spacious gallery depth.
2. **Exterior landscaping is visibly schematic.** Oversized green spherical tree canopies, uniform green strip and minimal texture are distracting in K05 and mobile K05; replace with believable but optimized multi-scale vegetation/landscape using licensed reusable assets, better geometry and light/material treatment. Do not place a flat still image that breaks the walking-camera parallax.
3. **Window framing remains too dominant:** K07 contains visible dark gray mullions crossing over/behind the large headline and body; slim and tone down the frames, move critical foreground elements, adapt camera composition or negative space while preserving a usable window system. Aim for text readable without visual crossing.
4. **Brand contrast issue:** top-left site mark and owner subtitle are very low contrast against the light gradient. Use deeper graphite, less wash over brand, appropriate text shadow or strategic placement. Keep all body/headline contrast readable across K05–K08.
5. **K08 lacks a legible 'threshold to next room' visual.** Improve the end-of-gallery portal architecture and eye-leading perspective, without fabricating Scene 03 geometry.

## Engineering constraints
- Keep scroll-scrubbed DOM transitions, existing chapter mapping, nav, reduced motion, mobile behavior and persistent Three.js renderer intact.
- Keep K04→K05 position/orientation/FOV continuous. Do not assert mathematical *exact* C1 from a finite-difference test with a tolerance; report it as numerical approximation with epsilon and observed difference. Do not regress it.
- Prefer Blender asset and renderer material/lighting enhancements to wholesale UI redesign. Tone mapping/color management, controlled environment lighting, baked ambient occlusion/lightmaps where appropriate, anti-aliasing, and appropriately rough PBR surfaces may help. Benchmark visual quality and performance.
- Inspect both original and new screenshots side by side with approved reference; screenshots alone are not proof of photorealism or approval.
- Automated checks should actually assert console warnings/failed requests, intermediate scroll behavior, and responsive text readability; test on actual browser/phone where feasible.

## Acceptance
- K05–K08 demonstrate credible curved museum geometry and visual depth: soft daylight/soft shadows, subtle stone surface and architectural glass, light/steel-blue material language, non-glaring highlights.
- The text remains **unboxed**, separate from 3D assets and legible on all inspected camera positions; no heavy mullions intersect important text.
- The owner name is high contrast and correctly accented.
- The exterior appears natural and unobtrusive, not low-poly green spheres.
- K08 clearly points toward the unbuilt Scene 03 opening.
- Preserve all existing functionality; deliver before/after annotated desktop+mobile screenshots, actual QA results, updated `PROJECT_STATUS.md`, and verified auto push to `main` under `AGENTS.md`.

**Recommended milestone:** 02D — Visual Fidelity Pass. No new chapter coding in this task.
