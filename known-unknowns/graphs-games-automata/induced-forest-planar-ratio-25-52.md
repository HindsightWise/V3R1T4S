# Induced forests in planar graphs after the Albertson-Berman refutation: a planar graph with largest induced forest below 25/52 of its vertices

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-hours for gadget composition plus an exact feedback-vertex-set or SAT certificate (seconds to minutes per graph up to about 100 vertices) · open as of 2026-10-30

## The problem

For a graph G let a(G) be the largest order of an induced forest, and c_P = inf a(G)/|V(G)| over planar graphs. Borodin's acyclic 5-colouring gives c_P >= 2/5, and Albertson and Berman conjectured in 1979 that c_P >= 1/2. The conjecture was disproved in August 2026 by Heejae Jung (31-vertex triangulation with a = 15, arXiv:2608.17350) and independently by Mikhail Makarov (39 vertices with a = 19, and an unproved 37/76 variant, arXiv:2608.13964). Wouter Cames van Batenburg, Jan Goedgebeur and Jorik Jooken (arXiv:2608.23260) then showed that the minimum order of a counterexample is 29, built 4-connected 5-edge-connected counterexamples (the smallest has 41 vertices), and gave a 52-vertex planar graph G52 with a(G52) = 25, so c_P <= 25/52 ~ 0.4808, the best bound so far. Their open problems are to improve 2/5 <= c_P <= 25/52 (Problem 5.1), to find a 5-connected counterexample (5.2), and the Chappell-Pelsmajer conjecture f_d(G) > 2dn/(4d+1) for 2 <= d <= 6, where f_d is the largest induced forest of maximum degree at most d (5.3; their family refutes it for d >= 7). MathWorld's Albertson-Berman Conjecture page (updated 29 Oct 2026) lists 25/52 as the best ratio bound. Disjoint unions of copies of one graph keep its ratio, so a single finite planar graph with a smaller ratio improves the bound.

## What counts as a win

An explicit simple planar graph G on n vertices (edge list plus a planar embedding), and an integer t with 52t < 25n (direction: smaller ratio), together with a certificate that G has NO induced forest on t+1 vertices: a DRAT/LRAT-checked UNSAT proof of an independently regenerated CNF, or agreement of two independent exact solvers (for example an ILP with lazy cycle constraints and an exact feedback-vertex-set solver). The ratio t/n must also be STRICTLY LESS than the best bound listed at claim time on https://mathworld.wolfram.com/Albertson-BermanConjecture.html and in a fresh arXiv search for 'Albertson-Berman' and 'induced forest planar'.

## Partial wins

- **p1:** A 5-connected planar graph G with a(G) < |V(G)|/2, with 5-connectivity computed exactly (for example networkx.node_connectivity) and the induced-forest bound certified as in the main criterion (answers Problem 5.2).
- **p2:** A planar graph G on n vertices and some d in {2,3,4,5,6} with f_d(G) <= 2dn/(4d+1), certified by UNSAT of 'induced forest of maximum degree at most d on floor(2dn/(4d+1))+1 vertices' with a checked proof: a counterexample to the Chappell-Pelsmajer conjecture for that d (Problem 5.3).

## How a win is checked

Check simplicity and planarity with two implementations (networkx.check_planarity and SageMath or the planarity library), and verify the supplied embedding. Re-encode 'G has an induced forest of size >= t+1' yourself (selection variables, plus acyclicity via a parent/rank encoding or iterated cycle cuts), solve with proof logging, check the proof with drat-trim. Independently compute the minimum feedback vertex set with an exact solver and confirm n minus it is at most t. Confirm 52t < 25n with integers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mathworld.wolfram.com/Albertson-BermanConjecture.html>

## Sources

- <https://arxiv.org/abs/2608.23260>
- <https://arxiv.org/abs/2608.17350>
- <https://arxiv.org/abs/2608.13964>
- <https://mathworld.wolfram.com/Albertson-BermanConjecture.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Gadget calculus: the paper's 17-vertex gadget R, with distinguished edge bc, has forest profile (8,8,8,9) on terminal sets {none, b, c, both}. G52 is three disjoint copies of R plus one new vertex z (3*17 + 1 = 52), so a(G52) = 25. Search for planar gadgets with a better profile-to-size ratio and compose them around shared vertices in the same way.
- Search triangulations directly. Stein's theorem (a triangulation's vertices split into two induced trees iff the dual is Hamiltonian) only bears on the a(G) >= n/2 side. Use an exact feedback-vertex-set solver as the inner loop of simulated annealing over edge flips; the paper used the Iwata-Imanishi solver, with a(G) = n - fvs(G).
- For p2 (d = 2, linear forests), adapt Chappell's tight examples.
- The paper's small counterexamples are on the House of Graphs (search keyword 'Albertson-Berman'); use them as seeds and to test your encoder.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Equal ratio 25/52 is not a win; you need strictly less.
- Makarov's 37/76 construction is stated without full proof; do not use it as a baseline.
- An induced forest must be induced: a chosen vertex set whose induced subgraph contains a cycle does not count, even if a spanning forest exists.
- The field moved fast in August 2026; check for later preprints before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/induced-forest-planar-ratio-25-52.md
```

Already set up? Say `run V3R1T4S on induced-forest-planar-ratio-25-52`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `induced-forest-planar-ratio-25-52`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
