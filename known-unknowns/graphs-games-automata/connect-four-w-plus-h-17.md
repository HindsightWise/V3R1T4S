# Connect Four on a board with width + height = 17 (9x8, 10x7, 11x6, 12x5, 13x4): the first unsolved sizes

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (Steininger reports 7x9 took about 16 hours on his machine; for w + h >= 17 he uses 64-bit table entries and recommends 32 GB or more of memory); 9x8 and 10x7 may need weeks or a large-memory server · open as of 2026-10-30

## The problem

Connect Four on a board w columns wide and h rows high (stones drop to the lowest free cell; four in a row horizontally, vertically or diagonally wins; a full board is a draw). James D. Allen and Victor Allis solved the 7x6 game in October 1988. John Tromp solved every size with w + h <= 15 (2006) and 8x8 (late 2015, second-player win). Christophe Steininger's solver (github.com/ChristopheSteininger/c4) solved every size with w + h = 16 and some larger ones. His README tables (width x height) give outcomes and last-move numbers for widths 4-12 and heights 4-13, reaching 12x4, 11x5, 10x6, 9x7, 8x8, 8x9, 7x10, 6x11, 6x12, 5x13 and 4x13; every board 4 or 5 columns wide up to height 13 is a draw. Wikipedia's 'Solved game' article credits him with all w + h = 16 boards (May 22, 2024). Of the w + h = 17 boards, 4x13, 5x12, 6x11, 7x10 and 8x9 are solved. 9x8, 10x7, 11x6 and 12x5 are blank in his table, and 13x4 lies outside it (the table stops at width 12); 9x9, 8x10, 7x11, 7x12 and 6x13 are blank too. In issue #2 on his repository (opened May 2025) a user asked about 9x8. Steininger replied (29 May 2025) with the settings he uses for w + h >= 17 boards: 64-bit table entries, WORK_BITS = 0, and a Chinese-remainder trick to store positions exactly. He asked to see the 9x8 book if it was produced; no result was reported there. Task: determine the perfect-play outcome (first-player win, draw, or second-player win) of one of these sizes. Status checked 2026-10-30 on the repository README and issue #2.

## What counts as a win

CONFIRMED: the perfect-play outcome of Connect Four from the empty board for one board size (width x height) with width + height >= 17 and both dimensions >= 4. The outcome must not be given in the results table of github.com/ChristopheSteininger/c4 at verification time (a blank cell, or a size outside the table such as 13x4), nor in Tromp's table or any other published source. It is established by two independent computations that agree: (1) the submitter's solver run, with its source, settings and log published, and (2) a second solver that shares no search or transposition-table code with the first (for example Steininger's c4 with WORK_BITS = 0 and a 64-bit entry as he recommends, Pascal Pons' solver, or Tromp's Fhourstones, adapted to the board size). Each solver must first reproduce at least three published neighbouring results from Steininger's table (for example 12x4, 11x5 and 8x8) and the published last-move numbers for them. A result does not count if it depends on a transposition table with unverified hash collisions (fewer bits stored than the position needs, without a Chinese-remainder or equivalent exact-recovery scheme).

## Partial wins

- **p1:** An independent confirmation of one of Steininger's w + h = 17 results (4x13, 5x12, 6x11, 7x10 or 8x9, width x height), so far computed only by his solver, by a solver sharing no search or transposition-table code with his, with the same outcome and last-move number.
- **p2:** An independent confirmation of a w + h = 16 result from Steininger's table that Tromp never computed (for example 9x7, 10x6 or 7x9), by a solver sharing no code with Steininger's, with the same outcome and last-move number.

## How a win is checked

Build both solvers from published source; run each on the claimed size and on the three control sizes; compare outcomes and last-move numbers. Check that the transposition-table entry stores enough bits to recover the position exactly (or that collisions are detected), and that multithreaded writes are atomic. Optionally replay the principal variation in a third, trivial move generator to confirm the claimed game end.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/ChristopheSteininger/c4>

## Sources

- <https://github.com/ChristopheSteininger/c4>
- <https://github.com/ChristopheSteininger/c4/issues/2>
- <https://tromp.github.io/c4/c4.html>
- <https://en.wikipedia.org/wiki/Solved_game>
- <https://github.com/tromp/fhourstones88>
- <https://github.com/PascalPons/connect4>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Narrow-tall and wide-short boards are cheapest: 13x4 has 52 cells, and the height-4 row of the table is all second-player wins from width 8 on, a pattern to test first.
- Steininger's issue #2 reply explains the settings he uses for w + h >= 17 (64-bit entries, WORK_BITS = 0, a larger NUM_TABLE_ENTRIES) and the Chinese-remainder trick for storing positions exactly.
- An opening book of all positions to depth d, each solved and stored, doubles as a checkable certificate: a second solver can re-solve a random sample of book positions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Width x height order: Steininger's and Tromp's tables put width across and height down; 9x8 means 9 columns and 8 rows.
- Tromp's own table is older and stops at w + h = 15 plus 8x8; do not mistake its blanks for open cells.
- Bit-packing 81 cells (9x8) into a 64-bit entry is only exact with the Chinese-remainder scheme; naive hashing silently corrupts results.
- Steininger's 128-bit-entry workaround is unsafe with multiple threads (his own warning in issue #2).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/connect-four-w-plus-h-17.md
```

Already set up? Say `run V3R1T4S on connect-four-w-plus-h-17`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `connect-four-w-plus-h-17`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
