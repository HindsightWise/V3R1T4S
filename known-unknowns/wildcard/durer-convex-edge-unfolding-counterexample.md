# MOONSHOT - Dürer's problem: a convex polyhedron with no edge unfolding to a net

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days for candidate search and exhaustive certification; any positive proof is pure thought · open as of 2026-10-30

## The problem

Dürer's problem (Shephard 1975; GFALOP Open Problem 21.1): does every convex polyhedron have an edge unfolding, a spanning tree of edges whose cutting unfolds the surface to a single non-overlapping planar polygon (a net, which may be weakly simple)? Demaine and O'Rourke's GFALOP update 22.1 (3 Sep 2025) says it remains open. Edge unfoldings are known for pyramids, prisms, prismoids, domes, convex generalized deltahedra, tall or rectangular-base prismatoids (Bian, Demaine and Madhukara 2021), nested prismatoids (Radons 2024), polar zonohedra (O'Rourke 2023), tapered polyhedra (O'Rourke and Vîlcu 2024), polyhedra with a Hamiltonian simple closed quasigeodesic (O'Rourke 2022), and nearly flat acutely triangulated convex caps, even closed by their base (O'Rourke 2018). Every convex polyhedron edge-unfolds after a suitable affine stretch (Ghomi 2014). The pseudo-edge generalisation fails (Barvinok and Ghomi, 340-vertex example). Akitaya, Demaine, Frei, Langerman, Lubiw and O'Rourke (arXiv 2607.09606, CCCG 2026) showed that for any thickness some convex polyhedron has an edge unfolding overlapping to that thickness; this does not settle the question. Prismatoids in general remain open (GFALOP 22.5 update).

## What counts as a win

(1) Exact rational vertex coordinates of a convex polyhedron P with exact convexity checks: every face planar and every dihedral angle below pi, with no coplanar adjacent faces. (2) A complete certificate that EVERY spanning tree of P's 1-skeleton gives an unfolding with strong overlap (two points interior to faces mapped to the same point; boundary-only contact does not count as overlap). The certificate can be an exhaustive enumeration or a branch-and-bound over dual spanning trees where each pruned branch carries an exact overlap witness among faces whose relative placement is already fixed. It must be reproduced by two independent implementations in exact arithmetic. (3) P lies in none of the proven-unfoldable classes listed on the GFALOP 22.5 update. (4) Literature check that the question is still open.

## Partial wins

- **p1:** A convex cap (the intersection of a convex polyhedron's surface with a closed halfspace, open along its planar rim), with exact coordinates, that has no edge unfolding. Every boundary-rooted spanning forest of its edges must give strong overlap: a forest of interior (non-rim) edges in which each tree contains exactly one rim vertex (its root) and the trees together span all interior vertices, as in O'Rourke (arXiv 1707.01006). It must be exhaustively certified as in criterion (2) and must not be acutely triangulated and nearly flat in O'Rourke's sense (that class unfolds). A literature check must find no prior example.
- **p2:** A machine-checked proof (Lean 4, Coq or Isabelle, kernel-checked) that every prismatoid, the convex hull of two convex polygons in parallel planes, has an edge unfolding to a net. The case is listed open in the GFALOP 22.5 update.

## How a win is checked

Check convexity exactly with rational arithmetic. Enumerate or replay the branch-and-bound over spanning trees: unfold each face by exact rational rotations (choose a coordinate frame where unfolding maps are rational, or use exact algebraic arithmetic) and test strong overlap with exact polygon-intersection predicates. Two independent codes must agree on the tree counts. For p2, compile the formal proof and audit the statement against the GFALOP definition.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.gfalop.org/updates/22.1.pdf>

## Sources

- <https://www.gfalop.org/updates/22.1.pdf>
- <https://www.gfalop.org/updates/22.5.pdf>
- <https://arxiv.org/abs/1908.07152>
- <https://arxiv.org/abs/2607.09606>
- <https://arxiv.org/abs/1707.01006>
- <https://arxiv.org/abs/1709.04944>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lucier (2006/2009) showed steepest-edge unfoldings can overlap for every direction. Use his local-overlap gadgets as building blocks and then kill the non-steepest trees.
- Random convex polytopes overlap for almost all trees. Search small, highly curved polytopes with few nets, using SAT or exact enumeration to count nets, and hill-climb on that count.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Weak (boundary) contact is allowed in a net. A certificate must show strong overlap.
- Floating-point unfolding gives false overlaps or false nets near touching configurations. Use exact arithmetic.
- Most random convex polytopes have some overlapping edge unfoldings; that is not a counterexample. Every spanning tree must fail.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/durer-convex-edge-unfolding-counterexample.md
```

Already set up? Say `run V3R1T4S on durer-convex-edge-unfolding-counterexample`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `durer-convex-edge-unfolding-counterexample`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
