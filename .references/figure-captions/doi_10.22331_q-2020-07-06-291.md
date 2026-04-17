---
source_pdf: ../doi_10.22331_q-2020-07-06-291.pdf
pages: 20
captions: 21
extracted_at: 2026-04-17T12:32:48+00:00
extractor: PyMuPDF (fitz)
title: "Option Pricing using Quantum Computers"
author: "Nikitas Stamatopoulos, Daniel J. Egger, Yue Sun, Christa Zoufal, Raban Iten, Ning Shen, Stefan Woerner, "
---

# doi_10.22331_q-2020-07-06-291 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## Table 1

Page: 3
Caption bbox: (205.4, 67.3, 389.9, 76.3)
Crop bbox: (307.6, 8.0, 541.5, 63.3)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_003_figure_01.png

Caption:

Table 1: Example of the diﬀerent option types.

## Figure 1

Page: 3
Caption bbox: (56.7, 303.3, 287.7, 323.2)
Crop bbox: (104.3, 70.8, 328.3, 293.1)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_003_figure_02.png

Caption:

Figure 1:
The quantum circuit of amplitude estimation,
where H denotes a Hadamard gate and F † the inverse QFT.

## Figure 2

Page: 5
Caption bbox: (56.7, 120.9, 287.7, 195.6)
Crop bbox: (67.6, 57.7, 294.7, 116.9)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_005_figure_01.png

Caption:

Figure 2: Quantum circuit that creates the state in Eq. (9).
Here, the independent variable i = 4i2 +2i1 +i0 ∈{0, ..., 7}
is encoded by three qubits in the state |i⟩3 = |i2i1i0⟩with
ik ∈{0, 1}. Therefore, the linear function f(i) = f1i + f0 is
given by 4f1i2 +2f1i1 +f1i0 +f0. After applying this circuit
the quantum state is |i⟩3 [cos(f1i+f0) |0⟩+sin(f1i+f0) |1⟩].
The circuit on the right shows an abbreviated notation.

## Figure 3

Page: 6
Caption bbox: (56.7, 236.4, 287.7, 278.3)
Crop bbox: (56.7, 48.7, 296.0, 232.4)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_006_figure_01.png

Caption:

Figure 3: Example price distribution at maturity loaded in a
three-qubit register. In this example we followed the Black-
Scholes-Merton model which implies a log-normal distribu-
tion of the asset price at maturity T with probability density

## Figure 4

Page: 7
Caption bbox: (56.7, 234.4, 538.6, 309.3)
Crop bbox: (8.0, 8.0, 587.3, 230.4)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_007_figure_01.png

Caption:

Figure 4: Circuit that compares the value represented by an n-qubit register |i⟩n, to a ﬁxed value K. We use n ancilla qubits
|a1, ..., an⟩, a classical array t[n] holding the precomputed binary value of K’s two’s complement and a qubit |c⟩which will
hold the result of the comparison with |c⟩= 1 if |i⟩≥K. For each qubit |ik⟩, with k ∈{1, ..., n}, we use a Toﬀoli gate to
compute the carry at position k if t[k] = 1 and a logical OR, see Fig. 5, if t[k] = 0. For k = 1, we only need to use a CNOT
on |i1⟩if t[1] = 1. In the circuit above, only one of two unitaries in a dotted box needs to be added to the circuit, depending
on the value of t[k] at each qubit. The last carry qubit |an⟩is then used to compute the ﬁnal result of the comparison in
qubit |c⟩.

## Figure 5

Page: 7
Caption bbox: (56.7, 420.6, 287.7, 451.4)
Crop bbox: (91.2, 87.4, 287.7, 404.7)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_007_figure_02.png

Caption:

Figure 5:
Circuit that computes the logical OR between
qubits |a⟩and |b⟩into qubit |c⟩. The circuit on the right
shows the abbreviated notation used in Fig. 4.

## Figure 6

Page: 7
Caption bbox: (56.7, 655.0, 287.7, 718.9)
Crop bbox: (91.2, 87.4, 287.7, 643.5)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_007_figure_03.png

Caption:

Figure 6: Quantum circuit that sets a comparator qubit |c⟩
to |1⟩if the value represented by |i⟩3 is larger than a strike
K = 1.9, for the spot distribution in Fig. 3. The unitary PX
represents the set of gates that load the probability distribu-
tion in Eq. (14). An ancilla qubit |a⟩is needed to perform
the comparison. It is uncomputed at the end of the circuit.

## Figure 7

Page: 7
Caption bbox: (307.6, 395.0, 538.6, 447.8)
Crop bbox: (307.6, 87.4, 484.1, 389.3)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_007_figure_04.png

Caption:

Figure 7:
Circuit that creates the state in Eq. (18). We
apply this circuit directly after the comparator circuit shown
in Fig. 6. The multi-controlled y-rotation is the gate shown
in Fig. 2 controlled by the ancilla qubit |c⟩that contains the
result of the comparison between i and K.

## Figure 8

Page: 8
Caption bbox: (56.7, 403.4, 287.7, 522.0)
Crop bbox: (56.7, 48.7, 287.7, 399.4)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_008_figure_01.png

Caption:

Figure 8:
Results from applying amplitude estimation
(Sec. 3.1) on a European call option with spot price dis-
tribution as given in Fig. 3 and a strike price K = 2.0, on
a simulated quantum device with m ∈{3, 5, 7, 9} sampling
qubits, i.e., M ∈{8, 32, 128, 512} quantum samples. The
red dashed line corresponds to the (undiscounted) analyti-
cal value for this option, calculated using the Black-Scholes-
Merton model. We limit the range of possible option values
shown to [0, 0.3] to illustrate the convergence of the esti-
mation, as the cumulative probability in the windows shown
exceeds 90% in each case.

## Figure 9

Page: 8
Caption bbox: (307.6, 165.0, 538.6, 195.9)
Crop bbox: (307.6, 8.0, 538.6, 161.0)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_008_figure_02.png

Caption:

Figure 9:
Quantum circuit that implements the multi-
controlled Y-rotations for a portfolio of options with m strike
prices.

## Figure 10

Page: 9
Caption bbox: (307.6, 199.5, 538.6, 340.0)
Crop bbox: (330.9, 59.8, 512.3, 194.2)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_009_figure_01.png

Caption:

Figure 10:
Schematic of the circuit that encodes the pay-
oﬀof a basket call option of d underlying assets into the
amplitude of a payoﬀqubit |p⟩. First, a unitary PX loads
the multivariate distribution of Eq. (28) into d registers
|i1⟩n1 . . . |id⟩nd using the methods described in Sec. 3.2. The
weighted sum operator S, see Appendix A, calculates the
weighted sum |w1 · i1 + . . . + wd · id⟩into a register |b⟩n′
with n′ qubits, where n′ is large enough to hold the maximum
possible sum. The comparator circuit C sets a comparator
qubit |c⟩to |1⟩if b ≥K. Lastly, controlled-Y rotations are
used to encode the option payoﬀf(b) = max(0, b −K) into
the payoﬀqubit using the method shown in Fig. 7, controlled
by the comparator qubit |c⟩.

## Figure 11

Page: 10
Caption bbox: (307.6, 225.6, 538.6, 355.1)
Crop bbox: (307.6, 48.7, 538.6, 221.6)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_010_figure_01.png

Caption:

Figure 11: Comparison of the estimation error between Am-
plitude Estimation and Monte Carlo at the 8/π2 ≈81% con-
ﬁdence interval for a basket option consisting of 3 identical,
equally weighted assets with the parameters of Fig. 3, strike
price K = 2.0 and asset correlations ρ12 = ρ13 = ρ23 = 0.8.
The approximation error for amplitude estimation is plotted
against the maximum expected error given by Eq. (31), illus-
trating the O(M −1) convergence. We calculate the equiva-
lent Monte Carlo error at the same 81% conﬁdence interval
over 10,000 simulations for each sample number 2m. The red
dashed line shows a linear ﬁt across the Monte Carlo errors,
displaying the expected O(M −1/2) scaling.

## Figure 12

Page: 11
Caption bbox: (56.7, 226.9, 287.7, 257.8)
Crop bbox: (56.7, 48.7, 287.7, 222.9)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_011_figure_01.png

Caption:

Figure 12: Probability density function of a multivariate log-
normal distribution, see Eq. (28), for the asset shown in Fig. 3
deﬁned on two time steps t = ∆t = T/2 and t = 2∆t = T

## Table 2

Page: 11
Caption bbox: (307.6, 148.5, 538.6, 201.3)
Crop bbox: (307.6, 48.9, 538.6, 135.9)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_011_figure_02.png

Caption:

Table 2: Single-qubit, CNOT, Toﬀoli gate counts and over-
all circuit depth required for the full amplitude estimation
circuits for each instance in Fig. 8, as a function of the num-
ber of sampling qubits m.
These ﬁgures assume all-to-all
connectivity across qubits.

## Figure 13

Page: 12
Caption bbox: (56.7, 210.8, 538.6, 274.7)
Crop bbox: (8.0, 8.0, 587.3, 206.8)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_012_figure_01.png

Caption:

Figure 13:
Circuit that encodes the payoﬀof a Knock-In barrier option in the state of an ancilla qubit |p⟩1. The unitary
operator PX is used to initialize the state of Eq. (25). Comparator circuits CB are used to set a barrier qubit bj for all j ∈[1, d]
if the asset price represented by |ij⟩crosses the barrier B. The logical OR of all bj qubits is computed into ancilla |b|⟩. The
strike comparator circuit CK sets the comparator qubit |c⟩1 to |1⟩if the asset price at maturity |id⟩≥K. Finally, Y-rotations
encode the payoﬀqubit |p⟩1, controlled on |id⟩, the strike qubit |c⟩1 and the barrier qubit |b|⟩which is |1⟩only if the asset
price has crossed the barrier at least once before maturity.

## Figure 14

Page: 12
Caption bbox: (56.7, 460.8, 287.7, 568.4)
Crop bbox: (48.7, 58.9, 442.4, 456.8)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_012_figure_02.png

Caption:

Figure 14: Estimated option price for a barrier option using
amplitude estimation on a quantum simulator. The option
is deﬁned on the asset of Fig. 3 with two timesteps T/2 and
T = 300/365 and 2 qubits used to represent the uncertainty
per timestep. The option strike is K = 1.9 and a barrier
was added at B = 2.0 on both timesteps. The red dotted
line is the (undiscounted) value of the option calculated with
classical Monte Carlo and 100, 000 paths and the blue bars
show the estimated option values using amplitude estimation
with m = 7 sampling qubits.

## Figure 15

Page: 14
Caption bbox: (56.7, 189.7, 538.6, 220.7)
Crop bbox: (8.0, 8.0, 587.3, 185.7)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_014_figure_01.png

Caption:

Figure 15: The A operator of the considered European call option: ﬁrst, the 2-qubit approximation of a log-normal distribution
is loaded, and second, the piecewise linear payoﬀfunction is applied to last qubit controlled by the ﬁrst two. This operator
can be used within amplitude estimation to evaluate the expected payoﬀof the corresponding option.

## Figure 16

Page: 15
Caption bbox: (56.7, 181.4, 538.7, 257.3)
Crop bbox: (54.7, 48.7, 550.0, 175.3)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_015_figure_01.png

Caption:

Figure 16: Error-mitigated hardware results for A |0⟩3, QA |0⟩3 and the estimated option price after applying maximum
likelihood estimation as a function of the initial spot price S0. (a) Probability of measuring |1⟩for the QA |0⟩3 circuit (see
Appendix B, Fig. 15) (b) Probability of measuring |1⟩for the QA |0⟩3 circuit (see Fig. 19). We show the measured probabilities
when replacing each CNOT by one, three and ﬁve CNOT gates (green, orange, red, respectively), the zero-noise limit calculated
using a second-order Richardson extrapolation method (purple), and the probability measured using the simulator (blue). (c)
Option price estimated with maximum likelihood estimation from measurements of QA |0⟩3 and A |0⟩3 with error mitigation
(purple) and without (green). The exact option price for each initial spot price S0 is shown in blue.

## Figure 17

Page: 16
Caption bbox: (56.7, 220.4, 287.7, 319.0)
Crop bbox: (138.9, 53.8, 267.5, 203.3)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_016_figure_01.png

Caption:

Figure 17: Three component gates used to construct the
weighted sum operator S. (a) The carry operator M con-
sisting of one Toﬀoli gate, which computes the carry from
adding |ai⟩(or |cj−1⟩) and |sj⟩into |sj+1⟩or |cj⟩. (b) The
bit addition operator D consisting of one CNOT gate, which
adds the state qubit |ai⟩or the carry qubit from the previ-
ous digit |cj−1⟩to the sum qubit |sj⟩. (c) The carry reset
operator f
M consisting of two X gates and one Toﬀoli gate,
which resets the carry qubit |cj⟩back to |0⟩.

## Figure 18

Page: 17
Caption bbox: (56.7, 239.6, 538.6, 259.6)
Crop bbox: (8.0, 8.0, 587.3, 235.6)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_017_figure_01.png

Caption:

Figure 18: A circuit computing the sum of binary numbers |a⟩3 and |b⟩3 into |s⟩4 implemented using the weighted sum operator
with weights ω = (1, 2, 4, 1, 2, 4).

## Figure 19

Page: 18
Caption bbox: (56.7, 239.6, 538.6, 271.8)
Crop bbox: (53.8, 61.9, 541.5, 232.0)
Crop asset: ../figure-crops/doi_10.22331_q-2020-07-06-291/page_018_figure_01.png

Caption:

Figure 19: The optimized circuit for QA |0⟩3 used for the experiments on real quantum hardware. It requires 18 CNOT gates
and 33 single qubit gates. The initial spot price is assumed to be equal to 2. The dashed boxes indicate which parts are used
for A, A†, Sψ0, and S0. Note that due to the circuit optimization, some boxes are slightly overlapping.
