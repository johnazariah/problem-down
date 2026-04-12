# Unit 6: Supply Chains — *10,000 Nurses, 50 Hospitals, 1 Schedule*


## The Hook

Every winter, Britain's National Health Service enters a scheduling crisis. Across 50 hospitals, 10,000 nurses need to be assigned to shifts; day, evening, night; across wards, specialties, and locations. Each nurse has qualifications (ICU-certified? paediatrics-trained?), contractual constraints (maximum hours, minimum rest), preferences (no nights, school pickup at 3 PM), and legal requirements (EU Working Time Directive: no more than 48 hours per week, 11 hours rest between shifts).

The NHS spends an estimated **£3 billion per year** on agency nurses; temporary staff hired at premium rates because the permanent workforce can't be scheduled efficiently. Not because there aren't enough nurses (though there often aren't), but because the scheduling problem is so complex that planners routinely produce suboptimal rosters, leaving gaps that agencies fill at 2–3× the cost.

This isn't a peculiarly British problem. Airlines schedule crews across thousands of flights. Manufacturing plants assign workers to production lines. Call centres staff agents across time zones. In every case, the mathematical structure is the same: assign $N$ resources to $M$ slots subject to constraints, minimising cost (or maximising fairness, or minimising overtime).

These are **constraint satisfaction problems**, and they are NP-hard. The nurse scheduling problem (NSP) was proven NP-hard by Osogami and Imai in 2000. No polynomial-time algorithm exists (unless P = NP). Classical solvers; integer linear programming (ILP), constraint programming (CP), simulated annealing; can handle instances with hundreds of nurses. At thousands, they struggle. At tens of thousands, they break.


## The Bottleneck

The nurse scheduling problem has a distinctive mathematical structure. It's not a pure optimisation problem (like MaxCut); it's a **constrained** optimisation problem, with both hard constraints (must satisfy) and soft constraints (prefer to satisfy).

**Hard constraints:**
- Each shift must be staffed by a qualified nurse
- No nurse works more than 48 hours/week
- Minimum 11 hours between consecutive shifts
- No nurse works more than 5 consecutive days

**Soft constraints (with penalties):**
- Honour nurse preferences (nights, weekends)
- Distribute unpopular shifts fairly
- Minimise travel between hospital sites
- Balance workload across the team

The search space is enormous. With $N$ nurses and $S$ shifts, there are $N^S$ possible assignments (ignoring constraints). For $N = 100$ nurses and $S = 500$ shifts across a week, that's $100^{500} \approx 10^{1000}$; absurdly beyond brute force.

The real difficulty is the **interaction structure**. Constraints are non-local: assigning Nurse A to Monday night affects whether Nurse B can take Tuesday morning (if they share qualifications and wards). These interactions create a web of dependencies that classical local-search methods struggle with; improving one part of the schedule can break another.


## The Quantum Angle

### QUBO: turning constraints into energy

The key idea is **Quadratic Unconstrained Binary Optimisation** (QUBO). We convert the constrained scheduling problem into an *unconstrained* minimisation of a quadratic function over binary variables; then map that to the ground state of a quantum Hamiltonian.

Each binary decision gets a variable: $x_{n,s} = 1$ if nurse $n$ is assigned to shift $s$, 0 otherwise. The total number of binary variables is $N \times S$.

Hard constraints become **penalty terms**: add a large positive cost for any assignment that violates them. Soft constraints become **smaller penalties**, proportional to how undesirable the violation is.

The result is a cost function:

$$C(x) = \sum_i \sum_j Q_{ij} x_i x_j + \sum_i c_i x_i$$

where $Q_{ij}$ encodes the interactions between binary decision variables and $c_i$ encodes the individual preferences. This is the QUBO form. The optimal schedule is the binary string $x^*$ that minimises $C(x)$.

### From QUBO to Ising Hamiltonian

The substitution $x_i = \frac{1 - Z_i}{2}$ converts each binary variable (0 or 1) to a spin variable ($+1$ or $-1$). The QUBO cost function becomes an **Ising Hamiltonian**:

$$H = \sum_{i < j} J_{ij} Z_i Z_j + \sum_i h_i Z_i + \text{const}$$

The ground state of this Hamiltonian is the optimal schedule. This is the same pattern as Unit 1 (MaxCut → cost Hamiltonian) and Unit 3 (molecule → molecular Hamiltonian); different problem, same mathematical structure.

### Quantum annealing

There are two quantum approaches to finding the ground state of an Ising Hamiltonian:

**Gate-based QAOA** (Unit 1): apply alternating problem and mixer unitaries, optimise parameters variationally. Works on universal quantum computers.

**Quantum annealing**: a different paradigm entirely. Start in the ground state of a simple Hamiltonian $H_\text{init}$ (whose ground state you know; typically all qubits in $|+\rangle$). Slowly transform $H_\text{init}$ into the problem Hamiltonian $H_\text{problem}$:

$$H(t) = \left(1 - \frac{t}{T}\right) H_\text{init} + \frac{t}{T} H_\text{problem}$$

The **adiabatic theorem** guarantees: if you go slowly enough (large $T$), the system stays in the ground state throughout. At the end ($t = T$), you're in the ground state of $H_\text{problem}$; the optimal schedule.

### Why quantum annealing might help

Classical simulated annealing explores the energy landscape by making random local moves, accepting uphill moves with decreasing probability as the "temperature" drops. It gets stuck when the optimal solution is separated from the current state by a tall energy barrier; it has to go *over* the barrier.

Quantum annealing can tunnel *through* barriers. Quantum tunnelling; the same effect that allows radioactive decay; lets the quantum state traverse energy barriers without climbing them. Barriers that are tall but *narrow* are easy to tunnel through; barriers that are tall and *wide* are hard.

This gives quantum annealing a structural advantage for problems with specific landscape properties: many tall, narrow barriers. Whether real-world scheduling problems have this property is an empirical question; and a contested one.


## Worked Example

Schedule 8 nurses across 4 shifts (Mon-day, Mon-night, Tue-day, Tue-night) in 2 wards, with constraints:

- Each shift/ward needs exactly 1 nurse
- No nurse works consecutive shifts (11-hour rest)
- Nurse preferences: 3 nurses prefer day shifts, 2 prefer nights

Formulate as QUBO: 8 nurses × 8 shift-slots = 64 binary variables (reducible with symmetries). Solve with simulated annealing (classical) and compare with a QAOA circuit.

→ **See [notebook `06-supply-chains.ipynb`](../notebooks/06-supply-chains.ipynb) for the runnable version.**



→ *Want to understand the algorithm in detail? Read the next chapter.*


## Reality Check

**D-Wave.** The company most associated with quantum annealing, D-Wave has built machines with over 5,000 qubits; far more than any gate-based machine. Their Advantage system can natively solve QUBO problems with thousands of variables. But the qubits are noisy, the connectivity is limited (Pegasus graph), and embedding real problems onto the hardware graph introduces significant overhead.

**The speedup debate.** Despite two decades of effort, no definitive quantum speedup for annealing has been demonstrated on a practical problem. Rønnow et al. (2014) found no speedup over classical simulated annealing on random instances. King et al. (2023) showed advantage on *specific* crafted instances. The picture is nuanced: annealing may offer advantages for specific problem structures, but general-purpose speedup remains unproven.

**Hybrid solvers.** D-Wave's most practically useful tool is its **hybrid classical-quantum solver** (Leap), which uses classical heuristics for most of the work and the quantum annealer for specific subproblems. These hybrids outperform pure classical solvers on some logistics and scheduling benchmarks; but it's hard to attribute the advantage specifically to the quantum component.

**Gate-based vs. annealing.** QAOA on gate-based hardware offers more flexibility (arbitrary cost functions, tuneable depth) but currently operates on far fewer qubits. Annealing offers more qubits but less control. The two approaches may converge as hardware improves.

**What would change the picture.** A demonstration of quantum speedup on a real scheduling or logistics problem with practical constraints; not a crafted benchmark instance. This would require either significant improvements in annealer quality or gate-based machines with $O(10^3)$ logical qubits.


## Chef's Notes

- **QUBO is the universal input format for constrained optimisation on quantum computers.** Any problem you can write as a quadratic function over binary variables can be solved (in principle) by quantum annealing or QAOA. Scheduling, routing, portfolio optimisation, resource allocation; they all have QUBO formulations. The D-Wave Ocean SDK has a library of pre-built QUBO templates for common problems.

- **The QUBO-to-Ising map is the bridge between classical OR and quantum computing.** If you know operations research, you already know how to formulate QUBO problems. The quantum part is "just" a different solver for the same formulation.

- **Quantum tunnelling vs. thermal hopping.** Simulated annealing hops over barriers using thermal energy. Quantum annealing tunnels through them. Neither is universally better; it depends on the barrier geometry. Tall-narrow barriers favour tunnelling; short-wide barriers favour hopping.

- **Connection to Unit 1.** QAOA and annealing are two paradigms for the same goal: finding the ground state of a cost Hamiltonian. Unit 1 introduced QAOA on MaxCut (a simple QUBO). This unit shows the QUBO formulation for a richer problem and introduces the annealing alternative.

- **Further reading:**
    - Lucas (2014). *Ising formulations of many NP problems.* [Frontiers in Physics 2:5](https://doi.org/10.3389/fphy.2014.00005)
    - Farhi et al. (2001). *A quantum adiabatic evolution algorithm applied to random instances of an NP-complete problem.* [Science 292:472–475](https://doi.org/10.1126/science.1057726) ([arXiv:quant-ph/0001106](https://arxiv.org/abs/quant-ph/0001106))
    - Rønnow et al. (2014). *Defining and detecting quantum speedup.* [Science 345:420–424](https://doi.org/10.1126/science.1252319) ([arXiv:1401.2910](https://arxiv.org/abs/1401.2910))
    - King et al. (2023). *Quantum critical dynamics in a 5,000-qubit programmable spin glass.* [Nature 617:61–66](https://doi.org/10.1038/s41586-023-05867-2) ([arXiv:2207.13800](https://arxiv.org/abs/2207.13800))
    - Katzgraber, Hamze & Andrist (2014). *Glued trees are not hard for quantum annealing: designing hard Ising instances.* [Physical Review X 4:021008](https://doi.org/10.1103/PhysRevX.4.021008) ([arXiv:1404.6539](https://arxiv.org/abs/1404.6539))
    - Katzgraber, Trebst, Huse & Troyer (2006). *Feedback-optimized parallel tempering Monte Carlo.* [Journal of Statistical Mechanics P03018](https://doi.org/10.1088/1742-5468/2006/03/P03018) ([arXiv:cond-mat/0602085](https://arxiv.org/abs/cond-mat/0602085))
    - Mandrà, Katzgraber & Thomas (2017). *The pitfalls of planar spin-glass benchmarks.* [Quantum Science and Technology 2:038501](https://doi.org/10.1088/2058-9565/aa7877) ([arXiv:1703.00622](https://arxiv.org/abs/1703.00622))
