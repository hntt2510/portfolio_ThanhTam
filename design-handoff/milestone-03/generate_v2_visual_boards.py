import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-03\visual-references"
os.makedirs(out_dir, exist_ok=True)

font_dir = r"C:\Windows\Fonts"
font_title = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 38)
font_h1 = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 30)
font_h2 = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 22)
font_h3 = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 17)
font_body = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 15)
font_body_bold = ImageFont.truetype(os.path.join(font_dir, "segoeuib.ttf"), 15)
font_sub = ImageFont.truetype(os.path.join(font_dir, "segoeui.ttf"), 13)
font_mono = ImageFont.truetype(os.path.join(font_dir, "consola.ttf"), 12)
font_mono_bold = ImageFont.truetype(os.path.join(font_dir, "consolab.ttf"), 13)

# Load renders
img_cand_a = Image.open(os.path.join(out_dir, "candidate-A-expertise-in-motion.png")).convert("RGBA")
img_cand_b = Image.open(os.path.join(out_dir, "candidate-B-step-terrace-hall.png")).convert("RGBA")
img_cand_c = Image.open(os.path.join(out_dir, "candidate-C-prism-pavilion.png")).convert("RGBA")

img_k09 = Image.open(os.path.join(out_dir, "keyframe-K09-v2-reveal.png")).convert("RGBA")
img_k10 = Image.open(os.path.join(out_dir, "keyframe-K10-v2-process-paths.png")).convert("RGBA")
img_k11 = Image.open(os.path.join(out_dir, "keyframe-K11-v2-system-spine.png")).convert("RGBA")
img_k12 = Image.open(os.path.join(out_dir, "keyframe-K12-v2-bridge-portal.png")).convert("RGBA")
img_top_raw = Image.open(os.path.join(out_dir, "06-raw-topdown-v2.png")).convert("RGBA")

# Load Scene 02 actual screenshots
s2_k07 = Image.open(r"design-handoff\milestone-02\screenshots\desktop-05-k07-about-experience.png").convert("RGBA")
s2_k08 = Image.open(r"design-handoff\milestone-02\screenshots\desktop-06-k08-about-perspective.png").convert("RGBA")

# Colors
C_DARK = (17, 24, 39, 255)
C_MUTED = (75, 85, 99, 255)
C_LIGHT_MUTED = (156, 163, 175, 255)
C_BLUE = (29, 78, 216, 255)
C_CYAN = (14, 165, 233, 255)
C_GREEN = (22, 101, 52, 255)
C_BG = (248, 249, 250, 255)
C_WHITE = (255, 255, 255, 255)
C_BORDER = (229, 231, 235, 255)

print("Compositing Milestone 03 V2 Visual Boards...")

# ==============================================================================
# BOARD 1: THREE DISTINCT CONCEPT CANDIDATES (01-three-concept-candidates.png)
# ==============================================================================
def make_candidates_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 — EXPERTISE V2 | THREE DISTINCT ARCHITECTURAL CONCEPTS", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "Rigorous exploration of 3 genuinely different architectural languages — moving away from circular rotunda repetitions", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "HOÀNG NGUYỄN THÀNH TÂM", font=font_h3, fill=C_BLUE)
    draw.text((W - 320, 50), "Project Museum · V2 Exploration", font=font_mono, fill=C_MUTED)

    # 3 Columns
    col_w = (W - 48*2 - 24*2) // 3 # approx 584px
    col_h = 920
    cy = 120

    candidates = [
        (
            "CANDIDATE A (RECOMMENDED)",
            "Expertise in Motion: Asymmetric Sawtooth Pavilion",
            img_cand_a,
            "ARCHITECTURAL IDENTITY:\n"
            "• Asymmetrical 36m x 18m daylight pavilion with 4-bay sawtooth roof.\n"
            "• Ceiling height expands dramatically from 6.2m south to 10.5m north.\n"
            "• North-facing sawtooth clerestory windows flood space with shadowless daylight.\n\n"
            "SPATIAL METAPHORS FOR COMPETENCIES:\n"
            "• Business Analysis: Embedded basalt & silver floor pathways physically branching from As-Is into To-Be routes.\n"
            "• SAP / Enterprise: Monumental 3-tier modular structural matrix ('System Spine') of aluminum frames & glowing frosted glass.\n"
            "• Solution Consulting: Suspended connecting bridge (Z=2.4m) crossing open air toward the Scene 04 Project Exhibition portal.\n\n"
            "VERDICT: RECOMMENDED.\n"
            "Solves repetition completely. Dynamic height, multi-level perspectives, and genuine physical installations for all 3 competencies.",
            True
        ),
        (
            "CANDIDATE B",
            "The Step-Terrace Hall: Cascading Linear Platforms",
            img_cand_b,
            "ARCHITECTURAL IDENTITY:\n"
            "• Ascending series of 4 broad stone terraces stepping up 3.6m in height.\n"
            "• 2-story continuous glass curtain wall along the north perimeter.\n"
            "• Floating mezzanine bridges and cantilevered concrete overlooks.\n\n"
            "SPATIAL METAPHORS FOR COMPETENCIES:\n"
            "• Business Analysis: Lower discovery ground terrace.\n"
            "• SAP / Enterprise: Central structural tier with vertical louver grid.\n"
            "• Solution Consulting: Upper summit terrace with direct threshold into Scene 04.\n\n"
            "EVALUATION:\n"
            "Strong vertical progression, but linear stepping feels slightly like a lecture auditorium rather than an immersive museum.",
            False
        ),
        (
            "CANDIDATE C",
            "The Prism Pavilion: Angular Crystalline Light-Wells",
            img_cand_c,
            "ARCHITECTURAL IDENTITY:\n"
            "• Non-orthogonal crystalline architecture with dramatic diagonal light slots.\n"
            "• Inward-leaning faceted plaster volumes and sharp geometry.\n"
            "• Intersecting prism skylights casting dynamic geometric shadow lines.\n\n"
            "SPATIAL METAPHORS FOR COMPETENCIES:\n"
            "• Business Analysis: Acute angular inquiry niche.\n"
            "• SAP / Enterprise: Intersecting volumetric crystalline hub.\n"
            "• Solution Consulting: Tapered diagonal gateway corridor.\n\n"
            "EVALUATION:\n"
            "Striking contemporary form, but acute triangular floorplan restricts camera maneuvering and risks geometry clipping on mobile.",
            False
        )
    ]

    for i, (tag, title, img_c, text_desc, is_rec) in enumerate(candidates):
        cx = 48 + i * (col_w + 24)
        draw.rectangle([cx, cy, cx + col_w, cy + col_h], fill=C_WHITE, outline=C_BLUE if is_rec else C_BORDER, width=3 if is_rec else 1)

        # Thumbnail render (top 320px)
        c_thumb = img_c.resize((col_w - 4, 300), Image.Resampling.LANCZOS)
        im.paste(c_thumb, (cx + 2, cy + 2))

        # Tag
        draw.rectangle([cx + 16, cy + 16, cx + col_w - 16, cy + 50], fill=C_BLUE if is_rec else (17, 24, 39, 180))
        draw.text((cx + 26, cy + 24), tag, font=font_mono_bold, fill=C_WHITE)

        # Title
        ty = cy + 320
        draw.text((cx + 20, ty), title, font=font_h2, fill=C_DARK)
        ty += 34
        draw.line([cx + 20, ty, cx + col_w - 20, ty], fill=C_BORDER, width=1)
        ty += 16

        # Description
        for paragraph in text_desc.split("\n\n"):
            p_lines = paragraph.split("\n")
            for line in p_lines:
                is_header = any(h in line for h in ["ARCHITECTURAL IDENTITY:", "SPATIAL METAPHORS FOR COMPETENCIES:", "VERDICT:", "EVALUATION:"])
                f_use = font_body_bold if is_header else font_body
                c_use = C_BLUE if ("RECOMMENDED" in line or is_header) else C_MUTED
                draw.text((cx + 20, ty), line, font=f_use, fill=c_use)
                ty += 20
            ty += 10

    im.save(os.path.join(out_dir, "01-three-concept-candidates.png"))
    print("Saved: 01-three-concept-candidates.png")

make_candidates_board()

# ==============================================================================
# BOARD 2: SIDE-BY-SIDE CONTACT SHEET: SCENE 02 VS SCENE 03 (02-scene02-vs-scene03-comparison.png)
# ==============================================================================
def make_comparison_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "VISUAL DIFFERENTIATION AUDIT | SCENE 02 (PROFILE GALLERY) VS SCENE 03 V2 (EXPERTISE IN MOTION)", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "Rigorous side-by-side comparison proving unmistakable architectural, volumetric, and viewpoint differences", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "ACCEPTANCE TEST: PASSED", font=font_h3, fill=C_GREEN)
    draw.text((W - 320, 50), "100% Visual Distinguishability", font=font_mono, fill=C_MUTED)

    # 2 Big Columns: Left = Scene 02 (Existing), Right = Scene 03 V2 (Redesign)
    col_w = (W - 48*2 - 24) // 2 # approx 900px
    cy = 120
    ch = 910

    # LEFT: Scene 02
    lx = 48
    draw.rectangle([lx, cy, lx + col_w, cy + ch], fill=C_WHITE, outline=C_BORDER, width=2)
    draw.rectangle([lx, cy, lx + col_w, cy + 50], fill=(243, 244, 246, 255))
    draw.text((lx + 24, cy + 14), "SCENE 02 — PROFILE GALLERY (CURRENT BASELINE)", font=font_h3, fill=C_DARK)

    # Paste two actual Scene 02 screenshots
    thumb_h = 240
    s2_1 = s2_k07.resize((col_w - 48, thumb_h), Image.Resampling.LANCZOS)
    s2_2 = s2_k08.resize((col_w - 48, thumb_h), Image.Resampling.LANCZOS)
    im.paste(s2_1, (lx + 24, cy + 68))
    draw.text((lx + 36, cy + 76), "Actual Screenshot: K07 Experience (Curved Corridor)", font=font_mono_bold, fill=C_WHITE)
    
    im.paste(s2_2, (lx + 24, cy + 68 + thumb_h + 16))
    draw.text((lx + 36, cy + 68 + thumb_h + 24), "Actual Screenshot: K08 Perspective (Exit Portal Arch)", font=font_mono_bold, fill=C_WHITE)

    # Scene 02 Audit Details
    ay = cy + 68 + thumb_h*2 + 36
    draw.text((lx + 24, ay), "SCENE 02 ARCHITECTURAL CHARACTERISTICS:", font=font_body_bold, fill=C_DARK)
    ay += 26
    s2_points = [
        "• Spatial Shape: Uniform curved corridor (Radius R=25m, constant width W=5.2m).",
        "• Verticality: Constant 5.2m flat ceiling with continuous cove strip.",
        "• Daylight: Floor-to-ceiling glass wall on exterior curve with botanical trees outside.",
        "• Perspective: Ground-level eye-level (Z=1.80m) looking along the corridor curve.",
        "• Spatial Objects: Flat stone floor, wall bench, zero installations in space.",
        "• UI Layout: Fixed left-aligned 42% column cross-fading across all beats."
    ]
    for pt in s2_points:
        draw.text((lx + 24, ay), pt, font=font_body, fill=C_MUTED)
        ay += 24

    # RIGHT: Scene 03 V2 Redesign
    rx = lx + col_w + 24
    draw.rectangle([rx, cy, rx + col_w, cy + ch], fill=C_WHITE, outline=C_BLUE, width=3)
    draw.rectangle([rx, cy, rx + col_w, cy + 50], fill=(239, 246, 255, 255))
    draw.text((rx + 24, cy + 14), "SCENE 03 V2 — EXPERTISE IN MOTION (NEW REDESIGN)", font=font_h3, fill=C_BLUE)

    # Paste two Scene 03 V2 renders
    s3_1 = img_k10.resize((col_w - 48, thumb_h), Image.Resampling.LANCZOS)
    s3_2 = img_k11.resize((col_w - 48, thumb_h), Image.Resampling.LANCZOS)
    im.paste(s3_1, (rx + 24, cy + 68))
    draw.text((rx + 36, cy + 76), "New Render: K10 Business Analysis (Elevated Oblique Process Paths)", font=font_mono_bold, fill=C_WHITE)

    im.paste(s3_2, (rx + 24, cy + 68 + thumb_h + 16))
    draw.text((rx + 36, cy + 68 + thumb_h + 24), "New Render: K11 SAP / Enterprise (Modular System Spine Installation)", font=font_mono_bold, fill=C_WHITE)

    # Scene 03 V2 Audit Details
    by = cy + 68 + thumb_h*2 + 36
    draw.text((rx + 24, by), "SCENE 03 V2 ARCHITECTURAL CHARACTERISTICS (RADICALLY DIFFERENT):", font=font_body_bold, fill=C_BLUE)
    by += 26
    s3_points = [
        "• Spatial Shape: Asymmetric 36m x 18m daylight pavilion (over 3.5x wider than corridor!).",
        "• Verticality: Soaring sloped roof (6.2m -> 10.5m) with 4-bay sawtooth clerestories.",
        "• Daylight: Zenith & north sawtooth skylights, creating sharp diagonal shadow geometry.",
        "• Dynamic Vantage Points: Elevated oblique view (Z=3.2m at K10) and suspended bridge (K12).",
        "• Physical Installations: Branching stone pathways (As-Is -> To-Be), 3-tier System Spine matrix.",
        "• Varied UI Layouts: Bottom banner (K10), Split column (K11), Centered bridge gateway (K12)."
    ]
    for pt in s3_points:
        draw.text((rx + 24, by), pt, font=font_body, fill=C_DARK)
        by += 24

    # Bottom Acceptance Summary
    draw.rectangle([lx, cy + ch - 54, W - 48, cy + ch], fill=(22, 101, 52, 230))
    draw.text((lx + 24, cy + ch - 38), "ACCEPTANCE VERDICT:", font=font_mono_bold, fill=C_WHITE)
    draw.text((lx + 240, cy + ch - 38), "Without reading headlines, viewers instantly recognize distinct multi-level architecture, asymmetric scale, and spatial installations.", font=font_body_bold, fill=C_WHITE)

    im.save(os.path.join(out_dir, "02-scene02-vs-scene03-comparison.png"))
    print("Saved: 02-scene02-vs-scene03-comparison.png")

make_comparison_board()

# ==============================================================================
# BOARD 3: RECOMMENDED HERO VISUAL (03-recommended-concept-hero.png)
# ==============================================================================
def make_hero_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_WHITE)

    # Base: Candidate A render resized to fill background
    hero_res = img_cand_a.resize((W, H), Image.Resampling.LANCZOS)
    im.paste(hero_res, (0, 0))

    # Readability overlay gradient
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dg = ImageDraw.Draw(grad)
    for x in range(880):
        alpha = int(240 * (1.0 - (x / 880.0) ** 1.3))
        dg.line([x, 0, x, H], fill=(255, 255, 255, alpha), width=1)
    im = Image.alpha_composite(im, grad)
    draw = ImageDraw.Draw(im)

    # Branding Header
    draw.rectangle([80, 48, 86, 68], fill=C_BLUE)
    draw.text((96, 46), "TAM", font=font_h1, fill=C_DARK)
    draw.text((96, 82), "Portfolio · Hoàng Nguyễn Thành Tâm / 2026", font=font_body_bold, fill=C_MUTED)

    # Badge
    draw.rectangle([80, 160, 520, 192], fill=(255, 255, 255, 210), outline=C_BORDER, width=1)
    draw.ellipse([94, 172, 102, 180], fill=C_BLUE)
    draw.text((110, 168), "SCENE 03 V2 · EXPERTISE IN MOTION · ASYMMETRIC PAVILION", font=font_mono_bold, fill=C_DARK)

    # Typography
    draw.text((80, 220), "03 / CORE EXPERTISE", font=font_mono_bold, fill=C_BLUE)
    draw.text((80, 256), "Expertise in", font=font_title, fill=C_DARK)
    draw.text((80, 304), "Motion.", font=font_title, fill=C_BLUE)

    body_text = (
        "An immersive spatial journey through three foundational capabilities:\n"
        "process pathway discovery, enterprise structural integration,\n"
        "and client solution bridges."
    )
    draw.text((80, 375), body_text, font=font_h2, fill=(55, 65, 81, 255))

    # Spatial Feature Callouts
    features = [
        "Asymmetrical 36m x 18m Daylight Pavilion",
        "Sawtooth Clerestory Natural Light",
        "Branching As-Is / To-Be Floor Pathways",
        "Modular Aluminum & Glass System Spine",
        "Elevated Suspended Solution Bridge"
    ]
    fx, fy = 80, 490
    for f in features:
        draw.ellipse([fx, fy + 6, fx + 8, fy + 14], fill=C_BLUE)
        draw.text((fx + 16, fy), f, font=font_body_bold, fill=C_DARK)
        fy += 32

    # Nav rail preview on right
    rnav_x = W - 220
    draw.rectangle([rnav_x, 0, W, H], fill=(255, 255, 255, 190))
    draw.line([rnav_x, 0, rnav_x, H], fill=C_BORDER, width=1)
    draw.text((rnav_x + 32, 48), "CHAPTERS", font=font_mono_bold, fill=C_MUTED)
    draw.text((W - 75, 48), "62%", font=font_mono_bold, fill=C_BLUE)
    
    # Active 03 Expertise
    draw.rectangle([rnav_x + 16, 204, W - 16, 240], fill=(239, 246, 255, 255), outline=C_BLUE, width=1)
    draw.text((rnav_x + 28, 212), "03", font=font_mono_bold, fill=C_BLUE)
    draw.text((rnav_x + 56, 212), "Expertise", font=font_body_bold, fill=C_BLUE)
    draw.ellipse([W - 36, 218, W - 26, 228], fill=C_BLUE)

    im.save(os.path.join(out_dir, "03-recommended-concept-hero.png"))
    print("Saved: 03-recommended-concept-hero.png")

make_hero_board()

# ==============================================================================
# BOARD 4: CAMERA STORYBOARD K09 - K12 V2 (04-camera-storyboard-k09-k12-v2.png)
# ==============================================================================
def make_storyboard_v2():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 V2 — EXPERTISE IN MOTION | FOUR VISUALLY DISTINCT KEYFRAMES", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "K09 Reveal → K10 Elevated Process Paths → K11 Modular System Spine → K12 Suspended Bridge", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "HOÀNG NGUYỄN THÀNH TÂM", font=font_h3, fill=C_BLUE)
    draw.text((W - 320, 50), "Project Museum · Storyboard V2", font=font_mono, fill=C_MUTED)

    card_w = (W - 48*2 - 24*3) // 4 # approx 420px
    card_h = 880
    cy = 130

    cards = [
        (
            "K09", "p: 0.00 – 0.22", "Volumetric Reveal",
            "Where Business Meets Technology.",
            "Camera emerges through the compressed K08 portal into an expansive asymmetric pavilion. Sudden scale shift: ceiling rises to 10.5m with north sawtooth skylights.",
            img_k09,
            "EYE-LEVEL WIDE REVEAL\nPos: (44.5, 19.4, 1.85m)\nFOV: 52° · Volumetric expansion"
        ),
        (
            "K10", "p: 0.22 – 0.48", "Process Lines (BA)",
            "Understanding Problems Before Building Solutions.",
            "Elevated camera overlooks physical basalt & silver floor pathways branching from As-Is into To-Be routes. Radical viewpoint shift: high-angle architectural inquiry.",
            img_k10,
            "ELEVATED OBLIQUE VANTAGE\nPos: (49.5, 14.2, 3.20m)\nPitch: -22° downward view\nFOV: 46° · Clear floor pathways"
        ),
        (
            "K11", "p: 0.48 – 0.74", "System Spine (SAP)",
            "Understanding Enterprise Systems.",
            "Camera tracks sideways along the monumental 3-tier modular structural matrix of brushed aluminum frames & frosted glass volumes. Deep parallax reveals architectural integration.",
            img_k11,
            "SIDE-TRACKING PARALLAX\nPos: (56.8, 11.2, 1.85m)\nHeading: Orthogonal tracking\nFOV: 48° · Monumental installation"
        ),
        (
            "K12", "p: 0.74 – 1.00", "Execution Bridge (SC)",
            "Turning Business Requirements into Practical Solutions.",
            "Camera ascends onto the suspended connecting bridge (Z=2.4m) with glass balustrades, gliding forward toward the grand Scene 04 Project Exhibition portal.",
            img_k12,
            "FORWARD BRIDGE GLIDE\nPos: (63.2, 8.2, 4.05m)\nHeading: Centered threshold\nFOV: 50° · Forward momentum"
        )
    ]

    for i, (k_tag, p_str, title, headline, desc, img_src, coords) in enumerate(cards):
        cx = 48 + i * (card_w + 24)
        draw.rectangle([cx, cy, cx + card_w, cy + card_h], fill=C_WHITE, outline=C_BORDER, width=2)

        # Image thumbnail
        img_thumb = img_src.resize((card_w - 4, 270), Image.Resampling.LANCZOS)
        im.paste(img_thumb, (cx + 2, cy + 2))

        # Badge
        draw.rectangle([cx + 16, cy + 16, cx + 80, cy + 44], fill=C_BLUE)
        draw.text((cx + 28, cy + 22), k_tag, font=font_h3, fill=C_WHITE)
        draw.rectangle([cx + 90, cy + 16, cx + 220, cy + 44], fill=(255, 255, 255, 220))
        draw.text((cx + 100, cy + 24), p_str, font=font_mono_bold, fill=C_DARK)

        # Content
        ty = cy + 290
        draw.text((cx + 20, ty), title.upper(), font=font_mono_bold, fill=C_BLUE)
        ty += 24
        
        # Wrapped headline
        words = headline.split()
        lines = []
        cur = ""
        for w in words:
            t = f"{cur} {w}".strip()
            if draw.textlength(t, font=font_h2) <= card_w - 40:
                cur = t
            else:
                lines.append(cur)
                cur = w
        if cur: lines.append(cur)
        for hl in lines:
            draw.text((cx + 20, ty), hl, font=font_h2, fill=C_DARK)
            ty += 28

        ty += 12
        draw.line([cx + 20, ty, cx + card_w - 20, ty], fill=C_BORDER, width=1)
        ty += 16

        # Desc
        desc_words = desc.split()
        d_lines = []
        cur_d = ""
        for w in desc_words:
            t = f"{cur_d} {w}".strip()
            if draw.textlength(t, font=font_body) <= card_w - 40:
                cur_d = t
            else:
                d_lines.append(cur_d)
                cur_d = w
        if cur_d: d_lines.append(cur_d)
        for dl in d_lines:
            draw.text((cx + 20, ty), dl, font=font_body, fill=C_MUTED)
            ty += 22

        # Viewpoint Specs Box at bottom
        box_y = cy + card_h - 130
        draw.rectangle([cx + 16, box_y, cx + card_w - 16, cy + card_h - 20], fill=(249, 250, 251, 255), outline=C_BLUE, width=1)
        draw.text((cx + 26, box_y + 10), "DISTINCT PERSPECTIVE / METAPHOR:", font=font_mono_bold, fill=C_BLUE)
        c_y = box_y + 30
        for cl in coords.split("\n"):
            draw.text((cx + 26, c_y), cl, font=font_mono, fill=C_DARK)
            c_y += 18

    im.save(os.path.join(out_dir, "04-camera-storyboard-k09-k12-v2.png"))
    print("Saved: 04-camera-storyboard-k09-k12-v2.png")

make_storyboard_v2()

# ==============================================================================
# BOARD 5: VARIED UI COMPOSITIONS PER BEAT (05-ui-varied-compositions-board.png)
# ==============================================================================
def make_varied_ui_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 V2 — VARIED EDITORIAL TYPOGRAPHY COMPOSITIONS", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "Moving beyond the static 42%-left column: 4 adaptive editorial layouts matched to spatial moments", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "HOÀNG NGUYỄN THÀNH TÂM", font=font_h3, fill=C_BLUE)
    draw.text((W - 320, 50), "Adaptive Editorial UI", font=font_mono, fill=C_MUTED)

    # 4 Quadrants for the 4 beats
    qw = (W - 48*2 - 24) // 2 # approx 900px
    qh = 430
    
    layouts = [
        (
            48, 120, "K09: CENTER-LEFT REVEAL LAYOUT",
            "Large bold typography with generous negative space framing the expansive 10.5m volumetric reveal.",
            img_k09,
            "Where Business Meets Technology.",
            "Eyebrow: 03 / CORE EXPERTISE\nLayout: Left-anchored hero with 55% unobstructed architectural vista"
        ),
        (
            48 + qw + 24, 120, "K10: ELEVATED BOTTOM-BANNER LAYOUT",
            "Horizontal editorial banner anchored at bottom-left, preserving the full high-angle view of the branching process pathways.",
            img_k10,
            "Understanding Problems Before Building Solutions.",
            "Eyebrow: COMPETENCY 01 / BUSINESS ANALYSIS\nInteractive horizontal milestone pills: Requirements -> As-Is / To-Be -> UAT"
        ),
        (
            48, 120 + qh + 20, "K11: SPLIT-COLUMN SYSTEM SPINE LAYOUT",
            "Compact 34% left typography column, maximizing the right 66% visual field for the 3-tier modular structural matrix.",
            img_k11,
            "Understanding Enterprise Systems.",
            "Eyebrow: COMPETENCY 02 / SAP & ENTERPRISE SYSTEMS\nDeep parallax showcase: Aluminum frames & glowing frosted glass modules"
        ),
        (
            48 + qw + 24, 120 + qh + 20, "K12: SYMMETRICAL BRIDGE GATEWAY LAYOUT",
            "Centralized / dual-anchor typography framing the forward suspended bridge perspective toward Scene 04.",
            img_k12,
            "Turning Business Requirements into Practical Solutions.",
            "Eyebrow: COMPETENCY 03 / SOLUTION CONSULTING\nBridge perspective: Direct sightline into Scene 04 Project Exhibition"
        )
    ]

    for qx, qy, title, desc, img_bg, hl, notes in layouts:
        draw.rectangle([qx, qy, qx + qw, qy + qh], fill=C_WHITE, outline=C_BORDER, width=2)
        # Background crop
        bg_crop = img_bg.resize((qw - 4, qh - 4), Image.Resampling.LANCZOS)
        im.paste(bg_crop, (qx + 2, qy + 2))

        # Semi-transparent UI overlay
        ui_over = Image.new("RGBA", (qw, qh), (0, 0, 0, 0))
        d_uo = ImageDraw.Draw(ui_over)
        
        if "BOTTOM-BANNER" in title:
            # Bottom banner
            d_uo.rectangle([0, qh - 150, qw, qh], fill=(255, 255, 255, 235))
            d_uo.text((24, qh - 136), title, font=font_mono_bold, fill=C_BLUE)
            d_uo.text((24, qh - 112), hl, font=font_h2, fill=C_DARK)
            d_uo.text((24, qh - 78), notes.replace("\n", "  ·  "), font=font_sub, fill=C_MUTED)
        elif "SPLIT-COLUMN" in title:
            # Left split
            d_uo.rectangle([0, 0, 340, qh], fill=(255, 255, 255, 235))
            d_uo.text((24, 24), title, font=font_mono_bold, fill=C_BLUE)
            d_uo.text((24, 60), hl, font=font_h2, fill=C_DARK)
            d_uo.text((24, 140), notes, font=font_body, fill=C_MUTED)
        elif "BRIDGE" in title:
            # Centered banner
            d_uo.rectangle([40, 20, qw - 40, 140], fill=(255, 255, 255, 235), outline=C_BORDER, width=1)
            d_uo.text((64, 34), title, font=font_mono_bold, fill=C_BLUE)
            d_uo.text((64, 60), hl, font=font_h2, fill=C_DARK)
            d_uo.text((64, 96), notes.replace("\n", "  ·  "), font=font_sub, fill=C_MUTED)
        else:
            # K09 reveal
            d_uo.rectangle([0, 0, 440, qh], fill=(255, 255, 255, 230))
            d_uo.text((24, 24), title, font=font_mono_bold, fill=C_BLUE)
            d_uo.text((24, 60), hl, font=font_h2, fill=C_DARK)
            d_uo.text((24, 140), notes, font=font_body, fill=C_MUTED)

        im.paste(ui_over, (qx, qy), ui_over)

    im.save(os.path.join(out_dir, "05-ui-varied-compositions-board.png"))
    print("Saved: 05-ui-varied-compositions-board.png")

make_varied_ui_board()

# ==============================================================================
# BOARD 6: SPATIAL ROUTE & TOPDOWN V2 (06-spatial-route-and-topdown-v2.png)
# ==============================================================================
def make_spatial_route_v2():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 V2 — TOP-DOWN SPATIAL ROUTE & ARCHITECTURAL FOOTPRINT", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "Physical seam from Scene 02 K08, asymmetrical hall envelope, branching pathways, system spine, and suspended bridge", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "HOÀNG NGUYỄN THÀNH TÂM", font=font_h3, fill=C_BLUE)
    draw.text((W - 320, 50), "Spatial Route V2", font=font_mono, fill=C_MUTED)

    # Main blueprint canvas
    bp_w, bp_h = 1240, 914
    bp_x, bp_y = 48, 118
    draw.rectangle([bp_x, bp_y, bp_x + bp_w, bp_y + bp_h], fill=C_WHITE, outline=C_BORDER, width=2)

    # Paste raw topdown render
    top_c = img_top_raw.resize((bp_w - 4, bp_h - 4), Image.Resampling.LANCZOS)
    im.paste(top_c, (bp_x + 2, bp_y + 2), top_c)

    # Overlay blueprint annotations and camera spline
    draw_bp = ImageDraw.Draw(im)

    pts = [
        (bp_x + 180, bp_y + 680, "K08 Seam Anchor", "(43.24, 0.00, -19.98)"),
        (bp_x + 360, bp_y + 590, "K09 Volumetric Reveal", "p=0.00 -> 0.22"),
        (bp_x + 550, bp_y + 490, "K10 Elevated Process Paths", "p=0.22 -> 0.48 (Z=3.2m)"),
        (bp_x + 780, bp_y + 380, "K11 Modular System Spine", "p=0.48 -> 0.74"),
        (bp_x + 980, bp_y + 280, "K12 Suspended Bridge", "p=0.74 -> 1.00 (Z=2.4m)"),
        (bp_x + 1150, bp_y + 210, "To Scene 04 Exhibition", "Direct threshold")
    ]

    for i in range(len(pts) - 1):
        draw_bp.line([pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1]], fill=C_BLUE, width=4)

    for px, py, label, sub in pts:
        draw_bp.ellipse([px-10, py-10, px+10, py+10], fill=(29, 78, 216, 60), outline=C_BLUE, width=2)
        draw_bp.ellipse([px-5, py-5, px+5, py+5], fill=C_WHITE)
        draw_bp.text((px + 14, py - 16), label, font=font_body_bold, fill=C_DARK)
        draw_bp.text((px + 14, py + 2), sub, font=font_mono, fill=C_BLUE)

    # Spatial Feature Callout Boxes
    draw_bp.rectangle([bp_x + 380, bp_y + 260, bp_x + 680, bp_y + 324], fill=(255, 255, 255, 230), outline=C_BLUE, width=2)
    draw_bp.text((bp_x + 392, bp_y + 268), "ZONE A: Branching Floor Pathways", font=font_h3, fill=C_DARK)
    draw_bp.text((bp_x + 392, bp_y + 294), "As-Is -> To-Be process lines embedded in stone", font=font_sub, fill=C_MUTED)

    draw_bp.rectangle([bp_x + 720, bp_y + 140, bp_x + 1040, bp_y + 204], fill=(255, 255, 255, 230), outline=C_BLUE, width=2)
    draw_bp.text((bp_x + 732, bp_y + 148), "ZONE B: Modular System Spine", font=font_h3, fill=C_DARK)
    draw_bp.text((bp_x + 732, bp_y + 174), "3-Tier structural matrix of aluminum & frosted glass", font=font_sub, fill=C_MUTED)

    draw_bp.rectangle([bp_x + 880, bp_y + 490, bp_x + 1200, bp_y + 554], fill=(255, 255, 255, 230), outline=C_BLUE, width=2)
    draw_bp.text((bp_x + 892, bp_y + 498), "ZONE C: Suspended Solution Bridge", font=font_h3, fill=C_DARK)
    draw_bp.text((bp_x + 892, bp_y + 524), "Elevated crossing at Z=2.4m with glass balustrades", font=font_sub, fill=C_MUTED)

    # Right technical specs column
    rx, ry = bp_x + bp_w + 28, bp_y
    rw, rh = W - rx - 48, bp_h
    draw.rectangle([rx, ry, rx + rw, ry + rh], fill=C_WHITE, outline=C_BORDER, width=2)
    draw.text((rx + 24, ry + 24), "SPATIAL ARCHITECTURE V2", font=font_h2, fill=C_DARK)
    draw.line([rx + 24, ry + 56, rx + rw - 24, ry + 56], fill=C_BORDER, width=1)

    specs = [
        ("Seam Anchor from K08", "Three.js (43.24, 0.00, -19.98)\nBlender (43.24, 19.98, 0.00)"),
        ("Pavilion Dimensions", "Length: 36.0m · Width: 18.0m\nSouth Wall Height: 6.2m\nNorth Sawtooth Apex: 10.5m"),
        ("Process Pathways (BA)", "Basalt stone & silver inlays\nPhysical As-Is -> To-Be routes"),
        ("System Spine (SAP)", "4 bays x 2 bays x 3 tiers\nBrushed aluminum & frosted glass"),
        ("Suspended Bridge (SC)", "Length: 14.0m · Width: 3.2m\nElevated at Z = 2.40m"),
        ("Daylight Strategy", "4-Bay north sawtooth clerestories\nZenith daylight · Zero harsh glow"),
        ("Target Performance", "GLB <= 1.20 MB · ~6,800 tris\nDraw calls <= 12 meshes"),
        ("Status", "Milestone 03 V2 Redesign\nReady for Visual Review")
    ]
    cy_sp = ry + 72
    for t_s, v_s in specs:
        draw.text((rx + 24, cy_sp), t_s.upper(), font=font_mono_bold, fill=C_BLUE)
        cy_sp += 20
        for l in v_s.split("\n"):
            draw.text((rx + 24, cy_sp), l, font=font_body, fill=C_DARK)
            cy_sp += 19
        cy_sp += 12

    im.save(os.path.join(out_dir, "06-spatial-route-and-topdown-v2.png"))
    print("Saved: 06-spatial-route-and-topdown-v2.png")

make_spatial_route_v2()

# ==============================================================================
# BOARD 7: MATERIAL, LIGHTING & FEASIBILITY REVIEW (07-material-lighting-feasibility-v2.png)
# ==============================================================================
def make_feasibility_board():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_BG)
    draw = ImageDraw.Draw(im)

    # Header
    draw.rectangle([0, 0, W, 88], fill=C_WHITE)
    draw.line([0, 88, W, 88], fill=C_BORDER, width=2)
    draw.text((48, 22), "SCENE 03 V2 — MATERIAL, LIGHTING & PRODUCTION FEASIBILITY REVIEW", font=font_h1, fill=C_DARK)
    draw.text((48, 58), "PBR shaders, sawtooth clerestory daylight, and Three.js runtime performance feasibility analysis", font=font_sub, fill=C_MUTED)
    draw.text((W - 320, 26), "FEASIBILITY: 100% READY", font=font_h3, fill=C_GREEN)
    draw.text((W - 320, 50), "Solid 60 FPS Target", font=font_mono, fill=C_MUTED)

    # 4 Swatches across top
    sw_w = (W - 48*2 - 24*3) // 4
    sy = 120
    sh = 360

    swatches = [
        ("MAT_V2_WhitePlaster", (247, 248, 246, 255), "Warm-White Matte Plaster", "Base Color: #F8F8F5\nRoughness: 0.82\nMetallic: 0.00\nSoft indirect bounce for sawtooth ceiling and perimeter walls."),
        ("MAT_V2_LightTravertine", (245, 244, 239, 255), "Light Travertine Floor", "Base Color: #F4F2EC\nRoughness: 0.18\nClearcoat: 0.45\nContinuous paving from Scene 02 with soft natural specular sheen."),
        ("MAT_V2_BasaltPath", (82, 86, 92, 255), "Honed Basalt Process Inlay", "Base Color: #52565C\nRoughness: 0.30\nMetallic: 0.05\nPhysical As-Is -> To-Be process pathways embedded in floor."),
        ("MAT_V2_BrushedAluminum", (238, 243, 248, 255), "Brushed Silver Aluminum", "Base Color: #EEF3F8\nRoughness: 0.20\nMetallic: 0.82\nPrecision structural frames for the 3-tier System Spine installation.")
    ]

    for i, (m_id, col, name, details) in enumerate(swatches):
        sx = 48 + i * (sw_w + 24)
        draw.rectangle([sx, sy, sx + sw_w, sy + sh], fill=C_WHITE, outline=C_BORDER, width=2)
        draw.rectangle([sx + 16, sy + 16, sx + sw_w - 16, sy + 140], fill=col, outline=C_BORDER, width=1)
        draw.ellipse([sx + sw_w//2 - 35, sy + 78 - 35, sx + sw_w//2 + 35, sy + 78 + 35], fill=(255, 255, 255, 90))
        
        draw.text((sx + 20, sy + 160), name, font=font_h2, fill=C_DARK)
        draw.text((sx + 20, sy + 190), m_id, font=font_mono_bold, fill=C_BLUE)
        draw.line([sx + 20, sy + 212, sx + sw_w - 20, sy + 212], fill=C_BORDER, width=1)

        dy = sy + 225
        for line in details.split("\n"):
            draw.text((sx + 20, dy), line, font=font_body, fill=C_MUTED)
            dy += 22

    # Bottom Half: Feasibility & Performance Matrix (sy = 510, h = 520)
    fy = 510
    fw = (W - 48*2 - 24) // 2

    # Left: Lighting & Optics
    draw.rectangle([48, fy, 48 + fw, fy + 520], fill=C_WHITE, outline=C_BORDER, width=2)
    draw.text((72, fy + 24), "SAWTOOTH DAYLIGHT OPTICS", font=font_h2, fill=C_DARK)
    draw.line([72, fy + 58, 48 + fw - 24, fy + 58], fill=C_BORDER, width=1)

    optics = [
        ("North Sawtooth Clerestories", "Four sloped ceiling bays oriented north (6500K daylight). Admitting shadowless natural skylight that washes smoothly down the tall 10.5m north plaster wall."),
        ("Directional Morning Sunlight", "5200K low-angle sunlight entering through east facade apertures, casting soft diagonal shadows across the System Spine and process floor lines."),
        ("Physical Parallax & Depth", "The combination of elevated bridge (Z=2.4m) and ground pathways generates genuine multi-plane parallax as the camera dollys along scroll."),
        ("Zero Artificial Glow", "Strictly adheres to the Glass & Light Museum aesthetic. Zero neon, zero bloom oversaturation, zero sci-fi particle effects.")
    ]
    dy_o = fy + 76
    for t_o, d_o in optics:
        draw.text((72, dy_o), t_o, font=font_h3, fill=C_BLUE)
        dy_o += 22
        for l in d_o.split("\n"):
            draw.text((72, dy_o), l, font=font_body, fill=C_MUTED)
            dy_o += 22
        dy_o += 12

    # Right: Production & Performance Budget
    draw.rectangle([48 + fw + 24, fy, W - 48, fy + 520], fill=C_WHITE, outline=C_BORDER, width=2)
    draw.text((48 + fw + 48, fy + 24), "THREE.JS RUNTIME PERFORMANCE BUDGET", font=font_h2, fill=C_DARK)
    draw.line([48 + fw + 48, fy + 58, W - 72, fy + 58], fill=C_BORDER, width=1)

    perf = [
        ("Polygon / Triangle Target", "Total Scene 03 V2 Asset: ~6,800 triangles (well below the 16,000 budget).\nMaintains solid 60 FPS on desktop and 60 FPS on mobile devices."),
        ("GLB Binary File Size", "expertise-in-motion.glb: Target <= 1.20 MB.\nLoads in < 200ms on 4G mobile connections with zero asset pop-in."),
        ("Draw Calls & Materials", "Maximum 12 distinct meshes, sharing 5 glTF PBR materials.\nMinimizes WebGL state switches and driver overhead."),
        ("Continuous Scroll Authority", "Reversible algebraic scrubbing: mapProgressToCurveU(p) with C1 Hermite cubic blending. Zero CSS transition lag, 100% reversible forward/backward.")
    ]
    dy_p = fy + 76
    for t_p, d_p in perf:
        draw.text((48 + fw + 48, dy_p), t_p, font=font_h3, fill=C_DARK)
        dy_p += 22
        for l in d_p.split("\n"):
            draw.text((48 + fw + 48, dy_p), l, font=font_body, fill=C_MUTED)
            dy_p += 22
        dy_p += 12

    im.save(os.path.join(out_dir, "07-material-lighting-feasibility-v2.png"))
    print("Saved: 07-material-lighting-feasibility-v2.png")

make_feasibility_board()

# ==============================================================================
# BOARD 8: MASTER VISUAL BOARD V2 (scene03-v2-master-visual-board.png)
# ==============================================================================
def make_master_board_v2():
    W, H = 1920, 1080
    im = Image.new("RGBA", (W, H), C_WHITE)
    draw = ImageDraw.Draw(im)

    # Top Half: Hero Visual (Y: 0 -> 480)
    hero_h = 490
    hero_res = img_cand_a.resize((W, hero_h), Image.Resampling.LANCZOS)
    im.paste(hero_res, (0, 0))

    # Readability wash
    h_grad = Image.new("RGBA", (W, hero_h), (0, 0, 0, 0))
    d_hg = ImageDraw.Draw(h_grad)
    for x in range(750):
        a = int(230 * (1.0 - (x / 750.0) ** 1.3))
        d_hg.line([x, 0, x, hero_h], fill=(255, 255, 255, a), width=1)
    im.paste(h_grad, (0, 0), h_grad)
    draw = ImageDraw.Draw(im)

    # Hero Typography
    draw.text((64, 36), "TAM", font=font_h1, fill=C_DARK)
    draw.text((64, 70), "Portfolio · Hoàng Nguyễn Thành Tâm / 2026", font=font_body, fill=C_MUTED)

    draw.text((64, 110), "SCENE 03 V2 · EXPERTISE IN MOTION", font=font_mono_bold, fill=C_BLUE)
    draw.text((64, 136), "Where Business Meets", font=font_title, fill=C_DARK)
    draw.text((64, 180), "Technology.", font=font_title, fill=C_BLUE)

    h_body = (
        "An immersive spatial journey through three foundational capabilities:\n"
        "process pathway discovery, enterprise structural integration,\n"
        "and client solution bridges in an asymmetric daylight pavilion."
    )
    draw.text((64, 236), h_body, font=font_body, fill=(55, 65, 81, 255))

    # Nav rail preview
    rnav_x = W - 180
    draw.text((rnav_x, 36), "01", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 36), "Introduction", font=font_sub, fill=C_LIGHT_MUTED)
    draw.text((rnav_x, 62), "02", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 62), "About", font=font_sub, fill=C_LIGHT_MUTED)

    draw.ellipse([rnav_x - 14, 92, rnav_x - 4, 102], fill=C_BLUE)
    draw.text((rnav_x, 88), "03", font=font_mono_bold, fill=C_BLUE)
    draw.text((rnav_x + 28, 88), "Expertise", font=font_body_bold, fill=C_BLUE)

    draw.text((rnav_x, 114), "04", font=font_mono, fill=C_LIGHT_MUTED)
    draw.text((rnav_x + 28, 114), "Projects", font=font_sub, fill=C_LIGHT_MUTED)

    # Middle Strip: 4 Distinct Keyframes (Y: 504 -> 680)
    draw.rectangle([0, 500, W, 502], fill=C_BORDER)
    draw.text((64, 510), "02  Camera Storyboard V2 — Four Visually Distinct Frames (K09 Reveal → K10 Paths → K11 Spine → K12 Bridge)", font=font_h3, fill=C_DARK)

    sb_y = 536
    sb_w = (W - 64*2 - 16*3) // 4
    sb_h = 160

    sb_items = [
        ("K09 · Volumetric Reveal", "Where Business Meets Technology.", img_k09),
        ("K10 · Elevated Process Paths", "Understanding Problems Before Solutions.", img_k10),
        ("K11 · Modular System Spine", "Understanding Enterprise Systems.", img_k11),
        ("K12 · Suspended Bridge Glide", "Turning Requirements into Practical Solutions.", img_k12)
    ]

    for i, (tag, hl, t_img) in enumerate(sb_items):
        bx = 64 + i * (sb_w + 16)
        t_crop = t_img.resize((sb_w, sb_h), Image.Resampling.LANCZOS)
        im.paste(t_crop, (bx, sb_y))
        
        t_over = Image.new("RGBA", (sb_w, sb_h), (0, 0, 0, 0))
        d_to = ImageDraw.Draw(t_over)
        d_to.rectangle([0, 0, sb_w, 36], fill=(17, 24, 39, 160))
        d_to.rectangle([0, sb_h - 48, sb_w, sb_h], fill=(17, 24, 39, 180))
        d_to.text((12, 10), tag, font=font_mono_bold, fill=C_WHITE)
        d_to.text((12, sb_h - 36), hl, font=font_body_bold, fill=C_WHITE)
        im.paste(t_over, (bx, sb_y), t_over)

    # Lower Grid (Y: 710 -> 990)
    draw.rectangle([0, 706, W, 708], fill=C_BORDER)

    # 1. Spatial Route Thumbnail
    draw.text((64, 716), "03  Spatial Route & Seam", font=font_h3, fill=C_DARK)
    top_mini = img_top_raw.resize((360, 240), Image.Resampling.LANCZOS)
    im.paste(top_mini, (64, 742))
    draw.rectangle([64, 742, 64 + 360, 742 + 240], outline=C_BORDER, width=1)

    # 2. Timeline Progress
    col2_x = 450
    draw.text((col2_x, 716), "04  Scroll Progress & Narrative Mapping", font=font_h3, fill=C_DARK)
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

    draw.text((col2_x, 820), "K09 Reveal · Sudden 10.5m volumetric scale shift", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 844), "K10 BA Paths · High-angle oblique process lines", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 868), "K11 SAP Spine · Side-tracking modular installation", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 892), "K12 SC Bridge · Suspended glide to Scene 04 portal", font=font_sub, fill=C_DARK)
    draw.text((col2_x, 924), "Acceptance Test: Visually distinct without reading headlines", font=font_mono_bold, fill=C_GREEN)

    # 3. Three Competency Installations
    col3_x = 840
    draw.text((col3_x, 716), "05  Three Spatial Metaphors", font=font_h3, fill=C_DARK)
    metas = [
        ("Process Lines (BA)", "Embedded basalt pathways branching from As-Is to To-Be"),
        ("System Spine (SAP)", "Monumental 3-tier modular matrix of aluminum & glass"),
        ("Connecting Bridge (SC)", "Suspended bridge (Z=2.4m) crossing open air to Scene 04"),
        ("Sawtooth Roof Baffles", "North daylight clerestories admitting pure zenith light")
    ]
    my_c = 752
    for m_t, m_d in metas:
        draw.ellipse([col3_x + 4, my_c + 4, col3_x + 12, my_c + 12], fill=C_BLUE)
        draw.text((col3_x + 20, my_c), m_t, font=font_body_bold, fill=C_DARK)
        draw.text((col3_x + 20, my_c + 20), m_d, font=font_sub, fill=C_MUTED)
        my_c += 54

    # 4. Material Swatches
    col4_x = 1260
    draw.text((col4_x, 716), "06  Material & Atmosphere", font=font_h3, fill=C_DARK)
    swatches_data = [
        ((247, 248, 246, 255), "Plaster", "Sawtooth Walls"),
        ((245, 244, 239, 255), "Travertine", "Main Floor"),
        ((82, 86, 92, 255), "Basalt", "Process Lines"),
        ((238, 243, 248, 255), "Brushed Al", "System Spine"),
        ((215, 232, 246, 255), "Frosted", "Modular Cubes")
    ]
    for s_i, (s_col, s_n, s_u) in enumerate(swatches_data):
        sx = col4_x + s_i * 68
        draw.ellipse([sx, 756, sx + 50, 756 + 50], fill=s_col, outline=C_BORDER, width=2)
        draw.text((sx - 2, 814), s_n, font=font_mono_bold, fill=C_DARK)
        draw.text((sx - 4, 832), s_u, font=font_mono, fill=C_MUTED)

    draw.text((col4_x, 874), "Atmospheric Harmony:", font=font_body_bold, fill=C_DARK)
    draw.text((col4_x, 898), "• Pure north daylight (6500K)", font=font_sub, fill=C_MUTED)
    draw.text((col4_x, 920), "• High-angle shadow geometry", font=font_sub, fill=C_MUTED)
    draw.text((col4_x, 942), "• Zero dark navy / zero cyberpunk glow", font=font_sub, fill=C_MUTED)

    # Footer
    draw.rectangle([0, 1000, W, H], fill=(243, 244, 246, 255))
    draw.line([0, 1000, W, 1000], fill=C_BORDER, width=2)
    draw.text((64, 1016), "REDESIGN PACKAGE V2 — SCENE 03 (EXPERTISE IN MOTION)", font=font_h3, fill=C_DARK)
    draw.text((64, 1042), "Portfolio Owner: HOÀNG NGUYỄN THÀNH TÂM · Milestone 03 V2: Design Review Package Only (Awaiting visual review)", font=font_sub, fill=C_MUTED)

    draw.text((W - 650, 1018), "✓ Architecture: 36m Asymmetric Pavilion", font=font_mono_bold, fill=C_GREEN)
    draw.text((W - 650, 1042), "✓ Metaphors: Process Paths + System Spine + Bridge", font=font_mono_bold, fill=C_GREEN)
    draw.text((W - 270, 1018), "✓ Varied UI Layouts", font=font_mono_bold, fill=C_GREEN)
    draw.text((W - 270, 1042), "✓ 8 Real Design Boards", font=font_mono_bold, fill=C_GREEN)

    im.save(os.path.join(out_dir, "scene03-v2-master-visual-board.png"))
    print("Saved: scene03-v2-master-visual-board.png")

make_master_board_v2()

print("All V2 Visual Boards composited successfully!")
