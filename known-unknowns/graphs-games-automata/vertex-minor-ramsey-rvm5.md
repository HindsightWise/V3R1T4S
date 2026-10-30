# Vertex-minor Ramsey numbers: a 13-vertex graph with no 5-vertex edgeless vertex-minor (R_vm(5) >= 14), or beat Bae's explicit bounds for k = 6..9

🕸️ **Graphs, games and automata** · standard · tractability ★★★★☆ · compute: laptop-hours (an exact check of one 13- or 14-vertex graph takes seconds; the search is local or SAT-guided) · open as of 2026-10-30

## The problem

A graph H is a vertex-minor of G if H is an induced subgraph of a graph locally equivalent to G (local complementation at v complements the edges inside N(v)). R_vm(k) is the least n such that every n-vertex graph has the edgeless graph E_k as a vertex-minor. Equivalently, every n-vertex graph has beta(G) >= k, where beta(G) is the largest independence number over the local-equivalence orbit of G. Ascoli, B. Frederickson, S. Frederickson, McFarland and Post ('Almost all graphs are vertex-minor universal', arXiv:2602.09049, 2026) proved (1+o(1)) k^2/(2 log2 3) <= R_vm(k) <= 2^k - 1. Ji Ho Bae, 'Vertex-minor Ramsey numbers: exact values and extremal structure', arXiv:2604.13434 (v1, 15 Apr 2026), proves R_vm(4) = 11 by exhaustive classification: exactly six 10-vertex graphs, in five LC classes, avoid E_4. Disjoint unions of these with K_2 and the complement of C_6 give the first explicit lower bounds (Corollary 6.3): R_vm(5) >= 13, R_vm(6) >= 17, R_vm(7) >= 21, R_vm(8) >= 23, R_vm(9) >= 27. The paper conjectures R_vm(5) = 15 (Conjecture C), states R_vm(5) as the next open case, and reports that more than five million 10-vertex graphs still avoid E_5. So no explicit graph on 13 or more vertices with beta <= 4 is known. A single explicit graph raises a bound.

## What counts as a win

An explicit graph G (graph6 or an edge list) on N vertices and an integer k in 5..9 with beta(G) <= k-1, that is, E_k is NOT a vertex-minor of G, where N is STRICTLY GREATER (direction: max) than the largest order of such a graph known at verification time. The values on 2026-10-30 come from Corollary 6.3 of arXiv:2604.13434: N > 12 for k = 5 (giving R_vm(5) >= 14), N > 16 for k = 6, N > 20 for k = 7, N > 22 for k = 8, N > 26 for k = 9. beta(G) <= k-1 must be certified by two independent exact methods (see verification_method). Re-check the arXiv abstract page and any 2026 follow-up for a larger explicit graph before claiming. A graph with N >= 15 for k = 5 contradicting a later proof of R_vm(5) = 15 means a bug.

## Partial wins

- **p1:** A connected 12-vertex graph with beta(G) = 4, certified as above. Connectivity is invariant under local complementation, so it is structurally new: the published 12-vertex example is the disjoint union of a 10-vertex extremal graph and K_2.
- **p2:** The exact number of non-isomorphic 10-vertex graphs with beta(G) <= 4 (Bae's 5,464,788 is only an upper bound because of an orbit-search budget), found by two independent exhaustive implementations whose full logs agree.

## How a win is checked

Method 1, Bouchet elimination: E_k is a vertex-minor of G iff for some k-set S the vertices outside S can be eliminated one at a time, each by deletion G-v, by G*v-v or by the pivot G x vw - v, so that the graph left on S is edgeless. E_k is alone in its LC class, so the final graph must be literally edgeless. Try all three options, and all neighbours w for the pivot, for every S. Method 2: BFS over the full labeled LC orbit of G (local complementation at every vertex until closure) and take the maximum independence number. The two must agree. Calibrate both on the complement of C_6 (beta = 2, labeled orbit size 132 by the auditor's own check) and on Bae's 10-vertex extremal graphs (beta = 3, orbit 8712). The lane's own checker reproduced Method 1 = Method 2 on 30 random 7-vertex graphs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2604.13434>

## Sources

- <https://arxiv.org/abs/2604.13434>
- <https://arxiv.org/html/2604.13434>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Local search on 13-vertex graphs seeded by Bae's six extremal 10-vertex graphs plus three vertices, scoring the number of k-sets S that admit an edgeless elimination.
- Highly symmetric candidates (circulants, Paley-type and other strongly regular graphs and their LC orbits) of order 13-14, whose many automorphisms cut the S-enumeration.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- beta is the maximum independence number over the whole LC orbit, not alpha(G) itself.
- Pivoting needs the edge vw to exist; skipping the pivot branch under-reports vertex-minors and can fake a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/vertex-minor-ramsey-rvm5.md
```

Already set up? Say `run V3R1T4S on vertex-minor-ramsey-rvm5`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `vertex-minor-ramsey-rvm5`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
