# Unrestricted ternary, quaternary and 5-ary codes A_q(n,d): new lower bound in Brouwer's small q-ary tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Brouwer's tables of general (nonlinear) codes over alphabets of size 3, 4 and 5 (from Brouwer-Hamalainen-Ostergard-Sloane 1998, Bogdanova-Brouwer-Kapralov-Ostergard 2001, Bogdanova-Ostergard 2001, with later improvements by Laaksonen-Ostergard 2017/2019 and others) list lower/upper bounds for n up to 16 (q=3), 12 (q=4) and 11 (q=5) with wide gaps, e.g. on 2026-10-28: A3(12,7) 60-108, A3(16,8) 387-1923, A3(15,10) 27-39, A5(9,5) 893-2152, A5(10,6) 625-1625. The ternary table credits football-pool enthusiasts ('found by ehl555', 'found by Codigo', 'spaik', 'PacoHH', 'Joan'), so local search on a laptop has produced records here; the ternary and 5-ary pages were updated on 2026-10-17 with new lower bounds from Oscar Sanchez (A3(14,8) >= 123, A3(15,5) >= 7929, A5(7,3) >= 1601, A5(9,4) >= 4500, A5(9,5) >= 893, A5(10,4) >= 18750). The quaternary page was last modified 2017-09-07.

## What counts as a win

Success means an explicit list of M distinct words over {0..q-1}^n (q in {3,4,5}) such that an independent script confirms all pairwise Hamming distances >= d, and M is STRICTLY GREATER (direction: max) than the lower bound for A_q(n,d) in the corresponding live table (https://aeb.win.tue.nl/codes/ternary-1.html, https://aeb.win.tue.nl/codes/quaternary-1.html or https://aeb.win.tue.nl/codes/5ary-1.html), re-fetched live immediately before claiming; '=' entries are exact and cannot be beaten; the improvement must not appear in the notes under the table or in an arXiv/journal search done on the day.

## Partial wins

- **p1:** An improved lower bound for a ternary cell with n = 17 or 18 (just beyond the table) over the best value in the literature.
- **p2:** An exact upper-bound improvement certified by a checkable LP/Delsarte certificate in rational arithmetic for one cell.

## How a win is checked

Parse codewords; pairwise Hamming distances vectorised in numpy (M up to ~2*10^4 fine); parse the live table cell (note 'ub'/'lb' rows and '=' convention). Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://aeb.win.tue.nl/codes/ternary-1.html>

## Sources

- <https://aeb.win.tue.nl/codes/ternary-1.html>
- <https://aeb.win.tue.nl/codes/quaternary-1.html>
- <https://aeb.win.tue.nl/codes/5ary-1.html>
- <https://aeb.win.tue.nl/codes/ternary.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prescribed-automorphism clique search: pick a group (cyclic runs x alphabet permutations, or PSL(2,p) on n=p+1 coordinates), compute orbits, max-weight clique on orbits.
- Unions of cosets of linear codes from codetables.de over GF(3)/GF(4)/GF(5) (a linear [n,k,d] code gives q^k words; unions of compatible cosets add more).
- Target cells with the widest relative gap (ub/lb) and moderate size (lb < 5000) first, e.g. A3(12,7), A3(13,7..8), A5(8..9,5..6).
- Cross-domain import (football-pool / lottery wheel design): the pool community's covering/packing heuristics (tabu search on forms) have already produced table entries; reuse their local-search with 'remove k, re-insert greedy' moves.
- Cross-domain import (quantum annealing / QUBO): formulate packing as QUBO on orbit variables and run classical simulated bifurcation / parallel tempering QUBO solvers.
- Cross-domain import (molecular dynamics): treat codewords as particles with repulsive potential on the Hamming graph and anneal, then repair violations.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Verify the minimum distance over ALL pairs (nonlinear codes) or all codewords (linear), never by sampling.
- Literature-ahead-of-table trap: Brouwer's pages are updated irregularly but are very active right now (binary table last modified 2026-10-21, ternary and 5-ary 2026-10-17, mixed binary/ternary 2026-10-17, quaternary not since 2017-09-07, with four independent groups sending improvements in October 2026); search arXiv for the specific (n,d) and re-fetch the page immediately before claiming.
- The tables' text notes list improvements that may not yet be reflected in the grid, and some older notes are superseded by the grid (e.g. the ternary notes still mention A3(13,4) >= 8559 and A3(14,4) >= 24786, while the grid now shows 13122 and 27702); compare against the max of grid and notes.
- q=4 codes from GF(4)-linear codes are often already in the table via codetables; a linear code is not an improvement unless M exceeds the unrestricted lb.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/brouwer-qary-unrestricted-a3-a4-a5.md
```

Already set up? Say `run V3R1T4S on brouwer-qary-unrestricted-a3-a4-a5`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `brouwer-qary-unrestricted-a3-a4-a5`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
