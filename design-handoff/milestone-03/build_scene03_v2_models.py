import bpy
import bmesh
import math
import os

out_dir = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references"
os.makedirs(out_dir, exist_ok=True)

# Clean slate
bpy.ops.wm.read_factory_settings(use_empty=True)

scene = bpy.context.scene
scene.name = "Scene03_V2_Redesign"
scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'RenderEngine') and 'BLENDER_EEVEE_NEXT' in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items] else 'BLENDER_EEVEE'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Color Management
scene.display_settings.display_device = 'sRGB'
scene.view_settings.view_transform = 'AgX' if 'AgX' in [v.identifier for v in scene.view_settings.bl_rna.properties['view_transform'].enum_items] else 'Filmic'
scene.view_settings.look = 'Medium High Contrast'
scene.view_settings.exposure = 0.22

# World Daylight
world = bpy.data.worlds.new("EXP_DaylightWorld_V2")
scene.world = world
world.use_nodes = True
nw = world.node_tree.nodes
nw.clear()
n_bg = nw.new(type='ShaderNodeBackground')
n_bg.inputs['Color'].default_value = (0.92, 0.96, 1.0, 1.0)
n_bg.inputs['Strength'].default_value = 1.7
n_out = nw.new(type='ShaderNodeOutputWorld')
world.node_tree.links.new(n_bg.outputs['Background'], n_out.inputs['Surface'])

# Collections
col_cand_a = bpy.data.collections.new("01_CandidateA_Motion")
col_cand_b = bpy.data.collections.new("02_CandidateB_Terraces")
col_cand_c = bpy.data.collections.new("03_CandidateC_Prism")
col_cams = bpy.data.collections.new("04_Cameras")
scene.collection.children.link(col_cand_a)
scene.collection.children.link(col_cand_b)
scene.collection.children.link(col_cand_c)
scene.collection.children.link(col_cams)

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

mat_plaster = make_pbr("MAT_V2_WhitePlaster", (0.97, 0.97, 0.96, 1.0), metallic=0.0, roughness=0.82)
mat_stone = make_pbr("MAT_V2_LightTravertine", (0.96, 0.95, 0.93, 1.0), metallic=0.02, roughness=0.18)
mat_dark_stone = make_pbr("MAT_V2_BasaltPath", (0.32, 0.34, 0.36, 1.0), metallic=0.05, roughness=0.30)
mat_aluminum = make_pbr("MAT_V2_BrushedAluminum", (0.94, 0.95, 0.97, 1.0), metallic=0.82, roughness=0.20)
mat_glass = make_pbr("MAT_V2_ClearGlass", (0.96, 0.98, 1.0, 1.0), metallic=0.0, roughness=0.02, transmission=0.96)
mat_frosted = make_pbr("MAT_V2_FrostedGlass", (0.94, 0.96, 0.99, 1.0), metallic=0.05, roughness=0.35, transmission=0.85)
mat_wood = make_pbr("MAT_V2_LightOak", (0.85, 0.76, 0.65, 1.0), metallic=0.0, roughness=0.55)

# Sunlight
sun_data = bpy.data.lights.new(name="V2_SunLight", type='SUN')
sun_data.color = (1.0, 0.98, 0.95)
sun_data.energy = 3.6
sun_obj = bpy.data.objects.new("V2_SunLight", sun_data)
sun_obj.rotation_euler = (math.radians(48.0), math.radians(24.0), math.radians(125.0))
col_cand_a.objects.link(sun_obj)

# Helper function to create cameras
def create_camera(name, loc, tgt, fov_deg=48.0, ortho_scale=0.0):
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

# ==============================================================================
# 1. BUILD CANDIDATE A: "EXPERTISE IN MOTION" (RECOMMENDED)
# ==============================================================================
# Seam anchor: (43.24, 19.98, 0.0) -> Pavilion extends East-South-East
# Dimensions: Length 34m, Width 18m, Height 6.5m to 10.5m (Sawtooth asymmetric roof)
P_ORIGIN = (43.24, 19.98, 0.0)

# 1A. Asymmetric Main Floor (Travertine with branching pathways)
mesh_fa = bpy.data.meshes.new("EXPA_Floor_Travertine")
bm = bmesh.new()
# Main rectangle rotated along tangent ~ -25 deg
cos_t = math.cos(math.radians(-25.0))
sin_t = math.sin(math.radians(-25.0))
norm_x = -sin_t
norm_y = cos_t

L_HALL = 36.0
W_HALL = 18.0

# Base corners of the asymmetric hall
def get_hall_xy(u, v):
    # u in [0, L_HALL], v in [-W_HALL/2, W_HALL/2]
    return (P_ORIGIN[0] + u * cos_t + v * norm_x, P_ORIGIN[1] + u * sin_t + v * norm_y)

c1 = get_hall_xy(0.0, -W_HALL/2.0)
c2 = get_hall_xy(L_HALL, -W_HALL/2.0)
c3 = get_hall_xy(L_HALL, W_HALL/2.0)
c4 = get_hall_xy(0.0, W_HALL/2.0)

vf1 = bm.verts.new((c1[0], c1[1], 0.0))
vf2 = bm.verts.new((c2[0], c2[1], 0.0))
vf3 = bm.verts.new((c3[0], c3[1], 0.0))
vf4 = bm.verts.new((c4[0], c4[1], 0.0))
bm.faces.new((vf1, vf2, vf3, vf4))

# 1B. Physical Branching Floor Pathways (As-Is -> To-Be process lines)
# Branch 1 (Straight Spine): width 1.8m
w_p = 1.0
p1_1 = get_hall_xy(2.0, -w_p)
p1_2 = get_hall_xy(16.0, -w_p)
p1_3 = get_hall_xy(16.0, w_p)
p1_4 = get_hall_xy(2.0, w_p)
vp1 = [bm.verts.new((x, y, 0.005)) for x, y in [p1_1, p1_2, p1_3, p1_4]]
bm.faces.new(vp1)

# Branch 2 (Branching out to North Alcove): from u=16, v=0 to u=28, v=6.0
p2_1 = get_hall_xy(16.0, w_p)
p2_2 = get_hall_xy(28.0, 5.0)
p2_3 = get_hall_xy(28.0, 7.0)
p2_4 = get_hall_xy(16.0, w_p + 1.2)
vp2 = [bm.verts.new((x, y, 0.005)) for x, y in [p2_1, p2_2, p2_3, p2_4]]
bm.faces.new(vp2)

bm.to_mesh(mesh_fa)
bm.free()
mesh_fa.update()
obj_fa = bpy.data.objects.new("EXPA_Floor", mesh_fa)
obj_fa.data.materials.append(mat_stone)
link_obj(obj_fa, col_cand_a)

# 1C. Asymmetrical Sawtooth Roof & Walls
mesh_wa = bpy.data.meshes.new("EXPA_Walls_Sawtooth")
bm_w = bmesh.new()

# Perimeter walls: South wall (low, 6.2m), North wall (high, 10.5m)
H_LOW = 6.20
H_HIGH = 10.50

# South wall (c1 -> c2)
vs1 = bm_w.verts.new((c1[0], c1[1], 0.0))
vs2 = bm_w.verts.new((c2[0], c2[1], 0.0))
vs2_t = bm_w.verts.new((c2[0], c2[1], H_LOW))
vs1_t = bm_w.verts.new((c1[0], c1[1], H_LOW))
bm_w.faces.new((vs1, vs2, vs2_t, vs1_t))

# North wall (c4 -> c3) with clerestory apertures
vn1 = bm_w.verts.new((c4[0], c4[1], 0.0))
vn2 = bm_w.verts.new((c3[0], c3[1], 0.0))
vn2_t = bm_w.verts.new((c3[0], c3[1], H_HIGH))
vn1_t = bm_w.verts.new((c4[0], c4[1], H_HIGH))
bm_w.faces.new((vn1, vn1_t, vn2_t, vn2))

# West wall with arched portal from K08
vw1 = bm_w.verts.new((c1[0], c1[1], 0.0))
vw2 = bm_w.verts.new((c4[0], c4[1], 0.0))
vw2_t = bm_w.verts.new((c4[0], c4[1], H_HIGH))
vw1_t = bm_w.verts.new((c1[0], c1[1], H_LOW))
bm_w.faces.new((vw1, vw1_t, vw2_t, vw2))

# East wall with exit portal toward Scene 04
ve1 = bm_w.verts.new((c2[0], c2[1], 0.0))
ve2 = bm_w.verts.new((c3[0], c3[1], 0.0))
ve2_t = bm_w.verts.new((c3[0], c3[1], H_HIGH))
ve1_t = bm_w.verts.new((c2[0], c2[1], H_LOW))
bm_w.faces.new((ve1, ve2, ve2_t, ve1_t))

# Sawtooth Roof Baffles (4 dramatic angled sawtooth bays with north clerestories)
N_SAW = 4
for si in range(N_SAW):
    u_start = (si / N_SAW) * L_HALL
    u_peak = ((si + 0.8) / N_SAW) * L_HALL
    u_end = ((si + 1.0) / N_SAW) * L_HALL
    
    # Sloped roof facet
    rf1 = get_hall_xy(u_start, -W_HALL/2.0)
    rf2 = get_hall_xy(u_start, W_HALL/2.0)
    rf3 = get_hall_xy(u_peak, W_HALL/2.0)
    rf4 = get_hall_xy(u_peak, -W_HALL/2.0)
    
    vr1 = bm_w.verts.new((rf1[0], rf1[1], H_LOW + 0.5*si))
    vr2 = bm_w.verts.new((rf2[0], rf2[1], H_HIGH))
    vr3 = bm_w.verts.new((rf3[0], rf3[1], H_HIGH + 1.2))
    vr4 = bm_w.verts.new((rf4[0], rf4[1], H_LOW + 0.5*si + 1.2))
    bm_w.faces.new((vr1, vr2, vr3, vr4))

bm_w.to_mesh(mesh_wa)
bm_w.free()
mesh_wa.update()
obj_wa = bpy.data.objects.new("EXPA_Walls_Sawtooth", mesh_wa)
obj_wa.data.materials.append(mat_plaster)
link_obj(obj_wa, col_cand_a)

# 1D. Monumental "System Spine" Architectural Installation (SAP / Enterprise)
# A multi-tiered modular framework of brushed aluminum beams and glowing glass volumes
mesh_spine = bpy.data.meshes.new("EXPA_SystemSpine_Installation")
bm_sp = bmesh.new()

# Grid: 4 bays along length (u: 14m to 24m), 2 bays deep (v: 2m to 6m), 3 tiers high (Z: 0.5m to 4.5m)
u_base = 15.0
v_base = 2.0
b_size = 2.4
h_tier = 1.4

for ix in range(4):
    for iy in range(2):
        for iz in range(3):
            # Cube center
            u_c = u_base + ix * b_size
            v_c = v_base + iy * b_size
            z_c = 0.5 + iz * h_tier
            p_c = get_hall_xy(u_c, v_c)
            
            # Aluminum frame struts
            s = b_size * 0.45
            h_s = h_tier * 0.45
            corners = [
                (p_c[0] - s*cos_t - s*norm_x, p_c[1] - s*sin_t - s*norm_y),
                (p_c[0] + s*cos_t - s*norm_x, p_c[1] + s*sin_t - s*norm_y),
                (p_c[0] + s*cos_t + s*norm_x, p_c[1] + s*sin_t + s*norm_y),
                (p_c[0] - s*cos_t + s*norm_x, p_c[1] - s*sin_t + s*norm_y)
            ]
            vb = [bm_sp.verts.new((x, y, z_c - h_s)) for x, y in corners]
            vt = [bm_sp.verts.new((x, y, z_c + h_s)) for x, y in corners]
            for c_i in range(4):
                next_c = (c_i + 1) % 4
                bm_sp.faces.new((vb[c_i], vb[next_c], vt[next_c], vt[c_i]))
            bm_sp.faces.new(vb)
            bm_sp.faces.new(vt)

bm_sp.to_mesh(mesh_spine)
bm_sp.free()
mesh_spine.update()
obj_spine = bpy.data.objects.new("EXPA_SystemSpine", mesh_spine)
obj_spine.data.materials.append(mat_aluminum)
link_obj(obj_spine, col_cand_a)

# 1E. Suspended Connecting Bridge (Solution Consulting / Exit toward Scene 04)
# Elevated bridge running from u = 24m to u = 36m at Z = 2.4m, width 3.2m
mesh_bridge = bpy.data.meshes.new("EXPA_SuspendedBridge")
bm_br = bmesh.new()

br_u1 = 22.0
br_u2 = 36.0
br_w = 3.2
br_z = 2.40

br_1 = get_hall_xy(br_u1, -br_w/2.0)
br_2 = get_hall_xy(br_u2, -br_w/2.0)
br_3 = get_hall_xy(br_u2, br_w/2.0)
br_4 = get_hall_xy(br_u1, br_w/2.0)

vbr1 = bm_br.verts.new((br_1[0], br_1[1], br_z))
vbr2 = bm_br.verts.new((br_2[0], br_2[1], br_z))
vbr3 = bm_br.verts.new((br_3[0], br_3[1], br_z))
vbr4 = bm_br.verts.new((br_4[0], br_4[1], br_z))
bm_br.faces.new((vbr1, vbr2, vbr3, vbr4))

# Glass balustrades
H_BAL = 1.10
vbr1_t = bm_br.verts.new((br_1[0], br_1[1], br_z + H_BAL))
vbr2_t = bm_br.verts.new((br_2[0], br_2[1], br_z + H_BAL))
vbr3_t = bm_br.verts.new((br_3[0], br_3[1], br_z + H_BAL))
vbr4_t = bm_br.verts.new((br_4[0], br_4[1], br_z + H_BAL))
bm_br.faces.new((vbr1, vbr2, vbr2_t, vbr1_t)) # South glass
bm_br.faces.new((vbr4, vbr4_t, vbr3_t, vbr3)) # North glass

bm_br.to_mesh(mesh_bridge)
bm_br.free()
mesh_bridge.update()
obj_bridge = bpy.data.objects.new("EXPA_SuspendedBridge", mesh_bridge)
obj_bridge.data.materials.append(mat_stone)
link_obj(obj_bridge, col_cand_a)

# ==============================================================================
# 2. BUILD CANDIDATE B: "THE STEP-TERRACE HALL" (TIERED LINEAR GALLERY)
# Placed offset along Y by +40m to render independently
# ==============================================================================
mesh_tb = bpy.data.meshes.new("EXPB_StepTerraces")
bm_tb = bmesh.new()
# Ascending platforms: Tier 1 (Z=0), Tier 2 (Z=1.2m), Tier 3 (Z=2.4m), Tier 4 (Z=3.6m)
for ti in range(4):
    tx0 = 43.24 + ti * 7.0
    tx1 = tx0 + 6.8
    tz = ti * 1.2
    ty0 = 55.0
    ty1 = 70.0
    v1 = bm_tb.verts.new((tx0, ty0, tz))
    v2 = bm_tb.verts.new((tx1, ty0, tz))
    v3 = bm_tb.verts.new((tx1, ty1, tz))
    v4 = bm_tb.verts.new((tx0, ty1, tz))
    bm_tb.faces.new((v1, v2, v3, v4))
    # Step riser
    if ti > 0:
        vr1 = bm_tb.verts.new((tx0, ty0, (ti-1)*1.2))
        vr4 = bm_tb.verts.new((tx0, ty1, (ti-1)*1.2))
        bm_tb.faces.new((vr1, v1, v4, vr4))

# Tall curtain wall along North
vcw1 = bm_tb.verts.new((43.24, 70.0, 0.0))
vcw2 = bm_tb.verts.new((43.24 + 28.0, 70.0, 0.0))
vcw2_t = bm_tb.verts.new((43.24 + 28.0, 70.0, 9.0))
vcw1_t = bm_tb.verts.new((43.24, 70.0, 9.0))
bm_tb.faces.new((vcw1, vcw2, vcw2_t, vcw1_t))

bm_tb.to_mesh(mesh_tb)
bm_tb.free()
mesh_tb.update()
obj_tb = bpy.data.objects.new("EXPB_StepTerraces", mesh_tb)
obj_tb.data.materials.append(mat_stone)
link_obj(obj_tb, col_cand_b)

# ==============================================================================
# 3. BUILD CANDIDATE C: "THE PRISM PAVILION" (ANGULAR CRYSTALLINE LIGHT-WELLS)
# Placed offset along Y by -40m to render independently
# ==============================================================================
mesh_tc = bpy.data.meshes.new("EXPC_PrismPavilion")
bm_tc = bmesh.new()
# Faceted triangular / hexagonal crystalline volumes
poly_pts = [
    (43.24, -25.0, 0.0),
    (54.00, -38.0, 0.0),
    (68.00, -32.0, 0.0),
    (74.00, -18.0, 0.0),
    (62.00, -12.0, 0.0),
    (48.00, -15.0, 0.0)
]
vp_floor = [bm_tc.verts.new(p) for p in poly_pts]
bm_tc.faces.new(vp_floor)

# Faceted angled walls leaning inward to form geometric light shafts
for pi in range(len(poly_pts)):
    next_pi = (pi + 1) % len(poly_pts)
    v_b1 = vp_floor[pi]
    v_b2 = vp_floor[next_pi]
    # Angled top vertices leaning inward
    p1 = poly_pts[pi]
    p2 = poly_pts[next_pi]
    v_t1 = bm_tc.verts.new((p1[0] * 0.9 + 5.8, p1[1] * 0.9 - 2.5, 8.5))
    v_t2 = bm_tc.verts.new((p2[0] * 0.9 + 5.8, p2[1] * 0.9 - 2.5, 8.5))
    bm_tc.faces.new((v_b1, v_b2, v_t2, v_t1))

bm_tc.to_mesh(mesh_tc)
bm_tc.free()
mesh_tc.update()
obj_tc = bpy.data.objects.new("EXPC_PrismPavilion", mesh_tc)
obj_tc.data.materials.append(mat_plaster)
link_obj(obj_tc, col_cand_c)

# ==============================================================================
# CAMERAS SETUP & RENDERING
# ==============================================================================
# Candidate A Hero View
cam_cand_a = create_camera("CAM_CandA_Hero", (46.0, 22.0, 2.4), (64.0, 11.0, 3.2), fov_deg=52.0)

# Candidate B Hero View
cam_cand_b = create_camera("CAM_CandB_Hero", (44.0, 52.0, 2.5), (62.0, 62.0, 3.5), fov_deg=50.0)

# Candidate C Hero View
cam_cand_c = create_camera("CAM_CandC_Hero", (45.0, -14.0, 2.2), (60.0, -25.0, 3.0), fov_deg=52.0)

# Candidate A Keyframes (The 4 Distinct Scrollytelling Frames)
# K09: Reveal through compressed portal into soaring asymmetric space
p_k09_loc = get_hall_xy(1.5, 0.0)
p_k09_tgt = get_hall_xy(14.0, 2.0)
cam_k09 = create_camera("CAM_K09_Reveal", (p_k09_loc[0], p_k09_loc[1], 1.85), (p_k09_tgt[0], p_k09_tgt[1], 3.8), fov_deg=52.0)

# K10: Elevated oblique view overlooking the As-Is -> To-Be branching floor pathways
p_k10_loc = get_hall_xy(9.0, -4.5)
p_k10_tgt = get_hall_xy(18.0, 2.0)
cam_k10 = create_camera("CAM_K10_Paths", (p_k10_loc[0], p_k10_loc[1], 3.20), (p_k10_tgt[0], p_k10_tgt[1], 0.20), fov_deg=46.0)

# K11: Side tracking shot past the modular aluminum/glass System Spine installation
p_k11_loc = get_hall_xy(17.0, -4.2)
p_k11_tgt = get_hall_xy(19.0, 3.2)
cam_k11 = create_camera("CAM_K11_Spine", (p_k11_loc[0], p_k11_loc[1], 1.85), (p_k11_tgt[0], p_k11_tgt[1], 2.20), fov_deg=48.0)

# K12: Forward bridge perspective looking across suspended bridge toward Scene 04 portal
p_k12_loc = get_hall_xy(24.0, 0.0)
p_k12_tgt = get_hall_xy(37.0, 0.0)
cam_k12 = create_camera("CAM_K12_Bridge", (p_k12_loc[0], p_k12_loc[1], br_z + 1.65), (p_k12_tgt[0], p_k12_tgt[1], br_z + 1.80), fov_deg=50.0)

# Top-Down Orthographic Spatial Route Camera for Candidate A
cam_top_a = create_camera("CAM_TopDown_A", (60.0, 12.0, 48.0), (60.0, 12.0, 0.0), ortho_scale=42.0)

# EXECUTE RENDERS
renders = [
    (cam_cand_a, "candidate-A-expertise-in-motion.png"),
    (cam_cand_b, "candidate-B-step-terrace-hall.png"),
    (cam_cand_c, "candidate-C-prism-pavilion.png"),
    (cam_k09, "keyframe-K09-v2-reveal.png"),
    (cam_k10, "keyframe-K10-v2-process-paths.png"),
    (cam_k11, "keyframe-K11-v2-system-spine.png"),
    (cam_k12, "keyframe-K12-v2-bridge-portal.png"),
    (cam_top_a, "06-raw-topdown-v2.png")
]

for cam, filename in renders:
    scene.camera = cam
    scene.render.filepath = os.path.join(out_dir, filename)
    bpy.ops.render.render(write_still=True)
    print("Rendered:", filename)

# Save blend file
blend_path = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\scene03-v2-exploration.blend"
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print("Saved Blend file:", blend_path)
