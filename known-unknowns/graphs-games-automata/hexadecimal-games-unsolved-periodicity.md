# Hexadecimal games: certify the (arithmetic) periodicity of one game on Nowakowski's unsolved list (.f6, .7f, .9, .e, .b6, ...)

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (three-heap splits cost O(n^2) per value; 1e5 to 1e6 values per game) · open as of 2026-10-30

## The problem

Hexadecimal games extend octal codes to the digits 0-f: bit 8 of digit d_k lets a player remove k tokens and leave three non-empty heaps (Winning Ways, pp. 116-117). Their nim-sequences may be arithmetic periodic: G(n + p) = G(n) + s from some n0 on. Nowakowski computed the first 100,000 values of every 1-, 2- and 3-digit game. Richard Austin's Theorem 6.8 (Calgary thesis, 1976) and Howse and Nowakowski's generalisation (Theoret. Comput. Sci. 313, 2004) certify several of them, for example .28 = .29 (period 53, saltus 16, only G(0) exceptional) and .9c (period 36, preperiod 28, saltus 16). Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem A3) lists as unsolved .1x (x in 8,9,c,d,e,f), .2x (a-f), .3x (8-e), .4x (9,b,d,f), .5x, .6x and .7x (8-f), .9x (1-a), .9d, .bx (6,9,d), .dx (1-f) and .fx (4,6,7). It singles out .9 (fractal-like values to 100,000), .e, .7f (a tendency to period 8, saltus 4, with 14 exceptional values to 100,000, the largest G(94,156) = 26,614), .b6 ('looks octal'), .b33b, and .f6 ('period 43, saltus 32, apparent preperiod 604', not certifiable because a theorem condition fails). The lane's own check on 2026-10-30, with two independent programs, reproduced .28 and .9c but found that .f6 keeps G(n + 43) = G(n) + 32 only for 604 <= n <= 1,885 and breaks at G(1,929) = 326 (pattern value 1,253). Even the listed patterns therefore need recomputation.

## What counts as a win

CONFIRMED: for one game that problem A3 of the latest Unsolved Problems column at verification time (Games of No Chance 6, 2025, on 2026-10-30) names as unsolved, an explicit n0, period p and saltus s (s = 0 allowed) with G(n + p) = G(n) + s for every n >= n0, established by both of the following. Eligible games are those in A3's list of 'other unsolved hexadecimal games' (.1x, .2x, .3x, .4x, .5x, .6x, .7x, .9x, .9d, .bx, .dx and .fx with the stated digits x) and the specimens .9, .e, .7f, .b6, .b33b and .f6. Games that A3 reports as regular (.28, .29, .9c, .205200c, .660060008, the .200...0048 family) do not count. (1) An exact check of every value over the finite window that the sufficient condition requires, by a program that shares no code with the claimant's. (2) The sufficient condition: Austin's Theorem 6.8 or the Howse-Nowakowski theorem with every hypothesis verified for this code, or a new theorem proved in the submission and formalised in Lean 4, Coq or Isabelle. A machine-checked proof that an eligible game is not arithmetic periodic is an equally full win. The code convention (bit 1: leave no heap; bit 2: one heap; bit 4: two; bit 8: three non-empty heaps) must be stated and calibrated on .28 and .9c. The result for that game must not already be published at verification time (Games of No Chance volumes, Theoret. Comput. Sci., Integers, Electron. J. Combin., arXiv).

## Partial wins

- **p1:** A formalisation in Lean 4, Coq or Isabelle of the Howse-Nowakowski arithmetic-periodicity theorem (or of Austin's Theorem 6.8), together with a verified executable checker that certifies .28 (period 53, saltus 16) and .9c (period 36, preperiod 28, saltus 16) from their nim-sequences.

## How a win is checked

Implement the nim-sequence from the code: for digit d_k and heap n, the options are the xors over all ways to leave n - k tokens in exactly h non-empty heaps, for each bit 2^h of d_k. Cross-check a fast version against brute-force enumeration of all splits for n <= 150 and calibrate on .28 and .9c. Then recompute the claimed game to the end of the window and test G(n + p) = G(n) + s for every n in [n0, window end - p]. Check each hypothesis of the cited theorem, or run the formal proof checker on the submitted formalisation.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Sources

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>
- <https://library.slmath.org/books/Book70/files/1005.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Several listed games look octal or sparse (like .b6 and .7f). Adapt Flammenkamp's rare/common sparse-space bookkeeping to three-heap splits to reach 10^7 values cheaply before looking for a period.
- Most listed games have a single digit with bit 8 set. A periodicity theorem only needs that digit's three-heap options to be handled, which may admit a cleaner window bound than Howse-Nowakowski's.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The specimen patterns quoted in A3 are not reliable at scale: .f6 breaks its quoted period-43, saltus-32 pattern at n = 1,929 (lane check with two programs, 2026-10-30). Recompute before trusting a quoted preperiod.
- Sources write hexadecimal codes with or without a leading digit before the point. In a code d1 d2 d3 here, digit k applies to removing k tokens.
- Arithmetic periodicity with rare exceptional values (as in .7f) is not arithmetic periodicity; the certificate must cover every n >= n0.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/hexadecimal-games-unsolved-periodicity.md
```

Already set up? Say `run V3R1T4S on hexadecimal-games-unsolved-periodicity`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hexadecimal-games-unsolved-periodicity`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
