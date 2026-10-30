# MOONSHOT - the Lehmer five: decide the fate of the aliquot sequence of 276, 552, 564, 660 or 966

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (GNFS on C179-C210 blocking composites at every step) · open as of 2026-10-30

## The problem

276 is the smallest number whose aliquot sequence (iterate s(n) = sigma(n) - n) is not known to terminate or become periodic. Together with 552, 564, 660 and 966 it forms the 'Lehmer five', the open main sequences below 1000. In the MersenneForum aliquot table (rechenkraft.net/aliquot) snapshot of 2026-10-30 they stand at: 276 at index 2162, 215 digits, 2*3^3*41*89*C210; 552 at index 1249, 211 digits, 2^3*P31*C179; 564 at index 3575, 209 digits, 2^2*3*5*137*C205; 660 at index 1187, 211 digits, 2^2*7*71*433*547048291*C196; 966 at index 1149, 209 digits, 2^4*13*31*67^2*C201. All five are reserved by the mersenneforum group. OEIS A008892 holds the 276 trajectory (b-file to index 2157 by Tyler Busby) and still calls its fate open. Paul Zimmermann carried 276 to index 2051 (C201) by 2017. Earlier work is due to D. H. Lehmer, Wolfgang Creyaufmueller, Christophe Clavier, Paul Zimmermann and many mersenneforum contributors.

## What counts as a win

CONFIRMED (full win) for one of 276, 552, 564, 660, 966: a chain of terms starting from the last term listed for it in https://www.rechenkraft.net/aliquot/AllSeq.txt (re-fetched immediately before the claim), each with a complete proven-prime factorisation and each next term equal to sigma minus the term, that ends at a prime (termination) or at a member of a known aliquot cycle, perfect number or amicable pair.

## Partial wins

- **p1:** Next step: a complete proven-prime factorisation of the blocking composite of one of the five as listed at verification time, giving the next term at index + 1.
- **p2:** One of the five advanced by at least 10 indices beyond the live table's index, every term fully factored into proven primes.

## How a win is checked

Recompute every step from the factorisations with big-integer arithmetic, prove every prime (ECPP for large ones), check that the start equals the table's last term at its index, and check the end (a prime, or membership in a cycle on Moews' list).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.rechenkraft.net/aliquot/AllSeq.txt>

## Sources

- <https://www.rechenkraft.net/aliquot/AllSeq.txt>
- <https://members.loria.fr/PZimmermann/records/aliquot.html>
- <https://oeis.org/A008892>
- <https://en.wikipedia.org/wiki/Aliquot_sequence>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Heavy ECM (t65+) on each new blocking composite before committing to GNFS.
- Watch for a driver escape: 552 currently carries the 2^3 guide, and losing it changes the expected trend.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- All five are reserved by the mersenneforum group; any work should be coordinated by a human.
- rechenkraft.net and FactorDB, the community stores for these sequences, refused automated clients during the 2026-10-30 check; do not bypass them, and cross-check the start term with the OEIS A008892 b-file and Zimmermann's page.
- A single wrong factorisation corrupts every later term; prove every prime.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/lehmer-five-aliquot.md
```

Already set up? Say `run V3R1T4S on lehmer-five-aliquot`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lehmer-five-aliquot`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
