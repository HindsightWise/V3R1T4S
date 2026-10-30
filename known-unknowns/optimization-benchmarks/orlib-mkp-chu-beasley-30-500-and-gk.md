# 0-1 multidimensional knapsack: beat a best known value on an OR-Library 30.500 (Chu-Beasley) or MK_GK (Glover-Kochenberger) instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (a 500 x 30 instance file is about 70 KB; record runs used 2 h per seed with a MIP solver inside an evolutionary loop) · open as of 2026-10-30

## The problem

The 0-1 multidimensional knapsack problem (MKP): pick a subset of n items maximising total profit subject to m capacity constraints. The standard benchmark is Chu and Beasley's OR-Library set (J. Heuristics 4, 1998; files mknapcb1..9, 270 instances). Xu, Li and Yin (FEPSS; arXiv 2210.03918v3, May 2024; Applied Soft Computing 164, 111934, 2024) report that the small classes are proven optimal but (250,30), (500,10) and (500,30) are still open. The hardest class, mknapcb9 = 30.500 (n=500, m=30; instances 500-30-0..29 in file order, tightness 0.25/0.50/0.75 in blocks of ten), carries best known values built up by Vasquez and Vimont, Boussier et al., Mansini and Speranza (CORAL), Lai, Hao, Glover and Lu (TPTEA, 2018) and FEPSS, which raised 500-30-3, -4, -11 and -18. The best published values (maximum of the BK column and every fbest column in Tables 2 and 5 of arXiv 2210.03918v3) for 500-30-0..29 are: 116056 114810 116741 115370 116553 115741 114181 114403 115419 117116 | 218104 214660 215978 217910 215689 215919 215907 216542 217364 214739 | 301675 300055 305087 302032 304462 297012 303364 307007 303199 300596. The 11 MK_GK instances (n up to 2500, m up to 100; hosted by Jin-Kao Hao's group) have best published values gk01..gk11: 3766 3958 5656 5767 7561 7680 19221 18808 58091 57296 95239 (FEPSS raised gk07-gk11). No 30.500 instance is reported proven optimal.

## What counts as a win

A 0/1 vector x of length 500 for one instance 500-30-j (the j-th of the 30 problems in https://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/mknapcb9.txt, counting from 0 in file order) that satisfies every one of the 30 constraints sum_i r(k,i) x_i <= b(k) in exact integer arithmetic and whose profit sum_i p(i) x_i is strictly greater than the value listed for 500-30-j in this entry's statement, and also strictly greater than every value for that instance in any 2024-2026 paper or preprint found in a literature check made at claim time (the check and what it found are written down). Feasibility and profit are recomputed by an independent checker from the downloaded file, whose sha256 is recorded. Nothing is submitted anywhere; the write-up goes to the human.

## Partial wins

- **p1:** The same for one MK_GK instance gk01..gk11 from https://leria-info.univ-angers.fr/~jinkao.hao/mkp/MK_GK_Instances.zip: a feasible 0/1 vector (exact integer check) whose profit is strictly greater than the gk value listed in the statement and than any 2024-2026 published value found in the claim-time literature check.
- **p2:** A proof that the listed value of some 500-30-j is optimal, as a VIPR certificate produced by exact SCIP on an MPS model regenerated from mknapcb9.txt and accepted by viprchk, together with a feasible vector attaining the listed value.

## How a win is checked

Download mknapcb9.txt and parse it (first token K=30; then per problem: n m opt, n profits, m rows of n weights, m capacities; a parser written during vetting consumed the file exactly and found 30 problems of n=500, m=30). Read the claimed vector, check every constraint and recompute the profit with integer arithmetic, compare with the statement's value and with the claim-time literature check. Seconds. FEPSS posts code (github.com/jetou/FEPSS) but no solution vectors, so there is no posted vector to reproduce; the checker is validated on the OR-Library file format instead.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2210.03918>

## Sources

- <https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html>
- <https://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/mknapcb9.txt>
- <https://arxiv.org/abs/2210.03918>
- <https://doi.org/10.1016/j.asoc.2024.111934>
- <https://leria-info.univ-angers.fr/~jinkao.hao/mkp.html>
- <https://github.com/jetou/FEPSS>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fix the cardinality sum x_i = K for each plausible K and run a reduced-cost-guided tabu or LNS per K (the Vasquez-Vimont idea), solving freed sub-problems exactly with CP-SAT or HiGHS.
- Core-problem approach: fix items with extreme LP reduced costs and solve the core exactly with long time limits; target the tightness-0.25 block (500-30-0..9), where FEPSS and TPTEA disagree most.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The BK column of FEPSS Table 5 is not the latest value for four instances: Table 2 (the time-limit study) reports 116553 for 500-30-4 and 214660 for 500-30-11, above Table 5. Use the statement's maxima.
- The OR-Library mkcbres file holds 1998 GA values, far below the current records; do not compare against it.
- Instance numbering: 500-30-j is the j-th problem in file order (0-based); the file header 'opt' field is 0 (unknown) and carries no information.
- MK_GK files use a different layout from the OR-Library files; check the parser against the n and m printed in FEPSS Table 6.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/orlib-mkp-chu-beasley-30-500-and-gk.md
```

Already set up? Say `run V3R1T4S on orlib-mkp-chu-beasley-30-500-and-gk`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `orlib-mkp-chu-beasley-30-500-and-gk`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
