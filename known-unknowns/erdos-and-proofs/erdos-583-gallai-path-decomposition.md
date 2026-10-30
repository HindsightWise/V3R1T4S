# Erdos #583 (Gallai path decomposition): a connected graph needing more than ceil(n/2) paths, or the exhaustive n = 12 check

✏️ **Erdős problems and proofs** · standard · tractability ★★★☆☆ · compute: laptop-days (n = 12 sweep reported to need about 15 h on 9 cores with the improved decider); needs cluster for n = 13 · open as of 2026-10-30

## The problem

Gallai's conjecture (Erdos-Gallai): every connected graph on n vertices can be partitioned into at most ceil(n/2) edge-disjoint simple paths. Known partial results include Lovasz (paths and cycles), Pyber (even-degree vertices induce a forest), Bonamy-Perrett (maximum degree <= 5), Blanche-Bonamy-Bonichon (planar), Anto-Basavaraju (2-degenerate) and Chu-Fan-Zhou (2026), plus the Dean-Kouider/Yan bound of ceil(2n/3). Exhaustive verification: Botler, Cano and Sambinelli (On computing the path number of a graph, ENTCS 346 (2019) 185-197) used an integer-programming model to verify the conjecture for all graphs on at most 11 vertices, bipartite graphs on at most 16 vertices and regular graphs on at most 14 vertices. Independently, sallerk (forum, 31 Aug 2026, github.com/sallerk/erdos-notes) did all connected graphs with n <= 11 (1,006,700,565 at n = 11). herong / Darrenus (17 Sep 2026, github.com/Darrenus/erdos583-gallai) reproduced n <= 11 with a much faster decider that uses ceil(Delta/2) and sums bounds over components. They announced an n = 12 sweep (164,059,830,476 graphs, about 15 h) as running, but no result has been posted on the forum or in the repository (last push 17 Sep 2026). sallerk's own n = 12 attempt left 35,633,639 graphs undecided.

## What counts as a win

CONFIRMED: an explicit connected graph G on n vertices (edge list) such that E(G) cannot be partitioned into ceil(n/2) edge-disjoint simple paths. The certificate is an exhaustive search that two independently written deciders (no shared code) both report as undecomposable. Decomposability into trails, or with repeated vertices, does not count.

## Partial wins

- **p1:** Exhaustive verification of every connected graph on 12 vertices: the shard counts sum to A001349(12) = 164,059,830,476, nothing is left undecided, and every 'yes' is witnessed by an explicit path family. A second decider must independently re-decide all graphs that the fast filters did not settle trivially, or a uniformly random sample of at least 10^6 of them. This counts only if no complete n = 12 verification has been published (paper or preprint) or posted on the forum thread, in github.com/Darrenus/erdos583-gallai or in github.com/sallerk/erdos-notes by verification time.
- **p2:** The same exhaustive verification for n = 13 (A001349(13) = 50,502,031,367,952 connected graphs).

## How a win is checked

Check a decomposition claim by confirming each path is simple, the paths are edge-disjoint and cover E(G), and their number is <= ceil(n/2). Check a counterexample by running two independent exact deciders (one written from the definition) to exhaustion. Check a census by re-running geng shards, confirming the totals equal A001349(n), and spot-checking witnesses.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/583>

## Sources

- <https://www.erdosproblems.com/583>
- <https://www.erdosproblems.com/forum/thread/583>
- <https://github.com/Darrenus/erdos583-gallai>
- <https://github.com/sallerk/erdos-notes/tree/main/p583>
- <https://doi.org/10.1016/j.entcs.2019.08.017>
- <https://oeis.org/A001349>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Apply the published sufficient conditions (Pyber forest condition, max degree <= 5, 2-degenerate, planar) as a cheap pre-filter. Only graphs outside all of them need the decider; per sallerk that is a majority already at n = 10.
- Search for counterexamples among dense graphs whose even-degree vertices induce a dense subgraph, since those are the cases the theorems miss.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Simple paths, not trails: a decider that lets a path revisit a vertex reports success on everything.
- Memoisation by hash can only prune. A false 'no' must be re-checked by hand, and a hash must never produce a 'yes'.
- herong's n = 12 run may finish and be posted at any time; re-check the thread and the repository before claiming p1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-583-gallai-path-decomposition.md
```

Already set up? Say `run V3R1T4S on erdos-583-gallai-path-decomposition`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-583-gallai-path-decomposition`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
