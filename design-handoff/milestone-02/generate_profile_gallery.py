"""
Procedural Generator for Milestone 02C: Profile Gallery (Glass & Light Museum)
Refinements:
- Sleek, slim brushed aluminum mullions (5cm x 10cm) with horizontal transoms at 1.6m and 3.8m
- 11 architectural bays along the 70-degree curve (spacious museum glazing, no dark cage bars)
- Arched threshold portal at exit (alpha=65 deg) with flush ceiling integration (no hanging beam)
- Warm polished travertine/stone floor, pristine white plaster walls, warm LED cove light channel
- Lush, sunlit botanical terrace landscape behind glass (hedges, organic canopy trees, lawn)
- Camera proof renders matching approved Visual Board V2 (K05, K06, K07, K08)
- Clean GLB export with PRG_ naming convention, 0 embedded lights/cameras
"""

import bpy
import bmesh
import math
import os

# Reset Scene
bpy.ops.wm.read_factory_settings(use_empty=True)

scene = bpy.context.scene
scene.name = "ProfileGallery_V2_Scene"
scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'RenderEngine') and 'BLENDER_EEVEE_NEXT' in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items] else 'BLENDER_EEVEE'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Color Management
scene.display_settings.display_device = 'sRGB'
scene.view_settings.view_transform = 'AgX' if 'AgX' in [v.identifier for v in scene.view_settings.bl_rna.properties['view_transform'].enum_items] else 'Filmic'
scene.view_settings.look = 'Medium High Contrast'
scene.view_settings.exposure = 0.15

# World Daylight Sky
world = bpy.data.worlds.new("PRG_DaylightWorld")
scene.world = world
world.use_nodes = True
nodes_w = world.node_tree.nodes
nodes_w.clear()
node_bg = nodes_w.new(type='ShaderNodeBackground')
node_bg.inputs['Color'].default_value = (0.88, 0.94, 0.99, 1.0)
node_bg.inputs['Strength'].default_value = 1.35
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
def create_pbr_material(name, base_color, metallic=0.0, roughness=0.5, transmission=0.0, ior=1.5, alpha=1.0):
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
        if alpha < 1.0:
            if 'Alpha' in bsdf.inputs:
                bsdf.inputs['Alpha'].default_value = alpha
            mat.blend_method = 'BLEND'
    return mat

mat_plaster = create_pbr_material("MAT_WhitePlaster", (0.98, 0.98, 0.97, 1.0), metallic=0.0, roughness=0.85)
mat_stone = create_pbr_material("MAT_LightStone", (0.95, 0.94, 0.93, 1.0), metallic=0.02, roughness=0.28)
mat_aluminum = create_pbr_material("MAT_BrushedAluminum", (0.92, 0.93, 0.95, 1.0), metallic=0.90, roughness=0.20)
mat_glass = create_pbr_material("MAT_ClearGlass", (0.96, 0.98, 1.0, 1.0), metallic=0.0, roughness=0.03, transmission=0.95, ior=1.52, alpha=0.30)
mat_greenery = create_pbr_material("MAT_LandscapeGreen", (0.42, 0.60, 0.32, 1.0), metallic=0.0, roughness=0.80)
mat_hedge = create_pbr_material("MAT_HedgeGreen", (0.28, 0.44, 0.22, 1.0), metallic=0.0, roughness=0.82)
mat_tree_trunk = create_pbr_material("MAT_TreeTrunk", (0.45, 0.40, 0.35, 1.0), metallic=0.0, roughness=0.90)

# Emission Cove Material
mat_cove = bpy.data.materials.new(name="MAT_CoveLight")
mat_cove.use_nodes = True
nodes = mat_cove.node_tree.nodes
nodes.clear()
node_out = nodes.new(type='ShaderNodeOutputMaterial')
node_emit = nodes.new(type='ShaderNodeEmission')
node_emit.inputs['Color'].default_value = (1.0, 0.97, 0.92, 1.0)
node_emit.inputs['Strength'].default_value = 3.5
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
WALL_H = 5.2

ALPHA_START = math.radians(135.0)
ALPHA_END = math.radians(65.0)
STEPS = 40

# 1. Floor Mesh: seamlessly spans between R_INNER and R_OUTER
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

# 3. Double-Height Glass Curtain Wall
mesh_glass = bpy.data.meshes.new("PRG_OuterCurtainWall_Glass")
verts_g = []
faces_g = []

verts_g.append((13.58, 16.40, 0.08))
verts_g.append((13.58, 16.40, WALL_H - 0.08))

for i in range(STEPS + 1):
    t = i / STEPS
    alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
    ox = CX + R_OUTER * math.cos(alpha)
    oy = CY + R_OUTER * math.sin(alpha)
    
    verts_g.append((ox, oy, 0.08))
    verts_g.append((ox, oy, WALL_H - 0.08))
    
    curr_idx = 2 + i * 2
    faces_g.append((curr_idx - 2, curr_idx, curr_idx + 1, curr_idx - 1))

mesh_glass.from_pydata(verts_g, [], faces_g)
mesh_glass.update()
obj_glass = bpy.data.objects.new("PRG_OuterCurtainWall_Glass", mesh_glass)
obj_glass.data.materials.append(mat_glass)
link_obj(obj_glass, col_arch)

# 4. Sleek Silver Mullions & Horizontal Transoms (11 Bays)
NUM_BAYS = 11
mull_w = 0.05  # 5cm width
mull_d = 0.10  # 10cm depth

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

# Horizontal Aluminum Transom Bars at 1.6m and 3.6m
for z_transom in [1.60, 3.60]:
    mesh_transom = bpy.data.meshes.new(f"PRG_Transom_{int(z_transom*10)}")
    verts_tr = []
    faces_tr = []
    for i in range(STEPS + 1):
        t = i / STEPS
        alpha = ALPHA_START + t * (ALPHA_END - ALPHA_START)
        ox1 = CX + (R_OUTER - 0.04) * math.cos(alpha)
        oy1 = CY + (R_OUTER - 0.04) * math.sin(alpha)
        ox2 = CX + (R_OUTER + 0.04) * math.cos(alpha)
        oy2 = CY + (R_OUTER + 0.04) * math.sin(alpha)
        verts_tr.append((ox1, oy1, z_transom - 0.025))
        verts_tr.append((ox1, oy1, z_transom + 0.025))
        verts_tr.append((ox2, oy2, z_transom + 0.025))
        verts_tr.append((ox2, oy2, z_transom - 0.025))
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
    ox1 = CX + (R_OUTER - 0.05) * math.cos(alpha)
    oy1 = CY + (R_OUTER - 0.05) * math.sin(alpha)
    ox2 = CX + (R_OUTER + 0.05) * math.cos(alpha)
    oy2 = CY + (R_OUTER + 0.05) * math.sin(alpha)
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
    ix1 = CX + (R_INNER + 0.15) * math.cos(alpha)
    iy1 = CY + (R_INNER + 0.15) * math.sin(alpha)
    ix2 = CX + (R_INNER + 0.35) * math.cos(alpha)
    iy2 = CY + (R_INNER + 0.35) * math.sin(alpha)
    
    verts_cove.append((ix1, iy1, WALL_H - 0.04))
    verts_cove.append((ix2, iy2, WALL_H - 0.04))
    if i > 0:
        idx = i * 2
        faces_cove.append((idx - 2, idx - 1, idx + 1, idx))

mesh_cove.from_pydata(verts_cove, [], faces_cove)
mesh_cove.update()
obj_cove = bpy.data.objects.new("PRG_CoveLight", mesh_cove)
obj_cove.data.materials.append(mat_cove)
link_obj(obj_cove, col_arch)

# 6. Elegant Exit Portal Wall to Scene 03 at ALPHA_END (Arched Bulkhead, NO hanging beams)
alpha_exit = ALPHA_END
ex_mid_x = CX + R_CENTER * math.cos(alpha_exit)
ex_mid_y = CY + R_CENTER * math.sin(alpha_exit)
tang_exit = alpha_exit - math.pi / 2.0

# Left and Right Portal Jambs (Flush with inner and outer walls)
jamb_w = 0.50
jamb_d = 0.40

pl_x = CX + (R_INNER + jamb_w/2.0) * math.cos(alpha_exit)
pl_y = CY + (R_INNER + jamb_w/2.0) * math.sin(alpha_exit)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(pl_x, pl_y, WALL_H / 2.0))
jamb_l = bpy.context.active_object
jamb_l.name = "PRG_Portal_JambL"
jamb_l.scale = (jamb_w, jamb_d, WALL_H)
jamb_l.rotation_euler = (0, 0, tang_exit)
jamb_l.data.materials.append(mat_plaster)
link_obj(jamb_l, col_arch)

pr_x = CX + (R_OUTER - jamb_w/2.0) * math.cos(alpha_exit)
pr_y = CY + (R_OUTER - jamb_w/2.0) * math.sin(alpha_exit)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(pr_x, pr_y, WALL_H / 2.0))
jamb_r = bpy.context.active_object
jamb_r.name = "PRG_Portal_JambR"
jamb_r.scale = (jamb_w, jamb_d, WALL_H)
jamb_r.rotation_euler = (0, 0, tang_exit)
jamb_r.data.materials.append(mat_plaster)
link_obj(jamb_r, col_arch)

# Portal Header: positioned flush at ceiling height (4.75m to 5.2m), forming a clean architectural arch
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(ex_mid_x, ex_mid_y, WALL_H - 0.22))
portal_head = bpy.context.active_object
portal_head.name = "PRG_Portal_Header"
portal_head.scale = (GALLERY_W, jamb_d, 0.45)
portal_head.rotation_euler = (0, 0, tang_exit)
portal_head.data.materials.append(mat_plaster)
link_obj(portal_head, col_arch)

# 7. Minimalist Stone Benches (3 benches along window line)
bench_angles = [
    ALPHA_START + 0.25 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.55 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.82 * (ALPHA_END - ALPHA_START)
]
R_BENCH = R_OUTER - 1.35

for b_idx, b_alpha in enumerate(bench_angles, start=1):
    bx = CX + R_BENCH * math.cos(b_alpha)
    by = CY + R_BENCH * math.sin(b_alpha)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(bx, by, 0.21))
    bench = bpy.context.active_object
    bench.name = f"PRG_Bench_{b_idx:02d}"
    bench.scale = (2.20, 0.60, 0.42)
    bench.rotation_euler = (0, 0, b_alpha - math.pi / 2.0)
    bench.data.materials.append(mat_stone)
    link_obj(bench, col_furn)

# 8. Natural Garden Terrace Scenery outside the Glass
# Manicured Terrace Lawn
mesh_lawn = bpy.data.meshes.new("PRG_LandscapeGround")
verts_l = []
faces_l = []
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.08) + t * (ALPHA_END - ALPHA_START - 0.16)
    lx1 = CX + (R_OUTER + 0.10) * math.cos(alpha)
    ly1 = CY + (R_OUTER + 0.10) * math.sin(alpha)
    lx2 = CX + (R_OUTER + 24.0) * math.cos(alpha)
    ly2 = CY + (R_OUTER + 24.0) * math.sin(alpha)
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
HEDGE_R = R_OUTER + 1.80
HEDGE_W = 1.10
HEDGE_H = 1.35
for i in range(STEPS + 1):
    t = i / STEPS
    alpha = (ALPHA_START + 0.05) + t * (ALPHA_END - ALPHA_START - 0.10)
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
obj_hedge = bpy.data.objects.new("PRG_HedgeRow", mesh_hedge)
obj_hedge.data.materials.append(mat_hedge)
link_obj(obj_hedge, col_env)

# Natural Canopy Clustered Trees
tree_angles = [
    ALPHA_START + 0.16 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.35 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.52 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.68 * (ALPHA_END - ALPHA_START),
    ALPHA_START + 0.84 * (ALPHA_END - ALPHA_START),
]
for t_idx, t_alpha in enumerate(tree_angles, start=1):
    dist = R_OUTER + 5.2 + (t_idx % 3) * 1.8
    tx = CX + dist * math.cos(t_alpha)
    ty = CY + dist * math.sin(t_alpha)
    
    # Trunk
    bpy.ops.mesh.primitive_cylinder_add(radius=0.18, depth=3.8, location=(tx, ty, 1.9))
    trunk = bpy.context.active_object
    trunk.name = f"PRG_TreeTrunk_{t_idx:02d}"
    trunk.data.materials.append(mat_tree_trunk)
    link_obj(trunk, col_env)
    
    # Canopy Clumps (Multi-spherical organic clusters)
    clump_offsets = [
        (0.0, 0.0, 4.4, 2.4),
        (-0.8, 0.6, 4.8, 1.9),
        (0.9, -0.5, 4.6, 2.1),
        (0.4, 0.8, 5.3, 1.6)
    ]
    for c_i, (ox, oy, oz, cr) in enumerate(clump_offsets):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=cr, location=(tx + ox, ty + oy, oz))
        canopy = bpy.context.active_object
        canopy.name = f"PRG_TreeCanopy_{t_idx:02d}_{c_i}"
        canopy.data.materials.append(mat_greenery)
        link_obj(canopy, col_env)

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

# Camera in walking aisle: R_cam = 24.8m (spacious clearance from walls)
# Target looking along promenade: R_tgt = 24.0m (looking down the corridor curve)
R_CAM = 24.8
R_TGT = 24.0

loc_k05 = get_curve_pos(R_CAM, 132.0)
tgt_k05 = get_curve_pos(R_TGT, 114.0)
create_cam_tracked("K05_Entry", loc_k05, tgt_k05, lens=32.0)

loc_k06 = get_curve_pos(R_CAM, 114.0)
tgt_k06 = get_curve_pos(R_TGT, 96.0)
create_cam_tracked("K06_Foundation", loc_k06, tgt_k06, lens=34.0)

loc_k07 = get_curve_pos(R_CAM, 96.0)
tgt_k07 = get_curve_pos(R_TGT, 78.0)
create_cam_tracked("K07_Experience", loc_k07, tgt_k07, lens=34.0)

loc_k08 = get_curve_pos(R_CAM, 80.0)
tgt_k08 = get_curve_pos(R_TGT, 65.0)
create_cam_tracked("K08_Perspective", loc_k08, tgt_k08, lens=32.0)

# TopDown Overview
cam_td_data = bpy.data.cameras.new("TopDown_Camera")
cam_td_data.type = 'ORTHO'
cam_td_data.ortho_scale = 36.0
cam_td_obj = bpy.data.objects.new("TopDown_Camera", cam_td_data)
cam_td_obj.location = (CX + R_CENTER * math.cos(math.radians(100.0)), CY + R_CENTER * math.sin(math.radians(100.0)), 28.0)
cam_td_obj.rotation_euler = (0, 0, 0)
link_obj(cam_td_obj, col_cam)
cameras["TopDown"] = cam_td_obj

# Seam Check
create_cam_tracked("Seam_Check", (11.5, 11.5, 2.2), (17.5, 17.5, 1.8), lens=28.0)

# ==========================================
# Daylight Museum Lighting
# ==========================================
# Warm sunlight pouring through glass curtain wall
sun_data = bpy.data.lights.new(name="Sun_Gallery", type='SUN')
sun_data.energy = 4.2
sun_data.color = (1.0, 0.98, 0.94)
sun_obj = bpy.data.objects.new("Sun_Gallery", sun_data)
sun_obj.location = (25.0, 36.0, 16.0)
sun_obj.rotation_euler = (math.radians(45.0), math.radians(18.0), math.radians(-115.0))
link_obj(sun_obj, col_render)

# Ambient daylight fill lights along corridor
fill_1 = bpy.data.lights.new(name="Fill_K05_K06", type='POINT')
fill_1.energy = 550.0
fill_1.color = (0.94, 0.97, 1.0)
fill_1_obj = bpy.data.objects.new("Fill_K05_K06", fill_1)
fill_1_obj.location = get_curve_pos(R_CENTER, 122.0, z=4.5)
link_obj(fill_1_obj, col_render)

fill_2 = bpy.data.lights.new(name="Fill_K07_K08", type='POINT')
fill_2.energy = 550.0
fill_2.color = (0.94, 0.97, 1.0)
fill_2_obj = bpy.data.objects.new("Fill_K07_K08", fill_2)
fill_2_obj.location = get_curve_pos(R_CENTER, 88.0, z=4.5)
link_obj(fill_2_obj, col_render)

# Save Native Blend
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

for cam_key, img_name in render_targets:
    cam_obj = cameras.get(cam_key)
    if cam_obj:
        scene.camera = cam_obj
        scene.render.filepath = os.path.join(out_dir, img_name)
        bpy.ops.render.render(write_still=True)
        print(f"[OK] Rendered {img_name}")

# Export GLB (Architecture, Furniture, Environment — 0 Lights/Cameras)
export_colls = [col_arch, col_furn, col_env]
export_objs = []
for c in export_colls:
    export_objs.extend(c.objects)

bpy.ops.object.select_all(action='DESELECT')
for o in export_objs:
    o.select_set(True)

out_glb = os.path.join(out_dir, "profile-gallery.glb")
bpy.ops.export_scene.gltf(
    filepath=out_glb,
    use_selection=True,
    export_format='GLB',
    export_apply=True,
    export_yup=True,
    export_materials='EXPORT',
    export_lights=False,
    export_cameras=False
)
print(f"[OK] Exported GLB: {out_glb}")

