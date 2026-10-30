# Number of short games born by day 4: tighten Suetsugu's bounds 10^28.2 < |G4| < 4.0e184 (OEIS A065401 a(4))

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (G3 has 1,474 elements; chain decompositions and antichain counts of its order; the exact |G4| would need far cleverer counting) · open as of 2026-10-30

## The problem

The short partizan games in canonical form born by day n number 1, 4, 22 and 1474 for n = 0..3 (OEIS A065401). The games born on day n number 1, 3, 18 and 1452 (A065402); a(3) was found by Dean Hickerson and Robert Li in 1974. The day-4 count is unknown. Wolfe and Fraser (Theoret. Comput. Sci. 313, 2004) proved 3.0e12 < |G4| < 10^434. Koki Suetsugu (arXiv:2208.13403, v2 24 Feb 2024; Games of No Chance 6, 2025) improved this to 10^28.2 < |G4| < 4.0e184 by dividing the partial order G3 into 86 chains (its width is 86), counting antichains, and bounding the canonical forms {L | R} built from them. He publishes G3 with its 45-level stratification as a spreadsheet (sites.google.com/site/kokisuetsugu2/games-born-by-day-3). The OEIS entry, re-read 2026-10-30, still has the keyword 'more' and no a(4), and a comment by Zhujun Zhang (May 06 2026) records Suetsugu's bounds as the current ones. Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem E7, Siegel's day-4 question) lists the same bounds as open. Applied one day earlier, to bound |G3| from G2, Suetsugu's methods give 208 <= |G3| <= 451,584 against the true 1,474, so the truth for G4 is probably much nearer 10^28 than 10^184. The lattice of games born by day 4 is known to have 2,949 levels (A065407).

## What counts as a win

CONFIRMED: either the exact value of |G4|, computed by two independent programs, or a proven bound at least ten times better than Suetsugu's: a lower bound |G4| >= 10^29.2 or an upper bound |G4| <= 4.0e183. A program that shares no code with the claimant's must reproduce every computational ingredient: the 1,474 canonical forms of G3, their partial order, any chain or antichain counts, and any family of day-4 games claimed to be distinct and canonical. Every mathematical step must be written out in full or formalised; a bound from a heuristic or from sampling does not count. The bound must not already be published at verification time (OEIS A065401 and its history, arXiv, Games of No Chance).

## Partial wins

- **p1:** Any rigorously proven lower bound above 10^28.2 or upper bound below 4.0e184, under the same reproduction rules as the success criterion.
- **p2:** An independent recomputation of G3 from the definitions, not from Suetsugu's tables or spreadsheet: all 1,474 canonical forms with their full partial order, published as a machine-readable file. It must reproduce A065402 (1, 3, 18, 1452), the 45 levels of the day-3 lattice (A065407) and Suetsugu's width of 86, shown by an 86-element antichain and a division of G3 into 86 chains. Chain divisions are not unique, so the chain lengths need not match his. A demonstration that one of these published numbers is wrong also counts.

## How a win is checked

Generate G_n from G_(n-1): every pair of antichains (L, R) of G_(n-1) gives {L | R}. Reduce each to canonical form (remove dominated options, bypass reversible ones) and compare games with the recursive order (G <= H unless some G^L >= H or some H^R <= G). Check |G1| = 4, |G2| = 22 and |G3| = 1474. Recompute the order on G3, any chains and the antichain counts with exact integer arithmetic, and re-derive the counting lemmas. For an upper bound, check that every canonical day-4 game is counted; for a lower bound, check that the claimed games are canonical and pairwise distinct.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A065401>

## Sources

- <https://oeis.org/A065401>
- <https://oeis.org/A065402>
- <https://oeis.org/A065407>
- <https://arxiv.org/abs/2208.13403>
- <https://doi.org/10.1016/j.tcs.2003.05.001>
- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Upper side: |G4| is at most the number of pairs of antichains of G3 that give canonical games. An exact count of the antichains of the 1,474-element poset (or of those with no reversible option) is the obvious first step below 4.0e184.
- Lower side: find large sub-posets of G3 in which every pair of antichains gives a distinct canonical game, as Suetsugu did with his stratification, and count them exactly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The OEIS 'last modified' footer is the site's date, not the entry's; read the entry's history for its last edit.
- Counting requires canonical forms: many pairs of antichains give equal games through reversible options, so a count of option pairs is only an upper bound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/games-born-by-day-4-count.md
```

Already set up? Say `run V3R1T4S on games-born-by-day-4-count`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `games-born-by-day-4-count`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
