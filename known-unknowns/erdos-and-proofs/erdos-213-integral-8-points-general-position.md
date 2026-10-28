# Erdos #213: eight points in the plane, no three on a line, no four on a circle, all distances integers

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Are there n points in the plane, no three collinear and no four concyclic, with all pairwise distances integers, for every n? Anning and Erdos (1945) showed no infinite set exists; Harborth found n = 5; the best known is n = 7, found by Kreisel and Kurz (2008) by computer search. Greenfeld, Iliopoulou and Peluse (2024) showed such sets in [-N,N]^2 have size (log N)^{O(1)}; Ascher, Braune and Turchet showed a uniform bound conditional on Bombieri-Lang. A September 2026 forum post reports AI-assisted relaxed searches for n = 8 only found sets with all points on a line or circle. Target: an explicit 8-point set in general position with integer distances.

## What counts as a win

Success means 8 points given by exact coordinates (integer distances force coordinates of the form (a, b sqrt(q)) up to rigid motion; give them in that exact form) such that, in exact integer arithmetic: all 28 pairwise squared distances are perfect squares of positive integers, no three points are collinear (all orientation determinants nonzero), and no four points are concyclic (all 70 four-point incircle determinants nonzero). The live page https://www.erdosproblems.com/213 (and its forum thread) must still report 7 as the best construction, re-fetched live immediately before claiming.

## Partial wins

- **p1:** A 7-point integral set in general position with a smaller diameter than every 7-point example in the literature (Kreisel-Kurz 2008 and later work by Kurz and coauthors, located by literature search before claiming), with exact verification.
- **p2:** An 8-point integral set with no three collinear and at most one concyclic quadruple (strictly better than the forum's reported C+Q = 5 relaxation), verified exactly; labelled as a relaxation, not a solution.

## How a win is checked

Check squared distances are integer squares (isqrt), orientation determinants nonzero, and the 4x4 concyclicity determinants (x^2+y^2, x, y, 1) nonzero, all in exact integers after scaling sqrt(q) components. Instant.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/213>

## Sources

- <https://www.erdosproblems.com/213>
- <https://www.erdosproblems.com/forum/thread/213>
- <https://arxiv.org/abs/2407.08121>
- <https://arxiv.org/abs/2401.10821>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Follow Kreisel-Kurz: all points share a characteristic (squarefree q with coordinates in Z x sqrt(q) Z); enumerate Heronian triangles with a fixed characteristic and grow cliques of mutually integral points, pruning collinear and concyclic configurations; push the diameter bound and the set of characteristics further with modern hardware.
- Cross-domain import (database joins / clique search): the problem is a maximum-clique search in the 'integer distance' graph on candidate points; use bitset clique solvers (as in coding-theory record searches) with incremental candidate generation.
- Cross-domain import (elliptic curves): adding a point at integer distances to three fixed points is a rational point problem on a curve; use Mordell-Weil generators of the associated elliptic curves to produce candidates instead of brute force.
- Extend each known 7-point set: for each, search for an 8th point with integer distances to all 7 via the elliptic-curve parametrisation of points at integer distance from two fixed points.
- Search characteristic-mixed relaxations first (allow exactly one concyclic quadruple) to learn structure, as the forum post began.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Concyclic quadruples are easy to miss: all 70 four-point subsets must be checked with an exact determinant, not a floating-point circle fit.
- Collinear triples hidden by scaling: check orientation determinants exactly after clearing sqrt(q).
- Sets with almost all points on a line or circle (Anning-Erdos families) satisfy integrality but not general position.
- Floating-point distances that are 'almost integers' (1e-9 off) are not integer distances.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-213-integral-8-points-general-position.md
```

Already set up? Say `run V3R1T4S on erdos-213-integral-8-points-general-position`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-213-integral-8-points-general-position`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
