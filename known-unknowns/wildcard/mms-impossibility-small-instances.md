# MMS impossibility: an additive instance where no allocation gives every agent more than 20/21 of her maximin share (or chores above 31/30)

🃏 **Wildcard** · standard · tractability ★★★☆☆ · compute: laptop-hours; exact checking of a 4-agent, 11-13-item instance enumerates 4^m labelled allocations (4^11 ~ 4.2e6 takes seconds with numpy) · open as of 2026-10-30

## The problem

In additive fair division with n agents and m indivisible goods, agent i's maximin share MMS_i is the largest value v_i can guarantee herself by splitting all goods into n bundles and keeping the worst. For goods, alpha*(I) is the best min over agents of v_i(A_i)/MMS_i achievable by any complete allocation; the universal constant alpha_MMS is the infimum of alpha*(I) over all instances. For chores, rho*(I) is the least max over agents of c_i(A_i)/MMS_i. Kurokawa-Procaccia-Wang showed that exact MMS can fail for three agents. Feige, Sapir and Tauber (WINE 2021, arXiv:2104.04977) gave a three-agent, nine-good instance with alpha* = 39/40, proved nine goods is tight, and gave a 44/43 chores instance. Ezra and Garbuz, 'Improved Impossibility Bounds for Maximin Share Allocations' (arXiv:2609.15085, v2 23 Oct 2026), give four-agent, eleven-item instances with two valuation types: goods alpha* = 20/21 (MMS 21, best achievable 20) and chores rho* = 93/90 = 31/30. Their asymptotic bounds 1 - Omega((log n)^-2) tend to 1, so the universal records stay 20/21 and 31/30. No three-agent bound below 39/40 is reported. The known guarantees (7/9, Huang-Zhou arXiv:2511.13056; 11/12 for three agents, Feige-Norkin arXiv:2205.05363) leave room. This lane checker reproduced both Ezra-Garbuz values exactly.

## What counts as a win

An explicit instance with nonnegative integer valuations (or costs), any n and m, such that either (goods) alpha*(I) < 20/21, or (chores) rho*(I) > 31/30, both strictly (direction: goods lower, chores higher). Here alpha*(I) = max over complete allocations A of min over agents i with MMS_i > 0 of v_i(A_i)/MMS_i, and MMS_i is computed exactly over all partitions of the items into n bundles. Chores are defined dually with min/max swapped. The claim must state each MMS_i exactly, with a partition attaining it. It must also give the exact optimal factor as a fraction and an allocation attaining it. Checking must fit in laptop-hours: exhaustive labelled enumeration, or for larger m an exact ILP with an independently re-verified certificate. Bars are re-checked at claim time against the latest version of arXiv:2609.15085 and any newer paper.

## Partial wins

- **p1:** Three agents, goods: an additive instance with n = 3 and alpha*(I) < 39/40 strictly. Feige-Sapir-Tauber proved 39/40 is the worst possible with nine goods, so this needs at least 10 goods.
- **p2:** Three agents, chores: an additive instance with n = 3 and rho*(I) > 44/43 strictly.

## How a win is checked

Write an independent checker (numpy or C, no claimant code). For each agent, compute MMS_i by enumerating all n^m labelled partitions, or by an exact DP over bundle sums, and check that the claimed partition attains it. Then enumerate all n^m complete allocations and compute the exact max-min ratio with fractions.Fraction; for chores compute the min-max ratio. Negative controls: the Ezra-Garbuz goods instance (v1 = 1 17 3 10 1 10 7 7 7 3 18 and v2 = 1 14 5 10 1 9 6 7 7 5 19, two agents of each type) must give MMS = 21 and best min value 20. Their chores instance must give MMS 90 and best max cost 93, and the FST instance must give 39/40. Compare strictly with the bars.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.15085>

## Sources

- <https://arxiv.org/abs/2609.15085>
- <https://arxiv.org/abs/2104.04977>
- <https://arxiv.org/abs/2205.05363>
- <https://arxiv.org/abs/2511.13056>
- <https://arxiv.org/abs/2610.06125>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ezra and Garbuz report that their small instances were explored with an LLM. Their structure is two valuation types, every agent's MMS equal to her proportional share, and two disjoint exact partitions. Generalise it to three types, five agents or 12-14 items, and search integer perturbations with an exact inner oracle.
- Treat the search as a game: fix target partitions (one per type), then maximise the number of allocations violated, and repair them with ILP.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Instances with m <= n + 5 goods always have MMS allocations (FST), and so do four agents with at most 10 goods (Hummel IJCAI 2023). Search above those sizes.
- Rounding MMS values or ratios in floating point can turn a tie into a false record; use exact arithmetic.
- Partial allocations (goods left unallocated) are not allowed. Every item must go to some agent.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/mms-impossibility-small-instances.md
```

Already set up? Say `run V3R1T4S on mms-impossibility-small-instances`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mms-impossibility-small-instances`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
