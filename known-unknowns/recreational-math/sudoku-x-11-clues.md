# Sudoku-X with 11 clues: beat the 12-clue minimum (known since 2007; 558,981 12-clue puzzles known, 552,952 public)

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

Sudoku-X is 9 x 9 Sudoku in which both main diagonals must also contain 1-9. The diagonals destroy many unavoidable sets, so Sudoku-X needs fewer clues than the 17 of plain Sudoku. Since November 2005 the best was 13. In July 2007 Ruud (SudoCue) found 12-clue Sudoku-X puzzles by neighbourhood search (forum thread '13-clue Sudoku X', 2005-2024). His 'Minimum Sudoku-X Collection' page says the search continues, doubts an 11 will ever be found, and offers a zip of 552,952 12-clue puzzles. That zip is the community list. From August 2018 Mathimagics, Leren and ton grew Ruud's 7,193 puzzles (7,180 after duplicates were removed) to 552,950 in the New Sudoku Players' Forum thread 'SudokuX (Diagonal Sudoku)', and Ruud added 2 in January 2022. Leren and ton kept searching. They had 558,389 known 12s by 10 Dec 2023 and 558,981 by 24 Nov 2024 (Leren, same thread). The roughly 6,000 newer puzzles are not posted. No 11-clue Sudoku-X has been found. Leren (Sept and Nov 2024) listed 67 'almosts': 11-clue sets with exactly two Sudoku-X solutions, only four of them using 8 distinct digits. m_b_metcalf (2022-2024) keeps analysing the collection (symmetric patterns, ratings up to ED 10.6). Mathimagics counted 9! x 153,255,603,504 Sudoku-X grids, and blue (Aug 2018) reduced this to 1,596,582,158 essentially different ones. Equivalence: 96 geometric maps (8 rotations and reflections x the joint r4 < ->r6, c4 < ->c6 swap x 6 joint permutations of the row/column pairs {1,9}, {2,8}, {3,7}), times relabelling. The trivial lower bound is 8. We re-verified two 12-clue examples on 2026-10-30 by SAT: unique and minimal as Sudoku-X, and not unique as plain Sudoku. All 67 almosts have exactly two Sudoku-X solutions. Target: an 11-clue Sudoku-X, or a proof that 12 is the minimum.

## What counts as a win

Success means either (a) a 9 x 9 array with at most 11 givens (STRICTLY fewer than 12; direction: min) with exactly one completion satisfying rows, columns, 3 x 3 boxes and both main diagonals, confirmed by two independent exact solvers or by a solution plus a DRAT-checked UNSAT proof; or (b) a machine-checked proof that every Sudoku-X with at most 11 givens has zero or several completions, e.g. a certified exhaustive search over essentially different Sudoku-X grids. Re-fetch https://www.sudocue.net/minx.php and the last pages of http://forum.enjoysudoku.com/sudokux-diagonal-sudoku-t34959.html and http://forum.enjoysudoku.com/13-clue-sudoku-x-t2715.html immediately before claiming: none may report an 11-clue puzzle or a proof.

## Partial wins

- **p1:** A new 'almost': a set of 11 givens with exactly two Sudoku-X completions, confirmed by two independent exact solvers. It must not be equivalent to any of the 67 almosts Leren posted on 27 Sept 2024 in the thread 'Symmetric 12-clue x-sudokus' (http://forum.enjoysudoku.com/symmetric-12-clue-x-sudokus-t43405.html) under the 96-element Sudoku-X geometric group and relabelling, compared by canonical form.
- **p2:** A reproducible exhaustive proof, agreed by two independent programs, that none of the solution grids underlying the SudoCue 12-clue collection has an 11-clue Sudoku-X puzzle.

## How a win is checked

CNF or DLX with 29 constraint groups (9 rows, 9 columns, 9 boxes, 2 diagonals). Count solutions up to 2 and check minimality per given. For p1, count up to 3 and require exactly 2. Then canonicalize under the 96 geometric maps (check that your enumeration of Sudoku maps preserving the diagonal pair finds exactly 96) and relabelling, and compare with Leren's 67 posted almosts. For p2, the grids come from solving the downloaded SudoCue zip.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://forum.enjoysudoku.com/sudokux-diagonal-sudoku-t34959-75.html>

## Sources

- <https://www.sudocue.net/minx.php>
- <http://forum.enjoysudoku.com/sudokux-diagonal-sudoku-t34959-75.html>
- <http://forum.enjoysudoku.com/sudokux-diagonal-sudoku-t34959-15.html>
- <http://forum.enjoysudoku.com/13-clue-sudoku-x-t2715-45.html>
- <http://forum.enjoysudoku.com/symmetric-12-clue-x-sudokus-t43405.html>
- <http://forum.enjoysudoku.com/12-clue-sudoku-x-t37941.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Grow from Leren's 67 'almosts' (11 clues, two solutions): try all one-cell moves and relabellings, then test uniqueness.
- Port the McGuire hitting-set method: with 1,596,582,158 essentially different Sudoku-X grids (blue, Aug 2018) and only 11 clues to place per grid, an exhaustive search looks cluster-scale rather than out of reach.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Ruud's early collections contained invalid puzzles and duplicates from a canonicalization bug: swapping rows 4 and 6 alone is not a Sudoku-X symmetry, it must go with columns 4 and 6.
- Diagonal conventions differ between sites; both main diagonals must hold 1-9.
- Sudoku-DG/SudokuP, Windoku-X and other combined variants are different problems.
- The SudoCue zip (552,952) is not the full list. Leren and ton knew 558,981 12-clue puzzles on 24 Nov 2024, and the extra ones are unpublished, so a 12 missing from the zip is not evidence that it is new. That is why it is not a partial win.
- Most almosts use only 7 distinct digits, so they are two-solution sets for a trivial reason (swap the two missing digits). Only the 4 with 8 distinct digits are close to an 11.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/sudoku-x-11-clues.md
```

Already set up? Say `run V3R1T4S on sudoku-x-11-clues`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sudoku-x-11-clues`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
