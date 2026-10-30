# Positive-weight quadrature on the sphere S^2: exact to degree t with fewer nodes than Graef's and Lebedev-Laikov's rules

⚪ **Packings and physics** · standard · tractability ★★☆☆☆ · compute: laptop-hours (orbit-structured nonlinear least squares, then high-precision polishing) · open as of 2026-10-30

## The problem

Find M nodes on S^2 and positive weights such that the rule integrates every polynomial of degree <= t exactly, with M as small as possible (Gauss-type rules; equal weights give designs, a separate bank entry). Live tables (checked 2026-10-30): Manuel Graef's putatively optimal Gauss-type S^2 rules (TU Chemnitz quadrature page, dated 18 Nov 2016; files S2quads/N < t > _M < M > _ < group > .dat, coordinates and weights to 11 digits) for t = 1..30, 32, 34..39 and 44, e.g. t = 13: 64, 20: 148, 30: 322, 35: 422, 39: 522, 44: 672; and the Lebedev-Laikov octahedral rules (degrees 3..131, list at people.sc.fsu.edu/~jburkardt), e.g. 31: 350, 35: 434, 41: 590, 47: 770, 131: 5810. Not every posted rule is positive: Graef's files for t = 18 (M = 122), 24 (M = 210) and 38 (M = 508) and the Lebedev rules of degree 13, 25 and 27 contain negative weights (checked 2026-10-30), so they are not positive-rule records. The record M(t) is the minimum over the positive rules in both tables and the spherical-design records of rules exact to degree >= t. Where Graef has no positive rule of degree t the record comes from a neighbour: t = 18 (130, Graef degree 19), 24 (220, Graef degree 25), 31 (350, Lebedev), 33 (410, from degree 34), 38 (522, Graef degree 39), 40 and 41 (590, Lebedev 41), 42 and 43 (672, from degree 44). Graef's rules for t = 1, 2, 3, 5 (M = 2, 4, 6, 12) attain the Delsarte-Goethals-Seidel bound and are optimal. The McLaren efficiency (t+1)^2/(3M) of Graef's odd-degree rules with t >= 13 is 1.02-1.04, so the gaps look improvable. The Encyclopaedia of Cubature Formulas (bank target ecf-cubature-fewer-points) tabulates the solid ball, not the sphere surface. Other published S^2 rules (Ahrens-Beylkin 2009 icosahedral rules, whose efficiency is generally below 1, e.g. 192 nodes for degree 23; A. S. Popov) must be checked for every claim. A 2026-10-30 literature search found no 2024-2026 paper with positive S^2 rules on fewer nodes; search again before attacking and before claiming.

## What counts as a win

Success means a rule (M nodes on S^2, M positive weights) exact to degree t for some t at which Graef's Gauss-type table has a positive rule, other than t = 1, 2, 3, 5 (t = 4, 6..17, 19..23, 25..30, 32, 34..37, 39, 44), with M STRICTLY LESS (direction: min) than Graef's M(t), than every positive Lebedev-Laikov rule of degree >= t, and than every spherical-design record of strength >= t, all re-fetched before claiming, and not matched by any published rule the skeptic finds (check Ahrens-Beylkin 2009, Proc. R. Soc. A, and A. S. Popov's 1994-2008 papers). Verification from nodes and weights given to >= 32 digits, in >= 40-digit arithmetic with weights normalized to sum 1: all weights > 0, |sum w - 1| < 1e-30, and for every l = 1..t, (4 pi/(2l+1)) sum_k |sum_j w_j Y_lk(x_j)|^2 < 1e-40, computed from the weighted Weyl sums (the pair-sum form sum_{i,j} w_i w_j P_l(x_i . x_j) needs >= 60 digits). M must exceed the Delsarte-Goethals-Seidel bound for positive rules ((e+1)^2 for t = 2e, (e+1)(e+2) for t = 2e+1), else it is a bug.

## Partial wins

- **p1:** A positive rule exact to degree t for a gap degree t in {18, 24, 31, 33, 38, 40, 41, 42, 43} (no positive Graef rule of that exact degree) with M strictly below the merged positive record M(t) defined in the statement (18: 130, 24: 220, 31: 350, 33: 410, 38: 522, 40-41: 590, 42-43: 672, re-fetched) and not matched by any published rule the skeptic finds (Ahrens-Beylkin, Popov), same high-precision checks.
- **p2:** A positive rule exact to degree t for some t in 45..131 with M strictly below every Lebedev-Laikov rule of degree >= t, every design record of strength >= t and every published rule the skeptic finds (Ahrens-Beylkin 2009 icosahedral rules, Popov), AND McLaren efficiency (t+1)^2/(3M) > 1.0; same checks.
- **p3:** A positive-weight quadrature on SO(3) exact for all Wigner D-functions of degree <= N with fewer nodes than Graef's SO(3) Gauss-type table (N = 1..9, 11, 14: M = 4, 11, 23, 43, 60, 116, 168, 240, 300, 504, 960) and than any published SO(3) rule the skeptic finds, verified with the same residual standard on D-functions.

## How a win is checked

Checker (minutes): build M(t) from Graef's page (S2quads and S2designs links), the Burkardt Lebedev list and the design tables, keeping only rules whose posted weights are all > 0 (this drops Graef's t = 18, 24, 38 files and Lebedev's degree-13, 25, 27 rules). Load the claimed rule at 40 digits; normalize nodes and weights; assert positivity; compute Weyl sums sum_j w_j Y_lk(x_j) for l <= t by recurrence and the quadratic residuals; assert < 1e-40. Sanity: the same code on Graef's N044_M672_Ico.dat must give residuals ~1e-16 in double (11-digit data).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/>

## Sources

- <https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/>
- <https://www-user.tu-chemnitz.de/~potts/workgroup/graef/quadrature/S2quads/N044_M672_Ico.dat>
- <https://people.sc.fsu.edu/~jburkardt/datasets/sphere_lebedev_rule/sphere_lebedev_rule.html>
- <https://en.wikipedia.org/wiki/Lebedev_quadrature>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Gap degrees first (p1): Graef's neighbours at t = 30/32 (C4, T) and 34/35 (C4, C5) suggest the group and orbit structure to try at t = 31 and 33; solve the invariant moment equations with Levenberg-Marquardt from many orbit-mix choices.
- Node elimination (Xiao-Gimbutas style): start from a rule of degree t with M nodes, remove the smallest-weight node or orbit and re-solve; repeat while it converges.
- Caratheodory-Tchakaloff compression: an LP/NNLS on a dense candidate grid yields a positive rule with at most (t+1)^2 nodes, a start for nonlinear node elimination.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A rule with a tiny negative weight is not a positive rule.
- Exactness to 1e-16 in double is not exactness when the system is overdetermined; use the 30-digit standard.
- Do not compare Lebedev rules by order alone: a rule of degree t also counts for every lower degree.
- Graef's posted Gauss-type files for t = 18, 24 and 38 and the Lebedev rules of degree 13, 25 and 27 have negative weights. They are not positive-rule records; a rule that beats only them is a gap-degree claim (p1).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/spherical-quadrature-s2-positive-fewest-nodes.md
```

Already set up? Say `run V3R1T4S on spherical-quadrature-s2-positive-fewest-nodes`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `spherical-quadrature-s2-positive-fewest-nodes`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
