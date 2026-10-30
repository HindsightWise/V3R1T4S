# MOONSHOT - an integer above 7373170279850 that is not a sum of four nonnegative cubes (Deshouillers-Hennecart-Landreau)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster · open as of 2026-10-30

## The problem

Deshouillers, Hennecart and Landreau ('7373170279850', Math. Comp. 69 (2000), 421-439, appendix by Purnaba) conjectured, on numerical and probabilistic evidence, that every integer greater than 7373170279850 is a sum of four nonnegative cubes, and that exactly 113936676 positive integers are not. The conjecture is recorded as open in OEIS A022566 (numbers that are not the sum of 4 nonnegative cubes, keyword 'fini'; conjecture comment by Felix Frohlich, 2019-06-01) and A181381 (comment by Martin Fuller, 2026-10-11); OEIS A003327 (sums of 4 positive cubes) carries a related comment (Greathouse and Noe, 2017) that every number above 7373170279850 is a sum of 4 positive cubes. It would give G(3) = 4 for Waring's problem for cubes, far beyond current methods (G(3) <= 7 is the proved bound), so it is believed but unproven. A counterexample would be a striking computational find. Credit: Deshouillers, Hennecart, Landreau, Purnaba, and the OEIS editors (Noe, Frohlich, Greathouse, Fuller).

## What counts as a win

CONFIRMED for an integer N > 7373170279850 such that N != a^3 + b^3 + c^3 + d^3 for all integers 0 <= a <= b <= c <= d. This is proved by a complete, independently rerunnable enumeration: for every a <= b with a^3 + b^3 <= N, the remainder N - a^3 - b^3 is shown not to be a sum of two nonnegative cubes, using exact integer cube-root tests or a sorted two-cube table. The verifier runs its own implementation. OEIS A022566 must still state the conjecture as open at verification time.

## Partial wins

- **p1:** Verified range extension: an exhaustive computation, independently reimplemented on sampled windows, certifying that every integer in (7373170279850, B] is a sum of four nonnegative cubes. B must be strictly greater than the largest range reported verified in Deshouillers-Hennecart-Landreau 2000 or later literature (the claimant cites it and the verifier confirms), with hashed per-window logs.

## How a win is checked

For a single N, an exact enumeration of a <= b with a^3 + b^3 <= N and a two-cube representability test on the remainder (about N^(2/3)/2 cases, minutes to hours for N near 10^14 to 10^16). For p1, sampled windows are rerun with an independent sieve over four-cube sums.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A022566>

## Sources

- <https://oeis.org/A022566>
- <https://oeis.org/A003327>
- <https://oeis.org/A181381>
- <https://doi.org/10.1090/S0025-5718-99-01116-3>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Numbers at or below 7373170279850 that are not sums of four cubes are expected and known; they are not counterexamples.
- The DHL paper's verified range sits behind an AMS bot check (BLOCKED on 2026-10-30). Read it through a library copy before claiming p1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/four-nonnegative-cubes-dhl-counterexample.md
```

Already set up? Say `run V3R1T4S on four-nonnegative-cubes-dhl-counterexample`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `four-nonnegative-cubes-dhl-counterexample`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
