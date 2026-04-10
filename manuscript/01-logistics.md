# Unit 1: Logistics — *Saving $50 Million One Mile at a Time*

---

## The Hook

Every morning, 130,000 UPS drivers leave their depots. Each driver visits between 100 and 200 stops. The order they visit those stops determines how many miles they drive, how much fuel they burn, and whether they make it home for dinner.

In 2012, UPS deployed a system called ORION — On-Road Integrated Optimization and Navigation. Its job: take each driver's list of deliveries and produce a better route. Not a perfect route. Just a better one. ORION shaved an average of one mile off each driver's daily route.

One mile doesn't sound like much. But multiply by 130,000 drivers, 250 working days per year, and the cost of fuel, vehicle wear, and driver time. UPS reported savings of **$50 million per year** from that single mile.

Now consider what a *two*-mile improvement would be worth. Or five.

The problem is that finding the optimal route isn't just difficult — it's one of the hardest problems in all of computer science. If a driver has 20 stops, there are $20! = 2.4 \times 10^{18}$ possible orderings. That's 2.4 quintillion routes to check. A desktop computer evaluating one billion routes per second would need 77 years. For 50 stops, the number of possibilities exceeds the number of atoms in the observable universe.

This is the **Travelling Salesman Problem** (TSP), and it has tormented mathematicians, computer scientists, and logistics companies for over a century. Every exact algorithm for TSP has a running time that grows at least exponentially with the number of stops. There is strong theoretical evidence (though no proof) that no efficient exact algorithm exists — the problem is NP-hard.

In practice, nobody solves TSP exactly at scale. ORION doesn't find the best route; it finds a *pretty good* route, using heuristics that have been refined over decades. Branch-and-bound, genetic algorithms, simulated annealing, Lin-Kernighan — these are all sophisticated methods for exploring the vast space of possible routes without drowning in it.

They work remarkably well. But they all share a fundamental limitation: they explore the space of routes *one at a time*. They walk through the landscape of possible solutions, stepping from one candidate to a neighbouring one, hoping that local improvements lead to global ones. Sometimes they get stuck in valleys — solutions that are better than all their neighbours but far worse than the global optimum.

What if you could explore the entire landscape at once?

---

## The Bottleneck

Let's make the problem concrete. Strip away the geography and the delivery trucks, and what remains is pure combinatorics.

You have a graph — a set of cities (nodes) connected by roads (edges), each road with a cost (the distance). You want to visit every city exactly once and return to where you started, minimising the total cost. That's TSP.

For our purposes, let's start with something even simpler: **MaxCut**. Take a graph and colour every node either red or blue. An edge is "cut" if its endpoints have different colours. MaxCut asks: what colouring cuts the most edges?

MaxCut sounds like a toy problem, but it's NP-hard — just as hard as TSP in a complexity-theoretic sense. And it's beautifully suited to our purposes because it translates directly into the language of qubits.

Here's why MaxCut is hard. A graph with $n$ nodes has $2^n$ possible colourings. For each colouring, you can count the cut edges in $O(m)$ time, where $m$ is the number of edges. So the brute-force algorithm takes $O(m \cdot 2^n)$ time. For $n = 50$, that's roughly $10^{15}$ operations — doable but slow. For $n = 100$, it's $10^{30}$ operations. For $n = 300$, you'd need more time than the age of the universe.

The problem is the search space. Every node is a binary decision: red or blue, 0 or 1. The decisions interact — the value of your choice for node $i$ depends on what you chose for nodes $j$, $k$, $l$ — every node that shares an edge with $i$. These interactions create a rugged *cost landscape*: a function over $\{0,1\}^n$ with exponentially many local optima.

Classical heuristics navigate this landscape by making local moves. Flip one node's colour. If the cut count improves, keep it; otherwise, try another flip. Simulated annealing adds randomness — occasionally accept a worse solution to escape local optima, gradually reducing the randomness as you "cool down."

These methods are powerful, but they have a fundamental weakness: they explore the landscape *sequentially*. At any moment, they're sitting at a single point in the space of $2^n$ possible colourings. They can only see the immediate neighbourhood. A better solution might exist on the other side of a high barrier, and no amount of local flipping will find it.

This is where the story turns quantum.

---

## The Quantum Angle

What if, instead of sitting at one colouring and looking around, you could be at *all* $2^n$ colourings simultaneously, and then use interference to amplify the ones that cut more edges?

That's the core idea behind the **Quantum Approximate Optimization Algorithm** (QAOA), introduced by Farhi, Goldstone, and Gutmann in 2014. It's not a magic bullet — it won't solve NP-hard problems in polynomial time (nobody believes that's possible). But it offers a fundamentally different way to explore the solution landscape, one that exploits quantum mechanics in a structural way that classical algorithms cannot mimic.

### Qubits as binary decisions

Let's encode our MaxCut problem. Each node in the graph gets one qubit. A qubit in state $|0\rangle$ means "red"; $|1\rangle$ means "blue." An $n$-node graph requires $n$ qubits. A specific colouring — say, nodes 1 and 3 are blue, node 2 is red — corresponds to the computational basis state $|101\rangle$.

The key is that a qubit doesn't have to be $|0\rangle$ or $|1\rangle$. It can be in a *superposition*: $\alpha|0\rangle + \beta|1\rangle$, where $\alpha$ and $\beta$ are complex numbers with $|\alpha|^2 + |\beta|^2 = 1$. When you put $n$ qubits in superposition, the system can be in a superposition of all $2^n$ colourings simultaneously. We don't look at them all — measurement gives us one. But between preparation and measurement, we can manipulate the amplitudes to make good colourings more likely.

### The cost Hamiltonian

QAOA turns the MaxCut objective into a quantum operator — a **cost Hamiltonian** $C$.

For each edge $(i, j)$ in the graph, the number of cuts contributed by that edge is:

$$\frac{1 - Z_i Z_j}{2}$$

where $Z_i$ is the Pauli-$Z$ operator on qubit $i$. This expression equals 1 when qubits $i$ and $j$ have different values (the edge is cut) and 0 when they agree (the edge is not cut). The total cost Hamiltonian is:

$$C = \sum_{(i,j) \in E} \frac{1 - Z_i Z_j}{2}$$

The ground state of $-C$ (the state with lowest energy) is the colouring that maximises the cut. We've translated "find the best colouring" into "find the ground state of this operator." This is not just a mathematical trick — it's a change of perspective that opens the door to quantum mechanics.

### The QAOA circuit

QAOA works by applying two alternating operations:

1. **The problem unitary** $e^{-i\gamma C}$: this "imprints" the cost function onto the phases of the quantum state. Good colourings acquire different phases from bad ones. The parameter $\gamma$ controls how strongly the cost function influences the state.

2. **The mixer unitary** $e^{-i\beta B}$, where $B = \sum_i X_i$: this "mixes" the amplitudes between different colourings, allowing the algorithm to explore the solution space. The parameter $\beta$ controls how much mixing occurs.

One round of QAOA applies both operators in sequence:

$$|\gamma, \beta\rangle = e^{-i\beta B} \, e^{-i\gamma C} \, |+\rangle^n$$

where $|+\rangle^n$ is the equal superposition of all colourings (created by applying Hadamard gates to all qubits). You measure the qubits, and the colouring you get is your candidate solution.

The magic is in the interference. The problem unitary $e^{-i\gamma C}$ assigns phases proportional to the cost of each colouring. The mixer $e^{-i\beta B}$ then causes these phases to interfere — constructively for good solutions, destructively for bad ones. After several rounds of alternation, the probability of measuring a high-quality colouring increases.

### The variational loop

But how do you choose $\gamma$ and $\beta$? This is where QAOA becomes a **variational** algorithm — a quantum-classical hybrid:

1. Pick initial values of $\gamma$ and $\beta$
2. Run the quantum circuit, measure the output
3. Compute the expected cost (run many times, take the average)
4. Feed this cost to a classical optimiser (COBYLA, Nelder-Mead, gradient descent)
5. The optimiser suggests better values of $\gamma$ and $\beta$
6. Repeat until convergence

The quantum computer explores the solution space. The classical computer tunes the exploration strategy. Neither could do the other's job efficiently.

For deeper QAOA (more rounds of alternation, called $p$-depth QAOA), you have $2p$ parameters: $\gamma_1, \beta_1, \gamma_2, \beta_2, \ldots, \gamma_p, \beta_p$. In principle, as $p \to \infty$, QAOA can find the exact optimum. In practice, you use a small number of rounds and accept an approximate answer — hence "Approximate" in the name.

### How it becomes a circuit

Each ingredient has a direct circuit implementation:

- **Initial state:** Apply a Hadamard gate $H$ to every qubit → equal superposition $|+\rangle^n$
- **Problem unitary ($e^{-i\gamma C}$):** For each edge $(i,j)$, apply $\text{CNOT}(i,j) \cdot R_Z(2\gamma) \cdot \text{CNOT}(i,j)$. This implements $e^{-i\gamma Z_i Z_j}$.
- **Mixer ($e^{-i\beta B}$):** Apply $R_X(2\beta)$ to every qubit.
- **Measurement:** Measure all qubits in the computational basis.

The circuit depth grows linearly with the number of edges and the depth parameter $p$. For small graphs, this is entirely feasible on current quantum hardware.

---

## Worked Example

Let's solve MaxCut on a triangle — three nodes, three edges. The optimal cut is 2 (colour one node differently from the other two).

### The graph

```
    0
   / \
  1 — 2
```

Three nodes, three edges: (0,1), (0,2), (1,2). Each node gets one qubit.

### The cost Hamiltonian

$$C = \frac{1 - Z_0 Z_1}{2} + \frac{1 - Z_0 Z_2}{2} + \frac{1 - Z_1 Z_2}{2}$$

### The circuit (depth $p = 1$)

1. Apply $H$ to all three qubits → $|+\rangle^3$
2. For each edge, apply the $ZZ$ interaction with angle $\gamma$
3. Apply $R_X(2\beta)$ to each qubit
4. Measure

### Running it

Using pre-optimised parameters $\gamma = \pi/4$, $\beta = \pi/8$ (these are close to optimal for the triangle), the circuit produces the following measurement distribution:

| Outcome | Cut value | Probability |
|---------|-----------|-------------|
| 000 | 0 | ~3% |
| 001 | 2 | ~16% |
| 010 | 2 | ~16% |
| 011 | 2 | ~16% |
| 100 | 2 | ~16% |
| 101 | 2 | ~16% |
| 110 | 2 | ~16% |
| 111 | 0 | ~3% |

The colourings with cut value 2 (all the ones with exactly one or two bits different from the others) are amplified. The "all same" colourings ($000$, $111$) are suppressed. QAOA has shifted probability mass toward the optimal solutions.

For larger graphs, the companion notebook runs the full QAOA loop with classical parameter optimisation, comparing the quantum result with brute-force and random sampling.

→ **See [notebook `01-logistics.ipynb`](../notebooks/01-logistics.ipynb) for the runnable version.**

→ **See [Quokka Cookbook — Recipe 07: QAOA for MaxCut](https://github.com/johnazariah/quokka-cookbook/recipes/07-qaoa-maxcut/) for the QASM implementation you can run on your Quokka.**

---

## Reality Check

Let's be honest about where QAOA stands.

**The theoretical picture.** For depth-1 QAOA on MaxCut, Farhi, Goldstone, and Gutmann (2014) proved a guaranteed approximation ratio of 0.6924 for 3-regular graphs. The best classical polynomial-time algorithm (Goemans-Williamson, 1995) achieves 0.878. So at low depth, QAOA *underperforms* the best classical algorithm.

At higher depths, the picture improves — performance monotonically increases with $p$ — but optimising the $2p$ parameters becomes harder. The classical optimisation landscape develops its own ruggedness. And there's a deeper obstacle: **barren plateaus** (McClean et al. 2018). For random circuits on many qubits, the gradient of the cost function vanishes exponentially with system size. This doesn't necessarily kill QAOA (it has more structure than random circuits), but it's a serious concern.

**The experimental picture.** QAOA has been demonstrated on trapped-ion and superconducting hardware for graphs up to ~20 nodes. Results roughly match simulator predictions after error mitigation. But no experiment has yet shown a practical advantage over classical solvers on a problem anyone cares about.

**The competitive landscape.** The best classical heuristics for MaxCut and graph problems are *very* good. Breakout Local Search (BLS), tabu search, and semi-definite programming relaxations are hard to beat. QAOA would need to reach high depth on large graphs — requiring deep circuits with low error rates — to be competitive. Current estimates (Guerreschi and Matsuura 2019) suggest quantum advantage for MaxCut would require thousands of qubits with error rates orders of magnitude below current hardware.

**What's real today:** QAOA is a proof of concept, not a production tool. It definitively demonstrates that combinatorial optimisation problems *can* be encoded into quantum circuits and that the variational approach works mechanically. The algorithm is correct; the hardware isn't ready.

**What would change the picture:** Fault-tolerant quantum computers with $\sim 10^4$ logical qubits would enable high-depth QAOA on industrially relevant graphs. Alternatively, better initialisation strategies, problem-specific ansätze, or recursive QAOA variants could reduce the depth requirements.

---

## Chef's Notes

- **MaxCut is a gateway drug.** We used it here because it maps directly to qubits ($Z_i Z_j$ interactions), but the QAOA framework applies to *any* combinatorial optimisation problem you can write as a cost function over binary variables. Scheduling, bin packing, graph colouring, portfolio optimisation — they all fit.

- **The cost Hamiltonian pattern recurs everywhere.** The idea of encoding an objective function as a quantum operator whose ground state is the optimal solution appears in Unit 3 (molecular simulation — the Hamiltonian encodes the energy), Unit 6 (QUBO/annealing), and Unit 7 (QPE). Once you see the pattern, you see it everywhere.

- **QAOA vs. quantum annealing.** QAOA explores the cost landscape via alternating unitaries (gate-based). Quantum annealing explores it via adiabatic evolution (slowly changing the Hamiltonian). They're different paradigms for the same goal. We'll see annealing in Unit 6 (Supply Chains).

- **The variational quantum-classical loop appears again in VQE** (Unit 3). If you understood the QAOA loop — quantum circuit produces a cost estimate, classical optimiser updates parameters, repeat — then you already understand VQE's architecture. The only difference is the cost function (molecular energy vs. cut count) and the ansatz (chemistry-motivated vs. graph-motivated).

- **For the runnable QASM circuit,** see [Quokka Cookbook — Recipe 07](https://github.com/johnazariah/quokka-cookbook/recipes/07-qaoa-maxcut/). That recipe builds the same MaxCut QAOA circuit gate by gate in OpenQASM 2.0.

- **Further reading:**
    - Farhi, Goldstone, Gutmann (2014). *A Quantum Approximate Optimization Algorithm.* [arXiv:1411.4028](https://arxiv.org/abs/1411.4028)
    - Guerreschi and Matsuura (2019). *QAOA for Max-Cut requires hundreds of qubits for quantum speed-up.* [arXiv:1812.07589](https://arxiv.org/abs/1812.07589)
    - Zhou et al. (2020). *Quantum Approximate Optimization Algorithm: Performance, Mechanism, and Implementation on Near-Term Devices.* [arXiv:1812.01041](https://arxiv.org/abs/1812.01041)
    - Bravyi, Kliesch, Koenig, Tang (2020). *Obstacles to variational quantum optimization from symmetry protection.* [arXiv:1910.08980](https://arxiv.org/abs/1910.08980)
