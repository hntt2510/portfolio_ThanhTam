/**
 * Application Entry & Scroll Controller
 * Project Museum:
 *  - Chapter 01: Entrance Atrium (K01 - K04)
 *  - Chapter 02: Profile Gallery (K05 - K08)
 */

import { World } from './src/world.js';

class App {
  constructor() {
    this.canvas = document.getElementById('world');
    this.readingBar = document.getElementById('readingBar');
    this.scrollPercent = document.getElementById('scrollPercent');
    this.exploreBtn = document.getElementById('exploreBtn');
    this.navIntroBtn = document.getElementById('navIntro');
    this.navAboutBtn = document.getElementById('navAbout');
    this.heroContent = document.getElementById('heroContent');
    this.aboutContent = document.getElementById('aboutContent');
    this.scrollHintText = document.getElementById('scrollHintText');

    this.beats = [
      document.getElementById('beat-k05'),
      document.getElementById('beat-k06'),
      document.getElementById('beat-k07'),
      document.getElementById('beat-k08')
    ];

    this.progress = 0;
    this.currentChapter = 1;
    this.currentBeatIndex = 0;
    this.world = null;

    window.__app = this;
    this.init();
  }

  init() {
    // 1. Initialize persistent 3D world
    this.world = new World(this.canvas);

    // 2. Setup scroll listener
    this.bindScroll();

    // 3. Setup CTA & Navigation interactions
    this.bindInteractions();

    // 4. Initial update
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
    
    // Normalized global progress p in [0, 1]
    this.progress = Math.min(1, Math.max(0, scrollY / maxScroll));

    // Update 3D world target progress
    if (this.world) {
      this.world.setProgress(this.progress);
    }

    // Update Global Reading Indicators
    const pct = Math.round(this.progress * 100);
    if (this.readingBar) {
      this.readingBar.style.width = `${pct}%`;
    }
    if (this.scrollPercent) {
      this.scrollPercent.textContent = `${pct.toString().padStart(2, '0')}%`;
    }

    // Centralized Chapter & Narrative Schedule:
    //  - Chapter 01 (Entrance Atrium): p in [0.00, 0.40]
    //  - Chapter 02 (Profile Gallery): p in (0.40, 1.00]
    if (this.progress <= 0.40) {
      // Chapter 01 Active
      this.currentChapter = 1;

      if (this.navIntroBtn) {
        this.navIntroBtn.classList.add('is-active');
        this.navIntroBtn.setAttribute('aria-current', 'step');
      }
      if (this.navAboutBtn) {
        this.navAboutBtn.classList.remove('is-active');
        this.navAboutBtn.removeAttribute('aria-current');
      }

      if (this.scrollHintText) {
        this.scrollHintText.textContent = 'SCROLL TO EXPLORE ATRIUM ↘';
      }

      // Hero overlay cross-fade
      if (this.heroContent) {
        if (this.progress <= 0.28) {
          this.heroContent.style.opacity = '1';
          this.heroContent.style.pointerEvents = 'auto';
        } else {
          const fade = Math.max(0, 1.0 - ((this.progress - 0.28) / 0.12));
          this.heroContent.style.opacity = fade.toFixed(2);
          this.heroContent.style.pointerEvents = this.progress > 0.35 ? 'none' : 'auto';
        }
      }

      // Hide About overlay
      if (this.aboutContent) {
        this.aboutContent.classList.remove('is-visible');
        this.aboutContent.setAttribute('aria-hidden', 'true');
      }

    } else {
      // Chapter 02 Active (Profile Gallery)
      this.currentChapter = 2;

      if (this.navIntroBtn) {
        this.navIntroBtn.classList.remove('is-active');
        this.navIntroBtn.removeAttribute('aria-current');
      }
      if (this.navAboutBtn) {
        this.navAboutBtn.classList.add('is-active');
        this.navAboutBtn.setAttribute('aria-current', 'step');
      }

      if (this.scrollHintText) {
        this.scrollHintText.textContent = 'SCROLL TO EXPLORE PROFILE GALLERY ↘';
      }

      // Hide Hero overlay
      if (this.heroContent) {
        this.heroContent.style.opacity = '0';
        this.heroContent.style.pointerEvents = 'none';
      }

      // Show About overlay
      if (this.aboutContent) {
        this.aboutContent.classList.add('is-visible');
        this.aboutContent.setAttribute('aria-hidden', 'false');
      }

      // Chapter 02 Local Narrative Beats:
      // Local progress in [0, 1]
      const localP = (this.progress - 0.40) / 0.60;
      let targetBeat = 0;

      if (localP < 0.25) {
        targetBeat = 0; // K05 Entry
      } else if (localP < 0.50) {
        targetBeat = 1; // K06 Foundation
      } else if (localP < 0.75) {
        targetBeat = 2; // K07 Experience
      } else {
        targetBeat = 3; // K08 Perspective / Exit
      }

      if (this.currentBeatIndex !== targetBeat) {
        this.currentBeatIndex = targetBeat;
      }

      this.beats.forEach((beatEl, idx) => {
        if (!beatEl) return;
        if (idx === targetBeat) {
          beatEl.classList.add('is-active');
          beatEl.removeAttribute('aria-hidden');
        } else {
          beatEl.classList.remove('is-active');
          beatEl.setAttribute('aria-hidden', 'true');
        }
      });
    }
  }

  bindInteractions() {
    const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const scrollBehavior = isReducedMotion ? 'auto' : 'smooth';

    // Primary CTA: Explore My Work -> scrolls smoothly to K03 Installation Focus
    if (this.exploreBtn) {
      this.exploreBtn.addEventListener('click', () => {
        const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
        window.scrollTo({
          top: maxScroll * 0.27,
          behavior: scrollBehavior
        });
      });
    }

    // Intro Nav click -> scrolls to top (progress = 0.00)
    if (this.navIntroBtn) {
      this.navIntroBtn.addEventListener('click', () => {
        window.scrollTo({
          top: 0,
          behavior: scrollBehavior
        });
      });
    }

    // About Nav click -> scrolls smoothly to start of Scene 02 (progress = 0.41)
    if (this.navAboutBtn) {
      this.navAboutBtn.addEventListener('click', () => {
        const maxScroll = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
        window.scrollTo({
          top: maxScroll * 0.41,
          behavior: scrollBehavior
        });
      });
    }
  }
}

// Instantiate on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => new App());
} else {
  new App();
}
