# Square-lattice site percolation threshold: settle the 5-sigma clash between Yang-Zhou's 0.5927460507896(1) and Jacobsen's 0.59274605079016(1) (2024)

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: needs cluster (exact transfer matrices with state counts growing like ~2.6-2.75^n; n >= 25 needs 100+ GB RAM big-memory nodes) · open as of 2026-10-30

## The problem

Site percolation on the square lattice has no exact threshold. Jesper Jacobsen (J. Phys. A 48 (2015) 454003, arXiv 1507.03027) located p_c from eigenvalue identities in the periodic Temperley-Lieb algebra on semi-infinite cylinders of circumference n <= 21 and quoted 0.59274605079210(2). Stephan Mertens (J. Phys. A 55 (2022) 334002, arXiv 2109.12102) computed the exact spanning probability R_n(p) of n x n squares up to n = 24 (complexity ~2.6^n) and got 0.592746050786(3). Yi Yang and Shuigeng Zhou (Comment, J. Phys. A 57 (2024) 258001) computed the exact critical probability h(n) of n x infinity helical lattices up to n = 24 (complexity O(n^2 c^n), c = 2.7459...). They found its extrapolation inconsistent with Jacobsen's value, extended exact cylinder critical points p_c(n) to n = 24, and concluded that the 2015 value is incorrect, giving 0.5927460507896(1). Jacobsen's Reply (J. Phys. A 57 (2024) 258002; full text paywalled) appears in the Wikipedia 'Percolation threshold' square-lattice row (maintained by Robert Ziff, last edited 2026-10-23) with 0.59274605079016(1). The two 2024 values differ by 5.6e-13 with stated errors of 1e-13 (Yang-Zhou) and 1e-14 (Reply), a gap of about 5.6 combined sigma, so at least one error bar is badly underestimated. Both lie within 1.5 sigma of Mertens's 3e-12-wide value. No later value is listed. Settling the 12th-13th digit needs larger exact cylinders, helices or squares (n = 25-28) or an independent extrapolation scheme with honest corrections to scaling.

## What counts as a win

Success means an estimate of the square-lattice site threshold with stated one-sigma uncertainty at most 5e-14, so that the 5.6e-13 gap between the two 2024 values exceeds 10 of its sigma. The estimate must meet five conditions. (a) It is obtained with code written independently of Jacobsen's and Yang-Zhou's, from finite-size data at sizes that include at least one n beyond the largest published for that geometry (n >= 25 for cylinders, helices or squares). (b) Two different estimator families agree within their combined uncertainties, for example Jacobsen's two-sector eigenvalue identity on cylinders and Mertens/Yang-Zhou exact crossing or cylinder critical points. (c) The claim states its distance, in combined sigma, to both 0.5927460507896(1) and 0.59274605079016(1); no particular outcome is required. (d) All finite-size numbers are released to at least 25 digits with the extrapolation script. (e) A re-check of the live Wikipedia row and a literature search immediately before claiming show no third published determination (beyond the 2015 and 2024 values above) with uncertainty at most 5e-14. Direction: a decisive independent value at uncertainty <= 5e-14.

## Partial wins

- **p1:** Exact spanning polynomial R_n(p) of the n x n square (Mertens's definition) for n = 25 or larger, as integer coefficients, with the same code reproducing Mertens's published n <= 24 data (or its root crossings) exactly.
- **p2:** Jacobsen-type two-sector eigenvalue-identity estimates p_c(n) for site percolation on cylinders of circumference n beyond the largest n published by Jacobsen (2015 paper or 2024 Reply), to at least 25 digits, with the code reproducing his published n <= 21 values.
- **p3:** Exact cylinder critical points p_c(n) or helical h(n) in Yang-Zhou's sense for some n >= 25, to at least 25 digits, reproducing their n <= 24 values where published.

## How a win is checked

Skeptic (< 1 hour for checks, not the search): rerun the claimant's code at small n (n <= 12) and compare with published R_n(p) and p_c(n) values exactly; recompute one large-n eigenvalue identity or polynomial root with an independent multiprecision solver; rerun the extrapolation on the released data and refit with one correction term fewer; confirm the stated sigma and the distance to both 2024 values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://arxiv.org/abs/1507.03027>
- <https://arxiv.org/abs/2109.12102>
- <https://doi.org/10.1088/1751-8121/ad4d2c>
- <https://doi.org/10.1088/1751-8121/ad4d33>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Mertens's R_n(p) algorithm is O(2.6^n) in time and memory; frontier-compression tricks from Jensen's SAW/polygon codes and modular arithmetic with CRT reconstruction can push n by 2-4.
- Use the exact cylinder p_c(n) sequence with the known correction exponents for 2D percolation (leading irrelevant exponent and analytic terms) rather than free power laws; the clash is probably about which corrections are included.
- Cross-check the method on bond percolation on the kagome lattice, where Scullard and Jacobsen give 0.52440499916744820(1), before trusting it on the square site problem.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Reply's full text is behind a paywall (IOP); quote its value from the Wikipedia row or a legitimate copy, and do not assume what its argument says.
- Error bars from the spread of the last few extrapolants are the classic false precision; both 2024 values cannot be right as stated.
- Spanning (open boundaries), wrapping (torus) and cylinder quantities converge at different rates and from different sides; do not mix them in one fit without the right correction terms.
- Double precision is useless here; work in exact rationals or >= 40-digit arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/square-site-percolation-threshold-13th-digit.md
```

Already set up? Say `run V3R1T4S on square-site-percolation-threshold-13th-digit`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `square-site-percolation-threshold-13th-digit`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
