---
source_pdf: ../arxiv_2602.11457.pdf
pages: 22
captions: 15
extracted_at: 2026-04-17T12:32:45+00:00
extractor: PyMuPDF (fitz)
title: "The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical qubits using quantum LDPC codes"
author: "Paul Webster; Lucas Berent; Omprakash Chandra; Evan T. Hockings; Nouédyn Baspin; Felix Thomsen; Samuel C. Smith; Lawrence Z. Cohen"
---

# arxiv_2602.11457 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## Figure 1

Page: 2
Caption bbox: (64.8, 399.7, 297.0, 479.7)
Crop asset: none

Caption:

Figure 1 shows how the Pinnacle Architecture is assem-
bled from these modules.
Compilation is performed via Pauli-based computa-
tion [13]. This allows for universal fault-tolerant quantum
computing on arbitrarily many logical qubits with a time
cost that scales with the T count.
Features of the Pinnacle Architecture include:

## FIG. 1.

Page: 3
Caption bbox: (64.8, 380.7, 547.2, 431.5)
Crop bbox: (59.0, 56.8, 557.4, 351.7)
Crop asset: ../figure-crops/arxiv_2602.11457/page_003_figure_01.png

Caption:

FIG. 1. Examples of the Pinnacle Architecture. These two examples represent specific examples of different space-time trade-offs and
code block choices, optimised for RSA-2048 factoring in different hardware regimes. Example (a) allows factoring in one month with
a physical error rate of p = 10−3 and a code cycle time of tc = 1 µs. Example (b) allows factoring in three months with a physical
error rate of p = 10−4 and a code cycle time of tc = 1 ms. Shorter runtimes can be achieved by adding more processing units,
increasing paralellisation at the cost of additional physical qubits.

## FIG. 2.

Page: 3
Caption bbox: (64.8, 660.5, 297.0, 711.3)
Crop bbox: (56.8, 56.8, 557.4, 655.3)
Crop asset: ../figure-crops/arxiv_2602.11457/page_003_figure_02.png

Caption:

FIG. 2. Physical qubits required for determining the ground
state energy of the Fermi-Hubbard model on an L × L lattice
to 0.5% relative precision. Surface code values correspond to the
minimum quoted number of physical qubits with u/τ = 4 in
Ref. [12].

## FIG. 3.

Page: 4
Caption bbox: (64.8, 692.6, 547.2, 722.4)
Crop bbox: (80.9, 57.7, 531.1, 677.0)
Crop asset: ../figure-crops/arxiv_2602.11457/page_004_figure_01.png

Caption:

FIG. 3. Optimal expected runtime for factoring an RSA-2048 integer on the Pinnacle Architecture as a function of the number of
physical qubits and the code cycle time at physical error rates of (a) p = 10−3 and (b) p = 10−4. White areas indicate insufficient
physical qubits to implement the algorithm. The reaction time in all cases is assumed to be equal to ten times the code cycle time.

## FIG. 4.

Page: 6
Caption bbox: (315.0, 251.5, 547.2, 312.8)
Crop bbox: (315.0, 58.9, 547.2, 247.5)
Crop asset: ../figure-crops/arxiv_2602.11457/page_006_figure_01.png

Caption:

FIG. 4. Structure and operation of a magic engine. Magic state
distillation is applied on one logical sector of a QLDPC code
block using noisy |T⟩states injected from ancillary systems. In
parallel, an arbitrary Pauli measurement on the processing unit
joint with ¯Z1 on the other logical sector injects an encoded | ¯T⟩
state that was distilled in the previous logical cycle.

## FIG. 5.

Page: 8
Caption bbox: (315.0, 703.2, 547.2, 722.7)
Crop bbox: (0.0, 8.0, 612.0, 699.2)
Crop asset: ../figure-crops/arxiv_2602.11457/page_008_figure_01.png

Caption:

FIG. 5. Process of joining and separating processing units with
Clifford frame cleaning to allow for flexible parallelism.

## TABLE I.

Page: 11
Caption bbox: (64.8, 74.3, 547.2, 114.7)
Crop bbox: (8.0, 8.0, 604.0, 70.3)
Crop asset: ../figure-crops/arxiv_2602.11457/page_011_figure_01.png

Caption:

TABLE I. Instances of the family of generalised bicycle codes. For each code, the parameters Jn, k, dK are provided, along with the
number of code cycles per logical cycle, dt = d+2. The codes are defined by l, A, and B, alongside Eq. (1) and Eq. (2). The remaining
columns show the number of physical qubits in their code blocks, gadgets, bridges and processing blocks. See Ref. [11] for more
details.

## FIG. 6.

Page: 12
Caption bbox: (315.0, 271.6, 547.2, 437.5)
Crop bbox: (315.0, 56.8, 547.2, 266.3)
Crop asset: ../figure-crops/arxiv_2602.11457/page_012_figure_01.png

Caption:

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

## TABLE II.

Page: 13
Caption bbox: (64.8, 74.3, 297.0, 104.2)
Crop bbox: (64.8, 8.0, 334.5, 70.3)
Crop asset: ../figure-crops/arxiv_2602.11457/page_013_figure_01.png

Caption:

TABLE II. Fitted parameters with 95% confidence intervals for
the ansatz in Eq. 5 for memory experiments and logical measure-
ment experiments.

## TABLE III.

Page: 13
Caption bbox: (64.8, 169.3, 297.0, 230.6)
Crop bbox: (84.7, 99.7, 277.1, 156.1)
Crop asset: ../figure-crops/arxiv_2602.11457/page_013_figure_02.png

Caption:

TABLE III. Error rates per logical qubit and logical cycle for log-
ical measurement in GB codes of each distance at physical error
rates of p = 10−3 and p = 10−4. Values correspond to the
central estimates of the fit parameters from the Logical Mea-
surement row of Table II substituted into the ansatz presented
in Eq. (6).

## Table IV

Page: 14
Caption bbox: (64.8, 650.5, 297.0, 729.2)
Crop bbox: (110.7, 79.1, 217.8, 635.1)
Crop asset: ../figure-crops/arxiv_2602.11457/page_014_figure_01.png

Caption:

Table IV shows the number of physical qubits required
for even L ≤32, along with the runtimes with code cycle
times of 1 µs and 1 ms. Figure 2 shows that the number of
physical qubits required is an order of magnitude smaller
than those required using surface codes in Ref. [12].
A full determination of the ground state energy re-
quires multiple shots of the algorithm, with the number

## TABLE IV.

Page: 14
Caption bbox: (315.0, 73.9, 547.2, 145.8)
Crop asset: none

Caption:

TABLE IV. Physical qubits and runtime required to perform one
shot of Fermi-Hubbard ground state energy estimation on an
L × L lattice with a relative error of ≤0.5% of the total lattice
energy. The runtime is approximately independent of L because
the relative error allows for fewer Trotter steps for larger lattices;
runtimes for each value of L are equal to or slightly smaller than
those given. kq represents kiloqubits (×103 qubits).

## FIG. 7.

Page: 15
Caption bbox: (315.0, 263.8, 547.2, 314.6)
Crop bbox: (315.0, 56.8, 547.2, 258.6)
Crop asset: ../figure-crops/arxiv_2602.11457/page_015_figure_01.png

Caption:

FIG. 7. Comparison of space, time and spacetime cost for our
parallelised algorithm to Gidney’s algorithm or Ref. [8]. For the
purpose of this plot, all algorithmic parameters (other than ρ)
are chosen to match those of the n = 2048 row of Table 5 of
Ref. [8].

## TABLE V.

Page: 17
Caption bbox: (64.8, 73.9, 547.2, 145.6)
Crop bbox: (8.0, 8.0, 604.0, 69.9)
Crop asset: ../figure-crops/arxiv_2602.11457/page_017_figure_01.png

Caption:

TABLE V. Time cost accounting for all subroutines required for each prime. Loop numbers refer to Gidney’s algorithm, as presented
in Ref. [8]. For lookups and phaseups, the size is the address size; for additions, it is the size of the registers being added. For addition
(loop 2) the size is the average over the loop, since it varies. The T Count column is the number of T gates required, which is four
times the Toffoli count. The Logical Cycles column is the total number of logical cycles, including both T state injections and other
logical measurements. Since each Toffoli gate requires four T gates and one logical measurement [56], and one additional logical
measurement is required for measurement-based uncompute, this is nearly always 3/2 times the T count. The only exception is
Lookup (Loop 1) which also requires additional logical measurements for Clifford frame cleaning.

## TABLE VI.

Page: 17
Caption bbox: (315.0, 291.3, 547.2, 331.9)
Crop bbox: (315.0, 141.1, 547.2, 270.2)
Crop asset: ../figure-crops/arxiv_2602.11457/page_017_figure_02.png

Caption:

TABLE VI. Minimum number of physical qubits required to com-
plete factoring in a range of expected runtimes for a range of
hardware parameters. Mq and kq represent megaqubits (i.e.,
×106 qubits) and kiloqubits (×103 qubits) respectively.
