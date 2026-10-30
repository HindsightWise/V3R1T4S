# MOONSHOT - Regular heptagons in the plane: a packing of congruent regular heptagons denser than the Kuperberg double lattice (0.8926906861...)

⚪ **Packings and physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours (small periodic cells; exact certification in seconds) · open as of 2026-10-30

## The problem

The densest packings of congruent regular polygons in the plane: even n-gons are centrally symmetric, and for those the lattice optimum is the packing optimum (L. Fejes Toth). Pentagons were settled by Hales and Kusner (arXiv:1602.07220, 2016): the pentagonal ice-ray double lattice with density (5-sqrt5)/3 is optimal. The regular heptagon is the next open case. Its densest double-lattice packing (G. Kuperberg and W. Kuperberg 1990, who showed that the densest double lattice of a convex disk K has density A(K)/(2*Delta(K)), with Delta the least area of an inscribed half-length parallelogram) has density (2/97)(-111+492u-356u^2) with u = cos(pi/7), i.e. 0.892690686126508075767... (Kallus, 'Pessimal packing shapes', Geom. Topol. 19 (2015), arXiv:1305.0289). Kallus proves the heptagon is a local minimum of the double-lattice density and conjectures it is the global pessimum. He notes that whether the heptagon's packing density delta equals its double-lattice density delta_L* is open. No better heptagon packing or proof was found in the sources checked on 2026-10-30. Numerically, the same A/(2*Delta) formula gives 0.9010300784 for the regular 9-gon and 0.9076648819 for the 11-gon, and it reproduces (5-sqrt5)/3 for the pentagon.

## What counts as a win

Success means a periodic packing of congruent regular heptagons: a lattice basis L and k heptagons, each given by a centre and a rotation angle, with vertices enclosed in 50-digit intervals or given exactly in Q(cos(pi/7), sin(pi/7)), such that (1) all pairs, including lattice images within 2*circumradius, have disjoint interiors, certified by a separating line per pair in interval or exact arithmetic, and (2) the certified lower bound of the density k*A/|det L| is STRICTLY GREATER (direction: max) than (2/97)(-111+492u-356u^2) = 0.8926906861265080757..., u = cos(pi/7), and than any denser heptagon packing published by verification time.

## Partial wins

- **p1:** Same certification for the regular 9-gon or 11-gon: a periodic packing whose certified density strictly exceeds that polygon's own Kuperberg double-lattice density, which the verifier recomputes with A/(2*Delta) (numerically, 2026-10-30: 0.9010300784 for n = 9, 0.9076648819 for n = 11), and any published value.
- **p2:** A counterexample to Kallus's conjecture: a convex polygon with rational vertices whose double-lattice density A/(2*Delta) is certified (exact minimisation over the finitely many combinatorial types of inscribed half-length parallelograms) to be strictly below 0.8926906861265.

## How a win is checked

Use interval arithmetic (mpmath iv or arb) at 50 digits. Construct the vertices, check separating lines for all neighbouring pairs, and compute the area and |det L| as intervals. For the bar, recompute Kallus's closed form, and for p1 compute Delta by minimising the half-length parallelogram area over directions: the area is piecewise algebraic in the direction, so minimise per edge-pair piece and certify with intervals. The heptagon check must reproduce 0.892690686126508 (an independent float computation matches it to 1e-15), and the pentagon must give (5-sqrt5)/3.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1305.0289>

## Sources

- <https://arxiv.org/abs/1305.0289>
- <https://arxiv.org/abs/1602.07220>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A double lattice re-expressed in a larger cell is not new: require a density strictly above the bar, not a re-parametrisation.
- Floating-point separating-line checks can accept overlaps at contacts; use interval arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/regular-heptagon-densest-packing.md
```

Already set up? Say `run V3R1T4S on regular-heptagon-densest-packing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `regular-heptagon-densest-packing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
