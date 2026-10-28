# APN functions: a new CCZ-inequivalent APN function (or APN permutation) in dimension 9 or 10

🗝️ **Crypto math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

An (n,n)-function F is APN if every derivative equation F(x+a)+F(x)=b (a!=0) has at most 2 solutions. CCZ classes are classified only for quadratic n<=7. In dimension 8, Beierle, Langevin, Leander, Polujan and Rasoolzadeh (arXiv:2508.04644, v2 2026-08-27) constructed 3,775,599 inequivalent quadratic APN functions (32,892 were known before; they estimate about six million), and Kuznetsov (arXiv:2606.11967, June 2026) reports four further classes. In dimensions 9 and 10 only the infinite families plus a modest number of sporadic quadratic instances are known: Beierle and Leander (IEEE TIT 2022, arXiv:2009.07204) found 35 new quadratic APN functions in dimension 9 (two of them APN permutations) and 5 in dimension 10; Yu, Kaleyski, Budaghyan and Li classified quadratic APN functions with coefficients in F2 up to n = 9, and Yu, Li, Ichanska and Kaleyski (IACR ePrint 2024/1778) did so for n = 10. The UiB Boolean Functions wiki lists CCZ-inequivalent representatives from the known families up to n = 11 and only one APN function CCZ-inequivalent to quadratics and monomials (in dimension 6). APN permutations are known only from monomials in odd n, one quadratic family in dimension 3k, Dillon's dimension-6 permutation and the two sporadic quadratic permutations in dimension 9. Finding a further CCZ class in n = 9 or 10 is checkable from a lookup table plus CCZ invariants. Dimension 11 with coefficients in F2 is the separate bank target binary-coefficient-apn-dimension-11.

## What counts as a win

Success means a lookup table (or polynomial with a stated irreducible modulus) F over GF(2^n), n in {9,10}, such that (1) an independent script confirms differential uniformity exactly 2 by exhaustive count over all a!=0 and all b; (2) at least one CCZ invariant, computed exactly (extended Walsh spectrum, Gamma-rank or Delta-rank, or for quadratic F the differential and extended Walsh spectra of the ortho-derivative), takes a value for F that differs from its value for: every representative listed on https://boolean.wiki.uib.no/Tables and its linked pages (re-fetched live immediately before claiming); EVERY instance (not only the wiki's representatives) of every known infinite APN family in dimension n, including the family C11 instances in dimension 10 that the wiki says have not all been checked; every function in the published datasets of Yu-Kaleyski-Budaghyan-Li (IACR ePrint 2019/1491, F2 coefficients up to n = 9), Beierle-Leander (IEEE TIT 2022) and Yu-Li-Ichanska-Kaleyski (ePrint 2024/1778); and every function in any other arXiv or ePrint dataset for that n, of any date; with the verifier recomputing the invariant for F and for every compared function; (3) a literature search on arXiv/ePrint for that n finds no prior instance with the same invariants. A failed equivalence search, a different truth table or the output of a heuristic classifier is not a certificate of inequivalence.

## Partial wins

- **p1:** A new APN permutation in dimension 9 CCZ-inequivalent to monomials, the 3k-family and both Beierle-Leander sporadic permutations (verified bijectivity + APN + distinguishing invariant).
- **p2:** A new quadratic APN function in dimension 10 whose ortho-derivative differential spectrum differs from all known dim-10 instances in the wiki tables and published datasets (including the F2-coefficient classification of ePrint 2024/1778).
- **p3:** A new CCZ class of APN functions in dimension 8 that is neither CCZ-equivalent to a quadratic function nor to a monomial (the wiki's list of APN polynomials CCZ-inequivalent to quadratic functions and monomials has a single entry, in dimension 6, and none in dimension 8). Certificate: (i) the extended Walsh spectrum of F contains a nonzero absolute value that is not a power of 2, which no function CCZ-equivalent to a quadratic one can have (quadratic components are plateaued with power-of-two amplitudes), and (ii) an exactly computed CCZ invariant of F differs from that of every APN power function in dimension 8 (the Gold functions and the Kasami function x^57).

## How a win is checked

Python/numpy or C: exhaustive differential table (2^n x 2^n counts, n<=11 is 4M cells, seconds). Walsh spectrum via fast Walsh-Hadamard of each component. Ortho-derivative for quadratic F: for each a, the unique pi(a) with pi(a).(F(x)+F(x+a)+F(a)+F(0))=0; compute its differential and extended Walsh spectra as CCZ invariants and compare to invariants recomputed from the known lists. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://boolean.wiki.uib.no/Tables>

## Sources

- <https://boolean.wiki.uib.no/Tables>
- <https://boolean.wiki.uib.no/APN_Permutations>
- <https://boolean.wiki.uib.no/CCZ-inequivalent_representatives_from_the_known_APN_families_for_dimensions_up_to_11>
- <https://boolean.wiki.uib.no/APN_polynomials_over_GF(2%5En)_CCZ-inequivalent_to_quadratic_functions_and_monomials>
- <https://arxiv.org/abs/2009.07204>
- <https://eprint.iacr.org/2019/1491>
- <https://eprint.iacr.org/2024/1778>
- <https://arxiv.org/abs/2508.04644>
- <https://arxiv.org/abs/2606.11967>
- <https://github.com/lpp-crypto/sboxU>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Beierle-Leander self-equivalence search: fix a linear self-equivalence (e.g. cyclotomic x -> a x or Frobenius-like) and search quadratic APN with that symmetry via a recursive tree over coordinate bilinear forms; dim 9 with a degree-3 extension structure is the sweet spot.
- QAM (quadratic APN matrix) method of Yu-Wang-Li: search symmetric matrices over GF(2^n) with the QAM rank property; prune by subspace counting.
- Switching neighbours: F + f(x)*u for Boolean f, starting from known dim-9/10 instances (Edel-Pott switching), keeping APN with incremental derivative checks.
- Cross-domain import (SAT/constraint programming from hardware verification): encode quadratic APN as bilinear-form constraints with symmetry breaking (CCZ canonical forms) and use CaDiCaL/kissat with cube-and-conquer across 10 cores.
- Cross-domain import (coding theory/ graph isomorphism tools from chemistry): use canonical labelling (nauty/bliss) of the associated design/code to decide CCZ inequivalence quickly, like molecule deduplication in chemical databases.
- Cross-domain import (evolutionary program synthesis): evolve small polynomial expressions over GF(2^n) (few terms, coefficients) with APN-ness as hard filter and novelty (distance in invariant space) as fitness, MAP-Elites style.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The wiki's dimension-8 instance list is far behind the literature (millions of quadratic classes in arXiv:2508.04644 and its Zenodo data, more in arXiv:2606.11967); any 'new' dim-8 claim must be checked against those datasets. Prefer n = 9 or 10.
- Same invariant does not prove equivalence, but DIFFERENT invariants prove inequivalence; the claim must rest on a differing invariant, not on failing to find an equivalence.
- EA-inequivalence is not CCZ-inequivalence; compositions with permutations' inverses can be CCZ-equivalent to known functions.
- Field-representation bugs: the lookup table must be with respect to a stated primitive polynomial; recompute everything from the table, not from the polynomial.
- A function that is APN only on a subset or with off-by-one counting (counting a=0) is the classic false positive.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/crypto-math/apn-new-ccz-class-dim9-10.md
```

Already set up? Say `run V3R1T4S on apn-new-ccz-class-dim9-10`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `apn-new-ccz-class-dim9-10`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
