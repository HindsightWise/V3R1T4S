# Petersen colouring conjecture (refuted 2026): a counterexample on fewer than 52 vertices (minimum is in [40, 52]) or a cyclically 5-edge-connected one

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days for gadget/multipole searches with SAT checks; a certificate check takes seconds to minutes · open as of 2026-10-30

## The problem

Jaeger (1988) conjectured that every bridgeless cubic graph G has a Petersen colouring: a map E(G) -> E(P) sending adjacent edges to adjacent edges of the Petersen graph P. It was refuted in 2026: a 68-vertex counterexample posted on X in July 2026 by @NeuralReformist (credited to GPT-5.6 Sol Ultra); a 112-vertex counterexample by Bryce Putman (arXiv:2608.10012, 8 Aug 2026, DRAT-certified; MathWorld credits him with two non-isomorphic 112-vertex examples); and two non-isomorphic 52-vertex counterexamples with a purely theoretical proof by Jan Goedgebeur, Jorik Jooken, Edita Macajova, Davide Mattiolo, Giuseppe Mazzuoccolo and Nikolay Ulyanov (arXiv:2608.10028, v4 of 30 Sep 2026; House of Graphs 57244 and 57278; 57244 was also posted by @ulya_niko on 12 Aug 2026), who also give a cyclically 4-edge-connected counterexample for every even order >= 60. Using Brinkmann and Van Overberghe's generator they checked all 7,142,217,899 weak snarks on 38 vertices (about 12 CPU years), so the smallest counterexample has between 40 and 52 vertices (their Observation 10 and Problem 9). All known counterexamples are cyclically 4-edge-connected and contain copies of a 4-pole W; whether a cyclically 5-edge-connected counterexample exists is their Problem 11. MathWorld's Petersen Coloring Conjecture page (updated 29 Oct 2026) and the House of Graphs comments (last edited 17 Oct 2026) still call 52 the smallest known. On 2026-10-30 the lane and its skeptic independently re-checked both 52-vertex graphs: cubic, bridgeless, girth 5, Petersen-colouring CNF UNSAT.

## What counts as a win

An explicit simple bridgeless cubic graph G on N vertices whose Petersen-colouring CNF is UNSAT, with a DRAT or LRAT proof checked by drat-trim or cake_lpr, and with N STRICTLY LESS (direction: min) than 52 and than the smallest counterexample listed at claim time on https://mathworld.wolfram.com/PetersenColoringConjecture.html, on House of Graphs (keyword 'Petersen Coloring') and in a fresh arXiv search for 'Petersen coloring conjecture counterexample'. Since 40 is a published lower bound, N must be even with 40 <= N <= 50; a smaller N means the checker is wrong.

## Partial wins

- **p1:** A cyclically 5-edge-connected bridgeless cubic graph (any order) with no Petersen colouring, with a checked UNSAT proof and the cyclic edge-connectivity verified exactly (answers Problem 11 of arXiv:2608.10028).
- **p2:** A third 52-vertex bridgeless cubic graph with no Petersen colouring (checked UNSAT proof), non-isomorphic (nauty canonical form) to House of Graphs 57244 and 57278.

## How a win is checked

Check that G is simple, cubic and bridgeless (networkx.bridges). Encode: one variable x[e][c] for each edge e of G and each of the 15 edges c of P, exactly one c per e, and for each vertex v and each pair of edges a, b at v, forbid every pair (c1, c2) that are not distinct adjacent edges of P. Since Aut(P) is edge-transitive, fixing the colour of one edge is a valid symmetry break. Solve with CaDiCaL/kissat with proof output and check the proof with drat-trim. Sanity-check the encoder: it must return SAT on the Petersen graph, the dodecahedron and any 3-edge-colourable cubic graph, and UNSAT on House of Graphs 57244 and 57278. For p1 compute cyclic edge-connectivity by brute force over small cuts or with an independent implementation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mathworld.wolfram.com/PetersenColoringConjecture.html>

## Sources

- <https://arxiv.org/abs/2608.10028>
- <https://arxiv.org/abs/2608.10012>
- <https://mathworld.wolfram.com/PetersenColoringConjecture.html>
- <https://houseofgraphs.org/graphs/57244>
- <https://houseofgraphs.org/graphs/57278>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Recombine multipoles: the 52-vertex graphs use several copies of the 4-pole W; search for smaller 4-poles or 6-poles with the same set of P-colourings (a colouring-set equivalence is a finite check), then glue.
- Start from the weak snarks on 40-50 vertices built by 4-joins of small snarks, and filter with a fast P-colouring SAT test.
- For p1, look outside the W-gadget family, e.g. superpositions or dot products of Petersen copies that keep cyclic 5-edge-connectivity.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- This field moved from 68 to 52 vertices in about six weeks (July-September 2026); re-check MathWorld, House of Graphs and arXiv the day you claim.
- A Petersen colouring maps adjacent edges to distinct adjacent edges; normal 5-edge-colourings are an equivalent reformulation, but mixing definitions breaks the encoder.
- Graphs with bridges or parallel edges do not count.
- A smallest counterexample must be a weak snark (cyclically 4-edge-connected and not 3-edge-colourable), so a 3-edge-colourable candidate is a bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/petersen-colouring-smallest-counterexample.md
```

Already set up? Say `run V3R1T4S on petersen-colouring-smallest-counterexample`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `petersen-colouring-smallest-counterexample`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
