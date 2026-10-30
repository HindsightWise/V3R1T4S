# Rupert's problem for the nine undecided classical solids: snub cube, snub dodecahedron, deltoidal and pentagonal hexecontahedra, Johnson solids J72-J75 and J77

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-days (passage search is laptop-hours; a non-Rupert certificate is days of exact-arithmetic box splitting) · open as of 2026-10-30

## The problem

A convex polyhedron P is Rupert if a congruent copy passes through a straight hole drilled in P. Equivalently, there are rotations R1, R2 and a planar translation t with pi(R1 P) + t inside the interior of pi(R2 P), where pi is orthogonal projection to the xy-plane. All 5 Platonic solids, 10 of 13 Archimedean, 11 of 13 Catalan and 87 of 92 Johnson solids are known to be Rupert. Contributors: Scriba (1968); Jerrard, Wetzel and Yuan (2017); Chai, Yuan and Zamfirescu (2018); Hoffmann (2019); Lavau (2019); Steininger and Yurkevich (Math. Comp. 2023); Fredriksson (arXiv 2210.00601); Gosain and Grimmer (arXiv 2509.08190, 2025). Steininger and Yurkevich (arXiv 2508.18475, v2 Jan 2026) proved that the 90-vertex Noperthedron is not Rupert. Bence Hervay (Zenodo 10.5281/zenodo.23013945, 28 Sep 2026) gave a computer-assisted exact-arithmetic proof that the rhombicosidodecahedron is not Rupert, settling the 2023 conjecture of Steininger and Yurkevich; MathWorld's Nopert Polyhedron page (updated 2026-10-29) lists it. As of 2026-10-30 nine classical solids remain undecided: the snub cube, the snub dodecahedron, the deltoidal hexecontahedron, the pentagonal hexecontahedron, and Johnson solids J72, J73, J74, J75 and J77 (gyrate, parabigyrate, metabigyrate and trigyrate rhombicosidodecahedra, and the paragyrate diminished rhombicosidodecahedron). Wikipedia (Prince Rupert's cube) lists these nine as open and, not yet recording Hervay's preprint, still leaves the rhombicosidodecahedron undecided too. Gosain and Grimmer ran 180 hours of high-precision local optimisation on each open Archimedean and Catalan solid and found no passage (best scale 0.999999999999); their Johnson table (16 hours per solid) gives no value for J72-J75 and J77.

## What counts as a win

Settle one of the nine solids, in either direction, for P given by its standard exact coordinates (dmccooey.com/polyhedra or the Wikipedia article for that solid). (a) RUPERT: an explicit passage given by rotations R1, R2 (rational entries via a rational quaternion or Cayley parametrisation, or exact algebraic numbers) and a rational translation t. Exact arithmetic, or outward-rounded interval arithmetic for the algebraic coordinates of the snubs, must show that every projected vertex of R1 P, shifted by t, lies strictly inside the convex hull of the projected vertices of R2 P, with a certified positive margin. (b) NOT RUPERT: a computer-assisted proof whose certificate covers the whole configuration space (every symmetry reduction proved in writing). An independent checker written from scratch must re-verify the full certificate in exact or rigorous interval arithmetic, in the style of github.com/Jakob256/Rupert or github.com/bence-hervay/nopert-rid. In both cases the solid must still be listed as open on the status source and in the literature at claim time.

## Partial wins

- **p1:** For one of the nine solids, a rigorous certificate (exact or outward-rounded interval arithmetic) that no Rupert passage exists in a stated region covering at least 99% of the symmetry-reduced configuration space, under the parametrisation and product measure of Steininger and Yurkevich (arXiv 2508.18475) or of Hervay's certificate. The region list and checker are published and re-run independently.
- **p2:** For one of the nine solids, a complete certificate of the 'global' stage of the Steininger-Yurkevich or Hervay method. Every configuration outside explicit neighbourhoods of a finite, listed set of touching configurations must be certified to contain no passage, so that only local analysis remains. Verified by an independent checker.
- **p3:** A from-scratch re-implementation, written independently of Hervay (a different language from his Rust prover and Python audit, exact arithmetic), that re-verifies every one of the 192,696 records of Hervay's rhombicosidodecahedron certificate (github.com/bence-hervay/nopert-rid, proof/results/full, SHA-256 as listed there) and the completeness of its cover, and reports full agreement, or reports a discrepancy with a minimal reproducing record.

## How a win is checked

For a passage, rebuild P from the published exact coordinates and apply the given rotations in exact rational (or interval) arithmetic. Project, compute the convex hull of the outer projection, and check each inner vertex with strict signed-area tests against every hull edge. The check takes seconds. For a non-Rupert proof, run the author's checker and an independent re-implementation, confirm that the certificate's cover of the reduced domain is complete, and audit the written symmetry-reduction lemmas.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Prince_Rupert%27s_cube>

## Sources

- <https://en.wikipedia.org/wiki/Prince_Rupert%27s_cube>
- <https://arxiv.org/abs/2508.18475>
- <https://arxiv.org/abs/2509.08190>
- <https://zenodo.org/doi/10.5281/zenodo.23013945>
- <https://github.com/bence-hervay/nopert-rid>
- <https://arxiv.org/abs/2112.13754>
- <https://arxiv.org/abs/2210.00601>
- <https://mathworld.wolfram.com/NopertPolyhedron.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The Johnson solids J72-J75 and J77 share most vertices with the rhombicosidodecahedron. Test whether Hervay's Domain, Global, Local and Exotic certificate components adapt after re-gyration or diminishing; a mostly reusable certificate would make these the easiest cells.
- The deltoidal hexecontahedron is centrally symmetric, so the Steininger-Yurkevich reduction to 5 dimensions applies. The pentagonal hexecontahedron and both snub solids are chiral (rotation symmetry only) and lack central symmetry, so the translation term must be kept.
- For passage search, restart Fredriksson's or Gosain-Grimmer's optimiser from orientations far from the projections already explored. Their reported optima sit at scale 1 - 1e-12, which suggests touching configurations.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The rhombicosidodecahedron is settled (Hervay 2026 preprint, MathWorld updated 2026-10-29). Do not target it.
- A floating-point 'passage' at scale 1 +/- 1e-12 is not a passage. Only certified strict containment counts.
- A passage for the dual solid is not one for the solid: Gosain-Grimmer found large gaps between dual pairs.
- Hervay's RID proof is a preprint. Treat its methods as a guide, not as a peer-reviewed theorem.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/rupert-open-classical-solids.md
```

Already set up? Say `run V3R1T4S on rupert-open-classical-solids`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rupert-open-classical-solids`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
