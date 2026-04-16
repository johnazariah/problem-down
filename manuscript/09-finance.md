# Unit 5: Finance — *Pricing the Unpriceable*


## The Hook

In 2008, the financial crisis taught the world that mispriced **derivatives** — financial contracts whose value derives from an underlying asset like a stock, a bond, or an interest rate — can destroy economies. At the heart of the crisis were *exotic options*: contracts that give the holder the right to buy or sell an asset at a fixed price on a future date, but with complex conditions that make them hard to value.

Pricing a derivative means answering one question: **what is the expected payoff** — the profit (if any) the contract delivers at maturity? For a simple **European call option** (the right to buy a stock at a fixed price, exercisable only at maturity), there's an analytical formula (Black-Scholes, 1973). For exotic options — path-dependent, multi-asset, with early exercise features — there is no formula. The standard method is **Monte Carlo simulation**: generate millions of random market scenarios, compute the payoff for each, and take the average.

Monte Carlo works, but it's slow. The statistical error (the uncertainty in your price estimate) shrinks as $1/\sqrt{N}$ where $N$ is the number of samples. To get one more digit of accuracy, you need **100 times more samples**. For complex derivatives that take seconds per sample, this translates to hours or days of computation. Banks run massive compute clusters to price their portfolios overnight. Goldman Sachs reportedly runs over a billion Monte Carlo simulations *per day*.

The $1/\sqrt{N}$ convergence rate isn't a software limitation. It's a mathematical theorem: for classical random sampling, you *cannot* do better than $1/\sqrt{N}$. It's a fundamental limit.

Unless you're quantum.


## The Bottleneck

The mathematical structure is clean. You have a **random variable** $X$ — a quantity whose value depends on a random outcome; here, the derivative's payoff under a randomly sampled market scenario — with expected value $\mu = \mathbb{E}[X]$ (the probability-weighted average of all possible outcomes). You want to estimate $\mu$.

Classical Monte Carlo: draw $N$ independent samples $X_1, \ldots, X_N$ and compute the sample mean $\bar{X} = \frac{1}{N}\sum_i X_i$. The error in this estimate shrinks as:

$$|\bar{X} - \mu| \sim \frac{\sigma}{\sqrt{N}}$$

where $\sigma$ is the **standard deviation** (a measure of how spread out the payoff values are). To halve the error, quadruple $N$. To gain a factor of 10 in precision, multiply $N$ by 100. This $1/\sqrt{N}$ convergence rate is a mathematical theorem, not a software limitation — for any estimator based on independent classical samples, you *cannot* do better.

For a derivative that needs 6 digits of accuracy ($10^{-6}$ relative error) with $\sigma \sim 1$: you need $N \sim 10^{12}$ samples. At 1 microsecond per sample, that's 12 days.


## The Quantum Angle

### Amplitude amplification: Grover as a subroutine

Before we get to financial pricing, we need the tool that makes it possible: **amplitude amplification**, which is Grover's search algorithm generalised.

Grover's algorithm (1996) solves unstructured search: given a function $f:\{0,1\}^n \to \{0,1\}$ with $M$ solutions among $N = 2^n$ inputs, find a solution. Classically: $O(N/M)$ queries. Quantumly: $O(\sqrt{N/M})$ queries. A quadratic speedup.

The key operation is the **Grover iterator** $G = S_0 \cdot S_f$, where $S_f$ flips the phase of solutions and $S_0$ reflects about the initial superposition. Geometrically, $G$ is a rotation in the 2D subspace spanned by "solutions" and "non-solutions." Each application rotates the state vector by an angle $2\theta$ toward the solution space, where $\sin\theta = \sqrt{M/N}$.

After $k = O(\sqrt{N/M})$ iterations, the overlap with the solution space is close to 1. Measure, and you get a solution with high probability.

### Quantum amplitude estimation

Now the key insight: the *angle* $\theta$ encodes $M/N$; the fraction of inputs that are solutions. If you can measure $\theta$ precisely, you can estimate $M/N$ without ever finding a specific solution.

**Quantum Amplitude Estimation** (QAE) does exactly this. It uses the same controlled-powers-plus-inverse-QFT pattern we built in Deep-Dive 2 for period-finding — that pattern is called **Quantum Phase Estimation** (QPE), and it works for *any* unitary operator, not just the modular exponentiation oracle from Shor's algorithm. Here we apply QPE to the Grover iterator $G$. The eigenvalues of $G$ are $e^{\pm 2i\theta}$, and QPE extracts $\theta$ with precision $O(1/N_{\text{queries}})$ — that's $1/N$, not $1/\sqrt{N}$.

Applied to Monte Carlo:

1. **Encode** the probability distribution as a quantum state: prepare $\sum_x \sqrt{p(x)}|x\rangle$
2. **Compute** the payoff function: mark states where the payoff exceeds a threshold (this is the "oracle" for Grover)
3. **Run QAE**: extract the amplitude $a = \sqrt{\Pr[\text{payoff} > \text{threshold}]}$
4. The expected payoff is encoded in $a$, estimated to precision $\epsilon$ using $O(1/\epsilon)$ queries

Classical Monte Carlo: precision $\epsilon$ requires $O(1/\epsilon^2)$ samples.
Quantum amplitude estimation: precision $\epsilon$ requires $O(1/\epsilon)$ queries.

**Same accuracy, quadratically fewer samples.** For the derivative that needs $10^{12}$ classical samples: quantum estimation needs $10^6$ queries. At the same time per query, that's 1 second instead of 12 days.

### When does $\sqrt{}$ matter?

A quadratic speedup sounds modest compared to Shor's exponential speedup. But for Monte Carlo, quadratic is transformative. The reason: the baseline is *already polynomial* (Monte Carlo is $O(1/\epsilon^2)$), and the constant factors are large. Going from $10^{12}$ to $10^6$ is the difference between "we need a compute cluster" and "we need a laptop."


## Worked Example

Price a European call option using quantum amplitude estimation. Compare the convergence rate with classical Monte Carlo.

Setup:
- Stock price $S_0 = 100$, strike price $K = 105$ (the fixed price at which the option can be exercised), volatility $\sigma = 20\%$ (the annualised standard deviation of the stock's returns — how wildly the price swings), maturity $T = 1$ year (the date when the option expires), risk-free rate $r = 5\%$ (the return on a riskless investment, like a government bond)
- Payoff: $\max(S_T - K, 0)$
- Black-Scholes analytical price: ~$8.02

We discretise the stock price into $2^n$ bins, encode the **log-normal distribution** (stock prices are modelled so that their logarithm follows a normal distribution, ensuring prices can't go negative) as a quantum state, and use the Grover oracle to mark states where $S_T > K$.

→ *The next chapter builds the amplitude estimation circuit from Grover's algorithm, and shows you the code.*

### Back to the trading floor

We priced a European call option — the simplest derivative there is. How does this help Goldman Sachs price exotic instruments?

The pipeline is identical. A more complex derivative has a more complex payoff function (path-dependent, multi-asset, with barriers and early exercise), but the quantum algorithm doesn't care: it just needs an oracle that marks states where the payoff exceeds a threshold, and QAE estimates the probability. The quadratic speedup applies regardless of the payoff's complexity. For Goldman's billion-simulation-per-day workload, the gap between $10^{12}$ classical samples and $10^6$ quantum queries is the gap between a compute cluster and a single machine.


## Reality Check

**What's been demonstrated.** Goldman Sachs and IBM published a series of papers (2019–2021) on quantum amplitude estimation for derivative pricing, demonstrating the algorithm on simulators for simple options. Actual quantum hardware experiments have been limited to toy models (2–4 qubits, highly simplified distributions).

**The depth problem.** QAE requires quantum phase estimation, which requires deep circuits: $O(1/\epsilon)$ applications of the Grover iterator. For useful precision ($\epsilon \sim 10^{-3}$), that's thousands of sequential operations, each involving the full oracle circuit. On NISQ devices with short coherence times, this is currently infeasible.

**Approximate QAE.** Variants like iterative QAE (Suzuki et al. 2020) and maximum likelihood QAE reduce the circuit depth at the cost of more measurements. These are more NISQ-friendly but haven't demonstrated practical advantage.

**What would change the picture.** Fault-tolerant quantum computers with $O(10^3)$ logical qubits and the ability to run circuits of depth $O(10^4)$. The financial industry is actively investing: JP Morgan, Goldman Sachs, BBVA, and others have quantum computing research teams focused on this exact application.

**The quadratic wall.** A quadratic speedup means quantum advantage arrives only above a certain problem size, where the improved scaling overcomes the overhead of quantum error correction. For Monte Carlo, estimates suggest this crossover requires $10^3$–$10^4$ logical qubits; ambitious but within the scope of hardware roadmaps.


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
