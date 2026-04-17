---
source_pdf: ../doi_10.1038_s41467-021-22539-9.pdf
pages: 9
extracted_at: 2026-04-17T12:32:47+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "Power of data in quantum machine learning"
author: "Hsin-Yuan Huang"
---

# doi_10.1038_s41467-021-22539-9

Original title: Power of data in quantum machine learning

Author metadata: Hsin-Yuan Huang

Source PDF: ../doi_10.1038_s41467-021-22539-9.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

ARTICLE

Power of data in quantum machine learning

Hsin-Yuan Huang1,2,3, Michael Broughton1, Masoud Mohseni1, Ryan Babbush1, Sergio Boixo
1,
Hartmut Neven1 & Jarrod R. McClean
1✉

The use of quantum computing for machine learning is among the most exciting prospective
applications of quantum technologies. However, machine learning tasks where data is pro-
vided can be considerably different than commonly studied computational tasks. In this work,
we show that some problems that are classically hard to compute can be easily predicted by
classical machines learning from data. Using rigorous prediction error bounds as a founda-
tion, we develop a methodology for assessing potential quantum advantage in learning tasks.
The bounds are tight asymptotically and empirically predictive for a wide range of learning
models. These constructions explain numerical results showing that with the help of data,
classical machine learning models can be competitive with quantum models even if they are
tailored to quantum problems. We then propose a projected quantum model that provides a
simple and rigorous quantum speed-up for a learning problem in the fault-tolerant regime. For
near-term implementations, we demonstrate a signiﬁcant prediction advantage over some
classical models on engineered data sets designed to demonstrate a maximal quantum
advantage in one of the largest numerical tests for gate-based quantum machine learning to
date, up to 30 qubits.

1234567890():,;

1 Google Quantum AI, Venice, CA, USA. 2 Institute for Quantum Information and Matter, Caltech, Pasadena, CA, USA. 3 Department of Computing and
Mathematical Sciences, Caltech, Pasadena, CA, USA. ✉email: jmcclean@google.com

NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications
1

## Page 2

ARTICLE
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9

A

We use our prediction error bounds to devise a ﬂowchart for
testing potential quantum prediction advantage, the separation
between prediction errors of quantum and classical ML models
for a ﬁxed amount of training data. The most important test is a
geometric difference between kernel functions deﬁned by classical
and quantum ML. Formally, the geometric difference is deﬁned
by the closest efﬁcient classical ML model. In practice, one should
consider the geometric difference with respect to a suite of
optimized classical ML models. If the geometric difference is
small, then a classical ML method is guaranteed to provide
similar or better performance in prediction on the dataset,
independent of the function values or labels. Hence this repre-
sents a powerful, function independent prescreening that allows
one to evaluate if there is any possibility of better performance.
On the other hand, if the geometry differs greatly, we show both
the existence of a dataset that exhibits large prediction advantage
using the quantum ML model and how one can construct it
efﬁciently. While the tools we develop could be used to compare
and construct hard classical models like hash functions, we
enforce restrictions that allow us to say something about a
quantum separation. In particular, the feature map will be white
box, in that a quantum circuit speciﬁcation is available for the
ideal feature map, and that feature map can be made computa-
tionally hard to evaluate classically. A constructive example of
this is a discrete log feature map, where a provable separation for
our kernel is given in Supplementary Section 11. Additionally, the
minimum over classical models means that classical hash func-
tions are reproduced formally by deﬁnition.
Moreover, application of these tools to existing models in the
literature rules many of them out immediately, providing a
powerful sieve for focusing development of new data encodings.
Following these constructions, in numerical experiments, we ﬁnd
that a variety of common quantum models in the literature
perform similarly or worse than classical ML on both classical
and quantum datasets due to a small geometric difference. The
small geometric difference is a consequence of the exponentially
large Hilbert space employed by existing quantum models, where
all inputs are too far apart. To circumvent the setback, we propose
an improvement, which enlarges the geometric difference by
projecting quantum states embedded from classical data back to
approximate classical representation25–27. With the large geo-
metric difference endowed by the projected quantum model, we
are able to construct engineered datasets to demonstrate large
prediction advantage over common classical ML models in
numerical experiments up to 30 qubits. Despite our constructions
being based on methods with associated kernels, we ﬁnd
empirically that the prediction advantage remains robust across
tested classical methods, including those without an easily
determined kernel. This opens the possibility to use a small
quantum computer to generate efﬁciently veriﬁable machine
learning problems that could be challenging for classical ML
models.

s quantum technologies continue to rapidly advance, it
becomes increasingly important to understand which
applications can beneﬁt from the power of these devices.
At the same time, machine learning on classical computers has
made great strides, revolutionizing applications in image recog-
nition, text translation, and even physics applications, with more
computational power leading to ever increasing performance1. As
such, if quantum computers could accelerate machine learning,
the potential for impact is enormous.
At least two paths towards quantum enhancement of machine
learning have been considered. First, motivated by quantum
applications in optimization2–4, the power of quantum comput-
ing could, in principle, be used to help improve the training
process of existing classical models5,6, or enhance inference in
graphical models7. This could include ﬁnding better optima in a
training landscape or ﬁnding optima with fewer queries. How-
ever, without more structure known in the problem, the advan-
tage along these lines may be limited to quadratic or small
polynomial speedups8,9.
The second vein of interest is the possibility of using quantum
models to generate correlations between variables that are inef-
ﬁcient to represent through classical computation. The recent
success both theoretically and experimentally for demonstrating
quantum computations beyond classical tractability can be taken
as evidence that quantum computers can sample from probability
distributions that are exponentially difﬁcult to sample from
classically10,11. If these distributions were to coincide with real-
world distributions, this would suggest the potential for sig-
niﬁcant advantage. This is typically the type of advantage that has
been
sought
in
recent
work
on
both
quantum
neural
networks12–14, which seek to parameterize a distribution through
some
set
of
adjustable
parameters,
and
quantum
kernel
methods15 that use quantum computers to deﬁne a feature map
that maps classical data into the quantum Hilbert space. The
justiﬁcation for the capability of these methods to exceed classical
models often follows similar lines as refs. 10,11 or quantum
simulation results. That is, if the model leverages a quantum
circuit that is hard to sample results from classically, then there is
potential for a quantum advantage.
In this work, we show quantitatively how this picture is
incomplete in machine learning (ML) problems where some
training data are provided. The provided data can elevate classical
models to rival quantum models, even when the quantum circuits
generating the data are hard to compute classically. We begin
with a motivating example and complexity-theoretic argument
showing how classical algorithms with data can match quantum
output. Following this, we provide rigorous prediction error
bounds for training classical and quantum ML methods based on
kernel functions15–24 to learn quantum mechanical models. We
focus on kernel methods, as they not only provide provable
guarantees, but are also very ﬂexible in the functions they can
learn. For example, recent advancements in theoretical machine
learning show that training neural networks with large hidden
layers is equivalent to training an ML model with a particular
kernel, known as the neural tangent kernel19–21. Throughout,
when we refer to classical ML models related to our theoretical
developments, we will be referring to ML models that can be
easily associated with a kernel, either explicitly as in kernel
methods, or implicitly as in the neural tangent kernels. However,
in the numerical section, we will also include performance
comparisons to methods where direct association of a kernel is
challenging, such as random forest methods. In the quantum
case, we will also show how quantum ML based on kernels can be
made equivalent to training an inﬁnite depth quantum neural
network.

Results
Setup and motivating example. We begin by setting up the
problems and methods of interest for classical and quantum
models, and then provide a simple motivating example for
studying how data can increase the power of classical models on
quantum data. The focus will be a supervised learning task with a
collection of N training examples {(xi, yi)}, where xi is the input
data and yi is an associated label or value. We assume that xi are
sampled independently from a data distribution D.
In our theoretical analysis, we will consider yi 2 R to be
generated by some quantum model. In particular, we consider a

2
NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications

## Page 3

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9
ARTICLE

continuous encoding unitary that maps a classical input data xi
into quantum state
xi
 
¼ UencðxiÞ 0j in
and
refer to the
corresponding density matrix as ρ(xi). The expressive power of
these embeddings have been investigated from a functional
analysis point of view28,29; however, the setting where data are
provided requires special attention. The encoding unitary is
followed by a unitary UQNN(θ). We then measure an observable O
after the quantum neural network. This produces the label/value
for input xi given as yi ¼ f ðxiÞ ¼ xi
 Uy
QNNOUQNN xi
 
. The
quantum model considered here is also referred to as a quantum
neural network (QNN) in the literature14,30. The goal is to
understand when it is easy to predict the function f(x) by training
classical/quantum machine learning models.
With notation in place, we turn to a simple motivating example
to understand how the availability of data in machine learning
tasks can change computational hardness. Consider data points
fxigN
i¼1 that are p-dimensional classical vectors with ∣∣xi∣∣2 = 1, and
use amplitude encoding31–33 to encode the data into an n-qubit
state xi
 
¼ ∑p
k¼1 xk
i kj i, where xk
i is the individual coordinate of
the vector xi. If UQNN is a time-evolution under a many-body
Hamiltonian, then the function f ðxÞ ¼ x
h jUy
QNNOUQNN xj i is in
general hard to compute classically34, even for a single input state.
In particular, we have the following proposition showing that if a
classical algorithm can compute f(x) efﬁciently, then quantum
computers will be no more powerful than classical computers; see
Supplementary Section 1 for a proof.

write out the expectation value as

k¼1 xk
i
k
h j


Uy
QNNOUQNN
∑
p

l¼1 xl
i lj i



f ðxiÞ ¼
∑
p

l¼1 Bklxk
i xl
i;
ð1Þ

¼ ∑
p

k¼1 ∑
p

which
is
a
quadratic
function
with
p2
coefﬁcients
Bkl ¼ k
h jUy
QNNOUQNN lj i. Using the theory developed later in
this work, we can show that, for any UQNN and O, training a
speciﬁc classical ML model on a collection of N training examples
{(xi, yi = f(xi))} would give rise to a prediction model h(xi) with

r

ﬃﬃﬃﬃ
p2

;
ð2Þ

ExDjhðxÞ  f ðxÞj ≤c

N

for a constant c > 0. We refer to Supplementary Section 1 for the
proof of this result. Hence, with N ∝p2/ϵ2 training data, one can
train a classical ML model to predict the function f(x) up to an
additive prediction error ϵ. This elevation of classical models
through some training samples is illustrative of the power of data.
In Supplementary Section 2, we give a rigorous complexity-
theoretic argument on the computational power provided by
data. A cartoon depiction of the complexity separation induced
by data is provided in Fig. 1(a).
While this simple example makes the basic point that sufﬁcient
data can change complexity considerations, it perhaps opens
more questions than it answers. For example, it uses a rather
weak encoding into amplitudes and assumes one has access to an
amount of data that is on par with the dimension of the model.
The more interesting cases occur if we strengthen the data
encoding, include modern classical ML models, and consider the
number of data N much less than the dimension of the model.
These more interesting cases are the ones we quantitatively
answer.

Proposition 1. If a classical algorithm without training
data can compute f(x) efﬁciently for any UQNN and O, then
BPP = BQP.
Nevertheless, it is incorrect to conclude that training a classical
model from data to learn this evolution is hard. To see this, we

Fig. 1 Illustration of the relation between complexity classes and a ﬂowchart for understanding and prescreening potential quantum advantage. a We
cartoon the separation between problem complexities that are created by the addition of data to a problem. Classical algorithms that can learn from data
deﬁne a complexity class that can solve problems beyond classical computation (BPP), but it is still expected that quantum computation can efﬁciently
solve problems that classical ML algorithms with data cannot. A rigorous deﬁnition and proof for the separation between classical algorithms that can learn
from data and BPP/BQP is given in Supplementary Section 2. b The ﬂowchart we develop for understanding the potential for quantum prediction
advantage. N samples of data from a potentially inﬁnite depth QNN made with encoding and function circuits Uenc and UQNN are provided as input along
with quantum and classical methods with associated kernels. Tests are given as functions of N to emphasize the role of data in the possibility of a
prediction advantage. One can ﬁrst evaluate a geometric quantity gCQ that measures the possibility of an advantageous quantum/classical prediction
separation without yet considering the actual function to learn. We show how one can efﬁciently construct an adversarial function that saturates this limit if
the test is passed, otherwise the classical approach is guaranteed to match performance for any function of the data. To subsequently consider the actual
function provided, a label/function-speciﬁc test may be run using the model complexities sC and sQ. If one speciﬁcally uses the quantum kernel (QK)
method, the red dashed arrows can evaluate if all possible choices of UQNN lead to an easy classical function for the chosen encoding of the data.

NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications
3

## Page 4

ARTICLE
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9

Our primary interest will be ML algorithms that are much
stronger than ﬁtting a quadratic function and the input data are
provided in more interesting ways than an amplitude encoding.
In this work, we focus on both classical and quantum ML models
based on kernel functions k(xi, xj). At a high level, a kernel
function can be seen as a measure of similarity, if k(xi, xj) is large
when xi and xj are close. When considered for ﬁnite input data, a
kernel function may be represented as a matrix Kij = k(xi, xj) and
the conditions required for kernel methods are satisﬁed when the
matrix representation is Hermitian and positive semi-deﬁnite.
A given kernel function corresponds to a nonlinear feature
mapping ϕ(x) that maps x to a possibly inﬁnite-dimensional
feature space, such that kðxi; xjÞ ¼ ϕðxiÞyϕðxjÞ. This is the basis of
the so-called “kernel trick” where intricate and powerful maps ϕ
(xi) can be implemented through the evaluation of relatively
simple kernel functions k. As a simple case, in the example above,
using a kernel of k(xi, xj) = ∣〈xi∣xj〉∣2 corresponds to a feature map
ϕðxiÞ ¼ ∑klxk
i xl
i kj i  lj i which is capable of learning quadratic
functions in the amplitudes. In kernel based ML algorithms, the
trained model can always be written as h(x) = w†ϕ(x) where w is
a vector in the feature space deﬁned by the kernel. For example,
training a convolutional neural network with large hidden
layers19,35 is equivalent to using a corresponding neural tangent
kernel kCNN. The feature map ϕCNN for the kernel kCNN is a
nonlinear mapping that extracts all local properties of x35. In
quantum mechanics, similarly a kernel function can be deﬁned
using the native geometry of the quantum state space xj i. For
example, we can deﬁne the kernel function as 〈xi∣xj〉or ∣〈xi∣xj〉∣2.
Using the output from this kernel in a method like a classical
support vector machine16 deﬁnes the quantum kernel method.
A wide class of functions can be learned with a sufﬁciently
large amount of data by using the right kernel function k. For
example, in contrast to the perhaps more natural kernel, 〈xi∣xj〉,
the quantum kernel kQ(xi, xj) = ∣〈xi∣xj〉∣2 = Tr(ρ(xi)ρ(xj)) can
learn arbitrarily deep quantum neural network UQNN that
measures any observable O (shown in Supplementary Section 3),
and the Gaussian kernel, kγðxi; xjÞ ¼ expðγjjxi  xjjj2Þ with
hyperparameter γ, can learn any continuous function in a
compact space36, which includes learning any QNN. Never-
theless, the required amount of data N to achieve a small
prediction error could be very large in the worst case. Although
we will work with other kernels deﬁned through a quantum
space, due both to this expressive property and terminology of
past work, we will refer to kQðxi; xjÞ ¼ Tr

ρðxiÞρðxjÞ
as the
quantum kernel method throughout this work, which is also the
deﬁnition given in15.

Testing quantum advantage. We now construct our more general
framework for assessing the potential for quantum prediction
advantage in a machine learning task. Beginning from a general
result, we build both intuition and practical tests based on the geo-
metry of the learning spaces. This framework is summarized in Fig. 1.
Our foundation is a general prediction error bound for training
classical/quantum ML models to predict some quantum model
deﬁned by f(x) = Tr(OUρ(x)) derived from concentration inequal-
ities, where OU ¼ Uy
QNNOUQNN. Suppose we have obtained N
training examples {(xi, yi = f(xi))}. After training on this data,
there exists an ML algorithm that outputs h(x) = w†ϕ(x) using
kernel
kðxi; xjÞ ¼ Kij ¼ ϕðxiÞyϕðxjÞ,
which
has
a
simpliﬁed
prediction error bounded by

r
ð3Þ

ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
sKðNÞ
N

ExDjhðxÞ  f ðxÞj ≤c

for a constant c > 0 and N independent samples from the data

distribution D. We note here that this and all subsequent bounds
have a key dependence on the quantity of data N, reﬂecting
the role of data to improve prediction performance. Due to a
scaling freedom between αϕ(x) and w/α, we have assumed
∑N
i¼1 ϕðxiÞyϕðxiÞ ¼ Tr ðKÞ ¼ N. A derivation of this result is
given in Supplementary Section 4.
Given this core prediction error bound, we now seek to
understand its implications. The main quantity that determines
the prediction error is

sKðNÞ ¼ ∑
N

i¼1 ∑
N

j¼1 ðK1Þij Tr ðOUρðxiÞÞ Tr ðOUρðxjÞÞ:
ð4Þ

The quantity sK(N) is equal to the model complexity of the
trained function h(x) = w†ϕ(x), where sK(N) = ∣∣w∣∣2 = w†w after
training. A smaller value of sK(N) implies better generalization to
new data x sampled from the distribution D. Intuitively, sK(N)
measures whether the closeness between xi, xj deﬁned by the
kernel function k(xi, xj) matches well with the closeness of the
observable
expectation
for
the
quantum
states
ρ(xi), ρ(xj),
recalling that a larger kernel value indicates two points are
closer. The computation of sK(N) can be performed efﬁciently on
a classical computer by inverting an N × N matrix K after
obtaining the N values Tr(OUρ(xi)) by performing order N
experiments on a physical quantum device. The time complexity
scales at most as order N3. Due to the connection between w†w
and the model complexity, a regularization term w†w is often
added to the optimization problem during the training of h(x) =
w†ϕ(x), see e.g., refs. 16,37,38. Regularization prevents sK(N) from
becoming too large at the expense of not completely ﬁtting the
training data. A detailed discussion and proof under regulariza-
tion is given in Supplementary Section 4 and 6.
The prediction error upper bound can often be shown to be
asymptotically tight by proving a matching lower bound. As an
example, when k(xi, xj) is the quantum kernel Tr(ρ(xi)ρ(xj)), we
can deduce that sK(N) ≤Tr(O2) hence one would need a number
of data N scaling as Tr(O2). In Supplementary Section 8, we give a
matching lower bound showing that a scaling of Tr(O2) is
unavoidable if we assume a large Hilbert space dimension. This
lower bound holds for any learning algorithm and not only for
quantum kernel methods. The lower bound proof uses mutual
information analysis and could easily extend to other kernels.
This proof strategy is also employed extensively in a follow-up
work39 to devise upper and lower bounds for classical and
quantum ML in learning quantum models. Furthermore, not only
are the bounds asymptotically tight, in numerical experiments
given in Supplementary Section 13 we ﬁnd that the prediction
error bound also captures the performance of other classical ML
models not based on kernels where the constant factors are
observed to be quite modest.
Given some set of data, if sK(N) is found to be small relative to
N after training for a classical ML model, this quantum model f(x)
can be predicted accurately even if f(x) is hard to compute
classically for any given x. In order to formally evaluate the
potential for quantum prediction advantage generally, one must
take sK(N) to be the minimal over efﬁcient classical models.
However, we will be more focused on minimally attainable values
over a reasonable set of classical methods with tuned hyperpara-
meters. This prescribes an effective method for evaluating
potential quantum advantage in practice, and already rules out
a considerable number of examples from the literature.
From the bound, we can see that the potential advantage for
one ML algorithm deﬁned by K1 to predict better than another
ML algorithm deﬁned by K2 depends on the largest possible
separation between sK1 and sK2 for a dataset. The separation can
be characterized by deﬁning an asymmetric geometric difference

4
NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications

## Page 5

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9
ARTICLE

Fig. 2 Cartoon of the geometry (kernel function) deﬁned by classical and quantum ML models. The letters A, B, ... represent data points {xi} in different
spaces with arrows representing the similarity measure (kernel function) between data. The geometric difference g is a difference between similarity
measures (arrows) in different ML models and d is an effective dimension of the dataset in the quantum Hilbert space.

that depends on the dataset, but is independent of the function
values or labels. Hence evaluating this quantity is a good ﬁrst step
in understanding if there is a potential for quantum advantage, as
shown in Fig. 1. This quantity is deﬁned by

g12 ¼ gðK1jjK2Þ ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
jj
ﬃﬃﬃﬃﬃ
K2
p
ðK1Þ1
ﬃﬃﬃﬃﬃ
K2
p
jj1

q
;
ð5Þ

where ∣∣. ∣∣∞is the spectral norm of the resulting matrix and we
assume Tr(K1) = Tr(K2) = N. One can show that sK1 ≤g2
12sK2,
which
implies
the
prediction
error
bound
c
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
sK1=N
p
≤cg12
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
sK2=N
p
.
A
detailed
derivation is
given
in
Supplementary Section C and an illustration of g12 can be found
in Fig. 2. The geometric difference g(K1∣∣K2) can be computed on
a classical computer by performing a singular value decomposi-
tion of the N × N matrices K1 and K2. Standard numerical
analysis packages40 provide highly efﬁcient computation of a
singular value decomposition in time at most order N3.
Intuitively, if K1(xi, xj) is small/large when K2(xi, xj) is small/
large, then the geometric difference g12 is a small value ~1, where
g12 grows as the kernels deviate.
To see more explicitly how the geometric difference allows one
to make statements about the possibility for one ML model to
make different predictions from another, consider the geometric
difference gCQ = g(KC∣∣KQ) between a classical ML model with
kernel kC(xi, xj) and a quantum ML model, e.g., with kQ(xi, xj) =
Tr(ρ(xi)ρ(xj)). If gCQ is small, because

sC ≤g2
CQsQ;
ð6Þ

the classical ML model will always have a similar or better model
complexity sK(N) compared to the quantum ML model. This
implies that the prediction performance for the classical ML will
likely be competitive or better than the quantum ML model, and
one is likely to prefer using the classical model. This is captured in
the ﬁrst step of our ﬂowchart in Fig. 1.
In contrast, if gCQ is large we show that there exists a dataset
with sC ¼ g2
CQsQ with the quantum model exhibiting superior

prediction
performance.
An
efﬁcient
method
to
explicitly
construct such a maximally divergent dataset is given in
Supplementary Section 7 and a numerical demonstration of the
stability of this separation is provided in the next section. While a
formal statement about classical methods generally requires
deﬁning it overall efﬁcient classical methods, in practice, we
consider gCQ to be the minimum geometric difference among a
suite of optimized classical ML models. Our engineered approach
minimizes this value as a hyperparameter search to ﬁnd the best
classical adversary, and shows remarkable robustness across
classical methods including those without an associated kernel,
such as random forests41.
In the speciﬁc case of the quantum kernel method with
KQ
ij ¼ kQðxi; xjÞ ¼ Tr ðρðxiÞρðxjÞÞ, we can gain additional insights
into the model complexity sK, and sometimes make conclusions
about classically learnability for all possible UQNN for the given
encoding of the data. Let us deﬁne vec(X) for a Hermitian matrix
X to be a vector containing the real and imaginary part of each
entry in X. In this case, we ﬁnd sQ ¼ vecðOUÞ
TPQvecðOUÞ, where
PQ is the projector onto the subspace formed by {vec(ρ(x1)), …,
vec(ρ(xN))}. We highlight

d ¼ dim ðPQÞ ¼ rank ðKQÞ ≤N;
ð7Þ

which deﬁnes the effective dimension of the quantum state space
spanned by the training data. An illustration of the dimension d can
be found in Fig. 1. Because PQ is a projector and has eigenvalues 0
or 1, sQ ≤minðd; vecðOUÞ
TvecðOUÞÞ ¼ minðd; Tr ðO2ÞÞ assuming
∣∣O∣∣∞≤1. Hence in the case of the quantum kernel method, the
prediction error bound may be written as

r

ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
minðd; Tr ðO2ÞÞ
N

:
ð8Þ

Ex2DjhðxÞ  f ðxÞj ≤c

A detailed derivation is given in Supplementary Section A. We can
also consider the approximate dimension d, where small eigenva-
lues in KQ are truncated, by incurring a small training error. After

NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications
5

## Page 6

ARTICLE
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9

obtaining KQ from a quantum device, the dimension d can be
computed efﬁciently on a classical machine by performing a
singular value decomposition on the N × N matrix KQ. Estimation
of Tr(O2) can be performed by sampling random states ψ
 
from a
quantum 2-design, measuring O on ψ
 
, and performing statistical
analysis on the measurement data25. This prediction error bound
shows that a quantum kernel method can learn any UQNN when the
dimension of the training set space d or the squared Frobenius
norm of observable Tr(O2) is much smaller than the amount of data
N. In Supplementary Section 8, we show that quantum kernel
methods are optimal for learning quantum models with bounded
Tr(O2) as they saturate the fundamental lower bound. However, in
practice, most observables, such as Pauli operators, will have
exponentially large Tr(O2), so the central quantity is the dimension
d. Using the prediction error bound for the quantum kernel
method, if both gCQ and minðd; Tr ðO2ÞÞ are small, then a classical
ML would also be able to learn any UQNN. In such a case, one must
conclude that the given encoding of the data is classically easy, and
this cannot be affected by an arbitrarily deep UQNN. This constitutes
the bottom left part of our ﬂowchart in Fig. 1.
Ultimately, to see a prediction advantage in a particular
dataset with speciﬁc function values/labels, we need a large
separation between sC and sQ. This happens when the inputs xi,
xj considered close in a quantum ML model are actually close in
the target function f(x), but are far in classical ML. This is
represented as the ﬁnal test in Fig. 1 and the methodology here
outlines how this result can be achieved in terms of its more
essential components.

that is capable of expressing arbitrary functions of powers of the
1-RDMs of the quantum state. From nonintuitive results in
density functional theory, we know even one body densities can
be sufﬁcient for determining exact ground state45 and time-
dependent46 properties of many-body systems under modest
assumptions. In Supplementary Section 10, we provide examples
of other projected quantum kernels. This includes an efﬁcient
method for computing a kernel function that contains all orders
of RDMs using local randomized measurements and the
formalism of classical shadows25. The classical shadow formalism
allows efﬁcient construction of RDMs from very few measure-
ments. In Supplementary Section 11, we show that projected
versions of quantum kernels lead to a simple and rigorous
quantum speed-up in a recently proposed learning problem based
on discrete logarithms24.

Numerical studies. We now provide numerical evidence up to 30
qubits that supports our theory on the relation between the
dimension d, the geometric difference g, and the prediction per-
formance. Using the projected quantum kernel, the geometric
difference g is much larger and we see the strongest empirical
advantage of a scalable quantum model on quantum datasets to
date. These are the largest combined simulation and analysis in
digital quantum machine learning that we are aware of, and make
use of the TensorFlow and TensorFlow-Quantum package47,
reaching a peak throughput of up to 1.1 quadrillion ﬂoating point
operations per second (petaﬂop/s). Trends of ~300 teraﬂop/s for
quantum simulation and 800 teraﬂop/s for classical analysis were
observed up to the maximum experiment size with the overall
ﬂoating point operations across all experiments totalling ~2
quintillion (exaﬂop).
In order to mimic a data distribution that pertains to real-world
data, we conduct our experiments around the fashion-MNIST
dataset48, which is an image classiﬁcation for distinguishing
clothing items, and is more challenging than the original digit-
based MNIST source49. We preprocess the data using principal
component
analysis50
to
transform
each
image
into
an
n-dimensional vector. The same data are provided to the quantum
and classical models, where in the classical case the data is the
n-dimensional input vector, and the quantum case uses a given
circuit to embed the n-dimensional vector into the space of
n qubits. For quantum embeddings, we explore three options, E1
is a separable rotation circuit32,51,52, E2 is an IQP-type embedding
circuit15, and E3 is a Hamiltonian evolution circuit, with explicit
constructions in Supplementary Section 12.
For the classical ML task (C), the goal is to correctly identify
the images as shirts or dresses from the original dataset. For the
quantum ML tasks, we use the same fashion-MINST source data
and embeddings as above, but take as function values the
expectation value of a local observable that has been evolved
under a quantum neural network resembling the Trotter
evolution of 1D-Heisenberg model with random couplings. In
these cases, the embedding is taken as part of the ground truth, so
the resulting function will be different depending on the quantum
embedding. For these ML tasks, we compare against the best
performing model from a list of standard classical ML algorithms
with properly tuned hyperparameters (see Supplementary Sec-
tion 12 for details).
In Fig. 3, we give a comparison between the prediction
performance of classical and quantum ML models. One can see
that not only do classical ML models perform best on the original
classical dataset, the prediction performance for the classical
methods on the quantum datasets is also very competitive and
can even outperform existing quantum ML models despite the
quantum ML models having access to the training embedding

Projected quantum kernels. In addition to analyzing existing
quantum models, the analysis approach introduced also provides
suggestions for new quantum models with improved properties,
which we now address here. For example, if we start with the
original quantum kernel, when the effective dimension d is large,
kernel Tr(ρ(xi)ρ(xj)), which is based on a ﬁdelity-type metric, will
regard all data to be far from each other and the kernel matrix KQ
will be close to identity. This results in a small geometric differ-
ence gCQ leading to classical ML models being competitive or
outperforming the quantum kernel method. In Supplementary
Section 9, we present a simple quantum model that requires an
exponential amount of samples to learn using the quantum kernel
Tr(ρ(xi)ρ(xj)), but only needs a linear number of samples to learn
using a classical ML model.
To circumvent this setback, we propose a family of projected
quantum kernels as a solution. These kernels work by projecting
the quantum states to an approximate classical representation,
e.g.,
using
reduced
physical
observables
or
classical
shadows25,27,42–44. Even if the training set space has a large
dimension d ~ N, the projection allows us to reduce to a low-
dimensional classical space that can generalize better. Further-
more, by going through the exponentially large quantum Hilbert
space, the projected quantum kernel can be challenging to
evaluate without a quantum computer. In numerical experiments,
we ﬁnd that the classical projection increases rather than
decreases the geometric difference with classical ML models.
These constructions will be the foundation of our best performing
quantum method later.
One of the simplest forms of projected quantum kernel is to
measure the one-particle reduced density matrix (1-RDM) on all
qubits for the encoded state, ρk(xi) = Trj≠k[ρ(xi)], then deﬁne the
kernel as



:
ð9Þ

kPQðxi; xjÞ ¼ exp γ ∑
k jjρkðxiÞ  ρkðxjÞjj2
F

This kernel deﬁnes a feature map function in the 1-RDM space

6
NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications

## Page 7

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9
ARTICLE

Fig. 3 Relation between dimension d, geometric difference g, and prediction performance. The shaded regions are the standard deviation over 10
independent runs and n is the number of qubits in the quantum encoding and dimension of the input for the classical encoding. a The approximate
dimension d and the geometric difference g with classical ML models for quantum kernel (Q) and projected quantum kernel (PQ) under different
embeddings and system sizes n. b Prediction error (lower is better) of the quantum kernel method (Q), projected quantum kernel method (PQ), and
classical ML models on classical (C) and quantum (Q) datasets with number of data N = 600. As d grows too large, the geometric difference g for
quantum kernel becomes small. We see that small geometric difference g always results in classical ML being competitive or outperforming the quantum
ML model. When g is large, there is a potential for improvement over classical ML. For example, projected quantum kernel improves upon the best classical
ML in Dataset (Q, E3).

Fig. 4 Prediction accuracy (higher the better) on engineered datasets. A label function is engineered to match the geometric difference g(C∣∣PQ)
between projected quantum kernel and classical approaches, demonstrating a signiﬁcant gap between quantum and the best classical models up to 30
qubits when g is large. We consider the best performing classical ML models among Gaussian SVM, linear SVM, Adaboost, random forest, neural
networks, and gradient boosting. We only report the accuracy of the quantum kernel method up to system size n = 28 due to the high simulation cost and
the inferior performance.

while the classical methods do not. The performance of the
classical ML model is especially strong on Dataset (Q, E1) and
Dataset (Q, E2). This elevation of the classical performance is
evidence of the power of data. Moreover, this intriguing behavior
and the lack of quantum advantage may be explained by
considering
the
effective
dimension
d
and
the geometric
difference g following our theoretical constructions. From Fig. 3a,
we can see that the dimension d of the original quantum state
space grows rather quickly, and the geometric difference g
becomes small as the dimension becomes too large (d ∝N) for the
standard quantum kernel. The saturation of the dimension
coincides with the decreasing and statistical ﬂuctuations in
performance
seen
in
Fig.
4.
Moreover,
given
poor
ML
performance a natural instinct is to throw more resources at
the problem, e.g., more qubits, but as demonstrated here, doing

this for naïve quantum kernel methods is likely to lead to tiny
inner products and even worse performance. In contrast, the
projected quantum space has a low dimension even when d
grows, and yields a higher geometric difference g for all
embeddings and system sizes. Our methodology predicts that,
when g is small, classical ML model will be competitive or
outperform the quantum ML model. This is veriﬁed in Fig. 3b for
both the original and projected quantum kernel, where a small
geometric difference g leads to a very good performance of
classical ML models and no large quantum advantage can be seen.
Only when the geometric difference g is large (projected kernel
method with embedding E3) can we see some mild advantage
over the best classical method. This result holds disregarding any
detail of the quantum evolution we are trying to learn, even for
ones that are hard to simulate classically.

NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications
7

## Page 8

ARTICLE
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9

In order to push the limits of separation between quantum and
classical approaches in a learning setting, we now consider a set of
engineered datasets with function values designed to saturate the
geometric inequality sC ≤gðKCjjKPQÞ
2sPQ between classical ML
models with associated kernels and the projected quantum kernel
method. In particular, we design the dataset such that sPQ = 1 and
sC ¼ gðKCjjKPQÞ
2. Recall from Eq. (3), this dataset will hence
show the largest separation in the prediction error bound
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
sðNÞ=N
p
. The engineered dataset is constructed via a simple
eigenvalue problem with the exact procedure described in
Supplementary Section 7 and the results are shown in Fig. 4.
As the quantum nature of the encoding increases from E1 to E3,
corresponding to increasing g, the performance of both the best
classical methods and the original quantum kernel decline
precipitously. The advantage of the projected quantum kernel
closely follows the geometric difference g and reaches more than
20% for large sizes. Despite the optimization of g only being
possible for classical methods with an associated kernel, the
performance advantage remains stable across other common
classical methods. Note that we also constructed engineered
datasets saturating the geometric inequality between classical ML
and the original quantum kernel, but the small geometric
difference g presented no empirical advantage at large system
size (see Supplementary Section 13).
In keeping with our arguments about the role of data, when we
increase the number of training data N, all methods improve, and
the advantage will gradually diminish. While this dataset is
engineered, it shows the strongest empirical separation on the
largest system size to date. We conjecture that this procedure
could be used with a quantum computer to create challenging
datasets that are easy to learn with a quantum device, hard to
learn classically, while still being easy to verify classically given
the correct labels. Moreover, the size of the margin implies that
this separation may even persist under moderate amounts of
noise in a quantum device.

local observables for very large numbers of qubits. Further
research will be required to ﬁnd use cases on datasets closer to
practical interest and evaluate potential claims of advantage, but
we believe the tools developed in this work will help to pave the
way for this exciting frontier.

Data availability
All other data that support the plots within this paper and other ﬁndings of this study are
available upon reasonable request. Source data are provided with this paper.

Code availability
A tutorial for reproducing smaller numerical experiments is available at https://www.
tensorﬂow.org/quantum/tutorials/quantum_data.

Received: 18 November 2020; Accepted: 16 March 2021;

References
1.
Halevy, A., Norvig, P. & Pereira, F. The unreasonable effectiveness of data.
IEEE Intell. Syst. 24, 8 (2009).
2.
Grover, L. K. A fast quantum mechanical algorithm for database search. in
Proc. twenty-eighth annual ACM symposium on Theory of computing (1996).
3.
Durr, C. & Hoyer, P. A quantum algorithm for ﬁnding the minimum. https://
arxiv.org/abs/quant-ph/9607014 (1996).
4.
Farhi, E. et al. A quantum adiabatic evolution algorithm applied to random
instances of an np-complete problem. Science 292, 472 (2001).
5.
Neven, H., Denchev, V. S., Rose, G. & Macready, W. G. Training a large scale
classiﬁer with the quantum adiabatic algorithm. https://arxiv.org/abs/
0912.0779 (2009).
6.
Rebentrost, P., Mohseni, M. & Lloyd, S. Quantum support vector machine for
big data classiﬁcation. Phys. Rev. Lett. 113, 130503 (2014).
7.
Leifer, M. S. & Poulin, D. Quantum graphical models and belief propagation.
Ann. Phys. 323, 1899 (2008).
8.
Aaronson, S. & Ambainis, A. The need for structure in quantum speedups.
https://arxiv.org/abs/0911.0996 (2009).
9.
McClean, J. R. et al. Low depth mechanisms for quantum optimization. https://
arxiv.org/abs/2008.08615 (2020).
10. Boixo, S. et al. Characterizing quantum supremacy in near-term devices. Nat.
Phys. 14, 595 (2018).
11. Arute, F. et al. Quantum supremacy using a programmable superconducting
processor. Nature 574, 505 (2019).
12. Peruzzo, A. et al. A variational eigenvalue solver on a photonic quantum
processor. Nat. Commun. 5, 4213 (2014).
13. McClean, J. R., Romero, J., Babbush, R. & Aspuru-Guzik, A. The theory
of variational hybrid quantum-classical algorithms. N. J. Phys. 18, 023023
(2016).
14. Farhi, E. & Neven, H. Classiﬁcation with quantum neural networks on near
term processors. arXiv preprint arXiv:1802.06002 https://arxiv.org/abs/
1802.06002 (2018).
15. Havlíček, V. et al. Supervised learning with quantum-enhanced feature spaces.
Nature 567, 209 (2019).
16. Cortes, C. & Vapnik, V. Support-vector networks. Mach. Learn. 20, 273
(1995).
17. Schölkopf, B. et al. Learning with kernels: support vector machines,
regularization, optimization, and beyond. https://mitpress.mit.edu/books/
learning-kernels (2002).
18. Mohri, M., Rostamizadeh, A. & Talwalkar, A. Foundations of machine
learning. https://mitpress.mit.edu/books/foundations-machine-learning-
second-edition (2018).
19. Jacot, A., Gabriel, F. & Hongler, C. Neural tangent kernel: Convergence and
generalization in neural networks. NIPS’18: Proceedings of the 32nd
International Conference on Neural Information Processing Systems https://dl.
acm.org/doi/abs/10.5555/3327757.3327948 pp. 8580–8589 (2018).
20. Novak, R. et al. Neural tangents: Fast and easy inﬁnite neural networks in
python. arXiv preprint arXiv:1912.02803 https://openreview.net/pdf?
id=SklD9yrFPS (2019).
21. Arora, S. et al. On exact computation with an inﬁnitely wide neural net. in
Advances in Neural Information Processing Systems (2019).
22. Blank, C., Park, D. K., Rhee, J.-K. K. & Petruccione, F. Quantum classiﬁer with
tailored quantum kernel. npj Quantum Inf. 6, 1 (2020).
23. Bartkiewicz, K. Experimental kernel-based quantum machine learning in ﬁnite
feature space. Sci. Rep. 10, 1 (2020).

Discussion
The use of quantum computing in machine learning remains an
exciting prospect, but quantifying quantum advantage for such
applications has some subtle issues that one must approach
carefully. Here, we constructed a foundation for understanding
opportunities for quantum advantage in a learning setting. We
showed quantitatively how classical ML algorithms with data can
become computationally more powerful, and a prediction
advantage for quantum models is not guaranteed even if the data
come from a quantum process that is challenging to indepen-
dently simulate. Motivated by these tests, we introduced projected
quantum kernels. On engineered datasets, projected quantum
kernels outperform all tested classical models in prediction error.
To the authors’ knowledge, this is the ﬁrst empirical demon-
stration of such a large separation between quantum and classical
ML models.
This work suggests a simple guidebook for generating ML
problems which give a large separation between quantum and
classical models, even at a modest number of qubits. The size of
this separation and trend up to 30 qubits suggests the existence of
learning tasks that may be easy to verify, but hard to model
classically, requiring just a modest number of qubits and allowing
for device noise. Claims of true advantage in a quantum machine
learning setting require not only benchmarking classical machine
learning models, but also classical approximations of quantum
models. Additional work will be needed to identify embeddings
that satisfy the sometimes conﬂicting requirements of being hard
to approximate classically and exhibiting meaningful signal on

8
NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications

## Page 9

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-021-22539-9
ARTICLE

24. Liu, Y., Arunachalam, S. & Temme, K. A rigorous and robust quantum speed-
up in supervised machine learning. arXiv preprint arXiv:2010.02174 https://
arxiv.org/abs/2010.02174 (2020).
25. Huang, H.-Y., Kueng, R. & Preskill, J. Predicting many properties of a
quantum system from very few measurements. Nat. Phys. https://doi.org/
10.1038/s41567-020-0932-7 (2020).
26. Cotler, J. & Wilczek, F. Quantum overlapping tomography. Phys. Rev. Lett.
124, 100401 (2020).
27. Paini, M. and Kalev, A. An approximate description of quantum states. arXiv
preprint arXiv:1910.10543 https://arxiv.org/abs/1910.10543 (2019).
28. Lloyd, S., Schuld, M., Ijaz, A., Izaac, J. & Killoran, N. Quantum embeddings
for machine learning. arXiv preprint arXiv:2001.03622 https://arxiv.org/abs/
2008.08605 (2020).
29. Schuld, M., Sweke, R. & Meyer, J. J. The effect of data encoding on the expressive
power of variational quantum machine learning models. Phys. Rev. A 103,
032430 (2021).
30. McClean, J. R., Boixo, S., Smelyanskiy, V. N., Babbush, R. & Neven, H. Barren
plateaus in quantum neural network training landscapes. Nat. Commun. 9, 1
(2018).
31. Grant, E., Wossnig, L., Ostaszewski, M. & Benedetti, M. An initialization
strategy for addressing barren plateaus in parametrized quantum circuits.
Quantum 3, 214 (2019).
32. Schuld, M., Bocharov, A., Svore, K. M. & Wiebe, N. Circuit-centric quantum
classiﬁers. Phys. Rev. A 101, 032308 (2020b).
33. LaRose, R. & Coyle, B. Robust data encodings for quantum classiﬁers. Phys.
Rev. A 102, 032420 (2020).
34. Harrow, A. W. & Montanaro, A. Quantum computational supremacy. Nature
549, 203 (2017).
35. Li, Z. et al. Enhanced convolutional neural tangent kernels. arXiv preprint
arXiv:1911.00809 https://arxiv.org/abs/1911.00809 (2019).
36. Micchelli, C. A., Xu, Y. & Zhang, H. Universal kernels. J. Mach. Learn. Res. 7,
2651 (2006).
37. Krogh, A. & Hertz, J. A. A simple weight decay can improve generalization.
Adv. Neural Inf. Process. Syst. 950–957 (1992).
38. Suykens, J. A. & Vandewalle, J. Least squares support vector machine
classiﬁers. Neural Process. Lett. 9, 293 (1999).
39. Huang, H.-Y., Kueng, R. & Preskill, J. Information-theoretic bounds on
quantum advantage in machine learning. arXiv preprint arXiv:2101.02464
https://arxiv.org/abs/2101.02464 (2021).
40. Anderson, E. et al. LAPACK Users’ Guide, 3rd edn. (Society for Industrial and
Applied Mathematics, 1999).
41. Breiman, L. Random forests. Mach. Learn. 45, 5 (2001).
42. Gosset, D. & Smolin, J. A compressed classical description of quantum
states. arXiv preprint arXiv:1801.05721 https://arxiv.org/abs/1801.05721
(2018).
43. Aaronson, S. Shadow tomography of quantum states. SIAM J. Comput. https://
dl.acm.org/doi/abs/10.1145/3188745.3188802 (2020).
44. Aaronson, S. and Rothblum, G. N. Gentle measurement of quantum states and
differential privacy. in Proc. 51st Annual ACM SIGACT Symposium on Theory
of Computing (2019).
45. Hohenberg, P. & Kohn, W. Inhomogeneous electron gas. Phys. Rev. 136, B864
(1964).
46. Runge, E. & Gross, E. K. Density-functional theory for time-dependent
systems. Phys. Rev. Lett. 52, 997 (1984).
47. Broughton, M. et al. Tensorﬂow quantum: A software framework for quantum
machine learning. arXiv preprint arXiv:2003.02989 https://arxiv.org/abs/
2003.02989 (2020).

48. Xiao, H., Rasul, K. & Vollgraf, R. Fashion-mnist: a novel image dataset for
benchmarking machine learning algorithms. arXiv preprint arXiv:1708.07747
https://arxiv.org/abs/1708.07747 (2017).
49. LeCun, Y., Cortes, C. & Burges, C. Mnist handwritten digit database. http://
yann.lecun.com/exdb/mnist (2010).
50. Jolliffe, I. T. in Principal component analysis 129–155 (Springer, 1986).
51. Schuld, M. & Killoran, N. Quantum machine learning in feature hilbert
spaces. Phys. Rev. Lett. 122, 040504 (2019).
52. Skolik, A., McClean, J. R., Mohseni, M., van der Smagt, P. & Leib, M.
Layerwise learning for quantum neural networks. Quantum Machine
Intelligence 3, 5 (2021).

Acknowledgements
We want to thank Richard Kueng, John Platt, John Preskill, Thomas Vidick, Nathan
Wiebe, and Chun-Ju Wu for valuable inputs and inspiring discussions. We thank Bálint
Pató for crucial contributions in setting up simulations.

Author contributions
H.H. and J.M. developed the theoretical aspects of this work. H.H. and M.B. conducted
the numerical experiments and wrote the open source code. H.H., M.M., R.B., S.B., H.N.,
and J.M. contributed to technical discussions and writing of the manuscript.

Competing interests
The authors declare no competing interests.

Additional information
Supplementary information The online version contains supplementary material
available at https://doi.org/10.1038/s41467-021-22539-9.

Correspondence and requests for materials should be addressed to J.R.M.

Peer review information Nature Communications thanks Nana Liu and the other,
anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional afﬁliations.

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long as you give
appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons license, and indicate if changes were made. The images or other third party
material in this article are included in the article’s Creative Commons license, unless
indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons license and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly from
the copyright holder. To view a copy of this license, visit http://creativecommons.org/
licenses/by/4.0/.

© The Author(s) 2021

NATURE COMMUNICATIONS | (2021) 12:2631 | https://doi.org/10.1038/s41467-021-22539-9 | www.nature.com/naturecommunications
9
