# Unit 3: Drug Discovery — *$2 Billion and 12 Years Per Drug*

---

## The Hook

In 2020, the pharmaceutical industry spent approximately $83 billion on research and development. The average cost to bring a single new drug to market: **$2.6 billion**. The average time: **12 years**. And roughly 90% of drug candidates that enter clinical trials fail.

Why is it so expensive? The cost isn't mostly in the lab work itself. It's in the *failures*. For every drug that reaches your pharmacy shelf, hundreds of candidates were synthesised, tested, found wanting, and discarded. Many of those failures could have been predicted — if we could accurately simulate how a drug molecule interacts with its biological target.

The bottleneck is **molecular simulation**. To predict whether a candidate drug will bind to a protein target, you need to compute the electronic structure of the drug-protein complex — the arrangement of electrons that determines binding affinity, reaction rates, and molecular stability. This is a quantum mechanical calculation. The molecule doesn't know classical physics. Its electrons obey the Schrödinger equation, and the only way to predict the molecule's behaviour accurately is to solve that equation.

For small molecules — up to about 50 electrons — classical computers can do this well enough. Density functional theory (DFT), the workhorse of computational chemistry, handles molecules of this size in minutes. For a drug candidate docked to a protein binding site — hundreds or thousands of electrons — DFT is too inaccurate and exact methods are unaffordable.

The exponential wall is not a metaphor. The quantum state of $N$ electrons occupying $M$ orbitals lives in a Hilbert space of dimension $\binom{M}{N}$. For a modest active site — say, 30 electrons in 60 orbitals — that's $\binom{60}{30} \approx 1.2 \times 10^{17}$ dimensions. Storing a single quantum state requires more memory than exists on Earth. No amount of classical computing power will cross this wall. The problem *is* quantum, and the solution might be too.

---

## The Bottleneck

Let's understand what makes molecular simulation hard — and why it's a fundamentally different kind of hardness from the combinatorial problems in Unit 1.

### The electronic structure problem

Given a molecule — its atoms and their positions — compute its **ground-state energy**: the lowest-energy arrangement of its electrons.

The ground-state energy determines everything chemists care about: whether a reaction is energetically favourable, how tightly a drug binds to a receptor, what shape a protein folds into, how strong a chemical bond is. It is arguably the single most important number in chemistry.

The governing equation is the Schrödinger equation:

$$H|\Psi\rangle = E|\Psi\rangle$$

where $H$ is the molecular Hamiltonian (encoding all the electron-electron and electron-nucleus interactions), $|\Psi\rangle$ is the wavefunction (describing the quantum state of all the electrons), and $E$ is the energy. Finding the ground-state energy means finding the smallest eigenvalue of $H$.

### Why electrons aren't qubits

There's a crucial complication. Electrons are **fermions** — they obey the Pauli exclusion principle. No two electrons can occupy the same quantum state. This means the wavefunction must be *antisymmetric*: swapping any two electrons flips the sign of $|\Psi\rangle$.

This is different from qubits, which are **bosonic** in the sense that there's no sign change when you swap them. A quantum computer built from qubits doesn't natively enforce fermionic antisymmetry. To simulate electrons on qubits, you need a **fermion-to-qubit encoding** — a mathematical map that translates between the language of electrons (creation and annihilation operators) and the language of qubits (Pauli operators).

This translation is non-trivial. Different encodings (Jordan-Wigner, Bravyi-Kitaev, parity, and others) make different tradeoffs between qubit count, gate depth, and locality. Choosing the right encoding can make the difference between a circuit that's feasible on near-term hardware and one that isn't. This is exactly the subject of our companion book, *From Molecules to Qubits*.

### The classical approximation hierarchy

Classical computational chemistry has developed a remarkable hierarchy of approximation methods:

| Method | Accuracy | Scaling | Captures correlation? |
|--------|----------|---------|----------------------|
| Hartree-Fock (HF) | ~99% of total energy | $O(N^4)$ | No — mean field only |
| DFT | Good for weak correlation | $O(N^3)$ | Partially — via functionals |
| MP2 | Perturbative correction | $O(N^5)$ | Partially |
| CCSD(T) | "Gold standard" | $O(N^7)$ | Yes — for weak correlation |
| Full CI | Exact (within basis) | $O(e^N)$ | Yes — all of it |

The pattern: more accuracy costs exponentially more computation. Hartree-Fock ignores electron correlation entirely (it treats each electron as moving in the average field of all others). Each step up the ladder captures more correlation but at drastically higher cost. Full Configuration Interaction (Full CI) is exact — it considers every possible arrangement of electrons — but its exponential scaling makes it usable only for tiny molecules.

The gap between CCSD(T) (the best practical classical method, scaling as $N^7$) and Full CI (exact but exponential) is where quantum computing enters. For molecules with **strong electron correlation** — where the mean-field picture breaks down entirely — CCSD(T) fails and Full CI is unaffordable. These are exactly the molecules that matter most for drug design: transition metal complexes, reaction transition states, and open-shell systems.

---

## The Quantum Angle

A quantum computer can represent the quantum state of $N$ electrons directly, using qubits in place of orbitals. The key algorithm is the **Variational Quantum Eigensolver** (VQE) — a hybrid quantum-classical algorithm for finding the ground-state energy of a molecular Hamiltonian.

### Second quantisation: the language of electrons

To put a molecular problem on a quantum computer, we first express it in **second quantisation** — a formalism where the Hamiltonian is written in terms of creation ($a_i^\dagger$) and annihilation ($a_i$) operators:

$$H = \sum_{ij} h_{ij} \, a_i^\dagger a_j + \frac{1}{2} \sum_{ijkl} h_{ijkl} \, a_i^\dagger a_j^\dagger a_k a_l$$

The coefficients $h_{ij}$ (one-electron integrals) capture electron-nucleus attraction and kinetic energy. The coefficients $h_{ijkl}$ (two-electron integrals) capture electron-electron repulsion. These numbers come from classical quantum chemistry packages — they are the "input" to the quantum computation.

### Fermion-to-qubit encodings

The creation and annihilation operators obey fermionic **anticommutation relations**: $\{a_i, a_j^\dagger\} = \delta_{ij}$. Pauli operators on qubits obey different algebra. The encoding translates between the two.

The simplest encoding is **Jordan-Wigner**: each orbital maps to one qubit, and $a_i^\dagger$ becomes a string of $Z$ operators (to enforce antisymmetry) followed by a raising operator. It's easy to understand but produces non-local operators — a single fermionic operator can touch all $N$ qubits.

**Bravyi-Kitaev** achieves better locality at the cost of a more complex mapping. There are many other encodings, each optimised for different properties. The choice of encoding affects the circuit depth and therefore the feasibility of the computation on real hardware.

For a deep dive on encodings, see our companion book: [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book).

### VQE: the variational quantum eigensolver

VQE uses the **variational principle**: for any trial state $|\psi(\theta)\rangle$, the expected energy is an upper bound on the true ground-state energy:

$$E_0 \leq \langle \psi(\theta) | H | \psi(\theta) \rangle$$

The algorithm:

1. **Prepare a trial state** on the quantum computer using a parameterised circuit (the **ansatz**): $|\psi(\theta)\rangle = U(\theta)|0\rangle$
2. **Measure the energy** by decomposing $H$ into a sum of Pauli operators and measuring each term. The total energy is the weighted sum of these measurements.
3. **Optimise classically**: feed the measured energy to a classical optimiser, which suggests new parameters $\theta$.
4. **Repeat** until the energy converges.

This is the same variational loop as QAOA (Unit 1) — quantum circuit produces an estimate, classical optimiser updates parameters, repeat. The difference is the cost function (molecular energy instead of cut count) and the ansatz (chemistry-inspired circuits instead of alternating problem/mixer layers).

### The ansatz: encoding chemical intuition

The quality of VQE depends heavily on the ansatz — the family of quantum states the parameterised circuit can reach. Two common choices:

**UCCSD (Unitary Coupled Cluster):** inspired by the classical CCSD method. It applies single and double excitations — moving one or two electrons between orbitals — with tunable coefficients. Chemically motivated, but the circuits can be deep.

**Hardware-efficient ansätze:** generic circuits (layers of rotations and entangling gates) that are short enough to run on noisy hardware. Less chemically motivated, but feasible. The risk: they may not contain the true ground state, or they may have barren plateaus.

### Measurement overhead

There's a catch. The molecular Hamiltonian, after encoding, becomes a sum of many Pauli terms: $H = \sum_i c_i P_i$. For H₂ with Jordan-Wigner, there are about 15 terms. For a drug-sized molecule, there could be millions. Each term requires separate measurements, and the statistical error shrinks as $1/\sqrt{N_\text{shots}}$. This **measurement overhead** is one of the main practical challenges of VQE.

---

## Worked Example

Let's compute the ground-state energy of **H₂** — the hydrogen molecule — at various bond lengths, building the potential energy surface.

H₂ has 2 electrons and (in a minimal basis) 4 spin-orbitals → 4 qubits after Jordan-Wigner encoding. This is small enough to run on any quantum computer (or simulator), but large enough to show the real VQE pipeline.

### The pipeline

1. **Compute molecular integrals** ($h_{ij}$, $h_{ijkl}$) using a classical chemistry package
2. **Build the qubit Hamiltonian** via Jordan-Wigner encoding
3. **Choose an ansatz** (UCCSD or hardware-efficient)
4. **Run VQE** — optimise parameters to minimise energy
5. **Sweep the bond length** from 0.2 Å to 2.5 Å and plot the potential energy surface

The equilibrium bond length (the minimum of the potential energy curve) is where H₂ is stable. The dissociation limit (large bond length) is where it breaks into two hydrogen atoms. Getting this curve right — especially the shape near the minimum — is the test of a good quantum chemistry method.

VQE with a 4-qubit UCCSD ansatz reproduces the exact Full CI result for H₂ to **chemical accuracy** (1.6 mHartree ≈ 1 kcal/mol) — the threshold at which energy differences become chemically meaningful.

→ **See [notebook `03-drug-discovery.ipynb`](../notebooks/03-drug-discovery.ipynb) for the runnable version.**

→ **See [Quokka Cookbook — Recipe 08: VQE for H₂](https://github.com/johnazariah/quokka-cookbook/recipes/08-vqe-h2/) for the QASM implementation.**

!!! lab "Lab 3: Run VQE on your Quokka"
    Recipe 08 builds the H₂ VQE circuit gate by gate in QASM. You'll see the Hartree-Fock initial state, the parameterised excitation, and the measurement — the same pipeline described in this chapter, rendered as a circuit you can run.

---

## Deep Dive: The VQE Pipeline End to End

*This section walks through every step from molecule to energy. Skip it if you want the application story only.*

### Step 1: Molecular integrals

The starting point is a classical quantum chemistry package (PySCF, Psi4, Gaussian). You specify the molecule (atom types and positions) and a basis set (e.g., STO-3G, cc-pVDZ). The package computes:

- **One-electron integrals** $h_{ij} = \langle \phi_i | \hat{h} | \phi_j \rangle$: kinetic energy + electron-nucleus attraction
- **Two-electron integrals** $h_{ijkl} = \langle \phi_i \phi_j | \hat{v} | \phi_k \phi_l \rangle$: electron-electron repulsion

For H₂ in STO-3G: 2 spatial orbitals → 4 spin-orbitals → a Hamiltonian with a handful of unique integrals. For a drug-sized molecule: hundreds of orbitals → billions of integrals (though many are negligibly small).

### Step 2: Fermion-to-qubit encoding

The second-quantised Hamiltonian is:

$$H = \sum_{ij} h_{ij} a_i^\dagger a_j + \frac{1}{2} \sum_{ijkl} h_{ijkl} a_i^\dagger a_j^\dagger a_k a_l$$

The **Jordan-Wigner** encoding maps each spin-orbital to one qubit:

$$a_j^\dagger \to \frac{1}{2}(X_j - iY_j) \otimes Z_{j-1} \otimes Z_{j-2} \otimes \cdots \otimes Z_0$$

The string of $Z$ operators enforces fermionic antisymmetry. Each fermionic term becomes a sum of Pauli strings. For H₂ (4 spin-orbitals, Jordan-Wigner), the Hamiltonian decomposes into ~15 Pauli terms.

The **Bravyi-Kitaev** encoding achieves $O(\log n)$ locality (vs. $O(n)$ for Jordan-Wigner) at the cost of a more complex mapping. For details, see [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book).

### Step 3: The ansatz circuit

The parameterised circuit that prepares trial wavefunctions. For UCCSD (Unitary Coupled Cluster with Singles and Doubles):

1. Start from the Hartree-Fock state: `x q[0]; x q[1];` (occupy the lowest orbitals)
2. Apply parameterised single excitations: $e^{\theta_s (a_i^\dagger a_j - a_j^\dagger a_i)}$
3. Apply parameterised double excitations: $e^{\theta_d (a_i^\dagger a_j^\dagger a_k a_l - \text{h.c.})}$

Each excitation operator, after encoding, becomes a sequence of CNOT ladders and $R_Z$ rotations. For H₂, the single UCCSD excitation is:

```
// Hartree-Fock state
x q[0];

// Single excitation with parameter theta
ry(theta) q[0];
cx q[0], q[1];
```

This is the circuit in the worked example and the Quokka Cookbook Recipe 08.

### Step 4: Measuring the energy

The encoded Hamiltonian is $H = \sum_i c_i P_i$ where each $P_i$ is a Pauli string (e.g., $Z_0 Z_1$, $X_0 X_1$, $Y_0 Y_1$).

To measure $\langle P_i \rangle$:

- **$Z$ terms:** measure directly in the computational basis. $\langle Z_j \rangle = P(|0\rangle_j) - P(|1\rangle_j)$.
- **$X$ terms:** apply $H$ (Hadamard) before measurement, then measure in the $Z$ basis. $\langle X_j \rangle = P(|+\rangle_j) - P(|-\rangle_j)$.
- **$Y$ terms:** apply $S^\dagger H$ before measurement.
- **Multi-qubit terms** ($Z_i Z_j$, $X_i X_j$): apply the appropriate basis rotations, measure, multiply the eigenvalues.

The total energy is:

$$\langle H \rangle = \sum_i c_i \langle P_i \rangle$$

Each $\langle P_i \rangle$ has statistical error $\sim 1/\sqrt{N_\text{shots}}$. For $T$ Pauli terms, the total error in the energy is $\sim T / \sqrt{N_\text{shots}}$. This **measurement overhead** is the main practical cost of VQE.

**Grouping trick:** Pauli terms that commute (e.g., $Z_0 Z_1$ and $Z_0$) can be measured simultaneously from the same circuit run. Optimal grouping reduces the number of distinct circuits needed.

### Step 5: Classical optimisation

Same loop as QAOA (Unit 1): the classical optimiser adjusts $\theta$ to minimise $\langle H \rangle$. Common choices: COBYLA (derivative-free), L-BFGS (gradient-based, using parameter-shift rules for gradients), SPSA (stochastic, noise-resilient).

The variational principle guarantees $\langle H \rangle \geq E_0$ — you can only overestimate the true ground-state energy. Finding the global minimum of the energy landscape is not guaranteed (local minima exist), but chemical intuition in the ansatz design helps: the UCCSD ansatz starts near the Hartree-Fock solution, so the optimiser has a good starting point.

---

## Reality Check

**What's been demonstrated.** VQE has been run on real quantum hardware for small molecules: H₂ (2 qubits, various groups since 2014), LiH (4 qubits), BeH₂ (6 qubits), and H₂O (up to 12 qubits with tapering). Google's 2020 Hartree-Fock experiment on 12 qubits was a milestone, though it used a non-variational approach.

**The gap to drug discovery.** A drug-sized active site might require 50–100 qubits (after encoding and tapering) and circuits with thousands or millions of gates. Current NISQ devices can handle at most ~20 qubits with meaningful accuracy. Error mitigation helps but doesn't close the gap for industrially relevant molecules.

**The measurement problem.** For a molecule with $M$ orbitals, the number of Pauli terms in the Hamiltonian scales as $O(M^4)$. Each term needs many measurement shots for acceptable statistics. For 100 orbitals, you might need $10^{10}$ measurements. Classical shadow tomography and grouping techniques reduce this, but it remains a bottleneck.

**What would change the picture.** Fault-tolerant quantum computers would enable **quantum phase estimation** (Unit 7) instead of VQE — giving exact energies rather than variational upper bounds, without the measurement overhead. But QPE requires much deeper circuits and is a post-NISQ algorithm.

**The hybrid approach works.** The real near-term strategy is **active-space methods**: use a classical computer for the "easy" electrons (core, weakly correlated) and a quantum computer for the "hard" ones (strongly correlated, in the active space). This is the approach we'll develop fully in Unit 8 (Climate & Energy).

---

## Chef's Notes

- **This chapter introduces the molecular Hamiltonian pattern.** In Unit 1, we encoded an optimisation objective as a cost Hamiltonian. Here we encode the *physical* Hamiltonian of a molecule. The mathematical structure is the same — a sum of Pauli operators — but the origin is different: physics rather than combinatorics.

- **VQE is QAOA's cousin.** Same variational loop, different cost function, different ansatz. If you understood the QAOA loop in Unit 1, VQE is a natural extension.

- **Fermion-to-qubit encodings are a deep topic.** We've given the 30-second version (Jordan-Wigner, Bravyi-Kitaev). For the full story — including parity encoding, ternary tree encoding, tapering, and the algebraic structure behind all of them — see our companion book: [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book).

- **H₂ is the "Hello World" of quantum chemistry.** Just as the Bell state is the simplest interesting quantum circuit, H₂ is the simplest interesting molecular simulation. It's small enough to verify classically, rich enough to show the full pipeline, and pedagogically indispensable. Our encodings book uses H₂ throughout for the same reason.

- **The path from here to real drug discovery** runs through Unit 8 (Climate & Energy), where we'll use quantum embedding methods to handle realistic molecular sizes — computing the active-site electrons quantumly and the environment classically.

- **Further reading:**
    - Peruzzo et al. (2014). *A variational eigenvalue solver on a photonic quantum processor.* [Nature Communications 5:4213](https://doi.org/10.1038/ncomms5213)
    - McArdle, Endo, Aspuru-Guzik, Benjamin, Yuan (2020). *Quantum computational chemistry.* [Reviews of Modern Physics 92:015003](https://doi.org/10.1103/RevModPhys.92.015003)
    - Google AI Quantum (2020). *Hartree-Fock on a superconducting qubit quantum computer.* [Science 369:1084–1089](https://doi.org/10.1126/science.abb9811)
    - Azariah et al. *From Molecules to Qubits.* [github.com/johnazariah/encodings-book](https://github.com/johnazariah/encodings-book)
    - Szabo and Ostlund (1996). *Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory.* The classical reference for computational chemistry foundations.
