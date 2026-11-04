# Scene 02 – Profile Gallery V2 (APPROVED)

Approved on 2026-11-04 for portfolio owner **Hoàng Nguyễn Thành Tâm**. Design approved; Blender modeling and Three.js implementation are NOT yet complete.

## Non-negotiable correction

Scene 02 is a **continuous scroll-driven architectural gallery**. The background is a curved, white/ivory museum corridor with tall glazed windows, slim aluminum mullions, pale stone floor, gentle ceiling light and natural greenery outside. **Do not create any 3D informational glass panels, wall plaques, signs, cards, or text mapped onto glass**. All About content is **HTML/CSS overlay text**, updating as the **same scroll** advances the camera.

Existing Entrance Atrium K04 must hand off continuously to K05 in the same persistent Three.js world. In commit 75e8452, K04 desktop camera position is (4.80, 1.80, -4.80), look-at (12.00, 1.80, -12.00) and FOV 48 degrees. Read current code before deriving geometry and confirm continuity; don't hardcode new waypoints without visual/geometry testing.

## Copy (English UI only)

- **K05 – My Journey**: “From Software Engineering to Enterprise Problem Solving.” Body: “A journey from building a technical foundation to understanding business processes and developing practical enterprise solutions.”
- **K06 – Foundation**: “Built on a Technical Foundation.” Body: “I studied Software Engineering at FPT University, with an academic focus on SAP and enterprise systems.”
- **K07 – Experience**: “Turning Requirements into Solutions.” Body: “My experience spans software development, business requirements analysis, and customer-facing solution consulting.”
- **K08 – Perspective**: “Connecting Business & Technology.” Body: “I combine technical understanding and business process thinking to help shape practical enterprise solutions.”

The owner name on the interface is **Hoàng Nguyễn Thành Tâm** (ASCII filename slug: Hoang-Nguyen-Thanh-Tam).

## UI/camera requirements

1. Hero/About copy in unboxed, left-aligned editorial DOM overlay; light gradient allowed solely for contrast, no three cards.
2. Fixed right vertical nav highlights **02 About** during Scene 02 and Introduction during Scene 01. Other sections stay inactive until built.
3. Four K05–K08 camera/copy states derive from global scroll → chapter → local progress, reversible without refresh or auto-play.
4. K05 begins at K04's exact position/look-at/FOV; no camera teleport or hard scene cut.
5. Mobile and reduced-motion variants preserve readable copy.
6. Preserve Glass & Light Museum colors: #F7F8F6, #E8EBED, #D7E8F6, #6F9EC8, #263640; no navy/cyberpunk/neon.
7. Don't build Scene 03 yet.

## Workflow / reference assets

Full prompt, approved original board and four extracted keyframe reference PNGs are included in the conversation attachment **Profile_Gallery_Scene_02_V2_Antigravity_Handoff.zip**. Before implementation, the agent must extract them into `design-handoff/milestone-02/` and inspect the images. This GitHub file is a summary; the ZIP contains the authoritative detailed spec, motion ledger, Blender asset spec and QA checklist. Any incidental signage in AI concept images is **not** to be modeled.

- **Milestone 02A**: Blender graybox physically extending Scene 01 corridor; `.blend`, `.glb`, render evidence and report; verify and auto commit/push.
- **Milestone 02B**: Import GLB into existing renderer, camera K05–K08, DOM copy, nav/scroll, responsive and browser QA; verify and auto commit/push.
- Follow `AGENTS.md` for safe push procedures. Verify remote SHA. Never claim visual approval based only on automated screenshot creation.
