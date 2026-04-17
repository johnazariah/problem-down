---
source_pdf: ../arxiv_1404.6539.pdf
pages: 26
extracted_at: 2026-04-17T12:32:29+00:00
extractor: PyMuPDF (fitz)
reflow: column-aware block ordering
---

# arxiv_1404.6539

Source PDF: ../arxiv_1404.6539.pdf

> Extraction note: this is text recovered from the PDF for analysis, not a hand-corrected transcription. The extractor reorders many two-column pages more naturally than a raw text dump, but formulas, figures, footnotes, and dense layouts may still degrade.

## Page 1

A RIGGED CONFIGURATION MODEL FOR Bp8q

BEN SALISBURY AND TRAVIS SCRIMSHAW

arXiv:1404.6539v4 [math.CO] 12 Feb 2015

Abstract. We describe a combinatorial realization of the crystals Bp8q and
Bpλq using rigged conﬁgurations in all symmetrizable Kac-Moody types up to
certain conditions. This includes all simply-laced types and all non-simply-
laced ﬁnite and aﬃne types.

1. Introduction

Crystal basis theory is an elegant and fruitful subject born out of the theory of
quantum groups. Deﬁned by Kashiwara in the early 1990s [13, 14], crystals provide
a natural combinatorial framework to study the representations of Kac-Moody alge-
bras (including classical Lie algebras) and their associated quantum groups. Their
applications span many areas of mathematics, including representation theory, al-
gebraic combinatorics, automorphic forms, and mathematical physics, to name a
few.
The study of crystal bases has led researchers to develop diﬀerent combinatorial
models for crystals which yield suitable settings to studying a particular aspect of
the representation theory of quantum groups. For example, highest weight crystals
(which are combinatorial skeletons of an irreducible highest weight module over a
quantum group) can be modeled using generalized Young tableaux [12, 18], using
the Littelmann path model [26, 27, 28, 29], using alcove paths [24, 25] or alcove
walks [35], using geometric methods [4, 7, 19], and many others. The choice of
using one model over the other usually depends on the underlying question at hand
(and/or on the preference of the author). In concert with the descriptions for the
highest weight crystals, there are several known realizations of the (inﬁnite) crystal
Bp8q (which is a combinatorial skeleton for the Verma module with highest weight
0), both in combinatorial and geometric settings, which have various applications.
Combinatorially describing the crystal Bp8q in aﬃne types is still a work in progress
(see [21, 22] for a generalization of the tableaux model to the aﬃne setting in certain
types), so another combinatorial model for Bp8q in aﬃne types may prove useful.
Our choice of model will be that of rigged conﬁgurations, which arise natu-
rally as indexing the eigenvalues and eigenvectors of a Hamiltonian of a statistical
model [3, 20, 23]. On the other hand, these eigenvectors may also be indexed by one-
dimensional lattice paths [2, 8, 9, 30, 41], which can be interpreted as highest weight
vectors in a tensor product of certain crystals. In recent years, the implied con-
nection between highest weight vectors in tensor products of Kirillov-Reshetikhin
crystals and rigged conﬁgurations has been worked out [32, 34, 37, 38, 40].

2010 Mathematics Subject Classiﬁcation. 05E10, 17B37.
Key words and phrases. crystal, rigged conﬁguration, quantum group.
T.S. was partially supported by NSF grant OCI-1147247.

1

## Page 2

2
BEN SALISBURY AND TRAVIS SCRIMSHAW

As we will show, the rigged conﬁguration model has simple combinatorial rules
for describing the structure which work in all ﬁnite, aﬃne, and all simply-laced Kac-
Moody types. These combinatorial rules are only based on the nodes of the Dynkin
diagram and their neighbors. This allows us to easily describe the embeddings of
Bpλq into Bpµq, where λa ď µa for all indices a. Moreover, we can easily describe
the so-called virtualization of Bpλq inside of a highest weight crystal of simply-laced
type via a diagram folding.
The purpose of this paper is to extend the crystal structure on highest weight
crystals in ﬁnite type in terms of rigged conﬁgurations [6, 31, 37, 38, 40] to other
types and to a crystal model for Bp8q in terms of rigged conﬁgurations. In slightly
more detail, the crystal Bp8q is a direct limit of all highest weight crystals, so
by relaxing a certain admissibility condition on elements of the highest weight
crystal, we may obtain a representative of an element of Bp8q given by a rigged
conﬁguration. An added perk of describing Bp8q using rigged conﬁgurations is
that the description is type-independent.
However our proofs are almost type-
independent as we can do our proofs uniformly across all simply-laced ﬁnite types,
but there will be some changes in the extension to non-simply-laced ﬁnite types
and then, again, when extending outside of ﬁnite type.
The organization of this paper goes as follows. Section 2 gives a background on
crystals and rigged conﬁgurations. In Section 3, we describe the rigged conﬁguration
model for Bp8q for simply-laced ﬁnite types. In Section 4, we extend our model
for arbitrary simply-laced types. We extend our model to all ﬁnite, aﬃne, and
certain indeﬁnite (symmetrizable) types in Section 5.
We describe how highest
weight crystals sit inside our Bp8q model using rigged conﬁgurations in Section 6.

Notational remark. The notation g may denote diﬀerent objects in diﬀerent
sections, but we will make this clear near the beginning of each (sub)section.

2. Background

2.1. Crystals. Let g be a symmetrizable Kac-Moody algebra with index set I,
generalized Cartan matrix A “ pAijqi,jPI, weight lattice P, root lattice Q, funda-
mental weights tΛi : i P Iu, simple roots tαi : i P Iu, and simple coroots thi : i P Iu.
There is a canonical pairing x , y: P _ ˆ P ÝÑ Z deﬁned by xhi, αjy “ Aij, where
P _ is the dual weight lattice.
An abstract Uqpgq-crystal is a nonempty set B together with maps

wt: B ÝÑ P,
εi, ϕi : B ÝÑ Z \ t´8u,
ei, fi : B ÝÑ B \ t0u,

subject to the conditions
(1) ϕipbq “ εipbq ` xhi, wtpbqy for all i P I,
(2) if b P B satisﬁes eib ‰ 0, then
(a) εipeibq “ εipbq ´ 1,
(b) ϕipeibq “ ϕipbq ` 1,
(c) wtpeibq “ wtpbq ` αi,
(3) if b P B satisﬁes fib ‰ 0, then
(a) εipfibq “ εipbq ` 1,
(b) ϕipfibq “ ϕipbq ´ 1,
(c) wtpfibq “ wtpbq ´ αi,
(4) fib “ b1 if and only if b “ eib1 for b, b1 P B and i P I,
(5) if ϕipbq “ ´8 for b P B, then eib “ fib “ 0.

## Page 3

A RIGGED CONFIGURATION MODEL FOR Bp8q
3

The operators ei and fi, for i P I, are referred to as the Kashiwara raising and
Kashiwara lowering operators, respectively. See [10, 14] for details.

Example 2.1. For a dominant integral weight λ, the crystal basis

Bpλq “ tfik ¨ ¨ ¨ fi1uλ : i1, . . . , ik P I, k P Zě0uzt0u

of an irreducible, highest weight Uqpgq-module V pλq is an abstract Uqpgq-crystal.
The crystal Bpλq is characterized by the following properties.

(1) The element uλ P Bpλq is the unique element such that wtpuλq “ λ.
(2) For all i P I, eiuλ “ 0.
(3) For all i P I, f xhi,λy`1
i
uλ “ 0.

Example 2.2. The crystal basis

Bp8q “ tfik ¨ ¨ ¨ fi1u8 : i1, . . . , ik P I, k P Zě0u

of the negative half U ´
q pgq of the quantum group is an abstract Uqpgq-crystal. Some
important properties of Bp8q are the following.

(1) The element u8 P Bp8q is the unique element such that wtpu8q “ 0.
(2) For all i P I, eiu8 “ 0.
(3) For any sequence pi1, . . . , ikq from I, fik ¨ ¨ ¨ fi1u8 ‰ 0.

An abstract Uqpgq-crystal is said to be upper regular if, for all b P B,

εipbq “ maxtk P Zě0 : ek
i b ‰ 0u.

Similarly, an abstract Uqpgq-crystal is said to be lower regular if, for all b P B,

ϕipbq “ maxtk P Zě0 : f k
i b ‰ 0u.

If B is both upper regular and lower regular, then we say B is regular. In this latter
case, we may depict the entire i-string through b P B diagrammatically as

eεipbq
i
b
i
ÝÑ eεipbq´1
i
b
i
ÝÑ ¨ ¨ ¨
i
ÝÑ eib
i
ÝÑ b
i
ÝÑ fib
i
ÝÑ ¨ ¨ ¨
i
ÝÑ f ϕipbq´1
i
b
i
ÝÑ f ϕipbq
i
b.

Note that Bpλq is a regular abstract Uqpgq-crystal, but Bp8q is only upper regular.
Let B1 and B2 be two abstract Uqpgq-crystals. A crystal morphism ψ: B1 ÝÑ B2
is a map B1 \ t0u ÝÑ B2 \ t0u such that

(1) ψp0q “ 0;
(2) if b P B1 and ψpbq P B2, then wtpψpbqq “ wtpbq, εipψpbqq “ εipbq, and
ϕipψpbqq “ ϕipbq;
(3) for b P B1, we have ψpeibq “ eiψpbq provided ψpeibq ‰ 0 and eiψpbq ‰ 0;
(4) for b P B1, we have ψpfibq “ fiψpbq provided ψpfibq ‰ 0 and fiψpbq ‰ 0.

A morphism ψ is called strict if ψ commutes with ei and fi for all i P I. Moreover,
a morphism ψ: B1 ÝÑ B2 is called an embedding if the induced map B1 \ t0u ÝÑ
B2 \ t0u is injective.
We say an abstract Uqpgq-crystal is simply a Uqpgq-crystal if it is crystal isomor-
phic to the crystal basis of a Uqpgq-module.
Again let B1 and B2 be abstract Uqpgq-crystals. The tensor product B2 b B1
is deﬁned to be the Cartesian product B2 ˆ B1 equipped with crystal operations

## Page 4

4
BEN SALISBURY AND TRAVIS SCRIMSHAW

deﬁned by

#
eib2 b b1
if εipb2q ą ϕipb1q,
b2 b eib1
if εipb2q ď ϕipb1q,

eipb2 b b1q “

#
fib2 b b1
if εipb2q ě ϕipb1q,
b2 b fib1
if εipb2q ă ϕipb1q,

fipb2 b b1q “

εipb2 b b1q “ max
`
εipb2q, εipb1q ´ xhi, wtpb2qy
˘
,

ϕipb2 b b1q “ max
`
ϕipb1q, ϕipb2q ` xhi, wtpb1qy
˘
,

wtpb2 b b1q “ wtpb2q ` wtpb1q.

Remark 2.3. Our convention for tensor products is opposite the convention given
by Kashiwara in [14].

More generally if B1, . . . , Bt are regular crystals, to compute the action of the
Kashiwara operators on the tensor product B “ Bt b ¨ ¨ ¨ b B2 b B1, we use the
signature rule. Indeed, for i P I and b “ bt b ¨ ¨ ¨ b b2 b b1 in B, write

` ¨ ¨ ¨ `
loomoon

ϕipbtq
´ ¨ ¨ ¨ ´
loomoon

εipb1q
.

εipbtq
¨ ¨ ¨ ` ¨ ¨ ¨ `
loomoon

ϕipb1q
´ ¨ ¨ ¨ ´
loomoon

From the above sequence, successively delete any p´, `q-pair to obtain a sequence

i-sgnpbq :“ ` ¨ ¨ ¨ `
loomoon

εipbq
.

ϕipbq
´ ¨ ¨ ¨ ´
loomoon

Suppose 1 ď j´, j` ď t are such that bj´ contributes the leftmost ´ in i-sgnpbq and
bj` contributes the rightmost ` in i-sgnpbq. Then

eib “ bt b ¨ ¨ ¨ b bj´`1 b eibj´ b bj´´1 b ¨ ¨ ¨ b b1,

fib “ bt b ¨ ¨ ¨ b bj``1 b fibj` b bj`´1 b ¨ ¨ ¨ b b1.

Let C denote the category of abstract Uqpgq-crystals. In [17], Kashiwara showed
that direct limits exist in C . Indeed, let tBjujPJ be a directed system of crystals
and let ψk,j : Bj ÝÑ Bk, j ď k, be a crystal morphism (with ψj,j being the identity
map on Bj) such that ψk,jψj,i “ ψk,i. Let ⃗B “ lim
ÝÑ Bj be the direct limit of this
system and let ψj : Bj ÝÑ ⃗B. Then ⃗B has a crystal structure induced from the
crystals tBjujPJ. Indeed, for ⃗b P ⃗B and i P I, deﬁne ei⃗b to be ψjpeibjq if there
exists bj P Bj such that ψjpbjq “ ⃗b and eipbjq ‰ 0. This deﬁnition does not depend
on the choice of bj. If there is no such bj, then set ei⃗b “ 0. The deﬁnition of fi⃗b is
similar. Moreover, the functions wt, εi, and ϕi on Bj extend to functions on ⃗B.

2.2. Rigged conﬁgurations. Let g be a symmetrizable Kac-Moody algebra with
index set I. Set H “ I ˆ Zą0. Consider a multiplicity array

L “
`
Lpaq
i
P Zě0 : pa, iq P H
˘

and a dominant integral weight λ of g. We call a sequence of partitions ν “ tνpaq :
a P Iu an pL, λq-conﬁguration if
ÿ

pa,iqPH
impaq
i
αa “
ÿ

pa,iqPH
iLpaq
i
Λa ´ λ,
(2.1)

## Page 5

A RIGGED CONFIGURATION MODEL FOR Bp8q
5

where mpaq
i
is the number of parts of length i in the partition νpaq. The set of all
such pL, λq-conﬁgurations is denoted CpL, λq. To an element ν P CpL, λq, deﬁne
the vacancy number of ν to be

ppaq
i
“ ppaq
i
pνq “
ÿ

jě0
minpi, jqLpaq
j
´
ÿ

pb,jqPH

Aab

γb
minpγai, γbjqmpbq
j ,
(2.2)

where tγa : a P Iu are some set of positive integers. If g is of simply-laced type, we
take γa “ 1 for all a P I.
Recall that a partition is a multiset of integers (typically sorted in decreasing
order). A rigged partition is a multiset of pairs of integers pi, xq such that i ą 0
(typically sorted under decreasing lexicographic order). Each pi, xq is called a string,
where i is called the length or size of the string and x is the label, rigging, or
quantum number of the string. Finally, a rigged conﬁguration is a pair pν, Jq where
ν P CpL, λq and J “
`
Jpaq
i
˘

pa,iqPH where each Jpaq
i
the weakly decreasing sequence

of riggings of strings of length i in νpaq. We call a rigged conﬁguration valid if
every label x P Jpaq
i
satisﬁes the inequality ppaq
i
ě x for all pa, iq P H. We say a
rigged conﬁguration is highest weight if x ě 0 for all labels x. Deﬁne the colabel or
coquantum number of a string pi, xq to be ppaq
i
´x. For brevity, we will often denote
the ath part of pν, Jq by pν, Jqpaq (as opposed to pνpaq, Jpaqq).

Example 2.4. Rigged conﬁgurations will be depicted as sequences of partitions
with parts labeled on the left by the corresponding vacancy number and labeled on
the right by the corresponding rigging. For example,

´1
´1
´1
´1

1
1
1

1
1
1

0
0
0
0

0
´2
0
0

0
0
0
0

0
0
0
0

is a rigged conﬁguration with g “ D5 and L is given by Lp1q
2
“ Lp2q
1
“ Lp3q
1
“ 1
with all other Lpaq
i
“ 0.

Denote by RC˚pL, λq the set of valid highest weight rigged conﬁgurations pν, Jq
such that ν P CpL, λq. In [38], an abstract Uqpgq-crystal structure was given to
rigged conﬁgurations, which we recall ﬁrst by deﬁning the Kashiwara operators.

Deﬁnition 2.5. Let pν, Jq be a valid rigged conﬁguration. Fix a P I and let x be
the smallest label of pν, Jqpaq.
(1) If x ě 0, then set eapν, Jq “ 0. Otherwise, let ℓbe the minimal length of
all strings in pν, Jqpaq which have label x. The rigged conﬁguration eapν, Jq
is obtained by replacing the string pℓ, xq with the string pℓ´ 1, x ` 1q and
changing all other labels so that all colabels remain ﬁxed.
(2) If x ą 0, then add the string p1, ´1q to pν, Jqpaq. Otherwise, let ℓbe the
maximal length of all strings in pν, Jqpaq which have label x. Replace the
string pℓ, xq by the string pℓ` 1, x ´ 1q and change all other labels so that
all colabels remain ﬁxed. If the result is a valid rigged conﬁguration, then
it is fapν, Jq . Otherwise fapν, Jq “ 0.

Let RCpL, λq denote the set generated by RC˚pL, λq by the Kashiwara operators.
For pν, Jq P RCpL, λq, if fa adds a box to a string of length ℓin pν, Jqpaq, then the

## Page 6

6
BEN SALISBURY AND TRAVIS SCRIMSHAW

vacancy numbers in simply-laced type are changed using the formula

ppbq
i
“

#
ppbq
i
if i ď ℓ,
ppbq
i
´ Aab
if i ą ℓ.
(2.3)

On the other hand, if ea removes a box from a string of length ℓ, then the vacancy
numbers must be changed using

ppbq
i
“

#
ppbq
i
if i ă ℓ,
ppbq
i
` Aab
if i ě ℓ.
(2.4)

Let RCpLq be the closure under the Kashiwara operators of the set RC˚pLq “
Ť
λPP ` RC˚pL, λq. Lastly, the weight map wt: RCpLq ÝÑ P is deﬁned as

wtpν, Jq “
ÿ

pa,iqPH
i
`
Lpaq
i
Λa ´ mpaq
i
αa
˘
.
(2.5)

Example 2.6. Let pν, Jq be the rigged conﬁguration from Example 2.4. Then

e3pν, Jq “
´1
´1
´1
´1

0
0
1

0
0
1

2
0
0
0

and

´1
´1
´1
´1

´1
´1
´1
´1

f2pν, Jq “
0
0
0
0

1
1
1
1

Also we have

´1
0
´1
0

´1
0
´1
0

2
0
0
0

1
´1
1
1

0
0
0
0

0
0
0
0
.

wt
`
pν, Jq
˘
“ 2Λ1 ` Λ2 ` Λ3 ´ 4α1 ´ 5α2 ´ 6α3 ´ 3α4 ´ 3α5
“ ´Λ1 ` Λ2,

wt
`
e3pν, Jq
˘
“ ´Λ1 ` 2Λ3 ´ Λ4 ´ Λ5 “ ´Λ1 ` Λ2 ` α3,

wt
`
f2pν, Jq
˘
“ ´Λ2 ` Λ3 “ ´Λ1 ` Λ2 ´ α2,

Theorem 2.7 ([38, Thm. 3.7]). Let g be a simply-laced Lie algebra. For pν, Jq P
RC˚pL, λq, let Xpν,Jq be the graph generated by pν, Jq and ea, fa for a P I. Then
Xpν,Jq is isomorphic to the crystal graph Bpλq as Uqpgq-crystals.

Remark 2.8. In [38], elements of Xpν,Jq were called unrestricted rigged conﬁgura-
tions and the graph Xpν,Jq was denoted Xp

Jq.

ν,

We note that our condition for highest weight rigged conﬁgurations is equivalent
to the rigged conﬁguration being highest weight in the sense of a crystal of type g;
i.e., that the action of all ea on a highest weight rigged conﬁguration is 0.
In the sequel, set νH to be the multipartition with all parts empty; that is, set
νH “ pνp1q, . . . , νpnqq where νpaq
i
“ H for all pa, iq P H. Therefore the rigging JH
of νH must be Jpaq
i
“ H for all pa, iq P H. When discussing the highest weight
crystals XpνH,JHq, we will choose our multiplicity array L to be such that
ÿ

pa,iqPH
iLpaq
i
Λa “ λ.

## Page 7

A RIGGED CONFIGURATION MODEL FOR Bp8q
7

It is clear that there are several choices of L that may ﬁt this condition, but this
does not aﬀect the crystal structure.

Deﬁnition 2.9. Deﬁne RCpλq to be XpνH,JHq for any symmetrizable Kac-Moody
algebra.

3. Rigged configuration model for Bp8q in simply-laced finite type

For this section, unless otherwise noted, let g be a Lie algebra of simply-laced
ﬁnite type. We wish to generate a model for Bp8q with pνH, JHq as its highest
weight vector. By choosing a ﬁxed λ ą 0, for any pν, Jq P RCpλq, there exists k ě 0
such that f k
a pν, Jq “ 0 by the validity condition given in Deﬁnition 2.5. Therefore,
we need a modiﬁed Kashiwara operator f 1
a (for a P Iq on rigged conﬁgurations to
allow the condition pf 1
aqkpν, Jq ‰ 0 for all k ě 0. To do so, simply deﬁne f 1
a by the
same process given in Deﬁnition 2.5 with the validity condition omitted and choose
λ “ 0.

Deﬁnition 3.1. For any symmetrizable Kac-Moody algebra g with index set I,
deﬁne RCp8q to be the graph generated by pνH, JHq, ea, and f 1
a, for a P I, where
ea acts on elements pν, Jq in RCp8q using the same procedure as in Deﬁnition 2.5.

The remainder of the crystal structure is given by

εapν, Jq “ maxtk P Zě0 : ek
apν, Jq ‰ 0u,
(3.1a)

ϕapν, Jq “ εapν, Jq ` xha, wtpν, Jqy,
(3.1b)

wtpν, Jq “ ´
ÿ

pa,iqPH
impaq
i
αa “ ´
ÿ

aPI
|νpaq|αa.
(3.1c)

It is worth noting that, in this case, the deﬁnition of the vacancy numbers reduces
to
ppaq
i
pνq “ ppaq
i
“ ´
ÿ

pb,jqPH
Aab minpi, jqmpbq
j .
(3.2)

Example 3.2. Let g be of type A5 and pν, Jq be the rigged conﬁguration

pν, Jq “
´1
´1
´1
´2
1
0
´1
0
´1
´3

Then wtpν, Jq “ ´α1 ´ 2α2 ´ α3 ´ α4 ´ 2α5,

e2pν, Jq “
´1
´1
0
0
1
0
´1
0
´1
´3

and

f2pν, Jq “
´1
´1
´2
´4
1
0
´1
0
´1
´3

Lemma 3.3. The set RCp8q is an abstract Uqpgq-crystal with Kashiwara operators
ea and f 1
a and remaining crystal structure given in equation (3.1).

Proof. This proof here is similar to that given in Proposition 9 of [37]. We need to
show the following, for pν, Jq in RCp8q.
(1) If eapν, Jq ‰ 0 for a P I, then f 1
aeapν, Jq “ pν, Jq.
(2) For any a P I, we have eaf 1
apν, Jq “ pν, Jq.
(3) If eapν, Jq ‰ 0 for a P I, then wt
`
eapν, Jq
˘
“ wtpν, Jq ` αa.
(4) For a P I, wt
`
f 1
apν, Jq
˘
“ wtpν, Jq ´ αa.
(5) For a P I, εa
`
f 1
apν, Jq
˘
“ εapν, Jq ` 1 and ϕa
`
f 1
apν, Jq
˘
“ ϕapν, Jq ´ 1.

## Page 8

8
BEN SALISBURY AND TRAVIS SCRIMSHAW

Let pν, Jq be an arbitrary rigged conﬁguration in RCp8q. In what follows, we will
suppose that mpaq
i
is the number of parts of length i in the partition νpaq and that
x is the smallest label of pν, Jqpaq. Set pν1, J1q “ f 1
apν, Jq and pν2, J2q “ eapν, Jq.
To prove (1), suppose that pν2, J2q is obtained from pν, Jq by changing the string
pℓ, xq to pℓ´ 1, x ` 1q, so that ℓis the minimal length string among all strings with
label x. If i ă ℓand pi, yq is a string in pν, Jq, then ppaq
i
pν2q “ ppaq
i
pνq by (2.4).
Thus pi, yq is unaﬀected by the action of ea, and y ě x ` 1. On the other hand,
if i ě ℓ, then ppaq
i
pν2q “ ppaq
i
pνq ` 2 by (2.4). Thus pi, yq is replaced by the string
pi, y ` 2q under the action of ea and y ` 2 ą x ` 1. In both cases, pℓ´ 1, x ` 1q is
the string with minimal label and longest length, so f 1
a will change pℓ´ 1, x ` 1q to
pℓ, xq and f 1
aeapν, Jq “ pν, Jq, as required.
Suppose that pν1, J1q is obtained from pν, Jq by changing the string pℓ, xq to
pℓ` 1, x ´ 1q, so ℓis the maximal length of all strings with label x. If i ď ℓand
pi, yq is a string in pν, Jqpaq, then ppaq
i
pν1q “ ppaq
i
pνq by (2.3). Thus pi, yq is left
unaﬀected by the action of f 1
a, and y ą x ´ 1 because x is the smallest label of
pν, Jq. On the other hand, if i ą ℓ, then ppaq
i
pν1q “ ppaq
i
pνq ´ 2 by (2.3). Thus
pi, yq is replaced by pi, y ´ 2q by the action of f 1
a and y ´ 2 ě x ´ 1. In both cases,
pℓ` 1, x ´ 1q is the string with minimal label and shortest length, so ea will change
pℓ` 1, x ´ 1q to pℓ, xq and eaf 1
apν, Jq “ pν, Jq to prove (2).
For (3), if pν2, J2q ‰ 0 for some a P I, then pν2, J2q is obtained from pν, Jq by
replacing the string pℓ, xq with pℓ´ 1, x ` 1q, where ℓis the minimal length of all
strings in pν, Jqpaq having label x. Then |ν2paq| “ |νpaq| ´ 1 and the result follows.
To see (4), if x ą 0, then the string p1, ´1q is added to pν, Jqpaq. Then |ν1paq| “
|νpaq| ` 1. On the other hand, if x ď 0 and ℓis the maximal length of all strings in
pν, Jqpaq with label x, then the string pℓ, xq is replaced by the string pℓ`1, x´1q, so
|ν1paq| “ |νpaq| ` 1. In both cases, the equality |ν1paq| “ |νpaq| ` 1 yields the desired
result.
The ﬁrst part of (5) follows immediately from the deﬁnition. To see ϕa
`
f 1
apν, Jq
˘
“
ϕa
`
pν, Jq
˘
´ 1, we have

ϕa
`
f 1
apν, Jq
˘
“ xha, wt
`
f 1
apν, Jq
˘
y ` εa
`
f 1
apν, Jq
˘

“ xha, wtpν, Jqy ´ xha, αay ` εapν, Jq ` 1

“ xha, wtpν, Jqy ´ 2 ` εapν, Jq ` 1

“ ϕapν, Jq ´ 1.

Deﬁnition 3.4. For a weight λ, let Tλ “ ttλu be the abstract Uqpgq-crystal with
operations deﬁned by

eatλ “ fatλ “ 0,
εaptλq “ ϕaptλq “ ´8,
wtptλq “ λ.

For any abstract Uqpgq-crystal B, the tensor product TλbB has the same crystal
graph as B, but with each weight shifted by λ (and appropriate modiﬁcations to
εa and ϕa). Following [17], there is an embedding of crystals

Iλ`µ,λ : T´λ b Bpλq ãÝÑ T´λ´µ b Bpλ ` µq

which sends t´λ b uλ ÞÑ t´λ´µ b uλ`µ and commutes with ea for each a P I.
Moreover, for any three dominant weights λ, µ, and ξ, we get a commutative

## Page 9

A RIGGED CONFIGURATION MODEL FOR Bp8q
9

diagram

Iλ`µ,λ

T´λ b Bpλq
T´λ´µ b Bpλ ` µq

Iλ`µ`ξ,λ`µ
(3.3)

T´λ´µ´ξ b Bpλ ` µ ` ξq.

Using the order on dominant integral weights given by µ ď λ if and only if λ ´ µ P
P `, the set tT´λ b BpλquλPP ` is a directed system.

Theorem 3.5 ([17]). We have Bp8q “ lim
ÝÑ
λPP `
T´λ b Bpλq.

By Theorem 2.7, each Bpλq is Uqpgq-crystal isomorphic to the graph RCpλq
generated by a highest weight rigged conﬁguration pν, Jq of weight λ in RCpLq and
the Kashiwara operators ea and fa deﬁned in Deﬁnition 2.5. Thus we have

lim
ÝÑ
λPP `
T´λ b Bpλq – lim
ÝÑ
λPP `
T´λ b RCpλq.

Our goal is to complete the diagram

–

lim
ÝÑ
λPP `
T´λ b Bpλq
lim
ÝÑ
λPP `
T´λ b RCpλq

Bp8q

(3.4)

RCp8q

by proving that the dashed equality on the right side of the square is actually
an equality among Uqpgq-crystals. Then we may deﬁne an isomorphism along the
bottom of the square by taking the composite map along the top of the diagram.

Lemma 3.6. Let λ and µ be dominant integral weights, and let

rIλ`µ,λ : T´λ b RCpλq ÝÑ T´λ´µ b RCpλ ` µq

by t´λbpν, Jq ÞÑ t´λ´µbpν1, J1q, where pν1, J1q “ pν, Jq as rigged conﬁgurations but
has vacancy numbers considered as an element of RCpλ ` µq. For pν, Jq P RCpλq,
the image pν1, J1q is valid in RCpλ ` µq. Moreover, rIλ`µ,λ is a crystal embedding.

Proof. Write λ “ ř
pa,iqPH iLpaq
i
Λa and µ “ ř
pa,iqPH iKpaq
i
Λa. Then

ppaq
i
pνq “
ÿ

jě1
minpi, jqLpaq
j
´
ÿ

ď
ÿ

pb,jqPH
pαa|αbq minpi, jqmpbq
j

jě1
minpi, jq
`
Lpaq
j
` Kpaq
j
˘
´
ÿ

“ ppaq
i
pν1q.

Thus

pb,jqPH
pαa|αbq minpi, jqmpbq
j

max Jpaq
i
“ max J1paq
i
ď ppaq
i
pνq ď ppaq
i
pν1q,

## Page 10

10
BEN SALISBURY AND TRAVIS SCRIMSHAW

for all pa, iq P H such that Jpaq
i
‰ H (and hence J1paq
i
‰ H). This proves that
pν1, J1q is valid so that rIλ`µ,λ is well-deﬁned. Moreover, we have

wt
`
t´λ´µ b pν1, J1q
˘

“ ´pλ ` µq ` wtpν1, J1q

“ ´
ÿ

pa,iqPH
i
`
Lpaq
i
` Kpaq
i
˘
Λa `
ÿ

“ ´
ÿ

pa,iqPH
iLpaq
i
Λa `
ÿ

“ ´λ ` wtpν, Jq

“ wt
`
t´λ b wtpν, Jq
˘
,

pa,iqPH
i
`
pLpaq
i
` Kpaq
i
qΛa ´ mpaq
i
αaq

pa,iqPH
i
`
Lpaq
i
Λa ´ mpaq
i
αa
˘

which shows that rIλ`µ,λ preserves the weight map. Since rIλ`µ,λ is the identity on
rigged conﬁgurations, we obtain that ea commutes with rIλ`µ,λ and rIλ`µ,λ preserves
εa, for all a P I. Also, fa commutes with rIλ`µ,λ if fapν, Jq ‰ 0 because the map is
the identity map on rigged conﬁgurations. Then

ϕapν1, J1q “ εapν1, J1q ` xha, µ ` λy

“ εapν, Jq ` xha, λy ` xha, µy

“ ϕapν, Jq ` xha, µy,

so we have

ϕa
`
t´λ b pν, Jq
˘
“ maxt´8, ϕapν, Jq ` xha, ´λyu

“ ϕapν, Jq ` xha, ´λy

“ ϕapν1, J1q ` xha, ´λ ´ µy

“ maxt´8, ϕapν1, J1q ` xha, ´λ ´ µyu

“ ϕa
`
t´λ´µ b pν1, J1q
˘
.

Hence rIλ`µ,λ is a crystal embedding.

To complete the construction of a directed system of crystals of rigged conﬁg-
urations, we have the following lemma, which follows from a modiﬁcation of the
proof of Lemma 3.6.

Lemma 3.7. For dominant integral weights λ, µ, and ξ, the diagram

rIλ`µ,λ

T´λ b RCpλq
T´λ´µ b RCpλ ` µq

commutes.

rIλ`µ`ξ,λ`µ

T´λ´µ´ξ b RCpλ ` µ ` ξq.

Proof. Follows by repeated use of Lemma 3.6 and the fact that rI´,´ is the identity
on rigged conﬁgurations.

Lemma 3.8. We have RCp8q “ lim
ÝÑ
λPP `
T´λ b RCpλq as abstract Uqpgq-crystals.

## Page 11

A RIGGED CONFIGURATION MODEL FOR Bp8q
11

Proof. By Lemmas 3.6 and 3.7, tT´λ b RCpλquλPP ` forms a directed system. Let
X denote the direct limit lim
ÝÑ T´λ b RCpλq. Let Θ: X ÝÑ RCp8q be the identity
map on rigged conﬁgurations; that is, for x P X such that x “ rIλpt´λ b pν, Jqq,
we have Θpxq “ pν, Jq. To make the setting clear, we will denote the Kashiwara
operators on X by ⃗ea, ⃗fa, the Kashiwara operators on RCpλq and T´λ b RCpλq by
eλ
a, f λ
a , and the Kashiwara operators on RCp8q by ea, f 1
a.
To see that Θ commutes with Kashiwara lowering operators, for x P X and λ
such that x “ rIλ
`
t´λ b pν, Jq
˘
, we have

⃗fax “ rIλ
`
f λ
a pt´λ b pν, Jqq
˘
“ rIλ
`
t´λ b f λ
a pν, Jq
˘
,

where t´λ b pν, Jq satisﬁes the condition f λ
a pν, Jq ‰ 0. Note that any such λ will
suﬃce by the deﬁnition of the direct limit. Thus

Θp⃗faxq “ f λ
a pν, Jq “ f 1
apν, Jq “ f 1
aΘpxq.

The calculation involving the Kashiwara raising operators is similar. By the deﬁni-
tion of the weight function, it is clear that Θ preserves weights. Moreover, Θ sends
the highest weight vector of X to the highest weight vector pνH, JHq of RCp8q, so
Θ is a bijection.

Theorem 3.9. Let g be a Lie algebra of simply-laced ﬁnite type. Then there exists
a Uqpgq-crystal isomorphism Bp8q – RCp8q which sends u8 ÞÑ pνH, JHq.

Proof. By Lemma 3.8, the dashed arrow on the right-hand of the square in (3.4)
becomes an isomorphism of Uqpgq-crystals, so we may construct an isomorphism
by composing the maps along the outside of the square.

Remark 3.10. From this point forward, we denote f 1
a simply by fa. This should
not cause any confusion.

4. Extending Theorem 3.9 to arbitrary simply-laced Kac-Moody
algebras

We show the convexity condition holds for general symmetrizable types.

Lemma 4.1. Consider a rigged conﬁguration pν, Jq. Fix pa, iq P H and suppose that
mpaq
i
“ 0. Let Ca,b, C1
a,b, C_
a,b P Zą0 for all a, b P I, and consider the generalization
of the vacancy numbers for pν, Jq to

ppaq
i
“
ÿ

jě1
minpi, jqLpaq
j
´
ÿ

pb,jqPH
C_
a,bAab minpCa,bi, C1
a,bjqmpbq
j

We have
2ppaq
i
ě ppaq
i´1 ` ppaq
i`1.

Proof. Consider any pb, jq P H and deﬁne

8
ÿ

Qpbq
j
“

k“1
minpCa,bj, C1
a,bkqmpbq
k .

This is the number of boxes in the ﬁrst Ca,bj columns in the shape C1
a,bνpbq. Set

Θpbq
j
“ Qpbq
j
´ Qpbq
j´1 and Ξpbq
j
“ Qpbq
j`1 ´ Qpbq
j . We must have Θpbq
j
ě Ξpbq
j
ě 0 since

## Page 12

12
BEN SALISBURY AND TRAVIS SCRIMSHAW

C1
a,bνpbq is a partition. Thus

2Qpbq
j
“ 2Qpbq
j´1 ` 2Θpbq
j

“ Qpbq
j´1 ` Qpbq
j`1.

Since mpaq
i
“ 0, we have Ξpaq
i
“ Θpaq
i
, and so

ě 2Qpbq
j´1 ` Θpbq
j
` Ξpbq
j

“ Qpbq
j´1 ` Qpbq
j
` Ξpbq
j

2Qpaq
i
“ Qpaq
i´1 ` Qpaq
i`1.

Recall Aab ď 0 for all a ‰ b and C_
a,b ą 0. Therefore we have ´C_
a,bAab ě 0 for all
a ‰ b, and hence

´2
ÿ

pb,jqPH
C_
a,bAabQpbq
j
ě ´
ÿ

Similarly we can show that
ÿ

ją0
minpi, jqLpaq
j
ě
ÿ

pb,jqPH
C_
a,bAab
`
Qpbq
j´1 ` Qpbq
j`1
˘

ją0
minpi ´ 1, jqLpaq
j
` minpi ` 1, jqLpaq
j ,

and hence

2ppaq
i
ě ppaq
i´1 ` ppaq
i`1.

We also show the following proposition for generalized types.

Proposition 4.2. Consider a rigged conﬁguration pν, Jq P RCp8q. Fix some a P I
and consider the generalization of the vacancy numbers given in Lemma 4.1 such
that ppaq
8 “ xha, wtpν, Jqy. Let x be the smallest label of pν, Jqpaq and s “ minp0, xq.
Then we have

εapν, Jq “ ´s,
ϕapν, Jq “ ppaq
8 ´ s.

Proof. The proof that ϕapν, Jq “ ppaq
8 ´s follows that given in [38, Lemma 3.6] and
relies on the convexity statement of Lemma 4.1. The statement for εapν, Jq follows
from ppaq
8 “ xha, wtpν, Jqy “ ϕapν, Jq ´ εapν, Jq (or [37, Thm. 3.8]).

Note that the proof of Theorem 2.7 given in [38] is based on the Stembridge
axioms [43] and does not use the condition that the crystal of ﬁnite type. However
it does rely upon Proposition 4.2 for simply-laced types (this is contained in [38]).
Hence the proof holds for arbitrary simply-laced types, and it gives a rigged conﬁgu-
ration model for highest weight modules in arbitrary simply-laced types. Similarly,
the proof of Theorem 3.9 does not use any assumption that the Kac-Moody algebra
be of ﬁnite type, so our result extends to arbitrary simply-laced types.

Theorem 4.3. Let g be of simply-laced type. Then there exists a Uqpgq-crystal
isomorphism Bp8q – RCp8q which sends u8 ÞÑ pνH, JHq.

Example 4.4. Consider the hyperbolic Kac-Moody algebra Hp4q
1
(see [5] for the
notation and list of Dynkin diagrams), whose Dynkin diagram is the complete graph

## Page 13

A RIGGED CONFIGURATION MODEL FOR Bp8q
13

Table 5.1. Well-known embeddings g ãÝÑ pg of aﬃne Kac-Moody

algebras by type as given in [11] pn ‰ 1q.

on four vertices.

2

1

3

4

Then the partitions are enumerated as pνp1q, νp2q, νp3q, νp4qq and

´1
1
0
1

2
4
´1
´1
´2
1
.

f4f 2
2f1f3f 3
4 f2f1pνH, JHq “
2
1
1
1

5. Extending Theorem 3.9 to non-simply-laced Lie algebras

5.1. Virtual crystals. In this section, g denotes an aﬃne Kac-Moody algebra with
classical subalgebra g0. Fix one of the embeddings g ãÝÑ pg from Table 5.1, so that pg
is simply-laced with index set denoted by pI. Let Γ be the Dynkin diagram of g and
pΓ be the Dynkin diagram of pg.1 These embeddings arise from the diagram foldings
φ: pΓ Œ Γ. We also have to deﬁne additional data γ “ pγaqaPI in the following way.
(1) Suppose Γ has a unique arrow. Removing the edge with this unique arrow
leaves two connected components.
(a) Suppose the arrow points towards the component of the special node
0. Then γa “ 1 for all a P I.
(b) Suppose instead the arrow points away from the component of the
special node 0. Then γa is the order of φ for all a in the component of
0 after removing the arrow. For a in the component not containing 0,
set γa “ 1.
(2) If Γ has two arrows, then Γ embeds into the Dynkin diagram of Ap1q
2n´1.
Then γa “ 1 for all 1 ď a ď n ´ 1, and for a P t0, nu, we have γa “ 2 if the
arrow points away from a and γa “ 1 otherwise.

We have two special cases of the above for types Ap1q
1
and Ap2q
2 . For type Ap1q
1 , we
consider the diagram folding of Ap1q
3
given by φ´1p0q “ t0, 2u and φ´1p1q “ t1, 3u
and γ0 “ γ1 “ 1. For type Ap2q
2 , we consider the diagram folding of Dp1q
4
given by
φ´1p0q “ t0, 1, 3, 4u and φ´1p1q “ t2u and γ0 “ 1 and γ1 “ 4.
The embeddings in Table 5.1 yield natural embeddings Ψ: P ÝÑ pP of weight
lattices as
Λa ÞÑ γa
ÿ

bPφ´1paq
pΛb
and
αa ÞÑ γa
ÿ

bPφ´1paq
pαb.

1From now on, if S is an object associated with g, then pS will denote the corresponding object
associated with pg under the appropriate embedding listed above.

## Page 14

14
BEN SALISBURY AND TRAVIS SCRIMSHAW

This implies that Ψpδq “ c0γ0pδ, where δ (resp. pδ) is the minimal positive imaginary
root in P (resp. pP).

Remark 5.1. There is another folding of Dp1q
4
to obtain Ap2q
2
by setting φ´1p0q “
t2u and φ´1p1q “ t0, 1, 3, 4u, but with γ0 “ γ1 “ 1. Since 0 R φ´1p0q, we have
Ψpδq ‰ c0γ0pδ. This implies Ψpδq “ cφp0qγφp0qpδ; i.e., we want the coeﬃcients of pδ
to correspond to the image of 0 under the diagram folding. Alternatively we could
consider this as a folding of Ap2q:
2
, which is the same as the Dynkin diagram of Ap2q
2
but with the labels of nodes interchanged (with 1 as the aﬃne node).

Next we restrict our focus to untwisted types; that is, we only consider

Cp1q
n
ãÝÑ Ap1q
2n´1,
Bp1q
n
ãÝÑ Dp1q
n`1,

F p1q
4
ãÝÑ Ep1q
6 ,
Gp1q
2
ãÝÑ Dp1q
4 .
(5.1)

When restricting to the classical subalgebras from (5.1), we get the embeddings

Cn ãÝÑ A2n´1,
Bn ãÝÑ Dn`1,
F4 ãÝÑ E6,
G2 ãÝÑ D4,
(5.2)

via diagram foldings.
If g0 ãÝÑ pg0 is one of the embeddings from (5.2), then it induces an injection
v: Bpλq ãÝÑ Bppλq as sets, where Ψpλq “ pλ. However, there is additional structure
on the image under v as a virtual crystal, where ea and fa are deﬁned on the image
as
ev
a “
ź

bPφ´1paq
pe γa
b
and
f v
a “
ź

bPφ´1paq
pf γa
b ,
(5.3)

respectively, and they commute with v [1, 33, 34]. These are known as the virtual
Kashiwara (crystal) operators. It is shown in [16] that for any a P I and b, b1 P
φ´1paq we have ebeb1 “ eb1eb and fbfb1 “ fb1fb as operators (recall that b and b1

are not connected), so both ev
a and f v
b are well-deﬁned. The inclusion map v also
satisﬁes the following commutative diagram.

v

Bpλq
Bppλq

wt
x
wt
(5.4)

Ψ

In [1], it was shown that this deﬁnes a Uqpgq-crystal structure on the image of v.
More generally, we deﬁne a virtual crystal as follows.

Deﬁnition 5.2. Consider any symmetrizable types g and pg with index sets I and
pI, respectively. Let φ: pI ÝÑ I be a surjection such that b is not connected to
b1 for all b, b1 P φ´1paq and a P I. Let pB be a Uqppgq-crystal and V Ď pB. Let
γ “ pγa P Zą0 : a P Iq. A virtual crystal is the quadruple pV, pB, φ, γq such that V
has an abstract Uqpgq-crystal structure deﬁned using the Kashiwara operators ev
a
and f v
a from (5.3) above,

εa :“ γ´1
a pεb,
ϕa :“ γ´1
a
pϕb,
for all b P φ´1paq,

and wt :“ Ψ´1 ˝ x
wt.

## Page 15

A RIGGED CONFIGURATION MODEL FOR Bp8q
15

Remark 5.3. The deﬁnition of εa and ϕa forces all of our virtual crystals to be
aligned, as deﬁned in [33, 34].

We say B virtualizes in pB if there exists a Uqpgq-crystal isomorphism v: B ÝÑ
V .
The resulting isomorphism is called the virtualization map.
We denote the
quadruple pV, pB, φ, γq simply by V when there’s no risk of confusion.
The virtualization map v from rigged conﬁgurations of type g0 to rigged conﬁg-
urations of type pg0 is deﬁned by

pmpbq
γai “ mpaq
i
,
pJpbq
γai “ γaJpaq
i
,
(5.5)

for all b P φ´1paq. A Uqpg0q-crystal structure on rigged conﬁgurations is deﬁned
by using virtual crystals [34].
Moreover, we use Equation (5.5) to describe the
virtual image of the type g0 rigged conﬁgurations into type pg0 rigged conﬁgurations.
Explicitly ppν, pJq P V if and only if

(1) pmpbq
i
“ pmpb1q
i
and pJpbq
i
“ pJpb1q
i
for all b, b1 P φ´1paq,
(2) pmpbq
i
P γaZ and pJpbq
i
P γaZ for all b P φ´1paq, and
(3) pmpbq
i
“ 0 and pJpbq
i
“ 0 for all j R γaZ for all b P φ´1paq.

Example 5.4. Consider the rigged conﬁguration in type C2

1
1
´1
´1
´1
´1

with Lp1q
1
“ Lp2q
1
“ 1, all other Lpaq
i
“ 0, and weight Λ1 ´ Λ2. The corresponding
virtual rigged conﬁguration in type A3 is

1
1
´2
´2
´2
´2

1
1

with Lp1q
1
“ Lp3q
1
“ Lp2q
2
“ 1, all other Lpaq
i
“ 0, and weight Λ1 ` Λ3 ´ 2Λ2.

Remark 5.5. There exist rigged conﬁgurations for Uqpg0q-crystals when g is of
twisted aﬃne type by considering U 1
qpgq crystals; however, we omit those here in
order to avoid confusion as we will be considering rigged conﬁgurations for Uqpgq-
crystals in the sequel. In particular, for type Ap2q:
2n , the riggings of νpnq are in 1

2Z.
See [34] for more information.

We note that it is suﬃcient to consider single tensor factors by the following
proposition.

Proposition 5.6 ([33, Prop. 6.4]). Virtual crystals form a tensor category.

Although [33] is concerned with U 1
qpgq-crystals, the proof of Proposition 5.6 does
not use the U 1
qpgq-crystals condition, but instead is a statement about the tensor
product rule. It has been cited as above in other papers; e.g., Proposition 3.3 of [34].

5.2. Extending Theorem 3.9 to all ﬁnite types. In this section we assume g
is of non-simply-laced ﬁnite type. For the vacancy numbers, we just consider this
as the classical subcrystal in the corresponding untwisted aﬃne type. Again, let
RCp8q be the set generated by pνH, JHq and ea, fa for a P I, where ea and fa are
deﬁned as in Section 3.
Proposition 5.7 and Theorem 5.8 below are proven in [39] for all ﬁnite types. We
will require these results in the sequel.

## Page 16

16
BEN SALISBURY AND TRAVIS SCRIMSHAW

Proposition 5.7. The crystal RCpλq virtualizes in RCppλq.

Theorem 5.8. Let g be of ﬁnite type. We have RCpλq – Bpλq.

Remark 5.9. Note the proof of Theorem 5.8 uses the fact that Bpλq virtualizes
in Bppλq in ﬁnite types [1, 33, 34].

By combining the virtualization results above with the method of proof given for
Theorem 3.9, we may extend Theorem 3.9 to include non-simply-laced ﬁnite types.

Theorem 5.10. Let g be of any ﬁnite type.
Then there exists a Uqpgq-crystal
isomorphism RCp8q – Bp8q such that pνH, JHq ÞÑ u8.

Proof. The proof of Theorem 3.9 holds here by following Section 3 and using The-
orem 5.8 in place of Theorem 2.7.

We also have the virtualization of Bp8q crystals.

Proposition 5.11. Let g be of any ﬁnite type. The Uqpgq-crystal Bp8q virtualizes
in the Uqppgq-crystal pBp8q.

Proof. This follows immediately from the fact that the diagram

Iλ`µ,µ

T´λ b Bpλq
T´λ´µ b Bpλ ` µq

T´pλ b Bppλq
T´pλ´pµ b Bppλ ` pµq

Ipλ` pµ, pµ
commutes.

5.3. Recognition Theorem. From the above, we see that we only need to know
the factors pγaqaPI in order to show that we get a virtualization of the Uqpgq-crystal
of rigged conﬁgurations into a Uqppgq-crystal by Equation (5.5). Thus we make the
following conjecture.

Conjecture 5.12. Let g be obtained via a diagram folding φ of a simply-laced type
pg. There exists pγaqaPI such that RCpλq virtualizes in RCppλq by Equation 5.5.

We have this for all ﬁnite and aﬃne types using the foldings given in Table 5.1.
We can also show this for all rank 2 with Cartan matrix
ˆ
2
x
y
2

˙

by considering a diagram folding of Kx,y, the complete bipartite graph on x and y
nodes, with γ1 “ γ2 “ 1. In such foldings, it is easy to see that Conjecture 5.12
holds from Equation (2.2). In fact, we believe there exists a pg such that γa “ 1 for
all a P I, and we call such a folding natural.
In their development of the geometric construction of the crystal basis, Kashi-
wara and Saito [19] established a recognition theorem for the crystal Bp8q valid for
all symmetrizable Kac-Moody types. In this section, we will recall the recognition
theorem with appropriate deﬁnitions and extend Theorem 3.9 to all Kac-Moody
algebras satisfying Conjecture 5.12 using the recognition theorem.

## Page 17

A RIGGED CONFIGURATION MODEL FOR Bp8q
17

Remark 5.13. A straightforward check shows that Proposition 5.7 holds in our
aﬃne setting, which requires Lemma 4.1, and so Conjecture 5.12 is true in aﬃne
types.

Remark 5.14. A priori, we do not have that RCpλq – Bpλq for arbitrary sym-
metrizable types, as there is no equivalent version of Table 5.1 which would give
the analogous statement to Theorem 5.8. Therefore we must change our techniques
to show that the crystal RCp8q – Bp8q by using the Bp8q recognition theorem
given in [19]. Nevertheless, we will be able to show that those RCpλq carved out of
RCp8q are isomorphic to Bpλq in Section 6.

From this viewpoint, it would be natural to restrict our attention for aﬃne
foldings from Table 5.1 given by

Dp2q
n`1 ãÝÑ Ap1q
2n´1,
Ap2q
2n´1 ãÝÑ Dp1q
n`1,

Ep2q
6
ãÝÑ Ep1q
6 ,
Dp3q
4
ãÝÑ Dp1q
4 ,
(5.6)

as these foldings satisfy γa “ 1 for all a P I. The corresponding classical foldings
from (5.2) are given by

Bn ãÝÑ A2n´1,
Cn ãÝÑ Dn`1,
F4 ãÝÑ E6,
G2 ãÝÑ D4.
(5.7)

We should also note that we can get natural foldings of the other (non-degenerate)
aﬃne types by

Bp1q
n , Ap2q
2n ãÝÑ Dp1q
2n`1
Cp1q
n
ãÝÑ Dp1q
n`1

As in Remark 5.1, we have Ψpδq “ cφp0qγφp0qpδ.

Deﬁnition 5.15. Let g be a symmetrizable Kac-Moody algebra and ﬁx a P I.
Deﬁne Zpaq “ tzapmq : m P Zu with the abstract Uqpgq-crystal structure given by

wt
`
zapmq
˘
“ mαa,
ϕa
`
zapmq
˘
“ m,
εa
`
zapmq
˘
“ ´m,

ϕb
`
zapmq
˘
“ εb
`
zapmq
˘
“ ´8 for a ‰ b,

eazapmq “ zapm ` 1q,
fazapmq “ zapm ´ 1q,

ebzapmq “ fbzapmq “ 0 for a ‰ b.

The crystal Zpaq is called an elementary crystal.

Remark 5.16. The crystal Zpaq was originally denoted by Bi in [15].

We must ﬁrst prove a technical lemma about the virtual elementary crystals.

Lemma 5.17. Let g be a Kac-Moody algebra satisfying Conjecture 5.12. Let φ be
the diagram folding with scaling factors pγaqaPI. Fix some a P I. The elementary
crystal Zpaq virtualizes in pZpaq “ Â
bPφ´1paq Zpbq (for any order of the factors) with
the virtualization map vpaq deﬁned by

zapmq ÞÑ
â

bPφ´1paq
zbpγamq.

Proof. If pZpaq “ Zpbq where tbu “ φ´1paq, then it is easy to see the claim is true
from Deﬁnition 5.15.

## Page 18

18
BEN SALISBURY AND TRAVIS SCRIMSHAW

Now we assume pZpaq “ Zpb2q b Zpb1q where tb1, b2u “ φ´1paq and b1 ‰ b2. If
b R φ´1paq, then

εb
`
zb2pγamq b zb1pγamq
˘
“ maxp´8, ´8 ´ xhb, γamαb2yq “ ´8.

If b “ b2, then we have

εb
`
zb2pγamq b zb1pγamq
˘
“ maxp´γam, ´8 ´ xhb, γamαb2yq

“ ´γam

“ γaεa
`
zapmq
˘

since ´8 ` k “ ´8 for any ﬁnite number k. If b “ b1, then we have

εb
`
zb2pγamq b zb1pγamq
˘
“ maxp´8, ´γam ´ xhb, γamαb2yq
“ ´γam

“ γaεa
`
zapmq
˘

since b1 ‰ b2. Similar statements hold for ϕb
`
zb2pγamq b zb1pγamq
˘
. From the
tensor product rule,

$
’
&

eb
`
zb2pγamq b zb1pγamq
˘
“

’
%

$
’
&

“

’
%

and

$
’
&

fb
`
zb2pγamq b zb1pγamq
˘
“

’
%

$
’
&

“

’
%

Thus we have

zb2pγamq b eb
`
zb1pγamq
˘
if b “ b1,
eb
`
zb2pγamq
˘
b zb1pγamq
if b “ b2,
0
otherwise,

zb2pγamq b zb1
`
γapm ` 1q
˘
if b “ b1,
zb2
`
γapm ` 1q
˘
b zb1pγamq
if b “ b2,
0
otherwise,

zb2pγamq b fb
`
zb1pγamq
˘
if b “ b1,
fb
`
zb2pγamq
˘
b zb1pγamq
if b “ b2,
0
otherwise,

zb2pγamq b zb1
`
γapm ´ 1q
˘
if b “ b1,
zb2
`
γapm ´ 1q
˘
b zb1pγamq
if b “ b2,
0
otherwise.

pev
a ˝ vq
`
zapmq
˘
“ eγa
b1 eγa
b2
`
zb2pγamq b zb1pγamq
˘

“ zb2
`
γapm ` 1q
˘
b zb1
`
γapm ` 1q
˘

“ v
`
zapm ` 1q
˘

“ v
`
eazapmq
˘
,

and ppea1 ˝ vq
`
zapmq
˘
“ 0 “ v
`
ea1zapmq
˘
for a1 ‰ a. Similar statements can be
shown for fa and fa1 for a1 ‰ a. Lastly

wt
`
zb2pγamq b zb1pγamq
˘
“ γampαb2 ` αb1q “ x
wtpzapmqq.

Therefore Zpaq virtualizes in Zpb2q b Zpb1q with virtualization map v. It is clear
that it is independent of the ordering. Moreover, we may generalize to the case of
ﬁnitely many tensor factors using induction and associativity of the tensor product
with a similar argument as above.

## Page 19

A RIGGED CONFIGURATION MODEL FOR Bp8q
19

Theorem 5.18 (Recognition Theorem [19, Prop. 3.2.3]). Let g be a symmetrizable
Kac-Moody algebra, B be an abstract Uqpgq-crystal, and x0 be an element of B with
weight zero. Assume the following conditions.

(1) wtpBq Ă Q´.
(2) x0 is the unique element of B with weight zero.
(3) εapx0q “ 0 for all a P I.
(4) εapxq P Z for all x P B and a P I.
(5) For every a P I, there exists a strict crystal embedding Ψa : B ÝÑ Zpaq bB.
(6) ΨapBq Ă tf m
a zap0q : m ě 0u ˆ B.
(7) For any x P B such that x ‰ x0, there exists a P I such that Ψapxq “
f m
a zap0q b x1 with m ą 0 and x1 P B.

Then B is isomorphic to Bp8q.

Lemma 5.19. Assume g satisﬁes Conjecture 5.12.
Then the crystal RCpλq is
generated by pνH, JHq and fa for all a P I.

Proof. By assumption, RCpλq virtualizes in RCppλq.
Since RCppλq – Bppλq and
Bppλq is generated by its highest weight vector and pfa for all a P pI, the statement
follows.

Theorem 5.20. Let g be a Kac-Moody algebra satisfying Conjecture 5.12. Then
RCp8q – Bp8q as Uqpgq-crystals.

Proof. Let x
RCp8q denote the rigged conﬁguration realization of the crystal pBp8q
corresponding to the simply-laced Kac-Moody algebra pg coming from Theorem 4.3,
so that
x
RCp8q “ lim
ÝÑ
λPP `

From Conjecture 5.12, we have

RCp8q “ lim
ÝÑ
λPP `

`
T´λ b RCppλq
˘
.

`
T´λ b RCpλq
˘
,

for reasons similar to the justiﬁcation of Theorem 5.10. Hence RCp8q virtualizes
in x
RCp8q as in Proposition 5.11.
It remains to show that RCp8q – Bp8q as
Uqpgq-crystals.
We note that (1) and (2) are satisﬁed from Equation (3.1c) where x0 “ pνH, JHq.
Condition (3) is satisﬁed directly by the deﬁnition of pνH, JHq, while (4) follows
from the deﬁnition of εa on RCp8q. The remaining properties require virtualization.
Let vpaq denote the virtualization map from Lemma 5.17. Now for each a P I,
deﬁne a crystal morphism Ψa : RCp8q ÝÑ Zpaq b RCp8q in the following way.
Consider the following commutative diagram.

v

RCp8q
x
RCp8q

Ψa
pΨa

Zpaq b RCp8q
pZpaq b x
RCp8q

vpaq b v

## Page 20

20
BEN SALISBURY AND TRAVIS SCRIMSHAW

Since both rows are virtualization maps by Proposition 5.6 and map on the right
side is a strict embedding because x
RCp8q – pBp8q by Theorem 4.3, we get a well-
deﬁned strict embedding Ψa “ pvpaq b vq´1 ˝ pΨa ˝ v for every a P I.
For (6), notice the crystal RCp8q is generated from pνH, JHq and fa, for a P I,
from the direct limit characterization of RCp8q and Lemma 5.19. That is to say,
we can write an arbitrary element pν, Jq of RCp8q as pν, Jq “ fak ¨ ¨ ¨ fa1pνH, JHq
where aj P I. Since Ψa is strict and f k
a is a nonzero operator on both Zpaq and
RCp8q for all a P I and k ě 0, we have Ψa
`
RCp8q
˘
Ă tf m
a zap0q : m ě 0uˆRCp8q.
Finally, set pν, Jq “ fak ¨ ¨ ¨ fa1pνH, JHq to be an arbitrary element of RCp8q
and take a “ a1. Note that ϕapνH, JHq “ 0 by Equation (3.1b). Then by the
tensor product rule for crystals, we have Ψa
`
fapνH, JHq
˘
“ fazap0q b pνH, JHq
because ΨapνH, JHq “ zap0q b pνH, JHq. Therefore there exists some subsequence
paj1, . . . , ajk´mq of pa1, . . . , akq such that a1 “ at, for all t ‰ j1, . . . , jk´m, and
Ψapν, Jq “ f m
a zap0q b fajt ¨ ¨ ¨ faj1pνH, JHq with m ą 0. This shows condition (7),
and we have RCp8q – Bp8q by Theorem 5.18.

Open Problem 5.21. It would be interesting to ﬁnd a proof which does not
appeal to virtualization in order to prove (5), (6), and (7); in particular, to show
that RCp8q is generated only by pνH, JHq and fa, for all a P I, without appealing
to virtualization.

6. Projecting from RCp8q to RCpλq

The goal of this section is to show that taking valid rigged conﬁgurations is
equivalent to projecting to highest weight Uqpgq-crystals, where g is any symmetriz-
able Kac-Moody type satisfying Conjecture 5.12. Recall the one-element crystal
Tλ “ ttλu given in Deﬁnition 3.4. Let C “ tcu be the one-element crystal with
crystal operations deﬁned by

wtpcq “ 0,
ϕapcq “ εapcq “ 0,
fapcq “ eapcq “ 0,
a P I.

It is known that the connected component in CbTλbBp8q generated by cbtλbu8
is isomorphic to Bpλq. In the setting of rigged conﬁgurations, recall that to pass
from RCp8q to RCpλq, we raise the weight by λ (equivalently we shift the vacancy
numbers), which corresponds to tensoring with Tλ. Next we take only valid rigged
conﬁgurations, and we will show that this restriction corresponds to tensoring with
the crystal C.
Let RCλp8q “ TλbRCp8q denote the crystal associated with the Verma module
with highest weight λ. Strictly speaking,

RCλp8q “
␣
fak ¨ ¨ ¨ fa1
`
tλ b pνH, JHq
˘
: a1, . . . , ak P I, k ě 0
(
,

but by an abuse of notation, we will consider RCλp8q as the set of all rigged
conﬁgurations generated by fa pa P Iq from pνH, JHq where the vacancy numbers
and the weights are shifted by λ. That is, if λ “ ř
pa,iqPH iLpaq
i
Λa is a dominant
integral weight of type g, then for all i P Zě0 we have

ppaq
i
pνλq “
ÿ

jě0
minpi, jqLpaq
j
` ppaq
i
pνq,
wtpνλ, Jλq “ wtpν, Jq ` λ,

where pνλ, Jλq P RCλp8q corresponds to pν, Jq P RCp8q.

## Page 21

A RIGGED CONFIGURATION MODEL FOR Bp8q
21

Theorem 6.1. Let CH denote the connected component of C b RCλp8q generated
by c b pνH, JHq. The map Ψ: CH ÝÑ RCpλq sending c b pνλ, Jλq ÞÑ pνλ, Jλq is a
Uqpgq-crystal isomorphism.

Proof. Let pνλ, Jλq P RCλp8q and a P I. First,

wt
`
c b pνλ, Jλq
˘
“ wtpcq ` wtpνλ, Jλq “ wtpνλ, Jλq,

so Ψ preserves weights. Then,

εa
`
c b pνλ, Jλq
˘
“ max
␣
0, εapνλ, Jλq
(
“ εapνλ, Jλq,

since εapνλ, Jλq ě 0, which implies that Ψ preserves εa. From the εa
`
c b pνλ, Jλq
˘

computation above, we have

ϕa
`
c b pνλ, Jλq
˘
“ max
␣
ϕapνλ, Jλq, xha, wtpνλ, Jλqy
(

“ max
␣
εapνλ, Jλq ` xha, wtpνλ, Jλqy, xha, wtpνλ, Jλqy
(

“ εapνλ, Jλq ` xha, wtpνλ, Jλqy

“ ϕapνλ, Jλq.

We have ϕapνλ, Jλq “ 0 if and only if fapνλ, Jλq “ 0 in RCpλq because RCpλq is a
(lower) regular crystal. Also if ϕapνλ, Jλq “ 0, we have

fa
`
c b pνλ, Jλq
˘
“ pfacq b pνλ, Jλq “ 0

by the tensor product rule. Similarly if ϕapνλ, Jλq ą 0, then

fa
`
c b pνλ, Jλq
˘
“ c b fapνλ, Jλq.

So Ψ ˝ fa “ fa ˝ Ψ. Recall that ϕa
`
c b pνλ, Jλq
˘
“ ϕapνλ, Jλq ě 0; so it follows, by
the tensor product rule, that

Ψ
`
ea
`
c b pνλ, Jλq
˘˘
“ Ψ
`
c b eapνλ, Jλq
˘
“ eapνλ, Jλq “ eaΨ
`
c b pνλ, Jλq
˘
.

This completes the proof that Ψ is a crystal isomorphism.

Thus, the projection map above corresponds to eliminating those rigged conﬁgu-
rations which are not valid; that is, Ψpcbpν, Jqq “ 0 if pν, Jq is not valid. Therefore
Theorem 5.20 implies the following.

Corollary 6.2. Suppose Conjecture 5.12 holds, then we have RCpλq – Bpλq.

Corollary 6.3. Suppose Conjecture 5.12 holds, then the Uqpgq-crystal Bpλq virtu-
alizes in the Uqppgq-crystal Bppλq.

We also note that Proposition 4.2 extends to both RCp8q and RCpλq.

Example 6.4. Consider RCpΛ0q with g “ Ap1q
2 . The top of the crystal graph is
shown in Figure 6.1.

Appendix A. Calculations using Sage

We begin by setting up the Sage environment to give a more concise printing.

We construct our the rigged conﬁguration from Example 2.4 (in the U 1
qpgq set-
ting).

## Page 22

22
BEN SALISBURY AND TRAVIS SCRIMSHAW

H
H
H

´1

´1

1

´1

´2

0

0

Figure 6.1. The top of the crystal RCpΛ0q in type Ap1q
2 , created
using Sage.

Alternatively, one could construct pν, Jq from Example 2.4 directly by specifying
the partitions and corresponding labels.

The crystal RCp8q and RCpλq has been implemented by the second author in
Sage. We conclude with examples.

## Page 23

A RIGGED CONFIGURATION MODEL FOR Bp8q
23

Example A.1. Let g0 “ D5.

Example A.2. Let g0 “ E7.

Example A.3. Let g “ Hp4q
1 .

Example A.4. Consider RCpΛ0q with g “ Ap1q
2 .
The followings generates the
crystal graph in Figure 6.1:

## Page 24

24
BEN SALISBURY AND TRAVIS SCRIMSHAW

Acknowledgements

We would like to thank Anne Schilling for very valuable discussions and for
reading a draft of this manuscript. We would also like to thank Sara Billey, Ben
Brubaker, Dan Bump, Gautam Chinta, Sol Friedberg, Dorian Goldfeld, JeﬀHoﬀ-
stein, Anne Schilling, and Nicolas Thi´ery for organizing the ICERM semester pro-
gram entitled “Automorphic Forms, Combinatorial Representation Theory, and
Multiple Dirichlet series,” where the idea for this project originated. This work
was also aided by Sage Mathematical Software [36, 42], in which the second named
author designed packages corresponding to the work in this paper. Finally, the au-
thors would like to thank the anonymous referees for there helpful comments and
insight.

References

[1] Timothy H. Baker, Zero actions and energy functions for perfect crystals, Publ. Res. Inst.
Math. Sci. 36 (2000), no. 4, 533–572.
[2] Rodney J. Baxter, Exactly solved models in statistical mechanics, Academic Press Inc. [Har-
court Brace Jovanovich Publishers], London, 1989, Reprint of the 1982 original.
[3] H. Bethe, Zur Theorie der Metalle, Zeitschrift f¨ur Physik 71 (1931), no. 3-4, 205–226 (Ger-
man).
[4] Alexander Braverman and Dennis Gaitsgory, Crystals via the aﬃne Grassmannian, Duke
Math. J. 107 (2001), no. 3, 561–575.
[5] Lisa Carbone, Sjuvon Chung, Leigh Cobbs, Robert McRae, Debajyoti Nandi, Yusra Naqvi,
and Diego Penta, Classiﬁcation of hyperbolic Dynkin diagrams, root lengths and Weyl group
orbits, J. Phys. A 43 (2010), no. 15, 155209, 30.
[6] Lipika Deka and Anne Schilling, New fermionic formula for unrestricted Kostka polynomials,
J. Combin. Theory Ser. A 113 (2006), no. 7, 1435–1461.
[7] S. Gaussent and P. Littelmann, LS galleries, the path model, and MV cycles, Duke Math. J.
127 (2005), no. 1, 35–88.
[8] Goro Hatayama, Anatol N. Kirillov, Atsuo Kuniba, Masato Okado, Taichiro Takagi, and
Yasuhiko Yamada, Character formulae of psln-modules and inhomogeneous paths, Nuclear
Phys. B 536 (1999), no. 3, 575–616.
[9] Goro Hatayama, Atsuo Kuniba, Masato Okado, Taichiro Takagi, and Zengo Tsuboi, Paths,
crystals and fermionic formulae, MathPhys odyssey, 2001, Prog. Math. Phys., vol. 23,
Birkh¨auser Boston, Boston, MA, 2002, pp. 205–272.
[10] Jin Hong and Seok-Jin Kang, Introduction to quantum groups and crystal bases, Graduate
Studies in Mathematics, vol. 42, American Mathematical Society, Providence, RI, 2002.
[11] Michio Jimbo and Tetsuji Miwa, On a duality of branching rules for aﬃne Lie algebras,
Algebraic groups and related topics (Kyoto/Nagoya, 1983), Adv. Stud. Pure Math., vol. 6,
North-Holland, Amsterdam, 1985, pp. 17–65.
[12] Seok-Jin Kang and Kailash C. Misra, Crystal bases and tensor product decompositions of
UqpG2q-modules, J. Algebra 163 (1994), no. 3, 675–691.

## Page 25

A RIGGED CONFIGURATION MODEL FOR Bp8q
25

[13] Masaki Kashiwara, Crystallizing the q-analogue of universal enveloping algebras, Comm.
Math. Phys. 133 (1990), no. 2, 249–260.
[14]

, On crystal bases of the q-analogue of universal enveloping algebras, Duke Math. J.
63 (1991), no. 2, 465–516.
[15]

, The crystal base and Littelmann’s reﬁned Demazure character formula, Duke Math.
J. 71 (1993), no. 3, 839–858.
[16]

, Similarity of crystal bases, Lie algebras and their representations (Seoul, 1995),
Contemp. Math., vol. 194, Amer. Math. Soc., Providence, RI, 1996, pp. 177–186.
[17]

, Bases cristallines des groupes quantiques, Cours Sp´ecialis´es [Specialized Courses],
vol. 9, Soci´et´e Math´ematique de France, Paris, 2002, Edited by Charles Cochet.
[18] Masaki Kashiwara and Toshiki Nakashima, Crystal graphs for representations of the q-
analogue of classical Lie algebras, J. Algebra 165 (1994), no. 2, 295–345.
[19] Masaki Kashiwara and Yoshihisa Saito, Geometric construction of crystal bases, Duke Math.
J. 89 (1997), no. 1, 9–36.
[20] S. V. Kerov, A. N. Kirillov, and N. Yu. Reshetikhin, Combinatorics, the Bethe ansatz and
representations of the symmetric group, Zap. Nauchn. Sem. Leningrad. Otdel. Mat. Inst.
Steklov. (LOMI) 155 (1986), no. Diﬀerentsialnaya Geometriya, Gruppy Li i Mekh. VIII,
50–64, 193.
[21] Jeong-Ah Kim and Dong-Uy Shin, Generalized Young walls and crystal bases for quantum
aﬃne algebra of type A, Proc. Amer. Math. Soc. 138 (2010), no. 11, 3877–3889.
[22]

, Zigzag strip bundles and crystals, J. Combin. Theory Ser. A 120 (2013), no. 5,
1087–1115.
[23] A. N. Kirillov and N. Yu. Reshetikhin, The Bethe ansatz and the combinatorics of Young
tableaux, Zap. Nauchn. Sem. Leningrad. Otdel. Mat. Inst. Steklov. (LOMI) 155 (1986),
no. Diﬀerentsialnaya Geometriya, Gruppy Li i Mekh. VIII, 65–115, 194.
[24] Cristian Lenart and Alexander Postnikov, Aﬃne Weyl groups in K-theory and representation
theory, Int. Math. Res. Not. IMRN (2007), no. 12, Art. ID rnm038, 65.
[25]

, A combinatorial model for crystals of Kac-Moody algebras, Trans. Amer. Math. Soc.
360 (2008), no. 8, 4349–4381.
[26] Peter Littelmann, A Littlewood-Richardson rule for symmetrizable Kac-Moody algebras, In-
vent. Math. 116 (1994), no. 1-3, 329–346.
[27]

, The path model for representations of symmetrizable Kac-Moody algebras, Pro-
ceedings of the International Congress of Mathematicians, Vol. 1, 2 (Z¨urich, 1994) (Basel),
Birkh¨auser, 1995, pp. 298–308.
[28]

, Paths and root operators in representation theory, Ann. of Math. (2) 142 (1995),
no. 3, 499–525.
[29]

, Characters of representations and paths in H˚
R, Representation theory and auto-
morphic forms (Edinburgh, 1996), Proc. Sympos. Pure Math., vol. 61, Amer. Math. Soc.,
Providence, RI, 1997, pp. 29–49.
[30] Atsushi Nakayashiki and Yasuhiko Yamada, Kostka polynomials and energy functions in
solvable lattice models, Selecta Math. (N.S.) 3 (1997), no. 4, 547–599.
[31] Masato Okado, Reiho Sakamoto, and Anne Schilling, Aﬃne crystal structure on rigged con-
ﬁgurations of type Dp1q
n , J. Algebraic Combin. 37 (2013), no. 3, 571–599.
[32] Masato Okado, Anne Schilling, and Mark Shimozono, A crystal to rigged conﬁguration bijec-
tion for nonexceptional aﬃne algebras, Algebraic combinatorics and quantum groups, World
Sci. Publ., River Edge, NJ, 2003, pp. 85–124.
[33]

, Virtual crystals and fermionic formulas of type Dp2q
n`1, Ap2q
2n , and Cp1q
n , Represent.
Theory 7 (2003), 101–163 (electronic).
[34]

, Virtual crystals and Kleber’s algorithm, Comm. Math. Phys. 238 (2003), no. 1-2,
187–209.
[35] Arun Ram, Alcove walks, Hecke algebras, spherical functions, crystals and column strict
tableaux, Pure Appl. Math. Q. 2 (2006), no. 4, part 2, 963–1013.
[36] The Sage-Combinat community, Sage-Combinat: enhancing Sage as a toolbox for computer
exploration in algebraic combinatorics, 2008, http://combinat.sagemath.org.
[37] Reiho Sakamoto, Rigged conﬁgurations and Kashiwara operators, SIGMA Symmetry Inte-
grability Geom. Methods Appl. 10 (2014), Paper 028, 88.
[38] Anne Schilling, Crystal structure on rigged conﬁgurations, Int. Math. Res. Not. (2006), Art.
ID 97376, 27.

## Page 26

26
BEN SALISBURY AND TRAVIS SCRIMSHAW

[39] Anne Schilling and Travis Scrimshaw, Crystal structure on rigged conﬁgurations and the
ﬁlling map, Preprint, http://arxiv.org/abs/1409.2920, 2014.
[40] Anne Schilling and Qiang Wang, Promotion operator on rigged conﬁgurations of type A,
Electron. J. Combin. 17 (2010), no. 1, Research Paper 24, 43.
[41] Anne Schilling and S. Ole Warnaar, Inhomogeneous lattice paths, generalized Kostka polyno-
mials and An´1 supernomials, Comm. Math. Phys. 202 (1999), no. 2, 359–401.
[42] W. A. Stein et al., Sage Mathematics Software (Version 6.2), The Sage Development Team,
2014, http://www.sagemath.org.
[43] John R. Stembridge, A local characterization of simply-laced crystals, Trans. Amer. Math.
Soc. 355 (2003), no. 12, 4807–4823 (electronic).

Department of Mathematics, Central Michigan University, Mt. Pleasant, MI 48859
E-mail address: ben.salisbury@cmich.edu
URL: http://people.cst.cmich.edu/salis1bt/

Department of Mathematics, University of California, Davis, CA 95616
E-mail address: tscrim@ucdavis.edu
URL: https://www.math.ucdavis.edu/~scrimsha/
