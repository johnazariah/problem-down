---
source_pdf: ../arxiv_quant-ph_0001106.pdf
pages: 24
extracted_at: 2026-04-17T12:32:46+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "arXiv:quant-ph/0001106v1  28 Jan 2000"
---

# arxiv_quant-ph_0001106

Original title: arXiv:quant-ph/0001106v1  28 Jan 2000

Source PDF: ../arxiv_quant-ph_0001106.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Quantum Computation by Adiabatic Evolution

Edward Farhi, Jeﬀrey Goldstone∗

Center for Theoretical Physics
Massachusetts Institute of Technology
Cambridge, MA 02139

Sam Gutmann†

Department of Mathematics
Northeastern University
Boston, MA 02115

arXiv:quant-ph/0001106v1 28 Jan 2000

Michael Sipser‡

Department of Mathematics
Massachusetts Institute of Technology
Cambridge, MA 02139

MIT CTP # 2936
quant-ph/0001106

Abstract
We give a quantum algorithm for solving instances of the satisﬁability problem, based on adiabatic
evolution. The evolution of the quantum state is governed by a time-dependent Hamiltonian that
interpolates between an initial Hamiltonian, whose ground state is easy to construct, and a ﬁnal
Hamiltonian, whose ground state encodes the satisfying assignment. To ensure that the system
evolves to the desired ﬁnal ground state, the evolution time must be big enough. The time required
depends on the minimum energy diﬀerence between the two lowest states of the interpolating
Hamiltonian. We are unable to estimate this gap in general. We give some special symmetric
cases of the satisﬁability problem where the symmetry allows us to estimate the gap and we show
that, in these cases, our algorithm runs in polynomial time.

1
Introduction

We present a quantum algorithm for the satisﬁability problem (and other combinatorial search prob-
lems) that works on the principle of quantum adiabatic evolution.
An n-bit instance of satisﬁability is a formula

C1 ∧C2 ∧· · · ∧CM
(1.1)

where each clause Ca is True or False depending on the values of some subset of the bits. For a single
clause, involving only a few bits, it is easy to imagine constructing a quantum device that evolves
to a state that encodes the satisfying assignments of the clause. The real diﬃculty, of course, lies in
constructing a device that produces an assignment that satisﬁes all M clauses.
Our algorithm is speciﬁed by an initial state in an n-qubit Hilbert space and a time-dependent
Hamiltonian H(t) that governs the state’s evolution according to the Schr¨odinger equation. The
Hamiltonian takes the form

H(t) = HC1(t) + HC2(t) + · · · + HCM (t)
(1.2)

∗farhi@mit.edu ; goldston@mitlns.mit.edu
†sgutm@neu.edu
‡sipser@math.mit.edu
This work was supported in part by The Department of Energy under cooperative agreement DE–FC02–94ER40818,
by the National Science Foundation under grant NSF 95–03322 CCR, and by a joint NTT/LCS research contract.

## Page 2

2
Quantum Computation by Adiabatic Evolution

where each HCa depends only on clause Ca and acts only on the bits in Ca. H(t) is deﬁned for t between
0 and T and is slowly varying. The initial state, which is always the same and easy to construct, is
the ground state of H(0). For each a, the ground state of HCa(T ) encodes the satisfying assignments
of clause Ca. The ground state of H(T ) encodes the satisfying assignments of the intersection of all
the clauses. According to the adiabatic theorem, if the evolution time T is big enough, the state of the
system at time T will be very close to the ground state of H(T ), thus producing the desired solution.
For this algorithm to be considered successful we require that T grow only polynomially in n, the
number of bits. In this paper we analyze three examples where T grows only polynomially in n. We
are unable to estimate the required running time T in general.
The quantum adiabatic evolution that we are using should not be confused with cooling. For
example, simulated annealing is a classical algorithm that attempts to ﬁnd the lowest energy conﬁgu-
ration of what we have called H(T ) by generating the stochastic distribution proportional to e−βH(T ),
where β is the inverse temperature, and gradually lowering the temperature to zero. In contrast, quan-
tum adiabatic evolution forces the state of the system to remain in the ground state of the slowly
varying H(t).
In Section 2 we present the building blocks of our algorithm in detail. This includes some discus-
sion of the adiabatic theorem and level crossings. In Section 3 we illustrate the method on a small
example that has three clauses, each acting on 2 bits. Each 2-bit clause has more than one satisfying
assignment but adiabatic evolution using H(t) of the form (1.2) produces the unique common sat-
isfying assignment. In Section 4 we look at examples that grow with the number of bits in order to
study the dependence of the required running time on the number of bits. We give three examples
of 2-SAT problems, each of which has a regular structure, which allows us to analyze the quantum
evolution. In these three cases the required evolution time T is only polynomially big in the number of
bits. We also look at a version of the Grover problem that can be viewed as a relativized satisﬁability
problem. In this case our algorithm requires exponential time to produce a solution. This had to be
so, as explained in Section 4.2.
In Section 5 we show that our algorithm can be recast within the conventional paradigm of quantum
computing, involving sequences of few-bit unitary operators.

2
Adiabatic Evolution for Solving Satisﬁability

In this section we present a quantum algorithm for solving satisﬁability problems.

2.1
The Adiabatic Theorem

A quantum system evolves according to the Schr¨odinger equation

i d

dt |ψ(t)⟩= H(t) |ψ(t)⟩
(2.1)

and the adiabatic theorem [1] tells us how to follow this evolution in the case that H(t) is slowly
varying. Consider a smooth one-parameter family of Hamiltonians eH(s), 0 ≤s ≤1, and take

H(t) = eH(t/T )
(2.2)

so that T controls the rate at which H(t) varies. Deﬁne the instantaneous eigenstates and eigenvalues
of eH(s) by

H(s) |ℓ; s⟩= Eℓ(s) |ℓ; s⟩
(2.3)

## Page 3

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
3

with

E0(s) ≤E1(s) ≤· · · ≤EN−1(s)
(2.4)

where N is the dimension of the Hilbert space. Suppose |ψ(0)⟩is the ground state of eH(0), that is,

|ψ(0)⟩= |ℓ= 0; s = 0⟩.
(2.5)

According to the adiabatic theorem, if the gap between the two lowest levels, E1(s)−E0(s), is strictly
greater than zero for all 0 ≤s ≤1, then

lim
T →∞
⟨ℓ= 0; s = 1| ψ(T )⟩
= 1 .
(2.6)

This means that the existence of a nonzero gap guarantees that |ψ(t)⟩obeying (2.1) remains very
close to the instantaneous ground state of H(t) of the form (2.2) for all t from 0 to T if T is big
enough. Let us deﬁne the minimum gap by

gmin = min
0≤s≤1
E1(s) −E0(s)

.
(2.7)

A closer look at the adiabatic theorem tells us that taking

T ≫
E

where

D
ℓ= 1; s
d eH

E = max
0≤s≤1

ds

g2
min
(2.8)

ℓ= 0; s
E
(2.9)

can make
⟨ℓ= 0; s = 1| ψ(T )⟩
(2.10)

arbitrarily close to 1. For all of the problems that we study E is of order a typical eigenvalue of H
and is not too big, so the size of T is governed by g−2
min.

2.2
The Satisﬁability Problem

Many computationally interesting problems can be recast into an equivalent problem of ﬁnding a
variable assignment that minimizes an “energy” function. As a speciﬁc example, consider 3-SAT. An
n-bit instance of 3-SAT is a Boolean formula, (1.1), that is speciﬁed by a collection of Boolean clauses,
each of which involves (at most) 3 of the n bits. Each bit zi can take the value 0 or 1 and the i label
runs from 1 to n. Clause C is associated with the 3 bits labeled iC, jC, and kC. For each clause C we
deﬁne an energy function

hC(ziC, zjC, zkC) =
 0 ,
if (ziC, zjC, zkC) satisﬁes clause C
1 ,
if (ziC, zjC, zkC) violates clause C.
(2.11)

We then deﬁne the total energy h as the sum of the individual hC’s,

h =
X

C
hC .
(2.12)

Clearly h ≥0 and h(z1, z2, . . . , zn) = 0 if and only if (z1, z2, . . . , zn) satisﬁes all of the clauses. Thus
ﬁnding the minimum energy conﬁguration of h tells us if the formula has a satisfying assignment.
We will not distinguish between conventional clauses, which compute the OR function of each
constituent variable or negated variable, and generalized clauses, which are permitted to compute
an arbitrary Boolean function of the constituent variables. In some of our examples it will be more
convenient to consider generalized clauses.

## Page 4

4
Quantum Computation by Adiabatic Evolution

2.3
The Problem Hamiltonian HP

If we go from classical to quantum computation we replace the bit zi by a spin- 1

2 qubit labeled by
|zi⟩where zi = 0, 1. The states |zi⟩are eigenstates of the z component of the i-th spin,

|0⟩=
 1
0

so


and
|1⟩=
 0
1


(2.13)

2(1 −σ(i)
z ) |zi⟩= zi |zi⟩
where
σ(i)
z
=
 1
0
0
−1

1


.
(2.14)

The Hilbert space is spanned by the N = 2n basis vectors |z1⟩|z2⟩· · · |zn⟩. Clause C is now associated
with the operator HP,C,

HP,C(|z1⟩|z2⟩· · · |zn⟩) = hC(ziC, zjC, zkC) |z1⟩|z2⟩· · · |zn⟩.
(2.15)

The Hamiltonian associated with all of the clauses, which we call HP,

HP =
X

C
HP,C
(2.16)

is the sum of Hamiltonians each of which acts on a ﬁxed number of bits. By construction, HP is
nonnegative, that is, ⟨ψ| HP |ψ⟩≥0 for all |ψ⟩and HP |ψ⟩= 0 if and only if |ψ⟩is a superposition
of states of the form |z1⟩|z2⟩· · · |zn⟩where z1, z2, . . . , zn satisfy all of the clauses. In this context,
solving a 3-SAT problem is equivalent to ﬁnding the ground state of a Hamiltonian. Clearly many
other computationally interesting problems can be recast in this form.

2.4
The Initial Hamiltonian HB

For a given problem, specifying HP is straightforward but ﬁnding its ground state may be diﬃcult.
We now consider an n-bit Hamiltonian HB that is also straightforward to construct but whose ground
state is simple to ﬁnd. Let H(i)
B
be the 1-bit Hamiltonian acting on the i-th bit

2(1 −σ(i)
x )
with
σ(i)
x
=
 0
1
1
0

H(i)
B = 1

so

H(i)
B |xi = x⟩= x |xi = x⟩

where

 1
1

|xi = 0⟩=
1

√

2


(2.17)


and
|xi = 1⟩=
1


1
−1


.
(2.18)

√

2

Continuing to take 3-SAT as our working example, clause C is associated with the bits iC, jC, and
kC. Now deﬁne

HB,C = H(iC)
B
+ H(jC)
B
+ H(kC)
B
(2.19)

and

HB =
X

C
HB,C .
(2.20)

## Page 5

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
5

The ground state of HB is |x1 = 0⟩|x2 = 0⟩· · · |xn = 0⟩. This state, written in the z basis, is a super-
position of all 2n basis vectors |z1⟩|z2⟩· · · |zn⟩,

2n/2
X

|x1 = 0⟩|x2 = 0⟩· · · |xn = 0⟩=
1

z1

Note that we can also write

n
X

HB =

X

z2
· · ·
X

zn
|z1⟩|z2⟩· · · |zn⟩.
(2.21)

i=1
diH(i)
B
(2.22)

where di is the number of clauses in which bit i appears in the instance of 3-SAT being considered.
The key feature of HB is that its ground state is easy to construct. The choice we made here will
lead to an H(t) that is of the form (1.2), that is, a sum of Hamiltonians associated with each clause.

2.5
Adiabatic Evolution

We will now use adiabatic evolution to go from the known ground state of HB to the unknown ground
state of HP. Assume for now that the ground state of HP is unique. Consider

H(t) = (1 −t/T )HB + (t/T )HP
(2.23)

so from (2.2),

eH(s) = (1 −s)HB + sHP .
(2.24)

Prepare the system so that it begins at t = 0 in the ground state of H(0) = HB. According to the
adiabatic theorem, if gmin is not zero and the system evolves according to (2.1), then for T big enough
|ψ(T )⟩will be very close to the ground state of HP, that is, the solution to the computational problem.
Using the explicit form of (2.16) and (2.20) we see that H(t) and eH(s) are sums of individual
terms associated with each clause. For each clause C let

HC(t) = (1 −t/T )HB,C + (t/T )HP,C
(2.25)

and accordingly

eHC(s) = (1 −s)HB,C + sHP,C .
(2.26)

Then we have

H(t) =
X

and

eH(s) =
X

C
HC(t)
(2.27)

C
eHC(s) .
(2.28)

This gives the explicit form of H(t) described in the Introduction as a sum of Hamiltonians associated
with individual clauses.

## Page 6

6
Quantum Computation by Adiabatic Evolution

2.6
The Size of the Minimum Gap and the
Required Evolution Time

Typically gmin is not zero. To see this, note from (2.7) that vanishing gmin is equivalent to there being
some value of s for which E1(s) = E0(s). Consider a general 2 × 2 Hamiltonian whose coeﬃcients are
functions of s

a(s)
c(s) + id(s)
c(s) −id(s)
b(s)


(2.29)

where a, b, c, and d are all real. The two eigenvalues of this matrix are equal for some s if and
only if a(s) = b(s), c(s) = 0, and d(s) = 0. The curve
a(s), b(s), c(s), d(s)

in R4 will typically not
intersect the line (y, y, 0, 0) unless the Hamiltonian has special symmetry properties. For example,
suppose the Hamiltonian (2.29) commutes with some operator, say for concreteness σx. This implies
that a(s) = b(s) and d(s) = 0. Now for the two eigenvalues to be equal at some s we only require c to
vanish at some s. As s varies from 0 to 1 it would not be surprising to ﬁnd c(s) cross zero so we see
that the existence of a symmetry, that is, an operator which commutes with the Hamiltonian makes
level crossing more commonplace. These arguments can be generalized to N × N Hamiltonians and
we conclude that in the absence of symmetry, levels typically do not cross. We will expand on this
point after we do some examples.
In order for our method to be conceivably useful, it is not enough for gmin to be nonzero. We must
be sure that gmin is not so small that the evolution time T is impractically large; see (2.8). For an
n-bit problem we would say that adiabatic evolution can be used to solve the problem if T is less than
np for some ﬁxed p whereas the method does not work if T is of order an for some a > 1. Returning
to (2.8) we see that the required running time T also depends on E given in (2.9). Using (2.24) we
have d eH/ds = HP −HB. Therefore E can be no larger than the maximum eigenvalue of HP −HB.
From (2.16) we see that the spectrum of HP is contained in {0, 1, 2, . . ., M} where M is the number of
terms in (2.16), that is, the number of clauses in the problem. From (2.22) we see that the spectrum
of HB is contained in {0, 1, 2, . . ., d} where d = P di. For 3-SAT, d is no bigger than 3M. We are
interested in problems for which the number of clauses grows only as a polynomial in n, the number
of bits. Thus E grows at most like a polynomial in n and the distinction between polynomial and
exponential running time depends entirely on gmin.
We make no claims about the size of gmin for any problems other than the examples given in
Section 4. We will give three examples where gmin is of order 1/np so the evolution time T is polynomial
in n. Each of these problems has a regular structure that made calculating gmin possible. However,
the regularity of these problems also makes them classically computationally simple. The question
of whether there are computationally diﬃcult problems that could be solved by quantum adiabatic
evolution we must leave to future investigation.

2.7
The Quantum Algorithm

We have presented a general quantum algorithm for solving SAT problems. It consists of:

1. An easily constructible initial state (2.21), which is the ground state of HB in (2.20).

2. A time-dependent Hamiltonian, H(t), given by (2.23) that is easily constructible from the given
instance of the problem; see (2.16) and (2.20).

3. An evolution time T that also appears in (2.23).

4. Schr¨odinger evolution according to (2.1) for time T .

## Page 7

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
7

5. The ﬁnal state |ψ(T )⟩that for T big enough will be (very nearly) the ground state of HP.

6. A measurement of z1, z2, . . . , zn in the state |ψ(T )⟩. The result of this measurement will be
a satisfying assignment of formula (1.1), if it has one (or more). If the formula (1.1) has no
satisfying assignment, the result will still minimize the number of violated clauses.

Again, the crucial question about this quantum algorithm is how big must T be in order to solve
an interesting problem. It is not clear what the relationship is, if any, between the required size of T
and the classical complexity of the underlying problem. The best we have been able to do is explore
examples, which is the main subject of the rest of this paper.

3
One-, Two-, and Three-Qubit Examples

Here we give some one-, two-, and three-qubit examples that illustrate some of the ideas of the
introduction. The two-qubit examples have clauses with more than one satisfying assignment and
serve as building blocks for the three-qubit example and for the more complicated examples of the
next section.

3.1
One Qubit

Consider a one-bit problem where the single clause is satisﬁed if and only if z1 = 1. We then take

HP = 1

2 + 1

2σ(1)
z
(3.1)

which has |z1 = 1⟩as its ground state. For the beginning Hamiltonian we take (2.22) with n = 1 and
d1 = 1,

HB = H(1)
B
= 1

2 −1

2σ(1)
x
.
(3.2)

2(1 ±
√

The smooth interpolating Hamiltonian eH(s) given by (2.24) has eigenvalues 1

1 −2s + 2s2),
which are plotted in Fig. 1.
We see that gmin is not small and we could adiabatically evolve from
|x1 = 0⟩to |z1 = 1⟩with a modest value of T .
At this point we can illustrate why we picked the beginning Hamiltonian, HB, to be diagonal in
a basis that is not the basis that diagonalizes the ﬁnal problem Hamiltonian HP. Suppose we replace
HB by H′
B

H′
B = 1

2 −1

2σ(1)
z
(3.3)

keeping HP as in (3.1). Now eH(s) is diagonal in the z-basis for all values of s. The two eigenvalues
are s and (1 −s), which are plotted in Fig. 2. The levels cross so gmin is zero. In fact there is a
symmetry, eH(s) commutes with σz for all s, so the appearance of the level cross is not surprising.
Adiabatically evolving, starting at |z1 = 0⟩, we would end up at |z1 = 0⟩, which is not the ground
state of HP. However, if we add to HB any small term that is not diagonal in the z basis, we break
the symmetry, and eH(s) will have a nonzero gap for all s. For example, the Hamiltonian
"
s
ε(1 −s)

ε(1 −s)
1 −s

#

(3.4)

has gmin = ε for ε small and the eigenvalues are plotted in Fig. 3 for a small value of ε. This “level
repulsion” is typically seen in more complicated systems whereas level crossing is not.

## Page 8

8
Quantum Computation by Adiabatic Evolution

1

0.9

0.8

0.7

eigenvalues

0.6

0.5

0.4

0.3

0.2

0.1

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0

s

Figure 1: The two eigenvalues of eH(s) for a one-qubit example.

3.2
Two Qubits

A simple two-qubit example has a single two-bit clause that allows the bit values 01 and 10 but not 00
and 11. We call this clause “2-bit disagree.” We take HB of the form (2.22) with n = 2 and d1 = d2 = 1,
and we take HP of the form (2.16) with the single 2-bit disagree clause. The instantaneous eigenvalues
of eH(s) of the form (2.24) are shown in Fig. 4. There are two ground states of HP, |z1 = 0⟩|z2 = 1⟩
and |z1 = 1⟩|z2 = 0⟩. The starting state |ψ(0)⟩, which is the ground state of HB, is (2.21) with n = 2.
There is a bit-exchange operation |z1⟩|z2⟩→|z2⟩|z1⟩that commutes with eH(s). Since the starting
state |ψ(0)⟩is invariant under the bit-exchange operation, the state corresponding to the s = 1 end
of the lowest level in Fig. 4 is the symmetric state
1

2
|z1 = 0⟩|z2 = 1⟩+ |z1 = 1⟩|z2 = 0⟩

. The next
level, E1(s), begins at the antisymmetric state
1

√

√

2
|x1 = 0⟩|x2 = 1⟩−|x1 = 1⟩|x2 = 0⟩

and ends at

2
|z1 = 0⟩|z2 = 1⟩−|z1 = 1⟩|z2 = 0⟩

. Because eH(s) commutes with the
bit-exchange operation there can be no transitions from the symmetric to the antisymmetric states.
Therefore the E1(s) curve in Fig. 4 is irrelevant to the adiabatic evolution of the ground state and the
relevant gap is E2(s) −E0(s).
Closely related to 2-bit disagree is the “2-bit agree clause,” which has 00 and 11 as satisfying
assignments. We can obtain HP for this problem by taking HP for 2-bit disagree and acting with
the operator that takes |z1⟩|z2⟩→|

the antisymmetric state
1

√

z1⟩|z2⟩. Note that HB = H(1)
B
+ H(2)
B
is invariant under this
transformation as is the starting state |ψ(0)⟩given in (2.21). This implies that the levels of eH(s)
corresponding to 2-bit agree are the same as those for 2-bit disagree and that beginning with the
ground state of HB, adiabatic evolution brings you to
1

2
|z1 = 0⟩|z2 = 0⟩+ |z1 = 1⟩|z2 = 1⟩

.
Another two-bit example that we will use later is the clause “imply”. Here the satisfying assign-
ments are 00, 01, and 11. The relevant level diagram is shown in Fig. 5.

√

## Page 9

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
9

1

0.9

0.8

0.7

0.6

eigenvalues

0.5

0.4

0.3

0.2

0.1

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0

s

Figure 2: The two eigenvalues of eH(s) for a one-qubit example where HB and HP are diagonal in the
same basis. The levels cross so gmin = 0.

3.3
Three Qubits

Next we present a three-bit example that is built up from two-bit clauses so we have an instance of
2-SAT with three bits. We take the 2-bit imply clause acting on bits 1 and 2, the 2-bit disagree clause
acting on bits 1 and 3, and the 2-bit agree clause acting on bits 2 and 3. Although each two-bit clause
has more than one satisfying assignment, the full problem has the unique satisfying assignment 011.
The corresponding quantum Hamiltonian, eH(s) = (1 −s)HB + sHP, we write as the sum of
Hamiltonians each of which acts on two bits,

HP = H12
imply + H13
disagree + H23
agree

HB = (H(1)
B
+ H(2)
B ) + (H(1)
B
+ H(3)
B ) + (H(2)
B
+ H(3)
B ) .
(3.5)

The eigenvalues of eH(s) are shown in Fig. 6. We see that gmin is not zero. Starting in the ground state
of HB, and evolving according to (2.1) with H(t) = eH(t/T ) the system will end up in the ground state
of HP for T ≫1/g2
min. This example illustrates how our algorithm evolves to the unique satisfying
assignment of several overlapping clauses even when each separate clause has more than one satisfying
assignment.
The alert reader may have noticed that two of the levels in Fig. 6 cross. This can be understood
in terms of a symmetry. The Hamiltonian HP of (3.5) is invariant under the unitary transformation
V
|z1⟩|z2⟩|z3⟩

= |

z1⟩|z3⟩, as is HB. Now the three states with energy equal to 4 at s = 0 are
|x1 = 1⟩|x2 = 1⟩|x3 = 0⟩, |x1 = 0⟩|x2 = 1⟩|x3 = 1⟩, and |x1 = 1⟩|x2 = 0⟩|x3 = 1⟩. The transforma-
tion |z⟩→|

z2⟩|

z⟩in the |x⟩basis is |x⟩→(−1)x |x⟩, so the states

|x1 = 1⟩|x2 = 1⟩|x3 = 0⟩and |x1 = 0⟩|x2 = 1⟩|x3 = 1⟩−|x1 = 1⟩|x2 = 0⟩|x3 = 1⟩

are invariant under V , whereas

|x1 = 0⟩|x2 = 1⟩|x3 = 1⟩+ |x1 = 1⟩|x2 = 0⟩|x3 = 1⟩

## Page 10

10
Quantum Computation by Adiabatic Evolution

1

0.9

0.8

0.7

0.6

eigenvalues

0.5

0.4

0.3

0.2

0.1

0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
0

s

Figure 3: A small perturbation is added to the Hamiltonian associated with Fig. 2 and we see that
the levels no longer cross.

goes to minus itself. We call these two diﬀerent transformation properties “invariant” and “odd”.
Thus at s = 0 there are two invariant states and one odd state with energy 4. We see from Fig. 6
that one combination of these states ends up at energy 2 when s = 1. The energy-2 state at s = 1 is
|z1 = 0⟩|z2 = 1⟩|z3 = 0⟩, which is invariant so the level moving across from energy 4 to energy 2 is
invariant. This means that one of the two levels that start at energy 4 and end at energy 1 is invariant
and the other is odd. Since the Hilbert space can be decomposed into a direct sum of the invariant
and odd subspaces and accordingly H(t) is block diagonal, the invariant and odd states are decoupled,
and their crossing is not an unlikely occurrence.
Since, in this simple 3-bit example, we do see levels cross you may wonder if we should expect
to sometimes see the two lowest levels cross in more complicated examples. We now argue that we
do not expect this to happen and even if it does occur it will not eﬀect the evolution of the ground
state. First note that the transformation which is a symmetry of (3.5) is not a symmetry of the
individual terms in the sum. Thus it is unlikely that such symmetries will typically be present in more
complicated n-bit examples. However, it is inevitable that certain instances of problems will give
rise to Hamiltonians that are invariant under some transformation. Imagine that the transformation
consists of bit interchange and negation (in the z basis) as in the example just discussed. Then
the starting state |x = 0⟩given by (2.21) is invariant. Assume that HP has a unique ground state
|z1 = w1⟩|z2 = w2⟩· · · |zn = wn⟩. Since HP is invariant this state must transform into itself, up to a
phase. However, from the explicit form of the ground state we see that it transforms without a phase,
that is, it is invariant. Thus, following the evolution of the ground state we can restrict our attention
to invariant states. The gap that matters is the smallest energy diﬀerence between the two lowest
invariant states.

## Page 11

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
11

2

1.8

1.6

1.4

1.2

eigenvalues

1

0.8

0.6

0.4

0.2

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0

s

Figure 4: The four eigenvalues of eH(s) associated with “2-bit disagree”. The same levels are associated
with “2-bit agree”.

4
Examples with an Arbitrary Number of Bits

Here we discuss four examples of n-bit instances of satisﬁability. In three of the examples the problems
are classically computationally simple to solve. These problems also have structure that we exploit
to calculate gmin in the corresponding quantum version. In each case gmin goes like 1/np, so these
problems can be solved in polynomial time by adiabatic quantum evolution. The other example is the
“Grover problem” [2], which has a single (generalized) n-bit clause with a unique satisfying assignment.
If we assume that we treat the clause as an oracle, which may be queried but not analyzed, it takes 2n

classical queries to ﬁnd the satisfying assignment. Our quantum version has gmin of order 2−n/2, so the
time required for quantum adiabatic evolution scales like 2n, which means that there is no quantum
speedup. Nonetheless, it is instructive to see how it is possible to evaluate gmin for the Grover problem.

4.1
2-SAT on a Ring: Agree and Disagree

Consider an n-bit problem with n clauses, each of which acts only on adjacent bits, that is, clause Cj
acts on bits j and j + 1 where j runs from 1 to n and bit n + 1 is identiﬁed with bit 1. Furthermore
we restrict each clause to be either “agree”, which means that 00 and 11 are satisfying assignments or
“disagree”, which means that 01 and 10 are satisfying assignments. Suppose there are an even number
of disagree clauses so that a satisfying assignment on the ring exists. Clearly given the list of clauses
it is trivial to construct the satisfying assignment. Also, if w1, w2, . . . , wn is a satisfying assignment,
so is

wn, so there are always exactly two satisfying assignments.
The quantum version of the problem has

w1,

w2, . . . ,

HP = H12
C1 + H23
C2 + · · · + Hnn+1
Cn
(4.1)

where each Cj is either agree or disagree. The ground states of HP are |w1⟩|w2⟩· · · |wn⟩and |

w1⟩×

## Page 12

12
Quantum Computation by Adiabatic Evolution

2

1.8

1.6

1.4

1.2

eigenvalues

1

0.8

0.6

0.4

0.2

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0

s

Figure 5: The four eigenvalues of eH(s) associated with the 2-bit imply clause.

|

w2⟩· · · |

wn⟩all in the z basis. Deﬁne the unitary transformation

|z1⟩|z2⟩· · · |zn⟩→|z′
1⟩|z′
2⟩· · · |z′
n⟩

Under this transformation HP becomes

(
z′
j =

zj ,
if wj = 1

z′
j = zj ,
if wj = 0 .
(4.2)

HP = H12
agree + H23
agree + · · · + Hnn+1
agree
(4.3)

and the symmetric ground state of HP is

|z1 = 0⟩|z2 = 0⟩· · · |zn = 0⟩+ |z1 = 1⟩|z2 = 1⟩· · · |zn = 1⟩

.
(4.4)

|w⟩=
1

√

2

We take HB to be (2.22) with n bits and each di = 2. HB is invariant under the transformation just
given. This implies that the spectrum of eH(s) = (1−s)HB +sHP, with HP given by (4.1), is identical
to the spectrum of eH(s) with HP given by (4.3). Thus when we ﬁnd gmin using (4.3) we will have
found gmin for all of the n-bit agree-disagree problems initially described.
We can write eH(s) using (4.3) for HP as

n
X

n
X

eH(s) = (1 −s)

j=1
(1 −σ(j)
x ) + s

j=1

2(1 −σ(j)
z σ(j+1)
z
) .
(4.5)

1

We denote the s = 0 ground state given by (2.21) as |x = 0⟩. Deﬁne the operator G that negates the
value of each bit in the z basis, that is, G |z1⟩|z2⟩· · · |zn⟩= |

n
Y

G =

z1⟩|

z2⟩· · · |

zn⟩. This can be written as

j=1
σ(j)
x
.
(4.6)

## Page 13

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
13

6

5

4

eigenvalues

3

2

1

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0

s

Figure 6: The eight levels of eH(s) for the 3-bit problem with HP and HB given by (3.5).

Since G |x = 0⟩= |x = 0⟩and

G, eH(s)

= 0, we can restrict our attention to states that are invariant
under G such as (4.4).
We now write (4.5) in the invariant sector as a sum of n/2 commuting 2 × 2 Hamiltonians that we
can diagonalize. First we make a standard transformation to fermion operators. To this end we deﬁne
for j = 1, . . . , n,

bj = σ(1)
x σ(2)
x
· · · σ(j−1)
x
σ(j)
−1(j+1) · · · 1(n)

b†
j = σ(1)
x σ(2)
x
· · · σ(j−1)
x
σ(j)
+ 1(j+1) · · · 1(n)
(4.7)

where

1
−1
1
−1

σ−= 1

2

It is straightforward to verify that

{bj, bk} = 0

where {A, B} = AB + BA. Furthermore

b†
jbj = 1

for j = 1, . . . , n and


and
σ+ = 1

 1
1
−1
−1


.

2

{bj, b†
k} = δjk
(4.8)

2(1 −σ(j)
x )
(4.9)

(b†
j −bj)(b†
j+1 + bj+1) = σ(j)
z σ(j+1)
z
(4.10)

for j = 1, . . . , n−1. We need a bit more care to make sense of (4.10) for j = n. An explicit calculation
shows that

(b†
n −bn)(b†
1 + b1) = −Gσ(n)
z
σ(1)
z
(4.11)

## Page 14

14
Quantum Computation by Adiabatic Evolution

where G is given by (4.6). Since we will restrict ourselves to the G = 1 sector, (4.10) and (4.11) are
only consistent if bn+1 = −b1, so we take this as the deﬁnition of bn+1.
We can now reexpress eH(s) of (4.5) in terms of the b’s:

n
2(1 −s)b†
jbj + s

n
X

eH(s) =

j=1

2
1 −(b†
j −bj)(b†
j+1 + bj+1)
o
.
(4.12)

Because this is invariant under the translation, bj →bj+1, and is quadratic in the bj and b†
j, a
transformation to fermion operators associated with waves running round the ring will achieve the
desired reduction of eH(s). Let

n
X

βp =
1

j=1
eiπpj/nbj
for p = ±1, ±3, . . ., ±(n −1)
(4.13)

√

n

which is equivalent to

X

bj =
1

√

n

p=±1,±3,...,±(n−1)
e−iπpj/nβp
(4.14)

and is consistent with bn+1 = −b1. (We assume for simplicity that n is even.) Furthermore


βp, βq
= 0

and


βp, β†
q
= δpq
(4.15)

which follows from (4.8). Substituting (4.14) into (4.12) gives

eH(s) =
X

where

Ap(s) = 2(1 −s)

β†
pβp + β†
−pβ−p


+ s
n
1 −cos πp

p=1,3,...,(n−1)
Ap(s)
(4.16)

n

β†
−pβ†
p −βpβ−p
o
.
(4.17)

n

β†
pβp −β−pβ†
−p

+ i sin πp

The Ap’s commute for diﬀerent values of p so we can diagonalize each Ap separately.
For each p > 0 let |Ωp⟩be the state annihilated by both βp and β−p, that is, βp |Ωp⟩= β−p |Ωp⟩= 0.
When s = 0, |Ωp⟩is the ground state of Ap. Now Ap(s) only connects |Ωp⟩to |Σp⟩= β†
−pβ†
p |Ωp⟩. In
the |Ωp⟩, |Σp⟩basis Ap(s) is

"
s + s cos πp/n
is(sin πp/n)

Ap(s) =

#

.
(4.18)

−is(sin πp/n)
4 −3s −s cos πp/n

For each p the two eigenvalues of Ap(s) are

E±
p (s) = 2 −s ±

(2 −3s)2 + 4s(1 −s)(1 −cos πp/n)
1

2 .
(4.19)

## Page 15

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
15

The ground state energy of (4.16) is P

p
E−
p (s). The next highest energy level is E+
1 (s) + P

The minimum gap occurs very close to s = 2

3 and is

gmin ≈E+
1 ( 2

3) −E−
1 ( 2

p=3...
E−
p (s).

3) ≈4π

3n
(4.20)

for n large.
Referring back to (2.8) we see that the required evolution time T must be much greater than
E/g2
min where for this problem E scales like n so T ≫cn3 where c is a constant. We have shown that
for any set of agree and disagree clauses on an n-bit ring, quantum adiabatic evolution will ﬁnd the
satisfying assignment in a time which grows as a ﬁxed power of n.

4.2
The Grover Problem

Here we consider the Grover problem [2], which we recast for the present context. We have a sin-
gle (generalized) clause, hG, which depends on all n bits with a unique (but unknown) satisfying
assignment w = w1, w2, . . . , wn. Corresponding to hG is a problem Hamiltonian

HP |z⟩=
 |z⟩,
z ̸= w
0 ,
z = w

= 1 −|z = w⟩⟨z = w|
(4.21)

where we use the shorthand |z⟩= |z1⟩|z2⟩. . . , |zn⟩. We imagine that we can construct H(t) = eH(t/T )
of the form (2.23) with HB given by (2.22) with di = 1 for all i from 1 to n. Since we are evolving
using H(t) the problem is “oracular,” that is, we use no knowledge about the structure of HP which
could aid us in ﬁnding w other than (4.21).
We can write eH(s) explicitly as

n
X

2
1 −σ(j)
x

+ s
1 −|z = w⟩⟨z = w|

.
(4.22)

eH(s) = (1 −s)

1

j=1

Consider the transformation given by (4.2). Under this transformation eH(s) becomes

n
X

2(1 −σ(j)
x ) + s
1 −|z = 0⟩⟨z = 0|

.
(4.23)

eH(s) = (1 −s)

1

j=1

Because the two Hamiltonians (4.22) and (4.23) are unitarily equivalent they have the same spectra
and accordingly the same gmin. Thus it suﬃces to study (4.23).
The ground state of eH(0) is |x = 0⟩, which is symmetric under the interchange of any two bits.
Also the operator (4.23) is symmetric under the interchange of any two bits. Instead of working in the
2n-dimensional space we can work in the (n + 1)-dimensional subspace of symmetrized states. It is
convenient (and perhaps more familiar to physicists) to deﬁne these states in terms of the total spin.
Deﬁne ⃗S = (Sx, Sy, Sz) by

n
X

Sa = 1

2

for a = x, y, z. The symmetrical states have ⃗S 2 equal to n

j=1
σ(j)
a
(4.24)

2 + 1), where ⃗S 2 = S2
x + S2
y + S2
z. We can
characterize these states as either eigenstates of Sx or Sz

2 ( n

Sx |mx = m⟩= m |mx = m⟩
m = −n

2 , −n

2 + 1, . . . , n

2
Sz |mz = m⟩= m |mz = m⟩
m = −n

2 , −n

2 + 1, . . . , n

2
(4.25)

## Page 16

16
Quantum Computation by Adiabatic Evolution

where we have suppressed the total spin label since it never changes. In terms of the z basis states
previously introduced,

2 −k
=
n
k

−1

2
X

mz = n

for k = 0, 1, . . . , n. In particular
mz = n

Now we can write eH(s) in (4.23) as

z1+z2+···+zn=k
|z1⟩|z2⟩· · · |zn⟩
(4.26)

2
= |z = 0⟩.
(4.27)

2 −Sx

+ s

1 −
mz = n

eH(s) = (1 −s)
 n

2

.
(4.28)

2
mz = n

We have reduced the problem, since eH(s) is now an (n + 1)-dimensional matrix whose elements we
can simply evaluate.
We wish to solve

eH(s) |ψ⟩= E |ψ⟩
(4.29)

for the lowest two eigenvalues at the value of s at which they are closest. Hitting (4.29) with
mx = n

2 −r
we get

2 −r
ψ
−s
mx = n

[s + (1 −s)r]
mx = n

= E
mx = n

2 −r
mz = n

2
ψ

2
mz = n

2 −r
ψ
.
(4.30)

We replace E by the variable λ where E = s + (1 −s)λ and obtain

2 −r
ψ
E
=
1

D
mx = n

D
mx = n

(1 −s)

s

r −λ

2
mx = n

Multiply by
mz = n

2 −r
and sum over r to get

n
X

(1 −s)

1

s
=

r=0

where

Pr =
D
mz = n

mx = n

2

2 −r
mz = n

ψ
E
.
(4.31)

E D
mz = n

2

2

r −λPr
(4.32)

2 −r
E
2
.
(4.33)

Using (4.26) with k = 0 and also the identical formula with z replaced by x we have

 n
r

Pr = 1

2n


.
(4.34)

The eigenvalue equation (4.32) has n + 1 roots. By graphing the right-hand side of (4.32) and
keeping 0 < s < 1 we see that there is one root for λ < 0, one root between 0 and 1, one root between
1 and 2, . . . , and one root between n −1 and n. The two lowest eigenvalues of E = s + (1 −s)λ
correspond to the root with λ < 0 and the root with 0 < λ < 1. We will now show that there is a
value of s for which these two roots are both very close to zero.

## Page 17

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
17

The left-hand side of (4.32) ranges over all positive values as s varies from 0 to 1. Pick s = s∗such
that

n
X

(1 −s∗)

Pr

s∗
=

r=1

At s = s∗the eigenvalue equation (4.32) becomes

n
X

P0

r=1
Pr
λ

λ =

r .
(4.35)

r(r −λ) .
(4.36)

From (4.34) we know that P0 = 2−n. Deﬁne u by λ = 2−n/2u. Then (4.36) becomes

n
X

1

r=1
Pr
u

u =

r(r −2−n/2u) .
(4.37)

Because of the 2−n/2 we can neglect the u piece in the denominator and we get

n
X

1

Pr

u2 ≈

r=1

which gives

λ ≈±

n
X

−1

Pr

r2

r=1

and we have

gmin ≈2(1 −s∗)

n
X

Pr

r2

r=1

Now

n + O
 1

n
X

Pr

r = 2

r=1

and

n2 + O
 1

n
X

Pr

r2 = 4

n3

r=1

So using (4.35) and (4.40) we have

gmin ≃2 · 2−n

r2
(4.38)

2 2−n/2
(4.39)

−1

2 2−n/2 .
(4.40)


(4.41)

n2


.
(4.42)

2
(4.43)

which is exponentially small.
In Fig. 7 we show the two lowest eigenvalues of eH(s) for the case of 12 bits. If you evolve too
quickly the system jumps across the gap and you do not end up in the ground state of eH(1).
That gmin goes like 2−n/2 means that the required time for ﬁnding the satisfying assignment grows
like 2n and quantum adiabatic evolution is doing no better than the classical algorithm which checks
all 2n variable assignments. In reference [3] a Hamiltonian version of the Grover problem was studied
with a time dependent Hamiltonian of the form

H(t) = HD(t) + (1 −|z = w⟩⟨z = w|) .
(4.44)

## Page 18

18
Quantum Computation by Adiabatic Evolution

1.2

1

0.8

eigenvalues

0.6

0.4

0.2

0

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
–0.2

s

Figure 7: The two lowest eigenvalues of eH(s) for the Grover problem with 12 bits.

The goal was to choose HD(t) without knowing w so that Schr¨odinger evolution from a w-independent
initial state would bring the system to |z = w⟩in time T . There it was shown how to choose HD so
that the required running time T grows as 2
n

2 , which is then interpreted as the square-root speedup
found by Grover. It was also shown that for any HD(t), T must be at least of order 2
n

2 for the quantum
evolution to succeed for all w. (The continuous time bound found in [3] is closely related to the query
bound found ﬁrst in [4].) A slight modiﬁcation of the argument which gives this lower bound can be
made for quantum evolution with

H(t) = HD(t) + t

T (1 −|z = w⟩⟨z = w|)
(4.45)

and again T must be at least of order 2
n

2 . The adiabatic evolution we studied in this section corresponds
to HD(t) = (1 −t/T )HB with HB as described above. The lower bound just discussed shows that no
choice of HB can achieve better than square-root speedup.

4.3
The Bush of Implications

Ultimately we would like to know if there are general (and identiﬁable) features of problems which
can tell us about the size of gmin. For the 2-SAT example of Section 4.1, gmin is of order 1/n whereas
for the Grover problem it is of order 2−n/2. In the Grover case HP has the property that 2n −1 states
have energy 1, that is, there are an exponential number of states just above the ground state. For
the ring problem this is not so. With HP of the form (4.3) there are no states with energy 1 and
(roughly) n2 states with energy 2. Here we present an example with an exponential number of states
with energy 1 but for which the gap is of order 1/np. This tells us that we cannot judge the size of
the minimum gap just from knowledge of the degeneracy of the ﬁrst level above the ground state of
HP.
The example we consider has n + 1 bits labeled 0, 1, 2 . . ., n. There are n 2-bit imply clauses, each
of which involves bit 0 and one of the other n bits. Recall that the imply clause is satisﬁed by the bit

## Page 19

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
19

values 00, 01 and 11 but not by 10. Furthermore we have a one-bit clause that is satisﬁed only if bit
0 has the value 1. The unique satisfying assignment of all clauses is z0 = 1, z1 = 1, z2 = 1, . . . , zn = 1.

Figure 8: The bush of implications. There is a one-bit clause that is satisﬁed if bit 0 has a value of 1.
There are n imply clauses. The jth imply clause is satisﬁed unless bit 0 has the value 1 and bit j has
the value 0.

Suppose that z0 = 0. Any of the 2n values of z1, z2, . . . , zn satisfy all of the imply clauses. Only
the one bit clause is not satisﬁed, so these 2n variable assignments violate only one clause. There
are n other variable assignments that violate only one clause. These have all bits set to 1 except for
the kth bit where 1 ≤k ≤n. In total there are 2n + n assignments that violate only one clause and
accordingly there are an exponential number of states with energy 1.
We can write HP explicitly as

n
X

2(1 + σ(0)
z ) + 1

HP = 1

4

j=1
(1 −σ(0)
z )(1 + σ(j)
z ) .
(4.46)

To evaluate HB from (2.22) note that bit 0 is involved in n + 1 clauses whereas bits 1 through n are
each involved in only one clause, so

n
X

2(1 −σ(0)
x ) +

HB = (n + 1) 1

i=1

Then eH(s) in terms of the spin operators (4.24) is

eH(s) = (1 −s)
hn + 1

2 −Sx
i
+ s
h
1

2
(1 −σ(0)
x ) + n

2(1 −σ(i)
x ) .
(4.47)

1

2(1 −σ(0)
z )
n

2 + Sz
i
.
(4.48)

2(1 + σ(0)
z ) + 1

We need only consider states that are symmetrized in the bits 1 to n. We can label the relevant states
as |z0⟩|mz⟩where z0 gives the value of bit 0 and mz labels the z component of the total spin as in
(4.25). We need to know the matrix elements of Sx in the |mz⟩basis. These are

2
hn

n

⟨m′
z | Sx | mz⟩= 1

2

+
n

n

2

2 + 1

−m2
z −mz
 1

2 δmz,m′z−1

2 + 1

−m′2
z −m′
z
 1

2 δm′
z,mz−1
i
.
(4.49)

Given (4.49) we have numerically evaluated the eigenvalues of the 2(n + 1)-dimensional matrix
with elements
⟨z′
0| ⟨m′
z|
 eH(s)
|z0⟩|mz⟩

(4.50)

for values of n in the range from 20 to 120. The two lowest eigenvalues are shown in Fig. 9 for n = 50.
The gap is clearly visible. In Fig. 10 we plot log(gmin) versus log(n) and a power law dependence is

## Page 20

20
Quantum Computation by Adiabatic Evolution

6

5

4

eigenvalues

3

2

1

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0

s

Figure 9: The two lowest eigenvalues of eH(s) for the bush of implications with n = 50. The visible
gap indicates that gmin is not exponentially small.

clearly visible. We conclude that gmin ∼n−p with p ≃3

8. For this problem the maximum eigenvalue
of HB is 2n + 1 and the maximum eigenvalue of HP is n + 1, so E, which appears in (2.8), at most
grows linearly with n. Therefore we have that with T of order n(1+2p) adiabatic evolution is assured.
We also analyzed adiabatic evolution for the bush of implications using a diﬀerent prescription for
the initial Hamiltonian. We tried

n
X

H′
B =

i=1
H(i)
B
(4.51)

as opposed to (2.22). This has the eﬀect of replacing the factor of (n+1) in (4.47) with a 1. The eﬀect
on gmin is dramatic. It now appears to be exponentially small as a function of n. This means that
with the choice of H′
B above, quantum adiabatic evolution fails to solve the bush of implications in
polynomial time. This sensitivity to the distinction between HB and H′
B presumably arises because
bit 0 is involved in (n + 1) clauses. This suggests to us that if we restrict attention to problems where
no bit is involved in more than, say, 3 clauses, there will be no such dramatic diﬀerence between using
HB or H′
B.

4.4
Overconstrained 2-SAT

In this section we present another 2-SAT problem consisting entirely of agree and disagree clauses.
This time every pair of bits is involved in a clause. We suppose the clauses are consistent, so there
are exactly 2 satisfying assignments, as in Section 4.1. In an n-bit instance of this problem, there are
n
2

clauses, and obviously the collection of clauses is highly redundant in determining the satisfying
assignments. We chose this example to explore whether this redundancy could lead to an extremely
small gmin. In fact, we will give numerical evidence that gmin goes like 1/np for this problem, whose
symmetry simpliﬁes the analysis.

## Page 21

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
21

-1.3

-1.4

-1.5

-1.6

log(gmin)

-1.7

-1.8

-1.9

-2

3
3.2
3.4
3.6
3.8
4
4.2
4.4
4.6
4.8
5
-2.1

log(n)

Figure 10: The bush of implications; log(gmin) versus log(n) with n ranging from 20 to 120. The
straight line indicates that gmin ∼n−p.

As with the problem discussed in Section 4.1, at the quantum level we can restrict our attention
to the case of all agree clauses, and we have

HP =
X

j<k
Hjk
agree .
(4.52)

Each bit participates in (n −1) clauses, so when constructing HB using (2.22) we take di = n −1 for
all i. We can write eH(s) explicitly for this problem

n
X

eH(s) = (1 −s)(n −1)

1

j=1

which in terms of the total spin operators Sx and Sz is

eH(s) = (1 −s)(n −1)
hn

2(1 −σ(j)
x ) + s
X

2(1 −σ(j)
z σ(k)
z )
(4.53)

1

j<k

2 −Sx
i
+ s
hn2

4 −SzSz
i
.
(4.54)

As in Section 4.3, it is enough to consider the symmetric states |mz⟩. Using (4.49), we can ﬁnd the
matrix elements

⟨m′
z| eH(s) |mz⟩
(4.55)

and numerically ﬁnd the eigenvalues of this (n + 1) × (n + 1)-dimensional matrix.
Actually there are two ground states of eH(1),
mz = n

2
and
mz = −n

2
, corresponding to all
bits having the value 0 or all bits having the value 1. The Hamiltonian eH(s) is invariant under the
operation of negating all bits (in the z basis) as is the initial state given by (2.21). Therefore we can
restrict our attention to invariant states. In Fig. 11 we show the two lowest invariant states for 33 bits.
The gap is clearly visible. (E1(0) = 64 = 2(33 −1) because the invariant states all have an even

## Page 22

22
Quantum Computation by Adiabatic Evolution

160

140

120

100

eigenvalues

80

60

40

20

0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
0

s

Figure 11: The two lowest eigenvalues of eH(s), restricted to the invariant subspace, for overconstrained
2-SAT with n = 33. The visible gap indicates that gmin is not exponentially small.

number of 1’s in the x-basis.) In Fig. 12 we plot log(gmin) against log(n). The straight line shows that
gmin ∼np with p ≃0.7. For this problem the maximum eigenvalues of HB and HP are both of order
n2 so E appearing in (2.8) is no larger than n2. Adiabatic evolution with T only as big as n(2−2p) will
succeed in ﬁnding the satisfying assignment for this set of problems.

5
The Conventional Quantum Computing Paradigm

The algorithm described in this paper envisages continuous-time evolution of a quantum system, gov-
erned by a smoothly-varying time-dependent Hamiltonian. Without further development of quantum
computing hardware, it is not clear whether this is more or less realistic than conventional quantum
algorithms, which are described as sequences of unitary operators each acting on a small number of
qubits. In any case, our algorithm can be recast within the conventional quantum computing paradigm
using the technique introduced by Lloyd [5].
The Schr¨odinger equation (2.1) can be rewritten for the unitary time evolution operator U(t, t0),

i d

dtU(t, t0) = H(t)U(t, t0)
(5.1)

and then

|ψ(T )⟩= U(T, 0) |ψ(0)⟩.
(5.2)

To bring our algorithm within the conventional quantum computing paradigm we need to approximate
U(T, 0) by a product of few-qubit unitary operators. We do this by ﬁrst discretizing the interval [0, T ]
and then applying the Trotter formula at each discrete time.
The unitary operator U(T, 0) can be written as a product of M factors

U(T, 0) = U(T, T −∆)U(T −∆, T −2∆) · · · U(∆, 0)
(5.3)

## Page 23

E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser
23

3.6

3.4

3.2

3

2.8

log(gmin)

2.6

2.4

2.2

2

1.8

3
3.5
4
4.5
5
5.5
1.6

log(n)

Figure 12: Overconstrained 2-SAT; log(gmin) versus log(n) with n ranging from 33 to 203. The straight
line indicates that gmin ∼np.

where ∆= T/M. We use the approximation

U((ℓ+ 1)∆, ℓ∆) ≃e−i∆H(ℓ∆)
(5.4)

which is valid in (5.3) if

∆H(t1) −∆H(t2)
≪1

M
for all
t1, t2 ∈[ℓ∆, (ℓ+ 1)∆] .
(5.5)

Using (2.23) this becomes

∆
HP −HB
≪1 .
(5.6)

We previously showed (in the paragraph after Eq. (2.29)) that ∥HP −HB∥grows no faster than the
number of clauses, which we always take to be at most polynomial in n. Thus we conclude that the
number of factors M = T/∆must be of order T times a polynomial in n.
Each of the M terms in (5.3) we approximate as in (5.4). Now H(ℓ∆) = uHB + vHP where
u = 1 −(ℓ∆/T ) and v = ℓ∆/T are numerical coeﬃcients each of which is between 0 and 1. To use
the Trotter formula

e−i∆H(ℓ∆) ≃(e−i∆uHB/Ke−i∆vHP/K)K
(5.7)

for each ℓ, ℓ= 0, 1, . . . , M −1, we need K ≫M
1 + ∆∥HB∥+ ∆∥HP∥
2. Since ∥HB∥and ∥HP∥are
at most a small multiple of the number of clauses, we see that K need not be larger than M times a
polynomial in n.
Now (5.7) is a product of 2K terms each of which is e−i∆uHB/K or e−i∆vHP/K. From (2.22) we see
that HB is a sum of n commuting one-bit operators. Therefore e−i∆uHB/K can be written (exactly)
as a product of n one-qubit unitary operators. The operator HP is a sum of commuting operators,

## Page 24

24
Quantum Computation by Adiabatic Evolution

one for each clause. Therefore e−i∆vHP/K can be written (exactly) as a product of unitary operators,
one for each clause acting only on the qubits involved in the clause.
All together U(T, 0) can be well approximated as a product of unitary operators each of which
acts on a few qubits. The number of factors in the product is proportional to T 2 times a polynomial
in n. Thus if the required T for adiabatic evolution is polynomial in n, so is the number of few-qubit
unitary operators in the associated conventional quantum computing version of the algorithm.

6
Outlook

We have presented a continuous-time quantum algorithm for solving satisﬁability problems, though
we are unable to determine, in general, the required running time. The Hamiltonian that governs the
system’s evolution is constructed directly from the clauses of the formula. Each clause corresponds
to a single term in the operator sum that is H(t). We have given several examples of special cases
of the satisﬁability problem where our algorithm runs in polynomial time. Even though these cases
are easily seen to be classically solvable in polynomial time, our algorithm operates in an entirely
diﬀerent way from the classical one, and these examples may provide a small bit of evidence that our
algorithm may run quickly on other, more interesting cases.

References

[1] A. Messiah, Quantum Mechanics, Vol. II, Amsterdam: North Holland; New York: Wiley (1976).

[2] L.K. Grover, “A Fast Quantum Mechanical Algorithm for Database Search”, quant-ph/9605043;
Phys. Rev. Lett. 78, 325 (1997).

[3] E. Farhi, S. Gutmann, “An Analog Analogue of a Digital Quantum Computation”, quant-
ph/9612026; Phys. Rev. A 57, 2403 (1998).

[4] C.H. Bennett, E. Bernstein, G. Brassard and U.V. Vazirani, “Strengths and Weaknesses of
Quantum Computing”, quant-ph/9701001.

[5] S. Lloyd, “Universal Quantum Simulators”, Science 273, 1073 (1996).
