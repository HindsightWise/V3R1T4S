# Bohr radius of the bidisc K_2 (C_59): an explicit Schur function beating the 0.302825279492 upper bound, or a certified lower bound above Knese's 0.3006

✏️ **Erdős problems and proofs** · standard · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 59. K_2 is the largest r such that sum |f_{jk}| r^{j+k} <= 1 for every analytic f mapping the bidisc D^2 into D (the Schur class). Bohr proved K_1 = 1/3, and the exact value of K_d is unknown for every d > 1. Bounds on the live page: 1/(3 sqrt 2) <= K_2 <= 1/3 (Harold Boas and Dmitry Khavinson, PAMS 1997). Greg Knese (PAMS Ser. B 12 (2025), arXiv 2410.21693) proved K_2 >= 0.3006. Upper bounds: 0.3177 (Baran, Pikul, Woerdeman and Wojtylak, JFA 2026), 0.3174541 (Sebastian Griego 2026, a degree-(250,250) rational-inner Fejer certificate) and 0.302825279492 (Shivam Patel, 26 Aug 2026). Patel's f = (SQ - P)/(SQ + P) is built from U = (1+z)(1-w), V = 1+zw, P = LU + iTV, Q = LV + iTU with integer L, T, S. Two independent exact computations of the 841 coefficients with j, k <= 28 give a majorant above 1 + 1e-26 at r = 0.302825279492; the Python and Lean proof package is Zenodo 10.5281/zenodo.22341928. The open gap [0.3006, 0.30283] is small, and the upper-bound side needs only an explicit object with an exact check.

## What counts as a win

Main win (upper): an explicit f with exact rational or Gaussian-rational parameters, a certificate that |f| <= 1 on D^2 (an exact algebraic argument, or interval verification on the torus plus the maximum principle with poles excluded from the closed bidisc), and an exact finite partial sum of |f_{jk}| r^{j+k} exceeding 1 at a rational r STRICTLY LESS (direction: min) than the smallest upper bound on https://teorth.github.io/optimizationproblems/constants/59a.html and in any open pull request touching constants/59a.md, re-fetched immediately before claiming. Alternative main win (lower): a proof that K_2 >= l with l STRICTLY GREATER than the page's best lower bound (0.3006), with all numerics certified by a supplied program.

## Partial wins

- **p1:** An independent replay of Patel's certificate in a second language or CAS (exact integer arithmetic): recompute all 841 coefficients and the majorant at r = 302825279492/10^12, and verify the Schur-class property, confirming the bound or exhibiting the step that fails.

## How a win is checked

Skeptic: recompute the Taylor coefficients of f exactly (rational or Gaussian-integer arithmetic, two implementations) and the partial majorant at the claimed r. Verify the Schur-class certificate: denominator nonvanishing on the closed bidisc and |f| <= 1, by exact positivity or interval subdivision of the torus. Expected: minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/59a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/59a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/59a.md>
- <https://doi.org/10.5281/zenodo.22341928>
- <https://github.com/Shivamshaiv/bidisc-bohr-certificate/tree/27464dce16c7fe41733befe32e672cff87139b6f/certificate>
- <https://arxiv.org/abs/2410.21693>
- <https://arxiv.org/pdf/math/9606203>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Patel's family is a Cayley transform of a two-variable rational function with a few integer parameters; search richer families (more factors in U and V, higher degree) with the exact majorant as objective.
- Rational inner functions on the bidisc have a stable-polynomial description (Agler, Knese), so optimise over stable polynomials p and f = z^n w^m conj(p(1/conj z, 1/conj w))/p.
- For the lower bound, Knese's three-radii method plus a computer-assisted coefficient-body estimate (as in Wikstrom's Landau work) may push past 0.3006.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Patel's note is also posted on mathdb.com, which returned HTTP 403 at check time. If that site attaches a live bounty to the problem, the target belongs with setter challenges; re-check before attacking.
- A partial sum over a finite coefficient box is a valid lower estimate of the majorant only because all terms are nonnegative; truncating the Schur-class proof the same way is not valid.
- Floating-point coefficient sums near 1 + 1e-26 are meaningless; use exact arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/bohr-radius-bidisc-k2-bounds.md
```

Already set up? Say `run V3R1T4S on bohr-radius-bidisc-k2-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bohr-radius-bidisc-k2-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
