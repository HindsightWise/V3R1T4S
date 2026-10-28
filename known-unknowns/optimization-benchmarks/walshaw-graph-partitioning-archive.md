# Walshaw Graph Partitioning Archive: beat a best known edge cut (k = 2..64, 0/1/3/5% imbalance)

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Chris Walshaw's Graph Partitioning Archive (running since 2000, last updated 25 March 2026, unchanged on 2026-10-28; the page notes its own graph and partition files are offline and available only on request from the maintainer, so 17 of its 34 graphs come from the SuiteSparse DIMACS10 copies and the rest need the maintainer's files, a human-only request) lists, for 34 benchmark graphs, the smallest known edge cut for partitioning into k = 2, 4, 8, 16, 32, 64 parts under four balance tolerances (0%, 1%, 3%, 5% imbalance): 816 records in total. The entries were set by KaFFPa/KaFFPaE and KaBaPE (Sanders and Schulz), ILP-polishing (Henzinger, Noe and Schulz), Jet (Gilbert et al., SIAM J. Sci. Comput. 2024), KaHyPar-E, IPMNE2 (Hein and Setzer) and others, and keep being lowered by improvement runs that start from archive partitions. Find a partition of one listed graph into k parts that respects the archive's balance bound and cuts strictly fewer edges than the table entry for that (graph, k, imbalance) cell.

## What counts as a win

A partition file (one block id 0..k-1 per vertex) for a graph and k listed on https://chriswalshaw.co.uk/partition/, such that an independent checker (a) evaluates it on the SuiteSparse DIMACS10 copy of that graph (https://sparse.tamu.edu/DIMACS10/<name>, vertex order as in that file) or, for an archive graph with no DIMACS10 copy, on the archive's own graph file obtained by the human from the maintainer, after confirming that |V| and |E| equal the archive's graph table, (b) confirms every block has weight at most floor(S_opt * (100 + x) / 100) with S_opt = ceil(|V| / k) and x the imbalance of the table being claimed, and (c) counts cut edges strictly below the entry in that table cell, with the archive page re-fetched live immediately before claiming.

## Partial wins

- **walshaw-any-cell-0pct:** Strict improvement of any cell of the 0% (perfect balance) table; these are the most contested cells and a confirmed improvement is a new archive record by itself.
- **walshaw-jet-cells:** Strict improvement of any 1/3/5% cell currently credited to Jet (the newest solver in the archive, e.g. auto k=16..64), independently checkable with the same checker.
- **walshaw-tie-new-partition:** A partition that exactly ties a k>=32 cell on a graph with |V| >= 100,000 that is available in the SuiteSparse DIMACS10 group (auto, 144, m14b, fe_ocean) produced from scratch in under 12 laptop-hours, verified by the checker; non-trivial because these entries come from long evolutionary plus ILP polishing runs.

## How a win is checked

Download the graph in Matrix Market form from the SuiteSparse DIMACS10 group (the 10th DIMACS Challenge copy of the Walshaw graphs, e.g. https://sparse.tamu.edu/DIMACS10/fe_4elt2; verified 2026-10-13 that its header gives 11143 vertices and 32818 edges, matching the archive). A 30-line script reads the edge list (symmetric pattern, ignore the diagonal), reads the partition, checks block sizes against floor(ceil(|V|/k)*(100+x)/100) and counts edges whose endpoints lie in different blocks. Compare with the live table cell. Runs in seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://chriswalshaw.co.uk/partition/>

## Sources

- <https://chriswalshaw.co.uk/partition/>
- <https://sparse.tamu.edu/DIMACS10>
- <https://sparse.tamu.edu/DIMACS10/fe_4elt2>
- <https://github.com/KaHIP/KaHIP>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the strongest open-source pipeline (KaHIP's KaFFPaE / KaBaPE with the 'strong' preset, and the ILP improver from Henzinger, Noe and Schulz) on the mid-sized graphs where the 0% cells were last set by older tools (FSMAGP, MAHMBCDP, JE): those are the cells most likely to have slack.
- Statistical physics: treat partitioning as a Potts-model ground-state search; parallel tempering with a balance-preserving Kawasaki (pair swap) move set is a natural fit for the 0% table, where single-vertex moves are illegal.
- Spectral and geometric seeding from numerical analysis: most archive graphs are finite-element meshes; recursive coordinate or inertial bisection on recovered mesh geometry (via a spectral embedding) gives very different starting partitions for multilevel refinement than random matching.
- Image segmentation import: graph-cut / max-flow based boundary refinement (FlowCutter-style most-balanced minimum cuts on a band around each block boundary) can shave edges that FM-style refinement cannot reach.
- Exploit the integer slack in the balance bound: for many (|V|, k) the bound floor(S_opt*(100+x)/100) allows one or two more vertices than a naive percentage calculation; search over which blocks carry the slack.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Balance bound arithmetic: the archive uses S_opt = ceil(|V|/k) and allows |S_p| <= S_opt*(100+x)/100, i.e. floor(S_opt*(100+x)/100) for integer block sizes; a checker that drops the ceiling rejects valid partitions, and one that rounds the bound up instead of down accepts partitions the archive would reject.
- Graph identity: only 17 archive graphs are in the SuiteSparse DIMACS10 group (data, uk, wing_nodal, fe_4elt2, fe_sphere, cti, cs4, fe_body, t60k, wing, fe_tooth, fe_rotor, 598a, fe_ocean, 144, m14b, auto). add20, 3elt, add32, bcsstk29-33, whitaker3, crack, vibrobox, 4elt, memplus, fe_pwt, brack2, finan512 and wave are not, and same-named matrices in other SuiteSparse groups (e.g. Hamm/add20) are not guaranteed to be the archive graph; matching |V| and |E| alone does not prove identity.
- Wrong table: a cut that beats the 5% cell but violates the 3% bound is a 5% record only; claims must name the exact (graph, k, imbalance) cell, and an improvement in a looser table never counts for a tighter one.
- Self-loops and duplicate edges: Matrix Market symmetric files store each edge once and may include diagonal entries; counting both triangles or the diagonal doubles or inflates the cut and can hide a non-improvement.
- Re-fetch the archive before claiming: entries are improved in batches and the page was last updated in 2026.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/walshaw-graph-partitioning-archive.md
```

Already set up? Say `run V3R1T4S on walshaw-graph-partitioning-archive`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `walshaw-graph-partitioning-archive`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
