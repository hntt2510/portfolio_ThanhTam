# ANTIGRAVITY MASTER PROMPT — MILESTONE 02: PROFILE GALLERY V2

## ROLE & OUTCOME
You are the senior Three.js creative technologist, Blender modeling specialist, front-end accessibility engineer, and QA lead for Project Museum. Implement **Scene 02: Profile Gallery** in the already-existing `hntt2510/portfolio_ThanhTam` repository, preserving Scene 01 and the approved Glass & Light Museum design. Do not create a separate demo site.

**Most important clarification from the owner:** The owner is **Hoàng Nguyễn Thành Tâm**. The story belongs in the **HTML/CSS interface**. The 3D corridor is atmospheric architecture only. There must be **NO three glass boards displaying Foundation/Experience/Perspective**, no caption-text walls, no info cards, and no text or UI as 3D meshes.

## SOURCE OF TRUTH (READ IN ORDER)
1. `AGENTS.md` and `PROJECT_STATUS.md` in the repository (including automatic GitHub push policy).
2. Current `src/world.js`, `src/scenes/entrance-atrium.js`, `src/camera-controller.js`, `app.js`, `index.html`, `styles.css`.
3. `design-handoff/milestone-01A/asset-report.md` and `design-handoff/milestone-01B/verification-report.md`.
4. This folder's `specs/01-DESIGN-SPEC.md`, `02-CAMERA-AND-SCROLL-LEDGER.md`, `03-CONTENT-COPY.md`, `04-BLENDER-ASSET-SPEC.md`, `qa/ACCEPTANCE-CHECKLIST.md`.
5. All PNGs in `visual-references/`. The approved V2 board defines visual *mood*, UI/camera beats, and placement—not finalized mesh coordinates. Incidental wall lettering in generated imagery MUST NOT be reproduced.

## PROJECT MEMORY / LOCKED DESIGN
- Bright warm white, light stone, silver, restrained ice blue; no dark navy/neon/cyberpunk.
- Entrance Atrium: Circular Skylight, three staggered glass installation objects, Hero left, fixed scroll navigation right. Preserve Scene 01.
- Scene 02: light-filled curved corridor with floor-to-ceiling windows, slim aluminum mullions, white wall/ceiling and matte stone floor; NO narrative exhibition objects.
- One persistent Three.js world and renderer. Camera and four DOM About copy states are driven by the same reversible scroll progress.
- Browser tests and screenshots required. Auto commit/push each verified unit of work, no added approval step for pushing.

## PREFLIGHT (inspect; do not guess)
- Fetch/pull latest `main`; inspect git status and current repo head; preserve existing user modifications.
- Check Blender version/tool availability, Three.js import map, GLTFLoader import, asset paths, and current camera/fov at K04.
- Confirm Scene 01 has no regressions before changing it.
- Follow repository `AGENTS.md` and report meaningful blockers instead of replacing the stack or destroying files.

## DELIVERY 02A — BLENDER GRAYBOX (commit+push after verification)
1. Design and build the Scene 02 continuation from the existing K04 corridor. Import/inspect Scene 01 Blender source and coordinate frame; connect floors and portal geometry seamlessly.
2. Create a spatially coherent bright *curved glass corridor* with warm plaster wall, clear windows/slim brushed-silver mullions, restrained daylight and pale matte stone floor. Furnish minimally.
3. Keep the model background-only; no inscriptions, plaque/info panels or text-on-glass.
4. Preserve editable `.blend`, export named `.glb`, plus reproducible script if used, K05–K08 consistent render frames, top-down join image, and asset report.
5. Re-import/validate actual GLB. Update `PROJECT_STATUS.md` and commit+push **verified 02A** deliverables; report remote SHA.

## DELIVERY 02B — THREE.JS INTEGRATION (commit+push after verification)
1. Extend the *existing* persistent renderer and scene to load the new gallery GLB, no duplicated atrium meshes. Keep the original GLB visible when needed in Scene 01.
2. Introduce a reusable global-scroll to chapter-local-progress map derived from chapter boundaries; do not permanently hardcode '12–32% of entire site'. Scene 01 and Scene 02 must own appropriate time/scroll ranges without changing old camera beats.
3. K05 begins **exactly** where K04 ends (position, look-at and FOV). Continue through gallery with K06 Foundation, K07 Experience, K08 Perspective/Exit, calibrated against actual Blender mesh. No camera clipping, hard scene cut or teleport.
4. Build screen-fixed HTML content overlay with 4 exact copy states in `specs/03-CONTENT-COPY.md`; use subtle transitions and straightforward reading order. No boxes around text. Update visual owner name to Hoàng Nguyễn Thành Tâm.
5. Keep right nav scroll-aware: `01 Introduction` active in Scene 01; `02 About` active in Scene 02. Upcoming sections remain non-functional until implemented. The progress indicator must represent actual global progress.
6. Maintain keyboard accessibility, mobile portrait-specific framing, reduced-motion mode, native scrolling, WebGL fallback and responsive text contrast.
7. Preserve imported Three.js module version/loader compatibility, prevent duplicate render loops, and handle loading/error states honestly.

## QA — REQUIRED, NOT OPTIONAL
- Actually run the project locally, check screenshots against approved refs, and test 1440×900 desktop + 390×844 mobile.
- Capture at least K04 before transition and K05, K06, K07, K08; include mobile Foundation/Experience and reverse scroll K04.
- Test fast-forward, reverse, scrollbar drag, reload in Scene 02, keyboard navigation and a reduced-motion sample.
- Verify true active chapter labels and proper About copy. Compare reverse camera states mathematically (positions/FOV/targets) and/or use a pixel comparison; screenshots *alone* do not prove pixel-identical reversibility.
- Report actual console/network warnings and GLB load results; avoid unsupported claims of GPU/FPS on real devices without hardware measurement.
- Record remaining issues and update `PROJECT_STATUS.md`.

## AUTOMATIC GIT POLICY
Do not ask for an extra authorization to commit or push after completed, verified 02A or 02B. Review staged diff for secrets/public-data leaks, commit to current allowed project branch and push without force; verify remote SHA and report commit URLs. If branch protection rejects direct push, follow the safe alternative in `AGENTS.md` and disclose any blocker. Never claim success before verifying the remote.

## STOP CONDITIONS
- Do not build Scene 03 or later chapters.
- Do not redesign Scene 01 or existing owner brand.
- Do not move biographical text into 3D, even if the generated reference image suggests it.
- Stop and document a blocker if Blender is unavailable, mesh connectivity cannot be achieved, or camera path crosses solids; do not fabricate proof renders or test passes.
- Complete and push verifiable partial work only when it is internally consistent and clearly labeled partial, not complete.

## FINAL RESPONSE FORMAT
State: 02A status, 02B status, commit SHA(s) and URLs, changed file manifest, exact test results with screenshot links, visual deviations from approved V2, unresolved issues, and next milestone suggestion. Do not claim user visual approval merely because automated tests pass.
