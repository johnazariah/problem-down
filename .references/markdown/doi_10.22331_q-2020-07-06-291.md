---
source_pdf: ../doi_10.22331_q-2020-07-06-291.pdf
pages: 20
extracted_at: 2026-04-17T12:32:48+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Option Pricing using Quantum Computers"
author: "Nikitas Stamatopoulos, Daniel J. Egger, Yue Sun, Christa Zoufal, Raban Iten, Ning Shen, Stefan Woerner, "
---

# doi_10.22331_q-2020-07-06-291

Original title: Option Pricing using Quantum Computers

Author metadata: Nikitas Stamatopoulos, Daniel J. Egger, Yue Sun, Christa Zoufal, Raban Iten, Ning Shen, Stefan Woerner, 

Source PDF: ../doi_10.22331_q-2020-07-06-291.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Option Pricing using Quantum Computers

Nikitas Stamatopoulos1, Daniel J. Egger2, Yue Sun1, Christa Zoufal2,3, Raban Iten2,3, Ning Shen1,
and Stefan Woerner2

1Quantitative Research, JPMorgan Chase & Co., New York, NY, 10017

2IBM Quantum, IBM Research – Zurich

3ETH Zurich

We present a methodology to price options
and portfolios of options on a gate-based quan-
tum computer using amplitude estimation, an
algorithm which provides a quadratic speedup
compared to classical Monte Carlo methods.
The options that we cover include vanilla op-
tions, multi-asset options and path-dependent
options such as barrier options.
We put an
emphasis on the implementation of the quan-
tum circuits required to build the input states
and operators needed by amplitude estimation
to price the diﬀerent option types. Addition-
ally, we show simulation results to highlight
how the circuits that we implement price the
diﬀerent option contracts.
Finally, we exam-
ine the performance of option pricing circuits
on quantum hardware using the IBM Q Tokyo
quantum device. We employ a simple, yet ef-
fective, error mitigation scheme that allows us
to signiﬁcantly reduce the errors arising from
noisy two-qubit gates.

arXiv:1905.02666v5 [quant-ph] 2 Jul 2020

1
Introduction

Options are ﬁnancial derivative contracts that give
the buyer the right, but not the obligation, to buy
(call option) or sell (put option) an underlying asset
at an agreed-upon price (strike) and timeframe (exer-
cise window). In their simplest form, the strike price
is a ﬁxed value and the timeframe is a single point in
time, but exotic variants may be deﬁned on more than
one underlying asset, the strike price can be a func-
tion of several market parameters and could allow for
multiple exercise dates. As well as providing investors
with a vehicle to proﬁt by taking a view on the market
or exploit arbitrage opportunities, options are core to
various hedging strategies and as such, understanding
their properties is a fundamental objective of ﬁnancial
engineering. For an overview of option types, features
and uses, we refer the reader to Ref. [1].
Due to the stochastic nature of the parameters op-
tions are deﬁned on, calculating their fair value can
be an arduous task and while analytical models ex-

Nikitas Stamatopoulos: Current Address: Goldman Sachs & Co.,
New York, NY, 10282

ist for the simplest types of options [2], the simpli-
fying assumptions on the market dynamics required
for the models to provide closed-form solutions often
limit their applicability [3]. Hence, more often than
not, numerical methods have to be employed for op-
tion pricing, with Monte Carlo being one of the most
popular due to its ﬂexibility and ability to generi-
cally handle stochastic parameters [4, 5]. However,
despite their attractive features in option pricing, clas-
sical Monte Carlo methods generally require extensive
computational resources to provide accurate option
price estimates, particularly for complex options. Be-
cause of the widespread use of options in the ﬁnance
industry, accelerating their convergence can have a
signiﬁcant impact in the operations of a ﬁnancial in-
stitution.

By leveraging the laws of quantum mechanics a
quantum computer [6] may provide novel ways to
solve computationally intensive problems such as
quantum chemistry [7–10], solving linear systems of
equations [11], and machine learning [12–14]. Quanti-
tative ﬁnance, a ﬁeld with many computationally hard
problems, may beneﬁt from quantum computing. Re-
cently developed applications of gate-based quantum
computing for use in ﬁnance [15] include portfolio op-
timization [16], the calculation of risk measures [17]
and pricing derivatives [18–20]. Several of these ap-
plications are based on the Amplitude Estimation al-
gorithm [21] which can estimate a parameter with a
convergence rate of 1/M, where M is the number of
quantum samples used.
This represents a theoreti-
cal quadratic speed-up compared to classical Monte
Carlo methods.

In this paper we extend the pricing methodology
presented in [17, 18] and place a strong emphasis on
the implementation of the algorithms in a gate-based
quantum computer. We ﬁrst classify options accord-
ing to their features and show how to take the dif-
ferent features into account in a quantum computing
setting. In Sec. 3, we review the quantum method-
ology to price options and discuss how to represent
relevant probability distributions in a quantum com-
puter. In Sec. 4, we show a framework to price vanilla
options and portfolios of vanilla options, options with
path-dependent dynamics and options on several un-
derlying assets. In Sec. 5 we show results from eval-

## Page 2

uating our option circuits on quantum hardware, and
describe the error mitigation scheme we employ to in-
crease the accuracy of the estimated option prices. In
particular, we employ the maximum likelihood esti-
mation method introduced in [22] to perform ampli-
tude estimation without phase estimation in option
pricing using three qubits of a real quantum device.

2
Review of option types and their
challenges

Option contracts are valid for a pre-determined pe-
riod of time, and their value at the expiration date
is called the payoﬀ. The goal of option pricing is to
estimate the option payoﬀat the expiration date in
the future and then discount that value to determine
its worth today. The discounted payoﬀis also called
the fair value and indicates the amount of money one
should pay to enter the option contract today, making
it worthwile receiving the payoﬀvalue at the expira-
tion date.
In practice, we price complex options numerically
using Monte Carlo methods by following these steps:

1. Model the asset price of the option’s underly-
ing(s) and any other sources of uncertainty as
random variables X = {X1, X2, . . . , XN} follow-
ing a stochastic process.

2. Generate a large number M of random price
paths {X1, X2, . . . , XM} for the underlying(s)
from the probability distribution P implied by
the stochastic process.

3. Calculate the option’s payoﬀf(Xi) on each gen-
erated price path and compute an estimator for
the expectation value of the payoﬀEP[f(X)] as
an average across all paths

M
X

ˆEP[f(X)] = 1

i=1
f(Xi)

M

By the Central Limit Theorem, the estimator ˆEP
converges to the expectation value EP as the num-
ber of paths goes to inﬁnity, with convergence
O
M −1/2
[23].

4. Discount the calculated expectation value to get
the option’s fair value.

The discounting process requires knowledge of in-
terest rates at future dates which is itself an impor-
tant question from a ﬁnancial modelling perspective.
However, for the types of options we consider, this
process is not computationally challenging and can
be performed classically after the payoﬀcalculation.
We therefore do not discount the expected payoﬀfor
simplicity.

We classify options according to two categories:
path-independent vs path-dependent and options on
a single asset or on multiple assets. Path-independent
options have a payoﬀfunction that depends on an un-
derlying asset at a single point in time. Therefore, the
price of the asset up to the exercise date of the op-
tion is irrelevant for the option price. By contrast, the
payoﬀof path-dependent options depends on the evo-
lution of the price of the asset and its history up to the
exercise date. Table 1 exempliﬁes this classiﬁcation.
Options that are path-independent and rely on a sin-
gle asset are the easiest to price, and in most cases
numerical calculation is straightforward and would
likely not beneﬁt by the use of a quantum computer.
Path-independent options on multiple assets are only
slightly harder to price since more than one asset is
now involved and the probability distributions must
account for correlations between the assets, but usu-
ally these can be priced quite eﬃciently on classical
computers as well.
Path-dependent options on the
other hand are signiﬁcantly harder to price than path-
independent options since they require an often ex-
pensive payoﬀcalculation at multiple time points on
each path, therefore minimizing the number of paths
required for this step would lead to a signiﬁcant bene-
ﬁt in the pricing process. It is this last case where we
envision the largest impact of quantum computing.

3
Quantum Methodology

Here we outline the building blocks needed to price
options on a gate-based quantum computer. As dis-
cussed in the previous section, the critical compo-
nents are 1) represent the probability distribution P
describing the evolution of random variables X =
{X1, X2, . . . , XN} on the quantum computer, 2) con-
struct the circuit which computes the payoﬀf(X)
and 3) calculate the expectation value of the payoﬀ
EP[f(X)].
In Sec. 3.1 we show how to use Ampli-
tude Estimation to calculate the expectation value of
a function of random variables.
In Sec. 3.2 we de-
scribe the process of loading the relevant probability
distributions to a quantum register, and in Sec. 3.3 we
construct the circuits to compute the payoﬀand set
up Amplitude Estimation to estimate the expectation
value of the payoﬀ. We then have all the ingredients
to price options on a quantum computer.

3.1
Amplitude Estimation

The advantage of pricing options on a quantum com-
puter comes from the Amplitude Estimation (AE) al-
gorithm [21] which provides a quadratic speed-up over
classical Monte Carlo simulations [24, 25]. Suppose a
unitary operator A acting on a register of (n + 1)
qubits such that

A |0⟩n+1 =
√

1 −a |ψ0⟩n |0⟩+ √a |ψ1⟩n |1⟩
(1)

## Page 3

Table 1: Example of the diﬀerent option types.

Single-asset
Multi-asset
Path-independent
European put/call
Basket option
Path-dependent
Barrier & Asian options
Multi-asset
barrier options

|0⟩

Figure 1:
The quantum circuit of amplitude estimation,
where H denotes a Hadamard gate and F † the inverse QFT.

for some normalized states |ψ0⟩n and |ψ1⟩n, where
a ∈[0, 1] is unknown. AE allows the eﬃcient esti-
mation of a, i.e., the probability of measuring |1⟩in
the last qubit. This estimation is obtained with an
operator Q = AS0A†Sψ0, where S0 = 1 −2 |0⟩⟨0|
and Sψ0 = 1 −2 |ψ0⟩|0⟩⟨ψ0| ⟨0|, which is a rotation
of angle 2θa in the two-dimensional space spanned
by |ψ0⟩n |0⟩and |ψ1⟩n |1⟩.
From Eq. (1) we know
that a = sin2(θa). To obtain an approximation for
θa, AE applies Quantum Phase Estimation [26, 27]
to approximate certain eigenvalues of Q, which are
classically mapped to an estimator for a. The Quan-
tum Phase Estimation uses m additional sampling
qubits to represent result and M = 2m applications
of Q, i.e., M quantum samples. The m qubits, ini-
tialized to an equal superposition state by Hadamard
gates, are used to control diﬀerent powers of Q. Af-
ter applying an inverse Quantum Fourier Transform
(QFT), their state is measured resulting in an integer
y ∈{0, ..., M −1}, which is classically mapped to the
estimator for a, i.e.

2n−1
X

i=0

˜a = sin2(yπ/M) ∈[0, 1].
(2)

The full circuit for AE is shown in Fig. 1. The esti-
mator ˜a satisﬁes

M + π2

|a −˜a| ≤π

M 2 = O
M −1
,
(3)

with probability of at least 8/π2. This represents a
quadratic speedup compared to the O
M −1/2
con-
vergence rate of classical Monte Carlo methods [28].
To reduce the required number of qubits and the
resulting circuit depth, Suzuki et al.
have shown
that AE can be performed without requiring quantum

phase estimation while still maintaining a quadratic
speed-up [22]. To this extent, they exploit that

QkA |0⟩n |0⟩= cos ((2k + 1)θa) |ψ0⟩n |0⟩+

sin ((2k + 1)θa) |ψ1⟩n |1⟩,
(4)

and by measuring QkA |0⟩for k = 20, ..., 2m−1 for a
given m and applying a maximum likelihood estima-
tion, an approximation for θa (and hence a) can be
recovered. If we deﬁne M = 2m−1, i.e. the total num-
ber of Q-applications, and we consider N shots for
each experiment, it has been shown empirically that
the resulting estimation error scales as O(1/(M
√

N)),
i.e., the algorithm achieves the quadratic speed-up in
terms of M. We will use this approach to demontrate
results from real quantum hardware in Sec. 5.
For the option contracts we consider, the random
variables involved represent the possible values Si
the underlying asset can take, and the corresponding
probabilities pi that those values will be realized. For
an option with payoﬀf, the A operator will create
the state

2n−1
X

1 −f(Si)√pi |Si⟩|0⟩+

f(Si)√pi |Si⟩|1⟩.

p

p

i=0

(5)
Comparing Eq. (1) and Eq. (5), we can see that

2n−1
X

i=0
f(Si)pi = E[f(S)],
(6)

a =

meaning AE allows us to compute the undiscounted
price of an option given a way to represent the option’s
payoﬀas a quantum circuit and create the state of
Eq. (5).
In the following sections, we describe the
necessary components to achieve that.

3.2
Distribution loading

The ﬁrst component of our option pricing model is
the circuit that takes a probability distribution im-
plied for possible asset prices in the future and loads
it into a quantum register such that each basis state
represents a possible value and its amplitude the cor-
responding probability. In other words, given an n-
qubit register, asset prices {Si} for i ∈{0, ..., 2n −1}
and corresponding probabilities {pi}, the distribution
loading module creates the state:

## Page 4

2n−1
X

√pi |Si⟩n .
(7)

|ψ⟩n =

i=0

The analytical formulas used to price options in the
Black-Scholes-Merton (BSM) model [2, 29] assume
that the underlying stock prices at maturity follow
a log-normal distribution with constant volatility. In
[30], the authors show that log-concave probability
distributions (such as the log-normal distribution of
the BSM model) can be eﬃciently loaded in a gate-
based quantum computer. The option types consid-
ered in this paper are modeled using the underlying
BSM dynamics and thus loading the relevant proba-
bility distributions onto quantum registers does not
require prohibitive complexity.
However, in option models of practical interest,
the simpliﬁed assumptions in the BSM model fail
to capture important market dynamics, limiting the
model’s applicability in real-life scenarios. As such,
the market-implied probability distribution of the un-
derlying needs to be captured properly in order for
valuation models to accurately estimate the intrinsic
value of option contracts. To address these shortcom-
ings, Artiﬁcial Neural Networks (ANN) are becoming
increasingly more popular as a means to capture the
real-life dynamics of the relevant market parameters,
without the need to assume a simpliﬁed underlying
model [31, 32]. It is thus important to be able to eﬃ-
ciently represent distributions of ﬁnancial parameters
on a quantum computer which might not have explicit
analytical representations.
The loading of arbitrary states into quantum sys-
tems requires exponentially many gates [33], making
it ineﬃcient to model arbitrary distributions as quan-
tum gates. Since the distributions of interest are of-
ten of a special form, the limitation may be overcome
by using quantum Generative Adverserial Networks
(qGAN). These networks allow us to load a distri-
bution using a polynomial number of gates [19]. A
qGAN can learn the random distribution X under-
lying the observed data samples { x0, . . . , xk−1 } and
load it directly into a quantum state. This generative
model employs the interplay of a classical discrimina-
tor, a neural network [34], and a quantum generator
(a parametrized quantum circuit). More speciﬁcally,
the qGAN training consists of alternating optimiza-
tion steps of the discriminator’s parameters φ and the
generator’s parameters θ. After the training, the out-
put of the generator is a quantum state

2n−1
X

p

|ψ(θ)⟩n =

pi(θ) |i⟩n ,
(8)

i=0

that represents the target distribution. The n-qubit
state |i⟩n
=
|in−1...i0⟩encodes the integer i
=
2n−1in−1+...+2i1+i0 ∈{0, ..., 2n−1} with ik ∈{0, 1}
and k = 0, ..., n −1. The probabilities pi(θ) approxi-
mate the random distribution underlying the training

data. We note that the outcomes of a random vari-
able X can be mapped to the integer set {0, ..., 2n−1}
using an aﬃne mapping. Furthermore, the approach
can be easily extended to multivariate data, where we
use a separate register of qubits for each dimension
[19].
Another useful feature in the use of qGANs for load-
ing probability distributions, is the fact that we can
tailor the qGAN variational form to construct short-
depth circuits for an acceptable degree of accuracy.
This in turn allows us to evaluate the performance of
option pricing quantum circuits in near-term quan-
tum hardware where resources are still quite limited.
The use of ANNs to represent probability distribu-
tions inevitably imposes a cost associated with the
training component, in both classical and quantum
models. However, during common business practices
such as overnight risk assessment of large portfolios
which may consist of millions of option contracts, the
same probability distributions can be used across a
large number of pricing calls deﬁned on the same un-
derlyings.
For example, it is quite common during
risk assessment valuations to require pricing of several
thousands of option contracts deﬁned on the same un-
derlying. As such, the eﬀective training cost per pric-
ing call can be eﬃciently amortized to represent only
a small fraction of the total individual option pricing
cost.
It is also noteworthy that the qGAN training per-
forms better if the initial distribution is close to the
target distribution [19].
Therefore, as new market
data comes in which needs to be incorporated into
the probability distribution (e.g. for overnight risk, a
lot of the same options as the day before need to be
priced, but there is one more day’s worth of market
data) the previously trained qGAN can be used as the
initial distribution, leading to faster convergence.

3.3
Computing the payoﬀ

We obtain the expectation value of a linear function
f of a random variable X with AE by creating the
operator A such that a = E[f(X)], see Eq. (6). Once
A is implemented we can prepare the state in Eq. (1),
and the Q operator, which only requires A and generic
quantum operations [26, 27]. In this section, we show
how to create a close relative of A and how to combine
it with AE to calculate the expectation value of f.
The payoﬀfunction for the option contracts of in-
terest is piece-wise linear and as such we only need
to consider linear functions f : {0, ..., 2n −1} →[0, 1]
which we write f(i) = f1i + f0. We can eﬃciently
create an operator that performs

|i⟩n |0⟩→|i⟩n (cos [f(i)] |0⟩+ sin [f(i)] |1⟩)
(9)

using controlled Y-rotations [17]. To implement the
linear term of f(i) each qubit j (where j ∈{0, . . . n −

## Page 5

|i⟩3
•

≡

|0⟩
Ry[f(i)]

Figure 2: Quantum circuit that creates the state in Eq. (9).
Here, the independent variable i = 4i2 +2i1 +i0 ∈{0, ..., 7}
is encoded by three qubits in the state |i⟩3 = |i2i1i0⟩with
ik ∈{0, 1}. Therefore, the linear function f(i) = f1i + f0 is
given by 4f1i2 +2f1i1 +f1i0 +f0. After applying this circuit
the quantum state is |i⟩3 [cos(f1i+f0) |0⟩+sin(f1i+f0) |1⟩].
The circuit on the right shows an abbreviated notation.

1}) in the |i⟩n register acts as a control for a Y-
rotation with angle 2jf1 of the ancilla qubit. The con-
stant term f0 is implemented by a rotation of the an-
cilla qubit without any controls, see Fig. 2. The con-
trolled Y-rotations can be implemented with CNOT
and single-qubit gates [35].
We now describe how to obtain E[f(X)] for a linear
function f of a random variable X which is mapped
to integer values i ∈{0, ..., 2n −1} that occur with
probability pi respectively.
To do this we use the
procedure outlined immediately above to create the
operator that maps P
i
√pi |i⟩n |0⟩to

2n−1
X

√pi |i⟩n
h
cos

c ˜f(i) + π


|0⟩+ sin

c ˜f(i) + π


|1⟩
i
,

4

4

i=0

(10)

where ˜f(i) is a scaled version of f(i) given by

˜f(i) = 2 f(i) −fmin

fmax −fmin
−1,
(11)

with fmin = mini f(i) and fmax = maxi f(i), and
c ∈[0, 1] is an additional scaling parameter. The re-
lation in Eq. (11) is chosen so that ˜f(i) ∈[−1, 1].
Consequently, sin2[c ˜f(i) + π/4] is an anti-symmetric
function around ˜f(i) = 0.
With these deﬁnitions,
the probability to ﬁnd the ancilla qubit in state |1⟩,
namely

2n−1
X

i=0
pi sin2 
c ˜f(i) + π


,

P1 =

4

is well approximated by

2n−1
X


= c2E[f(X)] −fmin


c ˜f(i) + 1

fmax −fmin
−c + 1

P1 ≈

i=0
pi

2.

2

(12)

To obtain this result we made use of the approxima-
tion

sin2 
c ˜f(i) + π


= c ˜f(i) + 1

2 + O(c3 ˜f 3(i))
(13)

4

which is valid for small values of c ˜f(i). With this ﬁrst
order approximation the convergence rate of AE is

O(M −2/3) when c is properly chosen which is already
faster than classical Monte Carlo methods [17]. We
can recover the O(M −1) convergence rate of AE by
using higher orders implemented with quantum arith-
metic.
The resulting circuits, however, have more
gates. This trade-oﬀ, discussed in Ref. [17], also gives
a formula that speciﬁes which value of c to use to
minimize the estimation error made when using AE.
From Eq. (12) we can recover E[f(X)] since AE al-
lows us to eﬃciently retrieve P1 and because we know
the values of fmin, fmax and c.

4
Option pricing on a quantum com-
puter

In this section we show how to price the diﬀerent op-
tions shown in Tab. 1. We put an emphasis on the
implementation of the quantum circuits that prepare
the states needed by AE. We use the diﬀerent building
blocks reviewed in Sec. 3.

4.1
Path-independent options

The price of path-independent vanilla options (e.g.
European call and put options) depends only on the
distribution of the underlying asset price ST at the op-
tion maturity T and the payoﬀfunction f(ST ) of the
option. To encode the distribution of ST in a quan-
tum state, we truncate it to the range [ST,min, ST,max]
and discretize this interval to {0, ..., 2n −1} using n
qubits.
In the quantum computer, the distribution
loading operator PX creates a state

2n−1
X

√pi |i⟩n ,
(14)

|0⟩n
PX
−−→|ψ⟩n =

i=0

with i ∈{0, ..., 2n−1} to represent ST . This state, ex-
empliﬁed in Fig. 3, may be created using the methods
discussed in Sec. 3.2.
We start by showing how to price vanilla call or put
options, and then generalize our method to capture
the payoﬀstructure of portfolios containing more than
one vanilla option.

4.1.1
Vanilla options

Vanilla call options are structured so that if the un-
derlying asset price is larger than a ﬁxed value K
(the strike price) at the expiration date, the contract
pays the diﬀerence between the realized price and the
strike. As such, the call option payoﬀfC(ST ) can be
written as

fC(ST ) = max(0, ST −K).
(15)

Equivalently, the corresponding put option has a sim-
ilar payoﬀbut it pays if the asset price at expiry is

## Page 6

Figure 3: Example price distribution at maturity loaded in a
three-qubit register. In this example we followed the Black-
Scholes-Merton model which implies a log-normal distribu-
tion of the asset price at maturity T with probability density

2πT exp

−(ln ST −µ)2

2σ2T

.
σ is the

function P(ST ) =
1
ST σ
√

volatility of the asset and µ =
r −0.5σ2
T + ln(S0), with
r the risk-free market rate and S0 the asset’s spot at t = 0.
In this ﬁgure we used S0 = 2, σ = 10%, r = 4% and
T = 300/365.

smaller than the strike. That is, the put option payoﬀ
is

fP (ST ) = max(0, K −ST ).
(16)

The linear part of the payoﬀcan be computed as
a quantum circuit with the approach outlined in
Sec. 3.3, but we need a way to express the max oper-
ation as a quantum circuit as well. We show how to
achieve that for both call and put option types by im-
plementing a comparison between the values encoded
in the basis states of Eq. (14) and K.
A quantum comparator circuit sets an ancilla qubit
|c⟩, initially in state |0⟩, to the state |1⟩if i ≥K
and |0⟩otherwise.
The state |ψ⟩n in the quantum
computer therefore undergoes the transformation

i<K

X

i≥K

√pi |i⟩n |0⟩+
X

√pi |i⟩n |1⟩.

|ψ⟩n |0⟩→|φ1⟩=
X

i≥K

i<K

This operation can be implemented by a quantum
comparator [36] based on CNOT and Toﬀoli gates.
Since we know the value of the strike, we can im-
plement a circuit tailored to the speciﬁc strike price.
We use n ancilla qubits |a1, ..., an⟩and compute the
two’s complement of the strike price K in binary us-
ing n bits, storing the digits in a (classical) array
t[n].
For each qubit |ik⟩in the |i⟩n register, with
k ∈{0, ..., n −1}, we compute the possible carry bit
of the bitwise addition of |ik⟩and t[k] into |ak⟩. If
t[k] = 0, there is a carry qubit at position k only if
there is a carry at position k −1 and |ik⟩= 1. If
t[k] = 1, there is a carry qubit at position k if there
is a carry at position k −1 or |ik⟩= 1. After going

through all n qubits from least to most signiﬁcant,
|i⟩n will be greater or equal to the strike price, only
if there is a carry at the last (most signiﬁcant) qubit.
This procedure along with the necessary gate opera-
tions is illustrated in Fig. 4. An implementation for
K = 1.9 and a three-qubit register is shown in Fig. 6.
To represent the payoﬀfunction f(i), we add to
|φ1⟩a second ancilla qubit, which corresponds to the
last qubit in Eq. (10). The payoﬀfunction of vanilla
options is piece-wise linear

(
a< · i + b<
i < K,
a≥· i + b≥
i ≥K.
(17)

f(i) =

We now focus on a European call option with payoﬀ
f(i) = max(0, i −K), i.e., a< = b< = 0, a≥= 1, and
b≥= −K. To prepare the operator that calculates
the payoﬀin the form of Eq. (10) for use with AE, we
set

(
g0
i < K,
g0 + g(i)
i ≥K,

c ˜f(i) + π

4 =

where g(i) is a linear function of i, and g0 is an angle
whose value we will carefully select. With this setup,
the payoﬀin Eq. (10) can be constructed, starting
from the state |φ1⟩|0⟩, by ﬁrst initializing the last
ancilla qubit to the state cos(g0) |0⟩+ sin(g0) |1⟩, and
then performing a rotation of the last ancilla qubit
controlled by the comparator qubit |c⟩and the qubits
in |ψ⟩n. This rotation operation, implemented by the
quantum circuit in Fig. 7, applies a rotation with an
angle g(i) only if i ≥K. The state of the n+2 qubits
after this operation becomes
X

√pi |i⟩n |0⟩[cos(g0) |0⟩+ sin(g0) |1⟩] +
(18)

√pi |i⟩n |1⟩{cos[g0 + g(i)] |0⟩+ sin[g0 + g(i)] |1⟩} .

The probability to ﬁnd the second ancilla in state |1⟩,
eﬃciently measurable using AE, is

P1 =
X

i<K
pi sin2(g0) +
X

i≥K
pi sin2[g0 + g(i)].
(19)

Now, we must carefully choose the angle g0 and the
function g(i) to recover the expected payoﬀE[f(X)]
of the option from P1 using the approximation in
Eq. (12). To reproduce f(i) = i −K for i ≥K and
simultaneously satisfy c ˜f(i) = g0+g(i)−π/4 ∈[−c, c]
(see Eq. (11)), we must set

g(i) = 2c(i −K)

imax −K ,
(20)

where imax = 2n −1. This choice of g(i) forces us to
choose

g0 = π

4 −c.
(21)

## Page 7

t[1] = 1

Figure 4: Circuit that compares the value represented by an n-qubit register |i⟩n, to a ﬁxed value K. We use n ancilla qubits
|a1, ..., an⟩, a classical array t[n] holding the precomputed binary value of K’s two’s complement and a qubit |c⟩which will
hold the result of the comparison with |c⟩= 1 if |i⟩≥K. For each qubit |ik⟩, with k ∈{1, ..., n}, we use a Toﬀoli gate to
compute the carry at position k if t[k] = 1 and a logical OR, see Fig. 5, if t[k] = 0. For k = 1, we only need to use a CNOT
on |i1⟩if t[1] = 1. In the circuit above, only one of two unitaries in a dotted box needs to be added to the circuit, depending
on the value of t[k] at each qubit. The last carry qubit |an⟩is then used to compute the ﬁnal result of the comparison in
qubit |c⟩.

|a⟩
X
•
X
•
|b⟩
X
•
X
≡
•
|c⟩
X
OR

Figure 5:
Circuit that computes the logical OR between
qubits |a⟩and |b⟩into qubit |c⟩. The circuit on the right
shows the abbreviated notation used in Fig. 4.





|0⟩



|i⟩3

Figure 6: Quantum circuit that sets a comparator qubit |c⟩
to |1⟩if the value represented by |i⟩3 is larger than a strike
K = 1.9, for the spot distribution in Fig. 3. The unitary PX
represents the set of gates that load the probability distribu-
tion in Eq. (14). An ancilla qubit |a⟩is needed to perform
the comparison. It is uncomputed at the end of the circuit.

Figure 7:
Circuit that creates the state in Eq. (18). We
apply this circuit directly after the comparator circuit shown
in Fig. 6. The multi-controlled y-rotation is the gate shown
in Fig. 2 controlled by the ancilla qubit |c⟩that contains the
result of the comparison between i and K.

To see why, we substitute Eqs. (20) and (21) into
Eq. (19) and use the approximation in Eq. (13), which
leads to

1

2 −c

+
X

2c(i −K)

2 −c


imax −K + 1

P1 ≈
X

i<K
pi

i≥K
pi

2 −c +
2c
imax −K

= 1

X

i≥K
pi(i −K),
(22)

where we have used P

i pi = 1 in the last equality.
Eq. (22) shows that by setting g0 = π/4 −c, we could
recover E[max(0, i−K)] from P1 up to a scaling factor
and a constant, from which we can subsequently re-
cover the expected payoﬀE[f(i)] of the option given
the probability distribution of the underlying asset.
We should note that the fair value of the option re-
quires appropriately discounting the expected payoﬀ
of the option to today, but as the discounting can be
performed after the expectation value has been cal-
culated, we omit it from our discussion for simplic-
ity. We demonstrate the performance of our approach
by running amplitude estimation using Qiskit [37] on
the overall circuit produced by the elements described
in this section, and verifying the convergence to the

## Page 8

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

analytically computed value or classical Monte Carlo
estimate. An illustration of the convergence of a Eu-
ropean call option with increasing evaluation qubits
is shown in Fig. 8.
A straightforward extension of the analysis above
yields a pricing model for a European put option,
whose payoﬀf(i) = max(0, K −i) is equivalent to
Eq. (17) with a> = b> = 0, a≤= −1, and b≤= K.

4.1.2
Portfolios of options

Various popular trading and hedging strategies rely
on entering multiple option contracts at the same time
instead of individual call or put options and as such,
these strategies allow an investor to eﬀectively con-
struct a payoﬀthat is more complex than that of
vanilla options. For example, an investor who wants
to proﬁt from a volatile asset without picking a di-

Figure 9:
Quantum circuit that implements the multi-
controlled Y-rotations for a portfolio of options with m strike
prices.

rection of where the volatility may drive the asset’s
price, may choose to enter a straddle option strategy,
by buying both a call and a put option on the asset
with the same expiration date and strike. If the un-
derlying asset moves sharply up to expiration date,
the investor can make a proﬁt regardless of whether
it moves higher or lower in value. Alternatively, the
investor may opt for a butterﬂy option strategy by en-
tering four appropriately structured option contracts
with diﬀerent strikes simultaneously. Because these
option strategies give rise to piecewise linear payoﬀ
functions, the methodology described in the previous
section can be extended to calculate the fair values of
these option portfolios.
In order to capture the structure of such option
strategies, we can think of the individual options as
deﬁning one or more eﬀective strike prices Kj and
add a linear function fj(S) = ajS+bj between each of
these strikes. For example, to price an option strategy
with the payoﬀfunction

fs(S) = max(0, S −K1) −max(0, S −K2),
(23)

which corresponds to a call spread (the option holder
has purchased a call with strike K1 and sold a call
with strike K2), we use functions f0, f1, and f2 such
that





f0(S)
S < K1,
f0(S) + f1(S)
K1 ≤S < K2,
f0(S) + f1(S) + f2(S)
K2 ≤S.
(24)

fs(S) =




To match Eq. (23) with Eq. (24), we set f0(S) = 0,
f1(S) = S −K1 and f2(S) = −S + K2.
In gen-
eral, to price a portfolio of options with m eﬀective-
strike prices K1, ..., Km and m+1 functions f0(S), ...,
fm(S), we need an ancilla qubit per strike to indicate
if the underlying has reached the strike. This allows
us to generalize the discussion from Sec. 4.1.1. We
apply a multi-controlled Y-rotation with angle gj(i) if
i ≥Kj for each strike Kj with j ∈{1, ..., m}. The ro-
tation g0(i) is always applied, see the circuit in Fig. 9.
The functions gj(i) are determined using the same
procedure as in Sec. 4.1.1.

## Page 9

4.2
Multi-asset and path-dependent options

In this section we show how to price options with
path-dependent payoﬀs as well as options on more
than one underlying asset. In these cases, the pay-
oﬀfunction depends on a multivariate distribution of
random variables {Sj} with j ∈{1, ..., d}. The Sj’s
may represent one or several assets at discrete mo-
ments in time or a basket of assets at the option ma-
turity. In both cases, the probability distribution of
the random variables Sj are truncated to the inter-
val [Sj,min, Sj,max] and discretized using 2nj points so
that they can be represented by d quantum registers
where register j has nj qubits. Thus, the multivariate
distribution is represented by the probabilities pi1,...,id
that the underlying has taken the values i1, ..., id with
ij ∈{0, ..., 2nj −1}. The quantum state that repre-
sents this probability distribution, a generalization of
Eq. (14), is

...

√pi1,...,id |i1⟩n1 ⊗... ⊗|id⟩nd ,
(25)

|ψ⟩n =
X

i1,...,id

with n = P

j nj. Various types of options, such as
Asian options or basket options, require us to compute
the sum of the random variables Sj. The addition of
the values in two quantum registers |a, b⟩→|a, a + b⟩
may be calculated in quantum computers with adder
circuits based on CNOT and Toﬀoli gates [38–40].
To this end we add an extra qubit register with n′

qubits to serve as an accumulator. By recursively ap-
plying adder circuits we perform the transformation
|ψ⟩n |0⟩n′ →|φ⟩n+n′ where |φ⟩n+n′ is given by

√pi1,...,id |i1⟩n1 ⊗... ⊗|id⟩nd ⊗|i1 + ... + id⟩n′ .

X

i1,...,id

(26)

Here circuit optimization may allow us to perform this
computation in-place to minimize the number of qubit
registers needed. Now, we use the methods discussed
in the previous section to encode the option payoﬀs
into the quantum circuit.

4.2.1
Basket Options

A European style basket option is an extension of the
single asset European option discussed in Sec. 4.1,
only now the payoﬀdepends on a weighted sum of
d underlying assets. A call option on a basket has the
payoﬀproﬁle

f(Sbasket) = max(0, Sbasket −K)
(27)

where Sbasket
=
⃗w · ⃗S, for basket weights ⃗w =
[w1, w2, . . . , wd], wi ∈[0, 1], underlying asset prices
at option maturity ⃗S = [S1, S2, . . . Sd] and strike K.
In the BSM model, the underlying asset prices are de-
scribed by a multivariate log-normal distribution with
probability density function [41]

|i1⟩n1

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

2(ln S −µ)T Σ−1(ln S −µ)


P(⃗S) = exp
−1

(2π)d/2(detΣ)1/2 Qd
i=1 Si
,
(28)

where ln S
=
(ln S1, ln S2 . . . , ln Sd)T
and µ
=
(µ1, µ2 . . . µd)T , where each µi is the log-normal distri-
bution parameter for each asset deﬁned in the caption
of Fig. 3. Σ is the d × d positive-deﬁnite covariance
matrix of the d underlyings





σ2
1
ρ12σ1σ2
. . .
ρ1dσ1σd
ρ21σ2σ1
σ2
2
. . .
ρ2dσ2σd
...
...
...
...
ρd1σdσ1
. . .
. . .
σ2
d




(29)

Σ = T

with σi the volatility of the ith asset, and −1 ≤ρij ≤
1 the correlation between assets i and j and T the
time to maturity.
The quantum circuit for pricing a European style
basket call option is analogous to the single asset case,
with an additional unitary to compute the weighted
sum of the uncertainty registers |i1⟩n1 . . . |id⟩nd be-
fore applying the comparator and payoﬀcircuits,
controlled
by
the
accumulator
register
|b⟩n′
=
|i1 + ... + id⟩n′. A schematic of these components is
shown in Fig. 10. The implementation details of the
circuit that performs the weighted sum operator is
discussed in Appendix A.
We use a basket option to compare the estima-
tion accuracy between AE and classical Monte Carlo.
From Eq. (2), we know that for M applications of
the Q operator (see Fig. 1), the possible values re-
turned by AE will be of the form sin2(yπ/M) for

## Page 10

y ∈{0, ..., M −1} and the maximum distance between
two consecutive values is

∆max = sin2
π


−sin2
π


.
(30)

4 + 2π

4 −2π

4M

4M

This quantity determines how close M operations of Q
can get us to the amplitude which encodes the option
price.
Using sin2(π/4 + x) = x + 1/2 + O(x3) for
x ≪1, we get ∆max = π/M + O(M −3) for π/M ≪1.
From Eq. (3) and Eq. (22), we can determine that
with probability of at least 8/π2, our estimated option
price using AE will be within

∆O
max = π/M

2c
× (imax −K) + O(M −3)
(31)

of the exact option price, where c, imax and K are
the parameters used to encode the option payoﬀinto
our quantum circuit, discussed in Sec. 4.1.1. To com-
pare this estimation error to Monte Carlo, we use the
same number of samples to price an option classically,
and determine the approximation error at the same
8/π2 ≈81% conﬁdence interval by repeated simula-
tions. The comparison for a basket option on three
underlying assets shows that AE provides a quadratic
speed-up, see Fig. 11. It is worth noting that for typ-
ical business cases, the number of paths required for
acceptable pricing accuracy goes from tens of thou-
sands to millions (depending on the option under-
lyings) [42, 43], so they are well within the range
where amplitude estimation becomes more eﬃcient
than Monte Carlo, as shown in Fig. 11.

4.2.2
Asian Options

We now examine arithmetic average Asian options
which are single-asset, path-dependent options whose
payoﬀdepends on the price of the underlying asset
at multiple time points before the option’s expiration
date. Speciﬁcally, the payoﬀof an Asian call option
is given by

f( ¯S) = max(0, ¯S −K)
(32)

where K is the strike price, ¯S is the arithmetic average
of the asset’s value over a pre-deﬁned number of points
d between 0 and the option maturity T

d
X

¯S = 1

t=1
St.
(33)

d

The probability distribution of the asset price at
time t will again be log-normal with probability den-
sity function

P(St) =
1

2π∆t
e−(ln St−µt)2

Stσ
√

2σ2∆t
,
(34)

with µt =
r −0.5σ2
∆t + ln(St−1) and ∆t = T/d.
We can then use the multivariate distribution in

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

Eq. (28), with ⃗S now a d-dimensional vector of as-
set prices at time points [t1 . . . td], instead of dis-
tinct underlying prices at maturity T.
As we are
not considering multiple underlying assets that could
be correlated, the covariance matrix is diagonal Σ =
∆t[diag(σ2, ..., σ2)]. An illustration of the probability
density function used for an asset deﬁned on two time
steps is shown in Fig. 12.
We now prepare the state |ψ⟩n, see Eq. (25), where
each register represents the asset price at each time
step up to maturity. Using the weighted sum opera-
tor of Appendix A with equal weights 1/d, we then
calculate the average value of the asset until maturity
T, see Eq. (33), into a register | ¯S⟩

d
X

| i1
|{z}
∆t
i2
|{z}
2∆t
... id
|{z}
T
⟩7→| ¯S⟩= |1

t=1
St⟩.
(35)

d

Finally, we use the same comparator and rotation cir-
cuits that we employed for the basket option illus-
trated in Fig. 10 to load the payoﬀof an arithmetic
average Asian option into the payoﬀqubit |p⟩.

4.2.3
Barrier Options

Barrier options are another class of popular option
types whose payoﬀis similar to vanilla European op-
tions, but they become activated or extinguished if
the underlying asset crosses a pre-determined level
called the barrier. In their simplest form, there are
two general categories of barrier options

## Page 11

Figure 12: Probability density function of a multivariate log-
normal distribution, see Eq. (28), for the asset shown in Fig. 3
deﬁned on two time steps t = ∆t = T/2 and t = 2∆t = T

• Knock-Out The option expires worthless if the
underlying asset crosses a certain price level be-
fore the option’s maturity.

• Knock-In The option has no value unless the un-
derlying asset crosses a certain price level before
maturity.

If the required barrier event for the option to have
value at maturity occurs, the payoﬀthen depends only
on the value of the underlying asset at maturity and
not on the path of the asset until then. If we consider
a Knock-In barrier option and label the barrier level
B, we can write the option’s payoﬀas

(
max(0, ST −K)
if ∃t s.t. St ≥B
0
otherwise
(36)

f(S) =

where T is the time to maturity, St the asset price at
time t with 0 < t ≤T and K the option strike.
To construct a quantum circuit to price a Knock-
In barrier option, we use the same method as for
the Asian option where T is divided into d equidis-
tant time intervals with ∆t = T/d, and use regis-
ters |i1⟩n1 |i2⟩n2 . . . |id⟩nd to represent the discretized
range of asset prices at time t ∈{∆t, 2∆t, . . . , d·∆t =
T}. The probability distribution of Eq. (34) is used
again to create the state |ψ⟩n in Eq. (25).
To capture the path dependence introduced by the
barrier, we use an additional d-qubit register |b⟩d to
monitor if the barrier is crossed. Each qubit |bt⟩in
|b⟩d is set to |1⟩if |it⟩nt ≥B. An ancilla qubit |b|⟩
is set to |1⟩if the barrier has been crossed in at least
one time step. This is done by computing the logical
OR, see Fig. 5, of every qubit in |b⟩d and storing the
result in the ancilla

|b1b2 . . . bd⟩|0⟩7→|b1b2 . . . bd⟩|b1 || b2 . . . || bd⟩.
(37)

Table 2: Single-qubit, CNOT, Toﬀoli gate counts and over-
all circuit depth required for the full amplitude estimation
circuits for each instance in Fig. 8, as a function of the num-
ber of sampling qubits m.
These ﬁgures assume all-to-all
connectivity across qubits.

This is computed with X (NOT) and Toﬀoli gates
and d −2 ancilla qubits.
The ancilla qubit |b|⟩is
then used as a control for the payoﬀrotation into the
payoﬀqubit, eﬀectively knocking the option in. For
Knock-Out barrier options, we can follow the same
steps and apply an X gate to the ancilla barrier qubit
before using it as control, in this manner knocking
the option out if the barrier level has been crossed. A
circuit displaying all the components required to price
a Knock-In barrier option is shown in Fig. 13. Results
from amplitude estimation on a barrier option circuit
using a quantum simulator are shown in Fig. 14.
Even though we have focused our attention on bar-
rier options where the barrier event is the underlying
asset crossing a barrier from below, we can use the
same method to price barrier options where barrier
events are deﬁned as the asset crossing the value from
above. This only requires changing the comparator
circuits to compute St ≤B in the barrier register
|b⟩d.
For all path-dependent options, including the Asian
and barrier options we have examined in this section,
we note that the choice of time intervals on which
we need to represent the probability distribution on
quantum registers depends on the type of option in
question and the type of underlying(s). For instance,
when pricing barrier options, we only need to repre-
sent the probability distribution at the barrier dates
and at maturity.
However, as the choice of which
time intervals need to be represented for option pric-
ing is independent of whether we employ a quantum
or a classical pricing model, a detailed analysis of this
choice is beyond the scope of this work.

5
Quantum hardware results

In this section we examine the performance of Euro-
pean call option circuits evaluated on quantum hard-
ware. Quantum circuits based on standard amplitude
estimation are not promising candidates for near-term
devices, given that they require extra qubits to control
the accuracy of the calculation, and multi-controlled
gate operations. Tab. 2 lists the number of single and
multi-qubit gates required for the European call op-

## Page 12

|i1⟩n1

Figure 13:
Circuit that encodes the payoﬀof a Knock-In barrier option in the state of an ancilla qubit |p⟩1. The unitary
operator PX is used to initialize the state of Eq. (25). Comparator circuits CB are used to set a barrier qubit bj for all j ∈[1, d]
if the asset price represented by |ij⟩crosses the barrier B. The logical OR of all bj qubits is computed into ancilla |b|⟩. The
strike comparator circuit CK sets the comparator qubit |c⟩1 to |1⟩if the asset price at maturity |id⟩≥K. Finally, Y-rotations
encode the payoﬀqubit |p⟩1, controlled on |id⟩, the strike qubit |c⟩1 and the barrier qubit |b|⟩which is |1⟩only if the asset
price has crossed the barrier at least once before maturity.

tion examples in Fig. 8, all of which are far from the
reach of current and near-term quantum hardware.
However, a quadratic speed-up is also possible by
performing AE without quantum phase estimation
(see Sec. 3.1).
Even though removing phase esti-
mation from amplitude estimation does not make
the overall algorithm immediately compatible with
noisy quantum computers, it does lead to signiﬁcantly
shorter circuits than the original implementation of
AE, allowing us to examine how it performs on noisy
quantum hardware.
We hence focus on the circuits required to perform
AE without phase estimation and show results for a
European call option, using three qubits, two of which
represent the uncertainty and one encodes the pay-
oﬀ.
We consider a log-normal random distribution
with S0 = 2, σ = 40%, r = 5%, and T = 40/365,
see Fig. 3, and truncate the distribution to the inter-
val deﬁned by three standard deviations around the
mean.
With two qubits encoding this distribution,
the possible values are [1.21, 1.74, 2.28, 2.81], repre-
sented by |00⟩, . . . , |11⟩, with corresponding probabil-
ities 0.1%, 55.4%, 42.5%, and 1.9%. We set the strike
price to K = 1.74.
To examine the behavior of the circuit for diﬀerent
input probability distributions, we run eight experi-
ments that diﬀer by the initial spot price S0 and all
other parameters are kept constant. The spot price
is varied from 1.8 to 2.5 in increments of 0.1. This
way we can use the same circuit for all experiments
and only vary the Y-rotation angles used to map the
initial probability distribution onto the qubit register.
This choice of input parameters allows us to evaluate
our circuits for expected option prices in the range
[0.0754, 0.7338].
Following the procedure detailed in Sec. 3.1, we con-
struct the circuits for A |0⟩3 and QA |0⟩3, which corre-
spond to k = 0, 1 (i.e. m = 1) in Eq. (4), with n = 2.

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

## Page 13

We then perform repeated measurements of the cir-
cuits, and by combining the measured probabilities for
all k in a single likelihood function, we can perform a
maximum likelihood estimation for θa, hence obtain-
ing an estimate for a = E[f(S)] (see Eq. (6)), i.e. the
expected payoﬀ. Each experiment is evaluated on the
IBM Q Tokyo 20-qubit device with 8192 shots. We
repeat each 8192-shot experiment 20 times and av-
erage over the 20 measured probabilities in order to
limit the eﬀect of any one-oﬀissues with the device.
The standard deviation of the measured probabilities
across the 20 runs was always < 2%. The connec-
tivity of IBM Q Tokyo allows to choose three fully
connected qubits for the experiments, and thus, no
swaps are required to implement any two-qubit gate
in our circuits [37]. For all circuits described in the
following sections, we used qubits 6, 10 and 11.
Note that even though we are only interested in the
result of a single qubit, we always measure all three
qubits to be able to apply readout error mitigation as
discussed later in Sec. 5.2.

5.1
Algorithm and Operators

We now show how to construct the operator A that is
required for AE. The log-normal distribution on two
qubits can be loaded using a single CNOT gate and
four single-qubit rotations [44]. To encode the payoﬀ
function, we also exploit the small number of qubits
and apply a uniformly controlled Y-rotation instead
of the generic construction using comparators intro-
duced in Sec. 4. A uniformly controlled Y-rotation,
i.e.

|i⟩n |0⟩→|i⟩n Ry(θi) |0⟩,
(38)

implements a diﬀerent rotation angle θi, i = 0, ..., 2n−
1 for each state of the n-control qubits. For n = 2,
this operation can be eﬃciently implemented using
four CNOT gates and four single qubit Y-rotations
[45, 46].
The resulting circuit implementing A is
shown in Fig. 15. Note that in our setup, diﬀerent
initial distributions only lead to diﬀerent angles of
the ﬁrst four Y-rotations and do not aﬀect the rest
of the circuit.
Although we use a uniformly con-
trolled rotation, the rotation angles are constructed
in the same way described in Sec. 3.3. We use an ap-
proximation scaling of c = 0.25 and the resulting an-
gles are [θ0, . . . , θ3] = [1.1781, 1.1781, 1.5708, 1.9635],
which shows the piecewise linear structure of the pay-
oﬀfunction.
The total resulting circuit requires ﬁve CNOT gates
and eight single-qubit Y-rotations, see Fig. 15. Since
we use uniformly controlled rotations, we do not need
any ancilla qubit. Note that if we want to evaluate the
circuit for A alone, we can replace the last CNOT gate
in Fig. 15 by classical post-processing of the measure-
ment result: if q1 is measured as |1⟩, we ﬂip q2 and
otherwise we do nothing.
This further reduces the
overall CNOT gate count to four.

In the remainder of this section, we focus on
QA |0⟩3, i.e., the outlined algorithm for m = 1, to
examine the reach of today’s quantum hardware in
evaluating AE option pricing circuits which do not
require phase estimation. We note that this evalua-
tion is relevant to any quantum algorithm realizing
AE without phase estimation and is independent of
the approach described in [22] or any other particular
implementation.
After optimzing the gate count, the resulting circuit
for QA |0⟩3 consists of 18 CNOT gates and 33 single-
qubit gates. The detailed circuit diagram and applied
circuit optimization steps are provided in Appendix
B.

5.2
Error mitigation and results

We run the circuits for A |0⟩3 and QA |0⟩3 on noisy
quantum hardware. The results are aﬀected by read-
out errors and errors that occur during the execution
of the circuits.
To mitigate readout errors we run a calibration se-
quence in which we individually prepare and measure
all eight basis states [37, 47]. The result is a 8 × 8
readout-matrix R that holds the probability of mea-
suring each basis state as function of the basis state in
which the system was prepared. We use R to correct
all subsequent measurements. The error we measure
on P1 for A |0⟩3 was reduced from ∼6% to ∼4%
using readout error mitigation.
Errors occuring during the quantum circuit can be
mitigated using Richardson extrapolation [48]. First,
the quantum circuit is run using a rescaled Hamil-
tonian to amplify the eﬀect of the noise. Second, a
Richardson extrapolation is used to extract the re-
sult of the quantum circuit at the zero noise limit.
In hardware, error mitigation is done by stretching
the duration of the gates. For each stretch factor the
qubit gates need to be recalibrated [8]. Here, we use a
simpliﬁed error mitigation protocol that circumvents
the need to recalibrate the gates but still allows us to
increase the accuracy of the quantum hardware [49].
Since the single-qubit and CNOT gates have an aver-
age randomized benchmarking ﬁdelity of 99.7% and
97.8%, respectively, we restrict our error mitigation
to the CNOT gates. Furthermore, because the opti-
mized circuit for A |0⟩3 contains only 4 CNOT gates,
we employ the error mitigation protocol only when
evaluating QA |0⟩3 which consists of 18 CNOT gates.
We run the circuit for QA |0⟩3 three times. In each
run we replace the CNOT gates of the original cir-
cuit by one, three and ﬁve CNOT gates for a total
of 18, 54, and 90 CNOT gates, respectively.
Since
a pair of perfect CNOT gates simpliﬁes to the iden-
tity these extra gates allow us to amplify the error
of the CNOT gate without having to stretch the gate
duration, thus, avoiding the need to recalibrate the
gate parameters. As the number of CNOT gates is

## Page 14

Loading random distribution
Evaluating payoﬀfunction

|q1⟩
Ry
2.90

Figure 15: The A operator of the considered European call option: ﬁrst, the 2-qubit approximation of a log-normal distribution
is loaded, and second, the piecewise linear payoﬀfunction is applied to last qubit controlled by the ﬁrst two. This operator
can be used within amplitude estimation to evaluate the expected payoﬀof the corresponding option.

increased the probability of measuring |1⟩tends to-
wards 0.5 for all initial spot prices, see Fig. 16(b).
After applying a second-order Richardson extrapola-
tion, i.e quadratic extrapolation, we recover the same
behavior as the option price obtained from classical
simulations, see Fig. 16(c).
Our simple error miti-
gation scheme dramatically increased the accuracy of
the calculated option price: it reduced the error, av-
eraged over the initial spot price, from 62% to 21%.

6
Conclusion

We have presented a methodology and the quantum
circuits to price options and option portfolios on a
gate-based quantum computer. We showed how to ac-
count for some of the more complex features present
in exotic options such as path-dependency with bar-
riers and averages.
The results that we show are
available in the ﬁnance module in Qiskit [37].
Fu-
ture work may involve calculating the price derivatives
[50] with a quantum computer. Pricing options relies
on AE. This quantum algorithm allows a quadratic
speed-up compared to traditional Monte Carlo simu-
lations, but will most likely require a universal fault-
tolerant quantum computer [51]. However, research
to improve the algorithms is ongoing [52–54]. Here
we have used a new algorithm [22] that retains the
AE speed-up but that uses less gates to measure the
price of an option. Furthermore, we employed a sim-
ple error mitigation scheme that allowed us to greatly
reduce the errors from the noisy quantum hardware.
However, larger quantum hardware capable of run-
ning deeper quantum circuits with more qubits than
the currently available quantum computers is needed
to price the typical portfolios seen in the ﬁnancial
industry.
Future work could focus on reducing the
number of quantum registers in our implementation
by performing some of the computation in-place.

7
Acknowledgments

The authors want to thank Abhinav Kandala for the
very constructive discussions on error mitigation and
real quantum hardware experiments. C.Z. and R.I.
acknowledge the support of the National Centre of
Competence in Research Quantum Science and Tech-
nology (QSIT).

Opinions and estimates constitute our judgment as
of the date of this Material, are for informational pur-
poses only and are subject to change without notice.
This Material is not the product of J.P. Morgan’s Re-
search Department and therefore, has not been pre-
pared in accordance with legal requirements to pro-
mote the independence of research, including but not
limited to, the prohibition on the dealing ahead of
the dissemination of investment research. This Ma-
terial is not intended as research, a recommendation,
advice, oﬀer or solicitation for the purchase or sale
of any ﬁnancial product or service, or to be used in
any way for evaluating the merits of participating in
any transaction. It is not a research report and is not
intended as such. Past performance is not indicative
of future results.
Please consult your own advisors
regarding legal, tax, accounting or any other aspects
including suitability implications for your particular
circumstances. J.P. Morgan disclaims any responsi-
bility or liability whatsoever for the quality, accuracy
or completeness of the information herein, and for any
reliance on, or use of this material in any way. Impor-
tant disclosures at: www.jpmorgan.com/disclosures

IBM, IBM Q, Qiskit are trademarks of Interna-
tional Business Machines Corporation, registered in
many jurisdictions worldwide. Other product or ser-
vice names may be trademarks or service marks of
IBM or other companies.

## Page 15

Figure 16: Error-mitigated hardware results for A |0⟩3, QA |0⟩3 and the estimated option price after applying maximum
likelihood estimation as a function of the initial spot price S0. (a) Probability of measuring |1⟩for the QA |0⟩3 circuit (see
Appendix B, Fig. 15) (b) Probability of measuring |1⟩for the QA |0⟩3 circuit (see Fig. 19). We show the measured probabilities
when replacing each CNOT by one, three and ﬁve CNOT gates (green, orange, red, respectively), the zero-noise limit calculated
using a second-order Richardson extrapolation method (purple), and the probability measured using the simulator (blue). (c)
Option price estimated with maximum likelihood estimation from measurements of QA |0⟩3 and A |0⟩3 with error mitigation
(purple) and without (green). The exact option price for each initial spot price S0 is shown in blue.

A
Circuit implementation of weighted
sum operator

A.1
Weighted sum of single qubits

In this appendix, we demonstrate an implementation
of the weighted sum operator on a quantum circuit.
The weighted sum operator S computes the arith-
metic sum of the values of n qubits |a⟩n = |a1 . . . an⟩
weighted by n classically deﬁned non-negative integer
weights ω = (ω1, ω2, . . . , ωn), and stores the result
into another m-qubit register |s⟩m = |s1 · · · sm⟩ini-
tialized to |0⟩m. In other words,

n
X

+

S |a⟩n |0⟩m = |a⟩n

i=1
ωiai

m
,
(39)

where

n
X

$

!%

m =

i=0
ωi

+ 1.
(40)

log2

The choice of m ensures that the sum register |s⟩m
is large enough to hold the largest possible weighted
sum, i.e. the sum of all weights. Alternatively, we
can write the weights in the form of a binary ma-
trix Ω= (Ωi,j) ∈{0, 1}n×n∗
, where the i-th row
in Ωis the binary representation of weight ωi and
n∗= maxd
i=1 ni. We use the convention that less sig-
niﬁcant digits have smaller indices, so |s1⟩and Ωi,1
are the least signiﬁcant digits of the respective binary
numbers. Using this binary matrix representation, S
is to add the i-th qubit |ai⟩of the state register to
the j-th qubit |sj⟩of the sum register if and only if
Ωi,j = 1. Depending on the values of the weights, an
additional quantum register may be necessary to tem-
porarily store the carries during addition operations.
We use |cj⟩to denote the ancilla qubit used to store
the carry from adding a digit to |sj⟩. These ancilla
qubits are initialized to |0⟩and will be reset to their
initial states at the end of the computation.

Based on the above setup, we build quantum cir-
cuits for the weighted sum operator using three el-
ementary gates: X (NOT), CNOT, and the Toﬀoli
gate (CCNOT). These three gates suﬃce to build any
Boolean function [38]. Starting from the ﬁrst column
in Ω, for each column j, we ﬁnd all elements with
Ωi,j = 1 and add the corresponding state qubit |ai⟩
to |sj⟩. The addition of two qubits involves three op-
erations detailed in Fig. 17: (a) computation of the
carry using a Toﬀoli gate (M), (b) computation of the
current digit using a CNOT (D), (c) reset of the carry
computation using two X gates and one Toﬀoli gate
( f
M). When adding |ai⟩to the j-th qubit of the sum
register, the computation starts by applying M and
then D to |ai⟩, |sj⟩and |cj⟩, which adds |ai⟩to |sj⟩
and stores the carry into |cj⟩. Then, using the same
two operations, it adds the carry |cj⟩to the next sum
qubit |sj+1⟩with carry recorded in |cj+1⟩. The pro-
cess is iterated until all carries are handled. Finally,
it resets the carry qubits by applying f
M in reverse
order of the carry computation. We reset the carry
qubits in order to reuse them in later computations if
necessary.
In general, we need max(k −2, 0) carry qubits to
compute the addition of |ai⟩on |sj⟩, where k ≥1 is
the smallest integer satisfying

k⟨1|ρs
j,j+k−1 |1⟩k = 0,
(41)

where ρs
j,j+k−1 is the density matrix corresponding to
|sj · · · sj+k−1⟩. In the k = 1 case, i.e. |sj⟩= 0, the
computation is reduced to “copying” |ai⟩to |sj⟩using
the bit addition operator D, and no carries would be
produced. For k ≥2, Eq. (41) guarantees no carries
from |sj+k−1⟩and beyond. Therefore we can directly
compute the carry from |sj+k−2⟩into |sj+k−1⟩with-
out worrying about additional carries. This eliminates
the need for an ancilla qubit |cj+k−2⟩, and hence the
number of carry qubits needed is k −2. To further
reduce the number of ancilla qubits, we can use any
sum qubit |sj⟩= |0⟩during the computation. In our

## Page 16

|ai⟩or |cj−1⟩

•
|sj⟩
•
|sj+1⟩or |cj⟩

(a)

|ai⟩or |cj⟩

D
=
•
|sj⟩

(b)

|ai⟩or |cj−1⟩

|sj⟩
=
X
•
X

(c)

|cj⟩
|0⟩

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

case, since we are processing Ωcolumn by column, all
sum qubits more signiﬁcant than |sj+k−1⟩would be
|0⟩. In other words, we have the last m −(j + k −1)
sum qubits usable as carry qubits in the computation
described above.
As the weights are known at the time of building the
circuit, the possible states that |s⟩m can have before
each addition of a state qubit |ai⟩are also computable.
Since we are adding |ai⟩to |s⟩m starting from the least
signiﬁcant bit, k equals the bit length of the maximum
possible sum on |sj . . . sm⟩after adding |ai⟩to |sj⟩. In
other words,


X

+ 1.
(42)

Ωu,v
2j−v

k = log2

u≤i, or
v≤j

Therefore, the number of carry operations and addi-
tional ancilla qubits required for each addition of |ai⟩
can be determined. The term in the ⌊·⌋in Eq. (42) is
upper-bounded by

m
X

nmax

Ωu,v

X

2v
≤

2j−1 < 2nmax ≤2n,
(43)

j=1

u≤i, or
v≤j

where nmax = maxm
j=1
P

i=1 nΩi,j is the maximum
number of 1’s in a column of Ω. It immediately follows
that the number of non-trivial carry operations (i.e.
carry operations that requires f
M) required to add |ai⟩
to |sj . . . sm⟩is upper-bounded by

k −2 < log2 ⌊nmax⌋≤log2 ⌊n⌋,
(44)

and the number of ancilla qubits required for the en-
tire implementation of S is at most the upper bound

for k−2, since we may use some sum qubits as carries.
In other words, the number of ancilla qubits required
for S grows at most logarithmically with the number
of state qubits n.

A.2
Sum of multi-qubit integers

The weighted sum operator S can be used to calculate
the sum of d multi-qubit positive integers on a quan-
tum register. To do that we ﬁrst prepare the input
register in the state

d
X

|a⟩n = |a(1)
1
. . . a(1)
n1 . . . a(d)
1
. . . a(d)
nd ⟩,
n =

i=1
ni,

(45)
where |a(i)
1 . . . a(i)
ni ⟩, i ∈[1, d] is the binary representa-
tion of the i-th integer to sum with ni qubits, least
signiﬁcant ﬁgure ﬁrst. Then we set the weights as

ω = (20, . . . , 2n1−1, . . . , 20, . . . , 2nd−1),
(46)

or equivalently,

Ωn×n∗=
IT
n1×n∗, . . . , IT
nd×n∗
T ,
(47)

where Ini×n∗=
Ini, 0ni×(n∗−ni)

, i ∈[1, d] and Ini is
the ni-dimensional identity matrix. Now if we build
a weighted sum operator based on the weights in
Eq. (46) and apply it on the input state qubits in
Eq. (45), we would have the sum of the d integers in
|s⟩m.
Fig. 18 shows an example circuit computing the
sum of two 3-digit binary numbers represented on a
6-qubit quantum register |a⟩3 |b⟩3, and storing the re-
sult into a 4-qubit register |s⟩4. The circuit is imple-
mented by a weighted sum operator S with weights
ω = (1, 2, 4, 1, 2, 4). The addition of each qubit onto
the sum qubits requires one carry gate (M) followed
by one addition gate (D), except for the ﬁrst bit |a1⟩
which does not have any carries before its addition.
This results in a total of 6 CNOT (D) gates and 5
Toﬀoli (M) gates. The 11 gates are grouped in three
groups, as is shown in Fig. 18 by dashed boxes. Each
group computes the sum of the bits |aj⟩and |bj⟩into
|sj⟩and the carry into |sj+1⟩.
Note that separate
carry qubits are not required, therefore no carry reset
operators f
M are used. In fact, using the above con-
struction for S, no extra carry qubits will be required
for the addition of any two binary numbers. In gen-
eral, S requires at most ⌊log2 d⌋ancilla qubits for car-
rying operations, which directly comes from Eq. (44).

A.3
Weighted sum of multi-qubit integers

In addition to summing up d integers equally, a weight
wi may also be added to each integer a(i). In that
case, the weight matrix would be

Ω=
w1 · IT
n1×n∗, . . . , wd · IT
nd×n∗
T .
(48)

## Page 17

|a1 + b1⟩→|s1s2⟩
|a2 + b2⟩→|s2s3⟩





|a⟩3




|b⟩3






|s⟩4













|a + b⟩4







Figure 18: A circuit computing the sum of binary numbers |a⟩3 and |b⟩3 into |s⟩4 implemented using the weighted sum operator
with weights ω = (1, 2, 4, 1, 2, 4).

In the case where wi are not integers, we can rescale
the values represented on the quantum register by a
common factor to make all weights integers. For ex-
ample, if we are adding two numbers with weights 0.2
and 0.8, we could use integer weights of w1 = 1 and
w2 = 4 instead, and reinterpret the resulting sum in
postprocessing by dividing it by 5.

B
Optimized Circuit for QA |0⟩3

In the following, we describe the circuit used for
QA |0⟩3 requiring only 18 CNOT gates.
We have
that Q = −AS0A†Sψ0, where S0 = 1 −2 |0⟩⟨0| and
Sψ0 = 1−2 |ψ0⟩|0⟩⟨ψ0| ⟨0| perform reﬂections on |0⟩3
and |ψ0⟩2 |0⟩, respectively. Sψ0 can be implemented
up to a global phase using a single-qubit Z-gate on
the last qubit, which is suﬃcient to diﬀerentiate be-
tween |ψ0⟩|0⟩and |ψ1⟩|1⟩. S0 is a bit more diﬃcult
and we use circuit synthesis for diagonal unitary ma-
trices to achieve an eﬃcient decomposition into gates
[55]. This construction lead to 16 CNOT gates for Q
and 21 for QA, which was still a bit too much to run
on real hardware.
To further reduce the CNOT count, we look at the
full circuit QA |0⟩3 and we applied the following opti-
mization steps. The last part in Q is the application
of A. As mentioned in Sec. 5, we can drop the very
last CNOT gate and apply it in a classical postpro-
cessing.
Furthermore, in QA |0⟩3, we have Sψ0 be-
tween A and A†, i.e. A†Sψ0A, where the uniformly
controlled Y -rotations in A (A†) are right before (af-
ter) Sψ0.
On the other hand, the Z-gate that im-
plements Sψ0 can be decomposed into an X-rotation
and a Y -rotation. The Y -rotation can subsequently
be absorbed into one of the uniformly controlled Y -
rotations in A or A†, changing the angles accordingly.
Since the remaining X-rotation commutes with the
two neighboring CNOT gates from A and A†, we can
move the X-rotation so that the two CNOT gates can-

cel each other. This reduces the CNOT gate count for
QA |0⟩3 to 18 and the resulting circuit is reported in
Fig. 19.

References

[1] John C. Hull, Options, futures, and other deriva-
tives, 6th ed. (Pearson Prentice Hall, Upper Sad-
dle River, NJ [u.a.], 2006).
[2] Fischer Black and Myron Scholes, “The pricing
of options and corporate liabilities,” Journal of
Political Economy 81, 637–654 (1973).
[3] Bruno Dupire, “Pricing with a smile,” Risk Mag-
azine , 18–20 (1994).
[4] Phelim P. Boyle, “Options: A Monte Carlo ap-
proach,” Journal of Financial Economics 4, 323–
338 (1977).
[5] Paul Glasserman, Monte Carlo Methods in Fi-
nancial Engineering (Springer-Verlag New York,
2003) p. 596.
[6] Michael A. Nielsen and Isaac L. Chuang, Cam-
bridge University Press (2010) p. 702.
[7] Abhinav Kandala, Antonio Mezzacapo, Kristan
Temme, Maika Takita, Markus Brink, Jerry M.
Chow,
and Jay M. Gambetta, “Hardware-
eﬃcient
variational
quantum
eigensolver
for
small molecules and quantum magnets,” Nature
549, 242 (2017).
[8] Abhinav Kandala,
Kristan Temme,
Antonio
D. Corcoles,
Antonio Mezzacapo,
Jerry M.
Chow, and Jay M. Gambetta, “Error mitigation
extends the computational reach of a noisy quan-
tum processor,” Nature 567, 491–495 (2019).
[9] N. Moll, P. Barkoutsos, L. S. Bishop, J. M. Chow,
A. Cross, D. J. Egger, S. Filipp, A. Fuhrer, J. M.
Gambetta, M. Ganzhorn, A. Kandala, A. Mez-
zacapo, P. Müller, W. Riess, G. Salis, J. Smolin,
I. Tavernelli,
and K. Temme, “Quantum opti-
mization using variational algorithms on near-

## Page 18

Figure 19: The optimized circuit for QA |0⟩3 used for the experiments on real quantum hardware. It requires 18 CNOT gates
and 33 single qubit gates. The initial spot price is assumed to be equal to 2. The dashed boxes indicate which parts are used
for A, A†, Sψ0, and S0. Note that due to the circuit optimization, some boxes are slightly overlapping.

term quantum devices,” Quantum Science and
Technology 3, 030503 (2018).
[10] M. Ganzhorn, D.J. Egger, P. Barkoutsos, P. Ol-
litrault, G. Salis, N. Moll, M. Roth, A. Fuhrer,
P. Mueller, S. Woerner, I. Tavernelli, and S. Fil-
ipp, “Gate-eﬃcient simulation of molecular eigen-
states on a quantum computer,” Phys. Rev. Ap-
plied 11, 044092 (2019).
[11] Aram W. Harrow, Avinatan Hassidim, and Seth
Lloyd, “Quantum algorithm for linear systems of
equations,” Phys. Rev. Lett. 103, 150502 (2009).
[12] Seth Lloyd, Masoud Mohseni,
and Patrick
Rebentrost,
“Quantum
principal
component
analysis,” Nature Physics 10, 631–633 (2014).
[13] Jacob Biamonte, Peter Wittek, Nicola Pan-
cotti, Patrick Rebentrost, Nathan Wiebe,
and
Seth Lloyd, “Quantum machine learning,” Na-
ture 549, 195–202 (2017).
[14] Vojtech Havlicek, Antonio D. Corcoles, Kristan
Temme, Aram W. Harrow, Abhinav Kandala,
Jerry M. Chow, and Jay M. Gambetta, “Super-
vised learning with quantum-enhanced feature
spaces,” Nature 567, 209 – 212 (2019).
[15] Roman
Orus,
Samuel
Mugel,
and
En-
rique Lizaso, “Quantum computing for ﬁnance:
Overview and prospects,” Reviews in Physics 4,
100028 (2019).
[16] Patrick Rebentrost and Seth Lloyd, “Quan-
tum computational ﬁnance:
quantum algo-
rithm
for
portfolio
optimization,”
(2018),
arXiv:1811.03975 .
[17] Stefan Woerner and Daniel J. Egger, “Quantum
risk analysis,” npj Quantum Information 5, 15
(2019).
[18] Patrick
Rebentrost,
Brajesh
Gupt,
and
Thomas R. Bromley, “Quantum computational
ﬁnance: Monte carlo pricing of ﬁnancial deriva-
tives,” Phys. Rev. A 98, 022321 (2018).

[19] Christa Zoufal, Aurélien Lucchi, and Stefan Wo-
erner, “Quantum generative adversarial networks
for learning and loading random distributions,”
npj Quantum Information 5, 1–9 (2019).
[20] Ana Martin, Bruno Candelas, Angel Rodriguez-
Rozas, Jose D. Martin-Guerrero, Xi Chen, Lu-
cas Lamata, Roman Orus, Enrique Solano, and
Mikel Sanz, “Towards pricing ﬁnancial deriva-
tives with an ibm quantum computer,”
(2019),
arXiv:1904.05803 .
[21] Gilles Brassard, Peter Hoyer, Michele Mosca,
and Alain Tapp, “Quantum Amplitude Ampli-
ﬁcation and Estimation,” Contemporary Mathe-
matics 305 (2002), 10.1090/conm/305/05215.
[22] Yohichi
Suzuki,
Shumpei
Uno,
Rudy
Ray-
mond, Tomoki Tanaka, Tamiya Onodera,
and
Naoki Yamamoto, “Amplitude estimation with-
out phase estimation,” Quantum Information
Processing 19, 75 (2020).
[23] Reuven Y. Rubinstein, Simulation and the Monte
Carlo Method, Wiley Series in Probability and
Statistics (Wiley, 1981).
[24] Daniel S Abrams and Colin P Williams, “Fast
quantum
algorithms
for
numerical
integrals
and stochastic processes,”
(1999), arxiv:quant-
ph/9908083 .
[25] Ashley Montanaro, “Quantum speedup of monte
carlo
methods,”
Proceedings
of
the
Royal
Society of London A: Mathematical,
Phys-
ical
and
Engineering
Sciences
471
(2015),
10.1098/rspa.2015.0301.
[26] A. Yu. Kitaev, “Quantum measurements and
the
Abelian
Stabilizer
Problem,”
(1995),
arXiv:quant-ph/9511026 .
[27] R. Cleve,
A. Ekert,
C. Macchiavello,
and
M. Mosca, “Quantum algorithms revisited,” Pro-
ceedings of the Royal Society of London. Series
A: Mathematical, Physical and Engineering Sci-
ences 454, 339–354 (1998).

## Page 19

[28] Paul Glasserman, Philip Heidelberger, and Per-
wez Shahabuddin, “Eﬃcient Monte Carlo Meth-
ods for Value-at-Risk,” in Mastering Risk, Vol. 2
(2000) pp. 5–18.
[29] Robert C. Merton, “Theory of rational option
pricing,” The Bell Journal of Economics and
Management Science 4, 141–183 (1973).
[30] Lov Grover and Terry Rudolph, “Creating super-
positions that correspond to eﬃciently integrable
probability distributions,”
(2002), arXiv:quant-
ph/0208112 .
[31] Adriano Koshiyama, Nick Firoozye, and Philip
Treleaven, “Generative adversarial networks for
ﬁnancial trading strategies ﬁne-tuning and com-
bination,” (2019), arXiv:1901.01751 .
[32] Blanka Horvath, Aitor Muguruza,
and Mehdi
Tomas, “Deep learning volatility,” SSRN Elec-
tronic Journal (2019), 10.2139/ssrn.3322085.
[33] Martin Plesch and Časlav Brukner, “Quantum-
state preparation with universal gate decomposi-
tions,” Phys. Rev. A 83, 032302 (2011).
[34] Ian Goodfellow,
Jean Pouget-Abadie,
Mehdi
Mirza, Bing Xu, David Warde-Farley, Sher-
jil Ozair, Aaron Courville,
and Yoshua Ben-
gio, “Generative adversarial nets,” in Advances
in Neural Information Processing Systems 27,
edited by Z. Ghahramani, M. Welling, C. Cortes,
N. D. Lawrence, and K. Q. Weinberger (Curran
Associates, Inc., 2014) pp. 2672–2680.
[35] Adriano Barenco, Charles H. Bennett, Richard
Cleve, David P. Divincenzo, Norman Margolus,
Peter Shor, Tycho Sleator, John A. Smolin, and
Harald Weinfurter, “Elementary gates for quan-
tum computation,” Phys. Rev. A 52, 3457–3467
(1995).
[36] Steven A Cuccaro, Thomas G Draper, Samuel A
Kutin,
and David Petrie Moulton, “A new
quantum ripple-carry addition circuit,”
(2004),
arxiv:quant-ph/0410184 .
[37] Gadi Aleksandrowicz, Thomas Alexander, Pana-
giotis Barkoutsos,
Luciano Bello,
Yael Ben-
Haim, David Bucher, Francisco Jose Cabrera-
Hernández,
Jorge
Carballo-Franquis,
Adrian
Chen, Chun-Fu Chen, Jerry M. Chow, An-
tonio D. Córcoles-Gonzales, Abigail J. Cross,
Andrew Cross, Juan Cruz-Benito, Chris Cul-
ver,
Salvador De La Puente González,
En-
rique De La Torre, Delton Ding, Eugene Du-
mitrescu, Ivan Duran, Pieter Eendebak, Mark
Everitt,
Ismael Faro Sertage,
Albert Frisch,
Andreas Fuhrer, Jay Gambetta, Borja Godoy
Gago, Juan Gomez-Mosquera, Donny Green-
berg, Ikko Hamamura, Vojtech Havlicek, Joe
Hellmers, Łukasz Herok, Hiroshi Horii, Shao-
han Hu, Takashi Imamichi, Toshinari Itoko,
Ali Javadi-Abhari,
Naoki Kanazawa,
Anton
Karazeev, Kevin Krsulich, Peng Liu, Yang Luh,
Yunho Maeng, Manoel Marques, Francisco Jose

Martín-Fernández, Douglas T. McClure, David
McKay, Srujan Meesala, Antonio Mezzacapo,
Nikolaj Moll,
Diego Moreda Rodríguez,
Gi-
acomo Nannicini, Paul Nation, Pauline Olli-
trault,
Lee James O’Riordan,
Hanhee Paik,
Jesús Pérez, Anna Phan, Marco Pistoia, Vik-
tor Prutyanov, Max Reuter, Julia Rice, Ab-
dón Rodríguez Davila, Raymond Harry Putra
Rudy, Mingi Ryu, Ninad Sathaye, Chris Schn-
abel, Eddie Schoute, Kanav Setia, Yunong Shi,
Adenilton Silva, Yukio Siraichi, Seyon Sivara-
jah, John A. Smolin, Mathias Soeken, Hitomi
Takahashi, Ivano Tavernelli, Charles Taylor, Pete
Taylour, Kenso Trabing, Matthew Treinish, Wes
Turner, Desiree Vogt-Lee, Christophe Vuillot,
Jonathan A. Wildstrom, Jessica Wilson, Er-
ick Winston, Christopher Wood, Stephen Wood,
Stefan Wörner, Ismail Yunus Akhalwaya,
and
Christa Zoufal, “Qiskit: An open-source frame-
work for quantum computing,” (2019).
[38] Vlatko Vedral, Adriano Barenco, and Artur Ek-
ert, “Quantum networks for elementary arith-
metic operations,” Phys. Rev. A 54, 147–153
(1996).
[39] Thomas G Draper, “Addition on a Quantum
Computer,” (2000), arXiv:quant-ph/0008033 .
[40] Thomas G Draper, Samuel A Kutin, Eric M
Rains,
and Krysta M Svore, “A logarithmic-
depth quantum carry-lookahead adder,” Quan-
tum Information and Computation 6, 351–369
(2006), arXiv:quant-ph/0406142 .
[41] Ghasem
Tarmast,
“Multivariate
Log-Normal
Distribution,” International Statistical Institute
Proceedings: 53rd Session, Seoul (2001).
[42] Emmanuel Gobet, “Advanced monte carlo meth-
ods for barrier and related exotic options,”
Handbook of Numerical Analysis, 15, 497 – 528
(2009).
[43] Pavel V. Shevchenko and Pierre Del Moral, “Val-
uation of barrier options using sequential monte
carlo,” Journal of Computational Finance 20,
107–135 (2014).
[44] M. Žnidarič, O. Giraud, and B. Georgeot, “Opti-
mal number of controlled-not gates to generate a
three-qubit state,” Physical Review A 77, 032320
(2008).
[45] Vivek V Shende, Stephen S Bullock, and Igor L
Markov, “Synthesis of quantum-logic circuits,”
IEEE Transactions on Computer-Aided Design
of Integrated Circuits and Systems 25, 1000–
1010 (2006).
[46] Raban Iten, Oliver Reardon-Smith, Luca Mon-
dada, Ethan Redmond, Ravjot Singh Kohli,
and Roger Colbeck, “Introduction to UniversalQ-
Compiler,” (2019), arXiv:1904.01072 .
[47] A. Dewes, F. R. Ong, V. Schmitt, R. Lauro,
N. Boulant, P. Bertet, D. Vion, and D. Esteve,
“Characterization of a two-transmon processor

## Page 20

with individual single-shot qubit readout,” Phys.
Rev. Lett. 108, 057002 (2012).
[48] Kristan Temme, Sergey Bravyi,
and Jay M.
Gambetta, “Error mitigation for short-depth
quantum circuits,” Phys. Rev. Lett. 119, 180509
(2017).
[49] E. F. Dumitrescu, A. J. McCaskey, G. Hagen,
G. R. Jansen, T. D. Morris, T. Papenbrock, R. C.
Pooser, D. J. Dean,
and P. Lougovski, “Cloud
quantum computing of an atomic nucleus,” Phys.
Rev. Lett. 120, 210501 (2018).
[50] Mark
Broadie
and
Paul
Glasserman,
“Es-
timating
security
price
derivatives
using
simulation,”
Management Science 42 (1996),
10.1287/mnsc.42.2.269.
[51] Austin G. Fowler, Matteo Mariantoni, John M.
Martinis,
and Andrew N. Cleland, “Surface
codes:
Towards practical large-scale quantum
computation,” Phys. Rev. A 86, 032324 (2012).
[52] Miroslav Dobšíček, Göran Johansson, Vitaly
Shumeiko,
and Göran Wendin, “Arbitrary ac-
curacy iterative quantum phase estimation algo-
rithm using a single ancillary qubit: A two-qubit
benchmark,” Phys. Rev. A 76, 030306 (2007).
[53] C. J. O’Loan, “Iterative phase estimation,” Jour-
nal of Physics A: Mathematical and Theoretical
43 (2010), 10.1088/1751-8113/43/1/015301.
[54] Krysta M Svore, Matthew B Hastings,
and
Michael Freedman, “Faster phase estimation,”
Quantum Information & Computation 14, 306–
328 (2014), arXiv:1304.0741 .
[55] S.S. Bullock and I.L. Markov, “Smaller circuits
for arbitrary n-qubit diagonal computations,”
Quantum Information & Computation 4, 027–
047 (2004), arXiv:quant-ph/0303039 .
