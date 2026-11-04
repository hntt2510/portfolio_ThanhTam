# Milestone 03 — Design Review: REVISE, NOT APPROVED

**Date:** 2026-11-04  
**Baseline package:** `eefc3a4f69323c5e761ad9a9c15727e9e670dfcc`  
**Owner feedback:** "thấy giao diện chả khác j" — the user finds the interface and experience insufficiently differentiated from earlier chapters.

## Finding

The current Scene 03 "Expertise Rotunda" repeats the existing presentation template: circular/curved white gallery, large skylight, text in a fixed 42%-left unboxed column, vertical nav on right, four headings cross-fading with camera travel. Scene 01 is also a circular atrium and Scene 02 also a curved gallery. This creates stylistic continuity at the expense of **scene identity and visual storytelling**.

The documents using the word "Approved" (for example `01-DESIGN-SPEC.md`) reflect an agent-authored title, **not the owner's approval**. Scene 03 design has not been approved, and no Scene 03 production geometry or code should be built.

## Required change: V2 experience concept

Do not just improve PBR materials or change the headline and four camera positions. First redesign the *scrollytelling experience* so Scene 03 feels unmistakably different in architecture, spatial choreography, interaction rhythm and responsive on-screen editorial layouts, while still belonging to the Glass & Light Museum.

A suitable starting proposal to explore, **not pre-approved**, is **Expertise in Motion — a sequence of three spatial metaphors**:

1. **K09 — Threshold & Reveal:** A compressed transitional vestibule opens into an unexpectedly broad **asymmetric** daylight gallery. Camera reveal uses an intentional change of spatial scale. Do not repeat a circular rotunda with a central oculus.
2. **K10 — Business Analysis / Process Lines:** Camera makes a gentle elevated/oblique view along a purpose-built architectural floor pathway / branching physical routes suggesting As-Is → To-Be analysis. Purely visual physical geometry; no words or data panels mapped onto meshes.
3. **K11 — SAP / Enterprise Systems / System Spine:** A distinct, readable architectural installation made of connected modular frames / refined aluminum and translucent-glass volumes, suggesting an integrated enterprise system. Track sideways past it to reveal parallax. No sci-fi neon/wireframe, no 3D info cards.
4. **K12 — Solution Consulting / Bridge to Execution:** Camera moves forward along a physical connecting bridge/threshold from diverging paths toward the Scene 04 Projects wing, giving a genuine destination and shift in viewpoint.

**Alternatives:** Produce at least three visual concepts with substantially different architectural grammar and camera choreography (not 3 renders of the same rotunda), then recommend one. The proposal above may be included as one candidate. Carry forward the exact K08 physical portal/camera anchor and existing scroll-world architecture.

## UI rules

- **Continue to show all skills/copy directly as semantic HTML/CSS on screen**, with absolutely no 3D textual panels.
- The fixed right-side scroll navigation and identity palette remain consistent, **but narrative placement/scale/hierarchy need not be identical in every beat**.
- Test distinct compositions for K09–K12: e.g. editorial large left reveal, small left side label with large bottom headline, split focal hierarchy, and a concluding bridge/transition layout. Do not hide important text under architecture or nav.
- Scroll is the single authority for camera and content; bidirectional, no autoplay or one-shot animation.
- Responsive/mobile text must be legible and free of boxed skill cards. No extra interactions required to understand the story.

## Mandatory design artifacts and approval gate

Deliver **real reference image files** in `design-handoff/milestone-03/visual-references/`:
- Three distinctly different candidate hero directions, with individual scene concept renders.
- Side-by-side contact sheet against actual **Scene 02 K07/K08 screenshot** to demonstrate *visible* differences in shape, point-of-view and composition.
- Four scene storyboard frames for the selected candidate, showing actual text on the UI, camera viewpoint and distinctive architecture per beat.
- Top-down path diagram showing physical seam from K08, spatial signature moments and next exit to Scene 04.
- Desktop and mobile editorial composition mockups.
- Distinctness checklist: silhouette, camera perspective, foreground/background hierarchy, content typography placement and motion change, all assessed against prior scenes.

Do not fabricate image deliverables. If suitable image generation/render tooling is unavailable, report limitation and stop rather than making a text-only board.

### Acceptance

A viewer should distinguish K10, K11 and K12 visually **without reading any headline**; Scene 03 should also be distinct from Scenes 01/02 at first glance. Maintain a bright contemporary museum aesthetic with warm white, brushed silver, light stone and ice blue accents, but avoid repetitive white curved corridor/oculus imagery. Do not reuse the same left-text/static-camera-follow template for all beats.

### Implementation boundary & publication

This is **Milestone 03 Design V2** only. No Blender production GLB, no runtime Three.js changes. Do not code until owner approves a new visual board. Commit the revised design package and real image references; auto-push to GitHub as in `AGENTS.md`, report verified remote SHA. Update `PROJECT_STATUS.md` as "V1 rejected, V2 design review pending", not "approved".
