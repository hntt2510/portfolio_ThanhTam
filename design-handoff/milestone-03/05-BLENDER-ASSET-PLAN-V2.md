# Scene 03 V2 — Core Expertise | Blender & 3D Asset Implementation Plan V2

## 1. Asset Overview & Architecture

- **Asset Name:** `expertise-in-motion.glb`
- **Source File:** `scene03-v2-exploration.blend`
- **Generator Script:** `generate_expertise_in_motion.py`
- **Target Export Path:** `design-handoff/milestone-03/expertise-in-motion.glb`
- **Asset Scope:** Static, physical architectural shell for Scene 03 V2. **Zero 3D text, zero embedded UI panels, zero scene cameras, zero scene lights in the exported GLB.**
- **World Position Anchor:** Connects physically to the Scene 02 exit threshold portal at $(43.24, 19.98, 0.00)$ in Blender ($Z$-up) metric space.

---

## 2. Object Hierarchy & Collections

All Scene 03 V2 objects use the `EXPM_` prefix (Expertise in Motion) to prevent namespace collisions with previous scenes:

```
Scene Collection
 ├── 01_Architecture (EXPM_Arch)
 │    ├── EXPM_Floor_Travertine           (Base 36m x 18m stone floor)
 │    ├── EXPM_Floor_BasaltPaths          (Inlaid dark basalt process lines As-Is -> To-Be)
 │    ├── EXPM_Floor_SilverInlays         (1.5cm brushed aluminum divider accents)
 │    ├── EXPM_Walls_Sawtooth             (Asymmetric perimeter walls: 6.2m south, 10.5m north)
 │    ├── EXPM_Roof_SawtoothBaffles       (4 sloped ceiling bays oriented north)
 │    ├── EXPM_Portal_EntryVestibule      (Transition connector from Scene 02 K08)
 │    └── EXPM_Portal_ExitThreshold       (Grand portal opening to Scene 04 Exhibition)
 ├── 02_Structure (EXPM_Struct)
 │    ├── EXPM_SystemSpine_Frames         (3-tier modular matrix of 8cm brushed-aluminum beams)
 │    ├── EXPM_SuspendedBridge_Deck       (Elevated pedestrian bridge at Z = 2.40m)
 │    └── EXPM_Bridge_Pylons              (Slim structural support columns)
 ├── 03_Glazing (EXPM_Glass)
 │    ├── EXPM_Clerestory_Glass           (Vertical north-facing sawtooth window panes)
 │    ├── EXPM_SystemSpine_FrostedCubes   (Semi-opaque glowing frosted-glass volumes)
 │    └── EXPM_Bridge_GlassBalustrades    (1.10m cantilevered clear glass safety rails)
 └── 04_Cameras (EXPM_Cameras - Render Only, excluded from GLB export)
      ├── CAM_K09_Reveal
      ├── CAM_K10_ProcessPaths
      ├── CAM_K11_SystemSpine
      └── CAM_K12_BridgeGlide
```

---

## 3. Geometry Dimensions & Mesh Budget

| Mesh Name | Type | Dimensions / Specs | Target Poly Count |
|---|---|---|:---:|
| `EXPM_Floor_Travertine` | Grid | $36.0\text{m} \times 18.0\text{m}$, subdivided grid | 288 quads |
| `EXPM_Floor_BasaltPaths` | Extruded Inlay | Width $1.0\text{m} \to 1.8\text{m}$, branching routes | 340 quads |
| `EXPM_Walls_Sawtooth` | Extruded Wall | Height $6.2\text{m} \to 10.5\text{m}$, $40\text{cm}$ wall thickness | 480 quads |
| `EXPM_Roof_SawtoothBaffles` | Sloped Shell | 4 angled bays inclined at $35^\circ$ | 384 quads |
| `EXPM_Clerestory_Glass` | Rectangular Panes | 4 north-facing vertical glazing strips | 64 quads |
| `EXPM_SystemSpine_Frames` | Modular Beams | $4 \times 2 \times 3$ matrix of $8\text{cm}$ aluminum beams | 960 quads |
| `EXPM_SystemSpine_FrostedCubes`| Cubes | 12 frosted glass cubes ($1.6\text{m} \times 1.6\text{m} \times 1.0\text{m}$) | 144 quads |
| `EXPM_SuspendedBridge_Deck` | Extruded Platform | Length $14.0\text{m}$, Width $3.2\text{m}$, elevated at $Z=2.4\text{m}$ | 128 quads |
| `EXPM_Bridge_GlassBalustrades` | Glass Strip | Height $1.10\text{m}$, continuous laminated glass | 96 quads |
| `EXPM_Portal_ExitThreshold` | Sculpted Arch | $W = 4.2\text{m}$, $H = 5.2\text{m}$ with chamfered reveals | 320 quads |
| **Total Asset Envelope** | — | — | **~3,400 quads (~6,800 tris)** |

*Budget Evaluation:* At $\approx 6,800$ triangles, the asset is exceptionally lightweight (well below the $16,000$ triangle limit), guaranteeing rock-solid 60 FPS performance on both mobile and desktop GPUs.

---

## 4. PBR Materials Specification

```
┌───────────────────────────┬───────────────┬───────────┬───────────┬──────────────┐
│ Material Name             │ Base Color    │ Metallic  │ Roughness │ Special      │
├───────────────────────────┼───────────────┼───────────┼───────────┼──────────────┤
│ MAT_V2_WhitePlaster       │ (0.97, 0.97, 0.96) │ 0.00 │ 0.82      │ Diffused     │
│ MAT_V2_LightTravertine    │ (0.96, 0.95, 0.93) │ 0.02 │ 0.18      │ Clearcoat .45│
│ MAT_V2_BasaltPath         │ (0.32, 0.34, 0.36) │ 0.05 │ 0.30      │ Honed stone  │
│ MAT_V2_BrushedAluminum    │ (0.94, 0.95, 0.97) │ 0.82 │ 0.20      │ Aniso sheen  │
│ MAT_V2_FrostedGlass       │ (0.94, 0.96, 0.99) │ 0.05 │ 0.35      │ Trans 0.85   │
│ MAT_V2_ClearGlass         │ (0.96, 0.98, 1.00) │ 0.00 │ 0.02      │ Trans 0.96   │
└───────────────────────────┴───────────────┴───────────┴───────────┴──────────────┘
```

---

## 5. Export Pipeline & Verification Gate

1. **Procedural Execution:**
   Export will be compiled via Blender 5.2 LTS CLI using `generate_expertise_in_motion.py`.
2. **Export Targets:**
   - Binary `.glb` format $\le 1.20\text{ MB}$.
   - Normals exported, UV maps optimized, materials mapped to glTF PBR.
   - Exclude cameras and lights.
3. **Strict Gate:** Production GLB export will **only** begin after portfolio owner visual sign-off on this V2 design package.