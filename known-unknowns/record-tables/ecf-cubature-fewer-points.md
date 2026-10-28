# Cubature: a positive-interior (PI) rule with fewer points than the best known for a standard region and degree

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Ronald Cools' Encyclopaedia of Cubature Formulas (nines.cs.kuleuven.be/ecf, KU Leuven) tabulates, for each standard region (square, cube, disk, ball, triangle, tetrahedron, hexagon and others) and polynomial degree, the known numbers of points N and their quality (P = positive weights, I = all points inside; '*' marks a rule attaining a known lower bound). The public overview tables are free to read, while the point files need a login. The site index was last modified 2022 and the tables page 2004. Later literature improved some entries, e.g. symmetric rules by Witherden-Vincent 2015 (polyquad), Xiao-Gimbutas 2010, Papanicolopulos 2015-2016 and Jaśkowiec-Sukumar 2019-2020. For many (region, degree) pairs the best PI rule is not known to be minimal. Can a PI rule be found with strictly fewer points than every published PI rule for some region and degree?

## What counts as a win

For a region R with an ECF overview table and a degree d whose best PI entry in that table is not marked '*': a saved rule (points, weights) with every weight > 0 and every point strictly inside R, exact for all polynomials of degree <= d. Exactness is checked in mpmath at 50 digits against the exact integral of every monomial of degree <= d, with maximum absolute error below 1e-30 times the integral of 1 over R, after Newton polishing. The rule's point count N must be STRICTLY LESS (direction: min) than both (a) the smallest PI entry for (R,d) in the ECF table, re-fetched live immediately before claiming, and (b) the smallest PI rule for (R,d) published in Witherden-Vincent (polyquad), Xiao-Gimbutas, Papanicolopulos, Jaśkowiec-Sukumar, or any other paper or software collection (e.g. quadpy) the skeptic finds. N must not fall below a proven lower bound (Möller, Mysovskikh); a rule below one means a bug.

## Partial wins

- **p1:** A fully symmetric PI rule for (R,d) whose N equals the best known N, where every published rule with that N is only PO, NI or worse, upgrading the quality. Checked by the same exactness, positivity and interiority tests.
- **p2:** A PI rule for the square or triangle at degree >= 25 with fewer points than any published fully symmetric PI rule for that degree, under the same checks.

## How a win is checked

Skeptic evaluates the rule on all monomials up to degree d in mpmath (exact monomial integrals over R), checks positivity and interiority, and compares N to the live ECF table and cited papers. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://nines.cs.kuleuven.be/ecf/tables.html>

## Sources

- <https://nines.cs.kuleuven.be/ecf/>
- <https://nines.cs.kuleuven.be/ecf/tables.html>
- <https://nines.cs.kuleuven.be/ecf/c2.html>
- <https://people.sc.fsu.edu/~jburkardt/datasets/quadrature_rules_tri/quadrature_rules_tri.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: symmetry-orbit ansatz + Levenberg-Marquardt on moment equations with point-elimination (Xiao-Gimbutas node elimination).
- Conventional: start from the best known rule and try to delete one orbit, re-solving with Newton.
- Cross-domain import (sparse signal recovery): L1 / Caratheodory-Tchakaloff compression of a dense rule (NNLS / LP) to a minimal positive support.
- Cross-domain import (molecular conformer search): basin-hopping over orbit parameters with repulsion terms to keep points interior.
- Cross-domain import (coding theory): treat rules as designs and use linear-programming bounds to target degrees where the gap to the lower bound is largest.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The ECF tables are stale; many entries were beaten after 2002 - compare against the literature sources too.
- Numerical exactness at 1e-12 is not exactness; polish to high precision and check all monomials.
- Points on the boundary or slightly outside (I vs O quality) and tiny negative weights disqualify a PI claim.
- The ECF point files are password-protected; do not request credentials - use the public overview tables only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/ecf-cubature-fewer-points.md
```

Already set up? Say `run V3R1T4S on ecf-cubature-fewer-points`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ecf-cubature-fewer-points`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
