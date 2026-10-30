# Shortest Lucas (differential addition) chains: compute C_L(51), the smallest n whose shortest Lucas chain has length 51 (OEIS A104892)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-days to a week (extend the complete L(n) table from 2^33 to about 1.1*10^10, with SIMD pruning); verification laptop-hours · open as of 2026-10-30

## The problem

A Lucas chain (Montgomery's differential addition chain) is an addition chain 1 = a_0 < ... < a_r = n in which each a_i = a_j + a_k also satisfies a_j - a_k = 0 or a_j - a_k = a_d for some earlier element. L(n) is the length of the shortest one. Daniel Bleichenbacher (thesis, ETH 1996) computed L(n) for n <= 432199 and C_L(r), the smallest n with L(n) = r. Neill Clift used Fibonacci-type element bounds and the factor method L(nm) <= L(n) + L(m) to compute L(n) for all n <= 2^33 (data addl33.bin.gz on his Lucas page). That gave C_L(r) up to r = 50: C_L(48) = 2680042177, C_L(49) = 4243717559, C_L(50) = 6698246557. OEIS A104892 credits terms from a(30) onwards to Clift (October 19, 2024). C_L(50) < 2^33 < C_L(51). Successive ratios are about 1.58, so C_L(51) is about 1.06*10^10, just past Clift's range. Bernstein, Cottaar and Lange (2024) also searched for differential addition chains.

## What counts as a win

CONFIRMED (full win) for an integer N with (a) an explicit Lucas chain of length 51 for N, every step checked for the difference condition; (b) a certificate that L(N) >= 51, given by an exhaustive search the verifier reruns with its own program; and (c) L(m) <= 50 for every m < N, shown by an extension of Clift's complete L(n) table from 2^33 to N that a second, independently written program reproduces (hash of the table, plus spot-check chains). N must not appear in https://oeis.org/A104892 or on http://additionchains.com/Lucas.html (re-fetched before the claim). Direction: extend the table (first unknown index r = 51).

## Partial wins

- **p1:** A rigorous lower bound C_L(51) > X for some X >= 9*10^9: a published complete L(n) table to X, matching Clift's addl33 data exactly on n <= 2^33, in which no n has L(n) = 51. A second, independently written program must reproduce randomly chosen blocks above 2^33 exactly.

## How a win is checked

Check that every element is a sum of two earlier elements whose difference is 0 or an earlier element. Rerun the exhaustive lower-bound search for N with an independent implementation using Fibonacci element bounds. Recompute random blocks of the table with factor-method propagation followed by single-doubling search. Diff against addl33 on the overlap.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A104892>

## Sources

- <http://additionchains.com/Lucas.html>
- <https://oeis.org/A104892>
- <http://cr.yp.to/bib/1996/bleichenbacher-thesis.ps>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Clift's layered method: get all L(n) = r + 1 targets from the L = r database through the factor method, then search only chains with a single doubling step under the Fibonacci bound a_i >= ceil((n - F_{r-i+1})/F_{r-i+2}) + 1.
- Pack 8 64-bit lanes into 512-bit SIMD registers as Clift did, and handle overflow explicitly (his first 2^32 run lost results to an overflow bug).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Differential condition: a_j - a_k must itself be in the chain (or be 0). Ordinary addition chains are shorter and do not count.
- Clift's addl33 file is indexed from zero: byte n holds L(n) and byte 0 is a dummy. Treating the first byte as L(1) shifts every value by one index.
- Overflow in vectorised pruning silently stops the search at the last level (Clift's own reported bug).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/lucas-chain-cl51.md
```

Already set up? Say `run V3R1T4S on lucas-chain-cl51`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lucas-chain-cl51`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
