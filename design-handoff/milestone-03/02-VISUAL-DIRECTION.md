# Scene 03 — Core Expertise | Visual Direction & Material Philosophy

## 1. Visual Philosophy: The Glass & Light Museum

The visual identity of Project Museum is defined by **quiet architectural grandeur**, **pristine natural daylight**, and **restrained material elegance**. Scene 03 (Core Expertise) expands on the spatial journey begun in the Entrance Atrium (Scene 01) and Profile Gallery (Scene 02).

Where Scene 01 established the museum's identity through circular geometry, and Scene 02 conveyed linear personal momentum through a curved corridor, **Scene 03 synthesizes these concepts into a grand circular Rotunda** — symbolizing the structural union of Business Analysis, SAP/Enterprise Systems, and Solution Consulting.

---

## 2. Color Palette & Tone Mapping

Scene 03 strictly avoids dark navy, cyberpunk, neon, or sci-fi visual tropes. All tones remain within a high-key, warm-neutral museum daylight spectrum.

```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│   Warm Plaster  │ Light Stone     │ Brushed Silver  │    Ice Blue     │  Deep Graphite  │
│     #F8F8F5     │     #F4F2EC     │     #EEF3F8     │     #D7E8F6     │     #111827     │
│   (Wall & Cove) │ (Travertine)    │  (Fins & Trims) │   (Sky & Glass) │   (Brand & UI)  │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

### Color Token Definitions
- **Warm White Plaster (`#F8F8F5` / `rgb(248, 248, 245)`):**
  Matte architectural surface for rotunda curved walls, ceiling dome, and arched portals. Reflects diffused daylight with a soft, warm ambiance ($R = 0.82$, $M = 0.00$).
- **Light Travertine Limestone (`#F4F2EC` / `rgb(244, 242, 236)`):**
  Continuous floor paving with subtle vein texture and a gentle eggshell sheen ($R = 0.20$, $Clearcoat = 0.45$). Catches soft natural daylight specular highlights without behaving like a mirror.
- **Brushed Silver Aluminum (`#EEF3F8` / `rgb(238, 243, 248)`):**
  Ultra-slim vertical colonnade fins ($4\text{cm} \times 12\text{cm}$), door jamb trims, and radial floor inlay strips ($M = 0.75$, $R = 0.22$). Subtle metallic micro-sheen.
- **Ice Blue Glass Accent (`#D7E8F6` / `rgb(215, 232, 246)`):**
  Clear architectural glazing for the circular skylight oculus and high perimeter clerestory ($Transmission = 0.96$, $IOR = 1.52$). Injects subtle freshness into zenith highlights.
- **Deep Graphite (`#111827` / `rgb(17, 24, 39)`):**
  Reserved exclusively for HTML typography headlines, active navigation indicators, and branding elements. Ensures WCAG AAA contrast ratio ($\ge 12:1$) against light plaster.

---

## 3. Lighting & Atmospheric Direction

Lighting in Scene 03 acts as an architectural material:

### 3.1 Primary Daylight Sources
1. **Zenith Oculus Skylight:**
   - Circular opening ($R = 4.0\text{m}$) at the apex of the $8.2\text{m}$ dome.
   - Emits pure, diffused zenith skylight ($6500\text{K}$, intensity $1.8\text{ lux}$), casting a soft circular pool of daylight at the center of the travertine floor.
2. **Directional Morning Sun:**
   - Warm sun angle ($\text{elevation } 42^\circ$, $\text{azimuth } 130^\circ$, $5200\text{K}$, intensity $2.8\text{ lux}$).
   - Filters through the clerestory colonnade fins, casting rhythmic, soft-edged diagonal shadow stripes across the floor and curved plaster walls.
3. **Architectural Cove Light:**
   - Concealed continuous LED cove perimeter along the base of the clerestory ring ($3200\text{K}$ warm white, soft indirect bounce).
   - Separates the vertical perimeter wall from the ceiling dome, creating spatial lightness.

### 3.2 Shadow Quality & Contrast
- **Soft Contact Shadows:** Ambient occlusion and soft directional penumbras; no harsh pitch-black shadows.
- **Exposure & Tone Mapping:** AgX or Filmic medium-high contrast tone mapping, avoiding blown-out white highlights or clipped shadows.

---

## 4. Lessons Learned from Scene 02 Visual Polish

Milestone 02 required several iterations (02C, 02D) because procedural graybox geometry initially lacked architectural maturity. Scene 03 incorporates those critical lessons from day one:

| Identified Issue in Scene 02 | Mandatory Design Rule in Scene 03 |
|---|---|
| **Raw Primitive Geometry:** Basic unchamfered cylinders looked like graybox blockouts. | **Architectural Sculpting:** All corners, archways, niches, and bases must feature realistic reveal shadowlines, $1.5\text{cm}$ chamfers, and plinth skirts. |
| **Heavy Dark Mullions:** Thick window frames dominated the scene and crossed text. | **Ultra-Slim Architectural Profiles:** Colonnade fins are slim brushed silver ($4\text{cm} \times 12\text{cm}$), maintaining lightness and keeping text areas clean. |
| **Conflicting Text Backdrop:** Windows behind text reduced headline contrast. | **Negative Space Engineering:** All camera waypoints position the editorial text over calm, warm-white plaster walls with zero structural mullions crossing behind headlines. |
| **Floor Uniformity:** Flat matte gray floor looked artificial. | **Material Depth:** Travertine stone floor features physical clearcoat sheen ($0.45$), radial aluminum divider lines, and soft daylight sheen reflections. |

---

## 5. UI Composition & Visual Balance

### 5.1 Desktop Layout Rule (1440 × 900)
- **Left Viewport (0%–42% width):** Unobstructed editorial reading column. Headline, narrative body, competency tags, and status badge sit directly over a gentle unboxed gradient mask.
- **Center & Right Viewport (42%–92% width):** Architectural showcase. The grand circular rotunda, colonnade fins, travertine floor, and oculus skylight are displayed with cinematic depth.
- **Right Viewport Edge (92%–100% width):** Fixed vertical navigation rail, indicating active state on `03 Expertise`.

### 5.2 Mobile Layout Rule (390 × 844)
- **Upper Screen (0%–58% height):** Architectural vista showcasing the rotunda dome and daylight opening.
- **Lower Screen (58%–100% height):** Editorial text anchored in a natural upward gradient wash, preserving thumb accessibility and complete legibility without boxed card borders.

---

## 6. Visual Reference Criteria for Review

For visual approval, renders and concept boards must meet the following criteria:
1. **Architectural Integrity:** Does the space look like a real, contemporary museum by an award-winning architectural firm?
2. **Material Realism:** Do plaster, stone, aluminum, and glass have tactile, believable surface qualities?
3. **Daylight Serenity:** Is the space bright, airy, and naturally lit without harsh glare or digital glow?
4. **Editorial Purity:** Is all storytelling in the HTML interface, with zero text mapped onto 3D objects?
5. **Continuous Spatial Connection:** Does the entrance threshold match the K08 portal of Profile Gallery?