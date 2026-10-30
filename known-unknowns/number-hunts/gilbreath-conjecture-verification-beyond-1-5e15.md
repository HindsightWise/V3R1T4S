# Gilbreath's conjecture: extend the verification beyond Colonna's x = 1.5 x 10^15 (2026)

🔢 **Number hunts** · standard · tractability ★★★☆☆ · compute: laptop-days (sieve the primes to about 2e15 and run about 820 rows of absolute differences over byte arrays; SIMD and multicore) · open as of 2026-10-30

## The problem

Gilbreath's conjecture (Proth 1878, Gilbreath 1958): in the triangle of iterated absolute differences of the primes 2, 3, 5, 7, 11, ..., every row after the first starts with 1. Odlyzko (1993) verified it for the first pi(10^13) = 3.4 x 10^11 rows, showing that 635 rows suffice: once a row starts with 1 followed only by 0s and 2s over a long enough stretch, all later rows in that range start with 1. The record moved in 2025-2026. Simon Plouffe (arXiv:2510.06688, Oct 2025) verified up to 10^14 independently of Jean-Francois Colonna (collaborating with Jean-Paul Delahaye). Colonna's page (last updated 2026-08-12) lists G(pi(10^14)) = 693, G(pi(2.2 x 10^14)) = 773, G(pi(6.15 x 10^14)) = 800, G(pi(10^15)) = 800, G(pi(1.2125 x 10^15)) = 811, and finally 'Verification up to 1.5x10^15 (03/18/2026)'. It says the computation was interrupted there and could have continued. Colonna also lists 'relative records', local depths in windows far beyond the verified range (for example G = 1935 near 6.02 x 10^27); these are not verifications. Wikipedia (edited 2026-10-20) cites the same 1.5 x 10^15. Target: a verification for a strictly larger x.

## What counts as a win

Success means the claimant's own computation, starting from p_1 = 2, showing that the leading entry of difference row k is 1 for every k <= pi(X), for some X STRICTLY GREATER (direction: max) than the largest verified bound on Colonna's live page (1.5 x 10^15 on 2026-10-30), in the same convention: X is the bound on the primes, the rows covered are k <= pi(X), and G(pi(X)) is reported. Colonna's and Plouffe's block data are not published, so the whole range from 2 must be covered by the claimant's logs. The claim gives the code, the depth G used, the block and overlap scheme (each block's overlap must exceed its depth so that no row is cut) and pi(X) checked against an independent pi(x) value (primecount). The skeptic re-runs the algorithm with an independently written difference-table routine on at least three randomly chosen blocks, and runs the full computation from scratch if compute allows. Colonna's page and arXiv are re-checked immediately before claiming.

## Partial wins

- **p1:** An independent reproduction of Colonna's G values at x = 10^14 (693) and x = 10^15 (800), or a documented discrepancy, with code.
- **p2:** Local Gilbreath depths for every block of a contiguous range of primes from 1.5 x 10^15 to at least 1.6 x 10^15 (block overlaps larger than the depths), with the maximum depth reported and at least three sampled blocks recomputed independently: the extension step toward the next bound.

## How a win is checked

Generate the primes with primesieve and check pi(X) against primecount. Recompute rows 1..G with an independently written loop (numpy uint8 abs-diff or C) on sampled blocks with the stated overlap, and confirm that at row G the leading entry is 1 and the following pi(X) entries are all in {0, 2}. A full re-run takes laptop-days.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.lactamme.polytechnique.fr/Mosaic/descripteurs/GilbreathConjecture.01.Ang.html>

## Sources

- <https://www.lactamme.polytechnique.fr/Mosaic/descripteurs/GilbreathConjecture.01.Ang.html>
- <https://arxiv.org/abs/2510.06688>
- <https://en.wikipedia.org/wiki/Gilbreath%27s_conjecture>
- <https://www-users.cse.umn.edu/~odlyzko/doc/arch/gilbreath.conj.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Odlyzko's reduction: you never need the full triangle, only the first G rows; once a row is 1 followed by a long run of 0/2 the remaining rows follow. Memory is one byte per prime per block.
- Rows beyond the first few fit in bytes after entries shrink, so store differences as uint8 and run abs-diff with SIMD; the cost is about G * pi(X) byte operations (about 5e16 for X = 2e15).
- Block decomposition: split the prime list into blocks overlapping by more than G entries, process them independently on all cores, and re-check the overlaps.
- Cross-domain import (streaming/GPU stencil codes): the row recurrence is a 1-D stencil, so temporal blocking (several rows per memory pass) cuts memory traffic by the blocking factor.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Convention: Colonna's 1.5 x 10^15 bounds the primes (x), not the number of rows (about pi(1.5 x 10^15) = 4.4 x 10^13 rows), while Odlyzko's 1993 record is usually quoted in rows (3.4 x 10^11); compare in the page's convention.
- Block overlaps smaller than the row depth silently corrupt later rows; a verifier must check each block's overlap.
- An off-by-one in where the prime list starts (2 or 3) changes the triangle.
- Local depths in windows far out (Colonna's 'relative records') grow with the local prime gaps; a large one near a big known gap is easy to produce and is not a verification or a win here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/gilbreath-conjecture-verification-beyond-1-5e15.md
```

Already set up? Say `run V3R1T4S on gilbreath-conjecture-verification-beyond-1-5e15`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gilbreath-conjecture-verification-beyond-1-5e15`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
