---
source_pdf: ../arxiv_quant-ph_9508027.pdf
pages: 28
captions: 4
extracted_at: 2026-04-17T12:32:46+00:00
extractor: PyMuPDF (fitz)
title: "arXiv:quant-ph/9508027v2  25 Jan 1996"
---

# arxiv_quant-ph_9508027 Figure Report

This report captures caption text and any extracted figure crops detected above those captions. When no reliable crop was found, the caption is still listed so the page can be reviewed manually.

## Table 3.1

Page: 9
Caption bbox: (189.8, 127.2, 421.7, 146.2)
Crop asset: none

Caption:

Table 3.1: Truth tables for Toﬀoli and Fredkin gates.
Toﬀoli Gate

## Table 3.2

Page: 10
Caption bbox: (163.1, 127.2, 452.3, 137.1)
Crop asset: none

Caption:

Table 3.2: Bennett’s method for making a computation reversible.

## Figure 5.1

Page: 18
Caption bbox: (117.7, 368.1, 497.6, 390.1)
Crop bbox: (271.1, 146.7, 480.5, 318.8)
Crop asset: ../figure-crops/arxiv_quant-ph_9508027/page_018_figure_01.png

Caption:

Figure 5.1: The probability P of observing values of c between 0 and 255, given q = 256
and r = 10.

## algorithm for

Page: 23
Caption bbox: (115.8, 120.2, 495.8, 321.5)
Crop asset: none

Caption:

algorithm for factoring. If we knew the remainder of r modulo all prime powers dividing
p −1, we could use the Chinese remainder theorem to recover r in polynomial time. We
will only be able to prove that we can ﬁnd this remainder for primes larger than 18, but
with a little extra work we will still be able to recover r.
Recall that each good (c, d) pair is generated with probability at least 1/(20q2), and
that at least a twelfth of the possible c’s are in a good (c, d) pair. From equation (6.19),
it follows that these c’s are mapped from c/q to c′/(p −1) by rounding to the nearest
integral multiple of 1/(p −1). Further, the good c’s are exactly those in which c/q is
close to c′/(p −1). Thus, each good c corresponds with exactly one c′. We would like
to show that for any prime power pαi
i
dividing p −1, a random good c′ is unlikely to
contain pi. If we are willing to accept a large constant for our algorithm, we can just
ignore the prime powers under 18; if we know r modulo all prime powers over 18, we can
try all possible residues for primes under 18 with only a (large) constant factor increase
in running time. Because at least one twelfth of the c’s were in a good (c, d) pair, at
least one twelfth of the c′’s are good. Thus, for a prime power pαi
i , a random good c′ is
divisible by pαi
i
with probability at most 12/pαi
i . If we have t good c′’s, the probability
of having a prime power over 18 that divides all of them is therefore at most
