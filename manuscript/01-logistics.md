# Unit 1: Logistics — *Saving $50 Million One Mile at a Time*


## The Hook

Every morning, 130,000 UPS drivers leave their depots. Each driver visits between 100 and 200 stops. The order they visit those stops determines how many miles they drive, how much fuel they burn, and whether they make it home for dinner.

In 2012, UPS deployed a system called ORION: On-Road Integrated Optimization and Navigation. Its job: take each driver's list of deliveries and produce a better route. Not a perfect route. Just a better one. ORION shaved an average of one mile off each driver's daily route.

One mile doesn't sound like much. But multiply by 130,000 drivers, 250 working days per year, and the cost of fuel, vehicle wear, and driver time. UPS reported savings of **$50 million per year** from that single mile.

Now consider what a *two*-mile improvement would be worth. Or five.

The problem is that finding the optimal route isn't just difficult; it's one of the hardest problems in all of computer science. If a driver has 20 stops, there are $20! = 2.4 \times 10^{18}$ possible orderings. That's 2.4 quintillion routes to check. A desktop computer evaluating one billion routes per second would need 77 years. For 50 stops, the number of possibilities exceeds the number of atoms in the observable universe.

This is the **Travelling Salesman Problem** (TSP), and it has tormented mathematicians, computer scientists, and logistics companies for over a century. Every exact algorithm for TSP has a running time that grows at least exponentially with the number of stops. There is strong theoretical evidence (though no proof) that no efficient exact algorithm exists; the problem is NP-hard.

In practice, nobody solves TSP exactly at scale. ORION doesn't find the best route; it finds a *pretty good* route, using heuristics that have been refined over decades. Branch-and-bound, genetic algorithms, simulated annealing, Lin-Kernighan; these are all sophisticated methods for exploring the vast space of possible routes without drowning in it.

They work remarkably well. But they all share a fundamental limitation: they explore the space of routes *one at a time*. They walk through the landscape of possible solutions, stepping from one candidate to a neighbouring one, hoping that local improvements lead to global ones. Sometimes they get stuck in valleys; solutions that are better than all their neighbours but far worse than the global optimum.

What if you could explore the entire landscape at once?


## The Bottleneck

Let's make the problem concrete. Strip away the geography and the delivery trucks, and what remains is pure combinatorics.

You have a graph; a set of cities (nodes) connected by roads (edges), each road with a cost (the distance). You want to visit every city exactly once and return to where you started, minimising the total cost. That's TSP.

For our purposes, let's start with something even simpler: **MaxCut**. Take a graph and colour every node either red or blue. An edge is "cut" if its endpoints have different colours. MaxCut asks: what colouring cuts the most edges?

MaxCut sounds like a toy problem, but it's NP-hard; just as hard as TSP in a complexity-theoretic sense. And it's beautifully suited to our purposes because it translates directly into the language of qubits.

Here's why MaxCut is hard. A graph with $n$ nodes has $2^n$ possible colourings. For each colouring, you can count the cut edges in $O(m)$ time, where $m$ is the number of edges. So the brute-force algorithm takes $O(m \cdot 2^n)$ time. For $n = 50$, that's roughly $10^{15}$ operations; doable but slow. For $n = 100$, it's $10^{30}$ operations. For $n = 300$, you'd need more time than the age of the universe.

The problem is the search space. Every node is a binary decision: red or blue, 0 or 1. The decisions interact; the value of your choice for node $i$ depends on what you chose for nodes $j$, $k$, $l$; every node that shares an edge with $i$. These interactions create a rugged *cost landscape*: a function over $\{0,1\}^n$ with exponentially many local optima.

Classical heuristics navigate this landscape by making local moves. Flip one node's colour. If the cut count improves, keep it; otherwise, try another flip. Simulated annealing adds randomness; occasionally accept a worse solution to escape local optima, gradually reducing the randomness as you "cool down."

These methods are powerful, but they have a fundamental weakness: they explore the landscape *sequentially*. At any moment, they're sitting at a single point in the space of $2^n$ possible colourings. They can only see the immediate neighbourhood. A better solution might exist on the other side of a high barrier, and no amount of local flipping will find it.

This is where the story turns quantum.


## The Quantum Angle

What if, instead of sitting at one colouring and looking around, you could be at *all* $2^n$ colourings simultaneously, and then use interference to amplify the ones that cut more edges?

That's the core idea behind the **Quantum Approximate Optimization Algorithm** (QAOA), introduced by Farhi, Goldstone, and Gutmann in 2014. It's not a magic bullet; it won't solve NP-hard problems in polynomial time (nobody believes that's possible). But it offers a fundamentally different way to explore the solution landscape, one that exploits quantum mechanics in a structural way that classical algorithms cannot mimic.

Before we dive into QAOA itself, let's step back and sketch how quantum algorithms work in general. Nearly every quantum algorithm follows the same three-act structure:

1. **Encode** the problem into a quantum system. Binary decisions become qubits. Costs become operators. The search space becomes the space of quantum states.
2. **Manipulate** the quantum state using carefully chosen operations. This is where the quantum magic happens: interference suppresses bad solutions and amplifies good ones, without ever looking at them one by one.
3. **Measure** the result. Measurement collapses the quantum state to a single classical answer. If the manipulation was done well, that answer is likely to be a good one.

That's the whole recipe. The art is in step 2, and it's different for every algorithm. For QAOA, the manipulation is a rhythmic alternation between "imprint the cost" and "mix the solutions." For Shor's algorithm (Unit 2), it's a Fourier transform. For VQE (Unit 3), it's a chemistry-inspired trial state. But the three-act structure is always the same.

Let's see how it plays out for MaxCut.

### Qubits as binary decisions

The first step is encoding. Each node in the graph gets one qubit. A qubit in state $|0\rangle$ means "red"; $|1\rangle$ means "blue." An $n$-node graph requires $n$ qubits. A specific colouring; say, nodes 1 and 3 are blue, node 2 is red; corresponds to the quantum state $|101\rangle$.

So far, this is just notation. The quantum part starts when we use *superposition*.

> **Superposition.** A qubit doesn't have to be $|0\rangle$ or $|1\rangle$. It can be in a state like $\alpha|0\rangle + \beta|1\rangle$, where $\alpha$ and $\beta$ are numbers (complex, if you care, but the intuition works with real numbers) satisfying $|\alpha|^2 + |\beta|^2 = 1$. The values $|\alpha|^2$ and $|\beta|^2$ are the probabilities of getting 0 or 1 when you measure. Before measurement, both possibilities coexist. This isn't a metaphor; it's how the physics works. When you put $n$ qubits into superposition, the system represents all $2^n$ possible states at once. You'll hear people say "the quantum computer tries all answers simultaneously." That's misleading. What really happens is subtler: the $2^n$ possibilities can *interfere* with each other, and clever algorithms arrange for the good answers to reinforce and the bad ones to cancel. Deep-Dive 1 makes this precise.

With $n$ qubits in superposition, we have all $2^n$ colourings present in a single quantum state. We can't look at them all; measurement gives us just one. But between preparation and measurement, we can manipulate the amplitudes to make good colourings more likely to appear. That's the game.

### Turning costs into energy

Now we need to tell the quantum computer what "good" means. We need to translate the MaxCut objective; "cut as many edges as possible"; into something a quantum system can work with.

Physicists have a word for "the function that assigns a number to every state of a system": they call it a **Hamiltonian**. In physics, the Hamiltonian describes the total energy, and the system naturally evolves toward its lowest-energy state. We're going to borrow this idea: assign an "energy" to every colouring, where lower energy means more edges cut. Then "find the best colouring" becomes "find the lowest-energy state."

This reframing is not just convenient; it's the key insight that makes quantum optimisation work. Quantum systems are *built* to find low-energy states. It's what they do naturally. By encoding our problem as a Hamiltonian, we're asking quantum mechanics to do what it already does best.

Here's how we build the Hamiltonian for MaxCut. For each edge $(i, j)$, we need an expression that equals 1 when the edge is cut and 0 when it isn't. The trick uses a quantum operator called $Z$ (the Pauli-$Z$ operator, which gives $+1$ for $|0\rangle$ and $-1$ for $|1\rangle$). If you want to verify the formula yourself, Deep-Dive 1 walks through the algebra; for now, just check the two cases:

$$\frac{1 - Z_i Z_j}{2}$$

If qubits $i$ and $j$ are the *same* colour, $Z_i Z_j = (+1)(+1) = +1$ or $(-1)(-1) = +1$, and the expression gives $(1-1)/2 = 0$. If they're *different* colours, $Z_i Z_j = (+1)(-1) = -1$, and the expression gives $(1-(-1))/2 = 1$. That's exactly what we want: 1 for a cut edge, 0 for an uncut one.

The total cost Hamiltonian sums this over every edge:

$$C = \sum_{(i,j) \in E} \frac{1 - Z_i Z_j}{2}$$

The state with the highest value of $C$ is the colouring that cuts the most edges. Equivalently, the **ground state** of $-C$ (the lowest-energy state) is the optimal solution.

This pattern; "encode the objective as a Hamiltonian, then find its ground state"; is the central trick of quantum optimisation, and it recurs throughout this book. In Unit 3, the Hamiltonian encodes molecular energy. In Unit 6, it encodes scheduling constraints. In Unit 7, it encodes the physics of a material. The problems are different, but the strategy is the same: translate "find the best X" into "find the lowest energy."

### Reading a quantum circuit

Before we look at the QAOA circuit, a quick orientation on how quantum programs are drawn.

A quantum circuit is read left to right, like sheet music. Each horizontal line (called a **wire**) represents one qubit. Boxes or symbols on the wires represent **operations** (also called gates). A gate on one wire acts on that qubit alone; a gate connecting two wires (drawn with a vertical line between them) acts on both qubits together. At the end, a measurement symbol ($M$ or a meter icon) reads out the qubit's value as a classical 0 or 1.

> **Unitary.** You'll see quantum operations called "unitary." This is a technical term from linear algebra that means two things: the operation is *reversible* (you can always undo it), and it *preserves probabilities* (they still add up to 1 afterwards). Every quantum gate is unitary. Measurement is not; it's the one irreversible step, where the quantum state collapses to a definite classical value. Deep-Dive 1 goes deeper into the mathematics.

A few gates we'll meet repeatedly:

- $H$ (Hadamard): puts a qubit into superposition. Turns $|0\rangle$ into an equal mix of $|0\rangle$ and $|1\rangle$.
- $Z$ (Pauli-Z): you've already met this; it gives $+1$ for $|0\rangle$ and $-1$ for $|1\rangle$. Related gates $R_Z(\theta)$ rotate by a tunable angle.
- $X$ (Pauli-X): flips a qubit; $|0\rangle \to |1\rangle$ and vice versa. Related gate $R_X(\theta)$ rotates by a tunable angle.
- CNOT: a two-qubit gate that flips the second qubit if the first is $|1\rangle$. This is how qubits become *entangled*; correlated in ways that have no classical analogue.

With that vocabulary, the QAOA circuit will make sense.

### The variational loop

But how do you choose $\gamma$ and $\beta$? This is where QAOA becomes a **variational** algorithm; a quantum-classical hybrid:

1. Pick initial values of $\gamma$ and $\beta$
2. Run the quantum circuit, measure the output
3. Compute the expected cost (run many times, take the average)
4. Feed this cost to a classical optimiser (COBYLA, Nelder-Mead, gradient descent)
5. The optimiser suggests better values of $\gamma$ and $\beta$
6. Repeat until convergence

The quantum computer explores the solution space. The classical computer tunes the exploration strategy. Neither could do the other's job efficiently.

For deeper QAOA (more rounds of alternation, called $p$-depth QAOA), you have $2p$ parameters: $\gamma_1, \beta_1, \gamma_2, \beta_2, \ldots, \gamma_p, \beta_p$. In principle, as $p \to \infty$, QAOA can find the exact optimum. In practice, you use a small number of rounds and accept an approximate answer; hence "Approximate" in the name.

### How it becomes a circuit

Each ingredient has a direct circuit implementation:

- **Initial state:** Apply a Hadamard gate $H$ to every qubit → equal superposition $|+\rangle^n$
- **Problem unitary ($e^{-i\gamma C}$):** For each edge $(i,j)$, apply $\text{CNOT}(i,j) \cdot R_Z(2\gamma) \cdot \text{CNOT}(i,j)$. This implements $e^{-i\gamma Z_i Z_j}$.
- **Mixer ($e^{-i\beta B}$):** Apply $R_X(2\beta)$ to every qubit.
- **Measurement:** Measure all qubits in the computational basis.

The circuit depth grows linearly with the number of edges and the depth parameter $p$. For small graphs, this is entirely feasible on current quantum hardware.


## Worked Example

Let's solve MaxCut on a triangle; three nodes, three edges. The optimal cut is 2 (colour one node differently from the other two).

### The graph

![MaxCut triangle graph: nodes 0, 1, 2 with edges (0,1), (0,2), (1,2)](../figures/maxcut-triangle-graph.png)

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





→ *Want to understand how the QAOA circuit is built, gate by gate? Read the next chapter.*


## Reality Check


Let's be honest about where QAOA stands; and where it's heading.

**The low-depth story.** For depth-1 QAOA on MaxCut, Farhi, Goldstone, and Gutmann (2014) proved a guaranteed approximation ratio of 0.6924 for 3-regular graphs. The best classical polynomial-time algorithm (Goemans-Williamson, 1995) achieves 0.878. So at low depth, QAOA *underperforms* the best classical method. This result gave QAOA a reputation as a promising but underpowered algorithm.

But low depth is not the whole story.

**The high-depth story is much more interesting.** QAOA's performance improves monotonically with depth $p$, and recent work has made it possible to compute exact QAOA performance at depths that were previously out of reach; not by running a quantum computer, but by exploiting the mathematical structure of the algorithm itself.

MaxCut and its generalisation to Max-$k$-XORSAT belong to a family of constraint satisfaction problems where the cost function decomposes into $k$-local terms. For $D$-regular instances of these problems, Basso et al. (2021) showed that QAOA's expected performance in the infinite-size limit can be computed via a *tree tensor network* contraction; a classical calculation whose cost is exponential in $p$ but independent of the graph size.

Farhi et al. (2025) pushed this to depth $p = 20$ for MaxCut on 3-regular graphs. Azariah and Jordan (2026) extended the approach to Max-$k$-XORSAT for $k \geq 3$ using a Walsh-Hadamard factorisation that reduces the computational cost by a factor of 65,000× for $k = 3$. This factorisation exploits the fact that the $k$-body constraint fold is a convolution on $\mathbb{Z}_2^{2p+1}$; the Walsh-Hadamard transform diagonalises it. The result: exact QAOA performance through depth $p = 13$ for $(k=3, D=4)$, achieving a satisfaction fraction of $\tilde{c} = 0.877$.

Why does this matter? Because we can now *precisely compare* QAOA against other quantum and classical algorithms on these problems. For Max-$k$-XORSAT, the main quantum competitor is **Decoded Quantum Interferometry** (DQI), a non-variational algorithm introduced by Jordan et al. (Nature, 2025). DQI combined with Belief Propagation post-processing (DQI+BP) was the previous state of the art. The exact QAOA evaluations show that **QAOA surpasses DQI+BP on 13 of 15 $(k, D)$ parameter pairs tested**.

This doesn't mean QAOA has "won": DQI has its own advantages (no classical optimiser loop, better scaling properties for some regimes). But it definitively refutes the narrative that QAOA is too weak to compete. For this family of problems, at sufficient depth, QAOA is a serious contender.

**The hardware gap.** These are theoretical results; computing what QAOA *would* achieve if you could run it at depth $p = 12$ on a large enough quantum computer. Today's hardware can run QAOA at $p = 1$ or $p = 2$ on a few dozen noisy qubits. The gap between where the algorithm shines ($p \geq 8$) and where hardware can operate ($p \leq 2$) is real. Fault-tolerant quantum computers with $\sim 10^4$ logical qubits would close this gap.

**The barren plateau question.** McClean et al. (2018) showed that for random quantum circuits, the cost function gradient vanishes exponentially with system size. This is a serious concern for variational algorithms. However, QAOA has far more structure than a random circuit; its alternating problem/mixer layers are determined by the problem graph. Barren plateaus have not been observed in practice for QAOA at moderate depths, and the exact evaluations confirm that the parameter landscape remains navigable through $p = 13$.

**What's real today:** QAOA's algorithmic performance is now well-characterised for an important family of combinatorial problems. The algorithm is provably competitive with the best known quantum alternatives. The bottleneck is hardware, not the algorithm.


## Chef's Notes

- **MaxCut is a gateway drug.** We used it here because it maps directly to qubits ($Z_i Z_j$ interactions), but QAOA applies to *any* combinatorial optimisation problem you can write as a cost function over binary variables. Scheduling, bin packing, graph colouring, portfolio optimisation; they all fit. MaxCut and $k$-XORSAT are the problems where we can compute QAOA's exact performance; for other problems, we rely on empirical evaluation.

- **The Max-$k$-XORSAT family.** MaxCut is the $k = 2$ case of a broader family: Max-$k$-XORSAT, where each constraint involves $k$ variables connected by an XOR. As $k$ increases, the problem gets harder classically (the random satisfiability threshold drops) but the QAOA analysis extends cleanly; the cost Hamiltonian becomes a sum of $k$-body $Z$-interactions instead of 2-body. The same tree tensor network machinery evaluates QAOA performance for any $k$, with a computational trick (Walsh-Hadamard factorisation) that makes $k \geq 3$ tractable.

- **The cost Hamiltonian pattern recurs everywhere.** The idea of encoding an objective function as a quantum operator whose ground state is the optimal solution appears in Unit 3 (molecular simulation; the Hamiltonian encodes the energy), Unit 6 (QUBO/annealing), and Unit 7 (QPE). Once you see the pattern, you see it everywhere.

- **QAOA vs. quantum annealing.** QAOA explores the cost landscape via alternating unitaries (gate-based). Quantum annealing explores it via adiabatic evolution (slowly changing the Hamiltonian). They're different paradigms for the same goal. We'll see annealing in Unit 6 (Supply Chains).

- **The variational quantum-classical loop appears again in VQE** (Unit 3). If you understood the QAOA loop; quantum circuit produces a cost estimate, classical optimiser updates parameters, repeat; then you already understand VQE's architecture. The only difference is the cost function (molecular energy vs. cut count) and the ansatz (chemistry-motivated vs. graph-motivated).


- **Further reading:**
    - Farhi, Goldstone, Gutmann (2014). *A Quantum Approximate Optimization Algorithm.* [arXiv:1411.4028](https://arxiv.org/abs/1411.4028)
    - Basso, Farhi, Marwaha, Villalonga, Zhou (2021). *The Quantum Approximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the Sherrington-Kirkpatrick Model.* [arXiv:2110.14206](https://arxiv.org/abs/2110.14206)
    - Farhi, Gutmann, Ranard, Villalonga (2025). *Lower bounding the MaxCut of high girth 3-regular graphs using the QAOA.* [arXiv:2503.12789](https://arxiv.org/abs/2503.12789)
    - Jordan, Shutty, Wootters, Zalcman, et al. (2025). *Optimization by decoded quantum interferometry.* [Nature (2025)](https://doi.org/10.1038/s41586-025-09527-5) ([arXiv:2408.08292](https://arxiv.org/abs/2408.08292))
    - Azariah and Jordan (2026). *Exact QAOA on Max-$k$-XORSAT via generic tree folding.* (Working title; in preparation.)
