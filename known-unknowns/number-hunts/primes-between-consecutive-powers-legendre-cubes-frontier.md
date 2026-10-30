# Primes between consecutive squares and cubes: extend Legendre's conjecture past n = 7.05 x 10^13 or the cube result past n^3 = 1.649 x 10^40

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster (the squares record ran for months on 256 Xeon Phi and 192 Xeon cores; the cubes record used about 415,000 core-hours); laptop-days for a verified block in the partial wins · open as of 2026-10-30

## The problem

Legendre's conjecture says there is a prime between n^2 and (n+1)^2 for every n. The stronger Oppermann's conjecture asks for primes in both (n^2 - n, n^2) and (n^2, n^2 + n). Proven results reach only primes between n^3 and (n+1)^3 for n >= exp(exp(32.537)) (Ingham; Dudek 2016; Cully-Hugill's thesis). The maximal-gap tables imply Legendre only up to about n = 10^10. Jonathan Sorenson and Jonathan Webster designed an algorithm in O(N log N log log N) time under Cramér's model. It sieves the progression 1 mod mR with a large prime R > n^(2/3), so each prime found is proven by a single Brillhart-Lehmer-Selfridge test, and it averages fewer than 3 primality tests per interval. arXiv:2401.13753 (Jan 2024) reported Oppermann's conjecture verified to N = 3.33 x 10^13. The published version ('An algorithm and computation to verify Legendre's conjecture up to 7 x 10^13', Res. Number Theory 11, article 4, 2025; code and data at github.com/sorenson64/olc) states N = 7.05 x 10^13 in its abstract (the title rounds it), after about half a year each on four Xeon Phi 7210s (256 cores) and a 192-core Xeon cluster. Johnston, Sorenson, Thomas and Webster ('Primes and almost primes between cubes', arXiv:2601.15564, v2 March 2026) adapted it to cubes and proved a prime in (n^3, (n+1)^3) for all n <= 2.54569 x 10^13, i.e. n^3 <= 1.649 x 10^40. That is a factor 10^5 beyond the n^3 <= 1.42 x 10^35 implied by interval estimates, at about 415,000 core-hours on Butler University clusters and NCI Gadi. Target: a strictly larger verified N for squares (Legendre) or for cubes.

## What counts as a win

Success means a verification, with a primality proof for every prime used, that each interval (n^2, (n+1)^2) for 7.05 x 10^13 < n <= N_2 contains a prime, with N_2 >= 7.5 x 10^13, or that each (n^3, (n+1)^3) for 2.54569 x 10^13 < n <= N_3 contains a prime, with N_3 >= 2.7 x 10^13 (direction: max; a shorter contiguous extension is partial win p2, not a full win). Below the published bounds the claim may rely on Sorenson-Webster (squares, N = 7.05 x 10^13) and Johnston-Sorenson-Thomas-Webster (cubes); the new range is the claimant's own logged computation from the published bound + 1, with no gap. If a newer bound is published (re-check arXiv and the sorenson64 GitHub repositories immediately before claiming), N must exceed it by at least 7%. The claim publishes code and per-block logs (first and last n, the primes found or their offsets, and the BLS certificate data R and witness). The skeptic re-runs a random sample of at least 1,000 blocks spread over the new range with independently written code (different sieve, primality proved by PARI isprime or an independent Pocklington/BLS check), and a gap in coverage voids the claim. Oppermann's two-sided form counts on the squares side under the same bar.

## Partial wins

- **p1:** An independent re-verification, with different code and proved primes, of a contiguous block of at least 10^11 consecutive n inside the already-covered range (squares: [3.33e13, 7.05e13]; cubes: [2e13, 2.54569e13]), confirming the published single computation.
- **p2:** A verified contiguous block of at least 10^11 consecutive n directly above either record (squares from 7.05e13 + 1, or cubes from 2.54569e13 + 1), published with logs, as a contribution toward the next bound.

## How a win is checked

Reimplement the progression sieve and the BLS test in C with GMP (or Python with gmpy2 for sampled blocks). For sampled n, confirm that the reported prime p lies in the interval and that p - 1 has the stated prime factor R > p^(1/3) with a valid BLS witness, or prove p with PARI. Check that the blocks tile the claimed range.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2601.15564>

## Sources

- <https://arxiv.org/abs/2401.13753>
- <https://github.com/sorenson64/olc>
- <https://arxiv.org/abs/2601.15564>
- <https://github.com/sorenson64/cubes>
- <https://en.wikipedia.org/wiki/Legendre%27s_conjecture>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the published MPI/GMP code (olc, cubes); the cube version uses m = the product of the first ten primes and no bit-mask sieve. A GPU port of the sieve-in-progression step is the obvious speed-up.
- Squares and cubes share the machinery (Theorem 2.2 of arXiv:2601.15564 covers any exponent alpha > 3/2), so a single code base can attack both frontiers.
- Cross-domain import (Monte Carlo variance reduction): Cramér's model predicts the number of candidates needed per interval; adaptive t (intervals per batch) tuned to cache, as the authors suggest, is the main lever.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Probable primes do not count: every prime used must be proved (BLS with R > p^(1/3), or another certificate).
- Check the bound conventions: the cube record is stated both as n <= 2.54569e13 and as n^3 <= 1.649e40; compare in the same unit.
- The squares record is N = 7.05 x 10^13 (published abstract), not the 7 x 10^13 in the paper's title or the olc README; a new range starting at 7e13 + 1 only re-covers known ground.
- Wikipedia's Legendre page (Jan 2026) still quotes only the maximal-gap bound (n^2 = 2e19); the real record is Sorenson-Webster's.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/primes-between-consecutive-powers-legendre-cubes-frontier.md
```

Already set up? Say `run V3R1T4S on primes-between-consecutive-powers-legendre-cubes-frontier`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `primes-between-consecutive-powers-legendre-cubes-frontier`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
