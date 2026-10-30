# MOONSHOT - Archimedean solids without central symmetry: beat 207/208 for truncated tetrahedra (Jiao-Torquato), or the lattice records 0.787699 / 0.788640 for the chiral snub cube and snub dodecahedron

⚪ **Packings and physics** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (floppy-box or adaptive-shrinking-cell Monte Carlo, small cells; exact check in minutes) · open as of 2026-10-30

## The problem

Three Archimedean solids lack a centre of symmetry: the truncated tetrahedron and the two chiral snubs. Torquato and Jiao (Phys. Rev. E 80, 041104 (2009), arXiv:0909.0940, Table IV) list the optimal Bravais-lattice densities of the Archimedean solids from Betke and Henk (Comput. Geom. 16 (2000), arXiv:math/9909172). These include the snub cube at 0.787699 and the snub dodecahedron at 0.788640. That paper wrongly calls the truncated tetrahedron the only non-centrally-symmetric Archimedean solid. Because the snubs lack central symmetry, non-lattice packings that use several rotated copies might be denser, as Torquato and Jiao conjecture is generic for shapes without central symmetry. Only proper motions are allowed: the point inversion x -> -x turns a chiral snub into its mirror image, which is not allowed here. Truncated tetrahedra: Conway and Torquato (PNAS 103 (2006) 10612) reached 23/24, de Graaf, van Roij and Dijkstra (PRL 107, 155501 (2011), arXiv:1107.0603) found a 0.988 dimer lattice, and Jiao and Torquato (J. Chem. Phys. 135, 151101 (2011), arXiv:1107.2300v4) built an analytic packing of density 207/208 = 0.995192... whose holes are small regular tetrahedra. Damasceno, Engel and Glotzer (ACS Nano 2012, arXiv:1109.1323) also reach 207/208 for this shape. It is believed optimal but this is not proven. De Graaf et al. state that their floppy-box runs reproduced the Archimedean literature values from below. Searches and fetches on 2026-10-30 found no later record for these three shapes. The de Graaf supplementary table (APS, returned 401) and the Damasceno-Engel-Glotzer Science 2012 supplement were not read.

## What counts as a win

Success means a periodic packing (lattice basis plus k congruent copies, each a rigid motion of one fixed solid with exact or certified vertex coordinates; for the snubs, mirror images are NOT allowed, since they are not congruent by a proper motion, only rotations and translations) such that (1) interiors are pairwise disjoint, certified exactly or by interval arithmetic with explicit separating planes for every pair within the circumradius cutoff, and (2) the density k*vol/|det L| is STRICTLY GREATER (direction: max) than the bar for that solid: 207/208 for the truncated tetrahedron, 0.787699 for the snub cube, 0.788640 for the snub dodecahedron. The bar is the max of these and any denser value published by verification time, including the de Graaf et al. 2011 supplementary table if the verifier can read it. Margin: 1e-6 above the 6-decimal table values for the snubs.

## Partial wins

- **p1:** A non-lattice periodic packing of snub cubes or snub dodecahedra (k >= 2 per primitive cell, proper rotations only) whose certified density equals or exceeds that solid's Betke-Henk lattice density minus 1e-4. This is evidence on the Torquato-Jiao generic non-lattice conjecture for chiral shapes.
- **p2:** An exact re-derivation of a lattice density for either snub that differs from the Table IV value of arXiv:0909.0940 in the 6th decimal or earlier, with the lattice certified as a packing and as locally optimal: a certified table correction.

## How a win is checked

Build the solid from exact vertex formulas (snub cube via the tribonacci constant, snub dodecahedron via the root of its cubic; use 50-digit interval enclosures). Apply the claimed rotations as rational quaternions, normalized exactly, or as interval matrices. Check pairwise non-overlap with separating planes verified in interval arithmetic, and compute volume and |det L| as intervals. Accept only if the lower end of the density interval exceeds the bar. Calibrate on the Betke-Henk lattice from Appendix A of arXiv:0909.0940 (recover 0.787699 and 0.788640) and on the 207/208 construction of arXiv:1107.2300.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1107.2300>

## Sources

- <https://arxiv.org/abs/0909.0940>
- <https://arxiv.org/abs/1107.2300>
- <https://arxiv.org/abs/1107.0603>
- <https://arxiv.org/abs/math/9909172>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For the snubs, try 2-particle cells pairing a copy with a copy turned by a proper rotation (e.g. 180 degrees about an axis that is not a symmetry axis of the solid), as in the dimer packings of tetrahedra. The point inversion x -> -x is not a proper motion and gives the mirror image of a chiral snub, so it is not allowed.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The snub cube and snub dodecahedron are chiral: their mirror images are not congruent by proper motions. Packings that mix enantiomers are a different problem.
- Torquato-Jiao's text calls the snubs centrally symmetric; they are not. Do not cite their conjecture as covering them.
- 207/208 leaves only tiny tetrahedral holes. Beating it is far less likely than the snub cases.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/truncated-tetrahedra-snub-solids-packing.md
```

Already set up? Say `run V3R1T4S on truncated-tetrahedra-snub-solids-packing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `truncated-tetrahedra-snub-solids-packing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
