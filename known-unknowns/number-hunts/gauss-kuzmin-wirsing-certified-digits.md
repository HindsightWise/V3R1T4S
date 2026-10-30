# Gauss-Kuzmin-Wirsing constant (C_83): more than Nisoli's 175 certified decimals of |lambda_2|

🔢 **Number hunts** · standard · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 83. The Gauss-Kuzmin-Wirsing operator (Lf)(x) = sum_k (x+k)^-2 f(1/(x+k)) is the transfer operator of the Gauss map. Its subdominant eigenvalue lambda_2 is negative, and C_83 = |lambda_2| = 0.30366300289873265859744812190155623... sets the rate in the Gauss-Kuzmin theorem. Certified bounds: 0.30366299 to 0.30366327 (Dieter Mayer and Gert Roepstorff 1987, Temple inequalities), then a 175-digit enclosure by Isaia Nisoli (arXiv 2602.19435, v2 1 Mar 2026). Nisoli's a posteriori finite-rank method certifies the first 50 nonzero eigenvalues to at least 90 rigorous digits, with eigenvectors and Riesz projectors; code is at github.com/orkolorko/GKWExperiments.jl. Non-certified values are much longer: Wirsing 1974 (20 digits), Flajolet-Vallee (about 30), Keith Briggs 2003 (385 digits; OEIS A038517 b-file has 382 terms) and Giedrius Alkauskas 2012 (over 480 digits). The certified record therefore lags the numerical one by a factor of almost three, and the operator is compact on Hardy spaces of discs around [0,1], so rigorous enclosures converge geometrically.

## What counts as a win

Success means a rigorous enclosure of lambda_2 with radius below 10^-D, D STRICTLY GREATER (direction: max) than the certified digit count on https://teorth.github.io/optimizationproblems/constants/83a.html and in any open pull request touching constants/83a.md (currently 175, Nisoli 2026), re-fetched immediately before claiming. The enclosure's centre must agree with Nisoli's 175-digit centre to within the two radii. The certificate is a program in rigorous arithmetic (Arb, python-flint, IntervalArithmetic.jl or exact rationals) that bounds the discretisation error on a stated function space and certifies isolation of lambda_2 (for example by a resolvent bound on a contour), and a skeptic reruns it.

## Partial wins

- **p1:** A rigorous enclosure of some other eigenvalue lambda_k (3 <= k <= 51) of the GKW operator with at least 150 certified decimals, beating Nisoli's at-least-90-digit guarantee for that eigenvalue.
- **p2:** A non-certified computation of lambda_2 to at least 600 decimals by two independent methods (for example Babenko-Mayer power-series matrices and Briggs-style Chebyshev collocation at sizes differing by at least 2%) agreeing on all 600, with the first 175 matching Nisoli's centre.

## How a win is checked

Skeptic: rerun the certifier at two working precisions. Check that the stated function space (for example H^inf of a disc containing [0,1]) makes L compact and that the truncation bound is applied as proved. Confirm that the isolating contour encloses exactly one eigenvalue. Compare the leading digits with Nisoli's centre and OEIS A038517. Expected: under an hour at 200-300 digits.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/83a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/83a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/83a.md>
- <https://arxiv.org/abs/2602.19435>
- <https://github.com/orkolorko/GKWExperiments.jl>
- <https://oeis.org/A038517>
- <http://keithbriggs.info/documents/wirsing.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the Mayer representation of L as an integral operator on a Hardy space of the disc |z - 1| < 3/2, where matrix truncation errors are explicit and decay geometrically.
- Numerical-analysis import: Kato-Temple and Lehmann-Goerisch bounds give two-sided eigenvalue enclosures from a Rayleigh quotient and a residual norm, often more digits for the same matrix size than resolvent methods.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Counting digits of agreement between two non-rigorous runs is not certification; the main win requires a proved error bound.
- lambda_2 is negative and C_83 = |lambda_2|; sign slips produce nonsense comparisons.
- The OEIS data field shows 105 digits and the b-file 382, but the record to beat is the certified 175.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/gauss-kuzmin-wirsing-certified-digits.md
```

Already set up? Say `run V3R1T4S on gauss-kuzmin-wirsing-certified-digits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gauss-kuzmin-wirsing-certified-digits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
