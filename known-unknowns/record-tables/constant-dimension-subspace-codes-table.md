# Constant dimension subspace codes A_q(n,d;k): beat a best known lower bound in the Bayreuth subspace code tables (q = 2..9, n <= 19)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (structured constructions or ILP with prescribed automorphisms; binary small n may need laptop-days) · open as of 2026-10-30

## The problem

A_q(n,d;k) is the largest number of k-dimensional subspaces of F_q^n with pairwise subspace distance d_S(U,W) = 2k - 2 dim(U cap W) >= d. Heinlein, Kiermaier, Kurz and Wassermann maintain online tables of lower and upper bounds (subspacecodes.uni-bayreuth.de, manual arXiv 1601.02864) for 2 <= q <= 9 and n <= 19. The field is very active: Li and Fu (arXiv 2502.12518, 63 new lower bounds; arXiv 2507.07842), Wang, Yao and Fu (arXiv 2508.01258, at least 65), Wang, Gao, Mesnager and Fu (arXiv 2508.03196), Xu and Li (arXiv 2510.27071, A_q(n,8;6) for 16 <= n <= 19) and Fu, Gao, Mesnager and Wang (arXiv 2609.24239, 2026) improved many cells in 2025-2026 via inserting, multilevel and parallel linkage constructions and new optimal Ferrers diagram rank-metric codes. Kurz's survey (arXiv 2112.11766, v3 2025-12-20, Sections 5 and 7) gives the best known small binary values: A_2(8,4;3) >= 1331 (Zhou, Chen, Zhang, Shi and He 2021; 1326 earlier by prescribed automorphisms), A_2(8,4;4) >= 4802 (Zhou et al., extending the 4801 code of Braun, Ostergard and Wassermann; anticode bound 6477), A_2(9,4;3) >= 5986 (Braun, Ostergard, Wassermann), A_2(9,4;4) >= 37265 and A_2(10,6;4) >= 4173; for q = 3, 754 <= A_3(6,4;3) <= 784 (formula (7.1) and Theorem 8.4). The cell A_2(7,4;3) = A_2(7,4;4) is a separate bank entry (binary-q-fano-plane-s2-2-3-7) and partial spread cells (d = 2k) belong to partial-spreads-smallest-open-cases; both are excluded here.

## What counts as a win

An explicit set of M k-dimensional subspaces of F_q^n (each given by a k x n generator matrix of rank k over F_q; q a prime power <= 9, n <= 19, d < 2k, and (q,n,d,k) neither (2,7,4,3) nor (2,7,4,4)) whose pairwise intersections all have dimension <= k - d/2, with M STRICTLY GREATER (direction: max) than the larger of: the lower bound shown for that cell (equivalently its dual cell k -> n-k) on subspacecodes.uni-bayreuth.de at verification time (if the live site is unreachable, the newest web.archive.org snapshot of that cell's table page, with its date recorded in the claim), and every value for that cell in arXiv 2112.11766, 2502.12518, 2507.07842, 2508.01258, 2508.03196, 2510.27071, 2609.24239 or any newer paper. M must not exceed the tabulated upper bound (that would mean a bug).

## Partial wins

- **p1:** An improvement in one of the named small cells, which are the most studied: A_2(8,4;3) >= 1332, A_2(8,4;4) >= 4803, A_2(9,4;3) >= 5987 or A_3(6,4;3) >= 755, in each case also strictly above any newer value for that cell, checked as in the full criterion.
- **p2:** An exact rational certificate (LP or SDP dual, verified in rational arithmetic) proving A_q(n,d;k) <= U with U strictly below the tabulated upper bound for some cell in the scope of the full criterion.

## How a win is checked

Bring each generator matrix to reduced row echelon form over F_q (q prime: integers mod q; q = 4, 8, 9: an explicit field table), assert rank k and distinctness, and for every pair compute dim(U cap W) = 2k - rank([U;W]) <= k - d/2. Use bitsets for q = 2; check all pairs, no sampling. Re-read the Bayreuth cell and the cited papers' tables on the day.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2112.11766>

## Sources

- <http://subspacecodes.uni-bayreuth.de/>
- <https://arxiv.org/abs/1601.02864>
- <https://arxiv.org/abs/2112.11766>
- <https://arxiv.org/abs/2502.12518>
- <https://arxiv.org/abs/2508.01258>
- <https://arxiv.org/abs/2507.07842>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Combine the 2025 inserting/multilevel/parallel-linkage constructions with better small ingredient codes (FDRM codes from ILP) in cells those papers did not touch.
- For binary small n, prescribe automorphism groups (Singer subgroups and normalizers) and solve the reduced ILP (Braun-Ostergard-Wassermann method).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Bayreuth site (and all of mathe2.uni-bayreuth.de) was unreachable on 2026-10-30, so the status_source is the survey. Wayback snapshots (2025-2026) of the table pages still work, but they lag the literature: the 2025-10-06 snapshot still shows 1326 and 4801 for A_2(8,4;3) and A_2(8,4;4), and the 2025-2026 arXiv papers may exceed any snapshot.
- The survey quotes two values for A_2(8,4;3): 1326 (Section 7, prescribed automorphisms) and 1331 (Section 5, Zhou et al. 2021); 2025 papers still use the 1326 code as an ingredient. The record to beat is 1331.
- A_q(n,d;k) = A_q(n,d;n-k): check the dual cell too.
- Many 2025 papers state sizes as formulas in q; evaluate them for the exact q before comparing.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/constant-dimension-subspace-codes-table.md
```

Already set up? Say `run V3R1T4S on constant-dimension-subspace-codes-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `constant-dimension-subspace-codes-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
