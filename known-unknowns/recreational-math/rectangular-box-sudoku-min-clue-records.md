# Fewest clues for Sudoku with other box shapes: beat ton's records (10x10 2x5: 22, 12x12 2x6: 32, 12x12 3x4: 30, 15x15 3x5: 48, 20x20 4x5: 88, 25x25 5x5: 146)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (SAT uniqueness checks take seconds to a minute even at 25 x 25) · open as of 2026-10-30

## The problem

For N x N Sudoku with h x w boxes, the fewest givens of a uniquely solvable puzzle is known only up to 9 x 9. OEIS A372224 (Gomez de la Vega and Karamchedu, 2024) tabulates the smallest critical set with A033676(n) x A033677(n) boxes for n <= 9 (a(6) = 8, a(8) = 14, a(9) = 17), so its a(10) (2 x 5 boxes) and a(12) (3 x 4 boxes) are open. For prime n the board is a Latin square; Richard Bean's October 2026 preprint (arXiv:2610.18199, not yet refereed) proves the minimum floor(n^2/4) there. The best-known values are in the New Sudoku Players' Forum thread 'Minimum givens on larger puzzles'. All are by 'ton': 10x10 (2x5) 22, 12x12 (2x6) 32, 12x12 (3x4) 30 and 15x15 (3x5) 48 (1 Apr 2017); 25x25 (5x5) 146 (1 Apr 2019); 20x20 (4x5) 88 (1 Apr 2024, after 91 in 2019 and 89 in 2021). Mathimagics (2019) and coloin keep summary tables there, now stale for 4x5. ton's heuristic floor(N^2/4) - (h-1)(w-1) is met exactly for 3x4, 3x5 and 4x5 boxes but not for 2x5 (21), 2x6 (31) or 5x5 (140). The thread's last post is from June 2024. We re-verified all six records on 2026-10-30 by SAT: each is unique and minimal. 16 x 16 (4x4) is a separate bank target. Target: strictly fewer clues for one listed shape, or a certified optimality proof.

## What counts as a win

Success means, for one listed shape (N, h x w) in {(10, 2x5), (12, 2x6), (12, 3x4), (15, 3x5), (20, 4x5), (25, 5x5)} with h rows and w columns per box, either (a) a puzzle with STRICTLY fewer givens than the live record (direction: min) and exactly one completion, shown by a solution plus a DRAT/LRAT-checked UNSAT proof after blocking it, or by two independent exact solvers each reporting one solution; or (b) a machine-checked proof that the live record is optimal. Case (b) would settle A372224 a(10) = 22 or a(12) = 30. Re-fetch the forum thread (all pages, http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801.html) and https://oeis.org/A372224 immediately before claiming; the claim must beat the best value shown there and in any later post.

## Partial wins

- **p1:** A certified lower bound above the trivial N - 1 for one listed shape, e.g. a DRAT-checked or two-implementation exhaustive proof that no 10 x 10 (2 x 5) puzzle with 11 or fewer givens is uniquely solvable.
- **p2:** A first record for a box shape absent from the thread on 2026-10-30: a unique, minimal puzzle with STRICTLY fewer than floor(N^2/4) givens (the value of the generic qiuyanzhe/hkociemba construction), i.e. 14 x 14 (2x7) with <= 48, 18 x 18 (3x6) with <= 80, or 24 x 24 (4x6) with <= 143 givens.

## How a win is checked

Generic CNF encoder for N x N with h x w boxes. One model, block it, UNSAT. Minimality is optional for (a) but required for p2: each single removal must give a second model. Our pysat checker verified ton's 25 x 25 record in under 60 s. Cross-check with an independent DLX.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801-30.html>

## Sources

- <http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801.html>
- <http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801-15.html>
- <http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801-30.html>
- <https://oeis.org/A372224>
- <https://arxiv.org/abs/2610.18199>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The shapes where records sit above ton's formula (2x5 at 22 vs 21, 2x6 at 32 vs 31, 5x5 at 146 vs 140) are the natural first attacks.
- Neighbourhood search {-k+m} from ton's puzzles with a fast SAT oracle; or SAT-based search with cardinality constraints on a fixed solution grid (minimum hitting set of unavoidable sets).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 2x6 and 3x4 boxes on 12 x 12 are different problems; A372224 uses the A033676 x A033677 shape (2x5 for 10, 3x4 for 12).
- For prime N the board is a Latin square, and Bean's October 2026 preprint proves the minimum floor(N^2/4): nothing to win there.
- The thread mixes 'h x w' and 'w x h' notation; state rows x columns per box explicitly.
- The summary tables in the thread (coloin, Mathimagics 2019) still show 91 for 4x5; the live record is ton's 88 of April 2024.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/rectangular-box-sudoku-min-clue-records.md
```

Already set up? Say `run V3R1T4S on rectangular-box-sudoku-min-clue-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rectangular-box-sudoku-min-clue-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
