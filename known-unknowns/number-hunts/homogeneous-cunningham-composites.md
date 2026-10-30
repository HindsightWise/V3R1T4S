# Homogeneous Cunningham numbers a^n +- b^n: a new factor of one of the 565 listed composites

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (ECM on C250-C309; SNFS on the C201-C230 entries) · open as of 2026-10-30

## The problem

The Homogeneous Cunningham tables factor a^n +- b^n for 1 < b < a <= 12 with gcd(a,b) = 1, up to 1024 bits, with Aurifeuillian parts. Bob Silverman created them; Paul Leyland made them public in 2006 and maintained them; Paul Leyland and Jon Becker extended them in 2016; Jon Becker has maintained them since October 2018 at unshlump.com/hcn. On 2026-10-30 the page says there are 565 composites in the tables, the smallest about C201. UPDATE.txt records steady progress through 2026: NFS@Home and G. Childers by SNFS/GNFS, for example 6+5 410 C207 on 2026-09-27 and 11-9 269 C240 on 2026-09-24, and yoyo@home by ECM, for example 5-3 461 C262 on 2026-09-05. A reservations page and an ECMNET server are linked from the main page.

## What counts as a win

CONFIRMED (full win) for a composite C marked as composite in one of the a+-b tables linked from https://www.unshlump.com/hcn (re-fetched immediately before the claim) and a prime p, proven prime, with 1 < p < C and C mod p = 0, where p is absent from that table and from UPDATE.txt at verification time (direction: max on the count of known factors).

## Partial wins

- **p1:** Complete proven-prime factorisation of a listed composite, so that a^n +- b^n (or its Aurifeuillian part) becomes fully factored.
- **p2:** A proven prime factor of at least 50 digits of a listed composite of at least 250 digits (an ECM-scale find on the tables' hardest tier).

## How a win is checked

Rebuild a^n +- b^n exactly, divide out the listed factors and algebraic parts, confirm the remaining cofactor is composite and has the digit count the table shows for it (the tables print composites only as C < digits > ), check divisibility, prove primes with PARI isprime / ECPP, and grep UPDATE.txt.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.unshlump.com/hcn>

## Sources

- <https://www.unshlump.com/hcn>
- <https://www.unshlump.com/hcn/UPDATE.txt>
- <https://www.unshlump.com/hcn/reservations.html>
- <https://www.unshlump.com/hcn/limits.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- SNFS with the homogeneous polynomial: a^n - b^n gives a degree-d polynomial in (a^(n/d), b^(n/d)), which is as easy as an ordinary Cunningham number of the same size.
- Pick composites whose SNFS difficulty is far below their table neighbours (n with many small divisors).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Check the reservations page before sieving.
- The 9^n +- 4^n tables are omitted because they are subsets of 3^n +- 2^n; do not count a factor twice.
- Aurifeuillian L/M parts are separate entries; say which part p divides.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/homogeneous-cunningham-composites.md
```

Already set up? Say `run V3R1T4S on homogeneous-cunningham-composites`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `homogeneous-cunningham-composites`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
