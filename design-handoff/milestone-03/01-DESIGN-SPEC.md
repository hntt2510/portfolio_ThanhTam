# Scene 03 — Core Expertise | Approved Design Specification

## 1. Executive Summary & Identity

- **Project:** Project Museum — Personal Professional Portfolio
- **Portfolio Owner:** **Hoàng Nguyễn Thành Tâm**
- **ASCII / URLs / Filenames:** Hoang Nguyen Thanh Tam / `Hoang-Nguyen-Thanh-Tam`
- **Milestone:** Milestone 03 — Core Expertise Design & Visual Planning
- **Scope Boundary:** **DESIGN ONLY**. Architectural concept, visual boards, camera ledger, content copy, asset specifications, and verification checklist. No WebGL code, GLB meshes, or camera implementation in this milestone.

---

## 2. Architectural Concept: The Expertise Rotunda

Following the circular **Entrance Atrium** (Scene 01) and the curved daylit **Profile Gallery** (Scene 02), Scene 03 introduces the **Expertise Rotunda** — a bright, expansive circular hall designed to represent the convergence of three foundational capabilities:

1. **Business Analysis**
2. **SAP / Enterprise Systems**
3. **Solution Consulting**

### 2.1 Spatial Philosophy & Museum Identity
- **Glass & Light Museum Aesthetic:** Clean contemporary museum architecture inspired by Scandinavian and Swiss civic design (SANAA, David Chipperfield, Tadao Ando).
- **Spatial Progression:** The visitor transitions from the intimate, linear curve of the 5.2m-wide Profile Gallery corridor through the daylit threshold portal into a grand, 24m-diameter circular rotunda.
- **Natural Light as Narrative:** A soaring central circular skylight oculus ($R = 4.0\text{m}$, height $8.2\text{m}$) floods the interior with diffused natural zenith daylight, symbolizing clarity and synthesis.
- **Architectural Harmony:** Preserves the approved palette: warm-white plaster (`#F8F8F5`), polished light travertine (`#F4F2EC`), slim brushed-silver aluminum (`#EEF3F8`), and subtle ice-blue sky accents (`#D7E8F6`).
- **Strictly Prohibited:** No dark navy walls, cyberpunk lighting, neon accents, floating sci-fi geometry, or oversaturated bloom.

---

## 3. Physical Seam & Coordinate Reconciliation

Scene 03 physically adjoins the Scene 02 exit threshold without seams, floating gaps, or camera jumps.

### 3.1 Seam Anchor Point
- **Scene 02 Exit Portal Anchor:**
  - Three.js coordinates: $(43.24, 0.00, -19.98)$
  - Blender coordinates: $(43.24, 19.98, 0.00)$
  - Portal Geometry: Semicircular arch ($W = 3.60\text{m}$, $H = 4.50\text{m}$) in `PRG_Portal_ArchedWall`
  - Corridor Tangent Vector: $(\cos(-25^\circ), -\sin(-25^\circ)) = (0.9063, 0.4226)$ in Three.js horizontal plane $(X, Z)$
  - Threshold Vestibule: Extends $4.20\text{m}$ along tangent to $(47.05, 0.00, -18.20)$

### 3.2 Rotunda Placement & Dimensions
- **Rotunda Center ($C_{\text{rot}}$):**
  - Three.js: $(58.00, 0.00, -13.00)$
  - Blender: $(58.00, 13.00, 0.00)$
  - Distance from vestibule mouth $(47.05, -18.20)$ to center: $12.12\text{m}$ along trajectory angle $\approx 25.4^\circ$.
- **Rotunda Radius ($R_{\text{rot}}$):** $12.00\text{m}$ (Diameter $24.00\text{m}$)
- **Clearance Height:**
  - Perimeter Wall Height: $6.80\text{m}$
  - Clerestory / Skylight Ring: $6.80\text{m} \to 8.20\text{m}$
  - Central Oculus Aperture: Radius $4.00\text{m}$ at $Z = 8.20\text{m}$
- **Floor Paving:** Continuous light travertine slabs with radial brushed-aluminum inlay joints radiating outward from the central oculus footprint at $15^\circ$ increments.

---

## 4. The Three Competency Zones

The rotunda perimeter is articulated into three distinct architectural zones, each providing contextual framing for one core competency:

```
                         [NORTH]
                  Zone B: SAP / Colonnade
                     (Clerestory Fins)
                           ▲
                           │
       Zone A: BA          │          Zone C: SC
       (Smooth Alcove)  ◄──┼──►  (Grand Exit Portal)
          [WEST]           │          [EAST]
                           ▼
                  Entrance Threshold
                 (From Scene 02 K08)
```

### 4.1 Zone A: Business Analysis Alcove (Framed at K10)
- **Concept:** Structure, clarity, and inquiry.
- **Architecture:** A deep curved wall niche ($W = 6.80\text{m}$, $D = 1.80\text{m}$, $H = 5.20\text{m}$) with soft perimeter reveal shadowlines, warm-white matte plaster finish, and an integrated minimal stone bench ledge.
- **Lighting:** Soft vertical wall-wash lighting from a concealed cove, illuminating the texture of the plaster without harsh hotspots.
- **Visual Composition:** Camera looks toward the alcove with generous negative space on the left screen for the editorial HTML overlay: *"Understanding Problems Before Building Solutions."*

### 4.2 Zone B: SAP / Enterprise Systems Colonnade (Framed at K11)
- **Concept:** Architecture, robust systems, and disciplined structure.
- **Architecture:** A curved colonnade featuring slim brushed-aluminum vertical fins ($4\text{cm} \times 12\text{cm}$ cross-section, $1.20\text{m}$ on center) fronting high floor-to-ceiling clerestory glass apertures.
- **Lighting:** Cool natural daylight filtering between the vertical fins, creating crisp, soft vertical shadow stripes across the travertine floor.
- **Visual Composition:** Camera tracks along the inner colonnade arc, revealing architectural rhythm in the upper right while maintaining an open, calm reading column on the left: *"Understanding Enterprise Systems."*

### 4.3 Zone C: Solution Consulting & Exit Threshold (Framed at K12)
- **Concept:** Synthesis, client bridge, and forward momentum.
- **Architecture:** A grand sculpted arched portal ($W = 4.00\text{m}$, $H = 5.00\text{m}$) framed by elegant flared plaster reveals, opening directly toward the future **Project Exhibition** wing (Scene 04).
- **Lighting:** Bright frontal daylight streaming into the portal from the forward wing, creating an inviting visual draw into the next chapter of the museum.
- **Visual Composition:** Left overlay states *"Turning Business Requirements into Practical Solutions,"* with the camera perfectly aligned along the threshold vector.

---

## 5. Critical UI Architecture & Anti-Patterns

### 5.1 Strictly Prohibited 3D Elements
- ❌ **NO 3D skill cards or information panels** placed on 3D meshes or floors.
- ❌ **NO text embedded into glass panels** or painted onto museum walls.
- ❌ **NO floating labels, icons, or badges** floating in 3D WebGL space.
- ❌ **NO three-card website layout** or generic SaaS feature blocks.
- ❌ **NO interactive 3D click targets** that compete with native scrolling.

### 5.2 Approved Unboxed Editorial DOM Overlay
- **Layer Separation:** 100% of narrative copy, competencies, and sub-themes reside in the semantic HTML/CSS DOM overlay (`#expertiseContent`).
- **Layout:** Left-aligned unboxed typography column ($480\text{px}$ desktop max width), positioned $80\text{px}$ from the left viewport edge.
- **Readability Protection:** Full-height unboxed subtle gradient wash (`rgba(255, 255, 255, 0.88) \to rgba(255, 255, 255, 0.0)`) on desktop; bottom-up gradient wash on mobile.
- **Motion:** Algebraic, reversible scroll scrubbing (`opacity` and `translateY` directly mapped to chapter-local scroll progress $p_{\text{local}}$). Zero CSS animation lag.
- **Navigation:** Fixed vertical navigation on the right edge dynamically highlights `03 Expertise` when $p_{\text{global}}$ is within Scene 03.

---

## 6. Technical & Performance Budget

| Parameter | Budget Target | Rationale |
|---|---|---|
| **GLB File Size** | $\le 1.50\text{ MB}$ | Fast network loading, zero pop-in |
| **Polygon Count** | $\le 8,500$ quads / 16,000 tris | Smooth 60 FPS on mobile devices |
| **Draw Calls** | $\le 14$ distinct meshes/materials | Minimizes WebGL driver overhead |
| **PBR Materials** | Max 6 shared materials | Plaster, Travertine, Brushed Al, Glass, Cove, Backdrop |
| **Texture Memory** | Procedural PBR preferred / $\le 2\text{ MB}$ textures | Keeps total mobile heap under $80\text{ MB}$ |
| **Camera FPS** | Solid 60 FPS (desktop) / 60 FPS (mobile) | Tested via requestAnimationFrame loop |

---

## 7. Delivery Status & Review Gates

- **Status:** **DESIGN SPECIFICATION COMPLETED** (Milestone 03).
- **Implementation Gate:** Geometry creation, Blender script generation, and Three.js runtime integration are strictly blocked until the portfolio owner reviews and approves this design package.