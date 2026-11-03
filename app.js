/**
 * Application Entry & Scroll Controller
 * Project Museum — Milestone 01: Entrance Atrium
 */

import { World } from './src/world.js';

class App {
  constructor() {
    this.canvas = document.getElementById('world');
    this.readingBar = document.getElementById('readingBar');
    this.scrollPercent = document.getElementById('scrollPercent');
    this.exploreBtn = document.getElementById('exploreBtn');
    this.navIntroBtn = document.getElementById('navIntro');
    this.heroContent = document.getElementById('heroContent');

    this.progress = 0;
    this.world = null;

    window.__app = this;
    this.init();
  }

  init() {
    // 1. Initialize persistent 3D world
    this.world = new World(this.canvas);

    // 2. Setup scroll listener
    this.bindScroll();

    // 3. Setup CTA interactions
    this.bindInteractions();

    // 4. Initial trigger
    this.updateScroll();
  }

  bindScroll() {
    const onScroll = () => {
      this.updateScroll();
    };

    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
  }

  updateScroll() {
    const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    const scrollY = window.scrollY || window.pageYOffset || 0;
    
    // Normalized local progress p in [0, 1]
    this.progress = Math.min(1, Math.max(0, scrollY / maxScroll));

    // Update 3D world target progress
    if (this.world) {
      this.world.setProgress(this.progress);
    }

    // Update UI Indicators
    const pct = Math.round(this.progress * 100);
    if (this.readingBar) {
      this.readingBar.style.width = `${pct}%`;
    }
    if (this.scrollPercent) {
      this.scrollPercent.textContent = `${pct.toString().padStart(2, '0')}%`;
    }

    // Softly reduce hero emphasis as we transition into K04 corridor handoff
    if (this.heroContent) {
      if (this.progress > 0.55) {
        const fade = Math.max(0, 1.0 - ((this.progress - 0.55) / 0.38));
        this.heroContent.style.opacity = fade.toFixed(2);
        this.heroContent.style.pointerEvents = this.progress > 0.80 ? 'none' : 'auto';
      } else {
        this.heroContent.style.opacity = '1';
        this.heroContent.style.pointerEvents = 'auto';
      }
    }
  }

  bindInteractions() {
    // Primary CTA: Explore My Work -> scrolls smoothly to K03 Installation Focus (progress = 0.66)
    if (this.exploreBtn) {
      this.exploreBtn.addEventListener('click', () => {
        const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
        const targetScroll = maxScroll * 0.66; // K03 Installation focus position
        window.scrollTo({
          top: targetScroll,
          behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
        });
      });
    }

    // Intro Nav click -> scrolls to top (progress = 0.00)
    if (this.navIntroBtn) {
      this.navIntroBtn.addEventListener('click', () => {
        window.scrollTo({
          top: 0,
          behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
        });
      });
    }
  }
}

// Instantiate on DOM load
window.addEventListener('DOMContentLoaded', () => {
  new App();
});
