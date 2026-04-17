# Deep-Dive 8: Quantum Embedding Methods

_This deep dive pairs with Unit 8 (Climate & Energy), which explained why catalyst design requires quantum accuracy for the active site and classical efficiency for the environment. Here we show how to combine both._

## In This Chapter

- **What you'll learn:** How to select an active space, embed it in a classical environment, solve the active space with VQE or QPE, and iterate to self-consistency.
- **What you need:** This is the capstone deep dive. It draws on VQE (Deep-Dive 3), QPE (Deep-Dive 7), and fermion-to-qubit encodings (Deep-Dive 3). If you've followed the deep dive path, you have everything you need.
- **Runnable version:** The companion notebook [`08-climate-energy.ipynb`](../notebooks/08-climate-energy.ipynb) illustrates the embedded VQE solve step on a cloud Quokka using a precomputed toy Hamiltonian.


## The active space idea

This chapter moves faster than the earlier deep dives. That's by design: it's the capstone, and every tool it uses has been built in a previous chapter. Where earlier deep dives taught one mechanism at a time (the ZZ gate, the QFT, the VQE loop), this one assembles a *pipeline* from pieces you already know. If a step feels unfamiliar, the cross-references will take you back to where it was introduced.

The pipeline has three stages: **select** the orbitals that need quantum treatment, **embed** them in the classical environment, and **solve** the embedded problem with VQE or QPE. Let's take them one at a time.

### Why you don't simulate the whole molecule

A catalyst system has hundreds of orbitals; carbon scaffolding, solvent molecules, bulk metal. But the chemistry happens at just a few: the metal d-orbitals where CO binds, the π* orbitals where electrons transfer.

**Strong correlation**; the kind that defeats classical methods; lives in these few orbitals. The rest are either doubly occupied (core electrons: inert, boring) or empty (high-energy virtual orbitals: irrelevant at normal temperatures). Classical methods handle these "boring" orbitals perfectly well.

The strategy: **use a quantum computer only for the hard part.** Select the 10–50 orbitals where classical methods are most stressed (the "active space"), and treat those with VQE (Deep-Dive 3) or, in a fault-tolerant setting, QPE (Deep-Dive 7). Let a classical computer handle the other 450 orbitals with standard DFT or Hartree-Fock.

### How to choose the active space

This is part science, part art:

- **The metal d-orbitals.** Transition metals (Fe, Cu, Mn, Co) have partially filled d-shells. These orbitals are close in energy and strongly coupled; the definition of strong correlation.
- **The adsorbate frontier orbitals.** For CO₂ capture: the CO₂ $\pi^*$ orbital that accepts electrons from the metal.
- **Natural orbital analysis.** Compute approximate natural orbital occupation numbers from a cheap classical calculation (CASSCF — Complete Active Space Self-Consistent Field, a classical method that optimises both orbitals and electron configurations within a small active space — or MP2, the perturbative correction from Unit 3's hierarchy). Orbitals with occupations significantly different from 0 or 2 are strongly correlated; include them.
- **Entropy-based selection.** Compute the single-orbital entropy from an approximate wavefunction. High-entropy orbitals are strongly correlated.

As an order-of-magnitude example, a catalyst active site with 6 metal d-orbitals and 4–8 ligand orbitals gives 10–14 active orbitals. After Jordan-Wigner encoding (Deep-Dive 3): 20–28 qubits. After tapering (using point-group symmetry and particle-number conservation to reduce qubits): possibly 12–20 qubits in a favourable case. That is small enough to motivate embedding, but not automatically practical on current hardware once circuit depth and measurement cost are included.


## DMET: Density Matrix Embedding Theory

### The mathematical framework

DMET (Knizia and Chan, 2012) is a clean embedding approach. It works by recognising that the environment's effect on the fragment can be captured by a small **bath**; a set of orbitals that encode the entanglement between the fragment and the rest of the system.

The procedure:

1. **Solve the full system cheaply.** Run Hartree-Fock on all 500 orbitals. This gives a mean-field **density matrix** $\rho_\text{MF}$ — a mathematical object that describes the quantum state of a system in terms of probabilities and correlations (a generalisation of the outer product $|\psi\rangle\langle\psi|$ from Deep-Dive 5, extended to handle statistical mixtures of states).

2. **Build the bath.** From $\rho_\text{MF}$, extract the entanglement between the fragment (active site) and the environment. The bath has the same number of orbitals as the fragment; so a 10-orbital fragment gets a 10-orbital bath. The 20-orbital *embedded problem* captures the fragment-environment entanglement exactly (at the mean-field level).

3. **Build the embedded Hamiltonian.** Project the full Hamiltonian onto the fragment + bath space. The result is a small Hamiltonian; 20 orbitals instead of 500; that includes the environment's effect as an effective potential.

4. **Solve the embedded problem.** Run VQE (Deep-Dive 3) or QPE (Deep-Dive 7) on the 20-orbital embedded Hamiltonian. This yields a fragment energy and density matrix in the presence of the environment: variational and approximate with VQE, systematically improvable and in principle arbitrarily precise with QPE.

5. **Self-consistency.** Update the mean-field solution with the quantum result. The new mean-field changes the bath, which changes the embedded Hamiltonian, which changes the quantum solution. Iterate until convergence (typically 5–10 cycles).

### What the quantum computer does

The quantum computer appears exactly once per self-consistency cycle: step 4. Everything else is classical linear algebra. The quantum computer tackles the small, strongly correlated fragment + bath problem; the part classical methods handle least systematically.

The pipeline is solver-agnostic. Today, use VQE on NISQ hardware. Tomorrow, use QPE on fault-tolerant hardware. The embedding framework doesn't change; only the quantum subroutine.


## The complete pipeline

This chapter ties together every deep dive in the book:

```{figure} ../figures/embedding-pipeline.png
:name: fig-embedding-pipeline
:alt: Quantum-classical embedding pipeline showing NISQ and fault-tolerant paths with chapter cross-references.

Embedding keeps the quantum computer on the small fragment where strong correlation lives and leaves the environment to the classical solver.
```

Every box references a chapter where the concept was introduced. A reader who followed the deep dive path (Chapters 2 → 4 → 6 → 8 → 10 → 12 → 14 → 16) has the tools to understand every step. A reader who skipped the deep dives can see the pipeline and know where to look for details.

The companion notebook is narrower than the full theory in this chapter. It starts from a precomputed embedded Hamiltonian for a 2-qubit toy active space, runs one VQE solve step on Quokka, and uses that runnable fragment to show where the quantum subroutine lives in the larger select → embed → solve → iterate pipeline.

→ **See [notebook `08-climate-energy.ipynb`](../notebooks/08-climate-energy.ipynb) for the runnable version.**


## What you should take away

1. **The active space is the key insight.** You don't need a quantum computer for the whole molecule; just for the 10–50 orbitals where classical methods are most stressed. This can reduce the quantum resource requirement by orders of magnitude.

2. **DMET provides the framework.** It tells you how to build the bath, how to embed the fragment, and how to iterate to self-consistency. The quantum computer plugs in as the solver for the embedded problem.

3. **Everything connects.** The qubit Hamiltonian comes from Deep-Dive 3 (VQE pipeline). The solver is either VQE (Deep-Dive 3) or QPE (Deep-Dive 7). The ZZ gates are from Deep-Dive 1 (QAOA). The QFT is from Deep-Dive 2 (Shor). Phase kickback drives QPE. The cost Hamiltonian pattern from Unit 1 reappears as the molecular Hamiltonian.

4. **This is one plausible pipeline for quantum utility in chemistry.** The target is not another H₂ demo but chemically meaningful embedded active spaces on realistic systems. Published chemistry resource estimates still span a wide band, from roughly a million physical qubits into the hundreds of millions depending on algorithm and assumptions. Embedding matters because it is one of the few routes to pushing those costs down by shrinking the quantum fragment instead of attacking the full system head-on.

5. **For the encoding step,** see [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book). That book covers exactly the transformation at the heart of this pipeline.
