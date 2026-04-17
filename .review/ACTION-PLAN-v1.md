# Synthesised Action Plan — All Four Reviews

**Date:** 2026-04-17
**Sources:** Gemini 3.1 Pro Preview, GPT 5.4 XHigh, Opus 4.6 1M, Full Manuscript Audit
**Purpose:** Ranked, actionable edit list the author can execute in a single working session

---

## Reviewer Key

| Short name | File |
|------------|------|
| **Gemini** | `2026-04-16-Gemini-3.1-Pro-Preview.md` |
| **GPT** | `2026-04-16-GPT-5.4-XHigh.md` |
| **Opus** | `2026-04-16-Opus-4.6-1M-High.md` |
| **Audit** | `2026-04-16-full-manuscript-audit.md` |

---

## A. Consensus Issues — Flagged by 2+ reviewers, same diagnosis

### A-1. Name-dropping without intuition (manuscript-wide)

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| Gemini | ✓ (Finding 1) | High |
| GPT | ✓ (Finding 4) | High |
| Opus | ✓ (A2, A3, B4, B6) | A/B |
| Audit | ✓ (multiple per-chapter) | A/B |

**Diagnosis:** All four reviewers agree. Algorithm names, author names, and framework names are dropped faster than intuition can absorb them. Worst offenders: Unit 1 Reality Check, DD2 (Deutsch-Jozsa/Bernstein-Vazirani/Simon list), DD7 (qubitization/QSP/QSVT), Unit 3 Crypto Reality Check.

**Reviewers agree on fix:** Name a thing only if the next paragraph uses it to sharpen the reader's mental model. Otherwise move to Chef's Notes/bibliography.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `01-logistics.md` | Reality Check: strip to 4 paragraphs (low depth, high depth, hardware gap, barren plateaus). Move Basso, Farhi, Jordan, DQI+BP, tree tensor networks, Walsh-Hadamard to Chef's Notes. | 30 min |
| `01-logistics.md` | Hook: cut "Branch-and-bound, genetic algorithms, simulated annealing, Lin-Kernighan" → "a toolkit of sophisticated heuristics — from simulated annealing to specialised graph algorithms" | 5 min |
| `03-cryptography.md` | Reality Check: move author names (Gidney/Ekerå, Webster et al., Kim/Jang) to parenthetical or footnotes. Keep the *results* inline. | 15 min |
| `04-inside-shors.md` | Cut the 5-algorithm list ("Deutsch-Jozsa, Bernstein-Vazirani, Simon's algorithm, Grover's search, and Shor's algorithm all use phase kickback") → "Several quantum algorithms — from Deutsch-Jozsa to Shor — all use phase kickback." Cut adder genealogy (Draper/Cuccaro/Gidney) → "efficient quantum adder circuits exist." | 15 min |
| `14-qpe-trotter.md` | Qubitization section: either expand with one concrete analogy (Trotter ≈ straight-line segments; qubitization ≈ tracing the exact curve) OR demote to a 1-paragraph Chef's Notes pointer. Current middle ground teaches nothing. | 30 min |

---

### A-2. Unit/Deep-Dive boundary too porous

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| GPT | ✓ (Finding 1 — top priority) | High |
| Opus | ✓ (implicit across B-notes) | B |
| Gemini | ✓ (concepts introduced but not explained) | Medium |
| Audit | ✓ (implicit across chapters) | B |

**Diagnosis:** Unit chapters leak gate-level and operator-level detail that belongs in the paired deep dive. This undermines both paths: the CEO reader hits circuit formalism, and the deep-dive reader gets repetition instead of new depth.

**Worst offenders:** `01-logistics.md` (ket notation, Pauli-Z table, teleportation circuit, gate glossary), `03-cryptography.md` (QFT formula, phase kickback mechanism), `13-materials-science.md` (creation operators, h.c., T-gates).

**Recommended rule (GPT's "Decision 1"):** If a concept needs notation, a truth table, a circuit decomposition, or operator identity, the default home is the Deep Dive. Exception: one mechanism per Unit chapter if the intuition collapses without it.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `01-logistics.md` | Move the teleportation circuit, Pauli-Z truth table, and gate glossary to DD1 or cut. Keep ket notation (needed minimally) and the QAOA loop description. | 45 min |
| `03-cryptography.md` | Move QFT formula and collapse-to-periodic-superposition mechanism to DD2. Keep the *function* of QFT ("it reads the period from the phases") but not the formula. | 30 min |
| `13-materials-science.md` | Move $c_{i\sigma}^\dagger$, h.c., and T-gate/distillation detail to DD7. Keep the Hubbard model *in words* (hopping + repulsion) and the resource estimate headline. | 30 min |

---

### A-3. Terminology creep — too many new terms per paragraph

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| Gemini | ✓ (Finding 3) | High |
| GPT | ✓ (Finding 5) | High |
| Opus | ✓ (implicit, multiple B-notes) | B |
| Audit | ✓ (per-chapter instances) | B |

**Diagnosis:** All four agree. Paragraphs often carry 3+ new terms with parenthetical definitions. Each definition is fine individually; together they create a glossary dump. GPT's heuristic: "one new technical label per paragraph is safe; three is rarely safe."

**Worst offenders:** Unit 3 Hook (Schrödinger/orbital/spin-orbital in one paragraph), Unit 4 throughout (kernel/SVM/margin/Hilbert/Born rule/dequantisation), Unit 7 Hubbard Hamiltonian (4 notational conventions in one equation), Unit 8 Bottleneck (d-orbitals/π orbitals/open-shell/multi-reference).

**Specific fix — Gemini's period/order and $U_f$ naming issues:**
- Gemini alone flagged these, but the diagnosis is correct. "Period" and "order" for the same $r$ adds friction. $U_f$ is called circuit/unitary/oracle/operator across chapters 3–4. Pick one label per context and stick to it.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `05-drug-discovery.md` | Split the Schrödinger/orbital/spin-orbital paragraph into two. Give Schrödinger its own beat. | 10 min |
| `07-machine-learning.md` | Add a standalone 2-sentence SVM explanation before the kernel discussion. Reduce jargon density in the Bottleneck section. | 20 min |
| `13-materials-science.md` | Build to the Hubbard equation in stages: hopping term first (words + formula), then interaction term (words + formula), then combine. | 20 min |
| `15-climate-energy.md` | Consolidate d-orbital/open-shell/multi-reference cluster → "The electrons in the catalyst's active site are strongly correlated." Move orbital labels to DD8. | 15 min |
| `03-cryptography.md` + `04-inside-shors.md` | Standardise: use "period" everywhere in running text; note once that mathematicians call it "order." Pick "oracle" for $U_f$ in Unit chapters, "unitary" in Deep Dives. | 20 min |

---

### A-4. Unit 5 (Finance): Grover + QAE compressed too tightly

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| Opus | ✓ (A1 — densest passage in book) | A |
| Audit | ✓ (A severity, L37–55) | A |
| GPT | ✓ (implicit — worked examples thin) | Medium |

**Diagnosis:** ~30 lines introduce Grover's search, the Grover iterator, rotation geometry, and amplitude estimation. Both Opus and Audit call this the densest passage in the book. The CEO reader is lost by paragraph 2.

**Reviewers agree on fix:** State the punchline first ("Grover rotates toward good answers; QAE measures the rotation speed"), then explain the rotation, then define the angle. Expand geometric picture from DD5 into the Unit.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `09-finance.md` | Restructure the Quantum Angle: (1) punchline, (2) rotation intuition, (3) angle → fraction, (4) QAE described by function not mechanism. Roughly double the passage length. | 45 min |

---

### A-5. Bloch sphere used before defined

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| Opus | ✓ (A4) | A |
| Audit | ✓ (cross-cutting) | A |
| Gemini | ✓ (Unit 17a) | Medium |

**Diagnosis:** Used without definition in DD1 (L101). First defined in DD4 (L10). Referenced in 17a.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `02-building-qaoa.md` | Add one-sentence definition at first use: "A single qubit's state can be visualised as a point on a sphere — the **Bloch sphere** — where $\|0\rangle$ is the north pole, $\|1\rangle$ is the south pole, and superpositions live on the surface." | 5 min |

---

### A-6. Reality Checks read like literature dumps

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| Gemini | ✓ (Units 2, 3) | High |
| GPT | ✓ (Finding 7) | High |
| Opus | ✓ (A3, B1) | A/B |

**Diagnosis:** Three reviewers agree. Reality Checks are the book's best feature (GPT, Opus), but several read like mini-literature-reviews. The CEO needs: (1) best classical baseline, (2) best quantum claim, (3) main blocker, (4) resource estimate. Everything else is supporting detail.

**Action:** Already covered in A-1 (Unit 1 and Unit 3 Reality Checks). Apply the same 4-sentence template to all Reality Checks as a consistency pass. Estimated additional effort: 1 hour across remaining chapters.

---

### A-7. Worked examples thin in Units 4–8

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| GPT | ✓ (Finding 2) | High |
| Opus | ✓ (B3, structural note) | B |
| Audit | ✓ (various chapters) | B |

**Diagnosis:** Units 4–8 average ~1,700 words vs ~3,400 for Units 1–3. The worked examples in later units are pointers to notebooks rather than in-chapter intuition builders.

**GPT's 5-beat worked example template:** (1) toy instance, (2) classical view, (3) quantum encoding, (4) algorithm output, (5) meaning back in application domain. Good template.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `07-machine-learning.md` | Add a concrete result from the notebook (decision boundary, accuracy) to the chapter text. | 20 min |
| `09-finance.md` | Already has numbers; mainly needs decompression (see A-4). | (covered) |
| `11-supply-chains.md` | Add one explicit penalty term construction to the worked example. | 20 min |
| `13-materials-science.md` | Ground the Mott insulator transition with one sentence of physical intuition. | 10 min |

---

### A-8. Machine learning pair is the weakest in the book

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| GPT | ✓ (Finding 9) | High |
| Opus | ✓ (B3) | B |
| Audit | ✓ (SVM assumed knowledge) | A |

**Diagnosis:** Unit 4 starts with Netflix but never cashes it out into a concrete "here's the geometric failure." DD4 is too compressed for the abstraction level.

**Additional bug (GPT):** Unit 4 contains a SPEC.md reference in reader-facing prose. Must be removed.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `07-machine-learning.md` | (1) Add standalone SVM explanation. (2) Remove SPEC.md reference. (3) Add concrete notebook result. (4) Reduce jargon density. | 45 min |
| `08-quantum-kernels.md` | Expand with one more concrete example or reduce scope. | 30 min |

---

### A-9. 17a error-correction chapter: structural placement

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| GPT | ✓ (Finding 10) | Medium |
| Opus | implicit | — |

**Diagnosis:** "17a" after the conclusion muddies the architecture. The content is excellent (GPT calls it one of the best chapters). The issue is placement.

**Fix options (ranked):**
1. Move before conclusion as a practical interlude
2. Rename as appendix
3. Leave as-is but reframe in the conclusion's forward-pointer

**Action:** This is a structural decision for John. Flag it but don't execute unilaterally.

---

### A-10. Unit 6 (Supply Chains): adiabatic theorem under-explained

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| Audit | ✓ (A severity) | A |
| Opus | ✓ (C6 — marble analogy) | C |

**Diagnosis:** The adiabatic theorem is stated but the reader has no physical intuition for why it works. Both reviewers suggest the same analogy: marble in a tilted bowl.

**Action:**

| File | What to do | Effort |
|------|-----------|--------|
| `11-supply-chains.md` | Add marble-in-bowl analogy before the adiabatic theorem statement. | 10 min |

---

### A-11. "Barren plateaus" and "tapering" — inconsistent definitions across chapters

| Reviewer | Flagged? | Severity |
|----------|----------|----------|
| Opus | ✓ (B9, B10) | B |
| Audit | ✓ (cross-cutting) | B |

**Action:**

| Term | Fix | Effort |
|------|-----|--------|
| Barren plateaus | Define at first use (Unit 1 or Unit 3). Add parenthetical reminder at each subsequent use. | 15 min |
| Tapering | Add consistent parenthetical "(exploiting symmetries to reduce qubit count)" at every use. | 10 min |

---

## B. Single-Reviewer Issues Worth Addressing

### B-1. Teleportation circuit in Unit 1 — introduced, never returned to
**Source:** Opus (C4)
**Assessment:** Valid. Text says "we'll return to teleportation in later units" — but doesn't. Either cut the forward reference or cut the circuit (it's already flagged for boundary-crossing in A-2).
**Action:** Remove forward reference when executing A-2 on Unit 1. **5 min.**

### B-2. "Interference machine" framing should appear earlier
**Source:** Opus (C5)
**Assessment:** Valid. The conclusion's thesis ("every quantum algorithm is an interference machine") is the best sentence in the book. Previewing it in Unit 1's interference box would give the reader a through-line.
**Action:** Add a callout in `01-logistics.md` interference section: "This is the pattern we'll see in every chapter: encode the problem, let interference amplify the right answer, measure." **10 min.**

### B-3. Garbage entanglement in DD2 — one more sentence needed
**Source:** Audit (A severity in DD2)
**Assessment:** Valid. "Garbage entanglement ruins interference" is an assertion without mechanism. One sentence fixes it: "If scratch qubits are still entangled with the answer, measuring the answer effectively measures the scratch too — collapsing the superposition and destroying the interference pattern."
**Action:** Add to `04-inside-shors.md`. **5 min.**

### B-4. Anticommutation in DD3 — needs a concrete before-and-after
**Source:** Audit (B severity)
**Assessment:** Valid. "Create A then B → $|\psi\rangle$. Create B then A → $-|\psi\rangle$. That minus sign is the entire difference between matter and light." Elegant fix.
**Action:** Add to `06-vqe-pipeline.md`. **5 min.**

### B-5. Deep-dive openings inconsistent
**Source:** Audit (B severity, cross-cutting)
**Assessment:** Valid. DD7's "where we are" inventory is the model. DD5 and DD6 are thinner. Adding a 2–3 sentence "what you need" recap to DD5 and DD6 openings would unify the reader experience.
**Action:** Add short recaps to `10-amplitude-estimation.md` and `12-qubo-engineering.md`. **15 min.**

### B-6. $\sigma$ overloading in Unit 5
**Source:** Opus (C8)
**Assessment:** Minor but valid. Standard deviation and volatility use the same symbol. Add one clause: "Volatility $\sigma$ — itself a standard deviation of returns — governs the width of the distribution."
**Action:** `09-finance.md`, one clause. **5 min.**

### B-7. "Cost landscape" metaphor used before grounded in Unit 1
**Source:** Opus (C1)
**Assessment:** Valid. One sentence: "Imagine a mountainous terrain where altitude represents cost and you're trying to find the lowest valley."
**Action:** `01-logistics.md`. **5 min.**

### B-8. LDPC codes section in 17a too brief
**Source:** Audit (B severity)
**Assessment:** Valid. Pinnacle (LDPC-based) is cited in Units 2, 7, 8. LDPC deserves 2–3 more sentences on *why* it's better (constant overhead vs. growing overhead for surface codes).
**Action:** `17a-error-correction.md`. **10 min.**

### B-9. "QUBO" acronym needs unpacking for CEO
**Source:** Audit (B severity)
**Assessment:** Valid. Each word of "Quadratic Unconstrained Binary Optimisation" deserves a beat. One line.
**Action:** `11-supply-chains.md`. **5 min.**

### B-10. Continued fractions — never grounded with an example
**Source:** Audit (B severity in `03-cryptography.md`)
**Assessment:** Valid. One-sentence example: "For instance, 0.74999… is close to 3/4, and the algorithm finds that 4 is the denominator."
**Action:** `03-cryptography.md`. **5 min.**

---

## C. Disagreements

### C-1. Bernstein-Vazirani / Simon in DD2: keep, cut, or expand?

| Reviewer | Position |
|----------|----------|
| Gemini | Cut or don't name |
| GPT | Adds cognitive load |
| Opus | Cut to unnamed description or add one-sentence descriptions |
| Audit | Current treatment is correct editorial judgment — no change needed |

**Assessment:** The Audit is closest to right. The current text names them, explicitly defers ("we won't detail them here"), and uses them as breadcrumbs. This is fine for the grad-student reader. No change needed. The names are low-friction as written because expectations are managed.

### C-2. Chemistry hierarchy table in Unit 3 — cut rows?

| Reviewer | Position |
|----------|----------|
| Opus | Reduce to 3 rows (HF, CCSD(T), Full CI) |
| Audit | Not flagged |
| GPT | Not specifically flagged |

**Assessment:** The table is useful and well-constructed. Cutting rows loses the "ladder of approximation" pedagogy. Better fix: add a "you are here" annotation or bold the row the chapter focuses on. **No cutting.**

### C-3. CRYSTALS-Kyber / CRYSTALS-Dilithium in Unit 2

| Reviewer | Position |
|----------|----------|
| Gemini | Overkill for executives |
| Others | Not flagged |

**Assessment:** These are the actual NIST post-quantum standards. A CEO doing a migration needs these names. Keep them but consider shortening: "the new standards (CRYSTALS-Kyber for encryption, CRYSTALS-Dilithium for signatures)" — one clause, not a paragraph.

---

## D. Dismiss

### D-1. Gemini's suggestion to cut all classical heuristics except simulated annealing
Too aggressive. Opus's fix ("a toolkit of sophisticated heuristics") is better and was adopted in A-1.

### D-2. Any suggestion to restructure the Unit/DD pairing architecture
The dual-path design works. The fix is boundary discipline (A-2), not reorganisation.

### D-3. Gemini's concern about "entanglement as a plot device" in Unit 2
The Unit chapter should *not* explain how entanglement locks states together — that's DD territory. The current one-liner is appropriate for the Unit lane.

### D-4. GPT's suggestion that Unit chapters should be readable in any order
The preface should be honest about light dependencies rather than promising full independence. Several units naturally build on earlier vocabulary. Retrofitting true independence would require massive duplication.

---

## Execution Order — Ranked by Impact per Hour

| Priority | Action | Files | Time |
|----------|--------|-------|------|
| 1 | Remove SPEC.md reference from ML chapter | `07-machine-learning.md` | 5 min |
| 2 | Bloch sphere definition at first use | `02-building-qaoa.md` | 5 min |
| 3 | Unit 1 Hook: replace heuristic list | `01-logistics.md` | 5 min |
| 4 | Unit 1: ground "cost landscape" metaphor | `01-logistics.md` | 5 min |
| 5 | Unit 1 Reality Check: strip to 4 paragraphs | `01-logistics.md` | 30 min |
| 6 | Unit 1: move teleportation circuit + gate glossary to DD1 or cut; remove forward reference | `01-logistics.md` | 45 min |
| 7 | Preview "interference machine" thesis in Unit 1 | `01-logistics.md` | 10 min |
| 8 | Unit 2 Reality Check: move author names to parenthetical | `03-cryptography.md` | 15 min |
| 9 | Unit 2: add continued-fractions example | `03-cryptography.md` | 5 min |
| 10 | Unit 2: move QFT formula to DD2, keep functional description | `03-cryptography.md` | 30 min |
| 11 | Standardise period/order and $U_f$ naming in crypto chapters | `03-cryptography.md`, `04-inside-shors.md` | 20 min |
| 12 | DD2: cut algorithm-bingo and adder-genealogy lists | `04-inside-shors.md` | 15 min |
| 13 | DD2: add garbage-entanglement mechanism sentence | `04-inside-shors.md` | 5 min |
| 14 | Unit 3: split Schrödinger/orbital/spin-orbital paragraph | `05-drug-discovery.md` | 10 min |
| 15 | DD3: add anticommutation concrete example | `06-vqe-pipeline.md` | 5 min |
| 16 | Unit 4: full rework (SVM explanation, remove SPEC.md ref, add notebook result, reduce jargon) | `07-machine-learning.md` | 45 min |
| 17 | DD4: expand with example or reduce scope | `08-quantum-kernels.md` | 30 min |
| 18 | Unit 5: decompress Grover/QAE passage | `09-finance.md` | 45 min |
| 19 | Unit 5: fix σ overloading | `09-finance.md` | 5 min |
| 20 | DD5 + DD6: add "where we are" opening recaps | `10-amplitude-estimation.md`, `12-qubo-engineering.md` | 15 min |
| 21 | Unit 6: add marble-in-bowl analogy for adiabatic theorem | `11-supply-chains.md` | 10 min |
| 22 | Unit 6: unpack QUBO acronym | `11-supply-chains.md` | 5 min |
| 23 | Unit 6: add explicit penalty term to worked example | `11-supply-chains.md` | 20 min |
| 24 | Unit 7: build Hubbard equation in stages | `13-materials-science.md` | 20 min |
| 25 | Unit 7: move creation operators / T-gate detail to DD7 | `13-materials-science.md` | 30 min |
| 26 | DD7: qubitization section — expand with analogy or demote to Chef's Notes | `14-qpe-trotter.md` | 30 min |
| 27 | Unit 8: consolidate chemistry jargon cluster | `15-climate-energy.md` | 15 min |
| 28 | Cross-cutting: barren plateaus — define at first use, reminder at subsequent uses | Multiple files | 15 min |
| 29 | Cross-cutting: tapering — consistent parenthetical at every use | Multiple files | 10 min |
| 30 | Reality Check template pass (apply 4-sentence structure to all) | All Unit files | 60 min |
| 31 | 17a: expand LDPC section | `17a-error-correction.md` | 10 min |
| 32 | Structural decision: 17a placement | `17a-error-correction.md` | Decision only |

**Total estimated effort:** ~10–12 hours of focused editing.

**Critical path (items 1–7, 16, 18):** ~3 hours. These fix the highest-severity issues and the ones most likely to lose readers. Everything else is friction reduction and polish.
