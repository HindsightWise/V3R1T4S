# QAPLIB: a permutation beating the best known value of one of the 28 unsolved instances (tai a/b, tai256c, sko, tho, wil)

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (n = 35..256; evaluating a permutation is O(n^2), a swap delta O(n)) · open as of 2026-10-30

## The problem

QAPLIB (R. E. Burkard, E. Çela, S. E. Karisch and F. Rendl; maintained by Peter Hahn and Miguel Anjos; COR@L mirror at Lehigh, whose solution table was last updated on 20 April 2012; Edinburgh DataShare copy doi:10.7488/ds/3428 from 2022) is the standard quadratic assignment library. Hans Mittelmann's page 'Improved QAPLIB lower bounds using BBCPOP and NewtBracket' (dated 2026/8/26, unchanged on 2026-10-29) lists the 28 instances still unsolved: Tai35a, Tai40a, Tai50a, Tai60a, Tai80a, Tai100a, Tai50b, Tai60b, Tai80b, Tai100b, Tai150b, Tai256c, Sko49, Sko56, Sko64, Sko72, Sko81, Sko90, Sko100a-f, Tho40, Tho150, Wil50 and Wil100. These are the open instances of QAPLIB's 2012 table minus four solved since. Fujii, Ito, Kim, Kojima, Shinano and Toh solved Tai30a and Sko42 (arXiv:2101.09629). Gonçalves, Pessoa, Bentes, Farias and Drummond solved Tai35b and Tai40b (RLT2 branch-and-bound on GPUs, INFORMS J. Comput. 29(4), 2017). The best known values are QAPLIB's, from Taillard's robust tabu search, Misevičius's iterated tabu search and simulated annealing, Stützle's ant system and genetic hybrids. The exception is Tai100a. V. P. Shylo lowered QAPLIB's 21,052,466 to 21,044,752 (2017), and Misevičius lowered it to 21,043,560 (Memetic Computing 11:331-332, 2019). Sergienko, V. P. Shylo, Roshchyn, P. V. Shylo, Boyarchuk and Moroz then reached 21,040,996 with a portfolio of 16 repeated iterated tabu searches (Cybernetics and Computer Technologies 2024 no. 3, doi:10.34229/2707-451X.24.3.3). Their paper prints the permutation, which evaluates to 21,040,996. Lower bounds come from Mittelmann's BBCPOP and Newton-bracketing runs. For Tai256c, QUADI (Travor Baylis) gives 44,445,735, and Fujii, Kim, Kojima, Mittelmann and Shinano give a symmetry-based reformulation and branch-and-bound (arXiv:2401.09439). Find a permutation with an objective strictly below the best known value of one of the 28.

## What counts as a win

A permutation p of 1..n for one of the 28 instances, evaluated by a standalone checker as sum_{i,j} a_ij * b_{p(i),p(j)} on the QAPLIB .dat file (n, then matrix A, then matrix B). The file comes from https://coral.ise.lehigh.edu/data-sets/qaplib/qaplib-problem-instances-and-solutions/ or the DataShare qapdata.tar.gz. Its value must be strictly below the best known value: Tai35a 2422002, Tai40a 3139370, Tai50a 4938796, Tai60a 7205962, Tai80a 13499184, Tai100a 21040996, Tai50b 458821517, Tai60b 608215054, Tai80b 818415043, Tai100b 1185996137, Tai150b 498896643, Tai256c 44759294, Sko49 23386, Sko56 34458, Sko64 48498, Sko72 66256, Sko81 90998, Sko90 115534, Sko100a 152002, Sko100b 153890, Sko100c 147862, Sko100d 149576, Sko100e 149150, Sko100f 149036, Tho40 240516, Tho150 8133398, Wil50 48816, Wil100 273038. It must also be below any value on https://plato.asu.edu/ftp/qaplib_bounds.html and any value found in a literature search at claim time. The checker must first reproduce QAPLIB's posted .sln values: tai100a 21052466, sko100a 152002, tai256c 44759294 and wil50 48816 directly, and tai60a 7205962 and tho150 8133398 only with the inverse permutation (see pitfalls). It must also reproduce the Tai100a record 21040996 from the permutation printed in Sergienko et al. 2024. The permutation with its convention, the checker, the .dat sha256 and the page snapshots are saved together. Nothing is sent to the maintainers by the agent; the write-up goes to the human.

## Partial wins

- **qap-certified-lower-bound:** A lower bound for any of the 28 strictly above the 'new bound' column of Mittelmann's page (for Tai256c, above the QUADI row's 44,445,735) and above any bound found in a literature search at claim time. It needs a certificate that an independent program verifies in exact (rational or integer) arithmetic. Examples: a Gilmore-Lawler or Lagrangian bound with explicit dual multipliers, or a dual-feasible solution of a DNN/SDP relaxation rounded to rationals with a rigorous error bound. A solver log alone does not count.

## How a win is checked

Download the .dat and .sln files from the COR@L QAPLIB page, or qapdata.tar.gz and qapsoln.tar.gz from doi:10.7488/ds/3428. Evaluate in exact integer arithmetic; the values fit in 64 bits. Verified 2026-10-29: the tai100a, sko100a, tai256c and wil50 .sln files reproduce under sum a_ij b_p(i)p(j), while tai60a and tho150 reproduce only after inverting the permutation. The Tai100a permutation printed in Sergienko et al. 2024 gives 21,040,996 on tai100a.dat (sha256 de053a8df4044c71d3d3da8b86a6e3bf32b1ac3053ab1970e6d81098a26a0895). Milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://plato.asu.edu/ftp/qaplib_bounds.html>

## Sources

- <https://plato.asu.edu/ftp/qaplib_bounds.html>
- <https://coral.ise.lehigh.edu/data-sets/qaplib/qaplib-problem-instances-and-solutions/>
- <https://coral.ise.lehigh.edu/data-sets/qaplib/qaplib-whats-new/>
- <https://doi.org/10.7488/ds/3428>
- <https://doi.org/10.34229/2707-451X.24.3.3>
- <https://cctech.org.ua/images/docs/Articles/2024/paper_24_3_3.pdf>
- <https://doi.org/10.1007/s12293-019-00289-y>
- <https://doi.org/10.3390/e23010108>
- <https://doi.org/10.3390/math12233726>
- <https://arxiv.org/abs/2101.09629>
- <https://arxiv.org/abs/2401.09439>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The record-holding methods are robust tabu search (Taillard 1991), Misevičius's iterated and hierarchical tabu search with genetic hybrids, and the Shylo group's repeated iterated tabu search (RITSK/RITSR). A portfolio of 16 of those runs (425 attempts of 2 hours each) set the 2024 Tai100a record. Misevičius and Verenė's hybrid genetic-hierarchical algorithm never reached the Tai80a and Tai100a records (Entropy 23:108, 2021), so long parallel runs on 10 cores have the best odds there.
- Tai256c is a grey-density instance. Fujii et al. show it reduces to a 256-variable binary quadratic problem with a single cardinality constraint (sum = 92) and a large symmetry group, so search that smaller space with symmetry breaking rather than permutations.
- Physics import: QAP on Euclidean or Manhattan layouts (sko, tho, wil) behaves like a disordered spin system, and replica-exchange Monte Carlo over permutations with swap moves is a natural fit.
- Keep Taillard's full swap-delta matrix with O(1) updates after each accepted swap, so a laptop evaluates hundreds of millions of moves per hour.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- QAPLIB's 2012 tables still list Tai30a, Tai35b, Tai40b and Sko42 as unsolved, although they are solved. Use Mittelmann's list for the open set. For Tai100a, QAPLIB and Mittelmann both show the stale 21052466, and recent papers (for example Misevičius and Verenė, Entropy 2021) quote Misevičius's 2019 value 21043560. The record is 21040996 (Sergienko et al. 2024).
- Mittelmann's upper bound for Tai60a reads 7505962, a typo for QAPLIB's 7205962. Compare against 7205962.
- Permutation convention: QAPLIB's own tai60a.sln and tho150.sln reproduce their values only as sum a_{p(i)p(j)} b_ij, i.e. with the inverse permutation. State the convention, and evaluate both p and its inverse under sum a_ij b_{p(i)p(j)}.
- QPLIB's QAP-structured instances (QPLIB_2492, 2512, 2733, 2880, 2957, 3307, 3347, 3361, 3402, 3413 and 3703, all with n <= 32) are not among these 28; improvements there belong to the separate QPLIB target.
- Many 'b' and Sko records are reached in every run of recent heuristics, which suggests they may be optimal. Strict improvements are most plausible on Tai80a, Tai100a, Tho150 and Tai256c.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/qaplib-open-instances-bkv.md
```

Already set up? Say `run V3R1T4S on qaplib-open-instances-bkv`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `qaplib-open-instances-bkv`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
