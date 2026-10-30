# Ramsey numbers of small complete bipartite graphs R(K_{m,n}, K_{p,q}): close a gap in DS1 Tables IVb/IVc (R(K3,5,K3,4) 25-29, R(K2,10,K2,7) 29-31, R(K2,2,K2,19) 28-29, R(K4,4,K4,4) 33-49)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for lower bounds (graphs on 20-65 vertices); laptop-days to needs cluster for upper bounds · open as of 2026-10-30

## The problem

Here edges of K_N are 2-coloured and complete bipartite graphs are avoided (not the bipartite Ramsey numbers of coloured K_{n,n}). DS1 revision #18 (24 Apr 2026), Section 3.3, Tables IVb and IVc, lists these open cases: R(K3,4, K3,3) 19-20; R(K3,5, K2,4) 19-20; R(K3,5, K2,5) 21-23; R(K3,5, K3,3) 21-24; R(K3,5, K3,4) 25-29; R(K2,5, K2,8) 22-23; R(K2,6, K2,10) 27-29; R(K2,7, K2,10) 29-31; R(K2,m, K2,11) for m = 3..6, where Table IVc prints only the lower bounds 22, 25, 28, 29 but DS1 item 3.3.2(j) (R(K2,n-s, K2,n) <= 4n-2s-3 for s >= 2, n >= s+2) gives the upper bounds 25, 27, 29, 31, so the gaps are 22-25, 25-27, 28-29 and 29-31 (for m = 7 the same item gives <= 33, equal to the printed lower bound 33, so R(K2,7, K2,11) = 33 is already determined and is not part of this target); R(K2,2, K2,19) 28-29 (item 3.3.1.f); and 33 <= R(K4,4, K4,4) <= 49 (item 3.3.1.i). The diagonal case DS1 calls the first open one, 65 <= R(K2,17, K2,17) <= 66 (item 3.3.1.h), is in fact settled. By Exoo-Harborth-Mengersen it equals 66 iff an srg(65,32,15,16) exists, and Gritsenko constructed one (arXiv:2102.05432, 2021), so it is not part of this target. No 2026 arXiv paper found changes the listed cells. Credit: Lortz and Mengersen, Harborth and Mengersen, Exoo-Harborth-Mengersen, Shao and coauthors, Dybizbanski, Goedgebeur and Van Overberghe, and Lidicky-Pfender (flag-algebra upper bounds).

## What counts as a win

Either (a) an explicit graph G on N vertices such that G contains no K_{m,n} and its complement contains no K_{p,q} (as subgraphs, not necessarily induced), checked by two independent exact programs, with N+1 STRICTLY GREATER (direction: max) than the lower bound for that cell in the live DS1 and any newer paper found by a fresh search; or (b) an upper bound STRICTLY BELOW (direction: min) the DS1 upper bound, backed by a DRAT/LRAT UNSAT certificate of a stated encoding (with any symmetry breaking proved sound) or an exact-rational flag-algebra certificate, re-verifiable by a referee. Off-by-one: a graph on N vertices proves R >= N+1.

## Partial wins

- **p1:** An unpublished (asterisked) DS1 entry, such as R(K3,5,K2,3) = 17* (Table IVb) or R(K2,9,K2,5) = 25* (Table IVc), confirmed by a fully verified lower-bound graph and a DRAT/LRAT UNSAT certificate for the upper bound.

## How a win is checked

K_{s,t}-freeness: for every s-subset S of vertices (or every pair when s = 2), count common neighbours and require fewer than t; do the same in the complement. Implement once with bitsets and once as a SAT/CP query that must be UNSAT. For upper bounds check the proof with drat-trim or cake_lpr and re-derive the encoding from the stated parameters.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/>
- <https://arxiv.org/abs/1704.03592>
- <https://github.com/Steven-VO/circulant-Ramsey>
- <https://arxiv.org/abs/2102.05432>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Polycirculant SAT search as in Goedgebeur-Van Overberghe.
- Strongly regular graphs: R(K2,n,K2,n) = 4n-2 iff an srg(4n-3,2n-2,n-2,n-1) exists (Exoo-Harborth-Mengersen). Before searching an off-diagonal cell, check srg witnesses from Brouwer's table: an srg with at most t-1 common neighbours per pair avoids K_{2,t}.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- R(K2,17,K2,17) = 66 is settled. DS1 3.3.1.h still prints 65-66, but EHM2's criterion and Gritsenko's srg(65,32,15,16) give 66. Likewise Verma's srg(85,42,20,21) (arXiv:2610.08893) gives R(K2,22,K2,22) = 86. Diagonal R(K2,n,K2,n) cells are not part of this target.
- Upper and lower table entries are stacked in the PDF; read the cell from the survey text, not a layout dump.
- Table IVc's row n = 11 shows only lower bounds, but upper bounds are not missing: DS1 item 3.3.2(j) gives R(K2,n-s, K2,n) <= 4n-2s-3, which reproduces the table's upper bounds where both exist (e.g. 31 for R(K2,7,K2,10), 35 for R(K2,8,K2,11)) and closes R(K2,7,K2,11) = 33. Compare any new upper bound with it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/ramsey-complete-bipartite-small-cells.md
```

Already set up? Say `run V3R1T4S on ramsey-complete-bipartite-small-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ramsey-complete-bipartite-small-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
