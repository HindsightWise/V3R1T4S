# Amicable pairs: beat the smallest known ratio m/n

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Sergei Chernykh's amicable-pairs site (sech.me/ap) announces on its news page that the BOINC search for all pairs with smaller member below 10^21 finished on 2026-04-08. The main page still describes the list as complete below 10^20, and the downloadable database is dated 2023-01-01. The site also holds over a billion larger constructed pairs. The record for the most unbalanced pair (smallest m/n with m < n) was set on 2023-10-16 by 149251425686668100950 / 255075095917125253802 (ratio about 0.58512739, credited on the news page to 'BOINC: Science United, BudgieSoft'). Before it, the best even-even pair had ratio about 0.60512272 (Chernykh, 2015). The best odd-odd pair, about 0.59834304 (1997), is still the odd-odd record. A smaller ratio is a clean, checkable record. It must come from constructions beyond 10^21, since everything below has been searched exhaustively.

## What counts as a win

CONFIRMED (full win) for positive integers m < n with complete proven factorisations such that sigma(m) = sigma(n) = m + n exactly and m/n, compared as an exact rational, STRICTLY LESS (direction: min) than the smallest ratio stated on https://sech.me/ap/news.html (re-fetched immediately before the claim) and than any smaller ratio found in a same-day check of sech.me pages and the literature.

## Partial wins

- **p1:** Odd-odd record: a new amicable pair with both members odd whose ratio m/n is STRICTLY LESS than the best odd-odd ratio stated on the news page at verification time.
- **p2:** New unbalanced pair: an amicable pair with m/n < 0.6 that is absent from the downloadable non-trivial pairs file c2_filtered.7z on https://sech.me/ap/ and is NOT of a type (3,2) to (10,2) with more than 30 digits (that file omits those types; such a pair counts only after a check against the full downloadable database). Labelled 'new relative to the public download'.

## How a win is checked

Prove every prime factor (BPSW + PARI isprime/ECPP), compute sigma(m) and sigma(n) from the factorisations, check both equal m+n, compare m*q < p*n with the record ratio p/q as exact integers. For p2 grep the pair in the downloaded non-trivial list.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://sech.me/ap/news.html>

## Sources

- <https://sech.me/ap/news.html>
- <https://sech.me/ap/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Borho-Hoffmann breeders and te Riele's rules: a pair (a*u, a*p) built on a common factor a; very abundant a with small extra primes drives sigma(m)/m up, which is what a small ratio needs (sigma(m)/m = 1 + n/m).
- Integer programming (imported from operations research): choose a set of prime powers for the common part to hit a target abundancy window, as a knapsack over log(sigma(p^e)/p^e).
- Meet-in-the-middle on abundancy (imported from cryptanalysis): tabulate products of small prime powers by their sigma/n ratio in two halves and match halves whose product lands in the narrow window the ratio record needs.
- Simulated annealing over prime-signature templates (imported from statistical physics), scoring by distance of the resulting equation from solvability.
- Study the 2023 record's structure (a 2*5^2*7^2*11*17*23*31*313*523*1487*1877 shape against 2*31*53*313*743*4463*74789471) and look for the same common factor with other cofactor splits.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Ratio defined with m < n; inverting gives a number above 1.
- Incomplete factorisation fakes sigma; every factor must be proven prime.
- Pairs below 10^21 are all known (BOINC search finished 2026-04-08); a 'new' small pair is a bug.
- The 446 MB non-trivial file covers all known pairs up to 30 digits but omits types (3,2)-(10,2) for longer pairs; the full database (25.44 GB compressed, 714 GB unpacked, dated 2023-01-01) is downloadable but heavy. State exactly which list novelty was checked against.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/amicable-pair-smallest-ratio.md
```

Already set up? Say `run V3R1T4S on amicable-pair-smallest-ratio`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `amicable-pair-smallest-ratio`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
