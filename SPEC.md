# Spec: What Quantum Computers Are Actually For

> **Subtitle:** Eight problems from logistics to climate — and the algorithms that could solve them
> **Status:** Draft — all 8 units drafted
> **Author:** John Azariah
> **Date:** April 2026
> **Relation to Quokka Cookbook:** Complementary project. The Cookbook teaches *how* (circuits, QASM, quokka). This project teaches *why* (applications, industry problems, quantum advantage). The Cookbook is "Book B"; this is "Book A." They cross-reference each other.

---

## 1. Thesis

Every quantum computing resource starts with qubits, then gates, then phase kickback, and by the time readers understand the mechanics they've lost sight of *why they should care*. We invert this.

**Start with a problem people already care about. Pull in only the quantum machinery needed to solve it.**

Each unit opens with a real industry problem — a dollar figure, a bottleneck, a human cost — then zooms into the mathematical structure that makes it hard classically, shows how quantum mechanics offers a structural advantage *at precisely that bottleneck*, and zooms back out to what it means in practice.

This is the same pedagogy that made the [encodings book](../encodings-book/) work: chemistry first, then formalism, then code. Here it's: industry problem → mathematical bottleneck → quantum resolution → honest reality check.

---

## 2. Audience

| Segment | What they want | What we give them |
|---------|---------------|-------------------|
| **Software engineers** | "Should I learn quantum computing?" → a concrete answer, not hype | Real problems mapped to real algorithms, with runnable code |
| **Domain experts** (finance, pharma, logistics) | "What can quantum do for *my* field?" → specifics, not hand-waving | One chapter per domain, written for people who know the *problem* but not the *quantum* |
| **CS/physics students** | "Why does this matter outside the lab?" → applications that motivate the theory | Every algorithm introduced *in context*, with forward pointers to deeper theory |
| **Technical managers / CTOs** | "Where should I invest?" → an honest playbook | Reality Check boxes: what's possible now vs. what needs fault tolerance |

**Prerequisites:** Curiosity. Comfort reading pseudocode. High-school math (we introduce linear algebra and probability in-context, with geometric / visual intuitions, as needed).

**Non-audience:** People who want a rigorous QC textbook (point them to Nielsen & Chuang). People who want a comprehensive algorithms survey (point them to Childs' lecture notes).

---

## 3. Structure

### 3.1 Overview

The book alternates between **application chapters** (the "why") and **deep dive chapters** (the "how"). Application chapters tell the industry story — problem, bottleneck, quantum angle, worked example, reality check. Deep dive chapters teach the algorithm from first principles, building quantum concepts organically when the algorithm needs them. Readers doing the quick path read only the application chapters; readers doing the full path read everything.

```
Preface              — Why another quantum computing book?
Introduction         — The zoom-in/zoom-out framework; how to read this book

Chapter 1            — Logistics         (application: QAOA for MaxCut)
Chapter 2            — Building QAOA     (deep dive: qubits, superposition, CNOT, ZZ gate, variational loop)

Chapter 3            — Cryptography      (application: Shor's algorithm)
Chapter 4            — Inside Shor's     (deep dive: phase kickback, QFT, modular exponentiation)

Chapter 5            — Drug Discovery    (application: VQE for molecular simulation)
Chapter 6            — The VQE Pipeline  (deep dive: fermions, encodings, Pauli measurement)

Chapter 7            — Machine Learning  (application: quantum kernel estimation)
Chapter 8            — Quantum Kernels   (deep dive: feature maps, swap test, kernel matrix)

Chapter 9            — Finance           (application: quantum amplitude estimation)
Chapter 10           — Amplitude Estimation (deep dive: Grover's algorithm, QPE on Grover)

Chapter 11           — Supply Chains     (application: QUBO and quantum annealing)
Chapter 12           — QUBO Engineering  (deep dive: constraint encoding, Ising conversion, annealing)

Chapter 13           — Materials Science (application: QPE for the Hubbard model)
Chapter 14           — QPE & Trotterisation (deep dive: time evolution, Trotter error, resource estimation)

Chapter 15           — Climate & Energy  (application: catalyst design with quantum embedding)
Chapter 16           — Quantum Embedding (deep dive: active space, DMET, self-consistency)

Chapter 17           — Error Mitigation  (practical: ZNE and noise-aware computing)
Chapter 18           — Quantum Counting  (practical: QPE meets Grover)

Conclusion           — What's actually ready today; a sober roadmap
Appendix A           — The quantum toolbox (glossary of every concept, where introduced, key formula)
Appendix B           — Further reading (curated, annotated bibliography)
```

**Key design decision:** No concept is taught before it's needed. Quantum concepts (qubits, superposition, entanglement, phase kickback, QFT, etc.) are introduced *inside* the deep dive chapters, the first time the algorithm under discussion requires them. The appendix collects all concepts into a reference glossary — but nobody should start there.

**Key design decision:** Application chapters contain *no* circuit-level detail. They reference the next chapter (the deep dive) for readers who want to go deeper. Deep dive chapters are self-contained algorithm tutorials that weave in circuit concepts from the [Quokka Cookbook](https://github.com/johnazariah/quokka-cookbook) organically — the cookbook content is subsumed into the book, not cross-referenced as a separate resource.

**Key design decision:** The Quokka Cookbook repo remains as a standalone QASM reference for people running circuits on their Quokka hardware, but the book is the complete pedagogical resource. Every circuit concept taught in the cookbook is covered in a deep dive chapter, in context, with full explanation. The cookbook is a *byproduct* of the book, not a dependency.

**Key design decision: two reading paths.**

- **Application chapters are self-contained and can be read in any order.** A finance person jumps to Chapter 9, a chemist to Chapter 5. Each application chapter makes sense without any prior reading.
- **Deep dive chapters are sequential and must be read in order (2 → 4 → 6 → 8 → 10 → 12 → 14 → 16).** Each deep dive builds on concepts introduced in earlier deep dives. Chapter 2 teaches qubits and CNOT. Chapter 4 assumes those and introduces phase kickback. Chapter 6 assumes CNOT and adds fermion encodings.
- **The natural hybrid path:** a reader starts at any application chapter, gets curious, reads the paired deep dive, discovers they need a concept from an earlier deep dive, follows the dependency chain backwards. The book *pulls them in* rather than *front-loading* prerequisites.

### 3.2 Chapter detail

Each unit follows a fixed template:

#### Unit template

| Section | Purpose | Length |
|---------|---------|--------|
| **The Hook** | Open with the industry problem. Real numbers, real stakes. No quantum yet. | ~800 words |
| **The Bottleneck** | Zoom into the mathematical structure that makes this hard. Show the exponential wall or the intractability argument. | ~1000 words |
| **The Quantum Angle** | Introduce the quantum algorithm/technique that addresses *this specific bottleneck*. Build the circuit or protocol step-by-step. Introduce quantum concepts *only as needed*. | ~1500 words |
| **Worked Example** | A toy-sized but complete instance. Runnable code (Jupyter notebook). Walk through input → circuit → output → interpretation. | ~1000 words |
| **Reality Check** | Honest assessment: what's achievable on NISQ hardware today? What needs fault tolerance? When might this be practical? Cite real resource estimates. | ~500 words |
| **Chef's Notes** | Connections to other units. Deeper references. Open problems. What to try next. | ~500 words |

**Target per unit:** ~5,000–5,500 words of prose + 1 companion notebook.

**Target total:** ~50,000 words (prose) + 8 notebooks. Roughly 250 pages in print.

### 3.3 Unit breakdown

---

#### Unit 1: Logistics — *"Saving $50M one mile at a time"*

**Hook:** UPS's ORION system saves $50M/year by removing 1 mile from each driver's route. But ORION is a heuristic — the underlying TSP/VRP is NP-hard. For 50 stops, there are more possible routes than atoms in the universe.

**Bottleneck:** Combinatorial explosion. The solution space grows factorially. Classical heuristics get stuck in local minima. The cost landscape has exponentially many valleys.

**Quantum angle:** QAOA (Quantum Approximate Optimization Algorithm). Encode candidate routes as qubit strings. Construct a cost Hamiltonian whose ground state is the optimal route. Use alternating problem/mixer unitaries to explore the landscape.

**Machinery introduced:**
- Qubits as binary decision variables
- Cost Hamiltonians (how to turn "minimise this function" into "find the ground state of this operator")
- Variational quantum-classical loops
- Approximation ratios — what "good enough" means

**Worked example:** MaxCut on a 6-node graph. Build the QAOA circuit, optimise parameters classically, compare with brute-force.

**Reality check:** QAOA on near-term hardware. Barren plateaus. The debate on quantum advantage for combinatorial optimisation (Bravyi et al. 2020, Farhi & Harrow 2016). Where things stand honestly.

---

#### Unit 2: Cryptography — *"The trapdoor quantum computers can kick open"*

**Hook:** Every time you buy something online, RSA or ECC protects the transaction. The security rests on a *trapdoor*: multiplying two primes is easy; factoring their product is (classically) hard. Quantum computers break this.

**Bottleneck:** Factoring and discrete logarithm. The best classical algorithms are sub-exponential but still impractical for large keys. The hardness isn't proven — it's an assumption. Quantum mechanics violates the assumption.

**Quantum angle:** Shor's algorithm, but taught as "period-finding breaks the trapdoor" rather than as an abstract circuit:

1. Factoring reduces to period-finding (number theory — keep it intuitive)
2. Period-finding reduces to phase estimation
3. Phase estimation uses the QFT

We teach the *why* at each reduction, not just the *how*.

**Machinery introduced:**
- Superposition (first proper introduction — motivated by "we need to try all periods at once")
- Interference (how the QFT amplifies the right answer)
- Quantum Fourier Transform — as a *tool*, not a topic. Enough to understand why it extracts periods.
- Phase kickback — explained exactly once, here, when it actually matters

**Worked example:** Factor 15 with Shor's algorithm. 4 qubits. Show the full circuit, the measurement histogram, the continued-fractions post-processing.

**Reality check:** Largest number factored quantumly. Resource estimates for RSA-2048 (Gidney & Ekerå 2021). Post-quantum cryptography migration timeline.

---

#### Unit 3: Drug Discovery — *"$2 billion and 12 years per drug"*

**Hook:** The average drug takes 12 years and $2.6B to develop. 90% of candidates fail in clinical trials. The bottleneck is *molecular simulation*: predicting how a candidate molecule interacts with a protein target. Classical simulation of electron interactions scales exponentially.

**Bottleneck:** The electronic structure problem. The Hilbert space of $N$ electrons grows as $\binom{M}{N}$ where $M$ is the number of spin-orbitals. For a drug-sized molecule, this is astronomical. Classical methods (DFT, CCSD(T)) trade accuracy for tractability.

**Quantum angle:** Variational Quantum Eigensolver (VQE). Encode the molecular Hamiltonian on qubits. Use a parameterised quantum circuit (ansatz) to prepare trial wavefunctions. Measure the energy. Optimise classically. This is the *direct bridge* to the encodings book.

**Machinery introduced:**
- Fermions and the Pauli exclusion principle (why electrons aren't like qubits)
- Second quantisation (creation/annihilation operators — just enough to build a Hamiltonian)
- Fermion-to-qubit encodings (Jordan-Wigner, Bravyi-Kitaev — pointers to the encodings book for depth)
- VQE: the variational principle, ansatz design, measurement overhead

**Worked example:** Ground-state energy of H₂ at various bond lengths using VQE. Build the potential energy surface. Compare with exact diagonalisation.

**Reality check:** Largest molecules simulated quantumly. The measurement overhead problem. Error mitigation vs. error correction. Google's Hartree-Fock experiment (2020).

**Cross-reference:** Readers who want to go deep on encodings → *From Molecules to Qubits* (the encodings book).

---

#### Unit 4: Machine Learning — *"10⁸ features and counting"*

**Hook:** Modern recommendation engines and classifiers operate in absurdly high-dimensional feature spaces. Kernel methods (the mathematical engine behind SVMs) compute inner products in these spaces — but the cost scales with the dataset size and dimensionality.

**Bottleneck:** The kernel trick lets you compute in exponentially large feature spaces *implicitly*. But some useful kernels are classically intractable to evaluate. And sampling from complex probability distributions (needed for generative models) can be exponentially slow.

**Quantum angle:** Quantum kernel estimation. A quantum computer can prepare states in an exponentially large Hilbert space *naturally*. The inner product between two quantum states gives you a kernel value. If the quantum feature map has no efficient classical simulation, you get a provable advantage.

**Machinery introduced:**
- Hilbert space as a feature space (the geometric picture)
- Inner products and measurement (Born rule as a kernel evaluator)
- Quantum feature maps and data encoding
- The distinction between *heuristic* quantum ML and *provable* quantum advantage

**Worked example:** Quantum kernel classifier on a synthetic dataset. Train an SVM with a quantum kernel vs. classical RBF kernel. Visualise the decision boundary.

**Reality check:** The "does quantum ML actually help?" debate (Tang's dequantisation results, Huang et al. 2022). Where provable advantage exists vs. where it's speculative. The data loading bottleneck.

---

#### Unit 5: Finance — *"Pricing the unpriceable"*

**Hook:** Banks price complex derivatives using Monte Carlo simulation: sample millions of random market scenarios, compute the payoff for each, take the average. For exotic options, each scenario is expensive. The uncertainty shrinks as $1/\sqrt{N}$ — painfully slowly. Getting one more digit of accuracy costs 100× more samples.

**Bottleneck:** The $1/\sqrt{N}$ convergence rate of classical Monte Carlo. You can't beat it classically (it's a fundamental limit of random sampling). But you can beat it quantumly.

**Quantum angle:** Quantum Amplitude Estimation (QAE). Encode the probability distribution as a quantum state. The amplitude of a target outcome encodes the expected payoff. QAE extracts this amplitude with $1/N$ convergence — a *quadratic* speedup. Same accuracy, quadratically fewer samples.

**Machinery introduced:**
- Amplitude amplification (Grover's algorithm as a subroutine, not a standalone topic)
- Grover's search — but motivated by "I need to boost the probability of good samples"
- Quantum amplitude estimation — QPE applied to the Grover operator
- The quadratic speedup: when $\sqrt{}$ makes or breaks practicality

**Worked example:** Price a European call option using quantum amplitude estimation. Compare convergence with classical Monte Carlo (10³ vs. 10⁶ samples for same accuracy).

**Reality check:** Goldman Sachs / IBM's derivative pricing experiments. Required qubit counts for practical advantage. The depth problem on NISQ devices. Approximate QAE variants.

---

#### Unit 6: Supply Chains — *"10,000 nurses, 50 hospitals, 1 schedule"*

**Hook:** NHS spends millions on agency nurses because scheduling is so hard. Assign 10,000 nurses to shifts across 50 hospitals with constraints (qualifications, preferences, regulations, fairness). This is a *constraint satisfaction problem* — and it's NP-hard.

**Bottleneck:** Constraint satisfaction with soft and hard constraints. The feasible region is a tiny fraction of the search space. Classical solvers (simulated annealing, integer programming) struggle when constraints interact non-locally.

**Quantum angle:** QUBO (Quadratic Unconstrained Binary Optimisation) formulations and quantum annealing. Encode constraints as penalty terms in a quadratic cost function. The ground state of the corresponding Ising Hamiltonian satisfies all constraints (or violates them minimally).

**Machinery introduced:**
- QUBO formulations (how to turn "satisfy these constraints" into "minimise this quadratic function")
- Energy landscapes (the classical picture — local minima, energy barriers)
- Quantum tunnelling (why quantum annealing can escape local minima that classical annealing can't)
- The adiabatic theorem (intuitively: "go slowly enough and you stay in the ground state")
- Gate-based vs. annealing approaches

**Worked example:** Nurse scheduling for 8 nurses, 4 shifts, 2 wards. Formulate as QUBO, solve with simulated + quantum annealing, compare solutions.

**Reality check:** D-Wave's capabilities and limitations. The quantum speedup debate for annealing. Hybrid classical-quantum solvers. Where annealing fits vs. gate-based QC.

---

#### Unit 7: Materials Science — *"The room-temperature superconductor problem"*

**Hook:** A room-temperature superconductor would revolutionise energy transmission, MRI, maglev, fusion reactors. We can't design one because we can't *simulate* one: strongly correlated electron systems defeat every classical approximation method. The Hubbard model — the simplest model that captures the essential physics — is unsolved for realistic system sizes.

**Bottleneck:** Strong electron correlation. Mean-field methods (DFT) fail. Exact methods (full CI) are exponentially expensive. The sign problem makes quantum Monte Carlo unreliable for fermions. We literally cannot compute the phase diagram of the 2D Hubbard model.

**Quantum angle:** Quantum Phase Estimation (QPE). Prepare a trial state, apply controlled time evolution under the Hubbard Hamiltonian, read out the energy eigenvalue to high precision. QPE gives *exact* energies (in principle), not variational upper bounds.

**Machinery introduced:**
- QPE in full (building on the pieces introduced in earlier units: QFT from Unit 2, phase kickback from Unit 2, controlled unitaries from Unit 5)
- Hamiltonian simulation / Trotterisation (how to implement $e^{-iHt}$ as a circuit)
- Resource estimation (how many qubits and gates do we actually need?)

**Worked example:** Ground state of the 2-site Hubbard model via QPE. Sweep the $U/t$ ratio. Observe the metal-insulator transition.

**Reality check:** Resource estimates for the 2D Hubbard model (Babbush et al.). Timeline for fault-tolerant QPE. What VQE can and can't do as a stopgap. The beyond-classical frontier.

---

#### Unit 8: Climate & Energy — *"Designing a better catalyst for carbon capture"*

**Hook:** Carbon capture at scale requires better catalysts — molecules that accelerate the absorption of CO₂ from air. Designing catalysts is a *quantum chemistry* problem: you need to simulate the reaction pathway on a metal surface, including transition states and activation energies. Classical methods can't handle the accuracy-size tradeoff.

**Bottleneck:** Surface chemistry. The catalyst active site involves strongly correlated electrons (like materials science) embedded in a much larger environment (the metal surface, solvent, substrate). You need quantum accuracy for the active site and classical efficiency for everything else.

**Quantum angle:** Hybrid quantum-classical embedding methods. Use a quantum computer for the *hard part* (the active site: ~20-50 correlated orbitals) and a classical computer for the *easy part* (the environment). This is DMET, DMFT, or active-space VQE/QPE.

**Machinery introduced:**
- Active-space methods (why you don't need to simulate the whole molecule)
- Quantum embedding (DMET / active-space decomposition — how to split a problem between quantum and classical processors)
- Hybrid quantum-classical workflows at scale
- The full pipeline: molecule → Hamiltonian → encoding → circuit → measurement → energy

**Worked example:** Active-space VQE for a small catalyst model (e.g., CO on a metal cluster). Compare active-space vs. full-space, quantum vs. classical.

**Reality check:** Microsoft / PNNL nitrogen fixation estimates. The road from toy models to industrial catalyst design. What needs to happen in error correction, qubit counts, and algorithm development.

**Cross-reference:** This is the "complete pipeline" chapter — it connects back to Unit 3 (VQE), Unit 7 (QPE/Trotter), and the encodings book for the encoding step.

---

## 4. Pedagogical principles

### 4.1 The zoom-in/zoom-out structure

Every unit follows the same rhythm:

```
WIDE    →  The industry problem (everyone gets this)
  ↓
NARROW  →  The mathematical bottleneck (this is why it's hard)
  ↓
QUANTUM →  The structural advantage (this is what quantum offers)
  ↓
CODE    →  The worked example (this is how you do it)
  ↓
WIDE    →  What it means in practice (so what?)
```

This rhythm is the book's signature. Readers who internalise it will start seeing "zoom-in/zoom-out" in everything they read about quantum computing.

### 4.2 Concept introduction policy

No concept is introduced before it is needed. Every concept is introduced *in the context of a problem it solves*, inside the deep dive chapter that first requires it.

| Concept | Introduced in deep dive | Motivated by | Cookbook recipe absorbed |
|---------|------------------------|--------------|------------------------|
| Qubits, measurement | Ch 2 (QAOA) | Encoding binary decisions | Recipe 01 (Bell State) |
| Superposition, Hadamard | Ch 2 (QAOA) | Creating uniform search | — |
| CNOT, entanglement | Ch 2 (QAOA) | The ZZ gate for edge costs | Recipe 01 (Bell State) |
| Phase kickback | Ch 4 (Shor's) | Why period-finding works | Recipe 03 (Deutsch-Jozsa) |
| Oracles | Ch 4 (Shor's) | Modular exponentiation | Recipe 03 (Deutsch-Jozsa) |
| QFT | Ch 4 (Shor's) | Extracting periodicity | Recipe 09 (QFT) |
| Teleportation | Ch 4 (Shor's) | Bell measurement aside | Recipe 02 (Teleportation) |
| Hidden structure / HSP | Ch 4 (Shor's) | Shor as a special case | Recipes 04, 05 (BV, Simon's) |
| Fermions / second quantisation | Ch 6 (VQE) | Why electrons aren't qubits | — |
| Pauli decomposition, measurement bases | Ch 6 (VQE) | Measuring molecular energy | Recipe 08 (VQE for H₂) |
| Variational methods | Ch 2 (QAOA) | Optimising circuit parameters | Recipe 07 (QAOA MaxCut) |
| Grover / amplitude amplification | Ch 10 (Amp. Est.) | Boosting good samples | Recipe 06 (Grover) |
| QPE | Ch 14 (QPE+Trotter) | Exact energy extraction | Recipe 10 (QPE) |
| Trotter decomposition | Ch 14 (QPE+Trotter) | Implementing time evolution | — |
| QUBO / Ising conversion | Ch 12 (QUBO) | Encoding constraints | Recipe 07 (QAOA MaxCut) |
| Quantum embedding | Ch 16 (Embedding) | Splitting quantum/classical | — |
| Error mitigation (ZNE) | Ch 17 (Practical) | Making noisy results useful | Recipe 11 (ZNE) |
| Quantum counting | Ch 18 (Practical) | Counting without finding | Recipe 12 (Counting) |

Every cookbook recipe finds a home in a deep dive chapter. Appendix A collects all concepts into a reference glossary — but nobody should start there.

### 4.3 Honesty policy

Every unit has a **Reality Check** box. These are non-negotiable. The rules:

1. **State the current best classical algorithm** and its performance. Don't compare quantum with straw-man classical.
2. **State resource estimates** for practical quantum advantage (qubit count, gate depth, error rates). Cite specific papers.
3. **State the timeline honestly.** "Requires fault-tolerant QC" is a valid and important answer.
4. **Acknowledge dequantisation.** If a claimed quantum advantage has been partially or fully matched classically (e.g., quantum recommendation systems → Tang 2019), say so.
5. **Never promise.** Use "could", "in principle", "if error rates improve." Never "will", "soon", or "inevitably."

### 4.4 Visual language

- **Circuit diagrams** for every quantum operation (QASM-style, matching Quokka Cookbook conventions)
- **Cost landscape visualisations** (3D surfaces, energy diagrams) wherever optimisation is involved
- **Scaling plots** (log-log: problem size vs. resources) in every Reality Check
- **"Before/after" comparisons** (classical bottleneck vs. quantum resolution) as a recurring visual motif
- **Chapter colour coding:** Application chapters use **teal / dark green** (grounded, real-world). Deep dive chapters use **deep purple** (technical, algorithmic). This gives readers an instant visual signal about the kind of chapter they're in — visible in headers, running footers, and thumb indexes. In the digital edition, chapter title bars and sidebar markers alternate colours.

---

## 5. Companion materials

### 5.1 Jupyter notebooks

One notebook per unit. Self-contained, executes end-to-end. Stack:

- **Qiskit** — broadest ecosystem, IBM hardware access
- **PennyLane** — best for variational / ML units
- **OpenFermion** — for Units 3, 7, 8 (molecular Hamiltonians)
- **Quokka** — QASM circuits from the Cookbook can be referenced directly

Each notebook follows the same structure:

```python
# Unit N: [Title]
# 1. The problem (classical setup)
# 2. The quantum circuit (build it step by step)
# 3. Run it (simulator or hardware)
# 4. Interpret results (compare with classical)
```

### 5.2 Cross-references

| From this book | To | What |
|---|---|---|
| Unit 3 (Drug Discovery) | Encodings book | Deep dive on fermion-to-qubit encodings |
| Units 1, 3, 7, 8 | Quokka Cookbook | Runnable QASM recipes for key sub-circuits |
| All Reality Checks | Primary literature | Resource estimates, benchmark papers |

### 5.3 Repository structure

```
problem-down/
├── README.md
├── manuscript/
│   ├── 00-preface.md
│   ├── 00-introduction.md
│   ├── 01-logistics.md
│   ├── 02-cryptography.md
│   ├── 03-drug-discovery.md
│   ├── 04-machine-learning.md
│   ├── 05-finance.md
│   ├── 06-supply-chains.md
│   ├── 07-materials-science.md
│   ├── 08-climate-energy.md
│   ├── 09-conclusion.md
│   ├── appendix-a-toolbox.md
│   └── appendix-b-further-reading.md
├── notebooks/
│   ├── 01-logistics.ipynb
│   ├── 02-cryptography.ipynb
│   ├── ...
│   └── 08-climate-energy.ipynb
└── figures/
```

---

## 6. Format & publication strategy

### Phase 1: Blog series (months 1–8)

- Publish one unit per month as a standalone ~5,000-word blog post
- Companion Jupyter notebook on GitHub
- Host on quokka-cookbook GitHub Pages site (shared infrastructure) or separate site
- Each post stands alone — readers can enter at any unit
- Collect feedback via GitHub issues and social media
- Build an audience before committing to print

### Phase 2: Book (months 9–12)

- Expand each unit from ~5,000 to ~8,000 words (add depth, exercises, sidebars)
- Write preface, introduction, conclusion, appendices (connective tissue)
- Establish cohesive notation thread across units
- Add 2–3 exercises per unit
- Target: Springer "Quantum Science and Technology" series, or Cambridge University Press

### Phase 3: Course integration

- Units map naturally to 8 lectures in a semester course
- Notebooks become problem sets
- Quokka Cookbook recipes become lab exercises
- Chris & Simon can integrate with existing UTS quantum computing curriculum

---

## 7. Working titles (rank-ordered)

1. **Quantum Computing From the Problem Down** — clear thesis in the title
2. **Why Quantum? Eight Problems That Need a Different Computer** — accessible, specific
3. **The Quantum Advantage Playbook** — practical, business-flavoured
4. **Quantum Computing for People Who Ship Software** — strong voice, narrower audience

---

## 8. Open questions

- [ ] **Unit ordering.** Current order follows a rough "increasing quantum sophistication" arc (QAOA → Shor → VQE → kernels → QAE → annealing → QPE → embedding). Alternative: order by "closeness to practical advantage" or by "how well-known the problem is."
- [ ] **Notebook platform.** Qiskit alone, or best-tool-per-unit (PennyLane for ML, OpenFermion for chemistry)? Consistency vs. authenticity tradeoff.
- [ ] **How tightly to couple with Quokka Cookbook.** Shared site? Shared repo? Independent projects that cross-link?
- [ ] **Co-authorship.** Solo? With Chris? With Chris and Simon? The cookbook pairing with their textbook argues for collaboration, but the "problem down" book could stand alone.
- [ ] **The ML unit.** Quantum ML is the most contentious application area. Do we include it with strong caveats, or replace it with something less debatable (e.g., quantum sensing, quantum communication)?
- [ ] **Blog host.** GitHub Pages (free, version-controlled)? Substack (audience-building, email list)? Medium (discoverability)? Recommendation: GitHub Pages for long-term ownership, cross-posted to Substack for reach.
