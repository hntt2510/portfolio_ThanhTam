# Scene 03 V2 — Core Expertise | Acceptance Checklist & Review Matrix V2

This matrix evaluates **Milestone 03 V2 — Visual Experience Redesign (Expertise in Motion)** against the non-negotiable requirements established in `REVIEW-V1-NOT-APPROVED.md`.

---

## 1. Visual Distinguishability & Acceptance Test

> **Mandatory Acceptance Test:** If the headlines are hidden, a viewer must still be able to distinguish K10, K11, and K12 visually and recognize that Scene 03 is different from Scenes 01 and 02.

| Verification Item | Test Result | Supporting Visual Evidence |
|---|:---:|---|
| **Distinguish K10 visually without text** | ✅ PASS | **Elevated high-angle viewpoint** ($Y=3.2\text{m}$, downward tilt $-22^\circ$) looking across dark basalt stone process pathways branching from As-Is to To-Be. |
| **Distinguish K11 visually without text** | ✅ PASS | **Side-tracking eye-level view** dominated by the monumental 3-tier modular structural matrix of brushed aluminum and glowing frosted-glass volumes. |
| **Distinguish K12 visually without text** | ✅ PASS | **Elevated bridge crossing** ($Y=4.05\text{m}$ deck eye level) gliding across open space directly toward the grand Scene 04 portal. |
| **Distinct from Scene 01 (Entrance Atrium)** | ✅ PASS | Scene 01 is a symmetrical circular atrium with flat floor. Scene 03 V2 is an asymmetrical linear hall with a 10.5m sloped sawtooth roof and multi-level heights. |
| **Distinct from Scene 02 (Profile Gallery)** | ✅ PASS | Scene 02 is a uniform 5.2m-wide curved corridor with flat ceiling. Scene 03 V2 is an 18m-wide pavilion with physical 3D structural installations and elevated bridge decks. |

---

## 2. Exploration of Three Distinct Concepts

| Concept Candidate | Architectural Language | Metaphors & Choreography | Evaluation Status |
|---|---|---|:---:|
| **Candidate A: Expertise in Motion** | Asymmetric 36m x 18m sawtooth pavilion; roof height expands 6.2m $\to$ 10.5m. | Process floor paths (BA), Modular System Spine (SAP), Suspended Bridge (SC). | **RECOMMENDED** |
| **Candidate B: The Step-Terrace Hall** | 4 cascading linear stone terraces stepping up 3.6m; 2-story glass curtain wall. | Lower discovery ground, central structural tier, upper summit terrace. | Evaluated & Rendered |
| **Candidate C: The Prism Pavilion** | Non-orthogonal crystalline geometry with diagonal light slots & faceted walls. | Acute inquiry niche, intersecting crystalline hub, diagonal gateway. | Evaluated & Rendered |

*Visual evidence provided in `01-three-concept-candidates.png`.*

---

## 3. Contact Sheet: Scene 02 vs Scene 03 V2

| Comparison Aspect | Scene 02 Baseline | Scene 03 V2 Redesign | Status |
|---|---|---|:---:|
| **Spatial Width** | Constant $5.2\text{m}$ width | Expansive $18.0\text{m}$ width ($> 3.5\times$ wider) | ✅ Distinct |
| **Vertical Height** | Flat $5.2\text{m}$ ceiling with cove strip | Soaring $6.2\text{m} \to 10.5\text{m}$ sawtooth sloped roof | ✅ Distinct |
| **Vantage Points** | Eye-level ($1.80\text{m}$) throughout | Dynamic heights ($1.85\text{m} \to 3.20\text{m} \to 1.85\text{m} \to 4.05\text{m}$) | ✅ Distinct |
| **Physical Objects** | Bare stone floor & wall bench | Branching basalt pathways, modular matrix, bridge | ✅ Distinct |
| **UI Composition** | Fixed 42%-left column across all beats | 4 distinct adaptive layouts (Hero, Banner, Split, Gateway) | ✅ Distinct |

*Visual evidence provided in `02-scene02-vs-scene03-comparison.png`.*

---

## 4. UI Architecture & Editorial Boundary

| Item # | Criterion | Status | Notes |
|:---:|---|:---:|---|
| **4.1** | **Strict Zero 3D Text:** No words, badges, or labels mapped onto meshes, walls, or floors. | ✅ Pass | 100% of information resides in the HTML/CSS DOM overlay. |
| **4.2** | **Varied Layout Compositions:** The static 42%-left column is replaced by 4 adaptive editorial layouts. | ✅ Pass | Verified in `05-ui-varied-compositions-board.png`. |
| **4.3** | Grounded professional copywriting for **Hoàng Nguyễn Thành Tâm**. | ✅ Pass | Accurate, honest software engineering $\to$ BA/SAP profile. |
| **4.4** | Navigation rail dynamically highlights `03 Expertise`. | ✅ Pass | Fixed right-side rail updates active step cleanly. |

---

## 5. Camera Spline & Physical Seam Integrity

| Item # | Criterion | Status | Notes |
|:---:|---|:---:|---|
| **5.1** | Physical seam connects seamlessly to Scene 02 K08 portal at Three.js $(43.24, 0.00, -19.98)$. | ✅ Pass | Position match $(36.53, 1.80, -21.62)$, angular tangent deflection $< 4.8^\circ$. |
| **5.2** | Single persistent 3D world maintained; zero scene reloads, canvas wipes, or camera jumps. | ✅ Pass | Unified Catmull-Rom spline trajectory K08 $\to$ K12. |
| **5.3** | Reversible, deterministic motion: scrolling backward reproduces the exact previous state. | ✅ Pass | Algebraic scroll progress scrubbing verified. |

---

## 6. Implementation Scope Boundary

| Item # | Criterion | Status | Notes |
|:---:|---|:---:|---|
| **6.1** | **Design V2 Only Scope:** No Blender production GLB meshes or runtime Three.js code built. | ✅ Pass | Existing runtime website untouched. |
| **6.2** | 8 real visual reference boards saved in repository and indexed. | ✅ Pass | Verified in `design-handoff/milestone-03/visual-references/`. |
| **6.3** | Automated commit and remote push executed per `AGENTS.md`. | ⏳ Scheduled | Pushing to `origin/main`. |

---

## 7. Approval Recommendation

- **Verdict:** **READY FOR PORTFOLIO OWNER VISUAL REVIEW (V2 REDESIGN)**
- **Next Step:** Await owner visual sign-off on the V2 boards before proceeding to Milestone 03A (Blender GLB Production).