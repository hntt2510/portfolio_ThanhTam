# Scene 03 — Core Expertise | Visual Reference Index & Licensing

This document details the generation origin, prompt specifications, architectural parameters, and licensing compliance for all visual reference assets prepared for **Milestone 03 — Core Expertise Design & Visual Planning**.

---

## 1. Visual Reference Asset Ledger

| Filename | Resolution | Description / Spatial Intent | Source / Tooling |
|---|:---:|---|---|
| `scene03-visual-board-master.png` | $1920 \times 1080$ | Comprehensive creative director visual board featuring hero perspective, unboxed typography, 4-shot camera storyboard, spatial layout, timeline progress, UI layer diagram, material swatches, and implementation checklist. | Custom procedural pipeline (PIL + Blender 5.2.3 LTS render integration) |
| `01-scene03-hero-visual.png` | $1376 \times 768$ | Wide establishing eye-level architectural concept view of the Expertise Rotunda, showcasing the central oculus skylight, travertine floor with radial inlays, warm-white plaster walls, and natural morning daylight. | Imagen 3 via Antigravity `image-generator` subagent |
| `02-architecture-and-spatial-layout.png` | $1920 \times 1080$ | Orthographic technical architectural plan diagram with coordinate grid, camera spline trajectory K08 $\to$ K12, seam anchor at $(43.24, 0.00, -19.98)$, and dimensions of the three competency zones. | Blender 5.2.3 LTS orthographic rendering + technical diagramming |
| `03-ui-composition-board.png` | $1920 \times 1080$ | Unboxed editorial typography overlay validation showing headline *"Where Business Meets Technology."*, sub-themes, brand title, owner subtitle **Hoàng Nguyễn Thành Tâm / 2026**, and fixed vertical navigation rail with `03 Expertise` active. | High-resolution render composite + DOM layout simulation |
| `04-camera-storyboard-k09-k12.png` | $1920 \times 1080$ | Four sequential scrollytelling keyframes (K09 Entrance, K10 Business Analysis, K11 SAP/Enterprise, K12 Solution Consulting) with scroll percentages, headlines, descriptions, and exact mathematical camera poses. | Multi-card composite with individual keyframe perspectives |
| `05-material-and-lighting-board.png` | $1920 \times 1080$ | Material PBR shader swatches (Plaster `#F8F8F5`, Travertine `#F4F2EC`, Brushed Aluminum `#EEF3F8`, Glass `#FAFCFF`, Cove Light `#FFF8EB`), daylight illumination strategy, and WCAG AAA contrast ratio compliance matrix. | Technical shader and colorimetric layout |
| `keyframe-K09-visual-reference.png` | $1376 \times 768$ | Keyframe K09: Eye-level perspective stepping through the sculpted arched portal into the threshold of the grand circular Expertise Rotunda. | Imagen 3 via Antigravity `image-generator` |
| `keyframe-K10-visual-reference.png` | $1376 \times 768$ | Keyframe K10: Eye-level tracking shot framing the Business Analysis curved alcove with clean negative space on the left for HTML text overlays. | Imagen 3 via Antigravity `image-generator` |
| `keyframe-K11-visual-reference.png` | $1920 \times 1080$ | Keyframe K11: Eye-level perspective tracking through the colonnade of slim vertical brushed-silver aluminum fins with morning daylight shadows streaming across the travertine floor. | Blender 5.2.3 LTS architectural EEVEE-Next render |
| `keyframe-K12-visual-reference.png` | $1920 \times 1080$ | Keyframe K12: Eye-level perspective approaching the grand architectural exit portal leading toward future Scene 04 (Project Exhibition). | Blender 5.2.3 LTS architectural EEVEE-Next render |

---

## 2. Prompts & Technical Generation Briefs

### 2.1 Hero Visual & Oculus Dome
> **Prompt:** *"Photorealistic 3D architectural concept render of the 'Expertise Rotunda' for a modern Glass & Light Museum. Grand circular museum rotunda with high domed ceiling featuring an elegant central circular oculus/clerestory admitting bright natural diffused daylight. Curved warm-white plaster walls with subtle reveals, polished light travertine limestone flooring with subtle radial brass/silver inlay lines and soft daylight specular reflections. Slim brushed-aluminum columns and minimalist architectural openings. Pristine, airy, bright daylight, subtle ice-blue tints through glass skylight, warm white interior ambiance, zero dark shadows, no dark navy, no cyberpunk, no neon. Contemporary Scandinavian / Swiss museum architecture (similar to SANAA or David Chipperfield). Clean architectural shot with no people, wide angle lens (28mm equivalent), eye level perspective."*

### 2.2 Keyframe K09 (Entrance Archway)
> **Prompt:** *"Keyframe K09 – Entrance to Expertise. Eye-level (1.8m) shot looking forward through an elegant sculpted arched portal from the connecting museum corridor, stepping into the threshold of the grand circular Expertise Rotunda. High domed ceiling with a central circular glass oculus admitting bright natural diffused daylight, polished travertine floor with subtle radial lines extending into the circular hall, warm-white plaster walls, slim brushed-aluminum trim. Serene daylight, warm-white and pale silver palette, pristine Swiss/Scandinavian modern museum aesthetic, no people."*

### 2.3 Keyframe K10 (Business Analysis Alcove)
> **Prompt:** *"Keyframe K10 – Business Analysis Alcove. Eye-level (1.85m) tracking shot inside the Expertise Rotunda, angled toward the first architectural zone on the left: the Business Analysis curved alcove. High negative space and soft daylight wash on the left side of the frame (reserved for editorial typography), while the right side frames the spacious circular rotunda with slim brushed-aluminum reveal details, polished travertine limestone floor with soft sun reflections, and warm-white plaster walls. Serene morning daylight, warm-white and silver palette, pristine Swiss museum architectural aesthetic, no text or people."*

---

## 3. Tooling & Reproducibility Scripts

All reference models and boards are fully reproducible from source code stored in this directory:
- **Blender 3D Scene Script:** `design-handoff/milestone-03/build_scene03_renders.py`
  - Re-run via: `blender -b -P design-handoff/milestone-03/build_scene03_renders.py`
  - Outputs: `02-raw-topdown.png`, `keyframe-K11-render.png`, `keyframe-K12-render.png`, `expertise-rotunda-design.blend`.
- **Visual Board Generator Script:** `design-handoff/milestone-03/generate_visual_boards.py`
  - Re-run via: `python design-handoff/milestone-03/generate_visual_boards.py`
  - Outputs: `scene03-visual-board-master.png`, `02-architecture-and-spatial-layout.png`, `03-ui-composition-board.png`, `04-camera-storyboard-k09-k12.png`, `05-material-and-lighting-board.png`.

---

## 4. Licensing & Copyright Compliance

- **Artistic Origin:** All architectural concepts and reference assets were procedurally modeled in Blender and generated via DeepMind Imagen 3 / Python imaging tools specifically for this repository.
- **Third-Party Intellectual Property:** **Zero** proprietary 3D models, unlicensed textures, copyrighted photos, or commercial stock imagery are included.
- **Production Boundary:** These images serve exclusively as design planning and visual review references. No reference images are shipped as runtime WebGL textures or production website assets. All production geometry in subsequent milestones will be clean procedural GLB geometry adhering to the design specifications.