# Unit 4: Machine Learning — *10⁸ Features and Counting*

---

## The Hook

In 2006, Netflix offered a $1 million prize to anyone who could improve their movie recommendation algorithm by 10%. The winning team needed three years and a blend of over 100 different algorithms to get there. The core challenge wasn't the prize — it was the **dimensionality** of the problem.

Netflix had roughly 480,000 users and 18,000 movies. Each user-movie pair is a potential data point. The "feature space" that recommendation algorithms operate in has dimensions proportional to the number of users times the number of features describing each user's preferences. Modern recommendation engines at companies like Spotify, TikTok, and Amazon operate in feature spaces with $10^8$ or more dimensions.

Machine learning at scale is fundamentally a problem of high-dimensional geometry. A classifier draws a boundary in feature space separating "cat" from "dog," "spam" from "not spam," "buy" from "don't buy." The more dimensions, the more expressive the boundary can be — but the harder it is to find.

**Kernel methods** are the mathematical engine behind this. A kernel function $K(x, x')$ computes the similarity between two data points — effectively computing an inner product in a high-dimensional (possibly infinite-dimensional) feature space *without ever explicitly constructing that space*. This is the famous **kernel trick**, and it's what makes Support Vector Machines (SVMs) powerful.

But some useful feature spaces are so large that even the kernel trick breaks down. The computation of certain kernels scales poorly with the number of features or requires evaluating functions that are classically intractable.

A quantum computer operates natively in an exponentially large space — the Hilbert space of $n$ qubits has $2^n$ dimensions. What if that's the feature space?

---

## The Bottleneck

The kernel trick is elegant: instead of mapping data into a high-dimensional space $\phi: x \mapsto \phi(x)$ and computing inner products $\langle \phi(x), \phi(x') \rangle$ explicitly, you compute $K(x, x') = \langle \phi(x), \phi(x') \rangle$ directly. The classifier never sees the high-dimensional representation — it only needs the kernel matrix $K_{ij} = K(x_i, x_j)$ over the training set.

This works beautifully when $K$ is cheap to compute. But consider:

- A feature map into a space of dimension $2^n$ (exponential in the number of input features)
- A kernel that requires sampling from a distribution that's hard to sample classically
- A learning task where the relevant structure lives in a space that has no efficient classical description

In these cases, the kernel trick doesn't help — you can't compute $K(x, x')$ efficiently, even though you never explicitly construct $\phi(x)$.

The question becomes: **are there feature maps whose kernels are hard to compute classically but easy to compute quantumly?** And if so, do they correspond to learning tasks anyone actually cares about?

---

## The Quantum Angle

### The Hilbert space as a feature space

Here's the key geometric insight. A quantum computer with $n$ qubits operates in a Hilbert space of dimension $2^n$. Preparing a quantum state $|\phi(x)\rangle$ from classical data $x$ is a **quantum feature map** — it maps data into an exponentially large space, natively.

The inner product between two quantum states $|\phi(x)\rangle$ and $|\phi(x')\rangle$ is:

$$K(x, x') = |\langle \phi(x') | \phi(x) \rangle|^2$$

This is just the **Born rule** — the probability of measuring $|\phi(x)\rangle$ and finding it in state $|\phi(x')\rangle$. A quantum computer can estimate this probability by preparing $|\phi(x)\rangle$, applying $U_{\phi(x')}^\dagger$, and measuring. The result is a kernel value.

If the feature map $|\phi(x)\rangle$ has no efficient classical simulation — if there's no way to compute $\langle \phi(x') | \phi(x) \rangle$ efficiently on a classical computer — then this quantum kernel is something genuinely new. The quantum computer is computing a similarity measure that a classical computer cannot.

### Quantum kernel estimation

The algorithm is straightforward:

1. **Encode** classical data point $x$ into a quantum state $|\phi(x)\rangle$ using a parameterised circuit $U_\phi(x)|0\rangle^n$
2. **Compute the kernel** $K(x_i, x_j) = |\langle 0^n | U_\phi(x_j)^\dagger U_\phi(x_i) | 0^n \rangle|^2$ by preparing $U_\phi(x_i)|0\rangle$, applying $U_\phi(x_j)^\dagger$, and measuring the probability of getting $|0\rangle^n$
3. **Build the kernel matrix** $K_{ij}$ over the training set
4. **Train a classical SVM** using this kernel matrix — the classical optimisation is the same as for any kernel SVM

The quantum computer is only used for step 2 — computing kernel values that are classically intractable. Everything else is classical.

### When does this actually help?

This is the most contested question in quantum machine learning. There are three scenarios:

**Provable advantage exists** for *constructed* problems. Huang, Broughton, et al. (2022) showed that there exist classification tasks where quantum kernels achieve exponentially better accuracy than any classical learner using the same data — but these tasks are specifically designed around the structure of quantum circuits. They're real proofs of separation, but the tasks are artificial.

**Dequantisation results limit the advantage.** Tang (2019) showed that several claimed quantum ML speedups (for recommendation systems, principal component analysis) can be matched classically under certain conditions. The classical algorithms are "quantum-inspired" — they use similar sampling techniques. This doesn't kill quantum ML, but it narrows the territory where advantage can exist.

**The data loading bottleneck.** To use a quantum kernel, you need to encode classical data into quantum states. If the data has $N$ features, encoding typically requires $O(N)$ or $O(\text{poly}(N))$ gates. For $N = 10^6$ features (common in practice), this circuit is too deep for near-term hardware. Quantum ML advantage, if it exists for practical problems, likely requires either quantum data (data that's already quantum) or very compact encodings.

### What's the honest picture?

Quantum kernel methods are the most *rigorous* approach to quantum ML — they come with provable guarantees under specific conditions. But the conditions are narrow, and it's an open question whether natural (non-constructed) datasets exhibit the kind of structure that quantum kernels exploit.

The alternative — **variational quantum ML** (parameterised quantum circuits trained end-to-end as classifiers) — is more heuristic. It's easier to run on near-term hardware but has weaker theoretical foundations and faces barren plateau problems at scale.

---

## Worked Example

We build a quantum kernel classifier for a synthetic 2D dataset: two classes arranged in a pattern that's separable by a quantum feature map but not by a linear classifier.

1. Generate synthetic data (two interleaved spirals)
2. Define a quantum feature map: encode each 2D point $(x_1, x_2)$ into a 2-qubit state using parameterised rotations and entanglement
3. Compute the quantum kernel matrix by running circuits on Quokka
4. Train a classical SVM with the quantum kernel
5. Compare the decision boundary with a classical RBF kernel

→ **See [notebook `04-machine-learning.ipynb`](../notebooks/04-machine-learning.ipynb) for the runnable version.**

!!! lab "Lab 4: Quantum feature maps on your Quokka"
    The quantum kernel circuit is just parameterised rotations + entanglement + measurement. See [Quokka Cookbook — Recipe 01: Bell State](https://github.com/johnazariah/quokka-cookbook/recipes/01-bell-state/) for entanglement fundamentals, and the companion notebook for the full kernel computation.

---

## Deep Dive: Building a Quantum Kernel Classifier

*This section constructs the classifier step by step. Skip it if you want the application story only.*

### Designing a quantum feature map

A feature map $U_\phi(x)$ encodes a classical data point $x$ into a quantum state $|\phi(x)\rangle = U_\phi(x)|0\rangle^n$. The art is choosing $U_\phi$ so that:

1. The resulting kernel $K(x, x') = |\langle \phi(x') | \phi(x) \rangle|^2$ has no efficient classical computation
2. The kernel captures useful structure in the data

A common design (Havlíček et al. 2019):

```
// Layer 1: encode features
ry(x₁) q[0];
ry(x₂) q[1];

// Entangle
cx q[0], q[1];

// Layer 2: encode feature interactions
rz(x₁ · x₂) q[1];

// Disentangle
cx q[0], q[1];
```

The $R_Y$ gates encode individual features as rotation angles. The CNOT creates entanglement. The $R_Z(x_1 \cdot x_2)$ gate encodes a *nonlinear* feature interaction — this is where the quantum kernel goes beyond linear maps. You can repeat layers for richer feature maps.

### Computing the kernel value

For two data points $x$ and $x'$, the kernel is:

$$K(x, x') = |\langle 0^n | U_\phi(x')^\dagger U_\phi(x) | 0^n \rangle|^2$$

Circuit: apply $U_\phi(x)$, then $U_\phi(x')^\dagger$ (the adjoint — reverse the gates, negate the angles), then measure. The probability of getting $|0\rangle^n$ is $K(x, x')$.

```
// Apply U(x)
ry(x₁) q[0]; ry(x₂) q[1]; cx q[0], q[1]; rz(x₁·x₂) q[1]; cx q[0], q[1];

// Apply U†(x')
cx q[0], q[1]; rz(-x'₁·x'₂) q[1]; cx q[0], q[1]; ry(-x'₂) q[1]; ry(-x'₁) q[0];

// Measure
measure q[0] -> c[0]; measure q[1] -> c[1];
```

Run this $N_\text{shots}$ times. $K(x, x') \approx \text{count}(00) / N_\text{shots}$.

### Building the kernel matrix

For $m$ training points, you need all $m^2$ pairwise kernel values. That's $m^2$ circuit executions (each with many shots). For $m = 100$ and 1000 shots each: 10 million total measurements.

This is the **kernel matrix** $K_{ij} = K(x_i, x_j)$. It's symmetric and positive semi-definite (by construction — it's a Gram matrix of inner products).

### Training the SVM

Once you have $K$, the rest is classical. A support vector machine with a precomputed kernel solves:

$$\max_\alpha \sum_i \alpha_i - \frac{1}{2} \sum_{i,j} \alpha_i \alpha_j y_i y_j K_{ij}$$

subject to $0 \leq \alpha_i \leq C$ and $\sum_i \alpha_i y_i = 0$. This is a standard quadratic program — solved by `sklearn.svm.SVC(kernel='precomputed')` in one line.

The quantum computer only appears in the kernel computation. Everything else — the SVM training, prediction, cross-validation — is classical.

### When is the quantum kernel provably better?

Huang et al. (2022) showed: if the quantum feature map produces states that are indistinguishable from Haar-random states when viewed through classical measurements, then no classical learner can compute the same kernel. But this doesn't guarantee the kernel is *useful* for any particular dataset.

The provable separations are for **constructed** problems: classification tasks deliberately designed to align with the quantum feature map's structure. For natural datasets, no provable advantage has been demonstrated.

---

## Reality Check

**The quantum ML landscape is contentious.** Unlike factoring (where Shor's algorithm gives a clear exponential speedup) or molecular simulation (where the problem is inherently quantum), ML advantage is much harder to establish. The data is classical, the metrics are empirical, and classical baselines keep improving.

**What's been demonstrated.** Quantum kernel classifiers have been run on real hardware for small datasets (up to ~20 features, ~100 data points). Results match classical kernel SVMs — no advantage has been demonstrated on a practical dataset.

**The most promising direction** may not be kernel methods at all, but using quantum computers to generate or model data distributions that are hard to sample classically. Quantum generative models (like quantum circuit Born machines) can sample from distributions that require exponential resources classically. Whether these distributions are *useful* for real-world generative tasks is an open question.

**What would change the picture:** Discovery of a natural, practically important dataset where quantum kernels provably outperform all classical methods. Or fault-tolerant quantum computers that eliminate the data-loading bottleneck.

**Honest assessment:** Quantum ML is the most speculative application area in this book. We include it because the *ideas* are beautiful (Hilbert space as feature space, Born rule as kernel evaluator) and because the theoretical framework is sound — but the path to practical advantage is less clear than for any other unit.

---

## Chef's Notes

- **Hilbert space as feature space** is a genuinely deep idea. It reframes quantum mechanics geometrically: a quantum state *is* a point in a high-dimensional vector space, and measurement *is* an inner product. If you've ever wondered "what's quantum mechanics good for besides physics?" — this is the cleanest answer: it gives you a feature space that's exponentially large and natively available.

- **The Born rule as a kernel evaluator.** In Unit 2, we used measurement to extract periodicity. In Unit 3, we used it to estimate energy. Here we use it to compute similarity. Same physical operation (measurement), different computational purpose. This is the versatility of quantum mechanics as a computational resource.

- **Connection to Unit 5 (Finance).** Quantum sampling — preparing and measuring quantum states to sample from hard distributions — appears in both quantum ML (generative models) and quantum finance (Monte Carlo). The underlying resource is the same: quantum mechanics lets you sample from distributions that are classically intractable.

- **The SPEC.md open question.** Whether to keep this unit was flagged as an open question. We keep it — with strong caveats — because (a) ML is what most readers will want to hear about, (b) the theoretical framework is honest and rigorous, and (c) the Reality Check is where we earn trust by *not* overpromising. A book that dodges ML looks like it's hiding something.

- **Further reading:**
    - Havlíček, Córcoles, Temme, et al. (2019). *Supervised learning with quantum-enhanced feature spaces.* [Nature 567:209–212](https://doi.org/10.1038/s41586-019-0980-2)
    - Huang, Broughton, Mohseni, et al. (2022). *Power of data in quantum machine learning.* [Nature Communications 12:2631](https://doi.org/10.1038/s41467-021-22539-9)
    - Tang (2019). *A quantum-inspired classical algorithm for recommendation systems.* [STOC 2019](https://doi.org/10.1145/3313276.3316310)
    - Schuld and Killoran (2019). *Quantum Machine Learning in Feature Hilbert Spaces.* [Physical Review Letters 122:040504](https://doi.org/10.1103/PhysRevLett.122.040504)
