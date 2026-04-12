# The Problem With Quantum

*What quantum computers are really for*

Each unit starts with an industry problem people already care about; a dollar figure, a bottleneck, a human cost; then pulls in only the quantum machinery needed to solve it.

## Units

| # | Unit | The Hook | The Quantum Angle |
|---|------|----------|-------------------|
| 1 | Logistics | UPS saves $50M/year shaving 1 mile off each route | QAOA on graph problems |
| 2 | Cryptography | Your bank uses a trapdoor quantum computers can kick open | Shor's algorithm / period-finding |
| 3 | Drug Discovery | $2B and 12 years per new drug | VQE / molecular simulation |
| 4 | Machine Learning | 10⁸ features in your recommendation engine | Quantum kernels / sampling advantage |
| 5 | Finance | Pricing derivatives when the market can do anything | Quantum amplitude estimation |
| 6 | Supply Chains | Scheduling 10,000 nurses across 50 hospitals | QUBO / quantum annealing |
| 7 | Materials Science | Why room-temp superconductivity is so hard to predict | QPE / Hubbard models |
| 8 | Climate & Energy | Designing a better catalyst for carbon capture | Quantum simulation / embedding |

## Structure

```
manuscript/    — chapter drafts (Markdown)
notebooks/     — companion Jupyter notebooks (one per unit)
figures/       — diagrams, plots, visualisations
SPEC.md        — project specification
```

## Related projects

- [The Quokka Cookbook](https://github.com/johnazariah/quokka-cookbook) — runnable QASM recipes for Quokka (the “how”)
- [From Molecules to Qubits](https://github.com/johnazariah/encodings-book) — deep dive on encodings for quantum chemistry simulation

## License

All rights reserved. See [LICENSE](LICENSE).
