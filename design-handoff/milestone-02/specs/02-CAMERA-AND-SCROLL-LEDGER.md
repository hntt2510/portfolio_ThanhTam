# Scene 02 — Camera and Scroll Ledger V2

## Existing runtime anchor
In committed Scene 01 (`src/camera-controller.js`), desktop K04 currently reports position `(4.80, 1.80, -4.80)`, look-at `(12.00, 1.80, -12.00)`, FOV `48°`. **Read current repo at runtime before modifying; coordinates are an existing-code reference, not an instruction to hardcode an incompatible target.** Mobile K04 uses same position/target and ~50° FOV. Scene 02 K05 must begin at the same world-space camera transform as K04 to prevent teleports.

## Timing architecture
The former `12–32%` *whole-site* progress examples are storyboard proportions only. Do not hard-code them while Scenes 03–06 do not exist. Implement a `globalScrollProgress -> chapter -> chapterLocalProgress` mapping derived from actual DOM chapter boundaries or a future-friendly centralized chapter schedule.

An example **Scene 02 local** beat schedule (adjust after graybox review):

| Beat | Local p | Camera intent | DOM content | Nav |
|---|---:|---|---|---|
| K05 Entry | 0.00 | Begin at **exactly** K04 end; smoothly pass through existing corridor into widening gallery | From Software Engineering to Enterprise Problem Solving. | 02 About |
| K06 Foundation | ~0.30 | Forward dolly beside floor-to-ceiling glazing; convey openness | Built on a Technical Foundation. | 02 About |
| K07 Experience | ~0.66 | Continue on mild curved path; reveal corridor depth without orbiting a single object | Turning Requirements into Solutions. | 02 About |
| K08 Perspective/Exit | 1.00 | Align toward eventual Expertise Room threshold; no fabricated Scene 03 geometry | Connecting Business & Technology. | 02 About until actual Scene 03 exists |

## Camera path handoff
- Preserve one persistent camera and the existing WebGL renderer.
- Preserve K01–K04 shots as closely as possible; K04→K05 must be C0/C1 continuous to avoid snap in position, orientation or FOV.
- Model the new corridor in Blender/GLB **in the same coordinate frame** as the existing atrium asset. If topology demands an offset, derive and document it, never manually guess camera positions against uninspected geometry.
- Maintain collision-free camera path through walls/floors/railings; test wide and portrait FOV.
- Separate exact scroll state for DOM/nav from eased camera display state; UI must never report the wrong chapter due to camera lag.
- Transition state must be reversible, including fast wheel input, drag scrollbar, navigation clicks and reload halfway through.

## Text animation
- 4 narrative states are DOM layers, not assets: fade/translateY as a small, short scroll interval around each beat, but avoid blank text for extended intervals.
- At any settled scroll position exactly one message is primarily readable. Keyboard and screen-reader order remain sane.
- The About heading and visual chapter indication remain legible during swaps.

## Handoff to Scene 03
- At K08, terminate facing a plausible bright architectural opening; Scene 03 is not built yet. The camera must stop cleanly.
- Navigation may display Expertise as upcoming/disabled until implementation, as in Scene 01.
