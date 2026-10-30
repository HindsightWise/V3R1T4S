# Shortest triorthogonal (transversal-T) codes [[n,1,d]] at d >= 7: beat the Jain-Albert table, e.g. distance 7 with fewer than 95 qubits

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (structured ILP/SAT searches over triorthogonal matrices with n in 55..94 at d = 7; exact distances for n <= ~200 are fast) · open as of 2026-10-30

## The problem

A triorthogonal matrix (Sergey Bravyi and Jeongwan Haah, PRA 86, 052329 (2012), arXiv:1209.2426) is a binary matrix G in which every pair and every triple of rows overlaps in an even number of positions, with k odd-weight rows. Its CSS code takes the even-weight rows as X stabilizers and G-perp as Z stabilizers. It encodes k qubits on which transversal T acts as logical T up to Clifford corrections. These codes underlie magic-state distillation. Weak triply even codes realise logical T with physical T gates alone. For k = 1, Shubham P. Jain and Victor V. Albert (arXiv:2408.12752, v3 24 March 2025; DOI 10.1109/JSAIT.2025.3570832) tabulated the shortest known codes for odd distances up to 31. Triorthogonal (their Table I): [[15,1,3]], [[49,1,5]] (Bravyi-Haah), [[95,1,7]], [[185,1,9]], [[279,1,11]], [[417,1,13]], [[575,1,15]], [[777,1,17]], [[983,1,19]], [[1317,1,21]], [[1651,1,23]], [[2033,1,25]], [[2415,1,27]], [[2813,1,29]], [[3211,1,31]]. Weak triply even (Table II): [[189,1,9]], [[283,1,11]], [[441,1,13]], [[599,1,15]], [[805,1,17]], [[1011,1,19]], [[1345,1,21]], [[1679,1,23]], [[2061,1,25]], [[2443,1,27]], [[2841,1,29]], [[3239,1,31]], with the same entries as Table I at d = 3, 5, 7. Both tables come from doubling (Bravyi and Cross, arXiv:1509.03239) of best-known self-dual or quadratic-residue codes. The two smallest cells are closed. Stergios Koutsioumpas, Darren Banfield and Alastair Kay (arXiv:2210.14066) proved that [[15,1,3]] is the smallest distance-3 code with a transversal non-Clifford gate. Sepehr Nezami and Jeongwan Haah (arXiv:2107.09684) classified all triorthogonal codes with n + k <= 38. Adam Wills, Shubham P. Jain and Shraddha Singh (arXiv:2609.30860, 25 Sep 2026) extended this to every generalised triorthogonal code with n <= 54 and Z-distance >= 3. For k = 1 their frontier first reaches Z-distance 4 at n = 48 and Z-distance 5 at n = 49, and has nothing of Z-distance 6 or more. So [[49,1,5]] is the shortest distance-5 triorthogonal code, and distance >= 6 needs n >= 55; no better lower bound is known. An ILP search by Alessio Baldelli, Olai A. Mostad, Hsuan-Yin Lin, Eirik Rosnes and Massimo Battaglioni (arXiv:2605.24519, v3 14 Oct 2026) recovered [[49,1,5]] and [[95,1,7]] and found longer distance-5 codes ([[85,1,5]], [[89,1,5]], [[93,1,5]]). Shiroman Prakash's census of triply even cyclic codes up to length 763 (arXiv:2610.08012, Oct 2026) gives nothing shorter at d >= 7 (for example [[127,1,7]] and [[223,1,9]]). No [[n,1,7]] triorthogonal code with n < 95 is known.

## What counts as a win

Success means an explicit binary matrix G (m x n) with exactly one odd-weight row such that an independent script verifies the following exactly over F_2. Every row pair and every row triple has even overlap (triorthogonality in the sense of Bravyi-Haah, arXiv:1209.2426). The even rows G_0 as X stabilizers and G-perp as Z stabilizers define an [[n,1]] CSS code. The full distance d = min(d_X, d_Z) is computed exactly, by full enumeration or by two independent exact algorithms. Here d_X is the minimum weight of the coset (odd row + span G_0) and d_Z the minimum weight of G_0-perp minus G-perp. n must be STRICTLY LESS (direction: min) than the Jain-Albert Table I entry for some odd d in 7..31: 95, 185, 279, 417, 575, 777, 983, 1317, 1651, 2033, 2415, 2813 and 3211 for d = 7, 9, ..., 31, as re-read from the latest version of arXiv:2408.12752 immediately before claiming. An arXiv search re-run at claim time must find no shorter [[n,1,d]] triorthogonal code. Distances 3 and 5 are closed and do not count.

## Partial wins

- **p1:** A weak triply even [[n,1,d]] code (logical T from transversal T with no Clifford correction, as defined in Sec. I-C of arXiv:2408.12752), verified exactly, with n strictly below the Table II entry for some odd d in 9..31 (189, 283, 441, 599, 805, 1011, 1345, 1679, 2061, 2443, 2841, 3239).
- **p2:** A k = 1 triorthogonal matrix with Z-distance d_Z >= 7 (the quantity that sets the distillation order) on at most 94 columns, even if d_X < 7. This would beat the T-count of the 95-to-1 distance-7 distillation protocol. It must also beat any published single-output distance-7 protocol found by an arXiv search at claim time.
- **p3:** An exhaustive, re-runnable certificate extending arXiv:2609.30860 for k = 1: no triorthogonal code with d_Z >= 6 exists for any n with 55 <= n <= n0, for some n0 >= 55. This raises the lower bound for distance 6 and above to n0 + 1.

## How a win is checked

Check triorthogonality with integer dot products mod 2; with about 30 rows, the C(m,3) checks are instant. Build H_X = G_0 and a basis of G-perp for H_Z by Gaussian elimination, and confirm k = n - rank H_X - rank H_Z = 1. Compute d_X by enumerating the coset (2^(m-1) words) and d_Z by Brouwer-Zimmermann or an exact MIP on G_0-perp minus G-perp; for n <= 100 each takes seconds to hours. Cross-check d with a second implementation, for example the open-source distance package of arXiv:2603.22532. For p1, also verify the weak triply even condition exactly as stated in Sec. I-C of arXiv:2408.12752. Then check by stabilizer simulation that transversal T maps the code space to itself and acts as logical T or T-dagger. For p3, reproduce the k = 1 part of the n <= 54 frontier of arXiv:2609.30860 with the claimant's code as a control, and re-run the extension with a second implementation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2408.12752>

## Sources

- <https://arxiv.org/abs/2408.12752>
- <https://arxiv.org/abs/1209.2426>
- <https://arxiv.org/abs/2609.30860>
- <https://arxiv.org/abs/2107.09684>
- <https://arxiv.org/abs/2210.14066>
- <https://arxiv.org/abs/2605.24519>
- <https://arxiv.org/abs/2610.08012>
- <https://errorcorrectionzoo.org/c/stab_49_1_5>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Doubling as used by Jain and Albert combines a self-dual CSS code of distance d with a triorthogonal code of distance d - 2. At d = 7 that needs a distance-7 self-dual CSS code and a distance-5 triorthogonal code. The first is the [[23,1,7]] Golay code: no self-dual binary code shorter than 24 has distance 8. The second is now known to need 49 qubits. So doubling cannot go below 2*23 + 49 = 95, and beating 95 needs a different construction.
- ILP with prescribed automorphism groups (Baldelli et al.) recovered the records. Target n in 55..94 at d = 7 with groups such as dihedral groups, AGL(1,p), or PSL(2,q) acting on q+1 points.
- Reuse the Wills-Jain-Singh pipeline (unital triorthogonal spaces correspond to RM(m-4, m) codewords, then logical rows are added) restricted to k = 1 and Z-distance >= 6. The restriction may be far cheaper than their 10^8 core-hour estimate for a full length-56 classification.
- For a fixed row count, the XOR-SAT formulation over column-type multiplicities applies (see the distillation-footprint target). Add 'no <= d-1 columns sum to a logical' clauses for the Z-distance, then run an exact d_X check.
- At larger d the table is a doubling ladder built on best-known self-dual codes. A shorter self-dual input or a direct construction (quadratic-residue, Reed-Muller-like or cyclic triply even codes) can beat a high-d entry; the cyclic census of arXiv:2610.08012 does not yet.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Distance conventions differ: distillation papers use only the Z-distance, while this table uses the full distance min(d_X, d_Z). Report both.
- Triorthogonal codes (T up to Clifford corrections) and weak triply even codes (T exactly) are separate columns of the Jain-Albert tables; compare each claim with the right one.
- Distances 3 and 5 are closed. [[15,1,3]] is optimal (arXiv:2210.14066). The n <= 54 classification of arXiv:2609.30860 shows that Z-distance 5 needs 49 qubits, so [[49,1,5]] is optimal too. Claims there are not wins.
- Non-stabilizer codes, such as the ((27,2,5)) binary dihedral permutation-invariant code mentioned by the Error Correction Zoo, realise transversal T with fewer qubits but do not count.
- Codes whose non-Clifford logical gate is a depth-one layer of multi-qubit gates, such as the [[37,1,7]] and [[59,1,9]] codes of arXiv:2610.06730, are not triorthogonal and do not count.
- The distillation-footprint target minimises rows N, not length n. A small-N protocol is not a short code.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/triorthogonal-codes-shortest-k1.md
```

Already set up? Say `run V3R1T4S on triorthogonal-codes-shortest-k1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `triorthogonal-codes-shortest-k1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
