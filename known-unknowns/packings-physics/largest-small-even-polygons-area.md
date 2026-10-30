# Largest small polygons: a convex n-gon of diameter 1 with larger area than Bingane-Mossinghoff's P_n* for some even n = 14..120

⚪ **Packings and physics** · standard · tractability ★☆☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

A polygon is small if its diameter is 1. For odd n the regular n-gon has maximal area (Reinhardt 1922). For even n the optimum is known only for n = 4, 6 (Graham 1975), 8 (Audet, Hansen, Messine and Xiong 2002), 10 and 12 (Henrion and Messine 2013). Foster and Szabo (2007) proved Graham's conjecture on the diameter graph of an optimal polygon, a cycle of n-1 diameters plus a pendant edge. Uniqueness and axial symmetry of the optimum are open. Christian Bingane and Michael J. Mossinghoff ('Small polygons with large area', J. Global Optim. 88(4) (2024) 1035-1050, arXiv:2204.04547, Table 4) computed P_n*, the best axially symmetric small n-gon in the Foster-Szabo skeleton, for n = 14, 16, ..., 24, 30, 40, ..., 120. Their values match or slightly exceed the earlier literature (Mossinghoff 2006, Pinter et al. 2021, Bingane 2021) and are the current records, e.g. A(P_14*) = 0.7675310111, A(P_16*) = 0.7718613220, A(P_120*) = 0.7851717941. Code and coordinates are in OPTIGON (github.com/cbingane/optigon). Mulansky and Potschka (Math. Program. 2025) settle the analogous perimeter problem numerically to 90 digits under a symmetry conjecture, but leave area untouched. A plain SLSQP multistart run on 2026-10-30 reproduced A(P_14*) to 10 digits, so the records are sharp under symmetry. A win most likely needs an asymmetric polygon, which would refute the symmetry expectation, or a better symmetric basin for large n.

## What counts as a win

Success means the n vertices ( > = 25 significant digits, in cyclic order) of a convex polygon, for an even n listed in Table 4 of arXiv:2204.04547 with n >= 14, such that, in mpmath at 50 digits: every pairwise vertex distance is <= 1 (after rescaling by the computed diameter, the area is divided by diam^2); the polygon is strictly convex and simple (all consecutive cross products > 0 and total turning exactly 2 pi); and the shoelace area is STRICTLY GREATER (direction: max) than A(P_n*) in Table 4 by at least 1e-9. Also, no larger value for n is found in an arXiv / Google Scholar check ('small polygon' 'maximal area' n), including any OPTIGON update.

## Partial wins

- **p1:** For some listed even n >= 14, a strictly convex small n-gon that is a numerically certified local maximiser of area (KKT residual < 1e-20 in mpmath for the diameter-constrained problem, with a positive-definite reduced Hessian of the Lagrangian) and has no axis of symmetry (no reflection maps the vertex set to itself within 1e-6), with area within 1e-7 of A(P_n*): a competing asymmetric basin, not a perturbation of P_n*.
- **p2:** For an even n in 26..118 not listed in Table 4, a certified small n-gon (same checker as the full win) whose area beats, by at least 1e-9, the optimum of the paper's symmetric problem (16) at that n, as computed by the skeptic with OPTIGON's AMPL model max_area/ampl_max_area_diameter.mod (param n set to that n, Ipopt, its built-in initial angles plus at least 20 random starts) and reported to 12 digits. Reported as beating the symmetric optimum, not a published record.

## How a win is checked

Checker (seconds): mpmath at 50 digits. Compute the diameter as the maximum over all vertex pairs and rescale. Check strict convexity via cross products and the turning number via the sum of exterior angles. Compute the shoelace area and compare with Table 4 (10 decimals). Reproduce A(P_n*) from Table 3 angles or OPTIGON for the same n first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2204.04547>

## Sources

- <https://arxiv.org/abs/2204.04547>
- <https://github.com/cbingane/optigon>
- <https://arxiv.org/abs/2110.11741>
- <https://link.springer.com/10.1007/s10898-023-01329-1>
- <https://doi.org/10.1007/s10107-025-02244-x>
- <https://en.wikipedia.org/wiki/Biggest_little_polygon>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Shoelace area of a non-simple polygon (winding twice) silently doubles: an unconstrained optimiser on 14 vertices 'found' area 1.39 > pi/4 on 2026-10-30. Always check convexity and turning number.
- Diameter <= 1 must hold for ALL vertex pairs, not only the diameter-graph edges, and in high precision. Use the scale-invariant area / diam^2.
- Odd n and n <= 12 are solved, so a 'win' there is a bug. Perimeter and width records are different problems and do not count here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/largest-small-even-polygons-area.md
```

Already set up? Say `run V3R1T4S on largest-small-even-polygons-area`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `largest-small-even-polygons-area`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
