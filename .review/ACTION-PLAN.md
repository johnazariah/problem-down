# Production Plan — The Best Version of the Book

**Date:** 2026-04-17
**Status:** Live plan. Phases 1-3 closed; Phase 4 active.
**Scope:** Take the manuscript from a reviewed draft to a publishable web-first, print-capable book.

Historical note: this file previously tracked the T0 / T0.5 / T1 / T2 review backlog. That review work is now captured in the addenda to `.review/2026-04-16-correctness-audit.md`. This file is now the forward-looking production plan.

## Current Production Snapshot

| Phase | Status | Notes |
|---|---|---|
| 1. Structure Freeze | Closed | Title/subtitle, README landing page, and conclusion now describe the same book object. |
| 2. Final Editorial Pass | Closed | The preface, Unit 4, the capstone, and the conclusion now read as one book rather than as mismatched artifacts. |
| 3. Figure Program | Closed | The mandatory figure set is in place, the inventory lives in this file, and manuscript figures now use one caption style. |
| 4. Notebook and Worked-Example Integrity | Active | The remaining live work is notebook truth-in-labelling, semantic assertions, and final alignment, tracked in `.review/NOTEBOOK-PLAN.md`. |

---

## North Star

Ship **The Quantum Bottleneck** as a book for smart non-specialists that is:

- problem-first rather than qubit-first;
- technically trustworthy and honest about current limits;
- readable straight through, not just as a set of strong isolated chapters;
- backed by notebooks that are genuinely useful companions; and
- polished enough to work as both a website and a PDF.

## Definition of Done

The book is ready for release when all of the following are true:

1. The structure is locked in `myst.yml`, `README.md`, and the manuscript itself.
2. Every chapter reads to the same editorial standard and preserves the book's zoom rhythm: wide → bottleneck → quantum → worked example → reality check.
3. Every strong quantitative claim, resource estimate, and historical assertion is cited and traceable.
4. Every notebook is either executable and prose-aligned, or explicitly labelled as a toy/demo rather than a faithful implementation.
5. The figure set is complete, stylistically coherent, and doing real explanatory work.
6. The site build and PDF build both pass a manual reading pass in output form.
7. External readers from three different audiences have done a targeted pass.
8. The remaining issue list contains no correctness, structure, or trust problems.

---

## Phase 1 — Structure Freeze

**Goal:** lock the architecture in a single decision session so all downstream work proceeds from a stable base.

**Status:** Closed on 2026-04-17.

### Decisions to lock (30-minute session)

- Confirm the current title/subtitle in `myst.yml`: **The Quantum Bottleneck** / **Real Problems and their Quantum Solutions**.
- Confirm that the website is the source-of-truth reading experience, with the PDF treated as a polished derivative.
- Confirm that `manuscript/17-error-correction.md` remains a numbered late-book chapter (recommendation: keep it — it earns its place as the foundation for every Reality Check).
- Freeze the current table of contents as represented in `myst.yml` and mirrored in `README.md`.

### Deliverables

- Finalised front matter and table of contents.
- No outstanding chapter-order or appendix-placement questions.
- `myst.yml` and `README.md` describing the same book object.
- `README.md` rewritten as a landing page that matches the preface's promise (not just a repo structure guide for contributors).

### Exit criteria

- No more chapter renumbering.
- No more moving chapters between main body and appendix without an explicit re-scope decision.

---

## Phase 2 — Final Editorial Pass

**Goal:** make the manuscript read like one book written with one pedagogical contract.

**Status:** Closed on 2026-04-17.

### Editorial rule set

For every chapter, verify the following:

- the hook starts from stakes before machinery;
- the bottleneck names the mathematical obstruction clearly;
- the quantum section introduces only the machinery that chapter earns;
- the worked example does not promise more than the notebook delivers;
- the reality check stays sober, specific, and current; and
- the handoff to the next chapter feels intentional rather than stacked on.

### Editorial order

1. `manuscript/00-preface.md`
2. `manuscript/07-machine-learning.md`
3. `manuscript/16-quantum-embedding.md`
4. `manuscript/18-conclusion.md`
5. Units 1–3 and their deep dives
6. Units 5–8 and their deep dives
7. Full-book cadence pass in output form

### Why this order

- The preface sets the promise.
- Unit 4 and Deep Dive 8 were the latest style-risk chapters and are still the most likely to drift from the house rhythm.
- The conclusion determines whether the book lands as sober synthesis rather than recap.

### Exit criteria

- No chapter feels like it belongs to a different book.
- No chapter relies on hidden prerequisites not signposted by the surrounding structure.

---

## Phase 3 — Figure Program

**Goal:** add the minimum figure set that reduces cognitive load and strengthens memory.

**Status:** Closed on 2026-04-17.

**Timing:** The figure *inventory* was created during the editorial pass and is kept in this file so the production plan and figure program do not drift apart.

### Figure principles

- Every figure must teach, not decorate.
- Captions should explain the point of the figure, not restate the title.
- Prefer recurring visual grammar across units: landscapes, pipelines, scaling plots, and circuit anatomy.

### Mandatory figure set

1. Book-level zoom-in / zoom-out framework figure for the preface.
2. QAOA cost-landscape figure for Unit 1.
3. Period-finding / Fourier-peaks figure for Unit 2.
4. Potential-energy-surface figure for Unit 3.
5. Decision-boundary or kernel-matrix figure for Unit 4.
6. Monte Carlo $1/\sqrt{N}$ vs QAE $1/N$ scaling figure for Unit 5.
7. QUBO / energy-landscape figure for Unit 6.
8. Hubbard energy / crossover figure for Unit 7.
9. Active-space / embedding pipeline figure for Unit 8.
10. One canonical circuit anatomy figure per deep dive where the circuit structure matters to understanding.

### Deliverables

- Figure inventory with one named purpose per figure.
- Final captions in a consistent style.
- All final artwork stored under `figures/`.

### Figure inventory

| Chapter | Figure file | Figure type | Teaching job |
|---|---|---|---|
| Preface | `book-zoom-rhythm.png` | workflow schematic | Make the book's wide → narrow → quantum → code → wide rhythm visible before the reader starts Unit 1. |
| Unit 1 | `cost-landscape.png` | landscape sketch | Show why local search stalls on combinatorial optimisation problems. |
| Unit 2 | `fourier-peaks.png` | frequency sketch | Make period-finding concrete by showing how a periodic support pattern becomes Fourier peaks. |
| Unit 3 | `h2-potential-energy.png` | chemistry benchmark plot | Show that molecular simulation is a curve over geometry, not a single isolated number. |
| Unit 4 | `kernel-decision-boundary.png` | comparison figure | Show why a richer feature map can make a nonlinear boundary easy. |
| Unit 5 | `qae-scaling.png` | scaling plot | Make the $1/\sqrt{N}$ versus $1/N$ convergence story visible at a glance. |
| Unit 6 | `qubo-landscape.png` | landscape schematic | Show how penalty terms create barriers and why tunnelling is the claimed annealing advantage. |
| Unit 7 | `hubbard-crossover.png` | benchmark plot | Show the crossover from delocalised to localised behaviour as $U/t$ increases. |
| Unit 8 | `climate-pipeline.png` | pipeline diagram | Show the full catalyst-screening workflow and how earlier units feed into it. |
| Deep-Dive 1 | `qaoa-full-circuit.png` | circuit anatomy | Show one complete QAOA layer at gate level. |
| Deep-Dive 2 | `qft-3qubit-circuit.png` | circuit anatomy | Show how the QFT factorises into Hadamards and controlled phase rotations. |
| Deep-Dive 3 | `h2-vqe-ansatz.png` | circuit anatomy | Show the smallest chemistry ansatz that still captures correlated behaviour. |
| Deep-Dive 4 | `kernel-circuit.png` | circuit anatomy | Show that kernel evaluation is an overlap test, not a full classifier living on the quantum chip. |
| Deep-Dive 5 | `grover-diffusion-circuit.png` | circuit anatomy | Show the oracle-plus-diffusion pattern that Grover and QAE reuse. |
| Deep-Dive 7 | `trotter-zz-interaction.png` | circuit anatomy | Show how a Hubbard interaction term decomposes into the familiar ZZ phase gadget. |
| Deep-Dive 8 | `embedding-pipeline.png` | pipeline diagram | Show exactly where the quantum fragment solve sits inside the larger embedding loop. |

### Exit criteria

- A reader can skim the figures and recover the book's structure.
- No chapter depends on an imagined figure that does not exist.

---

## Phase 4 — Notebook and Worked-Example Integrity

**Goal:** make the notebooks executable, honest about scope, and aligned with the surrounding worked examples.

**Status:** Active.

The notebook track now has its own operational source of truth in `.review/NOTEBOOK-PLAN.md`.
That separate document is agent-owned and is expected to change faster than this top-level production plan.

### Phase deliverables

- Every notebook has one explicit class: `faithful worked example`, `toy demonstration`, or `pipeline illustration`.
- Every notebook is covered by CI smoke tests and remains compatible with the site build.
- The manuscript never overstates what its companion notebook computes.

### Escalation boundary

Notebook work should only be pulled back into this main plan if it forces one of the following:

- a chapter title change;
- a worked example being removed rather than repaired;
- a material weakening of a chapter's promise; or
- a change in what the book claims quantum computers are actually for.

### Exit criteria

- `.review/NOTEBOOK-PLAN.md` can be marked complete.
- No notebook remains ambiguous, misleading, or unsupported by the manuscript.

---

## Phase 5 — Citation and Quantitative-Claim Pass

**Goal:** remove every remaining trust leak.

### Tasks

- Verify all hard numbers in hooks and reality checks.
- Verify all resource estimates and algorithm comparisons.
- Check that each cited paper needed for a major claim is archived in the repo.
- Confirm that dequantisation caveats and practical limitations are stated where they materially matter.

### Special attention areas

- cryptography resource estimates;
- finance convergence claims;
- materials-science resource counts;
- climate / embedding claims about what is already classically routine versus still aspirational.

### Exit criteria

- No strong claim feels uncited.
- No reader has to guess which paper underwrites an important number.

---

## Phase 6 — Production Polish

**Goal:** turn a strong manuscript into a finished book object.

### Tasks

- Rename GitHub repo from `problem-down` to `quantum-bottleneck` and update all internal references (manuscript, notebooks, copilot-instructions, README, conclusion).
- Build the site and PDF from the final text.
- Read the output artifacts, not just the markdown sources.
- Check navigation, headings, typography, KaTeX, links, notebook embeds, captions, and page breaks.
- Resolve build warnings and broken cross-references.
- Ensure the home page, title, subtitle, and unit labels all align.

### Exit criteria

- The website feels intentional and navigable.
- The PDF reads like a designed book, not an exported folder of chapters.

---

## Phase 7 — External Reader Passes

**Goal:** get targeted feedback from the right kinds of readers.

### Reader types

1. Domain expert in at least one application area.
2. Technical generalist who is smart but not a quantum specialist.
3. Intelligent outsider who can report where the book stops carrying them.

### Timeline

Allow **10 calendar days** for reader feedback. After that, triage what you have. Do not hold the release for a reader who hasn't responded.

### Questions to ask them

- Where did you slow down?
- What did you mistrust?
- What did you remember a day later?
- Which worked example clarified the argument, and which one did not?

### Exit criteria

- Feedback has been converted into a short RC issue list.
- No unresolved reader feedback points to a structural misunderstanding.

---

## Phase 8 — Release Candidate

**Goal:** freeze scope and ship.

### RC rules

- Only fix RC issues: broken links, stale references, bad figures, layout failures, misleading notebook framing, citation holes, and obvious sentence-level defects.
- No new topics.
- No new side quests.
- No speculative expansion once the artifact already works.

### Exit criteria

- Clean build.
- Clean issue list.
- Confidence that a first-time reader can trust the book.

---

## Suggested Three-Week Execution Window

### Week 1

- Finish the notebook program, especially the remaining amber notebooks and semantic assertions.
- Start the citation and quantitative-claim sweep.
- Build the site and PDF from the now-stable manuscript and capture output defects.

### Week 2

- Close the citation pass.
- Fix output-form issues: captions, links, navigation, notebook embeds, and PDF layout.
- Prepare the external-reader packet and questions.

### Week 3

- Send to external readers (10-day window starts).
- Triage feedback into RC issues only.
- Cut the release candidate.

---

## Immediate Next Moves

1. Finish the remaining notebook truth-in-labelling work in `.review/NOTEBOOK-PLAN.md`.
2. Run the citation and quantitative-claim sweep.
3. Build the website and PDF as production artifacts and fix what only appears in output form.
4. Prepare the external-reader pass and hold the line on release-candidate scope.

## Anti-Churn Rules

- Do not reopen solved correctness issues unless new evidence appears.
- Do not keep rewriting chapters that already satisfy the book's contract.
- Do not let notebook ambition outrun what the book can honestly support.
- Do not postpone figure work until the very end.
- Do not ask external readers for vague impressions; ask them for points of friction.
