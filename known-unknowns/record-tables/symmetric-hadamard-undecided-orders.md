# Symmetric Hadamard matrices: an order 4v where none is known (smallest 428 = 4*107, then 476, 652, 668, 716)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (propus difference families, multiplier-orbit searches, plug-in constructions; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A Hadamard matrix H is symmetric if H = H^T; they are conjectured to exist at every order 4v. D. Z. Dokovic (arXiv:2101.05429 v2, Jan 2022) listed the odd v < 200 still undecided after the propus-array work of Balonin, Dokovic and Kotsireas: 65, 89, 93, 101, 107, 119, 133, 149, 153, 163, 167, 179, 183, 189, 193; he settled 93 (order 372, arXiv:2301.02751) and 189, 473 and 1139 (arXiv:2508.17141, 2025). The unpublished Dokovic-Seberry census of 28 May 2025 lists 595 odd v < 2500 as undecided; Kishan (GitHub vatskishan03; repository 'New Hadamard matrices', github.com/vatskishan03/Hadamard) transcribed it (search/data/symmetric_census_undecided.txt) and in October 2026 posted symmetric Hadamard matrices for 102 census values (symmetric/ folder), including the orders 260, 356, 404, 532, 596, 612, 732, 772 and 876 (v = 65, 89, 101, 133, 149, 153, 183, 193, 219), leaving 490. The smallest remaining values are v = 107, 119, 163, 167, 179, 209, 213, 223, 239, 245, i.e. orders 428, 476, 652, 668, 716, 836, 852, 892, 956, 980. Hadamard matrices of these orders exist (668 and 716 since the 2026 matrices of Alpoge, Voinov and Reynolds-Haertle), but no symmetric one is reported in the sources read.

## What counts as a win

Success means an explicit 4v x 4v matrix H with entries +-1, H = H^T and H H^T = 4vI, both checked exactly by two independent programs, for v in {107, 119, 163, 167, 179} (orders 428, 476, 652, 668, 716), still listed in the live search/data/symmetric_census_undecided.txt of github.com/vatskishan03/Hadamard, with no symmetric matrix of that order in the repository's symmetric/ folder (re-listed immediately before claiming), and with no symmetric Hadamard matrix of that order found by a same-day arXiv search (direction: none; existence target).

## Partial wins

- **p1:** The same for any other odd v < 2500 on the census list, other than 189, 473 and 1139, that is still undecided at claim time (490 values at this check, for example v = 209, 213, 223, 239, 245, 247), verified as in the main criterion.

## How a win is checked

Check every entry is +-1, H equals its transpose entrywise, and H H^T = 4vI in integer arithmetic, with two independent checkers. If the claim is a propus difference family (v; k1, k2, k2, k4; lambda) with X2 = X3 and X1, X4 symmetric, expand it into the propus array with the verifier's own code and check the full matrix. Confirm the order is absent from Kishan's symmetric/ folder and from arXiv.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/vatskishan03/Hadamard/blob/main/symmetric/README.md>

## Sources

- <https://arxiv.org/abs/2101.05429>
- <https://arxiv.org/abs/2301.02751>
- <https://arxiv.org/abs/2508.17141>
- <https://github.com/vatskishan03/Hadamard/blob/main/symmetric/README.md>
- <https://github.com/vatskishan03/Hadamard/blob/main/search/data/symmetric_census_undecided.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Propus array: four circulants A, B, B, D of order v with A, D symmetric (Seberry-Balonin); search difference families invariant under a multiplier subgroup of (Z/vZ)*.
- Miyamoto's lemma and Yamada-Kiyasu in symmetric quaternary form (Kishan's main routes) from symmetric conference or skew inputs of order about 2v.
- For v = 107, 163, 167, 179 (primes), look for structures over Z_v with subgroup-orbit blocks.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A Hadamard or skew-Hadamard matrix of the same order is not enough: Kishan's repository has skew 476, and Alpoge et al. matrices of 668 and 716 are not reported symmetric.
- The census itself warns it may miss orders; Kishan found 9 census values settled by older published theorems, so check Spence's and Seberry-Balonin's corollaries before claiming novelty.
- A matrix only equivalent to a symmetric one must be presented in symmetric form.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/symmetric-hadamard-undecided-orders.md
```

Already set up? Say `run V3R1T4S on symmetric-hadamard-undecided-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `symmetric-hadamard-undecided-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
