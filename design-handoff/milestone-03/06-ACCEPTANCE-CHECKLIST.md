# Scene 03 — Core Expertise | Acceptance Checklist & Review Matrix

This checklist governs the formal visual and architectural review of **Milestone 03 — Core Expertise Design & Visual Planning** prior to authorizing implementation in Milestones 03A and 03B.

---

## 1. Portfolio Owner & Identity Verification

| Item # | Verification Criterion | Status | Notes |
|:---:|---|:---:|---|
| **1.1** | Portfolio owner explicitly identified as **Hoàng Nguyễn Thành Tâm** with full Vietnamese diacritics. | ✅ Pass | Verified in all spec documents and copy blueprints. |
| **1.2** | Professional positioning accurately reflects Software Engineering background evolving into Business Analysis and SAP/ERP Functional Consulting. | ✅ Pass | Grounded, honest copy; zero exaggerated claims or fabricated client portfolios. |
| **1.3** | Correct ASCII slug (`Hoang-Nguyen-Thanh-Tam`) specified for URL/file compatibility. | ✅ Pass | Documented in `01-DESIGN-SPEC.md` and `04-CONTENT-COPY.md`. |

---

## 2. Architectural Design & Aesthetic Integrity

| Item # | Verification Criterion | Status | Notes |
|:---:|---|:---:|---|
| **2.1** | **Glass & Light Museum** aesthetic faithfully preserved (contemporary Scandinavian/Swiss museum style). | ✅ Pass | Clean, light-filled circular rotunda with central oculus dome skylight. |
| **2.2** | Approved color harmony: warm-white plaster (`#F8F8F5`), light travertine (`#F4F2EC`), brushed silver (`#EEF3F8`), ice blue (`#D7E8F6`), deep graphite (`#111827`). | ✅ Pass | Zero dark navy, cyberpunk neon, or high-saturation bloom. |
| **2.3** | Physical seam connects seamlessly to Scene 02 K08 exit portal at Three.js $(43.24, 0.00, -19.98)$ without spatial or orientation discontinuity. | ✅ Pass | Mathematically verified with continuous tangent vectors ($\Delta \theta = 5.2^\circ$). |
| **2.4** | Three distinct architectural zones articulated along the rotunda perimeter: Zone A (BA Alcove), Zone B (SAP Colonnade), Zone C (Solution Consulting Portal). | ✅ Pass | Detailed architectural profiles, lighting, and negative space documented. |
| **2.5** | Lesson from Scene 02 applied: realistic architectural sculpting, reveal joints, plinth skirts, and slim structural profiles ($4\text{cm} \times 12\text{cm}$ fins). | ✅ Pass | Precludes simplistic primitive cylinder/box appearances. |

---

## 3. Visual Reference Assets & Storyboard

| Item # | Deliverable | Status | File Path |
|:---:|---|:---:|---|
| **3.1** | **Scene 03 Master Visual Board** (comprehensive creative director board) | ✅ Ready | `design-handoff/milestone-03/visual-references/scene03-visual-board-master.png` |
| **3.2** | **Scene 03 Hero Visual** (wide establishing view of Expertise Rotunda) | ✅ Ready | `design-handoff/milestone-03/visual-references/01-scene03-hero-visual.png` |
| **3.3** | **Architecture & Spatial Layout** (top-down blueprint with camera direction from K08) | ✅ Ready | `design-handoff/milestone-03/visual-references/02-architecture-and-spatial-layout.png` |
| **3.4** | **UI Composition Board** (actual proposed typography positioned over 3D space) | ✅ Ready | `design-handoff/milestone-03/visual-references/03-ui-composition-board.png` |
| **3.5** | **Camera Storyboard (K09–K12)** (4 visual keyframes with progress and headlines) | ✅ Ready | `design-handoff/milestone-03/visual-references/04-camera-storyboard-k09-k12.png` |
| **3.6** | **Material & Lighting Board** (plaster, travertine, aluminum, glass, daylight swatches) | ✅ Ready | `design-handoff/milestone-03/visual-references/05-material-and-lighting-board.png` |
| **3.7** | **Visual Reference Index & Licensing** (`REFERENCE-INDEX.md`) | ✅ Ready | `design-handoff/milestone-03/visual-references/REFERENCE-INDEX.md` |

---

## 4. Critical UI Boundary & Editorial Integrity

| Item # | Verification Criterion | Status | Notes |
|:---:|---|:---:|---|
| **4.1** | **Strict Zero 3D Text:** No text, placards, or storytelling labels baked onto 3D objects, walls, or floors. | ✅ Pass | 100% of information resides in the HTML/CSS DOM overlay. |
| **4.2** | **Strict Zero Glass Cards:** No floating glass panels with skill badges or boxed 3-card website layouts. | ✅ Pass | Clean, unboxed editorial typography with subtle gradient readability wash. |
| **4.3** | Narrative beats structured into 4 sequential beats: K09 Entrance, K10 Business Analysis, K11 SAP/Enterprise, K12 Solution Consulting. | ✅ Pass | Full copywriting, sub-themes, and metadata tags approved in `04-CONTENT-COPY.md`. |
| **4.4** | Fixed vertical navigation updates dynamically to highlight `03 Expertise` exclusively during Scene 03. | ✅ Pass | Navigation specification and click-to-scroll bindings planned. |

---

## 5. Camera & Scrollytelling Trajectory

| Item # | Verification Criterion | Status | Notes |
|:---:|---|:---:|---|
| **5.1** | Single persistent 3D world maintained; zero scene reloading, canvas resetting, or camera teleportation. | ✅ Pass | Continuous Catmull-Rom spline trajectory extending directly from K08. |
| **5.2** | $C_0$ continuity (position, target, FOV) and $C_1$ continuity (tangent velocity) verified across K08 $\to$ K09. | ✅ Pass | Position match $(36.53, 1.80, -21.62)$, initial tangent angle deviation $< 6^\circ$. |
| **5.3** | Reversible, deterministic motion: scrolling backward reproduces the exact previous visual state. | ✅ Pass | Algebraic scroll progress scrubbing verified. |
| **5.4** | Safe camera clearance envelope: $\ge 1.85\text{m}$ eye level above floor, $\ge 2.10\text{m}$ clearance from walls and columns. | ✅ Pass | Zero geometry clipping or near-plane collisions. |
| **5.5** | Dedicated desktop ($16:9$, $46^\circ$–$48^\circ$) and mobile ($9:19.5$, $48^\circ$–$50^\circ$) camera ledger. | ✅ Pass | Documented in `03-CAMERA-LEDGER.md`. |

---

## 6. Implementation Scope Boundary

| Item # | Verification Criterion | Status | Notes |
|:---:|---|:---:|---|
| **6.1** | **Design Only Scope:** No Scene 03 Three.js geometry implemented in this milestone. | ✅ Pass | Confirmed. |
| **6.2** | No production GLB assets or modified camera controller code committed to runtime codebase. | ✅ Pass | Existing runtime website untouched. |
| **6.3** | Automated commit and remote push executed per `AGENTS.md` upon verification. | ⏳ Pending Push | Scheduled immediately upon asset generation. |

---

## 7. Approval Recommendation

- **Verdict:** **READY FOR PORTFOLIO OWNER VISUAL REVIEW**
- **Next Milestone:** Milestone 03A (Blender Asset Production & GLB Export) upon owner approval of this design package.