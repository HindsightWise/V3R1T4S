# MOONSHOT - Neumann-Lara conjecture: a planar oriented graph that cannot be split into two acyclic sets, or verification beyond 26 vertices

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days for extending the verification; counterexample search open-ended · open as of 2026-10-30

## The problem

Neumann-Lara (1985) conjectured that every planar oriented graph (no digons) has dichromatic number at most 2: its vertices split into two sets each inducing an acyclic digraph. It is the directed analogue of the Four Colour Theorem and remains open; Li and Mohar proved it for digirth at least 4. Knauer and Valicov (arXiv 1712.06143, European J. Combin.) reduced it, by planar duality, to finding in planar cubic 3-connected digraphs a perfect matching without a directed cut; only duals of non-Hamiltonian triangulations matter, and using McKay's lists of non-Hamiltonian planar cubic graphs they verified the conjecture for all planar graphs on at most 26 vertices, all 4-connected planar graphs on at most 27 vertices and 4-connected planar graphs of minimum degree 5 on at most 39 vertices. They also show a counterexample would follow from a planar 3-connected cubic digraph with an 'a-arc', and found none among the girth-4 planar cubic graphs with an a-edge up to 38 vertices. Target: a counterexample, or a larger verified range.

## What counts as a win

A full win is an explicit planar oriented graph D (arc list plus a planar embedding as a rotation system) such that (i) planarity is confirmed by two independent testers and the rotation system satisfies Euler's formula, (ii) D has no digons, and (iii) D has no vertex 2-partition into acyclic sets, certified by an UNSAT result with a DRAT/LRAT proof checked by drat-trim or cake_lpr for a CNF the skeptic regenerates (acyclicity encoded by, e.g., per-class topological-order variables or one clause per directed cycle when D is small). Knauer-Valicov arXiv 1712.06143 and a citation search, rerun before claiming, must still describe the conjecture as open.

## Partial wins

- **p1:** A rerunnable exhaustive verification that the conjecture holds for all planar graphs on 27 vertices (equivalently, by the Knauer-Valicov reduction, for orientations of all triangle-free non-Hamiltonian 3-connected planar cubic graphs on 50 vertices), with published code and the list of cubic graphs produced by two independent generators (e.g. plantri plus a Hamiltonicity filter, and McKay's lists where they reach) agreeing.
- **p2:** Verification for all 4-connected planar graphs on 28 vertices, or for 4-connected planar graphs of minimum degree 5 on 40 vertices, rerunnable as in p1.

## How a win is checked

Planarity and embedding checks; CNF regeneration and proof check for a counterexample; for p1-p2, rerun the published enumeration and compare counts with plantri/McKay data.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1712.06143>

## Sources

- <https://arxiv.org/abs/1712.06143>
- <https://users.cecs.anu.edu.au/~bdm/data/planegraphs.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Work in the dual: only non-Hamiltonian cyclically 4-edge-connected planar cubic graphs (Holton-McKay style lists) can be duals of minimal counterexamples; for each, decide by SAT whether some orientation makes every perfect matching contain a directed cut.
- Eulerian triangulations are named by Knauer-Valicov as the natural open special case: search orientations of Eulerian triangulations first.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Digons (pairs of opposite arcs) are excluded; with digons the statement is false.
- A Hamiltonian dual already gives a partition into two induced trees, so random triangulations are useless search space.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/neumann-lara-planar-2-dicolouring.md
```

Already set up? Say `run V3R1T4S on neumann-lara-planar-2-dicolouring`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `neumann-lara-planar-2-dicolouring`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
