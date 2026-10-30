# QOBLIB node-disjoint Steiner tree packing (multi-layer switchbox routing): a cheaper packing for an instance without a proved optimum

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (multi-layer grid graphs up to 100 x 100 per layer and 5 layers; the 14 best-known instances are at most 70 x 70; the official checker runs in seconds) · open as of 2026-10-30

## The problem

QOBLIB's problem class 04 (ZIB-AOPT/QOBLIB, after Hoang and Koch, 'Steiner tree packing revisited', Math. Methods Oper. Res. 76, 2012) asks for node-disjoint Steiner trees connecting several terminal nets in a multi-layer grid graph with holes (switchbox wire routing), minimising total edge cost. There are 190 generated instances (grids up to 100 x 100, 1 to 5 layers), all feasible by construction, and every instance directory also ships the generator's seed solution (sol.txt). On 2026-10-30 the auto-generated best-known table lists 43 instances: 29 marked optimal and 14 marked best known, all from the curated reference. The 14 are stp_s020_l2_t3_h3_rs97531 363, s020_l2_t4_h0_rs24098 189, s020_l3_t4_h0_rs24098 344, s020_l4_t3_h3_rs37235 390, s020_l4_t4_h0_rs24098 228, s020_l5_t3_h3_rs24098 296, s020_l5_t4_h0_rs24098 242, s030_l3_t4_h0_rs24098 304, s030_l4_t4_h0_rs97531 480, s050_l2_t3_h1_rs97531 834, s050_l2_t4_h1_rs97531 756, s050_l3_t6_h2_rs97531 343, s060_l3_t4_h1_rs123 321 and s070_l4_t6_h0_rs97531 375. The other 147 have no table value, but they are not untouched: better packings live in two public places. In issue #2 (opened 2026-02-24) a commenter signing as RoutingEnthusiast posted checker-valid packings for all 190 instances (attachment 'solutons.tar.gz', 2026-03-06, offered for free re-use), including cost 475 for stp_s030_l3_t5_h1_rs24098 whose table row says 'optimal' at 476, cost 374 for stp_s070_l4_t6_h0_rs97531, and values strictly below both pull requests on 52 of the 147. And two open pull requests give checker-validated packings for all 147 and also reach 374 on stp_s070_l4_t6_h0_rs97531: #62 (Marcin Kaminski, 4colors, 2026-09-08) and #88 (Manan Gupta / mnn31, negotiated congestion, 2026-10-09); maintainer Maximilian Schicker has asked both to meet QOBLIB's AI policy before merging. In issue #2 (2026-03-09) and again in issue #55 he called the checker the source of truth and put the '476 optimal' row down to a log-parsing error.

## What counts as a win

A packing in the QOBLIB 04-steiner solution format ('node1 node2 net_id' per selected edge) for one instance in 04-steiner/instances, accepted by the official checker (04-steiner/check: every net's terminals connected, each net's edges forming a connected subgraph, node-disjoint across nets). Its total cost must be STRICTLY LESS (direction: min) than the minimum, over every public value for that instance, of: the table value in 04-steiner/solutions/README.md; the cost of the instance's own sol.txt; every value in merged or open QOBLIB submissions and pull requests (today #62 and #88); and every checker-valid packing posted in a QOBLIB issue thread, in particular the solution set attached to issue #2 on 2026-03-06. All of these must be re-read, and the competing solution files re-scored with your own checker, at claim time. An instance whose optimum is proved can only be won by showing that proof wrong.

## Partial wins

- **p1:** Certified optimality for one of the 14 'best known' instances, or for one of the 147 with no table value: a packing plus a lower-bound certificate checked independently of the solver (e.g. an exact-arithmetic VIPR certificate for the shipped multicommodity-flow ILP, checked by viprchk), with the model rebuilt from arcs.dat/terms.dat/roots.dat.
- **p2:** A certified optimum for stp_s030_l3_t5_h1_rs24098, whose 'optimal' 476 label is contradicted by checker-accepted packings of cost 475 (posted in issue #2 on 2026-03-06, restated in issue #55, and resubmitted in PR #62): a packing of cost at most 475 confirmed by your own independently written checker, plus a lower-bound certificate checked independently of the solver (e.g. VIPR checked by viprchk) for the model rebuilt from the instance files.

## How a win is checked

Read arcs.dat (undirected 'tail head cost'), terms.dat (terminal, net id) and param.dat. Check that the solution's node sets are pairwise disjoint and that each net's chosen edges exist in arcs.dat and connect all of its terminals. Sum the costs. Run both the official Rust checker and an independently written one. Then re-read the BKV table in 04-steiner/solutions/README.md, the instance's sol.txt, the open pull requests and the packings attached to the QOBLIB issue threads, and re-score each competing file with the same checker. A checker written during vetting accepted the issue-#2 packings for stp_s060_l5_t6_h2_rs37235 at 1402 and stp_s030_l3_t5_h1_rs24098 at 475.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/04-steiner/solutions/README.md>

## Sources

- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/04-steiner/README.md>
- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/04-steiner/solutions/README.md>
- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/04-steiner/instances/README.md>
- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/04-steiner/check/README.md>
- <https://github.com/ZIB-AOPT/QOBLIB/issues/2>
- <https://github.com/ZIB-AOPT/QOBLIB/issues/55>
- <https://github.com/ZIB-AOPT/QOBLIB/pull/62>
- <https://github.com/ZIB-AOPT/QOBLIB/pull/88>
- <https://link.springer.com/article/10.1007/s00186-012-0391-8>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Negotiated-congestion (PathFinder) routing gives feasible packings fast; improve them with rip-up-and-reroute where each net is re-solved as an exact Steiner tree problem (e.g. SCIP-Jack) on the graph minus the other nets' nodes.
- The shipped multicommodity-flow ILP plus a strong heuristic incumbent may close the 20x20 instances; use the layered grid symmetry and via costs for cuts.
- Large-neighbourhood search: free a window of the grid across all layers and re-solve it exactly with the ILP.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Public better values are not only in pull requests: the packings attached to issue #2 on 2026-03-06 beat the best open-PR value on 52 of the 147 instances and already reach 374 on stp_s070_l4_t6_h0_rs97531. Score them yourself before claiming a first or improved value.
- Values in open pull requests are not yet on the auto-generated table; check the PRs, or your 'first value' may already be beaten.
- Every instance directory ships the generator's seed solution sol.txt; its cost is a public value too, and for many instances it is worse than the heuristics above, but never assume it.
- A row marked 'optimal' may be wrong (stp_s030_l3_t5_h1_rs24098 at 476 versus checker-accepted 475); do not trust status flags without a certificate.
- Node-disjointness includes Steiner (non-terminal) nodes; edge-disjoint packings are a different, easier problem.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/qoblib-steiner-tree-packing-records.md
```

Already set up? Say `run V3R1T4S on qoblib-steiner-tree-packing-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `qoblib-steiner-tree-packing-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
