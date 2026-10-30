# MOONSHOT - a third Wolstenholme prime (p | B_(p-3) numerator, i.e. C(2p-1,p-1) == 1 mod p^4) beyond 10^11

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (GPU-scale; per-prime cost grows linearly in p; a single claim checks in under an hour) · open as of 2026-10-30

## The problem

A Wolstenholme prime is a prime p with binomial(2p-1, p-1) == 1 (mod p^4). Equivalently, p divides the numerator of the Bernoulli number B_(p-3), so (p, p-3) is an irregular pair. Only 16843 (Selfridge-Pollack 1964) and 2124679 (Buhler-Crandall-Ernvall-Metsankyla, 1993) are known (OEIS A088164, revision 2026-04-05). Search history: McIntosh (1995) to 2e8; Trevisan-Weber (2001) to 2.5e8; McIntosh-Roettger (2007) to 1e9; McIntosh later to 1e10. Andrew R. Booker, Shehzad Hathi, Michael J. Mossinghoff and Timothy S. Trudgian ('Wolstenholme and Vandiver primes', Ramanujan J. 58 (2022) 913-941; arXiv 2101.11157 v2, 2022-03-27) raised the bound tenfold and found none below 1e11, using new congruences for Bernoulli numbers mod p and GPU searches. The OEIS comment still cites the 6e10 bound of the paper's first version (Hathi-Mossinghoff-Trudgian 2021); Wikipedia (edited 2026-08-21) gives 1e11. No search past 1e11 was found on 2026-10-30. The log log heuristic expects about one Wolstenholme prime between 1e9 and 1e24, so about 0.8 between 1e11 and 1e24.

## What counts as a win

CONFIRMED (full win) for a proven prime p > 10^11 (direction: existence) with binomial(2p-1, p-1) mod p^4 == 1, or equivalently B_(p-3) == 0 (mod p). Both forms must be checked by independent programs. p must be absent from OEIS A088164 and the Wikipedia page at verification time. A p below 1e11 contradicts the 2022 search and is reported as a discrepancy (partial win p2).

## Partial wins

- **p1:** Block certificate: the first 10^5 consecutive primes above 1e11 tested, with B_(p-3) mod p published for each, and a random 20 of them recomputed by the verifier with an independent single-prime Bernoulli-mod-p algorithm (Harvey's bernmm-style method), all matching.
- **p2:** A verified error in the prior search: a Wolstenholme prime below 1e11, demonstrated exactly.

## How a win is checked

Prove p prime. Compute B_(p-3) mod p for the single p with an O(p log p) algorithm (Harvey's method or FLINT), and independently compute binomial(2p-1, p-1) mod p^4 via a fast factorial mod p^4 (product trees). Both must agree.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2101.11157>

## Sources

- <https://arxiv.org/abs/2101.11157>
- <https://link.springer.com/article/10.1007/s11139-021-00438-3>
- <https://oeis.org/A088164>
- <https://en.wikipedia.org/wiki/Wolstenholme_prime>
- <https://doi.org/10.1090/S0025-5718-07-01955-2>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the 2022 paper's congruences for B_(p-3) mod p, which shorten the sum per prime, and port them to GPU with 64-bit Montgomery arithmetic.
- Share the pass with the Vandiver-prime test (target vandiver-euler-prime-beyond-1e11), as the 2022 paper did.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The OEIS comment's 6e10 bound is older than the 2022 published 1e11.
- Composite n with binomial(2n-1, n-1) == 1 mod n^4 is a separate open question (converse of Wolstenholme's theorem) and does not count here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/wolstenholme-prime-beyond-1e11.md
```

Already set up? Say `run V3R1T4S on wolstenholme-prime-beyond-1e11`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wolstenholme-prime-beyond-1e11`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
