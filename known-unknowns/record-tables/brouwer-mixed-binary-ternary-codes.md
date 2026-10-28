# Mixed binary/ternary codes N(m,n,d): new lower bound in Brouwer's mixed-code tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

N(m,n,d) is the maximum number of words with m binary and n ternary coordinates at mutual Hamming distance >= d. Brouwer's page (tables copied from Brouwer-Hamalainen-Ostergard-Sloane 1998 with later improvements; HTTP Last-Modified 2026-10-17, no visible date on the page) tabulates bounds for d = 3..10; on 2026-10-28 the grids contain 253 cells still given as lower-upper ranges (counting the pure m=0 / n=0 border cells shown in the grids). Lower-bound improvements came from Ostergard and others and from football-pool enthusiasts (Codigo, PacoHH, Pucho, ehl555, Pedro fdez, 2010-2013), and most recently from Oscar Sanchez (2026, e.g. N(12,2,3) >= 1552, N(10,3,3) >= 1176, N(7,5,5) >= 104, N(5,8,5) >= 513, N(3,10,5) >= 736, N(5,9,7) >= 73, N(2,11,7) >= 77). The upper bounds of Naszvadi-Koniorczyk (arXiv:2310.01883) appear only in an HTML comment in the page source, marked 'not better than PRJÖ' (Östergård); they are not shown on the rendered page. The problem is the packing side of the football-pool problem and has received far less computation than pure binary codes.

## What counts as a win

Success means an explicit list of M distinct words in {0,1}^m x {0,1,2}^n (m >= 1, n >= 1) with all pairwise Hamming distances >= d (checked exhaustively by an independent script), where M is STRICTLY GREATER (direction: max) than the lower bound for N(m,n,d) on https://aeb.win.tue.nl/codes/23codes.html (grid and notes) re-fetched live immediately before claiming, and not already exceeded in an arXiv/journal search done on the day.

## Partial wins

- **p1:** A new code meeting a lower bound in a cell where the page records no explicit construction (only an existence argument or an announcement, e.g. the d=3 bounds announced by Código for which the page says 'No explicit construction was given'), giving the explicit word list, verified exhaustively.

## How a win is checked

Parse words, check coordinate alphabets (first m binary, last n ternary), pairwise distances in numpy; parse the live table cell. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://aeb.win.tue.nl/codes/23codes.html>

## Sources

- <https://aeb.win.tue.nl/codes/23codes.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the best pure ternary code of length m+n and binarise m coordinates (map ternary symbols to binary with a partition maximising retained distance) then re-optimise; and conversely extend binary codes.
- Prescribed automorphism groups acting separately on binary and ternary coordinate blocks; clique search on orbits.
- Exploit the d=3 cells' link to perfect/mixed perfect codes (sphere-packing bound is often near tight); search near-perfect codes by tabu.
- Cross-domain import (sports betting / football-pool systems): pool-system enthusiasts' packing heuristics and published 'reduced systems' are a source of seeds.
- Cross-domain import (crystal structure prediction): treat the mixed Hamming space as a product lattice and use symmetric 'Wyckoff-orbit' generation to produce candidate structures.
- Cross-domain import (integer programming from scheduling): column generation over orbit 'patterns' with Gurobi-free solvers (HiGHS/SCIP).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Verify the minimum distance over ALL pairs (nonlinear codes) or all codewords (linear), never by sampling.
- Literature-ahead-of-table trap: Brouwer's pages are updated irregularly but are very active right now (binary table last modified 2026-10-21, ternary and 5-ary 2026-10-17, mixed binary/ternary 2026-10-17, quaternary not since 2017-09-07, with four independent groups sending improvements in October 2026); search arXiv for the specific (n,d) and re-fetch the page immediately before claiming.
- Confusing (m binary, n ternary) order in the table axes is an easy way to compare against the wrong cell.
- Cells with m=0 or n=0 are the pure tables, handled by separate entries.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/brouwer-mixed-binary-ternary-codes.md
```

Already set up? Say `run V3R1T4S on brouwer-mixed-binary-ternary-codes`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `brouwer-mixed-binary-ternary-codes`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
