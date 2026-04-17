---
source_pdf: ../arxiv_2503.12789.pdf
pages: 14
extracted_at: 2026-04-17T12:32:44+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Lower bounding the MaxCut of high girth 3-regular graphs using the QAOA"
author: "Edward Farhi; Sam Gutmann; Daniel Ranard; Benjamin Villalonga"
---

# arxiv_2503.12789

Original title: Lower bounding the MaxCut of high girth 3-regular graphs using the QAOA

Author metadata: Edward Farhi; Sam Gutmann; Daniel Ranard; Benjamin Villalonga

Source PDF: ../arxiv_2503.12789.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Lower bounding the MaxCut of high girth 3-regular graphs using
the QAOA

Edward Farhi1,2, Sam Gutmann , Daniel Ranard3, and Benjamin Villalonga1

1Google Quantum AI, Venice, CA 90291
2Center for Theoretical Physics, Massachusetts Institute of Technology, Cambridge, MA 02139
3Walter Burke Institute for Theoretical Physics, California Institute of Technology, Pasadena, CA 91125

arXiv:2503.12789v2 [quant-ph] 26 Jan 2026

January 27, 2026

Abstract

We study MaxCut on 3-regular graphs of minimum girth g for various g’s. We obtain new lower bounds
on the maximum cut achievable in such graphs by analyzing the Quantum Approximate Optimization
Algorithm (QAOA). For g ≥16, at depth p ≥7, the QAOA improves on previously known lower bounds.
Our bounds are established through classical numerical analysis of the QAOA’s expected performance.
This analysis does not produce the actual cuts but establishes their existence. When implemented on a
quantum computer, the QAOA provides an efficient algorithm for finding such cuts, using a constant-
depth quantum circuit. To our knowledge, this gives an exponential speedup over the best known classical
algorithm guaranteed to achieve cuts of this size on graphs of this girth. We also apply the QAOA to
the Maximum Independent Set problem on the same class of graphs.

1
Introduction

The MaxCut problem asks one to partition the vertices of a graph into two subsets to maximize the size of
the “cut,” or the set of edges that cross between the subsets. Determining the maximum cut of a graph is
NP-hard, one of Karp’s original 21 problems [1], and it remains NP-hard when restricted to 3-regular graphs
[2]. Often one studies MaxCut as an approximate optimization problem, with the goal of finding a large cut.
Here we study MaxCut on 3-regular graphs with large girth. The girth of a graph is the length of its
shortest cycle. We are interested in two questions: (1) How can we lower bound the maximum cut of a
graph in terms of its girth, and (2) How can we use a classical or quantum algorithm to efficiently obtain
a cut at least this large? We answer both questions through our analysis of the Quantum Approximate
Optimization Algorithm (QAOA) [3]. While the first question is a mathematical question that does not
concern algorithms, we prove a new lower bound constructively, by proving a performance guarantee on the
QAOA applied to 3-regular graphs of sufficient girth. Here we have analyzed the performance of the QAOA
without the need to actually run the algorithm. To find a cut of that size using the QAOA, you need to run
the algorithm on quantum hardware. To our knowledge, the QAOA then provides an exponential speedup
over the best known classical algorithms guaranteed to achieve a cut of this size, which require exponential
time.
We quantify a cut by the cut fraction, that is, the fraction of edges that appear in the cut. For a graph G,
we can ask about the cut fraction of the largest cut, or MaxCut(G)/|E(G)| for edge set E(G). The smallest
possible maximum cut fraction among all 3-regular graphs of girth at least g is denoted

Mg =
inf
3-regular graphs G
girth(G)≥g

1

MaxCut(G)

|E(G)|
.
(1)

## Page 2

Figure 1: Edge neighborhood of the central edge of a 3-regular graph at p = 3 and girth g ≥8. Every edge in
the graph has this neighborhood structure at this minimum girth. We evaluate ˜cedge(p) which is the optimal
quantum expected value of the cost function on the central edge.

We use the infimum because the set of graphs G with girth(G)≥g is infinite, but (1) means that every graph
G of girth at least g has a cut of size at least |E(G)|Mg. The numerical value of Mg is currently unknown
for general g.
In this paper, we obtain new rigorous lower bounds on Mg. We do this by predicting the performance of
the QAOA for MaxCut on large girth 3-regular graphs. MaxCut may be viewed as an optimization problem
over bit strings of length |V (G)|, where V (G) is the vertex set, and each bit string indicates a partition of the
graph into two subsets. The QAOA is a quantum algorithm for approximate optimization over bit strings. It
has a depth parameter p and performance can only improve as p increases. The QAOA produces a quantum
state where the expectation of the MaxCut cost function is guaranteed to have a certain value. This means
that there must exist cuts of at least this value. The MaxCut cost function is a sum of terms from each
edge of the graph. For high-girth graphs, at each edge the neighborhood relevant to the QAOA is a tree.
See Fig. 1 for an example at p = 3. To guarantee this we need g ≥2p + 2. Each of these tree neighborhoods
is isomorphic and at optimal parameters makes a contribution of ˜cedge(p) for each edge of the graph. The
total contribution to the quantum expected value of the cost, at optimal parameters, is |E(G)|˜cedge(p). The
size of the largest cut must be at least the size of the cut found by the QAOA. So we then have

Mg ≥˜cedge(p)
(2)

for g ≥2p + 2. So Mg is lower bounded by a quantum expectation value.
Our paper explains how we calculate ˜cedge(p) with classical numerical computation. We get values for p
up to 17, corresponding to g of 36. The numerical computations are highly accurate and the numbers we
quote are good to at least four digits. In fact we have the best lower bound known to us for Mg for any
g ≥16, improving on previous results by Thompson, Parekh, and Marwaha [4]. At p = 17 and g = 36 we
are guaranteed a cut fraction of ˜cedge(p=17) = 0.8971. See Fig. 2. Separately, from Refs. [5] and [6], one
finds limg→∞Mg ≥0.912.
Actually running the QAOA on a graph G has time-complexity O(|E(G)|), and it uses a constant-depth
quantum circuit. For any 3-regular graph of girth g ≥2p + 2, by using repeated applications of the QAOA,
with total time-complexity O(|E(G)|2), we can obtain a cut of size at least ⌊|E(G)|˜cedge(p)⌋with probability
2/3. This may be viewed as an optimization or search problem with a promise (about the girth), with the
goal of obtaining a cut of size above this threshold. There exist several classical algorithms for MaxCut, and
we do not claim that the QAOA is superior in practice. However, besides the QAOA, we do not know any
quantum or classical algorithms proven to solve this promise problem in subexponential time.
A natural point of comparison is the celebrated Goemans-Williamson (GW) algorithm [7]. The success of

2

## Page 3

approximation algorithms is often measured by their approximation ratio: the ratio of the obtained value to
the optimal value. The GW algorithm guarantees an approximation ratio of 0.878 for general graphs, and an
improved ratio of 0.932 when specialized to graphs of maximum degree 3 [8]. Assuming the Unique Games
Conjecture [9], it is NP-hard to exceed the GW algorithm’s 0.878 guarantee for the worst case. Our present
analysis of the QAOA, however, focuses on cut fraction rather than approximation ratio. While our highest
cut fraction guarantee of 0.8971 immediately guarantees an approximation ratio at least this size, such an
approximation ratio is already exceeded by the specialized GW algorithm. Meanwhile, the GW algorithm
does not provide any direct guarantee on cut fraction. So given a graph of girth g ≥36, with the task of
finding a cut of size at least 0.8971|E(G)|, the GW algorithm is not guaranteed to succeed in general, while
our specification of the QAOA provides an efficient algorithm. On the other hand, in the particular case of
bipartite graphs (of any girth) the GW algorithm achieves the perfect cut, while the QAOA generally does
not.
We briefly review QAOA, then describe the classical numerical methods used to obtain the performance
guarantee. Our calculations are similar to the original calculations of Ref. [3], though performed at larger
depth with distinct methods. We draw inspiration from the tensor network methods of Ref. [10], where
the same QAOA quantities were calculated, though at lower depth p. See also Refs. [11, 12] for related
calculations at lower depth but including graphs of higher degree. Our main technical contribution is to
analyze the QAOA for MaxCut on 3-regular graphs of large girth, using modified numerical methods to allow
higher depth than previously obtained. We then interpret these results in relation to previous lower bounds
for the maximum cut and previous algorithms for approximating its value. Finally we apply the QAOA to
the problem of Maximum Independent Set on high-girth 3-regular graphs.

2
Review of the QAOA

The Quantum Approximate Optimization Algorithm (QAOA) is a quantum algorithm for finding approxi-
mate solutions to combinatorial optimization problems. We seek to optimize an objective function C over
bit strings, which is usually a sum over terms that each involves a few bits. The QAOA depends on an
integer parameter p ≥1 and produces quantum states of the form

|γ, β⟩= U(B, βp)U(C, γp) · · · U(B, β1)U(C, γ1)|s⟩.
(3)

Here |s⟩is the uniform superposition over computational basis states, U(C, γ) = e−iγC is diagonal in the
computational basis, and U(B, β) = e−iβB where B = P
j Xj is the sum of single-qubit Pauli X operators.
The angles γ = (γ1, . . . , γp) and β = (β1, . . . , βp) are classical parameters which specify the QAOA state.
For MaxCut, given a graph with vertices V and edges E, the cost function operator counts edges crossing
between two subsets in a partition,

C =
X

(j,k)∈E

1 −ZjZk

2
.
(4)

When measured in the computational basis, the state |γ, β⟩produces a bit string with a cost function value
whose expectation is
Fp(γ, β) = ⟨γ, β|C|γ, β⟩.
(5)

The angles (γ, β) are optimized to maximize the expectation value Fp(γ, β). The quantum circuit depth
grows with p, and the performance at optimal parameters can only improve with larger p.

3
Pre-computing QAOA parameters for graphs with large girth

Traditionally, the QAOA is executed by applying the quantum circuit with initial parameters, estimating Fp
through measurements, then using classical optimization to update (γ, β) and repeating the process. Here
we take a different approach, emphasized especially by Ref. [10], where parameters are chosen in advance
for all graphs of a given girth.

3

## Page 4

First note that the expectation value Fp(γ, β) can be decomposed as a sum over edge terms. For MaxCut,
each term depends only on the subgraph within distance p of that edge. When a graph has girth at least

g ≥2p + 2
(6)

these neighborhoods are trees. Moreover, for all 3-regular graphs with this minimum girth, these trees are
all isomorphic and make the same contribution to Fp(γ, β). We then can write

Fp(γ, β) = |E(G)| cedge(γ, β)
(7)

where

cedge(γ, β) = 1 −⟨γ, β|ZiZj|γ, β⟩

2
(8)

and (i, j) ∈E(G) can be any pair of neighboring nodes in G since they all make identical contributions.
Since (7) holds for all 3-regular graphs of girth at least g, we have

Mg ≥cedge(γ, β)
(9)

for any γ, β. By finding optimal (or near optimal) parameters we improve the bound. We later discuss how
we find the near optimal parameters ˜γ, ˜β. Let

˜cedge(p) = cedge(˜γ, ˜β).
(10)

Then we have

Mg ≥˜cedge(p)
(11)

for any p ≤(g −2)/2.
Wurtz and Lykov [10] computed ˜cedge(p) up to p = 11 and we reproduce these numbers. We compute
up to p = 17. More precisely, for any fixed γ, β, we compute cedge(γ, β) numerically using exact tensor
network methods. The numerical error in the computation of cedge(γ, β) is negligible compared to the 4-
digit accuracy reported in our results. Then we maximize to obtain some approximately optimal parameters
˜γ, ˜β. Despite this approximate optimization, the value ˜cedge(p) then serves as a precise lower bound for Mg,
due to (11).
When running the QAOA for graphs of girth greater than 36, it would be helpful to pre-compute the
optimal parameters for p > 17, which we have not done. For sufficiently large p this may be intractable,
or it may be well-approximated by extrapolation of the optimal parameters from smaller p to larger p.
Regardless, for the purpose of proposing a formal algorithm, for all 3-regular graphs of girth greater than 36,
we propose running the p = 17 QAOA with our fixed, pre-computed parameters. This protocol already gives
an algorithm with polynomial runtime with respect to graph size, with the best currently known performance
guarantee on cut fraction. The only other algorithms we currently know with the same performance guarantee
take exponential time. One example is the brute force algorithm, which finds the best cut in exponential
time, and is therefore guaranteed to find a cut of size at least 0.8971|E(G)|, whose existence follows from
our present results. A classical algorithm of Williams [13] finds the best cut in exponential time but using a
smaller exponent than brute force search.

4
Analyzing time-complexity

Here we detail the runtime of the QAOA as an algorithm running on a quantum computer to find an actual
cut. (This analysis is separate from the classical numerical computations discussed in Section 5.2, which
establish performance guarantees and serve as a pre-computation that is independent of problem instance.)

4

## Page 5

Figure 2: Lower bound on Mg for 3-regular graphs given by the present work (blue crosses). As a comparison
we show the results of Thompson-Parekh-Marwaha (TPM) [4] in orange. The QAOA lower bound exceeds
the TPM lower bound at g ≥16 (corresponding to p ≥7). The QAOA lower bound exceeds the TPM
g →∞bound at g ≥32 (p ≥15).

We focus on the QAOA for d-regular graphs on |V (G)| vertices, treating d as a constant. The MaxCut
problem size is the number of edges, |E(G)| = (d/2)|V (G)|. The QAOA at depth p uses O(p|E(G)|) total
gates. When analyzing the runtime of quantum algorithms, we are interested in both the total number of
gates and also the circuit depth, which counts the minimal number of layers such that each layer involves
non-overlapping gates.
While the parameter p is sometimes called the “depth” of the QAOA, its relation to circuit depth depends
on the graph. The unitary U(B, β) can be implemented in a single layer of depth 1. On the other hand, while
U(C, γ) = e−iγC is naturally implemented by a two-qubit gate for every edge, these gates overlap whenever
two edges share a vertex, so U(C, γ) requires circuit depth larger than 1. Szegedy noted that one can use
Vizing’s theorem to calculate the circuit depth [14]. For graph G, the “edge chromatic number” χ′(G) is the
minimal number of colors required for an edge-coloring where no two adjacent edges share the same color.
By using a layer of gates for each color, we see U(C, γ) can be implemented in depth χ′(G) using 2-local
gates. Vizing’s theorem states that for general graphs, χ′(G) ≤∆(G) + 1, where ∆(G) is the maximum
degree. Again treating d as a constant, we conclude U(C, γ) has O(1) circuit depth, and the full QAOA has
circuit depth O(p). To achieve this O(p)-depth circuit, we need to classically pre-compute to actually find
one of the colorings guaranteed by Vizing’s theorem. For a bounded degree graph, this computation runs in
time O(|E(G)|) [15], the same as the problem size, hence not contributing to the asymptotic complexity.
In this section, when we analyze the time complexity of running the QAOA on a quantum computer at
fixed p, we imagine running with fixed parameters γ, β given in advance. There is no outer loop variational
search. The quantum circuit uses |V (G)| qubits, with O(|E(G)|) = O(|V (G)|) gates and constant circuit
depth.
After running the QAOA circuit and performing a measurement in the computational basis, we obtain
a cut of the graph that depends on the measurement outcome.
The expected value of the cut size is
|E(G)|˜cedge(p). We can also ask for a guarantee that the cut is above (the floor of) this expected value with

5

## Page 6

Figure 3: Optimized parameters ˜γ and ˜β as a function of (j −1)/(p−1) for different values of p up to p=17.
These figures suggest that the optimal parameters might approach fixed curves as p increases.

high probability. To that end, repeat the QAOA circuit and measurement many times and record the best
outcome. The probability of sampling a cut size of at least ⌊|E(G)|˜cedge(p)⌋with a single sample is at least
1/|E(G)|. To see this, let C ∈{0, 1, . . . , |E(G)|} denote the cut size obtained from a single sample, and
denote C0 = ⌊|E(G)| ˜cedge(p)⌋, with p0 := Pr
C ≥C0

. We calculate

E[C] ≤(C0 −1) Pr(C ≤C0 −1) + |E(G)| Pr(C ≥C0)

= (1 −p0)(C0 −1) + p0 |E(G)|

≤C0 −1 + p0|E(G)|,
(12)

where the first line uses the fact C takes integer values with C ≤|E(G)|. Combining the above with E[C] ≥
C0, we obtain p0 ≥1/|E(G)|. Then with O(|E(G)|) repetitions of the QAOA circuit and measurement, we
obtain a sample with cut at least ⌊|E(G)|˜cedge(p)⌋, with probability at least 2/3 (or any constant probability
below 1).

5
Numerical results and methods

5.1
Results

Table 1: cedge at optimized angles ˜γ and ˜β as a function of p up to p = 17.

In order to maximize the quantum expected value of the cut size, we numerically evaluate the quantum
expectation value of the cost function of Eq. (4).
As we emphasized before, at the QAOA depths we
consider, on these high girth graphs, each edge has an isomorphic tree neighborhood and so each edge gives
the same contribution. We find values of (γ, β) that approximately maximize cedge(γ, β). For fixed (γ, β)

6

## Page 7

Figure 4:
We plot ˜cedge which is cedge at optimized angles ˜γ and ˜β as a function of 1/p. The value 0.912
is the lower bound on limg→∞Mg given by Refs. [5, 6]. If ˜cedge were to exceed this value at larger p, it
would provide a new lower bound on limg→∞Mg. The value 0.9239 is the upper bound on the expected cut
fraction of large random 3-regular graphs given in [16], and ˜cedge cannot exceed this value.

the quantum expectation is evaluated using the tensor network contraction method described in Section 5.2.
The blue crosses in Fig. 2 show the optimized values of cedge(γ, β) at approximately optimal parameters,
˜cedge(p) = cedge(˜γ, ˜β). The values are listed in Table 1. The parameters ˜γ and ˜β are shown in Fig. 3 for
different values of p.

5.2
Methods

In order to evaluate cedge(γ, β), we consider the operator ZiZj, as well as all quantum gates in the QAOA
circuit contained in the light cone of this operator. In the simple case of d = 2, i.e., when G is a line, the
tensor network that evaluates ⟨ZiZj⟩is that of Fig. 5(a). Here we have followed the tensor definitions:

=
1
√

(
eiγ
if a = b
e−iγ
if a ̸= b

2
∀a
=





1
if a = b = 0
−1
if a = b = 1
0
otherwise
(13)

(
cos (β)
if a = b
−i sin (β)
if a ̸= b
=

=




where all tensor indices have support {0, 1}. Note that every gate of the form eiγZiZj is diagonal, which we
explicitly exploit in writing its corresponding tensor over only two variables and making use of hyperindices
in the tensor network, corresponding to hyperedges in the underlying network.
In the generic case of d > 2 the number of qubits in the light-cone of the ZiZj operator grows exponentially
with p. For a 3-regular graph (i.e. d = 3), at p = 1, 2, 3, . . . the size of the light cone is 6, 14, 30, . . . In general,
for a d-regular graph, the number of qubits at depth p is 2 (d−1)p+1−1

7

d−2
. For d = 3 and p = 17 the size of the

## Page 8

light-cone is 524,286 qubits. However, due to the fact that all branches in the regular tree are identical, we
can perform this computation in a compact way that is not affected by the exponential growth in the number
of qubits in the calculation. We contract a single branch inwards towards the root of the tree, raising its
tensor entries to the (d −1)th power before proceeding to the next level of the tree. This is expressed in
graphical notation in Fig. 5(b), where we have made use of the definition

≡
(Ta1,a2,...,an)d−1
(14)

for the entrywise exponentiation of a tensor. Note that the cost of the evaluation of Eq. (8) as expressed in
Fig. 5(b) has both time and space complexities that grow as O(22p). This is quadratically better than the
time complexity reported in Refs. [11] and [12] for finite d. Note also that the cost is independent of d, in
contrast to that of the method used in Ref. [10], which scales exponentially in d and was run up to p = 11
at d = 3 and lower values of p at larger d. This allows us to evaluate and optimize Eq. (8) up to p = 17 for
any value of d. Our implementation of the method is written in C++ and parallelized using OpenMP [17].
We also make use of the Eigen library for the manipulation of vectors [18] as well as the LBFGS++ library,
which implements the Limited-memory BFGS algorithm for unconstrained optimization problems [19].
We remind the reader that all of our numerical methods are exact.
We use computers to evaluate
expressions, but there are no approximations. For d = 3 and at depth p we evaluate cedge(γ, β) on a tree
with (2(p+2) −2) vertices at a computational cost of O(4p). We go to p of 17. An alternate approach would
be to use a quantum computer with (2(p+2) −2) qubits. Here we would evaluate the central edge of the tree
using the full QAOA cost. Although we would be running a quantum computer, we would not be finding
cuts but rather estimates of lower bounds on MaxCut values. It appears that this scales more favorably than
our exact calculation of lower bounds, at least while d ≤4. For this method to go beyond our p = 17 result
requires a highly accurate quantum computer capable of handling graphs with at least one million vertices.
Repeated measurements would extract an accurate estimate of the quantum expectation but not a proof of
a lower bound.

6
MaxCut Comparisons

We can directly compare our results with those of Thompson, Parekh and Marwaha [4]. They have a classical
algorithm for MaxCut which they apply to large girth graphs. They lower bound the performance of their
algorithm to obtain lower bounds on Mg for all g. Using the formula found in Theorem 1 of their paper we
can compare with our results. See Fig. 2. For any g ≥16 the QAOA (at appropriate p) finds cuts bigger
than the TPM guarantees. Note that the limit as g goes to infinity of their bound is 0.8918 which we exceed
at g of 32.
The results of Cs´oka et al [5] and Gamarnik and Li [6] imply that the limit as g goes to infinity of Mg is
greater than or equal to 0.912. (These methods could in principle be used to find bounds on Mg for finite
g, but as far as we know this has not been done.) Our numerical techniques are stretched to the limit at p
of 17 and we do not have an analytic way of taking p to infinity. See Fig. 4 where we plot ˜cedge versus 1/p
and also show the target of 0.912. The reader can decide if we pass this target as p increases, an empirical
question left for future computations.
The graphs which we have considered have large girth and every edge sits in a tree neighborhood. We
can ask about large random 3-regular graphs where almost all edges sit in tree neighborhoods. Such graphs
have an order unity number of triangles, squares, pentagons, or any cycle of constant length, which means
that they are not strictly large girth. However, since there are so few short cycles, any lower bound on Mg
for any g is a lower bound on the cut fraction of a typical large random 3-regular graph [6]. Furthermore

8

## Page 9

(a)

(b)

Figure 5: Tensor network for the computation of ⟨γ, β|ZiZj|γ, β⟩for p = 3. On the left (a) we have d = 2
and on the right (b) arbitrary d. In the latter case, the tensor network diagramatic notation is extended
to denote extry-wise exponentiation of a tensor. In particular, the result of contracting the tensors in one
of the colored boxes is raised to the power (d −1) before proceeding to later contractions, as expressed in
Eq. (14). The time and space complexities of the contraction performed in this way are both O(22p). The
complexity does not depend on d. Higher values of p are tackled in a similar fashion.

the QAOA at level p achieves cut fraction ˜cedge(p) on these graphs. There is an upper bound on the cut
fraction of typical large random 3-regular graphs of 0.9239 [16], building on Refs. [20, 21, 22, 23]. Therefore
the QAOA cut fraction ˜cedge(p) cannot exceed 0.9239 even as p →∞. This value is shown in Fig. 4.

7
Maximum Independent Set

An independent set is a subset of the vertices of a graph with the property that there are no edges between
any two members of the subset.
The Maximum Independent Set problem (MIS) is to find the biggest
independent set. The MIS problem is NP-hard for general graphs. Here we will use a general connection
between independent sets and MaxCut that allows us to use our MaxCut results to get quick bounds on the
independence ratio which is the fraction of vertices in the largest independent set. We then apply a variant
of the QAOA to large-girth 3-regular graphs to establish better bounds on the independence ratio. We are
not aware of any other bounds for MIS on this class of fixed girth graphs. However there are results in the
limit as the girth goes to infinity [24].
A convenient local cost function for the MIS problem is

I1 =
X

i∈V
bi −
X

⟨i,j⟩∈E
bibj,
(15)

written as a function of the bit string (b1, . . . , b|V |), where each bit string also represents a subset of the
vertex set V , with bi = 1 if vertex i is in the subset. Note this cost function is defined on all subsets and
not just independent sets. The first term of I1 is the Hamming weight which we want to make big, and the
subtracted term counts violations of the independent set property. We now argue that given any bit string
with associated cost I1, there exists an independent set of size at least I1. In particular, we consider the set
of vertices labeled 1 in the bit string, and we construct a subset of these vertices that forms an independent

9

## Page 10

set of size at least I1. To begin, given a bit string with cost I1, assume that the set of 1’s is not yet an
independent set. Choose any violated edge ⟨i, j⟩, that is with bi = bj = 1, then choose either i or j and
re-label it as 0, that is, remove the vertex from the set under consideration. Consider the cost function I1
for this new string: the bit flip decreases the Hamming weight by 1 and decreases the number of violations
by at least 1, so I1 cannot decrease. Repeat this until there are no more violations so the final bit string
must have 1’s that form a valid independent set. The new value of I1 is equal the size of the independent
set which must be at least the original value of I1. Now the maximum of I1 occurs when b corresponds to
an actual maximum independent set so achieving a high value of I1 gives an approximation to the size of
the largest independent set.
We now use the connection between MaxCut and independent sets to get a general bound on MIS.
Consider the problem of maximizing the total number of vertices in two disjoint independent sets.
We
consider a cost function given by the sum of two terms, one for each set:







X

i∈V
bi −
X

X

I2 =

⟨i,j⟩∈E
bibj

+



i∈V
(1 −bi) −
X

⟨i,j⟩∈E
(1 −bi)(1 −bj)

.
(16)

Write the two terms as I2 = I2,1 + I2,0. For any input bit string, the 1’s represent one set and the 0’s the
complementary set. (Note that 0 and 1 here do not mean what they meant in the previous paragraph.) By
the above argument regarding I1, first applied to I2,1, there exists a subset of 1’s that forms an independent
set, with size at least I2,1. Meanwhile, the same argument applied to I2,0 implies there exists a subset of 0’s
that forms an independent set, with size at least I2,0. Thus we have two disjoint independent sets of total
size at least I2.
We can rewrite Eq. (16) to get

I2 = |V | −|E| +
X

⟨i,j⟩∈E
(bi + bj −2bibj)
(17)

where the sum on edges is the MaxCut cost. Let w be the maximum fraction of combined vertices in two
disjoint independent sets. Then for any graph,

|V | = 1 −|E|

w ≥I2

|V | + C(b)

|V |
(18)

where C(b) is the cut size associated to any bit string b. For 3-regular graphs we get

w ≥3

2
C(b)

|E| −1

2.
(19)

As an aside, we note an interesting relation between w and µ, where µ denotes the cut fraction of the
best cut:
w = 3

2µ −1

2.
(20)

Table 2: Independence ratio achieved by the QAOA for various values of p.

10

## Page 11

Figure 6:
We plot the independence ratio for the MIS problem as a function of 1/p. The value 0.4453
is the best available bound on the independence ratio for large-girth 3-regular graphs Ref. [24]. We show
bounds on the independence ratio for angles γ and β optimized for MaxCut, as well as the set of parameters
(γ, γ′, β) (see expression (28)). In the latter case we necessarily achieve larger values of the independence
ratio, although the improvement over the (γ, β) alternative decreases with p.

To see this, first note

w ≥3

2µ −1

2,
(21)

which follows immediately from Eq. (19). This holds for any 3-regular graph with no restriction on girth.
Now we refer to Gamarnik and Li [6]. From the argument in their Section 6, one can deduce

µ ≥2

3w + 1

3.
(22)

Together, these two inequalities yield the claimed Eq. (20) and we end our aside.
Let ir be the independence ratio, the fraction of vertices in the largest independent set. Then ir ≥w/2,
since one of the two independent sets must contain at least half of their combined vertices. So from Eq. (19)
we have

ir ≥3

4
C(b)

|E| −1

4.
(23)

Taking the quantum expectation and using our MaxCut result for large girth 3-regular graphs we have

ir ≥3

4˜cedge(p) −1

4 .
(24)

So we now have a lower bound on the independence ratio ir for any g ≥2p+2 using the values from Table 1.
These values are given as the first line in Table 2. In particular for girth at least 36 we get a lower bound of
0.4228.
But we can do better. Return to the cost function of Eq. (15). First we need to write it as a sum over
edges. For 3-regular graphs,

1

I1 =
X

⟨i,j⟩∈E

11


.
(25)

3(bi + bj) −bibj

## Page 12

Figure 7: Optimized parameters ˜γ, ˜γ′ and ˜β as a function of (j −1)/(p −1) for different values of p up to
p=15 for the MIS problem.

Now using the fact that bi = (1 −zi)/2 we can write the cost in terms of the Zi operators which is more
convenient,
X

1

1


−1

2 −1

2ZiZj

2

⟨i,j⟩∈E

12(Zi + Zj)

.
(26)

6 + 1

Again we are looking at graphs with g ≥2p+2 so each edge makes an identical contribution to the quantum
expectation in the QAOA state. The quantum expectation equals the contribution from any edge times the
number of edges |E|, that is,

⟨ψ|
1

1


−1

2 −1

6 + 1

2ZiZj

2

12(Zi + Zj)

|ψ⟩× |E|
(27)

where as before ⟨i, j⟩is any edge in the graph, and |ψ⟩is some state produced by the QAOA.
We are free to use any local operator to drive the QAOA. Here we modify the cost function part of the
driver and but not the sum of the X’s. We will introduce two parameters, γ and γ′, for each layer of the
cost function unitary. In particular for the driving cost function operator we try

γ
X

⟨i,j⟩∈E
ZiZj + γ′ X

i∈V
Zi.
(28)

Including the β at each layer there are a total of 3p parameters.
If γ′ = 0, this amounts to using the
MaxCut cost function as the driver. Using symmetry we can show that the linear term in the objective in
expression (27) vanishes. So in fact with γ′ = 0 both the driver and objective function are those of MaxCut
up to constants. Noting that |E| = 3

2|V | and dividing (27) by |V | gives, at optimal parameters, the right
hand side of (24). If the ratio of γ to γ′ is set to the right constant, see expression (26), then the driver
is the same as the objective function. So if we optimize over all γ’s and γ′’s and β’s we do at least as well
as using the MaxCut cost function as the driver or the local MIS cost function as the driver. In Table 2 we
give lower bounds on the independence ratio for MIS produced by this optimization over 3p parameters.
In Fig. 6 we show the lower bounds we get on the independence ratio as a function of 1/p from our
MaxCut results and using the 3-parameter per layer ansatz. The 3-parameter ansatz must lie above the
other but the difference shrinks as p grows. The red line is the best available bound on the independence
ratio for large girth 3-regular graphs as the girth goes to infinity [24]. The optimized parameters (˜γ, ˜γ′, ˜β)
are shown in Fig. 7 for different values of p.
To find independent sets which meet these guarantees you can run the QAOA on quantum hardware with
constant circuit depth for a constant p. This gives a polynomial-time quantum algorithm for this problem.

12

## Page 13

We know of no classical algorithm that performs as well (in terms of guaranteed independence ratio) on the
problem of MIS on 3-regular graphs of girth at least g.

8
Conclusions

We proved a new lower bound for MaxCut on high-girth graphs by using a classical computer to analyze
the performance of a quantum algorithm. This graph-theoretic result holds even if quantum computing is
infeasible. We are unaware of other examples where the analysis of quantum algorithmic performance yields
similarly novel results.
Running the quantum algorithm on a quantum computer would efficiently find the actual cuts that
achieve our lower bounds. This provides an exponential speedup for finding these cuts, compared to known
classical algorithms with rigorous guarantees.

9
Acknowledgements

This project was an outgrowth of a project which included Brandon Augustino, Madelyn Cain, Swati Gupta,
Eugene Tang and Katherine Van Kirk. We are grateful to them for getting us going. We also thank Ojas
Parekh and Kunal Marwaha for reading our manuscript. We thank David Gamarnik for suggesting that
we look at MIS. We thank Joao Basso, Stephen Jordan and Mario Szegedy for helpful comments and Leo
Zhou for introducing the idea of the last paragraph of Section 5.2. DR acknowledges support by the Simons
Foundation under grant 376205.

References

[1] Richard M Karp. On the computational complexity of combinatorial problems. Networks, 5(1):45–68,
1975.

[2] Mihalis Yannakakis. Node-and edge-deletion np-complete problems. In Proceedings of the tenth annual
ACM symposium on Theory of computing, pages 253–264, 1978.

[3] Edward Farhi, Jeffrey Goldstone, and Sam Gutmann. A quantum approximate optimization algorithm.
arXiv:1411.4028, 2014.

[4] Jessica K Thompson, Ojas Parekh, and Kunal Marwaha. An explicit vector algorithm for high-girth
maxcut. In Symposium on Simplicity in Algorithms (SOSA), pages 238–246. SIAM, 2022.

[5] Endre Cs´oka, Bal´azs Gerencs´er, Viktor Harangi, and B´alint Vir´ag. Invariant gaussian processes and
independent sets on regular graphs of large girth. Random Structures & Algorithms, 47(2):284–303,
2015.

[6] David Gamarnik and Quan Li.
On the max-cut of sparse random graphs.
Random Structures &
Algorithms, 52(2):219–262, 2018.

[7] Michel X Goemans and David P Williamson. Improved approximation algorithms for maximum cut and
satisfiability problems using semidefinite programming. Journal of the ACM (JACM), 42(6):1115–1145,
1995.

[8] Eran Halperin, Dror Livnat, and Uri Zwick. Max cut in cubic graphs. Journal of Algorithms, 53(2):169–
185, 2004.

[9] Subhash Khot. On the power of unique 2-prover 1-round games. In Proceedings of the thiry-fourth
annual ACM symposium on Theory of computing, pages 767–775, 2002.

13

## Page 14

[10] Jonathan Wurtz and Danylo Lykov. The fixed angle conjecture for qaoa on regular maxcut graphs.
arXiv:2107.00677, 2021.

[11] Joao Basso, Edward Farhi, Kunal Marwaha, Benjamin Villalonga, and Leo Zhou. The Quantum Ap-
proximate Optimization Algorithm at High Depth for MaxCut on Large-Girth Regular Graphs and the
Sherrington-Kirkpatrick Model. In Fran¸cois Le Gall and Tomoyuki Morimae, editors, 17th Conference
on the Theory of Quantum Computation, Communication and Cryptography (TQC 2022), volume 232
of Leibniz International Proceedings in Informatics (LIPIcs), pages 7:1–7:21, Dagstuhl, Germany, 2022.
Schloss Dagstuhl – Leibniz-Zentrum f¨ur Informatik.

[12] Elisabeth Wybo and Martin Leib. Missing puzzle pieces in the performance landscape of the quantum
approximate optimization algorithm. arXiv:2406.14618, 2024.

[13] Ryan Williams. A new algorithm for optimal 2-constraint satisfaction and its implications. Theoretical
Computer Science, 348(2-3):357–365, 2005.

[14] Mario Szegedy. What do qaoa energies reveal about graphs? arXiv:1912.12277, 2019.

[15] Anton Bernshteyn and Abhishek Dhawan. Fast algorithms for vizing’s theorem on bounded degree
graphs. arXiv:2303.05408, 2023.

[16] Viktor Harangi. Rsb bounds on the maximum cut. arXiv:2506.21296, 2025.

[17] Leonardo Dagum and Ramesh Menon. OpenMP: an industry standard API for shared-memory pro-
gramming. Computational Science & Engineering, IEEE, 5(1):46–55, 1998.

[18] Ga¨el Guennebaud, Benoˆıt Jacob, et al. Eigen v3. Online, 2010.

[19] Yixuan Qiu and Dirk Toewe. LBFGS++. Online, 2020.

[20] Amin Coja-Oghlan, Philipp Loick, Bal´azs F Mezei, and Gregory B Sorkin. The ising antiferromagnet
and max cut on random regular graphs. SIAM Journal on Discrete Mathematics, 36(2):1306–1342,
2022.

[21] Lenka Zdeborov´a and Stefan Boettcher. A conjecture on the maximum cut and bisection width in
random regular graphs. Journal of Statistical Mechanics: Theory and Experiment, 2010(02):P02020,
2010.

[22] Frantiˇsek Kardoˇs, Daniel Kr´al, and Jan Volec. Maximum edge-cuts in cubic graphs with large girth and
in random cubic graphs. Random Structures & Algorithms, 41(4):506–520, 2012.

[23] Brendan D McKay. Maximum bipartite subgraphs of regular graphs with large girth. In Proc. 13th SE
Conf. on Combin. Graph Theory and Computing, Boca Raton, Florida, volume 436, 1982.

[24] Endre Cs´oka. Independent sets and cuts in large-girth regular graphs. arXiv:1602.02747, 2016.

14
