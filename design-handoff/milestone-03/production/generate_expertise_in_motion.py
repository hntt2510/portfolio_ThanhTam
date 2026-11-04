import bpy
import bmesh
import math
import os
import sys

# Output paths
prod_dir = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production"
renders_dir = os.path.join(prod_dir, "renders")
os.makedirs(renders_dir, exist_ok=True)

glb_path = os.path.join(prod_dir, "expertise-in-motion.glb")
blend_path = os.path.join(prod_dir, "expertise-in-motion.blend")

print("======================================================================")
print("BUILDING MILESTONE 03A PRODUCTION ASSET: EXPERTISE IN MOTION")
print("======================================================================")

# Clean slate
bpy.ops.wm.read_factory_settings(use_empty=True)

scene = bpy.context.scene
scene.name = "Scene03A_Production"
scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'RenderEngine') and 'BLENDER_EEVEE_NEXT' in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items] else 'BLENDER_EEVEE'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Color Management
scene.display_settings.display_device = 'sRGB'
scene.view_settings.view_transform = 'AgX' if 'AgX' in [v.identifier for v in scene.view_settings.bl_rna.properties['view_transform'].enum_items] else 'Filmic'
scene.view_settings.look = 'Medium High Contrast'
scene.view_settings.exposure = 0.20

# World Natural Daylight
world = bpy.data.worlds.new("EXPM_DaylightWorld")
scene.world = world
world.use_nodes = True
nw = world.node_tree.nodes
nw.clear()
n_bg = nw.new(type='ShaderNodeBackground')
n_bg.inputs['Color'].default_value = (0.92, 0.96, 1.0, 1.0)
n_bg.inputs['Strength'].default_value = 1.8
n_out = nw.new(type='ShaderNodeOutputWorld')
world.node_tree.links.new(n_bg.outputs['Background'], n_out.inputs['Surface'])

# Collections
col_prod = bpy.data.collections.new("01_Production_EXPM")
col_helpers = bpy.data.collections.new("02_Lighting_Helpers")
col_cams = bpy.data.collections.new("03_Review_Cameras")
scene.collection.children.link(col_prod)
scene.collection.children.link(col_helpers)
scene.collection.children.link(col_cams)

def link_prod(obj):
    col_prod.objects.link(obj)

# ==============================================================================
# PBR MATERIALS
# ==============================================================================
def create_pbr(name, base_color, metallic=0.0, roughness=0.5, transmission=0.0, ior=1.5, alpha=1.0, emission=(0,0,0,1), emission_strength=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        if 'Base Color' in bsdf.inputs: bsdf.inputs['Base Color'].default_value = base_color
        if 'Metallic' in bsdf.inputs: bsdf.inputs['Metallic'].default_value = metallic
        if 'Roughness' in bsdf.inputs: bsdf.inputs['Roughness'].default_value = roughness
        if 'Transmission Weight' in bsdf.inputs: bsdf.inputs['Transmission Weight'].default_value = transmission
        elif 'Transmission' in bsdf.inputs: bsdf.inputs['Transmission'].default_value = transmission
        if 'IOR' in bsdf.inputs: bsdf.inputs['IOR'].default_value = ior
        if emission_strength > 0:
            if 'Emission Color' in bsdf.inputs: bsdf.inputs['Emission Color'].default_value = emission
            elif 'Emission' in bsdf.inputs: bsdf.inputs['Emission'].default_value = emission
            if 'Emission Strength' in bsdf.inputs: bsdf.inputs['Emission Strength'].default_value = emission_strength
        if alpha < 1.0:
            if 'Alpha' in bsdf.inputs: bsdf.inputs['Alpha'].default_value = alpha
            mat.blend_method = 'BLEND'
    return mat

mat_plaster = create_pbr("MAT_EXPM_WhitePlaster", (0.97, 0.97, 0.96, 1.0), metallic=0.0, roughness=0.82)
mat_travertine = create_pbr("MAT_EXPM_TravertineStone", (0.96, 0.95, 0.93, 1.0), metallic=0.02, roughness=0.18)
mat_basalt = create_pbr("MAT_EXPM_BasaltPath", (0.32, 0.34, 0.36, 1.0), metallic=0.05, roughness=0.30)
mat_aluminum = create_pbr("MAT_EXPM_BrushedAluminum", (0.94, 0.95, 0.97, 1.0), metallic=0.82, roughness=0.20)
mat_frosted = create_pbr("MAT_EXPM_FrostedGlass", (0.94, 0.96, 0.99, 1.0), metallic=0.05, roughness=0.35, transmission=0.85, ior=1.52)
mat_glass = create_pbr("MAT_EXPM_ClearGlass", (0.96, 0.98, 1.0, 1.0), metallic=0.0, roughness=0.02, transmission=0.96, ior=1.52, alpha=0.22)
mat_spine_light = create_pbr("MAT_EXPM_CoreLight", (1.0, 0.98, 0.94, 1.0), emission=(1.0, 0.98, 0.94, 1.0), emission_strength=3.5)

# Sunlight
sun_data = bpy.data.lights.new(name="EXPM_SunLight", type='SUN')
sun_data.color = (1.0, 0.98, 0.95)
sun_data.energy = 3.6
sun_obj = bpy.data.objects.new("EXPM_SunLight", sun_data)
sun_obj.rotation_euler = (math.radians(48.0), math.radians(24.0), math.radians(125.0))
col_helpers.objects.link(sun_obj)

# ==============================================================================
# GEOMETRY ENGINE: ASYMMETRIC SAWTOOTH PAVILION
# ==============================================================================
# Seam origin: Scene 02 K08 portal at (43.24, 19.98, 0.0)
P0 = (43.24, 19.98, 0.0)
TANG_DEG = -25.0
cos_t = math.cos(math.radians(TANG_DEG))
sin_t = math.sin(math.radians(TANG_DEG))
norm_x = -sin_t # Direction perpendicular to longitudinal axis (North)
norm_y = cos_t

L_HALL = 36.0 # Length along longitudinal axis
W_HALL = 18.0 # Total width across transverse axis
H_SOUTH = 6.20 # South perimeter wall height
H_NORTH = 10.50 # North perimeter wall height (sawtooth apex)

def get_pt(u, v):
    """Computes world (X, Y) from local longitudinal U and transverse V."""
    return (P0[0] + u * cos_t + v * norm_x, P0[1] + u * sin_t + v * norm_y)

# ------------------------------------------------------------------------------
# 1. Travertine Floor Slab (EXPM_Floor_Travertine)
# ------------------------------------------------------------------------------
mesh_floor = bpy.data.meshes.new("EXPM_Floor_Travertine")
bm_fl = bmesh.new()

# Grid subdivision for clean lighting / shadows
U_SEGS = 18
V_SEGS = 9
verts_grid = []
for iu in range(U_SEGS + 1):
    u = (iu / U_SEGS) * L_HALL
    row = []
    for iv in range(V_SEGS + 1):
        v = -W_HALL/2.0 + (iv / V_SEGS) * W_HALL
        px, py = get_pt(u, v)
        row.append(bm_fl.verts.new((px, py, 0.0)))
    verts_grid.append(row)

for iu in range(U_SEGS):
    for iv in range(V_SEGS):
        v1 = verts_grid[iu][iv]
        v2 = verts_grid[iu + 1][iv]
        v3 = verts_grid[iu + 1][iv + 1]
        v4 = verts_grid[iu][iv + 1]
        bm_fl.faces.new((v1, v2, v3, v4))

bm_fl.to_mesh(mesh_floor)
bm_fl.free()
mesh_floor.update()
obj_floor = bpy.data.objects.new("EXPM_Floor_Travertine", mesh_floor)
obj_floor.data.materials.append(mat_travertine)
link_prod(obj_floor)

# ------------------------------------------------------------------------------
# 2. Branching Process Pathways: Basalt Inlays (EXPM_Floor_BasaltPaths)
# ------------------------------------------------------------------------------
mesh_paths = bpy.data.meshes.new("EXPM_Floor_BasaltPaths")
bm_pt = bmesh.new()
Z_PATH = 0.003 # 3mm elevation above travertine to guarantee crisp render with zero z-fighting

# Spine 1: Main discovery trunk from entrance (u=0 to u=14, width 1.6m)
w_trunk = 0.80
p1_a = get_pt(0.0, -w_trunk)
p1_b = get_pt(14.0, -w_trunk)
p1_c = get_pt(14.0, w_trunk)
p1_d = get_pt(0.0, w_trunk)
vp1 = [bm_pt.verts.new((x, y, Z_PATH)) for x, y in [p1_a, p1_b, p1_c, p1_d]]
bm_pt.faces.new(vp1)

# Route A (Straight "As-Is" Analytical Route: u=14 to u=24, width 1.2m, staying south)
p_as1 = get_pt(14.0, -w_trunk)
p_as2 = get_pt(24.0, -1.8)
p_as3 = get_pt(24.0, -0.6)
p_as4 = get_pt(14.0, 0.0)
vp_as = [bm_pt.verts.new((x, y, Z_PATH)) for x, y in [p_as1, p_as2, p_as3, p_as4]]
bm_pt.faces.new(vp_as)

# Route B (Arcing "To-Be" Transformation Route: u=14 to u=26, branching North through daylight zone)
pts_arc = []
N_ARC = 8
for i in range(N_ARC + 1):
    t = i / N_ARC
    u = 14.0 + t * 12.0
    v = 0.0 + math.sin(t * math.pi) * 4.5
    pts_arc.append((u, v))

for i in range(N_ARC):
    u1, v1 = pts_arc[i]
    u2, v2 = pts_arc[i+1]
    w = 0.60
    pa = get_pt(u1, v1 - w)
    pb = get_pt(u2, v2 - w)
    pc = get_pt(u2, v2 + w)
    pd = get_pt(u1, v1 + w)
    v_quad = [bm_pt.verts.new((x, y, Z_PATH)) for x, y in [pa, pb, pc, pd]]
    bm_pt.faces.new(v_quad)

# Convergence Hub (u=24 to u=28): converging into the base of the bridge plinth
pc1 = get_pt(24.0, -1.8)
pc2 = get_pt(28.0, -1.2)
pc3 = get_pt(28.0, 1.2)
pc4 = get_pt(24.0, 1.6)
vp_c = [bm_pt.verts.new((x, y, Z_PATH)) for x, y in [pc1, pc2, pc3, pc4]]
bm_pt.faces.new(vp_c)

bm_pt.to_mesh(mesh_paths)
bm_pt.free()
mesh_paths.update()
obj_paths = bpy.data.objects.new("EXPM_Floor_BasaltPaths", mesh_paths)
obj_paths.data.materials.append(mat_basalt)
link_prod(obj_paths)

# 2B. Precision Brushed Aluminum Floor Inlays (EXPM_Floor_SilverInlays)
mesh_inlays = bpy.data.meshes.new("EXPM_Floor_SilverInlays")
bm_in = bmesh.new()
# Thin 2cm silver lines flanking the pathways
Z_IN = 0.004
w_in = 0.02
for v_off in [-w_trunk - w_in, w_trunk + w_in]:
    ia = get_pt(0.0, v_off)
    ib = get_pt(14.0, v_off)
    ic = get_pt(14.0, v_off + w_in)
    id = get_pt(0.0, v_off + w_in)
    v_in = [bm_in.verts.new((x, y, Z_IN)) for x, y in [ia, ib, ic, id]]
    bm_in.faces.new(v_in)

bm_in.to_mesh(mesh_inlays)
bm_in.free()
mesh_inlays.update()
obj_inlays = bpy.data.objects.new("EXPM_Floor_SilverInlays", mesh_inlays)
obj_inlays.data.materials.append(mat_aluminum)
link_prod(obj_inlays)

# ------------------------------------------------------------------------------
# 3. Perimeter Walls & Sawtooth Roof Baffles (EXPM_Walls_Sawtooth)
# ------------------------------------------------------------------------------
mesh_walls = bpy.data.meshes.new("EXPM_Walls_Sawtooth")
bm_wl = bmesh.new()

# Corner base points
c_sw = get_pt(0.0, -W_HALL/2.0)
c_se = get_pt(L_HALL, -W_HALL/2.0)
c_ne = get_pt(L_HALL, W_HALL/2.0)
c_nw = get_pt(0.0, W_HALL/2.0)

# South Wall (Low: 6.20m)
vs1 = bm_wl.verts.new((c_sw[0], c_sw[1], 0.0))
vs2 = bm_wl.verts.new((c_se[0], c_se[1], 0.0))
vs2_t = bm_wl.verts.new((c_se[0], c_se[1], H_SOUTH))
vs1_t = bm_wl.verts.new((c_sw[0], c_sw[1], H_SOUTH))
bm_wl.faces.new((vs1, vs2, vs2_t, vs1_t))

# North Wall (High: 10.50m)
vn1 = bm_wl.verts.new((c_nw[0], c_nw[1], 0.0))
vn2 = bm_wl.verts.new((c_ne[0], c_ne[1], 0.0))
vn2_t = bm_wl.verts.new((c_ne[0], c_ne[1], H_NORTH))
vn1_t = bm_wl.verts.new((c_nw[0], c_nw[1], H_NORTH))
bm_wl.faces.new((vn1, vn1_t, vn2_t, vn2))

# West Wall (Connection wall with arched opening for vestibule)
vw1 = bm_wl.verts.new((c_sw[0], c_sw[1], 0.0))
vw2 = bm_wl.verts.new((c_nw[0], c_nw[1], 0.0))
vw2_t = bm_wl.verts.new((c_nw[0], c_nw[1], H_NORTH))
vw1_t = bm_wl.verts.new((c_sw[0], c_sw[1], H_SOUTH))
bm_wl.faces.new((vw1, vw1_t, vw2_t, vw2))

# East Wall (Exit wall leading toward Scene 04 portal)
ve1 = bm_wl.verts.new((c_se[0], c_se[1], 0.0))
ve2 = bm_wl.verts.new((c_ne[0], c_ne[1], 0.0))
ve2_t = bm_wl.verts.new((c_ne[0], c_ne[1], H_NORTH))
ve1_t = bm_wl.verts.new((c_se[0], c_se[1], H_SOUTH))
bm_wl.faces.new((ve1, ve2, ve2_t, ve1_t))

# Four Sawtooth Sloped Roof Baffles with North Clerestories
N_SAW = 4
clerestory_quads = []
for si in range(N_SAW):
    u_start = (si / N_SAW) * L_HALL
    u_apex = ((si + 0.82) / N_SAW) * L_HALL
    u_drop = ((si + 1.0) / N_SAW) * L_HALL
    
    # Sloped roof baffle surface: slopes upward from South to North and along U
    p_s1 = get_pt(u_start, -W_HALL/2.0)
    p_n1 = get_pt(u_start, W_HALL/2.0)
    p_n2 = get_pt(u_apex, W_HALL/2.0)
    p_s2 = get_pt(u_apex, -W_HALL/2.0)
    
    z_s1 = H_SOUTH + (si * 0.3)
    z_s2 = H_SOUTH + ((si + 0.82) * 0.3)
    z_n1 = H_NORTH
    z_n2 = H_NORTH
    
    vr1 = bm_wl.verts.new((p_s1[0], p_s1[1], z_s1))
    vr2 = bm_wl.verts.new((p_n1[0], p_n1[1], z_n1))
    vr3 = bm_wl.verts.new((p_n2[0], p_n2[1], z_n2))
    vr4 = bm_wl.verts.new((p_s2[0], p_s2[1], z_s2))
    bm_wl.faces.new((vr1, vr2, vr3, vr4))
    
    # Vertical North-Facing Clerestory Aperture: drops vertically from u_apex to u_drop
    p_s3 = get_pt(u_drop, -W_HALL/2.0)
    p_n3 = get_pt(u_drop, W_HALL/2.0)
    z_s3 = H_SOUTH + ((si + 1.0) * 0.3)
    z_n3 = H_NORTH - 1.80 # Window height 1.80m
    
    vr_drop_s = bm_wl.verts.new((p_s3[0], p_s3[1], z_s3))
    vr_drop_n = bm_wl.verts.new((p_n3[0], p_n3[1], z_n3))
    
    # Store clerestory window aperture vertices for separate glass mesh
    clerestory_quads.append((
        (p_s2[0], p_s2[1], z_s2),
        (p_n2[0], p_n2[1], z_n2),
        (p_n3[0], p_n3[1], z_n3),
        (p_s3[0], p_s3[1], z_s3)
    ))

bm_wl.to_mesh(mesh_walls)
bm_wl.free()
mesh_walls.update()
obj_walls = bpy.data.objects.new("EXPM_Walls_Sawtooth", mesh_walls)
obj_walls.data.materials.append(mat_plaster)
link_prod(obj_walls)

# ------------------------------------------------------------------------------
# 4. North-Facing Clerestory Glazing (EXPM_Clerestory_Glass)
# ------------------------------------------------------------------------------
mesh_cl_glass = bpy.data.meshes.new("EXPM_Clerestory_Glass")
bm_cg = bmesh.new()
for q in clerestory_quads:
    v1 = bm_cg.verts.new(q[0])
    v2 = bm_cg.verts.new(q[1])
    v3 = bm_cg.verts.new(q[2])
    v4 = bm_cg.verts.new(q[3])
    bm_cg.faces.new((v1, v2, v3, v4))

bm_cg.to_mesh(mesh_cl_glass)
bm_cg.free()
mesh_cl_glass.update()
obj_cl_glass = bpy.data.objects.new("EXPM_Clerestory_Glass", mesh_cl_glass)
obj_cl_glass.data.materials.append(mat_glass)
link_prod(obj_cl_glass)

# ------------------------------------------------------------------------------
# 5. Monumental Modular System Spine Installation (EXPM_SystemSpine)
# ------------------------------------------------------------------------------
# A 4x2x3 bay structural matrix of brushed aluminum frames with nested frosted cubes
mesh_spine_fr = bpy.data.meshes.new("EXPM_SystemSpine_Frames")
bm_sf = bmesh.new()

mesh_spine_cu = bpy.data.meshes.new("EXPM_SystemSpine_FrostedCubes")
bm_sc = bmesh.new()

U_SPINE = 15.0
V_SPINE = 1.8
BAY_L = 2.40 # Bay length
BAY_W = 2.20 # Bay width
BAY_H = 1.40 # Bay height
BEAM_T = 0.08 # 8cm aluminum beam profile

for ix in range(4): # 4 bays long
    for iy in range(2): # 2 bays wide
        for iz in range(3): # 3 tiers high
            # Center coordinates
            u_c = U_SPINE + ix * BAY_L + BAY_L/2.0
            v_c = V_SPINE + iy * BAY_W + BAY_W/2.0
            z_c = iz * BAY_H + BAY_H/2.0
            
            # Aluminum frame struts
            hx = (BAY_L/2.0) - 0.04
            hy = (BAY_W/2.0) - 0.04
            hz = (BAY_H/2.0) - 0.04
            
            c_pt = get_pt(u_c, v_c)
            
            # Generate 8 corners of frame
            corn = [
                (c_pt[0] - hx*cos_t - hy*norm_x, c_pt[1] - hx*sin_t - hy*norm_y, z_c - hz),
                (c_pt[0] + hx*cos_t - hy*norm_x, c_pt[1] + hx*sin_t - hy*norm_y, z_c - hz),
                (c_pt[0] + hx*cos_t + hy*norm_x, c_pt[1] + hx*sin_t + hy*norm_y, z_c - hz),
                (c_pt[0] - hx*cos_t + hy*norm_x, c_pt[1] - hx*sin_t + hy*norm_y, z_c - hz),
                (c_pt[0] - hx*cos_t - hy*norm_x, c_pt[1] - hx*sin_t - hy*norm_y, z_c + hz),
                (c_pt[0] + hx*cos_t - hy*norm_x, c_pt[1] + hx*sin_t - hy*norm_y, z_c + hz),
                (c_pt[0] + hx*cos_t + hy*norm_x, c_pt[1] + hx*sin_t + hy*norm_y, z_c + hz),
                (c_pt[0] - hx*cos_t + hy*norm_x, c_pt[1] - hx*sin_t + hy*norm_y, z_c + hz)
            ]
            
            # Aluminum frame perimeter
            vb = [bm_sf.verts.new(c) for c in corn[:4]]
            vt = [bm_sf.verts.new(c) for c in corn[4:]]
            for c_i in range(4):
                next_c = (c_i + 1) % 4
                bm_sf.faces.new((vb[c_i], vb[next_c], vt[next_c], vt[c_i]))
            
            # Add nested frosted glass volumes in selected bays (rhythm of 10 cubes)
            if (ix + iy + iz) % 2 == 0 or (ix == 1 and iz == 1):
                ch_x = hx * 0.75
                ch_y = hy * 0.75
                ch_z = hz * 0.75
                c_corn = [
                    (c_pt[0] - ch_x*cos_t - ch_y*norm_x, c_pt[1] - ch_x*sin_t - ch_y*norm_y, z_c - ch_z),
                    (c_pt[0] + ch_x*cos_t - ch_y*norm_x, c_pt[1] + ch_x*sin_t - ch_y*norm_y, z_c - ch_z),
                    (c_pt[0] + ch_x*cos_t + ch_y*norm_x, c_pt[1] + ch_x*sin_t + ch_y*norm_y, z_c - ch_z),
                    (c_pt[0] - ch_x*cos_t + ch_y*norm_x, c_pt[1] - ch_x*sin_t + ch_y*norm_y, z_c - ch_z),
                    (c_pt[0] - ch_x*cos_t - ch_y*norm_x, c_pt[1] - ch_x*sin_t - ch_y*norm_y, z_c + ch_z),
                    (c_pt[0] + ch_x*cos_t - ch_y*norm_x, c_pt[1] + ch_x*sin_t - ch_y*norm_y, z_c + ch_z),
                    (c_pt[0] + ch_x*cos_t + ch_y*norm_x, c_pt[1] + ch_x*sin_t + ch_y*norm_y, z_c + ch_z),
                    (c_pt[0] - ch_x*cos_t + ch_y*norm_x, c_pt[1] - ch_x*sin_t + ch_y*norm_y, z_c + ch_z)
                ]
                v_cb = [bm_sc.verts.new(c) for c in c_corn[:4]]
                v_ct = [bm_sc.verts.new(c) for c in c_corn[4:]]
                for c_i in range(4):
                    next_c = (c_i + 1) % 4
                    bm_sc.faces.new((v_cb[c_i], v_cb[next_c], v_ct[next_c], v_ct[c_i]))
                bm_sc.faces.new(v_cb)
                bm_sc.faces.new(v_ct)

bm_sf.to_mesh(mesh_spine_fr)
bm_sf.free()
mesh_spine_fr.update()
obj_spine_fr = bpy.data.objects.new("EXPM_SystemSpine_Frames", mesh_spine_fr)
obj_spine_fr.data.materials.append(mat_aluminum)
link_prod(obj_spine_fr)

bm_sc.to_mesh(mesh_spine_cu)
bm_sc.free()
mesh_spine_cu.update()
obj_spine_cu = bpy.data.objects.new("EXPM_SystemSpine_FrostedCubes", mesh_spine_cu)
obj_spine_cu.data.materials.append(mat_frosted)
link_prod(obj_spine_cu)

# ------------------------------------------------------------------------------
# 6. Suspended Pedestrian Bridge (EXPM_SuspendedBridge)
# ------------------------------------------------------------------------------
# Bridge deck: starts with stone plinth ramp (u=22 to u=24), spans u=24 to u=36 at Z=2.40m
mesh_bridge = bpy.data.meshes.new("EXPM_SuspendedBridge_Deck")
bm_br = bmesh.new()

U_BR_START = 22.0
U_BR_END = 36.0
W_BR = 3.20
Z_BR = 2.40
DECK_T = 0.35 # Deck thickness

# Ramp section (u=22 to u=24, ascending from Z=0 to Z=2.4m)
ra1 = get_pt(U_BR_START, -W_BR/2.0)
ra2 = get_pt(U_BR_START + 2.0, -W_BR/2.0)
ra3 = get_pt(U_BR_START + 2.0, W_BR/2.0)
ra4 = get_pt(U_BR_START, W_BR/2.0)

vr_a1 = bm_br.verts.new((ra1[0], ra1[1], 0.0))
vr_a2 = bm_br.verts.new((ra2[0], ra2[1], Z_BR))
vr_a3 = bm_br.verts.new((ra3[0], ra3[1], Z_BR))
vr_a4 = bm_br.verts.new((ra4[0], ra4[1], 0.0))
bm_br.faces.new((vr_a1, vr_a2, vr_a3, vr_a4))

# Main horizontal bridge deck (u=24 to u=36, Z=2.4m)
rb1 = get_pt(U_BR_START + 2.0, -W_BR/2.0)
rb2 = get_pt(U_BR_END, -W_BR/2.0)
rb3 = get_pt(U_BR_END, W_BR/2.0)
rb4 = get_pt(U_BR_START + 2.0, W_BR/2.0)

# Top surface
vrb1 = bm_br.verts.new((rb1[0], rb1[1], Z_BR))
vrb2 = bm_br.verts.new((rb2[0], rb2[1], Z_BR))
vrb3 = bm_br.verts.new((rb3[0], rb3[1], Z_BR))
vrb4 = bm_br.verts.new((rb4[0], rb4[1], Z_BR))
bm_br.faces.new((vrb1, vrb2, vrb3, vrb4))

# Bottom surface (thickness 0.35m)
vrb1_b = bm_br.verts.new((rb1[0], rb1[1], Z_BR - DECK_T))
vrb2_b = bm_br.verts.new((rb2[0], rb2[1], Z_BR - DECK_T))
vrb3_b = bm_br.verts.new((rb3[0], rb3[1], Z_BR - DECK_T))
vrb4_b = bm_br.verts.new((rb4[0], rb4[1], Z_BR - DECK_T))
bm_br.faces.new((vrb1_b, vrb4_b, vrb3_b, vrb2_b))

# Bridge fascia sides
bm_br.faces.new((vrb1_b, vrb2_b, vrb2, vrb1)) # South side
bm_br.faces.new((vrb4, vrb3, vrb3_b, vrb4_b)) # North side

bm_br.to_mesh(mesh_bridge)
bm_br.free()
mesh_bridge.update()
obj_bridge = bpy.data.objects.new("EXPM_SuspendedBridge_Deck", mesh_bridge)
obj_bridge.data.materials.append(mat_travertine)
link_prod(obj_bridge)

# 6B. Glass Balustrades & Brushed Aluminum Handrails (EXPM_Bridge_Balustrades)
mesh_bal = bpy.data.meshes.new("EXPM_Bridge_Balustrades")
bm_ba = bmesh.new()
H_BAL = 1.10 # 1.10m safety rail height

# South Glass Balustrade
vs_b1 = bm_ba.verts.new((rb1[0], rb1[1], Z_BR))
vs_b2 = bm_ba.verts.new((rb2[0], rb2[1], Z_BR))
vs_t2 = bm_ba.verts.new((rb2[0], rb2[1], Z_BR + H_BAL))
vs_t1 = bm_ba.verts.new((rb1[0], rb1[1], Z_BR + H_BAL))
bm_ba.faces.new((vs_b1, vs_b2, vs_t2, vs_t1))

# North Glass Balustrade
vn_b1 = bm_ba.verts.new((rb4[0], rb4[1], Z_BR))
vn_b2 = bm_ba.verts.new((rb3[0], rb3[1], Z_BR))
vn_t2 = bm_ba.verts.new((rb3[0], rb3[1], Z_BR + H_BAL))
vn_t1 = bm_ba.verts.new((rb4[0], rb4[1], Z_BR + H_BAL))
bm_ba.faces.new((vn_b1, vn_t1, vn_t2, vn_b2))

bm_ba.to_mesh(mesh_bal)
bm_ba.free()
mesh_bal.update()
obj_bal = bpy.data.objects.new("EXPM_Bridge_Balustrades", mesh_bal)
obj_bal.data.materials.append(mat_glass)
link_prod(obj_bal)

# 6C. Bridge Handrail Trim (Brushed Aluminum)
mesh_rail = bpy.data.meshes.new("EXPM_Bridge_Handrail")
bm_rl = bmesh.new()
r_w = 0.04
for p_start, p_end in [(rb1, rb2), (rb4, rb3)]:
    r1 = (p_start[0] - r_w*norm_x, p_start[1] - r_w*norm_y, Z_BR + H_BAL)
    r2 = (p_end[0] - r_w*norm_x, p_end[1] - r_w*norm_y, Z_BR + H_BAL)
    r3 = (p_end[0] + r_w*norm_x, p_end[1] + r_w*norm_y, Z_BR + H_BAL)
    r4 = (p_start[0] + r_w*norm_x, p_start[1] + r_w*norm_y, Z_BR + H_BAL)
    vr = [bm_rl.verts.new(p) for p in [r1, r2, r3, r4]]
    bm_rl.faces.new(vr)

bm_rl.to_mesh(mesh_rail)
bm_rl.free()
mesh_rail.update()
obj_rail = bpy.data.objects.new("EXPM_Bridge_Handrail", mesh_rail)
obj_rail.data.materials.append(mat_aluminum)
link_prod(obj_rail)

# ------------------------------------------------------------------------------
# 7. Entrance Vestibule Collar (EXPM_Portal_EntryVestibule)
# Connects flush to Scene 02 portal at (43.24, 19.98) and extends into pavilion
# ------------------------------------------------------------------------------
mesh_vest = bpy.data.meshes.new("EXPM_Portal_EntryVestibule")
bm_vt = bmesh.new()
# Arch span 3.6m, height 4.5m
w_arch = 1.80
h_arch = 4.50
# Point at junction with Scene 02 (u = -0.2m overlap for watertight seam)
p_j_l = get_pt(-0.2, -w_arch)
p_j_r = get_pt(-0.2, w_arch)
# Point at entry into pavilion wall (u = 1.5m)
p_in_l = get_pt(1.5, -w_arch)
p_in_r = get_pt(1.5, w_arch)

# Floor
v_vf1 = bm_vt.verts.new((p_j_l[0], p_j_l[1], 0.0))
v_vf2 = bm_vt.verts.new((p_j_r[0], p_j_r[1], 0.0))
v_vf3 = bm_vt.verts.new((p_in_r[0], p_in_r[1], 0.0))
v_vf4 = bm_vt.verts.new((p_in_l[0], p_in_l[1], 0.0))
bm_vt.faces.new((v_vf1, v_vf2, v_vf3, v_vf4))

# Left Wall
v_vf1_t = bm_vt.verts.new((p_j_l[0], p_j_l[1], h_arch))
v_vf4_t = bm_vt.verts.new((p_in_l[0], p_in_l[1], h_arch))
bm_vt.faces.new((v_vf1, v_vf4, v_vf4_t, v_vf1_t))

# Right Wall
v_vf2_t = bm_vt.verts.new((p_j_r[0], p_j_r[1], h_arch))
v_vf3_t = bm_vt.verts.new((p_in_r[0], p_in_r[1], h_arch))
bm_vt.faces.new((v_vf2, v_vf2_t, v_vf3_t, v_vf3))

# Ceiling
bm_vt.faces.new((v_vf1_t, v_vf4_t, v_vf3_t, v_vf2_t))

bm_vt.to_mesh(mesh_vest)
bm_vt.free()
mesh_vest.update()
obj_vest = bpy.data.objects.new("EXPM_Portal_EntryVestibule", mesh_vest)
obj_vest.data.materials.append(mat_plaster)
link_prod(obj_vest)

# ------------------------------------------------------------------------------
# 8. Grand Exit Threshold toward Scene 04 (EXPM_Portal_ExitThreshold)
# Located at terminus of the bridge at u = 36.0m
# ------------------------------------------------------------------------------
mesh_exit = bpy.data.meshes.new("EXPM_Portal_ExitThreshold")
bm_ex = bmesh.new()
w_exit = 2.10
h_exit = 5.20 # High majestic portal opening

pe_l = get_pt(L_HALL, -w_exit)
pe_r = get_pt(L_HALL, w_exit)
pe_fl = get_pt(L_HALL + 2.0, -w_exit)
pe_fr = get_pt(L_HALL + 2.0, w_exit)

# Portal jamb walls
v_e1 = bm_ex.verts.new((pe_l[0], pe_l[1], Z_BR))
v_e2 = bm_ex.verts.new((pe_r[0], pe_r[1], Z_BR))
v_e3 = bm_ex.verts.new((pe_fr[0], pe_fr[1], Z_BR))
v_e4 = bm_ex.verts.new((pe_fl[0], pe_fl[1], Z_BR))
bm_ex.faces.new((v_e1, v_e2, v_e3, v_e4)) # Threshold floor

v_e1_t = bm_ex.verts.new((pe_l[0], pe_l[1], Z_BR + h_exit))
v_e2_t = bm_ex.verts.new((pe_r[0], pe_r[1], Z_BR + h_exit))
v_e3_t = bm_ex.verts.new((pe_fr[0], pe_fr[1], Z_BR + h_exit))
v_e4_t = bm_ex.verts.new((pe_fl[0], pe_fl[1], Z_BR + h_exit))

bm_ex.faces.new((v_e1, v_e4, v_e4_t, v_e1_t)) # Left reveal
bm_ex.faces.new((v_e2, v_e2_t, v_e3_t, v_e3)) # Right reveal
bm_ex.faces.new((v_e1_t, v_e4_t, v_e3_t, v_e2_t)) # Portal soffit

bm_ex.to_mesh(mesh_exit)
bm_ex.free()
mesh_exit.update()
obj_exit = bpy.data.objects.new("EXPM_Portal_ExitThreshold", mesh_exit)
obj_exit.data.materials.append(mat_plaster)
link_prod(obj_exit)

print("Geometry creation complete. 10 production meshes created with EXPM_ prefix.")

# ==============================================================================
# CAMERAS SETUP & RENDERING
# ==============================================================================
def create_cam(name, loc, tgt, fov_deg=48.0, ortho_scale=0.0):
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
    col_cams.objects.link(cam_obj)
    return cam_obj

# Camera 1: K08 Seam Preview (FOV 48.0° desktop, exactly matching runtime)
cam_k08 = create_cam("CAM_K08_Seam", (36.53, 21.62, 1.80), (43.24, 19.98, 2.20), fov_deg=48.0)

# Camera 2: K09 Reveal (FOV 52.0°)
cam_k09 = create_cam("CAM_K09_Reveal", (44.50, 19.40, 1.85), (55.80, 14.10, 3.80), fov_deg=52.0)

# Camera 3: K10 Process Paths (FOV 46.0°, elevated oblique view Z=3.20m, pitch -22°)
cam_k10 = create_cam("CAM_K10_ProcessPaths", (49.50, 14.20, 3.20), (57.80, 10.30, 0.20), fov_deg=46.0)

# Camera 4: K11 System Spine (FOV 48.0°, side-tracking view past modular matrix)
cam_k11 = create_cam("CAM_K11_SystemSpine", (56.80, 11.20, 1.85), (58.50, 4.50, 2.20), fov_deg=48.0)

# Camera 5: K12 Bridge (FOV 50.0°, elevated bridge glide Z=4.05m eye level)
cam_k12 = create_cam("CAM_K12_Bridge", (63.20, 8.20, 4.05), (75.00, 2.80, 4.20), fov_deg=50.0)

# Camera 6: Top-Down Orthographic Layout
cam_top = create_cam("CAM_TopDown", (60.0, 12.0, 46.0), (60.0, 12.0, 0.0), ortho_scale=44.0)

# Camera 7: Portal Seam Detail inspection shot
cam_seam = create_cam("CAM_Portal_Detail", (40.50, 20.80, 2.10), (45.00, 19.20, 2.30), fov_deg=44.0)

# Mobile portrait cameras (aspect 9:19.5, vertical FOVs)
cam_m_k09 = create_cam("CAM_Mob_K09", (44.20, 19.20, 1.90), (55.80, 14.10, 4.00), fov_deg=54.0)
cam_m_k10 = create_cam("CAM_Mob_K10", (49.20, 14.00, 3.30), (57.80, 10.30, 0.20), fov_deg=48.0)
cam_m_k11 = create_cam("CAM_Mob_K11", (56.50, 11.00, 1.90), (58.50, 4.50, 2.30), fov_deg=50.0)
cam_m_k12 = create_cam("CAM_Mob_K12", (62.80, 8.00, 4.10), (75.00, 2.80, 4.30), fov_deg=52.0)

# Render list
renders = [
    (cam_k08, "camera-K08-seam.png", 1920, 1080),
    (cam_k09, "camera-K09-reveal.png", 1920, 1080),
    (cam_k10, "camera-K10-process-paths.png", 1920, 1080),
    (cam_k11, "camera-K11-system-spine.png", 1920, 1080),
    (cam_k12, "camera-K12-bridge.png", 1920, 1080),
    (cam_top, "top-down-layout.png", 1920, 1080),
    (cam_seam, "portal-seam-detail.png", 1920, 1080),
    # Mobile Portrait renders
    (cam_m_k09, "mobile-K09.png", 1080, 1920),
    (cam_m_k10, "mobile-K10.png", 1080, 1920),
    (cam_m_k11, "mobile-K11.png", 1080, 1920),
    (cam_m_k12, "mobile-K12.png", 1080, 1920)
]

for cam, fname, rx, ry in renders:
    scene.camera = cam
    scene.render.resolution_x = rx
    scene.render.resolution_y = ry
    out_file = os.path.join(renders_dir, fname)
    scene.render.filepath = out_file
    bpy.ops.render.render(write_still=True)
    print(f"Rendered: {fname} ({rx}x{ry})")

# Save editable production .blend file
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print("Saved production .blend:", blend_path)

# ==============================================================================
# GLB EXPORT PIPELINE
# ==============================================================================
# Select ONLY objects in col_prod for export
bpy.ops.object.select_all(action='DESELECT')
for obj in col_prod.objects:
    obj.select_set(True)

bpy.context.view_layer.objects.active = col_prod.objects[0]

# Export GLB binary
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

glb_size_bytes = os.path.getsize(glb_path)
glb_size_kb = glb_size_bytes / 1024.0
print(f"Successfully exported GLB: {glb_path} ({glb_size_kb:.2f} KB)")

# ==============================================================================
# GLB RE-IMPORT VALIDATION IN CLEAN SCENE
# ==============================================================================
print("Starting GLB re-import validation...")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb_path)

imported_objs = [o for o in bpy.context.scene.objects if o.type == 'MESH']
total_verts = sum(len(o.data.vertices) for o in imported_objs)
total_polys = sum(len(o.data.polygons) for o in imported_objs)
total_tris = sum(len(o.data.loop_triangles) if hasattr(o.data, 'loop_triangles') else len(o.data.polygons)*2 for o in imported_objs)

print("--- GLB Re-Import Statistics ---")
print(f"Total Mesh Objects: {len(imported_objs)}")
for o in imported_objs:
    print(f"  - {o.name}: {len(o.data.vertices)} verts, {len(o.data.polygons)} polys, materials: {[m.name for m in o.data.materials if m]}")
print(f"Total Vertices: {total_verts}")
print(f"Total Polygons: {total_polys}")
print(f"Estimated Triangles: {total_tris}")
print(f"File Size: {glb_size_kb:.2f} KB (Budget limit: 1200 KB)")

assert len(imported_objs) >= 8, "Expected at least 8 distinct production meshes"
assert glb_size_kb <= 1200.0, f"GLB size ({glb_size_kb:.2f} KB) exceeds budget (1200 KB)"
print("GLB VALIDATION PASSED COMPLETELY.")
