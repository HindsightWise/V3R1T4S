# Matrices filled with 1..n^2 (Pfoertner's OEIS family): beat a best-known maximal determinant or extremal permanent

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (exact det/permanent of a 7x7 to 10x10 integer matrix takes microseconds to milliseconds; the work is local search over arrangements, which parallelises trivially) · open as of 2026-10-30

## The problem

A family of OEIS entries, curated mostly by Hugo Pfoertner, asks for the extreme value of the determinant or permanent of an n x n matrix whose entries are a fixed multiset arranged freely. Exact values are known only for small n. Above that, the entries record lower bounds (for maxima) or upper bounds (for minima) together with the people who found them. Open cells as of 2026-10-30, from the live entries: (a) A085000, max det using 1..n^2 once each: a(8) >= 440970981670289 and a(9) >= 346260899916111296 (Benjamin R. Buhrow, 2019), and a(10) >= 356948996371054862392 (Richard Gosiorovsky, 2021). The Gasper-Pfoertner-Sigg upper bounds (JIPAM 2009) are 441077015225642, 346335386150480625 and 357017114947987625629. (b) A180128, max det using the first n^2 primes: a(8) >= 154671943501236284416 (Gosiorovsky, 2021), with upper bound 154715716383037989022 (A180127). (c) A350566, max permanent using 1..n^2: a(7) >= 38677691168324 (Pontus von Broemssen, 2025-03-20; earlier 38677620556961 by Robert Israel). (d) A350565, min permanent using 1..n^2: a(7) <= 4755379618016 (von Broemssen, 2025-08-30). (e) A358487, max permanent using 0..n^2-1: a(7) >= 29821721685800 (von Broemssen, 2025-09-03). (f) A301371, max det of the multiset {1^n, ..., n^n}: a(10) has no listed value. The best known arrangement is the noncirculant Latin square of A309985 with determinant 36860608125 (Arthur Queiroz M., 2026-08-06), and the upper bound is A328031(10) = 37180409223. The matrices given in A350565, A350566 and A358487 were recomputed for this entry (exact Ryser permanent) and match the stated values. Each cell is a separate record. The A301371 cell is the free-arrangement problem, not the Latin-square sequence A309985.

## What counts as a win

Success means one explicit n x n integer matrix whose entries are exactly the multiset of the chosen cell, checked by sorting. Its exact determinant (absolute value) or permanent must be computed by two independent programs that agree. The value must be STRICTLY BETTER than the best bound for that cell at verification time: strictly greater for the maximisation cells A085000(8), A085000(9), A085000(10), A180128(8), A350566(7), A358487(7) and A301371(10), strictly smaller for A350565(7). The best bound is the best value in the live OEIS entry (data, comments, b-file, links and pending edits in https://oeis.org/Annnnnn/history), in Pfoertner's linked pages, and in any paper or preprint found by a fresh check, all re-fetched immediately before claiming. A maximum claim above a stated upper bound (Gasper-Pfoertner-Sigg, A180127, A328031) indicates a bug and is not accepted. One cell per claim. Submitting to the OEIS is an action for a human.

## Partial wins

- **p1:** For A350858(7) or A350859(7) (min or max permanent of a 7 x 7 matrix filled with the first 49 primes), for which no bound is published: an explicit matrix whose exact permanent beats the reference value obtained by putting the primes into the rank pattern of the A350565(7) (for the minimum) or A350566(7) (for the maximum) record matrix. The k-th smallest entry is replaced by the k-th prime. The verifier recomputes this reference value.

## How a win is checked

Check that the entries are a permutation of the required multiset. Compute det by fraction-free Bareiss elimination on Python integers and cross-check with sympy or PARI. Compute the permanent by Ryser's formula with Gray-code updates and cross-check with Glynn's formula or a direct expansion (7! = 5040 terms). Compare against the live entry's comments and history. For the maximisation cells, confirm the value does not exceed the published upper bound.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A085000>

## Sources

- <https://oeis.org/A085000>
- <https://oeis.org/A180128>
- <https://oeis.org/A180127>
- <https://oeis.org/A350565>
- <https://oeis.org/A350566>
- <https://oeis.org/A358487>
- <https://oeis.org/A301371>
- <https://oeis.org/A309985>
- <https://oeis.org/A328031>
- <https://oeis.org/A350858>
- <https://oeis.org/A350859>
- <https://arxiv.org/abs/1804.02897>
- <https://www.randomwalk.de/sequences/a085000.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For the determinant cells, the Gasper-Pfoertner-Sigg bound is attained only by matrices whose rows have equal sums and equal sums of squares and are nearly orthogonal after centring. Search near that structure: start from the known record matrices and use pair-swap simulated annealing with exact incremental determinant updates (rank-2 Sherman-Morrison on a float shadow, exact recheck of the finalists).
- For the maximum permanents, the 7 x 7 records are near-'sorted' block patterns (large entries concentrated on one permutation and its neighbours). Try parametrised families (staircase or anti-diagonal sortings, products of sorted vectors) and polish with 2-swaps and 3-cycles.
- For the A301371(10) cell, A309985 and A301371(9) show that free arrangements beat Latin squares at n = 9 (Oleg Vlasii's 2019 matrix). Start from the 36860608125 Latin square and allow non-Latin swaps.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Use exact integers: 10 x 10 determinants of this size exceed 2^64, and floats give spurious records.
- The A085000 comment bounds for n = 8 and 9 superseded the published 2009 bounds. Compare against the best value anywhere in the entry and its history, not against the first number you see.
- A301371 counts the multiset {1^n,...,n^n} (each value n times), not 1..n^2. A309985 (Latin squares only) is a different sequence and a separate record.
- The minimum-permanent cell has direction min.
- Do not run the FORTRAN or other programs linked from the entries. Write your own checkers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/matrix-1-to-n2-extremal-det-perm.md
```

Already set up? Say `run V3R1T4S on matrix-1-to-n2-extremal-det-perm`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `matrix-1-to-n2-extremal-det-perm`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
