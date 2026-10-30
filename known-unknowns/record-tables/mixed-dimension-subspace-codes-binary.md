# Mixed dimension binary subspace codes A_2(n,d), n = 6..8: improve a bound in Kurz's Table 8.1 (A_2(6,3) 108-117, A_2(7,3) 614-776, A_2(8,5) 263-326, ...)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (max independent set on 2825 / 29212 / 417199 subspaces) · open as of 2026-10-30

## The problem

A_2(n,d) is the largest set of subspaces of F_2^n of any dimensions with pairwise subspace distance d_S(U,W) = dim U + dim W - 2 dim(U cap W) >= d. Honold, Kiermaier and Kurz (Adv. Math. Commun. 2016), Heinlein and Kurz (Adv. Math. Commun. 2018) and Heinlein and Ihringer (SDP bounds, 2020) set the current state, summarized in Table 8.1 of Kurz's survey (arXiv 2112.11766, latest version 2025-12-20), which poses improving it as a research problem. Open cells: 108 <= A_2(6,3) <= 117, 614 <= A_2(7,3) <= 776, 334 <= A_2(7,4) <= 388, 5687 <= A_2(8,3) <= 9191, 4803 <= A_2(8,4) <= 6479, 263 <= A_2(8,5) <= 326. All other cells with n <= 8 are determined (e.g. A_2(6,4) = 77, A_2(7,5) = 34, A_2(8,6) = 257).

## What counts as a win

Either (a) an explicit set of M subspaces of F_2^n (n in {6,7,8}; each subspace as a binary generator matrix of full row rank, dimensions 0..n allowed) with pairwise subspace distance >= d and M STRICTLY GREATER (direction: max) than the lower bound for (n,d) in Table 8.1 of arXiv 2112.11766 and any newer published value; or (b) a verifiable proof that A_2(n,d) <= U with U strictly below the Table 8.1 upper bound: an exact rational LP/SDP dual certificate or a VIPR-format ILP certificate checked by an independent checker.

## Partial wins

- **p1:** Raise the smallest open lower bound: a mixed dimension code in F_2^6 with 109 or more subspaces and minimum subspace distance >= 3.
- **p2:** Raise A_2(8,5) above 263 or A_2(7,3) above 614 with an explicit code.

## How a win is checked

Reduce each generator matrix to RREF over F_2, assert distinctness, and for every pair compute d_S = rank(U) + rank(W) - 2(rank(U)+rank(W)-rank([U;W])) >= d. For upper bounds, re-check the dual certificate in exact rational arithmetic or run an independent VIPR checker. Re-read the survey and search for newer values before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2112.11766>

## Sources

- <https://arxiv.org/abs/2112.11766>
- <https://arxiv.org/abs/1512.06660>
- <https://arxiv.org/abs/1808.03580>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Model as maximum independent set on the conflict graph of all subspaces (2825 vertices for n=6) and run modern MIS solvers (KaMIS, ARW-ILS) with symmetry (Singer cycle) restrictions.
- For A_2(7,4) and A_2(8,4), note that the lower bounds come from constant dimension codes plus extra codewords; mix dimensions k and k+1 explicitly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A_2(7,4) >= 334 comes from the 333-plane code; an improvement there likely needs a better A_2(7,4;3) code (separate bank entry), so it is the hardest cell.
- Table 8.1 uses the subspace distance, not the injection distance.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mixed-dimension-subspace-codes-binary.md
```

Already set up? Say `run V3R1T4S on mixed-dimension-subspace-codes-binary`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mixed-dimension-subspace-codes-binary`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
