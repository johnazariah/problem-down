---
source_pdf: ../arxiv_2207.13800.pdf
pages: 45
extracted_at: 2026-04-17T12:32:42+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_2207.13800

Source PDF: ../arxiv_2207.13800.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Quantum critical dynamics in a 5000-qubit programmable spin glass

Andrew D. King,1, ∗Jack Raymond,1 Trevor Lanting,1 Richard Harris,1 Alex Zucca,1 Fabio Altomare,1

Andrew J. Berkley,1 Kelly Boothby,1 Sara Ejtemaee,1 Colin Enderud,1 Emile Hoskinson,1 Shuiyuan
Huang,1 Eric Ladizinsky,1 Allison J.R. MacDonald,1 Gaelen Marsden,1 Reza Molavi,1 Travis
Oh,1 Gabriel Poulin-Lamarre,1 Mauricio Reis,1 Chris Rich,1 Yuki Sato,1 Nicholas Tsai,1 Mark
Volkmann,1 Jed D. Whittaker,1 Jason Yao,1 Anders W. Sandvik,2, † and Mohammad H. Amin1, 3, ‡

1D-Wave Systems, Burnaby, British Columbia, Canada
2Department of Physics, Boston University, 590 Commonwealth Avenue, Boston, Massachusetts 02215, USA
3Department of Physics, Simon Fraser University, Burnaby, British Columbia, Canada
(Dated: April 20, 2023)

Experiments on disordered alloys1–3 suggest that spin glasses can be brought into low-energy
states faster by annealing quantum ﬂuctuations than by conventional thermal annealing. Due to the
importance of spin glasses as a paradigmatic computational testbed, reproducing this phenomenon
in a programmable system has remained a central challenge in quantum optimization4–13. Here we
achieve this goal by realizing quantum critical spin-glass dynamics on thousands of qubits with a
superconducting quantum annealer. We ﬁrst demonstrate quantitative agreement between quantum
annealing and time-evolution of the Schr¨odinger equation in small spin glasses. We then measure
dynamics in 3D spin glasses on thousands of qubits, where simulation of many-body quantum
dynamics is intractable. We extract critical exponents that clearly distinguish quantum annealing
from the slower stochastic dynamics of analogous Monte Carlo algorithms, providing both theoretical
and experimental support for a scaling advantage in reducing energy as a function of annealing time.

arXiv:2207.13800v2 [quant-ph] 18 Apr 2023

The study of spin glasses initiated an enormously
productive exchange between physics and computer sci-
ence14,15. One key byproduct of this exchange was the
invention of simulated annealing (SA)16, a method of op-
timization that simulates a gradually cooling system as it
settles into a low-energy state. Recent decades have seen
annealing brought to bear against countless multivariate
optimization applications, seeking low-energy states that
translate to low-cost solutions17.
Passing through a thermal phase transition—as in
SA—is not the only way to evolve a spin system from
an “easy” disordered phase into a “hard” glassy phase.
One can also pass through a quantum phase transition
(QPT), where the ground state undergoes a macroscopic
shift in response to changing quantum ﬂuctuations. Both
experiments1 and simulations4,5 suggested that quantum
annealing (QA) can guide a spin glass toward equilibrium
faster than thermal annealing. Thus originated QA as
a means of both studying quantum critical phenomena
and optimizing quadratic objective functions18,19. Sim-
ulating the Schr¨odinger dynamics of QA with a classical
computer is an unpromising optimization method, since
memory requirements grow exponentially with system
size. But, as Feynman famously asked20, “Can you do it
with a new kind of computer—a quantum computer?”
This question motivated not only the development of
programmable QA processors6,21–25, but a more general
eﬀort to probe the capabilities of near-term quantum
devices via quantum simulation, including in trapped

∗aking@dwavesys.com
† sandvik@buphy.bu.edu
‡ mhsamin@dwavesys.com

ions26,27, ultracold atoms28, and Rydberg arrays29 (the
latter was recently explored as an annealing optimizer30).
While D-Wave QA processors have already been used to
simulate quantum spin glasses in a decohering thermal
bath31, it was only recently shown that they can simu-
late QPTs with negligible interaction with the thermal
environment32: coherent dynamics of quantum-critical
phenomena despite the ﬁnite temperature of the appa-
ratus itself. Here we use a QA processor to study the
critical dynamics of a spin-glass QPT. The exceedingly
slow dynamics of the spin-glass state make this phase
transition vitally important in the study of quantum op-
timization. We compare these dynamics against SA and
simulated quantum annealing (SQA), an algorithm based
on path-integral Monte Carlo33 that reproduces thermal
equilibrium statistics of QA7,12,34.

QUANTUM ANNEALING AND SCHR¨ODINGER
DYNAMICS

We use a D-Wave Advantage QA processor (Fig. 1a)
whose pairwise-coupled superconducting ﬂux qubits can
be programmed to realize a transverse-ﬁeld Ising model
described by the Hamiltonian

H(s) = Γ(s)HD + J (s)HI
(1)

HD = −
X

i
σx
i
(2)

HI =
X

i,j
Jijσz
i σz
j
(3)

Here σx
i , σz
i are Pauli operators on qubit i, s is a unitless
normalized time, the transverse ﬁeld Γ(s) imparts quan-
tum ﬂuctuations through the driver Hamiltonian HD,

## Page 2

Energy

Time s = t/ta

e

Thermal annealing

Γ

Quantum annealing

FIG. 1. Programmable quantum spin glasses. a, QA processor realizing a transverse-ﬁeld Ising model in pairwise-coupled
superconducting ﬂux qubits, into which various lattice geometries can be programmed. b, 16-spin graph used for small-scale
studies of Schr¨odinger evolution. Each line represents a coupling, whose energy is set to JG or −JG at random. c, 3D structure,
where gray bonds represent ferromagnetically coupled dimers and any two dimers have total coupling JG, −JG, or 0 between
them. d, The QA schedule guides the system from a quantum paramagnet toward a classical state by annealing Γ(s)/J (s)
over time ta. e, 3D quantum spin-glass phase diagram. Paramagnet and spin-glass phases are separated by a thermal phase
transition at temperature T = T 3D
c
> 0 when Γ = 0, and a quantum phase transition at Γ3D
c
when T = 0.

and J (s) is the energy scale of the classical Ising Hamilto-
nian HI. Over annealing time ta, s = t/ta increases from
0 to 1, annealing the system from a quantum paramagnet
dominated by HD, to a classical Ising model dominated
by HI, following an annealing schedule as in Fig. 1d. The
coupling coeﬃcients Jij can be programmed into a vari-
ety of 2D and 3D geometries, among others12,31,35–38 (the
QA processor also provides programmable biases, which
we set to zero in this study).
Although our main focus is on large spin glasses, we
ﬁrst seek evidence of coherent quantum dynamics in an
ensemble of small spin glasses. Taking the 16-spin graph
in Fig. 1b, we generate spin-glass realizations with each
coupling set to Jij = +1 or −1 uniformly at random.
We select 100 spectrally unique realizations in which HI
has two ground states and many ﬁrst excited states. At
this scale we can numerically evolve the time-dependent
Schr¨odinger equation

iℏd

dt |ψ(t)⟩= H(t/ta) |ψ(t)⟩,
(4)

for the wavefunction |ψ(t)⟩, where H(s) is given by
Eq. (1). Let |φi(s)⟩denote instantaneous eigenstates of
H(s) with eigenvalues Ei(s). Suﬃciently slow evolution
results in adiabatic quantum optimization (AQO)39 into
the twofold-degenerate ﬁnal ground states |φ0(1)⟩and
|φ1(1)⟩. The relevant timescale is proportional to δ−2
min,
where

δmin = min
s
|E2(s) −E0(s)|
(5)

is the minimum parity-preserving eigengap. Faster an-
neals have a higher probability of excitation.
In Fig. 2a, we show spectral gaps Ei(s) −E0(s) for
three 16-qubit examples: one with a small gap, one with

a moderate gap, and one with a large gap. For ﬁxed ta
we deﬁne

n∈{0,1}
|⟨φn(s)|ψ(s)⟩|2 ,
(6)

Pinst(s) =
X

n∈{0,1}
|⟨φn(1)|ψ(s)⟩|2 ,
(7)

Pﬁnal(s) =
X

which measure instantaneous probabilities of being in the
ground or ﬁrst excited state of H(s) and H(1), respec-
tively. Since the classical ground states are twofold de-
generate, Pﬁnal(1) gives the success probability of QA
under Schr¨odinger dynamics. Fig. 2b tracks Pinst(s) and
Pﬁnal(s) through anneals with ta = 14 ns. The wavefunc-
tion begins concentrated on the easily-prepared ground
state at s = 0, and this probability decreases via Landau-
Zener excitation in the vicinity of a small gap.
We run QA experiments on each of these 100 in-
stances using 192 disjoint sets of qubits in parallel. The
Schr¨odinger excitation probability 1−PGS = 1−Pﬁnal(1)
is compared against experimental QA excitation prob-
ability in Fig. 2c; the probabilities are in close agree-
ment with no ﬁtting parameters used, showing an ap-
proximately exponential form. Fig. 2d compares PGS for
ta = 14 ns across the entire 100-instance ensemble. In
Extended Data Fig. E1 we compare probability distri-
butions among ground and ﬁrst excited states for QA,
SA, SQA, and Schr¨odinger dynamics, and ﬁnd that ex-
perimental QA data are better explained by Schr¨odinger
dynamics than by SA and SQA. The quantitative agree-
ment between QA experiment and Schr¨odinger evolution
up to ta = 30 ns provides strong evidence for coherent
quantum dynamics at small scale. We now consider crit-
ical dynamics in large 3D spin glasses.

## Page 3

0.8

0.6

QA PGS

0.4

0.2

QA
Schrödinger
0
0.2
0.4
0.6
0.8
0

Schrödinger PGS

FIG. 2. Coherent Schr¨odinger dynamics. a, For three exemplary 16-qubit spin glasses, we show the eight lowest eigengaps of
the time-dependent QA Hamiltonian. b, We evolve the Schr¨odinger equation for QA with ta = 14 ns, tracking the wavefunction’s
probability of collapse onto the ﬁnal (classical) ground-state manifold (Pﬁnal(s)) and the two lowest-energy instantaneous
eigenstates (Pinst(s)). Pﬁnal(1) is the ﬁnal ground-state probability PGS of the Schr¨odinger evolution. c, 1 −PGS for the same
three spin glasses, in experimental QA and Schr¨odinger evolution for a range of annealing times. d, Comparison of PGS for QA
and Schr¨odinger evolution for an ensemble of 100 16-spin glasses, for ta = 14 ns. Error bars indicate 95% conﬁdence intervals
for the average over parallel QA experiments using 192 diﬀerent sets of qubits.

CRITICAL SPIN-GLASS DYNAMICS

When a system is brought slowly (annealed) through a
continuous phase transition, its dynamics slow down due
to diverging correlations, and its macroscopic properties
follow universal behavior described by critical exponents.
Here we use extensions of the Kibble-Zurek (KZ) mech-
anism40–48, which describes the generation of excitations
as an annealed system falls out of equilibrium. We use
a dynamic ﬁnite-size scaling (DFSS) ansatz46 (SM I) to
relate time and the growth of correlations as functions
of two critical exponents: ν, which describes the diver-
gence of correlation length at a phase transition, and z,
which describes divergence of the characteristic timescale
of domain ﬂuctuations. We investigate three annealing
dynamics—QA, SQA, and SA—and their corresponding
phase transitions.
Spin-glass order is quantiﬁed via the overlap between
two replicas (independently annealed N-spin states S and
S′) of a given realization (set of couplings Jij):

N
X

q = 1

i=1
SiS′
i
Si, S′
i ∈{−1, 1}.
(8)

N

The mean-squared Edwards-Anderson order parameter
is given by ⟨q2⟩, with ⟨·⟩denoting an average over both
independent replicas and realizations.
Due to restrictions on the available coupling geometry,
we program spin glasses in the 3D layout shown in Fig. 1c,
which diﬀers from the simple cubic lattice: it has two
qubits at every (x, y, z) coordinate, coupled as a dimer
with strong ferromagnetic coupling Jij = −JFM = −2.
Between neighboring cubic coordinates, we program a to-
tal coupling of ±JG (0 < JG ≤1)—this coupling uses one
coupler in the x and y directions, and in the z direction

the coupling is equally divided between two couplers. We
use open x- and y-boundaries and periodic z-boundaries.
In this model,
contracting the strongly-correlated
dimers into individual spins yields the ±JG Ising spin
glass on a simple cubic lattice, so we expect experimen-
tal results to reﬂect criticality in the same universality
class. Fig. 1e shows the model’s phase diagram in the Γ,
T plane, where a spin-glass (SG) phase is separated from
a disordered paramagnetic (PM) phase. At T = 0 there
is a quantum critical point Γ = Γc > 0. At Γ = 0 there
is a ﬁnite-temperature classical transition at T = Tc > 0.
Tuning JG while keeping JFM = 2 varies the details of
the phase diagram, but not the qualitative picture.
We measure ⟨q2⟩for a range of ta, with linear sys-
tem size L ranging from 5 to 12, in QA (Fig. 3a), SA
(Fig. 3b), and SQA (Extended Data Fig. E6), for JG = 1.
For Monte Carlo (MC) methods, ta is measured in MC
sweeps (MCS). Although in all cases we anneal through
the critical point rather than stopping at the critical
point (see Methods), the system experiences a critical
slowing down at the QPT. Due to slower dynamics in
the glass phase, measurements in the ﬁnal state approxi-
mately reﬂect the relevant critical dynamics. The Binder
cumulant


3 −⟨q4⟩


(9)

U = 1

⟨q2⟩2

2

provides a statistical signature of phase transitions, and
like ⟨q2⟩, also grows with ta and 1/L, as seen in Fig. 3c–d.
For U, any post-critical eﬀective scaling dimensions in
⟨q2⟩2 and ⟨q4⟩cancel, but the functional dependence on
ta remains. Thus, under the DFSS ansatz, U(L, ta) is
expected to collapse onto a common curve for all system
sizes when ta is rescaled by L−z−1/ν (SM I B), reﬂecting
the fact that the annealing time required for the system

## Page 4

a

c

10−1

10−1

⟨q2⟩
⟨q2⟩

U
U

10−2

10−2

10
20
30

10
20
30

ta (ns)

ta (ns)

b

d

10−1

10−1

10−2

10−2

103
104
105

ta (MCS)

ta (MCS)

6

10−2
10−1

taL−μ (ns)

4

μ

2

FIG. 3. Dynamic ﬁnite-size scaling in 3D spin glasses. a–b, Squared overlap ⟨q2⟩varies as a function of L and ta in
QA (a) and SA (b) for 3D spin glasses. c–d, Binder cumulant U scales similarly; rescaling ta by Lµ collapses data onto a
single curve for a ﬁt parameter µ, providing estimates of the KZ exponent µ = z + 1/ν. e, Estimates of µ for varying spin-glass
coupling strengths JG, where dimer coupling JFM = 2, in QA, SA, and SQA. Solid and dashed horizontal lines indicate literature
values49 and estimates from simple cubic lattices (Extended Data E8) respectively. f, Tuning the doping probability p reveals
a ﬁnite-size crossover between the SG phase and the AFM phase, separated by a critical doping pc ≈0.778 at T = 0, Γ = 0
(vertical line). Observed dynamics in these phases are characteristic of critical dynamics and coarsening dynamics, respectively.
Vertical error bars are 95% statistical conﬁdence intervals and horizontal error bars indicate measurement uncertainty in ta.

to remain adiabatic up to a correlation length of L scales
as

ta(L) ∼Lµ,
µ = z + 1/ν.
(10)

Thus we estimate the KZ exponent µ via best-ﬁt col-
lapse of U horizontally along the time axis. Fig. 3c–d
show collapses of U, from which we extract µ as a ﬁtting
parameter.
In Fig. 3e we show these estimates for QA, SA and
SQA for a range of coupling energies JG. In all cases,
U(L, ta) approximately follows power-law scaling when
far from equilibrium48. The extracted KZ exponents are
clearly distinct, with smaller values indicating faster dy-
namics. We ﬁnd µQA between 2.9 and 3.1 depending on
JG. Adding our MC estimate 1/νQA ≈1.55 (SM III) to
zQA ≈1.349 gives µQA ≈2.85, in close agreement with
experimental results.
For SA we ﬁnd µSA ≈5.3, much larger than QA but
smaller than estimates from simple cubic lattices; for SA
we found a value 6.0 (dashed line) compared to previ-
ously reported48 value 6.3. These deviations are largely
explained by ﬁnite size eﬀects, and dimers delaying the
onset of asymptotic behavior (see Figs. E6—E8 and SM
Section IV A). No previous estimate of µSQA has been re-
ported; the dashed line in Fig. 3e indicates the extracted
value µSQA = 4.39 for simple cubic lattices (Fig. E8).
Since QA and SQA share an equilibrium exponent ν,
this corresponds to zSQA ≈2.8, which reﬂects the MC
dynamics.

To better understand the role of frustration in the
glassy dynamics, we increase the “doping” probability
p of a random inter-dimer coupling being antiferromag-
netic (+JG). The SG phase has been shown to persist un-
til pc = 0.778 (vertical line) for T = 0 and Γ = 0, beyond
which the system is a disordered antiferromagnet50–52—
we might expect that Γ > 0 slightly reduces pc53. Fig. 3f
shows the p-dependence of µ extracted by collapsing for
even values of L; all three dynamics are insensitive to
changes in p until it approaches pc.
For p close to 1,
QA, SA, and SQA all have µ ≈2, consistent with coars-
ening dynamics in the AFM phase47. In this scenario,
the dynamics that occurs after the critical point elimi-
nates small domains, replacing the KZ exponent µ with
a universal exponent 2. The latter corresponds to corre-
lation length scaling as ξ ∝t−1/2
a
, expected for diﬀusive
dynamics present in the AFM phase. Due to the rough
potential landscape in the SG phase, the post-critical dy-
namics have negligible eﬀect on µ, although they aﬀect
energy decay as we discuss next.

ENERGY DECAY

The smaller values of critical exponents z and µ, ob-
tained via data collapse, indicate faster critical dynamics
in QA compared to SA and SQA. We now ask whether
this leads to a speedup in approximating the ground-
state energy in classical Ising models. We ﬁrst answer

## Page 5

ρf
E

QA ta (ns)

FIG. 4. Critical scaling of ﬁnal residual energy. a, Scaling of ﬁnal residual energy density ρf
E versus ta, with lines showing
power-law ﬁts to the form ρf
E ∝t
−κf
a
. Empty markers are excluded from power-law ﬁt (see text). b, Markers show extracted
exponents κf for QA, SA, and SQA for varying JG in 3D spin glasses; horizontal lines show estimates of κc (Eq. (12)) using
estimates of µ shown as horizontal lines in Fig. 3e. c, Number of MCS required for SA and SQA to match the residual energy
achieved by QA in a given QA annealing time. Dashed line is a guide to the eye showing equal scaling. Shading represents the
onset of thermal eﬀects outside the coherent QA regime. Error bars represent 95% bootstrap C.I. over spin-glass realizations.

this question theoretically by considering a hypothetical
annealing protocol that is measured at the critical point.
Although this is not the real schedule of QA, it makes the
energy decay dependent only on the dynamics approach-
ing the critical point, and therefore allows connecting
the relevant critical exponents. We deﬁne dimensionless
residual Ising energy density at the critical point as

ρc
E =
HI −Ec
/(NJG).
(11)

Here N is the number of spins, and Ec is the equilibrium
expectation of HI at T = Tc and Γ = 0 for SA, and at
T = 0 and Γ = Γc for QA and SQA. Notice that ρc
E →0
as ta →∞. It is shown in SM I that ρc
E follows a power-
law relation:

ρc
E ∝t−κc
a
,
κc = (ds −1/ν)/µ,
(12)

where ds = d for SA and ds = d + zQA for QA and SQA.
As expected, κc is inversely related to the KZ exponent
µ, therefore faster critical dynamics (smaller µ) leads to
faster decay of energy. Moreover, ds is larger for quan-
tum than classical, making a larger contribution to the
numerator.
However, ρc
E is not very relevant to optimization be-
cause Ec is far from the ground-state energy E0 of HI.
We therefore consider the corresponding ﬁnal quantities
ρf
E and κf obtained by annealing to the low-temperature
classical point T ≪Tc, Γ = 0:

ρf
E =
HI −E0
/(NJG),
(13)

and ﬁtting ρf
E ∝t−κf
a
. Again the average is over realiza-
tions and samples, with annealing according to the full
QA schedule. For very long (adiabatic) anneals, we ex-
pect ρf
E →0, thus optimal solutions are asymptotically
reached.
Fig. 4a shows ρf
E as a function of annealing time for
QA, SQA, and SA, for 3D spin glasses on N = 5374 spins

(15 × 15 × 12 dimers, with some vacancies). The ground-
state energy E0 is estimated by exchange MC (see SM
II C). Each dynamics follows a power-law scaling within
a window of ta (SM V) but deviates outside the window,
most notably for QA due to the onset of thermal eﬀects.
For experimental QA, deviation from coherent behavior
is expected for longer anneals due to the onset of thermal
excitations32.
For SA, the decay of ρf
E settles onto a
consistent exponent only after several hundred MCS.
We estimate κf for the three dynamics with varying
JG from power-law ﬁts. Figure 4b shows, as a function
of JG, the ﬁt values of κf (symbols) as well as the critical
values κc (horizontal lines) obtained using independent
MC estimates of z and 1/ν, corresponding to the lines
in Fig. 3e.
Deviations κf < κc are expected beyond
the critical point (SM I C 4); we ﬁnd a modest correction
κc −κf ≈0.1 for both SA and SQA (SM IV B), which
one might also see in QA if it could be measured at the
critical point.
QA shows the fastest energy decay κf, followed by
SQA and SA. For suﬃciently large JG, ρf
E decays roughly
quadratically faster in QA than in SA, with SQA in be-
tween the two. This experimentally-observed scaling ad-
vantage is consistent with the theoretical speedup in crit-
ical ordering dynamics (smaller µ in Fig. 3e), and faster
critical energy decay (larger κc in Fig. 4b). In Fig. 4c
we show the annealing time (in MCS) required by SA
and SQA to match the energy achieved by a given ta in
QA; within the coherent QA regime, the approximation
speedup of QA over SA and SQA increases as a function
of annealing time.

OUTLOOK

We have experimentally demonstrated quantum criti-
cal dynamics in programmable spin glasses on thousands
of qubits, observing the expected scaling in system size

## Page 6

and annealing time. Simulation accuracy was conﬁrmed
via comparison to numerical simulation of Schr¨odinger
dynamics at the 16-qubit scale. For large 3D spin glasses,
the simulated many-body quantum dynamics are far be-
yond the reach of current exhaustive or tensor-based
techniques; the former is limited to tens of qubits and the
latter can be applied to moderately-sized 2D models30,54.
We therefore appeal to critical exponents via ﬁnite-size
scaling analysis, ﬁnding good agreement with indepen-
dent MC estimates. Thus we have presented both mi-
croscopic and macroscopic evidence for a coherently an-
nealed programmable quantum spin glass. These expo-
nents indicate, in theory and experiment, that quantum
annealing has a dynamical advantage over simulated an-
nealing and simulated quantum annealing in penetrating
the spin-glass phase. The predicted speedup was exper-
imentally demonstrated through a scaling advantage in
approach to the ground-state energy. These results point
to the utility of programmable quantum annealers both
as quantum simulators and optimization tools.

For suﬃciently large spin systems, the extent of ideal
quantum critical scaling is limited in time by qubit deco-
herence, disorder and noise, and the results shown here
indicate that improvements in these areas would pay
great dividends. Extending the region of critical scaling
would not only facilitate the further study of these dy-
namics, but also extend their utility in real-world appli-
cations, helping QA reach lower-energy solutions. These
eﬀorts must be balanced with improvements in qubit con-
nectivity, which allow more ﬂexible problem embeddings,
and high coupling energy, which can protect against con-
trol error and thermal excitation outside the coherent
limit.

Spin glasses represent a paradigmatic hard optimiza-
tion problem, and provide a robust theoretical framework
for understanding and demonstrating quantum critical
dynamics.
They were instrumental in motivating, via
magnetic experiments, the ﬁeld of quantum annealing
itself—here we have answered in the aﬃrmative the foun-
dational question raised over 20 years ago: Is it possible

[1] J. Brooke, D. Bitko, T. F., Rosenbaum, and G. Aep-
pli, Quantum Annealing of a Disordered Magnet, Science
284, 779 (1999).
[2] G. Aeppli and T. F. Rosenbaum, Experiments on
Quantum Annealing, in Quantum Annealing and Other
Optimization Methods, edited by A. Das and B. K.
Chakrabarti (Springer Berlin Heidelberg, 2005) Chap. 6,
pp. 157–169.
[3] A. Das and B. K. Chakrabarti, Colloquium: Quantum
annealing and analog quantum computation, Reviews of
Modern Physics 80, 1061 (2008).
[4] T. Kadowaki and H. Nishimori, Quantum annealing in
the transverse Ising model, Physical Review E 58, 5355
(1998).

to engineer a programmable quantum system, in which
quantum annealing imparts a dynamical advantage over
simulated annealing?
Extending this characterization
of quantum dynamics to industry-relevant optimization
problems, which generally do not allow for analysis via
universal critical exponents or ﬁnite-size scaling, would
mark an important next step in practical quantum com-
puting.

ACKNOWLEDGMENTS

The authors are grateful to Peter Young, Hidetoshi
Nishimori, Sei Suzuki, and Jonas Charfreitag for help-
ful discussions.
A.W.S. was supported by the the
Simons Foundation under Simons Investigator Award
No. 511064. Some of the numerical simulations were car-
ried out using the Shared Computing Cluster managed
by Boston University’s Research Computing Services.

AUTHOR CONTRIBUTIONS

A.D.K., J.R., T.L., R.H., A.Z., A.W.S., and M.H.S.
conceived and designed the experiments and analyzed
the data. A.D.K., J.R., T.L., and A.W.S. performed the
experiments and simulations. T.L., R.H., F.A., A.J.B.,
K.B., S.E., C.E., E.H., S.H., E.L., A.J.R.M., G.M., R.M.,
T.O., G.P.-L., M.R., C.R., Y.S., N.T., M.V., J.D.W.,
J.Y., and M.H.A. contributed to the design, fabrication,
deployment, and calibration of the quantum annealing
system. A.D.K., J.R., R.H., A.W.S., and M.H.A. wrote
the manuscript.

COMPETING INTERESTS

A.W.S. declares no competing interests. All other au-
thors have received stock options in D-Wave as current
or former employees, and declare a competing ﬁnancial
interest on that basis.

[5] G. E. Santoro, R. Marton´ak, E. Tosatti, and R. Car,
Theory of Quantum Annealing of an Ising Spin Glass,
Science 295, 2427 (2002).
[6] R. Harris, M. W. Johnson, T. Lanting, A. J. Berkley,
J. Johansson, et al., Experimental investigation of an
eight-qubit unit cell in a superconducting optimization
processor, Physical Review B 82, 1 (2010).
[7] T. F. Rønnow, Z. Wang, J. Job, S. Boixo, S. V. Isakov,
et al., Deﬁning and detecting quantum speedup, Science
345, 420 (2014).
[8] H. G. Katzgraber, F. Hamze, and R. S. Andrist, Glassy
Chimeras Could Be Blind to Quantum Speedup:
De-
signing Better Benchmarks for Quantum Annealing Ma-
chines, Physical Review X 4, 021008 (2014).

## Page 7

[9] I. Hen, J. Job, T. Albash, T. F. Rønnow, M. Troyer, and
D. A. Lidar, Probing for quantum speedup in spin-glass
problems with planted solutions, Physical Review A 92,
042325 (2015).
[10] B. Heim, T. F. Rønnow, S. V. Isakov, and M. Troyer,
Quantum versus classical annealing of Ising spin glasses,
Science 348, 215 (2015).
[11] S. Boixo, V. N. Smelyanskiy, A. Shabani, S. V. Isakov,
M. Dykman, V. S. Denchev, M. H. Amin, A. Y. Smirnov,
M. Mohseni, and H. Neven, Computational multiqubit
tunnelling in programmable quantum annealers, Nature
Communications 7, 10327 (2016).
[12] V. S. Denchev, S. Boixo, S. V. Isakov, N. Ding, R. Bab-
bush, V. N. Smelyanskiy, J. M. Martinis, and H. Neven,
What is the Computational Value of Finite-Range Tun-
neling?, Physical Review X 6, 031015 (2016).
[13] T. Albash and D. A. Lidar, Demonstration of a Scaling
Advantage for a Quantum Annealer over Simulated An-
nealing, Physical Review X 8, 031016 (2018).
[14] M. Mezard and A. Montanari, Information, physics, and
computation (Oxford University Press, 2009).
[15] D. L. Stein and C. M. Newman, Spin Glasses and Com-
plexity (Princeton University Press, 2013).
[16] S. Kirkpatrick, C. D. Gelatt, and M. P. Vecchi, Optimiza-
tion by Simulated Annealing, Science 220, 671 (1983).
[17] C. M. Tan, ed., Simulated Annealing (InTech, Vienna,
2008).
[18] T. Albash and D. A. Lidar, Adiabatic quantum compu-
tation, Reviews of Modern Physics 90, 015002 (2018).
[19] A. Das and B. K. Chakrabarti, eds., Quantum Anneal-
ing and Other Optimization Methods, Lecture Notes in
Physics, Vol. 679 (Springer Berlin Heidelberg, Berlin,
Heidelberg, 2005).
[20] R. P. Feynman, Simulating physics with computers,

[28] C. Gross and I. Bloch, Quantum simulations with ultra-
cold atoms in optical lattices, Science 357, 995 (2017).
[29] P. Scholl, M. Schuler, H. J. Williams, A. A. Eberharter,
D. Barredo, K.-N. Schymik, V. Lienhard, L.-P. Henry,
T. C. Lang, T. Lahaye, A. M. L¨auchli, and A. Browaeys,
Programmable quantum simulation of 2D antiferromag-
nets with hundreds of Rydberg atoms, Nature 595, 233
(2020).
[30] S. Ebadi, A. Keesling, M. Cain, T. T. Wang, H. Levine,
D. Bluvstein, G. Semeghini, A. Omran, J.-G. Liu,
R. Samajdar, X.-Z. Luo, B. Nash, X. Gao, B. Barak,
E. Farhi, S. Sachdev, N. Gemelke, L. Zhou, S. Choi,
H. Pichler, S.-T. Wang, M. Greiner, V. Vuletic, and
M. D. Lukin, Quantum optimization of maximum in-
dependent set using Rydberg atom arrays, Science 0,
eabo6587 (2022).
[31] R. Harris, Y. Sato, A. J. Berkley, M. Reis, F. Altomare,
et al., Phase transitions in a programmable quantum spin
glass simulator, Science 361, 162 (2018).
[32] A. D. King, S. Suzuki, J. Raymond, A. Zucca, T. Lanting,
et al., Coherent quantum annealing in a programmable
2,000 qubit Ising chain, Nature Physics 18, 1324 (2022).
[33] M. Suzuki, Relationship between d-Dimensional Quan-
tal Spin Systems and (d+1)-Dimensional Ising Systems:
Equivalence, Critical Exponents and Systematic Approx-
imants of the Partition Function and Spin Correlations,
Progress of Theoretical Physics 56, 1454 (1976).
[34] S. V. Isakov, G. Mazzola, V. N. Smelyanskiy, Z. Jiang,
S. Boixo, H. Neven, and M. Troyer, Understanding Quan-
tum Tunneling through Quantum Monte Carlo Simula-
tions, Physical Review Letters 117, 180402 (2016).
[35] A. D. King, J. Carrasquilla, J. Raymond, I. Ozﬁdan,
E. Andriyash, et al., Observation of topological phenom-
ena in a programmable lattice of 1,800 qubits, Nature
560, 456 (2018).
[36] K. Nishimura, H. Nishimori, and H. G. Katzgraber,
Griﬃths-McCoy singularity on the diluted Chimera
graph:
Monte Carlo simulations and experiments on
quantum hardware, Physical Review A 102, 042403
(2020).
[37] P. Weinberg, M. Tylutki, J. M. R¨onkk¨o, J. Westerholm,
J. A. ˚Astr¨om, P. Manninen, P. T¨orm¨a, and A. W. Sand-
vik, Scaling and Diabatic Eﬀects in Quantum Anneal-
ing with a D-Wave Device, Physical Review Letters 124,
090502 (2020).
[38] S. Zhou, D. Green, E. D. Dahl, and C. Chamon, Ex-
perimental realization of classical Z2 spin liquids in a
programmable quantum device, Physical Review B 104,
L081107 (2021).
[39] E. Farhi, J. Goldstone, S. Gutmann, J. Lapan, A. Lund-
gren, and D. Preda, A Quantum Adiabatic Evolution
Algorithm Applied to Random Instances of an NP-
Complete Problem, Science 292, 472 (2001).
[40] T. W. B. Kibble, Topology of cosmic domains and strings,

International Journal of Theoretical Physics 21, 467
(1982).
[21] M. W. Johnson, M. H. Amin, S. Gildert, T. Lanting,
F. Hamze, et al., Quantum annealing with manufactured
spins, Nature 473, 194 (2011).
[22] W. Lechner, P. Hauke, and P. Zoller, A quantum anneal-
ing architecture with all-to-all connectivity from local in-
teractions, Science Advances 1, 1 (2015).
[23] S. J. Weber, G. O. Samach, D. Hover, S. Gustavsson,
D. K. Kim, A. Melville, D. Rosenberg, A. P. Sears,
F. Yan, J. L. Yoder, W. D. Oliver, and A. J. Kerman, Co-
herent Coupled Qubits for Quantum Annealing, Physical
Review Applied 8, 014004 (2017).
[24] S. Novikov, R. Hinkey, S. Disseler, J. I. Basham, T. Al-
bash, A. Risinger, D. Ferguson, D. A. Lidar, and K. M.
Zick, Exploring More-Coherent Quantum Annealing, in
2018 IEEE International Conference on Rebooting Com-
puting (ICRC) (IEEE, 2018) pp. 1–7.
[25] P. Hauke, H. G. Katzgraber, W. Lechner, H. Nishimori,
and W. D. Oliver, Perspectives of quantum annealing:
methods and implementations, Reports on Progress in
Physics 83, 054401 (2020).
[26] R. Blatt and C. F. Roos, Quantum simulations with
trapped ions, Nature Physics 8, 277 (2012).
[27] C. Monroe, W. C. Campbell, L.-M. Duan, Z.-X. Gong,
A. V. Gorshkov, P. W. Hess, R. Islam, K. Kim, N. M.
Linke, G. Pagano, P. Richerme, C. Senko, and N. Y.
Yao, Programmable quantum simulations of spin systems
with trapped ions, Reviews of Modern Physics 93, 025001
(2021).

Journal of Physics A: Mathematical and General 9, 1387
(1976).
[41] W. H. Zurek, Cosmological experiments in superﬂuid he-
lium?, Nature 317, 505 (1985).
[42] A. Polkovnikov, Universal adiabatic dynamics in the
vicinity of a quantum critical point, Physical Review B
72, 161201 (2005).
[43] J. Dziarmaga, Dynamics of a quantum phase transition:
Exact solution of the quantum ising model, Physical Re-
view Letters 95, 1 (2005).

## Page 8

[44] W. H. Zurek, U. Dorner, and P. Zoller, Dynamics of a
quantum phase transition, Physical Review Letters 95, 2
(2005).
[45] S. Deng, G. Ortiz, and L. Viola, Dynamical non-ergodic
scaling in continuous ﬁnite-order quantum phase transi-
tions, Europhysics Letters 84, 67008 (2008).
[46] C. De Grandi, A. Polkovnikov, and A. W. Sandvik, Uni-
versal nonequilibrium quantum dynamics in imaginary
time, Physical Review B 84, 224303 (2011).
[47] A. Chandran, A. Erez, S. S. Gubser, and S. L. Sondhi,
Kibble-Zurek problem:
Universality and the scaling
limit, Physical Review B 86, 064304 (2012).
[48] C.-W. Liu, A. Polkovnikov, A. W. Sandvik, and A. P.
Young, Universal dynamic scaling in three-dimensional
Ising spin glasses, Physical Review E 92, 022128 (2015).
[49] M. Guo, R. N. Bhatt, and D. A. Huse, Quantum crit-
ical behavior of a three-dimensional Ising spin glass in
a transverse magnetic ﬁeld, Physical Review Letters 72,
4137 (1994).
[50] A. K. Hartmann, Ground-state behavior of the three -
dimensional ±J random-bond Ising model, Physical Re-
view B 59, 3617 (1999).
[51] M. Hasenbusch, F. P. Toldin, A. Pelissetto, and E. Vi-
cari, Critical behavior of the three-dimensional ±J Ising
model at the paramagnetic-ferromagnetic transition line,
Physical Review B 76, 1 (2007).
[52] M. Hasenbusch, F. P. Toldin, A. Pelissetto, and E. Vi-
cari, Magnetic-glassy multicritical behavior of the three-
dimensional ±J Ising model, Physical Review B 76,
184202 (2007).
[53] H. Nishimori, Boundary between the Ferromagnetic and
Spin Glass Phases, Journal of the Physical Society of
Japan 61, 1011 (1992).
[54] M. Schmitt, M. M. Rams, J. Dziarmaga, M. Heyl, and
W. H. Zurek, Quantum phase transition dynamics in the
two-dimensional transverse-ﬁeld Ising model, Science Ad-
vances 8, 1 (2022).
[55] R. Harris, J. Johansson, A. J. Berkley, M. W. Johnson,
T. Lanting, S. Han, P. Bunyk, E. Ladizinsky, T. Oh,
I. Perminov, E. Tolkacheva, S. Uchaikin, E. M. Chapple,
C. Enderud, C. Rich, M. Thom, J. Wang, B. Wilson,
and G. Rose, Experimental demonstration of a robust
and scalable ﬂux qubit, Physical Review B 81, 1 (2010).
[56] M. N. Barber, Finite-Size Scaling, in Phase Transitions
and Critical Phenomena, Vol. 8, edited by C. Domb and
J. L. Lebowitz (Academic Press, 1983).
[57] V. Privman, Finite-Size Scaling Theory, in Finite Size
Scaling and Numerical Simulation of Statistical Systems,
edited by V. Privman (World Scientiﬁc, 1990) Chap. 1,
pp. 1–98.
[58] D. Rossini and E. Vicari, Coherent and dissipative dy-
namics at quantum phase transitions, Physics Reports
936, 1 (2021).
[59] M. E. Fisher and M. N. Barber, Scaling Theory for Finite-
Size Eﬀects in the Critical Region, Physical Review Let-
ters 28, 1516 (1972).
[60] J. Cardy, Scaling and Renormalization in Statistical
Physics (Cambridge University Press, 1996).
[61] A. Aharony and M. E. Fisher, Nonlinear scaling ﬁelds and
corrections to scaling near criticality, Physical Review B
27, 4394 (1983).
[62] S. Jin, A. Sen, W. Guo, and A. W. Sandvik, Phase tran-
sitions in the frustrated Ising model on the square lattice,
Physical Review B 87, 144406 (2013).

[63] M. E. Fisher, Renormalization group theory: Its basis
and formulation in statistical physics, Reviews of Modern
Physics 70, 653 (1998).
[64] S. Sachdev, Quantum Phase Transitions (Cambridge
University Press, Cambridge, 2011).
[65] H. Rieger and A. P. Young, Zero-temperature quantum
phase transition of a two-dimensional Ising spin glass,
Physical Review Letters 72, 4141 (1994).
[66] W. Zurek, Cosmological experiments in condensed mat-
ter systems, Physics Reports 276, 177 (1996).
[67] C. De Grandi, V. Gritsev, and A. Polkovnikov, Quench
dynamics near a quantum critical point, Physical Review
B 81, 012303 (2010).
[68] M. Kolodrubetz, B. K. Clark, and D. A. Huse, Nonequi-
librium Dynamic Critical Scaling of the Quantum Ising
Chain, Physical Review Letters 109, 015701 (2012).
[69] C.-W. Liu, A. Polkovnikov, and A. W. Sandvik, Dynamic
scaling at classical phase transitions approached through
nonequilibrium quenching, Physical Review B 89, 054307
(2014).
[70] C. W. Liu, A. Polkovnikov, and A. W. Sandvik, Quantum
versus classical annealing: Insights from scaling theory
and results for spin glasses on 3-regular graphs, Physical
Review Letters 114, 1 (2015).
[71] S. J. Rubin, N. Xu, and A. W. Sandvik, Dual time scales
in simulated annealing of a two-dimensional Ising spin
glass, Physical Review E 95, 052133 (2017), 1609.09024.
[72] N. Xu, K.-H. Wu, S. J. Rubin, Y.-J. Kao, and A. W.
Sandvik, Dynamic scaling in the two-dimensional Ising
spin glass with normal-distributed couplings, Physical
Review E 96, 052102 (2017).
[73] H. Shao, W. Guo, and A. W. Sandvik, Monte Carlo
Renormalization Flows in the Space of Relevant and Ir-
relevant Operators: Application to Three-Dimensional
Clock Models, Physical Review Letters 124, 80602
(2020).
[74] T.
Blanchard,
L.
F.
Cugliandolo,
M.
Picco,
and
A. Tartaglia, Critical percolation in the dynamics of the
2D ferromagnetic Ising model, Journal of Statistical Me-
chanics: Theory and Experiment 2017, 113201 (2017).
[75] R.
Miyazaki
and
H.
Nishimori,
Real-space
renormalization-group
approach
to
the
random
transverse-ﬁeld
Ising
model
in
ﬁnite
dimensions,
Physical Review E 87, 1 (2013).
[76] D. A. Matoz-Fernandez and F. Rom´a, Unconventional
critical activated scaling of two-dimensional quantum
spin glasses, Physical Review B 94, 024201 (2016).
[77] C. Pich, A. P. Young, H. Rieger, and N. Kawashima, Crit-
ical behavior and griﬃths-mccoy singularities in the two-
dimensional random quantum ising ferromagnet, Physi-
cal Review Letters 81, 5916 (1998).
[78] R. R. Singh and A. P. Young, Critical and Griﬃths-
McCoy
singularities
in
quantum
Ising
spin
glasses
on d -dimensional hypercubic lattices:
A series ex-
pansion study, Physical Review E 96, 10.1103/Phys-
RevE.96.022139 (2017).
[79] E. Marinari, G. Parisi, and J. J. Ruiz-Lorenzo, Numerical
simulations of spin glass systems, in Spin Glasses and
Random Fields, edited by A. P. Young (World Scientiﬁc,
1997) pp. 59–98.
[80] K. Boothby, P. Bunyk, J. Raymond, and A. Roy, Next-
Generation Topology of D-Wave Quantum Processors
(2020), arXiv:2003.00133.

## Page 9

[81] J. Charfreitag, M. J¨unger, S. Mallach, and P. Mutzel,
McSparse:
Exact solutions of sparse maximum cut
and sparse unconstrained binary quadratic optimization
problems, in 2022 Proceedings of the Symposium on Algo-
rithm Engineering and Experiments (ALENEX), edited
by C. A. Phillips and B. Speckmann (2022) pp. 54–66.
[82] Z. Zhu, A. J. Ochoa, and H. G. Katzgraber, Eﬃcient
cluster algorithm for spin glasses in any space dimension,
Physical Review Letters 115, 077201 (2015).
[83] M. Baity-Jesi, R. A. Ba˜nos, A. Cruz, L. A. Fernandez,
J. M. Gil-Narvion, et al., Critical parameters of the three-
dimensional Ising spin glass, Physical Review B 88, 1
(2013).
[84] K. Binder and A. P. Young, Spin glasses: Experimental
facts, theoretical concepts, and open questions, Reviews
of Modern Physics 58, 801 (1986).
[85] N. Kawashima and A. Young, Phase transition in the
three-dimensional Ising spin glass, Physical Review B 53,
484 (1996).
[86] M. Newman and G. Barkema, Monte Carlo Methods in
Statistical Physics (Clarendon Press, 1999).
[87] H. Rieger and N. Kawashima, Application of a continuous
time cluster algorithm to the two-dimensional random
quantum Ising ferromagnet, European Physical Journal
B 9, 233 (1999).
[88] A. D. King, J. Raymond, T. Lanting, S. V. Isakov,
M. Mohseni, et al., Scaling advantage over path-integral
Monte Carlo in quantum simulation of geometrically
frustrated magnets, Nature Communications 12, 1113
(2021), code: https://github.com/dwavesystems/dwave-
pimc.
[89] M. Palassini and S. Caracciolo, Universal Finite-Size
Scaling Functions in the 3D Ising Spin Glass, Physical
Review Letters 82, 5128 (1999).
[90] M. Hasenbusch, A. Pelissetto, and E. Vicari, Critical be-
havior of three-dimensional ising spin glass models, Phys-
ical Review B 78, 214205 (2008).
[91] O. Melchert, autoScale.py - A program for automatic
ﬁnite-size scaling analyses:
A user’s guide (2009),
arXiv:0910.5403v1.
[92] P. Kairys, A. D. King, I. Ozﬁdan, K. Boothby, J. Ray-
mond, A. Banerjee, and T. S. Humble, Simulating the
Shastry-Sutherland Ising Model Using Quantum Anneal-
ing, PRX Quantum 1, 020320 (2020).
[93] A. D. King, C. Nisoli, E. D. Dahl, G. Poulin-Lamarre,
and A. Lopez-Bezanilla, Qubit spin ice, Science 373, 576
(2021).
[94] S. V. Isakov, I. Zintchenko, T. Rønnow, and M. Troyer,
Optimised simulated annealing for Ising spin glasses,
Computer Physics Communications 192, 265 (2015).

## Page 10

METHODS

Spin-glass instances

The 3D lattices have open x and y dimensions and peri-
odic z dimension. Instances up to size 9×9×9×2 (L = 9)
are fully yielded, with no site vacancies. Larger instances
have over 99.5% site yield. The inputs are heuristically
embedded into the qubit connectivity graph of the QA
processor, with a structure shown in Extended Data E2.
Input construction is discussed in detail in the supple-
mentary material.

Quantum annealing system and methods

All QA data, except speciﬁcally indicated tempera-
ture variation experiments discussed in the supplemen-
tary material, were taken using one D-Wave Advan-
tage system operating at 12 mK (QPU1). The variable-
temperature experiments were performed using a second
D-Wave Advantage system of the same design, between
12 mK and 21 mK (QPU2).
Calibration reﬁnement methods were used to balance
qubits at degeneracy and to synchronize annealing lines.
We follow the same method as described in the supple-
mentary materials for Ref.32, but with no tuning of cou-
pling strengths. We describe these methods in detail in
SM VII.
Each call to the QA system resulted in 200 anneals.
QA data on 3D spin glasses are generated from 900 calls,
cycling through 300 disorder realizations. For MC meth-
ods, between 100 and 300 realizations were used. Thus
the data points for ⟨q2⟩, U, and ρE represent the av-
erage over between 100 and 300 spin-glass realizations,
with error bars capturing variation between instances.
QA Binder cumulants were computed by comparing over-
lap between annealing samples generated in diﬀerent QA
calls but the same seed and embedding, thus suppressing
the eﬀect of correlated biases. The experiments were suf-
ﬁciently extensive that the Binder cumulants and over-
laps computed from samples within the same QA pro-
gramming give similar results.

Measuring annealing time

The anneal of the Hamiltonian from s = 0 to s = 1 over
annealing time ta is achieved through a rapid change in
qubit control current. Of the factors limiting the mini-
mum value of ta, two are most important: First is the
ability to reliably quench s at a known rate and with
tolerable nonlinearity and distortion from ﬁltering; sec-
ond is the ability to synchronize the qubits to within a
reasonable deviation in terms of s.
Annealing times slower than 20 ns are reliably realized.
Annealing times faster than 20 ns deviate signiﬁcantly

from their requested values due to lowpass ﬁlter band-
width and resolution of digital control electronics, and
must be measured independently. We do so in two ways.
The recent demonstration of the KZ mechanism in a 1D
Ising chain32 showed very good agreement with theory, in
particular a scaling of residual energy ρf
E ∝t−1/2
a
. There-
fore extrapolating 1D chain data from ta = 20 ns to faster
anneals provides a reliable measurement of eﬀective an-
nealing time. The second measurement we perform is a
direct measurement in which one qubit is quenched and
measured by a witness qubit, allowing us to estimate the
eﬀective annealing time.
Data for these two measure-
ments are compared in Extended Data E3. We take the
average of the two measurements as our value of ta. Error
bars are obtained by adding, in quadrature, the diﬀerence
between the two measurements and the deviation in an-
nealing slope before and after software ﬁltering (< 0.05
relative error).

Quantum annealing schedule

Simulating the time-dependent Schr¨odinger equation
requires an accurate annealing schedule (Γ(s), J (s)). To
achieve this, we diagonalize a time-dependent many-body
ﬂux-qubit Hamiltonian for a small representative system
of coupled qubits, using a ﬂux-qubit model55 whose pa-
rameters are given in Extended Data E4. Then, for each
s in our range of interest, we compute Γ(s) and J (s)
as best-ﬁt parameters that give an Ising model whose
eigengaps closely match those of the diagonalized super-
conducting quantum interference device (SQUID) Hamil-
tonian.

Diagonalizing the many-body ﬂux-qubit Hamiltonian
to high accuracy is computationally challenging even at
small scales because the ﬂux qubits have multiple en-
ergy levels, unlike the model two-level Ising spins. Thus
as a representative system we take eight qubits, and di-
vide them up into four dimers such that the two qubits
in each dimer have similar interactions with the other
qubits. We then treat each dimer as a six-level object,
and diagonalize the system of four dimers.

Reﬂecting the frustration in spin glasses, our eight-spin
system, shown in Extended Data E5, has frustration in
its twofold-degenerate classical ground state. Performing
a two-parameter ﬁt with Γ(s) and J (s) becomes numer-
ically unstable for s > 0.40 due to the small ﬁrst gap.
For s > 0.40 we ﬁt Γ(s) to the expected exponential
decay form and extract only J (s) as a ﬁtting parame-
ter. Extended Data E5 shows the nominal and extracted
schedules.

## Page 11

Classical Monte Carlo dynamics

Simulated annealing

SA uses a geometric annealing schedule from β =
0.001JG to β = 10JG.
Each MCS processes N spins,
sampled randomly with replacement. Spin updates are
accepted or rejected in a Metropolis-Hastings algorithm.

Simulated quantum annealing

SQA uses an annealing schedule based on the QA
schedule; to accelerate our experiments we begin when
Γ/J ≈6—a fast-equilibrating regime where we assume
the system is quasistatic with respect to the changing
Hamiltonian—and perform 10 MCS before proceeding
through the QA schedule until Γ/J ≈1/25, far into the
ordered phase for the models studied. Inverse tempera-
ture β, which is 64 except where speciﬁed, is relative to
Γ(s) = J (s) at the crossing point of Γ and J . Swendsen-
Wang cluster updates are used in imaginary time.

Time-dependent Schr¨odinger evolution

For the data in Fig. 2 we used an iterative method that
follows the annealing schedule from s = 0.1, where the
QA wavefunction ψ is concentrated on the instantaneous
ground state, and s = 0.7, where dynamics are negligi-
ble. We track populations for only the lowest 80 of 216

eigenstates; this exceeds the number of ground and ﬁrst
excited states for the classical models studied. Step sizes
in s are determined adaptively based on the minimum
eigengap, and range between 0.00008 and 0.01.

Statistical methods and error analysis

Error bars on the order parameter ⟨q2⟩, Binder cumu-
lant U, and residual energy ρf
E were generated by treat-
ing each random seed as an independent experiment and
performing a resampling bootstrap on the set of statis-
tics. This bootstrapping method gives a population for
each statistic estimate. We use this population in two
ways. First, we take the middle 95% of the population
as our conﬁdence interval for the statistic. Second, from
the population we compute a variance on the logarithm,
which we use to determine error weights for our data
collapses.

Data collapse

To collapse measurements of the Binder cumulant U
for varying system sizes onto a common target curve, we
need to ﬁnd a best-ﬁt value for µ.
This ﬁt minimizes

a weighted sum of squared distances (in the logarithm)
from the target curve. Weights in the sum are inversely
proportional to the variance of the logarithm of the es-
timator. The form of the target curve must capture a
crossover between the power-law form of the KZ regime
and the equilibrium (ta →∞) limit. To achieve this, for
each putative value of µ we ﬁnd a best-ﬁt target curve
(nested within the µ-optimizing method) whose power-
law slope varies as a logistic function. Our target curve
has the form

f(x) = a0 + a1 log(1 + exp(a2(x −a3))),
(14)

which ﬁts log(U) as a function of log(ta).
To generate error estimates for µ we perform a jack-
knife on the measurements in L and ta and add the re-
sulting standard errors in quadrature. To approximate
the 95% C.I. in the data points we use error bars that
span ±2σ.
Collapse in ⟨q2⟩is achieved with the same approach.
Selection of ranges of ta over which we collapse data is
described in the supplementary material.

DATA AVAILABILITY

The data supporting the ﬁndings are being prepared
for deposition in an online repository, and are currently
available upon request.

CODE AVAILABILITY

An
open-source
version
of
the
SQA
code
used
in this work is available at https://github.com/
dwavesystems/dwave-pimc.

## Page 12

100

100

a

Schrödinger probability

Schrödinger probability

10−1

10−1

10−2

10−2

10−3

10−3

10−4

10−4

10−5 10−4 10−3 10−2 10−1 100
10−5

100

Schrödinger probability

10−1

10−2

10−3

10−4

10−5 10−4 10−3 10−2 10−1 100
10−5

QA probability

100

100

10−1

10−1

SA probability

SA probability

10−2

10−2

10−3

10−3

10−4

10−4

10−5 10−4 10−3 10−2 10−1 100
10−5

10−5 10−4 10−3 10−2 10−1 100
10−5

QA probability

QA probability

100

10−1

SA probability

10−2

10−3

10−4

10−5 10−4 10−3 10−2 10−1 100
10−5

QA probability

100

100

10−1

10−1

SQA probability

SQA probability

10−2

10−2

10−3

10−3

10−4

10−4

10−5 10−4 10−3 10−2 10−1 100
10−5

10−5 10−4 10−3 10−2 10−1 100
10−5

QA probability

QA probability

100

10−1

SQA probability

10−2

10−3

10−4

10−5 10−4 10−3 10−2 10−1 100
10−5

QA probability

b

1

Empirical CDF

0.5

10−5 10−4 10−3 10−2 10−1 100
10−5

QA probability

QA probability

10−1
100
0

KL divergence

Extended Data E1. State probabilities for 16-spin glasses. a, We show observed probabilities for ground states and
ﬁrst excited states in Schr¨odinger evolution (ta = 14 ns), SA (ta = 200 MCS), and SQA (ta = 100 MCS) compared with
experimental measurements from QA (ta = 14 ns). The three columns contain data for the three exemplary instances, with
colors corresponding to those in Fig. 2. Annealing times for SA and SQA were chosen to have good agreement with Schr¨odinger
evolution in average ground state probability. Each dynamics was run 19,200 times; dashed lines indicate the statistical ﬂoor,
i.e., the probability if a state is seen exactly once. Unobserved states are represented by points below the statistical ﬂoor.
b, Kullback-Leibler (KL) divergence in the probability distribution among ﬁrst excited states, with QA used as a reference
distribution, measures deviation between two dynamics for a given realization. Empirical CDF (proportion of 100 realizations
below a given KL divergence) is shown. Data indicate that coherent quantum (Schr¨odinger) dynamics agrees more closely with
experimental data better than does SA or SQA.

## Page 13

1
2z+

1
2z+

Extended Data E2. 3D lattice structure in qubit connectivity graph. L × L × (max(L, 12)) × 2 lattices are found by
heuristic search given a basic structure in which horizontal and vertical (long) couplings form two dimensions, and the interior
of unit cells forms the third dimension. One dimer (thick gray line) and its six neighboring dimers are shown as thick gray
lines. As in Fig. 1, purple and yellow lines represent glass couplings of ±JG and ±JG/2 respectively.

30

20

Measured ta (ns)

10

5

5
10
20
30

Requested ta (ns)

Extended Data E3. Measurement of eﬀective QA annealing time. Two independent measurement methods are used
to estimate ta for fast anneals (< 20 ns). First is a direct measurement using a witness qubit. Second is an extrapolative
measurement that assumes a quantum KZ scaling in a 1D chain and assumes a kink density n ∝t−1/2
a
for ta < 20 ns. For the
fastest anneals, ta deviates signiﬁcantly from the values requested from the control electronics. However, the two independent
measurement approaches give consistent results.

## Page 14

Extended Data E4. Physical properties for the QA processor.

a
b

Jij = −1
Jij = 1

s

Extended Data E5. Extracting Ising model from ﬂux-qubit model. a, Eight-qubit gadget used to extract an eﬀective an-
nealing schedule in the transverse-ﬁeld Ising model based on a many-body ﬂux-qubit Hamiltonian. Dimers indicated by dashed
ellipses are treated as six-level objects and combined to diagonalize a many-body Hamiltonian. b, General-purpose (nominal)
annealing schedule based on single-qubit measurements, and extracted many-body eﬀective schedule, used for Schr¨odinger
evolution.

## Page 15

SA

10−1

10−1

⟨q2⟩

U

10−2

⟨q2⟩Lr

10−1

μ = 5.23(21)
r = 0.46(9)

10−2

10−3
10−2
10−1
100
101

103
104
105

ta (MCS)
taL−μ (MCS)

SQA

10−1

10−1

⟨q2⟩

U

10−2

10−2

10−3
10−2
10−1
100
101
10−2

103
104
105

ta (MCS)
taL−μ (MCS)

10−1

⟨q2⟩Lr

10−2

μ = 4.09(11)
r = 0.25(7)

10−2
10−1
100

102
103

ta (MCS)
taL−μ (MCS)

QA

10−1

10−1

⟨q2⟩

U

10−2

10−2

10−2
10−1
100

102
103

ta (MCS)
taL−μ (MCS)

10−1

⟨q2⟩Lr

10−2

μ = 3.11(10)
r = 0.11(09)

10
20
30

10−2
10−1

ta (ns)
taL−μ (ns)

10
20
30

10−2
10−1

ta (ns)
taL−μ (ns)

Extended Data E6. Data collapse for 3D spin glasses with JG = 1. Best-ﬁt exponent µ collapses U by rescaling data
horizontally based on L, and r collapses ⟨q2⟩by scaling vertically based on L, given a horizontal rescaling by L−µ.

## Page 16

SA

10−1

10−1

⟨q2⟩

U

10−2

10−2

10−0.5

⟨q2⟩Lr

10−1

10−1.5

μ = 5.37(16)
r = 0.65(7)

103
104
105

10−3
10−2
10−1
100
101

ta (MCS)
taL−μ (MCS)

SQA

10−1

10−1

⟨q2⟩

U

10−2

10−2

103
104
105

10−3
10−2
10−1
100
101

ta (MCS)
taL−μ (MCS)

10−1

⟨q2⟩Lr

10−2

μ = 3.73(14)
r = 0.50(9)

102
103
10−3

ta (MCS)
taL−μ (MCS)

QA

10−1

10−2

10−2

⟨q2⟩

U

10−3

102
103
10−3

10−2
10−1
100
101

ta (MCS)
taL−μ (MCS)

10−1

⟨q2⟩Lr

10−2

μ = 2.98(11)
r = 0.54(9)

10
20
30

10−2
10−1

ta (ns)
taL−μ (ns)

10
20
30
10−3

10−2
10−1

ta (ns)
taL−μ (ns)

Extended Data E7. Data collapse for 3D spin glasses with JG = 1/2. Best-ﬁt exponent µ collapses U by rescaling data
horizontally based on L, and r collapses ⟨q2⟩by scaling vertically based on L, given a horizontal rescaling by L−µ.

## Page 17

SA

10−0.5

10−0.5

⟨q2⟩

10−1

U

10−1

10−1.5

100

⟨q2⟩Lr

10−1

μ = 5.98(19)
r = 0.45(7)

10−1.5

10−3
10−2
10−1
100

103
104

ta (MCS)
taL−μ (MCS)

SQA

100

10−1

⟨q2⟩

U

10−1

103
104

10−3
10−2
10−1
100

ta (MCS)
taL−μ (MCS)

100

⟨q2⟩Lr

10−1

μ = 4.39(16)
r = 0.28(9)

10−2

102
103
10−2

ta (MCS)
taL−μ (MCS)
10−3
10−2
10−1
100
10−2

ta (MCS)
taL−μ (MCS)

102
103

10−3
10−2
10−1
100

Extended Data E8. Data collapse for 3D spin glasses on simple cubic lattices. Best-ﬁt exponent µ collapses U by
rescaling data horizontally based on L, and r collapses ⟨q2⟩by scaling vertically based on L, given a horizontal rescaling by
L−µ.

## Page 18

Supplementary Materials:
Quantum critical dynamics in a 5000-qubit programmable spin glass

CONTENTS

I. Finite-size scaling
19
A. Equilibrium ﬁnite-size scaling
19
1. Classical phase transitions
19
2. Quantum phase transitions
23
B. Dynamic ﬁnite-size scaling
25
C. Application to annealing experiments and simulations
27
1. Spin glass order parameter
28
2. Scaling of the spin-glass order parameter
29
3. The Binder ratio
30
4. Residual Ising energy
31

II. 3D spin glasses
32
A. Construction
32
B. Broken FM dimers in the 3D ground state
33
C. Estimating ground state energies
33
D. Quantum and classical phase transitions
34

III. Equilibrium analysis of critical phenomena by Monte Carlo methods
34
A. Finite-size scaling in classical and path-integral models
35
B. Monte Carlo sampling
35
C. Classical critical scaling
36
D. Quantum critical scaling
36

IV. Nonequilibrium dynamics of SA and SQA
39
A. Freezing of dynamics in SA
39
B. Energy decay at the critical point and inside the glass phase
39

V. Data collapse domains
40

VI. Eﬀect of temperature on QA
40

VII. Calibration reﬁnement
40

VIII. Residual energy decay
42

## Page 19

I.
FINITE-SIZE SCALING

Here we provide the required background on the dynamic ﬁnite-size scaling (FSS) ansatz used in this work. The
main goal is to justify the extraction of the KZ exponent µ by collapsing, as in Fig. 2, the Binder cumulant U for
multiple annealing times and system sizes, as well as the exponent κf of the power law quantifying the reduction in
excess energy with increasing annealing time in Fig. 4. Since the annealing process stops inside the glassy phase not
only for QA, but also in this work for SA and SQA, our analysis here must go beyond the simplest case of dynamic
scaling at a critical point. We will show that many aspects of KZ scaling remain valid under the circumstances
prevailing in the annealing experiments conducted here, including the power-law forms governed by the exponent µ,
even though the order parameter evolves beyond its critical form.
There are many excellent reviews of conventional critical phenomena and ﬁnite-size scaling, e.g., Refs.56,57, but for
ease of reference in the later sections we begin in Sec. I A by a concise summary. In particular, we explain the relation-
ships between the conventional critical exponents and the scaling dimensions appearing within the renormalization
group (RG) framework. The classical case of transitions driven by thermal ﬂuctuations at critical temperature Tc > 0
is considered ﬁrst, followed by the formally simple generalization to quantum phase transitions, where the ground
state (Tc = 0) of a system changes as a function of a model parameter regulating the quantum ﬂuctuations. In Sec. I B
we review the extensions of the ﬁnite-size scaling formalism to the case of a system brought through a classical or
quantum phase transition by an annealing process, where the annealing rate regulates the correlation length by the
KZ mechanism and there is a generalized FSS ansatz involving both the system size and the annealing rate. There are
also extensive reviews of this topic, e.g., the very recent Ref.58; here we outline the formalism underlying our analysis
of simulations and experimental data. In Sec. I C, we focus on the particular conditions pertaining to the quantum
annealing device and how some aspects of critical scaling can persists also when driving the system past the quantum
phase transition into an ordered (here glassy) state.

A.
Equilibrium ﬁnite-size scaling

1.
Classical phase transitions

Consider a system described by some Hamiltonian H at a short distance δ = T −Tc away from a classical continuous
phase transition with critical temperature Tc.
There is a characteristic length scale in the inﬁnite system, the
correlation length ξ governed by the exponent ν > 0,

ξ ∝δ−ν,
(S1)

where the divergence takes place for δ →0 both from above and below (and for δ < 0 the absolute value |δ| is implied
here and henceforth in similar power laws). Also consider some other quantity n (an expectation value of, typically,
a volume-normalized density) that in the thermodynamic limit is governed by another critical exponent σ,

n ∝δσ,
(S2)

where σ depends on the quantity n and the universality class of the transition.
For example, if n is the order
parameter, n = ⟨m⟩, then in the conventional nomenclature σ ≡β. The expectation value ⟨.⟩involves also averaging
over realizations in a system with some type of intrinsic disorder, like the spin glasses of interest here.
On a ﬁnite lattice with d spatial dimensions and volume N = Ld, the singular behavior breaks down when the
correlation length becomes of the order of L. According to FSS theory56,57,59, for ﬁnite L the critical form (S2) should
be replaced by

n = L−σ/νg(δL1/ν),
(S3)

where the scaling function g(x) has the property g(x) →constant when x →0. In order for the form (S2) in the
thermodynamic limit to be recovered when L →∞(at ﬁxed small δ), the large-x limit of g(x) must be of the form

g(x) →xσh(x),
(S4)

where h(x) →constant when x →∞. Then there is no longer any L dependence of Eq. (S3) and the correct exponent
on δ in Eq. (S2) is obtained.
In the case n = ⟨m⟩, it should be noted that a ﬁnite system does not break any symmetry spontaneously; thus
⟨m⟩= 0 for any ﬁnite L at any temperature. This apparent problem can be easily circumvented by considering

## Page 20

the squared order parameter ⟨m2⟩, which vanishes with increasing L for T ≥Tc and approaches the square of the
inﬁnite-size order parameter for T < Tc. The FSS form Eq. (S3) holds for ⟨m2⟩in the neighborhood of Tc, with
σ = 2β.
The critical exponents can be related to the RG scaling dimensions appearing in ﬁeld theory60.
Consider an
extensive operator P (a function of the system’s degrees of freedom) deﬁned as a sum over the entire system of local
density operators p(r);

P =
X

r
p(r).
(S5)

If this operator is added with some factor δp to the Hamiltonian at T = Tc, H →H +δpP, the system would typically
be driven away from the critical point and critical scaling forms such as those discussed above for ξ and n will apply
with δ →δp. The factor δp is referred to as the ﬁeld conjugate to P.
Classical statistical mechanics relies on the Boltzmann weight e−H/T . At T = Tc, if the perturbing operator P
is just the Hamiltonian itself, H →H + δH, the oﬀset δH is equivalent to just shifting the inverse temperature,
1/T = (1/Tc)(1+δ) with H kept unchanged. Therefore, instead of shifting H we consider deviations from the critical
temperature Tc and refer to δ = T −Tc as the thermal ﬁeld. Strictly speaking δ is the conjugate ﬁeld to the entropy
S, which appears in the free energy F = E −TS along with the internal energy E = ⟨H⟩. By the reverse of the above
arguments, we can also regard 1/T −1/Tc ≈−δ/T 2
c as the conjugate ﬁeld to H. Not worrying about factors, we can
say that δ is the ﬁeld conjugate to both the entropy and the internal energy.
A ﬁeld of strength δp conjugate to an arbitrary operator P is associated with a scaling dimension yp = 1/νp
governing ﬁnite-size forms such as Eq. (S3),

n = L−σ/νg(δpLyp),
(S6)

when perturbing the critical system by an arbitrary interaction δpP. In the above case of just changing the temper-
ature, the thermal exponent νt is conventionally just called ν as in Eqs. (S1) and (S3), and for simplicity we also do
not attach any subscript on δ = t ≡T −Tc. It is important to note that the symmetry of the system does not change
when the temperature is changed, and δ is therefore also referred to as a symmetric scaling ﬁeld.
For generic perturbations P, the symmetry of H(δp ̸= 0) can be lower than that of H(0), e.g., in the common case
of P = M, where ⟨m⟩= ⟨M⟩/N is the order parameter density of a system hosting a symmetry-breaking transition.
For instance, in the ferromagnetic Ising model, M is the total magnetization and δm is the external magnetic ﬁeld.
Thus, the spin-inversion symmetry is violated when δm ̸= 0, and when δm = 0 the system spontaneously breaks the
symmetry, ⟨m⟩̸= 0, for T < Tc in the thermodynamic limit.
It should be pointed out that a microscopic ﬁeld strength δp is never strictly speaking equivalent to the scaling ﬁeld
deﬁned in a continuum theory. The term δpP that we add (or imagine adding) to the Hamiltonian can be thought of
as consisting of an inﬁnite sum of operators Oj multiplied by their conjugate scaling ﬁelds λj,

δpP =
X

j
λjOj,
(S7)

and these ﬁelds enter scaling functions in the form λjLyj in the same way as in Eq. (S6). More precisely, the equality
above should be interpreted as a correspondence between the lattice operator P and operators Oj in a continuum
ﬁeld theory. If yj > 0 the ﬁeld λj (and operator Oj) is said to be relevant, as its eﬀect increases with the system size
(λjLyj →∞when L →∞), and, conversely, yj < 0 for an irrelevant ﬁeld (λjLyj →∞, with the marginal case yj = 0
is associated with logarithmic scaling corrections, which we will not discuss here).
Naturally the ﬁelds λj in Eq. (S7) are proportional to δp when the latter is small, but they also depend on other
parameters of a given model and the full form is nonlinear61, which causes corrections to scaling when taken into
account in FSS forms such as (S6). Here we neglect the scaling corrections that can (depending on the kind of analysis
performed) be generated by the nonlinear scaling ﬁeld, and, since constants of proportionality are not important, we
can use δp as the scaling parameter. The scaling dimension yp in Eq. (S6) corresponds to the largest among the yj
values of the ﬁelds λj in (S7), and normally we just refer to this yp as the scaling dimension of δp even though, strictly
speaking, this is only the leading scaling dimension.
We typically consider a transition tuned by the thermal ﬁeld δ, but scaling theory in principle relies on the possibility
of arbitrary perturbations of the critical system.
A key fact is that, in the entire space of possible inﬁnitesimal
deformations of H, there is only a small number of relevant ﬁelds (just δ ≡δt and δm in the most common case,
with multi-critical points having additional relevant ﬁelds), whose inﬁnitesimal presence destabilize the critical point.
Adding an irrelevant ﬁeld δi just extends the critical point at (δ = 0, δm = 0) to a line of critical points in the
parameter space, with the universality class not aﬀected. In practice, most lattice operators would contain all the

## Page 21

scaling ﬁelds (conjugate to continuum ﬁeld operators) allowed by symmetry, and adding them at weak strength to
H only changes the location of the critical point, again without changing the universality class. A simple example
is the Ising model with next-nearest-neighbor interactions J′ added to the conventional model with nearest-neighbor
interactions J, where Tc depends on J and J′ but the universality class of the J-only model persists (unless J and J′

are strongly frustrated, whence other phases and transitions are realized62).
A related important point is that it is normally only by symmetry that a given lattice operator P can be guaranteed
to contain a single relevant ﬁeld. In the Ising model, a change in temperature (conjugate to P = H) at zero external
ﬁeld only corresponds to “touching” the thermal ﬁeld.
However, at the critical point of water (which is also of
Ising type), changing the temperature (or the pressure) touches both the thermal ﬁeld and the order-parameter ﬁeld,
because there is no microscopic symmetry like the spin-inversion symmetry of the Ising model (though such symmetry
eﬀectively emerges close to the critical point). Spin models in general have the advantage that the thermal ﬁeld and
the order parameter ﬁeld can be separated thanks to symmetry.
In addition to the scaling ﬁelds δp, the local operators p(r) in Eq. (S5) are also associated with their own scaling
dimensions ∆p, which can be concretely deﬁned in terms of the asymptotic distance dependence of the corresponding
real-space correlation function at the critical point,

Cp(r) = ⟨p(r)p(0)⟩−⟨p⟩2 ∝
1
r2∆p ,
(S8)

where, depending on the operator, ⟨p⟩(same as ⟨p(r)⟩in a uniform system or in a system with randomness when
averaged over realizations) may or may not vanish. More precisely, each operator in the sum (S7) has its own scaling
dimension and ∆p is the smallest of these, i.e., (S8) represents the leading form of the correlations.
In the case of the order parameter, P = M, ⟨m⟩= 0 at Tc and the exponent 2∆m is related to the conventional
critical exponents by

2∆m = 2β/ν = d −2 + η,
(S9)

where η is called the anomalous dimension. Normally this kind of relationship is not used for any other operator
besides the order parameter, and no subscript is therefore attached to β and η.
The ﬁrst equality in Eq. (S9) follows from writing the squared order parameter ⟨m2⟩= ⟨M 2⟩/N 2 as a sum (converted
to an integral) of the order-parameter correlation function ⟨m(r)m(0)⟩over r up to a cut-oﬀlength L, which gives
⟨m2⟩∝L−2∆m from the form analogous to Eq. (S8). Then, comparing with Eqs. (S2) and (S3), where by deﬁnition
σ = 2β, the equality follows. The second equality in Eq. (S9) can be regarded as the deﬁnition of η, but this exponent
is also fundamentally related to the fractal dimensionality of critical domains in the system.
One can show, as we will below, that the scaling dimensions yp and ∆p are related to each other by

yp ≡1

νp
= d −∆p.
(S10)

If δp drives the transition (typically but not necessarily by changing the temperature, whence δp = δ and yp = 1/ν),
the FSS ansatz (S6) of an observable n in the neighborhood of the critical point can be expressed using the scaling
dimension yp of the driving ﬁeld and the scaling dimension ∆n of the observable n;

n(L, δp) = L−∆ng(δpLyp).
(S11)

Again, more precisely, ∆n is the smallest of the scaling dimensions of all operators in ﬁeld theory that may be
contained in the lattice operator n.
It should be noted that the correlation function (S8) from which a scaling dimension can be extracted may also
include a phase depending on r.
As a simple example, in a square-lattice antiferromagnet the sign of the spin
correlation function ⟨S(r)S(0)⟩is (−1)rx+ry, where rx and ry are the (integer) lattice coordinates. For simplicity we
do not consider any such phases here, but they can be easily handled by, e.g., considering absolute values. For the
order parameter M deﬁned using a sum of local operators as in Eq. (S5), a corresponding phase should then also
be included, i.e., the Fourier transform should be taken at the relevant ordering wave-vector, which is (π, π) in the
above case of the antiferromagnet with local operators S(r). These phases do not in any other way aﬀect the scaling
formalism discussed here, and we will assume that they are taken into account if needed.
In the common case of a simple critical point with only two relevant perturbations, we can extend the FSS form
Eq. (S11) of an observable to

n = L−∆ng(δL1/ν, δmLym, δiL−|yi|, . . .),
(S12)

## Page 22

where δi is just the ﬁrst of an inﬁnite number of irrelevant scaling ﬁelds that are normally present, δi ̸= 0, and
additional relevant ﬁelds are present at multi-critical points. An irrelevant ﬁeld has scaling dimension yi < 0 and only
produces ﬁnite-size scaling corrections in Eq. (S11), as seen when Taylor expanding in the argument δiLyi = δiL−|yi|

when L is suﬃciently large. Here we will henceforth neglect irrelevant ﬁelds and scaling corrections.
The most fundamental among the ﬁnite-size scaling forms in classical statistical mechanics is that of singular part
of the free-energy density f, which has scaling dimension equal to the system’s dimensionality, ∆f = d (for reasons
that we do not further motivate here but refer to the literature59,60,63);

f = L−dg(δL1/ν, δmLym, . . .).
(S13)

Scaling forms for arbitrary physical observables can be derived from this free-energy density by taking appropri-
ate derivatives with respect to added perturbations. As an example, the magnetization (the order parameter of a
ferromagnet for simplicity) is the derivative of f with respect to the magnetic ﬁeld h = δm,

∂δm
= L−d+ymg′(δL1/ν, δmLym),
g′(x, y) = ∂g(x, y)

⟨m⟩= ∂f

∂y
,
(S14)

where we see that, as implied by Eq. (S10), indeed ∆m = d −ym. Setting δ = 0 and taking L →∞we can argue, in
analogy with Eq. (S4), that the function g′ must become a power law; g′ →(δmLym)x, where the exponent must take
the value x = ∆m/ym = ∆m/(d−∆m) so that the size dependence is eliminated. Thus, ⟨m⟩= δx
m. In the conventional
nomenclature x is called 1/δ, which conﬂicts with our notation for the thermal ﬁeld. Therefore, continuing to use x
for this exponent here, we have the well known relationship 1/x = (dν −β)/β.
Another important case is when n in Eq. (S12) is the internal energy density E/N = ⟨H⟩/N. In this case, the
inﬁnite-size critical value (which by deﬁnition is its regular part) also has to be subtracted, and we deﬁne the singular
part of the energy density as (now for simplicity considering the tuning only of the thermal ﬁeld δ)

ρE(L, δ) = E(L, δ)/Ld −lim
ℓ→∞E(ℓ, 0)/ℓd.
(S15)

This residual energy density has the ﬁnite-size critical form ρE = L−∆eg(δL1/ν). Since, as discussed above, the
energy is conjugate to the thermal ﬁeld, we must have ∆e = d −1/ν by Eq. (S10). Therefore, in the thermodynamic
limit ρE ∝δdν−1, from which we can easily obtain the more often considered critical form of the speciﬁc heat:
c = dρE/dδ ∝δdν−2. The exponent governing the speciﬁc heat is customarily called α, and we see that the well
known exponent relation α = dν −2 is obtained.
An energy-energy correlation function Ce(r) deﬁned with local energy density operators e(r) can in principle be
used to determine the correlation-length exponent ν in numerical model simulations. At the critical point

Ce(r) ∼
1
r2∆e =
1
r2(d−1/ν) .
(S16)

Since the expectation value of the energy does not vanish, the correlation function is deﬁned with a subtraction of
⟨E(∞, 0)/N⟩2, or, equivalently, the operators e(r) can be deﬁned with E(∞, 0)/N subtracted.
In practice, it is often easier to determine ν using the ﬁnite-size scaling form (S11), preferably with some dimen-
sionless quantity n (∆n = 0), e.g., one of the Binder ratios Rk deﬁned by

Rk = ⟨m2k⟩

⟨mk⟩2 ,
(S17)

for which the scaling dimensions cancel. Data for Rk (normally with k = 2) versus x = (T −Tc)L1/ν for diﬀerent
T (suﬃciently close to Tc) and L (suﬃciently large) then collapse onto the common scaling function g(x), provided
that Tc and ν have their correct values.
These values can be determined by optimizing the quality of the data
collapse. Alternatively, Tc can be obtained by investigating the ﬂow of crossing points T12 = T(L1, L2) for which
Rk(L1, T12) = Rk(L2, T12) for diﬀerent system size pairs (L1, L2), e.g., L1 = L, L2 = 2L. The slope dRk/dδ at Tc
scales as L1/ν and can be used once Tc has been determined, or the maximum slope for each L can be used in the same
way even without prior knowledge of Tc. The location (temperature) of the maximum, or any feature in a quantity
governed by a scaling form such as Eq. (S3), shifts with L as L1/ν. Details of the practicalities of ﬁnite-size scaling
have been discussed extensively in the literature, and in Sec. III we illustrate procedures in our application to the
classical 3D spin glass.
The above formalism and scaling methodology also apply to a quantum system undergoing a phase transition at a
critical temperature Tc > 0, because the ﬂuctuations at the longest (diverging) length scale are always thermal unless
T = 0. Quantum ﬂuctuations can drive continuous transitions with Tc = 0, as we discuss next.

## Page 23

2.
Quantum phase transitions

A quantum system in d spatial dimensions can be mapped through the path integral approach to an eﬀective
statistical-mechanics system with an additional imaginary-time dimension60,64. In some cases, this eﬀective system
is space-time isotropic beyond a simple scale factor (a velocity) that relates space and time, but in general the
time dimension is very diﬀerent. The diﬀerence is quantiﬁed by the dynamic exponent z, which relates the spatial
correlation length ξ to a relaxation time ξτ (a correlation length in imaginary time) according to ξτ ∝ξz. A critical
real-space correlation function C(r) ∝r−a translates by r →τ 1/z into a corresponding critical time correlation
function C(τ) ∝τ −a/z.
In scaling dimensions and relationships where the dimensionality appears, the classical
spatial dimensionality d should be replaced by d + z (where we still use d for the spatial dimensionality of the
quantum system), following from the scaling dimension of the Hamiltonian density at T = 0 (which replaces the
classical free-energy density at T > 0). With these generalizations, the formalism discussed in the preceding section
remains valid, with important extensions described below.
A classical phase transition takes place at Tc > 0 as a consequence of competition between the internal energy and the
entropy. As discussed in the preceding section, the energy and the entropy can both be regarded as conjugate quantities
to the temperature, which we call the thermal ﬁeld when given relative to the critical temperature; δ = T −Tc. In
a quantum system at T = 0 it is instead the competition between diﬀerent terms in the Hamiltonian that cause
the ground state transition. The ﬂuctuations that allow for a continuous transition can in this case be traced to
non-commuting terms of the Hamiltonian, leading to quantum ﬂuctuations when the ground state is expressed in
some local basis, e.g., with the spin-z eigenvalues Sz
i (i = 1, . . . , N) in a spin system.,
The quantum ﬂuctuations are regulated by changing some model parameter. A non-trivial Hamiltonian can always
be formally decomposed into two non-commuting terms, H = aHA + bHB, so that the transition of the ground state
is driven by relative changes in the prefactors a and b. Since an overall factor does not matter for the ground state
wave function, we can ﬁx b = 1. Then we can deﬁne the critical Hamiltonian Hc and consider deviations from it by
tuning the parameter a only (for simplicity):

H(δa) = Hc + δaHA.
(S18)

Assuming that this tuning does not change the symmetry of H (i.e., Hc and HA have exactly the same symmetries,
which normally is apparent), δa is the symmetric scaling ﬁeld whose inverse scaling dimension deﬁnes the conventional
correlation length exponent ν. Thus, if HA consists of a sum of local terms hA(r) in the same way as the generic
perturbing operator P in Eq. (S5), we can deﬁne the correlation function, evaluated at δa = 0, and its asymptotic
power-law form will be dictated by the scaling dimension of the operator as in the classical case:

CA(r) = ⟨hA(r)hA(0)⟩−⟨hA⟩2 ∝
1
r2∆a .
(S19)

Then, in a generalization of the classical relationship Eq. (S10) between scaling dimensions, the correlation-length
exponent ν = 1/ya is given by

1
ν = d + z −∆a.
(S20)

Here it should be noted that, we can also go away from the critical point by letting H = Hc + δbHB, and, therefore,
the scaling dimensions of the operators HA and HB must be the same; ∆a = ∆b. Since it does not matter what term
is tuned, we will also just use δ without subscript for the deviation from the critical point. Similarly, we do not attach
any index on ν when there is a single relevant symmetric ﬁeld, i.e., at a regular critical point that can be reached by
tuning a single parameter in H.
The dynamic exponent z governs the low-energy excitations of the system, with the dispersion (energy–momentum)
relation ϵk ∝kz and a ﬁnite-size gap

∆L ∝L−z.
(S21)

This gap scaling corresponds directly to the scaling dimension of the total Hamiltonian H being z, i.e., the ground-state
energy density has scaling dimension d+z. The corresponding quantity in the classical case is the free-energy density
at T > 0, which has scaling dimension d, as stated explicitly in the ﬁnite-size form (S13). Thus, the replacement
d →d + z when converting classical scaling forms (obtained as derivatives of the free energy) to the quantum case
(corresponding derivatives of the ground state energy).
It is important to recognize that the scaling dimension of the total Hamiltonian H = aHa + bHb is diﬀerent from
that of Ha and Hb. The latter two terms can drive a transition, as discussed above, while just changing the overall

## Page 24

quantum-mechanical Hamiltonian by H →H + δhH does not change the ground state. It is interesting to note
that the relationship Eq. (S20) with ∆a replaced by the scaling dimension of the Hamiltonian density, ∆h = d + z,
gives 1/νh = 0. Thus, a scaling form L−∆ng(δhL1/νh) of some operator n under the change of δh reduces to just
n = L−∆ng(δh) without size dependence in g. In many cases the scaling function g(δh) must be a constant, since the
ground state does not depend on δh. An exception is the ﬁnite-size gap, which depends on the overall scale of H,
whence Eq. (S21) can be written as ∆L ∝(1 + δh)L−z, i.e., g(δh) ∝1 + δH.
A quantum phase transition takes place in the ground state, but the path integral representation is valid for any
temperature, and the length Lτ of the d + 1 dimensional system in the imaginary-time dimension is proportional to
the inverse temperature 1/T. Finite-size scaling can in general be formulated with both the spatial size L and the
temporal size Lτ. In order for expectation values to converge to their ground state limits, the temperature has to
be much smaller than the gap; T ≪L−z. This convergence and cross-over from ﬁnite-temperature behavior can be
expressed by an extended scaling function with an argument Lτ/Lz:

n = L−σ/νg(δL1/ν, Lτ/Lz).
(S22)

If z of a system is not known, it can be obtained by analyzing the dependence of some suitable quantity n on L as well
as the inverse temperature scaled with some exponent z′, i.e., 1/T ∝Lτ ∝Lz′. If z′ < z, the argument Lτ/Lz →0
when L increases, while if z′ > z we have Lτ/Lz →∞. Depending on the quantity n, the scaling function behaves
very diﬀerent in these two limits, and the correct value z′ = z can be deduced as a separatrix65. An example of this
type of analysis for the 3D spin glass is presented in Sec. III.
If z is known, the inverse temperature can just be scaled as 1/T ∝Lz and the scaling function (S22) then eﬀectively
has a single argument δL1/ν. In numerical simulations, an alternative approach if z is not a priori known is to study low
enough temperatures so that all ﬁnite-size observables have converged to their ground state values. Then, eﬀectively
the limit Lτ/Lz →∞is taken for each individual L, and again the scaling function in Eq. (S22) becomes one with a
single argument: g(x, y) →˜g(x). As we will see below, the dynamic exponent can still be accessed because it appears
in scaling dimensions when the classical scaling forms are modiﬁed by setting d →d + z.
An important aspect of quantum-critical scaling is that some physical observables are deﬁned at equal time, while
others are integrals over imaginary time. Consider ﬁrst the equal time expectation value ⟨m2⟩of the squared order
parameter, which, following the same procedures as in the classical case, we can express as a correlation function
integrated over r, resulting in ⟨m2⟩∝L−2∆m. Often, this quantity is multiplied by N = Ld for what is called the
static structure factor, and it scales as

Sm = ⟨M 2⟩/N = Ld⟨m2⟩∝Ld−2∆m = L2−z−η,
(S23)

where in the last step we have used the quantum mechanical analogue of Eq. (S9) for the scaling dimension of m2;

2∆m = d + z −2 + η.
(S24)

The scaling form of Sm also formally applies to a classical system by setting z = 0.
The perhaps most well known example of a quantity involving integration over imaginary time τ (a Kubo integral)
is the susceptibility corresponding to the order parameter ﬁeld: χ = d⟨m⟩/dδm In the common case where m = M/N
and H do not commute (e.g., in the case of the transverse-ﬁeld Ising model), we have

Z 1/T

χm ∝1

0
⟨M(τ)M(0)⟩dτ,
(S25)

N

which can be readily demonstrated by writing e−βH (with δmM included in H) in the thermal expectation value ⟨m⟩
as (e−∆τ H)k, with small ∆τ = β/k, so that the δm derivative can be taken properly in each of the factors (“time
slices”) and summed up in the form of an integral when k →∞. In order for the susceptibility to produce scaling
reﬂecting the properties of the ground state (which is the only case we consider here, though ﬁnite-temperature scaling
can also be considered and is an important aspect of quantum criticality64), T has to be below the lowest excitation
gap of the system, which has the scaling form (S21). Thus, the upper integration bound 1/T in Eq. (S25) has to be
of order Lz or larger. Formally the cut-oﬀshould be set at τ ∝Lz even when the limit T →0 is taken, because the
time correlations decay exponentially for τ ≫Lz.
Again writing M as a sum of local operators, now M(τ) = P

r m(r, τ), and integrating C(r, τ) = ⟨m(r, τ)m(0, 0)⟩
over both space and (imaginary) time, we have d spatial coordinates r = (r1, . . . , rd) and a time coordinate τ. The
critical correlation function has the asymptotic form

C(r, τ) =
1
(r2 + τ 2/z)∆m .
(S26)

## Page 25

To integrate this over the anisotropic space-time volume, we can deﬁne rd+1 ≡τ 1/z and use R for the length of the
vector R = (r1, . . . , rd+1). Then all components are integrated up to L, and the scaling form of χ becomes (neglecting
angular integrals that only produce unimportant factors)

χm ∝
Z L
dRRdRz−1

R2∆m
∝Ld+z−2∆m = L2−η.
(S27)

Thus, compared to the structure factor (S23), there is an additional factor Lz arising from the time integral, and the
dynamic exponent can be singled out, e.g., χm/Sm ∝Lz.
There is no obvious classical counterpart to the above scaling form of χm, which is reﬂected in the fact that there
is no z left that can be set to zero, unlike Eq. (S23). The deﬁnition (S25) of the susceptibility can of course still be
used classically, in which case M(τ) = M(0) = M (because M and H commute) and the integral only produces a
factor 1/T. Thus, classically χm = Sm/T, which holds at any temperature.
From Eqs. (S23) and (S27) we see that both the exponents z and η can, in principle, be determined by investigating
the size dependence of the structure factor and the susceptibility. In current quantum annealing devices, only equal-
time quantities are accessible, in the form of the probability distribution of the spin-z conﬁgurations at the end of
the annealing process. This state can contain “memories” of the wave function close to the quantum-critical point,
through the critical slowing-down mechanism ﬁrst discussed by Zurek41,66 in classical statistical mechanics (following
related work on cosmological topological defects by Kibble40) and later generalized to quantum phase transitions as
well42–44. The dynamics of quantum annealing depends on z, thus oﬀering a path to extracting this exponent from
experiments. We next discuss the generalization of FSS to a system undergoing an annealing process, ﬁrst in general
terms and then focusing speciﬁcally on the spin-glass annealing experiments and simulations.

B.
Dynamic ﬁnite-size scaling

In a classical or quantum annealing process in which a parameter like δ varies linearly as a function of time t, the
ﬁnite-size scaling form (S11) attains a second scaling argument;

n = L−∆ng(δL1/ν, vLµ),
(S28)

where v is the velocity by which δ changes, v = dδ(t)/dt taken at δ = 0 (and if v = 0 according to this deﬁnition, the
approach discussed here can be generalized to the second derivative or any higher derivative46,67), and we consider
v > 0 for simplicity. Since constants of proportionality do not matter in scaling forms, we can also simply deﬁne the
scaling velocity as the inverse of the total annealing time; v = 1/ta. The exponent µ controlling the velocity scaling
is deﬁned in the same way as in the main paper;

µ = z + 1/ν.
(S29)

The FSS form (S28) has its origin in the KZ mechanism42–44,66 and its use for analyzing numerical simulation data and
experiments under various dynamical protocols was further elaborated and tested in numerous later works45–47,68,69.
We here assume that the process starts with the system in a disordered phase and approaches an ordered phase,
though the opposite process can also be treated in a similar way. The basic starting point leading to (S28) is that a
ﬁnite system approaching a continuous classical or quantum phase transition at rate v “freezes out” when the remaining
time to reach the critical point is less than the required time for the system to equilibrate. In the thermodynamic
limit, the correlation length reached before the system falls out of equilibrium is similarly

ξv ∝v−1/µ.
(S30)

The argument vLµ in Eq. (S28) is simply a power of the dimensionless ratio L/ξv.
The KZ mechanism is often discussed in terms of defects generated by the out-of-equilibrium dynamics, but in
general, except for some often studied 1D systems, it is not easy to directly relate a defect density to observed
physical quantities. However, the scaling approach relies only on the existence of some dynamic process associated
with a relaxation time ξt, which should be related to a spatial correlation length ξ by ξt ∝ξz. No other information
on the dynamic process or the nature of the defects is required to derive universal scaling forms47,69.
In a quantum system undergoing an annealing process of the type considered here, z is exactly the dynamic
exponent discussed in the previous section. Though there z was introduced in the context of imaginary (Euclidean)
time, the relevant time scale is the same in real and imaginary time: ξt ∝ξτ ∝ξz. At a classical equilibrium phase
transition, this quantum dynamic exponent, which appears in the scaling dimensions, e.g., in Eq. (S20), is formally

## Page 26

zero. However, when a classical system is subjected to some stochastic dynamics, e.g., in a Monte Carlo simulation,
there is a dynamic exponent corresponding to the particular process used (Metropolis or cluster updates). Then, in the
KZ exponent Eq. (S29), z is the stochastic dynamic exponent. A third possibility is a quantum system with intrinsic
dynamic exponent z that is simulated using a Monte Carlo process, such as the SQA simulations used as benchmarks
here. Then the intrinsic (quantum) dynamic exponent should still be used in Eq. (S20), but z in the KZ exponent
should be the relevant exponent corresponding to the imposed Monte Carlo dynamics (which also depends on the
system studied)70. Here, for simplicity of the notation, we will ﬁrst assume an actual quantum system undergoing
Hamiltonian dynamics, where there is only a single dynamic exponent, but we will later return to the other cases as
well.
The easiest way to analyze data within the dynamic ﬁnite-size scaling ansatz is to consider the quantity n exactly
when the critical point has been reached: δ = 046,69. Then we can simply write Eq. (S28) as

n = L−∆ng(vLµ),
(S31)

which can be tested with data for diﬀerent values of v and system sizes L. For v →0, we should of course recover
the standard FSS form n ∝L−∆n, which means g(x) →constant when x →0. For v > 0, the scaling function can
be extracted by graphing y = nL∆n versus x = vLµ for suﬃciently large L and a range of v values, whence all the
data points should collapse onto the common function g(x). If the exponents are not known, they can be found by
adjusting their values for optimal collapse.
Quantities n with known scaling dimension ∆n = 0 are particularly useful, since any uncertainties in (or lack
of knowledge of) the leading ﬁnite-size dependence can then be avoided. A well known example is the Binder ratio
deﬁned with two diﬀerent powers of the order parameter, Eq. (S17), for which the scaling dimensions of the numerator
and denominator cancel. Normally the k = 2 case, R2 = ⟨m4⟩/⟨m2⟩2, is considered, and a corresponding cumulant
is deﬁned as U ≡U2 = a(1 −bR2), where the coeﬃcients a and b are determined using the symmetry of the order
parameter such that U →0 in the disordered phase and U →1 in the ordered phase. The deﬁnition of this quantity
in a system with random couplings is further discussed below in Sec. I C 3.
The asymptotic form of g(x) in Eq. (S31) can be argued as follows: For v > 0 the correlation length ξv is ﬁnite.
In limit L ≫ξv the system is disordered and the size dependence becomes trivial, though its form depends on the
quantity n considered. In the case of a squared order parameter, we have ⟨m2⟩= ⟨M 2⟩/N 2 ∝1/N = L−d, which
can be easily seen by expressing ⟨M 2⟩using the exponentially decaying (asymptotically) correlation function Cm(r)
of corresponding local operators [deﬁned with a generic operator P in Eq. (S5)]:

⟨M 2⟩= N
X

r
Cm(r) ∝N
(for short-ranged Cm).
(S32)

In order to obtain the L−d dependence of ⟨m2⟩from Eq. (S31), the scaling function must take an asymptotic power-
law form, g(x) →x−c˜g(x) with the function ˜g(x) approaching a constant when x →∞and the exponent c satisfying
cµ + ∆m2 = d, with ∆m2 = 2∆m, i.e.,

⟨m2⟩∝L−2∆m(vLµ)−c˜g(vLµ) →L−dv−c,
c = d −2∆m

µ
= d −2β/ν

µ
.
(S33)

This is the KZ FSS form far from equilibrium, which must eventually break down when v is very large, i.e., when
the correlation length ξv is of order unity (the lattice spacing in a lattice model). The ultimate high-velocity form is
just ⟨m2⟩= L−dg(v), where the function g is analytic in 1/v, and this form crosses smoothly over into the algebraic
KZ form (S33) as v is reduced. When v is further reduced, for given L this form turns smoothly into the equilibrium
form of Eq. (S31), ⟨m2⟩∝L−2β/ν, when v →0.
For the excess energy density deﬁned in Eq. (S15), the above arguments can be repeated with the modiﬁcation that
now ρE must be size independent at high velocities since it is a simple density with only exponentially small ﬁnite-size
corrections in the disordered initial state. Thus, the algebraic KZ form for large vLµ (but still v ≪1) is

ρE ∝L−∆ρE (vLµ)κ˜g(vLµ) →vκ,
κ = ∆ρE

µ
= d + z −1/ν

µ
.
(S34)

This form evolves gradually into a constant when v →∞, and in the other extreme it crosses over to the equilibrium
form ρE ∝L−∆e = L−(d+z−1/ν) when v is of order L−µ (i.e., when ξv grows to order L). Note that the exponents c
and κ in Eqs. (S34) and (S33) are both positive but they appear with diﬀerent signs when the powers of δ are taken,
reﬂecting the decrease in the residual energy and increase in the order parameter as the annealing velocity is reduced.
For the quantities n considered above, and many others, the algebraic KZ scaling form can be investigated by
graphing y = nL∆n versus x = vLµ after a process stopping at the critical point. The power-law forms discussed

## Page 27

above will then cross over into constants for suﬃciently low v, which is possible because of the function ˜g(vLµ) in
Eqs. (S33) and (S34). Upon increasing v, data for small systems will successively peel oﬀfrom the common scaling
function when the correlation length ξv is of the order of the lattice spacing (loosely speaking, when v is of order one).
In an alternative method, y = n (in the case of the residual energy density) or y = nLd (in the case of the squared
order parameter) can be graphed versus v or v−1, in which case the power-law behaviors in Eqs. (S33) and (S34)
are observed in the algebraic KZ regime but data collapse does not apply when equilibrium is approached (where
curves for diﬀerent L gradually peel oﬀfrom the common power-law form). Instead, data collapse now applies also in
the high-v limit, where constant behaviors pertain. The two ways of analyzing SA data have been demonstrated for
uniform 2D and 3d classical Ising models (using both local and cluster Monte Carlo updates)69 as well as 2D71,72 and
3D48 classical spin glasses. Similar methods were also applied to imaginary-time QA (implemented in quantum Monte
Carlo simulations with imaginary-time dependent interactions) of the transverse-ﬁeld Ising model with uniform46 and
random (3-regular graphs)70 interactions.
In the case of the Binder cumulant (or ratio), the scaling dimension is zero but the asymptotic form of the equilibrium
scaling function U = u(δL1/ν) in the disordered phase is non-trivial and still not well understood57,73. The size
dependence of U in a disordered state is not just a constant [as in Eq. (S34)] or ∝L−d [as in Eq. (S33)] but a diﬀerent
power-law Lk that is not known generically. The exponent b governing the KZ power law U ∝v−b when L ≫ξv can
therefore also not be obtained in a simple manner using just the arguments leading to Eqs. (S33) and (S34). The
scaling form U = u(vLµ) still of course applies (including an asymptotic power-law form with some exponent b) and
can be extracted empirically as in other cases by graphing y = U versus x = vLµ with µ optimized.
When annealing slightly into an ordered phase (taken as δ > 0) the extended KZ form (S28) can be Taylor expanded
as long as δL1/ν remains small, i.e., asymptotically for large L the system tends to the critical point. When annealing
more signiﬁcantly into the ordered phase, but still within the critical window δ ∝L−1/ν, power laws appear similar to
those discussed above on the disordered side of the transition. When annealing far into an ordered state the situation
is much more complicated and non-generic, requiring additional knowledge of the dynamical processes inside the
phase. While some progress on this front has been reported recently54, in general the issue remains largely open. We
next discuss annealing into a spin-glass phase and present insights and hypotheses of direct relevance to the quantum
annealing experiments and simulations reported in this work.

C.
Application to annealing experiments and simulations

For a system annealed through a phase transition and slightly into an ordered phase, we can expect the extended
KZ ﬁnite-size scaling form (S28) to apply. In principle, once the system is deep enough in the ordered phase, some
other dynamical process beyond the critical ﬂuctuations underlying the KZ mechanism will take over and eventually
dominate. In some cases, a dynamical process in the ordered phase is faster than the KZ dynamics, e.g., in the case
of coarsening dynamics of a system with no randomness—see Ref.74 for discussions of how the KZ scaling is violated
in the ordered phase in a simple Ising model. Then KZ dynamics should in general not be expected, though recent
work suggests that an extension of the scheme, with modiﬁed power laws, is valid slightly inside in ordered phase in
some cases like the standard uniform 2D Ising model in a transverse ﬁeld54.
Inside a classical or quantum glass phase, all dynamical processes should be extremely slow. Therefore, KZ scaling
can be anticipated even if the annealing process stops (and the outcome is observed only) far beyond the transition
point. In the QA device used in our experiments, there are also technical reasons related to the shape of the annealing
protocol (see Fig. 1b) why the system should “freeze out” and not evolve signiﬁcantly at the latter stages of the
process ending at the classical point s = 1 (because the transverse ﬁeld becomes very small already at s ≈0.7). In
MC simulations, KZ scaling can be measured by observing the system exactly at the critical point (as was done in
an SA study of the simple-cubic 3D Ising spin-glass48). However, in this work we anneal deep into the glassy phase
even in SA and SQA for two reasons. First, we wish to qualitatively reproduce the QA protocol. Second, annealing
toward the T = 0, Γ = 0 point guarantees a ﬁnal equilibrium near the classical ground state.
Fig. 3f shows quite clearly the expected crossover when the density of AFM bonds is increased from p = 1/2,
between glassy KZ dynamics with an exponent µ that is close to its known KZ value (µ = z +1/ν) and a smaller value
µ ≈2. The smaller value may indicate coarsening dynamics inside the AFM phase for p ≳0.8. However, coarsening
in quantum systems has not been extensively investigated using reliable unbiased simulations, and no direct evidence
of such dynamics was found at the early stages of entering the ferromagnetic phase of the transverse-ﬁeld Ising model
in Ref.54.
Focusing here on the glass phase, from the analysis of the Edwards-Anderson (EA) order parameter ⟨q2⟩(where
again ⟨.⟩also involves an average over disorder realizations), while the exponent µ is close to its KZ value, the
scaling dimension of the quantity itself (the exponent r in Figs. E6 and E7) is far from the anticipated critical
scaling dimension. We will show here that such behavior over a range of relatively fast annealing rates and small to

## Page 28

moderate system sizes can be explained by an extended KZ scaling form supplemented by mild, physically reasonable
assumptions pertaining to the glassy state.

1.
Spin glass order parameter

Before considering scaling behavior, we brieﬂy discuss the EA order parameter in light of the deﬁnitions of exponents
and scaling dimensions explained in the previous sections. We use the conventional overlap parameter of the spins
S(a) and S(b) in two replicas, a and b,

qab = 1

i
S(a)
i
S(b)
i
,
S(a,b)
i
∈{−1, +1},
(S35)

X

N

obtained from the same realization of the Ising couplings but in diﬀerent runs with the QA device or in independent
MC simulations. The expectation value (quantum or thermal, depending on the case considered) of the squared order
parameter for a given coupling realization is

⟨q2
ab⟩=
1
N 2
X

i,j
⟨S(a)
i
S(a)
j
⟩⟨S(b)
i
S(b)
j ⟩,
(S36)

where the expectation value factors because the two replicas are statistically independent. We can now take averages
also over the replicas. Because the coupling realization is the same in all replicas, the replica-averaged expectation
values in Eq. (S36) will be the same. In fact, over a suﬃciently long time a ﬁnite system is ergodic, and no average
over a and b replicas need to be formally taken. However, in reality simulations of glasses are extremely slow, and
replicas have to be considered in order to suﬃciently sample the conﬁguration space. In annealing experiments and
simulations out of equilibrium, the systems are by deﬁnition not ergodic, and averaging over replicas is an integral
aspect of such studies. Once replica and disorder averages have been taken, we drop the indices a and b and have

⟨q2⟩=
1
N 2
X

i,j
⟨SiSj⟩2.
(S37)

When averaging over coupling realizations, translational symmetry is also restored, and we can introduce a squared
correlation function C2(r) as the averaged ⟨SiSj⟩2, with r = ri −rj, to write

⟨q2⟩= 1

X

N

r
C2(r).
(S38)

Such a sum without squaring C(r) would vanish because of coupling averaging when the fraction of AFM couplings
is 1/2, and the use of the overlap q deﬁned with replicas is a convenient way to solve this problem. The fact that
the squared EA order parameter formally is a sum over squared correlation functions in Eq. (S38) then has to be
taken into account when using exponent relationships such as (S9), where d and z cannot depend on what correlation
function is considered and, therefore, the factor in front of the scaling dimension must be 4 instead of 2.
Note that ⟨q2⟩is a perfectly valid order parameter also for a system without disorder, e.g., an Ising ferromagnet.
Then it is clear that the decay of the squared correlation function should be associated with four times the scaling
dimension of the order parameter, C2
m(r) ∝1/r4∆m, because of the exponent 2∆m in the conventional (not squared)
correlation function (S8). Thus, if we wish to use conventional deﬁnitions of the critical exponents in the case of the
EA order parameter, obeying forms analogous to Eq. (S20), we would have to write the FSS form of ⟨q2⟩implied by
Eq. (S38) as

⟨q2⟩∝L−2(d+z−2+η).
(S39)

However, normally the exponents are deﬁned diﬀerently in spin glasses, by treating q as a regular order parameter
and deﬁning η based on the scaling form for susceptibilities such as (S27), where χq would be deﬁned with M = Nq in
Eq. (S25)65. Such a deﬁnition of η—let us call it η′—does not satisfy the common relationship to a scaling dimension,
i.e., 2∆q ̸= d + z −2 + η′.
To conform with the standard notation in the spin glass literature, we will here use the common deﬁnition of the
order parameter exponent β for spin glasses, i.e., we treat the EA order parameter as a conventional order parameter
with the form ⟨q2⟩∝δ2β in the thermodynamic limit, so that the critical ﬁnite-size form is ⟨q2⟩∝L−2β/ν. Note
that the above issue with exponent relationships does not aﬀect the exponent ν when extracted using data-collapse

## Page 29

methods, or the intrinsic (quantum) dynamic exponent z when it is extracted from the dependence on the aspect
ratio Lτ/Lz in Eq. (S22). The KZ exponent µ = z + 1/ν is also not aﬀected by the speciﬁc deﬁnitions of β and η.
We will use a conventional scaling dimension further below when discussing the residual energy, whose deﬁnition is
independent of the use of replicas.

2.
Scaling of the spin-glass order parameter

Applying the extended KZ form (S28) to the EA order parameter, we have

⟨q2⟩= L−2β/νg(vLµ, δL1/ν),
(S40)

where δ = s −sc and s(t) ∈[0, 1]. In theoretical work and simulations, the simple linear protocol J ∝s, Γ ∝1 −s is
often used for transverse-ﬁeld Ising models. In the QA experiments, the protocol is nonlinear (Fig. 1d) but linearity
still holds for s in the close neighborhood of the critical point and Eq. (S40) is valid with v deﬁned as the actual
coupling derivative, or, for scaling purposes, the inverse of the total annealing time.
Though there are some claims in the literature that z →∞at the glass transition in the 2D and 3D Ising spin
glasses considered here75,76 (similar to random-ﬁeld models36,77), in our opinion the available numerical evidence leans
in the favor of ﬁnite, relatively small values of z65,78. In our own simulations and QA experiments (SI Sec. II and
Figs. E6-E8), we also do not see any evidence of large or signiﬁcantly ﬂowing (with increasing system size) values of
z. Thought the possibility of an inﬁnite-disorder ﬁxed point (where formally z = ∞) cannot be completely ruled out,
we here consider only scaling with ﬁnite z.
As discussed in the preceding sections, the thermodynamic-limit form ⟨q2⟩∝δ2β demands that g(0, x) with x =
δL1/ν reduces to x2β when x →∞inside the spin-glass phase close to the transition point. Moving further inside
the glass phase, this power-law form can no longer hold. To enable the cross-over to a diﬀerent (unspeciﬁed) form in
equilibrium, we can consider a more ﬂexible version of Eq. (S40),

⟨q2⟩= L−2β/νf(vLµ, δ, L),
(S41)

where δ and L appear as two diﬀerent arguments in the function. For small δ we know that the function must simplify
to the standard scaling form (S40), where the two arguments δ and L are replaced by just the single argument δL1/ν.
We can express the cross-over from the two arguments (L, δ) to eﬀectively a single argument by introducing another
function as an argument to the scaling function,

⟨q2⟩= L−2β/νg(vLµ, h(δ, L)δL1/ν),
(S42)

where h →1 in the regime of δ and L where the simpler form (S40) applies. This functional form is still as general
as Eq. (S41) and can in principle describe the behavior for any δ and L. To recover the form ⟨q2⟩∝δ2β from (S42)
in the thermodynamic limit when v is small, a power-law of the second argument must again form

⟨q2⟩→L−2β/νh2β(δ, L)(δL1/ν)2βg(vLµ) = δ2βh2β(δ, L)g(vLµ),
(S43)

where we have also assumed that, to a good approximation, we do not need to keep a second argument of the
function g when the power law form has set in, which is equivalent to saying that the function g now is of the form
g(vLµ, k(δ, L)), where the function k is almost constant in the relevant regime of L and δ.
To simplify further, we can re-deﬁne the function h in Eq. (S43) without the exponent 2β, and we can also absorb
the factor δ. Then

⟨q2⟩= h(δ, L)g(vLµ).
(S44)

This form is clearly valid for v →0, since it can capture any dependence on δ and L, and we know that h(δ, L) →
h(δL1/ν) close to the critical point. We have of course made assumptions leading to g(vLµ) appearing as a separate
factor, for which we have no proof but which can be tested in experiments and simulations.
Inside the glass phase, the squared order parameter converges with L to a non-zero value when v →0. Thus, for
suﬃciently large L inside the ordered phase, in Eq. (S44) h(δ, L) →k(δ) and

⟨q2⟩= k(δ)g(vLµ),
(S45)

where the function k represents whatever the δ dependence is in equilibrium,

k(δ) ≡⟨q2(δ, v = 0)⟩,
(S46)

## Page 30

and g(x →0) →1.
The ﬁnal forms (S44) and (S45) cannot be strictly correct, as KZ dynamics should at least not be valid at the ﬁnal
stage (the most extreme case) when the order saturates. However, this just means that there is some other (assumed
to be slower) dynamics that takes over, but we have assumed only one dynamical mechanism. The assumptions and
resulting forms may be valid as long as the annealing time is not too long, so that the dynamics associated with the
glass phase can be considered as a weak perturbation to the critical dynamics with exponent z. Then also ⟨q2⟩will
remain small though its scaling may reﬂect (as we will see) a cross-over from critical to ordered behavior.
For δ not small and L not large enough to eliminate the L dependence of h in (S44), we must still keep the function
with two arguments. It is not clear what the functional form of this h(δ, L) is, but it is at least plausible that a power
law applies for some range of system sizes, i.e.,

h(δ, L) →˜k(δ)L−r.
(S47)

Here, for δ →0 (i.e., in the limit of conventional FSS and KZ scaling) we must have r = 2β/ν and k(δ) approaching
a non-zero constant. For L →∞and δ ̸= 0, the exponent r must tend to zero and ˜k(δ) the takes the equilibrium
form as in Eq. (S46). For ﬁxed δ inside the glass phase, the exponent r must then be ﬂowing but may still evolve
only slowly with L, thus essentially constant when observed only over a small range of system sizes. Indeed, in our
experiments and simulations, we observe an eﬀective exponent r between 0 and 2β/ν.

3.
The Binder ratio

According to our arguments above, an eﬀective scaling dimension diﬀerent from that at the critical point can be
manifested when annealing a system into a spin glass phase;

⟨q2⟩= ˜k(δ)L−rLg(vLµ),
(S48)

with an exponent rL that changes only slowly with L from rL = 0 to rL = 2β/ν. As in the case of conventional critical
scaling, the eﬀective scaling dimension of ⟨m4⟩should be twice that of ⟨m2⟩, and the Binder ratio (and cumulant)
then remains dimensionless. Thus, it is the preferred quantity to analyze when the goal is to extract the exponent µ
in annealing experiments where the state exactly at the transition point sc is inaccessible.
The Binder ratio for a system with intrinsic randomness (e.g., a spin glass) can be deﬁned with the average over
realizations taken either before or after evaluating the ratio in Eq. (S17). Now using [.] to denote a disorder average
and ⟨.⟩for only thermal and quantum averages (including replicas), we can deﬁne the following two ratios:

Ra =
 ⟨q4⟩

⟨q2⟩2

Rb = [⟨q4⟩]


,
(S49a)

[⟨q2⟩]2 .
(S49b)

While Eq. (S49a) has been frequently used (e.g., Ref.65), Eq. (S49b) has become more common (see also Ref.79).
They are both dimensionless quantities and in principle equally valid for use in scaling analysis.
Equation (S49a) has a drawback of being biased when evaluated with a ﬁnite number of measurements to estimate
the expectation values. Consider statistical deviations ϵ2 and ϵ4 of ⟨q2⟩and ⟨q4⟩from their exact values ⟨.⟩ex for a
given coupling realization, based on Λ measurements. Then the ratio Eq. (S49a) is

R = ⟨q4⟩

⟨q2⟩2 =
⟨q4⟩ex + ϵ4
(⟨q2⟩ex + ϵ2)2 = ⟨q4⟩ex

⟨q2⟩2ex
+ O(ϵ2
2, ϵ2ϵ4),
(S50)

where odd powers of the error vanish on average. Since the magnitudes of ϵ4 and ϵ2 scale as Λ−1/2, the expected bias
in the realization-averaged ratio Ra, Eq. (S49a), scales as Λ−1. While this bias decays faster than the expected overall
∝Λ−1/2 statistical error in R, if the number of measurements Λ is small there can still be a non-negligible eﬀect of
bias left. This bias is smaller by a factor N −1/2
r
in Rb, Eq. (S49b), when both the numerator and denominator are
averaged over Na independent disorder realizations.
The leading bias can in principle be removed by combining results for diﬀerent Λ. In the simulations and experiments
for the cumulant U = (3 −R)/2 presented here, Λ is suﬃciently large for the bias to be insigniﬁcant. We nevertheless
use Eq. (S49b), though (S49a) gives compatible results.

## Page 31

4.
Residual Ising energy

For the residual Ising energy E, we proceed in a slightly diﬀerent way. Since the Ising part of the Hamiltonian
drives the transition, its scaling dimension ∆e = d + z −1/ν is given by Eq. (S20) with ν being the conventional
correlation-length exponent. The KZ-FSS scaling form is

ρE = L−∆ρE f(vLµ, δL1/ν),
(S51)

where it is assumed that the regular part of the energy, i.e., the “background” that is not part of the singular behavior,
has been subtracted oﬀ. The need for a subtraction here is an important aspect of the residual energy that is absent
in the case of the order parameter. The subtracted part should normally be the equilibrium critical Ising energy in
the thermodynamic limit, as in Eq. (S15). However, nothing prohibits us from instead subtracting the equilibrium
ﬁnite-size Ising energy E(δ, L), which has the same scaling dimension as ρE. Then we have the following expected
FSS form [keeping the same symbol ρE as before even though its meaning has changed slightly]:

ρE(L, δ, v) = L−∆ρE [g(vLµ, δL1/ν) −g(0, δL1/ν)].
(S52)

Here the diﬀerence between the two scaling functions is just another scaling function, and we can write

ρE(L, δ, v) = L−∆ρE k(vLµ, δL1/ν).
(S53)

For any δ, by deﬁnition (because of what we have decided to subtract), this ρE must vanish when v →0. That means
that a positive power of v must appear as a factor, and δL1/ν can only appear in a function multiplying this overall v
dependence. The most natural way to express this behavior is for k to develop a power law of its ﬁrst argument, i.e.,

k(vLµ, δL1/ν) →(vLµ)κh(vLµ, δL1/ν).
(S54)

Note that the new scaling function h can still also depend on vLµ, and mathematically there is no approximation here
because the right-hand side still depends only on the two arguments x = vLµ and y = δL1/ν (i.e., it is some function
of these two arguments, as on the left-hand side).
The exponent κ can again be extracted as in Eq. (S34) if we demand no L dependence apart from that in the
function h, and we now call this critical exponent κc. We know that this scaling must hold when δ = 0 and the KZ
correlation length is smaller than the system size. At least for small δ, as long as the function h(x, y) is well behaved,
the exponent on v cannot change. Then, the ﬁnal residual Ising energy in a QA process stopping inside the glassy
phase takes the form

ρE(L, δ, v) = vκch(vLµ, δL1/ν),
(S55)

with the same exponent κc as when stopping at the critical point,

κc =
∆ρE
z + 1/ν = d + z −1/ν

µ
.
(S56)

It should be emphasized that Eqs. (S55) and Eq. (S53) are two completely equivalent forms of ρE, and whichever
form to use just depends on the type of scaling analys one wishes to perform. They are both scaling functions of the
single variable x = vLµ at the critical point δ = 0.
For a process not stopping exactly at the critical point, a scaling function of a single variable can still be obtained
when considering the thermodynamic limit of Eq. (S55). For δ ̸= 0, when L ≫ξ the system size can no longer
appear. L can only be eliminated from the scaling function h(x, y) with x = vLµ and y = δL1/ν if the function of
two argument evolves into one of a single argument, h[z(x, y)], where z does not depend on L. To cancel L, we can
take z = x1/µνy−1 and obtain a scaling function e(z) of a single variable, whence Eq. (S55) becomes

ρE(δ, v) = vκce(v1/νµδ−1).
(S57)

Recall that here we must have δ ̸= 0 so that the limit where L exceeds ξ exists. A physical argument for the new
scaling variable is that δ in this limit should not be compared with L−1/ν as in equilibrium ﬁnite size scaling (with
the single scaling argument δL1/ν). Instead, L must be replaced by the ﬁnite velocity-dependent KZ length scale ξv,
which is smaller than L. Thus, L1/ν is replaced by ξ1/ν
v
= v1/µν and the proper scaling argument is δv−1/µν = z−1,
or, alternatively, the inverse thereof as in (S57), where the low-velocity limit corresponds to e(z →0).
The way in which we have deﬁned the excess Ising energy ρE, it vanishes when v →0 for any δ. However, pure
critical KZ behavior, ρE ∝vκc, should only apply very close to δ = 0 for some range of velocities before a cross-over

## Page 32

into a form governed by the dynamics of the glassy state when v →0. For a process stopping signiﬁcantly inside the
glassy state, there may be no range of velocities for which the exponent κc strictly applies. However, if v is not too
low, i.e., the argument x = v1/νµδ−1 is relatively large in e(x) in Eq. (S57), it is plausible that the scaling function
takes a power-law form, e(x) ∼xk with some unknown exponent k (and also note that the scaling function cannot be
analytic in the glass phase, because κc does not asymptotically describe the dynamics). Since δ is just a ﬁxed number,
this behavior would imply a change in the exponent on v in Eq. (S57), ρE ∼vκf with κf = κc + k/µν. Given that
the dynamics of the quantum spin glass should be slower than the KZ dynamics, it is natural to expect κf < κc, as
we indeed also found in our QA experiments (Fig. 4b).
The above analysis presumes that δ drives a quantum phase transition at which the Hamiltonian is the sole provider
of dynamics. At a classical phase transition of a model with no intrinsic dynamics, d + z in the expression for κc,
Eq. (S56), should be just d, and the dynamic exponent in the KZ exponent µ = z+1/ν should be that of the stochastic
process used to evolve the system with SA,

κSA =
d −1/ν
zSA + 1/ν ,
(S58)

where zSA also depends on the system studied (i.e., it is a universal exponent given a critical point and a type of
stochastic process).
The case of SQA is a mix of QA and SA in the sense that it implements the imaginary-time dimension through
a path integral, hence d + z, with the same z as in QA, appears in the numerator of κSQA. However, the d + 1
dimensional eﬀective statistical-mechanics system is simulated by an MC procedure as in SA, and it is the exponent
corresponding to that process that allows the simulation to relax toward its equilibrium. Thus, in this case, the
exponent contains two dynamic exponents

κSQA = d + z −1/ν

zSQA + 1/ν ,
(S59)

where zSQA is not a priori known, and, like the classical exponent zSA, depends on both the system studied and the
MC procedures applied. To our knowledge, this exponent had not been computed previously for the 3D Ising spin
glass in a transeverse ﬁeld. In our SQA work, we extracted µSQA = zSQA + 1/ν from the data collapse of the Binder
cumulant (Fig. E6).

II.
3D SPIN GLASSES

A.
Construction

The instances we study for size L are on L×L×min(L, 12)×2 spins, indexed by (x, y, z, w) with x, y ∈{0, . . . , L−1},
z ∈{0, . . . , min(L −1, 11)}, and w ∈0, 1. For a given 3D coordinate x, y, z, sites (x, y, z, 0) and (x, y, z, 1) are coupled
with a strong ferromagnetic coupling, J = −JFM; in this work JFM = 2. For L > 9, instances contain site vacancies
due to inoperable qubits.
In the x dimension, couplings use only the w = 0 sites; the coupling between (x, y, z, 0) and (x+1, y, z, 0) for x < L
is ±JG: JG with probability p, and −JG otherwise. Random choices of spin-glass couplings are independent. Except
where stated, p = 0.5. The x dimension has open boundaries.
In the y dimension, couplings use only the w = 1 sites; the coupling between (x, y, z, 1) and (x, y + 1, z, 1) for y < L
is ±JG. The y dimension has open boundaries.
The z dimension is periodic. For z′ ≡z + 1 (mod L), the coupling between (x, y, z, 1) and (x, y, z′, 0) is equal to
the coupling between (x, y, z, 0) and (x, y, z′, 1); each is ±JG/2, meaning that their total is ±JG. Said diﬀerently, the
four spins (x, y, z, 0), (x, y, z, 1), (x, y, z′, 0), and (x, y, z′, 1) induce an unfrustrated loop.
In the limit JFM/JG →∞, FM-coupled dimers can be identiﬁed into single “logical” spins, so the model is equivalent
to a bimodal spin glass (random bond model) on a standard 3D cubic lattice with open x- and y-boundaries and
periodic z-boundaries.
The x- and y- dimensions are isotropic with respect to one another; the z-dimension is anisotropic in the following
three ways. First, the pair-to-pair couplings are split between two couplers. Second, the dimension is periodic, while
the x- and y-dimensions are open. Third, for L > 12, the z-dimension has length bounded by 12. This is because
the “Pegasus”80 layout of qubits is roughly described as a 16 × 16 grid of 24-qubit unit cells, with some loss around
the boundaries; the 24 qubits are used for 12 2-qubit dimers, forming the z and w dimensions. For this reason when
studying ﬁnite-size scaling, we restrict our attention to L ≤12. When studying energy scaling, we use the largest
size: 15 × 15 × 12 × 2, with inoperable qubits in the particular processor used leaving only 5374 of 5400 qubits in the
inputs.

## Page 33

−4,620

Eput(S, L = 15)

−4,640

−4,660

−4,680

103
104
105
106

Number of sweeps S

FIG. S1. Convergence of mean ground-state energy under the PT-ICM heuristic. Shown are average energies over
300 spin-glass realizations with L = 15 for a parallel tempering method used to estimate ground-state energies, running for up
to S ≥106 sweeps. The asymptote (power-law ﬁt to last 50 data points, shown in black, with limit −4669.6) appears to be
well established with bias and uncertainty negligible in comparison to the experimentally relevant residual energies.

B.
Broken FM dimers in the 3D ground state

There are diﬀerences between the 3D spin glasses studied in this work and the corresponding glasses on the simple
cubic lattice that one obtains by contracting each two-qubit dimer into a single spin. In Section III we will discuss
the eﬀect on critical exponents, which explains some of the deviation seen between QA values of the KZ exponent
µ = z + 1/ν from previously reported values for 3D quantum Ising spin glasses49. Here we consider the separate
question of how the classical ground states relate to one another between the “embedded” lattice that we study,
versus the “logical” counterpart in a simple cubic lattice.
Let us consider a single spin-glass realization, which has an embedded version and a logical version. When JFM >
3JG, it is easy to show that no ground state in the embedded problem can have a broken dimer, since ﬂipping a
spin to repair a broken dimer (one spin up, one spin down) in such a state would reduce the energy. Likewise, when
JFM ≥3JG it is easy to see that the problem must have at least one ground state with no broken dimers. However,
when JFM < 3JG it is possible that all ground states could have at least one broken dimer.
As an example, we begin with a completely ferromagnetic instance, where all couplings have negative sign. Now,
for some ﬁxed x0, y0, and w0, the spins with coordinates (x0, y0, z, w0) form an independent set. We ﬂip the sign of
all glass couplings incident to this set. It is a simple exercise to conﬁrm that this instance is valid in the sense that it
has a well-deﬁned logical counterpart. Furthermore the ground state is twofold degenerate, with broken dimers (with
x = x0 and y = y0) in each ground state. We conﬁrmed this with a computer search for the small case L = 4.
Therefore when JG > JFM/3 we cannot guarantee the existence of a ground state of the embedded lattice that
maps to a ground state of the logical lattice. However, this construction is pathological, and appears to rely on a
speciﬁc conﬁguration spanning the periodic z-dimension. Thus it seems to be highly unlikely in random inputs, and
we have not observed such an input in this study.

C.
Estimating ground state energies

To understand mean residual energy in the context of approximate optimization, we must estimate ground state
energy—this task is NP-hard for cubic lattices and practically challenging in the typical case for the largest system
sizes we consider. Bearing in mind the preceding discussion, we simplify the task by searching for ground states in
the logical model, i.e., spin glasses on a simple cubic lattice.
The spin glasses studied here are too large to solve with exhaustive approaches such as branch-and-cut81. We
instead use a parallel tempering algorithm with isoenergetic cluster moves (PT-ICM)82 to ﬁnd putative ground states
for each instance, and show by a self-consistent method that any bias introduced by failure to uncover the exact
ground state in some subset of instances is negligible with respect to the average residual energies studied in this
work.
We employ an adaptive form of the algorithm. The temperature range is initialized so that the lowest and highest
chains sample at T = ∞(spin ﬂip proposals accepted with 50% probability) and T = 0 (no upward energy proposals
accepted). Intermediate temperatures are then inserted iteratively, so as to approach replica exchange rates limited

## Page 34

to the range [0.2, 0.5]. The temperature set stabilizes after several thousand sweeps of all replicas. One sweep entails
updating all spins in all replicas in some ﬁxed order. Isoenergetic cluster moves are performed for all temperatures
every 10 sweeps. After S sweeps of the algorithm we can estimate the ground state as the best state observed across
the entire algorithm run.
This random estimator produces an S-dependent upper bound on the ground state Eput(S) in the lowest temperature
chain that tightens with S. For our analysis we require a model average per system size, Eput(L, S) = [Eput(S)]L where
square brackets denote our expectation with respect to the set of instances used experimentally. This estimator is
subject to a variance and bias, which increase with system size. We can determine conﬁdence intervals by considering
many independent instantiations of the algorithm at each S. The bias is expected to decrease with S as shown in
Fig. S1; Eput(L, S) appears to converge and we can assume the limit Eput(L) = limS→∞Eput(L, S) with reasonable
conﬁdence. The black line in Fig. S1 indicates a power-law ﬁt to the last 50 data points, which has a limit Eput(15) =
−4669.6, which would imply that our estimate of the mean ground state energy is correct to within 0.00005 relative
error, or 0.00004 energy per site—negligible in comparison to experimental values.
We needn’t (and cannot) claim to have found the ground state for every instance, at every size by this method for
any ﬁnite Smax. We only need convincing evidence that the error in the estimate of ground state energy is negligible
compared to the residual energies that we use to compare SA, QA, and SQA.
We can assume Eput(L, S) converges smoothly in S to obtain a suﬃcient estimator for our mean residual energy
analysis. Assuming a power-law form of residual energy gives one estimate of Eput(L, S), which describes the data
closely (see Fig. S1). In practice, we ﬁnd it suﬃcient to approximate

Eput(L) ≈
min
independent runs Eput(L, Smax),
(S60)

the best energy observed amongst 5 independent replicas at some large (but experimentally reasonable) number of
sweeps. The convergence Eput(L) is shown in Figure S1 for the most challenging problem scale (L = 15), and it is
clear the error in the ground state energy across 300 instances is a negligible factor in our analysis.
We emphasize that an error in ground state energy aﬀects the computed residual energy for all dynamics equally.

D.
Quantum and classical phase transitions

Here we brieﬂy describe the phase diagram for the 3D spin glass shown in Fig. 1e. We ﬁrst focus our attention on the
±J spin glass on a simple cubic lattice. The classical case has been studied in detail using the Janus special-purpose
computer83. Although it was not initially clear84,85, it has been established that there is a ﬁnite-temperature transition
at T 3D
c
≈1.101983. The critical correlation exponent and anomalous dimension have been estimated, respectively, as
ν = 2.562, η = −0.3983. In the main text we referenced an estimate of the dynamic exponent z = 5.93 for the ±J
case48, but in that paper48 (Table I) it is pointed out that a range of estimates has been reported over the last 20
years.
Our picture of the quantum phase transition is mostly informed by a study of Guo, Bhatt and Huse from 199449,
which gives estimates of z ≈1.3, ν ≈1/1.3.
Making use of relatively recent algorithmic advances—primarily,
continuous-time PIMC—we perform similar MC simulations on both the simple cubic lattice and the embedded 3D
lattices studied in this work. We discuss these simulations in the next section.

III.
EQUILIBRIUM ANALYSIS OF CRITICAL PHENOMENA BY MONTE CARLO METHODS

As highlighted in the main text, the universal and non-universal critical behavior of 2D and 3D transverse ﬁeld Ising
spin glass models has been studied in previous works49,83. In this section we use path-integral Monte Carlo—in the
limit of continuous imaginary time—to establish the equilibrium critical behavior of 3D spin glasses both on simple
cubic lattices and on the embedded models studied in the main text, as well as 2D square ferromagnets. We generate
data for ferromagnetic and spin-glass models at comparable scales to those employed in the QA studies. Our aims
in this section are: to verify previously reported critical exponents with an independent numerical analysis; to test
the viability of ﬁnite-size scaling analysis at the experimented scales; and to verify universality of the embedded 3D
spin glasses via the universal correlation exponent ν, regardless of microscopic model details. We use a methodology
inspired by previous studies of universal behavior, but adapted to allow for a continuous imaginary-time integral limit
of the Trotterized model49.

## Page 35

A.
Finite-size scaling in classical and path-integral models

As discussed in Section I, the properties of a classical or quantum spin-glass phase transition may be determined
by a ﬁnite-size scaling analysis of ⟨q2⟩49,65,86.
In the classical case we have a model over N-spin states ⃗s:



−β
X

P(⃗s) = exp

with

⟨q2⟩=
X

X

⃗s(2)
P(⃗s(1))P(⃗s(2))

⃗s(1)

The anticipated scaling form is



,
(S61)

i<j
Jijsisj

!2

1
N

i
s(1)
i s(2)
i

X

.
(S62)

⟨q2⟩= LbB(δL1/ν)
(S63)

with δ = (T −Tc)/Tc.
Critical behavior in the quantum model may be established by analysis of the density matrix exp(−βH(s)), where
H(s) is the Hamiltonian of our experimental Ising system (1) and β is the inverse temperature. By a process of
Trotterization this density matrix can be transformed into a classical model, suﬃcient to establish the distribution
of projected states and other statistics. The Trotterized model is deﬁned by a modiﬁed Hamiltonian over a space of
worldlines, in which each qubit i is replaced by Lz time-indexed classical spin-states si,t. For each time slice, variables
interact in accordance with the problem Hamiltonian, scaled to Lz. Spins are coupled ferromagnetically in imaginary
time, subject to periodic boundary conditions si,Lz = si,0. The probability distribution is given by



 Lz−1
X



−1

2 log tanh
βΓ(s)

P(⃗s, Lz) ∝exp

Lz

t=0



i
si,tsi,t+1 −βJ(s)

X

X

.
(S64)

i<j
Jijsi,tsj,t

Lz

An order parameter q can be deﬁned as the overlap of two states projected into the computational basis, the projected
state distribution is determined by the statistics of a single time slice (say t=0) in our model49,65. The spin-glass
susceptibility is deﬁned as the expected square value of this quantity, averaged over spin-glass realizations, i.e., ⟨q2⟩:

⟨q2⟩=
X

X

!2

1
N

i
s(1)
i,0 s(2)
j,0

X

⃗s(2)
P(⃗s(1), Lz)P(⃗s(2), Lz)

⃗s(1)

.
(S65)

Statistics of the quantum model are correctly established by taking the continuous limit in imaginary time1, Lz →∞.
In this limit the scaling of susceptibility is expected to take the form

⟨q2⟩= LbqB(δL1/ν, β/Lz),
(S66)

for a two-parameter collapse function B. Our analysis of the phase transition involves variation of Γ = Γ(s)/J(s) at
ﬁxed J(s), so that the reduced transverse ﬁeld is deﬁned as δ = (Γ −Γc)/Γc for a critical ﬁeld Γc.

B.
Monte Carlo sampling

Monte Carlo methods can be used to sample both the classical model (S61) and the Trotterized model (S64). For
the latter, we take the numerically convenient value of Lz = 216, which is indistinguishable from the continuous-time
limit (Lz →∞) for the relevant parameter ranges. Since in this limit the coupling strength in the imaginary time
direction is strong, it is necessary to employ Swendsen-Wang cluster updates87. Our algorithm thus proceeds by

1 Numerically we work at Lz = 216 with varying β. Because β ≪
Lz in all experiments conducted, this captures the continuous-
time limit.

## Page 36

iterating over sites i, and applying a cluster update (single-site, many-times) to si,· for each T or Γ. For our study
of embedded problems where disjoint pairs of qubits (dimers) are strongly ferromagnetically coupled (with relative
strength JFM/JG—see Fig. 1) we can apply a multi-site multi-time update per set; clustering occurs both in space
and time with respect to each dimer. The cluster updates are described, and code published, in previous studies35,88.
Since we are interested only in equilibrium behavior it is suﬃcient to consider a ﬁxed sequence of updates covering
all sites; one such sequence is called a sweep.
For the classical systems, we employ a standard parallel tempering (exchange Monte Carlo) method83. In the
quantum model we must sample across a larger parameter space, and with a slower worldline sampling update. For
eﬃciency of data collection we replace the parallel tempering routine with an annealing procedure. For a ﬁxed model
(disorder realization, at some size L) and ﬁxed Γ we vary inverse temperature at each sweep according to a geometric
schedule from a low value (where worldlines are fast-mixing) through the critical region to a low-enough temperature
for purposes of establishing critical scaling. In this way we collect single-sample (equilibrated, but correlated) data at
a wide range of temperatures. Statistics are averaged based upon 400 independent anneals drawing one realization of
the bond disorder per anneal. Uncertainty is estimated with bootstraps with respect to the disorder realizations. In
both the classical and quantum cases, we can maintain two independent Monte Carlo processes (replica) in parallel,
from which the overlaps can be calculated.
In the parallel tempering routine temperatures are spaced inclusive of high temperature fast mixing models and
critical region models to ensure suﬃcient replica exchange rates. Statistics are collected sequentially with exponentially
increasing burn-in and sampling times until convergence through the critical region is apparent. In the annealing
procedure fair sampling through the critical region requires a sweep rate (sweeps per unit change in log(β)) decreasing
with system size. In our methodology ⟨q2⟩converges from below, and this process becomes slow for large L, small Γ
and low temperature. We truncated our data collection at small size in part for this reason, and ensured that statistics
were for practical purposes insensitive in the data presented to variation by a factor of 4 in the sweep rate (estimators
agreeing within conﬁdence intervals at each system size and parameter set presented). The rate of progress, d log(β)
per sweep, was chosen between between 2 × 10−6 and 7 × 10−4, for the data presented.

C.
Classical critical scaling

Before showing collapse results in the quantum model, we digress to consider the classical model. In this case
we can collect data by a similar methodology but set Γ = 0 and employ in independent code a Metropolis method
supplemented with cluster ﬂip moves for the dimers. Estimates of Tc, ν, and η satisfying the classical scaling form
(S63) have evolved over the years83,85,89,90, with the most recent of these papers83 estimating Tc ≈1.1, ν ≈2.56,
and η ≈−0.39. Earlier estimates of ν85,89 were aﬀected by unaccounted corrections to ﬁnite-size scaling, leading to
signiﬁcantly lower estimates of ν. In Fig. S2 we show collapses of ⟨q2⟩Lb as functions of tL1/ν for Tc = 1.1, b = 0.61,
and ν = 1.5, for the logical (simple cubic) model and the embedded model with JFM = 2, 4, and 8. The value of ν is
far from recent estimates, but it provides a good collapse for the modest system sizes shown. For larger systems, the
appropriate collapse is achieved for ν ≈2.5. Here, the collapses simply illustrate the consistency of critical scaling
with respect to the dimer embedding and JFM. The evidence is consistent with little or no change in Tc, η, and ν
between the logical and embedded classical 3D spin glass models.

D.
Quantum critical scaling

We can now move on to collapses for the quantum model. An additional diﬃculty in performing a collapse of
data for the quantum model arises from the need to collapse a two-dimensional form (S66). In order to reduce this
to a one-dimensional problem we adapt the method of Guo, Bhatt and Huse49 to the continuous-time setting. The
eﬀect of increasing inverse temperature in our model (S64) is a nonlinear decrease in coupling strength in imaginary
time, with a linear increase in the coupling strength between sites. Therefore, at zero temperature the correlation
length ξz is much smaller than Lz in imaginary time, whereas spatial correlation length ξ approaches zero at high
temperature. Between these two extremes there exists—near the critical point—a value for which ξz ≈Lz and ξ ≈L
can be determined. This deﬁnes the point of maximum susceptibility which we presume (and show) to be approached
smoothly from high temperature; consequently β ∼Lz for this point.
We verify this intuition in a ferromagnetic model, then use it in a spin-glass model, as shown in Fig. S3. Since
we can determine by this method a β suﬃcient for the correlation length in imaginary time to match Lz, we are
able to reduce (S66) to a one-dimensional ﬁt ⟨q2⟩= Lbq maxβ′ B(γL1/ν, β′). As in the classical case we can extract
parameters Γc, ν, and bq from the ﬁt. We used an open-source library, autoScale.py91, to ﬁt this data, with the
JFM = 2JG example shown in Figure S4. For a goodness of ﬁt S (with small S indicating a good ﬁt; see91), error

## Page 37

1.5

⟨q2⟩Lb
⟨q2⟩Lb

1

0.5

1.5

1

0.5

−1
0
1

−1
0
1

(T −Tc)L1/ν
(T −Tc)L1/ν

FIG. S2. Collapse of ⟨q2⟩in the critical region for classical spin glasses. Finite-size collapses are shown for classical
3D spin glasses on the simple cubic lattice, along with the dimer-embedded lattices with varying JFM/JG, using identical
parameters Tc = 1.1, ν = 1.5, b = 0.61. The value of ν is far from recent estimates but provides a good collapse for these small
systems, regardless of embedding, suggesting that dimer-embedding does not cause a large change to Tc. The largest deviations
from the simple cubic model are seen for small JFM/JG, as one would expect.

a
b

0.2

L = 4
L = 6
L = 8
L = 10
L = 12

⟨m2⟩

0.1

0.05

0.01

0.005

L = 5
L = 6
L = 7
L = 8
L = 9

⟨q2⟩

0.002

0.001

2D ferromagnet
3D spin glass

2
5
10

TLz

2
5
10

TLz

FIG. S3. Susceptibility as a function of temperature for quantum models. a, 2D ferromagnet (Γ = 3.06) and b,
embedded 3D spin glass with JFM/JG = 2 (Γ = 2.9). In the case of the ferromagnet, we use the standard linear susceptibility
⟨m2⟩in place of ⟨q2⟩. Near the critical Γ, susceptiblity is small at high temperature and reaches a peak value as temperature is
decreased. Each model and size has data for 1024 temperatures. Solid colored lines indicate a 64-temperature moving average,
dashed lines indicate moving averages of bootstrap 95% conﬁdence intervals, and data with error bars indicate a subset of
individual temperatures and bootstrap conﬁdence intervals, selected for visual clarity. Black lines indicate polynomial ﬁts to
log-log data, with maxima marked with ×. Bootstrapping is done over 400 independently annealed realizations (all realizations
being identical for the ferromagnet). Rescaling the temperature by Lz with z = 1 (left) and z = 1.3 (right) leads to reasonably
well horizontally-aligned maxima, consistent with previous studies.

## Page 38

Γc = 2.89
1/ν = 1.55
bq = 2.80

3

2.5

2

⟨q2⟩Lbq

1.5

1

−4
−3
−2
−1
0
1
2
3
4
0.5

(Γ −Γc)L1/ν

FIG. S4. Collapse of peak susceptibility for embedded 3D quantum spin glass. Scaled susceptibility ⟨q2⟩Lbq collapses
as a function of reduced transverse ﬁeld (Γ−Γc)L1/ν in the vicinity of the QPT, for the embedded 3D system with JFM/JG = 2.
From ﬁtting the collapse we can determine ν, Γc, and bq. Error bars indicate S + 1 goodness-of-ﬁt intervals (see text).

TABLE I. Optimized collapse parameters for quantum spin glasses, with restriction of data to a rescaled interval |Γ−Γc|/Γc < 1.
Collapse values are determined by a χ2 method91. Parameters b and ν deviate slightly downward from expectations based on
the literature49,65, both for embedded and unembedded models. Aside from a large shift in the non-universal critical point,
foreseeable based on modiﬁcation of local tunneling rates, ﬁt quality is similar across all 3D models.

bars indicate values that lead to goodness of ﬁt at most S + 1. Outcomes for other models are shown in Table I. We
note that all models show 1/ν near 1.55, signiﬁcantly diﬀerent from the previously reported 1/ν ≈1.349, and we use
this new estimate in the main text.

As shown in Figure S3 the peak susceptibility in T for a given L and Γ can be established with reasonable conﬁdence.
We expect bq to describe the scaling of the peak height in the critical region, i.e. ⟨q2⟩max ∼L−bq; indeed we ﬁnd very
good agreement with this power-law form and ﬁnd very consistent estimates bq ≈2.8 for both logical and embedded
3D quantum spin glasses (Table I). In these simulations we were restricted in the largest value of L by convergence
requirements at low T and small Γ.

Similarly to the peak height, the peak location (in T) is expected to scale as L−z, so in principle we could use
this information to extract an estimate of the dynamic exponent z. Although the data in S3b are consistent with
the reported value of z ≈1.349, the data are not reliable enough to conﬁdently estimate z, owing to the ﬂat and
noisy nature of the peak for large systems. We note that in a random ferromagnetic transverse ﬁeld model study
based on a similar methodology, an alternative collapse form in temperature was successful77. If a similar inﬁnite
randomness ﬁxed point applied in the spin glass model, an exponential collapse form might prove valuable, but we
were unable based upon our data to establish z with conﬁdence based on such a hypothesis. (Our collapses use a peak
susceptibility value, and hence are robust with regards the scaling form in temperature, a strength of the method.)
We maintain the hypothesis that z ≈1.3, which despite the challenges of classical simulation, agrees well with our
quantum simulation data from the QA processor. The observed value of bq ≈2.8 diﬀers from Guo, Bhatt, and Huse’s
estimate bq ≈3.449.

In general, the FSS analysis appears to provide a good qualitative description of the quantum models at these small
scales. As in the classical case, collapses indicate that the scaling of the embedded models is very close to that of the
unembedded model. For these unembedded models we ﬁnd values that are—with the exception of η—not far from
those reported in the literature, but with important deviations in ν, where we use our estimate 1/ν ≈1.55 rather
than the previous estimate 1/ν ≈1.3. Diﬀerences in methodology may account for these deviations.

## Page 39

100

Spin-flip probability

10−1

10−2

FIG. S5. Freezing in SA. Spin-ﬂip acceptance probability varies as a function of JG, resulting in a freezing of dynamics at
high temperature for small JG. Three values of JG are shown, along with data for the logical model on a simple cubic lattice.

ρc
E

102
103
104

ta (MCS)

FIG. S6. Scaling of residual Ising energy density at the critical point. Results shown are analogous to Fig. 4a, with
SQA and SA anneals stopped at their respective critical points. SQA has κc = 0.61(3) with equilibrium Ising energy per site
≈−0.63, whereas SA has κc = 0.51(1) with equilibrium Ising energy per site ≈−1.79. Error bars indicate 95% bootstrap
conﬁdence intervals.

IV.
NONEQUILIBRIUM DYNAMICS OF SA AND SQA

A.
Freezing of dynamics in SA

The SA dynamics studied here proposes and accepts or rejects one spin update at a time, and proceeds along a
geometric schedule in β/JG. When JFM ≫JG, dynamics “freeze”—spin ﬂips become very unlikely to be accepted—at
a high temperature. To probe this phenomenon, we annealed L = 9 embedded 3D spin glasses with JG ∈{1/4, 1/2, 1},
as well as the corresponding logical (simple cubic) spin glasses, and tracked the probability of a spin ﬂip being accepted
at each sweep. Data are shown in Fig. S5.
For suﬃciently long anneals and large systems, this eﬀect should not change extracted KZ exponents. However,
there is a signiﬁcant eﬀect for the system sizes and anneal lengths probed in the main text, as evidenced by Extended
Data Figs. E6—E8.

B.
Energy decay at the critical point and inside the glass phase

As discussed in Section I, the form of energy decay at the critical point is subject to corrections within the glass
phase, and it is not obvious that Eq. (12) should hold even approximately. Here we investigate this question.

## Page 40

In Fig. 4, mean Ising energy at the end of the anneal for QA, SA, and SQA is compared to the putative ground-
state energy, giving a ﬁnal residual Ising energy density ρf
E. To study energy decay at the (quantum or classical)
critical point, we stop the anneal at the critical point—here this is Tc = 1.1 and Γc/J = 2.89 for SA and SQA
respectively, with JG = 1 (see Section III). We take the mean Ising energy for a given anneal time ta, and subtract
oﬀthe equilibrium Ising energy to obtain a critical Ising residual energy density ρc
E.
Here, the equilibrium Ising energy is estimated as a ﬁtting parameter to a best-ﬁt power-law form ρc
E ∝t−κc
a
. This
ﬁt is shown in Fig. S6. Based on the correction to Eq. (12), we may expect both SA and SQA to show κf < κc.
Indeed, for SA we see κc ≈0.51, κf ≈0.42. For SQA we see κc ≈0.61, κf ≈0.51. We note that the equilibrium Ising
energy per site is estimated at −0.63 at the quantum critical point for SQA, much higher than the value −1.79 at the
thermal critical point for SA. Eq. (12) predicts κc to be very close to the measured κf rather than the measured κc;
we attribute this mainly to ﬁnite size eﬀects.
Although we are not able to projectively read out QA states at the critical point, this evidence suggests that one
might expect QA to show κc > κf, more in line with Eq. (12).

V.
DATA COLLAPSE DOMAINS

All dynamics in this work are studied on the same geometries with the same boundary conditions (one periodic
dimension, 2 open dimensions). For this reason collapses are ideally performed over a range of ta such that the
observable, e.g., U, follows a consistent power-law scaling. Thus we discard fast annealing times that deviate from
this scaling. We also discard long annealing times where correlation length approaches system size, since this can lead
to anomalous boundary eﬀects. This window of ta varies from one dynamics to another. In particular, we restrict our
collapse for QA to the region ta ≤30 ns to minimize complications arising from decoherence and noise, which causes
a smooth increase in the observed KZ exponent µ.
In Fig. S7 we plot µ for QA, SA, and SQA across sliding windows of ta. These windows are chosen to span a given
dynamic range in ta: tmin ≤ta ≤3tmin for QA and tmin ≤ta ≤6tmin for SA and SQA; using diﬀerent dynamic ranges
is justiﬁed due to the polynomial speedup in QA compared to the software solvers. Only windows containing at least
6 measured annealing times are considered. As explained in the Methods section, conﬁdence intervals are generated
from combined jackknife standard errors across system sizes and annealing times. The conﬁdence intervals for the
individual windows overlap the conﬁdence intervals for the overall region of data collapse; annealing times that are
deemed too fast or too slow are shown in gray.
There are several potential causes for the observed increase in µ for increasing ta in QA. Decoherence and noise,
as mentioned above, are leading causes. Deviation between the rf-SQUID ﬂux qubit model and the transverse-ﬁeld
Ising model may also play a role.

VI.
EFFECT OF TEMPERATURE ON QA

Measurements in the main text were collected on a ﬁrst quantum processing unit (QPU1) at a cryostat set-point of
12 mK. To probe the eﬀect of temperature, we performed measurements on a second QPU (QPU2) at temperatures
varying from 12 mK to 21 mK. KZ exponents µ were extracted using annealing times ranging from 8.1 ns to 30 ns,
with results shown in Fig. S8. Measurements are insensitive to temperature over this parametric range, supporting a
hypothesis of a coherent regime with negligible interaction with the environment.

VII.
CALIBRATION REFINEMENT

Symmetries in the Ising Hamiltonian provide an opportunity to suppress calibration imperfections. This has been
shown to be very eﬀective for geometrically-frustrated low-dimensional systems35,36,88,92,93. In this work we study
thousands of spin-glass realizations, and it is impractical to extensively reﬁne the calibration for each one. Instead,
we tune only two aspects of the calibration: First, we balance qubits at degeneracy—with average magnitude zero—
using ﬂux oﬀsets. Second, we synchronize the eight annealing lines that control the annealing schedule of eight sets
of qubits, using anneal oﬀsets. The latter is most relevant for the fastest anneals, since desynchronization between
annealing lines is on the order of 1 ns or less. For both of these reﬁnements we use the same approach as was taken
in Ref.32, without tuning individual couplings; we refer the interested reader to the supplementary material of Ref.32

for more detail. For each selection of parameters (L, JG, ta, and pAFM) we perform an independent iterative shim for
both ﬂux oﬀsets and anneal oﬀsets; each of these oﬀsets is programmable on a per-qubit basis.

## Page 41

tmax (MCS)

SQA

6 · 102
6 · 103

102
103

tmin (MCS)

tmax (ns)

QA

18
24
30
45

6
8
10
15

tmin (ns)

tmax (MCS)

tmax (MCS)

6 · 102
6 · 103

6 · 102
6 · 103

102
103

102
103

tmin (MCS)

tmin (MCS)

tmax (ns)

tmax (ns)

18
24
30
45

18
24
30
45

6
8
10
15

6
8
10
15

tmin (ns)

tmin (ns)

FIG. S7. Data collapse windows. Each dynamics (SA, SQA, and QA) is run for varying annealing times; cumulants and
order parameters are collapsed over a subset of these times.
For each dynamics and each JG ∈{0.50, 0.75, 1.0}, the 95%
conﬁdence interval for the extracted exponent µ (Fig. 3e) is shown as a shaded region. To test self-consistency, we extract µ
for annealing time windows [tmin, ktmin] where k = 3 for QA, k = 6 for SA and SQA (see text). Windows within the collapse
range used to determine µ are shown in color; windows intersecting unused annealing times are shown in gray.

## Page 42

3.2

3

2.8

μ

2.6

2.4

2.2

12
14
16
18
20

T (mK)

FIG. S8. Kibble-Zurek exponents for varying temperature. Main-text measurements on QPU1 at 12 mK are compared
against a second QA processor, QPU2, operating at a range of temperatures. Error bars indicate jackknife 95% conﬁdence
intervals over system sizes and anneal times.

For i ∈{1, . . . , 8} let Vi denote the set of qubits on annealing line i, and for i, j ∈{1, . . . , 8} let Eij denote the set
of couplings coupling a qubit in Vi to a qubit in Vj.
We perform the shim based on two assumptions:

• All qubits should have average magnetization zero.

• The average frustration probability of a coupler in Eij—that is, the average observed probability of a nonzero
coupler between Vi and Vj having a positive contribution to the energy, where the average is taken over both
samples and realizations—should be eﬀectively independent of the choice of i and j.

The ﬁrst assumption is trivially justiﬁed because there are no longitudinal ﬁelds used in the Ising Hamiltonian in this
work. For the second, we assume that the sets Eij are large and suﬃciently spatially uncorrelated from the position
in the 3D lattice position. This assumption is reasonable because the annealing line assignments follow a regular
geometric pattern and the 3D lattice embeddings are determined with a heuristic random approach.
In Fig. S9a we show the ﬁnal anneal oﬀsets for the eight annealing lines after 1200 iterations on L = 12 3D spin
glasses. In Fig. S9b we show the distribution of average frustration in a glass coupling incident to each annealing
line.
Data are shown with and without the anneal oﬀset and ﬂux oﬀset shim, for ta = 6.2 ns and 30 ns.
The
calibration reﬁnement shim has a clear homogenizing eﬀect on the per-line frustration. In Fig. S9c we show the
average magnetization of each qubit over the ﬁnal 300 of 1200 iterations with and without the shim, which has a
clearly beneﬁcial eﬀect in balancing the qubits at zero magnetization.
In Fig. S10 we show the eﬀect of calibration reﬁnement on the dynamic scaling of the order parameter and Binder
cumulant. These data make it clear that the calibration reﬁnement is necessary to obtain reasonable estimates of
critical exponents. However, we are focusing on a regime far outside the speciﬁcations of the calibration being reﬁned,
which is intended for ta ≥500 ns.

VIII.
RESIDUAL ENERGY DECAY

In Fig. S11 we show decay of residual energy for three dynamics: QA, SA, and SQA. For the MC solvers (i.e., SA
and SQA), we show this both in terms of MCS and in terms of computation time. We measured times per MCS on
a CPU (Intel® Core™i7-7700HQ CPU @ 2.80GHz): 0.4 ms for SA and 8.5 ms for SQA. We call out two caveats:

• SQA time per sweep is approximately linearly dependent on β, and we have used a high value β = 64 throughout
(relative to crossing point Γ(s) = J(s); see Methods), to minimize thermal eﬀects. However, even with a lower
β, SQA is not competitive with SA on the systems studied here.

• The codes used are reasonably fast but are written to be general, without optimizations such as lattice-speciﬁc
memory structure, function lookup tables, static spin ordering for sweeps (which deviates from standard interpre-
tations of quasi-physical dynamics), and random number reuse. SA in particular can be sped up signiﬁcantly,
so we show SA annealing time using the quoted time of 2.42 spin ﬂips per nanosecond (0.4 ns per spin ﬂip)
for a highly optimized version of SA measured on an Intel® Xeon™E5-2670 CPU @ 2.60GHz (94, Table 4,
an ss ge fi).

## Page 43

a

0.1

Anneal offset

0

-0.1

6
10
20
30

ta (ns)

ta = 6.2 ns
ta = 30 ns

b

0.26

0.24

Frustration

0.22

0.2

0.18

0.16

Annealing line

c

Frequency

−0.4 −0.2
0
0.2
0.4

Qubit magnetization

Annealing line

−0.4 −0.2
0
0.2
0.4

Qubit magnetization

FIG. S9. Calibration reﬁnement. a, Anneal oﬀsets (unitless, in s) are tuned to synchronize eight annealing lines for fast
anneals. b, Anneal oﬀsets are learned through a loss function related to inhomogeneity of frustration of couplings incident to the
qubits on each annealing line. Flux oﬀsets are learned through a loss function that minimizes nonzero average magnetization of
individual qubits. Tuning these improves the homogeneity of frustration with respect to annealing line. c, Systematic nonzero
magnetization for the qubits is also reduced.

As previously noted in Section II C, the ground state energies of these “embedded” spin glasses, which use two-qubit
ferromagnetic dimers, can generally be found by instead solving a reduced “logical” problem on a simple cubic lattice.
Therefore we also compare QA performance on the embedded spin glasses against MC dynamics solving the logical
spin glasses. Although the primary aim of this work is to study quantum critical spin-glass dynamics, it is notable
that QA outperforms SA—both in scaling (in the coherent QA regime) and in absolute terms—even when QA has
an embedding overhead that does not aﬀect SA.

## Page 44

without shim

10−1.5

⟨q2⟩

10−2

10
20
30

ta (ns)

with shim

10−2

⟨q2⟩

10
20
30
10−3

ta (ns)

10−0.5

U

10−1

10
20
30
10−1.5

ta (ns)

10−1

U

10−2

10−3

10
20
30

ta (ns)

FIG. S10. Eﬀect of shim on dynamic scaling. Shown in the top and bottom rows, respectively, are Binder cumulant U
and order parameter ⟨q2⟩with and without the anneal oﬀset (synchronization) and ﬂux oﬀset (balancing) shim. Data are for
3D lattices, JG = 0.5.

## Page 45

Monte Carlo dynamics solve same embedded 3D spin glass as QA

100

10−1

100

10−1

FIG. S11. Residual energy decay. We compare ρE as a function of ta for QA, SA, and SQA. The top row shows data for
MC dynamics running on the same Ising model as QA, with two-qubit FM dimers. The bottom row shows the same data for
QA, but with MC dynamics running on a reduced Ising model on a simple cubic lattice, in which two-qubit FM dimers have
been contracted into single logical variables, reducing both time per sweep and the number of sweeps required to reach a given
ρE. The right-hand plots show annealing time in nanoseconds. For SQA we use measured sweep times; for SA we use a time
of 0.4 ns per spin update as reported in Ref.94 for a highly optimized SA code. Our SQA timescales rely on worldline updates,
for which open-source code is provided88.
