# Distinct distances in a lattice square (Erdős-Guy 'Golomb square'): n points with all distances distinct in a smaller k x k grid than known, n = 15..26

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (search; verifying a configuration is instant, exhaustive lower bounds laptop-days) · open as of 2026-10-30

## The problem

A193838(n) is the smallest k such that n points can be chosen from the k x k grid of lattice points with all C(n,2) mutual distances distinct (Erdős and Guy 1970; context of Erdős Problem #1208; inverse sequence A271490). Exact values are known for n <= 14: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 18 (a(12) Sean A. Irvine 2020, a(13) Bert Dobbelaere 2020, a(14) = 18 Fausto A. C. Cariboni 2022). Best known upper bounds: a(15) <= 20, a(16) <= 22, a(17) <= 24, a(18) <= 27 (Cariboni, July 2022), and a(19) <= 29, a(20) <= 33, a(21) <= 36, a(22) <= 37, a(23) <= 40, a(24) <= 43, a(25) <= 46, a(26) <= 49 (Dmitry Kamenetsky, 2021, from Al Zimmermann's 2009 Point Packing contest results, won by Hugo Pfoertner and Hermann Jurksch). The entry was last revised 30 May 2026 with no change to these bounds.

## What counts as a win

(A) n distinct integer points (15 <= n <= 26) with coordinates in {0,...,k-1}^2 whose C(n,2) squared distances are pairwise distinct (exact integers), where k is STRICTLY LESS (direction: min) than the best known upper bound for a(n) at verification time. That bound is the minimum over the live OEIS A193838 and A271490 pages (comments, links and history), the bounding boxes of the solutions in the AZsPCs Point Packing final report, and a fresh check. Or (B), for some n in 15..18, an exhaustive computation that settles a(n) exactly, published with code and reproduced by an independent implementation. It must exhibit a solution in the k x k grid and prove that none fits in the (k-1) x (k-1) grid.

## Partial wins

- **p1:** A reproducible exhaustive computation, confirmed by two independent programs, that settles whether 15 points with pairwise distinct distances fit in the 18 x 18 grid. A fit would itself be a main win; a proof that none fits gives a(15) >= 19.
- **p2:** An independent from-scratch exhaustive replay confirming a(14) = 18 (no 14-point solution in the 17 x 17 grid), published as a replay note.

## How a win is checked

Translate the points so the minimum coordinates are 0; the grid size is max(coordinate range) + 1. Compute all squared distances with integers and check that there are no duplicates. For exhaustive claims, rerun the published search and a second implementation (for example, a SAT or ILP model with symmetry breaking) and compare node counts or UNSAT certificates. Re-fetch the OEIS pages.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A193838>

## Sources

- <https://oeis.org/A193838>
- <https://oeis.org/A271490>
- <https://www.erdosproblems.com/1208>
- <http://azspcs.com/Contest/PointPacking/FinalReport>
- <https://doi.org/10.5169/seals-27359>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Backtracking with incremental distance sets (bitsets over squared distances up to 2(k-1)^2), D4 symmetry breaking on the first point, and ordering by most-constrained cell.
- For n = 19..26 the bounds come from a 2009 contest and look loose (a(20) <= 33 versus a(19) <= 29): simulated annealing or tabu search on the number of repeated distances, then exact repair.
- Sums of two squares: squared distances are restricted to integers that are sums of two squares, so collisions concentrate on numbers with many representations; penalise those differences.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Off-by-one: a k x k grid has coordinates 0..k-1, so a set spanning 0..16 needs k = 17.
- Comparing distances in floating point; use squared integer distances.
- Older OEIS comments list weaker bounds for a(15)..a(18); Cariboni's 2022 values are the records.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/golomb-square-grid-distinct-distances.md
```

Already set up? Say `run V3R1T4S on golomb-square-grid-distinct-distances`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `golomb-square-grid-distinct-distances`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
