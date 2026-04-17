---
source_pdf: ../arxiv_2602.11457.pdf
pages: 22
extracted_at: 2026-04-17T12:32:45+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
title: "The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical qubits using quantum LDPC codes"
author: "Paul Webster; Lucas Berent; Omprakash Chandra; Evan T. Hockings; Nouédyn Baspin; Felix Thomsen; Samuel C. Smith; Lawrence Z. Cohen"
---

# arxiv_2602.11457

Original title: The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical qubits using quantum LDPC codes

Author metadata: Paul Webster; Lucas Berent; Omprakash Chandra; Evan T. Hockings; Nouédyn Baspin; Felix Thomsen; Samuel C. Smith; Lawrence Z. Cohen

Source PDF: ../arxiv_2602.11457.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical
qubits using quantum LDPC codes

Paul Webster,∗Lucas Berent, Omprakash Chandra, Evan T. Hockings,
Nou´edyn Baspin, Felix Thomsen, Samuel C. Smith, and Lawrence Z. Cohen†

Iceberg Quantum, Sydney

The realisation of utility-scale quantum computing inextricably depends on the design of practical, low-
overhead fault-tolerant architectures. We introduce the Pinnacle Architecture, which uses quantum low-density
parity check (QLDPC) codes to allow for universal, fault-tolerant quantum computation with a spacetime
overhead significantly smaller than that of any competing architecture. With this architecture, we show that
2048-bit RSA integers can be factored with less than one hundred thousand physical qubits, given a physical
error rate of 10−3, code cycle time of 1 µs and a reaction time of 10 µs. We thereby demonstrate the feasibility
of utility-scale quantum computing with an order of magnitude fewer physical qubits than has previously been
believed necessary.

arXiv:2602.11457v1 [quant-ph] 12 Feb 2026

I.
INTRODUCTION

Quantum computers offer the promise of efficient so-
lutions to currently intractable problems with the poten-
tial to allow breakthroughs in areas such as cryptogra-
phy [1], materials science and chemistry [2]. However,
due to the precision required and the significant levels of
noise that afflict all engineered quantum systems, this is
only possible if quantum computers are fault tolerant [3].
Fault-tolerant quantum architectures are therefore a cor-
nerstone of all efforts to build useful quantum computers.
Sophisticated fault-tolerant architectures have been de-
veloped based on the surface code [4–8]. However, these
suffer from a very high overhead, since they require hun-
dreds or thousands of physical qubits to encode a sin-
gle logical qubit with a low enough failure rate to allow
utility-scale computations. As a result, utility-scale quan-
tum computers based on such architectures are expected
to require at least one million physical qubits [8, 9]. Scal-
ing quantum hardware to this size poses formidable chal-
lenges [9]. Developing fault-tolerant quantum architec-
tures with lower overhead is therefore of the utmost im-
portance.
To meet this goal, we introduce the Pinnacle Architec-
ture. This architecture achieves substantial spacetime re-
ductions compared with prior state-of-the-art architec-
tures [8, 10] by reducing the space overhead relative to
surface code architectures without a commensurate in-
crease in time overhead. We realise these savings through
the use of processing units constructed from bridged
QLDPC code blocks equipped with modular, efficient gad-
gets for performing gates by generalised surgery [11].
We also introduce a new component—the magic engine—
which exploits the multiple logical qubits of QLDPC codes
to simultaneously support magic state distillation and
injection in a single code block, allowing for constant
throughput of high-fidelity magic states with low over-

∗paul@iceberg-quantum.com
† larry@iceberg-quantum.com

head. Moreover, we introduce Clifford frame cleaning as
a new method that allows for efficient parallelism of op-
erations across processing units. In particular, this allows
for parallel access to a quantum memory that can allow
for spacetime overhead reductions by enabling algorithms
to be parallelised by duplicating processing units while
keeping only a single memory. Scalability and hardware-
compatibility is also ensured through a modular structure
which ensures that connectivity between physical qubits
is only required on a length scale constant in the number
of logical qubits. We summarise the main features of the
architecture in Section II A and, after reviewing relevant
background concepts in Section III, we then provide a full
presentation of the general architecture Section IV, and a
specific instantiation in Section V.

We benchmark the performance of the Pinnacle Archi-
tecture by presenting a compilation to a standard appli-
cation: factoring 2048-bit RSA integers [7, 8]. With stan-
dard hardware assumptions (i.e., a physical error rate of
10−3, code cycle time of 1 µs and reaction time of 10 µs),
we show that factoring can be achieved with fewer than
one hundred thousand physical qubits. This outperforms
the previous best result by an order of magnitude [8]. We
further show the broad applicability of the architecture
by showing that it allows for classically intractable in-
stances of the problem of determining the ground-state
energy of the Fermi-Hubbard model to be achieved with
tens of thousands of physical qubits, under the same as-
sumptions. Again, this amounts to an order-of-magnitude
improvement on the best prior end-to-end resource esti-
mates [12]. In addition to these results, we also apply our
compilations under alternative hardware assumptions to
provide optimised resource estimates applicable across a
range of hardware platforms. We summarise these results
in Section II B and present further details in Section VI.

Through the Pinnacle Architecture, we thus open the
door to utility-scale quantum computing on one hundred
thousand physical qubit devices. This has the potential to
significantly accelerate the timescale for commercialised
and impactful quantum computers.

## Page 2

II.
SUMMARY OF CONTRIBUTIONS

A.
Pinnacle Architecture

The Pinnacle Architecture consists of:

• Processing Units consisting of bridged processing
blocks each constructed from a QLDPC code block
with an ancillary measurement gadget system [11].
An arbitrary logical Pauli product measurement can
be performed on the logical qubits of the unit in
each logical cycle.

• Magic Engines consisting of a QLDPC code block
along with ancillary systems for injecting noisy
magic states. In each logical cycle, the magic en-
gine stores a high-fidelity magic state as it is in-
jected into a processing unit in parallel with host-
ing magic state distillation to prepare a high-fidelity
magic state for the next logical cycle. It thereby pro-
vides a high-fidelity magic state per logical cycle for
each processing unit to allow for universal quantum
computing.

• Memory included as an optional component that al-
lows for especially low overhead quantum storage
in code blocks, which can be accessed by processing
units via ports.

Figure 1 shows how the Pinnacle Architecture is assem-
bled from these modules.
Compilation is performed via Pauli-based computa-
tion [13]. This allows for universal fault-tolerant quantum
computing on arbitrarily many logical qubits with a time
cost that scales with the T count.
Features of the Pinnacle Architecture include:

• Low Spacetime Overhead: The use of QLDPC codes
allows order-of-magnitude reductions in physical
qubit number compared with surface code archi-
tectures. This is achieved without the correspond-
ing increase in time overhead of the previous state-
of-the-art QLDPC code architecture—the bicycle ar-
chitecture of Ref. [10]–through the use of efficient
gadget systems that allow for arbitrary logical Pauli
measurements instead of only a subset of them. It
therefore substantially reduces the total spacetime
overhead compared to previous fault-tolerant archi-
tectures.

• Limited Connectivity and Routing: The architecture
requires only interactions between physical qubits
on the scale of a processing block, which is constant
in the number of logical qubits. This means that it
does not depend on all-to-all connectivity but in-
stead is implementable on hardware platforms that
support quasi-local connections between physical
qubits separated by a bounded distance. Moreover,

2

arbitrary quantum circuits can be performed effi-
ciently using a static configuration of processing
blocks without depending on long-distance routing.

• Modularity and Parallelism: Computations can be
separated across multiple processing units with lim-
ited connectivity between them, allowing compati-
bility with modular hardware. Efficient parallelism
of non-Clifford gates is also supported by introduc-
ing the new technique of Clifford frame cleaning to
supplement this modular structure. This technique
also allows parallel, read-only access to memory by
multiple processing units.

The Pinnacle architecture therefore offers a new alter-
native architecture that is both practical for implementa-
tion on a range of hardware platforms and significantly
more efficient than previous state-of-the-art alternatives.

B.
Results

For concreteness, we present a specific instantiation
of the Pinnacle Architecture using the family of gener-
alised bicycle codes and the modular, efficient measure-
ment gadgets introduced in Ref. [11]. Based on compila-
tion to this instantiation, we present resource estimates
for two benchmark applications.
First, we consider determination of the ground state
energy of the Fermi-Hubbard model via plaquette Trot-
terisation [14]. As shown in Fig. 2, we achieve order-of-
magnitude reductions in physical qubit number relative to
the best available end-to-end surface code analysis [12].
For example, we find that at a lattice size of L = 16 (with
a coupling strength of u/τ = 4), only 62 thousand physi-
cal qubits are required at a physical error rate of p = 10−3

and only 22 thousand at p = 10−4. This compares with
940 thousand and 200 thousand, respectively, in Ref. [12].
We achieve these results while maintaining a modest run-
time per shot of 1–4 minutes with microsecond code cycle
times or 1–3 days with millisecond code cycle times.
Second, we analyse factoring RSA integers using an al-
gorithm based on that of Ref. [8]. Fig. 3 shows the required
physical qubits and runtime to factor a 2048-bit integer for
different code cycle times and physical error rates. With
standard assumptions of a physical error rate of p = 10−3

and a code cycle time of 1 µs and a 10 µs reaction time (see
Section III for definitions of these timescales), factoring is
possible with fewer than one hundred thousand physical
qubits, compared with the previous best result of close to
one million physical qubits [8]. Moreover, through par-
allelising the algorithm, we achieve an efficient spacetime
trade-off that allows for low overhead factoring in feasible
runtimes even with longer code cycle times. For example,
with a code cycle time of 1 ms, factoring can be completed
in one month with 3.1 million physical qubits at a physi-
cal error rate of p = 10−4 (typical of trapped ions [15]) or
with 13 million physical qubits at a physical error rate of
p = 10−3 (typical of, for example, neutral atoms [16]).

## Page 3

3

(a) Example of the Pinnacle Architecture with one processing unit and approximately one hundred thousand physical qubits.

(b) Example of the Pinnacle Architecture with 81 processing units and approximately one million physical qubits.

FIG. 1. Examples of the Pinnacle Architecture. These two examples represent specific examples of different space-time trade-offs and
code block choices, optimised for RSA-2048 factoring in different hardware regimes. Example (a) allows factoring in one month with
a physical error rate of p = 10−3 and a code cycle time of tc = 1 µs. Example (b) allows factoring in three months with a physical
error rate of p = 10−4 and a code cycle time of tc = 1 ms. Shorter runtimes can be achieved by adding more processing units,
increasing paralellisation at the cost of additional physical qubits.

We therefore conclude that the Pinnacle Architecture
can be used to achieve utility-scale quantum computation
with significantly reduced overhead across multiple appli-
cations and a range of hardware regimes.

III.
BACKGROUND

In this section we review concepts of fault-tolerant
quantum computation with QLDPC codes.

A.
Code Blocks

A code block is an instantiation of an Jn, k, dK quan-
tum error-correcting code. Error correction is facilitated
by repeatedly performing a syndrome extraction circuit
on the code block. This circuit involves measuring a set of
parity check operators, which collectively yield an error
syndrome. This is done with the use of nc ancilla qubits; in
each code cycle, each of these is entangled with the code
qubits in accordance with one of the parity check opera-
tors and then destructively measured. A code block there-

FIG. 2. Physical qubits required for determining the ground
state energy of the Fermi-Hubbard model on an L × L lattice
to 0.5% relative precision. Surface code values correspond to the
minimum quoted number of physical qubits with u/τ = 4 in
Ref. [12].

## Page 4

4

(a)

(b)

FIG. 3. Optimal expected runtime for factoring an RSA-2048 integer on the Pinnacle Architecture as a function of the number of
physical qubits and the code cycle time at physical error rates of (a) p = 10−3 and (b) p = 10−4. White areas indicate insufficient
physical qubits to implement the algorithm. The reaction time in all cases is assumed to be equal to ten times the code cycle time.

## Page 5

fore requires a total of ncb = n + nc physical qubits. In
order to ensure robustness against measurement errors,
the results of dt = Θ(d) code cycles must be combined
to yield a reliable error syndrome; this is referred to as a
logical cycle.

We assume the use of QLDPC codes [17, 18]. These are
defined by having low parity check operator weights and
qubit degrees (i.e., the number of parity checks supported
on each qubit). Precisely, these check weights and qubit
degrees are bounded by a constant independent of the
code distance. This ensures that syndrome extraction cir-
cuits can have constant depth, and therefore be fault tol-
erant. The most widely used QLDPC codes are distance-d
(rotated) surface codes [4], which are Jd2, 1, dK codes with
nc = d2−1 parity checks which have weight at most four
and require only nearest-neighbour interactions. Surface
code blocks therefore use 2d2−1 physical qubits to encode
one logical qubit. However, by relaxing the requirement
of nearest-neighbour interactions, more general QLDPC
codes can allow for many logical qubits to be encoded
in a single code block. This can allow for significant re-
ductions in the overhead of physical qubits required per
logical qubit [18]. The required non-local interactions are
supported on a range of hardware platforms [19–23].

B.
Processing Blocks

To allow for fault-tolerant quantum computation, in-
stead of only passive storage of quantum information, the
concept of a code block must be generalised to a process-
ing block. A processing block allows for logical operations
to be implemented on its encoded logical qubits.

A QLDPC code block can be turned into a processing
block by appending a measurement gadget system that al-
lows for generalised lattice surgery [24–26]. This construc-
tion ensures that the combined code block-gadget system
constituting the processing block remains a QLDPC code,
while also ensuring that measuring a selected Pauli logi-
cal operator of the code is equivalent to the product of a
set of parity check measurements on the gadget system.
This allows for a logical Pauli to be measured in parallel
with error correction within a logical cycle by performing
a modified circuit for syndrome extraction on the full pro-
cessing block [27]. Arbitrary logical Pauli measurements
can then be performed across multiple processing blocks
by bridging the gadget systems of these blocks [28, 29].
The number of physical qubits in the processing block is
given by npb = ncb +nG +nb, where nG is the number of
physical qubits in the gadget system and nb is the number
of physical qubits used to bridge it to another processing
block.

5

C.
Pauli-Based Computation

When combined with injected magic states, logical
measurements across bridged processing blocks support
universal quantum computation on the encoded logical
qubits using Pauli-based computation [13].
Indeed, a
quantum circuit on κ qubits with a T count of τ and any
number of Clifford gates can be performed using τ + κ
Pauli measurements and one |T⟩state for each of the first
τ measurements [6]. More generally, if the circuit also
contains o intermediate Pauli measurements on which
later operations adaptively depend, then the circuit can be
performed using τ + κ + o Pauli measurements without
any additional |T⟩states. This implies that such a circuit
can be performed fault-tolerantly using ⌈κ/k⌉Jn, k, dK
bridged processing blocks in τ + κ + o logical cycles.
The compilation which allows for this implementation
follows that presented in Ref. [6]. First, each T gate is re-
placed by a magic state injection circuit, which requires
one Pauli measurement with support on the processing
block. Then, all Clifford gates are commuted through to
the end of the circuit and absorbed into the final measure-
ment of each of the κ qubits. This is done using the rule
that the Pauli defining the basis of each measurement is
transformed by conjugation by each Clifford that either
passes through it or (in the case of the final measurements)
that it absorbs. By definition, Clifford gates map Pauli op-
erators to Pauli operators under conjugation, so the re-
sulting circuit consists of τ + κ + o Pauli measurements,
along with a |T⟩state for each T gate, as required.

D.
Relevant Timescales

There are three relevant timescales that we use in the
determination of the runtime of a fault-tolerant quantum
circuit. First, there is the code cycle time tc, which is the
time required for the completion of one code cycle (i.e.,
one round of syndrome extraction). This time is hardware-
dependent, with typical estimates for different platforms
ranging from 1 µs to 1 ms [16, 22, 30–32]. Second, there
is the logical cycle time tl, which is the time required for
one logical cycle. Since a logical cycle consists of dt code
cycles, this is related to the code cycle time by tl = dttc.
Finally, there is the reaction time tr [7]. This is defined
as the minimum time between the start of one logical mea-
surement, M and the start of any subsequent measure-
ment whose basis depends adaptively on the outcome of
M. The reaction time is dependent on the classical con-
trol system of the quantum hardware. For simplicity, we
assume throughout that the reaction time is equal to ten
times the code cycle time, i.e., tr = 10tc. Since tc ≥1 µs
for all resource estimates we present, this implies that the
reaction time always exceeds the conventionally-assumed
minimum value of 10 µs [7]. With this reaction time, our
architecture is not reaction-limited provided that dt ≥10
for all code blocks, which is true for all resource estimates

## Page 6

we present.

IV.
THE PINNACLE ARCHITECTURE

In this section we present the Pinnacle Architecture, a
low-overhead, modular and parallelisable quantum com-
puting architecture based on QLDPC codes. We begin by
presenting the modules that constitute the architecture—
processing units, magic engines and memory—and then
describe the overall operation, structure, and scalability
of the architecture.

A.
Modules

1.
Processing Units

The primary modules of the architecture are process-
ing units. A processing unit uses β processing blocks of
an Jn, k, dK QLDPC code to allow fault-tolerant quantum
computation on κ := βk logical qubits. These processing
blocks can be arranged in a line with bridges connecting
nearest-neighbour blocks. This allows for the measure-
ment of an arbitrary logical Pauli operator, supported on
any or all of the logical qubits in the processing unit, in
each logical cycle.

2.
Magic Engines

To allow for universal computation, we introduce a
new module, which we refer to as a magic engine.
A
magic engine allows magic states to simultaneously be
produced and consumed to provide a continuous through-
put of magic states to an associated processing unit.
Specifically, each processing unit is equipped with one
magic engine. The magic engine produces one encoded
| ¯T⟩magic state in each logical cycle, and is also bridged
to its associated processing unit to allow a joint measure-
ment with that unit in parallel with state production. This
is intended to ensure that in each logical cycle there is a
magic state available for the processing unit to consume
(i.e., the state produced in the previous logical cycle).
A magic engine can be constructed from an Jne, ke, deK
QLDPC code block as follows. Partition the logical qubits
of the code block into two halves, which we label the left
(L) and right (R) logical sectors. In odd-numbered logical
cycles, a magic state is produced by performing a magic
state distillation circuit consisting of a sequence of magic
state injections. These are implemented by joint logical
measurements on the logical qubits of the L logical sec-
tor and small ancilla systems that hold noisy |T⟩states.
The result is that the first logical qubit of the L logical
sector is in an encoded | ¯T⟩state at the end of the logical
cycle. In parallel, a magic state is consumed from logical

6

FIG. 4. Structure and operation of a magic engine. Magic state
distillation is applied on one logical sector of a QLDPC code
block using noisy |T⟩states injected from ancillary systems. In
parallel, an arbitrary Pauli measurement on the processing unit
joint with ¯Z1 on the other logical sector injects an encoded | ¯T⟩
state that was distilled in the previous logical cycle.

sector R by performing a logical measurement of an ar-
bitrary logical operator on the processing unit joint with
¯Z on the first logical qubit of R. This allows for the in-
jection of the | ¯T⟩state to perform arbitrary π

8 Pauli rota-
tions on the processing unit. To complete the injection, an
¯X measurement is also required on the first logical qubit
of R; a change of basis can be performed between log-
ical cycles to allow that logical qubit to be offline while
it is performed in parallel with the next logical cycle. In
even-numbered logical cycles, the roles of the two logical
sectors are swapped.
Since magic state distillation relies on post-selection,
for each logical cycle there is some probability pr that the
state produced by the magic engine is rejected. When this
happens—and if a magic state is required for the next log-
ical cycle—the processing unit can be left idle for the next
logical cycle to allow for a new magic state to be prepared.
This causes the expected number of logical cycles required
per T gate to increase from 1 to α = (1 −pr)−1. The dis-
tillation protocol should be chosen such that pr is small to
ensure that this effect is also small.

3.
Memory

The architecture can also include memory. This is op-
tional, but it is useful in cases where a large number
of logical qubits must be stored but not processed.
It
consists of ν code blocks of an Jnm, km, dmK quantum
error-correcting code encoding µ = νkm logical qubits.
Since these logical qubits are not processed, full process-
ing blocks are not required. However, to facilitate rear-
rangement of the memory, we ensure that each code block
has nm ancilla qubits (including those used for syndrome

## Page 7

extraction). This means that the memory consists of a to-
tal of 2νnm physical qubits.

Memory is accessed by processing units via ports. To
facilitate this, we partition the logical qubits of the mem-
ory into sets of size w, which we refer to as windows. For
simplicity, we enforce the condition that each window is
contained within a single code block; this implies that w
divides km such that there are a total of νkm/w windows.
Each port is associated with one window and consists of
a gadget that allows for arbitrary logical Z-type measure-
ments on the w logical qubits of that window. Bridging a
processing unit to a port then allows for any circuit with
arbitrary gates on the processing unit and controls on
the w logical qubits of the memory window to be imple-
mented (via Pauli-based computation). This is sufficient
to allow read-only access to that window of memory by
the processing unit [33]. More generally, we can assign a
port to any subset of the windows of the memory. Pro-
vided the gadgets constituting each of these ports allow
for arbitrary logical Z measurements to be performed in
parallel, this can allow for up to νkm/w processing units
to access the memory in parallel.

For each processing unit to access the full memory, the
memory code blocks must be permuted. To ensure that
this does not require arbitrary routing, we impose the con-
straint that each code block is to be shifted by at most one
position per logical cycle. We may then perform the re-
quired permutation without requiring connectivity on a
longer scale than the size of a code block as follows. The
ν memory code blocks are arranged such that the ith and
(i + 1)th (mod ν) code blocks are adjacent for 1 ≤i ≤ν
(e.g., in a loop). A cyclic shift of memory code blocks is
performed by physical SWAPs of the jth data qubit in code
block i with the jth ancilla qubit in code block i + 1 (mod
ν) for 1 ≤i ≤ν and 1 ≤j ≤n, followed by a (local)
SWAP of the jth data qubit and jth ancilla qubit in each
code block. Since such a circuit requires only one layer
of non-local gates confined to the scale of a code block,
whereas a QLDPC syndrome extraction circuit generally
requires many such gates, we assume that this rearrange-
ment can be completed during a code cycle and so its time
cost is negligible. By applying ν of these cyclic shifts over
a period of at least ν logical cycles, every window of mem-
ory can be accessed by each processing unit.

B.
Operation

We now consider how the architecture operates while
performing a quantum computation. To aid understand-
ing, we start with a simplified baseline operation (Sec-
tion IV B 1) and incrementally build up to the most general
operation (Section IV B 4).

7

1.
Serial Operation

As a baseline, let us first consider a serial mode of op-
eration. In this mode, there is a single processing unit
with κ logical qubits (and, for simplicity, we assume there
is no memory). During each logical cycle, a joint logical
Pauli measurement is performed on the processing unit
and magic engine. In parallel, the magic engine produces
a magic state for the next logical cycle. Accounting for
a magic engine reject rate of pr, this allows for an arbi-
trary Clifford+T circuit on κ qubits with a T count of τ
and o intermediate measurements to be performed fault-
tolerantly in an average of τ/(1 −pr) + κ + o logical
cycles.

2.
Fully Parallel Operation

As a next step, we can consider the case of implement-
ing a circuit that can be completely separated out into
two or more independent circuits. In this context, we
can separate the architecture up into a separate process-
ing unit for each independent circuit and perform all the
circuits in parallel. This reduces the number of logical
timesteps required from τ/(1 −pr) + κ + o to approx-
imately maxi
τi/(1 −pr) + κi + oi

where τi, κi and
oi denote the number of T gates, logical qubits and in-
termediate logical measurements in the ith independent
circuit. This expression omits an O
p

maxi (τi)

cor-
rection arising from variance in the proportion of magic
states rejected in different processing units across the du-
ration of the circuit. Since we are interested in circuits
where the T count is large, we assume this correction is
negligible.
An example of where this mode could be used is in im-
plementing multiple shots of an algorithm in parallel. In
this context, it can be considered a way to use a greater
number of qubits to reduce the runtime compared to when
all shots are performed in series.

3.
Flexibly Parallel Operation

More common and general is the case where a circuit
can be implemented partially in parallel. In such a circuit,
no subset of logical qubits is entirely separable from the
rest, but significant parts of the circuit involve operations
on disjoint registers of logical qubits. A conventional cir-
cuit implementation would allow such parts of the circuit
to be performed in parallel on the disjoint registers. We
now show how this can be done in the Pinnacle Architec-
ture.
Parallelism of this kind is inherently challenging with
Pauli-based computation because of the effect of commut-
ing Clifford gates through to the end. To see this, consider
the case of a Clifford frame at a given point in the circuit

## Page 8

(i.e., the product of Clifford gates up to that point) that
corresponds to an entangling gate between two process-
ing units. Then, as Cliffords are commuted through the
circuit the supports of the logical measurements on one
processing unit will spread out to straddle both. In partic-
ular, this means that a logical measurement correspond-
ing to a | ¯T⟩state injection—required to perform a ¯T gate
on either processing unit—comes to have support on both
units. Since each processing unit only allows one logical
measurement per logical cycle, this implies that a ¯T gate
on a logical qubit on one processing unit cannot be per-
formed in parallel with a ¯T gate acting on a logical qubit
of the other processing unit.
Parallelism therefore requires that the Clifford frame
acts as a tensor product across the units which are to be
parallelised. One way to achieve this (following Ref. [34])
could be to perform CNOT gates that entangle processing
units physically using additional logical measurements, so
that they can be excluded from the Clifford frame. How-
ever, this approach leads to a time cost that scales with
the number of CNOT gates, which can quickly cause the
benefits of parallelism to be erased. In particular, it per-
forms poorly in the common setting where one part of the
circuit is highly parallelisable but another is not, since the
cost of parallelising the former part scales with the num-
ber of entangling gates in the latter part.
We instead propose a more flexible alternative that al-
lows for parallelism when it is beneficial but avoids the
cost of physically implementing every CNOT gate. To de-
velop this approach, we introduce the technique of Clif-
ford frame cleaning. Precisely, let K be a set of logical
qubits and K′ ⊂K be a subset of
K′
of these logi-
cal qubits. If C is a Clifford frame acting on K, cleaning
C off K′ means physically performing a Clifford U such
that CU acts trivially on K′. We show in Lemma 1 that
this can be done using at most 4
K′
logical Pauli product
measurements on K.
Harnessing this tool, our flexible parallelism frame-
work is as follows. We consider processing units to auto-
matically be joined into larger units at any point in the cir-
cuit where there is an entangling gate between the units.
From that point on, ¯T gates and logical measurements on
any of the constituent processing units of this joined unit
are assumed to require joint logical Pauli product mea-
surements across the entire joined unit, meaning that only
one such gate can be implemented on the joined unit per
logical timestep. At any later time, we can then separate a
processing unit (with κ logical qubits) from a joined unit
by cleaning the Clifford frame off the joined unit, at a cost
of at most 4κ additional logical timesteps. From then on,
logical measurements on the separated unit can again be
performed in parallel with the unit it was separated from.
This process is shown in Fig. 5.
This framework allows for processing units to be joined
during parts of a circuit in which many inter-unit gates
occur, but then to be separated again (at a relatively small
cost) for parts of the circuit that are more amenable to par-

FIG. 5. Process of joining and separating processing units with
Clifford frame cleaning to allow for flexible parallelism.

## Page 9

allelisation. The choice of if and when to separate units
can be specifically optimised for compilation of any par-
ticular circuit, with the potential for significant time sav-
ings compared to either a fully serial approach or an ap-
proach that depends on physical implementation of all
inter-unit entangling gates.

4.
General Operation

The final step to our fully general operation is to op-
tionally incorporate the memory. Recall that each pro-
cessing unit accesses memory via a port. We allow for
read-only memory access, which requires only gates that
act as a control on the port and a target on the processing
unit [8, 33]. This means that the access can be provided
by using logical CNOT gates with controls on the logical
qubits in a port and targets on ancillary logical qubits in
the processing unit to fan out memory data onto the pro-
cessing unit at the start of the access and fan in at the end
of the access. Since such operations commute, arbitrarily
many processing units can access the memory in parallel,
provided they each have ports with measurement gadgets
that can be used in parallel.
Implementing memory access on the Pinnacle Archi-
tecture uses the same concepts of joining and separating
units presented in Section IV B 3. Specifically, when a pro-
cessing unit accesses a window of the memory, the port
associated with that window is joined onto the process-
ing unit by the logical CNOTs which implement the fan-
out. Since no entangling gates act within the memory,
these ports can always be assumed to be separate from
one another. Moreover, as all gates between a port and
processing unit act as controls on the port, commuting
through the Clifford frame only gives rise to Z-type log-
ical measurements on the port. When the access is fin-
ished, the Clifford frame is cleaned off the port such that
the port can be separated from the processing unit again.
As shown in Lemma 2, this requires only 2w logical cy-
cles for a port of w qubits. This ensures that subsequent
logical measurements on the processing unit act trivially
on the memory logical qubits, enabling subsequent access
by different processing units.

C.
Scalability

The architecture is designed to ensure that its opera-
tion remains feasible at large scale. Specifically, because
the processing units are assembled from individual pro-
cessing blocks that are all connected via bridges between
nearest neighbours, logical operators with support across
any subset of processing blocks in a processing unit can be
measured using connections between physical qubits that
are restricted to the scale of one processing block. This
means that arbitrarily large processing units supporting
arbitrarily many logical qubits can be realised with phys-

9

ical connections of constant scale. For example, in a two-
dimensional arrangement of qubits, this scale is approxi-
mately the square-root of the size of the processing block
√npb.
This means that the architecture can be supported even
on hardware platforms that only support interactions
whose fidelity decreases continuously with the interac-
tion distance. Moreover, it means that no routing of log-
ical qubits across the architecture is required. Instead, all
changes between logical cycles required to support differ-
ent logical operations are confined to the scale of a pro-
cessing block. As discussed in Section V A, code choice
and gadget design can minimise the dynamism required
even on this scale to be very limited. In summary, the sig-
nificant overhead reductions supported by QLDPC codes
can be realised with interactions and rewiring confined to
a fixed scale, which can be chosen to be consistent with a
given hardware platform.
The further modularisation of the architecture into pro-
cessing units provides an additional benefit. Specifically,
feasibility limitations are expected to require large-scale
quantum computers on many hardware platforms to be
assembled from smaller modules [9, 10, 35]. This opens up
an opportunity for hardware and architecture co-design
that can be realised by associating these hardware mod-
ules with processing units of the Pinnacle Architecture.
This is beneficial because it aligns compilation impera-
tives with hardware constraints.
Gates between hard-
ware modules should be minimised since they are likely to
have poorer performance than intra-module gates, while
gates between processing units should also be minimised
to maximise parallelism.

D.
Structure

The only constraint on the assembly of the architecture
is that modules that are joined together at any time must
be connected in the architecture. This ensures that these
modules can be bridged, and therefore logical measure-
ments are possible across them, without requiring long-
distance transport. In particular, this means that each pro-
cessing unit must be adjacent to its associated magic en-
gine and—if a memory is present—a port of memory. If
a set of processing units is to be joined, these processing
units should also be adjacent to each other.
The structure of the architecture for different example
instantiations is shown in Fig. 1.

V.
INSTANTIATION OF THE ARCHITECTURE

In this section, we present a specific instantiation of
the Pinnacle Architecture using a family of generalised
bicycle (GB) codes, along with numerical simulation re-
sults used to determine the logical error rates that can be
achieved for different of code distances and physical error

## Page 10

rates.

A.
Setup

GB codes are defined by a lift l ∈N and sets A, B ⊆
Zl [36]. They have n = 2l physical qubits which can be
divided into two sectors of l physical qubits each, which
we label L and R. The parity check operators of the code
are then

SX,j =
Y

a∈A
X(j+a),L
Y

b∈B
X(j+b),R,
(1)

SZ,j =
Y

a∈A
Z(j−a),R
Y

b∈B
Z(j−b),L.
(2)

Here, the first subscript on each operator denotes the po-
sition of a qubit within the sector and the second denotes
the sector. For any σ ∈Zl, a cyclic shift of all physical
qubits by σ sites preserves the group of parity check op-
erators, making it a qubit automorphism.
We construct code blocks from the specific family of
GB codes presented in Ref. [11], first explored in Ref. [37].
These codes have weight-six parity check operators and
require only simple, relatively short-distance transport
patterns for syndrome extraction. The code family is pa-
rameterised by an integer m > 3, and defined by choos-
ing the lift to be l = 2m −1, as well as the sets A
and B such that the polynomials A(x) = P

a∈A xa and
B(x) = P
b∈B xb generate the parity check matrices of
the classical simplex codes. Classical simplex codes have
parameters [2m −1, m, 2m−1] [38]. We conjecture that
the GB codes constructed in this way have parameters
J2(2m −1), 2m, m + (m −4)2K. We present explicit in-
stances for the first five codes in the family in Table I.
For these codes, we empirically find that performance
is improved by allowing for slightly more rounds of syn-
drome extraction than the code distance. Guided by this
observation, we choose to use dt = d + 2 code cycles per
logical cycle.
The code blocks are extended to processing blocks by
supplementing them with the gadget system presented
in Ref. [11]. This gadget system consists of four gadgets
which correspond to four seed operators chosen such that
all logical Pauli operators are products of cyclic shifts of
the seed operators. In particular, the k logical qubits of
each codes naturally divide into two logical sectors (L and
R) with k/2 logical qubits in each such that one X-type
and one Z-type seed operator suffice for each logical sec-
tor. Constructing, bridging, and shifting four gadgets ca-
pable of measuring each of the seed operators therefore
suffices to measure arbitrary logical Pauli operators on a
code block. This means that only minor alterations are re-
quired to allow the same syndrome extraction circuit to
measure any logical Pauli operator. Four bridges are also
included per processing block; three are used to bridge the
four gadgets within the block, while the fourth is used to

10

bridge the last gadget of the block to the first gadget of
the next block.
Therefore, letting ng be the number of physical qubits
per gadget and nb be the number of physical qubits per
bridge, and accounting for nc = n check qubits, the total
number of physical qubits per processing block is given
by:

npb = ncb + 4ng + 4nb.
(3)

The values of these parameters are provided in Table I.
These gadgets can also be used to measure certain sets
of logical operators in parallel (i.e., in a single logical cy-
cle) via the inclusion of duplicate gadgets. Specifically, a
set of m logical operators P1, . . . Pm can be measured in
parallel by using a different copy of the gadget to measure
each, provided they commute on every physical qubit.
This qubit-wise commutation condition ensures that the
check operators from different gadgets all commute. Con-
necting m gadgets to the same code block can increase
code check weights and qubit degrees in places where
multiple gadgets are joined to the same qubit or check.
In theory, this increase can be by up to m but, with in an
appropriately chosen basis, it is typically significantly less
than this. If necessary, a small number of ancillary qubits
can also be used to reduce check weights and/or qubit de-
grees [25, 39].

B.
Modules

1.
Processing Units

Using β processing blocks constructed from the GB
code family introduced above (for any β ∈N), we can
encode κ = βk logical qubits in βnpb physical qubits.
Specifically, with a code distance of d = 16, we can en-
code 14β logical qubits in 860β physical qubits. For better
protection, we can instead use a code distance of d = 24
and encode 16β logical qubits in 1620β physical qubits.

2.
Magic Engines

We construct each magic engine from code blocks of
the same GB code family as those used for the processing
blocks. These blocks naturally have the required L and R
logical sectors, with k/2 > 5 logical qubits in each sector
when d ≥10.
We use 15-to-1 magic state distillation on these code
blocks to produce encoded | ¯T⟩magic states [40]. Follow-
ing Ref. [41], this can be done using fifteen auto-corrected
Z-type π/8 rotations, followed by four logical X-type
measurements used for post-selection. Each of these ro-
tations is implemented by injecting a noisy |T⟩from a
bridged pair of small ancillary Jna, 1, daK codes. The | ¯T⟩
state is prepared in the first of these codes using stan-
dard techniques (e.g., using a post-selected state injection

## Page 11

11

TABLE I. Instances of the family of generalised bicycle codes. For each code, the parameters Jn, k, dK are provided, along with the
number of code cycles per logical cycle, dt = d+2. The codes are defined by l, A, and B, alongside Eq. (1) and Eq. (2). The remaining
columns show the number of physical qubits in their code blocks, gadgets, bridges and processing blocks. See Ref. [11] for more
details.

circuit [42] or, if necessary to increase the input state fi-
delity, zero-level distillation [43, 44] or magic state culti-
vation [45, 46]). The second of the codes provides an ancil-
lary logical qubit for auto-correction, to account for Clif-
ford corrections from the state injection. Parallel joint log-
ical measurements (repeated da times) between the L log-
ical sector of the GB code and the first ancillary code, and
between the two ancillary codes, are performed by gen-
eralised surgery, followed by destructive measurements
of the ancillary codes, to implement the auto-corrected
injection circuit presented in Fig. 13c of Ref. [41]. Paral-
lel X-type measurements (repeated r times) are then per-
formed on qubits 2–5 of the L logical sector and the state
rejected if any of these four measurement results is −1.
The physical qubits that must be accounted for in this
protocol are the GB code block itself (ncb), sixteen gadgets
used to perform up to sixteen logical measurements in
parallel (16ng), fifteen pairs of ancillary Jna, 1, daK codes
from which states are injected (2 × 15(2na −1)), fifteen
pairs of bridges used to connect these ancillary codes to
each other and to the GB code block and (if necessary)
ancillary qubits (nα) used to reduce the infidelity of input
states (e.g., by magic state cultivation). The total overhead
of the magic engine is therefore given by

that da + r ≤dt.
In practice, for the applications in Section VI, an out-
put fidelity of pT ≈10−11 is sufficient, which is achiev-
able provided with an input magic state infidelity of
pin ≈10−4.
For a physical error rate of p = 10−4, the desired out-
put fidelity can be achieved by a state injection circuit into
a colour code with post-selection [42]. Since this proto-
col takes only da + 1 colour code cycles for a distance-da
colour code, it can be attempted multiple times for each
colour code, which—given the post-selection acceptance
rate of 2%—makes the probability of failure to produce
the required states in each logical cycle negligible. This
means that we can assume the overall rejection rate of
the magic engine to be pr = 15p = 0.15%. A distance
of da = 5 for the pair of ancilla codes suffices to achieve
the requirement of a logical error rate much smaller than
pin [47]. Using the results of Section V C, GB code blocks
of distance de = 10 and r ≥7 rounds of X-type mea-
surements also ensure a sufficiently low logical error rate
from the QLDPC code and completion within one logi-
cal cycle for processing block codes of d ≥10 [48]. With
these considerations, the total physical qubit count for the
magic engine in this case is nme,10−4 = 2128.
For higher physical error rates, the input magic state
can be prepared in a rotated surface code using fold-
transversal cultivation [46]. In particular, we consider the
case of p = 10−3 and d = 24 processing blocks. In this
case, da = 9 rotated surface codes are sufficient for a logi-
cal error rate much smaller than pin [49]. Fold-transversal
cultivation into such codes can be performed to prepare
states with an infidelity of p = 10−4 with a success rate
of approximately 2/3. Post-selection on the final surface
code requires only three code cycles [46] and there are
dt −da = 17 code cycles during which injection into the
GB code is not taking place. Hence, the preparation can
be attempted five times, meaning that at least one suc-
cess on each of the fifteen required surface codes with a
probability of (1 −1/35)15 = 94%. By comparison, the
magic state distillation reject rate of 15pin = 0.15% is
negligible, so we can assume that the overall reject rate is
pr = 6%. To provide a sufficient throughput of cultivated
states that can be escaped into these codes, two copies of
a 25 physical qubit ancilla system are required per sur-

nme = ncb + 16ng + 60(na + da −1) + nα.
(4)

The protocol produces output |T⟩states of fidelity pT ,
which can be arbitrarily close to 35p3
in with a rejection
rate of approximately 15pin, where pin is the infidelity of
the input noisy states [41]. Specifically, to achieve this
we require that the distance of the QLDPC code block, de,
is large enough that the logical error rate of the QLDPC
code block is ≪pT . Hence, the contribution to the out-
put fidelity from logical errors in the QLDPC code block
is negligible. We also require that r is large enough that
the logical error rate of each X-type logical measurement
is ≪pT /pin, so that the probability of an error in a sin-
gle Z rotation both occurring and failing to be detected is
negligible. Finally, we require that da is large enough that
the logical error rate of each ancillary code is ≪pin, so
that the contribution to the probability of errors in each Z
rotation from logical errors during state injection or auto-
correction is negligible. The protocol completes within
the required time of one logical cycle (tl = dttc) provided

## Page 12

face code [46], leading to an additional ancilla overhead
of nα = 2 × 15 × 25 = 750. As shown in Section V C, GB
code blocks of distance de = 24 also satisfy the require-
ment of a logical error rate much smaller than pT . We also
find that r ≥13 rounds of logical X type measurements
suffice to achieve a logical error rate from these measure-
ments of ≪pT /pin = 4 × 10−7. This ensures that the
protocol completes within a d = 24 GB logical cycle of
dt = 26 code cycles. With these considerations, the total
physical qubit count for the magic engine in this case is
nme,10−3 = 8694.

3.
Memory

For the memory, we use the same code blocks as are
used for the processing blocks. For simplicity, we match
the window size with the number of logical qubits in a log-
ical sector, k/2. Each port then corresponds to one of the
Z-type gadgets used in the gadget system of the process-
ing blocks, along with a bridge to connect to a processing
unit. The logical operators that must be measured to ac-
cess the memory commute on every physical qubit and
so can be measured in parallel, as they act across disjoint
processing units and act only as Z-type operators on the
memory. Moreover, since each memory code block has at
most two ports, these measurements increase the check
weight and qubit degree by at most two.
Referring to Table I, the additional number of physical
qubits per port is ng+nb = 88 at d = 16 or ng+nb = 150
at d = 24. Hence, for any ν ∈N, we can encode 14ν
logical qubits in memory such that ρ processing units can
access it in parallel with 508ν + 88ρ physical qubits at
d = 16 or 16ν logical qubits in memory with 1020ν+150ρ
physical qubits at d = 24.

C.
Simulation Results

To assess the logical error rates achievable with dif-
ferent code choices, we perform numerical simulations
of both memory and logical measurements by gener-
alised surgery. These are performed for one logical cycle
(dt = d+2 rounds of syndrome extraction) with standard
circuit-level depolarising noise. For memory experiments
we instead simulated d rounds of syndrome extraction and
rescaled the logical failure rates by (d + 2)/d. Circuits for
the memory simulations are constructed as in Ref. [37],
while circuits for the surgery simulations are constructed
using integer linear programming [50]. We perform un-
correlated (only X-type detectors) most-likely error de-
coding by converting the decoding problem into a mixed
integer program and allow the solver to obtain an optimal
solution. Results of these simulations are shown in Fig. 6.
We assume each point is binomially distributed and use
maximum likelihood estimation to fit the points to the

12

FIG. 6.
Simulation results to determine logical error rates per
processing block (of k logical qubits) per logical cycle of the
Pinnacle Architecture using GB codes of different distances and
across different physical error rates. Solid markers show results
for X-basis memory experiments decoded with most-likely er-
ror decoding. Hollow markers show results for logical measure-
ments by generalised surgery; data was collected for the d = 4,
d = 6 and d = 10 codes at the same physical error rates as
for the memory experiments. Highlighted regions are 99% con-
fidence intervals for the memory experiment data points. The
solid and dashed lines are fits of the ansatz in Eq. (5) to the mem-
ory experiment data and logical measurement data respectively.
We emphasise that ansatz parameters are independent of dis-
tance (i.e., the same equations are used for all codes), which al-
lows for extrapolation of the collected data across the code fam-
ily.

sub-threshold ansatz

pL,cb(p, d) = A
 p

2 +C
.
(5)

B

Here pL is the total logical failure rate for all k logical
observables over dt rounds. It follows from this that the
error rate per logical observable and logical cycle is given
by

 p

2 +C
.
(6)

pL(p, k, d) = A

k

B

The fitted parameters for the ansatz with 95% confidence
intervals are given in Table II. Table III shows the logical
error rates per logical qubit per logical cycle derived from
this ansatz for each of the GB codes considered at physical
error rates of p = 10−3 and p = 10−4.
We emphasise that the purpose of these simulation re-
sults is to benchmark the capabilities of the architecture
and guide code distance choice for resource estimation.
This informs the decision to use most-likely error decod-
ing which correctly decodes all faults of weight less than
d
2 and avoids error floors that can arise from alternatives

## Page 13

TABLE II. Fitted parameters with 95% confidence intervals for
the ansatz in Eq. 5 for memory experiments and logical measure-
ment experiments.

TABLE III. Error rates per logical qubit and logical cycle for log-
ical measurement in GB codes of each distance at physical error
rates of p = 10−3 and p = 10−4. Values correspond to the
central estimates of the fit parameters from the Logical Mea-
surement row of Table II substituted into the ansatz presented
in Eq. (6).

such as belief propagation decoders [51]. The problem of
developing a sufficiently fast decoder for real-time use by
the classical control system of quantum hardware is out-
side the scope of this paper, and we look forward to ad-
dressing it in future work.



VI.
APPLICATIONS

In this section, we show how the Pinnacle Architec-
ture can be applied to two applications: determining the
ground state energy of the Fermi-Hubbard model, and fac-
toring RSA integers.

A.
Fermi-Hubbard Model

In this subsection, we determine the resources re-
quired to estimate the ground state energy of the two-
dimensional Fermi-Hubbard model using the Pinnacle Ar-
chitecture.

1.
Algorithm

The two-dimensional Fermi-Hubbard model represents
a system of interacting fermions and has the Hamiltonian

H = Hh + HI


a†
i,σaj,σ + a†
j,σai,σ

+ u
X

=
X

X

i
ˆni,↑ˆni,↓.

⟨i,j⟩

σ∈{↑,↓}

(7)

Here, i denotes the sites of an L × L lattice, ⟨i, j⟩denotes
pairs of nearest neighbours on this lattice, σ ∈{↑, ↓} de-
notes spins states, a† and a represent creation and annihi-
lation operators, respectively, ˆn = a†a denotes the num-

13

ber operator, and u denotes the (dimensionless) coupling
strength.

We follow Ref. [14] in using plaquette Trotterisation to
determine the ground state energy of the Fermi-Hubbard
model with a relative error of 0.5% of the total lattice en-
ergy. In order to minimise the number of qubits required,
we modify this method by omitting Hamming weight
phasing (which requires a system of 1 ≤α ≤L2/2 an-
cillary logical qubits), instead simply performing each re-
quired phase rotation in sequence. With this simplifica-
tion, the number of logical qubits required is

N = 2L2 + 2.
(8)

This accounts for two logical qubits for each lattice site
(one for each spin state) and two additional logical ancilla
qubits (one for phase estimation and one for repeat until
success synthesis) [14]. From Eq. (F10) of Ref. [14], the T
count for one shot of the algorithm is given by

s

W
ε(1 −x)
3 ×

τ = 6.203



NR
√





!

3W

x√1 −x
√


NR

1.15 log2

+ 9.2

+ NT


.

ε3

(9)

Here, NT = 12L2 and NR = 4L2 are the number of
T gates and arbitrary Z rotations (which are each syn-
thesised from a number of ¯T gates) required per Trotter
step. The number of Trotter steps required for the tar-
get precision is given by the prefactor. In this prefactor,
ε = 0.005E0 corresponds to the required relative error
of 0.5%, where the energy per site E0 is estimated at 1.02
hartrees for u = 4 and 0.74 hartrees for u = 8 [12]. W
is a parameter that bounds the Trotter error; bounds on
this parameter are provided in Ref. [14]. The parameter
x reflects a choice of how to split the error budget across
different sources; we optimise over this in our analysis.

In addition to T gates, the algorithm also requires ad-
ditional logical measurements. In particular, repeat-until-
success synthesis is used to perform each of the NR arbi-
trary Z rotations in each Trotter step [52, 53]. This method
successfully performs the correct rotation with a probabil-
ity of at least one half [53], and so the expected number
of attempts per rotation is at most two. Since one logical
measurement is required per attempt (in addition to the
T gates), this adds an average of up to two logical mea-
surements per arbitrary rotation. Logical measurements
are also required for the final phase estimation. How-
ever, since this is only performed once (not for each Trot-
ter step), it is negligible compared with the T count. We
therefore express T —the sum of the T count and number

## Page 14

of logical measurements—as

s

W
ε(1 −x)
3 ×

T = 6.203





NR
√





!

3W

x√1 −x
√


NR

1.15 log2

+ 11.2

+ NT


.

ε3

(10)

This quantity determines the number of logical cycles on
the Pinnacle Architecture. It is approximately constant in
L because the allowed error is relative to the total energy,
which scales as L2 [12].

2.
Implementation and Results

Concretely, we consider the case of even L ≤32 and
u = 4. In this regime, N ≤2050 and we find numerically
that the number of logical cycles satisfies T = 8 × 106,
which also upper bounds the T count. This implies that
the logical spacetime volume satisfies NT ≤2 × 1010.
Hence, the algorithm can be implemented with negligi-
ble failure probability provided the error rate per logical
qubit and logical cycle satisfies pL ≪5 × 10−11 and the
|T⟩state fidelity satisfies pT ≪10−7. With reference to
Table III, this is satisfied by using the d = 24 GB code in-
stantiation of the architecture for a physical error rate of
p = 10−3 and the d = 10 instantiation for p = 10−4.
To implement this on the Pinnacle Architecture, we
use a single processing unit with β =

N/k

processing
blocks to ensure there are κ ≥N logical qubits available.
We also account for a magic engine for this processing
unit, but do not include memory. The required number of
physical qubits is therefore given by

N


+ nme.
(11)

n = npb

k

Substituting N = 2L2 + 2 and the values for npb, nme
and k from Section V B, the numbers of physical qubits
required with physical error rates of p = 10−3 and p =
10−4, respectively, are therefore

&
L2 + 1

'

+ 8694,
(12)

n10−3 = 1620

8

&
L2 + 1

'

+ 2128.
(13)

n10−4 = 452

6

Table IV shows the number of physical qubits required
for even L ≤32, along with the runtimes with code cycle
times of 1 µs and 1 ms. Figure 2 shows that the number of
physical qubits required is an order of magnitude smaller
than those required using surface codes in Ref. [12].
A full determination of the ground state energy re-
quires multiple shots of the algorithm, with the number

14

TABLE IV. Physical qubits and runtime required to perform one
shot of Fermi-Hubbard ground state energy estimation on an
L × L lattice with a relative error of ≤0.5% of the total lattice
energy. The runtime is approximately independent of L because
the relative error allows for fewer Trotter steps for larger lattices;
runtimes for each value of L are equal to or slightly smaller than
those given. kq represents kiloqubits (×103 qubits).

dependent on the overlap between the initial state and the
true ground state. These shots can be performed in se-
ries (with a proportional increase in run time) or could be
performed in parallel using multiple separate processing
units (with a proportional increase in the required physi-
cal qubits).

B.
RSA Factoring

In this subsection, we show that the Pinnacle Architec-
ture can be used to efficiently perform the factoring nec-
essary to break RSA encryption.

1.
Algorithm

The algorithm we use is a generalisation of that pre-
sented by Gidney in Ref. [8], which uses techniques de-
veloped by Eker˚a and H˚astad [54] and by Chevignard et
al. [55]. We refer to this algorithm as Gidney’s algorithm.
This algorithm uses residue number system arithmetic to
replace modular arithmetic over NRSA (the number be-
ing factored) with modular arithmetic over a set of primes
P that each have size polylogarithmic in NRSA.
This
reduces the number of qubits required for the working
register required for modular exponentiation (the domi-
nant part of the factoring algorithm) from Θ (log NRSA)
to Θ (log log NRSA), reducing the space overhead. For
each individual prime, the time overhead for the modu-
lar exponentiation is also significantly reduced since the

## Page 15

time cost for arithmetic operations such as addition scales
with the size of the input registers. However, in Gidney’s
algorithm, this does not translate to an overall reduction
in runtime because the |P| primes are processed in series.
We generalise Gidney’s algorithm by allowing for the
possibility of processing multiple primes in parallel. This
is done by replacing the working register with ρ copies
of the register, for any positive integer ρ ≤|P|. The el-
ements of P are partitioned into ρ subsets such that the
maximum number of elements in each subset is ⌈|P|/ρ⌉.
The outer loop of Gidney’s algorithm is then applied in
parallel on a different register for each subset. Finally,
parallel reduction is used to combine the accumulators of
each register into a single accumulator by aggregating ac-
cumulators pairwise in the form a binary tree. The final
value of this accumulator matches that of Gidney’s algo-
rithm, since it simply amounts to a reordering of the sum
used to calculate the approximate modular exponential
(Eq. (20) of Ref. [8]). The required result may therefore
be extracted by measurement and classical processing in
the same way. Letting TG be the time cost for Gidney’s
algorithm, our algorithm has a time cost of

T = ⌈|P|/ρ⌉

|P|
TG + O (log ρ) ,
(14)

where the O (log ρ) term accounts for the parallel reduc-
tion required to combine accumulators. Since |P| is large
(e.g., ≈2.1 × 104 for RSA-2048 [8]), this can allow for a
reduction in the time cost by many orders of magnitude.
Importantly, the additional space incurred by this form
of parallelisation is not proportional to the reduction in
time cost. To see why, note that the full register in Gid-
ney’s algorithm has two components — an input register
of m = Θ (log NRSA) logical qubits and a working regis-
ter of Nw = Θ (log log NRSA) logical qubits used to per-
form the approximate modular exponentiation. While the
working register must be duplicated to allow for paral-
lelisation, the same input register can be reused for many
primes as it is only accessed by lookup operations. These
operations commute for different primes since they all use
only gates with controls on the input qubits. More pre-
cisely, given that a working register accesses the input
register in windows of w1 logical qubits at a time, pipelin-
ing these accesses can allow ⌈m/w1⌉registers to run in
parallel using a single input register. Therefore, the re-
quired number of logical qubits is

N =

ρ
⌈m/w1⌉


m + ρNw.
(15)

Noting that
l
ρ
⌈m/w1⌉
m
= 1 for ρ ≲200 and m is an or-
der of magnitude larger than Nw, this can be significantly
smaller than ρN1 = ρ(m + Nw) (where N1 is the num-
ber of logical qubits required for Gidney’s algorithm). This
leads to significant spacetime savings from parallelisation,
as shown in Fig. 7.

15

FIG. 7. Comparison of space, time and spacetime cost for our
parallelised algorithm to Gidney’s algorithm or Ref. [8]. For the
purpose of this plot, all algorithmic parameters (other than ρ)
are chosen to match those of the n = 2048 row of Table 5 of
Ref. [8].

Our modified algorithm allows for very efficient paral-
lelism, with orders of magnitude reductions in the time
overhead achievable with a smaller increase in the space
overhead. In particular, we note that while Gidney’s algo-
rithm has a longer runtime than the earlier implementa-
tion of Gidney and Eker˚a [7], our parallelised version can
achieve a significantly faster runtime. This motivates our
choice of this algorithm even for architectures with slow
clock cycles, where runtime is especially important.

2.
Implementation on Pinnacle Architecture

To implement the algorithm on the Pinnacle Architec-
ture, we begin by allocating a processing unit for each
working register. Recall that the working registers act en-
tirely independently for the entire duration of the modu-
lar exponentiations; they only interact at end when their
accumulators are combined. This means that the process-
ing units can run in parallel throughout the modular ex-
ponentiations, and then be joined pairwise as the parallel
reduction is implemented. Since the joining happens at
the end of the algorithm, it is not necessary to ever per-
form Clifford frame cleaning to separate the units again.
Each of these working registers is equipped with
enough logical qubits to allow implementation of Gid-
ney’s algorithm. This corresponds to: an f logical qubit
sub-register for the overall accumulator; an ℓ+ len(m)
logical qubit sub-register on which discrete-log values are
accumulated for each prime; two ancillary sub-registers
each with max
f, ℓ+ len(m)

logical qubits; a third an-
cillary sub-register with ℓlogical qubits; and one addi-
tional ancillary logical qubit for compiling Toffoli gates
from T gates using the circuit of Ref. [56]. As in Ref. [8],

## Page 16

f is the length of the truncated accumulator, ℓis the bit
length of the residue primes and len(m) = ⌊log2(m)⌋+1
is the bit length of m. We therefore require κ logical
qubits, given by

κ = f + 2ℓ+ len(m) + 2 max(f, ℓ+ len(m)) + 1. (16)

To achieve this, we allocate ⌈κ/k⌉processing blocks to
each processing unit, where k is the number of logical
qubits per code block.
The input register (or multiple input registers if ρ ≥
⌈m/w1⌉) is associated with memory in the architecture.
Access to this memory occurs during loop 1 of Gidney’s
algorithm, when windows of w1 logical qubits are used
as the address for a lookup operation targeted on each
working register. As discussed in Section V B 3, we fix
w1 = k/2, and we also enforce the condition that ℓ≥w1.
This ensures that there are at least w1 unused logical
qubits onto which the window can be fanned out, since
at the time of this loop, f +3ℓ+3 len(m) logical qubits of
each working register are in use, meaning that there are
at least ℓunused logical qubits.
Otherwise, we follow the decomposition into addition,
lookup and phaseup subroutines and implementation of
these subroutines presented in Ref. [8].

3.
Resource Analysis

a.
Physical Qubits:
We now determine the number
of physical qubits required. Each working register corre-
sponds to a processing unit with κ(f, ℓ, m) logical qubits,
as given in Eq. (16), along with a magic engine. The num-
ber of physical qubits required for the ρ working registers
is therefore

!

κ(f, ℓ, m)


+ nme

.
(17)

nw = ρ

npb

k

Each memory stores m logical qubits and there are
l
ρ
⌈m/w1⌉
m
such memories. Each memory requires ν =

m/k

code blocks of an Jn, k, dK code (with 2n physical
qubits each). For each processing unit, we also require a
port with ng + nb additional physical qubits. The number
of physical qubits required for the memory and ports is
therefore

nm = 2n

ρ
⌈m/w1⌉

 m


+ ρ(ng + nb).
(18)

k

Hence the total number of physical qubits is ntotal = nw+
nm.
b.
Runtime:
We define the total number of logical
cycles required per iteration of the outer loop of Gidney’s
algorithm to be Σ, which is equal to the sum of the final
column of Table V. Since we require

|P|/ρ

iterations,
this implies that the expected number of logical cycles re-
quired for the full outer loop is no more than

|P|/ρ

Σ.

16

Following the completion of this outer loop, we have some
further minor steps that are performed once. First, the
uncomputation of loop 1 [8]—which is performed in par-
allel on all streams—consists of a single instance of the
loop 1 lookup and addition. Referring to Table V, it takes
υ = ⌈m/w1⌉

6
2w1 −w1 + ℓ+ len(m) −2

+ 2w1


logical cycles. Second, the accumulators for the differ-
ent streams must be combined, which takes ⌈log2(ρ)⌉
layers of additions of f qubit registers and hence 6(f −
1)⌈log2(ρ)⌉logical cycles. Finally, there is a frequency
measurement (i.e. inverse quantum Fourier transform fol-
lowed by measurement); the nuber of logical cycles re-
quired for this is negligible compared to Σ so we follow
Ref. [8] in omitting it from our accounting. Assuming a
perfect success rate of magic engines we can therefore
write the total number of logical cycles as

|P|

!


Σ + υ + 6(f −1)⌈log2(ρ)⌉

T ′ =

.
(19)

ρ

The proportion of logical cycles requiring T states is ap-
proximately (in fact, slightly less than) 2/3, which leads to
an adjusted formula for the true number of logical cycles
accounting for the magic engine rejection rate of pr of

T =
2


T ′
(20)

3(1 −pr)−1 + 1

3

Then the total runtime per shot t = tlT is the product
of the number of logical cycles T and the time per logical
cycle tl = dttc.
The expected number of shots required for the factor-
ing, from Ref. [8], is given by

σ =
s + 1

,
(21)

s+2
2f+1sw1

0.99pS

where s is the Ekera-H˚astad parameter, and pS is the prob-
ability that a shot does not have a logical error, which is
given by

pS = (1 −pL)NT (1 −pT )τ ,
(22)

where pL is the logical error rate per logical qubit per log-
ical cycle, pT is the infidelity of output T states from the
magic engine, N and T are the total number of logical
qubits and logical cycles per shot and τ is the T count per
shot, which is given by

τ = |P|τ1 + 2

3υ + 4(f −1)⌈log2(ρ)⌉,
(23)

where τ1 is the T count per prime which is equal to the
sum of the T count column of Table V. Hence the expected
runtime for the factoring is ttotal = σt.

## Page 17

17

TABLE V. Time cost accounting for all subroutines required for each prime. Loop numbers refer to Gidney’s algorithm, as presented
in Ref. [8]. For lookups and phaseups, the size is the address size; for additions, it is the size of the registers being added. For addition
(loop 2) the size is the average over the loop, since it varies. The T Count column is the number of T gates required, which is four
times the Toffoli count. The Logical Cycles column is the total number of logical cycles, including both T state injections and other
logical measurements. Since each Toffoli gate requires four T gates and one logical measurement [56], and one additional logical
measurement is required for measurement-based uncompute, this is nearly always 3/2 times the T count. The only exception is
Lookup (Loop 1) which also requires additional logical measurements for Clifford frame cleaning.

4.
Results

We now consider the resources—both physical qubits
and time—required to factor an RSA-2048 integer on the
instantiation of the Pinnacle architecture presented in
Section V, given different hardware parameters, namely
the code cycle time and physical error rate. Following
Ref. [8], we expect the required logical error rate per logi-
cal qubit per logical cycle to be ≲10−14 (i.e., ≲10−15 per
code cycle). With reference to Table III, this motivates a
choice of the d = 24 GB code architecture for a physical
error rate of p = 10−3 and d = 16 for the p = 10−4 ar-
chitecture. The precise logical failure rate of the algorithm
varies somewhat as other parameters affect the number of
logical qubits and logical cycles; this effect is accounted
for in the number of shots, given in Eq. (21).
To determine the minimal required physical qubits and
runtime, we optimise over the algorithmic parameters of
Gidney’s algorithm with the following ranges:

• Eker˚a-H˚astad parameter, 1 ≤s ≤16;

• Accumulator truncation, 24 ≤f ≤59;

• Prime bit length, 18 ≤ℓ≤25;

• Loop 3 window size, 2 ≤w3 ≤6;

• Loop 4 window size, 2 ≤w4 ≤6.

We also optimise the parallelisation factor over the range
1 ≤ρ ≤|P|, where |P| ≈nm/ℓw1 is the num-
ber of primes in the residue system.
Recall that, un-
like in Ref. [8], we fix the loop 1 window size as w1 =
k/2.
Following Ref. [8], we also impose the feasibil-
ity condition that the number of primes of bit length ℓ,
π(ℓ) ≈2ℓ−1/ℓln(2), cannot be smaller than the number
of primes |P|. The results of this optimisation are shown
in Table VI and Fig. 3.
We find that fewer than one hundred thousand physical
qubits are required for factoring at a physical error rate of

TABLE VI. Minimum number of physical qubits required to com-
plete factoring in a range of expected runtimes for a range of
hardware parameters. Mq and kq represent megaqubits (i.e.,
×106 qubits) and kiloqubits (×103 qubits) respectively.

p = 10−3 in an expected runtime of one month. Alterna-
tively, with the same error rate and code cycle time, fac-
toring can be completed in one week with 151 thousand
physical qubits—compared to one million in Ref. [8]—or
in one day with 471 thousand physical qubits. With one
million physical qubits, factoring takes an expected time
of ten hours, compared with five days in Ref. [8].
We can also consider our results in regimes relevant to
other hardware platforms. For example, at a physical error
rate of p = 10−4—relevant to trapped ions [15]—the min-
imum number of physical qubits required for factoring is
53 thousand. For a typical trapped ion code cycle time of
1 ms [57], factoring with one million physical qubits takes
an expected time of approximately three months. Factor-
ing in a shorter time with these parameters is also possible
with a feasible number of physical qubits. For example,
factoring can be completed in one month with 3.1 million
physical qubits or in one week with 14 million physical
qubits. By comparison, adjusting the results of Ref. [8]
to such a code cycle time would give a prohibitively long
runtime, while Ref. [58] estimated a runtime of 3 years

## Page 18

with 8.6 million qubits for a surface code architecture with
trapped ion parameters.
Our results are also comparable to the results of
Ref. [16], which apply to a neutral atom platform with
physical error rate of p = 10−3 and a code cycle time of 1
ms. Specifically, with 19 million qubits we find a runtime
of 21 days, compared with the result of 5.6 days in Ref. [16]
The low runtime achieved by that work is achieved by us-
ing transversal gates with algorithmic fault tolerance to
reduce the logical cycle time to be equal to the code cycle
time, compared with dt = 26 code cycles on our archi-
tecture. Our architecture has the potential to support an
analogous reduction by incorporating fast surgery [59],
with the potential to achieve an order-of-magnitude lower
runtime or physical qubit number. We look forward to re-
alising this potential in future work.

VII.
CONCLUSION

We have presented the Pinnacle Architecture, which
leverages the high encoding rate of QLDPC codes to
achieve universal quantum computing with order-of-
magnitude overhead reductions compared with surface
code architectures.
In particular, we have shown that
factoring 2048-bit RSA integers, which requires close to
a million physical qubits using surface code architec-
tures [8], can be done with fewer than one hundred thou-
sand physical qubits on the Pinnacle Architecture. Given
the challenges posed in scaling from one hundred thou-
sand to one million physical qubits, such as the need on
many hardware platforms for networking between sep-
arated devices [9], this has the potential to significantly
hasten the onset of practical quantum computing.
Importantly, this is only the beginning of the story for
QLDPC architectures. While it has been suggested that re-
ducing the physical qubit count for 2048-bit RSA factoring
by an order of magnitude (i.e., to one hundred thousand
physical qubits) is implausible on surface code architec-
tures [8], the same cannot be said of QLDPC architectures.
Indeed, a range of higher rate QLDPC codes are known
than the generalised bicycle codes used here [18]. Incor-
porating such codes into the Pinnacle Architecture, com-
bined with further optimisation of its components, could
plausibly achieve such a reduction. As such, this work
serves not only as a major step forward in its own right,
but also a foundation on which we expect to make sub-
stantial further progress.

VIII.
ACKNOWLEDGEMENTS

We thank Stephen Bartlett and Kevin Obenland for
discussions, Calida Tang for organisational support, Fer-
nando Borretti for software engineering support, Max
McIsted for assistance with preparing the figures, and
Scott Aaronson for thoughtful feedback on the title.

18

Appendix A: Cost of Clifford Frame Cleaning

In this appendix, we show that Clifford frame cleaning
can be completed using the number of logical measure-
ments claimed in Section IV B 3. Specifically, we show that
it can be completed in the same number of Pauli π/4 ro-
tations, which we write as Rπ/4(P) for a Pauli rotation
axis P. Each such rotation can be implemented by a joint
logical Pauli measurement with a single logical ancilla in
the |¯0⟩state [6].
We present our proofs using the Pauli and Clifford
operator representation of Ref. [60]. Specifically, an n-
qubit Pauli operator is associated (uniquely, up to a global
phase) with an element v ∈Z2n
2
by the expression Pv =
Qn
i=1 Xvi
i Zvn+i
i
. In this formalism, PuPv = Pu+v. Com-
mutation relations are specified by the symplectic inner
product

⟨u, v⟩= uJvT ,
J =

0
In
In
0


,
(A1)

and u and v are treated as row vectors. Specifically, Pu and
Pv commute if ⟨u, v⟩= 0, and anti-commute if ⟨u, v⟩=
1. The symplectic complement W ⊥of subspace W is a
subspace whose elements commute with all elements in
W.
In the same formalism, an n-qubit Clifford operator
U can be represented by a 2n × 2n matrix MU that
preserves the symplectic inner product (i.e., such that
MUJM T
U
= J). The action of U on Pv by conjuga-
tion corresponds to matrix multiplication on the right (i.e.,
P 7→UPU † corresponds to v 7→vMU). The product
of two Clifford operators V U therefore corresponds to
the product of their matrix representations MUMV . A
Pauli π/4 rotation Rπ/4(Q) is a special type of Clifford
operator which is specified by an n-qubit Pauli operator
Q. It acts as Rπ/4(Q)PRπ/4(Q)† = PQ if P and Q
anti-commute, and as Rπ/4(Q)PRπ/4(Q)† = P if P and
Q commute. Therefore, Rπ/4(Pu) acts on v ∈Z2n
2
as
Eu(v) = v + ⟨u, v⟩u.
There are two cases of Clifford frame cleaning to con-
sider: the general case, where 4w steps are required to
clean off w qubits; and the case of cleaning a memory port,
where only 2w steps are required. We first consider the
general case.

Lemma 1.
Let U
be an n-qubit Clifford opera-
tor.
Then for w
≤
n, there exists a sequence
of
4w
Pauli
operators
P1, . . . , P4w
such
that
Rπ/4(P1)Rπ/4(P2) . . . Rπ/4(P4w)U
is a Clifford op-
erator supported only on the last n −w qubits.

Proof. We proceed by induction. Let





M (k) =



.
(A2)

## Page 19

We will show for 1 ≤k ≤w, given a matrix of the form
M (k−1), that there exists a product of four Pauli π/4 ro-
tations with matrices Eα1, Eα2, Eα3, and Eα4, such that
Eα4Eα3Eα2Eα1M (k−1) is of the form M (k). It follows
that U = M (0) can be mapped to an operator M (w) that
has support only on the last n −w qubits with 4w Pauli
π/4 rotations.
Let v(k) denote the kth row of M (k−1), ek denote
the kth vector in the standard symplectic basis and
fk = en+k, and let Ak−1 be the symplectic subspace
spanned by {e1, . . . ek−1, f1, . . . fk−1} corresponding to
the Pauli group on the first k −1 qubits. We will choose
α1, α2, α3, α4 ∈A⊥
k−1 to ensure that these operations act
as the identity on all a ∈Ak−1. We now consider two
cases, and in each choose α1, α2 such that they map v(k)

to ek.
First, if ⟨v(k), ek⟩= 1, let α1 = v(k) + ek and α2 = 0.
Then ⟨v(k), v(k) + ek⟩= 1, and so

Ev(k)+ek(v(k)) = ek.
(A3)

Second, if ⟨v(k), ek⟩= 0, then if ⟨v(k), fk⟩= 1 let uk =
fk, and if ⟨v(k), fk⟩= 0 let uk = fk + en+δ (mod 2n),
where δ > k is the position of the first nonzero element
of v(k). Moreover, let α1 = v(k) + uk and α2 = ek + uk.
Then ⟨v(k), v(k) + uk⟩= ⟨uk, ek + uk⟩= 1, and so

Eek+ukEv(k)+uk
v(k)
= Eek+uk(uk) = ek.
(A4)

Let ˜
M (k−1) = Eek+uEv(k)+u
M (k−1)
and the ith
row of ˜
M (k−1) be ˜v(i). As this preserves the symplec-
tic product, 1 = ⟨v(k), v(n+k)⟩= ⟨˜v(k), ˜v(n+k)⟩=
⟨ek, ˜v(n+k)⟩. We now consider two cases, and in each
choose α3, α4 such that they fix ek and map ˜v(n+k) to
fk.
First, if ⟨˜v(n+k), fk⟩= 1, let α3 = ˜v(n+k) + fk and
α4 = 0. Then ⟨˜v(n+k), ˜v(n+k) + fk⟩= 1, and so

E˜v(n+k)+fk(˜v(n+k)) = fk.
(A5)

We also have ⟨ek, ˜v(n+k) + fk⟩= 0, which implies that
E˜v(n+k)+fk(ek) = ek.
Second, if ⟨˜v(n+k), fk⟩= 0, let α3 = ˜v(n+k) + ek + fk
and α4 = ek. Then ⟨˜v(n+k), ˜v(n+k) + ek + fk⟩= 1, and
so

EekE˜v(n+k)+ek+fk(˜v(n+k)) = Eek(ek + fk) = fk. (A6)

We also have ⟨ek, ˜v(n+k) + ek + fk⟩= 0, which implies
that EekE˜v(n+k)+ek+fk(ek) = ek.
Hence in all cases

M (k) = Eα4Eα3Eα2Eα1M (k−1),
(A7)

which completes the proof.

Now we consider the specific case of cleaning a mem-
ory port.
Lemma 2. Let U be an n-qubit Clifford operator that is
a product of Clifford operators that act either trivially or
as the control of a CNOT on the first w ≤n qubits. Then

19

there exists a sequence of 2w Pauli operators P1, . . . , P2w
such that Rπ/4(P1)Rπ/4(P2) . . . Rπ/4(P2w)U is a Clif-
ford operator supported only on the last n −w qubits.

Proof. Since CNOTs commute with Z operators on their
control qubits, U must commute with all Z-type opera-
tors with support on the first w qubits. Consequently, the
matrix representation of U has the form







.
(A8)

U =

We proceed by induction, analogously to the proof of
Lemma 1. Let









M (k) =

.
(A9)

We will show for 1 ≤k ≤w, given a matrix of the
form M (k−1), that there exists a product of two Pauli
π/4 rotations with matrices Eα1 and Eα2, such that
Eα2Eα1M (k−1) is of the form M (k). It follows that U =
M (0) can be mapped to an operator M (w) that has support
only on the last n−w qubits with 2w Pauli π/4 rotations.
Let v(k) denote the kth row of M (k−1), ek denote the
kth vector in the standard symplectic basis and fk =
en+k, and let Ak−1 be the symplectic subspace spanned
by {e1, . . . ek−1, f1, . . . fk−1} corresponding to the Pauli
group on the first k −1 qubits. We will choose α1, α2 ∈
A⊥
k−1 to ensure that these operations act as the identity on
all a ∈Ak−1, and such that they also fix fj for k ≤j ≤w
and map v(k) to ek. We now consider two cases, noting
that the structure of M (k−1) implies that ⟨v(k), fj⟩= δjk
for 1 ≤j ≤w.
First, if ⟨v(k), ek⟩= 1, let α1 = v(k) + ek and α2 = 0.
Then ⟨v(k), v(k) + ek⟩= 1, and so

Ev(k)+ek
v(k)
= ek.
(A10)

We also have ⟨fj, v(k) + ek⟩= 2δjk = 0 for k ≤j ≤w,
which implies that Ev(k)+ek(fj) = fj.
Second, if ⟨v(k), ek⟩= 0, let α1 = v(k) + ek + fk and
α2 = fk. Then ⟨v(k), v(k) + ek + fk⟩= 1, and so

EfkEv(k)+ek+fk
v(k)
= Efk(ek + fk) = ek.
(A11)

We also have ⟨fj, v(k) + ek⟩= 2δjk = 0 for k ≤j ≤w,
which implies that EfkEv(k)+ek+fk(fj) = fj.
Hence in all cases

M (k) = Eα2Eα1M (k−1),
(A12)

which completes the proof.

## Page 20

20

[1] P. Shor, Algorithms for quantum computation: Discrete
logarithms and factoring, in Proceedings 35th Annual Sym-
posium on Foundations of Computer Science (1994) pp. 124–
134.
[2] S. Lloyd, Universal quantum simulators, Science 273, 1073
(1996).
[3] D. Gottesman, Opportunities and challenges in fault-
tolerant
quantum
computation,
Preprint
(2022),
arXiv:2210.15844.
[4] A. G. Fowler, M. Mariantoni, J. M. Martinis, and A. N. Cle-
land, Surface codes: Towards practical large-scale quan-
tum computation, Physical Review A 86, 032324 (2012),
arXiv:1208.0928.
[5] D. Horsman, A. G. Fowler, S. Devitt, and R. V. Meter, Surface
code quantum computing by lattice surgery, New Journal
of Physics 14, 123011 (2012), arXiv:1111.4022.
[6] D. Litinski, A game of surface codes: Large-scale quan-
tum computing with lattice surgery, Quantum 3, 128 (2019),
arXiv:1808.02892.
[7] C. Gidney and M. Eker˚a, How to factor 2048 bit RSA inte-
gers in 8 hours using 20 million noisy qubits, Quantum 5,
433 (2021), arXiv:1905.09749.
[8] C. Gidney, How to factor 2048 bit RSA integers with
less than a million noisy qubits, Preprint
(2025),
arXiv:2505.15917.
[9] M. Mohseni, A. Scherer, K. G. Johnson, O. Wertheim, M. Ot-
ten, N. A. Aadit, Y. Alexeev, K. M. Bresniker, K. Y. Cam-
sari, B. Chapman, S. Chatterjee, G. A. Dagnew, A. Espos-
ito, F. Fahim, M. Fiorentino, A. Gajjar, A. Khalid, X. Kong,
B. Kulchytskyy, E. Kyoseva, R. Li, P. A. Lott, I. L. Markov,
R. F. McDermott, G. Pedretti, P. Rao, E. Rieffel, A. Silva,
J. Sorebo, P. Spentzouris, Z. Steiner, B. Torosov, D. Ven-
turelli, R. J. Visser, Z. Webb, X. Zhan, Y. Cohen, P. Ronagh,
A. Ho, R. G. Beausoleil, and J. M. Martinis, How to build
a quantum supercomputer: Scaling from hundreds to mil-
lions of qubits, Preprint (2025), arXiv:2411.10406.
[10] T. J. Yoder, E. Schoute, P. Rall, E. Pritchett, J. M. Gambetta,
A. W. Cross, M. Carroll, and M. E. Beverland, Tour de gross:
A modular quantum computer based on bivariate bicycle
codes, Preprint (2025), arXiv:2506.03094.
[11] P. Webster, S. C. Smith, and L. Z. Cohen, Explicit construc-
tion of low-overhead gadgets for gates on quantum LDPC
codes, Preprint (2025), arXiv:2511.15989.
[12] I. D. Kivlichan, C. Gidney, D. W. Berry, N. Wiebe,
J. McClean, W. Sun, Z. Jiang, N. Rubin, A. Fowler,
A. Aspuru-Guzik, H. Neven, and R. Babbush, Improved
fault-tolerant quantum simulation of condensed-phase cor-
related electrons via Trotterization, Quantum 4, 296 (2020),
arXiv:1902.10673.
[13] S. Bravyi, G. Smith, and J. Smolin, Trading classical and
quantum computational resources, Physical Review X 6,
021043 (2016), arXiv:1506.01396.
[14] E. T. Campbell, Early fault-tolerant simulations of the Hub-
bard model, Quantum Science and Technology 7, 015007
(2022), arXiv:2012.09238.
[15] A. C. Hughes, R. Srinivas, C. M. L¨oschnauer, H. M. Knaack,
R. Matt, C. J. Ballance, M. Malinowski, T. P. Harty, and R. T.
Sutherland, Trapped-ion two-qubit gates with >99.99%
fidelity without ground-state cooling, Preprint
(2025),
arXiv:2510.17286.

[16] H. Zhou, C. Duckering, C. Zhao, D. Bluvstein, M. Cain,
A. Kubica, S.-T. Wang, and M. D. Lukin, Resource analy-
sis of low-overhead transversal architectures for reconfig-
urable atom arrays, in Proceedings of the 52nd Annual In-
ternational Symposium on Computer Architecture (2025) pp.
1432–1448, arXiv:2505.15907.
[17] D. J. C. MacKay, G. Mitchison, and P. L. McFadden, Sparse
graph codes for quantum error-correction, IEEE Transac-
tions on Information Theory 50, 2315 (2004), arXiv:quant-
ph/0304161.
[18] N. P. Breuckmann and J. N. Eberhardt, Quantum low-
density parity-check codes, PRX Quantum 2, 040101 (2021),
arXiv:2103.06309.
[19] J. Yoneda, W. Huang, M. Feng, C. H. Yang, K. W. Chan,
T. Tanttu, W. Gilbert, R. C. C. Leon, F. E. Hudson, K. M.
Itoh, A. Morello, S. D. Bartlett, A. Laucht, A. Saraiva, and
A. S. Dzurak, Coherent spin qubit transport in silicon, Na-
ture Communications 12, 4114 (2021), arXiv:2008.04020.
[20] M. Malinowski, D. T. C. Allcock, and C. J. Ballance, How
to wire a 1000-qubit trapped ion quantum computer, PRX
Quantum 4, 040313 (2023), arXiv:2305.12773.
[21] D. Bluvstein, H. Levine, G. Semeghini, T. T. Wang, S. Ebadi,
M. Kalinowski, A. Keesling, N. Maskara, H. Pichler,
M. Greiner, V. Vuletic, and M. D. Lukin, A quantum proces-
sor based on coherent transport of entangled atom arrays,
Nature 604, 451 (2022), arXiv:2112.03923.
[22] H. Bombin, I. H. Kim, D. Litinski, N. Nickerson, M. Pant,
F. Pastawski, S. Roberts, and T. Rudolph, Interleaving:
Modular architectures for fault-tolerant photonic quantum
computing, Preprint (2021), arXiv:2103.08612.
[23] S. Bravyi, A. W. Cross, J. M. Gambetta, D. Maslov,
P. Rall, and T. J. Yoder, High-threshold and low-overhead
fault-tolerant quantum memory, Nature 627, 778 (2024),
arXiv:2308.07915.
[24] L. Z. Cohen, I. H. Kim, S. D. Bartlett, and B. J. Brown, Low-
overhead fault-tolerant quantum computing using long-
range connectivity, Science Advances 8, eabn1717 (2022),
arXiv:2110.10794.
[25] D. J. Williamson and T. J. Yoder, Low-overhead fault-
tolerant quantum computation by gauging logical opera-
tors, Preprint (2024), arXiv:2410.02213.
[26] B. Ide, M. G. Gowda, P. J. Nadkarni, and G. Dauphi-
nais, Fault-tolerant logical measurements via homologi-
cal measurement, Physical Review X 15, 021088 (2025),
arXiv:2410.02753.
[27] Following Refs [6, 10], we assume that the time required
between logical measurements is negligible compared with
the timescale of a logical cycle.
[28] A. W. Cross, Z. He, P. J. Rall, and T. J. Yoder, Im-
proved QLDPC surgery: Logical measurements and bridg-
ing codes, Preprint (2025), arXiv:2407.18393.
[29] E. Swaroop, T. Jochym-O’Connor, and T. J. Yoder, Universal
adapters between quantum LDPC codes, Preprint (2025),
arXiv:2410.03628.
[30] R. Acharya, L. Aghababaie-Beni, I. Aleiner, T. I. Ander-
sen, M. Ansmann, F. Arute, K. Arya, A. Asfaw, N. As-
trakhantsev, J. Atalaya, R. Babbush, D. Bacon, B. Ballard,
J. C. Bardin, J. Bausch, A. Bengtsson, A. Bilmes, S. Black-
well, S. Boixo, G. Bortoli, A. Bourassa, J. Bovaird, L. Brill,
M. Broughton, D. A. Browne, B. Buchea, B. B. Buckley,

## Page 21

21

D. A. Buell, T. Burger, B. Burkett, N. Bushnell, A. Cabr-
era, J. Campero, H.-S. Chang, Y. Chen, Z. Chen, B. Chiaro,
D. Chik, C. Chou, J. Claes, A. Y. Cleland, J. Cogan, R. Collins,
P. Conner, W. Courtney, A. L. Crook, B. Curtin, S. Das,
A. Davies, L. D. Lorenzo, D. M. Debroy, S. Demura, M. De-
voret, A. D. Paolo, P. Donohoe, I. Drozdov, A. Dunsworth,
C. Earle, T. Edlich, A. Eickbusch, A. M. Elbag, M. Elzouka,
C. Erickson, L. Faoro, E. Farhi, V. S. Ferreira, L. F. Bur-
gos, E. Forati, A. G. Fowler, B. Foxen, S. Ganjam, G. Gar-
cia, R. Gasca, ´E. Genois, W. Giang, C. Gidney, D. Gilboa,
R. Gosula, A. G. Dau, D. Graumann, A. Greene, J. A. Gross,
S. Habegger, J. Hall, M. C. Hamilton, M. Hansen, M. P. Har-
rigan, S. D. Harrington, F. J. H. Heras, S. Heslin, P. Heu,
O. Higgott, G. Hill, J. Hilton, G. Holland, S. Hong, H.-Y.
Huang, A. Huff, W. J. Huggins, L. B. Ioffe, S. V. Isakov,
J. Iveland, E. Jeffrey, Z. Jiang, C. Jones, S. Jordan, C. Joshi,
P. Juhas, D. Kafri, H. Kang, A. H. Karamlou, K. Kechedzhi,
J. Kelly, T. Khaire, T. Khattar, M. Khezri, S. Kim, P. V.
Klimov, A. R. Klots, B. Kobrin, P. Kohli, A. N. Korotkov,
F. Kostritsa, R. Kothari, B. Kozlovskii, J. M. Kreikebaum,
V. D. Kurilovich, N. Lacroix, D. Landhuis, T. Lange-Dei,
B. W. Langley, P. Laptev, K.-M. Lau, L. L. Guevel, J. Ledford,
K. Lee, Y. D. Lensky, S. Leon, B. J. Lester, W. Y. Li, Y. Li,
A. T. Lill, W. Liu, W. P. Livingston, A. Locharla, E. Lucero,
D. Lundahl, A. Lunt, S. Madhuk, F. D. Malone, A. Mal-
oney, S. Mandr´a, L. S. Martin, S. Martin, O. Martin, C. Max-
field, J. R. McClean, M. McEwen, S. Meeks, A. Megrant,
X. Mi, K. C. Miao, A. Mieszala, R. Molavi, S. Molina,
S. Montazeri, A. Morvan, R. Movassagh, W. Mruczkiewicz,
O. Naaman, M. Neeley, C. Neill, A. Nersisyan, H. Neven,
M. Newman, J. H. Ng, A. Nguyen, M. Nguyen, C.-H. Ni,
T. E. O’Brien, W. D. Oliver, A. Opremcak, K. Ottosson,
A. Petukhov, A. Pizzuto, J. Platt, R. Potter, O. Pritchard,
L. P. Pryadko, C. Quintana, G. Ramachandran, M. J. Reagor,
D. M. Rhodes, G. Roberts, E. Rosenberg, E. Rosenfeld,
P. Roushan, N. C. Rubin, N. Saei, D. Sank, K. Sankarago-
mathi, K. J. Satzinger, H. F. Schurkus, C. Schuster, A. W. Se-
nior, M. J. Shearn, A. Shorter, N. Shutty, V. Shvarts, S. Singh,
V. Sivak, J. Skruzny, S. Small, V. Smelyanskiy, W. C. Smith,
R. D. Somma, S. Springer, G. Sterling, D. Strain, J. Suchard,
A. Szasz, A. Sztein, D. Thor, A. Torres, M. M. Torunbalci,
A. Vaishnav, J. Vargas, S. Vdovichev, G. Vidal, B. Villalonga,
C. V. Heidweiller, S. Waltman, S. X. Wang, B. Ware, K. We-
ber, T. White, K. Wong, B. W. K. Woo, C. Xing, Z. J. Yao,
P. Yeh, B. Ying, J. Yoo, N. Yosri, G. Young, A. Zalcman,
Y. Zhang, N. Zhu, and N. Zobrist, Quantum error correction
below the surface code threshold, Nature 638, 920 (2025),
arXiv:2408.13687.
[31] D. Pataki and A. P´alyi, Compiling the surface code to cross-
bar spin qubit architectures, Physical Review B 111, 115307
(2025), arXiv:2412.05425.
[32] H. Leone, T. Le, S. Srikara, and S. Devitt, Resource
overheads and attainable rates for trapped-ion lattice
surgery, Physical Review Research 7, 023088 (2025),
arXiv:2406.18764.
[33] R. Babbush, C. Gidney, D. W. Berry, N. Wiebe, J. McClean,
A. Paler, A. Fowler, and H. Neven, Encoding electronic
spectra in quantum circuits with linear T complexity, Phys-
ical Review X 8, 041015 (2018), arXiv:1805.03662.
[34] Z. He, A. Cowtan, D. J. Williamson, and T. J. Yoder, Extrac-
tors: QLDPC architectures for efficient Pauli-based compu-
tation, Preprint (2025), arXiv:2503.10390.
[35] D. Filippov, P. Yang, and P. Murali, Architecting distributed

quantum computers: Design insights from resource esti-
mation, Preprint (2025), arXiv:2508.19160.
[36] A. A. Kovalev and L. P. Pryadko, Quantum Kronecker sum-
product low-density parity-check codes with finite rate,
Physical Review A 88, 012311 (2013), arXiv:1212.6703.
[37] H.-K. Lin, X. Liu, P. K. Lim, and L. P. Pryadko, Single-
shot and two-shot decoding with generalized bicycle codes,
Preprint (2025), arXiv:2502.19406.
[38] F. J. MacWilliams and N. J. A. Sloane, The Theory of
Error-Correcting Codes, North-Holland Mathematical Li-
brary, Vol. 16 (Elsevier, 1977).
[39] A. Cowtan, Z. He, D. J. Williamson, and T. J. Yoder, Par-
allel Logical Measurements via Quantum Code Surgery,
Preprint (2026), arXiv:2503.05003.
[40] S. Bravyi and A. Kitaev, Universal quantum computation
with ideal Clifford gates and noisy ancillas, Physical Re-
view A 71, 022316 (2005), arXiv:quant-ph/0403025.
[41] D. Litinski, Magic state distillation: Not as costly as you
think, Quantum 3, 205 (2019), arXiv:1905.06903.
[42] J. Zhang, Y.-C. Wu, and G.-P. Guo, Facilitating practi-
cal fault-tolerant quantum computing based on color
codes,
Physical
Review
Research
6,
033086
(2024),
arXiv:2309.05222.
[43] H. Goto, Minimizing resource overheads for fault-tolerant
preparation of encoded states of the Steane code, Scientific
Reports 6, 19578 (2016).
[44] T. Itogawa, Y. Takada, Y. Hirano, and K. Fujii, Effi-
cient magic state distillation by zero-level distillation, PRX
Quantum 6, 020356 (2025), arXiv:2403.03991.
[45] C. Gidney, N. Shutty, and C. Jones, Magic state cultivation:
Growing T states as cheap as CNOT gates, Preprint (2024),
arXiv:2409.17595.
[46] K. Sahay, P.-K. Tsai, K. Chang, Q. Su, T. B. Smith, S. Singh,
and S. Puri, Fold-transversal surface code cultivation,
Preprint (2025), arXiv:2509.05212.
[47] S.-H. Lee, A. Li, and S. D. Bartlett, Color code decoder with
improved scaling for correcting circuit-level noise, Quan-
tum 9, 1609 (2025), arXiv:2404.07482.
[48] In determining the required value of r, we upper bound the
logical error rate for a logical measurement with r < dt
rounds by (pL)
r
dt , where pL is the logical error rate for
dt rounds presented in Table III, which is equivalent to the
worst-case assumption that all errors contributing to pL are
time-like.
[49] A. R. O’Rourke and S. Devitt, Compare the pair:
Ro-
tated versus unrotated surface codes at equal logical er-
ror rates, Physical Review Research 7, 033074 (2025),
arXiv:2409.14765.
[50] S. Vittal, A. Javadi-Abhari, A. W. Cross, L. S. Bishop, and
M. Qureshi, Flag-proxy networks: Overcoming the archi-
tectural, scheduling and decoding obstacles of quantum
LDPC codes, in 2024 57th IEEE/ACM International Sym-
posium on Microarchitecture (MICRO) (2024) pp. 718–734,
arXiv:2409.14283.
[51] N. Raveendran and B. Vasi´c, Trapping sets of quantum
LDPC codes, Quantum 5, 562 (2021), arXiv:2012.15297.
[52] A. Paetznick and K. M. Svore, Repeat-until-success: Non-
deterministic decomposition of single-qubit unitaries,
Quantum Information and Computation 14, 1277 (2014),
arXiv:1311.1074.
[53] A. Bocharov, M. Roetteler, and K. M. Svore, Efficient synthe-
sis of universal repeat-until-success circuits, Physical Re-
view Letters 114, 080502 (2015), arXiv:1404.5320.

## Page 22

22

[54] M. Eker˚a and J. H˚astad, Quantum algorithms for comput-
ing short discrete logarithms and factoring RSA integers,
in Post-Quantum Cryptography, Vol. 10346 (Springer
International
Publishing,
Cham,
2017)
pp.
347–363,
arXiv:1702.00249.
[55] C. Chevignard, P.-A. Fouque, and A. Schrottenloher, Re-
ducing the number of qubits in quantum factoring, in Ad-
vances in Cryptology – CRYPTO 2025, edited by Y. Tau-
man Kalai and S. F. Kamara (Springer Nature Switzerland,
Cham, 2025) pp. 384–415.
[56] C. Jones, Low-overhead constructions for the fault-
tolerant Toffoli gate, Physical Review A 87, 022328 (2013),

arXiv:1212.5069.
[57] D. Litinski, How to compute a 256-bit elliptic curve pri-
vate key with only 50 million Toffoli gates, Preprint (2023),
arXiv:2306.08585.
[58] M. E. Beverland, P. Murali, M. Troyer, K. M. Svore, T. Hoe-
fler, V. Kliuchnikov, G. H. Low, M. Soeken, A. Sundaram,
and A. Vaschillo, Assessing requirements to scale to practi-
cal quantum advantage, Preprint (2022), arXiv:2211.07629.
[59] N. Baspin, L. Berent, and L. Z. Cohen, Fast surgery for quan-
tum LDPC codes, Preprint (2025), arXiv:2510.04521.
[60] S. Aaronson and D. Gottesman, Improved simulation of
stabilizer circuits, Physical Review A 70, 052328 (2004),
arXiv:quant-ph/0406196.
