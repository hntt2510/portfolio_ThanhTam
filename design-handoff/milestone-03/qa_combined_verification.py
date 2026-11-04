import bpy
import bmesh
import math
import os
import json
from mathutils import Vector, Matrix
from mathutils.bvhtree import BVHTree

def run_qa():
    print("======================================================================")
    print("MILESTONE 03A: COMBINED GEOMETRY, SEAM & TRAJECTORY QA SCRIPT")
    print("======================================================================")

    out_renders_dir = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\renders"
    os.makedirs(out_renders_dir, exist_ok=True)
    
    # 1. Clean slate
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.name = "Scene_Combined_QA"
    
    # Render settings
    scene.render.engine = 'BLENDER_EEVEE_NEXT' if hasattr(bpy.types, 'RenderEngine') and 'BLENDER_EEVEE_NEXT' in [e.identifier for e in bpy.types.RenderSettings.bl_rna.properties['engine'].enum_items] else 'BLENDER_EEVEE'
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.display_settings.display_device = 'sRGB'
    scene.view_settings.view_transform = 'AgX' if 'AgX' in [v.identifier for v in scene.view_settings.bl_rna.properties['view_transform'].enum_items] else 'Filmic'
    scene.view_settings.look = 'Medium High Contrast'
    scene.view_settings.exposure = 0.20

    # World Daylight
    world = bpy.data.worlds.new("QA_Combined_World")
    scene.world = world
    world.use_nodes = True
    nw = world.node_tree.nodes
    nw.clear()
    n_bg = nw.new(type='ShaderNodeBackground')
    n_bg.inputs['Color'].default_value = (0.92, 0.96, 1.0, 1.0)
    n_bg.inputs['Strength'].default_value = 1.6
    n_out = nw.new(type='ShaderNodeOutputWorld')
    world.node_tree.links.new(n_bg.outputs['Background'], n_out.inputs['Surface'])

    # Sunlight
    sun_data = bpy.data.lights.new(name="QA_SunLight", type='SUN')
    sun_data.color = (1.0, 0.98, 0.95)
    sun_data.energy = 3.6
    sun_obj = bpy.data.objects.new("QA_SunLight", sun_data)
    sun_obj.rotation_euler = (math.radians(48.0), math.radians(24.0), math.radians(125.0))
    scene.collection.objects.link(sun_obj)

    # 2. Import Scene 02 GLB
    p_sc02 = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-02\profile-gallery.glb"
    p_sc03 = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\expertise-in-motion.glb"
    
    col_sc02 = bpy.data.collections.new("Scene02_ProfileGallery")
    col_sc03 = bpy.data.collections.new("Scene03_ExpertiseInMotion")
    scene.collection.children.link(col_sc02)
    scene.collection.children.link(col_sc03)

    # Import Scene 02
    bpy.ops.import_scene.gltf(filepath=p_sc02)
    sc02_objs = [obj for obj in scene.objects if obj.name != "QA_SunLight"]
    for obj in sc02_objs:
        if obj.name in scene.collection.objects:
            scene.collection.objects.unlink(obj)
        col_sc02.objects.link(obj)

    # Import Scene 03
    bpy.ops.import_scene.gltf(filepath=p_sc03)
    sc03_objs = [obj for obj in scene.objects if obj not in sc02_objs and obj.name != "QA_SunLight"]
    for obj in sc03_objs:
        if obj.name in scene.collection.objects:
            scene.collection.objects.unlink(obj)
        col_sc03.objects.link(obj)

    print(f"Imported Scene 02 objects: {len(sc02_objs)}")
    print(f"Imported Scene 03 objects: {len(sc03_objs)}")

    # 3. Precise Triangulation and Mesh Statistics
    mesh_stats = []
    total_sc03_verts = 0
    total_sc03_polys = 0
    total_sc03_tris = 0
    
    for obj in sc03_objs:
        if obj.type == 'MESH':
            bm = bmesh.new()
            bm.from_mesh(obj.data)
            n_verts = len(bm.verts)
            n_polys = len(bm.faces)
            bmesh.ops.triangulate(bm, faces=bm.faces[:])
            n_tris = len(bm.faces)
            bm.free()
            
            total_sc03_verts += n_verts
            total_sc03_polys += n_polys
            total_sc03_tris += n_tris
            
            mats = [slot.material.name if slot.material else "None" for slot in obj.material_slots]
            mesh_stats.append({
                "name": obj.name,
                "vertices": n_verts,
                "polygons": n_polys,
                "triangles": n_tris,
                "materials": mats
            })

    print(f"Scene 03 Total Meshes: {len(mesh_stats)}")
    print(f"Scene 03 Total Vertices: {total_sc03_verts}")
    print(f"Scene 03 Total Polygons: {total_sc03_polys}")
    print(f"Scene 03 Exact Triangulated Count: {total_sc03_tris}")

    # 4. Physical Seam Analysis at Junction (43.24, 19.98, 0.0)
    arch_wall = bpy.data.objects.get("PRG_Portal_ArchedWall")
    vest_floor_02 = bpy.data.objects.get("PRG_Vestibule_Floor")
    vest_wall_02 = bpy.data.objects.get("PRG_Vestibule_BackdropWall")
    alcove_bench_02 = bpy.data.objects.get("PRG_Portal_AlcoveBench")
    
    vest_collar_03 = bpy.data.objects.get("EXPM_Portal_EntryVestibule")
    floor_03 = bpy.data.objects.get("EXPM_Floor_Travertine")
    walls_03 = bpy.data.objects.get("EXPM_Walls_Sawtooth")

    seam_data = {}
    
    # Compute floor continuity
    # Scene 02 floor travertine elevation at seam
    sc02_fl_bbox = [vest_floor_02.matrix_world @ Vector(b) for b in vest_floor_02.bound_box]
    sc03_fl_bbox = [floor_03.matrix_world @ Vector(b) for b in floor_03.bound_box]
    fl02_z_max = max(v.z for v in sc02_fl_bbox)
    fl03_z_max = max(v.z for v in sc03_fl_bbox)
    fl_diff = abs(fl02_z_max - fl03_z_max)

    seam_data["floor_02_z"] = fl02_z_max
    seam_data["floor_03_z"] = fl03_z_max
    seam_data["floor_elevation_diff_m"] = fl_diff
    seam_data["floor_continuity_status"] = "PASSED (< 0.01m)" if fl_diff < 0.01 else "FAILED"

    # Analyze overlap between Scene 02 arch wall and Scene 03 entrance vestibule collar
    arch_bbox = [arch_wall.matrix_world @ Vector(b) for b in arch_wall.bound_box]
    collar_bbox = [vest_collar_03.matrix_world @ Vector(b) for b in vest_collar_03.bound_box]

    seam_data["scene02_arch_bounds"] = {
        "x": [min(v.x for v in arch_bbox), max(v.x for v in arch_bbox)],
        "y": [min(v.y for v in arch_bbox), max(v.y for v in arch_bbox)],
        "z": [min(v.z for v in arch_bbox), max(v.z for v in arch_bbox)]
    }
    seam_data["scene03_collar_bounds"] = {
        "x": [min(v.x for v in collar_bbox), max(v.x for v in collar_bbox)],
        "y": [min(v.y for v in collar_bbox), max(v.y for v in collar_bbox)],
        "z": [min(v.z for v in collar_bbox), max(v.z for v in collar_bbox)]
    }

    # Physical overlap volume check
    x_overlap = max(0.0, min(max(v.x for v in arch_bbox), max(v.x for v in collar_bbox)) - max(min(v.x for v in arch_bbox), min(v.x for v in collar_bbox)))
    y_overlap = max(0.0, min(max(v.y for v in arch_bbox), max(v.y for v in collar_bbox)) - max(min(v.y for v in arch_bbox), min(v.y for v in collar_bbox)))
    z_overlap = max(0.0, min(max(v.z for v in arch_bbox), max(v.z for v in collar_bbox)) - max(min(v.z for v in arch_bbox), min(v.z for v in collar_bbox)))

    seam_data["overlap_dimensions"] = {"x": x_overlap, "y": y_overlap, "z": z_overlap}
    seam_data["seam_overlap_status"] = "WATERTIGHT_OVERLAP" if (x_overlap > 0.1 and y_overlap > 0.1 and z_overlap > 3.0) else "POTENTIAL_GAP"

    # Crucial finding: PRG_Vestibule_BackdropWall check
    if vest_wall_02:
        bw_bbox = [vest_wall_02.matrix_world @ Vector(b) for b in vest_wall_02.bound_box]
        seam_data["vestibule_backdrop_wall"] = {
            "name": vest_wall_02.name,
            "location": [vest_wall_02.location.x, vest_wall_02.location.y, vest_wall_02.location.z],
            "x_span": [min(v.x for v in bw_bbox), max(v.x for v in bw_bbox)],
            "y_span": [min(v.y for v in bw_bbox), max(v.y for v in bw_bbox)],
            "z_span": [min(v.z for v in bw_bbox), max(v.z for v in bw_bbox)],
            "action_required": "MUST_BE_CULLED_AT_RUNTIME_WHEN_SCENE03_LOADED (Blocks K09-K10 corridor)"
        }

    # 5. Build BVH Tree and Sample Trajectory K08 -> K12 (100 intermediate samples)
    # Define Waypoints in Blender coordinates
    waypoints = [
        Vector((36.53, 21.62, 1.80)),  # K08
        Vector((44.50, 19.40, 1.85)),  # K09
        Vector((49.50, 14.20, 3.20)),  # K10
        Vector((56.80, 11.20, 1.85)),  # K11
        Vector((63.20, 8.20, 4.05))    # K12
    ]
    targets = [
        Vector((43.24, 19.98, 2.20)),  # K08 target
        Vector((55.80, 14.10, 3.80)),  # K09 target
        Vector((57.80, 10.30, 0.20)),  # K10 target
        Vector((58.50, 4.50, 2.20)),   # K11 target
        Vector((75.00, 2.80, 4.20))    # K12 target
    ]

    def catmull_rom(p0, p1, p2, p3, t):
        t2 = t * t
        t3 = t2 * t
        return 0.5 * (
            (2.0 * p1) +
            (-p0 + p2) * t +
            (2.0 * p0 - 5.0 * p1 + 4.0 * p2 - p3) * t2 +
            (-p0 + 3.0 * p1 - 3.0 * p2 + p3) * t3
        )

    # Generate 100 sample points along the 4 spline segments
    # Segment 0: K08 -> K09 (25 samples)
    # Segment 1: K09 -> K10 (25 samples)
    # Segment 2: K10 -> K11 (25 samples)
    # Segment 3: K11 -> K12 (25 samples)
    spline_samples = []
    
    # Extended points for endpoint tangent continuity
    ext_pts = [waypoints[0] + (waypoints[0] - waypoints[1])] + waypoints + [waypoints[-1] + (waypoints[-1] - waypoints[-2])]
    ext_tgts = [targets[0] + (targets[0] - targets[1])] + targets + [targets[-1] + (targets[-1] - targets[-2])]

    for seg in range(4):
        p0, p1, p2, p3 = ext_pts[seg], ext_pts[seg+1], ext_pts[seg+2], ext_pts[seg+3]
        t0, t1, t2, t3 = ext_tgts[seg], ext_tgts[seg+1], ext_tgts[seg+2], ext_tgts[seg+3]
        for s in range(25):
            u = s / 25.0
            pos = catmull_rom(p0, p1, p2, p3, u)
            tgt = catmull_rom(t0, t1, t2, t3, u)
            spline_samples.append({
                "index": seg * 25 + s,
                "segment": f"K0{seg+8}_to_K0{seg+9}" if seg < 2 else f"K{seg+8}_to_K{seg+9}",
                "u": u,
                "position": [pos.x, pos.y, pos.z],
                "target": [tgt.x, tgt.y, tgt.z]
            })

    # Add the final endpoint K12
    spline_samples.append({
        "index": 100,
        "segment": "K12_endpoint",
        "u": 1.0,
        "position": [waypoints[-1].x, waypoints[-1].y, waypoints[-1].z],
        "target": [targets[-1].x, targets[-1].y, targets[-1].z]
    })

    # We evaluate collision under runtime condition where PRG_Vestibule_BackdropWall is culled
    # Let's temporarily hide vest_wall_02 and alcove_bench_02 to represent the actual integrated world
    if vest_wall_02: vest_wall_02.hide_viewport = True; vest_wall_02.hide_render = True
    if alcove_bench_02: alcove_bench_02.hide_viewport = True; alcove_bench_02.hide_render = True

    # Build BVH tree from all solid mesh geometry in Scene 02 and Scene 03
    combined_bm = bmesh.new()
    for obj in sc02_objs + sc03_objs:
        if obj.type == 'MESH' and obj not in [vest_wall_02, alcove_bench_02]:
            # Apply world matrix to mesh vertices
            bm_temp = bmesh.new()
            bm_temp.from_mesh(obj.data)
            bm_temp.transform(obj.matrix_world)
            # Triangulate
            bmesh.ops.triangulate(bm_temp, faces=bm_temp.faces[:])
            
            # Transfer to combined_bm
            for v in bm_temp.verts:
                combined_bm.verts.new(v.co)
            combined_bm.verts.ensure_lookup_table()
            offset = len(combined_bm.verts) - len(bm_temp.verts)
            for f in bm_temp.faces:
                f_verts = [combined_bm.verts[offset + v.index] for v in f.verts]
                try:
                    combined_bm.faces.new(f_verts)
                except ValueError:
                    pass
            bm_temp.free()

    combined_bm.faces.ensure_lookup_table()
    bvh = BVHTree.FromBMesh(combined_bm)
    print(f"BVH Tree successfully constructed with {len(combined_bm.faces)} polygons.")

    clearance_results = []
    min_dist_overall = float('inf')
    min_sample_point = None

    for smp in spline_samples:
        pos = Vector(smp["position"])
        loc, normal, face_idx, dist = bvh.find_nearest(pos)
        if dist is not None:
            if dist < min_dist_overall:
                min_dist_overall = dist
                min_sample_point = smp
            clearance_results.append({
                "sample_idx": smp["index"],
                "segment": smp["segment"],
                "position": [round(pos.x, 3), round(pos.y, 3), round(pos.z, 3)],
                "nearest_mesh_pt": [round(loc.x, 3), round(loc.y, 3), round(loc.z, 3)],
                "clearance_m": round(dist, 3),
                "status": "CLEAR" if dist >= 0.50 else ("WARNING" if dist >= 0.25 else "COLLISION")
            })

    combined_bm.free()

    print(f"--- TRAJECTORY CLEARANCE RESULTS ---")
    print(f"Total Trajectory Samples Checked: {len(clearance_results)}")
    print(f"Minimum Clearance Distance Across Entire Path: {min_dist_overall:.3f} m")
    print(f"Occurs at sample {min_sample_point['index']} ({min_sample_point['segment']}) at position {min_sample_point['position']}")
    if min_dist_overall >= 0.50:
        print("Trajectory Clearance Status: FULL PASS (Safe comfort buffer >= 0.50m maintained everywhere)")
    else:
        print("Trajectory Clearance Status: WARNING / COLLISION DETECTED")

    # 6. Render High-Resolution Proof Images
    # Camera helper
    def render_shot(name, loc, tgt, fov_deg=48.0, res_x=1920, res_y=1080):
        cam_data = bpy.data.cameras.new(name)
        cam_data.angle = math.radians(fov_deg)
        cam_obj = bpy.data.objects.new(name, cam_data)
        cam_obj.location = loc
        dx = tgt[0] - loc[0]
        dy = tgt[1] - loc[1]
        dz = tgt[2] - loc[2]
        dist_xy = math.sqrt(dx*dx + dy*dy)
        yaw = math.atan2(dy, dx) - math.pi / 2.0
        pitch = math.atan2(dz, dist_xy)
        cam_obj.rotation_euler = (math.pi / 2.0 - pitch, 0.0, yaw)
        scene.collection.objects.link(cam_obj)
        scene.camera = cam_obj
        scene.render.resolution_x = res_x
        scene.render.resolution_y = res_y
        
        filepath = os.path.join(out_renders_dir, f"{name}.png")
        scene.render.filepath = filepath
        bpy.ops.render.render(write_still=True)
        print(f"Rendered: {filepath}")
        return filepath

    # Shot A: K08 Seam View (Combined Scene 02 + Scene 03 through archway)
    render_shot("combined-scene02-scene03-k08", 
                loc=(36.53, 21.62, 1.80), 
                tgt=(43.24, 19.98, 2.20), 
                fov_deg=48.0)

    # Shot B: K08 Mobile View
    render_shot("combined-scene02-scene03-k08-mobile", 
                loc=(36.53, 21.62, 1.88), 
                tgt=(43.24, 19.98, 2.20), 
                fov_deg=50.0, 
                res_x=1080, res_y=1920)

    # Shot C: High-angle exterior isometric showing physical junction of arch and collar
    render_shot("seam-joint-exterior", 
                loc=(48.0, 28.0, 12.0), 
                tgt=(43.24, 19.98, 2.0), 
                fov_deg=42.0)

    # Shot D: Interior detail looking right at the arch threshold
    render_shot("seam-joint-detail-interior", 
                loc=(41.0, 20.8, 1.6), 
                tgt=(44.5, 19.4, 1.8), 
                fov_deg=55.0)

    # 7. Write Structured JSON Report
    qa_report = {
        "milestone": "03A_FINAL_QA",
        "timestamp": "2026-11-04",
        "mesh_statistics": {
            "scene03_total_meshes": len(mesh_stats),
            "scene03_total_vertices": total_sc03_verts,
            "scene03_total_polygons": total_sc03_polys,
            "scene03_exact_triangles": total_sc03_tris,
            "triangle_budget_ceiling": 6800,
            "triangle_budget_percentage": round((total_sc03_tris / 6800.0) * 100.0, 2),
            "meshes": mesh_stats
        },
        "seam_verification": seam_data,
        "trajectory_clearance": {
            "total_samples": len(clearance_results),
            "minimum_clearance_distance_m": round(min_dist_overall, 3),
            "minimum_clearance_sample": min_sample_point,
            "comfort_threshold_m": 0.50,
            "status": "PASS" if min_dist_overall >= 0.50 else "WARN",
            "samples": clearance_results
        }
    }

    json_path = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\qa_combined_results.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(qa_report, f, indent=2)
    print(f"Saved QA report JSON: {json_path}")
    print("======================================================================")
    print("QA COMBINED VERIFICATION COMPLETED SUCCESSFULLY.")
    print("======================================================================")

if __name__ == "__main__":
    run_qa()
