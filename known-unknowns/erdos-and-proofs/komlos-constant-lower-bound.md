# Komlos discrepancy constant C_24: a finite matrix with unit-norm columns whose discrepancy beats Kunisky's 1 + sqrt(2)

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours (an exact discrepancy check is 2^n sign vectors for n nonzero columns, so n <= 30 takes minutes with bit-parallel Gray-code code; the search over real matrices is the expensive part) · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 24: for a real matrix A let disc(A) = min over x in {-1,1}^n of ||Ax||_inf. K_n is the supremum of disc(A) over n x n real matrices whose columns all have Euclidean norm at most 1, and C_24 = sup_n K_n. Zero rows and zero columns do not change disc, so any m x n matrix can be padded to a square one. The Komlos conjecture, that C_24 is finite, was proved in September 2026 by S. Guo, E. X. Fang and J. Lu (arXiv:2609.11189). S. R. Karingula and S. Lovett (arXiv:2609.20979) gave an elementary proof with C_24 <= 36, formalised in Lean by G. Dahia. E. Akbas and S. Sra (arXiv:2609.27172v2) claim 6.9013 (starred as unverified on the page). The lower side has not moved since D. Kunisky (SIAM J. Discrete Math. 37(2) 2023, arXiv:2111.02974) showed C_24 >= 1 + sqrt(2) ~ 2.41421. His bound is a limit: it uses a family of matrices built by scaling clause-variable matrices of unsatisfiable Boolean formulas through a second-order cone program, and their discrepancy approaches 1 + sqrt(2). Guo-Fang-Lu describe it the same way. The page asks whether C_24 = 1 + sqrt(2). On 2026-10-30 the live page (constants/24a, last changed 2026-10-22) still lists 1 + sqrt(2) as the best lower bound, and no open pull request touches constant 24. A single explicit finite matrix with discrepancy strictly above 1 + sqrt(2) would be the first improvement since 2021 and would refute the natural guess that the constant equals 1 + sqrt(2).

## What counts as a win

Success means an explicit real matrix A with m rows and n nonzero columns, saved as a file. Its entries must be rationals, or exact elements of a stated real quadratic field. Every column must have squared Euclidean norm <= 1, checked exactly. Its exact discrepancy d = min over all 2^n sign vectors x of max_i |(Ax)_i| must be computed by exhaustive enumeration in exact arithmetic by two independently written programs that agree. d must be STRICTLY GREATER (direction: max) than 1 + sqrt(2), checked exactly as d > 1 and (d - 1)^2 > 2. It must also be strictly greater than the largest lower bound on the live page https://teorth.github.io/optimizationproblems/constants/24a.html, in any open pull request touching constants/24a.md at https://github.com/teorth/optimizationproblems/pulls, and in any paper or preprint found by a fresh literature check (arXiv, and works citing Kunisky arXiv:2111.02974), all re-fetched immediately before claiming. Proposing the bound to the repository is an action for a human.

## Partial wins

- **p1:** An explicit matrix with at most 15 nonzero columns, rational entries and every column of squared Euclidean norm <= 1 (checked exactly), whose exact discrepancy (exhaustive over all 2^n sign vectors in exact arithmetic, two independent programs) is at least 2. For reference: Kunisky's tree matrices (arXiv:2111.02974, Theorem 1.1, K(2^k) >= 2^{-k/2} + sum_{a=1..k} 2^{-a/2}) first certify a value above 2 at 16 columns (K(16) >= 2.0607). The only smaller example reported there is D. Spielman's unpublished 15-column matrix with discrepancy in [2.005, 2.006].
- **p2:** An explicit matrix with at most 15 nonzero columns, under the same exactness rules as p1, whose exact discrepancy is strictly greater than 2.006, the upper end of the interval reported for Spielman's unpublished 15-column example in Kunisky (arXiv:2111.02974, Section 1).

## How a win is checked

Parse the matrix as exact rationals (Python Fraction or integers after clearing a common denominator) and check sum_i a_ij^2 <= 1 for every column j. Enumerate sign vectors in Gray-code order, fixing x_1 = +1 by symmetry and updating Ax incrementally. Record the minimum over x of the maximum absolute row sum. Recompute it with a second program in another language or by another method, for example an exact branch-and-bound whose optimum is re-checked by direct evaluation. Compare exactly: d > 1 and (d-1)^2 > 2. Re-fetch the 24a page and its open PRs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/24a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/24a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/24a.md>
- <https://arxiv.org/abs/2111.02974>
- <https://arxiv.org/abs/2609.11189>
- <https://arxiv.org/abs/2609.20979>
- <https://arxiv.org/abs/2609.27172>
- <https://github.com/teorth/optimizationproblems/pulls>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Kunisky's construction: take the clause-variable sign matrix of an unsatisfiable CNF, then choose the row and column scalings by a second-order cone program. His family approaches 1 + sqrt(2) from below. Try formulas with richer structure (Tseitin formulas on expanders, pigeonhole, random unsatisfiable 3-CNF near threshold) and re-optimise the scaling for each.
- Use an LP or SOCP inside local search: fix the set of sign vectors that each row is responsible for covering, maximise the common margin over the entries subject to the column-norm constraints, recompute the exact discrepancy, and reassign. This is the same max-min game used for Spencer's C_10c records.
- Nikolov showed that the vector-colouring relaxation is at most 1 for Komlos instances, so a good matrix must exploit integrality. Search for matrices whose SDP value is low but whose sign discrepancy is high, as integrality-gap instances.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point entries: a column norm of 1.0000001 or a rounded discrepancy voids the claim. Use exact rationals throughout.
- The constraint is on columns (the vectors being signed), not rows. Normalising rows gives a different problem (Spencer-type).
- Sampling sign vectors overestimates the discrepancy. Every one of the 2^n vectors must be checked.
- Kunisky's bound is a supremum. A finite matrix that matches 1 + sqrt(2) to many digits but not strictly is not a win.
- Kunisky's Theorem 4.1 (arXiv:2111.02974, Section 4): any matrix obtained by scaling the clause-variable matrix of a formula with a read-once resolution refutation (every tree / MU(1) formula among them) has certified value strictly below 1 + sqrt(2), and his Conjecture 4.4 says the same for every unsatisfiable-matrix certificate. Re-optimising tree formulas cannot win; use formulas without read-once refutations, or matrices whose discrepancy is not certified by unsatisfiability alone.
- The page and its pull requests move. Compare against the live maximum, not the number in this entry.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/komlos-constant-lower-bound.md
```

Already set up? Say `run V3R1T4S on komlos-constant-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `komlos-constant-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
