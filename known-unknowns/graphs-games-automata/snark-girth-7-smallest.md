# Smallest snark of girth 7: find one below 298 vertices (none exist up to 42), or a cyclically 7-edge-connected snark

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days for structured constructions (superposition, dot products, lifts) with a SAT 3-edge-colouring test; a certificate check takes seconds · open as of 2026-10-30

## The problem

A snark is a cubic, cyclically 4-edge-connected graph of girth at least 5 with no proper 3-edge-colouring. Jaeger and Swart (1980) conjectured that every snark has girth at most 6; Martin Kochol disproved this in 1996 with snarks of arbitrarily large girth (superposition). Gunnar Brinkmann and Jan Goedgebeur ('Generation of cubic graphs and snarks with large girth', J. Graph Theory 86 (2017) 255-272, arXiv:1512.05944) note that the smallest snark of girth 7 is still unknown. The smallest girth-7 snark obtained by Kochol's method has 298 vertices, and their exhaustive generation shows there is no snark of girth at least 7 on 42 or fewer vertices, so 44 <= order <= 298. They also generated all snarks of girth at least 6 up to 38 vertices (39 on 38 vertices). The other Jaeger-Swart conjecture, that there are no cyclically 7-edge-connected snarks, is still cited as open, e.g. by Goedgebeur, Macajova and Skoviera (Ars Math. Contemp. 16 (2019), arXiv:1712.07867). Target: an explicit snark of girth >= 7 on fewer than 298 vertices.

## What counts as a win

An explicit simple cubic graph G on N vertices with (1) girth >= 7 computed exactly, (2) cyclic edge-connectivity >= 4 computed exactly (a girth-7 non-3-edge-colourable cubic graph can still have a cyclic 2- or 3-edge-cut, which disqualifies it), (3) no proper 3-edge-colouring, proved by a DRAT/LRAT-checked UNSAT proof of an independently generated CNF, and (4) N STRICTLY LESS (direction: min) than 298 and than the smallest girth->=7 snark found at claim time in a fresh arXiv/Scholar search ('snark girth 7') and on House of Graphs. N <= 42 means the checker is wrong.

## Partial wins

- **p1:** A cyclically 7-edge-connected snark of any order (cubic, not 3-edge-colourable with a checked UNSAT proof, cyclic edge-connectivity computed exactly), refuting the Jaeger-Swart conjecture.
- **p2:** A snark of girth at least 7 on at most 298 vertices that is non-isomorphic to the published Kochol-type example, if that example is downloadable for comparison; not claimable otherwise.

## How a win is checked

Check cubicity and simplicity. Compute girth by BFS from every vertex and cross-check with networkx.girth. Compute cyclic edge-connectivity by an exact method (for small cuts, enumerate edge sets of size < k and test whether two components both contain cycles, or use a max-flow based algorithm cross-checked by brute force). Encode 3-edge-colouring (one variable per edge and colour, exactly one colour per edge, distinct colours at each vertex), fix the colours of the three edges at one vertex, and check the UNSAT proof with drat-trim.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1512.05944>

## Sources

- <https://arxiv.org/abs/1512.05944>
- <https://arxiv.org/abs/1712.07867>
- <https://arxiv.org/abs/1206.6690>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Kochol superposition with smaller 'supervertices' and 'superedges' of girth >= 7; optimise the gadget sizes rather than using the generic construction.
- Dot products and 4-joins of girth-6 snarks along carefully chosen edges, then check girth; or voltage lifts of small snarks, whose girth is computable on the base graph.
- Search cubic graphs of girth 7 with large automorphism groups (Cayley graphs of groups of order 44-200) and test 3-edge-colourability with SAT.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Girth-7 cubic graphs that are not snarks are plentiful; the hard part is non-3-edge-colourability, which needs a checked proof.
- Weak snarks (girth 4) and graphs with small cyclic cuts do not count.
- The 298-vertex value comes from Kochol's generic construction as reported in the 2017 paper. Brinkmann and Van Overberghe's 2026 generator (arXiv:2603.17789, March 2026 preprint) lists girth->=5 snarks only up to 38 vertices, so the lower bound 44 is unchanged. Search for newer constructions before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/snark-girth-7-smallest.md
```

Already set up? Say `run V3R1T4S on snark-girth-7-smallest`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `snark-girth-7-smallest`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
