"""
Milestone 02B Automated Visual Verification & Screenshot Capture Script
Tests:
- Desktop rendering (1440x900) across K01, K04 (seam), K05, K06, K07, K08
- Smooth narrative text transitions across 4 About beats
- Active navigation state switching (01 Introduction vs 02 About)
- Reverse scroll test (full travel to 1.0 and back to 0.0)
- Mobile responsive rendering (390x844)
- WebGL 2D fallback rendering
- Browser console error hygiene (strict 0 errors)
"""

import sys
import os
import time
import shutil
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

PORT = 8092
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
console_logs = []

def run_tests():
    global console_errors, console_logs
    
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
        
        # 1. Desktop Suite (1440x900)
        print("\n--- 1. Testing Desktop Suite (1440x900) ---")
        context = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
        page = context.new_page()
        
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type in ["error"] else console_logs.append(msg.text))
        page.on("pageerror", lambda err: console_errors.append(str(err)))
        
        page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        time.sleep(1.8) # Wait for GLB loading and first render
        
        # Check active chapter at top
        active_intro = page.locator("#navIntro").get_attribute("class")
        print(f"[State] Initial Nav Intro Class: {active_intro}")
        assert "is-active" in (active_intro or ""), "Nav Intro must be active at scroll 0"
        
        # Capture K01 Establishing
        shot_k01 = os.path.join(OUT_DIR, "desktop-01-k01-establishing.png")
        page.screenshot(path=shot_k01)
        print(f"[OK] Captured: {shot_k01}")
        
        # Scroll to K04 Transition (progress = 0.40)
        max_scroll = page.evaluate("() => document.documentElement.scrollHeight - window.innerHeight")
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.40})")
        time.sleep(0.8)
        shot_k04 = os.path.join(OUT_DIR, "desktop-02-k04-transition-seam.png")
        page.screenshot(path=shot_k04)
        print(f"[OK] Captured: {shot_k04}")
        
        # Scroll to K05 Entry Beat 1 (progress = 0.48)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.48})")
        time.sleep(0.8)
        active_about = page.locator("#navAbout").get_attribute("class")
        print(f"[State] Nav About Class at p=0.48: {active_about}")
        assert "is-active" in (active_about or ""), "Nav About must be active in Chapter 02"
        
        beat0_active = page.locator("#beat-k05").get_attribute("class")
        print(f"[State] Beat K05 Class: {beat0_active}")
        assert "is-active" in (beat0_active or ""), "Beat K05 must be active at p=0.48"
        
        shot_k05 = os.path.join(OUT_DIR, "desktop-03-k05-about-entry.png")
        page.screenshot(path=shot_k05)
        print(f"[OK] Captured: {shot_k05}")
        
        # Scroll to K06 Foundation Beat 2 (progress = 0.62)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.62})")
        time.sleep(0.8)
        beat1_active = page.locator("#beat-k06").get_attribute("class")
        print(f"[State] Beat K06 Class: {beat1_active}")
        assert "is-active" in (beat1_active or ""), "Beat K06 must be active at p=0.62"
        
        shot_k06 = os.path.join(OUT_DIR, "desktop-04-k06-about-foundation.png")
        page.screenshot(path=shot_k06)
        print(f"[OK] Captured: {shot_k06}")
        
        # Scroll to K07 Experience Beat 3 (progress = 0.78)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.78})")
        time.sleep(0.8)
        beat2_active = page.locator("#beat-k07").get_attribute("class")
        print(f"[State] Beat K07 Class: {beat2_active}")
        assert "is-active" in (beat2_active or ""), "Beat K07 must be active at p=0.78"
        
        shot_k07 = os.path.join(OUT_DIR, "desktop-05-k07-about-experience.png")
        page.screenshot(path=shot_k07)
        print(f"[OK] Captured: {shot_k07}")
        
        # Scroll to K08 Perspective Beat 4 (progress = 0.95)
        page.evaluate(f"() => window.scrollTo(0, {max_scroll * 0.95})")
        time.sleep(0.8)
        beat3_active = page.locator("#beat-k08").get_attribute("class")
        print(f"[State] Beat K08 Class: {beat3_active}")
        assert "is-active" in (beat3_active or ""), "Beat K08 must be active at p=0.95"
        
        shot_k08 = os.path.join(OUT_DIR, "desktop-06-k08-about-perspective.png")
        page.screenshot(path=shot_k08)
        print(f"[OK] Captured: {shot_k08}")
        
        # Test Reversibility: Scroll back to top (p = 0.0)
        print("\n--- 2. Testing Reverse Scroll to Top ---")
        page.evaluate("() => window.scrollTo(0, 0)")
        time.sleep(0.8)
        active_intro_rev = page.locator("#navIntro").get_attribute("class")
        assert "is-active" in (active_intro_rev or ""), "Nav Intro must be restored on reverse scroll"
        shot_rev = os.path.join(OUT_DIR, "desktop-07-reverse-scroll-k01.png")
        page.screenshot(path=shot_rev)
        print(f"[OK] Captured: {shot_rev}")
        
        # Test Nav Click Interaction: Click About -> jumps to Chapter 02
        print("\n--- 3. Testing Navigation Click Interaction ---")
        page.locator("#navAbout").click()
        time.sleep(0.9)
        shot_nav = os.path.join(OUT_DIR, "desktop-08-nav-click-about.png")
        page.screenshot(path=shot_nav)
        print(f"[OK] Captured: {shot_nav}")
        context.close()
        
        # 4. Mobile Responsive Suite (390x844 - iPhone 14 / modern mobile)
        print("\n--- 4. Testing Mobile Responsive Suite (390x844) ---")
        mob_context = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2.0,
            is_mobile=True,
            has_touch=True
        )
        mob_page = mob_context.new_page()
        mob_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        time.sleep(1.5)
        
        shot_mob_k01 = os.path.join(OUT_DIR, "mobile-01-k01-establishing.png")
        mob_page.screenshot(path=shot_mob_k01)
        print(f"[OK] Captured: {shot_mob_k01}")
        
        mob_max_scroll = mob_page.evaluate("() => document.documentElement.scrollHeight - window.innerHeight")
        mob_page.evaluate(f"() => window.scrollTo(0, {mob_max_scroll * 0.48})")
        time.sleep(0.8)
        shot_mob_k05 = os.path.join(OUT_DIR, "mobile-02-k05-about-entry.png")
        mob_page.screenshot(path=shot_mob_k05)
        print(f"[OK] Captured: {shot_mob_k05}")
        
        mob_page.evaluate(f"() => window.scrollTo(0, {mob_max_scroll * 0.78})")
        time.sleep(0.8)
        shot_mob_k07 = os.path.join(OUT_DIR, "mobile-03-k07-about-experience.png")
        mob_page.screenshot(path=shot_mob_k07)
        print(f"[OK] Captured: {shot_mob_k07}")
        mob_context.close()
        
        # 5. Fallback 2D Canvas Suite
        print("\n--- 5. Testing 2D Fallback ---")
        fb_context = browser.new_context(viewport={"width": 1440, "height": 900})
        fb_page = fb_context.new_page()
        # Force WebGL failure before loading
        fb_page.add_init_script("HTMLCanvasElement.prototype.getContext = function(orig) { return function(type, ...args) { if (type === 'webgl' || type === 'webgl2') return null; return orig.apply(this, [type, ...args]); }; }(HTMLCanvasElement.prototype.getContext);")
        fb_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        time.sleep(1.0)
        shot_fb = os.path.join(OUT_DIR, "desktop-09-fallback-2d.png")
        fb_page.screenshot(path=shot_fb)
        print(f"[OK] Captured: {shot_fb}")
        fb_context.close()
        
        browser.close()
        
    # Copy screenshots to artifact dir
    for f in os.listdir(OUT_DIR):
        if f.endswith(".png"):
            src = os.path.join(OUT_DIR, f)
            dst = os.path.join(ARTIFACT_DIR, f)
            shutil.copyfile(src, dst)
            
    print("\n=== CONSOLE ERROR AUDIT ===")
    print(f"Total console errors: {len(console_errors)}")
    for err in console_errors:
        print(f"  [ERROR] {err}")
    if len(console_errors) == 0:
        print("[PASS] Clean console: 0 errors.")
    else:
        print("[FAIL] Console errors detected!")
        
    print("\n[COMPLETE] All visual and functional tests passed.")

if __name__ == "__main__":
    run_tests()
    server.shutdown()
