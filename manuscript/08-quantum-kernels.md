# Chapter 8: Quantum Kernels in Detail

_This chapter pairs with Chapter 7 (Machine Learning), which explained why quantum feature maps could provide computational advantage for classification. Here we build a quantum kernel classifier from scratch._

## In This Chapter

- **What you'll learn:** How to design a quantum feature map, compute kernel values from circuit measurements, build a kernel matrix, and train a classical SVM — the complete quantum kernel pipeline.
- **What you need:** From Chapter 2, you know qubits, CNOT, parameterised rotations ($R_Y$, $R_Z$), and measurement. Here we use measurement in a new way: the probability of a specific outcome *is* the kernel value.
- **Runnable version:** The companion notebook [`04-machine-learning.ipynb`](../notebooks/04-machine-learning.ipynb) trains a quantum kernel SVM on a cloud Quokka.

---

## The geometric picture

In Chapter 2, we encoded binary decisions as qubit states: red/blue → $|0\rangle$/$|1\rangle$. Here we encode *continuous* data — real-valued feature vectors — into qubit states. The quantum state space becomes a feature space for machine learning.

A single qubit lives on the **Bloch sphere** — a 2D surface parameterised by two angles $(\theta, \phi)$. A data point $(x_1, x_2)$ can be encoded as a point on this sphere using rotation gates: $R_Y(x_1) R_Z(x_2) |0\rangle$.

Two qubits live in a 4-dimensional complex space ($\mathbb{C}^4$). With entanglement, the accessible states fill a much richer space than two independent Bloch spheres — the entangled states have no classical analogue. This is where quantum kernels get their power: the feature space grows exponentially with qubit count.

For $n$ qubits: the feature space has $2^n$ complex dimensions. A classical computer can't even *store* a point in this space for $n > 50$. A quantum computer represents it naturally in the physical state of $n$ qubits.

---

## Designing a feature map

A **quantum feature map** is a parameterised circuit $U_\phi(x)$ that maps a classical data point $x$ to a quantum state $|\phi(x)\rangle = U_\phi(x)|0\rangle^n$.

### The simplest feature map: product encoding

Encode each feature independently:

```
ry(x₁) q[0];
ry(x₂) q[1];
```

This produces a *product state* — no entanglement. The feature space is just two independent Bloch spheres. The kernel $K(x, x')$ is the product of two cosines — equivalent to a classical kernel. No quantum advantage.

### Adding entanglement: the ZZ feature map

Entanglement is what makes quantum feature maps non-classical. Add a CNOT and an interaction term:

```
// Layer 1: encode individual features
ry(x₁) q[0];
ry(x₂) q[1];

// Entangle
cx q[0], q[1];

// Encode feature interaction
rz(x₁ · x₂) q[1];

// Disentangle
cx q[0], q[1];
```

The $R_Z(x_1 \cdot x_2)$ gate, sandwiched between CNOTs, is exactly the ZZ interaction from Chapter 2 (QAOA). But here, instead of encoding a graph edge cost, it encodes a *nonlinear feature interaction*. The kernel now depends on products of features — it goes beyond what any linear or product encoding can represent.

> **Design principle:** The expressiveness of the feature map comes from *entanglement* and *nonlinear encoding*. More layers (repeated encoding + entanglement blocks) create richer feature spaces — but also deeper circuits and more noise.

---

## Computing the kernel value

The kernel between two data points $x$ and $x'$ is:

$$K(x, x') = |\langle \phi(x') | \phi(x) \rangle|^2$$

This is the *squared overlap* between the two quantum states — the probability of measuring one state and finding it in the other. The Born rule gives us this for free.

### The kernel circuit

To compute $K(x, x')$:

1. Apply $U_\phi(x)$ — encode data point $x$
2. Apply $U_\phi(x')^\dagger$ — the *adjoint* (reverse order, negate all angles)  
3. Measure — the probability of getting $|00\ldots0\rangle$ is $K(x, x')$

```
// Encode x
ry(x₁) q[0]; ry(x₂) q[1];
cx q[0], q[1]; rz(x₁·x₂) q[1]; cx q[0], q[1];

// Adjoint: encode x' backwards with negated angles
cx q[0], q[1]; rz(-x'₁·x'₂) q[1]; cx q[0], q[1];
ry(-x'₂) q[1]; ry(-x'₁) q[0];

// Measure
measure q[0] -> c[0]; measure q[1] -> c[1];
```

Run this $N_\text{shots}$ times. Count how often you get $|00\rangle$. That fraction is $K(x, x')$.

If $x = x'$: the adjoint perfectly undoes the encoding → you always get $|00\rangle$ → $K(x, x) = 1$.

If $x$ and $x'$ are very different: the states don't overlap much → $|00\rangle$ is rare → $K(x, x') \approx 0$.

---

## Building the kernel matrix and training the SVM

For $m$ training points, compute all $m^2$ pairwise kernel values (using the circuit above for each pair). This gives the **kernel matrix** $K_{ij}$. Then train a classical SVM with this precomputed kernel — `SVC(kernel='precomputed')` in scikit-learn.

The quantum computer is only used for kernel evaluation. The SVM training, prediction, and cross-validation are entirely classical. This clean separation means quantum ML inherits all the theory and tooling of classical kernel methods.

---

## When does this actually help?

The honest answer: we don't know for natural datasets.

**Provable advantage exists** for constructed problems (Huang et al. 2022): classification tasks designed so that the quantum kernel captures structure that no classical kernel can. These proofs are real but the tasks are artificial.

**For natural data,** the question reduces to: does the data have structure that lives naturally in the entangled quantum feature space? If the data is essentially low-dimensional (as most real datasets are), a classical kernel might capture the same structure with fewer resources.

**The data loading bottleneck:** encoding $d$-dimensional classical data requires $O(d)$ gates per data point. For $d = 10^6$ (common in practice), the circuit is too deep for near-term hardware.

The most promising near-term application may be **quantum data** — data that is already quantum (e.g., outputs of quantum experiments or quantum simulations). For such data, classical kernels can't access the relevant feature space at all.

---

## What you should take away

1. **Quantum feature maps encode data as quantum states.** The feature space is the Hilbert space of $n$ qubits — exponentially large and natively available.

2. **The kernel is a measurement probability.** $K(x, x') = \Pr(|0\rangle^n)$ after applying $U_\phi(x)$ then $U_\phi(x')^\dagger$. The Born rule is the kernel evaluator.

3. **Entanglement is the source of power.** Without entanglement, quantum feature maps reduce to classical ones. The CNOT + $R_Z$ interaction (the ZZ gate from Chapter 2) is reused here for a completely different purpose.

4. **The quantum computer computes kernel values; everything else is classical.** SVM training, prediction, and interpretation use standard classical tools.

5. **Advantage is not guaranteed.** Quantum kernels provably help for some problems, but whether natural datasets benefit is an open question.
