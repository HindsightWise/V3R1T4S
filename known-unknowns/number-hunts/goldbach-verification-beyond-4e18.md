# MOONSHOT - Goldbach verification beyond 4 x 10^18 (Oliveira e Silva, Herzog and Pardi, 2012/2014)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (the 4e18 run took about 4.6 million work units on university grids and volunteer machines); laptop-days for a 10^13-10^14 block in the partial wins · open as of 2026-10-30

## The problem

The strong Goldbach conjecture (every even n > 2 is a sum of two primes) has been verified for all even n <= 4 x 10^18 by Tomas Oliveira e Silva, Siegfried Herzog and Silvio Pardi (Math. Comp. 83, 2014). Their distributed project page (sweet.ua.pt/tos/goldbach.html) gives 4 x 10^18 as the limit 'reached' on 2012-04-04, says the range is double-checked only up to 4 x 10^17 with no further double-checking planned, and credits contributors (DETUA, IEETA, PSU, INFN, Kraken and others) and a top-50 table of minimal Goldbach partitions. The record minimal partition is p = 9781 for n = 3325581707333960528 (Pardi). For each n the algorithm finds the least prime p with n - p prime, using a segmented sieve over intervals with a precomputed small-prime list. It also produces first-occurrence prime gaps. Wikipedia (edited 2026-09-27) still gives 4 x 10^18 with no later verification, and the project page has not moved since 2015. Two unreviewed claims go past it. Gridbach (gridbach.com, a browser volunteer-compute project; Show HN 2025-04-19) claimed 4 x 10^18 + 7 x 10^13. Its server accepts client results without independent checking, and its kernel is now in a private repository. A non-peer-reviewed preprint by Gosar, Das and Pardasani (preprints.org 202503.0949, March 2025) claims checks above 4 x 10^18 using probabilistic primality tests. Neither is a double-checked, published verification, so the accepted frontier has stood at 4 x 10^18 for about 14 years. Target: extend the verified range past 4 x 10^18.

## What counts as a win

Success means a verification that every even n in (4 x 10^18, X] is a sum of two primes, for some X >= 4.1 x 10^18 (direction: max; a shorter contiguous extension is partial win p2, not a full win). The range below 4 x 10^18 may be taken from Oliveira e Silva, Herzog and Pardi (Math. Comp. 83, 2014); the new range is the claimant's own computation, and unverified volunteer or preprint claims above 4 x 10^18 (Gridbach, preprints.org 202503.0949) may not be relied on. Records are re-checked on the project page, Wikipedia and arXiv immediately before claiming. If a newer bound exists that is published with logs or code and independently double-checked, X must exceed it by at least 10^17; unverified claims do not raise the bar but must be cited. The claim publishes code and per-interval logs: for each interval, the count of even n, the maximum minimal partition p(n) and its location, and a checksum of the p(n) values. The skeptic re-runs at least 1,000 randomly chosen sub-intervals of length 10^9 with independently written code (different sieve, and n - p proved prime by a deterministic test such as Miller-Rabin with the first 12 prime bases, proven deterministic below 3.18 x 10^23) and must reproduce the logs exactly. A coverage gap voids the claim.

## Partial wins

- **p1:** An independent double-check of a contiguous block of length at least 10^14 inside (4 x 10^17, 4 x 10^18], which the project lists as single-checked only. It must reproduce the project's published statistics for that block (minimal-partition counts or first occurrences where published) or document a discrepancy.
- **p2:** An independently re-verified contiguous block of length at least 10^15 directly above 4 x 10^18, published with logs, as a step toward the next bound.

## How a win is checked

Re-implement the minimal-partition search: segmented sieve of the interval [n - P, n] (P about 10^4) against a precomputed prime table, so that for each even n the least p with n - p prime is found. Verify the reported p(n) values by recomputation on sampled sub-intervals, compare checksums, and check the tiling of the logs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://sweet.ua.pt/tos/goldbach.html>

## Sources

- <https://sweet.ua.pt/tos/goldbach.html>
- <https://en.wikipedia.org/wiki/Goldbach%27s_conjecture>
- <https://sweet.ua.pt/tos/primes.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Minimal partitions are tiny (below 10^4), so for each n only n - p for small primes p must be tested; sieve the window [n - 10^4, n] once per block of n and reuse it across all even n in the block.
- GPU port: the per-n work is uniform and branch-light, unlike 2005-2012 CPU grids.
- Cross-domain import (BOINC-style volunteer computing with redundancy): issue every work unit twice to independent hosts and accept only matching checksums. This is the double-check the project lacked above 4e17.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not 'win' by constructing one huge n with a large least Goldbach prime (easy with the CRT); records only count inside an exhaustively verified range.
- BPSW is not a proof; below 3.3e24 use deterministic Miller-Rabin with a proven base set.
- Hardware errors over long runs: insist on two independent runs per interval.
- Claims past 4e18 exist but are unverified: Gridbach's volunteer server accepts results without checking them, and the 2025 preprints.org manuscript uses probabilistic tests and is not peer-reviewed. Do not start from their bounds; an independent re-check of their ranges is p2 material.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/goldbach-verification-beyond-4e18.md
```

Already set up? Say `run V3R1T4S on goldbach-verification-beyond-4e18`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `goldbach-verification-beyond-4e18`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
