# AGENTS.md — Project Museum Agent Workflow

This file is the operating contract for AI coding agents working in this repository, including Antigravity.

## 1. Source of truth

- Repository: `hntt2510/portfolio_ThanhTam`
- Default integration branch: `main`.
- Project style: **Glass & Light Museum**, circular entrance atrium, warm white / silver / subtle ice blue; no dark navy, cyberpunk, or excessive glow.
- One persistent Three.js world; semantic HTML for text/navigation; scroll-driven reversible camera behavior.
- Maintain already-approved visuals and previous milestone work; extend incrementally rather than rebuilding unrelated parts.
- Read `PROJECT_STATUS.md` and the relevant design handoff before changing files.

## 2. Mandatory automatic commit and push

**After EACH completed, verified unit of work or milestone, commit and push the result to GitHub automatically, without waiting for an extra user approval.** This applies to code, Blender source files, GLB assets, approved references, documentation, tests, and milestone reports.

Routine workflow:

1. Check `git status`, active branch and the latest remote commit before making changes.
2. Modify only files relevant to the current approved milestone; preserve prior approved work.
3. Run the applicable local checks and validate generated assets.
4. Update `PROJECT_STATUS.md` with a factual summary, artifact paths, verification results, known issues, and next milestone.
5. Stage the intended files; review the staged diff and ensure no secrets/private artifacts are included.
6. Commit with a meaningful milestone-specific message.
7. Push to the project's remote branch immediately; normally `origin main`, if direct push is permitted.
8. Verify that the remote commit SHA matches the pushed HEAD. Report the commit SHA and GitHub link in the final response.

**Do not add or repeat blanket instructions such as "do not push", "no GitHub writes", or "wait for approval before push" in future handoffs or task prompts.** Any earlier blanket prohibition on pushing is superseded by this file.

## 3. Safety and operational boundaries

- Automatic pushes do NOT authorize force pushes, history rewrites, deletion of protected material, secrets exposure, or disabling repository protections.
- Respect the branch protection rules, if any. If direct push is blocked, push to an allowed feature branch and create a PR where possible, then report the blocker; do not pretend `main` was updated.
- Never commit credentials, tokens, `.env` secrets, private client documents, or unapproved proprietary content.
- Preserve source editable files (`.blend`, generator scripts), runtime assets (`.glb`), and render evidence when relevant.
- If validation fails, do not call the milestone complete. Explain what failed and what was/was not pushed.
- If GitHub is unreachable or push fails, clearly disclose that the work is only local and give the exact failure; retry appropriately without discarding changes.
- All public assets, including PDF/CV files, must be intentionally approved for public exposure.

## 4. Milestone completion report

For every completion, report:
- Milestone name and status: completed / partial / blocked
- What was changed, and paths of artifacts
- Evidence: build, tests, Blender GLB inspection, browser screenshots or recordings **only if actually performed**
- Commit SHA and GitHub commit link **only if remote push was verified**
- Outstanding issues and the next recommended task

Update `PROJECT_STATUS.md` in the same commit whenever practical.

## 5. Scope sequence

- Milestone 01: Entrance Atrium initial Three.js implementation — committed.
- Milestone 01A: Blender graybox, GLB, generator and reference renders — committed; quality acceptance is separate.
- Milestone 01B: Integrate the GLB into the existing persistent Three.js world, reconcile Blender/Three.js camera coordinates, and test responsive scroll behavior — next.
- Later scenes: Profile Gallery, Expertise, three Project Exhibition chapters, Experience Corridor and Let's Connect.

Do not confuse a commit with verified visual acceptance.
