# Scene 03 — Core Expertise | Camera and Scroll Ledger

## 1. Unified Spatial Trajectory (K08 → K12)

Milestone 03 extends the continuous single-world camera path of the Project Museum without resetting, jumping, or reloading WebGL canvases:

```
[Scene 01: Atrium]        [Scene 02: Gallery]            [Scene 03: Expertise Rotunda]
K01 ──► K02 ──► K03 ──► K04 ──► K05 ──► K06 ──► K07 ──► K08 ──► K09 ──► K10 ──► K11 ──► K12
                                                         ▲
                                               Physical Seam Portal
```

---

## 2. Mathematical Waypoint Specifications

All coordinates use metric units ($1.0 = 1\text{ meter}$).

- **Three.js Convention:** $X$ = Right/East, $Y$ = Up, $Z$ = South/Toward Viewer (Negative $Z$ = North/Forward).
- **Blender Convention:** $X$ = East, $Y$ = North, $Z$ = Up. Mapped by $X_{\text{Three}} = X_{\text{Blend}}$, $Y_{\text{Three}} = Z_{\text{Blend}}$, $Z_{\text{Three}} = -Y_{\text{Blend}}$.

### 2.1 Desktop Camera Ledger (16:9 Viewport, 1440 × 900)

| Waypoint | Narrative Beat | Three.js Position $(X, Y, Z)$ | Three.js Target $(X, Y, Z)$ | Blender Pos $(X, Y, Z)$ | Blender Tgt $(X, Y, Z)$ | Desktop FOV | Look Distance |
|---|---|---|---|---|---|:---:|:---:|
| **K08** | Perspective / Exit | `(36.53, 1.80, -21.62)` | `(43.24, 2.20, -19.98)` | `(36.53, 21.62, 1.80)` | `(43.24, 19.98, 2.20)` | $46.0^\circ$ | $6.92\text{m}$ |
| **K09** | Entrance to Expertise | `(48.60, 1.85, -17.48)` | `(58.00, 2.20, -13.00)` | `(48.60, 17.48, 1.85)` | `(58.00, 13.00, 2.20)` | $48.0^\circ$ | $10.42\text{m}$ |
| **K10** | Business Analysis | `(53.80, 1.85, -14.60)` | `(60.50, 2.10, -10.20)` | `(53.80, 14.60, 1.85)` | `(60.50, 10.20, 2.10)` | $46.0^\circ$ | $8.07\text{m}$ |
| **K11** | SAP / Enterprise Systems| `(59.60, 1.85, -11.40)` | `(66.80, 2.10, -7.50)` | `(59.60, 11.40, 1.85)` | `(66.80, 7.50, 2.10)` | $46.0^\circ$ | $8.20\text{m}$ |
| **K12** | Solution Consulting | `(65.40, 1.85, -8.00)` | `(73.20, 2.20, -4.20)` | `(65.40, 8.00, 1.85)` | `(73.20, 4.20, 2.20)` | $48.0^\circ$ | $8.72\text{m}$ |

### 2.2 Mobile Camera Ledger (Portrait Viewport, 390 × 844)

Mobile framing adjusts camera position slightly inward ($+0.4\text{m}$ clearance) and increases vertical FOV by $+2.0^\circ$ to maintain balanced architectural headroom:

| Waypoint | Mobile Position $(X, Y, Z)$ | Mobile Target $(X, Y, Z)$ | Mobile FOV | Headroom Intent |
|---|---|---|:---:|---|
| **K08** | `(36.53, 1.88, -21.62)` | `(43.24, 2.20, -19.98)` | $48.0^\circ$ | Frame arched portal with lower text clearance |
| **K09** | `(48.20, 1.90, -17.30)` | `(58.00, 2.30, -13.00)` | $50.0^\circ$ | Reveal dome skylight above bottom text |
| **K10** | `(53.40, 1.90, -14.40)` | `(60.50, 2.20, -10.20)` | $48.0^\circ$ | Clear upper architectural alcove |
| **K11** | `(59.20, 1.90, -11.20)` | `(66.80, 2.20, -7.50)` | $48.0^\circ$ | Rhythmic vertical fins in upper 55% |
| **K12** | `(65.00, 1.90, -7.80)` | `(73.20, 2.30, -4.20)` | $50.0^\circ$ | Grand exit archway framed toward top |

---

## 3. Continuity & Spline Mechanics (K08 → K09 Seam)

### 3.1 C0 Continuity (Zero Positional / Target Pop)
- The trajectory endpoint of Scene 02 is mathematically identical to the initial anchor of Scene 03:
  $$\mathbf{P}_{\text{Scene02}}(p = 1.0) = \mathbf{P}_{\text{Scene03}}(p_{\text{local}} = 0.0) = (36.53, 1.80, -21.62)$$
  $$\mathbf{T}_{\text{Scene02}}(p = 1.0) = \mathbf{T}_{\text{Scene03}}(p_{\text{local}} = 0.0) = (43.24, 2.20, -19.98)$$
  $$\text{FOV}_{\text{Scene02}}(p = 1.0) = \text{FOV}_{\text{Scene03}}(p_{\text{local}} = 0.0) = 46.0^\circ$$

### 3.2 C1 Continuity (Smooth Velocity & Tangent Direction)
- At K08, the incoming corridor tangent vector is $\mathbf{v}_{\text{in}} = (0.9063, 0.0, 0.4226)$.
- The chord vector from K08 to K09 is:
  $$\mathbf{\Delta P} = (48.60 - 36.53, 1.85 - 1.80, -17.48 - (-21.62)) = (12.07, 0.05, 4.14)$$
  Normalized horizontal direction:
  $$\mathbf{\hat{v}}_{\text{chord}} = \frac{(12.07, 4.14)}{\sqrt{12.07^2 + 4.14^2}} = \frac{(12.07, 4.14)}{12.76} = (0.946, 0.324)$$
  Angular deflection between $\mathbf{v}_{\text{in}}$ and $\mathbf{\hat{v}}_{\text{chord}}$ is only $5.2^\circ$, ensuring a velvety smooth, natural glide through the arched portal with zero jerk or abrupt steering.

---

## 4. Chapter-Local Scroll Progression Schedule

When Milestone 03B is implemented, the centralized chapter schedule in `app.js` will map global scroll progress $p \in [0, 1]$ into Scene 03 local progress $p_{\text{local}} \in [0, 1]$:

| Chapter Beat | Scene 03 Local $p_{\text{local}}$ | Camera Intent | Narrative Copy | Active Nav Indicator |
|---|:---:|---|---|:---:|
| **K09 Entrance** | $0.00 \to 0.22$ | Step through portal into grand Rotunda | *Where Business Meets Technology.* | `03 Expertise` |
| **K10 Business Analysis** | $0.22 \to 0.48$ | Glide along inner curve framing BA Alcove | *Understanding Problems Before Building Solutions.* | `03 Expertise` |
| **K11 SAP / Enterprise** | $0.48 \to 0.74$ | Track along Colonnade under Oculus | *Understanding Enterprise Systems.* | `03 Expertise` |
| **K12 Solution Consulting**| $0.74 \to 1.00$ | Approach grand exit portal to Exhibition | *Turning Business Requirements into Practical Solutions.* | `03 Expertise` |

### 4.1 Algebraic Beat Blending Formula
Each narrative beat $i \in \{0, 1, 2, 3\}$ uses pure algebraic interpolation:
- Lead-in fade: $t \in [p_{\text{start}}, p_{\text{endIn}}] \implies \text{opacity} = \frac{p - p_{\text{start}}}{p_{\text{endIn}} - p_{\text{start}}}$, $\Delta Y = 12(1 - t)\text{px}$
- Settled state: $t \in [p_{\text{endIn}}, p_{\text{startOut}}] \implies \text{opacity} = 1.0$, $\Delta Y = 0\text{px}$
- Lead-out fade: $t \in [p_{\text{startOut}}, p_{\text{end}}] \implies \text{opacity} = 1.0 - \frac{p - p_{\text{startOut}}}{p_{\text{end}} - p_{\text{startOut}}}$, $\Delta Y = -12(t)\text{px}$

This formula guarantees 100% reversible scrubbing without CSS transition lag.

---

## 5. Collision Avoidance & Safety Envelopes

- **Floor Clearance:** Eye level maintained strictly at $Y = 1.85\text{m}$ ($1.90\text{m}$ on mobile), giving $1.85\text{m}$ vertical clearance above the travertine surface ($Y = 0.00\text{m}$).
- **Wall Clearance:** Minimum distance from any perimeter plaster wall is $2.40\text{m}$.
- **Colonnade Clearance:** Camera path tracks $2.10\text{m}$ clear of the inner face of the brushed aluminum fins.
- **Oculus / Ceiling Clearance:** Highest point of the rotunda ceiling is $Y = 8.20\text{m}$, ensuring $> 6.3\text{m}$ headroom above the camera.
- **Near Clipping Plane:** Three.js camera near plane set to $0.10\text{m}$ ($10\text{cm}$), precluding geometry clipping even during extreme viewport aspect ratios.

---

## 6. Accessibility & Reduced Motion

- **Native Scroll Support:** Native wheel, trackpad, and touch drag events drive progress; zero scroll hijacking.
- **`prefers-reduced-motion` Compliance:** When reduced motion is active, $\Delta Y$ translation is clamped to $0$, and copy transitions occur via smooth linear opacity cross-fades only.
- **Screen Reader Navigation:** Narrative beats use semantic `<article>` tags with `aria-live="polite"` and programmatic focus management.