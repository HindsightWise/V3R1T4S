# Orchard planting: more 3-point or 4-point lines among n points than the best known (3 per row for n >= 17, 4 per row for n >= 21)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (incidence search plus exact realisation; checks take seconds) · open as of 2026-10-30

## The problem

t3(n) is the largest number of lines containing exactly 3 of n points in the real plane (OEIS A003035, Erdős #669); t4(n) is the same with exactly 4 points (OEIS A006065). t3 is known exactly for n <= 16 (t3(16) = 37; a(15) = 31 added by Zhao Hui Du, 29 Sep 2026). t3(17) is 40, 41 or 42 (OEIS). Best known t3 for n = 18..25 (Friedman's table, MathWorld): 46, 52, 57, 64, 70, 77, 85, 92, against upper bounds 48, 54, 60, 67, 73, 81, 88, 96. Burr-Grünbaum-Sloane give floor(n(n-3)/6)+1, which Green and Tao proved exact for all large n; some small n beat it (n = 7, 11, 16, 19). t4 is known exactly up to n = 20 (t4(20) = 23; Zhao Hui Du, 2008-2010, with Xianzu Lin's 2005 construction). Best known real lower bounds for t4 at n = 21..25: 24, 28, 28, 30, 32 (emathgroup table, Dec 2019; Friedman still lists 26 for n = 22). Upper bounds for t4 at n = 21..25: Friedman lists 31, 38, 40, 42, 50; the emathgroup page quotes floor((n+2)(n-3)/14) (credited to shengjianguo, from a book by Shan Zun), giving 29, 32, 35, 39, 42. Credit: Burr, Grünbaum, Sloane, Zhao Hui Du, Ed Pegg Jr, Erich Friedman, Xianzu Lin, Grünbaum-Rigby, and the emath forum.

## What counts as a win

n distinct points in the real affine plane with exact coordinates (rationals or elements of a stated number field; a projective configuration must be moved to affine coordinates first) such that the number L of lines containing EXACTLY k of the points (k = 3 with n >= 17, or k = 4 with n >= 21) is STRICTLY GREATER (direction: max) than the best known value for that (n, k) at verification time. The best known value is the maximum over: the live OEIS A003035 or A006065 data, comments and linked illustrations (including Pegg's constructions for 9 to 28 trees); for k = 4, OEIS A172992 (integer coordinates, so also a real lower bound) and its formula floor((n^2+12)/28) for n >= 28; the emathgroup orchard page; Friedman's table; MathWorld's Orchard-Planting page; and a fresh check. For k = 3 the best known value is never below the Burr-Grünbaum-Sloane count floor(n(n-3)/6)+1. L is counted exactly by two independent implementations.

## Partial wins

- **p1:** A reproducible exhaustive computation, with published code and a certificate for every eliminated case (a DRAT proof for the combinatorial part, and exact Gröbner or Nullstellensatz certificates for non-realisability), that settles t3(17) or proves t3(17) <= 41.
- **p2:** A reproducible certified proof of an upper bound on t4(n) for some 21 <= n <= 25 that is strictly below both Friedman's listed upper bound and floor((n+2)(n-3)/14) at verification time.
- **p3:** A configuration on integer coordinates for some 16 <= n <= 25 with strictly more exactly-4-point lines than the best integer-coordinate value in OEIS A172992 or the emathgroup table at verification time, counted exactly. No integer-coordinate table exists for 3 per row, so k = 3 does not count here.

## How a win is checked

Check all points are distinct. For every pair, compute the line exactly; group points by line using a canonical normalised integer or number-field representation; count lines with exactly k points. Cross-check with a brute-force collinearity test over all triples (and 4-sets for k = 4) using exact determinants. Re-fetch the OEIS entries, the emathgroup table and Friedman's page, and record the best value with fetch times.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A003035>

## Sources

- <https://oeis.org/A003035>
- <https://oeis.org/A006065>
- <https://oeis.org/A172992>
- <https://emathgroup.github.io/blog/orchard-planting-problem>
- <https://erich-friedman.github.io/packing/trees/>
- <https://mathworld.wolfram.com/Orchard-PlantingProblem.html>
- <https://www.erdosproblems.com/669>
- <https://arxiv.org/abs/1208.4714>
- <https://blog.wolfram.com/2018/02/02/cultivating-new-solutions-for-the-orchard-planting-problem/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Cubic-curve constructions: points on an elliptic curve (or a cubic) with group-law collinearity give floor(n(n-3)/6)+1. The sporadic winners (n = 7, 11, 16, 19) come from extra coincidences, so search small configurations with high symmetry (dihedral, 3-fold) for extra triple lines.
- Combinatorial first: enumerate linear spaces / partial Steiner triple systems with the target number of triples, then solve the realisability equations exactly (Gröbner bases), as Du did for 4-per-row.
- Pegg's 2018 method: take the n = 16 and 19 sporadic configurations, add points at triple intersections of existing lines, and re-optimise.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Counting lines with AT LEAST k points instead of EXACTLY k (A008997 and A003035 differ).
- Points at infinity in published pictures (the n = 16 drawing has 3 points and one line at infinity); count them after a projective map.
- Floating-point collinearity; near-collinear triples are common in optimised configurations.
- Friedman's table is older than OEIS for some cells (it still shows 13-15 as ranges); always take the maximum over sources.
- Complex-coordinate records in the emathgroup table do not count; the real plane is required.
- For n beyond the tables (k = 3 with n >= 26, k = 4 with n >= 26), compare with the Burr-Grünbaum-Sloane count and A172992; they are strong, and Green-Tao show the 3-per-row count is exact for all large n.
- Zhao Hui Du's newest exhaustive results are posted on the emath forum (bbs.emath.ac.cn, thread-50366 for 3 per row). On 2026-10-30 it showed a bot check to an automated fetch. A human must check it before a t3(17) claim; do not get around the check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/orchard-planting-small-n-records.md
```

Already set up? Say `run V3R1T4S on orchard-planting-small-n-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `orchard-planting-small-n-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
