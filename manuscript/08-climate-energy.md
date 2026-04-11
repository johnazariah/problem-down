# Unit 8: Climate & Energy — *Designing a Better Catalyst for Carbon Capture*

---

## The Hook

In 2024, the concentration of CO₂ in Earth's atmosphere passed 427 parts per million — the highest in at least 4 million years. To limit global warming to 1.5°C, we need to remove approximately **10 gigatonnes of CO₂ per year** from the atmosphere by 2050, on top of drastic emissions reductions. Current direct air capture (DAC) technology removes about 10,000 tonnes per year. The gap is six orders of magnitude.

The bottleneck isn't engineering — it's chemistry. Every DAC process depends on a **catalyst** or **sorbent** that captures CO₂ molecules from air. The best current sorbents are expensive, degrade quickly, and require too much energy to regenerate. Better catalysts exist in principle — the chemical space of possible materials is vast — but finding them requires predicting **reaction pathways** on catalyst surfaces: which molecules bind, how strongly, through what transition states, with what activation energy.

This is a quantum chemistry problem. The catalyst's active site — the few atoms where the CO₂ molecule actually binds and reacts — involves **strongly correlated electrons** (just like the Hubbard model in Unit 7) embedded in a much larger environment (the metal surface, the solvent, the substrate). You need quantum-level accuracy for the active site and classical efficiency for everything else.

No classical method handles both simultaneously. DFT is fast but inaccurate for strongly correlated active sites. Coupled cluster is accurate but can't handle the environment. Full CI is exact but impossible at scale.

This is where the quantum computing story comes together.

---

## The Bottleneck

### Surface chemistry: the accuracy-size tradeoff

A realistic catalyst simulation involves three scales:

1. **The active site** (~10–50 atoms, involving transition metals with partially filled d-orbitals): strongly correlated, requires quantum accuracy
2. **The local environment** (~50–200 atoms of the support material and nearby solvent): weakly correlated, treatable classically
3. **The bulk** (the rest of the material): can be described by a mean-field or continuum model

The challenge is that the active site's electronic structure depends on the environment, and the environment's response depends on the active site. They're coupled.

Classical methods pick one scale and approximate the others:
- **DFT**: handles everything at the same (insufficient) level of accuracy
- **Multiscale QM/MM**: quantum mechanics for the active site, molecular mechanics for the environment — but the QM part is still classical QM (DFT), which fails for strong correlation
- **Embedded CCSD(T)**: classical high-accuracy method for the active site, DFT for the environment — better, but CCSD(T) still scales as $O(N^7)$ and breaks down for the open-shell, multi-reference states common in catalysis

What we need: a method that gives quantum-accurate results for the active site while scaling efficiently with the total system size.

---

## The Quantum Angle

### Quantum embedding: the best of both worlds

The solution is **quantum embedding** — use a quantum computer for the hard part (the active site) and a classical computer for the easy part (the environment). This is not a compromise; it's the computationally optimal strategy.

The mathematical framework:

1. **Define the active space**: identify the orbitals (typically 20–50) where strong correlation lives — the partially filled d-orbitals of the transition metal, the π-orbitals of the reacting molecule
2. **Embed**: use a classical method (DFT or Hartree-Fock) to compute the effect of the environment on the active space, producing an **effective Hamiltonian** that includes the environment's influence as a potential
3. **Solve the active space quantumly**: run VQE (Unit 3) or QPE (Unit 7) on the effective Hamiltonian — a much smaller problem than the full system
4. **Self-consistently update**: the active-space solution modifies the environment, which modifies the effective Hamiltonian, iterate until convergence

This is known as **DMET** (Density Matrix Embedding Theory) or **active-space VQE/QPE**, depending on the specific formulation.

### The full pipeline

This unit is the culmination of the book. The complete quantum simulation pipeline draws on everything we've built:

```
Molecule / catalyst surface
    ↓
Molecular integrals (classical: PySCF, Psi4)         ← Unit 3
    ↓
Active space selection                                ← This unit
    ↓
Fermion-to-qubit encoding (JW, BK, ternary tree)     ← Unit 3 + encodings book
    ↓
Qubit Hamiltonian (sum of Pauli operators)            ← Unit 3
    ↓
Quantum circuit (VQE ansatz or QPE + Trotter)         ← Units 3, 7
    ↓
Measurement → energy                                  ← Unit 3
    ↓
Classical optimiser (VQE) or continued fractions (QPE) ← Units 1, 7
    ↓
Embedding self-consistency loop                       ← This unit
    ↓
Reaction pathway / activation energy / binding energy
```

Every step in this pipeline has been introduced in an earlier unit. This chapter shows how they connect into a single, end-to-end workflow.

### Why the active space matters

The active space is where the computational savings come from — and where the physical insight enters.

For CO₂ capture on a metal oxide surface, the active site might be an iron or copper atom with its nearest-neighbour oxygen atoms — perhaps 6 metal d-orbitals and 10 ligand orbitals: 16 active orbitals. After encoding and tapering, this requires ~12–16 qubits and circuits of moderate depth — feasible on near-term or early fault-tolerant hardware.

The key point: **you don't need to simulate the whole surface.** The quantum computer handles the 16 orbitals where strong correlation matters. The classical computer handles the other 500 orbitals where mean-field methods are perfectly adequate. This division of labour is what makes quantum-classical embedding practical.

---

## Worked Example

Active-space VQE for **CO adsorption on a small iron cluster** (a simplified model of an iron oxide catalyst surface).

Setup:
- Fe₂O₃ cluster with CO adsorbate
- Active space: 6 Fe d-orbitals + 4 CO π/π* orbitals = 10 active orbitals, 10 active electrons
- After Jordan-Wigner encoding: 20 qubits (or fewer with tapering)
- Environment: remaining orbitals treated with DFT embedding

The notebook computes the binding energy of CO on the cluster using:
1. Full DFT (fast, inaccurate for the binding site)
2. Active-space VQE (quantum accuracy for the binding site, DFT for the rest)
3. Exact active-space diagonalisation (classical benchmark)

The difference between DFT and active-space results is the **correlation energy** in the active site — the part that classical methods get wrong and quantum computers get right.

→ **See [notebook `08-climate-energy.ipynb`](../notebooks/08-climate-energy.ipynb) for the runnable version.**

!!! lab "Lab 8: The complete circuit pipeline"
    This example uses every circuit building block from the cookbook:
    
    - [Recipe 08: VQE for H₂](https://github.com/johnazariah/quokka-cookbook/recipes/08-vqe-h2/) — the VQE loop
    - [Recipe 09: QFT](https://github.com/johnazariah/quokka-cookbook/recipes/09-quantum-fourier-transform/) — if using QPE instead of VQE
    - [Recipe 10: QPE](https://github.com/johnazariah/quokka-cookbook/recipes/10-quantum-phase-estimation/) — the full phase estimation circuit
    - [Recipe 11: Error Mitigation](https://github.com/johnazariah/quokka-cookbook/recipes/11-error-mitigation-zne/) — making noisy results useful

---

## Reality Check

**Microsoft and PNNL's nitrogen fixation estimate.** In 2022, Microsoft and Pacific Northwest National Laboratory published resource estimates for simulating the FeMo cofactor of nitrogenase — the enzyme that fixes atmospheric nitrogen. This is a biologically critical catalyst with a strongly correlated active site. Their estimate: ~4 million physical qubits for a useful simulation using QPE with surface code error correction. With the Pinnacle architecture (Unit 2), this could potentially drop to $\sim 200,000$ physical qubits.

**What's been demonstrated.** Active-space VQE has been demonstrated for small molecules (H₂, LiH, BeH₂) on real hardware. No catalyst system has been simulated quantumly at a scale that produces new chemistry — the gap between "toy demonstration" and "useful catalyst screening" remains large.

**The classical competition.** DMRG (Density Matrix Renormalization Group) has made remarkable progress on catalyst active sites in recent years. Chan and co-workers have applied DMRG to problems with up to ~100 active orbitals in 1D-like geometries. For 2D active sites (common in surface catalysis), DMRG struggles — this is where quantum advantage is most likely.

**The timeline.** Useful quantum catalyst screening requires ~50 active orbitals → ~100 qubits (after encoding and tapering) → ~$10^5$ physical qubits with error correction. This is the same order of magnitude as the Hubbard model estimates from Unit 7. A generous estimate: 10–15 years.

**What's real today.** The *pipeline* is real — define active space, compute integrals, encode, optimize. The quantum chemistry software (PySCF, OpenFermion, the encodings library) exists and works. What's missing is a quantum computer large enough and quiet enough to run the circuits.

---

## Chef's Notes

- **This chapter is the capstone.** Every concept introduced in the book — qubits as binary variables (Unit 1), superposition and interference (Unit 2), fermions and encodings (Unit 3), variational methods (Units 1, 3), amplitude estimation (Unit 5), QPE and Trotterisation (Unit 7) — comes together here in a single end-to-end pipeline.

- **Active-space methods are the near-term strategy for quantum chemistry.** They reduce the quantum resource requirements by orders of magnitude compared to full-system simulation. The classical insight (where does strong correlation live?) combines with the quantum capability (solve the correlated subsystem exactly).

- **The encodings book covers the encoding step in depth.** This unit's pipeline includes "encode the active-space Hamiltonian as a qubit operator" — the step where [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book) begins. Readers who want to understand *why* Jordan-Wigner produces long operator strings, or how tapering reduces qubit count, should start there.

- **Catalyst design is a killer app for quantum computing.** It's economically critical (carbon capture, fertiliser production, hydrogen fuel cells), scientifically well-defined (compute the activation energy of a reaction pathway), and classically intractable at the relevant accuracy. If quantum computers prove their worth anywhere in chemistry, it's here.

- **Further reading:**
    - Reiher, Wiebe, Svore, Wecker, Troyer (2017). *Elucidating Reaction Mechanisms on Quantum Computers.* [PNAS 114:7555–7560](https://doi.org/10.1073/pnas.1619152114)
    - Lee, Berry, Gidney, et al. (2021). *Even More Efficient Quantum Computations of Chemistry Through Tensor Hypercontraction.* [PRX Quantum 2:030305](https://doi.org/10.1103/PRXQuantum.2.030305)
    - Li, Otten, Isaev, et al. (2022). *Toward Practical Quantum Embedding Simulation of Realistic Chemical Systems on Near-Term Quantum Computers.* [Chemical Science 13:8953–8962](https://doi.org/10.1039/D2SC01492K)
    - Azariah et al. *From Molecules to Qubits.* [github.com/johnazariah/encodings-book](https://github.com/johnazariah/encodings-book)
