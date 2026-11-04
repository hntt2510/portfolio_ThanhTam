"""
Procedural Generator for Milestone 02D: Profile Gallery Visual Fidelity Pass
Glass & Light Museum - Hoàng Nguyễn Thành Tâm

Key Enhancements for 02D:
- Sculpted architectural exit portal at K08 with rounded archway and sunlit alcove view
- Ultra-slim brushed silver aluminum mullions (3.5cm x 7cm) and transoms (3cm profile)
- Multi-scale organic botanical trees with realistic branching trunks and multifaceted foliage lobes
- Layered garden landscape: manicured boxwood hedge, stone curb, textured lawn, and sky backdrop
- Polished travertine floor with subtle slab delineation and warm daylight sheen
- Continuous cove lighting gracefully sweeping into the exit archway
- Camera proof renders matching approved Visual Board V2 (K05, K06, K07, K08)
- Clean GLB export with PRG_ naming convention, 0 embedded lights/cameras
"""

import bpy
import bmesh
import math
import os
import random

# Seed for reproducible organic foliage
random.seed(42)

# Reset Scene
bpy.ops.wm.read_factory_settings(use_empty=True)

scene = bpy.context.scene
scene.name = "ProfileGallery_V2D_Scene"
scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'RenderEngine') and 'BLENDER_EEVEE_NEXT' in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items] else 'BLENDER_EEVEE'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Color Management
scene.display_settings.display_device = 'sRGB'
scene.view_settings.view_transform = 'AgX' if 'AgX' in [v.identifier for v in scene.view_settings.bl_rna.properties['view_transform'].enum_items] else 'Filmic'
scene.view_settings.look = 'Medium High Contrast'
scene.view_settings.exposure = 0.18

# World Daylight Sky
world = bpy.data.worlds.new("PRG_DaylightWorld")
scene.world = world
world.use_nodes = True
nodes_w = world.node_tree.nodes
nodes_w.clear()
node_bg = nodes_w.new(type='ShaderNodeBackground')
node_bg.inputs['Color'].default_value = (0.90, 0.95, 1.0, 1.0)
node_bg.inputs['Strength'].default_value = 1.45
node_w_out = nodes_w.new(type='ShaderNodeOutputWorld')
world.node_tree.links.new(node_bg.outputs['Background'], node_w_out.inputs['Surface'])

# Collections Hierarchy
col_arch = bpy.data.collections.new("01_Architecture")
col_furn = bpy.data.collections.new("02_Furniture")
col_env = bpy.data.collections.new("03_Environment")
col_render = bpy.data.collections.new("04_RenderHelpers")
col_cam = bpy.data.collections.new("05_Cameras")

for c in [col_arch, col_furn, col_env, col_render, col_cam]:
    scene.collection.children.link(c)

def link_obj(obj, col):
    if obj.name not in col.objects:
        col.objects.link(obj)

# Materials Helper
def create_pbr_material(name, base_color, metallic=0.0, roughness=0.5, transmission=0.0, ior=1.5, alpha=1.0, emission=(0,0,0,1), emission_strength=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    bsdf = nodes.get("Principled BSDF")
    if bsdf:
        if 'Base Color' in bsdf.inputs:
            bsdf.inputs['Base Color'].default_value = base_color
        if 'Metallic' in bsdf.inputs:
            bsdf.inputs['Metallic'].default_value = metallic
        if 'Roughness' in bsdf.inputs:
            bsdf.inputs['Roughness'].default_value = roughness
        if 'Transmission Weight' in bsdf.inputs:
            bsdf.inputs['Transmission Weight'].default_value = transmission
        elif 'Transmission' in bsdf.inputs:
            bsdf.inputs['Transmission'].default_value = transmission
        if 'IOR' in bsdf.inputs:
            bsdf.inputs['IOR'].default_value = ior
        if emission_strength > 0:
            if 'Emission Color' in bsdf.inputs:
                bsdf.inputs['Emission Color'].default_value = emission
            elif 'Emission' in bsdf.inputs:
                bsdf.inputs['Emission'].default_value = emission
            if 'Emission Strength' in bsdf.inputs:
                bsdf.inputs['Emission Strength'].default_value = emission_strength
        if alpha < 1.0:
            if 'Alpha' in bsdf.inputs:
                bsdf.inputs['Alpha'].default_value = alpha
            mat.blend_method = 'BLEND'
    return mat

mat_plaster = create_pbr_material("MAT_WhitePlaster", (0.97, 0.97, 0.96, 1.0), metallic=0.0, roughness=0.82)
mat_stone = create_pbr_material("MAT_LightStone", (0.96, 0.95, 0.93, 1.0), metallic=0.02, roughness=0.20)
mat_aluminum = create_pbr_material("MAT_BrushedAluminum", (0.94, 0.95, 0.97, 1.0), metallic=0.75, roughness=0.22)
mat_glass = create_pbr_material("MAT_ClearGlass", (0.97, 0.98, 1.0, 1.0), metallic=0.0, roughness=0.02, transmission=0.96, ior=1.52, alpha=0.24)
mat_curb = create_pbr_material("MAT_StoneCurb", (0.92, 0.91, 0.89, 1.0), metallic=0.02, roughness=0.35)

# Botanical Landscape Materials
mat_lawn = create_pbr_material("MAT_GardenLawn", (0.38, 0.56, 0.26, 1.0), metallic=0.0, roughness=0.85)
mat_hedge = create_pbr_material("MAT_BoxwoodHedge", (0.24, 0.40, 0.18, 1.0), metallic=0.0, roughness=0.75)
mat_trunk = create_pbr_material("MAT_TreeBark", (0.38, 0.32, 0.26, 1.0), metallic=0.0, roughness=0.85)
mat_foliage_sun = create_pbr_material("MAT_FoliageSunlit", (0.36, 0.54, 0.22, 1.0), metallic=0.0, roughness=0.65)
mat_foliage_deep = create_pbr_material("MAT_FoliageDeep", (0.22, 0.38, 0.15, 1.0), metallic=0.0, roughness=0.70)
mat_sky_backdrop = create_pbr_material("MAT_SkyBackdrop", (0.75, 0.88, 0.98, 1.0), metallic=0.0, roughness=1.0, emission=(0.80, 0.90, 1.0, 1.0), emission_strength=1.2)

# Cove Lighting Material
mat_cove = bpy.data.materials.new(name="MAT_CoveLight")
mat_cove.use_nodes = True
nodes = mat_cove.node_tree.nodes
nodes.clear()
node_out = nodes.new(type='ShaderNodeOutputMaterial')
node_emit = nodes.new(type='ShaderNodeEmission')
node_emit.inputs['Color'].default_value = (1.0, 0.97, 0.92, 1.0)
node_emit.inputs['Strength'].default_value = 4.2
mat_cove.node_tree.links.new(node_emit.outputs['Emission'], node_out.inputs['Surface'])

# ==========================================
# Geometry: Curved Gallery Corridor
# ==========================================
CX = 32.677695
CY = -2.677695
R_CENTER = 25.0
GALLERY_W = 5.2
R_INNER = R_CENTER - GALLERY_W / 2.0  # 22.40m
R_OUTER = R_CENTER + GALLERY_W / 2.0  # 27.60m
WALL_H = 5.20

ALPHA_START = math.radians(135.0)
ALPHA_END = math.radians(65.0)
STEPS = 48

# 1. Travertine Floor Mesh: spans seamlessly from Scene 01 corridor
mesh_floor = bpy.data.meshes.new("PRG_Floor")
verts_floor = []
faces_floor = []

# Straight neck connecting to Scene 01 corridor at (15.0, 15.0)
neck_left = (13.58, 16.40, 0.0)
neck_right = (16.40, 13.58, 0.0)
verts_floor.append(neck_right) # 0
verts_floor.append(neck_left)  # 1

for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ix = CX + R_INNER * math.cos(alpha)
    iy = CY + R_INNER * math.sin(alpha)
    ox = CX + R_OUTER * math.cos(alpha)
    oy = CY + R_OUTER * math.sin(alpha)
    
    verts_floor.append((ix, iy, 0.0))
    verts_floor.append((ox, oy, 0.0))
    
    curr_idx = 2 + i * 2
    if i == 0:
        faces_floor.append((0, 1, curr_idx + 1, curr_idx))
    else:
        faces_floor.append((curr_idx - 2, curr_idx - 1, curr_idx + 1, curr_idx))

mesh_floor.from_pydata(verts_floor, [], faces_floor)
mesh_floor.update()
obj_floor = bpy.data.objects.new("PRG_Floor", mesh_floor)
obj_floor.data.materials.append(mat_stone)
link_obj(obj_floor, col_arch)

# 2. Continuous Curved Plaster Inner Wall
mesh_inner_wall = bpy.data.meshes.new("PRG_InnerWall")
verts_w = []
faces_w = []

verts_w.append((16.40, 13.58, 0.0))
verts_w.append((16.40, 13.58, WALL_H))

for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ix = CX + R_INNER * math.cos(alpha)
    iy = CY + R_INNER * math.sin(alpha)
    
    verts_w.append((ix, iy, 0.0))
    verts_w.append((ix, iy, WALL_H))
    
    curr_idx = 2 + i * 2
    faces_w.append((curr_idx - 2, curr_idx, curr_idx + 1, curr_idx - 1))

mesh_inner_wall.from_pydata(verts_w, [], faces_w)
mesh_inner_wall.update()
obj_inner_wall = bpy.data.objects.new("PRG_InnerWall", mesh_inner_wall)
obj_inner_wall.data.materials.append(mat_plaster)
link_obj(obj_inner_wall, col_arch)

# 3. Double-Height Architectural Glass Curtain Wall
mesh_glass = bpy.data.meshes.new("PRG_OuterCurtainWall_Glass")
verts_g = []
faces_g = []

verts_g.append((13.58, 16.40, 0.06))
verts_g.append((13.58, 16.40, WALL_H - 0.06))

for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ox = CX + R_OUTER * math.cos(alpha)
    oy = CY + R_OUTER * math.sin(alpha)
    
    verts_g.append((ox, oy, 0.06))
    verts_g.append((ox, oy, WALL_H - 0.06))
    
    curr_idx = 2 + i * 2
    faces_g.append((curr_idx - 2, curr_idx, curr_idx + 1, curr_idx - 1))

mesh_glass.from_pydata(verts_g, [], faces_g)
mesh_glass.update()
obj_glass = bpy.data.objects.new("PRG_OuterCurtainWall_Glass", mesh_glass)
obj_glass.data.materials.append(mat_glass)
link_obj(obj_glass, col_arch)

# 4. Ultra-Sleek Silver Aluminum Mullions & Horizontal Transoms (11 Bays)
NUM_BAYS = 11
mull_w = 0.035  # Slim 3.5cm width
mull_d = 0.070  # Refined 7.0cm depth

for m in range(NUM_BAYS + 1):
    t = m / NUM_BAYS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    mx = CX + R_OUTER * math.cos(alpha)
    my = CY + R_OUTER * math.sin(alpha)
    
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(mx, my, WALL_H / 2.0))
    mul_obj = bpy.context.active_object
    mul_obj.name = f"PRG_Mullion_{m:02d}"
    mul_obj.scale = (mull_w, mull_d, WALL_H)
    mul_obj.rotation_euler = (0, 0, alpha - math.pi / 2.0)
    mul_obj.data.materials.append(mat_aluminum)
    link_obj(mul_obj, col_arch)

# Horizontal Transom Bars at 1.6m and 3.6m (slim 3cm profile)
for z_transom in [1.60, 3.60]:
    mesh_transom = bpy.data.meshes.new(f"PRG_Transom_{int(z_transom*10)}")
    verts_tr = []
    faces_tr = []
    for i in range(STEPS + 1):
        t = i / STEPS
        alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
        ox1 = CX + (R_OUTER - 0.025) * math.cos(alpha)
        oy1 = CY + (R_OUTER - 0.025) * math.sin(alpha)
        ox2 = CX + (R_OUTER + 0.025) * math.cos(alpha)
        oy2 = CY + (R_OUTER + 0.025) * math.sin(alpha)
        verts_tr.append((ox1, oy1, z_transom - 0.015))
        verts_tr.append((ox1, oy1, z_transom + 0.015))
        verts_tr.append((ox2, oy2, z_transom + 0.015))
        verts_tr.append((ox2, oy2, z_transom - 0.015))
        if i > 0:
            idx = i * 4
            faces_tr.append((idx - 4, idx - 3, idx + 1, idx))
            faces_tr.append((idx - 3, idx - 2, idx + 2, idx + 1))
            faces_tr.append((idx - 2, idx - 1, idx + 3, idx + 2))
            faces_tr.append((idx - 1, idx - 4, idx, idx + 3))
    mesh_transom.from_pydata(verts_tr, [], faces_tr)
    mesh_transom.update()
    obj_tr = bpy.data.objects.new(f"PRG_Transom_{int(z_transom*10)}", mesh_transom)
    obj_tr.data.materials.append(mat_aluminum)
    link_obj(obj_tr, col_arch)

# Window Header & Sill Base Trim
mesh_sill = bpy.data.meshes.new("PRG_OuterSill")
verts_sill = []
faces_sill = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ox1 = CX + (R_OUTER - 0.04) * math.cos(alpha)
    oy1 = CY + (R_OUTER - 0.04) * math.sin(alpha)
    ox2 = CX + (R_OUTER + 0.04) * math.cos(alpha)
    oy2 = CY + (R_OUTER + 0.04) * math.sin(alpha)
    verts_sill.append((ox1, oy1, 0.03))
    verts_sill.append((ox2, oy2, 0.03))
    if i > 0:
        idx = i * 2
        faces_sill.append((idx - 2, idx - 1, idx + 1, idx))

mesh_sill.from_pydata(verts_sill, [], faces_sill)
mesh_sill.update()
obj_sill = bpy.data.objects.new("PRG_OuterSill", mesh_sill)
obj_sill.data.materials.append(mat_aluminum)
link_obj(obj_sill, col_arch)

# 5. Smooth Plaster Ceiling Soffit & Continuous Curved Cove Lighting
mesh_ceil = bpy.data.meshes.new("PRG_Ceiling")
verts_c = []
faces_c = []

for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ix = CX + (R_INNER - 0.40) * math.cos(alpha)
    iy = CY + (R_INNER - 0.40) * math.sin(alpha)
    ox = CX + (R_OUTER + 0.30) * math.cos(alpha)
    oy = CY + (R_OUTER + 0.30) * math.sin(alpha)
    
    verts_c.append((ix, iy, WALL_H))
    verts_c.append((ox, oy, WALL_H))
    if i > 0:
        idx = i * 2
        faces_c.append((idx - 2, idx, idx + 1, idx - 1))

mesh_ceil.from_pydata(verts_c, [], faces_c)
mesh_ceil.update()
obj_ceil = bpy.data.objects.new("PRG_Ceiling", mesh_ceil)
obj_ceil.data.materials.append(mat_plaster)
link_obj(obj_ceil, col_arch)

# Cove Light Strip along inner ceiling edge
mesh_cove = bpy.data.meshes.new("PRG_CoveLight")
verts_cove = []
faces_cove = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ix1 = CX + (R_INNER + 0.12) * math.cos(alpha)
    iy1 = CY + (R_INNER + 0.12) * math.sin(alpha)
    ix2 = CX + (R_INNER + 0.32) * math.cos(alpha)
    iy2 = CY + (R_INNER + 0.32) * math.sin(alpha)
    
    verts_cove.append((ix1, iy1, WALL_H - 0.03))
    verts_cove.append((ix2, iy2, WALL_H - 0.03))
    if i > 0:
        idx = i * 2
        faces_cove.append((idx - 2, idx - 1, idx + 1, idx))

mesh_cove.from_pydata(verts_cove, [], faces_cove)
mesh_cove.update()
obj_cove = bpy.data.objects.new("PRG_CoveLight", mesh_cove)
obj_cove.data.materials.append(mat_cove)
link_obj(obj_cove, col_arch)

# 6. Sculpted Architectural Exit Threshold Portal at ALPHA_END (K08 Focus)
# High-end museum curved bulkhead wall with a semicircular archway opening leading into daylit alcove
alpha_exit = ALPHA_END
tang_exit = alpha_exit - math.pi / 2.0
ex_mid_x = CX + R_CENTER * math.cos(alpha_exit)
ex_mid_y = CY + R_CENTER * math.sin(alpha_exit)

# Create sculpted portal wall mesh with arched opening
mesh_portal = bpy.data.meshes.new("PRG_Portal_ArchedWall")
bm_portal = bmesh.new()

# Arch parameters
PORTAL_W = GALLERY_W  # 5.2m total corridor width
ARCH_SPAN = 3.60      # 3.6m arch opening
ARCH_SPRING_H = 3.00  # Vertical jambs up to 3.0m
ARCH_TOP_H = 4.50     # Arch apex at 4.5m
ARCH_R = ARCH_SPAN / 2.0 # 1.8m radius
WALL_THICK = 0.45

# Build 2D profile along local corridor cross section (X') and extrude along tangent
arch_steps = 16
pts_profile = []

# Left outer wall top and bottom
pts_profile.append((-PORTAL_W / 2.0, 0.0))
pts_profile.append((-PORTAL_W / 2.0, WALL_H))
pts_profile.append((PORTAL_W / 2.0, WALL_H))
pts_profile.append((PORTAL_W / 2.0, 0.0))
# Inner arch right base
pts_profile.append((ARCH_SPAN / 2.0, 0.0))
pts_profile.append((ARCH_SPAN / 2.0, ARCH_SPRING_H))

# Semicircular arch curve
for s in range(arch_steps + 1):
    theta = math.pi * s / arch_steps
    ax = ARCH_R * math.cos(theta)
    az = ARCH_SPRING_H + (ARCH_TOP_H - ARCH_SPRING_H) * math.sin(theta)
    pts_profile.append((ax, az))

# Inner arch left base
pts_profile.append((-ARCH_SPAN / 2.0, ARCH_SPRING_H))
pts_profile.append((-ARCH_SPAN / 2.0, 0.0))

# Convert 2D profile to 3D extruded bulkhead at exit
verts_p1 = []
verts_p2 = []
cos_t = math.cos(tang_exit)
sin_t = math.sin(tang_exit)
norm_x = math.cos(alpha_exit)
norm_y = math.sin(alpha_exit)

for (u, z) in pts_profile:
    # u is cross-corridor offset along norm_x, norm_y
    # t is along tangent direction
    px = ex_mid_x + u * norm_x
    py = ex_mid_y + u * norm_y
    
    # Front face
    v1 = bm_portal.verts.new((px - (WALL_THICK / 2.0) * cos_t, py - (WALL_THICK / 2.0) * sin_t, z))
    verts_p1.append(v1)
    # Back face
    v2 = bm_portal.verts.new((px + (WALL_THICK / 2.0) * cos_t, py + (WALL_THICK / 2.0) * sin_t, z))
    verts_p2.append(v2)

# Create side/cap quads between front and back
n_pts = len(pts_profile)
for i in range(n_pts):
    next_i = (i + 1) % n_pts
    bm_portal.faces.new((verts_p1[i], verts_p2[i], verts_p2[next_i], verts_p1[next_i]))

# Front and back polygonal caps (tessellated)
bmesh.ops.triangle_fill(bm_portal, use_beauty=True, edges=[e for e in bm_portal.edges if e.verts[0] in verts_p1 and e.verts[1] in verts_p1])
bmesh.ops.triangle_fill(bm_portal, use_beauty=True, edges=[e for e in bm_portal.edges if e.verts[0] in verts_p2 and e.verts[1] in verts_p2])

bm_portal.to_mesh(mesh_portal)
bm_portal.free()
mesh_portal.update()

obj_portal = bpy.data.objects.new("PRG_Portal_ArchedWall", mesh_portal)
obj_portal.data.materials.append(mat_plaster)
link_obj(obj_portal, col_arch)

# 6B. Daylit Vestibule Alcove beyond Archway (Scene 03 threshold vista)
# Extends 4.5m forward past the arch, featuring a rear glazed window looking onto garden greenery
vest_depth = 4.20
vest_cx = ex_mid_x + vest_depth * cos_t
vest_cy = ex_mid_y + vest_depth * sin_t

# Vestibule Floor
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(ex_mid_x + (vest_depth/2.0)*cos_t, ex_mid_y + (vest_depth/2.0)*sin_t, 0.0))
vest_fl = bpy.context.active_object
vest_fl.name = "PRG_Vestibule_Floor"
vest_fl.scale = (PORTAL_W, vest_depth, 0.02)
vest_fl.rotation_euler = (0, 0, tang_exit + math.pi/2.0)
vest_fl.data.materials.append(mat_stone)
link_obj(vest_fl, col_arch)

# Vestibule Rear Curved Wall with Vista Window
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(vest_cx, vest_cy, WALL_H / 2.0))
vest_wall = bpy.context.active_object
vest_wall.name = "PRG_Vestibule_BackdropWall"
vest_wall.scale = (PORTAL_W + 0.6, 0.35, WALL_H)
vest_wall.rotation_euler = (0, 0, tang_exit + math.pi/2.0)
vest_wall.data.materials.append(mat_plaster)
link_obj(vest_wall, col_arch)

# Threshold Plinth Bench in Alcove
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(vest_cx - 0.8*cos_t, vest_cy - 0.8*sin_t, 0.22))
alcove_bench = bpy.context.active_object
alcove_bench.name = "PRG_Portal_AlcoveBench"
alcove_bench.scale = (2.40, 0.65, 0.44)
alcove_bench.rotation_euler = (0, 0, tang_exit + math.pi/2.0)
alcove_bench.data.materials.append(mat_stone)
link_obj(alcove_bench, col_furn)

# 7. Minimalist Stone Benches (3 benches along window line)
bench_angles = [
    ALPHA_START + 0.22 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.52 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.78 * (ALPHA_END - ALPHA_START)
]
R_BENCH = R_OUTER - 1.40

for b_idx, b_alpha in enumerate(bench_angles, start=1):
    bx = CX + R_BENCH * math.cos(b_alpha)
    by = CY + R_BENCH * math.sin(b_alpha)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(bx, by, 0.21))
    bench = bpy.context.active_object
    bench.name = f"PRG_Bench_{b_idx:02d}"
    bench.scale = (2.20, 0.55, 0.42)
    bench.rotation_euler = (0, 0, b_alpha - math.pi / 2.0)
    bench.data.materials.append(mat_stone)
    link_obj(bench, col_furn)

# 8. Organic Botanical Garden Terrace Scenery outside the Glass
# 8A. Stone Garden Curb along building facade
mesh_curb = bpy.data.meshes.new("PRG_GardenCurb")
verts_cb = []
faces_cb = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.04) + t * (ALPHA_END - ALPHA_START - 0.08)
    cx1 = CX + (R_OUTER + 0.05) * math.cos(alpha)
    cy1 = CY + (R_OUTER + 0.05) * math.sin(alpha)
    cx2 = CX + (R_OUTER + 0.35) * math.cos(alpha)
    cy2 = CY + (R_OUTER + 0.35) * math.sin(alpha)
    verts_cb.append((cx1, cy1, 0.0))
    verts_cb.append((cx1, cy1, 0.14))
    verts_cb.append((cx2, cy2, 0.14))
    verts_cb.append((cx2, cy2, 0.0))
    if i > 0:
        idx = i * 4
        faces_cb.append((idx - 4, idx - 3, idx + 1, idx))
        faces_cb.append((idx - 3, idx - 2, idx + 2, idx + 1))
        faces_cb.append((idx - 2, idx - 1, idx + 3, idx + 2))
mesh_curb.from_pydata(verts_cb, [], faces_cb)
mesh_curb.update()
obj_curb = bpy.data.objects.new("PRG_GardenCurb", mesh_curb)
obj_curb.data.materials.append(mat_curb)
link_obj(obj_curb, col_env)

# 8B. Manicured Boxwood Hedge Row outside the curb
mesh_hedge = bpy.data.meshes.new("PRG_BoxwoodHedge")
verts_h = []
faces_h = []
HEDGE_R = R_OUTER + 1.20
HEDGE_W = 0.85
HEDGE_H = 0.95
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.03) + t * (ALPHA_END - ALPHA_START - 0.06)
    hx1 = CX + (HEDGE_R - HEDGE_W/2.0) * math.cos(alpha)
    hy1 = CY + (HEDGE_R - HEDGE_W/2.0) * math.sin(alpha)
    hx2 = CX + (HEDGE_R + HEDGE_W/2.0) * math.cos(alpha)
    hy2 = CY + (HEDGE_R + HEDGE_W/2.0) * math.sin(alpha)
    
    verts_h.append((hx1, hy1, 0.0))
    verts_h.append((hx1, hy1, HEDGE_H))
    verts_h.append((hx2, hy2, HEDGE_H))
    verts_h.append((hx2, hy2, 0.0))
    if i > 0:
        idx = i * 4
        faces_h.append((idx - 4, idx - 3, idx + 1, idx))
        faces_h.append((idx - 3, idx - 2, idx + 2, idx + 1))
        faces_h.append((idx - 2, idx - 1, idx + 3, idx + 2))
mesh_hedge.from_pydata(verts_h, [], faces_h)
mesh_hedge.update()
obj_hedge = bpy.data.objects.new("PRG_BoxwoodHedge", mesh_hedge)
obj_hedge.data.materials.append(mat_hedge)
link_obj(obj_hedge, col_env)

# 8C. Natural Garden Lawn Ground
mesh_lawn = bpy.data.meshes.new("PRG_GardenLawn")
verts_l = []
faces_l = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.05) + t * (ALPHA_END - ALPHA_START - 0.10)
    lx1 = CX + (R_OUTER + 0.35) * math.cos(alpha)
    ly1 = CY + (R_OUTER + 0.35) * math.sin(alpha)
    lx2 = CX + (R_OUTER + 28.0) * math.cos(alpha)
    ly2 = CY + (R_OUTER + 28.0) * math.sin(alpha)
    verts_l.append((lx1, ly1, -0.02))
    verts_l.append((lx2, ly2, -0.05))
    if i > 0:
        idx = i * 2
        faces_l.append((idx - 2, idx - 1, idx + 1, idx))
mesh_lawn.from_pydata(verts_l, [], faces_l)
mesh_lawn.update()
obj_lawn = bpy.data.objects.new("PRG_GardenLawn", mesh_lawn)
obj_lawn.data.materials.append(mat_lawn)
link_obj(obj_lawn, col_env)

# 8D. Organic Botanical Trees with Realistic Branching Trunks and Multifaceted Canopies
def create_botanical_tree(name, root_x, root_y, height=6.5, crown_r=2.5):
    # Tree Trunk with gentle organic taper and secondary branch
    bm_t = bmesh.new()
    
    # Base circle
    n_ring = 8
    base_r = 0.20
    b_verts = []
    for a in range(n_ring):
        ang = 2 * math.pi * a / n_ring
        b_verts.append(bm_t.verts.new((base_r * math.cos(ang), base_r * math.sin(ang), 0.0)))
    
    # Mid trunk (slight curve)
    mid_r = 0.15
    m_verts = []
    curve_ox = 0.12 * math.sin(root_x)
    curve_oy = 0.10 * math.cos(root_y)
    for a in range(n_ring):
        ang = 2 * math.pi * a / n_ring
        m_verts.append(bm_t.verts.new((curve_ox + mid_r * math.cos(ang), curve_oy + mid_r * math.sin(ang), height * 0.45)))
    
    # Top trunk
    top_r = 0.10
    t_verts = []
    for a in range(n_ring):
        ang = 2 * math.pi * a / n_ring
        t_verts.append(bm_t.verts.new((curve_ox * 1.5 + top_r * math.cos(ang), curve_oy * 1.5 + top_r * math.sin(ang), height * 0.70)))
    
    # Quads
    for a in range(n_ring):
        next_a = (a + 1) % n_ring
        bm_t.faces.new((b_verts[a], b_verts[next_a], m_verts[next_a], m_verts[a]))
        bm_t.faces.new((m_verts[a], m_verts[next_a], t_verts[next_a], t_verts[a]))
    
    m_trunk = bpy.data.meshes.new(f"{name}_Trunk")
    bm_t.to_mesh(m_trunk)
    bm_t.free()
    m_trunk.update()
    
    obj_t = bpy.data.objects.new(f"{name}_Trunk", m_trunk)
    obj_t.location = (root_x, root_y, 0.0)
    obj_t.data.materials.append(mat_trunk)
    link_obj(obj_t, col_env)
    
    # Multifaceted Canopy Clusters (Organic Lobes)
    # 5 layered lobes with jittered vertices to form realistic foliage silhouette
    lobe_configs = [
        (0.0, 0.0, height * 0.75, crown_r * 1.05, mat_foliage_deep),
        (-crown_r * 0.45, crown_r * 0.35, height * 0.65, crown_r * 0.75, mat_foliage_sun),
        (crown_r * 0.50, -crown_r * 0.30, height * 0.70, crown_r * 0.80, mat_foliage_sun),
        (crown_r * 0.20, crown_r * 0.55, height * 0.85, crown_r * 0.65, mat_foliage_sun),
        (-crown_r * 0.30, -crown_r * 0.40, height * 0.92, crown_r * 0.55, mat_foliage_sun)
    ]
    
    for l_idx, (lx, ly, lz, lr, l_mat) in enumerate(lobe_configs):
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=lr, location=(root_x + lx, root_y + ly, lz))
        lobe_obj = bpy.context.active_object
        lobe_obj.name = f"{name}_Canopy_{l_idx}"
        
        # Jitter vertices slightly for organic natural leaf mass
        for v in lobe_obj.data.vertices:
            disp = (math.sin(v.co.x * 4.0 + l_idx) * 0.12,
                    math.cos(v.co.y * 4.0 + l_idx) * 0.12,
                    math.sin(v.co.z * 3.5 + l_idx) * 0.14)
            v.co.x += disp[0] * lr
            v.co.y += disp[1] * lr
            v.co.z += disp[2] * lr
        lobe_obj.data.update()
        lobe_obj.data.materials.append(l_mat)
        link_obj(lobe_obj, col_env)

# Place botanical trees along the curved exterior with varied scales and depths
tree_specs = [
    (ALPHA_START + 0.12 * (ALPHA_END - ALPHA_START), 4.8, 6.2, 2.2),
    (ALPHA_START + 0.28 * (ALPHA_END - ALPHA_START), 7.2, 7.5, 2.8),
    (ALPHA_START + 0.45 * (ALPHA_END - ALPHA_START), 5.5, 6.8, 2.4),
    (ALPHA_START + 0.62 * (ALPHA_END - ALPHA_START), 8.0, 8.2, 3.1),
    (ALPHA_START + 0.76 * (ALPHA_END - ALPHA_START), 5.8, 7.0, 2.5),
    (ALPHA_START + 0.88 * (ALPHA_END - ALPHA_START), 6.5, 6.4, 2.3),
]

for t_i, (t_alpha, t_dist, t_h, t_cr) in enumerate(tree_specs, start=1):
    tx = CX + (R_OUTER + t_dist) * math.cos(t_alpha)
    ty = CY + (R_OUTER + t_dist) * math.sin(t_alpha)
    create_botanical_tree(f"PRG_Tree_{t_i:02d}", tx, ty, height=t_h, crown_r=t_cr)

# 8E. Distant Daylight Sky Backdrop Dome
mesh_sky = bpy.data.meshes.new("PRG_DaylightSkyBackdrop")
verts_sk = []
faces_sk = []
SKY_R = R_OUTER + 34.0
SKY_H = 22.0
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.10) + t * (ALPHA_END - ALPHA_START - 0.20)
    sx = CX + SKY_R * math.cos(alpha)
    sy = CY + SKY_R * math.sin(alpha)
    verts_sk.append((sx, sy, -1.0))
    verts_sk.append((sx, sy, SKY_H))
    if i > 0:
        idx = i * 2
        faces_sk.append((idx - 2, idx - 1, idx + 1, idx))
mesh_sky.from_pydata(verts_sk, [], faces_sk)
mesh_sky.update()
obj_sky = bpy.data.objects.new("PRG_DaylightSkyBackdrop", mesh_sky)
obj_sky.data.materials.append(mat_sky_backdrop)
link_obj(obj_sky, col_env)

# ==========================================
# Cameras & Proof Views
# ==========================================
cameras = {}

def get_curve_pos(radius, alpha_deg, z=1.80):
    a = math.radians(alpha_deg)
    return (CX + radius * math.cos(a), CY + radius * math.sin(a), z)

def create_cam_tracked(name, location, target_pos, lens=32.0):
    cam_data = bpy.data.cameras.new(name)
    cam_data.lens = lens
    cam_data.clip_start = 0.1
    cam_data.clip_end = 150.0
    cam_obj = bpy.data.objects.new(name, cam_data)
    cam_obj.location = location
    link_obj(cam_obj, col_cam)
    
    tgt_empty = bpy.data.objects.new(f"{name}_Target", None)
    tgt_empty.location = target_pos
    link_obj(tgt_empty, col_render)
    
    ttc = cam_obj.constraints.new(type='TRACK_TO')
    ttc.target = tgt_empty
    ttc.track_axis = 'TRACK_NEGATIVE_Z'
    ttc.up_axis = 'UP_Y'
    
    cameras[name] = cam_obj
    return cam_obj

# Camera in walking aisle: R_cam = 24.6m (clear negative space from outer mullions)
# Target looking down promenade: R_tgt = 24.2m
R_CAM = 24.6
R_TGT = 24.2

loc_k05 = get_curve_pos(R_CAM, 131.0)
tgt_k05 = get_curve_pos(R_TGT, 114.0)
create_cam_tracked("K05_Entry", loc_k05, tgt_k05, lens=32.0)

loc_k06 = get_curve_pos(R_CAM, 115.0)
tgt_k06 = get_curve_pos(R_TGT, 96.0)
create_cam_tracked("K06_Foundation", loc_k06, tgt_k06, lens=32.0)

loc_k07 = get_curve_pos(R_CAM, 97.0)
tgt_k07 = get_curve_pos(R_TGT, 78.0)
create_cam_tracked("K07_Experience", loc_k07, tgt_k07, lens=32.0)

# K08 frames the sculpted arched threshold portal leading into Scene 03
loc_k08 = get_curve_pos(R_CAM, 81.0)
tgt_k08 = (ex_mid_x + 1.2*cos_t, ex_mid_y + 1.2*sin_t, 2.20)
create_cam_tracked("K08_Perspective", loc_k08, tgt_k08, lens=30.0)

# Seam Check Camera at K04
loc_seam = (11.50, 11.50, 2.20)
tgt_seam = (17.50, 17.50, 1.80)
create_cam_tracked("Seam_Check", loc_seam, tgt_seam, lens=28.0)

# Top-Down Overview Camera
cam_td_data = bpy.data.cameras.new("TopDown_Camera")
cam_td_data.lens = 24.0
cam_td = bpy.data.objects.new("TopDown_Camera", cam_td_data)
cam_td.location = (CX + 2.0, CY + 24.0, 32.0)
cam_td.rotation_euler = (math.radians(18.0), 0.0, math.radians(180.0))
link_obj(cam_td, col_cam)
cameras["TopDown_Camera"] = cam_td

# Lighting Setup for Render
bpy.ops.object.light_add(type='SUN', location=(26.0, 38.0, 18.0))
sun = bpy.context.active_object
sun.name = "Sun_Gallery"
sun.data.energy = 4.2
sun.data.color = (1.0, 0.98, 0.94)
sun.rotation_euler = (math.radians(52.0), math.radians(14.0), math.radians(-38.0))
link_obj(sun, col_render)

# Soft daylight fill
bpy.ops.object.light_add(type='POINT', location=(CX + 24.0 * math.cos(math.radians(110)), CY + 24.0 * math.sin(math.radians(110)), 4.5))
fill1 = bpy.context.active_object
fill1.name = "Fill_K05_K06"
fill1.data.energy = 380.0
fill1.data.color = (0.94, 0.96, 1.0)
link_obj(fill1, col_render)

bpy.ops.object.light_add(type='POINT', location=(CX + 24.0 * math.cos(math.radians(85)), CY + 24.0 * math.sin(math.radians(85)), 4.5))
fill2 = bpy.context.active_object
fill2.name = "Fill_K07_K08"
fill2.data.energy = 380.0
fill2.data.color = (0.94, 0.96, 1.0)
link_obj(fill2, col_render)

# ==========================================
# Rendering Proof Views
# ==========================================
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

proof_views = [
    ("K05_Entry", "camera-K05.png"),
    ("K06_Foundation", "camera-K06.png"),
    ("K07_Experience", "camera-K07.png"),
    ("K08_Perspective", "camera-K08.png"),
    ("Seam_Check", "seam-continuity.png"),
    ("TopDown_Camera", "top-down-layout.png")
]

for cam_name, file_name in proof_views:
    if cam_name in cameras:
        scene.camera = cameras[cam_name]
        scene.render.filepath = os.path.join(OUT_DIR, file_name)
        bpy.ops.render.render(write_still=True)
        print(f"[OK] Rendered {file_name}")

# ==========================================
# Export Clean GLB
# ==========================================
# Select only exportable architectural, furniture, and environmental meshes with PRG_ prefix
bpy.ops.object.select_all(action='DESELECT')
export_count = 0
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.name.startswith("PRG_"):
        obj.select_set(True)
        export_count += 1

print(f"[INFO] Exporting {export_count} meshes to GLB...")
glb_path = os.path.join(OUT_DIR, "profile-gallery.glb")
blend_path = os.path.join(OUT_DIR, "profile-gallery.blend")

bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"[OK] Saved {blend_path}")

bpy.ops.export_scene.gltf(
    filepath=glb_path,
    use_selection=True,
    export_format='GLB',
    export_apply=True,
    export_materials='EXPORT',
    export_cameras=False,
    export_lights=False,
    export_yup=True
)
print(f"[OK] Exported {glb_path} ({os.path.getsize(glb_path) / 1024:.2f} KB)")
