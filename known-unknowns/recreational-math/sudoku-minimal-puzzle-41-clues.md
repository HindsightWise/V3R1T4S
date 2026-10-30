# Most clues in a minimal 9 x 9 Sudoku: a minimal puzzle with 41 clues (only two 40-clue minimal puzzles are known)

🎲 **Recreational math** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

A minimal (irreducible) Sudoku has a unique solution, and deleting any clue gives a puzzle with several solutions. The minimum, 17, is settled (McGuire-Tugemann-Civario 2014). The maximum is open. Mladen Dobrichev ('dobrichev') found the only two known 40-clue minimal puzzles during the programmers-forum project on the 40+ clue space, where he and 'blue' made the main progress. He also collected 2,650 minimal 39-clue puzzles (batches to July 2015) and posted one more on 7 Aug 2025. The search is documented in eleven's thread 'High clue tamagotchis' (New Sudoku Players' Forum, 2010-2025), building on Havard's and others' earlier 'Max number of clues' threads. On 29 Jun 2025 eleven confirmed that the two 40s are still the only known ones and that nobody has searched seriously since; he rates the chances of a 41 as close to zero. Nobody has published a proof that 40 is the maximum. Mathimagics' 2019 table lists GNC = 40 for 3x3 boxes and leaves it unknown for every larger size. We re-verified both 40s on 2026-10-30 by SAT. Both are unique and minimal, with the same solution grid. Target: a minimal 41-clue puzzle, or a proof that none exists.

## What counts as a win

Success means either (a) a 9 x 9 Sudoku with at least 41 givens (STRICTLY more than 40; direction: max) that has exactly one completion and is minimal: for every given, deleting it leaves at least two completions, shown by an explicit second solution. Both properties must be confirmed by two independent exact solvers. Or (b) a machine-checked proof that no minimal 9 x 9 puzzle has 41 or more givens, establishing 40 as the maximum. Re-fetch the last pages of http://forum.enjoysudoku.com/high-clue-tamagotchis-t30020.html immediately before claiming: they must show no 41.

## Partial wins

- **p1:** A third minimal 40-clue puzzle that is not equivalent to either known 40 under the Sudoku symmetry group (3,359,232 geometric maps x 9! relabellings), shown by comparing minlex canonical forms.
- **p2:** A minimal 39-clue puzzle that is not equivalent to any of the 2,651 known 39s: dobrichev's list, reposted by ghfick on 8 Aug 2025 in the thread, plus dobrichev's 7 Aug 2025 puzzle.
- **p3:** A reproducible exhaustive proof, agreed by two independent programs, that the solution grid of the two known 40s (576821349812934567934576182741358296358692471629147853463715928185269734297483615) has no minimal puzzle with 41 or more clues.

## How a win is checked

Check that the givens are consistent. Run a SAT or DLX count capped at 2 for uniqueness, then one count per deleted given for minimality (81 checks, well under a second). Canonicalize to minlex (gsf-style or Serg's canonicalizer) to compare with the known 40s and 39s.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://forum.enjoysudoku.com/high-clue-tamagotchis-t30020-210.html>

## Sources

- <http://forum.enjoysudoku.com/high-clue-tamagotchis-t30020.html>
- <http://forum.enjoysudoku.com/high-clue-tamagotchis-t30020-195.html>
- <http://forum.enjoysudoku.com/high-clue-tamagotchis-t30020-210.html>
- <http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801-15.html>
- <https://github.com/dobrichev/sudoku35plus>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Dobrichev's sudoku35plus tool describes the seed-and-strip approach (subgrids with up to 40 givens, then strip to minimal); the forum says nobody has searched seriously since the 40s were found.
- High-clue minimal puzzles concentrate clues in a few boxes with many 'pinned' cells; search the space of minimal sub-puzzles of grids with many unavoidable 4-sets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 'Minimal' means no single clue is redundant; it does not mean the minimum number of clues for its grid.
- A valid but non-minimal 41-clue puzzle is trivial (any 41 cells of a grid); only minimal ones count.
- The original 40+ thread was lost in a forum crash; check dobrichev's and blue's later posts before calling a 39 or 40 new.
- Mathimagics (Apr 2019) mentions 1,261,278 puzzles extracted from Mladen's data, so larger unposted collections of high-clue puzzles may exist; p2 is judged only against the 2,651 posted 39s, and a claimant must say where a 'new' 39 came from.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/sudoku-minimal-puzzle-41-clues.md
```

Already set up? Say `run V3R1T4S on sudoku-minimal-puzzle-41-clues`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sudoku-minimal-puzzle-41-clues`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
