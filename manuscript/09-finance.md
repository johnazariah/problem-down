# Unit 5: Finance — *Pricing the Unpriceable*


## The Hook

In 2008, the financial crisis taught the world that mispriced **derivatives** — financial contracts whose value derives from an underlying asset like a stock, a bond, or an interest rate — can destroy economies. At the heart of the crisis were *exotic options*: contracts that give the holder the right to buy or sell an asset at a fixed price on a future date, but with complex conditions that make them hard to value.

Pricing a derivative means answering one question: **what is the expected payoff** — the profit (if any) the contract delivers at maturity? For a simple **European call option** (the right to buy a stock at a fixed price, exercisable only at maturity), there's an analytical formula (Black-Scholes, 1973). For exotic options — path-dependent, multi-asset, with early exercise features — there is no formula. The standard method is **Monte Carlo simulation**: generate many random market scenarios, compute the payoff for each, and take the average.

Monte Carlo works, but it's slow. The statistical error (the uncertainty in your price estimate) shrinks as $1/\sqrt{N}$ where $N$ is the number of samples. To get one more digit of accuracy, you need **100 times more samples**. For complex derivatives with expensive path simulation, this translates to substantial overnight compute budgets across large portfolios.

The $1/\sqrt{N}$ convergence rate isn't a software limitation. For generic random sampling — estimating the mean of an arbitrary distribution from independent samples — you *cannot* do better than $1/\sqrt{N}$. (Structured classical techniques like variance reduction and quasi-Monte Carlo can improve performance for specific problems, but they don't change the fundamental scaling.)

Unless you're quantum.


## The Bottleneck

The mathematical structure is clean. You have a **random variable** $X$ — a quantity whose value depends on a random outcome; here, the derivative's payoff under a randomly sampled market scenario — with expected value $\mu = \mathbb{E}[X]$ (the probability-weighted average of all possible outcomes). You want to estimate $\mu$.

Classical Monte Carlo: draw $N$ independent samples $X_1, \ldots, X_N$ and compute the sample mean $\bar{X} = \frac{1}{N}\sum_i X_i$. The error in this estimate shrinks as:

$$|\bar{X} - \mu| \sim \frac{\sigma}{\sqrt{N}}$$

where $\sigma$ is the **standard deviation** (a measure of how spread out the payoff values are). To halve the error, quadruple $N$. To gain a factor of 10 in precision, multiply $N$ by 100. This $1/\sqrt{N}$ convergence rate is a mathematical fact about generic sampling, not a software limitation — for any estimator based on independent classical samples from an arbitrary distribution, you *cannot* do better.

For a normalised problem targeting additive accuracy around $10^{-6}$ with $\sigma \sim 1$: you need $N \sim 10^{12}$ samples. At 1 microsecond per sample, that's about 12 days.


## The Quantum Angle

### Amplitude amplification: Grover as a subroutine

Before we get to financial pricing, we need the tool that makes it possible: **amplitude amplification**, which is Grover's search algorithm generalised.

Here's the idea. Imagine you have a bag of $N$ balls, $M$ of which are gold. Classical approach: draw balls one at a time, check each one. On average you need $N/M$ draws to find a gold ball.

Grover's algorithm (1996) does this quantumly with only $\sqrt{N/M}$ queries — a quadratic speedup. It works not by checking balls faster, but by *rotating* the quantum state. Think of it geometrically: the quantum state starts pointing mostly toward "non-gold" and Grover's algorithm rotates it, step by step, toward "gold." Each step rotates by a fixed angle $2\theta$, where $\sin\theta = \sqrt{M/N}$. After about $\pi/(4\theta)$ rotations, the state points almost entirely at "gold." Measure, and you get a gold ball with near-certainty.

The rotation is implemented by the **Grover iterator** $G$, which applies two reflections that together produce a rotation. Deep-Dive 5 builds $G$ from gates; here we just need the geometric picture.

### From search to estimation

Now the key insight. The rotation angle $\theta$ itself encodes the answer to a different question: *what fraction of balls are gold?* Since $\sin\theta = \sqrt{M/N}$, measuring $\theta$ precisely gives you $M/N$ — without ever finding a specific gold ball.

**Quantum Amplitude Estimation** (QAE) measures $\theta$. It uses the same controlled-powers-plus-inverse-QFT pattern we saw in Unit 2 (Shor's algorithm) — that pattern is called **Quantum Phase Estimation** (QPE), and it works for any unitary operator. Here we apply it to the Grover iterator $G$, whose eigenvalues are $e^{\pm 2i\theta}$, and QPE extracts $\theta$ with precision $O(1/N_{\text{queries}})$ — that's $1/N$, not $1/\sqrt{N}$.

### Applying QAE to Monte Carlo

For derivative pricing, the "gold balls" are market scenarios, and the "fraction of gold" is generalised to the expected payoff. Specifically:

1. **Encode** the probability distribution as a quantum state: prepare $\sum_x \sqrt{p(x)}|x\rangle$
2. **Encode the payoff** into an ancilla amplitude: for each price state $|x\rangle$, rotate an ancilla qubit so that its amplitude encodes the (normalised) payoff $f(x)$. The combined state becomes $\sum_x \sqrt{p(x)}|x\rangle\bigl(\sqrt{1-f(x)}|0\rangle + \sqrt{f(x)}|1\rangle\bigr)$
3. **Run QAE**: estimate the probability of measuring the ancilla in $|1\rangle$. This probability is $\sum_x p(x) \cdot f(x) = \mathbb{E}[f(X)]$ — the normalised expected payoff. Multiply by the payoff bound $P_{\max}$ to recover the actual expected payoff.
4. Precision $\epsilon$ requires $O(1/\epsilon)$ queries to the oracle

Classical Monte Carlo: precision $\epsilon$ requires $O(1/\epsilon^2)$ samples.
Canonical, phase-estimation-based quantum amplitude estimation: precision $\epsilon$ requires $O(1/\epsilon)$ oracle uses.

**Same target accuracy, quadratically fewer oracle calls.** For the normalised back-of-the-envelope above, $10^{12}$ classical samples becomes about $10^6$ quantum oracle uses. That is the asymptotic gain. Whether it becomes a wall-clock advantage depends on the cost of state preparation, payoff encoding, and fault tolerance.

```{figure} ../figures/qae-scaling.png
:name: fig-qae-scaling
:alt: Scaling comparison showing classical Monte Carlo with 1 over square root N convergence and quantum amplitude estimation with 1 over N convergence.

Monte Carlo is already useful, so the point of QAE is not a new problem class but a quadratic reduction in the number of samples needed for the same precision.
```

### When does $\sqrt{}$ matter?

A quadratic speedup sounds modest compared to Shor's exponential speedup. But for Monte Carlo, it is exactly the relevant asymptotic improvement: from $O(1/\epsilon^2)$ to $O(1/\epsilon)$. The open question is not whether that query-complexity gain exists; it does. The open question is whether a full fault-tolerant pricing oracle can realise it before implementation overhead erases the advantage.


## Worked Example

Price a European call option classically, then use a compiled **toy amplitude-estimation phase readout** for a discretised exercise-probability proxy. Compare the classical $1/\sqrt{N}$ convergence with the projected quantum $1/N$ scaling, and make the simplification explicit.

Setup:
- Stock price $S_0 = 100$, strike price $K = 105$ (the fixed price at which the option can be exercised), volatility $\sigma = 20\%$ (the annualised standard deviation of the stock's returns — how wildly the price swings; this is the same $\sigma$ from the Bottleneck, now applied specifically to stock returns), maturity $T = 1$ year (the date when the option expires), risk-free rate $r = 5\%$ (the return on a riskless investment, like a government bond)
- Payoff: $\max(S_T - K, 0)$
- Black-Scholes analytical price: ~$8.02

We discretise the stock price into $2^n$ bins, encode the **log-normal distribution** (stock prices are modelled so that their logarithm follows a normal distribution, ensuring prices can't go negative) as a quantum state, and rotate an ancilla to encode the normalised payoff $\max(S_T - K, 0) / P_{\max}$ into its amplitude. QAE then estimates the normalised expected payoff; multiplying by $P_{\max}$ gives the option price.

(The companion notebook keeps the pricing pipeline honest by splitting the problem in two: classical Black-Scholes and Monte Carlo for the actual option price, then a compiled toy amplitude-estimation circuit for the **discretised exercise probability**. It does **not** encode the full continuous payoff into amplitudes; the full payoff-encoding construction described above remains the standard approach for pricing continuous payoffs.)

→ *The next chapter builds the amplitude estimation circuit from Grover's algorithm, and shows you the code.*

### Back to the trading floor

We priced a European call option — the simplest derivative there is. How does this help price exotic instruments?

The pipeline is structurally similar. A more complex derivative has a more complex payoff function (path-dependent, multi-asset, with barriers and early exercise), and QAE still estimates the expected value by reading out an ancilla amplitude. But the oracle does care: state preparation, path dependence, arithmetic, and payoff logic all get more expensive as the product gets more realistic. The quadratic speedup survives at the query-complexity level; practical advantage depends on the total cost of that oracle.


## Reality Check

**What's been demonstrated.** Goldman Sachs and IBM published a series of papers (2019–2021) on quantum amplitude estimation for derivative pricing, including simulator studies for European, basket, Asian, and barrier options. The hardware demonstrations are still toy-scale: for example, Stamatopoulos et al. run a heavily discretised European-call experiment on three qubits using amplitude estimation without phase estimation and error mitigation.

**The depth problem.** QAE requires quantum phase estimation, which requires deep circuits: $O(1/\epsilon)$ applications of the Grover iterator. For useful precision ($\epsilon \sim 10^{-3}$), that's thousands of sequential operations, each involving the full oracle circuit. On NISQ devices with short coherence times, this is currently infeasible.

**Approximate QAE.** Variants like iterative QAE and maximum-likelihood / no-phase-estimation QAE reduce the circuit depth at the cost of more measurements. Suzuki et al. show that this can preserve the quadratic query improvement while substantially reducing gate counts in a Monte Carlo integration example. That improves implementability, but it does not by itself settle the full economic crossover for real pricing workloads.

**What would change the picture.** Fault-tolerant quantum computers able to run long coherent pricing oracles repeatedly, with enough clean workspace for state preparation, payoff arithmetic, and amplitude estimation. The missing ingredient is not just "more qubits" in the abstract, but reliable depth across the whole oracle.

**The quadratic wall.** A quadratic speedup means quantum advantage arrives only above a certain problem size, where the improved scaling overcomes oracle-construction and error-correction overhead. The option-pricing literature gives evidence for a query-count crossover on simplified models, but it does **not** yet pin this down to a settled full-stack threshold like "a few thousand logical qubits."

**What's real today:** The algorithm is sound and the quadratic speedup is mathematically proven. But the circuits are too deep for current hardware, and whether amplitude estimation beats the best classical finance stack after full fault-tolerant overhead remains open.


## Chef's Notes

- **Grover's algorithm appears here, not as a standalone topic.** Most books introduce Grover as "quantum search"; finding a needle in a haystack. That's correct but unrelatable. Here, Grover appears as a *subroutine* inside amplitude estimation, motivated by a real computational bottleneck ($1/\sqrt{N}$ convergence). The speedup matters because Monte Carlo is everywhere, not because search is theoretically interesting.

- **The quadratic speedup is the most common quantum advantage.** Exponential speedups (Shor, simulation) get the headlines, but quadratic speedups (Grover, amplitude estimation) apply to a much broader class of problems. Anywhere you're sampling, searching, or optimising, a quadratic improvement is potentially available.

- **Connection to Unit 2.** QAE uses QPE, which uses the QFT; the same machinery from Shor's algorithm. The quantum ingredient is the same: extract a quantity (a period, an eigenvalue, an amplitude) encoded in the *phase* of a quantum state.

- **Further reading:**
    - Montanaro (2015). *Quantum speedup of Monte Carlo methods.* [arXiv:1504.06987](https://arxiv.org/abs/1504.06987)
    - Stamatopoulos, Egger, Sun, et al. (2020). *Option pricing using quantum computers.* [Quantum 4:291](https://doi.org/10.22331/q-2020-07-06-291)
    - Suzuki, Uno, Raymond, et al. (2020). *Amplitude estimation without phase estimation.* [Quantum Information Processing 19:75](https://doi.org/10.1007/s11128-019-2565-2)
    - Grover (1996). *A fast quantum mechanical algorithm for database search.* [arXiv:quant-ph/9605043](https://arxiv.org/abs/quant-ph/9605043)
    - 3Blue1Brown (2023). [*Grover's algorithm visually explained*](https://www.youtube.com/watch?v=KeJqcnpPluc) (YouTube video)
