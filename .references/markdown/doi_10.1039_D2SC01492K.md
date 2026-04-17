---
source_pdf: ../doi_10.1039_D2SC01492K.pdf
pages: 11
extracted_at: 2026-04-17T12:32:47+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Toward practical quantum embedding simulation of realistic chemical systems on near-term quantum computers"
author: "Weitang Li"
---

# doi_10.1039_D2SC01492K

Original title: Toward practical quantum embedding simulation of realistic chemical systems on near-term quantum computers

Author metadata: Weitang Li

Source PDF: ../doi_10.1039_D2SC01492K.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Showcasing research from Dr. Dingshun Lv’s group,
AI Lab Research, ByteDance Inc., Beijing, China and
Prof. Zhigang Shuai’s group, Tsinghua University, Beijing,
China.

Toward practical quantum embedding simulation of realistic
chemical systems on near-term quantum computers

Quantum computing may revolutionize chemistry, yet
near-term quantum computers are conﬁ ned by limited
number of qubits and noisy quantum gates. By integrating
energy sorting variational quantum eigensolver (ESVQE)
and density matrix embedding theory (DMET), the
applicability of near-term quantum computers is greatly
expanded. Numerical benchmarks on a variety of chemical
systems show that the DMET-ESVQE is able to reduce the
number of qubits required by an order of magnitude while
maintaining accuracy comparable to CCSD or Full CI.

rsc.li/chemical-science

Registered charity number: 207890

## Page 2

Chemical
Science

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Toward practical quantum embedding simulation
of realistic chemical systems on near-term
quantum computers†

Cite this: Chem. Sci., 2022, 13, 8953

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

All publication charges for this article
have been paid for by the Royal Society
of Chemistry

Weitang Li,ab Zigeng Huang,
a Changsu Cao,
a Yifei Huang,a Zhigang Shuai,
b

Xiaoming Sun,cd Jinzhao Sun,e Xiao Yuanf and Dingshun Lv
*a

Quantum computing has recently exhibited great potential in predicting chemical properties for various

applications in drug discovery, material design, and catalyst optimization. Progress has been made in

simulating small molecules, such as LiH and hydrogen chains of up to 12 qubits, by using quantum
algorithms such as variational quantum eigensolver (VQE). Yet, originating from the limitations of the size

and the ﬁdelity of near-term quantum hardware, the accurate simulation of large realistic molecules

remains a challenge. Here, integrating an adaptive energy sorting strategy and a classical computational

method—the density matrix embedding theory, which respectively reduces the circuit depth and the

problem size, we present a means to circumvent the limitations and demonstrate the potential of near-

This article is licensed under a

term quantum computers toward solving real chemical problems. We numerically test the method for

the hydrogenation reaction of C6H8 and the equilibrium geometry of the C18 molecule, using basis sets

up to cc-pVDZ (at most 144 qubits). The simulation results show accuracies comparable to those of
advanced quantum chemistry methods such as coupled-cluster or even full conﬁguration interaction,

Received 14th March 2022
Accepted 11th July 2022

while the number of qubits required is reduced by an order of magnitude (from 144 qubits to 16 qubits

DOI: 10.1039/d2sc01492k

for the C18 molecule) compared to conventional VQE. Our work implies the possibility of solving

industrial chemical problems on near-term quantum devices.

rsc.li/chemical-science

reach.7–11 In the present noisy intermediate-scale quantum
(NISQ) era,12 variational quantum eigensolver (VQE), as one of
the most popular quantum-classical algorithms,4,13–27 has been
exploited to experimentally study molecules from H2 (2
qubits),14 BeH2 (6 qubits),15 H2O (8 qubits),26 to H12 (12 qubits)16

1
Introduction

Various methods based on wave function theory, from the
primary mean-eld Hartree–Fock to high accuracy coupled-
cluster and full conguration interaction methods, have been
developed to simulate many-electron molecular systems.1,2

and isomers of benzyne C6H4 (4 qubits).28,29 Meanwhile, the
largest scale numerical molecular VQE simulation is C2H4 (28
qubits).27 The simulation of even large molecular systems might
be realized in the future with the recently developed fermionic
quantum emulator,30 which utilizes the particle number and
spin symmetry along with custom evolution routines for
Hamiltonians to reduce the memory requirement.
However, realistic chemical systems with an appropriate
basis set generally involve hundreds or thousands of qubits,
and whether VQE with NISQ hardware is capable of solving any
practically meaningful chemistry problems remains open. The
main challenge owes to limitations on the size (the number of
qubits) and the delity (the simulation accuracy) of NISQ
hardware.12,17,18,21 Specically, it is yet hard to scale up the
hardware size, while maintaining or even increasing the gate
delity. Experimentally, when VQE is directly implemented on
more than hundreds of qubits, the number of gates needed
might become too large so that errors would accumulate dras-
tically and error mitigation would require too many measure-
ments to reach the desired chemical accuracy.

However, owing to the exponential wall,3 the exact treatment of
those systems with more than a few dozens of orbitals remains
intractable for classical computers, hindering further investi-
gations
on
large
realistic
chemical
systems.
Quantum
computing is believed to be a promising approach to overcome
the exponential wall in quantum chemistry simulation,4–6 which
may potentially boost relevant elds such as material design
and drug discovery. Despite the great potential, fault-tolerant
simulation of realistic molecules is still far beyond the current

aByteDance Inc, Zhonghang Plaza, No. 43, North 3rd Ring West Road, Haidian District,
Beijing, China. E-mail: lvdingshun@bytedance.com

bDepartment of Chemistry, Tsinghua University, Beijing 100084, China

cInstitute of Computing Technology, Chinese Academy of Sciences, China

dUniversity of Chinese Academy of Sciences, China

eCenter on Frontiers of Computing Studies, Peking University, Beijing 100871, China

fClarendon Laboratory, University of Oxford, Oxford OX1 3PU, UK

† Electronic
supplementary
information
(ESI)
available.
See
https://doi.org/10.1039/d2sc01492k

© 2022 The Author(s). Published by the Royal Society of Chemistry
Chem. Sci., 2022, 13, 8953–8962 | 8953

## Page 3

View Article Online

Chemical Science
Edge Article

Adaptive
and
hybrid
classical-quantum
computational
methods provide more economical ways to potentially bypass
the conundrum. On the one hand, adaptive VQE algorithms31–44

can greatly reduce the circuit depth and hence alleviate the
limitation on the gate delity. On the other hand, noticing the
fact that most quantum many-body systems have mixed strong
and weak correlation, we only need to solve the strongly corre-
lated degrees of freedom using quantum computing and
calculate the remaining part at a mean-eld level using classical
computational
methods.
Along
this
line,
several
hybrid
methods have been proposed by exploiting diﬀerent classical
methods,45–47 such as density matrix embedding theory,48–51

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

dynamical mean eld theory,52–54 density functional theory
embedding,55 quantum defect embedding theory,56,57 tensor
networks,23,58
and
perturbation
theory.59
Density
matrix
embedding is one of the representative embedding methods
that have been theoretically and experimentally developed in
several studies,6,48–51,60–67 yet the practical realization toward
realistic chemical systems remains a signicant technical
challenge.
In this work, we integrate the adaptive energy sorting
strategy68 and density matrix embedding theory,48–51,62 and
provide a systematic way with multiscale descriptions of
quantum systems toward practical quantum simulation of
realistic molecules. We numerically study chemical systems
with strong electron–electron correlation with specic geome-
tries, including the homogeneous stretching of the H10 chain,
the reaction energy prole for the hydrogenation of C6H8 and
the potential energy curve of the C18 molecule.69 While using
a much smaller number of qubits (from 144 qubits to 16 qubits
for the C18 molecule) and a much shallower quantum circuit,
our method can still reach high accuracy comparable to coupled
cluster or even full conguration interaction calculations. Our
work reveals the possibility of studying realistic chemical
processes on near-term quantum devices.

This article is licensed under a

2
Framework

The generic Hamiltonian of a quantum chemical system under
the
Born–Oppenheimer
approximation4
in
the
second-
quantized form can be expressed as

^
H ¼ Enuc þ
X

k;l
^Dkl þ
X

k;l;m;n
^V klmn;
(1)

where Enuc is the scalar nuclear repulsion energy, ^Dkl ¼ dkl^a†
k^al

and ^Vklmn ¼ 1
2hklmn^a†
k^a†
l ^am^an are the one and two-body inter-

action operators, respectively, ^ap (^a†
p) is the fermionic annihi-
lation (creation) operator to the pth orbital, and {dkl} and {hklmn}
are the corresponding one- and two-electron integrals calcu-
lated with classical computers, respectively. Here, we denote the
spin-orbitals of the molecule as k, l, m, and n. Variational
quantum eigensolvers (VQEs) can be used to nd a ground state
of the Hamiltonian in eqn (1).4,17 The key idea is that the
parametrized quantum state J(q⃑) is prepared and measured
on a quantum computer, while the parameters are updated
using a classical optimizer on a classical computer. The ground

state can be found by minimizing the total energy with respect
to the variational parameters q⃑, following the variational
principle, E ¼ minq⃑hJ(q⃑)j^HjJ(q⃑)i.
The above quantum algorithm entails a number of qubits no
smaller than the system size, making it inaccessible to large
realistic molecular systems. Here, we introduce the quantum
embedding approach, a powerful classical method originally
proposed by Knizia et al.,48 to reduce the required quantum
resources. We consider to divide the total Hilbert space H of the
quantum system into two parts, the fragment A with LA bases
{jAii} and the environment B with LB bases {jBji}, respectively.
The full quantum state in the {jAiijBji} basis can be represented
by jJi ¼ P

i;j
Ji;jjAii
Bji with dimensions LA  LB. However, this

can be largely reduced by considering the entanglement
between the two parts. Specically, the quantum state jJi can
be
decomposed
into
a
rotated
basis
f
~Aai
~Baig
as

a
la
~Aai
~Bai, corresponding to Schmidt decomposition

jJi ¼ P
LA

of bipartite states. Aer the decomposition, we can split the
environment into at most LA bath states that are entangled with
the fragment and purely disentangled ones. We could thus
construct the embedding Hamiltonian by projecting the full
Hamiltonian ^H3H into the space spanned by the basis of the
fragment and bath as ^Hemb ¼ ^P ^H^P with the projector ^P dened
as ^P ¼ P

~Aa~Bbih~Aa~Bb
: We note that the embedding Hamilto-

ab

nian can be represented in the rotated spin-orbitals p, q, r, s

with renormalized coeﬃcients ~dp;q and ~hp;q;r;s (see the ESI†),
and admits the second-quantized form as that in eqn (1).
We can nd that if jJi is the ground state of a Hamiltonian
^H, it must also be the ground state of ^Hemb. This indicates that
the solution of a small embedded system is the exact equivalent
to that of the full system,50 with the dimensions of the
embedded system reduced to LA  LA. In principle, the
construction of ^P requires the exact ground state of the full
system jJi, which makes it unrealistic from theory. However,
since we are interested in the ground state properties (for
instance, the energy, which is a local density), we can consider
to match the density or density matrix of the embedding
Hamiltonian and the full Hamiltonian at a self-consistency
level. More specically, we consider a set of coupled eigen-
value equations

^
HmfjFi ¼ EmfjFi, ^
HembjJi ¼ EembjJi,
(2)

which describe a low-level mean-eld system and a high-level
interacting embedding system, respectively. Here, the mean-
eld Hamiltonian can be constructed provided the correlation
potential ^C as ^Hmf ¼ ^H0
mf + ^C, and we can eﬃciently obtain the
low-level wavefunction jFi and hence the one-body reduced
density matrix 1Dkl ¼ h^a†
k^ali. Here H^mf0 is the original mean-
eld Hamiltonian constructed directly from ^H and 1Dkl. Given
the solution of the eigenvalue equations in eqn (2), we can also
obtain the reduced density matrix of the embedded system. At
a self-consistency level, we can match the reduced density
matrices of the multilevel systems by adjusting the correlation

8954 | Chem. Sci., 2022, 13, 8953–8962
© 2022 The Author(s). Published by the Royal Society of Chemistry

## Page 4

View Article Online

Edge Article
Chemical Science

potential ^C in the mean-eld Hamiltonian ^Hmf, and we obtain
a guess for the ground state solution at convergence.
Next, we discuss how to get the solution of the high-level
embedding Hamiltonian using variational quantum eigensolv-
ers. The key ingredient in VQE is to design an appropriate
circuit ansatz to approximate the unknown ground state of the
chemical system. Here, we use the unitary coupled-cluster
(UCC) ansatz,70–72 which eﬀectively considers the excitations
and de-excitations above a reference state. The UCC ansatz is
dened as jJi ¼ exp(^T  ^T†)jJ0i, where jJ0i is chosen as the
Hartree–Fock ground state represented in the basis of the
embedded system, and ^T is the cluster operator. The cluster
operator truncated at single- and double-excitations has the
form

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

^T

q!
¼
X

qpr ^Tpr þ
X

qpqrs ^Tpqrs;

p˛vir
r˛occ

p . q;r . s:
p;q˛vir
r;s˛occ

where the one- and two-body terms are dened as ^Tpr ¼ ^a†
p^ar and
^Tpqrs ¼ ^a†
p^a†
q^ar^as, respectively. Then, we can get the high-level
wavefunction by optimizing the energy of the embedded
system, E ¼ minqhJ(q⃑)j^HembjJ(q⃑)i, and thus can obtain the
reduced density matrices 1D. Matching the reduced density
matrices with those of the mean-eld system forms a self-
consistency loop until convergence.

This article is licensed under a

3
Implementation

Here, we discuss the implementation of the quantum embed-
ding theory in practice. In this work, we employ the energy
sorting (ES) strategy68 to select only the dominant excitations in
the original operator pool and construct a compact quantum
circuit in VQE procedures. We term the algorithm DMET-ESVQE
and an overall schematic owchart is presented in Fig. 1. Our
detailed algorithm can be found in the ESI.†
In practical molecular DMET implementation, we determine
the
fragment
partition
on
the
basis
of
atomic
orbital

Fig. 1
The workﬂow for the DMET–ESVQE method. The chemical
system is ﬁrst decomposed into fragments. Then the eﬀective
embedding Hamiltonian Hemb(mglobal) in DMET iteration is solved by
ESVQE. The ESVQE module utilizes quantum devices in the blue box to
prepare quantum states and measure physical observables. Both
DMET iteration and ESVQE parameter optimization are carried out on
a classical computer, indicated by green boxes.

interactions. The conventional partitioning based on clusters of
atoms chooses the set of single-particle bases UA
0 for fragment A
as UA
0 ¼ W
j UA
j , where UA
j is the set of bases located on the jth
atom of fragment A. Here, we dene a set of inactive orbitals
UA
mf treated at the mean-eld level and excluded from the DMET

iteration, resulting in a reduced basis set UA ¼ UA
0
UA
mf
. Note that

UA
mf could be an empty set. Compared to UA
0, UA can more
eﬀectively capture the entanglement between the orbitals and is
more compact for the VQE procedure. During the DMET opti-
mization, we introduce a global chemical potential mglobal to
preserve the total number of electrons Nocc, and the DMET cost
function LðmglobalÞ can now be written as

X

!2
;
(3)

X
LA

L

mglobal

¼

1Dfrag;A
rr

mglobal

þ Nmf  Nocc

A

r˛UA

where Nmf ¼ P

P

1Dmf
rr
is the number of electrons in the

A

r˛UA
mf

inactive orbitals obtained at the mean-eld level, termed the
single-shot embedding.50 We note that 1Dmf
rr is invariant during
single-shot embedding iteration, and thus Nmf is not a function
of mglobal. This feature distinguishes the approach from simply
adopting an active space high-level solver. More details can be
found in the ESI.†
For the ESVQE part, an eﬃcient ansatz for each of the frag-
ment is constructed by selecting dominant excitation operators
in the operator pool O ¼ f^Tpr; ^Tpqrsg. Here, the importance of
the operator ^Ti˛O is evaluated by the magnitude of energy
diﬀerence between the reference state as DEi ¼ Ei  Eref with Ei
¼ minqihJrefjeqi(^Ti 
^T†
i )^Heqi(^Ti 
^T†
i )jJrefi and Eref ¼
hJrefj^HjJrefi.
The
operators
with
contributions
above
a threshold jDEij > 3 are picked out and used to perform the VQE
optimization. Extra ne-tuning can be performed by iteratively
adding more operators to the ansatz until the energy diﬀerence
E(k1)  E(k) between the (k  1)th and the kth iteration is smaller
than a certain convergence criterion. In this work we skip this
step for simplicity. More details can be found in the ESI.†

Fig. 2
DMET–ESVQE simulated homogeneous stretching of an evenly
spaced hydrogen chain composed of 10 atoms in (a) STO-3G and (b)
6-31G basis sets, in comparison with RHF, CCSD and FCI results. The
MRCI + Q + F12@CBS results in both panels can be considered as the
exact reference in the complete basis set (CBS) limit.74 For the STO-3G
basis set, we also show the results obtained by conventional ESVQE.
The grey horizontal line indicates the exact dissociation limit
composed of non-interacting hydrogen atoms.

© 2022 The Author(s). Published by the Royal Society of Chemistry
Chem. Sci., 2022, 13, 8953–8962 | 8955

## Page 5

View Article Online

Chemical Science
Edge Article

4
Results and discussion

To benchmark our algorithm, we rst show the simulated
potential energy curve for the homogeneous stretching of
a hydrogen chain composed of 10 atoms in Fig. 2, a benchmark
platform for advanced many-body computation methods.73,74

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Classical quantum chemistry calculations are performed with
the PySCF package75 (the same hereinaer unless otherwise
stated). In our DMET-ESVQE simulation, we consider each
hydrogen atom as a fragment ðUA
mf ¼ BÞ. With both STO-3G
and 6-31G basis sets, DMET–ESVQE is in excellent agreement
with FCI results. The coupled-cluster singles and doubles
(CCSD) method performs well near the equilibrium bond
distance; however, in the dissociation limit (bond distance > 1.7
˚A) its calculation fails to converge.74 For the STO-3G basis set,
conventional ESVQE with 20 qubits is performed for a limited
number of bond distances due to the prohibitive computational
cost. Surprisingly, in the dissociation limit, DMET–ESVQE is
more accurate than conventional ESVQE despite the drastic
reduction of the number of qubits. This counter-intuitive
outcome, along with a detailed analysis of the errors, is dis-
cussed in the ESI.† To evaluate the error introduced by the
incomplete basis set, we include results from the MRCI + Q +
F12 method in the complete basis set (CBS) limit,74 which can
be considered as the true ground state energy for the potential
energy curve of H10. By comparing Fig. 2(a) and (b), we nd that
using a larger basis set brings the potential energy curve
produced by DMET–ESVQE much closer to the MRCI + Q +
F12@CBS reference curve and the exact dissociation limit,
which is only made possible by the DMET framework.
Next, we study the energy prole for the addition reaction
between C6H8 and H2 in the gas phase, which is a simplied
model for the addition of hydrogen to conjugated hydrocar-
bons, an essential step for many organic synthesis routes.76–78 A
schematic diagram of the addition reaction is depicted in
Fig. 3(a). A large fraction of the molecule is involved in conju-
gated p bonds, which poses a challenge for quantum embed-
ding theories. Besides, the transition state, dened as the rst
order saddle point in the potential energy surface, is known to

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

This article is licensed under a

Fig. 3
The potential energy curve for the hydrogenation reaction of
C6H8 with H2. (a) A schematic view for the hydrogenation reaction of
C6H8 with H2. Each atom in the magenta box is considered as a single
fragment. (b) Comparison of the energies obtained with RHF, B3LYP,
CCSD and DMET-ESVQE along the IRC of the reaction. The relative
energy Erel is E  ETS where ETS is the transition state energy. Note that
ETS is diﬀerent for diﬀerent methods.

be diﬃcult for electronic structure methods. In DMET–ESVQE
simulation, each atom in the magenta box is considered as
a single fragment with the 1s orbitals for carbon atoms frozen.
The transition state and the intrinsic reaction coordinates
(IRCs)79 for the reaction are determined by density functional
theory (DFT) with the hybrid functional B3LYP under an STO-3G
basis set using the Gaussian 09 package.80 In Fig. 3(b), we plot
the relative energy Erel ¼ E  ETS along with the IRC, where ETS is
the transition state energy. The absolute value of ETS can be
found in the ESI.† In agreement with the common quantum
chemistry perception, restricted Hartree–Fock (RHF) over-
estimates the reaction barrier, while B3LYP (DFT) underesti-
mates the reaction barrier. On the other hand, the energy prole
generated by DMET–ESVQE is in remarkable agreement with
the highly accurate and time-consuming CCSD method. We
note that using a basis set larger than STO-3G is essential for
a more realistic description of the reaction.
The last system studied is the C18 molecule, a novel carbon
allotrope with many potential applications such as molecular
devices due to its exotic electronic structure.81–84 Before its
experimental identication,69 the equilibrium geometry of the
molecule is under heated debate: DFT and perturbation theory
(MP2) oen conclude a D18h cumulenic structure, yet high-level
CCSD calculations indicate that a bond-length and bond-angle
alternated polyynic structure is more energetically favoured.85

In 2019, the polyynic structure is conrmed unambiguously via
experimental synthesis of the molecule.69 In this work we
investigate a series of geometries of the C18 molecule, as shown
in Fig. 4(a), to determine the molecule's equilibrium geometry.
These geometries are generated by relatively rotating two

Fig. 4
(a) A schematic diagram of the C18 molecule. q is the angle
between the two interleaving C9 nonagons, one of which is indicated
with orange dashed lines. R is the radius of the regular nonagons. d1
and d2 are the two sets of C–C bond lengths, respectively. (b) and (c)
Comparison of the energies obtained with UHF, B3LYP, CCSD and
DMET-ESVQE for the potential energy curve of the C18 molecule
within (b) STO-3G and (c) cc-pVDZ basis sets. The relative energy Erel is
deﬁned as E  Ecumu where Ecumu is the energy for the q ¼ 20

cumulenic structure. The DMET-ESVQE results suggest that the bond-
length alternating structure is favoured, which agrees with experi-
mental observation.

8956 | Chem. Sci., 2022, 13, 8953–8962
© 2022 The Author(s). Published by the Royal Society of Chemistry

## Page 6

View Article Online

Edge Article
Chemical Science

interleaving C9 regular nonagons by an angle of q ˛ [0, 40], with
all carbon atoms located on the same plane. We dene d1 and d2
as the lengths of the two sets of C–C bonds in the molecule and
the bond length alternation (BLA) as d1  d2. The q ¼ 20

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

geometry is known as the cumulenic structure, while for other
cases the geometries with D9h symmetry are called the polyynic
structure. The radius R of the regular nonagon is determined to
be 3.824 ˚A via geometry optimization at the CCSD/STO-3G level
using the Gaussian 09 package.80

In Fig. 4(b), we present the potential energy curve in the
physically intriguing region q ˛ [16.8, 23.2] within the STO-3G
basis set. The relative energy Erel is Erel ¼ E  Ecumu, where Ecumu
is the energy for the q ¼ 20 cumulenic structure. The absolute
value of Ecumu can be found in the ESI.† For this pathological
system, RHF is known to suﬀer from the convergence problem84

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

and thus the unrestricted Hartree–Fock (UHF) results are
shown. However, the UHF energy curve is qualitatively incorrect
in that it anticipates the cumulenic structure to be more stable.
The representative DFT method B3LYP predicts a rather at
potential energy curve around q ¼ 20 and the polyynic struc-
ture is slightly favoured by 11 mH compared to that of the
cumulenic structure. Because it is well documented that the full
degree of freedom optimization at the B3LYP level yields
a cumulenic structure,84–86 we believe the slight advantage of the
polyynic structure shown in Fig. 4(b) is an artifact of the xed R.
In DMET-ESVQE simulation, we treat each carbon atom as
a fragment with the 1s orbital frozen. As illustration, the
orbitals of the fragment and the corresponding bath under the
STO-3G basis set at the angle q ¼ 18 are shown in Fig. 5. The
orbitals are generated by the PYSCF package and drawn by
using VESTA soware.87 Unlike UHF and B3LYP, DMET–ESVQE
correctly reproduces the polyynic structure. We note that
solving the ground state of the full molecule with conventional
VQE requires 144 qubits under frozen core approximation,
while for DMET–ESVQE 16 qubits are suﬃcient for a correlated
treatment of the whole molecule. Fig. 4(c) shows the results with
Dunning's correlation-consistent basis set cc-pVDZ.88 In DMET-
ESVQE simulation, the 2s and 2p basis orbitals for each carbon
atom are considered as a single fragment and thus the eﬀect of
high angular momentum orbitals is treated at the mean-eld

This article is licensed under a

level. The general trends reected by Fig. 4(b) and (c) are
consistent and only CCSD and DMET–ESVQE are able to
produce the correct equilibrium geometry.

5
Simulation with noise

To evaluate the algorithm on real noisy quantum devices, we
performed noisy simulations on the H10 molecule with the STO-
3G basis set using the QASM simulator from the Qiskit toolkit.89

As shown in Fig. 6(a), we rst evaluate the shot-noise eﬀect with
the number of shots ranging from 210 to 218 without extra gate
noise. DMET-ESVQE exhibits fast convergence versus the repe-
titions of the quantum circuit. The diﬀerence between the
reference values and the simulated result is no more than 15
mH. When the number of shots is increased to 214, the standard
deviation also decreases to around 1 mH.
We next consider depolarizing noise and apply zero-noise
extrapolation based on linear tting using the Mitiq package90

to mitigate noise, as shown in Fig. 6(b). The quantum observ-
able is measured at noise-scaled quantum circuits by unitary
folding and extrapolated to the zero-noise limit by linear tting.
The scaling factors are 1.00, 1.25 and 1.50 in our calculations.
The calculated energy by naively applied DMET–ESVQE fails
when
encountering
large
noise
(depolarizing
probability,
Pdepolar $ 5  103). For smaller Pdepolar, the deviation becomes
smaller to tens of mH. Aer quantum error mitigation, the

Fig. 6
(a) DMET–VQE energy vs. number of shots for the H10 mole-
cule without introducing gate noise. The bond distance is set to 1.0 ˚A.
(b) DMET–VQE energy vs. depolarizing probability with 216 shots. The
red line is the calculated DMET–ESVQE energy using the ideal solver.

Fig. 5
The fragment and bath orbitals of the C18 molecule under the STO-3G basis set at the angle q ¼ 18. (a)–(d) Fragment orbitals corre-
sponding to localized 2s and 2p orbitals in a single carbon atom (red ball). (e)–(h) Bath orbitals obtained by Schmidt decomposition.

© 2022 The Author(s). Published by the Royal Society of Chemistry
Chem. Sci., 2022, 13, 8953–8962 | 8957

## Page 7

View Article Online

Chemical Science
Edge Article

Table 1
The reduction of the number of qubits and excitation parameters by DMET and ESVQE. cVQE represents conventional VQE without the
energy sorting (ES) strategy

System
Basis
Electrons
Spin–orbitals
Method
Qubits
Parameters

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

H10
STO-3G
10
20
cVQE
20
350
DMET–cVQE
4
2
DMET–ESVQE
4
1
H10
6-31G
10
40
cVQE
40
2925
DMET–cVQE
8
14
DMET–ESVQE
8
10
C6H8 + H2
STO-3G
34
68
cVQE
68
42 194
DMET–cVQE
16
152
DMET–ESVQE
16
105
C18
STO-3G
72
144
cVQE
144
841 752
DMET–cVQE
16
152
DMET–ESVQE
16
44
C18
cc-pVDZ
72
144
cVQE
144
841 752
DMET–cVQE
16
152
DMET–ESVQE
16
43

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

deviation from the reference value decreases from 2.065 Hartree
to 0.249 Hartree for Pdepolar ¼ 5  103. For calculations with
smaller Pdepolar, aer QEM the deviation is further reduced to
less than 10 mH. DMET–ESVQE calculations show fast conver-
gence with the number of shots and robustness to noise.
With the quantum error mitigation method, we can achieve
desired simulation accuracy with respect to the reference value
computed from an ideal simulator. Our result indicates
a promising application on real quantum devices.

This article is licensed under a

6
Quantum resource reduction

For the systems investigated in this work, DMET–ESVQE is able
to reduce the number of qubits by about an order of magnitude
and the number of excitation parameters by several orders of
magnitude, and thus eﬀectively reduces the resource require-
ments for quantum devices. In Table 1 we show the reduction of
the number of qubits and excitation parameters by DMET and
ESVQE. For H10 the bond distance is set to 3 ˚A while for C6H8 +
H2 and C18 we use the transition state geometry and the
cumulenic geometry respectively. When counting the total
number of electrons and spin-orbitals, for C6H8 + H2 and C18
(STO-3G), we have frozen the 1s orbitals, and for C18 (cc-pVDZ)
we have also frozen the 3s, 3p and 3d orbitals, in order for a fair
comparison with DMET. For conventional VQE (cVQE), the
number of qubits required are the same as the number of spin-
orbitals, assuming Jordan–Wigner transformation. In DMET
schemes, the number of qubits for the quantum solver is
determined by the maximum number of orbitals in each of the
fragment. Suppose in fragment A there are LA spin orbitals and
accordingly there are LA spin orbitals for the bath, then under
fermion-to-qubit
mapping (such as Jordan–Wigner trans-
formation) 2LA qubits are required for the quantum solver. The
number of excitation parameters is computed assuming that
the total spin of the molecule is zero. Suppose there are nocc
occupied spatial-orbitals and nvir unoccupied spatial-orbitals,
the total number of independent excitation amplitudes is:

Nex ¼ noccnvir + noccnvir(noccnvir + 1)/2
(4)

where the rst term and the second term correspond to single-
and double-excitations respectively. For the cumulenic structure
of C18 DMET and ESVQE together realize a 19 576-fold parameter
number reduction. We expect the eﬀect of DMET to be more
prominent for more complex chemical systems. We note here
that each parameter is associated with a generator ^Ti  ^T†
i , which
then transformed into the qubit type Pauli operator. The expo-
nential of the generator will decompose into a sequence of single-
qubit gates and two-qubit gates aer the Trotter decomposition.
We refer readers to nd more details about the decomposed
quantum gate and depth for the corresponding single-excitation
and double-excitation in Sec. II in the ESI.†

7
Conclusion

In this work, we propose to integrate ESVQE with DMET for the
study of realistic chemical problems. For benchmarking
purposes, the typical model system H10 is rst tested with the
STO-3G basis set, and we nd that DMET–ESVQE reaches near
FCI accuracy. DMET also enables ESVQE simulation of H10 with
the 6-31G basis set, producing a potential energy curve much
closer to the reference result in the complete basis set limit. The
study of the hydrogenation reaction between C6H8 and H2
shows that the accuracy of DMET–ESVQE is comparable to that
of CCSD, while the number of qubits required for VQE is
reduced from 68 qubits to 16 qubits. The last case studied in
this work is the equilibrium geometry of the C18 molecule and it
is found that DMET–ESVQE correctly predicts the experimen-
tally observed polyynic structure with a signicant reduction of
the quantum resource, from 144 qubits to 16 qubits. Our results
suggest that the DMET embedding scheme can eﬀectively
extend the simulation scale of the state-of-the-art NISQ
quantum computers.
To further expand the capability of quantum embedding
simulation, the eﬀort could be divided into two directions:
improved embedding scheme and high-level quantum solvers.

8958 | Chem. Sci., 2022, 13, 8953–8962
© 2022 The Author(s). Published by the Royal Society of Chemistry

## Page 8

View Article Online

Edge Article
Chemical Science

For the embedding scheme part, the eﬀorts could be further
divided into three sub-directions. One may need to develop
more eﬀective partition schemes to capture the correlation
between the fragment and bath. Or, one may apply the self-
consistent tting feature with a correlation potential to the
DMET iteration and try other cost functions, respectively.50

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Particularly, one may consider to speed up the convergence
through projected DMET60 and enhance the robustness and
eﬃciency of DMET via semidenite programming and local
correlation potential tting.63 Finally, one may consider the
bootstrap embedding scheme, which has been tested on larger
molecule systems to achieve better accuracy and faster conver-
gence.91–93 For the high-level quantum solvers part, there are at
least several directions that one can pursue. For the ESVQE, one
may reduce the energy threshold 3 to increase the operator pool
size selected for the VQE iteration, thus further increasing the
accuracy. Apart from the energy sorting scheme, it is worth
trying other schemes such as k-UpCCGSD31 to prepare trial
states in the high-level quantum solver. One may also try more
eﬃcient optimizers or more advanced quantum algorithms to
nd the ground state.94–99 When implementing the high-level
quantum solver on real quantum systems, one may explore
quantum error mitigation methods to improve the accuracy of
the measurement results.100–105 For more eﬃcient simulation of
larger molecule systems, advanced measurement schemes can
be used to reduce the measurement cost, such as (derandom-
ized) classical shadows or Pauli grouping methods to reduce the
measurement overhead.13,15,106–108

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

This article is licensed under a

The synergistic development of quantum embedding theory,
high-level quantum solvers and quantum devices provides a great
chance of solving strongly correlated chemical systems in future.
For example, one of the holy grails for quantum chemistry is the
electronic structure of the iron–sulfur clusters of nitroge-
nase,7,109,110 which contains eight transition metal atoms and
exhibits strong correlation. Within the polarized triple-zeta basis
set, it requires about 50 basis functions to describe each metal
atom. If, in the future, 200 qubits with a suﬃciently long coher-
ence time and high gate delity are available, the clusters can be
divided into fragments consisting of individual transition metal
atoms, such that the fragment + bath problem of embedded
transition metal atoms can be solved accurately using eﬃcient
VQE algorithms. The successful implementation of the proposed
protocol may elucidate the complicated interaction of transition
metal atoms and push the boundary of theoretical chemistry.

Data availability

Data for this paper are available at Zenodo at https://doi.org/
10.5281/zenodo.6544996.

Author contributions

D. Lv conceived the project. D. Lv, W. Li and Z. Huang imple-
mented the DMET–ESVQE algorithm. W. Li collected the
numerical data with the help from Z. Shuai. W. Li, Z. Huang, C.
Cao, Y. Huang, J. Sun, X. Yuan, and D. Lv wrote the manuscript.
J. Sun, X. Yuan and X. Sun helped analyze the data.

Conﬂicts of interest

The authors declare that there are no competing interests.

Acknowledgements

The authors gratefully thank Jiajun Ren, Chong Sun, Hongzhou
Ye, Hung Q. Pham, He Ma and Xuelan Wen, Nan Sheng, Zhihao
Cui, Zhen Huang, and Ji Chen for helpful discussions and Hang
Li for support and guidance.

Notes and references

1 A. Szabo and N. S. Ostlund, Modern Quantum Chemistry:
Introduction
to
Advanced
Electronic
Structure
Theory,
Courier Corporation, 2012.
2 I. N. Levine, D. H. Busch and H. Shull, Quantum Chemistry,
Pearson Prentice Hall, Upper Saddle River, NJ, 2009, vol. 6.
3 W. Kohn, Rev. Mod. Phys., 1999, 71, 1253–1266.
4 S. McArdle, S. Endo, A. Aspuru-Guzik, S. C. Benjamin and
X. Yuan, Rev. Mod. Phys., 2020, 92, 015003.
5 A. Aspuru-Guzik, A. D. Dutoi, P. J. Love and M. Head-
Gordon, Science, 2005, 309, 1704–1707.
6 B. Bauer, S. Bravyi, M. Motta and G. K.-L. Chan, Chem. Rev.,
2020, 120, 12685–12717.
7 M. Reiher, N. Wiebe, K. M. Svore, D. Wecker and M. Troyer,
Proc. Natl. Acad. Sci. U. S. A., 2017, 114, 7555–7560.
8 Z. Li, J. Li, N. S. Dattani, C. Umrigar and G. K.-L. Chan, J.
Chem. Phys., 2019, 150, 024302.
9 D. W. Berry, C. Gidney, M. Motta, J. R. McClean and
R. Babbush, Quantum, 2019, 3, 208.
10 V. von Burg, G. H. Low, T. H¨aner, D. S. Steiger, M. Reiher,
M. Roetteler and M. Troyer, Phys. Rev. Res., 2021, 3, 033055.
11 J. Lee, D. W. Berry, C. Gidney, W. J. Huggins, J. R. McClean,
N. Wiebe and R. Babbush, PRX Quantum, 2021, 2, 030305.
12 J. Preskill, Quantum, 2018, 2, 79.
13 P. J. O'Malley, R. Babbush, I. D. Kivlichan, J. Romero,
J.
R.
McClean,
R.
Barends,
J.
Kelly,
P.
Roushan,
A. Tranter, N. Ding, et al., Phys. Rev. X, 2016, 6, 031007.
14 A.
Peruzzo,
J.
McClean,
P.
Shadbolt,
M.-H.
Yung,
X.-Q. Zhou, P. J. Love, A. Aspuru-Guzik and J. L. O’brien,
Nat. Commun., 2014, 5, 1–7.
15 A. Kandala, A. Mezzacapo, K. Temme, M. Takita, M. Brink,
J. M. Chow and J. M. Gambetta, Nature, 2017, 549, 242–246.
16 F. Arute, K. Arya, R. Babbush, D. Bacon, J. C. Bardin,
R. Barends, S. Boixo, M. Broughton, B. B. Buckley,
D. A. Buell, et al., Science, 2020, 369, 1084–1089.
17 M. Cerezo, A. Arrasmith, R. Babbush, S. C. Benjamin,
S. Endo, K. Fujii, J. R. McClean, K. Mitarai, X. Yuan,
L. Cincio and P. J. Coles, Nat. Rev. Phys, 2021, 3, 625–644.
18 K. Bharti, A. Cervera-Lierta, T. H. Kyaw, T. Haug, S. Alperin-
Lea, A. Anand, M. Degroote, H. Heimonen, J. S. Kottmann,
T. Menke, W.-K. Mok, S. Sim, L.-C. Kwek and A. Aspuru-
Guzik, Rev. Mod. Phys., 2022, 94, 015004.
19 W. J. Huggins, J. R. McClean, N. C. Rubin, Z. Jiang,
N. Wiebe, K. B. Whaley and R. Babbush, Npj Quantum
Inf., 2021, 7, 23.

© 2022 The Author(s). Published by the Royal Society of Chemistry
Chem. Sci., 2022, 13, 8953–8962 | 8959

## Page 9

View Article Online

Chemical Science
Edge Article

20 S. Endo, J. Sun, Y. Li, S. C. Benjamin and X. Yuan, Phys. Rev.
Lett., 2020, 125, 010501.
21 S. Endo, Z. Cai, S. C. Benjamin and X. Yuan, J. Phys. Soc.
Jpn., 2021, 90, 032001.
22 C. Hempel, C. Maier, J. Romero, J. McClean, T. Monz,
H. Shen, P. Jurcevic, B. P. Lanyon, P. Love, R. Babbush,
A. Aspuru-Guzik, R. Blatt and C. F. Roos, Phys. Rev. X,
2018, 8, 031022.
23 X. Yuan, J. Sun, J. Liu, Q. Zhao and Y. Zhou, Phys. Rev. Lett.,
2021, 127, 040501.
24 K. Fujii, K. Mitarai, W. Mizukami and Y. O. Nakagawa, PRX
Quantum, 2022, 3, 010346.
25 X. Xu, J. Sun, S. Endo, Y. Li, S. C. Benjamin and X. Yuan, Sci.
Bull., 2021, 66, 2181–2188.
26 Y. Nam, J.-S. Chen, N. C. Pisenti, K. Wright, C. Delaney,
D. Maslov, K. R. Brown, S. Allen, J. M. Amini, J. Apisdorf,
et al., Npj Quantum Inf., 2020, 6, 1–6.
27 C. Cao, J. Hu, W. Zhang, X. Xu, D. Chen, F. Yu, J. Li, H. Hu,
D. Lv and M.-H. Yung, Phys. Rev. A, 2022, 105, 062452.
28 J.-N. Boyn, A. O. Lykhin, S. E. Smart, L. Gagliardi and
D. A. Mazziotti, J. Chem. Phys., 2021, 155, 244106.
29 S. E. Smart, J.-N. Boyn and D. A. Mazziotti, Phys. Rev. A,
2022, 105, 022405.
30 N. C. Rubin, K. Gunst, A. White, L. Freitag, K. Throssell,
G. K.-L. Chan, R. Babbush and T. Shiozaki, Quantum,
2021, 5, 568.
31 J. Lee, W. J. Huggins, M. Head-Gordon and K. B. Whaley, J.
Chem. Theory Comput., 2018, 15, 311–324.
32 H.
R.
Grimsley,
S.
E.
Economou,
E.
Barnes
and
N. J. Mayhall, Nat. Commun., 2019, 10, 3007.
33 H. L. Tang, V. Shkolnikov, G. S. Barron, H. R. Grimsley,
N. J. Mayhall, E. Barnes and S. E. Economou, PRX
Quantum, 2021, 2, 020310.
34 I. G. Ryabinkin, T.-C. Yen, S. N. Genin and A. F. Izmaylov, J.
Chem. Theory Comput., 2018, 14, 6317–6326.
35 I. G. Ryabinkin, R. A. Lang, S. N. Genin and A. F. Izmaylov, J.
Chem. Theory Comput., 2020, 16, 1055–1063.
36 Z.-J. Zhang, J. Sun, X. Yuan and M.-H. Yung, 2020,
arXiv:2011.05283.
37 M. Motta, E. Ye, J. R. McClean, Z. Li, A. J. Minnich, R. Babbush
and G. K.-L. Chan, npj Quantum Inf., 2021, 7, 1–7.
38 Y. Matsuzawa and Y. Kurashige, J. Chem. Theory Comput.,
2020, 16, 944–952.
39 J. S. Kottmann and A. Aspuru-Guzik, Phys. Rev. A, 2022, 105,
032449.
40 N. C. Rubin, J. Lee and R. Babbush, 2021, arXiv:2109.05010.
41 N.
V.
Tkachenko,
J.
Sud,
Y.
Zhang,
S.
Tretiak,
P. M. Anisimov, A. T. Arrasmith, P. J. Coles, L. Cincio and
P. A. Dub, PRX Quantum, 2021, 2, 020337.
42 A. Eddins, M. Motta, T. P. Gujarati, S. Bravyi, A. Mezzacapo,
C. Hadeld and S. Sheldon, PRX Quantum, 2022, 3, 010309.
43 Y. Zhang, L. Cincio, C. F. Negre, P. Czarnik, P. Coles,
P.
M.
Anisimov,
S.
M.
Mniszewski,
S.
Tretiak
and
P. A. Dub, 2021, arXiv:2106.07619.
44 A. Kumar, A. Asthana, C. Masteran, E. F. Valeev, Y. Zhang,
L. Cincio, S. Tretiak and P. A. Dub, 2022, arXiv:2201.09852.

45 T. Maier, M. Jarrell, T. Pruschke and M. H. Hettler, Rev.
Mod. Phys., 2005, 77, 1027.
46 Q. Sun and G. K.-L. Chan, Acc. Chem. Res., 2016, 49, 2705–
2712.
47 G. Kotliar, S. Y. Savrasov, K. Haule, V. S. Oudovenko,
O. Parcollet and C. A. Marianetti, Rev. Mod. Phys., 2006,
78, 865–951.
48 G. Knizia and G. K.-L. Chan, Phys. Rev. Lett., 2012, 109,
186404.
49 G. Knizia and G. K.-L. Chan, J. Chem. Theory Comput., 2013,
9, 1428–1432.
50 S. Wouters, C. A. Jim´enez-Hoyos, Q. Sun and G. K.-L. Chan,
J. Chem. Theory Comput., 2016, 12, 2706–2719.
51 N. C. Rubin, 2016, arXiv:1610.06910.
52 B. Bauer, D. Wecker, A. J. Millis, M. B. Hastings and
M. Troyer, Phys. Rev. X, 2016, 6, 031045.
53 I. Rungger, N. Fitzpatrick, H. Chen, C. H. Alderete, H. Apel,
A. Cowtan, A. Patterson, D. M. Ramo, Y. Zhu, N. H. Nguyen,
E. Grant, S. Chretien, L. Wossnig, N. M. Linke and
R. Duncan, 2020, arXiv:1910.04735.
54 H. Chen, M. Nusspickel, J. Tilly and G. H. Booth, Phys. Rev.
A, 2021, 104, 032405.
55 M. Rossmannek, P. K. Barkoutsos, P. J. Ollitrault and
I. Tavernelli, J. Chem. Phys., 2021, 154, 114105.
56 H. Ma, M. Govoni and G. Galli, npj Comput. Mater., 2020, 6, 85.
57 N. Sheng, C. Vorwerk, M. Govoni and G. Galli, Quantum
Simulations
of
Material
Properties
on
Quantum
Computers, 2021, arXiv:2105.04736.
58 R. Or´us, Nat. Rev. Phys., 2019, 1, 538–550.
59 J. Sun, S. Endo, H. Lin, P. Hayden, V. Vedral and X. Yuan,
2021, arXiv:2106.05938.
60 X. Wu, Z.-H. Cui, Y. Tong, M. Lindsey, G. K.-L. Chan and
L. Lin, J. Chem. Phys., 2019, 151, 064108.
61 Y. Kawashima, M. P. Coons, Y. Nam, E. Lloyd, S. Matsuura,
A.
J.
Garza,
S.
Johri,
L.
Huntington,
V.
Senicourt,
A. O. Maksymov, H. V. Nguyen Jason, Kim Jungsang,
Alidoust Nima, Zaribayan Arman and Yamazaki Takeshi,
Commun. Phys., 2021, 4, 245.
62 J. Tilly, P. V. Sriluckshmy, A. Patel, E. Fontana, I. Rungger,
E. Grant, R. Anderson, J. Tennyson and G. H. Booth, Phys.
Rev. Research, 2021, 3, 033230.
63 X. Wu, M. Lindsey, T. Zhou, Y. Tong and L. Lin, Phys. Rev. B,
2020, 102, 085123.
64 Z.-H. Cui, T. Zhu and G. K.-L. Chan, J. Chem. Theory
Comput., 2020, 16, 119–129.
65 E. Fertitta and G. H. Booth, J. Chem. Phys., 2019, 151,
014115.
66 X. Wen, D. S. Graham, D. V. Chulhai and J. D. Goodpaster, J.
Chem. Theory Comput., 2020, 16, 385–398.
67 C. Sun, U. Ray, Z.-H. Cui, M. Stoudenmire, M. Ferrero and
G. K.-L. Chan, Phys. Rev. B, 2020, 101, 075131.
68 Y. Fan, C. Cao, X. Xu, Z. Li, D. Lv and M.-H. Yung, 2021,
arXiv:2106.15210.
69 K. Kaiser, L. M. Scriven, F. Schulz, P. Gawel, L. Gross and
H. L. Anderson, Science, 2019, 365, 1299–1301.
70 W. Kutzelnigg, J. Chem. Phys., 1982, 77, 3081–3097.

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

This article is licensed under a

8960 | Chem. Sci., 2022, 13, 8953–8962
© 2022 The Author(s). Published by the Royal Society of Chemistry

## Page 10

View Article Online

Edge Article
Chemical Science

84 Z. Liu, T. Lu and Q. Chen, Carbon, 2020, 165, 468–475.
85 S. Arulmozhiraja and T. Ohno, J. Chem. Phys., 2008, 128,
114301.
86 J. M. L. Martin, J. El-Yazal and J.-P. François, Chem. Phys.
Lett., 1995, 242, 570–579.
87 K. Momma and F. Izumi, J. Appl. Crystallogr., 2011, 44,
1272–1276.
88 T. H. Dunning, J. Chem. Phys., 1989, 90, 1007–1023.
89 M.
S.
ANIS,
Abby-Mitchell,
H.
Abraham,
AduOﬀei,
R. Agarwal, G. Agliardi, M. Aharoni, I. Y. Akhalwaya,
G. Aleksandrowicz, T. Alexander, M. Amy, S. Anagolum,
Anthony-Gandon,
E.
Arbel,
A.
Asfaw,
A.
Athalye,
A.
Avkhadiev,
C.
Azaustre,
P.
BHOLE,
A.
Banerjee,
S.
Banerjee,
W.
Bang,
A.
Bansal,
P.
Barkoutsos,
A. Barnawal, G. Barron, G. S. Barron, L. Bello, Y. Ben-Haim,
M. C. Bennett, D. Bevenius, D. Bhatnagar, A. Bhobe,
P.
Bianchini,
L.
S.
Bishop,
C.
Blank,
S.
Bolos,
S. Bopardikar, S. Bosch, S. Brandhofer, Brandon, S. Bravyi,
N. Bronn, Bryce-Fuller, D. Bucher, A. Burov, F. Cabrera,
P.
Calpin,
L.
Capelluto,
J.
Carballo,
G.
Carrascal,
A. Carriker, I. Carvalho, A. Chen, C.-F. Chen, E. Chen,
J.
C.
Chen,
R.
Chen,
F.
Chevallier,
K.
Chinda,
R. Cholarajan, J. M. Chow, S. Churchill, CisterMoke,
C. Claus, C. Clauss, C. Clothier, R. Cocking, R. Cocuzzo,
J. Connor, F. Correa, Z. Crockett, A. J. Cross, A. W. Cross,
S. Cross, J. Cruz-Benito, C. Culver, A. D. C´orcoles-Gonzales,
N. D., S. Dague, T. E. Dandachi, A. N. Dangwal, J. Daniel,
M.
Daniels,
M.
Dartiailh,
A. R.
Davila, F.
Debouni,
A. Dekusar, A. Deshmukh, M. Deshpande, D. Ding, J. Doi,
E. M. Dow, E. Drechsler, E. Dumitrescu, K. Dumon,
I. Duran, K. EL-Say, E. Eastman, G. Eberle, A. Ebrahimi,
P. Eendebak, D. Egger, ElePT, Emilio, A. Espiricueta,
M. Everitt, D. Facoetti, Farida, P. M. Fern´andez, S. Ferracin,
D. Ferrari, A. H. Ferrera, R. Fouilland, A. Frisch, A. Fuhrer,
B. Fuller, M. GEORGE, J. Gacon, B. G. Gago, C. Gambella,
J. M. Gambetta, A. Gammanpila, L. Garcia, T. Garg,
S. Garion, J. R. Garrison, J. Garrison, T. Gates, L. Gil,
A. Gilliam, A. Giridharan, J. Gomez-Mosquera, Gonzalo,
S.
de
la
Puente
Gonz´alez,
J.
Gorzinski,
I.
Gould,
D. Greenberg, D. Grinko, W. Guan, D. Guijo, J. A. Gunnels,
H. Gupta, N. Gupta, J. M. G¨unther, M. Haglund, I. Haide,
I. Hamamura, O. C. Hamido, F. Harkins, K. Hartman,
A. Hasan, V. Havlicek, J. Hellmers, Ł. Herok, S. Hillmich,
H.
Horii,
C.
Howington,
S.
Hu,
W.
Hu,
J.
Huang,
R. Huisman, H. Imai, T. Imamichi, K. Ishizaki, Ishwor,
R. Iten, T. Itoko, A. Ivrii, A. Javadi, A. Javadi-Abhari,
W. Javed, Q. Jianhua, M. Jivrajani, K. Johns, S. Johnstun,
Jonathan-Shoemaker, JosDenmark, JoshDumo, J. Judge,
T. Kachmann, A. Kale, N. Kanazawa, J. Kane, Kang-Bae,
A. Kapila, A. Karazeev, P. Kassebaum, T. Kehrer, J. Kelso,
S. Kelso, V. Khanderao, S. King, Y. Kobayashi, Kovi11Day,
A. Kovyrshin, R. Krishnakumar, V. Krishnan, K. Krsulich,
P. Kumkar, G. Kus, R. LaRose, E. Lacal, R. Lambert,
H. Landa, J. Lapeyre, J. Latone, S. Lawrence, C. Lee, G. Li,
J. Lishman, D. Liu, P. Liu, Lolcroc, A. K. M., L. Madden,
Y. Maeng, S. Maheshkar, K. Majmudar, A. Malyshev,
M.
E.
Mandouh,
J.
Manela,
Manjula,
J.
Marecek,

71 R. J. Bartlett, S. A. Kucharski and J. Noga, Chem. Phys. Lett.,
1989, 155, 133–140.
72 A. G. Taube and R. J. Bartlett, Int. J. Quantum Chem., 2006,
106, 3393–3401.
73 J. Hachmann, W. Cardoen and G. K.-L. Chan, J. Chem. Phys.,
2006, 125, 144101.
74 M. Motta, D. M. Ceperley, G. K.-L. Chan, J. A. Gomez, E. Gull,
S. Guo, C. A. Jim´enez-Hoyos, T. N. Lan, J. Li, F. Ma, A. J. Millis,
N.
V.
Prokof’ev,
U.
Ray,
G.
E.
Scuseria,
S.
Sorella,
E. M. Stoudenmire, Q. Sun, I. S. Tupitsyn, S. R. White,
D. Zgid and S. Zhang, Phys. Rev. X, 2017, 7, 031059.
75 Q. Sun, X. Zhang, S. Banerjee, P. Bao, M. Barbry, N. S. Blunt,
N. A. Bogdanov, G. H. Booth, J. Chen, Z.-H. Cui, J. J. Eriksen,
Y. Gao, S. Guo, J. Hermann, M. R. Hermes, K. Koh, P. Koval,
S. Lehtola, Z. Li, J. Liu, N. Mardirossian, J. D. McClain,
M.
Motta,
B.
Mussard,
H.
Q.
Pham,
A.
Pulkin,
W. Purwanto, P. J. Robinson, E. Ronca, E. R. Sayfutyarova,
M. Scheurer, H. F. Schurkus, J. E. T. Smith, C. Sun,
S.-N. Sun, S. Upadhyay, L. K. Wagner, X. Wang, A. White,
J. D. Whiteld, M. J. Williamson, S. Wouters, J. Yang,
J.
M.
Yu,
T.
Zhu,
T.
C.
Berkelbach,
S.
Sharma,
A. Y. Sokolov and G. K.-L. Chan, J. Chem. Phys., 2020, 153,
024109.
76 N. S. Kumar, E. M. Dullaghan, B. B. Finlay, H. Gong,
N.
E.
Reiner,
J.
Jon
Paul
Selvam,
L.
M.
Thorson,
S. Campbell, N. Vitko, A. R. Richardson, R. Zoraghi and
R. N. Young, Bioorg. Med. Chem., 2014, 22, 1708–1725.
77 Y. Liang, Z. Chen, Y. Jing, Y. Rong, A. Facchetti and Y. Yao, J.
Am. Chem. Soc., 2015, 137, 4956–4959.
78 W. Stawski, K. Hurej, J. Skonieczny and M. Pawlicki, Angew.
Chem., Int. Ed., 2019, 58, 10946–10950.
79 K. Fukui, Acc. Chem. Res., 1981, 14, 363–368.
80 M. J. Frisch, G. W. Trucks, H. B. Schlegel, G. E. Scuseria,
M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone,
G.
A.
Petersson,
H.
Nakatsuji,
X.
Li,
M.
Caricato,
A. V. Marenich, J. Bloino, B. G. Janesko, R. Gomperts,
B. Mennucci, H. P. Hratchian, J. V. Ortiz, A. F. Izmaylov,
J.
L.
Sonnenberg,
D.
Williams-Young,
F.
Ding,
F. Lipparini, F. Egidi, J. Goings, B. Peng, A. Petrone,
T. Henderson, D. Ranasinghe, V. G. Zakrzewski, J. Gao,
N. Rega, G. Zheng, W. Liang, M. Hada, M. Ehara,
K.
Toyota,
R.
Fukuda,
J.
Hasegawa,
M.
Ishida,
T. Nakajima, Y. Honda, O. Kitao, H. Nakai, T. Vreven,
K.
Throssell,
J.
A.
Jr.,
J.
E.
Peralta,
F.
Ogliaro,
M. J. Bearpark, J. J. Heyd, E. N. Brothers, K. N. Kudin,
V. N. Staroverov, T. A. Keith, R. Kobayashi, J. Normand,
K. Raghavachari, A. P. Rendell, J. C. Burant, S. S. Iyengar,
J. Tomasi, M. Cossi, J. M. Millam, M. Klene, C. Adamo,
R. Cammi, J. W. Ochterski, R. L. Martin, K. Morokuma,
O. Farkas, J. B. Foresman, and D. J. Fox, Gaussian09,
revision E.01, Gaussian Inc., Wallingford CT, 2016.
81 L. Zhang, H. Li, Y. P. Feng and L. Shen, J. Phys. Chem. Lett.,
2020, 11, 2611–2617.
82 A. E. Raeber and D. A. Mazziotti, Phys. Chem. Chem. Phys.,
2020, 22, 23998–24003.
83 N. Fedik, M. Kulichenko, D. Steglenko and A. I. Boldyrev,
Chem. Commun., 2020, 56, 2711–2714.

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

This article is licensed under a

© 2022 The Author(s). Published by the Royal Society of Chemistry
Chem. Sci., 2022, 13, 8953–8962 | 8961

## Page 11

View Article Online

Chemical Science
Edge Article

jliu45, jscott2, klinvill, krutik2966, ma5x, michelle4654,
msuwama, nico lgrs, ntgiwsvp, ordmoj, sagar pahwa,
pritamsinha2304, ryancocuzzo, saktar unr, saswati qiskit,
septembrr,
sethmerkel,
sg495,
shaashwat,
smturro2,
sternparky, strickroman, tigerjack, tsura crisaldo, upsideon,
vadebayo49,
welien,
willhbang,
wmurphy
collabstar,
yang.luh and M. Cepulkovskis, Qiskit: An Open-source
Framework for Quantum Computing, 2021.
90 R. LaRose, A. Mari, S. Kaiser, P. J. Karalekas, A. A. Alves,
P. Czarnik, M. E. Mandouh, M. H. Gordon, Y. Hindy,
A. Robertson, P. Thakre, N. Shammah and W. J. Zeng,
2021, arXiv:2009.04417.
91 M. Welborn, T. Tsuchimochi and T. Van Voorhis, J. Chem.
Phys., 2016, 145, 074102.
92 H.-Z. Ye, N. D. Ricke, H. K. Tran and T. Van Voorhis, J.
Chem. Theory Comput., 2019, 15, 4497–4506.
93 H.-Z. Ye, H. K. Tran and T. Van Voorhis, J. Chem. Theory
Comput., 2020, 16, 5035–5046.
94 S. McArdle, T. Jones, S. Endo, Y. Li, S. C. Benjamin and
X. Yuan, npj Quantum Inf., 2019, 5, 75.
95 X. Yuan, S. Endo, Q. Zhao, Y. Li and S. C. Benjamin,
Quantum, 2019, 3, 191.
96 H. Nishi, T. Kosugi and Y.-i. Matsushita, npj Quantum Inf.,
2021, 7, 85.
97 M. Motta, C. Sun, A. T. Tan, M. J. O'Rourke, E. Ye,
A. J. Minnich, F. G. Brand˜ao and G. K.-L. Chan, Nat. Phys.,
2020, 16, 205–210.
98 M. Huo and Y. Li, Shallow Trotter circuits full error-
resilient quantum simulation of imaginary time 2021,
arXiv:2109.07807.
99 P. Zeng, J. Sun and X. Yuan, 2021.
100 K. Temme, S. Bravyi and J. M. Gambetta, Phys. Rev. Lett.,
2017, 119, 180509.
101 S. Endo, S. C. Benjamin and Y. Li, Phys. Rev. X, 2018, 8,
031027.
102 A. Strikis, D. Qin, Y. Chen, S. C. Benjamin and Y. Li, PRX
Quantum, 2021, 2, 040330.
103 J. Sun, X. Yuan, T. Tsunoda, V. Vedral, S. C. Benjamin and
S. Endo, Phys. Rev. Appl., 2021, 15, 034026.
104 S. Bravyi, S. Sheldon, A. Kandala, D. C. Mckay and
J. M. Gambetta, Phys. Rev. A, 2021, 103, 042605.
105 Y. Kim, C. J. Wood, T. J. Yoder, S. T. Merkel, J. M. Gambetta,
K. Temme and A. Kandala, 2021, arXiv:2108.09197.
106 H.-Y. Huang, R. Kueng and J. Preskill, Phys. Rev. Lett., 2021,
127, 030503.
107 B.
Wu,
J.
Sun,
Q.
Huang
and
X.
Yuan,
2021,
arXiv:2105.13091.
108 T. Zhang, J. Sun, X.-X. Fang, X. Zhang, X. Yuan and H. Lu,
Phys. Rev. Lett., 2021, 127, 200501.
109 J. M. Montgomery and D. A. Mazziotti, J. Phys. Chem. A,
2018, 122, 4988–4996.
110 Z. Li, S. Guo, Q. Sun and G. K.-L. Chan, Nat. Chem., 2019,
11, 1026–1033.

M.
Marques,
K.
Marwaha,
D.
Maslov,
P.
Maszota,
D.
Mathews,
A.
Matsuo,
F.
Mazhandu,
D.
McClure,
M. McElaney, C. McGarry, D. McKay, D. McPherson,
S.
Meesala,
D.
Meirom,
C.
Mendell,
T.
Metcalfe,
M. Mevissen, A. Meyer, A. Mezzacapo, R. Midha, D. Miller,
Z. Minev, A. Mitchell, N. Moll, A. Montanez, G. Monteiro,
M. D. Mooring, R. Morales, N. Moran, D. Morcuende,
S. Mostafa, M. Motta, R. Moyard, P. Murali, J. M¨uggenburg,
T. NEMOZ, D. Nadlinger, K. Nakanishi, G. Nannicini,
P. Nation, E. Navarro, Y. Naveh, S. W. Neagle, P. Neuweiler,
A.
Ngoueya,
T.
Nguyen,
J.
Nicander,
Nick-Singstock,
P.
Niroula,
H.
Norlen,
NuoWenLei,
L.
J.
O'Riordan,
O. Ogunbayo, P. Ollitrault, T. Onodera, R. Otaolea, S. Oud,
D.
Padilha,
H.
Paik,
S.
Pal,
Y. Pang,
A.
Panigrahi,
V. R. Pascuzzi, S. Perriello, E. Peterson, A. Phan, K. Pilch,
F. Piro, M. Pistoia, C. Piveteau, J. Plewa, P. Pocreau,
A. Pozas-Kerstjens, R. Pracht, M. Prokop, V. Prutyanov,
S.
Puri,
D.
Puzzuoli,
J.
P´erez,
Quant02,
Quintiii,
R. I. Rahman, A. Raja, R. Rajeev, I. Rajput, N. Ramagiri,
A. Rao, R. Raymond, O. Reardon-Smith, R. M.-C. Redondo,
M. Reuter, J. Rice, M. Riedemann, Rietesh, D. Risinger,
M. L. Rocca, D. M. Rodr´ıguez, RohithKarur, B. Rosand,
M. Rossmannek, M. Ryu, T. SAPV, N. R. C. Sa, A. Saha,
A. Ash-Saki,
S.
Sanand,
M.
Sandberg,
H.
Sandesara,
R. Sapra, H. Sargsyan, A. Sarkar, N. Sathaye, B. Schmitt,
C. Schnabel, Z. Schoenfeld, T. L. Scholten, E. Schoute,
M.
Schulterbrandt,
J.
Schwarm,
J.
Seaward,
Sergi,
I. F. Sertage, K. Setia, F. Shah, N. Shammah, R. Sharma,
Y. Shi, J. Shoemaker, A. Silva, A. Simonetto, D. Singh,
D. Singh, P. Singh, P. Singkanipa, Y. Siraichi, Siri, J. Sistos,
I. Sitdikov, S. Sivarajah, M. B. Sleterding, J. A. Smolin,
M. Soeken, I. O. Sokolov, I. Sokolov, V. P. Soloviev,
SooluThomas,
Starsh,
D.
Steenken,
M.
Stypulkoski,
A. Suau, S. Sun, K. J. Sung, M. Suwama, O. Słowik,
H.
Takahashi,
T.
Takawale,
I.
Tavernelli,
C.
Taylor,
P. Taylour, S. Thomas, K. Tian, M. Tillet, M. Tod,
M. Tomasik, C. Tornow, E. de la Torre, J. L. S. Toural,
K. Trabing, M. Treinish, D. Trenev, TrishaPe, F. Truger,
G. Tsilimigkounakis, D. Tulsi, W. Turner, Y. Vaknin,
C. R. Valcarce, F. Varchon, A. Vartak, A. C. Vazquez,
P. Vijaywargiya, V. Villar, B. Vishnu, D. Vogt-Lee, C. Vuillot,
J. Weaver, J. Weidenfeller, R. Wieczorek, J. A. Wildstrom,
J.
Wilson,
E.
Winston,
WinterSoldier,
J.
J.
Woehr,
S. Woerner, R. Woo, C. J. Wood, R. Wood, S. Wood,
J. Wootton, M. Wright, L. Xing, J. YU, B. Yang, U. Yang,
J.
Yao,
D.
Yeralin,
R.
Yonekura,
D.
Yonge-Mallo,
R. Yoshida, R. Young, J. Yu, L. Yu, C. Zachow, L. Zdanski,
H. Zhang, I. Zidaru, C. Zoufal, aeddins ibm, alexzhang13,
b63,
bartek
bartlomiej,
bcamorrison,
brandhsn,
charmerDark,
deeplokhande,
dekel.meirom,
dime10,
dlasecki,
ehchen,
fanizzamarco,
fs1132429,
gadial,
galeinston,
georgezhou20,
georgios
ts,
gruu,
hhorii,
hykavitha, itoko, jeppevinkel, jessica angel7, jezerjojo14,

Creative Commons Attribution-NonCommercial 3.0 Unported Licence.

Open Access Article. Published on 11 July 2022. Downloaded on 4/12/2026 4:19:28 AM.

This article is licensed under a

8962 | Chem. Sci., 2022, 13, 8953–8962
© 2022 The Author(s). Published by the Royal Society of Chemistry
