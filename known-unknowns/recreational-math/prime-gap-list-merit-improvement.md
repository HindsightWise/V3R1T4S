# Prime Gap List: improve the record merit for some gap size

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The community Prime Gap List (github.com/primegap-list-project/prime-gap-list, file allgaps.sql, 3,930 commits, continuing Thomas Nicely's tables) records the largest known merit g/ln(p1) of a gap between consecutive primes for each even gap size g it lists. Endpoints may be certified primes or probable primes, per the primecat column. On 2026-10-28 allgaps.sql held 124,966 gap sizes: every even g up to 122,288, then sparse coverage up to 16,045,848 (the first missing even size was 122,290). It is updated several times a day; commits on 2026-10-27/28 include '48 updates by S.Troisi', 'New record 206048 merit=20.7850 found by M.Jansen', 'New record 296626 merit=5.0928 found by PDeGeest', 'new gaps by A.Renyer' (gaps up to 2,477,052) and '7 updates by Gapcoin'. Target: find a prime gap of some size g whose merit strictly exceeds the live table's merit for g, or a gap of an even size with no entry.

## What counts as a win

Success means a pair (p1, g) such that an independent checker confirms three things. (1) p1 and p1+g are prime or strong probable prime (BPSW plus Miller-Rabin with at least 20 random bases; a primality certificate via PARI primecertify/ECPP is required only if the claim says 'certified'). (2) Every integer strictly between them is composite (sieve plus BPSW on survivors). (3) Either g/ln(p1), computed in mpmath, is STRICTLY GREATER (direction: max) than the merit recorded for g in allgaps.sql on the live master branch, or g is an even gap size with no row in allgaps.sql. The comparison uses allgaps.sql re-fetched immediately before claiming; also check the last 48h of commits, open PRs and the offsite https://primegaps.cloudygo.com/merits.txt for the same g. No submission is made.

## Partial wins

- **p1:** A gap with merit >= 20 (any size) verified by the checker, even if the size already has a higher-merit record (calibration of the search).
- **p2:** A record for a gap size in a band where the table's merits are locally low (a 'merit hole'), verified.

## How a win is checked

Use the repo's own check.py logic re-implemented independently with gmpy2: is_prime(p1), is_prime(p1+g), all interior numbers composite (trial sieve + gmpy2.is_prime), merit in mpmath; then parse allgaps.sql from a fresh clone. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/primegap-list-project/prime-gap-list>

## Sources

- <https://github.com/primegap-list-project/prime-gap-list>
- <https://raw.githubusercontent.com/primegap-list-project/prime-gap-list/master/allgaps.sql>
- <https://primegaps.cloudygo.com/merits.txt>
- <https://primegap-list-project.github.io/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Plot merit vs g from allgaps.sql and target 'holes' (sizes whose merit is far below neighbours); those are cheap to beat.
- Primorial-offset search: candidates N = m·P#/d − a with combined sieving over a long interval (Troisi's combined_sieve approach), then BPSW on survivors at both ends.
- Cross-domain import (radio astronomy / SETI dedispersion): run many trial offsets through one shared sieve pass the way dedispersion pipelines share FFT work across trial DMs.
- Cross-domain import (reliability engineering 'weakest-link' statistics): model expected merit from the Cramér/Gumbel extreme-value distribution to allocate CPU only to (m, P#) bands with the highest expected record yield.
- GPU-free: use 10 cores with gmpy2 and a segmented wheel sieve; avoid duplicating heavy-hitters by choosing primorials they do not use (inspect discoverer/primorial patterns in allgaps.sql).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The list is updated daily by heavy-compute contributors; a 'record' found today may already be superseded or pending. Re-fetch allgaps.sql and recent commits immediately before claiming.
- PRP vs proven primes: the list records the endpoint category (primecat); an interior number misclassified as composite, or an endpoint that is only a weak Fermat PRP, invalidates the gap.
- Merit uses natural log of the FIRST prime p1; using p2 or log10 gives inflated merits.
- A gap is only valid if the interval contains NO prime; a sieve bug that skips one candidate creates fake huge gaps.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/prime-gap-list-merit-improvement.md
```

Already set up? Say `run V3R1T4S on prime-gap-list-merit-improvement`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `prime-gap-list-merit-improvement`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
