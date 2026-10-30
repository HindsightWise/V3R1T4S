# Ternary Kerdock set of 6x6 matrices: 243 skew-symmetric matrices over GF(3) with all pairwise differences nonsingular

📊 **Record tables** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for search (clique of size 243 in a Cayley graph on 3^15 skew matrices); verification instant · open as of 2026-10-30

## The problem

For even m, an m-dimensional Kerdock set over F_q is a set of q^(m-1) skew-symmetric m x m matrices such that the difference of any two is nonsingular. Such a set is equivalent to a spread of the hyperbolic quadric Omega^+(2m,q), a 1-(m,m,1) design in the Kiermaier-Schmidt-Wassermann notation. Kerdock sets exist for all m when q is even (Kantor). For odd q, existence for m >= 6 is open, as stated in Kiermaier, Schmidt and Wassermann, 'Designs in finite classical polar spaces' (DCC 2025; arXiv:2403.11188v3, Oct 2025). They also showed by computer that the automorphism group of any 1-(6,6,1) design in Omega^+(12,3) has order 1, 2, 3, 4, 5, 6 or 8. Kantor (Ann. Discrete Math. 18 (1983), 511-518) wrote that hyperbolic spreads seem unlikely to exist in PG(2n-1,q) for n > 4 and q odd, which includes this case, so experts expect nonexistence; a construction would overturn that expectation. The smallest open case is m = 6, q = 3: 3^5 = 243 matrices in the 15-dimensional space of skew-symmetric 6 x 6 matrices over GF(3). Without loss of generality the set contains 0, so it is a clique in the Cayley graph whose connection set is the nonsingular skew matrices (nonzero Pfaffian). 243 is also the maximum possible size, so a 243-set is a Kerdock set.

## What counts as a win

Give 243 distinct 6 x 6 matrices over GF(3) that are skew-symmetric (A^T = -A, zero diagonal) and such that det(A_i - A_j) != 0 mod 3 for all 29403 pairs i < j. Alternatively, give an explicit spread of the hyperbolic quadric Q^+(11,3) (244 totally singular 6-spaces partitioning its singular points) in a stated form, from which the Kerdock set is derived and checked. Direction: settle an existence question open on 2026-10-30.

## Partial wins

- **p1:** Removal of one order r in {2,3,4,5,6,8} from the Kiermaier-Schmidt-Wassermann list. This is a published, rerunnable exhaustive computer search proving that no 1-(6,6,1) design in Omega^+(12,3) has an automorphism group of order r, for example by showing that no such design is invariant under any subgroup of order r of the quadric's collineation group, taken up to conjugacy. Code and orbit data are released, and the verifier reruns the search, or an independent reimplementation, to the same conclusion.

## How a win is checked

Parse the matrices, check entries in {0,1,2}, skew-symmetry, zero diagonal and distinctness. Compute det(A_i - A_j) mod 3 exactly by Gaussian elimination over GF(3), or the Pfaffian squared, for all pairs and require nonzero. Expect 29403 determinant evaluations, under a second. For the spread form, check total singularity, dimensions and the exact partition of the points.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2403.11188>

## Sources

- <https://arxiv.org/abs/2403.11188>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search sets invariant under a small allowed group (orders 2-8), which reduces the clique problem to orbits.
- Additive sets are ruled out. An F_3-additive Kerdock set would be a 5-dimensional subspace on which the Pfaffian, a cubic form, has no nontrivial zero, and Chevalley-Warning forbids that (5 variables > degree 3). So look at nonadditive sets, for example unions of cosets of large additive partial sets, or sets with additive structure over a subring or in a twisted coordinate system.
- Use the spread picture in Q^+(11,3) together with known spreads of Q^+(7,3) (which exist for q = 3 via triality) and look for lifting constructions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Nonsingular means determinant nonzero mod 3. Skew-symmetric matrices of odd size are always singular, so m must be 6.
- 243 is the maximum, so a claimed 244-set is a bug.
- Kerdock sets for q even, and the m = 4 case for q = 3 (from spreads of Q^+(7,3)), are known and do not count; only m = 6, q = 3 is the target.
- Kantor (1983) expected that no such spread exists for n > 4 and q odd. A long search that finds nothing is the likely outcome, and a nonexistence argument counts only through p1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/kerdock-set-ternary-m6.md
```

Already set up? Say `run V3R1T4S on kerdock-set-ternary-m6`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kerdock-set-ternary-m6`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
