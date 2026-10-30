# Largest k-AP-free subsets of [1..n] for k = 4, 5, 6: the next exact terms of A003003 (n = 143), A003004 (n = 116) and A003005 (n = 148)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (exact search; SAT with proof logging); a lucky witness is laptop-hours · open as of 2026-10-30

## The problem

r_k(n) is the largest subset of {1..n} with no k-term arithmetic progression (Erdős problems #3, #139, #142 for the asymptotics). Exact small values for k = 4, 5, 6 are OEIS A003003, A003004 and A003005. Their b-files come from Fausto A. C. Cariboni (2018), who also posted the extremal sets: A003003 to n = 142 (r_4(142) = 58; a(52)-a(72) earlier from Rob Pratt, 2015), A003004 to n = 115 (r_5(115) = 67) and A003005 to n = 147 (r_6(147) = 95). Earlier work is by Wagstaff (1972), Karl Rubin (1973) and Shao-Deng-Liang-Xu (J. Comput. Syst. Sci. 2012). None of these entries has changed since 2018 (no %E after 2018, as fetched on 2026-10-30), and the k = 3 case is a separate bank target (r3-212-salem-spencer-unit-gap). Each sequence is nondecreasing with steps of at most 1, so the next term is one of two values: either a witness one larger than the last term or an exhaustive certificate settles it. Target: a new exact term of one of the three sequences.

## What counts as a win

Success means, for some k in {4, 5, 6}, the exact value of r_k(n) at the first index n beyond the live b-file (n = 143 for A003003, n = 116 for A003004, n = 148 for A003005, re-fetched immediately before claiming). The proof needs (i) an explicit witness set of the claimed size in {1..n} with no k-term AP, checked by two programs, and (ii) unless the witness is one larger than r_k(n-1), a certificate that no set one larger exists: a DRAT/LRAT UNSAT proof checked by drat-trim or cake_lpr on a CNF regenerated independently from the definition, or two independently written exact searches that agree. The value must not already appear in the entry's data, b-file, a-files or history, or in a newer paper found by a fresh search.

## Partial wins

- **p1:** A certified exact value r_k(N) for some k in {4,5,6} and some N beyond the live b-file that is not the next index (N at most 30 beyond the b-file end), with witness plus UNSAT/exhaustive certificate as in the main criterion.
- **p2:** An independently certified discrepancy: a witness set or UNSAT certificate showing that a value in the live A003003/A003004/A003005 b-file is wrong, reproduced by two independent programs.

## How a win is checked

Two independent checkers enumerate every start a and difference d with a+(k-1)d <= n and test membership of all k terms. For the upper bound, regenerate the CNF (one clause per k-AP forbidding all k true, plus a cardinality encoding checked on small n), run drat-trim/cake_lpr, and calibrate by reproducing the last three b-file values. Compare with the live entries and their history pages.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A003003>

## Sources

- <https://oeis.org/A003003>
- <https://oeis.org/A003004>
- <https://oeis.org/A003005>
- <https://oeis.org/A003003/a003003_1.txt>
- <https://doi.org/10.1016/j.jcss.2011.09.003>
- <https://www.erdosproblems.com/142>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reuse the r_3 machinery: window-cardinality pruning from the known exact values (every interval of length L holds at most r_k(L)), endpoint forcing, and reflection symmetry.
- Seed the witness search with Cariboni's extremal sets at n-1 and try to extend by one element with SAT repair of a sliding window.
- For k = 5 the b-file stops at the shortest n (115). Its last terms sit on a plateau (67 for 113..115), so the next term is likely to stay at 67 and needs only the UNSAT side.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Offsets: A003003, A003004 and A003005 start at n = 1, unlike A003002 (n = 0).
- A progression means k distinct terms in AP with d >= 1. Check every difference, not only d <= n/(k-1) for a fixed start.
- A heuristic search that finds no larger set is not a proof. The upper bound needs a checkable certificate.
- WebSearch was unavailable when this entry was written: do a fresh literature search (e.g., later Shao/Cariboni-style computations) before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/rk-ap-free-next-terms-k4-k5-k6.md
```

Already set up? Say `run V3R1T4S on rk-ap-free-next-terms-k4-k5-k6`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rk-ap-free-next-terms-k4-k5-k6`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
