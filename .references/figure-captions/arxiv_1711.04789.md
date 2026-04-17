---
source_pdf: ../arxiv_1711.04789.pdf
pages: 8
captions: 4
extracted_at: 2026-04-17T12:32:32+00:00
extractor: PyMuPDF (fitz)
---

# arxiv_1711.04789 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## FIG. 1.

Page: 2
Caption bbox: (317.0, 459.2, 562.2, 562.4)
Crop bbox: (333.0, 274.9, 546.1, 453.6)
Crop asset: ../figure-crops/arxiv_1711.04789/page_002_figure_01.png

Caption:

FIG. 1. A depiction of how the canonical Jordan-Wigner or-
dering changes throughout ﬁve layers of fermionic swap gates.
Each circle represents a qubit in a linear array (qubits do not
move) and ϕp labels which spin-orbital occupancy is encoded
by the qubit during a particular gate layer. The lines in be-
tween qubits indicate fermionic swap gates which change the
canonical ordering so that the spin-orbitals are represented
by diﬀerent qubits in the subsequent layer. After N layers,
the canonical ordering is reversed, and each spin-orbital has
been adjacent to all others exactly once.

## FIG. 2.

Page: 4
Caption bbox: (54.0, 164.4, 299.1, 257.0)
Crop asset: none

Caption:

FIG. 2.
The numbers above indicate the order in which
matrix elements should be eliminated using nearest-neighbor
Givens rotations. We see that two elements must be elimi-
nated before any parallelization can begin. Each element is
eliminated via rotation with the row directly above it. We
place asterisks (*) on the upper-diagonal to emphasize that
one only needs to focus on removing the lower-diagonal ele-
ments; since the initial matrix and rotations are both unitary,
the upper-diagonals will be eliminated simultaneously.

## FIG. 3.

Page: 6
Caption bbox: (317.0, 141.3, 562.2, 275.8)
Crop bbox: (351.3, 44.3, 527.8, 135.7)
Crop asset: ../figure-crops/arxiv_1711.04789/page_006_figure_01.png

Caption:

FIG. 3. Depiction of the mapping of Hubbard sites to a linear
qubit chain.
The circles each represent a spin-orbital.
As
labeled, red circles contain spin-up orbitals and blue circles
contain spin-down orbitals. In the Hubbard Hamiltonian, the
on-site interaction gives a diagonal couplings between the two
spin-orbitals within each spatial orbital (e.g. n3,↑n3,↓) and
the hopping terms are oﬀ-diagonal between adjacent spatial
orbitals of the same spin (e.g. a†
5,↓a6,↓+a†
6,↓a5,↓). The arrows
between the circles indicate the canonical ordering that should
be used in the Jordan-Wigner transformation. The general
pattern here is that we alternate whether the up or down spin-
orbital comes ﬁrst across the rows, and we alternate whether
to order in ascending or descending order across columns.

## FIG. 4.

Page: 7
Caption bbox: (54.0, 267.9, 299.1, 361.6)
Crop bbox: (85.8, 44.3, 270.3, 252.1)
Crop asset: ../figure-crops/arxiv_1711.04789/page_007_figure_01.png

Caption:

FIG. 4. By repeating the pattern of fermionic swaps shown
as UL and UR one is able to bring spin-orbitals from adjacent
rows next to each other in the canonical ordering so that
the hopping term may be applied locally. First, one applies
UL. This will enable application of the remaining horizontal
hopping term that could not previously be reached. Then,
one should repeatedly apply URUL. After each application of
URUL new vertical hopping terms become available until one
has applied URUL a total of
p
