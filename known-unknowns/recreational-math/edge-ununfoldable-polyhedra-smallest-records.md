# Smallest edge-ununfoldable polyhedra in restricted classes: triangulated with fewer than 20 vertices, convex-faced with fewer than 13 faces, or stacked with acute triangles

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (exhaustive spanning-tree certification for polyhedra with fewer than 20 vertices) · open as of 2026-10-30

## The problem

Some non-convex but topologically convex polyhedra (1-skeleton isomorphic to that of a convex polyhedron) have no edge unfolding to a net. Records per face class: all faces triangles, 36 faces and 20 vertices (Bern, Demaine, Eppstein, Kuo, Mantler and Snoeyink, CGTA 2003, 'hat' constructions; the same paper gives a 24-face convex-faced example); all faces convex polygons, 13 faces and 13 vertices (Grünbaum). Akitaya, Demaine, Eppstein, Tachi and Uehara (JCDCGGG 2019; CGTA 103, 2022) found ununfoldable topologically convex polyhedra with 7 vertices and 6 faces and with 6 vertices and 7 faces (their faces include non-convex polygons), and listed improving the triangular (36 faces, 20 vertices) and convex-faced (13, 13) records as future work. The GFALOP update 22.4 (3 Sep 2025) adds that it is still open whether 5 or 6 faces/vertices are possible. Demaine, Demaine and Eppstein (CCCG 2020, arXiv 2007.14525) built ununfoldable polyhedra with all faces acute triangles and ununfoldable stacked polyhedra, and left open whether an ununfoldable STACKED polyhedron with all faces ACUTE triangles exists. GFALOP 22.4 lists no smaller triangular or convex-faced examples.

## What counts as a win

An embedded, topologically convex polyhedron P with exact rational vertex coordinates, plus a complete certificate that every spanning tree of its edges unfolds with strong overlap (two face-interior points coinciding). The certificate is an exhaustive enumeration, or a branch-and-bound over dual spanning trees with exact overlap witnesses, reproduced by two independent exact-arithmetic implementations. P must satisfy one of the following. (A) All faces triangles and strictly fewer than 20 vertices. (B) All faces strictly convex polygons and strictly fewer than 13 faces, or strictly fewer than 13 vertices. (C) P is a stacked polyhedron (tetrahedra glued face to face in a tree pattern, the result embedded) and every face angle is strictly below 90 degrees; any size. Records are those in the status source and the literature at claim time (direction: min).

## Partial wins

- **p1:** An exact computer certificate of edge-ununfoldability for a published example, where none has been published before (literature check): explicit rational coordinates realising Bern et al.'s 36-triangle polyhedron or Grünbaum's 13-face polyhedron (matching the published combinatorics and inequalities), with an exhaustive two-implementation check that all spanning trees overlap.
- **p2:** An edge-ununfoldable topologically convex polyhedron with all faces strictly convex, 13 faces and 13 vertices, not combinatorially equivalent to Grünbaum's example, exactly certified as in the success criterion.

## How a win is checked

Check embeddedness (faces meet only in shared edges and vertices) and planarity and convexity of faces in exact arithmetic, and check topological convexity (3-connected planar 1-skeleton). Replay the spanning-tree enumeration or branch-and-bound: unfold along each dual tree with exact maps and test strong overlap with exact predicates. Compare tree counts with the matrix-tree theorem. For (C), check the stacking sequence and every face angle exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.gfalop.org/updates/22.4.pdf>

## Sources

- <https://www.gfalop.org/updates/22.4.pdf>
- <https://erikdemaine.org/papers/MinimalUnunfoldable_JCDCGGG2019/paper.pdf>
- <https://arxiv.org/abs/2007.14525>
- <https://erikdemaine.org/papers/Ununfoldable/paper.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Leaves of a cut tree cannot sit at negatively curved vertices, and every negatively curved vertex needs at least 2 cut edges. Concentrating negative curvature cuts the space of admissible trees drastically, as in Akitaya et al.'s 6-vertex example; transplant that idea to triangulations.
- Search over triangulated spheres with 10-19 vertices (plantri) and optimise coordinates to maximise forced overlaps, then certify exactly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A triangulated sphere with V vertices always has 2V - 4 faces, so the triangular record is a vertex count.
- Self-intersecting realisations are not polyhedra. Check embeddedness exactly.
- Tarasov's examples and the very-ununfoldable families: do a literature check before claiming a record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/edge-ununfoldable-polyhedra-smallest-records.md
```

Already set up? Say `run V3R1T4S on edge-ununfoldable-polyhedra-smallest-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `edge-ununfoldable-polyhedra-smallest-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
