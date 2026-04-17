---
source_pdf: ../arxiv_1610.06546.pdf
pages: 23
captions: 4
extracted_at: 2026-04-17T12:32:29+00:00
extractor: PyMuPDF (fitz)
title: "Hamiltonian Simulation by Qubitization"
author: "Guang Hao Low, Isaac L. Chuang, "
---

# arxiv_1610.06546 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## Table 1

Page: 3
Caption bbox: (85.0, 208.9, 527.0, 287.9)
Crop bbox: (77.0, 77.0, 516.8, 204.9)
Crop asset: ../figure-crops/arxiv_1610.06546/page_003_figure_01.png

Caption:

Table 1:
Comparison of state-of-art with our new approaches (bottom three lines) for approximating e−i ˆ
Ht of
ˆH ∈C2n×2n with error ϵ. The d-sparse simulation oracle describes entries of ˆH with maximum absolute value
∥ˆH∥max = 1 to m bits of precision. The BCCKS oracle provides the decomposition ˆH = Pd
j=1 αj ˆUj, and each
ˆUj is given a cost O(C). The LMR query complexity refers to samples of the density matrix ˆρ = ˆH. This work
generalizes the above with oracles ˆG|0⟩= |G⟩∈Cd, ˆU ∈C2nd×2nd such that ⟨G| ˆU|G⟩= ˆH, where ∥ˆH∥≤1. A
new model where the oracle that outputs the puriﬁcation |ρ⟩= Pd
j=1 αj|j⟩a|ψj⟩, Tra[|ρ⟩⟨ρ|] = ˆρ is provided.

## Table 2

Page: 4
Caption bbox: (85.0, 161.1, 527.0, 213.9)
Crop bbox: (79.7, 77.0, 532.3, 157.1)
Crop asset: ../figure-crops/arxiv_1610.06546/page_004_figure_01.png

Caption:

Table 2: List of six example problems (top row), solvable using the quantum signal processor approach to compute
an operator function f[·] of Hermitian ˆH = ⟨G| ˆU|G⟩. Through qubitization, the scope of inputs to the Quantum
Linear Systems Problem (QLSP) and Gibbs Sampling (Gibbs) can be any ˆH of this form, either indirectly through
Hamiltonian simulation, or directly through quantum signal processing. Quantum Phase Estimation (QPE) here
decides whether eigenphases θ of an implemented unitary satisfy some property e.g. f(θ) ≥1/2.

## Figure 1

Page: 19
Caption bbox: (85.0, 190.5, 527.0, 211.9)
Crop bbox: (8.0, 8.0, 604.0, 186.5)
Crop asset: ../figure-crops/arxiv_1610.06546/page_019_figure_01.png

Caption:

Figure 1:
(Left) Approximation error ϵ = maxθ∈R |A[θ] −iC[θ] −eit sin (θ)|. (A[θ], C[θ]) are real Fourier series
in (cos (kθ), sin (kθ)), k = 0, ..., Q/2, and ϵ is plotted for the upper bound
4tq

## Table 3

Page: 20
Caption bbox: (85.0, 317.6, 527.0, 340.3)
Crop bbox: (77.0, 77.0, 535.0, 313.6)
Crop asset: ../figure-crops/arxiv_1610.06546/page_020_figure_01.png

Caption:

Table 3: Table of phases implementing target function h(θ) = t sin (θ) in quantum signal processing. Errors quoted
refer to ∥⟨+|b ˆV⃗ϕ|+⟩b −e−i ˆ
Ht∥≤ϵ.
