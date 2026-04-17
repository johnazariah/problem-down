---
source_pdf: ../arxiv_2012.09265.pdf
pages: 33
captions: 7
extracted_at: 2026-04-17T12:32:40+00:00
extractor: PyMuPDF (fitz)
---

# arxiv_2012.09265 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## FIG. 1.

Page: 2
Caption bbox: (54.0, 227.9, 562.2, 320.6)
Crop bbox: (46.0, 44.1, 570.1, 222.5)
Crop asset: ../figure-crops/arxiv_2012.09265/page_002_figure_01.png

Caption:

FIG. 1. Schematic diagram of a Variational Quantum Algorithm (VQA). The inputs to a VQA are: a cost function
C(θ), with θ a set of parameters that encodes the solution to the problem, an ansatz whose parameters are trained to minimize
the cost, and (possibly) a set of training data {ρk} used during the optimization. Here, the cost can often be expressed in
the form in Eq. (3), for some set of functions {fk}. Also, the ansatz is shown as a parameterized quantum circuit (on the
left), which is analogous to a neural network (also shown schematically on the right). At each iteration of the loop one uses
a quantum computer to eﬃciently estimate the cost (or its gradients). This information is fed into a classical computer that
leverages the power of optimizers to navigate the cost landscape C(θ) and solve the optimization problem in Eq. (1). Once a
termination condition is met, the VQA outputs an estimate of the solution to the problem. The form of the output depends
on the precise task at hand. The red box indicates some of the most common types of outputs.

## FIG. 2.

Page: 3
Caption bbox: (317.0, 258.1, 562.1, 308.9)
Crop bbox: (317.0, 44.4, 562.1, 252.4)
Crop asset: ../figure-crops/arxiv_2012.09265/page_003_figure_01.png

Caption:

FIG. 2. Schematic diagram of an ansatz. The unitary
U(θ), with θ a set of parameters, can be expressed as a prod-
uct of L unitaries Ul(θl) sequentially acting on an input state.
As indicated, each unitary Ul(θl) can in turn be decomposed
into a sequence of parametrized and unparametrized gates.

## FIG. 3.

Page: 7
Caption bbox: (317.0, 271.9, 562.1, 312.3)
Crop bbox: (317.0, 43.9, 562.1, 266.1)
Crop asset: ../figure-crops/arxiv_2012.09265/page_007_figure_01.png

Caption:

FIG. 3.
Applications of Variational Quantum Algo-
rithms (VQAs). Many applications have been envisioned
for VQAs. Here we show some of the key applications that
are discussed in this Review.

## FIG. 4.

Page: 8
Caption bbox: (54.0, 291.3, 299.1, 491.1)
Crop bbox: (70.7, 44.1, 282.6, 285.9)
Crop asset: ../figure-crops/arxiv_2012.09265/page_008_figure_01.png

Caption:

FIG. 4. Variational Quantum Eigensolver (VQE) im-
plementation. The VQE algorithm can be used to estimate
the ground state energy EG of a molecule. The interactions of
the system are encoded in a Hamiltonian H, usually expressed
as a linear combination of simple operators hk with coeﬃ-
cients ck. Taking H as input, VQE outputs an estimate eEG
of the ground-state energy. The lower part of the ﬁgure shows
the results of a VQE implementation for the electronic struc-
ture problem of an H2 molecule, whose exact energy is shown
as a dashed line. The experimental results were obtained us-
ing two of the ﬁve qubits in one of IBM’s superconducting
quantum processors (the inset illustrates qubit connectivity
with Q0 . . . Q4 denoting the qubits ). Due to the presence of
hardware noise the estimated energy eEG has a gap with the
true energy. In fact, amplifying the noise strength (that is
increasing the quantity s), deteriorates the solution quality.
However, as discussed below, one can use error mitigation
techniques to improve the solution quality. Figure adapted
from Ref. [106], Springer Nature Limited.

## FIG. 5.

Page: 10
Caption bbox: (317.0, 207.0, 562.1, 362.4)
Crop bbox: (333.5, 44.1, 545.6, 203.0)
Crop asset: ../figure-crops/arxiv_2012.09265/page_010_figure_01.png

Caption:

FIG. 5.
Quantum Approximate Optimization Algo-
rithm (QAOA). a. Schematic representation of the Trot-
terized adiabatic transformation in the ansatz.
The algo-
rithm only loosely follows the evolution of the ground state of
H(t) = (1−t)HM +tHP for every t ∈[0, 1], as one is interested
in making the ﬁnal state close to the ground state of the prob-
lem Hamiltonian HP , with HM being a mixer Hamiltonian.
The free parameters {βl}p
l=1 and {γl}p
l=1 are trained, with p
being the number of QAOA rounds. b. Problem Hamilto-
nian HP and graph ⟨jk⟩for a Max-Cut task. Each node in
the graph (circle) represents a spin. Vertices connecting two
nodes indicate an interaction σz
j σz
k in HP , with σz
k the Pauli
z operator on spin k. The solution is encoded in the ground
state of HP where some spins are pointing up (green) whereas
others point down (blue).

## FIG. 6.

Page: 16
Caption bbox: (54.0, 167.8, 299.1, 333.6)
Crop bbox: (0.0, 8.0, 612.0, 163.8)
Crop asset: ../figure-crops/arxiv_2012.09265/page_016_figure_01.png

Caption:

FIG. 6.
Barren plateau (BP) phenomenon.
a.
Vari-
ance of the cost function partial derivative, Var(∂θ1,1E), for
a particular parameter θ1,1 in the ansatz versus number of
qubits (n). Results were obtained from a Variational Quan-
tum Eigensolver implementation with a deep unstructured
ansatz. The y-axis is on a log scale. As the number of qubits
increases the variance vanish exponentially with the system
size. b. Visualization of the landscape of a global cost func-
tion which exhibits a BP for the quantum compilation imple-
mentation, . The orange (blue) landscape was obtained for
n = 24 (n = 4) qubits. As the number of qubits increases,
the landscape becomes ﬂatter. Moreover, this cost also ex-
hibits the narrow gorge phenomenon [166], where the volume
of parameters leading to small cost values shrinks exponen-
tially with n. Panel a is adapted from Ref. [194], CC BY 4.0;
Panel b is adapted from Ref. [166], CC BY 4.0.

## FIG. 7.

Page: 20
Caption bbox: (54.0, 208.3, 299.1, 321.9)
Crop bbox: (0.0, 0.0, 389.2, 199.1)
Crop asset: ../figure-crops/arxiv_2012.09265/page_020_figure_01.png

Caption:

FIG. 7. Qubit trajectories on the Bloch sphere with
the Zero-Noise Extrapolation (ZNE) technique. The
accuracy of a noisy quantum computer can be improved with
the ZNE error mitigation method.
a.
Here, one repeats a
given calculation with diﬀerent levels of noise.
The green
curve corresponds to a rotation on the Bloch sphere with a
higher noise level than that leading to the red curve. b. Tak-
ing data from the red and green curves, ZNE can be used
to estimate what the trajectory (blue) would be like in the
absence of noise. Adapted from Ref. [106], Springer Nature
Limited.
