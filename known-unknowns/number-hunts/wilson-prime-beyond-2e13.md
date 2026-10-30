# MOONSHOT - a fourth Wilson prime (p^2 | (p-1)! + 1) beyond 2*10^13

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (amortised remainder trees over all primes; a range certificate past 2e13 is laptop-days to weeks) · open as of 2026-10-30

## The problem

A Wilson prime satisfies (p-1)! == -1 (mod p^2). Only 5, 13 (Mathews 1892) and 563 (Goldberg 1953, on SEAC) are known (OEIS A007540, revision 2026-05-25). Search history: Crandall-Dilcher-Pomerance to 5e8 (1997); the Ibercivis and mersenneforum distributed searches (Tapio Rajala's status page, last updated 2011, shows ranges done to 4e11); Edgar Costa, Robert Gerbicz and David Harvey ('A search for Wilson primes', Math. Comp. 83 (2014) 3071-3091; arXiv 1209.3436) to 2e13 with new amortised algorithms. The OEIS entry and Wikipedia (edited 2026-08-21) both give 'next term > 2*10^13', and no later search was found on 2026-10-30. Near-Wilson primes ((p-1)! == -1 + B*p mod p^2 with |B| <= 100) are tabulated from 1e6 to about 4e11 on Wikipedia. Heuristically, the expected number of Wilson primes in [2e13, 4e13] is about ln(ln 4e13 / ln 2e13), roughly 0.02.

## What counts as a win

CONFIRMED (full win) for a proven prime p > 2*10^13 (direction: existence) with ((p-1)! + 1) mod p^2 == 0, computed by two independent fast-factorial implementations, and p absent from OEIS A007540 and the Wikipedia page at verification time. A p below 2e13 contradicts the Costa-Gerbicz-Harvey search and is reported as a discrepancy (partial win p2).

## Partial wins

- **p1:** Range certificate: every prime in [2e13, 2e13 + 1e11] tested, with Wilson quotients w_p mod p published in hashed blocks and all near-Wilson primes with |B| <= 100 listed. Survives a random spot-check of 1000 primes recomputed by the verifier with an independent single-prime fast factorial.
- **p2:** A verified error in the prior record: a prime below 2e13 that is a Wilson prime, or a near-Wilson prime with |B| <= 100 between 1e6 and 4e11 missing from the published table, demonstrated exactly.

## How a win is checked

Prove p prime. Compute (p-1)! mod p^2 for that single p with a sqrt(p)-time fast factorial (FLINT or PARI) and independently via the Wilson quotient and Lerch/Glaisher relations if available; check the result equals p^2 - 1.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A007540>

## Sources

- <https://oeis.org/A007540>
- <https://arxiv.org/abs/1209.3436>
- <https://doi.org/10.1090/S0025-5718-2014-02800-7>
- <https://en.wikipedia.org/wiki/Wilson_prime>
- <https://users.jyu.fi/~tamaraja/Wilson.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reimplement the Costa-Gerbicz-Harvey accumulating remainder tree. The same residues also settle generalized Wilson orders (see target generalized-wilson-primes-open-orders), so run both together.
- GPU-friendly polynomial product trees with NTT over 64-bit primes and CRT.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rajala's distributed-search page (last updated 2011) is stale; the 2e13 bound is Costa-Gerbicz-Harvey.
- Near-Wilson primes (B != 0) are not Wilson primes.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/wilson-prime-beyond-2e13.md
```

Already set up? Say `run V3R1T4S on wilson-prime-beyond-2e13`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wilson-prime-beyond-2e13`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
