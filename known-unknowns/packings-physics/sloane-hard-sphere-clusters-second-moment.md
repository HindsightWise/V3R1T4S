# Minimal-energy clusters of hard spheres: N unit spheres in R^3 (N <= 99) or R^4 (N <= 32) with smaller second moment than the Sloane-Hardin-Duff-Conway table

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Arrange N non-overlapping unit spheres (centres at mutual distance >= 2) to minimise the second moment sum_i |x_i - c|^2 about their centroid c. This is the hard-sphere limit of cluster energy minimisation, and the minimisers interpolate between close-packed and spherical clusters. N. J. A. Sloane, R. H. Hardin, T. D. S. Duff and J. H. Conway ('Minimal-energy clusters of hard spheres', Discrete Comput. Geom. 14 (1995), 237-259) tabulated putative minima for n = 3, N = 4..99 (96 rows, e.g. N = 13: 47.7012169, N = 99: 1532.2299539) and n = 4, N = 5..32 (28 rows, N = 32: 145.0449556). Henry Cohn now maintains the table (cohn.mit.edu/sloane, 7 decimals rounded UP, files clust-n-N.txt, data set hdl.handle.net/1721.1/147004) and asks for improvements. The small cases are easy to check by hand: N = 4 gives 6 (tetrahedron of edge 2) and N = 6 gives 12 (octahedron). The 1995 searches are three decades old, and the problem has received far less attention than Lennard-Jones or Morse clusters.

## What counts as a win

Success means N points in R^n (n = 3 or 4; >= 20 significant digits) for an (n, N) row of the live table at https://cohn.mit.edu/sloane (re-fetched immediately before claiming), whose scale-invariant moment M* = (4 / d_min^2) * sum_i |x_i - c|^2 is STRICTLY LOWER (direction: min) than the table's moment for (n, N) by at least 1e-6, computed in mpmath at 40 digits with d_min the minimal pairwise distance and c the centroid. Also, no published value for (n, N) found in an arXiv / Google Scholar search ('hard sphere' 'second moment' OR 'moment of inertia' cluster) is lower than M*.

## Partial wins

- **p1:** A table-integrity finding: at least one posted clust-n-N.txt that violates d_min >= 2 by more than 1e-7, or whose scale-invariant moment M* does not reproduce the table's moment for (n, N) to within 1e-6, reported with both values.
- **p2:** For some n = 3 row with N >= 20, a configuration whose M* is within 1e-7 of the table value (allowing for 7-decimal rounding) but whose contact graph (pairs with distance <= 2(1 + 1e-9) after rescaling to d_min = 2) is not isomorphic to that of the posted file: a degenerate competing minimum, checked with networkx isomorphism.

## How a win is checked

Checker (seconds): load coordinates, compute d_min and the centroid moment in mpmath, form M* = 4 M / d_min^2 (which rescales any configuration to unit-radius spheres), and compare with the live table. Run the same computation on the posted file for (n, N) to confirm it reproduces the table value.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cohn.mit.edu/sloane>

## Sources

- <https://cohn.mit.edu/sloane>
- <https://doi.org/10.1007/BF02570704>
- <https://hdl.handle.net/1721.1/147004>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Treat it as a cluster global optimisation with a hard-core constraint: basin hopping on a steep soft repulsion plus a harmonic trap (moment term), annealing the repulsion exponent to infinity, then a final active-set QP on the contact graph.
- Seed from Lennard-Jones, Morse (long-range) and sticky-hard-sphere cluster minima at the same N (CCD), which share compact polytetrahedral and decahedral motifs.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Normalisation: the table uses unit RADIUS (centres >= 2 apart), so N = 4 gives 6.0. Using unit diameter gives values 4 times smaller.
- Small overlaps lower the moment. Always use the scale-invariant M*, never the raw moment with a tolerance.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/sloane-hard-sphere-clusters-second-moment.md
```

Already set up? Say `run V3R1T4S on sloane-hard-sphere-clusters-second-moment`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sloane-hard-sphere-clusters-second-moment`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
