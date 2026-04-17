# Unit 3: Drug Discovery — *$2 Billion and 12 Years Per Drug*


## The Hook

In 2020, the pharmaceutical industry spent approximately $83 billion on research and development. The average cost to bring a single new drug to market: **$2.6 billion**. The average time: **12 years**. And roughly 90% of drug candidates that enter clinical trials fail.

Why is it so expensive? The cost isn't mostly in the lab work itself. It's in the *failures*. For every drug that reaches your pharmacy shelf, hundreds of candidates were synthesised, tested, found wanting, and discarded. Many of those failures could have been predicted; if we could accurately simulate how a drug molecule interacts with its biological target.

The bottleneck is **molecular simulation**. To predict whether a candidate drug will bind to a protein target, you need to compute the electronic structure of the drug-protein complex — the arrangement of electrons that determines binding affinity, reaction rates, and molecular stability. This is a quantum mechanical calculation. The molecule doesn't know classical physics. Its electrons obey the **Schrödinger equation** — the fundamental law governing quantum systems, which relates a system's energy to the quantum states its particles can occupy — and the only way to predict the molecule's behaviour accurately is to solve that equation.

For small molecules — up to about 50 electrons — classical computers can do this well enough. **Density functional theory** (DFT) — which approximates the many-electron problem by working with the electron density rather than tracking every electron individually — handles molecules of this size in minutes. For a drug candidate docked to a protein binding site — hundreds or thousands of electrons — DFT is too inaccurate and exact methods are unaffordable.

The exponential wall is not a metaphor. Each electron in a molecule occupies an **orbital** — a quantum state describing where the electron is likely to be found and what energy it has. A **spin-orbital** adds the electron's spin (up or down), doubling the count of available states.

The full quantum state of $N$ electrons occupying $M$ orbitals lives in a space of dimension $\binom{M}{N}$ — the number of ways to choose which $N$ orbitals are occupied. This space of all possible quantum states is called a **Hilbert space**. For a modest active site — say, 30 electrons in 60 orbitals — that's $\binom{60}{30} \approx 1.2 \times 10^{17}$ dimensions. Storing a single quantum state would require more memory than any machine on Earth. No amount of classical computing power will cross this wall. The problem *is* quantum, and the solution might be too.


## The Bottleneck

Let's understand what makes molecular simulation hard; and why it's a fundamentally different kind of hardness from the combinatorial problems in Unit 1.

### The electronic structure problem

Given a molecule — its atoms and their positions — compute its **ground-state energy**: the lowest-energy arrangement of its electrons.

The ground-state energy determines everything chemists care about: whether a reaction is energetically favourable, how tightly a drug binds to a receptor, what shape a protein folds into, how strong a chemical bond is. It is arguably the single most important number in chemistry.

In the language of quantum mechanics, the ground-state energy is the smallest eigenvalue of the molecular Hamiltonian $H$. You've met Hamiltonians before: in Unit 1, we built a cost Hamiltonian for MaxCut. Here the Hamiltonian encodes real physics — all the forces between electrons and atomic nuclei — and the Schrödinger equation $H|\Psi\rangle = E|\Psi\rangle$ says that the allowed energy states are precisely the eigenvalues of $H$. The **wavefunction** $|\Psi\rangle$ is the complete quantum description of every electron in the molecule — the multi-electron generalisation of the qubit states $|\psi\rangle$ you already know.

### Why electrons aren't qubits

There's a crucial complication. Electrons are **fermions** — particles that obey the Pauli exclusion principle: no two electrons can occupy the same quantum state. This means the wavefunction must be *antisymmetric*: swapping any two electrons flips the sign of $|\Psi\rangle$. (This is why atoms have shells and chemistry exists — if electrons could pile into the same state, every atom would behave the same.)

This is different from qubits. If you swap two qubits on a quantum computer, nothing special happens — no minus sign appears. A quantum computer built from qubits doesn't natively enforce fermionic antisymmetry. To simulate electrons on qubits, you need a **fermion-to-qubit encoding** — a mathematical map that translates between the language of electrons and the language of qubits, preserving the crucial minus signs.

### The classical approximation hierarchy

Classical computational chemistry has developed a remarkable hierarchy of approximation methods:

| Method | Accuracy | Scaling | What it does |
|--------|----------|---------|-------------|
| Hartree-Fock (HF) | ~99% of total energy | $O(N^4)$ | Each electron moves in the average field of all others (no correlation) |
| DFT | Good for weak correlation | $O(N^3)$ | Works with electron density instead of the full wavefunction |
| MP2 | Perturbative correction | $O(N^5)$ | Adds a first-order correction for electron-electron interaction |
| CCSD(T) | "Gold standard" | $O(N^7)$ | Systematically accounts for how pairs (and triples) of electrons interact |
| Full CI | Exact (within basis) | $O(e^N)$ | Tries every possible electron arrangement — brute force |

The pattern: more accuracy costs exponentially more computation.

The simplest method, Hartree-Fock, treats each electron as if it moves through the average field created by all the others — a **mean-field** approximation. This ignores the fact that electrons actively dodge each other: when one electron moves left, its neighbours respond instantly. The difference between this real, correlated dance and the mean-field approximation is called **electron correlation**. Hartree-Fock misses it entirely. Each step up the ladder captures more correlation, but at drastically higher cost. Full Configuration Interaction (Full CI) is exact but exponential.

The gap between CCSD(T) (the best practical classical method, scaling as $N^7$) and Full CI (exact but exponential) is where quantum computing enters. For molecules with **strong electron correlation** — where the mean-field picture breaks down entirely, such as transition metal complexes (molecules with partially filled d-orbitals) and reaction transition states — CCSD(T) fails and Full CI is unaffordable. These are exactly the molecules that matter most for drug design.


## The Quantum Angle

A quantum computer can represent the quantum state of $N$ electrons directly, using qubits in place of orbitals. The key algorithm is the **Variational Quantum Eigensolver** (VQE); a hybrid quantum-classical algorithm for finding the ground-state energy of a molecular Hamiltonian.

### From electrons to qubits

To put a molecular problem on a quantum computer, we need to translate the language of electrons into the language of qubits. The key idea: each orbital becomes one qubit ($|1\rangle$ = occupied, $|0\rangle$ = empty), and the electron-electron interactions become a sum of Pauli operators — just like the cost Hamiltonian in QAOA, but with coefficients that come from physics instead of a graph.

The translation isn't trivial because of the fermion sign rule. Different **encodings** (Jordan-Wigner, Bravyi-Kitaev, and others) handle the minus signs differently, making different tradeoffs between qubit count and circuit depth. Deep-Dive 3 walks through the Jordan-Wigner encoding in detail; for the full story, see our companion book [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book).

After encoding, the molecular Hamiltonian becomes a weighted sum of Pauli operators — terms like $Z_0 Z_1$, $X_0 X_1$, and so on — with real-valued coefficients computed from quantum chemistry. This is the input to the quantum algorithm.

### VQE: the variational quantum eigensolver

VQE uses the **variational principle**: for any trial state $|\psi(\theta)\rangle$, the expected energy is an upper bound on the true ground-state energy. (The notation $\langle \psi | H | \psi \rangle$ means "the expected value of measuring $H$ in state $|\psi\rangle$" — the quantum analogue of a weighted average.)

$$E_0 \leq \langle \psi(\theta) | H | \psi(\theta) \rangle$$

The algorithm:

1. **Prepare a trial state** on the quantum computer using a parameterised circuit (the **ansatz** — German for "initial guess," meaning the family of trial states the circuit can reach): $|\psi(\theta)\rangle = U(\theta)|0\rangle$
2. **Measure the energy** by decomposing $H$ into a sum of Pauli operators and measuring each term. The total energy is the weighted sum of these measurements.
3. **Optimise classically**: feed the measured energy to a classical optimiser, which suggests new parameters $\theta$.
4. **Repeat** until the energy converges.

This is the same variational loop as QAOA (Unit 1); quantum circuit produces an estimate, classical optimiser updates parameters, repeat. The difference is the cost function (molecular energy instead of cut count) and the ansatz (chemistry-inspired circuits instead of alternating problem/mixer layers).

### The ansatz: encoding chemical intuition

The quality of VQE depends heavily on the ansatz; the family of quantum states the parameterised circuit can reach. Two common choices:

**UCCSD (Unitary Coupled Cluster):** inspired by the classical CCSD method. It applies single and double excitations; moving one or two electrons between orbitals; with tunable coefficients. Chemically motivated, but the circuits can be deep.

**Hardware-efficient ansätze:** generic circuits (layers of rotations and entangling gates) that are short enough to run on noisy hardware. Less chemically motivated, but feasible. The risk: they may not contain the true ground state, or they may suffer from **barren plateaus** — regions of parameter space where the energy landscape is exponentially flat, leaving the optimiser with no useful gradient to follow.

### Measurement overhead

There's a catch. The molecular Hamiltonian, after encoding, becomes a sum of many Pauli terms: $H = \sum_i c_i P_i$. For H₂ with Jordan-Wigner, there are about 15 terms. For a drug-sized molecule, there could be millions. Each term requires separate measurements, and the statistical error shrinks as $1/\sqrt{N_\text{shots}}$. This **measurement overhead** is one of the main practical challenges of VQE.


## Worked Example

Let's compute the ground-state energy of **H₂**; the hydrogen molecule; at various bond lengths, building the potential energy surface.

H₂ has 2 electrons and (in a minimal basis) 4 spin-orbitals → 4 qubits after Jordan-Wigner encoding. This is small enough to run on any quantum computer (or simulator), but large enough to show the real VQE pipeline.

### The pipeline

1. **Compute molecular integrals** ($h_{ij}$, $h_{ijkl}$) using a classical chemistry package
2. **Build the qubit Hamiltonian** via Jordan-Wigner encoding
3. **Choose an ansatz** (UCCSD or hardware-efficient)
4. **Run VQE**; optimise parameters to minimise energy
5. **Sweep the bond length** from 0.2 Å to 2.5 Å and plot the potential energy surface

The equilibrium bond length (the minimum of the potential energy curve) is where H₂ is stable. The dissociation limit (large bond length) is where it breaks into two hydrogen atoms. Getting this curve right; especially the shape near the minimum; is the test of a good quantum chemistry method.

VQE with a 4-qubit UCCSD ansatz reproduces the exact Full CI result for H₂ to **chemical accuracy** (1.6 milliHartree ≈ 1 kcal/mol — the threshold at which energy differences become chemically meaningful; the Hartree is the atomic unit of energy, roughly 27.2 eV). At the equilibrium bond length (~0.74 Å, where 1 Å = $10^{-10}$ m), the computed energy matches the exact value to several decimal places. As we stretch the bond toward dissociation, the correlation between the two electrons grows stronger, and this is precisely where VQE outperforms Hartree-Fock.

→ *The next chapter builds the full VQE pipeline — from molecular integrals to circuit to energy — and shows you the code.*

### Back to the pharmacy

We computed the energy of H₂ — the simplest molecule there is. How does this help find a \$2.6 billion drug?

The pipeline is identical for any molecule. Only two things change: the number of qubits (one per orbital) and the number of Pauli terms in the Hamiltonian (which scales as $O(M^4)$ for $M$ orbitals). H₂ needs 4 qubits and ~15 terms. Caffeine would need ~100 qubits. A drug-sized active site might require several hundred. The algorithm doesn't change — you still prepare a trial state, measure Pauli terms, optimise classically, repeat.

The practical strategy, which we'll develop fully in Unit 8, is to use a classical computer for the "easy" electrons and a quantum computer only for the strongly correlated ones in the active site. This hybrid approach is how quantum computing will likely enter the pharmaceutical pipeline — not replacing classical chemistry, but solving the hardest sub-problems that classical methods can't.


## Reality Check

**What's been demonstrated.** VQE has been run on real quantum hardware for small molecules: H₂ (2 qubits, various groups since 2014), LiH (4 qubits), BeH₂ (6 qubits), and H₂O (up to 12 qubits with **tapering** — a technique that exploits molecular symmetries to remove qubits from the Hamiltonian). Google's 2020 Hartree-Fock experiment on 12 qubits was a milestone, though it used a non-variational approach.

**The gap to drug discovery.** A drug-sized active site might require 50–100 qubits (after encoding and tapering — exploiting symmetries to reduce qubit count) and circuits with thousands or millions of gates. Current NISQ devices can handle at most ~20 qubits with meaningful accuracy. **Error mitigation** techniques (like zero-noise extrapolation, which runs circuits at artificially increased noise levels and extrapolates back to zero) help but don't close the gap for industrially relevant molecules.

**The measurement problem.** For a molecule with $M$ orbitals, the number of Pauli terms in the Hamiltonian scales as $O(M^4)$. Each term needs many measurement shots for acceptable statistics. For 100 orbitals, you might need $10^{10}$ measurements. Techniques like **classical shadow tomography** (which extracts many properties from relatively few randomised measurements) and grouping of commuting terms reduce this, but it remains a bottleneck.

**What would change the picture.** Fault-tolerant quantum computers would enable **quantum phase estimation** (Unit 7) instead of VQE; giving exact energies rather than variational upper bounds, without the measurement overhead. But QPE requires much deeper circuits and is a post-NISQ algorithm.

**What's real today:** The real near-term strategy is **active-space methods**: use a classical computer for the "easy" electrons (core, weakly correlated) and a quantum computer for the "hard" ones (strongly correlated, in the active space). This hybrid approach works for small molecules today, and we'll develop it fully for industrial-scale systems in Unit 8 (Climate & Energy).


## Chef's Notes

- **This chapter introduces the molecular Hamiltonian pattern.** In Unit 1, we encoded an optimisation objective as a cost Hamiltonian. Here we encode the *physical* Hamiltonian of a molecule. The mathematical structure is the same; a sum of Pauli operators; but the origin is different: physics rather than combinatorics.

- **VQE is QAOA's cousin.** Same variational loop, different cost function, different ansatz. If you understood the QAOA loop in Unit 1, VQE is a natural extension.

- **Fermion-to-qubit encodings are a deep topic.** We've given the 30-second version (Jordan-Wigner, Bravyi-Kitaev). For the full story; including parity encoding, ternary tree encoding, tapering, and the algebraic structure behind all of them; see our companion book: [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book).

- **H₂ is the "Hello World" of quantum chemistry.** It's the simplest molecule with a non-trivial electronic structure — small enough to verify classically, rich enough to show the full VQE pipeline, and pedagogically indispensable. Our encodings book uses H₂ throughout for the same reason.

- **The path from here to real drug discovery** runs through Unit 8 (Climate & Energy), where we'll use quantum embedding methods to handle realistic molecular sizes; computing the active-site electrons quantumly and the environment classically.

- **Further reading:**
    - Peruzzo et al. (2014). *A variational eigenvalue solver on a photonic quantum processor.* [Nature Communications 5:4213](https://doi.org/10.1038/ncomms5213) ([arXiv:1304.3061](https://arxiv.org/abs/1304.3061))
    - McArdle, Endo, Aspuru-Guzik, Benjamin, Yuan (2020). *Quantum computational chemistry.* [Reviews of Modern Physics 92:015003](https://doi.org/10.1103/RevModPhys.92.015003) ([arXiv:1808.10402](https://arxiv.org/abs/1808.10402))
    - Google AI Quantum (2020). *Hartree-Fock on a superconducting qubit quantum computer.* [Science 369:1084–1089](https://doi.org/10.1126/science.abb9811) ([arXiv:2004.04174](https://arxiv.org/abs/2004.04174))
    - Azariah et al. *From Molecules to Qubits.* [github.com/johnazariah/encodings-book](https://github.com/johnazariah/encodings-book)
    - Szabo and Ostlund (1996). *Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory.* The classical reference for computational chemistry foundations.
