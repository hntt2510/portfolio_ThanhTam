import bpy
import bmesh
import math
import os
import shutil
from mathutils import Vector, Euler, Matrix

OUT_DIR = r"d:\THANHTAM\CV\Portfolio\design-handoff\milestone-01A"
ARTIFACT_DIR = r"C:\Users\LEGION\.gemini\antigravity\brain\3948c36f-fc7d-4ae0-b3e9-358d2b5f3cc7"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.scale_length = 1.0
    if hasattr(scene.eevee, "use_raytracing"):
        scene.eevee.use_raytracing = True
    if hasattr(scene.eevee, "shadow_resolution_scale"):
        scene.eevee.shadow_resolution_scale = 2.0

def hex_to_linear(hex_str):
    hex_str = hex_str.lstrip('#')
    r = int(hex_str[0:2], 16) / 255.0
    g = int(hex_str[2:4], 16) / 255.0
    b = int(hex_str[4:6], 16) / 255.0
    def to_lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    return (to_lin(r), to_lin(g), to_lin(b), 1.0)

def create_pbr_material(name, hex_color, roughness=0.5, metallic=0.0, transmission=0.0, ior=1.5):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = hex_to_linear(hex_color)
        bsdf.inputs["Roughness"].default_value = roughness
        bsdf.inputs["Metallic"].default_value = metallic
        if "Transmission Weight" in bsdf.inputs:
            bsdf.inputs["Transmission Weight"].default_value = transmission
        elif "Transmission" in bsdf.inputs:
            bsdf.inputs["Transmission"].default_value = transmission
        if "IOR" in bsdf.inputs:
            bsdf.inputs["IOR"].default_value = ior
    if transmission > 0.5:
        if hasattr(mat, "use_raytrace_refraction"):
            mat.use_raytrace_refraction = True
        if hasattr(mat, "use_screen_refraction"):
            mat.use_screen_refraction = True
        if hasattr(mat, "refraction_depth"):
            mat.refraction_depth = 0.14
        if hasattr(mat, "blend_method"):
            mat.blend_method = 'HASHED'
        if hasattr(mat, "use_transparent_shadow"):
            mat.use_transparent_shadow = True
    return mat

def create_thick_curved_wall(name, r_in, r_out, height, start_angle, end_angle, segments=48):
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    span = end_angle - start_angle
    
    in_bottom, in_top = [], []
    out_bottom, out_top = [], []
    
    for i in range(segments + 1):
        a = start_angle + (i / segments) * span
        cos_a, sin_a = math.cos(a), math.sin(a)
        in_bottom.append(bm.verts.new((cos_a * r_in, sin_a * r_in, 0.0)))
        in_top.append(bm.verts.new((cos_a * r_in, sin_a * r_in, height)))
        out_bottom.append(bm.verts.new((cos_a * r_out, sin_a * r_out, 0.0)))
        out_top.append(bm.verts.new((cos_a * r_out, sin_a * r_out, height)))
        
    bm.verts.ensure_lookup_table()
    
    for i in range(segments):
        # Inner face (facing center)
        bm.faces.new([in_bottom[i], in_top[i], in_top[i+1], in_bottom[i+1]])
        # Outer face (facing outward)
        bm.faces.new([out_bottom[i+1], out_top[i+1], out_top[i], out_bottom[i]])
        # Top cap
        bm.faces.new([in_top[i], out_top[i], out_top[i+1], in_top[i+1]])
        # Bottom cap
        bm.faces.new([in_bottom[i+1], out_bottom[i+1], out_bottom[i], in_bottom[i]])
        
    # Start cap
    bm.faces.new([in_bottom[0], out_bottom[0], out_top[0], in_top[0]])
    # End cap
    bm.faces.new([in_top[-1], out_top[-1], out_bottom[-1], in_bottom[-1]])
    
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    return obj

def create_ring_soffit(name, r_in, r_out, z, thickness=0.2, segments=64):
    mesh = bpy.data.meshes.new(name)
    bm = bmesh.new()
    
    b_in, b_out = [], []
    t_in, t_out = [], []
    
    for i in range(segments):
        a = (i / segments) * math.pi * 2
        cos_a, sin_a = math.cos(a), math.sin(a)
        b_in.append(bm.verts.new((cos_a * r_in, sin_a * r_in, z)))
        b_out.append(bm.verts.new((cos_a * r_out, sin_a * r_out, z)))
        t_in.append(bm.verts.new((cos_a * r_in, sin_a * r_in, z + thickness)))
        t_out.append(bm.verts.new((cos_a * r_out, sin_a * r_out, z + thickness)))
        
    bm.verts.ensure_lookup_table()
    for i in range(segments):
        nxt = (i + 1) % segments
        # Bottom face
        bm.faces.new([b_in[i], b_in[nxt], b_out[nxt], b_out[i]])
        # Top face
        bm.faces.new([t_out[i], t_out[nxt], t_in[nxt], t_in[i]])
        # Inner vertical rim
        bm.faces.new([b_in[nxt], b_in[i], t_in[i], t_in[nxt]])
        # Outer vertical rim
        bm.faces.new([b_out[i], b_out[nxt], t_out[nxt], t_out[i]])
        
    bm.to_mesh(mesh)
    bm.free()
    obj = bpy.data.objects.new(name, mesh)
    return obj

def build_scene():
    reset_scene()

    # World Lighting
    world = bpy.context.scene.world
    if not world:
        world = bpy.data.worlds.new("Museum_World")
        bpy.context.scene.world = world
    world.use_nodes = True
    bg_node = world.node_tree.nodes.get("Background")
    if bg_node:
        bg_node.inputs["Color"].default_value = hex_to_linear("#EBF3FA")
        bg_node.inputs["Strength"].default_value = 1.35

    # Materials
    mat_plaster = create_pbr_material("MAT_WhitePlaster", "#F7F8F6", roughness=0.82)
    mat_stone = create_pbr_material("MAT_LightStone", "#EDEDE9", roughness=0.34, metallic=0.03)
    mat_aluminum = create_pbr_material("MAT_BrushedAluminum", "#D4DBE0", roughness=0.22, metallic=0.90)
    mat_glass = create_pbr_material("MAT_FrostedGlass", "#EAF4FB", roughness=0.15, transmission=0.94, ior=1.52)
    mat_accent_blue = create_pbr_material("MAT_AccentBlue", "#6F9EC8", roughness=0.25, metallic=0.1)
    mat_cove = create_pbr_material("MAT_CoveLight", "#FFFDF8", roughness=0.9)

    # Collections Hierarchy
    col_root = bpy.data.collections.new("ATR_WorldRoot")
    bpy.context.scene.collection.children.link(col_root)
    col_arch = bpy.data.collections.new("ATR_Architecture")
    col_corridor = bpy.data.collections.new("ATR_Corridor")
    col_install = bpy.data.collections.new("ATR_Installation")
    col_cameras = bpy.data.collections.new("ATR_CameraGuides")
    col_render = bpy.data.collections.new("ATR_RenderOnly")
    for c in [col_arch, col_corridor, col_install, col_cameras, col_render]:
        col_root.children.link(c)

    exportable = []
    def link_arch(o):
        col_arch.objects.link(o)
        exportable.append(o)
    def link_corridor(o):
        col_corridor.objects.link(o)
        exportable.append(o)
    def link_install(o):
        col_install.objects.link(o)
        exportable.append(o)

    # ==========================================
    # 1. FLOOR & PERIMETER ARCHITECTURE
    # ==========================================
    # Main Atrium Stone Floor (Disc R=14.0m)
    bpy.ops.mesh.primitive_cylinder_add(radius=14.0, depth=0.3, vertices=64, location=(0, 0, -0.15))
    floor = bpy.context.active_object
    floor.name = "ATR_Floor"
    floor.data.materials.append(mat_stone)
    link_arch(floor)

    # Concentric floor aluminum joint rings
    for r in [4.5, 7.8, 11.0]:
        bpy.ops.mesh.primitive_torus_add(major_radius=r, minor_radius=0.02, major_segments=64, minor_segments=8, location=(0, 0, 0.005))
        j_ring = bpy.context.active_object
        j_ring.name = f"ATR_FloorJoint_{int(r*10)}dm"
        j_ring.data.materials.append(mat_aluminum)
        link_arch(j_ring)

    # Curved Architectural Walls with Openings:
    # Opening 1: Entrance at South (-Y, angle 252° to 288°) -> 36° opening
    # Opening 2: Corridor at North-East (+X, +Y, angle 33° to 57°) -> 24° opening
    # Wall West: from 57° to 252° (covers full west / left gallery wall)
    wall_west = create_thick_curved_wall("ATR_CurvedWall_West", r_in=11.2, r_out=11.6, height=9.2,
                                         start_angle=math.radians(57), end_angle=math.radians(252), segments=40)
    wall_west.data.materials.append(mat_plaster)
    link_arch(wall_west)

    # Wall East: from 288° to 393° (33°) (covers south-east perimeter)
    wall_east = create_thick_curved_wall("ATR_CurvedWall_East", r_in=11.2, r_out=11.6, height=9.2,
                                         start_angle=math.radians(288), end_angle=math.radians(393), segments=24)
    wall_east.data.materials.append(mat_plaster)
    link_arch(wall_east)

    # Pilasters / Columns around interior perimeter
    # 16 positions, but skip entrance (240°-300°) and corridor (25°-65°)
    for i in range(16):
        deg = (i / 16.0) * 360.0
        if (240 <= deg <= 300) or (25 <= deg <= 65):
            continue
        rad = math.radians(deg)
        x = math.cos(rad) * 11.0
        y = math.sin(rad) * 11.0
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(x, y, 4.6))
        pil = bpy.context.active_object
        pil.scale = (0.45, 0.35, 9.2)
        pil.rotation_euler = (0, 0, rad)
        pil.name = f"ATR_Pilaster_{i:02d}"
        pil.data.materials.append(mat_plaster)
        link_arch(pil)

    # Mezzanine Gallery Balcony Ring at height 5.0m
    mezz_slab = create_ring_soffit("ATR_MezzanineSlab", r_in=10.7, r_out=11.3, z=4.9, thickness=0.25, segments=64)
    mezz_slab.data.materials.append(mat_stone)
    link_arch(mezz_slab)

    # Mezzanine Glass Balustrade
    bpy.ops.mesh.primitive_cylinder_add(radius=10.72, depth=0.9, vertices=64, location=(0, 0, 5.6), end_fill_type='NOTHING')
    railing = bpy.context.active_object
    railing.name = "ATR_MezzanineRailingGlass"
    railing.data.materials.append(mat_glass)
    link_arch(railing)

    # Mezzanine Aluminum Handrail
    bpy.ops.mesh.primitive_torus_add(major_radius=10.72, minor_radius=0.03, major_segments=64, minor_segments=8, location=(0, 0, 6.08))
    handrail = bpy.context.active_object
    handrail.name = "ATR_MezzanineHandrail"
    handrail.data.materials.append(mat_aluminum)
    link_arch(handrail)

    # ==========================================
    # 2. ENTRANCE PORTAL (SOUTH, -Y)
    # ==========================================
    # Hollow archway: Left post, Right post, Top header
    ent_width = 5.2
    ent_h = 6.0
    # Left post
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(-ent_width/2.0, -11.2, ent_h/2.0))
    ent_p_l = bpy.context.active_object
    ent_p_l.scale = (0.35, 0.45, ent_h)
    ent_p_l.name = "ATR_EntrancePortal_PostL"
    ent_p_l.data.materials.append(mat_aluminum)
    link_arch(ent_p_l)

    # Right post
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(ent_width/2.0, -11.2, ent_h/2.0))
    ent_p_r = bpy.context.active_object
    ent_p_r.scale = (0.35, 0.45, ent_h)
    ent_p_r.name = "ATR_EntrancePortal_PostR"
    ent_p_r.data.materials.append(mat_aluminum)
    link_arch(ent_p_r)

    # Top header
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, -11.2, ent_h + 0.15))
    ent_header = bpy.context.active_object
    ent_header.scale = (ent_width + 0.35, 0.45, 0.3)
    ent_header.name = "ATR_EntrancePortal_Header"
    ent_header.data.materials.append(mat_aluminum)
    link_arch(ent_header)

    # Threshold vestibule side walls
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(-ent_width/2.0 - 0.2, -12.4, 3.2))
    ent_w_left = bpy.context.active_object
    ent_w_left.scale = (0.4, 2.0, 6.4)
    ent_w_left.name = "ATR_EntranceWall_Left"
    ent_w_left.data.materials.append(mat_plaster)
    link_arch(ent_w_left)

    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(ent_width/2.0 + 0.2, -12.4, 3.2))
    ent_w_right = bpy.context.active_object
    ent_w_right.scale = (0.4, 2.0, 6.4)
    ent_w_right.name = "ATR_EntranceWall_Right"
    ent_w_right.data.materials.append(mat_plaster)
    link_arch(ent_w_right)

    # ==========================================
    # 3. CEILING & SKYLIGHT STRUCTURE
    # ==========================================
    # Lower soffit ring (R=8.2m to 11.6m at Z=8.8m)
    ceil_lower = create_ring_soffit("ATR_CeilingSoffit_Lower", r_in=8.2, r_out=11.6, z=8.8, thickness=0.3, segments=64)
    ceil_lower.data.materials.append(mat_plaster)
    link_arch(ceil_lower)

    # Cove light ring
    bpy.ops.mesh.primitive_torus_add(major_radius=8.2, minor_radius=0.04, major_segments=64, minor_segments=8, location=(0, 0, 9.15))
    cove_ring = bpy.context.active_object
    cove_ring.name = "ATR_CeilingCoveLight"
    cove_ring.data.materials.append(mat_cove)
    link_arch(cove_ring)

    # Upper soffit ring (R=5.2m to 8.2m at Z=9.4m)
    ceil_upper = create_ring_soffit("ATR_CeilingSoffit_Upper", r_in=5.2, r_out=8.2, z=9.4, thickness=0.3, segments=64)
    ceil_upper.data.materials.append(mat_plaster)
    link_arch(ceil_upper)

    # Skylight outer aluminum ring (R=5.2m at Z=9.9m)
    bpy.ops.mesh.primitive_torus_add(major_radius=5.2, minor_radius=0.1, major_segments=64, minor_segments=16, location=(0, 0, 9.9))
    sky_ring = bpy.context.active_object
    sky_ring.name = "ATR_SkylightRing"
    sky_ring.data.materials.append(mat_aluminum)
    link_arch(sky_ring)

    # Skylight inner aluminum ring (R=2.6m at Z=10.3m)
    bpy.ops.mesh.primitive_torus_add(major_radius=2.6, minor_radius=0.06, major_segments=64, minor_segments=16, location=(0, 0, 10.3))
    inner_ring = bpy.context.active_object
    inner_ring.name = "ATR_SkylightInnerRing"
    inner_ring.data.materials.append(mat_aluminum)
    link_arch(inner_ring)

    # 12 Radial aluminum mullions
    mullions = []
    for i in range(12):
        a = (i / 12.0) * math.pi * 2
        mx = math.cos(a) * 2.6
        my = math.sin(a) * 2.6
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(mx, my, 10.15))
        m = bpy.context.active_object
        m.scale = (5.2, 0.08, 0.06)
        m.rotation_euler = (0, 0.04, a)
        m.name = f"ATR_SkylightMullion_{i:02d}"
        m.data.materials.append(mat_aluminum)
        link_arch(m)
        mullions.append(m)

    # Translucent Domed Skylight Glass
    bpy.ops.mesh.primitive_uv_sphere_add(radius=5.2, segments=32, ring_count=16, location=(0, 0, 9.3))
    sky_glass = bpy.context.active_object
    sky_glass.scale = (1.0, 1.0, 0.22)
    sky_glass.name = "ATR_SkylightGlass"
    sky_glass.data.materials.append(mat_glass)
    link_arch(sky_glass)

    # ==========================================
    # 4. CENTRAL INSTALLATION (RIGHT BIAS X=1.4m)
    # ==========================================
    inst_x = 1.4
    inst_y = 0.0

    # Low Circular Stone Pedestal (Radius 2.2m, Height 0.32m)
    bpy.ops.mesh.primitive_cylinder_add(radius=2.2, depth=0.32, vertices=64, location=(inst_x, inst_y, 0.16))
    pedestal = bpy.context.active_object
    pedestal.name = "ATR_Pedestal"
    pedestal.data.materials.append(mat_stone)
    link_install(pedestal)

    # Pedestal upper brushed aluminum trim
    bpy.ops.mesh.primitive_torus_add(major_radius=2.22, minor_radius=0.025, major_segments=64, minor_segments=16, location=(inst_x, inst_y, 0.31))
    ped_trim = bpy.context.active_object
    ped_trim.name = "ATR_PedestalTrim"
    ped_trim.data.materials.append(mat_aluminum)
    link_install(ped_trim)

    # Recessed Blue LED Halo Ring on floor around plinth
    bpy.ops.mesh.primitive_torus_add(major_radius=2.45, minor_radius=0.03, major_segments=64, minor_segments=16, location=(inst_x, inst_y, 0.01))
    halo = bpy.context.active_object
    halo.name = "ATR_FloorHalo"
    halo.data.materials.append(mat_accent_blue)
    link_install(halo)

    # Three Staggered Frosted-Glass Monoliths:
    # Panel 01: Front-Left (Business Analysis), wide landscape
    # Panel 02: Center-Rear (Enterprise Systems), tall vertical monolithic hero
    # Panel 03: Front-Right (Technology Solutions), medium vertical
    panels_data = [
        {
            'name': 'ATR_GlassPanel_01',
            'w': 2.2, 'h': 1.35, 'd': 0.14,
            'pos': (inst_x - 0.72, inst_y - 0.42, 0.32 + 1.35 / 2.0),
            'yaw': math.radians(4.0)
        },
        {
            'name': 'ATR_GlassPanel_02',
            'w': 1.9, 'h': 3.0, 'd': 0.14,
            'pos': (inst_x + 0.10, inst_y + 0.38, 0.32 + 3.0 / 2.0),
            'yaw': math.radians(-3.0)
        },
        {
            'name': 'ATR_GlassPanel_03',
            'w': 1.6, 'h': 2.1, 'd': 0.14,
            'pos': (inst_x + 0.86, inst_y - 0.22, 0.32 + 2.1 / 2.0),
            'yaw': math.radians(8.0)
        }
    ]

    for p in panels_data:
        # Glass Monolith Core
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=p['pos'])
        slab = bpy.context.active_object
        slab.scale = (p['w'], p['d'], p['h'])
        slab.rotation_euler = (0, 0, p['yaw'])
        slab.name = p['name']
        slab.data.materials.append(mat_glass)
        link_install(slab)

        # Aluminum Channel Edge Trim
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=p['pos'])
        frame = bpy.context.active_object
        frame.scale = (p['w'] + 0.035, p['d'] + 0.02, p['h'] + 0.035)
        frame.rotation_euler = (0, 0, p['yaw'])
        frame.name = f"{p['name']}_Frame"
        frame.data.materials.append(mat_aluminum)
        link_install(frame)

        # Floor Mounting Clamp Shoes
        cos_y, sin_y = math.cos(p['yaw']), math.sin(p['yaw'])
        for sx in [-0.34 * p['w'], 0.34 * p['w']]:
            px = p['pos'][0] + sx * cos_y
            py = p['pos'][1] + sx * sin_y
            bpy.ops.mesh.primitive_cube_add(size=1.0, location=(px, py, 0.32 + 0.06))
            shoe = bpy.context.active_object
            shoe.scale = (0.24, p['d'] + 0.06, 0.12)
            shoe.rotation_euler = (0, 0, p['yaw'])
            shoe.name = f"{p['name']}_MountShoe"
            shoe.data.materials.append(mat_aluminum)
            link_install(shoe)

    # ==========================================
    # 5. CORRIDOR (NORTH-EAST, 45° HEADING)
    # ==========================================
    # Heading 45 deg from center
    cor_heading = math.radians(45.0)
    c_cos = math.cos(cor_heading)
    c_sin = math.sin(cor_heading)
    # Perpendicular unit vector (points toward top-left of corridor)
    p_cos = -c_sin
    p_sin = c_cos

    r_start = 11.2
    c_len = 10.0
    c_w = 4.0
    half_w = c_w / 2.0

    # Start position of corridor center at atrium wall
    c_start_x = r_start * c_cos
    c_start_y = r_start * c_sin

    # Corridor Floor (Light Stone)
    cor_mesh = bpy.data.meshes.new("ATR_CorridorFloor")
    bm_c = bmesh.new()
    v1 = bm_c.verts.new((c_start_x - half_w * p_cos, c_start_y - half_w * p_sin, -0.05))
    v2 = bm_c.verts.new((c_start_x + half_w * p_cos, c_start_y + half_w * p_sin, -0.05))
    end_x = c_start_x + c_len * c_cos
    end_y = c_start_y + c_len * c_sin
    v3 = bm_c.verts.new((end_x + half_w * p_cos, end_y + half_w * p_sin, -0.05))
    v4 = bm_c.verts.new((end_x - half_w * p_cos, end_y - half_w * p_sin, -0.05))
    bm_c.faces.new([v1, v2, v3, v4])
    bm_c.to_mesh(cor_mesh)
    bm_c.free()
    cor_floor_obj = bpy.data.objects.new("ATR_CorridorFloor", cor_mesh)
    cor_floor_obj.data.materials.append(mat_stone)
    link_corridor(cor_floor_obj)

    # Corridor Portal Frame (Hollow Archway at opening)
    # Left post
    pos_lp_x = c_start_x + half_w * p_cos
    pos_lp_y = c_start_y + half_w * p_sin
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(pos_lp_x, pos_lp_y, 3.0))
    cor_post_l = bpy.context.active_object
    cor_post_l.scale = (0.35, 0.4, 6.0)
    cor_post_l.rotation_euler = (0, 0, cor_heading)
    cor_post_l.name = "ATR_CorridorPortal_PostL"
    cor_post_l.data.materials.append(mat_aluminum)
    link_corridor(cor_post_l)

    # Right post
    pos_rp_x = c_start_x - half_w * p_cos
    pos_rp_y = c_start_y - half_w * p_sin
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(pos_rp_x, pos_rp_y, 3.0))
    cor_post_r = bpy.context.active_object
    cor_post_r.scale = (0.35, 0.4, 6.0)
    cor_post_r.rotation_euler = (0, 0, cor_heading)
    cor_post_r.name = "ATR_CorridorPortal_PostR"
    cor_post_r.data.materials.append(mat_aluminum)
    link_corridor(cor_post_r)

    # Header lintel
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(c_start_x, c_start_y, 6.15))
    cor_lintel = bpy.context.active_object
    cor_lintel.scale = (c_w + 0.35, 0.4, 0.3)
    cor_lintel.rotation_euler = (0, 0, cor_heading - math.pi/2.0)
    cor_lintel.name = "ATR_CorridorPortal_Header"
    cor_lintel.data.materials.append(mat_aluminum)
    link_corridor(cor_lintel)

    # Corridor Right Wall (Smooth Warm Plaster)
    # Extends from right post to end of corridor
    r_wall_mesh = bpy.data.meshes.new("ATR_CorridorWall_Right")
    bm_rw = bmesh.new()
    rw_start_x = c_start_x - half_w * p_cos
    rw_start_y = c_start_y - half_w * p_sin
    rw_end_x = end_x - half_w * p_cos
    rw_end_y = end_y - half_w * p_sin
    # Wall thickness 0.35m extending outward
    th = 0.35
    w_b1 = bm_rw.verts.new((rw_start_x, rw_start_y, 0.0))
    w_t1 = bm_rw.verts.new((rw_start_x, rw_start_y, 6.0))
    w_t2 = bm_rw.verts.new((rw_end_x, rw_end_y, 6.0))
    w_b2 = bm_rw.verts.new((rw_end_x, rw_end_y, 0.0))
    # Inner face
    bm_rw.faces.new([w_b1, w_t1, w_t2, w_b2])
    bm_rw.to_mesh(r_wall_mesh)
    bm_rw.free()
    cor_r_wall_obj = bpy.data.objects.new("ATR_CorridorWall_Right", r_wall_mesh)
    cor_r_wall_obj.data.materials.append(mat_plaster)
    link_corridor(cor_r_wall_obj)

    # Corridor Left Wall (Architectural wall with tall daylight window apertures)
    l_wall_mesh = bpy.data.meshes.new("ATR_CorridorWall_Left")
    bm_lw = bmesh.new()
    lw_start_x = c_start_x + half_w * p_cos
    lw_start_y = c_start_y + half_w * p_sin
    lw_end_x = end_x + half_w * p_cos
    lw_end_y = end_y + half_w * p_sin
    lw_b1 = bm_lw.verts.new((lw_start_x, lw_start_y, 0.0))
    lw_t1 = bm_lw.verts.new((lw_start_x, lw_start_y, 6.0))
    lw_t2 = bm_lw.verts.new((lw_end_x, lw_end_y, 6.0))
    lw_b2 = bm_lw.verts.new((lw_end_x, lw_end_y, 0.0))
    bm_lw.faces.new([lw_b1, lw_b2, lw_t2, lw_t1])
    bm_lw.to_mesh(l_wall_mesh)
    bm_lw.free()
    cor_l_wall_obj = bpy.data.objects.new("ATR_CorridorWall_Left", l_wall_mesh)
    cor_l_wall_obj.data.materials.append(mat_plaster)
    link_corridor(cor_l_wall_obj)

    # Left wall window mullions (3 vertical window openings)
    for k in range(3):
        frac = 0.25 + k * 0.3
        wx = c_start_x + (c_len * frac) * c_cos + half_w * p_cos
        wy = c_start_y + (c_len * frac) * c_sin + half_w * p_sin
        bpy.ops.mesh.primitive_cube_add(size=1.0, location=(wx, wy, 3.0))
        mull = bpy.context.active_object
        mull.scale = (0.2, 0.35, 5.8)
        mull.rotation_euler = (0, 0, cor_heading)
        mull.name = f"ATR_CorridorWindowMullion_{k:02d}"
        mull.data.materials.append(mat_aluminum)
        link_corridor(mull)

    # Corridor Ceiling
    c_ceil_mesh = bpy.data.meshes.new("ATR_CorridorCeiling")
    bm_cc = bmesh.new()
    c1 = bm_cc.verts.new((rw_start_x, rw_start_y, 6.0))
    c2 = bm_cc.verts.new((lw_start_x, lw_start_y, 6.0))
    c3 = bm_cc.verts.new((lw_end_x, lw_end_y, 6.0))
    c4 = bm_cc.verts.new((rw_end_x, rw_end_y, 6.0))
    bm_cc.faces.new([c1, c2, c3, c4])
    bm_cc.to_mesh(c_ceil_mesh)
    bm_cc.free()
    cor_ceil_obj = bpy.data.objects.new("ATR_CorridorCeiling", c_ceil_mesh)
    cor_ceil_obj.data.materials.append(mat_plaster)
    link_corridor(cor_ceil_obj)

    # Linear ceiling cove light strip
    mid_cor_x = c_start_x + (c_len / 2.0) * c_cos
    mid_cor_y = c_start_y + (c_len / 2.0) * c_sin
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(mid_cor_x, mid_cor_y, 5.9))
    cove_cor = bpy.context.active_object
    cove_cor.scale = (0.25, c_len - 1.0, 0.05)
    cove_cor.rotation_euler = (0, 0, cor_heading - math.pi/2.0)
    cove_cor.name = "ATR_CorridorCoveLight"
    cove_cor.data.materials.append(mat_cove)
    link_corridor(cove_cor)

    # ==========================================
    # 6. LIGHTING (NATURAL DIFFUSED DAYLIGHT)
    # ==========================================
    # Sunlight streaming down through skylight dome
    sun_data = bpy.data.lights.new(name="Sun_Daylight", type='SUN')
    sun_data.energy = 4.5
    sun_data.color = (1.0, 0.99, 0.97)
    sun_data.angle = math.radians(4.0)
    sun_obj = bpy.data.objects.new("Sun_Daylight", sun_data)
    sun_obj.location = (2.0, -3.0, 16.0)
    sun_dir = Vector((-0.25, 0.35, -1.0))
    sun_obj.rotation_euler = sun_dir.to_track_quat('-Z', 'Y').to_euler()
    col_render.objects.link(sun_obj)

    # Diffused Skylight Ambient Fill
    sky_light = bpy.data.lights.new(name="Sky_AmbientFill", type='POINT')
    sky_light.energy = 1100.0
    sky_light.color = (0.90, 0.95, 1.0)
    sky_light.shadow_soft_size = 4.5
    sky_obj = bpy.data.objects.new("Sky_AmbientFill", sky_light)
    sky_obj.location = (inst_x, inst_y, 9.8)
    col_render.objects.link(sky_obj)

    # Pedestal & Glass Accent Fill
    glass_accent = bpy.data.lights.new(name="Glass_Accent", type='POINT')
    glass_accent.energy = 280.0
    glass_accent.color = (0.82, 0.92, 1.0)
    glass_accent.shadow_soft_size = 1.8
    glass_accent_obj = bpy.data.objects.new("Glass_Accent", glass_accent)
    glass_accent_obj.location = (inst_x + 0.3, inst_y - 0.3, 2.5)
    col_render.objects.link(glass_accent_obj)

    # Corridor Interior Light
    cor_light = bpy.data.lights.new(name="Corridor_Fill", type='POINT')
    cor_light.energy = 400.0
    cor_light.color = (1.0, 0.97, 0.94)
    cor_light.shadow_soft_size = 2.0
    cor_obj = bpy.data.objects.new("Corridor_Fill", cor_light)
    cor_obj.location = (mid_cor_x, mid_cor_y, 3.8)
    col_render.objects.link(cor_obj)

    # Corridor Left Window Daylight
    cor_sun = bpy.data.lights.new(name="Corridor_WindowDaylight", type='POINT')
    cor_sun.energy = 350.0
    cor_sun.color = (0.92, 0.96, 1.0)
    cor_sun.shadow_soft_size = 2.5
    cor_sun_obj = bpy.data.objects.new("Corridor_WindowDaylight", cor_sun)
    cor_sun_obj.location = (mid_cor_x + 3.0 * p_cos, mid_cor_y + 3.0 * p_sin, 3.5)
    col_render.objects.link(cor_sun_obj)

    # ==========================================
    # 7. CAMERA GUIDE RIGS
    # ==========================================
    cameras = {}
    cam_specs = [
        {
            # K01: Establishing Shot - Wide view from entrance threshold
            # Captures floor, pedestal, 3 staggered panels, left negative space, and circular skylight
            'name': 'K01_Establish',
            'pos': Vector((0.0, -10.2, 1.9)),
            'target': Vector((1.0, 0.2, 2.9)),
            'lens': 22.0
        },
        {
            # K02: Forward Dolly - Closer approach along central axis
            # Shows pedestal plinth, halo ring, stepped panel depths, and upper dome
            'name': 'K02_Approach',
            'pos': Vector((0.4, -6.6, 1.75)),
            'target': Vector((1.3, 0.0, 1.6)),
            'lens': 28.0
        },
        {
            # K03: Installation Focus - 3/4 hero view of the 3 glass monoliths
            # Clear layer separation, mounting shoes, frosted glass bevels, and halo glow
            'name': 'K03_Focus',
            'pos': Vector((5.2, -4.0, 1.6)),
            'target': Vector((1.3, 0.0, 1.4)),
            'lens': 30.0
        },
        {
            # K04: Transition Alignment - Threshold facing northeast gallery corridor
            # Curved corridor perspective, arched portal, and linear ceiling cove light
            'name': 'K04_Corridor',
            'pos': Vector((5.2, 4.6, 1.9)),
            'target': Vector((end_x, end_y, 2.4)),
            'lens': 28.0
        },
        {
            # Top-Down Layout - Plan view of circular atrium, entrance, pedestal, colonnade, corridor
            'name': 'TopDown_View',
            'pos': Vector((0.0, 0.0, 28.0)),
            'target': Vector((0.0, 0.0, 0.0)),
            'ortho': True,
            'ortho_scale': 30.0
        }
    ]

    for cs in cam_specs:
        cdata = bpy.data.cameras.new(cs['name'])
        if cs.get('ortho'):
            cdata.type = 'ORTHO'
            cdata.ortho_scale = cs['ortho_scale']
        else:
            cdata.type = 'PERSP'
            cdata.lens = cs['lens']
        cdata.clip_start = 0.1
        cdata.clip_end = 120.0

        cobj = bpy.data.objects.new(cs['name'], cdata)
        cobj.location = cs['pos']
        d = cs['target'] - cs['pos']
        cobj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
        col_cameras.objects.link(cobj)
        cameras[cs['name']] = cobj

    roof_objects = [ceil_lower, cove_ring, ceil_upper, sky_ring, inner_ring, sky_glass, cor_ceil_obj, cove_cor] + mullions
    return exportable, cameras, roof_objects

def render_and_export():
    exportable, cameras, roof_objects = build_scene()

    # 1. Save Native .blend file
    blend_path = os.path.join(OUT_DIR, "entrance-atrium.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    print("SAVED .BLEND:", blend_path)

    # 2. Export Validated .glb asset
    glb_path = os.path.join(OUT_DIR, "entrance-atrium.glb")
    bpy.ops.object.select_all(action='DESELECT')
    for o in exportable:
        o.select_set(True)

    bpy.ops.export_scene.gltf(
        filepath=glb_path,
        export_format='GLB',
        use_selection=True,
        export_apply=True,
        export_materials='EXPORT',
        export_cameras=False,
        export_lights=False
    )
    glb_size = os.path.getsize(glb_path)
    print(f"EXPORTED GLB: {glb_path} ({glb_size:,} bytes)")

    # 3. Render 5 Proof Images (1920x1080)
    scene = bpy.context.scene
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'

    render_tasks = [
        ('K01_Establish', 'camera-K01.png'),
        ('K02_Approach', 'camera-K02.png'),
        ('K03_Focus', 'camera-K03.png'),
        ('K04_Corridor', 'camera-K04.png')
    ]

    for cname, fname in render_tasks:
        scene.camera = cameras[cname]
        out_file = os.path.join(OUT_DIR, fname)
        scene.render.filepath = out_file
        bpy.ops.render.render(write_still=True)
        print(f"RENDERED: {fname}")
        shutil.copyfile(out_file, os.path.join(ARTIFACT_DIR, fname))

    # Top-Down view: temporarily hide roof elements so floor layout is visible
    for r in roof_objects:
        r.hide_render = True

    scene.camera = cameras['TopDown_View']
    top_file = os.path.join(OUT_DIR, 'top-down-layout.png')
    scene.render.filepath = top_file
    bpy.ops.render.render(write_still=True)
    print("RENDERED: top-down-layout.png")
    shutil.copyfile(top_file, os.path.join(ARTIFACT_DIR, 'top-down-layout.png'))

    for r in roof_objects:
        r.hide_render = False

    print("=== ALL MILESTONE 01A DELIVERABLES GENERATED SUCCESSFULLY ===")

if __name__ == "__main__":
    render_and_export()
