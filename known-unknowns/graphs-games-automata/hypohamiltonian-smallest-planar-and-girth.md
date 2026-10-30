# Smallest hypohamiltonian graphs with extra properties: a planar one below Tsai's 34 vertices, a planar one of order 35, a planar cubic one below 70, or a first one of girth 8

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days for planar generation (plantri) with Grinberg-type filters; a certificate check takes minutes · open as of 2026-10-30

## The problem

A graph is hypohamiltonian if it is non-hamiltonian but every vertex-deleted subgraph is hamiltonian. The order of the smallest planar hypohamiltonian graph is unknown. Cheng-Chen Tsai ('Small planar hypohamiltonian graphs', J. Graph Theory 108 (2025) 799-807, arXiv:2403.18384) found two on 34 vertices, beating the 25 graphs on 40 vertices of Jooyandeh, McKay, Ostergard, Pettersson and Zamfirescu (J. Graph Theory 84 (2017), arXiv:1302.2698), and settled order 41. Durias, Guerrero, Jaiyen, Kaplan, Lapine, Peralta and Shrivastav ('Local modifications in planar hypohamiltonian graphs', arXiv:2610.21210, 15 Oct 2026) proved existence for every order n >= 36, built over 100 examples below 40 vertices and conjecture that 34 is the minimum, so 35 is the only open order from 34 up. Lower bounds: 23 in general (Goedgebeur and Zamfirescu, Ars Math. Contemp. 13 (2017), arXiv:1602.07171; restated in arXiv:2311.10593 and arXiv:2610.21210), 27 without triangles, and exactly 45 for girth 5. The smallest known planar hypohamiltonian graph with a triangle has 216 vertices (arXiv:2610.21210, via Thomassen's construction and Wiener's 31-vertex almost hypohamiltonian graph). Cubic planar: 54 <= h <= 70 (Table 1 of arXiv:1602.07171; 70-vertex graphs of Araya and Wiener and of Jooyandeh and McKay, still cited as smallest by Tsai 2025); cubic planar of girth 5: exactly 76 (McKay). No hypohamiltonian graph of girth 8 or more is known (at least 36 vertices; at least 50 if cubic). Target: a planar hypohamiltonian graph on at most 33 vertices.

## What counts as a win

An explicit simple planar graph G on N vertices with (1) a planar embedding (rotation system) confirmed by an independent planarity test, (2) for every vertex v an explicit Hamiltonian cycle of G - v, (3) non-hamiltonicity of G proved by a DRAT/LRAT-checked UNSAT proof of an independently generated Hamiltonian-cycle CNF, or by two independent exact Hamiltonicity solvers that agree, and (4) N STRICTLY LESS (direction: min) than 34 and than the smallest planar hypohamiltonian graph reported at claim time in the latest version of arXiv:2610.21210, on House of Graphs and in a fresh arXiv/Scholar search for 'planar hypohamiltonian'. N below the proved lower bound 23 (27 for a triangle-free graph) means the checker is wrong.

## Partial wins

- **p1:** A planar hypohamiltonian graph on exactly 35 vertices, certified as in the main criterion: the only order >= 34 still open after Tsai (2025) and arXiv:2610.21210. It must be the first one published, per a fresh search at claim time.
- **p2:** A cubic planar hypohamiltonian graph on fewer than 70 vertices, certified as in the main criterion (lower bound 54).
- **p3:** A planar hypohamiltonian graph containing a triangle on fewer than 216 vertices, certified as in the main criterion.
- **p4:** A hypohamiltonian graph of girth at least 8, of any order and not necessarily planar, with girth computed exactly and hypohamiltonicity certified as in the main criterion (none known; at least 36 vertices, at least 50 if cubic).

## How a win is checked

Check simplicity, planarity (two implementations) and the embedding. For each v, check that the supplied cycle visits all vertices of G - v once and uses only edges. Prove G non-hamiltonian with your own CNF (successor or position encoding with subtour elimination), proof-checked, and cross-check with a second exact method (backtracking with pruning, or concorde on a TSP reformulation). Compute girth by BFS.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.21210>

## Sources

- <https://arxiv.org/abs/2610.21210>
- <https://arxiv.org/abs/2403.18384>
- <https://arxiv.org/abs/1602.07171>
- <https://arxiv.org/abs/1302.2698>
- <https://arxiv.org/abs/2311.10593>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Shrinking local modifications: arXiv:2610.21210 grows graphs with plus-two, plus-three and plus-four patch replacements. Look for replacements of a patch H by a smaller H' with the same cycle-fragment endpoints, starting from Tsai's 34-vertex graphs and Wiener's 31-vertex almost hypohamiltonian graph.
- Exhaustive plantri generation of triangle-free planar graphs on 27-33 vertices with only 4- and 5-faces, pruned by Grinberg-type face counts and the requirement of at least four cubic vertices, as outlined in Section 4 of arXiv:2610.21210.
- For p2, apply cubicity-preserving local replacements to the 70-vertex cubic planar graphs of Araya-Wiener and Jooyandeh-McKay.
- For p4, screen girth-8 cubic graphs with large automorphism groups (voltage lifts, Cayley graphs) for non-hamiltonicity first, then test every vertex-deleted subgraph.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Hypohamiltonian requires EVERY vertex-deleted subgraph to be hamiltonian; checking a few vertices is not enough.
- A planar hypohamiltonian graph has girth at most 5; the girth-8 partial concerns non-planar graphs.
- The record moved from 40 (2017) to 34 (Tsai 2025), and which orders are covered changed again in October 2026 (arXiv:2610.21210): re-check arXiv and House of Graphs the day you claim.
- Hypotraceable, almost hypohamiltonian and K2-hypohamiltonian graphs are different families with separate records.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/hypohamiltonian-smallest-planar-and-girth.md
```

Already set up? Say `run V3R1T4S on hypohamiltonian-smallest-planar-and-girth`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypohamiltonian-smallest-planar-and-girth`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
