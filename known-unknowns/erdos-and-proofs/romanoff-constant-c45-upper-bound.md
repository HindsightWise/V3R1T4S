# Romanoff's constant C_45: a smaller certified upper bound for the density of odd n = p + 2^k

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Tao's optimization-constants repository, constant 45: C_45 is the asymptotic density of odd integers of the form p + 2^k (p prime, k >= 0). Erdos (1950) showed it is below 1/2 using covering congruences; later upper bounds are finite 'obstruction certificates': choose a finite prime set P, look at residue classes a mod M = prod P, count how many exponents r mod T = lcm ord_q(2) keep a - 2^r coprime to M, and sum a sieve-type bound. Records on the page: 0.490941 (Habsieger-Roblot 2006), 0.490341088858244 (Chen-Dai-Li 2024), 0.490249407811155 (Griego 2026, 36 primes), 0.490180063290061 (Andrew Yoo 2026, 38 primes, optimised from Griego's set, exact-rational verifier). Open pull request #281 (27 Oct 2026) claims 0.489596115074071 with 39 primes (a 21-prime base with orders dividing T_0 = 5040, Yoo's 14 plus 43, 127, 241, 113, 109, 97, 151, together with the union of Griego's and Yoo's clusters), checked by two independently written checkers that also reproduce Griego's and Yoo's values. Lower bound 0.107648 (Elsholtz-Schlage-Puchta 2018). Target: a strictly smaller certified upper bound than the best of the page and open PRs (main), or a better lower bound (moonshot side). Variants appear as Erdos problems #205, #244 and #851.

## What counts as a win

Success means a finite prime set P and a verifier that computes, in exact rational arithmetic with a rigorous lower bound for log 2, an upper bound U on the upper density of {odd n : n = p + 2^k} via the obstruction inequality printed on the live page https://teorth.github.io/optimizationproblems/constants/45a.html, with U STRICTLY LESS (direction: min) than the smallest upper bound listed on that page and in any open pull request touching constants/45a.md at https://github.com/teorth/optimizationproblems/pulls, both re-fetched live immediately before claiming. The skeptic re-derives the residue histogram with an independently written program (at least for a seed subset of primes, plus exact replay of the cluster-update step) and recomputes U. A lower-bound improvement above the page's best lower bound also counts, with its full proof.

## Partial wins

- **p1:** An independent from-scratch reimplementation that reproduces the open PR #281 value 0.489596115074071 exactly (same rational) from its stated 39-prime set, or finds an error in it, documented as a replay note (not a record).

## How a win is checked

Clone the published verifier style (Griego's repository describes seed histogram + exact coprime-order cluster updates); rewrite the histogram step independently in another language for the first 13-20 primes and cross-check; run the exact-rational evaluation and compare to the live record. Expected minutes to an hour on a laptop.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/45a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/45a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/45a.md>
- <https://github.com/andrew-yoo/romanoff/tree/v3>
- <https://github.com/sebastian-griego/c45-romanoff-certificate/tree/v1-c45-certificate>
- <https://arxiv.org/abs/2402.06644>
- <https://github.com/teorth/optimizationproblems/pull/281>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prime-set search: add primes q whose multiplicative order of 2 divides the current T (cheap to add because T does not grow), e.g. Mersenne and Fermat-type factors of 2^d - 1 for d | T; this is how covering-system builders choose moduli.
- Cross-domain import (combinatorial optimisation / feature selection): treat the choice of P as subset selection with an expensive objective; use beam search or simulated annealing with a cheap surrogate (the seed-histogram bound) and certify only the best candidates exactly.
- Cross-domain import (covering systems research, Erdos #7 and Hough's work): reuse the large lists of moduli with small lcm used in covering-system searches to pick primes with highly composite ord_q(2).
- Change T: allow T to be a multiple of the lcm (padding) so more primes fit with the same structure; check whether the inequality benefits from coarser exponent classes.
- Lower-bound side: re-run the Elsholtz-Schlage-Puchta counting with a better Selberg-sieve upper bound for pairs p1 + 2^{k1} = p2 + 2^{k2}, computed numerically with rigorous error terms.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point log 2: the bound needs a rigorous lower bound for log 2; using double log(2) can flip the last digits.
- Silently changing the inequality: the obstruction bound has min(1/(2M), nu/(T phi(M) log 2)) per class; dropping the min or the factor 1/2 for odd n gives a fake improvement.
- Comparing to the certificate printed on the page (Griego's superseded 0.490249...) or to Yoo's page record instead of the best value including open pull requests (PR #281 claims 0.489596115074071 as of 2026-10-28).
- Histogram overflow: residue counts over M (a product of 38 primes) exceed 64 bits; use exact big integers or the cluster-update method.
- Claiming a density statement for all n instead of odd n (the page's set is odd integers).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/romanoff-constant-c45-upper-bound.md
```

Already set up? Say `run V3R1T4S on romanoff-constant-c45-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `romanoff-constant-c45-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
