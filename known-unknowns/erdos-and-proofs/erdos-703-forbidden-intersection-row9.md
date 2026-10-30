# Erdős #703 small cases: T(9,2) and T(9,3), the largest family of subsets of a 9-set with no two members meeting in exactly 2 (or 3) elements (OEIS A390645 row 9)

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (exact maximum independent set on 512 vertices per cell, with S_9 symmetry) · open as of 2026-10-30

## The problem

Erdős Problem #703 ($250) concerns T(n,r), the largest family of subsets of {1..n} in which no two distinct members meet in exactly r elements; its asymptotic question was answered by Frankl-Rödl (1987). OEIS A390645 (Elijah Beregovsky, Dec 2025, keyword more; last edited 2025-12-29) tabulates rows n <= 8 by exact maximum-clique search. Row 8 is 128, 94, 67, 93, 163, 219, 247, 255, 256 for r = 0..8. The entry also gives formulas: T(n,0) = 2^(n-1); T(n,1) = A045621(n+1) + 1 (Frankl 1977), so T(9,1) = 187; T(n,n) = 2^n; T(n,n-1) = 2^n - 1; and T(n,n-2) = 2^n - n - 1, so T(9,7) = 502. The b-file stops at T(9,1). Splitting a family by whether it contains the element 9 gives T(9,r) <= T(8,r) + T(8,r-1). The family of all sets of size at most r gives T(n,r) >= C(n,0) + ... + C(n,r). For r = 4, 5, 6 the two bounds meet, so T(9,4) = 256, T(9,5) = 382 and T(9,6) = 466 follow at once from row 8, though they are not yet in the entry. The same argument gives T(10,5) = 638, T(10,6) = 848 and T(10,7) = 968 (checked 2026-10-30). So only T(9,2) and T(9,3) are genuinely open at n = 9. Frankl-Füredi (1984) determined the extremal family for fixed r and large n: all sets of size < r, plus the members A with |A| > (n+r)/2 when n+r is odd, or with |A \ {1}| >= (n+r)/2 when n+r is even. At n = 9 that family has 140 members for r = 2 and 120 for r = 3, while all sets of size at most 3 give 130. So 140 <= T(9,2) <= 161 and 130 <= T(9,3) <= 160. On 2026-10-30, local search on the conflict graph reproduced row 8 but found nothing above 140 and 130. Each cell is a maximum independent set problem on the 512 subsets (conflict when |A ∩ B| = r) with an S_9 symmetry.

## What counts as a win

Success means the exact values of both open cells, T(9,2) and T(9,3), each with two parts. (a) An explicit family of that size (a list of 9-bit masks), checked so that no two distinct members meet in exactly r elements. (b) An optimality certificate the verifier checks independently: either an LRAT/DRAT proof (cake_lpr or drat-trim) of UNSAT for 'a family of size T+1 exists', on a CNF the verifier regenerates from the published encoding, or a VIPR-verified exact ILP certificate. Any symmetry-breaking constraints must be standard lex-leader constraints for S_9 that the verifier regenerates and checks for soundness. The values must not already be in the live https://oeis.org/A390645 entry, its b-file or its history, re-fetched immediately before claiming. T(9,2) must lie in [140, 161] and T(9,3) in [130, 160]; a value outside its range means a bug. The forced values T(9,4) = 256, T(9,5) = 382 and T(9,6) = 466 do not count.

## Partial wins

- **p1:** The exact value of T(9,2) or T(9,3), with a family and an optimality certificate as in the success criterion; each cell counts separately.
- **p2:** The exact value, with the same certificate standard, of T(10,2), T(10,3) or T(10,4). Their bounds are [271, 348], [232, 321] and [386, 416]. The other cells of row 10 follow from the A390645 formulas or from the size-at-most-r bound (T(10,5..7) = 638, 848, 968), so they do not count.

## How a win is checked

Check family sizes and all pairwise intersection sizes with popcount on 9-bit masks (at most 512^2/2 pairs). Rebuild the CNF or ILP from the published encoding, rerun it, and check the LRAT proof or VIPR certificate with an independent checker. Reproduce row 8 of A390645 with the same pipeline as a sanity test. Re-fetch the OEIS entry and history before confirming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A390645>

## Sources

- <https://www.erdosproblems.com/703>
- <https://oeis.org/A390645>
- <https://oeis.org/A390645/b390645.txt>
- <https://doi.org/10.1016/0097-3165(84)90008-6>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reproduce row 8 first with an exact max-clique solver (MoMC, CliSAT) on the complement graph, then inspect the n = 8 optima for structure (unions of size layers, stars at a point) to seed n = 9.
- Use the decomposition F = F0 ∪ (F1 + {9}) with F0 avoiding r and F1 avoiding r-1 on [8], plus cross constraints between F0 and F1; branch over the size profile of F0 and F1.
- Orbit-ILP: aggregate subsets by size and by intersection with a fixed small set, solve the symmetric relaxation for an upper bound, then close the gap with symmetry-broken SAT and cardinality constraints.
- Lower bounds: tabu or simulated annealing on the 512-vertex conflict graph, seeded with the Frankl-Füredi family and with doublings of the n = 8 optima.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Convention: OEIS forbids |A ∩ B| = r only for distinct A, B (so T(n,n) = 2^n); the erdosproblems wording 'for all A, B' would also forbid r-sets. Use the OEIS convention.
- Triangle indexing: row n has n+1 entries, and b-file index 45 is T(9,0) = 256, so the open b-file indices are 47 = T(9,2) and 48 = T(9,3).
- T(9,4), T(9,5) and T(9,6) (256, 382, 466) and T(10,5..7) (638, 848, 968) follow from the rows above them: the split bound T(n,r) <= T(n-1,r) + T(n-1,r-1) is met by the family of all sets of size <= r. Computing them is not a win.
- Complementation does not preserve intersection sizes, so it is not a symmetry of the problem; only S_9 acts.
- Unsound symmetry breaking gives a wrong 'optimum'; the verifier must be able to regenerate and justify every symmetry-breaking clause.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-703-forbidden-intersection-row9.md
```

Already set up? Say `run V3R1T4S on erdos-703-forbidden-intersection-row9`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-703-forbidden-intersection-row9`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
