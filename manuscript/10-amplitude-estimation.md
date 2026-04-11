# Chapter 10: Amplitude Estimation from Grover

_This chapter pairs with Chapter 9 (Finance), which explained why Monte Carlo pricing is slow and how quantum amplitude estimation offers a quadratic speedup. Here we build the amplitude estimation circuit from Grover's algorithm._

## In This Chapter

- **What you'll learn:** How Grover's algorithm works geometrically, how quantum amplitude estimation extracts probabilities, and why the quadratic speedup matters for Monte Carlo.
- **What you need:** From Chapter 4, you know phase kickback and the QFT. Here we add a new geometric picture: Grover's algorithm as a rotation in a 2D plane.
- **Runnable version:** The companion notebook [`05-finance.ipynb`](../notebooks/05-finance.ipynb) demonstrates amplitude estimation on a cloud Quokka.

---

## Grover's algorithm: the geometric picture

### The search problem

You have a function $f:\{0,1\}^n \to \{0,1\}$ with $M$ "marked" inputs (where $f(x) = 1$) among $N = 2^n$ total. Find a marked input.

Classically: $O(N/M)$ queries (check inputs one by one). Quantumly: $O(\sqrt{N/M})$ queries. Quadratic speedup.

### Two subspaces

Define two states:

$$|\text{good}\rangle = \frac{1}{\sqrt{M}} \sum_{x: f(x)=1} |x\rangle, \quad |\text{bad}\rangle = \frac{1}{\sqrt{N-M}} \sum_{x: f(x)=0} |x\rangle$$

The initial uniform superposition lies in the plane spanned by these two states:

$$|s\rangle = \sin\theta\,|\text{good}\rangle + \cos\theta\,|\text{bad}\rangle$$

where $\sin\theta = \sqrt{M/N}$. For $M \ll N$ (a needle in a haystack), $\theta$ is small — the initial state is almost entirely $|\text{bad}\rangle$.

### The Grover iterator as a rotation

The Grover iterator $G$ consists of two reflections:

1. **Oracle reflection** $S_f$: flip the phase of marked states. $S_f|x\rangle = (-1)^{f(x)}|x\rangle$. This is phase kickback from Chapter 4 — the oracle marks solutions by flipping their phase.

2. **Diffusion** $S_0 = 2|s\rangle\langle s| - I$: reflect about the mean amplitude. In circuit terms: $H^{\otimes n} \cdot (2|0\rangle\langle 0| - I) \cdot H^{\otimes n}$.

Two reflections make a rotation. $G = S_0 \cdot S_f$ rotates the state by angle $2\theta$ toward $|\text{good}\rangle$ in the 2D plane:

$$G^k|s\rangle = \sin((2k+1)\theta)\,|\text{good}\rangle + \cos((2k+1)\theta)\,|\text{bad}\rangle$$

After $k_\text{opt} = \lfloor \pi / (4\theta) \rfloor$ iterations, the state is nearly $|\text{good}\rangle$. Measure → get a marked item with probability $\geq 1 - O(M/N)$.

> **The key insight:** Grover doesn't search. It *rotates*. The search space isn't explored one item at a time — the quantum state rotates continuously from "mostly bad" to "mostly good." The number of rotations needed is $O(1/\theta) = O(\sqrt{N/M})$.

### The oracle circuit

For the financial application (Chapter 9), the oracle marks states where the stock price exceeds the strike: $f(x) = 1$ if $\text{price}(x) > K$.

This is a **comparator circuit**: given a quantum register encoding a discretised price, flip an ancilla if the price exceeds a threshold. The ancilla, prepared in $|{-}\rangle$, converts the flip to a phase via kickback — the same trick from Chapter 4.

### The diffusion circuit

The diffusion operator $2|s\rangle\langle s| - I$ is implemented as:

```
h q[0]; h q[1]; ... h q[n-1];      // Map |s⟩ → |0⟩
x q[0]; x q[1]; ... x q[n-1];      // Map |0⟩ → |1...1⟩
// Multi-controlled Z (phase flip on |1...1⟩)
h q[n-1];
// Toffoli chain
cx q[n-2], q[n-1]; ... 
h q[n-1];
x q[0]; x q[1]; ... x q[n-1];      // Undo
h q[0]; h q[1]; ... h q[n-1];      // Undo
```

This is the most gate-intensive part of Grover's algorithm, but it's a fixed overhead per iteration.

---

## From Grover to amplitude estimation

### The connection

Grover's algorithm uses $G$ to *find* marked items. But the angle $\theta$ — which determines how many iterations are needed — also encodes the *fraction* of marked items: $\sin^2\theta = M/N$.

**Quantum Amplitude Estimation** (QAE) extracts $\theta$ directly, without finding any specific marked item. This is exactly what we need for Monte Carlo pricing: we don't want a specific market scenario, we want the *probability* of favourable scenarios (which encodes the expected payoff).

### QPE on the Grover operator

The Grover iterator $G$ has eigenvalues $e^{\pm 2i\theta}$. Quantum Phase Estimation (Chapter 4) extracts eigenvalues. Apply QPE to $G$:

1. Prepare ancilla qubits in $|+\rangle$ (via Hadamard)
2. Apply controlled-$G^{2^k}$ operations (controlled by ancilla qubit $k$)
3. Apply inverse QFT to the ancillas
4. Measure → get an estimate of $\theta$

From $\theta$: compute $\tilde{a} = \sin^2\theta \approx M/N$. This is the amplitude (probability) we want.

### The convergence advantage

With $m$ ancilla qubits, QPE estimates $\theta$ to precision $O(1/2^m)$. This requires $O(2^m)$ applications of the Grover operator $G$.

Each application of $G$ is one "query" to the oracle. So:

- **Precision $\epsilon$** requires $O(1/\epsilon)$ queries
- **Classical Monte Carlo** requires $O(1/\epsilon^2)$ samples for the same precision

The quadratic advantage: same accuracy, quadratically fewer queries.

| Target precision | Classical samples | Quantum queries | Speedup |
|:---|:---|:---|:---|
| $10^{-1}$ | 100 | 10 | 10× |
| $10^{-3}$ | $10^6$ | $10^3$ | 1,000× |
| $10^{-6}$ | $10^{12}$ | $10^6$ | $10^6$× |

---

## What you should take away

1. **Grover's algorithm is a rotation, not a search.** It rotates the quantum state from "mostly wrong" to "mostly right" in the 2D good/bad plane. The number of rotations is $O(\sqrt{N/M})$.

2. **Amplitude estimation = QPE on Grover.** The angle $\theta$ that controls Grover encodes the probability $\sin^2\theta = M/N$. QPE extracts $\theta$ with precision $O(1/2^m)$ using $O(2^m)$ queries.

3. **The quadratic speedup is $1/\epsilon$ vs. $1/\epsilon^2$.** This transforms Monte Carlo from "days on a cluster" to "seconds on a quantum computer" for high-precision estimates.

4. **Phase kickback appears again.** The oracle uses it (Chapter 4). The Grover iterator uses it. QPE uses it. It's the same mechanism at every level.

5. **The circuit depth is the bottleneck.** QAE requires $O(1/\epsilon)$ sequential applications of the full Grover operator. Each application includes the oracle circuit. For useful precision, this means deep circuits — a fault-tolerant algorithm.
