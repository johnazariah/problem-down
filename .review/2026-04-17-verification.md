# Verification Report: Tier 0 and Tier 0.5 Correctness Fixes
**Date:** April 17, 2026
**Updated by:** GPT-5.4

I audited the current `HEAD` against the `TIER 0` and `TIER 0.5` items in [ACTION-PLAN.md](/workspace/.review/ACTION-PLAN.md). Most of the correctness work is now in good shape, but I am not comfortable marking the bundle fully complete yet.

## Tier 0

The following items now read as properly resolved:

1. **T0-1 (Finance payoff encoding):** The manuscript now correctly describes payoff-amplitude encoding in [manuscript/09-finance.md](/workspace/manuscript/09-finance.md) and [manuscript/10-amplitude-estimation.md](/workspace/manuscript/10-amplitude-estimation.md), including the $\sqrt{f(x)}$ amplitude construction and the rescaling by $P_{\max}$.
2. **T0-2 (Shor normalisation):** Fixed in [manuscript/03-cryptography.md](/workspace/manuscript/03-cryptography.md) from $1/\sqrt{r}$ to $1/\sqrt{M}$ with the correct register-size dependence.
3. **T0-3 (Phase-kickback catalyst overreach):** Fixed in [manuscript/04-inside-shors.md](/workspace/manuscript/04-inside-shors.md) with an explicit caveat for multi-bit outputs.
4. **T0-4 (Raising operator):** Fixed in [manuscript/06-vqe-pipeline.md](/workspace/manuscript/06-vqe-pipeline.md); the text now correctly says the operator annihilates $|1\rangle$.
5. **T0-5 (Y-basis measurement identity):** Fixed in [manuscript/06-vqe-pipeline.md](/workspace/manuscript/06-vqe-pipeline.md) by removing the incorrect identity and keeping the correct operational basis-change description.
6. **T0-6 (Mott transition vs crossover):** Fixed in [manuscript/13-materials-science.md](/workspace/manuscript/13-materials-science.md).
7. **T0-8 (Active-space qubit counting):** The Unit 8 / Deep-Dive 8 spatial-orbital versus spin-orbital convention is now materially clearer and internally consistent.

### Residual Tier 0 issue

**T0-7 is not fully resolved.**

The main DD7 resource paragraph is improved, but [manuscript/14-qpe-trotter.md](/workspace/manuscript/14-qpe-trotter.md) still summarizes the 2D Hubbard target as:

- `~200 qubits`
- `~10^7 gates`
- `~10^5 physical qubits`

in the takeaway section, while [manuscript/13-materials-science.md](/workspace/manuscript/13-materials-science.md) still gives an $8 \times 8$ lattice as `~400 logical` qubits and `$10^{11}$ T-gates`.

A larger `10 x 10` lattice cannot simultaneously require half as many qubits in the simplified summary. So the resource story is cleaner than before, but not yet internally closed.

## Tier 0.5

These items now look satisfactorily resolved:

1. **T0.5-1 (Logical vs physical qubit hygiene):** [manuscript/03-cryptography.md](/workspace/manuscript/03-cryptography.md) now keeps the major comparisons on the same footing and defines the distinction explicitly in the Reality Check.
2. **T0.5-2 (Continued fractions count):** Fixed in [manuscript/03-cryptography.md](/workspace/manuscript/03-cryptography.md) from the incorrect “three of four” claim.
3. **T0.5-3 (GNFS formula):** Fixed in [manuscript/03-cryptography.md](/workspace/manuscript/03-cryptography.md) by switching to the standard $\ln N$ / $\ln\ln N$ form.
4. **T0.5-4 (Memory claim):** Fixed in [manuscript/05-drug-discovery.md](/workspace/manuscript/05-drug-discovery.md).
5. **T0.5-5 (Monte Carlo scaling overclaim):** Fixed in [manuscript/09-finance.md](/workspace/manuscript/09-finance.md) with a generic-sampling caveat.
6. **T0.5-6 (Gate-model low-energy wording):** Fixed in [manuscript/01-logistics.md](/workspace/manuscript/01-logistics.md).
7. **T0.5-7 (QAOA $p \to \infty$ caveat):** Fixed in [manuscript/01-logistics.md](/workspace/manuscript/01-logistics.md).
8. **T0.5-8 (2D Hubbard overstatement):** Fixed in [manuscript/13-materials-science.md](/workspace/manuscript/13-materials-science.md).
9. **T0.5-9 (DMET scope):** Fixed in [manuscript/15-climate-energy.md](/workspace/manuscript/15-climate-energy.md).

## Conclusion

**Status: MOSTLY VERIFIED, NOT FULLY CLOSED.**

I am satisfied that all `Tier 0.5` items are resolved properly, and that `Tier 0` is resolved except for the remaining DD7 resource-summary inconsistency described above.

Once that one item is corrected, I would be comfortable signing off the full `Tier 0 + Tier 0.5` bundle as complete and moving cleanly to `Tier 1`.
