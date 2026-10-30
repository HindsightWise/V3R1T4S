# QOBLIB network design (Bienstock-Gunluk demands): a 2-in/2-out digraph and routing with lower maximum edge load for an open instance network11..network24

🚚 **Optimization benchmarks** · standard · tractability ★★☆☆☆ · compute: laptop-hours (n = 11..24 nodes; scoring a topology is one min-congestion multicommodity-flow LP) · open as of 2026-10-30

## The problem

QOBLIB problem class 08 (Network Design, Bienstock and Gunluk, Math. Programming 68, 1995): for the first n rows and columns of a fixed 24 x 24 demand matrix, build a simple digraph on n nodes with in-degree and out-degree exactly 2 and route every demand t_ij from i to j so as to minimise the maximum aggregate flow on any arc (objective z in thousandths of a unit). QOBLIB (ZIB-AOPT, maintained on GitHub with an auto-generated best-known table) lists network05..network10 as optimal and network11..network24 as best known only. A parallel-tempering submission (Manan Gupta, PR #45, dated 2026-08-18, merged 2026-10-19) lowered eleven of them (network13..network23), matched the reference value on network11 and was worse on network12 and network24; the auto-generated table credits it for twelve rows because it also re-attributed the network11 tie. Table best known z on 2026-10-30: network11 238334, network12 276474, network13 300620, network14 343091, network15 370870, network16 397908, network17 437000, network18 473375, network19 492924, network20 528528, network21 569273, network22 618135, network23 659369, network24 663688; network12 and network24 are still held by the curated reference solutions, the other twelve rows by the 2026-08-18 submission. Two open pull requests already go below the table and are not on it: #61 (Marcin Kaminski, 4colors, 2026-09-08) gives network20 520929 and network22 616578, and #98 (Manan Gupta, 2026-10-25) gives network20 522657 and network23 648241. Maintainer Maximilian Schicker has asked the open pull requests to meet QOBLIB's AI policy before merging.

## What counts as a win

A solution file in the QOBLIB Gurobi-style format (x#i#j arc indicators, f#k#i#j flow of commodity k on arc (i,j) in thousandths) for one instance networkNN with NN in 11..24 such that an independent checker confirms: every node has exactly 2 outgoing and 2 incoming arcs with no loops; flow is non-negative and only on chosen arcs; for each source k, net outflow at k equals 1000 times the sum of t_kj and net inflow at each j equals 1000 t_kj (t from the first NN rows and columns of 08-network/instances/demand.txt); and the maximum aggregate arc flow is STRICTLY BELOW (direction: min) the minimum, for that instance, of the Best Known value in https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/08-network/solutions/README.md and the objective of every solution file in a merged or open QOBLIB submission or pull request (today #61 and #98), all re-fetched and re-scored immediately before claiming. The checker must first validate the posted best solution for that instance and the best open-pull-request solution. Nothing is submitted; the write-up goes to the human.

## Partial wins

- **p1:** Prove the listed value of one instance network11..network24 optimal: a VIPR certificate from exact SCIP on the QOBLIB integer model that viprchk accepts, or another machine-checkable certificate whose checker the skeptic can build.
- **p2:** For one open instance, a checker-valid solution whose maximum load equals the listed best known value exactly and whose arc set differs from the posted best solution's arc set (an alternative record topology).

## How a win is checked

Parse demand.txt (24 rows of '|i | t_i1, ..., t_i24|'), take the leading n x n block, read x and f from the claimed file, check degrees, arc support, per-commodity conservation and recompute the max arc load. A 90-line Python checker written during vetting validated the posted network11.bst.sol (max load 238334 = z) and network20.bst.sol (528528 = z). Then re-read the solutions README and score the solution files attached to the open pull requests with the same checker. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/08-network/solutions/README.md>

## Sources

- <https://github.com/ZIB-AOPT/QOBLIB/tree/main/08-network>
- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/08-network/solutions/README.md>
- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/08-network/instances/demand.txt>
- <https://raw.githubusercontent.com/ZIB-AOPT/QOBLIB/main/08-network/check/README.md>
- <https://github.com/ZIB-AOPT/QOBLIB/pull/61>
- <https://github.com/ZIB-AOPT/QOBLIB/pull/98>
- <https://doi.org/10.1007/BF01585766>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search over topologies only (a 2-in/2-out digraph is a union of two derangements) with degree-preserving 2- and 3-exchanges, scoring each topology by the exact min-congestion LP; then restore integral thousandths by re-solving with integer flows.
- Seed from the posted best topology for n and from good topologies for n-1 and n+1 (add or remove a node and repair degrees).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Flows are integers in thousandths of a unit; a fractional LP routing must be rounded to an integral routing that still meets the claimed z.
- The table is not the whole record: open pull requests #61 and #98 already hold values below it on network20, network22 and network23, and they are not on the auto-generated table. Score the PR solution files yourself before claiming.
- network12 and network24 are still held by the curated reference solutions, the other twelve table rows by the 2026-08-18 submission; re-fetch the README, which is regenerated by CI on every accepted submission.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/qoblib-network-design-max-flow.md
```

Already set up? Say `run V3R1T4S on qoblib-network-design-max-flow`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `qoblib-network-design-max-flow`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
