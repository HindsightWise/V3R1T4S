# Rectangular sliding-tile puzzles: the first unknown God's numbers of the m x n table (OEIS A151944): 3x6, 2x9, 4x5

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster for an exact diameter (about 3.2e15 states for 3x6 and 2x9); laptop-hours for certified lower bounds · open as of 2026-10-30

## The problem

OEIS A151944 tabulates T(m,n), the maximal number of single-tile moves needed to solve the m x n sliding-tile puzzle. The entry (re-fetched 2026-10-30, last edited 2024-06-08) gives data through the seventh antidiagonal plus 1 x 8 = 7 and 2 x 7 = 108, and its example array adds 2 x 8 = 140: the 1 x n and 2 x n values to 2 x 8 (140), 3 x 3 = 31, 3 x 4 = 53, 3 x 5 = 84 and 4 x 4 = 80, from complete breadth-first searches by Richard Korf (JACM 2008, with corrections by Tomas Rokicki, 2011), Anton Kulchitsky and others. The 2 x n row A151943 also ends at n = 8, and Ben Whitmore (2021) gave T(2,n) >= 2n^2 - n. No value is listed for 3 x 6 (equivalently 6 x 3), 2 x 9 or 4 x 5, the first open cells. The square n x n cases are A087725 (the 5 x 5 case is the bank's slide-24-puzzle-lower-bound entry and is excluded here).

## What counts as a win

For at least one cell of A151944 with m, n >= 2, m != n and no value in the live entry at claim time (3 x 6, 2 x 9 and 4 x 5 being the first): the exact God's number, certified by a complete search whose per-depth position counts sum to (mn)!/2 and which an independent skeptic can rerun or check against a second implementation, together with an explicit antipodal position and its optimal solution. The value must not appear in A151944, A151943 or a later publication found at claim time.

## Partial wins

- **p1:** A 2 x 9 position with a certified optimal solution length strictly greater than 153 = 2*9^2 - 9 (Whitmore's general lower bound), certified by an exact IDA* or bidirectional search with an admissible heuristic, giving a new lower bound for T(2,9).
- **p2:** A 3 x 6 position with a certified optimal solution length strictly greater than 84 = T(3,5), giving the first published certified lower bound for T(3,6) above that value, or strictly greater than the best lower bound published for T(3,6) at claim time if one exists.
- **p3:** A rigorous upper bound for T(3,6), T(2,9) or T(4,5) from a phase decomposition in which every phase diameter is computed by complete BFS and the skeptic reproduces each one, strictly below every upper bound for that cell published at claim time and strictly below the naive two-phase bound (the BFS diameter of solving one end column or row, plus the known value of the remaining smaller puzzle: T(2,8) = 140 for 2 x 9, T(3,5) = 84 for 3 x 6, T(4,4) = 80 or T(3,5) = 84 for 4 x 5), which the claim must also compute and report.

## How a win is checked

Check solvability parity, apply the optimal solution, and rerun the optimal solver with independently built pattern databases to confirm no shorter solution. For an exact diameter, rerun the disk-based BFS (or compare against a second implementation) and check the per-depth counts and their total.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A151944>

## Sources

- <https://oeis.org/A151944>
- <https://oeis.org/A151943>
- <https://oeis.org/A087725>
- <https://www.cs.helsinki.fi/u/bmmalone/heuristic-search-fall-2013/Korf2008.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search for hard positions (reflections of the goal, blank-far configurations) and certify them with additive pattern databases; T(2,n) antipodes for n <= 8 show a regular structure worth extrapolating.
- Korf's two-bit BFS with the blank position as the outer index keeps memory per slice small; 3 x 6 needs about 0.8 PB of bits in all, so think about symmetry and frontier search before trying.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Single-tile metric only; multi-tile metric values are different.
- The goal configuration (blank in a corner) and the orientation (3 x 6 versus 6 x 3 are the same puzzle) must match the OEIS convention.
- Kulchitsky's 3 x 4 antipode list in the OEIS file has a known error (noted in the entry).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/rectangular-sliding-puzzle-gods-numbers.md
```

Already set up? Say `run V3R1T4S on rectangular-sliding-puzzle-gods-numbers`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rectangular-sliding-puzzle-gods-numbers`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
