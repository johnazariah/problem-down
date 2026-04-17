---
source_pdf: ../arxiv_cond-mat_0602085.pdf
pages: 12
extracted_at: 2026-04-17T12:32:45+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_cond-mat_0602085

Source PDF: ../arxiv_cond-mat_0602085.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

Feedback-optimized parallel tempering Monte Carlo

Helmut G. Katzgraber,1 Simon Trebst,1, 2, 3 David A. Huse,4 and Matthias Troyer1

1Theoretische Physik, ETH Z¨urich, CH-8093 Z¨urich, Switzerland
2Computational Laboratory, ETH Zentrum, CH-8092 Z¨urich, Switzerland
3Microsoft Research and Kavli Institute for Theoretical Physics,
University of California, Santa Barbara, CA 93106, USA
4Department of Physics, Princeton University, Princeton, NJ 08544, USA
(Dated: February 3, 2008)

arXiv:cond-mat/0602085v3 [cond-mat.other] 30 Mar 2006

We introduce an algorithm to systematically improve the eﬃciency of parallel tempering Monte
Carlo simulations by optimizing the simulated temperature set. Our approach is closely related to a
recently introduced adaptive algorithm that optimizes the simulated statistical ensemble in general-
ized broad-histogram Monte Carlo simulations. Conventionally, a temperature set is chosen in such
a way that the acceptance rates for replica swaps between adjacent temperatures are independent
of the temperature and large enough to ensure frequent swaps. In this paper, we show that by
choosing the temperatures with a modiﬁed version of the optimized ensemble feedback method we
can minimize the round-trip times between the lowest and highest temperatures which eﬀectively in-
creases the eﬃciency of the parallel tempering algorithm. In particular, the density of temperatures
in the optimized temperature set increases at the “bottlenecks” of the simulation, such as phase
transitions. In turn, the acceptance rates are now temperature dependent in the optimized tem-
perature ensemble. We illustrate the feedback-optimized parallel tempering algorithm by studying
the two-dimensional Ising ferromagnet and the two-dimensional fully-frustrated Ising model, and
brieﬂy discuss possible feedback schemes for systems that require conﬁgurational averages, such as
spin glasses.

PACS numbers: 75.50.Lk, 75.40.Mg, 05.50.+q

Parallel tempering Monte Carlo [9] has proven to be
a strong “workhorse” in ﬁelds as diverse as chemistry,
physics, biology, engineering, and material science [10].
Similar to replica Monte Carlo [11], simulated tempering
[12], or extended ensemble methods [13], the algorithm
aims to overcome entropic barriers in the free energy
landscape by simulating a broad range of temperatures.
This allows the system to escape metastable states when
wandering to higher temperatures and subsequently re-
laxing at lower temperatures again on time scales that
are substantially smaller than conventional simulations
at a ﬁxed temperature. In this paper, we maximize the
eﬃciency of parallel tempering Monte Carlo by optimiz-
ing the distribution of temperature points in the simu-
lated temperature set such that round-trip rates of repli-
cas between the two extremal temperatures in the sim-
ulated temperature set are maximized. The optimized
temperature sets are determined by an iterative feed-
back algorithm that is closely related to the previously
mentioned adaptive ensemble optimization method for
broad-histogram Monte Carlo simulations [1]. The feed-
back method concentrates temperature points near the
bottleneck of a simulation, typically in the vicinity of a
phase transition or the ground state of the system. As a
consequence, we ﬁnd that for the optimal choice of tem-
peratures the acceptance probabilities for swap moves
between neighboring temperature points show a strong
modulation with temperature and are not independent
of temperature as suggested in several recent approaches
[14, 15, 16, 17, 18, 19].
The paper is structured as follows: In Sec. II we present
a detailed introduction of the parallel tempering Monte

I.
INTRODUCTION

The free energy landscapes of complex systems are
characterized by many local minima that are separated
by entropic barriers. The simulation of such systems with
conventional Monte Carlo methods is slowed down by
long relaxation times due to the suppressed tunneling
through these barriers. Extended ensemble simulations
address this problem by broadening the range of phase
space which is sampled in the respective reaction coordi-
nate. Recently, an adaptive algorithm [1] has been intro-
duced that explores entropic barriers by sampling a broad
histogram in a reaction coordinate and iteratively opti-
mizes the simulated statistical ensemble deﬁned in the re-
action coordinate to speed up equilibration. The key idea
of the approach is to measure the local diﬀusivity along
the reaction coordinate, thereby identifying the bottle-
necks in the simulations and then using this information
to systematically shift statistical weights towards these
bottlenecks in a feedback loop. The optimized histogram
converges to a characteristic form exhibiting peaks at the
bottlenecks of the simulation, e.g., in the vicinity of the
entropic barriers. The simulation of an optimized ensem-
ble results in equilibration times that can be substantially
lower compared to other extended ensemble simulations
that aim at sampling a ﬂat histogram in the respective
reaction coordinate [1, 2]. Flat-histogram algorithms in-
clude the multicanonical method [3, 4], broad histograms
[5] and transition matrix Monte Carlo [6] when combined
with entropic sampling, as well as the adaptive algorithm
of Wang and Landau [7, 8].

## Page 2

Tmax

Carlo method.
In Sec. III we generalize the feedback
method of Ref. 1 to the parallel tempering Monte Carlo
algorithm. Results on two paradigmatic models, the two-
dimensional Ising ferromagnet and the two-dimensional
fully-frustrated Ising model are presented in Sec. IV, as
well as a discussion on how to proceed with systems that
require conﬁgurational averages, such as spin glasses.
Concluding remarks follow in Sec. V.

II.
PARALLEL TEMPERING MONTE CARLO

In the parallel tempering Monte Carlo algorithm [9,
11, 12, 13], M non-interacting replicas of the system
are simulated simultaneously at a range of temperatures
{T1, T2, . . . , TM}. After a ﬁxed number of Monte Carlo
sweeps a sequence of swap moves, the exchange of two
replicas at neighboring temperatures, Ti and Ti+1, is sug-
gested and accepted with a probability

p(Ei, Ti →Ei+1, Ti+1) = min {1, exp(∆β∆E)} ,
(1)

where ∆β = 1/Ti+1 −1/Ti is the diﬀerence between the
inverse temperatures and ∆E = Ei+1 −Ei is the diﬀer-
ence in energy of the two replicas. At a given tempera-
ture, an accepted swap move eﬀects in a global update
as the current conﬁguration of the system is exchanged
with a replica from a nearby temperature. For a given
replica, the swap moves induce a random walk in tem-
perature space. This random walk allows the replica to
overcome free energy barriers by wandering to high tem-
peratures where equilibration is rapid and return to low
temperatures where relaxation times can be long. The
simulated system can thereby eﬃciently explore complex
energy landscapes that can be found in frustrated spin
systems [20], spin glasses [21, 22, 23] or proteins [24].
While the simulation of M replicas takes M times more
CPU time, the speedup attained with parallel temper-
ing Monte Carlo can be orders of magnitude larger. In
addition, one often wishes to measure observables as a
function of temperature. Thus parallel tempering Monte
Carlo delivers already several measurements at diﬀerent
temperatures in one simulation. In order to maximize the
number of statistically independent visits at low temper-
atures, we want to maximize for each replica the number
of round-trips between the lowest and highest tempera-
ture, T1 and TM, respectively. The rate of round-trips
of a replica strongly depends on the simulated statisti-
cal ensemble, that is the choice of temperature points
{T1, T2, . . . , TM} in the parallel tempering simulation.
In this paper, we present an algorithm that systemati-
cally optimizes the simulated temperature set to max-
imize the number of round-trips between the two ex-
tremal temperatures T1 and TM for each replica and
thereby substantially improve equilibration of the system
at all temperatures.
Conventional approaches assume
that to achieve this goal, the simulated temperature set
should be chosen in such a way that the probability for
replica swap moves at neighboring temperatures should

τrt
Tmin

FIG. 1: (Color online) Sketch of the random walk that a
given replica performs in temperature space in the course of
the simulation. Ideally, the replica will wander up (τup) and
down (τdown) in the simulated temperature range [Tmin, Tmax].
The goal of the feedback method is to maximize the number of
round trips each replica performs in this temperature range,
and thereby minimize the average round-trip time τrt = τup +
τdown.

be “ﬂat”, that is approximately independent of temper-
ature. If the speciﬁc heat of the system is assumed to be
constant, then a good approximation for such a temper-
ature set can be attained with a geometric progression
[17]. Given a temperature range [T1, TM], the intermedi-
ate M −2 temperatures can be computed via

i=1
Ri
Ri =
M−1
r

k−1
Y

TM

Tk = T1

T1
.
(2)

The geometric progression peaks the number of tem-
peratures around the minimum temperature T1 where
a slower relaxation is assumed. This is not optimal when
the system has a diverging speciﬁc heat (at an interme-
diate temperature): Because in order to ensure enough
overlap between the energy distributions of neighboring
temperatures ∆Ti,i+1 ∼CV Ti/
√

N, where CV is the spe-
ciﬁc heat per spin and N the number of spins, the accep-
tance probabilities are inversely correlated to the func-
tional behavior of CV via the inverse beta function law
[17]. Thus, for example at a phase transition where the
speciﬁc heat diverges, the acceptance probabilities for a
geometric temperature set will show a pronounced dip
(cf. Sec. IV A). More complex methods such as the ap-
proach by Kofke [14, 15], its improvement by Rathore
et al. [16], as well as the method suggested by Predescu
[17, 18] aim to obtain acceptance probabilities for the
parallel tempering moves that are independent of tem-
perature by compensating for the eﬀects of the speciﬁc
heat. In particular, Kone and Kofke [19] suggest that an
acceptance probability of 23% is optimal. In this work
we show that this is not necessarily the optimal case.

III.
TEMPERATURE SET OPTIMIZATION

Our goal is to vary the temperature set {Ti} of a par-
allel tempering simulation in such a way that for a given
system we speed up equilibration at all temperatures. To
accomplish this, we maximize the rate of round trips that

## Page 3

each replica performs between the two extremal temper-
atures Tmin = T1 and Tmax = TM following a similar ap-
proach to the ensemble optimization technique presented
in Ref. [1]. For a given temperature set, we can measure
the diﬀusion of a replica through temperature space by
adding a label “up” or “down” to the replica that indi-
cates which of the two extremal temperatures, Tmin or
Tmax respectively, the replica has visited most recently.
The label of a replica changes only when the replica visits
the opposite extreme. For instance, the label of a replica
with label “up” remains unchanged if the replica returns
to the lowest temperature Tmin, but changes to “down”
upon its ﬁrst visit to Tmax. This is illustrated in Fig. 1.
For each temperature point in the temperature set {Ti},
we record two histograms nup(Ti) and ndown(Ti).
Be-
fore attempting a sequence of swap moves, we increment
that histogram at temperature Ti which has the label of
the respective replica currently at temperature Ti. If a
replica has not yet visited either of the two extremal tem-
peratures, we increment neither of the histograms. This
allows us to evaluate for each temperature point the frac-
tion of replicas which have visited one of the two extremal
temperatures most recently (e.g., Tmin) as

f(Ti) =
nup(Ti)

nup(Ti) + ndown(Ti) .
(3)

The labeled replicas deﬁne a steady-state current j
from Tmin to Tmax that is independent of temperature,
e.g., the rate at which “up” walkers are created at Tmin
and – in equilibrium – absorbed at Tmax. In the following
we assume that T is a continuous variable, independent
of the temperature points in the current temperature set.
We can then determine the current j to ﬁrst order in the
derivative as

j = D(T )η(T ) df

dT ,
(4)

where D(T ) is the local diﬀusivity at temperature T and
the derivative df/dT is estimated by a linear regression
based on the measurements in Eq. (3); η(T ) is a density
distribution indicating the probability for a replica to
reside at temperature T . We approximate η(T ) with a
step-function η(T ) = C/∆T , where ∆T = Ti+1−Ti is the
length of the temperature interval around temperature
Ti < T < Ti+1 for the current temperature set.
The
normalization constant C is chosen such that
Z TM

T1
η(T )dT = C
Z TM

dT

∆T = 1 .
(5)

T1

Rearranging Eq. (4) gives a simple measure of the local
diﬀusivity D(T ) of a replica at temperature T

D(T ) ∼
∆T

df/dT ,
(6)

where we have dropped the normalization constant C and
the current j which is constant for any speciﬁc choice of
temperature set.

To increase the eﬃciency of the algorithm, we maxi-
mize the current j in temperature space by varying the
simulated temperature set {Ti} and thus varying the
probability distribution η(T ) between the two extremal
temperatures, Tmin and Tmax, which are not changed. In
Ref. 1 it has been shown that the optimal probability dis-
tribution ηopt(T ) is inversely proportional to the square
root of the local diﬀusivity D(T ):

ηopt(T ) ∝
1

p

D(T )
.
(7)

For the optimal distribution of temperature points the
fraction f opt(T ) then decays as

opt
= ηopt(T ) ∝
1

df

∆T opt ,
(8)

dT

which implies that for any given temperature interval
∆T = Ti+1 −Ti of the optimal temperature set the frac-
tion has a constant decay

∆f opt = f opt(Ti) −f opt(Ti+1) = 1/(M −1) ,
(9)

where M is the number of replicas.
In our algorithm we approach the optimal temperature
set and its respective probability distribution by itera-
tively feeding back measurements of the local diﬀusivity.
After measuring the diﬀusion of replicas for a given tem-
perature set an improved probability distribution η′(T )
is found as

∆T ′ = C′
r

η′(T ) = C′

∆T
df

1

dT ,
(10)

where the normalization constant C′ is again chosen so
that the normalization condition in Eq. (5) is met. The
step-function η′(T ) is still deﬁned for the original temper-
ature set, that is the jumps in the function occur at the
temperature points in {Ti}. The optimized temperature
set {T ′
i} is then found by choosing the k-th temperature
point T ′
k such that

Z T ′
k

T ′
1
η′(T )dT = k

M ,
(11)

where 1 < k < M and the two extremal temperatures
T ′
1 = T1 and T ′
M = TM remain ﬁxed.
We summarize the feedback algorithm by the following
sequence of steps

• Start with a trial temperature set {Ti}.

• Repeat

◦Reset the histograms nup(T ) = ndown(T ) = 0.

◦For the current temperature set perform a
parallel tempering simulation with Nsw swap
moves. After each sequence of swap moves:

Update the labels of all replicas.

## Page 4

Record histograms nup(T ) and ndown(T ).

◦For the given temperature set estimate an op-
timized probability distribution η′(T ) via

η′(T ) = C′
r

∆T
df

1

dT .

◦Obtain the optimized temperatures {T ′
i} via

Z T ′
k

T1
η′(T )dT = k

M .

◦Increase the number of swaps Nsw ←2Nsw.

• Stop once the temperature set {Ti} has converged.

The initial number of swaps Nsw should be chosen large
enough such that a few of round-trips are recorded,
thereby ensuring that steady-state data for nup(T ) and
ndown(T ) are measured.
The derivative df/dT can be
determined by a linear regression, where the number
of regression points is ﬂexible. Initial batches with the
limited statistics of only a few round trips may require
a larger number of regression points than subsequent
batches with smaller round-trip times and better statis-
tics.

FIG. 2: (Color online) Fraction f(T) of replicas diﬀusing from
the lowest to the highest temperature as a function of the
temperature index for the ferromagnetic Ising model.
For
the initial temperature set based on a geometric progression
(ﬁlled squares), the fraction shows a sharp drop between two
temperature points. A similar behavior is found for a tem-
perature set where the acceptance rates are constant ∼40%
independent of temperature (temperature set with “ﬂat” ac-
ceptance rates, open squares). In contrast, for the optimized
temperature set (triangles) the fraction constantly decreases.
The inset shows the fraction as a function of temperature T.
The dashed line in the inset represents the critical tempera-
ture of the two-dimensional Ising model, Tc ≈2.269.

IV.
RESULTS

A.
Ferromagnetic Ising model

In order to illustrate the feedback method, we start
with a simple test model, the two-dimensional ferromag-
netic Ising model (FM). The Hamiltonian for the model
is given by

replicas wandering from the lowest to the highest tem-
perature using an additional label for each replica as de-
scribed above. In Fig. 2 we show the fraction of replicas
diﬀusing “up” in temperature space.
For the geomet-
ric temperature set a sharp drop between two tempera-
ture points is observed close to the critical region of the
phase transition at Tc ≈2.269. Similar results are also
found for a “ﬂat” temperature set where the acceptance
rates are approximately constant around ∼40% (with
ﬂuctuations of ∼10%) and independent of temperature,
although the drop is not as pronounced.
Calculating the local diﬀusivity D(T ) for the random
walk in temperature space using Eq. (6), we ﬁnd a strong
suppression around this critical region as illustrated in
Fig. 3. When increasing the size of the simulated sys-
tem, the dip in the local diﬀusivity further proliferates,
an additional indicator that the slowdown of the random
walk in temperature space is dominated by the occur-
rence of a phase transition. Note the logarithmic scale of
the ordinate axis in Fig. 3.
When applying the feedback, Eq. (11), to deﬁne a new
temperature set, this suppression in the local diﬀusivity
leads to a concentration of temperature points near the
critical temperature as shown in Fig. 4. The feedback
thereby tries to compensate for the reduced mobility of

HFM = −J
X

⟨i,j⟩
SiSj ,
(12)

where J = 1 and Si = ±1 represent Ising spins on
a square lattice with N = L2 spins.
In our simula-
tions we apply periodic boundary conditions and con-
sider nearest-neighbor interactions only. The simple Ising
model with uniform couplings has no frustration or dis-
order, and exhibits a second-order phase transition at
Tc = 2/ ln(1 +
√

2) ≈2.269 from a magnetically ordered
to a paramagnetic phase.
For simplicity, we deﬁne an initial temperature set
{Ti} with M = 21 temperature points performing a ge-
ometric progression, Eq. (2), for a temperature interval
[T1 = 0.1, TM = 10.0]. The minimum temperature T1
is chosen low enough such that the system can approach
the zero-temperature ground state of the model, and the
maximum temperature TM is chosen well above the crit-
ical region of the phase transition.
For a short paral-
lel tempering simulation (Nsw = 1.6 · 107, one parallel
tempering swap after each lattice sweep) using this ini-
tial temperature set, we measure the diﬀusive current of

## Page 5

FIG. 3: (Color online) Local diﬀusivity D(T) of the random
walk a replica performs in temperature space for the ferro-
magnetic Ising model as a function of temperature T after
the feedback optimization for several system sizes L. Notice
the logarithmic vertical scale. The vertical dashed line repre-
sents Tc ≈2.269.

FIG. 5: (Color online) Acceptance probabilities A(T) as a
function of temperature T for the ferromagnetic Ising model.
The inset shows the acceptance rates as a function of temper-
ature in the optimized case for varying system sizes L and a
ﬁxed number of temperature points. The vertical dashed line
marks the critical temperature.

replicas in the critical region by reallocating resources to-
wards this temperature range. In contrast, the density of
temperatures close to the lowest temperature is greatly
reduced, thereby suppressing constant swapping of repli-
cas at low temperatures where for the initial tempera-
ture set multiple replicas converged to the fully-polarized
ground state conﬁguration.
This eﬀect becomes even more evident when measuring
the acceptance probabilities for swap moves as illustrated
in Fig. 5. The acceptance probabilities for the initial tem-
perature set based on a geometric progression saturate
close to unity for temperatures below T ≲0.7, whereas
they show a pronounced dip already for small system
sizes (L = 20) around the critical temperature (marked
by a vertical dashed line).
In contrast, the feedback-
optimized temperature set shows a pronounced peak in
the acceptance rate A(T ) near the critical temperature
where temperature points are accumulated by the feed-
back. Away from the critical temperature region the ac-
ceptance probabilities drop. The inset of Fig. 5 shows the
acceptance probabilities A(T ) for the optimized tempera-
ture sets for a ﬁxed number of replicas and varying sizes of
the simulated system. While the acceptance probability
around the critical temperature remains nearly constant,
the exact value away from the critical region decreases
with increasing system size.
This “mean” acceptance
probability away from the bottleneck of the simulation
can be tuned by varying the number of simulated repli-
cas.
The fact that for the optimized temperature set the
acceptance probabilities vary with temperature contra-
dicts various alternative approaches in the literature

FIG. 4: (Color online) Temperature sets for the ferromag-
netic Ising model for diﬀerent feedback steps. Starting from
a geometric progression temperature set (step 0), we apply
a feedback loop until the temperature set converges. While
the geometric progression places many temperatures at low
temperatures, the density of temperatures after the feedback
optimization is highest at the bottleneck of the simulation
around the critical temperature (marked by a vertical dashed
line). Rapid convergence of the optimized temperature set is
found after 3 – 4 feedback steps and a total of Nsw ≈1.6 · 107

swap moves in our parallel tempering simulations.

## Page 6

times

FIG. 6: (Color online) Average round-trip times

τ rt before the
optimization divided by the average round-trip times after the
feedback optimization (

τ opt
rt ) as a function of system size. The
data for the ﬁlled squares are for a system starting from a geo-
metric progression and represent the speedup obtained by the
feedback method. The open symbols correspond to a temper-
ature set which initially has “ﬂat” acceptance probabilities.
The dashed lines are guides to the eye.

[15, 16, 17, 18, 19] that aim at choosing a tempera-
ture set in such a way that the acceptance probability of
attempted swaps becomes independent of temperature.
Naively, one might assume that the choice of constant
acceptance rates produces an unbiased random walk in
temperature space. This assumption is similar to the idea
underlying generalized-ensemble algorithms that aim to
sample a ﬂat histogram in the energy such as the multi-
canonical method [3, 4] or the Wang-Landau algorithm
[7, 8]. For these ﬂat-histogram algorithms, it has been
shown that they cannot reproduce the scaling behavior
of an unbiased Markovian random walk in energy space,
but experience critical slowing down [2]. This slowdown
can be overcome by optimizing the simulated statistical
ensemble by a similar feedback algorithm [1] as presented
here and sampling an optimized histogram that in general
is not ﬂat, but reallocates resources towards the bottle-
neck of the simulation, e.g., in the vicinity of a phase
transition or close to the ground state of the system.
Measuring the diﬀusion of replicas in a subsequent sim-
ulation for the optimized temperature set, we ﬁnd that
the current of replicas wandering from the lowest to the
highest temperature is now characterized by a constantly
decreasing fraction f(T ) in agreement with Eq. (9) as
shown in Fig. 2 (triangles). In addition, we ﬁnd that for
the optimized temperature set the replicas wander evenly
up and down in temperature space, that is τup ≈τdown.
In Fig. 6 we show the ratio between the mean round-
trip times

τ rt before optimization from a geometric and
“ﬂat” temperature set divided by the mean round-trip

τ opt
rt
after optimization in order to illustrate the
speedup in replica diﬀusion attained by the feedback
procedure.
The data show clearly for all system sizes
that the round-trip times after the optimization of the
temperature set do not increase as fast as for a geomet-
ric progression or “ﬂat” temperature set. Note that for
these temperature sets with a ﬁxed number of tempera-
ture points the average round-trip times before and after
the feedback optimization scale ∼exp(aLb) for the sys-
tem sizes studied. It is important to note that our algo-
rithm identiﬁes the bottleneck of the parallel tempering
simulation that in this model occurs in the form of criti-
cal slowing down at the phase transition solely based on
measurements of the local diﬀusivity. The feedback then
allows to shift additional resources towards this bottle-
neck in a quantitative way. In the next section, we apply
the algorithm to a more complex model with frustration
and a diﬀerent type of phase transition at zero tempera-
ture.

B.
Fully-frustrated Ising model

The Hamiltonian of the fully-frustrated (FF) Ising
model is given by

HFF = −
X

⟨i,j⟩
JijSiSj ,
(13)

where the spins lie on the vertices of a two-dimensional
square lattice with periodic boundary conditions. The
bonds Jij are chosen such that |Jij| = 1, but with the
constraint that the product of the bonds around all pla-
quettes of the system is negative, i.e.,
Y

□
Jij = −1 .
(14)

The model does not order at ﬁnite temperatures, but ex-
hibits a critical point at zero temperature. In the vicin-
ity of this transition to a highly degenerate ground-state
manifold, the system relaxes very slowly.
In this section, we discuss our feedback optimiza-
tion algorithm for two choices of the initial tempera-
ture set.
First we start from the temperature set in-
troduced in Sec. IV A computed with a geometric pro-
gression, Eq. (2), which has Tmin = 0.1, Tmax = 10.0 and
M = 21 temperatures. In this ﬁrst approach, we keep
the number of temperature points constant for all sys-
tem sizes L. In the second approach, we choose an initial
temperature set where we ﬁx again Tmin and Tmax to the
aforementioned values but tune the number of tempera-
tures M as well as their position in such a way that we
obtain acceptance probabilities for swap moves that are
approximately independent of the temperature (“ﬂat”)
with a mean value of A(T ) ∼40% and deviations around
this mean value of maximally 10% [25].
We show the fraction f(T ) of replicas diﬀusing from
the lowest to the highest temperature as a function of

## Page 7

FIG. 7: (Color online) Fraction f(T) of replicas diﬀusing from
the lowest to the highest temperature for the fully frustrated
Ising model.
Displayed are data for an initial “ﬂat” tem-
perature set with M = 21 temperature points that yields
temperature-independent acceptance probabilities for swap
moves (open squares). In addition, data for a geometric pro-
gression (M = 21) are also shown (ﬁlled squares). After the
optimization, the change in the fraction is independent of the
temperature index (triangles). The inset shows the fractions
as a function of temperature T. Data for Nsw = 2 · 106.

FIG. 8: (Color online) Local diﬀusivity D(T) of a random
walk in temperature space for the fully-frustrated Ising model
as a function of temperature T after the feedback optimization
for several system sizes L.
Notice the logarithmic vertical
scale.

the temperature index in Fig. 7.
Similar to the Ising
model, the data for the geometric progression tempera-
ture set deviate considerably from a straight line which
is expected for the optimal temperature distribution. A
similar behavior is found when starting from a temper-
ature set that initially has temperature-independent ac-
ceptance probabilities. The local diﬀusivity in tempera-
ture space calculated from the measured diﬀusive current
is plotted in Fig. 8. There is a pronounced dip in the dif-
fusivity around T ≈0.5 that we can identify as the tem-
perature region where the system enters the highly de-
generate ground-state manifold, e.g., by calculating the
energy of the system, as plotted in Fig. 9.
Again we
ﬁnd that the diﬀusivity points to a strong bottleneck of
the simulation at the critical point which for the fully
frustrated Ising model is at the transition to the zero-
temperature ground-state manifold. The general shape
of the diﬀusivity in the vicinity of this bottleneck re-
mains unchanged with respect to the feedback. By apply-
ing the feedback method, additional temperature points
are shifted towards this bottleneck which is illustrated
in Fig. 10 for the geometric progression (full symbols) as
well as the “ﬂat” temperature set (open symbols). For
moderately large system sizes, we again ﬁnd rapid con-
vergence of the generated temperature sets within 3 – 4
feedback steps and a total of Nsw ≈7.5·106 swap moves.
For the optimized temperature set, the diﬀusive current
is again characterized by a fraction of replicas drifting

FIG. 9: (Color online) Energy per spin e(T) = (1/N)[⟨H⟩]av
as a function of temperature T for the fully-frustrated Ising
model for several system sizes. The data show that already
for T ≲0.5 the energy is independent of temperature, thus
signaling that the system has reached the ground state. The
inset zooms into the temperature range around T = 0.

from the lowest to the highest temperature that linearly
decreases with the temperature index, see Fig. 7 (trian-
gles).
The acceptance probabilities A(T ) for replica swap
moves are shown in Fig. 11 for simulations with a ge-
ometric progression and the optimized temperature set.
While the acceptance probabilities peak at unity close

## Page 8

FIG. 10:
(Color online) Temperature sets for the fully-
frustrated Ising model for diﬀerent feedback steps. Starting
from a temperature set where the acceptance probabilities
are independent of temperature with M = 21 temperature
points (open symbols) and a temperature set obtained by a
geometric progression also with M = 21 temperature points
(ﬁlled symbols), we apply repeated feedback steps until the
temperature sets converge to the optimal distributions. Also
shown are data for an initial temperature set with M = 21
equidistant temperature points (stars). Independent of the
initial temperature set, an optimal temperature distribution
is found after 3 – 4 iterations and ∼7.5 · 106 swaps. After
the successful feedback, temperature points accumulate near
the transition to the ground state slightly above zero temper-
ature.

FIG. 11: (Color online) Acceptance probabilities A(T) for
replica swap moves as a function of temperature T for the
fully-frustrated Ising model. While the acceptance probabili-
ties for a geometric progression temperature set show a pro-
nounced dip close to T = 0, the optimized ensemble shows a
peak close to zero temperature where the system enters the
ground-state manifold. The inset shows, for a ﬁxed number
of temperatures, the acceptance rates as a function of tem-
perature for diﬀerent system sizes L. As for the Ising model,
the “mean” value away from the bottlenecks can be tuned by
increasing the number of temperatures. This illustrates that
in order to obtain higher acceptance rates away from the bot-
tlenecks of the simulation, the number of temperatures have
to be increased with increasing L.

round-trip times scale ∼a + bxc.
Finally, we discuss the eﬀects of varying the number of
temperatures M in the temperature set. Figure 13 shows
the average round-trip times for the fully frustrated Ising
model (L = 20) as a function of the number of tempera-
tures M. For M ≳12, the average round-trip times show
only moderate variations with the number of temperature
points M, whereas for a smaller number of temperatures
the average round-trip times increase drastically. This
can be understood by keeping in mind that a parallel
tempering swap will only be accepted with a high prob-
ability if the energy distributions between neighboring
temperatures overlap.
If the minimum and maximum
temperatures are ﬁxed and M is reduced, the energy dis-
tributions will cease to overlap, which accounts for the
increased average round-trip times. Factoring in the total
CPU time, which we deﬁne as the product of the aver-
age round-trip time with the number of temperatures,
the minimum is more pronounced (inset to Fig. 13) and
clearly illustrates that while a larger number of temper-
atures has little eﬀect on the round-trip times, the total
CPU time increases drastically with increasing M.
Because the data for the average round-trip times vs
M have an optimal value, it is conceivable to develop a
feedback optimization method that optimizes both the

to zero and dramatically drop in the geometric progres-
sion temperature set, in the optimized set most tem-
peratures are reshuﬄed to the low-temperature region
slightly above zero temperature where the system enters
the highly degenerate ground-state manifold. The inset
to Fig. 11 shows the acceptance probabilities as a func-
tion of temperature for a ﬁxed number of temperatures,
as well as Tmin = 0.1 and Tmax = 10.0 ﬁxed. As in the
case for the ferromagnet, the “mean” acceptance prob-
ability away from the ground state bottleneck seems al-
most independent of temperature and settles at a value
that is determined by the number of temperatures used
for a given system size L.
In order to test the eﬃciency of the feedback method
on the FFIM, in Fig. 12 we show the ratio between the
mean round-trip times

τ rt before optimization divided by
the mean round-trip times

τ opt
rt
after optimization in or-
der to illustrate the speedup in replica diﬀusion attained
by the feedback procedure. The data show clearly for all
system sizes that the round-trip times after the optimiza-
tion of the temperature set do not increase as fast as for
a geometric progression or “ﬂat” temperature set. For
these temperature sets where the number of temperature
points increases with system size we ﬁnd that the average

## Page 9

FIG. 12: (Color online) Average round-trip times

τ rt before
the optimization divided by the average round-trip times after
the feedback optimization (

τ opt
rt ) as a function of system size
for the fully-frustrated Ising model. The data for the ﬁlled
squares are for a system starting from a geometric progres-
sion temperature set and represent the speedup obtained by
the feedback method. In addition, we show data for a tem-
perature set with “ﬂat” temperature-independent acceptance
rates (open squares). The dashed lines are guides to the eye.

FIG. 13: (Color online) Average round-trip times

τ rt as a
function of the number of temperatures M for the fully-
frustrated Ising model with L = 20 after the feedback op-
timization. The data show that the round-trip times only de-
pend moderately on the number of temperatures M, provided
that there is suﬃcient overlap of the energy distributions. For
a small number of replicas, this is no longer the case and the
round-trip times increase drastically, e.g., for M ≲12 in this
plot. The inset shows the CPU time which is the product of
the average round-trip time with the number of temperatures
M. The data show a more pronounced minimum.

position of the temperatures and the number of temper-
atures M. Furthermore, in addition to optimizing the
number and locations of the temperature points, we have
also explored varying the ratio of the number of sweep
moves attempted to the number of replica-swap moves
attempted, since this is yet another parameter one must
set in a parallel tempering simulation. This ratio can be
adjusted globally (the same ratio at all temperatures) or
locally (the ratio optimized independently at each tem-
perature).
This will be discussed in more detail in a
subsequent communication.

C.
Spin glasses

Since the optimization of temperature sets improves
the sampling for the two paradigmatic spin models dis-
cussed above, it is a natural step to ask how this feed-
back optimization technique can be applied to improve
state-of-the-art parallel tempering simulations of Ising
spin glass models, such as the three-dimensional (3D)
Edwards-Anderson Ising spin glass [21, 26]:

HSG = −
X

⟨i,j⟩
JijSiSj.
(15)

Here the spins lie on the vertices of a cubic lattice with
periodic boundary conditions. The bonds Jij are chosen
according to a Gaussian distribution with zero mean and
standard deviation unity. The system undergoes a spin-
glass transition at Tc = 0.951(9) [27, 28, 29].
For the spin glass there is the additional complexity
that diﬀerent disorder realizations can lead to strong
sample-to-sample variations.
Thus one could also sur-
mise that strong sample-to-sample variations exist for
the time it takes to equilibrate individual samples. This
becomes evident when measuring the round-trip times
for replicas in a standard parallel tempering simulation
with a ﬁxed temperature set, as illustrated in Fig. 14 for
the Edwards-Anderson Ising spin glass. We ﬁnd that the
measured round-trip times follow a fat-tailed Fr´echet dis-
tribution [30, 31] (solid line, ﬁt performed with R [32]).
The integrated generalized extreme value distribution is
given by:

"

1/ξ#

−

1 + ξ τ −µ

Hξ;µ;β(τ) = exp

.
(16)

β

Here µ represents a generalized most probable value (lo-
cation parameter) and β a standard deviation (scale pa-
rameter). The value of the shape parameter ξ determines
whether the distribution is thin-tailed (ξ < 0, Weibull),
Gumbel (ξ = 0), or fat-tailed (ξ > 0, Fr´echet) [30]. Note
that when ξ > 0, the m-th moment of the Fr´echet dis-
tribution exists only if |ξ| < 1/m, e.g., if ξ > 1/2 the
variance of the distribution is not properly deﬁned. Our
results are in agreement to similar observations for broad-
histogram simulations [2, 33, 34]. Note that the distri-

## Page 10

of the distribution. To do so, we apply the feedback op-
timization outlined above in such a way that we generate
a common probability distribution ¯η(T ) for a set of sam-
ples that are each characterized by their own diﬀusivity
Di(T ), steady-state fraction fi(T ) and current ji, which
are related by

ji = Di(T )¯η(T ) dfi

dT ,
(17)

where the index i indicates the samples in the given set.
Rearranging this equation, the local diﬀusivity of an in-
dividual sample can be expressed as

Di(T ) =
ji

¯η(T ) · dfi/dT .
(18)

To ensure equilibration of all samples we want to simulate
each sample for a ﬁxed number of round trips, despite the
strong sample-to-sample variations. In order to minimize
the overall computer time spent to simulate such a set of
samples, we then minimize the sum of round-trip times
P
i τi. This is equivalent to minimizing the sum of the
inverse of all currents, i.e., j−1
i
, since the current ji is in-
versely proportional to the round-trip time τi. Following
a similar line of arguments as for the original tempera-
ture set optimization, we ﬁnd that the optimal common
temperature distribution ¯ηopt(T ) is proportional to the
square root of the sum of inverse local diﬀusivities

FIG. 14: (Color online) Distribution of average round-trip
times for 5000 diﬀerent samples of the 3D Edwards-Anderson
Ising spin glass with Gaussian disorder and ﬁxed system size
L = 4 in the temperature range from Tmin = 0.10 to Tmax =
2.0. The data follow a fat-tailed Fr´echet distribution (solid
line) with a shape parameter ξ = 035(1). The inset shows the
shape parameter ξ as a function of system size L. Already
for L ≳5, the shape parameter becomes ξ ≳1/2, indicating
that the variance of the distribution is no longer properly
deﬁned. The simulations have been performed using a ﬁxed
temperature set with M = 27 temperature points distributed
such that, on average, replica swap moves have a nearly ﬂat
acceptance rate.

s

X

1

¯ηopt(T ) ∝

Di(T ) .
(19)

i

Again we can use a feedback loop to ﬁnd an optimized
common temperature set by feeding back the measured
local diﬀusivities

bution is increasingly more fat-tailed as the system size
increases (see the inset to Fig. 14).
The measurement of the round-trip times thus allows
to classify individual spin-glass samples as “typical” with
round-trip times in the bulk of the distribution or “hard”
with round-trip times in the tail of the distribution. Such
a classiﬁcation can be very useful to shift computational
resources towards the “hard” samples in the course of
a simulation as these samples potentially might require
substantially longer simulation times in order to equi-
librate. Preliminary tests suggest correlations between
round-trip and equilibration times. The observation of
strong sample-to-sample variations in the distribution of
round-trip times also raises the general question, whether
previous spin-glass studies have properly equilibrated the
“hardest” samples in their simulations. It remains to be
veriﬁed whether this introduces a systematic error in the
analysis of spin-glass systems. Speciﬁcally, the ﬁnite-size
scaling should be sensitive to such systematic errors, as
it has been observed that the number of “hard” samples
signiﬁcantly increases with system size, see the inset in
Fig. 14 and Refs. 2, 33, and 34.
On the other hand, we can ask whether we can opti-
mize the simulated temperature set and generate a “com-
mon” temperature set for samples from the various parts

s


τi · dfi


,
(20)

¯η(T )
X

¯ηopt(T ) = C

dT

i

where C is a normalization constant. The common opti-
mized temperature set is then found using a partial inte-
gration as given in Eq. (11).

V.
CONCLUSIONS

We have introduced an approach to systematically op-
timize temperature sets for parallel tempering Monte
Carlo simulations using an adaptive feedback method
that is motivated by a recently developed ensemble op-
timization technique for broad-histogram Monte Carlo
simulations [1].
We have applied the method to two
paradigmatic spin models, the ferromagnetic Ising model
and the fully frustrated Ising model in two dimensions.
For both models we have shown that the feedback tech-
nique improves sampling of the phase space by reducing
the average round-trip time of replicas diﬀusing in tem-
perature space.

## Page 11

Probably our most important result is the insight,
that the common wisdom that temperature sets in par-
allel tempering Monte Carlo should yield temperature-
independent acceptance probabilities for the swap moves
is not necessarily an optimal choice. Our feedback al-
gorithm shifts temperature points in the optimized tem-
perature sets towards the bottlenecks of the simulation,
typically in the vicinity of a phase transition, where equi-
libration is suppressed. In particular, this has the eﬀect
that the acceptance probabilities for replica swap moves
are higher around the bottlenecks and are not tempera-
ture independent for the so-optimized temperature sets.
We also outline an approach to deﬁne “common” tem-
perature sets for systems that require conﬁgurational
averages, such as spin glasses.
In addition, we have
brieﬂy discussed the eﬀects of sample-to-sample ﬂuctu-
ations with respect to equilibration times of individual

spin glass samples, thus pointing towards a potential
source of systematic errors in previous numerical stud-
ies of spin glasses.
Clearly a deeper analysis of feedback-optimized paral-
lel tempering Monte Carlo is needed, in particular in the
context of spin glasses, as well as the questions raised at
the end of Sec. IV B.

Acknowledgments

We thank A. Honecker, S. D. Huber, M. K¨orner,
C. Predescu, K. Tran, D. W¨urtz and A. P. Young for
stimulating discussions. S. T. acknowledges support by
the Swiss National Science Foundation.

[15] D. A. Kofke, Comment on ”the incomplete beta function
law for parallel tempering sampling of classical canonical
systems” [j. chem. phys. 120, 4119 (2004)], J. Chem.
Phys. 121, 1167 (2004).
[16] N. Rathore, M. Chopra, and J. J. de Pablo, Optimal al-
location of replicas in parallel tempering simulations, J.
Chem. Phys. 122, 024111 (2005).
[17] C. Predescu, M. Predescu, and C. Ciobanu, The incom-
plete beta function law for parallel tempering sampling
of classical canonical systems, J. Chem. Phys. 120, 4119
(2004).
[18] C. Predescu, M. Predescu, and C. Ciobanu, On the Ef-
ﬁciency of Exchange in Parallel Tempering Monte Carlo
Simulations, J. Phys. Chem. B 109, 4189 (2005).
[19] A. Kone and D. A. Kofke, Selection of temperature inter-
vals for parallel-tempering simulations, J. Chem. Phys.
122, 206101 (2005).
[20] H. T. Diep, Frustrated Spin Systems (World Scientiﬁc,
Singapore, 2005).
[21] K. Binder and A. P. Young, Spin glasses: Experimental
facts, theoretical concepts and open questions, Rev. Mod.
Phys. 58, 801 (1986).
[22] M. M´ezard, G. Parisi, and M. A. Virasoro, Spin Glass
Theory and Beyond (World Scientiﬁc, Singapore, 1987).
[23] A. P. Young, ed., Spin Glasses and Random Fields
(World Scientiﬁc, Singapore, 1998).
[24] D. J. Wales, Energy Landscapes (Cambridge University
Press, Cambridge, 2003).
[25] Due to the discrete energy space for the fully-frustrated
Ising model the tuning of the temperature points is ex-
tremely diﬃcult. Small changes to one of the temperature
points can change the acceptance probabilities drasti-
cally. Thus the “ﬂat” temperature sets, computed with an
approximate method due to Predescu (private communi-
cation) exhibit acceptance probabilities for swap moves
which are approximatively constant and independent of
temperature within 10 – 20%.
[26] S. F. Edwards and P. W. Anderson, Theory of spin
glasses, J. Phys. F: Met. Phys. 5, 965 (1975).
[27] R. N. Bhatt and A. P. Young, Numerical studies of Ising
spin glasses in two, three and four dimensions, Phys.

[1] S. Trebst, D. A. Huse, and M. Troyer, Optimizing the en-
semble for equilibration in broad-histogram Monte Carlo
simulations, Phys. Rev. E 70, 046701 (2004).
[2] P. Dayal, S. Trebst, S. Wessel, D. W¨urtz, M. Troyer,
S. Sabhapandit, and S. N. Coppersmith, Performance
Limitations of Flat-Histogram Methods, Phys. Rev. Lett.
92, 097201 (2004).
[3] B. A. Berg and T. Neuhaus, Multicanonical algorithms
for ﬁrst order phase transitions, Phys. Lett. B 267, 249
(1991).
[4] B. Berg and T. Neuhaus, Multicanonical ensemble: a new
approach to simulate ﬁrst-order phase transitions, Phys.
Rev. Lett. 68, 9 (1992).
[5] P. M. C. de Oliveira, T. J. P. Penna, and H. J. Herrmann,
Broad Histogram Method, Braz. J. Phys. 26, 677 (1996).
[6] J.-S. Wang and R. H. Swendsen, Transition Matrix
Monte Carlo Method, J. Stat. Phys. 106, 245 (2002).
[7] F. Wang and D. P. Landau, An eﬃcient, multiple-range
random walk algorithm to calculate the density of states,
Phys. Rev. Lett. 86, 2050 (2001).
[8] F. Wang and D. P. Landau, Determining the density of
states for classical statistical models: A random walk al-
gorithm to produce a ﬂat histogram, Phys. Rev. E 64,
056101 (2001).
[9] K. Hukushima and K. Nemoto, Exchange Monte Carlo
method and application to spin glass simulations, J. Phys.
Soc. Jpn. 65, 1604 (1996).
[10] D. J. Earl and M. W. Deem,
Parallel Tempering:
Theory,
Applications,
and New Perspectives
(2005),
(physics/0508111).
[11] R. H. Swendsen and J. Wang, Replica Monte Carlo sim-
ulation of spin-glasses, Phys. Rev. Lett. 57, 2607 (1986).
[12] E. Marinari and G. Parisi, Simulated tempering: A new
Monte Carlo scheme, Europhys. Lett. 19, 451 (1992).
[13] A. P. Lyubartsev, A. A. Martsinovski, S. V. Shevkunov,
and P. N. Vorontsov-Velyaminov, New approach to Monte
Carlo calculation of the free energy: Method of expanded
ensembles, J. Chem. Phys. 96, 1776 (1992).
[14] D. A. Kofke, On the acceptance probability of replica-
exchange monte carlo trials, J. Chem. Phys. 117, 6911
(2004).

## Page 12

Rev. B 37, 5606 (1988).
[28] E. Marinari, G. Parisi, and J. J. Ruiz-Lorenzo, On the
phase structure of the 3d Edwards Anderson spin glass,
Phys. Rev. B 58, 14852 (1998).
[29] H. G. Katzgraber, M. K¨orner, and A. P. Young, Detailed
study of universality in three-dimensional spin glasses
(2006), (cond-mat/0602212).
[30] E. J. Gumbel, Statistics of extremes (Columbia Univer-
sity Press, New York, 1958).
[31] The deviations of the data to the ﬁtting function for large
average round-trip times can be ascribed to the limited

statistics used.
[32] R
Core
Team
(R
Manuals),
URL
http://cran.r-project.org.
[33] S. Alder, S. Trebst, A. K. Hartmann, and M. Troyer, Dy-
namics of the Wang Landau algorithm and complexity of
rare events for the three-dimensional bimodal Ising spin
glass, J. Stat. Mech. P07008 (2004).
[34] M. D. Costa, J. V. Lopes, and J. M. B. Lopes dos San-
tos, Analytical study of tunneling times in ﬂat histogram
Monte Carlo, Europhys. Lett. 72, 802 (2005).
