"""
Blender Procedural Modeling Script for Scene 02: Profile Gallery V2
Project Museum — Glass & Light Museum
Milestone 02A Deliverable

Creates:
- PRG_WorldRoot
- PRG_Architecture:
    - PRG_Floor (seamlessly joining Scene 01 corridor at X=15.0, Y=15.0)
    - PRG_InnerWall (smooth plaster wall with curved coves)
    - PRG_OuterCurtainWall_Glass (tall floor-to-ceiling clear glazing)
    - PRG_Mullion_00..PRG_Mullion_16 (slim brushed-silver mullions)
    - PRG_Ceiling (soffit with recessed cove lighting)
    - PRG_CoveLight (warm-neutral continuous strip luminaire)
    - PRG_Threshold_PostL, PRG_Threshold_PostR, PRG_Threshold_Header (exit portal to Scene 03)
- PRG_Furniture:
    - PRG_Bench_01, PRG_Bench_02, PRG_Bench_03 (minimalist light stone benches)
- PRG_Environment:
    - PRG_LandscapeGround (terrace grass lawn outside glazing)
    - PRG_HedgeRow (ornamental green hedge terrace)
- PRG_CameraGuides:
    - K05_Entry, K06_Foundation, K07_Experience, K08_Perspective, TopDown_Overview, Seam_Check
- PRG_RenderOnly:
    - Daylight Sun, Sky Fill, Gallery Accent Lights
"""

import bpy
import math
import os

# Clear scene
bpy.ops.wm.read_factory_settings(use_empty=True)

scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

# Render settings: EEVEE Next
scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'BLENDER_EEVEE_NEXT') else 'BLENDER_EEVEE'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.color_mode = 'RGBA'
scene.render.image_settings.color_depth = '8'

if hasattr(scene, 'eevee'):
    scene.eevee.use_shadows = True

# Setup bright daylight World background
world = bpy.data.worlds.new("PRG_DaylightWorld")
scene.world = world
world.use_nodes = True
bg_node = world.node_tree.nodes.get('Background')
if bg_node:
    bg_node.inputs['Color'].default_value = (0.87, 0.93, 0.99, 1.0) # Pale daylight sky
    bg_node.inputs['Strength'].default_value = 1.8

# Create Collections
def get_or_create_col(name, parent=None):
    if name in bpy.data.collections:
        col = bpy.data.collections[name]
    else:
        col = bpy.data.collections.new(name)
        if parent:
            parent.children.link(col)
        else:
            scene.collection.children.link(col)
    return col

col_root = get_or_create_col("PRG_WorldRoot")
col_arch = get_or_create_col("PRG_Architecture", col_root)
col_furn = get_or_create_col("PRG_Furniture", col_root)
col_env = get_or_create_col("PRG_Environment", col_root)
col_cam = get_or_create_col("PRG_CameraGuides", col_root)
col_render = get_or_create_col("PRG_RenderOnly", col_root)

def link_obj(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)

# Materials
def create_pbr_material(name, base_color, metallic=0.0, roughness=0.5, transmission=0.0, ior=1.45, alpha=1.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Metallic'].default_value = metallic
        bsdf.inputs['Roughness'].default_value = roughness
        if 'Transmission Weight' in bsdf.inputs:
            bsdf.inputs['Transmission Weight'].default_value = transmission
        elif 'Transmission' in bsdf.inputs:
            bsdf.inputs['Transmission'].default_value = transmission
        if 'IOR' in bsdf.inputs:
            bsdf.inputs['IOR'].default_value = ior
        if alpha < 1.0:
            if 'Alpha' in bsdf.inputs:
                bsdf.inputs['Alpha'].default_value = alpha
            mat.blend_method = 'BLEND'
    return mat

mat_plaster = create_pbr_material("MAT_WhitePlaster", (0.972, 0.975, 0.968, 1.0), metallic=0.0, roughness=0.82)
mat_stone = create_pbr_material("MAT_LightStone", (0.945, 0.948, 0.942, 1.0), metallic=0.02, roughness=0.38)
mat_aluminum = create_pbr_material("MAT_BrushedAluminum", (0.880, 0.900, 0.915, 1.0), metallic=0.85, roughness=0.28)
mat_glass = create_pbr_material("MAT_ClearGlass", (0.920, 0.960, 0.990, 1.0), metallic=0.0, roughness=0.05, transmission=0.92, ior=1.52, alpha=0.30)
mat_greenery = create_pbr_material("MAT_LandscapeGreen", (0.32, 0.54, 0.28, 1.0), metallic=0.0, roughness=0.75)
mat_hedge = create_pbr_material("MAT_HedgeGreen", (0.24, 0.44, 0.20, 1.0), metallic=0.0, roughness=0.82)

# Emission cove
mat_cove = bpy.data.materials.new(name="MAT_CoveLight")
mat_cove.use_nodes = True
nodes = mat_cove.node_tree.nodes
nodes.clear()
node_out = nodes.new(type='ShaderNodeOutputMaterial')
node_emit = nodes.new(type='ShaderNodeEmission')
node_emit.inputs['Color'].default_value = (1.0, 0.985, 0.95, 1.0)
node_emit.inputs['Strength'].default_value = 2.8
mat_cove.node_tree.links.new(node_emit.outputs['Emission'], node_out.inputs['Surface'])

# ==========================================
# Geometry Generation: Curved Gallery Corridor
# ==========================================
CX = 32.677695
CY = -2.677695
R_CENTER = 25.0
GALLERY_W = 5.2
R_INNER = R_CENTER - GALLERY_W / 2.0  # 22.4m
R_OUTER = R_CENTER + GALLERY_W / 2.0  # 27.6m
WALL_H = 5.2

ALPHA_START = math.radians(135.0)
ALPHA_END = math.radians(65.0)
STEPS = 36

# 1. Floor Mesh: seamlessly spans between R_INNER and R_OUTER
mesh_floor = bpy.data.meshes.new("PRG_Floor")
verts_floor = []
faces_floor = []

# Straight neck connecting to Scene 01 corridor at (15.0, 15.0)
# Scene 01 corridor left wall is at (13.58, 16.40), right wall is at (16.40, 13.58)
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
        # Connect neck to first arc ring
        faces_floor.append((0, 1, curr_idx + 1, curr_idx))
    else:
        faces_floor.append((curr_idx - 2, curr_idx - 1, curr_idx + 1, curr_idx))

mesh_floor.from_pydata(verts_floor, [], faces_floor)
mesh_floor.update()
obj_floor = bpy.data.objects.new("PRG_Floor", mesh_floor)
obj_floor.data.materials.append(mat_stone)
link_obj(obj_floor, col_arch)

# 2. Inner Wall (Plaster wall with cove ceiling)
mesh_iwall = bpy.data.meshes.new("PRG_InnerWall")
verts_iw = []
faces_iw = []

for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ix = CX + R_INNER * math.cos(alpha)
    iy = CY + R_INNER * math.sin(alpha)
    ix_back = CX + (R_INNER - 0.40) * math.cos(alpha)
    iy_back = CY + (R_INNER - 0.40) * math.sin(alpha)
    
    verts_iw.append((ix, iy, 0.0))
    verts_iw.append((ix, iy, WALL_H))
    verts_iw.append((ix_back, iy_back, WALL_H))
    verts_iw.append((ix_back, iy_back, 0.0))
    
    if i > 0:
        b0 = (i - 1) * 4
        b1 = i * 4
        faces_iw.append((b0 + 0, b1 + 0, b1 + 1, b0 + 1))
        faces_iw.append((b0 + 1, b1 + 1, b1 + 2, b0 + 2))
        faces_iw.append((b0 + 2, b1 + 2, b1 + 3, b0 + 3))

mesh_iwall.from_pydata(verts_iw, [], faces_iw)
mesh_iwall.update()
obj_iwall = bpy.data.objects.new("PRG_InnerWall", mesh_iwall)
obj_iwall.data.materials.append(mat_plaster)
link_obj(obj_iwall, col_arch)

# 3. Outer Curtain Wall (Clear Glass Panels)
mesh_glass = bpy.data.meshes.new("PRG_OuterCurtainWall_Glass")
verts_g = []
faces_g = []

for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ox = CX + R_OUTER * math.cos(alpha)
    oy = CY + R_OUTER * math.sin(alpha)
    
    verts_g.append((ox, oy, 0.08))
    verts_g.append((ox, oy, WALL_H - 0.08))
    
    if i > 0:
        idx = i * 2
        faces_g.append((idx - 2, idx, idx + 1, idx - 1))

mesh_glass.from_pydata(verts_g, [], faces_g)
mesh_glass.update()
obj_glass = bpy.data.objects.new("PRG_OuterCurtainWall_Glass", mesh_glass)
obj_glass.data.materials.append(mat_glass)
link_obj(obj_glass, col_arch)

# 4. Slim Brushed Aluminum Mullions along the glass facade
NUM_MULLIONS = 18
for m in range(NUM_MULLIONS + 1):
    t = m / NUM_MULLIONS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    mx = CX + R_OUTER * math.cos(alpha)
    my = CY + R_OUTER * math.sin(alpha)
    
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(mx, my, WALL_H / 2.0))
    mul_obj = bpy.context.active_object
    mul_obj.name = f"PRG_Mullion_{m:02d}"
    mul_obj.scale = (0.06, 0.12, WALL_H)
    mul_obj.rotation_euler = (0, 0, alpha - math.pi / 2.0)
    mul_obj.data.materials.append(mat_aluminum)
    link_obj(mul_obj, col_arch)

# Window Header and Sill Channels
mesh_sill = bpy.data.meshes.new("PRG_OuterSill")
verts_sill = []
faces_sill = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ox1 = CX + (R_OUTER - 0.06) * math.cos(alpha)
    oy1 = CY + (R_OUTER - 0.06) * math.sin(alpha)
    ox2 = CX + (R_OUTER + 0.06) * math.cos(alpha)
    oy2 = CY + (R_OUTER + 0.06) * math.sin(alpha)
    
    verts_sill.append((ox1, oy1, 0.04))
    verts_sill.append((ox2, oy2, 0.04))
    if i > 0:
        idx = i * 2
        faces_sill.append((idx - 2, idx - 1, idx + 1, idx))

mesh_sill.from_pydata(verts_sill, [], faces_sill)
mesh_sill.update()
obj_sill = bpy.data.objects.new("PRG_OuterSill", mesh_sill)
obj_sill.data.materials.append(mat_aluminum)
link_obj(obj_sill, col_arch)

# 5. Ceiling Soffit & Recessed Cove Lighting
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
    ix1 = CX + (R_INNER + 0.20) * math.cos(alpha)
    iy1 = CY + (R_INNER + 0.20) * math.sin(alpha)
    ix2 = CX + (R_INNER + 0.45) * math.cos(alpha)
    iy2 = CY + (R_INNER + 0.45) * math.sin(alpha)
    
    verts_cove.append((ix1, iy1, WALL_H - 0.05))
    verts_cove.append((ix2, iy2, WALL_H - 0.05))
    if i > 0:
        idx = i * 2
        faces_cove.append((idx - 2, idx - 1, idx + 1, idx))

mesh_cove.from_pydata(verts_cove, [], faces_cove)
mesh_cove.update()
obj_cove = bpy.data.objects.new("PRG_CoveLight", mesh_cove)
obj_cove.data.materials.append(mat_cove)
link_obj(obj_cove, col_arch)

# 6. Exit Threshold Portal to Scene 03 at ALPHA_END
alpha_exit = ALPHA_END
ex_mid_x = CX + R_CENTER * math.cos(alpha_exit)
ex_mid_y = CY + R_CENTER * math.sin(alpha_exit)
tang_exit = alpha_exit - math.pi / 2.0

post_w = 0.35
post_d = 0.40
post_h = WALL_H

pl_x = CX + (R_INNER) * math.cos(alpha_exit)
pl_y = CY + (R_INNER) * math.sin(alpha_exit)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(pl_x, pl_y, post_h / 2.0))
post_l = bpy.context.active_object
post_l.name = "PRG_Threshold_PostL"
post_l.scale = (post_w, post_d, post_h)
post_l.rotation_euler = (0, 0, tang_exit)
post_l.data.materials.append(mat_aluminum)
link_obj(post_l, col_arch)

pr_x = CX + (R_OUTER) * math.cos(alpha_exit)
pr_y = CY + (R_OUTER) * math.sin(alpha_exit)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(pr_x, pr_y, post_h / 2.0))
post_r = bpy.context.active_object
post_r.name = "PRG_Threshold_PostR"
post_r.scale = (post_w, post_d, post_h)
post_r.rotation_euler = (0, 0, tang_exit)
post_r.data.materials.append(mat_aluminum)
link_obj(post_r, col_arch)

bpy.ops.mesh.primitive_cube_add(size=1.0, location=(ex_mid_x, ex_mid_y, post_h - 0.15))
header = bpy.context.active_object
header.name = "PRG_Threshold_Header"
header.scale = (GALLERY_W + 0.35, post_d, 0.30)
header.rotation_euler = (0, 0, tang_exit)
header.data.materials.append(mat_aluminum)
link_obj(header, col_arch)

# 7. Gallery Furniture: 3 Minimalist Architectural Stone Benches along Window Line
bench_angles = [
    ALPHA_START + 0.28 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.55 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.82 * (ALPHA_END - ALPHA_START)
]
R_BENCH = R_OUTER - 1.40

for b_idx, b_alpha in enumerate(bench_angles, start=1):
    bx = CX + R_BENCH * math.cos(b_alpha)
    by = CY + R_BENCH * math.sin(b_alpha)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(bx, by, 0.21))
    bench = bpy.context.active_object
    bench.name = f"PRG_Bench_{b_idx:02d}"
    bench.scale = (2.40, 0.65, 0.42)
    bench.rotation_euler = (0, 0, b_alpha - math.pi / 2.0)
    bench.data.materials.append(mat_stone)
    link_obj(bench, col_furn)

# 8. Landscape Environment outside Curtain Glazing
# Terrace Lawn
mesh_lawn = bpy.data.meshes.new("PRG_LandscapeGround")
verts_l = []
faces_l = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.08) + t * (ALPHA_END - ALPHA_START - 0.16)
    lx1 = CX + (R_OUTER + 0.1) * math.cos(alpha)
    ly1 = CY + (R_OUTER + 0.1) * math.sin(alpha)
    lx2 = CX + (R_OUTER + 16.0) * math.cos(alpha)
    ly2 = CY + (R_OUTER + 16.0) * math.sin(alpha)
    verts_l.append((lx1, ly1, -0.02))
    verts_l.append((lx2, ly2, -0.02))
    if i > 0:
        idx = i * 2
        faces_l.append((idx - 2, idx - 1, idx + 1, idx))

mesh_lawn.from_pydata(verts_l, [], faces_l)
mesh_lawn.update()
obj_lawn = bpy.data.objects.new("PRG_LandscapeGround", mesh_lawn)
obj_lawn.data.materials.append(mat_greenery)
link_obj(obj_lawn, col_env)

# Continuous curved hedge row outside
mesh_hedge = bpy.data.meshes.new("PRG_HedgeRow")
verts_h = []
faces_h = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.06) + t * (ALPHA_END - ALPHA_START - 0.12)
    hx1 = CX + (R_OUTER + 3.2) * math.cos(alpha)
    hy1 = CY + (R_OUTER + 3.2) * math.sin(alpha)
    hx2 = CX + (R_OUTER + 4.5) * math.cos(alpha)
    hy2 = CY + (R_OUTER + 4.5) * math.sin(alpha)
    
    base = i * 4
    verts_h.append((hx1, hy1, 0.0))
    verts_h.append((hx1, hy1, 1.25))
    verts_h.append((hx2, hy2, 1.25))
    verts_h.append((hx2, hy2, 0.0))
    if i > 0:
        b0 = (i - 1) * 4
        b1 = i * 4
        faces_h.append((b0 + 0, b1 + 0, b1 + 1, b0 + 1))
        faces_h.append((b0 + 1, b1 + 1, b1 + 2, b0 + 2))
        faces_h.append((b0 + 2, b1 + 2, b1 + 3, b0 + 3))

mesh_hedge.from_pydata(verts_h, [], faces_h)
mesh_hedge.update()
obj_hedge = bpy.data.objects.new("PRG_HedgeRow", mesh_hedge)
obj_hedge.data.materials.append(mat_hedge)
link_obj(obj_hedge, col_env)

# Decorative trees outside
for tr in range(6):
    tr_t = tr / 5.0
    tr_alpha = (ALPHA_START + 0.08) + tr_t * (ALPHA_END - ALPHA_START - 0.16)
    tr_dist = R_OUTER + 8.5 + (tr % 2) * 3.0
    tx = CX + tr_dist * math.cos(tr_alpha)
    ty = CY + tr_dist * math.sin(tr_alpha)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=2.4 + (tr % 2) * 0.6, location=(tx, ty, 2.8))
    tree_obj = bpy.context.active_object
    tree_obj.name = f"PRG_TreeFoliage_{tr:02d}"
    tree_obj.data.materials.append(mat_hedge)
    link_obj(tree_obj, col_env)

# ==========================================
# Camera Setup: K05, K06, K07, K08 & TopDown
# ==========================================
cameras = {}

def create_cam_tracked(name, loc, target, lens=32.0, clip_start=0.1, clip_end=150.0):
    cam_data = bpy.data.cameras.new(name)
    cam_data.lens = lens
    cam_data.clip_start = clip_start
    cam_data.clip_end = clip_end
    
    cam_obj = bpy.data.objects.new(name, cam_data)
    cam_obj.location = loc
    link_obj(cam_obj, col_cam)
    
    # Target empty
    tgt_empty = bpy.data.objects.new(f"{name}_Target", None)
    tgt_empty.location = target
    link_obj(tgt_empty, col_cam)
    
    # TrackTo constraint
    tt = cam_obj.constraints.new(type='TRACK_TO')
    tt.target = tgt_empty
    tt.track_axis = 'TRACK_NEGATIVE_Z'
    tt.up_axis = 'UP_Y'
    
    cameras[name] = cam_obj
    return cam_obj

# Camera radius: R_cam = 24.6m (walking aisle)
# Target radius: R_tgt = 25.4m (looking along curve)
R_CAM = 24.6
R_TGT = 25.4
CAM_Z = 1.80

def get_curve_pos(radius, alpha_deg, z=1.80):
    a = math.radians(alpha_deg)
    return (CX + radius * math.cos(a), CY + radius * math.sin(a), z)

# K05 Entry: exactly matches K04 end heading, at start of gallery curve
loc_k05 = get_curve_pos(R_CAM, 134.0)
tgt_k05 = get_curve_pos(R_TGT, 116.0)
create_cam_tracked("K05_Entry", loc_k05, tgt_k05, lens=32.0)

# K06 Foundation: forward dolly beside floor-to-ceiling glass
loc_k06 = get_curve_pos(R_CAM, 116.0)
tgt_k06 = get_curve_pos(R_TGT, 98.0)
create_cam_tracked("K06_Foundation", loc_k06, tgt_k06, lens=35.0)

# K07 Experience: mid-gallery curved perspective
loc_k07 = get_curve_pos(R_CAM, 98.0)
tgt_k07 = get_curve_pos(R_TGT, 80.0)
create_cam_tracked("K07_Experience", loc_k07, tgt_k07, lens=35.0)

# K08 Perspective: exit threshold looking into Scene 03 opening
loc_k08 = get_curve_pos(R_CAM, 80.0)
tgt_k08 = get_curve_pos(R_TGT, 65.0)
create_cam_tracked("K08_Perspective", loc_k08, tgt_k08, lens=32.0)

# Top-Down Overview camera
cam_td_data = bpy.data.cameras.new("TopDown_Camera")
cam_td_data.type = 'ORTHO'
cam_td_data.ortho_scale = 36.0
cam_td_data.clip_start = 0.1
cam_td_data.clip_end = 100.0
cam_td_obj = bpy.data.objects.new("TopDown_Camera", cam_td_data)
# Centered over gallery curve
cam_td_obj.location = (CX + R_CENTER * math.cos(math.radians(100.0)), CY + R_CENTER * math.sin(math.radians(100.0)), 28.0)
cam_td_obj.rotation_euler = (0, 0, 0)
link_obj(cam_td_obj, col_cam)
cameras["TopDown"] = cam_td_obj

# Seam Check camera looking from corridor neck into gallery
create_cam_tracked("Seam_Check", (11.5, 11.5, 2.2), (17.5, 17.5, 1.8), lens=28.0)

# ==========================================
# Lighting (Daylight Sun & Gallery Fill)
# ==========================================
# 1. Warm natural sun coming through the glass curtain wall
sun_data = bpy.data.lights.new(name="Sun_Gallery", type='SUN')
sun_data.energy = 3.5
sun_data.color = (1.0, 0.985, 0.95)
sun_obj = bpy.data.objects.new("Sun_Gallery", sun_data)
sun_obj.location = (25.0, 36.0, 16.0)
sun_obj.rotation_euler = (math.radians(45.0), math.radians(18.0), math.radians(-115.0))
link_obj(sun_obj, col_render)

# 2. Ambient daylight sky fill
fill_1 = bpy.data.lights.new(name="Fill_K05_K06", type='POINT')
fill_1.energy = 600.0
fill_1.color = (0.92, 0.96, 1.0)
fill_1_obj = bpy.data.objects.new("Fill_K05_K06", fill_1)
fill_1_obj.location = get_curve_pos(R_CENTER, 122.0, z=4.5)
link_obj(fill_1_obj, col_render)

fill_2 = bpy.data.lights.new(name="Fill_K07_K08", type='POINT')
fill_2.energy = 600.0
fill_2.color = (0.92, 0.96, 1.0)
fill_2_obj = bpy.data.objects.new("Fill_K07_K08", fill_2)
fill_2_obj.location = get_curve_pos(R_CENTER, 88.0, z=4.5)
link_obj(fill_2_obj, col_render)

# Save Native Blend File
out_dir = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-02"
out_blend = os.path.join(out_dir, "profile-gallery.blend")
bpy.ops.wm.save_as_mainfile(filepath=out_blend)
print(f"[OK] Saved Blender scene: {out_blend}")

# Render Camera Proofs
render_targets = [
    ("K05_Entry", "camera-K05.png"),
    ("K06_Foundation", "camera-K06.png"),
    ("K07_Experience", "camera-K07.png"),
    ("K08_Perspective", "camera-K08.png"),
    ("TopDown", "top-down-layout.png"),
    ("Seam_Check", "seam-continuity.png")
]

for cam_name, fn in render_targets:
    cam_obj = cameras.get(cam_name)
    if cam_obj:
        scene.camera = cam_obj
        if cam_name == "TopDown":
            obj_ceil.hide_render = True
        else:
            obj_ceil.hide_render = False
            
        render_path = os.path.join(out_dir, fn)
        scene.render.filepath = render_path
        bpy.ops.render.render(write_still=True)
        print(f"[OK] Rendered {cam_name} -> {render_path}")

# Export GLB (Architecture, Furniture, Environment only; no cameras/lights)
export_cols = [col_arch, col_furn, col_env]
for obj in bpy.data.objects:
    obj.select_set(False)

for c in export_cols:
    for obj in c.objects:
        obj.select_set(True)

out_glb = os.path.join(out_dir, "profile-gallery.glb")
bpy.ops.export_scene.gltf(
    filepath=out_glb,
    use_selection=True,
    export_format='GLB',
    export_apply=True,
    export_cameras=False,
    export_lights=False,
    export_yup=True
)
print(f"[OK] Exported GLB: {out_glb}")
