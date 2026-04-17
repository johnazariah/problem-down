---
source_pdf: ../arxiv_2103.12097.pdf
pages: 42
extracted_at: 2026-04-17T12:32:41+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_2103.12097

Source PDF: ../arxiv_2103.12097.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

The Hubbard Model

Daniel P. Arovas1, Erez Berg2,
Steven A. Kivelson3, Srinivas Raghu3,4

1Department of Physics, University of California at San Diego, La Jolla,
California 92093, USA
2Department of Condensed Matter Physics, Weizmann Institute of Science,
Rehovot 76100, Israel
3Department of Physics, Stanford University, Stanford, USA, 94305
4Stanford Institute for Materials and Energy Sciences, SLAC National
Accelerator Laboratory and Stanford University, Menlo Park, CA 94025, USA

arXiv:2103.12097v2 [cond-mat.str-el] 18 Jul 2021

1

## Page 2

1. Introduction

The Hubbard model (1) has come to play a paradigmatic role in the theory of electronic
correlations in quantum materials where interactions play an essential role.
Its central-
ity in the quantum statistical mechanics of interacting fermions is comparable to that of
the Ising model in classical statistical mechanics, yet almost sixty years after it was ﬁrst
described, there remain unsettled basic questions, even concerning the actual phases that
arise for various lattice geometries. Conversely, the more progress that is made in obtaining
theoretical solutions, the clearer it becomes that this simple model can exhibit a startling
array of phases and regimes, many of which have clear parallels with observed behaviors
of a wide variety of complex materials.
For instance, there is compelling evidence that
ferromagnetism, various forms of antiferromagnetism, unconventional superconductivity,
charge-density waves, electronic liquid crystalline phases, and topologically ordered phases
(e.g., “spin liquids”), among other phases, occur in speciﬁc realizations of the Hubbard
model.
It is our purpose here to summarize, to the extent possible in a brief article, what is
established concerning the quantum phases of the Hubbard model. While some discussion of
the model on small clusters and in one dimension (d = 1) is included for pedagogic purposes,
the focus is primarily on the model on regular lattices (i.e. in the absence of disorder) in
d = 2 and d = 3. Likewise while we include some discussion of ﬁnite temperature results, our
focus is on ground state properties, mostly to keep the scope of the article manageable. In
the strong coupling limit and in the special case of one electron per site, the Hubbard model
reduces to an insulating quantum Heisenberg antiferromagnet, which itself can exhibit many
diﬀerent and fascinating quantum phases; these will be covered to an extent but mostly we
will focus on phases that occur for generic electron densities. Furthermore, we have mostly

2
Arovas et al.

## Page 3

focused on equilibrium properties of the model, especially those essential thermodynamic
correlation functions that characterize distinct quantum phases of matter.
Even within this limited scope, we have restricted ourselves to “controlled” solutions - by
which we mean either exact results (typically obtained using numerical methods of various
sorts) or in cases where there is an approximation scheme that becomes asymptotically exact
as an explicitly identiﬁed small parameter tends to zero. This has led us to omit discussion
of a variety of new and powerful “mean-ﬁeld” methods, including dynamical mean ﬁeld
theory and dynamical cluster approximations, which have proﬁtably been applied to this
problem. Fortunately, a companion paper to the present paper (2) has these approaches as
its complementary focus.
We also will not explore the relation between the Hubbard model and experiments in
any particular quantum material. Nonetheless, much of the modern resurgence of interest
in this model is a consequence of the role it has played in the study of high temperature
superconductivity in the cuprates. Originally, this connection was suggested on rather basic
phenomenological grounds (3, 4) - the “parent state” in the cuprates is a quasi-2d antifer-
romagnetic insulator, and the Hubbard model on the square lattice is the simplest possible
model of a doped antiferromagnet. It is thus striking that many of the properties of this
model that have been uncovered in subsequent theoretical studies turn out to resemble
essential features of the electronic states of the cuprates that have been revealed by exper-
iments, viz.: 1) The Hubbard model (at least for a range of U not too large) exhibits a
“dome” of d-wave superconductivity throughout a range of doping. 2) It exhibits antifer-
romagnetic long-range order when undoped. 3) It evolves to an eﬀectively weakly-coupled
Fermi liquid state upon heavy doping. 4) It exhibits a tendency toward formation of long-
period unidirectional charge and spin density wave orders (stripes) in the same range of
doping in which superconducting correlations (at least locally) appear strongest. Indeed, as
in the materials themselves, the relation between density-wave and superconducting orders
appears more complicated than the collocation “competing orders” might suggest, leading
to their description as “intertwined.” As has been noted earlier (5), this congruence in be-
havior is suﬃciently striking that it encourages the view that the solution of the Hubbard
model can, in some sense, be considered to be the solution of the high Tc problem.

2. Theorems

The Hubbard model describes itinerant, interacting electrons of spin- 1

2 hopping on a set Λ
of spatially localized orbitals. The Hamiltonian is written as

ˆH = −
X

X

σ
tij c†
iσ cjσ + U
X

i∈Λ
c†
i↑c†
i↓ci↓ci↑
,
1.

i,j∈Λ

where the hopping tij is often restricted to nearest-neighbor sites, i.e. tij = t∗
ji = t δ|i−j|,1,
but generalizations can include further neighbor hopping and/or Peierls phase factors to
account for nonzero magnetic ﬂux. Unless explicitly noted, we will conﬁne our attention
to the zero ﬂux (time-reversal invariant) case.
Moreover, we will consider only regular,
connected lattices, i.e. we do not consider the eﬀects of “disorder.” The electron ﬁlling is
deﬁned to be n ≡N/|Λ| where |Λ| is the total number of sites and N is the number of
electrons. The half-ﬁlled band, with one electron per site, corresponds to n = 1.
Continuous global symmetries – The model’s most apparent symmetry is a global U(2),
under which ciσ →Uσσ′ ciσ′ with U ∈U(2) the same matrix on all sites i.
Separating

www.annualreviews.org • The Hubbard Model
3

## Page 4

U(2) = U(1) × SU(2), the global U(1) invariance reﬂects global charge conservation, hence
the total particle number ˆ
N = P

i,σ c†
iσciσ is a good quantum number. This symmetry may
be spontaneously broken in a superconducting state. The global SU(2) invariance reﬂects
spin isotropy, hence ˆSz and ˆS2 are good quantum numbers, with ˆS = 1

i,µ,ν c†
iµ σµν ciν.
Global SU(2) invariance of the ground state is spontaneously broken in any ferromagnetic
or antiferromagnetic state.
Particle-hole symmetry – On a bipartite lattice, the transformation ciσ →ηi c†
iσ, where
ηi = ± on alternate sublattices, results in the transformed Hamiltonian

ˆH′ = −
X

X

i,j∈Λ

2
P

i∈Λ
c†
i↑c†
i↓ci↓ci↑+ U
|Λ| −ˆ
N

,
2.

σ
tij c†
iσ cjσ + U
X

At half-ﬁlling, ˆ
N = |Λ|, the model is particle-hole symmetric. In such cases, the system
is proven (6) to be of uniform density, with ⟨c†
iσcjσ⟩=
1
2 δij if i and j are on the same
sublattice (with no implicit sum on σ)1. However, this does not preclude either magnetic
or charge density wave order in the thermodynamic limit.
The SU(2) spin symmetry of the Hubbard model is generated by the operators

i
c†
i↑ci↓
,
ˆS−= ( ˆS+)†
,
ˆSz = 1

ˆS+ =
X

X

c†
i↑ci↑−c†
i↓ci↓

,
3.

2

i

all of which commute with ˆH as well as with the number operator ˆ
N = P

i,σ c†
iσciσ. A
second, “hidden” SU(2) symmetry (7, 8) is present on bipartite lattices, and is generated
by the pseudospin operators

2
ˆ
N −|Λ|

,
4.

i
ηi c†
i↑c†
i↓
,
ˆJ−= ( ˆJ+)†
,
ˆJz = 1

ˆJ+ =
X

where ηi = ±1 on the A and B sublattices, respectively. These operators also satisfy the
SU(2) algebra

Jα, Jβ
= iϵαβγJγ. While the Jα’s do not commute with ˆH and ˆ
N as do
the generators Sα for physical spin, they are eigenoperators in that

 ˆK, ˆJ±
= ±(U −2µ) J±
5.

and [ ˆK, ˆJz] = 0, where ˆK = ˆH −µ ˆ
N is the grand canonical Hamiltonian (µ is the chemical
potential). Thus, at half-ﬁlling, when µ = 1

2U, the Hubbard model has an additional SU(2)
symmetry. Hence, the global symmetry group at half-ﬁlling is SO(4) ∼= SU(2) × SU(2)/Z2,
where the Z2 is associated with the fact that ˆJz + ˆSz has to be an integer when |Λ| is even,
and half-integer when |Λ| is odd (9).
Lieb’s theorem – In 1989, Lieb (10) proved that for the attractive Hubbard model, with
U < 0 (and allowing more generally for site-dependent Ui < 0 ∀i) that if the total number
of electrons N is even, then the ground state of ˆH is unique, and is a total spin singlet, i.e.
with S = 0. A corollary is that if U > 0 (independent of i), Λ is bipartite with |A| ≥|B|, and
N = |Λ| is even, then the ground state of ˆH has total spin S = 1

2
|A| −|B|

and degeneracy
2S + 1 (i.e. spin degeneracy is the only degeneracy).
A convenient example is the so-
called Lieb lattice, in which the A sublattice is a square lattice and there is a B sublattice

1The conditions for uniform density from ref. (6) are much more general, and include the possi-
bility of site-dependent and even nonlocal interactions.

4
Arovas et al.

## Page 5

Table 1
Possible phases consistent with the LSMOH theorem. A check in the ﬁrst
column indicates that the number of electrons per site is not an even integer. “Unique”

indicates whether a single, non-degenerate ground state on the torus is possible. By
“featureless” we mean that there is no spontaneous symmetry breaking of any kind
(this does not exclude topological order).
The last column names a phase that is
consistent with the listed properties, if any.

site at the center of every link (i.e. the CuO2 lattice of the Emery model (11)). Lieb’s
proof extends the Perron-Frobenius argument deployed in one-dimensional systems (12) by
invoking a tool known as “spin-space reﬂection positivity”. The theorem then entails a
hierarchy of lowest energy levels in diﬀerent total spin sectors, E0(S) < E0(S + 1), where
S ∈
 1

2(|A| −|B|), . . . , 1

2|Λ| −1
. For bipartite lattices, the conditions of Lieb’s theorem
guarantee a ferromagnetic ground state when there is a sublattice imbalance, i.e. |A| ̸= |B|.
Thouless-Nagaoka-Tasaki theorem – An extension by Tasaki (13, 14) of the celebrated
Nagaoka theorem (15), which in fact was originally proven in a more restricted form by
Thouless (16), states the following: For the Hubbard model with U = ∞and arbitrary
non-negative tij, and with N = |Λ| −1, the ground state has total spin S =
1
2N and
degeneracy 2S + 1.
This establishes that there is a ferromagnetic ground state in the
U →∞limit when the system is one electron shy of half-ﬁlling. No rigorous extension of
these results to ﬁnite doped hole density has yet been achieved.
LSMOH theorem – The Lieb-Schultz-Mattis-Oshikawa-Hastings (LSMOH) theorem
states, in essence, that when the ﬁlling n is not an even integer, a unique, gapped, fea-
tureless, insulating ground state is impossible.
It is useful to ﬁrst consider the sort of
behavior that is ruled out by the theorem but which may pertain if the conditions of the
theorem are not met, examples of which are shown in Table 2. The Hubbard model in d = 1
is a band insulator when n = 0 or n = 2, but has a Mott phase for n = 1 that preserves
all symmetries and with no adiabatic connection to a band insulator. More generally, the
theorem applies to models with any number of conserved ﬂavors; in such a case, it states
that a featureless, gapped ground state is impossible if the ﬁlling of at least one ﬂavor per
unit cell is non-integer.
The original argument, due to Lieb, Schultz, and Mattis (LSM) (17), applied to an
N-site, spin-S XXZ spin chain with periodic boundary conditions and zero total magneti-
zation. LSM showed that if the ground state | Ψ0 ⟩is a state with crystal momentum K0,

i.e. if ˆt | Ψ0 ⟩= eiK0| Ψ0 ⟩, where ˆt is the lattice translation operator and we work in units
where the lattice spacing is a ≡1, then the application of the spin twist operator,

N
X

ˆV = exp
2πi


,
6.

j=1
j ˆSz
j

N

results in a state | Ψ1 ⟩= ˆV | Ψ0 ⟩with crystal momentum K1 = K0 + 2πS, satisfying

www.annualreviews.org • The Hubbard Model
5

## Page 6

Table 2
Character of the ground state of the positive U Hubbard square.

⟨Ψ1 | ˆHXXZ | Ψ1 ⟩= E0 + O(1/N). For exp(2πiS) = −1, the states are of diﬀerent crystal
momentum and thus orthogonal.
Thus, in the thermodynamic limit any ground state
| Ψ0 ⟩must be degenerate (or gapless). The theorem was extended to more general one-
dimensional systems in Ref. (18).
While the LSM argument does not apply in dimensions d > 1, it was extended by
Oshikawa (19) and subsequently rigorized by Hastings (20) to d-dimensional systems with
periodic boundary conditions (i.e. on a d-torus) and a ﬁnite excitation gap. The line of
reasoning, inspired by Laughlin’s argument for quantization of the Hall conductivity in
two dimensions (21), focuses on the consequences of adiabatic φ = 2π U(1) ﬂux threading
through one of the toroidal cycles, followed by a “pullback” to the original U(1) ﬂux state. In
the thermodynamic limit, starting with an initial ground state | Ψ0(φ = 0) ⟩, this procedure
results in a low energy state | Ψ1(φ = 0) ⟩(similar to the LSM construction), which becomes
degenerate with the ground state in the thermodynamic limit. The analysis can be applied
to bosonic systems as well (see, e.g., Ref. (22, 23)).

3. The Hubbard square and its extensions

The Hubbard square - that is the four site square “molecule” of Hubbard sites - is sim-
ple enough that its spectrum can be computed analytically (24), but already complicated
enough that it hosts a variety of non-trivial many-body eﬀects that shed considerable light
on the more general problem (25). The symmetry (i.e. total spin S and transformation
properties under the spatial symmetries of the square) of the ground state for the model
with nearest-neighbor hopping, t, in diﬀerent ranges of U/t and for diﬀerent values of the
electron number N between 0 and 4, is given in Table 2. Since in the absence of next-nearest-
neighbor hopping, t′ = 0, the model is particle-hole symmetric, the analogous results for
4 < N ≤8 are easily obtained.
The most remarkable feature of this table is that the ground state for N = 4 and
U > 0 transforms non-trivially under spatial symmetries - it transforms according to the
B1g representation of the D4 spatial symmetries of the square, (i.e.
it transforms like
x2 −y2). It is easy to prove (26) that no non-interacting model on the square can have this
property, i.e. this is an intrinsically new eﬀect of “strong” correlations. It is thus worthwhile
to understand its origin.
It is possible to understand this property in the weak coupling limit. We start from
considering the single-particle states for U = 0. Treating the square as a four site ring, all
eigenstates may be labeled by a Bloch wavevector k. Provided |t′| < |t|, the single particle
states are ordered in energy such that the lowest (k = 0) state has energy −2t−t′, the next

6
Arovas et al.

## Page 7

are the two-fold degenerate (k = ±π/2) with energy +t′ that transform as x and y, and the
highest (k = π) state has energy 2t −t′ and transforms as xy. Thus, for U = 0, the ground
state with N = 4 is any state with two electrons (of opposite spin) in the k = 0 state, and
two electrons in either of the ﬁrst excited states; it is thus six-fold degenerate. However,
they can be expressed uniquely as states of given symmetry: there is a triplet of S = 1 states
which transforms trivially under spatial transformations (rotations and mirror reﬂections),
and three S = 0 states, one (with one electron each in k = ±π/2) which transforms trivially
under spatial transformations, and two which are superpositions of states with two electrons
either in k = π/2 or k = −π/2, which transform either as xy or as x2 −y2. Of these, the
one that is adiabatically connected to the U > 0 ground state is the latter,

h
c†
π/2,↑c†
π/2,↓−c†
−π/2,↑c†
−π/2,↓
i
c†
0↑c†
0↓
0
.
7.

Ψx2−y2
=
1
√

2

Given that there are no degeneracies once symmetry is imposed, it is clearly possible to
incorporate the eﬀects of small U by straightforward perturbation theory. Hund’s ﬁrst rule,
which in this context would be expected to be derivable in ﬁrst order perturbation theory,
would imply that the triplet state would be the most likely candidate ground state. Indeed,
for any Slater determinant state, the ﬁrst order energy is 4UN↑N↓where Nσ is the number
of electrons with given spin polarization, and this takes its minimal value of 3U/4 in a triplet
state with three electrons of one polarization and one electron of the opposite polarization.
However, manifestly | Ψx2−y2 ⟩is not a Slater determinant, and indeed it is easy to show
that to ﬁrst order in U, it is degenerate with the triplet state. Computing the second order
correction requires a bit of algebra, but the result (given for t′ = 0 in Table 2) is that the
singlet state has the lower energy.
This is a rare example of a case in which Hund’s rule is violated. Note that the cause of
this is a subtle quantum eﬀect – the ground state in the U →0 limit is a highly entangled
state that does not reduce to a single Slater determinant.
The other case that has interesting structure is the N = 3 square. For U = 0, the
ground state is four-fold degenerate, but this degeneracy is ﬁxed by symmetry and hence
survives to non-zero U. Speciﬁcally, the ground state has S = 1/2 and k = ±π/2, i.e. it
transforms under the spatial symmetries as (x, y). However, for large U, we know from
Nagaoka’s theorem that the ground state must have S = 3/2. Since parallel spins do not
interact in the Hubbard model, this state is the non-interacting (Slater determinant) state
with one electron in each of k = 0 and ±π/2; the resulting state is manifestly invariant
under the spatial symmetries.
It requires a little algebra to derive the critical value of
U = UNag that separates the two regimes; for t′ = 0, UNag = 4(2 +
√

7) t ≈18.6t.
It is also interesting to consider an ensemble of Hubbard squares. If they can exchange
particles, we can ask the question: if we have a total of N electrons (with 0 < N ≤8) and
two molecular Hubbard squares on which to place them, what is the lowest energy state?
Not surprisingly, for N = 8 it is best to put four electrons on each molecule, while for N = 7
it is best to place three on one molecule and four on the other. However, for N = 6, the
result is more interesting. We deﬁne the pair binding energy,

∆p ≡2 E(3) −E(4) −E(2) ,
8.

where E(n) is the n-electron ground state energy of a molecule. ∆p is the energy diﬀerence
between placing 3 electrons (one “doped hole”) on each molecule, or two electrons (one pair
of doped holes) on one and four electrons (no holes) on the other. ∆p is negative for U

www.annualreviews.org • The Hubbard Model
7

## Page 8

larger than a certain value Up, as one might have expected, but it is positive for U < Up, i.e.
there is an eﬀective induced attraction between two doped holes. (For t′ = 0, Up ≈4.584t.)
The existence of a range of U > 0 in which ∆p > 0 constitutes the simplest paradigmatic
example of a system in which an eﬀective attraction - indeed induced pairing - arises from
purely repulsive microscopic interactions. Ultimately, it is related to the anomalous stability
of the state with four electrons on one molecule.
In the weak coupling limit, the pair-
binding can be computed perturbatively as ∆p = A U 2/t + . . . , where A is a function
of t′/t with A = 1/32 for t′ = 0.
One can also consider the separate contributions of
the kinetic energy (hopping term) and the interaction energy (Hubbard term) to ∆p. In
the weak-coupling limit, pair formation is associated with a cost in kinetic energy which
is more than compensated by a reduced cost in repulsion, but for Up > U > U ⋆(where
U ⋆≈2.457 t for t′ = 0), ∆p gets a positive contribution from a lowering of the kinetic
energy and a negative contribution (disfavoring pair-binding) from the interactions. An
intrinsically strong coupling mechanism of “kinetic-energy driven pairing” is thus in play
for U ⋆< U < Up.
One ﬁnal lesson from this concerns the preferred symmetry of a “pairing” order param-
eter. Consider the operator ˆΦ = P

i,j φi,j ci↑cj↓that creates the two-electron ground state
by acting on the undoped (four electron) ground state. This operator can be viewed as
creating a “Cooper pair” of doped holes. As ﬁrst observed by Scalapino and Trugman (25),
the symmetry properties of ˆΦ are determined by the diﬀerence of the spatial symmetries of
two and four electron ground states. For the case tabulated above valid for |t′| < |t|, this
means that this operator has dx2−y2 symmetry. This illustrates the robust preference for
d-wave superconductivity that we will see is a generic feature of the Hubbard model on the
square lattice.
While the Hubbard square is particularly illuminating as it is analytically solvable, it is
worth noting that other small clusters - solvable numerically - can exhibit similar behaviors,
and in particular regimes pair binding arises even when U > 0. Examples of this include
the Hubbard model on the tetrahedron (in which pair-binding persists for all U), cube, and
truncated tetrahedron (27).
Distinct phases of matter - and in particular spontaneously broken symmetries - do not
arise in ﬁnite Hubbard clusters. However, in certain circumstances, the properties of an
extended system consisting of weakly coupled clusters can be inferred from the properties
of an isolated cluster in a controlled expansion in powers of the (assumed small) intercluster
couplings. Such an analysis was carried through for a 2d “checkerboard” array of Hubbard
squares in Refs. (28, 29, 30, 31, 32, 33, 34). Here, the complexity of the various regimes
found for the isolated square implies the existence of a still richer phase diagram in the
U −x plane. Not surprisingly, in the range of U for which there is pair-binding on the single
square, there arises a substantial portion of this phase diagram in which the ground state is
a d-wave superconductor - although as a consequence of the reconstructed band-structure
implied by the four-site unit cell, the line of nodes fails to intersect the Fermi surface and
hence the quasiparticle spectrum is fully gapped. In addition, there is a variety of possibly
insulating charge and spin density wave states, and several distinct Fermi liquid phases
among which is one with spin- 3

2 charge e quasiparticles (which is thus not adiabatically
connected to any free electrons state) and one with quasi-particles with spin- 1

2, charge e,
and an additional orbital pseudo-spin 1

2.

8
Arovas et al.

## Page 9

4. One dimension

In a tour-de-force of mathematical physics, the 1d Hubbard chain was exactly solved by
the Bethe-ansatz method2 (35).
For this as well as more general 1d problems, such as
the Hubbard model on various relatively narrow width ladders and cylinders, much more
is known than for higher dimensional cases. Particularly powerful numerical methods can
be deployed, as discussed in § 6.1 below.
In addition, a weak-coupling renormalization
group (RG) - known colloquially as “g-ology” in reference to the various couplings ga -
leads to a rich set of results involving multiple “intertwined orders” in the sense that the
interactions that promote charge-density-wave, spin-density-wave, and singlet and triplet
superconducting correlations evolve in a complex, interrelated fashion under RG.
Moreover, at long distances and low energies, the properties of all such 1d systems
are describable by a limited set of free boson conformal ﬁeld theories, i.e. the physics is
that of a small number of weakly interacting, linearly dispersing bosonic collective modes.
Distinct quantum phases of matter are generically classiﬁed by possible discrete broken
symmetries, and by the number of gapless modes (i.e. the “central charge”) and the quantum
numbers (spin, charge, crystal-momentum) associated with each such mode (36, 37). The
relation between the microscopic fermionic degrees of freedom and the bosonic modes,
called “bosonization”, can be complicated in speciﬁc cases, but is in principle understood
in general.
Other than some of the numerical results, this intellectual block is relatively old and
well known - much of it dating from the 1970’s - and so will not be reviewed here. For a
modern treatment, see ref. (38).

5. Asymptotically exact results in special limits

5.1. Weak coupling limit

5.1.1. Background. In this section, we consider the instabilities of the Hubbard model in
d > 1 in the weak-coupling limit U/t ≪1. The goal is to express the properties of the
system starting from the band structure that results from diagonalizing the Hamiltonian
with U = 0.
Corrections to all quantities can be expressed as an asymptotic series in
U/t. Clearly, at zero temperature, the radius of convergence of this series is zero, since
the behavior is qualitatively distinct for U/t →0−and U/t →0+: When U/t →0−, BCS
mean-ﬁeld theory is asymptotically exact, and there is a superconducting instability below
a characteristic scale Tc,−∼exp [−1/(ρ|U|)], where ρ is the density of states at the Fermi
energy. The superconductivity is described by an order parameter ∆, which has only one
sign on the entire Fermi surface, so that ⟨∆⟩FS ≃max(∆)FS, where ⟨•⟩FS denotes an average
over the Fermi surface. Such a superconducting state is termed “conventional” as it arises
in many elemental metals where the pairing mechanism is the electron-phonon coupling.
When U/t →0+, as we now argue, there is also a superconducting instability, but with two
qualitatively diﬀerent features. First, the superconductivity itself sets in below a parametri-
cally lower scale Tc,+ ∼exp

−1/(αρ2U 2)

≪Tc,−, where α is an order unity constant that
depends on the entire band structure of the system. Second, the superconducting behavior
is “unconventional” in the sense that ⟨∆⟩FS ≪max(∆)FS.

2The Bethe Ansatz solution allows to calculate the spectrum and the many-body eigenstates of
the one-dimensional Hubbard model. Calculating correlation functions is more diﬃcult.

www.annualreviews.org • The Hubbard Model
9

## Page 10

These distinctions imply that the ground states on either side of U/t = 0 are not adi-
abatically connected. The point U/t = 0 is a peculiar multi-critical point corresponding
to a free Fermi gas. These sharply distinct asymptotic behaviors are also more directly
manifest in perturbation theory at ﬁnite frequency: a subclass of perturbative corrections
represented diagrammatically by ladders in the particle-particle (BCS) channel are loga-
rithmically divergent so long as either time-reversal symmetry or inversion symmetry are
present in the normal state.
In a seminal paper, Kohn and Luttinger (KL) (39) explored how superconductivity
arises from repulsive interactions.
They considered a 3d electron gas with weak short-
ranged repulsive interactions, for which they identiﬁed an instability to an unconventional
superconducting state with non-zero Cooper pair angular momentum. In particular, they
emphasized the role played by Friedel oscillations associated with the existence of a sharp
Fermi surface. Below, we provide a modern discussion of the problem in the language of
the renormalization group (RG), and show that (in contradistinction to the KL analysis)
the structure of the particle-hole susceptibility at all energy scales, not just close to the
Fermi level, dertermines the superconducting instabilities (40, 41). For a recent reviews on
superconductivity from repuslive interactions, consult Refs. (5, 42) and references therein.

5.1.2. The Fermi liquid ﬁxed point. We ﬁrst summarize the basic results of the RG formu-
lation of Landau Fermi liquid theory, pioneered by Polchinski (43) and by Shankar (44),
which will be invoked in the discussion that follows. To keep things simple, we will present
the key results for a rotationally-invariant Fermi surface. The generalization appropriate
for anisotropic Fermi surfaces, relevant to crystalline systems, is discussed below.
Instead of attempting to derive a Fermi liquid from microscopics, the strategy is to
proclaim a ﬁxed point of the RG and then to analyze its stability. The ﬁxed point theory is
similar to the action S0 in imaginary time of a free-Fermi gas in d-dimensions with chemical
potential µ and energy dispersion E(k):

S0 =
X

α=↑,↓

Z
ddk dω
(2π)d+1 ¯ψk,ω,α
iω −E(k) + µ

ψk,ω,α .
9.

We retain frequency modes |ω| less than a UV cutoﬀΛ ≪EF (having “integrated out”
higher energy modes) and thus can linearize the dispersion as E(k) = µ + vFk⊥+ · · · . We
express the measure as ddk = kd−1
F
dk⊥dΩk, where dΩk is a solid angle element on the Fermi
surface, k⊥is the direction of momentum perpendicular to the Fermi surface, and vF is the
magnitude of Fermi velocity. Redeﬁning fermion ﬁelds as ψk,ω →k(d−1)/2
F
ψk,ω , we arrive
at the ﬁxed point action for a Fermi liquid:

Λ
Z

dω
2π
dk⊥dΩk

SF L =
X

α=↑,↓

−Λ

(2π)d
¯ψk,ω,α
iω −vFk⊥

ψk,ω,α .
10.

The stability of the Fermi liquid ﬁxed point is determined by power counting from
which one learns that: (i) a constant shift to the kinetic energy is relevant but harmless,
as it amounts to a shift in the chemical potential, and (ii) all higher derivative corrections
to the kinetic energy are irrelevant, and hence the kinetic energy is governed by a single
parameter, the Fermi velocity vF.
Next we similarly analyze the role of interactions. A key observation is that generic
4-fermion interactions (and all higher order interactions) are irrelevant at the Fermi liquid

10
Arovas et al.

## Page 11

ﬁxed point, due to the phase space restrictions imposed by the Pauli principle and the
Fermi surface. This result explains in large part the ubiquity of Fermi liquids in nature
(the prime example being liquid helium-3) despite the presence of strong interactions in
real systems. Only under two special kinematic circumstances are interactions important.
First, forward scattering interactions are exactly marginal, and are incorporated into the
Landau parameters.
Second, the dimensionless BCS interaction Vℓ, where ℓlabels the
pairing channel3, is marginal only at tree-level: one-loop corrections are logarithmically
divergent. (This is directly related to the properties of the particle-particle ladders that lead
to the Cooper instability for negative U discussed above.) Attractive (repulsive) interactions
are marginally relevant (irrelevant). This is captured by the BCS β-function, obtained by
promoting Λ to a running scale Λ = Λ0 exp(−t), and obtaining the ﬂow of the coupling:

β = dVℓ

dt = −V 2
ℓ
.
11.

Thus, repulsive BCS interactions (Vℓ> 0) weaken and attractive interactions grow, even-
tually leading to the BCS instability.
At this point, it may seem that the KL instability is absent since we have just concluded
that the metal is stable for repulsive interactions. However, a system with short-ranged
repulsive interactions can have eﬀective attractive interactions in some pairing channel ℓ, in
which case the β-function in that channel would indicate a superconducting instability. In
the case of the Hubbard model, the bare repulsive U enters only the s-wave BCS channel
and is orthogonal to unconventional pairing channels (e.g. d-wave, p-wave, etc.). But as
we integrate out high energy modes, we induce attractive interactions in unconventional
pairing channels (45), and the dominant one among these leads to a superconducting state.
The proper description of such eﬀects involves a two-step renormalization group analy-
sis (46). In the ﬁrst step, we integrate out modes in a weakly interacting metal to obtain
a description along the lines of the ﬁxed point theory above. Then, what were formally
repulsive interactions at short-distances may manifest themselves as attractive interactions
in certain pairing channels. In the second step, the RG ﬂow of such couplings determines
the superconducting instabilities.

5.1.3. Two-step Renormalization group for the Hubbard model.
Mode elimination: Lattice electrons governed by the Hubbard model are far from any
RG ﬁxed point, and thus any perturbative RG in this regime is meaningless. To overcome
this apparent obstacle, we integrate out the high energy degrees of freedom perturbatively,
which is well-controlled in the weak-coupling limit. This is the ﬁrst step of the analysis.
Upon doing so, we obtain a low energy eﬀective theory consisting of modes within an
energy cutoﬀΛ0 ≪EF . Generically, the eﬀective ﬁeld theory is of the Fermi liquid form
described earlier, appropriately generalized to account for crystalline anisotropy. All salient
microscopic details (e.g., lattice symmetry, ﬁlling, etc.) are encoded in the shape of the
Fermi surface, the magnitude of the Fermi velocity as a function of position on the Fermi
surface, and the marginal perturbations of the Fermi liquid, namely the Landau parameters
and BCS couplings. The choice of the cutoﬀΛ0 is largely arbitrary. It should be suﬃciently
small that the quasiparticle dispersion can be linearized, but it cannot be exponentially small

3In a rotationally invariant system, ℓcorresponds to the angular momentum channel.
More
generally, ℓlabels the irreducible representation of a crystallographic point group.

www.annualreviews.org • The Hubbard Model
11

## Page 12

in the couplings, where perturbation theory breaks down, as we noted above. Importantly,
the ﬁnal results should not depend on the choice of Λ0.
At the end of the ﬁrst step, we thus obtain an eﬀective Hamiltonian of Fermi liquid form
Heﬀ= H0+HBCS where H0 is the kinetic energy keeping just the linearized dispersion about
the Fermi energy and

2
X

HBCS = −1

k,k′
Γα,β;γ,δ(k, k′) ψ†
k,α ψ†
−k,β ψ−k′,γ ψk′,δ
.
12.

When the system of interest has spatial inversion symmetry (“parity”), the BCS kernel
above decouples into even and odd parity channels. Constraints from the Pauli-principle
require that without spin-orbit coupling even (odd) parity solutions have spin zero (one):

Γα,β;γ,δ(k, k′) = Γs(k, k′) (δαγ δβδ −δαγ δβδ) + Γt(k, k′) (δαγ δβδ + δαδ δβγ)
,
13.

where the subscripts s(t) denote “singlet” (“triplet”). At weak coupling, these quantities
can be expressed as an asymptotic series in U/t:

Γs(k, k′) = 1

2U + 1

Γt(k, k′) = 1

4U 2 
χ(k + k′) + χ(k −k′)

+ O(U 3/t2)

4U 2 
χ(k + k′) −χ(k −k′)

+ O(U 3/t2)
.
14.

The quantity χ(k) is the non-interacting static particle-hole susceptibility, where from di-
mensional analysis it follows that χ ∼1/t. It is important to observe that the strength of
the interaction involves both large and small momentum transfers on the Fermi surface and
the full structure of the susceptibilities χ determine the eﬀective interaction, not just the
subtle non-analyticities of χ associated with the sharpness of the Fermi surface.
RG ﬂow: Having obtained the low energy eﬀective Hamiltonian we now proceed to
analyze the RG ﬂow of the BCS couplings. We deﬁne a dimensionless Hermitian matrix
g(kF, k′
F), which is the eﬀective interaction Γ(kF, k′
F) deﬁned above, evaluated on the Fermi
surface and weighted by the density of states in the neighborhood of the Fermi points kF, k′
F:

g(kF, k′
F) =
AF
(2π)d
Γ(kF, k′
F)
q

vF(kF) vF(k′
F)
,
15.

where AF =
R
dkF is the (d −1)-dimensional “area” of the Fermi surface. The RG ﬂows
are computed by promoting the cutoﬀΛ0 to a running scale Λ →Λ0 exp(−t), and the RG
equation obeyed by g is the convolution

dg(kF, k′
F, t)
dt
= −
Z dpF

AF
g(kF, pF, t) g(pF, k′
F, t)
.
16.

It is most convenient to analyze the RG ﬂows in the representation where g is diagonal. Dis-
tinct eigenstates correspond to, but are not fully speciﬁed by an irreducible representation
(irrep) of the crystalline point group, where
Z dk′
F
AF
g(kF, k′
F) ψℓ(k′
F) = λℓψℓ(kF)
.
17.

Here, ψℓ(kF) is normalized such that
R
dkF |ψℓ(kF)|2 = AF. Distinct eigenvalues do not
mix under RG (within the one-loop approximation), and the BCS β-function for each λℓis
identical in form to Eq. (11).

12
Arovas et al.

## Page 13

Thus, positive eigenvalues (corresponding to repulsive eﬀective interactions) weaken
and negative ones grow.
The ﬁrst eigenvalue to grow to be of order unity indicates an
instability of the Fermi liquid towards the corresponding superconducting state. That the
bare Hubbard repulsion can generate eﬀective attractive interactions in unconventional
pairing channels is the key result of the two-stage RG analysis.
In practice, one discretizes the points on the Fermi surface, and solves the resulting
discrete eigenvalue problem to ﬁnd the dominant eigenvalues. This way, the most important
features of the band structures determine the marginal BCS couplings and the dominant
instabilities.
Fig. 1 shows the result for the square lattice Hubbard model with second
neighbor hopping t′ = 0 (a) and t′ = −0.3t (b). One sees that the dominant instability of
the system in the weak-coupling limit is to a d-wave superconductor near half-ﬁlling. In
a similar fashion, one can study lattice systems of other geometries (47, 46, 48). Among
other things, Ref. (48) found a plotting error in Ref. (46). Figs.1c and 1d shows results for
the triangular and honeycomb lattices respectively with only nearest-neighbor hoppings.
Again, near half-ﬁlling, the dominant instability is to d-wave pairing, but in this case
this corresponds to a two dimensional irrep, i.e. a combination of dx2−y2 and dxy pairing.
Determining which combination of these two components is preferred in the ordered state
is beyond the scope of the RG treatment, but since the eﬀective couplings are weak, this
can be addressed within the context of BCS mean-ﬁeld theory.
As a consequence, one
expects the corresponding superconducting state to be the time-reversal symmetry breaking
combination generally referred to as d± id, although a nematic d-wave superconductor (i.e.
a real combination of dx2−y2 and dxy) is also possible.
Cutoﬀ-independence: A crucial observation made in ref. (46) was that the resulting
scale associated with superconductivity is independent of the arbitrary choice of cutoﬀ, Λ0.
Indeed, the only characteristic scale, namely the bandwidth W determines the supercon-
ducting instability: Tc ∼W exp
−1

αρ2U 2
, as alluded to earlier. While the details of
the proof of cutoﬀindependence can be found in ref. (46), we provide here some intuition
for why this has to be the case.
The main requirement for cutoﬀindependence is that
the Fermi liquid ﬁxed point be the only nearby ﬁxed point. This is certainly true in the
weak-coupling limit.
Let us consider two diﬀerent mode elimination schemes: (i) eliminating modes above
the scale Λ0, and (ii) eliminating all modes above Λ1 < Λ0. The only assumptions on the
cutoﬀs are that W exp(−1/ρU) ≪Λ1 < Λ2 ≪U 2/t. In the scheme with initial cutoﬀ
Λ1, we have “less RG time” t for attractive BCS couplings to grow than the scheme with
initial cutoﬀΛ0. But this discrepancy is precisely compensated by the fact that the eﬀective
attractions start oﬀbeing larger in the scheme with Λ1, which is obtained by integrating
the β-function in Eq. (11) between Λ0 and Λ1.
The presence of other nearby ﬁxed points, or of additional modes (e.g., phonons,
magnons, etc.) introduce additional scales and the cutoﬀindependence is then no longer
guaranteed.
There is a corollary to this absence of any characteristic scales other than
the bandwidth in the weak-coupling limit: associating a ‘pairing glue’ of a well-developed
bosonic ﬂuctuation spectrum, while tempting, is strictly incorrect. Instead, the electronic
ﬂuctuation spectrum itself, at all momentum scales ranging from the lattice scale down to
the longest length scales, is responsible for pairing.

5.1.4. Extensions. In the weak-coupling limit of the Hubbard model in d > 1 the Fermi
liquid state is generically unstable only to superconductivity. It is typically necessary to

www.annualreviews.org • The Hubbard Model
13

## Page 14

Figure 1

Dominant pairing eigenvalues λ (deﬁned in Eq. 17) as a function of n the density per site in the weak-coupling limit of the
Hubbard model on a square lattice (a-b) with second-neighbor hopping t′ = 0 (a), t′ = −0.3t (b), and (c) a triangular
lattice and (d) a honeycomb lattice, both with only nearest-neighbor hopping. The eigenvalues have been scaled by a
factor of 5 in (d) for clarity. The dominant pairing on a square lattice near half-ﬁlling has dx2−y2 symmetry (labeled
x2 −y2) for both t′ = 0 and t′ = −0.3t. On the triangular and honeycomb lattices, a two-dimensional irreducible
representation with d-wave symmmetry, labeled {x2 −y2, 2xy}, is favored when the Fermi surface is electron-like and
simply connected. By contrast, a solution with f-wave symmetry, labeled y(y2 −3x2), sets in near the van Hove ﬁlling,
and in the regime where there are two hole-like Fermi pockets centered at the zone corners. The f-wave symmetry
corresponds to a nodeless gap function with relative phase of π between the two hole pockets. Solutions with p-wave
symmetry, labeled {x, y}, also occur in (b-d) in a narrow sliver of energy about the van Hove ﬁlling. This occurs when
n ≈0.73 in (b) n = 1.5 in (c) and n = 0.75 in (d). The ﬁgures were obtained by discretizing the Fermi surfaces at each
density with a grid of 120 points. Care must be taken in the vicinity of the van Hove ﬁllings.

treat the model at intermediate or strong coupling to access non-superconducting orders,
for instance using the large-N or numerical approaches discussed below. To access such
orders within the weak-coupling limit, one has to consider non-generic band structures,
such as those that produce a perfectly nested Fermi surface or a case in which the Fermi
surface crosses a 2d van Hove singularity (vHS). While these are ﬁne-tuned cases, they bring
the interplay between superconductivity and the tendency towards other broken symmetry
phases into the weak-coupling regime (49).
Considerable eﬀort has been devoted to such problems.
For instance in the case of
Fermi surfaces crossing a 2d vHS, the problem has been studied in straight pertubation
theory, ﬁrst by Dzyaloshinskii (50) and Schulz (51), who concluded that the most singular
tendency was towards superconductivity. A more sophisticated scaling theory near 2d vHS
has remained elusive, as one must contend with the existence of log-squared divergences
in the Cooper channel along with log divergences of forward scattering interactions. The
interplay between these eﬀects lead to RG equations that explicitly depend on the energy
scale and hence are useless when it comes to constructing asymptotic behavior of correlation
functions. For a review, see ref. (49).
As already mentioned, the weak coupling RG in 1d is quite diﬀerent than for d > 1.
However, in special cases, such as for the case of quadratic band-touching in 2d, the RG
equations have similar form as in one dimension4 (54, 55). As in the usual FL, in these

4This also applies for quadratic band-touching in 3d with appropriate long-range forces (52, 53).

14
Arovas et al.

## Page 15

cases there are a number of interactions - represented by a set of running coupling constants,
ga(t), that are marginal (dimensionless) by power counting. To lowest non-trivial order,
this leads to a perturbative expression for the RG ﬂows (analogous to that in Eq. 16) of
the form

dga

dt = Γb,c
a gb gc + . . .
,
18.

where summation convention is assumed, and the remaining terms are of third order and
higher. The important point is that the tensor quantity Γ which reﬂects physics of the
speciﬁc system being studied, generally intertwines the various diﬀerent interactions in a
non-trivial fashion.
Depending on the speciﬁc problem being studied, and the bare values of the interactions,
there are two diﬀerent sorts of behavior solutions of this equation can exhibit.
Under
some circumstances, the interactions are all marginal or marginally irrelevant, i.e. some
combinations of g’s ﬂow to zero and others do not change under RG (at least to this
order). More usually, there are some set of interactions that are marginally relevant. In
this case, the RG ﬂows carry the system to a “ray” along which the interactions continue
to grow until, no matter how weak the bare interactions, a point is reached at which the
perturbative treatment breaks down. At this point, other methods must be employed to
solve the problem. The possible rays can be identiﬁed (56) by looking for possible solutions
of the form ga(t) = Ga(t∗−t)−1, where Ga are solutions of the set of quadratic equations

Ga = −Γb,c
a Gb Gc
.
19.

Those couplings for which Ga ̸= 0 grow strongly toward strong-coupling under the RG ﬂow,
while any coupling for which Ga = 0 remains relatively weak. Such a runaway ﬂow of some
of the coupling constants typically signals the opening of an interaction-driven gap, often
associated with spontaneous symmetry breaking.
Despite the fact that these results apply (in d > 1) only for ﬁne-tuned band-structures,
they may be useful over some range of intermediate energies and/or temperatures if the ﬁne-
tuned conditions are approximately satisﬁed, especially if one extrapolates the results to
intermediate coupling strengths. We refer the reader to the literature for further discussion
of these ideas (55, 57, 58).

5.2. Strong coupling limit

When the density of electrons per site is n = 1, the low energy physics in the strong coupling
limit of the Hubbard model is, famously, that of the corresponding spin- 1

2 Heisenberg anti-
ferromagnet, with exchange coupling 4 |tij|2/U . This applies whether the lattice is regular
or irregular. At the same time, the system is a “Mott” insulator in the simple sense that
the insulating gap

∆c = 1

2U + O(t)
20.

is determined by the interaction strength and has no relation to any ordering phenomena
that occur below temperature scales of order J.
Needless to say, the physics of quantum antiferromagnets is a rich topic in its own right.
Depending on the lattice structure, the range of the exchange interactions, and the degree
of disorder, strong evidence exists for the existence of various forms of antiferromagnetic

www.annualreviews.org • The Hubbard Model
15

## Page 16

ordered phases (colinear, coplanar, non-coplanar, commensurate or incommensurate, chiral
or non-chiral, etc.), spin-Peierls phases, nematic and spin nematic phases, quantum spin
liquid phases of various ﬂavors, spin-glasses, random singlet phases, and surely others.
For n < 1, the low energy physics (e.g., the equilibrium properties the system at tem-
peratures T ≪U/2) is governed by a version of the famous t-J model

i,j
Jij

Si · Sj −1

i,j
tij ˆBij +
X

Ht−J = −
X

4 ˆni ˆnj

−
X

i,j,k
Kijk ˆ∆†
ij ˆ∆jk + O
t3/U 2
, 21.

where ˆBij = c†
i↑cj↑+ c†
i↓cj↓, ˆ∆ij = 2−1/2
ci↑cj↓+ cj↑ci↓

, and Kijk = 2tijtjk/U, and
where it is understood that Ht−J operates in a restricted Hilbert space in which no site is
doubly occupied. This model is often studied in its own right (typically neglecting the term
proportional to K) and, so long as Jij < |tij|, the results are often taken as representative
of results for the Hubbard model in some physically reasonable range of Ueﬀ∼4t2/J.
However, strictly speaking, the mapping to the t −J model is valid only in the asymptotic
limit Jij/tij →0.
Thus, truly in the strong coupling limit, one should begin with the solution of U →∞
problem, i.e. the t−J model with Jij = Kijk = 0, and only keep corrections due to non-zero
J and K as small perturbations. The Hubbard model was originally introduced to study
itinerant ferromagnetism, based on the fact that this occurs in Hartree-Fock approximation
so long as the “Stoner” criterion is satisﬁed, Uρ(EF) > 1. However, more accurate numerical
studies have found that ferromagnetism in the Hubbard model on a bipartite lattice with
|A| = |B| seems to require Uρ(EF) ≫1. To elicit ferromagnetism for U/t = O(1), it appears
necessary to introduce frustration in the form of further neighbor same-sublattice hoppings,
or to consider the model on non-bipartite lattices (59) or on line graphs (60, 61) at densities
away from half-ﬁlling.
Provided the kinetic energy satisﬁes the Perron-Frobenius condition (tij ≥0 for all
i and j), the problem with a single hole in a ﬁnite size lattice is governed by Nagaoka’s
theorem (see § 2), i.e. the ground state is a fully polarized ferromagnetic state. Clearly, the
limit U →∞and N →∞do not commute. However, for large but ﬁnite U, the solution
in the thermodynamic limit can easily seen to be a “Nagoaka polaron.” Its nature can
be understood from a simple variational argument: Consider a state in which a region of
radius R has spins aligned ferromagnetically, while the rest of the system is in its n = 1
antiferromagnetic ground state. The variational energy of such a state is

ENag = −E0 + ¯tR−2 + ¯JRd
,
22.

j tij, and ¯t and ¯J are averages of tij and Jij that depend on the details of
the lattice structure and the assumed shape of the polaron; here, the second term is the
kinetic energy cost of conﬁning the hole in a region of size R and the third term is the
cost in exchange energy of making a ferromagnetic bubble. Minimizing this expression with
respect to R, we obtain an expression for the size and energy of the Nagaoka polaron:

where E0 = P

ENag = −E0 + 2¯tR−2 with RNag =
2¯t/d ¯J
1/(d+2)
.
23.

It is a straightforward exercise to go from the single polaron to the problem with a small
but ﬁnite hole density. The polaron should strictly be viewed as a new sort of quasi-particle
- one with charge e and spin S ∼Rd
Nag. Two such particles have a short-range eﬀective
attraction of order ¯tR−2
Nag; if two are placed adjacent to each other, the hole associated with

16
Arovas et al.

## Page 17

each polaron can now delocalize over twice as large a ferromagnetic region. Thus, there is a
tendency for polarons to agglomerate, i.e. for the system to phase separate. Opposing this
is the eﬀective Fermi pressure of the polaron gas – however, because the polaron is large,
its eﬀective mass is large,5 so the Fermi pressure is negligible. Thus, at T = 0 and for low
density of doped holes, 1 > n > nc, one expects macroscopic two-phase coexistence between
an undoped antiferromagnetic phase with n = 1 and a fully polarized ferromagnetic phase
with n = nc where nc ∼R−d
Nag. Correspondingly, for a range of densities n > nc but not too
small, this line of reasoning leads one to expect a half-metallic ferromagnetic phase, i.e. a
state with all the spins parallel to one another.
The stability of the fully spin-polarized state (known as a half-metallic ferromagnet) at
ﬁnite doped hole density has not been rigorously established. Indeed, it has been shown that
even for U = ∞, the fully polarized state is unstable beyond a (typically substantial) critical
doped hole density (62). However, exact diagonalization (63) and DMRG studies (64) of the
model on a square lattice (2d) provide strong corroborating evidence that the half-metallic
ferromagnetic phase is stable for U = ∞in the range of density 1 > n ≳0.8 and that two-
phase coexistence occurs at large but ﬁnite U in a range of density6 1 > n > nc ∼(t/U)1/2.
However, there is also indication that ferromagnetic phases arise only when U is extremely
large, U/t ≳100.
None-the-less, the existence of ferromagnetic phases at very large U
implies that, strictly speaking, the non-ferromagnetic states generally seen (and expected)
at intermediate values of U cannot be approached from a strong-coupling perspective.

5.3. Dilute limit

The dilute limit of the Hubbard model is deﬁned by ﬁxing U/t and letting n →0. In this
limit, strong arguments have been put forward that in d = 2 and 3 and for positive U,
the system forms a Fermi liquid (which may have a superconducting instability at very low
temperatures, to be discussed below).
Consider d = 3 ﬁrst. Using the ﬁlled Fermi sea as a trial state, the kinetic energy per
particle scales as EKE ∼t n2/3 (where we have used the eﬀective mass approximation near
the band bottom), whereas the typical interaction energy satisﬁes EPE ∼Un. Thus, in the
limit n →0, EK ≫EPE. One may therefore expect the system’s properties to be calculable
in an expansion in the small parameter (U/t) · n1/3 (which plays a similar role to that of rs
in a uniform electron gas). As explained in Refs. (65, 66, 67), the proper small parameter is
actually kFas, where kF ∝n1/3 and as is the scattering length. For small U/t, the scattering
length satisﬁes as ∼a (U/t) (where a is a lattice constant).
In d = 2, the situation is more subtle, since the above argument gives that EKE/EPE
is density independent. However, a more careful treatment (outlined below) shows that
in this case the two-particle scattering amplitude near the Fermi energy, propotional to
1/ ln(1/n), serves as an emergent small parameter (66). Thus, in both cases, a systematic
expansion starting from the Fermi gas is possible, resulting in a Fermi liquid whose Landau

5Relative to the band mass, the Nagaoka polaron can readily be seen to have has an eﬀective
mass enhancement of order (¯t/ ¯J)Rd−1
Nag. This is since moving the polaron involves ﬂipping spins
along its entire surface.
6It is a peculiarity of the Hubbard model that there is no interaction between electrons with the
same spin – thus, for any value of n, all energy eigenstates with maximal total spin are simply Slater
determinants. In particular the half-metallic ferromagnetic ground state is always an eigenstate of
the Hubbard Hamiltonian - the only question is under what circumstances it is the ground state.

www.annualreviews.org • The Hubbard Model
17

## Page 18

parameters are parametrically small in the n →0 limit.
To arrive at the expansion appropriate for the dilute limit, we examine the diagrammatic
representation of the two-particle vertex function. The dominant terms are the ones that
form the ladder series [Fig. 2(a)]. Summing the ladder series gives the eﬀective two-particle
interaction (also known as the T-matrix):

Ueﬀ(q, ϵ) =
U
1 + Γ0(q, ϵ) U
,
24.

where Γ0(q, ϵ) =
R
ddk
(2π)d (εk + ε−k+q −iϵ)−1. In the dilute limit, we are interested in the
interaction at momenta and energies of the order of the Fermi momentum and Fermi energy,
respectively. In d = 3, we can safely take |q| →0 and ϵ →0, obtaining Γ0 ∼1/t. Terms
that are not part of the ladder series, such as those shown in Fig. 2(b,c), are suppressed by
powers of ρUeﬀ∼kFas, and are thus small. The eﬀective interaction near the Fermi energy
is thus ﬁnite in the dilute limit. The Fermi liquid parameters, such as the Landau function
and the eﬀective mass correction, are all of the order of kFas (since they are proportional
to ν0 ∝kF). The smallness of the Fermi liquid parameters ensures the self-consistency of
the expansion.
In d = 2, Γ0 diverges logarithmically in the limit |q| →0, ϵ →0. This divergence is
cut oﬀby setting |q| ∼kF, ϵ ∼µ, where µ is the chemical potential. In the dilute limit,
such that (U/t) ln(1/n) ≫1, this gives Ueﬀ∼t/ ln(t/µ) ∼t/ ln(1/n). Hence, terms that
are not part of the ladder series are suppressed by a factor ρUeﬀ∼1/ ln(1/n) ≪1, and can
be neglected (66). The Fermi liquid parameters are small in proportion to 1/ ln(1/n).
In both d = 2 and d = 3, the system is thus described as a weakly interacting Fermi liq-
uid in the dilute limit, independently of the original Hubbard interaction. The Fermi liquid
state can then be treated as discussed in § 5.1. In d = 3, and in the presence of time reversal
or inversion symmetries, one expects an instability towards a triplet superconducting state
whose critical temperature Tc scales as

EF e−1/(ρUeff)2 ∼t n2/3 exp
n
−
1 + t

U
2 n−2/3o
,
25.

where we have omitted dimensionless numbers of the order of unity in the exponents. The
d = 2 case requires additional care, since the Lindhard susceptibility is nearly momentum
independent. Hence, no eﬀective attraction is generated at second order in Ueﬀ. A calcu-
lation of the third order terms, performed in ref. (68), gives Tc ∼EF exp

−1/(ρUeﬀ)3
∼
t n exp

−1/ ln3(1/n)

. Note that in both d = 2 and 3, Tc ≪EF .

5.4. Large-N generalization and the Hartree Fock approximation

5.4.1. A large N limit. While quantum many-body models are generally insoluble except
in very special cases, by extending the global symmetry of the model from SU(2) to a larger
group such as SU(N) or Sp(N), a systematic expansion in powers of 1/N about the N →∞
limit can often be derived (69, 70, 71, 72, 73, 74). Here, we discuss a large-N generalization
of the Hubbard model (75) that allows controlled access to a variety of intermediate-coupling
spin and charge ordered phases. Consider the Hamiltonian

N
X

m=1
c†
iαm
tij + µ δij

cjαm + 1

1

H = −
X

X

X

2KΨ†
iΨi

,
26.

2V n2
i −1

2JS 2
i + 1

N

α=±

i

⟨ij⟩

18
Arovas et al.

## Page 19

Figure 2

(a) Ladder series for the two-particle scattering amplitude in the dilute limit. The empty square
represents the bare interaction U, and the ﬁlled square is the eﬀective interaction Ueﬀ(also known
as the T matrix). (b,c) Examples of diagrams which are not part of the ladder series. These
diagrams are suppressed comapred to those shown in panel in the n →0 limit (a) (see text).

where i labels the lattice sites, α = ± the spin polarization, and m ∈{1, . . . , N} is a ‘ﬂavor’
index. The coupling constants V , J, and K are all non-negative. The local density ni, spin
Si, and superconducting order parameter Ψi are given by

α,m
c†
iαmciαm
,
Si = 1

ni =
X

α,β,m
c†
iαm σαβ ciβm
,
Ψi =
X

X

2

α,β,m
ciαm ϵαβ ciβm
,
27.

where ϵαβ = iσy
αβ. Consider a global transformation of the fermion ﬁelds

ciσm →eciσm = Rmm′ Uσσ′ ciσ′m′
.
28.

Suppressing the site index i, we write ˜c = R U c, where R acts on ﬂavor indices and U acts
on spin indices. Thus,

en = c†
σm (R†R)mm′ (U†U)σσ′ cσ′m′
eSa = 1

2 c†
σm (R†R)mm′ (U†σa U)σσ′ cσ′m′
eΨ = (RtR)nn′ (Utϵ U)σσ′ cσn cσ′n′
.

29.

Thus if U ∈SU(2) and R ∈O(N), we have en = n, eΨ = Ψ, and furthermore eSa = Mab Sb,
where Mab = 1

2 Tr
U† σa U σb
∈SO(3). Hence, e
H = H, i.e. the Hamiltonian H possesses a
global U(2) × O(N) symmetry (including the U(1) charge conservation). In the case N = 1,
the system reduces to the usual Hubbard model with U = V + 3

4J + 2K.
To elicit the large-N theory, we employ three Hubbard-Stratonovich transformations to
decouple each of the three terms quartic in the fermion operators. The resulting dimen-
sionless action is then

 N

β
Z

2K |∆i|2

+
X

2V φ2
i + N

2J χ2
i + N

0
dτ
X

A =

i

i,j
σ,m


¯ciαm ciαm

iφi δαβ + 1

¯ciσm
∂τ −tij −µδij

cjσm

30.

!
ciβm
¯ciβm

!

2χi · σαβ
i∆i ϵαβ
i ¯∆i ϵαβ
−iφi δαβ −1

−1

X

X

2

i,m

α,β

.

2χi · σαβ

Here β = 1/kBT where T is the temperature, τ is imaginary time, and

φi, χi, Re ∆i, Im ∆i

are the six time-dependent Hubbard-Stratonovich ﬁelds.

www.annualreviews.org • The Hubbard Model
19

## Page 20

We may now formally integrate out the fermions, obtaining the following eﬀective action:

 N

β
Z

2V φ2
i + N

2J χ2
i + N

0
dτ
X

Aeﬀ=

i

2K |∆i|2

−1

2N Tr log G−1[{φi}, {χi}, {∆i}]
. 31.

Here, G−1 = G−1
0
−M[{φi}, {χi}, {∆i}], where

G−1
0
=

G−1
0
0
0
−
G−1
0
T

!

.
32.

The inverse of the free Green’s function is given by G−1
0
= −∂τ + tij + µδij, and M is the
matrix that appears in the second line of Eq. (30).
Crucially, the eﬀective action is proportional to N. Hence, in the large N limit, the par-
tition function is dominated by the lowest-action saddle point of Aeﬀ. Fluctuations around
the saddle point are suppressed by powers of N −1. We seek a saddle point characterized
by time-independent, but possibly site-dependent ﬁelds φi and χi. Since we have assumed
K ≥0, it is straightforward to see that ∆i = 0 at any such saddle point. Substituting
eφi ≡iφi and diﬀerentiating the eﬀective action with respect to eφi and χi yields:

eφi = −V
X

α,m

2J
X

χi = 1

α,β,m

¯ciαm ciαm

eφi,χi

eφi,χi
.
33.

¯ciαm σαβ ciβm

Here, the expectation value is taken with respect to the quadratic action (30) with {eφi}, {χi}
set to their saddle point values. Eqs. (33) are the self-consistent Hartree-Fock (HF) equa-
tions describing possible spin and charge ordered states. They are identical to the HF equa-
tions of the one-band Hubbard model with 2V = 1

2J = U, K = 0. Thus, the Hartree-Fock
approximation becomes asymptotically exact in the large-N generalization of the Hubbard
model given by Eq. (26).7

5.4.2. Some Hartree-Fock results. There have been numerous Hartree-Fock studies of the
Hubbard model. A priori - especially when dealing with forms of order that only arise when
U exceeds a ﬁnite critical value - there is no obvious small parameter that justiﬁes these
solutions. However, with the large N limit as justiﬁcation, it is worth summarizing at least
some of the Hartree-Fock results that have been obtained in this way.
In the case of a half-ﬁlled band, n = 1, with t′ = 0, the Fermi surface is perfectly nested
and the HF ground state is a N´eel antiferromagnetic insulator for all U > 0. In particular,
for d > 2 and small U, the sublattice magnetization, m, and the quasi-particle gap, ∆AF ,
depend on U as m ∼∆AF ∼exp(−1/ρU), while for d = 2 the expressions are slightly
more complicated, with m ∼∆AF ∼exp
−
p

8π2t/U

, because of the logarithmically
divergent density of states associated with the van-Hove points. For small but non-zero
t′, the system remains metallic for U < Uc but is antiferromagnetic for larger U, where

7Interestingly, setting N = 1, this choice of parameters corresponds to a Hubbard model with
an interaction strength V + 3

4 J + K = 2U. This discrepancy between the Hartree-Fock equations
for the Hubbard model and the saddle point equations obtained by decoupling the interaction in
an SU(2) symmetric way was noted in Ref. (76).

20
Arovas et al.

## Page 21

Uc ∼t/ ln |t/t′| for d > 2 and Uc ∼t/ ln2 |t/t′| in d = 2. The details of the metal-insulator
transition as a function of U has not been exhaustively studied, and may vary depending on
dimensionality, the value of t′, and other details. The simplest cases involve either a direct
ﬁrst order transition from a featureless metal for U < Uc to an AF insulator for U > Uc, or
a sequence of two transitions, the ﬁrst (typically continuous) from a featureless metal for
U < Uc1 to an antiferromagnetic metal phase - i.e. with m small enough that a portion of
the Fermi surface remains ungapped - followed by a (typically ﬁrst order) transition to the
AF insulator at U > Uc2 > Uc1.
It is also interesting to consider the evolution of the HF ground state with the intro-
duction of a dilute concentration of doped holes, x ≡1 −n ≪1, starting from the AF
insulator. One possible solution of the HF equations is simply a doped version of the N´eel
state - here the energy cost per doped hole is ∆AF
n
1 + O(x2/d)
o
. This is typically never

the lowest energy HF solution (77); a better solution is one in which a portion of the sam-
ple is undoped AF and another is a non-magnetic metal with a ﬁnite concentration xc of
doped holes, where xc ∼ρ(EF) ∆AF. For small U in d > 2, it was shown in ref. (77) that

xc =
√

2 ρ(EF) ∆AF and that the energy per doped hole is 2−1/2∆AF
n
1 + O(x2/d
c
)
o
, i.e.

it has lower energy than the doped N´eel state. The same analysis applies for small t′ in
d = 2, and even for t′ = 0 with with slight complications due to the divergent density of
states. However, more interesting insulating “stripe” states were found (78, 79, 80) to have
still lower energies - at least in d = 2 with t′ = 0. Here for small x, the system forms
a unidirectional spin-density wave (SDW) state in which the doped holes are localized on
anti-phase domain walls a distance W apart, resulting in a new periodicity of the spin-order
λ = 2W. Moreover, the domain-wall spacing is such that there are an even-integer number
of electrons per unit cell, i.e. λ = 1/x, and the system remains insulating. From numerics
in 2d with t′ = 0, the energy per doped hole of the striped phase was estimated (81) to be
approximately 0.66 ∆AF, some 7% less than that of the phase separated state.

6. Numerical results

6.1. DMRG results for ladders and cylinders

The density-matrix-renormalization group (DMRG) approach (82, 83) has proven to be
extremely useful in obtaining ground state correlations of Hubbard cylinders and ladders.
As the computational eﬀort grows roughly linearly with the length of the system, L, but
exponentially with the number of legs, W, these results are largely conﬁned to rather small
W.
However, for these systems, it provides an incomparably versatile approach to the
intermediate coupling problem, without relying on any artiﬁcial limiting procedure.

6.1.1. The utility of DMRG . DMRG is now understood to be an extremely clever vari-
ational approach (84, 83) to studying the ground state properties of arbitrary interacting
electron models. It uses a class of variational states known as matrix-product states - which
as the name suggests are parameterized by the elements of a matrix associated with each
site. The larger the dimension of the matrices (known as the “bond dimension”), the better
the approximate ground state obtained. For any ﬁnite size system, DMRG calculations in
principle converge to the exact result for large enough bond dimension, Bd. However, as the
calculations are more demanding the larger Bd, not all published results can be taken at face
value. This is reﬂected in the unfortunate fact that there are examples in the literature of

www.annualreviews.org • The Hubbard Model
21

## Page 22

DMRG studies that have reached contradictory conclusions concerning the character of the
ground state phase of certain model problems. Moreover, diﬀerent sorts of results require
diﬀerent levels of care (85), as we elaborate below.

• Generally, the bond dimension required to achieve a given accuracy increases expo-
nentially with the degree of entanglement of the phases being explored. Thus, DMRG
results converge more easily in systems in which the central charge (the number of
gapless modes) is small and ones in which all correlation lengths are short. Con-
versely, systems with many gapless modes and/or long correlation lengths may need
a very large Bd to converge.
• Even within a given phase, the reliability of the DMRG results for ﬁxed Bd de-
pends, to some extent, on what questions are asked. The nature of the short-range
correlations – i.e. what sort of “local order” arises – is less sensitive to subtle as-
pects of the entanglement, and so can be extracted reliably even in calculations with
relatively modest values of Bd, while issues concerning long distance correlations –
especially power-law falloﬀof correlations associated with gapless modes – are much
more strongly dependent on Bd.

In quoting results of DMRG calculations, we have restricted ourselves to either dis-
cussing results that pertain to short-range correlations (about which there typically is no
disagreement), or to results in which the Bd dependence has been seriously investigated and
the extrapolation to Bd →∞appears convincing. There are also generalizations of DMRG,
such as projected entangled pair states (PEPS) (86), which uses tensorial generalizations of
the matrix product states of DMRG. Because these methods have not been as thoroughly
tested and benchmarked as has DMRG, we have largely omitted results obtained from these
approaches. DMRG methods have recently been extended and are beginning to be applied
to study dynamical properties of ladders and cylinders (87, 88). This is a very promising
new direction, but one that is still in its infancy. Again, taking a conservative stance, we
have mostly not reviewed these results either. (See, however, Ref. (89).)
The bulk of the DMRG studies have been carried out on ladder or cylinder versions
of Hubbard model for “intermediate” values of U of order the band-width, 8t ≤U ≤12t,
and for ranges of electrons per site n in the range 1.3 ≥n ≥0.7, corresponding to a
concentration of “doped holes” or “doped electrons” 0 ≤x ≤0.3. Eﬀects of diﬀering band-
structure have been studied largely by considering a range of ﬁrst and second neighbor
hopping, t′/t. Many studied have treated the t −J instead of the Hubbard model, because
the results for the former tend to have better convergence properties. Results so obtained
are generally interpreted as representative of the solutions of a corresponding Hubbard
model with U/t ≈(4t/J) and a somewhat renormalized value of t′/t.
We now summarize some of the salient results that have been obtained from these
studies. We distinguish three types of inferences that can be drawn:

1) Most directly, from an analysis of the short-distance behavior of various ground state
correlation functions, it is relatively straightforward to determine what sort of order-
ing tendencies are strong for particular ranges of parameters. We will illustrate such
orders by describing the form of broken symmetry (long-range order) that would
result were these short-distance correlations extended to long distances. Since the
Hubbard model is not a realistic model of any actual material, it may be that identi-
fying ordering tendencies reveals the most model independent - and hence physically

22
Arovas et al.

## Page 23

signiﬁcant - features of the interesting strong correlations physics.
2) Extrapolating the result to the limit of inﬁnitely long cylinders and ladders, we can
identify distinct phases of matter based on the asymptotic long-distance correlations.
As discussed in §4, this means identifying any discrete broken symmetries, and the
number and character of distinct gapless charge and spin modes; for instance, a
Luther-Emery liquid has a single gapless charge mode (central charge c = 1), and
power-law (QLRO) CDW and superconducting correlations.
3) Most speculatively, we can introduce conjectures concerning the extrapolation of the
DMRG results to the 2d (W →∞) limit. This can only be done with conﬁdence
when the results are weakly W dependent even for relatively small W.

6.1.2. The square lattice.

Undoped ladders: For the most part, studies of the undoped model (x = 0) have been
carried out in the regime in which U is (assumed) large enough that there is a substantial
charge gap, ∆c ≳t, so the Hubbard model is equivalent to a spin 1/2 Heisenberg model with
ﬁrst and second neighbor exchange couplings, J′/J = (t′/t)2. For even W, this necessarily
results in a fully gapped state (90, 91), i.e., with a non-zero spin-gap, ∆s.
However (92), for J′/J < Xc1 ≈0.41, the resulting state exhibits the same local spin
correlations as the N´eel state shown in Fig. 3a, and has a spin correlation length that
grows exponentially with W, i.e. ξs ∼exp(αW) with α = O(1).
Indeed, as shown on
theoretical grounds in ref. (91), in a range of J′/J in which the 2d system has long-range
antiferromagnetic order characterized by a renormalized spin-stiﬀnes ρs and a spin-wave
velocity c, α(J′/J) = 2πρs/ℏc. Thus, the DMRG results provide compelling evidence that
the 2d system has N´eel order in this regime, as shown in Fig. 3c.
For J′/J > Xc2 ≈0.62, the local order resembles the stripe magnetic state, shown
in Fig. 3b. While we have not found data that show the systematic scaling of ξs with
W, ∆s is a suﬃciently rapidly decreasing function of W up to at least W = 10 that it is
reasonable to conclude that stripe LRO arises in the W →∞limit. On the other hand, for
Xc1 < J′/J < Xc2, there is a spin-gap that does not decrease substantially with increasing
W. These results have led to the conjecture (93, 92) that for this intermediate range, there
is a quantum disordered phase or phases (i.e. phases with no magnetic order) in the W →∞
limit, as shown in Fig. 3c. However, there is still some debate (94) about the nature of this
region in the 2d limit, e.g., whether there is valence bond crystalline order or a Z2 quantum
spin liquid.
Lightly doped ladders: DMRG studies of the doped ladder have also primarily in-
volved U large enough that the undoped ladder is insulating, and have focused on the range
of parameters (i.e. J′/J < Xc1) which correspond to a doped N´eel antiferromagnet.
Naturally, the most reliable results have been obtained for the two-leg ladder, W = 2.
So long as x < xc ∼0.3, for the typical range of intermediate U and t′/t, there is general
consensus (95, 96, 97, 98) that, in the L →∞limit, such ladders generically form a Luther-
Emery liquid (99). Speciﬁcally, there is a non-zero spin-gap, ∆s ∼t2/U, a single gapless
charge mode (c = 1) and power-law equal-time CDW and SC correlations which fall as

cos(QCDWr + φ0)|r|−KCDW and |r|−KSC, respectively. The CDW ordering vector is equal
to the value of 2kF = Wπn mandated by the generalized LSM theorem (see § 2), QCDW =
Wπn ≡2πx and consistent with expectations from conformal ﬁeld theory, KSC = 1/KCDW.
While DMRG does not directly yield information concerning the susceptibility, once
the identiﬁcation with the corresponding quantum ﬁeld theory is established, it follows

www.annualreviews.org • The Hubbard Model
23

## Page 24

Figure 3

Forms of antiferromagnetic order in the undoped square lattice: a) N´eel, b) Stripe AF, c)
schematic phase diagram of the 2d model at large U as a function of J′/J ≡(t′/t)2

that these same exponents can be identiﬁed with the low T behavior of the corresponding
susceptibilities, i.e. χCDW(q = QCDW) ∼T −(2−KCDW) when KCDW < 2 and χSC(T) ∼

T −(2−KSC) if KSC < 2.
However, while both exponents are typically in the range 2 >
KSC > 1/2 in which both susceptibilities diverge, the precise values of these exponents, and
thus whether SC or CDW correlations are dominant, varies as a function of x and t′/t. In
fact, for the two-leg ladder, the same Luther-Emery phase has been shown to exist down
to U as small as U = 4t. To get an idea of why smaller values of U are so diﬃcult, note
that for t′ = 0 and x = 1/12, the spin correlation length ξs ≈30 lattice constants; it is thus
found that ladders up to L = 200 must be treated to get reliable results (98). (Interestingly,
in this case, the CDW and SC susceptibilities are equally divergent, KSC ≈KCDW ≈1.)
The nature of the short-range correlations on the two-leg ladder are also interest-
ing.
Although the SDW correlations decay exponentially with distance, the spin cor-
relation length is suﬃciently long that one can identify a preferred ordering vector,
QSDW = πn ≡π ± πx. Importantly, this is mutually commensurate with the CDW or-
dering vector, QCDW ≡2QSDW. Also, the superconducting order is “d-wave-like” in the
sense that the pair-ﬁeld correlations on bonds parallel to and perpendicular to the lad-
der direction have opposite signs. (Since the ladder does not have any symmetry relating
parallel and vertical bonds, this is not a precise symmetry classiﬁcation, and indeed the
magnitude of the pair-ﬁeld correlations are somewhat diﬀerent on the two sets of bonds.)
The short-range order is thus a two-leg version of the correlations shown schematically in
Fig. 4a, where for graphical simplicity we have drawn this picture for the commensurate
case x = 1/4 so that λCDW = 4. The relative phase of the CDW, SDW, and SC modulations
are representative of what is seen in the calculations, i.e. the spin order is strongest where
the SC order is weakest and where the local doped hole concentration is closest to 0. (The
fact that the CDW is “bond-centered,” i.e. that it preserves reﬂection symmetry about a
bond-centered mirror plane, was likewise chosen for purposes of illustration only.)
Even for the two-leg ladder, there are circumstances in which other phases arise. As
already mentioned in §5.2, for large enough U, for 0 < x ≲0.2, there is a fully polarized
(half-metallic) phase - a result that was also established using DMRG (64).
Moreover,

24
Arovas et al.

## Page 25

for special rational values of x (such as x = 1/8) and for a range of U/t, commensurate
CDW long-range order is possible (100, 101), i.e. a discrete breaking of the translational
symmetry. The ordering vector in this case is, as before, λCDW = 2/x, but now there is a
gap to charge excitations as well a spin-gap.
Moving to W = 4 leg ladders and cylinders, a still richer variety of behaviors has been
observed (102, 103, 104). In particular the nature of the states for a given value of x is
found to depend signiﬁcantly on the value of t′. Under some circumstances, especially in
4-leg cylinders with t′ small and negative,8 there appears to be (105, 106, 107) a Luther-
Emery liquid phase with c = 1, divergent CDW and SC susceptibilities with the product
KCDWKSC = 1 and with the KSC in the range 0.5 < KSC ≲2, and exponentially falling
SDW correlations with ξsdw ∼10. Where this occurs, it is typically also true that QCDW =
4πx. The sketch in Fig. 4b is a caricature of the short-range order seen here. Recalling
that periodic boundary conditions have been enforced around the cylinder, it is apparent
that the SC order – which oscillates in sign between neighboring bonds around the cylinder
– has a “true d-wave” form (108, 107) in the sense that it changes sign under a C4 rotation
about the central axis of the cylinder. Such a state is likely to be a peculiarity of the 4-leg
cylinder.
For t′ = 0, the W = 4 leg cylinder shows signiﬁcantly diﬀerent tendencies. The most
extensive studies (108, 109, 105, 107) have been carried out primarily for the (assumed
representative) value of x = 1/8. Here the preferred CDW ordering vector is half what it
was in the previous case, QCDW = 2kF ≡2πx. Moreover, it seems that the SC correlations
fall rapidly – most probably exponentially - with distance. (However, in this case, the SC
correlation length, ξSC is remarkably long - it is estimated in ref. (110) that ξSC ≈18).
There is again signiﬁcant short-range SC and SDW order, with, as in Fig. 4a, the SC order
being d-wave-like, and the SDW ordering vector satisfying the mutual comensurability
condition, 2QSDW ≡QCDW. This, if extrapolated to the 2d limit, is suggestive (109) of a
commensurate unidirectional CDW insulating state, either with or without accompanying
SDW order, with a signiﬁcant but strictly short-range correlated tendency toward d-wave
SC. Thinking of the peaks in the CDW as being a stripe of high doped hole density, this
state, which arises naturally in Hartree-Fock calculations in 2d, is sometimes referred to as
having “full stripes” – full, in the sense that since λCDW = 1/x, there is one doped hole per
site along the length of each stripe. By contrast, the state with λCDW =
1
2x (QCDW = 4πx)
is then referred to as ”half-ﬁlled” stripes.
Patterns of local order corresponding to partially-ﬁlled stripes of diﬀerent varieties have
been found in calculations on W = 6 leg ladders (111, 112). Very recently, there have been
the ﬁrst DMRG studies(113, 114, 115) (actually, of the t −J model) to ﬁnd direct evidence
of (quasi)-long-range d-wave-like SC order in cylinders with W > 4. Not surprisingly, the
SC correlations tend to be strongest for values of the parameters (e.g. t′/t) for which the
CDW correlations are relatively weaker(114, 115). Generally, the phases with strong SC
correlations occur only for x greater than a (parameter dependent) critical value of x - the
one exception to this(113) being the case of very large t′ ≈t/
√

2, where the state at x = 0
is (as already discussed) a quantum para-magnet (probably a spin liquid), and where SC
quasi-long-range-order appears down to the smallest values of x (x = 1/18) explored so far.
A periodic modulation of the hopping was found to signiﬁcantly enhance the d-wave like

8In DMRG studies, a value of t′ ≈−0.3t is often taken as a value representative of the band-
structure of the hole-doped cuprates.

www.annualreviews.org • The Hubbard Model
25

## Page 26

Figure 4

Various patterns of intertwined short-range order for the square lattice Hubbard model at moderate x and intermediate U.
Here the size of the circles indicates represents the doped hole density, the arrows represent the site magnetization, and
the thickness of the lines the magnitude of the singlet pair ﬁeld on each bond; the sign of the pair-ﬁeld is color coded with
red positive and blue negative. Here a) Represents coexisting SDW, CDW, and d-wave-like SC, b) (relevant in particular
to the M = 4 leg cylinder) represents SDW, CDW, and cylindrical “true d-wave” SC, and c) represents SDW, CDW, and
PDW order.

pairing correlations, as well (116). As these are very new results, it is still necessary for
further studies to be carried out to determine the full phase diagram.

6.1.3. The honeycomb lattice. DMRG studies have been performed for the Heisenberg
model on the honeycomb lattice for a range of J′/J (117, 118).
The behavior of the
honeycomb model appears to have similar motifs as the more studied square and triangular
lattices. In particular, there is evidence for an intermediate spin-disordered phase for a
range of J′/J between the N´eel and striped phases. All or much of this intermediate phase
seems to possess plaquette order (118). Some DMRG studies have also been performed on
the honeycomb Hubbard model away from half ﬁlling (119, 120, 121). We will not further
summarize these results here.

6.1.4. The triangular lattice. DMRG studies of the Hubbard model on the triangular lattice
have recently produced evidence of a number of intriguing behaviors (122, 123, 124, 125,
126, 127). Unfortunately, there is still considerable disagreement in the inferences drawn
from diﬀerent studies, making it diﬃcult to give a deﬁnitive review.
Undoped cylinders with 3 ≤W ≤5 have been studied at x = 0. There is strong
evidence (and a general consensus) that there are at least three distinct phases as a function
of U/t. For U < Uc1 ≈8t there is a compressible phase that has been identiﬁed as “metallic”
in several DMRG studies. More speciﬁcally the DMRG studies have concluded that it is
metallic in the sense of being adiabaticaly connected to the non-interacting limit, i.e. that
there are gapless spin and charge modes corresponding to each Fermi surface crossing of
the non-interacting band-structure. This conclusion is diﬃcult to reconcile with a weak
coupling analysis (98) of the sort described in §5.1. Rather, assuming there are no as yet
undetected transitions with a critical value of U < Uc1, it is likely that most of these modes
are gapped, but that the gaps are suﬃciently small (the correlation lengths suﬃciently
large) that they have been overlooked in DMRG studies to date. Indeed, the weak coupling
analysis suggests that the small U phase is a Luther-Emery liquid (c = 1) with time reversal
symmetry breaking - i.e. an extension of the d + id SC phase that arises in 2d at small U

26
Arovas et al.

## Page 27

(see §5.1) to a cylinderical geometry.
The most intriguing phase at x = 0 occurs for Uc1 < U < Uc2 ≈10t. Here there is
evidence that the system becomes a spin liquid in the 2d limit. For instance, for M = 4
and suitable boundary conditions, there seems to be a fully gapped state with only very
short-range spin correlations.
It was concluded in ref. (123) that this phase is chiral -
indicating that in the 2d limit it would correspond to a time reversal symmetry breaking
chiral spin liquid (i.e. a Kalmeyer-Laughlin phase (128)). This has a degree of naturalness
as it is easy to conceive a continuous transition from a d + id SC to a chiral spin liquid.
However, it should be mentioned that other studies (126, 125) have found evidence that
this intermediate phase is a fully gapped but non-chiral state – which is suggestive that
there is a Z2 spin liquid (i.e. a Moessner-Sondhi phase (129)) in the 2D limit – or even a
gapless spin liquid (127) with a nodal spinon spectrum.
Finally, for Uc2 < U there is a phase with local correlations corresponding to the 120◦

antiferromagentic state, known to be the ground state of the 2d model in the large U limit.
Doped cylinders: The nature of the lightly doped system clearly depends on the
character of the undoped parent state. The resulting phase diagram has not been nearly as
thoroughly investigated as in the case of the square lattice. Particularly interesting is the
fate of a lightly doped spin liquid. A spin liquid can be thought of as a quantum disordered
superconductor, such that upon light doping, the “pairing” is a property inherited from the
insulating state while the superﬂuid stiﬀness (and hence the ordering temperature) vanishes
continuously as x →0 (3, 130, 131). Speciﬁcally, light doping of a gapped spin liquid could
lead to a gapped superconductor - with the “superconducting” gap derived from the spin-
liquid gap - which is chiral (d + id) (132) or non-chiral depending on the nature of the
spin-liquid from which it arose - while a nodal spin liquid naturally connects to a nodal
superconductor (133). There is preliminary DMRG evidence that each of these may occur
on the triangular lattice under appropriate circumstances (134, 124, 127, 122, 135).

6.1.5. The kagome lattice. The Heisenberg model on the kagome lattice is a paradigmatic
example of a geometrically frustrated quantum magnet. It has long been suspected that this
system does not order magnetically, even with only nearest-neighbor J. Diﬀerent ground
states have been proposed based on exact diagonalization of ﬁnite clusters (136, 137, 138,
139, 140, 141), and various approximate approaches. [For a discussion, see Refs. (141, 142).]
DMRG calculations on cylinders of width up to W = 17 have been performed (143, 144,
145, 146, 147). (In some of these calculations, a small second-neighbor J′ ≤0.15J has been
applied.) These works consistently ﬁnd a quantum disordered ground state with no sign
of magnetic or valence bond crystalline order. This suggests a quantum spin liquid ground
state. Unfortunately, there is disagreement on the nature of this spin liquid, e.g., whether it
has a spin gap (145) or a gapless Dirac spinon spectrum (147). The disagreements suggest
that the long-range correlations may not yet be fully converged with respect to the bond
dimension, and more extensive studies are needed to resolve the nature of the ground state.
In the studies of the doped system carried out to date (148, 149), light doping of the
kagome spin liquid seemingly leads to a “holon” crystal phase - an insulating state with one
doped hole but zero spin per unit cell - rather than to a superconductor.

www.annualreviews.org • The Hubbard Model
27

## Page 28

6.2. Quantum Monte Carlo results

The determinant quantum Monte Carlo method (150, 151, 152, 153) is a powerful technique
to ﬁnd equilibrium properties of interacting fermions. It is controlled, in the sense that the
results are guaranteed to converge to the exact answers upon increasing the computational
eﬀort. Unfortunately, in many cases of interest, the applicability of the DQMC method is
limited due to the fermion sign problem (154). In these cases, the computational cost for
a given accuracy increases exponentially with the system size and the inverse temperature.
The repulsive Hubbard model suﬀers from the fermion sign problem in DQMC at generic
values of the ﬁlling. Below, we brieﬂy review some useful results that were nevertheless
obtained using DQMC, either for special parameters where the sign problem is absent, or
by employing very large computational resources to overcome the sign problem.
The U > 0 Hubbard model is sign problem free if the system is particle-hole sym-
metric (152). This is the case at half ﬁlling (n = 1) on a bipartite lattice (e.g., square or
honeycomb), when the intra-sublattice hopping is set to zero. Note that the sign of U can be
changed by performing a particle-hole transformation on one spin species, showing that the
U < 0 Hubbard model is sign problem free with zero total magnetization and an arbitrary
ﬁlling. The Hubbard model has been simulated using DQMC on a square lattice (152),
showing a clear Mott gap and an antiferromagnetic (N´eel) ground state for all U > 0.
On the honeycomb lattice, the semimetal state with Dirac nodes is stable for suﬃciently
small U, whereas the ground state for suﬃciently large U is a collinear sublattice antiferro-
magnet with opposite spin polarization on the two sublattices (155, 156). Initial simulations
suggested a quantum spin liquid state at intermediate U between the semimetal and the
AF (157); however, the current consensus is that there is a direct continuous transition
between the semimetal and AF phases with no intermediate phase (158, 159).
The bilayer Hubbard model has been studied at half ﬁlling for the square (160, 161, 162)
and honeycomb (163, 57) lattices. In the latter case, motivated by Bernal-stacked bilayer
graphene, an AB stacking has been considered.
In this case, the non-interacting band
structure has quadratic band touchings, and the system may be expected to be unstable
even in the presence of arbitrarily weak U, as discussed in §5.1. However, it was found that
for weak interactions, the dispersion gets renormalized, and each quadratic band touchings
splits into four linearly dispersing Dirac points (57). As a result, a ﬁnite U is needed to bring
the system from the semimetal into the AF phase, much as in the single layer honeycomb
model.
Finally, DQMC has been applied to the square (164, 165, 104, 166) and honeycomb (167)
lattice away from half ﬁlling. These calculations require massive computing resources. The
square lattice calculations have currently been performed for systems for size L = 8 at tem-
peratures down to T/t ≃0.2 and interaction strength U/t = 8. At these temperatures, ﬁnite
size eﬀects are found to be small, such that L = 8 is probably suﬃcient to make inferences
about the thermodynamic limit. No symmetry broken phase was found. However, there are
signiﬁcant short-range correlations (164) indicative of incommensurate unidirectional spin
density wave, d-wave superconductivity, as well as nematic bond order (166), that grow as
the temperature decreases.

7. Are there exotic phases in the Hubbard model?

Progress has been made in recent years in constructing “reverse engineered” model Hamil-
tonians - such as the Kitaev model or the quantum dimer model - that exhibit exotic

28
Arovas et al.

## Page 29

quantum phases of various sorts. This is suﬃcient to settle certain long-standing issues of
principle - such as whether quantum-spin-liquid phases exist. However, to address whether
it is reasonable to expect such phases to arise without extreme ﬁne tuning, it is worthwhile
to ask whether these arise in some version of the Hubbard model - with some particular
lattice geometry or some range of U/t or t′/t.

7.1. Phases with exotic broken symmetries

Two novel classes of broken symmetry phases have been proposed as candidate orders
to account for some observed anomalies in the cuprate high temperature superconductors:
states with orbital loop current order (168, 169) and pair-density-wave states (170, 171, 172)
with spatially modulated superconducting order.

7.1.1. Orbital Loop current order. These are states that are close relatives of a charge
density wave, but which break time-reversal symmetry, i.e. in which

i
X

σ
⟨c†
j,σck,σ −c†
k,σcj,σ⟩= Jjk ̸= 0
.
34.

Two particularly important such proposals are a zero-momentum “intra-unit cell orbital
antiferromagnet” in which Jjk = J(Rj −Rk), which has ordering vector Q = 0, and a “d-
density-wave,” in which - on a square lattice in particular - Jjk = eiQ·RjJ(Rj −Rk) with
Q = (π, π). In both these examples, J(R) transforms non-trivially under the operations
of the point group. Another related state - of which the “triplet d-density wave” is an
example (173) - is a spin-current density wave - which preserves time-reversal symmetry.
As far as we know, convincing evidence for the existence of such phases has not been
found in either numerical or controlled approximate studies of Hubbard models. DMRG
calculations on doped Hubbard ladders that have probed such order typically have found
very weak, extremely short-range current-current correlations (174, 175, 176, 108)9.
There is evidence (discussed in §7.2) that a chiral spin-liquid phase arises in a small but
ﬁnite range of U/t in the undoped Hubbard model on the triangular lattice. Moreover, for
a band-structure with a symmetry protected quadratic band-touching, there is a dominant
tendency toward an anomalous quantum Hall state at weak coupling (177). Although these
states break time reversal symmetry, they must have a zero orbital current on any link lying
in a mirror plane. However, a CDW state in doped versions of either of these seems likely
to support orbital loop current order.

7.1.2. Pair Density wave. A pair-density-wave (PDW) is a close relative of the famous
FFLO states (178, 179) that arise (at least in theory) in conventional superconductors in
response to a small degree of spin-polarization. As the name suggests, this is a supercon-
ducting state with a pair-ﬁeld that is spatially modulated:
c†
j,↑ck,↓+ c†
k,↑cj,↓
= Φ(Rj, Rk) ̸= 0
,
35.

where in contrast with any conventional superconducting state, the spatial average of Φ van-
ishes, P

R Φ(R, R + r) = 0 for ﬁxed r. (This is a spin-singlet PDW - one can also consider

9In (175), indications of loop current order were found for relatively large x in a three band
model with substantial nearest-neighbor V , but this was found to arise in an “unphysical” range of
parameters, i.e. one in which the undoped system is not an antiferromagnetic insulator.

www.annualreviews.org • The Hubbard Model
29

## Page 30

the possibility of a spin-triplet PDW.) Such states have been found as close competitors
in certain variational treatments of the Hubbard model, and short-range PDW correlations
have been reported in several diﬀerent DMRG calculations on Hubbard ladders. Moreover,
to date, no clear evidence of PDW long-range order (or even of suﬃciently strong quasi-
long-range order to lead to a divergent PDW susceptibility) has been presented in studies
of any version of the Hubbard model (180, 181), except in one dimension (182, 183). How-
ever, the observation of clear PDW short-range order in some cases is a promising point of
departure for future investigations (170, 184, 185).

7.2. Phases with topological character

There has been an extensive search for spin-liquid phases in Hubbard models with an
odd integer number of electrons per unit cell. Here, as discussed in § 2, it follows from the
generalized LSMOH theorem that any insulating phase that preserves translation symmetry
must be a topologically ordered “spin liquid” phase that cannot be adiabatically connected
to any band-insulator. At present, while there is no absolutely convincing evidence of such
a phase, as discussed in §6.1, there are several systems for which DMRG results are highly
suggestive of the existence of quantum spin liquid phases, albeit for relatively narrow ranges
of parameters.

8. Speculations concerning the phase diagram in d ≥2

Until this point, we have presented results that are established with some degree of theoret-
ical certainty. Alas, this means we have not been able to present any results for what might
a-priori be considered the most important regime - spin- 1

2 fermions with density near but
not equal to 1 per site and U comparable to the band-width. This is the range of parameters
that is likely most relevant to phenomena in a host of highly correlated materials including
the cuprate and various organic superconductors. In this ﬁnal section we make a specu-
lative attempt to extrapolate from regimes in which our theoretical understanding is solid
to obtain a global picture of the phases and regimes of the Hubbard model - particularly
focused on the properties of the model in 2d.

8.1. The square lattice Hubbard model

In Fig. 5a we show a schematic T = 0 phase diagram in the U/t −µ plane of the square
lattice Hubbard model with non-vanishing second neighbor hopping matrix, t′/t ̸= 0. On
the basis of the weak coupling analysis, we know that for U/8t ≪1, there is a uniform
d-wave SC phase with no other forms of coexisting order. (Here 8t is the non-interacting
bandwidth.) In the large U limit and for a range of doping 0 < x ≲0.2, one can conclude
on the basis of DMRG studies that there is a fully polarized ferromagnetic phase - a “half-
metallic ferromagnet” (HMF). Moreover, there are compelling theoretical arguments (63,
186) (which we will not review here) that there is a direct ﬁrst-order transtion from the
AFI to the HMF phase, giving rise to the region of two-phase coexistence indicated, with
the density of the compressible phase going as xc ∼
p

8t/U as U →∞.
Independent of U, in the dilute electron limit (not shown) the system behaves as a Fermi
liquid behavior down to an exponentially low energy scale, below which it presumably forms
an unconventional superconducting state by some version of the Kohn-Luttinger mechanism.
Finally, for the half ﬁlled band (x = 0) and U/8t greater than a critical value, αc, there is an

30
Arovas et al.

## Page 31

insulating phase which, so long as t′/t ≲1/2 (so the magnetism is not terribly frustrated),
exhibits long-range N´eel order. (As discussed in §5.4.2, αc ∼1/ ln |t/t′| →0 as t′/t →0.)
In the ﬁgure, we have indicated by the black circle a presumed direct (and conse-
quently ﬁrst order) transition from the d-wave superconductor at x = 0 to the insulating
antiferromagnetic phase. Such a direct transition occurs in Hartree-Fock approximation (or
equivalently in a suitable large N limit) for small t′/t, although at larger t′/t there can arise
an intermediate antiferromagnetic metal (i.e. only partially gapped) phase (187). Assum-
ing the transition at x = 0 is ﬁrst order, the transition must remain ﬁrst order for a range
of chemical potentials. Consequently, for small U/8t > αc there must exist a two-phase
coexistence region corresponding to the thick solid line in the ﬁgure.
Indeed, arguments suggesting that the antiferromagnetic insulating phase is generically
bounded by a line of ﬁrst order transitions (leading to phase separation) were summarized
in ref. (77), and more recently have been supported by extensive variational Monte Carlo
studies of the Hubbard model in ref. (188). Another candidate small x phase when U/8t ≳
αc that is suggested by Hartree-Fock studies (78, 79, 80) (especially in the limit t′ = 0)
is an insulating incommensurate unidirectional colinear SDW (stripe) phase. The stripe
phase can be thought of as a form of micro-phase-separation.
Unfortunately, the structure of the middle part of the phase diagram, where U/8t ∼1
and 1/12 ≲x ≲1/3, is presently unsettled. From DMRG and other studies, it is clear that
there are strong local tendencies toward d-wave SC, as well as unidirectional (stripe) CDW
and SDW orders. Implicit in the observation of striped states is a strong tendency toward
lattice rotational symmetry breaking, i.e. nematic order10.
That all DMRG studies (as well as other less controlled methods) ﬁnd strong local
tendencies toward d-wave SC is compatible with the supposition that the Hubbard model
at intermediate coupling captures an essential feature of cuprate physics that leads to high-
temperature d-wave SC. However, whether the Hubbard model has more than a “d-wave
tendency” - i.e. whether it actually supports a robust d-wave SC phase at intermediate U
or not - is still unsettled. Under most circumstances, especially in broader ladders, the
DMRG studies suggest that the competing tendency toward CDW order may be stronger.

8.2. The triangular lattice Hubbard model

Fig. 5b shows a conjectured phase diagram for the triangular lattice Hubbard model. Again,
from a weak coupling analysis, we know that the small U portion of the phase diagram is
superconducting, likely a d + id SC (189, 190). At n = 1 and large enough U, the model is
equivalent to a spin 1/2 Heisenberg model, for which strong evidence exists that the ground
state has long-range, coplanar three sublattice insulating antiferromagnetic order - the “120◦

state.”
DMRG studies consistently indicate the existence of an intermediate insulating
phase without any long or quasi-long-range antiferromagnetic order - corresponding to some
sort of quantum spin liquid (QSL). Thus, at x = 0 there are two transitions (indicated by
the solid circles) as a function of U/8t.
The exact nature of the QSL, however, is still
contravertial.
There is some evidence that the QSL in question is a chiral spin liquid, which would be
compatible with a continuous transition to a chiral (d + id) SC upon light doping, as shown

10This interpretation requires some care, because of the eﬀects of the boundaries, present in most
DMRG calculations.

www.annualreviews.org • The Hubbard Model
31

## Page 32

Figure 5

Speculative ground state phase diagrams of the Hubbard model as a function of U and chemical
potential, µ (upper panels) or doped hole density, x (lower panels). a) Square lattice with
t ≫|t′| > 0: AFI indicates an insulating (incompressible) phase with N´eel AF order and doped
hole-density x = 0. The thick solid line indicates a ﬁrst-order transition from the AFI to a
compressible phase, and the black circles denote points at which x = 0 in the compressible phase.
“2-phase” denotes a region of two-phase coexistence. HMF denotes a half metallic ferromagnetic
phase. At intermediate U/8t, there is clear numerical evidence of multiple local ordering
tendencies of comparable strengths including unidirectional CDW, colinear unidirectional SDW,
nematic, and d-wave SC. Which of these phases actually orders is still uncertain. b) Triangular
lattice: At weak coupling, the ground state is a dx2−y2 + idxy SC. DMRG studies suggest that
for x = 0 as a function of increasing U there is an insulating quantum spin liquid (QSL) phase
when U is comparable to the bandwdith, 9t, that lies between the small U SC and the large U
three-sublattice 120◦ordered AFI phase. The transition from the QSL to the AFI is likely ﬁrst
order. For U ∼9t and ﬁnite x, there is DMRG evidence of at least short-range tendencies to
d + id and nematic (NSC)superconducting order, as well as CDW, SDW and PDW phases.

in the ﬁgure. Then at larger doping and intermediate values of U/8t, there is evidence from
DMRG studies of a local tendency toward a variety of possible broken symmetry phases
including SDW, CDW, PDW and nematic SC. However, again, which of these orders exist
as ground state phases in 2d is still an open question. Preliminary evidence (122) that
the SC tendencies are particularly strong at small x and for U in the spin-liquid regime
oﬀers some encouragement for the long cherished ideal that a spin liquid may be a high
temperature superconductor waiting to happen.

32
Arovas et al.

## Page 33

9. Important Open Questions

We end by highlighting some of the major outstanding challenges in the physics of the
Hubbard model.
Is the Hubbard model a high temperature SC? It has been established that
the repulsive U Hubbard model has a superconducting ground state at small U, but it
still remains uncertain whether - and if so under what circumstances - it supports “high
temperature superconductivity.” In other words, are there circumstances (i.e. some range
of band-structure parameters) in which the Hubbard model is superconducting when all
the energy scales are comparable, i.e. when U is on the order of the bandwidth, so that
Tc - if a SC state arises - is a sizable fraction of EF. To get a quantitative feeling, recall
that the bandwidth in the cuprates is of the order of W ∼2eV. Taking W ≃8t, we obtain
that a Tc of 0.05t would correspond to Tc ∼150K, of the order of the maximal transition
temperature found in the cuprates.
While aﬃrmative answers to this question have been suggested on the basis of various
approximate calculations, the presence of multiple intertwined orders - with the consequent
existence of subtle energies that are diﬃcult to capture reliably - renders the validity of
these approximate results uncertain.
What exotic phases arise? At the same time, while there are various reasons to
feel that exotic forms of quantum order can arise in the Hubbard model - at least if the
underlying band-structure cooperates - currently the evidence for these states ranges from
suggestive to absent. Ideally, one would like to identify versions of the model that unam-
biguously exhibit various forms of insulating quantum spin liquids, pair-density-wave SCs
(in more than one dimension), and/or possible forms of orbital loop current order.
What sort of non-Fermi-liquid behaviors occur at elevated T? We have hardly
touched on the nature of the model at ﬁnite T (although much is known) and have totally
neglected any issues associated with near equilibrium dynamical properties, much less the
far from equilibrium behaviors that are of so much recent interest. For instance, for U on
the order of the bandwidth, there most probably will not be a broad range of T above all
ordering temperatures in which the system can be well described by the weakly interacting
quasi-particles of Fermi liquid theory. What the behavior is in this regime of T - especially
including what processes govern the dissipative linear response of the system - is one of the
most important open areas in the ﬁeld.
Have we learned anything useful? Finally, we have discussed controlled solutions
of the Hubbard model - and have emphasized the limited progress that has been made
even on this simplest of all model strongly correlated systems. Obviously, from a broader
perspective, what is needed are much simpler and more versatile methods of solution (2, 191,
192) that once benchmarked by comparison with the controlled results discussed here, can
be applied more widely - perhaps even in ways that interface with microscopic electronic-
structure approaches (193, 194, 195).

Acknowledgements

It is a pleasure to acknowledge numerous extremely helpful discussions about the Hubbard
model and related topics with too many colleagues to list. In particular, however, the writing
of this paper was greatly assisted by input from Ian Aﬄeck, Assa Auerbach, Vladimir
Calvera, Andrey Chubukov, Youjin Deng, Tom Devereaux, Eduardo Fradkin, Zhaoyu Han,
Hong-Chen Jiang, Elliott Lieb, Dror Orgad, Mohit Randeria, Doug Scalapino, and Richard

www.annualreviews.org • The Hubbard Model
33

## Page 34

Scalettar. SAK was supported, in part, by the National Science Foundation (NSF) under
Grant No. DMR2000987. EB acknowledges support from the European Research Council
(ERC) under grant HQMAT (Grant Agreement No. 817799). SR was supported in part by
the Department of Energy, Oﬃce of Basic Energy Sciences, Division of Materials Sciences
and Engineering, under contract DE-AC02- 76SF00515.

LITERATURE CITED

1. John Hubbard. Electron correlations in narrow energy bands. Proceedings of the Royal Society
of London. Series A. Mathematical and Physical Sciences, 276(1365):238–257, 1963.
2. M Qin, T Sch¨afer, S Andergassen, P. Corboz, and E. Gull. The Hubbard model: A computa-
tional perspective. arXiv:2104.00064, 2021.
3. P. W. Anderson.
The Resonating valence bond state in La2CuO4 and superconductivity.
Science, 235(4793):1196–1198, 1987.
4. V. J. Emery. Theory of high-Tc superconductivity in oxides. Phys. Rev. Lett., 58:2794–2797,
Jun 1987.
5. D. J. Scalapino. A common thread: The pairing interaction for unconventional superconduc-
tors. Reviews of Modern Physics, 84(4):1383–1417, October 2012.
6. Elliott H. Lieb, Michael Loss, and Robert J. McCann.
Uniform density theorem for the
Hubbard model. Journal of Mathematical Physics, 34(3):891–898, 1993.
7. Chen Ning Yang. η pairing and oﬀ-diagonal long-range order in a Hubbard model. Phys. Rev.
Lett., 63:2144–2147, Nov 1989.
8. Shoucheng Zhang. SO(4) symmetry of the Hubbard model and its experimental consequences.
Int. Jour. Mod. Phys. B, 5:153–167, May 1991.
9. Chen Ning Yang and S. C. Zhang. SO(4) symmetry in a Hubbard model. Modern Physics
Letters B, 04(11):759–766, 1990.
10. Elliott H. Lieb. Two theorems on the Hubbard model. Phys. Rev. Lett., 62:1201–1204, Mar
1989.
11. V. J. Emery. Theory of high-Tc superconductivity in oxides. Phys. Rev. Lett., 58:2794–2797,
Jun 1987.
12. Elliott Lieb and Daniel Mattis. Ordering energy levels of interacting spin systems. Journal of
Mathematical Physics, 3(4):749–751, 1962.
13. Hal Tasaki. Extension of Nagaoka’s theorem on the large-U Hubbard model. Phys. Rev. B,
40:9192–9193, Nov 1989.
14. Hal Tasaki. Physics and Mathematics of Quantum Many-Body Systems. Springer, 2021.
15. Yosuke Nagaoka. Ferromagnetism in a narrow, almost half-ﬁlled s-band. Phys. Rev., 147:392–
405, Jul 1966.
16. D. J. Thouless. Exchange in solid 3He and the Heisenberg Hamiltonian. Proceedings of the
Physical Society, 86(5):893–904, nov 1965.
17. Elliott Lieb, Theodore Schultz, and Daniel Mattis. Two soluble models of an antiferromagnetic
chain. Annals of Physics, 16(3):407–466, 1961.
18. Masanori Yamanaka, Masaki Oshikawa, and Ian Aﬄeck. Nonperturbative approach to Lut-
tinger’s theorem in one dimension. Phys. Rev. Lett., 79:1110–1113, Aug 1997.
19. Masaki Oshikawa. Commensurability, excitation gap, and topology in quantum many-particle
systems on a periodic lattice. Phys. Rev. Lett., 84:1535–1538, Feb 2000.
20. M. B. Hastings. Lieb-Schultz-Mattis in higher dimensions. Phys. Rev. B, 69:104431, Mar 2004.
21. R. B. Laughlin. Quantized Hall conductivity in 2 dimensions . Phys. Rev. B, 23(10):5632–5633,
1981.
22. Siddharth A. Parameswaran, Ari M. Turner, Daniel P. Arovas, and Ashvin Vishwanath. Topo-
logical order and absence of band insulators at integer ﬁlling in non-symmorphic crystals.
Nature Physics, 9(5):299–303, 2013.

34
Arovas et al.

## Page 35

23. Haruki Watanabe, Hoi Chun Po, Ashvin Vishwanath, and Michael Zaletel. Filling constraints
for spin-orbit coupled insulators in symmorphic and nonsymmorphic crystals. Proceedings of
the National Academy of Sciences, 112(47):14551–14556, 2015.
24. R Schumann.
Thermodynamics of a 4-site Hubbard model by analytical diagonalization.
Annalen der Physik , 11(1):49–87, Jan 2002.
25. D. J. Scalapino and S. A. Trugman. Local antiferromagnetic correlations and dx2−y2 pairing.
Philosophical Magazine B, 74(5):607–610, 1996.
26. Hong Yao and Steven A. Kivelson. Fragile Mott insulators. Phys. Rev. Lett., 105(16), Oct
2010.
27. Steven R. White, Sudip Chakravarty, Martin P. Gelfand, and Steven A. Kivelson. Pair binding
in small Hubbard-model molecules. Phys. Rev. B, 45:5062–5065, Mar 1992.
28. Ehud Altman and Assa Auerbach. Plaquette boson-fermion model of cuprates. Phys. Rev. B,
65:104508, Feb 2002.
29. Wei-Feng Tsai and Steven A. Kivelson. Superconductivity in inhomogeneous Hubbard models.
Phys. Rev. B, 73(21), Jun 2006.
30. Hong Yao, Wei-Feng Tsai, and Steven A. Kivelson. Myriad phases of the checkerboard Hub-
bard model. Phys. Rev. B, 76:161104, Oct 2007.
31. Shirit Baruch and Dror Orgad. Contractor-renormalization study of Hubbard plaquette clus-
ters. Phys. Rev. B, 82:134537, Oct 2010.
32. Gideon Wachtel, Shirit Baruch, and Dror Orgad. Optimal inhomogeneity for pairing in Hub-
bard systems with next-nearest-neighbor hopping. Phys. Rev. B, 96:064527, Aug 2017.
33. T. Ying, R. Mondaini, X. D. Sun, T. Paiva, R. M. Fye, and R. T. Scalettar. Determinant
quantum Monte Carlo study of d-wave pairing in the plaquette Hubbard Hamiltonian. Phys.
Rev. B, 90:075121, Aug 2014.
34. George Karakonstantakis, Erez Berg, Steven R. White, and Steven A. Kivelson. Enhanced
pairing in the checkerboard Hubbard ladder. Phys. Rev. B, 83:054508, Feb 2011.
35. Elliott H. Lieb and F. Y. Wu. Absence of Mott Transition in an Exact Solution of the Short-
Range, One-Band Model in One Dimension. Phys. Rev. Lett., 20:1445–1448, Jun 1968.
36. Hsiu-Hau Lin, Leon Balents, and Matthew P. A. Fisher. N-chain Hubbard model in weak
coupling. Phys. Rev. B, 56:6569–6593, Sep 1997.
37. V. J. Emery, S. A. Kivelson, and O. Zachar. Spin-gap proximity eﬀect mechanism of high-
temperature superconductivity. Phys. Rev. B, 56:6120–6147, Sep 1997.
38. Thierry Giamarchi. Quantum physics in one dimension, volume 121. Clarendon press, 2003.
39. W. Kohn and J. M. Luttinger.
New mechanism for superconductivity.
Phys. Rev. Lett.,
15:524–526, Sep 1965.
40. D. J. Scalapino, E. Loh, and J. E. Hirsch. d-wave pairing near a spin-density-wave instability.
Phys. Rev. B, 34(11):8190–8192, Dec 1986.
41. MT Bealmonod, C Bourbonnais, and VJ Emery. Possible Superconductivity in nearly anti-
ferromagnetic itinerant fermion systems. Phys. Rev. B, 34(11):7716–7720, Dec 1986.
42. Saurabh Maiti and Andrey V. Chubukov. Superconductivity from repulsive interaction. AIP
Conference Proceedings, 1550(1):3–73, 2013.
43. Joseph Polchinski. Eﬀective Field Theory and the Fermi Surface. arXiv e-prints, pages hep–
th/9210046, October 1992.
44. R. Shankar.
Renormalization-group approach to interacting fermions.
Rev. Mod. Phys.,
66:129–192, Jan 1994.
45. M. Yu. Kagan and A. V. Chubukov. Possibility of a superﬂuid transition in a slightly nonideal
Fermi gas with repulsion. Sov. Jour. Exp. Theor. Phys. Lett., 47:614, May 1988.
46. S. Raghu, S. A. Kivelson, and D. J. Scalapino. Superconductivity in the repulsive Hubbard
model: An asymptotically exact weak-coupling solution. Phys. Rev. B, 81:224505, Jun 2010.
47. Richard Hlubina. Phase diagram of the weak-coupling two-dimensional t −t′ Hubbard model
at low and intermediate electron density. Phys. Rev. B, 59:9600–9605, Apr 1999.

www.annualreviews.org • The Hubbard Model
35

## Page 36

48. Emergent BCS regime of the two-dimensional fermionic Hubbard model: ground-state phase
diagram. EPL (Europhysics Letters), 110(5):57001, Jun 2015.
49. R. S. Markiewicz.
A survey of the Van Hove scenario for high-Tc superconductivity with
special emphasis on pseudogaps and striped phases.
Journal of Physics and Chemistry of
Solids, 58(8):1179–1310, 1997.
50. I. E. Dzyaloshinskii. Superconducting transitions due to van Hove singularities in the electron
spectrum. JETP, 66, 1987.
51. H. J. Schulz.
Superconductivity and antiferromagnetism in the two-dimensional Hubbard
model: Scaling theory. EPL (Europhysics Letters), 4(5):609, 1987.
52. A. A. Abrikosov and S. D. Beneslavskii. Some properties of gapless semiconductors of the
second kind. Journal of Low Temperature Physics, 5(2):141–154, 1971.
53. A. A. Abrikosov. Calculation of critical indices for zero-gap semiconductors. J. Exp. Theor.
Phys, 66:1443–1460, 1974.
54. Kai Sun, Hong Yao, Eduardo Fradkin, and Steven A. Kivelson. Topological Insulators and
Nematic Phases from Spontaneous Symmetry Breaking in 2D Fermi Systems with a Quadratic
Band Crossing. Phys. Rev. Lett., 103:046811, Jul 2009.
55. Oskar Vafek and Kun Yang. Many-body instability of coulomb interacting bilayer graphene:
Renormalization group approach. Phys. Rev. B, 81:041401, Jan 2010.
56. Leon Balents and Matthew P. A. Fisher.
Weak-coupling phase diagram of the two-chain
Hubbard model. Phys. Rev. B, 53:12133–12141, May 1996.
57. Sumiran Pujari, Thomas C Lang, Ganpathy Murthy, and Ribhu K Kaul.
Interaction-
induced Dirac fermions from quadratic band touching in bilayer graphene. Phys. Rev. Lett.,
117(8):086404, 2016.
58. A. V. Chubukov. Renormalization group analysis of competing orders and the pairing sym-
metry in Fe-based superconductors. Physica C Superconductivity, 469(9):640–650, May 2009.
59. M. Ulmke. Ferromagnetism in the Hubbard model on fcc-type lattices. The European Physical
Journal B - Condensed Matter and Complex Systems, 1(3):301–304, 1998.
60. A Mielke. Ferromagnetic ground states for the Hubbard model on line graphs. Journal of
Physics A: Mathematical and General, 24(2):L73–L77, jan 1991.
61. A Mielke.
Exact ground states for the Hubbard model on the kagome lattice.
Journal of
Physics A: Mathematical and General, 25(16):4335–4345, aug 1992.
62. B. S. Shastry, H. R. Krishnamurthy, and P. W. Anderson. Instability of the Nagaoka ferro-
magnetic state of the U=∞Hubbard model. Phys. Rev. B, 41:2375–2379, Feb 1990.
63. V. J. Emery, S. A. Kivelson, and H. Q. Lin. Phase-separation in the t-J model . Phys. Rev.
Lett., 64(4):475–478, Jan 1990.
64. Li Liu, Hong Yao, Erez Berg, Steven R. White, and Steven A. Kivelson. Phases of the Inﬁnite
U Hubbard Model on Square Lattices. Phys. Rev. Lett., 108:126406, Mar 2012.
65. A. A. Abrikosov and I. M. Khalatnikov. Concerning a model for a non-ideal Fermi gas. Sov.
Phys. JETP, 6(5), 1958.
66. Jan R. Engelbrecht, Mohit Randeria, and Lizeng Zhang. Landau f-function for the dilute
Fermi gas in two dimensions. Phys. Rev. B, 45:10135–10138, May 1992.
67. V. M. Galitskii. The energy spectrum of a non-ideal Fermi gas. Sov. Phys. JETP, 7(1):104,
1958.
68. Andrey V. Chubukov. Kohn-Luttinger eﬀect and the instability of a two-dimensional repulsive
Fermi liquid at T = 0. Phys. Rev. B, 48:1097–1104, Jul 1993.
69. Ian Aﬄeck and J. Brad Marston. Large-N limit of the Heisenberg-Hubbard model: Implica-
tions for high-Tc superconductors. Phys. Rev. B, 37:3774–3777, Mar 1988.
70. Daniel P. Arovas and Assa Auerbach. Functional integral theories of low-dimensional quantum
Heisenberg models. Phys. Rev. B, 38:316–332, Jul 1988.
71. J. Brad Marston and Ian Aﬄeck. Large-n limit of the Hubbard-Heisenberg model. Phys. Rev.
B, 39:11538–11558, Jun 1989.

36
Arovas et al.

## Page 37

72. N. Read and Subir Sachdev. Large-N expansion for frustrated quantum antiferromagnets.
Phys. Rev. Lett., 66:1773–1776, Apr 1991.
73. Alexander Cyril Hewson.
The Kondo Problem to Heavy Fermions.
Cambridge Studies in
Magnetism. Cambridge University Press, 1993.
74. Assa Auerbach. Interacting Electrons and Quantum Magnetism. Springer, 1994.
75. Eduardo Fradkin. Field theories of condensed matter physics (2nd edition). Cambridge Uni-
versity Press, 2013.
76. H. J. Schulz. Functional integrals for correlated fermions. Journal of low temperature physics,
99(3):615–624, 1995.
77. S. A. Kivelson and V. J. Emery. “Electronic Phase Separation and High Temperature Su-
perconductors,” Proceedings of ‘Strongly Correlated Electronic Materials: The Los Alamos
Symposium 1993’. Addison Wesley, Redding, 1994.
78. Jan Zaanen and Olle Gunnarsson.
Charged magnetic domain lines and the magnetism of
high-Tc oxides. Phys. Rev. B, 40:7391–7394, Oct 1989.
79. H. J. Schulz. Domain walls in a doped antiferromagnet. J. Phys. France, 50(18):2833–2849,
1989.
80. Kazushige Machida. Magnetism in La2CuO4 based compounds. Physica C: Superconductivity,
158(1):192 – 196, 1989.
81. H. J. Schulz. Incommensurate antiferromagnetism in the two-dimensional Hubbard model.
Phys. Rev. Lett., 64:1445–1448, Mar 1990.
82. Steven R. White. Density matrix formulation for quantum renormalization groups. Phys. Rev.
Lett., 69:2863–2866, Nov 1992.
83. Ulrich Schollwoeck. The density-matrix renormalization group in the age of matrix product
states. Annals of Phys., 326(1, SI):96–192, Jan 2011.
84. S. Ostlund and S. Rommer. Thermodynamic limit of density-matrix renormalizaiton . Phys.
Rev. Lett., 75(19):3537–3540, Nov 6 1995.
85. Michele Dolﬁ, Bela Bauer, Sebastian Keller, and Matthias Troyer. Pair correlations in doped
Hubbard ladders. Phys. Rev. B, 92:195139, Nov 2015.
86. F. Verstraete, M. Wolf, D. P´erez-Garc´ıa, and J. I. Cirac. Projected entangled states : Prop-
erties and applications. International Journal of Modern Physics B, 20(30n31):5142–5153,
2006.
87. S. R. White and A. E. Feiguin. Real-time evolution using the density matrix renormalization
group. Phys. Rev. Lett., 93(7), Aug 13 2004.
88. Chun Yang and Adrian E. Feiguin. Spectral function of Mott-insulating Hubbard ladders:
From fractionalized excitations to coherent quasiparticles.
Phys. Rev. B, 99:235117, June
2019.
89. Mingpu Qin, Thomas Sch¨afer, Sabine Andergassen, Philippe Corboz, and Emanuel Gull. The
Hubbard model: A computational perspective. arXiv:2104.00064, 2021.
90. F. D. M. Haldane. Continuum dynamics of the 1-d Heisenberg antiferromagnet identiﬁcation
with the O(3) non-linear sigma-model . Phys. Lett. A , 93(9):464–468, 1983.
91. Sudip Chakravarty. Dimensional crossover in quantum antiferromagnets. Phys. Rev. Lett.,
77:4446–4449, Nov 1996.
92. Hong-Chen Jiang, Hong Yao, and Leon Balents. Spin liquid ground state of the spin- 1

2 square
J1-J2 Heisenberg model. Phys. Rev. B, 86:024424, Jul 2012.
93. F. Figueirido, A. Karlhede, S. Kivelson, S. Sondhi, M. Rocek, and D. S. Rokhsar.
Exact
diagonalization of ﬁnite frustrated spin- 1

2 Heisenberg models. Phys. Rev. B, 41:4619–4632,
Mar 1990.
94. Shou-Shu Gong, Wei Zhu, D. N. Sheng, Olexei I. Motrunich, and Matthew P. A. Fisher.
Plaquette ordered phase and quantum phase diagram in the spin- 1

2 J1−J2 square Heisenberg
model. Phys. Rev. Lett., 113:027201, Jul 2014.
95. R. M. Noack, S. R. White, and D. J. Scalapino. The doped two-chain Hubbard model. EPL

www.annualreviews.org • The Hubbard Model
37

## Page 38

(Europhysics Letters), 30(3):163–168, April 1995.
96. Matthias Troyer, Hirokazu Tsunetsugu, and T. M. Rice. Properties of lightly doped t-J two-leg
ladders. Phys. Rev. B, 53:251–267, Jan 1996.
97. D. Poilblanc, O. Chiappa, J. Riera, S. R. White, and D. J. Scalapino. Evolution of the spin
gap upon doping a 2-leg ladder. Phys. Rev. B, 62:R14633–R14636, Dec 2000.
98. Yuval Gannot, Yi-Fan Jiang, and Steven A. Kivelson. Hubbard ladders at small U revisited.
Phys. Rev. B, 102:115136, Sep 2020.
99. A. Luther and V. J. Emery. Backward scattering in the one-dimensional electron gas. Phys.
Rev. Lett., 33:589–592, Sep 1974.
100. Steven R. White, Ian Aﬄeck, and Douglas J. Scalapino. Friedel oscillations and charge density
waves in chains and ladders. Phys. Rev. B, 65:165122, Apr 2002.
101. H. J. Schulz.
Critical behavior of commensurate-incommensurate phase transitions in two
dimensions. Phys. Rev. B, 22:5274–5277, Dec 1980.
102. S. R. White and D. J. Scalapino. Ground states of the doped four-leg t-J ladder. Phys. Rev.
B, 55(22):14701–14704, June 1997.
103. S. R. White and D. J. Scalapino. Competition between stripes and pairing in a t-t′-J model.
Phys. Rev. B, 60(2):R753–R756, July 1999.
104. Edwin W. Huang, Christian B. Mendl, Hong-Chen Jiang, Brian Moritz, and Thomas P. De-
vereaux. Stripe order from the perspective of the Hubbard model. npj Quantum Materials,
3:22, April 2018.
105. Hong-Chen Jiang and Thomas P. Devereaux. Superconductivity in the doped Hubbard model
and its interplay with next-nearest hopping t′. Science, 365(6460):1424–1428, 2019.
106. Hong-Chen Jiang, Zheng-Yu Weng, and Steven A. Kivelson. Superconductivity in the doped
t-J model: Results for four-leg cylinders. Phys. Rev. B, 98:140505, Oct 2018.
107. Chia-Min Chung, Mingpu Qin, Shiwei Zhang, Ulrich Schollw¨ock, and Steven R. White. Pla-
quette versus ordinary d-wave pairing in the t′-Hubbard model on a width-4 cylinder. Phys.
Rev. B, 102:041106, Jul 2020.
108. John F. Dodaro, Hong-Chen Jiang, and Steven A. Kivelson. Intertwined order in a frustrated
four-leg t-J cylinder. Phys. Rev. B, 95:155116, Apr 2017.
109. Bo-Xiao Zheng, Chia-Min Chung, Philippe Corboz, Georg Ehlers, Ming-Pu Qin, Reinhard M.
Noack, Hao Shi, Steven R. White, Shiwei Zhang, and Garnet Kin-Lic Chan. Stripe order in
the underdoped region of the two-dimensional Hubbard model. Science, 358(6367):1155–1160,
December 2017.
110. Yi-Fan Jiang, Jan Zaanen, Thomas P. Devereaux, and Hong-Chen Jiang. Ground state phase
diagram of the doped Hubbard model on the four-leg cylinder.
Physical Review Research,
2(3):033073, July 2020.
111. G. Hager, G. Wellein, E. Jeckelmann, and H. Fehske. Stripe formation in doped Hubbard
ladders. Phys. Rev. B, 71:075108, Feb 2005.
112. S. R. White and D. J. Scalapino. Stripes on a 6-leg Hubbard ladder. Phys. Rev. Lett., 91(13),
Sep 26 2003.
113. Hong-Chen Jiang and Steven A. Kivelson. High temperature superconductivity in a lightly
doped quantum spin liquid. arXiv:2104.01485, 2021.
114. Shoushu Gong, W. Zhu, and D. N. Sheng. Robust d-wave superconductivity in the square-
lattice t-J model. arXiv:2104.03758, 2021.
115. Shengtao Jiang, Douglas J. Scalapino, and Steven R. White. Ground state phase diagram of
the t-t′-J model. arXiv:2104.10149, 2021.
116. Hong-Chen Jiang and Steven A. Kivelson. Stripe order enhanced superconductivity in the
Hubbard model. arXiv e-prints, page arXiv:2105.07048, May 2021.
117. Shou-Shu Gong, D. N. Sheng, Olexei I. Motrunich, and Matthew P. A. Fisher. Phase diagram
of the spin- 1

2 J1-J2 Heisenberg model on a honeycomb lattice. Phys. Rev. B, 88:165138, Oct
2013.

38
Arovas et al.

## Page 39

118. Shou-Shu Gong, Wei Zhu, and D. N. Sheng. Quantum phase diagram of the spin-1 J1 −J2
Heisenberg model on the honeycomb lattice. Phys. Rev. B, 92:195110, Nov 2015.
119. Shenghan Jiang, Andrej Mesaros, and Ying Ran. Chiral spin-density wave, spin-charge-Chern
liquid, and d+id superconductivity in 1

4 -doped correlated electronic systems on the honeycomb
lattice. Phys. Rev. X, 4:031040, Sep 2014.
120. Xu Yang, Hao Zheng, and Mingpu Qin. Stripe order in the doped hubbard model on the
honeycomb lattice. Phys. Rev. B, 103:155110, Apr 2021.
121. Mingpu Qin. Stripe versus superconductivity in the doped Hubbard model on the honeycomb
lattice. arXiv e-prints, page arXiv:2104.14160, Apr 2021.
122. Hong-Chen Jiang.
Superconductivity in the doped quantum spin liquid on the triangular
lattice. arXiv:1912.06624, Dec 2019.
123. Aaron Szasz, Johannes Motruk, Michael P. Zaletel, and Joel E. Moore. Chiral spin liquid
phase of the triangular lattice hubbard model: A density matrix renormalization group study.
Phys. Rev. X, 10:021042, May 2020.
124. Zheng Zhu, D. N. Sheng, and Ashvin Vishwanath. Doped Mott insulators in the triangular
lattice Hubbard model. arXiv e-prints, page arXiv:2007.11963, July 2020.
125. Shou-Shu Gong, Wei Zhu, and D. N. Sheng. Emergent chiral spin liquid: Fractional quantum
Hall eﬀect in a kagome Heisenberg Model. Scientiﬁc Reports, Sep 2014.
126. Shou-Shu Gong, Wayne Zheng, Mac Lee, Yuan-Ming Lu, and D. N. Sheng.
Chiral spin
liquid with spinon Fermi surfaces in the spin- 1

2 triangular Heisenberg model. Phys. Rev. B,
100:241111, Dec 2019.
127. Shijie Hu, W. Zhu, Sebastian Eggert, and Yin-Chen He.
Dirac spin liquid on the spin- 1

2
triangular Heisenberg antiferromagnet. Phys. Rev. Lett., 123:207203, Nov 2019.
128. V. Kalmeyer and R. B. Laughlin. Equivalence of the resonating-valence-bond and fractional
quantum Hall states. Phys. Rev. Lett., 59:2095–2098, Nov 1987.
129. R. Moessner and S. L. Sondhi. Resonating valence bond phase in the triangular lattice quantum
dimer model. Phys. Rev. Lett., 86:1881–1884, Feb 2001.
130. Daniel S. Rokhsar and Steven A. Kivelson. Superconductivity and the Quantum Hard-Core
Dimer Gas. Phys. Rev. Lett., 61:2376–2379, Nov 1988.
131. R. B. Laughlin. The relationship between high-temperature superconductivity and the frac-
tional quantum Hall eﬀect. Science, 242:525–533, October 1988.
132. D. S. Rokhsar. Pairing in doped spin liquids - anyon versus d-wave superconductivity . Phys.
Rev. Lett., 70(4):493–496, Jan 1993.
133. L. Balents, M. P. A. Fisher, and C. Nayak. Nodal liquid theory of the pseudo-gap phase of
high-Tc superconductors. Int. Jour. Mod. Phys. B, 12(10):1033–1068, Apr 1998.
134. Yi-Fan Jiang and Hong-Chen Jiang. Topological Superconductivity in the Doped Chiral Spin
Liquid on the Triangular Lattice. Phys. Rev. Lett., 125:157002, Oct 2020.
135. Jordan Venderley and Eun-Ah Kim. Density matrix renormalization group study of supercon-
ductivity in the triangular lattice Hubbard model. Phys. Rev. B, 100(6):060506, Aug 2019.
136. Chen Zeng and Veit Elser. Numerical studies of antiferromagnetism on a Kagom´e net. Phys.
Rev. B, 42:8436–8444, Nov 1990.
137. J. T. Chalker and J. F. G. Eastmond. Ground state disorder in the spin- 1

2 Kagom´e Heisenberg
antiferromagnet. Phys. Rev. B, 46:14201–14204, Dec 1992.
138. P. Lecheminant, B. Bernu, C. Lhuillier, L. Pierre, and P. Sindzingre. Order versus disorder in
the quantum Heisenberg antiferromagnet on the Kagom´e lattice using exact spectra analysis.
Phys. Rev. B, 56:2521–2529, Aug 1997.
139. Andreas M. L¨auchli, Julien Sudan, and Erik S. Sørensen. Ground state energy and spin gap
of spin- 1

2 Kagom´e-Heisenberg antiferromagnetic clusters: Large-scale exact diagonalization
results. Phys. Rev. B, 83:212401, Jun 2011.
140. Hiroki Nakano and Toru Sakai. Numerical-diagonalization study of spin gap issue of the kagome
lattice Heisenberg antiferromagnet. Journal of the Physical Society of Japan, 80(5):053704,

www.annualreviews.org • The Hubbard Model
39

## Page 40

2011.
141. Andreas M. L¨auchli, Julien Sudan, and Roderich Moessner. S = 1

2 kagome Heisenberg anti-
ferromagnet revisited. Phys. Rev. B, 100:155142, Oct 2019.
142. Hitesh J. Changlani, Dmitrii Kochkov, Krishna Kumar, Bryan K. Clark, and Eduardo Fradkin.
Macroscopically degenerate exactly solvable point in the spin- 1

2 kagome quantum antiferro-
magnet. Phys. Rev. Lett., 120:117202, Mar 2018.
143. Simeng Yan, David A. Huse, and Steven R. White. Spin-liquid ground state of the S = 1

2
kagome Heisenberg antiferromagnet. Science, 332(6034):1173–1176, 2011.
144. H. C. Jiang, Z. Y. Weng, and D. N. Sheng. Density matrix renormalization group numerical
study of the kagome antiferromagnet. Phys. Rev. Lett., 101:117203, Sep 2008.
145. Hong-Chen Jiang, Zhenghan Wang, and Leon Balents. Identifying topological order by entan-
glement entropy. Nature Physics, 8(12):902–905, 2012.
146. Stefan Depenbrock, Ian P. McCulloch, and Ulrich Schollw¨ock. Nature of the spin-liquid ground
state of the S = 1

2 Heisenberg model on the kagome lattice. Phys. Rev. Lett., 109:067201, Aug
2012.
147. Yin-Chen He, Michael P. Zaletel, Masaki Oshikawa, and Frank Pollmann. Signatures of Dirac
cones in a DMRG study of the kagome Heisenberg model. Phys. Rev. X, 7:031020, Jul 2017.
148. Hong-Chen Jiang, T. Devereaux, and S. A. Kivelson. Holon Wigner crystal in a lightly doped
kagome quantum spin liquid. Phys. Rev. Lett., 119:067002, Aug 2017.
149. Cheng Peng, Yi-Fan Jiang, Dong-Ning Sheng, and Hong-Chen Jiang. Doping quantum spin
liquids on the kagome lattice. Advanced Quantum Technologies, page 2000126, 2021.
150. R. Blankenbecler, D. J. Scalapino, and R. L. Sugar.
Monte Carlo calculations of coupled
boson-fermion systems. I. Phys. Rev. D, 24:2278–2286, Oct 1981.
151. J. E. Hirsch. Discrete Hubbard-Stratonovich transformation for fermion lattice models. Phys.
Rev. B, 28:4059–4061, Oct 1983.
152. S. R. White, D. J. Scalapino, R. L. Sugar, E. Y. Loh, J. E. Gubernatis, and R. T. Scalettar.
Numerical study of the two-dimensional Hubbard model. Phys. Rev. B, 40:506–516, Jul 1989.
153. Fakher F Assaad. Quantum Monte Carlo methods on lattices: The determinantal approach.
Quantum Simulations of Complex Many-Body Systems: From Theory to Algorithms, 10:99–
147, 2002.
154. S. R. White, D. J. Scalapino, R. L. Sugar, N. E. Bickers, and R. T. Scalettar. Attractive and
repulsive pairing interaction vertices for the two-dimensional Hubbard model. Phys. Rev. B,
39:839–842, Jan 1989.
155. Sandro Sorella and Erio Tosatti. Semi-metal-insulator transition of the Hubbard model in the
honeycomb lattice. EPL (Europhysics Letters), 19(8):699, 1992.
156. Thereza Paiva, R. T. Scalettar, W. Zheng, R. R. P. Singh, and J. Oitmaa. Ground state and
ﬁnite-temperature signatures of quantum phase transitions in the half-ﬁlled Hubbard model
on a honeycomb lattice. Phys. Rev. B, 72:085123, Aug 2005.
157. Z. Y. Meng, T. C. Lang, S. Wessel, F. F. Assaad, and A. Muramatsu. Quantum spin liquid
emerging in two-dimensional correlated Dirac fermions. Nature, 464(7290):847–851, 2010.
158. Sandro Sorella, Yuichi Otsuka, and Seiji Yunoki. Absence of a spin liquid phase in the Hubbard
model on the honeycomb lattice. Scientiﬁc reports, 2(1):1–5, 2012.
159. Fakher F. Assaad and Igor F. Herbut. Pinning the order: The nature of quantum criticality
in the Hubbard model on honeycomb lattice. Phys. Rev. X, 3:031010, Aug 2013.
160. Nejat Bulut, Douglas J. Scalapino, and Richard T. Scalettar. Nodeless d-wave pairing in a
two-layer Hubbard model. Phys. Rev. B, 45:5577–5584, Mar 1992.
161. Richard T. Scalettar, Joel W. Cannon, Douglas J. Scalapino, and Robert L. Sugar. Magnetic
and pairing correlations in coupled Hubbard planes. Phys. Rev. B, 50:13419–13427, Nov 1994.
162. K. Bouadim, G. G. Batrouni, F. H´ebert, and R. T. Scalettar. Magnetic and transport prop-
erties of a coupled Hubbard bilayer with electron and hole doping. Phys. Rev. B, 77:144527,
Apr 2008.

40
Arovas et al.

## Page 41

163. Thomas C. Lang, Zi Yang Meng, Michael M. Scherer, Stefan Uebelacker, Fakher F. Assaad,
Alejandro Muramatsu, Carsten Honerkamp, and Stefan Wessel. Antiferromagnetism in the
Hubbard model on the Bernal-stacked honeycomb bilayer. Phys. Rev. Lett., 109:126402, Sep
2012.
164. Edwin W. Huang, Christian B. Mendl, Shenxiu Liu, Steve Johnston, Hong-Chen Jiang, Brian
Moritz, and Thomas P Devereaux. Numerical evidence of ﬂuctuating stripes in the normal
state of high-Tc cuprate superconductors. Science, 358(6367):1161–1164, 2017.
165. Edwin W Huang, Ryan Sheppard, Brian Moritz, and Thomas P Devereaux. Strange metallicity
in the doped Hubbard model. Science, 366(6468):987–990, 2019.
166. Tianyi Liu, Daniel Jost, Brian Moritz, Edwin W. Huang, Rudi Hackl, and Thomas P. Dev-
ereaux. Tendencies of enhanced electronic nematicity in the Hubbard model and a comparison
with Raman scattering on high-temperature superconductors. arXiv:2101.07486, 2021.
167. Xingchuan Zhu, Tao Ying, Huaiming Guo, and Shiping Feng.
Quantum Monte Carlo
study of the dominating pairing symmetry in doped honeycomb lattice.
Chinese Physics
B, 28(7):077401, 2019.
168. C. M. Varma. Pseudogap phase and the quantum-critical point in copper-oxide metals. Phys.
Rev. Lett., 83:3538–3541, Oct 1999.
169. Sudip Chakravarty, R. B. Laughlin, Dirk K. Morr, and Chetan Nayak. Hidden order in the
cuprates. Phys. Rev. B, 63:094503, Jan 2001.
170. A Himeda, T Kato, and M Ogata. Stripe states with spatially oscillating d-wave supercon-
ductivity in the two-dimensional t −t′ −J model. Phys. Rev. Lett., 88(11), Mar. 18, 2002.
171. E. Berg, E. Fradkin, E.-A. Kim, S. A. Kivelson, V. Oganesyan, J. M. Tranquada, and S. C.
Zhang. Dynamical layer decoupling in a stripe-ordered high-Tc superconductor. Phys. Rev.
Lett., 99(12), Sep 21 2007.
172. Daniel F. Agterberg, J.C. S´eamus Davis, Stephen D. Edkins, Eduardo Fradkin, Dale J.
Van Harlingen, Steven A. Kivelson, Patrick A. Lee, Leo Radzihovsky, John M. Tranquada,
and Yuxuan Wang. The physics of pair-density waves: cuprate superconductors and beyond.
Annual Review of Condensed Matter Physics, 11(1):231–270, Mar 2020.
173. Chen-Hsuan Hsu, Zhiqiang Wang, and Sudip Chakravarty. Spin dynamics of possible density
wave states in the pseudogap phase of high-temperature superconductors.
Phys. Rev. B,
86:214510, Dec 2012.
174. D. J. Scalapino, S. R. White, and I. Aﬄeck. Rung-rung current correlations on a 2-leg t-J
ladder. Phys. Rev. B, 64(10), Sep 2001.
175. S. Nishimoto, E. Jeckelmann, and D. J. Scalapino. Current-current correlations in the three-
band model for two-leg CuO ladders: Density-matrix renormalization group study. Phys. Rev.
B, 79(20), May 2009.
176. Y. F. Kung, C. C. Chen, B. Moritz, S. Johnston, R. Thomale, and T. P. Devereaux. Numerical
exploration of spontaneous broken symmetries in multiorbital Hubbard models. Phys. Rev.
B, 90(22), Dec 2014.
177. Kai Sun, Hong Yao, Eduardo Fradkin, and Steven A. Kivelson. Topological insulators and
nematic phases from spontaneous symmetry breaking in 2D Fermi systems with a quadratic
band crossing. Phys. Rev. Lett., 103(4), Jul 24 2009.
178. Peter Fulde and Richard A. Ferrell. Superconductivity in a strong spin-exchange ﬁeld. Phys.
Rev., 135:A550–A563, Aug 1964.
179. A. I. Larkin and Y. N. Ovchinnikov. Nonuniform state of superconductors. Zh. Eksp. Teor.
Fiz., 47:1136–1146, 1964.
180. Steven R. White and D. J. Scalapino.
Pairing on striped t−t
′−J lattices.
Phys. Rev. B,
79:220504, Jun 2009.
181. T. P. Devereaux. Numerical investigations of models of the cuprates (Harvard CMSC Collo-
quium). https://www.youtube.com/watch?v=mAYnLdi3vs4, Jan. 20, 2021. Presents results of
a large body of the most recent and unpublished DQMC results on the square lattice Hubbard

www.annualreviews.org • The Hubbard Model
41

## Page 42

model.
182. Erez Berg, Eduardo Fradkin, and Steven A. Kivelson. Pair-density-wave correlations in the
kondo-heisenberg model. Phys. Rev. Lett., 105:146403, Sep 2010.
183. Akbar Jaefari and Eduardo Fradkin. Pair-density-wave superconducting order in two-leg lad-
ders. Phys. Rev. B, 85:035104, Jan 2012.
184. Philippe Corboz, T. M. Rice, and Matthias Troyer.
Competing states in the t-J model:
uniform d-wave state versus stripe state. Phys. Rev. Lett., 113:046402, Jul 2014.
185. Xiao Yan Xu, K. T. Law, and Patrick A. Lee. Pair density wave in the doped t-J model with
ring exchange on a triangular lattice. Phys. Rev. Lett., 122:167001, Apr 2019.
186. E. Eisenberg, R. Berkovits, David A. Huse, and B. L. Altshuler. Breakdown of the Nagaoka
phase in the two-dimensional t-J model. Phys. Rev. B, 65:134437, Mar 2002.
187. S. Raghu. unpublished manuscript.
188. Sandro Sorella. The phase diagram of the Hubbard model by variational auxiliary ﬁeld quan-
tum Monte Carlo. arXiv:2101.07045, 2021.
189. Rahul Nandkishore, L. S. Levitov, and A. V. Chubukov. Chiral superconductivity from repul-
sive interactions in doped graphene. Nature Physics, 8(2):158–163, 2012.
190. Rahul Nandkishore, Ronny Thomale, and Andrey V. Chubukov. Superconductivity from weak
repulsion in hexagonal lattice systems. Phys. Rev. B, 89:144501, Apr 2014.
191. Antoine Georges, Gabriel Kotliar, Werner Krauth, and Marcelo J. Rozenberg.
Dynamical
mean-ﬁeld theory of strongly correlated fermion systems and the limit of inﬁnite dimensions.
Rev. Mod. Phys., 68:13–125, Jan 1996.
192. J. P. F. LeBlanc, Andrey E. Antipov, Federico Becca, Ireneusz W. Bulik, Garnet Kin-Lic Chan,
Chia-Min Chung, Youjin Deng, Michel Ferrero, Thomas M. Henderson, Carlos A. Jim´enez-
Hoyos, E. Kozik, Xuan-Wen Liu, Andrew J. Millis, N. V. Prokof’ev, Mingpu Qin, Gustavo E.
Scuseria, Hao Shi, B. V. Svistunov, Luca F. Tocchio, I. S. Tupitsyn, Steven R. White, Shiwei
Zhang, Bo-Xiao Zheng, Zhenyue Zhu, and Emanuel Gull. Solutions of the two-dimensional
Hubbard model: benchmarks and results from a wide range of numerical algorithms. Phys.
Rev. X, 5:041041, Dec 2015.
193. Paul R. C. Kent and Gabriel Kotliar.
Toward a predictive theory of correlated materials.
Science, 361(6400):348–354, 2018.
194. Arpita Paul and Turan Birol.
Applications of DFT+DMFT in materials science.
Annual
Review of Materials Research, 49:31–52, 2019.
195. T. Maier, M. Jarrell, T. Pruschke, and M.H. Hettler. Quantum cluster theories. Reviews of
Modern Physics, 77:1027, 2005.

42
Arovas et al.
