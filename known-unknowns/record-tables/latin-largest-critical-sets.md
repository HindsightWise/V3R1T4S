# Largest critical sets lcs(n) of Latin squares: a critical set larger than the A063437 records for n = 8..17 (Bean's 2026 searches, n = 9..15 and 17)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (uniqueness-of-completion checks by SAT/DLX for n <= 17) · open as of 2026-10-30

## The problem

A critical set of a Latin square L is a partial Latin square that L is the unique completion of, and that is minimal: deleting any filled cell allows a second completion. The smallest size scs(n) = floor(n^2/4) has just been proved (Richard Bean, arXiv:2610.18199, Oct 2026). The largest size lcs(n) (OEIS A063437) is known only for n <= 7, with lcs(7) = 25 (Bean, Mar 2026). The proven upper bound is lcs(n) <= n^2 - 3n + 3 (Bean and Mahmoodian, Discrete Math. 267 (2003)). Bean conjectures, in the README of github.com/RichardBean/LatinSquares, that lcs(n) <= n^2 - 3^(log2 n). The records at n = 8 (37) and n = 16 (175) meet that bound. They are the older critical sets of size 4^k - 3^k in the elementary abelian 2-group table of order 2^k (Stinson and van Rees). Lower bounds at the other orders improved sharply in 2026 through Bean's searches (OEIS comment, 13 May 2026, examples in a063437_1.txt, which has none for n = 8 or 16): lcs(9) >= 46, lcs(10) >= 59, lcs(11) >= 74, lcs(12) >= 90, lcs(13) >= 105, lcs(14) >= 126, lcs(15) >= 147, lcs(17) >= 198. Earlier records came from Stinson-van Rees (1982) and Bean's thesis (arXiv:2606.12996).

## What counts as a win

Success means a partial Latin square P of order n, 8 <= n <= 17, with |P| STRICTLY GREATER than the live A063437 lower bound for n. Re-fetch A063437 immediately before claiming; on 2026-10-30 the bounds were 37, 46, 59, 74, 90, 105, 126, 147, 175, 198 for n = 8..17. P must satisfy: (a) P has exactly one completion to a Latin square, shown by a completion plus a DRAT-verified UNSAT proof or an exact-cover count of 1; and (b) for every filled cell e of P, P minus e has at least two completions, shown by an explicit second Latin square containing P minus e. Checked by two independent programs. At n = 8 and n = 16 the record equals Bean's conjectured bound n^2 - 3^(log2 n), which is not proven, so a win there also refutes that conjecture.

## Partial wins

- **p1:** Answer Bean's question of how many of the 147 main classes of order 7 contain a critical set of size 25 (his thesis found 113). The answer needs two independent exhaustive programs that agree, the list of classes and one size-25 critical set for each, each set checked as in the verification method.

## How a win is checked

Check P is a partial Latin square. Find its completion L. Prove uniqueness by adding the clause 'differs from L' to a Latin-square CNF with P fixed, then checking the solver's UNSAT certificate with drat-trim, or by a DLX count of 1 from two programs. For each cell of P, check the supplied alternative completion is Latin, contains P minus that cell, and differs from L.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A063437>

## Sources

- <https://oeis.org/A063437>
- <https://oeis.org/A063437/a063437_1.txt>
- <https://github.com/RichardBean/LatinSquares>
- <https://arxiv.org/abs/math/0107159>
- <https://arxiv.org/abs/2606.12996>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Bean's 2026 records came from perturbation and chunk-shuffle local search on fixed squares; vary the underlying square (intercalate-rich squares host large critical sets).
- Grow a critical set greedily, adding cells while uniqueness fails, then prune; use an incremental SAT solver with assumptions for the many uniqueness queries.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A defining set that is not minimal is not a critical set; check condition (b) for every cell.
- scs(n) is now proved; only the largest critical set is a target here.
- Records moved in May 2026; re-fetch A063437 and Bean's repository.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/latin-largest-critical-sets.md
```

Already set up? Say `run V3R1T4S on latin-largest-critical-sets`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `latin-largest-critical-sets`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
