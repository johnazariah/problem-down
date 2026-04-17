---
source_pdf: ../arxiv_quant-ph_0112176.pdf
pages: 18
extracted_at: 2026-04-17T12:32:46+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "arXiv:quant-ph/0112176v1  30 Dec 2001"
---

# arxiv_quant-ph_0112176

Original title: arXiv:quant-ph/0112176v1  30 Dec 2001

Source PDF: ../arxiv_quant-ph_0112176.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Experimental realization of Shor’s quantum factoring algorithm

using nuclear magnetic resonance

Lieven M.K. Vandersypen†,∗, Matthias Steﬀen∗,†, Gregory Breyta†,
Costantino S. Yannoni†, Mark H. Sherwood† and Isaac L. Chuang∗,†

arXiv:quant-ph/0112176v1 30 Dec 2001

† IBM Almaden Research Center,
San Jose, CA 95120
∗Solid State and Photonics Laboratory,
Stanford University,
Stanford, CA 94305-4075

1

## Page 2

2

The number of steps any classical computer requires in order to ﬁnd the prime

factors of an l-digit integer N increases exponentially with l, at least using algo-

rithms [1] known at present. Factoring large integers is therefore conjectured to be

intractable classically, an observation underlying the security of widely used crypto-

graphic codes [1, 2]. Quantum computers [3], however, could factor integers in only

polynomial time, using Shor’s quantum factoring algorithm [4, 5, 6]. Although im-

portant for the study of quantum computers [7], experimental demonstration of this

algorithm has proved elusive [8, 9, 10].
Here we report an implementation of the

simplest instance of Shor’s algorithm: factorization of N=15 (whose prime factors are

3 and 5). We use seven spin-1/2 nuclei in a molecule as quantum bits [11, 12], which

can be manipulated with room temperature liquid state nuclear magnetic resonance

techniques. This method of using nuclei to store quantum information is in principle

scalable to many quantum bit systems [13], but such scalability is not implied by the

present work. The signiﬁcance of our work lies in the demonstration of experimen-

tal and theoretical techniques for precise control and modelling of complex quantum

computers. In particular, we present a simple, parameter-free but predictive model

of decoherence eﬀects [14] in our system.

Shor’s factoring algorithm works by utilizing a quantum computer to quickly determine the

period of the function f(x) = ax mod N (the remainder of ax divided by N), where a is a randomly

chosen small number with no factors in common with N; from this period, number-theoretic

techniques can be employed to factor N with high probability [4]. The two main components of the

algorithm, modular exponentiation (computation of ax mod N) and the inverse quantum Fourier

transform (QFT) take only O(l3) operations [4, 5, 6]. Classically, in contrast, prime factorization

takes O(2l1/3) operations [1], which quickly becomes intractable as l increases.

The simplest meaningful instance of Shor’s algorithm is factorization of N = 15 [7] — the algo-

rithm fails for N even or a prime power. Even for such a small N, quantum factorization poses at

## Page 3

3

present a signiﬁcant experimental challenge: it requires coherent control over seven quantum bits

(qubits) in the course of a long sequence of controlled interactions, even after maximal reduction

of the quantum circuit; including the state initialization, interactions between almost all pairs of

qubits are needed. In comparison with earlier work [8, 9, 10], this experiment thus puts extraordi-

narily high demands on the spin-spin coupling network, the degree of control over the Hamiltonian

and the spin coherence times. Furthermore, numerically predicting the outcome of these experi-

ments has been considered impractical due to the enormous size of the state space transformations,

which are described by ∼47 × 47 real parameters if decoherence eﬀects are included.

Implementation of the algorithm can be broken into four distinct steps (Fig. 1a), with

the most complex being the computation of f(x) = ax mod N for 2n values of x in paral-

lel.
Following standard classical circuit techniques, this is performed by utilizing the identity

ax = a2n−1xn−1 . . . a2x1ax0, where xk are the binary digits of x. Modular exponentiation thus con-

sists of serial multiplication by a2k mod N for all k (0 ≤k ≤n−1) for which |xk⟩= |1⟩. The powers

a2k can be eﬃciently pre-computed on a classical machine by repeated squaring of a. For N = 15,

a may be 2, 4, 7, 8, 11, 13 or 14. If we happen to pick a = 2, 7, 8 or 13, we ﬁnd that a4 mod 15 = 1,

and therefore all a2k mod N = 1 for k ≥2. In this case, f(x) simpliﬁes to multiplications controlled

by just two bits, x0 and x1. If a = 4, 11 or 14, then a2 mod 15 = 1, so only x0 is relevant. Thus,

the ﬁrst register can be as small as two qubits (n = 2); however, three qubits (n = 3) allow for

the possibility of detecting more periods and thus constitutes a more stringent test of the modular

exponentiation and QFT [15]. Together with the m = ⌈log2 15⌉= 4 qubits to hold f(x), we need

seven qubits in total (Fig. 1b). We implemented this algorithm and tested it on two representative

parameter choices: a = 11 (an “easy” case) and a = 7 (a “diﬃcult” case).

The custom-synthesized molecule used as the quantum computer for this experiment contains

ﬁve 19F and two 13C spin-1/2 nuclei as qubits (Fig. 2). In a static magnetic ﬁeld, each spin has

two discrete energy eigenstates, |0⟩(spin-up) and |1⟩(spin-down), described by the Hamiltonian

H0 = −P
i ¯hωiIzi, where ωi/2π is the transition frequency between |0⟩and |1⟩and Iz is the ˆz

component of the spin angular momentum operator. All seven spins in this molecule are remarkably

## Page 4

4

well separated in frequency ωi/2π, and interact pairwise via the J-coupling, described by HJ =

P
i<j 2π¯hJijIziIzj [17].

The desired initial state of the seven qubits is |ψ1⟩= |0000001⟩(Fig. 1). However, experimen-

tally we start from thermal equilibrium. The density matrix is then given by ρth = e−H0/kBT /27,

with kBT ≫¯hωi at room temperature so each spin is in a statistical mixture of |0⟩and |1⟩(Fig. 4a).

We converted ρth into a 7-spin eﬀective pure state [11, 12] ρ1 via temporal averaging [9] (step 0); ρ1

constitutes a suitable initial state for Shor’s factoring algorithm since it generates the same signal

as |ψ1⟩, up to a proportionality constant [11, 12]. While ρ1 is highly mixed and in fact remains

separable under unitary transforms, the observed dynamics under multiple qubit operations such

as in Shor’s algorithm apparently remain hard to simulate classically [18, 19, 20].

The quantum circuit of Fig. 1 was realized with a sequence of ∼300 (a = 7) spin-selective

radio-frequency (RF) pulses separated by time intervals of free evolution under the Hamiltonian

(Fig. 3). The pulse sequence is designed such that the resulting transformations of the spin states

correspond to the computational steps in the algorithm. Upon completion of this sequence, we

estimate the state of the ﬁrst three qubits, ρ ∼P
c wc|c23/r⟩⟨c23/r|, via nuclear magnetic resonance

(NMR) spectroscopy. In the experiment, an ensemble of independent quantum computers rather

than a single quantum computer was used, so the measurement gives the bitwise average value of

8c/r, instead of a sample of 8c/r. This is suﬃcient to determine r in the present experiment, but for

larger N a continued fractions algorithm will need to be performed on the quantum computer [11]

requiring additional qubits. From r, at least one factor of N is given by the greatest common

denominator (gcd) of ar/2 ±1 and N (with probability greater than 1/2); the gcd can be computed

eﬃciently using Euclid’s algorithm on a classical computer [2] .

The experimental spectra acquired upon completion of the easy case (a = 11) of Shor’s algorithm

(Fig. 4c) clearly indicate that qubits 1 and 2 are in |0⟩(spectral lines up), and that 3 is in an equal

mixture of |0⟩and |1⟩(lines up and down, and the integral of the spectrum equal to zero). With

qubit 3 the most signiﬁcant qubit after the inverse QFT [22], the ﬁrst register is thus in a mixture

of |000⟩and |100⟩, or |0⟩and |4⟩in decimal notation. The periodicity in the amplitude of |y⟩

## Page 5

5

is thus 4, so r = 2n/4 = 2 and we ﬁnd that gcd(112/2 ± 1, 15) = 3, 5. The prime factors thus

unambiguously derive from the output spectra.

From analogous spectra for the diﬃcult case (a = 7; Fig. 4d), we see that qubit 1 is in |0⟩, and

qubits 2 and 3 are in a mixture of |0⟩and |1⟩. The register is thus in a mixture of |000⟩, |010⟩, |100⟩

and |110⟩, or |0⟩, |2⟩, |4⟩and |6⟩. The periodicity in the amplitude of |y⟩is now 2, so r = 8/2 = 4

and gcd(74/2 ± 1, 15) = 3, 5. Thus, even after the long and complex pulse sequence of the diﬃcult

case, the experimental data conclusively indicate the successful execution of Shor’s algorithm to

factor 15.

Nevertheless, there are obvious discrepancies between the measured and ideal spectra, most no-

tably for the diﬃcult case. Using a numerical model, we have investigated whether these deviations

could be caused by decoherence. A full description of relaxation for the seven coupled spins involves

almost 47 × 47 degrees of freedom and requires knowledge of physical properties of the molecule

which are not available [23, 24]. In order to get a ﬁrst estimate of the impact of decoherence

during the factoring pulse sequence we assume that each spin experiences independent stochastic

relaxation with correlation time scales ≪1/ωi. This permits the use of the phenomenological

Bloch equations [25], with just two time constants per spin (T1 and T2). We implemented this de-

coherence model for seven coupled spins via the operator sum representation [26] ρ 7→P
k EkρE†
k

(P
k E†
kEk = I), starting from existing single spin models [27] of generalized amplitude damping

(GAD, T1),






1
0

E0 = √

p

0
√

1 −γ

√





1 −γ
0

E2 =
p

1 −p



0
1

and phase damping (PD, related to T2),






1
0

E0 =
√

, E1 =
√

λ

0
1


0
√





γ

, E1 = √

p

,

0
0






0
0

, E3 =
p

1 −p

.
(1)

√

γ
0






1
0

1 −λ

,
(2)

0
−1

with γ = 1 −e−t/T1, p = 1/2 + ¯hω/4kBT and λ ∼(1 + e−t/T2)/2. The following observations

simplify the extension of these separate single spin descriptions to an integrated model for seven

## Page 6

6

spins: (1) GAD (and PD) error operators acting on diﬀerent spins commute; (2) the Ek for GAD

commute with the Ek for PD when applied to arbitrary ρ; and (3) PD commutes with the ideal

unitary time evolution e−iHt (H = H0 + HJ). However, GAD does not commute with e−iHt, and

PD and GAD do not commute with the ideal unitary evolution during RF pulses. Nevertheless,

we have treated these as commuting transformations, such that all of the processes which occur

simultaneously can be modeled sequentially.

Speciﬁcally, the model simulates a delay time of duration td by e−iHtd followed by GAD acting

on spin 1 for a duration td, then GAD acting on spin 2 and so forth, followed by PD acting serially

on each spin. Similarly, a shaped pulse of duration tp was modeled by a delay time of duration

tp (e−iH0tp, GAD and PD) followed by an instantaneous pulse. Using this simple model, the 7-

spin simulation of the complete Shor pulse sequence, including 36 temporal averaging sequences,

required only a few minutes on an IBM quad power3-II processor machine. Measured values of

T1 and T2 (Fig. 2) were used in the model.

The output spectra predicted by this parameter-free decoherence model are also shown in

Figs. 4c and d.
While some discrepancies between the data and the simulations remain (due

to the approximations in the model as well as due to experimental imperfections such as RF inho-

mogeneity, imperfect calibrations, incomplete ﬁeld drift compensation and incomplete unwinding

of coupled evolution during the RF pulses [15]), the model agrees well with the large non-idealities

of the data. The predictive value of the model was further conﬁrmed via independent test experi-

ments.

This is the ﬁrst NMR quantum computation experiment for which decoherence is the dominant

source of errors [8]; the demands of Shor’s algorithm clearly push the limits of the current molecule,

despite its exceptional properties. At the same time, the good agreement between the measured

and simulated spectra suggests that the degree of unitary control in the experiment was very high,

which bodes well for related proposed implementations of quantum computers [28, 29]. Finally, our

parameter-free decoherence model, a predictive tool for modeling quantum errors in this complex

## Page 7

7

system, provides an avenue for future design simulation of quantum computers.

Methods

Experiments were performed at the IBM Almaden Research Center with an 11.7 T (500 MHz)

Oxford Instruments magnet, a custom-modiﬁed four-channel Varian Unity INOVA spectrometer,

and a Nalorac HFX probe. We extended the techniques of Ref. [9] for serving multiple nuclei per

channel, for reducing cross-talk between RF pulses on diﬀerent spins and for sending simultaneous

pulses. We used spin-selective Hermite-180 and Gaussian-90 pulses [17], shaped in 256 steps, with

a duration of 0.22 to ∼2 ms. A technique to compensate for coupling eﬀects during the selective

pulses was developed and implemented via “negative delay” times before and after the pulse.

The amount of negative evolution needed depends on the pulse shape and was pre-computed via

numerical simulations.

To create an eﬀective pure ground state of all seven spins, which has never been done before,

we used a two-stage extension of the scheme of Ref. [9], necessary because ω13C is very diﬀerent

from ω19F. The ﬁve 19F spins are made eﬀective pure via the summation of nine experiments, each

with a diﬀerent sequence of CNij and Ni gates (CNij stands for a controlled-not operation, which

ﬂips the target qubit j if and only if the control i is in |1⟩; Ni simply ﬂips i) [27]. These nine

experiments are executed four times, each time with diﬀerent additional CNij and Ni, such that

the two 13C spins are also made eﬀective pure. Summation of the 4 × 9 = 36 experiments along

with a not on spin 7 gives ρ1. The state preparation sequences were designed to be as short as

possible (∼200 ms) by making optimal use of the available coupling network [15].

Multiplication of y = 1 by a mod 15 controlled by x0 (qubit 3) was replaced by controlled-

addition of (a −1) mod 15. For a = 11, this is done by CN34CN36 and for a = 7 by CN35CN36

(gates A and B of Fig. 1b). Multiplication of y by 72 mod 15 is equivalent to multiplication of

y by 4 mod 15, which reduces to swapping y0 with y2 and y1 with y3. Both swap operations

must be controlled by x1, which can be achieved [30] via gates C, D, E and F, G, H of Fig. 1b.

This quantum circuit can be further simpliﬁed by a quantum analogue to peephole compiler opti-

## Page 8

8

mization [31], which should become standard in future quantum compilers: (1) the control qubit

of gate C is |0⟩, so C was suppressed; (2) similarly, F was replaced by N5; (3) gates H and E

are inconsequential for the ﬁnal state of the ﬁrst register, so they were omitted; (4) the targets

of the doubly controlled not gates D and G are in a basis state, so they can be implemented as

CY †
24CZ2
64CY24 and CY †
27CZ2
57CY27 (CZij stands for a 90◦ˆz rotation of j if and only if i is in

|1⟩); (5) the refocusing schemes were kept as simple as possible. To this end, A was carried out

after E. We did refocus inhomogeneous dephasing for all spins in the transverse plane. Residual

couplings with the cyclopentadienyl protons were decoupled by continuous on-resonance low power

irradiation using a separate power ampliﬁer and additional power combiners and RF ﬁlters. After

all these simpliﬁcations, the pulse sequence for 7x mod 15 was ∼400 ms long. The inverse QFT

was implemented as shown in Fig. 1b and took ∼120 ms. The duration of the complete sequence

for the Shor algorithm was thus up to ∼720 ms. A detailed report on these methods will be

published elsewhere [15].

REFERENCES

[1] Knuth, D.E. The Art of Computer Programming, Vol. 2: Seminumerical Algorithms (Addison-

Wesley, Reading, Mass., 1998).

[2] Koblitz, N. A Course in Number Theory and Cryptography (Springer-Verlag, New York, 1994).

[3] Bennett, C.H. & DiVincenzo, D.P. Quantum information and computation. Nature 404, 247–

255 (2000).

[4] Shor, P. Algorithms for quantum computation: discrete logarithms and factoring. Proc. 35th

Ann. Symp. on Found. of Comp. Sci., 124–134 (IEEE Comp. Soc. Press, Los Alamitos, CA,

1994).

[5] Shor, P. Polynomial-time algorithms for prime factorization and discrete logarithms on a

quantum computer. SIAM J. Computing, 26, 1484–1509 (1997)

[6] Ekert, A. & Jozsa, R. Quantum computation and Shor’s factoring algorithm. Rev. of Mod.

## Page 9

9

Phys. 68, 3, 733–753 (1996).

[7] Beckman, D., Chari, A.N., Devabhaktuni S. & Preskill, J. Eﬃcient networks for quantum

factoring. Phys. Rev. A 54, 1034 (1996).

[8] Jones, J.A. NMR quantum computation. Progr. NMR Spectr., 38, 325–360 (2001).

[9] Vandersypen, L.M.K., et al. Experimental realization of an order-ﬁnding algorithm with an

NMR quantum computer. Phys. Rev. Lett. 85, 5452–5455 (2000).

[10] Knill, E., Laﬂamme, R., Martinez, R. & Tseng, C.-H. An algorithmic benchmark for quantum

information processing. Nature 404, 368–370 (2000).

[11] Gershenfeld N. & Chuang, I.L. Bulk spin-resonance quantum computation. Science 275, 350–

356 (1997).

[12] Cory, D.G., Fahmy, A.F. & Havel, T.F. Ensemble quantum computing by NMR spectroscopy.

Proc. Nat. Acad. Sci. 94, 1634–1639 (1997).

[13] Schulman, L. & Vazirani, U. Molecular Scale Heat Engines and Scalable NMR Quantum

Computation. Proceedings of the 31st ACM Symposium on Theory of Computing 322–329

(1999).

[14] Chuang, I.L., Laﬂamme, R., Shor, P. & Zurek, W.H. Quantum Computers, Factoring, and

Decoherence. Science 270, 1633 (1995).

[15] Steﬀen, et al. in preparation.

[16] Green, M., Mayne, N. & Stone, F.G.A. Chemistry of the metal carbonyls. Part XLVI. Perﬂu-

orobutadienyl iron, rhenium and manganese complexes. J. Chem. Soc. (A), 902–905 (1968).

[17] Freeman, R. Spin Choreography (Spektrum, Oxford, 1997).

[18] Braunstein, S. L. et al. Separability of very noisy mixed states and implications for NMR

quantum computing. Phys. Rev. Lett. 83, 1054–1057 (1999);

[19] Schack, R. and Caves, C. M. Classical model for bulk-ensemble NMR quantum computation.

Phys. Rev. A 60, 4354–4362 (1999).

[20] Linden, N. & Popescu, S. Good Dynamics versus Bad Kinematics: Is Entanglement Needed

for Quantum Computation? Phys. Rev. Lett. 87, 047901 2001

## Page 10

10

[21] Leung, D. W., et. al. Eﬃcient implementation of selective recoupling in heteronuclear spin

systems using Hadamard matrices. Phys. Rev. A 61, 0423101–7.

[22] Coppersmith, D. An approximate Fourier transform useful in quantum factoring. IBM Res.

Rep. RC19642 (1994).

[23] Vold, R.L. & Vold, R.R. Nuclear magnetic relaxation in coupled spin systems. Progr. in NMR

Spectr. 12, 79–133 (1978).

[24] Jeener, J. Superoperators in magnetic resonance. Adv. Magn. Res. 10, 1–51 (1982).

[25] Bloch, F. Nuclear induction. Phys. Rev. 70, 460–474 (1946).

[26] Kraus, K. States, Eﬀects, and Operations: Fundamental Notions of Quantum Theory.

(Springer-Verlag, Berlin, 1983).

[27] M.A. Nielsen & I.L. Chuang. Quantum computation and quantum information. (Cambridge

Univ. Press, Cambridge, England, 2000).

[28] Kane, B.E. A silicon-based nuclear spin quantum computer. Nature 393, 133–137 (1998).

[29] Loss, D. & DiVincenzo, D.P. Quantum computation with quantum dots. Phys. Rev. A 57,

120–126 (1998).

[30] Vandersypen, L.M.K., et al. Implementation of a three-quantum-bit search algorithm. Appl.

Phys. Lett. 76, 646–648 (2000).

[31] Aho, A.V., Sethi R, & Ullman J.D. Compilers: Principles, Techniques and Tools (Addison-

Wesley, 1986).

Acknowledgements

We thank X. Zhou and J. Preskill for useful discussions, J. Smolin for the use of his IBM work-

station, D. Miller for help with spectral analysis, A. Schwartz and his team at Varian for their

generous technical assistance, and J. Harris, W. Risk and H. Coufal for their support. L.V. grate-

fully acknowledges a Yansouni Family Stanford Graduate Fellowship. This work was supported by

## Page 11

11

DARPA under the NMRQC initiative.

Correspondence
and
requests
for
materials
should
be
addressed
to
ILC
(e-mail:

ichuang@media.mit.edu).

## Page 12

12

FIG. 1 a. Outline of the quantum circuit for Shor’s algorithm. Wires represent qubits and boxes

represent operations. Time goes from left to right. (0) Initialize a ﬁrst register of n = 2⌈log2 N⌉

qubits to |0⟩⊗. . . ⊗|0⟩(for short |0⟩) and a second register of m = ⌈log2 N⌉qubits to |0⟩⊗

. . .⊗|0⟩⊗|1⟩(|1⟩). (1) Apply a Hadamard transform H to the ﬁrst n qubits, so the ﬁrst register

reaches P2n−1
x=0 |x⟩/
√

2n. (2) Multiply the second register by f(x) = ax mod N (for some random

a < N which has no common factors with N), to get |ψ2⟩=
P2n−1
x=0 |x⟩|1 × ax mod N⟩/
√

2n .

Since the ﬁrst register is in a superposition of 2n terms |x⟩, the modular exponentiation is

computed for 2n values of x in parallel. (3) Perform the inverse QFT on the ﬁrst register [22],

giving |ψ3⟩= P2n−1
y=0
P2n−1
x=0 e2πixy/2n|y⟩|ax mod N⟩/2n, where interference causes only terms |y⟩

with y = c2n/r (for integer c) to have a substantial amplitude, with r the period of f(x). (4)

Measure the qubits in the ﬁrst register. On an ideal single quantum computer, the measurement

outcome is c2n/r for some c with high probability, and r can be quickly deduced from c2n/r

on a classical computer via continued fractions [2]. b. Detailed quantum circuit for the case

N = 15 and a = 7. Control qubits are marked by •; ⊕represents a not operation and 90

and 45 represent ˆz rotations over these angles. The gates shown in dotted lines can be removed

by optimization and the gates shown in dashed lines can be replaced by simpler gates (see the

methods section).

## Page 13

13

FIG. 2 Structure and properties of the quantum computer molecule, a perﬂuorobutadienyl iron

complex with the inner two carbons 13C-labeled. Based on the measured J13C19F values, we con-

cluded that the placement of the iron is as shown, diﬀerent than derived in Ref.[16] from infrared

spectroscopy. The table gives the ωi/2π at 11.7 T, relative to a reference frequency of ∼470

MHz and ∼125 MHz for 19F and 13C respectively [Hz], the longitudinal (T1, inversion recovery)

and transverse (T2, estimated from a single spin-echo sequence) relaxation time constants [s],

and the J-couplings [Hz]. Ethyl (2-13C)bromoacetate (Cambridge Isotope Laboratories, Inc.)

was converted to ethyl 2-ﬂuoroacetate by heating with AgF followed by hydrolysis to sodium

ﬂuoroacetate using NaOH in MeOH. This salt was converted to 1,1,1,2-tetraﬂuoroethane us-

ing MoF6 and was subsequently treated with two equivalents of BuLi followed by I2 to provide

triﬂuoroiodoethene. Half of the ethene was converted to the zinc salt which was recombined

with the remaining ethene and coupled using Pd(Ph3P)4 to give (2,3-13C)hexaﬂuorobutadiene.

The end product was obtained by reacting this butadiene with the anion obtained from treating

[(π-C5H5)Fe(CO)2]2 with sodium amalgam [16]. The product was puriﬁed with column chro-

matography, giving a total yield of about 5%. The sample at 0.88 ± 0.04 mole % in diethyl

ether-d10 was dried using 3 ˚A molecular sieves, ﬁltered through a 0.45 µm syringe ﬁlter and

ﬂame sealed in the NMR sample tube using three freeze-thaw vacuum degassing cycles. All

experiments were performed at 30◦C.

## Page 14

14

FIG. 3 Pulse sequence for implementation of the quantum circuit of Fig. 1 for a = 7. The

tall red lines represent 90◦pulses selectively acting on one of the seven qubits (horizontal lines)

about positive ˆx (no cross), negative ˆx (lower cross) and positive ˆy (top cross).
Note how

single 90◦pulses correspond to Hadamard gates and pairs of such pulses separated by delay

times correspond to two-qubit gates. The smaller blue lines denote 180◦selective pulses used for

refocusing [21], about positive (darker shade) and negative ˆx (lighter shade). Rotations about ˆz

are denoted by smaller and thicker green rectangles and were implemented with frame-rotations.

Time delays are not drawn to scale. The vertical dashed black lines visually separate the steps

of the algorithm; step (0) shows one of the 36 temporal averaging sequences.

FIG. 4 NMR spectra at diﬀerent stages in the computation.
a.
Experimentally measured

thermal equilibrium spectra (real part), acquired after a read-out pulse on spin i has tipped the

spin from |0⟩(+ˆz) or |1⟩(−ˆz) into the ˆx −ˆy-plane, where it induces a voltage oscillating at

ωi/2π + P
j ±Jij/2 (where the sign depends on the state of the other spins) in a transverse

RF coil placed nearby the sample. This voltage was recorded by a phase-sensitive detector and

Fourier transformed to obtain a spectrum, with the phase set such that positive (negative) lines

correspond to a spin in |0⟩(|1⟩) before the readout pulse. Frequencies are in Hertz, and with

respect to ωi/2π. b. Experimental spectra for the eﬀective pure ground state. As desired, only

one line is retained in each multiplet with its position depending on strength and sign of the

J-couplings. Here, the transition corresponds to all other spins in |0⟩. The state ρ1 is obtained

from this state by applying a not on spin 7. c. Output spectra of the easy case of Shor’s

algorithm (a = 11). The top traces are the ideally expected spectra, the middle traces are the

experimental data, and the bottom traces are simulations which incorporate decoherence eﬀects

(vide infra). Each trace was rescaled separately. d. Similar set of spectra as in c, but for the

diﬃcult case (a = 7).

## Page 15

(3)
(4)
(2)
(1)
(0)
a.

B C D E

4:
5:
6:
7:

3:
2:

15

L. Vandersypen NATURE 07-Sep-01

A
F G H

Figure 1

## Page 16

5
5
C H
CO

1 −22052.0 5.0 1.3 −221.0 37.7 6.6 −114.3 14.5 25.16
2 489.5 13.7 1.8 18.6 −3.9 2.5 79.9 3.9
3 25088.3 3.0 2.5 1.0 −13.5 41.6 12.9
4 −4918.7 10.0 1.7 54.1 −5.7 2.1
5 15186.6 2.8 1.8 19.4 59.5

7i
6i
5i
4i
3i
2i
1,i
2,i
i
ω / 2π
i

T
T
J
J
J
J

J
J

6 −4519.1 45.4 2.0 68.9

7 4244.3 31.6 2.0

16

L. Vandersypen NATURE 07-Sep-01

Figure 2

## Page 17

17

L. Vandersypen NATURE 07-Sep-01

Figure 3

## Page 18

18

SPIN
1
SPIN
2
SPIN
3

L. Vandersypen NATURE 07-Sep-01

Figure 4
