# Degree-diameter problem for bipartite graphs: a larger bipartite (d,k)-graph than the Combinatorics Wiki table

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Nb(d,k) is the largest order of a bipartite graph with maximum degree d and diameter k. The Combinatorics Wiki page 'The Degree Diameter Problem for Bipartite Graphs' (Loz, Pérez-Rosés, Pineda-Villavicencio; table 'as of January 2012', page last modified Feb 2022) lists the largest known bipartite graphs for 3 <= d <= 16 and 3 <= k <= 10 (examples: (3,5) = 56, (3,7) = 168, (3,10) = 800, (4,7) = 840, (5,10) = 90,068) and upper bounds. Known later results include Feria-Purón, Miller and Pineda-Villavicencio (order 190 for (11,3); Nb(7,3) = 80). Find a bipartite graph with maximum degree at most d and diameter at most k with strictly more vertices than the table entry and any later published value. The bank's general degree-diameter-table target counts a beat of a bipartite table as its partial win p2; a bipartite record is claimed once, here, not under both.

## What counts as a win

Success means an explicit graph (edge list) that is bipartite (2-colouring verified), has maximum degree at most d and diameter at most k (all-pairs BFS), with STRICTLY MORE vertices (direction: max) than the entry for (d,k) at http://combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_Bipartite_Graphs re-fetched live immediately before claiming, AND than every value for that (d,k) found by a fresh literature search covering 2012-2026 (the wiki table is dated January 2012, so later papers may hold larger graphs). Graphs exceeding the listed upper bound (bipartite Moore bound or better) mean the checker is wrong.

## Partial wins

- **p1:** A record for a small (d,k) with d <= 5 and k <= 6 (where exhaustive verification is instant), beating both the wiki table and the literature.
- **p2:** A checkable optimality proof for a small open (d,k) cell whose upper bound in the wiki is above the largest known order, via exhaustive search with a reproducible certificate.

## How a win is checked

Load the edge list; check simplicity, maximum degree, a proper 2-colouring by BFS, and all-pairs BFS diameter at most k; count vertices. Two independent implementations (e.g. networkx and a C BFS) must agree. Compare with the live wiki table and a literature search for that (d,k) since 2012.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_Bipartite_Graphs>

## Sources

- <http://combinatoricswiki.org/wiki/The_Degree_Diameter_Problem_for_Bipartite_Graphs>
- <https://arxiv.org/pdf/1203.3588>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lifts (voltage graphs) of small bipartite base graphs over cyclic and metacyclic groups: exhaust voltage assignments for base graphs with 2-6 vertices; this is how many general-graph records were found and the bipartite table is less picked over.
- From finite geometry: incidence graphs of generalized polygons are bipartite Moore graphs for k = 3, 4, 6; delete structured point/line subsets or take incidence graphs of partial geometries and nets for nearby (d,k).
- Bipartite Cayley-type graphs (bi-Cayley / Haar graphs) on groups of order n: a connection set S defines a bipartite graph; search groups from the SmallGroups library and random S with diameter checks.
- From coding theory: bipartite graphs of large girth and small diameter come from LDPC-code Tanner graph constructions (quasi-cyclic, protograph lifts). Repurpose QC-LDPC search code with a diameter objective.
- Computer search in the style of Exoo: start from a random d-regular bipartite graph on N vertices and do edge swaps that reduce the number of pairs at distance greater than k.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The table is dated January 2012; beating it is not enough if a later paper has a larger graph. Search the literature for each cell.
- Bipartite diameter subtlety: in a bipartite graph, vertices on the same side are at even distance. Compute the true diameter over all pairs, not just across the bipartition.
- The wiki's HTTPS certificate does not match the host; use the http:// URL.
- Maximum degree at most d is allowed; do not compare a non-regular graph against a regular-only table or vice versa.
- Exceeding the bipartite Moore bound 2((d-1)^k - 1)/(d-2) means the checker is wrong.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/degree-diameter-bipartite-table.md
```

Already set up? Say `run V3R1T4S on degree-diameter-bipartite-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `degree-diameter-bipartite-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
