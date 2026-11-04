# Project Museum · Scene 02 Profile Gallery — Antigravity Handoff V2

**Approved design:** 2026-11-04.  **Portfolio owner:** **Hoàng Nguyễn Thành Tâm** (ASCII slug: `Hoang-Nguyen-Thanh-Tam`).

## IMPORTANT — changed direction after Visual Board V1

**The glass panels containing Foundation / Experience / Perspective text in V1 are REJECTED.** Scene 02 must be **one continuous architectural gallery**, not a card carousel or an object-label exhibition. All biographical text must be **real HTML/CSS interface text**, overlaid independently of the 3D camera and tied to scroll progress. The screenshot/reference board is concept art, not geometry, and any inadvertent lettering/signage in the photograph must NOT become physical scene text.

Scene 01 (Entrance Atrium) already exists and must remain functional. The **K04 final pose** is the entry point for Scene 02. Do not reset or duplicate the Three.js world.

## Files in this package

- `visual-references/scene02-approved-visual-board-v2.png` — approved overall board, used for visual continuity and 4 beats.
- `visual-references/scene02-approved-corridor-and-UI.png` — approved opening composition.
- `visual-references/keyframe-K05...K08-visual-reference.png` — four cropped storyboard snapshots, for camera framing and UI state reference only.
- `specs/01-DESIGN-SPEC.md` — world style, architecture, overlays and negative design requirements.
- `specs/02-CAMERA-AND-SCROLL-LEDGER.md` — K04→K05 continuity; four states; global/local scroll mapping.
- `specs/03-CONTENT-COPY.md` — English UI copy with correct owner's name.
- `specs/04-BLENDER-ASSET-SPEC.md` — 3D modeling/GLB deliverable rules.
- `prompts/ANTIGRAVITY-IMPLEMENT-SCENE-02.md` — main build prompt.
- `qa/ACCEPTANCE-CHECKLIST.md` — verify before marking complete and pushing.

## How to hand over

1. Open the existing GitHub repo `hntt2510/portfolio_ThanhTam` in Antigravity and synchronize `main`.
2. Copy this folder into the repository as `design-handoff/milestone-02/`, retaining PNG images and Markdown files together. Use the repository's existing `AGENTS.md` and `PROJECT_STATUS.md` as binding project context.
3. Send the prompt in `prompts/ANTIGRAVITY-IMPLEMENT-SCENE-02.md` to Antigravity.
4. Have the agent complete **02A** Blender/GLB and publish its verified results, then **02B** runtime integration and browser QA and publish its verified results. Pushing does not need separate approval; do not force-push or expose secrets.
5. Review actual screenshots, including the K04→K05 transition, before considering Scene 02 visually accepted.

**No need to rebuild Scene 01 or re-theme the website.**
