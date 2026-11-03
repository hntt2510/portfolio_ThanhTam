# portfolio_ThanhTam

## Project Museum — Milestone 01: Entrance Atrium

An architectural, scroll-driven 3D personal portfolio built with **Three.js** and semantic HTML/CSS, adhering to the **Glass & Light Museum** visual design specification.

## Quick Start (Run Locally)

No `npm install` or complex build step required. The application runs natively on modern web browsers using vanilla ES Modules.

1. Open terminal in this folder:
   ```bash
   cd d:\THANHTAM\CV\Portfolio
   ```
2. Start any local static HTTP server, for example:
   ```bash
   python -m http.server 8000
   ```
   *or open with VS Code "Live Server" extension.*
3. Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## Architectural Highlights

- **Persistent 3D World**: Single canvas `#world` with high-performance `WebGLRenderer` configured with ACES Filmic tone mapping, soft shadows, and museum-grade daylighting.
- **Glass & Light Museum Aesthetic**:
  - Circular atrium with high curved walls and expansive light-stone floor.
  - Large circular skylight streaming natural diffused daylight.
  - Central installation: low circular stone pedestal and three staggered frosted-glass panels (`MeshPhysicalMaterial` with realistic transmission, roughness, and thickness).
  - Three pillar disciplines labeled: *Business Analysis*, *Enterprise Systems*, *Technology Solutions*.
- **Camera Motion Ledger**:
  - **K01 Establishing (0.00 - 0.25)**: Wide entrance threshold shot.
  - **K02 Forward Dolly (0.25 - 0.50)**: Smooth perspective zoom toward the installation.
  - **K03 Installation Focus (0.50 - 0.75)**: Subtle 10° arc revealing glass layer depth and aluminum trim.
  - **K04 Transition Alignment (0.75 - 1.00)**: Orientation toward the curved corridor leading to the future Profile Gallery.
- **Reversibility**: Camera trajectory is computed via smooth mathematical Catmull-Rom splines as a direct function of normalized scroll progress $p \in [0, 1]$.
- **Graceful Fallbacks**:
  - 2D Canvas architectural fallback when WebGL is unavailable.
  - Accessibility skip link, WCAG AA color contrast, and `prefers-reduced-motion` compliance.

---

## File Structure

```
Portfolio/
├── index.html                    # Semantic HTML entry point, overlays & navigation
├── styles.css                    # Glass & Light Museum design system
├── app.js                        # Master orchestrator & native scroll controller
├── src/
│   ├── world.js                  # Persistent Three.js renderer, scene & fallback manager
│   ├── camera-controller.js      # Catmull-Rom camera waypoints for beats K01–K04
│   └── scenes/
│       └── entrance-atrium.js    # Atrium architecture, skylight & frosted glass installation
├── assets/
│   ├── Hoang-Nguyen-Thanh-Tam-CV.pdf  # Verified resume asset
│   ├── vendor/three.module.js    # Pinned Three.js v0.180.0 for offline execution
│   └── visual-references/        # Design reference images
└── README.md                     # Documentation & usage instructions
```
