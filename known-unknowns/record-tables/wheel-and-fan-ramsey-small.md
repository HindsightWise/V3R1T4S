# Wheels and fans: close a gap in DS1 Table VIII (R(W7,W8) 19-21, R(W8,W8) 22-25, R(W4,W8) 22-26, ...) or R(F4,F4) 18-24

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for lower bounds (block-circulant SAT on 18-30 vertices); flag algebras or SAT for upper bounds · open as of 2026-10-30

## The problem

W_n = K_1 + C_{n-1} is the wheel on n vertices and F_n = K_1 + nK_2 the fan of n triangles. DS1 revision #18 (Apr 2026) Table VIII gives R(W_m,W_n) for m <= n <= 10. Open cells: R(W4,W8) 22-26, R(W6,W8) 22-26, R(W7,W8) 19-21, R(W8,W8) 22-25, and lower-only cells R(W4,W9) >= 25, R(W5,W10) >= 21, R(W6,W9) >= 25, R(W7,W9) >= 19, R(W7,W10) >= 21, R(W8,W9) >= 25, R(W9,W9) >= 21, R(W10,W10) >= 28. For fans, Table X shows only R(F4,F4) <= 28. But Lin and Li's R(F_n,F_n) <= 6n (DS1 item 5.7.b) already gives 24, and Zhang and Chen (arXiv:2604.13850, Theorem 3) give R(F4,F4) >= 18, so 18 <= R(F4,F4) <= 24. Jiang and Shao proved R(F3,F4) = 17 (arXiv:2610.26109). Recent general bounds (Li-Kashima-Mao 2026, DeBiasio-Wimbish 2026, Zhang-Chen 2026) move no two-sided wheel cell. For the lower-only diagonal cells they give the only upper bounds, e.g. R(W9,W9) <= 36 and R(W10,W10) <= 50 (Zhang-Chen; Li-Kashima-Mao give 37 and 54). Bereg (Mathematics 14 (2026) 2310) reports three new off-diagonal wheel lower bounds. Credit: Van Overberghe, Lidicky-Pfender, Lidicky-McKinley-Pfender-Van Overberghe (R(W5,W7) = 15, R(W5,W9) = 18), Wesley, Faudree-McKay, Hendry, Harborth-Mengersen, Lin-Li, Zhang-Chen, Jiang-Shao, Bereg.

## What counts as a win

Either (a) an explicit graph G on N vertices with no W_m (resp. F_m) and whose complement has no W_n (resp. F_n), subgraphs not necessarily induced, checked by two independent exact programs, with N+1 STRICTLY GREATER (direction: max) than the lower bound in the live DS1 tables and any newer paper; or (b) an upper bound STRICTLY BELOW (direction: min) the DS1 upper bound for a cell with one, certified by an exact-rational flag-algebra certificate or a DRAT/LRAT UNSAT proof with a checkable reduction. Off-by-one: a graph on N vertices proves R >= N+1.

## Partial wins

- **p1:** A first upper bound below the general-formula bound for one lower-only cell of Table VIII (e.g. R(W9,W9) or R(W10,W10)), certified as in (b), strictly below every bound in DS1, Li-Kashima-Mao (arXiv:2605.22116), Zhang-Chen (arXiv:2604.13850), DeBiasio-Wimbish (arXiv:2604.11937) and any newer paper.
- **p2:** R(F4,F4) improved on either side: a verified graph on 18 or more vertices with no F4 in it or its complement (giving >= 19), or a certified proof that R(F4,F4) <= 23.

## How a win is checked

W_n-freeness: for each vertex v, test whether G[N(v)] contains a cycle C_{n-1} (exact DFS over the neighbourhood, at most 10 vertices deep), cross-checked by a SAT encoding. F_n-freeness: for each v, compute the maximum matching of G[N(v)] (blossom algorithm, e.g. networkx) and require it to be below n. Run on G and the complement; check certificates with drat-trim or an exact SDP checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://arxiv.org/abs/2407.07285>
- <https://arxiv.org/abs/2610.26109>
- <https://arxiv.org/abs/2605.22116>
- <https://arxiv.org/abs/2604.13850>
- <https://arxiv.org/abs/2603.27110>
- <https://arxiv.org/abs/2604.11937>
- <https://doi.org/10.3390/math14132310>
- <https://github.com/Steven-VO/circulant-Ramsey>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Some papers define W_n = K_1 + C_n with n+1 vertices; DS1 uses n vertices.
- R(F3,F4) = 17 is now settled (Jiang-Shao 2026); DS1 still shows that cell blank.
- DS1 Table X still prints R(F4,F4) <= 28 with no lower bound; the live range is 18-24 (Lin-Li upper bound 6n, Zhang-Chen lower bound 18).
- Bereg, Computational Lower Bounds for Wheel Ramsey Numbers, Mathematics 14(13) (2026) 2310, gives three new off-diagonal wheel lower bounds with explicit certificate graphs (reported to be at n = 11, outside Table VIII); read it before claiming any wheel cell.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/wheel-and-fan-ramsey-small.md
```

Already set up? Say `run V3R1T4S on wheel-and-fan-ramsey-small`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wheel-and-fan-ramsey-small`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
