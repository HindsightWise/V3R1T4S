# Fault-free domino tilings of the 2n x 2n square: the next term A124997(13) (the 26 x 26 board), open since 2016

🕸️ **Graphs, games and automata** · standard · tractability ★★★★☆ · compute: laptop-hours to laptop-days (transfer matrices with inclusion-exclusion over fault lines) · open as of 2026-10-30

## The problem

A domino tiling is fault-free if every grid line through the interior of the rectangle cuts some domino (Graham's fault-free tilings). A124997(n), entered by Don Knuth in 2008, counts fault-free domino tilings of the 2n x 2n square, starting 0,0,0,25506 (the 8 x 8 board). Alois P. Heinz added a(7) in 2015, and Xu Mingkuan added a(8)-a(11) and a b-file to n = 12 (24 x 24) in Dec 2016. All domino tilings of the square are given by Kasteleyn's product formula (A004003), but the fault-free subclass has no formula. Re-fetched 2026-10-30: the b-file ends at a(12).

## What counts as a win

The exact integer A124997(13) (fault-free domino tilings of the 26 x 26 square), not in the b-file when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, for example inclusion-exclusion over fault sets vs a direct transfer matrix tracking unbroken lines. The same code must reproduce a(1)..a(12).

## Partial wins

- **p1:** A124997(14) after a(13), under the same two-run rule.
- **p2:** The exact number of fault-free domino tilings of the 24 x 26 rectangle, from two independent runs that agree, with the code reproducing a(1)..a(12).

## How a win is checked

Skeptic: brute-force the 8 x 8 and 10 x 10 boards (25506 and 1759280998), rerun the claimant's code for n = 13 modulo a fresh prime, and check that a(13) < A004003(13).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A124997/b124997.txt>

## Sources

- <https://oeis.org/A124997>
- <https://oeis.org/A004003>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- In a column transfer matrix, track which horizontal lines are still unbroken, and handle vertical faults by inclusion-exclusion over the columns where every row ends.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Offset 1 with board side 2n: a(12) is 24 x 24, and the target is 26 x 26.
- Both horizontal and vertical faults must be excluded.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/fault-free-domino-tilings-a124997-n13.md
```

Already set up? Say `run V3R1T4S on fault-free-domino-tilings-a124997-n13`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fault-free-domino-tilings-a124997-n13`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
