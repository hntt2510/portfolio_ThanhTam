# Scene 02 — Profile Gallery | Approved Visual & UI Specification V2

## Objective
The viewer has entered the Project Museum through Entrance Atrium and now walks through a light-filled, gently curved architectural corridor. Scrolling moves a real 3D camera. The portfolio owner's professional story is presented as **dynamic, readable, screen-fixed HTML copy** that transitions through four narrative beats.

## Owner identity
Full Vietnamese name: **Hoàng Nguyễn Thành Tâm**. Exact proper accents must appear in the visible owner-name field where technically supported. ASCII slug: `Hoang-Nguyen-Thanh-Tam`. Do NOT use a different person or placeholder contact data.

## Approved architectural design
- A single, wide **curved gallery corridor** that physically connects to the **north-east exit passage** at Scene 01 K04.
- White/ivory matte plaster interior wall with subtle rounded transitions and shallow coves (right side in preferred hero framing).
- Tall floor-to-ceiling clear glazing along the exterior curve, with **slim brushed-silver mullions**; natural greenery and daylight outside, designed as restrained atmosphere, not interactive targets.
- Pale stone/light limestone floor, low specular response and **soft** sun/shadow gradients, not mirror reflections.
- Gentle ceiling cove strips in warm-neutral white. Furnishing only if needed: small minimal seating / architecture-compatible ledges, sparingly.
- Visual materials same as Scene 01: warm white `#F7F8F6`, silver `#E8EBED`, ice blue `#D7E8F6`, steel blue `#6F9EC8`, graphite `#263640`.

## Rejected (critical)
- NO standing frosted-glass panels labeled Foundation/Experience/Perspective.
- NO 3D text, wall titles, plaques, UI cards, 3D headings, or storytelling information painted onto corridor objects.
- NO three boxed content cards arranged across the page.
- NO camera teleport or independent Scene 02 canvas/renderer.
- NO navy/dark/cyberpunk ambience, oversaturated glow, excessive glass reflection, particle effects, or rotating gallery objects.
- Concept images may contain incidental environment signage: **do not reproduce** it as geometry or texture.

## UI architecture
- An unobstructed, left-aligned **editorial DOM overlay**, width constrained for readable line lengths; not a bordered card. Use subtle white gradient/mask only to protect contrast against changing background.
- Four copy states: K05 Introduction to Journey; K06 Foundation; K07 Experience; K08 Perspective. Content and typography in `03-CONTENT-COPY.md`.
- Right side keeps the existing fixed vertical navigation, with **02 About** active throughout this chapter; Intro active before Scene 02 and Expertise only once that future scene actually exists.
- The left content must not move in 3D space or be rendered to a glass-texture canvas.
- On desktop, gallery remains visible through center-right; on mobile, place text in a stable lower/side overlay and keep enough scene visible without truncating content.
- The existing branding, typography (Manrope/Inter/IBM Plex Mono), blue accent, and general design tokens are inherited.

## Scroll/UI motion
- Scroll sets a deterministic global progress; chapter-specific progress is derived from the About chapter range.
- Smoothly interpolate camera, FOV, and look-at along the corridor; no forced camera spin.
- Update copy at beat boundaries with subtle opacity/translateY, continuously and reversibly driven by scroll, not one-shot animations that cannot rewind.
- Scrolling backward must restore exactly the previous content and camera state.
- Native wheel/touch scrolling remains available; no scroll hijack.
- A readable reduced-motion alternative must expose the same information.

## Scope
- Scene 02 and the minimum adjustments required to connect it to Scene 01.
- No building Scene 03 Expertise or adding arbitrary case studies.
- May extend scroll/navigation orchestration to a reusable chapter model, but preserve current behavior and existing K01–K04 visual intent.

## Reference priority
1. This approved V2 specification / owner clarification.
2. Existing Scene 01 project code and K04 position / camera path.
3. Approved V2 concept PNG and camera-board crops for framing/material mood.
4. Earlier scene 02 V1 references only for architectural feel, **never** for informational glass panels.
