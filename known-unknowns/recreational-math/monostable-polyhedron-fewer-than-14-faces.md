# Monostable polyhedron with fewer faces: a homogeneous convex polyhedron that rests stably on only one face, with fewer than Reshetov's 14 faces

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-hours (exact-centroid optimisation over small polyhedra) · open as of 2026-10-30

## The problem

A homogeneous convex polyhedron is monostable (unistable, monostatic) if it can rest in stable equilibrium on only one of its faces: the centroid projects orthogonally into the relative interior of exactly one face. Conway, Goldberg, Guy and Knowlton described these shapes in 1969, and Conway showed that no tetrahedron is monostable. Guy and Knowlton independently built a 19-face example, Bezdek an 18-face one (2011), and Reshetov a 14-face one by computer search (IJCGA 24(1), 2014). Lángi (Bull. LMS 2022, arXiv 2008.02090) answered two of Conway's other questions on monostable polyhedra (near-spherical examples, and k-fold rotational symmetry for every k). As of Wikipedia's 'Monostatic polytope' article (edited 19 Oct 2026), 14 is the fewest faces known. The minimum number of faces is not determined: the only proven bound excludes tetrahedra.

## What counts as a win

A convex polyhedron given by exact rational vertex coordinates (the faces being the facets of their convex hull, computed exactly) with F faces, F STRICTLY LESS than 14 (direction: min) and less than any smaller count published by claim time (literature check). Compute the centroid of the homogeneous solid exactly (rational tetrahedral decomposition). For every face, test exactly whether the orthogonal projection of the centroid onto the face's plane lies in the face's relative interior. Exactly one face must pass, and the centroid must project onto no face's boundary (non-degenerate).

## Partial wins

- **p1:** An exact-rational monostable polyhedron with exactly 14 faces and fewer vertices than every published 14-face example (literature check, starting with Reshetov 2014), certified exactly as in the success criterion.
- **p2:** An exactly certified monostable polyhedron with at most 30 faces and an n-fold rotational symmetry axis for some n >= 3, with no such explicit example published before (literature check). Lángi proved such polyhedra exist for every n, but his construction approximates a sphere and is not explicit or small.

## How a win is checked

Rebuild the hull from rational vertices (exact arithmetic) and count facets, merging coplanar triangles. Compute volume and centroid exactly by signed tetrahedra from an interior point. For each facet, project the centroid onto the facet plane and test strict containment with exact orientation predicates. Count stable facets. All in rationals with sympy or fractions; seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Monostatic_polytope>

## Sources

- <https://en.wikipedia.org/wiki/Monostatic_polytope>
- <https://arxiv.org/abs/2008.02090>
- <https://doi.org/10.1142/S0218195914500022>
- <http://www.fields.utoronto.ca/av/slides/11-12/wksp_geometry/bezdek/download.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conway-Guy style spirals: a polygonal 'spiral' of faces whose successive tipping leads to one face. Optimise vertex positions with a smooth margin objective (minimum over unstable faces of how far the centroid's projection falls outside the face), then snap to rationals.
- Start from Reshetov's 14-face polyhedron and try face-merging moves that keep the stability margin positive.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Mono-unstable and mono-monostatic are different properties, and point-mass (non-homogeneous) models do not count.
- Floating-point centroids can misclassify faces with small margins. Certify in exact arithmetic.
- The status source is a general reference. Search the literature since 2022 for smaller examples before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/monostable-polyhedron-fewer-than-14-faces.md
```

Already set up? Say `run V3R1T4S on monostable-polyhedron-fewer-than-14-faces`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `monostable-polyhedron-fewer-than-14-faces`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
