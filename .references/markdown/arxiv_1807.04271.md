---
source_pdf: ../arxiv_1807.04271.pdf
pages: 32
extracted_at: 2026-04-17T12:32:35+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_1807.04271

Source PDF: ../arxiv_1807.04271.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

A quantum-inspired classical algorithm for
recommendation systems

Ewin Tang

arXiv:1807.04271v3 [cs.IR] 9 May 2019

May 10, 2019

Abstract

We give a classical analogue to Kerenidis and Prakash’s quantum recommendation
system, previously believed to be one of the strongest candidates for provably expo-
nential speedups in quantum machine learning. Our main result is an algorithm that,
given an m × n matrix in a data structure supporting certain ℓ2-norm sampling op-
erations, outputs an ℓ2-norm sample from a rank-k approximation of that matrix in
time O(poly(k) log(mn)), only polynomially slower than the quantum algorithm. As a
consequence, Kerenidis and Prakash’s algorithm does not in fact give an exponential
speedup over classical algorithms. Further, under strong input assumptions, the clas-
sical recommendation system resulting from our algorithm produces recommendations
exponentially faster than previous classical systems, which run in time linear in m and
n.
The main insight of this work is the use of simple routines to manipulate ℓ2-norm
sampling distributions, which play the role of quantum superpositions in the classical
setting.
This correspondence indicates a potentially fruitful framework for formally
comparing quantum machine learning algorithms to classical machine learning algo-
rithms.

Contents

1
Introduction
2
1.1
Quantum Machine Learning . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.2
Recommendation Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.3
Algorithm Sketch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
1.4
Further Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7

2
Deﬁnitions
8
2.1
Low-Rank Approximations . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2
Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9

3
Data Structure
9

1

## Page 2

4
Main Algorithm
11
4.1
Vector Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
4.2
Finding a Low-Rank Approximation
. . . . . . . . . . . . . . . . . . . . . .
13
4.3
Proof of Theorem 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17

5
Application to Recommendations
19
5.1
Preference Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
5.2
Matrix Sampling
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
5.3
Proof of Theorem 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22

References
25

A Deferred Proofs
25

B Variant for an Alternative Model
30

1
Introduction

1.1
Quantum Machine Learning

This work stems from failed eﬀorts to prove that Kerenidis and Prakash’s quantum recom-
mendation system algorithm [KP17b] achieves an exponential speedup over any classical
algorithm. Such a result would be interesting because Kerenidis and Prakash’s algorithm is
a quantum machine learning (QML) algorithm.

Though QML has been studied since 1995 [BJ99], it has garnered signiﬁcant attention in
recent years, beginning in 2008 with Harrow, Hassidim, and Lloyd’s quantum algorithm
for solving linear systems [HHL09]. This burgeoning ﬁeld has produced exciting quantum
algorithms that give hope for ﬁnding exponential speedups outside of the now-established
gamut of problems related to period ﬁnding and Fourier coeﬃcients.
However, in part
because of caveats exposited by Aaronson [Aar15], it is not clear whether any known QML
algorithm gives a new exponential speedup over classical algorithms for practically relevant
instances of a machine learning problem.
Kerenidis and Prakash’s work was notable for
addressing all of these caveats, giving a complete quantum algorithm that could be compared
directly to classical algorithms.

When Kerenidis and Prakash’s work was published, their algorithm was exponentially faster
than the best-known classical algorithms. It was not known whether this was a provably
exponential speedup. The goal of this work is to describe a classical algorithm that performs
the same task as the quantum recommendation systems algorithm with only polynomially
slower runtime, thus answering this question.
This removes one of the most convincing
examples we have of exponential speedups for machine learning problems (see Section 6.7 of
Preskill’s survey for more context [Pre18]).

How the quantum algorithm works. Outside of the recommendation systems context,

2

## Page 3

the quantum algorithm just samples from the low-rank approximation of an input matrix.
It proceeds as follows. First, an application of phase estimation implicitly estimates singular
values and locates singular vectors of the input.
A quantum projection procedure then
uses this information to project a quantum state with a row of the input to a state with the
corresponding row of a low-rank approximation of the input. Measuring this state samples an
entry from the row with probability proportional to its magnitude. Kerenidis and Prakash
posited that, with a classical algorithm, producing samples following these distributions
requires time linear in the input dimensions.

The intuition behind this claim is not that singular value estimation or computing projections
is particularly diﬃcult computationally. Rather, it’s simply hard to believe that any of these
steps can be done without reading the full input. After all, a signiﬁcant portion of the theory
of low-rank matrix approximation only asks for time complexity linear in input-sparsity or
sublinear with some number of passes through the data. In comparison to these types of
results, what the quantum algorithm achieves (query complexity polylogarithmic in the input
size) is impressive.

With this claim in mind, Kerenidis and Prakash then apply their quantum algorithm to make
a fast online recommendation system. As information arrives about user-product preferences,
we place it into a dynamic data structure that is necessary to run the quantum algorithm.
We can then service requests for recommendations as they arrive by running the quantum
algorithm and returning the output sample. Under strong assumptions about the input data,
this sample is likely to be a good recommendation.

State preparation: the quantum algorithm’s assumption. To see why the classical
algorithm we present is possible, we need to consider the technique Kerenidis and Prakash
use to construct their relevant quantum states.

Kerenidis and Prakash’s algorithm is one of many QML algorithms [HHL09,LMR13,LMR14,
KP17a] that require quantum state preparation assumptions, which state that given an input
vector v, one can quickly form a corresponding quantum state |v⟩. To achieve the desired
runtime in practice, an implementation would replace this assumption with either a proce-
dure to prepare a state from an arbitrary input vector (where the cost of preparation could
be amortized over multiple runs of the algorithm) or a speciﬁcation of input vectors for which
quantum state preparation is easy. Usually QML algorithms abstract away these implemen-
tation details, assuming a number of the desired quantum states are already prepared. The
quantum recommendation systems algorithm is unique in that it explicitly comes with a
data structure to prepare its states (see Section 3).

These state preparation assumptions are nontrivial: even given ability to query entries of a
vector in superposition, preparing states corresponding to arbitrary length-n input vectors is
known to take Ω(√

n) time (a corollary of quantum search lower bounds [BBBV97]). Thus,
the data structure to quickly prepare quantum states is essential for the recommendation
systems algorithm to achieve query complexity polylogarithmic in input size.

How a classical algorithm can perform as well as the quantum algorithm. Our key
insight is that the data structure used to satisfy state preparation assumptions can also satisfy
ℓ2-norm sampling assumptions (deﬁned in Section 2.2). So, a classical algorithm whose goal

3

## Page 4

is to “match” the quantum algorithm can exploit these assumptions. The eﬀectiveness of ℓ2-
norm sampling in machine learning [SWZ16,HKS11] and randomized linear algebra [KV17,
DMM08] is well-established. In fact, a work by Frieze, Kannan, and Vempala [FKV04] shows
that, with ℓ2-norm sampling assumptions, a form of singular value estimation is possible in
time independent of m and n. Further, in the context of this literature, sampling from the
projection of a vector onto a subspace is not outside the realm of feasibility. This work just
puts these two pieces together.

The importance of ℓ2-norm sampling. In an imprecise sense, our algorithm replaces
state preparation assumptions with ℓ2-norm sampling assumptions. In this particular case,
while quantum superpositions served to represent data implicitly that would take linear
time to write out, this need can be served just as well with probability distributions and
subsamples of larger pieces of data.

The correspondence between ℓ2-norm sampling assumptions and state preparation assump-
tions makes sense. While the former sidesteps the obvious search problems inherent in linear
algebra tasks by pinpointing portions of vectors or matrices with the most weight, the latter
sidesteps these search problems by allowing for quantum states that are implicitly aware of
weight distribution. We suspect that this connection revealed by the state preparation data
structure is somewhat deep, and cannot be ﬁxed by simply ﬁnding a state preparation data
structure without sampling power.

This work demonstrates one major case where classical computing with ℓ2-norm sampling
is an apt point of comparison for revealing speedups (or, rather, the lack thereof) in QML.
We believe that this reference point remains useful, even for QML algorithms that don’t
specify state preparation implementation details, and thus are formally incomparable to any
classical model. So, we suggest a general framework for studying the speedups given by
QML algorithms with state preparation assumptions: compare QML algorithms with state
preparation to classical algorithms with sampling. Indeed, a QML algorithm using state
preparation assumptions should aim to surpass the capabilities of classical algorithms with
ℓ2-norm sampling, given that in theory, generic state preparation tends to only appear in
settings with generic sampling, and in practice, we already know how to implement fast
classical sampling on existing hardware.

In summary, we argue for the following guideline: when QML algorithms are compared to
classical ML algorithms in the context of ﬁnding speedups, any state preparation assumptions
in the QML model should be matched with ℓ2-norm sampling assumptions in the classical ML
model.

1.2
Recommendation Systems

In addition to our algorithm having interesting implications for QML, it also can be used as
a recommendation system.

To formalize the problem of recommending products to users, we use the following model, ﬁrst
introduced in 1998 by Kumar et al. [KRRT01] and reﬁned further by Azar et al. [AFK+01]

4

## Page 5

and Drineas et al. [DKR02]. We represent the sentiments of m users towards n products with
an m × n preference matrix T, where Tij is large if user i likes product j. We further assume
that T is close to a matrix of small rank k (constant or logarithmic in m and n), reﬂecting
the intuition that users tend to fall into a small number of classes based on their preferences.
Given a matrix A containing only a subset of entries of T, representing our incomplete
information about user-product preferences, our goal is to output high-value entries of T,
representing good recommendations.

Modern work on recommendation systems uses matrix completion to solve this (which works
well in practice1), but these techniques must take linear time to produce a recommendation.
Kerenidis and Prakash’s recommendation system (and, consequently, this work) follows in
an older line of research, which experiments with very strong assumptions on input with
the hope of ﬁnding a new approach that can drive down runtime to sublinear in m and n.
In Kerenidis and Prakash’s model, ﬁnding a good recommendation for a user i reduces to
sampling from the ith row of a low rank approximation of the subsampled data A, instead of
a low-rank completion. Using our classical analogue to Kerenidis and Prakash’s algorithm,
we can get recommendations in O(poly(k) polylog(m, n)) time, exponentially faster than the
best-known in the literature. Sublinear-time sampling for good recommendations has been
proposed before (see introduction of [DKR02]), but previous attempts to implement it failed
to circumvent the bottleneck of needing linear time to write down input-sized vectors.

For context, our model is most similar to the model given in 2002 by Drineas et al. [DKR02].
However, that algorithm’s main goal is minimizing the number of user preferences necessary
to generate good recommendations; we discuss in Appendix B how to adapt our algorithm
to that model to get similar results. Other approaches include combinatorial techniques
[KRRT01,APSPT05] and the use of mixture models [KS08].

We note two major assumptions present in our model that diﬀer from the matrix completion
setting. (The full list of assumptions is given in Section 5.) The ﬁrst assumption is that
our subsample A is contained in a data structure. This makes sense in the setting of an
online recommendation system, where we can amortize the cost of our preprocessing. Rec-
ommendation systems in practice tend to be online, so building a system that keeps data
in this data structure to satisfy this assumption seems reasonable. The second assumption
is that we know a constant fraction of the full preference matrix T. This is impractical
and worse than matrix completion, for which we can prove correctness given as little as an
˜Θ(
k

m+n) fraction of input data [Rec11]. This seems to be an issue common among works
reducing recommendation problems to low-rank matrix approximation [DKR02, AFK+01].
Nevertheless, we hope that this algorithm, by presenting a novel sampling-based technique
with a much faster asymptotic runtime, inspires improved practical techniques and provides
an avenue for further research.

1For practical recommendation systems, see Koren et al. [KBV09] for a high-level exposition of this
technique and Bell et al. [BK07] for more technical details.

5

## Page 6

1.3
Algorithm Sketch

We ﬁrst state the main result, a classical algorithm that can sample a high-value entry from
a given row of a low-rank approximation of a given matrix. The formal statement can be
found in Section 4.3.

Theorem (1, informal). Suppose we are given as input a matrix A supporting query and
ℓ2-norm sampling operations, a row i ∈[m], a singular value threshold σ, an error parameter
η > 0, and a suﬃciently small ε > 0. There is a classical algorithm whose output distribution
is ε-close in total variation distance to the distribution given by ℓ2-norm sampling from the
ith row of a low-rank approximation D of A in query and time complexity

O

poly
∥A∥F

σ
, 1

ε, 1

where the quality of D depends on η and ε.


,

η, ∥Ai∥

∥Di∥

This makes the runtime independent of m and n. Here, (∥A∥F/σ)2 is a bound on the rank
of the low-rank approximation, so we think of σ as something like ∥A∥F/
√

k. To implement
the needed sampling operations, we will use the data structure described in Section 3, which
adds at most an additional O(log(mn)) factor in overhead. This gives a time complexity of

˜O
 ∥A∥24
F


.

σ24ε12η6 log(mn)∥Ai∥2

∥Di∥2

This is a large slowdown versus the quantum algorithm in some exponents. However, we
suspect that these exponents can be improved with existing techniques.

The only diﬀerence between Theorem 1 and its quantum equivalent in [KP17b] is that the
quantum algorithm has only logarithmic dependence2 on ε.
Thus, we can say that our
algorithm performs just as well, up to polynomial slowdown and ε approximation factors.
These ε’s don’t aﬀect the classical recommendation system guarantees:

Theorem (2, informal). Applying Theorem 1 to the recommendation systems model with
the quantum state preparation data structure achieves identical bounds on recommendation
quality as the quantum algorithm in [KP17b] up to constant factors, for suﬃciently small ε.

To prove Theorem 1 (Section 4), we present and analyze Algorithm 3. It combines a variety
of techniques, all relying on sampling access to relevant input vectors. The main restriction
to keep in mind is that we need to perform linear algebra operations without incurring the
cost of reading a full row or column.

The algorithm begins by using the given support for ℓ2-norm sampling to run a sampling
routine (called ModFKV, see Section 4.2) based on Frieze, Kannan, and Vempala’s 1998
algorithm [FKV04] to ﬁnd a low-rank approximation of A. It doesn’t have enough time
to output the matrix in full; instead, it outputs a succinct description of the matrix. This

2The analysis of the phase estimation in the original paper has some ambiguities, but subsequent work
[GSLW18] demonstrates that essentially the same result can be achieved with a diﬀerent algorithm.

6

## Page 7

description is S, a normalized constant-sized subset of rows of A, along with some constant-
sized matrices ˆU and ˆΣ, which implicitly describe ˆV := ST ˆU ˆΣ−1, a matrix whose columns
are approximate right singular vectors of A. The corresponding low-rank approximation
is D := AˆV ˆV T, an approximate projection of the rows of the input matrix onto the low-
dimensional subspace spanned by ˆV . Though computing ˆV directly takes too much time,
we can sample from and query to its columns. Since rows of S are normalized rows of A, we
have sampling access to S with our input data structure. We can translate such samples to
samples from ˆV using the simple sampling routines discussed in Section 4.1.

Though we could use this access to ˆV for the rest of our algorithm, we take a more direct
approach. To sample from the ith row of D Ai(ST ˆU ˆΣ−1)(ST ˆU ˆΣ−1)T given D’s description,
we ﬁrst estimate AiST. This amounts to estimating a constant number of inner products and
can be done with sampling access to Ai by Proposition 4.2. Then, we multiply this estimate
by ˆU ˆΣ−1(ˆΣ−1)T ˆUT, which is a constant-sized matrix. Finally, we sample from the product of
the resulting vector with S and output the result. This step uses rejection sampling: given
the ability to sample and query to a constant-sized set of vectors (in this case, rows of S),
we can sample from a linear combination of them (Proposition 4.3).

This completes the broad overview of the algorithm. The correctness and runtime analysis
is elementary; most of the work is in showing that ModFKV’s various outputs truly behave
like approximate large singular vectors and values (Proposition 4.6 and Theorem 4.7).

To prove Theorem 2 and show that the quality bounds on the recommendations are the
same (see Section 5.3), we just follow Kerenidis and Prakash’s analysis and apply the model
assumptions and theorems (Section 5) in a straightforward manner. The ℓ2-norm sampling
operations needed to run Algorithm 3 are instantiated with the data structure Kerenidis and
Prakash use (Section 3).

1.4
Further Questions

Since this algorithm is associated both with recommendation systems and quantum machine
learning, two lines of questioning naturally follow.

First, we can continue to ask whether any quantum machine learning algorithms have prov-
ably exponential speedups over classical algorithms. We believe that a potentially enlight-
ening approach is to investigate how state preparation assumptions can be satisﬁed and
whether they are in some way comparable to classical sampling assumptions. After all, we
ﬁnd it unlikely that a quantum exponential speedup can be reinstated just with a better
state preparation data structure. However, we are unaware of any research in this area in
particular, which could formalize a possible connection between QML algorithms with state
preparation assumptions and classical ML algorithms with sampling assumptions.

Second, while the recommendation system algorithm we give is asymptotically exponentially
faster than previous algorithms, there are several aspects of this algorithm that make direct
application infeasible in practice. First, the model assumptions are somewhat constrictive. It
is unclear whether the algorithm still performs well when such assumptions are not satisﬁed.

7

## Page 8

Second, the exponents and constant factors are large (mostly as a result of using Frieze,
Kannan, and Vempala’s algorithm [FKV04]). We believe that the “true” exponents are much
smaller and could result from more sophisticated techniques (see, for example, [DV06]).

2
Deﬁnitions

Throughout, we obey the following conventions. We assume that basic operations on input
data (e.g. adding, multiplying, reading, and writing) take O(1) time.
[n] := {1, . . . , n}.
f ≲g denotes the ordering f = O(g) (and correspondingly for ≳and ≂). For a matrix
A, Ai and A(i) will refer to its ith row and column, respectively. ∥A∥F and ∥A∥2 will refer
to Frobenius and spectral norm, respectively. Norm of a vector v, denoted ∥v∥, will always
refer to ℓ2-norm. The absolute value of x ∈R will be denoted |x|. Occasionally, matrix and
vector inequalities of the form ∥x −y∥≤ε will be phrased in the form x = y + E, where
∥E∥≤ε. Thus, the letter E will always refer to some form of perturbation or error.

For a matrix A ∈Rm×n, let A = UΣV T = Pmin m,n
i=1
σiuivT
i be the SVD of A. Here, U ∈Rm×m

and V ∈Rn×n are unitary matrices with columns {ui}i∈[m] and {vi}i∈[n], the left and right
singular vectors, respectively. Σ ∈Rm×n is diagonal with σi := Σii and the σi nonincreasing
and nonnegative.

We will use the function ℓto indicate splitting the singular vectors along a singular value:

ℓ(λ) := max{i | σi ≥λ}.

For example, σ1 through σℓ(λ) gives all of the singular values that are at least λ. This notation
suppresses ℓ’s dependence on σi, but it will always be clear from context.

Π will always refer to an orthogonal projector. That is, if β = {b1, . . . , bd} is an orthonormal
basis for im Π, then Π = Pd
i=1 bibT
i = BBT for B the matrix whose columns are the elements
of β. We will often conﬂate B, the matrix of basis vectors, and the basis β itself.

2.1
Low-Rank Approximations

We will use various techniques to describe low-rank approximations of A.
All of these
techniques will involve projecting the rows onto some span of right singular vectors.

Ak := AΠk
im Πk := span{vi | i ∈[k]}
Aσ := AΠσ
im Πσ := span{vi | i ∈[ℓ(σ)]}

Ak and Aσ correspond to the standard notions of low-rank approximations of A.
Thus,
Ak = Pk
i=1 σiuivT
i and is a rank-k matrix minimizing the Frobenius norm distance from A.
Similarly, Aσ is just At for t = ℓ(σ). Notice that rank A ∥A∥F

λ ≤λ.

√

We will need to relax this notion for our purposes, and introduce error η ∈[0, 1]. Deﬁne
Aσ,η := APσ,η where Pσ,η is some Hermitian matrix satisfying Πσ(1+η) ⪯Pσ,η ⪯Πσ(1−η)

8

## Page 9

and ⪯is the Loewner order.
In words, Aσ,η is the class of matrices “between” Aσ(1+η)
and Aσ(1−η): Pσ,η is the identity on vi’s with i ≤ℓ(σ(1 + η)), the zero map on vi’s with
i > ℓ(σ(1 −η)), and some PSD matrix with norm at most on the subspace spanned by vi’s
with i ∈(ℓ(σ(1+η)), ℓ(σ(1−η))]. Such a form of error could arise from having η-like error in
estimating the singular values used to compute a low-rank matrix approximation. η should
be thought of as constant (1/5 will be the eventual value), and σ should be thought of as
very large (say, a constant multiple of ∥A∥F), so Aσ,η always has low rank.

2.2
Sampling

For a nonzero vector x ∈Rn, we denote by Dx the distribution over [n] whose probability
density function is

Dx(i) =
x2
i

∥x∥2

We will call a sample from Dx a sample from x.

We make two basic observations. First, Dx is the distribution resulting from measuring the
quantum state |x⟩:=
1

∥x∥
P xi |i⟩in the computational basis. Second, sampling access to
Dx makes easy some tasks that are hard given just query access to x. For example, while
ﬁnding a hidden large entry of x ∈Rn takes Ω(n) queries with just query access, it takes a
constant number of samples with query and sample access.

In all situations, sampling access will be present alongside query access, and accordingly, we
will conﬂate samples i ∼Dx with the corresponding entries xi. Note that knowledge of ∥x∥is
also relevant and useful in this sampling context, since it allows for computing probabilities
from Dx and yet is hard to compute even with query and sampling access to x.

For probability distributions P, Q (as density functions) over a (discrete) universe X, the
total variation distance between them is deﬁned as

X

∥P −Q∥TV := 1

2

x∈X

P(x) −Q(x)
.

For a set S, we denote pulling an s ∈S uniformly at random by s ∼u S. We will continue
to conﬂate a distribution with its density function.

3
Data Structure

Since we are interested in achieving sublinear bounds for our algorithm, we need to concern
ourselves with how the input is given.

In the recommendation systems context, entries correspond to user-product interactions, so
we might expect that the input matrix A ∈Rm×n is given as an unordered stream of entries
(i, j, Aij). However, if the entries are given in such an unprocessed format, then clearly linear

9

## Page 10

time is required even to parse the input into a usable form. Even when the input is relatively
structured (for example, if we are given the known entries of T sorted by row and column),
there is no hope to sample the low-rank approximation of a generic matrix in sublinear time
because of the time needed to locate a nonzero entry.

To avoid these issues, we will instead consider our input matrix stored in a low-overhead
data structure. We deﬁne it ﬁrst for a vector, then for a matrix.

Lemma 3.1. There exists a data structure storing a vector v ∈Rn with w nonzero entries
in O(w log(n)) space, supporting the following operations:

• Reading and updating an entry of v in O(log n) time;

• Finding ∥v∥2 in O(1) time;

• Sampling from Dv in O(log n) time.

∥v∥2

v2
1 + v2
2
v2
3 + v2
4

v2
1
v2
2
v2
3
v2
4

sgn(v1)
sgn(v2)
sgn(v3)
sgn(v4)

Figure 1: Binary search tree (BST) data structure for v ∈R4. The leaf nodes store vi via its
weight v2
i and sign sgn(vi), and the weight of an interior node is just the sum of the weights
of its children. To update an entry, update all of the nodes above the corresponding leaf.
To sample from Dv, start from the top of the tree and randomly recurse on a child with
probability proportional to its weight. To take advantage of sparsity, prune the tree to only
nonzero nodes.

Proposition 3.2. Consider a matrix A ∈Rm×n. Let ˜A ∈Rm be a vector whose ith entry
is ∥Ai∥. There exists a data structure storing a matrix A ∈Rm×n with w nonzero entries in
O(w log mn) space, supporting the following operations:

• Reading and updating an entry of A in O(log mn) time;

• Finding ˜Ai in O(log m) time;

• Finding ∥A∥2
F in O(1) time;

• Sampling from D ˜
A and DAi in O(log mn) time.

This can be done by having a copy of the data structure speciﬁed by Lemma 3.1 for each
row of A and ˜A (which we can think of as the roots of the BSTs for A’s rows). This has

10

## Page 11

all of the desired properties, and in fact, is the data structure Kerenidis and Prakash use
to prepare arbitrary quantum states (Theorem A.1 in [KP17b]). Thus, our algorithm can
operate on the same input, although any data structure supporting the operations detailed
in Proposition 3.2 will also suﬃce.

This data structure and its operations are not as ad hoc as they might appear. The operations
listed above appear in other work as an eﬀective way to endow a matrix with ℓ2-norm
sampling assumptions [DKR02,FKV04].

4
Main Algorithm

Our goal is to prove Theorem 1:

Theorem (1). There is a classical algorithm that, given a matrix A with query and sampling
assumptions as described in Proposition 3.2, along with a row i ∈[m], threshold σ, η ∈(0, 1],
and suﬃciently small ε > 0, has an output distribution ε-close in total variation distance
to DDi where D ∈Rm×n satisﬁes ∥D −Aσ,η∥F ≤ε∥A∥F for some Aσ,η, in query and time
complexity

O

poly
∥A∥F

σ
, 1

ε, 1


.

η, ∥Ai∥

∥Di∥

We present the algorithm (Algorithm 3) and analysis nonlinearly. First, we give two algo-
rithms that use ℓ2-norm sampling access to their input vectors to perform basic linear algebra.
Second, we present ModFKV, a sampling algorithm to ﬁnd the description of a low-rank
matrix approximation. Third, we use the tools we develop to get from this description to
the desired sample.

4.1
Vector Sampling

Recall how we deﬁned sampling from a vector.

Deﬁnition. For a vector x ∈Rn, we denote by Dx the distribution over [n] with density
function Dx(i) = x2
i /∥x∥2. We call a sample from Dx a sample from x.

We will need that closeness of vectors in ℓ2-norm implies closeness of their respective distri-
butions in TV distance:

Lemma 4.1. For x, y ∈Rn satisfying ∥x −y∥≤ε, the corresponding distributions Dx, Dy
satisfy ∥Dx −Dy∥TV ≤2ε/∥x∥.

11

## Page 12

Proof. Let ˆx and ˆy be the normalized vectors x/∥x∥and y/∥y∥.

n
X

ˆx2
i −ˆy2
i
= 1

2
|ˆx −ˆy|, |ˆx + ˆy|
≤1

∥Dx −Dy∥TV = 1

2

i=1

2∥ˆx −ˆy∥∥ˆx + ˆy∥

x −y −(∥x∥−∥y∥)ˆy
≤
1

≤∥ˆx −ˆy∥=
1

∥x∥


∥x −y∥+
∥x∥−∥y∥

≤2ε

∥x∥

∥x∥

The ﬁrst inequality follows from Cauchy-Schwarz, and the rest follow from triangle inequality.

Now, we give two subroutines that can be performed, assuming some vector sampling access.
First, we show that we can estimate the inner product of two vectors well.

Proposition 4.2. Given query access to x, y ∈Rn, sample access to Dx, and knowledge of
∥x∥, ⟨x, y⟩can be estimated to additive error ∥x∥∥y∥ε with at least 1 −δ probability using
O( 1

ε2 log 1

δ) queries and samples (and the same time complexity).

Proof. Perform samples in the following way: for each i, let the random variable Z be yi/xi
with probability x2
i /∥x∥2 (so we sample i from Dx). We then have:

E[Z] =
X yi

x2
i

xi

Var[Z] ≤
X yi

2
x2
i

xi

∥x∥2 =
P xiyi

∥x∥2
= ⟨x, y⟩

∥x∥2 ,

∥x∥2 =
P y2
i

∥x∥2 = ∥y∥2

∥x∥2.

Since we know ∥x∥, we can normalize by it to get a random variable whose mean is ⟨x, y⟩
and whose standard deviation is σ = ∥x∥∥y∥.

The rest follows from standard techniques: we take the median of 6 log 1

δ copies of the mean
of
9

2ε2 copies of Z to get within εσ = ε∥x∥∥y∥of ⟨x, y⟩with probability at least 1 −δ in
O( 1

ε2 log 1

δ) accesses. All of the techniques used here take linear time.

Second, we show that, given sample access to some vectors, we can sample from a linear
combination of them.

Proposition 4.3. Suppose we are given query and sample access to the columns of V ∈Rn×k,
along with their norms. Then given w ∈Rk (as input), we can output a sample from V w in
O(k2C(V, w)) expected query complexity and expected time complexity, where

C(V, w) :=
Pk
i=1 ∥wiV (i)∥2

∥V w∥2
.

C measures the amount of cancellation for V w. For example, when the columns of V are
orthogonal, C = 1 for all nonzero w, since there is no cancellation. Conversely, when the
columns of V are linearly dependent, there is a choice of nonzero w such that ∥V w∥= 0,
maximizing cancellation.
In this context, C is undeﬁned, which matches with sampling
from the zero vector also being undeﬁned. By perturbing w we can ﬁnd vectors requiring
arbitrarily large values of C.

12

## Page 13

Proof. We use rejection sampling: see Algorithm 1. Given sampling access to a distribution
P, rejection sampling allows for sampling from a “close” distribution Q, provided we can
compute some information about their corresponding distributions.

Algorithm 1: Rejection Sampling

Pull a sample s from P;
Compute rs =
Q(s)

MP (s) for some constant M;
Output s with probability rs and restart otherwise;

If ri ≤1 for all i, then the above procedure is well-deﬁned and outputs a sample from Q in
M iterations in expectation.3

In our case, P is the distribution formed by ﬁrst sampling a row j with probability propor-
tional to ∥wjV (j)∥2 and then sampling from DV (j); Q is the target DV w. We choose

ri =
(V w)2
i

k Pk
j=1(Vijwj)2,

which we can compute in k queries4. This expression is written in a way the algorithm can
directly compute, but it can be put in the form of the rejection sampling procedures stated
above:

M =
Q(i)k Pk
j=1(Vijwj)2

P(i)(V w)2
i
=
k(Pk
j=1 ∥wjV (j)∥2)

∥V w∥2
= kC(V, w).

M is independent of i, so it is a constant as desired. To prove correctness, all we need to
show is that our choice of ri is always at most 1. This follows from Cauchy-Schwarz:

k Pk
j=1(Vijwj)2 =
(Pk
j=1 Vijwj)2

ri =
(V w)2
i

k Pk
j=1(Vijwj)2 ≤1.

Each iteration of the procedure takes O(k) queries, leading to a query complexity of O(k2C(V, w)).
Time complexity is linear in the number of queries.

4.2
Finding a Low-Rank Approximation

Now, we describe the low-rank approximation algorithm that we use at the start of the main
algorithm.

3The number of iterations is a geometric random variable, so this can be converted into a bound guar-
anteeing a sample in M log 1/δ iterations with failure probability 1 −δ, provided the algorithm knows M.
All expected complexity bounds we deal with can be converted to high probability bounds in the manner
described.
4Notice that we can compute ri without directly computing the probabilities Q(i). This helps us because
computing Q(i) involves computing ∥V w∥, which is nontrivial.

13

## Page 14

Theorem 4.4. Given a matrix A ∈Rm×n supporting the sample and query operations de-
scribed in Proposition 3.2, along with parameters σ ∈(0, ∥A∥F], ε ∈(0,
p

σ/∥A∥F/4], η ∈
[ε2, 1], there is an algorithm that outputs a succinct description (of the form described below)
of some D satisfying ∥D −Aσ,η∥F ≤ε∥A∥F with probability at least 1 −δ and

O

poly
∥A∥2
F

σ2
, 1

ε, 1

query and time complexity.



η, log 1

δ

To prove this theorem, we modify the algorithm given by Frieze, Kannan, and Vempala
[FKV04] and show that it satisﬁes the desired properties. The modiﬁcations are not crucial
to the correctness of the full algorithm: without them, we simply get a diﬀerent type of
low-rank approximation bound. They come into play in Section 5 when proving guarantees
about the algorithm as a recommendation system.

Algorithm 2: ModFKV

Input: Matrix A ∈Rm×n supporting operations in Proposition 3.2, threshold σ, error
parameters ε, η
Output: A description of an output matrix D
Set K = ∥A∥2
F/σ2 and ¯ε = ηε2;
Set q = Θ
K4

¯ε2

;
Sample rows i1, . . . , iq from D ˜
A;
Let F denote the distribution given by choosing an s ∼u [q], and choosing a column
from DAis;
Sample columns j1, . . . , jq from F;
Let W be the resulting q × q row-and-column-normalized submatrix
Wrc :=
Airjc

q√

D ˜
A(ir)F(jc);

Compute the left singular vectors of W u(1), . . . , u(k) that correspond to singular
values σ(1), . . . , σ(k) larger than σ;
Output i1, . . . , iq, ˆU ∈Rq×k the matrix whose ith column is u(i), and ˆΣ ∈Rk×k the
diagonal matrix whose ith entry on the diagonal is σ(i). This is the description of the
output matrix D;

The algorithm, ModFKV, is given in Algorithm 2. It subsamples the input matrix, computes
the subsample’s large singular vectors and values, and outputs them with the promise that
they give a good description of the singular vectors of the full matrix.
We present the
algorithm as the original work does, aiming for a constant failure probability. This can be
ampliﬁed to δ failure probability by increasing q by a factor of O(log 1

δ) (the proof uses a
martingale inequality; see Theorem 1 of [DKM06]). More of the underpinnings are explained
in Frieze, Kannan, and Vempala’s paper [FKV04].

We get the output matrix D from its description in the following way. Let S be the submatrix
given by restricting the rows to i1, . . . , iq and renormalizing row i by 1/
p

qD ˜
A(i) (so they all
have the same norm). Then ˆV := ST ˆU ˆΣ−1 ∈Rn×k is our approximation to the large right

14

## Page 15

singular vectors of A; this makes sense if we think of S, ˆU, and ˆΣ as our subsampled low-rank
approximations of A, U, and Σ (from A’s SVD). Appropriately, D is the “projection” of A
onto the span of ˆV :
D := AˆV ˆV T = AST ˆU ˆΣ−2 ˆUT S.

The query complexity of ModFKV is dominated by querying all of the entries of W, which
is O(q2), and the time complexity is dominated by computing W’s SVD, which is O(q3). We
can convert this to the input parameters using that q = O( ∥A∥8

σ8ε4η2).

ModFKV diﬀers from FKV only in that σ is taken as input instead of k, and is used as the
threshold for the singular vectors. As a result of this change, K replaces k in the subsampling
steps, and σ replaces k in the SVD step. Notice that the number of singular vectors taken
(denoted k) is at most K, so in eﬀect, we are running FKV and just throwing away some of
the smaller singular vectors. Because we ignore small singular values that FKV had to work
to ﬁnd, we can sample a smaller submatrix, speeding up our algorithm while still achieving
an analogous low-rank approximation bound:

Lemma 4.5. The following bounds hold for the output matrix D (here, k is the width of
ˆV , and thus a bound on rank D):

∥A −D∥2
F ≤∥A −Ak∥2
F + ¯ε∥A∥2
F
(♦)

and ℓ((1 + ¯ε
√

K)σ) ≤k ≤ℓ((1 −¯ε
√

K)σ).
(♥)

The following property will be needed to prove correctness of ModFKV and Algorithm 3.
The estimated singular vectors in ˆV behave like singular vectors, in that they are close to
orthonormal.

Proposition 4.6. The output vectors ˆV satisfy

∥ˆV −Λ∥F = O(¯ε)

for Λ a set of orthonormal vectors with the same image as ˆV .

As an easy corollary, ˆV ˆV T is O(¯ε)-close in Frobenius norm to the projector ΛΛT, since
ˆV ˆV T = (Λ + E)(Λ + E)T and ∥ΛET∥F = ∥EΛT∥F = ∥E∥F. The proofs of the above lemma
and proposition delve into FKV’s analysis, so we defer them to the appendix.

The guarantee on our output matrix D is (♦), but for our recommendation system, we want
that D is close to some Aσ,η. Now, we present the core theorem showing that the former
kind of error implies the latter.

Theorem 4.7. If Π a k-dimensional orthogonal projector satisﬁes

∥Ak∥2
F ≤∥AΠ∥2
F + εσ2
k,

then
∥AΠ −Aσk,η∥2
F ≲εσ2
k/η,

where ε ≤η ≤1.5

5An analogous proof gives the more general bound ∥Π −Pσ,η∥2
F ≲ε/η.

15

## Page 16

The proof is somewhat involved, so we defer it to the appendix. To our knowledge, this is a
novel translation of a typical FKV-type bound as in (♦) to a new, useful type of bound, so
we believe this theorem may ﬁnd use elsewhere. Now, we use this theorem to show that D
is close to some Aσ,η.

Corollary 4.8. ∥D −Aσ,η∥F ≲ε∥A∥F/√

η.

Proof. Throughout the course of this proof, we simplify and apply theorems based on the
restrictions on the parameters in Theorem 4.4.

First, notice that the bound (♦) can be translated to the type of bound in the premise of
Theorem 4.7, using Proposition 4.6.

∥A −D∥2
F ≤∥A −Ak∥2
F + ¯ε∥A∥2
F
∥A −A(ΛΛT + E)∥2
F ≤∥A −Ak∥2
F + ¯ε∥A∥2
F
(∥A −AΛΛT∥F −¯ε∥A∥F)2 ≲∥A −Ak∥2
F + ¯ε∥A∥2
F
∥A∥2
F −∥AΛΛT∥2
F ≲∥A∥2
F −∥Ak∥2
F + ¯ε∥A∥2
F
∥Ak∥2
F ≲∥AΛΛT∥2
F + (¯ε∥A∥2
F/σ2
k)σ2
k

The result of the theorem is that

AΛΛT −Aσk, η−¯ε
√

2

1−¯ε
√

K

The bound on k (♥) implies that any Aσk, η−¯ε
√

1−¯ε
√

contained in the latter), so we can conclude

F ≲(¯ε∥A∥2
F/σ2
k)σ2
k

K
≲¯ε

η∥A∥2
F.

1−¯ε
√

K is also an Aσ,η (the error of the former is

∥D −Aσ,η∥F ≲∥AΛΛT −Aσ,η∥F + ¯ε∥A∥F ≲
r

¯ε

η∥A∥F.

¯ε was chosen so that the ﬁnal term is bounded by ε∥A∥F.

This completes the proof of Theorem 4.4.

To summarize, after this algorithm we are left with the description of our low-rank approx-
imation D = AST ˆUΣ−2 ˆUT S, which will suﬃce to generate samples from rows of D.
It
consists of the following:

• ˆU ∈Rq×k, explicit orthonormal vectors;

• ˆΣ ∈Rk×k, an explicit diagonal matrix whose diagonal entries are in (σ, ∥A∥F];

• S ∈Rq×n, which is not output explicitly, but whose rows are rows of A normalized to
equal norm ∥A∥F/√

q (so we can sample from S’s rows); and

• ˆV ∈Rn×k, a close-to-orthonormal set of vectors implicitly given as ST ˆU ˆΣ−1.

16

## Page 17

4.3
Proof of Theorem 1

Theorem 1. There is a classical algorithm that, given a matrix A with query and sampling
assumptions as described in Proposition 3.2, along with a row i ∈[m], threshold σ, η ∈(0, 1],
and suﬃciently small ε > 0, has an output distribution ε-close in total variation distance
to DDi where D ∈Rm×n satisﬁes ∥D −Aσ,η∥F ≤ε∥A∥F for some Aσ,η, in query and time
complexity

O

poly
∥A∥F

σ
, 1

ε, 1


.

η, ∥Ai∥

∥Di∥

Proof. We will give an algorithm (Algorithm 3) where the error in the output distribution is
O(ε∥Ai∥/∥Di∥)-close to DDi, and there is no dependence on ∥Ai∥/∥Di∥in the runtime, and
discuss later how to modify the algorithm to get the result in the theorem.

Algorithm 3: Low-rank approximation sampling

Input: Matrix A ∈Rm×n supporting the operations in 3.2, user i ∈[m], threshold σ,
ε > 0, η ∈(0, 1]
Output: Sample s ∈[n]
Run ModFKV (2) with parameters (σ, ε, η) to get a description of
D = AˆV ˆV T = AST ˆU ˆΣ−2 ˆUT S;
Estimate AiST entrywise by using Proposition 4.2 with parameter
ε

K to estimate
⟨Ai, ST
t ⟩for all t ∈[q]. Let est be the resulting 1 × q vector of estimates;
Compute est ˆU ˆΣ−2 ˆUT with matrix-vector multiplication;
Sample s from (est ˆU ˆΣ−2 ˆUT)S using Proposition 4.3;
Output s;

√

Correctness: By Theorem 4.4, for suﬃciently small6 ε, the output matrix D satisﬁes

∥D −Aσ,η∥F ≤ε∥A∥F.

So, all we need is to approximately sample from the ith row of D, given its description.

Recall that the rows of ST
t have norm ∥A∥F/√

q. Thus, the guarantee from Proposition 4.2
states that each estimate of an entry has error at most
ε

Kq∥Ai∥∥A∥F, meaning that ∥est −

√

K∥Ai∥∥A∥F. Further, using that ˆV is close to orthonormal (Proposition 4.6) and

AiST∥≤
ε

√

∥ˆUΣ−1∥≤1

σ, we have that the vector we sample from is close to Di:

∥(est −AiST) ˆUΣ−1 ˆV T∥≤(1 + O(ε2))∥est ˆUΣ−1 −AiST ˆUΣ−1∥

≲1

η,
p

6This is not a strong restriction: ε ≲min{√

σ∥est −AiST∥≤
ε

σ
√

K
∥Ai∥∥A∥F = ε∥Ai∥

σ/∥A∥F} works. This makes sense: for ε any larger, the
error can encompass addition or omission of full singular vectors.

17

## Page 18

Finally, by Lemma 4.1, we get the desired bound: that the distance from the output distri-
bution to DDi is O(ε∥Ai∥/∥Di∥).

Runtime: Applying Proposition 4.2 q times takes O( Kq

ε2 log q

δ) time; the naive matrix-vector
multiplication takes O(Kq) time; and applying Proposition 4.3 takes time O(Kq2), since

Pq
j=1 ∥(est ˆU ˆΣ−2 ˆUT )jSj∥2

∥est ˆU ˆΣ−2 ˆUT S∥2
≤∥est ˆU ˆΣ−2 ˆUT∥2∥S∥2
F

C(ST, ˆU ˆΣ−2 ˆUT estT) =

∥est ˆU ˆΣ−2 ˆUTS∥2

≤
∥ˆΣ−1 ˆUT ∥2∥S∥2
F

minx:∥x∥=1 ∥xΣ−1 ˆUTS∥2 ≲
∥A∥2
F

σ2(1 −ε2)2 = O(K)

using Cauchy-Schwarz, Proposition 4.6, and the basic facts about D’s description7.

The query complexity is dominated by the use of Proposition 4.3 and the time complexity
is dominated by the O(q3) SVD computation in ModFKV, giving

Query complexity = ˜O
∥A∥2
F

σ2

2
= ˜O
 ∥A∥18
F



 ∥A∥8
F

σ8ε4η2

σ18ε8η4

Time complexity = ˜O
 ∥A∥24
F


,

σ24ε12η6

where the ˜O hides the log factors incurred by amplifying the failure probability to δ.

Finally, we brieﬂy discuss variants of this algorithm.

• To get the promised bound in the theorem statement, we can repeatedly estimate AiST

(creating est1, est2, etc.) with exponentially decaying ε, eventually reducing the error
of the ﬁrst step to O(ε∥AiST∥). This procedure decreases the total variation error
to O(ε) and increases the runtime by ˜O(∥Ai∥2/∥Di∥2), as desired. Further, we can
ignore δ by choosing δ = ε and outputting an arbitrary s ∈[n] upon failure. This only
changes the output distribution by ε in total variation distance and increase runtime
by polylog 1

ε.

• While the input is a row i ∈[m] (and thus supports query and sampling access), it need
not be. More generally, given query and sample access to orthonormal vectors V ∈
Rn×k, and query access to x ∈Rn, one can approximately sample from a distribution
O(ε∥x∥/∥V V T x∥)-close to DV V T x, the projection of x onto the span of V , in O( k2

ε2 log k

δ)
time.

• While the SVD dominates the time complexity of Algorithm 3, the same description
output by ModFKV can be used for multiple recommendations, amortizing the cost
down to the query complexity (since the rest of the algorithm is linear in the number
of queries).

7We have just proved that, given D’s description, we can sample from any vector of the form ˆV x in
O(Kq2) time.

18

## Page 19

5
Application to Recommendations

We now go through the relevant assumptions necessary to apply Theorem 1 to the recom-
mendation systems context. As mentioned above, these are the same assumptions as those
in [KP17b]: an exposition of these assumptions is also given there. Then, we prove Theo-
rem 2, which shows that Algorithm 3 gives the same guarantees on recommendations as the
quantum algorithm.

5.1
Preference Matrix

Recall that given m users and n products, the preference matrix T ∈Rm×n contains the
complete information on user-product preferences. For ease of exposition, we will assume
the input data is binary:

Deﬁnition. If user i likes product j, then Tij = 1. If not, Tij = 0.

We can form such a preference matrix from generic data about recommendations, simply
by condensing information down to the binary question of whether a product is a good
recommendation or not.8

We are typically given only a small subsample of entries of T (which we learn when a user
purchases or otherwise interacts with a product). Then, ﬁnding recommendations for user i
is equivalent to ﬁnding large entries of the ith row of T given such a subsample.

Obviously, without any restrictions on what T looks like, this problem is ill-posed. We make
this problem tractable by assuming that T is close to a matrix of small rank k.

T is close to a low-rank matrix. That is, ∥T −Tk∥F ≤ρ∥T∥F for some k and ρ ≪1. k
should be thought of as constant (at worst, polylog(m, n)). This standard assumption comes
from the intuition that users decide their preference for products based on a small number
of factors (e.g. price, quality, and popularity) [DKR02,AFK+01,KBV09].

The low-rank assumption gives T robust structure; that is, only given a small number of
entries, T can be reconstructed fairly well.

Many users have approximately the same number of preferences. The low-rank
assumption is enough to get some bound on quality of recommendations (see Lemma 3.2
in [KP17b]). However, this bound considers “matrix-wide” recommendations. We would like
to give a bound on the probability that an output is a good recommendation for a particular
user.

It is not enough to assume that ∥T −Tk∥F ≤ρ∥T∥F. In a worst-case scenario, a few users
make up the vast majority of the recommendations (say, a few users like every product, and
the rest of the users are only happy with four products). Then, even if we reconstruct Tk

8This algorithm makes no distinction between binary matrices and matrices with values in the interval
[0, 1], and the corresponding analysis is straightforward upon deﬁning a metric for success when data is
nonbinary.

19

## Page 20

exactly, the resulting error, ρ∥T∥F, can exceed the mass of recommendations in the non-
heavy users, drowning out any possible information about the vast majority of users that
could be gained from the low-rank structure.

In addition to being pathological for user-speciﬁc bounds, this scenario is orthogonal to our
primary concerns: we aren’t interested in providing recommendations to users who desire
very few products or who desire nearly all products, since doing so is intractable and trivial,
respectively. To avoid considering such a pathological case, we restrict our attention to the
“typical user”:

Deﬁnition. For T ∈Rm×n, call S ⊂[m] a subset of users (γ, ζ)-typical (where γ > 0 and
ζ ∈[0, 1)) if |S| ≥(1 −ζ)m and, for all i ∈S,

1 + γ
∥T∥2
F

m
≤∥Ti∥2 ≤(1 + γ)∥T∥2
F

1

m
.

γ and ζ can be chosen as desired to broaden or restrict our idea of typical. We can enforce
good values of γ and ζ simply by requiring that users have the same number of good recom-
mendations; this can be done by deﬁning a good recommendation to be the top 100 products
for a user, regardless of utility to the user.

Given this deﬁnition, we can give a guarantee on recommendations for typical users that
come from an approximate reconstruction of T.

Theorem 5.1. For T ∈Rm×n, S a (γ, ζ)-typical set of users, and a matrix ˜T satisfying
∥T −˜T∥F ≤ε∥T∥F,

E
i∼uS

∥DTi −D ˜Ti∥TV

≤2ε√

1 + γ

1 −ζ
.

Further, for a chosen parameter ψ ∈(0, 1 −ζ) there exists some S′ ⊂S of size at least
(1 −ψ −ζ)m such that, for i ∈S′,

∥DTi −D ˜Ti∥TV ≤2ε
r

1 + γ

ψ
.

The ﬁrst bound is an average-case bound on typical users and the second is a strengthening
of the resulting Markov bound. Both bound total variation distance from DTi, which we
deem a good goal distribution to sample from for recommendations9. We defer the proof of
this theorem to the appendix.

When we don’t aim for a particular distribution and only want to bound the probability of
giving a bad recommendation, we can prove a stronger average-case bound on the failure
probability.

9When T is not binary, this means that if product X is λ times more preferable than product Y , then
it will be chosen as a recommendation λ2 times more often. By changing how we map preference data to
actual values in T , this ratio can be increased. That way, we have a better chance of selecting the best
recommendations, which approaches like matrix completion can achieve. However, these transformations
must also preserve that T is close-to-low-rank.

20

## Page 21

Theorem 5.2 (Theorem 3.3 of [KP17b]). For T ∈Rm×n a binary preference matrix, S
a (γ, ζ)-typical set of users, and a matrix ˜T satisfying ∥T −˜T∥F ≤ε∥T∥F, for a chosen
parameter ψ ∈(0, 1 −ζ) there exists some S′ ⊂S of size at least (1 −ψ −ζ)m such that

[(i, j) is bad] ≤
ε2(1 + ε)2

Pr
i∼uS′

(1 −ε)2
1/√

j∼˜Ti

ψ
2 (1 −ψ −ζ)
.

1 + γ −ε/√

For intuition, if ε is suﬃciently small compared to the other parameters, this bound becomes
O(ε2(1 + γ)/(1 −ψ −ζ)). The total variation bound from Theorem 5.1 is not strong enough
to prove this: the failure probability we would get is 2ε√

1 + γ/(1 −ψ −ζ). Accounting for
T being binary gives the extra ε factor.

We know k. More accurately, a rough upper bound for k will suﬃce. Such an upper bound
can be guessed and tuned from data.

In summary, we have reduced the problem of “ﬁnd a good recommendation for a user” to
“given some entries from a close-to-low-rank matrix T, sample from ˜Ti for some ˜T satisfying
∥T −˜T∥F ≤ε∥T∥F for small ε.”

5.2
Matrix Sampling

We have stated our assumptions on the full preference matrix T, but we also need assump-
tions on the information we are given about T. Even though we will assume we have a
constant fraction of data about T, this does not suﬃce for good recommendations. For ex-
ample, if we are given the product-preference data for only half of our products, we have no
hope of giving good recommendations for the other half.

We will use a model for subsampling for matrix reconstruction given by Achlioptas and
McSherry [AM07]. In this model, the entries we are given are chosen uniformly over all
entries.
This model has seen use previously in the theoretical recommendation systems
literature [DKR02]. Speciﬁcally, we have the following:

Deﬁnition. For a matrix T ∈Rm×n, let ˆT be a random matrix i.i.d. on its entries, where

(Tij

p
with probability p
0
with probability 1 −p .
(♣)

ˆTij =

Notice that E[ ˆT] = T. When the entries of T are bounded, ˆT is T perturbed by a random
matrix E whose entries are independent and bounded random variables. Standard concen-
tration inequalities imply that such random matrices don’t have large singular values (the
largest singular value is, say, O(
p

n/p)). Thus, for some vector v, if ∥Tv∥/∥v∥is large (say,
O(
p

mn/k)), then ∥(T +E)v∥/∥v∥will still be large, despite E having large Frobenius norm.

The above intuition suggests that when T has large singular values, its low-rank approxi-
mation Tk is not perturbed much by E, and thus, low-rank approximations of ˆT are good

21

## Page 22

reconstructions of T. A series of theorems by Achlioptas and McSherry [AM07] and Kereni-
dis and Prakash [KP17b] formalizes this intuition. For brevity, we only describe a simpliﬁed
form of the last theorem in this series, which is the version they (and we) use for analysis.
It states that, under appropriate circumstances, it’s enough to compute ˆTσ,η for appropriate
σ and η.

Theorem 5.3 (4.3 of [KP17b]). Let T ∈Rm×n and let ˆT be the random matrix deﬁned in

(♣), with p ≥
3
√

q

8k ∥ˆT∥F, let η = 1/5, and assume

29/2ε3∥T∥F and maxij |Tij| = 1. Let σ = 5

that ∥T∥F ≥
9

6

nk. Then with probability at least 1 −exp(−19(log n)4),

√

∥T −ˆTσ,η∥F ≤3∥T −Tk∥F + 3ε∥T∥F.

With this theorem, we have a formal goal for a recommendation systems algorithm. We are
given some subsample A = ˆT of the preference matrix, along with knowledge of the size
of the subsample p, the rank of the preference matrix k, and an error parameter ε. Given
that the input satisﬁes the premises for Theorem 5.3, for some user i, we can provide a
recommendation by sampling from (Aσ,η)i with σ, η speciﬁed as described. Using the result
of this theorem, Aσ,η is close to T, and thus we can use the results of Section 5.1 to conclude
that such a sample is likely to be a good recommendation for typical users.

Now, all we need is an algorithm that can sample from (Aσ,η)i.
Theorem 1 shows that
Algorithm 3 is exactly what we need!

5.3
Proof of Theorem 2

Theorem 2. Suppose we are given ˆT in the data structure in Proposition 3.2, where ˆT is a
subsample of T with p constant and T satisfying ∥T −Tk∥F ≤ρ∥T∥F for a known k. Further
suppose that the premises of Theorem 5.3 hold, the bound in the conclusion holds (which is
true with probability ≥1−exp(−19(log n)4)), and we have S a (γ, ζ)-typical set of users with
1 −ζ and γ constant. Then, for suﬃciently small ε, suﬃciently small ρ (at most a function
of ζ and γ), and a constant fraction of users ¯S ⊂S, for all i ∈¯S we can output samples
from a distribution Oi satisfying

∥Oi −DTi∥TV ≲ε + ρ

with probability 1 −(mn)−Θ(1) in O(poly(k, 1/ε) polylog(mn)) time.

Kerenidis and Prakash’s version of this analysis treats γ and ζ with slightly more care, but
does eventually assert that these are constants. Notice that we must assume p is constant.

Proof. We just run Algorithm 3 with parameters as described in Proposition 5.3: σ =

q

8k ∥A∥F, ε, η = 1/5. Provided ε ≲
p

5

p/k, the result from Theorem 1 holds. We can
perform the algorithm because A is in the data structure given by Proposition 3.2 (inﬂating
the runtime by a factor of log(mn)).

6

22

## Page 23

Correctness: Using Theorem 5.3 and Theorem 1,

∥T −D∥F ≤∥T −Aσ,η∥F + ∥Aσ,η −D∥F
≤3∥T −Tk∥F + 3ε∥T∥F + ε∥A∥F.

Applying a Chernoﬀbound to ∥A∥2
F (a sum of independent random variables), we get that
with high probability 1−e−∥T∥2
F p/3, ∥A∥F ≤
p

2/p∥T∥F. Since p is constant and ∥T −Tk∥F ≤
ρ∥T∥F, we get that ∥T −D∥F = O(ρ + ε)∥T∥F.

Then, we can apply Theorem 5.1 to get that, for S a (γ, ζ)-typical set of users of T, and Oi
the output distribution for user i, there is some S′ ⊂S of size at least (1 −ζ −ψ)m such
that, for all i ∈S′,

∥Oi −DTi∥TV ≤∥Oi −DDi∥TV + ∥DDi −DTi∥TV ≲ε + (ε + ρ)
r

1 + γ

ψ
≲ε + ρ,

which is the same bound that Kerenidis and Prakash achieve.

We can also get the same bound that they get when applying Theorem 5.2: although our
total variation error is ε, we can still achieve the same desired O(ε2) failure probability as
in the theorem. To see this, notice that in this model, Algorithm 3 samples from a vector
α such that ∥α −Ti∥≤ε. Instead of using Lemma 4.1, we can observe that because Ti is
binary, the probability that an ℓ2-norm sample from α is a bad recommendation is not ε,
but O(ε2). From there, everything else follows similarly.

In summary, the classical algorithm has two forms of error that the quantum algorithm does
not. However, the error in estimating the low-rank approximation folds into the error between
T and Aσ,η, and the error in total variation distance folds into the error from sampling from
an inexact reconstruction of T. Thus, we can achieve the same bounds.

Runtime: Our algorithm runs in time and query complexity

O(poly(k, 1/ε, ∥Ai∥/∥Di∥) polylog(mn, 1/δ)),

which is the same runtime as Kerenidis and Prakash’s algorithm up to polynomial slowdown.

To achieve the stated runtime, it suﬃces to show that ∥Ai∥/∥Di∥is constant for a constant
fraction of users in S. We sketch the proof here; the details are in Kerenidis and Prakash’s
proof [KP17b]. We know that ∥T −D∥F ≤O(ρ + ε)∥T∥F. Through counting arguments we
can show that, for a (1 −ψ′)-fraction of typical users S′′ ⊂S,


∥Ai∥2

E
i∼uS′′

∥(Aσ,η)i∥2


≲
(1 + ρ + ε)2

ψ
2.

(1 −ψ −ζ)
1

1+γ −ρ+ε

√

√

For ρ suﬃciently small, this is a constant, and so by Markov’s inequality a constant fraction
S′′′ of S′′ has ∥Ai∥/∥Di∥constant. We choose ¯S to be the intersection of S′′′ with S′.

23

## Page 24

Acknowledgments

Thanks to Scott Aaronson for introducing me to this problem, advising me during the re-
search process, and rooting for me every step of the way. His mentorship and help were
integral to this work as well as to my growth as a CS researcher, and for this I am deeply
grateful. Thanks also to Daniel Liang for providing frequent, useful discussions and for read-
ing through a draft of this document. Quite a few of the insights in this document were
generated during discussions with him.

Thanks to Patrick Rall for the continuing help throughout the research process and the par-
ticularly incisive editing feedback. Thanks to everybody who attended my informal presen-
tations and gave me helpful insight at Simons, including András Gilyén, Iordanis Kerenidis,
Anupam Prakash, Mario Szegedy, and Ronald de Wolf. Thanks to Fred Zhang for pointing
out a paper with relevant ideas for future work. Thanks to Sujit Rao and anybody else that
I had enlightening conversations with over the course of the project. Thanks to Prabhat
Nagarajan for the continuing support.

References

[Aar15]
Scott Aaronson. Read the ﬁne print. Nature Physics, 11(4):291, 2015.

[AFK+01]
Yossi Azar, Amos Fiat, Anna Karlin, Frank McSherry, and Jared Saia. Spectral analysis of data.
In Symposium on Theory of Computing. ACM, 2001.

[AM07]
Dimitris Achlioptas and Frank McSherry. Fast computation of low-rank matrix approximations.
Journal of the ACM (JACM), 54(2):9, 2007.

[APSPT05] Baruch Awerbuch, Boaz Patt-Shamir, David Peleg, and Mark Tuttle. Improved recommendation
systems. In Symposium on Discrete Algorithms, 2005.

[BBBV97]
Charles H Bennett, Ethan Bernstein, Gilles Brassard, and Umesh Vazirani.
Strengths and
weaknesses of quantum computing. SIAM Journal on Computing, 26(5):1510–1523, 1997.

[BJ99]
Nader H. Bshouty and Jeﬀrey C. Jackson. Learning DNF over the uniform distribution using a
quantum example oracle. SIAM J. Comput., 28(3):1136–1153, 1999.

[BK07]
Robert M Bell and Yehuda Koren. Lessons from the Netﬂix prize challenge. ACM SIGKDD
Explorations Newsletter, 9(2):75–79, 2007.

[DKM06]
P. Drineas, R. Kannan, and M. Mahoney. Fast Monte Carlo algorithms for matrices I: Approx-
imating matrix multiplication. SIAM Journal on Computing, 36(1):132–157, 2006.

[DKR02]
Petros Drineas, Iordanis Kerenidis, and Prabhakar Raghavan. Competitive recommendation
systems. In Symposium on Theory of Computing. ACM, 2002.

[DMM08]
P. Drineas, M. Mahoney, and S. Muthukrishnan. Relative-error CUR matrix decompositions.
SIAM Journal on Matrix Analysis and Applications, 30(2):844–881, 2008.

[DV06]
Amit Deshpande and Santosh Vempala. Adaptive sampling and fast low-rank matrix approx-
imation. In Approximation, Randomization, and Combinatorial Optimization. Algorithms and
Techniques, pages 292–303. Springer, 2006.

[FKV04]
Alan Frieze, Ravi Kannan, and Santosh Vempala.
Fast Monte-Carlo algorithms for ﬁnding
low-rank approximations. Journal of the ACM (JACM), 51(6):1025–1041, 2004.

24

## Page 25

[GSLW18]
András Gilyén, Yuan Su, Guang Hao Low, and Nathan Wiebe. Quantum singular value trans-
formation and beyond: exponential improvements for quantum matrix arithmetics. arXiv, 2018.

[HHL09]
Aram W Harrow, Avinatan Hassidim, and Seth Lloyd. Quantum algorithm for linear systems
of equations. Physical review letters, 103(15):150502, 2009.

[HKS11]
Elad Hazan, Tomer Koren, and Nati Srebro. Beating SGD: Learning SVMs in sublinear time.
In Neural Information Processing Systems, 2011.

[KBV09]
Yehuda Koren, Robert Bell, and Chris Volinsky. Matrix factorization techniques for recom-
mender systems. Computer, 42(8), 2009.

[KP17a]
Iordanis Kerenidis and Anupam Prakash. Quantum gradient descent for linear systems and
least squares. arXiv, 2017.

[KP17b]
Iordanis Kerenidis and Anupam Prakash. Quantum recommendation systems. In Innovations
in Theoretical Computer Science, 2017.

[KRRT01]
Ravi Kumar, Prabhakar Raghavan, Sridhar Rajagopalan, and Andrew Tomkins. Recommenda-
tion systems: a probabilistic analysis. Journal of Computer and System Sciences, 63(1):42 – 61,
2001.

[KS08]
Jon Kleinberg and Mark Sandler. Using mixture models for collaborative ﬁltering. Journal of
Computer and System Sciences, 74(1):49–69, 2008.

[KV17]
Ravindran Kannan and Santosh Vempala. Randomized algorithms in numerical linear algebra.
Acta Numerica, 26:95–135, 2017.

[LMR13]
Seth Lloyd, Masoud Mohseni, and Patrick Rebentrost. Quantum algorithms for supervised and
unsupervised machine learning. arXiv, 2013.

[LMR14]
Seth Lloyd, Masoud Mohseni, and Patrick Rebentrost. Quantum principal component analysis.
Nature Physics, 10(9):631, 2014.

[Pre18]
John Preskill. Quantum Computing in the NISQ era and beyond. Quantum, 2:79, 2018.

[Rec11]
Benjamin Recht.
A simpler approach to matrix completion.
Journal of Machine Learning
Research, 12:3413–3430, 2011.

[SWZ16]
Zhao Song, David P. Woodruﬀ, and Huan Zhang. Sublinear time orthogonal tensor decomposi-
tion. In Neural Information Processing Systems, 2016.

A
Deferred Proofs

Proof of Lemma 4.5. We can describe ModFKV as FKV run on K with the ﬁlter threshold
γ raised from Θ(¯ε/K) to 1/K. The original work aims to output a low-rank approximation
similar in quality to AK, so it needs to know about singular values as low as ¯ε/K. In our case,
we don’t need as strong of a bound, and can get away with ignoring these singular vectors.
To prove our bounds, we just discuss where our proof diﬀers from the original work’s proof
(Theorem 1 of [FKV04]). First, they show that

∆(W T; u(t), t ∈[K]) ≥∥AK∥2
F −¯ε

2∥A∥2
F.

The proof of this holds when replacing K with any K′ ≤K. We choose to replace K with
the number of singular vectors taken by ModFKV, k. Then we have that

∆(W T; u(t), t ∈T) = ∆(W T; u(t), t ∈[k]) ≥∥Ak∥2
F −¯ε

2∥A∥2
F.

25

## Page 26

We can complete the proof now, using that [k] = T because our ﬁlter accepts the top k
singular vectors (though not the top K). Namely, we avoid the loss of γ∥W∥2
F that they
incur in this way. This gives the bound (♦).

Further, because we raise γ, we can correspondingly lower our number of samples. Their
analysis requires q (which they denote p) to be Ω(max{ k4

¯ε2 , k2

¯εγ2,
1

¯ε2γ2}) (for Lemma 3, Claim 1,
and Claim 2, respectively). So, we can pick q = Θ(K4/¯ε2).

As for bounding k, ModFKV can compute the ﬁrst k singular values to within a cumulative
additive error of ¯ε∥A∥F. This follows from Lemma 2 of [FKV04] and the Hoﬀman-Wielandt
inequality.
Thus, ModFKV could only conceivably take a singular vector v such that
∥Av∥≥σ −¯ε∥A∥F = σ(1 −¯ε∥A∥F/σ), and analogously for the upper bound.

Proof of Proposition 4.6. We follow the proof of Claim 2 of [FKV04]. For i ̸= j, we have as
follows:
ˆvT
i ˆvj
=
|uT
i SSTuj|

∥W Tui∥∥W Tuj∥≤|uT
i SSTuj|

σ2
≤∥S∥2
F

q = ¯ε

σ2√

K
1 −ˆvT
i ˆvi
= |uT
i WW Tui| −|uT
i SSTui|

∥W Tui∥∥W Tui∥
≤∥S∥2
F

Here, we use that ∥WW T −SST∥≤∥S∥2
F/√

q = ¯ε

σ2√

K

q (Lemma 2 [FKV04]) and {Wui} are orthog-
onal.

This means that ˆV T ˆV is O(¯ε/K)-close entry-wise to the identity. Looking at ˆV ’s singular
value decomposition into AΣBT (treating Σ as square), the entrywise bound implies that
∥Σ2−I∥F ≲¯ε, which in turn implies that ∥Σ−I∥F ≲¯ε. Λ := ABT is close to ˆV , orthonormal,
and in the same subspace as desired.

Proof of Theorem 4.7. We will prove a slightly stronger statement: it suﬃces to choose Aσ,η
such that Pσ,η is an orthogonal projector10 (denoted Πσ,η).
We use the notation ΠE :=
Πσ,η −Πσ(1+η) to refer to the error of Πσ,η, which can be any orthogonal projector on the
span of the singular vectors with values in [σ(1 −η), σ(1 + η)). We denote σk by σ and
min m, n by N.

∥AΠ −Aσ,η∥2
F = ∥UΣV T(Π −Πσ,η)∥2
F
= ∥ΣV T(Π −Πσ,η)∥2
F

N
X

=

i=1
σ2
i ∥vT
i Π −vT
i Πσ,η∥2

That is, AΠ and Aσ,η are close when their corresponding projectors behave in the same way.
Let ai = vT
i Π, and bi = vT
i Πσ,η. Note that





vT
i
σi ≥(1 + η)σ
vT
i ΠE
(1 + η)σ > σi ≥(1 −η)σ
0
(1 −η)σ > σi

bi =




.

10In fact, we could have used this restricted version as our deﬁnition of Aσ,η.

26

## Page 27

Using the ﬁrst and third case, and the fact that orthogonal projectors Π satisfy ∥v −Πv∥2 =
∥v∥2 −∥Πv∥2, the formula becomes

ℓ(σ(1+η))
X

ℓ(σ(1−η))
X

∥AΠ −Aσ,η∥2
F =

1
σ2
i (1 −∥ai∥2) +

N
X

ℓ(σ(1+η))+1
σ2
i ∥ai −bi∥2 +

ℓ(σ(1−η))+1
σ2
i (∥ai∥2).
(♠)

Now, we consider the assumption equation. We reformulate the assumption into the following
system of equations:

k
X

N
X

i=1
σ2
i ∥ai∥2 + εσ2
σ2
i are nonincreasing

i=1
σ2
i ≤

∥ai∥2 ∈[0, 1]
X
∥ai∥2 = k

The ﬁrst line comes from the equation. The second line follows from Π being an orthogonal
projector on a k-dimensional subspace.

It turns out that this system of equations is enough to show that the ∥ai∥2 behave the way
we want them to. We defer the details to Lemma A.2; the results are as follows.

1
σ2
i (1 −∥ai∥2) ≤ε

1 + 1


σ2
k

ℓ(σk(1+η))
X

η

ℓ(σk1+η))
X

1
(1 −∥ai∥2) ≤ε

η

Now, applying the top inequalities to (♠):

∥AΠ −Aσ,η∥2
F ≤2εσ2

η
+

ℓ(σk(1−η))+1
σ2
i ∥ai∥2 ≤ε
1

η −1

σ2
k

N
X

N
X

ℓ(σk(1−η))+1
∥ai∥2 ≤ε

η

ℓ(σ(1−η))
X

ℓ(σ(1+η))+1
σ2
i ∥ai −bi∥2.

We just need to bound the second term of (♠). Notice the following:

ℓ(σ(1−η))
X

ℓ(σ(1+η))+1
σ2
i ∥ai −bi∥2 ≤σ2(1 + η)2∥UT(Π −ΠE)∥2
F,

where U is the set of vectors vℓ(σ(1+η))+1 through vℓ(σ(1−η)).

Notice that ΠE is the error component of the projection, and this error can be any projection
onto a subspace spanned by U. Thus, to bound the above we just need to pick an orthogonal
projector ΠE making the norm as small as possible. If UUT Π were an orthogonal projection,
this would be easy:
∥UT (Π −UUT Π)∥2
F = 0.

However, this is likely not the case.
UUT Π is close to an orthogonal projector, though,
through the following reasoning:

27

## Page 28

For ease of notation let P1 be the orthogonal projector onto the ﬁrst ℓ(σ(1 + η)) singular
vectors, P2 = UUT , and P3 be the orthogonal projector onto the the rest of the singular
vectors. We are concerned with P2Π.

Notice that P1 + P2 + P3 = I. Further, ∥(I −Π)P1∥2
F ≤ε/η and ∥ΠP3∥2
F ≤ε/η from
Lemma A.2. Then

P2Π = (I −P1 −P3)Π = Π −P1 + P1(I −Π) −P3Π

∥P2Π −(Π −P1)∥F = ∥P1(I −Π) −P3Π∥F ≤2
p

ε/η

So now it is suﬃcient to show that Π −P1 is close to a projector matrix. This follows from
Lemma A.1, since it satisﬁes the premise:

(Π −P1)2 −(Π −P1) = Π −ΠP1 −P1Π + P1 −Π + P1
= (I −Π)P1 + P1(I −Π)

∥(Π −P1)2 −(Π −P1)∥F ≤2
p

ε/η

Thus, UUT Π is (2
p

ε/η + (2
p

ε/η + 16ε/η))-close to an orthogonal projector in Frobenius
norm.

We can choose ΠE to be M, and plug this into (♠). We use the assumptions that ε/η < 1
and η < 1 to bound.

ℓ(σ(1−η))
X

ℓ(σ(1+η))+1
σ2
i ∥ai −bi∥2 ≤σ2(1 + η)2∥UT(Π −M)∥2
F

≤σ2(1 + η)2∥UT(Π −(UUT Π + E))∥2
F
≤σ2(1 + η)2∥UTE∥2
F
≲σ2(1 + η)2ε/η

∥AΠ −Aσ,η∥2
F ≲2εσ2

η
+ σ2(1 + η)2 ε

η ≲εσ2/η

This concludes the proof. (The constant factor is 1602.)

Lemma A.1. If a Hermitian A satisﬁes ∥A2 −A∥F ≤ε, then ∥A −P∥F ≤ε + 4ε2 for some
orthogonal projector P.

Proof. Use the fact that Hermitian matrices are normal, so A = UΓUT for unitary U and
diagonal matrix Γ, and

A2 −A = U(Γ2 −Γ)UT =⇒∥Γ2 −Γ∥F ≤ε.

From here, consider the entries γi of Γ, satisfying γ2
i −γi = ci and P c2
i = ε2.
Thus,
γi = (1 ± √

1 + 4ci)/2 which is at most ci + 4c2
i oﬀfrom 0.5 ± 0.5 (aka {0, 1}), using that

1 −x/2 −x2/2 ≤
√

1 −x ≤1 −x/2.

Finally, this means that Γ is oﬀfrom having only 0’s and 1’s on the diagonal by
p

P(ci + 4c2
i )2 ≤
ε + 4ε2 in Frobenius norm. If Γ had only 0’s and 1’s on the diagonal, the resulting UΓUT

would be an orthogonal projector.

28

## Page 29

Lemma A.2. The system of equations:

k
X

N
X

i=1
σ2
i ∥ai∥2 + εσ2
k
σ2
i are nonincreasing

i=1
σ2
i ≤

∥ai∥2 ∈[0, 1]
X
∥ai∥2 = k

imply the following, for 0 < η ≤1:

1
σ2
i (1 −∥ai∥2) ≤ε

1 + 1


σ2
k

ℓ(σk(1+η))
X

η

ℓ(σk1+η))
X

1
(1 −∥ai∥2) ≤ε

η

ℓ(σk(1−η))+1
σ2
i ∥ai∥2 ≤ε
1

η −1

σ2
k

N
X

N
X

ℓ(σk(1−η))+1
∥ai∥2 ≤ε

η

Proof. We are just proving straightforward bounds on a linear system. We will continue to
denote σk by σ. Thus, k = ℓ(σ).

The slack in the inequality is always maximized when the weight of the ∥ai∥2 is concentrated
on the large-value (small-index) entries. For example, the choice of ∥ai∥2 maximizing slack
in the given system of equations is the vector {∥ai∥}i∈[N] = 1≤k. Here, 1≤x denotes the
vector where

(1≤x)i :=

(
1
i ≤x
0
otherwise .

For brevity, we only give the details for the ﬁrst bound; the others follow similarly. Consider
adding the constraint C = Pℓ(σ(1+η))
1
σ2
i (1 −∥ai∥2) to the system of equations. We want to
determine for which values of C the modiﬁed system is still feasible; we can do this by trying
the values that maximize slack.

This occurs when weight is on the smallest possible indices:
when ∥aℓ(σ(1+η))∥2 = 1 −
C/σ2
ℓ(σ(1+η)), ∥aℓ(σ)+1∥2 = C/σ2
ℓ(σ(1+η)), and all other ∥ai∥2 are 1≥k. Notice that ∥aℓ(σ(1+η))∥2

could be negative and ∥aℓ(σ)+1∥could be larger than one, breaking constraints. However, if
there is no feasible solution even when relaxing those two constraints, there is certainly no
solution to the non-relaxed system. Thus, we check feasibility (by construction the second
equation is satisﬁed):

k
X

k
X

i=1
σ2
i ≤

C

1 −
σ2
ℓ(σ)+1


≤εσ2

σℓ(σ(1+η))

C

1 −
1


≤εσ2

(1 + η)2

29

i=1
σ2
i −C + C
σ2
ℓ(σ)+1

σℓ(σ(1+η))
+ εσ2

## Page 30

This gives the bound on C. Repeating for all four cases, we get the following bounds:

ℓ(σ(1+η))
X

1
σ2
i (1 −∥ai∥2) ≤ε(1 + η)2σ2

2η + η2

ℓ(σ(1+η))
X

1
(1 −∥ai∥2) ≤
ε

2η + η2

N
X

ℓ(σ(1−η))+1
σ2
i ∥ai∥2 ≤ε(1 −η)2σ2

2η −η2

N
X

ℓ(σ(1−η))+1
∥ai∥2 ≤
ε

2η −η2

We get the bounds in the statement by simplifying the above (using that η ≤1).

Proof of Theorem 5.1. The following shows the ﬁrst, average-case bound (note the use of
Lemma 4.1 and Cauchy-Schwarz).

X

Ei∼uS

∥DTi −D ˜Ti∥TV

= 1

|S|

≤
1

(1 −ζ)√

≤21 + γ

1 −ζ

≤21 + γ

1 −ζ

(1 −ζ)

i∈S
∥DTi −D ˜Ti∥TV

X

2∥Ti −˜Ti∥

(1 −ζ)m

∥Ti∥

i∈S

X

≤
2(1 + γ)

i∈S
∥Ti −˜Ti∥

m∥T∥F

P



i∈[m] ∥Ti −˜Ti∥

√

m∥T∥F

√



m∥T −˜T∥F

√

m∥T∥F

≤2ε(1 + γ)

Using that ∥T −˜T∥F ≤ε∥T∥F in combination with a pigeonhole-like argument, we know
that at least a (1 −ψ)-fraction of users i ∈[m] satisfy

∥Ti −˜Ti∥2 ≤ε2∥A∥2
F

ψm
.

Thus, there is a S′ ⊂S of size at least (1 −ψ −ζ)m satisfying the above. For such an i ∈S′,
we can argue from Lemma 4.1 and the deﬁnition of a (γ, ζ)-typical user that

∥Ti∥
≤2ε∥T∥F(1 + γ)√

∥DTi −D ˜Ti∥TV ≤2∥Ti −˜Ti∥

√

ψm∥T∥F
= 2ε(1 + γ)

m

√

ψ
.

B
Variant for an Alternative Model

In this section, we describe a variant of our recommendation systems algorithm for the
competitive recommendations model, seen in Drineas, Kerenidis, and Raghavan’s 2002 paper

30

## Page 31

giving two algorithms for competitive recommendations [DKR02]. The idea is to output good
recommendations with as little knowledge about the preference matrix T as possible. Our
algorithm is similar to Drineas et al’s second algorithm, which has weak assumptions on the
form of T, but strong assumptions on how we can gain knowledge about it.

We use a similar model, as follows:

• We begin with no knowledge of our preference matrix T apart from the promise that
∥T −Tk∥F ≤ρ∥T∥F;

• We can request the value of an entry Tij for some cost;

• For some constant 0 < c ≤1, we can sample from and compute probabilities from a
distribution P over [m] satisfying

P(i) ≥c∥Ti∥2

∥T∥2
F
.

Further, we can sample from and compute probabilities from distributions Qi over [n],
for i ∈[m], satisfying

Qi(j) ≥c T 2
ij

∥Ti∥2.

We discuss the ﬁrst assumption in Section 5.1. The second assumption is very strong, but
we will only need to use it sparingly, for some small set of users and products. In practice,
this assumption could be satisﬁed through paid user surveys.

The last assumption states that the way that we learn about users naturally, via normal
user-site interaction, follows the described distributions. For example, consider when T is
binary (as in Section 5.1). The assumption about P states that we can sample for users
proportional to the number of products they like (with possible error via c). Even though
we don’t know the exact number of products a user likes, it is certainly correlated with the
amount of purchases/interactions the user has with the site. With this data we can form
P. The assumption about Qi’s states that, for a user, we can sample uniformly from the
products that user likes. We can certainly assume the ability to sample from the products
that a user likes, since such positive interactions are common, intended, and implicit in the
user’s use of the website. It is not clear whether uniformity is a reasonable assumption,
but this can be made more reasonable by making T non-binary and more descriptive of the
utility of products to users.

Under these assumptions, our goal is, given a user i, to recommend products to that user
that were not previously known to be good and are likely to be good recommendations.

To do this, we run Algorithm 3 with T, k, ε as input, the main change being that we use
Frieze, Kannan, and Vempala’s algorithm as written in their paper instead of ModFKV. As
samples and requests are necessary, we can provide them using the assumptions above.

For the FKV portion of the algorithm, this leads to O(q2) requests to q users about q

31

## Page 32

products, where q = O(max{ k4

c3ε6,
k2

c3ε8}). This gives the description of a D such that

∥T −D∥F ≤
q

∥T −Tk∥2
F + ε2∥T∥2
F ≤(ρ + ε)∥T∥F.

Thus, immediately we can use theorems from Section 5.1 to show that samples from D will
give good recommendations.

From here, the next part of Algorithm 3 can output the desired approximate sample from Di.
A similar analysis will show that this approximate sample is likely to be a good recommen-
dation, all while requesting and sampling a number of entries independent of m and n. Such
requests and samples will only be needed for the q users chosen by FKV for its subsample,
along with the input user. Further, for more recommendations, this process can be iterated
with unused information about the q users chosen by FKV. Alternatively, if we can ask the
q users for all of their recommendations, we only need O( k2

ε2 log k

δ ) samples from the input
user to provide that user with an unlimited number of recommendations (we can store and
update the estimate of AiST to use when sampling).

This gives good recommendations, only requiring knowledge of O(poly(k, 1/ε)) entries of T,
and with time complexity polynomial in the number of known entries.

32
