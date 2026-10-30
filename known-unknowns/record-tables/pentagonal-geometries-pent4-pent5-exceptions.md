# Pentagonal geometries: construct PENT(4,r) for r in {8,12,16,28,32,36,44,48,56,64,72} or PENT(5,r) for r in {11,16,66,96,116}

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (SAT on 29-50 point cases) · open as of 2026-10-30

## The problem

A pentagonal geometry PENT(k,r) (Ball, Bamberg, Devillers and Stokes) is a partial linear space with k points on each line and r lines through each point, in which for every point x the points not collinear with x form a line (the opposite line of x). It has rk - r + k + 1 points and (rk - r + k + 1)r/k lines, so k must divide r(r-1). For k = 4, A. D. Forbes, T. S. Griggs and K. Stokes (Australas. J. Combin. 82 (2022); arXiv:2007.10810, Theorem 4.2 with Theorem 4.1) proved that PENT(4,r) exists for all r = 0 or 1 (mod 4) except r = 4 and 5, and except possibly r in {8, 12, 16, 28, 32, 36, 44, 48, 56, 64, 72}. For k = 5 and r = 1 (mod 5), Forbes and C. G. Rutherford (La Matematica 2024; arXiv:2111.13599v3, Theorem 5.1, a small improvement on T. S. Griggs and K. Stokes, Springer Proc. Math. Stat. 159 (2016), Theorem 12) proved existence except r = 6 and possibly r in {11, 16, 66, 96, 116}. The smallest open case, PENT(4,8), has 29 points and 58 lines; PENT(4,12) has 41 points and 123 lines; PENT(5,11) has 50 points and 110 lines. PENT(k,k) exists only for k = 2, 3, 7 and possibly 57; that case is tied to a Moore graph of degree 57 and is excluded here.

## What counts as a win

Success means an explicit PENT(k,r) for (k,r) in {(4,8), (4,12), (4,16), (4,28), (4,32), (4,36), (4,44), (4,48), (4,56), (4,64), (4,72), (5,11), (5,16), (5,66), (5,96), (5,116)}. It must have v = rk - r + k + 1 points and vr/k lines, each a k-subset; every point must lie on exactly r lines and any two points on at most one line. For every point x, the set of points other than x not collinear with x must be exactly one of the lines. Two independent programs must verify it. At claim time the case must still be listed as a possible exception, checked by a fresh literature search for PENT(4,r) and PENT(5,r), including Forbes' ORCID and arXiv lists.

## Partial wins

- **p1:** A machine-checked non-existence proof for one listed case (PENT(4,8) on 29 points is the natural first target), with a DRAT/LRAT certificate from an audited encoding, re-verified independently.
- **p2:** A type-A PENT(5,r) (connected deficiency graph of girth at least 5) for some admissible r not in the published lists of known type-A PENT(5,r) (r in {20,25,30,35,40} from Forbes 2021 and {21,26,31,36,41,45} from Forbes-Rutherford 2024), verified by two programs including the girth and connectivity of the non-collinearity graph.

## How a win is checked

Parse the lines. Check the point and line counts, line sizes, point degrees r and pairwise line intersections of at most 1. For each point x, compute the set of points not collinear with x and confirm it equals a line of the geometry. For p2, also compute the deficiency (non-collinearity) graph and check that it is connected with girth at least 5. Two independent checkers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2111.13599>

## Sources

- <https://arxiv.org/abs/2007.10810>
- <https://ajc.maths.uq.edu.au/pdf/82/ajc_v82_p095.pdf>
- <https://arxiv.org/abs/2111.13599>
- <https://arxiv.org/abs/2006.15734>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Forbes' examples are cyclic: points Z_v, lines developed from base lines under x -> x + d. Search PENT(4,8) on Z_29 and PENT(4,12) on Z_41 with SAT, then try non-cyclic groups.
- The deficiency graph is a disjoint union of K_{k,k} pieces (opposite line pairs) and a k-regular graph of girth at least 5. Enumerate candidate deficiency graphs first, then complete the remaining pairs to a linear structure.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- PENT(4,4), PENT(4,5) and PENT(5,6) are proven not to exist; they are not open.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/pentagonal-geometries-pent4-pent5-exceptions.md
```

Already set up? Say `run V3R1T4S on pentagonal-geometries-pent4-pent5-exceptions`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pentagonal-geometries-pent4-pent5-exceptions`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
