# Most intercalates (2x2 subsquares) in a Latin square of order n = 10..28: beat the A092237 / A307164 records

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-minutes to laptop-hours (counting intercalates is O(n^3)) · open as of 2026-10-30

## The problem

An intercalate is a 2x2 Latin subsquare. OEIS A092237 gives the maximum number of intercalates in a Latin square of order n. Any two rows hold at most n/2 intercalates for even n, and at most (n-3)/2 for odd n, because the permutation taking one row to the other is a derangement of odd order. So a(n) <= n^2(n-1)/4 for even n and a(n) <= n(n-1)(n-3)/4 for odd n (Heinrich and Wallis; A092237 FORMULA, Sep 2026). a(n) is known for n <= 9 (Richard Bean, 2004), for powers of 2, where the elementary abelian 2-group table meets the even bound, and for n = 2^k - 1, where a known construction meets the odd bound (630 at n = 15). Lower bounds for the other orders 10..28 come from Bean (thesis 2001) and Eduard I. Vatutin (2023-2025, proving list a092237_2.txt): a(10) >= 125, a(11) >= 172, a(12) >= 324, a(13) >= 216, a(14) >= 391, a(17) >= 736, a(18) >= 729, a(19) >= 472, a(20) >= 1500, a(21) >= 1026, a(22) >= 1497, a(23) >= 985 (proving list; the comment still says 983), a(24) >= 2736, a(25) >= 1888, a(26) >= 2197, a(28) >= 2940. The diagonal-square sequence A307164 also gives lower bounds, and at n = 27 it is higher: a diagonal Latin square of order 27 with 1372 intercalates, against A092237's listed 648. So the real record at 27 is at least 1372.

## What counts as a win

Success means an explicit Latin square of order n, 10 <= n <= 28 with n not 15 or 16, whose number of intercalates is STRICTLY GREATER than the largest bound listed for that n in A092237 (comments and the a092237_2.txt proving-list headers) and A307164 (comments and its proving-list headers). Re-fetch all of them immediately before claiming. The 2026-10-30 values are above; the n = 23 bar is 985 and the n = 27 bar is 1372. The count must agree between two independent programs. Order 16 is excluded because 960 meets the proven bound n^2(n-1)/4. Order 15 is excluded because 630 meets the proven odd-order bound n(n-1)(n-3)/4.

## Partial wins

- **p1:** A diagonal Latin square (both diagonals are transversals) of order n, 10 <= n <= 28 with n not 15 or 16, with more intercalates than the live A307164 bound for that n. The 2026-10-30 values for n = 10..28 are 109, 172, 324, 216, 391, -, -, 736, 547, 457, 1500, 785, 887, 899, 2160, 1888, 1525, 1372, 2892.

## How a win is checked

Check the square is Latin (and, for p1, that the main diagonal and the antidiagonal each have n distinct symbols). Count intercalates: for each pair of rows r < r' and each column c, let c' be the column where row r' has the symbol L[r][c]; count when L[r'][c] = L[r][c'] and c < c'. Use two independent programs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A092237>

## Sources

- <https://oeis.org/A092237>
- <https://oeis.org/A092237/a092237_2.txt>
- <https://oeis.org/A307164>
- <https://arxiv.org/abs/2606.12996>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Direct products and near-products of 2-group tables with small Latin squares (Bean's thesis Chapter 5 bounds for orders 2^a m and 2^a m + 1).
- Local search with intercalate-preserving cycle switches; the count updates incrementally.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A092237 understates n = 27 (648) relative to A307164 (1372). Always take the max of both.
- The odd-order bound is n(n-1)(n-3)/4: the permutation taking one row to another is a derangement of odd order, so it has at most (n-3)/2 transpositions. No claim may exceed it.
- OEIS comments lag the proving lists: a092237_2.txt gives a(23) >= 985 while the comment says 983. Use the larger value.
- An audit recount (2026-10-30, two independent counters) does not reproduce two posted witnesses. The order-17 square in both a092237_2.txt and a307164_5.txt has 272 intercalates, not the 736 in its header. The order-20 square in a307164_5.txt has 1100, not 1500 (A092237's order-20 square does give 1500). The bars stay at the listed 736 and 1500. Recount any posted square before building on it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/latin-max-intercalates.md
```

Already set up? Say `run V3R1T4S on latin-max-intercalates`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `latin-max-intercalates`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
