# Superpatterns: the shortest permutation containing all 5040 patterns of length 7 (OEIS A342474(7)), or the next row of A373778

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-hours for upper-bound searches (annealing over length-22 permutations, C(22,7) = 170,544 subsets per evaluation); laptop-days or more for an exhaustive lower-bound proof · open as of 2026-10-30

## The problem

A k-superpattern is a permutation containing every permutation of length k as a pattern (not necessarily contiguous). Its minimum length (OEIS A342474) is known only for k <= 6: 1, 3, 5, 9, 13, 17. Michael Engen and Vincent Vatter ('Containing all permutations', Amer. Math. Monthly 2021) gave the best general construction, length ceil((k^2+1)/2), and reported that Arnar Arnarson found a 6-superpattern of length 17 and computations show none is shorter. Asymptotically the bounds are 1.000076 k^2/e^2 (Zachary Chroman, Matthew Kwan, Mihir Singhal 2021) and about k^2/2. For k = 7 the published upper bound is 25, and A342474 (keyword 'more') has no a(7) on 2026-10-30. A V3R1T4S bank check on 2026-10-30 found, by about six minutes of simulated annealing, a 7-superpattern of length 23, 3 10 20 14 6 17 23 13 2 8 18 12 5 21 16 1 19 7 11 9 22 4 15 (independently re-verified: all 5040 patterns occur among its C(23,7) = 245,157 subsequences), and two 25-minute runs at length 22 reached at best 5030 of 5040 patterns, so 23 is the baseline here. The related triangle A373778 (Thomas Scheuerle 2024; maximum number of distinct length-k patterns in a length-n permutation, with T(n,k) = k! exactly when n >= A342474(k)) is known for rows n <= 12.

## What counts as a win

Success means determining A342474(7) exactly: an explicit 7-superpattern of length L (L <= 23 is already known, see statement) together with a re-runnable exhaustive computer proof that no permutation of length L - 1 contains all 5040 patterns of length 7, where the proof's search code is independent of any heuristic and its pruning rules are each justified in writing. Before claiming, re-check A342474, A373778 and arXiv for a published value.

## Partial wins

- **p1:** An explicit permutation of length at most 22 containing all 5040 permutations of length 7 as patterns (strictly shorter than the length-23 baseline in the statement and the published bound 25).
- **p2:** A re-runnable exhaustive proof that no permutation of length L contains all 5040 patterns of length 7, for some stated L >= 15 (the counting bound C(L,7) >= 7! only rules out L <= 14); the larger L, the stronger, and L = a(7) - 1 is the full win.
- **p3:** Row n = 13 of OEIS A373778 (the maximum, over all permutations of length 13, of the number of distinct length-k patterns, for every k = 1..13), computed exhaustively by two independent programs that both reproduce rows 1..12.

## How a win is checked

For an explicit superpattern: check it is a permutation of 1..L, enumerate all C(L,7) subsets, map each to its pattern, and confirm 5040 distinct patterns (seconds). For an impossibility proof: rerun the claimant's search, audit each pruning rule (symmetry under the 8-element dihedral group of the square, Erdos-Szekeres-type necessary conditions, extension arguments) on small cases, and confirm it reproduces 'no 6-superpattern of length 16' (Engen-Vatter) and the k <= 5 values before trusting it at k = 7. For p3, brute force rows n <= 10 and compare with the OEIS data.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A342474>

## Sources

- <https://oeis.org/A342474>
- <https://oeis.org/A373778>
- <https://oeis.org/A371822>
- <https://arxiv.org/abs/1810.08252>
- <https://arxiv.org/abs/2004.02375>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The good small superpatterns look like rank orders of {i * phi mod 1} (Scheuerle's A371822 rows match A194832 up to cyclic shift); seed searches with golden-ratio and other low-discrepancy permutations.
- For lower bounds, use a SAT/ILP formulation with symmetry breaking that shows every length-L permutation misses some 7-pattern, rather than enumerating L! permutations.
- Use inductive constraints from 6-superpatterns: the length-17 6-superpatterns can be enumerated and constrain how a short 7-superpattern can look after deleting a point.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Patterns here are classical (any subsequence), not consecutive; the substring version is the superpermutation problem, a different bank entry.
- Annealing scores near 5039/5040 at length 22 do not show 22 is impossible; only an exhaustive proof does.
- Symmetry reduction by reverse, complement and inverse is valid because the set of all k-permutations is closed under them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/superpatterns-seven-exact-length.md
```

Already set up? Say `run V3R1T4S on superpatterns-seven-exact-length`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `superpatterns-seven-exact-length`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
