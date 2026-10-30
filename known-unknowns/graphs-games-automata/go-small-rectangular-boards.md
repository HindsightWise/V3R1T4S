# Go on small rectangular boards: an exact first-player score for a blank or ' > =6' cell of van der Werf's m x n table (3x10, 2x12, 4x8, 5x7, 6x6, ...)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days for the 24-33-point boards (2x12, 3x10, 3x11); 4x8, 5x7 and 6x6 probably need a cluster or a much stronger solver · open as of 2026-10-30

## The problem

Go solved on small boards: Erik van der Werf's program Migos solved 5x5 (October 2002, first player wins all 25 points from the centre; all openings by December 2002), and in 2008-2009 an improved Migos solved rectangular boards up to 30 intersections, checked against earlier human analyses by Ted Drange (van der Werf and Winands, 'Solving Go for Rectangular Boards', ICGA Journal 32(2), 2009). Van der Werf's table of first-player scores for m x n boards (m, n <= 12) has exact values for every board up to 30 points except two: 3x10 is given only as ' > =6' and 2x12 is blank; 3x11, 3x12, 4x8 and longer, 5x7 and longer, and 6x6 and larger are blank too. In 2024 Randall, Mueller, Wei and Hayward (Expected Work Search, IJCAI 2024) solved empty 5x5 under positional superko, the first full-board solve under that rule, and cite only the van der Werf work as prior board solutions. Wikipedia's 'Solved game' article lists 7x7 as weakly solved in 2015 from professional players' analysis (its source says the work is still under research); neither 6x6 nor 7x7 has a published computer proof. Task: determine the exact first-player score (area scoring, no komi, as in the table) for one blank or bounded cell. Status checked 2026-10-30 on van der Werf's mxngo page and in the 2024 EWS paper.

## What counts as a win

CONFIRMED: the exact first-player score with perfect play on an m x n board (m <= n) whose cell is blank or ' > =6' in van der Werf's table at verification time, and not published elsewhere. The ruleset must be stated in full and labelled: either the Migos rules of van der Werf and Winands 2009 (their formalization of the Chinese rules: area scoring, basic ko plus Migos's long-cycle rule, no superko, specified in van der Werf's 2004 thesis), or positional superko with area scoring and no komi. Proof is one of two routes. (a) Two solution trees: one for 'first player scores at least S' and one for 'second player holds the first player to at most S'. Each is accepted by a checker that shares no code with the solver, regenerates every move of the side that must answer everything, applies the stated ko/superko rule with full game history (no transposition merging that ignores history under superko), and scores terminal positions itself. (b) Agreement of two independent solvers. Each first reproduces at least five published cells of the table under the Migos rules (including 5x5 = 25, 4x7 = 28 and 5x6 = 4), then solves the claimed board under the stated ruleset.

## Partial wins

- **p1:** A new proven bound for 3x10 or 2x12 under the Migos rules: one solution tree as in route (a), accepted by an independent checker, proving either that the first player scores at least S with S > 6 on 3x10 (any S on 2x12), or that the second player holds the first player to at most S.
- **p2:** An independent recomputation, under positional superko, of at least five cells of the table with 20 or more intersections (for example 4x5, 4x6, 3x9, 2x10, 5x6), with any disagreement with the Migos (basic-ko, long-cycle-rule) values documented position by position.

## How a win is checked

Rebuild the checker or second solver, run it on the control cells and confirm the published values, then check the submitted proof trees (or rerun the second solver) on the claimed board under the stated rules. Spot-check the principal variation by hand: a final position, its area count, and the ko history used.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://erikvanderwerf.tengen.nl/mxngo.html>

## Sources

- <https://erikvanderwerf.tengen.nl/mxngo.html>
- <https://erikvanderwerf.tengen.nl/5x5/5x5solved.html>
- <https://sites.ualberta.ca/~hayward/papers/ews.pdf>
- <https://en.wikipedia.org/wiki/Solved_game>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Migos used iterative-deepening alpha-beta with static recognition of unconditionally alive blocks and territory (Benson-style) to cut the tree; EWS adds win-rate guidance to proof-number search.
- Thin boards (2 and 3 rows) are nearly one-dimensional; their values in the table show patterns (2xn: 8, 10, 12, ... then 4, 6) that suggest where to look and which first moves to try.
- For a score proof, solve 'score >= S' and 'score >= S+1' as separate win/loss problems with a threshold-aware solver.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Ruleset changes values and cost: van der Werf's results use the Migos rules (a formalization of the Chinese rules with basic ko and a long-cycle rule, no superko; the EWS paper calls them Japanese-style), and the EWS paper reports that situational superko raised Migos's 4x4 solving time from 14.8 seconds to 1.1 hours. State the rules and compare only like with like.
- The page's table is easy to misread when scraped; cells are m rows x n columns, symmetric, and ' > =6' is a bound, not a value.
- Graph-history interaction: under superko, transposition tables keyed on board alone give wrong proofs.
- Engine evaluations (KataGo) and professional analyses of 6x6 or 7x7 are not proofs.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/go-small-rectangular-boards.md
```

Already set up? Say `run V3R1T4S on go-small-rectangular-boards`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `go-small-rectangular-boards`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
