---
source_pdf: ../arxiv_2004.04174.pdf
pages: 30
extracted_at: 2026-04-17T12:32:36+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_2004.04174

Source PDF: ../arxiv_2004.04174.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Hartree-Fock on a superconducting qubit quantum computer

Google AI Quantum and Collaborators∗

(Dated: September 22, 2020)

As the search continues for useful applications of noisy intermediate scale quantum devices, vari-
ational simulations of fermionic systems remain one of the most promising directions. Here, we
perform a series of quantum simulations of chemistry which involve twice the number of qubits and
more than ten times the number of gates as the largest prior experiments. We model the binding
energy of H6, H8, H10 and H12 chains as well the isomerization of diazene. We also demonstrate
error-mitigation strategies based on N-representability which dramatically improve the eﬀective ﬁ-
delity of our experiments. Our parameterized ansatz circuits realize the Givens rotation approach
to noninteracting fermion evolution, which we variationally optimize to prepare the Hartree-Fock
wavefunction. This ubiquitous algorithmic primitive corresponds to a rotation of the orbital basis
and is required by many proposals for correlated simulations of molecules and Hubbard models.
Because noninteracting fermion evolutions are classically tractable to simulate, yet still generate
highly entangled states over the computational basis, we use these experiments to benchmark the
performance of our hardware while establishing a foundation for scaling up more complex correlated
quantum simulations of chemistry.

arXiv:2004.04174v4 [quant-ph] 18 Sep 2020

The prediction of molecular properties and chemical
reactions from ab initio quantum mechanics has emerged
as one of the most promising applications of quantum
computing [1].
This fact is due both to the commer-
cial value of accurate simulations as well as the relatively
modest number of qubits required to represent interesting
instances. However, as the age of quantum supremacy
dawns [2], so has a more complete appreciation of the
challenges required to scale such computations to the
classically intractable regime using near-term interme-
diate scale quantum (NISQ) devices. Achieving that ob-
jective will require further algorithmic innovations, hard-
ware with more qubits and low error rates, and more
eﬀective error-mitigation strategies. Here, we report a
variational quantum eigensolver (VQE) [3] simulation of
molecular systems with progress in all three directions.
We used the Google Sycamore quantum processor to
simulate the binding energy of hydrogen chains as large
as H12, as well as a chemical reaction mechanism (the
isomerization of diazene). The Sycamore quantum pro-
cessor consists of a two-dimensional array of 54 transmon
qubits [2]. Each qubit is tunably coupled to four nearest
neighbors in a rectangular lattice. Our largest simula-
tions used a dozen qubits – twice the size as the largest
prior quantum simulations of chemistry [4] – and required
only nearest-neighbor coupling (depicted in Fig. 1). Prior
simulations of chemistry on superconducting qubit de-
vices and trapped ion systems demonstrated the possibil-
ity of error mitigation through VQE [4–10], albeit on a
small scale. We demonstrated that, to within the model,
achieving chemical accuracy through VQE is possible for
intermediate scale problems when combined with eﬀec-
tive error mitigation strategies. Furthermore, we argue
that the circuit ansatz we used for VQE is especially ap-
pealing as a benchmark for chemistry.

∗Corresponding author (Nicholas Rubin): nickrubin@google.com;
Corresponding author (Ryan Babbush): babbush@google.com

We
simulated
quantum
chemistry
in
a
second-
quantized representation where the state of each of N
qubits encoded the occupancy of an orbital basis func-
tion. We used what are commonly referred to as core
orbitals as the initial orbitals (shown for H12 on the left
of Fig. 1a), which are the eigenfunctions of the molecu-
lar Hamiltonian without the electron-electron interaction
term. The goal of this experiment was to use a quan-
tum computer to implement the Hartree-Fock procedure,
which is a method for obtaining the best single-particle
orbital functions assuming each electron feels the average
potential generated from all the other electrons. This as-
sumption is enforced by constraining the wavefunction
to be a product of one-particle functions which has been
appropriately antisymmetrized to satisfy the Pauli exclu-
sion principle. An initial guess for the Hartree-Fock state,
from which we can optimize the orbitals, was obtained by
ﬁlling the lowest energy η/2 orbitals, each with a spin-up
electron and a spin-down electron, where η is the number
of electrons. Since we simulated the singlet ground state
for all molecules considered here, there is no spin com-
ponent to the mean-ﬁeld approximation; thus, we only
needed to explicitly simulate the η/2 spin-up electrons.
By performing a unitary rotation of the initial (core)
orbital basis ϕp(r), one can obtain a new valid set of
orbitals eϕp(r) as a linear combination of the initial ones:

N
X

q=1
[eκ]pq ϕq(r) ,
(1)

eϕp(r) =

where κ is an N × N anti-Hermitian matrix and [eκ]pq
is the p, q element of the matrix exponential of κ.
A
result due to Thouless [11] is that one can express the
unitary that applies this basis rotation to the quantum
state as time-evolution under a non-interacting fermion
Hamiltonian.
Speciﬁcally, if we take a†
p and ap to be
fermionic creation and annihilation operators for the core
orbital ϕp(r) then we can parameterize |ψκ⟩, an anti-
symmetric product state in the new basis eϕp(r), as non-

## Page 2

the generator for Uκ corresponds to a non-interacting
fermion Hamiltonian, its action on a product state in sec-
ond quantization can be classically simulated in O(N 3)
by diagonalizing the one-body operator and in some cases
the Hartree-Fock procedure can be made to converge
with even lower complexity.
Despite that fact, we ar-
gue that this procedure is still a compelling experiment
for a quantum computer.
The Hartree-Fock state is usually the initial state for
classical correlated electronic structure calculations such
as coupled cluster and conﬁguration interaction methods,
as well as for many quantum algorithms for chemistry.
Thus, often one chooses to work in the molecular orbital
basis, which is deﬁned so that the Hartree-Fock state
is a computational basis state. However, the molecular
orbital basis Hamiltonian has a large number of terms
which can be challenging to simulate and measure with
low complexity.
Accordingly, the most eﬃcient quan-
tum algorithms for chemistry [12–15] require that one
perform the simulation in more structured bases with
asymptotically fewer terms [16–18], necessitating that
Uκ⋆is applied explicitly at the beginning of the com-
putation. Even when simulating chemistry in an arbi-
trary basis, the most eﬃcient strategies are based on a
tensor factorization of the Hamiltonian which requires
many applications of Uκ to simulate [19, 20]. Exploiting
this tensor factorization with basis rotations is also key
to the most eﬃcient strategy for measuring ⟨H⟩in vari-
ational algorithms, and requires implementing Uκ prior
to measurement [21].
We used this variational ansatz based on basis rota-
tions to benchmark the Sycamore processor for linear
hydrogen chains of length 6, 8, 10, and 12 and two path-
ways for diazene bond isomerization. We modeled hy-
drogen chains of length N with N qubits. Our simula-
tions required N qubits to simulate 2N spin-orbitals due
to the constraint that the α-spin-orbitals have the same
spatial wavefunction as the β-spin-orbitals. For diazene
we required 10 qubits after pre-processing. The hydro-
gen chains are a common benchmark in electronic struc-
ture [22–24] and the diazene bond isomerization provides
a system where the required accuracy is more representa-
tive of typical electronic structure problems and has been
used as a benchmark for coupled cluster methods [25].
For the diazene isomerization our goal was to resolve the
energetic diﬀerence between the transition states of two
competing mechanisms, requiring accuracy of about 40
milliHartree. This objective diﬀers from prior quantum
simulations of chemistry which have focused on bond dis-
sociation curves [4–7].
One motivation for this work was to calibrate and val-
idate the performance of our device in realizing an im-
portant algorithmic primitive for quantum chemistry and
lattice model simulation. Our experiment was also ap-
pealing for benchmarking purposes since the circuits we
explored generated highly entangled states but with spe-
cial structure that enabled the eﬃcient measurement of
ﬁdelity and the determination of systematic errors. Fur-

FIG. 1. Basis rotation circuit and compilation. a) To
the left of the circuit diagram are the initial orbitals for the
H12 chain with atom spacings of 1.3 ˚A, obtained by diago-
nalizing the Hamiltonian ignoring electron-electron interac-
tions. The circuit diagram depicts the basis rotation ansatz
for a linear chain of twelve hydrogen atoms. Each grey box
with a rotation angle θ represents a Givens rotation gate. b)
Compilation of the Givens rotation gate to
√

iswap gates and
single-qubit gates that can be realized directly in hardware.
The H12 circuit involves 72
√

iswap gates and 108 single-qubit
Z rotation gates with a total of 36 variational parameters. c)
Depiction of a twelve qubit line on a subgrid of the entire
54-qubit Sycamore device. All circuits only require gates be-
tween pairs of qubits which are adjacent in a linear topology.

interacting fermion dynamics from a computational basis
state |η⟩= a†
η · · · a†
1 |0⟩in the core orbital basis:

N
X

!

p,q=1
κpqa†
paq

|ψκ⟩= Uκ |η⟩,
Uκ = exp

.
(2)

Such states are referred to as Slater determinants.

To complete the accurate preparation of Hartree-Fock
states, we implemented variational relaxation of the κ
parameters to minimize the energy of |ψκ⟩starting from
the optimal κ determined by solving the Hartree-Fock
equations classically.
This is an idealized implementa-
tion of VQE that allowed us to demonstrate error miti-
gation of coherent errors through variational relaxation.
We deﬁned the Hartree-Fock state |ψHF⟩to be the lowest
energy Slater determinant for the molecular Hamiltonian
H, i.e.

|ψHF⟩= |ψκ⋆⟩
κ⋆= argminκ ⟨ψκ| H |ψκ⟩.
(3)

We applied Uκ to |η⟩using our quantum computer and
then performed the optimization over κ through feed-
back from a classical optimization routine. The energy
decreased because the initial core orbitals were obtained
by ignoring the electron-electron interaction and varia-
tional relaxation compensates for coherent errors. Since

## Page 3

a
c

b

2.00

Energy error [Hartree]

10
1

1 - [Fidelity Witness]

10
1

2.25

Energy [Hartree]

2.50

10
2

10
2

2.75

10
3

3.00

10
3

3.25

10
4

1
2
3
Bond distance [Å]

0.5
1.0
1.5
2.0
2.5
3.0
Bond distance [Å]

e

10
1

Energy error [Hartree]

10
2

10
3

1
2
Bond distance [Å]

0
2
4
6
8
10
12
14
16
18
Optimizer Iterations

d
f

3

8 qubits
10 qubits
12 qubits

2.5

3.0

3.5

Energy [Hartree]

Energy [Hartree]

3.0

Energy [Hartree]

4

8
10
6

4.0

3.5

4.5

4.0

5.0

0.5
1.0
1.5
2.0
2.5
3.0
Bond distance [Å]

5

6

0.5
1.0
1.5
2.0
2.5
3.0
Bond distance [Å]

0.5
1.0
1.5
2.0
2.5
3.0
Bond distance [Å]

FIG. 2. Static and VQE performance on hydrogen chains. Binding curve simulations for H6, H8, H10, and H12 with
various forms of error mitigation. Subﬁgures (a, d, e, f) compare Sycamore’s raw performance (yellow diamonds) with post-
selection (green squares), puriﬁcation (blue circles), and error mitigated combined with variational relaxation (red triangles).
For all hydrogen systems the raw data at 0.5 ˚A bond length is oﬀthe top of the plot. The yellow, green, and blue points
were calculated using the optimal basis rotation angles computed from a classical simulation; thus, the variational optimization
shown here is only used to correct systematic errors in the circuit realization. Subﬁgure (b) contains the absolute error and
inﬁdelity for the H6 system. For all points we calculated a ﬁdelity witness described in Appendix D. The error bars for all points
were computed by estimating the covariance between simultaneously measured sets of 1-RDM elements and resampling those
elements under a multivariate Gaussian model. Energies from each sample were tabulated and the standard deviation is used
as the error bar. The “+PS” means applying post-selection to the raw data, “+Puriﬁcation” means applying post-selection
and McWeeny puriﬁcation, and “+VQE” means post-selection, McWeeny puriﬁcation, and variational relaxation. Subﬁgure
(c) contains optimization traces for three H6 geometries (bond distances of 0.5 ˚A, 1.3 ˚A, and 2.1 ˚A). All optimization runs used
between 18 and 30 iterations. The lowest energy solution from the optimization trace was reported.

ther motivation was to implement the largest variational
quantum simulation of chemistry so that it is possible
to better quantify the current gap between the capabili-
ties of NISQ devices and real applications. Even though
the Hartree-Fock ansatz is eﬃcient to simulate classi-
cally, the circuits in our experiment are far more complex
than prior experimental quantum simulations of chem-
istry.
Finally, the structure of the Hartree-Fock state
enabled us to sample the energy and gradients of the
variational ansatz with fewer measurements than would
typically be required, allowing us to focus on other as-
pects of quantum simulating chemistry at scale, such
as the eﬀectiveness of various types of error-mitigation.
Thus, our choice to focus on Hartree-Fock for this exper-
iment embraces the notion that we should work towards
valuable quantum simulations of chemistry by ﬁrst scal-
ing up important components of the exact solution (e.g.,
error-mitigation strategies and basis rotations) in a fash-
ion that enables us to completely understand and perfect
those primitives.
Variational algorithms are speciﬁed in the form of a
functional minimization.
This minimization has three

main components: ansatz speciﬁcation in the form of a
parameterized quantum circuit (the function), observable
estimation (the functional), and outer-loop optimization
(the minimization). Each component is distinctively af-
fected by our choice to simulate a model corresponding
to non-interacting fermion wavefunctions.
Symmetries
built into this ansatz allowed for reduction of the num-
ber of qubits required to simulate molecular systems, a
reduction in the number of measurements needed to es-
timate the energy, and access to the gradient without
additional measurements beyond those required for en-
ergy estimation. See Appendix A for details on how we
realized Hartree-Fock with VQE.
The unitary in Eq. (2) can be compiled exactly (with-
out Trotterization) using a procedure based on Givens
rotations.
This strategy was ﬁrst suggested for quan-
tum computing in work on linear optics in [26] and later
in the context of fermionic simulations in [27].
Here,
we implemented these basis rotations using the optimal
compilation of [28] that has gate depth N/2 and requires
only η(N −η) two qubit “Givens rotation” gates on a
linearly connected architecture, giving one rotation for

## Page 4

FIG. 3. VQE performance on distinguishing the mech-
anism of diazene isomerization. Hartree-Fock curves for
diazene isomerization between cis and trans conﬁgurations.
TS1 and TS2 are the transition states for the in-plane and
out-of-plane rotation of the hydrogen, respectively. The yel-
low arrows on TS1 and TS2 indicate the corresponding reac-
tion coordinate. The solid curve is the energy obtained from
optimizing a 10-qubit problem generated by freezing the core
orbitals generated from two self-consistent-ﬁeld cycles. The
transparent lines of the same color are the full 12 qubit system
indicating that freezing the lowest two levels does not change
the characteristics of the model chemistry. Nine points along
the reaction paths are simulated on Sycamore using VQE.
We allowed the optimizer 30 iterations for all points except
for ﬁfth and sixth point from the left of the in-plane rota-
tion curve which we allowed 60 steps. The error bars for all
points were computed by estimating the covariance between
simultaneously measured sets of 1-RDM elements and resam-
pling those elements under a multivariate Gaussian model.
Energies from each sample were tabulated and the standard
deviation is used as the error bar. No puriﬁcation was applied
for the computation of the error bar. If puriﬁcation is applied
the error bars become smaller than the markers. Each ba-
sis rotation for diazene contains 50
√

iswap gates and 80 Rz
gates.

each element in the unitary basis change. These Givens
rotation gates were implemented by decomposition into
two
√

iswap gates and three Rz gates.
In Fig. 1, we
depict the basis change circuit for the H12 chain, which
has a diamond shaped structure. We further review the
compilation of these circuits in Appendix B.
The average energy of any molecular system can be
evaluated with knowledge of the one-particle reduced
density matrix (1-RDM), ⟨a†
paq⟩, and the two-particle re-
duced density matrix (2-RDM), ⟨a†
pa†
qaras⟩. In general,
it is not possible to exactly reconstruct the 2-RDM from
knowledge of just the 1-RDM. However, for single-Slater
determinants (as in our Hartree-Fock experiment), the
2-RDM is completely determined by the 1-RDM [29]:

⟨a†
pa†
qaras⟩= ⟨a†
pas⟩⟨a†
qar⟩−⟨a†
qas⟩⟨a†
par⟩.
(4)

Thus, in our experiment we only needed to sample the 1-
RDM to estimate the energy. As the 2-RDM has quadrat-
ically more elements than the 1-RDM, this approach is a
signiﬁcant simpliﬁcation. We measured the 1-RDM using

1-RDM elements with N + 1 distinct circuits. For each
distinct circuit we made 250,000 measurements.
We performed two types of error mitigation on our
measured data: post-selection on particle number (con-
served in basis rotations) and pure-state projection. To
apply post-selection we modiﬁed our circuits by ﬁrst ro-
tating into a basis that diagonalizes a†
paq + a†
qap for N
diﬀerent pairs of p and q so that these elements could be
sampled at the same time as the total particle-number
operator.
Following the strategy in Appendix C, this
measurement was accomplished at the cost of two T gates
and one
√

iswap gate per pair of qubits. We then post-
selected to discard measurements where the total number
of excitations changed from η/2.
For pure-state puriﬁcation, we leveraged the fact that
the 1-RDM for any single-Slater determinant wavefunc-
tion |ψκ⟩has eigenvalues restricted to be 0 and 1 [30].
We performed projection back to the pure-set of 1-
RDMs using a technique known as McWeeny puriﬁ-
cation
[29].
Details on the procedure and sampling
bounds for guaranteeing the procedure has a ﬁxed-point
1-RDM corresponding to a Slater determinant can be
found in Appendix E. Although McWeeny puriﬁcation
only works for Slater determinant wavefunctions, pure-
state N-representability conditions are known for more
general systems [31] and we expect that a computational
procedure similar to enforcing ensemble constraints could
be employed [32, 33].

A variety of circuit optimization techniques based on
gradient- and gradient-free methods have been proposed
in the context of NISQ algorithms. Here, we developed
an optimization technique that exploits local gradient
and Hessian information in a fashion which is distinctive
to the Hartree-Fock model.
It is based on a proposal
for iterative construction of a wavefunction to satisfy
the Brillouin condition for a single-particle model [34].
Our optimization protocol used the property that at
a local optima the commutator of the Hamiltonian H
with respect to any generator of rotation G is zero
(i.e. ⟨ψ| [H, G] |ψ⟩= 0) and the fact that sequential basis
change circuits can be concatenated into a single basis
change circuit (i.e. UaUb = Uab). Using these relations
and taking G = P

pq κpqa†
paq, as in our experiment, the
double commutator ⟨ψ|[[H, G], G]|ψ⟩determined an aug-
mented Hessian (matrix of derivatives) which we could
use to iteratively update the wavefunction such that the
ﬁrst order condition was approximately satisﬁed. Regu-
larization was added by limiting the size of update pa-
rameters [35]. For details, see Appendix H.
As a benchmark, we studied symmetrically stretched
hydrogen chains of length 6, 8, 10, and 12 atoms, Fig. 2.
The initial parameters were set to the parameters ob-
tained by solving the Hartree-Fock equations on a classi-
cal computer. The data from the quantum computer is
plotted along with classical Hartree-Fock results, showing
better and better agreement as we added post-selection,

## Page 5

respect to the simulated model.
Correctly identifying
this pathway requires resolving the energy gap of 40 milli-
Hartree between the two transition states. The pathways
correspond to the motion of the hydrogen in the process
of converting cis-diazene to trans-diazene. One mecha-
nism is in-plane rotation of a hydrogen and the other is
an out-of-plane rotation corresponding to rotation of the
HNNH dihedral angle. Fig. 3 contains VQE optimized
data simulating nine points along the reaction coordi-
nates for in-plane and out-of-plane rotation of hydrogen.
For all points along the reaction coordinate the initial
parameter setting was the solution to the Hartree-Fock
equations. VQE produced 1-RDMs with average ﬁdelity
greater than 0.98 after error-mitigation. Once again, we
see that our full error mitigation procedure signiﬁcantly
improves the accuracy of our calculation.
Our VQE calculations on diazene predicted the correct
ordering of the transition states to within the chemical
model with an energy gap of 41 ± 6 milliHartree and
the true gap is 40.2 milliHartree.
We provide a more
detailed analysis of the error mitigation performance on
the diazene circuits in Appendix F considering that the
√

TABLE I. Average ﬁdelity lower bounds for hydro-
gen chain calculations.
We report values of the ﬁ-
delity witness from [36], averaged across H-H separations of
{0.5, 0.9, 1.3, 1.7, 2.1, 2.5} ˚A, starting from circuits with the
theoretically optimal variational parameters (κ). “estimate”
corresponds to an estimate of the ﬁdelity derived by multiply-
ing gate errors assuming 0.5 percent single-qubit gate error,
1 percent two-qubit gate error and 3 percent readout error.
“Raw” corresponds to ﬁdelities from constructing the 1-RDM
without any error mitigation. “+ps” corresponds to ﬁdelities
from constructing the 1-RDM with post-selection on particle
number. “+pure” corresponds to ﬁdelities from constructing
the 1-RDM with post-selection and applying puriﬁcation as
post-processing.
Finally, “+VQE” corresponds to ﬁdelities
from using all previously mentioned error mitigation tech-
niques in conjunction with variational relaxation. Note that
for small values (such as the “raw” value for H12) we expect
the ﬁdelity lower-bound is more likely to be loose.

iswap gates we used had a residual cphase(π/24) and
Rz gates had stochastic control angles. This simulation
reinforced VQEs ability to mitigate systematic errors at
the scale of 50
√

post-selection and puriﬁcation, and then error mitigated
variational relaxation. The 6- and 8-qubit data achieved
chemical accuracy after VQE, and even the 12-qubit data
followed the expected energy closely. The error data in
Fig. 2b and the other inserts are remarkable as they show
a large and consistent decrease, about a factor of 100,
when using these protocols. Fig. 2c details the signiﬁ-
cant decrease in error using a modest number of VQE
iterations.
A ﬁdelity witness can be eﬃciently computed from the
experimental data [36]; see Appendix D 2. This value is
a lower bound to the true ﬁdelity, and thus potentially
loose when ﬁdelity is small. However, Fig. 2b demon-
strates that this ﬁdelity generally tracks the measured
errors. Table I shows how ﬁdelity increased as we added
various forms of error mitigation, starting on the left col-
umn where the optimal angles were computed classically.
Uncertainties in the last digit, indicated in the paren-
thesis, are calculated by the procedure described in Ap-
pendix C 5. The ﬁrst column of Table I is an estimate
of the ﬁdelity based on multiplying the ﬁdelity for all
the gates and readout assuming 99.5% ﬁdelity for single
qubit gates, 99% ﬁdelity for two-qubit gates, and 97% ﬁ-
delity for readout. We see that this estimate qualitatively
follows the “raw” ﬁdelity witness estimates except when
the witness value is very small. For all hydrogen systems
studied, we observed drastic ﬁdelity improvements with
combined error mitigation.
Diazene isomerization. We simulated two isomer-
ization pathways for diazene, marking the ﬁrst time that
a chemical reaction mechanism has been modelled using
a quantum computer. It is known that Hartree-Fock the-
ory reverses the order of the transition states; however,
here we focused on the accuracy of the computation with

iswap gates and over 80 Rz gates.
In this work we took a step towards answering the
question of whether NISQ computers can oﬀer quantum
advantage for chemical simulation by studying VQE per-
formance on basis rotation circuits that are widely used in
quantum algorithms for fermionic simulation. The con-
sidered ansatz aﬀorded ways to minimize the resource
requirements for VQE and study device performance for
circuits that are similar to those needed for full Hamilto-
nian simulation. These basis rotation circuits also made
an attractive benchmark due to their prevalence, opti-
mal known compilation, the ability to extract ﬁdelity
and ﬁdelity witness values and the fact that they pa-
rameterize a continuous family of analytically solvable
circuits demonstrating a high degree of entanglement.
The circuits also serve as a natural progression towards
more correlated ansatze such as a generalized swap net-
work [28] or a non-particle conserving circuit ansatz fol-
lowed by particle number projection.

We demonstrated the performance of two error mitiga-
tion techniques on basis rotation circuit ﬁdelity. The ﬁrst
is post-selection on total occupation number when mea-
suring all elements of the 1-RDM. This step was accom-
plished by permuting the basis rotation circuit such that
all measurements involved estimating nearest-neighbor
observables and measuring each pair of observables such
that the total occupation number is preserved. The sec-
ond is the application of McWeeny puriﬁcation as a post-
processing step. The energy improvements from project-
ing back to the pure-state N-representable manifold was
evidence that generalized pure-state N-representability
conditions would be instrumental in making NISQ chem-
istry computations feasible.
This fact underscores the

## Page 6

importance of developing procedures for applying pure-
state N-representability conditions in a more general con-
text. The post-selection and RDM measurement tech-
niques can be generalized to measuring all 1-RDM and 2-
RDM elements when considering a less restrictive circuit
ansatz by permuting the labels of the fermionic modes.
For ansatz such as the generalized swap network [28] the
circuit structure would not change, only the rotation an-
gles. Thus, the measurement schemes presented here are
applicable in the more general case. Furthermore, it is
important to understand the performance of these error
mitigation techniques when combined with alternatives
such as noise extrapolation [37].

Finally, we were able to show further evidence that
variational relaxation eﬀectively mitigates coherent er-
rors arising in implementation of physical gates.
The
performance of our problem speciﬁc optimization strat-
egy motivates the study of iterative wavefunction con-
structions [38] in a more general setting.
The combi-
nation of these error mitigation techniques with VQE
unambiguously resolved a chemical mechanism to within
the model chemistry using a quantum computation. It
is still an open question whether NISQ devices will be
able to simulate challenging quantum chemistry systems
and it is likely that major innovations would be required.

Google AI Quantum and Collaborators

However, we ﬁnd the accuracy of these experiments and
the eﬀectiveness of these error-mitigation procedures to
be an encouraging signal of progress in that direction.

ACKNOWLEDGEMENTS

D.B. is a CIFAR Associate Fellow in the Quantum In-
formation Science Program. Funding: This work was
supported by Google. Competing Interests: The au-
thors declare no competing interests. Author Contri-
butions: N.C.R. designed the experiment. C.N. assisted
with data collection. Z.J., V.S., and N.W. assisted with
analytical calculations and gate synthesis. N.C.R. and
R.B. wrote the paper. Experiments were performed us-
ing a quantum processor that was recently developed and
fabricated by a large eﬀort involving the entire Google
Quantum team.
Data and materials availability:
The code used for this experiment and a tutorial for run-
ning it can be found in the open source library Recirq,
located at https://github.com/quantumlib/ReCirq/
tree/master/recirq. All data needed to evaluate the
conclusions in the paper are present in the paper or the
Supplementary Materials. Data presented in the ﬁgures
can be found in the Dryad repository located at [39]

Frank Arute1, Kunal Arya1, Ryan Babbush1, Dave Bacon1, Joseph C. Bardin1, 2, Rami Barends1, Sergio Boixo1,
Michael Broughton1, Bob B. Buckley1, David A. Buell1, Brian Burkett1, Nicholas Bushnell1, Yu Chen1, Zijun
Chen1, Benjamin Chiaro1, 3, Roberto Collins1, William Courtney1, Sean Demura1, Andrew Dunsworth1, Daniel
Eppens1, Edward Farhi1, Austin Fowler1, Brooks Foxen1, Craig Gidney1, Marissa Giustina1, Rob Graﬀ1, Steve
Habegger1, Matthew P. Harrigan1, Alan Ho1, Sabrina Hong1, Trent Huang1, William J. Huggins1, 4, Lev Ioﬀe1,
Sergei V. Isakov1, Evan Jeﬀrey1, Zhang Jiang1, Cody Jones1, Dvir Kafri1, Kostyantyn Kechedzhi1, Julian Kelly1,
Seon Kim1, Paul V. Klimov1, Alexander Korotkov1, 5, Fedor Kostritsa1, David Landhuis1, Pavel Laptev1, Mike
Lindmark1, Erik Lucero1, Orion Martin1, John M. Martinis1, 3, Jarrod R. McClean1, Matt McEwen1, 3, Anthony
Megrant1, Xiao Mi1, Masoud Mohseni1, Wojciech Mruczkiewicz1, Josh Mutus1, Ofer Naaman1, Matthew Neeley1,
Charles Neill1, Hartmut Neven1, Murphy Yuezhen Niu1, Thomas E. O’Brien1, Eric Ostby1, Andre Petukhov1,
Harald Putterman1, Chris Quintana1, Pedram Roushan1, Nicholas C. Rubin1, Daniel Sank1, Kevin J. Satzinger1,
Vadim Smelyanskiy1, Doug Strain1, Kevin J. Sung1, 6, Marco Szalay1, Tyler Y. Takeshita7, Amit Vainsencher1,
Theodore White1, Nathan Wiebe1, 8, 9, Z. Jamie Yao1, Ping Yeh1, Adam Zalcman1

1 Google Research
2 Department of Electrical and Computer Engineering, University of Massachusetts, Amherst, MA
3 Department of Physics, University of California, Santa Barbara, CA
4 Department of Chemistry, University of California, Berkeley, CA
5 Department of Electrical and Computer Engineering, University of California, Riverside, CA
6 Department of Electrical Engineering and Computer Science, University of Michigan, Ann Arbor, MI
7 Mercedes-Benz Research and Development, North America, Sunnyvale, CA
8 Department of Physics, University of Washington, Seattle, WA
9 Paciﬁc Northwest National Laboratory, Richland, WA

[1] Alan Aspuru-Guzik, Anthony D Dutoi, Peter J Love,
and Martin Head-Gordon, “Simulated Quantum Compu-
tation of Molecular Energies,” Science 309, 1704 (2005).

## Page 7

[2] Frank Arute, Kunal Arya, Ryan Babbush, Dave Bacon,
Joseph C. Bardin, Rami Barends, Rupak Biswas, Sergio
Boixo, Fernando G. S. L. Brandao, David A. Buell, Brian
Burkett, Yu Chen, Zijun Chen, Ben Chiaro, Roberto
Collins, William Courtney, Andrew Dunsworth, Ed-
ward Farhi, Brooks Foxen, Austin Fowler, Craig Gidney,
Marissa Giustina, Rob Graﬀ, Keith Guerin, Steve Habeg-
ger, Matthew P. Harrigan, Michael J. Hartmann, Alan
Ho, Markus Hoﬀmann, Trent Huang, Travis S. Humble,
Sergei V. Isakov, Evan Jeﬀrey, Zhang Jiang, Dvir Kafri,
Kostyantyn Kechedzhi, Julian Kelly, Paul V. Klimov,
Sergey Knysh, Alexander Korotkov, Fedor Kostritsa,
David Landhuis, Mike Lindmark, Erik Lucero, Dmitry
Lyakh, Salvatore Mandr`a, Jarrod R. McClean, Matthew
McEwen, Anthony Megrant, Xiao Mi, Kristel Michielsen,
Masoud Mohseni, Josh Mutus, Ofer Naaman, Matthew
Neeley, Charles Neill, Murphy Yuezhen Niu, Eric Os-
tby, Andre Petukhov, John C. Platt, Chris Quintana,
Eleanor G. Rieﬀel, Pedram Roushan, Nicholas C. Ru-
bin, Daniel Sank, Kevin J. Satzinger, Vadim Smelyan-
skiy, Kevin J. Sung, Matthew D. Trevithick, Amit
Vainsencher,
Benjamin Villalonga,
Theodore White,
Z. Jamie Yao, Ping Yeh, Adam Zalcman, Hartmut Neven,
and John M. Martinis, “Quantum supremacy using a
programmable superconducting processor,” Nature 574,
505–510 (2019).
[3] Alberto Peruzzo, Jarrod McClean, Peter Shadbolt, Man-
Hong Yung, Xiao-Qi Zhou, Peter J Love, Alan Aspuru-
Guzik, and Jeremy L O’Brien, “A Variational Eigenvalue
Solver on a Photonic Quantum Processor,” Nature Com-
munications 5, 1–7 (2014).
[4] Abhinav Kandala, Antonio Mezzacapo, Kristan Temme,
Maika Takita, Markus Brink, Jerry M Chow,
and
Jay M Gambetta, “Hardware-eﬃcient variational quan-
tum eigensolver for small molecules and quantum mag-
nets,” Nature 549, 242–246 (2017).
[5] P J J O’Malley, R Babbush, I D Kivlichan, J Romero,
J R McClean, R Barends, J Kelly, P Roushan, A Tran-
ter, N Ding, B Campbell, Y Chen, Z Chen, B Chiaro,
A Dunsworth, A G Fowler, E Jeﬀrey, A Megrant, J Y
Mutus, C Neill, C Quintana, D Sank, A Vainsencher,
J Wenner, T C White, P V Coveney, P J Love, H Neven,
A Aspuru-Guzik, and J M Martinis, “Scalable Quantum
Simulation of Molecular Energies,” Physical Review X 6,
31007 (2016).
[6] Cornelius Hempel, Christine Maier, Jonathan Romero,
Jarrod McClean, Thomas Monz, Heng Shen, Petar Ju-
rcevic, Ben P. Lanyon, Peter Love, Ryan Babbush, Al´an
Aspuru-Guzik, Rainer Blatt,
and Christian F. Roos,
“Quantum chemistry calculations on a trapped-ion quan-
tum simulator,” Physical Review X 8, 031022 (2018).
[7] Abhinav Kandala, Kristan Temme, Antonio D C´orcoles,
Antonio Mezzacapo, Jerry M Chow,
and Jay M Gam-
betta, “Error mitigation extends the computational reach
of a noisy quantum processor,” Nature 567, 491–495
(2019).
[8] James I Colless,
Vinay V Ramasesh,
Dar Dahlen,
Machiel S Blok, Jarrod R McClean, Jonathan Carter,
Wibe A de Jong,
and Irfan Siddiqi, “Robust Determi-
nation of Molecular Spectra on a Quantum Processor,”
Physical Review X 8, 011021 (2018).
[9] Scott E. Smart and David A. Mazziotti, “Quantum-
classical hybrid algorithm using an error-mitigating n-
representability condition to compute the mott metal-

insulator transition,” Physical Review A 100, 022517
(2019).
[10] R. Sagastizabal, X. Bonet-Monroig, M. Singh, M. A.
Rol, C. C. Bultink, X. Fu, C. H. Price, V. P. Os-
troukh, N. Muthusubramanian, A. Bruno, M. Beekman,
N. Haider, T. E. O’Brien, and L. DiCarlo, “Experimen-
tal error mitigation via symmetry veriﬁcation in a vari-
ational quantum eigensolver,” Physical Review A 100,
010302 (2019).
[11] David J Thouless, “Stability conditions and nuclear ro-
tations in the Hartree-Fock theory,” Nuclear Physics 21,
225–232 (1960).
[12] Guang Hao Low and Nathan Wiebe, “Hamiltonian Sim-
ulation in the Interaction Picture,” arXiv:1805.00675
(2018).
[13] Ryan Babbush, Dominic W. Berry, Jarrod R. McClean,
and Hartmut Neven, “Quantum Simulation of Chemistry
with Sublinear Scaling in Basis Size,” npj Quantum In-
formation 5, 92 (2019).
[14] Andrew M Childs, Yuan Su, Minh C Tran, Nathan
Wiebe,
and Shuchen Zhu, “A theory of trotter error,”
arXiv:1912.08854 (2019).
[15] Ryan Babbush, Craig Gidney, Dominic Berry, Nathan
Wiebe,
Jarrod
McClean,
Alexandru
Paler,
Austin
Fowler, and Hartmut Neven, “Encoding Electronic Spec-
tra in Quantum Circuits with Linear T Complexity,”
Physical Review X 8, 041015 (2018).
[16] Ryan Babbush, Nathan Wiebe, Jarrod McClean, James
McClain, Hartmut Neven,
and Garnet Kin-Lic Chan,
“Low-Depth Quantum Simulation of Materials,” Physi-
cal Review X 8, 011044 (2018).
[17] Steven R White, “Hybrid grid/basis set discretizations
of the Schr¨odinger equation,” The Journal of Chemical
Physics 147, 244102 (2017).
[18] Jarrod R McClean, Fabian M Faulstich, Qinyi Zhu,
Bryan
O’Gorman,
Yiheng
Qiu,
Steven
R
White,
Ryan Babbush,
and Lin Lin, “Discontinuous galerkin
discretization for quantum simulation of chemistry,”
arXiv:1909.00028 (2019).
[19] Mario Motta, Erika Ye, Jarrod R. McClean, Zhendong Li,
Austin J. Minnich, Ryan Babbush, and Garnet Kin-Lic
Chan, “Low Rank Representations for Quantum Simula-
tion of Electronic Structure,” arXiv:1808.02625 (2018).
[20] Dominic Berry, Craig Gidney, Mario Motta, Jarrod Mc-
Clean,
and Ryan Babbush, “Qubitization of Arbitrary
Basis Quantum Chemistry Leveraging Sparsity and Low
Rank Factorization,” Quantum 3, 208 (2019).
[21] William J Huggins, Jarrod McClean, Nicholas Rubin,
Zhang Jiang, Nathan Wiebe, K Birgitta Whaley,
and
Ryan Babbush, “Eﬃcient and noise resilient measure-
ments for quantum chemistry on near-term quantum
computers,” arXiv:1907.13117 (2019).
[22] Mario Motta, David M. Ceperley, Garnet Kin-Lic Chan,
John A. Gomez, Emanuel Gull, Sheng Guo, Carlos A.
Jim´enez-Hoyos, Tran Nguyen Lan, Jia Li, Fengjie Ma,
Andrew J. Millis, Nikolay V. Prokof’ev, Ushnish Ray,
Gustavo E. Scuseria, Sandro Sorella, Edwin M. Stouden-
mire, Qiming Sun, Igor S. Tupitsyn, Steven R. White,
Dominika Zgid, and Shiwei Zhang (Simons Collaboration
on the Many-Electron Problem), “Towards the solution
of the many-electron problem in real materials: Equation
of state of the hydrogen chain with state-of-the-art many-
body methods,” Physical Review X 7, 031059 (2017).
[23] Peter A Limacher, Paul W Ayers, Paul A Johnson, Stijn

## Page 8

De Baerdemacker, Dimitri Van Neck, and Patrick Bult-
inck, “A new mean-ﬁeld method suitable for strongly cor-
related electrons: Computationally facile antisymmetric
products of nonorthogonal geminals,” Journal of chemi-
cal theory and computation 9, 1394–1401 (2013).
[24] Johannes Hachmann, Wim Cardoen,
and Garnet Kin-
Lic Chan, “Multireference correlation in long molecules
with the quadratic scaling density matrix renormaliza-
tion group,” The Journal of chemical physics 125, 144101
(2006).
[25] Rajat K Chaudhuri, Karl F Freed, Sudip Chattopadhyay,
and Uttam Sinha Mahapatra, “Potential energy curve
for isomerization of N2H2 and C2H4 using the improved
virtual orbital multireference moller-plesset perturbation
theory,” The Journal of Chemical Physics 128, 144304
(2008).
[26] Michael Reck, Anton Zeilinger, Herbert J. Bernstein,
and Philip Bertani, “Experimental realization of any dis-
crete unitary operator,” Physical Review Letters 73, 58–
61 (1994).
[27] Dave Wecker, Matthew B Hastings, Nathan Wiebe,
Bryan K Clark, Chetan Nayak,
and Matthias Troyer,
“Solving strongly correlated electron models on a quan-
tum computer,” Physical Review A 92, 62318 (2015).
[28] Ian D Kivlichan, Jarrod McClean, Nathan Wiebe, Craig
Gidney,
Alan Aspuru-Guzik,
Garnet Kin-Lic Chan,
and Ryan Babbush, “Quantum Simulation of Electronic
Structure with Linear Depth and Connectivity,” Physical
Review Letters 120, 110501 (2018).
[29] R. McWeeny, “Some recent advances in density matrix
theory,” Reviews of Modern Physics 32, 335–369 (1960).
[30] A. J. Coleman, “Structure of fermion density matrices,”

mura, Andrew Dunsworth, Edward Farhi, Austin Fowler,
Brooks Foxen, Craig Gidney, Marissa Giustina, Rob
Graﬀ, Steve Habegger, Matthew Harrigan, Alan Ho,
Sabrina Hong, Trent Huang, William Huggins, Lev
Ioﬀe, Sergei Isakov, Evan Jeﬀrey, Zhang Jiang, Cody
Jones, Dvir Kafri, Kostyantyn Kechedzhi, Julian Kelly,
Seon Kim, Paul Klimov, Alexander Korotkov, Fedor
Kostritsa, David Landhuis, Pavel Laptev, Mike Lind-
mark, Erik Lucero, Orion Martin, John Martinis, Jarrod
McClean, Matt McEwen, Anthony Megrant, Xiao Mi,
Masoud Mohseni, Wojciech Mruczkiewicz, Josh Mutus,
Ofer Naaman, Matthew Neeley, Charles Neill, Hartmut
Neven, Murphy Yuezhen Niu, Thomas O’Brien, Eric Os-
tby, Andre Petukhov, Harald Putterman, Chris Quin-
tana, Pedram Roushan, Nicholas Rubin, Daniel Sank,
Kevin Satzinger, Vadim Smelyanskiy, Doug Strain, Kevin
Sung, Marco Szalay, Tyler Takeshita, Amit Vainsencher,
Theodore White, Nathan Wiebe, Z. Jamie Yao, Ping
Yeh, and Adam Zalcman, “Hartree-fock on a supercon-
ducting qubit quantum computer,” (2020).
[40] Attila Szabo and Neil S Ostlund, Modern quantum chem-
istry: introduction to advanced electronic structure theory
(Courier Corporation, 2012).
[41] Zhang Jiang, Kevin J. Sung, Kostyantyn Kechedzhi,
Vadim N. Smelyanskiy,
and Sergio Boixo, “Quantum
algorithms to simulate many-body physics of correlated
fermions,” Physical Review Applied 9, 044036 (2018).
[42] Anmer Daskin and Sabre Kais, “Decomposition of uni-
tary matrices for ﬁnding quantum circuits: application
to molecular hamiltonians,” The Journal of chemical
physics 134, 144112 (2011).
[43] Tyler Takeshita, Nicholas C. Rubin, Zhang Jiang, Eun-
seok Lee, Ryan Babbush, and Jarrod R. McClean, “In-
creasing the representation accuracy of quantum simu-
lations of chemistry without extra quantum resources,”
Physical Review X 10, 011004 (2020).
[44] Alexander
J
McCaskey,
Zachary
P
Parks,
Jacek
Jakowski, Shirley V Moore, Titus D Morris, Travis S
Humble,
and Raphael C Pooser, “Quantum chemistry
as a benchmark for near-term quantum computers,” npj
Quantum Information 5, 1–8 (2019).
[45] Roger A Horn and Charles R Johnson, Matrix analysis
(Cambridge university press, 2012).
[46] RM Wilcox, “Exponential operators and parameter dif-
ferentiation in quantum physics,” Journal of Mathemat-
ical Physics 8, 962–982 (1967).
[47] Trygve Helgaker, Poul Jorgensen,
and Jeppe Olsen,
Molecular Electronic Structure Theory (Wiley, 2002).
[48] P. V. Klimov, J. Kelly, Z. Chen, M. Neeley, A. Megrant,
B. Burkett, R. Barends, K. Arya, B. Chiaro, Yu Chen,
A.
Dunsworth,
A.
Fowler,
B.
Foxen,
C.
Gidney,
M. Giustina, R. Graﬀ, T. Huang, E. Jeﬀrey, Erik
Lucero, J. Y. Mutus, O. Naaman, C. Neill, C. Quintana,
P. Roushan, Daniel Sank, A. Vainsencher, J. Wenner,
T. C. White, S. Boixo, R. Babbush, V. N. Smelyan-
skiy, H. Neven,
and John M. Martinis, “Fluctuations
of energy-relaxation times in superconducting qubits,”
Phys. Rev. Lett. 121, 090502 (2018).
[49] Jarrod R McClean, Kevin J Sung, Ian D Kivlichan,
Yudong Cao, Chengyu Dai, E Schuyler Fried, Craig Gid-
ney, Brendan Gimby, Thomas H¨aner, Tarini Hardikar,
Vojtch Havl´ıˇcek, Oscar Higgott, Cupjin Huang, Josh
Izaac, Zhang Jiang, Xinle Liu, Sam McArdle, Matthew
Neeley, Thomas O’Brien, Bryan O’Gorman, Isil Ozﬁdan,

Reviews of Modern Physics 35, 668–686 (1963).
[31] David A. Mazziotti, “Pure-n-representability conditions
of two-fermion reduced density matrices,” Phys. Rev. A
94, 032516 (2016).
[32] Nicholas C. Rubin, Ryan Babbush, and Jarrod McClean,
“Application of fermionic marginal constraints to hybrid
quantum algorithms,” New Journal of Physics 20, 053020
(2018).
[33] Alexander A Klyachko, “Quantum marginal problem and
n-representability,” in Journal of Physics:
Conference
Series, Vol. 36 (IOP Publishing, 2006) p. 72.
[34] Werner Kutzelnigg, “Generalized k-particle brillouin con-
ditions and their use for the construction of correlated
electronic wavefunctions,” Chemical Physics Letters 64,
383–387 (1979).
[35] Qiming Sun, “Co-iterative augmented hessian method for
orbital optimization,” arXiv:1610.08423 (2016).
[36] M. Gluza, M. Kliesch, J. Eisert, and L. Aolita, “Fidelity
witnesses for fermionic quantum simulations,” Physical
Review Letters 120, 190501 (2018).
[37] Kristan Temme, Sergey Bravyi,
and Jay M. Gam-
betta, “Error mitigation for short-depth quantum cir-
cuits,” Phys. Rev. Lett. 119, 180509 (2017).
[38] Harper R Grimsley, Sophia E Economou, Edwin Barnes,
and Nicholas J Mayhall, “An adaptive variational algo-
rithm for exact molecular simulations on a quantum com-
puter,” Nature communications 10, 1–9 (2019).
[39] Frank Arute, Kunal Arya, Ryan Babbush, Dave Bacon,
Joseph Bardin, Rami Barends, Sergio Boixo, Michael
Broughton, Bob B. Buckley, David Buell, Brian Bur-
kett, Nicholas Bushnell, Yu Chen, Zijun Chen, Ben
Chiaro, Roberto Collins, William Courtney, Sean De-

## Page 9

Maxwell D Radin, Jhonathan Romero, Nicholas Rubin,
Nicolas P. D. Sawaya, Kanav Setia, Sukin Sim, Damian S
Steiger, Mark Steudtner, Qiming Sun, Wei Sun, Daochen
Wang, Fang Zhang, and Ryan Babbush, “OpenFermion:
The Electronic Structure Package for Quantum Comput-
ers,” arXiv:1710.07629 (2017).
[50] Robert M Parrish, Lori A Burns, Daniel G A Smith, An-
drew C Simmonett, A Eugene DePrince, Edward G Ho-
henstein, Uur Bozkaya, Alexander Yu. Sokolov, Roberto
Di Remigio, Ryan M Richard, Jrme F Gonthier, An-

drew M James, Harley R McAlexander, Ashutosh Ku-
mar, Masaaki Saitow, Xiao Wang, Benjamin P Pritchard,
Prakash Verma, Henry F Schaefer, Konrad Patkowski,
Rollin A King, Edward F Valeev, Francesco A Evange-
lista, Justin M Turney, T Daniel Crawford, and C David
Sherrill, “Psi4 1.1: An Open-Source Electronic Structure
Program Emphasizing Automation, Advanced Libraries,
and Interoperability,” Journal of Chemical Theory and
Computation 13, 3185–3197 (2017).

## Page 10

Appendix A: Hartree-Fock Theory via Canonical Transformations

In this section we derive Hartree-Fock theory from the perspective of canonical transformations. This derivation
follows an original work by David Thouless [11] and is reproduced here due to its foundational importance to the
formulation of this experiment.
In Hartree-Fock theory one attempts to solve the time-independent Schr¨odinger
equation using a state ansatz that is an antisymmetrized product of one-particle functions. Starting from an arbitrary
orthogonal basis {φi} the goal is to variationally optimize the wavefunction

|ψ(r1, ..., rn)⟩= (n!)−1/2An (χ1(r1)...χn(rn))
(A1)

j cj
iφj(r) in terms of the coeﬃcients for χ. This antisymmetrized
product of one-particle functions is commonly expressed in a more compact form as a determinant of a matrix whose
elements are the functions χi(rj) with i indexing the column and j indexing the row of this matrix. This representation
of the antisymmetrized product through a determinant is why this wavefunction ansatz is commonly referred to as a
Slater determinant.
The variational principle for the Schr¨odinger equation can be stated as

where An is the antisymmetrizer and χi(r) = P

⟨δψ|H|ψ⟩= 0
(A2)

which is a statement that the energy is stationary with respect to ﬁrst order changes in the wavefunction. In second
quantization a single antisymmetrized product of orbitals corresponds to a product of ladder operators acting on the
vacuum to “create” a representation of the antisymmetrized wavefunction





n
Y

i=1
a†
i|0⟩=
1
√

⟨r|ψ⟩=⟨r|

n!
Det










χ1(r1)
...
χ1(rn)
...
...
...
χn(r1) ... χn(rn)

.
(A3)




Assuming we are working in a ﬁxed particle manifold and given the aforementioned complete set of one-particle
functions is used as a basis we can index the functions used in the product wavefunction by i and those not used are
labeled by a then any change in the wavefunction is generated by

⟨δψ| = ⟨ψ|a†
iaaζ
(A4)

where ζ is the ﬁrst order change to an orbital χi. This fact is because any unitary generator that has only indices
{a} or {i} merely changes the phase on the state and thus is not observable [40]. Evaluating Eq. (A2) one arrives at
an expression for the stationarity of the state

⟨ψ|a†
iaaH|ψ⟩= 0.
(A5)

All the quantities in Eq. (A5) can be evaluated using Wick’s theorem given the initial state ψ is a product state
and ar|0⟩= 0. This variational condition naturally leads to the self-consistent-ﬁeld Hamiltonian commonly derived
through a Lagrangian technique for the Hartree-Fock equations. In order to design a VQE style approach to solving the
Hartree-Fock equations we take a diﬀerent approach that leverages the fact that we can determine any basis rotation
through a linear-depth quantum circuit. Thouless demonstrated [11] that any non-orthogonal product wavefunction
can be obtained from a product wavefunction by a unitary generated by one-body fermionic operators of the form a†
paq.
The underlying reason for why this fact is true is that the one-body fermionic generators form a closed Lie-algebra.
Given,

a†
paq, a†
ras

= δq,ra†
pas −δp,sa†
ras
(A6)

the adjoint representation of any element of the algebra κ where

κ =
X

p,q
κp,qa†
paq,
(A7)

and its commutator with any other element can be eﬃciently represented as matrix that is m × m where m is the
number of fermionic modes.

κ, a†
p

= a†
qκp,q , [κ, ap] = aqκ∗
p,q
(A8)

## Page 11

Using the BCH expansion, we can express the similarity transformed ladder operators as

eKa†
pe−K =
X

q
a†
quq,p , eKape−K =
X

q
aqu∗
q,p
(A9)

where u is the matrix given by the exponentiation of the coeﬃcient matrix for the generator operator κ

u = eκ
(A10)

which is the proof for Eq. (1). Any rotation of the underlying basis can now be represented as a similarity transfor-
mation of each fermionic mode

|φ(κ)⟩= eKa†
1e−K...eKa†
ne−K|0⟩= eK|ψ⟩.
(A11)

Thus any non-orthogonal state can be generated by implementing eK as a circuit acting on an initial product state.
Given the Hartree-Fock wavefunction ansatz the energy is given by

E(κ) = ⟨φ(κ)|H|φ(κ)⟩= ⟨ψ|eKHe−K|ψ⟩.
(A12)

With the energy expressed in the form of Eq. (A12) it is not immediately clear that it can be evaluated without
knowledge of the 2-RDM. To see this fact, we used the BCH expansion and notice that all nested commutator terms
involve a†
paq-like terms and the original Hamiltonian. The commutator of a two-mode number conserving fermionic
operator with a four-mode number conserving fermionic operator produces a linear combination of four four-mode
number conserving fermionic operators. Therefore, all terms in the expansion can be evaluated with knowledge of only
the 2-RDM. If we start with a product state deﬁned from an orthogonal set of states the 2-RDM can be constructed
directly from the 1-RDM [29]

1Dj
i =⟨φ|a†
jai|φ⟩

2Dpq
ij =⟨φ|a†
pa†
qajai|φ⟩= 1Dp
i
1Dq
j −1Dq
i
1Dp
j .
(A13)

This expression also demonstrates that we only need to measure the 1-RDM to evaluate the energy. It is important to
note that the reconstruction of the 2-RDM from the 1-RDM described in Eq. (4) is only exact for Slater determinant
wavefunctions. The energy is evaluated as a function of the 1- and 2-RDM by

ij
hij⟨φ(κ)|a†
iaj|φ(κ)⟩+
X

ijkl
Vijkl⟨φ(κ)|a†
ia†
jakal|φ(κ)⟩=
X

E(κ) =
X

where hij and Vijkl

hi,j =
Z
drχ∗
i (r)

−∇2(r) +
X

A

V i,j
l,k =1

ijkl
Vijkl
2Dij
lk
(A14)

ij
hij
1Di
j +
X

!

ZA
|r −RA|

χj(r)
(A15)

Z Z
dr1dr2χ∗
i (r1)χ∗
j(r2)
|r1 −r2|−1
χk(r2)χl(r1)
(A16)

2

are the molecular integrals in the original basis. These orbitals are determined by diagonalizing the matrix of one-body
integrals hij = [h]ij described in the STO-3G atomic basis. In summary, to measure the energy of our system given
basis rotation circuit ansatz we need the following steps:

1 Measure the entire 1-RDM.

2 Compute the 2-RDM by evaluating. Eq. (A13)

3 Compute the energy by evaluating. Eq. (A14)

1.
Classical simulation of non-interacting fermion circuits

Given a particular set of parameters {κp,q} the 1-RDM resulting from a wavefunction ψ = U(κ)φ, where φ is an
initial product state, is

1 ˜Dp
q =⟨φ|e−Ka†
peKe−KapeK|φ⟩= ⟨φ|
X

j
up,ia†
i
X

ij
up,iu∗
q,j⟨φ|a†
iaj|φ⟩.
(A17)

q,j
u∗
q,jaj|φ⟩=
X

With this 1-RDM one can evaluate the energy and gradients with respect to κp,q. This expression requires two matrix
multiplications to evaluate along with the 1-RDM of the starting state.

## Page 12

Appendix B: Implementing the Basis Change Circuit and Circuit Concatenation

In order to implement the basis rotation circuits we leverage a number of recent works that provide asymptotically
optimal circuit compilations. We review a circuit construction that is analogous to a QR decomposition as motivation
before highlighting the salient features of the optimal circuit compilation. The basis rotation circuit is ﬁrst expressed
in fermionic modes which we then provide a compilation to the gate set used in this work. Our goal is to implement
a unitary corresponding to

U(eκ) = eK
K =
X

i,j
κi,ja†
iaj
κ† = −κ.
(B1)

Not all terms in K commute and thus naively one would expect an approximate method such as Trotterization to
be required. In Reference [28] the connection of the QR decomposition of eκ via Givens rotation to the sequence of
untiaries Rpq(u)

R(u)pq = elog[u]pq(a†
paq−a†
qap)
(B2)

was established allowing for the exact evolution of the one-body component of the Hamiltonian without Trotter error
and a circuit to implement any basis rotation–i.e. any Slater determinant. A distinctive feature of one-body rotations
is that the map U(eκ) is a homomorphism under matrix multiplication

U(eκ) · U(eκ′) = U(eκ · eκ′)
(B3)

We use this homomorphism through the observation that

Rpq(θ)U(u) = U(rpq(θ)u)
(B4)

where





1 ...
0
...
0
... 0
... ...
...
...
...
0 ... cos(θ) ... −sin(θ) ... 0
...
...
...
...
0 ...
sin(θ) ...
cos(θ)
... 0
...
...
...
... ...
0 ...
0
...
0
... 1

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

r(θ)p,q =

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

(B5)

which given an appropriate selection of a sequence of rp,q(θ) brings u into diagonal form
Y

k
Rk(θk)U(u) =
X

p
e−iφpa†
pap =
X

p
e−iφp|p⟩⟨p|
(B6)

The sequence of Rk(θk) can be determined by a QR decomposition of the matrix u. This fact was ﬁrst recognized by
Reck [26] and used in a variety of quantum optics experiments to implement universal unitary operations–limited to
unitaries associated with one-body fermionic Hamiltonians. Jiang et. al and Kivlichan et. al [28, 41] point out that
in a ﬁxed particle manifold the circuit depth can be further minimized. This fact is clearly shown by considering the
state in the basis that is being prepared through the Givens rotation network and back transforming to the original
basis

η
Y

η
Y

i=1
˜a†
i|vac⟩=

η
Y

i=1
e−K˜a†
ieK|vac⟩=

|ψ(κ)⟩=

X

p
[eκ]i,p a†
p|vac⟩
(B7)

i=1

we only need the ﬁrst η-columns of the matrix [eκ]. Therefore, we can focus on Givens network elimination on these
columns. Jiang et al. provide a further circuit minimization by noting that any rotation amongst the occupied orbitals
merely shifts the observable by a global phase. Given a unitary V

η
Y

η
X

η
Y

j=1
Vi,j˜a†
i|vac⟩= det [V ]

i=1

i=1
˜a†
i|vac⟩
(B8)

## Page 13

where the det [V ] is a phase and thus not observable. The V can be chosen such that the lower left triangle or
eκ are zeroed out by Givens rotations. In chemistry parlance, this transformation is called an occupied-occupied
orbital rotations and is known to be a redundant rotation. For restricted Hartree-Fock the number of non-redundant
parameters in κ is equal to the number of occupied spatial orbitals times the number of virtual orbitals. We also note
that this decomposition is exact and likely asymptotically optimal. While the authors of [28] argue that in terms of
gate count their Givens rotation circuits are likely optimal, we note that approximate unitary constructions such as
those in [42] may provide a route to approximating the compilation of similar circuits with even fewer gates.

FIG. 4. Givens rotation circuit for H8 simulating a random basis transformation in the half ﬁlling sector. Each Givens rotation
is compiled into
√

iswap (hexagon two-qubit gates) and Rz gates (square gates with an angle depicted).

An example of an eight qubit half-ﬁlling circuit is given in Fig. S4. When we are away from half ﬁlling the nice
symmetry of the circuit is lost. For example, Fig. S5 is Diazene which has 8-electrons in 12 orbitals.

FIG. 5. Givens rotation circuit for diazene prior to freezing the two lowest energy orbitals. Away from half ﬁlling the basis
rotations have a parallelogram structure.

Appendix C: Optimal Measurement of the 1-RDM

In this section we present a methodology that allows us to measure the 1-RDM in N + 1 measurement settings and
no additional quantum resources. We will also discuss a method that allows us to perform post selection on all the
Monte Carlo averaged terms at the cost of an additional row of
√

iswap gates at the end of the circuit. The 1-RDM
is an N × N hermitian positive semideﬁnite matrix with elements equal to the expectation values ⟨a†
iaj⟩where {i, j}
index the row and column of the matrix. The matrix of expectation values is depicted in Fig. S6. As a motivator for
our measurement protocol we start by describing circuits required to measure the diagonal elements of the 1-RDM of
a six qubit system at half ﬁlling–i.e. ⟨a†
iai⟩.

1.
Diagonal terms

Given a circuit U implementing the basis rotation eκ the diagonal elements of the 1-RDM are obtained by measuring
the Z expectation value on each qubit. The correspondence between a†
iai, measurement result Mi from qubit i, qubit
operators is derived using the Jordan-Wigner transform

⟨a†
iai⟩= I −⟨Zi⟩

2
= ⟨Mi⟩
(C1)

where Zi is the Z-qubit operator on qubit labeled i. The expectation value ⟨a†
iai⟩is equivalent to the probability of
measuring a 1 bit on qubit i–i.e ⟨Mi⟩. Because we are measuring in the computational basis we can post-select on
the three excitations in the measurement result. This process is depicted in Fig. S6.

## Page 14

FIG. 6. Measurement circuit associated with estimating all diagonal elements of the 1-RDM simultaneously. The elements that
are acquired with this circuit are highlighted in red.

The hermiticity of the 1-RDM demands that ⟨a†
iai+1⟩= ⟨a†
i+1ai⟩∗. The 1-RDM has no imaginary component
because we use an initial basis built from real valued orbitals and the basis rotation circuit implements an element
of SO(N)–i.e. the basis rotation circuit involves a unitary matrix with real values. Therefore, we only measure the
real part of all one-oﬀ-diagonal terms a†
iai+1 + a†
i+1ai which corresponds to 2ℜ⟨a†
iai+1⟩. Using the Jordan-Wigner
transform to map fermionic ladder operators to qubits

⟨a†
iai+1 + a†
i+1ai⟩= 1

2 (⟨XiXi+1⟩+ ⟨YiYi+1⟩) = 2ℜ⟨a†
iai+1⟩
(C2)

FIG. 7. The two circuits allowing for the measurement of all one-oﬀ-diagonal elements of the 1-RDM simultaneously. The teal
circuit involves performing an Ry rotation (to measure in the X basis) at the end of the circuit and the purple circuit contains
an Rx rotation (to measure in the Y basis). The 1-RDM elements that are acquired with these circuits are highlighted in
red. We label which pairs contribute to which expectation values with grey dashed lines. The thinner dashes are for the even
1-RDM pairs and the thicker dashes are for the odd 1-RDM pairs. Because Ry and Rx operations do not preserve particle
number we cannot post-select on total particle number with these measurement circuits.

3.
General oﬀ-diagonal terms and virtual swapping

The label of each fermionic mode is an arbitrary choice, so we are free to reorder the labels such that measuring
nearest-neighbor pairs of qubits corresponds to measuring diﬀerent oﬀ-diagonal 1-RDM elements. Every relabeling
of the qubits requires us to recompile the Givens rotation circuit. The structure of the circuit stays the same but
the rotation angles are diﬀerent. In this section we describe how to recompute the Givens rotation angles based on a
new label ordering. Using the label sets {1, 3, 0, 5, 2, 4} and {3, 5, 1, 4, 0, 2} we are able to use the two measurement
circuits in Fig. S7 to measure the remaining oﬀ-diagonal 1-RDM elements.
Formally, we build the new qubit labels by virtually swapping fermionic modes at the end of the original circuit
implement eκ. We note that performing nearest-neighbor fermionic swaps between adjacent pairs twice (even swaps
and odd swaps) we obtain a new ordering of qubits.
For example, consider six fermionic modes {0, 1, 2, 3, 4, 5}.
Performing a set of fermionic swaps on modes labeled {(0, 1), (2, 3), (4, 5)} followed by swaps on {(1, 2), (3, 4)} leaves
our mode ordering as {1, 3, 0, 5, 2, 4}. We can then perform X-Pauli and Y -Pauli measurements on each qubit to
recover expectation values associated with

{ℜ(a†
1a3 + a†
3a1), ℜ(a†
3a0 + a†
0a3), ℜ(a†
0a5 + a†
5a0), ℜ(a†
5a2 + a†
2a5), ℜ(a†
2a4 + a†
4a2)}.
(C3)

## Page 15

FIG. 8. Two-mode fermionic fast Fourier transform that diagonalizes the XX + Y Y Hamiltonian.

This procedure can be repeated once more to measure all the required two-body fermionic correlators to construct
the 1-RDM. Though it appears that each new label set incurs additional circuit by requiring fermionic swaps between
neighboring modes we can exploit the fact that one-body fermionic swaps generated by exp(−iπfswap/2) where
fswap is

fswap = a†
paq + a†
qap −a†
pap −a†
qaq.
(C4)

This one-body permutation can be viewed as a basis rotation which can be concatenated with the original circuit at
no extra cost due to Eq. (B3). The swapping unitary simply shuﬄes the columns of eκ that is used to generate the
Givens rotation network. The same eﬀect could have been achieved by relabeling the fermionic modes which would
have been equivalent to permuting the rows and columns of eκ. This relabeling technique can be applied beyond basis
rotation circuits. For example, one can relabel the fermionic modes of a generalized swap network such that diﬀerent
sets of RDM elements can be measured as nearest-neighbor pairs. The same logic can be applied to k-RDM elements.

In conclusion we need N/2 circuits, where each of the N/2 circuits gets measured in two or three diﬀerent ways, for
an N-qubit system to measure the 1-RDM. This is a quadratic improvement over the naive measurement scheme which
would require O(N 2) diﬀerent measurement settings. To make this savings concrete we consider the number of Pauli
terms one would need to measure for a 12-qubit system. If no grouping is applied then there are 276 measurement
circuits. With greedy grouping considering locally commuting Pauli terms then there are 149 diﬀerent measurement
circuits. With the measurement strategy outlined above we require 13 diﬀerent circuits.

4.
Oﬀ-diagonal terms with post-selection

The circuits depicted in Fig. S7 did not allow for post-selection because the rotations to measure in the X-basis
and Y -basis do not commute with the total number operator.
In this section we design a basis rotation circuit
that commutes with the total number operator and diagonalizes the 1

2 (XX + Y Y ) Hamiltonian. The diagonal form
means that after performing the basis rotation we can measure in the computational basis to obtain expectation
values 1

2⟨XX + Y Y ⟩.
The circuit that diagonalizes 1

2 (XX + Y Y ) is described in Fig. S8 and is denoted UM below. Its commutation
with the total number operator can be easy seen by recognizing that the T-gate (Rz(π/4)) commutes with the total
number operator and so does the
√

iswap. Applying UM to the 1

2 (XX + Y Y ) Hamiltonian

0 0 0 0
0 0 1 0
0 1 0 0
0 0 0 0

0 0
0
0
0 1
0
0
0 0 −1 0
0 0
0
0










U †
M =

UM



(C5)







transforms the operator into a diagonal representation. Given an ordered pair of qubits {a, a + 1} the last matrix
in (C5) is 1

2 (Za −Za+1) in qubit representation. Finally, we can relate the Z expectation values, the transformed
XX + Y Y expectation values, fermionic ladder operators, and binary measurements {Ma, Ma+1} via

⟨Um

a†
aaa+1 + a†
a+1aa

U †
m⟩= ⟨Um
1
2 (XaXa+1 + YaYa+1) U †
m⟩= 1

2⟨Za −Za+1⟩= 1

2 (Ma+1 −Ma) .
(C6)

The measurement circuit can only be applied to non-overlapping pairs and thus we can obtain estimates of XaXa+1 +
YaYa+1 for a values corresponding to even integers or a corresponding to odd integers. More concretely, we describe
this process in Fig. S9 for a six qubit problem. All experiments involved circuits that allowed for post-selection based
on total Hamming weight. The “raw” data indicates analysis of the resulting bitstrings without post-selection.

## Page 16

FIG. 9.
Two circuit measuring the one-oﬀ-diagonal of the 1-RDM such that the total particle number can be measured
simultaneously. This circuit allows us to post select on the correct number of excitations in the measured bitstring. The top
circuit measures the even pairs and the bottom circuit measures the odd pairs. Local Z expectation values are measured on
all the qubits and used to construct the expecation value for ⟨a†
iai+1⟩.

5.
Computing error bars for elements of the 1-RDM

We use two methods to estimate error bars for all quantities in our experiments. The procedures diﬀer in how the
covariance between 1-RDM terms is estimated. In the ﬁrst procedure, error bars are generated by estimating the
covariance between terms in the 1-RDM at the same time as the mean estimation. Mean values of oﬀ-diagonal 1-RDM
terms involve estimating the expectation values for (Za −Zb)/2. Therefore, the covariance between two oﬀ-diagonal
elements of the 1-RDM is

Cov
1

2 (Zp −Zq)

= 1

2 (Za −Zb) , 1

4 (Cov [Za, Zp] −Cov [Za, Zq] −Cov [Zb, Zp] + Cov [Zb, Zq])
(C7)

for all pair sets {(a, b), (p, q)} measured simultaneously.
All quantities can be estimated from the simultaneous
measurement of all qubits. Therefore, for each circuit permutation we obtain two covariance matrix of size N/2×N/2
and N/2 −1 × N/2 −1. For the circuit with no label permutation we also obtain the covariances for all a†
iai terms.
In the second procedure for estimating covariance matrices we assume we are sampling from a pure Gaussian state.
This assumption is applicable when the ﬁdelity is high enough as any change to the covariance matrix would be a second
order eﬀect. For these states the 2-RDM is exactly described by the 1-RDM and therefore all covariances between
the 1-RDM elements are perfectly deﬁned by a non-linear function of the 1-RDM elements. For any wavefunction
ψ corresponding to the output of a basis rotation circuit the covariance of 1-RDM elements computed from such a
wavefunction are as follows:

Cov
h
a†
iaj + a†
jai, a†
paq + a†
qap
i

ψ = Di
qδj
p −Di
qDp
j + Di
pδj
q −Di
pDq
j + Dj
qδi
p −Dj
qDp
i + Dj
pδi
q −Dj
pDq
i .
(C8)

With the estimates of the covariances we are able to re-sample the 1-RDM assuming central-limit theorem statistics.
We use a multinomial distribution where the mean values are ⟨a†
σ(i)aσ(i+1)⟩and the covariance matrix of the multino-
mial distribution is obtained by dividing the estimates of the covariance matrix above by α× 250,000. α is a number
less than 1 reﬂecting the probability that a bitstring is rejected. α is estimated from prior N-qubit experiments. Once
the new 1-RDM is obtained it can be puriﬁed, used to estimate a ﬁdelity witness, and compute the energy. For all
error bars we re-sample the 1-RDM 1000 times and compute a mean value and standard deviation from this set. All
quantities estimated are sensitive to the N-representability of the resampled 1-RDM. We use the ﬁxed trace positive
projection described in [32] to ensure that each resampled 1-RDM is positive semideﬁnite and has the correct trace.
The correction procedure is only applied when the resampled 1-RDM has eigenvalues below zero.

## Page 17

Appendix D: Computing the ﬁdelity and a ﬁdelity witness from the 1-RDM

1.
Fidelity Witness

The class of quantum circuits simulating non-interacting fermion dynamics have the special property that an eﬃcient
ﬁdelity witness can be derived. The formal derivation for general non-interacting fermion wavefunctions is described
in Ref. [36]. Here we adapt this result to the special case of particle conserving dynamics generated by one-body
fermionic generators. A ﬁdelity witness is an observable that provides a strict lower bound to the ﬁdelity for all input
states. The ﬁdelity witness is eﬃcient in the sense that for an L-qubit system only L2 expectation values are required
to evaluate the ﬁdelity witness. Given that U is a unitary corresponding to a basis transformation circuit and |ω⟩is
the initial computational basis state corresponding to ω = (ω1, ..., ωL) any L-bit string which satisﬁes nj|ω⟩= ωj|ω⟩
for j = 1, ..., L allows us to deﬁne a basis state annihilator operator

L
X

L
X

n(ω) =

j=1
[(1 −ωj)nj + ωj(I −nj)] =

L
X

j=1
[nj −ωjnj + ωjI −ωjnj] =

j=1
[nj + ωjI −2ωjnj]
(D1)

which satisﬁes n(ω)|ω⟩= 0. The computational basis state |ω⟩is the zero energy eigenstate of nω and any other
computational basis state an excitation from this state. The excitation energy is exactly the number of bits that are
diﬀerent from ω for each Fock basis state which can be computed by summing the resulting bit string from the XOR
operation between the two Fock basis states being considered. The ﬁdelty witness

W = U (I −nω) U †
(D2)

can be evaluated with knowledge of the measured 1-RDM. To relate the ﬁdelity witness to the 1-RDM it is important
to note the following

Tr
h
UρpU †a†
iaj
i
=

uDu†

i,j
(D3)

where D is the matrix of expectation values ⟨ρp, a†
iaj⟩and u = eκ because any one-body rotation on the state ρp can
be equated to a similarity transform of the generating matrix for that one-body transformation. This logic is similar
to logic used in [43] which moved one-body basis rotations at the end of the circuit into the Hamiltonian as an error
mitigation technique. Using this relationship we can evaluate the ﬁdelity witness with the following expression

L
X


u†Du


FW(ρp) = 1 −

j=1


(D4)

j,j + ωj −2ωj

u†Du


j,j

where D is the 1-RDM that is measured, u = eκ is the unitary rotation representing the new Slater determinant.

2.
Fidelity

Given an idempotent 1-RDM and the basis rotation unitary u = eκ, the ﬁdelity can be determined by the following
procedure:

1. Perform an eigen decomposition on the puriﬁed 1-RDM and use the eigenvectors associated with eigenvalues
equal to 1 as the columns of a unitary matrix v corresponding to the measured basis rotation.

2. Use the expression for the overlap between two basis rotation unitaries |⟨ψu|ψv⟩|2 = |det
v†u

|2 to compute
the ﬁdelity. The function det is the determinant of a matrix. This is the inner product between two Grassmann
representatives and is independent of choice of orbitals.

Appendix E: Error mitigation through puriﬁcation

A distinctive feature of the Slater determinant wavefunction ansatz is that their 1-RDMs are idempotent matrices.
The manifold of states with idempotent 1-particle density matrices is signiﬁcantly smaller than the space of possi-
ble wavefunctions. Thus our error mitigation strategy will rely on projecting the measured 1-RDM to the closest
idempotent 1-RDM. This projection procedure can be represented by the following mathematical program

min
T r[D]=η,D⪰0,D2=D ||D −˜D||
(E1)

## Page 18

that seeks to determine a 1-RDM D that is close to the measured 1-RDM ˜D with has ﬁxed trace, is positive semidef-
inite, and is a projector.
A practical implementation of the the program in Eq. (E1) is challenging due to the
idempotency constraint.
Instead of solving Eq. (E1) directly we rely on an iterative procedure that under mild
conditions projects a measured 1-RDM ˜D towards the set of idempotent matrices. This procedure is the McWeeny
puriﬁcation commonly used in linear scaling electronic structure techniques [29] and is deﬁned by the iteration

Dn+1 = 3D2
n −2D3
n.
(E2)

After each iteration the eigenvalues are closer to {0, 1}. Prior work [44] proposed to use McWeeny puriﬁcation on the
2-RDM, but it is not clear what that accomplishes. This is because, in general, 2-RDMs are not idempotent matrices
and applying pure-state puriﬁcation requires more general pure-state N-representability conditions [33]. Due to the
fact that McWeeny iteration has no eﬀect on the eigenvectors, it merely pushes the eigenvalues of D towards {0, 1},
we could have achieved this projection by diagonalizing D and rounding the eigenvalues to 0 or 1. We performed the
puriﬁcation iteration because we are able to analyze the convergence when D is obtained by sampling.

Here we will estimate the number of samples needed to ensure that the 1-RDMs can be faithfully reconstructed
within arbitrarily small error using our protocol. This analysis assumes we sample from a perfect state and thus our
goal is to provide evidence that McWeeny puriﬁcation is convergent under sampling noise. Consider the puriﬁcation
process in Eq. (E2). Now let us assume that the principal eigenvalue of D is Pk. In absentia of numerical error we
would have that Pk = 1 for Hartree-Fock theory. However, sampling error incurs an error in this eigenvalue such that

Pk = 1 + ∆,
(E3)

where ∆is a random variable with mean 0 and variance σ2. Further, let µk = E(∆k), where µ2 = σ2 for example.
Now given these quantities we wish to evaluate

E(Pk+1) = E(3P 2
k −2P 3
k ) = 1 −3σ2 −2µ3.
(E4)

Similarly we have that

E(P 2
k+1) = 1 −6σ2 −4µ3 + 9µ4 + 12µ5 + 4µ6.
(E5)

This implies that the variance is

V(Pk+1) = E(P 2
k+1) −E(Pk+1)2 = 9(µ4 −σ4) + 12(µ5 −σ2µ3) + 4(µ6 −µ2
3).
(E6)

Further, let us assume that µj ≤αjσj, for all j .

V(Pk+1) ≤9σ4(α4 −1) + 12|σ|5(α5 + α3) + 4|σ|6α6.
(E7)

Assuming that σ ≤1 we have that

V(Pk+1) ≤9σ4(α4 −1) + 4|σ|5(α6 + 3α5 + 3α3).
(E8)

It is clear from this recurrence relation that the variance for this method converges quadratically (assuming σ is
suﬃciently small). Speciﬁcally, we have that V(PK) ≤ϵ for K ∈O (log log(1/ϵ)) if appropriate convergence criteria
are met. A criterion for convergence is that 9σ4(α4 −1) + 4|σ|5(α6 + 3α5 + 3α3) ≤σ2. This is guaranteed if,

1 −
β

−β +
p



σ2 ≤
1
9(α4 −1)

β2 + 36α4 −36




,
(E9)

18(α4 −1)

where β = 4(α6 + 3α5 + 3α3).
The precise values of αj depend on the nature of the underlying distribution. However, if we assume that it is
Gaussian then we have that α2j+1 = 0 ∀j, α4 = 3, α6 = 15. Furthermore, we have under these Gaussian assumptions
(for any σ > 0) that

V(Pk+1) ≤18σ4 + 12σ6.
(E10)

In this case, we ﬁnd that the McWeeny iteration will converge if V(Pk+1) ≤σ2 which is implied by

√

σ2 ≤−3

20 +

564
120
≈0.048.
(E11)

This relatively broad distribution implies that even if the uncertainty in the principal eigenvalue of the reconstructed
RDM is large then the algorithm will with high probability converge to a pure state after a small number of iterations
(if the underlying distribution is Gaussian). If the distribution is non-Gaussian then Eq. (E9) can be used to show
convergence given that the moments of the distribution are appropriately small.

## Page 19

1.
Errors in Eigenvalues

The errors in the eigenvalues of the RDM are easy to compute from known results. We have from Corollary 6.3.4
from [45] that if ρ is the true density operator and ˜ρ = ρ + sE for some matrix E of errors and some scalar s ∈[0, 1]
then the error in a particular eigenvalue is at most

|λ(ρ) −λ(ρ + sE)| ≤s∥E∥,
(E12)

where ∥E∥is the spectral norm of the error matrix. We are of course most interested in the case where s = 1, however
below we will need the above formula for general values of s and so we give it for generality.
Now let E be a matrix consisting of M elements, each of which is independently distributed with zero mean and
variances at most σ2
M. We then have that



X

E
(λ(ρ) −λ(ρ + E))2
≤E

Thus



i,j
[E2]i,j

≤Mσ2
M.
(E13)

V(λ(ρ + E)) ≤Mσ2
M.
(E14)

Hence σ2 ≤Mσ2
M, which allows the upper bounds in Eq. (E10) to be easily computed (under assumptions of
Gaussianity). In particular, we then have convergence under the Gaussianity assumption if

√

−3

σ2
M ≤1

20 +

M

!

564
120

.
(E15)

Recall that the 1-RDM constists of N(N + 1)/2 independent matrix elements, which implies that M = N(N + 1)/2
in our case.

2.
Errors in Eigenvectors

Although the above criteria give conditions for the convergence of McWeeny puriﬁcation starting from a sampled
1-RDM, there remains the question of whether the pure state that it converges to is ϵ-close to the true value. This is
relevant because if the errors are large enough that an eigenvalue crossing occurs, then the puriﬁcation process can
fail to yield the desired state. Our aim here is to bound the distance between the eigenvectors.
First, rather than arguing about the diﬀerence in eigenvectors for ρ and ρ+E we will instead consider R time slices
and will be interested in the eigenvectors of ρ(j) := ρ + (j/R)E. Let the principal eigenvector of ρ be |λ⟩and more
generally at step j let us denote the eigenvector to be |λ(j)⟩and the correspeonding eigenvalue to be λ(j). We then
have from ﬁrst order perturbation theory, assuming that there is an eigenvalue gap that for any state |ν([j −1])⟩that
is orthogonal to |λ([j −1])⟩,

R
⟨ν(j −1)| E |λ(j −1)⟩

⟨ν(j −1)|λ(j)⟩= 1

ν(j −1) −λ(j −1)
+ O(1/R2)
(E16)

Thus if we deﬁne γ(j) to be the minimum eigenvalue gap between |λ(j)⟩and the remainder of the spectrum of ρ(j)
we have that
X

1
R2
| ⟨ν(j −1)| E |λ(j −1)⟩|2

ν̸=λ
|⟨ν(j −1)|λ(j)⟩|2 ≤
X

(λ(j −1) −ν(j −1))2
+ O(1/R3)

ν̸=λ

1
γ2(j −1)R2 | ⟨ν(j −1)| E |λ(j −1)⟩|2 + O(1/R3)

≤
X

ν̸=λ

1
γ2(j −1)R2 ⟨λ(j −1)| E |ν(j −1)⟩⟨ν(j −1)| E |λ(j −1)⟩|2 + O(1/R3)

=
X

ν̸=λ

=
1
γ2(j −1)R2
⟨λ(j −1)| E2 |λ(j −1)⟩−(⟨λ(j −1)| E |λ(j −1)⟩)2
+ O(1/R3)

≤
∥E2∥
γ2(j −1)R2 + O(1/R3)
(E17)

## Page 20

It then follows from Eq. (E17) that

|⟨λ(j −1)|λ(j)⟩−1|2 ≤
∥E2∥
γ2(j −1)R2 + O(1/R3)
(E18)

This gives us that, for the Euclidean distance between two vectors,

p

||λ(j)⟩−|λ(j −1)⟩| ≤

Next we have from the triangle inequality that for any integer R,

R
X

||λ(R)⟩−|λ(0)⟩| ≤

2∥E2∥
γ(j −1)R + O(1/R2).
(E19)

R
X

p

2∥E2∥
γ(j −1)R + O(1/R)
(E20)

j=1
||λ(j)⟩−|λ(j −1)⟩| ≤

In particular, this holds as we take R →∞, which yields

R
X

p

2∥E2∥
γ(j −1)R + O(1/R) ≤

lim
R→∞

j=1

j=1

√

p

2∥E2∥
γmin
=

2∥E∥
γmin
.
(E21)

Unfortunately, we do not know what γmin is apriori, however we can bound it modulo some weak assumptions. Let
∥E∥≤1/4, it is then straight forward to verify from Eq. (E12) that

γmin ≥1 −2∥E∥.
(E22)

Under the exact same assumptions we then have from a series expansion of the denominator that

||λ(ρ)⟩−|λ(ρ + E)⟩| ≤
√

2∥E∥(1 + 4∥E∥) ≤2
√

2∥E∥
(E23)

As E is a sum of M elements each with zero mean and variance at most σM we then have under the above assumptions
(and the additive property of variance) that

V ||λ(ρ)⟩−|λ(ρ + E)⟩| ≤8Mσ2
M.
(E24)

Therefore if we demand that the variance is atmost ϵ2 it suﬃces to pick

σ2
M = ϵ2

8M ,
(E25)

which sets a suﬃcient condition on the number of samples of Nsamp ≥
ϵ
2
√

2M . The remaining caveat is that in the
above analysis we needed to assume that ∥E∥≤1/4. If each of the entries of the matrix E are Gaussian random
variables, for example, it then follows that regardless of the value of σ there will always be a tail probability that this
eigenvalue condition is not met. We can bound the tail probability using Chebyshev’s inequality. Using the exact
same reasoning as in Eq. (E14) we have that

Thus the probability that ∥E∥≥1/4 is

V(∥E∥) ≤Mσ2
M.
(E26)

P ≤16Mσ2
M ∼2ϵ2.
(E27)

Thus even under the pessimistic assumptions of Chebyshev’s inequality, we have that the probability of failure is
asymptotically negligible if σM is chosen in accordance with Eq. (E25). Note that the number of samples needed
taken in this case is in Θ(ϵ/N) as there are M ∈Θ(N 2) independent matrix elements in the 1-RDM.

Appendix F: Eﬀect of CPHASE and Givens Rotation Error

In this section we consider two known gate errors that occur in the Givens rotation circuits and attempt to
analytically and numerically benchmark the eﬀect of these errors. When implementing the
√

iswap operation there is

## Page 21

a known |11⟩⟨11| phase error of approximately π/24. We model this phase error as a cphase(π/24) gate that occurs
directly after the
√

iswap gate (Eq. (F1)). We ﬁnd that the always on cphase(π/24) has negligible eﬀect on the
outcome of the experiment and the stochastic Rz(θ) errors coherently corrupt the output of the circuit.

1
0
0
0
0
1
√





2
i
√

√

2
0
0
i
√





iswap ≈

2
1
√

2
0
0
0
0
eiπ/24



= CPHASE(π/24)
√

iswap
(F1)

To benchmark the eﬀect of the parasitic cphase we simulate the diazene experiment with this interaction turned on
and evaluate the results with error mitigation. We can counteract the cphase(π/24) by performing local Rz gates.

FIG. 10. Analysis of the diazene isomerization curve where the Givens rotations are corrupted by a parasitic cphase(π/24). All
points are after puriﬁcation. Without puriﬁcation all curves are signiﬁcantly higher in energy. The light dots are the circuits
executed without optimization, the darker dots are with an angle adjustment to counteract the known parasitic cphase, and
the plus markers are VQE optimization of the cphase circuits.

Consider the imperfect gate

U1 = diag(1, 1, 1, e−iφ)
√

iswap
(F2)

we can use a diﬀerent imperfect gate which diﬀers only by single qubit phases,

U2 = diag(1, eiφ/2, eiφ/2, 1)
√

iswap.
(F3)

The error associated with U1 can be approximated by considering the Pauli expansion of the cphase part of U1,

diag(1, 1, 1, e−iφ) ≈e−iφ ×

II + iφ

and thus the error is approximately

Err1 ≈3
φ

4

Similarly for U2

4 ZZ

,
(F4)

4 IZ + iφ

4 ZI −iφ

2
= 3

16φ2.
(F5)

diag(1, eiφ/2, eiφ/2, 1) ≈eiφ/4

II −iφ

with an associated Pauli error of

Err2 ≈1

4 ZZ

(F6)

16φ2.
(F7)

## Page 22

Very crudely, since for
√

iswap φ = π/24, we expect Err1 to be approximately 0.32% and Err2 to be approximately
0.11%. This improvement is shown to be most beneﬁcial for simulating the in plane rotations of diazene in Fig. S10.
The light dots are with the original cphase gate whereas the solid dots are with this local Rz correction. We also
include a VQE optimization to numerically determine the noise ﬂoor for this experiment. This suggests that VQE +
error mitigation can mitigate not only control error but more fundamental gate physics issues. For in-plane rotation
circuits the dynamics during the circuit execution are apparently more sensitive to these types of coherent errors near
transition states, although the exact reason for increased sensitivity is unclear.
To determine the error budget on the Rz rotation angles we can determine the degree of corruption from Gaussian
noise on the control angle. Consider the Rz rotation

Rz(θ, δα) = e−iZθ(1+δα)/2
(F8)

where θ is the desired rotation angle and δα is a stochastic variable. We can build a simpliﬁed model of control angle
error as Givens rotation error

G(θ, δα) = eθ(1+δα)(a†
i aj−a†
jai)
(F9)

which can be expressed as

G(θ) =
√

iswap
†
i,je−iθ(1+δα)Zi/2eiθ(1+δα)Zj/2√

iswapi,j.
(F10)

For numerical simplicity we consider the eﬀect on elements of the 1-RDM





a†
i cos(θ(1 + δα)) + a†
j sin(θ(1 + δα))
if r = i
a†
j cos(θ(1 + δα)) −a†
i sin(θ(1 + δα))
if r = j
a†
r
if r ̸= i & r ̸= j
(F11)

G(−θ, δα, i, j)a†
rG(θ, δα, i, j) =








ai cos(θ(1 + δα)) + aj sin(θ(1 + δα))
if s = i
aj cos(θ(1 + δα)) −ai sin(θ(1 + δα))
if s = j
as
if s ̸= i & s ̸= j
(F12)

G(−θ, δα, i, j)asG(θ, δα, i, j) =




We can determine the expected 1-RDM with respect to a Gaussian distribution of noise by integrating with respect
to the perturbation

ρ(δα) =
1
σ
√





Z ∞

−∞
ρ(δα, σ)G(−θ, δα, i, j)a†
rG(θ, δα, i, j)dδα =








Z ∞

−∞
ρ(δα, σ)G(−θ, δα, i, j)asG(θ, δα, i, j)dδα =




2π e−(δα)2

2σ2
(F13)

a†
i cos(θ)e−θ2σ2

2
+ a†
j sin(θ)e−θ2σ2

2
if r = i

a†
j cos(θ)e−θ2σ2

2
−a†
i sin(θ)e−θ2σ2

(F14)

2
if r = j
a†
r
if r ̸= i & r ̸= j

ai cos(θ)e−θ2σ2

2
+ aj sin(θ)e−θ2σ2

2
if s = i

aj cos(θ)e−θ2σ2

2
−ai sin(θ)e−θ2σ2

(F15)

2
if s = j
as
if s ̸= i & s ̸= j

Therefore, propagating the 1-RDM with stochastic Rz errors corresponds to evaluating the map in Eq. (F15). This
calculation assumes that the stochasticity has a time-scale that is much faster than a single energy evaluation. We
ﬁnd that with σ > 0.22 puriﬁcation projects to the wrong 1-RDM.

Appendix G: Gradient for the Basis Rotation Ansatz

Another beneﬁt of restricting our ansatz to Slater determinants is the fact that the gradient with respect to the
parameters is accessible via the elements of the 1-RDM. The gradient of the energy with respect to the parameters

## Page 23

FIG. 11. Stochastic Rz simulation of diazene with σ = 0.22 radian ﬂuctuation on the Givens rotation gates. The plotted points
are after applying puriﬁcation to the result 1-RDM

i<b cb,i

a†
bai −a†
iab

is

of a one-body generator Z = P

dE
dcb,i
= ⟨φ0|de−Z

dcb,i
HeZ|φ0⟩+ ⟨φ0|e−ZH deZ

dcb,i
|φ0⟩.
(G1)

Due to the structure of this operator we expect the gradient to involve the commutator of the Hamiltonian with
respect to the anithermitian operator that becomes the prefactor to the right gradient. We call this prefactor ∇f(Z)
to indicate that it is a diﬀerent operator from just the rotation generator associated with cb,i.

dE
dcb,i
= ⟨φ0|e−Z 
H, ∇f(Z)cb,i

eZ|φ0⟩
(G2)

All quantities in the commutator above can be evaluated with knowledge of the 1-RDM when φ0 is a computational
basis state. In this work we utilized this gradient for a classical implementation and provide it here as justiﬁcation
for the ansatz and for future studies. The formal derivation of ∇f(Z) can be found in [46] and [47].
As a sketch for the form of ∇f(Z) consider the unitary performed in the Hartree-Fock experiment

b,i cb,iE−
b,i = e
P

U(cb,i) = e
P

b,i cb,i(a†
bai−a†
i ab).
(G3)

We now want to consider the energy derivative with respect to cb,i. Using the formulas in [46] we obtain

dcb,i
=
Z 1

dU(c)

b,i cb,iE−
b,i

e
P

b,i cb,iE−
b,iE−
b,ie−x P

0
dxex P

b,i cb,iE−
b,i.
(G4)

In order to evaluate this integral we need to have an analytical form for the similarity transform of the integrand.
The integrand can be expressed in series form with the Baker-Campbell-Hausdorﬀidentity where each term involves
nested commutators. Each nested commutator can be expressed more succinctly as the adjoint action of Z on E−
b,i





X

b′,i′
cb′,i′E−
b′,i′

ad



n 
E−
b,i

.
(G5)

b′,i′ cb′,i′E−
b′,i′ in its eigenbasis
and directly evaluate the commutator as a matrix power. In our case this would involve diagonalizing a large 2n × 2n

A general strategy for evaluating sums of adjoint actions is to represent the operator P

matrix. Fortunately, due to the connection between one-particle-basis rotations and rotations by one-body operators
on the full Hilbert space we can ﬁnd a n × n unitary that can diagonalize the matrix of cb,i coeﬃceints and represent
the operator E−
b,i in this one-particle basis. Following this step of the derivation in [47] we form the C matrix of
coeﬃcients cb,i which is antihermitian and diagonalize. Therefore, C is represented in its eigenbasis as

iC = i
X

r
λr˜a†
r˜ar
(G6)

## Page 24

where λ are purely imaginary and we have used the fact that

˜ap =
X

q
u∗
p,qaq , ˜a†
p =
X

We represent E−
b,i term in the basis that diagonalizes iC

Y =
X

Ykl =

U †E−
b,iU


q
up,qa†
q.
(G7)

k,l
Ykl˜a†
k˜al
(G8)

k,l
(G9)

here E−
b,i is an antisymmetric matrix with 1 at the (b, i) position and −1 at (i, b) position which is a representation of
the operator E−
b,i. Therefore,







E−
b,i

=
X

X

b′,i′
cb′,i′E−
b′,i′

ad

=
X

=i
X

Furthermore, powers of the adjoint action are





X

b′,i′
cb′,i′E−
b′,i′

ad



rkl
iλrYkl
h
˜a†
r˜ar, ˜a†
k˜al
i
(G10)

rkl
iλrYkl

˜a†
r˜alδr
k −˜a†
k˜arδl
r

(G11)

kl
(λk −λl) Ykl˜a†
k˜al.
(G12)

n 
E−
b,i

= in X

kl
(λk −λl)n Ykl˜a†
k˜al.
(G13)

Armed with the adjoint power we can now evaluate the integrand of Eq. (G4) via fundemental theorem of calculus
and arrive at an expression for the gradient

kl
Ykl
ei(λk−λl) −1

"X

dU(c)

dcb,i
=



kl a†
kal

X


UMU †

=

k,l

where Mkl = Ykl ei(λk−λl)−1

#

b,i cb,iE−
b,i
(G14)

i (λk −λl) ˜a†
k˜al

e
P



b,i cb,iE−
b,i
(G15)

e
P

i(λk−λl) . The expression in the parenthesis is a new one-body operator that we previous denoted
∇f(Z).

Appendix H: Optimization Technique

The optimizer we use in the experiment is based on Kutzelnigg’s approach to iteratively constructing a wavefunction
that satisﬁes the Brillouin condition [34]. In the following section we include the derivation and modiﬁcations of this
procedure from Reference [34] for completeness.
This approach starts from the Lie-algebraic perspective on the
variational principle. The generators for variations in a norm conserved wavefunction are elements of a complex Lie
algebra. The variational principle which states

δ ˜E = δ⟨˜ψ|H| ˜ψ⟩= 0
(H1)

can be cast as stationarity with respect to a unitary group

U = eR R = −R†
(H2)

## Page 25

where R is an element of the Lie algebra L supporting H. Formulation of the variations in ˜E with respect to R is
formulated using the BCH expansion

˜E →˜E′ = ˜E + ⟨˜ψ| [H, R] | ˜ψ⟩+ 1

2⟨˜ψ| [[H, R] , R] | ˜ψ⟩+ ...
(H3)

and thus stationarity with respect to inﬁnitesimal variations in R implies

⟨˜ψ| [H, R] | ˜ψ⟩= 0 ∀R = −R†
(H4)

1.
Iteratively constructing wavefunctions

Given an R that does not satisfy the ﬁrst order stationarity condition Eq. (H4) we can propose a new wavefunction
that is approximately stationary with respect to R.

AR = ⟨φ| [H, R] |φ⟩̸= 0
(H5)

We want to determine an update of the generator R such that the ﬁrst order condition holds. We consider the update
to the wavefunction

ψ = e−fRRφ
(H6)

where fr is a real number. Considering how the energy changes as a function of fR

EfR = ⟨φ|efRRHe−fRR|φ⟩≈⟨φ|H + fR [H, R] + f 2
R
2 [[H, R] , R] |φ⟩
(H7)

In a similar fashion to deriving a Newton-Raphson update in optimization we can diﬀerentiate to ﬁnd an fR that
approximately satisﬁes Eq. (H4).

dEfR

dfR
= ⟨φ| [H, R] + fR

2 [[H, R] , R] |φ⟩= 0
fR = −AR/BR,R
BR,R = ⟨φ| [[H, R] , R] |φ⟩
(H8)

Alternatively, one can determine the change in the stationary condition with respect to fR

0 = ⟨φ|efRR [H, R] e−fRR|φ⟩= ⟨φ| [H, R] + fR [[H, R] , R] + f 2
R
2 [[[H, R] , R] , R] + ...|φ⟩
(H9)

and enforce the stationarity approximately by truncating at ﬁrst order and solving for fR

fR = −AR/BR,R
(H10)

which provides the same type of update. The error in the residual for R, AR, is now of the magnitude O(f 2
R) at leading
order. This update inspires a possible iterative procedure for improving the wavefunction that will quadratically
converge to the correct state if we are in a convex region away from the exact solution [34].
One can use the above procedure where R is not an element of the operator basis {Xk} of the Lie algebra L

R =
X

k
ckX , X ⊂L
(H11)

and to determine a set of ck which approximately satisfy Eq. (H4).

0 ≈⟨φ| [H, Xk] +
X

l
[[H, Xk] , Xl] cl|φ⟩
(H12)

Again, approximating the expansion in Eq. (H12) to ﬁrst order we get a system of equations to solve for ck that
ensures the Brillouin condition is satisﬁed up to leading error of O(c2
k).
In the context of a NISQ machine one needs to consider the family of generators {R} that is tractable and the cost
of the measurements associated with measuring AR and Bk,l. In this work we use

Ap,q = ⟨ψ|

H, a†
paq

|ψ⟩
Bp,q;r,s = ⟨ψ|

H, a†
paq

, a†
ras

|ψ⟩.
(H13)

## Page 26

Both the gradient and the Hessian term can be evaluated with knowledge of the 1-RDM under the assumption that
ψ corresponds to a Slater determinant. The update parameters to κ, fp,q are computed by solving the augmented
Hessian eigenvalue problem

 0
A
A† B

 
1
fp,q


= ϵ

1
fp,q


(H14)

which provides an optimal level shift to Newton’s method

A + (B −ϵ)fp,q = 0.
(H15)

As described in [35] we add regularization by limiting the size of the update fp,q by rescaling under the condition that
the max update is above a parameter γ

(
fp,q
max(fp,q) < γ
γ
max(fp,q)fp,q
max(fp,q) ≥γ
(H16)

The algorithm then dictates that the wavefunction is updated through Eq. (H6) which is yet another non-interacting
fermion wavefunction. We concatenate this basis rotation with the original using Eq. (B3) so the circuit depth remains
constant. The optimization procedure is iterated for a ﬁxed number of steps or the commutator ⟨[H, Xk]⟩falls below
a predeﬁned threshold.

Appendix I: Additional Performance Analysis

1.
Post-selection performance

In this section we examine the percentage of measurements rejected by post-selection as a function of system size
and ﬁdelity metrics across the systems studied in the hydrogen chain and diazene experiments. In Table II we plot
the ratio of the total number of circuit repetitions that result in the correct excitation number. As expected this
ratio decreases with system size, almost perfectly tracking a joint readout ﬁdelity of 95%. We believe the discrepancy
between the two 10-qubit experiments (H10 and diazene experiments) stems from the fact that the diazene circuits
have more idle circuit moments where the qubits are free to decay.

TABLE II. The average fraction of the 250,000 circuit repetitions used to measure observables for each circuit. The average
is collected across all hydrogen geometries and diazene geometries for every circuit required to estimate the 1-RDM for these
systems.

Plotted another way, we can examine the distribution of local qubit expectation values ⟨Mi⟩where Mi is the
measurement result of qubit i.
In Fig.
S12 we plot the integrated histogram of Mi–i.e.
the probability of a 1
bit being measured from qubit i–(denoted P1) on all the qubits for all circuits in all hydrogen chain experiments.
This is compared to the theoretical value obtained by the perfect 1-RDM simulation described in Appendix A 1. The
signiﬁcant improvement in readout scatter from post-selection is a fundamental driver in the success of this experiment
due to the sensitivity of quantum chemistry energies to electron number.

## Page 27

FIG. 12. Integrated histogram of readout performance with and without post-selection on photon number. Grey lines are the
histograms of circuit measurements without post-selection.

2.
Natural Occupation Numbers

In this section we tabulate the natural occupation numbers for the “raw” and the “post-selection” data sets.

TABLE III. H6 raw natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
0.5
0.0024 0.0181 0.0338 0.8738 0.9109 0.9402
0.9
0.0000 0.0176 0.0295 0.8888 0.9142 0.9405
1.3
0.0083 0.0182 0.0321 0.8808 0.9157 0.9417
1.7
0.0080 0.0209 0.0400 0.8780 0.8999 0.9518
2.1
0.0103 0.0130 0.0378 0.8884 0.9074 0.9438
2.5
0.0098 0.0128 0.0403 0.8868 0.9126 0.9427

TABLE IV. H6 +post-selection natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
0.5
-0.0006 0.0113 0.0271 0.9768 0.9861 0.9993
0.9
-0.0037 0.0146 0.0204 0.9815 0.9883 0.9989
1.3
0.0042 0.0139 0.0266 0.9726 0.9818 1.0009
1.7
0.0019 0.0164 0.0322 0.9656 0.9732 1.0106
2.1
0.0075 0.0124 0.0332 0.9711 0.9737 1.0021
2.5
0.0085 0.0094 0.0343 0.9689 0.9801 0.9988

TABLE V. H8 raw natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
λ7
λ8
0.5
-0.0033 0.0083 0.0197 0.0365 0.8909 0.8975 0.9046 0.9283
0.9
-0.0047 0.0126 0.0290 0.0435 0.8742 0.8800 0.9181 0.9331
1.3
-0.0060 0.0148 0.0275 0.0469 0.8622 0.8881 0.9129 0.9238
1.7
-0.0089 0.0210 0.0426 0.0538 0.8594 0.8736 0.9118 0.9179
2.1
0.0026 0.0247 0.0458 0.0532 0.8454 0.8634 0.9139 0.9295
2.5
0.0085 0.0259 0.0572 0.0610 0.8379 0.8801 0.9010 0.9168

## Page 28

TABLE VI. H8 +post-selection natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
λ7
λ8
0.5
-0.0087 0.0042 0.0146 0.0216 0.9779 0.9889 0.9944 1.0072
0.9
-0.0136 0.0080 0.0207 0.0350 0.9637 0.9731 0.9992 1.0138
1.3
-0.0160 0.0115 0.0237 0.0395 0.9535 0.9748 0.9998 1.0132
1.7
-0.0209 0.0181 0.0357 0.0512 0.9500 0.9634 0.9926 1.0099
2.1
-0.0120 0.0188 0.0411 0.0517 0.9458 0.9502 0.9947 1.0097
2.5
-0.0075 0.0115 0.0513 0.0568 0.9362 0.9660 0.9814 1.0043

TABLE VII. H10 raw natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
λ7
λ8
λ9
λ10
0.5
-0.0503 -0.0067 0.0087 0.0493 0.0638 0.8663 0.8747 0.8961 0.9109 0.9222
0.9
-0.0176 0.0109 0.0169 0.0514 0.0829 0.8359 0.8490 0.8779 0.9165 0.9182
1.3
-0.0050 0.0020 0.0215 0.0279 0.0460 0.8302 0.8868 0.8892 0.9142 0.9266
1.7
-0.0289 0.0107 0.0212 0.0343 0.0535 0.8529 0.8747 0.8795 0.9106 0.9372
2.1
-0.0092 0.0048 0.0145 0.0299 0.0596 0.8537 0.8651 0.8985 0.9217 0.9352
2.5
-0.0010 0.0118 0.0216 0.0300 0.0626 0.8470 0.8739 0.8842 0.9107 0.9258

TABLE VIII. H10 +post-selection natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
λ7
λ8
λ9
λ10
0.5
-0.0624 -0.0122 0.0021 0.0492 0.0553 0.9488 0.9826 0.9984 1.0130 1.0251
0.9
-0.0224 0.0056 0.0139 0.0408 0.0736 0.9306 0.9585 0.9830 0.9985 1.0179
1.3
-0.0126 -0.0110 0.0185 0.0276 0.0497 0.9262 0.9791 0.9967 0.9978 1.0278
1.7
-0.0397 -0.0005 0.0170 0.0290 0.0561 0.9470 0.9731 0.9825 1.0077 1.0276
2.1
-0.0215 0.0026 0.0057 0.0224 0.0529 0.9559 0.9583 0.9851 1.0069 1.0317
2.5
-0.0184 0.0057 0.0232 0.0248 0.0597 0.9441 0.9672 0.9817 0.9997 1.0122

TABLE IX. H12 raw natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
λ7
λ8
λ9
λ10
λ11
λ12
0.5
-0.0037 0.0010 0.0077 0.0182 0.0500 0.0589 0.8361 0.8515 0.8828 0.8910 0.8995 0.9098
0.9
-0.0195 0.0021 0.0118 0.0247 0.0413 0.0713 0.7948 0.8316 0.8816 0.8919 0.9019 0.9442
1.3
-0.0160 0.0066 0.0192 0.0346 0.0521 0.0823 0.8035 0.8179 0.8853 0.8911 0.9099 0.9198
1.7
-0.0016 0.0087 0.0276 0.0288 0.0458 0.0737 0.7967 0.8480 0.8614 0.8906 0.8991 0.9099
2.1
-0.0153 -0.0011 0.0235 0.0325 0.0572 0.0777 0.8198 0.8331 0.8556 0.8646 0.9132 0.9260
2.5
-0.0143 0.0029 0.0207 0.0564 0.0650 0.0821 0.8143 0.8351 0.8719 0.8750 0.8966 0.9131

TABLE X. H12 +post-selection natural orbitals
bond distance
λ1
λ2
λ3
λ4
λ5
λ6
λ7
λ8
λ9
λ10
λ11
λ12
0.5
-0.0120 -0.0029 0.0030 0.0137 0.0474 0.0536 0.9349 0.9540 0.9878 0.9968 1.0042 1.0194
0.9
-0.0310 -0.0039 0.0037 0.0222 0.0337 0.0735 0.8947 0.9397 0.9889 0.9970 1.0166 1.0649
1.3
-0.0260 -0.0009 0.0113 0.0216 0.0454 0.0817 0.8979 0.9265 0.9924 0.9976 1.0231 1.0292
1.7
-0.0074 0.0002 0.0147 0.0231 0.0459 0.0719 0.8964 0.9596 0.9665 0.9995 1.0082 1.0215
2.1
-0.0296 -0.0082 0.0172 0.0223 0.0593 0.0735 0.9170 0.9403 0.9715 0.9803 1.0134 1.0430
2.5
-0.0252 -0.0156 0.0096 0.0397 0.0618 0.0878 0.9139 0.9410 0.9782 0.9837 1.0029 1.0222

3.
Energy and Fidelity

In Fig. S13 we plot the log-log scatter of absolute error and ﬁdelity witness for all systems studied. The correlation
in the ﬁdelity and absolute energy error suggests that ﬁdelity can be used as an optimization target for this system.
This is a useful property when considering basis rotation states as targets for benchmarks and tune-up protocols.

## Page 29

FIG. 13. Absolute error versus ﬁdelity witness for VQE optimized with error mitigation for all experiments.

Slow two-level-system (TLS) diﬀusion on the surface of superconducting processors can alter the performance of
qubits over time periods of hours or days. It is likely that the H10 data set was collected during a time where the best
performing qubits had worse coupling to an itinerant TLS[48] than when we collected the H12 dataset. Thus, there
was some variance in performance across the diﬀerent days when the chip was used to collect data. We believe that
by showing all of these results without cherry picking and rerunning less performant curves, we give a more accurate
representation of the average performance of the device.
To better describe the consistent quality of VQE optimized 10 qubit calculations we tabulate the perceived ﬁdelity
calculated from puriﬁed 1-RDMs in all 10 qubit experiments: six H10 experiments and eighteen diazene points. On
all but one experiment variational relaxation combined with other error mitigation techniques allows us to achieve
> 98.0% average ﬁdelity.

FIG. 14. Fidelity of 10 qubit experiments: A histogram of ﬁdelity witness values associated with the VQE optimized 10
qubit systems.

Appendix J: Molecular geometries

For the hydrogen chains OpenFermion [49] and Psi4 [50] were used to generate the integrals. All hydrogen chains
were computed at atom-atom separations of 0.5, 0.9, 1.3, 1.7, 2.1, and 2.5 ˚A. For the diazene curves we used Psi4
to map out the reaction coordinate for each isomerization mechanism by optimizing the geometries of the molecule
simultaneously constraining either the dihedral angle or NNH angle to a ﬁxed value. Table XI and Table XII, below,
contain the geometries we considered for out-of-plane rotation and in-plane rotation of the hydrogen atom. To reduce

## Page 30

diazene to a 10 qubit problem we perform two cycles of canonical Hartree-Fock self-consistent ﬁeld and then integrate
out the bottom two energy levels.

TABLE XI. Out-of-plane rotation geometries
Internal coord. Atom
Cartesian coordinates
3.157
H
-0.00183 0.61231 -1.23326
N
-0.00183 0.61231 -0.16961
N
-0.00183 -0.56366 0.29317
H
0.05269 -1.28820 -0.48362

TABLE XII. In-plane rotation geometries
Internal Coord. Atom
Cartesian coordinates
108.736
H
0.00000
0.61228 -1.23237
N
0.00000
0.61228 -0.16925
N
0.00000 -0.56613 0.29515
H
0.00001 -1.25344 -0.51686
