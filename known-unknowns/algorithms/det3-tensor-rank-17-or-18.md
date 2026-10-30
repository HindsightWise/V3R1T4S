# Tensor rank of the 3x3 determinant as a 9x9x9 tensor: 17 or 18? (Shitov's Question 11.1)

⚡ **Algorithms** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (numerical CP searches over C with ALS / Levenberg-Marquardt and symmetry ansatzes, then exactification; the exact check takes seconds) · open as of 2026-10-30

## The problem

Let det3 = sum over sigma in S3 of sgn(sigma) x_{1,sigma(1)} x_{2,sigma(2)} x_{3,sigma(3)}, a cubic in the 9 entries of a generic 3x3 matrix, and let T in C^9 (x) C^9 (x) C^9 be its symmetric tensor: T[a,b,c] = sgn(sigma) when {a,b,c} = {(1,sigma(1)),(2,sigma(2)),(3,sigma(3))} as a set of three distinct indices, else 0 (36 nonzero entries, each flattening has rank 9). Conner, Harper and Landsberg (Forum Math. Pi 11 (2023) e17, arXiv:1911.07981) proved its border rank is 17, so rank >= 17. Conner, Gesmundo, Landsberg and Ventura (Comput. Complexity 31 (2022), arXiv:1909.04785) gave an 18-term expression, so rank <= 18. Shitov (viXra:2010.0193, 2020) proved that the Waring (symmetric) rank and the partially symmetric rank are both exactly 18, and left open as his Question 11.1 whether the tensor rank is 17 or 18. A rank of 17 would be a 9x9x9 counterexample to Comon's conjecture (rank = symmetric rank); the smallest known order-3 counterexample is Lovitz's 27x27x27 tensor with rank 55 and symmetric rank 56 (arXiv:2609.28292, Sep 2026), whose survey table lists no smaller one. Earlier history: Waring rank lower bounds 14 (Landsberg-Teitler), 15 (Boij-Teitler 2020). This is NOT the 3x3x3 'determinant tensor' of Krishna-Makam (rank 5), and NOT the Waring rank (settled at 18).

## What counts as a win

Success means an explicit list of 17 triples (u_i, v_i, w_i) of vectors in K^9, where K is Q or a number field given by an explicit minimal polynomial, such that sum_{i=1..17} u_i (x) v_i (x) w_i equals T exactly (all 729 entries, in exact arithmetic), with T built as in the statement (any nonzero rescaling of T is fine; the variable order x_{11},x_{12},...,x_{33} must be stated). Direction: min; the bar is the known upper bound 18, so 17 terms is required. Before claiming, re-read Shitov's paper and Lovitz arXiv:2609.28292 and search arXiv for any later paper settling the rank; a published proof that the rank is 18 makes the target closed, not winnable.

## Partial wins

- **p1:** An exact 17-term decomposition of T over a finite field F_p with p >= 5, checked entrywise mod p (the border-rank lower bound 17 is a statement over C, so this does not settle Question 11.1, but it is a concrete lead for Hensel lifting).
- **p2:** A numerical 17-term decomposition over C with relative Frobenius residual <= 1e-40 after Newton refinement in 60-digit arithmetic, with every factor vector of Euclidean norm <= 100 after balancing the three factors of each term, so that it is not a border-rank degeneration; the residual and norms are recomputed independently with mpmath.

## How a win is checked

Build T from the definition (36 entries of +-1; check nnz = 36 and flattening ranks 9). For the full win, expand the 17 triples with exact arithmetic (SymPy or Sage over Q or the stated number field) and compare all 729 entries with T; confirm the number of terms by counting triples, never from a file name. For p1 do the same mod p. For p2 recompute the residual with mpmath at 60 digits and the per-term balanced norms. Re-fetch the status sources. Seconds to minutes on a laptop.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://vixra.org/pdf/2010.0193v1.pdf>

## Sources

- <https://vixra.org/pdf/2010.0193v1.pdf>
- <https://arxiv.org/abs/1911.07981>
- <https://arxiv.org/abs/1909.04785>
- <https://arxiv.org/abs/2609.28292>
- <https://arxiv.org/abs/1908.08896>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The symmetry group of det3 (X -> AXB with det(AB)=1, transpose, and the S3 permuting the three tensor factors) is large; search for 17-term decompositions invariant under a finite subgroup (for example a Z3 that cycles the tensor factors combined with a matrix symmetry), which shrinks the unknowns a lot.
- Start from the CHL border-rank-17 family and the CGLV 18-term expression and look for a degeneration-free 17-term limit point.
- Search over small finite fields first (SAT or Groebner over F_7, F_13), then Hensel-lift a solution to Q_p and recognise algebraic numbers (LLL).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Shitov proved that the symmetric rank and the partially symmetric rank (sums of terms a (x) a (x) b, symmetric in one fixed pair of modes) are both 18. So no 17-term decomposition can have all its terms symmetric, or all its terms symmetric in the same pair of modes, and ansatzes of that form cannot succeed. Decompositions where only some terms are symmetric are still allowed.
- Border rank is 17, so numerical optimisers reach small residuals with diverging factor norms; such sequences are border decompositions, not rank 17. Check norms (p2) and exactify.
- Different 'det3 tensors' exist: the 3x3x3 alternating tensor has rank 5 (Krishna-Makam); this target is the 9x9x9 tensor of the cubic polynomial.
- Shitov's paper is a viXra preprint; the 17-or-18 range for tensor rank rests on CHL and CGLV alone and does not depend on it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/det3-tensor-rank-17-or-18.md
```

Already set up? Say `run V3R1T4S on det3-tensor-rank-17-or-18`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `det3-tensor-rank-17-or-18`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
