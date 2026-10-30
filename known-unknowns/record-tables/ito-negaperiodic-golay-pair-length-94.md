# Ito's conjecture at t = 47: a negaperiodic Golay pair of length 94 (equivalently quasi-Williamson matrices of order 47)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (spectral-filtered meet-in-the-middle and SAT over Z[y]/(y^94 + 1); checking takes laptop-seconds) · open as of 2026-10-30

## The problem

Two +-1 sequences a, b of length v form a negaperiodic Golay (NG) pair if NAF_a(s) + NAF_b(s) = 0 for 1 <= s <= v - 1, where NAF_a(s) = sum_i a_i a_{i+s} with the sign of a term flipped when i + s wraps past v. NG pairs (Ito's 'associated pairs') give Hadamard matrices [[A, B], [-B^T, A^T]] of order 2v with A, B negacyclic. N. Ito conjectured that the dicyclic group of order 8t is a Hadamard group for every t; Balonin and Dokovic (Negaperiodic Golay pairs and Hadamard matrices, arXiv:1508.00640, 2015) showed this is equivalent to NG pairs existing at every even length, and for odd t to quasi-Williamson matrices of order t (four circulants in a Williamson-like array; Williamson matrices are the symmetric special case). Ito listed NG pairs of length 2t for every odd t <= 45; B. Schmidt (Des. Codes Cryptogr. 17 (1999) 61-68) proved the conjecture for t <= 46 and some infinite families. Balonin and Dokovic pose as an open problem whether NG pairs of length 94 (quasi-Williamson matrices of order 47) exist, and list the odd t <= 125 still open: 47, 59, 65, 67, 73, 81, 89, 93, 101, 103, 107, 109, 113, 119. K. Kumar's NOTES.md (github.com/vatskishan03/Hadamard, October 2026) states that the conjecture is verified for t <= 46 only and that this list has been open since 1999, recalls that Williamson matrices of orders 47 and 59 do not exist, and reports empty multiplier-invariant searches for NG pairs of lengths 94, 134, 186, 214 and 254 and for quasi-Williamson matrices of the listed orders. The near-Williamson matrices of order 47 of arXiv:2605.08661 are not quasi-Williamson matrices and do not by themselves settle t = 47. Neither does F. Szollosi's complex Hadamard matrix of order 94 (arXiv:2603.09572, March 2026): its circulant blocks of order 47 have two symmetric blocks, but one block enters as the back-circulant DR, and neither of his two published quadruples satisfies the quasi-Williamson condition AB^T + CD^T = BA^T + DC^T under any ordering, reversal, sign change or cyclic shift of the blocks (checked at audit, 2026-10-30).

## What counts as a win

Success means two +-1 sequences a, b of length 94 whose negaperiodic autocorrelations sum to zero at every shift s = 1..93, checked exactly by two independent programs, together with the Hadamard matrix [[A, B], [-B^T, A^T]] of order 188 built from the negacyclic matrices A, B and verified to satisfy H H^T = 188 I, where a same-day arXiv search finds no earlier NG pair of length 94 or quasi-Williamson matrices of order 47 (direction: none; existence target). A rigorous non-existence proof (exhaustive search with a DRAT/LRAT certificate) also counts and would refute Ito's conjecture.

## Partial wins

- **p1:** An NG pair of length 2t for t in {59, 65, 67, 73, 81, 89, 93, 101, 103, 107, 109, 113, 119} (the Balonin-Dokovic open list), after checking that no NG pair, quasi-Williamson matrices or Williamson matrices of order t have been published, checked as in the main criterion (with H H^T = 4tI for the order-4t matrix).
- **p2:** A certified exclusion, not previously published, of NG pairs of length 94 within a precisely stated structured class not already reported as searched in Kumar's NOTES.md (which reports as empty the multiplier-invariant NG structures with at most 6 orbits, notes there is none between 6 and 48 orbits, and reports as empty the quasi-Williamson quadruples of order 47 constant on the orbits of an odd-order multiplier group), for example the 48-orbit multiplier structure or a stated compression pattern, with a DRAT/LRAT certificate or an exhaustive search the skeptic re-runs to the same empty result.

## How a win is checked

Compute NAF exactly in integers: NAF_a(s) = sum_{i=0}^{v-1-s} a_i a_{i+s} - sum_{i=v-s}^{v-1} a_i a_{i+s-v}, and require NAF_a(s) + NAF_b(s) = 0 for every s >= 1. Then build the negacyclic matrices (row k is the first row shifted k places with wrapped entries negated), assemble the 2N-type array and check H H^T = 2vI. Use two independent programs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1508.00640>

## Sources

- <https://arxiv.org/abs/1508.00640>
- <https://github.com/vatskishan03/Hadamard/blob/main/NOTES.md>
- <https://arxiv.org/abs/2610.27175>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Work in Z[y]/(y^94 + 1) ~ Z[i] tensor Z[Z_47]: the power-spectrum condition |a(zeta)|^2 + |b(zeta)|^2 = 188 at the odd 188th roots of unity is a strong filter for meet-in-the-middle joins.
- Use the bijection to quasi-Williamson matrices of order 47 (four blocks with a skew/symmetric pattern) and search there with SAT+CAS.
- Turyn-type multiplication: an NG pair of length 2t times a Golay pair of length g gives length 2tg, so lengths in the open list cannot be reached from smaller ones; a direct search is needed.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Negaperiodic is not periodic or aperiodic: Golay pairs are both PG and NG pairs, but periodic Golay pairs (separate bank entries) are not NG pairs.
- Williamson matrices of order 47 do not exist (Holzmann-Kharaghani-Tayfeh-Rezaie), so Schmidt's route through Williamson orders does not apply.
- Kumar reports that multiplier-invariant structures for v = 94 jump from 6 to 48 orbits; small-orbit searches are already empty.
- A Hadamard matrix of order 188 or a complex Hadamard matrix of order 94 is not the target: the near-Williamson (arXiv:2605.08661) and Szollosi (arXiv:2603.09572) quadruples of order 47 give those but are not quasi-Williamson matrices, so they yield no NG pair of length 94.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/ito-negaperiodic-golay-pair-length-94.md
```

Already set up? Say `run V3R1T4S on ito-negaperiodic-golay-pair-length-94`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ito-negaperiodic-golay-pair-length-94`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
