# Generalized Cullen and Woodall numbers n*a^n +- 1 (a <= 12, n <= 1000): factor a listed composite cofactor

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (ECM on the large cofactors; NFS on the C188-C220 entries needs cluster) · open as of 2026-10-30

## The problem

Paul Leyland's GCW factorization tables (brnikat.com/nums/cullen_woodall) give factorizations of the Cullen numbers C(n) = n*2^n+1, the Woodall numbers W(n) = n*2^n-1 and their generalisations GC(a,n) = n*a^n+1 and GW(a,n) = n*a^n-1 for bases a = 2..12 and n <= 1000. The page, last updated 2026-10-28, says 24,845 factors have been found since the tables went public in September 2000 and 11,643 GCW numbers are fully factored. It also publishes comps.gz with the 10,369 remaining composite cofactors in numerical order; on 2026-10-30 the smallest is C188 (for example 2,934- and 5,440+) and the largest is above C1000. Progress tables credit the many contributors, and an ECMNET server is loaded with these numbers. Algebraic and Aurifeuillian factorizations are documented in algebraic.txt.

## What counts as a win

CONFIRMED (full win) for a composite C listed in https://brnikat.com/nums/cullen_woodall/comps.gz (re-fetched immediately before the claim) and a prime p, proven prime, with 1 < p < C and C mod p = 0, where p is absent from the table file for that base and sign at verification time (direction: max on the count of known factors).

## Partial wins

- **p1:** Complete proven-prime factorisation of a listed composite, so that its GCW number becomes fully factored.
- **p2:** A proven prime factor of a composite of at most 220 digits in comps.gz (the smallest, most-ECMed tier).

## How a win is checked

Compute n*a^n +- 1 exactly, divide out the table's factors, confirm the cofactor equals the comps.gz entry, check divisibility, and prove primes with PARI isprime / ECPP.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://brnikat.com/nums/cullen_woodall/cw.html>

## Sources

- <https://brnikat.com/nums/cullen_woodall/cw.html>
- <https://brnikat.com/nums/cullen_woodall/comps.gz>
- <https://brnikat.com/nums/cullen_woodall/progress_tables.html>
- <https://brnikat.com/nums/cullen_woodall/contributor_info.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Low-B1 ECM sweeps over the C500-C1100 cofactors, which have had the least work per digit.
- SNFS for n*a^n +- 1: when n = a^k*m, write it as m*a^(n+k) +- 1 and use a sextic in a^((n+k)/6).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Read contributor_info.html for reservations and the submission format.
- Known algebraic factors (algebraic.txt) are not new factors.
- The comps.gz snapshot can trail the tables by a little; check the base table too.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/gcw-cullen-woodall-composites.md
```

Already set up? Say `run V3R1T4S on gcw-cullen-woodall-composites`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gcw-cullen-woodall-composites`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
