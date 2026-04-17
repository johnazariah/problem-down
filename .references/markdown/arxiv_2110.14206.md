---
source_pdf: ../arxiv_2110.14206.pdf
pages: 39
extracted_at: 2026-04-17T12:32:41+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_2110.14206

Source PDF: ../arxiv_2110.14206.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

The Quantum Approximate Optimization Algorithm at High Depth
for MaxCut on Large-Girth Regular Graphs
and the Sherrington-Kirkpatrick Model

ID Joao Basso1, Edward Farhi1,2,
ID Kunal Marwaha3,

ID Benjamin Villalonga1, and
ID Leo Zhou4

arXiv:2110.14206v3 [quant-ph] 7 Jul 2022

1 Google Quantum AI, Venice, CA 90291
2 Center for Theoretical Physics, Massachusetts Institute of Technology, Cambridge, MA 02139
3 Department of Computer Science, University of Chicago, Chicago, IL 60637
4 Walter Burke Institute for Theoretical Physics, California Institute of Technology, Pasadena, CA 91125

July 6, 2022

Abstract

The Quantum Approximate Optimization Algorithm (QAOA) ﬁnds approximate

solutions to combinatorial optimization problems. Its performance monotonically im-

proves with its depth p.
We apply the QAOA to MaxCut on large-girth D-regular

graphs. We give an iterative formula to evaluate performance for any D at any depth p.

Looking at random D-regular graphs, at optimal parameters and as D goes to inﬁnity,

we ﬁnd that the p = 11 QAOA beats all classical algorithms (known to the authors) that

are free of unproven conjectures. While the iterative formula for these D-regular graphs

is derived by looking at a single tree subgraph, we prove that it also gives the ensemble-

averaged performance of the QAOA on the Sherrington-Kirkpatrick (SK) model deﬁned

on the complete graph. We also generalize our formula to Max-q-XORSAT on large-

girth regular hypergraphs. Our iteration is a compact procedure, but its computational

complexity grows as O(p24p). This iteration is more eﬃcient than the previous proce-

dure for analyzing QAOA performance on the SK model, and we are able to numerically

go to p = 20. Encouraged by our ﬁndings, we make the optimistic conjecture that the

QAOA, as p goes to inﬁnity, will achieve the Parisi value. We analyze the performance

of the quantum algorithm, but one needs to run it on a quantum computer to produce

a string with the guaranteed performance.

## Page 2

Contents

1
Introduction
3

2
Background on the QAOA and MaxCut
4

3
The QAOA on large-girth (D + 1)-regular graphs
5
3.1
An iteration for any ﬁnite D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
3.2
An iteration for D →∞. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6

4
Proof of the iterations
7
4.1
Proof of the ﬁnite D iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
4.2
Proof of D →∞iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10

5
Numerical evaluation and optimization
12

6
Agreement with the Sherrington-Kirkpatrick model
14

7
Conjecture that our iteration achieves the Parisi value
18

8
Generalized iterations for Max-q-XORSAT
19
8.1
J-independence of ν[q]
p
and implied worst-case limitation . . . . . . . . . . . . . . . .
20
8.2
An iteration for any ﬁnite D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
8.3
An iteration for D →∞. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
8.4
Proof of the ﬁnite D iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
8.5
Proof of the D →∞iteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
8.6
Numerical evaluation of the Max-q-XORSAT performance at inﬁnite D
. . . . . . .
24

9
Discussion
25

A Properties of the iterations
29
A.1 Properties of f(a)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
A.2 Properties of H(m)
D (a)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
A.3 Symmetries of the G(m) matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
A.4 Placement of the matrix elements of G(m) . . . . . . . . . . . . . . . . . . . . . . . .
35

B A lemma needed in Section 6
37

C Tables of best known γ, β for MaxCut
38

D Optimal γ and β for Max-q-XORSAT at p = 14
39

2

## Page 3

1
Introduction

We are at the start of an era in which quantum devices are running algorithms. We need to under-
stand the power of quantum computers for solving or ﬁnding approximate solutions to combinatorial
optimization problems. One approach is to learn by experimenting on hardware. Although useful
for probing the hardware and testing algorithms at small sizes, it does not give a convincing picture
of asymptotic behavior. To this end we need mathematical studies of the behavior of quantum al-
gorithms, running on ideal circuits, at large sizes. In this paper we take a step in that direction by
analyzing the Quantum Approximate Optimization Algorithm as applied to a certain combinatorial
optimization problem. The instances are large and the depth of the algorithm is high. For this
task, we will see that the QAOA outperforms the best assumption-free classical algorithm.
MaxCut is a combinatorial optimization problem on bit strings whose input is a graph. Each bit
is associated with a vertex, and the goal is to maximize the number of edges with bit assignments
that disagree on the two ends of the edge. It is NP-hard to solve this problem exactly, and even
approximating the optimal solution beyond a certain ratio is NP-hard [1]. We focus on MaxCut
for large-girth D-regular graphs. On these graphs, the currently known best classical algorithms
without assuming any unproven conjectures (including Goemans-Williamson and the Gaussian
wave process [2, 3, 4, 5]) achieve an expected cut fraction (the number of cut edges output by the
algorithm divided by the number of edges) of 1/2 + (2/π)/
√

D as both the girth and D go to ∞,
where 2/π ≈0.6366.
We apply the Quantum Approximate Optimization Algorithm (QAOA) [6] to large-girth D-
regular graphs. The QAOA depends on a parameter p, the algorithm’s depth. At small p, the
QAOA has been realized in current quantum hardware [7]. Some analytic results are also known.
At p = 1, the QAOA has a guaranteed approximation ratio (the number of cut edges output by
the algorithm divided by the maximum number of edges that can be cut) of at least 0.6924 on
all 3-regular graphs [6] and an expected cut fraction of at least 1/2 + 0.3032/
√

D on triangle-free
graphs [8]. For p = 2, the QAOA has an approximation ratio of at least 0.7559 on 3-regular graphs
with girth more than 5 and, for p = 3, that ratio becomes 0.7924 when the girth is more than 7
[9]. So far, expressions for the QAOA’s performance on any ﬁxed-D regular, large-girth graph are
known only for p = 1 [8] and p = 2 [10].
In this work, we analyze the performance of the QAOA on any large-girth D-regular graph for
any choice of p by looking at a single tree subgraph. Using the regularity of this tree subgraph,
we derive an iteration that computes the performance of the QAOA. After optimizing over the 2p
input parameters, we ﬁnd that the p = 11 QAOA improves on 1/2 + (2/π)/
√

D, when D is large
and the girth is more than 23. This is better than all assumption-free classical algorithms known
to the authors.1

We also show that this performance, obtained from one subgraph, is mathematically equal
to the ensemble-averaged performance of the QAOA applied to the Sherrington-Kirkpatrick (SK)
model [13]. This implies that the iteration in this paper can also be used to give the QAOA’s
performance on the SK model. A recent related work can be found in Ref. [14]. Our iteration is
more eﬃcient than the one originally shown in Ref. [13], and we have been able to go numerically
to higher depth.
Encouraged by our ﬁndings, we conjecture that the large p performance of the QAOA will
achieve the optimal cut fraction on large random D-regular graphs, where a vanishing fraction of
neighborhoods are not locally tree-like. The optimal cut fraction on these graphs is also related to

1There is a recent classical message-passing algorithm [11] that also does better than 1/2+(2/π)/
√

D for MaxCut
on large-girth D-regular graphs. It gets asymptotically close to the optimum assuming the solution space has no
“overlap gap property” (see [12] for a review).

3

## Page 4

the SK model. It is 1/2 + Π∗/
√

D + o(1/
√

D), where Π∗= 0.763166 . . ., the Parisi value, is the
ground state energy density of the SK model [15, 16]. If our conjecture is right we have a simple,
though computationally intensive, new iteration for calculating the Parisi value Π∗.
Generalizing our formalism, we also analyze the performance of the QAOA for Max-q-XORSAT
(of which MaxCut is a special case at q = 2) on large-girth D-regular hypergraphs. The p = 1 QAOA
was recently found to do better than an analogous classical threshold algorithm for q > 4 [17]. The
iterative formula for general q is very similar to that for MaxCut and has the same time and memory
complexities in the D →∞limit. We run this iteration to ﬁnd optimal QAOA parameters and
performance for 3 ≤q ≤6 and 1 ≤p ≤14. Moreover, we discuss potential obstructions to the
QAOA from not “seeing” the whole graph.

2
Background on the QAOA and MaxCut

The QAOA [6] is a quantum algorithm for ﬁnding approximate solutions to combinatorial opti-
mization problems. The cost function counts the number of clauses satisﬁed by an input string.
Given a cost function C(z) on strings z ∈{±1}n, we can deﬁne a corresponding quantum operator,
diagonal in the computational basis, as C|z⟩= C(z)|z⟩. Moreover, let B = Pn
j=1 Xj, where Xj
is the Pauli X operator acting on qubit j. Let γ = (γ1, γ2, . . . , γp) and β = (β1, β2, . . . , βp). The
QAOA initializes the system of qubits in the state |s⟩= |+⟩⊗n and applies p alternating layers of
e−iγjC and e−iβjB to prepare the state

|γ, β⟩= e−iβpBe−iγpC · · · e−iβ1Be−iγ1C|s⟩.
(2.1)

For a given cost function C, the corresponding QAOA objective function is ⟨γ, β|C|γ, β⟩. Preparing
the quantum state |γ, β⟩and then measuring in the computational basis enough times, one will
ﬁnd a bit string z such that C(z) is near ⟨γ, β|C|γ, β⟩or better.
We study the performance of the QAOA on MaxCut. Given a graph G = (V, E) with vertices
in V and edges in E, the MaxCut cost function is

CMC(z) =
X

(u,v)∈E

1
2(1 −zuzv).
(2.2)

We restrict our attention to graphs that are regular and have girth greater than 2p + 1. We work
with these graphs because the subgraph that the QAOA at depth p sees on them are regular trees
and this enables our calculation. Here, by “seeing” we refer to the fact that the output of the
QAOA on a qubit depends only on a neighborhood of qubits that are within distance p to the
given qubit on the graph. In what follows, we focus on (D + 1)-regular graphs, which implies the
subgraph seen by the QAOA on each edge is a D-ary tree.
With D large, we will see that the optimal γ are of order 1/
√

D. So we ﬁnd it convenient to
prepare the QAOA state |γ, β⟩using the scaled cost function operator

C = −1
√

X

D

(u,v)∈E
ZuZv,
(2.3)

where we have subtracted a constant that only introduces an irrelevant phase. The factor of 1/2
has been dropped so that this form of the cost function will match the cost function used in the
Sherrington-Kirkpatrick model. Note we are preparing the state |γ, β⟩using C as a driver instead
of the CMC operator. With this scaling, the optimal γ will be of order unity instead of 1/
√

D.
Given any edge in a (D + 1)-regular graph with girth greater than 2p + 1 the subgraph with
vertices at most p away from the edge is a D-ary tree regardless of which edge. Since the QAOA

4

## Page 5

at depth p only sees these trees, we have

⟨γ, β|CMC|γ, β⟩= 1

2|E|

1 −⟨γ, β|ZuZv|γ, β⟩

(2.4)

where (u, v) ∈E is any edge. The cut fraction output by the QAOA is then

⟨γ, β|CMC|γ, β⟩

|E|
= 1

2 −1

2 ⟨γ, β|ZuZv|γ, β⟩.
(2.5)

Since the QAOA cannot beat the optimal cut fraction of 1/2 + order(1/
√

D) in a typical random
regular graph, we write
1
2 ⟨γ, β|ZuZv|γ, β⟩= −νp(D, γ, β)
√

D
(2.6)

where νp(D, γ, β) for good parameters will be of order unity.

3
The QAOA on large-girth (D + 1)-regular graphs

We describe two iterations to evaluate the performance of the QAOA at high depth on MaxCut on
large-girth (D + 1)-regular graphs. The cut fraction output by the QAOA at any parameters is

⟨γ, β|CMC|γ, β⟩

|E|
= 1

2 + νp(D, γ, β)
√

D
.
(3.1)

We give one iteration to evaluate νp(D, γ, β) at ﬁnite D, and one for the D →∞limit. We have
attempted to make this section self-contained for those readers only interested in the form of the
iterations, and deferred the detailed proofs of these iterations to Section 4.
In what follows, we index vectors in the following order:

a = (a1, a2, · · ·, ap, a0, a−p, · · · , a−2, a−1) .
(3.2)

Deﬁne, for 1 ≤r ≤p,

Γr = γr,
Γ0 = 0,
Γ−r = −γr.
(3.3)

That is, Γ is a (2p + 1)-component vector. Furthermore, let

f(a) = 1

2 ⟨a1|eiβ1X|a2⟩· · · ⟨ap−1|eiβp−1X|ap⟩⟨ap|eiβpX|a0⟩

× ⟨a0|e−iβpX|a−p⟩⟨a−p|e−iβp−1X|a−(p−1)⟩· · · ⟨a−2|e−iβ1X|a−1⟩
(3.4)

where ai ∈{+1, −1} enumerates the two computational basis states, and

⟨a1|eiβX|a2⟩=

3.1
An iteration for any ﬁnite D

(
cos(β)
if a1 = a2
i sin(β)
if a1 ̸= a2.
(3.5)

Here we give an iteration that allows us to evaluate νp(D, γ, β) for any input parameters and D.
Let H(m)
D
: {−1, 1}2p+1 →C for 0 ≤m ≤p with

5

H(0)
D (a) = 1
(3.6)

## Page 6

and

H(m)
D (a) =
 X

b
f(b)H(m−1)
D
(b) cos
h
1
√

DΓ · (ab)
iD
for 1 ≤m ≤p
(3.7)

where we denote ab as the entry-wise product, i.e. (ab)j = ajbj. By starting with H(0)
D (a) = 1
and iteratively evaluating Eq. (3.7) for m = 1, 2, . . . , p, we arrive at H(p)
D (a) that can be used to
compute

νp(D, γ, β) = i
√

a,b
a0b0f(a)f(b)H(p)
D (a)H(p)
D (b) sin
h
1
√

D
2
X

DΓ · (ab)
i
.
(3.8)

We prove this in Section 4.1.
Note that each step of the above iteration involves a sum with 22p+1 terms for each of the 22p+1

entries of H(m)
D (a). The ﬁnal step has a sum with O(16p) terms. Overall, this iteration has a time
complexity of O(p 16p) and a memory complexity of O(4p). This is much faster than the original
“light cone” approach that directly evaluates ⟨ZuZv⟩on the subgraph seen by the QAOA [6]. That
procedure takes 2O(Dp) time without utilizing the symmetric structure of the regular tree subgraph.

3.2
An iteration for D →∞

We ﬁnd that in the inﬁnite D limit we get a more compact iteration which takes fewer steps to
evaluate. We state the result here and prove it in Section 4.2.
Deﬁne matrices G(m) ∈C(2p+1)×(2p+1) for 0 ≤m ≤p as follows. For j, k ∈{1, . . . , p, 0, −p, . . . ,
−1}, let
G(0)
j,k =
X

and

p
X

a
f(a)ajak exp

−1

G(m)
j,k =
X

2

a
f(a)ajak
(3.9)

j′,k′=−p
G(m−1)
j′,k′
Γj′Γk′aj′ak′

for 1 ≤m ≤p.
(3.10)

Starting at m = 0 and going up by p steps, we arrive at G(p) which is used to compute

p
X

νp(γ, β) := lim
D→∞νp(D, γ, β) = i

j=−p
Γj(G(p)
0,j)2.
(3.11)

2

Since there are p + 1 matrices with O(p2) entries, and each involves a sum over O(4p) terms, this
iteration na¨ıvely has a time complexity of O(p34p). This is quadratically better than the time
complexity of the ﬁnite-D formula. The memory complexity is only O(p2) for storing the G(m)

matrix, which is exponentially better than O(4p) memory needed to store the entries of H(m)
D
in
the ﬁnite-D iteration.
We note some properties about this iteration. Superﬁcially Eq. (3.10) looks like a recursive map
on the matrices G(m) which one might think would only asymptotically converge in the number
of steps. However it converges to a ﬁxed point G(p) after p steps in a highly structured way. In
particular, the iteration has the following three sets of properties, which we prove in Appendix A.
We use the convention 1 ≤r < s ≤p and j, k ∈{1, . . . , p, 0, −p, . . . , −1}.

(a) Values of the diagonal and anti-diagonal of G(m) are all 1. G(m) is symmetric with respect to
the diagonal, reﬂection with respect to the anti-diagonal results in complex conjugation, and
the matrix consists of 8 triangular regions which are rotations, reﬂections, and/or complex
conjugations of each other. To be precise, G(m) satisﬁes the following properties:

6

## Page 7

(1) G(m)
j,k = G(m)
k,j

(2) G(m)
j,j = G(m)
j,−j = 1

These are sketched in Fig. 1.

(3) G(m)
0,r = G(m)∗
0,−r

(4) G(m)
r,s = G(m)
r,−s = G(m)∗
−r,−s = G(m)∗
−r,s

(b) G(m)
r,s only depends on G(m−1)
r′,s′
where 1 ≤r′ < s′ < s. Similarly, G(m)
0,r only depends on G(m−1)
r′,s′
for 1 ≤r′ < s′ ≤p.

(c) As a consequence of (b), at each step m of the iteration the corner blocks of size (m+1)×(m+1)
of G(m) converge to their ﬁnal value, i.e., they reach a ﬁxed point and do not change in later
iteration steps. This implies that matrix G(p) is a ﬁxed point. This is sketched in Fig. 1,
where matrix entries of the same color reach their ﬁxed point at the same step of the iteration,
starting from the corners and ending with the central “cross” at step p.

Making use of (b) and some properties of f(a) allows us to lower the complexity of the iterative
procedure to O(p24p). We show this in Appendix A.4.

Figure 1: Sketch of the properties of matrices G(m) in the iterative formula of Section 3.2, at p = 4.
Regions of the same color converge in the same iteration step, starting from the corners and with
the central row and column converging after p steps.

4
Proof of the iterations

In this section, we prove the correctness of the two iterations in Section 3.1 and Section 3.2. These
proofs illustrate two key technical ideas in this paper: namely, we can exploit the regularity of the
tree subgraph seen by the QAOA to yield a compact formula for its performance, and we ﬁnd an
algebraic simpliﬁcation in the D →∞limit. The reader not interested in the techniques can skip
to Section 5.

4.1
Proof of the ﬁnite D iteration

We now prove the ﬁnite D iteration that was stated in Section 3.1. We focus on the iteration for
p = 2 as an example, and its generalization to other p is immediate.

7

## Page 8

Figure 2: The tree subgraph seen by the QAOA at p = 2 for the edge (L, R) on a (D + 1)-regular
graph with girth > 2p+1. For any node v on either of the D-ary trees we denote p(v) as the parent
of that node. In the ﬁgure w is a leaf node, and we show its parent and its parent’s parent.

The goal is to evaluate the energy expectation for a single edge (L, R) on a (D + 1)-regular
graph whose girth is larger than 2p + 1. For p = 2, this is

⟨γ, β|ZLZR|γ, β⟩= ⟨s|eiγ1Ceiβ1Beiγ2Ceiβ2BZLZRe−iβ2Be−iγ2Ce−iβ1Be−iγ1C|s⟩
(4.1)

where C = −(1/
√

D) P
(u,v)∈E ZuZv, and E denotes the set of edges for the given graph. In the
Heisenberg picture, it can be seen that the operator eiγ1C · · · eiβpBZLZRe−iβpB · · · e−iγ1C only acts
nontrivially on the subgraph induced by including all vertices distance p or less from either node
L or R. For a (D + 1)-regular graph with girth greater than 2p + 1, this subgraph looks like a pair
of D-ary trees that are glued at their roots (see Fig. 2), with a total of n = 2(Dp + · · · + D + 1)
nodes. In what follows, we compute Eq. (4.1) by restricting our attention to only the qubits in this
subgraph.
We start by inserting 5 complete sets in the computational Z-basis that we will label as
z[1], z[2], z[0], z[−2], and z[−1]. Each of these complete sets iterates over 2n basis states since the
number of qubits in the subgraph is n. Then

{z[i]}
⟨s|z[1]⟩eiγ1C(z[1]) ⟨z[1]|eiβ1B|z[2]⟩eiγ2C(z[2]) ⟨z[2]|eiβ2B|z[0]⟩z[0]
L z[0]
R

⟨γ, β|ZLZR|γ, β⟩=
X

× ⟨z[0]|e−iβ2B|z[−2]⟩e−iγ2C(z[−2]) ⟨z[−2]|e−iβ1B|z[−1]⟩e−iγ1C(z[−1]) ⟨z[−1]|s⟩

= 1

{z[i]}
exp
h
iγ1C(z[1]) + iγ2C(z[2]) −iγ2C(z[−2]) −iγ1C(z[−1])
i
z[0]
L z[0]
R

2n
X

n
Y

v=1
⟨z[1]
v |eiβ1X|z[2]
v ⟩⟨z[2]
v |eiβ2X|z[0]
v ⟩⟨z[0]
v |e−iβ2X|z[−2]
v
⟩⟨z[−2]
v
|e−iβ1X|z[−1]
v
⟩.
(4.2)

×

Let us deﬁne the following function which is the p = 2 version of Eq. (3.4):

f(a1, a2, a0, a−2, a−1) = 1

2 ⟨a1|eiβ1X|a2⟩⟨a2|eiβ2X|a0⟩⟨a0|e−iβ2X|a−2⟩⟨a−2|e−iβ1X|a−1⟩.
(4.3)

8

## Page 9

Then, using Γ as deﬁned in Eq. (3.3), we can rewrite Eq. (4.2) as

{z[i]}
z[0]
L z[0]
R exp
h
i

⟨γ, β|ZLZR|γ, β⟩=
X

j=−2
ΓjC(z[j])
i
n
Y

2
X

v=1
f(zv)
(4.4)

where zv = (z[1]
v , z[2]
v , z[0]
v , z[−2]
v
, z[−1]
v
) are the bits from the 5 complete sets associated with node v.
Using the fact that C(z) = −(1/
√

D) P
(u,v)∈E zuzv, we can rewrite ⟨γ, β|ZLZR|γ, β⟩as

{zu}
z[0]
L z[0]
R exp
h
−
i
√

⟨γ, β|ZLZR|γ, β⟩=
X

(u′,v′)∈E
Γ · (zu′zv′)
i
n
Y

D
X

v=1
f(zv)
(4.5)

where we have replaced the sum over the 2p+1 complete sets {z[i] : −2 ≤i ≤2} with an equivalent
sum over the bit conﬁgurations of each node {zu : 1 ≤u ≤n}. Now to evaluate ⟨ZLZR⟩we need
to perform a sum over the bit conﬁgurations zv of every node v in the tree subgraph, where each
node is coupled to its neighbors on the graph via the term in the exponential of Eq. (4.5).
We can start by considering a single leaf node w who is only connected to its parent node
p(w) on the tree, as shown in Fig. 2. Then the sum over the 32 bit values of the conﬁguration
zw = (z[1]
w , z[2]
w , z[0]
w , z[−2]
w
, z[−1]
w
) yields
X

zw
f(zw) exp
h
−
i
√

DΓ · (zwzp(w))
i
(4.6)

which is a function of the parent node’s conﬁguration zp(w). Note that doing this on every leaf
node contributes the same function to its parent. Since there are exactly D leaf nodes per parent,
we get the following contribution

H(1)
D (zp(w)) :=
 X

DΓ · (zwzp(w))
iD
.
(4.7)

zw
f(zw) exp
h
−
i
√

This is true for every parent node of any of the leaves.
After performing the sums for all the leaf nodes, we can move to the sums for their parents.
Let us look at the sum on the node p(w) for example, which yields
X

zp(w)
f(zp(w))H(1)
D (zp(w)) exp
h
−
i
√

DΓ · (zp(w)zp(p(w)))
i
.
(4.8)

Again, because its parent node p(p(w)) has D identical children like p(w), this yields

H(2)
D (zp(p(w))) :=
 X

DΓ · (zp(w)zp(p(w)))
iD
.
(4.9)

zp(w)
f(zp(w))H(1)
D (zp(w)) exp
h
−
i
√

Note at p = 2 we have reached the root of the tree L = p(p(w)) after these two iterations.
To evaluate ⟨γ, β|ZLZR|γ, β⟩, it only remains to sum over the 5 bits in zL and the 5 bits in
zR:

zL,zR
z[0]
L z[0]
R f(zL)f(zR)H(2)
D (zL)H(2)
D (zR) exp
h
−
i
√

⟨γ, β|ZLZR|γ, β⟩=
X

DΓ · (zLzR)
i
.
(4.10)

For higher p, we can see that the evaluation of ⟨γ, β|ZLZR|γ, β⟩simply involves more iterations
of Eq. (4.9) corresponding to more levels in the tree subgraph. In summary, the iteration for general
p can be written as starting with H(0)
D (a) = 1 and then evaluating for m = 1, 2, . . . , p,

9

## Page 10

H(m)
D (a) =
 X

DΓ · (ab)
iD
,
(4.11)

b
f(b)H(m−1)
D
(b) exp
h
−
i
√

since there are p levels in the tree subgraph seen by the QAOA with p layers. At the end we get

a,b
a0b0f(a)f(b)H(p)
D (a)H(p)
D (b) exp
h
−
i
√

⟨γ, β|ZLZR|γ, β⟩=
X

DΓ · (ab)
i
.
(4.12)

This is almost what we have stated for the iteration in Section 3.1.
To ﬁnish the proof, we note from Eq. (4.3) as well as its general p version in Eq. (3.4) that

f(−a) = f(a).
(4.13)

We now claim that
H(m)
D (−a) = H(m)
D (a)
for 0 ≤m ≤p
(4.14)

which we will show by induction on m. Note this is trivially true for the base case m = 0 since
H(0)
D (a) = 1 is constant. Assuming that H(m−1)
D
(−a) = H(m−1)
D
(a), we can take b →−b in the
summand of Eq. (4.11) and combine it with its original form to see that

H(m)
D (a) =
 X

DΓ · (ab)
iD
.
(4.15)

b
f(b)H(m−1)
D
(b) cos
h
1
√

From this form it follows that H(m)
D (−a) = H(m)
D (a) since a only appears in the cosine which is an
even function, establishing Eq. (4.14).
Similarly, we can take b →−b in Eq. (4.12) and combine with its original form to get

a,b
a0b0f(a)f(b)H(p)
D (a)H(p)
D (b) sin
h
1
√

⟨γ, β|ZLZR|γ, β⟩= −i
X

DΓ · (ab)
i
.
(4.16)

Thus to get the νp as deﬁned in Eq. (2.6) that tells us the cut fraction, we have

νp(D, γ, β) = i
√

D
2

a,b
a0b0f(a)f(b)H(p)
D (a)H(p)
D (b) sin
h
1
√

X

This proves our iteration for any ﬁnite D in Section 3.1.

4.2
Proof of D →∞iteration

We wish to evaluate Eq. (3.8) in the D →∞limit:

lim
D→∞νp(D, γ, β) = lim
D→∞
i
√

D
2

DΓ · (ab)
i
.
(4.17)

a,b
a0b0f(a)f(b)H(p)
D (a)H(p)
D (b) sin
h
1
√

X

We ﬁrst prove by induction that for 0 ≤m ≤p,

DΓ · (ab)
i
.
(4.18)

H(m)(a) := lim
D→∞H(m)
D (a)
(4.19)

exists and is ﬁnite. For m = 0, our claim holds because H(0)
D (a) = 1. Assuming the claim is true
for m −1, we examine H(m)(a) by taking the limit on Eq. (4.15)

 X

DΓ · (ab)
D
.
(4.20)

b
f(b)H(m−1)
D
(b) cos

1
√

H(m)(a) = lim
D→∞

10

## Page 11

Then performing a Taylor expansion of cos(· · ·), we get

b
f(b)H(m−1)
D
(b)

1 −
1
2D

Γ · (ab)
2
+ O

1
D2
D
.
(4.21)

 X

H(m)(a) = lim
D→∞

Using the fact that for any m,
X

a
f(a)H(m)
D (a) = 1
(4.22)

which is proved as Lemma 5 in Appendix A.2, we get

h
1 −
1
2D
X

H(m)(a) = lim
D→∞

Finally, taking the limit,

H(m)(a) = exp
h
−1

X

2

D2
iD
.
(4.23)

b
f(b)H(m−1)
D
(b)
Γ · (ab)
2 + O
1

b
f(b)H(m−1)(b)
Γ · (ab)
2i
(4.24)

which yields an iteration on H(m).
Returning to Eq. (4.18), we apply the product rule of limits to H(p)
D (a), H(p)
D (b), and
√

D sin[Γ·
(ab)/
√

D] and get

lim
D→∞νp(D, γ, β) = i

X

a,b
a0b0f(a)f(b)H(p)(a)H(p)(b)Γ · (ab).
(4.25)

2

This iteration can be simpliﬁed by expanding the dot products in Eqs. (4.24) and (4.25) to get

p
X

H(m)(a) = exp
h
−1

j,k=−p
ΓjΓkajak
 X

2

p
X

lim
D→∞νp(D, γ, β) = i

j=−p
Γj
 X

2

b
f(b)H(m−1)(b)bjbk
i
,
(4.26)

a
f(a)H(p)(a)a0aj
 X

b
f(b)H(p)(b)b0bj

(4.27)

and noticing that the quantity P
a f(a)H(m)(a)ajak appears repeatedly.
For 0 ≤m ≤p and
−p ≤j, k ≤p, deﬁne
G(m)
j,k :=
X

For m = 0, this is
G(0)
j,k =
X

For 1 ≤m ≤p, we plug Eq. (4.26) into Eq. (4.28) to get

p
X

a
f(a)ajak exp
h
−1

G(m)
j,k =
X

2

Finally, Eq. (4.27) can be written as

p
X

lim
D→∞νp(D, γ, β) = i

2

which establishes the iteration stated in Section 3.2.

11

a
f(a)H(m)(a)ajak.
(4.28)

a
f(a)ajak.
(4.29)

j′,k′=−p
G(m−1)
j′,k′
Γj′Γk′aj′ak′
i
.
(4.30)

j=−p
Γj(G(p)
0,j)2
(4.31)

## Page 12

5
Numerical evaluation and optimization

Let
νp(γ, β) = lim
D→∞νp(D, γ, β).
(5.1)

Numerically implementing the iteration summarized in Section 3.2 and optimizing for γ, β we ﬁnd

¯νp = max
γ,β νp(γ, β)
(5.2)

up to p = 17. The values are given in Table 1 and plotted in Fig. 3 as a function of 1/p. The
optimal γ and β can be found in Table 4 in Appendix C, and some examples are plotted in Fig. 4.
Based on the smooth pattern of the optimal γ and β up to p of 17, we guess these parameters at
p = 18, 19, 20 using heuristics similar to that in Ref. [18]. Then evaluation of νp(γ, β) gives lower
bounds on ¯νp at higher p which are listed in Table 2, and their corresponding γ and β are listed in
Table 5.

0.8

0.7

0.6

¯νp

0.5

0.4

0.3

0
1
1
2
1
3
1
4
1
6
1
8
1
11
1
17

1/p

Figure 3:
Optimal values ¯νp as a function of 1/p. At p = 11, ¯νp exceeds 2/π, related to the
cut fraction of the best currently known assumption-free classical algorithms. Here we made the
somewhat arbitrary choice of plotting the data against 1/p to see the large p region in a compact
plot.

2 + 2/π
√

Note that, at p = 11 and beyond, the QAOA achieves a cut fraction better than 1

D in the
large D limit, making it the best currently known assumption-free algorithm for MaxCut on large
random regular graphs.
We implement the iterative procedure described in Section 3.2 in C++. Our code is available
at Ref. [19]. Bit strings are encoded as unsigned long int variables, which allow for fast bit-wise
manipulations. Matrices and vectors are implemented using the Eigen library [20]. We parallelize

12

## Page 13

0.6

0.5

0.4

βr

γr

0.3

0.2

0.1

0.0
0.2
0.4
0.6
0.8
1.0
(r - 1) / (p - 1)

0.0
0.2
0.4
0.6
0.8
1.0
(r - 1) / (p - 1)

Figure 4:
Optimal γr and βr as a function of (r −1)/(p −1) ∈[0, 1] for p = 5, 9, 13, 17. For each
p, the index r = 1, 2, . . . , p enumerates the entries of γ and β. Dashed lines in between data points
are solely intended to guide the eye.

the sum over a in Eq. (3.10) using OpenMP [21]. We optimize γ, β for each value of p using
the LBFGS++ library, which implements the Limited-memory BFGS algorithm for unconstrained
optimization problems [22].
Each evaluation of the gradient of νp(γ, β) is a subroutine of the
optimization which takes 2p + 1 function calls. We run on a n2d-highcpu-224 machine in Google
Cloud, which has 224 vCPUs, using one thread per vCPU. A function call at p = 16 takes about
133 seconds, and a function call at p = 17 takes about 595 seconds. The run time of each function
call is roughly multiplied by 4 every time p is increased by 1. At p = 20, a single function call takes
slightly under 14 hours to evaluate. Memory usage is dominated by the need to store matrix G(m),
which is negligible and quadratic in p. Further optimizations might be possible.

Table 1: Optimal values of ¯νp up to p = 17.

Table 2:
Lower bounds of ¯νp for p = 18, 19, 20.

13

## Page 14

6
Agreement with the Sherrington-Kirkpatrick model

We note that Table 1 in this paper seems to be an extension of Table 1 in Ref. [13]. There, the
authors study the performance of the QAOA on the Sherrington-Kirkpatrick (SK) model [23], which
describes a spin-glass system with all-to-all random couplings. The cost function is

CSK
J (z) =
1
√n

X

1≤i<j≤n
Jijzizj
(6.1)

where the Jij are independently drawn from a distribution with mean 0 and variance 1.
The
authors arrive at an iterative formula for the ensemble-averaged performance of the QAOA on the
SK model
Vp(γ, β) := lim
n→∞EJ
h
⟨γ, β|CSK
J /n|γ, β⟩
J
J
i
,
(6.2)

where |γ, β⟩J is the QAOA state prepared with CSK
J . Since concentration is shown to hold, we
know that typical instances of the SK model all behave as the ensemble average.
Observe that ¯νp, the optimized values of νp(γ, β), listed in Table 1 of this paper agree with the
values of ¯Vp = maxγ,β Vp(γ, β) in Table 1 of Ref. [13]. It turns out that this is true in a general
sense:

Theorem 1. For all p and all parameters (γ, β), we have

Vp(γ, β) = νp(γ, β).
(6.3)

This theorem establishes the fact that for each p and ﬁxed parameters, the performance of the
QAOA on large-girth D-regular graphs in the D →∞limit is equal to its performance on the SK
model in the n →∞limit. We remark that in the iteration in this paper there is only one tree
subgraph, with of order Dp vertices, for every large-girth D-regular graph. On the other hand, in
the SK case, there is an ensemble of instances given by diﬀerent weights on the complete graph. It
is interesting to us that the ensemble average in Eq. (6.2) can be replaced by a single subgraph.
Theorem 1 also implies that the iteration in Section 3.2 works for evaluating the performance
of the QAOA applied to both large-girth regular graphs and the SK model.
In the rest of this section, we will prove this theorem by showing that the inﬁnite-D iteration
in Section 3.2 of this paper is equivalent to the iteration for the SK model in Section 4 of Ref. [13].
Showing this equivalence is a bit cumbersome since the two iterations are written with diﬀerent
conventions. We have attempted to keep the current section self-contained so the reader can skip
this proof and still read the rest of the paper.

Proof of Theorem 1.
— To help bridge the two approaches, let

A = {(a1, . . . ap, a−p, . . . , a−1) : ai = ±1}
(6.4)

be the set of 2p-bit strings that are used in the derivations of Ref. [13]. And let

B = {(a1, . . . ap, a0, a−p, . . . , a−1) : ai = ±1}
(6.5)

be the set of (2p + 1)-bit strings that are used in the derivations of the current paper.
We start with the version of the inﬁnite-D iteration of Eq. (4.24) which we restate here:

H(m)(a) = exp
h
−1

b∈B
f(b)H(m−1)(b)
Γ · (ab)
2i
for 1 ≤m ≤p,
(6.6)

X

2

14

## Page 15

where H(0)(a) = 1. Note importantly that H(m)(a) does not depend on a0 for 0 ≤m ≤p since
Γ0 = 0. Hence, in what follows, we will slightly abuse notation to write the function H(m)(a) to
take either an argument a ∈A or a ∈B.
We will now match this iteration to the one in Ref. [13] for evaluating Vp(γ, β) that uses symbols
such as Qa, Φa, ∆a,b, and Wa, which we will deﬁne as we progress in this proof.
For any (2p + 1)-bit string a ∈B, let us deﬁne the 2p-bit string ˆa ∈A via ˆa±r = a±ra±(r+1)
for 1 ≤r ≤p −1, and ˆa±p = a±pa0. More explicitly,

ˆa1 = a1a2,
. . . ,
ˆap−1 = ap−1ap,
ˆap = apa0,

ˆa−1 = a−1a−2,
. . . ,
ˆa−(p−1) = a−(p−1)a−p,
ˆa−p = a−pa0.
(6.7)

Then using the fact that ⟨a1|eiβX|a2⟩= ⟨a1a2|eiβX|1⟩, we can rewrite f(a) deﬁned in Eq. (3.4) for
any a ∈B as

f(a) = 1

2 ⟨ˆa1|eiβ1X|1⟩· · · ⟨ˆap−1|eiβp−1X|1⟩⟨ˆap|eiβpB|1⟩

× ⟨1|e−iβpX|ˆa−p⟩⟨1|e−iβp−1X|ˆa−(p−1)⟩· · · ⟨1|e−iβ1X|ˆa−1⟩

= 1

2Qˆa
(6.8)

where Qa is deﬁned in Section 4 of Ref. [13]:

p
Y

j=1
(cos βj)1+(aj+a−j)/2(sin βj)1−(aj+a−j)/2(i)(a−j−aj)/2
for any a ∈A.
(6.9)

Qa :=

Now, Ref. [13] makes use of the following ∗operation deﬁned on the set A of 2p-bit strings as

a∗
r = arar+1 · · · ap
and
a∗
−r = a−ra−r−1 · · · a−p
for 1 ≤r ≤p .
(6.10)

Please take care to note that in this proof, ∗is used only for the above operation and not complex
conjugation. Furthermore, Ref. [13] deﬁnes Φa as

p
X

r=1
γr(a∗
r −a∗
−r)
for any a ∈A.
(6.11)

Φa :=

Note ˆa∗
±r = ˆa±r · · · ˆa±p = a±ra0. Then for any a ∈B, Φˆa can be written as

p
X

p
X

r=1
γr(ˆa∗
r −ˆa∗
−r) =

Φˆa =

r=1
γr(ar −a−r)a0 = (Γ · a)a0.
(6.12)

Since a2
0 = 1, we get (Γ · a)2 = Φ2
ˆa. Also note c
ab = ˆaˆb, so we can rewrite Eq. (6.6) as

H(m)(a) = exp
h
−1

X

2

b∈B

1
2QˆbH(m−1)(b)Φ2
ˆaˆb

i
.
(6.13)

Note that
H(m)(ˆb
∗) = H(m)(bb0)
for any b ∈B,
(6.14)

where we slightly abuse notation to allow H(m) to take two types of argument: ˆb
∗∈A and b ∈B.
This equality follows from the fact that H(m)(a) for a ∈B does not depend on a0, the 0-th
component of a. Since H(m)(−b) = H(m)(b) which we have shown in Eq. (4.14), we have

H(m)(ˆb
∗) = H(m)(b)
for any b ∈B.
(6.15)

15

## Page 16

Hence, in Eq. (6.13) we can sum over ˆb ∈A instead of b ∈B, killing a 1/2 factor from the
redundancy of the sum over b0. Also we can replace H(m)(a) = H(m)(ˆa∗) and write Eq. (6.13) as

H(m)(ˆa∗) = exp
h
−1

ˆb∈A
QˆbH(m−1)(ˆb
∗)Φ2
ˆaˆb

X

2

We can then drop the hats and rewrite this as

H(m)(a∗) = exp
h
−1

i
for any ˆa ∈A.
(6.16)

b∈A
QbH(m−1)(b∗)Φ2
ab
i
for any a ∈A.
(6.17)

X

2

Now let us deﬁne for 0 ≤m ≤p and any a ∈A

R(m)
a
:= QaH(m)(a∗).
(6.18)

Then we have R(0)
a
= Qa, and plugging Eq. (6.17) into the above yields

R(m)
a
= Qa exp

−1

X

2

b∈A
R(m−1)
b
Φ2
ab

.
(6.19)

So far, we have transformed the iteration (6.6) on H(m)(a) for a ∈B to the above iteration
on R(m)
a
for a ∈A. This looks very similar as the iterative formula that yields Wa in Section 4 of
Ref. [13], which is then used to give Vp(γ, β). To show they are the same, i.e., R(p)
a
= Wa, we need
to describe a bit more of the formalism in Ref. [13]. There, the authors deﬁne a subset Ap+1 ⊂A
where
Ap+1 = {a : aj = a−j}.
(6.20)

Ref. [13] has also deﬁned a one-to-one “bar” operation that takes any a ̸∈Ap+1 to ¯a ̸∈Ap+1 such
that Q¯a = −Qa. This operation is its own inverse. Furthermore, we have the following fact:

H(m)(a∗) = 1
if
a ∈Ap+1
and
H(m)(¯a∗) = H(m)(a∗)
if
a ̸∈Ap+1
(6.21)

which we prove as Lemma 7 in Appendix B. Hence R(m)
a
= Qa if a ∈Ap+1 and R(m)
¯a
= −R(m)
a
if
a ̸∈Ap+1. Lastly, Ref. [13] deﬁnes for any a ∈A and b ∈A \ Ap+1

Xa := Qa exp

−1

b∈Ap+1
QbΦ2
ab

and
∆b,a := 1

X

2

Putting everything together, we can write (6.19) as

R(m)
a
= Qa exp
h
−1

b∈Ap+1
QbΦ2
ab −1

X

2

4

= Qa exp

−1

b∈Ap+1
QbΦ2
ab + 1

X

2

2

= Xa exp
1

2(Φ2
a¯b −Φ2
ab).
(6.22)

b̸∈Ap+1
R(m−1)
b
(Φ2
ab −Φ2
a¯b)
i

X

b̸∈Ap+1
R(m−1)
b
∆b,a


X

b̸∈Ap+1
R(m−1)
b
∆b,a

.
(6.23)

X

2

16

## Page 17

We now want to show that R(p)
a
is a ﬁxed point of the iteration in Eq. (6.23), by showing that
H(p)(a) is a ﬁxed point of the iteration in (6.6). Combining Eqs. (4.26) and (4.28), we can write

p
X

H(p)(a) = exp
h
−1

2

j,k=−p
G(p−1)
j,k
ΓjΓkajak
i
(6.24)

As discussed in Section 3.2 (and proved in Appendix A.4), after p −1 steps of the iteration, all
matrix elements G(p−1)
j,k
reach their ﬁnal value except when either j = 0 or k = 0. In other words,

G(p−1)
j,k
= G(p)
j,k except when j = 0 or k = 0. Noting that Γ0 = 0, we have

p
X

H(p)(a) = exp
h
−1

j,k=−p
G(p)
j,kΓjΓkajak
i
= exp
h
−1

2

b
f(b)H(p)(b)
Γ · (ab)
2i
.
(6.25)

X

2

where we plugged back in the deﬁnition (4.28) of G(p)
j,k. This means H(p)(a) is a ﬁxed point of the

iteration in Eq. (4.24), which also implies R(p)
a
is also a ﬁxed point of the iteration (6.23):

R(p)
a
= Xa exp
1

X

2

b̸∈Ap+1
R(p)
b ∆b,a

.
(6.26)

We can simplify this further. Note in general for b ̸∈Ap+1, we have R(p)
¯b ∆¯b,a = R(p)
b ∆b,a. Now,
let us bipartition A \ Ap+1 = D ∪Dc, such that if b ∈D then ¯b ∈Dc. Then we can rewrite the
above as
R(p)
a
= Xa exp
 X

b∈D
R(p)
b ∆b,a

.
(6.27)

Moreover, as stated in Section 4 of Ref. [13], for every element of b ∈D, there is a method to
assign a unique index j(b) ∈{1, 2, . . . , |D|} such that if j(b) ≤j(b′) then ∆b,b′ = 0. Thus, we have

R(p)
|D| = X|D|. The remaining R(p)
j
for j = |D| −1, . . . , 2, 1 are then determined via the following
relation

R(p)
j
= Xj exp

|D|
X


.
(6.28)

k=j+1
R(p)
k ∆k,j

which gives an alternative method to evaluate (6.19) to get R(p)
a
for all a ∈D. For the rest, we
have R(p)
¯a
= −R(p)
a
for ¯a ∈Dc, and R(p)
a
= Qa for a ∈Ap+1. This is precisely the iteration that
yields Wa described in Section 4 of Ref. [13]. Hence

Wa = R(p)
a
= QaH(p)(a∗)
for any a ∈A.
(6.29)

Finally, it remains to show νp(γ, β) = Vp(γ, β). Note we can rewrite the version of νp(γ, β) =
limD→∞νp(D, γ, β) in Eq. (4.25) as

νp(γ, β) = i

X

a,b∈B
a0b0f(a)f(b)H(p)(a)H(p)(b)Γ · (ab)

2

= i

1
2Qˆa
1
2QˆbH(p)(ˆa∗)H(p)(ˆb
∗)Φˆaˆb
(6.30)

X

2

a,b∈B

17

## Page 18

where we used Eqs. (6.8), (6.12) and (6.15). Since the summand is independent of a0 and b0, we
can sum over ˆa, ˆb ∈A instead of a, b ∈B, killing both 1/2 factors to get

νp(γ, β) = i

ˆa,ˆb∈A
QˆaQˆbH(p)(ˆa∗)H(p)(ˆb
∗)Φˆaˆb = i

X

2

= i

X

ˆa,ˆb∈A
ΦˆaˆbWˆaWˆb

2

X

u,v∈A
ΦuvWuWv = Vp(γ, β)
(6.31)

2

where in the last line we replaced ˆa, ˆb with dummy variables u, v since they are summed over. The
last equality follows from the formula of Vp(γ, β) detailed in Section 4 of Ref. [13]. This proves
Theorem 1.
So we have shown that the performance of the QAOA on any large-girth D-regular graph in the
D →∞limit is equivalent to its ensemble-averaged performance on the SK model in the inﬁnite
size limit.

7
Conjecture that our iteration achieves the Parisi value

The cut fraction output by the QAOA on MaxCut for large-girth (D + 1)-regular graphs is

⟨γ, β|CMC|γ, β⟩

|E|
= 1

2 + νp(D, γ, β)
√

D
.
(7.1)

We have given an iteration for evaluating νp(D, γ, β) for any depth p and parameters γ, β. Fur-
thermore, in Section 3.2 we give a compact iteration for νp(γ, β) = limD→∞νp(D, γ, β). Using this
iteration we can optimize over parameters to get ¯νp = maxγ,β νp(γ, β). Note ¯νp cannot be bigger
than the Parisi value, Π∗= limn→∞EJ[maxz CSK
J (z)/n]. From our numerics out to p = 17 we see
that ¯νp is headed in that direction.
Now we make the bold conjecture:

Conjecture. Let Π∗= 0.763166... be the Parisi value [15, 24]. Then

lim
p→∞¯νp = Π∗.
(7.2)

That is, the iteration in Section 3.2 is an alternative procedure to compute Π∗. To prove this
conjecture, perhaps one can show that the iteration in this paper is equivalent to one of the known
procedures for computing Π∗. (It may be interesting to note that Π∗= limk→∞Pk, where Pk
is the minimum of the Parisi variational principle over a k-step replica symmetry breaking ansatz
with 2k + 1 parameters [23, 25]. This is not unlike ¯νp.) Or one can ﬁnd a way to analytically
evaluate the p →∞limit.
There is an order of limits issue we now address. For any combinatorial optimization problem
of ﬁxed size, the QAOA can be shown to give the optimal solution in the p →∞limit [6]. This
may require p to grow exponentially in the system size. But we calculate the performance ¯νp of the
QAOA at ﬁxed p in the D →∞limit (which means inﬁnite system size). Then we take p →∞.
Our conjecture is about whether, under this new order of limits, the QAOA achieves the optimum
as p →∞.

18

## Page 19

8
Generalized iterations for Max-q-XORSAT

It turns out we can easily generalize our iterations for the QAOA’s performance on MaxCut in
Section 3 to the Max-q-XORSAT problem. MaxCut is a special case of Max-2-XORSAT. Given
a q-uniform hypergraph G = (V, E) where E ⊆V q, and given a signed weight Ji1i2...iq ∈{±1}
for each edge (i1, i2, . . . , iq) ∈E, Max-q-XORSAT is the problem of maximizing the following cost
function:
CXOR
J
(z) =
X

(i1,...,iq)∈E

1
2(1 + Ji1i2...iqzi1zi2 · · · ziq).
(8.1)

This cost function can be understood as counting the number of satisﬁed clauses, where a clause
is satisﬁed if zi1zi2 · · · ziq = Ji1i2...iq on the associated edge. Note the MaxCut cost function in
Eq. (2.2) is a special case of this problem where q = 2 and all Ji1i2 = −1.
We consider this problem on (D + 1)-regular hypergraphs, where each vertex has degree D + 1,
i.e., it is part of exactly D+1 hyperedges. (As in Section 2, working with (D+1)-regular hypergraphs
means the subgraphs that the QAOA sees are D-ary hypertrees.) The total number of hyperedges
is |E| = n(D + 1)/q, where n = |V | is the number of vertices. Due to a result by Sen [26], we
know that with high probability as n →∞, the maximum fraction of satisﬁed clauses for a random
(D + 1)-regular hypergraph for suﬃciently large D is

1
|E| max
z
CXOR
J
(z) = 1

2 + Πq

r q

2D + o(1/
√

D)
(8.2)

where Πq is the generalized Parisi value that can be determined explicitly.2 In particular, Π2 =
Π∗= 0.763166 . . ..
We want to evaluate how the QAOA performs on the Max-q-XORSAT problem for large-girth
(D + 1)-regular hypergraphs.
Here, girth is deﬁned as the minimum length of Berge cycles in
the hypergraph [27]. Similar to the MaxCut problem discussed in Section 2, we will see that the
QAOA has optimal parameters γ that are of order 1/
√

D for these graphs. For this reason, it
will be convenient to prepare the QAOA state |γ, β⟩J with the following shifted and scaled cost
function operator

CJ =
1
√

X

(i1,...,iq)∈E
Ji1i2...iqZi1Zi2 · · · Ziq.
(8.3)

D

For any such hypergraph, we are interested in the fraction of satisﬁed clauses output by the QAOA
at any parameters, for any choices of Ji1i2...iq drawn from {+1, −1}. We show the following:

Theorem 2. Consider CXOR
J
on any (D + 1)-regular q-uniform hypergraphs with girth > 2p + 1.
Let |γ, β⟩J be the QAOA state generated using CJ. Then for any choice of J,

1
|E|
⟨γ, β|CXOR
J
|γ, β⟩
J
J = 1

2 + ν[q]
p (D, γ, β)
r q

2D
(8.4)

where ν[q]
p (D, γ, β) is independent of J and can be evaluated (on a classical computer) with an
iteration using O(p4pq) time and O(4p) memory. In the inﬁnite D limit, limD→∞ν[q]
p (D, γ, β) can
be evaluated with an iteration using O(p24p) time and O(p2) memory.

In Section 8.1 that follows, we prove the J-independence of ν[q]
p
and discuss its implication for
a worst-case algorithmic threshold. We then state and prove the iterations for any ﬁnite D and the
inﬁnite D limit in Sections 8.2 through 8.5. We also present results of numerical evaluation of the
inﬁnite D iteration in Section 8.6.

2See Ref. [26] for how this value can be calculated. Take care to note that the conventions slightly diﬀer, and our
Πq = Pq/
√

2 where Pq is deﬁned in Section 2.1 of Ref. [26].

19

## Page 20

Figure 5: (a) The hypertree subgraph seen by the QAOA at p = 2 for the hyperedge (1, 2, . . . , q)
on a (D + 1)-regular q-uniform hypergraph with girth > 2p + 1, for q = 3 and D = 2. (b) A partial
view near the leaves of the hypertree subgraph for a general q and D. The starﬁsh are hyperedges.
Here w1, w2, . . . , wq−1 are leaf nodes in the same hyperedge, and we denote their common parent
as v1 = p(w1) = · · · = p(wq−1).

8.1
J-independence of ν[q]
p
and implied worst-case limitation

We start by arguing that the left hand side of Eq. (8.4) is independent of the choice of J’s, so there
is no J needed on the right hand side. When the girth of the hypergraph is larger than 2p + 1, the
subgraph seen by the QAOA on any hyperedge is always a D-ary q-uniform hypertree. See Fig. 5(a)
for an example. In this ﬁgure each triangle is associated with a coupling J that can be either +1 or
−1. Look at the triangle containing vertices 1, 2 and 3. We can absorb the sign of J123 into the bit
at vertex 1 as follows: if J123 = −1 do nothing, whereas if J123 = +1 ﬂip the sign of the bit at vertex
1 by redeﬁning Z1 →−Z1. Then J123Z1Z2Z3 →−Z1Z2Z3 under this transformation. Now look at
the triangle containing bits 1, v1 and v2. The sign of J1v1v2 may have been modiﬁed by the last step.
But we can now absorb the sign of J1v1v2 into the bit at v1 so that J1v1v2Z1Zv1Zv2 →−Z1Zv1Zv2.
This might aﬀect the sign of Jv1w1w2 in the triangle containing v1, w1 and w2. But we can redeﬁne
the bit at w1 appropriately so that Jv1w1w2Zv1Zw1Zw2 →−Zv1Zw1Zw2. Since there are no cycles
in the hypertree, we can move through the whole picture in this way resetting all the couplings J
to −1.
We have reset all the couplings J to −1 in the picture, and we now argue that this makes the
quantum expectation (8.4) independent of the J’s. At the quantum level we ﬂip the sign of the
operator Zu by conjugating with Xu, that is, XuZuXu = −Zu. Since the driver B commutes with
each Xu and the initial state is an eigenstate of each Xu, we can sprinkle Xu’s into the left hand
side of Eq. (8.4) and establish the J-independence of the expression coming from any particular
hyperedge.
Now the cost function (8.1) is a sum over the hyperedges of a given hypergraph,
but the expected value of each term in the QAOA state is independent of the J’s. So for every
(D + 1)-regular q-uniform hypergraph with girth > 2p + 1 we can write

1
|E|
⟨γ, β|CXOR
J
|γ, β⟩
J
J = 1

2 −1

2⟨γ, β|Z1Z2 . . . Zq|γ, β⟩
(8.5)

where (1, 2, 3, . . . , q) is any hyperedge, and the state |γ, β⟩without the J label has all the couplings

20

## Page 21

set to −1. In the sections that follow, we provide an iterative formula for

s

ν[q]
p (D, γ, β) = −

D
2q⟨γ, β|Z1Z2 . . . Zq|γ, β⟩
(8.6)

which gives the QAOA performance for Max-q-XORSAT at any parameters on any (D +1)-regular
q-uniform hypergraph with girth > 2p+1, regardless of the choices of J. This generalizes Eq. (2.6).
A corollary to this J-independence is that the QAOA at low depth fails to ﬁnd the optimal
assignment in the worst case. To see this, let us go back to the q = 2 case where we studied MaxCut
on a large-girth regular graph which has all of the couplings J = −1. At optimal parameters, the
fraction of satisﬁed clauses is 1/2 + ¯νp/
√

D in the large D limit, where ¯νp ≤Π∗. Consider the
corresponding instance where all the couplings on the same graph are set to J = +1, which makes
the instance fully satisﬁable.
In that case, the best possible fraction of satisﬁed clauses is 1.
However, the fraction output by the QAOA at optimal parameters is the same as in the J = −1
case, that is, at most 1/2 + Π∗/
√

D, which is only a bit more than 1/2 in the large D limit.
Here we have an example of the QAOA failing to reach the optimum in the worst case because
it does not “see” the whole graph. (Unlike previous results of the similar ﬂavor in Refs. [28, 29], we
do not need the graph to be bipartite to bound the worst-case approximation ratio.) Regardless
of the signs of the couplings, the low-depth QAOA sees a tree subgraph surrounding each edge.
On the tree subgraph the signs of the couplings are irrelevant so the QAOA does not distinguish
between instances where the cost function favors disagreement and instances where agreement is
favored. Without seeing cycles the QAOA cannot do better than what it can achieve in the most
frustrated case, and this yields an upper bound on the worst-case approximation ratio.

8.2
An iteration for any ﬁnite D

Here we give an iteration to evaluate ν[q]
p (D, γ, β) for any input parameters, q and D. We prove
that this iteration is correct in Section 8.4. We use the same convention as in Section 3, where we
deﬁned a (2p + 1)-component vector Γ and a function f(a) that takes any (2p + 1)-bit string a as
input. Similar to the iteration in Section 3.1, we start with H(0)
D (a) = 1, and for 1 ≤m ≤p, let

DΓ · (ab1b2 · · · bq−1)
i q−1
Y

H(m)
D (a) =

X

b1,...,bq−1
cos
h
1
√


f(bi)H(m−1)
D
(bi)
D
.
(8.7)

i=1

By iteratively evaluating Eq. (8.7) for m = 1, 2, . . . , p, we arrive at H(p)
D (a) which is used to compute

s

D
2q

a1,...,aq
sin
h
1
√

X

ν[q]
p (D, γ, β) = i

DΓ · (a1a2 · · · aq)
i
qY


ai
0f(ai)H(p)
D (ai)

.
(8.8)

i=1

We note that this iteration on H(m)
D
has p steps, each involving a sum with 2(2p+1)(q−1) terms
for each of the 22p+1 entries of H(m)
D (a). The ﬁnal step has a sum with O(4pq) terms. Overall,
this iteration has a time complexity of O(p 4pq) and a memory complexity of O(4p) for storing the
entries of H(m)
D .

8.3
An iteration for D →∞

In the inﬁnite D limit, we get a more compact iteration which we prove is correct in Section 8.5.
Similar to Section 3.2, we deﬁne matrices G(m) ∈C(2p+1)×(2p+1), for 0 ≤m ≤p as follows. For

21

## Page 22

j, k ∈{1, . . . , p, 0, −p, . . . , −1}, let G(0)
j,k = P
a f(a)ajak and

p
X

a
f(a)ajak exp
h
−1

G(m)
j,k =
X

2

j′,k′=−p

G(m−1)
j′,k′
q−1Γj′Γk′aj′ak′
i
for 1 ≤m ≤p.
(8.9)

Starting at m = 0 and going up by p steps we arrive at G(p) which is used to compute

p
X

ν[q]
p (γ, β) := lim
D→∞ν[q]
p (D, γ, β) =
i
√2q

j=−p
Γj(G(p)
0,j)q.
(8.10)

Note the only diﬀerence between Max-q-XORSAT and MaxCut, where q = 2, can be seen by
comparing Eqs. (3.10) and (3.11) in Section 3.2 to Eqs. (8.9) and (8.10) in the current iteration,
where we are raising the matrix element of G to some q-dependent power. This iteration takes
at most O(p24p) time and O(p2) memory to evaluate using the same method as described in
Appendix A.4, regardless of q. This is polynomially faster than the ﬁnite D case with exponentially
better memory usage.

8.4
Proof of the ﬁnite D iteration

We now prove that the iteration in Section 8.2 for ﬁnite degree D is correct. The proof is essentially
the same as in Section 4.1, and we will only focus on the diﬀerences in what follows. The goal is
to evaluate the expectation (8.6) on a single hyperedge (1, 2, . . . , q) by restricting to the hypertree
subgraph seen by the QAOA. As an example, we show such a subgraph in Fig. 5(a). After inserting
complete sets and reorganizing terms as we have done from Eq. (4.1) to Eq. (4.5), we arrive at

{zu}
z[0]
1 z[0]
2 · · · z[0]
q exp
h
−
i
√

⟨γ, β|Z1Z2 · · · Zq|γ, β⟩=
X

(i1,...,iq)∈E
Γ · (zi1zi2 · · · ziq)
i
n
Y

D
X

v=1
f(zv)

(8.11)

which is analogous to Eq. (4.5). To evaluate this, we again need to sum over all the bit conﬁgurations
zu = (z[1]
u , . . . , z[p]
u , z[0]
u , z[−p]
u
, . . . , z[−1]
u
) of every node u in the hypertree subgraph. We will do this
with the same method as in Section 4.1, where we ﬁrst sum over all the leaf nodes, then their
parents, and their parents’ parents, and so on.
We start by summing over a set of leaf nodes w1, w2, . . . , wq−1 which are in the same hyperedge
as their parent. Let their common parent be p(w1). See Fig. 5(b) for a visualization. Summing
over the bit conﬁgurations zw1, zw2, . . . , zwq−1 yields

DΓ · (zp(w1)zw1zw2 · · · zwq−1)
i q−1
Y

zw1,...,zwq−1
exp
h
−
i
√

X

j=1
f(zwj) .
(8.12)

Note this is a function of the parent node’s bit conﬁguration zp(w1). Since p(w1) is involved in
exactly D branching hyperedges, each of which contains q−1 distinct children, we get the following
contribution

H(1)
D (zp(w1)) :=

X

zw1,...,zwq−1
exp
h
−
i
√

22

DΓ · (zp(w1)zw1zw2 · · · zwq−1)
i q−1
Y

j=1
f(zwj)
D
(8.13)

## Page 23

after summing over all the leaf nodes. This applies to every parent node of any of the leaves. And
similar to what we have done to get Eq. (4.15) in Section 4.1, we can use the fact that f(−z) = f(z)
to take zw1 →−zw1 in the above summand and combine it with its original form to get

DΓ · (zp(w1)zw1zw2 · · · zwq−1)
i q−1
Y

H(1)
D (zp(w1)) =

X

zw1,...,zwq−1
cos
h
1
√

j=1
f(zwj)
D
.
(8.14)

Next, we repeat this argument for all the parent nodes like p(w1). Let v1 = p(w1), and let
v2, v3, . . . , vq−1 be the other nodes in the same hyperedge as v1 [see Fig. 5(b)]. We also denote p(v1)
as their shared parent node. Including the contribution H(1)
D (zvj) coming from the above sum over
the leaves, we sum over all zvj’s to get the following function on zp(v1)

DΓ · (zp(v1)zv1zv2 · · · zvq−1)
i q−1
Y

H(2)
D (zp(v1)) :=

X

zv1,...,zvq−1
exp
h
−
i
√


f(zvj)H(1)
D (zvj)
D

j=1

DΓ · (zp(v1)zv1zv2 · · · zvq−1)
i q−1
Y

=

X

zv1,...,zvq−1
cos
h
1
√


f(zvj)H(1)
D (zvj)
D
(8.15)

j=1

where the last equality follows from the fact that f(−z) = f(z) and H(1)
D (−z) = H(1)
D (z).
It is easy to see that continuing in this fashion we can iteratively sum over all but the root nodes
in p steps, corresponding to the p levels in the hypertree subgraph. At each step m, we obtain
H(m)
D (z) which is a function of the bit conﬁguration z of any node that is m levels away from the
leaves. For consistency of notation, we let H(0)
D (z) = 1. At the end of the iteration, we reach the
top-level root nodes inside the central hyperedge (1, 2, . . . , q), and we can evaluate Eq. (8.11) as

DΓ · (z1z2 · · · zq)
i
qY

z1,...,zq
z[0]
1 z[0]
2 · · · z[0]
q exp
h
−
i
√

⟨γ, β|Z1Z2 · · · Zq|γ, β⟩=
X

z1,...,zq
sin
h
1
√

= −i
X


f(zj)H(p)
D (zj)


j=1

DΓ · (z1z2 · · · zq)
i
qY


z[0]
j f(zj)H(p)
D (zj)

.
(8.16)

j=1

Then plugging this back into Eq. (8.6) gives the iterative formula for ν[q]
p (D, γ, β) in Eq. (8.8).

8.5
Proof of the D →∞iteration

To get the inﬁnite D iteration in Section 8.3, we follow the same argument as in Section 4.2. This
is done by ﬁrst deﬁning the following limiting functions for 0 ≤m ≤p

H(m)(a) := lim
D→∞H(m)
D (a).
(8.17)

These functions can be shown to satisfy the following recursion relation for 1 ≤m ≤p


X

b1,...,bq−1
cos
h
1
√

H(m)(a) = lim
D→∞

DΓ · (ab1b2 · · · bq−1)
i q−1
Y


f(bi)H(m−1)
D
(bi)
D

i=1

Γ · (ab1b2 · · · bq−1)
2
q−1
Y

= exp

−1

X

2

b1,...,bq−1

23


f(bi)H(m−1)(bi)

(8.18)

i=1

## Page 24

where the second line is obtained by performing Taylor expansion of the cosine, and using the
fact that P
b f(b)H(m−1)
D
(b) = 1 (which is analogous to Lemma 5 in Appendix A.2 for general q).
Expanding the dot product, we get

q−1
Y

p
X

H(m)(a) = exp

−1

j,k=−p
ΓjΓkajak

2

i=1

By deﬁning
G(m)
j,k :=
X

we can recast the iteration (8.19) as

p
X

a
f(a)ajak exp

−1

G(m)
j,k =
X

2

j′,k′=−p

for 1 ≤m ≤p. For m = 0, we have

G(0)
j,k =
X

bi
f(bi)H(m−1)(bi)bi
jbi
k

.
(8.19)

 X

a
f(a)H(m)(a)ajak,
(8.20)

G(m−1)
j′,k′
q−1Γj′Γk′aj′ak′

(8.21)

a
f(a)ajak,
(8.22)

since H(0)(a) = 1. Finally, we can write ν[q]
p
in Eq. (8.8) in the D →∞limit as

s

D
2q

a1,...,aq
sin
h
1
√

X

lim
D→∞ν[q]
p (D, γ, β) = lim
D→∞i

p
X

qY

=
i
√2q

 X

j=−p
Γj

i=1

p
X

=
i
√2q

DΓ · (a1a2 · · · aq)
i
qY


ai
0f(ai)H(p)
D (ai)


i=1

ai
ai
0ai
jf(ai)H(p)(ai)


j=−p
Γj
G(p)
0,j
q
(8.23)

which gives the inﬁnite D iterative formula in Eq. (8.10) as desired.

8.6
Numerical evaluation of the Max-q-XORSAT performance at inﬁnite D

We have taken our iteration for inﬁnite D and numerically optimized ν[q]
p (γ, β) to ﬁnd

¯ν[q]
p
= max
γ,β ν[q]
p (γ, β).
(8.24)

up to p = 14 for 3 ≤q ≤6. Combining with the data we have for q = 2 in Table 1, we plot the
results in Fig. 6. For ease of comparison across diﬀerent values of q we have normalized ¯ν[q]
p
by
its corresponding Parisi value Πq. See Appendix D for a plot of the optimal γ and β we found at
p = 14. Numerical values for ¯ν[q]
p
and optimal γ and β for all 1 ≤p ≤14 can be found in Ref. [19].
In some cases, there are thresholds on how well the QAOA at low depths can do. It is known
that for problems that exhibit the overlap gap property, the locality property of the QAOA prevents
it from getting close to the optimum at low depths where it does not see the whole graph [30, 31].
Speciﬁcally, using an overlap gap property in the Max-q-XORSAT problem on random Erd˝os-R´enyi
hypergraphs with constant average degree and even q ≥4, Ref. [31] showed that the QAOA (or

24

## Page 25

1.0

0.9

0.8

¯ν[q]
p
Πq

0.7

0.6

0.5

0.4

0.3

0
1
1
2
1
3
1
4
1
6
1
8
1
11
1
17

1/p

Figure 6:
Optimal values ¯ν[q]
p
normalized by their corresponding Parisi values Πq as a function of
1/p for q = 2, 3, 4, 5, 6. The Parisi values are taken from Ref. [17]. Similar to Fig. 3, we made the
somewhat arbitrary choice of plotting the data against 1/p to see the large p region in a compact
plot. Dashed lines in between data points are intended to guide the eye.

any local algorithm) has limited performance when the depth p is less than ϵ log(n), where n is
the graph size and ϵ is a constant that depends on the degree and q. Assuming the overlap gap
property also holds when the hypergraphs are regular, one can use similar arguments to show that
the QAOA’s performance as measured by ¯ν[q]
p /Πq does not converge to 1 as p →∞when q ≥4
and is even. This is because our large-girth assumption implies the graph has at least Dp vertices,
so p is always less than ϵ log n in this limit.

9
Discussion

In this paper, we have introduced new techniques for evaluating the performance of a quantum
algorithm at high qubit number and at high depth. In particular we do this by ﬁnding a compact
iteration for the QAOA’s performance on MaxCut on instances with locally tree-like neighbor-
hoods. On random large-girth D-regular graphs, the QAOA at p = 11 and higher has the highest
approximation ratio of any assumption-free algorithm. We have given performance guarantees for
the QAOA, but it is necessary to run a quantum computer to produce a string with the calculated
performance.
We have also shown that for any depth p and for any parameters, γ and β, the performance
of the QAOA on large-girth D-regular graphs, as D →∞, matches the typical performance of
the QAOA on the Sherrington-Kirkpatrick model at inﬁnite size. We ﬁnd it remarkable that the
ensemble averaging done in the SK model can be replaced by analyzing a single tree subgraph. For
both of these models the best conceivable performance is upperbounded by the Parisi constant, Π∗.

25

## Page 26

There are optimal parameters at each p, and we speculate that as p →∞these optimal parameters
give QAOA performance that matches the Parisi constant for both models.
Moreover, in Section 8, we have generalized our iteration for MaxCut on large-girth regular
graphs to evaluate the QAOA’s performance on Max-q-XORSAT problems for large-girth regular
hypergraphs. We have shown that, at ﬁxed parameters, the QAOA gives the same value of the
objective function regardless of the signs of the couplings on these hypergraphs.
This implies
a worst-case algorithmic threshold at low depth for fully satisﬁable instances. Building on our
work, Ref. [32] recently generalized the equivalence between MaxCut and the SK model to between
Max-q-XORSAT and the fully connected q-spin model.
There are a number of ideas to explore coming out of this work. Can we ﬁnd a more eﬃcient
iterative formula for the QAOA’s performance than the one in Section 3.2? If so, we can better
probe the large-p behavior of the QAOA. Can the iteration in Section 3.2 be recast in the p →∞
limit in terms of continuous functions corresponding to γ, β? This might be a way to verify, or
falsify, the conjecture in Section 7.
Can one ﬁnd other problems at high qubit number and high depth where the performance of
the QAOA can be established using techniques similar to the ones introduced in this paper?

Acknowledgements

The authors thank Sam Gutmann for being there and Matthew P. Harrigan for a careful read of
the manuscript. This material is based upon work supported by the National Science Foundation
Graduate Research Fellowship Program under Grant No. DGE-1746045. Any opinions, ﬁndings,
and conclusions or recommendations expressed in this material are those of the author(s) and do
not necessarily reﬂect the views of the National Science Foundation.

References

[1] L. Trevisan, G. B. Sorkin, M. Sudan, and D. P. Williamson, “Gadgets, approximation, and
linear programming,” SIAM Journal on Computing, vol. 29, no. 6, pp. 2074–2097, 2000.
https://doi.org/10.1137/S0097539797328847

[2] A. Montanari and S. Sen, “Semideﬁnite programs on sparse random graphs and their
application to community detection,” in Proceedings of the 48th Annual ACM Symposium on
Theory of Computing, ser. STOC ’16, 2016, pp. 814–827. arXiv:1504.05910

[3] R. Lyons, “Factors of iid on trees,” Combinatorics, Probability and Computing, vol. 26, no. 2,
pp. 285–300, 2017. arXiv:1401.4197

[4] B. Barak and K. Marwaha, “Classical Algorithms and Quantum Limitations for Maximum
Cut on High-Girth Graphs,” in Proceedings of the 13th Innovations in Theoretical Computer
Science Conference, ser. ITCS ’22, vol. 215, 2022, pp. 14:1–14:21. arXiv:2106.05900

[5] J. K. Thompson,
O. Parekh,
and K. Marwaha,
“An explicit vector algorithm for
high-girth MaxCut,” Symposium on Simplicity in Algorithms (SOSA), pp. 238–246, 2022.
arXiv:2108.12477

[6] E. Farhi,
J. Goldstone,
and S. Gutmann,
“A Quantum Approximate Optimization
Algorithm,” arXiv preprint, 2014. arXiv:1411.4028

[7] M. P. Harrigan, K. J. Sung, M. Neeley, K. J. Satzinger, F. Arute, K. Arya, J. Atalaya,
J. C. Bardin, R. Barends, S. Boixo et al., “Quantum approximate optimization of non-planar

26

## Page 27

graph problems on a planar superconducting processor,” Nature Physics, vol. 17, no. 3, pp.
332–336, 2021. arXiv:2004.04197

[8] Z. Wang, S. Hadﬁeld, Z. Jiang, and E. G. Rieﬀel, “Quantum approximate optimization
algorithm for MaxCut: A fermionic view,” Phys. Rev. A, vol. 97, no. 2, p. 022304, 2018.
arXiv:1706.02998

[9] J. Wurtz and P. Love, “MaxCut quantum approximate optimization algorithm performance
guarantees for p > 1,” Phys. Rev. A, vol. 103, p. 042612, 2021. arXiv:2010.11209

[10] K. Marwaha, “Local classical MAX-CUT algorithm outperforms p = 2 QAOA on high-girth
regular graphs,” Quantum, vol. 5, p. 437, 2021. arXiv:2101.05513

[11] A. E. Alaoui, A. Montanari, and M. Sellke, “Local algorithms for Maximum Cut and
Minimum Bisection on locally treelike regular graphs of large degree,” arXiv preprint, 2021.
arXiv:2111.06813

[12] D. Gamarnik, “The overlap gap property: A topological barrier to optimizing over random
structures,” Proceedings of the National Academy of Sciences, vol. 118, no. 41, 2021.
arXiv:2109.14409

[13] E. Farhi, J. Goldstone, S. Gutmann, and L. Zhou, “The Quantum Approximate Optimization
Algorithm and the Sherrington-Kirkpatrick Model at Inﬁnite Size,” Quantum, vol. 6, p. 759,
2022. arXiv:1910.08187v4

[14] S. Boulebnane and A. Montanaro, “Predicting parameters for the Quantum Approximate
Optimization Algorithm for MAX-CUT from the inﬁnite-size limit,” arXiv preprint, 2021.
arXiv:2110.10685

[15] G. Parisi, “Toward a mean ﬁeld theory for spin glasses,” Physics Letters A, vol. 73, no. 3, pp.
203–205, 1979. https://doi.org/10.1016/0375-9601(79)90708-4

[16] A. Dembo, A. Montanari, and S. Sen, “Extremal cuts of sparse random graphs,” The Annals
of Probability, vol. 45, no. 2, pp. 1190–1217, 2017. arXiv:1503.03923

[17] K. Marwaha and S. Hadﬁeld, “Bounds on approximating Max kXOR with quantum and
classical local algorithms,” arXiv preprint, 2021. arXiv:2109.10833

[18] L. Zhou, S.-T. Wang, S. Choi, H. Pichler, and M. D. Lukin, “Quantum approximate
optimization algorithm: Performance, mechanism, and implementation on near-term devices,”
Phys. Rev. X, vol. 10, p. 021067, 2020. arXiv:1812.01041

[19] J.
Basso,
E.
Farhi,
K.
Marwaha,
B.
Villalonga,
and
L.
Zhou,
“Performance
of
the
QAOA
on
MaxCut
over
Large-Girth
Regular
Graphs,”
Online,
2022.
https:
//github.com/benjaminvillalonga/large-girth-maxcut-qaoa

[20] G. Guennebaud, B. Jacob et al., “Eigen v3,” Online, 2010. https://eigen.tuxfamily.org

[21] L. Dagum and R. Menon,
“OpenMP: an industry standard API for shared-memory
programming,” Computational Science & Engineering, IEEE, vol. 5, no. 1, pp. 46–55, 1998.
https://doi.org/10.1109/99.660313

[22] Y. Qiu and D. Toewe, “LBFGS++,” Online, 2020. https://github.com/yixuan/LBFGSpp

27

## Page 28

[23] D. Panchenko, The Sherrington-Kirkpatrick model.
Springer Science & Business Media,
2013. https://doi.org/10.1007/978-1-4614-6289-7

[24] M. J. Schmidt, “Replica symmetry breaking at low temperatures,” Ph.D. dissertation,
Universit¨at W¨urzburg, 2008. https://d-nb.info/991972910/34

[25] A. Auﬃnger, W.-K. Chen, and Q. Zeng, “The SK Model Is Inﬁnite Step Replica Symmetry
Breaking at Zero Temperature,” Communications on Pure and Applied Mathematics, vol. 73,
no. 5, pp. 921–943, 2020. arXiv:1703.06872

[26] S. Sen, “Optimization on sparse random hypergraphs and spin glasses,” Random Structures
& Algorithms, vol. 53, no. 3, pp. 504–536, 2018. arXiv:1606.02365

[27] C.
Berge,
Hypergraphs,
Combinatorics
of
Finite
Sets.
North-Holland,
1989.
http:
//compalg.inf.elte.hu/∼tony/Oktatas/Algoritmusok-hatekonysaga/Berge-hypergraphs.pdf

[28] S. Bravyi,
A. Kliesch,
R. Koenig,
and E. Tang,
“Obstacles to variational quantum
optimization from symmetry protection,” Phys. Rev. Lett., vol. 125, p. 260505, Dec 2020.
arXiv:1910.08980

[29] E. Farhi, D. Gamarnik, and S. Gutmann, “The Quantum Approximate Optimization
Algorithm Needs to See the Whole Graph: Worst Case Examples,” arXiv preprint, 2020.
arXiv:2005.08747

[30] ——, “The Quantum Approximate Optimization Algorithm Needs to See the Whole Graph:
A Typical Case,” arXiv preprint, 2020. arXiv:2004.09002

[31] C.-N. Chou, P. J. Love, J. S. Sandhu, and J. Shi, “Limitations of Local Quantum Algorithms
on Random Max-k-XOR and Beyond,” arXiv preprint, 2021. arXiv:2108.06049

[32] J. Basso, D. Gamarnik, S. Mei, and L. Zhou, “Performance and limitations of the QAOA
at constant levels on large sparse hypergraphs and spin glass models,” arXiv preprint, 2022.
arXiv:2204.10306

28

## Page 29

A
Properties of the iterations

In this appendix, we prove some properties of the elements of the iterations. These properties are
of interest in their own right and also necessary to ﬁll in some gaps in the derivations.
We start in Appendix A.1 by proving some identities that will be used in the later proofs.
The assertion in Eq. (4.22) is proved in Appendix A.2. We prove in Appendix A.3 the symmetry
properties of the G(m) matrix elements asserted in Section 3.2. We show in Appendix A.4 how each
matrix element of G(m) only depends on a submatrix of G(m−1). This is key to understanding the
structure of the iteration and can be used to speed up the iteration by a factor of p.

A.1
Properties of f(a)

We start by establishing some notation and proving a few properties of f(a) that will be used
subsequently. Let
B = {(a1, a2, . . . , ap, a0, a−p, . . . , a−2, a−1) : aj = ±1}
(A.1)

be the set of (2p + 1)-bit strings. We deﬁne the following subset

B0 = {a ∈B : a−r = ar for all 1 ≤r ≤p}.
(A.2)

For any a ∈B, we deﬁne the T(a) to be the largest positive index T such that aT ̸= a−T if
a ̸∈B0, and 0 if a ∈B0. More formally,

(
max{r : a−r ̸= ar}
if a ̸∈B0
0
if a ∈B0.
(A.3)

T(a) =

To see how B is partitioned according to diﬀerent T(a), see Table 3. Note that a−r = ar
whenever r > T(a). These levels will help organize the a ∈B in the proofs below. Moreover, for
any a ̸∈B0, let a′ ̸∈B0 be the following bit string





a0
if r = 0
−a±r
if 1 ≤r ≤T(a)
a±r
if T(a) + 1 ≤r ≤p.

a′
±r =

(A.4)




As we will see, this deﬁnition is helpful as a and a′ are going to pair up leading to cancellations.

Table 3: a, T(a) and a′ for p = 3.

We also deﬁne, for any a ∈B, a corresponding ¨a ∈B whose entries are

¨aj = a−j
for −p ≤j ≤p.
(A.5)

That is, ¨a is the bit string a reversed.
Now we are ready to prove the identities on f(a). Recall its deﬁnition from Eq. (3.4):

f(a) = 1

2 ⟨a1|eiβ1X|a2⟩· · · ⟨ap−1|eiβp−1X|ap⟩⟨ap|eiβpX|a0⟩

× ⟨a0|e−iβpX|a−p⟩⟨a−p|e−iβp−1X|a−(p−1)⟩· · · ⟨a−2|e−iβ1X|a−1⟩,
(A.6)

29

## Page 30

which can be alternatively written as

f(a) = 1

2 ⟨a1a2|eiβ1X|1⟩· · · ⟨ap−1ap|eiβp−1X|1⟩⟨apa0|eiβpX|1⟩

× ⟨a0a−p|e−iβpX|1⟩⟨a−pa−(p−1)|e−iβp−1X|1⟩· · · ⟨a−2a−1|e−iβ1X|1⟩
(A.7)

where

⟨a|eiβX|1⟩=

(
cos(β)
if a = +1
i sin(β)
if a = −1 .
(A.8)

Lemma 1. For any a ∈B \ B0,
f(a′) = −f(a).
(A.9)

Proof. Note that the set B can be subdivided into sets of strings {a} with ﬁxed values of T(a).
We will start with the set of a’s where T(a) = p. Note from Eq. (A.7) that f(a) only depends on
the product of pairs of adjacent bits. Under the prime operation a →a′, these products will not
change except for apa0 and a0a−p. (As an example look at T = 3 in Table 3.) Flipping the signs of
these two products ﬂips the sign of the product of the two relevant matrix elements in Eq. (A.7).
Therefore, in this case, f(a′) = −f(a).
Now consider the set of a’s with T(a) = p−1. Now the product of any pair of adjacent bits will
not change under the prime operation except for ap−1ap and a−pa−(p−1). (As an example look at
T = 2 in Table 3.) Flipping the signs of these two products ﬂips the sign of the product of the two
relevant matrix elements in Eq. (A.7). Therefore in this case again we have that f(a′) = −f(a).
This argument can be repeated for T(a) = p −2, p −3, ..., 1 so the Lemma is established.

Lemma 2. For any a ∈B,
f(¨a) = f(a)∗.
(A.10)

Proof. This follows from Eq. (A.6) and noting that

⟨a1|eiβ1X|a2⟩⟨a−2|e−iβ1X|a−1⟩= ⟨¨a−1|eiβ1X|¨a−2⟩⟨¨a2|e−iβ1X|¨a1⟩

= ⟨¨a1|eiβ1X|¨a2⟩
∗⟨¨a−2|e−iβ1X|¨a−1⟩
∗.

The same follows for the other pairs, yielding Eq. (A.10).

Lemma 3.
X

a∈B
f(a) =
X

Proof. Using deﬁnition of f(a) in Eq. (A.6), we see that

a∈B0
f(a) = 1.
(A.11)

1
2 ⟨a1|eiβ1X · · · eiβpXe−iβpX · · · e−iβ1X|a−1⟩=
X

a∈B
f(a) =
X

X

a1,a−1

Also
X

a∈B0
f(a) + 1

a∈B
f(a) =
X

X

2

a̸∈B

1
2 ⟨a1|a−1⟩= 1.

a1,a−1


f(a) + f(a′)

=
X

a∈B0
f(a)

where we have decomposed the sum over a ∈B into a sum over a ∈B0 and a sum over a ̸∈B0,
and duplicated the latter by considering summing over a′ instead of a. Then applying Lemma 1
gives the ﬁrst equality in Eq. (A.11).

30

## Page 31

A.2
Properties of H(m)
D (a)

We now prove some properties involving H(m)
D (a), which are used in the proofs in Section 4.2 and
in the later sections of the appendix.

Lemma 4. For 0 ≤m ≤p,

H(m)
D (a) = 1
if
a ∈B0
and
H(m)
D (a′) = H(m)
D (a)
if
a ̸∈B0.
(A.12)

Proof. We proceed by induction on m. The base case m = 0 follows from the fact that, for all a,
H(0)
D (a) = 1. Now as an inductive hypothesis assume that the lemma is true for m−1. Then, using
Lemma 1, we can break the sum on b in the deﬁnition (3.7) of H(m)
D (a) into pieces as

H(m)
D (a) =

X

b: T(b)≤T(a)
f(b)H(m−1)
D
(b) cos
h
1
√

b: T(b)>T(a)
f(b)H(m−1)
D
(b)

cos
h
1
√

+ 1

X

2

DΓ · (ab)
i

DΓ · (ab′)
iD
.
(A.13)

DΓ · (ab)
i
−cos
h
1
√

We now show that the second sum evaluates to zero. To see this, note that

p
X

Γ · (ab) =

r=1
γr(arbr −a−rb−r) =

max{T(a),T(b)}
X

r=1
γr(arbr −a−rb−r)
(A.14)

since arbr = a−rb−r when r > max{T(a), T(b)}. Note if T(b) ≥T(a), then b±r = −b′
±r when
r ≤max{T(a), T(b)} = T(b) = T(b′). So whenever T(b) ≥T(a), which includes the case when
T(b) > T(a), we have from Eq. (A.14) that

max{T(a),T(b′)}
X

r=1
γr(arb′
r −a−rb′
−r) = −Γ · (ab′).
(A.15)

Γ · (ab) = −

And since cosine is an even function, Eq. (A.13) becomes

H(m)
D (a) =

X

DΓ · (ab)
iD
.
(A.16)

b: T(b)≤T(a)
f(b)H(m−1)
D
(b) cos
h
1
√

With this simpliﬁed form of H(m)
D (a), we now can prove the Lemma.
If a ∈B0, we have
T(a) = 0. Using the inductive hypothesis that H(m−1)
D
(b) = 1 when b ∈B0 and the fact that
Γ · (ab) = 0 when a, b ∈B0, we have

H(m)
D (a) =
 X

b∈B0
f(b)H(m−1)
D
(b) cos
h
1
√

DΓ · (ab)
iD
=
 X

b∈B0
f(b)
D
= 1,
(A.17)

where Lemma 3 is used in the last equality. Now consider the case of a ̸∈B0. When T(b) ≤T(a) as
in the sum in Eq. (A.16), we may switch the roles of a, b in Eq. (A.15) to see that Γ·(ab) = −Γ·(a′b).
Since T(a) = T(a′), we can rewrite Eq. (A.16) as

H(m)
D (a) =

X

b: T(b)≤T(a′)
f(b)H(m−1)
D
(b) cos
h
1
√

This completes the induction.

31

DΓ · (a′b)
iD
= H(m)
D (a′).
(A.18)

## Page 32

Next, we apply the above result to prove the assertion of Eq. (4.22), which is used in Section 4.2
to establish the correctness of the inﬁnite-D iteration. This assertion is the following lemma that
we now prove.

Lemma 5. For 0 ≤m ≤p, we have
X

a∈B
f(a)H(m)
D (a) = 1.
(A.19)

Proof. Decomposing the sum over a ∈B and applying Lemmas 1 and 4, we get

a∈B0
f(a)H(m)
D (a) + 1

a∈B
f(a)H(m)
D (a) =
X

X

X

2

a̸∈B0

a∈B0
f(a) + 1

=
X

X

2

a̸∈B0

=
X

a∈B0
f(a) = 1

where we used Lemma 3 on the last line.

h
f(a)H(m)
D (a) + f(a′)H(m)
D (a′)
i

h
f(a)H(m)
D (a) −f(a)H(m)
D (a)
i

Finally, we prove a lemma to be used in proving the properties of G(m)
r,s
that involve complex
conjugation in what follows in Appendix A.3.

Lemma 6. For any a ∈B and 0 ≤m ≤p,

H(m)
D (¨a) = H(m)
D (a)∗.
(A.20)

Proof. We proceed by induction on m. The base case m = 0 follows from the fact that H(0)
D (a) = 1.
Now assume that the lemma is true for m −1. By Eq. (3.7),

DΓ · (¨ab)
iD
=
 X

H(m)
D (¨a) =
 X

b
f(b)H(m−1)
D
(b) cos
h
1
√

DΓ · (¨a¨b)
iD

b
f(¨b)H(m−1)
D
(¨b) cos
h
1
√

since P
a∈B(· · · ) = P
¨a∈B(· · · ). Then, by the inductive hypothesis, Lemma 2 and the fact that
Γ · (¨a¨b) = −Γ · (ab) we have

H(m)
D (¨a) =
 X

b
f(b)∗H(m−1)
D
(b)∗cos
h
1
√

32

DΓ · (ab)
iD
= H(m)
D (a)∗.

## Page 33

A.3
Symmetries of the G(m) matrix

In this section of the appendix, we prove the following symmetry properties of the matrix G(m)

that are stated in Section 3.2: For 1 ≤r < s ≤p, and −p ≤j, k ≤p, we have

(1) G(m)
j,k = G(m)
k,j ,

(2) G(m)
j,j = G(m)
j,−j = 1,

(3) G(m)
0,r = G(m)∗
0,−r ,

(4) G(m)
r,s = G(m)
r,−s = G(m)∗
−r,−s = G(m)∗
−r,s .

Let us use the deﬁnition of G(m)
j,k in terms of H(m) in Eq. (4.28) which we reproduce here:

G(m)
j,k :=
X

a∈B
f(a)H(m)(a)ajak.
(A.21)

It is clear from this deﬁnition that G(m) is a symmetric matrix, so Property (1) holds. For the
remaining properties, let us rewrite Eq. (A.21) using Lemmas 1 and 4 as

a∈B0
f(a)ajak + 1

G(m)
j,k =
X

X

2

a̸∈B0
f(a)H(m)(a)(ajak −a′
ja′
k).
(A.22)

Note that Lemma 4 is applied to H(m)(a) which is H(m)
D (a) in the D →∞limit.
To prove Property (2), observe that

a∈B0
f(a) + 1

G(m)
j,j =
X

a̸∈B0
f(a)H(m)(a)(1 −1) =
X

X

2

where the last equality is due to Lemma 3. Also

a∈B0
f(a)aja−j + 1

G(m)
j,−j =
X

X

2

a∈B0
f(a) = 1,
(A.23)

a̸∈B0
f(a)H(m)(a)(aja−j −a′
ja′
−j).

Note that aj = a−j for a ∈B0, and aja−j = a′
ja′
−j for any a ∈B. Therefore

G(m)
j,−j =
X

a∈B0
f(a) = 1.
(A.24)

Next, we prove Property (3). From Eq. (A.21) we have

G(m)
0,r =
X

a∈B
f(a)H(m)(a)a0ar =
X

a∈B
f(¨a)H(m)(¨a)¨a0¨ar

where we used the fact that P
a∈B(· · · ) = P
¨a∈B(· · · ). Applying Lemma 6, which is true for each
D so it is true in the D →∞limit, along with Lemma 2 we get

a∈B
f(a)∗H(m)(a)∗a0a−r = G(m)∗
0,−r .
(A.25)

G(m)
0,r =
X

Lastly, we need to prove Property (4). Let 1 ≤r < s ≤p. Then from Eq. (A.22) we have

a∈B0
f(a)aras + 1

G(m)
r,s =
X

X

2

a∈B0
f(a)aras + 1

=
X

X

2

33

a̸∈B0
f(a)H(m)(a)(aras −a′
ra′
s)

a̸∈B0,r≤T(a)<s
f(a)H(m)(a)(aras −a′
ra′
s)

## Page 34

where we used the fact that the second summand is nonzero only if aras ̸= a′
ra′
s, which holds only
if r ≤T(a) < s. Under this condition we have aras −a′
ra′
s = 2aras, so

G(m)
r,s =
X

a∈B0
f(a)aras +
X

Similarly,

G(m)
r,−s =
X

a∈B0
f(a)ara−s +
X

=
X

a∈B0
f(a)aras +
X

a̸∈B0,r≤T(a)<s
f(a)H(m)(a)aras.
(A.26)

a̸∈B0,r≤T(a)<s
f(a)H(m)(a)ara−s

a̸∈B0,r≤T(a)<s
f(a)H(m)(a)aras
(A.27)

where we used the fact that a−s = as if a ∈B0 or if T(a) < s.
Comparing Eq. (A.26) and
Eq. (A.27), we conclude that
G(m)
r,s = G(m)
r,−s .
(A.28)

It remains to consider

G(m)
−r,±s =
X

a∈B
f(a)H(a)a−ra±s =
X

a∈B
f(¨a)H(¨a)¨a−r¨a±s

where we used the fact that P
a∈B(· · · ) = P
¨a∈B(· · · ). Now, using Lemma 2 and Lemma 6 in the
D →∞limit,
G(m)
−r,±s =
X

a∈B
f(a)∗H(a)∗ara∓s = G(m)∗
r,∓s
(A.29)

establishing Property (4).

34

## Page 35

A.4
Placement of the matrix elements of G(m)

In this section of the appendix, we show how the matrix elements of G(m) only depend on a
submatrix of G(m−1). This implies that the iteration on G(m) can be understood as a placement
of the entries in the matrix G(m) that remain unchanged after a suﬃcient number of steps. We
also elaborate on why this enables us to reduce the complexity of implementing the iteration in
Section 3.2 to O(p24p) instead of the na¨ıve O(p34p) estimate.
Recall the deﬁnition (4.28) of G(m)
j,k which states

G(m)
j,k =
X

Observe that combining Eqs. (4.26) and (4.28) we have

p
X

H(m)(a) = exp
h
−1

2

a
f(a)H(m)(a)ajak.
(A.30)

j′,k′=−p
G(m−1)
j′,k′
Γj′Γk′aj′ak′
i
.
(A.31)

Note the summand in the exponential is zero whenever either j′ = 0 or k′ = 0 since Γ0 = 0. Hence,
we can focus on j′, k′ ̸= 0, and enumerate all pairs of (j′, k′) by writing the sum as

p
X

H(m)(a) = exp

−1

h
G(m−1)
s′,s′
γ2
s′ −G(m−1)
s′,−s′ γ2
s′as′a−s′ −G(m−1)
−s′,s′ γ2
s′a−s′as′ + G(m−1)
−s′,−s′γ2
s′
i

2

s′=1

h
G(m−1)
r′,s′
γr′γs′ar′as′ −G(m−1)
r′,−s′ γr′γs′ar′a−s′

−
X

1≤r′<s′≤p

−G(m−1)
−r′,s′ γr′γs′a−r′as′ + G(m−1)
−r′,−s′γr′γs′a−r′a−s′
i
(A.32)

where the factor of 1/2 in front of the second sum is killed by considering the contribution from
the symmetric pair G(m−1)
s′,r′
= G(m−1)
r′,s′
, etc. Then applying the Properties (2) and (4) listed in
Appendix A.3 to G(m−1) yields the following simpliﬁed form

p
X

H(m)(a) = exp

−

s′=1
γ2
s′(1 −as′a−s′) −
X

1≤r′<s′≤p
γr′γs′
h
G(m−1)
r′,s′
ar′ −G(m−1)∗
r′,s′
a−r′
i
(as′ −a−s′)

.

(A.33)
Going back to Eqs. (A.30) and (A.31) we see that G(m) only depends on the matrix elements
of G(m−1) through H(m)(a), which only involves G(m−1)
r′,s′
for 1 ≤r′ < s′ ≤p as seen from the above

equation. In particular this means that G(m)
0,r depends only on G(m−1)
r′,s′
for 1 ≤r′ < s′ ≤p .

We next show that for 1 ≤r < s ≤p, G(m)
r,s only depends on G(m−1)
r′,s′
where 1 ≤r′ < s′ < s. We
ﬁrst restate Eq. (A.26)

G(m)
r,s =
X

a∈B0
f(a)aras +
X

a̸∈B0,r≤T(a)<s
f(a)H(m)(a)aras .
(A.34)

Observe that the dependence of G(m)
r,s on the matrix elements of G(m−1) is only via H(m)(a) in the
second summand in Eq. (A.33). However, this summand can be nonzero only if as′ ̸= a−s′, which
holds only if T(a) ≥s′. Additionally, in Eq. (A.34), G(m)
r,s only depends on H(m)(a) when a satisﬁes
T(a) < s. Hence the only relevant terms in Eq. (A.33) involve r′ < s′ ≤T(a) < s. Therefore, G(m)
r,s
only depends on G(m−1)
r′,s′
where r′ < s′ < s.

35

## Page 36

Improved complexity of the iteration.
— We now show why the aforementioned properties
imply that we can improve the time complexity of the iteration on G(m) in Section 3.2 from the
na¨ıve O(p34p) estimate to O(p24p).
Given the dependency of the elements of G(m) on those of G(m−1), at the m-th step of the
iteration, when 1 ≤m ≤p −1, we only need to place the elements G(m)
r,m+1, with 1 ≤r < m + 1.

Looking at Eq. (A.34) we see that calculating G(m)
r,m+1 only involves summing over a where a ∈B0
or r ≤T(a) < m + 1. So we can use the following implementation of our iteration:

Iteration for computing νp(γ, β)

1: Allocate memory for matrices G(0), G(1) ∈C(2p+1)×(2p+1), where the diagonal and anti-diagonal
entries are initialized to 1 due to Property (2), and the rest initialized to 0.

2: for m = 1, 2, . . . , p do

3:
for a ∈B0 ∪{a : 1 ≤T(a) < m + 1} do

4:
Compute f(a)
▷Use Eq. (3.4)

5:
Compute H(m)(a)
▷Use Eq. (A.33) restricted to s′ ≤T(a) < m + 1

6:
for r = 1, 2, . . . , m do

7:
if m ≤p −1 then
▷This implements Eq. (A.34)

8:
Update G(m)
r,m+1 ←G(m)
r,m+1 + f(a)H(m)(a)aram+1 when a ∈B0 or T(a) ≥r

9:
else

10:
Update G(p)
0,r ←G(p)
0,r + f(a)H(p)(a)a0ar
11:
end if

12:
end for

13:
end for

14:
If m ≤p −1 then remove G(m−1) from memory and create a copy G(m+1) ←G(m).

15: end for

16: Returns νp(γ, β) = (i/2) Pp
r=1 γr[(G(p)
0,r)2 −(G(p)∗
0,r )2]
▷Use Eq. (3.11) and G’s symmetry properties

Let us evaluate the complexity of the above iteration. Note there are 2p+1 elements in B0, and
2p+ℓelements a ∈B satisfying T(a) = ℓ≥1. (It may be helpful to see this via Table 3.) So
in line 3 above we only iterate over O(2p+m) many a’s. Lines 4 and 5 make use of the fact that
the factors f(a) and H(m)(a) are the same regardless of which element G(m)
r,m+1 we are computing.
They require only O(p) and O(m2) time, respectively. Thus, the overall time complexity of the
iteration is
O
Pp
m=1 2p+m(p + m2 + m)

= O(p24p).

The memory complexity is at most O(p2) for storing the 2 matrices of dimension (2p+1)×(2p+1).

36

## Page 37

B
A lemma needed in Section 6

In this appendix, we prove Eq. (6.21) that was asserted in Section 6 and used to prove Theorem 1.
This assertion turns out to be a version of Lemma 4 in the D →∞limit, except we need to bridge
the current formalism using (2p+1)-bit strings with the formalism in Ref. [13] using 2p-bit strings.
Following the notation in Ref. [13], we let

A = {(a1, a2, . . . , ap, a−p, . . . , a2, a1) : ai = ±1}
(B.1)

be the set of 2p-bit strings. We also let

Ap+1 = {a ∈A : a−r = ar for all 1 ≤r ≤p}.
(B.2)

Note that Ap+1 is the set B0 with the 0-th component removed. We use the index p + 1 because
it matches the conventions of Ref. [13]. Now note that T(a) as deﬁned in Eq. (A.3) for a ∈B can
also take a ∈A as argument since it does not depend on the value of a0. So in what follows we
slightly abuse notation to let T(a) to take arguments of both a ∈A and a ∈B.
We now deﬁne the “bar” operation from Ref. [13] as mentioned in Section 6. For any a ∈A,
we let

(
−a±r
if r = T(a)
a±r
if r ̸= T(a) .
(B.3)

¯a±r =

We also need the * operation deﬁned in Eq. (6.10), which we restate here: for any a ∈A, let a∗be
the bit string whose bits are given by

a∗
r = arar+1 · · · ap
and
a∗
−r = a−ra−r−1 · · · a−p
for 1 ≤r ≤p .
(B.4)

The * operation is one-to-one and therefore has a well deﬁned inverse acting on 2p-bit strings.
As discussed in Section 6, while H(m)(a) is deﬁned for a ∈B, it does not depend on a0. So we
abuse notation to let it take arguments of both a ∈A and a ∈B. The assertion of Eq. (6.21) we
wish to prove is the following lemma:

Lemma 7. For any a ∈A and 0 ≤m ≤p, we have

H(m)(a∗) = 1
if
a ∈Ap+1
and
H(m)(¯a∗) = H(m)(a∗)
if
a ̸∈Ap+1
(B.5)

Proof. We start by showing the ﬁrst half of Eq. (B.5). Note that if a ∈Ap+1 then a∗∈Ap+1. Also
note that H(m)(b) does not depend on b0. Then for any a ∈Ap+1, there is a corresponding b ∈B0
given by b±r = a∗
±r for 1 ≤r ≤p, and b0 = 1 so that H(m)(a∗) = H(m)(b). Applying Lemma 4 in
the D →∞limit with b ∈B0, we have H(m)(a∗) = H(m)(b) = 1.
For the second half of Eq. (B.5), we note from Eqs. (B.3) and (B.4) that for any a ∈A,

(
−a∗
±r
if 1 ≤r ≤T(a)
a∗
±r
if T(a) + 1 ≤r ≤p .
(B.6)

¯a∗
±r =

This is the same as the deﬁnition of the prime operation on b ∈B in Eq. (A.4), if one ignores the
0-th component. When b±r = a∗
±r, we have b′
±r = ¯a∗
±r. Hence, for any a ∈A \ Ap+1, there is a
corresponding b ∈B \ B0 with b0 = 1, such that H(m)(a∗) = H(m)(b) and H(m)(¯a∗) = H(m)(b′).
Since H(m)(b′) = H(m)(b) by Lemma 4 in the D →∞limit, we have H(m)(¯a∗) = H(m)(a∗),
concluding the proof.

37

## Page 38

C
Tables of best known γ, β for MaxCut

Table 4: Optimal values of γ and β up to p = 17.

38

## Page 39

Table 5: Suboptimal values of γ and β for p = 18, 19, 20 based on extrapolations of the optimal
values of γ and β up to p = 17 of Table 4. The values presented here are used to compute the
lower bounds on ¯νp of Table 2.

D
Optimal γ and β for Max-q-XORSAT at p = 14

0.6

0.5

0.4

γr

βr

0.3

0.2

0.1

0.0

0.0
0.2
0.4
0.6
0.8
1.0
(r - 1) / (p - 1)

0.0
0.2
0.4
0.6
0.8
1.0
(r - 1) / (p - 1)

Figure 7: Optimal QAOA parameters (γ, β) at p = 14 for various Max-q-XORSAT on D-regular
hypergraphs in the D →∞limit. This data can be found in Ref. [19].

39
