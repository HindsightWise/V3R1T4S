# Quadrilateral versus star (and wheel): settle an open value of R(C4, K_{1,n}) such as n = 39 (46-47) or n = 51-54, 71, 72

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (SAT with symmetry breaking on C4-free graphs of 46-82 vertices) · open as of 2026-10-30

## The problem

f(n) = R(C4, K_{1,n}) is the least N such that every graph on N vertices contains a 4-cycle or its complement contains a vertex of degree at least n; for n >= 6 it also equals R(C4, W_{n+1}) (Zhang-Broersma-Chen; Chen-Zhang-Zhang 2025 survey). DS1 revision #18 (Apr 2026) Table IVa gives every value for n <= 41 except 46 <= f(39) <= 47. Luis Boza (arXiv:2409.12770 v2, 12 Jun 2026) settled the eight earlier open values for n <= 38 (f(27) = 33, f(28..33) = n+7, f(37) = 44, plus f(67) = 76) and tabulated f(n) for n <= 82. His table still has ranges at n = 51 (59-60), 52 (60-61), 53 (61-62), 54 (62-63), 71 (80-81) and 72 (81-82), and partly blank entries at n = 39, 42, 44, 46, 56 and 69 (the published TeX omits one side). Monotonicity (f(n) <= f(n+1)), Parsons' bound f(n) <= n + ceil(sqrt(n-1)) + 1 and the neighbouring table values give 49 <= f(42) <= 50, 51 <= f(44) <= 52, 53 <= f(46) <= 54, 64 <= f(56) <= 65 and 78 <= f(69) <= 79, so the open n <= 82 are 39, 42, 44, 46, 51-54, 56, 69, 71 and 72. Credit: Parsons (polarity graphs), Boza, Wu-Sun-Radziszowski, Wu-Sun-Zhang-Radziszowski, Zhang-Chen-Cheng, Dybizbanski-Dzido, Tse, Noviani-Baskoro.

## What counts as a win

For one open n: either (a) an explicit C4-free graph G on N vertices whose complement has maximum degree at most n-1 (equivalently min degree of G at least N-n), proving f(n) >= N+1, with N+1 STRICTLY GREATER (direction: max) than the best lower bound in DS1 Table IVa, Boza's table (arXiv:2409.12770, latest version) and any newer paper; or (b) a proof that no such graph exists on N vertices, giving f(n) <= N STRICTLY BELOW (direction: min) the best published upper bound, certified by a DRAT/LRAT UNSAT proof of a stated encoding (any degree or symmetry reductions proved sound and checkable) that a referee regenerates and checks. Bounds implied by monotonicity f(n) <= f(n+1) and by Parsons' f(n) <= n + ceil(sqrt(n-1)) + 1 (the ranges listed in the statement) count as published. A matching pair settles f(n).

## Partial wins

- **p1:** Settle f(39): either a C4-free graph on 46 vertices with minimum degree at least 7, or a certified UNSAT proof that none exists (giving f(39) = 47 or 46 respectively).
- **p2:** Settle one of the cells that Boza's table leaves one-sided: f(42) (49-50), f(44) (51-52), f(46) (53-54), f(56) (64-65) or f(69) (78-79), with a verified graph or a certified UNSAT proof as in the main criterion.

## How a win is checked

C4-freeness: compute A^2 and check that every off-diagonal entry is at most 1 (two independent implementations: numpy matrix product and a common-neighbour bitset count). Check min degree. For UNSAT claims, check the proof with drat-trim or cake_lpr and re-derive the CNF from the stated parameters; reject unproved symmetry-breaking constraints.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2409.12770>

## Sources

- <https://arxiv.org/abs/2409.12770>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://users.cecs.anu.edu.au/~bdm/data/extremal.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lower bounds near q^2+q+1 come from Erdos-Renyi polarity graphs ER_q with vertices deleted or added; f(51..54) sit just above q = 7 (57 vertices).
- Afzaly-McKay's ex(n,C4) tables bound the edge count: a graph on N vertices with min degree N-n needs N(N-n)/2 edges, which must not exceed ex(N,C4).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Boza's table in the arXiv TeX has missing glyphs (e.g. '/46' at n = 39); take bounds from the text, DS1 and the cited papers, not the rendered cell.
- Wheel indexing differs between papers (W_n with n or n+1 vertices).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/c4-versus-star-ramsey-open-values.md
```

Already set up? Say `run V3R1T4S on c4-versus-star-ramsey-open-values`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `c4-versus-star-ramsey-open-values`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
