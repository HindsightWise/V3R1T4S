# Sokoban maximum moves: a board with n floor squares and k boxes whose shortest solution beats the DeStefano-qqwref archive

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Which Sokoban levels with n floor squares (spaces) have the longest shortest solution, measured in player steps? Erich Friedman posed the problem (Problem of the Month, March 2000); Brendan Owen, Philippe Fondanaiche, Trevor Green, John Hoffman and others contributed. Zachary DeStefano and qqwref maintain the Sokoban Max Moves Archive (re-fetched 2026-10-30), a table of best-known move counts for 3 to 32 spaces and 1 to 8 boxes, with proven column maxima in bold and best guesses in italics, and they invite new results. OEIS A195667 (longest game with n spaces, any number of boxes) lists exact values for n = 3..20, ending a(20) = 146 (a(18)-a(20) by DeStefano, 2021); A195668 is the 1-box case. Most archive cells beyond about 20 spaces are best-known values, not proven maxima, so better boards are expected.

## What counts as a win

A Sokoban level (walls, floor squares, player, boxes, goals; standard rules: the player pushes one box at a time and cannot pull) with exactly n floor squares and k boxes, for a cell (n, k) that the live archive shows in italics (a best guess) at claim time. Its minimum number of player steps to solve, certified by a complete BFS over the level's state space, must be strictly greater than the archive's value for that cell. Cells shown in bold (proven column maxima) or in plain type (computed values) are settled and do not count. Alternatively, an exact column maximum not yet listed (A195667(21) or later), certified by an exhaustive enumeration of all boards with that many spaces that a skeptic can rerun, and not already listed in OEIS or marked proven on the archive.

## Partial wins

- **p1:** Each further italic archive cell (n, k) beaten in the same way counts as one more partial win.
- **p2:** A proof by exhaustive search that an italic (best-guess) archive value is optimal for its cell, with released enumeration code.

## How a win is checked

Parse the level in standard .sok format, count floor squares and boxes, and run an independent BFS over (player region, box set) states to compute the exact minimum number of steps; compare with the archive's value for that cell. For exhaustive claims, rerun the released enumeration of polyomino boards with that number of spaces.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://sokoban-max-moves.herokuapp.com/>

## Sources

- <https://sokoban-max-moves.herokuapp.com/>
- <https://oeis.org/A195667>
- <https://oeis.org/A195668>
- <https://erich-friedman.github.io/mathmagic/0300.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The archive lists proved structural facts (maximal boards have at least two cycles, no bent arms); use them to prune a search over polyomino shapes, then optimize box and goal placement with exact BFS.
- Hill-climb over board shapes with an exact BFS evaluator; small boards make each evaluation fast.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The archive counts player steps (moves), not pushes; Friedman's page also discusses pushes separately.
- Spaces means all non-wall squares, including those under the player, boxes and goals.
- The archive's rows start at different space counts; align columns carefully before comparing values.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/sokoban-max-moves-small-boards.md
```

Already set up? Say `run V3R1T4S on sokoban-max-moves-small-boards`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sokoban-max-moves-small-boards`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
