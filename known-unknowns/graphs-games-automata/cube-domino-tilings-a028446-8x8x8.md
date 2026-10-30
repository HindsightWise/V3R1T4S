# MOONSHOT - Domino tilings of the 8 x 8 x 8 cube: the exact count A028446(4) (6 x 6 x 6 solved in March 2026)

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (a frontier DP of width 56 is out of reach without a new idea) · open as of 2026-10-30

## The problem

A028446(n) is the number of perfect matchings (domino tilings) of the 2n x 2n x 2n grid P_2n x P_2n x P_2n; three dimensions have no Kasteleyn-type formula. Per Hakan Lundow computed a(1) = 9 and a(2) = 5051532105 (1996-1998). On 29 Mar 2026 Steven Kotlarz found a(3) = 417898687046465734392674187695263185 for the 6 x 6 x 6 cube with a broken-profile DP in Rust. He used a diagonal vertex order, a peak of C(30,14) frontier states, three primes, a reverse ordering and a GF(2) parity check, all documented in the entry. Re-fetched 2026-10-30: a(4) is open. The neighbouring sequence A049507 (P_6 x P_6 x P_n, Lundow) lists only n <= 5. The 8 x 8 x 8 cube has 512 vertices and roughly 10^88 tilings (a bulk-plus-surface fit to a(1)..a(3)). Its diagonal frontier has about 56 vertices (C(56,28) ~ 7.6e15 states). The next term therefore needs a new idea: symmetry reduction, tensor-network contraction or a cleverer decomposition. The dimer constant of Z^3 is a separate bank entry; this one asks for the exact count.

## What counts as a win

The exact integer A028446(4) (perfect matchings of P_8 x P_8 x P_8), not in the DATA when re-fetched immediately before claiming. It must come from two independent computations that agree exactly, using different decompositions and at least three primes or exact integers. The same code must reproduce a(1)..a(3) and the A028454 (P_4 x P_4 x P_n) terms.

## Partial wins

- **p1:** A049507(7) or A049507(8), the exact number of perfect matchings of P_6 x P_6 x P_7 or P_6 x P_6 x P_8, not in the A049507 DATA when re-fetched. It must come from two runs with different vertex orders that agree, with the code reproducing A049507(0..5) and A028446(1..3) (A028446(3) = A049507(6)).
- **p2:** The exact number of perfect matchings of P_6 x P_8 x P_8, under the same rules.

## How a win is checked

Skeptic: rerun the claimant's code on the 4 x 4 x 4 and 6 x 6 x 6 cubes. Check the parity of the claim against the determinant of the biadjacency matrix over GF(2), and its residue modulo a fresh prime with the claimant's code. For a(4), a cluster rerun of one prime is the minimum.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A028446>

## Sources

- <https://oeis.org/A028446>
- <https://oeis.org/A028446/a028446.md.txt>
- <https://oeis.org/A028454>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Index n gives side 2n: a(3) is the 6 x 6 x 6 cube.
- Parity and small-case checks are necessary but nowhere near sufficient; insist on independent residues.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/cube-domino-tilings-a028446-8x8x8.md
```

Already set up? Say `run V3R1T4S on cube-domino-tilings-a028446-8x8x8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cube-domino-tilings-a028446-8x8x8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
