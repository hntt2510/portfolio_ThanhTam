# Scene 02 — Acceptance Checklist V2

## Architecture & continuity
- [ ] Existing Scene 01 remains visually/functionally intact, including K01–K04.
- [ ] Gallery grows naturally from K04 passage with contiguous floor/wall geometry.
- [ ] Curved white gallery, tall windows, natural daylight and muted stone/silver material language.
- [ ] No three glass information plaques, 3D headline textures, signage, or physical info cards.
- [ ] Blender asset, GLB, source generator (if applicable) and proof renders committed.

## UI, content & scroll
- [ ] Correct owner name: **Hoàng Nguyễn Thành Tâm**.
- [ ] About information appears directly in HTML/CSS overlay, never in the 3D mesh.
- [ ] K05/K06/K07/K08 each has its own correct headline, body copy and corresponding camera framing.
- [ ] Right nav correctly highlights `02 About`; only already-built sections are clickable.
- [ ] Continuity from Scene 01 K04 to Scene 02 K05: no pop, teleport, or FOV snap.
- [ ] Forward/reverse/fast/drag/reload-midpage scroll works; content and camera stay synchronized.
- [ ] Proper responsive composition at desktop 1440×900 and mobile 390×844; no clipping/horizontal overflow.
- [ ] WCAG-friendly text contrast, keyboard navigation and reduced-motion fallback.

## Technical evidence
- [ ] GLB loaded in same persistent world / renderer (no second renderer).
- [ ] Existing import maps and vendor Three.js dependencies stay compatible.
- [ ] Agent actually starts server, loads GLB and runs browser tests; screenshots K04, K05, K06, K07, K08, mobile and reverse scroll are saved.
- [ ] Script checks image comparison or geometry/camera state after reverse scroll; do not call screenshots alone 'pixel-identical'.
- [ ] Console/network errors counted and explicitly reported; log failures rather than claiming PASS.
- [ ] Resource disposal/load lifetime and lower-power devices considered.
- [ ] `PROJECT_STATUS.md` contains real results, unresolved risks and next steps.
- [ ] Both verified 02A and 02B results **automatically committed and pushed**; record remote SHAs.

**Visual approval remains separate from agent-reported PASS:** user/creative review of screenshots is required before treating the aesthetic as final.
