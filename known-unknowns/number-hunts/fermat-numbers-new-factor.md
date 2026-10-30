# Fermat numbers F_m = 2^(2^m)+1: a new prime factor not in Keller's table, above all for F12-F33

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (sieve k*2^n+1 and test divisibility of F_m; ECM on F12-F19 cofactors needs cluster for any real chance) · open as of 2026-10-30

## The problem

Wilfrid Keller's 'Fermat factoring status' page (prothsearch.com, last modified 2025-12-05) lists every known prime factor k*2^n+1 of a Fermat number F_m, plus the completely factored cases (F5-F11) and the composite cofactors that remain: F12 = 114689*...*C1133, F13 ... C2391, F14 ... C4880, and so on up to F19 ... C157770. F20 and F24 are known composite but have no known factor. The two newest factors on the page: Gary Gostin's 36812439837*2^3144+1 | F3135 (2025-11-27) and 1085*2^3943263+1 | F3943261 by Sascha Beat Dinkel and PrimeGrid (2025-12-03). Earlier ones include Valter Cavecchia (F5798447, 2025-01-14), Propper and Batalov (F414677, 2025-01-10) and Lelio de Paula (F7220, 2024-12-07). The page also lists the known search limits. Searches are coordinated by FermatSearch, PrimeGrid and GIMPS ECM.

## What counts as a win

CONFIRMED (full win) for m with 12 <= m <= 33 and a prime p = k*2^n+1 (n >= m+2), proven prime, such that F_m mod p = 0 and p is not listed for F_m on http://www.prothsearch.com/fermat.html (re-fetched immediately before the claim) (direction: max on the count of known Fermat factors).

## Partial wins

- **p1:** A proven prime p = k*2^n+1 dividing F_m for some m >= 34 that is not on Keller's page at verification time, outside the k- and n-ranges the page lists as fully searched.
- **p2:** A first known factor of a composite Fermat number with no known factor (for example F20 or F24), which is also a full win.

## How a win is checked

Prove p prime (Proth's theorem: find a with a^((p-1)/2) = -1 mod p). Then check 2^(2^m) = -1 mod p by m modular squarings (for huge m, by computing 2^(2^m) mod p with exponent arithmetic mod p-1). Look up p in Keller's table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.prothsearch.com/fermat.html>

## Sources

- <http://www.prothsearch.com/fermat.html>
- <https://www.fermatsearch.org/news.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For p1, sieve k*2^n+1 over a (k, n) window just past the page's search limits, then run Proth tests plus the Fermat-divisor check (pfgw -gxo style, or your own GMP code).
- For F12-F14, stage-1 ECM with very large B1 on the C1133/C2391 cofactors; GIMPS and FermatSearch keep the effort records.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- FermatSearch reserves k-ranges; a found factor in someone else's reserved range is still checkable but should be coordinated by a human.
- A k*2^n+1 prime that divides F_m for one m divides no other Fermat number; check which m with the squaring chain, not by guessing m = n-2.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/fermat-numbers-new-factor.md
```

Already set up? Say `run V3R1T4S on fermat-numbers-new-factor`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fermat-numbers-new-factor`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
