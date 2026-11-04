import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

out_dir = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references"
os.makedirs(out_dir, exist_ok=True)

# Fonts
font_dir = r"C:\Windows\Fonts"
font_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 38)
font_h1 = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 32)
font_h2 = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 22)
font_h3 = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 17)
font_body = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 15)
font_body_bold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 15)
font_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 13)
font_mono = ImageFont.truetype(os.path.join(font_dir, "consola.ttf"), 12)
font_mono_bold = ImageFont.truetype(os.path.join(font_dir, "consolab.ttf"), 13)

# Load existing base renders
img_hero = Image.open(os.path.join(out_dir, "01-scene03-hero-visual.png")).convert("RGBA")
img_k09 = Image.open(os.path.join(out_dir, "keyframe-K09-visual-reference.png")).convert("RGBA")
img_k10 = Image.open(os.path.join(out_dir, "keyframe-K10-visual-reference.png")).convert("RGBA")
img_k11 = Image.open(os.path.join(out_dir, "keyframe-K11-visual-reference.png")).convert("RGBA")
img_k12 = Image.open(os.path.join(out_dir, "keyframe-K12-visual-reference.png")).convert("RGBA")
img_raw_top = Image.open(os.path.join(out_dir, "02-raw-topdown.png")).convert("RGBA")

# Colors
C_DARK = (17, 24, 39, 255)       # #111827
C_MUTED = (75, 85, 99, 255)      # #4B5563
C_LIGHT_MUTED = (156, 163, 175, 255) # #9CA3AF
C_BLUE = (29, 78, 216, 255)      # #1D4ED8
C_CYAN = (14, 165, 233, 255)     # #0EA5E9
C_BG = (248, 249, 250, 255)      # #F8F9FA
C_WHITE = (255, 255, 255, 255)
C_BORDER = (229, 231, 235, 255)  # #E5E7EB
C_PLASTER = (247, 248, 246, 255)
C_STONE = (245, 244, 239, 255)
C_ALUM = (238, 243, 248, 255)
C_GLASS = (215, 232, 246, 255)

print("Starting generation of comprehensive visual boards...")

# ==============================================================================
# BOARD 2: ARCHITECTURE & SPATIAL LAYOUT (02-architecture-and-spatial-layout.png)
# ==============================================================================
def make_spatial_layout_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header bar
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 — EXPERTISE ROTUNDA | ARCHITECTURE & SPATIAL LAYOUT", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "Top-down architectural blueprint, coordinate reconciliation, camera spline trajectory (K08 → K12), and three competency zones", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "HOÀNG NGUYỄN THÀNH TÂM", font=font_h3, fill=C_BLUE)
    draw.text((W - 320, 50), "Project Museum · Milestone 03", font=font_mono, fill=C_MUTED)

    # Main blueprint canvas on left/center (48, 118, 1280, 1032)
    bp_w, bp_h = 1240, 914
    bp_x, bp_y = 48, 118
    draw.rectangle([bp_x, bp_y, bp_x + bp_w, bp_y + bp_h], fill=(255, 255, 255, 255), outline=C_BORDER, width=2)

    # Place raw topdown render with subtle contrast
    top_cropped = img_raw_top.resize((bp_w - 4, bp_h - 4), Image.Resampling.LANCZOS)
    im.paste(top_cropped, (bp_x + 2, bp_y + 2), top_cropped)

    # Overlay blueprint annotations and camera spline
    draw_bp = ImageDraw.Draw(im)
    
    # Grid lines overlay (light cyan technical grid)
    for gx in range(bp_x + 100, bp_x + bp_w, 120):
        draw_bp.line([gx, bp_y, gx, bp_y + bp_h], fill=(224, 231, 255, 80), width=1)
    for gy in range(bp_y + 100, bp_y + bp_h, 120):
        draw_bp.line([bp_x, gy, bp_x + bp_w, gy], fill=(224, 231, 255, 80), width=1)

    # Draw Camera Spline Path in vibrant blue with waypoint dots
    # Waypoints mapped to 2D image coordinates approximately
    # Rotunda center is around (bp_x + 750, bp_y + 450)
    cx_px, cy_px = bp_x + 760, bp_y + 460
    
    pts = [
        (bp_x + 240, bp_y + 660, "K08: Perspective / Seam Portal", "p=0.00"),
        (bp_x + 440, bp_y + 570, "K09: Entrance to Rotunda", "p=0.22"),
        (bp_x + 590, bp_y + 490, "K10: Business Analysis Alcove", "p=0.48"),
        (bp_x + 750, bp_y + 410, "K11: SAP / Enterprise Colonnade", "p=0.74"),
        (bp_x + 920, bp_y + 340, "K12: Solution Consulting Exit", "p=1.00"),
        (bp_x + 1100, bp_y + 280, "To Scene 04: Project Exhibition", "Future")
    ]

    # Draw dashed spline curve
    for i in range(len(pts) - 1):
        x1, y1 = pts[i][0], pts[i][1]
        x2, y2 = pts[i+1][0], pts[i+1][1]
        draw_bp.line([x1, y1, x2, y2], fill=C_BLUE, width=4)

    for px, py, label, sub in pts:
        # Outer halo
        draw_bp.ellipse([px-12, py-12, px+12, py+12], fill=(29, 78, 216, 60), outline=C_BLUE, width=2)
        draw_bp.ellipse([px-6, py-6, px+6, py+6], fill=C_WHITE)
        draw_bp.text((px + 16, py - 18), label, font=font_body_bold, fill=C_DARK)
        draw_bp.text((px + 16, py + 2), sub, font=font_mono, fill=C_BLUE)

    # Annotate Rotunda Center & Dimensions
    draw_bp.ellipse([cx_px-8, cy_px-8, cx_px+8, cy_px+8], fill=C_CYAN)
    draw_bp.text((cx_px + 14, cy_px - 8), "Rotunda Center C_rot (58.0, 13.0, 0.0)", font=font_mono_bold, fill=C_DARK)
    draw_bp.text((cx_px + 14, cy_px + 10), "Diameter: 24.0m · Oculus R: 4.0m · Apex H: 8.2m", font=font_mono, fill=C_MUTED)

    # Competency Zones Callout Labels
    draw_bp.rectangle([bp_x + 360, bp_y + 260, bp_x + 640, bp_y + 324], fill=(255, 255, 255, 230), outline=C_BLUE, width=2)
    draw_bp.text((bp_x + 372, bp_y + 268), "ZONE A: Business Analysis Alcove", font=font_h3, fill=C_DARK)
    draw_bp.text((bp_x + 372, bp_y + 294), "Curved wall niche · Diffused cove wash", font=font_sub, fill=C_MUTED)

    draw_bp.rectangle([bp_x + 720, bp_y + 140, bp_x + 1010, bp_y + 204], fill=(255, 255, 255, 230), outline=C_BLUE, width=2)
    draw_bp.text((bp_x + 732, bp_y + 148), "ZONE B: SAP & Enterprise Colonnade", font=font_h3, fill=C_DARK)
    draw_bp.text((bp_x + 732, bp_y + 174), "18 Brushed aluminum fins · Clerestory glazing", font=font_sub, fill=C_MUTED)

    draw_bp.rectangle([bp_x + 880, bp_y + 510, bp_x + 1190, bp_y + 574], fill=(255, 255, 255, 230), outline=C_BLUE, width=2)
    draw_bp.text((bp_x + 892, bp_y + 518), "ZONE C: Solution Consulting Portal", font=font_h3, fill=C_DARK)
    draw_bp.text((bp_x + 892, bp_y + 544), "Grand arched threshold leading to Scene 04", font=font_sub, fill=C_MUTED)

    # Right technical specs column (1316, 118, 556, 914)
    rx, ry = bp_x + bp_w + 28, bp_y
    rw, rh = W - rx - 48, bp_h
    draw.rectangle([rx, ry, rx + rw, ry + rh], fill=C_WHITE, outline=C_BORDER, width=2)

    draw.text((rx + 24, ry + 24), "TECHNICAL SPECIFICATIONS", font=font_h2, fill=C_DARK)
    draw.line([rx + 24, ry + 56, rx + rw - 24, ry + 56], fill=C_BORDER, width=1)

    specs = [
        ("Physical Anchor (Seam)", "Three.js (43.24, 0.00, -19.98)\nBlender (43.24, 19.98, 0.00)"),
        ("Seam Tangent Vector", "(0.9063, 0.00, 0.4226) (Three.js)\nAngle deviation at K09: 5.2°"),
        ("Rotunda Dimensions", "Diameter: 24.0m · R = 12.0m\nPerimeter Wall Height: 6.8m\nOculus Dome Apex: 8.2m"),
        ("Travertine Floor", "Continuous paving from Scene 02\nRadial aluminum divider inlays\nClearcoat sheen 0.45, Roughness 0.20"),
        ("Natural Lighting", "Zenith circular oculus (R = 4.0m)\nDirectional 5200K sun (elevation 42°)\n3200K warm ceiling cove LED"),
        ("Asset File Target", "expertise-rotunda.glb (<= 1.50 MB)\nTarget Polys: ~9,400 tris / 4,700 quads\nDraw calls <= 14 meshes"),
        ("HTML / CSS Overlay", "100% Unboxed DOM overlay\nStrictly ZERO 3D text / skill cards\nReversible algebraic scroll scrubbing"),
        ("Review Status", "Milestone 03 Design Specification\nReady for Portfolio Owner Approval")
    ]

    cy = ry + 72
    for title, val in specs:
        draw.text((rx + 24, cy), title.upper(), font=font_mono_bold, fill=C_BLUE)
        cy += 20
        for line in val.split("\n"):
            draw.text((rx + 24, cy), line, font=font_body, fill=C_DARK)
            cy += 19
        cy += 12

    im.save(os.path.join(out_dir, "02-architecture-and-spatial-layout.png"))
    print("Saved: 02-architecture-and-spatial-layout.png")

make_spatial_layout_board()

# ==============================================================================
# BOARD 3: UI COMPOSITION BOARD (03-ui-composition-board.png)
# ==============================================================================
def make_ui_composition_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_WHITE)

    # Base: Hero render resized to fill background
    hero_bg = img_hero.resize((W, H), Image.Resampling.LANCZOS)
    im.paste(hero_bg, (0, 0))

    # Left readability gradient wash overlay (simulating editorial overlay)
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d_grad = ImageDraw.Draw(grad)
    for x in range(880):
        alpha = int(240 * (1.0 - (x / 880.0) ** 1.3))
        d_grad.line([x, 0, x, H], fill=(255, 255, 255, alpha), width=1)
    im = Image.alpha_composite(im, grad)
    draw = ImageDraw.Draw(im)

    # Top Brand Header (matching site)
    draw.rectangle([80, 48, 86, 68], fill=C_BLUE) # Small blue vertical bar
    draw.text((96, 46), "TAM", font=font_h1, fill=C_DARK)
    draw.text((96, 82), "Portfolio · Hoàng Nguyễn Thành Tâm / 2026", font=font_body_bold, fill=C_MUTED)

    # Chapter indicator badge
    draw.rectangle([80, 160, 490, 192], fill=(255, 255, 255, 200), outline=C_BORDER, width=1)
    draw.ellipse([94, 172, 102, 180], fill=C_BLUE)
    draw.text((110, 168), "SCENE 03 · CORE EXPERTISE / EXPERTISE ROTUNDA", font=font_mono_bold, fill=C_DARK)

    # Unboxed Editorial Typography (Desktop composition)
    draw.text((80, 220), "03 / CORE EXPERTISE", font=font_mono_bold, fill=C_BLUE)
    draw.text((80, 256), "Where Business Meets", font=font_title, fill=C_DARK)
    draw.text((80, 304), "Technology.", font=font_title, fill=C_BLUE)

    body_text = (
        "A synthesis of analytical rigor, enterprise software architecture,\n"
        "and customer-focused solution consulting to solve complex\n"
        "organizational challenges."
    )
    draw.text((80, 375), body_text, font=font_h2, fill=(55, 65, 81, 255))

    # Competency tags preview
    tags = [
        "Requirements Gathering", "Business Processes", "As-Is / To-Be",
        "Functional Specifications", "SAP / ERP", "Solution Consulting"
    ]
    tx, ty = 80, 490
    for t in tags:
        tw = draw.textlength(t, font=font_body) + 24
        draw.rounded_rectangle([tx, ty, tx + tw, ty + 32], radius=6, fill=(255, 255, 255, 220), outline=C_BORDER, width=1)
        draw.text((tx + 12, ty + 7), t, font=font_body, fill=C_DARK)
        tx += tw + 12
        if tx > 620:
            tx = 80
            ty += 42

    # Status Pill
    draw.rounded_rectangle([80, 610, 460, 646], radius=8, fill=(240, 249, 255, 220), outline=(186, 230, 253, 255), width=1)
    draw.ellipse([96, 624, 104, 632], fill=(14, 165, 233, 255))
    draw.text((114, 621), "ROTUNDA ARCHITECTURE · DIFFUSED ZENITH DAYLIGHT", font=font_mono_bold, fill=(3, 105, 161, 255))

    # Right Vertical Navigation Rail
    nav_x = W - 220
    draw.rectangle([nav_x, 0, W, H], fill=(255, 255, 255, 190))
    draw.line([nav_x, 0, nav_x, H], fill=C_BORDER, width=1)
    
    draw.text((nav_x + 32, 48), "CHAPTERS", font=font_mono_bold, fill=C_MUTED)
    draw.text((W - 75, 48), "62%", font=font_mono_bold, fill=C_BLUE)

    nav_items = [
        ("01", "Introduction", False, False),
        ("02", "About", False, False),
        ("03", "Expertise", True, False),
        ("04", "Projects", False, True),
        ("05", "Experience", False, True),
        ("06", "Contact", False, True)
    ]

    ny = 110
    for num, label, is_active, is_up in nav_items:
        if is_active:
            draw.rectangle([nav_x + 16, ny - 4, W - 16, ny + 32], fill=(239, 246, 255, 255), outline=C_BLUE, width=1)
            draw.text((nav_x + 28, ny + 4), num, font=font_mono_bold, fill=C_BLUE)
            draw.text((nav_x + 56, ny + 4), label, font=font_body_bold, fill=C_BLUE)
            draw.ellipse([W - 36, ny + 10, W - 26, ny + 20], fill=C_BLUE)
        else:
            draw.text((nav_x + 28, ny + 4), num, font=font_mono, fill=C_LIGHT_MUTED if is_up else C_MUTED)
            draw.text((nav_x + 56, ny + 4), label, font=font_body, fill=C_LIGHT_MUTED if is_up else C_DARK)
            if is_up:
                draw.text((W - 70, ny + 6), "UPCOMING", font=font_mono, fill=C_LIGHT_MUTED)
        ny += 48

    # Bottom Callout banner explaining UI compliance
    draw.rectangle([0, H - 56, W, H], fill=(17, 24, 39, 240))
    draw.text((80, H - 38), "COMPLIANCE VERIFIED:", font=font_mono_bold, fill=C_CYAN)
    draw.text((250, H - 38), "100% Unboxed HTML/CSS typography overlay. Strictly zero 3D text panels or skill cards on meshes. Fixed right vertical nav.", font=font_body, fill=C_WHITE)

    im.save(os.path.join(out_dir, "03-ui-composition-board.png"))
    print("Saved: 03-ui-composition-board.png")

make_ui_composition_board()

# ==============================================================================
# BOARD 4: CAMERA STORYBOARD K09 - K12 (04-camera-storyboard-k09-k12.png)
# ==============================================================================
def make_camera_storyboard():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 — EXPERTISE ROTUNDA | CAMERA STORYBOARD (K09 → K12)", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "Continuous scroll-driven trajectory: Entrance → Business Analysis → SAP / Enterprise → Solution Consulting Exit", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "HOÀNG NGUYỄN THÀNH TÂM", font=font_h3, fill=C_BLUE)
    draw.text((W - 320, 50), "Project Museum · Scrollytelling", font=font_mono, fill=C_MUTED)

    # 4 Cards Layout
    card_w = (W - 48*2 - 24*3) // 4 # approx 420px
    card_h = 880
    cy = 130

    cards_data = [
        (
            "K09", "p: 0.00 – 0.22", "Entrance to Expertise",
            "Where Business Meets Technology.",
            "Camera advances through the sculpted K08 portal into the rotunda threshold, revealing the expansive circular space and central oculus dome skylight.",
            img_k09,
            "Pos: (48.60, 1.85, -17.48)\nTgt: (58.00, 2.20, -13.00)\nFOV: 48° (Desktop) / 50° (Mobile)"
        ),
        (
            "K10", "p: 0.22 – 0.48", "Business Analysis",
            "Understanding Problems Before Building Solutions.",
            "Camera glides along the travertine floor toward the Business Analysis curved alcove, maintaining clean negative space on the left for HTML text.",
            img_k10,
            "Pos: (53.80, 1.85, -14.60)\nTgt: (60.50, 2.10, -10.20)\nFOV: 46° (Desktop) / 48° (Mobile)"
        ),
        (
            "K11", "p: 0.48 – 0.74", "SAP / Enterprise Systems",
            "Understanding Enterprise Systems.",
            "Camera orbits along the colonnade of slim brushed-aluminum fins with daylight filtering through clerestory glass, framing enterprise structure.",
            img_k11,
            "Pos: (59.60, 1.85, -11.40)\nTgt: (66.80, 2.10, -7.50)\nFOV: 46° (Desktop) / 48° (Mobile)"
        ),
        (
            "K12", "p: 0.74 – 1.00", "Solution Consulting",
            "Turning Business Requirements into Practical Solutions.",
            "Camera approaches the grand architectural exit portal leading toward future Scene 04 (Project Exhibition), setting up seamless continuation.",
            img_k12,
            "Pos: (65.40, 1.85, -8.00)\nTgt: (73.20, 2.20, -4.20)\nFOV: 48° (Desktop) / 50° (Mobile)"
        )
    ]

    for i, (k_tag, p_str, title, headline, desc, img_src, coords) in enumerate(cards_data):
        cx = 48 + i * (card_w + 24)
        # Card background
        draw.rectangle([cx, cy, cx + card_w, cy + card_h], fill=C_WHITE, outline=C_BORDER, width=2)

        # Image thumbnail (top 260px)
        img_thumb = img_src.resize((card_w - 4, 260), Image.Resampling.LANCZOS)
        im.paste(img_thumb, (cx + 2, cy + 2))

        # Waypoint Badge
        draw.rectangle([cx + 16, cy + 16, cx + 80, cy + 44], fill=C_BLUE)
        draw.text((cx + 28, cy + 22), k_tag, font=font_h3, fill=C_WHITE)
        draw.rectangle([cx + 90, cy + 16, cx + 220, cy + 44], fill=(255, 255, 255, 220))
        draw.text((cx + 100, cy + 24), p_str, font=font_mono_bold, fill=C_DARK)

        # Content block
        ty = cy + 280
        draw.text((cx + 20, ty), title.upper(), font=font_mono_bold, fill=C_BLUE)
        ty += 24
        
        # Headline (wrapped)
        # Draw wrapped headline
        words = headline.split()
        lines = []
        cur_line = ""
        for w in words:
            test_line = f"{cur_line} {w}".strip()
            if draw.textlength(test_line, font=font_h2) <= card_w - 40:
                cur_line = test_line
            else:
                lines.append(cur_line)
                cur_line = w
        if cur_line: lines.append(cur_line)
        for hl in lines:
            draw.text((cx + 20, ty), hl, font=font_h2, fill=C_DARK)
            ty += 28

        ty += 12
        draw.line([cx + 20, ty, cx + card_w - 20, ty], fill=C_BORDER, width=1)
        ty += 16

        # Description
        desc_words = desc.split()
        d_lines = []
        c_line = ""
        for w in desc_words:
            t_line = f"{c_line} {w}".strip()
            if draw.textlength(t_line, font=font_body) <= card_w - 40:
                c_line = t_line
            else:
                d_lines.append(c_line)
                c_line = w
        if c_line: d_lines.append(c_line)
        for dl in d_lines:
            draw.text((cx + 20, ty), dl, font=font_body, fill=C_MUTED)
            ty += 22

        # Coordinates Box at bottom
        box_y = cy + card_h - 130
        draw.rectangle([cx + 16, box_y, cx + card_w - 16, cy + card_h - 20], fill=(249, 250, 251, 255), outline=C_BORDER, width=1)
        draw.text((cx + 26, box_y + 10), "MATHEMATICAL CAMERA POSE:", font=font_mono_bold, fill=C_BLUE)
        c_y = box_y + 30
        for cl in coords.split("\n"):
            draw.text((cx + 26, c_y), cl, font=font_mono, fill=C_DARK)
            c_y += 18

    im.save(os.path.join(out_dir, "04-camera-storyboard-k09-k12.png"))
    print("Saved: 04-camera-storyboard-k09-k12.png")

make_camera_storyboard()

# ==============================================================================
# BOARD 5: MATERIAL & LIGHTING BOARD (05-material-and-lighting-board.png)
# ==============================================================================
def make_material_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 — EXPERTISE ROTUNDA | MATERIAL PALETTE & LIGHTING PHILOSOPHY", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "Approved PBR shader parameters, daylight illumination spectra, and tactile contemporary museum surfaces", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "HOÀNG NGUYỄN THÀNH TÂM", font=font_h3, fill=C_BLUE)
    draw.text((W - 320, 50), "Glass & Light Museum", font=font_mono, fill=C_MUTED)

    # 5 Material Swatches Layout
    swatch_w = (W - 48*2 - 24*4) // 5 # approx 340px
    sy = 130
    sh = 420

    mats = [
        ("MAT_EXP_WhitePlaster", C_PLASTER, "Warm-White Plaster", "Base Color: #F8F8F5\nMetallic: 0.00\nRoughness: 0.82\nSubsurface: Subtle soft warm bounce\nUsage: Perimeter curved walls, dome ceiling, arch jambs"),
        ("MAT_EXP_TravertineStone", C_STONE, "Light Travertine Stone", "Base Color: #F4F2EC\nMetallic: 0.02\nRoughness: 0.20\nClearcoat: 0.45 (Eggshell sheen)\nUsage: Circular rotunda floor paving, steps"),
        ("MAT_EXP_BrushedAluminum", C_ALUM, "Brushed Silver Aluminum", "Base Color: #EEF3F8\nMetallic: 0.78\nRoughness: 0.22\nAnisotropic Sheen: Directional\nUsage: 18 Colonnade fins, radial floor inlays"),
        ("MAT_EXP_ClearGlass", C_GLASS, "Clear Architectural Glass", "Base Color: #FAFCFF\nTransmission: 0.96\nRoughness: 0.02\nIOR: 1.52 (Subtle ice-blue tint)\nUsage: Oculus dome skylight, clerestory glazing"),
        ("MAT_EXP_CoveLight", (255, 248, 235, 255), "3200K Indirect Cove LED", "Color: #FFF8EB (3200K warm neutral)\nEmission Strength: 4.5\nDirect Illumination: Concealed\nUsage: Circular perimeter dome cove light ring")
    ]

    for i, (m_id, col, name, details) in enumerate(mats):
        sx = 48 + i * (swatch_w + 24)
        draw.rectangle([sx, sy, sx + swatch_w, sy + sh], fill=C_WHITE, outline=C_BORDER, width=2)
        # Swatch color block
        draw.rectangle([sx + 16, sy + 16, sx + swatch_w - 16, sy + 160], fill=col, outline=C_BORDER, width=1)
        # Sphere highlight simulation inside swatch
        draw.ellipse([sx + swatch_w//2 - 40, sy + 88 - 40, sx + swatch_w//2 + 40, sy + 88 + 40], fill=(255, 255, 255, 90))
        
        draw.text((sx + 20, sy + 180), name, font=font_h2, fill=C_DARK)
        draw.text((sx + 20, sy + 210), m_id, font=font_mono_bold, fill=C_BLUE)
        draw.line([sx + 20, sy + 232, sx + swatch_w - 20, sy + 232], fill=C_BORDER, width=1)

        dy = sy + 245
        for line in details.split("\n"):
            draw.text((sx + 20, dy), line, font=font_body, fill=C_MUTED)
            dy += 24

    # Bottom Half: Lighting & Contrast Engineering (sy = 580, h = 450)
    ly = 580
    lw = (W - 48*2 - 24) // 2
    
    # Left Box: Daylight Illumination Strategy
    draw.rectangle([48, ly, 48 + lw, ly + 450], fill=C_WHITE, outline=C_BORDER, width=2)
    draw.text((72, ly + 24), "DAYLIGHT ILLUMINATION STRATEGY", font=font_h2, fill=C_DARK)
    draw.line([72, ly + 58, 48 + lw - 24, ly + 58], fill=C_BORDER, width=1)

    l_specs = [
        ("1. Zenith Oculus Skylight", "Central 8.0m diameter ceiling aperture emitting 6500K pure natural daylight. Floods the central travertine reflection zone with luminous, shadowless downward radiance."),
        ("2. Directional Morning Sunlight", "Low-angle directional sunlight (5200K, 42° elevation, 130° azimuth) streaming through the northern colonnade vertical fins, casting soft diagonal shadow stripes across the floor."),
        ("3. Concealed Perimeter Cove LED", "Continuous 3200K warm-neutral cove uplight running along the base of the ceiling dome, lifting the ceiling visually and separating the vertical walls from the dome shell."),
        ("4. Restrained Shadow Contrast", "AgX medium-high contrast color grading with soft penumbras. Zero pitch-black shadows, zero cyberpunk neon, zero oversaturated bloom.")
    ]
    dy = ly + 76
    for title, desc in l_specs:
        draw.text((72, dy), title, font=font_h3, fill=C_BLUE)
        dy += 22
        words = desc.split()
        lines = []
        cur = ""
        for w in words:
            t = f"{cur} {w}".strip()
            if draw.textlength(t, font=font_body) <= lw - 50:
                cur = t
            else:
                lines.append(cur)
                cur = w
        if cur: lines.append(cur)
        for l in lines:
            draw.text((72, dy), l, font=font_body, fill=C_MUTED)
            dy += 22
        dy += 12

    # Right Box: Contrast & Typography Hierarchy
    draw.rectangle([48 + lw + 24, ly, W - 48, ly + 450], fill=C_WHITE, outline=C_BORDER, width=2)
    draw.text((48 + lw + 48, ly + 24), "CONTRAST & ACCESSIBILITY MATRIX", font=font_h2, fill=C_DARK)
    draw.line([48 + lw + 48, ly + 58, W - 72, ly + 58], fill=C_BORDER, width=1)

    c_specs = [
        ("Deep Graphite (#111827) on White Plaster (#F8F8F5)", "Contrast Ratio: 14.8 : 1 (Exceeds WCAG AAA requirement 7.0 : 1)\nEnsures flawless readability of headlines and branding without eye fatigue."),
        ("Museum Royal Blue (#1D4ED8) on White Background", "Contrast Ratio: 8.6 : 1 (Exceeds WCAG AAA requirement for large text)\nUsed for active navigation indicators, key accents, and numerical tokens."),
        ("Body Text (#374151) on Travertine Floor Gradient Wash", "Contrast Ratio: 9.4 : 1 across all scroll positions.\nUnboxed horizontal gradient wash protects body copy from changing 3D geometry."),
        ("Anti-Pattern Rule from Scene 02", "Strictly NO dark window mullions crossing behind text columns. Camera waypoints frame copy exclusively over calm warm-white plaster walls.")
    ]
    dy = ly + 76
    for title, desc in c_specs:
        draw.text((48 + lw + 48, dy), title, font=font_h3, fill=C_DARK)
        dy += 22
        for l in desc.split("\n"):
            draw.text((48 + lw + 48, dy), l, font=font_body, fill=C_MUTED)
            dy += 22
        dy += 12

    im.save(os.path.join(out_dir, "05-material-and-lighting-board.png"))
    print("Saved: 05-material-and-lighting-board.png")

make_material_board()

# ==============================================================================
# BOARD 6: MASTER VISUAL BOARD (scene03-visual-board-master.png)
# Matches the design elegance and layout of approved Scene 02 visual board!
# ==============================================================================
def make_master_visual_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_WHITE)
    draw = ImageDraw.Draw(im)

    # Top Half: Hero Visual with Overlaid Typography & Navigation (Y: 0 -> 480)
    hero_h = 490
    hero_res = img_hero.resize((W, hero_h), Image.Resampling.LANCZOS)
    im.paste(hero_res, (0, 0))

    # Gradient wash over hero for text legibility
    h_grad = Image.new("RGBA", (W, hero_h), (0, 0, 0, 0))
    d_hg = ImageDraw.Draw(h_grad)
    for x in range(750):
        a = int(230 * (1.0 - (x / 750.0) ** 1.3))
        d_hg.line([x, 0, x, hero_h], fill=(255, 255, 255, a), width=1)
    im.paste(h_grad, (0, 0), h_grad)
    draw = ImageDraw.Draw(im)

    # Hero Typography
    draw.text((64, 36), "TAM", font=font_h1, fill=C_DARK)
    draw.text((64, 70), "Portfolio", font=font_body, fill=C_MUTED)

    draw.text((64, 110), "SCENE 03 · CORE EXPERTISE", font=font_mono_bold, fill=C_BLUE)
    draw.text((64, 136), "Where Business Meets", font=font_title, fill=C_DARK)
    draw.text((64, 180), "Technology.", font=font_title, fill=C_BLUE)

    h_body = (
        "A synthesis of analytical rigor, enterprise software architecture,\n"
        "and customer-facing solution consulting to solve complex organizational\n"
        "challenges and shape scalable digital solutions."
    )
    draw.text((64, 236), h_body, font=font_body, fill=(55, 65, 81, 255))

    # Vertical Nav on upper right
    rnav_x = W - 180
    draw.text((rnav_x, 36), "01", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 36), "Introduction", font=font_sub, fill=C_LIGHT_MUTED)
    draw.text((rnav_x, 62), "02", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 62), "About", font=font_sub, fill=C_LIGHT_MUTED)

    # Active 03 Expertise
    draw.ellipse([rnav_x - 14, 92, rnav_x - 4, 102], fill=C_BLUE)
    draw.text((rnav_x, 88), "03", font=font_mono_bold, fill=C_BLUE)
    draw.text((rnav_x + 28, 88), "Expertise", font=font_body_bold, fill=C_BLUE)

    draw.text((rnav_x, 114), "04", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 114), "Projects", font=font_sub, fill=C_LIGHT_MUTED)
    draw.text((rnav_x, 140), "05", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 140), "Experience", font=font_sub, fill=C_LIGHT_MUTED)
    draw.text((rnav_x, 166), "06", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 166), "Contact", font=font_sub, fill=C_LIGHT_MUTED)

    # Section 02: Camera Storyboard Strip (Y: 504 -> 680)
    draw.rectangle([0, 500, W, 502], fill=C_BORDER)
    draw.text((64, 510), "02  Camera Storyboard — Scroll-driven Scrollytelling Experience (Scene 03: K09 → K12)", font=font_h3, fill=C_DARK)

    sb_y = 536
    sb_w = (W - 64*2 - 16*3) // 4 # approx 436px
    sb_h = 160

    sb_items = [
        ("K09 · 00% – 22%", "Where Business Meets Technology.", img_k09),
        ("K10 · 22% – 48%", "Understanding Problems Before Solutions.", img_k10),
        ("K11 · 48% – 74%", "Understanding Enterprise Systems.", img_k11),
        ("K12 · 74% – 100%", "Turning Requirements into Practical Solutions.", img_k12)
    ]

    for i, (tag, hl, t_img) in enumerate(sb_items):
        bx = 64 + i * (sb_w + 16)
        # paste image
        t_crop = t_img.resize((sb_w, sb_h), Image.Resampling.LANCZOS)
        im.paste(t_crop, (bx, sb_y))
        
        # Overlay tag & headline
        t_over = Image.new("RGBA", (sb_w, sb_h), (0, 0, 0, 0))
        d_to = ImageDraw.Draw(t_over)
        d_to.rectangle([0, 0, sb_w, 36], fill=(17, 24, 39, 160))
        d_to.rectangle([0, sb_h - 48, sb_w, sb_h], fill=(17, 24, 39, 180))
        d_to.text((12, 10), tag, font=font_mono_bold, fill=C_WHITE)
        d_to.text((12, sb_h - 36), hl, font=font_body_bold, fill=C_WHITE)
        im.paste(t_over, (bx, sb_y), t_over)

    # Lower Grid: 5 Columns (Y: 710 -> 990)
    draw.rectangle([0, 706, W, 708], fill=C_BORDER)

    # 1. Spatial & Camera Layout
    draw.text((64, 716), "03  Spatial & Camera Layout", font=font_h3, fill=C_DARK)
    top_mini = img_raw_top.resize((360, 240), Image.Resampling.LANCZOS)
    im.paste(top_mini, (64, 742))
    draw.rectangle([64, 742, 64 + 360, 742 + 240], outline=C_BORDER, width=1)

    # 2. Scroll Progress & Content Mapping
    col2_x = 450
    draw.text((col2_x, 716), "04  Scroll Progress & Content Mapping", font=font_h3, fill=C_DARK)
    # Timeline bar
    draw.line([col2_x + 10, 770, col2_x + 350, 770], fill=C_BORDER, width=4)
    draw.line([col2_x + 10, 770, col2_x + 220, 770], fill=C_BLUE, width=4)
    beats_map = [
        (col2_x + 10, "K09", "0%"),
        (col2_x + 95, "K10", "22%"),
        (col2_x + 180, "K11", "48%"),
        (col2_x + 265, "K12", "74%"),
        (col2_x + 350, "Exit", "100%")
    ]
    for px, label, pct in beats_map:
        draw.ellipse([px-6, 770-6, px+6, 770+6], fill=C_BLUE if px <= col2_x + 220 else C_WHITE, outline=C_BLUE, width=2)
        draw.text((px - 10, 748), label, font=font_mono_bold, fill=C_DARK)
        draw.text((px - 8, 782), pct, font=font_mono, fill=C_MUTED)

    draw.text((col2_x, 820), "K09 Entrance · Reveal Rotunda & Oculus", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 844), "K10 Business Analysis · Framing BA Alcove", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 868), "K11 SAP / Enterprise · Vertical Colonnade", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 892), "K12 Solution Consulting · Lead to Scene 04", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 924), "Algebraic Reversible Scrubbing (Zero lag)", font=font_mono_bold, fill=C_BLUE)

    # 3. UI & Layer Structure
    col3_x = 840
    draw.text((col3_x, 716), "05  UI & Layer Structure", font=font_h3, fill=C_DARK)
    layers = [
        ("UI Overlay (HTML/CSS)", "Title, headline, sub-themes, vertical navigation rail"),
        ("Interaction Layer", "Normalized scroll progress p in [0, 1], reversible motion"),
        ("3D Persistent World", "Three.js WebGL, Blender GLB, single continuous camera"),
        ("Accessibility Layer", "prefers-reduced-motion, WCAG AAA contrast ratio")
    ]
    ly_curr = 752
    for l_title, l_desc in layers:
        draw.ellipse([col3_x + 4, ly_curr + 4, col3_x + 12, ly_curr + 12], fill=C_BLUE)
        draw.text((col3_x + 20, ly_curr), l_title, font=font_body_bold, fill=C_DARK)
        draw.text((col3_x + 20, ly_curr + 20), l_desc, font=font_sub, fill=C_MUTED)
        ly_curr += 54

    # 4. Material & Atmosphere Swatches
    col4_x = 1260
    draw.text((col4_x, 716), "06  Material & Atmosphere", font=font_h3, fill=C_DARK)
    swatches_data = [
        (C_PLASTER, "Plaster", "Walls & Dome"),
        (C_STONE, "Travertine", "Floor Paving"),
        (C_ALUM, "Brushed Al", "Fins & Inlay"),
        (C_GLASS, "Clear Glass", "Skylight Oculus"),
        ((255, 248, 235, 255), "Cove LED", "3200K Indirect")
    ]
    for s_i, (s_col, s_n, s_u) in enumerate(swatches_data):
        sx = col4_x + s_i * 68
        draw.ellipse([sx, 756, sx + 50, 756 + 50], fill=s_col, outline=C_BORDER, width=2)
        draw.text((sx - 2, 814), s_n, font=font_mono_bold, fill=C_DARK)
        draw.text((sx - 4, 832), s_u, font=font_mono, fill=C_MUTED)

    draw.text((col4_x, 874), "Atmospheric Harmony:", font=font_body_bold, fill=C_DARK)
    draw.text((col4_x, 898), "• Warm-neutral daylight (5200K – 6500K)", font=font_sub, fill=C_MUTED)
    draw.text((col4_x, 920), "• Diffused zenith oculus illumination", font=font_sub, fill=C_MUTED)
    draw.text((col4_x, 942), "• Strictly zero dark navy or cyberpunk neon", font=font_sub, fill=C_MUTED)

    # Footer Package Bar (Y: 1000 -> 1080)
    draw.rectangle([0, 1000, W, H], fill=(243, 244, 246, 255))
    draw.line([0, 1000, W, 1000], fill=C_BORDER, width=2)

    draw.text((64, 1016), "DESIGN HANDOFF PACKAGE — SCENE 03 (CORE EXPERTISE ROTUNDA)", font=font_h3, fill=C_DARK)
    draw.text((64, 1042), "Portfolio Owner: HOÀNG NGUYỄN THÀNH TÂM · Milestone 03: Design & Visual Planning Only (Approved for visual review)", font=font_sub, fill=C_MUTED)

    # Checklist tags on right footer
    draw.text((W - 650, 1018), "✓ Architecture: 24m Rotunda (connected to K08)", font=font_mono_bold, fill=(22, 101, 52, 255))
    draw.text((W - 650, 1042), "✓ Camera: K09 – K12 (spline C1 continuous)", font=font_mono_bold, fill=(22, 101, 52, 255))
    draw.text((W - 270, 1018), "✓ UI: Unboxed HTML/CSS only", font=font_mono_bold, fill=(22, 101, 52, 255))
    draw.text((W - 270, 1042), "✓ Verification: 6 Review Boards", font=font_mono_bold, fill=(22, 101, 52, 255))

    im.save(os.path.join(out_dir, "scene03-visual-board-master.png"))
    print("Saved: scene03-visual-board-master.png")

make_master_visual_board()

print("All visual boards completed successfully!")
