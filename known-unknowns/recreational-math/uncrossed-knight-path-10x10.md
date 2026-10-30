# Longest uncrossed knight's path: settle the open 10 x 10 value (OEIS A003192, best known 61) or the closed 11 x 11 value (A157416, best known 70)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (heuristic search for longer paths is laptop-hours; an exhaustive optimality proof for 10 x 10 is laptop-days or more) · open as of 2026-10-30

## The problem

L. D. Yarbrough (1968-69) asked for the longest knight's path on an n x n board whose move segments, drawn as straight lines between square centres, never cross. The open-path maximum (OEIS A003192) is known for n <= 9: 0,0,2,5,10,17,24,35,47. Donald Knuth confirmed a(9) = 47 with ZDDs in 2010. The closed-cycle maximum (OEIS A157416) is known for n <= 10, ending in 54 on 10 x 10. Wikipedia (edited April 2026) states that open paths are known only for n <= 9 and closed ones only for n <= 10. Derek Kisman (2018, written up by Tanya Khovanova in 2023) computed exact closed values for all 3 x N to 10 x N strips and open values for 3 x N to 9 x N, using a periodicity argument. The best-known table for m x n boards up to 31 x 31 is Alex Chernov's, from his own and Kisman's searches. His site ukt.alex-black.ru no longer answers, but the Wayback Machine copy of 2021-04-16 lists 61 for the open 10 x 10 path and 70 for the closed 11 x 11 cycle. An older table by Jean-Charles Meyrignac (euler.free.fr/knight) also gives 61 for open 10 x 10, credited mainly to Robin Merson and George Jelliss.

## What counts as a win

Either (a) an uncrossed open knight's path on the 10 x 10 board with at least 62 moves, strictly above the best known 61, or a reproducible exhaustive proof that 61 is the maximum, which settles A003192(10); or (b) an uncrossed closed knight's cycle on the 11 x 11 board with at least 72 moves (cycles have even length), strictly above 70, or a reproducible exhaustive proof that 70 is the maximum, which settles A157416(11). Proofs must be independently re-run and should reproduce the known values a(n) for n <= 9 (open) and n <= 10 (closed).

## Partial wins

- **p1:** An uncrossed open knight's path on an m x n board with 10 <= m <= n <= 31, or an uncrossed closed cycle on an m x n board with 11 <= m <= n <= 31, strictly longer than the corresponding entry in Chernov's archived table (web.archive.org copy of 2021-04-16). Rows with smaller m are proven optimal by Kisman and cannot be beaten.

## How a win is checked

Check that the claimed sequence of squares consists of legal knight moves, visits no square twice (except the closing return for a cycle), and stays on the board. Then test every pair of non-adjacent move segments for intersection, including touching and collinear overlap, using exact integer orientation tests. Count the moves. For optimality proofs, rerun the search code and confirm that it reproduces the known smaller values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A003192>

## Sources

- <https://oeis.org/A003192>
- <https://oeis.org/A157416>
- <https://en.wikipedia.org/wiki/Longest_uncrossed_knight%27s_path>
- <https://web.archive.org/web/20210416192956/http://ukt.alex-black.ru/>
- <https://blog.tanyakhovanova.com/2023/07/the-power-of-a-computational-proof-uncrossed-knights-tours-continued/>
- <http://euler.free.fr/knight/index.htm>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Length means the number of moves, not the number of squares visited.
- Chernov's live site is gone, and the best-known table is only available as a 2021 Wayback copy. Check OEIS and Wikipedia for newer values before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/uncrossed-knight-path-10x10.md
```

Already set up? Say `run V3R1T4S on uncrossed-knight-path-10x10`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `uncrossed-knight-path-10x10`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
