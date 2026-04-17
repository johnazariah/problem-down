# Unit 4: Machine Learning — *10⁸ Features and Counting*


## The Hook

In 2006, Netflix offered a $1 million prize to anyone who could improve their movie recommendation algorithm by 10%. The winning team needed three years and a blend of over 100 different algorithms to get there. The core challenge wasn't the prize; it was the **dimensionality** of the problem.

Netflix had roughly 480,000 users and 18,000 movies. Each user-movie pair is a potential data point. The "feature space" that recommendation algorithms operate in has dimensions proportional to the number of users times the number of features describing each user's preferences. Modern recommendation engines at companies like Spotify, TikTok, and Amazon operate in feature spaces with $10^8$ or more dimensions.

Machine learning at scale is fundamentally a problem of high-dimensional geometry. A classifier draws a boundary in feature space separating "cat" from "dog," "spam" from "not spam," "buy" from "don't buy." The more dimensions, the more expressive the boundary can be; but the harder it is to find.

**Kernel methods** are the mathematical engine behind this. A kernel function $K(x, x')$ computes the similarity between two data points — effectively computing an inner product in a high-dimensional (possibly infinite-dimensional) feature space *without ever explicitly constructing that space*. This is the famous **kernel trick**, and it's what makes **Support Vector Machines** (SVMs) powerful: an SVM finds the boundary that maximises the *margin* (the gap between the boundary and the nearest data points of each class), and it needs only kernel values — pairwise similarities — not the raw feature vectors.

But some useful feature spaces are so large that even the kernel trick breaks down. The computation of certain kernels scales poorly with the number of features or requires evaluating functions that are classically intractable.

A quantum computer operates natively in an exponentially large space; the Hilbert space of $n$ qubits has $2^n$ dimensions. What if that's the feature space?


## The Bottleneck

The kernel trick is effective: instead of mapping data into a high-dimensional space $\phi: x \mapsto \phi(x)$ and computing inner products $\langle \phi(x), \phi(x') \rangle$ explicitly, you compute $K(x, x') = \langle \phi(x), \phi(x') \rangle$ directly. The classifier never sees the high-dimensional representation; it only needs the kernel matrix $K_{ij} = K(x_i, x_j)$ over the training set.

The kernel trick works well when $K$ is cheap to compute. But consider:

- A feature map into a space of dimension $2^n$ (exponential in the number of input features)
- A kernel that requires sampling from a distribution that's hard to sample classically
- A learning task where the relevant structure lives in a space that has no efficient classical description

In these cases, the kernel trick doesn't help; you can't compute $K(x, x')$ efficiently, even though you never explicitly construct $\phi(x)$.

The question becomes: **are there feature maps whose kernels are hard to compute classically but easy to compute quantumly?** And if so, do they correspond to learning tasks anyone actually cares about?


## The Quantum Angle

### The Hilbert space as a feature space

The key geometric insight. A quantum computer with $n$ qubits operates in a Hilbert space of dimension $2^n$. Preparing a quantum state $|\phi(x)\rangle$ from classical data $x$ is a **quantum feature map**; it maps data into an exponentially large space, natively.

The inner product between two quantum states $|\phi(x)\rangle$ and $|\phi(x')\rangle$ is:

$$K(x, x') = |\langle \phi(x') | \phi(x) \rangle|^2$$

This is just the **Born rule** — the principle we've relied on since Unit 1: the probability of a measurement outcome equals the squared magnitude of its amplitude. Here, it gives us the probability of measuring $|\phi(x)\rangle$ and finding it in state $|\phi(x')\rangle$. A quantum computer can estimate this probability by preparing $|\phi(x)\rangle$, applying $U_{\phi(x')}^\dagger$, and measuring. The result is a kernel value.

If the feature map $|\phi(x)\rangle$ has no efficient classical simulation; if there's no way to compute $\langle \phi(x') | \phi(x) \rangle$ efficiently on a classical computer; then this quantum kernel is something genuinely new. The quantum computer is computing a similarity measure that a classical computer cannot.

### Quantum kernel estimation

The algorithm is straightforward:

1. **Encode** classical data point $x$ into a quantum state $|\phi(x)\rangle$ using a parameterised circuit $U_\phi(x)|0\rangle^n$
2. **Compute the kernel** $K(x_i, x_j) = |\langle 0^n | U_\phi(x_j)^\dagger U_\phi(x_i) | 0^n \rangle|^2$ by preparing $U_\phi(x_i)|0\rangle$, applying $U_\phi(x_j)^\dagger$, and measuring the probability of getting $|0\rangle^n$
3. **Build the kernel matrix** $K_{ij}$ over the training set (the labelled examples the algorithm learns from)
4. **Train a classical SVM** using this kernel matrix; the classical optimisation is the same as for any kernel SVM

The quantum computer is only used for step 2 — computing kernel values that are classically intractable. Everything else is classical. This encode → measure → classically-optimise pattern is the same variational architecture we saw in QAOA (Unit 1) and VQE (Unit 3) — the quantum computer evaluates a function that a classical computer cannot, and classical methods do the rest.

### When does this actually help?

This is the most contested question in quantum machine learning. There are three scenarios:

**Provable advantage exists** for *constructed* problems. Huang, Broughton, et al. (2022) showed that there exist classification tasks where quantum kernels achieve exponentially better accuracy than any classical learner using the same data; but these tasks are specifically designed around the structure of quantum circuits. They're real proofs of separation, but the tasks are artificial.

**Dequantisation results limit the advantage.** Tang (2019) showed that several claimed quantum ML speedups (for recommendation systems, principal component analysis — extracting the most important axes of variation in high-dimensional data) can be matched classically under certain conditions. The classical algorithms are "quantum-inspired"; they use similar sampling techniques. This doesn't kill quantum ML, but it narrows the territory where advantage can exist.

**The data loading bottleneck.** To use a quantum kernel, you need to encode classical data into quantum states. If the data has $N$ features, encoding typically requires $O(N)$ or $O(\text{poly}(N))$ gates. For $N = 10^6$ features (common in practice), this circuit is too deep for near-term hardware. Quantum ML advantage, if it exists for practical problems, likely requires either quantum data (data that's already quantum) or very compact encodings.

### What's the honest picture?

Quantum kernel methods are the most *rigorous* approach to quantum ML; they come with provable guarantees under specific conditions. But the conditions are narrow, and it's an open question whether natural (non-constructed) datasets exhibit the kind of structure that quantum kernels exploit.

The alternative: **variational quantum ML** (parameterised quantum circuits trained end-to-end as classifiers); is more heuristic. It's easier to run on near-term hardware but has weaker theoretical foundations and faces barren plateau problems at scale.


## Worked Example

We build a quantum kernel classifier for a synthetic 2D dataset: two classes arranged in a pattern (two interleaved spirals) that's separable by a quantum feature map but not by a linear classifier.

1. Generate synthetic data (two interleaved spirals, 100 points per class)
2. Define a quantum feature map: encode each 2D point $(x_1, x_2)$ into a 2-qubit state using parameterised rotations and entanglement
3. Compute the quantum kernel matrix by running circuits on Quokka
4. Train a classical SVM with the quantum kernel
5. Compare the decision boundary with a classical RBF (radial basis function) kernel, which measures similarity as a Gaussian that decays with distance: $K(x,x') = e^{-\gamma\|x - x'\|^2}$

On this dataset, the quantum kernel achieves ~95% classification accuracy — comparable to the classical RBF kernel. The decision boundaries look similar, which is the honest result: for this toy 2D problem, both kernels have enough expressive power. Whether a quantum kernel could outperform in higher dimensions depends on whether the data has structure that lives naturally in the entangled quantum feature space — and whether the encoding remains feasible. That's the open question the Reality Check addresses.

→ *The next chapter builds the quantum kernel pipeline from scratch, and shows you the code.*

### Back to the recommender

We started with Netflix's 480,000 users and $10^8$-dimensional preference space. Could a quantum kernel capture similarity between users that classical kernels miss?

In principle, yes — a quantum feature map encodes each user's preference vector into an exponentially large Hilbert space, and the Born rule computes a similarity measure that may be classically intractable. In practice, the obstacle is **data loading**: encoding a preference vector with $10^5$ features requires $10^5$ gates, far too deep for current hardware. For quantum kernels to reach Netflix scale, we'd need either much deeper circuits (fault-tolerant hardware) or data that's already quantum.

The more likely near-term path is smaller, harder problems: classifying outputs of quantum experiments, detecting phases of matter in quantum simulations, or analysing molecular fingerprints (connecting back to Unit 3). In these settings, the data has quantum structure that classical kernels can't access — and the feature vectors are naturally compact.


## Reality Check

**The quantum ML landscape is contentious.** Unlike factoring (where Shor's algorithm gives a clear exponential speedup) or molecular simulation (where the problem is inherently quantum), ML advantage is much harder to establish. The data is classical, the metrics are empirical, and classical baselines keep improving.

**What's been demonstrated.** Quantum kernel classifiers have been run on real hardware for small datasets (up to ~20 features, ~100 data points). Results match classical kernel SVMs; no advantage has been demonstrated on a practical dataset.

**The most promising direction** may not be kernel methods at all, but using quantum computers to generate or model data distributions that are hard to sample classically. **Generative models** — models that learn to *produce* new data resembling the training distribution, rather than classify existing data — are a natural fit. A **Born machine** treats the measurement probability distribution of a parameterised circuit as the model's output distribution; the Born rule becomes the generative engine. These can sample from distributions that require exponential classical resources, though whether those distributions are *useful* for real-world tasks is an open question.

**What would change the picture:** Discovery of a natural, practically important dataset where quantum kernels provably outperform all classical methods. Or fault-tolerant quantum computers that eliminate the data-loading bottleneck.

**Honest assessment:** Quantum ML is the most speculative application area in this book. We include it because the *ideas* are beautiful (Hilbert space as feature space, Born rule as kernel evaluator) and because the theoretical framework is sound; but the path to practical advantage is less clear than for any other unit.


## Chef's Notes

- **Hilbert space as feature space** is a genuinely deep idea. It reframes quantum mechanics geometrically: a quantum state *is* a point in a high-dimensional vector space, and measurement *is* an inner product. If you've ever wondered "what's quantum mechanics good for besides physics?"; this is the cleanest answer: it gives you a feature space that's exponentially large and natively available.

- **Connection to Unit 1 (Logistics).** The quantum kernel circuit — parameterised gates, entanglement, measurement — is structurally identical to a QAOA layer. In Unit 1, we optimised the *parameters*; here the parameters are fixed by the *data*. Same hardware, different purpose.

- **The Born rule as a kernel evaluator.** In Unit 2, we used measurement to extract periodicity. In Unit 3, we used it to estimate energy. Here we use it to compute similarity. Same physical operation (measurement), different computational purpose. This is the versatility of quantum mechanics as a computational resource.

- **Connection to Unit 5 (Finance).** Quantum sampling; preparing and measuring quantum states to sample from hard distributions; appears in both quantum ML (generative models) and quantum finance (Monte Carlo). The underlying resource is the same: quantum mechanics lets you sample from distributions that are classically intractable.

- **Why we include this unit despite the uncertainty.** ML is what most readers will want to hear about. The theoretical framework is honest and rigorous, and the Reality Check is where we earn trust by *not* overpromising. A book that dodges quantum ML looks like it's hiding something.

- **Further reading:**
    - Havlíček, Córcoles, Temme, et al. (2019). *Supervised learning with quantum-enhanced feature spaces.* [Nature 567:209–212](https://doi.org/10.1038/s41586-019-0980-2) ([arXiv:1804.11326](https://arxiv.org/abs/1804.11326))
    - Huang, Broughton, Mohseni, et al. (2022). *Power of data in quantum machine learning.* [Nature Communications 12:2631](https://doi.org/10.1038/s41467-021-22539-9)
    - Tang (2019). *A quantum-inspired classical algorithm for recommendation systems.* [STOC 2019](https://doi.org/10.1145/3313276.3316310) ([arXiv:1807.04271](https://arxiv.org/abs/1807.04271))
    - Schuld and Killoran (2019). *Quantum Machine Learning in Feature Hilbert Spaces.* [Physical Review Letters 122:040504](https://doi.org/10.1103/PhysRevLett.122.040504) ([arXiv:1803.07128](https://arxiv.org/abs/1803.07128))
    - Mohanty, Behera & Ferrie (2024). *Solving the vehicle routing problem via quantum support vector machines.* [Quantum Machine Intelligence 6:27](https://doi.org/10.1007/s42484-024-00161-4)
    - Nair & Ferrie (2025). *Local surrogates for quantum machine learning.* [arXiv:2506.09425](https://arxiv.org/abs/2506.09425)
