# Primes in arithmetic progression: beat a largest-known or smallest-known AP-k record (k = 3..27), or find the first AP28

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (mid-k largest cells and red smallest cells); an AP28 is PrimeGrid-scale luck · open as of 2026-10-30

## The problem

An AP-k is k primes p + d*n for n = 0..k-1. The 'Primes in Arithmetic Progression Records' page, created by Jens Kruse Andersen (2005-2019) and now kept by Norman Luhn at pzktupel.de (last updated 12 Oct 2026), lists for k = 3..27 the largest known AP-k (judged by its largest prime; an AP-k also counts as an AP-(k-1)) and three smallest tables: minimal difference, minimal start and minimal end, where red entries are only the smallest known. The longest known progressions have 27 primes: the first, (1006686614 + 81292139*n)*23# + 31695731, by Rob Gahan with PrimeGrid's AP26 search (19 Sep 2019), and the largest, (4361612620 + 174505864*n)*23# + 184607939, by Kai Presler with PrimeGrid (2 Aug 2026). No AP28 is known. Active in 2024-2026: Norman Luhn (largest AP-9 to AP-20 except AP-14), Serge Batalov (AP-4, AP-5), Joris Perrenet (largest AP-21, Mar 2026; minimal-end AP-25 and AP-26 proved minimal, Feb 2026), Dmitry Petukhov (minimal-end AP-24 proved, Nov 2025; smallest known minimal-difference AP-22, May 2025), Christian Carquillat and an anonymous PrimeGrid user (largest AP-26, AP-25). Older cells include the largest AP-14 (103 digits, Norman Luhn, 27 Dec 2019) and AP-22/AP-23 (20 digits, Jaroslaw Wroblewski, 16 Apr 2014). Red cells on 2026-10-30: minimal difference for k = 22..27 (no AP with difference k# found), minimal start for k = 20 (only the difference is open) and k = 21..27, and minimal end for k = 27 (last prime 696112717486210091).

## What counts as a win

CONFIRMED (full win) for some k in 3..27: k integers p + d*n (n = 0..k-1), all PROVEN prime (probable primes are not accepted), whose largest member is STRICTLY GREATER (as integers) than the largest member of the largest known AP-k entry AND of every largest known AP-j entry with j > k on https://www.pzktupel.de/PAP/aprecords.php, re-fetched immediately before the claim. Direction: max on the largest prime.

## Partial wins

- **p1:** Longest ever: a proven AP-28 (or longer) of primes of any size; none is listed at verification time. Headline result.
- **p2:** Smallest-table cell: for a cell shown in red (smallest known, not proven minimal) on the live page, a proven AP-k that beats it strictly: a smaller difference than the listed one in the minimal-difference table (k = 22..27), a smaller first prime than the listed start in the minimal-start table (k = 21..27), or for k = 20 an AP-20 starting at 23 with a smaller difference, or for k = 27 an AP-27 whose last prime is below 696112717486210091.

## How a win is checked

Recompute all k members from (p, d) or the page's (a + b*n)*q# + c form, check d is a multiple of the product of primes <= k (unless p = k), prove each member prime (PARI isprime with certificate; for a*q# + 1 forms an N-1 proof since q# is factored), and compare the largest (or first, last, difference) member with the live table, including every longer listed AP, since a sub-progression of a listed longer AP is not new.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.pzktupel.de/PAP/aprecords.php>

## Sources

- <https://www.pzktupel.de/PAP/aprecords.php>
- <https://www.pzktupel.de/Documents/First_AP27.pdf>
- <http://primerecords.dk/aprecords.htm>
- <https://www.primegrid.com/forum_thread.php?id=1246>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Large-k route used by PrimeGrid's AP26 program (Jaroslaw Wroblewski, adapted by Geoff Reynolds): progressions (a + b*n)*23# + c, with a wheel sieve that rejects any (a, b) for which some member has a prime factor below a few hundred before any primality test.
- Mid-k route described on the page: compute many primes a*q# + 1 for one fixed primorial q#, then look for k-term APs among the a's (a 3-sum-like search with hashing); proofs are cheap because N - 1 is smooth.
- Red minimal-end cell for k = 27: a sieve-first search below 7*10^17 restricted to differences that are multiples of 23#, ordered by last term.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A sub-progression of a listed longer AP (e.g. n = 1..22 of a listed AP-23) is not a new record.
- Records are judged by the largest prime, not the first one or the digit count.
- Probable primes are not accepted by the table.
- The difference must be a multiple of k# unless the AP starts at the prime k itself.
- Red and black cells differ: a black cell in a smallest table is already proven minimal and cannot be beaten.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/primes-in-ap-records-ap28.md
```

Already set up? Say `run V3R1T4S on primes-in-ap-records-ap28`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `primes-in-ap-records-ap28`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
