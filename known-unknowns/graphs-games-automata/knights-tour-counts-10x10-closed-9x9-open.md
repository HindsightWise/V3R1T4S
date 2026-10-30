# Knight's tour enumeration: the number of closed tours on the 10 x 10 board (A001230(5)) or open tours on the 9 x 9 board (A165134(9))

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster (frontier/transfer-matrix over two-column knight frontiers with path-connectivity states; the 9 x 10 closed partial is laptop-days to cluster) · open as of 2026-10-30

## The problem

Closed tours on 8 x 8: 13,267,364,410,532 undirected. Loebbing and Wegener (1996) used BDDs, and Brendan McKay corrected their value (1997). Open tours (directed Hamiltonian paths) on 8 x 8: 19,591,828,170,979,904 (Alex Chernov, 2014, A165134). Frontier methods have since moved on narrow boards. Donald Knuth extended closed tours on 8 x n to n = 32 (A193055 b-file, 2025). Closed tours on 9 x 2n for n <= 4 come from Knuth's Prefascicle 8a and his Christmas lecture 'Adventures with Knight's Tours' (Dec 2025), entered as A391999 by Peter Luschny: 9 x 6 = 3,374,967,940 and 9 x 8 = 7,112,881,119,092,574. Luschny counted undirected Hamiltonian paths on 9 x n up to n = 8 (A391009, Dec 2025). The square boards beyond 8 x 8 remain open. OEIS checked live 2026-10-30: A001230 stops at 8 x 8, A165134 at 8 x 8, A391999 at 9 x 8 and A391009 at 9 x 8, with no pending drafts.

## What counts as a win

Success means the exact number of undirected closed knight's tours on the 10 x 10 board (A001230(5)), or of directed Hamiltonian paths in the 9 x 9 knight graph (A165134(9), which is 2 x A391009(9)). It must be computed by two independent runs (different program or decomposition, and different moduli or exact arithmetic) that agree exactly. The code must reproduce A001230(4), A165134(8), and all published terms of A193055 (8 x n) or A391009 (9 x n) for the widths it supports. The live OEIS entries, re-fetched before claiming, must still lack the value.

## Partial wins

- **p1:** A391999(5): the number of undirected closed knight's tours on the 9 x 10 board, two runs agreeing, with the code reproducing A391999(3), A391999(4) and the A193055 terms for 8 x n, n <= 20.
- **p2:** A193055(33): the number of closed knight's tours on the 8 x 33 board (Knuth's b-file ends at 32), two runs agreeing, with the code reproducing every A193055 term.

## How a win is checked

Skeptic: rerun the claimant's frontier program on the published boards (8 x 8 closed, 8 x 8 open, 9 x 8 closed) and compare; rerun the claimed board modulo one fresh prime; for a 10 x 10 claim also check divisibility by the 8 board symmetries' orbit structure (count of tours fixed by each symmetry computed separately must make the Burnside quotient an integer).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A001230>

## Sources

- <https://oeis.org/A001230>
- <https://oeis.org/A165134>
- <https://oeis.org/A391999>
- <https://oeis.org/A391009>
- <https://oeis.org/A193055>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Directed vs undirected and open vs closed conventions differ across these sequences (A165134 counts directed paths; A391009 undirected; A001230 undirected cycles). Factor-2 errors are common.
- Loebbing and Wegener's first 8 x 8 figure was wrong; reproduce McKay's value before trusting any new code.
- Knuth's December 2025 lecture may contain values not yet in OEIS; check the lecture materials and any 2026 OEIS additions before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/knights-tour-counts-10x10-closed-9x9-open.md
```

Already set up? Say `run V3R1T4S on knights-tour-counts-10x10-closed-9x9-open`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knights-tour-counts-10x10-closed-9x9-open`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
