# Erdős #217 (crescent configurations): 9 points in general position whose 8 distances occur 1, 2, ..., 8 times

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact integer lattice searches; off-lattice needs algebraic-number optimisation) · open as of 2026-10-30

## The problem

For which n are there n points in the plane, no three on a line and no four on a circle, determining exactly n-1 distinct distances such that (in some order) the i-th distance occurs exactly i times? Burt, Goldstein, Manski, Miller, Palsson and Suh (arXiv:1509.07220) call these crescent configurations. Known: n=4 (isosceles triangle plus centre), n=5 (Pomerance), n=6 with no equilateral triangle (Palásti 1989), n=7 (Palásti 1987), n=8 (Palásti 1989b). Erdős believed they cannot exist for large n. No n=9 example is known. Burt et al. exhaustively searched a 91-point hexagonal patch of the triangular lattice (none). Forum, sallerk (2026-08-31): exact search shows no 9-point crescent configuration on the triangular lattice with squared diameter <= 400 (1,459 lattice points, ~3.1e12 nodes), and the same code recovers Palásti's n=8 example. Forum, IheartTesla (2026-09-04): relaxing general position, a 9-point triangular-lattice set with multiplicities 1..8 and only C+Q = 3 defects (1 collinear triple, 2 concyclic quadruples); best for n=10 was (C,Q) = (2,2). Status on erdosproblems.com and the teorth database: open.

## What counts as a win

CONFIRMED: exact coordinates (integers, rationals, or elements of an explicitly given number field with exact arithmetic) for 9 points in R^2 such that (i) no three are collinear and no four are concyclic, checked with exact 3x3 and 4x4 determinants; (ii) the squared pairwise distances take exactly 8 distinct values; (iii) the multiset of their multiplicities is exactly {1,2,...,8} (any order of distances is allowed, as in Palásti's n=8 example). The same with n >= 10 points and multiplicities {1,...,n-1} also counts. Alternatively a machine-checked proof that no 9-point crescent configuration exists in the plane.

## Partial wins

- **p1:** A 9-point planar set with exact coordinates whose distances have multiplicities exactly {1,...,8} and whose number of collinear triples plus concyclic quadruples (counted as in IheartTesla's 2026-09-04 forum comment) is at most 2, strictly below the best value posted on the #217 thread at verification time (3 on 2026-10-30).
- **p2:** A 10-point planar set with exact coordinates, multiplicities exactly {1,...,9}, and C+Q at most 3, strictly below the best value posted at verification time (4, i.e. (2,2), on 2026-10-30).
- **p3:** A reproducible exhaustive exact search proving that no 9-point crescent configuration lies on the triangular lattice with squared diameter up to at least 800, double the forum's 400, with code that also recovers the known n=4..8 configurations.

## How a win is checked

Recompute all C(9,2)=36 squared distances exactly, tally multiplicities, and test every triple (collinearity determinant) and every quadruple (concyclicity determinant, 126 quadruples) in exact arithmetic with an independent script. For p3, rerun the search at a verifier-chosen rung and check the positive controls (Palásti's n=8 set scaled by sqrt 7 at squared diameter 21).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/217>

## Sources

- <https://www.erdosproblems.com/217>
- <https://www.erdosproblems.com/forum/thread/217>
- <https://arxiv.org/abs/1509.07220>
- <https://github.com/sallerk/erdos-notes/tree/main/p217>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Off-lattice: fix a combinatorial pattern of which pairs share a distance (from the n=8 Palásti set plus one point) and solve the polynomial system with Gröbner bases or certified Newton, then check genericity exactly.
- Other lattices (Z^2, Z[sqrt(-d)]) are not covered by the forum search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 'In some ordering' matters: Palásti's own n=8 set has multiplicities 1,4,5,6,7,2,3 by increasing distance, so do not require monotone multiplicities.
- Floating-point concyclicity tests give false negatives; use exact determinants.
- The triangular lattice up to squared diameter 400 is already excluded (sallerk).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-217-crescent-configuration-n9.md
```

Already set up? Say `run V3R1T4S on erdos-217-crescent-configuration-n9`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-217-crescent-configuration-n9`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
