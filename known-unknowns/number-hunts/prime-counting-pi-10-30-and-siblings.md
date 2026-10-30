# Prime-counting records: pi(10^30) (A006880), or a new pi(2^n), pi(e^n), pi(10^(n/2)) or 10^n-th prime value beyond Baugh and Walisch

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (or a 64+ core server for weeks to months; pi(10^29) took months); laptop-days only for checking smaller values · open as of 2026-10-30

## The problem

Exact values of pi(x) at large x come from combinatorial Meissel-Lehmer methods (Lagarias-Miller-Odlyzko, Deleglise-Rivat, Gourdon) and from analytic methods (Lagarias-Odlyzko; Platt; Büthe-Franke-Jost-Kleinjung, who computed pi(10^25) unconditionally in 2013). Kim Walisch's primecount, run by David Baugh, holds most records, each computed twice with different alpha tuning: pi(10^27) (2015), pi(10^28) (2020), and pi(10^29) = 1520698109714272166094258063 (2022-02-28). In sibling sequences the primecount records page (doc/Records.md, read 2026-10-30) lists pi(2^92) (2020) for A007053, pi(e^62) (2022) for A040014, pi(10^(53/2)) (2016) for A122121, and the 10^25-th prime (2022) for A006988. OEIS A006880's b-file ends at n = 29. pi(10^30) is unknown in OEIS and on the records page. The cheapest open cells are around 2-3 x 10^27: pi(e^63) (2.29e27) and pi(10^(55/2)) (3.16e27); even-indexed A122121 terms duplicate A006880. A double-checked new value in any of these sequences is a record.

## What counts as a win

Success means a new exact value for an index absent from both the live primecount Records.md and the OEIS entry (A006880 n = 30; A007053 n >= 93; A040014 n >= 63; A122121 odd n >= 55, since even n duplicate A006880; A006988 n >= 26), re-fetched immediately before claiming. It must be computed twice with different internal parameters (primecount --double-check or two different algorithms), agree exactly, and come with logs and the software version. The skeptic re-runs the same and an independent code on smaller sanity points (for example pi(10^24) and pi(10^25)) to rule out a broken build, and checks the new value against the analytic estimate R(x) + O(sqrt(x) log x) under RH as a gross-error test. A full independent re-run is the gold standard if compute allows. Direction: a new term.

## Partial wins

- **p1:** Independent confirmation of one existing record (pi(10^28), pi(10^29), pi(2^92) or pi(e^62)) by a different algorithm (an analytic method such as Platt's or Büthe-Franke-Jost-Kleinjung's), agreeing exactly.

## How a win is checked

Build primecount from source; run the claimed x with and without --double-check (on 64+ cores this takes weeks for x near 3e27). Check that the reported values agree, and compare against li(x) - (1/2) li(sqrt(x)) and Riemann's R(x) for plausibility.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/kimwalisch/primecount/blob/master/doc/Records.md>

## Sources

- <https://github.com/kimwalisch/primecount/blob/master/doc/Records.md>
- <https://oeis.org/A006880>
- <https://oeis.org/A007053>
- <https://oeis.org/A040014>
- <https://oeis.org/A122121>
- <https://oeis.org/A006988>
- <https://arxiv.org/abs/1203.5712>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- primecount 7.x is much faster than the v6.4 backup build used for the records; on a modern 128-core server pi(e^63) is weeks, not months. Use a UPS and tee logs, as the records page advises.
- Analytic route for p1: Platt's and Büthe et al.'s Weil-explicit-formula methods use zeta zeros plus a short sieve and are completely independent of Meissel-Lehmer, which makes an ideal cross-check.
- Pick the cheapest open cell (e^63, about 2.29e27) before attempting 10^30.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- OEIS b-files lag the records page (A122121's b-file ends at n = 52 while Records.md lists 10^(53/2)); check both.
- Single runs do not count; Gourdon's 2002 pi(10^23) needed a correction of 14,037,804.
- Do not confuse pi(x) at x = 10^n with the number of primes below 10^n (identical here, since 10^n is not prime), or A006988's 10^n-th prime with pi(10^n).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/prime-counting-pi-10-30-and-siblings.md
```

Already set up? Say `run V3R1T4S on prime-counting-pi-10-30-and-siblings`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `prime-counting-pi-10-30-and-siblings`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
