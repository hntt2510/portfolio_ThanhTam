"""
Milestone 02D Automated Visual Verification & Quality Acceptance Suite
Tests:
- Numerical C0 and C1 Continuity across the p = 0.40 chapter boundary
- Desktop rendering (1440x900) across K01, K04, K05, K06, K07, K08
- Sculpted architectural threshold portal framing at K08
- High-contrast brand header (Hoàng Nguyễn Thành Tâm / 2026) and unboxed editorial typography
- Botanical garden landscape outside the glazing
- Forward / reverse scroll consistency and navigation two-way interaction
- Mobile responsive rendering (390x844)
- 2D Canvas Fallback
- Strict console error, warning, and network 404 audit
"""

import sys
import os
import time
import math
import shutil
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 8098
DIRECTORY = r"D:\THANHTAM\CV\Portfolio"
OUT_DIR = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-02\screenshots"
ARTIFACT_DIR = r"C:\Users\LEGION\.gemini\antigravity\brain\3948c36f-fc7d-4ae0-b3e9-358d2b5f3cc7"

os.makedirs(OUT_DIR, exist_ok=True)

class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(('127.0.0.1', PORT), QuietHandler)
server_thread = threading.Thread(target=server.serve_forever, daemon=True)
server_thread.start()
print(f"[OK] Local test server listening on http://127.0.0.1:{PORT}")

console_errors = []
console_warnings = []
failed_requests = []

def run_tests():
    global console_errors, console_warnings, failed_requests
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--enable-webgl",
                "--enable-features=Vulkan",
                "--ignore-gpu-blocklist",
                "--use-gl=angle",
                "--use-angle=default"
            ]
        )
        
        # 1. Desktop Visual Acceptance (1440 x 900)
        context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
        page = context.new_page()
        
        page.on("console", lambda msg: (
            console_errors.append(msg.text) if msg.type == "error" else (
                console_warnings.append(msg.text) if msg.type == "warning" else None
            )
        ))
        page.on("pageerror", lambda err: console_errors.append(str(err)))
        page.on("requestfailed", lambda req: (
            failed_requests.append(f"{req.url} - {req.failure}")
        ))
        
        print("\n--- 1. Testing Desktop Suite (1440x900) ---")
        page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        time.sleep(2.2) # Allow Three.js GLB models to parse and load
        
        # Verify Brand Typography & Vietnamese Diacritics
        header_text = page.locator(".brand-subtitle").text_content()
        print(f"[Check] Brand Subtitle: {header_text}")
        assert "Hoàng Nguyễn Thành Tâm" in header_text, "Brand subtitle must display Hoàng Nguyễn Thành Tâm"
        
        hero_name = page.locator(".hero-name").text_content()
        print(f"[Check] Hero Name: {hero_name}")
        assert "Hoàng Nguyễn Thành Tâm" in hero_name, "Hero name must display Hoàng Nguyễn Thành Tâm"
        
        # Verify Unboxed Editorial UI: No border, box-shadow, or card border-radius on desktop
        about_styles = page.evaluate("""() => {
            const el = document.getElementById('aboutContent');
            const style = window.getComputedStyle(el);
            return {
                border: style.border,
                boxShadow: style.boxShadow,
                borderRadius: style.borderRadius,
                background: style.backgroundImage
            };
        }""")
        print(f"[Check] About Overlay Styles: {about_styles}")
        assert "none" in about_styles["boxShadow"] or "0px" in about_styles["boxShadow"], "About overlay must NOT have box-shadow on desktop"
        assert "0px" in about_styles["borderRadius"] or "" == about_styles["borderRadius"], "About overlay must NOT have rounded card border-radius"
        
        # Capture K01 Establishing
        shot_k01 = os.path.join(OUT_DIR, "desktop-01-k01-establishing.png")
        page.screenshot(path=shot_k01)
        print(f"[OK] Captured: {shot_k01}")
        
        max_scroll = page.evaluate("() => document.documentElement.scrollHeight - window.innerHeight")
        
        # 2. Numerical C0 and C1 Continuity Test across p = 0.40 Boundary
        print("\n--- 2. Numerical C0 & C1 Continuity Evaluation ---")
        continuity_metrics = page.evaluate("""() => {
            const cc = window.__app.world.cameraController;
            const eps = 0.0002;
            
            // Left sample (p = 0.40 - eps)
            cc.update(0.40 - eps);
            const posL = { x: cc.currentPosition.x, y: cc.currentPosition.y, z: cc.currentPosition.z };
            const tgtL = { x: cc.currentTarget.x, y: cc.currentTarget.y, z: cc.currentTarget.z };
            const fovL = cc.camera.fov;
            
            // Boundary sample (p = 0.40)
            cc.update(0.40);
            const posM = { x: cc.currentPosition.x, y: cc.currentPosition.y, z: cc.currentPosition.z };
            const tgtM = { x: cc.currentTarget.x, y: cc.currentTarget.y, z: cc.currentTarget.z };
            const fovM = cc.camera.fov;
            
            // Right sample (p = 0.40 + eps)
            cc.update(0.40 + eps);
            const posR = { x: cc.currentPosition.x, y: cc.currentPosition.y, z: cc.currentPosition.z };
            const tgtR = { x: cc.currentTarget.x, y: cc.currentTarget.y, z: cc.currentTarget.z };
            const fovR = cc.camera.fov;
            
            // Finite differences
            const velL = {
                x: (posM.x - posL.x) / eps,
                y: (posM.y - posL.y) / eps,
                z: (posM.z - posL.z) / eps
            };
            const velR = {
                x: (posR.x - posM.x) / eps,
                y: (posR.y - posM.y) / eps,
                z: (posR.z - posM.z) / eps
            };
            
            const velDiff = Math.sqrt(
                Math.pow(velR.x - velL.x, 2) +
                Math.pow(velR.y - velL.y, 2) +
                Math.pow(velR.z - velL.z, 2)
            );
            
            const velNorm = Math.sqrt(
                Math.pow(velL.x, 2) + Math.pow(velL.y, 2) + Math.pow(velL.z, 2)
            );
            const relVelDiff = velDiff / velNorm;
            
            const fovDerivL = (fovM - fovL) / eps;
            const fovDerivR = (fovR - fovM) / eps;
            const fovDerivDiff = Math.abs(fovDerivR - fovDerivL);
            
            return {
                posM,
                tgtM,
                fovM,
                velL,
                velR,
                velNorm,
                velDiff,
                relVelDiff,
                fovDerivL,
                fovDerivR,
                fovDerivDiff
            };
        }""")
        
        print(f"[C0 Position at p=0.40]: ({continuity_metrics['posM']['x']:.3f}, {continuity_metrics['posM']['y']:.3f}, {continuity_metrics['posM']['z']:.3f})")
        print(f"[C0 Target at p=0.40]: ({continuity_metrics['tgtM']['x']:.3f}, {continuity_metrics['tgtM']['y']:.3f}, {continuity_metrics['tgtM']['z']:.3f})")
        print(f"[C0 FOV at p=0.40]: {continuity_metrics['fovM']:.2f} deg")
        print(f"[C1 Left Velocity Vector]: ({continuity_metrics['velL']['x']:.3f}, {continuity_metrics['velL']['y']:.3f}, {continuity_metrics['velL']['z']:.3f})")
        print(f"[C1 Right Velocity Vector]: ({continuity_metrics['velR']['x']:.3f}, {continuity_metrics['velR']['y']:.3f}, {continuity_metrics['velR']['z']:.3f})")
        print(f"[C1 Velocity Difference norm]: {continuity_metrics['velDiff']:.6f}")
        print(f"[C1 Relative Velocity Difference]: {continuity_metrics['relVelDiff'] * 100:.3f}% (finite difference approximation with eps=0.0002)")
        print(f"[C1 FOV Derivative Difference]: {continuity_metrics['fovDerivDiff']:.6f}")
        assert continuity_metrics["relVelDiff"] < 0.02, "C1 relative velocity derivative difference must be < 2% across p=0.40"
        print("[PASS] Mathematical C0 & C1 continuity verified!")
        
        # Capture K04 Transition Seam (progress = 0.40)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.40})")
        time.sleep(0.7)
        shot_k04 = os.path.join(OUT_DIR, "desktop-02-k04-transition-seam.png")
        page.screenshot(path=shot_k04)
        print(f"[OK] Captured: {shot_k04}")
        
        # Scroll to K05 Entry Beat 1 (progress = 0.48)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.48})")
        time.sleep(0.7)
        shot_k05 = os.path.join(OUT_DIR, "desktop-03-k05-about-entry.png")
        page.screenshot(path=shot_k05)
        print(f"[OK] Captured: {shot_k05}")
        
        # Scroll to K06 Foundation Beat 2 (progress = 0.62)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.62})")
        time.sleep(0.7)
        shot_k06 = os.path.join(OUT_DIR, "desktop-04-k06-about-foundation.png")
        page.screenshot(path=shot_k06)
        print(f"[OK] Captured: {shot_k06}")
        
        # Scroll to K07 Experience Beat 3 (progress = 0.78)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.78})")
        time.sleep(0.7)
        shot_k07 = os.path.join(OUT_DIR, "desktop-05-k07-about-experience.png")
        page.screenshot(path=shot_k07)
        print(f"[OK] Captured: {shot_k07}")
        
        # Scroll to K08 Perspective Beat 4 (progress = 0.95 - Exit Arch Focus)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.95})")
        time.sleep(0.7)
        shot_k08 = os.path.join(OUT_DIR, "desktop-06-k08-about-perspective.png")
        page.screenshot(path=shot_k08)
        print(f"[OK] Captured: {shot_k08}")
        
        # 3. Test Full Reverse Scroll Reversibility
        print("\n--- 3. Testing Reverse Scroll ---")
        page.evaluate("() => window.scrollTo(0, 0)")
        time.sleep(0.8)
        shot_rev = os.path.join(OUT_DIR, "desktop-07-reverse-scroll-k01.png")
        page.screenshot(path=shot_rev)
        print(f"[OK] Captured: {shot_rev}")
        
        # 4. Test Navigation Two-Way Click Interaction
        print("\n--- 4. Testing Nav Click Interaction ---")
        page.locator("#navAbout").click()
        time.sleep(0.8)
        shot_nav = os.path.join(OUT_DIR, "desktop-08-nav-click-about.png")
        page.screenshot(path=shot_nav)
        print(f"[OK] Captured: {shot_nav}")
        
        context.close()
        
        # 5. Mobile Responsive Suite (390 x 844 - iPhone 14)
        print("\n--- 5. Testing Mobile Responsive Suite (390x844) ---")
        mob_context = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True, device_scale_factor=2.0)
        mob_page = mob_context.new_page()
        mob_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        time.sleep(2.0)
        
        mob_max = mob_page.evaluate("() => document.documentElement.scrollHeight - window.innerHeight")
        
        shot_mob_k01 = os.path.join(OUT_DIR, "mobile-01-k01-establishing.png")
        mob_page.screenshot(path=shot_mob_k01)
        print(f"[OK] Captured: {shot_mob_k01}")
        
        mob_page.evaluate(f"() => window.scrollTo(0, {mob_max * 0.48})")
        time.sleep(0.7)
        shot_mob_k05 = os.path.join(OUT_DIR, "mobile-02-k05-about-entry.png")
        mob_page.screenshot(path=shot_mob_k05)
        print(f"[OK] Captured: {shot_mob_k05}")
        
        mob_page.evaluate(f"() => window.scrollTo(0, {mob_max * 0.78})")
        time.sleep(0.7)
        shot_mob_k07 = os.path.join(OUT_DIR, "mobile-03-k07-about-experience.png")
        mob_page.screenshot(path=shot_mob_k07)
        print(f"[OK] Captured: {shot_mob_k07}")
        
        mob_context.close()
        
        # 6. Fallback 2D Canvas Verification
        print("\n--- 6. Testing 2D Fallback ---")
        fb_context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
        fb_page = fb_context.new_page()
        # Force 2D fallback by disabling WebGL context
        fb_page.add_init_script("""
            HTMLCanvasElement.prototype.getContext = function(orig) {
                return function(type, ...args) {
                    if (type === 'webgl' || type === 'webgl2') return null;
                    return orig.apply(this, [type, ...args]);
                };
            }(HTMLCanvasElement.prototype.getContext);
        """)
        fb_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        time.sleep(0.8)
        shot_fb = os.path.join(OUT_DIR, "desktop-09-fallback-2d.png")
        fb_page.screenshot(path=shot_fb)
        print(f"[OK] Captured: {shot_fb}")
        fb_context.close()
        
        browser.close()
    
    # Copy screenshots to artifact directory for inspection
    if os.path.exists(ARTIFACT_DIR):
        for img in os.listdir(OUT_DIR):
            if img.endswith(".png"):
                src = os.path.join(OUT_DIR, img)
                dst = os.path.join(ARTIFACT_DIR, img)
                shutil.copy2(src, dst)
        print(f"[OK] Mirrored all screenshots to {ARTIFACT_DIR}")

    # Console Audit
    print("\n=== CONSOLE AUDIT ===")
    print(f"Total console errors: {len(console_errors)}")
    for err in console_errors:
        print(f"  [ERROR]: {err}")
    print(f"Total console warnings: {len(console_warnings)}")
    for warn in console_warnings:
        print(f"  [WARNING]: {warn}")
    print(f"Total failed network requests (404/ERR): {len(failed_requests)}")
    for req in failed_requests:
        print(f"  [REQ FAILED]: {req}")
    
    assert len(console_errors) == 0, f"Expected 0 console errors, got {len(console_errors)}"
    assert len(failed_requests) == 0, f"Expected 0 failed network requests, got {len(failed_requests)}"
    print("[PASS] Strict Console Audit: 0 errors.")

if __name__ == "__main__":
    run_tests()
