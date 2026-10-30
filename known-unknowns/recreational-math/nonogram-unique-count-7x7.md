# Uniquely solvable nonograms: count the 7 x 7 case (OEIS A242876 a(7)) or a new n x m cell beyond n*m = 44 (A384764)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (7 x 7 is 2^49 grids, 32 times the largest size done; the n*m = 45..48 cells are laptop-hours to laptop-days) · open as of 2026-10-30

## The problem

A nonogram's clues are the run lengths of filled cells in each row and column. A242876(n) counts the n x n binary grids that are the unique solution of their clues: 1, 2, 14, 384, 52362, 25309575, 49745060669 for n = 0..6 (Charles R Greathouse IV and Sophia Greathouse 2014; a(5) Mark E. Shoulson 2014; a(6) = 49745060669 by Bertram Felgenhauer, June 2025, correcting the value 49866168063 entered by Karl W. Heuer in January 2015). Batenburg and Kosters (ICGA J. 2012) gave the erroneous 49745060370, 299 below Felgenhauer's value; a parity argument by olligobber (May 2026, cited in the OEIS history) shows a(6) is odd. Felgenhauer's 'Counting Nonograms' page and OEIS A384764 (b-file to antidiagonal n+m = 13) give n x m counts up to n*m = 44 (June 2025): m = 3 to n = 14, m = 4 to n = 11, m = 5 to n = 8, m = 6 to n = 7. The 7 x 7 value and the cells 3x15, 5x9 (n*m = 45), 4x12, 3x16 and 6x8 (48) are unknown. Related: A391619 (line-solvable grids, Andrei Zabolotskii 2026, with olligobber's LocalNonogram, whose README estimates over 12 years for 7 x 7 with that code) and the yesnogram counts A385861/A385862 (Karl W. Heuer 2025, from Felgenhauer's table). We reproduced the 2x2, 3x3, 4x4, 2x6 and 3x5 counts with our own brute force. Target: A242876 a(7).

## What counts as a win

Success means the exact value of A242876 a(7): the number of 7 x 7 binary grids whose (row clues, column clues) pair is shared by no other 7 x 7 grid. It must be computed by two independently written programs (different algorithms or languages) that agree, and both must reproduce every entry of Felgenhauer's table with n*m <= 42. The value must not appear in A242876 DATA, its history page (https://oeis.org/history?seq=A242876, including pending drafts) or https://int-e.eu/nono/, all re-fetched live immediately before claiming. No OEIS submission is part of the win.

## Partial wins

- **p1:** A new A384764 cell with n*m >= 45 and min(n, m) >= 3 (e.g. 5x9, 3x15, 4x12 or 6x8). It must be absent from the live int-e.eu/nono table, the A384764 b-file and A383345, and computed by two independent programs that reproduce the n*m <= 42 table.
- **p2:** A391619 a(7): the number of 7 x 7 nonograms solvable by iterated single-line reasoning, by two independent programs that reproduce a(0..6).
- **p3:** A new yesnogram count (A385861 a(7), or an A385862 cell with n*m >= 45 and min(n, m) >= 3) by two independent programs that reproduce Felgenhauer's yesnogram table.

## How a win is checked

Rerun both programs. Check the n x m vs m x n symmetry. Check the parity of the result against olligobber's parity argument where it applies. Check the partial sums by column-signature class. Brute force verifies the small cases in seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://int-e.eu/nono/>

## Sources

- <https://oeis.org/A242876>
- <https://oeis.org/A384764>
- <https://oeis.org/A391619>
- <https://int-e.eu/nono/>
- <https://doi.org/10.3233/ICG-2012-35402>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Felgenhauer's method groups grids by column signature (F(n+2) classes per column) so only row signatures are stored per class. 7 x 7 needs chunked parallel enumeration with on-disk sorting or hashing per class.
- A transfer-matrix or meet-in-the-middle count over row signatures, using the reflection and transposition symmetries to cut the work by up to 8.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The count is of grids with a unique clue signature (equivalently clue sets with exactly one solution), not of all clue sets.
- Empty rows have the empty clue; mishandling them changes every count.
- The 2012 Batenburg-Kosters 6 x 6 value is wrong; validate against Felgenhauer's table, not the paper.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/nonogram-unique-count-7x7.md
```

Already set up? Say `run V3R1T4S on nonogram-unique-count-7x7`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nonogram-unique-count-7x7`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
