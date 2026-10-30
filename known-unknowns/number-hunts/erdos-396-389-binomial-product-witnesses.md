# Erdős #396 and #389: the first n with (n)(n-1)...(n-17) dividing C(2n,n), or a first witness for #389 at n = 36

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (sieved exhaustive scans near 1e17) · open as of 2026-10-30

## The problem

396 (Erdős-Graham): is it true that for every k there is n with prod_{i=0..k} (n - i) dividing C(2n,n)? OEIS A375077 gives the least such n for k = 1..16; the last three are a(14) = 359503904702190 (Justin Dehorty and Sharvil Kesarwani, Apr 2026, also found by wibble132), a(15) = 2394789405254721 (Kesarwani, Jul 2026) and a(16) = 20021368432952099 (Dehorty, Jul 2026); minimality of a(8)-a(13) is certified (Dehorty, with a Lean-verified small-prime barrier theorem, github.com/jdehorty/erdos396). Heuristically a(k+1)/a(k) is about 1/c_1 = 8.75 (Ford-Konyagin density; Nat Sothanaphan). #389 (Erdős-Straus): for every n is there k with n(n+1)...(n+k-1) | (n+k)...(n+2k-1)? OEIS A375071 (Bhavik Mehta, then Kesarwani, then Leandre Jack) gives the least k exactly for n <= 29 (k_min(28) = 18253129921815, k_min(29) = 18253129921814, Leandre Jack, forum 2026-09-04). Witnesses, not known minimal, exist for n = 30..35 (KentaKitamura 2026-08-01, Kesarwani 2026-08-25; corrected values for n = 34, 35 by Leandre Jack). A #396 witness N for k gives #389 witnesses for n = 2k+2 and 2k+3 via (n,k) -> (n+k-1, n). Both problems are open.

## What counts as a win

CONFIRMED (either): (A) an integer n with prod_{i=0..17} (n-i) | C(2n,n), i.e. a #396 witness for k = 17 (or for the smallest k with no entry in A375077 at verification time); or (B) a positive integer k with 36*37*...*(35+k) | (36+k)*...*(35+2k), i.e. a first #389 witness for n = 36 (or for the smallest n with no posted witness at verification time). In both cases the witness must not already appear in OEIS A375077/A375071 (data or comments), the #396 or #389 threads, or the Dehorty, Kesarwani (github.com/sharky564/ErdosProblems) or Leandre Jack repositories at verification time. Divisibility is checked prime by prime with Legendre's formula for the factorials involved (exact integer arithmetic), by two independent programs.

## Partial wins

- **p1:** A certified minimality proof (exhaustive scan with a provably complete sieve, reproducible) for the least k in #389 for some n in 30..35, i.e. a new exact term of A375071 beyond k_min(29).
- **p2:** A witness for #389 at some n in 30..35 with k strictly smaller than the smallest witness posted on the #389 thread or in A375071 comments at verification time.

## How a win is checked

For each prime p up to 2n (#396) or up to n+2k (#389), compute v_p of both sides via Legendre's formula v_p(N!) = sum floor(N/p^j) and check the inequality; a separate implementation recomputes with Kummer carries. For minimality claims, rerun the scan on verifier-chosen sub-intervals and audit the sieve's completeness argument.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A375077>

## Sources

- <https://www.erdosproblems.com/396>
- <https://www.erdosproblems.com/389>
- <https://oeis.org/A375077>
- <https://oeis.org/A375071>
- <https://www.erdosproblems.com/forum/thread/389>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Governor primes: v_p(C(2n,n)) is the number of carries adding n+n in base p (Kummer); candidates must make n, n-1, ..., n-k all smooth relative to sqrt(2n). Sieve by large prime factors first.
- Search directly for #389 witnesses at n = 36 using its own structure rather than the #396 transformation, which does not give minimal k.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A375071 is indexed from 0: OEIS index i corresponds to n = i+1 in the site's formulation.
- Posted witnesses for n = 34, 35 were wrong at first (they fail at p = 67); verify every posted witness before using it.
- Floating-point binomials are useless; work with valuations.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/erdos-396-389-binomial-product-witnesses.md
```

Already set up? Say `run V3R1T4S on erdos-396-389-binomial-product-witnesses`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-396-389-binomial-product-witnesses`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
