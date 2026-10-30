# Generalized off-diagonal Schur numbers S(3; s,t,u): refute Ahmed–Schaal's S = stu - tu - u - 1 or settle a new cell with a certificate

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Let L(t) be the equation x_1 + ... + x_{t-1} = x_t. The generalized off-diagonal Schur number S(3; s,t,u) is the least N such that every 3-colouring of [1,N] has a solution of L(s) in colour 1, L(t) in colour 2 or L(u) in colour 3, with all variables taken from that colour class. This is the smallest-failing-N convention of Song-Mao. The diagonal case S(3;k,k,k) = k^3-k^2-k-1 was proven by Boza, Marín, Revuelta and Sanz (2019), matching Znám's lower bound. Tanbir Ahmed and Daniel Schaal (2015/16) computed small values, proved a general lower bound that gives S(3;s,t,u) >= stu-tu-u-1, and made two conjectures: (1) S(3;3,t,u) > 2tu-u-1, and (2) S(3;s,t,u) = stu-tu-u-1 for 4 <= s <= t <= u. Yanyan Song and Yaping Mao (arXiv:2604.11030, Apr 2026) proved (1) and rederived the lower bound in (2) (Proposition 3.1). They report SAT-computed values in Table 3, for example S(3;3,3,8) = 59, S(3;3,4,8) = 67, S(3;4,4,8) = 87, S(3;4,5,8) = 111 and S(3;4,6,7) = 118. Every published cell with s >= 4 agrees with stu-tu-u-1. Equality in Conjecture 2 is open, and so is every value outside the published tables.

## What counts as a win

Success means a 3-colouring c of {1..N} with N = stu-tu-u-1, for some 4 <= s <= t <= u not all equal. Colour class 1 must contain no solution of x_1+...+x_{s-1} = x_s, class 2 none of L(t) and class 3 none of L(u), with variables from the class, repetition allowed unless the latest arXiv:2604.11030 uses a different convention. Two independent programs must verify it. This shows S(3;s,t,u) > stu-tu-u-1 (STRICTLY GREATER, direction: max) and refutes Conjecture 2 as stated in the latest arXiv:2604.11030. Re-fetch that paper and search arXiv for newer results immediately before claiming.

## Partial wins

- **p1:** The exact value of S(3;s,t,u) for a triple with 4 <= s <= t <= u, s < u, u <= 12, that is not in the Ahmed-Schaal tables, Song-Mao Tables 2-3 or any later source found by a fresh search. It needs a valid colouring of [1, M-1] and a DRAT or LRAT certificate, checked by drat-trim or cake_lpr, that [1, M] has no valid colouring, using an encoding independent of the solver's preprocessing.
- **p2:** The same for s = 3, where no closed form is conjectured: the exact value of S(3;3,t,u) for some 3 <= t <= u <= 14 not in those tables, with a colouring and a checked UNSAT certificate.

## How a win is checked

For each colour class C and its equation length k, compute the set of sums of exactly k-1 elements of C with repetition. Use a bitset DP: P_1 = C, P_{j+1} = (P_j + C) truncated at N. The class is valid if P_{k-1} and C are disjoint. The cost is O(k N^2 / 64). For the second implementation, enumerate solutions directly for small N, or use a DP over multisets. Check that the colouring has exactly N entries and that colours are matched to equations consistently. For p1 and p2, check the UNSAT proof with drat-trim or cake_lpr and audit the CNF generator against the definition.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2604.11030>

## Sources

- <https://arxiv.org/abs/2604.11030>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Song-Mao's lower bound colourings are block or interval constructions. Use SAT with the block colouring fixed on most of [1, N-1] and a free window near the boundaries, then try to extend to N.
- For the UNSAT side, use symmetry breaking: 1 must take a colour whose equation is not solvable with x = 1 alone. Use interval-structure lemmas from Ahmed-Schaal to fix early cells, then use cube-and-conquer.
- Look at unbalanced triples (s = 4, u large), where the gap between stu-tu-u-1 and Song-Mao's Ramsey-type upper bound is largest.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Convention: S here is the least N at which every colouring fails, so a valid colouring of [1, N-1] only proves S >= N.
- Generalized Schur numbers allow repeated variables (x_1 = x_2 allowed); weak versions require distinct variables. Use the paper's convention.
- The diagonal case s = t = u is proven exact, so no counterexample exists there.
- Assigning equations to colours: S(3;s,t,u) is symmetric under permuting (s,t,u) together with the colours. Do not double count a known cell under a permutation.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/generalized-offdiagonal-schur-s3-stu.md
```

Already set up? Say `run V3R1T4S on generalized-offdiagonal-schur-s3-stu`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `generalized-offdiagonal-schur-s3-stu`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
