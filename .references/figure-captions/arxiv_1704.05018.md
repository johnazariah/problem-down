---
source_pdf: ../arxiv_1704.05018.pdf
pages: 24
captions: 16
extracted_at: 2026-04-17T12:32:30+00:00
extractor: PyMuPDF (fitz)
---

# arxiv_1704.05018 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## FIG. 1.

Page: 2
Caption bbox: (54.0, 343.6, 562.2, 458.2)
Crop bbox: (84.0, 44.1, 532.1, 338.2)
Crop asset: ../figure-crops/arxiv_1704.05018/page_002_figure_01.png

Caption:

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

## FIG. 2.

Page: 3
Caption bbox: (54.0, 271.7, 299.1, 414.2)
Crop bbox: (0.0, 8.0, 612.0, 267.7)
Crop asset: ../figure-crops/arxiv_1704.05018/page_003_figure_01.png

Caption:

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

## FIG. 3.

Page: 4
Caption bbox: (54.0, 228.0, 562.2, 310.2)
Crop bbox: (48.0, 40.0, 578.5, 222.6)
Crop asset: ../figure-crops/arxiv_1704.05018/page_004_figure_01.png

Caption:

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

## FIG. 4.

Page: 5
Caption bbox: (54.0, 399.0, 299.1, 512.6)
Crop bbox: (0.0, 8.0, 612.0, 395.0)
Crop asset: ../figure-crops/arxiv_1704.05018/page_005_figure_01.png

Caption:

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

## FIG. S1.

Page: 7
Caption bbox: (54.0, 637.6, 562.2, 719.8)
Crop bbox: (8.0, 8.0, 604.0, 633.6)
Crop asset: ../figure-crops/arxiv_1704.05018/page_007_figure_01.png

Caption:

FIG. S1.
Device and circuit schematic False colored optical micrograph depicts the components of our superconducting
quantum processor: seven transmon qubits, two shared CPW resonators (in blue) for qubit-qubit coupling, and seven individual
CPW resonators used for both, qubit control and readout. The qubits are controlled solely by microwave pulses that are delivered
from the room temperature electronics via attenuated coaxial lines. The single qubit gates are implemented by microwave drives
at the speciﬁc qubit Qi’s frequency ωi , while the entangling two-qubit CR gates are implemented by driving a control qubit
Qc at the frequency ωt of the target qubit Qt, where i, c, t ∈{1, 2, 3, 4, 5, 6}. The state of each qubit is measured at its readout
resonator frequency ωMi. The reﬂected readout signals are ampliﬁed ﬁrst by a JPC, pumped at a frequency ωP i, followed by
HEMT ampliﬁers at 4K.

## TABLE S1.

Page: 8
Caption bbox: (54.0, 172.7, 562.1, 202.5)
Crop bbox: (66.0, 44.3, 550.0, 168.7)
Crop asset: ../figure-crops/arxiv_1704.05018/page_008_figure_01.png

Caption:

TABLE S1.
Qubit and readout characterization. Qubit transitions (ω01/2π), average relaxation times (T1), average
coherence times (T2, T ∗
2 ), readout resonator frequencies (ωr/2π), qubit anharmonicity (δ/2π), readout assignment errors (ϵr)
for the six qubits discussed in the paper.

## FIG. S2.

Page: 8
Caption bbox: (54.0, 524.0, 562.2, 574.8)
Crop bbox: (66.0, 44.3, 550.0, 518.6)
Crop asset: ../figure-crops/arxiv_1704.05018/page_008_figure_02.png

Caption:

FIG. S2.
Asymmetric transmon and tuning curve a False-colored optical micrograph of an asymmetric transmon, with
an Al SQUID loop (in green), shunted by Nb capacitor pads (in blue). b Qubit frequency versus ﬂux for the asymmetric
transmon Q4. A constant ﬂux oﬀset is subtracted, and the ﬂux is expressed in units of the ﬂux quantum Φ0 = h/2e, where h
is Planck’s constant, and e is electric charge. The qubit is operated at its upper ﬂux sweet spot, indicated by the arrow. The
dashed line is a guide to the eye.

## FIG. S3.

Page: 9
Caption bbox: (54.0, 252.0, 562.2, 282.2)
Crop bbox: (84.0, 44.1, 532.0, 246.6)
Crop asset: ../figure-crops/arxiv_1704.05018/page_009_figure_01.png

Caption:

FIG. S3.
Single qubit gate drifts Repeated calibrations of the amplitude for a Xπ pulse over 18 hours for Q1-4 (a-d) reveal
the magnitude and timescale for drifts in the amplitude of the single qubit gates. Here, the amplitude drifts are scaled as angle
deviations ∆θ from the starting Xπ-rotation.

## Algorithm 1

Page: 9
Caption bbox: (54.0, 406.9, 408.9, 416.8)
Crop bbox: (46.0, 44.1, 570.1, 402.9)
Crop asset: ../figure-crops/arxiv_1704.05018/page_009_figure_02.png

Caption:

Algorithm 1 Hardware-eﬃcient optimization of quantum Hamiltonian problems

## FIG. S4.

Page: 12
Caption bbox: (54.0, 385.5, 562.2, 458.7)
Crop bbox: (48.0, 35.1, 582.3, 380.1)
Crop asset: ../figure-crops/arxiv_1704.05018/page_012_figure_01.png

Caption:

FIG. S4.
Dependence of energy error on entangler phase a Energy error of numerical optimizations, as a function of
the phase of the entanglers, for diﬀerent depths d = 1, 2, 3, 4, 6, 8. The energy error is averaged over 10 optimization runs, for
each depth, with bands represent the standard deviation of the distribution. The dashed vertical lines indicate approximate
gate phases of the individual CR gates for the gate time of 150 ns, including ﬁnite pulse ramping times. b Norm of the Bloch
vector ||⃗R|| as a function of gate time for all the two-qubit entangling gates used in the experiment. The black dashed line
corresponds to a gate time of 150 ns. The points where ||⃗R|| = 0 indicate gate times of maximal entanglement. c Concurrence
v/s gate phase of a ZX gate, starting from the state (| 10⟩+ | 00⟩)
√

## FIG. S5.

Page: 14
Caption bbox: (54.0, 328.7, 561.6, 339.1)
Crop bbox: (48.0, 44.1, 568.0, 324.7)
Crop asset: ../figure-crops/arxiv_1704.05018/page_014_figure_01.png

Caption:

FIG. S5.
Energy variance Numerical computation of the variance of the mean energy ϵ2, as in Eq. (18), with S = 103

## FIG. S6.

Page: 16
Caption bbox: (54.0, 260.6, 562.2, 339.5)
Crop bbox: (19.9, 19.8, 545.7, 256.6)
Crop asset: ../figure-crops/arxiv_1704.05018/page_016_figure_01.png

Caption:

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

## FIG. S7.

Page: 18
Caption bbox: (54.0, 217.9, 562.2, 258.2)
Crop bbox: (84.0, 44.1, 550.4, 212.5)
Crop asset: ../figure-crops/arxiv_1704.05018/page_018_figure_01.png

Caption:

FIG. S7.
Scaling of resources to reach chemical accuracy. a The critical depth required for reaching chemical accuracy
for the 3 molecules discussed in the paper, using an all-to-all qubit connectivity (blue) and the experimental qubit connectivity
(red). b The number of function calls for reaching chemical accuracy for the 3 molecules at their respective critical depths from
a. Each data point in both plots is obtained by averaging over 10 optimization runs.

## FIG. S8.

Page: 19
Caption bbox: (54.0, 311.7, 562.2, 352.1)
Crop bbox: (8.0, 8.0, 604.0, 307.7)
Crop asset: ../figure-crops/arxiv_1704.05018/page_019_figure_01.png

Caption:

FIG. S8.
Scaling of energy error with noise strength Error in the energy estimate for the 4-qubit LiH Hamiltonian at
its bond length, for diﬀerent depolarizing noise strengths of the model in Eq. (30), for diﬀerent circuit depths used for trial
state preparation, after 5 × 104 function calls. Each data point is obtained by averaging over 10 optimization runs. The black
dashed line indicates the energy error for chemical accuracy.

## FIG. S9.

Page: 20
Caption bbox: (54.0, 451.7, 562.2, 575.7)
Crop bbox: (84.0, 39.5, 532.8, 446.2)
Crop asset: ../figure-crops/arxiv_1704.05018/page_020_figure_01.png

Caption:

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

## TABLE S2

Page: 21
Caption bbox: (58.7, 55.0, 566.9, 105.8)
Crop bbox: (8.0, 8.0, 604.0, 51.0)
Crop asset: ../figure-crops/arxiv_1704.05018/page_021_figure_01.png

Caption:

TABLE S2: The H2, LiH and BeH2 Hamiltonians at the bond distance. Listed are all the Pauli operators, grouped in the
diﬀerent TPB sets, with the corresponding coeﬃcients, not taking into account for the energy shifts due to the ﬁlling of inner
orbitals and the Coulomb repulsion between nuclei. X,Y,Z,I here stand for the Pauli matrices σx, σy, σz and the identity
operator on a single qubit subspace, respectively. There are 2,25,44 TPB sets for H2, LiH and BeH2, respectively with 4, 99
and 164 Pauli terms in total.
