# KnotInfo bridge index: settle one of the 536 13-crossing knots listed [3,4] by a 3-bridge diagram or a rank-4 Coxeter quotient

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The bridge index br(K) is the minimum number of local maxima of K (Schubert). KnotInfo (Livingston and Moore) lists it for all prime knots up to 13 crossings. Chad Musick did 11 crossings (arXiv:1208.4233). Blair, Kjuchukova, Velazquez and Villanueva did 12 crossings via the Wirtinger number (arXiv:1705.03108, Comm. Anal. Geom. 28 (2020)). Ella Pfaff did 13 crossings by combining upper bounds from that work and from Blair-Kjuchukova-Pfaff, 'The plain sphere number of a link' (arXiv:2504.10517, Pacific J. Math. 342 (2026)), with lower bounds from Blair-Kjuchukova-Morrison, 'Coxeter quotients of knot groups through 16 crossings' (Exp. Math. 34 (2025), arXiv:2208.09032). Those lower bounds use Baader-Blair-Kjuchukova: if the knot group surjects onto a Coxeter group of rank r with meridians mapped to reflections, then the meridional rank (and hence br) is at least r. In database_knotinfo 2026.10.5, every knot through 12 crossings is determined, but 536 13-crossing knots are still [3,4]. On 2026-10-20/21 Deep Bhattacharjee (github.com/creelie/conjecture-to-choose, Zenodo doi:10.5281/zenodo.23521967; unrefereed, AI-assisted) posted certificates that 243 of the 536 have br = 4. Each certificate is a representation of the knot group into GL(4, F_q) that sends meridians to pseudo-reflections with no common nonzero fixed vector: transvections in Sp(4,F_3) for 67 knots, in Sp(4,F_5) for 161, and reflections in O(4,F_5) for 15. So fewer than four meridians cannot generate the group. An independent re-check on 2026-10-30 confirmed all 243 certificates against the KnotInfo PD codes. The other 293 knots (data/still_open.json in that repository) remain [3,4]. Those searches found no such representation over Sp(4,F_q) for q in {3,4,5,7,8,9,11}, over O(4,F_q) for q in {3,5,7}, or by pseudo-reflections in GL(4,F_2) and GL(4,F_3). They also found no 3-bridge diagram among 300 random diagrams per knot. Can a certificate settle one of the 293?

## What counts as a win

The target is a 13-crossing knot K that meets two conditions, both re-fetched immediately before claiming: (i) its bridge_index is [3,4] in live KnotInfo (https://knotinfo.org/, or the database_knotinfo mirror when that is not older than the site); (ii) it is not settled by data/certificates.json in github.com/creelie/conjecture-to-choose, or by any other public source found in a fresh search. Today that leaves the 293 knots in that repository's data/still_open.json. A win is one of two certificates for K. (a) br = 3: a PD code D, verified as K by SnapPy/Regina identification, plus three seed strands from which the Wirtinger colouring process of Blair-Kjuchukova-Velazquez-Villanueva (arXiv:1705.03108) colours every strand of D. This shows the Wirtinger number of D is at most 3, hence br(K) <= 3. A 6-strand braid whose plat closure is verified as K also counts. (b) br = 4: an assignment to each Wirtinger generator of a verified diagram of K that satisfies every Wirtinger relation and is one of two kinds. (b1) Each generator goes to a reflection (a word conjugating a standard generator) in an explicit Coxeter group W of rank 4; the relations are checked by a word-problem solver for Coxeter groups, and the images generate W. (b2) Each generator goes to an invertible 4x4 matrix A over an explicit finite field with rank(A - I) = 1 (a pseudo-reflection), and the matrices (A - I) of all generators, stacked, have rank 4, so no nonzero vector is fixed by the image. Either gives meridional rank >= 4, and the known upper bound then gives br = 4.

## Partial wins

- **p1:** Settle 10 or more of the knots that count under the main criterion, each with a certificate (a) or (b), in one reproducible run.
- **p2:** A demonstrated inconsistency, with all inputs saved: a certificate (a) for a knot listed 4 in KnotInfo, or for one of the 243 knots certified br = 4 in creelie/conjecture-to-choose; or a certificate (b) for a knot listed 3.

## How a win is checked

(a) The skeptic re-identifies D as K with SnapPy/Regina and reruns the Wirtinger colouring from the three seeds, or builds the plat closure and identifies it. (b1) The skeptic checks every Wirtinger relation in W with a Coxeter-group word-problem routine (for example the Tits/Brink-Howlett solution, or the geometric representation over exact algebraic numbers) and checks that the images generate W. (b2) Working over F_q, the skeptic checks: the matrices are constant along arcs; one orientation convention holds at every crossing (x_c = x_o^e x_a x_o^-e); each matrix is invertible with rank(A - I) = 1; and the stacked (A - I) have rank 4. In every case, also confirm that K is not among the knots already certified in creelie/conjecture-to-choose data/certificates.json. Minutes per knot.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/bridge_index.html>

## Sources

- <https://knotinfo.org/descriptions/bridge_index.html>
- <https://arxiv.org/abs/1705.03108>
- <https://arxiv.org/abs/2208.09032>
- <https://arxiv.org/abs/2504.10517>
- <https://arxiv.org/abs/1208.4233>
- <https://github.com/creelie/conjecture-to-choose>
- <https://doi.org/10.5281/zenodo.23521967>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: randomised Reidemeister exploration, recomputing the Wirtinger number on each new diagram, since non-minimal diagrams can have a lower Wirtinger number. The 300 random diagrams per knot already tried are a small sample, and many of the 293 may well be 3-bridge.
- Conventional: search for 3-bridge plat presentations (6-strand braids) by matching HOMFLY or Alexander data, then identify the closure with SnapPy.
- Conventional: for br = 4, search rank-4 Coxeter quotients beyond the finite and small dihedral targets of arXiv:2208.09032, or 4-dimensional pseudo-reflection representations over fields not yet tried (larger q, extension fields beyond F_4, F_8, F_9, or orthogonal forms over other q). Only dimension 4 is useful: a fixed-point-free pseudo-reflection representation in dimension d forces meridional rank >= d, and br <= 4 is already known.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Wirtinger colouring rule must be the published one (a strand is coloured when it is the understrand at a crossing whose overstrand and other understrand are coloured). A looser rule gives false upper bounds.
- A Coxeter quotient certifies rank r only if the meridians go to reflections and the target has Coxeter rank r. A surjection onto a group that merely needs 4 generators is not enough. Likewise a matrix certificate needs every generator to be a pseudo-reflection and no common fixed vector.
- 243 of the 536 KnotInfo [3,4] knots are already br = 4 by the creelie/conjecture-to-choose certificates (independently re-checked on 2026-10-30). KnotInfo had not taken them in at database_knotinfo 2026.10.5, so a [3,4] entry in KnotInfo alone does not mean a knot is open.
- That repository's verifier and search programs are third-party code. Its certificates are plain JSON (PD code, prime q, one 4x4 matrix per edge, four seed edges) and can be re-checked with an independent program.
- Check for newer preprints by Blair, Kjuchukova and coauthors, and for later releases of creelie/conjecture-to-choose (its Zenodo record already has newer versions), which may settle more of the 293.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/knotinfo-bridge-index-13-crossing.md
```

Already set up? Say `run V3R1T4S on knotinfo-bridge-index-13-crossing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `knotinfo-bridge-index-13-crossing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
