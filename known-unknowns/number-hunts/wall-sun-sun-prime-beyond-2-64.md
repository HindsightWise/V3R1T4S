# MOONSHOT - a Wall-Sun-Sun (Fibonacci-Wieferich) prime: p^2 | F_(p - (p/5)), beyond 2^64

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (Lucas-sequence doubling mod p^2 with p > 2^64; a small range certificate is laptop-days) · open as of 2026-10-30

## The problem

A Wall-Sun-Sun prime is a prime p with F_(p - (p/5)) == 0 (mod p^2), where (p/5) is the Legendre symbol. It is also called a Fibonacci-Wieferich prime. None is known. Before Wiles, Sun and Sun showed that a failure of the first case of Fermat's Last Theorem for p would force p to be a Wall-Sun-Sun prime. Search history: McIntosh and Roettger (Math. Comp. 2007) to 2e14; Dorais and Klyve to 9.7e14; PrimeGrid's first project (2011-2017, suspended as unreliable). PrimeGrid's combined Wieferich and Wall-Sun-Sun BOINC project ran from November 2020 to its close in December 2022 and reached the software limit 2^64 without a find (Wikipedia, page last edited August 2026). Heuristically about one prime per ln-ln unit is expected, and none was found below 2^64. Generalised k-Wall-Sun-Sun primes for other Lucas sequences have known small examples and do not count here.

## What counts as a win

CONFIRMED (full win) for a proven prime p > 2^64 (direction: existence) with F_(p - (p/5)) mod p^2 == 0, where F is the Fibonacci sequence (F_0 = 0, F_1 = 1), computed by fast doubling with exact big integers. p must not be reported on the Wikipedia Wall-Sun-Sun prime page at verification time. A p < 2^64 contradicts PrimeGrid's search and is reported as a discrepancy (partial win p2).

## Partial wins

- **p1:** Range certificate above 2^64: every prime in [2^64, 2^64 + 10^14] tested, with F_(p-(p/5))/p mod p published in hashed blocks and every near-Wall-Sun-Sun prime (|A| <= 1000 in PrimeGrid's classification) listed. Survives a random 0.5% recomputation by the verifier.
- **p2:** A verified error in the prior search: a prime p < 2^64 with p^2 | F_(p-(p/5)), shown exactly.

## How a win is checked

Prove p prime. Compute the Legendre symbol (p/5), then F_n mod p^2 by fast doubling in Python big integers, and check zero. Cross-check with the Lucas-sequence matrix power [[1,1],[1,0]]^n mod p^2 in independent code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime>

## Sources

- <https://en.wikipedia.org/wiki/Wall%E2%80%93Sun%E2%80%93Sun_prime>
- <https://doi.org/10.1090/S0025-5718-07-01955-2>
- <https://www.primegrid.com/forum_thread.php?id=10037>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Share the prime sieve and 256-bit Montgomery machinery with the Wieferich base-2 search: one pass tests both conditions.
- Use the Lucas V-sequence doubling (V_2n = V_n^2 - 2Q^n), which needs fewer multiplications than Fibonacci doubling.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- This is the same problem as 'Fibonacci-Wieferich prime'; do not double count.
- Use p - (p/5), not p - 1, as the index; p = 5 is excluded.
- Primes for other Lucas sequences (Pell, k-Wall-Sun-Sun) are different problems.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/wall-sun-sun-prime-beyond-2-64.md
```

Already set up? Say `run V3R1T4S on wall-sun-sun-prime-beyond-2-64`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wall-sun-sun-prime-beyond-2-64`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
