# Notebook Program — Agent-Owned Execution Plan

**Date:** 2026-04-17
**Status:** Active
**Owner:** GitHub Copilot
**Scope:** Take the eight companion notebooks from runnable drafts to honest, production-ready companions for the book.

This file is the working source of truth for notebook execution, fidelity, CI coverage, and manuscript alignment. The top-level `.review/ACTION-PLAN.md` retains only the executive summary for this phase.

---

## Mission

For each notebook, do one of three things and say which one was done:

1. promote it to a **faithful worked example**;
2. keep it as a **toy demonstration** that teaches the right idea honestly; or
3. frame it as a **pipeline illustration** when its value is structural rather than algorithmically faithful.

The failure mode to avoid is not merely broken execution. It is a notebook that runs but teaches the wrong thing, overclaims what it computes, or silently disagrees with the manuscript.

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
- Prefer honest relabelling over fake fidelity.
- Rewrite only when relabelling would leave the chapter underpowered or misleading.
- A notebook that merely runs is still red if it teaches the wrong algorithmic story.
- Any notebook that supports a quantitative manuscript claim must eventually carry at least one semantic assertion, not just a runtime check.

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
- **Green**: classified, tested, manuscript-aligned, and ready to be treated as production-stable.

---

## Program board

| Notebook | Runtime | Program state | Current diagnosis | Preferred end state | Next action |
|----------|---------|---------------|-------------------|---------------------|-------------|
| `01-logistics.ipynb` | passing | Amber | strong pedagogical demo; likely under-labelled rather than wrong | `Faithful worked example` | validate links and claims, then add a semantic check and lock classification |
| `02-cryptography.ipynb` | passing | Red | compiled period-finding toy with internal inconsistency | `Toy demonstration` unless a larger rewrite earns more | rewrite or sharply reframe so it stops presenting itself as faithful Shor |
| `03-drug-discovery.ipynb` | passing | Amber | useful VQE anatomy demo that overclaims geometry range and measurement fidelity | `Toy demonstration` or single-geometry `Faithful worked example` | narrow the promise or implement the missing XX/YY measurement path |
| `04-machine-learning.ipynb` | passing | Amber | conceptually strong and probably close to done | `Faithful worked example` | validate kernel behavior, links, and quantitative claims, then add semantic coverage |
| `05-finance.ipynb` | passing | Red | title and framing overpromise relative to a Grover-style toy | `Toy demonstration` unless rewritten into real amplitude estimation | rewrite or relabel so it no longer claims amplitude estimation it does not perform |
| `06-supply-chains.ipynb` | passing | Red | readable toy with untrustworthy QUBO-to-Ising mapping and scale framing | `Toy demonstration` | repair the mapping and explicitly frame it as a micro-example |
| `07-materials-science.ipynb` | passing | Green | rewritten as an honest compiled phase-readout notebook anchored to the 2-site Hubbard benchmark | `Toy demonstration` | locked unless later promoted to faithful controlled-time-evolution Hubbard simulation |
| `08-climate-energy.ipynb` | passing | Amber | strong capstone structure with inherited analytical shortcuts | `Pipeline illustration` unless missing measurement work is implemented | relabel as a pipeline demonstration and align claims with what is actually computed |

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

## Immediate queue

### Now

1. Rewrite or relabel `05-finance.ipynb` so it stops claiming amplitude estimation it does not implement.
2. Reframe `02-cryptography.ipynb` as a compiled toy or rebuild it to remove the internal inconsistency.
3. Repair the QUBO-to-Ising story in `06-supply-chains.ipynb`.

### After that

4. Narrow or deepen `03-drug-discovery.ipynb` until the VQE claims are true.
5. Lock the capstone framing for `08-climate-energy.ipynb`.
6. Promote `01-logistics.ipynb` and `04-machine-learning.ipynb` to green.
