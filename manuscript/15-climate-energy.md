# Unit 8: Climate & Energy — *Designing a Better Catalyst for Carbon Capture*


## The Hook

In 2024, the concentration of CO₂ in Earth's atmosphere passed 427 parts per million; the highest in at least 4 million years. To limit global warming to 1.5°C, we need to remove approximately **10 gigatonnes of CO₂ per year** from the atmosphere by 2050, on top of drastic emissions reductions. Current direct air capture (DAC) technology removes about 10,000 tonnes per year. The gap is six orders of magnitude.

The bottleneck isn't engineering; it's chemistry. Every DAC process depends on a **catalyst** or **sorbent** that captures CO₂ molecules from air. The best current sorbents are expensive, degrade quickly, and require too much energy to regenerate. Better catalysts exist in principle; the chemical space of possible materials is vast; but finding them requires predicting **reaction pathways** on catalyst surfaces: which molecules bind, how strongly, through what transition states, with what activation energy.

This is a quantum chemistry problem. The catalyst's active site; the few atoms where the CO₂ molecule actually binds and reacts; involves **strongly correlated electrons** (just like the Hubbard model in Unit 7) embedded in a much larger environment (the metal surface, the solvent, the substrate). You need quantum-level accuracy for the active site and classical efficiency for everything else.

No single classical method gives uniformly reliable, systematically improvable treatment across both scales. DFT is fast but often unreliable for strongly correlated active sites. **CCSD(T)** (the "gold standard" classical method from Unit 3, scaling as $O(N^7)$) can be very accurate in weak-to-moderate correlation regimes, but it becomes expensive and less reliable for strongly multireference states. **Full CI** (exact but exponentially expensive) is impossible at scale.

This is where the quantum computing story comes together.


## The Bottleneck

### Surface chemistry: the accuracy-size tradeoff

A realistic catalyst simulation involves three scales:

1. **The active site** (~10–50 atoms, involving transition metals with partially filled **d-orbitals** — the outermost electron orbitals of metals like iron and copper, which give these atoms their complex chemistry): strongly correlated, requires quantum accuracy
2. **The local environment** (~50–200 atoms of the support material and nearby solvent): weakly correlated, treatable classically
3. **The bulk** (the rest of the material): can be described by a mean-field or continuum model

The challenge is that the active site's electronic structure depends on the environment, and the environment's response depends on the active site. They're coupled.

Classical methods pick one scale and approximate the others:
- **DFT**: handles everything at the same (insufficient) level of accuracy
- **Multiscale QM/MM**: use quantum mechanics (QM) for the active site and classical molecular mechanics (MM, a ball-and-spring model) for the environment — but the QM part is still classical DFT, which fails for strong correlation
- **Embedded CCSD(T)**: classical high-accuracy method for the active site, DFT for the environment — better, but CCSD(T) still scales as $O(N^7)$ and breaks down for the strongly correlated electronic states common in catalysis (molecules with unpaired electrons, or systems where multiple electron configurations contribute equally to the wavefunction)

What we need: a method that gives quantum-accurate results for the active site while scaling efficiently with the total system size.


## The Quantum Angle

### Quantum embedding: the best of both worlds

A plausible route is **quantum embedding**: use a quantum computer for the hard correlated fragment (the active site) and a classical computer for the rest (the environment). This is not a concession to limited hardware; it is a natural multiscale way to reserve expensive quantum resources for the part of the calculation where they matter most.

The mathematical framework:

1. **Define the active space**: identify the orbitals (typically 20–50) where strong correlation lives; the partially filled d-orbitals of the transition metal, the π-orbitals of the reacting molecule
2. **Embed**: use a classical method (DFT or Hartree-Fock) to compute the effect of the environment on the active space, producing an **effective Hamiltonian** that includes the environment's influence as a potential
3. **Solve the active space quantumly**: run VQE (Unit 3) or QPE (Unit 7) on the effective Hamiltonian; a much smaller problem than the full system
4. **Self-consistently update**: the active-space solution modifies the environment, which modifies the effective Hamiltonian, iterate until convergence

This approach — embedding a quantum-solved active space inside a classically-solved environment — goes by several names. **DMET** (Density Matrix Embedding Theory) is one well-developed framework; **active-space VQE/QPE** is the broader idea.

### The full pipeline

This unit is the culmination of the book. The complete quantum simulation pipeline draws on everything we've built:

```{figure} ../figures/climate-pipeline.png
:name: fig-climate-pipeline
:alt: Quantum simulation pipeline for catalyst modelling with cross-references to earlier units.

The capstone workflow is mostly classical plumbing around one hard quantum subproblem: solve the correlated active space, then feed that result back into the embedding loop.
```

Every step in this pipeline has been introduced in an earlier unit. This chapter shows how they connect into a single, end-to-end workflow.

### Why the active space matters

The active space is where the computational savings come from; and where the physical insight enters.

As an order-of-magnitude counting example, a CO₂-capture active site on a metal oxide surface might involve an iron or copper centre and its nearest-neighbour ligands — say 16 spatial orbitals (32 spin-orbitals after accounting for spin). After Jordan-Wigner encoding: 32 qubits. After symmetry reduction in a favourable encoding: perhaps 20–24 qubits. That does not make the problem automatically easy, but it shows why embedding is attractive: the quantum register tracks the fragment, not the whole surface.

The key point: **you don't need to simulate the whole surface.** The quantum computer handles the orbitals where strong correlation matters. The classical computer handles the rest of the surface and solvent at a cheaper approximate level. This division of labour is what makes quantum-classical embedding practical.


## Worked Example

To keep the capstone notebook runnable and honest, the companion notebook uses a **precomputed 2-qubit embedded Hamiltonian** for a toy catalyst active site rather than a full Fe₂O₃ cluster calculation.

What the notebook actually does:
1. starts from a classical embedding baseline and a precomputed reduced Hamiltonian;
2. runs one active-space VQE solve step on that reduced model;
3. compares the VQE result against exact diagonalisation of the same embedded toy Hamiltonian; and
4. shows where that quantum solve step sits inside the larger catalyst-screening pipeline.

What it does **not** do: build the active space from molecular integrals, construct the bath, or iterate the embedding self-consistently. Those are part of the real workflow, but they are represented structurally rather than executed in the notebook.

That still teaches the central idea. The point of quantum embedding is not that the quantum computer simulates the whole catalyst; it solves the **hard correlated fragment** after the classical front end has compressed the environment into an effective Hamiltonian.

→ *The next chapter builds the embedding workflow conceptually — select, embed, solve, iterate — while the notebook keeps the runnable part focused on the quantum solve step.*


## Reality Check

**Catalysis-scale resource estimates are still large.** Published fault-tolerant chemistry estimates for strongly correlated benchmarks such as FeMo-co remain far beyond current hardware. McArdle et al. (2020) summarise about 200 million physical qubits for the 2017 Trotter/QPE FeMo-co estimate under the surface-code assumptions used there, and about 1 million physical qubits' worth of Toffoli-distillation cost in a later qubitization-based estimate, though a full end-to-end fault-tolerant analysis for that later algorithm was not yet completed. These are nitrogen-fixation benchmarks rather than DAC calculations, but they show the right scale.

**What's been demonstrated.** Active-space VQE has been demonstrated for small molecules (H₂, LiH, BeH₂) on real hardware. No catalyst system has been simulated quantumly at a scale that produces new chemistry; the gap between "toy demonstration" and "useful catalyst screening" remains large.

**The classical competition.** DMRG and related tensor-network methods have made real progress on strongly correlated active spaces, including metalloenzyme complexes with active spaces above 70 spin-orbitals. But the review literature still points to a hard sweet spot around 100–200 spin-orbitals where no classical method is uniformly reliable.

**What remains open.** Embedding can shrink the quantum part dramatically, but the literature does not yet support a settled catalyst-screening threshold in qubits or years. Resource needs depend on the active-space choice, the solver (VQE versus QPE), and the fault-tolerance stack. The safe claim is that useful catalyst screening remains a fault-tolerant problem, not a NISQ one.

**What's real today:** The *pipeline* is real in pieces: active-space selection, integral generation, encoding, and classical embedding loops are mature workflows, and toy quantum subroutines can be inserted into that stack. What's missing is an end-to-end quantum solve at scientifically useful catalyst scale.


## Chef's Notes

- **This chapter is the capstone.** Every concept introduced in the book; qubits as binary variables (Unit 1), superposition and interference (Unit 2), fermions and encodings (Unit 3), variational methods (Units 1, 3), amplitude estimation (Unit 5), QPE and Trotterisation (Unit 7); comes together here in a single end-to-end pipeline.

- **Active-space and embedding methods are the main scaling strategy for quantum chemistry on limited hardware.** They can reduce the quantum resource requirement by an order of magnitude or more on realistic benchmark systems. The classical insight (where does strong correlation live?) combines with the quantum capability (treat the correlated subsystem more accurately).

- **The encodings book covers the encoding step in depth.** This unit's pipeline includes "encode the active-space Hamiltonian as a qubit operator"; the step where [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book) begins. Readers who want to understand *why* Jordan-Wigner produces long operator strings, or how tapering reduces qubit count, should start there.

- **Catalyst design is a compelling long-term target for quantum computing.** It's economically important (carbon capture, fertiliser production, hydrogen fuel cells), chemically concrete (compute reaction energetics for an active site), and still difficult for the classical toolbox in the strongly correlated regime. If quantum computers prove their worth anywhere in chemistry, embedded catalytic active sites are one plausible place it could happen.

- **Further reading:**
    - Reiher, Wiebe, Svore, Wecker, Troyer (2017). *Elucidating Reaction Mechanisms on Quantum Computers.* [PNAS 114:7555–7560](https://doi.org/10.1073/pnas.1619152114)
    - Lee, Berry, Gidney, et al. (2021). *Even More Efficient Quantum Computations of Chemistry Through Tensor Hypercontraction.* [PRX Quantum 2:030305](https://doi.org/10.1103/PRXQuantum.2.030305) ([arXiv:2012.09265](https://arxiv.org/abs/2012.09265))
    - Li, Otten, Isaev, et al. (2022). *Toward Practical Quantum Embedding Simulation of Realistic Chemical Systems on Near-Term Quantum Computers.* [Chemical Science 13:8953–8962](https://doi.org/10.1039/D2SC01492K)
    - Azariah et al. *From Molecules to Qubits.* [github.com/johnazariah/encodings-book](https://github.com/johnazariah/encodings-book)
