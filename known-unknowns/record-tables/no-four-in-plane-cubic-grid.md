# No four in a plane: more points in the n x n x n grid with no four coplanar than the best known (OEIS A280537, AZsPCs 2016)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (local search or SAT; exact checking is O(N^4) integer determinants, seconds) · open as of 2026-10-30

## The problem

a(n) is the largest number of points of the n x n x n integer grid with no four in a common plane (OEIS A280537, Hugo Pfoertner). Exhaustive search settles n <= 6 (5, 8, 10, 13, 16 for n = 2..6; Möhres for n = 6); a(7) = 18 and a(8) = 20 rest only on numerical evidence. Best known lower bounds: 9: 23, 10: 26, 11: 28, 12: 31 (Aleksei Kudriashov, Aug 2026), 13: 32, 14: 35, 15: 36, 16: 38, 17: 42, 18: 43 (OEIS comments and the linked configuration file by Franckenstein, Kudriashov and Pfoertner). Al Zimmermann's closed 2016 contest 'Non-Coplanar Points' (prime n up to 97; score = points squared; best solutions published in the final report) ended with 19: 46, 23: 54, 29: 66, 31: 71, 37: 81, 41: 89, 43: 92, 47: 100, 53: 110, 59: 121, 61: 125, 67: 137, 71: 142, 73: 145, 79: 157, 83: 164, 89: 173, 97: 188, all by Tim Foden (Jarek Wroblewski tied at 19; other contestants include Rokicki, Sirgedas, Sigg and Franckenstein). Kudriashov, arXiv:2609.25133 (v1, 20 Sep 2026), with public configurations at github.com/iwasborninbali/saturation (certs/a280537_first_solver), also gives 21: 47, 22: 49 and 27: 56; these appear in OEIS revisions #19-28 but not in the approved entry. Se Young Park proposed a 58-point configuration for n = 28 in OEIS revisions #44-50 (27 Oct 2026). After an objection from Pfoertner, the approved revision #52 carries neither the comment nor the link, but the file oeis.org/A280537/a280537_5.txt is still served, and its 58 points check out. Trivially a(n) <= 3n, a(n) >= a(m) for m < n, and a(n) >= a(m) - 9(m - n) for m > n (delete boundary slices, each holding at most 3 points).

## What counts as a win

A set of distinct integer points in {0,...,n-1}^3 for some n >= 7 with no four coplanar, checked exactly by two independent implementations, whose size is STRICTLY GREATER (direction: max) than the best known value B(n) at verification time. B(n) is the maximum of three values. (i) Every value listed for any m <= n on the live OEIS A280537 page, in its revisions (oeis.org/history?seq=A280537) and in its linked or still-served files (including a280537_5.txt), in Kudriashov's arXiv:2609.25133 and its GitHub configurations, and in the AZsPCs Non-Coplanar Points final report (points = square root of the score). On 2026-10-30 this gives, for example, 21: 47, 22: 49, 27: 56 and 28: 58. (ii) For every published configuration with m > n (the OEIS files, Park's n = 28 file, Kudriashov's GitHub configurations, the AZsPCs report), the largest number of its points inside any n x n x n sub-box, and at least a(m) - 9(m - n) for listed values whose configuration is not public. (iii) A fresh check. For n = 7 or 8, a set beating 18 or 20 also counts, since those values are not proved.

## Partial wins

- **p1:** A reproducible exhaustive computation, with published code and a DRAT/LRAT certificate or an independent second run, that determines a(7) or a(8) exactly.
- **p2:** A certified proof (for example, a DRAT-checked UNSAT result with an independently re-derived encoding) that a(n) <= 3n - 1 for some n >= 7.

## How a win is checked

Check that coordinates are in range and distinct. For every 4-subset compute the 3x3 determinant of difference vectors with exact integers and require it nonzero. Faster cross-check: for every triple, compute the plane's primitive normal and offset, hash, and require each plane to hold at most 3 points. Re-fetch the OEIS page, history and the AZsPCs final report, and record the best value for each m <= n.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A280537>

## Sources

- <https://oeis.org/A280537>
- <https://oeis.org/history?seq=A280537>
- <https://oeis.org/A280537/a280537_4.txt>
- <https://oeis.org/A280537/a280537_5.txt>
- <https://arxiv.org/abs/2609.25133>
- <https://github.com/iwasborninbali/saturation>
- <http://azspcs.com/Contest/Tetrahedra/FinalReport>
- <http://azspcs.com/Contest/Tetrahedra>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Composite n with no direct record (20, 24-26, 30, 32-36, ...) have only the monotone bound from the nearest smaller record (20: 46 from n = 19; 24-26: 54 from n = 23; 30: 66 from n = 29); a direct search there is the cheapest record. n = 21, 22, 27 and 28 already have direct records (47, 49, 56, 58).
- Algebraic seeds: points on the twisted cubic (t, t^2, t^3) mod p have no four coplanar over F_p; lift or crop them into the integer grid and repair with local search.
- SAT with one variable per grid point and at-most-3 cardinality constraints per plane, restricted to a symmetry class (point reflection through the centre, or a 3-fold rotation about the main diagonal; Kudriashov's records are invariant under (x,y,z) -> (y,z,x)).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Checking only axis-parallel or small-normal planes; every plane through three grid points matters.
- Off-by-one: the n x n x n grid is coordinates 0..n-1.
- Comparing only with the approved OEIS text; the AZsPCs report and the OEIS revision history hold the records for n >= 19.
- Monotonicity works both ways: a record for n must beat the best value at every m <= n and every crop of a published configuration for m > n.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/no-four-in-plane-cubic-grid.md
```

Already set up? Say `run V3R1T4S on no-four-in-plane-cubic-grid`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `no-four-in-plane-cubic-grid`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
