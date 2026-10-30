# Exact Mertens function values: M(10^24) (A084237) or M(2^76) (A084236), with new terms of A084235 (first k with |M(k)| = 2^n) as partial wins

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (or an 80+ core server for weeks: Helfgott-Thompson's M(2^75) took about 9.7 days and M(10^23) about 18.6 days on 80 cores); laptop-hours for the A084235 partial win (segmented Mobius sieve to about 3.3e11) · open as of 2026-10-30

## The problem

Exact values of M(x) = sum_{n<=x} mu(n) at large x come from combinatorial algorithms in the Lagarias-Miller-Odlyzko / Deleglise-Rivat tradition. On 2026-10-30 OEIS A084237 (M(10^n)) ends at M(10^23) = 62467771689. M(10^18)-M(10^22) are from Eugene Kuznetsov's GPU code (2011-2012; a(17)-a(19) independently confirmed by Richard Sladkey). a(21)'s sign correction and a(23) are from Harald Helfgott and Lola Thompson ('Summing mu(n): a faster elementary algorithm', arXiv:2101.08773, time O(x^(3/5)(log x)^(3/5+eps)), the first exponent improvement for an elementary method since 1985). A084236 (M(2^n)) has a b-file to n = 75: terms to 2^73 are from Greg Hurst (Math. Comp. 2018, an O(x^(2/3)) method), and M(2^74) = -6336351930 and M(2^75) = -4000846218 are from Helfgott-Thompson. Their M(10^23) took about 18.6 days on an 80-core machine and M(2^75) about 9.7 days, so M(2^76) (about 7.6e22) is a multi-week server job and M(10^24) more. Neither is in OEIS. A cheap side cell: A084235, the least k with |M(k)| = 2^n, stops at a(17) = 108500046711 (Ashley Jordan and Luke March, 2014). Hurst's published list of prominent extrema for x <= 10^16 suggests a(18) (|M| = 262144) lies between 2.97e11 and 3.31e11 and a(19) between 1.44e12 and 1.65e12; the exact first hits need only a segmented Mobius sieve. Target: a new exact value of M(10^24) or of M(2^n) for some n >= 76.

## What counts as a win

Success means a new term of A084237 (n = 24) or A084236 (n >= 76), at an index absent from the live OEIS entry and b-file when re-fetched immediately before claiming, computed twice with different algorithm parameters or different code and agreeing exactly. The claim states the exact integer, the code, the run logs, and a consistency check: the same code reproduces M(10^22), M(10^23), M(2^74) and M(2^75). The skeptic reproduces at least one smaller known value with the claimant's code and re-runs the new value if compute allows. Direction: a new term (higher index).

## Partial wins

- **p1:** New terms of A084235 beyond a(17): the least k with |M(k)| = 2^18 (expected in (2.97e11, 3.31e11) from Hurst's extrema list) and, for more, 2^19 and 2^20, each from a full segmented Mobius sieve from 1, verified by a second independent run, at indices absent from OEIS on the day of claiming.
- **p2:** An independent re-computation of M(10^22) or M(2^75) by a different code (confirming Kuznetsov or Helfgott-Thompson), documented with timings.

## How a win is checked

For the large values, build Helfgott-Thompson's algorithm (or a Deleglise-Rivat Mertens code) independently, reproduce known values at 10^20..10^23, then run the new x with two parameter settings. For the sieve terms, run a segmented Mobius sieve with a running sum and record the first k where |M| hits 2^18, then re-run on separate hardware.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A084237>

## Sources

- <https://oeis.org/A084237>
- <https://oeis.org/A084236>
- <https://oeis.org/A084235>
- <https://oeis.org/A395914>
- <https://arxiv.org/abs/2101.08773>
- <https://arxiv.org/abs/1610.08551>
- <https://arxiv.org/abs/1108.0135>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- A084235(18) first: Hurst's extrema list puts it in (2.97e11, 3.31e11), so a segmented sieve of mu with a running sum to 3.31e11 takes well under an hour on 8 cores. Record the first k where |M(k)| = 2^18.
- Helfgott-Thompson give pseudo-code and analysis; the space-saving variant (Helfgott 2020) keeps memory near x^(1/5), so M(10^24) runs on a workstation.
- Cross-domain import (pi(x) engineering in primecount): reuse Walisch's load balancing and the 'alternative alpha tuning' double-check trick, so the second run uses different internal bounds.
- M(2^76) before M(10^24): 2^76 = 7.6e22 is cheaper than the known 10^23 value and gives a calibration point.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Silent hardware errors in multi-week runs: OEIS records a past sign error (a(21)). Always do two runs with different parameters.
- Overflow: Helfgott-Thompson's implementation uses 128-bit signed integers and needed a stricter parameter choice at 10^23 to avoid overflow; check the bounds again at 10^24.
- A084235 uses |M(k)| = 2^n exactly; since M moves by at most 1 per step the first k with |M| >= 2^n has |M| = 2^n, but mind the offset (corrected March 2026).
- Hurst's 10^16 sieve recorded every extremum, so exact A084235 terms up to about n = 25 may exist in his data; the linked notebook (wolfr.am/mertens) returned 404 on 2026-10-30. Re-check OEIS before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/mertens-function-exact-values-next-terms.md
```

Already set up? Say `run V3R1T4S on mertens-function-exact-values-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mertens-function-exact-values-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
