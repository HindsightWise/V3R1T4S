# Kummer-Vandiver conjecture: extend the verified range past 2^31 (Hart-Harvey-Ong, 2016)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster for the full win (Hart-Harvey-Ong used about 8.6 million core-hours below 2^31); near 2^31 one prime takes about 300-500 s on one core and 8-60 GB of RAM, so the p1 window (about 4,700 primes) is laptop-days on a 10-core, 64 GB machine · open as of 2026-10-30

## The problem

The Kummer-Vandiver conjecture says p does not divide the class number of Q(zeta_p + zeta_p^-1). William Hart, David Harvey and Wilson Ong (Irregular primes to two billion, Math. Comp. 86 (2017), arXiv 1605.02398) computed every irregular pair (p, r), r even in {2, ..., p-3} with B_r = 0 mod p, for all 105,097,564 odd primes p < 2^31 = 2147483648. They verified the conjecture for each of them and checked that lambda_p = nu_p = i_p, so the p-part of the class group of Q(zeta_(p^n)) is (Z/p^n)^(i_p). They found four primes with irregularity index 8 and one with index 9 (p = 1767218027); the previous maximum known was 7. The computation took about 8.6 million core-hours. This follows Buhler-Harvey (to 163,577,856, 2011), Buhler-Crandall-Ernvall-Metsankyla-Shokrollahi (to 12 million, 2001) and earlier work back to Kummer. As of 2026-10-30, no later extension past 2^31 turned up. Washington's heuristics suggest that the number of counterexamples below x grows like log log x, so a counterexample is possible but rare. The conjecture remains open.

## What counts as a win

CONFIRMED (full win): a new verified bound B >= 2^32. For every prime 2^31 < p < B: the complete list of even irregular indices r in {2, 4, ..., p-3} with B_r = 0 mod p; for every irregular pair, the Kummer-Vandiver sufficient criterion passed (the V_(p,r) test of Buhler-Harvey 2011, with the exponent correction c -> c/2 noted in HHO Section 7); and lambda_p = nu_p = i_p certified by the four incongruences of HHO Section 7, or, for pairs with 2r = 1 mod p, by the alternative test HHO use (Criteria 2 and 4 of their reference [7]). The whole range must be run by two independent implementations, or by one implementation plus an independent check of a random sample of at least 1% of the primes, and the bound must exceed any extension in the literature at verification time. A prime where the Vandiver sufficient criterion fails is not a counterexample: report it as PROMISING with its data.

## Partial wins

- **p1:** The same verification, under the same independence rules, for every prime p in [2^31, 2^31 + 1e5], with the irregular-pair list published.
- **p2:** The same for every prime p in [2^31, 2^31 + 1e6].

## How a win is checked

Reimplement the Bernoulli-mod-p computation independently (for example Harvey's multimodular approach, or a Voronoi-congruence or power-series method) and rerun random primes from the claimed window. Compare irregular-pair counts with the Poisson(1/2) expectation, rerun the V_(p,r) and Iwasawa congruence checks for every claimed irregular pair, and regression-test the code on primes below 2^31 against HHO's published irregular-pair table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1605.02398>

## Sources

- <https://arxiv.org/abs/1605.02398>
- <https://arxiv.org/abs/0912.2121>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- HHO's Rader-algorithm reduction makes the cost per prime O(p log p) word operations; a GPU number-theoretic-transform implementation is the obvious speedup.
- Only irregular pairs (about 0.5 per prime) need the costly V_(p,r) check; regular primes are done after the Bernoulli scan.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The published V_(p,r) formula in Buhler-Harvey and earlier papers has an exponent error (c should be c/2), per HHO Section 7.
- Primes just above 2^31 need more than 31-bit modular arithmetic; watch for overflow in 64-bit products.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/vandiver-beyond-2-31.md
```

Already set up? Say `run V3R1T4S on vandiver-beyond-2-31`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `vandiver-beyond-2-31`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
