# Hilbert's 16th problem for invariant tori in 3D: more normally hyperbolic limit tori than N_h(2) >= 3, N_h(3) >= 5, N_h(4) >= 7, N_h(5) >= 13

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (exact averaged functions and root isolation; validated numerics for p1) · open as of 2026-10-30

## The problem

Douglas Novaes and Pedro Pereira (arXiv 2212.12006, v2 Sept 2024) posed a 3D version of Hilbert's 16th problem: the maximal number of isolated, normally hyperbolic invariant tori of a polynomial vector field of degree m in R^3. Using averaging they showed growth at least m^3/128. Lucas Queiroz Arakaki, Luiz F. S. Gouveia and Douglas Novaes (arXiv 2507.17932, July 2025) studied families near Hopf-zero and nilpotent-zero monodromic singularities and proved N_h(2) >= 3, N_h(3) >= 5, N_h(4) >= 7 and N_h(5) >= 13, which they describe as the best available lower bounds. They extend these to higher degrees by strict monotonicity and a Christopher-Lloyd-type recursion.

## What counts as a win

For some m in 2..5, an explicit degree-m polynomial vector field family in R^3 with at least N + 1 normally hyperbolic limit tori, where N = 3, 5, 7, 13 for m = 2..5 (direction: max), also beating any value found by a literature search re-run just before claiming. Certified by an exact-arithmetic check of every hypothesis of a cited averaging theorem for invariant tori (Novaes-Pereira 2022 or Arakaki-Gouveia-Novaes 2025 form): the first non-vanishing averaged function is computed exactly, and its N + 1 simple zeros in the admissible domain are isolated by Sturm sequences or interval Newton, with the non-degeneracy conditions the theorem needs.

## Partial wins

- **p1:** A validated-numerics certificate (interval Poincaré map on a 2D section, with an invariant-circle validation for the section map) showing 3 normally hyperbolic invariant tori in an explicit quadratic 3D field at one explicit rational parameter value, not only for epsilon small enough.

## How a win is checked

Skeptic: recompute the averaged function of the posted family in exact arithmetic (Sage or Mathematica), re-run the Sturm or interval root isolation, check the theorem's hypotheses (smoothness, the transformation to the standard averaging form, Jacobian non-vanishing at each zero), and confirm the degree of the vector field. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2507.17932>

## Sources

- <https://arxiv.org/abs/2507.17932>
- <https://arxiv.org/abs/2212.12006>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Tori coming from planar limit cycles in a degree-m/2 - 1 subsystem must be counted with the degree bookkeeping of Novaes-Pereira; a degree slip gives a false record.
- A young area: re-check arXiv for 2026 papers by Novaes, Gouveia or coauthors before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/limit-tori-3d-polynomial-hilbert-numbers.md
```

Already set up? Say `run V3R1T4S on limit-tori-3d-polynomial-hilbert-numbers`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `limit-tori-3d-polynomial-hilbert-numbers`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
