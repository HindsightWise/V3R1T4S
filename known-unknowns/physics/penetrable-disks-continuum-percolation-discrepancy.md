# Penetrable disks in the plane: settle the 3-sigma clash between Mertens-Moore's eta_c = 1.12808737(6) and the critical-polynomial 1.12808706(8)

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (microcanonical union-find on tori with 1e8-1e9 disks) · open as of 2026-10-30

## The problem

The critical filling factor eta_c of equal fully penetrable disks (2D Poisson Boolean model; critical density n_c = 4 eta_c / pi) is a benchmark of continuum percolation. Stephan Mertens and Cristopher Moore (Phys. Rev. E 86 (2012) 061109, arXiv 1209.4936) used wrapping probabilities with the exactly known universal torus values and found eta_c = 1.12808737(6), n_c = 1.43632545(8). Wenhui Xu, Junfeng Wang, Hao Hu and Youjin Deng (Phys. Rev. E 103 (2021) 022127, arXiv 2010.02887) used critical polynomials and found n_c = 1.43632505(10) (eta_c = 1.12808706(8)), which they describe as slightly below Mertens-Moore's. Zbigniew Koza, Piotr Brzeski and Grzegorz Kondrat (J. Phys. A 56 (2023) 165001, three-leg cluster method) found 1.1280867(5), closer to the critical-polynomial value but too coarse to decide. The gap, about 3.1e-7 in eta, is about 3 combined sigma; Wikipedia's 2D continuum table (checked 2026-10-30) lists no resolution.

## What counts as a win

Success means an estimate of eta_c for equal fully penetrable disks with stated one-sigma uncertainty at most 2e-8 (3 times smaller than Mertens-Moore's), such that (a) two methods agree within their combined uncertainties (for example wrapping probabilities on tori with and without the universal-value constraint, critical polynomials on growing bases, or the three-leg method), (b) the claim states its distance, in combined sigma, to both 1.12808737(6) and 1.12808706(8) (no particular outcome is required), (c) finite-size data, fits and code are released, and (d) a literature search immediately before claiming finds no published value with uncertainty below 2e-8. Direction: smaller uncertainty.

## Partial wins

- **p1:** An independent eta_c with uncertainty <= 6e-8 (matching Mertens-Moore's) from a method different from both wrapping-with-universal-value and critical polynomials (for example crossing-only wrapping fits or the three-leg method), under rules (c) and (d), stating its distance to both values.
- **p2:** Using one of the two published methods on the claimant's own released data, reproduce that method's published estimate within its stated error. Then show that including one specific, named systematic effect (a neglected correction term, aspect-ratio effect or base-size trend) shifts the estimate by at least 2e-7 in eta, with the shift stable under dropping the smallest sizes.

## How a win is checked

Skeptic (< 1 hour): rerun the claimant's simulation at two system sizes with fresh seeds; check the universal wrapping values used against the exact torus formulas; refit the released data with an extra correction term and with the correction exponent left free; if critical polynomials are used, re-estimate P_B at two densities from the released samples and refit its zero crossing.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://arxiv.org/abs/1209.4936>
- <https://arxiv.org/abs/2010.02887>
- <https://doi.org/10.1088/1751-8121/acc3d0>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Mertens-Moore fix the threshold from the universal wrapping value; repeating it with a crossing-only fit (no universal input) separates a universal-value bias from statistics.
- Xu et al. simulate the continuum disks directly (tori of side L = 3 to 128, disk diameter 1), assume P_B = 0 at criticality as on planar lattices, and fit with yt = 3/4 and the correction exponent fixed at -2. Freeing the correction exponent, or measuring P_B at the Mertens-Moore density on large L, tests whether the bias sits in that ansatz.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- eta_c vs n_c vs phi_c = 1 - exp(-eta_c): convert consistently before comparing (n_c = 4 eta_c / pi for unit-radius disks).
- Wikipedia's row also lists several 2019-21 powder-technology values with no error bars; they do not count as comparators.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/penetrable-disks-continuum-percolation-discrepancy.md
```

Already set up? Say `run V3R1T4S on penetrable-disks-continuum-percolation-discrepancy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `penetrable-disks-continuum-percolation-discrepancy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
