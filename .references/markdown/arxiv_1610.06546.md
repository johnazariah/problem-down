---
source_pdf: ../arxiv_1610.06546.pdf
pages: 23
extracted_at: 2026-04-17T12:32:29+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Hamiltonian Simulation by Qubitization"
author: "Guang Hao Low, Isaac L. Chuang, "
---

# arxiv_1610.06546

Original title: Hamiltonian Simulation by Qubitization

Author metadata: Guang Hao Low, Isaac L. Chuang, 

Source PDF: ../arxiv_1610.06546.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Hamiltonian Simulation by Qubitization

Guang Hao Low1 and Isaac L. Chuang2

1Department of Physics, Massachusetts Institute of Technology, Cambridge, Massachusetts, USA

2Department of Electrical Engineering and Computer Science, Department of Physics, Research Laboratory of Electronics,

Massachusetts Institute of Technology, Cambridge, Massachusetts, USA

July 12, 2019

arXiv:1610.06546v3 [quant-ph] 11 Jul 2019

We present the problem of approximating the time-evolution operator e−i ˆ
Ht to error ϵ,
where the Hamiltonian ˆH = (⟨G|⊗ˆI) ˆU(|G⟩⊗ˆI) is the projection of a unitary oracle ˆU onto
the state |G⟩created by another unitary oracle. Our algorithm solves this with a query
complexity O
t + log(1/ϵ)

to both oracles that is optimal with respect to all parameters
in both the asymptotic and non-asymptotic regime, and also with low overhead, using at
most two additional ancilla qubits. This approach to Hamiltonian simulation subsumes
important prior art considering Hamiltonians which are d-sparse or a linear combination
of unitaries, leading to signiﬁcant improvements in space and gate complexity, such as a
quadratic speed-up for precision simulations. It also motivates useful new instances, such
as where ˆH is a density matrix. A key technical result is ‘qubitization’, which uses the
controlled version of these oracles to embed any ˆH in an invariant SU(2) subspace. A large
class of operator functions of ˆH can then be computed with optimal query complexity, of
which e−i ˆ
Ht is a special case.

Contents

1
Introduction
2

2
Overview of the Quantum Signal Processor
5

3
Explicit Encodings of ˆH = (⟨G| ⊗ˆI) ˆU(|G⟩⊗ˆI)
7
3.1
Linear Combination of Unitaries
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
3.2
d-Sparse Hamiltonians . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
3.3
Puriﬁed Density Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9

4
Qubitization in a Quantum Signal Processor
9

5
Operator Function Design on a Quantum Signal Processor
11
5.1
Ancilla-Free Quantum Signal Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
5.2
Single-Ancilla Quantum Signal Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12

6
Application to Hamiltonian Simulation
15

7
Conclusion
16
7.1
Developments after preprint release . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17

8
Acknowledgments
17

A Qubitization of Normal Operators
17
A.1 Minimal example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18

B Practical Details for Implementing Hamiltonian Simulation
20

## Page 2

1
Introduction

Quantum computers were originally envisioned as machines for eﬃciently simulating quantum Hamilto-
nian dynamics. As Hamiltonian simulation is BQP-complete, the problem is believed to be intractable
by classical computers, and remains a strong primary motivation. The ﬁrst explicit quantum algorithms
for Hamiltonian simulation were discovered by Lloyd [1] for local interactions, and then generalized by
Aharonov and Ta-Shma [2] to sparse Hamiltonians. Celebrated achievements over the years [3–7] have
each ignited a ﬂurry of activity in diverse applications from quantum algorithms [8–11] to quantum
chemistry [12–18]. In this dawning era of the small quantum computer [19, 20], the relevance and
necessity of space and gate eﬃcient procedures for practical Hamiltonian simulation has intensiﬁed.
The cost of simulating the time-evolution operator e−i ˆ
Ht depends on several factors: the number
of system qubits n, evolution time t, target error ϵ, and how information on the Hamiltonian ˆH is
accessed by the quantum computer. This ﬁeld has progressed rapidly following groundbreaking work
in the fractional query model [21], which was the ﬁrst to achieve query complexities that depend
logarithmically on error. This was generalized by Berry, Childs, Cleve, Kothari, and Somma (BC-
CKS) [22] to the common case where ˆH = Pd
j=1 αj ˆUj is a linear combination of d unitaries1 with

log log (τ/ϵ)

ancilla qubits and only O
τ log (τ/ϵ)

an algorithm using O
log (d) log (τ/ϵ)

log log (τ/ϵ)

queries, where τ ←∥⃗α∥1t

and ∥⃗α∥1 = Pd
j=1 |αj| is the usual L1 norm. Subsequently, an extension was made to d-sparse Hamil-

tonians [6] that have at most d non-zero elements per row, also using O
τ log (τ/ϵ)

log log (τ/ϵ)

queries with
τ ←dt∥H∥max. A prominent open question in all these works was whether the additive lower bound
Ω
τ +
log(1/ϵ)
log log (1/ϵ)
2 was achievable for any of these models.
Recently, we found for the d-sparse model [7], which is popular in algorithm design by quantum
walks [23], a procedure achieving the optimal trade-oﬀbetween all parameters up to constant factors,
with query complexity O
τ+log (1/ϵ)
3. This strictly linear-time performance with additive complexity
is a quadratic improvement over prior art for precision simulations when t = Θ(log (1/ϵ)). Moreover,
the number of ancilla qubits required is independent of τ and ϵ, which is another important practical
improvement. The approach, based on Childs’ [4, 24, 25] extension of Szegedy’s quantum walk [26],
required two quantum oracles: one accepting a row j and column k index to return the value of entry
ˆHjk to m bits of precision, and another accepting a j row and l sparsity index to return in-place the
lth non-zero entry in row j.
Unfortunately, the d-sparse model is less appealing in practical implementations for several rea-
sons. First, it is exponentially slower than BCCKS when the ˆUj are of high weight with sparsity O(2n).
Second, its black-box oracles can be challenging to realize. Avoiding the exponential blowup by ex-
ploiting sparsity requires that positions of non-zero elements are both few in number and eﬃciently
row-computable, which is not always the case. Third, the Childs quantum walk requires a doubling of
the n system qubits, which is not required by BCCKS. It is unclear whether our methodology could
be applied to other formulations of Hamiltonian simulation, in contrast to alternatives that seem more
ﬂexible [27].
Ideally, the best features of these two algorithms could be combined, such as in Table 1.
For
example, given the decomposition ˆH = Pd
j=1 αj ˆUj, one would like the optimal additive complex-
ity of sparse Hamiltonian simulation, but with the BCCKS oracles that are more straightforward to
implement. Furthermore, one could wish for a constant ancilla overhead, of say ⌈log2(d)⌉+ 2, supe-

1A particularly interesting and general class of systems are k-local Hamiltonians with m terms.
These are also
m2k-sparse, and can be expressed as a linear combination of ≤m4k Pauli operators, each of which are unitary.

2A slightly tighter lower bound is Ω(q) queries, where q = min {q ∈Z+ : ϵ < | sin(|τ|/q)|q = O((τ/q)q)} [6, 21]. Note
that q ∈O(τ + log (1/ϵ)) ∩Ω
τ +
log(1/ϵ)
log log (1/ϵ)

.

3In the respective limits τ = Θ(1) and ϵ = Θ(1), the query complexity is O
log(1/ϵ)
log log (1/ϵ)

and O(τ). Importantly, this

does not imply a complexity of O
τ +
log(1/ϵ)
log log (1/ϵ)

. The precise form of the upper bound matches the lower bound with

respect to all parameters up to constant factors and lies between Ω
τ +
log(1/ϵ)
log log (1/ϵ)

and O
τ + log (1/ϵ)

## Page 3

Table 1:
Comparison of state-of-art with our new approaches (bottom three lines) for approximating e−i ˆ
Ht of
ˆH ∈C2n×2n with error ϵ. The d-sparse simulation oracle describes entries of ˆH with maximum absolute value
∥ˆH∥max = 1 to m bits of precision. The BCCKS oracle provides the decomposition ˆH = Pd
j=1 αj ˆUj, and each
ˆUj is given a cost O(C). The LMR query complexity refers to samples of the density matrix ˆρ = ˆH. This work
generalizes the above with oracles ˆG|0⟩= |G⟩∈Cd, ˆU ∈C2nd×2nd such that ⟨G| ˆU|G⟩= ˆH, where ∥ˆH∥≤1. A
new model where the oracle that outputs the puriﬁcation |ρ⟩= Pd
j=1 αj|j⟩a|ψj⟩, Tra[|ρ⟩⟨ρ|] = ˆρ is provided.

rior to either algorithm. These improvements would greatly enhance the potential of early practical
applications of quantum computation.
We achieve precisely this optimistic fusion via an extremely general procedure, made possible
by what we call ‘qubitization’, that subsumes both and motivates new formulations of Hamiltonian
simulation, as captured by this main theorem:

Theorem 1 (Optimal Hamiltonian simulation by Qubitization). Let (⟨G|a ⊗ˆIs) ˆU(|G⟩a ⊗ˆIs) = ˆH ∈
CN×N be Hermitian for some unitary ˆU ∈CNd×Nd and some state preparation unitary ˆG|0⟩a = |G⟩a ∈
Cd. Then e−i ˆ
Ht can be simulated for time t, error ϵ in spectral norm, and failure probability O(ϵ),
using at most ⌈log2(N)⌉+ ⌈log2(d)⌉+ 2 qubits in total, Θ(Q) queries to controlled- ˆG, controlled- ˆU,
and their inverses, and O(Q log (d)) additional two-qubit quantum gates where

Q = min

q ∈Z+ : ϵ ≥4|t|q

q!2q = O
eτ

q
= O(t + log (1/ϵ)).
(1)

2q

The optimality of the procedure follows by using oracles ˆG and ˆU that implement the Childs
quantum walk. Furthermore, the transparent Hamiltonian input model of Theorem 1 signiﬁcantly
expedites the development of new useful formulations of Hamiltonian simulation. For instance, we
easily obtain a new result for the scenario where ˆH is a density matrix ˆρ. Whereas ˆρ can be produced
by discarding the ancilla of some output from a quantum circuit ˆG, we instead keep this ancilla, leading
to an unconditional quadratic improvement in time scaling, and an exponential improvement in error
scaling over the sample-based Lloyd, Mohseni, and Rebentrost (LMR) model [5, 28], as summarized
in Table 1. Though certainly a stronger model than was previously considered, the inputs to many
quantum machine learning as well as quantum semideﬁnite programming [11] applications are actually
of this more restricted form, and are thus enhanced.
In fact, Hamiltonian simulation is just one application of our main innovation: an approach we
call the ‘quantum signal processor’, where the equation (⟨G|a ⊗ˆIs) ˆU(|G⟩a ⊗ˆIs) = ˆH in Theorem 1 is
interpreted as a non-unitary signal operator ˆH encoded in a subspace of an oracle ˆU ﬂagged by |G⟩a ⊗
ˆIs. This general encoding deﬁned in Deﬁnition 14 unveils a systematic approach toward exponential
quantum speedups with generic inputs, and is central to our results:

4After the original preprint release of this manuscript, standard-form encoding has been replaced in the community
by ‘block-encoding’ [29], which is a more informative description.

## Page 4

Table 2: List of six example problems (top row), solvable using the quantum signal processor approach to compute
an operator function f[·] of Hermitian ˆH = ⟨G| ˆU|G⟩. Through qubitization, the scope of inputs to the Quantum
Linear Systems Problem (QLSP) and Gibbs Sampling (Gibbs) can be any ˆH of this form, either indirectly through
Hamiltonian simulation, or directly through quantum signal processing. Quantum Phase Estimation (QPE) here
decides whether eigenphases θ of an implemented unitary satisfy some property e.g. f(θ) ≥1/2.

Deﬁnition 1 (Standard-form). A signal operator ˆH with spectral norm ∥ˆH∥≤1 is encoded in the
standard-form if we may query a unitary oracle ˆU : Ha⊗Hs →Ha⊗Hs and a unitary state preparation
oracle ˆG|0⟩a = |G⟩a ∈Ha with the property (⟨G|a ⊗ˆIs) ˆU(|G⟩a ⊗ˆIs) = ˆH. We also assume query
access to the inverses and controlled versions of ˆU, ˆG.

The inputs to many problems, highlighted in Table 2, can be of this form. We introduce ‘qubitiza-
tion’: the essential ﬁrst step that converts this description of ˆH into unitary evolution with properties
that depend directly on ˆH. When ˆH is Hermitian, The oracles ˆG and ˆU are queried to obtain a
Grover-like search parallelized over all eigenvalues λ of ˆH through the iterate, which is isomorphic to
e−i ˆY ⊗cos−1 [ ˆ
H] in some subspace. Similar structures are of foundational importance to many quantum
algorithms – the gap ∆of eigenvalues λ = 1 −∆of ˆH is ampliﬁed to cos−1 (λ) = O(
√

∆) in the
phase of the iterate, which resembles spectral gap ampliﬁcation [30], the quantization of stochastic
matrices [31], as well as Szegedy’s [26] and Childs’ [24] quantum walk. The key diﬀerence lies in the
generalized encoding of the signal operator through any ˆG and ˆU of Deﬁnition 1, instead of the more
restrictive sparse Hamiltonian formulation.
Unlike Grover search, we do not seek to prepare some target state. Rather, we exploit a direct sum
of Grover-like rotations that are each isomorphic to SU(2), to engineer arbitrary target functions f(λ)
of its overlap λ. The quantum signal processor exploits this structure to attack the often-considered
problem of designing a quantum circuit ˆQ that queries ˆG and ˆU such that in the standard-form,
(⟨G|a ⊗ˆIs) ˆQ(|G⟩a ⊗ˆIs) = f[ ˆH] for some target operator f[·]. Though this is accomplished in prior
art using the linear-combination-of-unitaries algorithm [25], that approach requires a case-by-case
detailed analysis of f to obtain the L1 norm of its coeﬃcients in a Taylor expansion, and has a success
probability that decays with the inverse square of this norm.
Our quantum signal processor computes f[ ˆH] with no such restrictions and with an optimal query
complexity that exactly matches polynomial lower bounds for a large class of functions.
We call
this ‘quantum signal processing’, which generalizes our previous results [7] for d-sparse oracles to
the standard-form and a larger class of functions.
Thus generic improvements to all applications
in Table 2 can be expected in query complexity, ancilla overhead, and scope of possible signal inputs.
In particular, Theorem 1 follows directly from the query complexity of the choice f(λ) = e−iλt, which
corresponds to applying −t sin (·) on eigenphases of the iterate.
In Section 2, we provide a detailed overview of the quantum signal processor, which uses the
standard-form encoding of a matrix ˆH in Deﬁnition 1 as an input. Our claim to the generality of this
encoding is justiﬁed in Section 3, where we map a variety of other common input models describing
matrices to the standard-form. The next key result is qubitization, which converts a standard-form
encoding to a Grover-like iterate, is proven in Section 4. By creatively applying this iterate, we show
in Section 5 how a large class of polynomials of ˆH may be eﬃciently computed. Our ﬁnal result on
Hamiltonian simulation by qubitization is proven in Section 6 by a simple choice for this polynomial.
Though we focus on qubitization of Hermitian matrices in the body of this paper, we also describe the
extension to normal matrices in Appendix A.

## Page 5

2
Overview of the Quantum Signal Processor

Since coherent quantum computation is restricted to unitary operations, one commonly ﬁnds a situ-
ation such as in Table 2, where post-selection is required to accomplish some desired quantum state
transformation. Consider some arbitrary input system quantum state |ψ⟩s ∈Hs and suppose that it is
transformed by some desired signal operator ˆH like |ψ⟩s →ˆH|ψ⟩s. In order to realize this operation,
which is non-unitary in general, it is necessary to embed ˆH in a larger Hilbert space.
This is embedding accomplished through some given unitary signal oracle ˆU : Ha ⊗Hs →Ha ⊗Hs
that acts jointly on Hs and another Hilbert space Ha.
The signal oracle encodes ˆH = (⟨G|a ⊗
ˆIs) ˆU(|G⟩a ⊗ˆIs) in a subspace ﬂagged by an ancilla signal state |G⟩a ∈Ha. This is the standard-form
of Deﬁnition 1, which applies ˆH as follows.

1 −∥ˆH|ψ⟩∥2|G⊥
ψ⟩as,
ˆU =
 ˆH
·
·
·


,
(⟨G|a ⊗ˆIs)|G⊥
ψ⟩as = 0.
(2)

ˆU|G⟩a|ψ⟩s = |G⟩a ˆH|ψ⟩s +
q

The signal state deﬁnes the measurement basis of the appended register Ha, which naturally divides
ˆU into two subspaces.
First, HG = |G⟩⊗Hs where the measurement succeeds with probability
∥ˆH|ψ⟩∥2 and ˆU|G⟩a|ψ⟩s is projected onto |G⟩a ˆ
H|ψ⟩s
∥ˆ
H|ψ⟩∥. Second, the orthogonal complement HG⊥where

the measurement fails. As probabilities are bounded by 1, the signal operator ˆH must have spectral
norm ∥ˆH∥≤1. Whenever the context is clear, we drop the ancilla and system subscripts, and use
|G⟩a ⊗ˆIs and |G⟩interchangeably. We represent ˆU such that the top-left block is precisely ˆH and acts
on an input state |Gψ⟩≡|G⟩|ψ⟩∈HG, whereas the undeﬁned parts of ˆU transform |Gψ⟩into some
orthogonal state |G⊥
ψ⟩∈HG⊥of lesser interest.
In the following, we consider the case where ˆH is a Hermitian matrix. The case of normal ˆH is
discussed in Appendix A. Thus the action of ˆU on |Gψ⟩in Eq. (2) can be written more clearly in the
eigenbasis of ˆH|λ⟩= λ|λ⟩. For each eigenstate of ˆH,

ˆU|G⟩|λ⟩= ˆU|Gλ⟩= λ|Gλ⟩+
p

1 −|λ|2|G⊥
λ ⟩,
(3)

and we ﬁnd it convenient to deﬁne the subspace Hλ = span{|Gλ⟩, ˆU|Gλ⟩}. Note the trivial case λ = 1
where Hλ is one-dimensional, which we will ignore. We also emphasize that the action of ˆU on states
orthogonal to |Gλ⟩are generally not easily controlled by the user, and thus left undeﬁned.
Given any scalar function f, our goal is to ﬁnd an optimal quantum circuit that transforms any
standard-form encoding of ˆH into a standard-form encoding of f[ ˆH] ≡P
λ f(λ)|λ⟩⟨λ|. We accomplish
this with the quantum signal processor.

Deﬁnition 2 (Quantum Signal Processor). A quantum signal processor solves the following.
Inputs:
• A Hermitian matrix ˆH with bounded spectral norm ∥ˆH∥≤1.
•
A function f : [−1, 1] →D, where D is the complex unit disc, i.e.
∀x ∈
[−1, 1], |f(x)| ≤1.

Resources:
• An encoding of ˆH = ⟨G| ˆU|G⟩by the oracles of Deﬁnition 1.
• A constant number of additional qubits.
• Arbitrary single and two-qubit gates.

Outputs:
• A standard-form encoding of f[ ˆH], i.e. a unitary ˆQ where f[ ˆH] = ⟨0| ˆQ|0⟩.

In the simplest case, one might wish to apply ˆH multiple times to generate higher moments. For
instance, ˆH2 would allow a direct estimate of variance.
Unfortunately, the subspace Hλ for each
eigenstate |λ⟩is not invariant under ˆU in general. As a result, repeated applications in this basis do
not produce higher moments of ˆH due to leakage out of Hλ. The structure of this leakage depends
on the undeﬁned components of ˆU, must be analyzed on a case-by-case basis, and thus is of limited
utility.

## Page 6

Order can be restored to this undeﬁned behavior by stemming the leakage. The simplest possibility
that preserves the signal operator of Eq. (2) replaces ˆU with a unitary, the iterate ˆW, that also encodes
ˆH = ⟨G| ˆW|G⟩, but for each eigenstate |λ⟩, performs a rotation in SU(2) on disjoint two-dimensional
subspaces Hλ = span{|Gλ⟩, ˆW|Gλ⟩} = span{|Gλ⟩, |G⊥
λ ⟩}. This deﬁnes the state |G⊥
λ ⟩through Gram-
Schmidt orthogonalization, and a set of Pauli operators ˆXλ, ˆYλ, ˆZλ for each subspace.

|G⊥
λ ⟩= ( ˆW −λ)|Gλ⟩
p

1 −|λ|2
,
ˆXλ|Gλ⟩= |G⊥
λ ⟩,
ˆYλ|Gλ⟩= i|G⊥
λ ⟩,
ˆZλ|Gλ⟩= |Gλ⟩.
(4)

In this basis, the iterate for each eigenvalue of ˆH is deﬁned to be exactly

1 −|λ|2|Gλ⟩⟨G⊥
λ |
+
p

ˆW =

λ
−
p

λ
=
λ|Gλ⟩⟨Gλ|
−
p



1 −|λ|2
p

1 −|λ|2|G⊥
λ ⟩⟨Gλ|
+λ|G⊥
λ ⟩⟨G⊥
λ | ,
(5)

1 −|λ|2
λ

On a general input |G⟩P

λ aλ|λ⟩∈HG, the iterate is represented by


λ
−
p



1 −|λ|2.
p

λ
e−i ˆYλθλ,
(6)

ˆW =
M

λ
=
M

1 −|λ|2.
λ

λ

where θλ is deﬁned through the equality

1 −|λ|2 = cos (θλ) −i sin (θλ) ⇒θλ = cos−1 (λ).
(7)

∀λ ∈[−1, 1], λ −i
p

In the following, the iterate will always be applied to states spanned by the subspace L

λ Hλ. Thus
its action on states outside this subspace need not be deﬁned. The usefulness of this construct is
evident. Due to its invariant subspace, multiple applications of the iterate result in highly structured
behavior. However, implementing ˆW appears diﬃcult in general. One one hand, the function
p

1 −|λ|2
must be computed for each eigenstate. In principle, this can be approximated using phase estimation
with considerable overhead [32]. On the other hand, it is not at all clear whether a unitary with the
form of ˆW can always be engineered from the standard-form encoding of ˆH. ‘Qubitization’ is our
solution to constructing this iterate with minimal overhead.

Theorem 2 (Qubitization). Given a Hermitian matrix ˆH = ⟨G|a ˆU|G⟩a encoded in standard-form as
described in Deﬁnition 1, the iterate ˆW of Eq. (6) can be constructed using at most one query each to
ˆG, controlled-U, their inverses, at most one additional qubit, and O(log (dim (Ha))) quantum gates.

Using the oracles ˆG, ˆU, and arbitrary unitary operations on only the ancilla register, we also provide
necessary and suﬃcient conditions in Lemma 8, for when ˆW can be implemented exactly using only one
query to ˆU. As these conditions are somewhat restrictive, we then prove in Lemma 10 that qubitization
is unconditionally possible by instead using the controlled- ˆU oracle in a quantum circuit that generates
the same ˆH and satisﬁes these conditions. We describe a similar construction for normal operators in
Appendix. A.
Observe that ˆW N eﬃciently produces Chebyshev polynomials TN[ ˆH] [9]. We call any function [·]
of the signal ˆH target operators when they occur in the top-left block and are thus automatically in
standard-form. The fact that Chebyshev polynomials are the best polynomial basis for L∞function
approximation on an ﬁnite interval [33] suggests that the any target operator f[ ˆH] = A[ ˆH] + iB[ ˆH]
could be approximated with a judicious choice of controls on the ancilla register. We present two
implementation of the quantum signal processor described in Deﬁnition 2. The ﬁrst does not require
any additional qubits beyond that for qubitization, and realizes a broad class of target operators f.

Theorem 3 (Ancilla-Free Quantum Signal Processing). A quantum signal processor can be imple-
mented with the following properties.

## Page 7

Inputs
• The iterate ˆW obtained from the qubitization procedure of Theorem 2 on a Hermitian
matrix ˆH = ⟨G| ˆU|G⟩encoded by the oracles of Deﬁnition 1.
• Real polynomials A(λ), B(λ) of degree Q and equal parity satisfying all following.
• A(1) = 1;
• ∀λ ∈[−1, 1], A2(λ) + B2(λ) ≤1;
• ∀λ ≥1, A2(λ) + B2(λ) ≥1;
• ∀Q even, λ ≥0, A2(iλ) + B2(iλ) ≥1.

Output:
• A standard-form encoding of A[ ˆH] + iB[ ˆH].

Cost
• Q queries to ˆW.
• Zero additional qubits beyond that for ˆW.
• O(Q log (dim (Ha))) arbitrary single and two-qubit gates.

Note that the two polynomials in our solution of ancilla-free quantum signal processing are of the
same parity. At this point, we assume that all ˆU have been qubitized and so use the iterate ˆW as our
basic building block. A diﬀerent basis set of functions with fewer restrictions on parity can be obtained
by embedding ˆW into yet another SU(2) invariant subspace by adding an ancilla qubit. This leads to
the second implementation of the quantum signal processor of Deﬁnition 2.

Theorem 4 (Single-Ancilla Quantum Signal Processing). A quantum signal processor can be imple-
mented with the following properties.
Inputs:
• The iterate ˆW obtained from the qubitization procedure of Theorem 2 on a Hermitian
matrix ˆH = ⟨G| ˆU|G⟩encoded by the oracles of Deﬁnition 1.
• Real polynomials A(λ), C(λ) of degree Q/2 and opposite parity satisfying all following.
• A(0) = 1;
• ∀λ ∈[−1, 1], A2(λ) + C2(λ) ≤1;

Output:
• A standard-form encoding of A[ ˆH] + iC[ ˆH].

Cost:
• Q queries to controlled- ˆW.
• One additional qubit beyond that for ˆW.
• O(Q log (dim (Ha))) arbitrary single and two-qubit gates.

These powerful tools for target operator processing, made possible by qubitization, are agnostic
to the underlying oracles that describe the signal operator ˆH. In many instances, converting this
description to the standard-form of Deﬁnition 1 is straightforward and is indeed how our Hamiltonian
simulation results for the varied input models of Table 1 are proven.

3
Explicit Encodings of ˆH = (⟨G| ⊗ˆI) ˆU(|G⟩⊗ˆI)

We now justify our motivation for encoding matrices ˆH in the standard-form format of ˆH = ⟨G| ˆU|G⟩
in Deﬁnition 1. A number of common techniques for encoding matrix problems on quantum computers
map naturally to the standard-form with minimal overhead. Thus taking the standard-form as our
starting point is without any loss of generality. This is demonstrated by the following three explicit
implementation of the oracles ˆU and ˆG|0⟩= |G⟩for Hamiltonians represented as a linear combination
of unitaries, d-sparse Hamiltonians, and a new input model where Hamiltonians are represented by a
puriﬁed density matrix.

3.1
Linear Combination of Unitaries

One option for implementing the standard-form encoding is provided by the Linear-Combination-of-
Unitaries algorithm (LCU) [3, 25], which underlies the BCCKS simulation algorithm. LCU is based

## Page 8

on the fact that any complex ˆH is a linear combination of some d unitary operators:

d
X

ˆH =

d
X

j=1
αj ˆUj,
∥ˆH∥≤∥⃗α∥1 =

j=1
|αj|,
(8)

where the upper bound on the spectral norm is ∥⃗α∥1. Note that this bound depends on the choice of
decomposition, but is tight for the some choice. Without loss of generality, all αj ≥0 by absorbing
complex phases into ˆUj. The algorithm assumes that the αj are provided as a list of d numbers, and
each ˆUj is provided as a quantum circuit composed of constant number O(C) of primitive gates. With
these inputs, the oracles

r αj

d
X

d
X

ˆG =

∥⃗α∥1
|j⟩⟨0|a + · · · ,
ˆU =

j=1

j=1
|j⟩⟨j|a ⊗ˆUj,
⟨G| ˆU|G⟩=
ˆH
∥⃗α∥1
(9)

can be constructed, where the ancilla state creation operator ˆG|0⟩= |G⟩is implemented with O(d)
primitive gates, and the selector ˆU is implemented with O(dC) primitive gate. By direct expansion of
ˆU ˆG|0⟩a|ψ⟩s, this leads exactly to Eq. (2). This proves the following.

Lemma 5 (Standard-Form Encoding by a Linear Combination of Unitaries). Let ˆG prepare the state
|G⟩a = Pd
j=1
p

αj/∥⃗α∥1|j⟩a where αj ≥0. Let ˆU = Pd
j=i |j⟩⟨j|a ⊗ˆUj. These oracles encode the

matrix ⟨G| ˆU|G⟩=
1
∥⃗α∥1
Pd
j=1 αj ˆUj.

Proof. Consider the computation

r αj




d
X

(⟨G|a ⊗ˆIs) ˆU(|G⟩a ⊗ˆIs) = (⟨G|a ⊗ˆIs)

j=1

d
X

=
1
∥⃗α∥1

√αjαk



d
X

∥⃗α∥1
|j⟩a ⊗ˆUj

∥⃗α∥1
⟨k|j⟩⊗ˆUj

=

j,k=1

j=1
αj ˆUj.
(10)

Of course, the optimal decomposition that costs the fewest number of ancilla qubits and primitive
gates may be diﬃcult to ﬁnd, and may not even ﬁt naturally in this model, but LCU shows that
implementing an encoding for any ˆH is possible in principle.

3.2
d-Sparse Hamiltonians

The model of d-sparse Hamiltonians is another paradigm for specifying matrices to quantum comput-
ers, and is particularly common in the design of quantum algorithms by quantum walks [2]. Such
Hamiltonians have at most d non-zero entries in any row, and information on their positions and
matrix values ˆHjk are accessed through the following two standard unitary oracles [4].

ˆOH|j⟩|k⟩|z⟩= |j⟩|k⟩|z ⊕ˆHjk⟩,
ˆOF |j⟩|l⟩= |j⟩|f(j, l)⟩.
(11)

Observe that ˆOH accepts a row j and column k index and returns ˆHjk in some binary format. The
other oracle ˆOF accepts a row j index and a number l ∈[d] to compute in-place the column index
f(j, l) of the lth non-zero element in row j. Given this input, we now encode ˆH in standard-form.

Lemma 6 (Standard-Form Encoding of a d-Sparse Hamiltonian). Let the oracles of Eq. (11) specify a
d-sparse Hamiltonian ˆH with max-norm ∥H∥max. Then the oracles encoding ⟨G| ˆU|G⟩=
ˆ
H
d∥ˆ
H∥max can
be implemented using O(1) queries.

## Page 9

Proof. Let |G⟩= |0⟩a1|0⟩a2|0⟩a3 ≡|0⟩a be a computational basis state, and let Fj = {f(j, l)}l∈[d] be
the set of column indices to all non-zero elements in row j. Ref. [4] shows how each of the isometries

s

|p⟩a3
√

ˆT1 =
X

j
|ψj⟩⟨0|a⟨j|s, |ψj⟩=
X

d

p∈Fj

s

⟨p|s
√

ˆT2 =
X

k
|χk⟩⟨0|a⟨k|s, ⟨χk| =
X

d

p∈Fk

s

1 −
|Hpj|

Hpj
∥ˆH∥max
|0⟩a1 +

∥ˆH∥max
|1⟩a1

|0⟩a2|j⟩s,
(12)

s

1 −
|Hkp|

Hkp
∥ˆH∥max
⟨0|a2 +

∥ˆH∥max
⟨1|a2

⟨0|a1⟨k|a3,

can be implemented using using 2 queries to ˆOH and 1 query to ˆOF . By construction, the overlap of
these states is ⟨χk|ψj⟩=
Hkj
d∥ˆ
H∥max . Now choose ˆU = ˆT †
2 ˆT1. By a direct computation,

(⟨G|a ⊗ˆIs) ˆU(|G⟩a ⊗ˆIs) =
X

Hkj
d∥ˆH∥max
|k⟩⟨j|s =
ˆH

k,j
|k⟩s⟨χk|ψj⟩⟨j|s =
X

3.3
Puriﬁed Density Matrix

d∥ˆH∥max
.
(13)

k,j

The simplicity of the standard-form encoding allows us to swiftly devise new input models for Hamil-
tonians. Here, we consider the case where a Hamiltonian ˆH = Tr [|G⟩⟨G|]a1 is a density matrix ˆρ
obtained by tracing out the ancilla register of a pure state prepared by some oracle ˆG. That is,

√αj|j⟩a1|χj⟩a2,
ˆρ = Tr [|G⟩⟨G|]a1 =
X

ˆG|0⟩a = |G⟩a =
X

j

j
αj|χj⟩⟨χj|.
(14)

Lemma 7 (Standard-Form Encoding of a Puriﬁed Density Matrix). Let the oracle of Eq. (14) pre-
pare a state ˆG|0⟩a = |G⟩a = P
j
√αj|j⟩a1|χj⟩a2 that is a puriﬁcation of the density matrix ˆρ =
P

j αj|χj⟩⟨χj| = Tr [|G⟩⟨G|]a1. Let ˆU be a unitary that swaps the register a2 with the system register
s. These oracles encode the matrix ⟨G| ˆU|G⟩= ˆρ.

Proof. Let {|λ⟩} be a complete basis on the system. By a direct computation,

j
⟨G|√αj|j⟩a1|λ⟩a2|χj⟩⟨λ|s =
X

⟨G| ˆU|G⟩a
X

λ
|λ⟩⟨λ|s =
X

X

λ

X

j
|αj||χj⟩s⟨χj|λ⟩⟨λ|s = ˆρ.
(15)

λ

4
Qubitization in a Quantum Signal Processor

This section describes qubitization in detail: the process for creating the iterate ˆW given ˆH encoded
in standard-form, and an essential component in a systematic procedure for implementing operator
transformations of ˆH. In Lemma 8, we provide necessary and suﬃcient conditions on when ˆW can
be constructed from the oracles ˆG, ˆU.
Then in Lemma 10, we show that any ˆG, ˆU not satisfying
these conditions can be eﬃciently transformed into a ˆG′, ˆU ′ that do, and encode the same signal
operator ˆH = ⟨G′| ˆU ′|G′⟩. Together, these Lemmas in the remainder of this section complete the proof
of Theorem 2 for the case of Hermitian ˆH.
For now, we assume that |G⟩is known. This soon proves to be unnecessary and only oracle access
to ˆG is required. Thus we must ﬁnd a unitary ˆS′, acting only on the ancilla register such that the
iterate ˆW = ˆS′ ˆU of Eq. (6) is obtained. For the case of Hermitian ˆH|λ⟩= λ|λ⟩, we now determine

## Page 10

necessary and suﬃcient conditions on what ˆS′ must be. As ˆS′ is otherwise arbitrary, we use without
loss of generality the ansatz of ˆS′ being a product of a reﬂection about |G⟩and another arbitrary
unitary ˆS on the ancilla:

ˆW = ((2|G⟩⟨G| −ˆI)a ⊗ˆIs) ˆS ˆU,
|Gλ⟩= |G⟩|λ⟩⇒|G⊥
λ ⟩= λ|Gλ⟩−ˆS ˆU|Gλ⟩
√

1 −λ2
.
(16)

Lemma 8 (Conditions on Qubitization). For all signal oracles ˆU that implement the Hermitian signal
operator ˆH, the unitary ˆS in Eq. (16) creates a unitary iterate ˆW with the same signal operator in the
same basis, but in an SU(2) invariant subspace containing |G⟩if and only if

⟨G|a ˆS ˆU|G⟩a = ˆH and ⟨G|a ˆS ˆU ˆS ˆU|G⟩a = ˆI.
(17)

Proof. In the forward direction, we assume Eq. (6), then compute and compare with Eq. (16): λ =
⟨Gλ| ˆW|Gλ⟩= ⟨Gλ| ˆS ˆU|Gλ⟩. By using this result repeatedly together with the fact that ˆS ˆU is unitary,
Gram-Schmidt orthonormalization of ˆW|Gλ⟩furnishes the state |G⊥
λ ⟩= λ|Gλ⟩−ˆS ˆU|Gλ⟩
√

onal to |Gλ⟩. By similarly computing and comparing −
√

1−λ2
which is orthog-

1 −λ2 = ⟨Gλ| ˆW|G⊥
λ ⟩= λ2−⟨Gλ|( ˆS ˆU)2|Gλ⟩
√

1−λ2
, we

obtain ⟨Gλ|( ˆS ˆU)2|Gλ⟩= 1. As these must be true for all eigenvectors |λ⟩, the conditions in Eq. (17)
are necessary.
That these are also suﬃcient follows from assuming Eq. (17) and attempting to recover the compo-
nents of Eq. (6) using the deﬁnitions of Eq. (16). By applying ⟨G|a ˆS ˆU|G⟩a = ˆH, we compute ˆW|Gλ⟩=
2|G⟩a⟨G|a ˆS ˆU|Gλ⟩−ˆS ˆU|Gλ⟩= 2λ|Gλ⟩−ˆS ˆU|Gλ⟩. In the basis of |Gλ⟩and |G⊥
λ ⟩, ⟨Gλ| ˆW|Gλ⟩= 2λ −

⟨Gλ| ˆS ˆU|Gλ⟩= λ and ⟨G⊥
λ | ˆW|Gλ⟩= ⟨Gλ|λ−⟨Gλ|( ˆS ˆU)†

√

1−λ2
=
√

1−λ2
(2λ|Gλ⟩−ˆS ˆU|Gλ⟩) = 2λ2−2λ2−λ2+1
√

1 −λ2.

A similar calculation for the remaining components requires ⟨G|a ˆS ˆU ˆS ˆU|G⟩a = ˆI and reveals that
⟨G⊥
λ | ˆW|G⊥
λ ⟩= λ and ⟨Gλ| ˆW|G⊥
λ ⟩= −
√

λ

λ
−
√



represent ˆW = L

1−λ2
√

λ.

1−λ2
λ

1 −λ2.
As this must be true for all λ, we may indeed

In hindsight, these results are manifest. After all, ⟨G| ˆS ˆU ˆS ˆU|G⟩= ˆI implies that ˆS ˆU is a reﬂection
when controlled by input state |G⟩, and it is well-known that a Grover iterate [34, 35] is the product
of two reﬂection about start and target subspaces. Nevertheless, the suﬃciency of these conditions
highlights that this is the simplest method to extract controllable and predictable behavior out of ˆU.
In particular, these conditions are automatically satisﬁed in the trivial case with ˆS = ˆIas when ˆU only
has eigenvalues ±1, such as when it is a controlled-Pauli operator.

Corollary 9 (Qubitization of Reﬂections). For all signal oracles ˆU that satisfy ˆU 2 = ˆIas and imple-
ment the Hermitian signal operator ⟨G|a ˆU|G⟩a = ˆH, the unitary iterate ˆW = ((2|G⟩⟨G| −ˆI)a ⊗ˆIs) ˆU
implements the same signal operator in the same basis, but in an SU(2) invariant subspace containing
|G⟩.

Proof. Set ˆS = ˆIas in Lemma 8, and verify that Eq. (17) is satisﬁed.

Unfortunately, a solution to Eq. (17) may not exist for more general ˆU. Lemma 8, amounts to
choosing ˆS such that ˆS ˆU ˆS is the inverse ˆU † whist preserving the signal operator ⟨G| ˆS ˆU|G⟩= ˆH.
Given that ˆS only acts on the ancilla register, it is hard to see how this is always possible. Even if so,
ˆS may be diﬃcult to implement as it is an arbitrary unitary acting on a potentially large ancilla register.
The solution is to construct a diﬀerent quantum circuit ˆU ′ that contains ˆU but still implements the
same signal operator, and crucially always has a extremely simple solution ˆS. We now show how this
can be done in all cases using only 1 query to controlled- ˆU and controlled- ˆU †.

Lemma 10 (Existence of Qubitization). For all signal unitaries ˆU that implement the Hermitian
signal operator ⟨G| ˆU|G⟩= ˆH, there exists a quantum circuit ˆU ′, using one more qubit, that queries

## Page 11

controlled- ˆU and controlled- ˆU † once to implements the same signal operator. Moreover, ˆU ′ satisﬁes
the conditions Eq. (17)

Proof. We prove this by an explicit construction. Let the controlled- ˆU operators be ˆV1 = |0⟩⟨0| ⊗ˆI +
|1⟩⟨1| ⊗ˆU †, ˆV2 = |0⟩⟨0| ⊗ˆU + |1⟩⟨1| ⊗ˆI. Thus the extra qubit states |0⟩, |1⟩, are ﬂags that selects
either ˆUj or ˆU †
j . By multiplying, ˆU ′ = ˆV1 ˆV2 = |0⟩⟨0| ⊗ˆU + |1⟩⟨1| ⊗ˆU †. Now consider the ancilla state
|G′⟩=
1
√

2(|0⟩+ |1⟩)|G⟩, and choose ˆS = (|0⟩⟨1| + |1⟩⟨0|) ⊗ˆIas. It is easy to verify that the conditions
of Eq. (17) is satisﬁed.

⟨G′| ˆS ˆU ′|G′⟩= ⟨G′| ˆU ′|G′⟩= 1

2( ˆH + ˆH†) = ˆH,
⟨G′| ˆS ˆU ′ ˆS ˆU ′|G′⟩= ⟨G′| ˆU ′† ˆU ′|G′⟩= ˆI,
(18)

where we have used the fact that ˆS|G′⟩= |G′⟩is an eigenstate, and that ˆS swaps the |0⟩, |1⟩ancilla
states in ˆU ′, thus transforming it into its inverse.

Even if we are given ˆU for which there is no solution to Eq. (17), we can always apply Lemma 10 to
construct a ˆU ′ that does with minimal overhead. Furthermore our proof uses no information about the
detailed structure of |G⟩. Thus without loss of generality, we can assume that any ˆG, ˆU have already
been qubitized.

5
Operator Function Design on a Quantum Signal Processor

The purpose of the quantum signal processor is to transform the signal ˆH into any desired target op-
erator f[ ˆH]. We present a systematic framework that furnishes the optimal complexity and a concrete
procedure for almost any f and show how an exact connection is made between query complexity and
the theory of best function approximations with polynomials [33, 36].
Qubitization in Section 4 is the essential ﬁrst step that makes this endeavor plausible, as evidenced
by the highly structured behavior of the iterate ˆW in Eq. (6), where for Hermitian ˆH, multiple
applications elegantly generate Chebyshev polynomials TL[ ˆH] [9]. To go further, additional control
parameters on ˆW are necessary, and in the following, we only consider Hermitian ˆH. Thus we introduce
the phased iterate ˆWφ with the same invariant subspace as ˆW, and parameterized by φ ∈R.


λ
−ie−iφp

ˆWφ =
M

−ieiφp

1 −|λ|2
λ

λ



1 −|λ|2

λ
e−i ˆφλθλ,
(19)

λ
=
M

where ˆφλ = cos (φ) ˆXλ + sin (φ) ˆYλ, and the eigenphase θλ is deﬁned similar to Eq. (7).

Lemma 11. The phased iterate ˆWφ in Eq. (19) is equal to ˆWφ = ˆZφ+π/2 ˆW ˆZ−φ−π/2, where ˆZφ =
((1 + e−iφ)|G⟩⟨G| −ˆI) is a partial reﬂection about |G⟩by angle φ ∈R and implements a relative phase
between the |Gλ⟩and |G⊥
λ ⟩subspaces. In block form,

ˆZφ =
M

λ


e−iφ
0
0
−1



λ
.
(20)

Proof. Let us compute the phase applied to states |Gλ⟩, |G⊥
λ ⟩:
ˆZφ|Gλ⟩= ((1 + e−iφ) −1)|Gλ⟩=
e−iφ|Gλ⟩and ˆZφ|G⊥
λ ⟩= −|G⊥
λ ⟩. As this true for all λ, Eq. (20) follows. Combining the representation
of ˆW from Eq. (6) with this leads to Eq. (19),


−ie−iφ
0
0
−1



ˆWφ = ˆZφ−π/2 ˆW ˆZ−φ+π/2 =
M

λ

λ


λ
−
p


ieiφ
0
0
−1





1 −|λ|2
p

λ
.

1 −|λ|2
λ

λ

## Page 12

We provide algorithms with diﬀerent overheads for large classes of transformations. ‘Ancilla-free
quantum signal processing’ in Section 5.1 implement target operators where the real and imaginary
parts have the same parity with respect to ˆH. Opposite parity is obtained by ‘single-ancilla quantum
signal processing’ in Section 5.2.

5.1
Ancilla-Free Quantum Signal Processing

Consider a sequence of Q of phased iterates, where the angle φ deﬁning each may diﬀer.

λ
e−i ˆφλ
Qθλ · · · e−iφλ
2 θλe−i ˆφλ
1 θλ,
ˆφλ
j = cos (φj) ˆXλ + sin (φj) ˆYλ.

ˆW⃗φ = ˆWφQ · · · ˆWφ2 ˆWφ1 =
M

λ
A(2θλ)ˆIλ + iB(2θλ) ˆZλ + iC(2θλ) ˆXλ + iD(2θλ) ˆYλ.
(21)

=
M

In each subspace Hλ, this is a product of SU(2) rotations. As such, we may decompose this in the
Pauli basis ˆIλ, ˆXλ, ˆYλ, ˆZλ with the real functions (A, B, C, D) as coeﬃcients. As we can only prepare
and measure in the basis of the state |G⟩a, consider the component ⟨G|a ˆW⃗φ|G⟩a = P

λ(A(θλ) +

iB(θλ))|λ⟩⟨λ| ≡A[ ˆH]+iB[ ˆH]. Any choice of phases ⃗φ ∈RQ generates sophisticated interference eﬀects
between elements of the sequence, leading to (A, B, C, D) with some non-trivial functional dependence
on ˆH. Though the dependence of the output on ⃗φ seems hard to intuit, they nevertheless specify a
program for computing functions of ˆH, similar to how a list of numbers might specify a polynomial.
To understand Eq. (21), it suﬃces to study the following sequence of single-qubit rotations.

ˆU⃗φ = e−i ˆφQθ/2 · · · e−i ˆφ2θ/2e−i ˆφ1θ/2 = A(θ)ˆI + iB(θ) ˆZ + iC(θ) ˆX + iD(θ) ˆY ,
(22)

These functions previously characterized in Ref. [37], and found the following.

Lemma 12 (Achievable A, B – Thm. 2.3 of Ref. [37]). For any integer Q > 0, a choice of functions
A(θ) ≡A(x), B(θ) ≡B(x) in Eq. (22) is achievable by some ⃗φ ∈RQ if and only if all the following are
true:
(1) A(x) and B(x) are real parity-(Q mod 2) polynomials in x = cos (θ/2) of degree at most Q;
(2) A(1) = 1;
(3) ∀x ∈[−1, 1], A2(x) + B2(x) ≤1;
(4) ∀x ≥1, A2(x) + B2(x) ≥1;
(5) ∀Q even, x ≥0, A2(ix) + B2(ix) ≥1.
Moreover, ⃗φ ∈RQ can be computed in classical O(poly(Q)) time.

In other words, we may specify only the components A, B, independent of the others C, D that are
of lesser interest. By mapping this result to Eq. (21), we complete the proof of Theorem 3.

Proof of Theorem 3. The unitary operators in each subspace Hλ of ˆW⃗φ are isomorphic to the product

of single qubit rotations e−i ˆφQθ/2 · · · e−i ˆφ2θ/2e−i ˆφ1θ/2. We identify θ/2 = θλ, where θλ = cos−1(λ) as
deﬁned in Eq. (7). Thus the result follows from Lemma 12 by substituting x = cos (θλ) = λ.

As polynomials form a complete basis on bounded real intervals, these results imply the query
complexity of approximating any real function A[ ˆH] with error ϵ is exactly that of its best polynomial
ϵ-approximation satisfying the constraints of Theorem 3, and similarly for the complex case.

5.2
Single-Ancilla Quantum Signal Processing

Using no ancilla, Theorem 3 implements a target operator f[ ˆH] where the real and complex parts are
constrained to have the same parity. By introducing additional ancilla, other general classes of functions
can be implemented, sometimes with looser constraints. In this section, we use a key observation from

## Page 13

Ref. [7]. Given any unitary ˆV with eigenstates ˆV |λ⟩= eiθλ|λ⟩and ˆV0 = |+⟩⟨+|b ⊗ˆIs + |−⟩⟨−|b ⊗ˆV
controlled by the single-qubit ancilla register b where ˆXb|±⟩b = ±|±⟩b, consider the sequence

Q/2
Y

k odd≥1
ˆV †
ϕk+1+π ˆVϕk = ˆV †
ϕQ+π · · · ˆVϕ3 ˆV †
ϕ2+π ˆVϕ1, ˆVϕ = (e−iϕ ˆ
Z/2 ⊗ˆIs) ˆV0(eiϕ ˆ
Z/2 ⊗ˆIs).
(23)

ˆV⃗ϕ =

For each eigenstate |λ⟩, we obtain a product of single qubit operators e−i ˆϕQθλ/2 · · · e−i ˆϕ1θλ/2 similar
to Eq. (21) but with a halved phased, and these only act on the ancilla b. Using the same reasoning
as in Section 5.1, the choice of ⃗ϕ determines the eﬀective single-qubit ancilla operator


ˆIbA(θλ) + i ˆZbB(θλ) + i ˆXbC(θλ) + i ˆYbD(θλ)

⊗|λ⟩⟨λ|s.
(24)

ˆV⃗ϕ =
M

λ

In the following, we focus on the functions A, C, which we also characterized fully in previous work.

Lemma 13 (Achievable (A, C) – Thm. 1 of Ref. [7]). For any even integer Q > 0, a choice of functions
A(θ), C(θ) in Eq. (22) is achievable by some ⃗φ ∈RQ if and only if all the following are true:
(1) A(θ) = PQ/2
k=0 ak cos (kθ) is a real cosine Fourier series of degree at most Q/2;
(2) C(θ) = PQ/2
k=1 ck sin (kθ) is a real sine Fourier series of degree at most Q/2;
(3) A(0) = 1;
(4) ∀θ ∈R, A2(θ) + C2(θ) ≤1.
Moreover, ⃗φ ∈RQ can be computed in classical O(poly(Q)) time.

In some cases, one might be given target functions A, C that are only ϵ-close to being achievable,
for instance, if A, C are the output of some numerical procedure. This poses no fundamental diﬃculty,
as we prove in the following, which generalizes slightly a similar statement in Ref. [7].

Lemma 14 (Stability of Achievable (A, C)). For any even integer Q > 0, let
(1) ˜
A(θ) = PQ/2
k=0 ak cos (kθ) be a real cosine Fourier series of degree at most Q/2;
(2) ˜C(θ) = PQ/2
k=1 ck sin (kθ) be a real sine Fourier series of degree at most Q/2;
(3) ˜
A(0) = 1 + ϵ1, where ϵ1 ≤1;
(4) ∀θ ∈R, ˜
A2(θ) + ˜C2(θ) ≤1 + ϵ2, where ϵ2 ∈[0, 1].
Then there exists Fourier series A, C that satisfy the conditions of Lemma 13, approximate

max
θ∈R |(A + iC) −( ˜
A + i ˜C)| = O(
p

|ϵ1| + ϵ2),
(25)

and are computable in classical O(poly(Q)) time.

Proof. First, we satisfy condition (4) of Lemma 13 by rescaling A1 =
˜
A
1+ϵ2 ,
C =
˜C
1+ϵ2 .
Second, we use the polynomial sum-of-squares technique to compute real Fourier series B1 =
PQ/2
k=0 bk cos (kθ) and D1 = PQ/2
k=1 dk sin (kθ) such that A2
1 + B2
1 + C2 + D2
1 = 1. Following [37, Section
C], this can be done in classical O(poly(Q)) time. By construction, A2
1(0) + B2
1(0) = 1 as C and D1
are odd functions. Let us deﬁne sin (δ) ≡B1(0). Hence, cos (δ) ≡A1(0) = 1+ϵ1

1+ϵ2 .
Third, let A(θ) = cos (δ)A1(θ) + sin (δ)B1(θ). By deﬁnition, A(0) = cos2 (δ) + sin2 (δ) = 1. Thus
A, C satisfy satisfy the conditions of Lemma 13.

## Page 14

Last, we bound the error of this approximation.

max
θ∈R |(A + iC) −( ˜
A + i ˜C)|

≤max
θ∈R |(A + iC) −(A1 + iC)| + max
θ∈R |(A1 + iC) −( ˜
A + i ˜C)|
by a triangle inequality

≤max
θ∈R |(cos (δ) −1)A1(θ) + sin (δ)B1(θ)| + ϵ2

≤
q

(cos (δ) −1)2 + sin2 (δ) + ϵ2
using A2
1(θ) + B2
1(θ) ≤1

≤
√

1 −cos (δ) + ϵ2 =
r

2ϵ2 −ϵ1

2
p

1 + ϵ2
+ ϵ2

= O(
p

|ϵ1| + ϵ2).
(26)

We now prove Theorem 4 by evaluating Eq. (24) using Lemma 13 for the case where the arbitrary
unitary ˆV is replaced with the more structured iterate eiΦ ˆW, and also where we have added a global
phase Φ ∈R.

Proof of Theorem 4. Observe from Eq. (6) that eiΦ ˆW can be diagonalized to obtain its eigenvalues
θλ± and eigenvectors |Gλ±⟩.

eiΦ ˆW|Gλ±⟩= ei(Φ+θλ±)|Gλ±⟩,
θλ± = ∓cos−1 (λ),
|Gλ±⟩= |Gλ⟩± i|G⊥
λ ⟩
√

With this substitution ˆV ←eiΦ ˆW, Eq. (24) becomes

2
.
(27)


ˆIbA(Φ + θλ±) + i ˆXbC(Φ + θλ±) + · · ·

⊗|Gλ±⟩⟨Gλ±|as.
(28)

ˆV⃗ϕ =
M

λ,±

Similar to Section 5.1, we are only allowed to prepare and measure in the subspace supported by signal
state |G⟩a. Recall that (⟨G|a ⊗ˆIs)|G⊥
λ ⟩= 0, so projecting the sequence Eq. (28) onto |+⟩b|G⟩a results
in

⟨G|a⟨+|b ˆV⃗ϕ|+⟩b|G⟩a =
M

λ,±
(A(Φ + θλ±) + iC(Φ + θλ±)) ⊗⟨G|a|Gλ±⟩⟨Gλ±|as|G⟩a

P

± (A(Φ + θλ±) + iC(Φ + θλ±))

=
M

λ

2
⊗|λ⟩⟨λ|.
(29)

For this proof, it suﬃces to choose Φ = π/2, and set ak = 0 for all odd k, and ck = 0 for all even
k. We then evaluate each component of Eq. (29) using Lemma 13 and the Chebyshev polynomials
Tk(x) ≡cos (k cos−1 (x)).

Q/2
X

Q/2
X

A(π/2 + θλ±) =

k even
ak cos (k(π/2 + θλ±)) =

Q/2
X

Q/2
X

C(π/2 + θλ±) =

k odd
ck sin (k(π/2 + θλ±)) =

Q/2
X

k even
a′
kTk(λ) = A(λ),
(30)

k even
akikTk(λ) =

Q/2
X

k odd
ckik−1Tk(λ) =

k odd
c′
kTk(λ) = C(λ).

## Page 15

Thus Eq. (29) simpliﬁes to

⟨G|a⟨+|b ˆV⃗ϕ|+⟩b|G⟩a =
M

λ
(A(λ) + iC(λ)) ⊗|λ⟩⟨λ|.
(31)

We now express the conditions of Lemma 13 in terms of polynomials. As Tk(−x) = (−1)kTk(x),
conditions (1) and (2) map to A(λ) being an even polynomial and C(λ) being an odd polynomial
respectively. When θλ± = −π/2, this implies that λ = cos (±π/2) = 0. Hence condition (3) maps to
A(π/2 + θλ± = 0) = 1 ⇒A(λ = 0) = 1. As λ ∈[−1, 1] for all values of θλ±, condition (4) maps to
∀λ ∈[−1, 1], A2(λ) + C2(λ) ≤1.

Of course, other choices of Φ, such as Φ = 0, π/3, π/4, ..., lead to diﬀerent families of target
functions. However, those are beyond the scope of this work.

6
Application to Hamiltonian Simulation

With these results for qubitization and operator function design with a quantum signal processor,
the application to Hamiltonian simulation follows easily. We complete the proof Theorem 1, and then
apply these results to obtain our claims of improvements in Table 1. Given any Hamiltonian ˆH encoded
in the standard-form of Deﬁnition 1, Theorem 4 allows us to use 2Q queries to encode exactly any
function A[ ˆH] + iC[ ˆH] where A(λ) and C(λ) are bounded polynomials of opposite parity and degree
Q. Hamiltonian simulation is accomplished by choosing a good degree Q polynomial approximation
to A(λ) + iC(λ) = e−iλt.

Proof of Theorem 1. Similar to previous approaches [6, 7], we approximate e−iλt with the Jacobi-
Anger expansion ei cos (z)t = P∞
k=−∞ikJk(t)eikz [38], where Jk(t) are Bessel function of the ﬁrst kind.
By identifying cos (z) = λ, suitable polynomials A, C are obtained by a truncation and rescaling of

∞
X

e−iλt = J0(t) + 2

∞
X

k odd>0
(−1)(k−1)/2Jk(t)Tk(λ).
(32)

k even>0
(−1)k/2Jk(t)Tk(λ) + i2

The error from truncating this expansion for k > Q = q −1 is a sum of |Jk(t)| that was bounded in [6]:

2

≤

∞
X

∞
X

k=q
(−1)
k
2 Jk(t)Tk(λ)

ϵ =
max
λ∈[−1,1]

⇒log
1


= O

q log
2q



ϵ

et

⇒q = O(t + log (1/ϵ)).

k=q
2|Jk(t)| ≤4tq

2qq! = O
et

q
(33)

q

The rapid converge by truncation arises as e−iλt is an entire analytic function [39].
With the choice

Q
X

˜A(λ) = J0(t) + 2

Q
X

k even>0
(−1)k/2Jk(t)Tk(λ),
˜C(λ) = 2

k odd>0
(−1)(k−1)/2Jk(t)Tk(λ)
(34)

the error maxλ∈[−1,1] | ˜A(λ) + i ˜C(λ) −e−iλt| ≤ϵ. Though this choice satisﬁes conditions (1-2) of Theo-
rem 4, it is only ϵ-close to satisfying conditions (3-4). Fortunately, this is not a fundamental problem
following the stability analysis of Lemma 14. One can perturb ˜A(λ), ˜C(λ) to construct approximations
A(λ) + iC(λ) that are achievable, with error maxλ∈[−1,1] |A(λ) + iC(λ) −e−iλt| = O(
p

ϵ). Thus the
overall procedure constructs a unitary ˆV⃗ϕ that approximates the time-evolution operator with error

## Page 16

∥⟨+|b⟨G|a ˆV⃗ϕ|G⟩a|+⟩b −e−i ˆ
Ht∥= O(√ϵ). The failure probability is O(ϵ), and solving for Q furnishes
stated the number of queries to ˆW and hence the oracles encoding ˆH = ⟨G| ˆU|G⟩.

As we have already shown in Section 3 how a variety of matrix input models such as linear-
combination-of-unitaries, d-sparse Hamiltonians, and puriﬁed density matrices map to the standard-
form encoding, their respective algorithms for simulating the time-evolution operators follow trivially.

Corollary 15 (Hamiltonian Simulation of a Sparse Hermitian Matrix). Given access to the oracle
of Eq. (11) specifying a d-sparse Hamiltonian ˆH, time evolution by ˆH can be simulated for time t and
error ϵ with O(dt∥ˆH∥max + log (1/ϵ)) queries to ˆOH, ˆOF .

Proof. Follows from combining Theorem 1 with the standard-form encoding Lemma 6.

The query complexity in Eq. (33) for this sparse case exactly matches a lower bound based on
simulating a Hamiltonian that solves PARITY with unbounded error [21], valid for all parameter
values, and not just in asymptotic limits [6, 7]. This completes the optimality proof of Theorem 1.
The case where ˆH decomposes into a linear combination of unitaries is an immediate application:

Corollary 16 (Hamiltonian Simulation of a Linear Combination of Unitaries). Given access to the
oracles of Eq. (9) specifying a Hamiltonian ˆH = Pd
j=1 αj ˆUj, time evolution by ˆH can be simulated for
time t and error ϵ with O(αt + log (1/ϵ)) queries.

Proof. Follows from combining Theorem 1 with the standard-form encoding Lemma 5.

The intuitiveness of Theorem 1 allows us to swiftly devise new models of Hamiltonian simulation.

Corollary 17 (Hamiltonian Simulation of a Puriﬁed Density Matrix). Given access to the ora-
cle Eq. (14) specifying a Hamiltonian ˆH = ˆρ that is a density matrix ˆρ, time evolution by ˆH can
be simulated for time t and error ϵ with O(t + log (1/ϵ)) queries.

Proof. Follows from combining Theorem 1 with the standard-form encoding Lemma 7.

In all the above, the query complexity O(· · · t+log (1/ϵ)) is an upper bound on the more precise form
of Eq. (33). The exact the tradeoﬀbetween ϵ, t, Q in Eq. (33) is studied numerically in Appendix B,
together with example phases ⃗ϕ implementing ˆV⃗ϕ for the polynomials in Eq. (34).

7
Conclusion

Our general procedure for Hamiltonian simulation in Theorem 1 extends the scope of possible useful
formulations of Hamiltonian simulation.
As seen in Table 1, it encompasses any case where the
Hamiltonian is embedded in a ﬂagged subspace of the signal unitary. Given this, a simulation algorithm
with query complexity optimal in all parameters, and also not just in asymptotic limits, is easily
obtained with minimal overhead.
While this procedure contains and signiﬁcantly improves upon
important models where the Hamiltonian is d-sparse or a linear combination of unitaries, its greater
value lies in illuminating an intuitive and straightforward path to other as-yet undiscovered models of
Hamiltonian simulation. In particular, our result for time-evolution by a puriﬁed density matrix is a
quadratic improvement in time and an exponential improvement in error over the sample-based model
– the proof of which consisted of just a few lines.
Many other exciting directions extend from this work. One example is how additional structural
information about ˆH [40] may be exploited. This is illustrated by when the spectral norm of ∥ˆH∥is
signiﬁcantly smaller than the sum of coeﬃcients ∥⃗α∥1 of a particular linear combination of unitaries
decomposition. If this decomposition were to be used, simulation would take time O
∥⃗α∥1t+log (1/ϵ)


– a factor ∥⃗α∥1/∥ˆH∥slowdown. Unfortunately, an ∥⃗α∥1 = O(∥ˆH∥) decomposition appears diﬃcult to

## Page 17

ﬁnd in general. Furthermore, it is easy to construct pathological ˆH with small norms, but nevertheless
decompose by naive methods into components with large spectral norms [41]. Our approach oﬀers a
possible solution – one ﬁnds any encoding the Hamiltonian in the standard-form, rather than some
speciﬁc decomposition into parts with properties dictated by the formulation. It remains an interesting
challenge to identify the cases where, and determine how structural information may be incorporated.
These advances are special cases arising from our vision of the more general quantum signal proces-
sor. Through qubitization, structure is imposed onto any unitary process implementing some Hermitian
signal operator. This structure allows for eﬃcient processing of the signal by the techniques of quan-
tum signal processing into some more desired form. As the query complexity of approximating any
arbitrary target function of the signal exactly matches fundamental bounds lower in polynomial and
Fourier approximation theory [33], we expect this to have numerous application in metrology [42] and
other quantum algorithms [35].

7.1
Developments after preprint release

The preprint of this manuscript was released on October 2016. There have since been a number of
developments building oﬀ, or relating to, the concepts of the standard-form encoding, qubitization,
and quantum signal processing that could be of interest to the reader.

Singular value transformations: The standard-form encoding, qubitization, and quantum
signal processing of Hermitian or normal matrices has been extended to perform polynomial
transformations on the singular value of arbitrary matrices [43]. This generalization has proven
to be surprisingly broad, and provides a uniﬁed framework for deriving and understanding many
other quantum algorithms.

Structured Hamiltonian simulation: The Hamiltonian of many interesting systems possess
additional structure that should be exploited to further reduce the cost of simulation. More
reﬁned simulation algorithms can exploit prior knowledge of geometric locality [44, 45], Hamilto-
nian induced one-norm [46], spectral norm [47], and separation of energy scales [48]. In particular,
these algorithms are also optimal, up to sub-polynomial factors, with respect to their structural
parameters.

Numerical Quantum signal processing: The numerical algorithm for decomposing target
polynomials of degree Q into phases was originally claimed to be polynomial time [37], but only
when counting arbitrary-precision arithmetical operations, and appeared to be ill-conditioned
in case studies [49]. A more thorough analysis [50] proved that the algorithm had a runtime of
O(Q3 polylog(Q/ϵ)) with ﬁnite-precision arithmetic, provided that some subtleties were carefully
managed to control this ill-conditioned behavior.

8
Acknowledgments

G.H.Low and I.L.Chuang thank Robin Kothari, Yuan Su, and Andrew Childs for insightful discus-
sions, the excellent reviews by anonymous referees, and acknowledge funding by the ARO Quantum
Algorithms Program and NSF RQCC Project No.1111337.

A
Qubitization of Normal Operators

The results of Lemmas 8 and 10 for qubitization can be extended to normal operators. Let ⟨G|a ˆU|G⟩a =
ˆH in Eq. (2) encode a normal matrix ˆH.
It is well known that any normal matrix has a polar
decomposition

ˆH = ˆHU · ˆHH.
(35)

## Page 18

where ˆHU is unitary, ˆHH is positive-semideﬁnite, [ ˆHU, ˆHH] = 0 commute. Thus the eigenvalues are
ˆH|λ⟩= eiθλλ|λ⟩, where λ ≥0, θλ ∈R, and

ˆU|G⟩|λ⟩= ˆU|Gλ⟩= λeiθλ|Gλ⟩+
p

1 −|λ|2|G⊥
λ ⟩,
(36)

This reduces to a Hermitian operator when ˆHU has eigenvalues ±1, and reduces to a unitary
operator when all ˆHH has eigenvalues 1. The trivial approach to qubitization in fact applies to any
complex matrix. We simply use the construction of Lemma 10 to implement the Hermitian signal
operator 1

2( ˆH + ˆH†).
Another possibility uses two phased iterates in an alternating sequence on input state |G⟩a|ψ⟩s,

ˆWφ± = ˆZφ−π/2(2|G⟩⟨G| −ˆI) ˆU± ˆZ−φ+π/2,
ˆW⃗φ± = ˆW⃗φ = ˆWφL+ · · · ˆWφ3+ ˆWφ2−ˆWφ1+,
(37)

where ˆU+ = ˆU and ˆU−= ˆU †. We work through a minimal example in Appendix A.1, from which
it follows that for each eigenstate |λ⟩, the iterates ˆWφ± maps states in the subspace spanned by
{|G⟩|λ⟩, ˆWπ/2,±|G⟩|λ⟩} to a state in the span of {|G⟩|λ⟩, ˆWπ/2,∓|G⟩|λ⟩}. Let us deﬁne the following
states by Gram-Schmidt orthogonalization

|G⊥±
λ
⟩= (λeiθλ −ˆWπ/2,±)|Gλ⟩
p

Then these iterates have form

1 −|λ|2
.
(38)

ˆWφ± =
λe±iθλ|Gλ⟩⟨Gλ|
−ie−iφ√

1 −λ2|Gλ⟩⟨G⊥∓
λ
|
−ieiφ√

1 −λ2|G⊥±
λ
⟩⟨Gλ|
+λe∓iθλ|G⊥±
λ
⟩⟨G⊥∓
λ
| .
(39)

The subspace spanned by these states is only invariant in general under the action of iterates with
alternating sign ±, such as the product ˆWφi−ˆWφj+. In other words, they are not invariant under any
repeated application of an iterate of the same sign. With the understanding that we only consider
alternating sequences, each ˆWφ± has the representation

ˆWφ± =

e±iθλλ
−ie−iφ√

−ieiφ√


.
(40)

1 −λ2

1 −λ2
e∓iθλλ

Note that when all eigenvalues λ are identical and φ = π/2, this reduces to Oblivious amplitude
ampliﬁcation [4], and we recover Hermitian qubitization when all θλ = 0. While this approach uses one
less ancilla qubit than the construction of Lemma 10, quantum signal processing can only be performed
on controlled block of even length ˆW⃗φ±, as only they have an invariant subspace. This limitation can
be relevant in some cases, such as Hamiltonian simulation where quantum signal processing is applied
to a single ˆWφ.

A.1
Minimal example

A minimal example illustrating the phenomenon of normal qubitization is worked through in this
section. For simplicity, let us drop the |λ⟩state. Let us set the phase φ = π/2 in the ˆZ· operator.
Let |G⟩→|0⟩. Let R = 2|0⟩⟨0| −1. Let us map the subspace spanned by {|G⟩|λ⟩, |G⊥+
λ
⟩, |G⊥−
λ
⟩} →
{|0⟩, −|1⟩, −|2⟩}. Then

1 −|λ|2|1⟩,
U †|0⟩= λ∗|0⟩+
p

U|0⟩= λ|0⟩+
p

1 −|λ|2|2⟩,
(41)

1 −|λ|2|1⟩,
RU †|0⟩= λ∗|0⟩−
p

RU|0⟩= λ|0⟩−
p

1 −|λ|2|2⟩.

## Page 19

Figure 1:
(Left) Approximation error ϵ = maxθ∈R |A[θ] −iC[θ] −eit sin (θ)|. (A[θ], C[θ]) are real Fourier series
in (cos (kθ), sin (kθ)), k = 0, ..., Q/2, and ϵ is plotted for the upper bound
4tq

## Page 20

Table 3: Table of phases implementing target function h(θ) = t sin (θ) in quantum signal processing. Errors quoted
refer to ∥⟨+|b ˆV⃗ϕ|+⟩b −e−i ˆ
Ht∥≤ϵ.

B
Practical Details for Implementing Hamiltonian Simulation

This appendix illustrates a speciﬁc application of the quantum signal processing approach to a sig-
nal unitary that encodes the Hamiltonian ˆH as a signal operator.
In particular, a comparison of
performance with the BCCKS approach is made. The details will be useful to readers interested in
implementing our procedure on a quantum computer. These include plots for the exact error scal-
ing Eq. (33) of the Q/2 term Fourier approximation to eit sin (θ) in Fig. 1(Left), and the number of
required queries per unit of simulated time in Fig. 1(Right). Furthermore, a table of select phases ⃗ϕ
computed using the algorithm in [37] can be found in Table 3.
In the interests of a fair comparison, Fig. 1(Right) counts the number of queries to the signal
operator ˆU in the ˆH = ⟨G| ˆU|G⟩encoding. ˆU is not assumed to be qubitized, thus incurring a factor
2 additional cost from querying ˆU and ˆU † each over the asymptotic limit of 2 queries per unit of
simulation time in Fig. 1(Left). Similarly, the BCCKS algorithm [22] incurs a factor 3 additional cost
from querying ˆU twice and ˆU † in their use of oblivious amplitude ampliﬁcation. As BCCKS is known
to be optimal in the regime t = O(
log (1/ϵ)
log log (1/ϵ)), the improvement of our approach is most dramatic

outside of it. In particular, the queries per unit time of BCCKS scales like O(
log (t/ϵ)
log log (t/ϵ)), whereas our
approach approaches 4 in the limit t →∞.
The number of queries to in the BCCKS model is 3Kr, where K is the queries per segment
e−i ˆ
H log 2/r, r = ⌈t/ log (2)⌉is the number of segments, and 3 is for oblivious amplitude ampliﬁcation
on each segment. K is chosen such that P∞
k=K+1
logk 2

k!
≤ϵ

r. An analysis of the procedure [22] shows
that the error of its simulated evolution is a factor O(1) ≳2 larger than ϵ.
Thus Fig. 1 slightly
overestimates BCCKS performance as we take ϵ directly to be the error.

References

[1] S. Lloyd, “Universal Quantum Simulators,” Science 273, 1073 (1996).
[2] D. Aharonov and A. Ta-Shma, “Adiabatic quantum state generation and statistical zero knowl-

## Page 21

edge,” in Proceedings of the thirty-ﬁfth ACM symposium on Theory of computing - STOC ’03,
STOC ’03 (ACM Press, New York, New York, USA, 2003) p. 20.
[3] A. M. Childs and N. Wiebe, “Hamiltonian Simulation Using Linear Combinations of Unitary
Operations,” Quantum Information & Computation 12, 901 (2012).
[4] D. W. Berry and A. M. Childs, “Black-box Hamiltonian simulation and unitary implementation,”

Quantum Information & Computation 12, 29 (2012).
[5] S. Lloyd, M. Mohseni,
and P. Rebentrost, “Quantum principal component analysis,” Nature
Physics 10, 631 (2014).
[6] D. W. Berry, A. M. Childs, and R. Kothari, “Hamiltonian Simulation with Nearly Optimal De-
pendence on all Parameters,” in 2015 IEEE 56th Annual Symposium on Foundations of Computer
Science, FOCS ’15 (IEEE, Washington, DC, USA, 2015) pp. 792–809.
[7] G. H. Low and I. L. Chuang, “Optimal Hamiltonian Simulation by Quantum Signal Processing,”

Physical Review Letters 118, 010501 (2017).
[8] A. W. Harrow, A. Hassidim, and S. Lloyd, “Quantum Algorithm for Linear Systems of Equations,”

Physical Review Letters 103, 150502 (2009).
[9] A. M. Childs, R. Kothari, and R. D. Somma, “Quantum Algorithm for Systems of Linear Equa-
tions with Exponentially Improved Dependence on Precision,” SIAM Journal on Computing 46,
1920 (2017).
[10] A. N. Chowdhury and R. D. Somma, “Quantum algorithms for Gibbs sampling and hitting-time
estimation,” Quantum Information & Computation 17, 41 (2017).
[11] F. G. Brandao and K. M. Svore, “Quantum Speed-Ups for Solving Semideﬁnite Programs,” 2017
IEEE 58th Annual Symposium on Foundations of Computer Science (FOCS) , 415 (2017).
[12] M.-H. Yung, J. D. Whitﬁeld, S. Boixo, D. G. Tempel,
and A. Aspuru-Guzik, “Introduction to
Quantum Algorithms for Physics and Chemistry,” in Quantum Information and Computation for
Chemistry (John Wiley & Sons, Inc., 2014) pp. 67–106.
[13] D. Wecker, B. Bauer, B. K. Clark, M. B. Hastings,
and M. Troyer, “Gate-count estimates for
performing quantum chemistry on small quantum computers,” Physical Review A 90, 022305
(2014).
[14] D. Poulin, M. B. Hastings, D. Wecker, N. Wiebe, A. C. Doherty, and M. Troyer, “The Trotter
step size required for accurate quantum simulation of quantum chemistry,” Quantum Information
& Computation 15, 361 (2015).
[15] M. Reiher, N. Wiebe, K. M. Svore, D. Wecker, and M. Troyer, “Elucidating reaction mechanisms
on quantum computers,” Proceedings of the National Academy of Sciences 114, 7555 (2017).
[16] R. Babbush, D. W. Berry, I. D. Kivlichan, A. Y. Wei, P. J. Love, and A. Aspuru-Guzik, “Expo-
nentially more precise quantum simulation of fermions in second quantization,” New Journal of
Physics 18, 033032 (2016).
[17] I. D. Kivlichan, N. Wiebe, R. Babbush,
and A. Aspuru-Guzik, “Bounding the costs of quan-
tum simulation of many-body physics in real space,” Journal of Physics A: Mathematical and
Theoretical 50, 305301 (2017).
[18] P. J. J. O’Malley, R. Babbush, I. D. Kivlichan, J. Romero, J. R. McClean, R. Barends, J. Kelly,
P. Roushan, A. Tranter, N. Ding, B. Campbell, Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth, A. G.
Fowler, E. Jeﬀrey, E. Lucero, A. Megrant, J. Y. Mutus, M. Neeley, C. Neill, C. Quintana, D. Sank,
A. Vainsencher, J. Wenner, T. C. White, P. V. Coveney, P. J. Love, H. Neven, A. Aspuru-Guzik,
and J. M. Martinis, “Scalable Quantum Simulation of Molecular Energies,” Physical Review X 6,
031007 (2016).
[19] R. Barends, J. Kelly, A. Megrant, A. Veitia, D. Sank, E. Jeﬀrey, T. C. White, J. Mutus, A. G.
Fowler, B. Campbell, Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth, C. Neill, P. O’Malley,
P. Roushan, A. Vainsencher, J. Wenner, A. N. Korotkov, A. N. Cleland,
and J. M. Martinis,
“Superconducting quantum circuits at the surface code threshold for fault tolerance,” Nature
508, 500 (2014).
[20] S. Debnath, N. M. Linke, C. Figgatt, K. A. Landsman, K. Wright, and C. Monroe, “Demonstration
of a small programmable quantum computer with atomic qubits,” Nature 536, 63 (2016).

## Page 22

[21] D. W. Berry, A. M. Childs, R. Cleve, R. Kothari, and R. D. Somma, “Exponential improvement in
precision for simulating sparse Hamiltonians,” in Proceedings of the 46th Annual ACM Symposium
on Theory of Computing - STOC ’14, STOC ’14 (ACM Press, New York, New York, USA, 2014)
pp. 283–292.
[22] D. W. Berry, A. M. Childs, R. Cleve, R. Kothari, and R. D. Somma, “Simulating Hamiltonian
Dynamics with a Truncated Taylor Series,” Physical Review Letters 114, 090502 (2015).
[23] A. M. Childs, R. Cleve, E. Deotto, E. Farhi, S. Gutmann,
and D. A. Spielman, “Exponential
algorithmic speedup by a quantum walk,” in Proceedings of the thirty-ﬁfth ACM symposium on
Theory of computing - STOC ’03, STOC ’03 (ACM Press, New York, New York, USA, 2003)
p. 59.
[24] A. M. Childs, “On the Relationship Between Continuous- and Discrete-Time Quantum Walk,”

Communications in Mathematical Physics 294, 581 (2010).
[25] R. Kothari, Eﬃcient algorithms in quantum query complexity, Ph.D. thesis, University of Waterloo
(2014).
[26] M. Szegedy, “Spectra of Quantized Walks and a
√

δϵ rule,” arXiv preprint quant-ph/0401053
(2004).
[27] D. W. Berry and L. Novo, “Corrected Quantum Walk for Optimal Hamiltonian Simulation,”

Quantum Information & Computation 16, 1295 (2016).
[28] S. Kimmel, C. Y.-Y. Lin, G. H. Low, M. Ozols, and T. J. Yoder, “Hamiltonian simulation with
optimal sample complexity,” npj Quantum Information 3, 13 (2017).
[29] S. Chakraborty, A. Gilyén, and S. Jeﬀery, “The power of block-encoded matrix powers: improved
regression techniques via faster Hamiltonian simulation,” arXiv preprint arXiv:1804.01973 (2018).
[30] R. D. Somma and S. Boixo, “Spectral Gap Ampliﬁcation,” SIAM Journal on Computing 42, 593
(2013).
[31] M. Szegedy, “Quantum Speed-Up of Markov Chain Based Algorithms,” in 45th Annual IEEE
Symposium on Foundations of Computer Science, FOCS ’04 (IEEE, Washington, DC, USA, 2004)
pp. 32–41.
[32] A. Daskin and S. Kais, “An ancilla-based quantum simulation framework for non-unitary matri-
ces,” Quantum Information Processing 16, 33 (2017).
[33] G. Meinardus, Approximation of Functions: Theory and Numerical Methods, Springer Tracts in
Natural Philosophy, Vol. 13 (Springer Berlin Heidelberg, Berlin, Heidelberg, 1967).
[34] L. K. Grover, “A fast quantum mechanical algorithm for database search,” Proceedings of the
twenty-eighth annual ACM symposium on Theory of computing - STOC ’96 STOC ’96, 212
(1996).
[35] T. J. Yoder, G. H. Low,
and I. L. Chuang, “Fixed-Point Quantum Search with an Optimal
Number of Queries,” Physical Review Letters 113, 210501 (2014).
[36] J. McClellan, T. Parks, and L. Rabiner, “A computer program for designing optimum FIR linear
phase digital ﬁlters,” IEEE Transactions on Audio and Electroacoustics 21, 506 (1973).
[37] G. H. Low, T. J. Yoder, and I. L. Chuang, “Methodology of Resonant Equiangular Composite
Quantum Gates,” Physical Review X 6, 041067 (2016).
[38] M. Abramowitz, I. A. Stegun,
and Others, “Handbook of mathematical functions,” Applied
mathematics series 55, 62 (1966).
[39] J. P. Boyd, “Rootﬁnding for a transcendental equation without a ﬁrst guess: Polynomialization
of Kepler’s equation through Chebyshev polynomial expansion of the sine,” Applied Numerical
Mathematics 57, 12 (2007).
[40] A. M. Childs and R. Kothari, “Limitations on the Simulation of Non-sparse Hamiltonians,” Quan-
tum Information & Computation 10, 669 (2010).
[41] R. D. Somma, “A Trotter-Suzuki approximation for Lie groups with applications to Hamiltonian
simulation,” Journal of Mathematical Physics 57, 062202 (2016).
[42] G. H. Low, T. J. Yoder,
and I. L. Chuang, “Quantum Imaging by Coherent Enhancement,”
Physical Review Letters 114, 100801 (2015).

## Page 23

[43] A. Gilyén, Y. Su, G. H. Low,
and N. Wiebe, “Quantum singular value transformation and
beyond: exponential improvements for quantum matrix arithmetics,” in Proceedings of the 51st
Annual ACM Symposium on Theory of Computing - STOC ’19 (ACM Press, New York, New
York, USA, 2019) pp. 193–204.
[44] J. Haah, M. Hastings, R. Kothari,
and G. H. Low, “Quantum Algorithm for Simulating Real
Time Evolution of Lattice Hamiltonians,” in 2018 IEEE 59th Annual Symposium on Foundations
of Computer Science (FOCS), FOCS ’18 (IEEE, Washington, DC, USA, 2018) pp. 350–360.
[45] A. M. Childs and Y. Su, “Nearly optimal lattice simulation by product formulas,” arXiv preprint
arXiv:1901.00564 (2019).
[46] G. H. Low and I. L. Chuang, “Hamiltonian Simulation by Uniform Spectral Ampliﬁcation,” arXiv
preprint arXiv:1707.05391 (2017).
[47] G. H. Low, “Hamiltonian simulation with nearly optimal dependence on spectral norm,” in Pro-
ceedings of the 51st Annual ACM Symposium on Theory of Computing - STOC ’19 (ACM Press,
New York, New York, USA, 2019) pp. 491–502.
[48] G. H. Low and N. Wiebe, “Hamiltonian Simulation in the Interaction Picture,” arXiv preprint
arXiv:1805.00675 (2018).
[49] A. M. Childs, D. Maslov, Y. Nam, N. J. Ross, and Y. Su, “Toward the ﬁrst quantum simulation
with quantum speedup,” Proceedings of the National Academy of Sciences 115, 9456 (2018).
[50] J. Haah, “Product Decomposition of Periodic Functions in Quantum Signal Processing,” arXiv
preprint arXiv:1806.10236 (2018).
[51] L. J. Karam and J. H. McClellan, “Chebyshev digital FIR ﬁlter design,” Signal Processing 76, 17
(1999).
