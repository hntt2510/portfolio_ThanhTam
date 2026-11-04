# Scene 03 — Core Expertise | Blender & 3D Asset Implementation Plan

## 1. Asset Overview & Architecture

- **Asset Name:** `expertise-rotunda.glb`
- **Source File:** `expertise-rotunda.blend`
- **Generator Script:** `generate_expertise_rotunda.py`
- **Target Export Path:** `design-handoff/milestone-03/expertise-rotunda.glb`
- **Asset Scope:** Static, physical architectural shell for Scene 03. **Zero 3D text, zero embedded UI panels, zero cameras, zero scene lights in the exported GLB.**
- **World Position Anchor:** Connects physically to the Scene 02 exit threshold portal at $(43.24, 19.98, 0.00)$ in Blender ($Z$-up) metric space.

---

## 2. Object Naming Conventions & Scene Hierarchy

All Scene 03 objects strictly use the `EXP_` prefix (Expertise Rotunda) to eliminate namespace collisions with Scene 01 (`ATR_`) and Scene 02 (`PRG_`).

```
Scene Collection
 ├── 01_Architecture (EXP_Arch)
 │    ├── EXP_Floor_Travertine           (Circular travertine floor with radial seams)
 │    ├── EXP_Floor_Inlay_Rings          (Brushed aluminum radial divider strips)
 │    ├── EXP_Wall_Perimeter             (Curved warm-white plaster perimeter wall)
 │    ├── EXP_Alcove_BusinessAnalysis    (Recessed architectural wall niche)
 │    ├── EXP_Dome_Ceiling               (Spherical ceiling dome with circular aperture)
 │    ├── EXP_Oculus_SkylightRing        (Architectural reveal and trim around oculus)
 │    ├── EXP_Portal_EntryVestibule      (Transition connector from Scene 02 K08)
 │    └── EXP_Portal_ExitThreshold       (Grand archway opening to Scene 04 Exhibition)
 ├── 02_Structure (EXP_Struct)
 │    ├── EXP_Colonnade_VerticalFins     (Array of 24 slim brushed-aluminum fins)
 │    ├── EXP_Colonnade_Architrave       (Curved aluminum head rail above colonnade)
 │    └── EXP_Portal_JambTrims           (Precision aluminum portal frames)
 ├── 03_Glazing (EXP_Glass)
 │    ├── EXP_Glass_OculusDome           (Segmented architectural clear glass dome)
 │    └── EXP_Glass_Clerestory           (Curved exterior daylight clerestory panes)
 ├── 04_Lighting (EXP_LightHelpers)
 │    └── EXP_Light_CoveRing             (Mesh light emitting 3200K warm indirect bounce)
 └── 05_Cameras (EXP_Cameras - Render Only, excluded from GLB export)
      ├── CAM_K09_Entrance
      ├── CAM_K10_BusinessAnalysis
      ├── CAM_K11_EnterpriseSystems
      └── CAM_K12_SolutionConsulting
```

---

## 3. Geometry Dimensions & Mesh Budget

| Mesh Name | Type | Dimensions / Specs | Target Poly Count |
|---|---|---|:---:|
| `EXP_Floor_Travertine` | N-Gon / Grid | Radius $12.00\text{m}$, 48 radial segments, 4 concentric rings | 384 quads |
| `EXP_Floor_Inlay_Rings` | Extruded Curve | $1.5\text{cm} \times 0.5\text{cm}$ brushed aluminum inlays | 288 quads |
| `EXP_Wall_Perimeter` | Curved Extrusion | Height $6.80\text{m}$, Radius $12.00\text{m}$, $35\text{cm}$ wall thickness | 768 quads |
| `EXP_Alcove_BusinessAnalysis`| Sculpted Wall | Width $6.80\text{m}$, Depth $1.80\text{m}$, Height $5.20\text{m}$ with chamfers | 320 quads |
| `EXP_Dome_Ceiling` | Dome Shell | Radius $12.00\text{m} \to 4.00\text{m}$ oculus, Height $6.80\text{m} \to 8.20\text{m}$ | 768 quads |
| `EXP_Oculus_SkylightRing` | Revolve | Inner $R = 4.00\text{m}$, Outer $R = 4.25\text{m}$, depth $30\text{cm}$ | 256 quads |
| `EXP_Portal_EntryVestibule` | Sculpted Arch | $W = 3.60\text{m}$, $H = 4.50\text{m}$, length $4.20\text{m}$ | 384 quads |
| `EXP_Portal_ExitThreshold` | Sculpted Arch | $W = 4.00\text{m}$, $H = 5.00\text{m}$, length $2.50\text{m}$ | 412 quads |
| `EXP_Colonnade_VerticalFins` | Extruded Array | 24 fins, $4\text{cm} \times 12\text{cm} \times 4.80\text{m}$ high | 576 quads |
| `EXP_Glass_OculusDome` | Low-poly Dome | $R = 4.00\text{m}$, segmented clear glazing | 192 quads |
| `EXP_Glass_Clerestory` | Cylindrical Strip| Height $1.60\text{m}$, curved facade glazing | 256 quads |
| `EXP_Light_CoveRing` | Revolve Strip | Concealed $10\text{cm}$ indirect LED cove strip | 96 quads |
| **Total Asset Envelope** | — | — | **~4,700 quads (~9,400 tris)** |

*Budget Evaluation:* At $\approx 9,400$ triangles, the asset operates well within the $16,000$ triangle budget, ensuring silky-smooth 60 FPS performance even on low-tier mobile devices.

---

## 4. PBR Materials Specification

All materials are formulated as glTF 2.0 compliant PBR shaders:

```
┌───────────────────────────┬───────────────┬───────────┬───────────┬──────────────┐
│ Material Name             │ Base Color    │ Metallic  │ Roughness │ Special      │
├───────────────────────────┼───────────────┼───────────┼───────────┼──────────────┤
│ MAT_EXP_WhitePlaster      │ (0.97, 0.97, 0.96) │ 0.00 │ 0.82      │ Soft bounce  │
│ MAT_EXP_TravertineStone   │ (0.96, 0.95, 0.93) │ 0.02 │ 0.20      │ Clearcoat .45│
│ MAT_EXP_BrushedAluminum   │ (0.94, 0.95, 0.97) │ 0.75 │ 0.22      │ Aniso sheen  │
│ MAT_EXP_ClearGlass        │ (0.97, 0.98, 1.00) │ 0.00 │ 0.02      │ Trans 0.96   │
│ MAT_EXP_CoveLight         │ (1.00, 0.97, 0.92) │ 0.00 │ 1.00      │ Emission 4.5 │
└───────────────────────────┴───────────────┴───────────┴───────────┴──────────────┘
```

---

## 5. Export Pipeline & glTF Configuration

1. **Automation:** Export will be executed headlessly via Blender 5.2 LTS CLI:
   `blender -b -P design-handoff/milestone-03/generate_expertise_rotunda.py`
2. **Export Settings:**
   - Format: `GLB` (binary glTF 2.0).
   - Coordinate Conversion: $+Y$ up (Blender to Three.js conversion handled by exporter).
   - Apply Modifiers: `True`.
   - Include: Mesh, Materials.
   - Exclude: Cameras, Lights, Animation, Custom Properties.
   - Geometry: Normals exported, Tangents computed, Materials exported as PBR.
3. **Verification Target:**
   - Resulting file size strictly $\le 1.50\text{ MB}$.
   - Validated via Three.js `GLTFLoader` with zero shader compile warnings and zero missing textures.