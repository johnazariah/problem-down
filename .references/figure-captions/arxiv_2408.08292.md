---
source_pdf: ../arxiv_2408.08292.pdf
pages: 80
captions: 20
extracted_at: 2026-04-17T12:32:43+00:00
extractor: PyMuPDF (fitz)
title: "Optimization by Decoded Quantum Interferometry"
author: "Stephen P. Jordan; Noah Shutty; Mary Wootters; Adam Zalcman; Alexander Schmidhuber; Robbie King; Sergei V. Isakov; Tanuj Khattar; Ryan Babbush"
---

# arxiv_2408.08292 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## Figure 1

Page: 3
Caption bbox: (72.0, 320.6, 540.0, 366.7)
Crop bbox: (8.0, 8.0, 604.0, 316.6)
Crop asset: ../figure-crops/arxiv_2408.08292/page_003_figure_01.png

Caption:

Figure 1: A schematic illustration of the steps of the DQI algorithm. Since the initial Dicke state
is of weight ℓ, the final polynomial P is of degree ℓ. Here, for simplicity, we take wℓ= 1 and wk = 0
for all k ̸= ℓ.

## Figure 2

Page: 5
Caption bbox: (72.0, 281.7, 540.0, 321.0)
Crop bbox: (8.0, 8.0, 604.0, 277.7)
Crop asset: ../figure-crops/arxiv_2408.08292/page_005_figure_01.png

Caption:

Figure 2: A stylized example of the Optimal Polynomial Intersection (OPI) problem. For y1 ∈Fp,
the orange set above the point y1 represents Fy1. Both of the polynomials Q1(y) and Q2(y) represent
solutions that have a large objective value, as they each intersect all but one set Fy.

## Figure 3

Page: 8
Caption bbox: (72.0, 297.2, 540.1, 356.8)
Crop bbox: (8.0, 8.0, 604.0, 293.2)
Crop asset: ../figure-crops/arxiv_2408.08292/page_008_figure_01.png

Caption:

Figure 3:
Here we plot the expected fraction ⟨s⟩/p of satisfied constraints achieved by DQI with
the Berlekamp-Massey decoder and by Prange’s algorithm for the OPI problem in the balanced
case r/p = 1/2, as a function of the ratio of variables to constraints n/p. At n/p = 1/10 Prange’s
algorithm satisfies a fraction 0.55 of the clauses whereas DQI satisfies ⟨s⟩/p = 1/2 +
√

## Table 1

Page: 8
Caption bbox: (72.0, 570.4, 540.1, 684.2)
Crop bbox: (8.0, 8.0, 604.0, 566.4)
Crop asset: ../figure-crops/arxiv_2408.08292/page_008_figure_02.png

Caption:

Table 1:
Here, we compare DQI, using a standard belief propagation decoder, against classical
algorithms for a randomly-generated max-XORSAT instance with irregular degree distribution
specified in §12. We consider an example instance with 31, 216 variables and 50, 000 constraints.
The classical algorithms above are defined in §11. For simulated annealing the satisfaction fraction
grows with runtime, so we report two numbers. The first is the optimum reachable by limiting
simulated annealing to the same runtime used by belief propagation to solve the problem to which
the max-XORSAT instance is reduced by DQI (8 seconds × 1 core) and the second is for the
shortest anneal that matched satisfaction fraction achieved by DQI+BP (73 hours × 5 cores).

## Figure 4

Page: 18
Caption bbox: (72.0, 609.5, 540.0, 702.1)
Crop bbox: (64.6, 64.4, 546.9, 605.5)
Crop asset: ../figure-crops/arxiv_2408.08292/page_018_figure_01.png

Caption:

Figure 4: Decoded Quantum Interferometry over F2. The algorithm begins with a computation,
on a classical computer, of the principal eigenvector (w0, . . . , wℓ)T of a certain matrix A(m,ℓ,0).
P(f) is a degree-ℓpolynomial that enhances the probability of sampling x ∈Fn
2 with high value
of the objective f. Index k ranges over {0, . . . , ℓ} and y over the set {y ∈Fm
2 : |y| = k} of m-bit
strings of Hamming weight k. Weight register qubits may be reused for the syndrome register. If
2ℓ+ 1 < d⊥, the postselection succeeds with probability ≥1 −εℓ, where εℓis the decoding failure
rate on random weight-ℓerrors.

## Figure 5

Page: 25
Caption bbox: (72.0, 293.5, 540.1, 345.4)
Crop bbox: (8.0, 8.0, 604.0, 289.5)
Crop asset: ../figure-crops/arxiv_2408.08292/page_025_figure_01.png

Caption:

Figure 5: Here we plot the expected fraction ⟨s⟩/m of satisfied constraints, as dictated by Lemma
9.2, upon measuring |P(f)⟩when P is the optimal degree-ℓpolynomial. We show the balanced case
where |f−1
i
(+1)| ≃p/2 for all i. Accordingly, the dashed black line corresponds to the asymptotic
formula (9) with r/p = 1/2.

## Figure 6

Page: 46
Caption bbox: (72.0, 279.7, 540.1, 358.7)
Crop bbox: (54.0, 76.0, 548.0, 261.8)
Crop asset: ../figure-crops/arxiv_2408.08292/page_046_figure_01.png

Caption:

Figure 6: The approximation achieved by simulated annealing (left) and greedy optimization
(right) in our computer experiments at n = 105, on a log-log scale, where each constraint contains
k variables and each variable is contained in D constraints. The lines illustrates linear least-squares
curve fits to the log-log data. The ensemble of max-k-XORSAT instances is formally defined in
Appendix B. In these anneals we use 5, 000 sweeps with single-bit updates, and linearly increasing
inverse temperature β.

## Figure 7

Page: 47
Caption bbox: (72.0, 574.6, 540.1, 680.7)
Crop bbox: (8.0, 8.0, 604.0, 570.6)
Crop asset: ../figure-crops/arxiv_2408.08292/page_047_figure_01.png

Caption:

Figure 7: Here we show the dependence of the fraction of constraints satisfied ϕ on the number of
Metropolis updates N used in simulated annealing. That is, N is the number of variables times the
number of sweeps. We find that the functional form ϕ = a + b√c log N suggested by the heuristic
argument of §11.1 fits poorly, but the form ϕ = a −bN−c fits reasonably well. On the top panel
we consider an instance from Gallager’s ensemble with k = 30, D = 60, and n = 15, 000. On
the bottom we use the irregular instance defined in §12, which has n = 31, 216. Each data point
represents the final outcome of an independent anneal, and in each anneal we vary β linearly from
zero to five.

## Figure 8

Page: 48
Caption bbox: (72.0, 302.3, 540.1, 354.2)
Crop bbox: (8.0, 8.0, 604.0, 298.3)
Crop asset: ../figure-crops/arxiv_2408.08292/page_048_figure_01.png

Caption:

Figure 8: Here we show the satisfaction fraction achieved by simulated annealing as a function of
the number of sweeps. For each number of sweeps we run five independent executions of simulated
annealing with different pseudorandom seeds. At the right-hand side of the plot we incremented
the number of sweeps by larger increments due to computational cost.

## Figure 9

Page: 50
Caption bbox: (72.0, 440.8, 540.1, 533.3)
Crop bbox: (70.0, 208.5, 554.0, 433.8)
Crop asset: ../figure-crops/arxiv_2408.08292/page_050_figure_01.png

Caption:

Figure 9:
On Gallager’s ensemble we compare the fraction ϕ of constraints satisfied in the
solutions found by DQI+BP, AdvRand, and simulated annealing. We also show the approximate
performance of p = 14 QAOA on large girth D-regular max-3-XORSAT instances, which was
calculated in [7], up to O(1/D) corrections. We fix k, the number of variables in each constraint, at
3 and we vary D, the number of constraints that each variable is contained in, from 4 to 687. The
red, blue, and green lines display the linear least-square fits to the log-log plot of ϕ −1/2 versus D.
We keep the number of variables fixed at n = 20, 000, thus m = Dn/3.

## Figure 10

Page: 54
Caption bbox: (72.0, 218.6, 540.1, 338.3)
Crop bbox: (69.2, 64.0, 542.9, 214.6)
Crop asset: ../figure-crops/arxiv_2408.08292/page_054_figure_01.png

Caption:

Figure 10: The attack of Bleichenbacher and Nguyen [25] is workable when the shortest nonzero
vector in a particular lattice has weight √m. Above, left, we apply the BKZ algorithm [72] to
find the shortest nonzero vector (under the 2-norm) in the lattices arising from random problem
instances for various m and ndistractors. We observe that the shortest vector almost always has 2-
norm < √m in the regime where m and ndistractors are both a significant fraction of p. Consequently,
the success probability of the attack when applied to our OPI problem in the regime where m =
p −1, n = m/2, ndistractors = (p −3)/2 appears to exhibit exponential decay with p whether LLL,
BKZ with a block size of 15 (“BKZ-15”) or BKZ with unlimited block size. In this regime we
believe the lattice-based heuristic of [25] does not succeed.

## Figure 11

Page: 55
Caption bbox: (72.0, 298.7, 540.1, 323.5)
Crop bbox: (8.0, 8.0, 604.0, 294.7)
Crop asset: ../figure-crops/arxiv_2408.08292/page_055_figure_01.png

Caption:

Figure 11: Tanner graph for a sparse irregular LDPC code illustrating the notation introduced
in §12.

## Figure 12

Page: 56
Caption bbox: (72.0, 211.0, 540.1, 249.6)
Crop bbox: (8.0, 8.0, 604.0, 207.0)
Crop asset: ../figure-crops/arxiv_2408.08292/page_056_figure_01.png

Caption:

Figure 12: Degree distribution for an irregular instance sampled with m = 50, 000 and n = 31, 216.
The full table of variable and constraint degrees is available in our Zenodo record https://doi.
org/10.5281/zenodo.13327870.

## Figure 13

Page: 58
Caption bbox: (72.0, 508.1, 540.1, 604.3)
Crop bbox: (8.0, 8.0, 604.0, 504.1)
Crop asset: ../figure-crops/arxiv_2408.08292/page_058_figure_01.png

Caption:

Figure 13:
Here we consider degree-D max-k-XORSAT instances Bx max
=
v where v is uni-
formly random and B is drawn from the (k, D)-regular Gallager ensemble. In the orange region it
is information-theoretically impossible for DQI with classical decoding to outperform simulated
annealing on average-case instances from Gallager’s ensemble.
In the blue region, DQI with
maximum-likelihood (i.e.
Shannon-limit) decoding achieves a higher satisfaction fraction than
simulated annealing, but realizing this advantage with polynomial-time decoders remains an open
problem. Prange’s algorithm does not win on any region of this plot.

## Figure 14

Page: 66
Caption bbox: (72.0, 190.1, 540.1, 269.1)
Crop bbox: (8.0, 8.0, 604.0, 186.1)
Crop asset: ../figure-crops/arxiv_2408.08292/page_066_figure_01.png

Caption:

Figure 14: Quantum circuit implementing Gi gate using oracle access. The circuit takes as input
a single subregister of the error register and employs an auxiliary qubit initialized in |0⟩. It begins
by swapping the qubit corresponding to 1 in the input with the auxiliary qubit. Then it applies
the Quantum Fourier Transform (QFT) F over Fr
q, followed by a call to the oracle Ui, followed by
another QFT. The QFT gates are conditional on the auxiliary qubit. The circuit ends with the
uncomputation of the auxiliary qubit by flipping it when the subregister is non-zero.

## Table 2

Page: 69
Caption bbox: (85.5, 257.6, 526.5, 269.8)
Crop bbox: (66.9, 64.2, 577.0, 253.6)
Crop asset: ../figure-crops/arxiv_2408.08292/page_069_figure_01.png

Caption:

Table 2: Quantum circuit costs for modular arithmetic operations on n-bit operands in Fp.

## Table 3

Page: 69
Caption bbox: (72.0, 470.6, 540.0, 536.0)
Crop bbox: (64.0, 64.2, 577.0, 466.6)
Crop asset: ../figure-crops/arxiv_2408.08292/page_069_figure_02.png

Caption:

Table 3: Cost of finding shortest linear feedback shift register (LFSR) using Algorithm 2, imple-
mented and analyzed using Qualtran [34]. This is the most expensive step of Berlekamp-Massey
syndrome decoding algorithm [23] for Reed Solomon codes, as presented in Algorithm 1. Here
n = N −K is the number of syndromes, which is equal to the length of the input sequence to
Berlekamp-Massey algorithm, and ℓ= n

## Algorithm 1

Page: 70
Caption bbox: (72.0, 415.4, 486.7, 427.5)
Crop bbox: (73.3, 102.3, 342.0, 411.4)
Crop asset: ../figure-crops/arxiv_2408.08292/page_070_figure_01.png

Caption:

Algorithm 1 Syndrome decoding of RSq(⃗γ, N, K) using Berlekamp Massey algorithm

## Algorithm 2

Page: 71
Caption bbox: (72.0, 169.3, 483.4, 181.5)
Crop bbox: (0.0, 8.0, 612.0, 165.3)
Crop asset: ../figure-crops/arxiv_2408.08292/page_071_figure_01.png

Caption:

Algorithm 2 Reversible Berlekamp-Massey algorithm to find shortest LFSR over Fq.

## Figure 15

Page: 73
Caption bbox: (72.0, 529.6, 540.1, 595.1)
Crop bbox: (8.0, 8.0, 604.0, 525.6)
Crop asset: ../figure-crops/arxiv_2408.08292/page_073_figure_01.png

Caption:

Figure 15: Here we generate OPI instances over Fp where p takes prime values from 307 to 12, 343.
The number of constraints is m = p −1. For each m we take n ∈{m/2, m/6, m/10}, rounded to
the nearest integer. We find that, independent of n/m, the approximation achieved by simulated
annealing with 10, 000 sweeps fits well to ϕmax = 1/2 + 1.8D−0.45. Note that, in OPI the degree D
equals the number of constraints m, since every variable is contained in every constraint.
