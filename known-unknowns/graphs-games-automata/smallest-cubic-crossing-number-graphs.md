# Smallest cubic graphs with crossing number 12-15: beat an upper bound in OEIS A110507 (a(12) <= 30, a(13) <= 30, a(14) <= 36, a(15) <= 40)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (exact crossing numbers of 28-38-vertex cubic graphs); needs cluster for partial p2 · open as of 2026-10-30

## The problem

OEIS A110507 gives the order of the smallest cubic graph with crossing number n: 4, 6, 10, 14, 16, 18, 20, 22, 24, 26, 28, 28 for n = 0..11. Pegg and Exoo (2009) did the early work. Clancy, Haythorpe, Newcombe and Pegg (arXiv 1804.10336, Graphs Combin. 2020) showed by explicit drawings that no cubic graph on 26 vertices has crossing number 10 or more. This gave a(10) = 28 (a 28-vertex graph with crossing number 10) and a(11) = 28 (the Coxeter graph, crossing number 11). The same paper gives a 30-vertex cubic graph with crossing number 12 and conjectures that it is minimal. For n >= 12 only upper bounds are known: a(12) <= 30 (CNG 12A = CNG 10A plus an edge insertion), a(13) <= 30 (the Tutte 8-cage / Levi graph), a(14) <= 36 (GP(18,5)) and a(15) <= 40 (GP(20,8)). Weisstein's MathWorld table and OEIS A110507 mark these with '?'. A307450 records the number of extremal graphs, with only lower bounds for n >= 9. Weisstein's A390643 counts connected cubic graphs on 2n vertices by crossing number, with rows through 22 vertices (row 11 added Feb 2026). Goal: a smaller cubic graph with crossing number exactly n for some n in 12..15. Credit: Pegg, Exoo, Clancy, Haythorpe, Newcombe, Weisstein.

## What counts as a win

An explicit connected simple cubic graph G on v vertices with v STRICTLY LESS than the A110507 upper bound for some n in {12, 13, 14, 15} at verification time (30, 30, 36, 40 on 2026-10-30), together with (i) a planarization of a drawing with exactly n crossings, certified planar by two independent testers, and (ii) a certificate that cr(G) >= n (formal proof, or an exact crossing-number ILP/SAT certificate with a checked proof log and an independently re-derived encoding). Re-fetch https://oeis.org/A110507 and https://mathworld.wolfram.com/SmallestCubicCrossingNumberGraph.html immediately before claiming, and check that no newer paper lowers the bound.

## Partial wins

- **p1:** A cubic graph on 28 vertices other than the Coxeter graph (non-isomorphic by canonical labelling) with crossing number exactly 11, certified by a drawing and a lower-bound certificate, which raises A307450's lower bound for n = 11 (currently 1).
- **p2:** The next row of OEIS A390643: the number of connected cubic graphs on 24 vertices with each crossing number k, computed with certified exact crossing numbers and summing to A002851(12).

## How a win is checked

Check that G is simple, connected and 3-regular, and compute its canonical form (nauty) to compare with known graphs. Check the planarization (edge paths reproduce E(G), planar by two testers plus an Euler check, dummy count = n). Check the lower bound by regenerating the encoding and verifying the DRAT/LRAT/VeriPB log, after reproducing a(11) = 28 (Coxeter graph cr = 11) with the same pipeline.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A110507>

## Sources

- <https://oeis.org/A110507>
- <https://mathworld.wolfram.com/SmallestCubicCrossingNumberGraph.html>
- <https://oeis.org/A307450>
- <https://oeis.org/A390643>
- <https://arxiv.org/abs/1804.10336>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search symmetric cubic graphs (generalised Petersen, I-graphs, cubic Cayley and voltage graphs) on 28-34 vertices for high crossing numbers, since the records so far are symmetric graphs.
- Edge-insertion and excision moves on the Coxeter graph and the Levi graph (the CNG 9B/10A/12A constructions), screened by fast heuristic upper bounds, then exact lower bounds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The graph must have crossing number exactly n; a graph with crossing number above n does not bound a(n).
- An upper-bound drawing alone is not enough; a lower-bound certificate is required for the claimed crossing number.
- MathWorld notes that CNG 8D, 8E and 9A were mislabelled in Pegg-Exoo (2009); check claimed crossing numbers of old examples independently.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/smallest-cubic-crossing-number-graphs.md
```

Already set up? Say `run V3R1T4S on smallest-cubic-crossing-number-graphs`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `smallest-cubic-crossing-number-graphs`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
