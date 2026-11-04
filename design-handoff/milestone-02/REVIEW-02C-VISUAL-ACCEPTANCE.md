# Milestone 02C — Visual Acceptance Review & Required Refinements

**Reviewed:** 2026-11-04 (Asia/Ho_Chi_Minh)  
**Reviewed against:** approved Scene 02 V2 design in `design-handoff/milestone-02/specs/01-DESIGN-SPEC.md` and visual references.  
**Baseline implementation:** `dca778b3a19a74036688e9b74a47beabea6792c9` (`main` at review).  
**Verdict:** Milestone 02A and 02B code/assets are present and committed. **Technical delivery accepted; visual design acceptance is pending. Do not label Scene 02 fully approved or proceed with Scene 03 implementation before resolving the differences below.**

## Evidence inspected
- `design-handoff/milestone-02/screenshots/desktop-03-k05-about-entry.png`
- `design-handoff/milestone-02/screenshots/desktop-05-k07-about-experience.png`
- `design-handoff/milestone-02/screenshots/desktop-06-k08-about-perspective.png`
- `design-handoff/milestone-02/screenshots/desktop-02-k04-transition-seam.png`
- `design-handoff/milestone-02/screenshots/mobile-02-k05-about-entry.png`
- `styles.css`, `app.js`, `src/camera-controller.js`, `index.html`, and automated QA script.
- See approved Scene 02 reference board and K05–K08 image references in `design-handoff/milestone-02/visual-references/`.

## Priority 0: Deviations from approved Visual Board V2

1. **Unboxed editorial overlay required.** Current `.about-overlay` in `styles.css` uses a frosted background, `backdrop-filter: blur(14px)`, substantial padding, border, rounded corners and box shadow. This creates a large framed card visible on desktop and mobile, contradicting the approved spec: *unobstructed left-aligned editorial DOM overlay, not a bordered card*. Remove visible card styling on desktop. Use only a subtle unframed, left-edge readability gradient where necessary. Mobile text must remain readable without a prominent outlined bottom card (a soft unframed gradient is acceptable).
2. **Environment looks like graybox rather than Glass & Light Museum.** Actual screenshots show flat white surfaces, prominent dark repeated vertical bars, low-poly gray/green exterior objects and little architectural glazing/daylight depth. Refine Blender mesh and web PBR materials/lighting to evoke the approved spacious, bright, softly sunlit curved corridor with tall realistic windows, slim silver mullions, warm plaster, pale stone, restrained reflections, and natural-looking exterior. Preserve geometry continuity with Scene 01 and do not resort to neon/bloom. Use the supplied approved reference PNGs as art-direction targets, not as exact photorealism promises.
3. **Legibility and camera framing.** Screenshots show thick foreground mullions/beams intruding into brand and chapter UI, especially at K07/K08. Adjust geometry visibility, material appearance and/or camera framing so the architecture creates depth without obscuring content or dominating the view.

## Priority 1: Motion and verification

4. **Scroll-synchronized copy transition.** Current `app.js` maps progress to four discrete class switches, while `.about-beat` uses CSS transitions of 360ms. The result may continue transitioning after the scroll stops and cannot be directly scrubbed backwards through a partial transition. Implement an opacity/translateY curve evaluated from chapter-local scroll progress around transitions; preserve exact content selection for accessibility and reduced-motion.
5. **C1 continuity claim needs verification.** Matching K04 and K05 position/target/FOV proves C0, not tangent/velocity continuity. Camera code uses separate Catmull-Rom curves across the 0.40 boundary. Measure finite-difference camera position, look direction, and FOV before/after this boundary on desktop/mobile; adjust tangents/curves if needed, and report results rather than assuming C1.
6. **Improve automated QA assertions.** Current Playwright script checks active classes and captures screenshots, but screenshot creation itself is not a visual-quality pass; console warnings are not included in the errors-only collector. Add explicit warning and 404 tracking, measurable screenshot regression/diff where practical, and test at intermediate scroll positions. Test FPS/frame stability on a real target device separately if possible. Document hardware/runtime constraints transparently.

## Priority 2: Content consistency

7. The portfolio owner is **Hoàng Nguyễn Thành Tâm**. Use this exact accented display name in visible UI where the name is rendered; keep ASCII slugs for file paths if needed.
8. Keep the three future chapters disabled/unbuilt and preserve Scene 01 approved architecture. Maintain one persistent renderer, native scroll, correct active section, fallback/reduced-motion/mobile support.

## Acceptance requirements

- Compare screenshots K05–K08 and mobile K05/K07 **side-by-side with approved reference images**, not just with each other.
- Confirm text is visually unboxed on desktop; mobile uses unobtrusive gradient instead of prominent border/card.
- Corridor looks like a finished daylight museum, not a graybox; no text/info panels in 3D.
- Verify K04→K05 continuous position, orientation **and tangent behavior**.
- Camera and DOM copy remain reversible for forward/back, fast scroll, drag, and nav jumps.
- Preserve source `.blend`, `.glb`, test script, and screenshots; update `PROJECT_STATUS.md`.
- Auto-commit and push verified refinement work to `main` following `AGENTS.md` (no extra push approval; no force-push).
- Include actual screenshots, verification report, and a remote commit SHA/link. The owner will still decide the final visual acceptance.

## Suggested implementation phase

**Milestone 02C – Visual Polish & Scroll-Sync Fix**; modify existing Scene 02 in place. Do not build Scene 03 geometry until this design-deviation review is cleared.
