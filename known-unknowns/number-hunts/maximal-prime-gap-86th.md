# The 86th maximal prime gap: the first gap above 1854 (rank 85 confirmed at 1.0141 x 10^20 in May 2026)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster (exhaustive gap search above the swept frontier, about 1.37e20 in late October 2026, with mingap filtering; a heuristic estimate puts the next maximal gap near 4.4e20); laptop-days for the partial-win gap hunt with primorial-offset sieving · open as of 2026-10-30

## The problem

A maximal prime gap is a gap between consecutive primes larger than every earlier gap (OEIS A005250/A002386). Proving a gap maximal needs an exhaustive search of everything below it. Oliveira e Silva, Herzog and Pardi searched exhaustively to 4 x 10^18 (rank 75, found 2009), and distributed and GPU searches carried it past 2^64. The 'Prime Number Gap Record Rising' table kept by Norman Luhn after Jens Kruse Andersen and Thomas Nicely (pzktupel.de, updated 2026-10-26) lists confirmed ranks 78-85: Steve Cole (2018), Bertil Nyman (found 2014, verified 2018), Craig Loizides (1552 and 1572, verified 2023-2024), Brian Kehrig (1676 at 2.07e19, 2024), Martin Raab and Kehrig (1724 at 6.81e19, Jan 2026), and Robert Smith and Kehrig (rank 85: 1854 at 101412319996363309069, merit 40.25, found 2026-05-08, verified 2026-05-22). Ranges above 1e20 are reserved and swept in the mersenneforum '1e20' prime-gap thread. By 2026-10-30, posts report completed ranges up to about 1.37e20 (for example BriK 1.365-1.37e20, mart_r 1.35-1.355e20) with no gap above 1854, and further reservations such as 1.38-1.39e20. The same table lists unconfirmed candidates: the smallest known start of a gap above 1854 is the 1858 at 39422251630462640179641871 (Loizides 2021, 3.94e25). Legendre's, Andrica's and Firoozbakht's conjectures and the Cramér-Shanks-Granville ratio are checked up to the same exhaustive frontier, so they are not separate targets here.

## What counts as a win

Success means a pair of consecutive primes (p, p + g) with g > 1854, p > 1.0141e20, every integer strictly between them proved composite and both endpoints proved prime, together with exhaustive coverage of [101412319996363310923, p] (from the end of the rank-85 gap) showing no gap > 1854 there. Coverage can come from the claimant's own double-checked runs or from runs already published as double-checked in the mersenneforum gap-search threads, with every sub-range cited. The claim must match the table's notion of confirmation: rank 86 is shown as confirmed on the live pzktupel page, or the evidence meets the same standard (two independent sweeps of each range). The skeptic re-verifies the gap itself (minutes) and re-sweeps a random sample of at least 1% of the claimant's own coverage with independent code. The page is re-fetched before claiming. Direction: a new confirmed rank.

## Partial wins

- **p1:** A prime gap with g >= 1856 whose start p is below 3.9422e25, i.e. below the smallest known start of any gap exceeding 1854 on the live table. This lowers the known upper bound on the start of the 86th maximal gap. Endpoints must be proved prime (ECPP/APR-CL) and interior composites must be checked.
- **p2:** A gap g > 1854 with start below 1e22 (an unconfirmed rank-86 candidate in the plausible window), checked as in p1.

## How a win is checked

For the gap: gmpy2 is_prime on all interior numbers after a wheel sieve, and ECPP (PARI primecertify or ecpp-dj) on the endpoints. For coverage: re-run an independent segmented sieve with mingap filtering on random sub-ranges and compare the lists of gaps >= 1380 with the claimant's logs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.pzktupel.de/RecordGaps/risinggap.php>

## Sources

- <https://www.pzktupel.de/RecordGaps/risinggap.php>
- <https://www.mersenneforum.org/node/1111887?p=1113181#post1113181>
- <https://oeis.org/A005250>
- <https://oeis.org/A002386>
- <https://sweet.ua.pt/tos/gaps.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For p1/p2: primorial-offset candidates N = m * P#/d - a with combined sieving (Troisi's combined_sieve) target merits of about 32-33 at 10^24-10^25, which the 1858 record shows is reachable.
- For the exhaustive search: Kehrig-style GPU sieving with mingap filtering (report only gaps >= 1380, as the forum reservations do) is orders of magnitude faster than enumerating all primes. Coordinate ranges in the forum thread so the work does not duplicate live reservations.
- Cross-domain import (extreme-value statistics): Kourbatov's record-gap heuristics (arXiv:1709.05508 on the nth record gap; the forum's own estimate puts rank 86 near 4.4e20) show where rank 86 is most likely to fall, so compute can go to that window first.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Not the merit table: the Prime Gap List (index entry prime-gap-list-merit-improvement) records the largest merit per gap size; maximality needs exhaustive coverage from below, which a merit record does not give.
- Reservations are not coverage; only double-checked, published sweeps count.
- Endpoints near 10^20-10^25 must be proved prime; BPSW alone is the forum's 'D' (double-checked, not deterministic) status, not proof.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/maximal-prime-gap-86th.md
```

Already set up? Say `run V3R1T4S on maximal-prime-gap-86th`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `maximal-prime-gap-86th`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
