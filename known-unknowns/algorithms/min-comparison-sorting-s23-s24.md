# Minimum-comparison sorting: settle S(23) in {75, 76} or S(24) in {80, 81} (OEIS A036604), or raise the n = 28 lower bound

⚡ **Algorithms** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster (Stober-Weiss needed 89 h on 48 threads with 768 GB RAM for n = 18; n = 23 is harder); certificate replay similar · open as of 2026-10-30

## The problem

S(n) is the minimum worst-case number of pairwise comparisons that suffices to sort n distinct elements (Knuth TAOCP 5.3.1; OEIS A036604). The information-theoretic bound gives S(n) >= ceil(log2 n!), and Ford-Johnson merge insertion gives the upper bound F(n) (A001768); Peczarski (IPL 2007) showed no split-and-merge algorithm beats it for n < 47, and whether any algorithm beats it for some n < 47 is open. S(n) is known for n <= 22: Wells (n = 12), Kasai-Sawato-Iwata and independently Peczarski (13), Peczarski (14, 22), Cheng-Liu-Wang-Liu (15, 19), and Florian Stober and Armin Weiss (ALENEX 2023, arXiv:2206.05597), who proved S(16) = 46, S(17) = 50, S(18) = 54 with a bidirectional poset search and also showed that 28 elements cannot be sorted with 98 comparisons. Open cells (information bound, or the Stober-Weiss bound for n = 28, to F(n)): S(23) in {75, 76}, S(24) in {80, 81}, S(25) in {84, 85, 86}, S(26) in {89, 90, 91}, S(27) in {94, 95, 96}, S(28) in {99, 100, 101}. Stober and Weiss wrote that for n >= 23 the value of S(n) is still a wide open question and that S(23) and S(24) look computable with improved methods. OPEN as of 2026-10-30: OEIS A036604 (last edited 5 Nov 2025) lists terms only to n = 22; their code repository (CodeCrafter47/sortinglowerbounds) was last changed Feb 2024.

## What counts as a win

Success means one of: (a) a proof that 23 elements cannot be sorted with 75 comparisons (so S(23) = 76) or that 24 elements cannot be sorted with 80 (S(24) = 81), delivered as an exhaustive-search result with released code and a certificate (the set of posets shown unsortable with their remaining budgets) that an independent re-implementation re-derives; or (b) an explicit comparison strategy sorting 23 elements in 75 comparisons or 24 in 80 (STRICTLY BETTER than Ford-Johnson, direction: min), given as a decision table over poset isomorphism classes and checked to reach a total order on every branch within the budget. Either must improve on OEIS A036604 and the literature at claim time.

## Partial wins

- **p1:** A checked proof that 28 elements cannot be sorted with 99 comparisons (S(28) >= 100), improving the Stober-Weiss bound of 99.
- **p2:** For n in {25, 26, 27}, a checked proof that n elements cannot be sorted with ceil(log2 n!) comparisons (84, 89 or 94), provided no published source (including those cited by OEIS A036604 and Peczarski's Algorithmica 2004 table) already shows it.

## How a win is checked

For lower bounds: re-run the search with an independently written poset-sortability checker (canonical forms via nauty or brute force, forward plus backward search), confirm that the root poset is unsortable within C comparisons, and cross-check sample entries of the certificate. For an upper bound: replay the strategy, for every reachable poset class apply the stated comparison, and verify by memoised recursion that both outcomes lead to total orders within the remaining budget.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A036604>

## Sources

- <https://oeis.org/A036604>
- <https://arxiv.org/abs/2206.05597>
- <https://github.com/CodeCrafter47/sortinglowerbounds>
- <https://oeis.org/A001768>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Extend the Stober-Weiss bidirectional search with stronger poset canonisation and disk-backed storage; their n = 28, C = 98 run took 10 h at efficiency 0.96, while C = 99 halves the efficiency and needs a much larger search.
- Exploit duality (a poset and its dual are equally sortable) and the efficiency threshold n!/2^C to prune.
- For upper bounds, seed from Ford-Johnson and search locally for a first comparison sequence that leaves more balanced posets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- S(n) is the worst-case count for adaptive algorithms, not comparator networks (A003075) and not selection (V_t(n)).
- An unsortability proof must cover all comparison choices at every poset; heuristic pruning that is not provably safe invalidates it.
- Known values n <= 22 are proven; a result contradicting them means a bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/min-comparison-sorting-s23-s24.md
```

Already set up? Say `run V3R1T4S on min-comparison-sorting-s23-s24`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `min-comparison-sorting-s23-s24`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
