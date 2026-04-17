# Deep-Dive 7: QPE and Trotterisation

_This deep dive pairs with Unit 7 (Materials Science), which explained why the Hubbard model defeats classical methods and how QPE could solve it. Here we build QPE and the Trotter time-evolution circuit from the components introduced in earlier deep dives._

## In This Chapter

- **What you'll learn:** How QPE extracts exact energy eigenvalues, how Trotterisation approximates time evolution as a circuit, and how to estimate the resources needed for real materials simulation.
- **What you need:** From Deep-Dive 2 (Shor), you know the QFT and phase kickback. From Deep-Dive 1 (QAOA), you know the ZZ gate and CNOT sandwich. Here we combine them for Hamiltonian simulation.
- **Runnable version:** The companion notebook [`07-materials-science.ipynb`](../notebooks/07-materials-science.ipynb) classically benchmarks the 2-site Hubbard model and then runs a compiled toy QPE phase-readout circuit on a cloud Quokka.


## QPE: from phases to eigenvalues

### Where we are

Let's take stock of what we already have. From Deep-Dive 1, we know how to build cost Hamiltonians from ZZ gates and encode optimisation problems as quantum operators. From Deep-Dive 2, we know how to extract a hidden number from the phase of a quantum state — that's what the controlled-powers-plus-inverse-QFT pattern did for Shor's algorithm. From Deep-Dive 3, we know how to encode a molecular Hamiltonian as a sum of Pauli operators.

QPE puts these together. The question it answers: given a physical system described by a Hamiltonian $H$, what are its energy levels?

Here's the idea in words before we touch a formula. If you let a quantum system evolve under its Hamiltonian $H$ for time $t$, each energy eigenstate picks up a phase proportional to its energy — states with higher energy rotate faster. QPE measures that rotation speed. The QFT (from Deep-Dive 2) converts the rotation into a binary number you can read out. Phase kickback (from Deep-Dive 2) is the mechanism that transfers the phase information from the system to the measurement qubits.

That's it. Same tools, new application. Let's see how they fit together.

### The setup

QPE involves two registers. The **system register** holds the quantum state whose energy we want to measure. The **ancilla register** — $m$ helper qubits used as a measurement instrument — will hold the answer.

If the system is in an eigenstate $|\\psi\\rangle$ of the Hamiltonian with energy $E$, then time evolution gives $e^{-iHt}|\\psi\\rangle = e^{-iEt}|\\psi\\rangle$. The phase $\\phi = -Et/(2\\pi)$ encodes the energy. QPE extracts $\\phi$.

### The circuit

The circuit has four steps — all of which reuse pieces you've seen before:

1. **Hadamard** all ancillas → superposition
2. **Controlled-$U^{2^k}$** for each ancilla qubit $k$ → phase accumulation
3. **Inverse QFT** on the ancillas → converts phases to a binary number
4. **Measure** the ancillas → read out $\phi$

Steps 1, 3, and 4 we've seen before. The inverse QFT is the QFT from Deep-Dive 2, run backwards (swap the order of gates, negate the rotation angles). Step 2 is the new ingredient.

### Controlled-$U^{2^k}$

Ancilla qubit $k$ controls the application of $U^{2^k}$ to the system register. If the system is in eigenstate $|\psi\rangle$:

$$\text{c-}U^{2^k}\left(\frac{|0\rangle + |1\rangle}{\sqrt{2}}\right)|\psi\rangle = \frac{|0\rangle + e^{2\pi i \cdot 2^k \phi}|1\rangle}{\sqrt{2}} |\psi\rangle$$

The ancilla picks up a phase proportional to $2^k \phi$. After all $m$ controlled operations, the ancilla register holds:

$$\frac{1}{\sqrt{2^m}} \sum_{k=0}^{2^m-1} e^{2\pi i k \phi} |k\rangle$$

This is exactly the QFT of $|\phi\rangle$. Applying the inverse QFT yields $\phi$ (or its best $m$-bit approximation).

> **Connection to Shor:** In Deep-Dive 2, QPE was implicit — the controlled modular exponentiation + QFT was QPE applied to the modular multiplication operator. Here we make it explicit and apply it to a physically motivated Hamiltonian.


## Trotterisation: implementing $e^{-iHt}$

### The problem

QPE requires controlled applications of $U = e^{-iHt}$. But $H$ is a sum of terms that don't commute:

$$H = H_1 + H_2 + \cdots + H_L$$

We can implement $e^{-iH_k t}$ for each individual term (because each term has a simple structure; products of Pauli operators). But $e^{-iHt} \neq e^{-iH_1 t} \cdot e^{-iH_2 t} \cdots e^{-iH_L t}$ because the terms don't commute.

### First-order Trotter

The **Trotter formula** says: the product of exponentials approximates the exponential of the sum if the time step is small:

$$e^{-iHt} \approx \left(e^{-iH_1 \Delta t} \cdot e^{-iH_2 \Delta t} \cdots e^{-iH_L \Delta t}\right)^{N}$$

where $\Delta t = t/N$. The error is $O(L^2 t^2 \Delta t)$; it goes to zero as $\Delta t \to 0$ (more Trotter steps).

### Second-order Trotter (Suzuki)

A better approximation symmetrises the product:

$$e^{-iHt} \approx \left(e^{-iH_1 \Delta t/2} \cdot e^{-iH_2 \Delta t/2} \cdots e^{-iH_L \Delta t} \cdots e^{-iH_2 \Delta t/2} \cdot e^{-iH_1 \Delta t/2}\right)^{N}$$

The error drops to $O(L^3 t^3 \Delta t^2)$; much better for the same circuit depth. Higher-order formulas exist but add circuit complexity.

### Implementing each term

For the Hubbard model:

**Hopping terms** $c_{i\sigma}^\dagger c_{j\sigma} + \text{h.c.}$: after Jordan-Wigner encoding (Deep-Dive 3), these become $\frac{1}{2}(X_i X_j + Y_i Y_j) \cdot Z_\text{string}$. The time evolution under this term is:

$$e^{-i\theta(X_i X_j + Y_i Y_j)/2}$$

This requires 2 CNOTs mixed with single-qubit rotations — a known decomposition that generalises the ZZ sandwich from Deep-Dive 1.

**Interaction terms** $n_{i\uparrow} n_{i\downarrow}$: after encoding, each becomes $\frac{(1-Z_{i\uparrow})(1-Z_{i\downarrow})}{4}$. This is diagonal; the time evolution is a $ZZ$ phase gate, exactly the CNOT sandwich from Deep-Dive 1:

```{figure} ../figures/trotter-zz-interaction.png
:name: fig-trotter-zz-interaction
:alt: Trotter ZZ interaction term implemented as a CNOT-Rz-CNOT sequence.

The interaction term is diagonal, so the Hubbard Trotter step reuses the same ZZ phase gadget that already appeared in QAOA and VQE.
```

Every piece of the Trotter circuit is built from gates we already know.


## Resource estimation

### Gate count

For an $L \times L$ Hubbard lattice with $2L^2$ spin-orbitals:

| Component | Gate count |
|:---|:---|
| Hopping + interaction terms per Trotter step | $O(L^2)$ two-qubit gates |
| One Trotterized call to $e^{-iHt}$ | $O(N_\text{Trotter} \cdot L^2)$ gates |
| Standard QPE to phase precision $\epsilon_\text{PE}$ | $O(N_\text{Trotter} \cdot L^2 / \epsilon_\text{PE})$ controlled evolution |
| Inverse QFT overhead | $O(\log^2(1/\epsilon_\text{PE}))$ controlled rotations |

The key point is that QPE is **not** linear in the number of ancilla bits. If you use $m$ ancillas, standard QPE applies $U, U^2, \ldots, U^{2^{m-1}}$, so the total coherent evolution scales like $2^m = O(1/\epsilon_\text{PE})$, not $O(m)$. That is why it is safer to quote published end-to-end resource estimates than to multiply a few back-of-the-envelope factors.

McArdle et al. (2020) summarise two representative results for a 100-site 2D Fermi-Hubbard problem. A qubitization-based estimate with an intensive error target lands at about $7.1 \times 10^8$ T-gates and roughly $2$-$3$ million physical qubits. A Trotter-based estimate with a size-extensive error target lands at about $10^6$ Toffoli gates / $10^7$-$10^8$ T-gates and roughly $4 \times 10^5$-$6 \times 10^5$ physical qubits. Those figures are not plug-and-play comparable because the error conventions differ, but they put the problem firmly in the fault-tolerant regime.

### Physical qubits

There is no single, architecture-independent conversion from logical to physical qubits. The code distance, factory overhead, routing strategy, and target logical failure rate all matter. That is why the literature for similar Hubbard problems reports a **band** of physical-qubit costs, from hundreds of thousands into the low millions, rather than one fixed number obtained by a single logical-to-physical multiplier.


## What you should take away

1. **QPE = controlled time evolution + inverse QFT.** It extracts energy eigenvalues to arbitrary precision. The QFT (from Deep-Dive 2) and phase kickback (from Deep-Dive 2) do the heavy lifting.

2. **Trotterisation is the bridge between Hamiltonians and circuits.** It breaks $e^{-iHt}$ into a product of simple operations — each implemented with the gates from Deep-Dive 1 (ZZ sandwich for diagonal terms) and generalisations for off-diagonal terms.

3. **The circuit is deep but structured.** Every gate in a Trotter circuit has a physical meaning: it simulates one interaction in the Hamiltonian for one time step. More accuracy → more Trotter steps → deeper circuit.

4. **Resource estimates are concrete, but assumption-dependent.** For roughly 100-site 2D Hubbard problems, published fault-tolerant studies land in the $10^7$-$10^8$ to $10^9$ T-gate band and the hundreds-of-thousands to low-millions physical-qubit band, depending on the algorithm and error model.

5. **Everything connects.** QPE reuses the QFT from Deep-Dive 2 (Shor). Trotterisation reuses the ZZ gate from Deep-Dive 1 (QAOA). The fermionic encoding comes from Deep-Dive 3 (VQE). This is where the threads converge.


## Beyond Trotter: qubitization

Trotterisation approximates time evolution by breaking it into small steps — like drawing a curve with many short straight-line segments. More segments give a better approximation, but the circuit gets deeper.

**Qubitization** (Low and Chuang, 2019) takes a fundamentally different approach: instead of approximating the curve, it encodes the Hamiltonian directly into a larger unitary (a technique called **block encoding**) and traces the exact curve. The result is a family of algorithms — **quantum signal processing** (QSP) and **quantum singular value transformation** (QSVT) — that achieve the theoretically optimal gate count for Hamiltonian simulation.

The tradeoff: qubitization requires more ancilla qubits and a more complex circuit structure. For near-term devices, Trotterisation's simpler circuits may still win. But for the long-term fault-tolerant regime, qubitization is the theoretically optimal approach.

- Low and Chuang (2019). *Hamiltonian Simulation by Qubitization.* [Quantum 3:163](https://doi.org/10.22331/q-2019-07-12-163) ([arXiv:1610.06546](https://arxiv.org/abs/1610.06546))
- Gilyén, Su, Low, Wiebe (2019). *Quantum singular value transformation and beyond.* [STOC 2019](https://doi.org/10.1145/3313276.3316366) ([arXiv:1806.01838](https://arxiv.org/abs/1806.01838))
