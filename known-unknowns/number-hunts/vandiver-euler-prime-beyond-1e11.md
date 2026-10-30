# MOONSHOT - a ninth Vandiver (Euler) prime, p | E_(p-3), beyond 10^11 (OEIS A198245)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (GPU-scale per-prime Euler-number residues; a single claim checks in under an hour) · open as of 2026-10-30

## The problem

A Vandiver prime (also called an Euler prime) is a prime p that divides the Euler number E_(p-3). Zhi-Wei Sun found 149 and 241 (2010) and Romeo Mestrovic found 2946901 (2011). OEIS A198245 (revision 67, 2026-06-28; keyword more) lists eight terms and credits the next five, 16467631, 17613227, 327784727, 426369739 and 1062232319, to Hiroaki Yamanouchi (2017, with a(9) > 2e9); Booker et al. say 16467631 and 17613227 were already reported by John B. Cosgrave and Karl Dilcher (Acta Arith. 161, 2013). Andrew R. Booker, Shehzad Hathi, Michael J. Mossinghoff and Timothy S. Trudgian ('Wolstenholme and Vandiver primes', Ramanujan J. 58 (2022); arXiv 2101.11157 v2) increased the search range twentyfold and found no others below 1e11. No later extension was found on 2026-10-30. Heuristically, about one Vandiver prime is expected per factor-e increase of ln p, so the expected count in [1e11, 1e12] is ln(27.6/25.3), roughly 0.09.

## What counts as a win

CONFIRMED (full win) for a proven prime p > 10^11 (direction: existence) with E_(p-3) == 0 (mod p), computed by two independent programs. p must be absent from OEIS A198245 (DATA, comments, b-file) re-fetched immediately before the claim. A p below 1e11 not in the list contradicts the 2022 search and is reported as a discrepancy (partial win p2).

## Partial wins

- **p1:** Block certificate: the first 10^5 consecutive primes above 1e11 tested, with E_(p-3) mod p published, and a random 20 recomputed by the verifier with an independent algorithm, all matching.
- **p2:** A verified error in the prior search: a Vandiver prime below 1e11 not among the eight listed, demonstrated exactly.

## How a win is checked

Prove p prime. Compute E_(p-3) mod p for the single p through its relation to Bernoulli-type sums (for example via sums of Legendre-like characters or the generalized Bernoulli number B_(p-2, chi_4)), using two independent methods. Reproduce the eight known terms as a regression first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A198245>

## Sources

- <https://oeis.org/A198245>
- <https://arxiv.org/abs/2101.11157>
- <https://arxiv.org/abs/1212.3602>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- E_(p-3) mod p is a twisted Bernoulli number B_(p-2, chi_4) up to a unit, so Harvey-style multimodular methods for Bernoulli numbers apply.
- Run in the same GPU pass as the Wolstenholme test.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- OEIS notes an inconsistency: Hathi et al. list 2124679 (the second Wolstenholme prime) in a Vandiver context; it is not an accepted term.
- A different 'Euler primes' sequence (A196230) exists; use A198245.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/vandiver-euler-prime-beyond-1e11.md
```

Already set up? Say `run V3R1T4S on vandiver-euler-prime-beyond-1e11`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `vandiver-euler-prime-beyond-1e11`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
