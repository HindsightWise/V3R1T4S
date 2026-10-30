# Equidistant subspace codes: more than 40 four-dimensional subspaces of F_2^8 pairwise meeting in exactly a point (B_2(8,1;4))

📊 **Record tables** · standard · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

B_q(n,t;k) is the maximum number of k-subspaces of F_q^n whose pairwise intersections all have dimension exactly t (t-intersecting equidistant codes). Sunflowers (all pairs meeting in the same t-space) give at most A_2(7,6;3) = 17 for (q,n,t,k) = (2,8,1,4), and by Etzion and Raviv (Discrete Appl. Math.) any such code with at least 211 members is a sunflower, so B_2(8,1;4) <= 210. Bartoli and Pavese proved B_2(6,1;3) = 20. Kurz's survey (arXiv 2112.11766, latest version 2025-12-20, Section 9.1) lifts Boston's 5-dimensional binary 4x4 equidistant rank-metric code (rank distance 3) to get B_2(8,1;4) >= 32, adds 8 more codewords by computer to get B_2(8,1;4) >= 40, and poses determining B_2(8,1;4) as a research problem. Similarly B_2(10,1;5) >= 64 from a 6-dimensional 5x5 code.

## What counts as a win

An explicit set of M >= 41 four-dimensional subspaces of F_2^8 (each a 4x8 binary generator matrix of rank 4) such that every pair intersects in a subspace of dimension exactly 1, with M STRICTLY GREATER (direction: max) than 40, the value in arXiv 2112.11766 Section 9.1 (and greater than any newer published value).

## Partial wins

- **p1:** An explicit set of at least 65 five-dimensional subspaces of F_2^10 pairwise intersecting in exactly a 1-dimensional subspace, beating the B_2(10,1;5) >= 64 noted in arXiv 2112.11766.
- **p2:** An exact upper bound certificate proving B_2(8,1;4) <= U for some U < 210, checkable by an independent program (e.g. an exhaustive search over a stated symmetry-reduced case split with a DRAT/VIPR certificate).

## How a win is checked

For every pair compute dim(U cap W) = 8 - rank([U;W]) over F_2 and assert it equals 1; assert all matrices have rank 4 and the subspaces are distinct (compare RREFs). The check is a few thousand rank computations.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2112.11766>

## Sources

- <https://arxiv.org/abs/2112.11766>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from lifted linear 4x4 equidistant rank-metric codes (several inequivalent ones exist) and extend with max-clique search on the compatibility graph of the 200787 solids.
- Drop the lifting structure: search for G-invariant codes under subgroups of GL(8,2).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Exactly one dimension: pairs meeting trivially are not allowed (that would be distance 8).
- The survey says these lifted bounds had not appeared elsewhere; check Boston's paper and newer arXiv work for larger codes before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/equidistant-subspace-codes-b2-8-1-4.md
```

Already set up? Say `run V3R1T4S on equidistant-subspace-codes-b2-8-1-4`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `equidistant-subspace-codes-b2-8-1-4`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
