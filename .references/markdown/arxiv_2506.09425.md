---
source_pdf: ../arxiv_2506.09425.pdf
pages: 13
extracted_at: 2026-04-17T12:32:44+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Local surrogates for quantum machine learning"
author: "Sreeraj Rajindran Nair; Christopher Ferrie"
---

# arxiv_2506.09425

Original title: Local surrogates for quantum machine learning

Author metadata: Sreeraj Rajindran Nair; Christopher Ferrie

Source PDF: ../arxiv_2506.09425.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Local surrogates for quantum machine learning

Sreeraj Rajindran Nair
1 and Christopher Ferrie
1

1Centre for Quantum Software and Information, University of Technology Sydney, Australia

Surrogates have been proposed as classical simulations of the pretrained quantum learning models,
which are capable of mimicking the input-output relation inherent in the quantum model. Quantum
hardware within this framework is used for training and for generating the classical surrogates.
Inference is relegated to the classical surrogate, hence alleviating the extra quantum computational
cost once training is done.
Taking inspiration from interpretable models, we introduce a local
surrogation protocol based on reuploading-type quantum learning models, including local quantum
surrogates as cost-efficient intermediate quantum learning models. When the training and inference
are only concerned with a subregion of the data space, deploying a local quantum surrogate offers
qubit cost reductions and the downstream local classical surrogate achieves dequantization of the
inference phase. Several numerical experiments are presented.

arXiv:2506.09425v1 [quant-ph] 11 Jun 2025

I.
INTRODUCTION

A widely employed class of quantum learning models
uses a parameterized quantum circuit to encode input
data and generate predictions. These models are often
referred to as quantum neural networks [1–4], as the pa-
rameters of the circuit loosely resemble the weights in
traditional neural networks.
Reuploading quantum models [5, 6] fall under this
quantum neural networks class, structured with alter-
nating layers of data-encoding gates and trainable uni-
tary gates. The input data is reuploaded multiple times
throughout the circuit. It has been shown that these reu-
ploading models can be exactly represented as truncated
Fourier series [7]. Utilizing this unique property of such
models, Schreiber et al [8] proved that re-uploading mod-
els always warranted Fourier-based classical surrogates.
With this, the inference phase of such quantum learning
models was de-quantized [9, 10], as the quantum hard-
ware is only required for the training phase and for the
subsequent creation of the classical surrogate.
Jerbi et al [11] further expanded upon this concept
beyond just the reuploading models to propose a gen-
eral framework for ’shadow models’ and conditions for
’shadowfiable’ quantum learning models. Shadows and
surrogates are interchangeable terms within our context
[12]. In addition to classical simulations [10, 13, 14], sur-
rogates taking inspiration from classical machine learn-
ing [15] have been used for optimization purposes as well
[16]. Moreover, quantum surrogates for quantum mod-
els are also an active area of research [17]. Throughout
the rest of this paper, quantum models/surrogates re-
fer to learning models that require quantum hardware in
the inference phase, and classical models/surrogates refer
to models where classical hardware would suffice for the
same.
The aforementioned works were concerned primarily
with the surrogation of the whole data space of the
trained quantum model. Taking a cue from classical ma-
chine learning interpretability techniques [18], we refer
to such surrogation protocols as global surrogation in
this paper.

FIG. 1: Local surrogation. For a small enough local
region within the data space of a quantum learning
model, a cost-efficient local quantum/classical surrogate
can be generated with adequate accuracy, potentially as
a two-step protocol.

Our work focuses on surrogation when performed on
smaller regions within the fully trained arbitrary quan-
tum model data space, dubbed local surrogation. We
consider both local quantum surrogates and local clas-
sical surrogates. We numerically demonstrate that any
arbitrary quantum model can be locally quantum surro-
gated with a reuploading-type model up to a certain error
threshold within a local region of the data space. Once
such a quantum Fourier local surrogate is generated, it
is always possible to construct a local classical surro-
gate using the classical surrogation protocol proposed by
Schreiber et al [8]. Within our framework, the sizes of
local regions for the local quantum surrogate and the
local classical surrogate are mutually independent. Al-
though one can apply a modified version of the classical-
surrogation protocol directly on the arbitrary quantum
learning model, the global spectrum typically grows com-
binatorially with circuit depth and data dimension, and
no tight cost guarantees currently exist.
Local
surrogates
are
used
extensively
in
classi-

## Page 2

cal
machine
learning
within
the
context
of
inter-
pretable/explainable AI (XAI) [19].
For instance, Lo-
cal Interpretable Model-agnostic Explanations (LIME)
[20] is an approach to explain the individual predictions
of a black-box machine learning model. Recently, this
framework was extended to quantum machine learning as
quantum local interpretable model-agnostic explanations
(QLIME) [21]. Likewise, localization in the data space
is a staple of digital signal processing (DSP) [22, 23]. In
DSP, this usually refers to the use of windowing tech-
niques [24] when processing large or real-time signals, as
seen in short-time Fourier transform (STFT) processing
[25–28]. Windowing broadly refers to the operation of
chopping up signals/data into smaller chunks and pro-
cessing these with standard window functions [29]. Tak-
ing a cue from DSP, we refer to the local regions in the
data space as windows and the size of these local regions
as window sizes later in our simulations. The terminol-
ogy is appropriate, given that both formalisms share a
common Fourier representation.
A recent paper [30] introduced a hybrid quantum-
classical simulation framework designed to approximate
expectation landscapes generated by quantum circuits.
They focus on small subregions or “patches” of these
landscapes, defined over a subregion, using a classical
surrogate. The work purports that it is indeed possible to
efficiently simulate the quantum system classically with
polynomial complexity and to efficiently distribute com-
putational labour between quantum and classical hard-
ware by essentially minimizing the use of quantum hard-
ware to the absolute bare minimum.
The conceptual-
ization of these “patches” is similar to the local region
or windows from our framework. However, in contrast
to our work, they do not delve into the windowing tech-
niques [24] from digital signal processing [22, 23] nor are
they concerned with localization in the data space as we
are.
The structure of the paper follows. We begin by dis-
cussing reuploading quantum models and their Fourier
representation.
We reiterate its generalization to the
multidimensional case and follow it up with its expres-
sivity. Then we review the classical surrogation protocol
proposed by Schreiber et al, along with their definitions
for classical surrogates. With these background materi-
als covered, we introduce our local surrogation protocol
and its potential advantages. We discuss the details and
results of our simulations to validate our claims before
giving a final conclusion at the end.

II.
REUPLOADING QUANTUM MODELS

A reuploading quantum model consists of alternating
layers of data encoding gates S(x) and trainable unitaries
W(θ) [5, 6]. The model’s output at a specific input x is
given by the expectation value of an observable M with
respect to the quantum state prepared by the circuit:

fθ(x) = ⟨0|U †(x, θ)MU(x, θ)|0⟩,
(1)

where the circuit U(x, θ) has the structure:

U(x, θ) = W (L+1)(θ)S(x)W (L)(θ) · · · S(x)W (1)(θ). (2)

Here, L is the number of reuploading layers, S(x) =
e−ixH encodes the input x into the quantum state using
a Hamiltonian H, and W (k)(θ) are the trainable unitaries
parametrized by θ.

A.
Fourier Representation

Earlier work has proven that the natural representa-
tion of fθ(x) is as a truncated Fourier series [7, 31, 32].
The data encoding gates S(x) introduce a frequency spec-
trum Ωdetermined by the eigenvalues of the Hamiltonian
H. The overall model can be expressed as:

fθ(x) =
X

ω∈Ω
cω(θ)eiωx,
(3)

where cω(θ) are the Fourier coefficients, determined by
the trainable gates W(θ) and the measurement observ-
able M.

B.
Truncated Fourier Series

The frequency spectrum Ωaccessible to the model de-
pends on the eigenvalues λi of H. Specifically, the spec-
trum is given by:

Ω= {λi −λj | i, j ∈[d]},
(4)

where d is the dimension of the Hilbert space.
The
Fourier series is truncated in the sense that only frequen-
cies in Ωcontribute to the model’s output. The coeffi-
cients cω(θ) determine how these frequencies combine to
form the final function fθ(x) [33].

III.
MULTIDIMENSIONAL FOURIER SERIES

A multidimensional Fourier series generalizes the con-
cept of a one-dimensional Fourier series to higher
dimensions.
For
an
M-dimensional
input
x
=
(x1, x2, . . . , xM) ∈RM, the series is represented as

f(x) =
X

ω∈Ω
cωeiω·x,
(5)

where ω = (ω1, ω2, . . . , ωM) are the frequency compo-
nents and cω are the Fourier coefficients. The frequency
spectrum Ωcontains all possible combinations of the fre-
quency components up to a given degree D, ensuring that
the series captures the desired expressivity.
The number of independent Fourier coefficients is given
by

Nc = (2D + 1)M −1

2
+ 1,
(6)

## Page 3

which scales exponentially with the dimension M. This
highlights the computational challenges associated with
high-dimensional Fourier representations.
To implement multidimensional Fourier series using
quantum circuits, earlier works [34] considered different
ansatzes that encode data into quantum states and apply
parameterized gates for processing. Each ansatz balances
expressivity and scalability differently. For our simula-
tions, we used the so called “line ansatz”. The line ansatz
encodes all data dimensions into a single qubit sequen-
tially. The encoding gate S(xm) acts on the m-th data
feature, followed by a processing gate A(θ) that applies
trainable parameters. The output is a Fourier series in
which all dimensions are mixed, achieving expressivity at
the cost of reduced scalability.
Note that the particular ansatz chosen to arrive at
the Fourier representation is not a relevant parameter
in this work, though in practice it may be an important
application-dependent factor.

IV.
EXPRESSIVITY OF REUPLOADING
MODELS

The expressivity of a quantum model is governed by
two factors:

• Frequency Spectrum: The set of accessible fre-
quencies Ωdetermines the model’s ability to rep-
resent functions with varying oscillatory behavior.
Increasing the number of layers L or using a richer
encoding Hamiltonian H expands Ω.

• Fourier Coefficients: The trainable gates W(θ)
control the coefficients cω(θ), which determine how
the accessible frequencies combine to approximate
the target function.

For a single-layer model (L = 1) with a Pauli-X
encoding (H = σx/2), the spectrum consists of fre-
quencies {−1, 0, 1}.
By repeating the encoding layer
multiple times (L > 1), the spectrum is extended to
{−L, −L + 1, . . . , L}, allowing the model to represent
higher-degree Fourier series.
The expressivity of quantum circuits for multidimen-
sional Fourier series depends on the encoding strategy,
the number of layers L, and the structure of the pro-
cessing gates. The degrees of freedom increase with L,
enabling the representation of higher-order frequencies.
However, practical considerations such as gate fidelity
and noise impose constraints on the achievable expres-
sivity.
The scaling of the Fourier series coefficients is also in-
fluenced by the eigenvalues of the encoding Hamiltonian
H. By optimizing the eigenvalue spectrum, we can en-
hance the coverage of the frequency spectrum and tailor
the model to specific applications.
Reuploading quantum models can approximate any
square-integrable function f(x) on a compact domain by

increasing the number of layers L and using sufficiently
flexible trainable gates W(θ) [7, 31]. The universal ap-
proximation theorem for quantum models follows from
the fact that Fourier series with arbitrarily many fre-
quencies can approximate any L2-function to arbitrary
accuracy [33].

V.
CLASSICAL SURROGATION PROTOCOL

Quantum machine learning (QML) explores the use
of quantum circuits to approximate complex functions.
Despite the potential advantages of quantum learning
models, their deployment is limited by the constraints of
NISQ devices [35]. Although even with adequate fault-
tolerant quantum infrastructure, it is unlikely that it
would be possible or even recommended to deploy quan-
tum models for all and every learning task due to the
associated high computational cost. The notion of clas-
sical surrogates provides a practical means to overcome
this limitation by enabling efficient evaluation and infer-
ence of quantum models in classical settings [8, 11].
In this section, we discuss how reuploading-type quan-
tum models admit classical surrogation through their
representation as truncated Fourier series [8, 32]. We also
outline the classical surrogation protocol and its theoret-
ical guarantees. We will now reiterate the definition for
a classical surrogate as provided by Schreiber et al. for
completion.

Definition 1 (Classical Surrogate [8]) A hypothesis
class of quantum learning models F has classical sur-
rogates if there exists a process S that upon input of a
learning model f ∈F produces a classical model g ∈G
such that the maximal deviation of the surrogate from the
quantum learning model is bounded with high probability.
Formally, we require:

P

sup
x∈X
∥f(x) −g(x)∥≤ϵ

≥1 −δ,

for a suitable norm on the output space Y. The surroga-
tion process S must be efficient in the size of the quantum
learning model, the error bound ϵ, and the failure proba-
bility δ.

Given the Fourier representation of a quantum model,
a classical surrogate can be constructed by estimating
the Fourier coefficients {cω}. The protocol proceeds as
follows:

1. Frequency Spectrum Identification:
Deter-
mine the accessible frequency spectrum Ωbased on
the structure of the encoding Hamiltonian H and
the number of data encoding layers L.

2. Sampling and Coefficient Estimation: Eval-
uate the quantum model fθ(x) at discrete points
{xj}T
j=1 wherein T = (2L + 1)d (L = number of

## Page 4

reuploading layers, d = number of data features)
and solve the least-squares problem:

2

T
X

ω∈Ω
cωeiωxj −fθ(xj)

X

ˆcω = arg min
cω

.
(7)

j=1

3. Classical Surrogate Construction: Construct
the classical surrogate g(x) as:

g(x) =
X

ω∈Ω
ˆcωeiωx.
(8)

This approach ensures that the classical surrogate g(x)
reproduces the output of the quantum model fθ(x) with
high fidelity. The classical surrogate gc, generated with
the surrogation protocol, satisfies the surrogation condi-
tions of Definition 1 with the following number of invo-
cations of the quantum learning model:

Ntotal = TN = 2T∥M∥2
∞
ϵ2


log 1

δ + T log 2

,
(9)

where ∥M∥is the bound on the norm of the measurement
operator applied to the quantum state. It characterizes
the measurement’s sensitivity.
It is evident that with a larger number of data features
d, the classical surrogation protocol will become compu-
tationally intractable due to the exponential scaling on
d.

VI.
LOCAL SURROGATION PROTOCOL

The surrogation protocol described by Schreiber et al
generates a global surrogate for the reuploading-type
quantum learning model. This broadly means that the
surrogate tries to replicate the predictions of the quan-
tum model for all of the input data space.
However,
there are cases where the intent behind the creation of
a surrogate might not require such full-scale prediction
replication. In cases where the intention is to generate a
surrogate only for a local region within the data space of
an arbitrary quantum learning model, we can deploy the
local surrogation protocol. We numerically show that for
most applications, this is a sufficient model and results
in a generous reduction in qubit resources.
In this manner, our work aligns with the [30] wherein
classical surrogates were created for smaller regions of
the parameter space. Whereas, our work concerns local
surrogates in the data space and extends the surrogation
from local classical surrogates to local quantum surro-
gates as well, which we introduce in this paper.
Given a fully trained arbitrary quantum learning
model, we can create a local Fourier bases quantum sur-
rogate with the reuploading architecture, which would
replicate the predictions of the quantum learning model
within the local region the quantum model was trained

on. We train the reuploading-type local quantum surro-
gate on the inputs and outputs of the arbitrary quantum
model within the local region. Because it is confined to a
restricted input region, the local quantum surrogate can
be trained with markedly fewer quantum-circuit evalu-
ations and a lower-dimension least-squares fit than its
global counterpart.
In addition to being more compact and resource-
efficient, a local quantum surrogate can directly seed the
Fourier classical-surrogation protocol, which guarantees
the construction of a corresponding local classical surro-
gate. Local quantum surrogates can act as a cost-efficient
intermediate model for classical surrogate creation.
While it is possible to perform a modified version of
the classical surrogation protocol directly on the said ar-
bitrary quantum model, the number of required query
points and the size of the resulting linear system scale
with the overall input space and circuit depth.
With-
out any proven upper bound, runtime and memory re-
quirements can quickly become prohibitive, and the fit
may suffer from poor numerical conditioning for higher-
dimensional data.

VII.
SIMULATIONS

We ran several numerical simulations to validate our
local surrogation protocol. In the following simulation
cases, we first train our local quantum and classical sur-
rogates on sampled target functions; that is, data will re-
fer to the output of a previously trained quantum model.
Later on, we ran the same simulations on a quantum sup-
port vector machine model. As before, here the window
size refers to the size of the local region. We also tried to
restrict ourselves to the least capable surrogate models,
or rather low qubit count shallow circuits in each case
to showcase that local surrogation can aid in leveraging
and extracting better performance from hitherto lacklus-
ter model configurations.

A.
Local quantum surrogation on 1D target
function

To test the effect of window size against learning met-
rics in the case of 1D local quantum surrogation, we ran
simulations with a 1D target function directly. For such
a target function, we train local surrogates for various
window sizes. We tested the 1D target function fitting
for improvement in R2 learning metrics for the local re-
gion in the case of 1, 2, and 3 qubit single-layer quantum
reuploading models using a modified version of the model
described in [7]. These models were trained with a max-
imum of 60 steps of an Adam optimizer with a learning
rate of 0.3 and a batch size of 25. The target function was
sampled at the rate of 10 samples per unit within the x
values (−6, 6) for creating a net total of 120 data points.
The window begins as a 0.5-unit slice (5 data points) of

## Page 5

FIG. 2: Testing 1D signal fitting in terms of
improvement in R2 learning metric in the case of 1, 2,
and 3 qubit single-layer quantum reuploading models.
The 1D signal under consideration is a truncated
Fourier series of degree 3, i.e., g(x) = P5
n=−5 cne2inx

with cn = 0.15 + 0.15i for n = 1, 2, 3 and c0 = 0.1. For
the sampling rate of 10 within x values (-6, 6), the
window begins as a 0.5-unit slice (i.e., 5 data points) of
the data space, grows by 0.2 units every iteration, and
maxes out before 120 data points.

the data space, grows by 0.2 units every iteration, and
maxes out at 120 data points. We see a clear trend of
reduction in R2 for the local region as the window size
increases Figure 2. The details of the target function are
also provided in the Figure 2.

B.
Local surrogation on 2D target functions

In Figure 3a, we see a demonstration of local quan-
tum surrogation for a fixed patch in the data space of
a given target function.
We use a modified version of
the model described by [34] wherein a 2-dimensional line
ansatz of 1 qubit with 2 layers of reuploading is used
for the simulation.
As in the original, we too use the
Nelson-Mead method for the classical optimization with
500 training and 1500 testing data points for the local re-
gion. Thus, train samples per axis =
j√

500
k
= 22 and
total grid points = 22 × 22 = 484. 484 values constitute
the full target function on a square domain x, y ∈[−π, π]
in the 22 × 22 training grid.
The window for the quantum surrogate shown in Fig-
ure 3a is a 10 × 10 grid, i.e., 100 data points. The imme-
diate observation is that we are able to extract superior
performance from these seemingly worse-performing line
ansatz models when trained on an appropriately sized
local region.
After creating a local quantum surrogate, we use this
surrogate to generate a classical surrogate by implemen-
tation of a version of the classical surrogation protocol
(wherein the local quantum surrogate is treated as a
black-box model) with a patch of 8 × 8 grid size as seen
in Figure 3b. In both surrogation protocols, we observed
high R2 values for the local region. The window/patch
size for each of the local surrogations here are indepen-

dent of each other.
In a similar manner, we trained 1-qubit local quan-
tum surrogates and generated local classical surrogates
in the case of various 2D target functions for various
window sizes. To stress–test the surrogation pipeline we
constructed a suite F = f (m)13
m=1 of real-valued, twice-
differentiable functions f (m) : [−π, π]2 →R (Figure 4d,
Table I). All functions are analytically known, ensuring
noise-free ground truth. For 2D signal fitting, we used
the same modified line ansatz form of the multidimen-
sional Fourier model and trained on these 13 different 2D
target functions. This time, we looped over different win-
dow/patch sizes. The square patch is always anchored at
grid index (2, 2) (counting from 0) of the 22×22 training
grid, starting as a 2×2 grid and increments in size by one
grid index in each window cycle until reaching the size of
20×20. Four of these target functions showed significant
negative R2
Q→T (local quantum surrogate versus target
function) for the local region values and did not converge
satisfactorily. We suspect this could be attributed to the
limitations of the Fourier-based surrogates. For the rest,
we see a clear large R2
Q→T for the local region in the
case of small window sizes and a steady drop in learn-
ing accuracy as the window sizes increase Figure 4a, as
expected.
Two Fourier-based classical approximations are imple-
mented: one for the local quantum surrogate and an-
other for the direct classical surrogation on the target
functions.

1.
Local classical surrogate for the local quantum surrogate

We used the classical surrogation protocol on the local
quantum surrogate of depth L generated before and as-
sumed that we always know the number of reuploading
layers of the reuploading-based local quantum surrogate.
The admissible spectrum is the square

ΩL =

(k1, k2) ∈Z2 : |k1|, |k2| ≤L
,
|ΩL| = (2L+1)2.

For every window of edge length w (a w × w sub-array
of the 22 × 22 training grid, anchored at index (2,2)) we
rescale the canonical (2L+1)×(2L+1) Cartesian lattice
so that all (2L + 1)2 nodes lie inside the patch. Let’s
denote those nodes as X1, . . . , X(2L+1)2.
We build the design matrix

Φij = e i kj·Xi,
kj ∈ΩL,

Query the trained quantum surrogate once at each node
to obtain yq = [f q
Θ(X1), . . . , f q
Θ(X(2L+1)2)]⊤, and solve
the square system Φ α = yq. Exactly (2L+1)2 quantum
circuit calls are made.
The resulting local classical surrogate is

gα(x) = ℜ
X

k∈ΩL
αk e i k·x.

## Page 6

(a) Local quantum surrogation of the target patch sampled from the target function
0.05x2 −0.1y + 0.6cos(1.2x + 0.5y) −0.4sin(0.8x −1.3y) + 0.35cos(2x) + 0.2sin(2y). A modified 2D line ansatz with 1 qubit
and 2 layers was used for the simulation.

(b) Local classical surrogation of the quantum (QNN) patch sampled from the
trained local quantum surrogate, wherein the latter is treated as a black-box model.

FIG. 3: Demonstration of local quantum and local classical surrogation. The 22 × 22 training grid for the full target
function on a square domain x, y ∈[−π, π] had a patch of fixed 10 × 10 and 8 × 8 grid size for the local quantum
surrogate and the local classical surrogate, respectively.

2.
local classical surrogate for the direct surrogation on the
target functions

The direct surrogate operates on the true target values
ytar and we assume that the arbitrary quantum model
(predefined target functions in this case) is a blackbox
for all our intents and purposes. We choose a separable
spectrum ˜Ωkmax = {0} ∪{±k}kmax
k=1 with kmax = ⌈w/2⌉.
The real–valued basis functions on x = (x1, x2) are

Ψ(x) =

1, cos(kx1), sin(kx1)kmax
k=1 , cos(kx2), sin(kx2)kmax
k=1

,

giving 1 + 4 kmax columns in the matrix Ψij = Ψj(Xi).
The least-squares solution

β = (Ψ⊤Ψ)−1 Ψ⊤ytar

minimises the patch MSE, and the separable surrogate is

gsep
β (x) = Ψ(x) β.

For both these local classical surrogations, we compute
the coefficient of determination for each window size. For

most cases R2
C→T (local classical surrogate versus target
function) for the local region of most target functions, we
observe an inverse relation between the window size and
R2
C→T i.e R2 decreases as window size increases, as seen
in Figure 4c. And for R2
C→Q (local classical surrogate
versus local quantum surrogate) for the local region, we
observe consistently high (mostly 1 due to the machine
precision of the simulations) R2
C→Q values regardless of
the window size due to the classical surrogation guaran-
tees associated with the local quantum surrogate based
on reuploading in our framework, as seen in Figure 4b.

C.
Demonstration on a QSVM model

We now demonstrate our local surrogation protocol
with a quantum support vector machine (QSVM) as our
arbitrary quantum model. We used PennyLane [36] to
write code for the QSVM and the reuploading-based lo-
cal quantum surrogate. We adopt the classical Iris data
set [37], Diris = {(xi, yi)}150
i=1, where xi ∈R4 encodes
sepal and petal statistics and yi ∈{0, 1, 2} denotes the

## Page 7

(a) Local quantum surrogate fit to target function (window
size vs R2)

(c) Local classical surrogate fit to target function with the
latter treated as a black-box model (window size vs R2)

(b) Local classical surrogate fit to the local quantum
surrogate, wherein the number of reuploading layers is fed
to the local classical surrogate. (window size vs R2)

(d) 2-D target functions used in the experiment (definitions
provided in Table I).

FIG. 4: Testing the performance of local quantum/classical surrogates in the case of various 2D target functions.
Tests had a 22 × 22 training grid for the full target function on a square domain x, y ∈[−π, π]. The simulation
looped over different window/patch sizes. The square patch is always anchored at grid index (2, 2) of the 22 × 22
training grid, starting as a 2 × 2 grid and increments in size by 1 grid index in each window cycle until reaching the
final size of 20 × 20.

species label. Only the first two classes (setosa and versi-
color) and the first two features (sepal length/width) are
retained, yielding

D =

(xi, yi) ∈R2 × {0, 1}
100
i=1.

All inputs are standardised by ˜xi = diag(σ)−1(xi −µ),
where µ and σ are the empirical mean and standard
deviation, respectively. The scaled data occupy the range
˜xi ∈[−2.6, 2.6]2.
A
binary
QSVM
is
trained
on
D
using
a
data–dependent quantum kernel

Kθ(x, x′) =
⟨0⊗2|Uθ(x′)†Uθ(x)|0⊗2⟩
2,

with Uθ
= Uent

RY (x)

implemented on two qubits
(Pennylane’s default.qubit backend).
Here RY (x)
embeds the input angles and Uent is a single layer of
nearest–neighbour CNOTs.
The full 100 × 100 kernel
matrix is computed explicitly and supplied to SVC in
scikit–learn with default hyperparameters. QSVM at-
tains a training accuracy R2 of ≈85.0%. This served as
the arbitrary quantum model for our local surrogation
protocol, as seen in the first plot of Figure 5a.
Local surrogation is performed on a circular patch

P(r) =
˜xi ∈D : ∥˜xi∥2 < r
,
r > 0.

Throughout we fix the radius at r = 1.0 centered at (0,0),
which selects |P(1.0)| = 30 points. The QSVM posterior
pQ(x) = Pr [y = 1 | x] is linearly rescaled to [−1, 1],

zQ(x) = 2 pQ(x) −1,

and used as a regression target on the patch.
We implemented a 1-qubit local quantum surrogate as
per our protocol with PennyLane. A single-qubit feature
reupload circuit of depth L = 2 is used:

2
Y

ℓ=1
Uvar
θℓ


UΘ(x) =

Uenc(x),

|
{z
}
StronglyEntangling layer

with
Uenc(x)
=
Uent

RY (x1), RY (x2)

Uent
and
Strongly Entangling layer template from PennyLane is
used to design the trainable block. The model output is
the Pauli-Z expectation fΘ(x) = ⟨0|U †
Θ(x)Z UΘ(x)|0⟩.
The trainable tensor Θ ∈R2×6 (6 Euler angles per
upload, 12 angles total) is initialised θij ∼N(0, 10−4)
and trained on the patch MSE

Lq =
1
|P|


fΘ(x) −zQ(x)
2,

X

x∈P

using 100 steps of Nesterov momentum (η = 0.5). For
evaluation, a 100 × 100 Cartesian mesh covering the

## Page 8

(a) Local and global performances of local quantum surrogate trained on sampled data from the QSVM and local classical
surrogate trained on sampled data from local quantum surrogate.

(b) Relative errors of local quantum surrogate against QSVM and local classical
surrogate against local quantum surrogate.

FIG. 5: Local surrogation protocol on a QSVM trained on a 2-class, 2-feature Iris data set. QSVM had a R2 of 0.84
after its training. PennyLane was used to design the 2-qubit QSVM and the 1-qubit 2-layer reuploading local
quantum surrogate. The local quantum-to-classical surrogate is implemented as per the classical surrogation
protocol, with the local quantum surrogate treated as a white-box model.

bounding box of ˜D is generated. The final surrogate at-
tains R2
Q→T(P) = 0.94. for the local region, as seen in
the second plot of Figure 5a.
Local classical surrogation on the local quantum surro-
gate is performed exactly as outlined before, wherein we
assume that the internal parameters of the local quantum
surrogate is known. For R2
C→Q (local classical surrogate
versus local quantum surrogate) for the local region, we
observe consistently high (mostly 1 due to the machine
precision of the simulations) R2
C→Q values regardless of
the window size due to the classical surrogation guaran-
tees associated with the local quantum surrogate based
on reuploading in our framework, as seen in the third
plot of Figure 5a.
In Figure 5b we see the relative error for both local
quantum surrogation and local classical surrogation. We
see that within the local region, the relative errors are
nominal. In both Figure 5a and Figure 5b we also show
the global behavior of the local surrogates. As expected,
outside the local region, the accuracy metrics perform
poorly for the local quantum surrogates.
This is the

trade-off we make to achieve high accuracy metrics inside
the local region within cost-efficient model constraints.
However, for local classical surrogates, the global ac-
curacy metrics perform well given enough data points
(although far fewer than the full data space) and given
full white-box access to the hyperparameters of the local
quantum surrogate. We ran the simulations for various
radii patch sizes, starting from 0.3 radii to 2.5 radii, all
centered at (0,0) as before. In Figure 6a we plot win-
dow size vs R2 and observe the reduction in R2
local for
local quantum surrogate as window size increases, local
quantum-to-classical surrogation R2
local is 1 regardless of
the window size.
In Figure 6b we plot the optimiza-
tion step vs training loss (MSE) for the local quantum
surrogate training. Loss converges well in relatively few
optimization steps for all these window sizes.

Thus, we have constructed a local quantum surrogate
for the QSVM with fewer qubit resources and generated
a local classical surrogate for the said local quantum sur-
rogate.
This exemplifies the cost reduction as well as
the dequantization of the inference phase aspects of the

## Page 9

(a) Patch radius r vs Local R2 for the local quantum
surrogate and its downstream local classical surrogate.

(b) Optimization step vs. training loss (MSE) for the same
set of patch radii in the case of local quantum surrogate; loss
converges within few iterations.

FIG. 6: Local-surrogate performance (top) and training
convergence (bottom) trained on the QSVM for varying
patch radii from 0.3 radii to 2.5 radii, all centered at
(0, 0).

2-step local surrogation protocol outlined in this paper.

D.
Practical limits of exact classical surrogation
protocol

To demonstrate the exponential blowup in the number
of quantum evaluations required with the classical sur-
rogation protocol [8], we worked with the Breast Cancer
Wisconsin (Diagnostic) dataset [38], containing 569 sam-
ples with 30 real–valued features and binary labels. To
compress redundancies while retaining ≈95% of the to-
tal variance, the feature matrix is projected onto its first
d = 6 principal components via PCA. Each component is
then standard-scaled to zero mean and unit variance, and
finally mapped to the interval [0, 2π) for ease of training
with the reuploading model. The class labels are mapped
from {0, 1} to {−1, +1}, matching the output range of a
Pauli-Z expectation value.
Local surrogate training is performed in the scaled

PCA space. For a given hyper-radius R we retain only
those samples whose absolute value in each coordinate
satisfies |xi| < R; geometrically this is an axis-aligned
hyper-cube of half-width R.
Radii are swept over the
grid R ∈{0.5, 0.55, . . . , 3.45}. For every hypercube patch
we train a reuploading-type local quantum surrogate fθ
with nq = 2 qubits and L = 3 data-reuploading layers in
the case of QSVM, written in PennyLane.
A local classical surrogate g is then fitted only to the
predictions fθ(x) on the same patch i.e nlocal.
Thus,
sample complexity scales linearly with nlocal under the
no-noise assumption.
We now employed a separable
Fourier basis

Φ(x) =

1, cos(kxj), sin(kxj)
j=1,...,d
k=1,...,L,

whose design matrix has 1 + 2Ld (37 columns for L = 3
and d = 6). This lacked the full expressiveness of the
Full Fourier basis, but was adequate for this simulation.
The least-squares solution α = (Φ⊤Φ)−1Φ⊤fθ(X) yields
g(x) = Φ(x)α.
In contrast, the exact classical surro-
gation protocol employs the full tensor-product Fourier
lattice exp(iω · x) with ω ∈{−L, . . . , L}d, requiring
(2L+1)d ((76 = 117,649 for our particular configuration)
basis functions and at least as many samples under the
no-noise assumption.
Thus our separable construction
slashes the sample complexity by a factor of ≈3 × 103

while still capturing the dominant single-coordinate har-
monics responsible for the quantum model’s behaviour
on each local patch. Due to exponential dependence on
the number of features, the exact classical surrogation
protocol quickly became computationally expensive for
this simulation. In the first and second plots in Figure 7
for local quantum and local classical surrogates we see
the familiar pattern of reduction in R2
local as the hyper-
cube patch radius increases. Unlike before, we don’t see
the near-perfect R2
local for classical surrogates. Neverthe-
less, we observed a R2
local of above 0.7 for our simulations
within the given patch range. This is an acceptable trade-
off given the high number of quantum evaluations re-
quired with the exact classical surrogation protocol. The
third plot shows the quantum calls/evaluations the sep-
arable classical surrogate required for each of the patch
radii.

VIII.
CONCLUSION

In this paper, we introduced a local surrogation pro-
tocol for quantum learning models. Within the protocol,
we introduced reuploading-type based local quantum sur-
rogates. These local quantum surrogates were trained on
sampled data within a local region of interest from a fully
trained arbitrary quantum learning model.
Given the classical surrogation guarantees associated
with these reuploading-type local quantum surrogates, it
is always possible to construct a local classical surrogate
for the local region [8]. This two-step protocol dequan-

## Page 10

FIG. 7: Local surrogation protocol on PCA reduced 6-feature Breast Cancer Wisconsin (Diagnostic) data set
to test the practical limits of classical surrogation protocol. Hypercube patch radii ranged between 0.5 −3.5 with
step size 0.05. PennyLane was used to design the 2-qubit 3-layer reuploading local quantum surrogate. The local
quantum-to-classical surrogate is implemented as per the simplified separable bases Fourier classical surrogate.

tizes and reduces the cost during the inference phase. Al-
ternatively, it is possible to directly train a Fourier based
local classical surrogate on the sampled data from the ar-
bitrary quantum learning model, but we would lack any
tight cost guarantees as in the two-step protocol outlined
earlier.
We ran several numerical experiments to validate our
two-step protocol, as well as the direct surrogation on
the sampled data. In each of these cases, we observed an
inverse relation between the size of the local region and
the local quantum surrogate’s accuracy metrics. This is
expected, given that the smaller the size of the local re-
gion, the fewer queries we require of the trained arbitrary
quantum model, the fewer computational resources, and
the easier it is for the Fourier-based local quantum sur-
rogates to fit the sampled data.
The local classical surrogate constructed from these
local quantum surrogates showed near-perfect accuracy
metrics as outlined in the classical surrogation protocol.
In this paper, the local quantum surrogates served as
an intermediary for the construction of the local clas-
sical surrogates for the dequantization of the inference
phase. But these local quantum surrogates could possi-
bly be used for other purposes, such as in retraining or
benchmarking quantum learning models, balancing train-
ing between different quantum architectures [39] and for
interpretability purposes, to name a few. An argument
can be made that for sufficiently large local quantum sur-
rogates, constructing a classical surrogate may become
computationally intractable, even with the classical sur-
rogation protocol, making the local quantum surrogate
preferable. Likewise, in the near future, large arbitrary
quantum learning models trained on fault-tolerant quan-
tum computers could potentially be surrogated with lo-
cal quantum surrogates trained on smaller NISQ devices,
thus offloading the inference phase onto cheaper, readily
accessible hardware while retaining the benefits of fault-
tolerant training.
Different training schemes, such as
sampling the arbitrary quantum learning model on a grid
and using that to train the local quantum surrogate could

certainly offer high accuracy metrics for a larger range of
patch sizes for the same quantum model configurations.

On a similar note, we observed a similar inverse re-
lation between the size of the local region and the di-
rectly trained local classical surrogate’s accuracy metrics
for quite a substantial number of cases.
Although we
lack any analytical cost guarantees, it might be possible
to construct better-performing directly trained local clas-
sical surrogates. As discussed earlier, the exact classical
surrogation protocol is well-suited for quantum models
trained on low-dimensional data. As there is no explicit
dependence on the size of the data space means that for
higher-dimensional data, even with localization, this pro-
tocol quickly becomes computationally intractable due
to the exponentially large number of quantum evalua-
tions it would require.
We showed an example of a
simpler separable bases Fourier surrogate in such cases,
but it works best when the local regions are relatively
small.
Designing better classical surrogation protocols
that achieve near-perfect accuracies without such quan-
tum call blowups is certainly an area for continued re-
search.

We chose the reuploading-type quantum model to con-
struct the framework to deploy our local surrogation pro-
tocol as it has analytically proven surrogation guarantees,
costs, and a surrogation protocol to back it up. It should
be possible to extend the local surrogation protocol to
work within other quantum learning architectures as the
basis for the local quantum surrogate. One such potential
architecture is the matrix product states (MPS) [40–42],
but it currently lacks analytical cost guarantees, as seen
in the case of reuploading architecture. Therefore, the
local surrogation protocol is expected to work effectively
when implemented within an appropriate architectural
framework.

## Page 11

Academy (SQA), for their continued support. We would
also like to thank Afrad Basheer (IQM Quantum Com-
puters), John Azariah (Microsoft, UTS), and Benjamin
Southwell (Dolby Labs Sydney) for their valuable discus-
sions on QML and DSP.

DATA AVAILABILITY

All code used in this work, including the ones for gen-
erating the figures, is available on the GitHub repos-
itory:
https://github.com/sreerajrajindrannair/
Local-surrogates-for-qml.

ACKNOWLEDGMENT

S.R.N. would like to acknowledge and thank his
doctoral research funding agency,
Sydney Quantum

[1] J. R. McClean, J. Romero, R. Babbush, and A. Aspuru-
Guzik, “The theory of variational hybrid quantum-
classical algorithms,” New Journal of Physics, vol. 18,
p. 023023, Feb. 2016.
[2] K. Mitarai, M. Negoro, M. Kitagawa, and K. Fujii,
“Quantum circuit learning,” Phys. Rev. A, vol. 98,
p. 032309, Sep 2018.
[3] V. Dunjko and H. J. Briegel, “Machine learning & arti-
ficial intelligence in the quantum domain,” 2017.
[4] Y. Wang and J. Liu, “A comprehensive review of quan-
tum machine learning: from nisq to fault tolerance,” Re-
ports on Progress in Physics, vol. 87, p. 116402, Oct.
2024.
[5] A. P´erez-Salinas, A. Cervera-Lierta, E. Gil-Fuster, and
J. I. Latorre, “Data re-uploading for a universal quantum
classifier,” Quantum, vol. 4, p. 226, Feb. 2020.
[6] A. P´erez-Salinas,
D. L´opez-N´u˜nez,
A. Garc´ıa-S´aez,
P. Forn-D´ıaz, and J. I. Latorre, “One qubit as a uni-
versal approximant,” Physical Review A, vol. 104, July
2021.
[7] M. Schuld, R. Sweke, and J. J. Meyer, “Effect of data en-
coding on the expressive power of variational quantum-
machine-learning models,”
Phys. Rev. A, vol. 103,
p. 032430, Mar 2021.
[8] F. J. Schreiber, J. Eisert, and J. J. Meyer, “Classical sur-
rogates for quantum learning models,” Physical Review
Letters, vol. 131, Sept. 2023.
[9] J. Cotler, H.-Y. Huang, and J. R. McClean, “Revisit-
ing dequantization and quantum advantage in learning
tasks,” 2021.
[10] M. Cerezo, M. Larocca, D. Garc´ıa-Mart´ın, N. L. Diaz,
P. Braccia, E. Fontana, M. S. Rudolph, P. Bermejo,
A. Ijaz, S. Thanasilp, E. R. Anschuetz, and Z. Holmes,
“Does provable absence of barren plateaus imply classi-
cal simulability? or, why we need to rethink variational
quantum computing,” 2024.
[11] S. Jerbi, C. Gyurik, S. C. Marshall, R. Molteni, and
V. Dunjko, “Shadows of quantum machine learning,” Na-
ture Communications, vol. 15, July 2024.
[12] A. Basheer, Y. Feng, C. Ferrie, and S. Li, “Alternating
layered variational quantum circuits can be classically
optimized efficiently using classical shadows,” 2022.
[13] M. S. Rudolph, E. Fontana, Z. Holmes, and L. Cincio,
“Classical surrogate simulation of quantum systems with
lowesa,” 2023.

[14] Y. Shao, F. Wei, S. Cheng, and Z. Liu, “Simulating
noisy variational quantum algorithms: A polynomial ap-
proach,” Physical Review Letters, vol. 133, Sept. 2024.
[15] L. J. Hong and X. Zhang, “Surrogate-based simulation
optimization,” 2021.
[16] R. Shaffer, L. Kocia, and M. Sarovar, “Surrogate-based
optimization for variational quantum algorithms,” Phys.
Rev. A, vol. 107, p. 032415, Mar 2023.
[17] A. Nakayama, H. Morisaki, K. Mitarai, H. Ueda, and
K. Fujii, “Explicit quantum surrogates for quantum ker-
nel models,” 2024.
[18] C. Molnar, Interpretable Machine Learning. 3 ed., 2025.
[19] L. Longo, M. Brcic, F. Cabitza, J. Choi, R. Con-
falonieri, J. D. Ser, R. Guidotti, Y. Hayashi, F. Her-
rera, A. Holzinger, R. Jiang, H. Khosravi, F. Lecue,
G. Malgieri, A. P´aez, W. Samek, J. Schneider, T. Speith,
and S. Stumpf, “Explainable artificial intelligence (xai)
2.0: A manifesto of open challenges and interdisciplinary
research
directions,”
Information
Fusion,
vol.
106,
p. 102301, June 2024.
[20] M. T. Ribeiro, S. Singh, and C. Guestrin, “”why should i
trust you?”: Explaining the predictions of any classifier,”
in Proceedings of the 22nd ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining,
KDD ’16, (New York, NY, USA), p. 1135–1144, Associ-
ation for Computing Machinery, 2016.
[21] L. Pira and C. Ferrie, “On the interpretability of quan-
tum neural networks,” Quantum Machine Intelligence,
vol. 6, Aug. 2024.
[22] S. W. Smith, The scientist and engineer’s guide to digital
signal processing. USA: California Technical Publishing,
1997.
[23] A. V. Oppenheim, Discrete-time signal processing. Pear-
son Education India, 1999.
[24] K. Prabhu, Window Functions and Their Applications in
Signal Processing. 10 2013.
[25] J. Allen, “Short term spectral analysis, synthesis, and
modification by discrete fourier transform,” IEEE trans-
actions on acoustics,
speech,
and signal processing,
vol. 25, no. 3, pp. 235–238, 1977.
[26] J. Allen and L. Rabiner, “A unified approach to short-
time fourier analysis and synthesis,” Proceedings of the
IEEE, vol. 65, no. 11, pp. 1558–1564, 1977.
[27] P. Duhamel and M. Vetterli, “Fast fourier transforms: A
tutorial review and a state of the art,” Signal Processing,
vol. 19, no. 4, pp. 259–299, 1990.

## Page 12

[28] T. G. Stockham, “High-speed convolution and correla-
tion,” in Proceedings of the April 26-28, 1966, Spring
Joint Computer Conference, AFIPS ’66 (Spring), (New
York, NY, USA), p. 229–233, Association for Computing
Machinery, 1966.
[29] P. Bergold and C. Lasser, “Fourier series windowed by a
bump function,” 2020.
[30] S. Lerch, R. Puig, M. S. Rudolph, A. Angrisani, T. Jones,
M. Cerezo, S. Thanasilp, and Z. Holmes, “Efficient
quantum-enhanced classical simulation for patches of
quantum landscapes,” 2024.
[31] J. G. Vidal and D. O. Theis, “Input redundancy for pa-
rameterized quantum circuits,” 2020.
[32] J. Landman, S. Thabet, C. Dalyac, H. Mhiri, and
E. Kashefi, “Classically approximating variational quan-
tum machine learning with random fourier features,”
2022.
[33] L. Carleson, “On convergence and growth of partial sums
of fourier series,” 1966.
[34] B. Casas and A. Cervera-Lierta,
“Multidimensional
fourier series with quantum circuits,” Phys. Rev. A,
vol. 107, p. 062612, Jun 2023.
[35] M. Schuld and N. Killoran, “Is quantum advantage the
right goal for quantum machine learning?,” PRX Quan-
tum, vol. 3, July 2022.
[36] V. Bergholm, J. Izaac, M. Schuld, C. Gogolin, S. Ahmed,
V. Ajith, M. S. Alam, G. Alonso-Linaje, B. Akash-
Narayanan, A. Asadi, J. M. Arrazola, U. Azad, S. Ban-
ning, C. Blank, T. R. Bromley, B. A. Cordier, J. Ceroni,
A. Delgado, O. D. Matteo, A. Dusko, T. Garg, D. Guala,
A. Hayes, R. Hill, A. Ijaz, T. Isacsson, D. Ittah, S. Ja-

hangiri, P. Jain, E. Jiang, A. Khandelwal, K. Kottmann,
R. A. Lang, C. Lee, T. Loke, A. Lowe, K. McKiernan,
J. J. Meyer, J. A. Monta˜nez-Barrera, R. Moyard, Z. Niu,
L. J. O’Riordan, S. Oud, A. Panigrahi, C.-Y. Park,
D. Polatajko, N. Quesada, C. Roberts, N. S´a, I. Schoch,
B. Shi, S. Shu, S. Sim, A. Singh, I. Strandberg, J. Soni,
A. Sz´ava, S. Thabet, R. A. Vargas-Hern´andez, T. Vin-
cent, N. Vitucci, M. Weber, D. Wierichs, R. Wiersema,
M. Willmann, V. Wong, S. Zhang, and N. Killoran, “Pen-
nylane:
Automatic differentiation of hybrid quantum-
classical computations,” 2022.
[37] R. A. Fisher, “Iris.” UCI Machine Learning Repository,
1936. DOI: https://doi.org/10.24432/C56C76.
[38] W.
Wolberg,
O.
Mangasarian,
N.
Street,
and
W.
Street,
“Breast
Cancer
Wisconsin
(Diagnos-
tic).” UCI Machine Learning Repository, 1993.
DOI:
https://doi.org/10.24432/C5DW2B.
[39] R. Bhowmick, H. Wadhwa, A. Singh, T. Sidana, Q. H.
Tran, and K. K. Sabapathy, “Enhancing variational
quantum algorithms by balancing training on classical
and quantum hardware,” 2025.
[40] D. Perez-Garcia, F. Verstraete, M. M. Wolf, and J. I.
Cirac, “Matrix product state representations,” 2007.
[41] J. C. Bridgeman and C. T. Chubb, “Hand-waving and
interpretive dance: an introductory course on tensor net-
works,” Journal of Physics A: Mathematical and Theo-
retical, vol. 50, p. 223001, May 2017.
[42] S. Shin, Y. S. Teo, and H. Jeong, “Dequantizing quantum
machine learning models using tensor networks,” Phys.
Rev. Res., vol. 6, p. 023218, May 2024.

## Page 13

TABLE I: 2D target functions used in our experiments

Function Name
Definition

Default Function
−0.02 + 0.04 cos(2x + y) + 0.25 sin x −0.30 cos(2y) −0.10 sin(x −y)

Polynomial
0.10 x2 −0.20 y + 0.30 xy −0.40 x + 2.0

Sinc
sin r

x2 + y2 + ε

r
,
r =
p

Random Trig
a1 sin x + a2 cos y + b1 sin(2x + 0.5y) + b2 cos(2y −0.3x) + a3x + b3y, ai, bi ∼U(−1, 1)

Big Trig
0.70 sin(0.5x) + 0.40 sin(2.2y) −0.30 cos(2.0x + 1.3y) + 0.25 sin(1.5x −0.8y) + 0.15 cos(0.9x +
2.1y) + 0.05 sin(3.0x + 0.2y)

Combined Oscillator 0.05 x2 −0.10 y + 0.60 cos(1.2x + 0.5y) −0.40 sin(0.8x −1.3y) + 0.35 cos(2x) + 0.20 sin(2y)

3
X

i=1
αi sin(ωx,ix + ωy,iy) + βi cos(˜ωx,ix ± ˜ωy,iy), αi, βi ∼U(−1, 1), ω(·) ∈[0.5, 2.5]

Random Trig 2

Freq Soup
0.30 sin(x + 2y) + 0.20 cos(2x + y) + 0.15 sin(3x + 3y) + 0.10 cos(x −3y) + 0.05 sin(2x −2y)

Peaks Trig
0.50 cos(1.3x −0.5y) + 0.40 sin(2.1x + 0.7y) −0.30 cos(3.0x −2.2y) + 0.20 sin(1.1x −3.0y) +
0.10 cos(0.6x + 0.3y)

x2 + y2, θ =
atan2(y, x)

Spiral Mix
0.10 r + 0.50 sin(2θ) + 0.25 cos(3θ) −0.20 sin(0.5x −0.8y) + 0.05 r cos(5θ), r =
p

K
X

K
X

h
Akx,ky cos(kxx + kyy + ϕkx,ky) + Bkx,ky sin(kxx + kyy −ϕkx,ky)
i

Random Fourier

kx=1

ky=1

Large Amplitude Mix 2.5 sin(1.2x+0.7y)−2.0 cos(0.6x−1.1y)+1.5 sin(2.0x−2.5y)+0.8 cos(3.0x+2.0y)−0.3 sin(4.0x−
0.2y)

Cross Terms
sin(x + y) + 0.5 cos(2x −y) −0.4 sin(3y + 2.1x) + 0.3 cos(1.2x −2.5y) + 0.2 x sin y
