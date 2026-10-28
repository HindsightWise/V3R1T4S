# Hales-Jewett numbers: beat HJ(3,3) >= 22 or HJ(4,2) >= 14 with an explicit line-free colouring

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

HJ(t,r) is the least n such that every r-colouring of the grid [t]^n contains a monochromatic combinatorial line. Younes Mouhib (arXiv:2606.22155, v2 24 Jul 2026) raised HJ(3,3) >= 22 (previous record 14) and HJ(4,2) >= 14 (previous record 12) using colourings that are invariant under coordinate permutations, so a colouring depends only on the letter-count vector; certificates are in the GitHub repository ysmouhib/hj-certificates. The same paper reports new Gallai and Rado numbers and lists open cells such as G_4({0,1,3}) >= 94. Exact values are known only for tiny cases (HJ(2,r)=r, HJ(3,2)=4). Find an explicit line-free colouring of [t]^n for some small (t,r) with n at or above the current record, i.e. proving HJ(t,r) > n with n strictly larger than the best known lower bound minus one.

## What counts as a win

Success means an explicit r-colouring of [t]^n (given as a full table, or as a function of the letter-count vector if it is symmetric) with no monochromatic combinatorial line, verified by two independent checkers, proving HJ(t,r) >= n+1, where n+1 is STRICTLY GREATER (direction: max) than the best lower bound for that (t,r) at verification time: the maximum over the latest version of https://arxiv.org/abs/2606.22155 re-fetched live immediately before claiming, the ysmouhib/hj-certificates repository, and a fresh arXiv search for 'Hales-Jewett' lower bounds over the last 24 months. Bounds that only hold for a restricted line family (bracket, q-fold or interval lines) do not count.

## Partial wins

- **p1:** A new exact or improved Gallai number listed as open in arXiv:2606.22155 (for example a 4-colouring of a window of length 94 or more with no monochromatic homothet of {0,1,3}, beating G_4({0,1,3}) >= 94), verified by exhaustive homothet enumeration.
- **p2:** An improved lower bound for some other small Hales-Jewett cell (for example HJ(3,4), HJ(4,3) or HJ(5,2)) beating both the van der Waerden shadow bound and any value in arXiv:2606.22155 and a fresh search, with an explicit checked colouring.

## How a win is checked

For symmetric colourings: a combinatorial line in [t]^n with active set size m and fixed part having letter counts v corresponds to the t letter-count vectors v + m*e_i; enumerate all (v,m) pairs with m >= 1 and |v|+m = n and check that the t colours are not all equal. Cross-check this reduction on n <= 6 against brute force over all lines of the full grid ((t+1)^n - t^n lines). For non-symmetric colourings, brute force over all lines (feasible for [4]^13, about 1.2e9 lines, in C on a laptop). Two independent implementations must agree. Then re-fetch arXiv:2606.22155 and search arXiv for newer records.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2606.22155>

## Sources

- <https://arxiv.org/abs/2606.22155>
- <https://github.com/ysmouhib/hj-certificates>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search the symmetric (equivalently one-weight) class directly with SAT: variables are colours of the letter-count simplex points, clauses forbid monochromatic corner tuples v+m*e_i. For (3,3) at n=22 this is about 276 cells, tiny for CaDiCaL. The paper proves the symmetric class equals the one-weight class, so check its results tables and SAT logs for which cells it already exhausted before repeating a search.
- Go beyond symmetry: colourings invariant under a smaller group (for example S_a x S_b acting on two blocks of coordinates) give a two-simplex reduction with more freedom; encode lines across the blocks and SAT-solve.
- From additive combinatorics: one-weight colourings reduce to Gallai homothety problems in Z. Import Behrend-style and Rankin-type constructions for sets free of homothets of {0,1,2} or {0,2,3,5}, then lift.
- From coding theory: treat a colour class as a code in [t]^n avoiding lines (a cap-set-like condition). Use known large line-free sets (density Hales-Jewett constructions, Polymath DHJ(3) data) as colour classes and complete the rest with SAT.
- Cube-and-conquer over 10 cores on the symmetric encoding for (3,3) at n=22 and (4,2) at n=14, splitting on the colours of the simplex corners.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A colouring that is line-free only for a restricted line family (bracket lines, q-fold lines, interval lines) gives no bound on HJ(t,r). Check all combinatorial lines.
- Off-by-one: a line-free colouring of [t]^n proves HJ(t,r) >= n+1. Matching the record dimension is not an improvement.
- Trusting the symmetric reduction without testing it: cross-check the corner-tuple checker against brute force on small n, since an indexing bug silently drops lines.
- The records are from one recent single-author preprint. Re-check its certificates yourself and search for any correction or newer version before taking its numbers as the baseline.
- Confusing combinatorial lines with geometric lines (which also include reversed coordinates). The Hales-Jewett number uses combinatorial lines only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/hales-jewett-small-lower-bounds.md
```

Already set up? Say `run V3R1T4S on hales-jewett-small-lower-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hales-jewett-small-lower-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
