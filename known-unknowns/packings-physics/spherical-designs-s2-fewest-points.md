# Spherical t-designs on S^2 with fewer points: beat the smallest known N for a degree t (Hardin-Sloane, Graef-Potts and Womersley tables)

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (numerical design search plus high-precision polishing; N up to ~5000) · open as of 2026-10-30

## The problem

A spherical t-design is a set of N points on S^2 whose equal-weight average integrates every polynomial of degree <= t exactly. The smallest N for each t is unknown beyond small cases. Live records (checked 2026-10-30): (1) R. H. Hardin and N. J. A. Sloane (neilsloane.com/sphdesigns/, DCG 1996, last modified Oct 02 2002) conjecture tau(N), the largest t for an N-point design, for N <= 100, giving minimal N = 12, 24, 24, 36, 48, 60, 70, 84, 94 for t = 5..13; their library /sphdesigns/dim3/ also has des.3.N.t files up to a 240-point 21-design; (2) Manuel Graef's putatively optimal Chebyshev-type rules (TU Chemnitz quadrature page, dated 18 Nov 2016; Graef-Potts, Numer. Math. 2011) for t = 1..42 (except 4 and 6), even t = 44..90, t = 94, 98, 100, 114, 124 and high-degree files for t = 100..1000, e.g. t = 14: 108, 20: 216, 30: 480, 40: 840, 60: 1860, 100: 5100; (3) Rob Womersley's efficient designs (UNSW, index updated 4-Feb-2017): sf for all t <= 180 with N = ceil((t+1)^2/2)+1 for even t and t >= 17 (e.g. t = 92: 4326), and symmetric ss for odd t <= 325 with N = 2 ceil((t^2+t+4)/4) for t >= 17 (e.g. t = 43: 948, 99: 4952). Womersley says these need not be smallest. The record N(t) is the minimum over all these files of designs with strength >= t, e.g. 13: 94, 15: 120, 43: 948, 92: 4326, 96: 4706. Henry Cohn now hosts the Hardin-Sloane table (cohn.mit.edu/sloane, same tau values). A 2026-10-30 literature search found no smaller designs: the AlphaEvolve survey (Georgiev, Gomez-Serrano, Tao, Wagner, arXiv:2511.02864, section 17) reports uncertified numerical (error < 1e-8) 19-designs with 198-204 points and 21-designs with 234-236 points, which improve only on the Hardin-Sloane library files (204, 240) and do not beat Graef's 192 and 234; Xu and Xu (arXiv:2609.15016) prove existence with 54t^2 points, far above the records. Search again before attacking and before claiming.

## What counts as a win

Success means either (a) for some t in 13..100, an N-point t-design on S^2 with N STRICTLY LESS (direction: min) than the record N(t) = minimum over the Hardin-Sloane tau table and /sphdesigns/dim3/ library, Graef's Chebyshev-type S^2 files (S2designs and S2designs_high) and Womersley's sf and ss tables of the N of any design with strength >= t, all re-fetched immediately before claiming, or (b) for some N <= 100, an N-point design of strength tau(N)+1 (disproving the Hardin-Sloane conjecture at that N). The design is verified from coordinates given to >= 32 significant digits: after normalization in >= 40-digit arithmetic (mpmath or Arb), S_l = (4 pi/(2l+1)) sum_k |(1/N) sum_j Y_lk(x_j)|^2 (equal to (1/N^2) sum_{i,j} P_l(x_i . x_j)) is < 1e-40 for every l = 1..t, computed from the Weyl sums (the pair-sum form needs >= 60 digits because of cancellation). N must also exceed the Delsarte-Goethals-Seidel bound ((e+1)^2 for t = 2e, (e+1)(e+2) for t = 2e+1) and must not be matched by any design the skeptic finds in the literature for strength >= t.

## Partial wins

- **p1:** For some t in 101..325, an N-point t-design with N strictly below the same merged record N(t), verified in double precision with every S_l <= 1e-26 for l = 1..t (the standard of Womersley's posted files), coordinates to >= 16 digits.
- **p2:** A computer-assisted existence proof (interval Newton or Krawczyk in Arb, in a symmetry-reduced system, own code that the skeptic reruns) of a t-design with N equal to the record N(t) for some t >= 14 for which the skeptic finds no published existence proof at that N (Hardin-Sloane's V1/V2 proofs cover only a few small cases; Chen-Frommer-Lang's interval proofs use N = (t+1)^2).

## How a win is checked

Checker: fetch neilsloane.com/sphdesigns/ (tau table), Graef's page (S2designs/N < t > _M < N > _*.dat links) and Womersley's sf.html and ss.html (file names sfTTT.NNNNN, ssTTT.NNNNN) and build N(t) = min N over all entries of strength >= t. Load claimed points in mpmath at 40 digits, normalize, compute Weyl sums sum_j Y_lk(x_j) by the stable Legendre recurrence for l <= t (cost N (t+1)^2; minutes for N <= 1000, about an hour at N = 5000), and S_l = 4 pi/(2l+1) sum_k |sum_j Y_lk(x_j)/N|^2; assert max S_l < 1e-40. Check N < N(t). Run the checker on one posted file per source as a parser sanity test.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/>

## Sources

- <http://neilsloane.com/sphdesigns/>
- <https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/>
- <https://web.maths.unsw.edu.au/~rsw/Sphere/EffSphDes/>
- <https://web.maths.unsw.edu.au/~rsw/Sphere/EffSphDes/sf.html>
- <https://web.maths.unsw.edu.au/~rsw/Sphere/EffSphDes/ss.html>
- <https://cohn.mit.edu/sloane>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Graef's records use rotation-group symmetry (Sobolev's theorem): only invariant harmonics need vanish, so a T-, O- or I-invariant ansatz with N = sum of orbit sizes reduces the equations sharply; try orbit mixes Graef did not list, especially at even t > 60 where only Womersley's sf formula is posted (e.g. t = 92, 96, 102-112) and Graef's pattern sits 2-6 points lower.
- Minimize Womersley's potential A_{t,N} (sum of a positive-definite polynomial kernel) with L-BFGS at N = record-1, record-2 from many starts; polish survivors with Levenberg-Marquardt in double-double, then mpmath.
- For odd t, antipodal designs need only even-degree harmonics; Womersley's ss family is the record at most odd t >= 43, so a symmetric search with 2 fewer points is the most direct test.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A double-precision residual of 1e-16 does not prove a design when N < (t+1)^2/2 (more equations than unknowns): the 1e-40 standard at >= 30 digits is required for a full win.
- The record at t is the minimum over designs of strength >= t, so a 14-design with 108 points also bounds t = 13 and lower.
- Graef's regular files start with a header (number of columns, number of points) followed by Cartesian rows; his high-degree S2designs_high files instead give spherical angles (phi, theta).
- t <= 12 entries are Hardin-Sloane conjectures backed by extensive search; attacking them is a moonshot.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/spherical-designs-s2-fewest-points.md
```

Already set up? Say `run V3R1T4S on spherical-designs-s2-fewest-points`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `spherical-designs-s2-fewest-points`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
