---
source_pdf: ../arxiv_1808.10402.pdf
pages: 59
extracted_at: 2026-04-17T12:32:35+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_1808.10402

Source PDF: ../arxiv_1808.10402.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Quantum computational chemistry

Sam McArdle,1, ∗Suguru Endo,1 Al´an Aspuru-Guzik,2, 3, 4 Simon C. Benjamin,1 and Xiao Yuan1, †

1Department of Materials,
University of Oxford,
Parks Road, Oxford OX1 3PH,
United Kingdom
2Department of Chemistry and Department of Computer Science,
University of Toronto,
Toronto, Ontario M5S 3H6,
Canada
3Vector Institute for Artiﬁcial Intelligence,
Toronto, Ontario M5S 1M1,
Canada
4Canadian Institute for Advanced Research (CIFAR) Senior Fellow,
Toronto, Ontario M5S 1M1,
Canada

arXiv:1808.10402v3 [quant-ph] 27 Jan 2020

(Dated: January 28, 2020)

One of the most promising suggested applications of quantum computing is solving
classically intractable chemistry problems. This may help to answer unresolved ques-
tions about phenomena like: high temperature superconductivity, solid-state physics,
transition metal catalysis, or certain biochemical reactions. In turn, this increased un-
derstanding may help us to reﬁne, and perhaps even one day design, new compounds
of scientiﬁc and industrial importance. However, building a suﬃciently large quantum
computer will be a diﬃcult scientiﬁc challenge. As a result, developments that enable
these problems to be tackled with fewer quantum resources should be considered very
important. Driven by this potential utility, quantum computational chemistry is rapidly
emerging as an interdisciplinary ﬁeld requiring knowledge of both quantum computing
and computational chemistry.
This review provides a comprehensive introduction to
both computational chemistry and quantum computing, bridging the current knowl-
edge gap. We review the major developments in this area, with a particular focus on
near-term quantum computation. Illustrations of key methods are provided, explicitly
demonstrating how to map chemical problems onto a quantum computer, and solve
them. We conclude with an outlook for this nascent ﬁeld.

CONTENTS

I. Introduction
2

II. Quantum computing and simulation
4
A. Quantum computing
4
B. Quantum simulation
6

III. Classical computational chemistry
8
A. The electronic structure problem
9
1. Chemical systems of interest
9
B. First and Second quantisation
10
1. First quantisation
11
a. Grid based methods
11
b. Basis set methods
11
2. Second quantisation
12
a. Basis set methods
12
b. Grid based methods
13
C. Classical computation methods
13
1. Hartree–Fock
14
2. Multiconﬁgurational self-consistent ﬁeld
15
3. Conﬁguration interaction
15
4. Coupled cluster
16
D. Chemical basis sets
17

∗sam.mcardle.science@gmail.com
† xiao.yuan.ph@gmail.com

1. STO-nG and split-valence basis sets
17
2. Correlation-consistent basis sets
18
3. Plane wave basis sets
18
E. Reduction of orbitals
19

IV. Quantum computational chemistry mappings
19
A. First quantised encoding methods
20
1. Grid based methods
20
2. Basis set methods
21
B. Second quantised basis set encoding methods
22
1. Jordan-Wigner encoding
22
2. Bravyi–Kitaev encoding
23
3. Locality preserving mappings
24
C. Resource reduction
24
1. Hamiltonian reduction
24
2. Low rank decomposition techniques
25

V. Quantum computational chemistry algorithms
25
A. Quantum phase estimation
25
1. Implementation
25
2. State preparation
27
3. Hamiltonian simulation
27
a. Product formulae
28
b. Advanced Hamiltonian simulation methods
28
4. Phase estimation for chemistry simulation
28
a. Gaussian orbital basis sets
29
b. Plane wave basis sets
29
c. Fermi-Hubbard model
30
d. Grid based methods
30
5. Outstanding problems
31

## Page 2

Song et al., 2019, 2017), and photonic systems (Chen
et al., 2017; Wang et al., 2016; Zhong et al., 2018). It is
believed that using quantum systems as our simulation
platform will enable us to tackle classically intractable
problems in chemistry, physics, and materials science.
Classical computational methods have become an im-
portant investigative tool in areas like transition metal
catalysis (Vogiatzis et al., 2019) and high temperature
superconductivity (Dagotto, 1994).
Classical simula-
tions enable us to rationalise experimental results, test
physical models,
and understand system properties.
However, their ability to guide design is often precluded
by the computational complexity of realistic models.
As quantum computers are able to eﬃciently simulate
quantum systems, it is believed that they will enable a
more accurate understanding of the models in use today,
as well as the ability to simulate more complex (and
therefore, more realistic) models. This may lead to an
increased understanding which we can leverage to make
advances in areas as diverse as chemistry (Aspuru-Guzik
et al., 2018), biology (Reiher et al., 2017), medicine
(Cao et al., 2018), and materials science (Babbush et al.,
2018c).
It has even been speculated that as quantum
hardware develops, quantum simulation may one day
progress from being accurate enough to conﬁrm the
results of experiments, to being more accurate than
the experiments themselves.
Quantum simulations of
such high precision may in turn enable the design of
new, useful compounds.
However, we stress that to
achieve this ultimate goal we would need considerable
further developments – both in the technology required
to build such as powerful quantum computer, and the
theory behind an appropriate algorithm and model.
This can be likened to the aerospace industry, where
computational ﬂuid dynamics calculations on classical
computers have replaced wind tunnel testing in many
stages of wing design (Jameson, 1999).
However, for
the most demanding parts of aerospace design, neither
our largest classical computers, nor the physical models
considered,
are yet powerful enough to completely
replace experimental testing (Malik and Bushnell, 2012).
Instead, the two methods work together in synergy, to
enable increased understanding, with greater eﬃciency.

B. Variational algorithms
31
1. Ans¨atze
32
a. Hardware eﬃcient ans¨atze
33
b. Chemically inspired ans¨atze
33
c. Hamiltonian variational ansatz
34
2. Measurement
34
3. Classical optimisation
35
a. Previous optimisation studies
35
b. Related methods of optimisation
36
C. Evaluation of excited states
36
1. Quantum subspace expansion
37
2. Overlap-based methods
38
3. Contraction VQE methods
38

VI. Error mitigation for chemistry
38
A. Extrapolation
39
B. Probabilistic error cancellation
39
C. Quantum subspace expansion
40
D. Symmetry based methods
41
E. Other methods of error mitigation
41

VII. Illustrative examples
41
A. Hydrogen
41
1. STO-3G basis
42
2. 6-31G basis
43
3. cc-PVDZ basis
44
B. Lithium Hydride STO-3G basis
44

VIII. Discussion and Conclusions
46
A. Classical limits
46
B. Quantum resources: medium to long-term
48
C. Quantum resources: near to medium-term
49
D. Summary and outlook
51

Acknowledgments
51

References
52

I. INTRODUCTION

Quantum mechanics underpins all of modern chem-
istry.
One might therefore imagine that we could use
this theory to predict the behaviour of any chemical com-
pound. This is not the case. As Dirac noted; “The ex-
act application of these laws leads to equations much too
complicated to be soluble.” (Dirac, 1929). The problem
described by Dirac is that the complexity of the wave-
function of a quantum system grows exponentially with
the number of particles.
This leaves classical comput-
ers unable to exactly simulate quantum systems in an
eﬃcient way. Feynman proposed a solution to this prob-
lem; using quantum hardware as the simulation platform,
remarking that “If you want to make a simulation of na-
ture, you’d better make it quantum mechanical, and by
golly it’s a wonderful problem, because it doesn’t look so
easy.” (Feynman, 1982).

To date, several eﬃcient quantum algorithms have
been proposed to solve problems in chemistry.
The
runtime and physical resources required by these algo-
rithms are expected to scale polynomially with both the
size of the system simulated and the accuracy required.
Experimental developments have accompanied these
theoretical milestones, with many groups demonstrating
proof of principle chemistry calculations.
However,
limited by hardware capabilities,
these experiments
focus only on small chemical systems that we are already
able to simulate classically. Moreover, the gate counts
currently estimated for transformative chemistry simula-

Although developing small quantum computers has
taken over 30 years, we may soon be in a position to
test Feynman’s proposal, following recent developments
in quantum hardware including ion traps (Ballance
et al., 2016; Gaebler et al., 2016; Harty et al., 2014;
Monz et al., 2011), superconducting systems (Arute
et al., 2019; Barends et al., 2014; Chow et al., 2012;

## Page 3

tions likely signal the need for quantum error correction,
which requires orders of magnitude more qubits, and
lower error rates, than are currently available (Babbush
et al., 2018b; Kivlichan et al., 2019a; Mueck, 2015).
Despite ongoing experimental eﬀorts, no group has yet
demonstrated a single fully error corrected qubit. Even if
the signiﬁcant hardware challenges to build an error cor-
rected quantum computer can be overcome (Gambetta
et al., 2017; Ladd et al., 2010; Monroe and Kim, 2013),
new theoretical developments may be needed to solve
classically intractable chemistry problems on a quantum
computer that we could realistically imagine building in
the next few decades, such as probing biological nitrogen
ﬁxation, or investigating new metal ion battery designs.
These breakthroughs may be achieved by connecting
researchers working in quantum computing with those
working in computational chemistry.
We seek to aid
this connection with this succinct, yet comprehensive,
review of quantum computational chemistry (using
quantum algorithms, run on quantum computers, to
solve problems in computational chemistry) and its
foundational ﬁelds.

Although quantum algorithms can solve a range of
problems in chemistry, we focus predominantly on the
problem of ﬁnding the low lying energy levels of chem-
ical systems. This is known as ‘the electronic structure
problem’.
There are three reasons for this restriction
of scope. Primarily, this problem is a fundamental one
in classical computational chemistry. Knowledge of the
energy eigenstates enables the prediction of reaction
rates, location of stable structures, and determination of
optical properties (Helgaker et al., 2012). Secondly, the
machinery developed to solve this problem on quantum
computers is easily applied to other types of problems,
such as ﬁnding transition states, or understanding the
vibrational structure of molecules. Finally, most of the
prior work in quantum computational chemistry has
focused on this problem. As such, it provides an ideal
context in which to explain the most important details
of quantum computational chemistry.

This review is organised as follows. We ﬁrst provide a
brief overview of quantum computing and simulation in
Sec. II. We then introduce the key methods and terminol-
ogy used in classical computational chemistry in Sec. III.
The methods developed to merge these two ﬁelds, includ-
ing mapping chemistry problems onto a quantum com-
puter, are described in Sec. IV. We continue our discus-
sion of quantum computational chemistry in Sec. V by
describing algorithms for ﬁnding the ground and excited
states of chemical systems. Sec. VI highlights the tech-
niques developed to mitigate the eﬀects of noise in non-
error corrected quantum computers, which will be crucial
for achieving accurate simulations in the near-future.
In Sec. VII we provide several examples of how to

map chemistry problems onto a quantum computer.
We discuss techniques that can be used to reduce
the simulation resources required, and the quantum
circuits that can be used. This section seeks to illustrate
the techniques described throughout the rest of the
review, providing worked examples for the reader. We
conclude this review in Sec. VIII with a comparison
between classical and quantum techniques, and resource
estimations for the diﬀerent quantum methods.
This
section aims to help the reader to understand when, and
how, quantum computational chemistry may surpass its
classical counterpart.

A handful of related reviews on this topic exist in
the literature.
Summaries of early theoretical and
experimental work in quantum computational chemistry
were carried out by Kassal et al. (2011) and Lu et al.
(2012). More focused discussions of quantum algorithms
introduced for chemistry simulation before 2015, and the
computational complexity of problems in chemistry can
be found in works by Kais et al. (2014); Veis and Pittner
(2012); and Yung et al. (2012). A comprehensive review
was recently released by Cao et al. (2019). Said review,
and our own, are complementary; the review of Cao
et al. (2019) is well suited to experienced practitioners
of classical electronic structure theory, and provides
excellent detail on the computational complexity of
quantum simulations,
and how they asymptotically
compare to cutting edge methods in classical chemistry.
Our review provides a more practical guide to the
ﬁeld (especially for those new to electronic structure
theory), showing explicitly how the workhorse methods
of classical chemistry have been translated to work
on quantum computers, and describing techniques to
facilitate
experimental
demonstrations
of
quantum
chemistry algorithms, such as resource reduction and
error mitigation.
Together, these reviews provide a
complete overview of the progress to date in quantum
computational chemistry.

Despite being a relatively young ﬁeld,
quantum
computational chemistry has grown extremely rapidly,
and has already evolved beyond the stage that it can
be fully described by a single review.
As such, there
are approaches to solving chemistry problems with a
quantum computer which we are not able to describe
fully in this review. As stated above, we have chosen to
prioritise the canonical topics in the ﬁeld: using either
near-term, or further-future digital quantum computers
to solve the electronic structure problem ab initio.
We have focused on the most promising methods for
solving this problem: variational algorithms with error
mitigation, and the quantum phase estimation algorithm
with quantum error correction. Extended discussion is
reserved for methods which are key to understanding
how quantum computers can be used to solve general

## Page 4

chemistry problems, or articles which have made im-
portant observations on ways to make these simulations
more tractable. It is beyond the scope of this review to
summarise work in directions complementary to these,
such as: quantum machine learning based approaches to
the electronic structure problem (Xia et al., 2018; Xia
and Kais, 2018), using quantum computers as part of a
problem decomposition approach to simulation (Bauer
et al., 2016; Dallaire-Demers and Wilhelm, 2016a,b;
Keen et al., 2019; Kreula et al., 2016; Rubin, 2016;
Rungger et al., 2019), hybrid quantum algorithms for
density functional theory (Hatcher et al., 2019; Whitﬁeld
et al., 2014), relativistic quantum chemistry (Senjean,
2019; Veis et al., 2012), gate based methods for sim-
ulating molecular vibrations (McArdle et al., 2018b;
Sawaya and Huh, 2018; Sawaya et al., 2019), analog
simulators of molecular vibrations (Chin and Huh, 2018;
Clements et al., 2017; Hu et al., 2018a; Huh et al., 2015;
Huh and Yung, 2017; Joshi et al., 2014; Shen et al.,
2018; Sparrow et al., 2018; Wang et al., 2019), fermionic
quantum computation for chemistry simulation (O’Brien
et al., 2018b), quantum methods for electron-phonon
systems (Macridin et al., 2018a,b; Wu et al., 2002),
protein folding and molecular docking (Babbush et al.,
2012; Babej et al., 2018; Banchi et al., 2019; Fingerhuth
et al., 2018; Lu and Li, 2019; Perdomo et al., 2008;
Perdomo-Ortiz et al., 2012; Robert et al., 2019), solving
problems in chemistry using a quantum annealer (Bab-
bush et al., 2014; Genin et al., 2019; Teplukhin et al.,
2018; Xia et al., 2018), and quantum algorithms for
ﬁnding the eigenvalues of non-hermitian Hamiltoni-
ans (Daskin et al., 2014; Wang et al., 2010).

II. QUANTUM COMPUTING AND SIMULATION

In this section, we introduce the basic elements of
quantum computing and quantum simulation.
We re-
fer the reader to the works of Georgescu et al. (2014)
and Nielsen and Chuang (2002) for more detailed intro-
ductions.

A. Quantum computing

In this review, we focus on the qubit-based circuit
model of quantum computation (Nielsen and Chuang,
2002). Other paradigms that vary to a greater or lesser
extent include: adiabatic quantum computing (Aharonov
et al., 2008; Albash and Lidar, 2018; Farhi et al.,
2000), one-way or measurement based quantum com-
puting (Jozsa, 2005; Raussendorf and Briegel, 2001;
Raussendorf et al., 2003), and continuous-variable quan-
tum computing (Braunstein and van Loock, 2005; Lloyd
and Braunstein, 1999).

The canonical circuit model of quantum computation
is so-named because of its resemblance to the logic cir-
cuits used in classical computing. In the classical circuit
model, logic gates (such as AND, OR and NOT) act on
bits of information. In the quantum case, quantum gates
are acted upon the basic unit of information, the qubit.
The qubit lives in a two-dimensional Hilbert space. The
basis vectors of the space are denoted as {|0⟩, |1⟩}, which
are referred to as the computational basis states,









1

0

|0⟩=

,
|1⟩=

.
(1)

0

1

A general single qubit state is described by





α

|ϕ⟩= α |0⟩+ β |1⟩=

,
(2)

β

α, β ∈C,

|α|2 + |β|2 = 1.

When quantum logic gates act on the qubits, they ma-
nipulate both basis state vectors at the same time, pro-
viding (measurement limited) parallelism. Although the
qubit is in a quantum superposition during the algorithm,
when it is measured in the computational basis, it will
be found in state |0⟩or state |1⟩, not in a superposition.
These measurement outcomes occur with probability |α|2

and |β|2, respectively. For now, we will treat the qubit
as an abstract two level system, before later elaborating
on how they can be physically realised.
If there are n qubits in the system, the state is de-
scribed by a vector in the 2n dimensional Hilbert space
formed by taking the tensor product of the Hilbert spaces
of the individual qubits. States can be classiﬁed as either
‘product’ or ‘entangled’. Product states can be decom-
posed into tensor products of fewer qubit wavefunctions,
such as

1
√

2(|00⟩+ |01⟩) = |0⟩⊗1
√

2(|0⟩+ |1⟩).
(3)

Entangled states cannot be decomposed into tensor prod-
ucts, such as the state

1
√

2(|00⟩+ |11⟩).
(4)

In this review, we refer to the leftmost qubit in a vector
as the (n −1)th qubit, and the rightmost qubit as the
zeroth qubit. This choice enables us to write numbers
in binary using computational basis states. For example,
we can write |7⟩= |1⟩|1⟩|1⟩= |111⟩. We can then place
a quantum register of n qubits in a superposition of the
2n possible numbers that can be represented by n bits.
This is typically written as P2n−1
x=0 cx |x⟩.

## Page 5

A quantum circuit consists of a number of single and
two qubit gates acting on the qubits.
The qubits are
initialised in a well deﬁned state, such as the |¯0⟩state
(|¯0⟩= |0⟩⊗n = |0⟩⊗|0⟩⊗· · · ⊗|0⟩). A quantum cir-
cuit generally concludes with measurements to extract
information. It may also employ additional intermediate
measurements, for example, to check for errors. From a
mathematical perspective, the gates are unitary matri-
ces. Typical gates include the Pauli gates













0 −i

0 1

1
0

X =

,
Y =

,
Z =

,
(5)

0 −1

1 0

i
0

the single qubit rotation gates

Rx(θ) = e( −iθX

2
), Ry(θ) = e( −iθY

2
), Rz(θ) = e( −iθZ

2
)

(6)

the Hadamard and T gates









1
1

1
0

Had =
1
√

,
T =

,
(7)

2

0 eiπ/4

1 −1

and multi-qubit entangling gates, such as the two qubit
controlled-NOT (CNOT) gate shown in Fig. 1. The ac-

FIG. 1 The controlled-NOT (CNOT) gate. ‘•’ denotes the
control qubit and ‘⊕’ denotes the target qubit.

tion of the CNOT gate can be written mathematically
as

|0⟩⟨0|C ⊗IT + |1⟩⟨1|C ⊗XT ,
(8)

where T denotes the target qubit, and C denotes the
control qubit. The matrix form of this operation is given
by




1 0 0 0

















0 1 0 0

.
(9)

0 0 0 1

0 0 1 0

These gates are used to create an example quantum
circuit in Fig. 2.
This circuit generates the entangled
state of 2 qubits given by Eq. (4), and then measures
both of the qubits.
With only single qubit operations and CNOT gates, it
is possible to approximate an arbitrary multi-qubit gate
to any desired accuracy (DiVincenzo, 1995). As a result,
the circuit model of quantum computing typically decom-
poses all algorithms into single and two qubit gates. We

|0⟩

FIG. 2 A quantum circuit that generates the entangled state
(|00⟩+ |11⟩)/
√

2 and measures each qubit in the computa-
tional basis. Time runs from left to right. Here, Had is the
Hadamard gate, deﬁned in the main text. When measured,
the qubits will either both be in the state 0 (|00⟩), or both 1
(|11⟩). Each of these two outcomes occurs with 50 % proba-
bility.

denote each gate by a unitary operator U i,j(⃗θ), where i, j
are the indices of the qubits the gates act on (i = j for
single qubit operations), and ⃗θ are gate parameters (al-
though the gates do not have to be parametrized, such as
the Pauli gates). We can then mathematically describe
a quantum circuit by

k
U ik,jk
k
(⃗θk) |¯0⟩,
(10)

|ϕ⟩=
Y

where k denotes the kth gate in the circuit. The gates are
ordered right to left. For example, the circuit in Fig. 2
would be written as

1
√

2(|00⟩+ |11⟩) = CNOT0,1Had0 |00⟩.
(11)

We extract information from the circuits by performing
measurements of observables, O, which are represented
by Hermitian matrices. Typically, we seek the average
value over many measurements, ¯O, given by

¯O = ⟨ϕ| O |ϕ⟩,
(12)

referred to as the expectation value of the operator O.
Measuring the expectation value of qubit i in the com-
putational basis corresponds to ⟨ϕ| Zi |ϕ⟩. In practice,
this means that we repeatedly prepare the state |ϕ⟩, and
measure the state of qubit i, labelling the outcomes +1
(for |0⟩) and −1 (for |1⟩). We then take the mean of these
measurement outcomes. In order to measure qubits in
the X or Y basis, single qubit rotations are ﬁrst applied
to change the basis of the relevant qubits, which are then
measured in the Z basis. We can obtain the outcomes of
measuring multi-qubit operators by taking the product
of the measurement outcomes of single qubit operators
measured in the same circuit iteration. For example, the
expectation value of ZiZj could be obtained by prepar-
ing state |ϕ⟩, measuring Zi on qubit i and Zj on qubit j,
multiplying these two measurement outcomes together,
and averaging the results over many repetitions of this
process. These outcomes are typically correlated for en-
tangled states. For example, the measurement outcome
for Z1Z0 on the state in Eq. (4) is always +1 (+1 × +1
for |00⟩and −1 × −1 for |11⟩).

## Page 6

The Pauli operators and identity matrix, multiplied
by real coeﬃcients, form a complete basis for any
Hermitian single or multi-qubit operator. Therefore any
multi-qubit observable can be expanded into strings of
Pauli operators, the expectation values of which we can
measure eﬃciently with a quantum computer.

manner (Campbell et al., 2017; Fowler et al., 2012a;
O’Gorman and Campbell, 2017).
For example, if we
consider using a quantum computer to factor numbers
in polynomial time (Shor, 1994), current estimates (at
time of writing) suggest that we would require around
20 million physical qubits to factor a number that is too
large to tackle using known classical algorithms (Gidney
and Eker, 2019).
Building a machine of this size will
be extremely diﬃcult, in terms of isolating the qubits
from
the
environment,
developing
scalable
control
systems, and minimising qubit crosstalk, as discussed
by Gambetta et al. (2017) and Ladd et al. (2010). We
will discuss the comparably lower resources required for
error corrected chemistry calculations in Sec. VIII.B.

It is important to distinguish between the number
of physical and logical qubits in a quantum computer.
Physical qubits are approximate two-level systems, which
can be created in a range of diﬀerent systems, including,
but not limited to: energy levels in trapped ions (Cirac
and Zoller, 1995; Leibfried et al., 2003), polarization
states of photons (Knill et al., 2001), spins in quantum
dots (Hanson et al., 2007; Loss and DiVincenzo, 1998)
or silicon (Kane, 1998), and energy levels of supercon-
ducting circuit resonators (Nakamura et al., 1999; Shnir-
man et al., 1997; Wendin, 2017). In order to protect our
qubits from decoherence caused by coupling to the envi-
ronment (Landauer, 1995; Unruh, 1995), we can encode
m logical qubits into n > m physical qubits. These log-
ical qubits can simply be thought of as the abstract two
level system described by Eq. (2).
The codes used to
construct logical qubits are analogous to classical error
correcting codes, but are in general more complex, due
to the delicate nature of quantum information and the
‘no-cloning theorem’ of quantum mechanics. Depending
on the code used, we can either detect, or detect and
correct the errors which occur. The number of errors we
can detect and/or correct depends on the code used (it
is related to the distance of the code). We must also ac-
count for the fact that the error checking measurements
and correction procedure can cause additional errors to
occur (Knill et al., 1996). We seek to build circuits in
a ‘fault tolerant’ (Aharonov and Ben-Or, 1997; Gottes-
man, 1998; Shor, 1996) manner, which limits the spread
of errors during logical blocks of the computation. If this
is achieved, then it is possible to scale up computations
arbitrarily. If the physical error rate in the gates is be-
low a certain (code-dependent) threshold value, the error
rate in the logical operations can be made arbitrarily low,
either by concatenation, or for certain codes, by growing
the code. A more detailed discussion of error correction
is given by Devitt et al. (2013); Lidar and Brun (2013);
Raussendorf (2012); and Terhal (2015).
One of the most widely studied error correction codes
is the surface code (Kitaev, 1997), which is particularly
suitable for 2D grids of qubits with nearest-neighbour
connectivity. Physical error rates below the surface code
threshold of around 1 % (Fowler et al., 2012b; Stephens,
2014; Wang et al., 2011) have been achieved for trapped
ion (Ballance et al., 2016; Gaebler et al., 2016) and
superconducting (Arute et al., 2019; Barends et al.,
2014) qubits. However, with these error rates, we would
require around 103 −104 physical qubits per logical
qubit to perform interesting tasks in a fault-tolerant

In contrast to the large error corrected machines de-
scribed above, current quantum computers possess only
tens of error-prone physical qubits. Nevertheless, quan-
tum computers with more than around 50 qubits are
considered too large to exactly simulate classically, and
may thus be capable of solving problems which are
intractable on even the largest classical supercomput-
ers (Arute et al., 2019).
However, these problems are
typically artiﬁcially constructed examples, rather than
real-world problems (Boixo et al., 2018; Harrow and Mon-
tanaro, 2017).
Preskill (2018) dubbed these machines
‘noisy intermediate-scale quantum’ (NISQ) devices, and
observed that it is currently unclear whether they will be
able to outperform classical computers on useful tasks.
The dichotomy between the resources needed for tackling
problems like factoring, and the ‘supremacy’ of a machine
with more than around 50 qubits poses the question;
‘What, if anything, will near-term quantum computers be
useful for?’. The answer may lie with Feynman’s original
proposal; using quantum systems to simulate quantum
systems.

B. Quantum simulation

In this review, we focus on the digital quantum
simulation of many-body quantum systems.
Digital
quantum simulation maps the target problem onto a
set of gates which can be implemented by a quantum
computer.
A universal quantum computer can be
programmed to perform many diﬀerent simulations.
This can be contrasted with analog quantum simulation,
where the simulator emulates a speciﬁc real system
of interest.
However, analog simulators are generally
considered more robust to noise, and therefore easier to
construct (Georgescu et al., 2014). To date, there have
been several proposals for the simulation of chemistry
using analog simulators (Arg¨uello-Luengo et al., 2018;
Chin and Huh, 2018; Huh et al., 2015; Huh and Yung,
2017; Torrontegui et al., 2011), some of which have been
experimentally realised (Clements et al., 2017; Hu et al.,

## Page 7

2018b; Shen et al., 2018; Smirnov et al., 2007; Sparrow
et al., 2018).
Nevertheless, to perform accurate simu-
lations of large chemical systems, we will likely require
digital quantum simulation, as it is not yet clear how
to protect large analog simulations from errors. Digital
quantum simulation is more vulnerable to noise and
device imperfections than analog simulation. While such
imperfections can be addressed via error correction, this
requires additional qubits and places stringent require-
ments on gate ﬁdelities. In this review we focus solely
on digital quantum simulation of chemistry problems.
We refer the reader to the works of Aspuru-Guzik and
Walther (2012); Blatt and Roos (2012); Georgescu et al.
(2014); Houck et al. (2012); and Schneider et al. (2012)
for information about digital quantum simulation of
other physical systems, and analog quantum simulation.

BQP (bounded-error quantum polynomial-time) (Bern-
stein and Vazirani, 1997; Lloyd, 1996). It is important
to note that, while it is widely believed to be true, it has
not yet been mathematically proven that BPP ̸= BQP
(where BPP is the complexity class containing problems
that are solvable in polynomial time on a probabilistic
classical computer). Further discussion of general Hamil-
tonian simulation methods is given in Sec. V.A.3.
It has also been shown that time evolution of open and
closed quantum systems can be simulated using varia-
tional approaches (Chen et al., 2019; Endo et al., 2018b;
Heya et al., 2019; Li and Benjamin, 2017). A variational
circuit is one with parametrized quantum gates, whose
parameters are updated according to an algorithm spe-
ciﬁc update rule. They are discussed in more detail in
Sec. V.B. These techniques may enable simulation of time
evolution using circuits with fewer gates than Trotteriza-
tion. However, a variational circuit with set parameters
is tailored to the time evolution of one or more speciﬁc
initial states, in contrast to a Trotter circuit, which can
be used to time evolve any valid initial state.
Once the system has been time evolved for the desired
duration, we can extract useful dynamical quantities
from these simulations.
Examples of such quantities
include the electronic charge density distribution, or
particle
correlation
functions
(Abrams
and
Lloyd,
1997). Further information on quantum dynamics sim-
ulation can be found in the review by Brown et al. (2010).

The numerous problems in chemistry that can be
simulated on a quantum computer can be divided into
static and dynamics problems. Here, we use ‘dynamics’
to mean evolving wavefunctions in time and seeing
how certain observables vary, as opposed to chemical
reaction dynamics, which are discussed separately below.

Methods for solving dynamics problems were for-
malised by Lloyd (1996) and further developed by
Abrams and Lloyd (1997). As illustrated in Fig. 3, we
can map the system Hamiltonian, Hs, to a qubit Hamil-
tonian, Hq. We similarly map the initial system wave-
function |ψi
s⟩to a qubit representation |ψi
q⟩.
We can
then evolve the qubit wavefunction in time by mapping
the system time evolution operator, e−itHs, to a series of
gates. This can be achieved using a Lie-Trotter-Suzuki
decomposition (Trotter, 1959), commonly referred to as
Trotterization or a Trotter circuit. This means that if
the Hamiltonian of the system, Hs can be written as

In chemistry, one is often concerned with determining
whether two or more sub-systems will react with each
other, when brought together with a certain energy.
One might assume that this could be studied by simply
initialising the reactants on the quantum computer,
and time evolving under the system Hamiltonian, using
the methods described above.
However, it depends
on the method used to map the chemical problem
onto the quantum computer.
We must take care to
ensure that our model is able to accurately describe
the system during all parts of the reaction.
This is
naturally taken care of using grid based methods,
where the electrons and nuclei are treated on an equal
footing, as discussed in Sec. III.B.1 and Sec. IV.A.1.
In contrast, if the problem is projected onto a ﬁnite
basis set of electron spin-orbitals, we must be careful
to ensure that: 1) The nuclear dynamics are accurately
described, either through a precise classical treatment
of the nuclear dynamics, or by using additional orbitals
to describe the nuclear motion, and 2) The electron
spin-orbitals used are able to accurately describe the
positions of the electrons at all points in the reaction.
This may require the orbitals to change in time. To the
best of our knowledge, only the work by Berry et al.
(2019a) considers a chemical reaction dynamics cal-
culation on a quantum computer using basis set methods.

Hs =
X

j
hj,
(13)

where hi are local terms which act on a small subset of
the particles in the system, then a small time evolution
under the Hamiltonian can be decomposed as

j hjδt ≈
Y

e−iHsδt = e−i P

j
e−ihjδt + O(δt2).
(14)

The number of terms in the Hamiltonian scales polyno-
mially with the number of particles for systems of in-
terest in chemistry, due to the two-body nature of the
Coulomb interactions between particles (Helgaker et al.,
2014). Each of the exponential terms in Eq. (14) can be
realised eﬃciently using a quantum computer.
As the
dynamics of local Hamiltonians can be eﬃciently simu-
lated on a quantum computer, but are generally thought
to be ineﬃcient to simulate on a classical computer, this
problem belongs to the computational complexity class

## Page 8

FIG. 3 Digital quantum simulation of time evolution of a spin chain, using a canonical Trotter-type method. We ﬁrst map
the system Hamiltonian, Hs, to a qubit Hamiltonian, Hq. Then the initial system wavefunction |ψi
s⟩is mapped to a qubit
wavefunction |ψi
q⟩. The time evolution of the system can be mapped to a Trotterized circuit that acts on the initial qubit
wavefunction. Finally, well chosen measurements are applied to extract the desired information, such as particle correlation
functions. For a spin chain with an Ising Hamiltonian, H = P

⟨i,j⟩JijZiZj + P

i BiXi, where the ﬁrst sum is over nearest-
neighbour spins i and j, the unitaries Uij are given by Uij = CNOTi,j Rj
z(2Jij) CNOTi,j Ri
x(2Bi).

We can obtain static properties by mapping the tar-
get wavefunction (such as the ground state wavefunction
of the system) onto a qubit wavefunction. We can then
use the quantum computer to calculate the expectation
value of the desired observable, ⟨ψq| Oq |ψq⟩. In partic-
ular, Abrams and Lloyd (1999) showed that the phase
estimation algorithm (Kitaev, 1995) can be used to ﬁnd
the energy of a quantum system, and collapse it into the
desired energy eigenstate. We will discuss this approach
in Sec. V.A. The ground state problem can also be tack-
led using variational algorithms (Peruzzo et al., 2014),
which we will discuss in detail in Sec. V.B.

Finding the low lying energy levels of a quantum
Hamiltonian is in general an exponentially diﬃcult prob-
lem for classical computers. Moreover, it is important
to note that solving the ground state problem for a
completely general local Hamiltonian is QMA-complete
(quantum Merlin-Arthur complete, the quantum ana-
logue of NP-complete) (Cubitt and Montanaro, 2016;
Kempe et al., 2006). Problems in this complexity class
are not believed to be eﬃciently solvable with either a
classical or quantum computer.
For such systems, it
would appear that Nature itself cannot eﬃciently ﬁnd
the ground state.

Despite this, the situation is not as bleak as it may
initially seem. As stated in the introduction, we focus

on ﬁnding the low lying energy levels of chemical sys-
tems (solving the electronic structure problem).
It is
widely believed that this problem should be eﬃciently
solvable with a quantum computer, for physically rel-
evant systems (Whitﬁeld et al., 2013).
The electronic
structure problem has received signiﬁcant attention since
it was ﬁrst introduced in the context of quantum com-
putational chemistry by Aspuru-Guzik et al. (2005), and
is widely considered to be one of the ﬁrst applications
of quantum computing. Solving the electronic structure
problem is often a starting point for more complex cal-
culations in chemistry, including the calculation of re-
action rates, the determination of molecular geometries
and thermodynamic phases, and calculations of optical
properties (Helgaker et al., 2012).
Before discussing how the electronic structure problem
can be solved using a quantum computer in Sec. IV and
Sec. V, we ﬁrst summarise the classical methods used
to solve this problem in Sec. III. Many of these meth-
ods have formed the basis of the work done thus far in
quantum computational chemistry.

III. CLASSICAL COMPUTATIONAL CHEMISTRY

In this section, we introduce a selection of the most
widely used techniques in ab initio classical computa-

## Page 9

tional chemistry. As discussed in the introduction, we
focus on tools developed to solve the electronic structure
problem. The problem is formulated in Sec. III.A, and
translated into the language of ﬁrst and second quantisa-
tion in Sec. III.B. In Sec. III.C we describe the diﬀerent
approximations that can be used to make this problem
tractable for classical computers. In Sec. III.D we review
some of the common spin-orbital basis functions used in
basis set approaches to the molecular electronic structure
problem.
We discuss orbital basis changes, and their
use in reducing the simulation resources in Sec. III.E.
We have sought to produce a self-contained summary
of the essential knowledge required for quantum compu-
tational chemistry, and we refer the reader to Helgaker
et al. (2014) and Szabo and Ostlund (2012) for further
information.

A. The electronic structure problem

The Hamiltonian of a molecule consisting of K nuclei
and N electrons is

ℏ2

ℏ2

e2

ZI
|ri −RI|

H = −
X

2me
∇2
i −
X

2MI
∇2
I −
X

4πϵ0

i

I

i,I

e2

e2

+ 1

1
|ri −rj| + 1

ZIZJ
|RI −RJ|,

X

X

2

4πϵ0

2

4πϵ0

i̸=j

I̸=J

(15)
where MI, RI, and ZI denote the mass, position, and
atomic number of the Ith nucleus, and ri is the posi-
tion of the ith electron.
The ﬁrst two sums in H are
the kinetic terms of the electrons and nuclei, respectively.
The ﬁnal three sums represent the Coulomb repulsion be-
tween: the electrons and nuclei, the electrons themselves,
and the nuclei themselves, respectively. For conciseness,
we work in atomic units, where the unit of length is
a0 = 1 Bohr (0.529 × 10−10 m), the unit of mass is
the electron mass me, and the unit of energy is 1 Hartree
(1 Hartree
=
e2/4πϵ0a0
=
27.211 eV).
Denoting
M ′
I = MI/me, the Hamiltonian in atomic units becomes

∇2
i
2 −
X

∇2
I
2M ′
I
−
X

ZI
|ri −RI|

H = −
X

i

I

i,I

ZIZJ
|RI −RJ|.
(16)

+ 1

1
|ri −rj| + 1

X

X

2

2

i̸=j

I̸=J

We are predominantly interested in the electronic
structure of the molecule. As a nucleon is over one thou-
sand times heavier than an electron, we apply the Born-
Oppenheimer approximation, treating the nuclei as clas-
sical point charges. As a result, for a given nuclear con-
ﬁguration one only needs to solve the electronic Hamil-
tonian

∇2
i
2 −
X

ZI
|ri −RI| + 1

1
|ri −rj|. (17)

He = −
X

X

2

i

i̸=j

i,I

Our aim is to ﬁnd energy eigenstates |Ei⟩and the
corresponding energy eigenvalues Ei of the Hamiltonian
He.
In the rest of this review, we drop the subscript
e. In particular, we are interested in the ground state
energy and the lowest excited state energies.
We can
solve this equation for a range of nuclear conﬁgurations
to map out the potential energy surfaces of the molecule.
Mapping out these potential energy curves explicitly
is exponentially costly in the degrees of freedom of
the molecule, and that there are a variety of methods
being developed to solve this diﬃcult problem more
eﬃciently (Christiansen, 2012).

We wish to measure the energy to an accuracy of at
least 1.6 × 10−3 Hartree, known as ‘chemical accuracy’.
If the energy is known to chemical accuracy, then the
chemical reaction rate at room temperature can be pre-
dicted to within an order of magnitude using the Eyring
equation (Evans and Polanyi, 1935; Eyring, 1935)

Rate ∝e−∆E/kBT ,
(18)

where T is the temperature of the system, and ∆E is
the energy diﬀerence between the reactant and product
states. In computational chemistry, we are typically more
interested in the relative energies of two points on the
potential energy surface than the absolute energy of a
single point. Even if the individual energy values can-
not be measured to within chemical accuracy, there is
often a fortuitous cancellation of errors, which leads to
the energy diﬀerence being found to chemical accuracy.
However, in this review we consider chemical accuracy to
mean an error of less than 1.6 × 10−3 Hartree in the en-
ergy value at every point on the potential energy surface.

1. Chemical systems of interest

While classical computational chemistry has made
tremendous progress in describing and predicting the
properties of a multitude of systems, there are some
systems that appear classically intractable to simulate
with currently known techniques.
Consequently, there
has been signiﬁcant interest in the possibility of using
quantum computers to eﬃciently solve these problems.
In particular, we are interested in solving so-called
‘strongly correlated systems’ (we will explain this term
more carefully in Sec. III.C.1.
Here, it suﬃces to say
that these are systems which possess wavefunctions
with a high degree of entanglement. Many systems of
commercial and scientiﬁc interest, such as catalysts and
high temperature superconductors, are believed to be
strongly correlated. In this section, we discuss two such
strongly correlated systems that have been identiﬁed
as interesting potential targets for a future quantum

## Page 10

computer.

Many transition metals have found use as cata-
lysts (Vogiatzis et al., 2019).
However, many of these
systems show strong correlation, often due to their open-
shell nature, and spatially degenerate states (Lyakh
et al., 2012).
This strong correlation often precludes
their study in silico, forcing us to carry out expen-
sive, trial-and-error based discovery – especially for
transition metal based biological catalysts (Podewitz
et al., 2011).
One such system is the biological en-
zyme nitrogenase, which enables microorganisms which
contain it to convert atmospheric dinitrogen (N2) to
ammonia (NH3) under ambient conditions. This process
is known as nitrogen ﬁxation, and is one of the two
main ways of producing ammonia for fertiliser – the
other is the energy intensive Haber-Bosch process. The
Haber-Bosch process requires high temperatures and
pressures, and is believed to consume up to 2 % of
the world’s energy output (Reiher et al., 2017). While
there has been signiﬁcant experimental progress in
understanding the structure of the nitrogenase enzyme
over the last 100 years, the reaction mechanism is
not yet fully understood (Burgess and Lowe, 1996).
The crux of understanding the enzyme appears to be
several transition metal compounds found within it:
the P cluster (containing iron and sulphur) and the
iron molybdenum cofactor (FeMo-co, containing iron,
molybdenum, carbon, hydrogen and oxygen) (Hoﬀman
et al., 2014).
Computational models of FeMo-co have
been proposed which are beyond the reach of current
classical methods for solving strongly correlated systems
(see Sec. VIII.A) but would be accessible with a small
error corrected quantum computer (Berry et al., 2019b;
Reiher et al., 2017). We discuss the resources required
for these simulations in Sec. VIII.B.

High temperature superconductors are also believed
to be strongly correlated systems.
Since their discov-
ery in the 1980’s, there has been signiﬁcant experimen-
tal and theoretical work to understand these compounds,
which are not well described by the Bardeen-Cooper-
Schrieﬀer theory of superconductivity. In the case of the
so-called cuprate superconductors, it is widely believed
that the mechanism of high temperature superconductiv-
ity is closely linked to the physics of the copper-oxygen
planes that comprise them. A complete analytic or com-
putational understanding of these layers is beyond the ca-
pabilities of current classical techniques. Several simpli-
ﬁed models have been proposed, which have been found
to capture some of the important behaviour of high tem-
perature superconductors (Dagotto, 1994). In particu-
lar, models of fermions hopping on a 2D square lattice,
such as the one-band Fermi-Hubbard model (Hubbard,
1963), and the related t-J model, appear to reproduce
many experimental observations (Anderson, 2002; Lee

et al., 2006). While more complex models are likely re-
quired to fully understand the mechanism of cuprate su-
perconductivity, a complete understanding of even the
Fermi-Hubbard model is still elusive. Close to half ﬁll-
ing, at intermediate interaction strengths, the system ap-
pears to show several competing orders in its phase di-
agram, which makes it diﬃcult to reliably extract the
ground state properties from classical numerical calcu-
lations (Fradkin et al., 2015). Interestingly, this is the
same regime that is believed to be most relevant to under-
standing cuprate superconductors (LeBlanc et al., 2015).
Properties are typically obtained by performing ground
state calculations on the Fermi-Hubbard model for a
range of diﬀerent system sizes, and then extrapolating
to the thermodynamic limit (LeBlanc et al., 2015). We
discuss the system sizes that can be tackled using modern
classical techniques in Sec. VIII.A. We then examine the
quantum resources required to surpass these calculations
in Sec. VIII.B.

B. First and Second quantisation

As a consequence of the Pauli exclusion principle, the
electronic wavefunction must be antisymmetric under the
exchange of any two electrons. This antisymmetrisation
can be accounted for in two ways, known as ﬁrst and
second quantisation.
These names are largely histori-
cal; ﬁrst quantisation was the approach initially taken
by the pioneers of quantum mechanics, whereby variables
like position and momentum are promoted to being op-
erators (they are ‘quantised’). Second quantisation was
developed afterwards, and quantises ﬁelds, rather than
variables. There are key diﬀerences between these repre-
sentations, which aﬀect how simulations of physical sys-
tems are carried out using a quantum computer.

As will be discussed in Sec. III.B.1, ﬁrst quantised
methods explicitly retain the antisymmetry in the wave-
function. In contrast, second quantisation maintains the
correct exchange statistics through the properties of the
operators which are applied to the wavefunction, as we
will show in Sec. III.B.2. These diﬀerences will become
more apparent in the context of quantum computational
chemistry mappings, which we will discuss in Sec. IV.
It is important to note that whether a simulation is
carried out in ﬁrst or second quantisation is distinct from
whether a ‘basis set’ or ‘grid based’ method is used. This
will be elaborated on in more detail in the following sec-
tions. However, one key diﬀerence is that using a basis
set is known as a ‘Galerkin discretisation’, which ensures
that the energy converges to the correct value from above,
as the number of basis functions tends to inﬁnity. This
property does not hold for grid based methods. A more
detailed discussion on the diﬀerences between grid based
and basis set methods can be found in the main text and
Appendix A of Babbush et al. (2018c).

## Page 11

1. First quantisation

Here, we focus on classical ﬁrst quantised simulation
methods. Discussion of ﬁrst quantised chemistry simula-
tion on quantum computers is postponed until Sec. IV.A.

a. Grid based methods
We
consider
the
wavefunction
in
the
position
representation, {|r⟩}, which must be explicitly anti-
symmetrised to enforce exchange symmetry. Mathemat-
ically, we describe the N electron wavefunction as

|Ψ⟩=
Z

x1,...,xN
ψ(x1, . . . , xN)A (|x1, . . . , xN⟩) dx1, . . . , dxN

(19)
where A denotes antisymmetrisation, xi = (ri, σi) =
(xi, yi, zi, σi) gives the position and spin of the ith elec-
tron and ψ(x1, x2, . . . , xN) = ⟨x1, x2, . . . , xN|Ψ⟩.
We
can simulate this system on a classical computer by eval-
uation of the wavefunction on a discretised spatial grid.
However, the cost of storing the wavefunction scales ex-
ponentially with the number of electrons, N. Suppose
each axis of space is discretised into P equidistant points.
The discretised wavefunction is given by

|Ψ⟩=
X

x1,...,xN
ψ(x1, . . . , xN)A (|x1, . . . , xN⟩) ,
(20)

where |xi⟩= |ri⟩|σi⟩is a spatial and spin-coordinate,
|ri⟩
=
|xi⟩|yi⟩|zi⟩, ∀i
∈
{1, 2, . . . , N},
xi, yi, zi
∈
{0, 1, . . . , P −1}, and σi ∈{0, 1}.
In total, there are
P 3N × 2N complex amplitudes, showing that the mem-
ory required scales exponentially with the size of the sim-
ulated system. This makes it classically intractable to
simulate more than a few particles on a grid using a clas-
sical computer. Consequently, we do not discuss classical
methods that are speciﬁc to the grid based mapping in
this review.
Grid based methods are useful when considering
chemical reaction dynamics, or when simulating systems
for which the Born-Oppenheimer approximation is not
appropriate.
In these scenarios, we must include the
motion of the nuclei. If we consider the nuclear motion
separately, we need to obtain the potential energy
surfaces from electronic structure calculations.
As
mentioned in the previous section, mapping out these
potential energy surfaces is exponentially costly.
As
such, it may be better to treat the nuclei and electrons
on an equal footing, which is best achieved with grid
based methods. This is discussed further by Kassal et al.
(2008).

b. Basis set methods

We project the Hamiltonian onto M basis wavefunc-
tions, {φp(xi)}, where xi is the spatial and spin coordi-
nate of the ith electron, xi = (ri, σi). These basis func-
tions approximate electron spin-orbitals. The grid based
method described above directly stores the wavefunction
without exploiting any knowledge we may have about the
general spatial form of the orbitals. In contrast, basis set
methods exploit this knowledge to reduce the resources
needed to simulate chemical systems. We write the many
electron wavefunction as a Slater determinant, which is
an antisymmetrised product of the single electron basis
functions. The wavefunction is given by

ψ(x0 . . . xN−1) =

φ0(x0)
φ1(x0)
...
φM−1(x0)

φ0(x1)
φ1(x1)
...
φM−1(x1)

. (21)

.
.
.
.

1
√

N!

.
.
.
.

.
.
.
.

φ0(xN−1) φ1(xN−1) ... φM−1(xN−1)

Swapping the positions of any two electrons is equiva-
lent to interchanging two rows of the Slater determinant,
which changes the sign of the wavefunction. This pro-
vides the correct exchange symmetry for the fermionic
wavefunction. While the number of spin-orbitals consid-
ered, M, is typically larger than the number of electrons
in the system, N, the electrons can only occupy N of
the spin-orbitals in a given Slater determinant. As a re-
sult, the Slater determinant only contains the N occupied
spin-orbitals. For example, imagine a ﬁctitious system
with two electrons, distributed among basis functions
A(x) and B(x). Each of these basis functions could be oc-
cupied by an electron of either spin, so we eﬀectively work
with four basis functions {A↑(x), A↓(x), B↑(x), B↓(x)}.
We consider the case where both electrons are in the A
orbitals (and therefore have opposite sz values, where sz
is the z component of the spin of the electron). As dis-
cussed above, the Slater determinant only contains the
N occupied spin-orbitals. We use Eq. (21) to obtain the
wavefunction

ψ(x0, x1) =

=

A↑(x0) A↓(x0)

1
√

(22)

2

A↑(x1) A↓(x1)


A↑(x0)A↓(x1) −A↓(x0)A↑(x1)

.

1
√

2

This wavefunction is antisymmetric under the exchange
of the two electrons, as required.

As we will see in Sec. III.B.2, the information encoded
by a Slater determinant can be compressed by moving

## Page 12

to the second quantised formalism. As a consequence,
ﬁrst quantised basis set methods are rarely, if ever, used
in classical computational chemistry calculations. Nev-
ertheless, it is important to be aware of what the wave-
function looks like in the ﬁrst quantised basis set rep-
resentation for two reasons. Firstly, as discussed above,
the second quantised basis set method follows directly
from the ﬁrst quantised basis set approach.
Secondly,
ﬁrst quantised basis set approaches have found use in
quantum computational chemistry, as we will discuss in
Sec. IV.A.2.

2. Second quantisation

a. Basis set methods
The second quantised basis set approach follows nat-
urally from the ﬁrst quantised basis set method discussed
in Sec. III.B.1. We again project the Hamiltonian onto
M basis wavefunctions, {φp(xi)}, and consider many-
electron wavefunctions that must be antisymmetric un-
der the exchange of any two electrons.
As we saw in
Sec. III.B.1, to write down a Slater determinant we only
need to indicate which spin-orbitals are occupied by elec-
trons.
This enables the introduction of a convenient
shorthand for Slater determinants (Szabo and Ostlund,
2012)

ψ(x0 . . . xN−1) = |fM−1, . . . , fp, . . . , f0⟩= |f⟩,
(23)

where fp = 1 when φp is occupied (and therefore present
in the Slater determinant), and fp = 0 when φp is empty
(and therefore not present in the determinant).
The
vector |f⟩is known as an occupation number vector,
and the space of all such vectors is known as ‘Fock
space’.
The second quantised formalism is concerned
with manipulating these occupation number vectors.
As these occupation number vectors are a convenient
short-hand for Slater determinants, we will refer to them
throughout this review as Slater determinants. This is
common practice in computational chemistry (Szabo
and Ostlund, 2012).

with

Electrons are excited into the single electron spin-
orbitals by fermionic creation operators, a†
p. They are
de-excited by annihilation operators, ap. These opera-
tors obey fermionic anti-commutation relations

{ap, a†
q} = apa†
q + a†
qap = δpq,

{ap, aq} = {a†
p, a†
q} = 0.
(24)

The determinants |f⟩form an orthonormal basis for
the Fock space of the system.
The actions of the

fermionic operators on the determinants are given by

ap |fM−1, fM−2, . . . , f0⟩

=δfp,1(−1)
Pp−1
i=0 fi |fM−1, fM−2, . . . , fp ⊕1, . . . , f0⟩,

a†
p |fM−1, fM−2, . . . , f0⟩

=δfp,0(−1)
Pp−1
i=0 fi |fM−1, fM−2, . . . , fp ⊕1, . . . , f0⟩,
(25)
where ⊕denotes addition modulo 2, such that 0⊕1 = 1,
1 ⊕1 = 0.
The phase term (−1)
Pp−1
i=0 fi enforces the
exchange anti-symmetry of fermions.
The spin-orbital
occupation operator is given by

ˆni = a†
iai,

ˆni |fM−1, . . . , fi, . . . , f0⟩= fi |fM−1, . . . , fi, . . . , f0⟩,
(26)
and counts the number of electrons in a given spin-
orbital.

Observables must be independent of the representa-
tion used. Therefore, the expectation values of second
quantised operators must be equivalent to the expecta-
tion values of the corresponding ﬁrst quantised opera-
tors. As ﬁrst quantised operators conserve the number
of electrons, the second quantised operators must contain
an equal number of creation and annihilation operators.
We can use these requirements to obtain the second quan-
tised form of the electronic Hamiltonian (Helgaker et al.,
2014; Szabo and Ostlund, 2012).

p,q
hpqa†
paq + 1

H =
X

X

p,q,r,s
hpqrsa†
pa†
qaras,
(27)

2

!

−∇2

ZI
|r −RI|

hpq =
Z
dxφ∗
p(x)

2 −
X

φq(x),

I

hpqrs =
Z
dx1dx2
φ∗
p(x1)φ∗
q(x2)φr(x2)φs(x1)

|r1 −r2|
.

(28)
The ﬁrst integral represents the kinetic energy terms
of the electrons, and their Coulomb interaction with
the nuclei. The second integral is due to the electron-
electron Coulomb repulsion. The Hamiltonian only con-
tains terms with up to four creation and annihilation
operators (two creation, two annihilation) because the
Coulomb interaction between the electrons is a two-body
interaction.
As a result, the Hamiltonian contains up
to M 4 terms, depending on the basis functions used.
We examine the form of these basis functions, and how
to select them in Sec. III.D. A special case of the elec-
tronic structure Hamiltonian is obtained for the Fermi-
Hubbard model, introduced in Sec. III.A.1. The Fermi-
Hubbard Hamiltonian considers fermions hopping be-
tween nearest-neighbour lattice sites with strength t.

## Page 13

These fermions feel a repulsive (or attractive) force U
when they occupy the same lattice site, i. The Hamilto-
nian is given by


a†
i,σaj,σ + a†
j,σai,σ

+ U
X

H = −t
X

i
ni,↑ni,↓(29)

⟨i,j⟩,σ

where ⟨i, j⟩denotes a sum over nearest-neighbour lattice
sites, and σ is a spin-coordinate. This Hamiltonian has
only O(M) terms, where M is the number of spin-sites.
For convenience, throughout the rest of this review we
will refer to both molecular spin-orbitals and lattice spin
sites as spin-orbitals.

Let us consider general and approximate solutions of
the electronic structure Hamiltonian.
If the electron-
electron Coulomb interaction term in Eq. (17) is ne-
glected, we obtain a new Hamiltonian which describes
the behaviour of N independent electrons. We can de-
ﬁne a suitable basis for this ﬁctitious system as the set of
molecular orbitals which diagonalise the non-interacting
Hamiltonian. These molecular orbitals are typically lin-
ear combinations of orbitals localised around each of the
atoms. We note that in practice, the molecular orbitals
obtained by diagonalising the non-interacting part of the
Hamiltonian will likely form a poor basis for the sys-
tem. Instead, a mean-ﬁeld approximation (the Hartree-
Fock procedure, to be described in Sec. III.C.1) can be
used to obtain more suitable molecular orbitals.
As
these single-particle molecular orbitals are chosen such
that they diagonalise the non-interacting (or mean-ﬁeld)
Hamiltonian, energy eigenstates can be formed by tak-
ing tensor products of each electron in a diﬀerent molec-
ular spin-orbital. In order to obey the Pauli exclusion
principle, these tensor products must be correctly anti-
symmetrised.
This can be achieved by creating Slater
determinants from the molecular orbitals, as described
by Eq. (21).
As they are eigenstates of a Hermitian operator, these
Slater determinants form a complete basis of the problem
Hilbert space. Consequently, the eigenstates of the true
Hamiltonian can be expressed as linear combinations of
these Slater determinants, written as

|Ψ⟩=
X

f
αf |f⟩,
(30)

where αf are complex coeﬃcients which we refer to herein
as the determinant amplitudes. These solutions are ex-
act, provided that the molecular orbitals form a complete
basis for the single particle states, and the N-electron
wavefunction contains all of the determinants that these
molecular orbitals can generate (Helgaker et al., 2014;
Szabo and Ostlund, 2012). If all
M
N

determinants are
included, the wavefunction is known as the full conﬁg-
uration interaction (FCI) wavefunction.
However, this
wavefunction contains a number of determinants which

scales exponentially with the number of electrons, mak-
ing large calculations classically intractable.
Second quantised basis set methods are the most
widely used approach in classical computational chem-
istry, and have formed the basis of most of the work
done so far in quantum computational chemistry. As a
result, we discuss some of the approximate methods used
in second quantised basis set simulations in Sec. III.C
and Sec. III.D. In Sec. III.C we consider making ground
state calculations classically tractable by approximating
the exact ground state wavefunction with a restricted
number of Slater determinants. In Sec. III.D we consider
approximating the exact wavefunction by considering
only the most important molecular orbitals.
However,
ﬁrst we brieﬂy discuss the limited work that has been
done on second quantised grid based methods, for the
sake of completeness.

b. Grid based methods

To the best of our knowledge, second quantised
grid based methods have only been discussed by Bab-
bush et al. (2018c) in their Appendix A. Nevertheless,
these methods follow naturally from the discussion of
second quantised basis sets above.
Our discussion of
the topic closely follows the derivation of Babbush et al.
(2018c). As a ﬁrst step, we can consider our real space
grid to be described by a set of basis functions that are
delta functions, δ(r −ri), each positioned at grid point
ri = (xi, yi, zi). The creation operators a†
i,σ then become
a†
xi,yi,zi,σ ; rather than creating an electron in spin-orbital
i, they now create an electron with spin σ at the grid
point (xi, yi, zi) in 3D space. As the basis functions do
not overlap in space, the kinetic energy operator must be
deﬁned using a ﬁnite diﬀerence formula, rather than the
integral in Eq. (28). We must also deﬁne a suitable in-
ner product between functions deﬁned on the grid. These
steps allow us to calculate the coeﬃcients of each term in
the Hamiltonian. As discussed above, this second quan-
tised grid based method has not yet (to the best of our
knowledge) been used in any classical or quantum com-
putational chemistry algorithms.

C. Classical computation methods

In this section, we review four methods for approximat-
ing the ground state wavefunction with a restricted num-
ber of Slater determinants: the Hartree-Fock (HF), mul-
ticonﬁgurational self-consistent ﬁeld (MCSCF), conﬁgu-
ration interaction (CI), and coupled cluster (CC) meth-
ods.
These methods create parametrized trial states,
which can then be optimised to approach the ground
state (to an accuracy determined by the approximations
made).
In order to isolate the errors arising from the

## Page 14

method used, we assume that we are working in the
full molecular orbital basis for our molecule, although
in practice this would be classically intractable for large
system sizes (with the size of the system dependent upon
the accuracy of the method used). Restricting the size of
the basis set will be discussed in Sec. III.D.
The methods discussed below are considered in the
context of second quantised basis set calculations, as
these translate most easily to the methods used in quan-
tum computational chemistry. These methods are among
the most straightforward and widely used in classical
computational chemistry.

the old orbitals). This process is repeated until the or-
bitals converge (Szabo and Ostlund, 2012). The new or-
bitals obtained are referred to as the canonical orbitals.
This procedure generates single particle molecular or-
bitals from combinations of the single particle atomic
orbitals.
The term hikkj describes the Coulomb interaction of
an electron with the charge distribution of the other elec-
trons, while the term hikjk describes exchange eﬀects
(also called Fermi correlation) arising from the required
antisymmetrisation. However, as a mean-ﬁeld solution,
the HF method neglects the eﬀects of dynamic and static
correlation in the wavefunction.
Dynamic
correlation
is
a
typically
small
correc-
tion (Hattig et al., 2012), arising from the Coulomb
repulsion between electrons.
Wavefunctions display-
ing dynamic correlation are often dominated by the
Hartree-Fock determinant, and have small additional
contributions from a (potentially large) number of ex-
cited state determinants. Static correlation occurs when
more than one Slater determinant is equally dominant
in the wavefunction (Hattig et al., 2012). In this case,
the Hartree-Fock method provides a poor approximation
to the ground state wavefunction.
The presence of
strong static correlation can be evidenced by multiple
near-degenerate solutions of the Hartree-Fock procedure.
Static correlation can arise because the wavefunction
may require several determinants to be coupled in a
proper spin conﬁguration, or during bond breaking in
order to account for the separation of the electrons
onto the products (the latter case is often referred to
as non-dynamic, or left-right correlation) (Lyakh et al.,
2012). The relative contribution of these eﬀects depends
on the orbital basis used.
Lyakh et al. (2012) note
that, while it is sometimes possible to reduce the level
of static correlation by manually enforcing correct spin
symmetries, and using appropriately localised orbitals,
it is in general not possible to avoid strong static
correlation when considering the whole of the potential
energy surface.
As a result, static correlation often
dominates in many systems of scientiﬁc interest, such
as excited states (Lischka et al., 2018), or transition
metals (Vogiatzis et al., 2019).

1. Hartree–Fock

The Hartree–Fock (HF) method is a mean-ﬁeld tech-
nique which aims to ﬁnd the dominant Slater determi-
nant in the system wavefunction. This is achieved by op-
timising the spatial form of the spin-orbitals to minimise
the energy of the wavefunction. We generally consider a
set of spin-orbitals, M, that is larger than the number of
electrons in the molecule, N. As we only consider a single
Slater determinant, we are essentially assuming that N
of the spin-orbitals are occupied, and M −N are left un-
occupied, or virtual. In the HF method, we ﬁrst neglect
the Coulomb repulsion term in the electronic structure
Hamiltonian (Eq. (17)), reducing the problem to one of
N independent electrons. We then assume that each elec-
tron moves in the average charge distribution of all of the
other electrons, which introduces an eﬀective potential.
We can solve the N coupled equations iteratively; ﬁrst
calculating the position of each electron, then updating
the potential, and repeating this process until the orbitals
converge. In the second quantised formalism, this proce-
dure is carried out by using the orbitals to construct the
‘Fock operator’, and diagonalising the Fock operator to
obtain new orbitals. This process is repeated until the
orbitals converge, and so HF is also referred to as the
self-consistent ﬁeld (SCF) method. The Fock operator,
ˆf, is given by (Helgaker et al., 2014)

ˆf =
X

i,j
(hij + Vij)a†
iaj,

k∈occ
(hikkj −hikjk),
(31)

The Slater determinant generated from a HF calcula-
tion is typically taken as the reference state for post-HF
methods, such as conﬁguration interaction and coupled
cluster, which seek to capture some of the dynamic corre-
lation energy by including additional determinants, de-
scribing excitations above the HF state.
Although we
will discuss orbital basis sets in more detail in Sec. III.D,
we note here that the HF orbitals are not suitable for
describing the virtual orbitals that electrons are excited
into. This is because the HF method only optimises the
occupied orbitals in the single Slater determinant wave-
function. In order to obtain suitable virtual orbitals, we

Vij =
X

where Vij describes the eﬀective potential, and occ is the
set of occupied orbitals. We see that the Fock operator
depends on the spatial form of the orbitals through hij,
hikkj, and hikjk which are obtained by calculating the
integrals in Eq. (28). When performing a HF calcula-
tion, we typically input a set of atomic orbitals, which
are localised around each atom. These orbitals are used
to calculate the Fock operator, which is then diagonalised
to obtain new orbitals (which are linear combinations of

## Page 15

can instead perform correlated calculations on individual
atoms. The details of how to perform these correlated
atomic calculations are beyond the scope of this review,
and are not relevant for quantum computing applications.
We refer the interested reader to Section 8.3 of the text-
book by Helgaker et al. (2014) for additional details. The
importance of each of the virtual atomic orbitals is deter-
mined by their contribution to either the electron density
(atomic natural orbitals) or the atomic correlation energy
(correlation-consistent basis sets). These two metrics are
closely related, and while either can be used, the lat-
ter produces more compact basis sets, and hence is used
more frequently in practice (Helgaker et al., 2014). We
will discuss the use of correlation consistent basis sets
further in Sec. III.D.2.

2. Multiconﬁgurational self-consistent ﬁeld

As discussed above, the Hartree-Fock method performs
poorly for strongly correlated systems.
Systems with
strong static correlation are deﬁned as those where mul-
tiple Slater determinants are equally dominant. These
include excited states (Lischka et al., 2018), transition
states (Szalay et al., 2012), systems at the dissociation
limit (Lyakh et al., 2012), and transition metals (Vo-
giatzis et al., 2019). In order to account for static cor-
relation, we need to use a wavefunction which exhibits
the required multireference nature. One such approach
is the multiconﬁgurational self-consistent ﬁeld (MCSCF)
method. The MCSCF approach considers a wavefunc-
tion with several Slater determinants, and variationally
optimises both the molecular orbitals, and the deter-
minant amplitudes simultaneously (Roos et al., 1980).
Mathematically, we write our MCSCF wavefunction as
|Ψ⟩= e−κ P



=

f αf |f⟩, where again αf are determinant
amplitudes, and |f⟩are Slater determinants. Here, κ is
an anti-Hermitian operator given by κ = P

i,j kija†
iaj.
Exponentiating κ produces a unitary operator which ro-
tates the orbital basis (Helgaker et al., 2014). We then
variationally minimise the energy by optimising both the
amplitudes αf, and the entries kij of κ.

MCSCF can be considered the best approximation to
the exact wavefunction for a given number of determi-
nants (Wang et al., 2008).
It is not possible to per-
form a complete MCSCF calculation on all possible de-
terminants for systems with more than a few electrons,
as the number of determinants scales exponentially with
the number of electrons. We can attempt to use chem-
ical intuition to select the most important Slater deter-
minants, and perform an MCSCF calculation on this
restricted number of determinants.
Alternatively, we
can use the complete active space self-consistent ﬁeld
(CASSCF) method (Roos et al., 1980).
This consid-
ers only the most important orbitals (an active space,
see Sec. III.E) and performs an MCSCF calculation on

all of the determinants that could be generated from
distributing a certain number of electrons in these or-
bitals.
MCSCF and CASSCF calculations are among
the most eﬀective classical methods at treating systems
with strong static correlation (Szalay et al., 2012). Re-
cent approaches, including replacing the CASSCF sub-
routine with tensor network methods, have enabled the
treatment of even larger active spaces (Knecht et al.,
2016). However, while the methods described above are
often eﬀective at recovering the static correlation energy,
they struggle to recover the dynamic correlation energy.
This requires additional techniques, such as multirefer-
ence conﬁguration interaction (see Sec. III.C.3 and Sza-
lay et al. (2012)) and multireference coupled cluster (see
Sec. III.C.4 and Lyakh et al. (2012)) .

3. Conﬁguration interaction

The conﬁguration interaction (CI) method generates a
correlated wavefunction by considering excitations above
a reference state, typically the Hartree-Fock state.
If
all determinants are included, we recover the full con-
ﬁguration interaction (FCI) wavefunction, generated by
considering all excitations above the Hartree-Fock wave-
function

|ΨFCI⟩



i,α
Ciαa†
iaα +
X

i>j,α>β
Cijαβa†
ia†
jaαaβ + ...

I +
X

|ΨHF⟩,

(32)
where C are parameters to be optimised according to
the Rayleigh-Ritz variational principle.
The Rayleigh-
Ritz variational principle states that the energy expec-
tation value of a parametrized wavefunction is greater
than or equal to the lowest energy eigenvalue of the
Hamiltonian being measured. As considering all deter-
minants is classically intractable, the CI method is typ-
ically limited to including a small number of excitations
above the reference state: single excitations (CIS), dou-
ble excitations (CISD), and occasionally triple excita-
tions (CISDT). However, as low energy excitations domi-
nate the ground state wavefunction in many physical sys-
tems, these truncations can still produce good approxi-
mations to the ground state energy (Helgaker et al., 2014;
Szabo and Ostlund, 2012). The CI method is eﬀective at
recovering dynamic correlation, but less eﬀective at re-
covering static correlation (Helgaker et al., 2014). If the
reference state is a MCSCF state, the method is known
as multireference conﬁguration interaction, which seeks
to recover dynamic correlation on top of the static corre-
lation described by the MCSCF state.
The CI method suﬀers from two major limitations.
The method converges slowly to the full conﬁgura-
tion interaction wavefunction, as a result of its linear

## Page 16

parametrization. In addition, the energy obtained from
a truncated CI calculation does not scale correctly with
the system size. A calculation is said to produce ‘size
extensive’ results for an observable if the correct scaling
behaviour of that observable is obtained as the system is
scaled to the thermodynamic limit (Lyakh et al., 2012).
The energy obtained from a truncated CI calculation is
not size extensive.
Truncated CI calculations also fail
to satisfy a related property, known as ‘size consistency’.
Size consistency arises from multiplicative separability
of wavefunctions describing two non-interacting systems;
i.e. |AB⟩= |A⟩|B⟩for HAB = HA ⊕HB. One can easily
verify that this does not hold for truncated CI calcula-
tions.
Size consistency is important for obtaining the
correct behaviour from calculations to determine reac-
tion rates, as reactants at the beginning of the process
are considered non-interacting.

4. Coupled cluster

The coupled cluster (CC) method also includes addi-
tional determinants to recover the correlation energy, but
uses a product parametrization. The CC wavefunction is
given by


I + Ciαa†
iaα

×

|ΨCC⟩=
Y

i,α


I + Cijαβa†
ia†
jaαaβ

× ...|ΨHF⟩.
(33)

Y

i>j,α>β

This formula can be recast in an exponential form, writ-
ten as

|ΨCC⟩= eT |ΨHF⟩,
(34)

where T = P

i Ti,

i∈virt,α∈occ
tiαa†
iaα,

T1 =
X

i,j∈virt,α,β∈occ
tijαβa†
ia†
jaαaβ,

T2 =
X

(35)

...,

where occ denotes orbitals that are occupied in the
Hartree-Fock state, virt denotes orbitals that are unoccu-
pied (virtual) in the Hartree-Fock state, and t are excita-
tion amplitudes. When all of the excitation operators Ti
are included, the CC method recovers the full conﬁgura-
tion interaction wavefunction – however, performing this
calculation would be exponentially costly. As a result,
the method is normally truncated at a lower excitation
level, often single and double excitations (CCSD). The
canonical implementation of CCSD does not store the
wavefunction, as this would be exponentially costly (as
the CCSD wavefunction has support on all possible Slater

determinants). Instead, coupled non-linear equations can
be derived. The solution to these equations is the CCSD
approximation to the ground state (Helgaker et al., 2014;
Purvis and Bartlett, 1982). The time taken to solve these
equations scales as O((M −N)4N 2) (Purvis and Bartlett,
1982), while the memory needed to store the molecular
integrals needed scales as O(M 4).
For more accurate
results, the CCSD(T) method can be used, which treats
the triple excitations pertubatively, and scales in time ap-
proximately as O(M 7). There has been signiﬁcant work
to reduce these high computational costs, often introduc-
ing approximations which exploit the locality of dynami-
cal electron correlation in certain systems (Schutz, 2000;
Schutz and Werner, 2000). This has reduced the scaling
to be, in some cases, linear (Werner and Schutz, 2011).

Because of its product parametrization,
the CC
method generates a trial wavefunction which includes
all possible determinants,
albeit with an incorrect
parametrization.
It therefore provides faster conver-
gence than the conﬁguration interaction method.
The
product parametrization also ensures size extensivity
and size consistency.
However, the CC method is not
without its own shortcomings. Most notably, the wave-
function generated by the canonical CC method does not
obey the Rayleigh-Ritz variational principle (Helgaker
et al., 2014). While it is possible to formulate alternative
variants of the coupled cluster method,
which are
variational (Van Voorhis and Head-Gordon, 2000), these
are not as widely used by the computational chemistry
community.
Moreover, the conventional CC method
described above is a single determinant reference state
method. Consequently, it does not tend to perform well
when applied to multireference states, which are required
to treat systems with strong static correlation (Lischka
et al., 2018; Lyakh et al., 2012).
While there have
been eﬀorts to develop multireference coupled cluster
approaches, these have their own limitations, and are
not in widespread use, as discussed by Lyakh et al.
(2012).
In Sec. V.B we will describe a modiﬁed form
of the CC method, known as unitary coupled cluster
(UCC). This method is both variational and suitable for
multireference states.
While it is exponentially costly
to implement with a classical computer, this method is
eﬃcient to implement using a quantum computer.

This section has treated the inaccuracies which re-
sult from approximating the full conﬁguration interaction
wavefunction, while including all molecular orbitals. The
following section will discuss the converse case; we con-
sider only a limited number of molecular orbitals, but
assume that we include all possible determinants that
they can generate, unless explicitly stated.

## Page 17

D. Chemical basis sets

In this section, we describe some of the conventional
orbital basis sets used in classical computational chem-
istry. Throughout this section, we will refer to the ‘true’
orbitals of the system. These can be obtained by numer-
ically solving the Schr¨odinger equation using grid based
methods with a very ﬁne grid spacing, which is only pos-
sible for small atoms or simple molecules. The orbital
functions introduced in this section are approximations
of these true orbitals.
Although the Schr¨odinger equation can be solved ex-
actly for one electron atoms, the orbitals obtained be-
come diﬀuse too rapidly to accurately describe many-
electron atoms, especially close to the nuclei (Helgaker
et al., 2014). A better basis can be obtained by consider-
ing parametrized functions known as Slater-type orbitals
(STO)

RSTO
n
(r) ∝(ζr)n−1e−ζr,
(36)

where n is the energy level and ζ is a ﬁtting parameter.
By using diﬀerent values of ζ for each orbital, we can
generate a good basis (Helgaker et al., 2014). Unlike the
true atomic orbitals, these functions do not display oscil-
latory behaviour. Consequently, linear combinations of
STOs are required to approximate the true orbitals. It is
possible to only introduce a single basis function for each
considered orbital in the molecule, and give each basis
function a diﬀerent ζ value. This is known as a single-
zeta representation. Alternatively, we can introduce n
basis functions (where n is not the energy level of the
orbital, but a number deﬁning the number of basis func-
tions we wish to include), each with a diﬀerent ζ value,
for each orbital. This is known as an n-zeta representa-
tion. Introducing additional basis functions in this way
increases the radial ﬂexibility of the wavefunction. While
the STO functions exhibit many desirable features, they
make evaluating the two-electron integrals in Eq. (28)
computationally expensive.
To simplify the two-electron integrals, we can instead
use Gaussian basis functions. The Gaussian basis func-
tions are obtained by considering the Schr¨odinger equa-
tion with a three dimensional Harmonic oscillator poten-
tial. The form of a Gaussian-type orbital (GTO) is given
by

RGTO
nl
(r) ∝(√αnlr)le−αnlr2,
(37)

where αnl is a ﬁtting parameter and l denotes the an-
gular momentum quantum number of the orbital. Be-
cause of the dependence on r2 in the exponent, GTOs
are more localised than STOs. As a result, GTOs do not
approximate the atomic charge distribution as well as
STOs, so more are required to describe a given orbital.
However, this limitation is compensated by the ease of
integral evaluation. Furthermore, the disadvantages of

GTOs are less prominent in molecular calculations (Hel-
gaker et al., 2014).
The most common basis sets construct approximate
STOs from linear combinations of GTOs.
These ap-
proximate STOs are used as the basis functions for our
atomic orbitals. The number and type of orbitals deﬁnes
the basis set. There is a compromise between the accu-
racy obtained and the number of basis functions used.
The number of orbitals considered determines the run-
time and memory requirements of classical chemistry al-
gorithms. In the case of quantum computational chem-
istry, the number of basis functions determines the num-
ber of qubits and gate operations required to solve the
problem, which we will discuss explicitly in Sec. IV and
Sec. V, respectively.

1. STO-nG and split-valence basis sets

Some of the most simple bases are the STO-nG ba-
sis sets (Slater Type Orbital-n Gaussians) (Hehre et al.,
1969). In an STO-nG basis, each atomic orbital is consid-
ered to be an approximate STO. The STOs are approxi-
mated using n GTOs. STO-nG basis sets are often called
minimal basis sets, as they contain only the orbitals re-
quired to write the Hartree–Fock (HF) state (and those
orbitals of similar energy). Calculations using minimal
basis sets are of limited accuracy, giving only a qualita-
tive description of the system. It is important to note
that when carrying out a HF calculation in an STO-nG
basis, the true HF energy (i.e. the energy obtained by
performing a HF calculation using a grid based method,
on an inﬁnitely precise grid) will not be obtained, as the
STO-nG basis sets only approximate the true HF or-
bitals. As an example of an STO-nG basis set we con-
sider lithium, which has 3 electrons, of which 2 can reside
in the 1s orbital, leaving 1 in the second energy level. We
include in the minimal basis set {1s, 2s, 2px, 2py, 2pz} or-
bitals. We include both the 2s and 2p orbitals because
they are of the same energy level.
More accurate basis sets can be formed by adding in-
creased radial ﬂexibility to the valence orbitals (the or-
bitals of the highest occupied energy level), by consider-
ing a double-zeta representation of the valence orbitals.
This can be achieved using split-valence (Ditchﬁeld et al.,
1971) basis sets, such as the 6-31G basis. These basis sets
can be further improved by adding additional orbitals
with higher angular momenta, which make the angular
part of the wavefunction more ﬂexible. These orbitals are
called ‘polarisation functions’, as they describe the polar-
isation of atomic charge caused by bonding (for example,
the 6-31G* basis).

Although the aforementioned basis sets are too small
for calculations of such high accuracy that quantum com-
puters are warranted, it is important to discuss them
here, as they have been used extensively in the small ex-

## Page 18

perimental demonstrations possible on today’s quantum
hardware.

2. Correlation-consistent basis sets

Additional accuracy can be obtained by using cc-PVnZ
basis sets (correlation consistent polarised valence n
zeta), introduced by Dunning Jr. (1989). These include
additional unoccupied (‘virtual’) orbitals to recover the
correlation energy.
The virtual orbitals are generated
from correlated calculations on atoms. The core orbitals
have a single-zeta representation, while the valence or-
bitals have an n-zeta representation. The virtual orbitals
considered are polarisation functions, with higher angu-
lar momenta than the valence orbitals. The polarisation
functions are selected by the size of their contribution to
the correlation energy.

For atomic hydrogen in the cc-PVDZ (D = double,
so n = 2) the highest occupied energy level (the valence
level) is the ﬁrst level, and so we take a double-zeta rep-
resentation of the 1s state, considering {1s, 1s′} orbitals.
The 1s′ orbital is often referred to as a 2s orbital. This
is because the additional function chosen to describe the
valence orbital has the same angular momentum as the
ordinary 1s orbital, but is more diﬀuse – so it resembles
a 2s orbital.
We then include polarisation functions,
which have a higher angular momentum value than the
valence functions. In total, there are ﬁve basis functions
for cc-PVDZ hydrogen: {1s, 1s′, 2px, 2py, 2pz}.
For
lithium in the cc-PVDZ basis, the core orbital is {1s}.
The valence orbitals (which have a double-zeta repre-
sentation) are {2s, 2px, 2py, 2pz, 2s′, 2p′
x, 2p′
y, 2p′
z},
and the polarisation functions are {3dzz, 3dxz, 3dyz,
3dxy, 3dx2−y2 }, which we write as {5 × 3d}. This yields
14 basis functions.
For lithium in the cc-PVTZ basis
(T = triple so n = 3), we ﬁrst include the 14 orbitals
above. As we consider a triple-zeta representation of the
valence orbitals, we need additional {2s′′, 2p′′
x, 2p′′
y, 2p′′
z}
orbitals. We then include additional polarisation func-
tions; {5×3d′, 7×4f}. This leads to a total of 30 orbitals.

cc-PVnZ basis sets with higher values of n contain
orbitals that better approximate the true atomic orbitals
than those with lower n values.
However, even large
(n = 5) basis sets struggle to exactly represent the true
HF orbitals of simple molecules such as N2 (Helgaker
et al., 2014).
This limitation can be overcome by
measuring the ground state energy in several diﬀerent
cc-PVnZ bases, and then extrapolating to the basis set
limit.

FIG. 4 The orbitals included in diﬀerent basis sets for the
di-hydrogen molecule. The 1s′ orbital is often written as 2s.
The plots show the radial probability distributions for the true
Hydrogenic orbitals, which the basis orbitals approximate.

3. Plane wave basis sets

While the aforementioned basis sets have a long history
of use in classical computational chemistry (and as a re-
sult, early work in quantum computational chemistry),
they are not necessarily optimal basis sets for calcula-
tions performed on quantum computers.
While these
basis sets result in an accurate description of the sys-
tem with relatively few basis functions, they also lead to
Hamiltonians containing up to O(M 4) terms. As we will
see in Sec. V, the number of terms in the Hamiltonian
plays a key role in the cost of some quantum chemistry al-
gorithms. It is therefore interesting to question whether
there are basis sets that are more useful for quantum
computational chemistry. Two examples of such bases
are the plane wave and plane wave dual basis sets intro-
duced for quantum computing by Babbush et al. (2018c).
The plane wave basis functions, φν(r), are given by

r

1
V exp
2πiνr


,
(38)

φν =

L

for a plane wave with wavevector corresponding to the
νth harmonic of the computational cell with length L
and volume V . The plane wave dual basis is obtained by
taking the discrete Fourier transform of the plane wave
basis states, so are like a smooth approximation to a
grid (Babbush et al., 2018c). These basis sets diagonalise
the kinetic and potential operators, respectively. This re-
duces the number of Hamiltonian terms from O(M 4) to
O(M 3) in the plane wave basis, and O(M 2) in the plane
wave dual basis. This in turn leads to a reduction in the
asymptotic scaling of quantum chemistry algorithms to
ﬁnd the ground state energy of molecules and solid state
systems (we will discuss the magnitude of this poten-
tial speedup in Sec. V). These plane wave basis sets are
well suited to periodic systems, and have a long history

## Page 19

of use in classical density functional theory calculations.
However, to describe molecular systems, approximately
10 to 100 times as many plane wave basis functions are
required as GTOs (Babbush et al., 2018c).
A similar reduction in the number of Hamiltonian
terms can be obtained using gausslet basis sets (White,
2017), or ‘discontinuous Galerkin’ sets (McClean et al.,
2019a), which can both require fewer functions to ac-
curately describe individual molecules than plane wave
basis sets. Creating eﬃcient basis sets for quantum com-
putational chemistry remains an open and fundamental
area of research.

E. Reduction of orbitals

It is sometimes the case that certain orbitals are very
likely to be either occupied or virtual in all Slater deter-
minants in the wavefunction. As calculating the ground
state energy is essentially a question of distributing elec-
trons among orbitals, we can simplify our calculation by
using this information. Speciﬁcally, we are able to re-
move spin-orbitals from the calculation if their expected
occupation number is close to 0 or 1. Our calculation is
reduced to including only the most important (ambigu-
ously occupied) orbitals. This is known as performing
the calculation in a reduced active space.
In order to determine the occupation of orbitals, we
can use the reduced density matrices (RDMs) of the sys-
tem. The expectation value of any 1- or 2-electron Hermi-
tian operator, O, with a state |Ψ⟩= P

f αf |f⟩, is given
by (Helgaker et al., 2014)

⟨Ψ| O |Ψ⟩=
X

i,j
Oijρ1
ij +
X

i,j,k,l
Vijklρ2
ijkl,

ρ1
ij = ⟨Ψ| a†
iaj |Ψ⟩,
ρ2
ijkl = ⟨Ψ| a†
ia†
kalaj |Ψ⟩,
(39)

where ρ1 is the single-particle reduced density matrix (1-
RDM), ρ2 is the two-particle reduced density matrix (2-
RDM), and Oij and Vijkl are deﬁned in a similar way to
the coeﬃcients in Eq. (28). When eliminating orbitals in
this way, the RDMs are deﬁned with respect to a state
which is an approximation of the ground state, which
could be the results of a classically tractable conﬁgu-
ration interaction or coupled cluster calculation. These
RDMs contain all of the information required to evalu-
ate ⟨O⟩Ψ. From the deﬁnition above, we can see that the
diagonal elements of ρ1 are the expectation values of the
number operator for the corresponding orbitals. As ρ1 is
a Hermitian operator, we can diagonalise it with a uni-
tary transform. This is a basis change from the canonical
orbitals to the ‘natural molecular orbitals’. The diago-
nal elements of the basis transformed ρ1 are called the
natural orbital occupation numbers (NOONs).
Spin-orbitals with a NOON close to 0 or 1 (compared
to the other NOONs) can be assumed to be empty or

occupied, respectively.
Occupied orbitals are typically
referred to as ‘core’ orbitals, while the empty orbitals are
known as ‘virtual’ orbitals. As a result, we can reduce our
problem by considering only the ambiguously occupied
orbitals. In Sec. VII we provide an explicit example of
how this method can be used to reduce the number of
orbitals required to simulate lithium hydride in an STO-
3G basis set.

Takeshita et al. (2019) showed how to re-integrate
some of the energy contribution of the virtual orbitals
into a quantum simulation, without requiring additional
qubits to represent the virtual orbitals. Their method
utilises an increased number of measurements,
and
classical post-processing. We will describe this method
in more detail in Sec. V.C.1.
Those authors also
provide a technique to improve the energy estimate
from a calculation by optimising the active space using
orbital rotations, as is done in MCSCF calculations
(Sec. III.C.2).

This section has introduced the concepts in classical
computational chemistry necessary to understand how
quantum computers can be used for chemical simulation.
The following sections introduce methods developed to
solve chemistry problems using quantum computers. We
return to classical computational chemistry methods in
Sec. VIII.A, where we assess the strengths, weaknesses,
and computational limits of the methods introduced here.

IV. QUANTUM COMPUTATIONAL CHEMISTRY
MAPPINGS

In this section, we describe the techniques developed
to enable quantum computers to represent problems in
chemistry.
In Sec. IV.A and Sec. IV.B we introduce
methods for encoding fermions into qubits (both in ﬁrst
and second quantisation).
We then describe methods
which utilise knowledge of the structure of chemistry
problems to reduce the resources required, in Sec. IV.C.
As discussed in Sec. III.B the distinguishing feature be-
tween ﬁrst and second quantised methods is whether an-
tisymmetry is enforced in the wavefunction directly (ﬁrst
quantised), or in the behaviour of the operators which act
on the wavefunction (second quantised). As in the pre-
vious section, we consider a system with M spin-orbitals
(when discussing basis set approaches) and N electrons.
We summarise the number of qubits required to store the
wavefunction in each of the representations in Table I.

In order to make the mappings more clear, we show
how the wavefunction would look under each mapping for
a ﬁctitious system. When considering a basis set map-
ping of this system, we consider spin-orbitals |A↑⟩, |A↓⟩,
|B↑⟩, |B↓⟩. We are free to arbitrarily deﬁne the Hartree-
Fock state of our ﬁctitious system, and choose it to be
both electrons in the |A⟩orbital. We are interested in the

## Page 20

TABLE I The number of qubits required to store the wave-
function using the diﬀerent encoding methods.
M is the
number of spin-orbitals used in a basis set simulation, N
is the number of simulated particles in the problem, and
m = log2(P), where P is the number of grid points per axis
for a grid based simulation. The number of qubits can often
be further reduced, as discussed in Sec. IV.C.1.

wavefunction when the z component of the spin is zero.
When considering a grid based approach, for the sake of
simplicity we consider spinless electrons on a 1D grid.
The two single particle wavefunctions considered are ap-
proximately ‘n’ shaped (see Eq. (41)) and ‘u’ shaped (see
Eq. (42)).

A. First quantised encoding methods

Here we give an overview of ﬁrst quantised quantum
simulation, which can be carried out using either a dis-
crete single-particle basis, or grid based methods.

1. Grid based methods

As discussed in Sec. III.B.1, the wavefunction of an
N-particle system can be represented in real space on a
discretised grid of P points per axis, and is given by

|Ψ⟩=
X

x1,...,xN
ψ(x1, . . . , xN)A (|x1, . . . , xN⟩) ,
(40)

where |xi⟩= |ri⟩|σi⟩is a spatial and spin-coordinate,
|ri⟩
=
|xi⟩|yi⟩|zi⟩, ∀i
∈
{1, 2, . . . , N},
xi, yi, zi
∈
{0, 1, . . . , P −1}, and σ ∈{0, 1}.
We consider the
case where P = 2m, where m is an arbitrary num-
ber which determines the precision of our simulation.
While it is classically intractable to store the required
P 3N×2N = 2(3m+1)N complex amplitudes for large quan-
tum systems, it is possible using a quantum computer.
If we write the basis vector |x = 2m −1⟩in binary as
|11....11⟩, we can see that it only requires m bits. An
m qubit register can be in a superposition of 2m pos-
sible states.
As a result, it only requires (3m + 1)N
qubits to store the N electron wavefunction described by
Eq. (40). Using a grid based method, rather than basis
sets, means that the Born-Oppenheimer approximation
is not required.
As a result, we are able to treat the
electrons and nuclei on an equal footing using grid based
methods, which can be important for systems undergoing
reactions.

In order to make the ﬁrst quantised grid based map-
ping more understandable, we consider three example
wavefunctions. Without loss of generality, we neglect the
spin coordinate of the electrons, and consider only a sin-
gle spatial dimension for each electron. The ﬁrst example
considers a single spinless electron, on a four point grid.
The ‘n’-shaped wavefunction considered is given by

|ϕ⟩=
1
√

6 |00⟩+ 1
√

3 |01⟩+ 1
√

3 |10⟩+ 1
√

6 |11⟩

6 |3⟩
(41)

=
1
√

6 |0⟩+ 1
√

3 |1⟩+ 1
√

3 |2⟩+ 1
√

and can be stored using two qubits. The second exam-
ple considers an antisymmetrised product state of two
electrons, where one electron is in the state |ϕ⟩, and the
other has a ‘u’-shaped wavefunction

|φ⟩=
1
√

3 |0⟩+ 1
√

6 |1⟩+ 1
√

6 |2⟩+ 1
√

3 |3⟩.
(42)

The pair wavefunction is then given by

|Φ⟩= 1
√

2 (|ϕ⟩1 |φ⟩2 −|φ⟩1 |ϕ⟩2) ,

= 1

6
√

2(|1⟩1 |0⟩2 −|0⟩1 |1⟩2 + |1⟩1 |3⟩2 −|3⟩1 |1⟩2

+ |2⟩1 |0⟩2 −|0⟩1 |2⟩2 + |2⟩1 |3⟩2 −|3⟩1 |2⟩2),
(43)
where the subscripts label the electrons. In general, an
entangled state of two spinless electrons on a P point 1D
grid can be written in this way as

P −1
X

P −1
X

|Ψ⟩=

j=0
ψij (|i⟩1 |j⟩2 −|j⟩1 |i⟩2) ,
(44)

i=0

where again, the subscripts label the electrons.

Grid based methods were ﬁrst introduced for the quan-
tum simulation of general quantum systems by Wiesner
(1996) and Zalka (1998). They were then adapted for
simulating problems in chemistry by Lidar and Wang
(1999) and Kassal et al. (2008). Physically relevant states
can then be prepared using the algorithms outlined by
Ward et al. (2009). Kassal et al. (2008) showed how to
time evolve the wavefunction under the electronic stuc-
ture Hamiltonian. As we will discuss in Sec. V.A, time
evolution is a key subroutine of algorithms that ﬁnd the
ground states of chemical systems. Finally, the relevant
observables can be measured (Kassal et al., 2008; Whit-
ﬁeld, 2015). A thorough investigation of the resources
required to perform these simulations in a fault-tolerant
manner was carried out by Jones et al. (2012). The time
evolution algorithm of Kassal et al. (2008) was subse-
quently made more eﬃcient by Kivlichan et al. (2017),
who also performed a more thorough analysis of both
gate counts and errors. We will discuss the method used
by Kivlichan et al. (2017) in more detail in Sec. V.A.4.

## Page 21

Although the spatial resolution of grid based methods
increases exponentially with the number of qubits used,
it is not possible to use this to exponentially improve the
accuracy of the calculation. This is because all known
grid based algorithms have gate counts which scale poly-
nomially with the inverse grid spacing. As a result, any
attempt to exponentially increase the simulation accu-
racy by exponentially reducing the grid spacing causes
the gate count to increase exponentially. Kivlichan et al.
(2017) also showed that there exist systems where the
grid spacing must decrease exponentially with the num-
ber of particles in the system to maintain constant accu-
racy. Consequently, these systems are not eﬃcient to sim-
ulate using this method. However, those authors noted
that such pathological cases can also exist for basis set
methods, but are typically dealt with eﬃciently using a
clever choice of basis function.
The simulation of chemical systems using a grid based
method can require considerably more qubits than in ba-
sis set approaches. For example, it would require 96 logi-
cal qubits to store the position of a single spinless particle
to 32 bits of accuracy using a grid based approach. This
can be contrasted with basis set approaches, where in-
teresting molecules or Fermi-Hubbard models could be
simulated with around 100 logical qubits (as we will dis-
cuss in Sec. VIII.B). Consequently, grid based approaches
are typically considered unsuitable for near-term quan-
tum computers, which will have relatively few qubits.

2. Basis set methods

The original algorithm for simulating quantum systems
in the ﬁrst quantisation using a discrete basis was given
by Abrams and Lloyd (1997). If we consider M single-
particle basis functions (such as the molecular orbitals
or lattice spin sites described in Sec. III.B.2), we can
enumerate these from 0 to M−1. We can store these spin-
orbitals using ⌈log2(M)⌉qubits, denoting spin-orbital 0
as |0...00⟩, spin-orbital 1 as |0...01⟩and so on, such that
spin-orbital M −1 is represented as |1...11⟩. We then use
N registers of these ⌈log2(M)⌉qubits (one register for
each electron) to describe the states of all of the electrons
in the system. As a result, it requires N⌈log2(M)⌉qubits
to store the wavefunction.
If we consider a product state generated by each elec-
tron being in a single orbital, we observe that the wave-
function does not have the correct antisymmetry.
As
such, it must be antisymmetrised. The original approach,
by Abrams and Lloyd (1997), accomplished this using
O(N 2log2
2(M)) gates and O(Nlog2(M)) ancilla qubits.
This was improved by Berry et al. (2018), who used a
circuit with O(Nlogc
2(N)log2(M)) gates, with a depth of
O(logc
2(N)log2log2(M)), where c ⩾1 and depends on the
choice of sorting network used, and O(Nlog2(N)) ancilla
qubits.

where

We can apply the ﬁrst quantised basis set mapping
to the ﬁctitious system described above.
We ﬁrst la-
bel each of the orbitals:
|A↑⟩= |00⟩= |0⟩, |A↓⟩=
|01⟩= |1⟩, |B↑⟩= |10⟩= |2⟩, |B↓⟩= |11⟩= |3⟩. The
Hartree-Fock state has both electrons in the |A⟩orbitals.
An incorrectly symmetrised HF state would therefore
be |A↑⟩1 |A↓⟩2 = |0⟩1 |1⟩2, where the subscripts denote
which electron each orbital describes. The correctly an-
tisymmetrised HF wavefunction would be

|ΨHF⟩=
1
√

2(|0⟩1 |1⟩2 −|1⟩1 |0⟩2).
(45)

If we now consider excitations above the HF state, then a
general wavefunction with sz = 0 that has been correctly
antisymmetrised is given by

|Ψ⟩= α
√

2 (|0⟩1 |1⟩2 −|1⟩1 |0⟩2)

+ β
√

2 (|2⟩1 |3⟩2 −|3⟩1 |2⟩2)

(46)

+ γ
√

2 (|0⟩1 |3⟩2 −|3⟩1 |0⟩2)

+ δ
√

2 (|1⟩1 |2⟩2 −|2⟩1 |1⟩2) .

As we have N = 2 electrons, and M = 4 spin-orbitals,
we can see that we only require N⌈log2(M)⌉= 2 ×
⌈log2(4)⌉= 4 qubits to store the wavefunction.

The Hamiltonian can be obtained by projecting it onto
the single-particle basis functions

M−1
X

N
X

α,β=0
hαβ |φβ⟩i ⟨φα|i

H =

i=1

(47)

M−1
X

N
X

+ 1

α,β,γ,δ
hαβγδ |φα⟩i |φβ⟩j ⟨φγ|j ⟨φδ|i ,

2

i̸=j

!

−∇2

ZI
|r −RI|

hαβ =
Z
dxφ∗
β(x)

2 −
X

φα(x),

I

hαβγδ =
Z
dx1dx2
φ∗
α(x1)φ∗
β(x2)φγ(x2)φδ(x1)

|r1 −r2|
.

(48)
For example, if we denote terms in the ﬁrst sum of
Eq. (47) as Hi
φαφβ, and consider our model system with
spin-orbitals φα = {|A↑⟩, |A↓⟩, |B↑⟩, |B↓⟩}, then the term
H1
A↑B↑(which acts on electron 1) is given by

hA↑B↑|B↑⟩e1 ⟨A↑|e1 =

hA↑B↑|10⟩e1 ⟨00|e1 =

hA↑B↑(|1⟩q3 ⟨0|q3) ⊗(|0⟩q2 ⟨0|q2) =

(49)

1

2(Xq3 −iYq3)

⊗
1

2(Iq2 −Zq2)

=

hA↑B↑

hA↑B↑

4
(Xq3Iq2 −iYq3Iq2 −Xq3Zq2 + iYq3Zq2),

## Page 22

where ei denotes electron i, qi denotes the ith qubit
(counting from the right), X, Y, Z, I are the Pauli op-
erators introduced in Sec. II.A, and hA↑B↑is given by
the ﬁrst integral in Eq. (48). There are up to O(N 2M 4)
possible 2-body terms, each leading to up to O(22log2(M))
Pauli terms – meaning the Hamiltonian can contain up to
O(N 2M 6) Pauli terms, which are up to 2log2(M)-local.

Once the Hamiltonian has been obtained, we can use it
to time evolve the wavefunction, which maintains the cor-
rect antisymmetry (Abrams and Lloyd, 1997). As men-
tioned previously, and shown in Sec. V.A, time evolution
is a key subroutine of algorithms to ﬁnd the ground state
of chemical systems.

B. Second quantised basis set encoding methods

To simulate chemical systems in the second quantised
representation on a quantum computer, we need to
map from operators which act on indistinguishable
fermions to operators acting on distinguishable qubits.
An encoding method is a map from the fermionic Fock
space to the Hilbert space of qubits, such that every
fermionic state can be represented by a qubit state.
There are multiple methods of encoding, which we
describe below. In the following section, we only discuss
second quantised basis set methods, as second quantised
grid based methods have only brieﬂy been discussed in
the context of quantum computational chemistry (see
Babbush et al. (2018c) Appendix A).

1. Jordan-Wigner encoding

In the Jordan–Wigner (JW) encoding (Jordan and
Wigner, 1928), we store the occupation number of a spin-
orbital in the |0⟩or |1⟩state of a qubit (unoccupied and
occupied, respectively). More formally,

|fM−1, fM−2, . . . , f0⟩→|qM−1, qM−2, . . . , q0⟩,

qp = fp ∈{0, 1}.
(50)

The fermionic creation and annhilation operators in-
crease or decrease the occupation number of a spin-
orbital by 1, and also introduce a multiplicative phase
factor (see Eq. (25)). The qubit mappings of the opera-
tors preserve these features, and are given by,

ap = Qp ⊗Zp−1 ⊗· · · ⊗Z0,

a†
p = Q†
p ⊗Zp−1 ⊗· · · ⊗Z0,
(51)

where Q = |0⟩⟨1| =
1
2(X + iY ) and Q† = |1⟩⟨0| =
1
2(X−iY ). The Q or Q† operator changes the occupation
number of the target spin-orbital, while the string of Z
operators recovers the exchange phase factor (−1)
Pp−1
i=0 fi.
We refer to the action of the Z operators as ‘computing

the parity of the state’.
Using the JW encoding, the
second quantised fermionic Hamiltonian is mapped to a
linear combination of products of single-qubit Pauli op-
erators

i
σj
i ,
(52)

H =
X

j
hjPj =
X

j
hj
Y

where hj is a real scalar coeﬃcient, σj
i represents one of
I, X, Y or Z, i denotes which qubit the operator acts on,
and j denotes the term in the Hamiltonian. Each term
Pj in the Hamiltonian is typically referred to as a ‘Pauli
string’, and the number of non-identity single-qubit Pauli
operators in a given string is called its ‘Pauli weight’. All
of the second quantised encoding methods discussed in
this section produce Hamiltonians of this form. An ex-
ample JW mapping is shown in Table. II. In order to
further clarify the second quantised JW encoding, we
apply it to the ﬁctitious system described earlier.
As
stated previously, we assume that the Hartree-Fock state
for this system has both electrons occupying the |A⟩or-
bitals. We store the occupations of the spin-orbitals |A↑⟩,
|A↓⟩, |B↑⟩, |B↓⟩, which we order as |fB↓, fB↑, fA↓, fA↑⟩,
with fi = 0, 1. The Hartree-Fock state is then given by

|ΨHF⟩= |0011⟩.
(53)

This state corresponds to the antisymmetrised Slater de-
terminant shown in Eq. (45). The sz = 0 wavefunction
is then

|Ψ⟩= α |0011⟩+ β |1100⟩+ γ |1001⟩+ δ |0110⟩.
(54)

This state can be compared with the ﬁrst quantised
basis set mapping shown in Eq. (46).
Working in the
JW basis, it is easy to see the advantage that quantum
computers have over their classical counterparts for
chemistry problems.
As discussed in Sec. III.B.2, the
full
conﬁguration
interaction
wavefunction
contains
a number of determinants which scales exponentially
with the number of electrons, as roughly O(M N). As
such, it requires an amount of memory that scales
exponentially with the system size.
However, using
a quantum computer, we can instead store the full
conﬁguration interaction (FCI) wavefunction using only
M qubits (Aspuru-Guzik et al., 2005). A register of M
qubits can be in a superposition of 2M computational
basis states. In the JW basis, every Slater determinant
required for the FCI wavefunction can be written as one
of these computational basis states. As such, quantum
computers can eﬃciently store the FCI wavefunction.
This is also true for the other second quantised encodings.

The primary advantage of the JW encoding is its sim-
plicity. However, while the occupation of a spin-orbital is
stored locally, the parity is stored non-locally. The string
of Z operators means that a fermionic operator mapped

## Page 23

TABLE II Example mappings of a fermionic Fock state and its fermionic operators onto the corresponding qubit state, and
qubit operators. ˆni is the fermionic number operator.

to qubits generally has a weight of O(M) Pauli operators,
each acting on a diﬀerent qubit.
An alternative to the JW mapping that has not yet
found particular use within the ﬁeld, but is worth the
reader being aware of, is the parity encoding. This ap-
proach stores the parity locally, and the occupation num-
ber non-locally. We use the pth qubit to store the parity
of the ﬁrst p modes,

|fM−1, fM−2, . . . , f0⟩→|qM−1, qM−2, . . . , q0⟩,

qp =

p
X


(mod 2).
(55)

i=0
fi

The transformed creation and annihilation operators are
described by Seeley et al. (2012).
An example of the
parity mapping is shown in Table. II.

2. Bravyi–Kitaev encoding

The Bravyi–Kitaev (BK) encoding (Bravyi and Ki-
taev, 2002) is a midway point between the JW and parity
encoding methods, in that it compromises on the local-
ity of occupation number and parity information. The
orbitals store partial sums of occupation numbers. The
occupation numbers included in each partial sum are de-
ﬁned by the BK matrix, βpq.

|fM−1, fM−2, . . . , f0⟩→|qM−1, qM−2, . . . , q0⟩,

" p
X

#

(mod 2).
(56)

qp =

q=0
βpqfq

It is deﬁned recursively (Bravyi and Kitaev, 2002; Seeley
et al., 2012) via

β1 = [1],





,
(57)

β2x
0

β2x+1 =

A
β2x

where A is an (2x ×2x) matrix of zeros, with the bottom
row ﬁlled with ones, and 0 is a (2x × 2x) matrix of zeros.
As an example, when M = 4 (x = 1), the matrix βpq is





1 0 0 0

















1 1 0 0

β4 =

.
(58)

0 0 1 0

1 1 1 1

When the number of qubits is not a power of two, the
BK encoding is carried out by creating the BK matrix
for the next largest power of two, and only using the
ﬁrst M rows. The qubit operators for the BK encoding
are considerably more complicated than those in the JW
or parity encodings. We refer to Table II for an exam-
ple, and works by Seeley et al. (2012) and Tranter et al.
(2015) for a more detailed discussion. Applying the BK
mapping to a fermionic operator results in a qubit op-
erator with a Pauli weight of O(log2 M).
A thorough
comparison of the BK and JW mappings was performed
by Tranter et al. (2018) for 86 molecular systems. They
found that the BK transform was at least as eﬃcient, in
general, as the JW transform when ﬁnding the ground
states of the molecular systems. In many cases using the
BK transform made the calculations considerably more
eﬃcient.

Another version of the BK encoding also exists in the
literature.
This is referred to as the BK-tree method,
as it takes its inspiration from a classical data structure
known as a Fenwick tree (Havlicek et al., 2017). We ex-
plicitly show how to use this mapping with molecules in
Sec. VII. As with the standard BK mapping, the BK-tree
encoding balances how it stores occupation and parity
information. As a result, it too only requires O(log2 M)
qubit operations to realise a fermionic operator, in gen-
eral. However, there are subtle diﬀerences between the
two mappings. It has been noted that the BK-tree map-

## Page 24

ping produces qubit operators with a greater weight than
the standard BK mapping (Sung, 2018). This would sug-
gest that it is less suitable for near-term quantum com-
putation. However, the BK-tree mapping also possesses
advantages over the standard BK encoding. The BK-tree
mapping is uniquely deﬁned even when the number of or-
bitals, M, is not a power of 2. As a result, when using the
BK-tree mapping we are always able to use the qubit re-
duction by symmetry technique, which we will discuss in
Sec. IV.C. We have observed that it is only possible to use
this technique with the standard BK mapping when the
number of orbitals is a power of two. As a result, it is im-
portant to consider the beneﬁts of both mappings, before
choosing which one to use. A further generalisation of
the BK-tree encoding is to consider ternary trees (Jiang
et al., 2019), which leads to asymptotic reductions in the
Pauli weight of Hamiltonian terms.

3. Locality preserving mappings

Mappings have been developed which endow the
qubit operators with the same locality as the underlying
fermionic
Hamiltonian.
These
mappings
typically
require more qubits than the JW encoding. Verstraete
and Cirac (2005) developed a scheme to eliminate
the strings of Z
operators introduced by the JW
transform, resulting in qubit operators with the same
locality as the fermionic operators.
This is achieved
by doubling the number of qubits.
Similar ideas were
introduced by Ball (2005) and Farrelly and Short (2014).
These ideas were later generalised and expanded upon by
Steudtner and Wehner (2018) and Whitﬁeld et al. (2016).

There is also another variant of the BK trans-
form, known as the Bravyi-Kitaev superfast transform
(BKSF) (Bravyi and Kitaev, 2002). This mapping ﬁrst
represents each spin-orbital by a vertex on a graph, and
each interaction term in the Hamiltonian as an edge on
the graph. Qubits are then associated to the edges. In
general, a graph will have more edges than vertices, so
this increases the number of qubits required. However,
the number of gates required to implement a fermionic
operator will scale as O(d) where d is the degree of the
graph. Assuming fairly local interactions for a molecule,
the degree of the graph will be less than the number of
vertices. As a result, the BKSF transform may require
fewer gates than the JW mapping. We refer the reader to
the work of Chien et al. (2019) and Setia and Whitﬁeld
(2018) for a detailed discussion of the BKSF transform,
and comparison to the JW transform. The BKSF trans-
form has been generalised (Setia et al., 2018) to either:
1) Reduce the weight of each of the Pauli operators in the
Hamiltonian to O(log d), or 2) Provide some protection
from errors.
A related mapping, known as the majo-
rana loop stabilizer code, was introduced by Jiang et al.

(2018a). It also preserves the locality of the underlying
model, and oﬀers some protection from errors. We will
discuss this error detecting/correcting property in more
detail in Sec. VI.D.

C. Resource reduction

In this section, we focus on general techniques that
can be used to reduce the resources required for quantum
chemistry simulation. In particular, we focus on methods
to remove qubits from the simulation using symmetries,
and low rank decomposition methods for reducing the
cost of quantum circuits.

1. Hamiltonian reduction

We focus on techniques to reduce the number of qubits
required for the second quantised approach, using Z2
symmetries. More general qubit reduction schemes have
also been developed (Bravyi et al., 2017), but these have
yet to be numerically or experimentally investigated.
In the JW, parity and BK encoding methods, the num-
ber of qubits is equal to the number of spin-orbitals
considered, M. However, as the Hamiltonian possesses
symmetries, the wavefunction can be stored in a smaller
Hilbert space.
Here, we will describe the method by
Bravyi et al. (2017), which utilises two such symmetries:
conservation of electron number and spin. This method
enables the systematic reduction of two qubits when us-
ing the parity, BK (with the caveat that the number of
orbitals is a power of two), or BK-tree encoding. For a
system with M spin-orbitals, we can arrange the orbitals
such that the ﬁrst M/2 spin-orbitals describe spin up
states, and the last M/2 spin-orbitals describe spin down
states. For non-relativistic molecules, the total number
electrons and the total sz value are conserved. Exam-
ining the BK matrix presented in Eq. (58), we see that
every element in the ﬁnal row is one, and the ﬁrst half
of the elements in the M/2th row are also one. Conse-
quently, the ﬁnal element of the vector encoded by this
matrix, qM−1, is equal to the number of electrons (mod
2). Similarly, the M/2th element in the encoded vector,
q M

2 −1, is equal to the number of spin up electrons (mod
2). As the electron number and total sz value are con-
served by the Hamiltonian, these qubits are only acted
on by the identity or Pauli Z operators.
We can re-
place these operators by their corresponding eigenvalues
(+1 for the identity, +1 for ZM−1 if the total number
of electrons is even, −1 for ZM−1 if the total number of
electrons is odd, +1 for Z M

2 −1 if the number of spin up
electrons is even, and −1 for Z M

2 −1 if the number of spin
up electrons is odd).
The Hamiltonian then only acts
on (M −2) qubits, so two qubits can be removed from
the simulation. Exactly the same method can be used

## Page 25

for the parity and BK-tree encodings. We will explicity
show how this method can be used to remove two qubits
from chemical Hamiltonians in Sec. VII. We remark that
while this transformation leaves the ground state of the
system unchanged, it does alter the excited states that
can be found. In particular, we are restricted to ﬁnding
those states with an electron number and total sz value
equal to the values determined as described above. These
techniques have been extended by Setia et al. (2019) to
include molecular point group symmetries.

2. Low rank decomposition techniques

As discussed in Sec. III.A, the electronic structure
Hamiltonian in the canonical molecular orbital basis con-
tains O(M 4) terms, where M is the number of spin-
orbitals in the molecule. This means that many quantum
circuits implementing time evolution under the molecular
Hamiltonian naively scale in a similar way. As we shall
discuss in Sec. V.A and Sec. V.B, such circuits are a key
component of many quantum algorithms. Motta et al.
(2018) utilised a low rank decomposition of the Hamilto-
nian in a Gaussian orbital basis to reduce the cost of time
evolution. This decomposition is made possible by the
structure present in the molecular Hamiltonian, which
arises from the pairwise nature of the electron-electron
interactions. Those authors leveraged a doubly factorised
Cholesky decomposition of the Hamiltonian, with an eﬃ-
cient quantum circuit implementation. By carefully trun-
cating the number of terms in the decomposition, they
were able to reduce the cost of time evolution, with a
controllable error. Similar decompositions were also in-
troduced for other quantum circuits of interest. We will
discuss the impact of these cost reductions in more detail
in Sec. V.A and Sec. V.B.

This low rank decomposition technique was also used
by Huggins et al. (2019b), to reduce the number of
circuit repetitions required for variational algorithms to
ﬁnd the ground state energy of chemical systems. We
discuss this technique in more detail in Sec. V.B.2.

We note that most of the work to date in quantum
computational chemistry has focused on second quan-
tised basis set methods. While ﬁrst quantised basis set
simulations require asymptotically fewer qubits than sec-
ond quantised basis set simulations, for the smallest sim-
ulable systems (such as small molecules in minimal basis
sets), second quantised basis set methods require either
fewer qubits and/or shorter gate sequences.
This has
caused second quantised basis set methods to become
the de facto option for experimental demonstrations of
quantum computational chemistry algorithms, due to the
limits of current quantum hardware.

V. QUANTUM COMPUTATIONAL CHEMISTRY
ALGORITHMS

In this section, we focus on methods used to solve the
electronic structure problem with a quantum computer.
We describe the quantum phase estimation algorithm
and related methods in Sec. V.A. We then discuss the
variational quantum eigensolver (VQE) in Sec. V.B. Both
of these sections are concerned with ﬁnding the ground
state energies of chemical systems. We conclude this sec-
tion with a discussion of methods that can be used to
ﬁnd excited states in Sec. V.C.

As mentioned in Sec. I, the techniques developed for
solving the electronic structure problem can often be gen-
eralised to solve other problems in computational chem-
istry.
For example, O’Brien et al. (2019) showed how
to calculate the energy derivatives of molecular Hamil-
tonians (which can be used for geometry optimisation
and transition state discovery) by using algorithms based
on phase estimation (Sec. V.A), or based on a linear re-
sponse quantum subspace expansion (Sec. V.C.1). The
same properties can also be calculated using the method
of Mitarai et al. (2019), who leveraged the variational
quantum eigensolver (Sec. V.B), with analytic gradient
measurements (Sec. V.B.3), and by Parrish et al. (2019a)
who used the contraction VQE method (Sec. V.C.3).

It can be argued that the VQE and phase estimation,
as presented herein, represent near-term and long-term
methods (respectively) for solving chemistry problems
with a quantum computer. However, in reality, aspects
of each algorithm can be incorporated into the other,
creating new methods (Wang et al., 2018; Yung et al.,
2014) which occupy the intermediate region in the
quantum computational chemistry timeline. Algorithms
to ﬁnd the ground state using methods which diﬀer
from both phase estimation and the VQE have also
been proposed such as techniques based on time series
estimation (O’Brien et al., 2018a; Somma et al., 2002;
Somma, 2019), or the method by Ge et al. (2017).

A. Quantum phase estimation

1. Implementation

Phase estimation (Kitaev, 1995) can be used to ﬁnd
the lowest energy eigenstate, |E0⟩, and excited states,
|Ei>0⟩, of a physical Hamiltonian (Abrams and Lloyd,
1999). In the case of quantum computational chemistry,
this qubit Hamiltonian can encode a fermionic Hamilto-
nian, obtained using the methods discussed in Sec. IV.
The canonical phase estimation algorithm is described
as follows (Nielsen and Chuang, 2002), and shown in
Fig. 5.

1. We initialise the qubit register in state |Ψ⟩, which

## Page 26

FIG. 5 The canonical quantum phase estimation circuit with
three ancilla qubits. When the ancilla qubits are in state |x⟩,
a control rotation e−2πiHx is applied to the target state |Ψ⟩.
QFT denotes the quantum Fourier transform (Coppersmith,
1994; Shor, 1994).
By measuring the ancilla qubits in the
computational basis, they collapse to an eigenvalue of H and
the register qubits collapse to an estimate of the correspond-
ing energy eigenstate.

has non-zero overlap with the true full conﬁgura-
tion interaction (FCI) target eigenstate state of the
system. We require an additional register of ω an-
cilla qubits. We can expand the state |Ψ⟩in terms
of energy eigenstates of the Hamiltonian, writing
that |Ψ⟩= P

i ci |Ei⟩, where ci are complex coeﬃ-
cients.

2. We apply a Hadamard gate to each ancilla qubit,
placing the ancilla register in the superposition
1
√

2ω
P
x |x⟩, where x are all possible bit-strings that
can be constructed from ω bits. We then apply the
controlled gates shown in Fig. 5:

1
√

x
|x⟩ci |Ei⟩→
1
√

2ω
X

X

2ω
X

X

x
e−2πiEixci |x⟩|Ei⟩.

i

i

(59)

3. We apply the inverse quantum Fourier transform
to the ancilla qubits in order to learn the phase,
which encodes the information about the energy
eigenvalue:

1
√

x
e−2πiEixci |x⟩|Ei⟩
QFT−1
−−−−−→
X

2ω
X

X

i
ci |bin(Ei)⟩|Ei⟩.

i

(60)

4. We measure the ancilla qubits in the Z basis, which
gives an estimate of the energy eigenvalue as a
binary bit-string, bin(Ei), with probability |ci|2.
This procedure collapses the main register into the
corresponding energy eigenstate, |Ei⟩.

The number of ancilla qubits, ω, required for the
method of phase estimation described above is deter-
mined by the desired success probability and precision in
the energy estimate. Nielsen and Chuang (2002) showed
that to obtain a binary estimate of the energy, precise to
n bits, with success probability p, requires

ω = n +

log2


2 + 1


(61)

2p

ancilla qubits. Phase estimation has been experimentally
demonstrated in a variety of quantum architectures (Du
et al., 2010; Lanyon et al., 2010; Li et al., 2011; O’Malley
et al., 2016; Paesani et al., 2017; Santagati et al., 2018;
Wang et al., 2015)
To realise the standard phase estimation algorithm
given above, we sequentially need to time evolve the main
register under the Hamiltonian H for times t0 = 2π, t1 =
4π, ..., tω−1 = 2ωπ. The total coherent time evolution,
T, is then given by approximately T = 2ω+1π. Using
Eq. (61), for a success probability of p = 0.5, we require
ω = n + 2 ancilla qubits. The total evolution time can
be related to the binary precision ϵPE = 1/2n, to show
that T = 8π/ϵPE. Given that our success probability for
this estimate is p = 0.5, we expect to have to repeat the
procedure twice to obtain a good estimate of the ground
state. This is equivalent to a total of 16π/ϵPE calls to the
unitary e−iH (Reiher et al., 2017). In order to account
for the fact that c0 < 1, we must multiply the number of
repetitions of phase estimation by 1/|c0|2, on average, to
obtain the ground state.
The basic phase estimation algorithm described above
can be improved in many ways. It can be modiﬁed to use
only a single ancilla qubit, which is used to measure each
bit in the energy eigenvalue sequentially (Aspuru-Guzik
et al., 2005; Kitaev, 1995). It can also be made more
eﬃcient (Kivlichan et al., 2019b; Svore et al., 2013),
parallelised (Knill et al., 2007; Reiher et al., 2017), or
made more resilient to noise (O’Brien et al., 2018a).
We can further improve upon the asymptotic scaling
of phase estimation by using classically obtainable
knowledge about the energy gap between the ground
and ﬁrst excited states (Berry et al., 2018). The ultimate
limit for the number of calls required to e−iH is π/ϵPE
(for a completely general Hamiltonian, H), which is ap-
proximately obtained using Bayesian approaches (Berry
et al., 2009; Higgins et al., 2007; Paesani et al., 2017;
Wiebe and Granade, 2016),
or entanglement based
approaches (Babbush et al., 2018b). For the case of a
molecular Hamiltonian Reiher et al. (2017) showed that
a number of calls scaling as π/2ϵPE will suﬃce.

The ﬁnite precision, ϵPE, obtained in E0 is not the
only source of error in the algorithm.
There are also
errors arising from imperfect implementation of the con-
trolled unitary evolutions applied to the main register,
which we denote as ϵU. This error can arise, for exam-
ple, from a decomposition of e−iH into arbitrary single
and two qubit gates, as occurs during a Trotter decom-
position. There are also errors arising from constructing
arbitrary gates from a discrete set of gates – such as ap-
proximating single qubit rotations from multiple T and
Hadamard gates. These are typically referred to as cir-
cuit synthesis errors, ϵCS, and can be quantiﬁed using
techniques such as the Solovay-Kitaev theorem (Dawson
and Nielsen, 2005). For the speciﬁc case of a Trotter de-

## Page 27

composition of e−iH, Reiher et al. (2017) showed that
the error in the energy eigenvalue obtained from phase
estimation is upper bounded by ϵPE + ϵU + ϵCS.
In
general, it is diﬃcult to optimally allocate resources be-
tween these error budgets in order to minimise the total
error (Kivlichan et al., 2019a; Reiher et al., 2017).

Regardless of which version of phase estimation is
used, there are two universal features.
Firstly, it is
necessary for the register to initially be in a state with
a non-zero overlap with the target eigenstate. Secondly,
we must have a way to coherently implement a unitary
operator deﬁned by an eﬃciently invertible function of
the Hamiltonian. This unitary operator is often (but not
always) chosen to be the time evolution operator, e−iH,
used above. We will discuss techniques to satisfy both of
these requirements in Sec. V.A.2 and Sec. V.A.3, below.

2. State preparation

Initialising the qubit register in a state which has a
suﬃciently large overlap with the target eigenstate (typ-
ically the ground state), is a non-trivial problem. This is
important, because a randomly chosen state would have
an exponentially vanishing probability of collapsing to
the desired ground state, as the system size increases.
Even more problematically, McClean et al. (2014) showed
that phase estimation can become exponentially costly,
by considering the imperfect preparation of eigenstates of
non-interacting subsystems. This highlights the necessity
of developing state preparation routines which result in
at worst a polynomially decreasing overlap with the FCI
ground state, as the system size increases. Several tech-
niques have been proposed for state preparation. One ap-
proach is to prepare reference states obtained from classi-
cally tractable calculations, such as: conﬁguration inter-
action states (Babbush et al., 2015; Wang et al., 2009),
open-shell spin symmetry-adapted states (Sugisaki et al.,
2016, 2018), multireference states (Sugisaki et al., 2019),
or states produced by adaptive sampling conﬁguration
interaction methods (Tubman et al., 2018).
Alterna-
tively, we can use: the variational methods discussed in
Sec. V.B (Yung et al., 2014), quantum algorithms for
imaginary time evolution (Motta et al., 2019), or adia-
batic state preparation (Aspuru-Guzik et al., 2005). We
focus here on adiabatic state preparation, an approach
inspired by the adiabatic model of quantum computa-
tion (Farhi et al., 2000).
For any Hamiltonian Hs, we can prepare a state |Ψ⟩
that is close to its ground state via adiabatic state prepa-
ration (Albash and Lidar, 2018). To do so, we ﬁrst start
with a simple Hamiltonian H0 and prepare its ground
state. We then time evolve the system under a Hamilto-
nian that changes slowly from H0 to Hs, thus preparing

a state that is close to the ground state of Hs. The eﬃ-
ciency of adiabatic state preparation depends on the gap
between the ground state and the ﬁrst excited state along
the path between H0 and Hs. For chemical systems, ASP
may be achieved by initialising the system in the ground
state of the Hartree-Fock Hamiltonian (H0), and interpo-
lating between the initial and ﬁnal Hamiltonians using an
annealing schedule such as H(t) = (1−t/T)H0+(t/T)Hs,
where t is the time and T is the maximum desired simula-
tion time (Aspuru-Guzik et al., 2005). Alternative paths
that may be more eﬃcient for problems of chemical inter-
est have also been investigated (Veis and Pittner, 2014;
Wecker et al., 2015b). The maximum annealing time, T,
is given by

T ≈O

M 4


,
(62)

mins∆(t)

where ∆(t) = E1(t)−E0(t) and M is the number of spin-
orbitals in the molecule. Reiher et al. (2017) noted that
the true scaling may be closer to O(M 2/mint∆(t)). It is
diﬃcult to know the size of the gap along the entire adi-
abatic path a priori, restricts our ability to perform ASP
in the minimum amount of time. One possible method
for reducing the annealing time required is to introduce
additional ‘driving’ Hamiltonians, as was numerically in-
vestigated by Matsuura et al. (2018). Although Eq. (62)
does not explicitly depend on the initial state used, it
is intuitively preferable to start in a state that has good
overlap with the target ground state. We would expect
the anneal path to be shorter, and we may be more con-
ﬁdent that the gap between the ground and excited state
does not shrink exponentially. This view is supported by
the numerical simulations of Veis and Pittner (2014), who
found that annealing times for methylene (CH2) could be
reduced by up to four orders of magnitude by using an ini-
tial state with larger overlap with the true ground state.
We note however that if an initial state with suﬃciently
large overlap with the ground state is available, we may
be able to forgo adiabatic state preparation entirely, and
instead carry out phase estimation directly on that initial
state. As discussed above, phase estimation only requires
a non-negligible overlap with the target ground state.

There are a variety of methods that can be used to
evolve the system under this time-dependent Hamilto-
nian, which are discussed below.

3. Hamiltonian simulation

As discussed above, both the canonical phase estima-
tion algorithm and adiabatic state preparation require
implementation of the time evolution operator, e−iHt,
where H may or may not be time dependent. There are
several ways to do this, each with their own advantages
and disadvantages.

## Page 28

a. Product formulae
The most simple method for time evolution has al-
ready been described in Sec. II.B; Trotterization. If a
time-independent Hamiltonian H, can be decomposed as
H = P

i hi, where hi are local Hamiltonians, then a ﬁrst
order Lie-Trotter-Suzuki approximation (Trotter, 1959)
of the time evolution is

i
e−ihit/S
!S

Y

e−iHt =

+ O(t2/S).
(63)

This approach is also referred to as the ‘product formula’
method. In practice, to achieve accuracy ε, the number of
Trotter steps S = O(t2/ε) should be large in order to sup-
press the errors in the approximation. This is eﬀectively
a stroboscopic evolution under time evolution operators
corresponding to each of the terms in the Hamiltonian.
It is also possible to use higher order product formu-
lae (Berry et al., 2007; D¨ur et al., 2008; Suzuki, 1976),
which scale better with respect to the simulation error
than the ﬁrst order method. Randomisation procedures
(such as randomly ordering the terms in the Trotter se-
quence, or stochastically choosing which terms to include
in the Hamiltonian), have been shown to improve the ac-
curacy obtained using product formulae (Campbell, 2018;
Childs et al., 2018; Ouyang et al., 2019).
Product formulae can also be used to simulate dynam-
ics under a time dependent Hamiltonian, H(t). Wiebe
et al. (2011) showed that the accuracy of such simulations
depends on the derivatives of the Hamiltonian (although
this dependence may be alleviated by incorporating ran-
domisation procedures (Poulin et al., 2011)).
As discussed above, the error in the simulation is
determined by the Trotter formula used, the number
of Trotter steps, and the ordering of the terms.
It is
important to note that the gate counts of all product
formula based methods scale as O(poly(1/ϵ)).
Endo
et al. (2018c) investigated using extrapolation to sup-
press the error arising from using a ﬁnite number of
Trotter steps, as is often done in classical computations.

b. Advanced Hamiltonian simulation methods
Alternative methods have been introduced which
may realise the time evolution operator more eﬃciently
than Trotterization, including:
quantum walk based
methods (Berry et al., 2015b; Childs and Kothari, 2011),
multiproduct formulae (Childs and Wiebe, 2012; Low
et al., 2019b), Taylor series expansions (Berry and Childs,
2012; Berry et al., 2015a,c) or Chebyshev polynomial ap-
proximations (Subramanian et al., 2018), and qubitiza-
tion (Low, 2018; Low and Chuang, 2016) in conjunction
with quantum signal processing (Low and Chuang, 2017;
Low et al., 2016). The cost of these methods depends
on how the Hamiltonian is accessed or ‘queried’ during

the computation. One approach is the ‘linear combina-
tions of unitaries’ (LCU) query model, which decomposes
the Hamiltonian or time evolution operator into a linear
combination of unitary operators, which are then applied
in superposition using oracle circuits (which must be ex-
plicitly constructed for a given problem).
As a linear
combination of unitaries is itself not necessarily unitary,
these approaches may require additional techniques (such
as amplitude ampliﬁcation (Berry et al., 2014)) to main-
tain a high probability of success. Alternatively, we can
use oracles to access the non-zero entries of Hamiltoni-
ans which are d-sparse (they have at most d non-zero
elements in each row and column, where d is a polyloga-
rithmic function of the matrix dimension).
In addition the the product formula approach, the
Taylor series and quantum signal processing + qubiti-
zation techniques have found the most use to date in
quantum computational chemistry algorithms. Both of
the aforementioned query models can be used for the
Taylor series and quantum signal processing + qubitiza-
tion approaches. The Taylor series and quantum signal
processing + qubitization algorithms scale exponentially
better with regards to the accuracy of the simulation
than product formula based methods.

The Taylor series method expands the time evolution
operator as a truncated Taylor series, where each term in
the expansion is unitary. We can then use the aforemen-
tioned LCU oracles to implement these unitary opera-
tors in superposition, thus realising time evolution under
the Hamiltonian. Variants of the Taylor series method
for simulating time dependent Hamiltonians have also
been developed (Berry et al., 2019a; Kieferova et al.,
2018). Qubitization provides another way of accessing
the Hamiltonian during quantum computation, using a
‘block encoding’ of the Hamiltonian. Qubitization nat-
urally implements a quantum walk operator with eigen-
values e−iarcsin(Ek/α) where Ek is the kth eigenvalue of
the Hamiltonian H and α is a normalisation factor. We
can then use quantum signal processing to invert the
arcsin function, recovering time evolution with the de-
sired eigenvalues e−iEkt. We refer the readers to work by
Childs et al. (2017) and the review of Cao et al. (2019) for
a summary of recent progress in Hamiltonian simulation
and a comparison of the diﬀerent methods.

4. Phase estimation for chemistry simulation

Both product formulae and more advanced methods
of Hamiltonian simulation have been applied to solve
problems in quantum computational chemistry.
We
discuss the asymptotic results obtained using these
diﬀerent methods for four classes of problems: molecules
in Gaussian orbital basis sets, systems treated with
plane wave basis sets, the Fermi-Hubbard model, and

## Page 29

ﬁrst quantised grid based simulations. We will discuss
the explicit gate and qubit counts required to implement
some of these methods in Sec. VIII.B. Once again, the
number of spin-orbitals in the molecule, or spin-sites in
a lattice is given by M, and the number of electrons
is given by N.
We also refer the reader to the tables
produced by Babbush et al. (2018b,c), which chart de-
velopments in the asymptotic scaling of phase estimation
based approaches to quantum computational chemistry.

a. Gaussian orbital basis sets
As discussed in Sec. III.D, Gaussian orbitals can be
used to compactly describe single molecules. They result
in a second quantised Hamiltonian with O(M 4) terms.
The overall cost of phase estimation using product for-
mulae depends on the cost of implementing a single Trot-
ter step (which can be inﬂuenced by the number of terms
in the Hamiltonian), and the number of Trotter steps re-
quired to achieve the desired accuracy, and the accuracy
desired (typically taken as a constant value, such as to
within chemical accuracy).
Early works on ﬁnding the ground state of molecular
systems in Gaussian basis sets used ﬁrst and second
order product formalae (Aspuru-Guzik et al., 2005;
Babbush et al., 2015; Hastings et al., 2015; Poulin
et al., 2015; Reiher et al., 2017; Wecker et al., 2014;
Whitﬁeld et al., 2011).
A series of improvements
throughout these papers reduced the scaling of phase
estimation for molecules from O(M 11) (Wecker et al.,
2014) to (empirically) O(M 5) (Babbush et al., 2015).
A notable feature of these Trotter-based simulations is
that rigorous bounds on the Trotter error are believed
to be loose by several orders of magnitude, which may
impact the scaling of these approaches. We discuss this
in more detail in Sec. V.A.5.

As would be expected, the introduction of more
advanced Hamiltonian simulation algorithms led to a
reduction in the asymptotic scaling of chemistry algo-
rithms. Using the Taylor series method, algorithms were
developed which scale as O(M 5) (Babbush et al., 2016)
and O(N 2M 3) (Babbush et al., 2017) for molecules in
Gaussian basis sets.
The ﬁrst result uses the second
quantised representation of the Hamiltonian.
The
second, more eﬃcient result is obtained by constructing
oracle circuits which access the non-zero elements of the
Hamiltonian in a basis of Slater determinants (known
as the CI matrix (Toloui and Love, 2013)). The Hamil-
tonian has a sparsity of O(N 2M 2) in this basis. These
algorithms calculated the molecular integrals on the
quantum computer, exploiting an analogy between the
discretisation of space in Riemannian integration and
the discretisation of time in time dependent Hamiltonian
simulation methods (Babbush et al., 2016). Techniques

to further increase the sparsity of the problem, such
as using symmetries present in the electronic structure
Hamiltonian, have also been proposed; however these
have yet to be thoroughly investigated in the context of
Hamiltonian simulation (Gulania and Whitﬁeld, 2019;
Whitﬁeld, 2013).

As discussed above, qubitization (Low, 2018; Low and
Chuang, 2016) is a technique originally introduced in
conjunction with quantum signal processing (Low and
Chuang, 2017; Low et al., 2016) to approximate the uni-
tary e−iHt, in order to perform time evolution of a given
state. However, it was later noted that for certain func-
tions f(H), qubitization could be used on its own to di-
rectly implement the unitary e−if(H)t without approx-
imation errors (Berry et al., 2018; Poulin et al., 2018).
One can then perform phase estimation on this unitary
to obtain the energy eigenvalues of the Hamiltonian, pro-
vided f(H) is eﬃciently invertible. This technique was
used by Berry et al. (2019b), in conjunction with a low
rank decomposition of the Hamiltonian (Motta et al.,
2018) (described in Sec. IV.C.2). This produced an algo-
rithm with a scaling of O(M 1.5λ), where λ is the 1-norm
of the Hamiltonian.
While rigorous bounds on λ in a
Gaussian basis are not known, Berry et al. (2019b) noted
that it usually scales as at least O(M 1.5).

b. Plane wave basis sets
As discussed in Sec. III.D.3, plane wave basis sets
are particularly suitable for periodic systems, such as
materials. While they can also be used to simulate sin-
gle molecules, we require approximately 10 to 100 times
as many plane waves as Gaussian orbitals for accurate
simulations. The plane wave and plane wave dual basis
sets reduce the number of terms in the Hamiltonian to
O(M 3) and O(M 2), respectively. As a result, using the
plane wave basis sets can reduce the asymptotic scaling
of several approaches to chemistry simulation.
The best product based formulae approaches de-
scribed above scale as O(M 1.67N 1.83) in a plane wave
basis (Babbush et al., 2018c).
This can be further
improved for systems where it is appropriate to target
an extensive error in the energy (Kivlichan et al., 2019a).
This means that the error in the energy scales with the
size of the system, and therefore with M. As the scaling
of a Trotterized simulation is inversely proportional to
the energy error desired, factors of M can be cancelled
from both the numerator and denominator of the algo-
rithm scaling. For 3D materials, such as diamond, the
scaling of Trotter based approaches to phase estimation
in a plane wave dual basis was reduced to around O(M 2).

The plane wave basis also beneﬁted the algorithms de-
scribed above which utilise the Taylor series method for
Hamiltonian simulation. The scaling of the CI matrix

## Page 30

based algorithm of Babbush et al. (2017) was reduced
from O(N 2M 3) in a Gaussian basis to O(M 2.67) in a
plane wave basis (Babbush et al., 2018c).
A time dependent form of the Taylor series approach
was used for simulation in the ‘interaction picture’,
which enables more eﬃcient time evolution in a plane
wave dual basis, scaling as O(M 2) (Low and Wiebe,
2018)
(although
this
algorithm
uses
O(Mlog2(M))
qubits).
A similar interaction picture method was
introduced by Babbush et al. (2018a), using plane waves
and ﬁrst quantisation. This algorithm has a gate scaling
of O(N 8/3M 1/3) and requires O(Nlog2(M)) qubits,
plus ancillas (Babbush et al., 2018a). This was the ﬁrst
quantum computational chemistry algorithm to achieve
sublinear scaling in M; a feature that can be used
to mitigate the inability of plane waves to compactly
describe molecular systems.

Qubitization has also been used to produce highly eﬃ-
cient algorithms for the plane wave and related basis sets.
Babbush et al. (2018b) used qubitization and a form of
phase estimation which saturates the Heisenberg limit to
construct algorithms for simulations of matter in a plane
wave dual basis. Their algorithm has a gate scaling of
O(M 3), for condensed phase electronic structure prob-
lems.

Continuing the trend of exploiting diﬀerent chemical
representations to improve the eﬃciency of qubitization,
McClean et al. (2019a) investigated the use of discontin-
uous Galerkin basis sets. As discussed in Sec. III.D.3),
these basis sets provide a more compact description of
molecular systems than plane waves, but also reduce the
number of terms in the Hamiltonian to O(M 2).
Mc-
Clean et al. (2019a) estimated from numerics on hydro-
gen chains that these basis sets could reduce the scaling
of qubitization to around O(M 2.6). Further work is re-
quired to better ascertain and optimise the scaling of this
technique.

Qubitization can also be used in ﬁrst quantization with
the plane wave basis to achieve a sublinear scaling with
the number of plane waves. Babbush et al. (2018a) ob-
tained a scaling of O(N 4/3M 2/3 + N 8/3M 1/3), similar
to the scaling of their interaction picture algorithm dis-
cussed above.

c. Fermi-Hubbard model
As described in Sec. III.B.2, the Fermi-Hubbard
Hamiltonian contains O(M) terms, many of which com-
mute with each other. This can improve the eﬃciency of
many of the algorithms discussed above.

Wecker et al. (2015b) investigated using adiabatic state
preparation and a Trotter based approach to phase esti-
mation to probe the phase diagram of the Fermi-Hubbard
model. Their approach to ﬁnding the ground state re-
quired O(M 3) gates. This was subsequently improved by

Kivlichan et al. (2019a), who considered the case where
an extensive error in the energy is targeted, and found
that the cost of Fermi-Hubbard model simulations was
eﬀectively between O(1) and O(M 1/2) using Trotterisa-
tion.
The qubitization algorithm of Babbush et al. (2018b),
discussed above, was also applied to the Fermi-Hubbard
model. Those authors obtained a gate scaling of O(M)
for the Fermi-Hubbard model.
When considering an
intensive error in the energy, this approach outperforms
the Trotter-based method of Kivlichan et al. (2019a).

New procedures have also been developed speciﬁcally
for time evolution under lattice Hamiltonians.
These
Hamiltonians
have
geometrically
local
interactions
between qubits that are laid out on a lattice – such as
the Fermi-Hubbard model under a locality preserving
mapping (see Sec. IV.B.3). Haah et al. (2018) made use
of arguments about the speed of information propaga-
tion in lattice systems to obtain a simulation algorithm
requiring O(Mt) gates to simulate time evolution for
time t under lattice Hamiltonians. Similar results were
obtained by Childs and Su (2019), who proved that a
kth order product formula can simulate time evolution
of an M qubit lattice Hamiltonian using O((Mt)1+ 1

k )
elementary operations.
These algorithms are almost
optimal in terms of asymptotic gate complexity.

d. Grid based methods
As discussed in Sec. III.B.1, grid based methods are
particularly suitable for high accuracy calculations – in
particular, calculations which do not make the Born-
Oppenheimer approximation, and so treat both the elec-
trons and nuclei on an equal footing.
The ﬁrst quantised grid based algorithm algorithm
of Kassal et al. (2008) proceeds as follows. The qubits
are used to create a discretised grid,
as described
in Sec. IV.A. Physically relevant states can then be
prepared using the algorithms outlined by Kassal et al.
(2008) and Ward et al. (2009).
The state can be
propagated in time by repeatedly using the quantum
Fourier transform to move between the position and
momentum bases, so that the potential and kinetic
terms are diagonal (respectively) and therefore simple to
apply. Kassal et al. (2008) did not calculate an explicit
scaling for their algorithm.

Kivlichan et al. (2017) improved upon the method de-
scribed above, using the Taylor series method for time
evolution. Their method discretised the kinetic and po-
tential terms of the Hamiltonian, separated them into
linear combinations of unitary operators, and applied
the Taylor expansion method to simulate time evolution.
Those authors obtained a scaling of O((N/h2+N 2)t) (ex-

## Page 31

cluding logarithmic factors), where h is the grid spacing
and t is the simulation time.

5. Outstanding problems

While the advanced Hamiltonian simulation methods
described above are asymptotically more eﬃcient than
Trotterization, the Trotter error bounds appear to be
loose by several orders of magnitude (Babbush et al.,
2015; Poulin et al., 2015). A study of spin Hamiltoni-
ans (Childs et al., 2017) found that the asymptotic scal-
ing of Trotter methods was much worse than the qubiti-
zation + quantum signal processing, and Taylor series
methods.
However, when numerical simulations were
performed, Trotter methods required lower gate counts
than the other methods. There are three main factors
that may make the Trotter error bound loose in chemical
simulations. Firstly, it is diﬃcult to obtain a tight error
bound for a Trotterized time evolution under a physi-
cal Hamiltonian, as analytic proofs typically utilise mul-
tiple triangle inequalities, each of which may be loose.
Secondly, these error bounds can be understood as the
worst error that could be induced in any state which the
unitary acts on. However, for chemistry simulation, we
are often only interested in a small subset of the pos-
sible states, which again may reduce the Trotter error.
Finally, we are often interested not in the error in the
state, but in the error of some observable. This fact was
exploited by Heyl et al. (2019) who considered the er-
ror in local observables of spin chains, and obtained an
improved simulation complexity.

A challenge facing the Taylor series method is that it
may require many elementary logic operations, resulting
in a large T gate count when considering fault-tolerant
approaches (although work by Sanders et al. (2019) may
help to alleviate this problem). However, while the Tay-
lor series method is asymptotically more expensive than
qubitization + quantum signal processing, there has not
yet been a variant of the latter technique formulated for
time dependent Hamiltonians.
Time dependent tech-
niques are used in the interaction picture method that
underpins the algorithms of Babbush et al. (2018a) and
Low and Wiebe (2018).
In addition, it was noted by
Childs et al. (2017) that implementing quantum signal
processing required intensive classical pre-computation
to obtain the parameters used in the quantum circuit.
As such, it is not yet possible to conclusively state which
method will perform best for chemical systems.

Despite this progress, all of the methods discussed
above require circuits with a large number of gates. As
a result, these methods are typically assumed to require
fault-tolerance.
As near-term quantum computers will
not have enough physical qubits for error correction, the
long gate sequences required by these algorithms make
them unsuitable for near-term hardware. Consequently,

FIG. 6 A schematic of the variational quantum eigensolver
(VQE). The VQE attempts to ﬁnd the ground state of a
given problem Hamiltonian, by classically searching for the
optimal parameters ⃗θ which minimise ⟨Ψ(⃗θ)| H |Ψ(⃗θ)⟩. The
state preparation and measurement subroutines (red, upper
left, and blue, right) are performed on the quantum computer.
The measured observable O(⃗θ) and parameter values are fed
into a classical optimisation routine (green, lower), which out-
puts new values of the parameters. The new parameters are
then fed back into the quantum circuit. The gates acting on
the qubits can be any parametrized gates, e.g. single qubit ro-
tations or controlled rotations. Non-parametrized gates (e.g.
X, Y, Z, CNOT) are also allowed. The circuit U(⃗θ) and trial
wavefunction it produces |Ψ(⃗θ)⟩are both known as the VQE
ansatz. The process is repeated until the energy converges.

alternative methods are required for near-future chem-
istry simulation. We discuss one such approach in the
following section.

B. Variational algorithms

A promising algorithm for near-term quantum hard-
ware is the variational quantum eigensolver (VQE), ﬁrst
proposed and experimentally realised by Peruzzo et al.
(2014), and elaborated on by McClean et al. (2016). The
VQE aims to ﬁnd the lowest eigenvalue of a given Hamil-
tonian, such as that of a chemical system. The VQE is a
hybrid quantum-classical algorithm. This means that it
uses the quantum computer for a state preparation and
measurement subroutine, and the classical computer to
process the measurement results and update the quan-
tum computer according to an update rule.
This ex-
changes the long coherence times needed for phase esti-
mation for a polynomial overhead due to measurement
repetitions and classical processing. To date, the VQE
has only been applied to second quantised basis set simu-
lations, and so our discussion of it will only be concerned
with that scenario.
The VQE relies upon the Rayleigh-Ritz variational
principle. This states that for a parametrized trial wave-

## Page 32

function |Ψ(⃗θ)⟩

⟨Ψ(⃗θ)| H |Ψ(⃗θ)⟩≥E0,
(64)

where E0 is the lowest energy eigenvalue of the Hamilto-
nian H, and ⃗θ is a vector of independent parameters,
⃗θ = (θ1, ..., θn)T.
This implies that we can ﬁnd the
ground state wavefunction and energy by ﬁnding the val-
ues of the parameters which minimise the energy expec-
tation value. As classical computers are unable to eﬃ-
ciently prepare, store and measure the wavefunction, we
use the quantum computer for this subroutine. We then
use the classical computer to update the parameters us-
ing an optimisation algorithm. This sequence is shown
in Fig. 6.
The qubit register is initialised in the zero
state. We can optionally apply a non-parametrized set
of gates to generate a mean-ﬁeld (Jiang et al., 2018b;
Kivlichan et al., 2018; Wecker et al., 2015b) or multi-
reference state (Babbush et al., 2015; Dallaire-Demers
et al., 2018; Sugisaki et al., 2019, 2016, 2018; Tubman
et al., 2018) describing the chemical system of interest

|Ψref⟩= Uprep|¯0⟩.
(65)

A
series
of
parametrized
gates
U(⃗θ)
=
UN(θN) . . . Uk(θk) . . . U1(θ1) are then applied to the
qubits.
Here, Uk(θk) is the kth single or two qubit
unitary gate, controlled by parameter θk. This circuit
generates the trial wavefunction

|Ψ(⃗θ)⟩= U(⃗θ)|Ψref⟩.
(66)

We refer to |Ψ(⃗θ)⟩as the ansatz state, and U(⃗θ) as the
ansatz circuit. However, the reader will ﬁnd that in the
literature the word ansatz is typically used interchange-
ably to describe both. The set of all possible states that
can be created by the circuit U is known as the ‘ansatz
space’. We must select an ansatz appropriate for both
the available hardware, and chemical system being sim-
ulated.
The merits, drawbacks and implementation of
common ans¨atze will be discussed in Sec. V.B.1.
Once the wavefunction has been generated, we need
to measure the expectation value of the Hamiltonian.
Chemical Hamiltonians in the second quantised basis set
approach can be mapped to a linear combination of prod-
ucts of local Pauli operators, using the transformations
introduced in Sec. IV.B. We write that

i
σj
i ,
(67)

H =
X

j
hjPj =
X

j
hj
Y

where hj is a real scalar coeﬃcient, σj
i represents one of
I , X , Y or Z, i denotes which qubit the operator acts
on, and j denotes the term in the Hamiltonian. We can
then use the linearity of expectation values to write that

N
X

E(⃗θk) =

j
hj⟨Ψ(⃗θk)|
Y

i
σj
i |Ψ(⃗θk)⟩.
(68)

These state preparation and measurement steps should
be repeated many times in order to measure the expec-
tation value of every term in the Hamiltonian to the
required precision. As the quantum computer is reini-
tialised for each repetition, the required coherence time
is reduced compared to quantum phase estimation. This
is known as the Hamiltonian averaging method of cal-
culating the energy (McClean et al., 2014), and requires
O(1/ϵ2) measurements to determine the energy to a pre-
cision ϵ. We will discuss the measurement aspect of the
VQE in more detail in Sec. V.B.2.
Once the energy has been measured, it is passed to a
classical optimisation routine, together with the current
values of ⃗θk (other observables, such as the energy gradi-
ent, could also be supplied to the optimisation routine).
The optimisation routine outputs new values of the cir-
cuit parameters, ⃗θk+1. These are used to prepare a new
trial state, |Ψ(⃗θk+1)⟩, which is ideally lower in energy.
These steps are repeated until the energy converges to
a minimum. We will summarise previous investigations
into classical optimisation routines in Sec. V.B.3.
The VQE has been experimentally demonstrated on
most leading quantum architectures including: supercon-
ducting qubits (Colless et al., 2018; Kandala et al., 2017;
O’Malley et al., 2016), trapped ions (Hempel et al., 2018;
Kokail et al., 2019; Nam et al., 2019; Shen et al., 2017),
and photonic systems (Peruzzo et al., 2014), and shows
many desirable features. It appears to be robust against
some errors (McClean et al., 2016; O’Malley et al., 2016),
and capable of ﬁnding the ground state energies of small
chemical systems using low depth circuits (Kandala et al.,
2017). While the VQE appears promising for near-term
chemistry simulation, several considerable challenges re-
main. Firstly, the VQE is a heuristic method; it is cur-
rently unclear whether the quantum circuits proposed
will yield better approximations of the ground state than
the classical methods already available. This challenge
is exacerbated by the diﬃculty of optimising the wave-
function, as optimisation routines could fail to ﬁnd the
global minimum. Secondly, the number of measurements
required to obtain the energy to the desired accuracy can
be large. Finally, the VQE is typically considered in the
context of near-term quantum computers, without error
correction. While techniques have been proposed to pro-
tect these calculations from the eﬀects of noise (which we
will discuss in Sec. VI), it is still possible that noise may
prevent us from implementing suﬃciently long circuits to
surpass classical methods.

1. Ans¨atze

The parametrized circuits, or ‘ans¨atze’, for the VQE lie
between two extremes: hardware-eﬃcient and chemically
inspired. There has been relatively little work compar-
ing the eﬀectiveness of diﬀerent ans¨atze for anything but

## Page 33

the smallest chemistry problems. As quantum comput-
ers with tens of qubits become more widely available, and
quantum simulators become more powerful, there will be
greater scope to test diﬀerent ans¨atze for larger problem
sizes.

a. Hardware eﬃcient ans¨atze
Hardware eﬃcient ans¨atze have been in use since the
ﬁrst VQE experiment by Peruzzo et al. (2014). These
ans¨atze are comprised of repeated, dense blocks of a lim-
ited selection of parametrized gates that are easy to im-
plement with the available hardware. They seek to build
a ﬂexible trial state using as few gates as possible. As
such, they are well suited to the quantum computers cur-
rently available, which have short coherence times and
constrained gate topologies. Hardware-eﬃcient ans¨atze
have been used to ﬁnd the ground state energies of sev-
eral small molecules (Kandala et al., 2017, 2018). How-
ever they are unlikely to be suitable for larger systems, as
they take into account no details of the chemical system
being simulated. Barkoutsos et al. (2018) attempted to
tackle this issue, by proposing hardware eﬃcient ans¨atze
which conserve particle number, and so permit the use
of a chemically motivated initial state.
This proposal
has been experimentally demonstrated (Ganzhorn et al.,
2018) on a superconducting system.

McClean et al. (2018) showed that using hardware
eﬃcient ans¨atze with random initial parameters makes
the energy gradient essentially zero among most direc-
tions of Hilbert space, making classical optimisation
extremely diﬃcult.
This eﬀect becomes exponentially
more prominent as the number of qubits and circuit
depth increases. This suggests that randomly initialised
hardware eﬃcient ans¨atze are not a scalable solution
for
problems
in
quantum
computational
chemistry.
While techniques have been proposed to combat this
problem (Grant et al., 2019), further work is needed to
determine their eﬃcacy beyond small system sizes.

b. Chemically inspired ans¨atze
Chemically inspired ans¨atze result from adapting
classical computational chemistry algorithms to run ef-
ﬁciently on quantum computers.
Most notably, the
coupled cluster (CC) method discussed in Sec. III.C.4
can be extended to produce the unitary coupled cluster
(UCC) ansatz (Bartlett et al., 1989; Hoﬀmann and Si-
mons, 1988). The UCC method creates a parametrized
trial state by considering excitations above the initial ref-
erence state, and can be written as

U(⃗θ) = eT −T †,
(69)

where T = P
i Ti, and

i∈virt,α∈occ
tiαa†
iaα,

T1 =
X

i,j∈virt,α,β∈occ
tijαβa†
ia†
jaαaβ,

T2 =
X

(70)

...

and occ are occupied orbitals in the reference state, and
virt are orbitals that are initially unoccupied in the ref-
erence state. The UCC method is intractable on classical
computers, but can be eﬃciently implemented on a quan-
tum computer. It was originally proposed for quantum
computational chemistry by Yung et al. (2014) and Pe-
ruzzo et al. (2014). A comprehensive review of the UCC
method for quantum computational chemistry is given
by Romero et al. (2019).
The UCC method retains all of the advantages of the
CC method, with the added beneﬁts of being fully vari-
ational, and able to converge when used with multi-
reference initial states. The UCC ansatz is typically trun-
cated at a given excitation level – usually single and dou-
ble excitations (known as UCCSD). We show a canonical
implementation of the UCCSD ansatz in Sec. VII.A. The
canonical UCCSD implementation requires O(M 3N 2)
gates when using the Jordan-Wigner mapping (where M
is the number of spin-orbitals, and N is the number of
electrons) (Romero et al., 2019). This has been improved
to O(M 3N) gates, with a depth of O(M 2N) using swap
networks (O’Gorman et al., 2019), or O(M 3) −O(M 4)
gates using a low-rank decomposition of the UCCSD ten-
sor (Motta et al., 2018).
These gate counts assume that a single Trotter step can
be used to implement the UCC operator, which has pre-
viously been shown to yield accurate results (Barkoutsos
et al., 2018; Romero et al., 2019). However, this approach
has been questioned by Grimsley et al. (2019) who found
that depending on how the operators in the Trotterized
UCCSD ansatz are ordered, the optimised energies of sys-
tems displaying signiﬁcant electron correlation can vary
by amounts larger than chemical accuracy. As a result,
determining a suitable (or even optimal) ordering of the
operators in the UCCSD ansatz may be an interesting
and important area of future research.

In practice, the gate scaling is typically better than the
bounds given above, as many excitations are forbidden
by the symmetry point groups of molecular orbitals.
For example, the LiH molecule in an STO-3G basis
naively has around 200 excitation operators to consider.
However, taking into account symmetries and a reduced
active space, one can achieve accurate results while con-
sidering only around 12 excitation operators (Hempel
et al., 2018). Moreover, we can use classically tractable
methods to get initial approximations for the remaining
non-zero parameters (O’Malley et al., 2016; Romero
et al., 2019), which makes the classical optimisation step

## Page 34

of the VQE easier.

Alternative variants of the UCC ansatz have also
been proposed for solving problems in quantum com-
putational chemistry.
These include: the Bogoliubov-
UCC ansatz (Dallaire-Demers et al., 2018) (a quasipar-
ticle variant of UCC that is suitable for more general
Hamiltonians than the UCC ansatz, potentially includ-
ing the pairing terms present in superconductivity or
three body terms present in nuclear physics), the ‘low-
depth circuit ansatz’ (Dallaire-Demers et al., 2018) (a
heuristic which attempts to mimic the aforementioned
Bogoliubov-UCC ansatz using a lower depth circuit), or-
bital optimised-UCCD (Mizukami et al., 2019; Sokolov
et al., 2019) (which treats single excitations on the clas-
sical computer, rather than on the quantum computer,
to reduce the depth and number of gates in the cir-
cuit), k-UpCCGSD (Lee et al., 2019) and k-uCJ (Mat-
suzawa and Kurashige, 2019) (heuristic ans¨atze com-
prised of repeated layers of selected UCC operators),
adaptive-VQE (Grimsley et al., 2018; Tang et al., 2019)
(which creates an adaptive ansatz designed to maximise
recovery of the correlation energy), and qubit coupled-
cluster (Ryabinkin and Genin, 2019; Ryabinkin et al.,
2018) (a heuristic method which produced lower gate
counts than the UCC ansatz when applied to several
small molecules).

c. Hamiltonian variational ansatz
There are also variational ans¨atze that lie between
the extremes of chemically inspired ans¨atze and hard-
ware eﬃcient ans¨atze.
One important example is the
Hamiltonian variational ansatz (also commonly referred
to as a Trotterized adiabatic state preparation ansatz),
proposed by Wecker et al. (2015a). This ansatz was in-
spired by adiabatic state preparation and the quantum
approximate optimisation algorithm (a similar quantum-
classical hybrid algorithm for combinatorial optimisation
problems (Farhi et al., 2014)). The idea is to Trotterize
an adiabatic path to the ground state, using a number of
Trotter steps that may be insuﬃcient for accurate results.
One can then variationally optimise the Trotter evolution
times to create a variational ansatz for the ground state.
The number of parameters in this ansatz scales linearly
with the number of Trotter steps, S. Mathematically, we
write that

S
Y

Y

i
exp (θs
i Pi)
(71)

U =

s

where Pi are the Pauli strings in the Hamiltonian.

The eﬃciency of this ansatz is determined by the num-
ber of terms in the Hamiltonian. This leads to a scaling
of approximately O(M 4) when considering a Gaussian
molecular orbital basis (Wecker et al., 2015a).
Motta

et al. (2018) improved this asymptotic scaling using the
low rank decomposition method discussed in Sec. IV.C.
They reduced the number of gates required to implement
a Trotter step of the Hamiltonian to O(M 2log2(M)) with
increasing molecular size, and O(M 3) for ﬁxed molecu-
lar size and increasing basis size. The electronic struc-
ture Hamiltonian in a plane wave dual basis only con-
tains O(M 2) terms. Kivlichan et al. (2018) showed that
for Hamiltonians of this form, we can implement Trotter
steps in depth O(M), using O(M 2) two qubit gates.
The Hamiltonian variational ansatz appears particu-
larly suitable for the Fermi-Hubbard model, which only
has O(M) terms in its Hamiltonian.
Kivlichan et al.
(2018) showed that it is possible to implement Trotter
steps of the Fermi-Hubbard Hamiltonian with O(
√

M)
depth and O(M 1.5) gates on a linear array of qubits with
nearest-neighbour connectivity. Jiang et al. (2018b) im-
proved this result for the case of a 2D array of qubits with
nearest-neighbour connectivity. They showed that it is
possible to prepare initial states of the Fermi-Hubbard
model using O(M 1.5) gates, and perform Trotter steps of
the Hamiltonian using O(M) gates for each Trotter step.
It has also been noted (Kivlichan et al., 2018) that it is
possible to use locality preserving mappings (Jiang et al.,
2018a; Verstraete and Cirac, 2005) to perform Trotter
steps in constant depth. However, this comes at a cost
of requiring additional qubits, and may have a large con-
stant factor gate overhead.

2. Measurement

In Sec. V.B we described the Hamiltonian averaging
method, whereby the expectation value of each term
in the Hamiltonian is estimated through repeated state
preparation and measurement.
This procedure can be
used to calculate the 1-RDM and 2-RDM of the system.
McClean et al. (2016) and Romero et al. (2019) showed
that the number of measurements Nm, required to esti-
mate the energy to a precision ϵ, is bounded by

P
i |hi|
2

Nm =

ϵ2
,
(72)

where hi are the coeﬃcients of each Pauli string in the
Hamiltonian. This leads to a scaling of O(M 6/ϵ2) in a
Gaussian orbital basis, and O(M 4/ϵ2) for a plane wave
dual basis (Babbush et al., 2018c; Cao et al., 2019; Mc-
Clean et al., 2014).
These scalings may be problematic for large molecular
calculations. For example, Wecker et al. (2015a) found
that around 1013 samples would be required per energy
evaluation for a 112 spin-orbital molecule such as Fe2S2.
Fortunately, strategies have been proposed to reduce the
cost of measurement. Several groups have proposed using
heuristics to group together commuting terms (Izmaylov
et al., 2018; Kandala et al., 2017; McClean et al., 2016;

## Page 35

Verteletskyi et al., 2019), which appears to reduce the
measurement cost by a constant factor. Some authors
have also considered using additional unitary transforms
to enable more terms to be grouped, reducing the num-
ber of groups of terms from O(M 4) to O(M 3) (Crawford
et al., 2019; Gokhale et al., 2019; Gokhale and Chong,
2019; Jena et al., 2019; Yen et al., 2019b; Zhao et al.,
2019).
By grouping terms at a fermionic level, rather
than a qubit level, Bonet-Monroig et al. (2019) devised a
method for measuring the fermionic 2-RDM using O(M 2)
circuits (an additional gate depth of O(M) is required).
Similar results were obtained by Jiang et al. (2019), by
combining Bell basis measurements, and the ternary-tree
mapping described in Sec. IV.B.2. Another interesting
direction to explore may be to combine locality preserv-
ing fermion-to-qubit mappings with eﬃcent results for
qubit tomography (Bonet-Monroig et al., 2019; Cotler
and Wilczek, 2019; Paini and Kalev, 2019).
Although
we might expect that it would be optimal to divide the
Hamiltonian into the fewest possible number of groups,
this is not always the case. McClean et al. (2016) showed
that it is important to consider the covariances between
Hamiltonian terms within groups, as if these covariances
are positive, then it may be better to measure the terms
separately.
These covariances can be estimated using
classical approximations of the target state.

If we are only interested in measuring the energy ex-
pectation value, rather than the 1 and 2-RDMs, Hug-
gins et al. (2019b) showed that it is possible to use
the low rank Hamiltonian decomposition technique (dis-
cussed in Sec. IV.C.2) and orbital basis rotations to di-
vide the Hamiltonian into O(M) measurement groups.
When taking into account covariances between commut-
ing terms, the total number of measurements required for
small molecules was reduced by several orders of magni-
tude. This measurement scheme also reduces the locality
of strings in the qubit Hamiltonian, thus reducing the
impact of qubit read-out error.

3. Classical optimisation

As discussed above, classical optimisation is a crucial
aspect of the VQE. However, it is often diﬃcult to min-
imise complicated functions in high dimensional parame-
ter spaces. Classical optimisation routines must be both
fast and accurate. They also need to be robust to noise,
which will be signiﬁcant in near-term quantum comput-
ers.
Classical optimisation algorithms can be broadly di-
vided into two classes: direct search and gradient based
methods. Direct search algorithms are considered more
robust to noise than gradient based methods, but may
require more function evaluations (Kolda et al., 2006).
Below, we summarise the results of previous ex-
perimental and numerical investigations into classical

optimisation algorithms used in conjunction with the
VQE. We also discuss methods to assist the classical
optimisation procedure.

a. Previous optimisation studies
Prior experimental VQE implementations have been
limited to small systems by the number of qubits avail-
able. As a result, the parameter space to optimise over
is relatively small, so previous results may not be in-
dicative of how these optimisation algorithms will per-
form for large problems. However, these studies are able
to demonstrate which methods can cope with the high
noise rates of current hardware. Direct search methods
(such as Nelder-Mead simplex (Hempel et al., 2018; Pe-
ruzzo et al., 2014; Shen et al., 2017), simulated anneal-
ing (Hempel et al., 2018), particle swarm (Colless et al.,
2018; Santagati et al., 2018) covariance matrix adapta-
tion (Sagastizabal et al., 2019), and the dividing rectan-
gles algorithm (Kokail et al., 2019)) were found to exhibit
good convergence to the ground state energy of small sys-
tems, despite relatively high noise rates.

The simultaneous perturbation stochastic approxima-
tion (SPSA) algorithm, has also been used to successfully
ﬁnd the ground state energy of small molecules, despite
relatively large uncertainties due to shot noise, and phys-
ical error rates (Ganzhorn et al., 2018; Kandala et al.,
2017, 2018).
The SPSA algorithm is an approximate
gradient based method, which steps ‘downhill’ along
a randomly chosen direction in parameter space.
In
contrast, canonical gradient descent based methods have
struggled to ﬁnd the ground state, due to the high levels
of noise present in current quantum devices (Peruzzo
et al., 2014).

The number of numerical studies comparing a subset of
optimisation algorithms for the VQE has grown rapidly –
hence, a full discussion of every study is beyond the scope
of this review. Instead, we summarise the major ﬁndings,
and highlight the diﬀerent approaches for optimisation.
In comparisons of ‘out-of-the-box’ optimisers (Mc-
Clean et al., 2016; Romero et al., 2019), the Nelder-
Mead simplex algorithm utilised in experimental stud-
ies was outperformed by both other direct search ap-
proaches, and gradient based approaches, such as L-
BFGS-B. All methods were liable to becoming trapped
in local minima, even for small systems.
This prob-
lem was partly mitigated by using a good initialisation
strategy, such as using a chemically motivated (M¨oller-
Plesset) guess for UCC excitation amplitudes (Romero
et al., 2019). Similar results were obtained using heuris-
tic methods of optimisation and initialisation (Wecker
et al., 2015a). Other investigations have considered op-
timisation using algorithms related to gradient descent,
such as: stochastic gradient descent (Harrow and Napp,

## Page 36

2019; Sweke et al., 2019), variational imaginary time evo-
lution (McArdle et al., 2018a), and quantum natural gra-
dient descent (Stokes et al., 2019; Yamamoto, 2019). A
limitation of the majority of these studies is that realis-
tic noise has rarely been considered, so it is still unclear
exactly how eﬀective each method may be in practice.

An alternative approach to optimising all of the pa-
rameters simultaneously, is to optimise them sequentially
(Nakanishi et al., 2019; Ostaszewski et al., 2019; Parrish
et al., 2019c). One can analytically minimise the energy
with respect to a single parameter, and can then sequen-
tially optimise the cost function over all of the parame-
ters. Repeated sequential optimisations are required to
ﬁnd a good estimate of the energy minimum.

Recent numerical work has explored the possibility of
using classical neural networks to optimise VQE circuits
for small instances of the Fermi-Hubbard model (Ver-
don et al., 2019; Wilson et al., 2019).
This approach
(known as ‘meta-learning’) works by training the neural
networks on many random instances of the system being
studied. The networks were able to successfully ‘learn’
to optimise the VQE ansatz, and showed indications
that they may be able to generalise to larger systems
than those on which they were trained (Verdon et al.,
2019). The approach also demonstrated some resilience
to noise included in the simulations (Wilson et al., 2019).

b. Related methods of optimisation
Methods which aid classical optimisation, but that
are not optimisation algorithms in their own right, have
also been proposed.
Quantum circuits have been proposed to calculate the
analytic gradient of the energy with respect to one of the
parameters (Guerreschi and Smelyanskiy, 2017; Mitarai
and Fujii, 2018; Schuld et al., 2019). This avoids the use
of ﬁnite diﬀerence formulae, which restrict the accuracy
of gradient evaluation, as the ﬁnite diﬀerence considered
is limited by the noise in the energy evaluation.
The
quantum gradient method makes use of the diﬀerentia-
bility of parametrized unitary operators. parametrized
unitaries can be written as exponentials of the parame-
ter and an anti-Hermitian operator, which are simple to
diﬀerentiate. A circuit to obtain the gradient of a toy
VQE simulation is shown in Fig. 7.
Several works have used concepts from adiabatic quan-
tum computing to aid the classical optimisation proce-
dure. Wecker et al. (2015a) proposed an ‘annealed vari-
ational’ method alongside the Hamiltonian variational
ansatz. This technique can be generalised to any ansatz
with a repeating, layered structure.
We assume that
the ansatz is composed of S layers. We ﬁrst decompose
the Hamiltonian of interest into Hs = H0 + sH1, where
H0 is a Hamiltonian that is eﬃciently solvable with a
classical computer, and H1 is a diﬃcult Hamiltonian to

FIG. 7 A quantum circuit to calculate the gradient of a toy
VQE simulation.
In this toy problem, the ansatz used is
|Ψ⟩= Rx(θ) |0⟩, and the Hamiltonian is H = Y . The energy
is given by E(θ) = ⟨Ψ(θ)| H |Ψ(θ)⟩= ⟨0| R†
x(θ)Y Rx(θ) |0⟩.
The energy gradient,
∂E

∂θ
=
i
2(⟨0| XR†
x(θ)Y Rx(θ) |0⟩−
⟨0| R†
x(θ)Y Rx(θ)X |0⟩).
This is the expectation value gen-
erated by the circuit above.

solve. When s = 1, the Hamiltonian is equivalent to the
problem Hamiltonian. The annealed variational method
works by considering the S layers as separate, distinct
ans¨atze. The input state to the ﬁrst layer of the ansatz
is the ground state of Hs=0. We optimise this ﬁrst layer
to ﬁnd the ground state of Hs=1/S. This state is then the
input into layer 2, which is optimised to ﬁnd the ground
state of Hs=2/S. This process is repeated until the ﬁnal
layer, which takes the ground state of Hs=(S−1)/S as its
input, and targets the ground state of Hs=1. All of these
steps are then combined, and used as the starting point
for a standard VQE optimisation. A similar technique
was proposed by Garcia-Saez and Latorre (2018).

Barkoutsos et al. (2018) introduced a transformation
of the Hamiltonian, such that it only measures the
energy of excitations above the Hartree-Fock state (the
correlation energy). Because only the correlation energy
is calculated, fewer measurements are required and
classical optimisation becomes easier. Overall, simulated
VQE calculations on small molecules were sped up by a
factor of 2 to 4 (Barkoutsos et al., 2018).

C. Evaluation of excited states

In this section, we discuss methods used to evaluate
the excited states of chemical Hamiltonians. These are of
interest for calculations of spectral properties, such pho-
todissociation rates and absorption bands. We are some-
times interested in obtaining excited states with speciﬁc
properties, such as a certain spin, or charge (Ryabinkin
and Genin, 2018; Ryabinkin et al., 2019; Yen et al.,
2019a).
The techniques used to obtain these special
states are similar in nature to the methods we discuss
for ﬁnding general excited states. There is still no clear
consensus as to which method may perform best for ﬁnd-
ing excited states. As such, we describe each of the lead-
ing methods in turn, and discuss their advantages and
limitations. We note that this area has seen rapid recent
development. Consequently, we do not discuss initial pro-
posals to calculate excited states, such as the folded spec-
trum method (McClean et al., 2016) and WAVES (San-

## Page 37

tagati et al., 2018), which are comparatively less eﬃcient
than more recent proposals.

1. Quantum subspace expansion

The quantum subspace expansion (QSE) method was
originally introduced to ﬁnd excited states (McClean
et al., 2017a), but has proven to be one of the most useful
techniques introduced to near-term quantum computa-
tional chemistry, with beneﬁts including better ground
state estimation (discussed below) and mitigation of
hardware errors (discussed in Sec. VI.C).
The original formulation of the QSE used a polynomial
number of additional measurements to ﬁnd the excited
states of a quantum system (McClean et al., 2017a). The
motivation for this was that the higher order reduced
density matrices (RDMs) can be obtained by expanding
the wavefunction in a subspace around the ground state.
These RDMs can then be used to ﬁnd the linear response
excited eigenstates. McClean et al. (2017a) considered
the single excitation linear response subspace around the
fermionic ground state. This subspace is spanned by the
states a†
iaj |E0⟩for all possible i, j, which corresponds to
measuring the 3- and 4-RDMs. This is designed to target
the low-lying excited states, which are assumed to diﬀer
from the ground state by a small number of excitations.
The excited states can be found by solving a gener-
alised eigenvalue problem in fermionic Fock space

HQSEC = SQSECE,
(73)

with a matrix of eigenvectors C, and a diagonal matrix
of eigenvalues E.
The Hamiltonian projected into the
subspace is given by

HQSE
ij,kl = ⟨E0| aia†
jHa†
kal |E0⟩.
(74)

The overlap matrix, required because the subspace states
are not orthogonal to each other, is given by

SQSE
ij,kl = ⟨E0| aia†
ja†
kal |E0⟩.
(75)

The QSE was experimentally demonstrated in a two
qubit superconducting system to ﬁnd the ground and
excited states of H2 (Colless et al., 2018).
Ollitrault
et al. (2019) showed that the QSE with single and double
excitations can be understood as an approximation to
the ‘equation of motion’ (EoM) method for ﬁnding
excited states, which was originally introduced as a
classical method in quantum chemistry by Rowe (1968).
Ollitrault et al. (2019) showed how the EoM method
can be implemented on a quantum computer.
They
found the EoM method to be robust to noise when
demonstrated experimentally, and more accurate for
ﬁnding excitation energies than the QSE, in numerical
tests.

As discussed above, the QSE has also been extended
to provide better estimates of the ground state energy.
Takeshita et al. (2019) showed how the QSE can be
used to recover the energy contribution of virtual or-
bitals, without requiring additional qubits to represent
the virtual orbitals.
This was achieved by consider-
ing a QSE with single and double excitations, where
the double excitations take two electrons from an active
space, to the virtual space. Naively, this would require
the measurement of matrix elements like Hijkl
αβγδ,ϵζηθ =

⟨E0| aαa†
βaγa†
δ

a†
ia†
jakal

a†
ϵaζa†
ηaθ |E0⟩, of which there

are O(M 12).
However, because the double excitations
are restricted to exciting two electrons into the virtual
space, it is possible to use Wick’s theorem, and contract
over the operators in the virtual space, to express the ma-
trix element above in terms of matrix elements involving
only 8 creation/annihilation operators (which deﬁnes the
4-RDM). These operators only act on the active space or-
bitals, MA, which reduces the number of measurements
required to O(M 8
A), and means that no additional qubits
are required.
Those authors demonstrate this method
by numerically simulating a cc-PVDZ calculation on H2
(which normally requires 20 qubits), using just 4 qubits,
and the additional measurements described above.

The QSE was also extended by Huggins et al. (2019a),
who devised a low cost method to extend the subspace
from being excitations above a reference state, to being
any state that is eﬃciently preparable on the quantum
computer. The method thus allows for creation of ﬂex-
ible ansatz states, without a dramatic increase in the
circuit depth. This approach was further reﬁned by Stair
et al. (2019), who provided a more eﬃcient approach to
realising this technique, when the ansatz circuit used is
composed of products of exponentiated Pauli operators.

The main drawback of the QSE is the large number of
measurements that may be required to obtain the 4-RDM
of the system. In general there are O(M 8) elements to
measure in the 4-RDM, compared to O(M 4) elements for
the Hamiltonian. The cost can be somewhat reduced by
approximating the 4-RDM using products of lower order
RDMs, and perturbative corrections. In addition, using
the linear response excitation operators described above,
we are limited in our description of excited states. This
can be problematic for systems which need higher order
excitations to accurately describe the excited states (Lee
et al., 2019; Watson and Chan, 2012).

We provide more information on the QSE method in
Sec. VI, where we discuss how it can also be used to
mitigate the eﬀects of errors.

## Page 38

2. Overlap-based methods

Overlap based methods exploit the orthogonality of
energy eigenstates. Once an eigenstate is found, we can
ﬁnd other eigenstates by ensuring that they are orthog-
onal to the original state (Endo et al., 2018a; Higgott
et al., 2018). After ﬁnding the ground state |E0⟩of a
Hamiltonian H with a VQE calculation, we replace the
Hamiltonian with

H′ = H + α |E0⟩⟨E0| ,
(76)

where α is chosen to be suﬃciently large compared to
the energy scale of the system.
The ground state of
the updated Hamiltonian H′ is no longer |E0⟩, but
the ﬁrst excited state |E1⟩of the original Hamilto-
nian H.
This process can be repeated to obtain
higher energy eigenstates.
The energy of the up-
dated Hamiltonian, ⟨Ψ(⃗θ)| H′ |Ψ(⃗θ)⟩= ⟨Ψ(⃗θ)| H |Ψ(⃗θ)⟩+
α ⟨Ψ(⃗θ)|E0⟩⟨E0|Ψ(⃗θ)⟩can be obtained by measuring
each term separately.
We can measure the ﬁrst term
using the Hamiltonian averaging procedure described in
Sec. V.B. The second term can be obtained from circuits
which calculate the overlap between the states, such as
the SWAP test.
The SWAP test approach requires a
circuit that has twice as many gates as the ansatz used
(but is of the same depth), and has twice as many qubits.
We can also use a method which requires twice as many
gates and is twice as deep as the original ansatz, but
does not require additional qubits (Higgott et al., 2018).
The additional resources required are the main limitation
of this approach to calculating excited states. Overlap-
based techniques were numerically investigated by Lee
et al. (2019), who also considered the propagation of er-
rors resulting from only obtaining an approximation of
lower lying eigenstates, rather than the true eigenstates.

3. Contraction VQE methods

The Subspace-search variational quantum eigensolver
(SSVQE) (Nakanishi et al., 2018) and the multistate con-
tracted variational quantum eigensolver (MCVQE) (Par-
rish et al., 2019b) methods are related to the overlap
based methods described above, in that they are driven
by the orthogonality of energy eigenstates. The diﬀer-
ences lie in how they enforce this orthogonality, as well
as how the ordering of the eigenstates is determined. In
the overlap based methods, orthogonality is enforced by
including the overlap between states in the cost function.
In contrast, the contraction VQE methods exploit con-
servation of orthogonality between states under a unitary
transform. To be more speciﬁc, a set of orthonormal ap-
proximate eigenstates {|φi⟩k
i=0} are chosen using an eﬃ-
cient classical approach. The quantum computer must be

able to be initialised in any of these states. The orthog-
onality of these states is invariant under the application
of a unitary ansatz circuit. The aim of the ansatz circuit
is to generate linear combinations of these initial states,
to form good approximations of the low energy subspace
of the system. This is achieved by optimising the ansatz
over an ensemble cost function,

k
X

C(⃗θ) =

j=0
⟨φj| U †(⃗θ)HU(⃗θ) |φj⟩.
(77)

Both of the contraction VQE methods then use fur-
ther processing to ﬁnd the ordering of the energy eigen-
states.
The SSVQE method uses a similar quantum-
classical hybrid approach to the ordinary VQE. In con-
trast, the MCVQE method uses classical diagonalisation
of a Hamiltonian matrix obtained in the low energy sub-
space (similar to the way in which the quantum subspace
expansion works). These contraction VQE methods dif-
fer from the overlap based methods, in that they obtain
all of the eigenstates at the same time, rather than se-
quentially. Consequently, all eigenstates should be ob-
tained to a similar accuracy. However, it may be diﬃ-
cult to ﬁnd a unitary circuit that simultaneously prepares
many eigenstates on an equal footing, which may make
these contraction methods diﬃcult to realise in practice.

VI. ERROR MITIGATION FOR CHEMISTRY

As discussed in Sec. II.A, physical qubits accumulate
errors during computation, due to their interaction with
the environment, and our imperfect control. While the
eﬀects of these errors can be suppressed using quantum
error correction, this requires a considerable increase in
the number of qubits used for the computation. If these
errors are not dealt with, they will corrupt the results of
our algorithms, rendering the calculations meaningless.
This was conﬁrmed for the case of chemistry calculations
by Sawaya et al. (2016), who used numerical simulations
to show the impact that noise has on phase estimation
based chemistry calculations.
Phase estimation based
approaches (discussed in Sec. V.A) require long circuit
depths, and so implicitly assume the use of quantum er-
ror correction. We will discuss the resources required to
carry out these calculations in Sec. VIII.B – however, it
suﬃces to say here that they are considerably greater
than the resources we have available at time of writing.
We claimed in Sec. V.B that the reduced coherence time
requirements of the VQE make it more suitable for noisy
quantum hardware, and may enable the extraction of
accurate results without the use of quantum error cor-
rection. It has been shown both theoretically (McClean
et al., 2016) and experimentally (O’Malley et al., 2016)
that the VQE can be inherently robust to some coher-
ent errors, such as qubit over-rotation. However, small

## Page 39

experimental demonstrations of the VQE have shown
that noise can still prevent us from reaching the de-
sired levels of accuracy (Hempel et al., 2018; Kandala
et al., 2017). Consequently, it appears that additional
techniques are required, if we are to perform classically
intractable chemistry calculations, without error correc-
tion.
The methods described in this section have been
developed to mitigate errors, rather than correct them.
These techniques are only eﬀective when used with
low depth circuits, such that the total error rate in the
circuit is low. However, the additional resources required
are much more modest than for full error correction. In
general, these techniques only require a multiplicative
overhead in the number of measurements required, if the
error rate is suﬃciently low. Many of these techniques
were introduced for use in general near-term algorithms,
and so can be applied to problems beyond chemistry
simulation.

As we are dealing with errors, it becomes necessary to
consider mixed states, rather than just pure states. As
such, we now switch to the density matrix formalism of
quantum mechanics.
We consider a quantum circuit that consists of G uni-
tary gates applied to an initial reference state |¯0⟩. The
output state if errors do not occur is given by

ρ0 = UG ◦· · · ◦U2 ◦U1(|¯0⟩⟨¯0|),
(78)

where for a density matrix ρ, U(ρ) = UρU †. We extract
information from the circuit by measuring a Hermitian
observable, O

¯O0 = Tr[ρ0O].
(79)

If each gate is aﬀected by a noise channel Ni, the pre-
pared state becomes

ρ =
Y

i
Ni ◦Ui(|¯0⟩⟨¯0|),
(80)

and the measurement result becomes ¯O = Tr[ρO].
In
general, we cannot recover the noiseless state ρ0 from
the noisy state ρ without error correction. However, the
error mitigation methods discussed below can approxi-
mate the noiseless measurement result ¯O0 from the noisy
measurement result, ¯O when the error rate is suﬃciently
low. It is important to note that error mitigation schemes
are not a scalable solution to the problem of noise in
quantum hardware. In order to scale up computations
to arbitrarily large sizes, fault-tolerant, error corrected
quantum computers are required.

A. Extrapolation

The extrapolation method (Li and Benjamin, 2017;
Temme et al., 2017) works by intentionally increasing

FIG. 8 A comparison of linear (blue, lower) and exponential
(grey, upper) extrapolation. The horizontal axis is the error
rate of each gate and the vertical axis is the expectation value
of the measured observable, ¯O. This ﬁgure was reproduced
from Endo et al. (2017), with permission.

the dominant error rate, ϵ0, by a factor λ, and inferring
the error free result by extrapolation. We can increase
the error rate using the techniques described by Kandala
et al. (2018) and Li and Benjamin (2017). The technique
is based on Richardson extrapolation (Richardson et al.,
1927), which to ﬁrst order corresponds to linear extrap-
olation using two points. We could also take a linear or
higher order ﬁt with several data points. For the former
case, the estimated value of the observable is given by

¯Oest
0
= λ ¯O(ϵ0) −¯O(λϵ0)

λ −1
.
(81)

While this method can improve the accuracy of calcu-
lations, it requires additional measurements in order to
keep the variance of the measured observable the same
as the non-extrapolated case. The extrapolation method
has been demonstrated for VQE experiments in both
molecular chemistry (Kandala et al., 2018; Ollitrault
et al., 2019), and nuclear physics (Shehab et al., 2019).
Exponential extrapolation was introduced by Endo
et al. (2017) as a more appropriate extrapolation tech-
nique for large quantum circuits. A comparison between
the two extrapolation methods is shown in Fig. 8. Otten
and Gray (2018b) have also extended the extrapolation
method to the scenario where the error rates of diﬀerent
gates are increased by diﬀerent factors.

B. Probabilistic error cancellation

The probabilistic error cancellation method introduced
by Temme et al. (2017) works by eﬀectively realis-
ing the inverse of an error channel, N −1, such that
N −1(N(ρ0)) = ρ0. Because realising the inverse channel
is in general an unphysical process, we use the scheme de-
picted in Fig. 9 to eﬀectively realise the inverse channel
by focusing only on measurement results.

## Page 40

FIG. 9 A schematic of the probabilistic error cancellation
method for a depolarising error resulting from a single qubit
gate. After the gate is applied, there is a noise channel N.
The method works by eﬀectively realising the inverse channel
N −1. This is achieved by randomly applying one of the X,
Y or Z operators with probability p2, or the identity gate
with p1. The expectation values resulting from the circuits
are combined.
If one of the Pauli matrices was applied to
realise the inverse channel, the resulting expectation value is
subtracted, rather than added (parity −1). The overhead γ
determines the number of additional measurements required
to keep the variance of the error mitigated result equal to
the variance of the noisy result. This can be generalised to
multi-qubit gates as described in the main text.

As an example, we consider the case of a depolarising
error channel,

ρ = D(ρ0) =

1 −3

4p

ρ0 + p

4(Xρ0X + Y ρ0Y + Zρ0Z).

(82)
The unphysical inverse channel is

ρ0 = D−1(ρ) = γ[p1ρ −p2(XρX + Y ρY + ZρZ)], (83)

where the coeﬃcient γ = (p + 2)/(2 −2p) ≥1, p1 =
(4 −p)/(2p + 4), and p2 = p/(2p + 4) in this case.
We cannot directly realise D−1 due to the minus sign
before p2. However, we can consider and correct its eﬀect
on the expectation value ¯O0

¯O0 = Tr[OD−1(ρ)],

= γ[p1 ⟨O⟩ρ −p2(⟨O⟩XρX + ⟨O⟩Y ρY + ⟨O⟩ZρZ)],

= γ[p1 ⟨O⟩ρ −p2(⟨XOX⟩ρ + ⟨Y OY ⟩ρ + ⟨ZOZ⟩ρ)],
(84)
where ⟨O⟩ρ = Tr[Oρ].
We can therefore measure O,
XOX, Y OY , ZOZ, and linearly combine the measure-
ment results to eﬀectively realise the inverse channel,
thus obtaining the noiseless measurement result ¯O0. The
variance in our estimate of ¯O0 is increased by a factor
of γG, where γ is the overhead coeﬃcient, and G is the
number of gates in the circuit.
In practice, it is not possible to exactly measure all
of the possible terms resulting from errors if there are

many gates in the circuit.
Instead, we can consider
only the most important terms, which result from a
small number of errors occurring.
If the error rate is
low, then the other terms can be considered negligibly
small.
After each single qubit gate, we can apply X,
Y or Z operators with probability p2, or the identity
gate with p1.
We repeat that circuit variant many
times to extract the expectation value, and multiply the
expectation value by (−1)Gp, where Gp is the number
of additional X, Y or Z gates that were applied in that
circuit iteration. We then sum up the values for several
circuit variants and multiply by γ to obtain the error
mitigated result.
This method can also be extended
to multi-qubit gates. For example, for two qubit gates
in the depolarising noise model, after each two qubit
gate we insert one of the pairs: XI, IX, Y I, IY, ZI, IZ
(parity −1) with probability p2,
one of the pairs
XX, Y Y, ZZ, XY, Y X, XZ, ZX, Y Z, ZY
(parity
+1)
with probability p2 and II (parity +1) with probability
p1.

The probabilistic error cancellation method described
above has been shown to work for general Markovian
noise (Endo et al., 2017), and has also been extended to
work with temporally correlated errors and low frequency
noise (Huo and Li, 2018). Probabilistic error cancella-
tion requires full knowledge of the noise model associated
with each gate. This can be obtained from either process
tomography, or a combination of process and gate set
tomography. The latter approach reduces the eﬀect of
errors due to state preparation and measurement (Endo
et al., 2017). The probabilistic error cancellation method
has been experimentally demonstrated on both supercon-
ducting (Song et al., 2018) and trapped ion (Zhang et al.,
2019) systems.

C. Quantum subspace expansion

The quantum subspace expansion (QSE) (McClean
et al., 2017a) described in Sec. V.C.1 can mitigate errors
in the VQE, in addition to calculating the excited energy
eigenstates. This method is most eﬀective at correcting
systematic errors, but can also suppress some stochastic
errors. Suppose that we use the VQE to ﬁnd an approx-
imate ground state | ˜E0⟩. Noise may cause this state to
deviate from the true ground state |E0⟩. For example,
if | ˜E0⟩= X1 |E0⟩, we can simply apply an X1 gate to
recover the correct ground state.
However, as we do not know which errors have oc-
curred, we can instead consider an expansion in the sub-
space {|Pi ˜E0⟩}, where Pi are matrices belonging to the
Pauli group. Then, one can measure the matrix repre-
sentation of the Hamiltonian in the subspace,

HQSE
ij
= ⟨˜E0| PiHPj | ˜E0⟩.
(85)

## Page 41

As the subspace states are not orthogonal to each other,
we should also measure the overlap matrix

SQSE
ij
= ⟨˜E0| PiPj | ˜E0⟩.
(86)

By solving the generalised eigenvalue problem

HQSEC = SQSECE,
(87)

with a matrix of eigenvectors C and diagonal matrix of
eigenvalues E, we can get the error mitigated spectrum
of the Hamiltonian. A small number of Pauli group op-
erators are typically considered, in order to minimise the
required number of measurements. The QSE has been
experimentally demonstrated, using a two qubit super-
conducting system to measure the ground and excited
state energies of H2 (Colless et al., 2018).

D. Symmetry based methods

It is also possible to mitigate some errors by us-
ing symmetry checks on a suitably constructed ansatz
state (Bonet-Monroig et al., 2018; McArdle et al., 2018c).
A key concern for the VQE is preserving particle num-
ber, as states with electron number far from the true
value appear to have a larger energy variance than those
with smaller particle number errors (Sawaya et al., 2016).
Consequently, we can perform ‘checks’ on quantities
which should be conserved (such as number of electrons,
or sz value), discarding the results if the measured value
is not as expected.
This can be achieved in a number of ways: by using
stabiliser checks with additional ancilla qubits (Bonet-
Monroig et al., 2018; McArdle et al., 2018c),
by
taking additional measurements and performing post-
processing
(Bonet-Monroig
et
al.,
2018)
(this
has
been experimentally demonstrated in superconducting
qubits (Sagastizabal et al., 2019)), by enforcing physi-
cally derived constraints on the form of the measured
1 and 2-RDMs (known as the n-representability con-
straints) (Rubin et al., 2018), or by using the low-rank +
orbital rotations measurement technique of Huggins et al.
(2019b) (discussed in Sec. V.B.2). The latter method ap-
pears to be the most powerful of these, requiring a mod-
est additional circuit depth, limited connectivity, and en-
abling eﬀective post-selection on the electron number and
sz value, rather than just the parities of these quantities.
These methods of error mitigation can be combined with
some of the other techniques discussed above, such as
extrapolation.
A related extension of the quantum subspace expan-
sion was developed by McClean et al. (2019b), who ef-
fectively engineered additional symmetries in the system
using an error correcting code. By post-processing mea-
surements from multiple iterations, they could detect
some errors, or eﬀectively realise a limited form of er-
ror correction. In order to maintain a polynomial cost

for the procedure, the authors introduced a stochastic
sampling scheme for the code stabilisers.

The choice of fermion-to-qubit mapping can also intro-
duce additional symmetries. For example, both the gen-
eralised Bravyi-Kitaev superfast transform (Setia et al.,
2018), and the majorana loop stabiliser code (Jiang et al.,
2018a) (discussed in Sec. IV.B.3) introduce additional
qubits, whose values are constrained by the mappings.
By performing suitable stabiliser checks on these qubits,
single qubit errors can be detected and corrected.

E. Other methods of error mitigation

Other methods of error mitigation have been proposed,
but require further research in order to assess how they
can be best incorporated into chemistry calculations.
One such method is the quantum variational error cor-
rector (Johnson et al., 2017), which uses a variational al-
gorithm to construct noise-tailored quantum memories.
Another example is individual error reduction (Otten and
Gray, 2018a). This method uses error correction to pro-
tect a single qubit, while leaving the rest of the physical
qubits subject to noise.
The process is repeated sev-
eral times, with each physical qubit being protected in
turn. Post-processing the results produces a more accu-
rate expectation value than would be obtained without
the mitigation technique.

VII. ILLUSTRATIVE EXAMPLES

In this section we illustrate many of the techniques de-
scribed in the previous sections of this review, by explic-
itly demonstrating how to map electronic structure prob-
lems onto a quantum computer. We do this in second
quantisation for the Hydrogen molecule (H2) in the STO-
3G, 6-31G and cc-PVDZ bases, and Lithium Hydride
(LiH) in the STO-3G basis (as described in Sec. III.D).
Across these examples, we showcase the Jordan–Wigner
(JW), Bravyi–Kitaev (BK) and BK tree mappings (as de-
scribed in Sec. IV.B), reduction of active orbitals using
the Natural Molecular Orbital (NMO) basis (as described
in Sec. III.E), reduction of qubits using symmetry conser-
vation (as described in Sec. IV.C.1) and the unitary cou-
pled cluster ansatz (as described in Sec. V.B.1). These
examples are designed to familiarise the reader with the
key steps of formulating a quantum computational chem-
istry problem. Many of these techniques are applicable
to both ground state and general chemical problems.

A. Hydrogen

The continuous space molecular Hamiltonian for H2 is
given by Eq. (17) (which we reproduce here), with two

## Page 42

FIG. 10 Comparing the ground state dissociation curves of
H2 for a range of basis sets.

electrons and two nuclei

∇2
i
2 −
X

ZI
|ri −RI| + 1

1
|ri −rj|. (88)

HH2 = −
X

X

2

i

i̸=j

i,I

To convert this Hamiltonian into the second quantised
representation,

p,q
hpqa†
paq + 1

H =
X

X

p,q,r,s
hpqrsa†
pa†
qaras,
(89)

2

with

!

−∇2

ZI
|r −RI|

hpq =
Z
dxφ∗
p(x)

2 −
X

φq(x),

I

hpqrs =
Z
dx1dx2
φ∗
p(x1)φ∗
q(x2)φr(x2)φs(x1)

|x1 −x2|
,

(90)
we need to select a basis set, φp(x).
As discussed in
Sec. III.D, this is a discrete set of functions which are
used to approximate the spin-orbitals of the molecule.
By considering a larger number of orbitals (and the Slater
determinants that they can generate), we are able to re-
cover a larger proportion of the correlation energy in a
molecule, resulting in a more accurate estimate of the
true ground state energy. Fig. 10 shows the H2 ground
state dissociation curves in the STO-3G, 6-31G and cc-
PVDZ bases. We can see that the diﬀerences in energy
between the three minima are considerably larger than
chemical accuracy (1.6 mHartree). This highlights that
working in a suitably large basis set is crucial for obtain-
ing accurate results.

1. STO-3G basis

The STO-3G basis for H2 includes only the {1s} orbital
for each hydrogen atom. The 1s orbital is represented

by a linear combination of three Gaussian type orbitals.
Each hydrogen atom contributes one orbital, and there
are two possible spins for each orbital – resulting in a
total of 4 spin-orbitals for STO-3G H2. We denote these
orbitals as

|1sA↑⟩, |1sA↓⟩, |1sB↑⟩, |1sB↓⟩,
(91)

where the subscript A or B denotes which of the two
atoms the spin-orbital is centred on, and the ↑/ ↓de-
notes the sz value of the electron in the spin-orbital. For
convenience, we work in the molecular orbital basis for
H2, which is simple to construct manually. These single
electron molecular spin-orbitals are given by

|σg↑⟩=
1
p

Ng
(|1sA↑⟩+ |1sB↑⟩),

|σg↓⟩=
1
p

Ng
(|1sA↓⟩+ |1sB↓⟩),

(92)

|σu↑⟩=
1
√Nu
(|1sA↑⟩−|1sB↑⟩),

|σu↓⟩=
1
√Nu
(|1sA↓⟩−|1sB↓⟩),

where Ng/u are normalisation factors that depend on
the overlap between the atomic orbitals, Ng = 2(1 +
⟨1sA|1sB⟩), Nu = 2(1 −⟨1sA|1sB⟩).
We can write a
Slater determinant in the occupation number basis as

|ψ⟩= |fσu↓, fσu↑, fσg↓, fσg↑⟩,
(93)

where fi = 1 if spin-orbital i is occupied, and fi = 0
if spin-orbital i is unoccupied.
We can now calculate
the integrals given in Eq. (90) using these molecular or-
bitals. These integrals have been calculated for a large
number of basis sets, and the results can be obtained by
using a computational chemistry package (Frisch et al.,
2016; Muller, 2004; Parrish et al., 2017; Sun et al., 2017).
We must then map the problem Hamiltonian from being
written in terms of creation and annihilation operators,
to being written in terms of qubit operators. Using the
JW encoding, we can obtain the 4 qubit Hamiltonian for
H2

H = h0I + h1Z0 + h2Z1 + h3Z2 + h4Z3
+ h5Z0Z1 + h6Z0Z2 + h7Z1Z2 + h8Z0Z3 + h9Z1Z3
+ h10Z2Z3 + h11Y0Y1X2X3 + h12X0Y1Y2X3
+ h13Y0X1X2Y3 + h14X0X1Y2Y3.
(94)
While it is important to understand this procedure,
every step from selecting a basis to producing an
encoded qubit Hamiltonian can be carried out using
a
quantum
computational
chemistry
package
such
as
OpenFermion
(McClean
et
al.,
2017b),
Qiskit
Aqua (IBM, 2018), or QDK-NWChem (Low et al.,
2019a).

## Page 43

In the JW encoding, it is simple to construct the
Hartree-Fock (HF) state for the H2 molecule. The HF
state for H2 in the occupation number basis is given by

|ΨH2
HF⟩= |0011⟩.
(95)

This represents the Slater determinant

ΨH2
HF(r1, r2) =
1
√

2(σg↑(r1)σg↓(r2) −σg↑(r2)σg↓(r1)),

(96)
where ri is the position of electron i. The most general
state for H2 (with the same sz value and electron number
as the HF state) is given by

|ΨH2⟩= α |0011⟩+ β |1100⟩+ γ |1001⟩+ δ |0110⟩, (97)

and the ground state of the H2 molecule at its equilibrium
bond distance is given by (Helgaker et al., 2014)

|ΨH2
g ⟩= 0.9939 |0011⟩−0.1106 |1100⟩.
(98)

The ﬁrst determinant in the ground state wavefunction
is the HF state for H2, showing that a mean-ﬁeld solu-
tion is a good approximation for this molecule at this
interatomic distance. The second determinant represents
the antibonding state, and accounts for dynamical cor-
relation between the electrons due to their electrostatic
repulsion. While the HF determinant dominates at the
equilibrium separation, at large separation the two de-
terminants contribute equally to the wavefunction. This
is because the bonding and antibonding conﬁgurations
become degenerate.
We require both determinants to
accurately describe the state, ensuring that only one
electron locates around each atom. This is an example
of static correlation, which can also be dealt with using
multiconﬁgurational self-consistent ﬁeld methods,
as
described in Sec. III.C.1.

As discussed previously, in order to ﬁnd the ground
state of the H2 molecule (using either the VQE or phase
estimation), we need to construct the state on the quan-
tum computer. Here we explicitly derive the unitary cou-
pled cluster (UCC) ansatz with single and double excita-
tions (UCCSD) for H2. As discussed in Sec. V.B.1, the
UCCSD operator we seek to realise is given by

U = e(T1−T †
1 )+(T2−T †
2 ),

i∈virt,α∈occ
tiαa†
iaα,

T1 =
X

(99)

i,j∈virt,α,β∈occ
tijαβa†
ia†
jaαaβ,

T2 =
X

where occ are initially occupied orbitals in the HF state,
virt are initially unoccupied orbitals in the HF state, and
tiα and tijαβ are variational parameters to be optimised.
For H2, the only operators which do not change the sz

value of the molecule when acting upon the HF state are:
a†
2a0, a†
3a1, a†
3a†
2a1a0. Other valid operators are equiva-
lent to these operators, and can be combined with them,
such as a†
3a†
0a1a0 = −a†
3a1.
As a result, the UCCSD
operator takes the form

U = et02(a†
2a0−a†
0a2)+t13(a†
3a1−a†
1a3)+t0123(a†
3a†
2a1a0−a†
0a†
1a2a3).
(100)
We can split this operator using Trotterization with a
single Trotter step

U = et02(a†
2a0−a†
0a2) × et13(a†
3a1−a†
1a3)

× et0123(a†
3a†
2a1a0−a†
0a†
1a2a3).
(101)

Using the JW encoding, we ﬁnd that

(a†
2a0 −a†
0a2) = i

2(X2Z1Y0 −Y2Z1X0)

(a†
3a1 −a†
1a3) = i

2(X3Z2Y1 −Y3Z2X1)

(a†
3a†
2a1a0 −a†
0a†
1a2a3) =
i
8(X3Y2X1X0 + Y3X2X1X0 + Y3Y2Y1X0 + Y3Y2X1Y0

−X3X2Y1X0 −X3X2X1Y0 −Y3X2Y1Y0 −X3Y2Y1Y0).
(102)
It was shown by Romero et al. (2019) that all Pauli terms
arising from the same excitation operators commute. As
a result, each of the exponentials in Eq. (101) can be
separated into a product of exponentials of a single Pauli
string. For example

et02(a†
2a0−a†
0a2) = e

−it02

it02

2
X2Z1Y0 × e

2
Y2Z1X0.
(103)

Hempel et al. (2018) simpliﬁed the UCCSD operator for
H2 by implementing the single excitation terms as ba-
sis rotations, and combining terms in the double excita-
tion operator (by considering the eﬀect of each term on
the HF state). This latter technique is only possible be-
cause there is only one double excitation operator for this
molecule, and so is not a scalable technique in general.
The UCCSD operator is simpliﬁed to

U = e−iθX3X2X1Y0.
(104)

This can be implemented using the circuit
(Whitﬁeld
et al., 2011) shown in Fig. 11.
Applying the simpliﬁed UCCSD operator to the HF
state in Eq. (95) gives

U |0011⟩= (cos(θ)I −isin(θ)X3X2X1Y0) |0011⟩,

= cos(θ) |0011⟩−sin(θ) |1100⟩,
(105)

which can reproduce the ground state given by Eq. (98).

2. 6-31G basis

As discussed in Sec. III.D, H2 in the 6-31G basis
has a double-zeta representation of the valence elec-
trons. This means we have 8 spin-orbitals to consider

## Page 44

σg↑: |1⟩
Rx( π

FIG. 11 The circuit for implementing the UCCSD operator
for H2 in the STO-3G basis, as given by Eq. (104). The Rx( π

2 )
and Had gates rotate the basis such that the exponentiated
operator applied to the corresponding qubit is either Y or X,
respectively. Single excitation terms are implemented with a
change of basis (Hempel et al., 2018).

in total; {1s↑, 1s↓, 1s′
↑, 1s′
↓} from each atom.
Working
in the canonical orbital basis, (obtained by performing
a Hartree–Fock calculation) we show how to construct
Bravyi-Kitaev encoded states of 6-31G H2.
The BK
transform matrix for an 8 spin-orbital system is given
by





1 0 0 0 0 0 0 0









































1 1 0 0 0 0 0 0

0 0 1 0 0 0 0 0

1 1 1 1 0 0 0 0

.
(106)

0 0 0 0 1 0 0 0

0 0 0 0 1 1 0 0

0 0 0 0 0 0 1 0

1 1 1 1 1 1 1 1

We order the spin-orbitals such that the ﬁrst M/2 spin-
orbitals are spin up, and the ﬁnal M/2 spin-orbitals are
spin down. When the spin-orbitals are ordered in this
way, the 4th entry in the BK encoded vector is the sum
(mod 2) of the spin up occupancies, which sums to the
number of spin up electrons. Moreover, the 8th entry is
the sum (mod 2) of all of the orbital occupancies, which
sums to the number of electrons. As these quantities are
conserved, we can remove these two qubits from the sim-
ulation, following the procedure of Sec. IV.C. If the spin-
orbitals are arranged ‘up-down, up-down’, then while the
8th entry is still equal to the number of electrons, the
4th entry is no longer necessarily equal to a conserved
quantity. The JW mapped HF state (8 qubits) is given
by |00010001⟩. Using the matrix given above, the BK
mapped HF state (8 qubits) is |00111011⟩.
When the
two conserved qubits are removed, the BK mapped HF
state (6 qubits) is |011011⟩.

3. cc-PVDZ basis

As discussed in Sec. III.D, the cc-PVDZ basis for H2
includes a double-zeta representation of the valence shell,
and additional polarisation orbitals.
Each atom con-
tributes {1s, 1s′, 2px, 2py, 2pz} orbitals, resulting in 20
spin-orbitals in total.
In order to reduce our active
space, we ﬁrst change to the natural molecular orbital
(NMO) basis, using the single particle reduced density
matrix (1-RDM), as discussed in Sec. III.E. We ﬁrst ob-
tain the 1-RDM for H2 in the cc-PVDZ basis with a
classically tractable conﬁguration interaction singles and
double (CISD) calculation.
We perform a unitary diagonalisation of this ma-
trix, and rotate the orbitals by the same unitary ma-
trix.
This constitutes a change of basis to the NMOs
of the molecule.
The diagonalised 1-RDM is given by
Diag(1.96588, 0.00611, 0.02104, 0.0002, 0.00001, 0.00314,
0.00314, 0.00016, 0.00016, 0.00016). There are only 10
diagonal entries in this 1-RDM because the spin-up and
spin-down entries for the same spatial orbitals have been
combined. As discussed in Sec. III.E, the diagonal entries
are the natural orbital occupation numbers (NOONs).
We can see that the 5th orbital has a NOON that is 20
times smaller than the next smallest NOON. As a result,
we consider this spatial orbital to always be empty, and so
remove all terms involving it from the Hamiltonian. This
leaves a Hamiltonian acting on M = 18 spin-orbitals. We
now map these into qubits using the BK-tree method.
To map fermionic orbitals to qubits we follow a similar
procedure to that shown in Fig. 12 for the LiH molecule.
The reader will ﬁnd that the 9th and 18th orbitals store
the number of spin up electrons and total number of elec-
trons, respectively.
As a result, they can be removed.
This reduces the problem to one of 16 qubits.
The lowest energy computational basis state of cc-
PVDZ H2 in the Jordan-Wigner encoding (18 qubits)
is |000000001000000001⟩.
The corresponding BK-tree
mapped state (16 qubits) is given by |0001011100010111⟩.
We stress that while this procedure may seem complex,
it can in fact be easily implemented using the functions
available in the aforementioned quantum computational
chemistry packages.

B. Lithium Hydride STO-3G basis

For
LiH
in
the
STO-3G
basis,
we
consider
{1s, 2s, 2px, 2py, 2pz}
functions
for
lithium,
and
a
single {1s} orbital for hydrogen. This gives a total of
12 spin-orbitals. We can reduce this problem to one of
six qubits, as illustrated in Fig. 12. The 1-RDM in the
canonical orbital basis from a CISD calculation on LiH
(at an internuclear separation of 1.45 ˙A) is given by

## Page 45

FIG. 12 A pictorial representation of the fermion-to-qubit mapping procedure for LiH in the STO-3G basis. The fermionic nat-
ural molecular orbitals (NMO) are initially arranged ‘spin up, spin down, spin up, spin down, ...’, and have their corresponding
natural orbital occupation number (NOON) below. As the NOON of orbitals 6 and 7 is so small, they can be assumed unﬁlled,
and removed from the Hamiltonian. As the combined NOON of orbitals 0 and 1 is close to 2, they can be assumed ﬁlled, and
removed from the Hamiltonian. We then rearrange the remaining orbitals to be ‘all spin up, all spin down’, and re-label them
from 0 to 7. We then perform the BK-tree mapping by constructing the Fenwick tree, Fen(0,7), as described in Fig. 13. The
value xi is the value of the ith qubit under the BK-tree mapping, while ni is the value of the ith qubit under the JW mapping.
We see that qubit 3 stores the sum P3
i=0 ni, and qubit 7 stores the sum P7
i=0 ni. As these sums are conserved quantities, these
qubits do not ﬂip throughout the simulation, and so can be removed from the Hamiltonian as described in Sec. IV.C.





1.9999
−0.0005
0.0006
0.0000
0.0000 −0.0010





























−0.0005
1.9598
0.0668
0.0000
0.0000
0.0084

0.0006
0.0668
0.0097
0.0000
0.0000 −0.0138

.

0.0000
0.0000
0.0000
0.0017 0.0000
0.0000

0.0000
0.0000
0.0000
0.0000 0.0017
0.0000

−0.0010
0.0084
−0.0138 0.0000
0.0000
0.0273

There are only 6 rows/columns in this 1-RDM because
the spin-up and spin-down entries for the same spatial or-
bitals have been combined. We diagonalise this 1-RDM,
moving to the NMO basis. The NMO 1-RDM is given by





1.99992
0.00000
0.00000
0.00000
0.00000
0.00000





























0.00000
1.96206
0.00000
0.00000
0.00000
0.00000

0.00000
0.00000
0.03454
0.00000
0.00000
0.00000

.

0.00000
0.00000
0.00000
0.00005
0.00000
0.00000

0.00000
0.00000
0.00000
0.00000
0.00171
0.00000

0.00000
0.00000
0.00000
0.00000
0.00000
0.00171

The ﬁrst orbital has a NOON close to two, and so we con-
sider it to always be doubly occupied. We can then re-
move any terms containing a†
0, a0, a†
1, a1 (the spin-orbitals
corresponding to the ﬁrst spatial orbital in the 1-RDM)

from the Hamiltonian.
In contrast, the fourth orbital
has a very small NOON. As a result, we assume that this
orbital is never occupied, and so remove the two corre-
sponding fermion operators from the Hamiltonian. This
leaves a Hamiltonian acting on 8 spin-orbitals. As the
number of orbitals is now a power of 2, we can use ei-
ther the BK or BK-tree mappings to remove the 2 qubits
associated with conservation symmetries.
We use the
BK-tree mapping in order to provide an explicit example
of Fenwick tree construction. The Fenwick tree tells us
which qubits store which orbitals in the BK-tree map-
ping. We denote the Fenwick tree for the M orbitals as
Fen(0, M −1). We can obtain this data structure using
an iterative algorithm, which we reproduce from Havlicek
et al. (2017) below. The generation of the Fenwick tree
for the LiH molecule using this algorithm is shown in
Fig. 13.

Our ﬁnal Hamiltonian acts on 6 qubits, but diﬀers
in energy from the full 12 qubit Hamiltonian by only
0.2 mHartree.
A similar procedure is described by
Hempel et al. (2018).

## Page 46

FIG. 13 A pictorial representation of the Fenwick tree construction for LiH, shown in Fig. 12. We carry out the BK-tree
mapping by constructing the Fenwick tree, Fen(0,7), as described in Algorithm. 1. The algorithmic steps are shown on the left
hand side of the ﬁgure, while the corresponding actions are shown on the right hand side. The notation X →Y means connect
spin-orbital X to spin-orbital Y with an arrow. ‘Fin’ means that the corresponding branch of the Fenwick tree is ﬁnished. The
ﬁnished Fenwick tree Fen(0,7) is shown at the bottom of the ﬁgure.

calculations on smaller system sizes. We conclude this
review in Sec. VIII with a blueprint for future investiga-
tions.

A. Classical limits

As discussed in Sec. III, there are many diﬀerent meth-
ods used in classical computational chemistry, which all
seek to approximate the true ground state energy of the
system of interest, to varying degrees of accuracy. In gen-
eral, the cost of applying these methods grows with the
accuracy of the results that they produce, and the size
of the system simulated. In this section, we discuss the
system sizes that one can typically accurately treat using
some of the commonly used classical methods. This will
help us to elucidate where, and when, quantum comput-
ers may become useful for chemistry simulation. As in
previous sections, M denotes the number of spin-orbitals
considered in basis set approaches, and N denotes the
number of electrons in the system.
At one end of the spectrum are density functional the-
ory (DFT), and the Hartree-Fock (HF) method. These
calculations are often very eﬃcient to run, and can treat
large systems.
As a result, they are used widely in
chemistry and materials science.
However, these tech-
niques can struggle to achieve highly accurate results for
strongly correlated systems, and are not systematically
improvable. Consequently, they are often used for ob-
taining qualitative results for large system sizes. We do
not expect these calculations to be replaced by those on
quantum computers, given the large system sizes that are
simulated.

VIII. DISCUSSION AND CONCLUSIONS

We have now reviewed the key concepts in both clas-
sical, and quantum, computational chemistry. In partic-
ular, we have discussed and shown how to map chemi-
cal problems onto quantum computers, and how to solve
them to obtain both the ground and excited states. We
now turn our attention to how these techniques com-
pare to the established classical methods discussed in
Sec. III. We will ﬁrst review the applicability and lim-
itations of the various classical methods, in Sec. VIII.A.
This will highlight the problems for which quantum com-
puters may one day be useful. We discuss the resources
required for such calculations in Sec. VIII.B. We will
see that the resources required are considerably greater
than what we currently have available, at time of writing.
Consequently, in Sec. VIII.C we consider routes towards
these calculations. This will include both heuristic calcu-
lations on classically intractable system sizes, and exact

## Page 47

At the other end of the spectrum, are exact cal-
culations – by which we mean the exact energy that
can be obtained from the model of the system.
It is
important to note that these ‘exact’ calculations are
rarely performed.
Moreover, the degree of accuracy
depends on the details included in the calculation, such
as: the inclusion of relativistic corrections, whether the
Born-Oppenheimer approximation is used, or whether
nuclear vibrational and rotational contributions are
included.
Grid-based simulations (as described in
Sec. III.B.1) provide the most accurate results – but can
only be carried out for a very small number of particles,
because of the large number of grid points required.
Exact results (albeit with a less accurate model of the
system) can also be obtained by carrying out basis
set,
full conﬁguration interaction (FCI) calculations
(Sec. III.B.2), which are less computationally expensive
than grid based approaches. However, the cost of these
calculations still scales exponentially with the system
size, so they are only applicable to small systems, like
the dinitrogen molecule (Rossi et al., 1999).
In the
context of condensed matter physics, these calculations
are referred to as ‘exact diagonalisation’ and are possible
up to system sizes of around 20 to 30 lattice sites, in
the case of Fermi-Hubbard models (Jiang et al., 2018b;
Yamada et al., 2005).

functions (Booth and Alavi, 2010)), as well as state of the
art results in Fermi-Hubbard systems that are accurate
to around 100 sites (LeBlanc et al., 2015), and less accu-
rate results in other, larger systems (Austin et al., 2012).
However, Monte Carlo methods are not without their
own shortcomings, including the infamous ‘sign problem’,
that aﬀects fermionic simulations (Austin et al., 2012;
Ortiz et al., 2001).
Tensor network methods, such as density matrix renor-
malisation group (DMRG), have proven eﬀective for
dealing with systems displaying strong static correla-
tion. They provide an alternative approach to CASSCF
(see Sec. III.C.2) approaches (Knecht et al., 2016), al-
lowing the treatment of larger active spaces, including
those of metalloenzyme complexes with active spaces of
over 70 spin-orbitals (Kurashige et al., 2013; Sharma
et al., 2014). This is larger than the roughly 30 to 40
spin-orbitals that can be treated with a CASSCF ap-
proach (Lischka et al., 2018). Tensor network methods
are also useful for treating systems in condensed matter
physics, including Fermi-Hubbard models that are accu-
rate to around 100 sites (LeBlanc et al., 2015). While ten-
sor network methods are best suited to dealing with sys-
tems with strong static correlation, recent work has inves-
tigated post-DMRG methods to recover dynamic corre-
lation (Knecht et al., 2016; Yanai et al., 2015). For more
information on the use of DMRG in quantum chemistry,
we refer the reader to the reviews by Olivares-Amaya
et al. (2015) and Szalay et al. (2015).
We can see from the above discussion that there ap-
pears to be an untreated ‘sweet spot’, of systems with
around 100 to 200 spin-orbitals, that require high ac-
curacy calculations.
These systems are too strongly
correlated to be tackled with methods like HF, DFT
or even CCSD. They are also too large to be reliably
dealt with using DMRG or quantum Monte Carlo, and
much too large for classical FCI methods. Interestingly,
many problems of scientiﬁc interest ﬁt this description,
including: transition metal catalysts (Podewitz et al.,
2011; Vogiatzis et al., 2019) and the Fermi-Hubbard
model (LeBlanc et al., 2015).
As we have discussed
throughout this review, a small quantum computer, with
around 100 perfect qubits, would be able to calculate the
FCI energy of a system with around 100 spin-orbitals in
polynomial time. This would imply that these problems
are among the best targets for quantum computers.
It is important to note that being able to accurately
predict the ground state energy of 100 spin-orbital
systems still leaves us far from our long-term goal of
designing new medicines and materials with simulations.
For example, Yamazaki et al. (2018) noted that over
95 % of the approved drug molecules in DrugBank 5.0
are larger than these 100-200 spin-orbital systems that
we might aim to simulate with a small, error-corrected
quantum computer. However, in practice it is not always
necessary to perform highly accurate calculations on the

The vast majority of calculations carried out by the
computational chemistry community do not achieve this
level of accuracy.
Instead, approximate, less costly
methods are used, such as:
conﬁguration interaction
(Sec. III.C.3), coupled cluster (Sec. III.C.4) multiconﬁg-
urational self-consistent ﬁeld (Sec. III.C.2), tensor net-
work methods, or quantum Monte Carlo. An exhaustive
comparison of these methods is beyond the scope of this
review, as is attempting to catalogue the ever-evolving
list of the largest calculations performed. However, we
will brieﬂy highlight some of the system sizes where these
methods have been successfully applied.
Coupled cluster methods (often CCSD) are some of
the most widely used high-accuracy methods.
They
are applicable to large systems (hundreds of spin-
orbitals (Bartlett and Musia l, 2007)) which do not
display strong static correlation.
Examples include:
the DNA base guanine (C5H5N5O) in a cc-PVTZ ba-
sis (Hobza and Sponer, 2002), or the hydrocarbon octane
(C8H18) also in a cc-PVTZ basis (Yamazaki et al., 2018).
While CC methods can also be applied to strongly cor-
related systems (LeBlanc et al., 2015; Watson and Chan,
2012), higher excitation degrees are often required, mak-
ing the method more costly to implement.
Quantum Monte Carlo has many variants, and has
been used to obtain results comparable to FCI in rel-
atively small systems (the Cr2 molecule with 24 active
electrons in 30 spin-orbitals (Tubman et al., 2016), or
the ﬂuorine atom in a cc-PV5Z basis with additional basis

## Page 48

entirety of a large molecule or enzyme. Instead, problem
decomposition approaches can be utilised,
whereby
the most important part of the system is accurately
simulated, and then integrated with a potentially less
accurate simulation of the less challenging parts of the
system.
This approach has been investigated in the
context of quantum computing by Bauer et al. (2016);
Kreula et al. (2016); Reiher et al. (2017); Rubin (2016);
and Yamazaki et al. (2018).

B. Quantum resources: medium to long-term

As discussed in Sec. IV.B, quantum computers can
store the FCI wavefunction of M spin-orbitals using only
M qubits in second quantisation. However, as discussed
in Sec. II, we must also take into consideration the qubit
overhead of error correction. Initial work suggested that
around 1018 gates would be necessary to perform phase
estimation on a system of around 100 spin-orbitals (ex-
cluding the overhead of error correction) (Wecker et al.,
2014). This estimate was subsequently reduced through
a series of algorithmic optimisations, as described in
Sec V.A.4.a.
These initial estimates did not focus on speciﬁc prob-
lems of interest, and neglected the overhead of quantum
error correction, which is necessitated by the large
number of gates needed. Fault-tolerant resource estima-
tions have since been carried out for two main systems:
small transition metal molecules, and condensed phase
materials (including 2D Fermi-Hubbard models, 2D and
3D electron gases, and solid materials, such as lithium
or diamond). When performing fault-tolerant resource
estimates, one must specify details of the problem, the
hardware considered, and the error correcting code
used.
All resource estimates to date have focused on
the 2D surface code, due to its high threshold, and
suitability for architectures with a 2D nearest-neighbour
connectivity.
In the standard model of surface code
resource estimation, Cliﬀord gates (such as Pauli gates
and the CNOT gate) are considered to be of negligible
cost, while non-Cliﬀord gates (such as the T gate, or
Toﬀoli gate) are more costly.
This is because these
non-Cliﬀord gates cannot be natively implemented in a
fault-tolerant way in the surface code, but instead are
typically implemented using magic state distillation and
teleportation (Bravyi and Kitaev, 2005), which is often
expensive (Campbell et al., 2017). As a result, algorithm
complexities are measured in terms of the number of T
and/or Toﬀoli gates that they contain, as these are often
the dominant contribution to the cost of the algorithm.
There has been considerable work to reduce the cost
of operations in the surface code (including magic
state distillation), which has reduced the overhead of
error correction by several orders of magnitude (Fowler

and Gidney, 2018; Gidney and Fowler, 2019; Litinski,
2019a,b; Trout and Brown, 2015). These improvements,
combined
with
the
algorithmic
advances
described
throughout this review, have contributed to a signiﬁ-
cant reduction in the resources required for chemistry
calculations, compared to the initial estimates. In order
to distinguish algorithmic advances from fault-tolerance
improvements, we list both the number of T and/or
Toﬀoli gates required for the simulation, as well as the
corresponding number of physical qubits, obtained using
the best fault-tolerance procedures available at that
work’s time of writing.

Reiher et al. (2017) carried out a fault-tolerant re-
source estimation for the problem of biological dinitro-
gen ﬁxation, as described in Sec. III.A.1. Those authors
calculated the resources required to perform an FCI cal-
culation on an active space of 54 electrons in 108 spin-
orbitals for FeMo-co, using a Trotter-based approach to
phase estimation.
They found that this would require
around 1014 T gates. Assuming the best physical error
rates (10−3) at our time of writing, this would require
around 200 million physical qubits, and take on the order
of weeks (10 ns to implement a T gate, including surface
code decoding) or months (100 ns per T gate) (Reiher
et al., 2017). We note that those authors were considering
a targeted majorana fermion-based quantum computer,
with physical error rates 103 times lower than has been
demonstrated in trapped ion or superconducting qubits,
at our time of writing.

A similar resource estimation (although using the more
accurate FeMo-co active space of Li et al. (2018), with
113 electrons in 152 spin-orbitals) was carried out by
Berry et al. (2019b), who used the algorithm based on
qubitization and low-rank decompositions of the Hamil-
tonian, described in Sec. V.A.4. This approach reduced
the resources required to around 1011 Toﬀoli gates (which
are currently the bottleneck for this approach). While a
complete fault-tolerant resource analysis for this new ap-
proach has not yet been performed, those authors showed
that the cost of Toﬀoli gate distillation is equivalent to
around 1 million physical qubits, working for 2 months
(assuming 10−3 error rates and surface code cycle times
of 1 µs), at our time of writing.

Other works have conducted similar resource esti-
mations for equivalently sized problems (100-200 spin-
orbitals), but have focused on matter in the condensed
phase. This enables the use of the plane wave dual ba-
sis (Sec. III.D.3), which as discussed in Sec. V.A.4.b can
reduce the costs of simulations. Babbush et al. (2018b)
used the algorithm based on qubitization in a plane dual
wave basis (discussed in Sec. V.A.4.b) to obtain resource
estimates of around 2 × 108 T gates for a 128 spin-
orbital 3D homogeneous electron gas (with similar re-
sults for other 3D materials), and around 7.1 × 108 T

## Page 49

gates for the 2D Fermi-Hubbard model with 100 lattice
sites (200 spin-orbitals). Assuming error rates of 10−3,
1 µs to implement a T gate (including surface code de-
coding), and 10 µs feedforward, this led to resources of
around 2-3 million qubits, running for tens of hours (us-
ing the best fault-tolerance protocols available when that
work was completed). Subsequent improvements in fault-
tolerance protocols have further reduced these physical
resources (Fowler and Gidney, 2018; Gidney and Fowler,
2019; Litinski, 2019a,b).

Kivlichan et al. (2019a) also performed resource es-
timations for condensed matter and solid state prob-
lems, using the Trotter based algorithm discussed in
Sec. V.A.4.b. They considered simulations targeting a
size-extensive error in the energy (which is appropriate
when considering scaling to the thermodynamic limit).
They found that simulations of a 100 site Fermi-Hubbard
model, and a 128 spin-orbital homogeneous electron gas
would both require on the order of 106 Toﬀoli gates and
107 −108 T gates. Assuming error rates of 10−3, surface
code error detection times of 1 µs, and surface code er-
ror decoding times of 10 µs, they require around 400,000
– 600,000 physical qubits, running for a couple of hours.
As these simulations consider a loose-but-rigorous bound
on the energy error (as discussed in Sec. V.A.5), these
resource estimates may be overly pessimistic. Kivlichan
et al. (2019a) found that if an intensive (e.g. absolute)
error in the energy is targeted, then their algorithm was
less eﬃcient than the qubitization algorithm of Babbush
et al. (2018b).

All of the resource estimation papers above focus on
the cost of phase estimation, and assume that the system
is prepared in an initial state that has a suﬃciently
large overlap with the true ground state. As discussed
in Sec. V.A.2, there are many techniques for state
preparation, including adiabatic state preparation, or
variational approaches. Tubman et al. (2018) presented
an algorithm which can prepare a suitable initial state by
leveraging a classical adaptive conﬁguration interaction
method.
This algorithm was numerically shown to
provide good estimates for the ground states of many
systems of interest in chemistry, physics and materials
science.
This stems from the fact that the dominant
Slater determinants in the wavefunction typically con-
verge much more quickly than the correlation energy.
Tubman et al. (2018) showed that the cost of this state
preparation algorithm is considerably lower than the
cost for phase estimation detailed above, and hence,
may be neglected for many systems of interest.
This
technique can also be combined with that of Berry et al.
(2018), which used classically obtained knowledge of
the energy eigenvalues to reduce the number of times
that phase estimation must be repeated. This reduced
the necessity of having a large overlap with the ground
state.

One might assume that grid based methods will
require considerably larger quantum computers than
basis set approaches, given the former’s non-compact
description of the wavefunction. However, as described
above, the ﬁgure of merit for fault-tolerant calculations
is often the circuit depth – in particular the number of T
or Toﬀoli gates. While an initial investigation into fault-
tolerant grid based simulation was performed (Jones
et al., 2012), it did not calculate the total number of T
gates required, or the number of qubits, for systems of
interest. As such, it is not directly comparable to the
methods described above.
The algorithm investigated
in that work (the algorithm of Kassal et al. (2008))
has since been surpassed by the algorithm of Kivlichan
et al. (2017).
Moreover, there have been many im-
provements in fault-tolerant circuit design and magic
state distillation since the work of Jones et al. (2012).
As classical computers are limited to small grid based
calculations, it would be an interesting direction of
future research to establish the quantum resources re-
quired to surpass these small, high accuracy calculations.

These results suggest that certain calculations with
around 100 spin-orbitals may be better suited to early
quantum computers than others. In particular, materials
in the condensed phase and Fermi-Hubbard simulations
so far require considerably fewer resources than simula-
tions of individual molecules. Despite these promising re-
sults, and recent, rapid improvements, we see that it still
requires on the order of 100, 000 physical qubits to sur-
pass classical techniques. Current quantum computers
possess only around 100 physical qubits, and we have yet
to demonstrate a fully protected logical qubit. It may be
many years before we possess a quantum computer with
the resources required to implement these algorithms,
given the challenges in scaling up hardware and perform-
ing quantum error correction (Gambetta et al., 2017).
In order to attempt to solve classically intractable chem-
istry problems before that time, diﬀerent approaches are
required. We discuss the potential paths towards these
classically intractable simulations below.

C. Quantum resources: near to medium-term

As discussed above, existing estimates for surpassing
classical calculations require on the order of 100,000 phys-
ical qubits, in order to implement quantum error correc-
tion. The ﬁrst generations of quantum computers will be
signiﬁcantly smaller than this.
Nevertheless, there are
many interesting avenues to pursue with these ﬁrst ma-
chines.
As discussed in Sec. V.B, the variational quantum
eigensolver (VQE) has received signiﬁcant attention in
recent years, due to its short required circuit depth (com-

## Page 50

pared to phase estimation). It has been speculated that
the VQE may enable small quantum computers with 100
to 200 physical qubits to surpass classical methods. Con-
siderable further work is required to demonstrate that
this will be possible. The VQE is a heuristic approach,
which attempts to generate an approximation to the
ground state wavefunction that is better than classical
methods, using a short circuit.
It is diﬃcult to prove
that a given circuit will be able to obtain a good esti-
mate for the ground state, especially when the diﬃculty
of classical optimisation is considered.
In general, the longer the circuit is, the better it can
approximate the ground state wavefunction.
However,
the length of circuit that we can implement without
error correction is heavily limited by noise.
A simple
calculation demonstrates the limited number of gates
that we have available.
If we assume a discrete error
model for our circuit, such that error events happen
probabilistically and independently following each gate
in the circuit, then even with an optimistic two qubit
gate error rate of 0.01 % (10 times better than the error
rates achieved to date), we could only carry out around
10,000 gates before we expect one or more errors to occur
in the circuit with high probability.
While the error
mitigation techniques discussed in Sec. VI may enable
us to recover accurate results from a circuit deeper than
10,000 gates, it seems unlikely that these methods alone
would enable more than a small multiplicative increase
in the circuit depth.

neglects constant factors, and so the number of gates
required would likely be higher. More thorough resource
estimates for the same problem on a silicon quantum
architecture were performed by Cai (2019). Our estimate
of 40,000 two-qubit gates is approximately equal to the
number of gates that we were limited to by noise in
our back-of-the-envelope calculation above.
There are
a number of routes to try and overcome the issue of
noise in such a calculation. We may be able to combine
existing error mitigation techniques, or try to develop
new ones.
We could also utilise ans¨atze which appear
robust to noise (Borregaard et al., 2019; Kim, 2017; Kim
and Swingle, 2017).

A less widely discussed approach is to perform
error corrected VQE simulations.
The aim would be
to suppress the error rate to a value low enough to
obtain chemically accurate energies from the simulation.
For example, we could use fermion-to-qubit mappings
which enable the detection and/or correction of single
qubit errors (Jiang et al., 2018a; Setia et al., 2018)
(discussed in Sec. IV.B.3 and Sec. VI.D). Alternatively,
we could explore using small error correcting codes. An
initial foray into this area was conducted by Urbanek
et al. (2019), who experimentally implemented a VQE
calculation on the H2 molecule encoded in the [[4,2,2]]
error detecting code. This calculation showed improved
accuracy over an un-encoded calculation, due to the use
of post-selection. Nevertheless, the use of error correct-
ing codes is complicated by the diﬃculty of producing
error protected T gates. As such, it is important to ask
if variational algorithms can be implemented with fewer
T gates than their phase estimation based counterparts.
As an example, the phase estimation based algorithm of
Kivlichan et al. (2019a) is already only a constant factor
less eﬃcient (in terms of T/Toﬀoli gates) than just
implementing time evolution under the Fermi-Hubbard
Hamiltonian directly (as is required for a Hamiltonian
variational ansatz). Moreover, synthesizing an arbitrary
angle rotation gate can require at least 10 to 100 T
gates.
For the hypothetical O(M 2) scaling variational
algorithm described above, we may still need around
4 × 105 to 4 × 106 T gates, neglecting constant factors.
This is comparable to the T gate counts required
for phase estimation based approaches described in
Sec. VIII.B. In addition, the long duration of such a
computation could be problematic, given the potentially
large number of measurements required by the VQE.

It is unclear whether we would be able to surpass
classical methods for any chemistry problems with this
number of gates.
The Fermi-Hubbard model is one
of the leading candidates for such a simulation.
As
described in Sec. V.B.1, the Hamiltonian variational
ansatz is particularly eﬃcient for this problem.
We
can prepare initial states of the Fermi-Hubbard model
using O(M 1.5) gates, and perform Trotter steps of
the Hamiltonian using O(M) gates for each Trotter
step (Jiang et al., 2018b).
Previous work has shown
that the Hamiltonian variational ansatz performs well
for the Fermi-Hubbard model, although it is not yet
known how many Trotter steps may be required for
accurate results.
Wecker et al. (2015a) achieved good
convergence for a 12 site problem with 20 Trotter steps.
Further work has shown promising results for both
the ground state problem (Reiner et al., 2018a), and
dynamics simulation (Reiner et al., 2018b), both in
the presence of realistic noise rates. These results were
obtained using less eﬃciently scaling circuits than those
described above.
Nevertheless, even if the number of
Trotter steps required to ﬁnd the ground state scaled
only linearly with the number of spin-orbitals, the total
algorithm scaling would be O(M 2), which is around
40,000 two-qubit gates for a 10 × 10 site Fermi-Hubbard
model (which requires 200 qubits). This rough estimate

An alternative approach to doggedly pursuing classi-
cally intractable problems is to use chemistry calculations
whose results we do know as a benchmark of our tech-
nology. This eﬀort has arguably already begun, follow-
ing the publication of many VQE experiments on small
molecules like H2 and LiH, in a range of diﬀerent hard-
ware systems. This proposal has recently been formalised

## Page 51

by McCaskey et al. (2019) and Nam et al. (2019). We
cannot expect to surpass classical methods without ﬁrst
reproducing classically known results. In a similar vein,
once we are able to experimentally demonstrate error cor-
rected logical qubits, the next step will be to perform
small, error corrected demonstrations of the algorithms
described throughout this review.
This approach was
recommended by Love (2012), who charted the evolution
of classical computational chemistry milestones since the
1930’s, and selected target problems to emulate. Equiv-
alent targets would be small Fermi-Hubbard models, or
the G1 set of molecules (Pople et al., 1989). This is a
small set of molecules whose energy is known extremely
accurately. For many of the molecules in the G1 set, an
FCI calculation on a suﬃciently accurate basis set would
be classically intractable (although they are typically not
necessary due to highly accurate approximate methods
and experimental results). As a result, this may be an
excellent test case for future quantum computers.

D. Summary and outlook

This review has sought to be accessible to both scien-
tists working on quantum computing, and those work-
ing on computational chemistry. We have discussed the
key methods used in classical computational chemistry,
and how these have been incorporated into quantum al-
gorithms. Emphasis has been placed on the key diﬀer-
ences between quantum and classical methods of chem-
istry simulation, and the resulting beneﬁts that quan-
tum computing is widely predicted to bring to the ﬁeld
of computational chemistry.
However, we have also shown that quantum methods
still face many challenges, not least the high error rates
and low qubit counts of existing hardware. Ultimately,
the success of quantum computational chemistry will
depend on our ability to construct larger and better
controlled quantum computers.
The question of how
large, and how well controlled these machines must be
will be determined by the quality of the procedures that
we have developed to carry out calculations of interest.
It is therefore crucial that we continue to develop and
optimise new:
algorithms, mappings, error correction
codes and procedures, basis sets, and error mitigation
techniques.
Below, we highlight potential research
directions to aid in this goal.

In the realm of variational algorithms, a wide range
of ans¨atze, chemistry mappings, classical optimisation
routines, and error mitigation techniques have been pro-
posed in recent years. However, the vast majority of these
proposals: were tested on small system sizes, performed a
limited number of comparisons to other techniques, and
were not optimised for maximum eﬃcacy. We suggest
that future work should begin to collate the existing pro-

posals, and determine which look most promising. This
review is a ﬁrst step in this direction, as is the growing
availability of quantum computational chemistry pack-
ages, and software libraries to emulate quantum comput-
ers.
Fast numerical simulations may enable us to test
variational algorithms on systems with up to around 30
to 40 qubits. This may begin to show which methods
are most suitable for near-term hardware.
These cal-
culations should be performed both with, and without
noise, in order to ascertain the all-round performance of
the various techniques. As quantum hardware develops,
this eﬀort can be migrated onto real systems, in order to
test whether our algorithms are as eﬀective as we expect
them to be. We expect that this more focused research
program will lead to new developments, as well as the
optimisation of existing methods.
It is more diﬃcult to construct a road-map for
phase estimation based approaches to solving chemistry
problems, given the higher degree of sophistication of
these methods, and the fact that there is less variation
between the diﬀerent approaches.
It is also diﬃcult
to anticipate breakthroughs that can lead to a large
reduction in required resources, such as the introduction
of the qubitization technique or tightening of Trotter
error bounds. One potential route to new developments
is to investigate areas that appear to be less well ex-
plored. One example may be error correction procedures
that are tailored speciﬁcally for chemistry problems.
Alternatively, one could import ideas that are well
established in classical computational chemistry. This is
how transformative ideas like the plane wave basis sets
and low rank Hamiltonian decomposition entered the
ﬁeld.

Successful exploration of these future directions may
only prove possible through close collaboration between
chemists and quantum information scientists. We hope
that this review helps to develop a common language for
these two groups, facilitating this important collabora-
tion.

ACKNOWLEDGMENTS

This work was supported by BP plc and by the EPSRC
National Quantum Technology Hub in Networked Quan-
tum Information Technology (EP/M013243/1). A.A.G.
acknowledges Anders G Froseth for his generous support,
as well as the Vannevar Bush Faculty Fellowship program
of the US Department of Defense. We thank R. Babbush
for insightful comments. S.M. and X.Y. thank L. Lindoy
for initial discussions on basis sets. SE is supported by
Japan Student Services Organization (JASSO) Student
Exchange Support Program (Graduate Scholarship for
Degree Seeking Students).

## Page 52

REFERENCES

Babej,
T.,
C.
Ing,
and
M.
Fingerhuth
(2018),
arXiv:1811.00713.
Ball, R. C. (2005), Phys. Rev. Lett. 95, 176407.
Ballance, C. J., T. P. Harty, N. M. Linke, M. A. Sepiol, and
D. M. Lucas (2016), Phys. Rev. Lett. 117, 060504.
Banchi, L., M. Fingerhuth, T. Babej, C. Ing,
and J. M.
Arrazola (2019), arXiv:1902.00462.
Barends, R., J. Kelly, A. Megrant, A. Veitia, D. Sank, E. Jef-
frey, T. C. White, J. Mutus, A. G. Fowler, B. Campbell,
et al. (2014), Nature 508 (7497), 500.
Barkoutsos, P. K., J. F. Gonthier, I. Sokolov, N. Moll,
G. Salis, A. Fuhrer, M. Ganzhorn, D. J. Egger, M. Troyer,
A. Mezzacapo, S. Filipp,
and I. Tavernelli (2018), Phys.
Rev. A 98, 022322.
Bartlett, R. J., S. A. Kucharski, and J. Noga (1989), Chem-
ical Physics Letters 155 (1), 133 .
Bartlett, R. J., and M. Musia l (2007), Rev. Mod. Phys. 79,
291.
Bauer, B., D. Wecker, A. J. Millis, M. B. Hastings,
and
M. Troyer (2016), Phys. Rev. X 6, 031045.
Bernstein, E., and U. Vazirani (1997), SIAM Journal on com-
puting 26 (5), 1411.
Berry, D. W., G. Ahokas, R. Cleve, and B. C. Sanders (2007),

Abrams, D. S.,
and S. Lloyd (1997), Phys. Rev. Lett. 79,
2586.
Abrams, D. S.,
and S. Lloyd (1999), Phys. Rev. Lett. 83,
5162.
Aharonov, D., and M. Ben-Or (1997), in Proceedings of the
twenty-ninth annual ACM symposium on Theory of com-
puting (ACM) pp. 176–188.
Aharonov, D., W. Van Dam, J. Kempe, Z. Landau, S. Lloyd,
and O. Regev (2008), SIAM review 50 (4), 755.
Albash, T.,
and D. A. Lidar (2018), Rev. Mod. Phys. 90,
015002.
Anderson, P. W. (2002), Physica Scripta T102 (1), 10.
Arg¨uello-Luengo, J., A. Gonz´alez-Tudela, T. Shi, P. Zoller,
and J. I. Cirac (2018), arXiv:1807.09228.
Arute, F., K. Arya, R. Babbush, D. Bacon, J. C. Bardin,
R. Barends, R. Biswas, S. Boixo, F. G. S. L. Brandao,
D. A. Buell, B. Burkett, Y. Chen, Z. Chen, B. Chiaro,
R. Collins, W. Courtney, A. Dunsworth, E. Farhi, B. Foxen,
A. Fowler, C. Gidney, M. Giustina, R. Graﬀ, K. Guerin,
S. Habegger, M. P. Harrigan, M. J. Hartmann, A. Ho,
M. Hoﬀmann, T. Huang, T. S. Humble, S. V. Isakov, E. Jef-
frey, Z. Jiang, D. Kafri, K. Kechedzhi, J. Kelly, P. V.
Klimov, S. Knysh, A. Korotkov, F. Kostritsa, D. Land-
huis, M. Lindmark, E. Lucero, D. Lyakh, S. Mandr`a, J. R.
McClean, M. McEwen, A. Megrant, X. Mi, K. Michielsen,
M. Mohseni, J. Mutus, O. Naaman, M. Neeley, C. Neill,
M. Y. Niu, E. Ostby, A. Petukhov, J. C. Platt, C. Quin-
tana, E. G. Rieﬀel, P. Roushan, N. C. Rubin, D. Sank, K. J.
Satzinger, V. Smelyanskiy, K. J. Sung, M. D. Trevithick,
A. Vainsencher, B. Villalonga, T. White, Z. J. Yao, P. Yeh,
A. Zalcman, H. Neven, and J. M. Martinis (2019), Nature
574 (7779), 505.
Aspuru-Guzik, A., A. D. Dutoi, P. J. Love,
and M. Head-
Gordon (2005), Science 309 (5741), 1704.
Aspuru-Guzik, A., R. Lindh,
and M. Reiher (2018), ACS
Central Science 4 (2), 144.
Aspuru-Guzik, A.,
and P. Walther (2012), Nature Physics
8 (4), 285.
Austin,
B.
M.,
D.
Y.
Zubarev,
and
W.
A.
Lester
(2012), Chemical Reviews 112 (1), 263, pMID: 22196085,
https://doi.org/10.1021/cr2001564.
Babbush, R., D. W. Berry, I. D. Kivlichan, A. Y. Wei, P. J.
Love, and A. Aspuru-Guzik (2016), New Journal of Physics
18 (3), 033032.
Babbush, R., D. W. Berry, J. R. McClean,
and H. Neven
(2018a), arXiv:1807.09802.
Babbush, R., D. W. Berry, Y. R. Sanders, I. D. Kivlichan,
A. Scherer, A. Y. Wei, P. J. Love,
and A. Aspuru-Guzik
(2017), Quantum Science and Technology 3 (1), 015006.
Babbush, R., C. Gidney, D. W. Berry, N. Wiebe, J. McClean,
A. Paler, A. Fowler, and H. Neven (2018b), Phys. Rev. X
8, 041015.
Babbush, R., P. J. Love, and A. Aspuru-Guzik (2014), Sci-
entiﬁc reports 4, 6603.
Babbush, R., J. McClean, D. Wecker, A. Aspuru-Guzik, and
N. Wiebe (2015), Phys. Rev. A 91, 022311.
Babbush,
R.,
A.
Perdomo-Ortiz,
B.
O’Gorman,
W.
Macready,
and
A.
Aspuru-Guzik
(2012),
10.1002/9781118755815.ch05, arXiv:1211.3422.
Babbush, R., N. Wiebe, J. McClean, J. McClain, H. Neven,
and G. K.-L. Chan (2018c), Phys. Rev. X 8, 011044.

Communications in Mathematical Physics 270 (2), 359.
Berry, D. W., and A. M. Childs (2012), Quantum Info. Com-
put. 12 (1-2), 29.
Berry, D. W., A. M. Childs, R. Cleve, R. Kothari,
and
R. D. Somma (2014), in Proceedings of the Forty-sixth An-
nual ACM Symposium on Theory of Computing, STOC ’14
(ACM, New York, NY, USA) pp. 283–292.
Berry, D. W., A. M. Childs, R. Cleve, R. Kothari, and R. D.
Somma (2015a), Phys. Rev. Lett. 114, 090502.
Berry, D. W., A. M. Childs, and R. Kothari (2015b), in Foun-
dations of Computer Science (FOCS), 2015 IEEE 56th An-
nual Symposium on (IEEE) pp. 792–809.
Berry, D. W., A. M. Childs, and R. Kothari (2015c), in 2015
IEEE 56th Annual Symposium on Foundations of Com-
puter Science, pp. 792–809.
Berry, D. W., A. M. Childs, Y. Su, X. Wang, and N. Wiebe
(2019a), arXiv:1906.07115.
Berry, D. W., C. Gidney, M. Motta, J. R. McClean,
and
R. Babbush (2019b), arXiv:1902.02134.
Berry, D. W., B. L. Higgins, S. D. Bartlett, M. W. Mitchell,
G. J. Pryde, and H. M. Wiseman (2009), Phys. Rev. A 80,
052114.
Berry, D. W., M. Kieferov´a, A. Scherer, Y. R. Sanders, G. H.
Low, N. Wiebe, C. Gidney,
and R. Babbush (2018), npj
Quantum Information 4 (1), 22.
Blatt, R., and C. F. Roos (2012), Nature Physics 8 (4), 277.
Boixo, S., S. V. Isakov, V. N. Smelyanskiy, R. Babbush,
N. Ding, Z. Jiang, M. J. Bremner, J. M. Martinis,
and
H. Neven (2018), Nature Physics 14 (6), 595.
Bonet-Monroig, X., R. Babbush, and T. E. O’Brien (2019),

arXiv:1908.05628.
Bonet-Monroig, X., R. Sagastizabal, M. Singh,
and T. E.
O’Brien (2018), arXiv:1807.10050.
Booth,
G.
H.,
and
A.
Alavi
(2010),
The
Jour-
nal
of
Chemical
Physics
132
(17),
174104,
https://doi.org/10.1063/1.3407895.
Borregaard, J., M. Christandl,
and D. S. Frana (2019),
arXiv:1909.04786.
Braunstein, S. L., and P. van Loock (2005), Rev. Mod. Phys.
77, 513.
Bravyi, S., J. M. Gambetta, A. Mezzacapo, and K. Temme

## Page 53

(2017), arXiv preprint arXiv:1701.08213.
Bravyi, S., and A. Kitaev (2005), Phys. Rev. A 71, 022316.
Bravyi, S. B.,
and A. Y. Kitaev (2002), Annals of Physics
298 (1), 210 .
Brown, K. L., W. J. Munro, and V. M. Kendon (2010), En-
tropy 12 (11), 2268.
Burgess,
B.
K.,
and
D.
J.
Lowe
(1996),
Chem-
ical
Reviews
96
(7),
2983,
pMID:
11848849,
https://doi.org/10.1021/cr950055x.
Cai, Z. (2019), arXiv:1910.02719.
Campbell, E. (2018), arXiv preprint arXiv:1811.08017.
Campbell, E. T., B. M. Terhal, and C. Vuillot (2017), Nature
549 (7671), 172.
Cao, Y., J. R. Fontalvo, and A. Aspuru-Guzik (2018), IBM
Journal of Research and Development , 1.
Cao, Y., J. Romero, J. P. Olson, M. Degroote, P. D. John-
son, M. Kieferov, I. D. Kivlichan, T. Menke, B. Per-
opadre, N. P. D. Sawaya, S. Sim, L. Veis, and A. Aspuru-
Guzik (2019), Chemical Reviews 119 (19), 10856, pMID:
31469277, https://doi.org/10.1021/acs.chemrev.8b00803.
Chen, L.-K., Z.-D. Li, X.-C. Yao, M. Huang, W. Li, H. Lu,
X. Yuan, Y.-B. Zhang, X. Jiang, C.-Z. Peng, L. Li, N.-L.
Liu, X. Ma, C.-Y. Lu, Y.-A. Chen, and J.-W. Pan (2017),
Optica 4 (1), 77.
Chen, M.-C., M. Gong, X.-S. Xu, X. Yuan, J.-W. Wang,
C. Wang, C. Ying, J. Lin, Y. Xu, Y. Wu, et al. (2019),
arXiv preprint arXiv:1905.03150.
Chien, R. W., S. Xue, T. S. Hardikar, K. Setia,
and J. D.
Whitﬁeld (2019), Phys. Rev. A 100, 032337.
Childs, A. M., and R. Kothari (2011), in Theory of Quantum
Computation, Communication, and Cryptography, edited
by W. van Dam, V. M. Kendon, and S. Severini (Springer
Berlin Heidelberg, Berlin, Heidelberg) pp. 94–103.
Childs, A. M., D. Maslov, Y. Nam, N. J. Ross,
and Y. Su
(2017), arXiv preprint arXiv:1711.10980.
Childs, A. M., A. Ostrander, and Y. Su (2018), arXiv preprint
arXiv:1805.08385.
Childs, A. M., and Y. Su (2019), arXiv:1901.00564.
Childs, A. M., and N. Wiebe (2012), Quantum Info. Comput.
12 (11-12), 901.
Chin,
S.,
and
J.
Huh
(2018),
arXiv
preprint
arXiv:1803.10002.
Chow, J. M., J. M. Gambetta, A. D. C´orcoles, S. T. Merkel,
J. A. Smolin, C. Rigetti, S. Poletto, G. A. Keefe, M. B.
Rothwell, J. R. Rozen, M. B. Ketchen,
and M. Steﬀen
(2012), Phys. Rev. Lett. 109, 060501.
Christiansen,
O.
(2012),
Physical
Chemistry
Chemical
Physics 14 (19), 6672.
Cirac, J. I., and P. Zoller (1995), Phys. Rev. Lett. 74, 4091.
Clements, W. R., J. J. Renema, A. Eckstein, A. A. Valido,
A. Lita, T. Gerrits, S. W. Nam, W. S. Kolthammer,
J. Huh,
and I. A. Walmsley (2017), arXiv preprint
arXiv:1710.08655.
Colless, J. I., V. V. Ramasesh, D. Dahlen, M. S. Blok, M. E.
Kimchi-Schwartz, J. R. McClean, J. Carter, W. A. de Jong,
and I. Siddiqi (2018), Phys. Rev. X 8, 011021.
Coppersmith, D. (1994), IBM Research Report RC 19642.
Cotler, J., and F. Wilczek (2019), arXiv:1908.02754.
Crawford, O., B. van Straaten, D. Wang, T. Parks, E. Camp-
bell, and S. Brierley (2019), arXiv:1908.06942.
Cubitt, T., and A. Montanaro (2016), SIAM Journal on Com-
puting 45 (2), 268, https://doi.org/10.1137/140998287.
Dagotto, E. (1994), Rev. Mod. Phys. 66, 763.
Dallaire-Demers, P.-L., J. Romero, L. Veis, S. Sim,
and

A. Aspuru-Guzik (2018), arXiv preprint arXiv:1801.01053.
Dallaire-Demers, P.-L.,
and F. K. Wilhelm (2016a), Phys.
Rev. A 93, 032303.
Dallaire-Demers, P.-L.,
and F. K. Wilhelm (2016b), Phys.
Rev. A 94, 062304.
Daskin, A., A. Grama, and S. Kais (2014), Quantum Infor-
mation Processing 13 (2), 333.
Dawson, C. M.,
and M. A. Nielsen (2005),
arXiv:quant-
ph/0505030.
Devitt, S. J., W. J. Munro, and K. Nemoto (2013), Reports
on Progress in Physics 76 (7), 076001.
Dirac, P. (1929), Proceedings of the Royal Society of London
123, 10.1098/rspa.1929.0094.
Ditchﬁeld, R., W. J. Hehre,
and J. A. Pople (1971), The
Journal of Chemical Physics 54 (2), 724.
DiVincenzo, D. P. (1995), Phys. Rev. A 51, 1015.
Du, J., N. Xu, X. Peng, P. Wang, S. Wu, and D. Lu (2010),

Phys. Rev. Lett. 104, 030502.
Dunning Jr., T. H. (1989), The Journal of Chemical Physics
90 (2), 1007.
D¨ur, W., M. J. Bremner,
and H. J. Briegel (2008), Phys.
Rev. A 78, 052325.
Endo, S., S. C. Benjamin, and Y. Li (2017), arXiv preprint
arXiv:1712.09271.
Endo, S., T. Jones, S. McArdle, X. Yuan, and S. Benjamin
(2018a), arXiv preprint arXiv:1806.05707.
Endo, S., Y. Li, S. Benjamin,
and X. Yuan (2018b), arXiv
preprint arXiv:1812.08778.
Endo, S., Q. Zhao, Y. Li, S. Benjamin, and X. Yuan (2018c),
arXiv preprint arXiv:1808.03623.
Evans, M. G.,
and M. Polanyi (1935), Trans. Faraday Soc.
31, 875.
Eyring, H. (1935), The Journal of Chemical Physics 3 (2),
107, https://doi.org/10.1063/1.1749604.
Farhi, E., J. Goldstone,
and S. Gutmann (2014), arXiv
preprint arXiv:1411.4028.
Farhi, E., J. Goldstone, S. Gutmann, and M. Sipser (2000),
arXiv:quant-ph/0001106.
Farrelly, T. C.,
and A. J. Short (2014), Phys. Rev. A 89,
012302.
Feynman, R. P. (1982), International Journal of Theoretical
Physics 21 (6), 467.
Fingerhuth, M., T. Babej,
and C. Ing (2018), “A quantum
alternating operator ansatz with hard and soft constraints
for lattice protein folding,” arXiv:1810.13411.
Fowler, A. G., and C. Gidney (2018), arXiv:1808.06709.
Fowler, A. G., M. Mariantoni, J. M. Martinis,
and A. N.
Cleland (2012a), Physical Review A 86 (3), 032324.
Fowler, A. G., A. C. Whiteside,
and L. C. L. Hollenberg
(2012b), Phys. Rev. Lett. 108, 180501.
Fradkin, E., S. A. Kivelson,
and J. M. Tranquada (2015),
Rev. Mod. Phys. 87, 457.
Frisch, M. J., G. W. Trucks, H. B. Schlegel, G. E. Scuseria,
M. A. Robb, J. R. Cheeseman, G. Scalmani, V. Barone,
G. A. Petersson, H. Nakatsuji, X. Li, M. Caricato, A. V.
Marenich, J. Bloino, B. G. Janesko, R. Gomperts, B. Men-
nucci, H. P. Hratchian, J. V. Ortiz, A. F. Izmaylov, J. L.
Sonnenberg, D. Williams-Young, F. Ding, F. Lipparini,
F. Egidi, J. Goings, B. Peng, A. Petrone, T. Hender-
son, D. Ranasinghe, V. G. Zakrzewski, J. Gao, N. Rega,
G. Zheng,
W. Liang,
M. Hada,
M. Ehara, K. Toy-
ota, R. Fukuda, J. Hasegawa, M. Ishida, T. Nakajima,
Y. Honda, O. Kitao, H. Nakai, T. Vreven, K. Throssell,
J. A. Montgomery, Jr., J. E. Peralta, F. Ogliaro, M. J.

## Page 54

Bearpark, J. J. Heyd, E. N. Brothers, K. N. Kudin,
V. N. Staroverov, T. A. Keith, R. Kobayashi, J. Normand,
K. Raghavachari, A. P. Rendell, J. C. Burant, S. S. Iyengar,
J. Tomasi, M. Cossi, J. M. Millam, M. Klene, C. Adamo,
R. Cammi, J. W. Ochterski, R. L. Martin, K. Morokuma,
O. Farkas, J. B. Foresman, and D. J. Fox (2016), “Gaus-
sian16 Revision B.01,” Gaussian Inc. Wallingford CT.
Gaebler, J. P., T. R. Tan, Y. Lin, Y. Wan, R. Bowler, A. C.
Keith, S. Glancy, K. Coakley, E. Knill, D. Leibfried, et al.
(2016), Physical review letters 117 (6), 060505.
Gambetta, J. M., J. M. Chow,
and M. Steﬀen (2017), npj
Quantum Information 3 (1), 2.
Ganzhorn, M., D. J. Egger, P. K. Barkoutsos, P. Ollitrault,
G. Salis, N. Moll, A. Fuhrer, P. Mueller, S. Woerner, I. Tav-
ernelli, and S. Filipp (2018), arXiv:1809.05057.
Garcia-Saez, A., and J. I. Latorre (2018), arXiv:1806.02287.
Ge, Y., J. Tura, and J. I. Cirac (2017), arXiv:1712.03193.
Genin, S. N., I. G. Ryabinkin,
and A. F. Izmaylov (2019),
arXiv:1901.04715.
Georgescu, I. M., S. Ashhab, and F. Nori (2014), Rev. Mod.
Phys. 86, 153.
Gidney, C., and M. Eker (2019), arXiv:1905.09749.
Gidney, C., and A. G. Fowler (2019), Quantum 3, 135.
Gokhale, P., O. Angiuli, Y. Ding, K. Gui, T. Tomesh,
M. Suchara, M. Martonosi,
and F. T. Chong (2019),
arXiv:1907.13623.
Gokhale, P., and F. T. Chong (2019), arXiv:1908.11857.
Gottesman, D. (1998), Physical Review A 57 (1), 127.
Grant, E., L. Wossnig, M. Ostaszewski,
and M. Benedetti
(2019), arXiv:1903.05076.
Grimsley, H. R., D. Claudino, S. E. Economou, E. Barnes,
and N. J. Mayhall (2019), arXiv:1910.10329.
Grimsley, H. R., S. E. Economou, E. Barnes, and N. J. May-
hall (2018), arXiv:1812.11173.
Guerreschi,
G.
G.,
and
M.
Smelyanskiy
(2017),
arXiv:1701.01450.
Gulania, S., and J. D. Whitﬁeld (2019), arXiv:1904.10469.
Haah, J., M. B. Hastings, R. Kothari, and G. H. Low (2018),
arXiv preprint arXiv:1801.03922.
Hanson, R., L. P. Kouwenhoven, J. R. Petta, S. Tarucha, and
L. M. K. Vandersypen (2007), Rev. Mod. Phys. 79, 1217.
Harrow, A., and J. Napp (2019), arXiv:1901.05374.
Harrow,
A.
W.,
and
A.
Montanaro
(2017),
Nature
549 (7671), 203.
Harty, T., D. Allcock, C. J. Ballance, L. Guidoni, H. Janacek,
N. Linke, D. Stacey, and D. Lucas (2014), Physical review
letters 113 (22), 220501.
Hastings, M. B., D. Wecker, B. Bauer, and M. Troyer (2015),
QIC 15.
Hatcher,
R.,
J.
A.
Kittl,
and
C.
Bowen
(2019),
arXiv:1903.05550.
Hattig,
C.,
W.
Klopper,
A.
Khn,
and
D.
P.
Tew
(2012), Chemical Reviews 112 (1), 4, pMID: 22206503,
https://doi.org/10.1021/cr200168z.
Havlicek, V., M. Troyer,
and J. D. Whitﬁeld (2017), Phys.
Rev. A 95, 032332.
Hehre,
W.
J.,
R.
F.
Stewart,
and
J.
A.
Pople
(1969), The Journal of Chemical Physics 51 (6), 2657,
https://doi.org/10.1063/1.1672392.
Helgaker, T., S. Coriani, P. Jrgensen, K. Kristensen, J. Olsen,
and K. Ruud (2012), Chemical Reviews 112 (1), 543,
pMID: 22236047, https://doi.org/10.1021/cr2002239.
Helgaker, T., P. Jorgensen,
and J. Olsen (2014), Molecular
electronic-structure theory (John Wiley & Sons).

Hempel, C., C. Maier, J. Romero, J. McClean, T. Monz,
H. Shen, P. Jurcevic, B. P. Lanyon, P. Love, R. Babbush,
A. Aspuru-Guzik, R. Blatt, and C. F. Roos (2018), Phys.
Rev. X 8, 031022.
Heya, K., K. M. Nakanishi, K. Mitarai, and K. Fujii (2019),
arXiv e-prints , arXiv:1904.08566arXiv:1904.08566 [quant-
ph].
Heyl, M., P. Hauke, and P. Zoller (2019), Science advances
5 (4), eaau8342.
Higgins, B. L., D. W. Berry, S. D. Bartlett, H. M. Wiseman,
and G. J. Pryde (2007), Nature 450, 393 EP .
Higgott, O., D. Wang, and S. Brierley (2018), arXiv preprint
arXiv:1805.08138.
Hobza, P.,
and J. Sponer (2002), Journal of the Ameri-
can Chemical Society 124 (39), 11802, pMID: 12296748,
https://doi.org/10.1021/ja026759n.
Hoﬀman, B. M., D. Lukoyanov, Z.-Y. Yang, D. R. Dean, and
L. C. Seefeldt (2014), Chemical Reviews 114 (8), 4041,
pMID: 24467365, https://doi.org/10.1021/cr400641x.
Hoﬀmann,
M.
R.,
and
J.
Simons
(1988),
The
Journal
of
Chemical
Physics
88
(2),
993,
https://doi.org/10.1063/1.454125.
Houck, A. A., H. E. T¨ureci,
and J. Koch (2012), Nature
Physics 8 (4), 292.
Hu, L., Y.-C. Ma, Y. Xu, W.-T. Wang, Y.-W. Ma, K. Liu, H.-
Y. Wang, Y.-P. Song, M.-H. Yung, and L.-Y. Sun (2018a),
Sci. Bull. 63 (5), 293.
Hu, L., Y.-C. Ma, Y. Xu, W.-T. Wang, Y.-W. Ma, K. Liu, H.-
Y. Wang, Y.-P. Song, M.-H. Yung, and L.-Y. Sun (2018b),
Science Bulletin 63 (5), 293 .
Hubbard,
J.
(1963),
Proceedings
of
the
Royal
Society
of
London.
Series
A.
Mathemati-
cal
and
Physical
Sciences
276
(1365),
238,
https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.1963.0204.
Huggins, W. J., J. Lee, U. Baek, B. O’Gorman,
and K. B.
Whaley (2019a), arXiv:1909.09114.
Huggins, W. J., J. McClean, N. Rubin, Z. Jiang, N. Wiebe,
K. B. Whaley, and R. Babbush (2019b), arXiv:1907.13117.
Huh, J., G. G. Guerreschi, B. Peropadre, J. R. McClean, and
A. Aspuru-Guzik (2015), Nature Photonics 9 (9), 615.
Huh, J.,
and M.-H. Yung (2017), Scientiﬁc reports 7 (1),
7462.
Huo, M., and Y. Li (2018), arXiv:1811.02734.
IBM, (2018), “Ibm qiskit,” https://qiskit.org/.
Izmaylov, A. F., T.-C. Yen, and I. G. Ryabinkin (2018), arXiv
preprint arXiv:1810.11602.
Jameson,
A.
(1999),
Journal
of
Aircraft
36
(1),
36,
https://doi.org/10.2514/2.2412.
Jena, A., S. Genin, and M. Mosca (2019), arXiv:1907.07859.
Jiang, Z., A. Kalev, W. Mruczkiewicz, and H. Neven (2019),

arXiv:1910.10746.
Jiang, Z., J. McClean, R. Babbush, and H. Neven (2018a),

arXiv:1812.08190.
Jiang, Z., K. J. Sung, K. Kechedzhi, V. N. Smelyanskiy, and
S. Boixo (2018b), Phys. Rev. Applied 9, 044036.
Johnson, P. D., J. Romero, J. Olson, Y. Cao, and A. Aspuru-
Guzik (2017), arXiv preprint arXiv:1711.02249.
Jones, N. C., J. D. Whitﬁeld, P. L. McMahon, M.-H. Yung,
R. Van Meter, A. Aspuru-Guzik, and Y. Yamamoto (2012),
New Journal of Physics 14 (11), 115023.
Jordan, P.,
and E. Wigner (1928), Zeitschrift f¨ur Physik
47 (9), 631.
Joshi, S., A. Shukla, H. Katiyar, A. Hazra, and T. S. Mahesh
(2014), Phys. Rev. A 90, 022303.

## Page 55

Jozsa, R. (2005), arXiv:quant-ph/0508124.
Kais, S., S. A. Rice,
and A. R. Dinner (2014), Quantum
information and computation for chemistry (John Wiley &
Sons).
Kandala, A., A. Mezzacapo, K. Temme, M. Takita, M. Brink,
J. M. Chow,
and J. M. Gambetta (2017), Nature
549 (7671), 242.
Kandala, A., K. Temme, A. D. Corcoles, A. Mezzacapo, J. M.
Chow, and J. M. Gambetta (2018), arXiv:1805.04492.
Kane, B. E. (1998), Nature 393 (6681), 133.
Kassal, I., S. P. Jordan, P. J. Love, M. Mohseni,
and
A. Aspuru-Guzik (2008), Proceedings of the National
Academy of Sciences 105 (48), 18681.
Kassal, I., J. D. Whitﬁeld, A. Perdomo-Ortiz, M.-H. Yung,
and A. Aspuru-Guzik (2011), Annual review of physical
chemistry 62, 185.
Keen, T., T. Maier, S. Johnston,
and P. Lougovski (2019),
arXiv:1910.09512.
Kempe,
J.,
A.
Kitaev,
and
O.
Regev
(2006),
SIAM
Journal
on
Computing
35
(5),
1070,
https://doi.org/10.1137/S0097539704445226.
Kieferova, M., A. Scherer,
and D. Berry (2018), arXiv
preprint arXiv:1805.00582.
Kim, I. H. (2017), arXiv:1703.00032.
Kim, I. H., and B. Swingle (2017), arXiv:1711.07500.
Kitaev,
A.
Y.
(1995),
Preprint
at
http://arxiv.
org/abs/quant-ph/9511026.
Kitaev, A. Y. (1997), Russian Mathematical Surveys 52 (6),
1191.
Kivlichan,
I. D.,
C. Gidney,
D. W. Berry,
N. Wiebe,
J. McClean, W. Sun, Z. Jiang, N. Rubin, A. Fowler,
A. Aspuru-Guzik, R. Babbush,
and H. Neven (2019a),
arXiv:1902.10673.
Kivlichan, I. D., C. E. Granade,
and N. Wiebe (2019b),
arXiv:1907.10070.
Kivlichan,
I.
D.,
J.
McClean,
N.
Wiebe,
C.
Gidney,
A. Aspuru-Guzik, G. K.-L. Chan, and R. Babbush (2018),
Phys. Rev. Lett. 120, 110501.
Kivlichan, I. D., N. Wiebe, R. Babbush,
and A. Aspuru-
Guzik (2017), Journal of Physics A: Mathematical and The-
oretical 50 (30).
Knecht, S., E. D. Hedegaard, S. Keller, A. Kovyrshin, Y. Ma,
A. Muolo, C. J. Stein,
and M. Reiher (2016), CHIMIA
International Journal for Chemistry 70 (4).
Knill, E., R. Laﬂamme,
and G. J. Milburn (2001), Nature
409 (6816), 46.
Knill, E., R. Laﬂamme, and W. Zurek (1996), .
Knill, E., G. Ortiz, and R. D. Somma (2007), Phys. Rev. A
75, 012328.
Kokail, C., C. Maier, R. van Bijnen, T. Brydges, M. K. Joshi,
P. Jurcevic, C. A. Muschik, P. Silvi, R. Blatt, C. F. Roos,
and P. Zoller (2019), Nature 569 (7756), 355.
Kolda, T. G., R. M. Lewis,
and V. Torczon (2006), SIAM
Rev. 45, 385482.
Kreula, J., S. R. Clark, and D. Jaksch (2016), Scientiﬁc re-
ports 6, 32940.
Kurashige, Y., G. K.-L. Chan, and T. Yanai (2013), Nature
chemistry 5 (8), 660.
Ladd, T. D., F. Jelezko, R. Laﬂamme, Y. Nakamura, C. Mon-
roe, and J. L. O’Brien (2010), Nature 464, 45 EP , review
Article.
Landauer, R. (1995), Philosophical Transactions of the Royal
Society of London A: Mathematical, Physical and Engi-
neering Sciences 353 (1703), 367.

Lanyon, B. P., J. D. Whitﬁeld, G. G. Gillett, M. E. Goggin,
M. P. Almeida, I. Kassal, J. D. Biamonte, M. Mohseni,
B. J. Powell, M. Barbieri, et al. (2010), Nature chemistry
2 (2), 106.
LeBlanc, J. P. F., A. E. Antipov, F. Becca, I. W. Bulik, G. K.-
L. Chan, C.-M. Chung, Y. Deng, M. Ferrero, T. M. Hen-
derson, C. A. Jim´enez-Hoyos, E. Kozik, X.-W. Liu, A. J.
Millis, N. V. Prokof’ev, M. Qin, G. E. Scuseria, H. Shi,
B. V. Svistunov, L. F. Tocchio, I. S. Tupitsyn, S. R. White,
S. Zhang, B.-X. Zheng, Z. Zhu, and E. Gull (Simons Col-
laboration on the Many-Electron Problem) (2015), Phys.
Rev. X 5, 041041.
Lee, J., W. J. Huggins, M. Head-Gordon,
and K. B. Wha-
ley (2019), Journal of Chemical Theory and Computation
15 (1), 311, https://doi.org/10.1021/acs.jctc.8b01004.
Lee, P. A., N. Nagaosa,
and X.-G. Wen (2006), Rev. Mod.
Phys. 78, 17.
Leibfried, D., R. Blatt, C. Monroe, and D. Wineland (2003),

Rev. Mod. Phys. 75, 281.
Li, Y., and S. C. Benjamin (2017), Phys. Rev. X 7, 021050.
Li, Z., J. Li, N. S. Dattani, C. J. Umrigar, and G. K.-L. Chan
(2018), arXiv:1809.10307.
Li, Z., M.-H. Yung, H. Chen, D. Lu, J. D. Whitﬁeld, X. Peng,
A. Aspuru-Guzik, and J. Du (2011), Scientiﬁc reports 1,
88.
Lidar, D. A., and T. A. Brun (2013), Quantum Error Cor-
rection (Cambridge University Press).
Lidar, D. A., and H. Wang (1999), Phys. Rev. E 59, 2429.
Lischka, H., D. Nachtigallov, A. J. A. Aquino, P. G. Sza-
lay, F. Plasser, F. B. C. Machado,
and M. Barbatti
(2018), Chemical Reviews 118 (15), 7293, pMID: 30040389,
https://doi.org/10.1021/acs.chemrev.8b00244.
Litinski, D. (2019a), Quantum 3, 128.
Litinski, D. (2019b), arXiv:1905.06903.
Lloyd, S. (1996), Science 273 (5278), 1073.
Lloyd, S., and S. L. Braunstein (1999), Phys. Rev. Lett. 82,
1784.
Loss, D.,
and D. P. DiVincenzo (1998), Phys. Rev. A 57,
120.
Love, P. J. (2012), arXiv:1208.5524.
Low, G. H. (2018), arXiv preprint arXiv:1807.03967.
Low, G. H., N. P. Bauman, C. E. Granade, B. Peng, N. Wiebe,
E. J. Bylaska, D. Wecker, S. Krishnamoorthy, M. Roet-
teler, K. Kowalski, M. Troyer,
and N. A. Baker (2019a),
arXiv:1904.01131.
Low, G. H.,
and I. L. Chuang (2016), arXiv preprint
arXiv:1610.06546.
Low, G. H., and I. L. Chuang (2017), Phys. Rev. Lett. 118,
010501.
Low,
G. H.,
V. Kliuchnikov,
and N. Wiebe (2019b),
arXiv:1907.11679.
Low, G. H., and N. Wiebe (2018), arXiv:1805.00675.
Low, G. H., T. J. Yoder, and I. L. Chuang (2016), Phys. Rev.
X 6, 041067.
Lu, D., B. Xu, N. Xu, Z. Li, H. Chen, X. Peng, R. Xu, and
J. Du (2012), Phys. Chem. Chem. Phys. 14, 9411.
Lu, L.-H., and Y.-Q. Li (2019), arXiv:1906.09184.
Lyakh, D. I., M. Musia, V. F. Lotrich,
and R. J. Bartlett
(2012), Chemical Reviews 112 (1), 182, pMID: 22220988,
https://doi.org/10.1021/cr2001417.
Macridin, A., P. Spentzouris, J. Amundson,
and R. Harnik
(2018a), Phys. Rev. A 98, 042312.
Macridin, A., P. Spentzouris, J. Amundson,
and R. Harnik
(2018b), Phys. Rev. Lett. 121, 110504.

## Page 56

Malik, M. R., and D. M. Bushnell (2012), NASA Technical
Report .
Matsuura, S., T. Yamazaki, V. Senicourt, L. Huntington, and
A. Zaribaﬁyan (2018), arXiv:1810.11511.
Matsuzawa, Y., and Y. Kurashige (2019), arXiv:1909.12410.
McArdle, S., S. Endo, Y. Li, S. Benjamin,
and X. Yuan
(2018a), arXiv preprint arXiv:1804.03023.
McArdle, S., A. Mayorov, X. Shan, S. Benjamin, and X. Yuan
(2018b), arXiv:1811.04069.
McArdle,
S.,
X.
Yuan,
and
S.
Benjamin
(2018c),
arXiv:1807.02467.
McCaskey, A. J., Z. P. Parks, J. Jakowski, S. V. Moore,
T. Morris, T. S. Humble,
and R. C. Pooser (2019),
arXiv:1905.01534.
McClean, J., S. Boixo, V. Smelyanskiy, R. Babbush,
and
H. Neven (2018), Nature Communications 9, 4812.
McClean,
J.
R.,
R.
Babbush,
P.
J.
Love,
and
A.
Aspuru-Guzik
(2014),
The
Journal
of
Physical
Chemistry
Letters
5
(24),
4368,
pMID:
26273989,
https://doi.org/10.1021/jz501649m.
McClean, J. R., F. M. Faulstich, Q. Zhu, B. O’Gorman,
Y. Qiu, S. R. White, R. Babbush,
and L. Lin (2019a),
arXiv:1909.00028.
McClean, J. R., Z. Jiang, N. C. Rubin, R. Babbush,
and
H. Neven (2019b), arXiv preprint arXiv:1903.05786.
McClean, J. R., M. E. Kimchi-Schwartz, J. Carter, and W. A.
de Jong (2017a), Phys. Rev. A 95, 042308.
McClean, J. R., I. D. Kivlichan, K. J. Sung, D. S. Steiger,
Y. Cao, C. Dai, E. S. Fried, C. Gidney, B. Gimby,
P. Gokhale, T. Hner, T. Hardikar, V. Havlek, C. Huang,
J. Izaac, Z. Jiang, X. Liu, M. Neeley, T. O’Brien, I. Ozﬁ-
dan, M. D. Radin, J. Romero, N. Rubin, N. P. D. Sawaya,
K. Setia, S. Sim, M. Steudtner, Q. Sun, W. Sun, F. Zhang,
and R. Babbush (2017b), arXiv:1710.07629.
McClean, J. R., J. Romero, R. Babbush,
and A. Aspuru-
Guzik (2016), New Journal of Physics 18 (2), 023023.
Mitarai, K., and K. Fujii (2018), arXiv:1901.00015.
Mitarai, K., Y. O. Nakagawa,
and W. Mizukami (2019),
arXiv:1905.04054.
Mizukami, W., K. Mitarai, Y. O. Nakagawa, T. Yamamoto,
T. Yan, and Y. ya Ohnish (2019), arXiv:1910.11526.
Monroe, C.,
and J. Kim (2013), Science 339 (6124), 1164,
https://science.sciencemag.org/content/339/6124/1164.full.pdf.
Monz, T., P. Schindler, J. T. Barreiro, M. Chwalla, D. Nigg,
W. A. Coish, M. Harlander, W. H¨ansel, M. Hennrich, and
R. Blatt (2011), Phys. Rev. Lett. 106, 130506.
Motta, M., C. Sun, A. T. K. Tan, M. J. O. Rourke, E. Ye,
A. J. Minnich, F. G. S. L. Brandao,
and G. K.-L. Chan
(2019), arXiv:1901.07653.
Motta, M., E. Ye, J. R. McClean, Z. Li, A. J. Minnich, R. Bab-
bush, and G. K.-L. Chan (2018), arXiv:1808.02625.
Mueck, L. (2015), Nature chemistry 7 (5), 361.
Muller,
R.
P.
(2004),
“Pyquante,”
http://pyquante.
sourceforge.net/, accessed: 24.7.2018.
Nakamura, Y., Y. A. Pashkin, and J. S. Tsai (1999), Nature
398 (6730), 786.
Nakanishi, K. M., K. Fujii,
and S. Todo (2019), arXiv
preprint arXiv:1903.12166.
Nakanishi, K. M., K. Mitarai,
and K. Fujii (2018), arXiv
preprint arXiv:1810.09434.
Nam, Y., J.-S. Chen, N. C. Pisenti, K. Wright, C. Delaney,
D. Maslov, K. R. Brown, S. Allen, J. M. Amini, J. Apis-
dorf, K. M. Beck, A. Blinov, V. Chaplin, M. Chmielewski,
C. Collins, S. Debnath, A. M. Ducore, K. M. Hudek,

M. Keesan, S. M. Kreikemeier, J. Mizrahi, P. Solomon,
M. Williams, J. D. Wong-Campos, C. Monroe, and J. Kim
(2019), arXiv:1902.10171.
Nielsen, M. A., and I. Chuang (2002), “Quantum computa-
tion and quantum information,”.
O’Brien, T. E., B. Senjean, R. Sagastizabal, X. Bonet-
Monroig, A. Dutkiewicz, F. Buda, L. DiCarlo, and L. Viss-
cher (2019), arXiv:1905.03742.
O’Brien, T. E., B. Tarasinski,
and B. M. Terhal (2018a),
arXiv:1809.09697.
O’Brien, T. E., P. Ro˙zek, and A. R. Akhmerov (2018b), Phys.
Rev. Lett. 120, 220504.
O’Gorman, B., W. J. Huggins, E. G. Rieﬀel, and K. B. Wha-
ley (2019), arXiv:1905.05118.
O’Gorman, J., and E. T. Campbell (2017), Phys. Rev. A 95,
032338.
Olivares-Amaya, R., W. Hu, N. Nakatani, S. Sharma, J. Yang,
and G. K.-L. Chan (2015), The Journal of Chemical Physics
142 (3), 034102, https://doi.org/10.1063/1.4905329.
Ollitrault, P. J., A. Kandala, C.-F. Chen, P. K. Barkoutsos,
A. Mezzacapo, M. Pistoia, S. Sheldon, S. Woerner, J. Gam-
betta, and I. Tavernelli (2019), arXiv:1910.12890.
O’Malley, P. J. J., R. Babbush, I. D. Kivlichan, J. Romero,
J. R. McClean, R. Barends, J. Kelly, P. Roushan, A. Tran-
ter, N. Ding, B. Campbell, Y. Chen, Z. Chen, B. Chiaro,
A. Dunsworth,
A. G. Fowler,
E. Jeﬀrey,
E. Lucero,
A. Megrant, J. Y. Mutus, M. Neeley, C. Neill, C. Quin-
tana, D. Sank, A. Vainsencher, J. Wenner, T. C. White,
P. V. Coveney, P. J. Love, H. Neven, A. Aspuru-Guzik,
and J. M. Martinis (2016), Phys. Rev. X 6, 031007.
Ortiz, G., J. E. Gubernatis, E. Knill,
and R. Laﬂamme
(2001), Phys. Rev. A 64, 022319.
Ostaszewski, M., E. Grant, and M. Benedetti (2019), arXiv
e-prints , arXiv:1905.09692arXiv:1905.09692 [quant-ph].
Otten, M., and S. Gray (2018a), arXiv:1804.06969.
Otten, M., and S. Gray (2018b), arXiv:1806.07860.
Ouyang,
Y.,
D. R. White,
and E. Campbell (2019),
arXiv:1910.06255.
Paesani, S., A. A. Gentile, R. Santagati, J. Wang, N. Wiebe,
D. P. Tew, J. L. O’Brien,
and M. G. Thompson (2017),
Phys. Rev. Lett. 118, 100503.
Paini, M., and A. Kalev (2019), arXiv:1910.10543.
Parrish, R. M., L. A. Burns, D. G. A. Smith, A. C. Sim-
monett, A. E. DePrince, E. G. Hohenstein, U. Bozkaya,
A. Y. Sokolov, R. Di Remigio, R. M. Richard, J. F.
Gonthier, A. M. James, H. R. McAlexander, A. Ku-
mar, M. Saitow, X. Wang, B. P. Pritchard, P. Verma,
H.
F.
Schaefer,
K.
Patkowski,
R.
A.
King,
E.
F.
Valeev, F. A. Evangelista, J. M. Turney, T. D. Craw-
ford,
and C. D. Sherrill (2017), Journal of Chemical
Theory and Computation 13 (7), 3185, pMID: 28489372,
https://doi.org/10.1021/acs.jctc.7b00174.
Parrish, R. M., E. G. Hohenstein, P. L. McMahon, and T. J.
Martinez (2019a), arXiv:1906.08728.
Parrish, R. M., E. G. Hohenstein, P. L. McMahon, and T. J.
Martinez (2019b), arXiv preprint arXiv:1901.01234.
Parrish, R. M., J. T. Iosue, A. Ozaeta, and P. L. McMahon
(2019c), arXiv preprint arXiv:1904.03206.
Perdomo, A., C. Truncik, I. Tubert-Brohman, G. Rose, and
A. Aspuru-Guzik (2008), Phys. Rev. A 78, 012320.
Perdomo-Ortiz, A., N. Dickson, M. Drew-Brook, G. Rose,
and A. Aspuru-Guzik (2012), Scientiﬁc reports 2, 571.
Peruzzo, A., J. McClean, P. Shadbolt, M.-H. Yung, X.-Q.
Zhou, P. J. Love, A. Aspuru-Guzik,
and J. L. Obrien

## Page 57

(2014), Nature communications 5.
Podewitz, M., M. T. Stiebritz, and M. Reiher (2011), Faraday
Discuss. 148, 119.
Pople, J. A., M. HeadGordon, D. J. Fox, K. Raghavachari,
and L. A. Curtiss (1989), The Journal of Chemical Physics
90 (10), 5622, https://doi.org/10.1063/1.456415.
Poulin, D., M. B. Hastings, D. Wecker, N. Wiebe, A. C. Do-
herty, and M. Troyer (2015), QIC 15.
Poulin, D., A. Kitaev, D. S. Steiger, M. B. Hastings,
and
M. Troyer (2018), Phys. Rev. Lett. 121, 010501.
Poulin, D., A. Qarry, R. Somma, and F. Verstraete (2011),

Sanders, Y. R., G. H. Low, A. Scherer,
and D. W. Berry
(2019), Phys. Rev. Lett. 122, 020502.
Santagati, R., J. Wang, A. A. Gentile, S. Paesani, N. Wiebe,
J. R. McClean, S. Morley-Short, P. J. Shadbolt, D. Bon-
neau, J. W. Silverstone, D. P. Tew, X. Zhou, J. L. O’Brien,
and M. G. Thompson (2018), Science Advances 4 (1),
10.1126/sciadv.aap9646.
Sawaya, N. P. D., and J. Huh (2018), arXiv:1812.10495.
Sawaya, N. P. D., T. Menke, T. H. Kyaw, S. Johri, A. Aspuru-
Guzik, and G. G. Guerreschi (2019), arXiv:1909.12847.
Sawaya,
N.
P.
D.,
M.
Smelyanskiy,
J.
R.
McClean,
and A. Aspuru-Guzik (2016), Journal of Chemical The-
ory and Computation 12 (7), 3097, pMID: 27254482,
https://doi.org/10.1021/acs.jctc.6b00220.
Schneider, C., D. Porras, and T. Schaetz (2012), Reports on
Progress in Physics 75 (2), 024401.
Schuld, M., V. Bergholm, C. Gogolin, J. Izaac, and N. Kil-
loran (2019), Phys. Rev. A 99, 032331.
Schutz, M. (2000), The Journal of Chemical Physics 113 (22),
9986, https://doi.org/10.1063/1.1323265.
Schutz, M., and H.-J. Werner (2000), Chemical Physics Let-
ters 318 (4), 370 .
Seeley, J. T., M. J. Richard,
and P. J. Love (2012), The
Journal of Chemical Physics 137 (22), 224109.
Senjean,
B.
(2019),
“Openfermion-dirac,”
https://github.com/bsenjean/Openfermion-Dirac.
Setia, K., S. Bravyi, A. Mezzacapo,
and J. D. Whitﬁeld
(2018), arXiv:1810.05274.
Setia, K., R. Chen, J. E. Rice, A. Mezzacapo, M. Pistoia, and
J. Whitﬁeld (2019), arXiv:1910.14644.
Setia, K., and J. D. Whitﬁeld (2018), The Journal of Chem-
ical Physics 148 (16), 164104.
Sharma, S., K. Sivalingam, F. Neese,
and G. K.-L. Chan
(2014), Nature chemistry 6 (10), 927.
Shehab, O., K. A. Landsman, Y. Nam, D. Zhu, N. M. Linke,
M. J. Keesan, R. C. Pooser,
and C. R. Monroe (2019),
arXiv:1904.04338.
Shen, Y., Y. Lu, K. Zhang, J. Zhang, S. Zhang, J. Huh, and
K. Kim (2018), Chem. Sci. 9, 836.
Shen, Y., X. Zhang, S. Zhang, J.-N. Zhang, M.-H. Yung, and
K. Kim (2017), Phys. Rev. A 95, 020501.
Shnirman, A., G. Sch¨on, and Z. Hermon (1997), Phys. Rev.
Lett. 79, 2371.
Shor, P. W. (1994), in Foundations of Computer Science, 1994
Proceedings., 35th Annual Symposium on (Ieee) pp. 124–
134.
Shor, P. W. (1996), in Foundations of Computer Science,
1996. Proceedings., 37th Annual Symposium on (IEEE) pp.
56–65.
Smirnov, A. Y., S. Savel’ev, L. G. Mourokh,
and F. Nori
(2007), EPL (Europhysics Letters) 80 (6), 67008.
Sokolov, I., P. K. Barkoutsos, P. J. Ollitrault, D. Green-
berg, J. Rice, M. Pistoia,
and I. Tavernelli (2019),
arXiv:1911.10864.
Somma, R., G. Ortiz, J. E. Gubernatis, E. Knill,
and
R. Laﬂamme (2002), Phys. Rev. A 65, 042323.
Somma, R. D. (2019), arXiv:1907.11748.
Song, C., J. Cui, H. Wang, J. Hao, H. Feng, and Y. Li (2018),

Phys. Rev. Lett. 106, 170501.
Preskill, J. (2018), arXiv preprint arXiv:1801.00862.
Purvis,
G.
D.,
and
R.
J.
Bartlett
(1982),
The
Journal
of
Chemical
Physics
76
(4),
1910,
https://doi.org/10.1063/1.443164.
Raussendorf,
R.
(2012),
Philosophical
Transactions
of
the Royal Society of London A: Mathematical, Phys-
ical
and
Engineering
Sciences
370
(1975),
4541,
http://rsta.royalsocietypublishing.org/content/370/1975/4541.full.pdf.
Raussendorf, R., and H. J. Briegel (2001), Phys. Rev. Lett.
86, 5188.
Raussendorf, R., D. E. Browne,
and H. J. Briegel (2003),
Phys. Rev. A 68, 022312.
Reiher, M., N. Wiebe, K. M. Svore, D. Wecker, and M. Troyer
(2017), Proceedings of the National Academy of Sciences .
Reiner, J.-M., F. Wilhelm-Mauch, G. Schn, and M. Marthaler
(2018a), arXiv:1811.04476.
Reiner,
J.-M.,
S.
Zanker,
I.
Schwenk,
J.
Leppkangas,
F. Wilhelm-Mauch, G. Schn,
and M. Marthaler (2018b),
Quantum Science and Technology 3 (4), 045008.
Richardson, L. F., B. J Arthur Gaunt, et al. (1927), Phil.
Trans. R. Soc. Lond. A 226 (636-646), 299.
Robert, A., P. K. Barkoutsos, S. Woerner, and I. Tavernelli
(2019), arXiv:1908.02163.
Romero, J., R. Babbush, J. R. McClean, C. Hempel, P. J.
Love, and A. Aspuru-Guzik (2019), Quantum Science and
Technology 4 (1), 014008.
Roos, B. O., P. R. Taylor, and P. E. Sigbahn (1980), Chemical
Physics 48 (2), 157 .
Rossi, E., G. L. Bendazzoli, S. Evangelisti, and D. Maynau
(1999), Chemical Physics Letters 310 (5), 530 .
Rowe, D. J. (1968), Rev. Mod. Phys. 40, 153.
Rubin, N. C. (2016), arXiv:1610.06910.
Rubin, N. C., R. Babbush,
and J. McClean (2018), New
Journal of Physics 20 (5), 053020.
Rungger, I., N. Fitzpatrick, H. Chen, C. H. Alderete, H. Apel,
A. Cowtan, A. Patterson, D. M. Ramo, Y. Zhu, N. H.
Nguyen, E. Grant, S. Chretien, L. Wossnig, N. M. Linke,
and R. Duncan (2019), arXiv:1910.04735.
Ryabinkin, I. G., and S. N. Genin (2018), arXiv:1812.09812.
Ryabinkin, I. G., and S. N. Genin (2019), arXiv:1906.11192.
Ryabinkin,
I.
G.,
S.
N.
Genin,
and
A.
F.
Iz-
maylov
(2019),
Journal
of
Chemical
Theory
and
Computation
15
(1),
249,
pMID:
30512959,
https://doi.org/10.1021/acs.jctc.8b00943.
Ryabinkin,
I.
G.,
T.-C.
Yen,
S.
N.
Genin,
and
A.
F.
Izmaylov
(2018),
Journal
of
Chemical
The-
ory and Computation 14 (12), 6317, pMID: 30427679,
https://doi.org/10.1021/acs.jctc.8b00932.
Sagastizabal, R., X. Bonet-Monroig, M. Singh, M. A. Rol,
C. C. Bultink, X. Fu, C. H. Price, V. P. Ostroukh,
N. Muthusubramanian, A. Bruno, M. Beekman, N. Haider,
T. E. O’Brien, and L. DiCarlo (2019), arXiv:1902.11258.

arXiv:1812.10903.
Song, C., K. Xu, H. Li, Y. Zhang, X. Zhang, W. Liu, Q. Guo,
Z. Wang, W. Ren, J. Hao, et al. (2019), arXiv preprint
arXiv:1905.00320.
Song, C., K. Xu, W. Liu, C.-p. Yang, S.-B. Zheng, H. Deng,
Q. Xie, K. Huang, Q. Guo, L. Zhang, P. Zhang, D. Xu,

## Page 58

D. Zheng, X. Zhu, H. Wang, Y.-A. Chen, C.-Y. Lu, S. Han,
and J.-W. Pan (2017), Phys. Rev. Lett. 119, 180511.
Sparrow, C., E. Mart´ın-L´opez, N. Maraviglia, A. Neville,
C. Harrold, J. Carolan, Y. N. Joglekar, T. Hashimoto,
N. Matsuda, J. L. OBrien, et al. (2018), Nature 557 (7707),
660.
Stair, N. H., R. Huang,
and F. A. Evangelista (2019),
arXiv:1911.05163.
Stephens, A. M. (2014), Phys. Rev. A 89, 022321.
Steudtner, M., and S. Wehner (2018), arXiv:1810.02681.
Stokes, J., J. Izaac, N. Killoran,
and G. Carleo (2019),
arXiv:1909.02108.
Subramanian, S., S. Brierley,
and R. Jozsa (2018), arXiv
preprint arXiv:1806.06885.
Sugisaki, K., S. Nakazawa, K. Toyota, K. Sato, D. Shiomi,
and T. Takui (2019), ACS Central Science 5 (1), 167,
https://doi.org/10.1021/acscentsci.8b00788.
Sugisaki,
K.,
S. Yamamoto,
S. Nakazawa,
K. Toyota,
K. Sato, D. Shiomi,
and T. Takui (2016), The Journal
of Physical Chemistry A 120 (32), 6459, pMID: 27499026,
https://doi.org/10.1021/acs.jpca.6b04932.
Sugisaki, K., S. Yamamoto, S. Nakazawa, K. Toyota, K. Sato,
D. Shiomi, and T. Takui (2018), Chemical Physics Letters:
X , 100002.
Sun, Q., B. T. C., B. N. S., B. G. H., G. Sheng, L. Zhendong,
L. Junzi, M. J. D., S. E. R., S. Sandeep, W. Sebastian,
and C. G. Kin-Lic (2017), Wiley Interdisciplinary Re-
views:
Computational Molecular Science 8 (1), e1340,
https://onlinelibrary.wiley.com/doi/pdf/10.1002/wcms.1340.
Sung,
K.
(2018),
“https://github.com/quantumlib/
OpenFermion/issues/259,” Accessed: 24.7.2018.
Suzuki, M. (1976), Communications in Mathematical Physics
51 (2), 183.
Svore, K. M., M. B. Hastings,
and M. Freedman (2013),
arXiv:1304.0741.
Sweke,
R.,
F.
Wilde,
J.
Meyer,
M.
Schuld,
P.
K.
Fhrmann, B. Meynard-Piganeau,
and J. Eisert (2019),
arXiv:1910.01155.
Szabo, A., and N. S. Ostlund (2012), Modern quantum chem-
istry: introduction to advanced electronic structure theory
(Courier Corporation).
Szalay, P. G., T. Mller, G. Gidofalvi, H. Lischka,
and
R. Shepard (2012), Chemical Reviews 112 (1), 108, pMID:
22204633, https://doi.org/10.1021/cr200137a.
Szalay,
S.,
M. Pfeﬀer,
V. Murg,
G. Barcza,
F. Ver-
straete, R. Schneider,
and . Legeza (2015), Interna-
tional Journal of Quantum Chemistry 115 (19), 1342,
https://onlinelibrary.wiley.com/doi/pdf/10.1002/qua.24898.
Takeshita, T., N. C. Rubin, Z. Jiang, E. Lee, R. Babbush,
and J. R. McClean (2019), arXiv:1902.10679.
Tang, H. L., E. Barnes, H. R. Grimsley, N. J. Mayhall, and
S. E. Economou (2019), arXiv:1911.10205.
Temme, K., S. Bravyi,
and J. M. Gambetta (2017), Phys.
Rev. Lett. 119, 180509.
Teplukhin, A., B. K. Kendrick,
and D. Babikov (2018),
arXiv:1812.05211.
Terhal, B. M. (2015), Rev. Mod. Phys. 87, 307.
Toloui, B., and P. J. Love (2013), arXiv:1312.2579.
Torrontegui, E., A. Ruschhaupt, D. Gury-Odelin, and J. G.
Muga (2011), Journal of Physics B: Atomic, Molecular and
Optical Physics 44 (19), 195302.
Tranter,
A.,
P.
J.
Love,
F.
Mintert,
and
P.
V.
Coveney
(2018),
Journal
of
Chemical
Theory
and
Computation
14
(11),
5617,
pMID:
30189144,

https://doi.org/10.1021/acs.jctc.8b00450.
Tranter, A., S. Soﬁa, J. Seeley, M. Kaicher, J. McClean,
R. Babbush, P. V. Coveney, F. Mintert, F. Wilhelm, and
P. J. Love (2015), International Journal of Quantum Chem-
istry 115 (19), 1431.
Trotter, H. F. (1959), Proceedings of the American Mathe-
matical Society 10 (4), 545.
Trout,
C. J.,
and K. R. Brown (2015), International
Journal
of
Quantum
Chemistry
115
(19),
1296,
https://onlinelibrary.wiley.com/doi/pdf/10.1002/qua.24856.
Tubman, N. M., J. Lee, T. Y. Takeshita, M. Head-Gordon,
and K. B. Whaley (2016), The Journal of Chemical Physics
145 (4), 044112, https://doi.org/10.1063/1.4955109.
Tubman, N. M., C. Mejuto-Zaera, J. M. Epstein, D. Hait,
D. S. Levine, W. Huggins, Z. Jiang, J. R. McClean,
R. Babbush, M. Head-Gordon, and K. B. Whaley (2018),
arXiv:1809.05523.
Unruh, W. G. (1995), Phys. Rev. A 51, 992.
Urbanek, M., B. Nachman,
and W. A. de Jong (2019),
arXiv:1910.00129.
Van
Voorhis,
T.,
and
M.
Head-Gordon
(2000),
The
Journal
of
Chemical
Physics
113
(20),
8873,
https://doi.org/10.1063/1.1319643.
Veis, L., and J. Pittner (2012), arXiv:1203.6204.
Veis,
L.,
and
J.
Pittner
(2014),
The
Jour-
nal
of
Chemical
Physics
140
(21),
214111,
https://doi.org/10.1063/1.4880755.
Veis, L., J. Viˇsˇn´ak, T. Fleig, S. Knecht, T. Saue, L. Visscher,
and J. c. v. Pittner (2012), Phys. Rev. A 85, 030304.
Verdon, G., M. Broughton, J. R. McClean, K. J. Sung,
R. Babbush, Z. Jiang, H. Neven, and M. Mohseni (2019),
arXiv:1907.05415.
Verstraete, F., and J. I. Cirac (2005), Journal of Statistical
Mechanics: Theory and Experiment 2005.
Verteletskyi, V., T.-C. Yen,
and A. F. Izmaylov (2019),
arXiv:1907.03358.
Vogiatzis,
K.
D.,
M.
V.
Polynski,
J.
K.
Kirkland,
J.
Townsend,
A.
Hashemi,
C.
Liu,
and
E.
A.
Pidko
(2019),
Chemical
Reviews
119
(4),
2453,
https://doi.org/10.1021/acs.chemrev.8b00361.
Wang, C. S., J. C. Curtis, B. J. Lester, Y. Zhang, Y. Y.
Gao, J. Freeze, V. S. Batista, P. H. Vaccaro, I. L. Chuang,
L. Frunzio, L. Jiang, S. M. Girvin,
and R. J. Schoelkopf
(2019), arXiv:1908.03598.
Wang,
D.,
O.
Higgott,
and
S.
Brierley
(2018),
arXiv:1802.00171.
Wang, D. S., A. G. Fowler, and L. C. L. Hollenberg (2011),

Phys. Rev. A 83, 020302.
Wang, H., S. Ashhab, and F. Nori (2009), Phys. Rev. A 79,
042335.
Wang, H., S. Kais, A. Aspuru-Guzik,
and M. R. Hoﬀmann
(2008), Phys. Chem. Chem. Phys. 10, 5388.
Wang, H., L.-A. Wu, Y.-x. Liu,
and F. Nori (2010), Phys.
Rev. A 82, 062303.
Wang, X.-L., L.-K. Chen, W. Li, H.-L. Huang, C. Liu,
C. Chen, Y.-H. Luo, Z.-E. Su, D. Wu, Z.-D. Li, H. Lu,
Y. Hu, X. Jiang, C.-Z. Peng, L. Li, N.-L. Liu, Y.-A. Chen,
C.-Y. Lu,
and J.-W. Pan (2016), Phys. Rev. Lett. 117,
210502.
Wang, Y., F. Dolde, J. Biamonte, R. Babbush, V. Bergholm,
S. Yang, I. Jakobi, P. Neumann, A. Aspuru-Guzik, J. D.
Whitﬁeld, et al. (2015), ACS nano 9 (8), 7769.
Ward, N. J., I. Kassal,
and A. Aspuru-Guzik (2009), The
Journal of Chemical Physics 130 (19), 194105.

## Page 59

Watson, M. A.,
and G. K.-L. Chan (2012), Journal of
Chemical Theory and Computation 8 (11), 4013, pMID:
26605568, https://doi.org/10.1021/ct300591z.
Wecker, D., B. Bauer, B. K. Clark, M. B. Hastings,
and
M. Troyer (2014), Phys. Rev. A 90, 022305.
Wecker, D., M. B. Hastings,
and M. Troyer (2015a), Phys.
Rev. A 92, 042303.
Wecker, D., M. B. Hastings, N. Wiebe, B. K. Clark, C. Nayak,
and M. Troyer (2015b), Phys. Rev. A 92, 062318.
Wendin, G. (2017), Reports on Progress in Physics 80 (10),
106001.
Werner,
H.-J.,
and
M.
Schutz
(2011),
The
Jour-
nal
of
Chemical
Physics
135
(14),
144116,
https://doi.org/10.1063/1.3641642.
White, S. R. (2017), The Journal of Chemical Physics
147 (24), 244102.
Whitﬁeld, J., V. Havlicek,
and M. Troyer (2016), Physical
Review A 94 (3).
Whitﬁeld, J. D. (2013), The Journal of Chemical Physics
139 (2), 021105, https://doi.org/10.1063/1.4812566.
Whitﬁeld, J. D. (2015), arXiv preprint arXiv:1502.03771.
Whitﬁeld, J. D., J. Biamonte, and A. Aspuru-Guzik (2011),

Zhang, S., Y. Lu, K. Zhang, W. Chen, Y. Li, J.-N. Zhang,
and K. Kim (2019), arXiv:1905.10135.
Zhao, A., A. Tranter, W. M. Kirby, S. F. Ung, A. Miyake,
and P. Love (2019), arXiv:1908.08067.
Zhong, H.-S., Y. Li, W. Li, L.-C. Peng, Z.-E. Su, Y. Hu, Y.-M.
He, X. Ding, W. Zhang, H. Li, L. Zhang, Z. Wang, L. You,
X.-L. Wang, X. Jiang, L. Li, Y.-A. Chen, N.-L. Liu, C.-Y.
Lu, and J.-W. Pan (2018), Phys. Rev. Lett. 121, 250505.

Molecular Physics 109 (5), 735.
Whitﬁeld, J. D., P. J. Love,
and A. Aspuru-Guzik (2013),
Phys. Chem. Chem. Phys. 15, 397.
Whitﬁeld, J. D., M.-H. Yung, D. G. Tempel, S. Boixo, and
A. Aspuru-Guzik (2014), New Journal of Physics 16 (8),
083035.
Wiebe, N., D. W. Berry, P. Høyer,
and B. C. Sanders
(2011), Journal of Physics A: Mathematical and Theoreti-
cal 44 (44), 445308.
Wiebe, N.,
and C. Granade (2016), Phys. Rev. Lett. 117,
010503.
Wiesner, S. (1996), arXiv preprint quant-ph/9603028.
Wilson, M., S. Stromswold, F. Wudarski, S. Hadﬁeld, N. M.
Tubman, and E. Rieﬀel (2019), arXiv:1908.03185.
Wu, L.-A., M. S. Byrd, and D. A. Lidar (2002), Phys. Rev.
Lett. 89, 057904.
Xia, R., T. Bian, and S. Kais (2018), The Journal of Physical
Chemistry B 122 (13), 3384.
Xia, R., and S. Kais (2018), Nature Communications 9 (1),
4195.
Yamada, S., T. Imamura,
and M. Machida (2005), in SC
’05: Proceedings of the 2005 ACM/IEEE Conference on
Supercomputing, pp. 44–44.
Yamamoto, N. (2019), arXiv:1909.05074.
Yamazaki, T., S. Matsuura, A. Narimani, A. Saidmuradov,
and A. Zaribaﬁyan (2018), arXiv:1806.01305.
Yanai,
T.,
Y. Kurashige,
W. Mizukami,
J. Chalupsk,
T.
N.
Lan,
and
M.
Saitow
(2015),
International
Journal
of
Quantum
Chemistry
115
(5),
283,
https://onlinelibrary.wiley.com/doi/pdf/10.1002/qua.24808.
Yen, T.-C., R. A. Lang,
and A. F. Izmaylov (2019a),
arXiv:1905.08109.
Yen, T.-C., V. Verteletskyi,
and A. F. Izmaylov (2019b),
arXiv:1907.09386.
Yung, M.-H., J. Casanova, A. Mezzacapo, J. McClean,
L. Lamata, A. Aspuru-Guzik, and E. Solano (2014), Sci-
entiﬁc reports 4, 3589.
Yung, M.-H., J. D. Whitﬁeld, S. Boixo, D. G. Tempel, and
A. Aspuru-Guzik (2012), arXiv:1203.1331.
Zalka, C. (1998), Proceedings of the Royal Society of Lon-
don A: Mathematical, Physical and Engineering Sciences,
454 (1969), 313.
