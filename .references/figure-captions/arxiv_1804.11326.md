---
source_pdf: ../arxiv_1804.11326.pdf
pages: 22
captions: 17
extracted_at: 2026-04-17T12:32:33+00:00
extractor: PyMuPDF (fitz)
---

# arxiv_1804.11326 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## FIG. 1.

Page: 2
Caption bbox: (54.0, 213.7, 562.2, 306.3)
Crop bbox: (81.1, 48.8, 540.4, 203.4)
Crop asset: ../figure-crops/arxiv_1804.11326/page_002_figure_01.png

Caption:

FIG. 1.
Quantum Kernel Functions: (a) Feature map representation for a single qubit. A classical dataset in the interval
Ω= (0, 2π] with binary labels (a, right) can be mapped onto the Bloch sphere (red / blue - lines) by using the non-linear
feature map described in (b). For a single qubit UΦ(x) = Zx is a phase-gate of angle x ∈Ω. The mapped data can be separated
by the hyperplane given by normal ⃗w. States with a positive expectation value of ⃗w receive a [+1] (red) label, while negative
values are labeld [−1](blue). (b) For the general circuit UΦ(⃗x) is formed by products of single- and two-qubit unitaries that
are diagonal in the computational basis. In our experiments, both the training and testing data is artiﬁcially generated to be
perfectly classiﬁable with the aforementioned feature map. The circuit family depends non-linearly on the data through the
coeﬃcients φS(⃗x) with |S| ≤2. (c) Experimental implementation of the parameterized diagonal two-qubit operations using
CNOTs and Z−gates.

## FIG. 2.

Page: 3
Caption bbox: (317.0, 257.6, 562.2, 337.1)
Crop bbox: (316.9, 53.2, 562.2, 249.8)
Crop asset: ../figure-crops/arxiv_1804.11326/page_003_figure_01.png

Caption:

FIG. 2.
Experimental implementations (a) Schematic
of the 5-qubit quantum processor. The experiment was per-
formed on qubits Q0 and Q1, highlighted in the image. (b)
Variational circuit used for our optimization method. Here
we choose a rather common Ansatz for the variational unitary
W(⃗θ) = U (l)
loc(θl) Uent . . . U (2)
loc (θ2) Uent U (1)
loc (θ1) [16, 17]. We
alternate layers of entangling gates Uent = Q

## FIG. 3.

Page: 4
Caption bbox: (54.0, 238.8, 562.2, 392.5)
Crop bbox: (8.0, 8.0, 604.0, 234.8)
Crop asset: ../figure-crops/arxiv_1804.11326/page_004_figure_01.png

Caption:

FIG. 3.
Convergence of the method and classiﬁcation results: (a) Convergence of the cost function Remp(⃗θ) after
250 iterations of Spall’s SPSA algorithm. Red (black) curves correspond to l = 4 (l = 0). The value of the cost function,
obtained from estimates of ˆpk after zero-noise extrapolation (solid lines), is compared with values obtained from experimental
measurements of ˆpk with standard single and two-qubit gate times (dashed). We train three sets of data per depth and perform
20 classiﬁcations per trained set.
The results of these classiﬁcations are shown in (c) as black dots (amounting to 60 per
depth), with mean values at each depth represented by red dots. The error bar is the standard error of the mean. The inset
shows histograms as a function of the probability of measuring label +1 for a test set of 20 points per label obtained with a
l = 4 classiﬁer circuit, depicting classiﬁcation with 100% success.. The dashed blue lines show the results of our direct kernel
estimation method for comparison, with Sets I and II yielding 100% success and Set III yielding 94.75% success. (b) Example
data set used for both methods in this work. The data labels (red for +1 label and blue for −1 label) are generated with a
separation gap of magnitude 0.3 between them (white areas). The 20 points per label training set is shown as white and black
circles. For our quantum kernel estimation method we show the obtained support vectors (green circles) and a classiﬁed test
set (white and black squares). Three of the test sets points are misclasiﬁed, labeled as A, B, and C. For each of the test data
points ⃗xj we plot at the bottom of (b) the amount P

## FIG. 4.

Page: 5
Caption bbox: (317.0, 225.5, 562.1, 320.4)
Crop bbox: (325.6, 47.1, 555.0, 218.9)
Crop asset: ../figure-crops/arxiv_1804.11326/page_005_figure_01.png

Caption:

FIG. 4.
Kernels for Set III. (a) Experimental (left) and
ideal (right) kernel matrices containing the inner products of
all data points used for training Set III (round symbols in Fig.
3 (b)). The maximal deviation from the ideal kernel |K −ˆK|
occurs at element K8,15. A cut through row 8 (indicated by
red arrow in (a)) is shown in (b), where the experimental
(ideal) results are shown as red (blue) bars. Note that entries
that are close zero in the kernel can become negative (c.f.
K8,30 (b)) when the error-mitigation technique is applied.

## FIG. S1.

Page: 8
Caption bbox: (54.0, 405.8, 562.1, 428.9)
Crop bbox: (8.0, 8.0, 604.0, 401.8)
Crop asset: ../figure-crops/arxiv_1804.11326/page_008_figure_01.png

Caption:

FIG. S1.
Quantum variational classiﬁcation: The circuit takes a references state, | 0⟩n, applies the unitary UΦ(vecx) fol-
lowed by the variational unitary W(⃗θ) and applies a measurement in the Z-basis.
The resulting bit string z ∈{0, 1}n

## Algorithm 1

Page: 8
Caption bbox: (54.0, 487.6, 353.9, 497.5)
Crop bbox: (46.0, 281.4, 570.1, 483.6)
Crop asset: ../figure-crops/arxiv_1804.11326/page_008_figure_02.png

Caption:

Algorithm 1 Quantum variational classiﬁcation: the training phase

## Algorithm 2

Page: 9
Caption bbox: (54.0, 102.2, 374.5, 112.1)
Crop asset: none

Caption:

Algorithm 2 Quantum variational classiﬁcation: the classiﬁcation phase

## FIG. S2.

Page: 14
Caption bbox: (54.0, 195.0, 562.2, 237.2)
Crop bbox: (8.0, 8.0, 604.0, 191.0)
Crop asset: ../figure-crops/arxiv_1804.11326/page_014_figure_01.png

Caption:

FIG. S2.
A circuit representation of the feature map family we consider here. We ﬁrst apply a series of Hadamard gates before
applying the diagonal phase gate component. Then we apply a second layer of Hadamard gates, followed by the same diagonal
phase gate. This encodes both the actual function value of the phase Φ⃗x(z) as well as the value of the ZN
2 Fourier transform
ˆΦ⃗x(S) for every basis element.

## FIG. S3.

Page: 15
Caption bbox: (54.0, 649.9, 562.2, 690.6)
Crop bbox: (8.0, 8.0, 604.0, 645.9)
Crop asset: ../figure-crops/arxiv_1804.11326/page_015_figure_01.png

Caption:

FIG. S3.
(a) Circuit representation of short depth quantum circuit to deﬁne the separating hyperplane. The single qubit
rotations U(θi,t) ∈SU(2) are depicted by single line boxes parametrized by the angles θi, while the entangling operation Uent
is determined by the interaction graph of the superconducting chip. (b) Depiction of entangling gate as a product of CZi,i+1
for i = 1, . . . , 5 gates following the interaction graph of a circle G = C5.

## Fig. S3.b

Page: 16
Caption bbox: (54.0, 54.3, 562.1, 98.6)
Crop bbox: (8.0, 8.0, 604.0, 50.3)
Crop asset: ../figure-crops/arxiv_1804.11326/page_016_figure_01.png

Caption:

Fig. S3.b, interspersed with single qubit control pulses in SU(2) on every qubit. It is known that this set of drift
steps together with all single control pulses are universal, so we have that any state can be prepared this way with
suﬃcient circuit depth [35]. For a general unitary gate sequence the entangling unitary has to be eﬀectively generated
from cross resonance gates, by applying single qubit control pulses.

## FIG. S4.

Page: 17
Caption bbox: (54.0, 407.7, 562.2, 438.7)
Crop bbox: (8.0, 8.0, 604.0, 403.7)
Crop asset: ../figure-crops/arxiv_1804.11326/page_017_figure_01.png

Caption:

FIG. S4.
Single shot to multi-shot decision rule for classiﬁcation. The contribution to the cost-function interpolates from
linear to logistic-normal CDF (approximately sigmoid). In the experiment the data was sampled with R = O(103), although
the cost-function was evaluated with only ˜R = O(102) to provide a smoother function to the optimization routine.

## FIG. S5.

Page: 18
Caption bbox: (54.0, 567.4, 562.1, 632.5)
Crop bbox: (88.4, 90.9, 523.9, 555.5)
Crop asset: ../figure-crops/arxiv_1804.11326/page_018_figure_01.png

Caption:

FIG. S5.
a) Estimating the expectation value of the SWAP- matrix as derived in [27]. This circuit diagonalizes the SWAP -
gate, when it is treated as a hermitian observables with eigenvalues ±1. Averaging the eigenvalues, c.f. eqn. (36), with samples
from the output distribution constructs an estimator for | ⟨Φ(⃗x) | Φ(⃗y) ⟩|2. b) The ciruit estimates the ﬁdelity between two
states in feature space directly by ﬁrst applying the unitary UΦ(⃗x) followed by the inverse U†
Φ(⃗y) and measuring all bits at the
output of the circuit. The frequency ν0,...,0 = | ⟨Φ(⃗x) | Φ(⃗y) ⟩|2 of the all the zero outcome precisely corresponds to the desired
state overlap.

## TABLE S1.

Page: 20
Caption bbox: (54.0, 363.7, 562.2, 383.2)
Crop bbox: (8.0, 8.0, 604.0, 359.7)
Crop asset: ../figure-crops/arxiv_1804.11326/page_020_figure_01.png

Caption:

TABLE S1.
RB of our single-qubit gates. Qubit labels indicate which qubit was bencharmked on each case, with label 11
indicating simultaneous RB.

## TABLE S2.

Page: 21
Caption bbox: (54.0, 331.8, 562.1, 351.2)
Crop bbox: (8.0, 8.0, 604.0, 327.8)
Crop asset: ../figure-crops/arxiv_1804.11326/page_021_figure_01.png

Caption:

TABLE S2.
Suport vectors for all three data sets used for our kernel estimation method, as shown as green circles in Figs. 3
(b) and S6.

## FIG. S6.

Page: 21
Caption bbox: (59.6, 581.8, 556.6, 590.8)
Crop bbox: (45.6, 44.3, 570.9, 577.1)
Crop asset: ../figure-crops/arxiv_1804.11326/page_021_figure_02.png

Caption:

FIG. S6.
Sets I (a) and II (b), including training data points (white and black circles) and support vectors (green circles).

## FIG. S7.

Page: 22
Caption bbox: (54.0, 253.0, 562.2, 273.7)
Crop bbox: (48.5, 45.5, 566.7, 244.8)
Crop asset: ../figure-crops/arxiv_1804.11326/page_022_figure_01.png

Caption:

FIG. S7.
Experimentally estimated and ideal kernel matrices for Sets I (a, b) and II (c, d). For both datasets we show a cut
(b, d) through the row at which the maximum of | ˆK −K| occurs, similarly as in Fig. 4 in the main text.

## FIG. S8.

Page: 22
Caption bbox: (54.0, 480.3, 562.1, 510.3)
Crop bbox: (48.5, 45.5, 566.7, 468.5)
Crop asset: ../figure-crops/arxiv_1804.11326/page_022_figure_02.png

Caption:

FIG. S8.
Inner products between experimentally obtained hyperplanes and the ideal for each training set. The x−axis shows
the results for the two diﬀerent time stretches used in our experiments, c1 and c1.5, corresponding to the faster and slower
gates, respectively. We also show the error-mitigated hyperplanes inner products.
