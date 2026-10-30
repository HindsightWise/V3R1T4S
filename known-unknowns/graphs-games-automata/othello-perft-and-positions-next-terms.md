# Othello from the start: games after 22 plies (OEIS A124004) and distinct positions after 14 plies (A124005)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days for A124005 a(14) (about 2.5e10 positions, external-memory dedup); needs cluster for A124004 a(22): about 12 times the work of a(21), which took about 1000 hours on a desktop with two GTX 1080 Ti, so GPU-months even on several modern GPUs unless the method improves · open as of 2026-10-30

## The problem

A124004 counts Othello (Reversi) games from the standard start after n plies (perft). It is known to n = 21: a(21) = 4228388321175157140 (Dominic Hofer, February 2021, ReversiPerftCUDA). a(20) is Hofer's (January 2021), a(19) Hofer's (2014), a(15) to a(18) Paul Byrne's (2008); Alain Brobecker started the sequence. A124005 counts distinct positions after n plies, known to n = 13: a(13) = 3772081046 (Hofer, 2019). Checked 2026-10-30: both OEIS entries stop there, and the documentation in Hofer's repository (docs/A124004.md) lists terms only to a(21).

## What counts as a win

CONFIRMED: an exact new term A124004 a(22) or A124005 a(14), absent from OEIS and from any published source (forum posts and code repositories included) at verification time, from code that reproduces every known term of the same sequence, published with subtotals over a fixed split ply (for example one per symmetry-reduced position at ply 7) and confirmed by an independently written move generator on all subtotals or on a random 2% of them, or by a full second run.

## Partial wins

- **p1:** A124005 a(15), meeting the same validation, after or together with a(14).
- **p2:** A fully independent verification of A124004 a(21) (credited to one GPU code), with per-position subtotals over Hofer's published 10,649 symmetry-reduced ply-7 positions that sum to 4228388321175157140.

## How a win is checked

Reproduce A124004 a(0..21) and A124005 a(0..13) with the independent generator. Recompute a random 2% of claimed subtotals and check their sum and symmetry multiplicities. For distinct positions, check that positions are keyed by board plus side to move.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A124005>

## Sources

- <https://oeis.org/A124004>
- <https://oeis.org/A124005>
- <https://github.com/PanicSheep/ReversiPerftCUDA/blob/master/docs/A124004.md>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Pass and end-of-game conventions (whether a forced pass is a ply, and whether finished games are still counted at later plies) must match the OEIS definitions; reproducing all known terms is the test.
- Distinct positions must include the side to move.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/othello-perft-and-positions-next-terms.md
```

Already set up? Say `run V3R1T4S on othello-perft-and-positions-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `othello-perft-and-positions-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
