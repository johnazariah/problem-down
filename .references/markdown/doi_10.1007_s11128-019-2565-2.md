---
source_pdf: ../doi_10.1007_s11128-019-2565-2.pdf
pages: 17
extracted_at: 2026-04-17T12:32:46+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Amplitude estimation without phase estimation"
author: "Yohichi Suzuki "
---

# doi_10.1007_s11128-019-2565-2

Original title: Amplitude estimation without phase estimation

Author metadata: Yohichi Suzuki 

Source PDF: ../doi_10.1007_s11128-019-2565-2.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Quantum Information Processing (2020) 19:75
https://doi.org/10.1007/s11128-019-2565-2

Amplitude estimation without phase estimation

Yohichi Suzuki1 · Shumpei Uno1,2 · Rudy Raymond1,3 · Tomoki Tanaka1,4 ·
Tamiya Onodera1,3 · Naoki Yamamoto1,5

Received: 29 May 2019 / Accepted: 24 December 2019 / Published online: 9 January 2020
© The Author(s) 2020

Abstract
Thispaperfocusesonthequantumamplitudeestimationalgorithm,whichisacoresub-
routine in quantum computation for various applications. The conventional approach
for amplitude estimation is to use the phase estimation algorithm, which consists
of many controlled ampliﬁcation operations followed by a quantum Fourier trans-
form. However, the whole procedure is hard to implement with current and near-term
quantum computers. In this paper, we propose a quantum amplitude estimation algo-
rithm without the use of expensive controlled operations; the key idea is to utilize the
maximum likelihood estimation based on the combined measurement data produced
from quantum circuits with different numbers of amplitude ampliﬁcation operations.
Numerical simulations we conducted demonstrate that our algorithm asymptotically
achieves nearly the optimal quantum speedup with a reasonable circuit length.

Keywords Quantum amplitude estimation · Classical post-processing · Maximum
likelihood estimation · Cramér–Rao bound

Yohichi Suzuki and Shumpei Uno are equally contributing authors.

B Naoki Yamamoto
yamamoto@appi.keio.ac.jp

1
Quantum Computing Center, Keio University, 3-14-1 Hiyoshi, Kohoku-ku, Yokohama,
Kanagawa 223-8522, Japan

2
Mizuho Information and Research Institute, Inc., 2-3 Kanda-Nishikicho, Chiyoda-ku, Tokyo
101-8443, Japan

3
IBM Research - Tokyo, 19-21 Nihonbashi Hakozaki-cho, Chuo-ku, Tokyo 103-8510, Japan

4
Mitsubishi UFJ Financial Group, Inc. and MUFG Bank, Ltd., 2-7-1 Marunouchi, Chiyoda-ku,
Tokyo 100-8388, Japan

5
Department of Applied Physics and Physico-Informatics, Keio University, 3-14-1 Hiyoshi,
Kohoku-ku, Yokohama, Kanagawa 223-8522, Japan

123

## Page 2

75
Page 2 of 17
Y. Suzuki et al.

1 Introduction

Quantum computers are expected to allow us to perform high-speed computations over
classical computations for problems in a wide range of scientiﬁc and technological
ﬁelds. Environments in which quantum algorithms can be executed by real quantum
devices are currently being provided [1–3]. Real quantum devices with several tens
of qubits will soon be realized in near future, although those are the so-called noisy
intermediate-scale quantum (NISQ) devices that impose several practical limitations
on their use [4], both in the number of gate operations and in the number of available
qubits. Hence, several custom subroutines taking into account these constraints have
been proposed, typically the variational quantum eigensolver [5,6].
In this paper, we focus on the amplitude estimation algorithm, which is a core
subroutine in quantum computation for various applications, e.g., in chemistry [7,8],
ﬁnance [9,10], and machine learning [11–14]. In particular, quantum speedup of Monte
Carlo sampling via amplitude estimation [15] lies in the heart of these applications.
Therefore, in light of its importance, we followed the aforementioned direction and
developed a new amplitude estimation algorithm that can be executed in NISQ devices.
Note that Ref. [16] demonstrated that the amplitude estimation problem can be
formulated as a phase estimation problem [17], where the amplitude to be estimated is
inferred from the eigenvalue of the corresponding ampliﬁcation operator. Owing to the
ubiquitous nature of the eigenvalue estimation problem, some versions of the phase
estimation algorithm suitable for NISQ devices [18–22] have been proposed (with the
last one appeared slightly after ours), and they all rely on classical post-processing
statistics such as the Bayes method. However, these modiﬁed phase estimation algo-
rithms as well as the original scheme [17] still involve many controlled operations
(e.g., the controlled ampliﬁcation operation in the case of Ref. [16]) that can be dif-
ﬁcult to implement on NISQ devices. Therefore, a new algorithm specialized to the
amplitude estimation problem is required, one that does not use expensive controlled
operations.
The goal of amplitude estimation is, in its simplest form, to estimate the unknown
parameter θ contained in the state |Ψ ⟩= sin θ |good⟩+cos θ |bad⟩, where |good⟩and
|bad⟩are given orthogonal state vectors. Our scheme is composed of the amplitude
ampliﬁcation process and the maximum likelihood (ML) estimation; the controlled
operations and the subsequent quantum Fourier transform (QFT) are not involved. The
ampliﬁcation process transforms the coefﬁcient of |good⟩to sin((2m + 1)θ) with m
being the number of operations; if θ is known, then, by suitably choosing m, we can
enhance the probability of hitting “good” quadratically greater than the classical case,
wherenoamplitudeampliﬁcationisutilized[23].However,thefunctionsin((2m+1)θ)
does not always take a relatively large value for a certain m because θ is unknown in
this problem, meaning that an effective quantum speedup is not always available; also,
the ML estimate is not uniquely determined due to the periodicity of this function.
Our strategy is the ﬁrst to make measurements on the transformed quantum state and
to construct likelihood functions for several m, say {m0, . . . , mM}, and then combine
them to construct a single likelihood function that uniquely produces the ML estimate;
see Fig. 1. The broad concept behind this scheme is to combine the data produced from
different quantum circuits, and the scheme might be performed even on NISQ devices

123

## Page 3

Amplitude estimation without phase estimation
Page 3 of 17
75

to compute a target value faster than classical algorithms via some post-processing.
Actually a numerical simulation demonstrates that, by appropriately designing {mk},
compared with the classical sampling we can achieve nearly a square root reduction in
the total number of queries to reach the speciﬁed estimation precision; notably, only
relatively short-depth circuits are required to achieve this quantum speedup. We also
show that, in an application of the amplitude estimation to Monte Carlo integration, our
algorithm requires many fewer controlled NOT (CNOT) gates than the conventional
phase-estimation-based approach, so it is suitable for obtaining quantum advantages
with NISQ devices. Note that Ref. [24] also took the approach without using the
phase estimation method, but it needed to change the query in each iteration, which is
highly demanding in practice. Also the paper Ref. [25] gave an amplitude estimation
scheme that employs a Bayes rule together with applying random Unitary operations
(subjected to the Haar measure) to ideally realize the quadratic speedup, without a
controlled Unitary operation; this scheme is applicable to low-dimensional quantum
circuits, due to the hardness to implement the random Unitaries.

2 Preliminary

We herein brieﬂy describe the quantum amplitude ampliﬁcation, which is the basis of
our approach for the amplitude estimation problem.
Our proposed algorithm mainly consists of two parts: quantum amplitude ampli-
ﬁcation and amplitude estimation based on likelihood analysis. The amplitude
ampliﬁcation [26,27] is the generalization of the Grover’s quantum searching algo-
rithm [23]. Similar to quantum searching, the amplitude ampliﬁcation is known to
achieve quadratic speedup over the corresponding classical algorithm.
We assume a unitary operator A that acts on (n + 1) qubits, such that |Ψ ⟩=
A |0⟩n+1 = √a| ˜Ψ1⟩|1⟩+√1 −a| ˜Ψ0⟩|0⟩, where a ∈[0, 1] is the unknown parameter
to be estimated, while | ˜Ψ1⟩and | ˜Ψ0⟩are the n-qubit normalized good and bad states.
The query complexity of estimating a is counted by the number of the operations of
A , which is often denoted as the number of queries for simplicity. By performing
measurements on |Ψ ⟩repeatedly, we can infer a from the ratio of obtaining the good
and bad states, but the number of queries is exactly the same as the classical one in
this case.
The advantage offered by the quantum amplitude ampliﬁcation is that, instead of
measuring right after the single operation of A , we can amplify the probability of
obtaining the good state by applying the following operator.

Q = −A S0A −1Sχ,
(1)

where the operator Sχ puts a negative sign to the good state, i.e., Sχ| ˜Ψ1⟩|1⟩=
−| ˜Ψ1⟩|1⟩, and does nothing to the bad state. Similarly, S0 puts a negative sign to
the all-zero state |0⟩n+1 and does nothing to the other states. A −1 is the inverse of A ,
the operation of which requires the same query complexity as A .

123

## Page 4

75
Page 4 of 17
Y. Suzuki et al.

By deﬁning a parameter θa ∈[0, π/2] such that sin2 θa = a, we have

A |0⟩n+1 = sin θa| ˜Ψ1⟩|1⟩+ cos θa| ˜Ψ0⟩|0⟩.
(2)

Brassard et al. [16] showed that repeatedly applying Q for m times on |Ψ ⟩results in

Qm|Ψ ⟩= sin((2m + 1)θa)| ˜Ψ1⟩|1⟩+ cos((2m + 1)θa)| ˜Ψ0⟩|0⟩.
(3)

This equation represents that, after applying Q m times (with 2m queries), we can
obtain the good state with a probability of at least 4m2 times larger than that obtained
from A |0⟩n+1 for sufﬁciently small a. This is in contrast with having 2m number of
measurements from A |0⟩n+1, which only gives the good state with probability 2m
times larger. This intuitively gives the quadratic speedup obtained from the amplitude
ampliﬁcation: if we can infer the ratio of the good state after the amplitude ampliﬁ-
cation, we can estimate the value of a from the number of queries required to obtain
such a ratio.
The conventional amplitude estimation [16] utilizes the quantum phase estimation
which requires a quantum circuit that implements the multiple controlled Q operations,
namely, Controlled-Q : |m⟩|Ψ ⟩→|m⟩Qm|Ψ ⟩. Performing the controlled operations
simultaneously on many m’s consecutively and gathering the amplitude by the inverse
QFT enables an accurate estimation of a [16]. However, this approach suffers from
the need for many controlled gates (thus, CNOT gates) and additional ancilla qubits
(the number of which is dictated by the required accuracy). Such an approach can be
problematic for NISQ devices.

3 Amplitude estimation without phase estimation

3.1 Algorithm

This section shows the quantum algorithm to estimate θa in Eq. (3) without using the
conventional phase-estimation-based method [16]. The ﬁrst stage of the algorithm is to
make good or bad measurements on the quantum state Qmk|Ψ ⟩for a chosen set of {mk}.
Let Nk be the number of measurements (shots) and hk be the number of measuring
good states for the state Qmk|Ψ ⟩; then, because the probability measuring the good
state is sin2((2mk +1)θa), the likelihood function representing this probabilistic event
is given by

Lk(hk; θa) =

sin2((2mk + 1)θa)
hk 
cos2((2mk + 1)θa)
Nk−hk .
(4)

The second stage of the algorithm is to combine the likelihood functions Lk(hk; θa)
for several {m0, . . . , mM} to construct a single likelihood function L(h; θa):

M


L(h; θa) =

k=0
Lk(hk; θa),
(5)

123

## Page 5

Amplitude estimation without phase estimation
Page 5 of 17
75

Fig.1 Schematic picture of our amplitude estimation algorithm using the ML estimation. After preparing the
states Qmk |Ψ ⟩, the numbers of measuring good states, i.e., hk are obtained (left). Based on the obtained hk,
the likelihood functions Lk(hk; θa) are constructed (center). Finally, a single likelihood function L(h; θa)
is introduced by combining the likelihood functions Lk(hk; θa) (right). The ML estimate is the value that
maximizes the likelihood function L(h; θa)

where h = (h0, h1, . . . , hM). The ML estimate is deﬁned as the value that maximizes
L(h; θa):

ˆθa = arg max
θa
L(h; θa) = arg max
θa
ln L(h; θa)
(6)

The whole procedure is summarized in Fig. 1. Now a and θa are uniquely related
through a = sin2 θa in the range 0 ≤θa ≤π/2, and ˆa := sin2 ˆθa is the ML estimate
for a; thus, in what follows, L(h; a) is denoted as L(h; θa). Note that the random
variables h0, h1, . . . , hM are independent but not identically distributed because the
probability distribution for obtaining hk, i.e., pk(hk; θa) ∝Lk(hk; θa), is different for
each k; however, the set of multidimensional random variables h = (h0, h1, . . . , hM)
is independently generated from the identical joint probability distribution p(h; θa) ∝
L(h; θa).
This algorithm has two caveats: (i) if only a single amplitude ampliﬁcation circuit
is used like in the Grover search algorithm, i.e., the case M = 0 and m0 ̸= 0, the
ML estimate ˆθa cannot be uniquely determined due to the periodicity of L0(h0; θa),
and (ii) if no ampliﬁcation operator is applied, i.e., mk = 0 ∀k, then the ML estimate
is unique, but it does not have any quantum advantages, as shown later. Hence, the
heart of our algorithm can be regarded as the quantum circuit fusion technique that
combines some quantum circuits to determine the target value uniquely, while some
quantum advantage is guaranteed.

123

## Page 6

75
Page 6 of 17
Y. Suzuki et al.

3.2 Statistics: Cramér–Rao bound and Fisher information

The remaining to be determined in our algorithm was to design the sequences {mk, Nk}
so that the resulting ML estimate ˆθa might have a distinct quantum advantage over the
classical one. Here, we introduce a basic statistical method to carry out this task and,
based on that method, give some speciﬁc choice of {mk, Nk}.
First, in general, the Fisher information I (a) is deﬁned as

 ∂

I (a) = E

∂a ln L(x; a)
2

,
(7)

where the expectation is taken over a random variable x subjected to a given probability
distribution p(x; a) with an unknown parameter a. The importance of the Fisher
information can be clearly seen from the fact that any estimate ˆa satisﬁes the following
Cramér–Rao inequality.

var(ˆa) = E[(ˆa −E[ˆa])2] ≥[1 + b′(a)]2

I (a)
,
(8)

where b(a) represents the bias deﬁned by b(a) = E[ˆa −a] and b′(a) indicates the
derivative of b(a) with respect to a. It is easy to see that the mean squared estimation
error satisﬁes

E[(ˆa −a)2] ≥[1 + b′(a)]2

I (a)
+ b(a)2.
(9)

A speciﬁcally important property of the ML estimate, which maximizes the likelihood
function
k p(xk; a) with the measurement data xk, is that it becomes unbiased, i.e.,
b(a) = 0, and further achieves the equality in Eq. (9) in the large number limit of
measurement data [28]; that is, the ML estimate is asymptotically optimal.
In our case, by substituting Eqs. (4) and (5) into Eq. (7) together with a straight
forward calculation E[hk] = Nk sin2((2mk + 1)θa), we ﬁnd that

M

I (a) =
1
a(1 −a)

k=0
Nk(2mk + 1)2.
(10)

Also, for any sequences {mk, Nk}, the total number of queries is given as

M

Nq =

k=0
Nk(2mk + 1).
(11)

As stated before, the coefﬁcient 2 multiplying mk in Eq. (11) originates from the
fact that the operator Q uses A and A −1, and the constant +1 is due to the initial
state preparation of |Ψ ⟩= A |0⟩n+1. If Q is not applied to |Ψ ⟩and if only the ﬁnal

123

## Page 7

Amplitude estimation without phase estimation
Page 7 of 17
75

measurements are performed for |Ψ ⟩, i.e., mk = 0 for all k, the total number of queries
is identical to that of classical random sampling. Because Nk and (2mk+1) are positive
integers, the Fisher information in Eq. (10) satisﬁes the following relation.

M

2

I (a) ≤
1
a(1 −a)

=
1
a(1 −a) N 2
q .
(12)

k=0
Nk(2mk + 1)

Here, ˆa is set to the ML estimate (6), and the estimation error is considered to be ˆε =

E[(ˆa −a)2] in this case. The total number of measurements M
k=0 Nk is assumed
to be sufﬁciently large, in which case the ML estimate asymptotically converges to an
unbiased estimate and achieves the lower bound of the Cramér–Rao inequality (8), as
aforementioned. Hence, from Eqs. (8) and (12), the error ˆε satisﬁes

ˆε →
1
I (a)1/2 ≥
√a(1 −a)

Nq
.
(13)

(More precisely, ˆε I (a)1/2 →1.) That is, the lower bound of the estimation error
is on the order of O(N −1
q ), which is referred to as the Heisenberg limit. This is in
stark contrast to the classical sampling method, the estimation error of which is lower
bounded by √a(1 −a)/N 1/2
q
, obtained by setting mk = 0 ∀k (i.e., a case with no
amplitude ampliﬁcation) in Eqs. (10) and (11); that is, the lower bound is at best on
the order of O(N −1/2
q
) in the classical case.
Now, we can consider the problem posed at the beginning of this subsection: design-
ing the sequences {mk, Nk} so that the resulting ML estimate ˆθa outperforms the
classical limit O(N −1/2
q
) and hopefully achieves the Heisenberg limit O(N −1
q ), i.e.,
the quantum quadratic speedup. Although the problem can be formulated as a max-
imization problem of Fisher information (10) with respect to {mk, Nk} under some
constraints on these variables, here we ﬁx Nk’s to a constant and provide just two
examples of the sequence {mk}:

– Linearly incremental sequence (LIS): Nk = Nshot for all k, and mk = k, i.e., it
increases as m0 = 0, m1 = 1, m2 = 2, . . . , mM = M.
– Exponentially incremental sequence (EIS): Nk = Nshot for all k, and mk increases
as m0 = 0, m1 = 20, m2 = 21, . . . , mM = 2(M−1).

In the case of LIS, the Fisher information (7) and the number of queries (11) are calcu-
latedasI (a) = Nshot(2M+3)(2M+1)(M+1)/(3a(1−a))and Nq = Nshot(M+1)2,
respectively. Because Nq ∼NshotM2 and I (a) ∼NshotM3/(3a(1 −a)) when M ≫
1, the lower bound of the estimation error is evaluated as ˆε = 1/I (a)1/2 ∼N −3/4
q
;
hence, a distinct quantum advantage occurs, although it does not reach the Heisenberg
limit. Next for the case of EIS, we ﬁnd Nq ∼Nshot2M+1 and I (a) ∼Nshot22(M+1)/3,
which as a result lead to ˆε ∼N −1
q . Therefore, this choice is asymptotically optimal;
we again emphasize that the statistical method certainly serves as a guide for us to ﬁnd
an optimal sequence {mk}, achieving an optimal quantum amplitude estimation algo-
rithm. But note that these quantum advantages are guaranteed only in the asymptotic

123

## Page 8

75
Page 8 of 17
Y. Suzuki et al.

regime and that the realistic performance with the ﬁnite (or rather short) circuit depth
should be analyzed. We will carry out a numerical simulation to see this realistic case
in the following.

3.3 Numerical simulation

In this section, the ML estimates ˆθa and errors ˆε are evaluated numerically for several
ﬁxed target probabilities a = sin2 θa. Based on the chosen sequence of {Nk} and {mk}
shown in the previous subsection, hk’s in Eq. (5) are generated using the Bernoulli
sampling with probability sin2((2mk + 1)θa) for each k. The global maximum of the
likelihood function can be obtained by using a modiﬁed brute-force search algorithm;
the global maximum of m
k=0 Lk(hk; θa) is determined by searching around the vicin-
ity of the estimated global maximum for m−1
k=0 Lk(hk; θa). The errors ˆε are evaluated
by repeating the aforementioned procedures 1000 times for each Nq.
In Fig. 2, the relationship between the number of queries and errors is plotted
for the target probabilities a = sin2 θa = 2/3, 1/3, 1/6, 1/12, 1/24, and 1/48 with
Nshot = 100. The (red) triangles and (black) circles in Fig. 2 are errors that are obtained
using LIS and EIS, respectively. For comparison, numerical simulations with mk = 0
for all k are also performed, and the results are plotted as (blue) squares in Fig. 2. In
addition, the lower bounds of errors (13) when the estimate is not biased are also plotted
as (red) dotted and (black) solid lines for LIS and EIS, respectively. The (blue) dashed
lines in Fig. 2 are the lower bounds for classical random sampling, i.e.,
a(1 −a)/Nq.
The slopes of the simulated results with the target probability a = sin2 θa = 1/48
rangingfrom Nq ≃103 to Nq ≃105 inFig.2areﬁttedbylog ˆε = γ ·log Nq+δ,andthe
ﬁtted parameters corresponding to the slope are obtained as γ = −0.76, γ = −0.95
and γ = −0.50 for LIS and EIS, and classical random sampling, respectively. Similar
slopes are obtained with other target probabilities. The ﬁtted values of γ for LIS and
EIS are consistent with the slopes obtained using the Fisher information, although γ
slightly deviated from the theoretical values. This slight deviation indicates that ˆa is a
biased estimate; in fact, this deviation decreases as Nshot increases, which is consistent
with the fact that, in general, the ML estimate becomes unbiased asymptotically as the
sampling number increases. Also, the efﬁciency of the ML estimate can be observed
in the numerical simulation; the estimation error approaches the Cramér–Rao lower
bound (13). In Appendix A, we show the comparison of the error for the conventional
phase-estimation-based approach with that of EIS. As a result, their estimation errors
are found to be comparable.
Finally, we remark that the computational complexity for naively ﬁnding the maxi-
mum of the likelihood function is on the order of O((1/ε) ln(1/ε)) if mk exponentially
grows, as in EIS. This is because the computational complexity to obtain the likeli-
hood function ln L(h; θa) is evaluated as O(M) in this case. The order of the error ε
is estimated as O(N −1
q ) based on the Cramér–Rao bound. Because Nq ∼2M Nshot,
the complexity of evaluating the likelihood function is O(ln(1/ε)). Assuming that the
brute-force search among 1/ε segments is performed to ﬁnd the global maximum of
the likelihood function, the complexity of ﬁnding the maximum is O((1/ε) ln(1/ε)).
In the case of LIS, the order of the computational complexity can also be evaluated

123

## Page 9

Amplitude estimation without phase estimation
Page 9 of 17
75

Fig. 2 Relationships between the number of queries and the estimation error for several target probabilities
a = sin2 θa. The lower bounds of estimation error based on the Cramér–Rao inequality are depicted as
lines, the (blue) dashed line is for mk = 0 for all k (classical random sampling), the (red) dotted line is for
m0 = 0, m1 = 1, . . . mM = M (LIS), and the (black) solid line is for m0 = 0, m1 = 20, . . . mM = 2M−1

(EIS), respectively. The estimation errors obtained by numerical simulations are also plotted as symbols,
the (blue) squares are for classical random sampling, the (red) triangles are for LIS, and the (black) circles
are for EIS (Color ﬁgure online)

as O(ε−5/3) in the same manner as before. It should be noted that the brute-force
search algorithm for ﬁnding global minima of M
k=0 Lk(hk; θa) is not necessary if
mk is zero for all k (classical case), since the target value is simply obtained by
ˆa = M
k=0 hk/ M
k=0 Nshot. The error can be obtained as O(N −1/2
q
) based on the
Cramér–Rao bound. Due to the fact that Nq = NshotM, the computational complexity

123

## Page 10

75
Page 10 of 17
Y. Suzuki et al.

Table 1 Summary of the complexities for estimating target value with given error ε. The query complexity
and computational complexity of post-processing for different update rules of mk are listed

Update rule of mk
Query complexity
Computational complexity of
post-processing

Classical (mk = 0∀k)
O(ε−2)
O(ε−2)

O(ε−4/3)
O(ε−5/3)

Linearly incremental sequence (LIS)
(m0 = 0, m1 = 1, m2 =
2, . . . , mM = M)

O(ε−1)
O(ε−1 ln ε−1)

Exponentially incremental sequence
(EIS) (m0 = 0, m1 = 20, m2 =
21, . . . , mM = 2(M−1))

in the classical case is O(ε−2). The evaluated computational complexities of post-
processing for different update rules of mk are summarized together with the query
complexities in Table 1.

4 Application to the Monte Carlo integration

We conduct a Monte Carlo integration as an example of the application of our algo-
rithm, as follows. In this section, we ﬁrst review the quantum algorithm to calculate
the Monte Carlo integration by amplitude estimation [15] and then explain the ampli-
tude ampliﬁcation operator used in our algorithm. Next, we present the integral of the
sine function as a simple example of Monte Carlo integration. Using this example,
we discuss the number of CNOT gates and qubits required for our algorithm and the
conventional amplitude estimation [16].

4.1 The Monte Carlo integration as an amplitude estimation

One purpose of the Monte Carlo integration is to calculate the expected value of real-
valued function 0 ≤f (x) ≤1 deﬁned for n-bit input x ∈{0, 1}n with probability
p(x):

2n−1

E[ f (x)] =

x=0
p(x) f (x).
(14)

In the quantum algorithm for the Monte Carlo integration, an additional (ancilla) qubit
is introduced and assumed to be rotated as

R|x⟩n|0⟩= |x⟩n


1 −f (x)|0⟩

,
(15)

f (x)|1⟩+

where R is a unitary operator acting on n + 1 qubits. In addition, an algorithm P is
introduced, and operating P to n-qubit resister |0⟩n yields

123

## Page 11

Amplitude estimation without phase estimation
Page 11 of 17
75

Fig. 3 Quantum circuit of
amplitude ampliﬁcation for the
Monte Carlo integration

2n−1

P|0⟩n =

x=0

p(x)|x⟩n,
(16)

where all qubits in |0⟩n are in the state |0⟩. Operating R(P ⊗I1) to the state |0⟩n|0⟩
generates |Ψ ⟩:

|Ψ ⟩= R(P ⊗I1)|0⟩n|0⟩
(17)

2n−1

p(x)|x⟩n


=

x=0

1 −f (x)|0⟩

,
(18)

f (x)|1⟩+

where I1 is the identity operator acting on an ancilla qubit. For convenience, we put
a = 2n−1
x=0 p(x) f (x) and introduce two orthonormal bases:

2n−1

p(x)

| ˜Ψ1⟩=
1
√a

x=0

2n−1

p(x)

| ˜Ψ0⟩=
1
√1 −a

x=0

f (x)|x⟩n|1⟩,
(19)

1 −f (x)|x⟩n|0⟩.
(20)

By using these bases, the state |Ψ ⟩can be rewritten as

|Ψ ⟩= √a| ˜Ψ1⟩+
√

1 −a| ˜Ψ0⟩.
(21)

Then, the square root of expected value a = E[ f (x)] appears in the amplitude of
| ˜Ψ1⟩, and the Monte Carlo integration can be regarded as an amplitude estimation
of | ˜Ψ1⟩. The operator Q deﬁned in Eq. (1) can be achieved using UΨ U ˜Ψ0, where
U ˜Ψ0 = I −2| ˜Ψ0⟩⟨˜Ψ0|, UΨ = I −2|Ψ ⟩⟨Ψ |, and I is the identity acting on n + 1 qubits
[16]. In terms of a practical point of view, we use U ˜Ψ0 = In+1 −2In|0⟩⟨0|, where
I = In+1 = In ⊗(|0⟩⟨0| + |1⟩⟨1|). By putting a = sin2 θa and using Eq. (3), we
could apply our algorithm to the Monte Carlo integration. The circuit diagram of the
amplitude ampliﬁcation used in our algorithm is shown in Fig. 3. Note that the multi-
qubit gate consisting of P and R in Fig. 3 corresponds to the quantum algorithm A
shown in Sect. 2, and the only ancilla qubit for each k is measured when our algorithm
is applied to the Monte Carlo. Similarly, the circuit of the conventional amplitude
estimation [16] is shown in Fig. 4. In the following, we applied our algorithm to a
very simple integral of the sine function and compared the number of CNOT gates
and qubits with the results of the conventional amplitude estimation.

123

## Page 12

75
Page 12 of 17
Y. Suzuki et al.

Fig. 4 Quantum circuit of conventional amplitude estimation for the Monte Carlo integration. F−1
m
repre-
sents the inverse QFT of m qubits

4.2 Simple example: integral of the sine function

As a simple example of the Monte Carlo integration, the following integral is consid-
ered.

 bmax

I =
1
bmax

0
sin(x)2dx,
(22)

where bmax is a constant that determines the upper limit of the integral. By discretizing
this integral in n-qubit, we obtain

x=0
p (x) sin2

x + 1

2n−1

S =

2

bmax
2n

,
(23)

where p(x) =
1
2n is a discrete uniform probability distribution. We now explicitly
describe the operators P and R for applying our algorithm to calculate sum (23). The
operator P acting on the n-qubit initial state can be deﬁned as

P : |0⟩n|0⟩→
1
√

2n

2n−1

x=0
|x⟩n|0⟩.
(24)

The operator P can be constructed using n Hadamard gates. The operator R acting
on the (n + 1)-qubit state |x⟩n|0⟩can be deﬁned as

123

## Page 13

Amplitude estimation without phase estimation
Page 13 of 17
75

Fig. 5 Quantum circuit achieving the operator R in Eq. (25). In this circuit, |x⟩in Eq. (25) is represented
by n qubits, denoted by |q⟩(1), |q⟩(2), . . . , |q⟩(n). Ry(θ) represents a Y-rotation with angle θ

Fig. 6 Quantum circuit of amplitude ampliﬁcation in the case of n = 2 with single Q operation

Fig. 7 Quantum circuit of conventional amplitude estimation in the case of n = 2 with a single Q operation


x + 1


x + 1

2

bmax
2n

2

bmax
2n

R : |x⟩n|0⟩→|x⟩n

|1⟩+ cos

|0⟩

. (25)

sin

The operator R can be constructed using controlled Y-rotations as illustrated in Fig. 5.
We now explicitly show an example of the circuits for the amplitude ampliﬁcation
used in our algorithm and a conventional amplitude estimation with a single Q opera-
tion, which calculates sum (23). For simplicity, the circuit for bmax = π/4 and n = 2
is shown here. The quantum circuits for amplitude ampliﬁcation and conventional
amplitude estimation are shown in Figs. 6 and 7, respectively. In these circuits, all-to-
all qubit connectivity is assumed. From these ﬁgures, we can see that the circuit for
conventional amplitude estimation tends to have more gates and qubits than that of our
algorithm. Furthermore, the multi-controlled operation in the conventional amplitude
estimation circuit of Fig. 7 may require several ancilla qubits.
Table2showsthenumberofCNOTgatesandqubitsasafunctionofthenumberofQ
operators required for conventional amplitude estimation and our algorithm. Here, we
assumethegatesetsupportedbyQiskitver.0.7[29].BecausethenumberofCNOTgate
operations is restricted in NISQ devices due to the error accumulation, the numbers
of CNOT gates in our algorithm only those for the circuit with the largest mk are
evaluated. The numbers of CNOT gates in our algorithm are about 7–18 times smaller
than those of conventional amplitude estimation. The number of qubits required for
conventional amplitude estimation increases as the number of Q operations increased,
while that for our algorithm kept constant. The source code for Monte Carlo integration
based on our proposed algorithm is available at [30].

123

## Page 14

75
Page 14 of 17
Y. Suzuki et al.

Table 2 Number of CNOT gates and qubits to calculate (23) as a function of Q operations

# Operators Q
Conventional amplitude estimation
Our algorithm

# CNOT gates
# Qubits
# CNOT gates
# Qubits

0
–
–
4
3

20
135
7
18
3

21
399
8
32
3

22
927
9
60
3

23
1981
10
116
3

24
4085
11
228
3

25
8287
12
452
3

26
16,683
13
900
3

27
33,465
14
1796
3

28
67,017
15
3588
3

5 Conclusion

We proposed a quantum amplitude estimation algorithm achieving quantum speedup
by reducing controlled gates with ML estimation. The essential idea of the proposed
algorithm is constructing a likelihood function using the outcomes of measurements on
several quantum states, which are transformed by the amplitude ampliﬁcation process.
Although the probability measuring good or bad states depends on the number of
amplitude ampliﬁcation operations, the outcomes are correlated due to the fact that
each ampliﬁed probability is a function of a single parameter. To test the efﬁciency
of the proposed algorithm, we performed numerical simulations and analyzed the
relationships between the number of queries and estimation error. Empirical evidences
showed the algorithm could estimate the target value with fewer queries than the
classical algorithm. We also presented the lower bound of the estimation error in
terms of the Fisher information and found that the estimation error observed in a
numerical simulation was sufﬁciently close to the Heisenberg limit. In addition, we
experimented the proposed algorithm for a Monte Carlo integration and found that
fewer CNOT gates and qubits were required in comparison with the conventional
amplitude estimation. These facts indicate that our algorithm could work well even
with noisy intermediate-scale quantum devices.
Shortly after the publication of our results, simpliﬁed quantum counting and ampli-
tude estimation without QFT with rigorous proofs were shown [31]. In contrast to
our approach that can be run in parallel on multiple quantum devices, the simpli-
ﬁed algorithms are adaptive and have to be run sequentially. They also require large
constant-factor overhead, e.g., millions of measurement samples, which could be
expensive in practice. Nevertheless, there are several interesting directions for future
work as pointed out in [31], such as, obtaining rigorous proofs for our parallel approach
and achieving quantum speedups with depth-limited quantum circuits.

123

## Page 15

Amplitude estimation without phase estimation
Page 15 of 17
75

Acknowledgements We thank Yutaka Shikano and Hideo Watanabe for their constructive comments. This
work was supported by MEXT Quantum Leap Flagship Program Grant Number JPMXS0118067285.

OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if changes were made. The images or other third party material in this article are included
in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If
material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

Appendix A: Comparison of estimation errors with conventional
amplitude estimation

We compare the estimation error between the conventional amplitude estimation
algorithm and our proposed algorithm. The details of conventional amplitude esti-
mation algorithm are presented in Ref. [16]. For simplicity, only the result of
a = sin2 θa = 1/48 is shown here.
Figure 8 shows the relations between the number of queries and estimation error
for the conventional amplitude estimation and our proposed algorithm. In the ﬁgure,
the (black) circles, which represent the data of conventional algorithm, are generated
in the following manner. The conventional algorithm outputs four integers closest to
the target value θa M/π and M −θa M/π with success probability of at least 8/π2 ×
100% ∼81% after M = 2m −1 times application of controlled Q operation followed
by QFT [16]. The largest estimation error calculated from these four integers is plotted
in Fig. 8. The (red) triangles and (blue) squares represent the data of our proposed

10
2
10
3
10
4
10
5

Number of queries

Fig. 8 The relationship between the number of queries and estimation error, for our proposed algorithm
and the conventional amplitude estimation algorithm [16]. The (black) circles are generated from the
conventional phase-estimation-based approach. The (red) triangles and (blue) squares are the 81 percentile
values of estimation error with numerical simulations for Nshot = 30 and Nshot = 100 for EIS, respectively.
For comparison, the 81 percentile values of estimation error with classical sampling are also shown as
(green) crosses. Against a ﬁxed total number of queries, the smaller Nshot becomes, the more queries for
the quantum amplitude ampliﬁcation are used and thereby the estimation error approaches more closely to
that of the conventional algorithm (Color ﬁgure online)

123

## Page 16

75
Page 16 of 17
Y. Suzuki et al.

method with Nshot = 30 and 100, respectively. The 8/π2 ×100 ∼81 percentile of the
estimation error is plotted here for a fair comparison with the conventional algorithm,
while the averaged error is described in the main text. The data of our algorithm is
generated by the same manner as in Sect. 3.3.
This ﬁgure shows that the estimation error of our proposed method increases as the
number of shots increases. This is because, as can be seen from Eqs. (10) and (11), the
degree of quantum speedup becomes relatively smaller by increasing the number of
shots to the limit that it is essentially a classical sampling where the number of shots
is equal to the total number of queries. The ﬁgure shows that the estimation error of
the conventional algorithm is almost the same as that of ours with Nshot = 30.

References

1. IBM Q Experience: https://quantumexperience.ng.bluemix.net/qx/editor (2019). Accessed 26 Mar
2019
2. Friis, N., Marty, O., Maier, C., Hempel, C., Holzäpfel, M., Jurcevic, P., Plenio, M.B., Huber, M., Roos,
C., Blatt, R., Lanyon, B.: Observation of entangled states of a fully controlled 20-qubit system. Phys.
Rev. X 8, 021012 (2018)
3. Song, C., Xu, K., Liu, W., Yang, Cp, Zheng, S.B., Deng, H., Xie, Q., Huang, K., Guo, Q., Zhang, L.,
Zhang, P., Xu, D., Zheng, D., Zhu, X., Wang, H., Chen, Y.A., Lu, C.Y., Han, S., Pan, J.W.: 10-qubit
entanglement and parallel logic operations with a superconducting circuit. Phys. Rev. Lett. 119, 180511
(2017)
4. Preskill, J.: Quantum computing in the NISQ era and beyond. Quantum 2, 79 (2018)
5. McClean, J.R., Romero, J., Babbush, R., Aspuru-Guzik, A.: The theory of variational hybrid quantum-
classical algorithms. New J. Phys. 18, 023023 (2016)
6. Yung, M.H., Casanova, J., Mezzacapo, A., McClean, J., Lamata, L., Aspuru-Guzik, A., Solano, E.:
From transistor to trapped-ion computers for quantum chemistry. Sci. Rep. 4, 3589 (2014)
7. Knill, E., Ortiz, G., Somma, R.D.: Optimal quantum measurements of expectation values of observ-
ables. Phys. Rev. A 75, 012328 (2007)
8. Kassala, I., Jordan, S.P., Lovec, P.J., Mohsenia, M., Aspuru-Guzik, A.: Polynomial-time quantum
algorithm for the simulation of chemical dynamics. Proc. Natl. Acad. Sci. USA 105, 18681–18686
(2008)
9. Rebentrost, P., Gupt, B., Bromley, T.R.: Quantum computational ﬁnance: Monte Carlo pricing of
ﬁnancial derivatives. Phys. Rev. A 98, 022321 (2018)
10. Woerner, S., Egger, D.J.: Quantum risk analysis. npj Quantum Inf. 5, 15 (2019)
11. Wiebe, N., Kapoor, A., Svore, K.M.: Quantum algorithms for nearest-neighbor methods for supervised
and unsupervised learning. Quantum Inf. Comput. 15, 316–356 (2015)
12. Wiebe, N., Kapoor, A., Svore, K.M.: Quantum deep learning. Quantum Inf. Comput. 16, 541–587
(2016)
13. Wiebe, N., Kapoor, A., Svore, K.M.: Quantum perceptron models. In: Proceedings of the 30th Inter-
national Conference on Neural Information Processing Systems, pp. 4006–4014 (2016)
14. Kerenidis, I., Landman, J., Luongo, A., Prakash, A.: q-means: A quantum algorithm for unsupervised
machine learning. arXiv:1812.03584 (2018)
15. Montanaro, A.: Quantum speedup of Monte Carlo methods. Proc. Royal Soc. A 471, 20150301 (2015)
16. Brassard, G., Høyer, P., Mosca, M., Tapp, A.: Quantum amplitude ampliﬁcation and estimation. Con-
temp. Math. Ser. Millenn. 305, 53–74 (2002)
17. Kitaev, A.Y.: Quantum measurements and the Abelian stabilizer problem. Electron. Colloq. Comput.
Complex. arXiv:quant-ph/9511026 (1996)
18. Svore, K.M., Hastings, M.B., Freedman, M.: Faster phase estimation. Quantum Inf. Comput. 14, 306–
328 (2014)
19. Wiebe, N., Granade, C.: Efﬁcient Bayesian phase estimation. Phys. Rev. Lett. 117, 010503 (2016)
20. O’Brien, T.E., Tarasinski, B., Terhal, B.M.: Quantum phase estimation of multiple eigenvalues for
small-scale (noisy) experiments. New J. Phys. 21, 023022 (2019)

123

## Page 17

Amplitude estimation without phase estimation
Page 17 of 17
75

21. van den Berg, E.: Practical sampling schemes for quantum phase estimation. arXiv:1902.11168 (2019)
22. Wie, C.R.: Simpler quantum counting. arXiv:1907.08119 (2019)
23. Grover, L.K.: A fast quantum mechanical algorithm for database search. In: Proceedings of 28th Annual
ACM Symposium on Theory of Computing, pp. 212–219 (1996)
24. Abrams,D.S.,Williams,C.P.:Fastquantumalgorithmsfornumericalintegralsandstochasticprocesses.

arXiv:quant-ph/9908083 (1999)
25. Zintchenko, I., Wiebe, N.: Randomized gap and amplitude estimation. Phys. Rev. A 93, 062306 (2016)
26. Brassard, G., Høyer, P.: An exact quantum polynomial-time algorithm for Simon’s problem. In: Pro-
ceedings of the 5th Israeli Symposium on Theory of Computing and Systems, pp. 12–23 (1997)
27. Grover, L.K.: Quantum computers can search rapidly by using almost any transformation. Phys. Rev.
Lett. 80, 4329–4332 (1998)
28. Rao, C.R.: Linear Statistical Inference and its Applications, vol. 2. Wiley, New York (1973)
29. Aleksandrowicz, G., Alexander, T., Barkoutsos, P., Bello, L., Ben-Haim, Y., Bucher, D., Cabrera-
Hernádez, F.J., Carballo-Franquis, J., Chen, A., Chen, C.F., Chow, J.M., Córcoles-Gonzales, A.D.,
Cross, A.J., Cross, A., Cruz-Benito, J., Culver, C., González, S.D.L.P., Torre, E.D.L., Ding, D.,
Dumitrescu, E., Duran, I., Eendebak, P., Everitt, M., Sertage, I.F., Frisch, A., Fuhrer, A., Gambetta, J.,
Gago, B.G., Gomez-Mosquera, J., Greenberg, D., Hamamura, I., Havlicek, V., Hellmers, J., Herok, Ł.,
Horii, H., Hu, S., Imamichi, T., Itoko, T., Javadi-Abhari, A., Kanazawa, N., Karazeev, A., Krsulich, K.,
Liu, P., Luh, Y., Maeng, Y., Marques, M., Martín-Fernández, F.J., McClure, D.T., McKay, D., Meesala,
S., Mezzacapo, A., Moll, N., Rodríguez, D.M., Nannicini, G., Nation, P., Ollitrault, P., O’Riordan, L.J.,
Paik, H., Pérez, J., Phan, A., Pistoia, M., Prutyanov, V., Reuter, M., Rice, J., Davila, A.R., Rudy, R.H.P.,
Ryu, M., Sathaye, N., Schnabel, C., Schoute, E., Setia, K., Shi, Y., Silva, A., Siraichi, Y., Sivarajah, S.,
Smolin, J.A., Soeken, M., Takahashi, H., Tavernelli, I., Taylor, C., Taylour, P., Trabing, K., Treinish,
M., Turner, W., Vogt-Lee, D., Vuillot, C., Wildstrom, J.A., Wilson, J., Winston, E., Wood, C., Wood, S.,
Wörner, S., Akhalwaya, I.Y., Zoufal, C.: Qiskit: An open-source framework for quantum computing
(2019). https://doi.org/10.5281/zenodo.2562110
30. Qiskit
Community
Tutorials:
Amplitude
estimation
without
quantum
Fourier
transform
and controlled grover operators. https://github.com/Qiskit/qiskit-community-tutorials/blob/master/
algorithms/SimpleIntegral_AEwoPE.ipynb (2019). Accessed 30 Oct 2019
31. Aaronson, S., Rall, P.: Quantum approximate counting, simpliﬁed. arXiv:1908.10846 (2019)

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional afﬁliations.

123
