# Unit 7: Materials Science — *The Room-Temperature Superconductor Problem*


## The Hook

A room-temperature superconductor would be one of the most transformative discoveries in the history of technology. Superconductors carry electrical current with **zero resistance**; no energy lost to heat, no wasted power. Today's superconductors require cooling to near absolute zero (below −140°C for "high-temperature" superconductors, below −250°C for conventional ones). The cooling infrastructure is expensive, bulky, and energy-intensive.

If you could superconduct at room temperature, you could:
- **Transmit electricity with zero loss.** The U.S. electrical grid loses about 5% of generated power to transmission resistance; roughly $20 billion per year.
- **Build MRI machines without liquid helium.** A hospital MRI costs $1–3M, largely because of the superconducting magnets that need continuous helium cooling.
- **Enable practical fusion reactors.** Tokamak fusion requires superconducting magnets to confine plasma. Room-temperature superconductors would simplify the engineering dramatically.
- **Revolutionise computing.** Superconducting circuits (already the basis of most quantum computers) could operate without cryogenics.

The problem is that we can't *predict* which materials will superconduct at high temperatures. The physics involves **strongly correlated electrons** — quantum systems where the interactions between electrons are so strong that the **mean-field** approximation (treating each electron as if it moves in the average field of all the others) breaks down completely.

The **Hubbard model** — the simplest model that captures this physics — has been studied for over 60 years. Its full phase diagram in two dimensions remains unsettled: different high-accuracy methods disagree in key parameter regimes, and whether the model supports superconductivity at high temperatures is still debated. This is not just a matter of computational effort; for the strongly correlated regime, it's a matter of computational *impossibility* with classical methods.


## The Bottleneck

### The Hubbard model

The Hubbard model describes electrons on a lattice with just two ingredients.

**Hopping.** An electron can jump from one lattice site to a neighbouring site. The amplitude for this hop is $t$ (the kinetic energy scale). In the language of creation and annihilation operators from Deep-Dive 3:

$$H_\text{hop} = -t \sum_{\langle i,j \rangle, \sigma} (c_{i\sigma}^\dagger c_{j\sigma} + \text{h.c.})$$

Here $c_{i\sigma}^\dagger$ creates an electron with spin $\sigma$ (up or down) at site $i$. The symbol $\langle i,j \rangle$ means the sum runs over neighbouring sites. The notation "h.c." (Hermitian conjugate) means "add the dagger of the preceding term" — it ensures electrons can hop in both directions.

**Repulsion.** Two electrons on the *same* site pay an energy cost $U$. The number operator $n_{i\sigma} = c_{i\sigma}^\dagger c_{i\sigma}$ counts whether site $i$ is occupied by a spin-$\sigma$ electron (0 or 1), so:

$$H_\text{int} = U \sum_i n_{i\uparrow} n_{i\downarrow}$$

This term is zero unless both a spin-up and a spin-down electron occupy the same site, in which case it costs energy $U$.

**The full Hamiltonian** is just these two terms combined:

$$H = H_\text{hop} + H_\text{int} = -t \sum_{\langle i,j \rangle, \sigma} (c_{i\sigma}^\dagger c_{j\sigma} + \text{h.c.}) + U \sum_i n_{i\uparrow} n_{i\downarrow}$$

Two parameters, $t$ and $U$. The ratio $U/t$ controls the physics:

- **Small $U/t$:** electrons hop freely, metal
- **Large $U/t$:** electrons localise to avoid repulsion, insulator (Mott insulator)
- **Intermediate $U/t$:** neither picture works; strongly correlated regime; this is where superconductivity may live

### Why classical methods fail

The Hilbert space of $N$ electrons on $L$ sites with spin has dimension $\binom{2L}{N}$. For a modest $10 \times 10$ lattice with 100 electrons: $\binom{200}{100} \approx 10^{58}$. No classical computer can store or diagonalise a matrix of this size.

**Density functional theory (DFT)** — the workhorse of solid-state physics — approximates the many-electron problem by working with the electron density rather than the full wavefunction (the same approach we met in Unit 3). It's a mean-field method: it handles weakly correlated materials well but *systematically fails* for strongly correlated systems.

**Quantum Monte Carlo (QMC)** — the best classical method for many-body quantum systems — works for bosons but suffers the **sign problem** for fermions: the antisymmetry of the fermionic wavefunction (the same minus sign that requires fermion-to-qubit encodings) causes Monte Carlo sampling to produce catastrophic cancellations, making the calculation exponentially expensive at low temperatures. Troyer and Wiese (2005) proved the sign problem is NP-hard in general.

**Exact diagonalisation** — exact but limited to ~20 sites. Physically relevant results require hundreds of sites.

**DMRG (Density Matrix Renormalization Group)** — an approach that represents the wavefunction as a chain of tensors (a **matrix product state**), capturing correlations efficiently in one dimension. Excellent for 1D systems, but the entanglement structure of 2D strongly correlated systems exceeds what matrix product states can represent.

The 2D Hubbard model at intermediate $U/t$ is in a computational no-man's land. No classical method can solve it reliably.


## The Quantum Angle

### Quantum Phase Estimation (QPE)

In Unit 3 (Drug Discovery), we used VQE; a variational method that gives energy *upper bounds*. VQE is a NISQ algorithm: shallow circuits, resilient to some noise, but limited by measurement overhead and ansatz quality.

**Quantum Phase Estimation** (QPE) is the fault-tolerant alternative. It gives the *exact* energy eigenvalue (to arbitrary precision) without variational optimisation or measurement overhead. The tradeoff: it requires much deeper circuits and full error correction.

QPE works like this:

1. **Prepare a trial state** $|\psi\rangle$ with non-zero overlap with the ground state
2. **Apply controlled time evolution** $e^{-iHt}$ to the trial state, controlled by an ancilla register
3. **Apply the inverse QFT** to the ancilla register
4. **Measure** the ancilla → the result is the energy eigenvalue (encoded as a binary fraction)

The key ingredient is step 2: implementing $e^{-iHt}$; the time evolution operator under the Hubbard Hamiltonian; as a quantum circuit.

### Hamiltonian simulation via Trotterisation

The Hamiltonian $H = H_\text{hop} + H_\text{int}$ is a sum of non-commuting terms. We can't implement $e^{-iHt}$ directly, but we can approximate it using the **Trotter-Suzuki decomposition**:

$$e^{-iHt} \approx \left(e^{-iH_\text{hop}\Delta t} \cdot e^{-iH_\text{int}\Delta t}\right)^{t/\Delta t}$$

Each factor ($e^{-iH_\text{hop}\Delta t}$ and $e^{-iH_\text{int}\Delta t}$) is easy to implement as a circuit because the individual terms within each part *do* commute. The error is $O(\Delta t^2)$ per step, so $O(t \cdot \Delta t)$ total. Use more Trotter steps (smaller $\Delta t$) for better accuracy; at the cost of deeper circuits.

Higher-order Trotter formulas reduce the error further. The encodings book (Chapter 15, *Trotter Formulas*) covers this in full detail.

### Resource estimation: how big does the quantum computer need to be?

This is the critical question. Babbush et al. (2018) estimated the resources for QPE on the 2D Hubbard model:

| Lattice size | Qubits needed | T-gates | Estimated wall time |
|---|---|---|---|
| $4 \times 4$ | ~100 logical | $10^8$ | Minutes |
| $8 \times 8$ | ~400 logical | $10^{11}$ | Hours |
| $16 \times 16$ | ~1,600 logical | $10^{14}$ | Days |

(A **T-gate** is a specific rotation gate that, together with the Clifford gates, enables universal quantum computation. T-gates are the most expensive operation in fault-tolerant computing because they require resource-intensive distillation procedures, so the T-gate count is the standard cost metric.)

With **surface code** error correction (the leading scheme, which encodes one logical qubit using ~1,000 physical qubits arranged on a 2D grid, at a physical error rate of $10^{-3}$), the $8 \times 8$ lattice needs about 400,000 physical qubits — well beyond current hardware, but within the scope of what might be built in 10–15 years.

The Pinnacle architecture (Unit 2) could dramatically reduce these numbers if quantum LDPC codes prove applicable to Hamiltonian simulation.


## Worked Example

Classically benchmark the **2-site Hubbard model** across $U/t \in [0, 10]$, then feed one benchmark ground-state energy into a compiled **3-bit QPE toy**. The sweep shows the **crossover from more delocalised to more localised behaviour** (a true Mott phase transition emerges only in larger lattices). The compiled circuit then shows what QPE is for: reading out an eigenphase once controlled time evolution exists.

The 2-site Hubbard model with 2 electrons has a 6-dimensional Hilbert space, representable with 4 qubits after Jordan-Wigner encoding. Small enough to benchmark exactly, and still useful for showing the structure of the quantum algorithm:

- At $U/t = 0$: the ground state is more delocalised
- At $U/t \gg 1$: the benchmark ground state becomes more localised, one electron per site
- The notebook's QPE step is a **toy phase-readout demonstration**, not a full controlled-$e^{-iHt}$ Hubbard simulation

→ *The next chapter builds QPE and the Trotter circuit from the components introduced in earlier deep dives, and the companion notebook shows the phase-readout part honestly on a compiled toy.*


## Reality Check

**The 2D Hubbard model is the "grand challenge" of quantum simulation.** It has been called the "standard model of condensed matter physics"; the simplest model that might explain high-temperature superconductivity in cuprate materials. Solving it is widely regarded as the problem most likely to yield the *first* practical quantum advantage in simulation.

**What's been demonstrated.** Small Hubbard models (2–4 sites) have been simulated on quantum hardware using VQE. Google's 2020 experiment on a $2 \times 2$ plaquette was a notable milestone. But these sizes are trivially classical; the value was in demonstrating the pipeline, not in producing new physics.

**The VQE stopgap.** Until fault-tolerant QPE is available, VQE on the Hubbard model is an active area of research. Problem-specific ansätze (like the Hamiltonian variational ansatz) can capture Hubbard physics better than generic hardware-efficient circuits. But VQE is fundamentally limited by measurement overhead and barren plateaus (exponentially flat optimisation landscapes) at scale.

**What would change the picture.** A fault-tolerant quantum computer capable of running QPE on a $10 \times 10$ Hubbard lattice. This would produce *new physics* — results that cannot be obtained any other way. The resource estimates suggest $\sim 10^5$ physical qubits with error rates $< 10^{-3}$. This is the most concrete milestone for "quantum utility" in simulation.

**What's real today:** Small Hubbard models are solvable classically. The quantum advantage will come from lattice sizes ($\geq 8 \times 8$) where classical methods disagree. The algorithms are ready; the hardware is not. Of all the applications in this book, materials simulation has the clearest path to producing genuinely new scientific knowledge once fault-tolerant machines arrive.


## Chef's Notes

- **QPE = QFT + controlled time evolution.** QPE was previewed in Unit 2 (Shor uses it for period-finding). Here it appears in its natural habitat: extracting energy eigenvalues from a physical Hamiltonian. The QFT, phase kickback, and controlled unitaries are the same machinery; applied to a different problem.

- **Trotterisation bridges Units 3, 7, and 8.** In Unit 3 (VQE), we prepared trial states and measured energy variationally. Here and in Unit 8, we implement actual time evolution ($e^{-iHt}$), which requires decomposing the Hamiltonian into a Trotter product. The encodings book (Chapters 14–16) covers this in detail.

- **The sign problem is deep.** The reason QMC fails for fermions is intimately connected to the antisymmetry of the fermionic wavefunction; the same physics that requires fermion-to-qubit encodings. Quantum computers bypass the sign problem by representing the fermionic state *directly* (via encodings), rather than sampling from it.

- **Further reading:**
    - Hubbard (1963). *Electron correlations in narrow energy bands.* [Proceedings of the Royal Society A 276:238–257](https://doi.org/10.1098/rspa.1963.0204)
    - Babbush, Wiebe, McClean, et al. (2018). *Low-Depth Quantum Simulation of Materials.* [Physical Review X 8:011044](https://doi.org/10.1103/PhysRevX.8.011044) ([arXiv:1711.04789](https://arxiv.org/abs/1711.04789))
    - Troyer and Wiese (2005). *Computational Complexity and Fundamental Limitations to Fermionic Quantum Monte Carlo Simulations.* [Physical Review Letters 94:170201](https://doi.org/10.1103/PhysRevLett.94.170201) ([arXiv:cond-mat/0407066](https://arxiv.org/abs/cond-mat/0407066))
    - Qin, Schäfer, Andergassen, Corboz, Gull (2022). *The Hubbard Model: A Computational Perspective.* [Annual Review of Condensed Matter Physics 13:275–302](https://doi.org/10.1146/annurev-conmatphys-090921-033948) ([arXiv:2103.12097](https://arxiv.org/abs/2103.12097))
