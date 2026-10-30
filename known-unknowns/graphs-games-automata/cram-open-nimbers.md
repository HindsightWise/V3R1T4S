# Cram: compute a missing nimber in Beling's normal-play table (5x13, 6x11, 7x10, ...) or a missing misère value (5x8, 5x9, 6x7, 6x8, 6x9)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (Beling reports that for most boards in his table, for example 13x4, his solver needed no more than a few minutes; the open cells are the next sizes up and may take far longer) · open as of 2026-10-30

## The problem

Cram is the impartial version of Domineering: players alternately place a domino in either orientation on an m x n grid. Under normal play the player who cannot move loses; under misère play that player wins. Even x even boards are second-player wins and even x odd boards first-player wins by symmetry, so the open questions are nimbers (Grundy values) and misère values. Normal play: Martin Schneider (2009) computed boards up to 3x9, 4x5 and 5x7. Julien Lemoine and Simon Viennot's Glop (2010-2013) reached 3x20, 4x9, 5x9, 6x7 and 7x7. Jos Uiterwijk (ACG 2019) showed 11x5 has nimber 0. Piotr Beling's Rust solver igsolve (github.com/beling/impartial-games) extended the table to 7x9, 8x7, 9x6, 10x5, 11x4, 12x5 and 15x4 (13x4 first computed by Thomas Plick). Beling's table (heights 4-7, widths 4-15) still shows '?' for 13x5, 14x5, 15x5, 11x6, 13x6, 15x6 and 7x10 through 7x15. Misère play: Schneider and Glop reached 3x15, 4x9, 5x7 and 6x6 (2009-2011). Wikipedia's Cram article lists the misère values of 5x8, 5x9, 6x7, 6x8 and 6x9 as '?', and Beling's README says misère support is only planned. Task: compute one missing value. Status checked 2026-10-30 on Beling's README, the Glop records page and the Wikipedia article.

## What counts as a win

CONFIRMED: for a board shown as '?' in Beling's normal-play table or in Wikipedia's misère Cram table at verification time (and not published elsewhere), its exact normal-play nimber or misère Grundy value (Conway's definition: the unique n such that G + *n is a misère second-player win), computed by two independent programs that agree, where each program first reproduces at least five published neighbouring values from the same table (for example 7x9 = 1, 9x6 = 1, 12x5 = 3 for normal play; 5x7 = 1, 6x6 = 1, 4x9 = 1 for misère). For normal play one program may be Beling's igsolve if the other shares no code with it. Each run publishes its source, its command line and the number of positions stored.

## Partial wins

- **p1:** The normal-play outcome only (zero or non-zero nimber) of an odd x odd '?' board (5x13, 5x15, 7x11, 7x13 or 7x15), confirmed by two independent programs as in the success criterion.
- **p2:** An extension of a published three-row sequence by at least two new terms: normal-play nimbers of 3xn beyond n = 20, or misère values of 3xn beyond n = 15 (conjectured period 3). Each new term must be confirmed by two independent programs, and none may be given at verification time on the Glop records page, Wikipedia's Cram article, Beling's README or any OEIS entry.

## How a win is checked

Build both programs; reproduce the control cells; run both on the claimed board and compare values. For a normal-play nimber v, a third check is cheap to state: G + *v must be a second-player win and G + *u a first-player win for every u < v. For misère, confirm that the definition used is Conway's misère Grundy value, not the normal nimber of the misère game.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/beling/impartial-games>

## Sources

- <https://github.com/beling/impartial-games>
- <https://en.wikipedia.org/wiki/Cram_(game)>
- <http://sprouts.tuxfamily.org/wiki/doku.php?id=records>
- <https://arxiv.org/abs/1011.5841>
- <https://doi.org/10.1016/j.artint.2020.103262>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Beling and Rogalski's pruning (Artificial Intelligence 283, 2020) and Lemoine-Viennot's component splitting with nimber databases are the state of the art for normal play; both rely on Sprague-Grundy sums that are invalid in misère play.
- For misère, Glop's reduced canonical trees (from its Sprouts work) are the known sound decomposition; a fresh misère solver for Cram is the gap Beling's README names as planned.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Normal and misère values must never be mixed; nimber addition does not hold in misère play.
- Width x height symmetry: an m x n board equals n x m; check both spellings before calling a cell open.
- Even x even and even x odd outcomes are known by symmetry; only the nimber (or misère value) is open there.
- The Glop records page lists Cram values only up to 2013 and has no '?' cells; Beling's README and Wikipedia's tables are the places that mark open cells.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/cram-open-nimbers.md
```

Already set up? Say `run V3R1T4S on cram-open-nimbers`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cram-open-nimbers`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
