# Revised Action Plan v2 — All Five Reviews + Correctness Audit

**Date:** 2026-04-17  
**Sources:** Gemini 3.1 Pro Preview, GPT 5.4 XHigh, Opus 4.6 1M, Full Manuscript Audit, Correctness Audit  
**Purpose:** Ranked, actionable edit list incorporating both readability and correctness findings

---

## Reviewer Key

| Short name | File | Type |
|------------|------|------|
| **Gemini** | `2026-04-16-Gemini-3.1-Pro-Preview.md` | Readability |
| **GPT** | `2026-04-16-GPT-5.4-XHigh.md` | Readability |
| **Opus** | `2026-04-16-Opus-4.6-1M-High.md` | Readability |
| **Audit** | `2026-04-16-full-manuscript-audit.md` | Readability |
| **Correctness** | `2026-04-16-correctness-audit.md` | Factual/Math |

---

## TIER 0 — Correctness Fixes (must fix before any readability pass)

Mathematical errors, wrong identities, or inconsistent numbers that will undermine credibility with any technically literate reader.

| ID | Issue | Files | Fix | Effort |
|----|-------|-------|-----|--------|
| **T0-1** | Finance payoff encoding conflates exceedance probability with expected payoff | `09-finance.md`, `10-amplitude-estimation.md` | Re-frame worked example as digital option / exceedance probability, OR describe payoff-encoding construction | 45 min |
| **T0-2** | Shor periodic superposition has wrong normalisation ($r$ vs $M \approx Q/r$ terms) | `03-cryptography.md` L118–122 | Fix to $1/\sqrt{M}$ with $M \approx 2^n/r$ | 10 min |
| **T0-3** | Phase kickback "catalyst" overgeneralised to multi-bit Shor oracle | `04-inside-shors.md` L104, L302 | Add clarification that output register stays entangled for multi-bit functions | 15 min |
| **T0-4** | Raising operator: "$\sigma^+|1\rangle$ leaves $|1\rangle$ unchanged" is wrong (annihilates to zero) | `06-vqe-pipeline.md` L81 | "annihilates $|1\rangle$ (gives zero — can't create electron in occupied orbital)" | 5 min |
| **T0-5** | Y-measurement basis-change identity $S^\dagger H \cdot Y \cdot HS = Z$ is wrong | `06-vqe-pipeline.md` L132–136 | Drop the identity, keep operational description (apply $S^\dagger$ then $H$, measure) | 10 min |
| **T0-6** | 2-site Hubbard "Mott transition" is a crossover, not a phase transition | `13-materials-science.md` L96–104 | Replace "transition" with "crossover" and note true transitions need larger lattices | 10 min |
| **T0-7** | Resource estimates inconsistent: Unit 7 ($8\times8$ = 400 qubits, $10^{11}$ gates) vs DD7 ($10\times10$ = 200 qubits, $10^7$ gates) | `13-materials-science.md`, `14-qpe-trotter.md` | Align DD7 with Babbush scaling, or label DD7 as per-Trotter-step count | 20 min |
| **T0-8** | Active-space qubit counting inconsistent (spatial vs spin-orbital convention) | `15-climate-energy.md`, `16-quantum-embedding.md` | Standardise: spatial orbitals in prose, explicit ×2 at encoding step | 15 min |

**T0 subtotal: ~2.5 hours**

---

## TIER 0.5 — Medium-Severity Correctness

| ID | Issue | Files | Fix | Effort |
|----|-------|-------|-----|--------|
| **T0.5-1** | Logical vs physical qubit comparison apples-to-oranges | `03-cryptography.md` | Add "(logical)" / "(physical)" labels consistently | 10 min |
| **T0.5-2** | Continued fractions count: "three of four" → "two of four" | `03-cryptography.md` | Fix count, note $k=8$ gives factor not the period itself | 10 min |
| **T0.5-3** | GNFS constant 1.923 may not match bit-length form | `03-cryptography.md` | Verify or switch to standard $\ln N$ form | 10 min |
| **T0.5-4** | "More memory than exists on Earth" overstated | `05-drug-discovery.md` | → "far beyond the memory of any single machine" | 5 min |
| **T0.5-5** | "$1/\sqrt{N}$ is a fundamental limit" too broad (ignores variance reduction) | `09-finance.md` | Narrow to "for generic black-box sampling" | 10 min |
| **T0.5-6** | "Quantum systems are built to find low-energy states" too strong for gate model | `01-logistics.md` | Soften to "provides natural machinery for exploring energy landscapes" | 5 min |
| **T0.5-7** | QAOA $p\to\infty$ convergence needs "with optimal parameters" caveat | `01-logistics.md` | Add caveat | 5 min |
| **T0.5-8** | 2D Hubbard superconductivity uncertainty overstated | `13-materials-science.md` | Reword to "remains unsettled, different methods disagree" | 5 min |
| **T0.5-9** | DMET conflated with all active-space embedding | `15-climate-energy.md` | Distinguish DMET as one specific framework | 5 min |

**T0.5 subtotal: ~1 hour**

---

## TIER 1 — High-Impact Readability Fixes

(From readability reviews — consensus or high-severity items)

| ID | Issue | Files | Reviewers | Fix | Effort |
|----|-------|-------|-----------|-----|--------|
| **T1-1** | Hook lists 4 classical heuristics cold | `01-logistics.md` | Gemini, Opus | "a toolkit of heuristics — from simulated annealing to specialised graph algorithms" | 5 min |
| **T1-2** | Bloch sphere used before defined | `02-building-qaoa.md` | Opus, Audit, Gemini | One-sentence definition at first use | 5 min |
| **T1-3** | Unit 1 Reality Check = literature dump | `01-logistics.md` | Opus, Gemini, GPT | Strip to 4 paragraphs, move detail to Chef's Notes | 30 min |
| **T1-4** | Unit 5 Grover/QAE densest passage in book | `09-finance.md` | Opus, Audit | Decompress: punchline first, rotation intuition, expand | 45 min |
| **T1-5** | Unit 4 ML weakest unit | `07-machine-learning.md` | GPT, Opus, Audit | Add SVM explanation, concrete result, reduce jargon | 45 min |
| **T1-6** | Teleportation circuit forward reference never fulfilled | `01-logistics.md` | Opus, GPT | Remove "we'll return to teleportation" | 5 min |
| **T1-7** | "Interference machine" thesis should appear in Unit 1 | `01-logistics.md` | Opus | Add to interference callout | 5 min |
| **T1-8** | Unit 7 Hubbard equation = notation dump | `13-materials-science.md` | Opus, Audit | Build in stages: hopping → interaction → combine | 20 min |

**T1 subtotal: ~2.5 hours**

---

## TIER 2 — Friction Reduction

| ID | Issue | Files | Effort |
|----|-------|-------|--------|
| T2-1 | Unit 2 Reality Check: author names to parenthetical | `03-cryptography.md` | 15 min |
| T2-2 | DD2: cut algorithm-bingo and adder-genealogy | `04-inside-shors.md` | 15 min |
| T2-3 | DD2: garbage entanglement mechanism sentence | `04-inside-shors.md` | 5 min |
| T2-4 | Unit 3: split Schrödinger/orbital paragraph | `05-drug-discovery.md` | 10 min |
| T2-5 | DD3: anticommutation concrete example | `06-vqe-pipeline.md` | 5 min |
| T2-6 | DD7: qubitization — expand with analogy or demote | `14-qpe-trotter.md` | 30 min |
| T2-7 | Unit 8: consolidate chemistry jargon cluster | `15-climate-energy.md` | 15 min |
| T2-8 | Barren plateaus: define at first use | Multiple | 15 min |
| T2-9 | Tapering: consistent parenthetical at every use | Multiple | 10 min |
| T2-10 | Unit 6: marble-in-bowl analogy for adiabatic theorem | `11-supply-chains.md` | 10 min |
| T2-11 | Unit 6: unpack QUBO acronym | `11-supply-chains.md` | 5 min |
| T2-12 | Unit 5: σ overloading note | `09-finance.md` | 5 min |
| T2-13 | Unit 1: ground "cost landscape" metaphor | `01-logistics.md` | 5 min |
| T2-14 | DD5 + DD6: "where we are" opening recaps | `10-amplitude-estimation.md`, `12-qubo-engineering.md` | 15 min |
| T2-15 | Reality Check template pass | All Unit files | 60 min |
| T2-16 | 17a: expand LDPC section | `17a-error-correction.md` | 10 min |
| T2-17 | 17a naming/placement decision | Decision for John | — |

**T2 subtotal: ~3.5 hours**

---

## Execution Summary

| Tier | Items | Est. Time | Priority |
|------|-------|-----------|----------|
| **T0 Correctness** | 8 | ~2.5 hours | **Fix first — these are wrong** |
| **T0.5 Med. Correctness** | 9 | ~1 hour | **Fix second — these are misleading** |
| **T1 Readability** | 8 | ~2.5 hours | Fix third |
| **T2 Friction** | 17 | ~3.5 hours | Fix fourth |
| **Total** | 42 | ~9.5 hours | |

**Critical path (4 hours):** All T0 items + T0.5-4 + T0.5-6 + T0.5-7 + T1-2 + T1-7. These fix every mathematical error and the most visible readability gaps.

---

## Dismissed Suggestions

| Source | Suggestion | Why dismissed |
|--------|-----------|---------------|
| Gemini | Cut all heuristics except simulated annealing | Too aggressive; Opus's softer fix adopted |
| Gemini | CRYSTALS-Kyber/Dilithium names are overkill | CEOs doing migration need these names |
| GPT | Unit chapters should be independently readable in any order | Would require massive duplication |
| Various | Restructure Unit/DD pairing architecture | Design works; fix boundary discipline instead |
| Gemini | Entanglement in Unit 2 needs deeper treatment | That's DD territory by design |
| Audit | Bernstein-Vazirani/Simon: change treatment | Current "named, explicitly deferred" is fine |
