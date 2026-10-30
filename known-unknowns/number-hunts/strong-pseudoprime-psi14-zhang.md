# Smallest strong pseudoprime to the first 14 prime bases: beat Zhang's conjectured psi_14 = 6003094289670105800312596501 (OEIS A014233)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-days (structured candidates of the form q*(k(q-1)+1)); an exhaustive determination of psi_14 needs a cluster · open as of 2026-10-30

## The problem

psi_m is the smallest odd composite n that is a strong probable prime (passes the Miller-Rabin test) to each of the first m prime bases (OEIS A014233, last edited 13 Oct 2026). Exact values are known for m <= 13: psi_9 = psi_10 = psi_11 = 3825123056546413051 (Yupeng Jiang and Yingpu Deng), psi_12 = 318665857834031151167461 and psi_13 = 3317044064679887385961981 (Jonathan Sorenson and Jonathan Webster, Math. Comp. 2017, arXiv:1509.00864). For m = 14..19 only upper bounds are known, from numbers Zhenxiang Zhang found in his search of special forms up to 10^36 (Math. Comp. 2007), which he conjectured to be the exact values; MathWorld's Strong Pseudoprime page lists psi_14 <= 6003094289670105800312596501, psi_15 <= 59276361075595573263446330101, psi_16 = psi_17 <= 564132928021909221014087501701 and psi_18 = psi_19 <= 1543267864443420616877677640751301. Our own check on 2026-10-30 confirmed that each is q*(2q - 1) with both factors prime and is a strong probable prime to exactly the first 14, 15, 17 and 19 prime bases. So psi_14 lies in (psi_13, 6.0*10^27]. The AMS page of Zhang's paper showed a bot check on 2026-10-30 and was not read.

## What counts as a win

CONFIRMED (full win): an odd composite n < 6003094289670105800312596501, given with its proven factorisation, that is a strong probable prime to every one of the bases 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41 and 43, refuting Zhang's conjectured value and lowering the upper bound on psi_14; n must not already be reported as a(14) in https://oeis.org/A014233, re-fetched immediately before the claim.

## Partial wins

- **p1:** Higher m: for some m in 15..19, an odd composite n that is a strong probable prime to each of the first m prime bases and is STRICTLY SMALLER than the Zhang upper bound for psi_m listed in the statement.

## How a win is checked

Independent Miller-Rabin implementation in Python (write n - 1 = d*2^s and check a^d == 1 or a^(d*2^r) == -1 mod n for some r < s) for each required base; confirm n is composite by its factorisation and compare n with the bound.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A014233>

## Sources

- <https://oeis.org/A014233>
- <https://arxiv.org/abs/1509.00864>
- <https://mathworld.wolfram.com/StrongPseudoprime.html>
- <https://arxiv.org/abs/1207.0063>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Two-factor forms n = q*(k(q - 1) + 1) with k small (Zhang's examples all have k = 2): the conditions on each base reduce to Legendre-symbol and order constraints on q, which can be sieved over q up to 10^14.
- Sorenson-Webster's algorithm for all n <= B that are strong pseudoprimes to the first m bases (heuristically B^(2/3+o(1))) restricted to the two- and three-prime cases, which are the only shapes seen for m >= 9.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Strong pseudoprimes differ from Fermat and Euler pseudoprimes; test the strong condition.
- Base 43 is the 14th prime; psi_13 itself fails base 43.
- A number that passes the 14 bases but is above Zhang's bound is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/strong-pseudoprime-psi14-zhang.md
```

Already set up? Say `run V3R1T4S on strong-pseudoprime-psi14-zhang`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `strong-pseudoprime-psi14-zhang`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
