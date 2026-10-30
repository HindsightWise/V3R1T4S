# MOONSHOT: an ECPP proof of a famous probable prime: Wagstaff (2^267017+1)/3, Lucas L(344293) or Fibonacci F(397379)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (tens of CPU-years: the 109 297-digit repunit proof took about 220 CPU-years) · open as of 2026-10-30

## The problem

ECPP is the only general proof method for numbers without useful N+-1 structure. The record is R(109297) (109297 digits), proven by Andreas Enge and Paul Underwood with Enge's CM software (May 2025), after R(86453) (May 2023) and R(49081) (Mar 2022). Enge's write-up puts the next repunit, R(270343), about 37 times further out of reach. Other famous families have a smallest unproven PRP of 70 000-85 000 digits. The PrimePages Wagstaff record table lists proven (2^p+1)/3 up to p = 141079 (Oct 2025), and (2^267017+1)/3 (80380 digits) is the smallest Wagstaff PRP without a proof. The Lucas-number table's largest proven is L(202667) (Nov 2023), and the next Lucas index in OEIS A001606 is 344293 (71953 digits). The Fibonacci table's largest proven is F(201107) (Sep 2023), and F(397379) (83047 digits, in OEIS A001605 since 2003) is the next PRP. On 2026-10-30 the 20th entry of the PrimePages ECPP top-20 has 45428 digits.

## What counts as a win

CONFIRMED (full win) for a complete ECPP (or other) primality certificate, checked by an independent verifier, for one of (2^267017+1)/3, L(344293) or F(397379), provided that number is not yet listed as proven on the live PrimePages Wagstaff, Lucas Number or Fibonacci Number top-20 pages (https://t5k.org/top20/page.php?id=67, id=48, id=39) or the ECPP top-20 (id=27) at claim time.

## Partial wins

- **p1:** A verified ECPP certificate for any number not already listed that has more digits than the 20th entry of the live PrimePages ECPP top-20 (45428 digits on 2026-10-30), so that it would enter that table.

## How a win is checked

Rebuild N from its definition (Wagstaff formula, or the Lucas/Fibonacci recurrence by fast doubling). Verify the certificate with an independent implementation (PARI/GP primecertisvalid for PARI-format certificates, or CM's checker). For the R(86453) record, verification took about 190 CPU-days (almost two days of real time on many cores), so budget accordingly. Confirm the number is not yet in the live tables.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://t5k.org/top20/page.php?id=27>

## Sources

- <https://t5k.org/top20/page.php?id=27>
- <https://t5k.org/top20/page.php?id=67>
- <https://t5k.org/top20/page.php?id=48>
- <https://t5k.org/top20/page.php?id=39>
- <https://enge.math.u-bordeaux.fr/blog/ecpp-109297.html>
- <https://oeis.org/A001606>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use FastECPP (CM) with a gwnum-linked arithmetic backend, as Underwood did for R(109297). Phase 1 (the curve chain) and phase 2 (CM curve construction) can run in parallel on different machines.
- Pick the smallest candidate: L(344293) at 71953 digits needs roughly 0.6 times the work of the 80380-digit Wagstaff number, since ECPP cost grows roughly with the fourth power of the digit count.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Enge and others publish these runs only at the end. A 21-month effort may already be under way, so ask around (a human action) before committing a cluster.
- A probable-prime test or a partial certificate chain is not a proof.
- Primes of 45 000+ digits that are provable by N-1/N+1 tests do not enter the ECPP table.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/ecpp-famous-unproven-prps.md
```

Already set up? Say `run V3R1T4S on ecpp-famous-unproven-prps`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ecpp-famous-unproven-prps`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
