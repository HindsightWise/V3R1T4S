# MOONSHOT - a third Wieferich prime (p^2 | 2^(p-1) - 1) beyond 2^64

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (primes above 2^64 need 128-bit moduli; a small range certificate is laptop-days) · open as of 2026-10-30

## The problem

A Wieferich prime satisfies 2^(p-1) == 1 (mod p^2). Only 1093 (Meissner 1913) and 3511 (Beeger 1922) are known (OEIS A001220). Search history: Crandall-Dilcher-Pomerance (1997); Knauer-Richstein (2005); Dorais-Klyve to 6.7e15 (2011). Wieferich@Home (2007-2016) and PrimeGrid's PRPNet search (to about 4.97e17) were not double-checked; PrimeGrid suspended its search as unreliable in May 2017. PrimeGrid's BOINC Wieferich and Wall-Sun-Sun project (2020-2022) reached the software limit 2^64 = 18446744073709551616 and closed in December 2022 (end notice: forum thread 10037, 2022-11-14). OEIS (Charles R Greathouse IV, 2024-09-24) records that PrimeGrid completed the search to 2^64 with no plans to continue. Wikipedia ('As of 2026') says any third Wieferich prime exceeds 2^64. Heuristically the expected count in [2^64, 2^65] is ln(65/64), about 0.016, so this is a long shot. A hit would be checked instantly.

## What counts as a win

CONFIRMED (full win) for a proven prime p > 2^64 (direction: existence) with pow(2, p-1, p^2) == 1, checked with exact big-integer arithmetic. p must not already be reported on the status sources (OEIS A001220 and the Wikipedia Wieferich prime page, re-fetched immediately before the claim). A p below 2^64 contradicts PrimeGrid's completed search and is reported as a discrepancy, which is partial win p2, not a win.

## Partial wins

- **p1:** Range certificate above 2^64: every prime in [2^64, 2^64 + 10^14] tested, with q_p(2) mod p published in hashed blocks and every near-Wieferich prime (2^((p-1)/2) == ±1 + A*p mod p^2 with |A| <= 1000) listed. Survives a random 0.5% recomputation by the verifier.
- **p2:** A verified error in the prior search: a prime p < 2^64 with pow(2, p-1, p^2) == 1, or a near-Wieferich prime with |A| <= 100 below 2^64 that contradicts a published PrimeGrid near-Wieferich list, demonstrated exactly.

## How a win is checked

BPSW plus an ECPP/PARI primality proof for p (a 20-digit number takes milliseconds). Check pow(2, p-1, p*p) == 1 in Python. For range certificates, recompute random primes' Fermat quotients with independent code (gmpy2) and compare block hashes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A001220>

## Sources

- <https://oeis.org/A001220>
- <https://en.wikipedia.org/wiki/Wieferich_prime>
- <https://www.primegrid.com/forum_thread.php?id=10037>
- <https://www.primegrid.com/forum_thread.php?id=9436>
- <https://cs.uwaterloo.ca/journals/JIS/VOL14/Klyve/klyve3.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- 128-bit p means a 256-bit modulus p^2: use Montgomery multiplication with four 64-bit limbs, or work mod p via Fermat-quotient tricks (2^(p-1) mod p^2 from 2^((p-1)/2) computations).
- Combine with the Wall-Sun-Sun test in the same sieve pass, as PrimeGrid did.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- PrimeGrid's 2^64 result is the bound; older 'not double-checked' claims (4.97e17) are superseded.
- Wieferich primes are a different question from base-2 Wieferich pseudoprimes (composites); only primes count here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/wieferich-base-2-beyond-2-64.md
```

Already set up? Say `run V3R1T4S on wieferich-base-2-beyond-2-64`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wieferich-base-2-beyond-2-64`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
