# Correctness Audit - 2026-04-16

Scope: factual accuracy, mathematics, conceptual framing, and resource-estimate sanity across the manuscript.

No manuscript text was edited. This note only records issues.

## Overall verdict

The manuscript is mostly sound at the big-picture level. The core application-first framing works, and most chapters are conceptually aligned with the literature. The problems are local but important: several Shor/QPE details are mathematically wrong, the finance unit currently describes the wrong quantity for option pricing, two operator statements in the VQE deep dive are incorrect, and some resource estimates are internally inconsistent.

I would treat the high-severity findings below as pre-publication fixes. The medium-severity findings are mostly overstatements, variable-mismatch issues, or places where a technically literate reader will feel the prose has outrun the math.

## High-severity findings

1. `manuscript/09-finance.md:51-52`, `manuscript/09-finance.md:82`, `manuscript/10-amplitude-estimation.md:52`
   The finance pair currently conflates an exceedance probability with an expected payoff. Marking states where the payoff exceeds a threshold and estimating

   $$\Pr[\text{payoff} > \text{threshold}]$$

   does not price a European call option with payoff

   $$\max(S_T - K, 0).$$

   It prices a digital-or-threshold event. Standard amplitude-estimation finance constructions encode a bounded payoff into an ancilla amplitude, e.g.

   $$\sum_x \sqrt{p_x}|x\rangle\left(\sqrt{1-f(x)}|0\rangle + \sqrt{f(x)}|1\rangle\right),$$

   then estimate

   $$\mathbb{E}[f(X)].$$

   Fix either by re-framing the worked example as a digital option / exceedance-probability problem, or by explaining the usual payoff-encoding construction for a vanilla call.

2. `manuscript/03-cryptography.md:118-122`
   The periodic superposition after measuring the output register is normalised incorrectly. The text says

   $$\frac{1}{\sqrt{r}} \sum_{j=0}^{r-1} |x_0 + jr\rangle,$$

   but the number of terms is not generally $r$. If the first register has size $Q = 2^n$, the post-measurement state is a superposition over all values congruent to $x_0 \pmod r$ that still lie in $\{0,\dots,Q-1\}$, i.e.

   $$\frac{1}{\sqrt{M}} \sum_{j=0}^{M-1} |x_0 + jr\rangle,$$

   where $M \approx Q/r$ and depends on $x_0$. This is a real mathematical error, not just a pedagogical simplification.

3. `manuscript/04-inside-shors.md:104`, `manuscript/04-inside-shors.md:302`
   The deep dive over-generalises the Deutsch-Jozsa phase-kickback story into the standard period-finding circuit. In standard Shor period-finding, the output register is not a "catalyst" that returns to its starting state and leaves all information purely in the phase of the input register. The modular-exponentiation register is generally entangled with the input register until it is measured or traced out. The "catalyst" description is correct for the single-bit $| - \rangle$ kickback trick, but not for the usual modular-exponentiation oracle used in Shor.

4. `manuscript/06-vqe-pipeline.md:81`
   The raising-operator description is wrong. The text says $\frac{1}{2}(X_i - iY_i)$ "flips $|0\rangle$ to $|1\rangle$ while leaving $|1\rangle$ unchanged." On a single qubit,

   $$\sigma^+ = \frac{X - iY}{2}$$

   satisfies

   $$\sigma^+ |0\rangle = |1\rangle, \qquad \sigma^+ |1\rangle = 0.$$

   It annihilates $|1\rangle$; it does not leave it unchanged.

5. `manuscript/06-vqe-pipeline.md:132-136`
   The basis-change identity for measuring $Y$ is wrong. The text says to apply $S^\dagger H$ and then states

   $$S^\dagger H \cdot Y \cdot H S = Z.$$

   That identity is not correct. If you apply $S^\dagger$ then $H$ before measurement, the measurement unitary is $U = H S^\dagger$, and the relevant relation is

   $$U^\dagger Z U = Y,$$

   i.e.

   $$S H Z H S^\dagger = Y,$$

   or equivalently

   $$H S^\dagger Y S H = Z.$$

   The current order is reversed.

6. `manuscript/13-materials-science.md:96-104`
   The 2-site Hubbard worked example is described as showing a "Mott insulator transition." A 2-site Hubbard dimer does not exhibit a genuine Mott phase transition. It shows a finite-size crossover from delocalised to localised behaviour as $U/t$ increases. Calling it a transition is physically inaccurate, and saying the transition is visible in the ground-state energy curve overstates what a 2-site example can demonstrate.

7. `manuscript/14-qpe-trotter.md:104-118` versus `manuscript/13-materials-science.md:78-91`
   The resource estimates are internally inconsistent by orders of magnitude. Unit 7 gives Babbush-style numbers such as an $8 \times 8$ lattice needing about 400 logical qubits and $10^{11}$ T-gates. Deep-Dive 7 then says a $10 \times 10$ lattice needs roughly $10^7$ gates on about 200 qubits. Those claims cannot both be right in the same resource model. Even as a back-of-the-envelope estimate, the deep-dive number is far too small relative to the surrounding chapter. This section should either be aligned with the cited literature or explicitly labelled as a toy scaling estimate rather than a practical resource estimate.

8. `manuscript/15-climate-energy.md:50`, `manuscript/15-climate-energy.md:64`, `manuscript/16-quantum-embedding.md:31`
   The active-space resource accounting is inconsistent. Unit 8 says "6 metal d-orbitals and 10 ligand orbitals: 16 active orbitals" and then claims this becomes "~12-16 qubits" after encoding and tapering. But Deep-Dive 8 uses the chemistry convention where active orbitals are spatial orbitals, and explicitly says 10-14 active orbitals become 20-28 qubits after Jordan-Wigner. Those two conventions are incompatible as written. If 16 means spatial orbitals, the qubit count before tapering is about 32, not 12-16. If 16 means spin-orbitals, the terminology needs to be made consistent everywhere.

## Medium-severity findings

1. `manuscript/03-cryptography.md:22`, `manuscript/03-cryptography.md:201`, `manuscript/03-cryptography.md:209`
   The cryptography chapter mixes logical-qubit and physical-qubit resource counts in the same comparison, then later understates qubit requirements for large instances. Saying ECC needs ~2,330 logical qubits while RSA-2048 needs ~20 million noisy physical qubits is apples-to-oranges. Likewise, saying a 2,000-digit factoring instance needs roughly 4,000 logical qubits is too small given the chapter's own register description; for a 2,000-digit modulus, the control register alone is already on the order of $2n$ bits, with $n \approx 6{,}600$ bits.

2. `manuscript/03-cryptography.md:180-189`
   The worked-example post-processing count is wrong. The table shows outcomes $\{0,4,8,12\}$, with only $4$ and $12$ directly reconstructing denominator 4 via continued fractions. The text then says "Three out of four outcomes give us $r=4$ (or a multiple)." But $8/16 = 1/2$ gives denominator 2, which is a divisor, not a multiple, and not the order itself. The text should say two of the four outcomes directly return denominator 4, while another may still be useful and zero gives no information.

3. `manuscript/03-cryptography.md:46-48`
   The GNFS asymptotic is written with a constant/variable pairing that does not match the usual form. The standard expression is in terms of $\ln N$ and $\ln\ln N$:

   $$\exp\!\left((64/9)^{1/3}(\ln N)^{1/3}(\ln\ln N)^{2/3}\right).$$

   If the text wants to use $n$ as the bit-length, the constant should change accordingly. As written, the chapter says the constant 1.923 applies directly to the bit-length form, which is sloppy enough that a numerate reader will notice.

4. `manuscript/05-drug-discovery.md:14`
   The memory claim is overstated. $\binom{60}{30} \approx 1.18 \times 10^{17}$ amplitudes is huge, but storing that many double-precision complex amplitudes is on the order of exabytes, not "more memory than exists on Earth." The combinatorial point is good; the literal claim is false. Replace it with something like "far beyond the memory budget of any single machine" or "well beyond practical classical state-vector storage."

5. `manuscript/09-finance.md:12`, `manuscript/09-finance.md:25`
   The statement that classical sampling "cannot do better than $1/\sqrt{N}$" is too broad for the way the chapter is written. For black-box Monte Carlo mean estimation, the lower-bound intuition is right. But in practical finance, classical variance reduction, quasi-Monte Carlo, control variates, and multilevel Monte Carlo can outperform plain $1/\sqrt{N}$ behaviour for structured problems. The text should narrow the claim to generic Monte Carlo / black-box sampling rather than all classical pricing methods.

6. `manuscript/01-logistics.md:80`, `manuscript/01-logistics.md:152`
   Two optimisation intuitions are too strong.
   - "Quantum systems are built to find low-energy states. It's what they do naturally" is misleading for gate-model quantum computing. Closed quantum systems evolve unitarily; they do not automatically relax to the ground state of an arbitrary cost Hamiltonian.
   - "As $p \to \infty$, QAOA converges to the exact optimum" needs a caveat about optimal parameter selection / adiabatic-style limits. The best achievable QAOA objective is nondecreasing with depth, but the sentence as written sounds unconditional.

7. `manuscript/13-materials-science.md:16`
   "We literally do not know whether the 2D Hubbard model supports high-temperature superconductivity" is too categorical. The better statement is that the full phase diagram remains unsettled and different high-accuracy methods still disagree in key parameter regimes. There is substantial evidence for superconducting behaviour in some regimes, so the current wording overstates the uncertainty.

8. `manuscript/15-climate-energy.md:50`
   "This is known as DMET or active-space VQE/QPE" conflates one specific embedding framework (DMET) with the broader idea of active-space quantum embedding using VQE or QPE. DMET is one formulation, not a synonym for all active-space quantum/classical embedding pipelines.

## Chapters that looked technically solid on this pass

- `manuscript/02-building-qaoa.md`
- `manuscript/11-supply-chains.md`
- `manuscript/12-qubo-engineering.md`
- `manuscript/17a-error-correction.md`

These chapters still have stylistic and pacing issues noted in the separate reader-experience review, but I did not find comparable math-level errors in them on this pass.

## Reference spot-checks

I spot-checked several of the highest-stakes citations. The following references do appear to exist and broadly support the claims attached to them:

- Gidney and Ekerå (2021) on RSA-2048 and 20 million noisy qubits
- Webster et al. (2026) on the Pinnacle architecture and sub-100,000 physical qubits for RSA-2048 under stated assumptions
- Kim, Jang, et al. (ePrint 2026/106) on updated ECDLP circuits

So the main issue in the cryptography chapter is not fabricated citation; it is comparison hygiene and resource-description accuracy.

## Verification addendum - 2026-04-17

I re-checked the manuscript after the Tier 0 and Tier 0.5 fixes landed, including the follow-up commit that aligned the Deep-Dive 7 Hubbard resource paragraph with the Unit 7 Babbush table.

### Tier 0 status

I am now satisfied that the original Tier 0 issues raised in this audit are resolved:

- The finance pair now describes payoff-amplitude encoding correctly, and the deep dive explicitly uses the $\sqrt{f(x)}$ amplitude construction instead of implying a threshold-event estimator.
- The Shor periodic-superposition normalisation has been fixed from $1/\sqrt{r}$ to $1/\sqrt{M}$.
- The phase-kickback "catalyst" language in Deep-Dive 2 now correctly distinguishes the single-bit $| - \rangle$ trick from the entangled multi-bit Shor oracle.
- The raising-operator and Y-measurement statements in the VQE deep dive have been corrected.
- The 2-site Hubbard worked example now uses "crossover" language instead of claiming a true Mott phase transition.
- The Deep-Dive 7 resource paragraph is now aligned to the same $8 \times 8$, ~400 logical-qubit, ~$10^{11}$ T-gate benchmark used in Unit 7.
- The active-space qubit-counting language in Units 8 / Deep-Dive 8 is materially clearer and now consistently distinguishes spatial orbitals from spin-orbitals and encoded qubits.

### Tier 0.5 status

I am satisfied that the Tier 0.5 issues are now resolved as well:

- The continued-fractions count in the toy Shor example is fixed.
- The GNFS asymptotic is now written in the standard $\ln N$ / $\ln\ln N$ form.
- The memory claim in the drug-discovery chapter has been softened to something technically defensible.
- The Monte Carlo discussion now scopes the $1/\sqrt{N}$ statement to generic sampling rather than all classical finance methods.
- The gate-model low-energy-language and QAOA $p \to \infty$ caveat in Unit 1 are fixed.
- The 2D Hubbard uncertainty language is now appropriately cautious.
- The DMET / active-space embedding distinction is now explicit.
- The RSA-2048 logical-qubit estimate in the cryptography chapter has been updated from the earlier rough ~4,000 figure to ~6,000, which is consistent with the Gidney and Ekerå abstract-circuit formula quoted in this audit.

## Current status

**Tier 0: closed.**

**Tier 0.5: closed.**

At this point, I am satisfied that the Tier 0 and Tier 0.5 bundle is resolved properly and can be treated as complete for purposes of moving on to Tier 1 readability work.

No manuscript text was changed.

## Tier 1 verification addendum - 2026-04-17

I then reviewed the Tier 1 readability pass against the targets in `ACTION-PLAN.md`.

### Initial Tier 1 landing

The main Tier 1 readability changes landed cleanly:

- `01-logistics.md` now introduces the "interference machine" thesis early, removes the unfulfilled teleportation forward reference, and trims the Reality Check into a more readable shape.
- `02-building-qaoa.md` now defines the Bloch sphere at first use.
- `09-finance.md` now gives Grover / amplitude estimation substantially more runway before introducing QAE.
- `13-materials-science.md` now builds the Hubbard Hamiltonian in stages rather than dropping the full notation all at once.

Those changes improved readability without introducing any obvious new mathematical problems.

### Follow-up concerns from the first Tier 1 review

My first Tier 1 pass still identified two residual issues:

1. the high-depth QAOA claim in `01-logistics.md` needed a narrower caveat; and
2. the worked-example prose in `07-machine-learning.md` had drifted away from the notebook.

### Follow-up verification

These two follow-up commits resolved those concerns in sequence:

- `89231e24ae529fb17ee5e3ca703e47125143b839` fixed the QAOA caveat by narrowing the high-depth competitiveness claim to the specific problem families supported by the cited exact-evaluation results.
- `033dd71282ce4880632e51505eb1d90205506a91` fixed the remaining Unit 4 mismatch by bringing the worked example back into alignment with the notebook: interleaved half-moons, 40 points, and no unsupported specific accuracy figure.

The final Unit 4 wording is also stronger on honesty: for this toy 2D problem, both kernels perform well, and any higher-dimensional advantage is left conditional on data structure and feasible encoding.

## Final status

**Tier 0: closed.**

**Tier 0.5: closed.**

**Tier 1: closed.**

At this point, I am satisfied that the Tier 1 readability bundle has landed cleanly and that the earlier residual concerns from the first Tier 1 review are now resolved.

Residual note: I did not rerun the machine-learning notebook end-to-end in this verification pass, but the prose no longer depends on any unverified accuracy number.

## Tier 2 verification addendum - 2026-04-17

I reviewed the Tier 2 readability / friction-reduction commit `07b13b1b8ab9782014dbec4e83cdfd8c98986e87`.

### Result

I did **not** find any new factual, mathematical, or conceptual regressions in the landed Tier 2 edits.

The following changes all look directionally good and technically safe on this pass:

- Unit 1 now grounds the "cost landscape" metaphor more concretely and defines barren plateaus at first use.
- Unit 2's Reality Check uses cleaner parenthetical citation style, and Deep-Dive 2 is less cluttered by adder name-dropping.
- Deep-Dive 2's garbage-entanglement explanation is more concrete.
- Deep-Dive 3 now gives a useful anticommutation example.
- Unit 5 now disambiguates the overloaded $\sigma$ notation.
- Deep-Dive 5 has a stronger opening orientation section.
- Unit 6 now unpacks QUBO and adds a good marble-in-a-bowl intuition for the adiabatic theorem.
- Units 4 and 7 define barren plateaus at first use.
- Units 3 and 8 now remind the reader what tapering means when it reappears.
- Deep-Dive 7's qubitization section is clearer.
- 17a's LDPC section is more useful and better connected to the resource-estimate story elsewhere in the book.

This commit also correctly keeps the review trail consolidated by deleting the standalone `2026-04-17-tier1-verification.md` note and leaving the main audit as the single review record.

### Remaining Tier 2 items

I would **not** mark the entire Tier 2 bundle closed yet.

At least two Action Plan items still appear open:

- `T2-4` (`05-drug-discovery.md`): the long Schrödinger / orbital setup still appears largely intact rather than being split into a gentler progression.
- `T2-15` (global Reality Check template pass): I do not see evidence in this commit of a full all-units template pass; this looks like a strong partial Tier 2 landing rather than the complete Tier 2 checklist.

### Current assessment

The Tier 2 edits that *did* land are in good shape. I am comfortable signing off on this commit as a clean readability pass with no new technical problems introduced.

But Tier 2 as a whole still looks **partially complete**, not fully closed.
