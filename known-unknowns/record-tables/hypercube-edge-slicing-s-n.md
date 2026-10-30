# Slicing the hypercube: fewer hyperplanes than ceil(4n/5) cutting every edge of Q_n (e.g. 5 for Q_7), or new S(n,k) edge records

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (edge-weighted local search over integer hyperplanes; a full check of Q_n for n <= 20 takes seconds) · open as of 2026-10-30

## The problem

S(n) is the fewest hyperplanes in R^n such that every edge of the cube Q_n on {-1,1}^n is cut in its interior by one of them. Trivially S(n) <= n. Paterson's construction (reported by O'Neil, 1971) gave S(n) <= ceil(5n/6), and this stood for over fifty years. S(n) = n for n <= 5 and S(6) = 5 (Emamy-Khansary and Ziegler). Lower bounds are sublinear: O'Neil Omega(sqrt n), then Yehuda-Yehudayoff, Klein, and Sauermann-Xu (2025) Omega(n^{13/19} polylog). Sauermann-Xu (2026) show that integer coefficients suffice and give n/(4C) for coefficients bounded by C. Soiffer, Itty, Rosin, Bruell, DiCicco, Sárközy, Offstein and Reichman, 'Improved Upper Bounds for Slicing the Hypercube', arXiv:2602.16807 (v2, 29 Jun 2026), found 8 hyperplanes slicing Q_10 with CPro1-assisted search. By subadditivity S(n) <= ceil(4n/5), or 4n/5 + 1 when n is an odd multiple of 5. Current bounds: S(7) <= 6, S(8) <= 7, S(9) <= 8, S(11) <= 9, S(12) <= 10, S(13) <= 11. The paper says it is open whether S(7) = 5. Its Tables 1-2 give record partial slicings S(n,k), the most edges of Q_n cut by k hyperplanes, for example S(7,5) >= 440 of 448, S(9,7) >= 2298 of 2304 and S(11,8) >= 11240 of 11264. Code and solutions: github.com/DSoiffer/upper-bounds-for-hypercube-slicing.

## What counts as a win

Integer vectors a_i and rational thresholds b_i (equivalently, all integers after scaling), i = 1..k, for some n >= 7. k must be STRICTLY LESS (direction: min) than the best upper bound on S(n) at verification time. On 2026-10-30 that bound is ceil(4n/5), or 4n/5 + 1 for odd multiples of 5, from arXiv:2602.16807; S(n) is known exactly for n <= 6. For EVERY edge {u, v} of Q_n some i must have (a_i.u - b_i)(a_i.v - b_i) < 0, checked over all n 2^(n-1) edges in exact arithmetic. For an odd multiple of 5 this means 4n/5 hyperplanes already win (for example 12 for Q_15, removing the '+1' exception). Any construction with k/n < 4/5 also lowers the asymptotic constant. Re-check the arXiv page, the authors' GitHub repository (results.txt, other-constructions) and any 2026 follow-up first.

## Partial wins

- **p1:** A new S(n,k) record for n >= 7: k hyperplanes (integer normals, rational thresholds) cutting STRICTLY MORE edges of Q_n, counted exactly with a strict sign change, than the value for that (n,k) in Table 1 (n = 7..11, k = 4..10) or Table 2 (n = k+3, k = 9..12) of arXiv:2602.16807, or than any later published record. The cell's current value must be below the total n 2^(n-1).

## How a win is checked

An independent script: read the integer matrix A (k x n) and vector b, enumerate all 2^n vertices, compute A x - b exactly, and for every edge (flip one coordinate) test for a strict sign change in some row. Count the sliced edges and compare with n 2^(n-1). Calibrate on Paterson's 5 planes for Q_6 and the paper's 8 planes for Q_10 (both must slice everything) and on a corrupted plane (must fail). For n up to about 24 this is a direct loop; beyond that use the paper's reduced-cube symmetry argument only if its correctness is re-derived.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2602.16807>

## Sources

- <https://arxiv.org/abs/2602.16807>
- <https://github.com/DSoiffer/upper-bounds-for-hypercube-slicing>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The successful Q_10 solutions fix many coefficients to one common value and the bias to 0.5. Search compositions b = [6,1,1,1,1]-style reduced cubes for Q_11 with 8 planes or Q_7 with 5.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A hyperplane through a vertex does not cut the edge's interior; require strict sign change.
- Floating-point coefficients can hide zeros; use integers (Sauermann-Xu: an integer solution exists whenever a real one does).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/hypercube-edge-slicing-s-n.md
```

Already set up? Say `run V3R1T4S on hypercube-edge-slicing-s-n`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypercube-edge-slicing-s-n`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
