# Scene 03 V2 — Core Expertise | Approved Design Specification V2

## 1. Executive Summary & Identity

- **Project:** Project Museum — Personal Professional Portfolio
- **Portfolio Owner:** **Hoàng Nguyễn Thành Tâm**
- **ASCII / URLs / Filenames:** Hoang Nguyen Thanh Tam / `Hoang-Nguyen-Thanh-Tam`
- **Milestone:** Milestone 03 V2 — Visual Experience Redesign (Expertise in Motion)
- **Status:** **Design Package Complete · Pending Portfolio Owner Visual Review**
- **Scope Boundary:** **DESIGN ONLY**. Architectural concept, visual boards, camera ledger, content copy, asset specifications, and verification checklist. No WebGL code, GLB meshes, or camera implementation in this milestone.

---

## 2. Problem Statement & The V2 Redesign

### 2.1 Why Milestone 03 V1 Was Not Approved
The previous Milestone 03 V1 proposed the "Expertise Rotunda" — a white circular room with a central oculus skylight, fixed 42%-left unboxed text, and ground-level camera tracking. As noted in owner review `REVIEW-V1-NOT-APPROVED.md`:
- Scene 01 was a circular atrium with skylight and left text.
- Scene 02 was a curved gallery corridor with skylight/glazing and left text.
- Scene 03 V1 repeated the exact same circular geometry, flat eye-level perspective, and static left-aligned text column, resulting in stylistic monotony without scene identity.

### 2.2 V2 Solution: "Expertise in Motion"
Scene 03 V2 discards the circular rotunda entirely in favor of an **expansive, asymmetrical daylight pavilion** featuring **three distinct physical spatial metaphors**:

```
[From Scene 02 K08]
       │
       ▼
 ┌───────────────┐
 │ K09: REVEAL   │  Compressed portal expands into 10.5m-high asymmetric pavilion
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ K10: BA PATHS │  Elevated oblique view (Z=3.2m) overlooking branching As-Is -> To-Be stone lines
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ K11: SAP SPINE│  Side-tracking past monumental 3-tier modular structural matrix of aluminum/glass
 └───────┬───────┘
         ▼
 ┌───────────────┐
 │ K12: SC BRIDGE│  Ascending onto suspended bridge (Z=2.4m) crossing open air toward Scene 04 portal
 └───────────────┘
```

---

## 3. Architectural Grammar & Dimensions

### 3.1 Spatial Dimensions
- **Footprint:** Length $36.0\text{m}$, Width $18.0\text{m}$ (over $3.5\times$ wider than the Scene 02 corridor).
- **Asymmetric Verticality:** Sloped sawtooth roof rising from $6.20\text{m}$ on the south wall to $10.50\text{m}$ on the north wall.
- **North Sawtooth Clerestories:** Four angled ceiling baffles with vertical north-facing clerestory glass apertures admitting pure, diffused natural daylight ($6500\text{K}$) without glare or harsh hotspots.

### 3.2 Seam Connection to Scene 02 K08
- **Physical Anchor Point:**
  - Three.js coordinates: $(43.24, 0.00, -19.98)$
  - Blender coordinates: $(43.24, 19.98, 0.00)$
  - Tangent Vector: $(\cos(-25^\circ), -\sin(-25^\circ)) = (0.9063, 0.4226)$ in Three.js horizontal plane.
- The compressed entrance vestibule from K08 empties directly into the south-west corner of the asymmetric pavilion, producing an immediate, dramatic volumetric scale shift.

---

## 4. The Three Spatial Metaphors for Competencies

Rather than generic wall niches, each professional competency is represented by a physical architectural feature in 3D space:

### 4.1 Zone A: Business Analysis — Branching Process Pathways (Framed at K10)
- **Concept:** Inquiry, process modeling, and As-Is $\to$ To-Be discovery.
- **Physical Geometry:** Inlaid dark basalt stone and brushed silver metal lines embedded into the light travertine floor. The main spine physically branches into multiple exploratory lines before converging toward execution.
- **Camera Vantage:** Elevated oblique camera angle ($Z = 3.20\text{m}$, downward tilt $-22^\circ$) looking across the floor pathways.
- **UI Composition:** Horizontal bottom-left editorial banner with interactive milestone tags, preserving the upper 65% of the screen for the architectural floor view.

### 4.2 Zone B: SAP / Enterprise Systems — The Modular System Spine (Framed at K11)
- **Concept:** Enterprise data architecture, modularity, robustness, and integration.
- **Physical Geometry:** A monumental 3-tier modular structural matrix ($4\text{ bays long} \times 2\text{ bays deep} \times 3\text{ tiers high}$) constructed from precision $8\text{cm}$ brushed-silver aluminum frames and glowing frosted-glass volumes.
- **Camera Vantage:** Eye-level side-tracking shot past the installation, generating rich multi-layer parallax between the foreground aluminum grid, interior frosted cubes, and background sawtooth daylight.
- **UI Composition:** Split-column layout (compact 34% left typography column, leaving 66% of the screen completely clear for the structural matrix).

### 4.3 Zone C: Solution Consulting — The Suspended Bridge (Framed at K12)
- **Concept:** Synthesis, connecting business needs to technical reality, and crossing into project execution.
- **Physical Geometry:** A physical suspended pedestrian bridge ($L = 14.0\text{m}$, $W = 3.2\text{m}$, elevated at $Z = 2.40\text{m}$) with cantilevered clear glass balustrades spanning across the open volume directly toward the grand portal into Scene 04 (Project Exhibition).
- **Camera Vantage:** Elevated bridge glide along the bridge deck ($Z = 4.05\text{m}$ eye level), looking straight through the grand portal.
- **UI Composition:** Symmetrical gateway composition with central-anchored typography framing the forward threshold.

---

## 5. UI Architecture & Anti-Patterns

### 5.1 Strict Anti-Patterns
- ❌ **NO 3D skill cards or info panels** mounted on walls, floors, or floating in space.
- ❌ **NO static 42%-left text column across all beats** (eliminated in V2).
- ❌ **NO generic 3-card SaaS website blocks**.
- ❌ **NO dark navy or cyberpunk neon colors**.

### 5.2 Adaptive Editorial DOM Overlays
Each narrative beat features a bespoke editorial layout tailored to its spatial moment:
1. **K09 Reveal:** Large center-left hero typography with expansive negative space.
2. **K10 Process Paths:** Bottom-left horizontal banner with process tags.
3. **K11 System Spine:** Split column with compact left typography and broad right visual field.
4. **K12 Bridge:** Centered gateway composition leading into Scene 04.

---

## 6. Acceptance Test Verification

> **Acceptance Test:** If the headlines are hidden, a viewer must still be able to distinguish K10, K11, and K12 visually and recognize that Scene 03 is different from Scenes 01 and 02.

- **K10 vs K11 vs K12:**
  - K10 is instantly recognizable by its **high-angle elevated perspective** overlooking dark basalt process lines branching on the floor.
  - K11 is instantly recognizable by its **monumental modular aluminum/glass structural matrix** dominating the view.
  - K12 is instantly recognizable by its **elevated suspended bridge perspective** looking straight across open space into the Scene 04 portal.
- **Scene 03 vs Scene 01/02:**
  - Scene 01 is a symmetrical circular atrium with flat ground.
  - Scene 02 is a curved 5.2m-wide corridor with flat ceiling and botanical trees outside.
  - Scene 03 V2 is an asymmetrical 18m-wide hall with a 10.5m soaring sawtooth roof, multi-level elevations ($Z=0\text{m} \to 2.4\text{m} \to 3.2\text{m}$), and a physical 3D structural installation.
  - **Result: 100% Visually Distinguishable.**

---

## 7. Review Status

- **Status:** **DESIGN V2 READY FOR PORTFOLIO OWNER VISUAL REVIEW**
- **Next Milestone:** Milestone 03A (Blender Asset Production & GLB Export) only after portfolio owner explicitly approves this V2 design package.