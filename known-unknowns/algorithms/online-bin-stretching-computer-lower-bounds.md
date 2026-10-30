# Online bin stretching: a computer-certified adversary tree beating the best lower bound for some m in 3..12 (41/30, 19/14, 15/11 cells), with randomized and upper-bound cells as partial wins

⚡ **Algorithms** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (minimax game-tree search with DP feasibility caching; LRCB reached 15/11 for m = 6-8 on desktop hardware, harder cells may need a cluster as in Bohm's parallel runs; Rocq certification of a large tree takes hours and several GB) · open as of 2026-10-30

## The problem

Online bin stretching (Azar and Regev 1998): items arrive one at a time and are known to fit into m bins of size 1. Each item is placed irrevocably, and the stretching factor is the largest final load. s*(m) is the best stretching factor of a deterministic algorithm. Lower bounds come from adversary trees found by computer and certified in Coq/Rocq. Bohm's binstretch README (state as of 2023-06-29) lists m = 2: 4/3, tight. m = 3: 41/30, unpublished (Bohm) but Coq-verified; the published value is 112/82 (Bohm and Simon, TCS 2022). m = 4, 5: 19/14 (Bohm and Simon). m = 6, 7, 8: 15/11 (Lhomme, Romane, Catusse and Brauner, arXiv:2207.04931), Coq-verified. m = 9-12: 19/14, unpublished and unverified. m >= 13: 4/3. Upper bounds: 11/8 for m = 3 (Bohm, Sgall, van Stee and Vesely). 31/22, 23/16 and 19/13 for m = 4, 5, 6 (Lieskovsky, arXiv:2201.12393, by computer search). 3/2 for all m. 139/93 < 1.495 for large m (Bohm, Lieskovsky, Schmitt, Sgall and van Stee, APPROX 2024). Lhomme, Catusse and Brauner (arXiv:2506.17271, 2025) prove that these computational searches converge. Randomized algorithms (Lhomme, Catusse and Brauner, arXiv:2405.19071): m = 2 lies in [7/6, 5/4]; lower bounds are 19/16 for m = 3 and 11/9 for m = 4, by LP over the finite game. Credit: the authors named above.

## What counts as a win

A full win is an adversary tree establishing Lower_bound m t g (all items integer, the whole input packable into m bins of capacity g at every node, every algorithm forced to a load of at least t) for some m in 3..12. It must be certified by the Rocq/Coq development of github.com/bs24/LB_BinStretching, or by an independent exact checker that shares no code with the search and reproduces the published witnesses first. It must hold with t/g strictly greater than the best lower bound for that m at claim time (higher is better). Current bars: m = 3: 41/30. m = 4 or 5: 19/14. m = 6, 7 or 8: 15/11. m = 9 to 12: 19/14. Each bar is the larger of the published value and the value in Bohm's README; re-check the README, arXiv and the Lhomme and Bohm repositories before claiming. Every cell lies strictly below a proven upper bound (m = 3: 11/8; m = 4, 5, 6: 31/22, 23/16, 19/13; otherwise 3/2), so no cell asks to beat a proven optimum. The gaps are open, and the true value may still equal the current lower bound. Values in unmerged pull requests are not bars.

## Partial wins

- **p1:** The first certified (Rocq/Coq-checked) adversary tree proving 19/14 for some m in 9..12, where the README lists the bound as unpublished and unverified, or any certified lower bound strictly above 4/3 for some m >= 13.
- **p2:** Deterministic upper bound: an explicit algorithm strategy for m = 3, 4, 5 or 6 in Lieskovsky's computer-search framework (a finite strategy over item classes plus 'good situations' that cover all continuations). An independent checker must certify that its stretching factor is strictly below 11/8, 31/22, 23/16 or 19/13 respectively.
- **p3:** Randomized bounds: an exact rational LP certificate (primal and dual) on a finite discretised game giving a lower bound on the randomized stretching factor strictly above 7/6 (m = 2), 19/16 (m = 3) or 11/9 (m = 4). Or a randomized algorithm for m = 2 with a certified stretching factor strictly below 5/4.

## How a win is checked

Deterministic lower bounds: convert the tree from DOT to Rocq with the LB_BinStretching converter and run 'cd Rocq && ./testnewtree.sh m t g'. Calibrate first on the shipped witnesses (4..8 19 14, 3 112 82). An independent checker must at every adversary node check that the items sent so far fit offline into m bins of capacity g (exact bin-packing feasibility by DP or ILP). At every algorithm node it must check that all placements are covered, and that each leaf has a bin of load at least t. Randomized: rebuild the finite game at the stated granularity, solve the sequence-form LP in exact rationals, and check the dual certificate. Upper bounds: replay the algorithm strategy against every adversary move, including the class-interval and good-situation arguments, with exact arithmetic.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/bohm/binstretch>

## Sources

- <https://github.com/bohm/binstretch>
- <https://arxiv.org/abs/2207.04931>
- <https://github.com/lhommeant/Lower-bound-for-online-bin-stretching>
- <https://github.com/bs24/LB_BinStretching>
- <https://arxiv.org/abs/2001.01125>
- <https://arxiv.org/abs/2201.12393>
- <https://arxiv.org/abs/2405.19071>
- <https://arxiv.org/abs/2506.17271>
- <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX/RANDOM.2024.10>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Granularity is the lever. LRCB proved 15/11 for m = 6-8 but not for m = 4, 5. Try 15/11 = 30/22 or intermediate fractions such as 26/19 or 41/30 for m = 4 and 5 at larger g, using LRCB's pruning propagation (precomputed always-winning packings for the algorithm) and Bohm's parallel caching.
- For m = 9-12 the unverified 19/14 trees may already exist in Bohm's runs. Rebuilding one with the tree-proof variant of LRCB's bound_finder and certifying it is the cheapest win (p1).
- The randomized m = 2 gap [7/6, 5/4] is small, and the LP game is tiny at moderate granularity. Push g upward and exploit symmetry (bin relabelling) to shrink the LP.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The README's m = 3 value 41/30 is unpublished. Compare against it, not against the published 112/82.
- The 9-12 bin 19/14 bound is listed as unverified. A certified 19/14 there is p1, not a full win.
- An adversary node is legal only if the whole input so far fits into m bins of capacity g. Skipping the offline feasibility check yields bogus trees.
- Never compare randomized and deterministic values, and do not treat online makespan scheduling without the known-OPT promise as the same problem.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/online-bin-stretching-computer-lower-bounds.md
```

Already set up? Say `run V3R1T4S on online-bin-stretching-computer-lower-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `online-bin-stretching-computer-lower-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
