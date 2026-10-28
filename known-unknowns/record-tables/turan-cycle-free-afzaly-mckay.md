# Turan numbers for forbidden cycles: beat an 'at least' entry in the Afzaly-McKay extremal graph tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Narjess Afzaly and Brendan McKay maintain tables of extremal graphs ex(n,H) for many families H of forbidden cycles: {C4}, {C5}, ..., {C3,C4} (girth 5), {C3,...,Ck}, {C4,C6}, bipartite families {C_odd,C4}, and more. Entries are exact where proved; for larger n they give lower bounds marked '>=' from graphs found by search (the page was last modified 2026-10-09). Examples on 2026-10-13: ex(n,C4) >= 132, 137, 142 for n = 41, 42, 43 (Max Alekseyev's upper bounds in OEIS A006855 are 133, 139, 145); girth-5 graphs ex(n,{C3,C4}) >= 185, 189, 193 for n = 54, 55, 56 (OEIS A006856). Find a graph on n vertices with no forbidden cycle and strictly more edges than a '>=' entry in any of the tables.

## What counts as a win

Success means an explicit simple graph on n vertices (edge list) containing none of the forbidden cycles of a family H on the Afzaly-McKay page, verified by two independent cycle checkers, whose edge count is STRICTLY GREATER (direction: max) than the table entry for (H,n) on https://users.cecs.anu.edu.au/~bdm/data/extremal.html re-fetched live immediately before claiming, and also greater than the matching OEIS entry (A006855 for C4, A006856 for girth 5, and so on) and any value found by a fresh arXiv search. Edge counts above a proved upper bound (for example Alekseyev's ex(41,C4) <= 133) mean the checker is wrong.

## Partial wins

- **p1:** Determine an exact value: a graph attaining a proved upper bound (for example a C4-free graph on 41 vertices with 133 edges, which would settle ex(41,C4) = 133), or a checkable proof that the '>=' entry is exact for some (H,n) via an UNSAT certificate verified by drat-trim/LRAT.
- **p2:** A bipartite C4-free graph with parts of sizes m and n and more edges than the best known value of the Zarankiewicz number z(m,n;2,2) in OEIS A072567 or a fresh search, for some m,n beyond the exactly known range (n x n case known to n = 24).

## How a win is checked

Parse the edge list, check simplicity (no loops, no multi-edges) and the vertex count. For each forbidden cycle length L, run an exact search: for C4, check that no two vertices share two neighbours (adjacency-matrix product); for longer cycles, run an independent DFS-based cycle detector and also networkx's simple_cycles with length bound, and require both to find none. Compare the edge count with the live Afzaly-McKay table, the OEIS entry and the proved upper bound.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://users.cecs.anu.edu.au/~bdm/data/extremal.html>

## Sources

- <https://users.cecs.anu.edu.au/~bdm/data/extremal.html>
- <https://oeis.org/A006855>
- <https://oeis.org/A006856>
- <https://oeis.org/A072567>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from algebraic extremal graphs: polarity graphs of projective planes (Erdős-Rényi graphs ER_q, q^2+q+1 vertices) are near-optimal for C4. Delete or add vertices carefully, then repair with SAT. The '>=' entries near q^2+q+1 for q = 5, 7 (31, 57 vertices) are natural starting points.
- From coding theory and finite geometry: generalized polygons and their subgraphs are extremal for {C3,...,C_{2k}}. Take an incidence graph of a generalized quadrangle or hexagon, then search for large induced subgraphs on the target vertex count.
- Tabu search on edge sets with an incremental count of forbidden cycles through each new edge (cheap for C4 via common-neighbour counts), seeded with the downloaded sparse6 extremal graphs from the page for n-1 and n+1.
- Vertex-extension SAT: take a record graph on n-1 vertices and solve for the neighbourhood of a new vertex that maximises degree without creating forbidden cycles, then allow a few edge flips in the old graph.
- Prescribed symmetry: assume a cyclic or dihedral automorphism of order n or n-1, so the graph is circulant or bi-circulant, and exhaust connection sets; this is the same reduction that works for Ramsey graphs.
- From statistical physics: simulated annealing at fixed edge count with a penalty for cycles, then greedy edge addition at zero penalty.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Confusing families: {C4} allows triangles; {C3,C4} (girth 5) does not; bipartite families forbid all odd cycles. Check the exact family heading on the page.
- Equalling the '>=' value is not a record; the page already lists such graphs. You need strictly more edges.
- A heuristic cycle detector that misses some cycles gives false positives. Use an exact method and two independent implementations.
- Exceeding a proved upper bound (Alekseyev's bounds in OEIS A006855) signals a bug, not a breakthrough.
- The page and OEIS can disagree in timing; check both and any newer paper (for example on the Zarankiewicz problem) before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/turan-cycle-free-afzaly-mckay.md
```

Already set up? Say `run V3R1T4S on turan-cycle-free-afzaly-mckay`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `turan-cycle-free-afzaly-mckay`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
