---
source_pdf: ../arxiv_1711.04789.pdf
pages: 8
extracted_at: 2026-04-17T12:32:32+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_1711.04789

Source PDF: ../arxiv_1711.04789.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Quantum Simulation of Electronic Structure with Linear Depth and Connectivity

Ian D. Kivlichan,1, 2 Jarrod McClean,1 Nathan Wiebe,3 Craig Gidney,4

Al´an Aspuru-Guzik,2 Garnet Kin-Lic Chan,5, ∗and Ryan Babbush1, †

1Google Inc., Venice, CA 90291
2Department of Chemistry and Chemical Biology, Harvard University, Cambridge, MA 02138
3Microsoft Research, Redmond, WA 98052
4Google Inc., Santa Barbara, CA 93117
5Division of Chemistry and Chemical Engineering,
California Institute of Technology, Pasadena, CA 91125
(Dated: February 6, 2018)

As physical implementations of quantum architectures emerge, it is increasingly important to
consider the cost of algorithms for practical connectivities between qubits. We show that by using an
arrangement of gates that we term the fermionic swap network, we can simulate a Trotter step of the
electronic structure Hamiltonian in exactly N depth and with N 2/2 two-qubit entangling gates, and
prepare arbitrary Slater determinants in at most N/2 depth, all assuming only a minimal, linearly
connected architecture.
We conjecture that no explicit Trotter step of the electronic structure
Hamiltonian is possible with fewer entangling gates, even with arbitrary connectivities.
These
results represent signiﬁcant practical improvements on the cost of most Trotter based algorithms
for both variational and phase estimation based simulation of quantum chemistry.

arXiv:1711.04789v2 [quant-ph] 3 Feb 2018

The electronic structure Hamiltonian describes the
properties of interacting electrons in the presence of sta-
tionary nuclei. The physics of such systems determine
the rates of chemical reactions, molecular structure, as
well as the properties of most materials.
Toward this
goal, multiple approaches to quantum simulating elec-
tronic structure have been explored (see e.g. [1–28]), with
some even demonstrated experimentally [29–39].
Most past work has focused on using Gaussian basis
functions in second quantization, for which the Hamil-
tonian contains O(N 4) terms, where N is the number
of spin-orbitals.
However, a recent paper showed that
careful selection of basis functions yields a Hamiltonian
with O(N 2) terms [40].
While certain bases meeting
these conditions are nearly ideal for periodic systems,
for single molecules they incur a constant overhead com-
pared to Gaussian bases. In this Letter, we introduce
two simulation advances inspired by these recently devel-
oped Hamiltonian representations that lower the barrier
to practical quantum simulation of chemical systems on
emerging hardware platforms.
Our ﬁrst result is a new implementation of the Trot-
ter step, which uses an optimal swap network combined
with fermionic swap gates in order to avoid the fermionic
fast Fourier transform (FFFT), which is costly to im-
plement with restricted qubit connectivity. Our circuit
involves exactly
N
2

entangling operations for the
N
2


orbital interactions and is perfectly parallelized to a cir-
cuit depth of N. We conjecture that the gate complexity
of this Trotter step cannot be improved even with arbi-
trary connectivity.
Our technique can also be used to
simulate Trotter steps of the Hubbard model in O(
√

N)
depth, even when restricted to linear qubit connectivity.

∗Corresponding author: gkc1000@gmail.com
† Corresponding author: ryanbabbush@gmail.com

Our second result is a new method to prepare arbi-
trary Slater determinants in gate depth of at most N/2
on a linear architecture.
This is crucial for preparing
initial states in nearly all approaches to quantum simu-
lation, including both variational and phase estimation
based algorithms. Our work starts from a known strat-
egy based on the QR decomposition [41], but organizes
the rotations in such a way as to allow the algorithm to
run with linear connectivity by using parallelization and
elimination of redundant rotations based on symmetry
considerations to achieve gate depth of at most N/2.
Both algorithms improve asymptotically over all prior
implementations specialized to restricted connectivity ar-
chitectures, and additionally give signiﬁcant constant
factor improvements over the best prior algorithms de-
scribed with arbitrary connectivity. Such improvements
are crucial when planning simulations with limited hard-
ware resources; thus, we expect these strategies will be
useful primitives in near-term experiments. The combi-
nation of these two steps enables an extremely low depth
implementation of the variational ansatz based on Trot-
terized adiabatic state preparation [40, 42] (equivalent to
the quantum approximate optimization algorithm when
the target Hamiltonian is diagonal [43]). Since our Trot-
ter steps appear optimal even for arbitrary connectiv-
ities, we expect these results will also prove useful for
error-corrected quantum simulations.

Linear Trotter Steps by Fermionic Swap Network

We consider the general problem of simulating any
fermionic Hamiltonian of the form

H =
X

pq
Tpqa†
paq +
X

p
Upnp +
X

p̸=q
Vpqnpnq,
(1)

## Page 2

where a†
p and ap are fermionic creation and annihilation
operators and np = a†
pap is the number operator. Map-
ping to qubits under the Jordan-Wigner transformation
[44], Eq. (1) becomes (up to constant factors)

Tpp + Up

!

Vpq

Vpq

H =
X

4 ZpZq −
X

2
+
X

Zp (2)

2

p

q

p̸=q

Tpq

+
X

2 (XpZp+1 · · · Zq−1Xq + YpZp+1 · · · Zq−1Yq) .

p̸=q

This includes a range of Hamiltonians, such as the Hub-
bard model, ﬁnite diﬀerence discretization of quantum
chemistry, and the dual basis encoding described in [40].
Recent work has shown that single Trotter steps can
be implemented for a special case of this Hamiltonian in
O(N) depth on a quantum computer with planar nearest-
neighbor connectivity [40]. The approach of that work
involves (i) applying the FFFT in order to switch be-
tween the plane wave basis (where the a†
paq are diago-
nal single-qubit operators) and the dual basis (where the
npnq are diagonal two-qubit operators) and (ii) apply-
ing a linear depth swap network which places all qubits
adjacent at least once so that the npnq terms can be
simulated. That swap network requires 2N depth with
planar connectivity. We will show a new swap network
of N depth with linear connectivity which accomplishes
the same result. More importantly, we will show that
if one uses fermionic swaps gates instead of qubit swap
gates, this swap network will actually enable local sim-
ulation of all Hamiltonian terms (the a†
paq terms as well
as the npnq terms), still in depth N with linear connec-
tivity.
This represents a major improvement over the
technique of [40] which requires two costly applications
of the fermionic fast Fourier transform per dimension in
each Trotter step in order to simulate the a†
paq terms.
Additionally, the procedure here is more general since it
works for any Hamiltonian of the form of Eq. (1).
Fermionic swap gates originated in literature explor-
ing tensor networks for classical simulation of fermionic
systems (see e.g. [45]). They can be expressed indepen-
dently of the qubit mapping as

f p,q
swap = 1 + a†
paq + a†
qap −a†
pap −a†
qaq
(3)

f p,q
swapa†
p
f p,q
swap
† = a†
q
f p,q
swapap
f p,q
swap
† = aq.
(4)

Thus, the fermionic swap exchanges orbitals p and q
while maintaining proper anti-symmetrization. The im-
portance of exchanging orbitals is related to the qubit
representation of the fermionic operators, which under
the Jordan-Wigner transformation depends on an order-
ing of the orbitals called the canonical ordering [2, 44].
While interaction terms npnq are 2-local qubit operators
under the Jordan-Wigner transform, hopping terms a†
paq
are k-local qubit operators where k = |p −q| + 1. Thus,
under the Jordan-Wigner transform, the fermionic swap
gate between orbitals p and p + 1 is a 2-local qubit oper-
ator. By applying |p −q| −1 such neighboring fermionic

swap gates, one can thus bring any two qubits p and q
next to each other in the canonical ordering. In our algo-
rithm we will only apply the fermionic swap to neighbor-
ing orbitals in the Jordan-Wigner representation; thus,
we drop superscripts henceforth and use the notation
fswap = Jordan-Wigner[f p,p+1
swap ].
The key idea for our algorithm is to construct a near-
est neighbor fermionic swap network that is interleaved
with gates that simulate the evolution of the Hamilto-
nian terms within a Trotter-Suzuki decomposition. We
construct a fermionic swap network in which each or-
bital is adjacent in the canonical ordering exactly once.
Then, in the layer where orbitals p and q are adjacent
in the canonical ordering, evolution with the operators
a†
paq + a†
qap and npnq can be applied using only 2-local
nearest neighbor entangling gates. The entire network
can be implemented with exactly N layers of swaps.

1
2
3
4
5
Qubit

FIG. 1. A depiction of how the canonical Jordan-Wigner or-
dering changes throughout ﬁve layers of fermionic swap gates.
Each circle represents a qubit in a linear array (qubits do not
move) and ϕp labels which spin-orbital occupancy is encoded
by the qubit during a particular gate layer. The lines in be-
tween qubits indicate fermionic swap gates which change the
canonical ordering so that the spin-orbitals are represented
by diﬀerent qubits in the subsequent layer. After N layers,
the canonical ordering is reversed, and each spin-orbital has
been adjacent to all others exactly once.

The swap network is composed of alternating layers
of fermionic swaps which reverse the ordering of or-
bitals as an odd-even transposition sort (parallel bubble
sort) run on the reversed list of spin-orbital indices N.
The ﬁrst of these two layers consists of fermionic swap
gates between the odd-numbered qubits and the even-
numbered qubits to their right (qubits 2j + 1 and 2j + 2
for j ∈[0, ⌊(N −2)/2⌋]). If N is odd, the last qubit is un-
touched in this layer, because there is no even-numbered
qubit to its right. The second of these layers applies a
fermionic swap between the even qubits and the odd-
numbered qubit to their right (qubits 2j + 2 and 2j + 3,
again for j ∈[0, ⌊(N −2)/2⌋]).
In this second layer,

## Page 3

the ﬁrst qubit is always left untouched (there is no even
qubit on its left); if N is even the last qubit is untouched.
Alternating between these layers N times reverses the
canonical ordering, thus swapping each spin-orbital with
every other spin-orbital exactly once. All layers of this
procedure are illustrated for N = 5 in Figure 1.
Suppose that in a particular layer of the swap network,
orbital p (encoded by qubit ip) undergoes a fermionic
swap with orbital q (encoded by qubit iq = ip+1). Then,
evolution for time t under the fermionic operator Vpqnpnq
and the fermionic operators Tpq(a†
paq + a†
qap) can be
performed while simultaneously applying the fermionic
swap. This composite two-qubit gate which we refer to
as the “fermionic simulation gate” can be expressed as

Ft (ip, iq) = e−iVpqnpnqte−iTpq(a†
paq+a†
qap)tf p,q
swap
(5)

1
0
0
0
0 −i sin(Tpqt)
cos(Tpqt)
0
0
cos(Tpqt)
−i sin(Tpqt)
0
0
0
0
−e−iVpqt





=



(6)




where the second line holds whenever we use the Jordan-
Wigner transform and q = p + 1. This will always be
the case for us due to the reordering of orbitals in our
algorithm from the fermionic swap network.
Thus, Figure 1 depicts an entire ﬁrst-order (asymmet-
ric) Trotter step if the lines between qubits are inter-
preted as the gate Ft(ip, iq). A second-order (symmetric)
Trotter step of time 2t can be performed by doubling the
strength of the ﬁnal interaction in the ﬁrst-order step, not
performing the corresponding fermionic swap, and then
applying all other operations again in reverse order. The
network can be extended similarly to higher-order Trot-
ter formulae.
Like any two qubit operation, Ft (ip, iq)
can be implemented with a sequence of at most three
entangling gates from any standard library (e.g. CNOT
or CZ) with single-qubit rotations. Finally, the external
potential Upnp can be simulated by applying single-qubit
rotations in a single layer. Interestingly, while charges
of the nuclei are all that contribute the external poten-
tial (thus, distinguishing various molecules and materials
from jellium), these charges enter only through this layer
of single-qubit rotations, adding no additional complex-
ity to the quantum circuit for a single Trotter step.
We have shown that exactly
N
2

two-qubit gates (i.e.
fermionic simulation gates Ft(ip, iq)) are suﬃcient to im-
plement a single Trotter step in gate depth N.
For
Tpq = 0, a Trotter step under Eq. (1) is equivalent to
a network of arbitrary CPhase gates between all pairs of
qubits. Since such CPhase networks seem unlikely to sim-
plify, we conjecture that one cannot decompose Trotter
steps of Eq. (1) into fewer than
N
2

two-qubit gates (as-
suming no structure in the coeﬃcients). As our gates are
fully parallelized, assumption of this conjecture also im-
plies that no algorithm can achieve lower depth for these
Trotter steps without additional spatial complexity.
Finally, in Appendix A, we show that the fermionic
swap network can be applied to simulate Trotter steps

of the Hubbard model on a linear array with O(
√

N)
depth. This is an asymptotic improvement in time over
all prior approaches to simulate the Hubbard model on a
linear array and represents an improvement in space over
methods specialized to a planar lattice [46].

Linear Preparation of Slater Determinants with
Parallel Givens Rotations

All schemes for quantum simulation of electronic struc-
ture require that one initialize the system register in some
state that has reasonable overlap with an eigenstate of in-
terest (e.g. the ground state). Usually, the initial state
is a single Slater determinant such as the Hartree-Fock
state. This is a trivially preparable computational ba-
sis state if the simulation is performed in the basis of
Hartree-Fock molecular orbitals. However, as argued in
the literature, there is a trade-oﬀbetween the number of
terms in a Hamiltonian representation and the compact-
ness of the Hartree-Fock state [40]. Rather than change
the basis of the Hamiltonian, which could asymptotically
reduce its sparsity, one can use a quantum circuit to ro-
tate the state into the desired basis. Eﬃcient circuits of
this kind have previously been considered [2, 44]; e.g.,
[41] describes a procedure for preparing arbitrary Slater
determinants with N 2 gates using arbitrary connectivity
and [40] proposes to use the FFFT to prepare a plane-
wave state with O(N) depth using planar connectivity.
We present here an arbitrary-basis Slater determinant
preparation protocol which executes in N/2 depth for
systems with linear connectivity.
Our scheme is a variant of the QR decomposition based
method of constructing single-particle unitaries described
in other work [41, 47, 48]. Any particle-conserving rota-
tion of the single-particle basis can be expressed as

eϕp =
X

q
ϕqupq
˜a†
p =
X

q
a†
qupq
˜ap =
X

q
aqu∗
pq
(7)

where eϕp, ˜a†
p, and ˜a†
p correspond to spin-orbitals and op-
erators in the rotated basis and u is an N×N unitary ma-
trix. From the Thouless theorem [49], this single-particle
rotation is equivalent to applying the 2N × 2N operator

X

pq
[log u]pq
a†
paq −a†
qap

!

U(u) = exp

(8)

where [log u]pq is the (p, q) element of the matrix log u.
To eﬃciently implement U(u) without the overhead of
Trotterization, we will decompose it into a sequence of
exactly
N
2

rotations of the form

Rpq (θ) = exp

θpq
a†
paq −a†
qap

.
(9)

In Appendix B we show that

Rpq (θ) U (u) = U (rpq (θ) u)
(10)

## Page 4

∗∗
∗
∗
∗
∗
∗
∗
∗
8 ∗
∗
∗
∗
∗
∗
∗
∗
7 9
∗
∗
∗
∗
∗
∗
∗
6 8 10
∗
∗
∗
∗
∗
∗
5 7
9
11
∗
∗
∗
∗
∗
4 6
8
10 12
∗
∗
∗
∗
3 5
7
9
11 13
∗
∗
∗
2 4
6
8
10 12 14
∗
∗
1 3
5
7
9
11 13 15 ∗































FIG. 2.
The numbers above indicate the order in which
matrix elements should be eliminated using nearest-neighbor
Givens rotations. We see that two elements must be elimi-
nated before any parallelization can begin. Each element is
eliminated via rotation with the row directly above it. We
place asterisks (*) on the upper-diagonal to emphasize that
one only needs to focus on removing the lower-diagonal ele-
ments; since the initial matrix and rotations are both unitary,
the upper-diagonals will be eliminated simultaneously.

where rpq(θ) corresponds to a Givens rotation by angle
θ between rows p and q of u.
The QR decomposition strategy for decomposing U(u)
into a sequence of Rpq(θ) rotations is based on ﬁnding
a series of rpq(θ) rotations which diagonalize u.
This
elucidates the inverses of u and U(u) up to some phases:
Y

N
X

!

p=1
eiφp |p⟩⟨p|
(11)

k
rk (θk)

u =

N
Y

Y

!

p=1
eiφpnp
(12)

k
Rk (θk)

U (u) =

where the index k represents a particular pair of orbitals
p, q involved in the rotation at iteration k and eiφp is
a unit phase. Given this sequence of rotations and the
phases φp, we may implement U by applying Q
p e−iφpnp

(a single layer of gates) and then reversing the sequence of
rotations. Viewed in terms of its corresponding action on
u, Eq. (11) corresponds to a classical QR decomposition
by Givens rotations from Eq. (9). The right-hand side of
Eq. (11) is the upper-triangular matrix in QR form. But
since that matrix is also unitary, the upper-triangular
form is diagonal with the pth entry equal to eiφp.
When the Givens rotation matrix rpq(θ) left multiplies
the N × N unitary matrix u it eﬀects a rotation between
rows up and uq which can be used to zero out a sin-
gle element in one of those rows.
Since there are
N
2


elements below the diagonal, the number of Givens ro-
tation required is
N
2

. The usual strategy for the QR
decomposition via Givens rotations involves ﬁrst rotat-
ing all the oﬀ-diagonal elements in the ﬁrst column to
zero, and then rotating all the oﬀ-diagonal elements in
the second column to zero, etc., starting from the bot-
tom.
Since Givens rotations aﬀect only the rows that
they act upon, one can zero out an entire column before
moving on to the next. In order to avoid worrying about
non-local Jordan-Wigner strings, we will want to restrict

Givens rotations to act on adjacent rows, q and q −1.
With that restriction, if elements (p, q) and (p, q −1) are
already zero, then no Givens rotations between rows q
and q −1 can restore those elements to nonzero values.
This observation suggests a parallelization scheme which
is suitable for even a linear array of qubits. The paral-
lelization scheme is illustrated in Figure 2.
In the scheme depicted in Figure 2, elements should
always be eliminated by performing a Givens rotation
with the row above it.
As we can see from Figure 2,
one will not perform a Givens rotation to eliminate an
element in column q until 2q−1 parallel layers of rotations
have already occurred. The algorithm terminates once
rotations have reached q = N −1; thus, gate depth of
2N −3 is suﬃcient to implement the basis change.
We can gain additional constant factor eﬃciencies from
symmetries of the Hamiltonian.
The usual electronic
structure Hamiltonian has both SU(2) (spin) and U(1)
(particle number η) symmetry. We can arrange the ini-
tial state to be an eigenstate of spin with the ﬁrst N/2
qubits spin-up and the remaining qubits spin-down; u is
block-diagonal in these two spin sectors. Performing the
procedure in parallel across the two sectors brings the
total depth to N −3 layers. In addition, working within
the η-electron manifold of Slater determinants, one only
needs to perform rotations creating excitations between
the η occupied orbitals and the N −η virtual orbitals.
Thus, rather than the
N
2

Givens rotations required, only
η(N −η) Givens rotations are required. If we assume that
the ﬁrst η/2 orbitals of each spin sector are initially oc-
cupied, then after η −1 parallel steps of the algorithm
depicted in Figure 2, one has implemented all rotations
that couple occupied and virtual spaces (all remaining
rotations are between virtual orbitals). If η > N/2 we
can rotate the holes instead of the particles; thus, gate
depth of η −1 < N/2 is suﬃcient to prepare any single
Slater determinant using our approach.
We have thus shown a method for preparing arbitrary
Slater determinants with at most N/2 depth on a linear
nearest-neighbor architecture. This is even lower depth
than any known implementation of the FFFT when the
FFFT is restricted to linear or planar connectivities.
Thus, our result represents an improvement in situations
that call for applying the FFFT on a limited connectivity
architecture, such as in the experimental proposal of [40].
Unlike implementations of the FFFT based on radix-2
decimation [40, 45], the state preparation described here
is not limited to binary power system sizes.

Conclusion

We have introduced approaches for both state prepa-
ration and time evolution of electronic structure Hamil-
tonians which execute in at most linear gate depth with
linear connectivity. In the near-term, both results raise
the prospects of practical algorithms for non-trivial sys-
tem sizes which meet the limitations of available hard-

## Page 5

ware. Even within a fault-tolerant paradigm, both our
state preparation and Trotterization procedures aﬀord
constant factor improvements over all prior approaches,
including those requiring arbitrary connectivity. While
we have argued for the optimality of our Trotter steps,
proving a formal lower bound remains an open problem.
Future work should numerically investigate the Trotter
errors associated with these Trotter steps in the spirit of
prior work on Gaussian bases [14, 23].

Acknowledgments

We thank Zhang Jiang, Sergio Boixo, Eddie Farhi,
James McClain, Kevin Sung, and Guang Hao Low for
helpful discussions. I. D. K. acknowledges partial sup-
port from the National Sciences and Engineering Re-
search Council of Canada. A. A.-G. acknowledges the
Army Research Oﬃce under Award: W911NF-15-1-0256.
We thank contributors to the open source library Open-
Fermion (www.openfermion.org) [50] which was used to
verify some equations of this work.

[1] D. S. Abrams and S. Lloyd, Physical Review Letters 79,
4 (1997).
[2] G. Ortiz, J. Gubernatis, E. Knill,
and R. Laﬂamme,
Physical Review A 64, 22319 (2001).
[3] A. Aspuru-Guzik, A. D. Dutoi, P. J. Love, and M. Head-
Gordon, Science 309, 1704 (2005).
[4] I. Kassal, S. P. Jordan, P. J. Love, M. Mohseni,
and
A. Aspuru-Guzik, Proceedings of the National Academy
of Sciences 105, 18681 (2008).
[5] J. D. Whitﬁeld, J. Biamonte, and A. Aspuru-Guzik, Mol.
Phys. 109, 735 (2011).
[6] L. Veis, J. Viˇs´ak, T. Fleig, S. Knecht, T. Saue, L. Viss-
cher,
and J. Pittner, Physical Review A 85, 30304
(2012).
[7] J. T. Seeley, M. J. Richard, and P. J. Love, Journal of
Chemical Physics 137, 224109 (2012).
[8] L. Veis and J. Pittner, Journal of Chemical Physics 140,
1 (2014).
[9] R. Babbush, P. J. Love, and A. Aspuru-Guzik, Scientiﬁc
Reports 4, 6603 (2014).
[10] D. Wecker, B. Bauer, B. K. Clark, M. B. Hastings, and
M. Troyer, Phys. Rev. A 90, 022305 (2014).
[11] M. B. Hastings, D. Wecker, B. Bauer,
and M. Troyer,
Quantum Info. Comput. 15, 1 (2015).
[12] N. Moll, A. Fuhrer, P. Staar, and I. Tavernelli, Journal
of Physics A: Mathematical and Theoretical 49, 295301
(2016).
[13] D. Poulin, M. B. Hastings, D. Wecker, N. Wiebe, A. C.
Doberty,
and M. Troyer, Quantum Info. Comput. 15,
361 (2015).
[14] R. Babbush, J. McClean, D. Wecker, A. Aspuru-Guzik,
and N. Wiebe, Phys. Rev. A 91, 022311 (2015).
[15] J. D. Whitﬁeld, V. Havl´ıˇcek,
and M. Troyer, Physical
Review A 94, 030301(R) (2016).
[16] P.-L. Dallaire-Demers and F. K. Wilhelm, Physical Re-
view A 94, 62304 (2016).
[17] K. Sugisaki, S. Yamamoto, S. Nakazawa, K. Toyota,
K. Sato, D. Shiomi, and T. Takui, The Journal of Phys-
ical Chemistry A 120, 6459 (2016).
[18] J. R. McClean, M. E. Schwartz, J. Carter,
and W. A.
de Jong, Physical Review A 95, 42308 (2017).
[19] B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings, and
M. Troyer, Physical Review X 6, 31045 (2016).
[20] R. Babbush, D. W. Berry, I. D. Kivlichan, A. Y. Wei,
P. J. Love, and A. Aspuru-Guzik, New Journal of Physics
18, 033032 (2016).

[21] J. R. McClean, J. Romero, R. Babbush, and A. Aspuru-
Guzik, New Journal of Physics 18, 23023 (2016).
[22] V. Havl´ıˇcek, M. Troyer,
and J. D. Whitﬁeld, Physical
Review A 95, 032332 (2017).
[23] M. Reiher, N. Wiebe, K. M. Svore, D. Wecker,
and
M. Troyer, Proceedings of the National Academy of Sci-
ences 114, 7555 (2017).
[24] F. Motzoi, M. P. Kaicher, and F. K. Wilhelm, Physical
Review Letters 119, 160503 (2017).
[25] S. Bravyi,
J. M. Gambetta,
A. Mezzacapo,
and
K. Temme, arXiv:1701.08213 (2017).
[26] N.
Rubin,
R.
Babbush,
and
J.
McClean,
arXiv:1801.03524 (2018).
[27] M. Steudtner and S. Wehner, arXiv:1712.07067 (2017).
[28] R. Babbush, D. W. Berry, I. D. Kivlichan, A. Y. Wei,
P. J. Love, and A. Aspuru-Guzik, Quantum Science and
Technology 3, 15006 (2018).
[29] B. P. Lanyon, J. D. Whitﬁeld, G. G. Gillett, M. E.
Goggin, M. P. Almeida, I. Kassal, J. D. Biamonte,
M. Mohseni, B. J. Powell, M. Barbieri, A. Aspuru-Guzik,
and a. G. White, Nature Chemistry 2, 106 (2010).
[30] J. Du, N. Xu, X. Peng, P. Wang, S. Wu,
and D. Lu,
Physical Review Letters 104, 30502 (2010).
[31] A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q.
Zhou, P. J. Love, A. Aspuru-Guzik, and J. L. O’Brien,
Nature Communications 5, 1 (2014).
[32] Y.
Wang,
F.
Dolde,
J.
Biamonte,
R.
Babbush,
V.
Bergholm,
S.
Yang,
I.
Jakobi,
P.
Neumann,
A. Aspuru-Guzik, J. D. Whitﬁeld,
and J. Wrachtrup,
ACS Nano 9, 7769 (2015).
[33] R. Barends, L. Lamata, J. Kelly, L. Garc´ıa-´Alvarez, A. G.
Fowler, A. Megrant, E. Jeﬀrey, T. C. White, D. Sank,
J. Y. Mutus, B. Campbell, Y. Chen, Z. Chen, B. Chiaro,
A. Dunsworth, I.-C. Hoi, C. Neill, P. J. J. O’Malley,
C. Quintana, P. Roushan, A. Vainsencher, J. Wenner,
E. Solano, and J. M. Martinis, Nature Communications
6, 7654 (2015).
[34] Y. Shen, X. Zhang, S. Zhang, J.-N. Zhang, M.-H. Yung,
and K. Kim, Physical Review A 95, 020501(R) (2017).
[35] R. Santagati, J. Wang, A. Gentile, S. Paesani, N. Wiebe,
J. McClean, S. Short, P. Shadbolt, D. Bonneau, J. Silver-
stone, D. Tew, X. Zhou, J. OBrien, and M. Thompson,
arXiv:1611.03511 (2016).
[36] P.
J.
J.
O’Malley,
R.
Babbush,
I.
D.
Kivlichan,
J. Romero,
J. R. McClean,
R. Barends,
J. Kelly,
P. Roushan, A. Tranter, N. Ding, B. Campbell, Y. Chen,
Z. Chen, B. Chiaro, A. Dunsworth, A. G. Fowler, E. Jef-

## Page 6

frey, A. Megrant, J. Y. Mutus, C. Neill, C. Quintana,
D. Sank, A. Vainsencher, J. Wenner, T. C. White, P. V.
Coveney, P. J. Love, H. Neven, A. Aspuru-Guzik,
and
J. M. Martinis, Physical Review X 6, 31007 (2016).
[37] J. I. Colless, V. V. Ramasesh, D. Dahlen, M. S. Blok,
J. R. McClean, J. Carter, W. A. de Jong, and I. Siddiqi,
arXiv:1707.06408 (2017).
[38] A. Kandala, A. Mezzacapo, K. Temme, M. Takita,
M. Brink, J. M. Chow,
and J. M. Gambetta, Nature
549, 242 (2017).
[39] E. F. Dumitrescu, A. J. McCaskey, G. Hagen, G. R.
Jansen, T. D. Morris, T. Papenbrock, R. C. Pooser, D. J.
Dean, and P. Lougovski, arXiv:1801.03897 (2018).
[40] R. Babbush,
N. Wiebe,
J. McClean,
J. McClain,
H. Neven, and G. K.-L. Chan, arXiv:1706.0023 (2017).
[41] D. Wecker, M. B. Hastings, N. Wiebe, B. K. Clark,
C. Nayak, and M. Troyer, Physical Review A 92, 062318
(2015).
[42] D. Wecker, M. B. Hastings, and M. Troyer, Phys. Rev.
A 92, 042303 (2015).
[43] E.
Farhi,
J.
Goldstone,
and
S.
Gutmann,
arXiv:1411.4028 (2014).
[44] R. D. Somma, G. Ortiz, J. Gubernatis, E. Knill,
and
R. Laﬂamme, Phys. Rev. A 65, 17 (2002).
[45] F. Verstraete, J. I. Cirac, and J. I. Latorre, Phys. Rev.
A 79, 032316 (2009).
[46] F. Verstraete and J. I. Cirac, Journal of Statistical Me-
chanics: Theory and Experiment 2005, P09012 (2005).
[47] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani,

Physical Review Letters 73, 58 (1994).
[48] D. Maslov, Physical Review A 76, 52310 (2007).
[49] D. J. Thouless, Nuclear Physics 21, 225 (1960).
[50] J. R. McClean, I. D. Kivlichan, K. J. Sung, D. S. Steiger,
Y. Cao, C. Dai, E. S. Fried, C. Gidney, T. H¨aner,
T. Hardikar, V. Havl´ıˇcek, C. Huang, Z. Jiang, M. Neeley,
J. Romero, N. Rubin, N. P. D. Sawaya, K. Setia, S. Sim,
W. Sun, F. Zhang,
and R. Babbush, arXiv:1710.07629
(2017).

Appendix A: Hubbard Model Trotter Steps

Using the fermionic swap network described in the
main paper, we can also simulate Trotter steps of the 2D
Hubbard model with gate depth O(
√

N) on a linear array
of qubits. We can do this for Hubbard models with and
without spin, but it is currently not clear how one might
eﬃciently handle periodic boundary conditions with the
same strategy.
Below, we explain how this algorithm
would work for the 2D Hubbard model with spins but
note that a simple extension of the algorithm is possible
for models in d dimensions with gate depth O(N
d−1

d ).
The 2D Hubbard Hamiltonian with spins is

H =−t
X

a†
p,σaq,σ + a†
q,σap,σ

+ U
X

p
np,↑np,↓(A1)

⟨pq⟩,σ

where ⟨pq⟩indicates that the sum should be taken over
all pairs of spin-orbitals (p, σ) and (q, σ) which are ad-
jacent on the 2D Hubbard lattice. The Hubbard Hamil-
tonian is a special case of the general electronic struc-
ture Hamiltonian where many of the terms are zero;

FIG. 3. Depiction of the mapping of Hubbard sites to a linear
qubit chain.
The circles each represent a spin-orbital.
As
labeled, red circles contain spin-up orbitals and blue circles
contain spin-down orbitals. In the Hubbard Hamiltonian, the
on-site interaction gives a diagonal couplings between the two
spin-orbitals within each spatial orbital (e.g. n3,↑n3,↓) and
the hopping terms are oﬀ-diagonal between adjacent spatial
orbitals of the same spin (e.g. a†
5,↓a6,↓+a†
6,↓a5,↓). The arrows
between the circles indicate the canonical ordering that should
be used in the Jordan-Wigner transformation. The general
pattern here is that we alternate whether the up or down spin-
orbital comes ﬁrst across the rows, and we alternate whether
to order in ascending or descending order across columns.

whereas the general electronic structure Hamiltonian has
O(N 2) terms, the Hubbard Hamiltonian has only O(N)
terms.
The ﬁrst step in our procedure will be to use
the Jordan-Wigner transformation to map Eq. (A1) to
a qubit Hamiltonian. One needs to choose a particular
ordering of the orbitals for the Jordan-Wigner transfor-
mation in order for our technique to work. The ordering
we choose is explained in Figure 3.
With the term ordering depicted in Figure 3, terms
are arranged so that we may immediately simulate all of
the npnq terms. The diﬃcult part of this simulation is
the hopping terms a†
p,σaq,σ + a†
p,σaq,σ. With the order-
ing of Figure 3, one can also immediately simulate half
of the horizontal hopping terms. The ﬁnal step performs
a series of O(
√

N) layers of fermionic swaps depicted in
Figure 4 which cycles all spin-orbitals through conﬁgura-
tions in which they are adjacent to all orbitals with which
they share a hopping term.
This algorithm would appear to be the most eﬃcient
strategy for simulating the 2D Hubbard model on a lin-
ear array of qubits.
However, note that given planar
qubit connectivity, there is an obvious way to implement
Trotter steps of O(1) depth that is readily apparent (and
likely anticipated by those authors) from the techniques
of [46]. However, the mapping in Ref. [46] requires dou-
bling the number of qubits in the simulation and involves
a more complicated (though still local) Hamiltonian; this
constant overhead may be signiﬁcant for moderate N.

Appendix B: State Preparation by Givens Rotation

Here, we provide a pedagogical explanation of the
strategy based on Givens rotations discussed in the main
text. We will show that one can implement any 2N × 2N

## Page 7

(a) Left Stagger UL

(b) Right Stagger UR

FIG. 4. By repeating the pattern of fermionic swaps shown
as UL and UR one is able to bring spin-orbitals from adjacent
rows next to each other in the canonical ordering so that
the hopping term may be applied locally. First, one applies
UL. This will enable application of the remaining horizontal
hopping term that could not previously be reached. Then,
one should repeatedly apply URUL. After each application of
URUL new vertical hopping terms become available until one
has applied URUL a total of
p

N/8 −1 times. At that point,
one needs to reverse the series of swaps until the orbitals are
back to their original locations in the canonical ordering. At
that point, applying URUL will cause the qubits to circulate
in the other direction. This should be repeated for a total
of
p

N/8 −1 times to make sure all neighboring orbitals are
adjacent at least once. The total number of layers of fermionic
swaps required for the whole procedure is
p

9 N/2.

unitary operator of the form

X

pq
[log u]pq
a†
paq −a†
qap

!

U(u) = exp

(B1)

where [log u]pq is the (p, q) element of the N × N matrix
log u, with a sequence of exactly
N
2

rotations of the form

Rpq (θ) = exp

θpq
a†
paq −a†
qap

.
(B2)

Notice that Rpq (θ) is a special case of the basis transfor-
mation unitary U(u) from Eq. (B1) which occurs when
U (rpq (θ)) = Rpq (θ).
By the deﬁnition of the matrix
logarithm we see that





1 · · ·
0
· · ·
0
· · · 0
... ...
...
...
...
0 · · · cos (θ) · · · −sin (θ) · · · 0
...
...
...
...
...
0 · · · sin (θ) · · ·
cos (θ)
· · · 0
...
...
...
... ...
0 · · ·
0
· · ·
0
· · · 1



























rpq (θ) =

.
(B3)

The cosine terms appear in the pth and qth entries along
the diagonal, and the positive (negative) sine term ap-
pears at the intersections of row p (q) and column q (p).
We see then that Rpq(θ) represents a 2N × 2N matrix
whereas rpq(θ) represents an N × N matrix. Note that
rpq (θ) is a Givens rotation matrix.
Crucial to the procedure we will describe is the fact
that the map U(u) is a homomorphism under matrix
multiplication:

U (ua) · U (ub) = U (ua · ub) .
(B4)

We now prove this. To construct our proof, we introduce
a representation of a Slater determinant, C, which is a
matrix whose columns hold the coeﬃcients of the orbitals
in some basis |φi⟩. This matrix is an element of the Grass-
mann algebra. It is the natural object obtained from a
classical mean-ﬁeld calculation that deﬁnes a Slater de-
terminant within the speciﬁed basis. The matrix can be
computed in two equivalent ways.
First, the mapping
from this representation to the full space is given by the
Pl¨ucker embedding Φ





|Φ(C)⟩=
^

X

j
Ci
j |φj⟩


(B5)

i

where ∧denotes the Grassmann wedge product.
Second, and more commonly in electronic structure
and quantum mechanics, this map can be expressed con-
veniently in terms of second quantization as

i
c†
i |∅⟩
c†
i =
X

j
Ci
ja†
j
(B6)

|Φ(C)⟩=
Y

where |Φ(C)⟩is in the full Hilbert space, |∅⟩is the Fermi
vacuum, and a†
i expresses the occupation of an orbital
site |φi⟩. We will ﬁrst show that the map satisﬁes

U(u) |Φ(C)⟩= |Φ(uC)⟩= |Φ( ˜C)⟩
(B7)

where we have deﬁned ˜C = uC. We begin as

i
c†
i |∅⟩
(B8)

|Φ( ˜C)⟩= U(u)
Y

i
U(u)c†
iU(u)† |∅⟩=
Y

i
˜c†
i |˜∅⟩

=
Y

where ˜c†
i = U(u)c†
iU(u)i, the rotated vacuum |˜∅⟩=
U(u)† |∅⟩= |∅⟩due to vanishing action on the vacuum,
and we used the fact that anti-Hermitian operators gen-
erate the unitary group. To demonstrate this equality,
we wish to show that

˜c†
i =
X

j
˜Ci
ja†
j.
(B9)

Using the BCH expansion to determine ˜c†
i, we ﬁnd

˜c†
i = U(u)c†
iU(u)† = eˆκc†
ie−ˆκ
(B10)

= c†
i + [ˆκ, c†
i] + 1

2[ˆκ, [ˆκ, c†
i]] + · · ·

## Page 8

where we have deﬁned

ˆκ =
X

pq
[log u]pqa†
paq =
X

pq
κpqa†
paq.
(B11)

Evaluating the ﬁrst order term, we ﬁnd that





[ˆκ, c†
i] =

j
Ci
ja†
j

X

pq
κpqa†
paq,
X


(B12)

X

!

=
X

a†
p;

q
κpqCi
q

p

following to higher orders, we ﬁnd that the eﬀect is to
deﬁne a new creation operator whose coeﬃcients in the
|φi⟩basis are eκCi, i.e.

˜c†
i =
X

j a†
j,
(B13)


uCi

j

which demonstrates the equality

U(u) |Φ(C)⟩= |Φ( ˜C)⟩= |Φ(uC)⟩.
(B14)

With this equality, we ﬁnd that

U(ua)U(ub) |Φ(C)⟩= U(ua) |Φ(ubC)⟩
(B15)
= |Φ(uaubC)⟩

this yields an expansion with coeﬃcients

i
˜˜c †
i |∅⟩
(B16)

|Φ(uaubC)⟩=
Y

j
[uaubC]i
j a†
j.
(B17)

˜˜c †
i =
X

From this we see that

|Φ(uaubC)⟩= U(uaub) |Φ(C)⟩
(B18)

and as the representative C we chose was arbitrary, it
must hold for any C within the Grassmann algebra, and
thus we conclude that

U(ua)U(ub) = U(uaub)
(B19)

which shows the desired property.
Combining Eq. (B3) and Eq. (B4) brings us to the
important observation

Rpq (θ) U (u) = U (rpq (θ) u) .
(B20)

We will show that by applying a sequence of these rota-
tions, one can implement U † up to some trivial phases:

N
X

Y

p=1
eiφpnp
(B21)

k
Rk (θk) U (u) =

N
X

p=1
eiφp |p⟩⟨p|
(B22)

Y

k
rk (θk) u =

where the index k represents a particular pair p, q which is
applied at iteration k and eiφp is a unit phase. Given this
sequence of rotations and the phases deﬁned by φp, we
may implement U by applying Q

p eiφpnp (a single layer of
gates) and then reversing the sequence of rotations. We
explain how this sequence and these phases can be deter-
mined by focusing on how Givens rotations in the smaller
space can be used to manipulate u. Finding the sequence
of rotations in Eq. (B21) is equivalent to performing the
QR decomposition, which involves decomposing a square
matrix into a product of an orthogonal (in our case, uni-
tary) matrix right multiplied by an upper-triangular ma-
trix. This upper-triangular matrix is diagonal, with the
pth entry given by eiφp, as in Eq. (B21).
When the Givens rotation matrix rpq(θ) left multiplies
the N × N unitary matrix u, the product is a unitary
matrix with entries (assuming p < q)





upj cos θ −uqj sin θ
i = p
uqj sin θ + upj cos θ
i = q
uij
otherwise.

Aij = [rpq (θ) u]ij =




In order to diagonalize u (as shown in Eq. (B21)) our
strategy will always be to use Givens rotations in or-
der to rotate an element Aqj to zero. Thus, when ap-
plying rpq(θ) to the matrix A, we will always choose
θ = arctan(−Apj/Aqj) depending on which column j we
are targeting. Because each rotation only modiﬁes two
rows of A, it is possible to carry out this procedure in par-
allel to reduce the depth. We discuss an eﬀective strategy
for the order of parallel rotations in the main text.
