# NoGo: a position on a Go board with value 1/16 (only 1, 1/2, 1/4 and 1/8 are known)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (canonical-form search over small partly filled grids) · open as of 2026-10-30

## The problem

NoGo (also called 'Anti-Atari Go'; invented independently by Neil McKay) is played on a Go board. Players alternately place stones of their colour (Black = Left), and a placement is illegal if afterwards any group of either colour has no liberty, so nothing is ever captured; the player who cannot move loses. Burke and Hearn (Int. J. Game Theory 48, 2019) showed that NoGo is hard on graphs. McKay, Nowakowski and Angela Siegel found NoGo positions on a Go board with the values 1, 1/2, 1/4 and 1/8. Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem B12) asks whether the denominators of the numbers that occur on the two-dimensional board are bounded, and asks for the nim-dimension of the one- and two-dimensional boards. Disjoint regions walled off by stones add as a sum, so multiples of 1/8 are cheap, but 1/16 cannot arise as a sum of positions of value 1, 1/2, 1/4 or 1/8.

## What counts as a win

CONFIRMED: a legal NoGo position on an m x n rectangular grid whose canonical value, with Black as Left, is a number with denominator at least 16 (for example 1/16), computed exactly by two independent programs. Legal means stones of both colours placed so that every group has at least one liberty; any m and n are allowed. Reachability from the empty board is not required, but the claim must say whether it holds. The value must not be published at verification time (Games of No Chance volumes, arXiv, Sensei's Library AntiAtariGo page).

## Partial wins

- **p1:** A legal NoGo position on a general planar graph (NoGo on graphs, same legality rule) whose canonical value is a number with denominator at least 16, computed by two independent programs, while the grid question is still open.

## How a win is checked

Implement NoGo legality (after a placement, every maximal same-colour connected group of both colours must be adjacent to an empty point) and a canonical-form engine. Test them on small cases such as the one-dimensional position . x . . o . = +-1 quoted in GONC6 B12. Recompute the claimed position's canonical form with a second program (for example a CGSuite ruleset script) and compare.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Sources

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>
- <https://senseis.xmp.net/?AntiAtariGo>
- <https://library.slmath.org/books/Book70/files/1005.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Number values arise when one player has a reservoir of safe moves the other lacks. Look for corridor-shaped empty regions bordered by stones whose options are 0 and 1/8, which gives {0 | 1/8} = 1/16.
- Search systematically over small empty regions (up to about 14 empty points) inside a frame of stones, caching canonical forms by region shape and boundary colours.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The one-dimensional nimber question is not part of this target. GONC6 states that the strips x . o . x . o ... are equivalent to the octal game .6 (Officers), whose values reach 16 at heap 381 and 256 at heap 10,344 (Flammenkamp), so large nimbers there follow from the octal game.
- Capture never happens in NoGo, so a Go engine's legality code is wrong for it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/nogo-fraction-one-sixteenth.md
```

Already set up? Say `run V3R1T4S on nogo-fraction-one-sixteenth`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nogo-fraction-one-sixteenth`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
