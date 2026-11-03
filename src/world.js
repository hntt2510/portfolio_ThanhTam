/**
 * World: Master Three.js Scene and Renderer Manager
 * Houses the persistent 3D world, renderer, camera controller, and scene modules.
 */

import * as THREE from 'three';
import { CameraController } from './camera-controller.js';
import { EntranceAtriumScene } from './scenes/entrance-atrium.js';

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

      // 2. Persistent Scene with subtle museum atmosphere fog
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0xF7F8F6); // Warm White
      this.scene.fog = new THREE.Fog(0xF7F8F6, 18, 50);

      // 3. Perspective Camera
      const aspect = window.innerWidth / window.innerHeight;
      this.camera = new THREE.PerspectiveCamera(57, aspect, 0.1, 100);

      // 4. Camera Controller for K01 - K04 waypoints
      this.cameraController = new CameraController(this.camera);
      this.cameraController.setMobile(window.innerWidth < 768);

      // 5. Build Milestone 01: Entrance Atrium Scene (loads GLB)
      this.entranceAtrium = new EntranceAtriumScene(() => {
        if (this.cameraController) {
          this.cameraController.update(this.smoothProgress);
        }
        if (this.renderer && this.scene && this.camera) {
          this.renderer.render(this.scene, this.camera);
        }
      });
      this.scene.add(this.entranceAtrium.group);

      // Initial camera update at progress 0
      this.cameraController.update(0);
      this.renderer.render(this.scene, this.camera);

      // 6. Bind resize
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
      // Immediate responsive progress update with settling step
      this.smoothProgress += (this.targetProgress - this.smoothProgress) * 0.45;
      if (Math.abs(this.targetProgress - this.smoothProgress) < 0.01) {
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
      if (Math.abs(diff) > 0.0005) {
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

      // Architectural concentric rings (representing skylight & atrium)
      ctx.strokeStyle = 'rgba(111, 158, 200, 0.2)';
      ctx.lineWidth = 1.5;

      const cx = w * 0.58;
      const cy = h * 0.48;

      for (let r = 80; r <= 320; r += 45) {
        ctx.beginPath();
        ctx.arc(cx, cy, r, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Three frosted card outlines
      ctx.fillStyle = 'rgba(215, 232, 246, 0.35)';
      ctx.strokeStyle = 'rgba(111, 158, 200, 0.4)';
      ctx.lineWidth = 2;

      const cards = [
        { x: cx - 140, y: cy - 70, w: 90, h: 170, label: '01 BUSINESS ANALYSIS' },
        { x: cx - 35, y: cy - 110, w: 100, h: 210, label: '02 ENTERPRISE SYSTEMS' },
        { x: cx + 80, y: cy - 50, w: 85, h: 150, label: '03 TECH SOLUTIONS' }
      ];

      cards.forEach(c => {
        ctx.fillRect(c.x, c.y, c.w, c.h);
        ctx.strokeRect(c.x, c.y, c.w, c.h);
      });
    };

    drawFallback();
    window.addEventListener('resize', drawFallback);
  }

  destroy() {
    this.isRunning = false;
    window.removeEventListener('resize', this.onResize);
    this.entranceAtrium?.dispose();
    this.renderer?.dispose();
  }
}
