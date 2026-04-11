# Chapter 16: Quantum Embedding Methods

_This chapter pairs with Chapter 15 (Climate & Energy), which explained why catalyst design requires quantum accuracy for the active site and classical efficiency for the environment. Here we show how to combine both._

## In This Chapter

- **What you'll learn:** How to select an active space, embed it in a classical environment, solve the active space with VQE or QPE, and iterate to self-consistency.
- **What you need:** This is the capstone deep dive. It draws on VQE (Chapter 6), QPE (Chapter 14), and fermion-to-qubit encodings (Chapter 6). If you've followed the deep dive path, you have everything you need.
- **Runnable version:** The companion notebook [`08-climate-energy.ipynb`](../notebooks/08-climate-energy.ipynb) demonstrates active-space VQE on a cloud Quokka.

---

## The active space idea

### Why you don't simulate the whole molecule

A catalyst system has hundreds of orbitals — carbon scaffolding, solvent molecules, bulk metal. But the chemistry happens at just a few: the metal d-orbitals where CO binds, the π* orbitals where electrons transfer.

**Strong correlation** — the kind that defeats classical methods — lives in these few orbitals. The rest are either doubly occupied (core electrons: inert, boring) or empty (high-energy virtual orbitals: irrelevant at normal temperatures). Classical methods handle these "boring" orbitals perfectly well.

The strategy: **use a quantum computer only for the hard part.** Select the 10–50 orbitals where classical methods fail (the "active space"), and solve those exactly with VQE (Chapter 6) or QPE (Chapter 14). Let a classical computer handle the other 450 orbitals with standard DFT or Hartree-Fock.

### How to choose the active space

This is part science, part art:

- **The metal d-orbitals.** Transition metals (Fe, Cu, Mn, Co) have partially filled d-shells. These orbitals are close in energy and strongly coupled — the definition of strong correlation.
- **The adsorbate frontier orbitals.** For CO₂ capture: the CO₂ $\pi^*$ orbital that accepts electrons from the metal.
- **Natural orbital analysis.** Compute approximate natural orbital occupation numbers from a cheap classical calculation (CASSCF or MP2). Orbitals with occupations significantly different from 0 or 2 are strongly correlated — include them.
- **Entropy-based selection.** Compute the single-orbital entropy from an approximate wavefunction. High-entropy orbitals are strongly correlated.

For a typical catalyst active site: 6 metal d-orbitals + 4–8 ligand orbitals = 10–14 active orbitals. After Jordan-Wigner encoding (Chapter 6): 20–28 qubits. After tapering (using point-group symmetry and particle-number conservation to reduce qubits): possibly 12–20 qubits. Feasible on near-term hardware.

---

## DMET: Density Matrix Embedding Theory

### The mathematical framework

DMET (Knizia and Chan, 2012) is the most elegant embedding approach. It works by recognising that the environment's effect on the fragment can be captured by a small **bath** — a set of orbitals that encode the entanglement between the fragment and the rest of the system.

The procedure:

1. **Solve the full system cheaply.** Run Hartree-Fock on all 500 orbitals. This gives a mean-field density matrix $\rho_\text{MF}$.

2. **Build the bath.** From $\rho_\text{MF}$, extract the entanglement between the fragment (active site) and the environment. The bath has the same number of orbitals as the fragment — so a 10-orbital fragment gets a 10-orbital bath. The 20-orbital *embedded problem* captures the fragment-environment entanglement exactly (at the mean-field level).

3. **Build the embedded Hamiltonian.** Project the full Hamiltonian onto the fragment + bath space. The result is a small Hamiltonian — 20 orbitals instead of 500 — that includes the environment's effect as an effective potential.

4. **Solve the embedded problem.** Run VQE (Chapter 6) or QPE (Chapter 14) on the 20-orbital embedded Hamiltonian. This gives the exact energy and density matrix for the fragment, in the presence of the environment.

5. **Self-consistency.** Update the mean-field solution with the quantum result. The new mean-field changes the bath, which changes the embedded Hamiltonian, which changes the quantum solution. Iterate until convergence (typically 5–10 cycles).

### What the quantum computer does

The quantum computer appears exactly once per self-consistency cycle: step 4. Everything else is classical linear algebra. The quantum computer solves a small, strongly correlated problem — the fragment + bath — that classical methods can't handle.

The pipeline is solver-agnostic. Today, use VQE on NISQ hardware. Tomorrow, use QPE on fault-tolerant hardware. The embedding framework doesn't change — only the quantum subroutine.

---

## The complete pipeline

This chapter ties together every deep dive in the book:

```
Catalyst system (molecule + surface)
    │
    ├── Classical: compute molecular integrals       [Chapter 6]
    │   (PySCF, Psi4 → h_ij, h_ijkl)
    │
    ├── Choose active space                          [This chapter]
    │   (metal d-orbitals + adsorbate frontier)
    │
    ├── Build embedding (DMET)                       [This chapter]
    │   (full system mean-field → bath construction → embedded Hamiltonian)
    │
    ├── Fermion-to-qubit encoding                    [Chapter 6]
    │   (Jordan-Wigner / Bravyi-Kitaev / From Molecules to Qubits)
    │
    ├── Qubit Hamiltonian = Σ g_k P_k               [Chapter 6]
    │
    ├── ┌── NISQ path ────────────────────┐
    │   │  VQE: ansatz + measurement      │          [Chapter 6]
    │   │  + classical optimiser           │          [Chapter 2]
    │   └─────────────────────────────────┘
    │   or
    │   ┌── Fault-tolerant path ──────────┐
    │   │  QPE + Trotterisation           │          [Chapter 14]
    │   │  → exact eigenvalue             │
    │   └─────────────────────────────────┘
    │
    ├── Self-consistency loop                        [This chapter]
    │   (update mean-field → rebuild bath → repeat)
    │
    └── Result: binding energy, activation barrier, reaction pathway
```

Every box references a chapter where the concept was introduced. A reader who followed the deep dive path (Chapters 2 → 4 → 6 → 8 → 10 → 12 → 14 → 16) has the tools to understand every step. A reader who skipped the deep dives can see the pipeline and know where to look for details.

---

## What you should take away

1. **The active space is the key insight.** You don't need a quantum computer for the whole molecule — just for the 10–50 orbitals where classical methods fail. This reduces the quantum resource requirement by orders of magnitude.

2. **DMET provides the framework.** It tells you how to build the bath, how to embed the fragment, and how to iterate to self-consistency. The quantum computer plugs in as the solver for the embedded problem.

3. **Everything connects.** The qubit Hamiltonian comes from Chapter 6 (VQE pipeline). The solver is either VQE (Chapter 6) or QPE (Chapter 14). The ZZ gates are from Chapter 2 (QAOA). The QFT is from Chapter 4 (Shor). Phase kickback drives QPE. The cost Hamiltonian pattern from Chapter 2 reappears as the molecular Hamiltonian.

4. **This is the pipeline for quantum utility in chemistry.** Not toy demonstrations on H₂, but real catalyst screening on industrially relevant systems. The engineering target: 50 active orbitals → 100 qubits → $10^5$ physical qubits with error correction. Ambitious but concrete.

5. **For the encoding step,** see [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book). That book covers exactly the transformation at the heart of this pipeline.
