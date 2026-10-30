# Diagonal Latin squares (Vatutin's proving lists): fewer transversals, fewer or more diagonal transversals, or fewer intercalates than the best known for n = 10..28

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-minutes to laptop-hours · open as of 2026-10-30

## The problem

A diagonal Latin square (DLS) has both main diagonals as transversals. A diagonal transversal is a transversal with exactly one cell on each main diagonal. Eduard I. Vatutin, with the Gerasim@Home/RakeSearch volunteers Natalia Makarova, Tomas Brada and Harry White, keeps proving lists of best-known DLS in OEIS. Live bounds on 2026-10-30, taking the better of each entry's comment and its best-known-examples file: min transversals in a DLS (A287645; file a287645_21.txt): n=10 <= 128, 11 <= 778, 12 <= 192, 13 <= 26132, 14 <= 2224, 15 <= 170369, 16 <= 7465984 (the comment, updated 18 Sep 2026, still gives 40806 and 25720 for n = 13 and 14). Min diagonal transversals (A287647): 10 <= 3, 11 <= 43, 13 <= 4756, 14 <= 1446, 15 <= 15510, 16 <= 898988, 17 <= 12058840, 18 <= 82577875, 19 <= 592174879, 20 <= 4488686380 (n = 12 is exactly 0). Max diagonal transversals (A287648): 10 >= 890, 11 >= 4828, 12 >= 30192, 13 >= 131106, 14 >= 490218, 15 >= 4620434, 16 >= 32172800, 17 >= 204995269, 18 >= 281593874, 19 >= 11254190082, 20 >= 90010806304, 21 >= 51162162017, 22 >= 3227747329246. Min transversals in an orthogonal DLS (A357514): 10 <= 652, 11 <= 2091, 12 <= 6240, 13 <= 80380 (the last only in a357514_1.txt). Min intercalates in a DLS (A307163): 16 <= 2, 18 <= 9, 21 <= 11, 22 <= 9, 24 <= 2, 26 <= 29, 27 <= 35, 28 <= 33. Every listed bound is open except the exact cells: A287647(12) = 0, and the A307163 cells already equal to 0 (n = 10..15, 17, 19, 20, 23, 25).

## What counts as a win

Success means an explicit diagonal Latin square (for A357514, a DLS together with an orthogonal DLS mate) of order n that STRICTLY improves one listed cell in the right direction: fewer for A287645, A287647, A357514 and A307163, more for A287648. The comparison is against the better of the live OEIS comment and the headers of its 'best known examples' file, re-fetched immediately before claiming. The relevant count must agree between two independent programs. Cells with exact known values (such as A287647(12) = 0, or A307163 at orders where it is 0) cannot be improved and do not count.

## Partial wins

- **p1:** An independent recount that fails to reproduce a count in one of Vatutin's proving lists (an error in the table), with both programs and the square.

## How a win is checked

Check the square is Latin and that both diagonals contain n distinct symbols; for A357514 also check that the mate is a DLS and is orthogonal (all n^2 pairs distinct). Count transversals, diagonal transversals (with exactly one cell on the main diagonal and exactly one on the antidiagonal; for odd n the centre cell can serve as both) or intercalates with two independent programs, and compare with the live entry.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A287645>

## Sources

- <https://oeis.org/A287645>
- <https://oeis.org/A287647>
- <https://oeis.org/A287648>
- <https://oeis.org/A357514>
- <https://oeis.org/A307163>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Many records are found by 'diagonalising' (Vatutin et al., RuSCDays 2023) good Latin squares from the general tables: permute rows and columns of a square with few or many transversals until both diagonals are transversals.
- Use the cheap counters (intercalates, diagonal transversals) as a fast filter in local search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The diagonal-transversal definition is strict: exactly one cell on each main diagonal (a transversal through the centre of an odd square meets both at once).
- Maximum transversals in DLS (A287644) coincide with the general table; that cell belongs to latin-max-transversals-n10-20.
- A091323 (general odd-order minimum) is a lower bound for A287645 at odd n; a DLS beating A091323 also wins latin-min-transversals-odd-orders.
- OEIS comments lag the examples files: on 2026-10-30, a287645_21.txt had 26132 (n = 13) and 2224 (n = 14) against the comment's 40806 and 25720, and a357514_1.txt had an n = 13 bound that the comment lacks. Always read the file headers too.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/diagonal-latin-square-spectra-vatutin.md
```

Already set up? Say `run V3R1T4S on diagonal-latin-square-spectra-vatutin`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `diagonal-latin-square-spectra-vatutin`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
