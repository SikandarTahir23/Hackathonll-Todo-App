---
id: 2
title: Create Phase II Constitution
stage: constitution
date: 2026-01-06
surface: agent
model: Qwen
feature: none
branch: main
user: Full Stack Developer
command: /sp.constitution
labels: [constitution, phase-ii, taskmastery]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

/sp.constitution Create the PHASE II CONSTITUTION for the project:

"TaskMastery – Full-Stack Todo Web Application (Hackathon II)"

BACKGROUND:
Phase I is completed and locked.
Phase II introduces a full-stack web application with authentication
and persistent storage.

PRIMARY OBJECTIVE:
Define strict governance rules for Phase II so that the system evolves
cleanly from Phase I without scope leakage or premature complexity.

PHASE II SCOPE (ALLOWED):
- Web application using Next.js 16+ (App Router)
- Professional, responsive UI
- Login & Signup (popup / modal based)
- User-specific Todo management
- Full CRUD operations on Todos
- Mark task as completed via icon
- Filtering (All / Pending / Completed)
- Persistent database storage
- REST API using Python FastAPI
- SQLModel ORM
- Neon Serverless PostgreSQL
- Better Auth for authentication

STRICTLY FORBIDDEN:
- AI logic or decision-making
- Agents, MCP, or automation
- Analytics computation
- Team collaboration logic
- Realtime sync
- Role-based access control
- Containers, Kubernetes, or cloud orchestration

REQUIRED SECTIONS (MANDATORY):
1. Purpose of Phase II
2. Phase II Scope & Boundaries
3. Allowed Technologies
4. Forbidden Technologies
5. UI & UX Governance Rules
6. Backend & API Governance Rules
7. Authentication & Security Principles
8. Data Consistency & Integrity Rules
9. Migration Rules from Phase I
10. Quality, Performance & Maintainability Standards

RULES:
- Write in professional, enforceable Markdown
- No implementation code
- No mention of future phases
- This document must be strong enough to govern an AI system

Generate the complete Phase II Constitution.

## Response snapshot

I've created the Phase II Constitution for the TaskMastery project. The constitution document includes all required sections:

1. Purpose of Phase II
2. Phase II Scope & Boundaries
3. Allowed Technologies
4. Forbidden Technologies
5. UI & UX Governance Rules
6. Backend & API Governance Rules
7. Authentication & Security Principles
8. Data Consistency & Integrity Rules
9. Migration Rules from Phase I
10. Quality, Performance & Maintainability Standards

The constitution defines the governance rules for evolving from Phase I (console-based) to Phase II (full-stack web application) with clear boundaries, technology constraints, and quality standards. It specifically addresses the tech stack requirements (Next.js 16+, FastAPI, SQLModel, Neon PostgreSQL, Better Auth) while prohibiting advanced features that would belong in future phases.

## Outcome

- ✅ Impact: Updated project constitution to govern Phase II development
- 🧪 Tests: N/A
- 📁 Files: .specify/memory/constitution.md updated
- 🔁 Next prompts: Phase II Specification, Implementation Plan, and Execution Tasks
- 🧠 Reflection: Constitution provides clear governance for AI behavior during Phase II implementation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): Standard constitution creation
- Next experiment (smallest change to try): Begin Phase II Specification based on new constitution