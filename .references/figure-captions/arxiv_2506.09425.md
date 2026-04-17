---
source_pdf: ../arxiv_2506.09425.pdf
pages: 13
captions: 8
extracted_at: 2026-04-17T12:32:44+00:00
extractor: PyMuPDF (fitz)
title: "Local surrogates for quantum machine learning"
author: "Sreeraj Rajindran Nair; Christopher Ferrie"
---

# arxiv_2506.09425 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## FIG. 1

Page: 1
Caption bbox: (317.3, 408.0, 561.8, 463.8)
Crop bbox: (0.0, 252.1, 612.0, 404.0)
Crop asset: ../figure-crops/arxiv_2506.09425/page_001_figure_01.png

Caption:

FIG. 1: Local surrogation. For a small enough local
region within the data space of a quantum learning
model, a cost-efficient local quantum/classical surrogate
can be generated with adequate accuracy, potentially as
a two-step protocol.

## FIG. 2

Page: 5
Caption bbox: (58.5, 178.0, 294.6, 240.9)
Crop bbox: (54.0, 44.1, 299.1, 174.0)
Crop asset: ../figure-crops/arxiv_2506.09425/page_005_figure_01.png

Caption:

FIG. 2: Testing 1D signal fitting in terms of
improvement in R2 learning metric in the case of 1, 2,
and 3 qubit single-layer quantum reuploading models.
The 1D signal under consideration is a truncated
Fourier series of degree 3, i.e., g(x) = P5
n=−5 cne2inx

## FIG. 3

Page: 6
Caption bbox: (54.0, 406.3, 562.1, 439.3)
Crop bbox: (46.0, 44.1, 570.1, 375.4)
Crop asset: ../figure-crops/arxiv_2506.09425/page_006_figure_01.png

Caption:

FIG. 3: Demonstration of local quantum and local classical surrogation. The 22 × 22 training grid for the full target
function on a square domain x, y ∈[−π, π] had a patch of fixed 10 × 10 and 8 × 8 grid size for the local quantum
surrogate and the local classical surrogate, respectively.

## FIG. 4

Page: 7
Caption bbox: (55.0, 339.5, 561.1, 395.3)
Crop bbox: (46.0, 44.1, 570.1, 308.4)
Crop asset: ../figure-crops/arxiv_2506.09425/page_007_figure_01.png

Caption:

FIG. 4: Testing the performance of local quantum/classical surrogates in the case of various 2D target functions.
Tests had a 22 × 22 training grid for the full target function on a square domain x, y ∈[−π, π]. The simulation
looped over different window/patch sizes. The square patch is always anchored at grid index (2, 2) of the 22 × 22
training grid, starting as a 2 × 2 grid and increments in size by 1 grid index in each window cycle until reaching the
final size of 20 × 20.

## FIG. 5

Page: 8
Caption bbox: (54.0, 406.5, 562.1, 454.5)
Crop bbox: (46.0, 44.1, 570.1, 378.9)
Crop asset: ../figure-crops/arxiv_2506.09425/page_008_figure_01.png

Caption:

FIG. 5: Local surrogation protocol on a QSVM trained on a 2-class, 2-feature Iris data set. QSVM had a R2 of 0.84
after its training. PennyLane was used to design the 2-qubit QSVM and the 1-qubit 2-layer reuploading local
quantum surrogate. The local quantum-to-classical surrogate is implemented as per the classical surrogation
protocol, with the local quantum surrogate treated as a white-box model.

## FIG. 6

Page: 9
Caption bbox: (54.6, 424.3, 298.5, 468.7)
Crop bbox: (54.0, 44.1, 299.1, 382.8)
Crop asset: ../figure-crops/arxiv_2506.09425/page_009_figure_01.png

Caption:

FIG. 6: Local-surrogate performance (top) and training
convergence (bottom) trained on the QSVM for varying
patch radii from 0.3 radii to 2.5 radii, all centered at
(0, 0).

## FIG. 7

Page: 10
Caption bbox: (54.0, 189.2, 562.1, 235.7)
Crop bbox: (46.0, 44.1, 570.1, 185.2)
Crop asset: ../figure-crops/arxiv_2506.09425/page_010_figure_01.png

Caption:

FIG. 7: Local surrogation protocol on PCA reduced 6-feature Breast Cancer Wisconsin (Diagnostic) data set
to test the practical limits of classical surrogation protocol. Hypercube patch radii ranged between 0.5 −3.5 with
step size 0.05. PennyLane was used to design the 2-qubit 3-layer reuploading local quantum surrogate. The local
quantum-to-classical surrogate is implemented as per the simplified separable bases Fourier classical surrogate.

## TABLE I

Page: 13
Caption bbox: (188.2, 54.3, 427.9, 64.3)
Crop bbox: (0.0, 8.0, 612.0, 50.3)
Crop asset: ../figure-crops/arxiv_2506.09425/page_013_figure_01.png

Caption:

TABLE I: 2D target functions used in our experiments
