---
source_pdf: ../arxiv_1703.00622.pdf
pages: 5
extracted_at: 2026-04-17T12:32:30+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_1703.00622

Source PDF: ../arxiv_1703.00622.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

The pitfalls of planar spin-glass benchmarks: Raising the bar for quantum annealers (again)

Salvatore Mandr`a,1, 2, ∗Helmut G. Katzgraber,3, 4, 5, † and Creighton Thomas6, ‡

1Quantum Artiﬁcial Intelligence Lab., NASA Ames Research Center, Moffett Field, CA 94035, USA
2Stinger and Ghaffarian Technologies, 7701 Greenbelt Road, Suite 400 Greenbelt, MD 20770, USA
3Department of Physics and Astronomy, Texas A&M University, College Station, Texas 77843-4242, USA
41QB Information Technologies (1QBit), Vancouver, British Columbia, Canada V6B 4W4
5Santa Fe Institute, 1399 Hyde Park Road, Santa Fe, New Mexico 87501 USA
6Google Inc., 111 8th Avenue New York, NY 10011, USA
(Dated: July 24, 2017)

In an effort to overcome the limitations of random spin-glass benchmarks for quantum annealers, focus has
shifted to carefully-crafted gadget-based problems whose logical structure has typically a planar topology. Recent
experiments on these gadget problems using a commercially-available quantum annealer have demonstrated an
impressive performance over a selection of commonly-used classical optimization heuristics. Here we show
that efﬁcient classical optimization techniques, such as minimum-weight perfect matching, can solve these
gadget problems exactly and in polynomial time. We present approaches on how to mitigate this shortcoming of
commonly-used benchmark problems based on planar logical topologies.

arXiv:1703.00622v2 [quant-ph] 21 Jul 2017

PACS numbers: 75.50.Lk, 75.40.Mg, 05.50.+q, 03.67.Lx

in an embedding overhead that results in logical problems with
less sites than the native topology of the chip. As such, it is
desirable to ﬁnd classes of problems for benchmarking that
ideally use the complete set of variables on the chip, while not
being a trivial optimization problem [1].

I.
INTRODUCTION

The quest for quantum speedup using analog quantum an-
nealing machines with a transverse ﬁeld remains elusive. There
have been multiple attempts [1–5] to demonstrate that the D-
Wave Systems Inc. quantum annealers can outperform classical
optimization methods. Unfortunately, it has been relatively
straightforward for classical optimization algorithms to stay
ahead in this race [6]. Either the random spin-glass benchmark
problems were too easy on the quasi-planar topology of the
D-Wave quantum annealer [1, 3, 7], or the logical structure of
carefully-crafted problems designed to give the annealer an
advantage have a trivial structure [5].
The notable advances made by D-Wave Systems Inc. in
the development of medium-scale quantum annealing tech-
nologies has inspired multiple corporations (e.g., Microsoft,
Google, and IBM) to further invest in quantum comput-
ing, in addition to large-scale government-funded projects.
The D-Wave 2000Q device is a special-purpose quantum opti-
mization machine specialized in minimizing quadratic uncon-
strained binary cost functions by means of quenching quantum
ﬂuctuations induced by a transverse ﬁeld. The generic cost
function to be minimized is given by

There have been multiple approaches to harden the bench-
mark problems to be solved on different generations of the
D-Wave device, ranging from post-selection methods based on
statistical-physics metrics [3] to planting of solutions [9] and
the engineering of problems based on the classical algorithmic
complexity of the Hamze–de Freitas–Selby [10, 11] algorithm
[12]. Although these approaches generated harder problems
for different generations of the D-Wave devices and there were
some suggestions that there is some level of “quantumness”
in the device [3], only studies tailored to explicitly demon-
strate quantumness, as well as attempt to determine (quantum)
speedup [1, 6] pushed the ﬁeld forward noticeably. Both the
studies of Denchev et al. [5] and King et al.[13] focused on
the generation of logical problems designed to elucidate the
value of quantum ﬂuctuations, as well as to “fool” archetypal
classical optimization algorithms (e.g., simulated annealing
[14], the classical pendant to quantum annealing [15, 16]) to
become stuck in the carefully-designed energy landscape of the
problems. In Ref. [6] it was subsequently shown that the use
of state-of-the-art optimization techniques beyond simulated
annealing for the benchmarks designed in Ref. [5] resulted in
time-to-solutions scaling considerably better than the D-Wave
device, as well as simulated quantum annealing. In this work
we demonstrate that if the logical problems to be optimized on
the D-Wave device have a planar structure, a quantum annealer
would have to scale polynomially in the number of (logical)
variables (i.e., be exponentially faster) to compete with the
current classical state-of-the-art for frustrated problems on pla-
nar topologies, such as the minimum-weight perfect-matching
(MWPM) exact algorithm [17, 18]. We emphasize that both the
benchmark instances designed by Denchev et al. [5] and King
et al.[13] suffer from the same problem. Namely, they can both
be solved in polynomial time. Although one could, in principle,

n
X

n
X

HP =

i=1
Jijσiσj +

i=1
hiσi,
(1)

where the n variables σi ∈{±1} are Boolean and the cou-
plings Jij ∈R and biases hi ∈R are the parameters that
deﬁne the problem to be minimized. In the case of the D-Wave
chip, these variables are arranged in the so-called Chimera
topology [8]. Real-world applications then require the embed-
ding of the problems onto this topology, thus typically resulting

∗Electronic address: salvatore.mandra@nasa.gov
†Electronic address: hgk@tamu.edu
‡Electronic address: creightonthomas@gmail.com

## Page 2

compare the quantum annealer against fast heuristics such as
the Hamze–de Freitas–Selby [10, 11] algorithm [12] or parallel
tempering Monte Carlo with isoenergetic cluster moves [19],
if claims of speedups over many orders of magnitude against
classical algorithms are made, then the true state-of-the-art for
planar topologies should be included in the study.
Although one might argue that exploiting the logical struc-
ture of the problem could be seen as “cheating,” combining
MWPM techniques with simple cluster-ﬁnding and/or decima-
tion techniques that are also polynomial in the size of the input
would still scale exponentially faster than the D-Wave device.
However, there would be no more guarantee for an exact result
and the cluster-detecting MWPM algorithm could, at best, be
seen as a heuristic that scales polynomial in the size of the
input.
The paper is structured as follows. In Section II we describe
the crafted benchmark problem designed by D-Wave Systems
Inc. [13] and in Section III we describe the classical algorithms
and methods we used in our analysis of these problems. Results
are summarized in Section IV, followed by a discussion that
also includes different strategies to design problems on quan-
tum annealing machines that might have potential for quantum
speedup and cannot be solved with polynomial algorithms for
planar technologies.

II.
D-WAVE’S CRAFTED PROBLEMS

Given its hardware limitations, not all possible couplings
{Jij} between two arbitrary qubits i and j can be set in the
D-Wave quantum annealer. Indeed, only those couplings be-
longing to the native Chimera topology can be independently
tuned within the range [−1, +1], while the remaining are set
to zero. The Chimera topology [8] is composed of k × k unit
cells, each containing a K4,4 fully-connected bipartite graph
of 8 qubits. The unit cells are coupled together so that only
adjacent unit cells share couplings. Despite the somewhat
restrictive structure of the lattice, it can be shown that, in prin-
ciple, any topology can be embedded, albeit at the cost of using
multiple physical variables to deﬁne a logical variable.
In Ref. [13], the latest incarnation of the quantum annealer,
namely the D-Wave 2000Q with over 2000 quantum bits, is
tested using a set of carefully crafted optimization problems
also referred to as the “frustrated cluster loop” (FCL) problems.
One of the main characteristics which makes the FCL problems
appealing for benchmarking is that many classical heuristics
struggle with minimizing the value of the cost function, even
though the optimal conﬁguration can be deduced by exploiting
the actual structure of the problem [9, 13].
Although the FCL problems can, in principle, be directly
generated for the Chimera topology [9], the D-Wave Systems
Inc. group has chosen a slightly different strategy, divided
into two steps, which assists in elucidating the effects of the
landscape ruggedness:

1. All couplings inside a K4,4 unit cell are set to be ferro-
magnetic, i.e., Jij = −1, ∀i, j ∈K4,4 . because the unit
cells are fully connected, all the “physical” qubits within
a single cell are forced to behave as a single “logical”

qubit. This process generates a two-dimensional lattice
with open boundary conditions of these logical variables.

2. The FCL instances are then generated on the logical
topology with a varying level of ruggedness of the energy
landscape and parameters α (clause-to-variable ratio)
and ρ (precision), as deﬁned in Ref. [20]. Note that for
the ruggedness R we expect R ≥ρ.

This local ruggedness R then makes the problems hard to
treat for typical classical optimization techniques with the
interactions for the logical qubits being in the range [−R, +R].
Disconnected graphs are discarded in the study.
It is important to stress that, despite the fact that
D-Wave 2000Q can optimize problems on the Chimera topol-
ogy, the benchmark problems used in Ref. [13] are deﬁned
on the logical topology of the machine, namely on a two-
dimensional lattice with open boundaries. Therefore, a fair
comparison requires that the D-Wave 2000Q benchmarking
be performed against heuristics which are optimized for the
logical problem, rather than on the Chimera topology. It is
noteworthy, however, that the D-Wave 2000Q solves problems
on the full Chimera lattice, i.e., the machine seems to be able
to efﬁciently overcome local energy barriers.

III.
METHODS

In this Section, we brieﬂy outline the algorithms used, as
well as the deﬁnition of time-to-solution used in the bench-
marks. Reference [19] provides the necessary details for the
isoenergetic cluster move (ICM) heuristic.

A.
Minimum-weight perfect matching algorithm

The minimum-weight perfect matching (MWPM) algorithm
is an exact classical algorithm designed to ﬁnd optimal conﬁgu-
rations for planar two-dimensional spin-glass-like optimization
problems without biases (i.e., hi = 0, ∀i ∈n). The algorithm
is polynomial in the size of the input n. The MWPM algorithm
consists of three steps:

1. The planar spin-glass problem is mapped onto a
minimum-weight perfect matching problem.

2. The minimum weight-perfect matching problem is
solved exactly using the deterministic Blossom algo-
rithm [21] that scales polynomially in the size of the
input.

3. The perfect matching solution is then translated to the
optimal conﬁguration for the spin-glass problem.

B.
Deﬁnition of time-to-solution

Heuristic methods, such as simulated annealing, simulated
quantum annealing, the D-Wave 2000Q quantum annealer or

## Page 3

107

107

106

106

105

105

104

TTS (µs)

104

TTS (µs)

103

103

102

102

MWPM
DW2000Q, TTS1
DW2000Q, TTS2
ICM (logical), TTS2
100

101

101

100

1
10
100
1000

Logical lattice size

107

107

106

106

105

105

104

TTS (µs)

104

TTS (µs)

103

103

102

102

MWPM
DW2000Q, TTS1
DW2000Q, TTS2
ICM (logical), TTS2
100

101

101

100

1
10
100
1000

Logical lattice size

107

107

106

106

105

105

104

TTS (µs)

104

TTS (µs)

103

103

102

102

MWPM
DW2000Q, TTS1
DW2000Q, TTS2
ICM (logical), TTS2
100

101

101

100

1
10
100
1000

Logical lattice size

107

107

106

106

105

105

104

TTS (µs)

104

TTS (µs)

103

103

102

102

MWPM
DW2000Q, TTS1
DW2000Q, TTS2
ICM (logical), TTS2
100

101

101

100

1
10
100
1000

Logical lattice size

0
10
20
30
40
50

Logical lattice size

0
10
20
30
40
50

Logical lattice size

0
10
20
30
40
50

Logical lattice size

0
10
20
30
40
50

Logical lattice size

Figure 1:
Scaling of the TTS in µs as a function of logical variables in a log-log scale (left) or linear-log scale (right). Data for the
D-Wave 2000Q (DW2000Q) quantum annealer for both deﬁnitions of the TTS are compared to MWPM and ICM. Because the maximal logical
problem size is limited on the D-Wave 2000Q to 16 × 16 variables, we have generated artiﬁcial full Chimera lattices with no broken qubits of
up to 256 × 256 K4,4 unit cells. Note that MWPM scales linearly in a log-log scale, whereas the D-Wave 2000Q scales exponentially. In all
panels, data points represent the 50% of the TTS, while error bars represent the 5%-95% of the distribution. Although the D-Wave 2000Q is
relatively fast for a small number of logical qubits n, MWPM quickly outperforms the quantum device by several orders of magnitude for the
larger lattice sizes. Raw D-Wave 2000Q data taken from Ref. [13].

## Page 4

Figure 2: Left panel: D-Wave Systems Inc. Chimera topology [8].
To generate the anticluster lattice (right panel), two qubits in different
K4,4 cells are contracted to a logical qubit with a strong ferromagnetic
coupler. Different shadings are used as a guide to the eye. Right panel:
Anticluster lattice of logical qubits. Each bulk logical qubit has 10
neighbors and the lattice is nonplanar. Therefore, polynomial exact
algorithms cannot be used to solve the logical problems.

isoenergetic cluster moves, can only determine the optimum
of the cost function up to a probability p. If the optimization
procedure requires a certain time T, given that the optimum is
only obtained with a probability p, it is necessary to deﬁne a
time-to-solution (TTS). A simple (yet naive) possibility con-
sists of making the observation that, on average, one needs
to repeat the computation ≈1/p times in order to observe
one optimal result. Therefore, for a computational time T, a
possible deﬁnition of the TTS is

TTS1 = T

p .
(2)

A commonly-used, more accurate deﬁnition of the TTS that
incorporates the cost of having uncertainty in the heuristic
results is given as follows: Let k be the number of (unknown)
iterations required to have a probability of success of at least
99%, i.e., s = 0.99. The probability that all k attempts fail to
ﬁnd the correct answer is Pwrong = (1−p)k. Because an overall
probability of success s is needed, it is required that Pwrong < s.
Therefore, k must be at least k > log(1 −s)/ log(1 −p).
Assuming that each attempt require T times, the TTS can be
deﬁned as

TTS2 = T log(0.01)

log(1 −p).
(3)

Note that TTS2 < TTS1 at ﬁxed p and T. However, in general,
TTS2 is preferred, because it gives a lower bound to the overall
probability. Reference [13] used the deﬁnition shown in Eq. (2).
Using the raw data from Ref. [13], we have converted their
results into the more commonly used TTS shown in Eq. (3).

IV.
RESULTS

Figure 1 summarizes our results where we compare the
performance of the D-Wave 2000Q quantum annealer to both
ICM and MWPM. The simulations were performed on a single
core of an Intel(R) Xeon(R) CPU (E5-1650v2 with 3.50GHz

clock speed). While both the D-Wave 2000Q quantum an-
nealer and ICM scale exponentially, MWPM scales polyno-
mially with the size of the input. To show this in more detail,
we have generated artiﬁcial problems on perfect Chimera lat-
tices of up to 256 × 256 logical variables. Although for small
systems the D-Wave 2000Q chip is remarkably fast, only by
doubling the largest number of logical variables on the chip
results in MWPM outperforming the quantum annealer by ap-
proximately three orders of magnitude. One has to remember,
however, that the D-Wave 2000Q quantum annealer is a spe-
cial purpose machine designed to minimize binary problems,
whereas classical CMOS technologies require other processes
to run, such as the operating system, kernel and other concur-
rent processes.

V.
DISCUSSION

Although the D-Wave chip shows remarkable promise, in
this work we show that benchmarks which encode the logical
problem on a planar topology is bound to fail in reaching the
crown of quantum speedup. The quantum annealer would have
to perform exponentially faster, in order to outperform the
exact polynomial algorithm.
So how can we eventually prove the value of quantum an-
nealing topologies? First and foremost, encode the problems
in nonplanar logical topologies to ensure that no exact polyno-
mial algorithms can be used. One possible approach we call
“anticlusters” (see Fig. 2) is to contract the links between the
K4,4 cells to become logical variables. This would results in
a nontrivial nonplanar topology where each logical variable
has 10 neighbors, except for the logical variables on the edges
of the lattice which only have 5 neighbors. For a Chimera
lattice with c × c K4,4 cells (i.e., 8c2 physical qubits), the
corresponding anticluster lattice would have 4c(c + 1) logi-
cal qubits arranged on a square-lattice-like structure of linear
dimensions c × c. The large connectivity of the anticluster
lattice, as well as the large number of logical variables allows
for the generation of nontrivial benchmarking problems. For
example, overlaying this topology that resembles the offspring
of a farm fence with a square lattice with frustrated cluster
loops or post-selected spin-glass problems, should generate
hard benchmarks for classical algorithms.
A second alternative to demonstrate the capabilities of the
D-Wave 2000Q is to use the machine as a physical simulator to
study nontrivial quantum physics Hamiltonians [22]. Because
these are very hard to simulate already for small numbers
of variables, the D-Wave 2000Q might be able to outperform
classical simulation techniques in the near future.

Acknowledgments

We would like to thank the D-Wave team and, in partic-
ular, J. King for sharing their problem instances and raw
data, as well as comments on the manuscript. We are also
indebted to Richard Harris at D-Wave for sharing potentially
groundbreaking, yet hopefully soon-to-be-published results.

## Page 5

We thank H. Munoz-Bauza for rendering the anticluster prob-
lems. H. G. K. would like to thank Zheng Zhu for sharing
his implementation of the ICM heuristic, as well as F. Hamze
and G. Rosenberg for multiple discussions. He also thanks
Franziskaner Naturtr¨ub for inspiration. H. G. K. acknowledges
support from the NSF (Grant No. DMR-1151387). S. M. ac-
knowledges Eleanor G. Rieffel for the useful discussions and
the careful reading of the manuscript. This research is based
upon work supported in part by the Ofﬁce of the Director of

National Intelligence (ODNI), Intelligence Advanced Research
Projects Activity (IARPA), via MIT Lincoln Laboratory Air
Force Contract No. FA8721-05-C-0002. The views and conclu-
sions contained herein are those of the authors and should not
be interpreted as necessarily representing the ofﬁcial policies or
endorsements, either expressed or implied, of ODNI, IARPA,
or the U.S. Government. The U.S. Government is authorized
to reproduce and distribute reprints for Governmental purpose
notwithstanding any copyright annotation thereon.

ference on Uncertainty in Artiﬁcial Intelligence (AUAI Press,
Arlington, Virginia, United States, 2004), UAI ’04, p. 243, ISBN
0-9749039-0-6.
[11] A. Selby, Efﬁcient subgraph-based sampling of Ising-type mod-
els with frustration (2014), (arXiv:cond-mat/1409.3934).
[12] J. Marshall, V. Martin-Mayor, and I. Hen, Practical engineering
of hard spin-glass instances, Phys. Rev. A 94, 012320 (2016).
[13] J. King, S. Yarkoni, J. Raymond, I. Ozﬁdan, A. D. King, M. M.
Nevisi, J. P. Hilton, and C. C. McGeoch, Quantum Anneal-
ing amid Local Ruggedness and Global Frustration (2017),
(arXiv:quant-phys/1701.04579).
[14] S. Kirkpatrick, C. D. Gelatt, Jr., and M. P. Vecchi, Optimization
by simulated annealing, Science 220, 671 (1983).
[15] T. Kadowaki and H. Nishimori, Quantum annealing in the trans-
verse Ising model, Phys. Rev. E 58, 5355 (1998).
[16] E. Farhi, J. Goldstone, S. Gutmann, and M. Sipser, Quan-
tum Computation by Adiabatic Evolution (2000), arXiv:quant-
ph/0001106.
[17] A. K. Hartmann and H. Rieger, Optimization Algorithms in
Physics (Wiley-VCH, Berlin, 2001).
[18] A. K. Hartmann and H. Rieger, New Optimization Algorithms in
Physics (Wiley-VCH, Berlin, 2004).
[19] Z. Zhu, A. J. Ochoa, and H. G. Katzgraber, Efﬁcient Cluster
Algorithm for Spin Glasses in Any Space Dimension, Phys. Rev.
Lett. 115, 077201 (2015).
[20] A. D. King, T. Lanting, and R. Harris, Performance of a quan-
tum annealer on range-limited constraint satisfaction problems
(2015), arXiv:1502.02098.
[21] V. Kolmogorov, Blossom V: A new implementation of a mini-
mum cost perfect matching algorithm, Math. Prog. Comp. 1, 43
(2009).
[22] R. Harris et al., in preparation (2017).

[1] T. F. Rønnow, Z. Wang, J. Job, S. Boixo, S. V. Isakov, D. Wecker,
J. M. Martinis, D. A. Lidar, and M. Troyer, Deﬁning and detect-
ing quantum speedup, Science 345, 420 (2014).
[2] S. Boixo, T. F. Rønnow, S. V. Isakov, Z. Wang, D. Wecker, D. A.
Lidar, J. M. Martinis, and M. Troyer, Evidence for quantum
annealing with more than one hundred qubits, Nat. Phys. 10,
218 (2014).
[3] H. G. Katzgraber, F. Hamze, Z. Zhu, A. J. Ochoa, and H. Munoz-
Bauza, Seeking Quantum Speedup Through Spin Glasses: The
Good, the Bad, and the Ugly, Phys. Rev. X 5, 031026 (2015).
[4] D. Venturelli, S. Mandr`a, S. Knysh, B. O’Gorman, R. Biswas,
and V. Smelyanskiy, Quantum Optimization of Fully Connected
Spin Glasses, Phys. Rev. X 5, 031040 (2015).
[5] V. S. Denchev, S. Boixo, S. V. Isakov, N. Ding, R. Babbush,
V. Smelyanskiy, J. Martinis, and H. Neven, What is the Com-
putational Value of Finite Range Tunneling?, Phys. Rev. X 6,
031015 (2016).
[6] S. Mandr`a, Z. Zhu, W. Wang, A. Perdomo-Ortiz, and H. G. Katz-
graber, Strengths and weaknesses of weak-strong cluster prob-
lems: A detailed overview of state-of-the-art classical heuristics
versus quantum approaches, Phys. Rev. A 94, 022337 (2016).
[7] H. G. Katzgraber, F. Hamze, and R. S. Andrist, Glassy Chimeras
Could Be Blind to Quantum Speedup: Designing Better Bench-
marks for Quantum Annealing Machines, Phys. Rev. X 4,
021008 (2014).
[8] P. Bunyk, E. Hoskinson, M. W. Johnson, E. Tolkacheva, F. Al-
tomare, A. J. Berkley, R. Harris, J. P. Hilton, T. Lanting, and
J. Whittaker, Architectural Considerations in the Design of a
Superconducting Quantum Annealing Processor, IEEE Trans.
Appl. Supercond. 24, 1 (2014).
[9] I. Hen, J. Job, T. Albash, T. F. Rønnow, M. Troyer, and D. A.
Lidar, Probing for quantum speedup in spin-glass problems with
planted solutions, Phys. Rev. A 92, 042325 (2015).
[10] F. Hamze and N. de Freitas, in Proceedings of the 20th Con-
