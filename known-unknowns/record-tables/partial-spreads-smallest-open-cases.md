# Maximum partial spreads: settle 129 <= A_2(11,8;4) <= 132 or 244 <= A_3(8,6;3) <= 248

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (ILP with prescribed automorphisms or exhaustive structure search) · open as of 2026-10-30

## The problem

A partial k-spread in F_q^n is a set of k-dimensional subspaces pairwise intersecting trivially; A_q(n,2k;k) is its maximum size. For q = 2 all values with n < 11 are known and the smallest undecided binary case is 129 <= A_2(11,8;4) <= 132 (stated by Heinlein, Kiermaier, Kurz and Wassermann, arXiv 1708.06224; the bound is the t = 2 case of the family 2^4 l + 1 <= A_2(4t+3,8;4) <= 2^4 l + 4 from Kurz, Packing vector spaces into vector spaces, 2017, restated in Kurz's survey arXiv 2112.11766, v3 2025-12-20, Section 4.3). For q = 3 the smallest open case is 244 <= A_3(8,6;3) <= 248 (Honold, Kiermaier and Kurz 2018; restated by Kurz, arXiv 2302.08939, and the survey says A_q(8,6;3) is known only for q = 2). If 248 planes exist the 56 uncovered points must form the Hill cap.

## What counts as a win

Either (a) an explicit partial spread beating a lower bound: at least 130 four-dimensional subspaces of F_2^11 pairwise intersecting in {0}, or at least 245 three-dimensional subspaces of F_3^8 pairwise intersecting in {0} (direction: max, strictly above 129 resp. 244); or (b) a machine-checkable proof lowering an upper bound (A_2(11,8;4) <= 131 or A_3(8,6;3) <= 247), e.g. an exhaustive search certificate (DRAT/LRAT or VIPR) with an independently audited encoding, or a formal proof.

## Partial wins

- **p1:** An improved lower bound for any other open partial spread value listed in Section 4.3 of arXiv 2112.11766 (for example A_2(6t+4,12;6) or A_2(6t+5,12;6) for the smallest t = 2, currently 1025 <= A_2(16,12;6) <= 1032 and 2049 <= A_2(17,12;6) <= 2066): an explicit partial spread strictly larger than the stated lower bound q^k l + 1 for that family and parameter t, and strictly larger than the Bayreuth table cell (live, or its newest web.archive.org snapshot if the site is unreachable) and any newer published value, verified as in the full criterion.

## How a win is checked

For each subspace compute its full point set (15 points for q=2,k=4; 13 for q=3,k=3), assert rank k, and check that all point sets are pairwise disjoint. Upper-bound claims: re-run the certificate checker and audit the encoding. Re-read the survey's Section 4.3 and recent literature before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2112.11766>

## Sources

- <https://arxiv.org/abs/1708.06224>
- <https://arxiv.org/abs/2112.11766>
- <https://arxiv.org/abs/2302.08939>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Holes of a partial k-spread form a q^(k-1)-divisible point set: enumerate admissible hole sets (e.g. 2^3-divisible sets of 2047-15M points for A_2(11,8;4)) and solve the packing problem on their complement.
- Prescribe Singer-subgroup or normalizer automorphisms to shrink the ILP.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Lower bound 129 = 2^4*8+1 comes from the standard Echelon-Ferrers type construction; plain greedy or random searches usually land well below it.
- For A_3(8,6;3) the trivial bound is 252; 248 comes from divisible-code arguments, so do not report 248..252 as an improvement.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/partial-spreads-smallest-open-cases.md
```

Already set up? Say `run V3R1T4S on partial-spreads-smallest-open-cases`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `partial-spreads-smallest-open-cases`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
