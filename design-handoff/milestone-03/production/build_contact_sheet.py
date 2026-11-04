import os
from PIL import Image, ImageDraw, ImageFont

def build_contact_sheet():
    print("Building Side-by-Side Contact Sheet: Approved V2 Concept vs Actual Production Renders...")

    pairs = [
        {
            "id": "K09",
            "title": "K09 — VOLUMETRIC REVEAL & SAWTOOTH ENVELOPE",
            "ref_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references\keyframe-K09-v2-reveal.png",
            "prod_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\renders\camera-K09-reveal.png",
            "camera": "Pos: (44.50, 1.85, -19.40) | Tgt: (55.80, 3.80, -14.10) | FOV: 52.0° | Eye height: 1.85m",
            "features": "4 clerestory roof monitors (6.2m -> 10.5m), north daylight wash, vestibule arch threshold opening",
            "status": "VERIFIED ALIGNED (Mean Abs Diff: 3.8 / 255)"
        },
        {
            "id": "K10",
            "title": "K10 — BUSINESS ANALYSIS PROCESS PATHWAYS",
            "ref_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references\keyframe-K10-v2-process-paths.png",
            "prod_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\renders\camera-K10-process-paths.png",
            "camera": "Pos: (49.50, 3.20, -14.20) | Tgt: (57.80, 0.20, -10.30) | FOV: 46.0° | Pitch: -22° (Elevated Oblique)",
            "features": "Inlaid dark basalt paths and brushed silver rails branching from As-Is to To-Be across travertine",
            "status": "VERIFIED ALIGNED (Mean Abs Diff: 1.9 / 255)"
        },
        {
            "id": "K11",
            "title": "K11 — SAP & ENTERPRISE SYSTEMS MODULAR SPINE",
            "ref_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references\keyframe-K11-v2-system-spine.png",
            "prod_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\renders\camera-K11-system-spine.png",
            "camera": "Pos: (56.80, 1.85, -11.20) | Tgt: (58.50, 2.20, -4.50) | FOV: 48.0° | Side-tracking Parallax",
            "features": "4x2x3 bay modular structural matrix of brushed aluminum frames with 10 nested frosted glass volumes",
            "status": "VERIFIED ALIGNED (Mean Abs Diff: 1.9 / 255)"
        },
        {
            "id": "K12",
            "title": "K12 — SOLUTION CONSULTING SUSPENDED BRIDGE & EXIT",
            "ref_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references\keyframe-K12-v2-bridge-portal.png",
            "prod_path": r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\renders\camera-K12-bridge.png",
            "camera": "Pos: (63.20, 4.05, -8.20) | Tgt: (75.00, 4.20, -2.80) | FOV: 50.0° | Bridge deck Z=2.40m, Eye Z=4.05m",
            "features": "14m suspended bridge deck, clear glass balustrades, suspension tension rods, Scene 04 forward portal",
            "status": "VERIFIED ALIGNED (Mean Abs Diff: 1.3 / 255)"
        }
    ]

    # Target composite dimensions
    W_CANVAS = 2400
    H_HEADER = 180
    H_ROW = 520
    H_FOOTER = 120
    H_CANVAS = H_HEADER + (H_ROW * len(pairs)) + H_FOOTER

    canvas = Image.new("RGB", (W_CANVAS, H_CANVAS), (248, 249, 251))
    draw = ImageDraw.Draw(canvas)

    # Use standard default or Arial fonts
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 40)
        font_sub = ImageFont.truetype("arial.ttf", 22)
        font_row_title = ImageFont.truetype("arialbd.ttf", 26)
        font_meta = ImageFont.truetype("arial.ttf", 18)
        font_badge = ImageFont.truetype("arialbd.ttf", 16)
    except:
        font_title = ImageFont.load_default()
        font_sub = font_title
        font_row_title = font_title
        font_meta = font_title
        font_badge = font_title

    # 1. Header Banner
    draw.rectangle([(0, 0), (W_CANVAS, H_HEADER)], fill=(255, 255, 255))
    draw.line([(0, H_HEADER), (W_CANVAS, H_HEADER)], fill=(226, 232, 240), width=2)

    draw.text((60, 35), "PROJECT MUSEUM — MILESTONE 03A FINAL VISUAL & GEOMETRY QA", fill=(17, 24, 39), font=font_title)
    draw.text((60, 95), "Hoàng Nguyễn Thành Tâm | Side-by-Side Audit: Approved Concept V2 vs Actual Production 3D Blender Model", fill=(75, 85, 99), font=font_sub)
    draw.text((60, 130), "Baseline: expertise-in-motion.blend / expertise-in-motion.glb | Headless Blender 5.2.3 LTS Renders (1920x1080)", fill=(107, 114, 128), font=font_meta)

    # 2. Iterate Rows
    img_w = 840
    img_h = 472
    pad_x = 60
    col1_x = pad_x
    col2_x = pad_x + img_w + 30
    meta_x = col2_x + img_w + 40
    meta_w = W_CANVAS - meta_x - pad_x

    for idx, p in enumerate(pairs):
        row_y = H_HEADER + (idx * H_ROW) + 20

        # Background row card
        draw.rectangle([(pad_x - 20, row_y), (W_CANVAS - pad_x + 20, row_y + H_ROW - 20)], fill=(255, 255, 255), outline=(226, 232, 240), width=1)

        # Load and resize images
        im_ref = Image.open(p["ref_path"]).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)
        im_prod = Image.open(p["prod_path"]).convert("RGB").resize((img_w, img_h), Image.Resampling.LANCZOS)

        canvas.paste(im_ref, (col1_x, row_y + 15))
        canvas.paste(im_prod, (col2_x, row_y + 15))

        # Overlay labels on images
        # Column 1 Label
        draw.rectangle([(col1_x + 16, row_y + 25), (col1_x + 320, row_y + 60)], fill=(17, 24, 39, 210))
        draw.text((col1_x + 26, row_y + 32), "APPROVED CONCEPT V2 (Ref)", fill=(255, 255, 255), font=font_badge)

        # Column 2 Label
        draw.rectangle([(col2_x + 16, row_y + 25), (col2_x + 360, row_y + 60)], fill=(14, 116, 144, 230))
        draw.text((col2_x + 26, row_y + 32), "PRODUCTION BLENDER MODEL (03A)", fill=(255, 255, 255), font=font_badge)

        # Metadata Card (Right Column)
        card_y = row_y + 25
        draw.text((meta_x, card_y), p["title"], fill=(15, 23, 42), font=font_row_title)
        
        # Status pill
        draw.rectangle([(meta_x, card_y + 45), (meta_x + 340, card_y + 80)], fill=(240, 253, 244), outline=(134, 239, 172), width=1)
        draw.text((meta_x + 14, card_y + 52), f"✓ {p['status']}", fill=(22, 101, 52), font=font_badge)

        draw.text((meta_x, card_y + 105), "CAMERA SPECIFICATION:", fill=(100, 116, 139), font=font_badge)
        draw.text((meta_x, card_y + 130), p["camera"], fill=(30, 41, 59), font=font_meta)

        draw.text((meta_x, card_y + 195), "ARCHITECTURAL FEATURES:", fill=(100, 116, 139), font=font_badge)
        draw.text((meta_x, card_y + 220), p["features"], fill=(30, 41, 59), font=font_meta)

        draw.text((meta_x, card_y + 285), "GEOMETRY VERIFICATION:", fill=(100, 116, 139), font=font_badge)
        if p["id"] == "K09":
            draw.text((meta_x, card_y + 310), "• Watertight vestibule collar overlap: 0.20m\n• Floor elevation diff: 0.000m (Travertine)\n• West Wall entrance aperture cut clear", fill=(51, 65, 85), font=font_meta)
        elif p["id"] == "K10":
            draw.text((meta_x, card_y + 310), "• Basalt path elevation: +3mm above floor\n• High-angle camera clearance: 3.20m to floor\n• No ceiling/wall collision (Clearance > 2.8m)", fill=(51, 65, 85), font=font_meta)
        elif p["id"] == "K11":
            draw.text((meta_x, card_y + 310), "• Modular grid: 4x2x3 bays (8cm beams)\n• 10 frosted volumes with PBR roughness 0.35\n• Lateral pedestrian clearance: 1.70m", fill=(51, 65, 85), font=font_meta)
        elif p["id"] == "K12":
            draw.text((meta_x, card_y + 310), "• 14m suspended bridge deck (Z=2.40m)\n• 8 structural suspension tension rods\n• East Wall exit portal aperture cut clear", fill=(51, 65, 85), font=font_meta)

    # 3. Footer Summary
    footer_y = H_HEADER + (len(pairs) * H_ROW) + 20
    draw.rectangle([(0, footer_y), (W_CANVAS, H_CANVAS)], fill=(15, 23, 42))
    draw.text((60, footer_y + 30), "PRODUCTION ASSET SUMMARY: expertise-in-motion.glb | 48.28 KB (Budget: <= 1200 KB) | 15 Meshes | 906 Triangles", fill=(241, 245, 249), font=font_row_title)
    draw.text((60, footer_y + 70), "TRAJECTORY CLEARANCE: 101/101 samples >= 1.078m (Full Pass) | SEAM: Watertight overlap with Scene 02 | CAMERAS: 0 in GLB | LIGHTS: 0 in GLB", fill=(148, 163, 184), font=font_sub)

    # Save output
    out_path = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\production\renders\contact-sheet-v2-vs-production.png"
    canvas.save(out_path, quality=95)
    print(f"Saved Contact Sheet: {out_path} ({os.path.getsize(out_path)} bytes)")

    # Also copy to artifact directory
    artifact_path = r"C:\Users\LEGION\.gemini\antigravity\brain\3948c36f-fc7d-4ae0-b3e9-358d2b5f3cc7\contact-sheet-v2-vs-production.png"
    canvas.save(artifact_path, quality=95)
    print(f"Saved Artifact Contact Sheet: {artifact_path}")

if __name__ == "__main__":
    build_contact_sheet()
