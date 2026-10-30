# MOONSHOT - Chromatic number of 3-space: a finite unit-distance graph in R^3 that is not 6-colourable (lower bound 6, upper bound 15)

✏️ **Erdős problems and proofs** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (SAT on graphs with thousands of vertices; a single check is laptop-hours) · open as of 2026-10-30

## The problem

chi(R^3), the least number of colours for 3-space with no two points at distance 1 the same colour, satisfies 6 <= chi(R^3) <= 15. The lower bound is Nechushtan's (Discrete Math. 2002). The upper bound is from 15-colourings by Coulson (2002) and Radoičić-Tóth (2003). Cherkashin-Kulikov-Raigorodskii (arXiv:1512.03472) list chi(R^3) >= 6 as the best lower bound, and the Wikipedia Hadwiger-Nelson article, edited in 2026, still gives 6 to 15. In the plane, OpenAI's preprint 'The Euclidean plane is not five-colorable' (23 Sep 2026; Lean formalisation in github.com/openai/math) gives chi(R^2) >= 6 non-constructively, without an explicit 6-chromatic finite graph. That implies chi(R^3) >= 6 again but not 7. By de Bruijn-Erdős, chi(R^3) >= 7 is equivalent to the existence of a finite unit-distance graph in R^3 with chromatic number at least 7. Such a graph would also be the first improvement of the lower bound since 2002. Plane-only finite witnesses are covered by the separate entry hadwiger-nelson-smaller-5-chromatic-udg.

## What counts as a win

An explicit finite graph G with exact algebraic coordinates in R^3 for every vertex (in a stated number field) such that (i) the vertices are distinct, (ii) every listed edge joins two points at distance exactly 1 (exact arithmetic), and (iii) G is not 6-colourable, proved by a SAT solver's UNSAT result with a DRAT or LRAT proof checked by drat-trim or cake_lpr on a CNF that the skeptic regenerates from the coordinates. This must exceed (direction: max) the best lower bound for chi(R^3) stated on the live Wikipedia Hadwiger-Nelson page and in a fresh literature check at verification time (6 on 2026-10-30).

## Partial wins

- **p1:** An explicit finite unit-distance graph in R^3 with exact coordinates and a checked DRAT/LRAT proof that it is not 5-colourable (chromatic number 6), with strictly fewer vertices than every explicit 6-chromatic unit-distance graph in R^3 in the literature at verification time. On 2026-10-30 the smallest known has 47 vertices and 146 edges (de Grey and Haugstrup, 'Two small 6-chromatic unit-distance graphs in R^3', Geombinatorics 2022; MathWorld 'de Grey-Haugstrup Graphs'), so the bar is 46 vertices or fewer. The claimant documents a fresh search.

## How a win is checked

Parse the coordinates as exact algebraic numbers (sympy or Sage); check distinctness and that each edge has squared length exactly 1 (optionally add every unit pair present, which can only help). Encode k-colouring as CNF with symmetry breaking on a known clique (a unit tetrahedron gives 4 forced colours); run CaDiCaL or kissat with proof output; check the proof with drat-trim or an LRAT checker. Re-fetch Wikipedia and record the stated bounds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Hadwiger%E2%80%93Nelson_problem>

## Sources

- <https://en.wikipedia.org/wiki/Hadwiger%E2%80%93Nelson_problem>
- <https://arxiv.org/abs/1512.03472>
- <https://doi.org/10.1016/s0012-365x(00)00406-4>
- <https://github.com/openai/math/blob/main/lean/docs/158.md>
- <https://mathworld.wolfram.com/deGrey-HaugstrupGraphs.html>
- <https://mathworld.wolfram.com/deGreyGraphs.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- 3D spindles: rotating a rigid unit-distance gadget about an axis through two points at a forced-equal-colour distance gives continuum families. Combine planar 5-chromatic graphs (Parts' 509-vertex graph) placed on several planes through a common axis so that the planes' colour constraints interact.
- Lattice-based: subsets of {-1,0,1}-vectors of fixed norm (as in Cherkashin-Kulikov-Raigorodskii for higher dimensions) and of the face-centred cubic lattice scaled so some norm is 1; compute independence numbers exactly and look for |V|/alpha > 6.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Numerical unit distances: coordinates must be exact algebraic numbers.
- An abstract 7-chromatic graph that is not realisable with distinct points in R^3 does not count.
- The solver's verdict alone is not enough; the DRAT/LRAT proof must be checked, on a CNF regenerated from the coordinates.
- A 6-chromatic finite graph in the plane is a different target, and a separate open question.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/chromatic-number-r3-7-chromatic-udg.md
```

Already set up? Say `run V3R1T4S on chromatic-number-r3-7-chromatic-udg`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chromatic-number-r3-7-chromatic-udg`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
