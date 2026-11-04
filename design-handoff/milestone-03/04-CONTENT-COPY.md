# Scene 03 — Core Expertise | Approved Content & Copy Specification

## 1. Owner Identity & Editorial Governance

- **Portfolio Owner:** **Hoàng Nguyễn Thành Tâm**
- **ASCII / URLs / Filenames:** Hoang Nguyen Thanh Tam / `Hoang-Nguyen-Thanh-Tam`
- **Tone & Positioning:** Professional, grounded, articulate, and academically sound. Strictly avoid inflated corporate buzzwords, fabricated enterprise client lists, or unverified claims of production SAP implementations. The narrative accurately portrays a solid software engineering background evolving into Business Analysis and SAP/ERP Functional Consulting.
- **Accessibility & UI Boundary:** 100% of this copy must be rendered directly in semantic HTML/CSS overlays (`index.html`). **Zero copy may be baked into textures, 3D meshes, glass panels, or virtual walls.**

---

## 2. Narrative Beat Copywriting

```
┌────────────────────────────────────────────────────────────────────────┐
│ K09: Entrance       │ "Where Business Meets Technology."              │
├────────────────────────────────────────────────────────────────────────┤
│ K10: Business Anal. │ "Understanding Problems Before Building Sol."   │
├────────────────────────────────────────────────────────────────────────┤
│ K11: SAP / ERP      │ "Understanding Enterprise Systems."             │
├────────────────────────────────────────────────────────────────────────┤
│ K12: Solution Cons. │ "Turning Business Requirements into Solutions." │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Beat 1: K09 — Entrance to Expertise (Overview / Synthesis)
- **Beat ID:** `beat-k09`
- **Scroll Trigger Range:** Scene 03 Local $p_{\text{local}} \in [0.00, 0.22]$
- **Eyebrow:** `03 / CORE EXPERTISE`
- **Headline:** `Where Business Meets <span class="highlight">Technology.</span>`
- **Body Copy:**  
  `A synthesis of analytical rigor, enterprise system understanding, and customer-focused consulting to solve real-world organizational challenges.`
- **Pill / Badge:**  
  `● SCENE 03 / EXPERTISE ROTUNDA · GLASS & LIGHT MUSEUM`

---

### Beat 2: K10 — Business Analysis (Inquiry & Structure)
- **Beat ID:** `beat-k10`
- **Scroll Trigger Range:** Scene 03 Local $p_{\text{local}} \in [0.22, 0.48]$
- **Eyebrow:** `COMPETENCY 01 / BUSINESS ANALYSIS`
- **Headline:** `Understanding Problems <span class="highlight">Before Building Solutions.</span>`
- **Body Copy:**  
  `Bridging the gap between stakeholder needs and technical execution through structured requirements elicitation, workflow modeling, and clear functional specifications.`
- **Competency Sub-themes (Rendered as interactive metadata pills):**  
  `Requirements Gathering` · `Business Processes` · `As-Is / To-Be Modeling` · `Functional Specifications` · `User Acceptance Testing (UAT)`
- **Pill / Badge:**  
  `● BUSINESS ANALYSIS · PROCESS & FUNCTIONAL SPECIFICATION`

---

### Beat 3: K11 — SAP / Enterprise Systems (Architecture & Integration)
- **Beat ID:** `beat-k11`
- **Scroll Trigger Range:** Scene 03 Local $p_{\text{local}} \in [0.48, 0.74]$
- **Eyebrow:** `COMPETENCY 02 / SAP & ENTERPRISE SYSTEMS`
- **Headline:** `Understanding <span class="highlight">Enterprise Systems.</span>`
- **Body Copy:**  
  `Exploring core enterprise resource planning, business process integration, and structured data flows to ensure scalable and reliable business operations.`
- **Competency Sub-themes (Rendered as interactive metadata pills):**  
  `SAP / ERP Fundamentals` · `Enterprise Data Structures` · `Business Process Integration` · `SAP Development Fundamentals`
- **Pill / Badge:**  
  `● ENTERPRISE SYSTEMS · PROCESS INTEGRATION & ERP`

---

### Beat 4: K12 — Solution Consulting (Synthesis & Delivery)
- **Beat ID:** `beat-k12`
- **Scroll Trigger Range:** Scene 03 Local $p_{\text{local}} \in [0.74, 1.00]$
- **Eyebrow:** `COMPETENCY 03 / SOLUTION CONSULTING`
- **Headline:** `Turning Business Requirements into <span class="highlight">Practical Solutions.</span>`
- **Body Copy:**  
  `Translating customer discovery into viable solution roadmaps, aligning multi-disciplinary stakeholders, and validating technical feasibility at every stage.`
- **Competency Sub-themes (Rendered as interactive metadata pills):**  
  `Customer Discovery` · `Solution Mapping` · `Technical Feasibility` · `Stakeholder Communication`
- **Pill / Badge:**  
  `● SOLUTION CONSULTING · DISCOVERY & VALUE MAPPING`

---

## 3. Typography & Styling Specification

### 3.1 Typeface Tokens
- **Headlines:** `Manrope`, 600–700 weight, letter-spacing `-0.025em`, line-height `1.15`.
- **Eyebrows & Metadata:** `IBM Plex Mono` or `Inter`, 500 weight, uppercase, letter-spacing `+0.08em`, font-size `11px`.
- **Body Text:** `Inter`, 400 weight, line-height `1.6`, font-size `15px` (`14px` on mobile), color `#374151`.
- **Highlight Accent:** `color: #1D4ED8` or `#2563EB` (deep royal museum blue, matching brand accent).

### 3.2 HTML Structure Blueprint (For Milestone 03B)

```html
<!-- Scene 03 Editorial Overlay Container -->
<aside class="expertise-overlay" id="expertiseContent" aria-label="Core Expertise Narrative">
  <div class="expertise-inner">
    
    <!-- Beat 1: K09 Entrance -->
    <article class="expertise-beat" id="beat-k09" data-beat="0">
      <div class="expertise-eyebrow">03 / CORE EXPERTISE</div>
      <h2 class="expertise-headline">Where Business Meets <span class="highlight">Technology.</span></h2>
      <p class="expertise-copy">
        A synthesis of analytical rigor, enterprise system understanding, and customer-focused consulting to solve real-world organizational challenges.
      </p>
      <div class="expertise-badge">
        <span class="status-dot" aria-hidden="true"></span>
        <span>SCENE 03 / EXPERTISE ROTUNDA · GLASS &amp; LIGHT MUSEUM</span>
      </div>
    </article>

    <!-- Beat 2: K10 Business Analysis -->
    <article class="expertise-beat" id="beat-k10" data-beat="1">
      <div class="expertise-eyebrow">COMPETENCY 01 / BUSINESS ANALYSIS</div>
      <h2 class="expertise-headline">Understanding Problems <span class="highlight">Before Building Solutions.</span></h2>
      <p class="expertise-copy">
        Bridging the gap between stakeholder needs and technical execution through structured requirements elicitation, workflow modeling, and clear functional specifications.
      </p>
      <div class="competency-tags" role="list">
        <span class="tag">Requirements Gathering</span>
        <span class="tag">Business Processes</span>
        <span class="tag">As-Is / To-Be Modeling</span>
        <span class="tag">Functional Specifications</span>
        <span class="tag">UAT</span>
      </div>
      <div class="expertise-badge">
        <span class="status-dot" aria-hidden="true"></span>
        <span>BUSINESS ANALYSIS · PROCESS &amp; FUNCTIONAL SPECIFICATION</span>
      </div>
    </article>

    <!-- Additional beats K11 and K12 follow identical semantic structure -->
  </div>
</aside>
```

---

## 4. Navigation & Chapter Synchronization

- **Fixed Vertical Navigation Item:**
  ```html
  <li>
    <button type="button" class="nav-item" id="navExpertise">
      <span class="nav-num">03</span>
      <span class="nav-label">Expertise</span>
    </button>
  </li>
  ```
- **Active State Behavior:**
  When scroll enters Scene 03 range, the navigation item automatically receives `.is-active` and `aria-current="step"`, while `01 Introduction` and `02 About` transition to inactive state. Clicking `#navExpertise` scrolls directly to the K09 establishing waypoint.
- **Upcoming Sections:**
  `04 Projects`, `05 Experience`, and `06 Contact` remain labeled `UPCOMING` with `aria-disabled="true"`.