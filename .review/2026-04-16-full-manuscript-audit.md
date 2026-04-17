# Full Manuscript Audit — Reader Experience Review

**Date:** 2026-04-16
**Scope:** All chapters except 00-preface.md and 01-logistics.md (previously reviewed)
**Criteria:** (1) Ungrounded jargon, (2) Name-dropping without intuition, (3) Difficulty jumps, (4) CEO-reader clarity, (5) Grad-student calibration
**Severity:** **(A)** Will lose readers, **(B)** Friction but recoverable, **(C)** Polish

---

## 02-building-qaoa.md (Deep-Dive 1)

This is the strongest deep-dive in the book. Gate-by-gate construction is exemplary. Very few issues.

### (C) L31 — "tensor product" introduced without a sentence of English
> "the combined state is the tensor product"

The math follows immediately and is self-explanatory from context, but the term "tensor product" lands without grounding. One clause would fix it: "the tensor product — simply multiplying the individual states together as independent systems —".

### (C) L101 — "Bloch sphere" dropped without explanation
> "$R_X(\theta)$ rotates the qubit's state around the X axis of the Bloch sphere"

Bloch sphere hasn't been introduced yet (it appears again in 08-quantum-kernels.md where it's explained). Either cut the reference or add a one-line gloss: "the Bloch sphere is a geometric picture of a qubit's state — the poles are $|0\rangle$ and $|1\rangle$, the equator is superposition."

### (C) L159 — "tree tensor network methods" name-dropped
> "the tree tensor network methods described in the Reality Check compute"

This reaches backward to Unit 1's Reality Check. If the reader hasn't read Unit 1 recently, this is opaque. Low-priority since it's the final paragraph.

---

## 03-cryptography.md (Unit 2)

Excellent chapter overall. The Hook is one of the book's best. A few places where the math leaps ahead of the reader.

### (B) L55–60 — Shor's 1994 paper does two things — the sentence is 90 words
> "Shor's algorithm doesn't just threaten RSA. His 1994 paper actually contains *two* quantum algorithms..."

This paragraph is a dense info-dump. It piles ECC, Roetteler et al. resource estimates, and logical-vs-physical qubit foreshadowing into one breath. The CEO reader loses the thread. The grad student doesn't need all of it yet.

**Suggestion:** Move the Roetteler ECC estimate to the Reality Check where it's more at home. Keep the Hook focused on RSA; mention ECC vulnerability in a single clause.

### (B) L82 — "General Number Field Sieve" appears and is never explained
> "the best classical algorithms are still *sub-exponential*"

"GNFS" is used again in the Bottleneck with a formula but still no intuitive explanation of what it does. The CEO doesn't know what "algebraic number theory" means. Consider: "The GNFS finds relationships between numbers that, combined cleverly, reveal factors — but even that cleverness can't escape sub-exponential scaling."

### (C) L99 — gcd defined inline but "Euler's totient" is implicit
> "decryption requires a key derived from $(p-1)(q-1)$"

The phrase "the count of integers less than $N$ that share no factor with $N$" is a parenthetical that describes Euler's totient without naming it. This is actually good pedagogy — but "(p-1)(q-1)" comes *before* the gloss, so the reader hits the formula before the English. Swap order.

### (B) L119–122 — "continued fractions algorithm" introduced as a black box
> "Use the **continued fractions algorithm** — a classical method that finds the simplest fraction $j/r$ close to $k / 2^n$ — to extract $r$"

This is the right level of gloss for the Unit chapter, but the phrase appears three times across Units 2 and Deep-Dive 2 and is never built up intuitively. A one-sentence example — "For instance, 0.74999... is close to 3/4, and the continued fractions algorithm finds that 4 is the denominator" — would ground it for the CEO reader without slowing down the grad student.

### (C) L175 — "harvest now, decrypt later" is industry jargon
The phrase is explained well in context. Just noting that without the surrounding sentence, it would be opaque. As written, it's fine.

---

## 04-inside-shors.md (Deep-Dive 2)

The best pedagogical writing in the book. Phase kickback, the |−⟩ trick, and the Deutsch-Jozsa pattern are masterfully built. One structural issue and a few jargon items.

### (B) L71–80 — The |−⟩ trick derivation is beautiful, but the "eigenvalue" generalization is abrupt
> "the phase encodes the *eigenvalue* of the oracle operator. (An eigenvalue is the factor by which an operator scales a particular state...)"

The parenthetical definition is good, but the jump from "(-1)^{f(x)}" (concrete, tangible) to "eigenvalue of the oracle operator" (abstract, general) is a difficulty jump. The grad student is fine; the advanced-hobbyist reader who made it through the |−⟩ trick will stumble.

**Suggestion:** Add a bridge sentence: "This is just a more general version of what we saw: instead of ±1, the phase can be *any* complex number of magnitude 1. That number is called the eigenvalue."

### (C) L97 — "Bernstein-Vazirani" and "Simon's algorithm" name-dropped
> "Bernstein-Vazirani extends this... Simon's algorithm goes further..."

These are acknowledged as stepping stones and explicitly deferred ("we won't detail them here"). This is correct editorial judgment. The names serve as breadcrumbs for the grad student without creating obligations. No change needed.

### (C) L143 — "NISQ" abbreviation appears for the first time
> "far too deep for today's noisy hardware (sometimes called NISQ — Noisy Intermediate-Scale Quantum)"

Well-handled parenthetical definition. No issue.

### (A) L168 — "Uncomputation" and "garbage entanglement" introduced without enough context
> "any scratch work must be run backwards after use. Leftover scratch qubits become entangled with the result — called *garbage entanglement* — which ruins interference."

For the CEO reader (who shouldn't be here — it's a deep dive), this is fine. But even for the grad student, "garbage entanglement ruins interference" is an assertion without mechanism. One sentence explaining *why* leftover entanglement ruins things would help: "If scratch qubits are still entangled with the answer, measuring the answer effectively measures the scratch too — collapsing the superposition and destroying the interference pattern we need."

### (C) L174 — "Toffoli gates" defined well
> "a Toffoli flips a target qubit only when *two* control qubits are both $|1\rangle$, making it the quantum AND gate"

Good inline definition.

---

## 05-drug-discovery.md (Unit 3)

Solid chapter. Previously audited in session. Noting remaining issues:

### (B) L14–17 — Three pieces of jargon in quick succession
> "**Schrödinger equation** — the fundamental law... **orbital** — a quantum state describing... **spin-orbital** adds the electron's spin"

Each term has an inline definition, which is good. But three bolded terms in one paragraph is a wall of new vocabulary. The CEO reader may experience definitional fatigue.

**Suggestion:** Spread across two paragraphs. Give the Schrödinger equation its own beat before introducing orbitals.

### (B) L20 — "Hilbert space" first appears here
> "This space of all possible quantum states is called a **Hilbert space**"

Good placement — grounded by the concrete dimensionality calculation. But it's worth noting this term recurs heavily in Unit 4 (ML). The definition here is "space of all possible quantum states." In Unit 4 it's used as "feature space." A reader who skipped Unit 3 and jumped to Unit 4 would miss the definition.

### (C) L48 — "mean-field" used twice before it's properly explained
It's defined at the Hartree-Fock row of the table: "Each electron moves in the average field of all others." But the term "mean-field" itself first appeared in the Hook, line 20 area. Minor — the definition-before-use gap is small.

---

## 06-vqe-pipeline.md (Deep-Dive 3)

Previously audited. Noting one new observation:

### (B) L46–50 — Anticommutation relation is a difficulty jump
> "$\{a_i, a_j^\dagger\} \equiv a_i a_j^\dagger + a_j^\dagger a_i = \delta_{ij}$"

The curly-brace notation and Kronecker delta are introduced, but the *significance* of anticommutation vs. commutation isn't made visceral. The paragraph says "this is the mathematical expression of the Pauli exclusion principle" — but a reader who doesn't already know what anticommutation means won't get the connection from the formula alone.

**Suggestion:** Add a concrete before-and-after: "If you create electron A then electron B, you get state $|\psi\rangle$. If you create B then A, you get $-|\psi\rangle$. That minus sign is the entire difference between matter and light."

### (C) L93 — "h.c." introduced late relative to its first use
"h.c." is used in the UCCSD ansatz formula and defined only in the line after: "Here 'h.c.' stands for **Hermitian conjugate**". This works, but it's a speed bump. Consider inlining the definition at first use.

---

## 07-machine-learning.md (Unit 4)

The most self-aware chapter in the book, and rightly so. The Reality Check is honest to a fault. One significant reader-experience issue.

### (A) L24–30 — "kernel trick" is explained, but "SVM" is assumed knowledge
> "Support Vector Machines (SVMs) powerful: an SVM finds the boundary that maximises the *margin*"

The margin concept is glossed parenthetically, but "SVM" itself is introduced as a known quantity. For the CEO reader, this is the most important concept in the chapter — it's the *classifier* — and it deserves a one-sentence standalone explanation before the kernel discussion. Something like: "An SVM is a classical machine learning algorithm that finds the best dividing line between two categories — think of drawing a straight line on a scatter plot that separates red dots from blue dots, positioned to be as far as possible from both groups."

### (B) L66–70 — "dequantisation" is used without definition
> "Tang (2019) showed that several claimed quantum ML speedups... can be matched classically"

"Dequantisation" is used in the Bottleneck section. The concept is clear from context (classical algorithms matching quantum ones), but the term itself is jargon. Add "(a process called **dequantisation** — finding classical algorithms that match quantum ones)".

### (C) L88 — "Born machine" introduced well
> "A **Born machine** treats the measurement probability distribution of a parameterised circuit as the model's output distribution"

Clear, good.

### (B) L92 — "barren plateaus" mentioned without mechanism
> "faces barren plateau problems at scale"

This is the second mention (first in Unit 3). The Unit 3 definition — "regions of parameter space where the energy landscape is exponentially flat" — is good. But in Unit 4, "barren plateau" is used as if the reader remembers it. A brief reminder clause would help.

---

## 08-quantum-kernels.md (Deep-Dive 4)

Clean and well-structured. The ZZ feature map explanation is particularly good — it explicitly connects to the ZZ gate from Deep-Dive 1.

### (C) L10 — "Bloch sphere" defined here
> "A single qubit lives on the **Bloch sphere** — a 2D surface parameterised by two angles"

This is the first *definition* of the Bloch sphere, but it was *used* without definition in Deep-Dive 1 (L101 of 02-building-qaoa.md). Suggests the Bloch sphere should either be defined in DD1 or cut from DD1 and saved for here.

### (C) L40 — "cross-validation" defined well inline
Good parenthetical: "(testing the trained model on held-out data to estimate real-world accuracy)".

---

## 09-finance.md (Unit 5)

Strong Hook. The $1/\sqrt{N}$ framing is the chapter's backbone and works well. One significant structural issue.

### (A) L37–55 — Grover's algorithm introduced as a "subroutine" but with insufficient scaffolding
> "**amplitude amplification**, which is Grover's search algorithm generalised."

The section "Amplitude amplification: Grover as a subroutine" introduces Grover's search, the Grover iterator, the rotation geometry, and amplitude estimation all in ~30 lines. This is the densest passage in the book. The CEO reader is lost by paragraph 2. The grad student is being asked to absorb four new concepts at conference-paper speed.

**Suggestion:** This passage needs decompression. The key insight — "the *angle* θ encodes M/N" — is the whole point. Everything before it is scaffolding that could be gentler. Consider: (1) state the punchline first ("Grover's algorithm rotates a quantum state toward good answers; amplitude estimation measures the rotation speed"), (2) *then* explain the rotation, (3) *then* define the angle.

### (B) L52–54 — QPE invoked before the reader has seen it in depth
> "QAE does exactly this. It uses the same controlled-powers-plus-inverse-QFT pattern we built in Deep-Dive 2"

This assumes the reader has read Deep-Dive 2. Unit readers who skipped the deep dives will see "controlled-powers-plus-inverse-QFT pattern" as alphabet soup. The parenthetical "(that pattern is called **Quantum Phase Estimation**, or QPE)" helps, but the Unit chapter should be self-contained enough that a reader can follow the *logic* without having built the circuit.

**Suggestion:** Instead of describing QPE mechanically, describe it by *function*: "QPE is a quantum subroutine that measures the rotation speed of a quantum operation — how fast it turns the state around. For Grover, that rotation speed encodes the fraction of good answers."

### (C) L62 — "log-normal distribution" glossed well
> "stock prices are modelled so that their logarithm follows a normal distribution, ensuring prices can't go negative"

Good.

---

## 10-amplitude-estimation.md (Deep-Dive 5)

Well-built. The geometric Grover picture is clear.

### (B) L26–33 — The "outer product" / "bra" explanation is a difficulty spike
> "$|s\rangle\langle s|$ is an **outer product** — it produces an operator (a matrix), not a number. Applied to any state $|\psi\rangle$, it gives... The notation $\langle s|$ is called a **bra**..."

This is three new concepts (outer product, projection, bra notation) crammed into one parenthetical inside the diffusion operator explanation. The grad student is fine. The advanced hobbyist is overwhelmed.

**Suggestion:** Either (a) move the bra/outer-product definition to a callout box or (b) strip it down to: "$2|s\rangle\langle s| - I$ reflects about the initial state $|s\rangle$ — it flips the amplitude of every state around the mean." The formal definition can go in a footnote or "Math Aside" box.

### (C) L62 — Table comparing classical and quantum convergence is excellent
The convergence table is the clearest "why this matters" display in the book.

---

## 11-supply-chains.md (Unit 6)

Strong Hook. The NHS £3B figure is visceral. The QUBO introduction is well-paced.

### (B) L44–50 — "QUBO" introduced without grounding the acronym's meaning
> "**Quadratic Unconstrained Binary Optimisation** (QUBO)"

The name is expanded, but each word deserves a beat: "Quadratic" (costs depend on pairs of decisions), "Unconstrained" (constraints are absorbed into the cost — we'll show how), "Binary" (yes/no decisions), "Optimisation" (find the best). The CEO would benefit from this one-line unpacking.

### (B) L60–65 — "Ising Hamiltonian" transition is too fast
> "The substitution $x_i = \frac{1 - Z_i}{2}$ converts each binary variable (0 or 1) to a spin variable (+1 or −1)"

This is correct but mechanical. The CEO reader doesn't know why we're substituting. One sentence of motivation: "This substitution translates the scheduling cost function into the language of physics — specifically, the language of interacting magnets (spins) — which is exactly what a quantum computer manipulates natively."

### (A) L72–85 — Quantum annealing's adiabatic theorem is under-explained for the CEO reader
> "The **adiabatic theorem** guarantees: if you change the Hamiltonian slowly enough (large T), the system stays in the ground state throughout"

The adiabatic theorem is stated but the reader has no physical intuition for *why* it's true. The parenthetical gloss "(it continuously adapts to the changing energy landscape rather than getting excited)" is good but not enough.

**Suggestion:** Add an analogy: "Imagine slowly tilting a bowl with a marble in it. If you tilt slowly enough, the marble stays at the bottom — it continuously adjusts to the changing slope. Tilt too fast, and it sloshes up the sides. The adiabatic theorem is the quantum version: change the energy landscape slowly, and the system stays in its lowest-energy state."

### (C) L93 — "simulated annealing" explained well
> "explores the energy landscape by making random local moves — flip one variable and check if the cost improves. It occasionally accepts *worse* moves (uphill steps)..."

Good scaffolding for the tunnelling comparison.

---

## 12-qubo-engineering.md (Deep-Dive 6)

Practical and well-structured. The penalty-term construction is the most "hands-on engineering" content in the book.

### (B) L30–40 — Inequality constraint handling has a hidden difficulty jump
> "penalise every possible group of 4... This penalty is zero when the nurse works 3 or fewer shifts"

The math is correct and the approach is explained, but the jump from "here's the concept" to "there's a problem: it's a product of four variables, QUBO only allows products of two" is abrupt. The reader needs to understand *why* QUBO is limited to quadratic terms before being told it is.

**Suggestion:** Insert one sentence before: "QUBO stands for Quadratic — meaning the cost function can multiply at most two variables together. This keeps the problem tractable and maps cleanly to two-body interactions between qubits. But some constraints naturally involve three or more variables..."

### (C) L52 — "transverse field" defined well inline
> "a **transverse field** $\sum_i X_i$ — an $X$ operator on every qubit — whose ground state is $|+\rangle^n$"

Good.

### (C) L60 — "spectral gap" introduced without a physical picture
> "the minimum spectral gap — the smallest energy difference between the ground state and the first excited state"

The definition is correct but clinical. Consider: "Think of it as the clearance between the marble and the rim of the bowl during the tilt — if the bowl gets nearly flat at any point, the marble can easily slosh out of the bottom."

---

## 13-materials-science.md (Unit 7)

The Hook is excellent — room-temperature superconductors are genuinely exciting. The Hubbard model introduction is clean.

### (B) L26–30 — The Hubbard Hamiltonian appears with a lot of notation at once
> "$H = -t \sum_{\langle i,j \rangle, \sigma} (c_{i\sigma}^\dagger c_{j\sigma} + \text{h.c.}) + U \sum_i n_{i\uparrow} n_{i\downarrow}$"

Each piece is defined, but there are four notational conventions in one equation ($\langle i,j \rangle$, h.c., $n_{i\sigma}$, $c_{i\sigma}^\dagger$). The reader who followed Deep-Dive 3 knows creation/annihilation operators. The reader who skipped deep dives is overwhelmed.

**Suggestion:** Before the equation, say: "Don't worry about the notation — we'll unpack every symbol. The equation says two things: electrons hop between neighboring atoms (first term), and two electrons on the same atom repel each other (second term). That's it."

### (C) L40 — "sign problem" explained well
> "the antisymmetry of the fermionic wavefunction causes Monte Carlo sampling to produce catastrophic cancellations"

Good link back to the fermion sign from Unit 3.

### (B) L49 — "DMRG" introduced with "matrix product state" jargon
> "**DMRG (Density Matrix Renormalization Group)** — an approach that represents the wavefunction as a chain of tensors (a **matrix product state**)"

Two new terms in one parenthetical. "Matrix product state" is never used again in the book. Either cut it or give it one clause of intuition: "a compressed representation that works well when correlations are short-range."

### (C) L64 — "Trotterisation" previewed clearly
> "the **Trotter-Suzuki decomposition**"

Well-introduced.

### (B) L72–75 — T-gate parenthetical is dense
> "A **T-gate** is a specific rotation gate that, together with the Clifford gates, enables universal quantum computation. T-gates are the most expensive operation in fault-tolerant computing because they require resource-intensive distillation procedures"

Two new concepts (Clifford gates, distillation) introduced parenthetically. The CEO doesn't need either. The grad student might want more.

**Suggestion:** Simplify to: "T-gates are the most expensive operation in fault-tolerant quantum computing — think of them as the premium fuel that powers the hardest calculations. They're expensive because they require a resource-intensive manufacturing process called distillation." Cut "Clifford gates" — it's not used elsewhere.

---

## 14-qpe-trotter.md (Deep-Dive 7)

Structurally sound. The "where we are" inventory at the top is the best chapter opening in the deep-dive series.

### (C) L8–12 — Opening paragraph is excellent
> "Let's take stock of what we already have..."

This is the ideal deep-dive opening. Every other deep dive should aspire to this.

### (B) L60–70 — Trotter error analysis is a difficulty jump
> "The error is $O(L^2 t^2 \Delta t)$... error drops to $O(L^3 t^3 \Delta t^2)$"

The error formulas are stated without intuition. What does $L^2 t^2 \Delta t$ *mean*? "More terms in the Hamiltonian (L), longer simulation time (t), and larger time steps (Δt) all increase the error." One sentence like this would ground the formulas.

### (B) L99–110 — Qubitization section is a name-drop gauntlet
> "**qubitization** (Low and Chuang, 2019) avoids Trotter error entirely by encoding the Hamiltonian as a *block* of a larger unitary — a technique called a **block encoding**... **quantum signal processing** (QSP) and **quantum singular value transformation** (QSVT)"

Four new terms (qubitization, block encoding, QSP, QSVT) in one section, none built up intuitively. This section reads like a literature review rather than pedagogy. The reader who made it through Trotterisation has earned an explanation of *why* qubitization is better, not just *that* it exists.

**Suggestion:** Either (a) expand this into a proper subsection with an analogy (Trotter is like approximating a curve with straight-line segments; qubitization traces the exact curve), or (b) demote it to a Chef's Notes bullet with a pointer to the papers. As written, it's in an uncanny valley — too detailed to skim, too sparse to teach.

---

## 15-climate-energy.md (Unit 8)

The capstone. The Hook is strong. The "full pipeline" framing works well.

### (B) L26–30 — "d-orbitals" jargon cluster
> "transition metals with partially filled **d-orbitals** — the outermost electron orbitals of metals like iron and copper"

The inline definition is fine, but "d-orbitals" appear again in the active space section. The CEO reader needs to know *why* d-orbitals are special, not just *what* they are.

**Suggestion:** Add: "These d-orbitals are special because they're close enough in energy that electrons constantly shuffle between them — creating exactly the kind of strong correlation that classical methods can't handle."

### (B) L38–42 — "open-shell" and "multi-reference" hit together
> "**open-shell** systems (molecules with unpaired electrons) and **multi-reference** states (systems where no single electron arrangement dominates)"

Two pieces of chemistry jargon in one clause. The definitions are good individually, but together they feel like a glossary dump. The CEO reader doesn't need both. Consider cutting "open-shell" and keeping only "multi-reference," which is the more important concept for the narrative.

### (C) L57 — Pipeline figure reference
> "Every step in this pipeline has been introduced in an earlier unit."

Excellent capstone framing. Works well.

### (B) L64–66 — "tapering" used with minimal explanation
> "After encoding and tapering, this requires ~12–16 qubits"

Tapering was mentioned in Unit 3's Reality Check and briefly in Deep-Dive 3, but never explained mechanistically. By Unit 8 it's doing real work (reducing 16 orbitals → 12 qubits). A one-line reminder: "(tapering exploits symmetries — like electron count and spin — to eliminate redundant qubits)" would help.

---

## 16-quantum-embedding.md (Deep-Dive 8)

Short and well-focused. The DMET procedure is clear.

### (B) L20–25 — "density matrix" definition is tucked inside the DMET procedure
> "a mathematical object that describes the quantum state of a system in terms of probabilities and correlations (a generalisation of the outer product $|\psi\rangle\langle\psi|$ from Deep-Dive 5, extended to handle statistical mixtures of states)"

The parenthetical is long and references Deep-Dive 5. For a reader who skipped that deep dive, "outer product" is not grounded. Consider simplifying: "a mathematical summary of the quantum state — like a blurry photograph that captures the statistical behavior without tracking every detail."

### (C) L28 — "CASSCF" abbreviation
> "CASSCF — Complete Active Space Self-Consistent Field, a classical method that optimises both orbitals and electron configurations within a small active space"

Good inline expansion. The abbreviation soup is unavoidable in quantum chemistry; the definition mitigates it.

### (C) L32 — "Entropy-based selection" is clean
> "Compute the single-orbital entropy from an approximate wavefunction. High-entropy orbitals are strongly correlated."

Clear and actionable.

---

## 17a-error-correction.md

This standalone chapter is remarkably clean. The analogy-first approach works well.

### (B) L12 — "Bloch sphere" used as known
> "A qubit's state is a point on the Bloch sphere — a continuous value, not a discrete one."

By this point in the book, the Bloch sphere has been mentioned in DD1, defined in DD4, and used in Unit 4. A reader who's read linearly knows it. But a reader who jumped to this chapter (which is plausible — it's a standalone topic) doesn't have it.

**Suggestion:** Add: "(the geometric representation of a qubit's state, introduced in Deep-Dive 4)".

### (C) L35–40 — Surface code explanation is well-paced
The "2D grid, distance $d$, threshold 1%" structure is clear and doesn't over-explain.

### (B) L42–45 — "LDPC codes" section is too brief relative to its importance
> "Quantum LDPC codes... encode more logical qubits per physical qubit"

Given that Pinnacle (LDPC-based) is cited in Units 2, 7, and 8, LDPC codes deserve 2–3 more sentences explaining *why* they're better. Currently the section says "more efficient" and "need longer-range connectivity" — but not *why* they're more efficient.

**Suggestion:** Add: "The key advantage: LDPC codes can protect logical qubits with a constant overhead — roughly the same number of physical qubits per logical qubit regardless of how many logical qubits you have. Surface codes' overhead grows with the computation size."

### (C) L55 — Error mitigation techniques are well-listed
Zero-noise extrapolation, probabilistic error cancellation, symmetry verification — each gets a one-line explanation. Good density for a survey section.

---

## 17-conclusion.md

### (C) L1–5 — Opening is strong
> "We started with a UPS driver and 20 stops. We end with a catalyst and 50 orbitals."

Excellent bookend. The three-act "encode, interfere, measure" unification is the right closing insight.

### (B) L14–16 — "Unknown" section could be stronger
> "Whether QAOA will beat classical optimisation at scale. Whether quantum kernels will find natural datasets..."

This is a list of open questions, but it reads like a disclaimer. The book's honesty policy has been a strength throughout. Here at the end, the honesty should feel *confident*, not defensive. Consider: "These aren't failures of quantum computing — they're active research frontiers. The theory permits advantage; the experiments haven't yet delivered it. That gap is where the field lives."

### (C) L20–23 — "The one thing to remember" is perfect
> "quantum computing is not about parallelism... It's about **interference**"

This is the best single paragraph in the book. Do not change it.

### (C) L30+ — Annotated bibliography is excellent
Each paper gets a one-line annotation explaining why it matters. This is the right format. No issues.

---

## Cross-Cutting Issues

### (A) Bloch sphere — defined too late
Used without definition in DD1 (L101), defined in DD4 (L10), referenced in error-correction chapter. Move the definition to DD1 or Unit 1, since it's a foundational visual tool.

### (B) "Barren plateaus" — defined once, used three times
Defined in Unit 3, used again in Unit 4 and DD3 without reminder. Add a parenthetical reminder at second use.

### (B) "Tapering" — used in four chapters, never properly explained
Mentioned in Unit 3 Reality Check, DD3, Unit 8, and DD8. Never gets more than a clause. Deserves either a callout box in DD3 or a "Math Aside" in Unit 3.

### (C) Chapter numbering in cross-references
DD8 references "Chapters 2 → 4 → 6 → 8 → 10 → 12 → 14 → 16" — these are file numbers, not chapter labels. If the published book uses different numbering, all cross-references need updating. Worth a pass once the final structure is set.

### (B) Consistent treatment of "grad student vs. CEO" across deep dives
DD7 (QPE/Trotter) opens with a beautiful "where we are" inventory. Other deep dives (DD5, DD6) jump straight into formalism. Recommend adding a 2–3 sentence "what you need" recap to every deep dive opening. DD1, DD2, DD3, DD4, and DD8 already have this. DD5, DD6, and DD7 are inconsistent — DD7 has an excellent version, DD5 and DD6 have them but shorter.
