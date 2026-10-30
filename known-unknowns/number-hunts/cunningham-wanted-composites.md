# Cunningham project: a new factor of a composite cofactor of b^n +- 1 (b = 2..12), above all from the wanted lists

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★☆☆☆☆ · compute: needs cluster for NFS on C216+; ECM attempts run at laptop-days but are a lottery · open as of 2026-10-30

## The problem

The Cunningham project, run by Samuel S. Wagstaff Jr. (Purdue), keeps the tables of factorizations of b^n +- 1 for b = 2, 3, 5, 6, 7, 10, 11, 12 (with Aurifeuillian L/M parts). The 'Wanted' lists issued 2026-01-04 (want148.txt) give Ten Most Wanted, Twenty More Wanted and Smaller-but-Needed composites. Many have since been factored on the update page page149.txt (Last-Modified 2026-10-23), nearly all by NFS@Home with SNFS (2,1129+, 3,703-, 6,431+-, 7,397+, 12,311-, 12,313-, ...) and by 'Lu' (2,1207-, 11,331-, and 2,1277- C385 = p106 * p117 * p163, which completes the factorization of M1277). Still unfactored from the lists on 2026-10-30: 2,1139+ C248, 10,353- C328, 10,346+ C300, 5,503- C260, 2,1213- C297, 2,1217- C248, 2,2266L C255, ..., and all six Smaller-but-Needed: 2,1421+ C216, 10,407- C216, 2,1415+ and 2,1415- (C217 and C219; want148 and Appendix C assign the two sizes oppositely), 7,917L C217, 11,371- C217. Appendix C (appc126.txt, as of 2026-01-05; appc.txt is the bare 'Numbers to factor' list) gives every composite cofactor; the smallest is C216. Reservations are in who.txt. Champions (champ.txt): ECM record P83 by R. Propper (7,337+); SNFS record C355 (2,1193-) by J. Bos, T. Kleinjung and A. K. Lenstra; GNFS record C221 by NFS@Home.

## What counts as a win

CONFIRMED (full win) for a composite cofactor C listed in Appendix C or the 'Numbers to factor' list linked from https://homes.cerias.purdue.edu/~ssw/cun/index.html (appc126.txt and appc.txt on 2026-10-30; re-fetched immediately before the claim) and a prime p, proven prime, with 1 < p < C and C mod p = 0, provided p is not on any update page issued since that Appendix C (page149.txt and any later page linked from the index) at verification time and p divides the part of C that is still composite after dividing out every factor on those update pages (the prime cofactor left by a split reported there, printed only as pNNN, does not count) (direction: max on the count of known factors).

## Partial wins

- **p1:** The factor is for a composite on the current Wanted lists (Ten Most Wanted, Twenty More Wanted or Smaller-but-Needed, the want*.txt file linked from the index page), not yet reported on the update page.
- **p2:** Complete proven-prime factorisation of a composite listed as one of the 'first five holes' of any table in champ.txt that is not already completely factored on page149.txt or any later update page at verification time (on 2026-10-30, 2,1207-, 2,1129+, 3,703-, 3,709+, 6,431-, 6,431+, 6,436+, 7,397+, 7,398+, 7,401+, 11,331-, 12,311-, 12,313- and 12,319- were already done).

## How a win is checked

Rebuild b^n +- 1 (or the L/M Aurifeuillian part) exactly, divide out the factors in the main table and on every update page issued since (page149.txt and later), confirm the remaining composite part is the Appendix C entry or a still-composite cofactor of it, check divisibility by p, and prove p (and any cofactor claimed prime) with PARI isprime / ECPP.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://homes.cerias.purdue.edu/~ssw/cun/index.html>

## Sources

- <https://homes.cerias.purdue.edu/~ssw/cun/index.html>
- <https://homes.cerias.purdue.edu/~ssw/cun/want148.txt>
- <https://homes.cerias.purdue.edu/~ssw/cun/page149.txt>
- <https://homes.cerias.purdue.edu/~ssw/cun/appc126.txt>
- <https://homes.cerias.purdue.edu/~ssw/cun/appc.txt>
- <https://homes.cerias.purdue.edu/~ssw/cun/champ.txt>
- <https://homes.cerias.purdue.edu/~ssw/cun/who.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- ECM at B1=850M-2.9G on the unreserved Smaller-but-Needed C216-C219, which are the cheapest composites in the whole table.
- SNFS by cyclotomic polynomial: for 2,1421+ the primitive part comes from Phi_2842(2); pick a degree-6 or degree-8 polynomial and estimate the sieving with CADO-NFS before committing.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Check who.txt: many wanted numbers are reserved by NFS@Home or individuals.
- File names roll over (want148, appc126, page149 become want149, appc127, page150); always follow the index page.
- Appendix C is only reissued with each edition, so a composite already split on page149 still appears there; check the update pages.
- Rebuild sizes from b^n +- 1 yourself: want148 and Appendix C disagree on which of 2,1415+ and 2,1415- is the C217.
- M1277 (2,1277-) was fully factored in 2026 (page149); it is no longer open.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/cunningham-wanted-composites.md
```

Already set up? Say `run V3R1T4S on cunningham-wanted-composites`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cunningham-wanted-composites`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
