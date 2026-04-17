---
source_pdf: ../arxiv_1401.2910.pdf
pages: 15
captions: 12
extracted_at: 2026-04-17T12:32:29+00:00
extractor: PyMuPDF (fitz)
---

# arxiv_1401.2910 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## FIG. 1.

Page: 3
Caption bbox: (317.0, 422.0, 562.1, 546.0)
Crop bbox: (317.0, 44.1, 562.1, 416.6)
Crop asset: ../figure-crops/arxiv_1401.2910/page_003_figure_01.png

Caption:

FIG. 1. Scaling of the typical time to ﬁnd a solution
at constant annealing time.
Shown is the typical (me-
dian) time to ﬁnd a ground state with 99% probability for
spin glasses with ±1 couplings and no local ﬁeld. A) for SA,
B) for SQA. The envelope of the curves at constant ta, shown
in red, corresponds to the minimal time at a given problem
size N and is relevant for discussion of the asymptotic scal-
ing. Annealing times are given in units of Monte Carlo steps
(MCS). One MCS corresponds to one update per spin. Note
in particular that the slope for small N is much ﬂatter at
large annealing time (e.g., MCS = 4000) than that of the
true scaling.

## FIG. 2.

Page: 4
Caption bbox: (54.0, 243.7, 299.1, 367.8)
Crop bbox: (54.0, 44.1, 299.1, 238.3)
Crop asset: ../figure-crops/arxiv_1401.2910/page_004_figure_01.png

Caption:

FIG. 2. Pitfalls when detecting speedup. Shown is the
speedup of SQA over SA, deﬁned as the ratio of median time
to ﬁnd a solution with 99% probability between SA and SQA.
Two cases are presented: a) both SA and SQA run optimally
(i.e., the ratio of the true scaling curves shown in Figure 1),
and there is no asymptotic speedup (solid line). b) SQA is run
suboptimally at small sizes by choosing a ﬁxed large annealing
time ta = 10000 MCS (dashed line). The apparent speedup
is, however, due to suboptimal performance on small sizes
and not indicative of the true asymptotic behavior given by
the solid line, which displays a slowdown of SQA compared
to SA.

## FIG. 3.

Page: 6
Caption bbox: (54.0, 506.6, 562.2, 588.8)
Crop bbox: (77.9, 44.1, 535.1, 501.2)
Crop asset: ../figure-crops/arxiv_1401.2910/page_006_figure_01.png

Caption:

FIG. 3. Scaling of time to solution for the ranges r = 1 (panels A, C and E) and r = 7 (panels B, D and F). Shown
is the scaling of the time to ﬁnd the ground state at least once with a probability p = 0.99 for various quantiles of hardness,
for A,B) simulated annealing (SA), C,D) simulated quantum annealing (SQA) and E,F) the DW2. The SA and SQA data is
obtained by running the simulations at an optimized annealing time for each problem size. The DW2 annealing time of 20µs is
the shortest possible. Note the diﬀerent vertical axis scales, and that both the DW2 and SQA have trouble solving the hardest
instances for the large problem sizes, as indicated by the terminating lines for the highest quantiles. More than the maximum
number of of repetitions (10000 for SQA, at least 32000 for DW2) of the annealing we performed would be needed to ﬁnd the
ground state in those cases.

## FIG. 4.

Page: 7
Caption bbox: (54.0, 377.4, 299.1, 449.2)
Crop bbox: (54.0, 44.1, 299.1, 372.0)
Crop asset: ../figure-crops/arxiv_1401.2910/page_007_figure_01.png

Caption:

FIG. 4. Speedup for ratio of quantiles for the DW2
compared to SA. A) For instances with range r = 1. B)
For instances with range r = 7. Shown are curves from the
median (50th quantile) to the 99th quantile. 16 gauges were
used.
In these plots we multiplied Eq. (6) by 512 so that
the speedup value at N = 512 directly compares one DW2
processor against one classical CPU.

## FIG. 5.

Page: 7
Caption bbox: (317.0, 377.4, 562.1, 480.5)
Crop bbox: (317.0, 44.1, 562.1, 372.0)
Crop asset: ../figure-crops/arxiv_1401.2910/page_007_figure_02.png

Caption:

FIG. 5. Comparing wall-clock times A comparison of the
wall-clock time to ﬁnd the solution with probability p = 0.99
for SA running on a single CPU (dashed lines) compared to
the DW2 (solid lines) using 16 gauges. A) for range r = 1,
B) for range r = 7. Shown are curves from the median (50th
quantile) to the 99th quantile. The large constant program-
ming overhead of the DW2 masks the exponential increase of
time to solution that is obvious in the plots of pure annealing
time. Results for a single gauge are shown in the Supplemen-
tary Material.

## FIG. 6.

Page: 8
Caption bbox: (54.0, 372.7, 562.2, 444.4)
Crop bbox: (57.2, 44.1, 555.9, 367.2)
Crop asset: ../figure-crops/arxiv_1401.2910/page_008_figure_01.png

Caption:

FIG. 6. Instance-by-instance comparison of annealing times and wall-clock times. Shown is a scatter plot of the
pure annealing time for the DW2 compared to a simulated classical annealer (SA) using an average over 16 gauges on the DW2.
A) DW2 compared to SA for r = 1, B) DW2 compared to SA for r = 7. The color scale indicates the number of instances
in each square. Instances below the diagonal red line are faster on the DW2, those above are faster classically. Instances for
which the DW2 did not ﬁnd the solution with 10000 repetitions per gauge are shown at the top of the frame (no such instances
were found for SA). Panels C) and D) show wall-clock times using a single gauge on the DW2. Panels E) and F) show the
wall-clock time for DW2 using 16 gauges. N = 503 in all cases.

## FIG. 7.

Page: 9
Caption bbox: (54.0, 366.5, 299.1, 448.7)
Crop bbox: (54.0, 44.1, 299.1, 361.0)
Crop asset: ../figure-crops/arxiv_1401.2910/page_009_figure_01.png

Caption:

FIG. 7. Speedup for quantiles of the ratio of the DW2
compared to SA, for A) r = 1, B) r = 7.
No asymptotic
speedup is visible for any of the quantiles at r = 7, while some
evidence of a limited quantum speedup (relative to SA) is seen
for quantiles higher than the median at r = 1. As in Figure 4
we multiplied Eq. (7) by 512 so that the speedup value at
N = 512 directly compares one DW2 processor against one
classical CPU.

## FIG. 8.

Page: 11
Caption bbox: (317.0, 412.6, 562.2, 505.2)
Crop bbox: (171.7, 43.1, 557.3, 406.8)
Crop asset: ../figure-crops/arxiv_1401.2910/page_011_figure_01.png

Caption:

FIG. 8. Qubits and couplers in the D-Wave Two de-
vice. The DW2 “Vesuvius” chip consists of an 8 × 8 two-
dimensional square lattice of eight-qubit unit cells, with open
boundary conditions. The qubits are each denoted by circles,
connected by programmable inductive couplers as shown by
the lines between the qubits. Of the 512 qubits of the de-
vice located at the University of Southern California used in
this work, the 503 qubits marked in green and the couplers
connecting them are functional.

## FIG. 9.

Page: 12
Caption bbox: (54.0, 377.4, 299.1, 438.7)
Crop bbox: (54.0, 44.1, 299.1, 372.0)
Crop asset: ../figure-crops/arxiv_1401.2910/page_012_figure_01.png

Caption:

FIG. 9. Annealing schedules. A) The amplitude of the
median transverse ﬁeld A(t) (decreasing, blue) and the longi-
tudinal couplings B(t) (increasing, red) as a function of time.
The device temperature of T = 18mK is indicated by the
black horizontal dashed line. B) The linear annealing sched-
ule used in simulated quantum annealing.

## TABLE I.

Page: 12
Caption bbox: (317.0, 268.1, 562.1, 308.5)
Crop bbox: (317.0, 8.0, 562.2, 264.1)
Crop asset: ../figure-crops/arxiv_1401.2910/page_012_figure_02.png

Caption:

TABLE I. Wallclock times on the DW2. Listed are mea-
sured programming times tp and annealing plus readout times
tr (for a pure annealing time of 20µs) on the DW2 for various
problem sizes.

## TABLE II.

Page: 12
Caption bbox: (317.0, 358.8, 562.1, 399.2)
Crop bbox: (335.2, 44.3, 543.9, 354.8)
Crop asset: ../figure-crops/arxiv_1401.2910/page_012_figure_03.png

Caption:

TABLE II. Repetitions of annealing runs used on the
DW2. This table summarizes the total number of repetitions
used to estimate the success probabilities on the DW2 for
various system sizes.

## FIG. 10.

Page: 13
Caption bbox: (54.0, 358.5, 562.1, 409.3)
Crop bbox: (8.0, 8.0, 604.0, 354.5)
Crop asset: ../figure-crops/arxiv_1401.2910/page_013_figure_01.png

Caption:

FIG. 10. Optimal annealing times for the simulated annealer and for the D-Wave device. Shown is the total
eﬀort R(ta)ta as a function of annealing time ta for various quantiles of problems with r = 1 and r = 7 (see Supplementary
Information for r = 3). A) and B) SA, where the minimum of the total eﬀort determines the optimal annealing time topt
a . C)
and D) DW2, where we ﬁnd a monotonically increasing total eﬀort, meaning that the optimal time topt
a
is always shorter than
the minimal annealing time of 20µs.
