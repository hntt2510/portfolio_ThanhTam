# Scene 03 V2 — Core Expertise | Camera and Scroll Ledger V2

> **Approved 03A preflight correction (2026-11-04):** The live Scene 02 K08 uses **FOV 48° desktop / 50° mobile**, confirmed in `src/camera-controller.js` at the time of the 03A handoff. Older V2 camera tables mistakenly listed 46° / 48°. The scene model and camera preview MUST preserve live K08 framing. Do not edit Scene 01/02 runtime camera code in Milestone 03A. The K09+ values are provisional and must be tested at 03B. A small chord-angle difference does not mathematically establish C1 continuity.\n\n## 1. Unified Spatial Trajectory (K08 → K12)

Milestone 03 V2 maintains the single persistent Three.js world, extending the continuous camera path from Scene 02 K08 without scene resets, teleportation, or canvas reloads:

```
[Scene 01: Atrium]      [Scene 02: Gallery]         [Scene 03 V2: Expertise in Motion]
K01 ──► K02 ──► K03 ──► K04 ──► K05 ──► K06 ──► K07 ──► K08 ──► K09 ──► K10 ──► K11 ──► K12
                                                        ▲
                                              Physical Portal Seam
```

---

## 2. Mathematical Waypoint Ledger V2

All coordinates use metric units ($1.0 = 1\text{ meter}$).

- **Three.js Convention:** $X$ = Right/East, $Y$ = Up, $Z$ = South/Toward Viewer (Negative $Z$ = North/Forward).
- **Blender Convention:** $X$ = East, $Y$ = North, $Z$ = Up. Mapped by $X_{\text{Three}} = X_{\text{Blend}}$, $Y_{\text{Three}} = Z_{\text{Blend}}$, $Z_{\text{Three}} = -Y_{\text{Blend}}$.

### 2.1 Desktop Camera Ledger (16:9 Viewport, 1440 × 900)

| Waypoint | Narrative Beat | Three.js Position $(X, Y, Z)$ | Three.js Target $(X, Y, Z)$ | Blender Pos $(X, Y, Z)$ | Blender Tgt $(X, Y, Z)$ | FOV | Vantage Point Intent |
|---|---|---|---|---|---|:---:|---|
| **K08** | Anchor / Seam | `(36.53, 1.80, -21.62)` | `(43.24, 2.20, -19.98)` | `(36.53, 21.62, 1.80)` | `(43.24, 19.98, 2.20)` | $48.0^\circ$ | Frames the daylit arched portal exit of Profile Gallery. |
| **K09** | **Volumetric Reveal** | `(44.50, 1.85, -19.40)` | `(55.80, 3.80, -14.10)` | `(44.50, 19.40, 1.85)` | `(55.80, 14.10, 3.80)` | $52.0^\circ$ | Enters pavilion threshold; camera tilts up slightly revealing the soaring 10.5m sawtooth ceiling. |
| **K10** | **Process Paths (BA)** | `(49.50, 3.20, -14.20)` | `(57.80, 0.20, -10.30)` | `(49.50, 14.20, 3.20)` | `(57.80, 10.30, 0.20)` | $46.0^\circ$ | **Elevated oblique view** ($Y=3.2\text{m}$, pitch $-22^\circ$) overlooking basalt floor pathways branching from As-Is to To-Be. |
| **K11** | **System Spine (SAP)** | `(56.80, 1.85, -11.20)` | `(58.50, 2.20, -4.50)` | `(56.80, 11.20, 1.85)` | `(58.50, 4.50, 2.20)` | $48.0^\circ$ | **Side-tracking parallax view**; camera glides past the 3-tier modular structural matrix of aluminum & glass. |
| **K12** | **Solution Bridge (SC)**| `(63.20, 4.05, -8.20)` | `(75.00, 4.20, -2.80)` | `(63.20, 8.20, 4.05)` | `(75.00, 2.80, 4.20)` | $50.0^\circ$ | **Elevated forward bridge glide** ($Y=4.05\text{m}$ eye level above bridge deck); direct sightline into Scene 04 portal. |

### 2.2 Mobile Camera Ledger (Portrait Viewport, 390 × 844)

| Waypoint | Mobile Position $(X, Y, Z)$ | Mobile Target $(X, Y, Z)$ | Mobile FOV | Headroom Intent |
|---|---|---|:---:|---|
| **K08** | `(36.53, 1.88, -21.62)` | `(43.24, 2.20, -19.98)` | $50.0^\circ$ | Stable archway framing with bottom text room |
| **K09** | `(44.20, 1.90, -19.20)` | `(55.80, 4.00, -14.10)` | $54.0^\circ$ | Captures tall sawtooth roof apex |
| **K10** | `(49.20, 3.30, -14.00)` | `(57.80, 0.20, -10.30)` | $48.0^\circ$ | High-angle floor visibility above bottom banner |
| **K11** | `(56.50, 1.90, -11.00)` | `(58.50, 2.30, -4.50)` | $50.0^\circ$ | Structural matrix fills upper 60% of frame |
| **K12** | `(62.80, 4.10, -8.00)` | `(75.00, 4.30, -2.80)` | $52.0^\circ$ | Forward portal framing centered in upper viewport |

---

## 3. Continuity Across the K08 Seam

- **$C_0$ Continuity:**
  $\mathbf{P}_{\text{K08}} = (36.53, 1.80, -21.62)$, $\mathbf{T}_{\text{K08}} = (43.24, 2.20, -19.98)$, $\text{FOV}_{\text{K08, desktop}} = 48.0^\circ,\quad \text{FOV}_{\text{K08, mobile}} = 50.0^\circ$.
- **$C_1$ Tangent Continuity:**
  Corridor tangent vector at K08 exit is $(0.9063, 0.00, 0.4226)$. The chord vector to K09 is $(44.50 - 36.53, 1.85 - 1.80, -19.40 - (-21.62)) = (7.97, 0.05, 2.22)$, which yields horizontal angle deflection $< 4.8^\circ$. This establishes only a small planned chord deflection, not exact C1 continuity. Actual K08→K09 camera position, view-direction and FOV derivatives must be checked after 03B integration using finite differences and browser footage.

---

## 4. Scroll Progression Schedule

| Beat | Scene 03 Local $p_{\text{local}}$ | Camera Motion | Metaphor & Installation | Editorial UI Mode |
|---|:---:|---|---|---|
| **K09 Reveal** | $0.00 \to 0.22$ | Through portal into threshold | Volumetric scale shift | Center-Left Hero |
| **K10 Business Analysis** | $0.22 \to 0.48$ | Elevated rise ($Y=3.2\text{m}$, tilt $-22^\circ$) | Branching process floor lines | Bottom-Left Banner |
| **K11 SAP / Enterprise** | $0.48 \to 0.74$ | Side-tracking dolly | Modular System Spine matrix | Split Column |
| **K12 Solution Consulting**| $0.74 \to 1.00$ | Ascending bridge glide ($Y=4.05\text{m}$) | Suspended bridge & portal | Centered Gateway |

Reversible algebraic scrubbing drives camera and typography without CSS animation delay. Native scroll wheel and touch drag remain authoritative.