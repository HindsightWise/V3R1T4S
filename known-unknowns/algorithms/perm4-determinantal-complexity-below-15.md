# Determinantal complexity of the 4x4 permanent: a determinantal expression smaller than Grenet's 15 x 15

⚡ **Algorithms** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (structured search over affine matrices with SAT/Groebner on small patterns; the exact check takes minutes) · open as of 2026-10-30

## The problem

A determinantal expression of size m for a polynomial f in variables x_1..x_k is an affine linear map L into m x m matrices with det(L(x)) = f(x) identically; dc(f) is the least such m. Valiant's permanent-versus-determinant conjecture says dc(per_n) grows superpolynomially. Small cases: Grenet (2011) turned a 2^n-vertex algebraic branching program into expressions of size 2^n - 1 for every n (characteristic other than 2), with entries in {x_ij} and the constants -1, 0, 1, so dc(per_4) <= 15. Huttenhain and Ikenmeyer (arXiv:1410.8202, Theorem 1.3 and Lemma 6.2) note that swapping two rows fixes the sign, so size 2^n - 1 is reached with the constants 0 and 1 alone. Mignon and Ressayre (2004) proved dc(per_n) >= n^2/2 in characteristic 0 (Cai, Chen and Li extended a quadratic bound to characteristic other than 2). Alper, Bogart and Velasco (Found. Comput. Math., arXiv:1505.02205) proved dc(f) >= codim Sing(f) + 1 when that codimension is at least 5 and deduced dc(per_3) = 7 and dc(per_4) >= 9 (characteristic other than 2), noting that 8 <= dc(per_4) <= 15 was the state before their work. Yabe (arXiv:1504.00151, not refereed) claims dc(per_n) >= (n-1)^2 + 1 over the reals, which would give >= 10 for expressions over Q. Huttenhain and Ikenmeyer (Linear Algebra Appl. 504 (2016)) showed 7 is also optimal for per_3 with entries in {0, 1, variables} and wrote that the binary case for per_4 is out of reach of their enumeration. Landsberg and Ressayre proved Grenet's expressions optimal among determinantal representations that respect left multiplication by permutation and diagonal matrices (roughly half the symmetry group of the permanent), so a smaller expression for n = 4 must break that symmetry. A check on 2026-10-30 of papers citing Alper-Bogart-Velasco and Huttenhain-Ikenmeyer found no improvement: 9 <= dc(per_4) <= 15 (at least 10 over the reals if Yabe's bound holds).

## What counts as a win

Success means an explicit m x m matrix L(x) with m <= 14 whose entries are affine linear forms over Q (or a number field given by an explicit minimal polynomial) in the 16 variables x_ij, such that det L(x) = per_4(x) as polynomials, verified by exact symbolic expansion (direction: min; the bar is Grenet's 15). Before claiming, search arXiv and the GCT literature for any published determinantal expression of per_4 of size below 15; a smaller published size becomes the bar.

## Partial wins

- **p1:** An expression of size <= 14 for per_4 over a finite field F_p with p >= 3, with det L(x) = per_4(x) verified as polynomials over F_p.
- **p2:** An expression of size <= 2^n - 2 for per_n for some n >= 5 (for n = 5, size <= 30) over Q, verified exactly.

## How a win is checked

Parse L as a matrix of affine forms. Screen with random evaluations: compare det L(x) with per_4(x) at 50 random integer points mod several 61-bit primes. Then confirm exactly: compute det L(x) symbolically (Bareiss or Berkowitz in SymPy/Sage/Singular over Q[x_11..x_44], or over F_p[x] for p1), expand, and compare with the 24-term per_4. Calibrate on Grenet's 15 x 15 construction, which must pass. Report m from the matrix. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://sites.math.washington.edu/~jarod/papers/determinantal-complexity.pdf>

## Sources

- <https://sites.math.washington.edu/~jarod/papers/determinantal-complexity.pdf>
- <https://arxiv.org/abs/1505.02205>
- <https://membres-ljk.imag.fr/Bruno.Grenet/publis/Gre11.pdf>
- <https://arxiv.org/abs/1410.8202>
- <https://people.tamu.edu/~jml//LRpermdet8-4.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Grenet's matrices are adjacency matrices of layered graphs over subsets; search non-equivariant graph shapes (ABP-like digraphs with fewer vertices, allowing constants other than 0 and 1) with SAT over F_3 first.
- Huttenhain-Ikenmeyer enumerated bipartite graphs for per_3; extend their enumeration with pruning to size 13-14 patterns for per_4.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Characteristic 2 is trivial (per = det there); claims must be in characteristic 0 for the full win and odd characteristic for p1.
- Random evaluation is only a screen; the claim needs an exact symbolic identity.
- Grenet's 15 x 15 matrix for n = 4 uses the constant -1; swapping two rows gives a 15 x 15 matrix with constants 0 and 1 only (Huttenhain-Ikenmeyer, Lemma 6.2). The bar is 15 either way; Grenet's 16 x 16 0/1 variant is not the calibration target.
- Over Q or any real field, Yabe's claimed bound (n-1)^2 + 1 rules out sizes below 10 for per_4; do not spend search on m <= 9.
- Representations that respect left multiplication by permutation and diagonal matrices cannot beat Grenet (Landsberg-Ressayre); ansatzes with that symmetry waste time.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/perm4-determinantal-complexity-below-15.md
```

Already set up? Say `run V3R1T4S on perm4-determinantal-complexity-below-15`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `perm4-determinantal-complexity-below-15`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
