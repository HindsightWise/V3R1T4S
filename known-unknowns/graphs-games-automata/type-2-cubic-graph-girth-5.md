# A Type 2 cubic graph of girth at least 5 (total chromatic number 5), open since Cavicchioli et al. 2003

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days for constructions and checks; needs cluster for exhaustive extensions beyond 32 vertices · open as of 2026-10-30

## The problem

A total colouring colours vertices and edges so that adjacent or incident elements differ. Rosenfeld showed every cubic graph has total chromatic number 4 (Type 1) or 5 (Type 2). Cavicchioli et al. (2003) asked for the smallest Type 2 snark of girth at least 5. Brinkmann, Preissmann and Sasaki (DMTCS, 2015) built the first Type 2 snarks (all of girth 4, every even order >= 40), and split the question: Question 2, what is the smallest Type 2 cubic graph of girth at least 5? Their computer search showed all cubic graphs of girth 5 on up to 32 vertices are Type 1, so such a graph needs at least 34 vertices; they note that no Type 2 cubic graph of girth greater than 4 is known, and ask (Question 3) whether some girth forces Type 1. Later work by Sasaki, Dantas, de Figueiredo, Araujo and others (2023-2025, Kochol superpositions) produced more Type 2 snarks, still of girth 4, and describes Type 2 snarks as rare and hard to construct. Target: one explicit Type 2 cubic graph of girth >= 5.

## What counts as a win

An explicit simple cubic graph G (edge list, graph6) with girth >= 5 (checked by BFS) that has no total 4-colouring, certified by an UNSAT result with a DRAT/LRAT proof checked by drat-trim or cake_lpr for a CNF the skeptic regenerates (variables for colours of vertices and edges; constraints for adjacency and incidence; symmetry breaking only by fixing the colours at one vertex and its three edges), confirmed by a second independent method (e.g. Brinkmann-style strong 4-edge-colouring test, or a second solver and encoding). A literature search (OpenAlex citations of DMTCS 2111), rerun before claiming, must show no Type 2 cubic graph of girth >= 5 published earlier.

## Partial wins

- **p1:** A rerunnable exhaustive proof that every connected cubic graph of girth >= 6 on 34 vertices is Type 1, with published generator and checker code and a graph count equal to OEIS A014374 at 34 vertices (93,990,692,595).
- **p2:** A rerunnable exhaustive proof that every connected cubic graph of girth >= 5 on 34 vertices is Type 1 (raising the bound to >= 36), with published generator and checker code, its graph count cross-checked by a second generator (OEIS A014372 lists counts only up to 32 vertices).

## How a win is checked

Girth check; regenerate the total-colouring CNF; check the DRAT/LRAT proof; second method agreement. Seconds to minutes for graphs of a few hundred vertices.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://dmtcs.episciences.org/2111>

## Sources

- <https://dmtcs.episciences.org/2111>
- <https://doi.org/10.5753/etc.2025.7019>
- <https://doi.org/10.1016/j.procs.2025.10.299>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lemma 1 of Brinkmann et al.: a cubic graph is Type 1 iff it has a strong 4-edge-colouring (a proper 4-edge-colouring in which the two ends of every edge together see all 4 colours); encode only edge colours, which shrinks the SAT instance.
- Gadget gluing: their Type 2 snarks are junctions of Type 2 bricks of girth 4; search for girth-5 bricks (cubic semi-graphs with four semi-edges) whose total colourings force the same boundary obstruction.
- Search high-girth Cayley and voltage-lift cubic graphs (girth 5-7) with SAT, which scales to thousands of vertices.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Type 2 is about total colouring, not edge colouring (Class 2); snarks are Class 2 but almost all are Type 1.
- Girth 4 examples already exist; the girth >= 5 requirement is the whole problem.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/type-2-cubic-graph-girth-5.md
```

Already set up? Say `run V3R1T4S on type-2-cubic-graph-girth-5`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `type-2-cubic-graph-girth-5`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
