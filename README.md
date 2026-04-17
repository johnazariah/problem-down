# The Quantum Bottleneck

*Real Problems and their Quantum Solutions*

**Eight problems from logistics to climate — and the algorithms that could solve them.**

Most quantum computing books start with a qubit. This one starts with a delivery truck.

Each unit opens with an industry problem — a dollar figure, a bottleneck, a human cost — then pulls in only the quantum machinery needed to address it. No qubit-first pedagogy. No hype. Every chapter includes a Reality Check that states plainly what works today and what doesn't.

## Two ways to read this book

**The fast path.** Read the application chapters (Units 1–8). You'll understand what quantum computers could do for logistics, cryptography, drug discovery, machine learning, finance, supply chains, materials science, and climate — and which applications are close to practical.

**The full path.** Read the application chapters *and* the deep dives. You'll understand QAOA, Shor's algorithm, VQE, quantum kernels, amplitude estimation, QUBO, QPE, and quantum embedding — not as abstractions, but as tools built to solve specific problems.

## The eight units

| # | Unit | The Problem | The Quantum Angle |
|---|------|-------------|-------------------|
| 1 | Logistics | UPS saves $50M/year shaving 1 mile off each route | QAOA on graph problems |
| 2 | Cryptography | Your bank uses a trapdoor quantum computers can kick open | Shor's algorithm / period-finding |
| 3 | Drug Discovery | $2B and 12 years per new drug | VQE / molecular simulation |
| 4 | Machine Learning | 10⁸ features in your recommendation engine | Quantum kernels / sampling advantage |
| 5 | Finance | Pricing derivatives when the market can do anything | Quantum amplitude estimation |
| 6 | Supply Chains | Scheduling 10,000 nurses across 50 hospitals | QUBO / quantum annealing |
| 7 | Materials Science | Why room-temp superconductivity is so hard to predict | QPE / Hubbard models |
| 8 | Climate & Energy | Designing a better catalyst for carbon capture | Quantum simulation / embedding |

## Companion notebooks

Every unit has a companion Jupyter notebook. Some are faithful worked examples; others are toy demonstrations or pipeline illustrations where that is the honest way to show the idea at runnable scale. All are there to teach the algorithmic structure without pretending current hardware can already support the full industrial version.

The code in those notebooks is intentionally pedagogy-friendly rather than production-ready. We keep the Quokka calls, circuit construction, and measurement post-processing explicit so readers can see the mechanism directly; a polished software library would factor more of that away, but that would make the teaching worse.

## Companion books

- [**The Quokka Cookbook**](https://github.com/johnazariah/quokka-cookbook) — runnable QASM recipes for Quokka. This book tells you *why*; the Cookbook shows you *how*.
- [**From Molecules to Qubits**](https://github.com/johnazariah/encodings-book) — fermion-to-qubit encodings for quantum chemistry. Units 3, 7, and 8 bridge to this.

## Building

```bash
# PDF
bash build-pdf.sh

# Website
bash build-site.sh
```

## License

All rights reserved. See [LICENSE](LICENSE).
