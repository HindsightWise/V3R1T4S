# Full flag codes over F_2: beat A^f_2(5,2) >= 3120 (upper bound 3255) or A^f_2(6,6) >= 224

📊 **Record tables** · standard · tractability ★★★★☆ · compute: laptop-hours (max independent set on 9765 vertices) · open as of 2026-10-30

## The problem

A full flag in F_q^n is a chain V_1 < V_2 < ... < V_(n-1) with dim V_i = i; the Grassmann distance of two full flags is the sum over i of dim V_i - dim(V_i cap V'_i). A^f_q(n,d) is the largest set of full flags with pairwise Grassmann distance >= d. Kurz (Bounds for flag codes, Des. Codes Cryptogr. 2021, arXiv 2005.04768) determined A^f_2(n,d) for all n <= 5 except 3120 <= A^f_2(5,2) <= 3255 (lower bound by ILP with a prescribed cyclic group of order 15; the CPLEX run was stopped with the group-restricted bound at 3178) and gave 224 <= A^f_2(6,6) <= 567 and upper bounds for n = 6, 7. Kurz's survey (arXiv 2112.11766, latest version 2025-12-20, Section 9.2, Table 9.1) still lists 3120-3255 and asks for improved bounds.

## What counts as a win

An explicit set of M full flags of F_2^5 (each given by an ordered basis b1..b4 with V_i = span(b1..bi)) with pairwise Grassmann distance >= 2 and M >= 3121 (direction: max, strictly above 3120 in Table 9.1 of arXiv 2112.11766 and any newer published value).

## Partial wins

- **p1:** A set of at least 225 full flags of F_2^6 with pairwise Grassmann distance >= 6, beating A^f_2(6,6) >= 224 in arXiv 2005.04768 (and any newer published value).
- **p2:** A proof that A^f_2(5,2) <= U for some U <= 3254, given as a VIPR-format ILP certificate or exact LP/SDP certificate verified by an independent checker.

## How a win is checked

Two full flags of F_2^5 are at Grassmann distance 1 exactly when they differ in one position only; so for distance >= 2 check, for each of the 4 positions, that no two flags agree in the other 3 subspaces (bucket flags by the 4 partial flags obtained by deleting one subspace). Assert each basis is independent and flags are distinct. For n = 6, compute all pairwise Grassmann distances directly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2112.11766>

## Sources

- <https://arxiv.org/abs/2005.04768>
- <https://arxiv.org/abs/2112.11766>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The conflict graph has 9765 vertices and 13020 triangles-as-cliques (each partial flag missing one subspace has 3 completions); run KaMIS or ILS-based MIS solvers, then re-optimize with the order-15 group or groups listed in arXiv 2005.04768 as still promising.
- Finish Kurz's aborted ILP: with G of order 15 the bound was 3178 after 9 hours.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The paper has a typo 3225 in two sentences (Example 3.14 discussion and its summary '3120 <= A^f_2(5,2) <= 3225'); Table 5, Proposition 6.1 and survey Table 9.1 give the upper bound 3255 = 9765/3.
- Grassmann distance uses injection distance (half the subspace distance).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/full-flag-codes-binary-a2f-5-2.md
```

Already set up? Say `run V3R1T4S on full-flag-codes-binary-a2f-5-2`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `full-flag-codes-binary-a2f-5-2`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
