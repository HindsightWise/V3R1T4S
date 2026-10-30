# Brier numbers (both Sierpiński and Riesel): one smaller than Clavier's 3316923598096294713661, or a missing small one

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-hours (covering-set and CRT search; certificates check in seconds) · open as of 2026-10-30

## The problem

A Brier number is an odd k such that k*2^n + 1 and k*2^n - 1 are both composite for every n >= 1, i.e. k is at once a Sierpiński and a Riesel number (OEIS A076335, last edited 30 May 2026). All known ones are proved by covering sets. The smallest known is 3316923598096294713661 (22 digits). Christophe Clavier found it and four other listed terms on 31 Dec 2013, with covering sets {3, 5, 17, 13, 241, 97, 673} for +1 and {1321, 41, 11, 31, 151, 331, 37, 109, 73, 19, 7, 3} for -1; our own checker confirmed both over their full periods, 48 and 180. 10439679896374780276373 was found earlier in 2013 by Dan Ismailescu and Peter Seho Park, and three further terms by Emmanuel Vantieghem in 2014. Earlier smallest-known values came from Cohen and Selfridge (1975), Eric Brier (1998), Yves Gallot (2000) and Filaseta, Finch and Kozek (2007, 24 digits). Wilfrid Keller's catalogue (prothsearch.com/Catalogue.txt) collects the known examples. Carlos Rivera's Prime Puzzles Problem 29 table of 8 Oct 2026 still shows Clavier's number as the smallest known; the later finds by Arkadiusz Wesolowski (2023), Gurisatti (2026) and Rivera (2026) are larger. The OEIS entry stresses 'there may be smaller ones'. The lower bound is 10^11: Kellen Shenton showed on 6 Oct 2025 that every odd n < 10^11 has a prime n*2^k + 1 or n*2^k - 1 (the hardest needed 38118498221*2^7552807+1).

## What counts as a win

CONFIRMED (full win): an odd k < 3316923598096294713661 with a complete proof that k*2^n + 1 and k*2^n - 1 are composite for all n >= 1: for each sign, a finite prime set S and a period L divisible by the order of 2 modulo every p in S, such that for every n in 1..L some p in S divides k*2^n +- 1, and k*2^n +- 1 > p for all n >= 1 (or another complete proof, e.g. algebraic factors on some residue classes), checked by the verifier's own code; k must be absent from https://oeis.org/A076335, re-fetched immediately before the claim.

## Partial wins

- **p1:** Missing small term: a Brier number below the listed a(9) = 32904995562220857573541, with the same kind of certificate, that is not among the listed terms of A076335, not in Clavier's list https://oeis.org/A076335/a076335.txt, not in A234594 and not in Wilfrid Keller's catalogue http://www.prothsearch.com/Catalogue.txt at verification time.

## How a win is checked

For each sign, compute L = lcm of ord_p(2) over S and check, for n = 1..L, that some p in S divides k*2^n +- 1 using modular arithmetic; check k is odd and k*2 +- 1 exceeds max S. Compare k with the OEIS data and Clavier's list.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A076335>

## Sources

- <https://oeis.org/A076335>
- <https://oeis.org/A076335/a076335.txt>
- <http://www.prothsearch.com/Catalogue.txt>
- <https://cs.uwaterloo.ca/journals/JIS/VOL16/Ismailescu/ismailescu3.html>
- <http://www.primepuzzles.net/problems/prob_029.htm>
- <http://www.primepuzzles.net/problems/prob_058.htm>
- <https://arxiv.org/abs/2209.10646>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Two-sided covering design: pick a Sierpiński covering (residue classes of n modulo L1 with primes) and a Riesel covering (modulo L2) whose prime sets are disjoint, then solve the joint congruences on k by CRT and minimise the smallest odd solution; the choice of residues is a small constraint-satisfaction problem (SAT or ILP).
- Reuse the known coverings: Clavier's 14 numbers share a few covering pairs; enumerate all residue assignments for those pairs and other low-period coverings (primes dividing 2^24 - 1, 2^36 - 1, 2^48 - 1, 2^180 - 1) to find the least CRT solution.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- k must be odd, and k*2^n +- 1 may not equal a covering prime itself.
- A failure to find primes up to some n is not a proof; only a covering (or algebraic) argument proves a Brier number.
- Raising the 10^11 lower bound is not a win under this entry.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/brier-number-smaller-than-clavier.md
```

Already set up? Say `run V3R1T4S on brier-number-smaller-than-clavier`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `brier-number-smaller-than-clavier`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
