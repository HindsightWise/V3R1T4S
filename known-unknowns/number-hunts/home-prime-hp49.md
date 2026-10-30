# MOONSHOT - home prime HP(49) = HP(77): factor the c251 at step 119 and continue to a prime

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (GNFS on a c251 is at the edge of public records; ECM is a lottery) · open as of 2026-10-30

## The problem

The home prime HP(n) is the prime reached by repeatedly replacing n with the concatenation of its prime factors in increasing order, with repetition. HP(49) = HP(77) (77 is step 1 of 49's trajectory) is the only open case below 100. Patrick De Geest's World!Of Numbers page (topic1.htm; server Last-Modified 2026-07-18, page footer December 12, 2022) records the history: Warut Roonguthai to step 55; Paul Leyland's MPQS and ECM breaks (steps 56 and 74); Alex Kruppa, Nicolas Daminelli, David Cleaver (WraithX) and others through step 117. HP49(119) = 73 * 16249 * c251; David Cleaver ran about 2*t60 of ECM on the c251, and Tom Dean's 2022 CADO-NFS attempt failed after six weeks, with no reported result since. OEIS A056938 has the trajectory as a b-file to step 119 (257 digits), and the 251-digit cofactor is composite.

## What counts as a win

CONFIRMED (full win) for the complete continuation of the HP(49) trajectory from HP49(119) (as given in the OEIS A056938 b-file and on https://www.worldofnumbers.com/topic1.htm, re-fetched immediately before the claim). Each step must carry a complete proven-prime factorisation, and each next step must be the decimal concatenation of the previous step's prime factors in non-decreasing order with repetition. The chain ends at a proven prime, which is HP(49).

## Partial wins

- **p1:** Complete proven-prime factorisation of the c251 cofactor of HP49(119) (= HP49(119)/(73*16249)), giving HP49(120).
- **p2:** A proven prime proper factor of that c251 (even if the cofactor stays composite).

## How a win is checked

Take HP49(119) from the b-file, check 73 * 16249 * c251 = HP49(119), check divisibility and prove primes with ECPP, form each concatenation exactly, and prove the final prime with ECPP (Primo or CM).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.worldofnumbers.com/topic1.htm>

## Sources

- <https://www.worldofnumbers.com/topic1.htm>
- <https://oeis.org/A056938>
- <https://oeis.org/A037274>
- <https://en.wikipedia.org/wiki/Home_prime>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- ECM at B1 = 3e9 and up is the only laptop-scale route; it pays off only if the c251 has a factor of at most about 80 digits.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The OEIS comment text says 117 steps while the b-file runs to step 119; use the b-file and the World!Of Numbers page.
- Order matters: concatenate the prime factors in increasing order with repetition, never with exponents (that is A195264).
- Tom Dean's 2022 note on the page says 'a c251 is being attempted at nfs@home'. That was C251_127_108, an XYYXF SNFS number (factored p107 * p145 by Jon Becker), not HP49; on 2026-10-30 the NFS@Home status page lists no HP49 number. FactorDB refused automated fetches that day, so check FactorDB and mersenneforum by hand for any result on this c251 before claiming novelty.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/home-prime-hp49.md
```

Already set up? Say `run V3R1T4S on home-prime-hp49`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `home-prime-hp49`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
