# Production Plan — The Best Version of the Book

**Date:** 2026-04-17  
**Status:** Live plan  
**Scope:** Take the manuscript from a reviewed draft to a publishable web-first, print-capable book.

Historical note: this file previously tracked the T0 / T0.5 / T1 / T2 review backlog. That review work is now captured in the addenda to `.review/2026-04-16-correctness-audit.md`. This file is now the forward-looking production plan.

---

## North Star

Ship **The Problem With Quantum** as a book for smart non-specialists that is:

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

**Goal:** stop architectural churn before line-editing and figure production.

### Decisions to lock

- Confirm the current title/subtitle in `myst.yml`: **The Problem With Quantum** / **What quantum computers are really for**.
- Confirm that the website is the source-of-truth reading experience, with the PDF treated as a polished derivative.
- Confirm whether `manuscript/17-error-correction.md` remains a numbered late-book chapter or moves to appendix status.
- Freeze the current table of contents as represented in `myst.yml` and mirrored in `README.md`.

### Deliverables

- Finalised front matter and table of contents.
- No outstanding chapter-order or appendix-placement questions.
- `myst.yml` and `README.md` describing the same book object.

### Exit criteria

- No more chapter renumbering.
- No more moving chapters between main body and appendix without an explicit re-scope decision.

---

## Phase 2 — Final Editorial Pass

**Goal:** make the manuscript read like one book written with one pedagogical contract.

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

### Exit criteria

- A reader can skim the figures and recover the book's structure.
- No chapter depends on an imagined figure that does not exist.

---

## Phase 4 — Notebook and Worked-Example Integrity

**Goal:** make the notebooks worthy companions rather than aspirational props.

### Global tasks

- Standardise the notebook execution environment and dependency story.
- Re-run every notebook end-to-end.
- Check that every worked example in prose matches the actual notebook scope, simplifications, and outputs.
- Label toy constructions honestly when they are intuition builders rather than faithful implementations.

### Current triage

| Notebook | Status | Production action |
|----------|--------|-------------------|
| `01-logistics.ipynb` | strong pedagogical demo | repair and validate |
| `02-cryptography.ipynb` | internally inconsistent toy period-finding demo | rewrite or sharply reframe |
| `03-drug-discovery.ipynb` | useful VQE anatomy demo, currently overclaims | relabel and repair |
| `04-machine-learning.ipynb` | strong conceptual fit | repair and validate |
| `05-finance.ipynb` | title overpromises relative to implementation | rewrite or relabel |
| `06-supply-chains.ipynb` | good conceptually, math needs tightening | repair the mapping and narrow the claim |
| `07-materials-science.ipynb` | core quantitative story currently too fragile | rewrite |
| `08-climate-energy.ipynb` | good capstone structure, still inherits simplifications | relabel and repair |

### Repair order

1. Shared notebook execution and API assumptions
2. `07-materials-science.ipynb`
3. `05-finance.ipynb`
4. `02-cryptography.ipynb`
5. `06-supply-chains.ipynb`
6. `03-drug-discovery.ipynb`
7. `08-climate-energy.ipynb`
8. `01-logistics.ipynb`
9. `04-machine-learning.ipynb`

### Exit criteria

- Each notebook has an honest label: faithful worked example, toy demonstration, or pipeline illustration.
- The surrounding manuscript says exactly the same thing.

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

## Suggested Four-Week Execution Window

### Week 1

- Freeze structure.
- Complete the anchor editorial pass on the preface, Unit 4, Deep Dive 8, and the conclusion.
- Build the figure inventory.
- Finalise notebook triage.

### Week 2

- Complete the manuscript-wide editorial pass.
- Run the citation and quantitative-claim sweep.
- Start figure production from the now-stable text.

### Week 3

- Finish figures.
- Repair or relabel notebooks in priority order.
- Run full site/PDF builds and capture production issues.

### Week 4

- Send to external readers.
- Triage feedback into RC issues only.
- Cut the release candidate.

---

## Immediate Next Moves

1. Lock the current title/subtitle, TOC, and `17-error-correction` placement.
2. Start the final editorial pass with the preface, Unit 4, Deep Dive 8, and the conclusion.
3. Create the figure inventory before producing any art.
4. Triage the notebooks as a production risk, not an afterthought.
5. Treat the website as the primary artifact and the PDF as a derivative that must still read cleanly.

## Anti-Churn Rules

- Do not reopen solved correctness issues unless new evidence appears.
- Do not keep rewriting chapters that already satisfy the book's contract.
- Do not let notebook ambition outrun what the book can honestly support.
- Do not postpone figure work until the very end.
- Do not ask external readers for vague impressions; ask them for points of friction.
