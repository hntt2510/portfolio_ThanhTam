# Milestone 02A — Profile Gallery Asset Report

## 1. Overview
- **Asset Name**: `profile-gallery.glb`
- **Blender Source**: `profile-gallery.blend`
- **Generator Script**: `generate_profile_gallery.py`
- **Output Directory**: `design-handoff/milestone-02/`
- **File Size**: 126.66 KB
- **Architecture**: Gently curved daylight architectural gallery connecting directly to Scene 01's north-east exit corridor at $(15.0, 15.0, 0.0)$, curving along an arc of radius $R = 25.0\text{m}$ (width $W = 5.20\text{m}$) from $\alpha = 135^\circ$ to $\alpha = 65^\circ$.
- **Adherence to Spec**: 100% background architecture. Zero 3D text, zero UI panels, zero narrative labels on meshes. All biographical copy is reserved for the HTML/CSS DOM layer.

## 2. Technical Validation
GLB re-import verification performed using Blender 5.2.3 LTS headless:

| Metric | Measured Value | Spec Target / Limit | Status |
|---|---|---|---|
| File Size | 126.66 KB | < 5.0 MB | PASS |
| Mesh Objects | 39 meshes | Clean modular hierarchy | PASS |
| Vertices Count | 3,280 vertices | < 30,000 | PASS |
| Polygons / Triangles | 1,646 faces | < 25,000 | PASS |
| Materials Count | 7 safe PBR materials | Compact, standard glTF PBR | PASS |
| Embedded Lights | 0 | 0 (Lights configured in Three.js runtime) | PASS |
| Embedded Cameras | 0 | 0 (Cameras handled by Three.js controller) | PASS |
| Bounding Box X | -0.52 to 54.83 m | Spans seam to exit arch | PASS |
| Bounding Box Y | 12.88 to 40.92 m | Smooth continuous arc | PASS |
| Bounding Box Z | -0.29 to 5.80 m | Floor to ceiling height ~5.2m | PASS |

## 3. Hierarchy and Mesh Naming
All architectural elements follow the `PRG_` prefix convention:
- `PRG_Floor`: Continuous curved stone promenade floor ($R_{\text{in}} = 22.40\text{m}$, $R_{\text{out}} = 27.60\text{m}$, thickness $0.20\text{m}$).
- `PRG_InnerWall`: Continuous curved white plaster gallery wall with architectural baseboard.
- `PRG_OuterCurtainWall_Glass`: Double-height curved architectural glazing panels.
- `PRG_OuterSill`: Ground perimeter sill anchoring curtain wall.
- `PRG_Mullions` (`Cube.001`–`Cube.018`): 18 structural vertical mullions spaced regularly along the glazed arc.
- `PRG_Ceiling`: Curved architectural ceiling with perimeter soffit.
- `PRG_CoveLight`: Curved architectural LED cove lighting channel.
- `PRG_Threshold_PostL`, `PRG_Threshold_PostR`, `PRG_Threshold_Header`: Minimalist aluminum architectural portal at exit to future Scene 03 ($\alpha = 65^\circ$).
- `PRG_Bench_01`–`PRG_Bench_03`: Three minimalist stone gallery benches placed along the window promenade.
- `PRG_LandscapeGround` & `PRG_HedgeRow` & Low-poly trees: Exterior landscape garden elements visible through glass.

## 4. Materials
All materials use standard Principled BSDF nodes compatible with glTF 2.0 and Three.js `MeshPhysicalMaterial` / `MeshStandardMaterial`:
1. `MAT_WhitePlaster`: Base color `(0.96, 0.96, 0.95)`, Roughness `0.88`, Metallic `0.0`.
2. `MAT_LightStone`: Base color `(0.92, 0.90, 0.88)`, Roughness `0.35`, Metallic `0.02`.
3. `MAT_ClearGlass`: Base color `(0.98, 0.99, 1.0)`, Transmission `1.0`, Roughness `0.05`, IOR `1.52`.
4. `MAT_BrushedAluminum`: Base color `(0.85, 0.86, 0.88)`, Roughness `0.30`, Metallic `0.85`.
5. `MAT_CoveLight`: Base color `(1.0, 0.98, 0.95)`, Emission Strength `3.0`.
6. `MAT_HedgeGreen`: Base color `(0.42, 0.52, 0.40)`, Roughness `0.75`, Metallic `0.0`.
7. `MAT_LandscapeGreen`: Base color `(0.55, 0.62, 0.50)`, Roughness `0.85`, Metallic `0.0`.

## 5. Camera Waypoint Alignment & Seam Continuity
- **Coordinate Conversion**: $X_{\text{Three}} = X_{\text{Blender}}, Y_{\text{Three}} = Z_{\text{Blender}}, Z_{\text{Three}} = -Y_{\text{Blender}}$.
- **Seam Join**: Entrance corridor of Scene 01 terminates at Blender $(15.0, 15.0, 0.0)$, matching Three.js $(15.0, 0.0, -15.0)$. Scene 02 begins flush at this exact interface with zero elevation step or gap.
- **Camera Path Radii**: Walking aisle placed at $R_{\text{cam}} = 24.60\text{m}$, looking ahead at $R_{\text{tgt}} = 25.40\text{m}$ along the curve at height $Z = 1.80\text{m}$.
- **Proof Renders Generated**:
  - `camera-K05.png`: Entry establishing view (Beat 1: From Software Engineering to Enterprise Problem Solving).
  - `camera-K06.png`: Foundation view along glazed colonnade (Beat 2: Built on a Technical Foundation).
  - `camera-K07.png`: Experience view through mid-gallery (Beat 3: Turning Requirements into Solutions).
  - `camera-K08.png`: Perspective / Exit view toward threshold arch (Beat 4: Connecting Business & Technology).
  - `top-down-layout.png`: Orthographic layout showing curve curvature and garden terrace.
  - `seam-continuity.png`: View from corridor neck into gallery establishing contiguous transition.
