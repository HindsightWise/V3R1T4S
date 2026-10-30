# Spherical t-designs on S^3 (including SO(3) Chebyshev rules) with fewer points: beat the smallest known N for a degree t

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (N up to ~12000 points in R^4; high-precision polishing is the bottleneck) · open as of 2026-10-30

## The problem

A spherical t-design on S^3 (unit sphere in R^4) is a set of N points whose average integrates every polynomial of degree <= t exactly. Live tables (checked 2026-10-30): (1) Rob Womersley's efficient S^3 designs (UNSW S3SD.html, updated 09-Oct-2017; Womersley 2018, Springer volume for Ian Sloan's 80th): sdf for t = 1..20 (e.g. t = 4: 20, 8: 97, 12: 275, 16: 597, 20: 1106), symmetric sds for odd t <= 31 (e.g. 13: 308, 21: 1184, 25: 1954, 31: 3642) and regular sets sdr (e.g. the 24-cell 5-design and the 120-point 600-cell 11-design); (2) Manuel Graef's Chebyshev-type rules on SO(3) (TU Chemnitz quadrature page, dated 18 Nov 2016) for degrees N = 1..9, 11, 13, 14, 15, 17, 19, 23 with M rotations, which give antipodal S^3 designs of strength 2N+1 with 2M points via unit quaternions +-q (e.g. N = 7, M = 168: a 336-point 15-design). The record N(t) is the minimum over both tables of designs of strength >= t: 12: 275, 13: 308, 14-15: 336, 16: 597, 17: 624, 18-19: 720, 20: 1106, 21: 1184, 22-23: 1344, 24-25: 1954, 26-27: 2352, 28-29: 2520, 30-31: 3552, 32-35: 5040, 36-39: 6600, 40-47: 11760. Above t = 31 the record comes only from sparse SO(3) entries, so t = 32..47 look improvable. Small t (<= 11) involve proven or near-proven cases (8-point cross-polytope, 24-cell, 600-cell; Boyvalenkov-Danev) and Hardin-Sloane-Cara's 4-d tables, so full wins start at t = 12. Checked 2026-10-30: Graef's N07_M168 rotations converted to +-q give a 336-point 15-design (residuals about 1e-17 in double), and a literature search found no 2024-2026 paper with smaller S^3 designs; search again before attacking and before claiming.

## What counts as a win

Success means, for some t in 12..47, an N-point t-design on S^3 with N STRICTLY LESS (direction: min) than the record N(t) (minimum over Womersley's sdf/sds/sdr files on S3SD.html and Graef's SO(3) Chebyshev entries converted to 2M points of strength 2N+1, re-fetched before claiming), not matched by any design the skeptic finds in the literature, and above the Delsarte-Goethals-Seidel bound. Verified from coordinates given to >= 32 digits: after normalization, S_l = (1/N^2) sum_{i,j} U_l(x_i . x_j)/(l+1) < 1e-40 for every l = 1..t (U_l = C_l^(1), Chebyshev of the second kind; these sums are >= 0 and vanish exactly for a design), computed in >= 60-digit arithmetic (Arb or python-flint) because the pair sum cancels from O(1) terms, or from S^3 harmonic Weyl sums in >= 40-digit arithmetic.

## Partial wins

- **p1:** For some t in 32..47, an N-point t-design with N strictly below the record N(t), verified only in double precision with every S_l <= 1e-26 (the standard of the posted files), coordinates to >= 16 digits.
- **p2:** An antipodal (x and -x both present) t-design on S^3 for some odd t in 13..47 with fewer points than every antipodal entry (Womersley sds, sdr, Graef SO(3) conversions) of strength >= t, under the full high-precision checks, even if a smaller non-antipodal design exists.
- **p3:** For some t in 21..31, a t-design with N strictly below the record N(t), verified in double precision as in p1 (a stepping stone toward a full win at the same t).

## How a win is checked

Checker: build N(t) from S3SD.html (file names sd[frs]TTT.NNNNN) and Graef's SO3designs/N < k > _M < m > _*.dat links (strength 2k+1, size 2m). Load claimed points at 40 digits, normalize, compute S_l via S^3 harmonic Weyl sums or the pair sum with the Chebyshev-U recurrence (pair sum cost N^2 t: use Arb or python-flint for N > 2000); assert max S_l < 1e-40. Sanity: convert Graef's N07_M168 rotations to quaternions +-q and confirm a 15-design with S_l ~ 1e-16 in double.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.maths.unsw.edu.au/~rsw/Sphere/EffSphDes/S3SD.html>

## Sources

- <https://web.maths.unsw.edu.au/~rsw/Sphere/EffSphDes/S3SD.html>
- <https://web.maths.unsw.edu.au/~rsw/Sphere/EffSphDes/>
- <https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/>
- <https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/SO3designs/N07_M168_OctaC7.dat>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- t = 32..35: Womersley's sdf growth (about 1.2 t^3/9 points) predicts roughly 4400 points for t = 32, below the 5040 record; minimize the positive-definite potential A_{t,N} with L-BFGS in double, then polish with double-double Gauss-Newton and confirm in Arb.
- Group orbits: unions of orbits of the binary icosahedral group (order 120) acting on both sides of S^3 (pairs G1 x G2 as in Graef's SO(3) tables) reduce the equations by Sobolev's theorem; try group pairs Graef did not list.
- Antipodal symmetry halves the work for odd t: only even-degree harmonics need vanish.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Gegenbauer normalization: for S^3 use C_l^(1) = U_l (Chebyshev second kind), divided by U_l(1) = l+1.
- SO(3) rotation matrices map to quaternions only up to sign; include both q and -q (2M points).
- The record at t is the minimum over designs of strength >= t; for example the 600-cell (120 points) is an 11-design and so bounds t = 10 as well.
- Some small cases are proven minimal or unique (e.g. the 8-point cross-polytope 3-design; Boyvalenkov and Danev on the 120-point 11-design); check the literature before attacking t <= 11.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/spherical-designs-s3-fewest-points.md
```

Already set up? Say `run V3R1T4S on spherical-designs-s3-fewest-points`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `spherical-designs-s3-fewest-points`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
