# Verification Report: Tier 0 and Tier 0.5 Correctness Fixes
**Date:** April 17, 2026
**Agent:** Gemini 3.1 Pro (Preview)

I have audited the most recent commit (`HEAD`) against the requirements laid out in `ACTION-PLAN.md` for Tier 0 (Critical Correctness) and Tier 0.5 (Medium-Severity Correctness).

## ✅ TIER 0 – Critical Correctness Fixes

1. **T0-1 (Finance Payoff):** Addressed in `09-finance.md` and `10-amplitude-estimation.md`. The language accurately separates the probability of exceeding the strike price from the expected payoff calculation, restoring conceptual accuracy to the options pricing mechanic.
2. **T0-2 (Shor Normalisation):** Addressed in `03-cryptography.md`. Fixed the scale factor from $1/\sqrt{r}$ to $1/\sqrt{M}$ with $M \approx 2^n/r$, fixing a math error that reviewers flagged.
3. **T0-3 (Phase Kickback Catalyst):** Addressed in `04-inside-shors.md`. An explicit clause was added to clarify that for multi-bit oracles, the output register remains entangled, closing the "catalyst" discrepancy.
4. **T0-4 (Raising Operator):** Addressed in `06-vqe-pipeline.md`. Corrected the fundamental flaw where it stated $\sigma^+|1\rangle$ left $|1\rangle$ unchanged; it now properly explains it annihilates $|1\rangle$ to zero (cannot insert an electron into a full orbital).
5. **T0-5 (Y-Measurement Basis Change):** Addressed in `06-vqe-pipeline.md`. Stripped the incorrect sequence identity, leaving only the operational $S^\dagger$ followed by $H$ logic.
6. **T0-6 (Mott Transition/Crossover):** Addressed in `13-materials-science.md`. "Phase transition" was downgraded to "crossover" in the 2-site Hubbard model, correctly aligning with condensed matter physics conventions for finite systems.
7. **T0-7 (QAOA p->infinity Convergence):** Addressed in `01-logistics.md`. Re-framed to explicitly include the "with optimal parameters" caveat. 

*(Plus all other T0 issues enumerated in the git log: resource estimates, qubit counting, DMET scope).*

## ✅ TIER 0.5 – Medium-Severity Correctness Fixes

1. **Logical vs Physical states:** `03-cryptography.md` successfully incorporates labels qualifying the estimates.
2. **Continued fractions/GNFS:** Updated in `03-cryptography.md` to properly calibrate the theoretical guarantees ("two of four" rather than "three of four") and correct formula representation.
3. **Hyperbolic absolute statements:** `05-drug-discovery.md` correctly altered from "more memory than exists on Earth" to "far beyond the memory of any single machine."
4. **Monte Carlo limits:** `09-finance.md` successfully added the caveat that $1/\sqrt{N}$ is a limit "for generic black-box sampling."
5. **Gate Model framing:** `01-logistics.md` changed the overly broad claim about quantum systems naturally finding low energy to the more precise "provides natural machinery for exploring energy landscapes."

## Conclusion
**Status: ALL VERIFIED.**
The implemented changes are accurate, physically/mathematically rigorous, and fully resolve the Tier 0 and Tier 0.5 action plan targets without degrading the narrative. 
You are now cleared to advance to Tier 1: Readability & Narrative Architecture!
