# MOONSHOT - Torquato-Jiao conjecture: a non-lattice packing of a centrally symmetric Platonic or Archimedean solid denser than its optimal lattice packing

⚪ **Packings and physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days (multi-particle periodic compression; exact certification in minutes) · open as of 2026-10-30

## The problem

Torquato and Jiao (Nature 460, 876 (2009), arXiv:0908.4107; full version Phys. Rev. E 80, 041104, arXiv:0909.0940) conjectured that the densest packings of the centrally symmetric Platonic and Archimedean solids are their optimal Bravais lattice packings, an analogue of Kepler's conjecture. The lattice optima come from Minkowski (octahedron 18/19), Betke and Henk (Comput. Geom. 16 (2000) 157-186, arXiv:math/9909172) and Hoylman. Non-tiling cases with their Table III/IV lattice densities: icosahedron 0.836357, dodecahedron 0.904508 = (5+sqrt5)/8, octahedron 18/19 = 0.947368, truncated icosahedron 0.784987, rhombicosidodecahedron 0.804708, truncated icosidodecahedron 0.827213, truncated cuboctahedron 0.849373, icosidodecahedron 0.864720, rhombicuboctahedron 0.875805, truncated dodecahedron 0.897787, cuboctahedron 45/49 = 0.918367, truncated cube 0.973747. Wikipedia's Packing problems page (fetched 2026-10-30) still says simulations only 'suggest' these lattices are optimal. For octahedra the best rigorous upper bound is 1 - 1.4e-12 (Gravel-Elser-Kallus 2011). Jiao, Stillinger and Torquato (PRE 79, 041309 (2009), arXiv:0902.1504) made the same lattice-optimality conjecture for superballs |x|^2p+|y|^2p+|z|^2p <= 1, p >= 1/2, with candidate lattices O0/O1 (1/2 <= p <= 1) and C0/C1 (p >= 1). Ni, Gantapara, de Graaf, van Roij and Dijkstra (Soft Matter 8 (2012), arXiv:1111.4357) then found Bravais crystals denser than O0 and O1 for 1/2 < p < 1 (bct 0.7661 against 0.7656 at p = 0.85; deformed bcc 0.832839 against 0.824976 at p = 0.7). Those candidate lattices are therefore not optimal, but no non-lattice superball packing is known to beat the best lattice. De Graaf et al. (2011) report the same lattice behaviour for centrally symmetric Johnson and Catalan solids. No counterexample is known.

## What counts as a win

Success means a periodic, non-Bravais packing (lattice basis L plus k >= 2 congruent copies per primitive cell, proper rigid motions, exact or 50-digit interval vertex coordinates) of one of the twelve centrally symmetric non-tiling solids listed in the statement, such that pairwise interiors are disjoint (certified by a separating plane for each pair within the circumradius cutoff, checked in exact or interval arithmetic) and the certified lower end of the density interval k*vol/|det L| is STRICTLY GREATER (direction: max) than that solid's optimal lattice density (exact value for 18/19, 45/49 and (5+sqrt5)/8; otherwise the Betke-Henk value recomputed exactly by the verifier from arXiv:math/9909172 or Appendix A of arXiv:0909.0940, and at least 1e-6 above the 6-decimal value).

## Partial wins

- **p1:** Superballs: for some exactly stated p >= 1/2, p != 1, a periodic packing of the superball |x|^2p+|y|^2p+|z|^2p <= 1 whose certified density strictly exceeds both the best Jiao-Stillinger-Torquato candidate lattice at that p (O0/O1 for 1/2 <= p <= 1, C0/C1 for p >= 1, arXiv:0902.1504, recomputed by the verifier) and every published packing at that p. For 1/2 < p < 1 that includes the denser Bravais crystals of Ni et al. (arXiv:1111.4357), which already beat O0/O1 (e.g. 0.832839 at p = 0.7), so beating O0/O1 alone is not a win.
- **p2:** A rigorous upper bound on the density of regular octahedron packings strictly below 1 - 1.4e-12 (Gravel-Elser-Kallus, arXiv:1008.2830), delivered as a re-runnable exact or interval computation with a written reduction that the skeptic re-executes.

## How a win is checked

Exact vertex formulas in Q(sqrt2, sqrt5) or 50-digit intervals. Rotations are interval matrices from rational quaternions. For each pair, check a separating plane against all vertices in interval arithmetic. Density uses exact volumes and an interval determinant. Calibrate by reproducing each Betke-Henk lattice from Appendix A of arXiv:0909.0940 and checking that it is a packing with the tabulated density. For superballs, overlap needs a certified test, e.g. a separating plane checked against support functions in interval arithmetic.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/0909.0940>

## Sources

- <https://arxiv.org/abs/0909.0940>
- <https://arxiv.org/abs/0908.4107>
- <https://arxiv.org/abs/math/9909172>
- <https://arxiv.org/abs/0902.1504>
- <https://arxiv.org/abs/1111.4357>
- <https://arxiv.org/abs/1008.2830>
- <https://en.wikipedia.org/wiki/Packing_problems>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A Bravais lattice re-expressed with a supercell (k copies, identical orientations, lattice-related positions) is not a new packing. Require at least two distinct orientations or a non-lattice translate set.
- The cube and truncated octahedron tile space (density 1) and are excluded.
- Six-decimal table values are rounded: recompute the lattice optimum exactly before claiming a 1e-6 win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/torquato-jiao-centrosymmetric-polyhedra.md
```

Already set up? Say `run V3R1T4S on torquato-jiao-centrosymmetric-polyhedra`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `torquato-jiao-centrosymmetric-polyhedra`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
