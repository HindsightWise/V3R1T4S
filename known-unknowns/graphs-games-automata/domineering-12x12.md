# Domineering on the 12x12 board (largest solved square board is 11x11, Uiterwijk 2016)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (each square board from 8x8 to 11x11 was a new record solve; 12x12 has 144 cells and a far larger tree); a named-move refutation (partial win p2) may fit laptop-days · open as of 2026-10-30

## The problem

Domineering (Stop-Gate, Crosscram): two players alternately place dominoes on a grid, one player vertically and the other horizontally; the player unable to move loses. On square boards the two roles are symmetric, so the question is whether the first or second player wins. Solved: 8x8 by Breuker, Uiterwijk and van den Herik (2000), 9x9 soon after, 10x10 by Nathan Bullock (MSc thesis, 2002, using combinatorial-game-theory evaluation of regions), 11x11 by Jos Uiterwijk ('11x11 Domineering Is Solved: The First Player Wins', Computers and Games 2016). Wikipedia's Domineering article (edited October 2025) states that the game is a first-player win on 2x2, 3x3, 4x4 and 6x6-11x11, a second-player win on 1x1 and 5x5, and lists no larger square board. Task: determine the outcome of 12x12 Domineering. Status checked 2026-10-30 on the Wikipedia article; Bullock's table of rectangular values (webdocs.cs.ualberta.ca/~games/domineering/updated.html, cited there) now redirects to a University of Alberta directory page and was not readable.

## What counts as a win

CONFIRMED: the outcome (first-player win or second-player win) of Domineering on the empty 12x12 board, while it is not reported solved on Wikipedia's Domineering article or in the literature at verification time, shown by a solution tree for the winning side (one named move at that side's nodes, every legal move of the opponent at the other side's nodes) whose leaves are either terminal positions or positions decided by a cited, proven rule (for example safe-move counting or a combinatorial-game value of independent regions computed by the checker itself), accepted by a checker that shares no code with the solver. Alternatively, agreement of two independent solvers that each first reproduce the published outcomes for 8x8, 9x9 and 10x10.

## Partial wins

- **p1:** An independent confirmation of the 11x11 first-player win (Uiterwijk 2016) by a solver or checker that shares no code with Uiterwijk's, with the winning first move and the solution tree or a second-solver agreement as in the success criterion.
- **p2:** A proof, certified as in the success criterion, that one named first move on the empty 12x12 board loses (the opponent then has a winning strategy).

## How a win is checked

Check leaves with an independent implementation: recompute region decompositions and their combinatorial-game values (or safe-move counts) from scratch, regenerate all opponent moves at every AND node, and verify that the root is the empty 12x12 board with the stated player to move. Run the control boards first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Domineering>

## Sources

- <https://en.wikipedia.org/wiki/Domineering>
- <https://doi.org/10.1007/978-3-319-50935-8_12>
- <https://doi.org/10.1016/S0304-3975(99)00082-1>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Bullock's solver split the board into independent regions once dominoes partition it and used precomputed combinatorial-game values for small regions; Uiterwijk's 11x11 run relied on safe-move counting and knowledge-based move ordering.
- Partial results on 12xn and nx12 rectangles (one side moving first) are natural stepping stones and give move ordering for 12x12.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Which player moves first matters on rectangles but not on squares; on rectangles state who places vertical dominoes and who moves first.
- Bullock's rectangular-board table is offline at its old address; do not assume a rectangle is open or solved without another source.
- Safe-move counting rules have conditions; a leaf decided by a misapplied rule invalidates the tree.
- The Springer page of Uiterwijk's 2016 paper sits behind a login redirect; read the status from Wikipedia and confirm in the ICGA/CG literature before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/domineering-12x12.md
```

Already set up? Say `run V3R1T4S on domineering-12x12`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `domineering-12x12`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
