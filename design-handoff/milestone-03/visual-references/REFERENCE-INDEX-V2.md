# Scene 03 V2 — Visual Reference Index & Generation Audit

This document catalogues the complete visual reference deliverables prepared for **Milestone 03 V2 — Visual Experience Redesign (Expertise in Motion)**.

---

## 1. Primary Review Deliverables

| Board File | Resolution | Description & Verification Target |
|---|:---:|---|
| [`scene03-v2-master-visual-board.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/scene03-v2-master-visual-board.png) | $1920 \times 1080$ | **Master Visual Board V2:** Unifying hero visual, 4 distinct keyframes, spatial route, scroll progress schedule, 3 spatial metaphors, material swatches, and implementation checklist. |
| [`01-three-concept-candidates.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/01-three-concept-candidates.png) | $1920 \times 1080$ | **Three Concept Candidates:** Side-by-side evaluation of Candidate A (Expertise in Motion), Candidate B (The Step-Terrace Hall), and Candidate C (The Prism Pavilion) with structural descriptions and recommendations. |
| [`02-scene02-vs-scene03-comparison.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/02-scene02-vs-scene03-comparison.png) | $1920 \times 1080$ | **Scene 02 vs Scene 03 Contact Sheet:** Side-by-side audit comparing actual Scene 02 K07/K08 screenshots against Scene 03 V2 renders, proving radical differences in spatial volume, height, perspective, and installations. |
| [`03-recommended-concept-hero.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/03-recommended-concept-hero.png) | $1920 \times 1080$ | **Recommended Hero Perspective:** Wide establishing view of the 36m asymmetric sawtooth pavilion with brand typography and owner subtitle **Hoàng Nguyễn Thành Tâm / 2026**. |
| [`04-camera-storyboard-k09-k12-v2.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/04-camera-storyboard-k09-k12-v2.png) | $1920 \times 1080$ | **Four Visually Distinct Keyframes:** K09 Reveal, K10 Elevated Process Paths ($Z=3.2\text{m}$), K11 Modular System Spine ($Z=1.85\text{m}$ side-tracking), and K12 Suspended Bridge ($Z=4.05\text{m}$). |
| [`05-ui-varied-compositions-board.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/05-ui-varied-compositions-board.png) | $1920 \times 1080$ | **Varied Editorial UI Layouts:** 4 distinct on-screen compositions: center-left reveal (K09), bottom-left banner with horizontal milestone pills (K10), split column (K11), and bridge gateway (K12). |
| [`06-spatial-route-and-topdown-v2.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/06-spatial-route-and-topdown-v2.png) | $1920 \times 1080$ | **Top-Down Spatial Route & Footprint:** Technical architectural blueprint showing seam from K08, 36m x 18m asymmetric hall, branching pathways, system spine matrix, bridge, and camera spline. |
| [`07-material-lighting-feasibility-v2.png`](file:///D:/THANHTAM/CV/Portfolio/design-handoff/milestone-03/visual-references/07-material-lighting-feasibility-v2.png) | $1920 \times 1080$ | **Material, Lighting & Feasibility Review:** PBR shaders, north sawtooth daylight optics, and Three.js runtime performance budget ($\sim 6,800$ triangles, GLB $\le 1.20\text{ MB}$). |

---

## 2. Individual 3D Renders & Assets

- `candidate-A-expertise-in-motion.png`: Full-resolution 3D render of Candidate A.
- `candidate-B-step-terrace-hall.png`: Full-resolution 3D render of Candidate B.
- `candidate-C-prism-pavilion.png`: Full-resolution 3D render of Candidate C.
- `keyframe-K09-v2-reveal.png`: K09 wide reveal through portal into asymmetric space.
- `keyframe-K10-v2-process-paths.png`: K10 elevated oblique vantage point overlooking branching floor lines.
- `keyframe-K11-v2-system-spine.png`: K11 side-tracking view of the 3-tier modular structural installation.
- `keyframe-K12-v2-bridge-portal.png`: K12 forward perspective crossing suspended bridge toward Scene 04.
- `06-raw-topdown-v2.png`: Orthographic top-down render of the entire spatial layout.
- `scene03-v2-exploration.blend`: Archival Blender 5.2.3 LTS project containing all 3 candidate models and cameras.

---

## 3. Tooling & Reproducibility

- **Blender 3D Modeling & Rendering:**
  `blender -b -P design-handoff/milestone-03/build_scene03_v2_models.py`
- **Visual Board Compositor:**
  `python design-handoff/milestone-03/generate_v2_visual_boards.py`

---

## 4. Licensing & IP Audit

- 100% procedurally authored in Blender and Python for this repository. Zero copyrighted external 3D models or stock imagery used.
- All assets strictly designated for design planning and visual review. Zero production GLB assets or Three.js code created in this milestone.