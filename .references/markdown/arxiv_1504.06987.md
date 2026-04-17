---
source_pdf: ../arxiv_1504.06987.pdf
pages: 28
extracted_at: 2026-04-17T12:32:29+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_1504.06987

Source PDF: ../arxiv_1504.06987.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Quantum speedup of Monte Carlo methods

Ashley Montanaro∗

July 12, 2017

arXiv:1504.06987v3 [quant-ph] 11 Jul 2017

Abstract

Monte Carlo methods use random sampling to estimate numerical quantities which are hard
to compute deterministically. One important example is the use in statistical physics of rapidly
mixing Markov chains to approximately compute partition functions. In this work we describe
a quantum algorithm which can accelerate Monte Carlo methods in a very general setting. The
algorithm estimates the expected output value of an arbitrary randomised or quantum subrou-
tine with bounded variance, achieving a near-quadratic speedup over the best possible classical
algorithm. Combining the algorithm with the use of quantum walks gives a quantum speedup of
the fastest known classical algorithms with rigorous performance bounds for computing partition
functions, which use multiple-stage Markov chain Monte Carlo techniques. The quantum algo-
rithm can also be used to estimate the total variation distance between probability distributions
eﬃciently.

1
Introduction

Monte Carlo methods are now ubiquitous throughout science, in ﬁelds as diverse as statistical
physics [37], microelectronics [30] and mathematical ﬁnance [23]. These methods use randomness
to estimate numerical properties of systems which are too large or complicated to analyse deter-
ministically. In general, the basic core of Monte Carlo methods involves estimating the expected
output value µ of a randomised algorithm A. The natural algorithm for doing so is to produce k
samples, each corresponding to the output of an independent execution of A, and then to output
the average eµ of the samples as an approximation of µ. Assuming that the variance of the random
variable corresponding to the output of A is at most σ2, the probability that the value output by
this estimator is far from the truth can be bounded using Chebyshev’s inequality:

Pr[|eµ −µ| ≥ϵ] ≤σ2

kϵ2 .

It is therefore suﬃcient to take k = O(σ2/ϵ2) to estimate µ up to additive error ϵ with, say, 99%
success probability.
This simple result is a key component in many more complex randomised
approximation schemes (see e.g. [50, 37]).

Although this algorithm is fairly eﬃcient, its quadratic dependence on σ/ϵ seems far from ideal:
for example, if σ = 1, to estimate µ up to 4 decimal places we would need to run A over 100 million
times. Unfortunately, it can be shown that, without any further information about A, the sample
complexity of this algorithm is asymptotically optimal [15] with respect to its scaling with σ and
ϵ, although it can be improved by a constant factor [29].

∗Department of Computer Science, University of Bristol, UK; ashley.montanaro@bristol.ac.uk.

1

## Page 2

We show here that, using a quantum computer, the number of uses of A required to approximate
µ can be reduced almost quadratically beyond the above classical bound.
Assuming that the
variance of the output of the algorithm A is at most σ2, we present a quantum algorithm which
estimates µ up to additive error ϵ, with 99% success probability, using A only eO(σ/ϵ) times1. It
follows from known lower bounds on the quantum complexity of approximating the mean [45] that
the runtime of this algorithm is optimal, up to polylogarithmic factors. This result holds for an
arbitrary algorithm A used as a black box, given only an upper bound on the variance.

An important aspect of this construction is that the underlying subroutine A need not be a
classical randomised procedure, but can itself be a quantum algorithm. This enables any quantum
speedup obtained by A to be utilised within the overall framework of the algorithm. A particu-
lar case in which this is useful is quantum speedup of Markov chain Monte Carlo methods [38].
Classically, such methods use a rapidly mixing Markov chain to approximately sample from a
probability distribution corresponding to the stationary distribution of the chain. Quantum walks
are the quantum analogue of random walks (see e.g. [57] for a review). In some cases, quantum
walks can reduce the mixing time quadratically (see e.g. [3, 58]), although it is not known whether
this can be achieved in general [48, 6, 18]. We demonstrate that this known quadratic reduction
can be combined with our algorithm to speed up the fastest known general-purpose classical algo-
rithm with rigorous performance bounds [50] for approximately computing partition functions up
to small relative error, a fundamental problem in statistical physics [37]. As another example of
how our algorithm can be applied, we substantially improve the runtime of a quantum algorithm
for estimating the total variation distance between two probability distributions [13].

1.1
Prior work

The topic of quantum estimation of mean output values of algorithms with bounded variance con-
nects to several previously-explored directions. First, it generalises the problem of approximating
the mean, with respect to the uniform distribution, of an arbitrary bounded function. This has
been addressed by a number of authors. The ﬁrst asymptotically optimal quantum algorithm for
this problem, which uses O(1/ϵ) queries to achieve additive error ϵ, seems to have been given by
Heinrich [27]; an elegant alternative optimal algorithm was later presented by Brassard et al. [11].
Previous algorithms, which are optimal up to lower-order terms, were described by Grover [25],
Aharonov [2] and Abrams and Williams [1]. Using similar techniques to Brassard et al., Wocjan et
al. [59] described an eﬃcient algorithm for estimating the expected value of an arbitrary bounded
observable. It is not diﬃcult to combine these ideas to approximate the mean of arbitrary bounded
functions with respect to nonuniform distributions (see Section 2.1).

One of the main technical ingredients in the present paper is based on an algorithm of Heinrich
for approximating the mean, with respect to the uniform distribution, of functions with bounded
L2 norm [27].
Section 2.2 describes a generalisation of this result to nonuniform distributions,
using similar techniques. This is roughly analogous to the way that amplitude ampliﬁcation [12]
generalises Grover’s quantum search algorithm [24].

The related problem of quantum estimation of expectation values of observables, an important
task in the simulation of quantum systems, has been studied by Knill, Ortiz and Somma [36]. These
authors give an algorithm for estimating tr(Aρ) for observables A such that one can eﬃciently
implement the operator e−iAt. The algorithm is eﬃcient (i.e. achieves runtimes close to O(1/ϵ))
when the tails of the distribution tr(Aρ) decay quickly. However, in the case where one only knows

1The eO notation hides polylogarithmic factors.

2

## Page 3

Table 1: Summary of the main quantum algorithms presented in this paper for estimating the mean
output value µ of an algorithm A. (Algorithm 2, omitted, is a subroutine used in Algorithm 3.)

an upper bound on the variance of this distribution, the algorithm does not achieve a better runtime
than classical sampling. Yet another related problem, that of exact Monte Carlo sampling from a
desired probability distribution, was addressed by Destainville, Georgeot and Giraud [17]. Their
quantum algorithm, which uses Grover’s algorithm as a subroutine, achieves roughly a quadratic
speedup over classical exact sampling. This algorithm’s applicability is limited by the fact that its
runtime scaling can be as slow as O(
√

N), where N is the number of states of the system; we often
think of N as being exponential in the input size.

Quantum algorithms have been used previously to approximate classical partition functions and
solve related problems. In particular, a number of authors [40, 39, 4, 56, 21, 7, 22, 16, 43] have
considered the complexity of computing Ising and Potts model partition functions. These works
in some cases achieve exponential quantum speedups over the best known classical algorithms.
Unfortunately, they in general either produce an approximation accurate up to a speciﬁed additive
error bound, or only work for speciﬁc classes of partition function problems with restrictions on
interaction strengths and topologies, or both. Here we aim to approximate partition functions up
to small relative error in a rather general setting.

Using related techniques to the present work, Somma et al. [49] used quantum walks to accelerate
classical simulated annealing processes, and quantum estimation of partition functions up to small
relative error was addressed by Wocjan et al. [59]. Their algorithm, which is based on the use of
quantum walks and amplitude estimation, achieves a quadratic speedup over classical algorithms
with respect to both mixing time and accuracy. However, it cannot be directly applied to accelerate
the most eﬃcient classical algorithms for approximating partition function problems, which use
so-called Chebyshev cooling schedules (discussed in Section 3). This is essentially because these
algorithms are based around estimating the mean of random variables given only a bound on the
variance. This was highlighted as an open problem in [59], which we resolve here.

Several recent works have developed quantum algorithms for the quantum generalisation of
sampling from a Gibbs distribution: producing a Gibbs state ρ ∝e−βH for some quantum Hamil-
tonian H [53, 47, 52, 60]. Given such a state, one can measure a suitable observable to compute
some quantity of interest about H. Supplied with an upper bound on the variance of such an ob-
servable, the procedure detailed here can be used (as for any other quantum algorithm) to reduce
the number of repetitions required to estimate the observable to a desired accuracy.

1.2
Techniques

We now give an informal description of our algorithms, which are summarised in Table 1 (for
technical details and proofs, see Section 2). For any randomised or quantum algorithm A, we write
v(A) for the random variable corresponding to the value computed by A, with the expected value of
v(A) denoted E[v(A)]. For concreteness, we think of A as a quantum algorithm which operates on
n qubits, each initially in the state |0⟩, and whose quantum part ﬁnishes with a measurement of k

3

## Page 4

of the qubits in the computational basis. Given that the measurement returns outcome x ∈{0, 1}k,
the ﬁnal output is then φ(x), for some ﬁxed function φ : {0, 1}k →R. If A is a classical randomised
algorithm, or a quantum circuit using (for example) mixed states and intermediate measurements,
a corresponding unitary quantum circuit of this form can be produced using standard reversible-
computation techniques [5]. As is common in works based on quantum amplitude ampliﬁcation
and estimation [12], we also assume that we have the ability to execute the algorithm A−1, which
is the inverse of the unitary part of A. If we do have a description of A as a quantum circuit, this
can be achieved simply by running the circuit backwards, replacing each gate with its inverse.

We ﬁrst deal with the special case where the output of A is bounded between 0 and 1. Here a
quantum algorithm for approximating µ := E[v(A)] quadratically faster than is possible classically
can be found by combining ideas from previously known algorithms [27, 11, 59].
We append
an additional qubit and deﬁne a unitary operator W on k + 1 qubits which performs the map
|x⟩|0⟩7→|x⟩(
p

1 −φ(x)|0⟩+
p

φ(x)|1⟩). If the ﬁnal measurement of the algorithm A is replaced
with performing W, then measuring the added qubit, the probability that we receive the answer
1 is precisely µ. Using quantum amplitude estimation [12] the probability that this measurement
returns 1 can be estimated to higher accuracy than is possible classically. Using t iterations of
amplitude estimation, we can output an estimate eµ such that |eµ −µ| = O(√µ/t + 1/t2) with high
probability [12]. In particular, O(1/ϵ) iterations of amplitude estimation are suﬃcient to produce
an estimate eµ such that |eµ −µ| ≤ϵ with, say, 99% probability.

The next step is to use the above algorithm as a subroutine in a more general procedure
that can deal with algorithms A whose output is non-negative, has bounded ℓ2 norm, but is not
necessarily bounded between 0 and 1. That is, algorithms for which we can control the expression
∥v(A)∥2 :=
p

E[v(A)2]. The procedure for this case generalises, and is based on the same ideas as,
a previously known result for the uniform distribution [27].

The idea is to split the output of A up into disjoint intervals depending on size. Write Ap,q
for the “truncated” algorithm which outputs v(A) if p ≤v(A) < q, and otherwise outputs 0. We
estimate µ by applying the above algorithm to estimate E[v(Ap,q)] for a sequence of O(log 1/ϵ)
intervals which are exponentially increasing in size, and summing the results. As the intervals [p, q)
get larger, the accuracy with which we approximate E[v(Ap,q)] decreases, and values v(A) larger
than about 1/ϵ are ignored completely. However, the overall upper bound on ∥v(A)∥2 allows us to
infer that these larger values do not aﬀect the overall expectation µ much; indeed, if µ depended
signiﬁcantly on large values in the output, the ℓ2 norm of v(A) would be high.

The ﬁnal result is that for ∥v(A)∥2 = O(1), given appropriate parameter choices, the estimate
eµ satisﬁes |eµ −µ| = O(ϵ) with high probability, and the algorithm uses A eO(1/ϵ) times in total.
This scaling is a near-quadratic improvement over the best possible classical algorithm.

We next consider the more general case of algorithms A which have bounded variance, but whose
output need not be non-negative, nor bounded in ℓ2 norm. To apply the previous algorithm, we
would like to transform the output of A to make its ℓ2 norm low. If v(A) has mean µ and variance
upper-bounded by σ2, a suitable way to achieve this is to subtract µ from the output of A, then
divide by σ. The new algorithm’s output would have ℓ2 norm upper-bounded by 1, and estimating
its expected value up to additive error ϵ/σ would give us an estimate of µ up to ϵ. Unfortunately,
we of course do not know µ initially, so cannot immediately implement this idea. To approximately
implement it, we ﬁrst run A once and use the output em as a proxy for µ. Because Var(v(A)) ≤σ2,
em is quite likely to be within distance O(σ) of µ. Therefore, the algorithm B produced from A by
subtracting em and dividing by σ is quite likely to have ℓ2 norm upper-bounded by a constant. We
can thus eﬃciently estimate the positive and negative parts of E[v(B)] separately, then combine

4

## Page 5

and rescale them. The overall algorithm achieves accuracy ϵ in time eO(σ/ϵ).

A similar idea can be used to approximate the expected output value of algorithms for which
we have a bound on the relative variance, namely that Var(v(A)) = O(µ2). In this setting it turns
out that eO(1/ϵ) uses of A suﬃce to produce an estimate eµ accurate up to relative error ϵ, i.e. for
which |eµ −µ| ≤ϵµ. This is again a near-quadratic improvement over the best possible classical
algorithm.

1.3
Approximating partition functions

In this section we discuss (with details in Section 3) how these algorithms can be applied to the
problem of approximating partition functions. Consider a (classical) physical system which has
state space Ω, together with a Hamiltonian H : Ω→R specifying the energy of each conﬁguration2

x ∈Ω. Here we will assume that H takes integer values in the set {0, . . . , n}. A central problem is
to compute the partition function
Z(β) =
X

x∈Ω
e−β H(x)

for some inverse temperature β deﬁned by β = 1/(kBT), where T is the temperature and kB is
Boltzmann’s constant. As well as naturally encapsulating various models in statistical physics, such
as the Ising and Potts models, this framework also encompasses well-studied problems in computer
science, such as counting the number of valid k-colourings of a graph. In particular, Z(∞) counts
the number of conﬁgurations x such that H(x) = 0. It is often hard to compute Z(β) for large
β but easy to approximate Z(β) ≈|Ω| for β ≈0. In many cases, such as the Ising model, it is
known that computing Z(∞) exactly falls into the #P-complete complexity class [34], and hence
is unlikely to admit an eﬃcient quantum or classical algorithm.

Here our goal will be to approximate Z(β) up to relative error ϵ, for some small ϵ. That is, to
output eZ such that | eZ −Z(β)| ≤ϵ Z(β), with high probability. For simplicity, we will focus on
β = ∞in the following discussion, but it is easy to see how to generalise to arbitrary β.

Let 0 = β0 < β1 < · · · < βℓ= ∞be a sequence of inverse temperatures. A standard classical
approach to design algorithms for approximating partition functions [55, 19, 10, 50, 59] is based
around expressing Z(βℓ) as the telescoping product

Z(βℓ) = Z(β0)Z(β1)

Z(β0)
Z(β2)
Z(β1) . . . Z(βℓ)

Z(βℓ−1).

If we can compute Z(β0) = |Ω|, and can also approximate each of the ratios αi := Z(βi+1)/Z(βi)
accurately, taking the product will give a good approximation to Z(βℓ). Let πi denote the Gibbs
(or Boltzmann) probability distribution corresponding to inverse temperature βi, where

πi(x) =
1
Z(βi)e−βiH(x).

To approximate αi we deﬁne the random variable

Yi(x) = e−(βi+1−βi)H(x).

Then one can readily compute that Eπi[Yi] = αi, so sampling from each distribution πi allows us
to estimate the quantities αi. It will be possible to estimate αi up to small relative error eﬃciently

2We use x to label conﬁgurations rather than the more standard σ to avoid confusion with the variance.

5

## Page 6

if the ratio E[Y 2
i ]/E[Yi]2 is low. This motivates the concept of a Chebyshev cooling schedule [50]:
a sequence of inverse temperatures βi such that E[Y 2
i ]/E[Yi]2 = O(1) for all i. It is known that,
for any partition function problem as deﬁned above such that |Ω| = A, there exists a Chebyshev
cooling schedule with ℓ= eO(√log A) [50].

It is suﬃcient to approximate E[Yi] up to relative error O(ϵ/ℓ) for each i to get an overall
approximation accurate up to relative error ϵ. To achieve this, the quantum algorithm presented
here needs to use at most eO(ℓ/ϵ) samples from Yi. Given a Chebyshev cooling schedule with ℓ=
eO(√log A), the algorithm thus uses eO((log A)/ϵ) samples in total, a near-quadratic improvement
in terms of ϵ over the complexity of the fastest known classical algorithm [50].

In general, we cannot exactly sample from the distributions πi. Classically, one way of approx-
imately sampling from these distributions is to use a Markov chain which mixes rapidly and has
stationary distribution πi. For a reversible, ergodic Markov chain, the time required to produce
such a sample is controlled by the relaxation time τ := 1/(1 −|λ1|) of the chain, where λ1 is the
second largest eigenvalue in absolute value [38]. In particular, sampling from a distribution close
to πi in total variation distance requires Ω(τ) steps of the chain.

It has been known for some time that quantum walks can sometimes mix quadratically faster [3].
One case where eﬃcient mixing can be obtained is for sequences of Markov chains whose stationary
distributions π are close [58]. Further, for this special case one can approximately produce coherent
“quantum sample” states |π⟩= P
x∈Ω
p

π(x)|x⟩eﬃciently. Here we can show (Section 3.2) that the
Chebyshev cooling schedule condition implies that each distribution in the sequence π1, . . . , πℓ−1
is close enough to its predecessor that we can use techniques of [58] to approximately produce any
state |πi⟩using eO(ℓ√τ) quantum walk steps each. Using similar ideas we can approximately reﬂect
about |πi⟩using only eO(√τ) quantum walk steps.

Approximating E[Yi] up to relative error O(ϵ/ℓ) using our algorithm requires one quantum sam-
ple approximating |πi⟩, and eO(ℓ/ϵ) approximate reﬂections about |πi⟩. Therefore, the total number
of quantum walk steps required for each i is eO(ℓ√τ/ϵ). Summing over i, we get a quantum algo-
rithm for approximating an arbitrary partition function up to relative error ϵ using eO((log A)√τ/ϵ)
quantum walk steps. The fastest known classical algorithm [50] exhibits quadratically worse de-
pendence on both τ and ϵ.

In the above discussion, we have neglected the complexity of computing the Chebyshev cool-
ing schedule itself.
An eﬃcient classical algorithm for this task is known [50], which runs in
time eO((log A)τ).
Adding the complexity of this part, we ﬁnish with an overall complexity of
eO((log A)√τ(√τ + 1/ϵ)). We leave the interesting question open of whether there exists a more
eﬃcient quantum algorithm for ﬁnding a Chebyshev cooling schedule.

1.4
Applications

We now sketch several representative settings (for details, see Section 3.4) in which our algorithm
for approximating partition functions gives a quantum speedup.

• The ferromagnetic Ising model above the critical temperature. This well-studied statis-
tical physics model is deﬁned in terms of a graph G = (V, E) by the Hamiltonian H(z) =
−P
(u,v)∈E zuzv, where |V | = n and z ∈{±1}n. The Markov chain known as the Glauber
dynamics is known to mix rapidly above a certain critical temperature and to have as its
stationary distribution the Gibbs distribution. For example, for any graph with maximum
degree O(1), the mixing time of the Glauber dynamics for suﬃciently low inverse temperature
β is O(n log n) [44]. In this case, as A = 2n, the quantum algorithm approximates Z(β) to

6

## Page 7

within relative error ϵ in eO(n3/2/ϵ + n2) steps. The corresponding classical algorithm [50]
uses eO(n2/ϵ2) steps.

• Counting colourings. Here we are given a graph G with n vertices and maximum degree
d. We seek to approximately count the number of valid k-colourings of G, where a colouring
of the vertices is valid if all pairs of neighbouring vertices are assigned diﬀerent colours. In
the case where k > 2d, the use of a rapidly mixing Markov chain gives a quantum algorithm
approximating the number of colourings of G up to relative error ϵ in time eO(n3/2/ϵ + n2),
as compared with the classical eO(n2/ϵ2) [50].

• Counting matchings. A matching in a graph G is a subset M of the edges of G such
that no pair of edges in M shares a vertex. In statistical physics, matchings are studied
under the name of monomer-dimer coverings [26]. Our algorithm can approximately count
the number of matchings on a graph with n vertices and m edges in eO(n3/2m1/2/ϵ + n2m)
steps, as compared with the classical eO(n2m/ϵ2) [50].

Finally, as another example of how our algorithm can be applied, we improve the accuracy
of an existing quantum algorithm for estimating the total variation distance between probability
distributions. In this setting, we are given the ability to sample from probability distributions p
and q on n elements, and would like to estimate the distance between them up to additive error
ϵ. A quantum algorithm of Bravyi, Harrow and Hassidim solves this problem using O(√n/ϵ8)
samples [13], while no classical algorithm can achieve sublinear dependence on n [54].

Quantum mean estimation can signiﬁcantly improve the dependence of this quantum algorithm
on ϵ. The total variation distance between p and q can be described as the expected value of the
random variable R(x) = |p(x)−q(x)|

p(x)+q(x) , where x is drawn from the distribution r = (p + q)/2 [13].

For each x, R(x) can be computed up to accuracy ϵ using eO(√n/ϵ3/2) iterations of amplitude
estimation. Wrapping this within O(1/ϵ) iterations of the mean-estimation algorithm, we obtain
an overall algorithm running in time eO(√n/ϵ5/2). See Section 4 for details.

2
Algorithms

We now give technical details, parameter values and proofs for the various algorithms described
informally in Section 1.2. Recall that, for any randomised or quantum algorithm A, we let v(A)
be the random variable corresponding to the value computed by A. We assume that A takes no
input directly, but may have access to input (e.g. via queries to some black box or “oracle”) during
its execution. We further assume throughout that A is a quantum algorithm of the following form:
apply some unitary operator to the initial state |0n⟩; measure k ≤n qubits of the resulting state in
the computational basis, obtaining outcome x ∈{0, 1}k; output φ(x) for some easily computable
function φ : {0, 1}k →R. We ﬁnally assume that we have access to the inverse of the unitary part
of the algorithm, which we write as A−1.

Lemma 1 (Powering lemma [35]). Let A be a (classical or quantum) algorithm which aims to
estimate some quantity µ, and whose output eµ satisﬁes |µ −eµ| ≤ϵ except with probability γ, for
some ﬁxed γ < 1/2. Then, for any δ > 0, it suﬃces to repeat A O(log 1/δ) times and take the
median to obtain an estimate which is accurate to within ϵ with probability at least 1 −δ.

We will also need the following fundamental result from [12]:

7

## Page 8

Theorem 2 (Amplitude estimation [12]). There is a quantum algorithm called amplitude es-
timation which takes as input one copy of a quantum state |ψ⟩, a unitary transformation U =
2|ψ⟩⟨ψ| −I, a unitary transformation V = I −2P for some projector P, and an integer t. The
algorithm outputs ea, an estimate of a = ⟨ψ|P|ψ⟩, such that

p

|ea −a| ≤2π

t
+ π2

a(1 −a)

t2

with probability at least 8/π2, using U and V t times each.

The success probability of 8/π2 can be improved to 1 −δ for any δ > 0 using the powering
lemma at the cost of an O(log 1/δ) multiplicative factor.

2.1
Estimating the mean with bounded output values

We ﬁrst consider the problem of estimating E[v(A)] in the special case where v(A) is bounded
between 0 and 1. The algorithm for this case is eﬀectively a combination of elegant ideas of Brassard
et al. [11] and Wocjan et al. [59]. The former described an algorithm for eﬃciently approximating
the mean of an arbitrary function with respect to the uniform distribution; the latter described
an algorithm for approximating the expected value of a particular observable, with respect to an
arbitrary quantum state. The ﬁrst quantum algorithm achieving optimal scaling for approximating
the mean of a bounded function under the uniform distribution was due to Heinrich [27].

Algorithm 1: Approximating the mean output value of algorithms bounded between 0 and 1 (cf. [11,
27, 59])

Theorem 3. Let |ψ⟩be deﬁned as in Algorithm 1 and set U = 2|ψ⟩⟨ψ| −I. Algorithm 1 uses
O(log 1/δ) copies of the state A|0n⟩, uses U O(t log 1/δ) times, and outputs an estimate eµ such

8

## Page 9

that

p

|eµ −E[v(A)]| ≤C

!

E[v(A)]

t
+ 1

t2

with probability at least 1 −δ, where C is a universal constant. In particular, for any ﬁxed δ > 0
and any ϵ such that 0 ≤ϵ ≤1, to produce an estimate eµ such that with probability at least 1 −δ,
|eµ −E[v(A)]| ≤ϵ E[v(A)] it suﬃces to take t = O(1/(ϵ
p

E[v(A)])). To achieve |eµ −E[v(A)]| ≤ϵ
with probability at least 1 −δ it suﬃces to take t = O(1/ϵ).

Proof. The complexity claim follows immediately from Theorem 2. Also observe that W can be
implemented eﬃciently, as it is a controlled rotation of one qubit dependent on the value of φ(x) [59].
It remains to show the accuracy claim. The ﬁnal state of A, just before its last measurement, can
be written as
|ψ′⟩= A|0n⟩=
X

x
αx|ψx⟩|x⟩

for some normalised states |ψx⟩. If we then attach an ancilla qubit and apply W, we obtain

|ψ⟩= (I ⊗W)(A ⊗I)|0n⟩|0⟩=
X

We have
⟨ψ|P|ψ⟩=
X

x
αx|ψx⟩|x⟩
p

φ(x)|1⟩

.

1 −φ(x)|0⟩+
p

x
|αx|2φ(x) = E[v(A)].

Therefore, when we apply amplitude estimation, by Theorem 2 we obtain an estimate eµ of µ =
E[v(A)] such that

p

|eµ −µ| ≤2π

t
+ π2

µ(1 −µ)

t2

with probability at least 8/π2.
The powering lemma (Lemma 1) implies that the median of
O(log 1/δ) repetitions will lie within this accuracy bound with probability at least 1 −δ.

Observe that U = 2|ψ⟩⟨ψ| −I can be implemented with one use each of A and A−1, and
V = I −2P is easy to implement.

It seems likely that the median-ﬁnding algorithm of Nayak and Wu [45] could also be generalised
in a similar way, to eﬃciently compute the median of the output values of any quantum algorithm.
As we will not need this result here we do not pursue this further.

2.2
Estimating the mean with bounded ℓ2 norm

We now use Algorithm 1 to give an eﬃcient quantum algorithm for approximating the mean output
value of a quantum algorithm whose output has bounded ℓ2 norm. In what follows, for any algorithm
A, let A<x, Ax,y, A≥y, be the algorithms deﬁned by executing A to produce a value v(A) and:

• A<x: If v(A) < x, output v(A), otherwise output 0;

• Ax,y: If x ≤v(A) < y, output v(A), otherwise output 0;

• A≥y: If y ≤v(A), output v(A), otherwise output 0.

9

## Page 10

In addition, for any algorithm A and any function f : R →R, let f(A) be the algorithm produced by
evaluating v(A) and computing f(v(A)). Note that Algorithm 1 can easily be modiﬁed to compute
E[f(v(A))] rather than E[v(A)], for any function f : R →[0, 1], by modifying the operation W.

Our algorithm and correctness proof are a generalisation of a result of Heinrich [27] for com-
puting the mean with respect to the uniform distribution of functions with bounded L2 norm, and
are based on the same ideas. Write ∥v(A)∥2 :=
p

E[v(A)2].

Algorithm 2: Approximating the mean of positive functions with bounded ℓ2 norm

Lemma 4. Let |ψ⟩= A|0n⟩, U = 2|ψ⟩⟨ψ| −I. Algorithm 2 uses O(log(1/ϵ) log log(1/ϵ)) copies
of |ψ⟩, uses U O((1/ϵ) log3/2(1/ϵ) log log(1/ϵ)) times, and estimates E[v(A)] up to additive error
ϵ(∥v(A)∥2 + 1)2 with probability at least 4/5.

Proof. We ﬁrst show the resource bounds. Algorithm 1 is run Θ(log 1/ϵ) times, each time with pa-
rameter δ = Ω(1/(log 1/ϵ)). By Theorem 3, each use of Algorithm 1 consumes O(log log 1/ϵ) copies
of |ψ⟩and uses U O((1/ϵ)
p

log(1/ϵ) log log(1/ϵ)) times. The total number of copies of |ψ⟩used is
O(log(1/ϵ) log log(1/ϵ)), and the total number of uses of U is O((1/ϵ) log3/2(1/ϵ) log log(1/ϵ)).

All of the uses of Algorithm 1 succeed, except with probability at most 1/5 in total. To estimate
the total error in the case where they all succeed, we write

k
X

E[v(A)] = E[v(A0,1)] +

and use the triangle inequality term by term to obtain

k
X

|eµ −E[v(A)]| ≤|eµ0 −E[v(A0,1)]| +

ℓ=1
2ℓE[v(A2ℓ−1,2ℓ)/2ℓ] + E[v(A≥2k)]

ℓ=1
2ℓ|eµℓ−E[v(A2ℓ−1,2ℓ)/2ℓ]| + E[v(A≥2k)].

Let p(x) denote the probability that A outputs x. We have

x≥2k
p(x)x ≤1

E[v(A≥2k)] =
X

2k
X

By Theorem 3,

p

|eµ0 −E[v(A0,1)]| ≤C

10

x
p(x)x2 = ∥v(A)∥2
2
2k
.

!

E[v(A0,1)]

t0
+ 1

t2
0

## Page 11

and similarly

q



|eµℓ−E[v(A2ℓ−1,2ℓ)/2ℓ]| ≤C



So the total error is at most

q





k
X

E[v(A0,1)]


p

t0
+ 1

ℓ=1
2ℓ

C

t2
0
+





E[v(A2ℓ−1,2ℓ)]

t0 2ℓ/2
+ 1

.

t2
0





E[v(A2ℓ−1,2ℓ)]

+ ∥v(A)∥2
2
2k
.

t0 2ℓ/2
+ 1



t2
0

We apply Cauchy-Schwarz to the ﬁrst part of each term in the sum:

k
X

k
X

E[v(A2ℓ−1,2ℓ)] ≤
√

ℓ=1
2ℓ/2q

k

where the second inequality follows from

!1/2

≤
√

ℓ=1
2ℓE[v(A2ℓ−1,2ℓ)]

2k ∥v(A)∥2 ,

2ℓ−1≤x<2ℓ
p(x)x2 = ∥v(A2ℓ−1,2ℓ)∥2
2
2ℓ−1
.

2ℓ−1≤x<2ℓ
p(x)x ≤
1
2ℓ−1
X

E[v(A2ℓ−1,2ℓ)] =
X

Inserting this bound and using E[v(A0,1)] ≤1, we obtain

√

1
t0
+ 1

|eµ −E[v(A)]| ≤C

t2
0
+

!

+ ∥v(A)∥2
2
2k
.

t0
+ 2k+1

2k ∥v(A)∥2

t2
0

Inserting the deﬁnitions of t0 and k, we get an overall error bound

|eµ −E[v(A)]|

ϵ
p

D log2 1/ϵ +
√

log2 1/ϵ
+
ϵ2

≤C

2ϵ ∥v(A)∥2

D


ϵ + ϵ


+ ϵ ∥v(A)∥2
2

≤C

D + 2ϵ ∥v(A)∥2 + 4ϵ

D

D

= ϵ
C


1 + 5


+ ∥v(A)∥2
2



D + 2 ∥v(A)∥2

D

!

1/2
+
4ϵ
D log2 1/ϵ


1 +
1
log2 1/ϵ

+ ϵ ∥v(A)∥2
2

using 0 < ϵ < 1/2 in the second inequality. For a suﬃciently large constant D, this is upper-bounded
by ϵ(∥v(A)∥2 + 1)2 as claimed.

Observe that, if E[v(A)2] = O(1), to achieve additive error ϵ the number of uses of A that
we need is O((1/ϵ) log3/2(1/ϵ) log log(1/ϵ)). By the powering lemma, we can repeat Algorithm 2
O(log 1/δ) times and take the median to improve the probability of success to 1 −δ for any δ > 0.

2.3
Estimating the mean with bounded variance

We are now ready to formally state our algorithm for estimating the mean output value of an
arbitrary algorithm with bounded variance. For clarity, some of the steps are reordered as compared
with the informal description in Section 1.2. Recall that, in the classical setting, if we wish to
estimate E[v(A)] up to additive error ϵ for an arbitrary algorithm A such that

Var(v(A)) := E[(v(A) −E[v(A)])2] ≤σ2,

we need to use A Ω(σ2/ϵ2) times [15].

11

## Page 12

Algorithm 3: Approximating the mean with bounded variance

Theorem 5. Let |ψ⟩= A|0n⟩, U = 2|ψ⟩⟨ψ| −I. Algorithm 3 uses O(log(σ/ϵ) log log(σ/ϵ)) copies
of |ψ⟩, uses U O((σ/ϵ) log3/2(σ/ϵ) log log(σ/ϵ)) times, and estimates E[v(A)] up to additive error ϵ
with success probability at least 2/3.

Proof. First, observe that em is quite close to µ′ := E[v(A′)] with quite high probability.
As
Var(v(A′)) = Var(v(A))/σ2 ≤1, by Chebyshev’s inequality we have

Pr[|v(A′) −µ′| ≥3] ≤1

9.

We therefore assume that | em −µ′| ≤3. In this case we have

∥v(B)∥2
=
E[v(B)2]1/2 = E[((v(A′) −µ′) + (µ′ −em))2]1/2

≤
E[(v(A′) −µ′)2]1/2 + E[(µ′ −em)2]1/2

≤
4,

where the ﬁrst inequality is the triangle inequality.
Thus ∥v(B)/4∥2 ≤1, which implies that
∥v(−B<0)/4∥2 ≤1 and ∥v(B≥0)/4∥2 ≤1.

The next step is to use Algorithm 2 to estimate E[v(−B<0)/4] and E[v(B≥0)/4] with accuracy
ϵ/(32σ) and failure probability 1/9. By Lemma 4, if the algorithm succeeds in both cases the
estimates are accurate up to ϵ/(8σ). We therefore obtain an approximation of each of E[v(−B<0)]
and E[v(B≥0)] up to additive error ϵ/(2σ). As we have

E[v(A)] = σ E[v(A′)] = σ( em −E[v(−B<0)] + E[v(B≥0)])

by linearity of expectation, using a union bound we have that σ eµ approximates E[v(A)] up to
additive error ϵ with probability at least 2/3.

2.4
Estimating the mean with bounded relative error

It is often useful to obtain an estimate of the mean output value of an algorithm which is accurate
up to small relative error, rather than the absolute error achieved by Algorithm 3. Assume that

12

## Page 13

we have the bound on the relative variance that Var(v(A))/(E[v(A)])2 ≤B, where we normally
think of B as small, e.g. B = O(1). Classically, it follows from Chebyshev’s inequality that the
simple classical algorithm described in the Introduction approximates E[v(A)] up to additive error
ϵ E[v(A)] with O(B/ϵ2) uses of A. In the quantum setting, we can improve the dependence on ϵ
near-quadratically.

Algorithm 4: Approximating the mean with bounded relative error

Theorem 6. Let |ψ⟩= A|0n⟩, U = 2|ψ⟩⟨ψ| −I. Algorithm 4 uses O(B + log(1/ϵ) log log(1/ϵ))
copies of |ψ⟩, uses U O((B/ϵ) log3/2(B/ϵ) log log(B/ϵ)) times, and outputs an estimate eµ such that

Pr[|eµ −E[v(A)]| ≥ϵ E[v(A)]] ≤1/4.

Proof. The complexity bounds follow from Lemma 4; we now analyse the claim about accuracy.
em is a random variable whose expectation is E[v(A)] and whose variance is Var(v(A))/⌈32B⌉. By
Chebyshev’s inequality, we have

Pr[| em −E[ em]| ≥|E[ em]|/2] ≤4 Var( em)

E[ em]2
=
4 Var(v(A))
⌈32B⌉E[v(A)]2 ≤1

8.

We can thus assume that E[v(A)]/2 ≤em ≤3 E[v(A)]/2. In this case, when we apply Algorithm 2
to A/ em, we receive an estimate of E[v(A)]/ em which is accurate up to additive error

B + 1)2
≤ϵ E[v(A)](2 ∥v(A)∥2 /E[v(A)] + 1)2

2ϵ(∥v(A)∥2 / em + 1)2

3(2
√

em(2
√

B + 1)2
≤ϵ E[v(A)]

em

except with probability 1/8, where we use ∥v(A)∥2 /E[v(A)] ≤
√

B. Multiplying by em and taking
a union bound, we get an estimate of E[v(A)] which is accurate up to ϵ except with probability at
most 1/4.

Once again, using the powering lemma we can repeat Algorithms 3 and 4 O(log 1/δ) times and
take the median to improve their probabilities of success to 1 −δ for any δ > 0.

To see that Algorithms 3 and 4 are close to optimal, we can appeal to a result of Nayak
and Wu [45]. Let A be an algorithm which picks an integer x between 1 and N uniformly at
random, for some large N, and outputs f(x) for some function f : {1, . . . , N} →{0, 1}. Then
E[v(A)] = |{x : f(x) = 1}|/N. It was shown by Nayak and Wu [45] that any quantum algorithm
which computes this quantity for an arbitrary function f up to (absolute or relative) error ϵ must
make at most Ω(1/ϵ) queries to f in the case that |{x : f(x) = 1}| = N/2. As the output of A
for any such function has variance 1/4, this implies that Algorithms 2 and 4 are optimal in the
black-box setting in terms of their scaling with ϵ, up to polylogarithmic factors. By rescaling, we
get a similar near-optimality claim for Algorithm 3 in terms of its scaling with σ.

13

## Page 14

3
Partition function problems

In this section we formally state and prove our results about partition function problems. We ﬁrst
recall the deﬁnitions from Section 1.3. A partition function Z is deﬁned by

Z(β) =
X

x∈Ω
e−β H(x)

where β is an inverse temperature and H is a Hamiltonian function taking integer values in the set
{0, . . . , n}. Let 0 = β0 < β1 < · · · < βℓ= ∞be a sequence of inverse temperatures and assume
that we can easily compute Z(β0) = |Ω|. We want to approximate Z(∞) by approximating the
ratios αi := Z(βi+1)/Z(βi) and using the telescoping product

Z(βℓ) = Z(β0)Z(β1)

Z(β0)
Z(β2)
Z(β1) . . . Z(βℓ)

Z(βℓ−1).

Finally, a sequence of Gibbs distributions πi is deﬁned by

πi(x) =
1
Z(βi)e−βiH(x).

3.1
Chebyshev cooling schedules

We start by motivating, and formally deﬁning, the concept of a Chebyshev cooling schedule [50].
To approximate αi we deﬁne the random variable

Yi(x) = e−(βi+1−βi)H(x).

Then

E[Yi] := Eπi[Yi] =
1
Z(βi)

x∈Ω
e−βiH(x)e−(βi+1−βi)H(x) =
1
Z(βi)

X

x∈Ω
e−βi+1H(x) = Z(βi+1)

X

Z(βi)
= αi.

The following result was shown by Dyer and Frieze [19] (see [50] for the statement here):

Theorem 7. Let Y0, . . . , Yℓ−1 be independent random variables such that E[Y 2
i ]/E[Yi]2 ≤B for all
i, and write Y = E[Y0]E[Y1] . . . E[Yℓ−1]. Let eαi be the average of 16Bℓ/ϵ2 independent samples from
Yi, and set eY = eα0 eα1 . . . eαℓ−1. Then

Pr[(1 −ϵ)Y ≤eY ≤(1 + ϵ)Y ] ≥3/4.

Thus a classical algorithm can approximate Z(∞) up to relative error ϵ using O(Bℓ2/ϵ2) sam-
ples in total, assuming that Z(0) can be computed without using any samples and that we have
E[Y 2
i ]/E[Yi]2 ≤B. To characterise the latter constraint, observe that we have

E[Y 2
i ] =
1
Z(βi)

x∈Ω
e−βiH(x)e−2(βi+1−βi)H(x) =
1
Z(βi)

X

x∈Ω
e(βi−2βi+1)H(x) = Z(2βi+1 −βi)

X

Z(βi)
,

so
E[Y 2
i ]
(E[Yi])2 = Z(2βi+1 −βi)Z(βi)

This motivates the following deﬁnition:

14

Z(βi+1)2
.

## Page 15

Deﬁnition 1 (Chebyshev cooling schedules [50]). Let Z be a partition function. Let β0, . . . , βℓbe
a sequence of inverse temperatures such that 0 = β0 < β1 < · · · < βℓ= ∞. The sequence is called
a B-Chebyshev cooling schedule for Z if

Z(2βi+1 −βi)Z(βi)

for all i, for some ﬁxed B.

Z(βi+1)2
≤B

Assume that we have a sequence of estimates eαi such that, for all i, |eαi −αi| ≤(ϵ/2ℓ) αi with
probability at least 1 −1/(4ℓ). We output as a ﬁnal estimate

eZ = Z(0) eα0 eα1 . . . eαℓ−1.

By a union bound, all of the estimates eαi are accurate to within (ϵ/2ℓ) αi, except with probability
at most 1/4. Assuming that all the estimates are indeed accurate, we have

1 −ϵ/2 ≤(1 −ϵ/(2ℓ))ℓ≤
eZ
Z(∞) ≤(1 + ϵ/(2ℓ))ℓ≤eϵ/2 ≤1 + ϵ

for ϵ < 1. Thus | eZ −Z(∞)| ≤ϵ Z(∞) with probability at least 3/4.

Using these ideas, we can formalise the discussion in Section 1.3.

Theorem 8. Let Z be a partition function with |Ω| = A. Assume that we are given a B-Chebyshev
cooling schedule 0 = β0 < β1 < · · · < βℓ= ∞for Z. Further assume that we have the ability to
exactly sample from the distributions πi, i = 1, . . . , ℓ−1. Then there is a quantum algorithm which
outputs an estimate eZ such that

Pr[(1 −ϵ)Z(∞) ≤eZ ≤(1 + ϵ)Z(∞)] ≥3/4.

using

O
Bℓlog ℓ

ϵ
log3/2
Bℓ

ϵ

samples in total.


= eO
Bℓ2


log log
Bℓ



ϵ

ϵ

Proof. For each i = 1, . . . , ℓ−1, we use Algorithm 4 to estimate E[Yi] up to additive error
(ϵ/(2ℓ))E[Yi] with failure probability 1/(4ℓ).
As the βi form a B-Chebyshev cooling schedule,
E[Y 2
i ]/E[Yi]2 ≤B, so Var(Yi)/E[Yi]2 ≤B. By Theorem 6, each use of Algorithm 4 requires

O
Bℓ

ϵ log3/2
Bℓ

ϵ


log log
Bℓ


log ℓ


ϵ

samples from πi to achieve the desired accuracy and failure probability.
The total number of
samples is thus

O
Bℓ2 log ℓ

ϵ
log3/2
Bℓ

ϵ

as claimed.

15


log log
Bℓ



ϵ

## Page 16

3.2
Approximate sampling

It is unfortunately not always possible to exactly sample from the distributions πi. However, one
classical way of approximately sampling from each of these distributions is to use a (reversible,
ergodic) Markov chain which has unique stationary distribution πi. Assume the Markov chain has
relaxation time τ, where τ := 1/(1−|λ1|), and λ1 is the second largest eigenvalue in absolute value.
Then one can sample from a distribution eπi such that ∥eπi−πi∥≤ϵ using O(τ log(1/(ϵπmin,i))) steps
of the chain, where πmin,i = minx |πi(x)| [38]. We would like to replace the classical Markov chain
with a quantum walk, to obtain a faster mixing time. A construction due to Szegedy [51] deﬁnes
a quantum walk corresponding to any ergodic Markov chain, such that the dependence on τ in the
mixing time can be improved to O(√τ) [48]. Unfortunately, it is not known whether in general the
dependence on πmin,i can be kept logarithmic [48, 18]. Indeed, proving such a result is likely to be
hard, as it would imply a polynomial-time quantum algorithm for graph isomorphism [6].

Nevertheless, it was shown by Wocjan and Abeyesinghe [58] (improving previous work on us-
ing quantum walks for classical annealing [49]) that one can achieve relatively eﬃcient quantum
sampling if one has access to a sequence of slowly varying Markov chains.

Theorem 9 (Wocjan and Abeyesinghe [58]). Let M0, . . . , Mr be classical reversible Markov chains
with stationary distributions π0, . . . , πr such that each chain has relaxation time at most τ. Assume
that |⟨πi|πi+1⟩|2 ≥p for some p > 0 and all i ∈{0, . . . , r −1}, and that we can prepare the state
|π0⟩. Then, for any ϵ > 0, there is a quantum algorithm which produces a quantum state |eπr⟩such
that ∥|eπr⟩−|πr⟩|0a⟩∥≤ϵ, for some integer a. The algorithm uses

O(r√τ log2(r/ϵ)(1/p) log(1/p))

steps in total of the quantum walk operators Wi corresponding to the chains Mi.

In addition, one can approximately reﬂect about the states |πi⟩more eﬃciently still, with a
runtime that does not depend on r. This will be helpful because Algorithm 4 uses signiﬁcantly
more reﬂections than it does copies of the starting state.

Theorem 10 (Wocjan and Abeyesinghe [58], see [59] for version here). Let M0, . . . , Mr be classical
reversible Markov chains with stationary distributions π0, . . . , πr such that each chain has relaxation
time at most τ. For each i there is an approximate reﬂection operator eRi such that

eRi|φ⟩|0b⟩= (2|ψ⟩⟨ψ| −I)|φ⟩|0b⟩+ |ξ⟩,

where |φ⟩is arbitrary, b = O((log τ)(log 1/ϵ)), and |ξ⟩is a vector with ∥|ξ⟩∥≤ϵ. The algorithm
uses O(√τ log(1/ϵ)) steps of the quantum walk operator Wi corresponding to the chain Mi.

In our setting, we can easily create the quantum state |π0⟩, which is the uniform superposition
over all conﬁgurations x. We now show that the overlaps |⟨πi|πi+1⟩|2 are large for all i. We go via
the chi-squared divergence

x∈Ω
π(x)
ν(x)

χ2(ν, π) :=
X

As noted in [50], one can calculate that

π(x) −1
2
=
X

ν(x)2

π(x) −1.

x∈Ω

χ2(πi+1, πi) = Z(βi)Z(2βi+1 −βi)

16

Z(βi+1)2
−1.
(1)

## Page 17

Therefore, if the βi values form a Chebyshev cooling schedule, χ2(πi+1, πi) ≤B −1 for all i. For
any distributions ν, π, we also have

1
p

χ2(ν, π) + 1
=
1
qP
x∈Ων(x) ν(x)

s

π(x)
ν(x) = ⟨ν|π⟩

π(x)
≤
X

x∈Ω
ν(x)

by applying Jensen’s inequality to the function x 7→1/√x. So, for all i, |⟨πi|πi+1⟩|2 ≥1/B. Note
that in [50] it was necessary to introduce the concept of a reversible Chebyshev cooling schedule to
facilitate “warm starts” of the Markov chains used in the algorithm. That work uses the fact that
one can eﬃciently sample from πi+1, given access to samples from πi, if χ2(πi, πi+1) = O(1); this
is the reverse of the condition (1). Here we do not need to reverse the schedule as the precondition
|⟨πi|πi+1⟩|2 ≥Ω(1) required for Theorem 9 is already symmetric.

We are now ready to formally state our result about approximating partition functions. We
assume that ϵ is relatively small to simplify the bounds; this is not an essential restriction.

Theorem 11. Let Z be a partition function. Assume we have a B-Chebyshev cooling schedule
β0 = 0 < β1 < β2 < · · · < βℓ= ∞for B = O(1). Assume that for every inverse temperature βi
we have a reversible ergodic Markov chain Mi with stationary distribution πi and relaxation time
upper-bounded by τ. Further assume that we can sample directly from M0. Then, for any δ > 0
and ϵ = O(1/√log ℓ), there is a quantum algorithm which uses

O((ℓ2√τ/ϵ) log5/2(ℓ/ϵ) log(ℓ/δ) log log(ℓ/ϵ)) = eO(ℓ2√τ/ϵ)

steps of the quantum walks corresponding to the Mi chains and outputs eZ such that

Pr[(1 −ϵ)Z(∞) ≤eZ ≤(1 + ϵ)Z(∞)] ≥1 −δ.

Proof. For each i, we use Algorithm 4 to approximate αi up to relative error ϵ/(2ℓ), with failure
probability γ, for some small constant γ. This would require R reﬂections about the state |πβi⟩, for
some R such that R = O((ℓ/ϵ) log3/2(ℓ/ϵ) log log(ℓ/ϵ)), and O(log(ℓ/ϵ) log log(ℓ/ϵ)) copies of |πβi⟩.

Instead of performing exact reﬂections and using exact copies of the states |πi⟩, we use approx-
imate reﬂections and approximate copies of |πi⟩. By Theorem 10, O(√τ log(1/ϵr)) walk operations
are suﬃcient to reﬂect about |πi⟩up to an additive error term of order ϵr. By Theorem 9, as we
have a Chebyshev cooling schedule, a quantum state |eπi⟩such that ∥|eπi⟩−|πi⟩|0b⟩∥≤ϵs can be
produced using O(ℓ√τ log2(ℓ/ϵs)) steps of the quantum walks corresponding to the Markov chains
M0, . . . , Mi.

We choose ϵr = γ/R, ϵs = γ. Then the ﬁnal state of Algorithm 4 using approximate reﬂections
and starting with the states |eπi⟩rather than |πi⟩can diﬀer from the ﬁnal state of an exact algorithm
by at most Rϵr + ϵs = 2γ in ℓ2 norm. This implies that the total variation distance between the
output probability distributions of the exact and inexact algorithms is at most 2γ, and hence by a
union bound that the approximation is accurate up to relative error ϵ/(2ℓ) except with probability
3γ. For each i, we then take the median of O(log(ℓ/δ)) estimates to achieve an estimate which is
accurate up to relative error ϵ/(2ℓ) except with probability at most δ/ℓ. By a union bound, all
the estimates are accurate up to relative error ϵ/(2ℓ) except with probability at most δ, so their
product is accurate to relative error ϵ except with probability at most δ.

The total number of steps needed to produce all the copies of the states |eπi⟩required is thus

O(ℓ· ℓ√τ(log2 ℓ) · log(ℓ/ϵ) log log(ℓ/ϵ) · log(ℓ/δ))

17

## Page 18

and the total number of steps needed to perform the reﬂections is

O(ℓ· √τ(log R) · R · log(ℓ/δ)).

Adding the two, substituting the value of R, and using ϵ = O(1/√log ℓ), we get an overall bound
of
O((ℓ2√τ/ϵ) log5/2(ℓ/ϵ) log(ℓ/δ) log log(ℓ/ϵ)) = eO(ℓ2√τ/ϵ)

as claimed.

We remark that, in the above complexities, we have chosen to take the number of quantum
walk steps used as our measure of complexity. This is to enable a straightforward comparison with
the classical literature, which typically uses a random walk step as its elementary operation for
the purposes of measuring complexity [50]. To implement each quantum walk step eﬃciently and
accurately, two possible approaches are to use eﬃcient state preparation [14] or recently developed
approaches to eﬃcient simulation of sparse Hamiltonians [9].

Finally, we mention that one could also consider a more general setting for approximate sam-
pling. Imagine that we would like to approximate the mean µ of some random variable chosen
according to some distribution π, but only have access to samples from a distribution eπ that ap-
proximates π (using some method which, for example, might not be a quantum walk). In this case,
one can show that the estimation algorithm does not notice the diﬀerence between eπ and π and
hence allows eﬃcient estimation of µ. See Appendix A for the details.

3.3
Computing a Chebyshev cooling schedule

We still need to show that, given a particular partition function, we can actually ﬁnd a Chebyshev
cooling schedule. For this we simply use a known classical result:

Theorem 12 (ˇStefankoviˇc, Vempala and Vigoda [50]). Let Z be a partition function. Assume that
for every inverse temperature β we have a Markov chain Mβ with stationary distribution πβ and
relaxation time upper-bounded by τ. Further assume that we can sample directly from M0. Then,
for any δ > 0 and any B = O(1), we can produce a B-Chebyshev cooling schedule of length

ℓ= O(
p

log A(log n)(log log A))

with probability at least 1 −δ, using at most

Q = O((log A)((log n) + log log A)5τ log(1/δ))

steps of the Markov chains.

We remark that a subsequent algorithm [28] improves the polylogarithmic terms and the hidden
constant factors in the complexity. However, this algorithm assumes that we can eﬃciently generate
independent samples from distributions approximating πβ for arbitrary β. The most eﬃcient general
algorithm known [50] for approximately sampling from arbitrary distributions πβ uses “warm starts”
and hence does not produce independent samples.

Combining all the ingredients, we have the following result:

Corollary 13. Let Z be a partition function and let ϵ > 0 be a desired precision such that ϵ =
O(1/√log log A). Assume that for every inverse temperature β we have a Markov chain Mβ with

18

## Page 19

stationary distribution πβ and relaxation time upper-bounded by τ. Further assume that we can
sample directly from M0. Then, for any δ > 0, there is a quantum algorithm which uses

O(((log A)(log2 n)(log log A)2√τ/ϵ) log5/2((log A)/ϵ) log((log A)/δ) log log((log A)/ϵ)

+ (log A)((log n) + log log A)5τ log(1/δ)))

= eO((log A)√τ(1/ϵ + √τ))

steps of the Mβ chains and their corresponding quantum walk operations, and outputs eZ such that

Pr[(1 −ϵ)Z(∞) ≤eZ ≤(1 + ϵ)Z(∞)] ≥1 −δ.

The best comparable classical result known is eO((log A)τ/ϵ2) [50]. We therefore see that we
have achieved a near-quadratic reduction in the complexity with respect to both τ and ϵ, assuming
that ϵ ≤1/√τ. Otherwise, we still achieve a near-quadratic reduction with respect to ϵ.

Note that, if we could ﬁnd a quantum algorithm that outputs a Chebyshev cooling schedule
using eO((log A)√τ) steps of the Markov chains, Corollary 13 would be improved to a complexity
of eO((log A)√τ/ϵ). It is instructive to note why this does not seem to be immediate. The classical
algorithm for this problem [50] needs to approximately sample from Markov chains Mβ for arbitrary
values of β. To do this, it starts by ﬁxing a nonadaptive Chebyshev cooling schedule 0 < β′
1 <
β′
2 < · · · < β′
ℓ= ∞of length ℓ= eO(log A). When the algorithm wants to sample from Mβ with
β′
i < β < β′
i+1, the algorithm uses an approximate sample from Mβ′
i as a “warm start”. To produce

one sample corresponding to each β′
i value requires eO(ℓτ) samples, because each Mβ′
i also provides
a warm start for Mβ′
i+1. But, in the quantum case, this does not work because, by no-cloning, the
states |πβ′
i⟩cannot be reused in this way to provide warm starts for multiple runs of the algorithm.

3.4
Some partition function problems

In this section we describe some representative applications of our results to problems in statistical
physics and computer science.

The ferromagnetic Ising model. This well-studied statistical physics model is deﬁned in
terms of a graph G = (V, E) by the Hamiltonian

H(z) = −
X

(u,v)∈E
zuzv,

where |V | = n and z ∈{±1}n. A standard method to approximate the partition function of the
Ising model uses the Glauber dynamics. This is a simple Markov chain with state space {±1}n,
each of whose transitions involves only updating individual sites, and whose stationary distribution
is the Gibbs distribution
πβ(z) =
1
Z(β)e−βH(z).

This Markov chain, which has been intensively studied for decades, is known to mix rapidly in
certain regimes [41]. Here we mention just one representative recent result:

Theorem 14 (Mossel and Sly [44]). For any integer d > 2, and inverse temperature β > 0 such
that (d −1) tanh β < 1, the mixing time of the Glauber dynamics on any graph of maximum degree
d is O(n log n).

19

## Page 20

(More precise results than Theorem 14 are known for certain speciﬁc graphs such as lattices [42].)
As we have A = 2n, in the regime where (d −1) tanh β < 1 the quantum algorithm approximates
Z(β) to within ϵ relative error in eO(n3/2/ϵ + n2) steps. The fastest known classical algorithm with
rigorously proven performance bounds [50] uses time eO(n2/ϵ2). We remark that an alternative
approach of Jerrum and Sinclair [34], which is based on analysing a diﬀerent Markov chain, gives a
polynomial-time classical algorithm which works for any temperature, but is substantially slower.

Counting colourings. Here we are given as input a graph G with n vertices and maximum
degree d. We seek to approximately count the number of valid k-colourings of G, where a colouring
of the vertices is valid if all pairs of neighbouring vertices are assigned diﬀerent colours, and k =
O(1). In physics, this problem corresponds to the partition function of the Potts model evaluated
at zero temperature. It is known that the Glauber dynamics for the Potts model mixes rapidly in
some cases [20]. One particularly clean result of this form is work of Jerrum [31] showing that this
Markov chain mixes in time O(n log n) if k > 2d. As here A = kn, we obtain a quantum algorithm
approximating the number of colourings of G up to relative error ϵ in eO(n3/2/ϵ + n2) steps, as
compared with the classical eO(n2/ϵ2) [50].

Counting matchings. A matching in a graph G is a subset M of the edges of G such that no
pair of edges in M shares a vertex. In statistical physics, matchings are often known as monomer-
dimer coverings [26]. To count the number of matchings, we consider the partition function

Z(β) =
X

M∈M
e−β|M|,

where M is the set of matchings of G. We have Z(0) = |M|, while Z(∞) = 1, as in this case
the sum is zero everywhere except the empty matching (00 = 1). Therefore, in this case we seek
to approximate Z(0) using a telescoping product which starts with Z(∞). In terms of the cooling
schedule 0 = β0 < β1 < · · · < βℓ= ∞, we have

Z(β0) = Z(βℓ)Z(βℓ−1)

Z(βℓ)
Z(βℓ−2)
Z(βℓ−1) . . . Z(β0)

Z(β1).

As we have reversed our usage of the cooling schedule, rather than looking for it to be a B-Chebyshev
cooling schedule we instead seek the bound

Z(2βi −βi+1)Z(βi+1)

Z(βi)2
≤B

to hold for all i = 0, . . . , ℓ−1. That is, the roles of βi and βi+1 have been reversed as compared
with (1). However, the classical algorithm for printing a cooling schedule can be modiﬁed to output
a “reversible” schedule where this constraint is satisﬁed too, with only a logarithmic increase in
complexity [50]. In addition, it was shown by Jerrum and Sinclair [33, 32] that, for any β, there is
a simple Markov chain which has stationary distribution π, where

π(M) =
1
Z(β)

X

M∈M
e−β|M|,

and which has relaxation time τ = O(nm) on a graph with n vertices and m edges. Finally, in the
setting of matchings, A = O(n!2n). Putting these parameters together, we obtain a quantum com-
plexity eO(n3/2m1/2/ϵ + n2m), as compared with the lowest known classical bound eO(n2m/ϵ2) [50].

20

## Page 21

4
Estimating the total variation distance

Here we give the technical details of our improvement of the accuracy of a quantum algorithm of
Bravyi, Harrow and Hassidim [13] for estimating the total variation distance between probability
distributions. In this setting, we are given the ability to sample from probability distributions p
and q on n elements, and would like to estimate ∥p −q∥:= 1

2∥p −q∥1 = 1

2
P
x∈[n] |p(x) −q(x)|
up to additive error ϵ. Classically, estimating ∥p −q∥up to error, say, 0.01 cannot be achieved
using O(nα) samples for any α < 1 [54], but in the quantum setting the dependence on n can be
improved quadratically:

Theorem 15 (Bravyi, Harrow and Hassidim [13]). Given the ability to sample from p and q, there
is a quantum algorithm which estimates ∥p −q∥up to additive error ϵ, with probability of success
1 −δ, using O(√n/(ϵ8δ5)) samples.

Here we will use Theorem 3 to improve the dependence on ϵ and δ of this algorithm. We will
approximate the mean output value of the following algorithm, which was a subroutine previously
used in [13].

Algorithm 5: Subroutine for estimating the total variation distance

If the estimates ep(x), eq(x) were precisely accurate, the expected output of the subroutine would
be

 |p(x) −q(x)|

p(x) + q(x)

p(x) + q(x) = 1

E :=
X

2

2

x∈[n]

X

x∈[n]
|p(x) −q(x)| = ∥p −q∥.

We now bound how far the expected output eE of the algorithm is from this exact value. By linearity
of expectation,

X

x∈[n]
r(x)E[ed(x) −d(x)]

| eE −E| =

≤
X

x∈[n]
r(x)E[|ed(x) −d(x)|]

where d(x) = |p(x) −q(x)|/(p(x) + q(x)), ed(x) = |ep(x) −eq(x)|/(ep(x) + eq(x)). Note that ed(x) is a
random variable. Split [n] into “small” and “large” parts according to whether r(x) ≤ϵ/n. Then

| eE −E|
≤
X

x,r(x)≤ϵ/n
r(x)E[|ed(x) −d(x)|] +
X

≤
ϵ +
X

x,r(x)≥ϵ/n
r(x)E[|ed(x) −d(x)|]

x,r(x)≥ϵ/n
r(x)E[|ed(x) −d(x)|]

using that 0 ≤d(x), ed(x) ≤1. From Theorem 2, for any δ > 0 we have

p

|ep(x) −p(x)| ≤2π

21

t
+ π2

p(x)

t2

## Page 22

except with probability at most δ, using O(t log 1/δ) samples from p. If t ≥4π/(η
p

p(x) + q(x))
for some 0 ≤η ≤1, this implies that

|ep(x) −p(x)| ≤2πη
p

p(x)
p

p(x) + q(x)
4π
+ π2η2(p(x) + q(x))

16π2
≤η(p(x) + q(x))

except with probability at most δ. A similar claim also holds for |eq(x) −q(x)|. We now use the
following technical result from [13]:

Proposition 16. Consider a real-valued function f(p, q) = (p −q)/(p + q) where 0 ≤p, q ≤1.
Assume that |p −ep|, |q −eq| ≤η(p + q) for some η ≤1/5. Then |f(p, q) −f(ep, eq)| ≤5η.

By Proposition 16, for all x such that t ≥4π/(η
p

p(x) + q(x)) we have |ed(x) −d(x)| ≤5η,
except with probability at most 2δ. We now ﬁx t = ⌈10
√

2π√nϵ−3/2⌉. Then, for all x such that
p(x) + q(x) ≥2ϵ/n, |ed(x) −d(x)| ≤ϵ except with probability at most 2δ. Thus, for all x such that
r(x) ≥ϵ/n,
E[|ed(x) −d(x)|] ≤2δ + (1 −2δ)ϵ ≤2δ + ϵ.

Taking δ = ϵ, we have
| eE −E| ≤4ϵ

for any ϵ, using O(√nϵ−3/2 log(1/ϵ)) samples.
It therefore suﬃces to use O(√nϵ−3/2 log(1/ϵ))
samples to achieve | eE −E| ≤ϵ/2. As the output of this subroutine is bounded between 0 and 1, to
approximate eE up to additive error ϵ/2 with failure probability δ, it suﬃces to use the subroutine
O((1/ϵ) log(1/δ)) times by Theorem 3. So the overall complexity is O((√n/ϵ5/2) log(1/ϵ) log(1/δ)).
For small ϵ and δ this is a substantial improvement on the O(√n/(ϵ8δ5)) complexity stated by
Bravyi, Harrow and Hassidim [13].

Acknowledgements

This work was supported by the UK EPSRC under Early Career Fellowship EP/L021005/1. I
would like to thank Aram Harrow for helpful conversations and pointing out references, and Daniel
Lidar for supplying further references. I would also like to thank several anonymous referees for
their helpful comments. Special thanks to Tongyang Li for pointing out an error in Section 4.

A
Stability of Algorithm 3

It is often the case that one wishes to estimate some quantity of interest deﬁned in terms of samples
from some probability distribution π, but can only sample from a distribution eπ which is close to
π in total variation distance (for example, using Markov chain Monte Carlo methods). We now
show that, if Algorithm 3 is given access to samples from eπ rather than π, it does not notice the
diﬀerence. We will need the following claim.

Claim 17. For any x, y ∈[0, 1],

| arcsin x −arcsin y| ≤π

2

22

|x2 −y2|.

p

## Page 23

Proof. We use a standard addition formula for arcsin to obtain

1 −y2 −y
p

| arcsin x −arcsin y|
=
| arcsin(x
p

≤
π

2 |
p

≤
π

p

2

1 −x2)|

x2(1 −y2) −
p

y2(1 −x2)|

|x2 −y2|,

where the ﬁrst inequality is sin θ ≥(2/π)θ for all θ ∈[0, π/2], and the second inequality is

|a2 −b2|,

|a −b|(a + b) =
p

|a −b| ≤
p

valid for all non-negative a and b.

Lemma 18. Let A and B be algorithms with distributions DA and DB on their output values, such
that ∥DA −DB∥≤γ, for some γ. Assume that Algorithm 3 is applied to A, and uses the operator
U = 2|ψ⟩⟨ψ| −I T times, where |ψ⟩= A|0⟩. Then the algorithm estimates E[v(B)] up to additive
error ϵ except with probability at most 3/10 + π2
√

6T√γ.

Lemma 18 is reminiscent of the hybrid argument for proving lower bounds on quantum query
complexity [8]: if the distributions DA and DB are close, and the amplitude ampliﬁcation algorithm
makes few queries, it cannot distinguish them. However, here the quantiﬁers appear in a diﬀerent
order: whereas in the setting of lower-bounding quantum query complexity we wish to show that
there exist pairs of distributions which are indistinguishable by any possible algorithm, here we
wish to show that one ﬁxed algorithm cannot distinguish any pair of close distributions.

Also note that Wocjan et al. [59] proved a similar result in the setting where we are given access
to an approximate rotation eU ≈U. However, the result here is more general, in that we do not
assume that |φ⟩= B|0⟩is close to |ψ⟩, but merely that the measured probability distributions are
close.

Proof. We ﬁrst use the calculations for the output probabilities of the amplitude estimation algo-
rithm from [12] when applied as in Theorem 3 with t queries to an algorithm with mean output
value µA, and another with mean output value µB.

For x, y ∈R, deﬁne d(x, y) = minz∈Z |z+x−y|. 2πd(x, y) is the length of the shortest arc on the
unit circle between e2πix and e2πiy. Let ωA and ωB be deﬁned by sin2 ωA = µA, sin2 ωB = µB, and
set ∆= d(ωA, ωB). Finally, let MA and MB be the distributions over the measurement outcomes
when amplitude estimation is applied to estimate µA, µB.

The distribution on the measurement outcomes of the amplitude estimation algorithm after t
uses of the input operator, when applied to a phase of ω, is equivalent [12] to that obtained by
measuring the state

|St(ω)⟩:= 1
√

X

t

y∈[t]
e2πiωy|y⟩,

so the total variation distance between the distributions MA and MB obeys the bound

∥MA −MB∥2 ≤1 −|⟨St(ωA)|St(ωB)⟩|2 = 1 −sin2(πt∆)

t2 sin2(π∆),

where the ﬁrst equality is standard [46] and the second equality is [12, Lemma 10]. Using the
inequalities

θ −θ3

23

6 ≤sin θ ≤θ,

## Page 24

valid for θ ≥0, we obtain

∥MA −MB∥2 ≤1 −
πt∆−(πt∆)3/6

tπ∆

2
= 1 −

1 −(πt∆)2

2
≤(πt∆)2

3
.

6

As we have
∆= min
z∈Z |z + ωA −ωB| ≤|ωA −ωB| ≤π

by Claim 17, we have

∥MA −MB∥≤π2

3t
p

2
√

p

|µA −µB|

2

|µA −µB|.

Within Algorithm 2, Theorem 3 is applied to v(A2ℓ−1,2ℓ)/2ℓfor various values of ℓ. We have

|E[v(A2ℓ−1,2ℓ)/2ℓ] −E[v(B2ℓ−1,2ℓ)/2ℓ]|
=
1
2ℓ
X

≤
X

2ℓ−1≤x<2ℓ
x| Pr[v(A) = x] −Pr[v(B) = x]|

x
| Pr[v(A) = x] −Pr[v(B) = x]|

=
2∥DA −DB∥≤2γ.

Thus, for each run of the algorithm which uses A t times,

∥MA −MB∥≤π2

√

3t√γ.

This is equivalent to the output of the algorithm being a probabilistic mixture of MB and some
other distribution M, where the probability of it being M is at most π2
√

3t√γ.

Algorithm 3 uses A T times in total. Each use of A is either within Algorithm 2 or one separate
sample from v(A) in Algorithm 3. We can similarly think of this sample as being taken from B,
except with probability at most γ ≤π2
√

3
√γ. Taking a union bound over all uses of A, we get the
claimed bound.

References

[1] D. Abrams and C. Williams. Fast quantum algorithms for numerical integrals and stochastic
processes, 1999. quant-ph/9908083.

[2] D. Aharonov. Quantum computation. In Annual Reviews of Computational Physics VI, chap-
ter 7, pages 259–346. World Scientiﬁc, 1998. quant-ph/9812037.

[3] D. Aharonov, A. Ambainis, J. Kempe, and U. Vazirani. Quantum walks on graphs. In Proc.
33rd Annual ACM Symp. Theory of Computing, pages 50–59, 2001. quant-ph/0012090.

[4] D. Aharonov, I. Arad, E. Eban, and Z. Landau.
Polynomial quantum algorithms for
additive approximations of the Potts model and other points of the Tutte plane, 2007.
quant-ph/0702008.

[5] D. Aharonov, A. Kitaev, and N. Nisan. Quantum circuits with mixed states. In Proc. 30th

Annual ACM Symp. Theory of Computing, pages 20–30, 1998.

24

## Page 25

[6] D. Aharonov and A. Ta-Shma.
Adiabatic quantum state generation.
SIAM J. Comput.,
37(1):47–82, 2007. quant-ph/0301023.

[7] I. Arad and Z. Landau. Quantum computation and the evaluation of tensor networks. SIAM
J. Comput., 39:3089–3121, 2010. arXiv:0805.0040.

[8] C. Bennett, E. Bernstein, G. Brassard, and U. Vazirani. Strengths and weaknesses of quantum
computing. SIAM J. Comput., 26(5):1510–1523, 1997. quant-ph/9701001.

[9] D. Berry, A. Childs, and R. Kothari. Hamiltonian simulation with nearly optimal dependence
on all parameters. In Proc. 56th Annual Symp. Foundations of Computer Science, pages 792–
809, 2015. arXiv:1501.01715.

[10] I. Bez´akov´a, D. ˇStefankoviˇc, V. Vazirani, and E. Vigoda. Accelerating simulated annealing
for the permanent and combinatorial counting problems. SIAM J. Comput., 37(5):1429–1454,
2008.

[11] G. Brassard, F. Dupuis, S. Gambs, and A. Tapp. An optimal quantum algorithm to approx-
imate the mean and its application for approximating the median of a set of points over an
arbitrary distance, 2011. arXiv:1106.4267.

[12] G. Brassard, P. Høyer, M. Mosca, and A. Tapp. Quantum amplitude ampliﬁcation and es-
timation. Quantum Computation and Quantum Information: A Millennium Volume, pages
53–74, 2002. quant-ph/0005055.

[13] S. Bravyi, A. W. Harrow, and A. Hassidim. Quantum algorithms for testing properties of
distributions. IEEE Trans. Inform. Theory, 57(6):3971–3981, 2011. arXiv:0907.3920.

[14] C.-F. Chiang, D. Nagaj, and P. Wocjan. Eﬃcient circuits for quantum walks. Quantum Inf.
Comput., 10(5&6):420–424, 2010. arXiv:0903.3465.

[15] P. Dagum, R. Karp, M. Luby, and S. Ross. An optimal algorithm for Monte Carlo estimation.
SIAM J. Comput., 29(5):1484–1496, 2000.

[16] G. De las Cuevas, W. D¨ur, M. van den Nest, and M. Martin-Delgado. Quantum algorithms
for classical lattice models. New J. Phys., 13:093021, 2011. arXiv:1104.2517.

[17] N. Destainville, B. Georgeot, and O. Giraud.
Quantum algorithm for exact Monte Carlo
sampling. Phys. Rev. Lett., 104:250502, 2010. arXiv:1003.1862.

[18] V. Dunjko and H. Briegel. Sequential quantum mixing for slowly evolving sequences of Markov
chains, 2015. arXiv:1503.01334.

[19] M. Dyer and A. Frieze. Computing the volume of convex bodies: a case where randomness
provably helps. In Probabilistic Combinatorics and Its Applications, volume 44 of Proceedings
of Symposia in Applied Mathematics, pages 123–170. American Mathematical Society, 1992.

[20] A. Frieze and E. Vigoda. A survey on the use of Markov chains to randomly sample colourings.
In Combinatorics, Complexity and Chance, pages 53–71. Oxford University Press, 2007.

[21] J. Geraci and D. Lidar. On the exact evaluation of certain instances of the Potts partition
function by quantum computers. Comm. Math. Phys., 279:735–768, 2008. quant-ph/0703023.

25

## Page 26

[22] J. Geraci and D. Lidar.
Classical Ising model test for quantum circuits.
New J. Phys.,
12:075026, 2010. arXiv:0902.4889.

[23] P. Glasserman. Monte Carlo methods in ﬁnancial engineering. Springer, New York, 2003.

[24] L. Grover. Quantum mechanics helps in searching for a needle in a haystack. Phys. Rev. Lett.,
79(2):325–328, 1997. quant-ph/9706033.

[25] L. Grover. A framework for fast quantum mechanical algorithms. In Proc. 30th Annual ACM
Symp. Theory of Computing, pages 53–62, 1998. quant-ph/9711043.

[26] O. Heilmann and E. Lieb. Theory of monomer-dimer systems. Comm. Math. Phys., 25:190–
232, 1972.

[27] S. Heinrich. Quantum summation with an application to integration. Journal of Complexity,
18(1):1–50, 2001. quant-ph/0105116.

[28] M. Huber. Approximation algorithms for the normalizing constant of Gibbs distributions,
2012. arXiv:1206.2689.

[29] M.
Huber.
Improving
Monte
Carlo
randomized
approximation
schemes,
2014.
arXiv:1411.4074.

[30] C. Jacoboni and P. Lugli.
The Monte Carlo method for semiconductor device simulation.
Springer-Verlag, Wien-New York, 1989.

[31] M. Jerrum. A very simple algorithm for estimating the number of k-colourings of a low-degree
graph. Random Structures and Algorithms, 7(2):157–165, 1995.

[32] M. Jerrum. Counting, sampling and integrating: algorithms and complexity. Birkh¨auser Verlag,
Basel, 2003.

[33] M. Jerrum and A. Sinclair. Approximating the permanent. SIAM J. Comput., 18(6):1149–
1178, 1989.

[34] M. Jerrum and A. Sinclair. Polynomial-time approximation algorithms for the Ising model.
SIAM J. Comput., 22(5):1087–1116, 1993.

[35] M. Jerrum, L. Valiant, and V. Vazirani. Random generation of combinatorial structures from
a uniform distribution. Theoretical Computer Science, 43(2–3):169–188, 1986.

[36] E. Knill, G. Ortiz, and R. Somma. Optimal quantum measurements of expectation values of
observables. Phys. Rev. A, 75:012328, 2007. quant-ph/0607019.

[37] W. Krauth. Statistical Mechanics: Algorithms and Computations. Oxford University Press,
Oxford, 2006.

[38] D. Levin, Y. Peres, and E. Wilmer. Markov chains and mixing times. American Mathematical
Society, 2009.

[39] D. Lidar. On the quantum computational complexity of the Ising spin glass partition function
and of knot invariants. New J. Phys., 6:167, 2004. quant-ph/0309064.

[40] D. Lidar and O. Biham. Simulating Ising spin glasses on a quantum computer. Phys. Rev. E,
56:3661, 1997. quant-ph/9611038.

26

## Page 27

[41] F. Martinelli. Lectures on Glauber dynamics for discrete spin models. In Lectures on probability
theory and statistics (Saint-Flour, 1997), volume 1717 of Lecture Notes in Mathematics, pages
93–191. Springer, 1997.

[42] F. Martinelli and E. Olivieri. Approach to equilibrium of Glauber dynamics in the one phase
region. Comm. Math. Phys., 161(3):447–486, 1994.

[43] A. Matsuo, K. Fujii, and N. Imoto. Quantum algorithm for an additive approximation of Ising
partition functions. Phys. Rev. A, 90:022304, 2014. arXiv:1405.2749.

[44] E. Mossel and A. Sly. Exact thresholds for Ising-Gibbs samplers on general graphs. The Annals
of Probability, 41(1):294–328, 2013.

[45] A. Nayak and F. Wu.
The quantum query complexity of approximating the median and
related statistics. In Proc. 31st Annual ACM Symp. Theory of Computing, pages 384–393,
1999. quant-ph/9804066.

[46] M. A. Nielsen and I. L. Chuang. Quantum Computation and Quantum Information. Cambridge
University Press, 2000.

[47] D. Poulin and P. Wocjan. Sampling from the thermal quantum Gibbs state and evaluating
partition functions with a quantum computer. Phys. Rev. Lett., 103:220502, 2009. 0905.2199.

[48] P. Richter. Quantum speedup of classical mixing processes. Phys. Rev. A, 76:042306, 2007.
quant-ph/0609204.

[49] R. Somma, S. Boixo, H. Barnum, and E. Knill. Quantum simulations of classical annealing
processes. Phys. Rev. Lett., 101(13):130504, 2008. arXiv:0804.1571.

[50] D. ˇStefankoviˇc, S. Vempala, and E. Vigoda. Adaptive simulated annealing: a new connection
between sampling and counting. J. ACM, 56(3):18:1–18:36, 2009. cs.DS/0612058.

[51] M. Szegedy. Quantum speed-up of Markov chain based algorithms. In Proc. 45th Annual
Symp. Foundations of Computer Science, pages 32–41, 2004. quant-ph/0401053.

[52] K. Temme, T. Osborne, K. Vollbrecht, D. Poulin, and F. Verstraete. Quantum Metropolis
sampling. Nature, 471:87–90, 2011. arXiv:0911.3635.

[53] R. Tucci. Use of quantum sampling to calculate mean values of observables and partition
function of a quantum system, 2009. arXiv:0912.4402.

[54] P. Valiant. Testing symmetric properties of distributions. SIAM J. Comput., 40(6):1927–1968,
2011.

[55] J. Valleau and D. Card. Monte Carlo estimation of the free energy by multistage sampling. J.
Chem. Phys., 57:5457, 1972.

[56] M. Van den Nest, W. D¨ur, R. Raussendorf, and H. Briegel. Quantum algorithms for spin
models and simulable gate sets for quantum computation. Phys. Rev. A, 80:052334, 2008.
arXiv:0805.1214.

[57] S. Venegas-Andraca. Quantum walks: a comprehensive review. Quantum Information Pro-
cessing, 11(5):1015–1106, 2012. arXiv:1201.4780.

27

## Page 28

[58] P. Wocjan and A. Abeyesinghe. Speedup via quantum sampling. Phys. Rev. A, 78:042336,
2008. arXiv:0804.4259.

[59] P. Wocjan, C.-F. Chang, D. Nagaj, and A. Abeyesinghe. Quantum algorithm for approximating
partition functions. Phys. Rev. A, 80:022340, 2009. arXiv:0811.0596.

[60] M.-H. Yung and A. Aspuru-Guzik. A quantum-quantum Metropolis algorithm. Proceedings
of the National Academy of Sciences, 109(3):754–759, 2012. arXiv:1011.1468.

28
