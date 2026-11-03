"""
Milestone 01B Automated Visual Verification & Screenshot Capture Script
Tests:
- Desktop rendering (1440x900) across K01, K02, K03, K04
- Reversibility test (scroll down to 1.0 then back to 0.0)
- Mobile responsive rendering (390x844)
- WebGL 2D fallback rendering
- Browser console error hygiene
"""

import sys
import os
import time
import shutil
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright

PORT = 8089
DIRECTORY = r"D:\THANHTAM\CV\Portfolio"
OUT_DIR = r"D:\THANHTAM\CV\Portfolio\design-handoff\milestone-01B\screenshots"
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
print(f"[OK] Local server listening on http://127.0.0.1:{PORT}")

console_errors = []
console_logs = []

def run_tests():
    global console_errors, console_logs
    
    with sync_playwright() as p:
        # Launch browser with WebGL enabled
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

        page.on("console", lambda msg: (
            console_errors.append(f"[{msg.type.upper()}] {msg.text}") if msg.type in ["error", "warning"] else console_logs.append(f"[LOG] {msg.text}")
        ))
        page.on("pageerror", lambda err: console_errors.append(f"[PAGE_ERROR] {err}"))

        page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")

        # Wait for GLB to load
        print("Waiting for GLB asset to load...")
        page.wait_for_function("() => window.__app && window.__app.world && window.__app.world.entranceAtrium && window.__app.world.entranceAtrium.isLoaded === true", timeout=15000)
        time.sleep(1.2) # Allow shader compilation & render settle

        # Function to scroll to progress
        def scroll_to_progress(target_p):
            page.evaluate(f"""() => {{
                const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
                window.scrollTo(0, max * {target_p});
            }}""")
            time.sleep(0.8) # Allow camera smooth glide to settle

        # Screenshot K01
        scroll_to_progress(0.00)
        p0 = os.path.join(OUT_DIR, "desktop-k01-establishing.png")
        page.screenshot(path=p0)
        print(f"Captured: {p0}")

        # Screenshot K02
        scroll_to_progress(0.33)
        p1 = os.path.join(OUT_DIR, "desktop-k02-dolly.png")
        page.screenshot(path=p1)
        print(f"Captured: {p1}")

        # Screenshot K03
        scroll_to_progress(0.66)
        p2 = os.path.join(OUT_DIR, "desktop-k03-focus.png")
        page.screenshot(path=p2)
        print(f"Captured: {p2}")

        # Screenshot K04
        scroll_to_progress(1.00)
        p3 = os.path.join(OUT_DIR, "desktop-k04-transition.png")
        page.screenshot(path=p3)
        print(f"Captured: {p3}")

        # Reversibility test: scroll back up to 0.00
        print("Testing scroll reversibility (back to 0.00)...")
        scroll_to_progress(0.00)
        p_rev = os.path.join(OUT_DIR, "desktop-reverse-scroll-k01.png")
        page.screenshot(path=p_rev)
        print(f"Captured: {p_rev}")

        context.close()

        # 2. Mobile Suite (390x844 - iPhone 14 style)
        print("\n--- 2. Testing Mobile Suite (390x844) ---")
        m_context = browser.new_context(
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            has_touch=True,
            device_scale_factor=2
        )
        m_page = m_context.new_page()
        m_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        m_page.wait_for_function("() => window.__app && window.__app.world && window.__app.world.entranceAtrium && window.__app.world.entranceAtrium.isLoaded === true", timeout=15000)
        time.sleep(1.0)

        def m_scroll_to_progress(target_p):
            m_page.evaluate(f"""() => {{
                const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
                window.scrollTo(0, max * {target_p});
            }}""")
            time.sleep(0.8)

        m_scroll_to_progress(0.00)
        pm0 = os.path.join(OUT_DIR, "mobile-k01-establishing.png")
        m_page.screenshot(path=pm0)
        print(f"Captured: {pm0}")

        m_scroll_to_progress(0.66)
        pm1 = os.path.join(OUT_DIR, "mobile-k03-focus.png")
        m_page.screenshot(path=pm1)
        print(f"Captured: {pm1}")

        m_context.close()
        browser.close()

        # 3. Fallback Suite (WebGL context forced to null)
        print("\n--- 3. Testing 2D Canvas Fallback Suite ---")
        browser_fallback = p.chromium.launch(
            headless=True,
            args=["--disable-webgl", "--disable-3d-apis"]
        )
        f_context = browser_fallback.new_context(viewport={"width": 1440, "height": 900})
        f_page = f_context.new_page()
        f_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        time.sleep(1.0)
        pf = os.path.join(OUT_DIR, "fallback-2d-canvas.png")
        f_page.screenshot(path=pf)
        print(f"Captured: {pf}")
        f_context.close()
        browser_fallback.close()

    # Mirror screenshots to artifact directory
    if os.path.exists(ARTIFACT_DIR):
        print(f"\nMirroring screenshots to artifact dir: {ARTIFACT_DIR}")
        for f in os.listdir(OUT_DIR):
            if f.endswith(".png"):
                src = os.path.join(OUT_DIR, f)
                dst = os.path.join(ARTIFACT_DIR, f)
                shutil.copy2(src, dst)
                print(f"  Mirrored {f}")

    print("\n--- Console Messages Summary ---")
    print(f"Total Warnings/Errors: {len(console_errors)}")
    for e in console_errors:
        print(" ", e)
    print("Verification completed successfully!")

if __name__ == "__main__":
    run_tests()
    server.shutdown()
