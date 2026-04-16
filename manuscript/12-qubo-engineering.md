# Deep-Dive 6: QUBO Engineering

_This chapter pairs with Chapter 11 (Supply Chains), which introduced nurse scheduling and constraint satisfaction. Here we show how to formulate real-world constraints as QUBO problems and solve them on quantum hardware._

## In This Chapter

- **What you'll learn:** How to turn constraints into penalty terms, convert QUBO to an Ising Hamiltonian, and why quantum annealing tunnels through barriers that classical methods can't climb.
- **What you need:** From Chapter 2, you know cost Hamiltonians and the $ZZ$ gate. Here we extend the cost Hamiltonian concept to *constrained* problems; where not every binary string is a valid solution.
- **Runnable version:** The companion notebook [`06-supply-chains.ipynb`](../notebooks/06-supply-chains.ipynb) solves a small scheduling QUBO on a cloud Quokka.


## From constraints to energy

### The QUBO pattern

In Chapter 2 (QAOA), our cost function was simple: count the cut edges. Every binary string was a valid colouring; there were no constraints, just better and worse solutions.

Real problems have constraints. "Each shift has exactly one nurse." "No nurse works more than 48 hours." "At least two ICU-certified nurses per night shift." Some constraints are negotiable (preferences); others are mandatory (regulations).

**QUBO** (Quadratic Unconstrained Binary Optimisation) handles constraints by converting them to **penalty terms**; large positive costs added whenever a constraint is violated. The optimisation becomes: minimise the total cost (objective + penalties). A solution with zero penalty satisfies all constraints.

### Encoding equality constraints

**"Each shift must have exactly one nurse assigned."**

Binary variables: $x_{n,s} = 1$ if nurse $n$ takes shift $s$. The constraint for shift $s$:

$$\sum_n x_{n,s} = 1$$

Convert to penalty: $P \cdot \left(\sum_n x_{n,s} - 1\right)^2$ where $P$ is large.

Expand (using $x_i^2 = x_i$ for binary variables):

$$P \cdot \left(\sum_n x_{n,s}^2 + 2\sum_{n < n'} x_{n,s} x_{n',s} - 2\sum_n x_{n,s} + 1\right) = P \cdot \left(-\sum_n x_{n,s} + 2\sum_{n < n'} x_{n,s} x_{n',s} + 1\right)$$

This is quadratic in the binary variables; it fits QUBO form. The minimum (zero penalty) occurs when exactly one $x_{n,s} = 1$.

### Encoding inequality constraints

**"No nurse works more than 3 shifts."**

The constraint is $\sum_s x_{n,s} \leq 3$. Introduce **slack variables** $y_1, y_2, y_3$ (binary) to convert to equality:

$$\sum_s x_{n,s} + y_1 + y_2 + y_3 = 3 + |\text{max possible excess}|$$

Wait; that's getting complicated. A simpler approach for small bounds: enumerate the violations. For "at most 3":

$$P \cdot \sum_{s_1 < s_2 < s_3 < s_4} x_{n,s_1} x_{n,s_2} x_{n,s_3} x_{n,s_4}$$

But this is a *quartic* term (four variables), not quadratic. Trick: introduce auxiliary variables to reduce higher-order terms to quadratic. Or use penalty functions that are quadratic approximations of the constraint.

> **The QUBO art:** formulating constraints as quadratic penalties is part engineering, part art. Simple constraints (equalities, pairwise exclusions) map cleanly. Complex constraints (inequality chains, conditional requirements) require creativity. Libraries like D-Wave's `dwavebinarycsp` automate common patterns.

### Soft constraints as linear costs

**"Nurse A prefers day shifts."**

Add a small cost for night assignments: $w \cdot x_{A,\text{night}}$ where $w \ll P$. The optimiser will avoid night shifts when possible, but will violate the preference if needed to satisfy hard constraints (because the hard-constraint penalty $P$ is much larger than the preference cost $w$).

This priority structure; hard constraints as large penalties, soft preferences as small costs; is what makes QUBO flexible enough for real scheduling problems.


## From QUBO to Ising Hamiltonian

### The substitution

Once you have a QUBO cost function $C(x) = x^T Q x + c^T x + \text{const}$, the map to an Ising Hamiltonian is mechanical. Substitute $x_i = \frac{1 - Z_i}{2}$:

$$x_i x_j = \frac{(1 - Z_i)(1 - Z_j)}{4} = \frac{1 - Z_i - Z_j + Z_i Z_j}{4}$$

Every QUBO term becomes a combination of:
- $Z_i Z_j$ terms (the same interactions as MaxCut in Chapter 2)
- $Z_i$ terms (local fields)
- Constants (global energy offset)

The resulting Ising Hamiltonian $H = \sum_{ij} J_{ij} Z_i Z_j + \sum_i h_i Z_i + \text{const}$ is exactly the kind of operator we can implement with QAOA (Chapter 2) or quantum annealing.

### The circuit connection

The QAOA circuit for a QUBO problem uses the same building blocks as Chapter 2:
- $ZZ$ gates (CNOT sandwich) for the $J_{ij}$ terms
- $R_Z$ rotations for the $h_i$ terms
- $R_X$ mixer rotations

The only difference is more terms; a QUBO with $n$ variables and $O(n^2)$ interactions needs $O(n^2)$ CNOT sandwiches per QAOA layer. The circuit is wider and deeper, but the structure is identical.


## Quantum annealing: a different paradigm

### The adiabatic approach

QAOA (Chapter 2) uses gate-based quantum computing: discrete operations applied in sequence. **Quantum annealing** takes a completely different approach: continuous time evolution.

Start in the ground state of a simple Hamiltonian $H_0$ (typically a **transverse field** $\sum_i X_i$ — an $X$ operator on every qubit — whose ground state is $|+\rangle^n$, which we already know how to prepare from Deep-Dive 1). Slowly interpolate to the problem Hamiltonian $H_1$:

$$H(t) = \left(1 - \frac{t}{T}\right) H_0 + \frac{t}{T} H_1$$

The **adiabatic theorem** says: if the interpolation is slow enough, the system stays in the ground state throughout. At the end ($t = T$), you're in the ground state of $H_1$; the optimal solution.

### How slow is slow enough?

"Slow enough" means $T \geq O(1/\Delta_\text{min}^2)$ where $\Delta_\text{min}$ is the minimum spectral gap; the smallest energy difference between the ground state and the first excited state during the anneal.

For easy problems, $\Delta_\text{min}$ is large and the anneal is fast. For hard problems, $\Delta_\text{min}$ can be exponentially small; the anneal time grows exponentially, and any speedup disappears.

The open question: for which problems is the spectral gap large enough that annealing is practical?

### Quantum tunnelling: the potential advantage

Classical simulated annealing gets stuck at energy barriers; to escape a local minimum, it must thermally "hop" over the barrier, which requires the barrier to be low or the temperature to be high.

Quantum annealing can **tunnel through** barriers. Quantum tunnelling; the same physics that enables radioactive decay; lets the quantum state pass through energy barriers that are tall but narrow. The tunnelling rate depends on the barrier *width*, not its height.

For problems with many tall, narrow barriers: quantum annealing may explore the energy landscape more efficiently than classical annealing. For problems with wide barriers: classical annealing may be better.

> **The honest picture:** Despite two decades of effort, definitive quantum speedup for annealing on practical problems remains unproven. D-Wave's quantum annealers (5,000+ qubits) solve some crafted instances faster than classical methods, but general-purpose advantage has not been demonstrated. This is an active research frontier.


## What you should take away

1. **QUBO is the universal language for constrained binary optimisation.** Any problem with binary decisions and quadratic interactions can be written as a QUBO. The map from constraints to penalties is the key engineering step.

2. **QUBO → Ising is mechanical.** The substitution $x_i = (1-Z_i)/2$ converts any QUBO to an Ising Hamiltonian that can be solved with QAOA or annealing.

3. **The circuit is the same as Chapter 2, just bigger.** More variables → more qubits. More interactions → more ZZ gates. Same structure.

4. **Annealing is a different paradigm.** Continuous time evolution instead of discrete gates. The adiabatic theorem provides the guarantee. Tunnelling provides the (potential) advantage.

5. **Penalty weight matters.** $P$ must be large enough that violating a hard constraint is always worse than any feasible solution. But too large, and the energy landscape becomes dominated by the constraint surface, making the optimisation harder.
