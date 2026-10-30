# Counting n x n Life configurations: still lifes in the 16 x 16 square (A136278 a(16)) and patterns that vanish in one step in the 15 x 15 square (A134963 a(15))

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (cell-by-cell transfer-matrix or BDD counting; the naive frontier is 2n+2 cells, i.e. 2^32-2^34 states at n = 15-16, so sparse or hashed state storage, or splitting the frontier, is needed; 128-bit or multi-modular arithmetic) · open as of 2026-10-30

## The problem

Count configurations confined to an n x n square, with all cells outside dead, evolving under Conway's Life (B3/S23) on the infinite plane. A136278(n) counts those that are unchanged after one step, including that no birth happens just outside the square. A134963(n) counts those whose successor is empty. Counts are not reduced by symmetry. Don Knuth introduced both (OEIS 2008, TAOCP Vol. 4A, Sec. 7.1.4). Tomas Rokicki corrected A136278 and extended it to n = 15 in 2010: a(15) = 1,327,574,905,899,625,395,329,686. A134963 is known through n = 14 (a(14) = 4,080,967,796,136,376,032,811,105,207,453, last edit 2015). Neither sequence has been extended since. A small brute force written for this check reproduced a(1..4) of both (1, 2, 12, 83 and 2, 11, 51, 860), which confirms the dead-exterior convention.

## What counts as a win

The exact value of A136278(16) or A134963(15), computed by two independent methods that agree. For example, a transfer-matrix count in exact big integers, plus a second implementation (another frontier order, or the same algorithm run modulo several 64-bit primes and recombined by the CRT, with a code base written separately). Both methods must reproduce every listed term of the sequence exactly. The value must not already be in the live OEIS entry at claim time.

## Partial wins

- **p1:** The exact value of the other sequence's next term, under the same two-method rule. Both terms together count as one full win, and the second term as this partial.
- **p2:** The counts of rotation- and reflection-inequivalent configurations for A136278 n = 1..15 (a new companion table), computed via Burnside's lemma with two independent implementations whose fixed-point counts for the identity element reproduce A136278.

## How a win is checked

Run both programs. Check them against the brute force for n <= 5 and against every OEIS term. For modular runs, check the CRT reconstruction across disjoint prime sets. Fetch OEIS live.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A136278>

## Sources

- <https://oeis.org/A136278>
- <https://oeis.org/A134963>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Cells just outside the square must stay dead (births outside are forbidden). A count on a bounded board with a 'no neighbours outside' convention gives different numbers.
- Counts are not symmetry-reduced.
- The terms overflow 64 bits (a(14) of A134963 is about 4e30). Unsigned 128-bit integers suffice for A136278(16) (about 4e27) and A134963(15) (about 1e35), or use big integers or several primes with the CRT.
- A134963's extension line reads 'a(12)-a(15) from Tomas Rokicki, Oct 31 2010', but only a(12)..a(14) were entered (history revision #2). A value of a(15) may exist in Rokicki's or Knuth's notes, so check before claiming.
- The A134963 growth ratio jumps between n = 13 and 14. An independent counter reproduced a(13) mod 2^64 and a(14) mod 2^32, so this is real, not a typo.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/life-nxn-still-life-and-vanishing-counts.md
```

Already set up? Say `run V3R1T4S on life-nxn-still-life-and-vanishing-counts`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `life-nxn-still-life-and-vanishing-counts`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
