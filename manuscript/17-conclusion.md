# What Quantum Computers Are Actually For

We started with a UPS driver and 20 stops. We end with a catalyst and 50 orbitals. Between them, eight problems — and one recurring pattern.

Every quantum algorithm in this book does the same thing: it encodes a hard problem as a quantum operator, manipulates phases through interference, and extracts the answer through measurement. The operator changes — a cost Hamiltonian in Unit 1, a modular exponentiation oracle in Unit 2, a molecular Hamiltonian in Unit 3, a Grover iterator in Unit 5, a lattice Hamiltonian in Unit 7. The interference mechanism changes — the QAOA mixer, the QFT, the VQE ansatz, Grover's diffusion operator. But the architecture is always the same three acts: encode, interfere, measure.

This is not a coincidence. It's the structure of quantum mechanics itself. Quantum systems carry information in phases. Phases interfere. Measurement collapses the interference pattern into a classical answer. Every quantum algorithm is an interference machine designed to make the right answer loud and the wrong answers quiet.

## What's real, what's next, what's unknown

**Real today.** The algorithms work. Shor's algorithm factors numbers. VQE computes molecular energies. QAOA optimises combinatorial problems. Quantum kernels classify data. These are mathematical facts, verified on simulators and demonstrated on small quantum hardware. The question has never been whether the algorithms work — it's whether the hardware can run them at useful scale.

**Next.** The hardware gap is closing. Resource estimates for breaking RSA-2048 have dropped from 20 million physical qubits to under 100,000 in the space of five years. Early fault-tolerant devices — machines with a few thousand logical qubits — could arrive within a decade. The first applications to cross the utility threshold will likely be quantum chemistry (Units 3 and 8), where the problems are natively quantum and the active-space trick keeps qubit counts manageable.

**Unknown.** Whether QAOA will beat classical optimisation at scale. Whether quantum kernels will find natural datasets where they outperform classical methods. Whether the quadratic speedup of amplitude estimation justifies the overhead of error correction. These are open research questions, not marketing talking points. The honest answer is: we don't know yet. This book has tried to give you the tools to follow the answers as they emerge.

## The one thing to remember

If you take away a single idea from this book, let it be this: quantum computing is not about parallelism. It's not about "trying all answers at once." It's about **interference** — the ability to make wrong answers cancel and right answers reinforce, using the phase structure of quantum mechanics. Every algorithm, every speedup, every advantage traces back to this one mechanism.

The problems are real. The algorithms are sound. The hardware is coming. What remains is engineering — and the quiet, persistent work of turning mathematical possibility into practical capability.
