# Degree-diameter problem for planar graphs: a larger planar graph than the Combinatorics Wiki table

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

For maximum degree d and diameter k, find the largest planar graph. The Combinatorics Wiki page 'The Degree Diameter Problem for Planar Graphs' (Loz, Pérez-Rosés, Pineda-Villavicencio; last modified Feb 2022) lists the largest known planar graphs for 3 <= d <= 10 and 2 <= k <= 10 (examples on 2026-10-13: (3,10) = 157, (4,10) = 728, (5,6) = 158, (6,5) = 117), with constructions by Fellows-Hell-Seyffarth, Yang-Lin-Dai, Exoo, Tishchenko, Feria-Purón and Pineda-Villavicencio (2013) and others, and a separate table for regular planar graphs (3 <= d <= 5). Most entries are not known to be optimal. Find a planar graph with maximum degree at most d and diameter at most k with strictly more vertices than a table entry.

## What counts as a win

Success means an explicit graph (edge list) that is planar (checked by two independent planarity tests, e.g. networkx check_planarity and a Boyer-Myrvold or SageMath implementation, plus an explicit combinatorial embedding), has maximum degree at most d and diameter at most k (all-pairs BFS), and has STRICTLY MORE vertices (direction: max) than the entry for (d,k) in the general or regular planar table at http://combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_Planar_Graphs re-fetched live immediately before claiming, and than any value found by a fresh search (Feria-Purón and Pineda-Villavicencio 2013 and later papers on large planar graphs). Matching an entry does not count.

## Partial wins

- **p1:** A record in the regular planar table (d-regular planar graph of diameter k, 3 <= d <= 5) beating the live entry and any later paper, verified as above plus regularity.
- **p2:** An exact value: a checkable proof (exhaustive enumeration with plantri plus a reproducible log, or an UNSAT certificate) that a current entry for some small (d,k) is optimal, where the page does not already mark it optimal.

## How a win is checked

Load the edge list, check simplicity, the maximum degree and the vertex count; compute all-pairs BFS distances and check the maximum is at most k; run two independent planarity tests and output a planar embedding (rotation system) checked by Euler's formula on its faces. Then compare with the live wiki table and a literature search.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_Planar_Graphs>

## Sources

- <http://combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_Planar_Graphs>
- <https://ar5iv.arxiv.org/html/1302.1648>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Recursive 'replace vertex by gadget' constructions (Fellows-Hell-Seyffarth, Feria-Purón-Pineda-Villavicencio): search over small planar gadgets with a SAT/ILP model for the best gadget at each (d,k), since the published gadgets were hand-designed.
- From network design: planar graphs of small diameter look like hierarchical 'hub and spoke' or nested-ring layouts. Parametrise nested rings with chords and search the parameters exhaustively for each (d,k).
- Local search on planar triangulations with plantri-generated seeds: flip edges and add vertices while maintaining planarity and degree, scoring by diameter violations.
- Rotationally symmetric planar graphs (cyclic symmetry around a centre face or vertex) reduce the search to a fundamental sector; this matches the shape of many record graphs.
- For large k, combine good small-diameter blocks by identifying boundary vertices, then repair degree and diameter with SAT.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The wiki serves HTTPS with a certificate for a different host; use the http:// URL. Do not ignore a stale page: it was last modified in 2022, so also search for later papers on large planar graphs.
- The wiki links to 'Tables of the largest known planar graphs maintained by James Preen' (http://faculty.cbu.ca/jpreen/degdiam.html), which may hold newer values; it did not connect on 2026-10-28. Try it once honestly and, if unreachable, record the comparison against it as pending rather than skipping it.
- Diameter 3 is nearly settled: Dailly, Darmon, Giocanti, Hilaire and Valicov (arXiv:2507.18797, 2025) prove the maximum order is at most 9Δ/2 + c, matching the Fellows-Hell-Seyffarth lower bound 9Δ/2 - 3 that the k = 3 column already attains; expect at most a constant gain there.
- Maximum degree versus regular: the general table allows degree at most d, the regular table requires exactly d at every vertex. Compare with the right table.
- Planarity checked only by a drawing or a single library call with a bug: use two independent tests and an explicit embedding.
- Diameter computed on a directed or weighted interpretation, or ignoring disconnected graphs (infinite diameter).
- Off-by-one in the table indices: rows are degree d, columns diameter k.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/degree-diameter-planar-table.md
```

Already set up? Say `run V3R1T4S on degree-diameter-planar-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `degree-diameter-planar-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
