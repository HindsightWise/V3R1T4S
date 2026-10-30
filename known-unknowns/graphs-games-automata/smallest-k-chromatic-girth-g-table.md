# Smallest k-chromatic graphs of given girth: beat an upper bound in the Exoo-Goedgebeur n_g(k) table (incl. the triangle-free 6-chromatic gap 32..40)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days for structured search (LCF/Cayley/lift searches plus SAT colouring checks); a certificate check takes minutes to hours · open as of 2026-10-30

## The problem

n_g(k) is the smallest order of a k-chromatic graph with girth at least g. Geoffrey Exoo and Jan Goedgebeur, 'Bounds for the smallest k-chromatic graphs of given girth' (DMTCS 21:3 #9, 2019, arXiv:1805.06713), Table 1, gives the known values n_4(4)=11 (Chvatal), n_4(5)=22 (Jensen-Royle) and n_5(4)=21 (Royle; the Brinkmann graph). Open cells with an explicit upper bound: 29 <= n_6(4) <= 64 (Glauco Rampone, arXiv:2608.23652, Aug 2026: an explicit 64-vertex, 152-edge graph G64, Lean-certified and on House of Graphs, beating Exoo-Goedgebeur's 66-vertex LCF(6,11) graph; the lower bound 29 is an exhaustive SAT-modulo-symmetries computation), 30 <= n_7(4) <= 171 (LCF(9,19) graph), 29 <= n_5(5) <= 80 (Royle's Cayley graph), 32 <= n_4(6) <= 40 (Goedgebeur, J. Graph Theory 93 (2020), arXiv:1707.07581; this is the next term a(6) of OEIS A292528, whose January 2026 edits still give 32 <= a(6) <= 40), 41 <= n_4(7) <= 77 and 51 <= n_4(8) <= 155. Cells with only a lower bound (no explicit small example published): n_6(5) >= 33, n_7(5) >= 66, n_5(6) >= 36, n_6(6) >= 51, n_7(6) >= 127, n_5(7) >= 45, n_6(7) >= 73, n_7(7) >= 218. Exoo and Goedgebeur list a 355-vertex girth-5 LCF(5,71) graph that they suspect is 6-chromatic but could not certify. Upper-bound graphs are in the papers' ancillary files and on House of Graphs (keywords '4-chromatic girth 6', '5-chromatic girth 5', 'triangle-free 7-chromatic'). Target: a k-chromatic graph of girth >= g with fewer vertices than a listed upper bound.

## What counts as a win

An explicit simple graph G (edge list or graph6) on N vertices such that (1) girth(G) >= g, computed exactly; (2) G has no proper (k-1)-colouring, proved by an UNSAT result of the (k-1)-colouring CNF with a DRAT or LRAT proof checked by drat-trim or cake_lpr (a k-colouring need not be shown: if chi(G) > k, a vertex-critical subgraph is a smaller k-chromatic witness); and (3) N is STRICTLY LESS (direction: min) than the current upper bound for that (g,k): 64 for (6,4) (arXiv:2608.23652), and Table 1 of arXiv:1805.06713 for the rest (171, 80, 40, 77, 155 for (7,4), (5,5), (4,6), (4,7), (4,8)). N must also beat OEIS A292528 for g = 4 and any newer bound found by a fresh arXiv / Google Scholar search for 'k-chromatic graphs of girth' and on House of Graphs, all checked immediately before claiming. N below a proved lower bound (29 for (6,4), Table 1 otherwise) means the checker is wrong.

## Partial wins

- **p1:** A first explicit upper bound for a Table 1 cell that lists only a lower bound: a graph of girth >= g with no (k-1)-colouring (DRAT/LRAT-checked UNSAT) and at most 400 vertices, for (g,k) in {(6,5), (7,5), (5,6), (6,6), (5,7)}; certifying that Exoo-Goedgebeur's 355-vertex LCF(5,71) graph (Table 5 of the paper) is not 5-colourable counts, giving n_5(6) <= 355.

## How a win is checked

Parse the graph, check simplicity and the vertex count. Compute girth by BFS from every vertex and cross-check with networkx.girth. Generate the (k-1)-colouring CNF independently (one variable per vertex-colour pair, at-least-one and at-most-one clauses, edge conflict clauses, colour symmetry broken on a clique or a fixed vertex only), solve with CaDiCaL or kissat with proof output, and check the proof with drat-trim or an LRAT checker. Compare N against the live table, OEIS A292528 and a fresh literature search.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1805.06713>

## Sources

- <https://arxiv.org/abs/1805.06713>
- <https://arxiv.org/abs/2608.23652>
- <https://arxiv.org/abs/1707.07581>
- <https://oeis.org/A292528>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- LCF(r,s) and circulant / Cayley searches with fixed symmetry, as in the paper, then a SAT 3- or 4-colouring test as the inner loop.
- Droogendijk's doubling construction (Section 3.1 of the paper) applied to the 750,000+ triangle-free 6-chromatic graphs on 40 vertices, aiming below 77 for k = 7.
- Vertex-deletion search from Rampone's 64-vertex girth-6 graph G64 and the 80-vertex girth-5 record: delete a small vertex set, repair with local edge moves that keep the girth, re-test with SAT.
- Voltage lifts of small base graphs: girth is computable on the base graph, and colourability of lifts can be tested quickly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Girth at least g is required, not exactly g; triangle-free means g = 4.
- A SAT solver's UNSAT verdict without a checked proof is not a certificate.
- Table 1 dates from 2019 and has already moved: n_6(4) went from 26..66 to 29..64 in August 2026 (arXiv:2608.23652). OEIS A292528 still shows 32 <= a(6) <= 40 after January 2026 edits, but search every cell before claiming.
- For (6,4), arXiv:2608.23652 already rules out local modifications of the known witnesses, 4-chromatic Cayley graphs of girth 6 on 54-63 vertices, and witnesses on at most 63 vertices with a semiregular automorphism group of 2 or 3 vertex orbits; do not spend a run there.
- n_4(k) for k >= 7 and other large-k lower bounds are formula bounds, not exhaustive searches; do not cite them as exact.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/smallest-k-chromatic-girth-g-table.md
```

Already set up? Say `run V3R1T4S on smallest-k-chromatic-girth-g-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `smallest-k-chromatic-girth-g-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
