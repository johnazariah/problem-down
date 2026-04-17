---
source_pdf: ../arxiv_2408.08292.pdf
pages: 80
extracted_at: 2026-04-17T12:32:43+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Optimization by Decoded Quantum Interferometry"
author: "Stephen P. Jordan; Noah Shutty; Mary Wootters; Adam Zalcman; Alexander Schmidhuber; Robbie King; Sergei V. Isakov; Tanuj Khattar; Ryan Babbush"
---

# arxiv_2408.08292

Original title: Optimization by Decoded Quantum Interferometry

Author metadata: Stephen P. Jordan; Noah Shutty; Mary Wootters; Adam Zalcman; Alexander Schmidhuber; Robbie King; Sergei V. Isakov; Tanuj Khattar; Ryan Babbush

Source PDF: ../arxiv_2408.08292.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Optimization by Decoded Quantum Interferometry

Stephen P. Jordan∗1, Noah Shutty†1, Mary Wootters2, Adam Zalcman1,
Alexander Schmidhuber1,3, Robbie King1,4, Sergei V. Isakov1,
Tanuj Khattar1, and Ryan Babbush1

1Google Quantum AI, Venice, CA 90291
2Departments of Computer Science and Electrical Engineering, Stanford University, Stanford, CA 94305
3Center for Theoretical Physics, Massachusetts Institute of Technology, Cambridge, MA 02139
4Department of Computing and Mathematical Sciences, Caltech, Pasadena, CA 91125

arXiv:2408.08292v5 [quant-ph] 22 Oct 2025

Achieving superpolynomial speedups for optimization has long been a central goal for quan-
tum algorithms. Here we introduce Decoded Quantum Interferometry (DQI), a quantum algo-
rithm that uses the quantum Fourier transform to reduce optimization problems to decoding
problems. For approximating optimal polynomial fits over finite fields, DQI achieves a super-
polynomial speedup over known classical algorithms. The speedup arises because the problem’s
algebraic structure is reflected in the decoding problem, which can be solved efficiently. We
then investigate whether this approach can achieve speedup for optimization problems that lack
algebraic structure but have sparse clauses. These problems reduce to decoding LDPC codes,
for which powerful decoders are known. To test this, we construct a max-XORSAT instance
where DQI finds an approximate optimum significantly faster than general-purpose classical
heuristics, such as simulated annealing. While a tailored classical solver can outperform DQI
on this instance, our results establish that combining quantum Fourier transforms with pow-
erful decoding primitives provides a promising new path toward quantum speedups for hard
optimization problems.

1
Introduction

NP-hardness results suggest that finding exact optima and even sufficiently good approximate op-
tima for worst-case instances of many optimization problems is likely out of reach for polynomial-
time algorithms both classical and quantum [1]. Nevertheless, there remain combinatorial opti-
mization problems, such as the closest vector problem, for which there is a large gap between
the best approximation achieved by a polynomial-time classical algorithm [2] and the strongest
complexity-theoretic inapproximability result [3]. When considering average-case complexity such
gaps become more prevalent, as few average-case inapproximability results are known. These gaps
present a potential opportunity for quantum computers, namely achieving in polynomial time an
approximation that requires superpolynomial time to achieve using known classical algorithms.
Quantum algorithms for combinatorial optimization have been the subject of intense research
over the last three decades [4–10], which has uncovered some evidence of possible superpolynomial
quantum speedup for certain optimization problems [11–17]. Nevertheless, the problem of finding

∗stephenjordan@google.com
†shutty@google.com

1

## Page 2

superpolynomial quantum advantage for optimization is extremely challenging and remains largely
open.
Here, we propose a quantum algorithm for optimization that uses interference patterns as
its main underlying principle. We call this algorithm Decoded Quantum Interferometry (DQI).
DQI uses a Quantum Fourier Transform to arrange that amplitudes interfere constructively on
symbol strings for which the objective value is large, thereby enhancing the probability of obtaining
good solutions upon measurement. Most prior approaches to quantum optimization have been
Hamiltonian-based [4,5], with a notable exception being the superpolynomial speedup due to Chen,
Liu, and Zhandry [13] for finding short lattice vectors, which uses Fourier transforms and can
be seen as an ancestor of DQI. Whereas Hamiltonian-based quantum optimization methods are
often regarded as exploiting the local structure of the optimization landscape (e.g.
tunneling
across barriers [18]), our approach instead exploits sparsity that is routinely present in the Fourier
spectrum of the objective functions for combinatorial optimization problems and can also exploit
more elaborate structure in the spectrum if present.
Before presenting evidence that DQI can efficiently obtain approximate optima not achievable by
known polynomial-time classical algorithms, we quickly illustrate the essence of the DQI algorithm
by applying it to max-XORSAT. We use max-XORSAT as our first example because, although it
is not the problem on which DQI has achieved its greatest success, it is the context in which DQI
is simplest to explain.
Given an m × n matrix B with m > n, the max-XORSAT problem is to find an n-bit string x
satisfying as many as possible among the m linear mod-2 equations Bx = v. Since we are working
modulo 2 we regard all entries of the matrix B and the vectors x and v as coming from the finite
field F2. The max-XORSAT problem can be rephrased as maximizing the objective function

m
X

f(x) =

i=1
(−1)vi+bi·x.
(1)

where bi is the ith row of B. Thus f(x) is the number among the m linear equations that are
satisfied minus the number unsatisfied.
From (1) one can see that the Hadamard transform of f is extremely sparse: it has m nonzero
amplitudes, which are on the strings b1, . . . , bm. The state P
x∈Fn
2 f(x) |x⟩is thus easy to prepare.
Simply prepare the superposition Pm
i=1(−1)vi |bi⟩and apply the quantum Hadamard transform.
(Here, for simplicity, we have omitted normalization factors.) Measuring the state P
x∈Fn
2 f(x) |x⟩
in the computational basis yields a biased sample, where a string x is obtained with probability
proportional to f(x)2, which slightly enhances the likelihood of obtaining strings of large objective
value relative to uniform random sampling.
To obtain stronger enhancement, DQI prepares states of the form

|P(f)⟩=
X

x∈Fn
2
P(f(x)) |x⟩,
(2)

where P is an appropriately normalized degree-ℓpolynomial. The Hadamard transform of such a
state always takes the form
ℓ
X

wk
qm
k

X

y∈Fm
2
|y|=k

k=0

2

(−1)v·y |BT y⟩,
(3)

## Page 3

ancillas
Dicke state

Figure 1: A schematic illustration of the steps of the DQI algorithm. Since the initial Dicke state
is of weight ℓ, the final polynomial P is of degree ℓ. Here, for simplicity, we take wℓ= 1 and wk = 0
for all k ̸= ℓ.

for some coefficients w0, . . . , wℓ. Here |y| denotes the Hamming weight of the bit string y. The DQI
algorithm prepares |P(f)⟩in five steps. The first step is to prepare the superposition Pℓ
k=0 wk |Dm,k⟩,
where
|Dm,k⟩=
1
qm
k

X

|y⟩
(4)

y∈Fm
2
|y|=k

is the Dicke state of weight k. Preparing such superpositions over Dicke states can be done using
O(m2) quantum gates using the techniques of [19, 20]. Second, the phase (−1)v·y is imposed by
applying the Pauli product Zv1
1 ⊗. . . ⊗Zvm
m . Third, the quantity BT y is computed into an ancilla
register using a reversible circuit for matrix multiplication. This yields the state

ℓ
X

wk
qm
k

X

y∈Fm
2
|y|=k

k=0

(−1)v·y |y⟩|BT y⟩.
(5)

The fourth step is to use the value BT y to infer y, which can then be subtracted from |y⟩, thereby
bringing it back to the all zeros state, which can be discarded. (This is known as “uncomputation”
[21].) The fifth and final step is to apply a Hadamard transform to the remaining register, yielding
|P(f)⟩. This sequence of steps is illustrated in Fig. 1.
The fourth step, in which |y⟩is uncomputed, is not straightforward because B is a nonsquare
matrix and thus inferring y from BT y is an underdetermined linear algebra problem. However, we
also know that |y| ≤ℓ. The problem of solving this underdetermined linear system with a Hamming

3

## Page 4

weight constraint is precisely the syndrome decoding problem for the classical error correcting code
C⊥= {d ∈Fm
2 : BT d = 0} with up to ℓerrors.
In general, syndrome decoding is an NP-hard problem [22]. However, when B is very sparse or
has certain kinds of algebraic structure, the decoding problem can be solved by polynomial-time
classical algorithms even when ℓis large (e.g. linear in m). By solving this decoding problem using
a reversible implementation of such a classical decoder one uncomputes |y⟩in the first register. If
the decoding algorithm requires T quantum gates, then the number of gates required to prepare
|P(f)⟩is O(T + m2).
Approximate solutions to the optimization problem are obtained by measuring |P(f)⟩in the
computational basis. The higher the degree of the polynomial in |P(f)⟩, the greater one can bias
the measured bit strings toward solutions with large objective value. However, this requires solving
a harder decoding problem, as the maximum number of errors is equal to the degree of P. Next,
we summarize how, by making optimal choice of P and judicious choice of decoder, DQI can be a
powerful optimizer for some classes of problems.

2
Results

Although DQI can be applied more broadly, the most general optimization problem that we apply
DQI to in this paper is max-LINSAT, which we define as follows.

Definition 2.1. Let Fp be a finite field and let B ∈Fm×n
p
. For each i = 1, . . . , m, let Fi ⊂Fp be an
arbitrary subset of Fp, which yields a corresponding constraint Pn
j=1 Bijxj ∈Fi. The max-LINSAT
problem is to find x ∈Fn
p satisfying as many as possible of these m constraints.

We focus primarily on the case that p has at most polynomially large magnitude and the subsets
F1, . . . , Fm are given as explicit lists. The max-XORSAT problem is the special case where p = 2
and |Fi| = 1 for all i.
Consider a max-LINSAT instance where the sets F1, . . . , Fm each have size r. Let ⟨s⟩be the
expected number of constraints satisfied by the symbol string sampled in the final measurement of
the DQI algorithm. Suppose we have a polynomial-time algorithm that can correct up to ℓbit flip
errors on codewords from the code C⊥= {d ∈Fm
p : BT d = 0}. Then, in polynomial time, DQI
achieves the following approximate optimum to the max-LINSAT problem

s

s


1 −r


+

⟨s⟩

ℓ
m

m =

p

m and ⟨s⟩

if r

p ≤1 −ℓ

!2


1 −ℓ

r
p

(6)

m

m = 1 otherwise. See Theorem 4.1 for the precise statement in the case of
perfect decoding and Theorem 10.1 for the analogous statement in the presence of decoding errors.
This is achieved by a specific optimal choice of the coefficients w0, . . . , wℓ, which can be classically
precomputed in polynomial time, as described in §9.
Note that r/p is the fraction of constraints that would be satisfied if the variables were assigned
uniformly at random. In the case r/p = 1/2, (6) becomes the equation of a semicircle, as illustrated
in Fig. 5. Hence we informally refer to (6) as the “semicircle law.”
Via (6), any result on decoding a class of linear codes implies a corresponding result regarding
the performance of DQI for solving a class of combinatorial optimization problems which are dual
to these codes. This enables two new lines of research in quantum optimization. The first is to

4

## Page 5

Fp

Fy1

y1

Q2(y)

Q1(y)

Fp

Figure 2: A stylized example of the Optimal Polynomial Intersection (OPI) problem. For y1 ∈Fp,
the orange set above the point y1 represents Fy1. Both of the polynomials Q1(y) and Q2(y) represent
solutions that have a large objective value, as they each intersect all but one set Fy.

harvest the coding theory literature for rigorous theorems on the performance of decoders for various
codes and obtain as corollaries guarantees on the approximation achieved by DQI for corresponding
optimization problems. The second is to perform computer experiments to determine the empirical
performance of classical heuristic decoders, which through equation (6) can be compared against the
empirical performance of classical heuristic optimizers. In this manner DQI can be benchmarked
instance-by-instance against classical heuristics, even for optimization problems far too large to
attempt on present-day quantum hardware. We next describe our results so far from each of these
two lines of research.
We first use rigorous decoding guarantees to analyze the performance of DQI on the following
problem.

Definition 2.2. Given integers n < p −1 with p prime, an instance of the Optimal Polynomial
Intersection (OPI) problem is as follows. Let F1, . . . , Fp−1 be subsets of the finite field Fp. Find
a polynomial Q ∈Fp[y] of degree at most n −1 that maximizes fOPI(Q) = |{y ∈{1, . . . , p −1} :
Q(y) ∈Fy}|, i.e. intersects as many of these subsets as possible.

An illustration of this problem is given in Fig. 2.
In §5 we show that OPI is a special case of max-LINSAT over Fp with m = p −1 constraints
in which B is a Vandermonde matrix and thus C⊥is a Reed-Solomon code. Syndrome decoding
for Reed-Solomon codes can be solved in polynomial time out to half the distance of the code, e.g.
using the Berlekamp-Massey algorithm [23]. Consequently, in DQI we can take ℓ= ⌊n+1

2 ⌋. For the
regime where r/p and n/p are constants and p is taken asymptotically large, the fraction of satisfied
constraints achieved by DQI using the Berlekamp Massey decoder can be obtained by substituting
ℓ
m = n

2p into (6).
OPI and special cases of it have been studied in several domains. In the coding theory literature,
OPI is studied under the name list-recovery, and in the cryptography literature it is studied under
the name noisy polynomial reconstruction/interpolation [24, 25].
OPI can also be viewed as a

5

## Page 6

generalization of the polynomial approximation problem, studied in [26–28], in which each set Fi is
a contiguous range of values in Fp. In §11 we analyze the algorithms from these literatures and find
that, for the parameter regime addressed by DQI, the best approximation achieved in polynomial
time classically is 1

2 + n

2p, via Prange’s algorithm. As shown in Figure 3, for r/p = 1/2 and any fixed
0 < n/p < 1, DQI with the Berlekamp-Massey decoder exceeds the satisfaction fraction achieved by
Prange’s algorithm in the limit of large p. Classically, the only methods we are aware of to exceed
the satisfaction fraction achieved by Prange’s algorithm are brute force search or slight refinements
thereof, which have exponential runtime. Thus, DQI achieves superpolynomial speedup for this
problem, assuming no polynomial-time algorithm is found that can match the satisfaction fraction
that DQI achieves.
Currently, there are no results directly showing that the OPI problem in the parameter regime
that we consider is classically intractable under any standard complexity-theoretic or cryptographic
assumptions. However, such results are known for certain limiting cases of the OPI problem, and
we propose the task of extending these results to regimes more relevant to DQI for future research.
The hardness of the special case of OPI when |f−1
i
(+1)| = 1, in a certain parameter regime, has
been proposed as a cryptographic assumption in [29], which has not been broken to our knowledge.
Finding exact optima for OPI with |f−1
i
(+1)| = 1 can be cast as maximum-likelihood decoding for
Reed-Solomon codes, which is known to be NP-hard [30,31]. Finding sufficiently good approximate
optima is known to be as hard as discrete log [32,33], but these hardness results do not match the
parameter regime addressed by DQI.
As a concrete example, for n ≃p/10 and r/p ≃1/2, the fraction of constraints satisfied by
Prange’s algorithm is 0.55, whereas DQI achieves 1/2 +
√

19/20 ≃0.7179. As a specific point of
comparison, we challenge the algorithms community to beat this by a classical polynomial time
algorithm. Interestingly, for these parameters, one statistically expects that solutions satisfying all
p−1 constraints exist, but they apparently remain out of reach of polynomial time algorithms both
quantum and classical.
To find classically intractable instances of OPI solvable by DQI with minimal quantum re-
sources, we find it is advantageous to choose n/p ≃r/p ≃1/2. For these parameters DQI achieves
satisfaction fraction 0.933. As discussed in §16, achieving this using classical algorithms known to
us has prohibitive computational cost for p as small as 521. The dominant cost in DQI+BM is
the reversible implementation of the subroutine to find the shortest linear feedback shift register
(LFSR) used in the Berlekamp-Massey algorithm. In §16 we use Qualtran [34] to find that at
p = 521 the LFSR can be found using approximately 1×108 logical Toffoli gates and 9×103 logical
qubits.
We next use computer experiments to benchmark the performance of DQI against classical
heuristics on average-case instances from certain families of max-XORSAT with sparse B. DQI
reduces such problems to decoding problems on codes with sparse parity check matrices. Such codes
are known as Low Density Parity Check (LDPC) codes.
Polynomial-time classical algorithms
such as belief propagation (BP) can decode randomly sampled LDPC codes up to numbers of
errors that nearly saturate information-theoretic limits [35–37]. This makes sparse max-XORSAT
an enticing target for DQI. Although we use max-XORSAT as a convenient testbed for DQI,
other commonly-studied optimization problems such as max-k-SAT could be addressed similarly.
Specifically, consider any binary optimization problem in which the objective function counts the
number of satisfied constraints, where each constraint is a Boolean function of at most k variables.
By taking the Hadamard transform of the objective function, one converts such a problem into an

6

## Page 7

instance of weighted max-k-XORSAT, where the number of variables is unchanged and the number
of constraints has been increased by at most a factor of 2k.
Although we are able to analyze the asymptotic average case performance of DQI rigorously
we do not restrict the classical competition to algorithms with rigorous performance guarantees.
Instead, we choose to set a high bar by also attempting to beat the empirical performance of
classical heuristics that lack such guarantees.
Through careful tuning of sparsity patterns in B, we are able to find some families of sparse
max-XORSAT instances for which DQI with standard belief propagation decoding finds solutions
satisfying a larger fraction of constraints than we are able to find using a comparable number of
computational steps by any of the general-purpose classical optimization heuristics that we tried,
which are listed in Table 1.
However, unlike our OPI example, we do not put this forth as a
potential example of superpolynomial quantum advantage.
Rather, we are able to construct a
tailored classical algorithm specialized to these instances which, with seven minutes of runtime,
finds solutions where the fraction of constraints satisfied slightly beats DQI+BP. As discussed in
§12, our tailored heuristic is a variant of simulated annealing that assigns temperature-dependent
weights to the terms in the cost function determined by how many variables they contain.
The comparison against simulated annealing is complicated by the fact that, as shown in §11.2,
the fraction of clauses satisfied by simulated annealing increases as a function of the duration of the
anneal. Thus there is not a unique sharply-defined number indicating the maximum satisfaction
fraction reachable by simulated annealing. DQI reduces our sparsity-tuned max-XORSAT problem
to an LDPC decoding problem that our implementation of belief propagation solves in approxi-
mately 8 seconds on a single core, excluding the time used to load and parse the instance. Thus,
a natural point of comparison is the result obtained by simulated annealing with similar runtime.
By running our optimized C++ implementation of simulated annealing for 8 seconds, we are only
able to reach 0.764. If we allow parallel execution of multiple anneals and increase our runtime
allowance, we are able to eventually replicate the satisfaction fraction achieved by DQI+BP using
simulated annealing. The shortest anneal that achieved this used five cores and ran for 73 hours,
i.e. five orders of magnitude longer than our belief propagation decoder. Although dependent on
implementation details, we can take this ratio of runtimes as a rough indicator of the ratio of com-
putational steps. In the context of DQI the decoder would need to be implemented as a reversible
circuit and subject to overhead due to quantum error correction, so this should not be interpreted
as an indicator of quantum versus classical runtime.

3
Discussion

The idea that quantum Fourier transforms could be used to achieve reductions between problems
on lattices and their duals originates in the early 2000s in work of Regev, Aharonov, and Ta-
Shma [38–41]. Linear codes, as considered here, are closely analogous to lattices but over finite
fields.
By considering lattices with only geometric structure no quantum speedups were found
using these reductions until the 2021 breakthrough of Chen, Liu, and Zhandry [13], which obtains
a superpolynomial speedup for a constraint satisfaction problem by combining these ideas with
an intrinsically quantum decoding method. Other recent explorations of Regev-style reductions to
general unstructured codes and lattices are given in [17,42,43]. Here, we restrict attention to codes
defined by matrices that are either sparse or algebraically structured and in the latter case are able
to obtain an apparent superpolynomial quantum speedup for an optimization problem.

7

## Page 8

1
10

1
2

⟨s⟩/p

0
1

n/p

Figure 3:
Here we plot the expected fraction ⟨s⟩/p of satisfied constraints achieved by DQI with
the Berlekamp-Massey decoder and by Prange’s algorithm for the OPI problem in the balanced
case r/p = 1/2, as a function of the ratio of variables to constraints n/p. At n/p = 1/10 Prange’s
algorithm satisfies a fraction 0.55 of the clauses whereas DQI satisfies ⟨s⟩/p = 1/2 +
√

19/20 ≃
0.7179. As a concrete challenge to the classical algorithms community we propose matching or
exceeding this value in polynomial time. In our concrete resource estimation in §16 we consider
n/p = 1/2, where OPI achieves ⟨s⟩/p = 1/2+
√

3/4 ≃0.9330 and Prange’s algorithm achieves 0.75.

Table 1:
Here, we compare DQI, using a standard belief propagation decoder, against classical
algorithms for a randomly-generated max-XORSAT instance with irregular degree distribution
specified in §12. We consider an example instance with 31, 216 variables and 50, 000 constraints.
The classical algorithms above are defined in §11. For simulated annealing the satisfaction fraction
grows with runtime, so we report two numbers. The first is the optimum reachable by limiting
simulated annealing to the same runtime used by belief propagation to solve the problem to which
the max-XORSAT instance is reduced by DQI (8 seconds × 1 core) and the second is for the
shortest anneal that matched satisfaction fraction achieved by DQI+BP (73 hours × 5 cores).

8

## Page 9

Recently, Yamakawa and Zhandry have also considered the application of Regev-style reductions
to a problem with extra structure and obtained quantum advantage [44]. They define an oracle
problem that they prove can be solved using polynomially many quantum queries but requires
exponentially many classical queries. Their problem is essentially equivalent to max-LINSAT over
an exponentially large finite field F2t, where the sets F1, . . . , Fm are defined by random oracles and
the matrix B is obtained from a folded Reed-Solomon code. In §14 we recount the exact definition
of the Yamakawa-Zhandry problem and argue that DQI can be extended to the Yamakawa-Zhandry
problem and in this case likely yields solutions satisfying all constraints. Although problems with
exponentially large F1, . . . , Fm defined by oracles are far removed from industrial optimization
problems, this limiting case provides evidence against the possibility of efficiently simulating DQI
with classical algorithms and thereby “dequantizing” it, as has happened with some prior quantum
algorithms proposed as potential superpolynomial speedups [45]. More precisely, our argument
suggests that DQI cannot be dequantized by any relativizing techniques, in the sense of [46].
We conclude by noting that the work reported here initiates the exploration of quantum
speedups through DQI but is very far from completing it. In particular, we highlight three av-
enues for future work: multivariate OPI, custom decoders for solving max-XORSAT by DQI, and
sampling problems. First, we note that the DQI algorithm can be straightforwardly adapted to
solve the multivariate generalization of OPI. As shown in §15, multivariate OPI gets reduced by
DQI to the decoding of Reed-Muller codes. Known polynomial-time classical algorithms can de-
code all Reed-Muller codes out to half their distance [47]. (Reed-Solomon codes are the univariate
special case.) Consequently, one expects a region of parameter space for which DQI achieves super-
polynomial speedup on multivariate OPI, which includes the speedup on univariate OPI presented
here as a special case. Mapping out this region of quantum advantage remains for future work.
Second, we note that our exploration of DQI applied to max-XORSAT is far from exhaustive.
In particular, (6) enables a benchmark-driven approach to the development of tailored heuristics
for decoding designed to achieve quantum speedup on some class of optimization problems via DQI.
This search can be guided by upper bounds on the performance of DQI that, via the semicircle law,
follow from information-theoretic limits on decoding. Such an analysis is given in §13 and shows
that for D-regular max-k-XORSAT instances, the upper bound on the possible performance of DQI
with classical decoders is already exceeded by the empirical performance of simulated annealing
when k is too small relative to D. Additionally, we are able to compare the performance of DQI
against the Quantum Approximate Optimization Algorithm (QAOA) for various ensembles of max-
k-XORSAT instances at k = 2 and k = 3 and on all of these QAOA exceeds the upper bound on
performance for DQI with classical decoders.
These limits show that, for DQI to achieve advantage on max-k-XORSAT, one must either go
to large k or move to quantum decoders that exploit the coherence of the bit flip errors. Large-k
problems are reduced by DQI to decoding problems in which the parity check matrix is denser than
in typical LDPC codes. The increased density degrades the performance of belief propagation.
This suggests future research developing decoders to tolerate denser parity check matrices than are
typically used. Despite some progress along these lines [48–54] this remains an underexplored area
compared to the decoding of codes with very sparse parity check matrices. With quantum decoders,
it remains information-theoretically possible for DQI to achieve advantage over known polynomial-
time classical and quantum algorithms, even for small k. Realizing this potential advantage depends
on the development of polynomial-size quantum circuits for this quantum decoding problem. Some
exciting progress on this problem has been reported in [13,42,55].

9

## Page 10

Third, we note that DQI produces unbiased samples, in which the probability of obtaining a
given solution to an optimization problem is constant across all solutions achieving a given objective
value. This guarantee of fair sampling is absent for most classical optimization algorithms and has
known applications to very hard problems of approximate counting [56].

Data availability: The problem instances that we describe, the code used in our computer
experiments and resource estimation, and the raw data from our plots are available at https:
//doi.org/10.5281/zenodo.13327870.

Acknowledgments: We thank Robin Kothari, Ryan O’Donnell, Edward Farhi, Hartmut Neven,
Kostyantyn Kechedzhi, Sergio Boixo, Vadim Smelyanskiy, Yuri Lensky, Dorit Aharonov, Oded
Regev, Jarrod McClean, Madhu Sudan, Umesh Vazirani, Yuval Ishai, Brett Hemenway Falk, Oscar
Higgott, John Azariah, Ojas Parekh, Jon Machta, Helmut Katzgraber, Craig Gidney, Noureldin
Yosri and Dmitri Maslov for useful discussions. MW’s work on this project was funded by a grant
from Google Quantum AI.

Organization: In §4, we state Theorem 4.1, which characterizes the performance of DQI on max-
LINSAT problems in terms of the ability to solve the corresponding decoding problem. In §5 we
formally define the OPI problem and apply Theorem 4.1 to predict DQI’s performance on OPI. In
§6 we discuss how DQI performs on unstructured sparse instances of sparse max-XORSAT using
belief propagation decoding. In §7 we discuss the long line of prior work related to DQI. In §8 we
explain the DQI algorithm in detail. In §9 we prove Theorem 4.1. In §10 we state and prove 10.1,
which is an analogue of Theorem 4.1 for the setting where p = 2 and ℓexceeds half the distance
of the code C⊥. In §11 we discuss several existing classical and quantum optimization algorithms
and compare their performance with DQI. We follow this in §12 by showing how we construct an
instance for which DQI, using belief propagation decoding, can achieve an approximate optimum
that is very difficult to replicate using simulated annealing. In §13 we derive information-theoretic
upper bounds on the approximate optima achievable by DQI, which depend on whether one is
considering classical or quantum decoders. In §14 we generalize the max-LINSAT problem and the
DQI algorithm to folded codes and extension fields in order to shed some light on DQI’s potential
applicability to the problem considered by Yamakawa and Zhandry in [44]. In §15 we generalize the
OPI problem to multivariate polynomials. Lastly, in §16 we obtain concrete resource requirements
(qubits, Clifford gates, and non-Clifford gates) to apply DQI, using the Berlekamp Massey decoder,
to the OPI problem.

4
Characterizing the Performance of DQI

DQI reduces the problem of approximating max-LINSAT to the problem of decoding the linear
code C⊥over Fp whose parity check matrix is BT . That is,

C⊥= {d ∈Fm
p : BT d = 0}.
(7)

This decoding problem is to be solved in superposition, such as by a reversible implementation of
any efficient classical decoding algorithm. If C⊥can be efficiently decoded out to ℓerrors then,

10

## Page 11

given any appropriately normalized degree-ℓpolynomial P, DQI can efficiently produce the state

|P(f)⟩=
X

x∈Fnp
P(f(x)) |x⟩.
(8)

Upon measuring in the computational basis one obtains a given string x with probability P(f(x))2.
One can choose P to bias this distribution toward strings of large objective value. Larger ℓallows
this bias to be stronger, but requires the solution of a harder decoding problem.
More quantitatively, in §9, we prove the following theorem.

Theorem 4.1. Given a prime p and B ∈Fm×n
p
, let f(x) = Pm
i=1 fi(Pn
j=1 Bijxj) be a max-LINSAT
objective function. Suppose |f−1
i
(+1)| = r for all i = 1, . . . , m and some r ∈{1, . . . , p −1}. Given
a degree-ℓpolynomial P, let ⟨s⟩be the expected number of satisfied constraints for the symbol string
obtained upon measuring the corresponding DQI state |P(f)⟩in the computational basis. Suppose
2ℓ+ 1 < d⊥where d⊥is the minimum distance of the code C⊥= {d ∈Fm
p : BT d = 0}, i.e. the
minimum Hamming weight of any nonzero codeword in C⊥. In the limit m →∞, with ℓ/m fixed,
the optimal choice of degree-ℓpolynomial P to maximize ⟨s⟩yields

s

s


1 −r


+

⟨s⟩

ℓ
m

m =

p

m and ⟨s⟩

if r

p ≤1 −ℓ

m = 1 otherwise.

!2


1 −ℓ

r
p

(9)

m

Theorem 4.1 assumes that 2ℓ+ 1 < d⊥, which is the same as requiring that C⊥can be in
principle decoded from up to ℓworst-case errors. Further, if this decoding can be done efficiently,
then the DQI algorithm is also efficient. In our analysis, we show how to relax these assumptions.
In particular, in Theorem 10.1 we show that even when 2ℓ+1 ≥d⊥and it is not possible to decode
ℓworst-case errors, an efficient algorithm that succeeds with high probability over random errors
can be used in the DQI algorithm to efficiently achieve a fraction of satisfied constraints close to
the one given by (9), at least for max-XORSAT problems Bx max
= v with average-case v.
For the balanced case r →p/2, (9) simplifies to

s

⟨s⟩

m = 1

ℓ
m

2 +


1 −ℓ


,
(10)

m

i.e. the equation of a semicircle.
DQI reduces the problem of satisfying a large number of linear constraints to the problem of
correcting a large number of errors in a linear code. Decoding linear codes is also an NP-hard
problem in general [22]. So, one must ask whether this reduction is ever advantageous. We next
present evidence that it can be.

5
Optimal Polynomial Intersection

The problem which provides our clearest demonstration of the power of DQI is the OPI problem,
as specified in Definition 2.2 and illustrated in Fig. 2. In this section, we explain how to apply DQI

11

## Page 12

to OPI, and identify a parameter regime for OPI where DQI outperforms all classical algorithms
known to us.
We first observe that OPI is equivalent to a special case of max-LINSAT. Let q0, . . . , qn−1 ∈Fp
be the coefficients in Q:

n−1
X

Q(y) =

j=0
qj yj.
(11)

Recall that a primitive element of a finite field is an element such that taking successive powers of
it yields all nonzero elements of the field. Every finite field contains one or more primitive elements.
Thus, we can choose γ to be any primitive element of Fp and re-express the OPI objective function
as
fOPI(Q) = |{i ∈{0, 1, . . . , p −2} : Q(γi) ∈Fγi}|.
(12)

Next, let

fi(x) =
 +1
if x ∈Fγi
−1
otherwise
(13)

for i = 0, . . . , p −2 and define the matrix B by

Bij = γi×j
i = 0, . . . , p −2
j = 0, . . . , n −1.
(14)

Then the max-LINSAT objective function is f(q) = Pp−2
i=0 fi(bi ·q) where q = (q0, . . . , qn−1)T ∈Fn
p
and bi is the ith row of B. But bi · q = Q(γi), so f(q) = 2 · fOPI(Q) −(p −1) which means that
the max-LINSAT objective function f and the OPI objective function fOPI are equivalent. Thus
we have re-expressed our OPI instance as an equivalent instance of max-LINSAT with m = p −1
constraints.
We will apply DQI to the case where

|f−1
i
(+1)| = ⌊p/2⌋
∀i = 0, . . . , p −2.
(15)

By (15), in the limit of large p we have |f−1
i
(+1)|/p →1/2 and |f−1
i
(−1)|/p →1/2 for all i. We
call functions with this property “balanced.”
When B has the form (14), then C⊥= {d ∈Fp−1
p
: BT d = 0} is a Reed-Solomon code with
alphabet Fp, block length p −1, dimension p −n −1, and distance n + 1. Note that our definition
of n is inherited from the parameters of the max-LINSAT instances that we start with and hence
our notations for block length and dimension unfortunately do not conform to standard notations
from coding theory.
Maximum likelihood syndrome decoding for Reed-Solomon codes can be solved in polynomial
time out to half the distance of the code, e.g. using the Berlekamp-Massey algorithm [23]. Con-
sequently, in DQI we can take ℓ= ⌊n+1

2 ⌋. In (10) we can thus set the number of errors corrected
ℓ→n

2 and the number of constraints m →p, which shows that the asymptotic performance of
DQI using Berlekamp-Massey is

s

⟨s⟩DQI+BM

p
= 1

n
2p

2 +


1 −n


.
(16)

2p

Here we have approximated n + 1 by n and p −1 by p since this is an asymptotic formula anyway.
For exact expressions at finite size see §9. The largest asymptotic fraction of satisfied clauses for

12

## Page 13

OPI that we know how to obtain classically in polynomial time is

⟨s⟩Prange

m
= 1

2 + n

2p,
(17)

which is achieved by Prange’s algorithm. These are plotted in Fig. 3, where one sees that DQI+BP
exceeds Prange’s algorithm for all n/p ∈(0, 1). (See §11.3 for a description of Prange’s algorithm.)
Therefore, the Optimal Polynomial Intersection problem demonstrates the power of DQI. As-
suming no polynomial-time classical algorithm for this problem is found that can match this fraction
of satisfied constraints, this constitutes an example of an superpolynomial quantum speedup. It is
noteworthy that our quantum algorithm is not based on a reduction to an Abelian Hidden Sub-
group or Hidden Shift problem. The margin of victory for the approximation fraction (0.7179 vs.
0.55) is also satisfyingly large. Nevertheless, it is also of great interest to investigate whether such
a quantum speedup can be obtained for more generic constraint satisfaction problems, with less
underlying structure, as we do in the next section.
Before moving on to unstructured optimization problems, we make two remarks.

Remark 5.1 (Relationship to the work of Yamakawa and Zhandry). First, we note that the
algorithm of Yamakawa and Zhandry [44]—which solves a version of OPI—does not apply in our
setting. As discussed in §11.6, the parameters of our OPI problem are such that solutions satisfying
all constraints are statistically likely to exist but these exact optima seem to be computationally
intractable to find using known classical algorithms. The quantum algorithm of Yamakawa and
Zhandry, when it can be used, produces a solution satisfying all constraints. However, the quantum
algorithm of Yamakawa and Zhandry has high requirements on the decodability of C⊥. Specifically,
for the “balanced case” in which |fi(+1)| ≃|fi(−1)| for all i, the requirement is that C⊥can be
decoded from a 1/2 fraction of random errors. For our OPI example, C⊥has rate 9/10. Shannon’s
noisy-channel coding theorem implies that it is not possible to reliably decode C⊥in this setting.
Thus, the quantum algorithm of Yamakawa and Zhandry is not applicable.

Remark 5.2 (Classical Complexity of OPI). Proving rigorous classical hardness guarantees for
OPI seems like a challenging problem. OPI, and OPI-like problems, have been proposed as crypto-
graphically hard problems. As discussed in §11.7, a version of OPI in a different parameter regime
was proposed as a hardness assumption for cryptographic applications by [24]. This conjecture was
broken by [25] using lattice attacks, but we demonstrate in §11.7 that these attacks do not apply
in our parameter regime. Later work [29] proposed two updated hardness assumptions, which each
would imply the hardness of a special case of OPI.1 These assumptions have yet to be broken to the
best of our knowledge, and DQI does not seem to be an effective attack on them in the parameter
regimes of interest.
There are other problems related to OPI that are known to be computationally hard, under stan-
dard assumptions. For example, the problem of maximum-likelihood decoding for Reed-Solomon
Codes—which is the case of OPI when |f−1
i
(+1)| = 1 for all i—is known to be NP-hard [30, 31].
List-decoding and bounded-distance decoding for Reed-Solomon codes to a large enough radius—
also related to OPI when |f−1
i
(+1)| = 1—is known to be as hard as discrete log [32,33]. Theorem 4.1

1In more detail, the first problem assumed to be hard is related to bounded distance decoding for Reed-Solomon
codes from random errors, which corresponds to OPI when |f −1
i
(+1)| = 1. The second problem can be viewed as a
generalization of OPI to randomly folded Reed-Solomon codes with |f −1
i
(+1)| larger than 1; we show in Appendix 14
that DQI can apply to folded codes, but it does not yield useful attacks in the relevant parameter regime.

13

## Page 14

does not provide strong performance guarantees for DQI applied to these problems. It would be
very interesting to show that OPI (in a parameter regime |f−1
i
(+1)| ∝p where Theorem 4.1 does
give strong performance guarantees) is classically hard under standard cryptographic assumptions.

6
Random Sparse max-XORSAT

In this section, we consider average-case instances from certain families of bounded degree max-k-
XORSAT. In a max-k-XORSAT instance with degree bounded by D, each constraint contains at
most k variables and each variable is contained in at most D constraints. In other words, the matrix
B ∈Fm×n
2
defining the instance has at most k nonzero entries in any row and at most D nonzero
entries in any column. DQI reduces this to decoding the code C⊥whose parity check matrix is BT .
Codes with sparse parity check matrices are known as Low Density Parity Check (LDPC) codes.
Randomly sampled LDPC codes are known to be correctable from a near-optimal number of random
errors (asymptotically as m grows) [35]. Consequently, in the limit of large m they can in principle
be decoded up to a number of random errors that nearly saturates the information-theoretic limit
dictated by the rate of the code. When k and D are very small, information-theoretically optimal
decoding for random errors can be closely approached by polynomial-time decoders such as belief
propagation [36,37]. This makes sparse max-XORSAT a promising target for DQI.
In this section we focus on benchmarking DQI with standard belief propagation decoding
(DQI+BP) against simulated annealing on max-k-XORSAT instances. We choose simulated an-
nealing as our primary classical point of comparison because it is often very effective in practice
on sparse constraint satisfaction problems and also because it serves as a representative example
of local search heuristics. Local search heuristics are widely used in practice and include greedy
algorithms, parallel tempering, TABU search, and many quantum-inspired optimization methods.
As discussed in §11.1, these should all be expected to have similar scaling behavior with D on
average-case max-k-XORSAT with bounded degree. Because of simulated annealing’s simplicity,
representativeness, and strong performance on average-case constraint satisfaction problems, beat-
ing simulated annealing on some class of instances is a good first test for any new classical or
quantum optimization heuristic.
It is well-known that max-XORSAT instances become harder to approximate as the degree of
the variables is increased [57, 58]. Via DQI, a max-XORSAT instance of degree D is reduced to
a problem of decoding random errors for a code in which each parity check contains at most D
variables. As D increases, with m/n held fixed, the distance of the code and hence its performance
under information-theoretically optimal decoding are not degraded at all. Thus, as D grows, the
fraction of constraints satisfied by DQI with information-theoretically optimal decoding would
not degrade. In contrast, classical optimization algorithms based on local search yield satisfaction
fractions converging toward 1/2 in the limit D →∞which is no better than random guessing. Thus
as D grows with k/D fixed, DQI with information-theoretically optimal decoding will eventually
surpass all classical local search heuristics.
(See also Fig.
13.)
However, for most ensembles
of codes, the number of errors correctable by standard polynomial-time decoders such as belief
propagation falls increasingly short of information-theoretic limits as the degree D of the parity
checks increases. Thus increasing D generically makes the problem harder both for DQI+BP and
for classical optimization heuristics.
Despite this challenge, we are able to find some unstructured families of sparse max-XORSAT
instances for which DQI with standard belief propagation decoding finds solutions satisfying a

14

## Page 15

fraction of constraints that is very difficult to replicate using simulated annealing. We do so by
tuning the degree distribution of the instances. For example, in §12, we generate an example max-
XORSAT instance from our specified degree distribution, which has 31, 216 variables and 50, 000
constraints, where each constraint contains an average of 53.973 variables and each variable is
contained in an average of 86.451 constraints. We find that DQI with standard belief propagation
decoding can find solutions in which the fraction of constraints satisfied is at least 0.831. It does so
by reducing this problem to a decoding problem that can be solved by our implementation of belief
propagation in 8 seconds, excluding the time needed to load and parse the instance. In contrast,
our implementation of simulated annealing requires approximately 73 hours to reach this, even
when allowed five cores in parallel; restricted to 8 seconds of runtime on a single core it is only able
to satisfy 0.764.
Furthermore, as shown in Table 1, DQI+BP achieves higher satisfaction fraction than we are
able to obtain in a comparable number of computational steps using any of the general-purpose
classical optimization algorithms that we tried.
However, unlike our OPI example, we do not
put this forth as an example of quantum advantage. Rather, we are able to construct a tailored
classical algorithm specialized to these instances which, within seven minutes of runtime, finds
solutions where the fraction of constraints satisfied is 0.88, thereby slightly beating DQI+BP.

7
Relation to Other Work

DQI is related to a family of quantum reductions that originate with the work of Aharonov, Ta-
Shma, and Regev [38, 40]. In this body of work the core idea is to use the Fourier convolution
theorem to obtain reductions between nearest lattice vector problems and shortest lattice vector
problems. In this section we summarize the other quantum algorithms using this idea and discuss
their relationship to DQI.
In [13], Chen, Liu, and Zhandry introduce a novel and powerful intrinsically-quantum decoding
method that they call filtering, which can in some cases solve quantum decoding problems for
which the analogous classical decoding problems cannot be solved by any known efficient classical
algorithm. By combining this decoding method with a Regev-style reduction, they are able to
efficiently find approximate optima to certain shortest vector problems defined using the infinity
norm for which no polynomial-time classical solution is known. Due to the use of the infinity norm,
the problem solved by the quantum algorithm of [13] is one of satisfying all constraints, rather
than the more general problem of maximizing the number of constraints satisfied, as is addressed
by DQI. Although conceptualized differently, and implemented over the space of codewords rather
than the space of syndromes, the algorithm of [13] is similar in spirit to DQI and can be regarded
as a foundational prior work.
It is particularly noteworthy that the apparent superpolynomial
quantum speedup achieved in [13], through the use of quantum decoders, is obtained for a purely
geometrical problem with no algebraic structure.
In [44], Yamakawa and Zhandry define an oracle problem that they prove can be solved us-
ing polynomially many quantum queries but requires exponentially many classical queries. Their
problem is essentially a class of instances of max-LINSAT over an exponentially large finite field
F2t, where the functions f1, . . . , fm are defined by random oracles and the matrix B has algebraic
structure. In §14 we recount the exact definition of the Yamakawa-Zhandry problem and show how
DQI can be extended to the Yamakawa-Zhandry problem. In the problem defined by Yamakawa
and Zhandry, the truth tables for the constraints are defined by random oracles, and therefore, in

15

## Page 16

the language of Theorem 4.1, r/p = 1/2. Furthermore, the Yamakawa-Zhandry instance is designed
such that C⊥can be decoded with exponentially small failure probability if half of the symbols are
corrupted by errors. Thus, in the language of Theorem 4.1, we can take ℓ/m = 1/2. In this case, if
we extrapolate (9) to the Yamakawa-Zhandry regime, one obtains ⟨s⟩/m = 1, indicating that DQI
should find a solution satisfying all constraints. The quantum algorithm given by Yamakawa and
Zhandry for finding a solution satisfying all constraints is different from DQI, but similar in spirit.
Extrapolation of the semicircle law is necessary because the Yamakawa-Zhandry example does
not satisfy 2ℓ+ 1 < d⊥, and therefore the conditions of Theorem 4.1 are not met. In Theorem
10.1 we prove a variant of the semicircle law for 2ℓ+ 1 > d⊥for max-XORSAT with average case
v. The Yamakawa-Zhandry problem uses a random oracle, which is the direct generalization to Fq
of average case v. It seems likely that the proof of Theorem 10.1 can be generalized to from F2
to Fq with arbitrary q at the cost of additional technical complications but without the need for
conceptual novelty. In this case the claim that DQI encompasses the Yamakawa-Zhandry upper
bound on quantum query complexity could be made rigorous.
An important difference between our OPI results and the exponential quantum query complexity
speedup of Yamakawa and Zhandry is that the latter depends on Fq being an exponentially large
finite field. This allows Yamakawa and Zhandry to obtain an information-theoretic exponential
classical query-complexity lower bound, thus making their separation rigorous. In contrast, our
apparent superpolynomial speedup for OPI uses a finite field of polynomial size, in which case the
truth tables are polynomial size and known explicitly. This regime is more relevant to real-world
optimization problems. The price we pay is that the classical query complexity in this regime is
necessarily polynomial. This means that the information-theoretic argument of [44] establishing
an exponential improvement in query complexity does not apply in our setting. Instead, we argue
heuristically for an superpolynomial quantum speedup, by comparing to known classical algorithms.
In [43], Debris-Alazard, Remaud, and Tillich construct a quantum reduction from the approx-
imate shortest codeword problem on a code C to the bounded distance decoding problem on its
dual C⊥. The shortest codeword problem is closely related to max-XORSAT: the max-XORSAT
problem is to find the codeword in C = {Bx | x ∈Fn
2} that has smallest Hamming distance from
a given bit string v, whereas the shortest codeword problem is to find the codeword in C \ {0}
with smallest Hamming weight. Roughly speaking, then, the shortest codeword problem is the
special case of max-XORSAT where v = 0 except that the trivial solution 0 is excluded. Although
conceptualized quite differently, the reduction of [43] is similar to the p = 2 special case of DQI in
that it is achieved via a quantum Hadamard transform.
Another interesting connection between DQI and prior work appears in the context of planted
inference problems, such as planted kXOR, where the task is to recover a secret good assignment
planted in an otherwise random kXOR instance. It has been recently shown that quantum algo-
rithms can achieve polynomial speedups for planted kXOR by efficiently constructing a guiding
state that has improved overlap with the planted solution [59]. Curiously, the ℓth order guiding
state studied in [59] seems related to the ℓth order DQI state presented here. The key conceptual
difference is that, to obtain an assignment that satisfies a large number of constraints, the DQI state
in this work is measured in the computational basis, whereas the guiding state in [59] is measured in
the eigenbasis of the so-called Kikuchi matrix, and subsequently rounded. It is interesting that for
the large values of ℓstudied in this work, the (Fourier-transformed) Kikuchi matrix asymptotically
approaches a diagonal matrix such that its eigenbasis is close to the computational basis.
Next, we would like to highlight [42] in which Chailloux and Tillich introduce a method for

16

## Page 17

decoding superpositions of errors, which they use in the context of a Regev-style reduction. Their
method to solve the quantum decoding problem is based on a technique called unambiguous state
discrimination (USD). Roughly speaking, USD is a coherent quantum rotation which allows us to
convert bit-flip error into erasure error. If the resulting erasure error rate is small enough, one
can decode perfectly using Gaussian elimination. Interestingly, this is efficient regardless of the
sparsity of the code. Curiously, however, Chailloux and Tillich find that the resulting performance
of this combination of quantum algorithms yields performance for the shortest codeword problem
that exactly matches that of Prange’s algorithm [60].
Lastly, we note that since we posted the first version of this manuscript as an arXiv preprint
in August, 2024 there have already been some works that nicely build upon DQI. In particular, we
would like to highlight [61] in which Chailloux and Tillich observe that for p > 2 the distribution
over errors on a given corrupted symbol in the decoding problem faced by DQI is non-uniform.
Information-theoretically this is more advantageous than uniform errors. Furthermore, they show
that this advantage can be exploited by polynomial-time decoders, thereby improving the approx-
imation ratio efficiently achievable by DQI. Additionally, in [62], a concrete resource analysis is
carried out for DQI in which the decoding of C⊥is carried out using a reversible circuit implement-
ing information set decoding.

8
Decoded Quantum Interferometry

Here we describe in full detail the Decoded Quantum Interferometry algorithm, illustrated in Fig.
4. We start with DQI for max-XORSAT, which is the special case of max-LINSAT with F = F2.
Then we describe DQI with F = Fp for any prime p. In each case, our explanation consists of
a discussion of the quantum state we intend to create followed by a description of the quantum
algorithm used to create it. The generalization of DQI to extension fields is given in §14.
In this section, we assume throughout that 2ℓ+1 < d⊥. In some cases we find that it is possible
to decode more than d⊥/2 errors with high probability, in which case we can use ℓexceeding this
bound. This contributes some technical complications to the description and analysis of the DQI
algorithm, which we defer to §10.

8.1
DQI for max-XORSAT

8.1.1
DQI Quantum State for max-XORSAT

Recall that the objective function for max-XORSAT can be written in the form f = f1 + . . . + fm,
where fi takes the value +1 if the ith constraint is satisfied and −1 otherwise. More concretely, the
function defined by

m
X

f(x)
=

i=1
fi(bi · x)
(18)

fi(bi · x)
=
(−1)vi(−1)bi·x,
(19)

expresses the number of constraints satisfied minus the the number of constraints unsatisfied by
the bit string x.

17

## Page 18

Figure 4: Decoded Quantum Interferometry over F2. The algorithm begins with a computation,
on a classical computer, of the principal eigenvector (w0, . . . , wℓ)T of a certain matrix A(m,ℓ,0).
P(f) is a degree-ℓpolynomial that enhances the probability of sampling x ∈Fn
2 with high value
of the objective f. Index k ranges over {0, . . . , ℓ} and y over the set {y ∈Fm
2 : |y| = k} of m-bit
strings of Hamming weight k. Weight register qubits may be reused for the syndrome register. If
2ℓ+ 1 < d⊥, the postselection succeeds with probability ≥1 −εℓ, where εℓis the decoding failure
rate on random weight-ℓerrors.

18

## Page 19

Given an objective of the form f = f1 + . . . + fm and a degree-ℓunivariate polynomial

ℓ
X

P(f) =

k=0
αkfk,
(20)

we can regard P(f) as a degree-ℓmultivariate polynomial in f1, . . . , fm. Since f1, . . . , fm are ±1-
valued we have f2
i = 1 for all i. Consequently, we can express P(f) as

ℓ
X

P(f) =

k=0
ukP (k)(f1, . . . , fm),
(21)

where P (k)(f1, . . . , fm) is the degree-k elementary symmetric polynomial, i.e. the unweighted sum
of all
m
k

products of k distinct factors from f1, . . . , fm.
For simplicity, we will henceforth always assume that the overall normalization of P has been
chosen so that the state |P(f)⟩= P
x∈Fn
2 P(f(x)) |x⟩has unit norm. In analogy with equation

(21), we will write the DQI state |P(f)⟩as a linear combination of |P (0)⟩, . . . , |P (ℓ)⟩, where

|P (k)⟩:=
1
q

2nm
k

X

x∈Fn
2
P (k)(f1(b1 · x), . . . , fm(bm · x)) |x⟩.
(22)

Thus, by (19),

P (k)(f1, . . . , fm)
=
X

i1,...,ik
distinct

=
X

i1,...,ik
distinct

=
X

y∈Fm
2
|y|=k

fi1 × . . . × fik
(23)

(−1)vi1+...+vik(−1)(bi1+...+bik)·x
(24)

(−1)v·y(−1)(BT y)·x,
(25)

where |y| indicates the Hamming weight of y. From this we see that the Hadamard transform of
|P (k)⟩is

| eP (k)⟩:= H⊗n |P (k)⟩=
1
qm
k

X

(−1)v·y |BT y⟩.
(26)

y∈Fm
2
|y|=k

For the set of y ∈Fn
2 with |y| < d⊥/2 the corresponding bit strings BT y are all distinct. Therefore,
| eP (0)⟩, . . . , | eP (ℓ)⟩form an orthonormal set provided ℓ< d⊥/2, and so do |P (0)⟩, . . . , |P (ℓ)⟩. In this
case, the DQI state |P(f)⟩= P
x∈Fn
2 P(f(x)) |x⟩can be expressed as

ℓ
X

|P(f)⟩=

where

s

2n
m
k

wk = uk

and ⟨P(f)|P(f)⟩= ∥w∥2 where w := (w0, . . . , wℓ)T .

19

k=0
wk |P (k)⟩,
(27)


,
(28)

## Page 20

8.1.2
DQI Algorithm for max-XORSAT

With these facts in hand, we now present the DQI algorithm for max-XORSAT. The algorithm
utilizes three quantum registers: a weight register comprising ⌈log2 ℓ⌉qubits, an error register with
m qubits, and a syndrome register with n qubits.
As the first step in DQI we initialize the weight register in the state

ℓ
X

k=0
wk |k⟩.
(29)

The choice of w ∈Rℓ+1 that maximizes the expected number of satisfied constraints can be obtained
by solving for the principal eigenvector of an (ℓ+ 1) × (ℓ+ 1) matrix, as described in §9. Given w,
this state preparation can be done efficiently because it is a state of only ⌈log2 ℓ⌉qubits. One way to
do this is to use the method from [63] that prepares an arbitrary superposition over ℓcomputational
basis states using eO(ℓ) quantum gates.
Next, conditioned on the value k in the weight register, we prepare the error register into the
uniform superposition over all bit strings of Hamming weight k

ℓ
X

k=0
wk |k⟩
1
qm
k

X

→

|y⟩.
(30)

y∈Fm
2
|y|=k

Efficient methods for preparing such superpositions using O(ℓm) quantum gates have been devised
due to applications in physics, where they are known as Dicke states [19,20]. Next, we uncompute
|k⟩which can be done easily since k is simply the Hamming weight of y.
After doing so and
discarding the weight register, we are left with the state

ℓ
X

k=0
wk
1
qm
k

X

→

|y⟩.
(31)

y∈Fm
2
|y|=k

Next, we apply the phases (−1)v·y by performing a Pauli-Zi on each qubit for which vi = 1, at the
cost of O(m) quantum gates

ℓ
X

k=0
wk
1
qm
k

X

→

|y|=k
(−1)v·y |y⟩.
(32)

Then, we reversibly compute BT y into the syndrome register by standard matrix-vector multipli-
cation over F2 at the cost O(mn) quantum gates

ℓ
X

k=0
wk
1
qm
k

X

→

|y|=k
(−1)v·y |y⟩|BT y⟩.
(33)

From this, to obtain | eP (k)⟩we need to use the content s = BT y of the syndrome register to
reversibly uncompute the content y of the error register, in superposition. This is the hardest part.
We next discuss how to compute y from s.

20

## Page 21

Recall that B ∈Fm×n
2
with m > n. Thus, given s, solving s = BT y, for y is an underdetermined
linear algebra problem over F2. It is only the constraint |y| ≤ℓthat renders the solution unique,
provided ℓis not too large. This linear algebra problem with a Hamming weight constraint is
recognizable as syndrome decoding. The kernel of BT defines an error correcting code C⊥. The
string s is interpreted as the error syndrome, and y is interpreted as the error. If ℓis less than
half the minimum distance of C⊥then the problem of inferring the error from the syndrome has
a unique solution. When this solution can be found efficiently, we can efficiently uncompute the
content of the error register, which can then be discarded. This leaves

ℓ
X

k=0
wk
1
qm
k

X

→

in the syndrome register which we recognize as

ℓ
X

=

By taking the Hadamard transform we then obtain

ℓ
X

→

which is the desired DQI state |P(f)⟩.

8.2
DQI for General max-LINSAT

|y|=k
(−1)v·y |BT y⟩
(34)

k=0
wk | eP (k)⟩.
(35)

k=0
wk |P (k)⟩
(36)

8.2.1
DQI Quantum State for General max-LINSAT

Recall that the max-LINSAT objective takes the form f(x) = Pm
i=1 fi(bi · x) with fi : Fp →
{+1, −1}. In order to keep the presentation as simple as possible, we restrict attention to the
situation where the preimages Fi := f−1
i
(+1) for i = 1, . . . , m have the same cardinality r := |Fi| ∈
{1, . . . , p −1}. We will find it convenient to work in terms of gi which we define as fi shifted and
rescaled so that its Fourier transform

˜gi(y) =
1
√p

X

x∈Fp
ωyx
p gi(x)
(37)

vanishes at y = 0 and is normalized, i.e. P
x∈Fp |gi(x)|2 = P
y∈Fp |˜gi(y)|2 = 1. (Here and through-
out, ωp = ei2π/p.) In other words, rather than using fi directly, we will use

gi(x) := fi(x) −f

φ
(38)

p
P
x∈Fp fi(x) and φ :=
P
y∈Fp |fi(y) −f|21/2
. Explicitly, one finds

where f := 1

¯f
=
2r

s

φ
=

21

p −1
(39)

4r

1 −r


.
(40)

p

## Page 22

By (38), the sums

f(x)
=
f1(b1 · x) + . . . + fm(bm · x)
(41)

g(x)
=
g1(b1 · x) + . . . + gm(bm · x)
(42)

are related according to
f(x) = g(x)φ + mf.
(43)

We transform the polynomial P(f(x)) into an equivalent polynomial Q(g(x)) of the same degree
by substituting in this relation and absorbing the relevant powers of φ and mf into the coefficients.
That is, Q(g(x)) = P(f(x)). As shown in Appendix A, Q(g(x)) can always be expressed as a linear
combination of elementary symmetric polynomials. That is,

ℓ
X

k=0
ukP (k)(g1(b1 · x), . . . , gm(bm · x)).
(44)

Q(g(x)) :=

As in the case of DQI for max-XORSAT above, we write the DQI state

|P(f)⟩=
X

x∈Fnp
P(f(x)) |x⟩=
X

as a linear combination of |P (0)⟩, . . . , |P (ℓ)⟩defined as

|P (k)⟩:=
1
q

pn−km
k

X

x∈Fnp
Q(g(x)) |x⟩= |Q(g)⟩
(45)

x∈Fnp
P (k)(g1(b1 · x), . . . , gm(bm · x)) |x⟩.
(46)

By definition,
P (k)(g1(b1 · x), . . . , gm(bm · x)) =
X

Substituting (37) into (47) yields

P (k)(g1(b1 · x), . . . , gm(bm · x))
=
X

i1,...,ik
distinct

1
p

=
X

y∈Fm
p
|y|=k

Y

i∈{i1,...,ik}
gi(bi · x).
(47)

i1,...,ik
distinct





1
√p

Y

X

yi∈Fp
ω−yibi·x
p
˜gi(yi)


(48)

i∈{i1,...,ik}

m
Y

pk ω−(BT y)·x
p

˜gi(yi).
(49)

i=1
yi̸=0

From this we see that the Quantum Fourier Transform of |P (k)⟩is

| eP (k)⟩:= F ⊗n|P (k)⟩=
1
qm
k

X

y∈Fm
p
|y|=k

22





m
Y


|BT y⟩
(50)

˜gi(yi)




i=1
yi̸=0

## Page 23

where Fij = ωij
p /√p with i, j = 0, . . . , p −1. As in the case of max-XORSAT earlier, if |y| < d⊥/2,
then BT y are all distinct. Therefore, if ℓ< d⊥/2 then | eP (0)⟩, . . . , | eP (ℓ)⟩form an orthonormal set
and so do |P (0)⟩, . . . , |P (ℓ)⟩. Thus, the DQI state |P(f)⟩= P
x∈Fnp P(f(x)) |x⟩can be expressed as

ℓ
X

|P(f)⟩=

where

s

wk = uk

and ⟨P(f)|P(f)⟩= ∥w∥2.

8.2.2
DQI Algorithm for General max-LINSAT

k=0
wk |P (k)⟩
(51)

pn−k
m
k


,
(52)

DQI for general max-LINSAT employs three quantum registers:
a weight register comprising
⌈log2 ℓ⌉qubits, an error register with m⌈log2 p⌉qubits, and a syndrome register with n⌈log2 p⌉
qubits. We will consider the error and syndrome registers as consisting of m and n subregisters,
respectively, where each subregister consists of ⌈log2 p⌉qubits2. We will also regard the ordered
collection of least significant3 qubits from the m subregisters of the error register as the fourth
register. We will refer to this m qubit register as the mask register.
The task of DQI is to produce the state |Q(g)⟩, which by construction is equal to |P(f)⟩. We
proceed as follows. First, as in the p = 2 case, we initialize the weight register in the normalized
state
ℓ
X

k=0
wk |k⟩.
(53)

Next, conditioned on the value k in the weight register, we prepare the mask register in the corre-
sponding Dicke state

ℓ
X

k=0
wk |k⟩
1
qm
k

X

→

|µ⟩.
(54)

µ∈{0,1}m
|µ|=k

Then, we uncompute |k⟩using the fact that k = |µ|, which yields

ℓ
X

k=0
wk
1
qm
k

X

→

|µ⟩.
(55)

µ∈{0,1}m
|µ|=k

Subsequently, we will turn the content of the error register from a superposition of bit strings
µ ∈{0, 1}m of Hamming weight k into a superposition of symbol strings y ∈Fm
p of Hamming
weight k. Let Gi denote an operator acting on ⌈log2 p⌉qubits such that

Gi |0⟩= |0⟩,
Gi |1⟩=
X

y∈Fp
˜gi(y) |y⟩.
(56)

2One can also regard each subregister as a logical p-level quantum system, i.e. a qudit, encoded in ⌈log2 p⌉qubits.
3Least significant qubit is the one which is in the state |1⟩when the subregister stores the value 1 ∈Fp.

23

## Page 24

By reparametrizing from f1, . . . , fm to g1, . . . , gm we ensured that ˜gi(0) = 0 for all i, so

Gi |1⟩=
X

y∈F∗p
˜gi(y) |y⟩
(57)

where F∗
p = Fp \ {0}. This guarantees that Gi |0⟩= |0⟩is orthogonal to Gi |1⟩, so we may assume
that Gi is unitary. It may be realized, e.g. using the techniques from [63]. The fact that ˜gi(0) = 0
also implies that the parallel application G := Qm
i=1 Gi of each Gi to the respective subregister of
the error register preserves the Hamming weight. More precisely, the symbol string on every term
in the expansion of G |µ⟩in the computational basis has the same Hamming weight as µ. Indeed,
using (56) and (57), we find
X

G |µ⟩=
X

y∈Fm
p
|y|=k

µ∈{0,1}m
|µ|=k

˜gy(1)
yy(1)

. . . ˜gy(k)
yy(k)

|y⟩
(58)

where yi denotes the ith entry of y, and y(j) denotes the index of the jth nonzero entry of y. Thus,
by applying G to the error register, we obtain

ℓ
X

k=0
wk
1
qm
k

X

→

y∈Fm
p
|y|=k

˜gy(1)
yy(1)

. . . ˜gy(k)
yy(k)

|y⟩.
(59)

Next, we reversibly compute BT y into the syndrome register, obtaining the state

ℓ
X

k=0
wk
1
qm
k

X

˜gy(1)
yy(1)

. . . ˜gy(k)
yy(k)

|y⟩|BT y⟩.
(60)

→

y∈Fm
p
|y|=k

The task of finding y from BT y is the bounded distance decoding problem on C⊥= {y ∈Fm
p :
BT y = 0}. Thus uncomputing the content of the error register can be done efficiently whenever
the bounded distance decoding problem on C⊥can be solved efficiently out to distance ℓ.
Uncomputing disentangles the syndrome register from the error register leaving it in the state

ℓ
X

k=0
wk
1
qm
k

X

→

y∈Fm
p
|y|=k



ℓ
X

m
Y

k=0
wk
1
qm
k

X

=




y∈Fm
p
|y|=k

i=1
yi̸=0

Comparing (62) with (50) shows that this is equal to

ℓ
X

=

24

˜gy(1)
yy(1)

. . . ˜gy(k)
yy(k)

|BT y⟩
(61)




|BT y⟩.
(62)

˜gi(yi)

k=0
wk | eP (k)⟩.
(63)

## Page 25

Figure 5: Here we plot the expected fraction ⟨s⟩/m of satisfied constraints, as dictated by Lemma
9.2, upon measuring |P(f)⟩when P is the optimal degree-ℓpolynomial. We show the balanced case
where |f−1
i
(+1)| ≃p/2 for all i. Accordingly, the dashed black line corresponds to the asymptotic
formula (9) with r/p = 1/2.

Thus, by applying the inverse Quantum Fourier Transform on Fn
p to the syndrome register we
obtain

ℓ
X

→

k=0
wk |P (k)⟩.
(64)

By the definition of wk this is |Q(g)⟩, which equals |P(f)⟩.

9
Optimal Expected Fraction of Satisfied Constraints

In this section we prove Theorem 4.1 for the asymptotic performance of DQI as well as quantify
the finite-size corrections. Before doing so, we make two remarks. First, we note that the condition
2ℓ+ 1 < d⊥is equivalent to saying that ℓmust be less than half the distance of the code, which
is the same condition needed to guarantee that the decoding problem used in the uncomputation
step of DQI has a unique solution. This condition is met by our OPI example. It is not met in
our irregular max-XORSAT example. In §10 we show that the semicircle law (9) remains a good
approximation even beyond this limit, for average case v. Second, we note that Lemma 9.2 gives
an exact expression for the expected number of constraints satisfied by DQI at any finite size and
for any choice of polynomial P, in terms of an (ℓ+ 1) × (ℓ+ 1) quadratic form. By numerically
evaluating optimum of this quadratic form we find that the finite size behavior converges fairly
rapidly to the asymptotic behavior of Theorem 4.1, as illustrated in Fig. 5.

25

## Page 26

9.1
Preliminaries

Recall from §8.2.1 that the quantum state | eP(f)⟩= F ⊗n|P(f)⟩obtained by applying the Quantum
Fourier Transform to a DQI state |P(f)⟩= P
x∈Fnp P(f(x))|x⟩is



ℓ
X

wk
qm
k

X

| eP(f)⟩=




y∈Fm
p
|y|=k

k=0

This can be written more succinctly as

ℓ
X

wk
qm
k

X

| eP(f)⟩=

y∈Fm
p
|y|=k

k=0

by defining for any y ∈Fm
p

m
Y

˜g(y) =

i=1
yi̸=0



m
Y


|BT y⟩
(65)

˜gi(yi)

i=1
yi̸=0

˜g(y) |BT y⟩
(66)

˜gi(yi)
(67)

where we regard the product of zero factors as 1, so that ˜gi(0) = 1. Next, we note that



|˜g(y)|2 =
X

X

X

y1∈Fp
|˜gi1(y1)|2

y∈Fm
p
|y|=k

i1,...,ik∈{1,...,m}
distinct







=
m
k


(68)

X

yk∈Fp
|˜gik(yk)|2

. . .

where we used the fact that ˜gi(0) = 0 for all i. Lastly, we formally restate the following fact, which
we derived in §8.2.1.

Lemma 9.1. Let d⊥denote the minimum distance of the code C⊥= {d ∈Fm
p : BT d = 0}. If
2ℓ< d⊥, then ⟨eP(f)| eP(f)⟩= ∥w∥2.

The proof of Theorem 4.1 consists of two parts. In the next subsection, we express the expected
fraction ⟨s(m,ℓ)⟩/m of satisfied constraints as a quadratic form involving a certain tridiagonal matrix.
Then, we derive a closed-form asymptotic formula for the maximum eigenvalue of the matrix. We
end this section by combining the two parts into a proof of Theorem 4.1.
We note that [64]
encountered a similar matrix in the context of proving bounds on the size of codes with good
distance, and derived a similar expression for the maximum eigenvalue, using similar methods.

9.2
Expected Number of Satisfied Constraints

Lemma 9.2. Let f(x) = Pm
i=1 fi
Pn
j=1 Bijxj

be a max-LINSAT objective function with matrix

B ∈Fm×n
p
for a prime p and positive integers m and n such that m > n. Suppose that |f−1
i
(+1)| = r
for some r ∈{1, . . . , p −1}. Let P be a degree-ℓpolynomial normalized so that ⟨P(f)|P(f)⟩= 1

with P(f) = Pℓ
k=0 wkP (k)(f1, . . . , fm)/
q

26

pn−km
k

its decomposition as a linear combination of

## Page 27

elementary symmetric polynomials. Let ⟨s(m,ℓ)⟩be the expected number of satisfied constraints for
the symbol string obtained upon measuring the DQI state |P(f)⟩in the computational basis. If
2ℓ+ 1 < d⊥where d⊥is the minimum distance of the code C⊥= {d ∈Fm
p : BT d = 0}, then

p

r(p −r)

⟨s(m,ℓ)⟩= mr

p +

p
w†A(m,ℓ,d)w
(69)

where w = (w0, . . . , wℓ)T and A(m,ℓ,d) is the (ℓ+ 1) × (ℓ+ 1) symmetric tridiagonal matrix



0
a1
a1
d
a2



A(m,ℓ,d) =

k(m −k + 1) and d =
p−2r
√

with ak =
p

r(p−r).

Proof. The number of constraints satisfied by x ∈Fn
p is

m
X

s(x) =

where

1A(x) =





a2
2d
...
...
aℓ
aℓ
ℓd

(70)

i=1
1Fi(bi · x)
(71)

(
1
if
x ∈A
0
otherwise
(72)

is the indicator function of the set A. For any v, x ∈Fp, we can write

1{v}(x) = 1

X

p

so

v∈Fi
1{v}(x) = 1

1Fi(x) =
X

p

Substituting into (71), we have

m
X

s(x) = 1

X

X

p

v∈Fi

i=1

a∈Fp
ωa(x−v)
p
(73)

X

X

a∈Fp
ωa(x−v)
p
.
(74)

v∈Fi

a∈Fp
ωa(bi·x−v)
p
.
(75)

The expected number of constraints satisfied by a symbol string sampled from the output distri-
bution of a DQI state |P(f)⟩is

⟨s(m,ℓ)⟩= ⟨P(f)|Sf|P(f)⟩
(76)

27

## Page 28

where Sf = P
x∈Fnp s(x)|x⟩⟨x|. We can express the observable Sf in terms of the clock operator

Z = P
b∈Fp ωb
p|b⟩⟨b| on Cp as

Sf =
X

x∈Fnp
s(x)|x⟩⟨x|
(77)

m
X

= 1

X

X

X

p

a∈Fp

v∈Fi

i=1

m
X

n
Y

= 1

X

X

a∈Fp
ω−av
p

p

v∈Fi

i=1

j=1

m
X

n
Y

= 1

X

X

a∈Fp
ω−av
p

p

v∈Fi

i=1

x∈Fnp
ωa(bi·x−v)
p
|x⟩⟨x|
(78)

xj∈Fp
ωaBijxj
p
|xj⟩⟨xj|
(79)

X

j=1
ZaBij.
(80)

Next, we apply the Fourier transform Fij = ωij
p /√p with i, j = 0, . . . , p−1 to write ⟨s(m,ℓ)⟩in terms
of the shift operator X = P
b∈Fp |b + 1⟩⟨b| on Cp as

m
X

⟨s(m,ℓ)⟩= 1

X

X

p

v∈Fi

i=1

m
X

= 1

X

X

p

v∈Fi

i=1

where we used FZF † = X−1 and | eP(f)⟩= F ⊗n|P(f)⟩.
Substituting (66) into (82), we get

ℓ
X

m
X

w∗
k1wk2
qm
k1
m
k2

X

⟨s(m,ℓ)⟩= 1

˜g∗(y1)˜g(y2)

p

y1,y2∈Fm
p
|y1|=k1
|y2|=k2

i=1

k1,k2=0

n
Y

j=1
ZaBij
j
|P(f)⟩
(81)

a∈Fp
ω−av
p
⟨P(f)|

n
Y

j=1
X−aBij
j
| eP(f)⟩.
(82)

a∈Fp
ω−av
p
⟨eP(f)|

n
Y

a∈Fp
ω−av
p
⟨BT y1|

j=1
X−aBij
j
|BT y2⟩

X

X

v∈Fi

(83)

Let e1, . . . , em ∈Fm
p denote the standard basis of one-hot vectors. Then

n
Y

j=1
X−aBij
j
|BT y2⟩= |BT y2 −abT
i ⟩= |BT (y2 −aei)⟩
(84)

so

ℓ
X

m
X

w∗
k1wk2
qm
k1
m
k2

X

⟨s(m,ℓ)⟩= 1

˜g∗(y1)˜g(y2)

p

y1,y2∈Fm
p
|y1|=k1
|y2|=k2

i=1

k1,k2=0

a∈Fp
ω−av
p
⟨BT y1|BT (y2 −aei)⟩.
(85)

X

X

v∈Fi

But |BT y1⟩and |BT (y2 −aei)⟩are computational basis states, so

⟨BT y1|BT (y2 −aei)⟩=

28

(
1
if
BT y1 = BT (y2 −aei)
0
otherwise.
(86)

## Page 29

Moreover,

BT y1 = BT (y2 −aei) ⇐⇒y1 −y2 + aei ∈C⊥⇐⇒y1 = y2 −aei
(87)

where we used the assumption that the smallest Hamming weight of a non-zero symbol string in
C⊥is d⊥> 2ℓ+ 1 ≥k1 + k2 + 1.
There are three possibilities to consider: |y1| = |y2| −1, |y2| = |y1| −1, and |y1| = |y2|. We
further break up the last case into y1 ̸= y2 and y1 = y2. Before simplifying (85), we examine the
values of i ∈{1, . . . , m} and a ∈Fp for which ⟨BT y1|BT (y2 −aei)⟩= 1 in each of the four cases.
We also compute the value of the product ˜g∗(y1)˜g(y2).
Consider first the case |y1| = |y2| −1. Here, a ̸= 0 and i ∈{1, . . . , m} is the position which is
zero in y := y1 and a in y2. Therefore, by definition (67)

˜g∗(y1)˜g(y2) = |˜g(y)|2˜gi(a).
(88)

Next, suppose |y2| = |y1| −1. Then a ̸= 0 and i ∈{1, . . . , m} is the position which is zero in
y := y2 and −a in y1. Thus,

˜g∗(y1)˜g(y2) = |˜g(y2)|2˜g∗
i (−a) = |˜g(y)|2˜gi(a).
(89)

Consider next the case |y1| = |y2| and y1 ̸= y2. Here, a ̸= 0 and i ∈{1, . . . , m} is the position
which is z −a in y1 and z in y2 for some z ∈Fp \ {0, a}. Let y ∈Fm
p denote the vector which is
zero at position i and agrees with y1, and hence with y2, on all other positions. Then

˜g∗(y1)˜g(y2) = |˜g(y)|2˜g∗
i (z −a)˜gi(z) = |˜g(y)|2˜gi(a −z)˜gi(z).
(90)

Finally, when y := y1 = y2, we have

˜g∗(y1)˜g(y2) = |˜g(y)|2.
(91)

In this case, a = 0 and i ∈{1, . . . , m}.
Putting it all together we can rewrite (85) as

ℓ−1
X

|˜g(y)|2
m
X

w∗
kwk+1
qm
k
 m
k+1

X

⟨s(m,ℓ)⟩= 1

p

y∈Fm
p
|y|=k

i=1
yi=0

k=0

ℓ−1
X

|˜g(y)|2
m
X

w∗
k+1wk
q m
k+1
m
k

X

+ 1

p

y∈Fm
p
|y|=k

i=1
yi=0

k=0

ℓ
X

|˜g(y)|2
m
X

|wk|2

+ 1

m
k

X

X

p

y∈Fm
p
|y|=k−1

v∈Fi

i=1
yi=0

k=1

ℓ
X

|˜g(y)|2
m
X

|wk|2

+ 1

m
k

X

X

X

p

y∈Fm
p
|y|=k

v∈Fi

i=1

k=0

29

X

X

a∈F∗p
ω−av
p
˜gi(a)
(92)

v∈Fi

X

X

a∈F∗p
ω−av
p
˜gi(a)
(93)

v∈Fi

X

X

z∈Fp\{0,a}
ω−av
p
˜gi(a −z)˜gi(z)
(94)

a∈F∗p

a∈{0}
ω−av
p
.
(95)

## Page 30

Remembering that ˜gi(0) = 0, we recognize the innermost sums in (92) and (93) as the inverse
Fourier transform so, for y with |y| = k, we have

m
X

m
X

a∈F∗p
ω−av
p
˜gi(a) = √p

X

X

X

v∈Fi

i=1
yi=0

i=1
yi=0

where we used (39) and (40) to calculate

gi(v) = 1 −¯f

v∈Fi
gi(v) = (m −k)
p

r(p −r)
(96)

φ
=
rp −r

pr
(97)

for v ∈Fi. Similarly, with ˜gi(0) = 0, we recognize the sums indexed by a and z in (94) as the
inverse Fourier transform of the convolution of ˜gi with itself, so

z∈Fp
˜gi(a −z)˜gi(z) = 1

a∈Fp
ω−av
p
X

X

X

p

=
X

=
X

x∈Fp
gi(x)2 X

and, for y with |y| = k −1, we have



m
X

m
X

X

X

X

X

z∈Fp\{0,a}
ω−av
p
˜gi(a −z)˜gi(z) =

a∈F∗p

v∈Fi

v∈Fi

i=1
yi=0

i=1
yi=0

m
X

X

=

v∈Fi

i=1
yi=0

m
X

X

=

v∈Fi

i=1
yi=0

30

a∈Fp
ω−av
p
X

x∈Fp
ωx(a−z)
p
gi(x)
X

X

y∈Fp
ωyz
p gi(y)
(98)

z∈Fp

a,x,y∈Fp
ωa(x−v)
p
gi(x)gi(y)1

X

z∈Fp
ω(y−x)z
p
(99)

p

a∈Fp
ωa(x−v)
p
= p gi(v)2
(100)



X

a,z∈Fp
ω−av
p
˜gi(a −z)˜gi(z) −
X

z∈Fp
|˜gi(z)|2



p gi(v)2 −1

(101)

p −r

r
−1

(102)

= (m −k + 1)(p −2r)
(103)

## Page 31

where we used (97). Substituting back into (92), (93), and (94), we obtain

ℓ−1
X

p

r(p −r)

⟨s(m,ℓ)⟩=

p

ℓ−1
X

p

r(p −r)

+

p

ℓ
X

+ p −2r

k=0
w∗
kwk+1
m −k
qm
k
 m
k+1

X

|˜g(y)|2
(104)

y∈Fm
p
|y|=k

k=0
w∗
k+1wk
m −k
q m
k+1
m
k

X

|˜g(y)|2
(105)

y∈Fm
p
|y|=k

k=1
|wk|2 m −k + 1
m
k

X

p

ℓ
X

+ mr

k=0
|wk|2 1
m
k

X

p

y∈Fm
p
|y|=k

and using equation (68), we get

ℓ−1
X

p

r(p −r)

⟨s(m,ℓ)⟩=

p

ℓ−1
X

p

r(p −r)

+

p

ℓ
X

+ p −2r

|˜g(y)|2
(106)

y∈Fm
p
|y|=k−1

|˜g(y)|2
(107)

k=0
w∗
kwk+1
p

(k + 1)(m −k)
(108)

k=0
w∗
k+1wk
p

(k + 1)(m −k)
(109)

k=0
|wk|2k + mr

p

Defining



0
a1
a1
d
a2



A(m,ℓ,d) =

where ak =
p

p .
(110)





a2
2d
...
...
aℓ
aℓ
ℓd

(111)

k(m −k + 1) for k = 1, . . . , ℓand d ∈R, we can write

p

r(p −r)

⟨s(m,ℓ)⟩= mr

p +

where w = (w0, . . . , wℓ)T and d =
p−2r
√

r(p−r).

31

p
w†A(m,ℓ,d)w
(112)

## Page 32

9.3
Asymptotic Formula for Maximum Eigenvalue of Matrix A(m,ℓ,d)/m

Lemma 9.3. Let λ(m,ℓ,d)
max
denote the maximum eigenvalue of the symmetric tridiagonal matrix
A(m,ℓ,d) defined in (111). If ℓ≤m/2 and d ≥−
m−2ℓ
√

λ(m,ℓ,d)
max

ℓ(m−ℓ), then

m
= µd + 2
p

lim
m,ℓ→∞
ℓ/m=µ

µ(1 −µ)
(113)

where the limit is taken as both m and ℓtend to infinity with the ratio µ = ℓ/m fixed.

Proof. First, we show that if ℓ≤m/2, then

λ(m,ℓ,d)
max

m
≥µd + 2
p

lim
m,ℓ→∞
ℓ/m=µ

Define vector v(m,ℓ) ∈Rℓ+1 as

µ(1 −µ).
(114)

(
0
for
i = 0, 1, . . . , ℓ−⌈
√

ℓ⌉
⌈
√

v(m,ℓ)
i
=

ℓ⌉−1/2
for
i = ℓ−⌈
√

Then, ∥v(m,ℓ)∥2
2 = ⌈
√

ℓ⌉
⌈
√

ℓ⌉= 1. But

v(m,ℓ)T A(m,ℓ,d)v(m,ℓ)

λ(m,ℓ,d)
max

m
≥
lim
m,ℓ→∞
ℓ/m=µ

lim
m,ℓ→∞
ℓ/m=µ

ℓ⌉+ 1, . . . , ℓ.
(115)

m
(116)





ℓ
X


1
m⌈
√

=
lim
m,ℓ→∞
ℓ/m=µ

ℓ⌉+1
kd

ℓ⌉

k=ℓ−⌈
√

The second term in (117) is bounded below by





ℓ
X


1
m⌈
√

≥
lim
m,ℓ→∞
ℓ/m=µ

lim
m,ℓ→∞
ℓ/m=µ

ℓ⌉+2
2ak

ℓ⌉

k=ℓ−⌈
√

2
q



=
lim
m,ℓ→∞
ℓ/m=µ

= 2
p





ℓ
X


1
m⌈
√

+
lim
m,ℓ→∞
ℓ/m=µ

ℓ⌉+2
2ak

.
(117)

ℓ⌉

k=ℓ−⌈
√

!

m⌈
√

(118)

ℓ⌉

(ℓ−⌈
√

ℓ⌉+ 2)(m −ℓ+ ⌈
√

m
· ⌈
√



ℓ⌉−1)

ℓ⌉−1
⌈
√



ℓ⌉

µ(1 −µ)
(119)

where we used the fact that ak increases as a function of k for k ≤m/2. If d ≥0, then the first
term in (117) is bounded below by





ℓ
X


1
m⌈
√

≥
lim
m,ℓ→∞
ℓ/m=µ

lim
m,ℓ→∞
ℓ/m=µ

ℓ⌉+1
kd

ℓ⌉

k=ℓ−⌈
√

32

⌈
√

ℓ⌉· (ℓ−⌈
√

ℓ⌉+ 1) · d
m⌈
√

ℓ⌉
= µd
(120)

## Page 33

and if d < 0, then it is bounded below by





ℓ
X


1
m⌈
√

lim
m,ℓ→∞
ℓ/m=µ

ℓ⌉+1
kd

ℓ⌉

k=ℓ−⌈
√

Putting it all together, we get

λ(m,ℓ,d)
max

⌈
√

ℓ⌉· ℓ· d
m⌈
√

≥
lim
m,ℓ→∞
ℓ/m=µ

ℓ⌉
= µd.
(121)

m
≥µd + 2
p

lim
m,ℓ→∞
ℓ/m=µ

µ(1 −µ).
(122)

Next, we establish a matching upper bound on λ(m,ℓ,d)
max
. For k = 0, 1, . . . , ℓ, let R(m,ℓ,d)
k
denote
the sum of the off-diagonal entries in the kth row of A(m,ℓ,d) and set a0 = aℓ+1 = 0, so that
Rk = ak + ak+1. By Gershgorin’s circle theorem, for every eigenvalue λ(m,ℓ,d) of A(m,ℓ,d), we have

λ(m,ℓ,d) ≤
max
k∈{0,...,ℓ}(kd + Rk)
(123)


kd +
p

=
max
k∈{0,...,ℓ}

By assumption, ℓ< m/2, so
p

(k + 1)(m −k) ≥
p

(k + 1)(m −k)

.
(124)

k(m −k + 1) +
p

k(m −k + 1) for all k in the sum. Thus (124)
yields

λ(m,ℓ,d) ≤
max
k∈{0,...,ℓ}


kd + 2
p


kd + 2
p

≤
max
k∈{0,...,ℓ}

≤2√m +
max
k∈{0,...,ℓ}

(k + 1)(m −k)

(125)

k(m −k) + 2
√

m −k

(126)


kd + 2
p

k(m −k)

(127)

= 2√m +
max
k∈{0,...,ℓ} ξ(k)
(128)

x(m −x). Note that ξ
′′(x) = −
m2
2[x(m−x)]3/2 < 0 for all x ∈(0, m),

where we define ξ(x) = xd + 2
p

so the derivative ξ
′(x) = d +
m−2x
√

x(m−x) is decreasing in this interval.
However, by assumption

ℓ(m−ℓ), so ξ
′(x) ≥ξ
′(ℓ) ≥0 for x ∈(0, ℓ], since ℓ< m/2. Therefore, ξ(x) is increasing on

d ≥−
m−2ℓ
√

this interval and we have

λ(m,ℓ,d) ≤2√m + ℓd + 2
p

But then

2√m + ℓd + 2
p

λ(m,ℓ,d)
max

m
≤
lim
m,ℓ→∞
ℓ/m=µ

lim
m,ℓ→∞
ℓ/m=µ

ℓ(m −ℓ).
(129)

ℓ(m −ℓ)
m
= µd + 2
p

µ(1 −µ)
(130)

which establishes the matching upper bound and completes the proof of the lemma.

33

## Page 34

9.4
Optimal Asymptotic Expected Fraction of Satisfied Constraints

In this subsection we use Lemmas 9.2 and 9.3 to prove Theorem 4.1.

Proof. Recall from Lemma 9.1 that ∥w∥2 = 1. Therefore, the expected number of satisfied con-
straints is maximized by choosing w in (69) to be the normalized eigenvector of A(m,ℓ,d) corre-
sponding to its maximal eigenvalue. This leads to

⟨s(m,ℓ)⟩opt

m
= ρ +
p

p and d =
p−2r
√

where ρ = r

ρ(1 −ρ)λ(m,ℓ,d)
max

m
(131)

m. Then p−r

r(p−r). Consider first the case of r

r

r

d =
p −2r
p

p −r

r
−
r
r
p −r ≥

r(p −r)
=

p ≤1 −ℓ

r
≥
ℓ
m−ℓand

r

m −ℓ

ℓ
= −
m −2ℓ
p

ℓ
m −ℓ−

ℓ(m −ℓ)
.
(132)

Moreover, ℓ< (d⊥−1)/2 ≤(m −1)/2. Therefore, Lemma 9.3 applies and we have

⟨s(m,ℓ)⟩opt

m
= ρ +
p

lim
m,ℓ→∞
ℓ/m=µ

= ρ +
p

Recalling d =
1−2ρ
√

ρ(1−ρ) this yields

⟨s(m,ℓ)⟩opt

λ(m,ℓ,d)
max

ρ(1 −ρ)
lim
m,ℓ→∞
ℓ/m=µ

m
.
(133)

ρ(1 −ρ)

µd + 2
p

µ(1 −µ)

(134)

(135)

m
= µ + ρ −2µρ + 2
p

lim
m,ℓ→∞
ℓ/m=µ

=
p

µ(1 −µ)ρ(1 −ρ)
(136)

ρ(1 −µ)
2
(137)

µ(1 −ρ) +
p

ρ(1 −µ)
2
= 1. But ⟨s(m,ℓ)⟩opt is
an increasing function of r that cannot exceed 1. Consequently,

for ρ ≤1 −µ. In particular, if ρ = 1 −µ, then
p

⟨s(m,ℓ)⟩opt

lim
m,ℓ→∞
ℓ/m=µ

for ρ > 1 −µ. Putting it all together, we obtain




p

⟨s(m,ℓ)⟩opt

µ(1 −ρ) +
p

lim
m,ℓ→∞
ℓ/m=µ

m
=

µ(1 −ρ) +
p

m
= 1
(138)

ρ(1 −µ)
2
if ρ ≤1 −µ

1
otherwise
(139)



which completes the proof of Theorem 4.1.

34

## Page 35

10
Removing the Minimum Distance Assumption

So far, in our description and analysis of DQI we have always assumed that 2ℓ+ 1 < d⊥. This
condition buys us several advantages. First, it ensures that the states | eP (0)⟩, . . . , | eP (ℓ)⟩, from which
we construct

ℓ
X

k=0
wk
1
qm
k

X

| eP(f)⟩=

y∈Fm
2
|y|=k

form an orthonormal set which implies that

(−1)v·y |BT y⟩,
(140)

⟨eP(f)| eP(f)⟩= w†w.
(141)

Second, it allows us to obtain an exact expression for the expected number of constraints satisfied
without needing to know the weight distributions of either the code C or C⊥, namely for p = 2

⟨s⟩= 1

2m + 1

2w†A(m,ℓ,0)w
(142)

where A(m,ℓ,d) is the (ℓ+ 1) × (ℓ+ 1) matrix defined in (70). These facts in turn allow us to prove
Theorem 4.1.
For the irregular LDPC code described in §12, we can estimate d⊥using the Gilbert-Varshamov
bound4. By experimentally testing belief propagation, we find that for some codes it is able to
correct slightly more than (d⊥−1)/2 errors with high reliability. Under this circumstance, equations
(141) and (142) no longer hold exactly. Here, we prove that they continue to hold in expectation
for max-XORSAT with uniformly average v, up to small corrections due to decoding failures. The
precise statement of our result is given in Theorem 10.1.
In the remainder of this section we first describe precisely what we mean by the DQI algorithm
in the case of 2ℓ+ 1 ≥d⊥. (For simplicity, we consider the case p = 2.)
As the initial step of DQI, we perform classical preprocessing to choose w ∈Rℓ+1, which is
equivalent to making a choice of degree-ℓpolynomial P. In the case 2ℓ+ 1 < d⊥we can exactly
compute the choice of w that maximizes ⟨s⟩/m.
Specifically, it is the principal eigenvector of
A(m,ℓ,d) defined in (70). Once we reach or exceed 2ℓ+ 1 = d⊥the principal eigenvector of this
matrix is not necessarily the optimal choice. But we can still use it as our choice of w, and as we
will show below, it remains a good choice.
After choosing w, the next step in the DQI algorithm, as discussed in §8.1.2 is to prepare the
state
ℓ
X

k=0
wk
1
qm
k

X

y∈Fm
2
|y|=k

(−1)v·y |y⟩|BT y⟩.
(143)

The following step is to uncompute |y⟩. When 2ℓ+ 1 ≥d⊥this uncomputation will not succeed
with 100% certainty and one cannot produce exactly the state | eP(f)⟩= Pℓ
k=0 wk | eP (k)⟩. Instead,
the goal is to produce a good approximation to | eP(f)⟩with high probability. This is because the
number of errors ℓis large enough so that, by starting from a codeword in C⊥and then flipping

4By [35] it is known that the distance of random LDPC codes drawn from various standard ensembles is well-
approximated asymptotically by the Gilbert-Varshamov bound. We extrapolate that this is also a good approximation
for our ensemble of random LDPC codes with irregular degree distribution.

35

## Page 36

ℓbits, the nearest codeword (in Hamming distance) to the resulting string may be a codeword
other than the starting codeword. (This is the same reason that | eP (0)⟩, . . . , | eP (ℓ)⟩are no longer
orthogonal and hence the norm of | eP(f)⟩is no longer exactly equal to ∥w∥.)
If the decoder succeeds on a large fraction of the errors that are in superposition, one simply
postselects on success of the decoder and obtains a normalized state which is a good approximation
to the (unnormalized) ideal state | eP(f)⟩.
The last steps of DQI are to perform a Hadamard
transform and then measure in the computational basis, just as in the case of 2ℓ+ 1 < d⊥.

10.1
General Expressions for the Expected Number of Satisfied Constraints

Here we derive generalizations of lemmas 9.1 and 9.2 for arbitrary code distances. We restrict our
attention to the max-XORSAT case where we are given B ∈Fm×n
2
and v ∈Fm
2 and we seek to
maximize the objective function f(x) = Pm
i=1(−1)bi·x+vi, where bi is the ith row of B and vi is the
ith entry of v.
By examining (140) one sees that if d⊥> 2ℓthen the BT y are all distinct and the norm of
| eP(f)⟩is the norm of w, as shown in Lemma 9.1. More generally, we have the following lemma.

Lemma 10.1. The squared norm of | eP(f)⟩is

⟨eP(f)| eP(f)⟩= w†M(m,ℓ)w,
(144)

where M(m,ℓ) is the (ℓ+ 1) × (ℓ+ 1) symmetric matrix defined by

M(m,ℓ)
k,k′
=
1
qm
k
m
k′

X

X

y∈Fm
2
|y|=k

y′∈Fm
2
|y′|=k′

for 0 ≤k, k′ ≤ℓ.

(−1)(y+y′)·vδBT y,BT y′,
(145)

Proof. This is immediate from (140) and the fact that the |BT y⟩are computational basis states.

Note that if d⊥> 2ℓ, then M(m,ℓ)
k,k′
= δk,k′, in agreement with Lemma 9.1.

Lemma 10.2. Let |P(f)⟩be the Hadamard transform of the state | eP(f)⟩defined in (140). Let ⟨f⟩
be the expected objective value for the symbol string obtained upon measuring the DQI state |P(f)⟩
in the computational basis. If the weights wk are such that |P(f)⟩is normalized, then

⟨f⟩= w† ¯A(m,ℓ)w
(146)

where ¯A(m,ℓ) is the (ℓ+ 1) × (ℓ+ 1) symmetric matrix defined by

m
X

¯A(m,ℓ)
k,k′
=
1
qm
k
m
k′


X

i=1

for 0 ≤k, k′ ≤ℓ, and

(−1)vi+v·(y+y′)
(147)

(y,y′)∈S(i)
k,k′

S(i)
k,k′ = {(y, y′) ∈Fm
2 × Fm
2 : |y| = k, |y′| = k′, BT (y + y′ + ei) = 0}.
(148)

for one-hot vectors e1, . . . , em in Fm
2 .

36

## Page 37

Proof. The expected value of f(x) in state |P(f)⟩is

⟨f⟩= ⟨P(f)| Hf |P(f)⟩,
(149)

where

m
X

Hf =

i=1
(−1)vi
Y

j:Bij=1
Zj
(150)

and Zj denotes the Pauli Z operator acting on the jth qubit.
Recalling that conjugation by
Hadamard interchanges Pauli X with Z, we have

m
X

i=1
(−1)vi ⟨P(f)|
Y

⟨f⟩
=

j:Bij=1
Zj |P(f)⟩
(151)

m
X

i=1
(−1)vi ⟨eP(f)|
Y

j:Bij=1
Xj | eP(f)⟩
(152)

=

ℓ
X

|y′|=k′
(−1)v·(y+y′)
m
X

wkwk′
qm
k
m
k′

X

X

=

k,k′=0

|y|=k

i=1
(−1)vi ⟨BT y|
Y

j:Bij=1
Xj |BT y′⟩,
(153)

where in the last line we have plugged in the definition of | eP(f)⟩. We can rewrite this quadratic
form as

ℓ
X

⟨f⟩=

where

|y′|=k′
(−1)v·(y+y′)
m
X

¯A(m,ℓ)
k,k′
=
1
qm
k
m
k′

X

X

|y|=k

For the one-hot vectors e1, . . . , em ∈Fm
2 we have
Y

k,k′=0
wk wk′ ¯A(m,ℓ)
k,k′ ,
(154)

i=1
(−1)vi ⟨BT y|
Y

j:Bij=1
Xj |BT y′⟩.
(155)

j:Bij=1
Xj |BT y′⟩= |BT (y′ + ei)⟩.
(156)

Substituting this into (155) yields

|y′|=k′
(−1)v·(y+y′)
m
X

¯A(m,ℓ)
k,k′
=
1
qm
k
m
k′

X

X

|y|=k

i=1
(−1)vi⟨BT y|BT (y′ + ei)⟩.
(157)

We next note that ⟨BT y|BT (y′ + ei)⟩equals one when BT y = BT (y′ + ei) and zero otherwise.
The condition BT y = BT (y′ + ei) is equivalent to BT (y + y′ + ei) = 0. Hence,

m
X

¯A(m,ℓ)
k,k′
=
1
qm
k
m
k′


X

i=1

(−1)vi+v·(y+y′)
(158)

(y,y′)∈S(i)
k,k′

where
S(i)
k,k′ = {(y, y′) ∈Fm
2 × Fm
2 : |y| = k, |y′| = k′, BT (y + y′ + ei) = 0}.
(159)

37

## Page 38

Note once again that if d⊥> 2ℓ+ 1 then ¯A(m,ℓ) simplifies to A(m,ℓ,0) defined in (70). It is also
easy to verify that ¯A(m,ℓ) can be rewritten in terms of M as

¯A(m,ℓ)
k,k′
=
p

k′(m −k′ + 1)M(m,ℓ)
k,k′−1 +
p

(k′ + 1)(m −k′)M(m,ℓ)
k,k′+1,
(160)

where we define M (m,ℓ)
k,k′
according to formula (145), even if k or k′ exceed ℓ+ 1.

10.2
Average-case v

Any choice of w ∈Cℓ+1 defines a corresponding state |P(f)⟩= H⊗n | eP(f)⟩via (140). (In general
this will not be normalized.)
As shown in the previous subsection the general expression for the expected value of f achieved
by measuring the ideal normalized DQI state |P(f)⟩/∥|P(f)⟩∥in the computational basis, which
holds even when 2ℓ+ 1 ≥d⊥, is

⟨f⟩= w† ¯A(m,ℓ)w

w†M(m,ℓ)w.
(161)

In the case 2ℓ+ 1 ≥d⊥it is impossible to precisely obtain the ideal DQI state. This is because
the number of errors ℓis large enough so that, by starting from a codeword in C⊥and then flipping
ℓbits, the nearest codeword (in Hamming distance) to the resulting string may be a codeword
other than the starting codeword. Therefore, in this section, we analyze ⟨f⟩in the presence of a
nonzero rate of decoding failures. Specifically, we consider the case that v is chosen uniformly at
random and calculate Ev⟨f⟩, as this averaging simplifies the analysis substantially, mainly due to
the following fact.

Lemma 10.3. Let ¯A(m,ℓ) be as defined in (147). Suppose v is chosen uniformly at random from
Fm
2 . Then Ev ¯A(m,ℓ) = A(m,ℓ,0), where A(m,ℓ,0) is as defined in (70).

Proof. Recall that

m
X

¯A(m,ℓ)
k,k′
=
1
qm
k
m
k′


X

i=1

for 0 ≤k, k′ ≤ℓ, and

(−1)vi+v·(y+y′)
(162)

(y,y′)∈S(i)
k,k′

S(i)
k,k′ = {(y, y′) ∈Fm
2 × Fm
2 : |y| = k, |y′| = k′, BT (y + y′ + ei) = 0}.
(163)

We can express S(i)
k,k′ as the union of two disjoint pieces

S(i)
k,k′
=
S(i,0)
k,k′ ∪S(i,1)
k,k′
(164)

S(i,0)
k,k′
=
{(y, y′) ∈S(i)
k,k′ : y + y′ + ei = 0}
(165)

S(i,1)
k,k′
=
{(y, y′) ∈S(i)
k,k′ : y + y′ + ei ̸= 0}.
(166)

We can then write ¯A(m,ℓ) as the corresponding sum of two contributions

m
X

¯A(m,ℓ)
k,k′
=
1
qm
k
m
k′


X

i=1

m
X

+
1
qm
k
m
k′


X

i=1

38

(−1)v·(y+y′+ei)

(y,y′)∈S(i,0)
k,k′

(−1)v·(y+y′+ei).
(167)

(y,y′)∈S(i,1)
k,k′

## Page 39

We next average over v. By the definition of S(i,0)
k,k′ , all terms in the sum have y + y′ + ei = 0
and therefore the first term is independent of v. This renders the averaging over v trivial for the
first term. By the definition of S(i,1)
k,k′ , the second term contains exclusively contributions where
y + y′ + ei ̸= 0. By the identity
1
2m
P
v∈Fm
2 (−1)v·z = δz,0 we see that the second term makes zero
contribution to the average. Thus we obtain

m
X

Ev ¯A(m,ℓ)
k,k′
=
1
qm
k
m
k′


X

i=1

(−1)v·(y+y′+ei).
(168)

(y,y′)∈S(i,0)
k,k′

We next observe that S(i,0)
k,k′ contains the terms where y + y′ + ei = 0 which are exactly the

terms that contribute at 2ℓ+ 1 < d⊥, whereas S(i,1)
k,k′ contains the terms where y + y′ + ei ∈
C⊥\ {0} which, prior to averaging, are the new contribution arising when ℓexceeds this bound.
Consequently, Ev ¯A(m,ℓ)
k,k′
is exactly equal to A(m,ℓ,0)
k,k′
, as defined in (70). (One can also verify this by
direct calculation.) That is, we have obtained

Ev ¯A(m,ℓ)
k,k′
= A(m,ℓ,0)
k,k′
,
(169)

which completes the proof of the lemma.

10.3
Imperfect decoding

A deterministic decoder partitions the set of errors Fm
2 = D ∪F into the set D of errors y correctly
identified by the decoder based on the syndrome BT y and the set F of errors misidentified. The
Hamming shell Ek of radius k is analogously partitioned Ek = Dk ∪Fk. We will quantify decoder’s
failure rate using εk := |Fk|/
m
k

and ε := max0≤k≤ℓεk.
The quantum state of the error and syndrome registers after the error uncomputation step of
the DQI algorithm using an imperfect decoder is



ℓ
X

wk
qm
k




(−1)v·y|0⟩|BT y⟩+
X




X

y∈Dk
|y|=k

k=0

(−1)v·y|y ⊕y′⟩|BT y⟩




(170)

y∈Fk
|y|=k

where y ̸= y′. After uncomputing the error register, we postselect on the register being |0⟩. If the
postselection is successful, then the syndrome register is in the quantum state proportional to the
following unnormalized state vector

ℓ
X

wk
qm
k

X

| ePD(f)⟩:=

y∈Dk
|y|=k

k=0

(−1)v·y|BT y⟩.
(171)

The following theorem describes the effect that decoding failure rate ε has on the approximation
ratio achieved by DQI. We do not assume that 2ℓ+ 1 < d⊥.

Theorem 10.1. Given B ∈Fm×n
2
and v ∈Fm
2 , let f be the objective function f(x) = Pm
i=1(−1)vi+bi·x.

Let P be any degree-ℓpolynomial and let P(f) = Pℓ
k=0 wkP (k) (f1, . . . , fm) /
q

2nm
k

be the decom-
position of P(f) as a linear combination of elementary symmetric polynomials. Let |PD(f)⟩denote

39

## Page 40

a DQI state prepared using an imperfect decoder that misidentifies εk
m
k

errors of Hamming weight
k and let ⟨f⟩be the expected objective value for the symbol string resulting from the measurement
of this state in the computational basis. If v ∈Fm
2 is chosen uniformly at random, then

Ev⟨f⟩≥w† 
A(m,ℓ,0) −2ε(m + 1)

w
Pℓ
k=0 w2
k(1 −εk)
≥

w†A(m,ℓ,0)w

!

w†w
−2ε(m + 1)

,
(172)

where ε = max0≤k≤ℓεk and A(m,ℓ,0) is the tridiagonal matrix defined in equation (70). Moreover,
if ℓ≤m/2 and one chooses w to be the principal eigenvector of A(m,ℓ,0) then (172) yields the
following lower bound in the limit of large ℓand m with the ratio µ = ℓ/m fixed: For a random
v ∈Fm
2 ,

s

Ev⟨f⟩

ℓ
m

m
≥2

lim
m→∞
ℓ/m=µ

!


1 −ℓ


−ε

.
(173)

m

Before proving Theorem 10.1, we generalize lemma 10.1 and lemma 10.2 to the state |PD(f)⟩
prepared by DQI with an imperfect decoder upon successful postselection.

Lemma 10.4. The squared norm of | ePD(f)⟩is

ℓ
X

⟨ePD(f)| ePD(f)⟩=

k=0
w2
k(1 −εk) ≤w†w.
(174)

Proof. We first observe that all syndromes |BT y⟩for y ∈D are necessarily distinct bit strings and
thus orthogonal quantum states. This follows from the fact that if a deterministic decoder correctly
recovers y from the syndrome BT y, then it must fail on all y′ ̸= y with BT y′ = BT y. The squared
norm of | ePD(f)⟩is thus

ℓ
X

⟨ePD(f)| ePD(f)⟩=

k=0

as claimed.

ℓ
X

w2
k
m
k
|Dk| =

k=0
w2
k(1 −εk),
(175)

Lemma 10.5. For B ∈Fm×n
2
and v ∈Fm
2 , let f be the objective function f(x) = Pm
i=1(−1)vi+bi·x.

Let P be any degree-ℓpolynomial and let P(f) = Pℓ
k=0 wkP (k) (f1, . . . , fm) /
q

2nm
k

be the de-
composition of P(f) as a linear combination of elementary symmetric polynomials.
Let ⟨f⟩be
the expected objective value for the symbol string obtained upon measuring the imperfect DQI state
|PD(f)⟩in the computational basis. If the weights wk are such that |PD(f)⟩is normalized, then

⟨f⟩= w† ¯A(m,ℓ,D)w
(176)

where ¯A(m,ℓ,D) is the (ℓ+ 1) × (ℓ+ 1) symmetric matrix defined by

m
X

¯A(m,ℓ,D)
k,k′
=
1
qm
k
m
k′


X

i=1

40

(−1)vi+v·(y+y′)
(177)

(y,y′)∈S(i,D)
k,k′

## Page 41

for 0 ≤k, k′ ≤ℓ, and

S(i,D)
k,k′
= {(y, y′) ∈Dk × Dk′ : BT (y + y′ + ei) = 0}
(178)

for one-hot vectors e1, . . . , em in Fm
2 .

Proof. The proof is obtained from the proof of Lemma 10.2 by replacing each sum ranging over
Ek with a sum ranging over Dk and the ideal DQI state |P(f)⟩with the imperfect DQI state
|PD(f)⟩.

10.4
Average-case vith imperfect decoding

The expected objective value achieved by sampling from a normalized DQI state |PD(f)⟩is

⟨f⟩=
w† ¯A(m,ℓ,D)w
Pℓ
k=0 w2
k(1 −εk)
≥w† ¯A(m,ℓ,D)w

Next, we find the expectation of ¯A(m,ℓ,D).

w†w
.
(179)

Lemma 10.6. Let ¯A(m,ℓ,D) be defined as in (177). Suppose v is chosen uniformly at random from
Fm
2 . Then
Ev ¯A(m,ℓ,D) = A(m,ℓ,0) −E(m,ℓ,F)
(180)

where A(m,ℓ,0) is defined as in (70) and

E(m,ℓ,F)
k,k′
=
1
qm
k
m
k′


for 0 ≤k, k′ ≤ℓwith

m
X

i=1
|T (i,F)
k,k′ |
(181)

T (i,F)
k,k′
= {(y, y′) ∈Ek × Fk′ ∪Fk × Ek′ : y + y′ + ei = 0}.
(182)

Proof. We can partition S(i,D)
k,k′
into two disjoint subsets

S(i,D)
k,k′
=
S(i,0,D)
k,k′
∪S(i,1,D)
k,k′
(183)

S(i,0,D)
k,k′
=
{(y, y′) ∈S(i,D)
k,k′
: y + y′ + ei = 0}
(184)

S(i,1,D)
k,k′
=
{(y, y′) ∈S(i,D)
k,k′
: y + y′ + ei ̸= 0}
(185)

so that

m
X

¯A(m,ℓ,D)
k,k′
=
1
qm
k
m
k′


i=1

m
X

+
1
qm
k
m
k′


i=1

41

(−1)vi+v·(y+y′)

X

(y,y′)∈S(i,0,D)
k,k′

(−1)vi+v·(y+y′).
(186)

X

(y,y′)∈S(i,1,D)
k,k′

## Page 42

We next observe that when we average over v, the second term in (186) vanishes, because





(−1)vi+v·(y+y′)



X

Ev

(y,y′)∈S(i,1,D)
k,k′

Ev

(−1)vi+v·(y+y′)



=
X

(187)

(y,y′)∈S(i,1,D)
k,k′

1
2m
X

v∈Fm
2
(−1)v·(y+y′+ei)
(188)

=
X

(y,y′)∈S(i,1,D)
k,k′

=
X

δy+y′+ei,0
(189)

(y,y′)∈S(i,1,D)
k,k′

=
0,
(190)

where the last equality follows from the definition of S(i,1,D)
k,k′
. Hence,

m
X

Ev ¯A(m,ℓ,D)
k,k′
= Ev
1
qm
k
m
k′


i=1

(−1)vi+v·(y+y′).
(191)

X

(y,y′)∈S(i,0,D)
k,k′

We next examine (168) and observe that Ev ¯A(m,ℓ,D)
k,k′
and Ev ¯A(m,ℓ)
k,k′
differ only by replacing the

summation over S(i,0,D)
k,k′
with a summation over S(i,0)
k,k′ . Recalling the definition of S(i,0)
k,k′ from equation

(165), we observe that S(i,0)
k,k′ = S(i,0,D)
k,k′
∪T (i,F)
k,k′ . Hence,

m
X

Ev ¯A(m,ℓ)
k,k′
= Ev ¯A(m,ℓ,D)
k,k′
+ Ev
1
qm
k
m
k′


i=1

(y,y′)∈T (i,F)
(−1)v·(y+y′+ei).
(192)

X

By the definition of T (i,F) one sees that all terms in the sum have v · (y + y′ + ei) = 0 and hence

m
X

Ev ¯A(m,ℓ)
k,k′
= Ev ¯A(m,ℓ,D)
k,k′
+
1
qm
k
m
k′


By Lemma 10.3, this simplifies to

i=1
|T (i,F)|.
(193)

m
X

¯A(m,ℓ,0)
k,k′
= EvA(m,ℓ,D)
k,k′
+
1
qm
k
m
k′


By (181) we can rewrite this as

i=1
|T (i,F)|.
(194)

¯A(m,ℓ,0)
k,k′
= EvA(m,ℓ,D)
k,k′
+ E(m,ℓ,F)
k,k′
,
(195)

which rearranges to (180) completing the proof.

The last remaining ingredient for the proof of theorem 10.1 is the following upper bound on the
error term identified in Lemma 10.6.

42

## Page 43

Lemma 10.7. Let εk = |Fk|/
m
k

and ε = max0≤k≤ℓεk. Then,

∥E(m,ℓ,F)∥≤2ε(m + 1).
(196)

Proof. We note that E(m,ℓ,F)
k,k′
= 0 unless k = k′ ± 1, so E(m,ℓ,F) is tridiagonal with zeros on the
diagonal. By (181) we have

E(m,ℓ,F)
k,k+1
=
1
qm
k
 m
k+1


m
X

i=1
|T (i,F)
k,k+1|.
(197)

Note that if (y, y′) ∈T (i,F)
k,k+1, then yi = 0 and y′
i = 1. Therefore, every pair (y, y′) with y ∈Fk
contributes to at most m −k out of the m terms in the sum above. Similarly, every pair (y, y′)
with y′ ∈Fk+1 contributes to at most k + 1 terms. Consequently,

E(m,ℓ,F)
k,k+1
≤
1
qm
k
 m
k+1


(m −k)|Fk| + (k + 1)|Fk+1|

(198)


(m −k)εk

m
k

=
1
qm
k
 m
k+1


≤(εk + εk+1)
p

 m
k + 1


+ (k + 1)εk+1


(199)

(k + 1)(m −k)
(200)

≤ε(m + 1)
(201)

and by Gershgorin’s circle theorem

∥E(m,ℓ,F)∥≤2ε(m + 1)
(202)

completing the proof of the Lemma.

10.5
Proof of Theorem 10.1

Finally, we prove Theorem 10.1.

Proof. Equation (179) and Lemma 10.6 imply that

Ev⟨f⟩≥w† 
A(m,ℓ,0) −E(m,ℓ,F)
w
Pℓ
k=0 w2
k(1 −εk)
≥

which in light of Lemma 10.7 becomes

Ev⟨f⟩≥w† 
A(m,ℓ,0) −2ε(m + 1)

w
Pℓ
k=0 w2
k(1 −εk)
≥

w†A(m,ℓ,0)w

!

w†w
−w†E(m,ℓ,F)w

(203)

w†w

w†A(m,ℓ,0)w

!

w†w
−2ε(m + 1)

.
(204)

This proves the first part of Theorem 10.1. The second part, equation (173), follows by substi-
tuting the asymptotic formula for the leading eigenvalue of A(m,ℓ,0) derived in Lemma 9.3.

Remark 10.1. In practice, we find that decoding success probability decreases as the number of
errors increases. Therefore, we can use the empirical failure probability of a classical decoder on
uniformly random errors of Hamming weight ℓas an upper bound on ε, which would be the failure
probability of a decoder applied to a distribution over error weights zero to ℓdetermined by the
vector w.

43

## Page 44

11
Other Optimization Algorithms

In this section we survey algorithms against which DQI can be compared. In §11.1, we consider local
search heuristics such as simulated annealing and greedy optimization. In §11.2 we comment in more
detail on the convergence of simulated annealing when one adds more sweeps. In §11.3 we analyze
Prange’s algorithm in which one discards all but n of the m constraints on the n variables and then
solves the resulting linear system. In §11.4, we summarize the AdvRand algorithm of [58]. In §11.5,
we discuss the Quantum Approximate Optimization Algorithm (QAOA). Though necessarily not
exhaustive, we believe these algorithms constitute a thorough set of general-purpose optimization
strategies to benchmark DQI against on random sparse max-XORSAT. Lastly, we analyze the two
classes of algebraic algorithms that pose the most plausible challenge to DQI on our OPI problem
and find that they are not successful in our parameter regime. Specifically, in §11.6 we consider
list-recovery algorithms, and in §11.7, we summarize the lattice-based heuristic of [25].

11.1
General Local Search Heuristics

In local search methods, one makes a sequence of local moves in the search space, such as by flipping
an individual bit, and preferentially accepts moves that improve the objective function. This class
of heuristics includes simulated annealing, parallel tempering, TABU search, greedy algorithms,
and some quantum-inspired optimization methods. For simplicity, we will restrict our analysis to
max-XORSAT and consider only local search algorithms in which at each move a single variable
among x1, . . . , xn is flipped between 1 and 0.
The generalization to single-symbol-flip updates
applied to max-LINSAT is straightforward.
Let Ci be the set of constraints containing the variable xi. In Gallager’s ensemble |Ci| = D
for all i. For assignment x ∈Fn
2 let Si(x) be the number of constraints in Ci that are satisfied.
Consider an assignment x such that a fraction ϕ of the m constraints are satisfied. Then, modeling
C1, . . . , Cm as random subsets, we have

Pr [Si(x) = s] =
D
s


ϕs(1 −ϕ)D−s.
(205)

Next, consider the move x →x′ induced by flipping bit i. This causes all satisfied constraints in
Ci to become unsatisfied and vice-versa. Hence, such a move induces the change

Si(x′) = D −Si(x).
(206)

This will be an improvement in the objective value if and only if Si(x) < D/2. According to (205)
the probability P (+)
i
that the flip is an improvement is

⌊D−1

2
⌋
X

D
s

P (+)
i
=

s=0

By Hoeffding’s inequality, we have that


ϕs(1 −ϕ)D−s.
(207)

P (+)
i
≤exp
−2(ϕ −1/2)2D

.
(208)

For large ϕ the probability P (+)
i
becomes very small. When the probability of making an upward
move becomes extremely small, the local optimization algorithm will no longer be able to achieve

44

## Page 45

further improvement in any reasonable number of steps. If the algorithm takes a total of N steps
then, by the union bound and (208), the probability of finding such a move in any of the steps is
upper bounded by
P bound
success(ϕ) = N exp
−2(ϕ −1/2)2D

.
(209)

From this we can see what is the highest value of ϕ for which the success probability remains
significant. For example, if we set P bound
success(ϕmax) = 1/2 and solve for ϕmax the result is

r

ϕmax = 1

2 +

log N + log 2

2D
(210)

This analysis is only approximate. Indeed, one can see that the model cannot hold indefinitely
as N becomes larger, because eventually ϕmax becomes limited by the true optimum. Let us now
compare it with computer experiment. In Fig. 6 we show best fits to the satisfaction fraction
versus D with k/D fixed at 1/10, 1/2, and 9/10 for simulated annealing and greedy descent (which
is equivalent to zero-temperature simulated annealing).
We find that for each choice of k/D,
ϕmax −1/2 fits well to cD−ν for some constant c and some power ν but that the power ν is slightly
smaller than 1/2. We believe this to be a finite-size effect, as it has been shown [65] that for an
ensemble of random degree-D max-k-XORSAT instances differing only slightly from the Gallager
ensemble, the exact optimum scales like 1

2 + Pk
√

ϕmax = 1

2 +
c
√

D. Thus we find that the functional form

D
(211)

predicted by this argument is in reasonably good agreement with our experimental observations.

11.2
Convergence of Simulated Annealing

We next investigate whether the N-scaling predicted by the argument in §11.1 yields a good model
of the behavior of simulated annealing. This scaling cannot persist indefinitely because eventually
ϕmax is limited by the true optimum. In fact, we find that, in contrast to the D-scaling, the N-
scaling suggested by the above argument is not corroborated by experimental evidence. Instead,
empirical N-scaling fits much better to power-law convergence, as illustrated in Fig. 7.
Although we do not have a strong theoretical handle on the N-scaling, we can nevertheless
exploit the simple observation that increasing N has diminishing returns. Thus, in all empirical
analysis relating to simulated annealing, by choosing N large one can ensure data points are on
the relatively flat tail of the convergence curve and thus relatively insensitive to the specific choice
of N. This renders the trends noted in figures 6, 9, 13, and 15 relatively robust to choice of sweep
count. In each of these plots we also kept the number of sweeps fixed for all data points plotted in
order to minimize the effect of this as a confounding factor.
We next consider the problem of comparing the performance of DQI against simulated annealing.
This task is rendered complicated by the fact that the number of clauses that simulated annealing
is able to satisfy depends on how long one is willing to run the anneal. In Fig. 8, we plot the
convergence of simulated annealing as a function of number of sweeps for the instance defined in
§12 and compare against the satisfaction fraction achieved by DQI+BP. We use the same data as
in the lower panel of Fig. 7 but using a linear instead of logarithmic scale on the horizontal axis
and zooming in on the region where the number of sweeps is at least 105.

45

## Page 46

Figure 6: The approximation achieved by simulated annealing (left) and greedy optimization
(right) in our computer experiments at n = 105, on a log-log scale, where each constraint contains
k variables and each variable is contained in D constraints. The lines illustrates linear least-squares
curve fits to the log-log data. The ensemble of max-k-XORSAT instances is formally defined in
Appendix B. In these anneals we use 5, 000 sweeps with single-bit updates, and linearly increasing
inverse temperature β.

In all anneals, we start with inverse temperature β = 0 and then linearly increase with each
sweep to a final value of β = 5. Our results suggests this is an effective annealing schedule, although
we do not claim it is precisely optimal. In each sweep, we cycle through the n = 31, 216 bits, and for
each one consider a move in which the bit is flipped, accepting the move according to the Metropolis
criterion. For this instance, our implementation of simulated annealing, which is optimized C++
code, is able to execute approximately 16 sweeps (5 × 105 Metropolis moves) per second, though
this varied slightly from run to run likely due to the fact that accepted Metropolis moves incur a
larger computational cost than rejected moves in our implementation. Among our 1,079 annealing
experiments, the largest number of sweeps we carried out was 7 × 107, and the longest anneal
completed after 118 hours of runtime.
The first anneal to exceed the satisfaction fraction of 0.831 guaranteed by Theorem 10.1 for
BP+DQI used 6 × 107 sweeps and ran for 73 hours. Since we ran five anneals at each number of
sweeps we estimate that running five independent anneals in parallel at 6 × 107 sweeps would yield
a collection of approximate optima, the best of which has a nontrivial chance of exceeding 0.831.

11.3
Prange’s Algorithm

Consider an instance of max-XORSAT
Bx max
= v
(212)

where B is an m × n matrix over F2 and m > n. The system (212) is therefore overdetermined
and we wish to satisfy as many equations as possible. In Prange’s algorithm we simply throw away
all but n of the linear equations from this system so that it is no longer overdetermined. Then,
provided the remaining system is not singular, we can simply solve it, e.g. by Gaussian elimination.

46

## Page 47

Figure 7: Here we show the dependence of the fraction of constraints satisfied ϕ on the number of
Metropolis updates N used in simulated annealing. That is, N is the number of variables times the
number of sweeps. We find that the functional form ϕ = a + b√c log N suggested by the heuristic
argument of §11.1 fits poorly, but the form ϕ = a −bN−c fits reasonably well. On the top panel
we consider an instance from Gallager’s ensemble with k = 30, D = 60, and n = 15, 000. On
the bottom we use the irregular instance defined in §12, which has n = 31, 216. Each data point
represents the final outcome of an independent anneal, and in each anneal we vary β linearly from
zero to five.

47

## Page 48

Figure 8: Here we show the satisfaction fraction achieved by simulated annealing as a function of
the number of sweeps. For each number of sweeps we run five independent executions of simulated
annealing with different pseudorandom seeds. At the right-hand side of the plot we incremented
the number of sweeps by larger increments due to computational cost.

We thus obtain a bit string that definitely satisfies n of the original m constraints. Heuristically, one
expects the remaining m−n constraints each to be satisfied with probability 1/2, independently. In
other words the number of these m −n constraints satisfied is binomially distributed. One reruns
the above steps polynomially many times with different random choices of constraints to solve for.
In this manner one can reach a logarithmic number of standard deviations onto the tail of this
binomial distribution. Consequently, for max-XORSAT, the number of constraints one can satisfy
using Prange’s algorithm with polynomially many trials is n + (m −n)/2 + e
O(√m).
One can make the procedure more robust by bringing BT to reduced row-echelon form rather
than throwing away columns and hoping that what is left is non-singular. In this case, as long as
BT is full rank, one can find a bit string satisfying n constraints with certainty. From numerical
experiments one finds that matrices from Gallager’s ensemble often fall just slightly short of full
rank. Nevertheless, this procedure, when applied to Gallager’s ensemble, matches very closely the
behavior predicted by the above argument.
This heuristic generalizes straightforwardly to max-LINSAT. First, consider the case that
|f−1
i
(+1)| = r for all i = 1, . . . , m. In this case, we throw away all but n constraints, and choose
arbitrarily among the r elements in the preimage f−1
i
(+1) for each of those that remain. After
solving the resulting linear system we will satisfy all of these n constraints and on average we expect
to satisfy a fraction r/p of the remaining n −m constraints assuming the fi are random. Hence,
with polynomially many randomized repetitions of this scheme, the number of constraints satisfied
will be n + (m −n)(r/p) + e
O(√m). That is, the fraction ϕPR of the m constraints satisfied by a
solution found by Prange’s algorithm will be

 n

m + e
O(1/√m).
(213)

p +

1 −r

ϕPR = r

p

48

## Page 49

If the preimages f−1
i
(+1) for i = 1, . . . , m do not all have the same size, then one should choose the
n constraints with smallest preimages as the ones to keep in the first step. The remaining m −n
are then those most likely to be satisfied by random chance.

11.4
The AdvRand Algorithm

Prompted by some successes [5] of the Quantum Approximate Optimization Algorithm (QAOA),
a simple but interesting algorithm for approximating max-XORSAT was proposed by Barak et
al. in [58], which the authors named AdvRand. Although designed primarily for the purpose of
enabling rigorous average-case performance guarantees, the AdvRand algorithm can also be tried
empirically as a heuristic, much like simulated annealing, and compared against DQI.
Given an instance of max-XORSAT with n variables, the AdvRand algorithm works as follows.
Select two parameters R, F ∈(0, 1). Repeat the following sequence of steps polynomially many
times. First assign Rn of the variables uniformly at random. Substitute these choices into the
instance, yielding a new instance with (1 −R)n variables. A constraint of degree D will become a
constraint of degree D −r if r of the variables it contains have been replaced by randomly chosen
values. Thus, in the new instance some of the resulting constraints may have degree one. Assign
the variables in such constraints to the values that render these constraints satisfied. If there are
remaining unassigned variables, assign them randomly. Lastly, flip each variable independently
with probability F.
In [58], formulas are given for R and F that enable guarantees to be proven about worst case
performance. Here, we treat R and F as hyperparameters. We set F = 0 and exhaustively try all
values of Rn from 0 to n, then retain the best solution found. Our results on Gallager’s ensemble at
k = 3 are displayed and compared against simulated annealing and DQI+BP in Fig. 9 for constant
n and growing D.
In [58] it was proven that, given max-k-XORSAT instances, AdvRand can in polynomial time
find solutions satisfying a fraction 1

2 + e−O(k)
√

D
of the constraints, even in the worst case, provided
each variable is contained at most D constraints. Our observed empirical performance in Fig. 9
is in good agreement with this. In [65] it was shown that at large D, for average-case degree-D
max-3-XORSAT, the exact optimum concentrates at 1

2 + 0.9959
√

D , in the limit of large D. Thus, for
fixed k, the functional form of the scaling of AdvRand is provably optimal, and the key metric
of performance for given k is the specific value of the numerator e−O(k). For our experiments at
n = 20, 000 with k = 3 we empirically observe a value of 0.31.
In the simulated annealing experiments shown in Fig. 9, we vary β linearly from 0 to 3 and
apply 5, 000 sweeps through the variables, i.e. 5, 000n Metropolis updates.

11.5
Quantum Approximate Optimization Algorithm

In 2014, Farhi, Goldstone, and Gutmann introduced a new quantum algorithm for optimization
that they called the Quantum Approximate Optimization Algorithm (QAOA) [66]. The QAOA
algorithm is parameterized by a number of rounds, p. Allowing additional rounds can only improve
the approximate optima found by QAOA, but this also makes the algorithm harder to analyze
theoretically. The largest p for which QAOA’s performance has been analyzed on max-3-XORSAT
is p = 14, which was achieved in [7] using nontrivial tensor network techniques, which apply to
all D-regular max-3-XORSAT instances whose hypergraphs have girth greater than 2p + 1. In [7]
it was found that the fraction of satisfied clauses for every D-regular large-girth hypergraph, or

49

## Page 50

Figure 9:
On Gallager’s ensemble we compare the fraction ϕ of constraints satisfied in the
solutions found by DQI+BP, AdvRand, and simulated annealing. We also show the approximate
performance of p = 14 QAOA on large girth D-regular max-3-XORSAT instances, which was
calculated in [7], up to O(1/D) corrections. We fix k, the number of variables in each constraint, at
3 and we vary D, the number of constraints that each variable is contained in, from 4 to 687. The
red, blue, and green lines display the linear least-square fits to the log-log plot of ϕ −1/2 versus D.
We keep the number of variables fixed at n = 20, 000, thus m = Dn/3.

50

## Page 51

random D-regular hypergraphs in the n →∞limit, is

s

ϕQAOA = 1

2 + ¯ν[3]
14

where ¯ν[3]
14 = 0.6422 [67].

3
2(D −1) ± O(1/D),
(214)

In Fig.
9 we include a plot of the line ϕQAOA =
1
2 + ¯ν[3]
14
q

3
2(D−1), alongside the empirical
average-case performance on the Gallager ensemble of DQI using a standard belief propagation
decoder (DQI+BP). At small D the comparison between p = 14 QAOA and DQI+BP is not fully
conclusive due to the unknown O(1/D) corrections in (214), but for all D for which we can draw
firm conclusions, i.e. large D, QAOA at p = 14 outperforms DQI+BP on max-3-XORSAT.
A second point of comparison between DQI and QAOA is the Sherrington-Kirkpatrick model,
analyzed in [7,68]. The analysis in [7] shows that for average-case max-2-XORSAT containing all
n
2

possible constraints of the form xi ⊕xj = vk, each with random vk ∈{0, 1}, the number of
satisfied minus unsatisfied clauses achieved by QAOA scales as νpn3/2, where νp is a constant that
depends on p, the number of rounds in the QAOA algorithm. Using Theorem 13.2 from §13 one
finds that DQI, even using a classical decoder saturating the Shannon bound, would achieve at best
O(n3/2/√log n). Thus, DQI is not competitive on this problem, at least using classical decoders5.
A third point of comparison between DQI and QAOA is max-2-XORSAT where each variable
is contained in exactly D constraints. MaxCut for D-regular graphs is the special case of this
where v is the all ones vector. In [11] it was shown that QAOA with 17 rounds, when applied
to the MaxCut problem on any 3-regular graph of girth at least 36 can achieve a cut fraction
of 0.8971. For random 3-regular graphs, and any constant g, as the number of vertices goes to
infinity, the fraction of vertices that are involved in loops of size g goes to zero. Thus for average-
case instances of 3-regular MaxCut, QAOA with 17 rounds can asymptotically achieve cut fraction
0.8971.
Furthermore, since the performance of QAOA on max-XORSAT is independent of v,
QAOA can also satisfy fraction 0.8971 of the constraints for 3-regular max-2-XORSAT on average-
case graphs and arbitrary v. By Theorem 13.4, the satisfaction fraction achievable by DQI with
classical decoding is asymptotically upper bounded for 3-regular max-2-XORSAT by 0.75 if v is
chosen uniformly at random. Thus, at least for random v, DQI with classical decoders is beaten
by QAOA on 3-regular max-2-XORSAT.
In [7] it was shown that when applied to MaxCut problems on large-girth D-regular graphs,
QAOA achieves a cut fraction
1
2 +
νp
√

D −1 ± O(1/D),
(215)

where νp is a constant that increases with the number of rounds p and for which ν17 = 0.6773. As
in the case of D = 3 described above, this implies the same asymptotic performance on average-
case D-regular max-2-XORSAT. Since this analysis is only up to O(1/D) corrections, it cannot
be quantitatively compared at finite D against DQI. Nevertheless, Theorem 13.4 shows that the
approximation to average-case D-regular max-2-XORSAT achievable by DQI with classical decoders
is limited to 1/2 + 1/(2D −2). Thus, QAOA outperforms DQI with classical decoders in the limit
where k = 2 and D is large. To search for regimes of advantage for DQI one could instead consider
increasing k together with D, or using quantum decoders, as discussed in §13.

5One could also consider using quantum decoders such as BPQM [55], which take advantage of the coherence of
the errors and are limited only by the Holevo bound rather than the Shannon bound.

51

## Page 52

11.6
Algebraic Attacks Based on List Recovery

For our OPI instances, we believe that the most credible classical algorithms to consider as com-
petitors to DQI must be attacks that exploit algebraic structure.
The max-LINSAT problem can be viewed as finding a codeword from C that approximately
maximizes f. With DQI we have reduced this to a problem of decoding C⊥out to distance ℓ. For
a Reed-Solomon code, as defined in (14), its dual is also a Reed-Solomon code. Hence, both C and
C⊥can be efficiently decoded out to half their distances, which are m−n+1 and n+1, respectively.
However, max-LINSAT is not a standard decoding problem, i.e. finding the nearest codeword to a
given string under the promise that the distance to the nearest string is below some bound. In fact,
exact maximum-likelihood decoding for general Reed-Solomon codes with no bound on distance is
known to be NP-hard [30,31].
The OPI problem is very similar to a problem studied in the coding theory literature known as
list-recovery, applied in particular to Reed-Solomon codes. In list-recovery, for a code C ⊆Fm
p , one
is given sets F0, F1, . . . , Fm−1 ⊆Fp (which correspond to our sets f−1
i
(+1)), and asked to return all
codewords c ∈C so that ci ∈Fi for as many i as possible. It is easy to see that solving this problem
for Reed-Solomon codes will solve the OPI problem, assuming the list of all matching codewords is
small. However, existing list-recovery algorithms for Reed-Solomon codes rely on the size of the Fi
being quite small (usually constant, relative to m) and do not apply in this parameter regime. In
particular, the best known list-recovery algorithm for Reed-Solomon codes is the Guruswami-Sudan
algorithm [69]; but this algorithm breaks down when the size of the |Fi| is larger than m/n (this
is the Johnson bound for list-recovery). In our setting, |Fi| = p/2 ≈m/2, which is much larger
than m/n ≈10. Thus, the Guruswami-Sudan algorithm does not apply. Moreover, we remark
that in this parameter regime, if the fi are random, we expect there to be exponentially many
codewords satisfying all of the constraints; this is very different from the coding-theoretic literature
on list-recovery, which generally tries to establish that the number of such codewords is at most
polynomially large in m, so that they can all be returned efficiently. Thus, standard list-recovery
algorithms are not applicable in the parameter regime we consider.

11.7
Lattice-Based Heuristics

A problem similar to our Optimal Polynomial Intersection problem—but in a very different param-
eter regime—has been considered before, and has been shown to be susceptible to lattice attacks.
In more detail, in the work [24], Naor and Pinkas proposed essentially the same problem, but in the
parameter regime where p is exponentially large compared to m, and where |f−1
i
(+1)| ≪p/2 is very
small (in particular, not balanced, like we consider).6 The work [24] conjectured that this problem
was (classically) computationally difficult. This conjecture was challenged by Bleichenbacher and
Nguyen in [25] using a lattice-based attack, which we describe in more detail below. However, this
lattice-based attack does not seem to be effective—either in theory or in practice—against our OPI
problem. Intuitively, one reason is that in the parameter regime that the attack of [25] works, a
solution to the max-LINSAT problem—which will be unique with high probability—corresponds
to a unique shortest vector in a lattice, which can be found via heuristic methods. In contrast,

6In this parameter regime, unlike ours, for random fi it is unlikely that there are any solutions x with f(x)
appreciably large, so the problem of [24] also “plants” a solution x∗with f(x∗) = m; the problem is to find this
planted solution. Another difference is that DQI attains (213) for any functions fi, while in the conjecture of Naor
and Pinkas the fi are random except for the values corresponding to the planted solution.

52

## Page 53

in our parameter regime, there are many optimal solutions, corresponding to many short vectors;
moreover, empirically it seems that there are much shorter vectors in the appropriate lattice that do
not correspond to valid solutions. Thus, these lattice-based methods do not seem to be competitive
with DQI for our problem.
The target of the attack in [25] is syntactically the same as our problem, but in a very different
parameter regime. Concretely, p is chosen to be much larger than m or n, while the size r :=
|f−1
i
(+1)| of the set of “allowed” symbols for each i = 1, . . . , m is very small. (Here, we assume
that f−1
i
(+1) has the same size r for all i for simplicity of presentation; this can be relaxed). In [25],
the fi’s are chosen as follows. Fix a planted solution x∗, and set the fi so that fi(bi · x∗) = 1 for
all i; thus f(x∗) = m. Then for each i, fi(y) is set to 1 for a few other random values of y ∈Fp,
and fi(z) = −1 for the remaining z ∈Fp. With high probability, x∗is the unique vector with large
objective value, and the problem is to find it.
In our setting, where r = |f−1
i
(+1)| ≈p/2, m = p −1 and n = ⌈m/10⌋, we expect there to be
many vectors x with f(x) = m when the fi are random. We have seen that DQI can find a solution
with f(x) ≈0.7179m (even for arbitrary fi).
The way the attack of [25] works in our setting is the following. For x ∈Fn
p, define a polynomial
Px(Z) = Pn
j=1 xjZj−1. Let Fi = f−1
i
(+1), and write Fi = {vi,1, vi,2, . . . , vi,r} ⊆Fp. If f(x) = m,
then Px(γi) ∈Fi for all i = 1, . . . , m, where we recall from §5 that γ is a primitive element of Fp,
and Bi,j = γij. Let Li(Z) = Q
j̸=i
Z−γj
γi−γj . By Lagrange interpolation, we have



m
X

m
X

i=1
Px(γi)Li(Z) =

Px(Z) =

i=1




r
X

j=1
δ(P)
i,j
vi,j

Li(Z),
(216)

where δ(P)
i,j is 1 if Px(γi) = vi,j and 0 otherwise. Since Px(Z) has degree at most n−1, the coefficients
on Zk are equal to zero for k = n, n+1, . . . , p−1. Hence, (216) gives us p−n = m−n+1 Fp-linear
constraints on the vector δ ∈{0, 1}rm that contains the δ(P)
i,j ’s. Collect these constraints in a matrix
A ∈Fm−n+1×rm
p
, so that Aδ = 0. Consider the lattice Λ := {δ′ ∈Zrm | Aδ′ = 0 mod p}. Our
target vector δ clearly lies in Λ, and moreover it has a very short ℓ2 norm: ∥δ∥2 = √m. Thus, we
may hope to find it using methods like LLL [70] or Schnorr’s BKZ reduction [71, 72], and this is
indeed the attack.7 Upon finding a vector δ of the appropriate structure (namely, so that δ(P)
i,j = 1
for exactly one j ∈{1, . . . , r} for each i), we may read off the evaluations of Px from the Fi, and
hence recover x.
Bleichenbacher and Nguyen show that in some parameter regimes, the target vector δ with
length √m is likely to be the shortest vector in Λ. However, these parameter regimes are very
different from ours. For example, their results hold for p ≈280, and r ≤16, with codes of rate
n/m at least 0.88. In contrast, in our setting we have much larger lists, with r ≈p/2, and much
lower-rate codes, with n/m ≈1/10 (although in [25], they take m, n ≪p while we take m ≈p, so
this is not a direct comparison).
Empirically, this attack does not seem to work in our parameter regime. Indeed, the lattice
heuristics do find short vectors in the lattice Λ, but these vectors are much shorter than √m
whenever m and ndistractors are comparable to p (see Fig.
10).
As a consequence, the success
probability when applied to our OPI instances appears to decay exponentially with p.

7There are further improvements given in [25], notably passing to a sub-lattice that enforces the constraint that
Pr
j=1 δ(P )
i,j
is the same for all i.

53

## Page 54

Figure 10: The attack of Bleichenbacher and Nguyen [25] is workable when the shortest nonzero
vector in a particular lattice has weight √m. Above, left, we apply the BKZ algorithm [72] to
find the shortest nonzero vector (under the 2-norm) in the lattices arising from random problem
instances for various m and ndistractors. We observe that the shortest vector almost always has 2-
norm < √m in the regime where m and ndistractors are both a significant fraction of p. Consequently,
the success probability of the attack when applied to our OPI problem in the regime where m =
p −1, n = m/2, ndistractors = (p −3)/2 appears to exhibit exponential decay with p whether LLL,
BKZ with a block size of 15 (“BKZ-15”) or BKZ with unlimited block size. In this regime we
believe the lattice-based heuristic of [25] does not succeed.

12
Max-XORSAT Instances Advantageous to DQI Over Simu-
lated Annealing

In this section we construct a class of max-XORSAT instances such that DQI, using belief propaga-
tion decoders, achieves a better approximation than we are able to achieve using simulated annealing
if we restrict simulated annealing to a comparable number of computational steps. DQI+BP also
achieves a better approximation than we obtain from any of the other general-purpose optimiza-
tion algorithms that we try: greedy optimization, Prange’s algorithm, and AdvRand. However,
we do not claim this as an example of quantum advantage because we are able to also construct
a classical heuristic tailored to the class of instances which, within reasonable runtime, beats the
approximation achieved by DQI+BP. Also, as noted in the introduction, using very long anneals
(up to 118 hours) we are able to reach the satisfaction fraction achieved by DQI+BP for the in-
stance considered here. We have left the systematic investigation the scaling with n of the runtime
of simulated annealing for these instances to future work.
Given a max-XORSAT instance Bx max
= v, the degree of a variable is the number of constraints
in which it is contained. The degree of a constraint is the number of variables that are contained in
it. Hence, the degree of the ith constraint is the number of nonzero entries in the ith row of B and
the degree of the jth variable is the number nonzero entries in the jth column of B. For an LDPC
code, the degree of a parity check is the number of bits that it contains, and the degree of a bit is
the number of parity checks in which it is contained. These degrees correspond to the number of
nonzero entries in the rows and columns of the parity check matrix.
Given a max-XORSAT instance, let ∆j be the fraction of variables that have degree j. Let
κi be the fraction of constraints that have degree i. This is illustrated in Fig. 11. Via DQI, a
max-XORSAT instance with degree distribution ∆for the variables and κ for the constraints is

54

## Page 55

n variables

∆2 = 3

∆3 = 3

∆4 = 1

m constraints

κ2 = 1

2

κ3 = 1

5

κ1 = 3

10

Figure 11: Tanner graph for a sparse irregular LDPC code illustrating the notation introduced
in §12.

reduced to a decoding problem for a code with degree distribution ∆for the parity checks and
κ for the bits. For regular LDPC codes, in which every bit has degree k and every constraint
has degree D, the error rate from which belief propagation can reliably decode deteriorates as D
increases. However, it has been discovered that belief propagation can still work very well for certain
irregular codes in which the average degree ¯D of the parity checks is large [73]. In contrast, we
find that the approximate optima achieved by simulated annealing on the corresponding irregular
max-XORSAT instances of average degree ¯D are typically no better than on regular instances in
which every variable has degree exactly ¯D. This allows us to find examples where DQI achieves a
better approximation than simulated annealing.
If the m bits in an LDPC code have degree distribution κ the total number of nonzero entries in
the parity check matrix is m P
i iκi. If the n parity checks in an LDPC code have degree distribution
∆then the total number of nonzero entries in the parity check matrix is n P
j j∆j. Hence to define
a valid LDPC code, a pair of degree distributions must satisfy
Pm
i=1 κi
=
1
(217)
Pn
j=1 ∆j
=
1
(218)

m Pm
i=1 iκi
=
n Pn
j=1 j∆j.
(219)

Given any κ1, . . . , κm and ∆1, . . . , ∆n satisfying these constraints, it is straightforward to sample
uniformly from the set of all parity check matrices with m bits whose degree distribution is κ and
n parity checks whose degree distribution is ∆. Furthermore, the maximum error rate from which
belief propagation can reliably correct on codes from this ensemble can be computed in the limit
of m →∞by a method called density evolution, which numerically solves for the fixed point of a
certain stochastic process [36]. Using this asymptotic maximum error rate as an objective function,
one can optimize degree distributions to obtain irregular LDPC codes that outperform their regular
counterparts [73].

55

## Page 56

Figure 12: Degree distribution for an irregular instance sampled with m = 50, 000 and n = 31, 216.
The full table of variable and constraint degrees is available in our Zenodo record https://doi.
org/10.5281/zenodo.13327870.

As a concrete example, we consider the degree distribution shown in Fig. 12. After generating
a random max-XORSAT instance with 50,000 constraints and 31,216 variables consistent with this
degree distribution we find that belief propagation fails on 9 out of 10, 000 trials of decoding from
uniformly random errors of Hamming weight 6, 350. This bit flip error rate of 6, 350/50, 000 is
close to the asymptotic threshold of ≈13% predicted by density evolution. Thus for average case
v, Theorem 10.1 shows that DQI can asymptotically find solutions that satisfy at least 0.831m
constraints with high probability. In contrast, when we run simulated annealing on this instance
with 106 sweeps, for example, in sixteen trials the fraction of satisfied constraints ranges from
0.81024 to 0.81488.
The performance of simulated annealing on this instance as a function of
number of sweeps is discussed in detail in §11.2. Prange’s algorithm would be predicted to achieve
approximately 0.8122, and experimentally we saw 0.8124. The greedy algorithm performs far worse
than simulated annealing on this instance. In sixteen trials its best satisfaction fraction was 0.666.
Our trial of AdvRand achieved 0.5536.
The following classical algorithm can exceed the approximation achieved by DQI+BP on the
above example, by exploiting the highly unbalanced degree distribution of its constraints.
We
modify simulated annealing (which is described in §11.1) by adding a β-dependent factor to each
term in the objective function. Letting ni denote the number of variables contained in constraint
i, we use the objective function

We apply 1 million sweeps (since there are 50, 000 constraints this corresponds to fifty billion
Metropolis updates), interpolating linearly from β = 0 to β = 5.
After this, we are left with
solutions that satisfy approximately 0.88m clauses. We call this algorithm irregular annealing since
it takes advantage of the irregularity of the instance by prioritizing the lower-degree constraints
early in the annealing process.

## Page 57

13
Limitations of DQI

In addition to the power of DQI for solving optimization problems it is also interesting to delineate
its fundamental limits. Because DQI reduces optimization problems to decoding problems, some
limitations of DQI can be deduced from information theory. In this section we use information-
theoretic considerations to prove upper bounds on the performance of DQI on max-XORSAT. We
first consider the case where DQI uses a classical decoding algorithm implemented reversibly, as is
done throughout the rest of this manuscript. We then consider the case of intrinsically quantum
decoders. Lastly, we consider the special case of max-2-XORSAT, which in many respects behaves
differently from max-k-XORSAT with k ≥3.

13.1
General Limitations of DQI Under Classical Decoding

DQI reduces max-XORSAT to a decoding problem for a code C⊥with m bits and n parity checks.
Hence its rate R is
R = 1 −n

m.
(221)

The decoding is required to succeed with high probability when an error string e with Hamming
weight ℓhas been added to the codeword. We can model this by an error channel where each bit
is independently flipped with probability

p = ℓ/m.
(222)

This model is called the binary symmetric channel BSC(p). Although the distribution over error
weights in DQI is given by Pr(|e| = k) = |wk|2, whereas BSC(p) has Pr(|e| = k) = pk(1−p)m−km
k

,
the channels with these error distributions both asymptotically yield the same information-theoretic
capacity because in both cases the probability distribution over error weights is narrowly peaked
around ℓ. As shown by Shannon, the rate of a code that can reliably transmit information over
BSC(p) is limited by
R ≤1 −H2(p),
(223)

where H2(p) = −p log2(p) −(1 −p) log2(1 −p) is the binary entropy function. Substituting (221)
and (222) into (223) yields n

m ≥H2
ℓ

m

, which implies

ℓ
m ≤H−1
2
 n

m


(224)

where the inverse H−1
2
is well-defined, because ℓ/m ≤1/2. Substituting this into the semicircle
law (10) yields the following bound

H−1
2
 n

2 +
r

⟨s⟩Shannon

m
≤1

m

 
1 −H−1
2
 n


.
(225)

m

Since mH−1
2 (n/m) in general exceeds d⊥/2, Theorem 4.1 does not apply, though Theorem 10.1 still
does. That is, this must be interpreted as a bound on the performance of DQI for max-XORSAT
with average case v.
Let’s now consider this limit in relation to the ensemble of degree-D max-k-XORSAT instances
in which B is chosen from the (k, D)-regular Gallager ensemble. In this case we have n/m = k/D,
which can be substituted into (225) to yield concrete upper bounds on ⟨s⟩Shannon/m. In Fig. 13

57

## Page 58

we compare these upper bounds on the performance of DQI with classical decoding against the
empirical performance of simulated annealing as well as the known asymptotic performance of
Prange’s algorithm.
We note that in Fig. 13, DQI is analyzed asymptotically, whereas simulated annealing results are
obtained empirically at finite n. For simulated annealing we take n ≃2, 000 and use 500, 000 sweeps,
as we found these parameters to achieve a good tradeoff between asymptotic informativeness and
computational convenience. To improve the results of simulated annealing we run it five times for
each instance with different random seeds and report the maximum number of satisfied constraints
achieved by any of these five trials. This technique is referred to as “restarts,” and it is often used
in simulated annealing because running r repetitions of simulated annealing and keeping the best
result may often outperform the equally costly procedure of running a single anneal with r times
as many sweeps. We have n ≃2, 000 rather than n = 2, 000 because in the Gallager ensemble n
must always be a multiple of D.

Figure 13:
Here we consider degree-D max-k-XORSAT instances Bx max
=
v where v is uni-
formly random and B is drawn from the (k, D)-regular Gallager ensemble. In the orange region it
is information-theoretically impossible for DQI with classical decoding to outperform simulated
annealing on average-case instances from Gallager’s ensemble.
In the blue region, DQI with
maximum-likelihood (i.e.
Shannon-limit) decoding achieves a higher satisfaction fraction than
simulated annealing, but realizing this advantage with polynomial-time decoders remains an open
problem. Prange’s algorithm does not win on any region of this plot.

Although our main focus in this section is on limitations of DQI it is also worth discussing the
possibilities of DQI. In the blue region of Fig. 13 it is information-theoretically possible for DQI to
achieve average-case quantum advantage using classical decoders. Based on computational experi-
ments, we believe that this potential advantage is not realized by belief propagation decoding. This
is because the number of errors that belief propagation can successfully correct falls increasingly

58

## Page 59

short of the Shannon limit as the parity check matrices defining C⊥become denser. It is an open
question whether efficient classical decoders can be devised that approach the Shannon limit closely
enough for denser codes to allow DQI to outperform simulated annealing on average case instances
from Gallager’s ensemble. Efficient classical decoding of LDPC codes with denser than usual parity
check matrices has so far not been a subject of intensive research but some results in this direction
are obtained in [48–54].
To make (225) less unwieldy, we can use the following useful bound from [74].

Theorem 13.1. For all x ∈[0, 1],

x
2 log2
6

x
 ≤H−1
2 (x) ≤
x
log2
1

x
.
(226)

2 +
q

Substituting (226) into (225) yields the simpler but looser bound ⟨s⟩

n/m
log(m/n). In summary,
we have the following.

m ≤1

Theorem 13.2. Consider a max-XORSAT instance with m constraints and n variables where
v ∈Fm
2 is chosen uniformly at random. The expected number of satisfied clauses ⟨s⟩obtained by
DQI in the limit of large n using a classical decoder is bounded by

H−1
2
 n

 
1 −H−1
2
 n

2 +
r

⟨s⟩

m
≤1

m

m

s


≤1

n/m
log(m/n).
(227)

2 +

13.2
General Limitations of DQI Under Quantum Decoding

The bit flip errors that must be decoded in DQI are in coherent superposition. One can treat
these errors classically by implementing a classical decoding algorithm as a reversible circuit and
separately performing classical error correction on each “branch” of the superposition. This is the
strategy we describe and analyze throughout this manuscript.
However, this is not necessarily
optimal. Information-theoretically, at least, coherent errors are more advantageous than random
errors.
In the preceding section, to avoid complications arising from the details of the distribution
Pr(|e| = k) = |wk|2 over error weights arising in DQI, we approximated this by the binary symmetric
channel with bit flip probability p = ℓ/m. Similarly, we may approximate our distribution over
coherent errors using the following channel

|0⟩
→
|0p⟩

|1⟩
→
|1p⟩

where

|0p⟩
=
p

|1p⟩
=
√p |0⟩+
p

1 −p |0⟩+ √p |1⟩

1 −p |1⟩

and p = ℓ/m. The capacity of this channel is limited by Holevo’s bound, which states

59

R ≤χ(p),
(228)

## Page 60

where

χ(p) = S
1

2 |0p⟩⟨0p| + 1

2 |1p⟩⟨1p|

,
(229)

and S denotes the von Neumann entropy. By direct computation, one finds

1

2 −
p

χ(p) = H2

p(1 −p)

,
(230)

where, as before, H2 denotes the binary entropy function. When applying DQI to a max-XORSAT
problem with n variables and m constraints, our decoding problem is for a code C⊥of rate R =
1 −n/m. Hence, the Holevo bound implies via the semicircle law (10)

2 +
r

⟨s⟩Holevo

m
≤1

χ−1

1 −n

m

 
1 −χ−1

1 −n


(231)

m

where the inverse χ−1 is well-defined, because p = ℓ/m ≤1/2. Using (230) and simplifying one can
equivalently write (231) as
⟨s⟩Holevo

m
≤1 −H−1
2

1 −n


.
(232)

m

Next we apply this limit to Gallager’s ensemble where n/m = k/D. If we compare this limit to
the performance of simulated annealing and Prange’s algorithm for average-case instances of max-
XORSAT drawn from Gallager’s ensemble, analogously to in Fig. 13, we do not find any region
of the (k, D)-plane in which simulated annealing or Prange’s algorithm beat this upper bound on
DQI’s performance. Thus, the Holevo bound does not allow us to rule out quantum advantage by
DQI with quantum decoding for any region of the (k, D) plane for Gallager-ensemble instances.
But for other ensembles it may be successful in doing so.
In this section we consider the Holevo bound only as a tool for ruling out quantum advantage.
But it also suggests that in regions where quantum advantage is not achievable using DQI with
classical decoders it might be achievable using DQI with quantum decoders, if efficient quantum
circuits can be found to implement them. Some exciting results on efficient quantum circuits for
decoding coherent bit flip errors can be found in [13,42,55].

13.3
Limitations of DQI with Classical Decoding for max-2-XORSAT

The special case of max-k-XORSAT where k = 2 behaves somewhat differently in the context
of DQI than k > 2 and benefits from separate analysis. The max-2-XORSAT problem is widely
studied, particularly the special case of max-2-XORSAT where v is the all-ones vector, which is
known as MaxCut. Additionally, max-2-XORSAT is the unweighted special case of the Quadratic
Unconstrained Binary Optimization (QUBO) problem.
The code C⊥dual to an instance of max-2-XORSAT is one in which each bit is contained in
exactly two parity checks. Such codes are sometimes referred to as cycle codes (not to be confused
with cyclic codes, which are unrelated). It is known that cycle codes have minimum distance that is
at most logarithmic in their block length [75]. Although decoding of adversarial errors is impossible
beyond half the code distance, a large fraction of random errors of far greater Hamming weight
may be decodable.
Interestingly, for cycle codes, unlike for general LDPC codes, polynomial-time decoders can
achieve exact maximum-likelihood decoding, i.e. saturate the information-theoretic limit. A cycle

60

## Page 61

code can be associated with a graph whose edges represent bits and whose vertices represent the
parity checks. A given syndrome corresponds to a subset T of the vertices, and the lowest Hamming
weight error (which is the maximum likelihood error for the binary symmetric channel) is given by
the minimum-weight T-join, which can be found in polynomial time [76].
In [75], the following theorem is proven.

Theorem 13.3. Consider an asymptotic family of LDPC codes in which each bit is contained in
exactly two parity checks and each parity check contains exactly D bits. The rate of these codes is
then R = 1−2/D. Let p2 be the largest probability such that, if each bit is independently flipped with
probability p2, then maximum-likelihood decoding will recover the original codeword with probability
converging to one in the limit of large block size. Then,

2
(1 −
√

p2 ≤1

R)2

1 + R
.
(233)

This theorem provides new information specific to k = 2 because, as one can easily verify, the
above bound on p2 lies below the corresponding Shannon bound pgeneral ≤H−1
2 (1 −R) for general
codes. We also note that our computer experiments suggest that, for D = 3 the bound (233) is
essentially saturated by the cycle codes arising from random 3-regular graphs.
For max-2-XORSAT, we are mainly interested in the case 2ℓ+ 1 > d⊥since, as noted above,
d⊥= O(log n). We therefore rely on Theorem 10.1, which together with Theorem 13.3 implies the
following.

Theorem 13.4. Consider an asymptotic family of max-2-XORSAT instances in which v ∈Fm
2 is
chosen uniformly at random and each variable is contained in exactly D constraints. In the limit
of large n the performance of DQI using classical decoders is limited by

⟨s⟩

m ≤1

2 +
1
2(D −1).
(234)

Proof. Rewriting (173) from Theorem 10.1 in terms of the expected number of constraints satisfied
⟨s⟩instead of the expected objective value ⟨f⟩yields

s

⟨s⟩

m = 1

ℓ
m

2 +


1 −ℓ


−ε.
(235)

m

From Theorem 13.3, the information-theoretic limit of decoding cycle codes is at

2
(1 −
√

R)2

ℓ
m = 1

1 + R
and
ε = 0
(236)

Substituting (236) and R = 1 −2/D into (235) and simplifying yields (234).

14
DQI for Folded Codes and over Extension Fields

In §8, we describe the DQI algorithm for the max-LINSAT problem over prime fields. However,
DQI works over extension fields as well, and also works for so-called folded codes. In this section,
we go through the details to extend DQI to these settings. Our main motivation is to show that
DQI is applicable to the problem considered by Yamakawa and Zhandry in [44], which is similar to
our OPI problem, but for folded Reed-Solomon codes. Moreover, as discussed in §7, if a variant of
Theorem 4.1 applies in the regime studied by Yamakawa and Zhandry, then equation (9) implies
that DQI can find a solution satisfying all constraints.

61

## Page 62

14.1
Folded max-LINSAT problem

In [44], Yamakawa and Zhandry define the following oracle problem, which they prove can be solved
in polynomially many queries by a quantum computer but requires exponentially many queries for
classical computers.

Definition 14.1. Fix a prime power q and integers m, n, r such that r divides m and m > n. Let
O : {1, . . . , m/r} × Fr
q →{0, 1} be a random function. Let B ∈Fm×n
q
be a Vandermonde matrix
(so that Bi,j = γij for i ∈{0, . . . , m −1}, j ∈{0, . . . , n −1} where γ is a primitive element of Fq),
written as





B1
B2



B =

...
Bm/r


(237)

where Bi ∈Fr×n
q
. The Yamakawa-Zhandry problem is, given B and query access to O, to efficiently
find x ∈Fn
q such that O(i, Bix) = 1 for all i ∈{1, . . . , m/r}.

The problem in Definition 14.1 has some similarities to Definition 2.1, and especially to our
OPI example in §5, but is not exactly the same, as the problem in Definition 14.1 is for folded
Reed-Solomon codes, over an extension field Fq.
Below, we extend DQI to this setting. More
precisely, we consider the following generalization of Definition 2.1.

Definition 14.2 (Folded max-LINSAT). Let Fq be a finite field, where q is any prime power. For
i = 1, . . . , m/r, let fi : Fr
q →{+1, −1} be arbitrary functions. Given a matrix B ∈Fm×n
q
written as





B1
B2



B =

...
Bm/r


(238)

with Bi ∈Fr×n
q
, the r-folded max-LINSAT problem is to find x ∈Fn
q maximizing the objective
function

m/r
X

f(x) =

i=1
fi(Bix).
(239)

We now describe how to adapt the presentation in §8.2 to the folded max-LINSAT problem.
As before, we first discuss the properties of the DQI state |P(f)⟩:= P
x∈Fnp P(f(x))|x⟩and then
describe the algorithm for creating it.
Again, mirroring §8.2, we assume that 2ℓ+ 1 < d⊥where d⊥is the minimum distance of the
folded code C⊥= {d ∈Fm
q : BT d = 0}. Note that folding affects the definition of d⊥. In a folded
code, we view every codeword y ∈Fm
q as an m/r-tuple (y1, . . . ym/r) of elements of Fr
q and regard
each yi as a symbol. Consequently, the Hamming weight |.| : Fm
q →{0, . . . , m/r} associated with
the folded code is the number of yi not equal to 0 ∈Fr
q.

62

## Page 63

14.2
DQI Quantum State for Folded max-LINSAT

As in §8.2, we assume that no fi is constant and that the preimages Fi := f−1
i
(+1) have the same
cardinality for all i = 1, . . . , m/r. This allows us to define gi as fi shifted and rescaled so that its
Fourier transform
˜gi(y) =
1
√qr
X

x∈Frq
ωtr(y·x)
p
gi(x),
(240)

where tr : Fq →Fp given by tr(x) = x+xp+xp2 +. . .+xq/p is the field trace, vanishes at y = 0 ∈Fr
q
and is normalized, i.e. P
x∈Frq |gi(x)|2 = P
y∈Frq |˜gi(y)|2 = 1. More explicitly, we define

gi(x) := fi(x) −f

φ
(241)

qr
P
x∈Frq fi(x) and φ :=
P
y∈Frq |fi(y) −f|21/2
. The sums f(x) = Pm/r
i=1 fi(Bix) and

where f := 1

g(x) = Pm/r
i=1 gi(Bix) are related by f(x) = g(x)φ + mf/r. Substituting this relationship for f
in P(f), we obtain an equivalent polynomial Q(g) which, by Lemma A.1 in Appendix A, can be
expressed as a linear combination of elementary symmetric polynomials P (k)

ℓ
X

l=0
ukP (k)
g1(B1x), . . . , gm/r(Bm/rx)

.
(242)

Q(g(x)) :=

We will write the DQI state

|P(f)⟩=
X

x∈Fnq
P(f(x))|x⟩=
X

as a linear combination of |P (0)⟩, . . . , |P (ℓ)⟩defined as

|P (k)⟩:=
1
q

qn−rkm/r
k

X

x∈Fnq
Q(g(x))|x⟩= |Q(g)⟩
(243)

x∈Fnq
P (k)
g1(B1x), . . . , gm/r(Bm/rx)

|x⟩.
(244)

By definition,

P (k)(g1(B1x), . . . , gm/r(Bm/rx))
=
X

Y

i1,...,ik
distinct

=
X

Y

i1,...,ik
distinct

1
p

=
X

y∈Fm
q
|y|=k

63

i∈{i1,...,ik}
gi(Bix)
(245)





1
√qr
X

yi∈Frq
ω−tr(yi·Bix)
p
˜gi(yi)

(246)

i∈{i1,...,ik}

m/r
Y

qrk ω−tr((BT y)·x)
p

˜gi(yi)
(247)

i=1
yi̸=0

## Page 64

where |.| : Fm
q →{0, . . . , m/r} is the Hamming weight associated with the folded code. From (247)
we see that the Quantum Fourier Transform of |P (k)⟩is

| eP (k)⟩:= F ⊗n|P (k)⟩=
1
qm/r
k

X

y∈Fm
q
|y|=k





m/r
Y


|BT y⟩.
(248)

˜gi(yi)




i=1
yi̸=0

As in §8.2, if |y| < d⊥/2, then BT y are all distinct and |P (0)⟩, . . . , |P (ℓ)⟩form an orthonormal set.
Consequently,

ℓ
X

|P(f)⟩=

where

s

wk = uk

and ⟨P(f)|P(f)⟩= ∥w∥2.

k=0
wk |P (k)⟩
(249)

qn−rk
m/r
k


,
(250)

14.3
DQI Algorithm for Folded max-LINSAT

Similarly to DQI for general max-LINSAT, the algorithm for folded max-LINSAT uses three quan-
tum registers: a weight register comprising ⌈log2 ℓ⌉qubits, an error register with m⌈log2 q⌉qubits,
and a syndrome register with nr⌈log2 q⌉qubits. We will consider the error and syndrome registers
as consisting of m/r and n subregisters, respectively, where each subregister consists of r⌈log2 q⌉
qubits. We will also regard the rightmost qubits from all subregisters of the error register as forming
the mask register of m/r qubits. We assume that the encoding of Fq into each of the r components
of a subregister uses a basis that contains 1, so that 1 ∈Fq is encoded as |0, . . . , 0, 1⟩.
We begin by initializing the weight register in the normalized state Pℓ
k=0 wk |k⟩.
Next, we
prepare the mask register in the Dicke state corresponding to the weight register

ℓ
X

k=0
wk |k⟩
1
qm/r
k

X

→

and then uncompute the weight register, obtaining

ℓ
X

|µ⟩
(251)

µ∈{0,1}m/r
|µ|=k

k=0
wk
1
qm/r
k

X

→

|µ⟩.
(252)

µ∈{0,1}m/r
|µ|=k

Let Gi denote a unitary acting on r⌈log2 q⌉qubits that sends |0⟩to |0⟩and |0, . . . , 0, 1⟩to
X

c∈Frq
˜gi(c) |c⟩=
X

64

c∈Frq\{0}
˜gi(c) |c⟩.
(253)

## Page 65

See §14.4 below for an implementation of Gi in the oracle setting. As in the case of DQI for general
max-LINSAT, parallel application G := Qm/r
i=1 Gi of Gi to all subregisters of the error register
preserves the Hamming weight, so that
X

G |µ⟩=
X

y∈Fm
q
|y|=k

µ∈{0,1}m/r
|µ|=k

˜gy(1)
yy(1)

. . . ˜gy(k)
yy(k)

|y⟩
(254)

where yi for i ∈{1, . . . , m/r} denotes the ith entry of y, and y(j) denotes the index of the jth

nonzero entry of y. Consequently, by applying G to the error register, we obtain

ℓ
X

k=0
wk
1
qm/r
k

X

→

y∈Fm
q
|y|=k

˜gy(1)(yy(1)) . . . ˜gy(k)(yy(k)) |y⟩.
(255)

Next, we reversibly compute BT y into the syndrome register

ℓ
X

k=0
wk
1
qm/r
k

X

→

y∈Fm
q
|y|=k

˜gy(1)(yy(1)) . . . ˜gy(k)(yy(k)) |y⟩|BT y⟩.
(256)

The task of finding y from BT y is the bounded distance syndrome decoding problem on the folded
code C⊥= {y ∈Fm
q : BT y = 0}. Consequently, uncomputing the content of the error register can
be done efficiently whenever the bounded distance decoding problem on C⊥can be solved efficiently
out to distance ℓ.
Uncomputing disentangles the syndrome register from the error register, leaving behind

ℓ
X

k=0
wk
1
qm/r
k

X

→

y∈Fm
q
|y|=k



m/r
Y

ℓ
X

k=0
wk
1
qm/r
k

X

˜gi(yi)

=




y∈Fm
q
|y|=k

i=1
yi̸=0

ℓ
X

˜gy(1)(yy(1)) . . . ˜gy(k)(yy(k)) |y⟩|BT y⟩
(257)




|BT y⟩
(258)

k=0
wk | eP (k)⟩
(259)

=

which becomes the desired state |P(f)⟩after applying the Quantum Fourier Transform.

14.4
Oracle Access to Objective Function

In our discussion of DQI for general max-LINSAT, we assumed that the field size p is polynomial in
n. In that setting, the objective functions fi can be given explicitly by their values at all elements
of Fp and hence the gates Gi can be realized efficiently using techniques from [63]. By contrast, in
Yamakawa-Zhandry problem, the random function O is available via query access to an oracle.

65

## Page 66

Figure 14: Quantum circuit implementing Gi gate using oracle access. The circuit takes as input
a single subregister of the error register and employs an auxiliary qubit initialized in |0⟩. It begins
by swapping the qubit corresponding to 1 in the input with the auxiliary qubit. Then it applies
the Quantum Fourier Transform (QFT) F over Fr
q, followed by a call to the oracle Ui, followed by
another QFT. The QFT gates are conditional on the auxiliary qubit. The circuit ends with the
uncomputation of the auxiliary qubit by flipping it when the subregister is non-zero.

Here, we show how to realize the gates Gi in a setting where the functions fi(.) = O(i, .) are
provided by oracles and without assuming that the field size q is polynomial in n. For simplicity,
we assume that q is a power of two, fi is balanced, i.e. |f−1(+1)| = qr/2, and fi(0) = +1.
Suppose oracle Ui for fi is defined as

Ui |x⟩= fi(x) |x⟩
(260)

for x ∈Fr
q and let

F |x⟩=
1
√qr
X

y∈Frq
(−1)tr(x·y) |y⟩
(261)

be the Quantum Fourier Transform on a subregister of the error register. Then Gi can be realized
using a single auxiliary qubit as shown in Fig. 14. When the input is |0⟩, then all operations act
as identity, so Gi |0⟩= |0⟩. When the input is |0, . . . , 0, 1⟩, then the SWAP gate sets the auxiliary
qubit to the |1⟩state and the input qubits into |0⟩. Subsequent three operations yield

FUiF |0⟩=
X

y∈Frq
˜gi(y) |y⟩.
(262)

Moreover, ˜gi(0) = 0, so the last operation uncomputes the auxiliary qubit.

15
Multivariate Optimal Polynomial Intersection

In this section we describe the application of DQI to the multivariate generalization of the OPI
problem.

Definition 15.1. Let r, u, m, q be integers where q is a prime power, 1 ≤u ≤(q −1)m, and
1 ≤r < q. For each z ∈Fm
q
let L(z) ⊂Fq with |L(z)| = r. Given such subsets specified by
explicit tables, the multivariate optimal polynomial intersection problem mOPI(r, u, m, q) is to find
a polynomial Q ∈Fq[z1, . . . , zm] of total degree at most u that maximizes the objective function f
defined by
f[Q] =

z ∈Fm
q : Q(z) ∈L(z)
.
(263)

66

## Page 67

An instance of mOPI(r, u, m, q) is specified by the lists L(z) ⊂Fq for all z ∈Fm
q .
Specifying
these requires qm+1 bits. Hence, throughout this section when we say “polynomial-time” we mean
polynomial in qm. The OPI problem is the special case of mOPI where m = 1 and q is a prime of
polynomial magnitude.
We next recount some background information about Reed-Muller codes, which we will need to
describe how DQI can be applied to the mOPI problem. The following exposition is based on [77].
For a given multivariate polynomial Q(z1, . . . , zm) over Fq let Eval(Q) be the symbol string
in Fn
q obtained by evaluating Q at all possible assignments to z1, . . . , zm in lexicographical order.
Hence,
n = qm.
(264)

Let Pq,m,u be the set of polynomials in Fq[z1, . . . , zm] of total degree at most u. In Fq, raising a
variable to power q −1 yields the identity. Thus, the number of distinct monomials from which
elements of Pq,m,u can be constructed is







.
(265)

m
X

(i1, . . . , im) : 0 ≤ij ≤q −2 and

k =

j=1
ij ≤u



A polynomial in Pq,m,u is determined by choosing the coefficients from Fq for each of these k
monomials. Hence, |Pq,m,u| = qk.

Definition 15.2. Given a prime power q and integers u, m satisfying 1 ≤u ≤m(q −1), the
corresponding Reed-Muller code RMq(u, m) is {Eval(Q) : Q ∈Pq,m,u}.

We observe that RMq(u, m) is an Fq-linear code; it linearly maps from the k coefficients that define
Q to the n values in Eval(Q).

As discussed in [47], the dual of a Reed-Muller code is also Reed-Muller code.

Theorem 15.1. The dual code to RMq(u, m) is RMq(u⊥, m), where

u⊥= m(q −1) −u −1.
(266)

From [78], based on [79], we have the following.

Theorem 15.2. Let α and β be the quotient and remainder obtained when dividing u by q −1.
That is, u = α(q−1)+β with 0 ≤β < q−1. Then the distance of RMq(u, m) is d = (q−β)qm−α−1.

As discussed in Chapter 13 of [80], the methods of [47] imply a polynomial-time classical reduction
from decoding Reed-Muller codes to decoding Reed-Solomon codes, and therefore the following
theorem holds.

Theorem 15.3. The code RMq(u, m) can be decoded from errors up to weight
 d−1

2

with perfect
reliability by a polynomial time classical algorithm.

From the above facts we see that DQI reduces the problem mOPI(r, u, m, q) to decoding of a
Reed-Muller code RMq(u⊥, m), where u⊥= m(q −1) −u −1. Given an algorithm that can decode
RMq(u⊥, m) out to ℓerrors, DQI will achieve an expected value of f given by the following theorem,
which is a straightforward generalization of Lemma 9.2. (Here we include finite-size corrections since
taking a limit of large problem size while keeping the ratio of constraints to variables fixed is not
straightforward in the context of mOPI.)

67

## Page 68

Theorem 15.4. Suppose we have an efficient algorithm that decodes C⊥= RMq(u⊥, m) out to ℓ
errors. Let d⊥be the distance of C⊥. If 2ℓ+1 < d⊥, then for any instance of GPR(r, u, m, q), DQI
produces in polynomial time samples from polynomials Q such that expected value of the objective
f[Q] is

p

⟨f⟩= qm r

q +

r(q −r)

q
λ(q)
max
(267)

where λ(q)
max is the largest eigenvalue of the following (ℓ+ 1) × (ℓ+ 1) symmetric tridiagonal matrix



0
a1
a1
d
a2



A(q) =

k(qm −k + 1) and d =
q−2r
√

with ak =
p

r(qm−r).





a2
2d
...
...
aℓ
aℓ
ℓd

(268)

Together, theorems 15.4, 15.3, and 15.2 yield a strong performance guarantee for DQI applied to
mOPI(r, u, m, q), particularly when q ≥u. Comparing this performance against competing classical
algorithms remains for future work.

16
Resource Estimation for OPI

In this section we look at the resources required to construct a quantum circuit for syndrome
decoding of Reed Solomon codes using the Berlekamp-Massey decoding algorithm [23]. Since the
decoding step is the dominant cost in DQI, this gives us an estimate of the resource requirements
for DQI to solve OPI. Whereas our example in §5 uses a ratio of ten constraints per variable,
here we consider two constraints per variable, as this appears to be a more optimal choice for the
purpose of solving classically-intractable instances of OPI using as few quantum gates and qubits
as possible. That is, throughout this section, the number of constraints is p −1 and the number of
variables is n ≃p/2.
An outline of the key steps of Berlekamp-Massey syndrome decoding algorithm is given in Al-
gorithm 1. Readers seeking more detail can see Appendix E of [81], where the algorithm used here
is explained in the context of BCH decoding. Asymptotically, the most computationally intensive
step is the subroutine BerlekampMasseyLFSR, responsible for finding the shortest linear feedback
shift register (LFSR). Standard irreversible implementations of this subroutine often rely on con-
ditional branching and variable assignments that do not directly translate to efficient reversible
circuits. Consequently, a naive reversible implementation of this subroutine can lead to significant
overhead in terms of quantum resources, potentially undermining the overall efficiency of the DQI
algorithm.
We address this challenge by presenting an optimized reversible implementation of the Berlekamp-
Massey algorithm for finding the shortest LFSR in Algorithm 2. Our implementation is a gener-
alization of the implementation given by [82], and works for any finite field Fq. For a sequence of
length n and a retroaction polynomial of maximum degree ℓ, Algorithm 2 can be implemented as
a quantum circuit using O(n · ℓ) multiplications in Fq and using 2 · (n + ℓ) · ⌈log2 q⌉+ n + log2 ℓ

68

## Page 69

Table 2: Quantum circuit costs for modular arithmetic operations on n-bit operands in Fp.

qubits. For finite fields Fp, where p is a prime, we list the costs for performing modular arithmetic
operations in Table 2. In our Zenodo record (https://doi.org/10.5281/zenodo.13327870) we
provide an implementation of Algorithm 2 for prime fields Fp using Qualtran [34]. We present the
resulting resource estimates in Table 3.

Table 3: Cost of finding shortest linear feedback shift register (LFSR) using Algorithm 2, imple-
mented and analyzed using Qualtran [34]. This is the most expensive step of Berlekamp-Massey
syndrome decoding algorithm [23] for Reed Solomon codes, as presented in Algorithm 1. Here
n = N −K is the number of syndromes, which is equal to the length of the input sequence to
Berlekamp-Massey algorithm, and ℓ= n

2 is the maximum number of correctable errors, which is
equal to the degree of retroaction polynomial.

As a point of comparison, we can estimate the classical cost of solving the instances in Table
3 by repeating Prange’s algorithm with different size-n random subsets of the constraints until
the target satisfaction fraction is reached. As an example, consider the case p = 521. Here, we
have 260 variables and 521 constraints, of which DQI is able to satisfy 486. In a given trial of
Prange’s algorithm one uses Gaussian elimination to obtain a solution that is guaranteed to satisfy
260 of the constraints and which satisfies each of the remaining 261 constraints with probability
r/p = 1/2. To beat DQI Prange’s algorithm needs to satisfy at least 226 among these remaining

69

## Page 70

261 constraints. The probability of this on a given trial is

261
X

261
m

1
2261

m=226


≃10−35.
(269)

Thus solving this instance by the repeat-until-success version of Prange’s algorithm should require
on the order of 1035 repetitions. Therefore, assuming a CPU can execute on the order of a billion
elementary operations per second this yields a total cost of at least 1026 CPU-seconds, even if each
trial could be parallelized into a single clock-cycle.
As noted in [89], achieving such large separation between classical and quantum resource costs
at reasonable problem size is only possible when the underlying source of advantage goes beyond
quadratic speedups based on Grover’s algorithm and its generalizations such as amplitude ampli-
fication and quantum walks. More specifically, in [90] the cost of solving random 14-SAT at the
satisfiability phase transition using Grover’s algorithm and quantum backtracking methods was
estimated, and it was found that Grover’s algorithm required lower resources, namely a T-depth of
1014 and a Toffoli count of 1019 on instances that they estimate would require 1010 CPU-seconds
classically.
Although the repeat-until-success version of Prange’s algorithm is a standard technique that
provides a useful point of comparison, we do not specifically claim it to be optimal. In §11.6 and
§11.7 we have surveyed all of the classical algorithms that we can find in the literature applicable
to OPI and find that none yield polynomial-time solutions in the parameter regime discussed here.
Nevertheless, there may be classical techniques to achieve better scaling than Prange’s algorithm,
while still requiring exponential time; such incremental improvements to exponential runtimes are
quite common in the cryptanalysis literature (see for example [91]). We leave the investigation of
this possibility to future work.

Algorithm 1 Syndrome decoding of RSq(⃗γ, N, K) using Berlekamp Massey algorithm

1: Input: A list s = [s1, s2, . . . , sn] of syndromes where n = N −K.

2: Output: A list e = [e1, e2, . . . , eN] of error values such that |supp(e)| ≤ℓwhere ℓ= n

2
3: ▷Step-1: Find error locator polynomial σ(Z) of degree ≤ℓ, by solving for shortest linear
feedback shift register (LFSR) using Berlekamp-Massey algorithm.

4: ▷Uses O(N2) multiplications and O(N) inversions of elements in Fq.

5: σ(Z) ←BerlekampMasseyLFSR(s, ℓ)

6: ▷Step-2: Find error evaluator polynomial Ω(Z) via fast polynomial multiplication using Number
Theoretic Transform (NTT).

7: ▷Uses O(N log N) multiplications of elements in Fq.

8: Ω(Z) ←σ(Z) × S(Z) mod Zn+1

9: ▷Step-3: Find roots of σ(Z) to determine locations of errors by evaluating σ(Z) for all N roots
of unity (⃗γ) using NTT.

10: ▷Uses O(N log N) multiplications of elements in Fq.

11: sigma roots ←chien search(σ(Z),⃗γ)

12: ▷Step-4: Use evaluations of Ω(Z) and σ′(Z) for all N roots of unity (⃗γ) to determine the values
of errors e.

13: ▷Uses O(N log N) multiplications and O(N) divisions of elements in Fq.

14: e ←forneys algorithm(Ω(Z), σ(Z), sigma roots,⃗γ)

70

## Page 71

Algorithm 2 Reversible Berlekamp-Massey algorithm to find shortest LFSR over Fq.

1: Input: A list s = [s0, s1, . . . , sn−1] in Fq and an integer ℓ≤n.

2: Output: Retroaction polynomial C(X) ∈Fq[X] such that deg(C(X)) ≤ℓ.

3: Storage: Register for s (n elements in Fq) and C(X) (ℓelements in Fq)

4: Garbage: Register for L (log2 ℓbits), B(X) (ℓelements in Fq), d = [d0, d2, . . . , dn−1] (n
elements in Fq) and v = [v0, v2, . . . , vn−1] (n bits)

5: Total Qubits: 2 × (n + ℓ) × ⌈log2 q⌉+ log2(ℓ) + n

6: c ←[−1]
▷c and b correspond to list of coefficients for C(X) and B(X); C(X) = Pℓ
i=0 cixi

7: b ←[−1]
▷−1 is the additive inverse of 1 in Fq
8: L ←0

9: for i in 0, . . . , N −1 do

10:
di ←Plen(c)
j=0 si−j × cj
▷≤ℓ+ 1 quantum-quantum multiplications and additions

11:
vi ←(2L ≤i)
▷quantum-classical comparator to decide between case 2 and case 3

12:
if i < ℓthen

13:
c ←concatenate(c, [0])
▷Extends register for C(X) upto a maximum length ℓ+ 1

14:
b ←concatenate([0], b)
▷Equivalent to performing B(X) ←X · B(X)

15:
else

16:
b ←roll(b, 1)
▷Equivalent to performing B(X) ←X · B(X)

17:
end if

18:
r ←(1 if di = 0 else di)

19:
b ←b × r
▷≤ℓ+ 1 in-place quantum-quantum multiplications

20:
if di ̸= 0 then

21:
c ←c −b
▷≤ℓ+ 1 quantum-quantum controlled subtractions

22:
end if

23:
if di ̸= 0 and vi then

24:
L ←i + 1 −L

25:
b ←b + c
▷≤ℓ+ 1 quantum-quantum controlled additions

26:
end if

27:
b ←b × r−1
▷≤ℓ+ 1 in-place quantum-quantum multiplications and 1 modular inverse

28: end for

29: return c

71

## Page 72

A
Elementary Symmetric Polynomials

In this section we prove Lemma A.1. Recall that our max-LINSAT objective function takes the
form f(x) = f1(b1 · x) + . . . + fm(bm · x), where fj : Fp →{+1, −1}. Hence f2
j −1 = 0 for all
j. Consequently, the rescaled functions gj(x) = (fj(x) −f)/φ also obey a quadratic identity that
does not depend on j. (Namely, φ2g2
j + 2fφg + f
2 −1 = 0.) Thus the conditions of Lemma A.1
are met by both f1, . . . , fm and g1, . . . , gm.

Lemma A.1. Let P be any degree-ℓpolynomial in a single variable. Let x1, . . . , xm be variables that
each obey a quadratic identity ax2
j +bxj +c = 0, where a, b, c are independent of j and a ̸= 0. Then
P(x1 + . . . + xm) can be expressed as a linear combination of elementary symmetric polynomials:
P(x1 + . . . + xm) = Pℓ
k=0 ukP (k)(x1, . . . , xm).

Proof. Reducing modulo the quadratic identities:

ax2
j + bxj + c = 0
j = 1, . . . , m
(270)

brings P(x1+. . .+xm) into a form where none of x1, . . . , xm is raised to any power greater than one.
We can think of the resulting expression as a multilinear multivariate polynomial P(x1, . . . , xm),
which is of total degree ℓ. Since the coefficients in the m identities described in (270) are independent
of j, this multilinear multinomial is symmetric. That is, for any permutation π ∈Sm we have
P(xπ(1), . . . , xπ(m)) = P(x1, . . . , xm).
By the fundamental theorem of symmetric polynomials,
multilinearity and symmetry together imply that the degree-ℓpolynomial P(x1, . . . , xm) can be
expressed as a linear combination of elementary symmetric polynomials of degree at most ℓ.

B
Gallager’s Ensemble

In [92] Gallager defined the following ensemble of matrices over F2. This ensemble is widely used in
coding theory because when parity check matrices are drawn from Gallager’s ensemble, the resulting
LDPC codes have good parameters with high probability. Together with a choice of v, a matrix B
sampled from Gallager’s ensemble also induces a natural ensemble of D-regular max-k-XORSAT
instances.
Given parameters (k, D, b), a sample from Gallager’s ensemble of matrices B ∈Fbk×bD
2
is gen-
erated as follows. Let A denote the horizontal concatenation of D identity matrices, each b × b,
yielding A = [I1I2 . . . ID]. For i = 1, . . . , k let Mi = APi where P1, . . . , Pk are independent uni-
formly random bD × bD permutation matrices. Concatenate these vertically yielding





M1
M2



BT =

...
Mk


(271)

The matrix BT thus has n = bk rows and m = bD columns, with k ones in each row and D
ones in each column. By choosing each function f1, . . . , fm independently at random to be either
fi(x) = (−1)x or fi(x) = −(−1)x we obtain a D-regular instance of max-k-XORSAT as a special
case of max-LINSAT over F2.

72

## Page 73

Gallager’s (k, D, b) ensemble is not equivalent to sampling uniformly from all bk × bD matrices
with k ones in each row and D ones in each column.
It shares many properties with such a
distribution but is more convenient to sample from.

C
Simulated Annealing Applied to OPI

By the results of §11.1 we expect simulated annealing to yield solutions to the OPI instances of §5
where the fraction ϕmax of constraints satisfied scales like

ϕmax ≃1

2 + c

Dν .
(272)

where c and ν are free parameters of the fit. According to our crude theoretical model ν should
be 1/2. However, extrapolating from our empirical results with sparse instances we would expect
ν to be slightly smaller than 1/2. As shown in Fig. 15, experimental results match well to this
prediction with ν = 0.45. In OPI every variable is contained in every constraint so the degree D is
equal to the number of constraints m.

Figure 15: Here we generate OPI instances over Fp where p takes prime values from 307 to 12, 343.
The number of constraints is m = p −1. For each m we take n ∈{m/2, m/6, m/10}, rounded to
the nearest integer. We find that, independent of n/m, the approximation achieved by simulated
annealing with 10, 000 sweeps fits well to ϕmax = 1/2 + 1.8D−0.45. Note that, in OPI the degree D
equals the number of constraints m, since every variable is contained in every constraint.

References

[1] Luca Trevisan.
Inapproximability of combinatorial optimization problems.
Paradigms
of Combinatorial Optimization:
Problems and New Approaches, pages 381–434, 2014.
arXiv:cs/0409043.

73

## Page 74

[2] Mikl´os Ajtai, Ravi Kumar, and Dandapani Sivakumar. A sieve algorithm for the shortest
lattice vector problem. In Proceedings of the thirty-third annual ACM symposium on Theory
of computing, pages 601–610, 2001.

[3] Dana Moshkovitz. The projection games conjecture and the NP-hardness of ln n-approximating
set-cover. Theory of Computing, 11:221–235, 2015.

[4] Edward Farhi, Jeffrey Goldstone, Sam Gutmann, Joshua Lapan, Andrew Lundgren, and Daniel
Preda.
A quantum adiabatic evolution algorithm applied to random instances of an NP-
complete problem. Science, 292(5516):472–475, 2001.

[5] Edward Farhi, Jeffrey Goldstone, and Sam Gutmann. A quantum approximate optimization
algorithm applied to a bounded occurrence constraint problem. arXiv:1412.6062, 2014.

[6] Matthew B. Hastings. A short path quantum algorithm for exact optimization. Quantum,
2:78, 2018. arXiv:1802.10124.

[7] Joao Basso, Edward Farhi, Kunal Marwaha, Benjamin Villalonga, and Leo Zhou. The quantum
approximate optimization algorithm at high depth for MaxCut on large-girth regular graphs
and the Sherrington-Kirkpatrick model. In Fran¸cois Le Gall and Tomoyuki Morimae, editors,
17th Conference on the Theory of Quantum Computation, Communication and Cryptography
(TQC 2022), volume 232 of Leibniz International Proceedings in Informatics (LIPIcs), pages
7:1–7:21, Dagstuhl, Germany, 2022. Schloss Dagstuhl – Leibniz-Zentrum f¨ur Informatik.

[8] Alexander M. Dalzell, Nicola Pancotti, Earl T. Campbell, and Fernando G.S.L. Brand˜ao. Mind
the gap: achieving a super-Grover quantum speedup by jumping to the end. In Proceedings of
the 55th annual ACM Symposium on Theory of Computing (STOC), pages 1131–1144, 2023.
2212.01513.

[9] Eliot Kapit, Brandon A. Barton, Sean Feeney, George Grattan, Pratik Patnaik, Jacob Sagal,
Lincoln D. Carr, and Vadim Oganesyan. On the approximability of random-hypergraph MAX-
3-XORSAT problems with quantum algorithms. arXiv:2312.06104, 2023.

[10] R. Shaydulin, C. Li, S. Chakrabarti, M. DeCross, D. Herman, N. Kumar, J. Larson, D. Lykov,
P. Minssen, Y. Sun, Y. Alexeev, J. M. Dreiling, J. P. Gaebler, T. M. Gatterman, J. A. Gerber,
K. Gilmore, D. Gresh, N. Hewitt, C. V. Horst, S. Hu, J. Johansen, M. Matheny, T. Mengle,
M. Mills, S. A. Moses, B. Neyenhuis, P. Siegfried, R. Yalovetzky, and M. Pistoia. Evidence
of scaling advantage for the quantum approximate optimization algorithm on a classically
intractable problem. Science Advances, 10(22):eadm6761, 2024.

[11] Edward Farhi, Sam Gutmann, Daniel Ranard, and Benjamin Villalonga. Lower bounding the
MaxCut of high girth 3-regular graphs using the QAOA. arXiv:2503.12789, 2025.

[12] Jiaqi Leng, Yufan Zheng, and Xiaodi Wu. A quantum-classical performance separation in
nonconvex optimization. arXiv:2311.00811, 2023.

[13] Yilei Chen, Qipeng Liu, and Mark Zhandry. Quantum algorithms for variants of average-case
lattice problems via filtering. In Annual international conference on the theory and applications
of cryptographic techniques (EUROCRYPT), pages 372–401. Springer, 2022.

74

## Page 75

[14] Niklas Pirnay, Vincent Ulitzsh, Frederik Wilde, Jens Eisert, and Jean-Pierre Seifert. An in-
principle super-polynomial quantum advantage for approximating combinatorial optimization
problems via computational learning theory. Science Advances, 10:eadj5170, 2024.

[15] Mario Szegedy.
Quantum advantage for combinatorial optimization problems, simplified.
arXiv:2212.12572, 2022.

[16] Andr´as Gily´en, Matthew B Hastings, and Umesh Vazirani. (Sub)exponential advantage of
adiabatic quantum computation with no sign problem. In Proceedings of the 53rd Annual
ACM SIGACT Symposium on Theory of Computing, pages 1357–1369, 2021.

[17] Lior Eldar and Sean Hallgren. An efficient quantum algorithm for lattice problems achieving
subexponential approximation factor. arXiv:2201.13450, 2022.

[18] Vasil S. Denchev, Sergio Boixo, Sergei V. Isakov, Nan Ding, Ryan Babbush, Vadim Smelyan-
skiy, John Martinis, and Hartmut Neven. What is the computational value of finite-range
tunneling? Physical Review X, 6(3):031015, 2016.

[19] Andreas Bartschi and Stephan Eidenbenz. Short-depth circuits for Dicke state preparation. In
2022 IEEE International Conference on Quantum Computing and Engineering (QCE). IEEE,
2022. arXiv:2207.09998.

[20] Hanyu Wang, Bochen Tan, Jason Cong, and Giovanni De Micheli. Quantum state preparation
using an exact CNOT synthesis formulation. arXiv:2401.01009, 2024.

[21] Michael A. Nielsen and Isaac L. Chuang. Quantum Computation and Quantum Information.
Cambridge University Press, 2010.

[22] Elwyn Berlekamp, Robert McEliece, and Henk Van Tilborg. On the inherent intractability of
certain coding problems. IEEE Transactions on Information theory, 24(3):384–386, 1978.

[23] Elwyn R. Berlekamp. Algebraic coding theory (revised edition). World Scientific, 2015.

[24] Moni Naor and Benny Pinkas. Oblivious transfer and polynomial evaluation. In Proceedings
of the thirty-first annual ACM Symposium On Theory of Computing (STOC), pages 245–254,
1999.

[25] Daniel Bleichenbacher and Phong Q. Nguyen. Noisy polynomial interpolation and noisy Chi-
nese remaindering. In International Conference on the Theory and Applications of Crypto-
graphic Techniques, pages 53–69. Springer, 2000.

[26] Oscar Garcia-Morchon, Ronald Rietman, Igor E. Shparlinski, and Ludo Tolhuizen. Interpola-
tion and approximation of polynomials in finite fields over a short interval from noisy values.
Experimental Mathematics, 23(3):241–260, 2014.

[27] Igor Shparlinski and Arne Winterhof. Noisy interpolation of sparse polynomials in finite fields.
Applicable Algebra in Engineering, Communication and Computing, 16:307–317, 2005.

[28] Igor E. Shparlinski. Playing “hide-and-seek” with numbers. Public-Key Cryptography: Amer-
ican Mathematical Society Short Course, January 13-14, 2003, Baltimore, Maryland, 62:153,
2005.

75

## Page 76

[29] Moni Naor and Benny Pinkas. Oblivious polynomial evaluation. SIAM Journal on Computing,
35(5):1254–1281, 2006.

[30] Venkatesan Guruswami and Alexander Vardy. Maximum-likelihood decoding of Reed-Solomon
codes is NP-hard. IEEE Transactions on Information Theory, 51(7):2249–2256, 2005.

[31] Venkata Gandikota, Badih Ghazi, and Elena Grigorescu. NP-hardness of Reed-Solomon decod-
ing, and the Prouhet-Tarry-Escott problem. SIAM Journal on Computing, 47(4):1547–1584,
2018.

[32] Qi Cheng and Daqing Wan. On the list and bounded distance decodability of Reed-Solomon
codes. SIAM Journal on Computing, 37(1):195–209, 2007.

[33] Qi Cheng and Daqing Wan. Complexity of decoding positive-rate Reed-Solomon codes. In In-
ternational Colloquium on Automata, Languages, and Programming, pages 283–293. Springer,
2008.

[34] Matthew P. Harrigan, Tanuj Khattar, Charles Yuan, Anurudh Peduri, Noureldin Yosri,
Fionn D. Malone, Ryan Babbush, and Nicholas C. Rubin. Expressing and analyzing quantum
algorithms with qualtran. arXiv:2409.04643, 2024.

[35] Robert Gallager. Low-density parity-check codes. IRE Transactions on Information Theory,
8(1):21–28, 1962.

[36] Thomas J. Richardson and R¨udiger L. Urbanke. The capacity of low-density parity-check codes
under message-passing decoding. IEEE Transactions on Information Theory, 47(2):599–618,
2001.

[37] Mark M´ezard and Andrea Montanari. Information, Physics, and Computation. Oxford Uni-
versity Press, 2009.

[38] Dorit Aharonov and Amnon Ta-Shma. Adiabatic quantum state generation and statistical
zero knowledge. In Proceedings of the 35th Annual ACM Symposium on Theory of Computing
(STOC), pages 20–29, 2003. arXiv:quant-ph/0301023.

[39] Oded Regev.
Quantum computation and lattice problems.
SIAM Journal on Computing,
33(3):738–760, 2004.

[40] Dorit Aharonov and Oded Regev. Lattice problems in NP ∩coNP. Journal of the ACM
(JACM), 52(5):749–765, 2005.

[41] Oded Regev. On lattices, learning with errors, random linear codes, and cryptography. Journal
of the ACM (JACM), 56(6):1–40, 2009.

[42] Andr´e Chailloux and Jean-Pierre Tillich. The quantum decoding problem. In 19th Conference
on the Theory of Quantum Computation, Communication and Cryptography (TQC 2024),
pages 6–1. Schloss Dagstuhl–Leibniz-Zentrum f¨ur Informatik, 2024. arXiv:2310.20651.

[43] Thomas Debris-Alazard, Maxime Remaud, and Jean-Pierre Tillich. Quantum reduction of
finding short code vectors to the decoding problem. IEEE Transactions on Information Theory,
2023.

76

## Page 77

[44] Takashi Yamakawa and Mark Zhandry. Verifiable quantum advantage without structure. In
2022 IEEE 63rd Annual Symposium on Foundations of Computer Science (FOCS), pages 69–
74. IEEE, 2022.

[45] Nai-Hui Chia, Andr´as Pal Gily´en, Tongyang Li, Han-Hsuan Lin, Ewin Tang, and Chunhao
Wang. Sampling-based sublinear low-rank matrix arithmetic framework for dequantizing quan-
tum machine learning. Journal of the ACM, 69(5):1–72, 2022.

[46] Lance Fortnow.
The role of relativization in complexity theory.
Bulletin of the EATCS,
52:229–243, 1994.

[47] Ruud Pellikaan and Xin-Wen Wu. List decoding of q-ary Reed-Muller codes. IEEE Transac-
tions on Information Theory, 50(4):679–682, 2004.

[48] Jon Feldman, Martin J. Wainwright, and David R. Karger.
Using linear programming to
decode binary linear codes. IEEE Transactions on Information Theory, 51(3):954–972, 2005.

[49] Jon Feldman, Tal Malkin, Rocco A. Servedio, Cliff Stein, and Martin J. Wainwright.
LP
decoding corrects a constant fraction of errors. IEEE Transactions on Information Theory,
53(1):82–89, 2007.

[50] Constantinos Daskalakis, Alexandros G. Dimakis, Richard M. Karp, and Martin J. Wainwright.
Probabilistic analysis of linear programming decoding. IEEE Transactions on Information
Theory, 54(8):3565–3578, 2008.

[51] Mohammad H. Taghavi and Paul H. Siegel. Adaptive methods for linear programming decod-
ing. IEEE Transactions on Information Theory, 54(12):5396–5410, 2008.

[52] Alex Yufit, Asi Lifshitz, and Yair Be’ery. Efficient linear programming decoding of HDPC
codes. IEEE Transactions on Communications, 59(3):758–766, 2010.

[53] Akin Tanatmis, Stefan Ruzika, Horst W. Hamacher, Mayur Punekar, Frank Kienle, and Nor-
bert Wehn. Valid inequalities for binary linear codes. In 2009 IEEE International Symposium
on Information Theory (ISIT), pages 2216–2220. IEEE, 2009.

[54] Akin Tanatmis, Stefan Ruzika, Horst W. Hamacher, Mayur Punekar, Frank Kienle, and Nor-
bert Wehn. A separation algorithm for improved LP decoding of linear block codes. IEEE
Transactions on Information Theory, 56(7):3277–3289, 2010.

[55] Christophe Piveteau and Joseph M. Renes. Quantum message-passing algorithm for optimal
and efficient decoding. Quantum, 6:784, 2022.

[56] Alistair Sinclair and Mark Jerrum. Approximate counting, uniform generation and rapidly
mixing Markov chains. Information and Computation, 82(1):93–133, 1989.

[57] Johan H˚astad. On bounded occurrence constraint satisfaction. Information Processing Letters,
74(1-2):1–6, 2000.

77

## Page 78

[58] Boaz Barak, Ankur Moitra, Ryan O’Donnell, Prasad Raghavendra, Oded Regev, David
Steurer, Luca Trevisan, Aravindan Vijayaraghavan, David Witmer, and John Wright. Beat-
ing the random assignment on constraint satisfaction problems of bounded degree. In Ap-
proximation, Randomization, and Combinatorial Optimization. Algorithms and Techniques
(APPROX/RANDOM 2015), volume 40 of Leibniz International Proceedings in Informatics
(LIPIcs), pages 110–123, 2015. arXiv:1505.03424.

[59] Alexander Schmidhuber, Ryan O’Donnell, Robin Kothari, and Ryan Babbush. Quartic quan-
tum speedups for planted inference. Physical Review X, 15(2):021077, 2025. arXiv:2406.19378.

[60] Eugene Prange. The use of information sets in decoding cyclic codes. In IRE Transactions on
Information Theory, volume 8, pages 5–9, 1962.

[61] Andr´e Chailloux and Jean-Pierre Tillich.
Quantum advantage from soft decoders.
arXiv:2411.12553, 2024.

[62] Natchapol Patamawisut, Naphan Benchasattabuse, Michal Hajduˇsek, and Rodney Van Meter.
Quantum circuit design for decoded quantum interferometry. arXiv:2504.18334, 2025.

[63] Guang Hao Low, Vadym Kliuchnikov, and Luke Schaeffer. Trading T-gates for dirty qubits in
state preparation and unitary synthesis. Quantum, 8:1375, 2024. arXiv:1812.00954.

[64] Alexander M. Barg and Dmitry Yu. Nogin. Spectral approach to linear programming bounds
on codes. Problems of Information Transmission, 42(2):77–89, 2006.

[65] Kunal Marwaha and Stuart Hadfield. Bounds on approximating Max-k-XOR with quantum
and classical local algorithms. Quantum, 6:757, 2022.

[66] Edward Farhi, Jeffrey Goldstone, and Sam Gutmann. A quantum approximate optimization
algorithm. arXiv:1411.4028, 2014.

[67] Joao Basso, Edward Farhi, Kunal Marwaha, Benjamin Villalonga, and Leo Zhou. Performance
of the QAOA on MaxCut over large-girth regular graphs. github.com/benjaminvillalonga/
large-girth-maxcut-qaoa/blob/main/data.csv, 2022.

[68] Sami Boulebnane, Abid Khan, Minzhao Liu, Jeffrey Larson, Dylan Herman, Ruslan Shaydulin,
and Marco Pistoia. Evidence that the quantum approximate optimization algorithm optimizes
the Sherrington-Kirkpatrick model efficiently in the average case. arXiv:2505.07929, 2025.

[69] Venkatesan Guruswami and Madhu Sudan. Improved decoding of Reed-Solomon and algebraic-
geometric codes. In Proceedings 39th Annual Symposium on Foundations of Computer Science
(FOCS), pages 28–37. IEEE, 1998.

[70] Arjen K. Lenstra, Hendrik Willem Lenstra, and L´aszl´o Lov´asz. Factoring polynomials with
rational coefficients. Mathematische Annalen, 261:515–534, 1982.

[71] Claus-Peter Schnorr. A hierarchy of polynomial time lattice basis reduction algorithms. The-
oretical Computer Science, 53(2-3):201–224, 1987.

[72] Claus-Peter Schnorr and Martin Euchner. Lattice basis reduction: Improved practical algo-
rithms and solving subset sum problems. Mathematical Programming, 66:181–199, 1994.

78

## Page 79

[73] Thomas J. Richardson, Mohammad Amin Shokrollahi, and R¨udiger L. Urbanke. Design of
capacity-approaching irregular low-density parity-check codes. IEEE Transactions on Infor-
mation Theory, 47(2):619–637, 2001.

[74] Chris Calabro. The exponential complexity of satisfiability problems. Phd thesis, University of
California, San Diego, 2009. cseweb.ucsd.edu/~ccalabro/thesis.pdf.

[75] Laurent Decreusefond and Gilles Z´emor. On the error-correcting capabilities of cycle codes of
graphs. Combinatorics, Probability and Computing, 6(1):27–38, 1997.

[76] Jack Edmonds and Ellis L. Johnson. Matching, Euler tours and the Chinese postman. Math-
ematical programming, 5:88–124, 1973.

[77] Emmanuel Abbe, Amir Shpilka, and Min Ye. Reed–Muller codes: Theory and algorithms.
IEEE Transactions on Information Theory, 67(6):3251–3277, 2020.

[78] Philippe Delsarte, Jean-Marie Goethals, and F. J. MacWilliams. On generalized Reed-Muller
codes and their relatives. Information and Control, 16(5):403–442, 1970.

[79] Tadao Kasami, Shu Lin, and W. Peterson. New generalizations of the Reed-Muller codes–I:
Primitive codes. IEEE Transactions on information theory, 14(2):189–199, 1968.

[80] Venkatesan Guruswami, Atri Rudra, and Madhu Sudan.
Essential Coding Theory.
cse.
buffalo.edu/faculty/atri/courses/coding-theory/book/, 2023.

[81] Yevgeniy Dodis, Rafail Ostrovsky, Leonid Reyzin, and Adam Smith. Fuzzy extractors: How
to generate strong keys from biometrics and other noisy data. SIAM journal on computing,
38(1):97–139, 2008.

[82] Cl´emence Chevignard, Pierre-Alain Fouque, and Andr´e Schrottenloher. Reducing the number
of qubits in quantum information set decoding. In International Conference on the Theory
and Application of Cryptology and Information Security, pages 299–329. Springer, 2024.

[83] Dmytro Fedoriaka. New circuit for quantum adder by constant. arXiv:2501.07060, 2025.

[84] Thomas H¨aner, Samuel Jaques, Michael Naehrig, Martin Roetteler, and Mathias Soeken. Im-
proved quantum circuits for elliptic curve discrete logarithms. In Post-Quantum Cryptography,
pages 425–444. Springer, 2020. arXiv:2001.09580.

[85] Craig Gidney. Halving the cost of quantum addition. Quantum, 2:74, June 2018.

[86] Alessandro
Luongo,
Antonio
Michele
Miti,
Varun
Narasimhachar,
and
Adithya
Sireesh.
Measurement-based uncomputation of quantum circuits for modular arithmetic.
arXiv:2407.20167, 2024.

[87] Craig Gidney and Martin Eker˚a. How to factor 2048 bit RSA integers in 8 hours using 20
million noisy qubits. Quantum, 5:433, April 2021.

[88] Daniel Litinski. How to compute a 256-bit elliptic curve private key with only 50 million Toffoli
gates. arXiv:2306.08585, 2023.

79

## Page 80

[89] Ryan Babbush, Jarrod R. McClean, Michael Newman, Craig Gidney, Sergio Boixo, and Hart-
mut Neven. Focus beyond quadratic speedups for error-corrected quantum advantage. PRX
quantum, 2(1):010103, 2021.

[90] Earl Campbell, Ankur Khurana, and Ashley Montanaro. Applying quantum algorithms to
constraint satisfaction problems. Quantum, 3:167, 2019.

[91] Daniel J. Bernstein, Tung Chou, Tanja Lange, Ingo von Maurich, Rafael Misoczki, Ruben
Niederhagen, Eduardo Persichetti, Christiane Peters, Peter Schwabe, Nicolas Sendrier, et al.
Classic McEliece: conservative code-based cryptography. NIST submissions, 1(1):1–25, 2017.

[92] Robert G. Gallager. Low-Density Parity-Check Codes. MIT Press, 1963.

80
