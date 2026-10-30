# Bivariate bicycle codes: prove the exact distance of IBM's [[360,12,<=24]] or [[756,16,<=34]] code (only upper bounds are published)

⚛️ **Physics** · standard · tractability ★★★☆☆ · compute: laptop-days (exhaustive anchored cluster search at radius 23 for n = 360, parallel over anchors and branches); [[756,16]] likely needs a cluster · open as of 2026-10-30

## The problem

Bivariate bicycle (BB) codes are weight-6 quantum LDPC codes; IBM's [[144,12,12]] gross code is the best-known example. They are defined by x and y, the commuting cyclic shifts on Z_l x Z_m; A = A1+A2+A3 and B = B1+B2+B3, sums of monomials; and check matrices H_X = [A|B] and H_Z = [B^T|A^T]. The family is due to Sergey Bravyi, Andrew W. Cross, Jay M. Gambetta, Dmitri Maslov, Patrick Rall and Theodore J. Yoder (Nature 627, 778 (2024), arXiv:2308.07915). Their Table 3 gives distances computed by mixed integer programming up to [[288,12,18]]. For the two largest examples it gives only upper bounds: [[360,12,<=24]] (l = 30, m = 6, A = x^9+y+y^2, B = y^3+x^25+x^26) and [[756,16,<=34]] (l = 21, m = 18, A = x^3+y^10+y^17, B = y^5+x^3+x^19). Benjamin C. B. Symons, Abhishek Rajput and Dan E. Browne (arXiv:2511.13560, v3 6 Aug 2026) built sequences of covering BB codes. They obtained exact MIP distances only up to d = 14 and used BP-OSD upper bounds above that, for example [[432,12,<=24]] (l = 18, m = 12, A = x^15+y^7+y^2, B = y^9+x^7+x^14) and [[504,12,<=30]] (l = 42, m = 6, A = x^27+y+y^2, B = y^3+x^37+x^38). Mohammad Rowshan and Simon Devitt (arXiv:2609.39395, v2 1 Oct 2026) proved all six standard BB distances up to [[288,12,18]] with an anchored cluster search; the 288 case took 455,504,708 nodes at radius 17. The README of their public tool reports bounds 18 <= d <= 30 for the [[360,12]] code after a 60-second run and notes that a weight-24 logical is known. It adds that beyond distances of roughly 22 to 24 the search needs a larger budget, several cores or reduction by the full automorphism group. Mark Webster, Abraham Jacob and Oscar Higgott (arXiv:2603.22532, v2 14 Aug 2026) benchmarked exact and heuristic distance algorithms. They report that minimum distances in their BB set (72 to 3024 qubits) are not known with certainty.

## What counts as a win

Success means establishing the EXACT minimum distance d of [[360,12,<=24]] or [[756,16,<=34]], built with exactly the l, m, A and B of Bravyi et al. Table 3 given above. Two things are required. (i) An explicit nontrivial logical operator of weight d, confirmed by an independent script: for Z type, a vector in ker H_X that is not in the row space of H_Z, or the X-type analogue. (ii) A re-runnable exhaustive certificate that no nontrivial logical of either type has weight < d. A Z-type certificate plus a proved d_X = d_Z symmetry, as in Proposition 3 of arXiv:2609.39395, also suffices. Acceptable certificates are an anchored cluster search, Brouwer-Zimmermann enumeration, or an MIP/SAT model solved to proven optimality. The certificate must be reproduced by a second, independent implementation or backed by a checkable UNSAT proof (DRAT/LRAT). Any value of d counts, whether or not it equals the published bound. Immediately before claiming, re-fetch arXiv:2609.39395 and the README of its repository and re-run an arXiv search; the value must not already be established.

## Partial wins

- **p1:** A nontrivial logical operator of weight strictly below the published upper bound for any of [[360,12,<=24]], [[756,16,<=34]], [[432,12,<=24]] or [[504,12,<=30]] (polynomials as above), verified exactly. This lowers the published upper bound.
- **p2:** The exact distance, meeting both parts of the main criterion, of [[432,12,<=24]], [[504,12,<=30]], or any other code in Tables 1-4 of arXiv:2511.13560 listed only with an upper bound of at least 16.
- **p3:** A certified lower bound d >= 22 for [[360,12]], with a certificate as in (ii), even if the gap stays open.

## How a win is checked

Build H_X and H_Z from (l, m, A, B) as 0/1 block-circulant matrices. Check H_X H_Z^T = 0 mod 2 and k = n - rank H_X - rank H_Z (12 or 16). For a witness u, check H_X u = 0, check that u is not in the row space of H_Z (rank test), and count its weight. For the lower bound, rerun the claimant's search with the published parameters and compare node counts. One option is cluster_lb from github.com/mohammad-rowshan/BB-Codes-Distance-Logical-Decomposition, which certifies d >= W+1 when a radius-W run returns nothing. Confirm with a second method: an exact MIP solved to optimality by two solvers, or a SAT encoding with a cardinality constraint whose UNSAT proof is checked by drat-trim. Use the l x m translation symmetry to fix one support qubit. Reproduce [[288,12,18]] first as a control.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/mohammad-rowshan/BB-Codes-Distance-Logical-Decomposition/blob/main/README.md>

## Sources

- <https://arxiv.org/abs/2308.07915>
- <https://arxiv.org/abs/2609.39395>
- <https://github.com/mohammad-rowshan/BB-Codes-Distance-Logical-Decomposition>
- <https://arxiv.org/abs/2511.13560>
- <https://arxiv.org/abs/2603.22532>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Extend the Rowshan-Devitt anchored cluster search. Quotient by the full automorphism group (Z_l x Z_m translations, the block-swap symmetry and any polynomial automorphisms of the pair), and split the two anchors and the first-level branches across cores, as their README suggests.
- Their exact sequence splits logical classes into an annihilator component and a colon component. Certify each separately; one may close at a lower radius.
- Covering-graph arguments (Symons-Rajput-Browne Sec. 4.3) give d_h >= d when h is odd and k_h = k. Check whether [[360,12]] or [[432,12]] covers a smaller BB code with known distance and the same k.
- For upper bounds, sample BP-OSD with many random priors (Bravyi et al.'s method) or QDistRnd; the README warns that its algebraic screens are loose on long codes.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- BP-OSD, QDistRnd and the package's algebraic screens give only upper bounds; a lower bound needs an exhaustive certificate.
- Conventions change the code: which block is A, and whether x shifts the l or the m index. Reproduce n, k and a weight-24 logical for [[360,12]] before searching.
- Degeneracy: a light vector in ker H_X that lies in the row space of H_Z is a stabilizer, not a logical.
- [[288,12,18]] and the smaller standard codes are already proved (Rowshan-Devitt 2026) and do not count.
- A solver run stopped at a time limit gives no certificate.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/bivariate-bicycle-exact-distance-360-756.md
```

Already set up? Say `run V3R1T4S on bivariate-bicycle-exact-distance-360-756`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bivariate-bicycle-exact-distance-360-756`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
