# Maximum-determinant (Fekete-type interpolation) points on S^2: a larger log det than Womersley's table for some degree n <= 100

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (n <= 40) to laptop-days (n near 100; (n+1)^2 x (n+1)^2 Gram matrices up to 10201 x 10201) · open as of 2026-10-30

## The problem

For polynomial degree n choose d_n = (n+1)^2 points x_1..x_dn on S^2 to maximize log det G, where G_ij = sum_{l=0}^n (2l+1)/(4 pi) P_l(x_i . x_j) is the reproducing-kernel Gram matrix of polynomials of degree <= n (maximum determinant, or extremal, systems; good interpolation and cubature nodes). Rob Womersley's MaxDet page (UNSW, updated 03-Jun-2020; with Ian Sloan, Adv. Comput. Math. 2001, 2004) lists n = 1..200 with f = log det G to 2 decimals, bounds log(d_n!/(4 pi)^d_n) <= f <= d_n log(d_n/(4 pi)), the gradient norm, and files S2Pts/MD/mdNNN.NNNNN (x, y, z and cubature weight per row, 16 digits). Only n = 1 (regular tetrahedron) is a proven global maximum; Womersley notes many local maxima and that background searches update the table when better systems are found. Rows n <= 100 are converged (gradient 1e-15 to 3e-10); rows n = 101..200 have gradient 4.9e-4 to 1e-2. Checked 2026-10-30: md010.00121 recomputes to f = 266.3178 (table 266.32). Example values: n = 20: 1535.65, n = 50: 13648.51, n = 100: 67416.72. Womersley's older extremal tables (17-Oct-2007 and 16-Jan-2003 pages) have no row above the 2020 values. A 2026-10-30 literature search found no later improvement; search again before claiming.

## What counts as a win

Success means, for some n in 2..100, (n+1)^2 points on the unit sphere (coordinates to >= 16 digits) whose log det G* (Cholesky in double after normalizing; confirmed in mpmath at 30 digits for n <= 20) is STRICTLY GREATER (direction: max) than both (i) the table value f(n) on the live MaxDet1.html plus 0.005 (the 2-decimal rounding), and (ii) the log det of Womersley's posted md file for n after the skeptic polishes it by gradient ascent to gradient norm < 1e-10, by at least 1e-6 in each case, re-fetched immediately before claiming. The claimed set must be a numerical local maximum (gradient norm < 1e-8) so the value is well defined.

## Partial wins

- **p1:** For some n in 101..150 (rows whose posted gradient norm is 4.9e-4 or more), a point set whose log det exceeds the polished posted md file's value by at least 0.01; this beats the table only in its unconverged region, so it is a partial win.
- **p2:** A table-integrity finding: an n whose posted md file recomputes to a log det differing from the table's f by more than 0.01, reported with both values.

## How a win is checked

Checker: fetch MaxDet1.html and parse f(n); download S2Pts/MD/md < n > . < d_n > ; build G from the Legendre recurrence; slogdet via Cholesky (assert positive definite); polish posted points by projected gradient ascent (the gradient of log det G is the row-wise kernel derivative weighted by G^-1); compute the claimed set's log det the same way; assert both margins. About 2 minutes for n = 100 on 16 GB RAM.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.maths.unsw.edu.au/~rsw/Sphere/MaxDet/MaxDet1.html>

## Sources

- <https://web.maths.unsw.edu.au/~rsw/Sphere/MaxDet/>
- <https://web.maths.unsw.edu.au/~rsw/Sphere/MaxDet/MaxDet1.html>
- <https://web.maths.unsw.edu.au/~rsw/Sphere/S2Pts/MD/md010.00121>
- <https://web.maths.unsw.edu.au/~rsw/Sphere/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Many restarts with diverse seeds (spiral, Thomson minima, efficient designs with (n+1)^2 points, icosadeltahedral sets) followed by L-BFGS on log det; low-n rows (n = 14..46) date from 2002-2006 and may have been searched less than the 2019-2020 rows.
- Defect engineering as in Thomson searches: relocate the 12 disclination-like defects of the Voronoi structure and re-optimize.
- Use the gradient formula with a G^-1 update (Sherman-Morrison) for single-point moves to make basin hopping cheap.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The table has 2 decimals; always compare against the recomputed and polished posted file, not the printed number.
- log det depends on the kernel normalization; use exactly G_ij = sum (2l+1)/(4 pi) P_l, which reproduces Womersley's values.
- n >= 101 rows are unconverged; polishing alone raises them, which is why they are only p1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/womersley-maxdet-points-s2.md
```

Already set up? Say `run V3R1T4S on womersley-maxdet-points-s2`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `womersley-maxdet-points-s2`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
