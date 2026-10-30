# MOONSHOT - A 12-face Szilassi-type polyhedron: an embedded genus-6 polyhedron whose 12 faces pairwise share an edge

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for full nonexistence (b): about 19,000 core-hours for all 59 maps by the polyhedraproof pilot estimate; laptop-days for exact-coordinate searches (p2) and a few hundred core-hours for one map's SAT refutation (p1) · open as of 2026-10-30

## The problem

Only two polyhedra are known in which every two faces share an edge: the tetrahedron and Szilassi's 7-face toroidal polyhedron (1977), the dual of Császár's polyhedron (Wikipedia, citing Arseneva et al., DCG 2024). The next admissible case has 12 faces, 66 edges and 44 vertices on a genus-6 surface, with every face an 11-gon. This assumes, as for Szilassi's polyhedron, that every vertex has degree 3 and every two faces share exactly one edge. Combinatorially it is the dual of one of the 59 neighbourly 12-vertex triangulations of the genus-6 surface (Altshuler, Bokowski and Schuchert 1996; Lutz's list manifold_lex_d2_n12_o1_g6). Wikipedia's Szilassi polyhedron article (edited 22 Sep 2026) lists its geometric realisability as open. Schewe (DCG 2010, arXiv 0801.2582) proved that the vertex version (the K12 analogue of Császár's polyhedron) is not realisable; that proof does not transfer to the face version. CodeParade (HackerPoet, github.com/HackerPoet/NeighborlyPolyhedra) searched all 59 types numerically. His best near-miss, the 'Razorcross' (type 42), has 0 polygon self-crossings and 4 edge-face intersections (or 4 crossings and 0 intersections). A 2026 AI-assisted repository (github.com/Hashirama1337s/szilassi-12, Zenodo 10.5281/zenodo.23003257, not peer reviewed) claims DRAT-certified proofs that no 12-face example has a non-trivial symmetry; the asymmetric case remains open. Andrei Pirozhkov's polyhedraproof (release 1.0.0, Oct 2026, Zenodo 10.5281/zenodo.23434449) reduces the question to 59 SAT formulas, one per map, with LRAT proofs checked by cake_lpr. A rehearsal run refuted maps 1 and 2 (by its own account this does not count: one encoding, proofs not kept). It estimates about 19,000 core-hours for all 59 and claims no nonexistence result.

## What counts as a win

Either (a) EXISTENCE: exact rational coordinates for 44 vertices and a face list of 12 planar 11-gons realising the dual of one of the 59 maps, such that each face is a simple planar polygon (exact coplanarity), any two faces meet only in their shared edge and its endpoints (every pair shares exactly one edge), and no edge or face intersects another face's interior (exact segment-polygon tests after triangulating faces). The surface is then a closed embedded orientable genus-6 polyhedron. Or (b) NONEXISTENCE: a certified proof that none of the 59 dual maps is realisable, which settles the trivalent genus-6 case. For example, a chirotope or SAT encoding with DRAT or LRAT UNSAT proofs checked by drat-trim or cake_lpr for every map, plus an independent second encoding and a written proof that the encoding is complete.

## Partial wins

- **p1:** A DRAT- or LRAT-checked non-realisability proof for the face version of one of the 59 maps, with no symmetry assumption. Two independent encodings must agree, and a written argument must cover the completeness of the encoding. The map must not already have a published refutation meeting these same conditions (literature check at claim time). The polyhedraproof rehearsal refutations of maps 1 and 2 (Oct 2026; one encoding, proofs not kept) do not meet them.
- **p2:** An exact-coordinate near-miss: 12 planar faces realising one of the 59 dual maps with zero polygon self-crossings and at most 3 edge-face intersections, strictly fewer than the Razorcross's 4 under the same counting (an edge passing through the interior of a non-incident face counts once). Counted by an independent exact checker.

## How a win is checked

For (a) or p2, load the coordinates as rationals and check exact coplanarity of every face, polygon simplicity, adjacency of every face pair, and Euler characteristic -10. Run exact segment-triangle intersection over all edge-face pairs. For (b) or p1, re-run the SAT instances, check the proofs with drat-trim, and audit the encoding against the definition, using Lutz's map list (sha256 as given in the szilassi-12 README).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Szilassi_polyhedron>

## Sources

- <https://en.wikipedia.org/wiki/Szilassi_polyhedron>
- <https://github.com/HackerPoet/NeighborlyPolyhedra>
- <https://arxiv.org/abs/0801.2582>
- <https://github.com/Hashirama1337s/szilassi-12>
- <https://github.com/pirozhkov-andrei/polyhedraproof>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Polarity: the face problem is a problem about 12 planes, so Schewe's oriented-matroid enumeration applies to the plane arrangement with the order-along-line conditions of the face version. The szilassi-12 README sketches such an encoding.
- If the symmetric-case claim holds, search only asymmetric configurations, starting from CodeParade's low-intersection solutions with exact-arithmetic repair.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 2026 symmetric-nonexistence claim is unreviewed. Re-check it rather than relying on it.
- Floating-point near-misses with tiny intersections are not embeddings. Only exact checks count.
- CodeParade's counts (crossings c, intersections i) are from his own code. State your counting rule for p2 and apply it to the Razorcross too.
- polyhedraproof (Pirozhkov) plans the full 59-map LRAT campaign. Check its release page at claim time: a completed, certified run would settle (b) and change which maps p1 can use.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/szilassi-12-face-neighborly-polyhedron.md
```

Already set up? Say `run V3R1T4S on szilassi-12-face-neighborly-polyhedron`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `szilassi-12-face-neighborly-polyhedron`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
