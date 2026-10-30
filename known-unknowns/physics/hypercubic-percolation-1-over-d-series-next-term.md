# MOONSHOT - Percolation threshold of Z^d in powers of 1/(2d-1): the first coefficient beyond Mertens-Moore's 119077/96 (site) and 4855/12 (bond)

⚛️ **Physics** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster (classical route: Mertens-Moore Table 9 puts the missing bond enumerations at 9 years for (d, e) = (6, 14) up to 133,800 years for (11, 14) on 368 cores, so a full win needs new closed formulas; the Pade route for p1 is months to years) · open as of 2026-10-30

## The problem

With sigma = 2d - 1, the percolation thresholds of the d-dimensional hypercubic lattice have asymptotic expansions p_c^site = 1/sigma + (3/2)sigma^-2 + (15/4)sigma^-3 + (83/4)sigma^-4 + (6577/48)sigma^-5 + (119077/96)sigma^-6 + O(sigma^-7) and p_c^bond = 1/sigma + (5/2)sigma^-3 + (15/2)sigma^-4 + 57 sigma^-5 + (4855/12)sigma^-6 + O(sigma^-7). The first terms are from David Gaunt, Michael Sykes and Heather Ruskin (J. Phys. A 9 (1976) 1899; Gaunt-Ruskin J. Phys. A 11 (1978) 1369). Stephan Mertens and Cristopher Moore (J. Phys. A 51 (2018) 475001, arXiv 1805.02701) added terms after about 40 years. Enumerating proper lattice animals with perimeter and vertex counts on a 368-core cluster, and proving formulas for the top binomial coefficients of bond perimeter polynomials (Theorems 4-6), they obtained 6577/48 and 4855/12 by the classical procedure. Each came from fitting the minimum number of points (for 4855/12 a quadratic in r through r = 10, 11, 12), checked by the cancellation of higher powers of r in ln b_r. The site term 119077/96 comes from their observation that (l-1,1) Pade approximants of the mean-cluster-size series stabilise one coefficient per two terms. Their Theorem 7 shows that this stabilisation is equivalent to the classical one (coefficients of ln b_r linear in r for r >= 2j), so neither route is a proof; the classical route needs more data and so carries more internal checks. For the next bond term the classical route needs b_r for r = 12..15, and their Table 9 estimates the missing enumerations at (d, e) = (6, 14) about 9 years, (7, 14) 116 years and (11, 14) about 133,800 years. The Pade route needs only b_13: about 57 days at (7, 12), 387 days at (8, 12) and 4.5 years at (9, 12). One more site coefficient b_13, which they put at months on a small cluster, would conjecturally give the sigma^-7 site term. The Wikipedia 'Percolation threshold' page (checked 2026-10-30) still shows both series ending at sigma^-6.

## What counts as a win

Success means the exact rational coefficient of sigma^-7 in p_c^site(d) or p_c^bond(d), obtained by the classical Gaunt-Sykes-Ruskin procedure as Mertens-Moore used it for 4855/12, and not from the Pade stabilisation alone. That procedure uses exact perimeter polynomials as functions of d (from enumeration or from proven closed formulas) and fits the sigma^-k coefficients of b_r / sigma^r as polynomials in r through at least the minimum number of points, with the higher powers of r cancelling in ln b_r as the consistency check. Four conditions apply. (a) All enumeration data are released and reproducible by an independent program on at least the smaller (d, size) cases. (b) The same pipeline reproduces every known coefficient obtained classically (site through sigma^-5, bond through sigma^-6). (c) The new series agrees with Mertens-Moore's numerical thresholds for d = 10..13 better than the old series does. (d) A literature check before claiming shows no published sigma^-7 coefficient. Direction: one more exact term.

## Partial wins

- **p1:** The coefficient b_13 of the site (or bond) mean-cluster-size series in Mertens-Moore's sense, as an exact polynomial in d, with the resulting Pade-stabilised (conjectural) sigma^-7 coefficient, both reproducible by a second program.
- **p2:** A proven closed formula for the next coefficient family of the bond perimeter polynomial D_e (the binom(d, e-3) coefficient, extending Mertens-Moore's Theorems 4-6 for binom(d, e), binom(d, e-1), binom(d, e-2)), or the analogous site formula with perimeter. It must remove one of the enumeration tasks in their Table 9 and be checked by computer against brute-force counts for small e and d.

## How a win is checked

Skeptic: recompute the claimed animal counts with perimeter data for small (d, e) by brute force and match exactly; rerun the series derivation script from the released data to reproduce all known coefficients and the new one; compare the extended series with the numerical thresholds for d = 10..13 on the Wikipedia hypercubic table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Percolation_threshold>

## Sources

- <https://arxiv.org/abs/1805.02701>
- <https://en.wikipedia.org/wiki/Percolation_threshold>
- <https://arxiv.org/abs/1806.08067>
- <https://doi.org/10.1088/0305-4470/9/11/015>
- <https://doi.org/10.1088/0305-4470/11/7/025>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exploit that only the dependence on d up to fixed degree matters: count animals as polynomials in d via their 'dimension-reduced' shapes (animals spanning k dimensions times binomial(d, k)), which is how the top coefficients were proven.
- Lace-expansion work (Hara-Slade) gives rigorous 1/d expansions to low order; matching to it is a check on any new term.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Pade stabilisation is an observed pattern, not a proof; it gives p1, not the full win.
- Lattice-animal counts alone (OEIS A151830-type sequences, a separate bank entry) do not suffice; perimeter and vertex counts are needed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/hypercubic-percolation-1-over-d-series-next-term.md
```

Already set up? Say `run V3R1T4S on hypercubic-percolation-1-over-d-series-next-term`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypercubic-percolation-1-over-d-series-next-term`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
