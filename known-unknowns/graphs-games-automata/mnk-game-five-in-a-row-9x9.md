# m,n,k-games: settle five-in-a-row (k = 5) on 9x9 or another board between 8x8 (draw) and 15x15 (win)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (8x8 needed a dedicated research solve in 2018 by Hsu, Ko, Hsueh and Wu; 9x9 has 81 cells); a narrow board such as (9,5,5) or (9,6,5) may fall in laptop-days · open as of 2026-10-30

## The problem

In the m,n,k-game two players alternately place stones on an m x n board, and the first to get k in a row (horizontally, vertically or diagonally) wins. No rules restrict moves (free-style, overlines count). Strategy stealing shows the first player never loses. For k = 5: Wei-Yuan Hsu, Chu-Ling Ko, Chu-Hsuan Hsueh and I-Chen Wu proved (7,7,5) and (8,8,5) draws (ICGA Journal 40(3), 2018), so every board with both sides at most 8 is a draw. L. Victor Allis proved (15,15,5) a first-player win (free-style gomoku, 1994). Nothing is listed in between. Wikipedia's m,n,k-game article was last edited in October 2026; its k = 4 results were updated in November 2025 with Christian Vogt's 2025 report that (6,5,4) is a win. It gives no result for any k = 5 board with a side from 9 to 14. Task: settle (9,9,5), or another unlisted k = 5 board with both sides at least 5 and at least one side from 9 to 14. Status checked 2026-10-30 on the Wikipedia article.

## What counts as a win

CONFIRMED: the outcome (first-player win or draw) of the free-style (m,n,5)-game for (m,n) = (9,9), not settled on Wikipedia's m,n,k-game article or in the literature at verification time, shown by a solution tree accepted by a checker that shares no code with the solver. For a first-player win: one named first-player move at each first-player node, every legal second-player reply at the others, and every leaf a completed five. For a draw: one named second-player reply at each second-player node and every legal first-player move at the others, every leaf a full board or a position where the checker itself proves no line of five remains completable by the first player; threat-space or relevance-zone pruning is allowed only if the checker re-derives each pruning step from its stated rule.

## Partial wins

- **p1:** The outcome of another free-style (m,n,5) board with 5 <= m <= n <= 14 and n >= 9 (for example (9,8,5), (9,6,5) or (10,10,5)), not settled on the Wikipedia article or in the literature at verification time, certified as in the success criterion.
- **p2:** An independent re-verification of the (8,8,5) draw by a solver and checker sharing no code with Hsu et al., with a checkable second-player strategy tree.

## How a win is checked

Run the independent checker on the tree: regenerate every move of the side that must answer everything, verify every claimed five or 'dead board' leaf by brute force over all lines, and re-derive each pruning step. Sanity-check the checker on small solved cases ((5,5,4) draw, (6,5,4) win, (9,4,4) win).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/M,n,k-game>

## Sources

- <https://en.wikipedia.org/wiki/M,n,k-game>
- <https://content.iospress.com/articles/icga-journal/icg180061>
- <https://ieee-cog.org/2019/papers/paper_115.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Threat-space search and dependency-based search (Allis) find first-player wins quickly when they exist; a draw proof instead needs second-player blocking strategies, where pairing strategies on part of the board and relevance zones shrink the tree.
- Narrow boards (m = 5 or 6, n large) behave almost one-dimensionally and may be cheapest; check first that they are not already settled in the 4-in-a-row and 5-in-a-row literature (Uiterwijk).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Free-style rules only: gomoku's exactly-five rule, renju restrictions or swap openings define different games.
- Wikipedia's silence on a board is not proof it is open; search the ICGA Journal and Computers and Games proceedings before claiming.
- k = 6 and k = 7 on the infinite board are famous open questions, but no finite certificate settles them; they are out of scope here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/mnk-game-five-in-a-row-9x9.md
```

Already set up? Say `run V3R1T4S on mnk-game-five-in-a-row-9x9`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mnk-game-five-in-a-row-9x9`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
