import bpy
import bmesh
import math
import os

# Clean slate
bpy.ops.wm.read_factory_settings(use_empty=True)

scene = bpy.context.scene
scene.name = "Scene03_Design_Review"
scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'RenderEngine') and 'BLENDER_EEVEE_NEXT' in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items] else 'BLENDER_EEVEE'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Color Management
scene.display_settings.display_device = 'sRGB'
scene.view_settings.view_transform = 'AgX' if 'AgX' in [v.identifier for v in scene.view_settings.bl_rna.properties['view_transform'].enum_items] else 'Filmic'
scene.view_settings.look = 'Medium High Contrast'
scene.view_settings.exposure = 0.20

# World Daylight Sky
world = bpy.data.worlds.new("EXP_DaylightWorld")
scene.world = world
world.use_nodes = True
nw = world.node_tree.nodes
nw.clear()
n_bg = nw.new(type='ShaderNodeBackground')
n_bg.inputs['Color'].default_value = (0.92, 0.96, 1.0, 1.0)
n_bg.inputs['Strength'].default_value = 1.6
n_out = nw.new(type='ShaderNodeOutputWorld')
world.node_tree.links.new(n_bg.outputs['Background'], n_out.inputs['Surface'])

# Collections
col_arch = bpy.data.collections.new("01_Architecture")
col_struct = bpy.data.collections.new("02_Structure")
col_cam = bpy.data.collections.new("03_Cameras")
scene.collection.children.link(col_arch)
scene.collection.children.link(col_struct)
scene.collection.children.link(col_cam)

def link_obj(obj, col):
    if obj.name not in col.objects:
        col.objects.link(obj)

# PBR Materials
def make_pbr(name, color, metallic=0.0, roughness=0.5, transmission=0.0, emission=(0,0,0,1), emission_strength=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        if 'Base Color' in bsdf.inputs: bsdf.inputs['Base Color'].default_value = color
        if 'Metallic' in bsdf.inputs: bsdf.inputs['Metallic'].default_value = metallic
        if 'Roughness' in bsdf.inputs: bsdf.inputs['Roughness'].default_value = roughness
        if 'Transmission Weight' in bsdf.inputs: bsdf.inputs['Transmission Weight'].default_value = transmission
        elif 'Transmission' in bsdf.inputs: bsdf.inputs['Transmission'].default_value = transmission
        if emission_strength > 0:
            if 'Emission Color' in bsdf.inputs: bsdf.inputs['Emission Color'].default_value = emission
            elif 'Emission' in bsdf.inputs: bsdf.inputs['Emission'].default_value = emission
            if 'Emission Strength' in bsdf.inputs: bsdf.inputs['Emission Strength'].default_value = emission_strength
    return mat

mat_plaster = make_pbr("MAT_EXP_WhitePlaster", (0.97, 0.97, 0.96, 1.0), metallic=0.0, roughness=0.82)
mat_stone = make_pbr("MAT_EXP_TravertineStone", (0.96, 0.95, 0.93, 1.0), metallic=0.02, roughness=0.20)
mat_aluminum = make_pbr("MAT_EXP_BrushedAluminum", (0.94, 0.95, 0.97, 1.0), metallic=0.78, roughness=0.22)
mat_glass = make_pbr("MAT_EXP_ClearGlass", (0.96, 0.98, 1.0, 1.0), metallic=0.0, roughness=0.02, transmission=0.96)
mat_cove = make_pbr("MAT_EXP_CoveLight", (1.0, 0.97, 0.92, 1.0), emission=(1.0, 0.97, 0.92, 1.0), emission_strength=4.5)

# Rotunda Dimensions
CX = 58.00
CY = 13.00
R_ROT = 12.00
WALL_H = 6.80
DOME_TOP_H = 8.20
OCULUS_R = 4.00

# 1. Travertine Floor (Mesh Circle with radial subdivisions)
mesh_floor = bpy.data.meshes.new("EXP_Floor_Travertine")
bm = bmesh.new()
# Center ring and outer rings
rings = [0.0, 4.0, 8.0, 12.0]
verts_by_ring = []
NSEG = 48
for r in rings:
    ring_verts = []
    for s in range(NSEG):
        theta = 2.0 * math.pi * s / NSEG
        vx = CX + r * math.cos(theta)
        vy = CY + r * math.sin(theta)
        ring_verts.append(bm.verts.new((vx, vy, 0.0)))
    verts_by_ring.append(ring_verts)

for ri in range(len(rings) - 1):
    r1 = verts_by_ring[ri]
    r2 = verts_by_ring[ri + 1]
    for s in range(NSEG):
        next_s = (s + 1) % NSEG
        bm.faces.new((r1[s], r2[s], r2[next_s], r1[next_s]))

bm.to_mesh(mesh_floor)
bm.free()
mesh_floor.update()
obj_floor = bpy.data.objects.new("EXP_Floor_Travertine", mesh_floor)
obj_floor.data.materials.append(mat_stone)
link_obj(obj_floor, col_arch)

# 1B. Radial Floor Inlay Strips (brushed aluminum)
mesh_inlay = bpy.data.meshes.new("EXP_Floor_Inlays")
bm_in = bmesh.new()
for s in range(0, NSEG, 2):
    theta = 2.0 * math.pi * s / NSEG
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    norm_x = -sin_t
    norm_y = cos_t
    w = 0.015 # 1.5cm width
    v1 = bm_in.verts.new((CX + 3.9 * cos_t - w * norm_x, CY + 3.9 * sin_t - w * norm_y, 0.002))
    v2 = bm_in.verts.new((CX + 3.9 * cos_t + w * norm_x, CY + 3.9 * sin_t + w * norm_y, 0.002))
    v3 = bm_in.verts.new((CX + 11.9 * cos_t + w * norm_x, CY + 11.9 * sin_t + w * norm_y, 0.002))
    v4 = bm_in.verts.new((CX + 11.9 * cos_t - w * norm_x, CY + 11.9 * sin_t - w * norm_y, 0.002))
    bm_in.faces.new((v1, v2, v3, v4))
bm_in.to_mesh(mesh_inlay)
bm_in.free()
mesh_inlay.update()
obj_inlay = bpy.data.objects.new("EXP_Floor_Inlays", mesh_inlay)
obj_inlay.data.materials.append(mat_aluminum)
link_obj(obj_inlay, col_struct)

# 2. Perimeter Wall with Openings (Entry Portal, Exit Portal, Business Analysis Alcove, Clerestory)
mesh_wall = bpy.data.meshes.new("EXP_Wall_Perimeter")
bm_w = bmesh.new()
THICK = 0.40

# We create cylindrical wall segments
for s in range(NSEG):
    theta1 = 2.0 * math.pi * s / NSEG
    theta2 = 2.0 * math.pi * (s + 1) / NSEG
    
    # Deg angles
    deg1 = math.degrees(theta1) % 360
    
    # Entrance from Scene 02 is around 205 deg (west-southwest)
    # Exit toward Scene 04 is around 335 deg (east-southeast)
    # Business Analysis alcove is around 140-165 deg (northwest)
    # SAP Colonnade is around 45-115 deg (north)
    
    is_entry = (195 <= deg1 <= 215)
    is_exit = (325 <= deg1 <= 345)
    is_alcove = (140 <= deg1 <= 165)
    is_colonnade = (45 <= deg1 <= 115)
    
    r_in = R_ROT
    r_out = R_ROT + THICK
    
    if is_entry or is_exit:
        # Lintel wall above archway (H from 4.8m to 6.8m)
        h_base = 4.80
    elif is_alcove:
        # Deep alcove wall pushed back by 1.8m
        r_in = R_ROT + 1.80
        r_out = R_ROT + 1.80 + THICK
        h_base = 0.0
    elif is_colonnade:
        # Lower parapet wall up to 0.8m, then clerestory glass from 0.8m to 6.8m
        h_base = 0.0
        # Lower knee wall
        v1 = bm_w.verts.new((CX + r_in * math.cos(theta1), CY + r_in * math.sin(theta1), 0.0))
        v2 = bm_w.verts.new((CX + r_out * math.cos(theta1), CY + r_out * math.sin(theta1), 0.0))
        v3 = bm_w.verts.new((CX + r_out * math.cos(theta2), CY + r_out * math.sin(theta2), 0.0))
        v4 = bm_w.verts.new((CX + r_in * math.cos(theta2), CY + r_in * math.sin(theta2), 0.0))
        v1b = bm_w.verts.new((CX + r_in * math.cos(theta1), CY + r_in * math.sin(theta1), 0.8))
        v2b = bm_w.verts.new((CX + r_out * math.cos(theta1), CY + r_out * math.sin(theta1), 0.8))
        v3b = bm_w.verts.new((CX + r_out * math.cos(theta2), CY + r_out * math.sin(theta2), 0.8))
        v4b = bm_w.verts.new((CX + r_in * math.cos(theta2), CY + r_in * math.sin(theta2), 0.8))
        bm_w.faces.new((v1, v4, v4b, v1b))
        bm_w.faces.new((v2, v2b, v3b, v3))
        bm_w.faces.new((v1b, v4b, v3b, v2b))
        h_base = 6.20 # Upper architrave beam
    else:
        h_base = 0.0

    # Solid wall section from h_base to WALL_H
    v_b1 = bm_w.verts.new((CX + r_in * math.cos(theta1), CY + r_in * math.sin(theta1), h_base))
    v_b2 = bm_w.verts.new((CX + r_out * math.cos(theta1), CY + r_out * math.sin(theta1), h_base))
    v_b3 = bm_w.verts.new((CX + r_out * math.cos(theta2), CY + r_out * math.sin(theta2), h_base))
    v_b4 = bm_w.verts.new((CX + r_in * math.cos(theta2), CY + r_in * math.sin(theta2), h_base))
    
    v_t1 = bm_w.verts.new((CX + r_in * math.cos(theta1), CY + r_in * math.sin(theta1), WALL_H))
    v_t2 = bm_w.verts.new((CX + r_out * math.cos(theta1), CY + r_out * math.sin(theta1), WALL_H))
    v_t3 = bm_w.verts.new((CX + r_out * math.cos(theta2), CY + r_out * math.sin(theta2), WALL_H))
    v_t4 = bm_w.verts.new((CX + r_in * math.cos(theta2), CY + r_in * math.sin(theta2), WALL_H))
    
    # Inner face
    bm_w.faces.new((v_b1, v_b4, v_t4, v_t1))
    # Outer face
    bm_w.faces.new((v_b2, v_t2, v_t3, v_b3))
    # Top face
    bm_w.faces.new((v_t1, v_t4, v_t3, v_t2))

bm_w.to_mesh(mesh_wall)
bm_w.free()
mesh_wall.update()
obj_wall = bpy.data.objects.new("EXP_Wall_Perimeter", mesh_wall)
obj_wall.data.materials.append(mat_plaster)
link_obj(obj_wall, col_arch)

# 3. Colonnade Vertical Fins (Brushed Aluminum)
mesh_fins = bpy.data.meshes.new("EXP_Colonnade_VerticalFins")
bm_f = bmesh.new()
# Fins along the colonnade arc (45 deg to 115 deg)
num_fins = 18
for i in range(num_fins):
    t = i / (num_fins - 1)
    angle = math.radians(45.0 + t * 70.0)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    fx = CX + R_ROT * cos_a
    fy = CY + R_ROT * sin_a
    
    # Fin size: width 0.04m, depth 0.14m (radial)
    w = 0.02
    d = 0.07
    norm_x = -sin_a
    norm_y = cos_a
    
    # 8 vertices for rectangular prism from Z=0.8 to Z=6.2m
    z0 = 0.80
    z1 = 6.20
    corners = [
        (fx - w*norm_x - d*cos_a, fy - w*norm_y - d*sin_a),
        (fx + w*norm_x - d*cos_a, fy + w*norm_y - d*sin_a),
        (fx + w*norm_x + d*cos_a, fy + w*norm_y + d*sin_a),
        (fx - w*norm_x + d*cos_a, fy - w*norm_y + d*sin_a)
    ]
    vb = [bm_f.verts.new((x, y, z0)) for x, y in corners]
    vt = [bm_f.verts.new((x, y, z1)) for x, y in corners]
    
    # 4 side faces
    for c in range(4):
        next_c = (c + 1) % 4
        bm_f.faces.new((vb[c], vb[next_c], vt[next_c], vt[c]))

bm_f.to_mesh(mesh_fins)
bm_f.free()
mesh_fins.update()
obj_fins = bpy.data.objects.new("EXP_Colonnade_VerticalFins", mesh_fins)
obj_fins.data.materials.append(mat_aluminum)
link_obj(obj_fins, col_struct)

# 4. Ceiling Dome with Central Oculus Skylight
mesh_dome = bpy.data.meshes.new("EXP_Dome_Ceiling")
bm_d = bmesh.new()
DOME_SEGS = 48
DOME_RINGS = 8
for ri in range(DOME_RINGS):
    t1 = ri / (DOME_RINGS - 1)
    r_val = R_ROT - t1 * (R_ROT - OCULUS_R)
    # Cosine easing curve for dome profile
    z_val = WALL_H + math.sin(t1 * math.pi * 0.5) * (DOME_TOP_H - WALL_H)
    
    for s in range(DOME_SEGS):
        theta = 2.0 * math.pi * s / DOME_SEGS
        vx = CX + r_val * math.cos(theta)
        vy = CY + r_val * math.sin(theta)
        bm_d.verts.new((vx, vy, z_val))

bm_d.verts.ensure_lookup_table()

for ri in range(DOME_RINGS - 1):
    for s in range(DOME_SEGS):
        next_s = (s + 1) % DOME_SEGS
        v1 = bm_d.verts[ri * DOME_SEGS + s]
        v2 = bm_d.verts[ri * DOME_SEGS + next_s]
        v3 = bm_d.verts[(ri + 1) * DOME_SEGS + next_s]
        v4 = bm_d.verts[(ri + 1) * DOME_SEGS + s]
        bm_d.faces.new((v1, v2, v3, v4))

bm_d.to_mesh(mesh_dome)
bm_d.free()
mesh_dome.update()
obj_dome = bpy.data.objects.new("EXP_Dome_Ceiling", mesh_dome)
obj_dome.data.materials.append(mat_plaster)
link_obj(obj_dome, col_arch)

# 4B. Oculus Ring Trim (Brushed Aluminum)
mesh_oc_ring = bpy.data.meshes.new("EXP_Oculus_SkylightRing")
bm_o = bmesh.new()
for s in range(DOME_SEGS):
    theta1 = 2.0 * math.pi * s / DOME_SEGS
    theta2 = 2.0 * math.pi * (s + 1) / DOME_SEGS
    r_in = OCULUS_R - 0.08
    r_out = OCULUS_R + 0.12
    z_ring = DOME_TOP_H
    v1 = bm_o.verts.new((CX + r_in * math.cos(theta1), CY + r_in * math.sin(theta1), z_ring - 0.15))
    v2 = bm_o.verts.new((CX + r_out * math.cos(theta1), CY + r_out * math.sin(theta1), z_ring - 0.15))
    v3 = bm_o.verts.new((CX + r_out * math.cos(theta2), CY + r_out * math.sin(theta2), z_ring - 0.15))
    v4 = bm_o.verts.new((CX + r_in * math.cos(theta2), CY + r_in * math.sin(theta2), z_ring - 0.15))
    v1t = bm_o.verts.new((CX + r_in * math.cos(theta1), CY + r_in * math.sin(theta1), z_ring))
    v2t = bm_o.verts.new((CX + r_out * math.cos(theta1), CY + r_out * math.sin(theta1), z_ring))
    v3t = bm_o.verts.new((CX + r_out * math.cos(theta2), CY + r_out * math.sin(theta2), z_ring))
    v4t = bm_o.verts.new((CX + r_in * math.cos(theta2), CY + r_in * math.sin(theta2), z_ring))
    bm_o.faces.new((v1, v2, v3, v4))
    bm_o.faces.new((v1t, v4t, v3t, v2t))
    bm_o.faces.new((v1, v4, v4t, v1t))
bm_o.to_mesh(mesh_oc_ring)
bm_o.free()
mesh_oc_ring.update()
obj_oc_ring = bpy.data.objects.new("EXP_Oculus_SkylightRing", mesh_oc_ring)
obj_oc_ring.data.materials.append(mat_aluminum)
link_obj(obj_oc_ring, col_struct)

# 4C. Oculus Clear Glass Disk
mesh_glass = bpy.data.meshes.new("EXP_Glass_OculusDome")
bm_g = bmesh.new()
vc = bm_g.verts.new((CX, CY, DOME_TOP_H - 0.05))
ring_g = []
for s in range(DOME_SEGS):
    theta = 2.0 * math.pi * s / DOME_SEGS
    ring_g.append(bm_g.verts.new((CX + OCULUS_R * math.cos(theta), CY + OCULUS_R * math.sin(theta), DOME_TOP_H - 0.05)))
for s in range(DOME_SEGS):
    next_s = (s + 1) % DOME_SEGS
    bm_g.faces.new((vc, ring_g[s], ring_g[next_s]))
bm_g.to_mesh(mesh_glass)
bm_g.free()
mesh_glass.update()
obj_glass = bpy.data.objects.new("EXP_Glass_OculusDome", mesh_glass)
obj_glass.data.materials.append(mat_glass)
link_obj(obj_glass, col_arch)

# 5. Connection Corridor from Scene 02 K08 Portal (from (43.24, 19.98) to Rotunda entrance)
mesh_corr = bpy.data.meshes.new("EXP_Portal_EntryVestibule")
bm_c = bmesh.new()
# Entry point from Scene 02
p0_l = (41.65, 20.72, 0.0)
p0_r = (44.83, 19.24, 0.0)
# Rotunda wall junction point (around angle 205 deg)
rot_entry_ang = math.radians(205.0)
rot_w = 3.60
rot_norm_x = -math.sin(rot_entry_ang)
rot_norm_y = math.cos(rot_entry_ang)
p1_cx = CX + R_ROT * math.cos(rot_entry_ang)
p1_cy = CY + R_ROT * math.sin(rot_entry_ang)
p1_l = (p1_cx - (rot_w/2.0)*rot_norm_x, p1_cy - (rot_w/2.0)*rot_norm_y, 0.0)
p1_r = (p1_cx + (rot_w/2.0)*rot_norm_x, p1_cy + (rot_w/2.0)*rot_norm_y, 0.0)

# Floor quad
vf1 = bm_c.verts.new(p0_l)
vf2 = bm_c.verts.new(p0_r)
vf3 = bm_c.verts.new(p1_r)
vf4 = bm_c.verts.new(p1_l)
bm_c.faces.new((vf1, vf2, vf3, vf4))

# Left wall
vf1_t = bm_c.verts.new((p0_l[0], p0_l[1], 4.8))
vf4_t = bm_c.verts.new((p1_l[0], p1_l[1], 4.8))
bm_c.faces.new((vf1, vf4, vf4_t, vf1_t))

# Right wall
vf2_t = bm_c.verts.new((p0_r[0], p0_r[1], 4.8))
vf3_t = bm_c.verts.new((p1_r[0], p1_r[1], 4.8))
bm_c.faces.new((vf2, vf2_t, vf3_t, vf3))

# Ceiling
bm_c.faces.new((vf1_t, vf4_t, vf3_t, vf2_t))

bm_c.to_mesh(mesh_corr)
bm_c.free()
mesh_corr.update()
obj_corr = bpy.data.objects.new("EXP_Portal_EntryVestibule", mesh_corr)
obj_corr.data.materials.append(mat_stone)
link_obj(obj_corr, col_arch)

# 6. Lighting Setup
# 6A. Directional Sunlight
sun_data = bpy.data.lights.new(name="EXP_SunLight", type='SUN')
sun_data.color = (1.0, 0.98, 0.95)
sun_data.energy = 3.2
sun_obj = bpy.data.objects.new("EXP_SunLight", sun_data)
sun_obj.rotation_euler = (math.radians(48.0), math.radians(22.0), math.radians(135.0))
col_arch.objects.link(sun_obj)

# 6B. Cove Light Ring at dome base
mesh_cove_strip = bpy.data.meshes.new("EXP_Light_CoveRing")
bm_cv = bmesh.new()
for s in range(DOME_SEGS):
    theta1 = 2.0 * math.pi * s / DOME_SEGS
    theta2 = 2.0 * math.pi * (s + 1) / DOME_SEGS
    r_cv = R_ROT - 0.15
    v1 = bm_cv.verts.new((CX + r_cv * math.cos(theta1), CY + r_cv * math.sin(theta1), WALL_H - 0.05))
    v2 = bm_cv.verts.new((CX + (r_cv + 0.10) * math.cos(theta1), CY + (r_cv + 0.10) * math.sin(theta1), WALL_H - 0.05))
    v3 = bm_cv.verts.new((CX + (r_cv + 0.10) * math.cos(theta2), CY + (r_cv + 0.10) * math.sin(theta2), WALL_H - 0.05))
    v4 = bm_cv.verts.new((CX + r_cv * math.cos(theta2), CY + r_cv * math.sin(theta2), WALL_H - 0.05))
    bm_cv.faces.new((v1, v2, v3, v4))
bm_cv.to_mesh(mesh_cove_strip)
bm_cv.free()
mesh_cove_strip.update()
obj_cove = bpy.data.objects.new("EXP_Light_CoveRing", mesh_cove_strip)
obj_cove.data.materials.append(mat_cove)
link_obj(obj_cove, col_arch)

# 7. Setup Render Cameras
# Helper to point camera at target
def setup_cam(name, loc, tgt, fov_deg=48.0, ortho_scale=0.0):
    cam_data = bpy.data.cameras.new(name)
    if ortho_scale > 0:
        cam_data.type = 'ORTHO'
        cam_data.ortho_scale = ortho_scale
    else:
        cam_data.type = 'PERSP'
        cam_data.angle = math.radians(fov_deg)
    cam_obj = bpy.data.objects.new(name, cam_data)
    cam_obj.location = loc
    # Aim at target
    dx = tgt[0] - loc[0]
    dy = tgt[1] - loc[1]
    dz = tgt[2] - loc[2]
    dist_xy = math.sqrt(dx*dx + dy*dy)
    yaw = math.atan2(dy, dx) - math.pi / 2.0
    pitch = math.atan2(dz, dist_xy)
    cam_obj.rotation_euler = (math.pi / 2.0 - pitch, 0.0, yaw)
    col_cam.objects.link(cam_obj)
    return cam_obj

# Cam 1: Top-down spatial layout (orthographic)
cam_top = setup_cam("CAM_TopDown", (52.0, 15.0, 40.0), (52.0, 15.0, 0.0), ortho_scale=38.0)

# Cam 2: K11 Enterprise Systems Colonnade (Blender coords: pos (59.60, 11.40, 1.85), tgt (66.80, 7.50, 2.10))
cam_k11 = setup_cam("CAM_K11_Enterprise", (59.60, 11.40, 1.85), (66.80, 7.50, 2.10), fov_deg=46.0)

# Cam 3: K12 Solution Consulting / Exit Threshold (Blender coords: pos (65.40, 8.00, 1.85), tgt (73.20, 4.20, 2.20))
cam_k12 = setup_cam("CAM_K12_Solution", (65.40, 8.00, 1.85), (73.20, 4.20, 2.20), fov_deg=48.0)

# Output directory
out_dir = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references"
os.makedirs(out_dir, exist_ok=True)

# Render Top-Down
scene.camera = cam_top
scene.render.filepath = os.path.join(out_dir, "02-raw-topdown.png")
bpy.ops.render.render(write_still=True)
print("Rendered TopDown Layout:", scene.render.filepath)

# Render K11
scene.camera = cam_k11
scene.render.filepath = os.path.join(out_dir, "keyframe-K11-render.png")
bpy.ops.render.render(write_still=True)
print("Rendered K11:", scene.render.filepath)

# Render K12
scene.camera = cam_k12
scene.render.filepath = os.path.join(out_dir, "keyframe-K12-render.png")
bpy.ops.render.render(write_still=True)
print("Rendered K12:", scene.render.filepath)

# Save blend file for archival
blend_path = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\expertise-rotunda-design.blend"
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print("Saved Blend file:", blend_path)
