# Erdős #20 small cases (Erdős-Rado sunflower numbers): beat Abbott et al.'s 38 three-sets with no 4-sunflower, 54 four-sets with no 3-sunflower, or 88 three-sets with no 5-sunflower (OEIS A332077)

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Erdős Problem #20 concerns f(m,k), the largest family of m-element sets with no k-sunflower: no k members whose pairwise intersections all equal one common core, which may be empty. Erdős's $1000 prize is for the open asymptotic conjecture f(m,k) < c_k^m, not for these small cases. OEIS A332077 (M. F. Hasler, keyword more) tabulates Sun(m,n) = f + 1 for sets of size at most m. Padding each set with its own new points shows the uniform and 'at most m' versions agree. Known exactly: Sun(1,k) = k, Sun(m,2) = 2, Sun(2,k) by the Abbott-Hanson-Sauer formula (1972), and Sun(3,3) = 21. Three small cells are open, and their lower bounds have stood for decades. Sun(3,4) >= 39: a 38-set 3-uniform family with no 4-sunflower (Abbott-Exoo 1992). Sun(4,3) >= 55: 54 four-sets with no 3-sunflower (Abbott-Hanson-Sauer 1972). Sun(3,5) >= 89: 88 three-sets with no 5-sunflower (Abbott-Hanson 1974). Kyle Wood posted explicit example files for all three in Oct-Nov 2025, and the entry was last edited 2025-11-11. On 2026-10-30 the files were re-checked with an independent SAT-based checker: 38, 54 and 88 distinct sets, with no sunflower of the stated size. The next unknown term of A332077 is Sun(3,4). This is the uniform Erdős-Rado problem, not the Erdős-Szemerédi sunflower-free capacity of subsets of [n] (a separate bank entry).

## What counts as a win

Success means an explicit family F of distinct sets, all of the same size m, containing no k members with pairwise equal intersections (direction: max). It must have |F| >= 39 for (m,k) = (3,4), |F| >= 55 for (4,3), or |F| >= 89 for (3,5). The size must be strictly above the live lower bound Sun(m,k) - 1 shown in https://oeis.org/A332077 and its example files, re-fetched immediately before claiming, and above any value found in a fresh literature check. The verifier checks every possible core C (every proper subset of a member, including the empty set) and confirms that the petals {S \ C : S in F, C ⊆ S} contain no k pairwise disjoint sets. It uses two independent implementations: exhaustive search, and SAT with a cardinality constraint.

## Partial wins

- **p1:** The exact value of one of the three cells, e.g. Sun(3,4) = 39. This needs a complete proof that no larger family exists, with the ground-set reduction written out as checkable lemmas and the computational part ending in LRAT-checked UNSAT certificates or a Lean proof.
- **p2:** An explicit 5-uniform family with no 3-sunflower and more than 160 members, or a 4-uniform family with no 4-sunflower and more than 114 members. These beat the lower bounds f(5,3) >= 160 and f(4,4) >= 114 in the small-values table of the Wikipedia Sunflower article (from Abbott-Hanson-Sauer 1972 and Abbott-Exoo 1992). It counts only if the skeptic finds no larger published value for that cell.

## How a win is checked

For each core C (enumerate all subsets of members), collect the petals of the members containing C and test with two independent methods (backtracking and SAT) whether k pairwise disjoint petals exist. Check uniformity and distinctness. Re-run the checker on Kyle Wood's OEIS files (38, 54, 88 sets) as a positive control, and on a family with an added sunflower as a negative control.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A332077>

## Sources

- <https://www.erdosproblems.com/20>
- <https://oeis.org/A332077>
- <https://en.wikipedia.org/wiki/Sunflower_(mathematics)>
- <https://doi.org/10.1007/BF01271703>
- <https://doi.org/10.1016/0097-3165(72)90103-3>
- <https://doi.org/10.1016/0012-365X(74)90103-4>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Inspect Wood's example files: the 54-set family is a union of two isomorphic 27-set blocks on disjoint 9-point sets, and the 38 and 88 families have visible structure; search for one-set extensions or two-out-three-in swaps with SAT.
- Restrict to families invariant under a group on v points (cyclic, affine AGL(1,p), PSL(2,q)) and solve the orbit-selection problem exactly with SAT, adding sunflower constraints only between orbits.
- Product lemma: if F1 and F2 on disjoint ground sets have no k-sunflower, neither does {A ∪ B}; it gives baselines such as 3·38 = 114 for the 4-uniform 4-petal cell, but beating the p2 bars needs better blocks or non-product constructions.
- Tabu search with incremental conflict counts: for each core C keep the petals and a disjointness structure so a move updates only the cores inside the changed set.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Three pairwise disjoint sets form a 3-sunflower (empty core); forgetting empty cores inflates families.
- OEIS uses Sun = (largest sunflower-free family) + 1 and 'at least n petals'; some papers use f(k,r) for 'more than r'; off-by-one errors are common.
- The $1000 Erdős prize is for the asymptotic conjecture; no small-case record claims it.
- Do not mix this up with sunflower-free capacity on a fixed ground set [n] (non-uniform, a separate bank entry).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-20-sunflower-numbers-small.md
```

Already set up? Say `run V3R1T4S on erdos-20-sunflower-numbers-small`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-20-sunflower-numbers-small`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
