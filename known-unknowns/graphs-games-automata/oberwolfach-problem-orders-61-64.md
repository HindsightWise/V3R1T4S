# Oberwolfach problem: solve every instance OP(F) of order 61 to 64 (verified so far for all orders up to 60)

🕸️ **Graphs, games and automata** · standard · tractability ★★★★☆ · compute: laptop-days (order 59 took about 29 CPU-hours with the published method) · open as of 2026-10-30

## The problem

OP(F), posed by Gerhard Ringel in 1967, asks for a decomposition of K_v (v odd) or K_v minus a perfect matching (v even) into copies of a given 2-regular graph F of order v. The only known non-solvable instances are [3,3], [4,5], [3,3,5] and [3,3,3,3]. Deza, Franek, Hua, Meszka and Rosa (JCMCC 2010) solved all orders up to 40; Salassa, Dragotto, Traetta, Buratti and Della Croce (Australasian J. Combin. 79, 2021; arXiv 1903.12112) solved every instance with at least three cycles for orders 41 to 60 (239,444 instances by their Table 1; their text quotes 241,200, which includes order 40) with 1- and 2-rotational models on a desktop PC, releasing their code (TheOberSolver). Theorems cover uniform F, bipartite F, two-table F (Traetta 2013) and all sufficiently large v (Glock, Joos, Kim, Kuhn and Osthus, JEMS 2021, with an inexplicit bound). Wikipedia's Oberwolfach problem page and the 2023 survey of Burgess, Danziger and Traetta (arXiv 2308.04307) still give the verification for v <= 60. Counting 2-regular graphs with at least three cycles (partitions into at least three parts >= 3; this reproduces the paper's 33,552 at order 60), the next orders have 38,409 (v = 61), 43,974 (62), 50,275 (63) and 57,449 (64) instances. Credit: Ringel; Deza et al.; Salassa et al.; Traetta; Glock et al.

## What counts as a win

Success means, for every 2-regular graph F with at least three cycles and order v in {61, 62, 63, 64}, an explicit solution of OP(F): either the full list of 2-factors, or base 2-factor(s) plus the 1- or 2-rotational group action that the checker expands, such that every expanded factor is isomorphic to F (same multiset of cycle lengths, each a simple cycle), the factors are pairwise edge-disjoint, and together they cover every edge of K_v (v odd) or of K_v minus one perfect matching that is itself checked (v even). The number of instances solved must equal 38,409 / 43,974 / 50,275 / 57,449. Before claiming, re-check the literature for a newer computational extension beyond order 60; orders already published do not count.

## Partial wins

- **p1:** A complete, checked solution set for all instances of one order v in {61, 62, 63, 64}.
- **p2:** Complete, checked solution sets for both orders 61 and 62, extending the verification to all orders up to 62.

## How a win is checked

For each instance expand the stored base factors under the stated group (Z_{v-1} plus a fixed point, or a 2-rotational action), check each factor is a 2-factor with the right cycle type, check pairwise edge-disjointness and full coverage of K_v or K_v - I with a bitset over the C(v,2) edges, and enumerate the partitions independently to confirm coverage. Minutes per order.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Oberwolfach_problem>

## Sources

- <https://arxiv.org/abs/1903.12112>
- <https://github.com/ALCO-PoliTO/TheOberSolver>
- <https://en.wikipedia.org/wiki/Oberwolfach_problem>
- <https://arxiv.org/abs/2308.04307>
- <https://arxiv.org/abs/1806.04644>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reimplement Salassa et al.'s 1-rotational (orders 4t+1, giving 4t+2) and 2-rotational (orders 4t+3, giving 4t) labeling models with an open solver (OR-tools CP-SAT or HiGHS) instead of CPLEX.
- Handle instances without 1-rotational solutions (their Proposition 3.4) with the 2-rotational model for even n.
- Cache sub-labelings: many partitions share all but one or two cycles.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Instances with one or two cycles are settled by theorems and are not part of the count; do not omit any instance with three or more cycles.
- For even v the target graph is K_v minus a perfect matching, not K_v.
- Derived solutions (4t+2 from 4t+1, 4t from 4t-1) must still be expanded and checked explicitly.
- The published code uses IBM CPLEX; a licence is not needed if the models are reimplemented.
- Salassa et al. state 241,200 instances for orders 41-60 although their Table 1 rows for 41-60 sum to 239,444 (the 241,200 includes order 40's 1,756); use your own partition count per order.
- The 2023 survey of Burgess, Danziger and Traetta (arXiv 2308.04307) still gives v <= 60 as the computational bound; re-check for a newer extension before attacking.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/oberwolfach-problem-orders-61-64.md
```

Already set up? Say `run V3R1T4S on oberwolfach-problem-orders-61-64`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `oberwolfach-problem-orders-61-64`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
