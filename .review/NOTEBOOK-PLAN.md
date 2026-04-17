# Notebook Program — Agent-Owned Execution Plan

**Date:** 2026-04-17
**Status:** Complete
**Owner:** GitHub Copilot
**Scope:** Take the eight companion notebooks from runnable drafts to honest, pedagogy-first companions for the book.

This file is the working source of truth for notebook execution, fidelity, CI coverage, and manuscript alignment. The top-level `.review/ACTION-PLAN.md` retains only the executive summary for this phase.

---

## Mission

For each notebook, do one of three things and say which one was done:

1. promote it to a **faithful worked example**;
2. keep it as a **toy demonstration** that teaches the right idea honestly; or
3. frame it as a **pipeline illustration** when its value is structural rather than algorithmically faithful.

The failure mode to avoid is not merely broken execution. It is a notebook that runs but teaches the wrong thing, overclaims what it computes, or silently disagrees with the manuscript.

The code standard here is teaching clarity, not production abstraction. If a reusable layer would make the mechanism harder for a student to see, the notebook should stay more explicit.

---

## Autonomy

GitHub Copilot owns this program end to end:

- notebook edits;
- CI and smoke-test coverage;
- truth-in-labelling fixes;
- notebook/manuscript consistency work when the change is local and non-architectural; and
- ongoing status updates in this file.

### Escalate only if

- a notebook fix requires changing a chapter title;
- a worked example must be removed rather than repaired;
- a chapter promise has to be materially weakened; or
- the book's central application-first claim would need to change.

---

## Verified baseline

- The live Quokka response format is normalised across all eight notebooks.
- The repo has a smoke runner at `scripts/notebook_smoke_test.py`.
- GitHub Pages CI runs the notebook smoke suite before the site build.
- The static site build requires `HOST=127.0.0.1` during `jupyter-book build --html`.
- All eight notebooks currently pass runtime smoke tests locally.

This baseline proves runtime reliability only. It does **not** prove that the notebooks are yet honest, faithful, or quantitatively defensible.

---

## Operating doctrine

- Prefer truth over ambition.
- Prefer pedagogy over polish.
- Prefer honest relabelling over fake fidelity.
- Rewrite only when relabelling would leave the chapter underpowered or misleading.
- A notebook that merely runs is still red if it teaches the wrong algorithmic story.
- Any notebook that supports a quantitative manuscript claim must eventually carry at least one semantic assertion, not just a runtime check.
- Keep Quokka-facing code local and inspectable unless abstraction removes only accidental plumbing.

---

## Notebook classes

- **Faithful worked example**: the notebook implements the stated algorithm closely enough to support the surrounding prose and quantitative claims.
- **Toy demonstration**: the notebook simplifies or compiles away major machinery, but says so explicitly and still teaches the right intuition.
- **Pipeline illustration**: the notebook demonstrates workflow structure, embedding, or decomposition rather than a faithful end-to-end algorithm.

---

## Quality gates

Every notebook must clear these gates in order:

1. **Runtime gate**: it executes successfully against current environment and Quokka assumptions.
2. **Framing gate**: the title, opening cells, and surrounding manuscript make the same claim.
3. **Algorithm gate**: the notebook class is explicit and defensible.
4. **Semantic gate**: where quantitative claims are made, there is at least one assertion that would fail on a numerically wrong output.
5. **CI gate**: the notebook remains covered by the automated smoke path.

---

## Status language

- **Red**: runnable or not, it is still misleading, quantitatively wrong, or structurally dishonest.
- **Amber**: runtime is stable and the notebook is useful, but framing, mapping, links, or quantitative trust still need work.
- **Green**: classified, tested, manuscript-aligned, and ready to be treated as stable teaching material.

---

## Program board

| Notebook | Runtime | Program state | Current diagnosis | Preferred end state | Next action |
|----------|---------|---------------|-------------------|---------------------|-------------|
| `01-logistics.ipynb` | passing | Green | explicit faithful worked example with the exact depth-1 triangle MaxCut parameters and semantic smoke coverage for optimal-state dominance | `Faithful worked example` | locked unless later expanded to a larger still-truthful routing micro-instance |
| `02-cryptography.ipynb` | passing | Green | rewritten as an honest compiled period-finding toy for the $N = 15$, $a = 7$ example | `Toy demonstration` | locked unless later promoted to genuine modular-exponentiation period finding |
| `03-drug-discovery.ipynb` | passing | Green | rewritten as an honest single-geometry H2 VQE anatomy demo with direct XX and YY measurements and an exact-diagonalisation benchmark for the reduced model | `Toy demonstration` | locked unless later promoted to a full geometry-dependent chemistry pipeline |
| `04-machine-learning.ipynb` | passing | Green | explicit faithful worked example with kernel-behavior semantic checks and corrected manuscript navigation | `Faithful worked example` | locked unless later expanded with a stronger or larger benchmark task |
| `05-finance.ipynb` | passing | Green | rewritten as an honest classical-pricing notebook plus compiled toy QAE phase readout for exercise probability | `Toy demonstration` | locked unless later promoted to full payoff-encoding amplitude estimation |
| `06-supply-chains.ipynb` | passing | Green | rewritten as an honest 2-nurse, 2-shift QUBO micro-example with an exact Ising map and tuned one-layer QAOA | `Toy demonstration` | locked unless later promoted to a larger but still truthful scheduling instance |
| `07-materials-science.ipynb` | passing | Green | rewritten as an honest compiled phase-readout notebook anchored to the 2-site Hubbard benchmark | `Toy demonstration` | locked unless later promoted to faithful controlled-time-evolution Hubbard simulation |
| `08-climate-energy.ipynb` | passing | Green | reframed as an honest embedding-pipeline illustration with one direct-measurement embedded VQE solve step and semantic smoke bounds | `Pipeline illustration` | locked unless later promoted to a real embedding front end with self-consistency |

---

## Execution order

### Priority 0 — complete

1. Shared execution adapter
2. Smoke runner
3. CI integration
4. Static-build host fix

### Priority 1 — high-risk truth repairs

1. `07-materials-science.ipynb`
2. `05-finance.ipynb`
3. `02-cryptography.ipynb`

### Priority 2 — mathematical and framing repairs

4. `06-supply-chains.ipynb`
5. `03-drug-discovery.ipynb`
6. `08-climate-energy.ipynb`

### Priority 3 — promotion to locked companions

7. `01-logistics.ipynb`
8. `04-machine-learning.ipynb`

### Priority 4 — hardening

9. Notebook link and navigation sweep
10. Add semantic assertions to the smoke suite wherever a notebook carries quantitative argumentative weight

---

## Definition of done for one notebook

- The notebook title and opening cell tell the truth about scope.
- The surrounding manuscript makes the same claim as the notebook.
- The notebook passes the CI smoke test.
- Links, next steps, and chapter references are current.
- The notebook class is explicit: `faithful worked example`, `toy demonstration`, or `pipeline illustration`.
- If the notebook supports a quantitative claim, `scripts/notebook_smoke_test.py` contains at least one semantic assertion that would fail on an obviously wrong output.
- The notebook can be described in one sentence without hedging or apology.

---

## Completion criteria for the whole program

- Each notebook has one explicit, honest class.
- Every notebook passes CI smoke tests and the site build.
- The manuscript never overstates what its companion notebook computes.
- The three high-risk notebooks (`02`, `05`, `07`) are no longer ambiguous, numerically misleading, or structurally dishonest.
- Notebook status can be reported as green without relying on "runs on my machine" language or hidden caveats.

---

## Completion note

All eight notebooks are now classified, manuscript-aligned, and covered by semantic smoke assertions where they carry quantitative claims.

The final full smoke run passed across `01` through `08`, so this plan can be treated as closed unless later notebook work reopens it intentionally.
