# Linear ordered orthogonal arrays of depth 2-8: higher strength than MinT's best known (MinT 'Advanced' tables)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-minutes to laptop-hours · open as of 2026-10-30

## The problem

A linear OOA(b^m, s, F_b, T, k) of depth T is an m x (sT) matrix over F_b whose columns form s blocks of T columns, such that for every (d_1..d_s) with 0 <= d_i <= T and d_1+...+d_s = k the first d_i columns of each block are linearly independent. Depth T = 1 gives orthogonal arrays (duals of linear codes, covered by codetables-binary-linear); depth T >= k gives digital nets. Its dual is a linear NRT (Rosenbloom-Tsfasman ordered) code. OOAs of intermediate depth feed net constructions such as the (u,u+v) rule. MinT's advanced interface (Schurer and Schmid, University of Salzburg; database footer 2024-09-05, no new methods listed after 2008-03-11) tabulates the best known strength k = m - t and lower bounds on t for depths 2..8. On 2026-10-30, base 2 depth 2 has 182 cells with constructive linear t above the linear lower bound for m <= 20, s <= 30, and depth 3 has 198. The smallest depth-2 gaps were (m,s) = (6,6), best t = 2 from an extended algebraic-geometric NRT code (genus 2), bound t >= 1, and (8,7) and (8,8), t = 3 vs 2. Short randomized depth-first searches in this lane and in an independent skeptic recheck (2026-10-30, under two minutes each, confirmed by exhaustive rank checks) found linear depth-2 OOAs over F_2 with t = 1 at (6,6) and t = 2 at (8,7) and (8,8), each meeting the bound. So the depth-2 tables are soft, and those three cells are taken. Cells (8,11), (9,7), (9,10), (9,15), (10,7), (10,9), (10,10) and (10,12) resisted 40-100 s each. An independent audit search (2026-10-30) reproduced the three easy cells in under a second each and also failed on (8,11), (9,7) and (10,7) within 60 s.

## What counts as a win

Success means an explicit m x (sT) matrix over F_b (b in MinT's list; field model stated for prime powers), with columns grouped into s blocks of T, whose strength k (every left-justified selection (d_1..d_s), 0 <= d_i <= T, sum k, has full column rank k, checked exhaustively) is STRICTLY GREATER (direction: max) than m minus the 'Constructive and linear' t on the live MinT query page http://mint.sbg.ac.at/query.php?i=x&b= < b > &s= < s > &m= < m > &p=smt&de= < T > , for some depth 2 <= T <= 8 with k > T, and at most m minus that page's linear lower bound on t. With k <= T the array is a digital net; such cells belong to mint-digital-nets-lower-t and do not count here. The cells (b,T,m,s) = (2,2,6,6), (2,2,8,7) and (2,2,8,8), already reached in the 2026-10-30 lane and skeptic checks, do not count. No paper, preprint or public table of any date may already give a linear OOA (or, dually, a linear NRT code) with that strength for the cell (MinT lists no new methods after 2008).

## Partial wins

- **p1:** A raised lower bound: a re-runnable exhaustive proof (two independent programs that agree, or a DRAT proof checked with drat-trim) that no linear OOA(b^m, s, F_b, T, k) exists for k = m minus MinT's live linear lower bound on t, for some depth 2 <= T <= 8 gap cell with k > T, so the linear bound on t rises by one. It counts only if no paper or preprint already proves that bound (check the RT-metric literature since 2008, e.g. Wang, Li and Heng, IEEE Trans. Inf. Theory 71 (2025) 6844-6856).
- **p2:** An exact rational dual certificate for the Martin-Stinson linear-programming bound for OOAs (association scheme of the ordered Hamming space), verified in exact arithmetic, that excludes an arbitrary (not necessarily linear) OOA(b^m, s, S_b, T, k) in a cell where MinT's arbitrary lower bound on t is smaller than the value the certificate gives.

## How a win is checked

Independent checker: enumerate all left-justified selections (d_1..d_s) with d_i <= T and sum k, and compute rank over F_b; confirm all have rank k, and that k is compared with the live MinT advanced-table cell (fetched over http) for the same base, depth, m and s. For p1, re-run both exhaustive programs. For p2, check dual feasibility and the objective in exact rational arithmetic.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://mint.sbg.ac.at/table.php?i=x&b=2&col=1&mode=cd&opt=bd&de=2&p=smt&minx=1&maxx=30&miny=0&maxy=20>

## Sources

- <http://mint.sbg.ac.at/table.php?i=x&b=2&col=1&mode=cd&opt=bd&de=2&p=smt&minx=1&maxx=30&miny=0&maxy=20>
- <http://mint.sbg.ac.at/table.php?i=x&b=2&col=1&mode=cd&opt=bd&de=3&p=smt&minx=1&maxx=30&miny=0&maxy=20>
- <http://mint.sbg.ac.at/query.php?i=x&b=2&s=6&m=6&p=smt&de=2>
- <http://mint.sbg.ac.at/query.php?i=x&b=2&s=7&m=8&p=smt&de=2>
- <http://mint.sbg.ac.at/glossary.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Depth-first search block by block, keeping for every vector of F_b^m the least selection cost that reaches it; a new block is rejected as soon as it closes a dependency of cost <= k. This settled the two smallest depth-2 cells in seconds.
- Try depth 2 and 3 in bases 3 and 4, which nobody seems to have searched.
- Seed searches from NRT codes: shorten or puncture known AG NRT codes and repair with local search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Strength must be checked for left-justified selections only (prefixes of each block), not arbitrary subsets.
- MinT's t is the log of the index: strength k = m - t.
- MinT answers only on http; table URLs need minx, maxx, miny and maxy (as in status_source) or MinT returns 'ERROR: Argument dx is missing'. Read the query page for the exact depth T you claim.
- MinT lists no new methods after 2008; search the NRT-code and OOA literature since then before claiming, e.g. LFSR-based OOA constructions (Castoldi, Moura, Panario and Stevens, arXiv:2208.00333) and new RT-metric bounds and optimal linear matrix codes (Wang, Li and Heng, IEEE Trans. Inf. Theory 2025).
- A strength k <= T makes the array a digital net: that is a different target (mint-digital-nets-lower-t).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mint-linear-ooa-depth-2-to-8.md
```

Already set up? Say `run V3R1T4S on mint-linear-ooa-depth-2-to-8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mint-linear-ooa-depth-2-to-8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
