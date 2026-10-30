# Mahler's problem for Littlewood polynomials: beat the skew-symmetric record Mahler measure at an even degree 32-60 in Mossinghoff's tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (local search over +-1 coefficient vectors with root-finding; exhaustive extensions need laptop-days) · open as of 2026-10-30

## The problem

For a Littlewood polynomial f (all coefficients +-1) of degree d, Mahler's problem asks how large M(f)/sqrt(d+1) can be (is it bounded by 1 - epsilon? Borwein's book, Problem P10). M. Mossinghoff's Mahler-Measure-Database lists the largest Mahler measures of all Littlewood polynomials of each degree d <= 30 (LargeLittlewood.txt, 23 Jun 2026, extending Borwein-Mossinghoff 2008) and of skew-symmetric ones for each even d <= 60 (LargeSkewSymmLittlewood.txt, 18 Jul 2026). For even d in 32..60 only the skew-symmetric maximum is known, so it is the best known value at that degree; at d <= 30 a non-skew polynomial beats the skew maximum at d = 8, 16, 18, 24 and 30 (e.g. d = 30: 5.367254 vs 5.315882). The largest known normalized value is 0.98636 at d = 12 (the Barker polynomial of length 13). For large degree Erdelyi (2020) showed Rudin-Shapiro polynomials reach sqrt(2/e) = 0.8578, and Mossinghoff (arXiv:2405.08281v2, Oct 2025) set the asymptotic record above 0.951 with Turyn polynomials (Fekete shifted by about p/4), suggesting generalized Turyn polynomials may do better. All 1280 table entries were recomputed on 2026-10-30 with no mismatch. Open as of 2026-10-30.

## What counts as a win

CONFIRMED requires either (i) a Littlewood polynomial f of even degree d, 32 <= d <= 60, with certified M(f) STRICTLY GREATER (direction: max) than the largest value listed for that d in LargeSkewSymmLittlewood.txt (re-downloaded from https://github.com/mossinghoff/Mahler-Measure-Database at verification time) and than any value for that d in other files of the database or in newer literature (d = 60: 7.524118801007 on 2026-10-30); or (ii) a Littlewood polynomial of any degree d >= 13 with certified M(f)/sqrt(d+1) > 0.98636599 (the Barker-13 value). M(f) must be certified by rigorous root isolation (Arb/acb_poly) or by two independent high-precision methods agreeing to 20 digits. Improvements must exceed the listed value by more than 1e-9.

## Partial wins

- **p1:** An exhaustive, independently reproducible computation of the largest Mahler measure (with the top-25 list in the database's format) over all Littlewood polynomials of degree 31, provided the database does not list degree 31 at verification time; the same code must reproduce LargeLittlewood.txt for d <= 30 as a regression.
- **p2:** The same exhaustive extension for skew-symmetric Littlewood polynomials of degree 62, reproducing LargeSkewSymmLittlewood.txt for d <= 60, provided degree 62 is not listed at verification time.
- **p3:** For some degree d with 61 <= d <= 200, a Littlewood polynomial with certified M(f)/sqrt(d+1) > 0.971124, the largest normalized value in LargeSkewSymmLittlewood.txt for d >= 32 (at d = 52), provided no larger value at degree >= 61 is published at verification time.

## How a win is checked

Parse the +- string, compute all roots with python-flint acb_poly at >= 200 bits, take M(f) = product of max(1,|root|) as a certified ball, and compare with the freshly downloaded table for that degree after canonicalisation (f(x), f(-x), reversal and sign give the same M). Calibrate by recomputing the table entries (a numpy check on 2026-10-30 matched all 1280 entries to 1e-8).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/mossinghoff/Mahler-Measure-Database>

## Sources

- <https://github.com/mossinghoff/Mahler-Measure-Database>
- <https://raw.githubusercontent.com/mossinghoff/Mahler-Measure-Database/main/LargeSkewSymmLittlewood.txt>
- <https://raw.githubusercontent.com/mossinghoff/Mahler-Measure-Database/main/LargeLittlewood.txt>
- <https://arxiv.org/abs/2405.08281>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Seed local search (single and double flips, maximising log M via the sum of log|roots| outside the circle) with the skew-symmetric record polynomials and with truncated or periodically extended Turyn polynomials (Jedwab-Katz-Schmidt parameters t ~ 0.221p, d ~ 1.058p).
- log M(f) is the mean of log|f| on the unit circle (Jensen), so flips can be scored quickly with an FFT on a fine grid before exact certification.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Jensen-formula estimates on a grid are not certificates; near-unimodular roots make log|f| singular, so certify with root isolation.
- The general table stops at d = 30 and the skew table at even d = 60; at odd d >= 31 there is no listed value to beat, which is why only even d in 32..60 count for (i).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mahler-problem-littlewood-large-measure-records.md
```

Already set up? Say `run V3R1T4S on mahler-problem-littlewood-large-measure-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mahler-problem-littlewood-large-measure-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
