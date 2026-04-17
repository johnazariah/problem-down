---
source_pdf: ../arxiv_1704.05018.pdf
pages: 24
extracted_at: 2026-04-17T12:32:30+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_1704.05018

Source PDF: ../arxiv_1704.05018.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Hardware-eﬃcient Variational Quantum Eigensolver for Small Molecules and
Quantum Magnets

Abhinav Kandala,∗Antonio Mezzacapo,∗Kristan Temme,
Maika Takita, Markus Brink, Jerry M. Chow, and Jay M. Gambetta
IBM T.J. Watson Research Center, Yorktown Heights, NY 10598, USA
(Dated: October 16, 2017)

Quantum computers can be used to address
molecular structure, materials science and con-
densed matter physics problems, which currently
stretch the limits of existing high-performance
computing resources [1]. Finding exact numerical
solutions to these interacting fermion problems
has exponential cost, while Monte Carlo methods
are plagued by the fermionic sign problem. These
limitations of classical computational methods
have made even few-atom molecular structures
problems of practical interest for medium-sized
quantum
computers.
Yet,
thus
far
experi-
mental implementations have been restricted to
molecules involving only Period I elements
[2–
8].
Here, we demonstrate the experimental op-
timization of up to six-qubit Hamiltonian prob-
lems with over a hundred Pauli terms, determin-
ing the ground state energy for molecules of in-
creasing size, up to BeH2.
This is enabled by
a hardware-eﬃcient variational quantum eigen-
solver with trial states speciﬁcally tailored to
the available interactions in our quantum pro-
cessor, combined with a compact encoding of
fermionic Hamiltonians [9] and a robust stochas-
tic optimization routine [10]. We further demon-
strate the ﬂexibility of our approach by apply-
ing the technique to a problem of quantum mag-
netism [11].
Across all studied problems, we
ﬁnd agreement between experiment and numeri-
cal simulations with a noisy model of the device.
These results help elucidate the requirements for
scaling the method to larger systems, and aim at
bridging the gap between problems at the fore-
front of high-performance computing and their
implementation on quantum hardware.
The fundamental goal of addressing molecular struc-
ture problems is to solve for the ground state energy of
many-body interacting fermionic Hamiltonians. Solving
this problem on a quantum computer relies on a mapping
between fermionic and qubit operators [12]. This restates
it as a speciﬁc instance of a local Hamiltonian problem
on a set of qubits. Given a k-local Hamiltonian H, com-
posed of terms that act on at most k qubits, the solution
to the local Hamiltonian problem amounts to ﬁnding its

arXiv:1704.05018v2 [quant-ph] 13 Oct 2017

∗These authors contributed equally to this work.

smallest eigenvalue EG,

H| Φ⟩= EG| Φ⟩.
(1)

To date, no eﬃcient algorithm is known that can solve
this problem in full generality. For k ≥2 the problem is
known to be QMA-complete [13]. However, it is expected
that physical systems have Hamiltonians that do not con-
stitute hard instances of this problem, and can be solved
eﬃciently on a quantum computer, while remaining hard
to solve classically.
Following Feynman’s idea for quantum simulation,
a quantum algorithm for the ground state problem
of interacting fermions was proposed in [14] and [15].
The approach relies on a good initial state that has
a large overlap with the ground state and then solves
the problem using the quantum phase estimation algo-
rithm (PEA) [16]. While PEA has been demonstrated to
achieve extremely accurate energy estimates for quantum
chemistry [2, 3, 5, 8], it applies stringent requirements on
quantum coherence.
An alternative approach is the use of quantum op-
timizers.
Their utility spans from combinatorial opti-
mization problems [17, 18] to quantum chemistry in the
form of variational quantum eigensolvers (VQEs), where
they were introduced to reduce coherence requirements
on quantum hardware [4, 19, 20]. The VQE uses Ritz’s
variational principle to prepare approximations to the
ground state and its energy. In this approach, the quan-
tum computer is used to prepare variational trial states
that depend on a set of parameters. Then, the expec-
tation value of the energy is estimated and used by a
classical optimizer to generate a new set of improved pa-
rameters. The advantage of VQE over classical simula-
tion methods is that is can prepare trial states that are
not amenable to eﬃcient classical numerics.
To date, the VQE approach realized in experiment has
been limited by diﬀerent factors.
Typically, one con-
siders a unitary coupled cluster (UCC) ansatz for the
trial state [6, 7], which has a number of parameters that
scale quartically with the number of spin-orbitals con-
sidered, in the single and double excitation approxima-
tion. Furthermore, when implementing the UCC ansatz
on a quantum computer, one has to account for Trot-
terization errors [20–22]. In this work, we introduce and
implement a “hardware-eﬃcient” ansatz preparation for
VQE, where trial states are parameterized by quantum
gates that are tailored to the physical device available.
We numerically show the viability of such trial states for

## Page 2

FIG. 1.
Quantum chemistry on a superconducting quantum processor:
device and quantum circuit for
variational trial state preparation. Solving molecular structure problems on a quantum computer relies on mappings
between fermionic and qubit operators. a Parity mapping of 8 spin orbitals (drawn in blue and red, not to scale) onto 8 qubits,
reduced to 6 qubits via qubit tapering of fermionic spin-parity symmetries. The bars indicate the parity of the spin-orbitals
encoded in each qubit. b False colored optical micrograph of the superconducting quantum processor. The transmon qubits
are coupled via two CPW resonators, highlighted in blue, and have individual CPW resonators for control and readout. c
Hardware-eﬃcient quantum circuit for trial state preparation and energy estimation, shown here for 6 qubits. The circuit is
composed of a sequence of interleaved single-qubit rotations, and entangling unitary operations UENT that entangle all the
qubits in the circuit. A ﬁnal set of post-rotations prior to qubit readout are used to measure the expectation values of the terms
in the qubit Hamiltonian, and estimate the energy of the trial state. d An example of the pulse sequence for the preparation
of a six qubit trial state, where UENT is implemented as a sequence of two-qubit cross resonance gates.

small molecular structure problems and use a supercon-
ducting quantum processor to perform optimizations of
the molecular energies of H2, LiH and BeH2, and extend
its application to a Heisenberg antiferromagnetic model
in an external magnetic ﬁeld.
The device used in the experiments is a superconduct-
ing quantum processor with six ﬁxed-frequency transmon
qubits, together with a central weakly-tunable asymmet-
ric transmon qubit [23]. The device is cooled down in
a dilution refrigerator, thermally anchored to its mixing
chamber plate at 25 mK. The experiments discussed here
make use of six of these qubits (labeled Q1-6), highlighted
in Fig. 1b. The qubits are coupled via two superconduct-
ing coplanar waveguide (CPW) resonators that serve as
quantum buses, and can be individually controlled and
read out through independent readout resonators.
The hardware-eﬃcient trial states we consider use the
naturally available entangling interactions of the super-
conducting hardware, described by a drift Hamiltonian
H0 that generates the entanglers UENT = exp(−iH0τ)
which entangle all the qubits in the circuit. These are

interleaved with arbitrary single-qubit Euler rotations
which are implemented as a combination of Z and X
gates, given by U q,i(⃗θ) = Zq
θq,i
1 Xq
θq,i
2 Zq
θq,i
3 , where q identi-
ﬁes the qubit and i = 0, 1, ...d refers to the depth posi-
tion, as depicted in Fig. 1c. The N-qubit trial states are
obtained from the state | 00 . . . 0⟩, applying d entanglers
UENT that alternate with N Euler rotations, giving

N
Y

N
Y

h
U q,d(⃗θ)
i
× UENT ×

h
U q,d−1(⃗θ)
i

| Φ(⃗θ)⟩=

q=1

q=1

N
Y

h
U q,0(⃗θ)
i
| 00...0⟩.
(2)

· · · × UENT ×

q=1

Since the qubits are all initialized in their ground state
| 0⟩, the ﬁrst set of Z rotations of U q,0(⃗θ) is not imple-
mented, resulting in a total of p = N(3d + 2) indepen-
dent angles.
In the experiment, the evolution time τ
and the individual couplings in H0 can be controlled.

## Page 3

qubit Qt. Hamiltonian tomography of the CRc−t gates
is used to reveal the strengths of the various interaction
terms, and the gate time for maximal entanglement [24].
We set our two-qubit gate times at 150 ns, simultaneously
trying to minimize the eﬀect of decoherence without com-
promising the accuracy of the optimization outcome, see
Supplementary Information.
After each trial state is prepared, we estimate the asso-
ciated energy by measuring the expectation values of the
individual Pauli terms in the Hamiltonian. These esti-
mates are aﬀected by stochastic ﬂuctuations due to ﬁnite
sampling. Diﬀerent post-rotations are applied after trial
state preparation for sampling diﬀerent Pauli operators,
see Fig. 1c,d. We group the Pauli operators into tensor
product basis sets that require the same post-rotations.
We numerically show that such grouping reduces the en-
ergy ﬂuctuations, keeping the same total number of sam-
ples, thereby reducing the time overhead for energy esti-
mation, see Supplementary Information. The energy esti-
mates are then used by a gradient descent algorithm that
relies on a simultaneous perturbation stochastic approx-
imation (SPSA) to update the control parameters. The
SPSA algorithm approximates the gradient using only
two energy measurements, regardless of the dimensions
of the parameter space p, achieving a level of accuracy
comparable to standard gradient descent methods, in the
presence of stochastic ﬂuctuations [10]. This is a crucial
aspect for optimizing over many qubits and long depths
for trial state preparation, allowing us to optimize over a
number of parameters as large as p = 30.
To address molecular problems on our quantum pro-
cessor, we rely on a compact encoding of the second-
quantized fermionic Hamiltonians on to qubits.
The
H2 molecular Hamiltonian has 4 spin-orbitals, represent-
ing the spin-degenerate 1s orbitals of the two Hydrogen
atoms. We use a binary tree encoding [12] to map it to
a 4 qubit system, and remove two qubits associated with
the spin-parities of the system [9]. The BeH2 Hamilto-
nian is deﬁned upon the 1s, 2s, 2px orbitals associated
to Be, and 1s orbital associated to each H atom, for a
total of 10 spin orbitals. We then assume perfect ﬁlling
of the two innermost 1s spin-orbitals of Be, after dressing
them via the diagonalization of the non-interacting part
of the fermionic Hamiltonian. We map the 8 spin-orbital
Hamiltonian of BeH2 spin-orbital Hamiltonian using the
parity mapping, and remove, as in the case of H2, two
qubits associated to the spin-parity symmetries, reducing
this to a 6 qubit problem that encodes 8 spin-orbitals. A
similar approach is also used to map LiH onto 4 qubits.
The Hamiltonians for H2, LiH and BeH2 at their equilib-
rium distance are explicitly given in the Supplementary
Information.
The results from an optimization procedure are illus-
trated in detail in Fig. 2, using the BeH2 Hamiltonian for
the interatomic distance of 1.7

FIG. 2.
Experimental implementation of six-qubit
optimization. Energy minimization for the six-qubit Hamil-
tonian describing BeH2 at interatomic distance l = 1.7
◦A,
plotted against the exact value (black dashed line). For each
iteration k, the gradient at each control ⃗θk is approximated
using 103 samples for energy estimations at ⃗θ+
k and ⃗θ−
k , shown
in blue and red, respectively. The inset shows the simultane-
ous optimization of 30 Euler angles that control the trial state
preparation. Each color refers to a particular qubit, following
the qubit color scheme of Fig. 1. The ﬁnal energy estimate
(green dashed line) is obtained using the angles
⃗
θﬁnal, aver-
aged over the last 25 angle updates, in order to mitigate the
eﬀect of stochastic ﬂuctuations, with a higher number of 105

samples, to get a more accurate energy estimation.

However, numerical simulations indicate that accurate
optimizations are obtained for ﬁxed-phase UENT, leav-
ing the p control angles as variational parameters . Our
hardware-eﬃcient approach does not rely on the accu-
rate implementation of speciﬁc two qubit gates and can
be used with any UENT that generates suﬃcient entan-
glement.
This is in contrast to UCC trial states that
require high-ﬁdelity quantum gates approximating a uni-
tary operator tailored on a theoretical ansatz. For the
experiments considered here, the entanglers UENT are
composed of a sequence of two-qubit cross-resonance
(CR) gates [24].Simulations as a function of entangler
phase show plateaus of minimal energy error around gate
phases corresponding to the maximal pairwise concur-
rence, see Supplementary Information. We therefore set
the entangler evolution time τ at the beginning of such
plateaus, in order to reduce decoherence eﬀects.
In our experiments, the Z rotations are implemented as
frame changes in the control software [25], while the X ro-
tations are implemented by appropriately scaling the am-
plitude of calibrated Xπ pulses, using a ﬁxed total time of
100 ns for every single-qubit rotation. The CRc−t gates
that compose UENT are implemented by driving a control
qubit Qc with a microwave pulse resonant with a target

◦A. It is important to note
that while using a large number of entanglers UENT helps
achieve better energy estimates in the absence of noise,
the combined eﬀect of decoherence and ﬁnite sampling

## Page 4

FIG. 3.
Application to quantum chemistry: Potential energy surfaces
Experimental results (black circles), exact
energy surfaces (dotted lines) and density plots of outcomes from numerical simulations, for a number of interatomic distances
for a, H2 b, LiH, and c, BeH2. The experimental and numerical results presented here use depth d = 1 circuits. The error bars
on the experimental data are smaller than the size of the markers. The density plots are obtained from 100 numerical outcomes
at each interatomic distance. The top insets of each ﬁgure highlight the qubits used for the experiment, and the cross-resonance
gates that constitute UENT. The bottom insets of each ﬁgure are representations of the molecular geometry, not drawn to scale.
For all the three molecules, the deviation of the experimental results from the exact curves, is well explained by the stochastic
simulations.

sets the optimal depth for optimizations on our quantum
hardware to 0 −2 entanglers. The results presented in
Fig. 2 are obtained using a depth d = 1 circuit, with a
total of 30 Euler control angles associated with 6 qubits.
The inset of Fig. 2 shows the simultaneous perturbation
of 30 Euler angles, as the energy estimates are updated.
To obtain the potential energy surfaces for H2, LiH,
and BeH2, we search for the ground state energy of their
molecular Hamiltonians, using 2, 4, and 6 qubits respec-
tively, for depth d = 1, for a range of diﬀerent inter-
atomic distances. The experimental results are compared
with the ground state energies obtained from exact di-
agonalization and outcomes from numerical simulations
in Fig. 3. The colored density plots in each panel are
obtained from 100 numerical optimizations for each in-
teratomic distance, using CR entangling gates on the
same topology as the experiments. These numerics ac-
count for decoherence eﬀects, simulated by adding am-
plitude damping and dephasing channels after each layer
of quantum gates. The impact of ﬁnite sampling on the
optimization algorithm is taken into account by numer-
ically sampling the individual Pauli terms in the Hamil-
tonian, and adding their averages. The strengths of the
noise channels are derived from the measured values for
T1, T ∗
2 coherence times.
In addition to the eﬀects of
decoherence and noisy energy estimates, the deviations
are also due to low circuit depth for trial state prepara-
tion, which, for example, explains the kink in the range
l = 2.5 −3

ond order for a 8-orbital molecule such as our model
of BeH2 would require 4160 fermionic variational terms,
which, after accounting for fermionic mappings and Trot-
terization would generate a number of quantum gates of
the same order. The scaling of resources and noise re-
quirements to achieve chemical accuracy using hardware-
eﬃcient trial states are detailed in the Supplementary In-
formation. We emphasize that our approach is unaﬀected
by coherent gate errors, which shifts the focus to the re-
duction of incoherent errors, favoring our ﬁxed-frequency,
all-microwave control, qubit architecture. Furthermore,
the eﬀect of incoherent errors can be mitigated as recently
proposed [26–28], without requiring additional quantum
resources.
We now demonstrate the applicability of our technique
to a problem of quantum magnetism, and show that with
the same noisy quantum hardware, the advantage of us-
ing higher circuits depths is crucially dependent on the
target Hamiltonian. Speciﬁcally, we consider a four qubit
Heisenberg model on a square lattice, in the presence of
an external magnetic ﬁeld. The model is described by the
Hamiltonian H = J P

⟨ij⟩(XiXj+YiYj+ZiZj)+B P

i Zi,
where ⟨ij⟩indicates the nearest neighbor pairs, J is the
strength of the spin-spin interaction, and B the magnetic
ﬁeld along the Z-direction. We utilize our technique to
solve for the ground state energy of the system for a
range of J/B values.
When J = 0, the ground state
is completely separable, and the best estimates are ob-
tained for depth d =0. As J is increased, the ground
state is increasingly entangled, and the best estimates
are instead obtained at d = 2, despite the increased de-
coherence caused by using two entanglers for trial state
preparation. This is shown in Fig. 4a for J/B = 1. The
experimental results are compared with the exact ground

◦A, in Fig. 3b. In the absence of noise, criti-
cal depths of d = 1, 8, 28(1, 6, 16) are required to achieve
chemical accuracy (approx. 0.0016 Hartree), on the cur-
rent experimental (all-to-all) connectivities for H2, LiH
and BeH2, respectively, see Supplementary Information.
In contrast, a generic UCC ansatz truncated to the sec-

## Page 5

perconducting quantum processor is capable of address-
ing molecular problems beyond period 1 elements, up
to BeH2.
A numerical analysis for the hardware re-
quirements to improve the accuracy of a VQE for the
molecules addressed suggest the need for dramatic im-
provements in coherence and sampling, see Supplemen-
tary Information. For more complex problems, increased
coherence and faster gates would enable longer circuit
depths for state preparation while an increased on-chip
qubit connectivity is crucial for reducing critical depth
requirements.The use of fast reset schemes [29] would en-
able increased sampling rates, improving the eﬀectiveness
of the classical optimizer, while reducing time overheads.
The performance of the quantum-classical feedback loop
could be further improved by variants [30] of the simul-
taneous perturbation protocol discussed here. Trial state
preparation circuits, combining better ansatzes from clas-
sical approximate methods and hardware-eﬃcient gates,
can be further investigated to improve on the current
ansatzes. Finally, in the absence of a fault tolerant ar-
chitechture, the agreement of our experimental results
with the noise models considered opens a path to error
mitigation protocols for experimentally accessible circuit
depths [26–28].
Supplementary Information is available in the on-
line version of the paper.
Acknowledgments We thank J. Chavez-Garcia, A.
D. Corcoles and J. Rozen for experimental contributions;
J. Hertzberg and S. Rosenblatt for room temperature
characterization; B. Abdo for providing the Jospehson
Parametric Converters; S. Brayvi, J. Smolin, E. Mage-
san, L. Bishop, S. Sheldon, N. Moll, P. Barkoutsos, and
I. Tavernelli for valuable discussions; W. Shanks for assis-
tance with the experimental control software. We thank
A. D. Corcoles for edits to the manuscript. We acknowl-
edge support from the IBM Research Frontiers Institute.
We acknowledge support from IARPA under contract
W911NF-10-1-0324 for device fabrication.
Author contributions A.K. and A.M. contributed
equally to this work. J.M.G and K.T designed the ex-
periments. A.K and M.T characterized the device and
A.K performed the the experiments. M.B fabricated the
devices.
AM developed the theory and the numerical
simulations. A.K, A.M and J.M.G interpreted and ana-
lyzed the experimental data. A.K, A.M, K.T, J.M.C and
J.M.G contributed to the composition of the manuscript.
Author information The authors declare no com-
peting ﬁnancial interests.
Correspondence and re-
quests for materials should be addressed to A.K. (akan-
dala@us.ibm.com) or A.M. (amezzac@us.ibm.com)

FIG. 4.
Application to quantum magnetism: 4 qubit
Heisenberg model on a square lattice, in an external
magnetic ﬁeld. Comparison of the optimization using d = 0
(blue) and d = 2 (red) circuits for state preparation. a Energy
optimization for J/B = 1, plotted against the exact energy
(dashed black line). The inset of highlights the qubits used
for the experiment, and the cross-resonance gates that con-
stitute UENT. Experimental results for d = 0 (blue squares)
and d = 2 (red circles) plotted against exact curves (black
dashed lines) and density plots of 100 numerical outcomes,
for b energy and c magnetization, for a range of J/B ratios.

state energies for a range of J/B values in Fig. 4b, and
our deviations are captured by the density plots of the
numerical outcomes that account for noisy energy esti-
mations and decoherence. Furthermore, in Fig. 4c, we
show that our approach can also be used to evaluate ob-
servables such as the magnetization of the system Mz.
The experiments presented here have shown that a
hardware-eﬃcient VQE implemented on a six-qubit su-

[1] National Energy Research Scientiﬁc Computing Center
2015 Annual Report.
http://www.nersc.gov/assets/
Annual-Reports/2015NERSCAnnualReportFinal.pdf.
(2015).
[2] Lanyon, B. P. et al. Towards quantum chemistry on a

quantum computer. Nat. Chem. 2, 106–111 (2010).
[3] Du, J. et al. NMR implementation of a molecular hy-
drogen quantum simulation with adiabatic state prepa-
ration. Phys. Rev. Lett. 104, 030502 (2010).
[4] Peruzzo, A. et al. A variational eigenvalue solver on a

## Page 6

photonic quantum processor. Nat. Commun. 5 (2014).
[5] Wang, Y. et al. Quantum simulation of helium hydride
cation in a solid-state spin register. ACS Nano 9, 7769–
7774 (2015).
[6] O’Malley, P. J. J. et al. Scalable quantum simulation of
molecular energies. Phys. Rev. X 6, 031007 (2016).
[7] Shen, Y. et al. Quantum implementation of the unitary
coupled cluster for simulating molecular electronic struc-
ture. Phys. Rev. A 95, 020501 (2017).
[8] Paesani, S. et al. Experimental bayesian quantum phase
estimation on a silicon photonic chip. Phys. Rev. Lett.
118, 100503 (2017).
[9] Bravyi, S., Gambetta, J. M., Mezzacapo, A. & Temme,
K. Tapering oﬀqubits to simulate fermionic hamiltoni-
ans. arXiv preprint arXiv:1701.08213 (2017).
[10] Spall, J. C.
Multivariate stochastic approximation us-
ing a simultaneous perturbation gradient approximation.
IEEE Trans. Autom. Control 37, 332 (1992).
[11] Lanyon, B. P. et al. Universal digital quantum simulation
with trapped ions. Science 334, 57 (2011).
[12] Bravyi, S. & Kitaev, A. Fermionic quantum computa-
tion. Ann. Phys. 298, 210–226 (2002).
[13] Kempe, J., Kitaev, A. & Regev, O. The complexity of
the local hamiltonian problem.
SIAM J. Comput. 35,
1070 (2006).
[14] Abrams, D. S. & Lloyd, S.
Simulation of many-body
Fermi systems on a universal quantum computer. Phys.
Rev. Lett. 79, 2586 (1997).
[15] Aspuru-Guzik, A., Dutoi, A. D., Love, P. J. & Head-
Gordon, M. Simulated quantum computation of molecu-
lar energies. Science 309, 1704 (2005).
[16] Kitaev, A. Y. Quantum measurements and the abelian
stabilizer problem.
arXiv preprint quant-ph/9511026
(1995).
[17] Farhi, E., Goldstone, J. & Gutmann, S.
A quan-
tum approximate optimization algorithm. arXiv preprint
arXiv:1411.4028 (2014).
[18] Farhi, E., Goldstone, J., Gutmann, S. & Neven, H.
Quantum algorithms for ﬁxed qubit architectures. arXiv
preprint arXiv:1703.06199 (2017).
[19] Yung, M.-H. et al. From transistor to trapped-ion com-
puters for quantum chemistry. Sci. Rep. 4, 3589 (2014).
[20] McClean, J., Romero, J., Babbush, R. & Aspuru-Guzik,
A.
The theory of variational hybrid quantum-classical
algorithms. New J. Phys. 18, 023023 (2016).
[21] Wecker, D., Hastings, M. B. & Troyer, M. Progress to-
wards practical quantum variational algorithms. Phys.
Rev. A 92, 042303 (2015).
[22] Romero, J. et al.
Strategies for quantum comput-
ing molecular energies using the unitary coupled cluster
ansatz. arXiv preprint arXiv:1701.02691 (2017).
[23] Hutchings, M. et al.
Tunable superconducting qubits
with
ﬂux-independent
coherence.
arXiv
preprint
arXiv:1702.02253 (2017).
[24] Sheldon, S., Magesan, E., Chow, J. M. & Gambetta,
J. M. Procedure for systematically tuning up cross-talk
in the cross-resonance gate.
Phys. Rev. A 93, 060302
(2016).
[25] McKay, D. C., Wood, C. J., Sheldon, S., Chow, J. M. &
Gambetta, J. M. Eﬃcient Z-gates for quantum comput-
ing. arXiv preprint arXiv:1612.00858 (2016).
[26] McClean, J. R., Schwartz, M. E., Carter, J. & de Jong,
W. A. Hybrid quantum-classical hierarchy for mitigation
of decoherence and determination of excited states. Phys.

Rev. A 95, 042308 (2017).
[27] Li, Y. & Benjamin, S. C. Eﬃcient variational quantum
simulator incorporating active error minimisation. Phys.
Rev. X 7, 021050 (2017).
[28] Temme, K., Bravyi, S. & Gambetta, J. M. Error miti-
gation for short depth quantum circuits. arXiv preprint
arXiv:1612.02058 (2016).
[29] Bultink, C. C. et al. Active resonator reset in the nonlin-
ear dispersive regime of circuit QED. Phys. Rev. Applied
6, 034008 (2016).
[30] Spall, J. C. Adaptive stochastic approximation by the
simultaneous perturbation method. IEEE Trans. Autom.
Control 45, 1839 (2000).

## Page 7

SUPPLEMENTARY INFORMATION: HARDWARE-EFFICIENT QUANTUM OPTIMIZER FOR
SMALL MOLECULES AND QUANTUM MAGNETS

I.
DEVICE AND CHARACTERIZATION

The fundamental building blocks of our quantum hardware are superconducting Josephson junction (JJ) based
qubits. The physical device includes 6 ﬁxed frequency transmon qubits and a central ﬂux-tunable asymmetric trans-
mon qubit [1]. For the experiments discussed in this paper, we use 6 of these qubits, including the central ﬂux-tunable
qubit. The device connectivity is provided by two superconducting coplanar waveguide (CPW) resonators acting as
quantum information buses, each of which couples four qubits, with the central asymmetric transmon coupled to
both buses (see Fig. S1). Each qubit has its own individual CPW resonator for control and readout. The device is
fabricated on a Si wafer using a single step of photolithography and sputtering for the superconducting Nb resonators
and qubit capacitor pads, followed by e-beam lithography and double angle evaporation to deﬁne the Al-based JJ’s.
Refer to [2, 3] for further fabrication details.
Frequency crowding is an important issue for large networks of ﬁxed frequency qubits employing cross resonance
(CR) as an entangling gate, leading to crosstalk, leakage out of the computational sub-space or very slow gate times.
Furthermore, current fabrication capabilities make it challenging to control the frequencies of transmons to within
200 MHz. In this context, we designed our central qubit Q4, which is directly coupled to all other qubits on the chip,
to be weakly frequency tunable for reduced sensitivity to ﬂux noise [1]. The qubit is referred to as an ‘asymmetric
transmon’, and uses a superconducting quantum interference device (SQUID) as its inductive element.
The two
junctions in the SQUID however have diﬀerent Jospehson energies, engineered by varying the size of the junctions.
An external superconducting coil is used to tune Q4 to its upper sweet spot, which, in the current experiment, is
the optimal point for CR gates to its neighbors. The ﬂux-tuning curve is shown in Fig. S2. At its upper sweet spot,
Q4 is operated as a ﬁxed frequency transmon, with coherence times that are comparable to other qubits on the chip
Table S1.

FIG. S1.
Device and circuit schematic False colored optical micrograph depicts the components of our superconducting
quantum processor: seven transmon qubits, two shared CPW resonators (in blue) for qubit-qubit coupling, and seven individual
CPW resonators used for both, qubit control and readout. The qubits are controlled solely by microwave pulses that are delivered
from the room temperature electronics via attenuated coaxial lines. The single qubit gates are implemented by microwave drives
at the speciﬁc qubit Qi’s frequency ωi , while the entangling two-qubit CR gates are implemented by driving a control qubit
Qc at the frequency ωt of the target qubit Qt, where i, c, t ∈{1, 2, 3, 4, 5, 6}. The state of each qubit is measured at its readout
resonator frequency ωMi. The reﬂected readout signals are ampliﬁed ﬁrst by a JPC, pumped at a frequency ωP i, followed by
HEMT ampliﬁers at 4K.

## Page 8

TABLE S1.
Qubit and readout characterization. Qubit transitions (ω01/2π), average relaxation times (T1), average
coherence times (T2, T ∗
2 ), readout resonator frequencies (ωr/2π), qubit anharmonicity (δ/2π), readout assignment errors (ϵr)
for the six qubits discussed in the paper.

FIG. S2.
Asymmetric transmon and tuning curve a False-colored optical micrograph of an asymmetric transmon, with
an Al SQUID loop (in green), shunted by Nb capacitor pads (in blue). b Qubit frequency versus ﬂux for the asymmetric
transmon Q4. A constant ﬂux oﬀset is subtracted, and the ﬂux is expressed in units of the ﬂux quantum Φ0 = h/2e, where h
is Planck’s constant, and e is electric charge. The qubit is operated at its upper ﬂux sweet spot, indicated by the arrow. The
dashed line is a guide to the eye.

The qubits are readout by dispersive measurements through independent readout resonators, with each readout line
having a sequence of low temperature ampliﬁers — a Josephson parametric converter (JPC) [4, 5] followed by a high
electron mobility transistor (model : LNF-LNC4 8A) — for achieving high assignment ﬁdelity. For a measurement
time of 1.5 µs, the joint readout assignment errors on Q2, Q4, Q6 are < 0.06, and < 0.03 for Q1, Q3, and Q5. The
anharmonicity of the ﬁxed frequency qubits are ∼310 MHz, while the asymmetric transmon has an anharmonicity
of ∼300 MHz. Further details of the device parameters are listed in Table S1.
The experimental implementation of variational quantum algorithms requires stability of the gates used for trial
state preparation. Given the long times associated with optimization of large Hamiltonians, we periodically calibrate
the amplitude and phase of our single-qubit and two-qubit gates during the course of the experiment. In order to
estimate the time scale and magnitude of drifts in pulse amplitude and phase, we repeatedly calibrate our gates over
several hours. For instance, Fig. S3 shows the drifts in the pulse amplitude for calibrated Xπ pulses, expressed as

## Page 9

FIG. S3.
Single qubit gate drifts Repeated calibrations of the amplitude for a Xπ pulse over 18 hours for Q1-4 (a-d) reveal
the magnitude and timescale for drifts in the amplitude of the single qubit gates. Here, the amplitude drifts are scaled as angle
deviations ∆θ from the starting Xπ-rotation.

angle deviations from the starting 180o X-rotation. Over the course of 18 hours, the deviations are less than 1.5o.

II.
HARDWARE-EFFICIENT OPTIMIZATION OF QUANTUM HAMILTONIAN PROBLEMS

We present here a compact scheme describing the whole optimization algorithm. The individual subroutines of the
method will be described in the following sections.

Algorithm 1 Hardware-eﬃcient optimization of quantum Hamiltonian problems

1: Map the quantum Hamiltonian problem to a qubit Hamiltonian H
2: Choose a depth d for the quantum circuit that prepares the trial state
3: Choose a set of variational controls ⃗θ1 that parametrize the starting trial state
4: Choose a number of samples S for the feedback loop and one Sf for the ﬁnal estimation
5: Choose a number of maximal control updates kL
6: while Ef has not converged do
7:
procedure Quantum Feedback Loop
8:
for k = 1 to kL
do
9:
Prepare trial states around ⃗θk and evaluate ⟨H⟩with S samples

10:
Update and store the controls ⃗θk
11:
end for
12:
Evaluate Ef = ⟨H⟩using the best controls with Sf samples
13:
end procedure
14:
Increase d, kL, S, Sf
15: end while
16: return Ef

In the above algorithm, the ﬁrst item describes the encoding of quantum Hamiltonians on a set of qubits. In the
case of addressing a fermionic problem, we use an encoding and qubit reduction scheme from Ref. [6], explained in
Section III, which is convenient for the molecular problems considered in this work. In general, diﬀerent encodings
could be considered, such as ones based on ﬁrst-quantization methods. The outcome of the optimization depends on
the parameters d, kL, S, Sf, and in general will be better as these are increased, up to a point in which either one
saturates the quantum resources available (e.g. decoherence limit, sampling time), or the optimization outcome Ef
has converged: in this case increasing d, kL, S, Sf will not improve the ﬁnal answer Ef. In Section IV we describe
the speciﬁc entangling gates we have used int the experiment to prepare trial states. In Section V we give details
on the evaluation of the mean energy ⟨H⟩, and its dependence on the total number of samples S and experimental
assignement errors. The energies measured in this way are then fed to a classical optimizer, described in Section VI.

## Page 10

In Section VII we numerically estimate the resources required (circuit depth d, number of control updates kL, number
of samples S) to improve the accuracy of the optimization outcome.

III.
MOLECULAR HAMILTONIANS

The molecular Hamiltonians considered in this work are computed in the STO-3G basis, using the software
PyQuante [7] to obtain the one and two-electron integrals. The STO-3G minimal basis is obtained by ﬁtting three
gaussians to the Slater atomic orbitals, and commonly used in quantum chemistry because of the eﬃciency in obtain-
ing electronic integrals [8]. For the H2 molecule, each atom contributes a 1s orbital, for a total of 4 spin-orbitals. We
set the X axis as the interatomic axis for the LiH and BeH2 molecules, and consider the orbitals 1s for each H atom
and 1s, 2s, 2px for the Li and Be atoms, assuming zero ﬁlling for the 2py and 2pz orbitals, which do not interact
strongly with the subset of orbitals considered. This choice of orbitals amounts to a total of 8 spin-orbitals for LiH
and 10 for BeH2. The Hamiltonians are expressed using the second quantization language,

M
X

α,β=1
tαβ a†
αaβ + 1

H = H1 + H2 =

2

M
X

α,β,γ,δ=1
uαβγδ a†
αa†
γaδaβ,
(3)

where a†
α(aα) is the fermionic creation(annihilation) operator of the fermionic mode α, satisfying fermionic commu-
tation rules {aα, aβ} = 0, {a†
α, a†
β} = 0, {aα, a†
β} = δαβ. Here M = 4, 8, 10 is the number of spin-orbitals for H2, LiH
and BeH2 respectively, and we have used the chemists’ notation [8] for the two-body integrals,

tαβ =
Z
d⃗x1Ψα(⃗x1)

i

!

−
⃗∇2
1
2 +
X

Zi
|⃗r1i|

Ψβ(⃗x1),
(4)

uαβγδ =
Z Z
d⃗x1d⃗x2Ψ∗
α(⃗x1)Ψβ(⃗x1) 1

|⃗r12|Ψ∗
γ(⃗x2)Ψδ(⃗x2),
(5)

where we have deﬁned the nuclei charges Zi, the nuclei-electron and electron-electron separations ⃗r1i and ⃗r12, the
α-th orbital wavefunction Ψα(⃗x1), and we have assumed that the spin is conserved in the spin-orbital indices α, β and
α, β, γ, δ. In the case of LiH and BeH2, we then consider perfect ﬁlling for the inner 1s orbitals, dressed in the basis in
which H1 is diagonal. To this extent, we ﬁrst implement a Bogoliubov transformation on the modes a′
α = P

β Uαβaβ,
such that

Hd
1 = U †H1U,
Hd
1 =

M
X

α=1
ω′
αa′†
αa′
α.
(6)

We then consider the “dressed” 1s modes of Li and Be to be ﬁlled, eﬃciently obtaining an eﬀective Hamiltonian
acting on generic states of the form | Ψ⟩= a′†
1s↑a′†
1s↓
P

β̸=1sσ ψβa′†
β

| 0⟩, where ψβ are generic normalized coeﬃcients,

and 1sσ = {1s ↑, 1s ↓} refers to the inner 1s orbitals of Li and Be. Note that this approximation is valid whenever
−ω′
1sσ ≫|u′
αβγδ| ∀σ, α, β, γ, δ, i.e. in the case of very low-energy orbitals that do not interact strongly with the

higher-energy ones. The ansatz | Ψ⟩= a′†
1s↑a′†
1s↓
P

β̸=1sσ ψβa′†
β

| 0⟩allows to deﬁne an eﬀective screened Hamiltonian
on the 1s orbitals for the hydrogen atoms, and 2s and 2px for Lithium and Berillium, for a total of 6 and 8 spin-orbitals
for LiH and BeH2, respectively. According to this ansatz, the one-body fermionic terms containing the ﬁlled orbitals
will now contribute as a shift to the total energy (I here is the identity operator)

ω′
1↑a′†
1↑a′
1↑→ω′
1↑I,
ω′
1↓a′†
1↓a′
1↓→ω′
1↓I,
(7)

while some of the two-body interactions, containing the set F of 1s ﬁlled modes of Li and Be, F = {1s ↑, 1s ↓},
become eﬀective one-body or energy shift terms,

u′
αβγδ














2
a′†
γ a′
δ,
α = β, α ∈F, {γ, δ} /∈F
u′
αβγδ

2
a′†
αa′
β,
γ = δ, γ ∈F, {α, β} /∈F

−
u′
αβγδ

u′
αβγδ

2
a′†
γ a′
β,
α = δ, α ∈F, {β, γ} /∈F

2
a′†
αa′†
γ a′
δa′
β →

−
u′
αβγδ

(8)

2
a′†
αa′
δ,
γ = β, γ ∈F, {α, δ} /∈F
u′
αβγδ













2
I,
α = β, γ = δ, α ̸= γ, {α, γ} ∈F

−
u′
αβγδ

2
I,
α = δ, γ = β, α ̸= γ, {α, γ} ∈F,

## Page 11

while the two-body operators containing an odd number of modes in F will be neglected. We then map the fermionic
Hamiltonians H = P

α,β,γ,δ̸=1sσ u′
αβγδ a′†
αa′†
γ a′
δa′
β obtained in this way to our qubits. The H2
Hamiltonian is mapped ﬁrst onto 4 qubits using a binary-tree mapping [9]. We order the M spin-orbitals by listing
ﬁrst the M/2 spin-up ones and then the M/2 spin-down ones. When using the binary-tree mapping, this produces
a qubit Hamiltonian diagonal in the second and fourth qubit, which has the total particle and spin Z2 symmetries
encoded in those qubits [6]. For the LiH and BeH2 Hamiltonians we use the parity mapping, which has the two Z2
symmetries encoded in the M/2-th and M-th mode, even if the total number of spin orbitals is not a power of 2, as
in the case of H2. We then assign to the Z Pauli operators of the M/2- and M-th qubits a value based on the total
number of electrons m in the system according to

α,β̸=1sσ tαβ a′†
αa′
β +1/2 P







{+1, +1},
mod (m, 4) = 0
{±1, −1},
mod (m, 4) = 1
{−1, +1},
mod (m, 4) = 2
{±1, −1},
mod (m, 4) = 3,

{ZM/2, ZM} =

(9)






The +1(−1) on ZM for even(odd) m implies an even(odd) total electron parity. The values +1, −1 and ±1 for
ZM/2 mean that the total number of electrons with spin-up in the ground state is even, odd, or there is an even/odd
degeneracy, respectively. In the last case both +1 and −1 can be used equivalently for ZM/2. The ﬁnal qubit-tapered
Hamiltonians consist of 4, 99 and 164 Pauli terms supported on 2, 4, 6 qubits, each having 2, 25 and 44 tensor product
basis (TPB) sets (see Section V) for H2, LiH and BeH2, respectively. We explicitly list the Hamiltonians at the bond
distance in Table S2.

IV.
CHARACTERIZATION OF THE ENTANGLERS

The entanglers in our hardware-eﬃcient approach are collective gates composed of individual two-qubit gates on
a convenient connectivity. For our ﬁxed frequency, multi-qubit architecture, a good choice of two-qubit entangling
gate is the microwave-only cross resonance (CR) gate [10–12]. These gates constitute the entanglers UENT in the trial
state preparation and are implemented by driving a control qubit Qc with a microwave pulse that is resonant with
a target qubit Qt. With the addition of single qubit rotations, the CR gate can be used to construct a controlled
NOT (CNOT), with ﬁdelities exceeding 99% for gate time ∼160 ns [13]. In the hardware-eﬃcient approach, however,
tuning up a high-ﬁdelity CNOT gate is not required, as long as entanglement is delivered with the CR drive. A
simplistic model of the CR drive Hamiltonian is given by

HD ≈/ℏϵCR(t)

mIX −(J/∆)ZX + (µ)ZI

(10)

Here, ϵCR(t) is the CR drive amplitude, m quantiﬁes the strength of the classical cross-talk, J is the strength of
the qubit-qubit coupling, ∆is the frequency separation between the qubits, and µ corresponds to the drive induced
Stark-shift. However, a more detailed study [13] of the drive revealed additional terms, whose strengths are revealed
by Hamiltonian tomography. For instance, in the CR2−4 drive used in the experiment, these terms are ZX : 1.04
MHz, ZY : 0.07 MHz, ZZ : 0.05 MHz , IX : 0.68 MHz, IY : 0.12 MHz, IZ : 0.02 MHz. We measure the norm of the
Bloch vector ||⃗R|| discussed in [13], whose time evolution indicates points of maximal entanglement at ||⃗R|| = 0; see
Fig. S4b.
As discussed in the main text, the entangling gate phase could be an additional variational parameter for the
optimization. However we show by numerical simulations that chemical accuracy (≈0.0016 Hartree, the accuracy of
the energy estimate required to predict the exponentially sensitive chemical reaction rates at room temperature to
within an order of magnitude of the exact value) can be reached for a range of ﬁxed gate phases around points of
maximum concurrence. This is shown in Fig. S4a,d which shows the error in the energy estimates from numerical
optimization of the LiH Hamiltonian at bond distance, as a function of the gate phase of the two-qubit gates that
compose the entanglers UENT. For these simulations, we choose ZX gates for UENT, using the same connectivity
as the experiment (2-1, 1-3, 2-4 for the case of 4-qubit experiments). In order to isolate the eﬀect of the entangling
phase in the optimization, we do not consider a decoherence model and stochastic ﬂuctuations in these simulations (as
opposed to Fig. 3 and 4 in the main text), and set a high total number of energy evaluations to 5 × 104. The results
show plateaus of minimum energy errors, correlated with regions around points of maximal concurrence (Fig. S4c)
for the individual two-qubit gates. Instead of setting our gate times to points of maximal concurrence, we choose
them such that the corresponding gate phases lie at the beginning of the minimal error plateaus, in order to minimize
the eﬀect of decoherence while delivering suﬃcient entanglement. For our chosen two-qubit gate time of 150 ns, we

## Page 12

FIG. S4.
Dependence of energy error on entangler phase a Energy error of numerical optimizations, as a function of
the phase of the entanglers, for diﬀerent depths d = 1, 2, 3, 4, 6, 8. The energy error is averaged over 10 optimization runs, for
each depth, with bands represent the standard deviation of the distribution. The dashed vertical lines indicate approximate
gate phases of the individual CR gates for the gate time of 150 ns, including ﬁnite pulse ramping times. b Norm of the Bloch
vector ||⃗R|| as a function of gate time for all the two-qubit entangling gates used in the experiment. The black dashed line
corresponds to a gate time of 150 ns. The points where ||⃗R|| = 0 indicate gate times of maximal entanglement. c Concurrence
v/s gate phase of a ZX gate, starting from the state (| 10⟩+ | 00⟩)
√

2. The energy error in a is least around points of maximal
concurrence. d Energy error v/s entangler gate phase on a log linear scale. The dashed black line indicates chemical accuracy
(0.0016 Hartree), showing that a critical depth d = 6 is required to achieve such accuracy. Color scheme follows from a.

extrapolate the phases of all CR gates under the simple assumption of having a time independent ZX Hamiltonian
with ﬁnite pulse ramping times, and indicate them in Fig. S4a. Also, CR drives for qubits on diﬀerent buses are
driven simultaneously, in order to reduce the time associated with state preparation.

V.
ENERGY ESTIMATION

The update of the angles in our optimization routine is based on measurements of the expectation value of the
Hamiltonian operator. These measurements are then used to build an approximation of the gradient of the energy
landscape, which is in turn used to get a better update of the angles (see Section VI). The energy estimation at every
k-th trial state of the optimization is a central part of the optimization algorithm, since its accuracy aﬀects the ﬁnal
outcome of the optimization. Once mapped to qubits (see Section III), every molecular Hamiltonian is expressed as
a weighted sum of T Pauli terms supported on N qubits

T
X

H =

α=1
hαPα,
(11)

where each Pα ∈{X, Y, Z, I}⊗N is a tensor product of single-qubit Pauli operators X, Y, Z and the identity I, on N
qubits, with hα being real coeﬃcients. We are interested in estimating the mean energy ⟨Φ(⃗θk) |H| Φ(⃗θk)⟩≡⟨H⟩k

## Page 13

for the k-th control updates (more speciﬁcally for two sets of angles close to ⃗θk, see Section VI). This can be done
by averaging measurements outcomes from individual experiments, where one prepares the same initial state, applies
the quantum gates parametrized by ⃗θk, and ﬁnally performs projective measurements on the individual qubits. In
the experiment we do not have access to direct measurements of the Hamiltonian operator ⟨H⟩and its variance
⟨∆H2⟩= ⟨H2 −⟨H⟩2⟩.
Instead, we sample the individual Pauli operators Pα, estimating the mean values and
variances ⟨Pα⟩, ⟨∆P 2
α⟩= ⟨P 2
α −⟨Pα⟩2⟩from the measurements outcomes of the α-th Pauli operator. The energy and
Hamiltonian variance can then be obtained as

T
X

⟨H⟩=

T
X

Var[H] =

α=1
hα⟨Pα⟩,
(12)

α=1
h2
α⟨∆P 2
α⟩
(13)

Note that the variance on the mean energy Var[H] is diﬀerent from ⟨∆H2⟩, since we are sampling the individual Pauli
terms separately: for example, eigenstates of H will have ⟨∆H2⟩= 0, but a ﬁnite Var[H] ̸= 0. The error on the mean
energy ⟨H⟩after taking S samples for each Pauli operator is

r

r

Var[H]

S
≤

ϵ =

T|h2max|

S
(14)

where hmax = maxα |hα| is the absolute value of the largest Pauli coeﬃcient. Since sampling S times for a large
number of trial states and Pauli operators comes with signiﬁcant time overhead, one can instead use the same state
preparations to measure diﬀerent Pauli operators. This approach was considered in [14] for commuting operators.
Here we use a stronger condition on grouping diﬀerent Pauli terms, based on improving time eﬃciency. We ﬁst brieﬂy
describe how we sample an individual Pauli operator. The individual Pauli operators are measured by correlating
measurement outcomes of single-qubit dispersive readouts in the Z basis, which can be done simultaneously since
each qubit is provided with an individual readout resonator. In case a target multi-qubit Pauli operator contains non
diagonal single-qubit Pauli operator, single-qubit rotations (post-rotations) are performed before the measurement in
the Z basis. Speciﬁcally, a −π/2(π/2) rotation along the X(Y ) axis to measure a Y(X) single-qubit Pauli operator.

A.
Grouping Pauli Operators

To minimize sampling overheads, we group the T Pauli operators Pα in A sets s1, s2, ...sA, which have terms that
are diagonal in the same tensor product basis. The post-rotations required to measure all the Pauli terms in a given
TPB set are the same, and a unique state preparation can be used to sample all the Pauli operators in the same set.
By doing so, however, covariance eﬀects in the same TPB set contribute to the variance of the total Hamiltonian,

A
X

X

VarG[H] =

α,β∈si
hαhβ⟨(Pα −⟨Pα⟩)(Pβ −⟨Pβ⟩)⟩≤h2
max(T + As2
max),
(15)

i=1

where smax = maxi |si| is the number of elements in the largest TPB set.
Keeping the same total number of
measurements TS as in Eq. (14), the error on the mean in this case is given by

s

r

VarG[H]

S
≤

ϵ =

Ah2max(T + As2max)

TS
,
(16)

which can be compared to the case in which one samples the single Pauli terms individually, Eq. (14). The error
contribution from the covariance (which can be positive or negative) has to be traded oﬀagainst the use of less
samples from grouping. The quantities in Eqs. (12) and (15) can be estimated in the experiment and in the numerical
simulations as

S
X

d
⟨Pα⟩= 1

S

A
X

\
VarG[H] =

X

i=1

i=1
Xi,α,
(17)

α,β∈si
hαhβcov( d
⟨Pα⟩, d
⟨Pβ⟩),
(18)

## Page 14

FIG. S5.
Energy variance Numerical computation of the variance of the mean energy ϵ2, as in Eq. (18), with S = 103

samples, for the molecular Hamiltonians of H2 (a, d), LiH (b, e) and BeH2 (c, f) at their bond interatomic distances (see
Table S2). The variances are computed sampling each Pauli operator Pα in H of Eq. (11) individually ( a, b, c ) and grouping
them in TPB sets ( d, e, f ), keeping the total number of samples the same.

where we have deﬁned the outcome of the i-th measurement on the α-th Pauli term as Xi,α. The covariance matrix
element is deﬁned after S measurements as

S
X

cov( d
⟨Pα⟩, d
⟨Pβ⟩) =
1
S −1

i=1
(Xi,α −d
⟨Pα⟩k)(Xi,β −d
⟨Pβ⟩).
(19)

To evaluate whether grouping into TPB sets is convenient for the molecular Hamiltonians considered in this work, we
perform numerical sampling experiments, shown in Fig. S5, using the Hamiltonians in Table S2. The variance of the
mean energy is numerically sampled on 104 random states. In the “TPB sets” simulations (red histograms), the set of
post-rotations associated to each TPB set if found by union of the set of post-rotations necessary to sample each Pauli
in a given TPB set: for example, for the third TPB set of BeH2 in Table S2 we have the post-rotations associated
to ZZXXZX. Then, for each random state, a sample of S = 103 measurement outcomes are drawn for every TPB
set. The total number of measurement is therefore AS. These measurements are then used to obtain the mean value
and covariance for each Pauli operator in the TPB set. The variance of the mean total energy is then obtained as in
Eq. (15). In the “No-TPB sets” simulations (blue histograms), the same measurements are drawn independently for
each Pauli operator, with a number of samples per Pauli term SA/T, in order to keep the total number of samples in
the TPB and No-TBP simulations the same. The results show the advantage of grouping into TPB sets for all the
molecular Hamiltonians considered.

B.
Assignement Errors

An important aspect to take into account when sampling is the presence of assignment errors at the qubit readout.
A qubit-independent assignement error can be modeled by a deformation ˆΠ0, ˆΠ1, of the ideal projectors Π0, Π1 on
the | 0⟩, | 1⟩states for the qubit,

ˆΠ0 = (1 −η0 + η1)Π0 + (1 −η0 −η1)Π1 = (1 −η0)I + η1Z
ˆΠ1 = (η0 −η1)Π0 + (η0 + η1)Π1 = η0I −η1Z,
(20)

## Page 15

via the two parameters η0, η1 (note that in the absence of errors η0 = η1 = 1/2), such that ˆΠ0 + ˆΠ1 = I. With these
deﬁnitions, the assignment error of reading a qubit in | 1⟩(| 0⟩) when it is in | 0⟩(| 1⟩) is given by 1−η0−η1, or (η0−η1).
The measured readout assignement error, averaged on preparations of | 0⟩and | 1⟩in Table S1, can be expressed with
the parametrization considered as ϵr = 1/2 −η1. The projectors in Eqs. (20) deﬁne an eﬀective deformed ˆZ operator,
related to the ideal one Z via

ˆZ = ˆΠ0 −ˆΠ1,
Z =
ˆZ −(1 −2η0)I

2η1
.
(21)

Note that the measured value ⟨bZ⟩is aﬀected by the contrast factor 2η1, and shifted by the amount 1−2η0. Generalizing
this to a Pauli operator with weight w, one has that

Z⊗w ∝
ˆZ⊗w

(2η1)w ,
(22)

revealing an exponential loss in contrast in the weight w. When addressing larger systems, it will then be important to
use the binary tree encoding [9], for its logarithmic scaling in locality with the system size, to combat the exponential
scaling in (22). Note that the error model in Eq. (20) only takes into account independent readout errors, while in
general correlated readout errors may happen. In our experiments we take into account assignement errors by running
readout calibrations before sampling for every update of the angles ⃗θ, and then correcting our sampling outcome with
the calibrations.

VI.
OPTIMIZATION USING A SIMULTANEOUS PERTURBATION METHOD

The energy ⟨Φ(⃗θk) |H| Φ(⃗θk)⟩≡⟨H⟩k discussed in Section V, which needs to be evaluated before every update of the
angles ⃗θ, has a number of parameters p = N(3d−1) that grows linearly with the depth of the circuit d and the number
of qubits N. As the number of parameters increases the classical optimization component of the algorithm comes with
increasing overheads. The accuracy of the optimization may also be signiﬁcantly lowered by the presence of energy
ﬂuctuations at the k-th step ϵk. Furthermore, on real quantum hardware, there are time overheads associated with
loading of pulse waveforms on the electronics, resonator and qubit reset, and repeated sampling of the qubit readout.
Ideally, one would like to use an optimizer robust to statistical ﬂuctuations, that uses the least number of energy
measurements per iteration. The simultaneous perturbation stochastic approximation (SPSA) algorithm, introduced
in [15], is a gradient-descent method that gives a level of accuracy in the optimization of the cost function that is
comparable with ﬁnite-diﬀerence gradient approximations, while saving an order O(p) of cost function evaluations. It
has been recently used in the context of quantum control and quantum tomography [16–18].
In the SPSA approach, for every step k of the optimization, we sample from p symmetrical Bernoulli distributions
(coin ﬂips) ⃗∆k, and use preassigned elements from two sequences converging to zero, ck and ak. The gradient at ⃗θk
is approximated using energy evaluations at ⃗θ±
k = ⃗θk ± ck ⃗∆k, and is constructed as

⃗gk(⃗θk) = ⟨Φ(⃗θ+
k )|H|Φ(⃗θ+
k )⟩−⟨Φ(⃗θ−
k )|H|Φ(⃗θ−
k )⟩
2ck
⃗∆k,
(23)

as illustrated in Fig. S6a. Note that this gradient approximation only requires two estimations of the energy, regardless
of the number p of variables in ⃗θ. The controls are then updated as

⃗θk+1 = ⃗θk −ak⃗gk(⃗θk).
(24)

The convergence of θk to the optimal solution ⃗θ∗can be proven even in the presence of stochastic ﬂuctuations, if
the starting point is in the domain of the attraction of the problem [15], . Convergence remains an open issue if the
starting point for the controls is not in a domain of attraction. In this case strategies like multiple competing starting
points can be adopted [19]. The sequences ck, ak can be chosen as

ck = c

kγ ,

ak = a

kα .
(25)

We pick the parameters α, γ optimally at {α, γ} = {0.602, 0.101} [20], ensuring the smoothest descent along the
approximate gradients deﬁned in Eq. (24). We then tune the value of c to adjust the robustness of the gradient

## Page 16

FIG. S6.
Calibration of the classical optimizer a Good gradient approximations ⃗gk(⃗θk) are obtained if the energy
diﬀerence |⟨Φ(⃗θ+
k )|H|Φ(⃗θ+
k )⟩−⟨Φ(⃗θ−
k )|H|Φ(⃗θ−
k )⟩| is larger than the stochastic ﬂuctuations on the energy ϵk. The parameter c
in Eq. (25) is heuristically chosen to meet this condition. b The parameter a in Eq. (25) is calibrated by measuring 25 times
the energies E(⃗θ±
1 ) = ⟨Φ(⃗θ±
1 )|H|Φ(⃗θ±
1 )⟩, measured here for the LiH molecule at the bond distances, from the starting angles
⃗θ1, for diﬀerent random gradients approximations. c The energy diﬀerence ∆E = |⟨Φ(⃗θ+
1 )|H|Φ(⃗θ+
1 )⟩−⟨Φ(⃗θ−
1 )|H|Φ(⃗θ−
1 )⟩| is
measured for each random instance of the gradient (solid green line), averaged (black dotted line), and then used to calibrate
the parameter a, according to Eq. (27).

evaluation with respect to the magnitude of the energy ﬂuctuations. In fact, large ﬂuctuations of the energy require
gradient evaluations with large ck (23), so that the ﬂuctuations do not substantially aﬀect the gradient approximation.
This condition is valid in the regime

|⟨Φ(⃗θ+
k )|H|Φ(⃗θ+
k )⟩−⟨Φ(⃗θ−
k )|H|Φ(⃗θ−
k )⟩| ≫ϵk,
(26)

depicted visually in Fig. S6a. Keeping these considerations in mind, we have used c = 10−1 to ensure robustness in
all the experiments and in the realistic simulations that include decoherence noise and energy ﬂuctuations, while the
smaller c = 10−2 factor is used in the numerical optimizations where the energy is evaluated without ﬂuctuations.
The parameter a is then calibrated experimentally in order to achieve a reasonable angle update on the ﬁrst step of
the optimization, which we chose to be |θ(i)
2 −θ(i)
1 | = 2π/10, for all the angles i = 1, 2, ...p. To achieve this, we use an
inverse formula based on Eq. (24),

a = 2π

5
c
D
|⟨Φ(⃗θ+
1 )|H|Φ(⃗θ+
1 )⟩−⟨Φ(⃗θ−
1 )|H|Φ(⃗θ−
1 )⟩|
E

,
(27)

⃗∆1

where the notation
DE

⃗∆1 indicates an average over diﬀerent samples from the distribution ⃗∆1 that generates the

ﬁrst gradient approximation. In fact, by averaging along diﬀerent directions, we can measure the average slope of the
functional landscape of ⟨Φ(⃗θ)|H|Φ(⃗θ)⟩in the vicinity of the starting point ⃗θ1, and calibrate the experiment accordingly.

In the experiment and in the numerics the average
DE

⃗∆1
is realized over 25 random gradient directions. The gradient

averaging is shown for the optimization of the LiH Hamiltonian at bond distance with a d = 1 circuit, in Fig. S6b,c.
Note that along the optimization we do not measure the value of the energy for the k-th optimized angles
⟨Φ(⃗θk)|H|Φ(⃗θk)⟩, instead we only measure and report the values ⟨Φ(⃗θ+
k )|H|Φ(⃗θ+
k )⟩and ⟨Φ(⃗θ−
k )|H|Φ(⃗θ−
k )⟩, which
serve to generate a new gradient approximation. The underlying optimized angles ⃗θk are only measured at the end of
the optimization, averaging over the last 25 ⃗θ+
k and 25 ⃗θ−
k , to further minimize stochastic ﬂuctuations eﬀect. Further-
more, this last average is done with 105 samples, as opposed to the 103 samples used to generate ⃗θ+
k and ⃗θ−
k during
the optimization, in order to reduce the error on the measurement.

## Page 17

VII.
NUMERICAL SIMULATIONS AND SCALING OF RESOURCES

In this Section we ﬁrst describe the numerical simulations used in Fig. 3 and Fig. 4, which include decoherence eﬀects
and stochastic ﬂuctuations on the energy evaluation. We then show numerical results that indicate the scaling of the
optimization outcome with the depth of the trial state preparation circuit, the number of angle updates considered
in the optimization, and the sampling statistics. We estimate the resources necessary to achieve chemical accuracy
for the three molecules considered. Last, we show the interplay between circuit depth and decoherence aﬀecting the
quantum circuit, using a depolarizing noise model.

A.
Numerical model of the experiment

In the numerical simulations in Fig. 3, Fig. 4 and Fig. S9, we have used entanglers made up of ZX two-qubit
entangling gates, with a phase of π/4, and with additional terms ZY , ZZ, IX, IY , and IZ, whose relative phases
are chosen according to the measurement reported in Section IV for CR2−4. We use the same connectivity as in the
experiment, with entangling gates between qubits 1 −2, 2 −4 and 1 −3 in the 4-qubit simulations (LiH and quantum
magnetism model) and gates between qubits 1 −2, 2 −4, 1 −3, 4 −5 and 5 −6 in the 6-qubit simulations (BeH2).
The initial Z angles are distributed normally around zero according to N(0, 1), and the X angles set to π/2.
The eﬀect of decoherence is taken into account by adding amplitude damping (Ea
0(τ), Ea
1(τ)) and dephasing
(Ed
0(τ), Ed
1(τ)) channels acting on the system density matrix ρ →Ea
0(τ)ρEa†
0 (τ)+Ea
1(τ)ρEa†
1 (τ), ρ →Ed
0(τ)ρEd†
0 (τ)+
Ed
1(τ)ρEd†
1 (τ), for all the qubits, after each round of Euler gates and entanglers, respectively. The strength of the
channels is set by the experimental coherence times and the length of the gates,

"
0
√

"
1
0
0
√

#

#

1 −e−τ/T1

Ea
0(τ) =

, Ea
1(τ) =

(28)

e−τ/T1

0
0

"
1
0
0 e−τ/Tφ

#

"
0
0
0
p

#

Ed
0(τ) =

, Ed
1(τ) =

.
(29)

1 −e−2τ/Tφ

Here the time τ alternates between the duration of each single qubit gate sequence or entangler step, and the pure
dephasing time is deﬁned as Tφ = 2T ∗
2 T1/(2T1 −T ∗
2 ), see Table S1 for measured values on each qubit.
In the
H2 simulations, since we use the most coherent qubits on the chip, we parametrize the noise channels considering
T1 = T ∗
2 = 40 µs and set the length of UENT to 150 ns, while for the 4 and 6-qubit simulations we use typical coherence
values for the qubits of T1 = 30 µs, T ∗
2 = 20 µs and a duration for UENT of 450 ns. Note that the duration for both
4 and 6-qubit entanglers is set to be the same because the two-qubit gates CR2−1, CR4−5 and CR1−3, CR6−5 are
done in parallel, see Fig. 1c in the main text. To simulate the eﬀect of ﬁnite sampling in the experiment, we ﬁrst
compute an average value of the standard deviation of the energy by sampling 103 times on 100 random states, as
described in Section V. Then we add a normal-distributed error to each energy evaluation along the optimization,
with the standard mean deviation computed previously on random states. On average, this will account for the energy
ﬂuctuations at the k-th step of the optimization. We ﬁx the total number of angle updates to 250. For the ﬁnal
energy estimate, we average over the last 25 control updates, to mitigate the eﬀect of stochastic ﬂuctuation in the
optimization. For every interatomic distance (for every J/B ratio in the case of Fig. 4), we show the outcome of 100
numerical simulations, in the form of a density plot, in Fig. 3 (Fig. 4) in the main text.

B.
Scaling of resources: depth, function calls, sampling

In order to estimate resources required to reach chemical accuracy (i.e. an energy error of approximately 0.0016
Hartree), we consider molecular Hamiltonians at the bond distance for H2, LiH and BeH2 (see Table S2), and declare
convergence when the best energy estimate is close to the exact solution up to chemical accuracy. We assume that
the resources required to reach chemical accuracy at the bond distance are comparable with the ones for any other
interatomic distance, ensuring chemical accuracy also for the dissociation energy (deﬁned as the molecular energy
diﬀerence at the bond length and in the limit of inﬁnite interatomic energy). In these simulations for determining
the scaling of the resources, we consider ideal ZZ entangling gates with a phase of π/2. Note that any two qubit
interaction can be mapped to a ZZ one via local rotations (i.e. our Euler angles). We use only the last two single-qubit
rotation for each step, since Z rotations commute with the ZZ entangling gates, and consider two diﬀerent topologies

## Page 18

FIG. S7.
Scaling of resources to reach chemical accuracy. a The critical depth required for reaching chemical accuracy
for the 3 molecules discussed in the paper, using an all-to-all qubit connectivity (blue) and the experimental qubit connectivity
(red). b The number of function calls for reaching chemical accuracy for the 3 molecules at their respective critical depths from
a. Each data point in both plots is obtained by averaging over 10 optimization runs.

for the qubit connectivity: in addition to the experimental connecivity, we consider an “all connected” connectivity,
where the entanglers UENT are composed of ZZ gates among all the qubit pairs in the system.
For the simulations outcomes plotted in Fig. S7a, we set a maximal number of function calls to 5 × 104 (i.e. evalu-
ations of the energy as described in Section VI), ensuring convergence of the optimization beyond chemical accuracy
for all the simulations considered. We start by not taking into account decoherence and stochastic ﬂuctuations, run
10 optimizations for increasing circuit depths, average the ﬁnal optimized energies, and report the shortest depth that
has an average energy converged within chemical accuracy. Chemical accuracy is reached for depths d = 1, 8, 28 for
the experimental connectivity, and d = 1, 6, 16 for the all connected case, for H2, LiH and BeH2, respectively. Having
computed the shortest circuit depth for each molecule and connectivity, we now keep the circuit depth ﬁxed and run
optimizations, keeping track of the number of trial states suﬃcient to achieve chemical accuracy. We average the
number of trial states obtained for 10 separate optimizations. The results are plotted in Fig. S7b. Approximately
2×103 function calls (103 angle updates) are suﬃcient for reaching chemical accuracy on H2, 2×104 for LiH2 both for
the all-connected and experiment connectivity, 2 × 104 for BeH2 in the all-connected case and approximately 3 × 104

for the experiment connectivity.
We ﬁnally estimate the number of samples S required to reach chemical accuracy. We start by computing an
average standard deviation ϵA for the energy on 102 random states, considering S = 103 samples, see Section V. Then
we add the averaged deviation to the energies evaluated at the k-th step of the optimization. Then, we extrapolate
standard deviations at higher samplings S, via ϵA →ϵA
p

103/S. Using the depths indicated in Fig. S7a, we ﬁnd that
chemical accuracy is reached for all the three molecules when the number of samples is S ≈106, i.e. approximately
when all the energies in the optimization are evaluated at chemical accuracy. This can be understood by using values
for the standard deviations of the mean energies as in Fig. S5, computed at 103 samples, and extrapolating to 106

samples. These results indicate a scaling of the resources with the problem size which is not very dramatic. If we set
aside decoherence eﬀects, both number of function calls and sampling could be increased in the near future by rapid
reset protocols of the qubits [21–23].

C.
Scaling of resources: decoherence

In order to address the behavior of the optimization versus decoherence eﬀects, we run numerical simulations that
include a depolarizing noise model following each gate. We consider one-qubit and two-qubit depolarizing channels
acting on the system density matrix ρ as

ρ →(1 −ξ)ρ + ξ

X

i=1,2,3
σiρσi,

3

ρ →(1 −ξ)ρ + ξ

σj
l σi
mρσi
mσj
l ,
(30)

X

15

{i,j}={0,1,2,3}
{i,j}̸={0,0}

## Page 19

FIG. S8.
Scaling of energy error with noise strength Error in the energy estimate for the 4-qubit LiH Hamiltonian at
its bond length, for diﬀerent depolarizing noise strengths of the model in Eq. (30), for diﬀerent circuit depths used for trial
state preparation, after 5 × 104 function calls. Each data point is obtained by averaging over 10 optimization runs. The black
dashed line indicates the energy error for chemical accuracy.

where σ1 = X, σ2 = Y, σ3 = Z, σ0 = I. The single-qubit depolarizing channels act on every qubit after the Euler
rotations, while the two-qubit channels act on every qubit pair {l, m} considered in a given connectivity. We run noisy
optimizations for the LiH Hamiltonian at the bond distance, for diﬀerent number of entanglers and noise strengths,
for a maximum of 5 × 104 function calls. The results are shown in Fig. S8, averaged on 10 diﬀerent optimizations.
There is a clear interplay between the number of entanglers and the noise strength. For low noise rates ξ, higher
depths give better results, while as ϵ increases lower depths perform better. Chemical accuracy is reached for noise
rates of ≈10−5, for 6 and 8 entanglers. Such low noise rates emphasize that it will be important in the near future
to explore error mitigation methods for short depth quantum circuits [24–26].
When considering the combined eﬀects of decoherence, stochastic ﬂuctuations due to ﬁnite sampling and limited
number of trial states, the advantages of using more entanglers may not be apparent anymore. This is the case
for many of the molecular Hamiltonians discussed in this paper, whose energies are well approximated by separable
states prepared using low-depth circuits. In Fig. S9 we show the experimental optimization for diﬀerent depths,
d = 0, 1, 2, for the Hamiltonian of LiH at the bond distance, compared with 100 outcomes of numerical simulations.
The numerical histograms in Fig. S9b show large overlap between ﬁnal energy distributions for d = 0, 1, 2, conﬁrmed
by the experiments presented in Fig. S9a. This overlap between outcomes of optimizations with diﬀerent entanglers
appear for most of the molecular Hamiltonians. In contrast, for the interacting spin Hamiltonians discussed in Fig. 4
of the main text, signiﬁcantly better estimates are obtained with d = 1, 2, 3 circuits than d = 0 circuits.

## Page 20

FIG. S9.
Experimental optimization for diﬀerent depths:
LiH Hamiltonian at bond distance and 4-qubit
Heisenberg model a Experimental optimization of the 4-qubit LiH Hamiltonian at bond distance, using depth d = 0 (green),
1 (red) 2 (blue) circuits for trial state preparation. The exact energy is indicated by the black dashed line. Bottom inset
describes the qubits and the cross resonance gates that constitute UENT, for this experiment. b Histograms of outcomes from
100 numerical simulations that account for decoherence and ﬁnite sampling eﬀects show signiﬁcant overlap for depth d = 0
(green), 1 (red), 2 (blue) circuits. The black dashed line indicates the exact energy and the green, red and blue dashed lines
are the results from the single experimental runs of a, for d = 0, 1 and 2 circuits respectively. c Experimental optimization
of the 4-qubit Heisenberg Hamiltonian for J/B = 1, using depth d = 0 (green), 1 (red), 2 (blue), 3 (orange) circuits for trial
state preparation. The exact energy is indicated by the black dashed line. d Histograms of outcomes from 100 numerical
simulations that account for decoherence and ﬁnite sampling eﬀects show signiﬁcant improvement over depth d = 0 circuits
with d = 1(red), 2 (blue), 3 (orange) circuits. The black dashed line indicates the exact energy and the green, red, blue and
orange dashed lines are the results from the single experimental runs of c, for d = 0, 1, 2 and 3 circuits respectively.

## Page 21

TABLE S2: The H2, LiH and BeH2 Hamiltonians at the bond distance. Listed are all the Pauli operators, grouped in the
diﬀerent TPB sets, with the corresponding coeﬃcients, not taking into account for the energy shifts due to the ﬁlling of inner
orbitals and the Coulomb repulsion between nuclei. X,Y,Z,I here stand for the Pauli matrices σx, σy, σz and the identity
operator on a single qubit subspace, respectively. There are 2,25,44 TPB sets for H2, LiH and BeH2, respectively with 4, 99
and 164 Pauli terms in total.

H2 at bond distance

LiH at bond distance

## Page 22

BeH2 at bond distance

## Page 23

[1] Hutchings, M. et al. Tunable superconducting qubits with ﬂux-independent coherence. arXiv preprint arXiv:1702.02253
(2017).
[2] Chow, J. M. et al. Implementing a strand of a scalable fault-tolerant quantum computing fabric. Nat. Commun. 5:4015
doi: 10.1038/ncomms5015 (2014).
[3] C´orcoles, A. D. et al. Demonstration of a quantum error detection code using a square lattice of four superconducting
qubits. Nat. Commun. 6:6979 doi: 10.1038/ncomms7979 (2015).
[4] Bergeal, N. et al. Analog information processing at the quantum limit with a josephson ring modulator. Nat. Phys. 6,
296–302 (2010).
[5] Abdo, B., Schackert, F., Hatridge, M., Rigetti, C. & Devoret, M. Josephson ampliﬁer for qubit readout. Appl. Phys. Lett.
99, 162506 (2011).
[6] Bravyi, S., Gambetta, J. M., Mezzacapo, A. & Temme, K. Tapering oﬀqubits to simulate fermionic hamiltonians. arXiv
preprint arXiv:1701.08213 (2017).
[7] Muller, R. P. Python quantum chemistry, version 1.6.0. http://pyquante.sourceforge.net/.
[8] Szabo, A. & Ostlund, N. S. Modern quantum chemistry: introduction to advanced electronic structure theory (Courier
Corporation, 1989).
[9] Bravyi, S. & Kitaev, A. Fermionic quantum computation. Ann. Phys. 298, 210–226 (2002).
[10] Paraoanu, G. S. Microwave-induced coupling of superconducting qubits. Phys. Rev. B 74, 140504 (2006).
[11] Rigetti, C. & Devoret, M. Fully microwave-tunable universal gates in superconducting qubits with linear couplings and
ﬁxed transition frequencies. Phys. Rev. B 81, 134507 (2010).
[12] Chow, J. M. et al. Simple all-microwave entangling gate for ﬁxed-frequency superconducting qubits. Phys. Rev. Lett. 107,
080502 (2011).
[13] Sheldon, S., Magesan, E., Chow, J. M. & Gambetta, J. M.
Procedure for systematically tuning up cross-talk in the
cross-resonance gate. Phys. Rev. A 93, 060302 (2016).
[14] McClean, J., Romero, J., Babbush, R. & Aspuru-Guzik, A. The theory of variational hybrid quantum-classical algorithms.
New J. Phys. 18, 023023 (2016).
[15] Spall, J. C. Multivariate stochastic approximation using a simultaneous perturbation gradient approximation. IEEE Trans.
Autom. Control 37, 332 (1992).
[16] Ferrie, C. Self-guided quantum tomography. Phys. Rev. Lett. 113, 190404 (2014).
[17] Ferrie, C. & Combes, J. Robust and eﬃcient in situ quantum control. Phys. Rev. A 91, 052306 (2015).
[18] Chapman, R., Ferrie, C. & Peruzzo, A. Experimental demonstration of self-guided quantum tomography. Phys. Rev. Lett.
117, 040402 (2016).
[19] Wecker, D., Hastings, M. B. & Troyer, M. Progress towards practical quantum variational algorithms. Phys. Rev. A 92,
042303 (2015).
[20] Spall, J. C. Implementation of the simultaneous perturbation algorithm for stochastic optimization. IEEE Trans Aerosp.
and Electron. Syst. 34, 817–823 (1998).
[21] Rist´e, D., Bultink, C. C., Lenhert, K. W. & DiCarlo, L. Feedback control of a solid-state qubit using high-ﬁdelity projective
measurement. Phys. Rev. Lett. 109, 240502 (2012).
[22] McClure, D. T., Paik, H., Bishop, L. S., Chow, J. M. & Gambetta, J. M. Rapid driven reset of a qubit readout resonator.
Phys. Rev. Applied 5, 011001 (2016).
[23] Bultink, C. C. et al. Active resonator reset in the nonlinear dispersive regime of circuit QED. Phys. Rev. Applied 6, 034008
(2016).

## Page 24

[24] McClean, J. R., Schwartz, M. E., Carter, J. & de Jong, W. A.
Hybrid quantum-classical hierarchy for mitigation of
decoherence and determination of excited states. Phys. Rev. A 95, 042308 (2017).
[25] Li, Y. & Benjamin, S. C. Eﬃcient variational quantum simulator incorporating active error minimisation. Phys. Rev. X
7, 021050 (2017).
[26] Temme, K., Bravyi, S. & Gambetta, J. M.
Error mitigation for short depth quantum circuits.
arXiv preprint
arXiv:1612.02058 (2016).
