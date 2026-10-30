# KnotInfo stick numbers: a polygon with fewer edges than the best known for a prime knot up to 13 crossings, or a 9-stick realisation of a knot listed [9,10]

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (simulated annealing over polygons; checks take seconds) · open as of 2026-10-30

## The problem

The stick number (KnotInfo field polygon_index) of a knot K is the fewest straight edges in a closed polygon of type K. KnotInfo (Charles Livingston and Allison Moore, knotinfo.org) lists it for all prime knots up to 13 crossings. The data through 9 crossings comes from Cromwell, Calvo, Negami and Randell. Calvo's classification of the knots with at most 8 sticks gives the lower bound 9 for every other knot. The upper bounds for all knots through 13 crossings come from Cantarella, Rechnitzer, Schumacher and Shonkwiler, 'New upper bounds for stick numbers' (arXiv:2508.18263, JKTR 35 (2026) 2650008). They found low-stick polygons by simulated annealing with moves that preserve knot type, building on Eddy and Shonkwiler's random sampling (arXiv:1909.00917). In database_knotinfo 2026.10.5, 12,910 of the 12,965 prime knots have interval-valued stick numbers. Of these, 513 are [9,10], including every 8-crossing knot except 8_16-8_21 and most 9-crossing knots, e.g. 8_1, 9_1, 9_10. The rest include 1,134 12-crossing knots at [9,11], 6,107 13-crossing knots at [9,12] and 877 at [9,13]. Can an explicit polygon close an interval, or beat a listed upper bound?

## What counts as a win

For a prime knot K whose polygon_index is an interval [a,b] in the live KnotInfo database (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site), re-fetched immediately before claiming: a closed polygon with n vertices, given as exact rational coordinates. It must be in general position: no three consecutive vertices collinear, and non-adjacent edges disjoint, both checked in exact arithmetic. Its knot type, read off a regular projection as a PD code, must be identified as K (or its mirror) by SnapPy and Regina. n must equal a, which closes the interval (e.g. a 9-stick polygon for a knot listed [9,10]).

## Partial wins

- **p1:** For any interval-valued knot, a polygon verified the same way with n STRICTLY LESS than the listed upper bound b and than the bound in arXiv:2508.18263's table (direction: min), even if n > a.
- **p2:** A demonstrated table inconsistency: a polygon whose verified knot type contradicts a KnotInfo entry, e.g. an n-stick realisation of a knot whose listed lower bound exceeds n, with the coordinates saved.

## How a win is checked

Skeptic loads the rational coordinates, checks general position exactly, projects along a generic rational direction to get a PD code, and identifies the knot with SnapPy (identify(), plus a verified isometry for hyperbolic knots) and Regina. The edge count is the vertex count. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/polygon_index.html>

## Sources

- <https://knotinfo.org/descriptions/polygon_index.html>
- <https://arxiv.org/abs/2508.18263>
- <https://arxiv.org/abs/1909.00917>
- <https://github.com/soehms/database_knotinfo>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: start from the arXiv:2508.18263 polygons and run annealing at the target edge count with crankshaft and pivot moves, rejecting moves that change knot type (fast checks with HOMFLY or a hyperbolic volume).
- Conventional: search for 9-stick knots with the Eddy-Shonkwiler confined-polygon sampler, targeted with importance weights at the remaining [9,10] types.
- Cross-domain import (protein folding / molecular conformations): treat edges as rigid bonds and run parallel tempering on vertex positions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point coordinates can hide a self-intersection. Rationalise them and recheck exactly before identifying the knot.
- Knots listed [9,10] have survived heavy 9-gon sampling by Eddy and Shonkwiler and by Cantarella et al. Expect long odds there, and record negative runs.
- Check arXiv:2508.18263 and any newer preprint for the current upper bound. KnotInfo may lag behind a paper.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-stick-number-bounds.md
```

Already set up? Say `run V3R1T4S on knotinfo-stick-number-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-stick-number-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
