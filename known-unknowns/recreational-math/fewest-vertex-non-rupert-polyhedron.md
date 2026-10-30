# Simplest non-Rupert polyhedron: certify a convex polyhedron with fewer than 60 vertices that is not Rupert (Zeng's 8-vertex stellated tetrahedron P_11/20 is the leading candidate)

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact or interval box-splitting of a 5- to 6-dimensional configuration space) · open as of 2026-10-30

## The problem

Only two convex polyhedra are proven not Rupert: the 90-vertex Noperthedron (Steininger and Yurkevich, arXiv 2508.18475, 2025) and the 60-vertex rhombicosidodecahedron (Bence Hervay, Zenodo, 28 Sep 2026, with an exact-arithmetic Rust certificate and a Python audit at github.com/bence-hervay/nopert-rid). MathWorld's 'Nopert Polyhedron' page (updated 2026-10-29) lists exactly these two. Tony Zeng (arXiv 2604.26531, Apr 2026) asked for the 'simplest' non-Rupert polyhedron. He conjectured that the 8-vertex stellated tetrahedron P_a with vertices (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1), (-a,-a,-a), (-a,a,a), (a,-a,a), (a,a,-a), a = 11/20, is not Rupert: his code found no passage for any a in (0.5, 0.57). He gave numerical (floating-point LP, not rigorous) evidence that over 88% of his parameter space Lambda = [0,2pi]^2 x [0,pi] x [0,pi/2]^2 contains no passage, and he has no local theorem, because P_a is not centrally symmetric and the translation term cannot be removed. Find and certify a non-Rupert convex polyhedron with fewer vertices than any proven so far. (Proving one of the classical solids of rupert-open-classical-solids non-Rupert, e.g. the 24-vertex snub cube, would also count here.)

## What counts as a win

A convex polyhedron P with exact rational (or explicitly algebraic) vertex coordinates and V vertices, with V STRICTLY LESS than the smallest vertex count of any convex polyhedron proven non-Rupert at verification time (60 as of 2026-10-30, the rhombicosidodecahedron). It must come with a complete computer-assisted proof that no rotations R1, R2 and translation t give pi(R1 P) + t inside the interior of pi(R2 P). The certificate must cover the whole configuration space (every symmetry reduction proved in writing), including all touching or local configurations. It must be re-verified end to end by an independent checker in exact or outward-rounded interval arithmetic. Direction: min V.

## Partial wins

- **p1:** For Zeng's P_11/20, a rigorous certificate (exact or outward-rounded interval arithmetic, independent checker) that no Rupert passage exists on a region of Zeng's parameter space Lambda of product measure at least 99% (Zeng's 88% is numerical only).
- **p2:** A certified Rupert passage (rational rotations and translation, strict containment checked exactly) for P_a with some rational a in (0.5, 0.57), refuting Zeng's candidate family.
- **p3:** A certified local theorem for P_11/20: an explicit epsilon > 0 and a proof, by exact certificate or machine-checked argument, that no passage exists with R2 within epsilon of g R1 for any symmetry g of P_11/20 (any translation). Zeng states the lack of such a local theory is what blocks a full proof.

## How a win is checked

Rebuild P exactly and confirm convexity and the vertex count with exact hull code. Run the submitted checker, then an independent re-implementation that re-verifies every box of the cover with rational or outward-rounded interval arithmetic. Confirm that the boxes cover the stated domain and audit the written reductions. For p2, check strict containment of the projected vertices exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mathworld.wolfram.com/NopertPolyhedron.html>

## Sources

- <https://arxiv.org/abs/2604.26531>
- <https://arxiv.org/abs/2508.18475>
- <https://github.com/bence-hervay/nopert-rid>
- <https://mathworld.wolfram.com/NopertPolyhedron.html>
- <https://github.com/Jakob256/Rupert>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Design the candidate for provability, as Steininger and Yurkevich did: centrally symmetric (this removes the translation and gives a 5-dimensional search) and free of mirror symmetry, so their local theorem applies in every direction, but with far fewer than 60 vertices.
- Hervay's lemma (divide a necessary inequality by the distance to the touching set, then certify its sign with Bernstein coefficients) handles touching configurations. It may give the local theorem Zeng lacks.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Numerical failure to find a passage proves nothing (MathWorld says so explicitly).
- Non-convex polyhedra do not count: P must be the convex hull of its vertices.
- Check the status source at claim time: a smaller nopert may appear first, and the target moves with it.
- The 60-vertex bar rests on unrefereed preprints: Hervay's Zenodo v1 (28 Sep 2026) and a separate claim for the same solid by Jung Gi-hyo (Zenodo/GitHub, 5 Oct 2026). If both are withdrawn or refuted, the bar goes back to the Noperthedron's 90. Re-check their status, and MathWorld's, before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/fewest-vertex-non-rupert-polyhedron.md
```

Already set up? Say `run V3R1T4S on fewest-vertex-non-rupert-polyhedron`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fewest-vertex-non-rupert-polyhedron`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
