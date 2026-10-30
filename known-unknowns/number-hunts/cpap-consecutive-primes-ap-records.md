# Consecutive primes in arithmetic progression (CPAP-k, k = 3..10): beat a largest, smallest or largest-difference known record

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (smaller CPAP-7..10 and larger-difference cells) · open as of 2026-10-30

## The problem

A CPAP-k is k CONSECUTIVE primes in arithmetic progression (no other prime between them). Norman Luhn's 'The Largest Known CPAP's' page at pzktupel.de (continuing Jens Kruse Andersen's 2005-2019 page; last updated 8 Oct 2026) lists the largest known CPAP-k for k = 3..10, with subpages for the minimal and smallest known CPAP-k (mini.php) and the largest known CPAP-k difference (diff.php). Serge Batalov holds all eight largest cells, most set in 2024-2026 (CPAP-3 with 16330 digits, 26 Jun 2024; CPAP-5, 2006 digits, 10 Jun 2026; CPAP-9, 242 digits, 8 Oct 2026; CPAP-10, 174 digits, 2 Oct 2026). The minimal CPAP-k is known only for k <= 6 (CPAP-6: 121174811 + 30n, Lander and Parkin, 1967). The smallest known CPAP-7 is 71137654873189893604531 + 210n (23 digits, Paul Zimmermann, 11 Nov 2018; the page says heuristics put the minimal near 21 digits). The smallest known CPAP-8 and CPAP-9 were improved in Sep 2026 by Ryan Min June Shin and Sohum Sukhatankar (47 and 48 digits), while the smallest known CPAP-10 (93 digits) is still Manfred Toplic's first CPAP-10 of 2 Mar 1998. CPAP-8 to -10 are known only with difference 210. No CPAP-11 is known: its difference would be a multiple of 2310 and the page calls it 'extremely hard'. The first CPAP-11 (Erdős #141) is the separate bank target erdos-141-eleven-consecutive-primes-ap, whose partial win p1 (a CPAP-10 with more digits than the largest listed) overlaps this entry's full win for k = 10.

## What counts as a win

CONFIRMED (full win) for some k in 3..10: k primes p, p + d, ..., p + (k-1)d, all PROVEN prime, with every integer strictly between consecutive members certified composite (a stated small factor or a failed base-2 Fermat test, rerun by the verifier), whose largest member is STRICTLY GREATER than the largest member of the largest known CPAP-k listed on https://www.pzktupel.de/CPAP/cpap.php, re-fetched immediately before the claim. Direction: max on the largest prime.

## Partial wins

- **p1:** Smaller known CPAP-k for k = 7..10: a certified CPAP-k whose first prime is STRICTLY SMALLER than rank 1 of the smallest known CPAP-k on https://www.pzktupel.de/CPAP/mini.php (on 2026-10-30, 71137654873189893604531 for k = 7).
- **p2:** Larger difference: a certified CPAP-k (3 <= k <= 10) whose common difference is STRICTLY GREATER than the largest known CPAP-k difference for that k on https://www.pzktupel.de/CPAP/diff.php (for k = 8..10, where only 210 is known, that means a difference of 420 or another multiple of 210 above 210).

## How a win is checked

Recompute the k members, prove each prime (PARI isprime with certificate, Primo for large ones), and check every integer between consecutive members: even numbers and multiples of small primes by trial division, the rest by a base-2 Fermat test, which certifies compositeness. Compare the largest prime (or first prime, or difference) with the live table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.pzktupel.de/CPAP/cpap.php>

## Sources

- <https://www.pzktupel.de/CPAP/cpap.php>
- <https://www.pzktupel.de/CPAP/mini.php>
- <https://www.pzktupel.de/CPAP/diff.php>
- <http://primerecords.dk/aprecords.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For difference 210 and large primes, choose the offset so that the 1254 intermediate numbers are forced composite by a covering of small primes (the page notes a guarantee for CPAP-7 above about 190 digits using the constant x177), then sieve only the k members.
- For the smallest CPAP-7, sieve p + 210n for n = 0..6 together with the 6*209 gap positions over admissible residues modulo a large primorial, keeping only p whose gaps all have a small factor or fail a cheap Fermat test. Any p below 7.11*10^22 wins, and the page's heuristic puts the minimal near 10^21, so estimate the expected number of CPAP-7s below the record before committing compute.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- An AP-k of primes is not a CPAP-k unless every number between members is composite: 41, 47, 53, 59 is an AP-4 but not a CPAP-4 because 43 is prime.
- Probable-prime members need proofs before the table accepts them (the page asks for shared credit for proofs above 2000 digits).
- Compare exact integers, not digit counts, against the listed expression with its big constants (x159, x215 and so on).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/cpap-consecutive-primes-ap-records.md
```

Already set up? Say `run V3R1T4S on cpap-consecutive-primes-ap-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cpap-consecutive-primes-ap-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
