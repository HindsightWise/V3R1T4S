# Linear trimer (I-tromino) tilings of the 3n x 3n square: the next term A139772(8), the 24 x 24 board

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (a 3^24 broken-profile state space, about 2.8e11 states) unless a better method is found · open as of 2026-10-30

## The problem

A139772(n) counts tilings of the 3n x 3n square by 1 x 3 and 3 x 1 trominoes, i.e. rigid linear trimers at close packing, whose residual entropy Van Craen studied (J. Chem. Phys. 1975). Steven Finch entered it in 2008, and Andrew Howroyd added a(6)-a(7) in Feb 2022: a(7) = 11281654633785546173131745084 for the 21 x 21 board. In Apr 2026 Nicolas Belohoubek added the bound a(n) <= 162^(n^2) and a conjectured asymptotic. Re-fetched 2026-10-30: 7 terms, keyword 'more'. The natural column transfer matrix has 3^(3n) profile states: about 1e10 at width 21 and 2.8e11 at width 24.

## What counts as a win

The exact integer A139772(8) (linear trimer tilings of the 24 x 24 square), not in the DATA when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, using different primes and a different decomposition. The same code must reproduce a(1)..a(7).

## Partial wins

- **p1:** The exact count of linear trimer tilings of the 21 x 24 rectangle (width 21, the largest width already handled), with the code reproducing A139772(1..7), under the same two-run rule.

## How a win is checked

Skeptic: check the code against a(1)..a(5) (minutes), then recompute one residue of a(8) modulo a fresh prime with the claimant's code, or recompute a sample of transfer-matrix columns.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A139772>

## Sources

- <https://oeis.org/A139772>
- <https://doi.org/10.1063/1.431651>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Meeting in the middle across the central column (sum over profiles of left count times right count) halves the sweep but not the state space; the reflection symmetry of the profile halves memory.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A Monte Carlo or asymptotic estimate is not a term.
- Index n gives the 3n x 3n board: a(7) is 21 x 21.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/linear-trimer-coverings-a139772-24x24.md
```

Already set up? Say `run V3R1T4S on linear-trimer-coverings-a139772-24x24`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `linear-trimer-coverings-a139772-24x24`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
