# MOONSHOT - a sixth unitary perfect number (Erdős #1052, OEIS A002827)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days (structured search over 2^m times products of odd prime powers; long odds) · open as of 2026-10-30

## The problem

A unitary divisor d of n satisfies gcd(d, n/d) = 1. n is unitary perfect when the sum of its unitary divisors other than n equals n, i.e. usigma(n) = prod (1 + p^e) = 2n over the prime powers p^e exactly dividing n. Only five are known (OEIS A002827, last edited 28 Jun 2026): 6, 60, 90, 87360 and 146361946186458562560000 = 2^18*3*5^4*7*11*13*19*37*79*109*157*313, found by Charles R. Wall ('The fifth unitary perfect number', Canad. Math. Bull. 1975). Erdős Problem #1052 on erdosproblems.com (Thomas Bloom; last edited 02 Sep 2026; no comments or proof claims) asks whether there are only finitely many; Guy reports that Carlitz, Erdős and Subbarao offered $10 for settling it and Subbarao 10 cents per new example (all three offerers have died, and a sixth example would not settle finiteness). Known constraints: every unitary perfect number is even (proof by Robb J. Walters on LeanGenius, cited by OEIS in June 2026); one not divisible by 3 would be divisible by 2^m with m >= 144, have at least 144 distinct odd prime factors and exceed 10^440 (Frei 1978); and n < 2^(2^k) when n has k distinct prime factors (Goto 2007). No unitary multiperfect number with usigma(n)/n >= 3 is known (OEIS A327158).

## What counts as a win

CONFIRMED (full win): a positive integer n other than 6, 60, 90, 87360 and 146361946186458562560000, given with its complete proven prime factorisation n = prod p^e, such that prod (1 + p^e) = 2n exactly, and n absent from https://oeis.org/A002827 and from the comments on https://www.erdosproblems.com/1052, both re-fetched immediately before the claim.

## Partial wins

- **p1:** Unitary multiperfect: an integer n > 1 with complete proven factorisation such that prod (1 + p^e) = k*n exactly for an integer k >= 3, absent from OEIS A327158 (which lists 1, 6, 60, 90, 87360, all with k <= 2) at verification time.

## How a win is checked

Prove every prime factor (PARI isprime), compute prod (1 + p^e) exactly with Python big integers and compare with 2n (or k*n); check n against the OEIS data and the Erdős problem page.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A002827>

## Sources

- <https://oeis.org/A002827>
- <https://www.erdosproblems.com/1052>
- <https://doi.org/10.4153/CMB-1975-021-9>
- <http://doi.org/10.1216/rmjm/1194275935>
- <https://oeis.org/A327158>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Wall-style balancing: start from 2^m with 1 + 2^m factored (Cunningham tables), and greedily add odd prime powers p^e whose 1 + p^e supplies the missing primes, backtracking when the abundance ratio overshoots 2.
- Prime-power ledger search (imported from constraint programming): each chosen p^e contributes the factorisation of 1 + p^e to the right-hand side; require every prime's exponent to balance exactly, and prune by the rational ratio prod (1 + p^-e) against 2.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- usigma uses 1 + p^e for each exact prime power, not sigma(p^e).
- Check the full integer equality, not a ratio rounded in floating point.
- Unproven large prime factors leave the claim unproven.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/unitary-perfect-sixth-erdos-1052.md
```

Already set up? Say `run V3R1T4S on unitary-perfect-sixth-erdos-1052`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `unitary-perfect-sixth-erdos-1052`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
