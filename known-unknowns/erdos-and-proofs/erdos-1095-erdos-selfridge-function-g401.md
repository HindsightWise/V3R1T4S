# Erdos #1095 (Ecklund-Erdos-Selfridge function g(k)): g(401) and beyond, or an independent replay of g(378..400)

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (GPU wheel sieve; Eastwood's 2026 runs used CUDA), laptop-hours for checking witnesses · open as of 2026-10-30

## The problem

g(k) is the least n > k+1 such that every prime factor of C(n,k) is > k (Ecklund-Erdos-Selfridge 1974; Erdos #1095; OEIS A003458). Bounds: g(k) >> exp(c (log k)^2) (Konyagin 1999; Woett formalised this lower-bound proof in Lean, Jun 2026) and g(k) <= exp((1+o(1))k) (Ecklund-Erdos-Selfridge 1974). Exact values come from Scheidler-Williams (1992), Lukes-Scheidler-Williams (1997) and Sorenson-Sorenson-Webster (to k = 377), with the CUDA wheel method of Alexander Eastwood (2026, github.com/AlexanderEastwood/erdos-selfridge; an earlier snapshot is archived at doi 10.5281/zenodo.22057210, which predates the 400-term release) for k = 378..400. The OEIS b-file now covers k = 1..400 (A003458 edited 18 Sep 2026); g(400) = 58305842808280308870124770403739. Eastwood's README says minimality for 378..400 rests on recorded exhaustive block scans with two wheels that share implementation components, not on a fresh independent replay.

## What counts as a win

CONFIRMED: the exact value of g(401) (or of the next k beyond the OEIS b-file at verification time). The witness must satisfy the defining condition, checked with exact big-integer arithmetic and Kummer digit tests for every prime p <= k. Minimality needs an exhaustive scan of all smaller candidates, reproduced by two implementations that share no code.

## Partial wins

- **p1:** An independent exhaustive replay of g(378), ..., g(400) by code sharing no components with Eastwood's wheels, matching all 23 values or exhibiting a smaller admissible n for some k.
- **p2:** Exact g(k) for every 401 <= k <= 410 with minimality as in the success criterion.

## How a win is checked

Check the witness by Kummer's theorem: for each prime p <= k, adding k and n-k in base p has no carries, equivalently p does not divide C(n,k). Confirm with an exact binomial computation for small cases. Re-run the minimality scan with an independent sieve and compare survivor lists and hashes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A003458>

## Sources

- <https://www.erdosproblems.com/1095>
- <https://oeis.org/A003458>
- <https://github.com/AlexanderEastwood/erdos-selfridge>
- <https://arxiv.org/abs/1907.08559>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the Sorenson-Sorenson-Webster partial-prime-power wheel: CRT over small prime powers gives admissible residues, then filter the remaining primes by digit constraints.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Admissibility of a witness is easy to check; minimality is the hard part and must be exhaustive.
- Values grow irregularly (g(397) has 34 digits, g(400) 32), so a search bound from neighbouring k can be wrong.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-1095-erdos-selfridge-function-g401.md
```

Already set up? Say `run V3R1T4S on erdos-1095-erdos-selfridge-function-g401`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-1095-erdos-selfridge-function-g401`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
