/**
 * World: Master Three.js Scene and Renderer Manager
 * Houses the persistent 3D world, renderer, camera controller, and architectural scenes:
 *  - Scene 01: Entrance Atrium
 *  - Scene 02: Profile Gallery
 */

import * as THREE from 'three';
import { CameraController } from './camera-controller.js';
import { EntranceAtriumScene } from './scenes/entrance-atrium.js';
import { ProfileGalleryScene } from './scenes/profile-gallery.js';

export class World {
  constructor(canvasElement) {
    this.canvas = canvasElement;
    this.targetProgress = 0;
    this.smoothProgress = 0;
    this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.isRunning = false;

    this.init();
  }

  init() {
    try {
      // 1. WebGL Renderer with natural museum tone mapping and soft shadows
      this.renderer = new THREE.WebGLRenderer({
        canvas: this.canvas,
        antialias: true,
        alpha: false,
        powerPreference: 'high-performance'
      });
      this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.renderer.shadowMap.enabled = true;
      this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
      this.renderer.outputColorSpace = THREE.SRGBColorSpace;
      this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
      this.renderer.toneMappingExposure = 1.05;

      // 2. Persistent Scene with gentle museum atmosphere fog
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0xF5F8FA); // Daylight Sky White
      this.scene.fog = new THREE.Fog(0xF5F8FA, 32, 90);

      // 3. Perspective Camera
      const aspect = window.innerWidth / window.innerHeight;
      this.camera = new THREE.PerspectiveCamera(57, aspect, 0.1, 120);

      // 4. Camera Controller for K01 - K08 waypoints
      this.cameraController = new CameraController(this.camera);
      this.cameraController.setMobile(window.innerWidth < 768);

      // Trigger render callback on GLB load
      const onSceneLoaded = () => {
        if (this.cameraController) {
          this.cameraController.update(this.smoothProgress);
        }
        if (this.renderer && this.scene && this.camera) {
          this.renderer.render(this.scene, this.camera);
        }
      };

      // 5. Build Milestone 01: Entrance Atrium Scene
      this.entranceAtrium = new EntranceAtriumScene(onSceneLoaded);
      this.scene.add(this.entranceAtrium.group);

      // 6. Build Milestone 02: Profile Gallery Scene
      this.profileGallery = new ProfileGalleryScene(onSceneLoaded);
      this.scene.add(this.profileGallery.group);

      // Initial camera update at progress 0
      this.cameraController.update(0);
      this.renderer.render(this.scene, this.camera);

      // 7. Bind resize
      this.onResize = this.handleResize.bind(this);
      window.addEventListener('resize', this.onResize);

      // Start RAF loop
      this.isRunning = true;
      this.tick = this.render.bind(this);
      requestAnimationFrame(this.tick);

    } catch (err) {
      console.warn('WebGL initialization failed, falling back to 2D Canvas:', err);
      this.init2DFallback();
    }
  }

  handleResize() {
    if (!this.renderer || !this.camera) return;
    const width = window.innerWidth;
    const height = window.innerHeight;

    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();

    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));

    this.cameraController.setMobile(width < 768);
    this.cameraController.update(this.smoothProgress);
    this.renderer.render(this.scene, this.camera);
  }

  setProgress(p) {
    this.targetProgress = Math.min(1, Math.max(0, p));
    if (this.reducedMotion) {
      this.smoothProgress = this.targetProgress;
    } else {
      // Smooth responsive progress update with settling threshold
      this.smoothProgress += (this.targetProgress - this.smoothProgress) * 0.45;
      if (Math.abs(this.targetProgress - this.smoothProgress) < 0.005) {
        this.smoothProgress = this.targetProgress;
      }
    }
    
    // Immediate render update on scroll input
    if (this.cameraController) {
      this.cameraController.update(this.smoothProgress);
    }
    if (this.renderer && this.scene && this.camera) {
      this.renderer.render(this.scene, this.camera);
    }
  }

  render() {
    if (!this.isRunning) return;

    if (!this.reducedMotion) {
      const diff = this.targetProgress - this.smoothProgress;
      if (Math.abs(diff) > 0.0003) {
        this.smoothProgress += diff * 0.15;
        this.cameraController.update(this.smoothProgress);
        this.renderer.render(this.scene, this.camera);
      }
    }

    requestAnimationFrame(this.tick);
  }

  init2DFallback() {
    const ctx = this.canvas.getContext('2d');
    if (!ctx) return;

    const drawFallback = () => {
      const w = (this.canvas.width = window.innerWidth);
      const h = (this.canvas.height = window.innerHeight);

      ctx.fillStyle = '#F7F8F6';
      ctx.fillRect(0, 0, w, h);

      if (this.smoothProgress <= 0.40) {
        // Scene 01 Fallback: Architectural concentric rings
        ctx.strokeStyle = 'rgba(111, 158, 200, 0.2)';
        ctx.lineWidth = 1.5;

        const cx = w * 0.58;
        const cy = h * 0.48;

        for (let r = 80; r <= 320; r += 45) {
          ctx.beginPath();
          ctx.arc(cx, cy, r, 0, Math.PI * 2);
          ctx.stroke();
        }

        ctx.fillStyle = 'rgba(215, 232, 246, 0.35)';
        ctx.strokeStyle = 'rgba(111, 158, 200, 0.4)';
        ctx.lineWidth = 2;

        const cards = [
          { x: cx - 140, y: cy - 70, w: 90, h: 170 },
          { x: cx - 35, y: cy - 110, w: 100, h: 210 },
          { x: cx + 80, y: cy - 50, w: 85, h: 150 }
        ];

        cards.forEach(c => {
          ctx.fillRect(c.x, c.y, c.w, c.h);
          ctx.strokeRect(c.x, c.y, c.w, c.h);
        });
      } else {
        // Scene 02 Fallback: Curved gallery promenade arcs
        ctx.strokeStyle = 'rgba(111, 158, 200, 0.25)';
        ctx.lineWidth = 2;

        const cx = w * 0.85;
        const cy = h * 0.50;

        for (let r = 200; r <= 500; r += 60) {
          ctx.beginPath();
          ctx.arc(cx, cy, r, Math.PI * 0.65, Math.PI * 1.35);
          ctx.stroke();
        }

        // Promenade mullions
        ctx.strokeStyle = 'rgba(111, 158, 200, 0.18)';
        ctx.lineWidth = 1.5;
        for (let a = Math.PI * 0.70; a <= Math.PI * 1.30; a += 0.08) {
          ctx.beginPath();
          ctx.moveTo(cx + Math.cos(a) * 200, cy + Math.sin(a) * 200);
          ctx.lineTo(cx + Math.cos(a) * 500, cy + Math.sin(a) * 500);
          ctx.stroke();
        }
      }
    };

    drawFallback();
    window.addEventListener('resize', drawFallback);
  }

  destroy() {
    this.isRunning = false;
    window.removeEventListener('resize', this.onResize);
    this.entranceAtrium?.dispose();
    this.profileGallery?.dispose();
    this.renderer?.dispose();
  }
}
