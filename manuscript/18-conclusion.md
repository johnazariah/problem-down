# The Quantum Bottleneck

We started with a UPS driver and 20 stops. We end with a catalyst and 50 orbitals. Between them, eight problems — eight bottlenecks — and one recurring pattern.

Every quantum algorithm in this book does the same thing: it encodes a hard problem as a quantum operator, manipulates phases through interference, and extracts the answer through measurement. The operator changes — a cost Hamiltonian in Unit 1, a modular exponentiation oracle in Unit 2, a molecular Hamiltonian in Unit 3, a Grover iterator in Unit 5, a lattice Hamiltonian in Unit 7. The interference mechanism changes — the QAOA mixer, the QFT, the VQE ansatz, Grover's diffusion operator. But the architecture is always the same three acts: encode, interfere, measure.

This is not a coincidence. It's the structure of quantum mechanics itself. Quantum systems carry information in phases. Phases interfere. Measurement collapses the interference pattern into a classical answer. Every quantum algorithm is an interference machine designed to make the right answer loud and the wrong answers quiet.

## What's real, what's next, what's unknown

**Real today.** The algorithms work. Shor's algorithm factors numbers. VQE computes molecular energies. QAOA optimises combinatorial problems. Quantum kernels classify data. These are mathematical facts, verified on simulators and demonstrated on small quantum hardware. The question has never been whether the algorithms work — it's whether the hardware can run them at useful scale.

**Next.** The hardware gap is closing, but the target moves with the architecture. Resource estimates for breaking RSA-2048 have dropped from the 20-million-physical-qubit surface-code estimate of 2021 to sub-100,000-qubit QLDPC architecture studies in 2026, under different hardware and runtime assumptions. That does not mean practical cryptanalytic machines are imminent. It means the engineering target depends strongly on error correction, architecture, and parallelisation.

**Unknown.** Whether QAOA will beat classical optimisation at scale. Whether quantum kernels will find natural datasets where they outperform classical methods. Whether the quadratic speedup of amplitude estimation justifies the overhead of error correction. These are open research questions, not marketing talking points. The honest answer is: we don't know yet. This book has tried to give you the tools to follow the answers as they emerge.

## The one thing to remember

If you take away a single idea from this book, let it be this: quantum computing is not about parallelism. It's not about "trying all answers at once." It's about **interference** — the ability to make wrong answers cancel and right answers reinforce, using the phase structure of quantum mechanics. Every algorithm, every speedup, every advantage traces back to this one mechanism.

The problems are real. The algorithms are sound. The hardware is coming. What remains is engineering — and the quiet, persistent work of turning mathematical possibility into practical capability.


## Where to go from here

**If you want to build circuits.** Our companion book, the [Quokka Cookbook](https://github.com/johnazariah/quokka-cookbook), contains runnable recipes for every algorithm in this book — QAOA, Shor's period-finding, VQE, quantum kernels, amplitude estimation, and more — designed for the Quokka cloud platform. This book told you *why*; the Cookbook shows you *how*.

**If you want to understand encodings.** The transformation from molecules to qubits — fermion-to-qubit encodings — is the subject of [*From Molecules to Qubits*](https://github.com/johnazariah/encodings-book). It covers Jordan-Wigner, Bravyi-Kitaev, parity, ternary tree, and compact encodings, with the algebraic structure behind all of them.

**If you want the full mathematical treatment.** Nielsen and Chuang's *Quantum Computation and Quantum Information* (2000) remains the standard reference. It covers everything in this book and more, but starts from qubits rather than problems. Szabo and Ostlund's *Modern Quantum Chemistry* (1996) is the classical reference for the computational chemistry foundations behind Units 3, 7, and 8.

**If you want to follow the research.** The arXiv preprint server ([arxiv.org](https://arxiv.org)) is where quantum computing research appears first. The annotated bibliography below is a starting point; every paper links to its arXiv version where available.

**If you want to follow the project structure.** The authoritative manuscript and build source stays in the private working repo for this book while it is being prepared for publication. Runnable workbook exports are intended to live in `quantum-workbooks`, so the public notebook surface can stay separate from the book-writing source of truth.


## Annotated Bibliography

The references below are the most important papers cited in this book, grouped by topic. Each annotation explains what the paper contributes and why it matters. The full citation list for each unit appears in that unit's Chef's Notes.

### Quantum optimisation (Units 1, 6)

- Farhi, Goldstone, Gutmann (2014). *A Quantum Approximate Optimization Algorithm.* [arXiv:1411.4028](https://arxiv.org/abs/1411.4028). The paper that introduced QAOA — the starting point for quantum combinatorial optimisation. Short, readable, and still the best introduction to the algorithm.

- Basso, Farhi, Marwaha, Villalonga, Zhou (2021). *The Quantum Approximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the Sherrington-Kirkpatrick Model.* [arXiv:2110.14206](https://arxiv.org/abs/2110.14206). Showed how to compute exact QAOA performance at high depth via tree tensor networks — the framework that enabled precise comparison with other algorithms.

- Lucas (2014). *Ising formulations of many NP problems.* [Frontiers in Physics 2:5](https://doi.org/10.3389/fphy.2014.00005). The reference for encoding combinatorial problems as QUBO/Ising Hamiltonians. Covers graph problems, scheduling, satisfiability, and more.

- Farhi et al. (2001). *A quantum adiabatic evolution algorithm applied to random instances of an NP-complete problem.* [Science 292:472–475](https://doi.org/10.1126/science.1057726) ([arXiv:quant-ph/0001106](https://arxiv.org/abs/quant-ph/0001106)). The foundational paper on quantum annealing as an algorithmic paradigm.

### Cryptography and period-finding (Unit 2)

- Shor (1994). *Algorithms for Quantum Computation: Discrete Logarithms and Factoring.* [arXiv:quant-ph/9508027](https://arxiv.org/abs/quant-ph/9508027). The paper that launched quantum computing as a practical field. Still worth reading for its clarity.

- Gidney and Ekerå (2021). *How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits.* [arXiv:1905.09749](https://arxiv.org/abs/1905.09749). The definitive resource estimate for breaking RSA with a quantum computer — the benchmark that every subsequent estimate improves on.

- Webster, Berent, Chandra, Hockings et al. (2026). *The Pinnacle Architecture.* [arXiv:2602.11457](https://arxiv.org/abs/2602.11457). Reduced the quoted RSA-2048 footprint to under 100,000 physical qubits under its stated hardware and runtime assumptions, using quantum LDPC codes — a dramatic improvement over surface-code estimates.

### Quantum chemistry and simulation (Units 3, 7, 8)

- Peruzzo et al. (2014). *A variational eigenvalue solver on a photonic quantum processor.* [Nature Communications 5:4213](https://doi.org/10.1038/ncomms5213) ([arXiv:1304.3061](https://arxiv.org/abs/1304.3061)). The first experimental demonstration of VQE — the algorithm that makes quantum chemistry possible on near-term hardware.

- McArdle, Endo, Aspuru-Guzik, Benjamin, Yuan (2020). *Quantum computational chemistry.* [Reviews of Modern Physics 92:015003](https://doi.org/10.1103/RevModPhys.92.015003) ([arXiv:1808.10402](https://arxiv.org/abs/1808.10402)). The most comprehensive review of quantum algorithms for chemistry. Start here for the full landscape.

- Low and Chuang (2019). *Hamiltonian Simulation by Qubitization.* [Quantum 3:163](https://doi.org/10.22331/q-2019-07-12-163) ([arXiv:1610.06546](https://arxiv.org/abs/1610.06546)). Introduced qubitization — a fundamentally different approach to Hamiltonian simulation that achieves optimal query complexity. The theoretical foundation for next-generation quantum simulation algorithms.

- Reiher, Wiebe, Svore, Wecker, Troyer (2017). *Elucidating Reaction Mechanisms on Quantum Computers.* [PNAS 114:7555–7560](https://doi.org/10.1073/pnas.1619152114). A landmark early FeMoCo resource estimate for fault-tolerant quantum chemistry; useful as a benchmark, though later algorithms materially change the cost picture.

- Babbush, Wiebe, McClean, et al. (2018). *Low-Depth Quantum Simulation of Materials.* [Physical Review X 8:011044](https://doi.org/10.1103/PhysRevX.8.011044). A landmark resource-estimate paper for fault-tolerant Hubbard-model simulation; best read alongside later reviews when comparing assumptions across algorithms.

### Quantum machine learning (Unit 4)

- Havlíček, Córcoles, Temme, et al. (2019). *Supervised learning with quantum-enhanced feature spaces.* [Nature 567:209–212](https://doi.org/10.1038/s41586-019-0980-2) ([arXiv:1804.11326](https://arxiv.org/abs/1804.11326)). The experimental demonstration of quantum kernel methods — the algorithm from Unit 4 running on real hardware.

- Tang (2019). *A quantum-inspired classical algorithm for recommendation systems.* [STOC 2019](https://doi.org/10.1145/3313276.3316310) ([arXiv:1807.04271](https://arxiv.org/abs/1807.04271)). The dequantisation result that narrowed the territory for quantum ML advantage. Essential reading for anyone claiming quantum speedups in ML.

### Quantum finance (Unit 5)

- Montanaro (2015). *Quantum speedup of Monte Carlo methods.* [arXiv:1504.06987](https://arxiv.org/abs/1504.06987). The theoretical foundation for quantum amplitude estimation applied to Monte Carlo — the quadratic speedup that Unit 5 is built on.

- Grover (1996). *A fast quantum mechanical algorithm for database search.* [arXiv:quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043). Grover's search algorithm, which underlies amplitude estimation. The original quadratic speedup.

### Textbooks

- Nielsen and Chuang (2000). *Quantum Computation and Quantum Information.* Cambridge University Press. The standard reference for the field. Covers algorithms, error correction, and the mathematical foundations. Dense but comprehensive.

- Szabo and Ostlund (1996). *Modern Quantum Chemistry: Introduction to Advanced Electronic Structure Theory.* Dover. The classical reference for computational chemistry. Essential background for Units 3, 7, and 8.
