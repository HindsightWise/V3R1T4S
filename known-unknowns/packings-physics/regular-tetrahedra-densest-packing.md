# MOONSHOT - Regular tetrahedra: a packing of congruent regular tetrahedra denser than the Chen-Engel-Glotzer dimer double lattice 4000/4671 = 0.856347...

⚪ **Packings and physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days (periodic hard-polyhedron compression of small cells, then exact certification in minutes) · open as of 2026-10-30

## The problem

What is the largest fraction of R^3 that congruent non-overlapping regular tetrahedra can fill? This is part of Hilbert's 18th problem (Aristotle wrongly thought tetrahedra tile space). After a 2006-2010 race (Conway-Torquato about 0.72; Chen 2008 0.7786; Torquato-Jiao 2009 0.823; Haji-Akbari et al. 2009, a quasicrystal approximant of 0.8503; Kallus-Elser-Gravel 2010, 100/117 = 0.854700 with 4 tetrahedra per cell; Torquato-Jiao, analytic dimer constructions up to 12250/14319 = 0.855506), Elizabeth Chen, Michael Engel and Sharon Glotzer (Discrete Comput. Geom. 44 (2010) 253-280, arXiv:1001.0586) gave a three-parameter family of double-dimer packings (triangular bipyramids, 4 tetrahedra per cell) of density exactly 4000/4671 = 0.85634767715692571... This is still the densest known packing on the Wikipedia 'Tetrahedron packing' page (fetched 2026-10-30). The best rigorous upper bound is only 1 - 2.6e-25 (Gravel, Elser and Kallus, DCG 2011, arXiv:1008.2830). The densest lattice packing is 18/49 (Hoylman 1970). Jin, Lu and Li (Sci. Rep. 2015) showed that for slightly ROUNDED tetrahedra a quasicrystal approximant beats the dimer lattice; this does not apply to sharp regular tetrahedra. Web searches on 2026-10-30 found no denser packing of regular tetrahedra and no upper bound below 1 - 2.6e-25 (Dostert, Guzman, de Oliveira Filho and Vallentin, arXiv:1510.02331, bound translative packings only).

## What counts as a win

Success means a periodic packing: a lattice basis L (3 vectors) and k tetrahedra, each given by 4 vertices with exact rational coordinates (or exact algebraic numbers) such that every tetrahedron is EXACTLY regular, with all six edge lengths equal to a common value a, checked exactly. (1) Interiors are pairwise disjoint over all tetrahedron pairs, including lattice translates within the circumradius cutoff. This is certified exactly by a separating plane per pair (supplied or found by LP) with all vertices of one body weakly on each side. (2) The density k*(a^3/(6*sqrt2))/|det L|, computed exactly, is STRICTLY GREATER (direction: max) than 4000/4671 and than any denser value published by verification time. Rational approximations that are not exactly regular do not count. Instead, shrink each tetrahedron about its centroid by a certified factor and report the density after shrinking.

## Partial wins

- **p1:** A new periodic packing of regular tetrahedra whose primitive cell holds a number of tetrahedra other than 4 (so it is not in the Kallus-Elser-Gravel, Torquato-Jiao or Chen-Engel-Glotzer dimer families), with certified density STRICTLY GREATER than 100/117 = 0.854700... (Kallus-Elser-Gravel), certified as in the main criterion.
- **p2:** A rigorous upper bound on the packing density of regular tetrahedra strictly below 1 - 2.6e-25 (Gravel-Elser-Kallus 2011). The proof must be machine-checked or come as a re-runnable exact or interval-arithmetic computation that the skeptic re-executes, with a written reduction that matches it.

## How a win is checked

Independent script in exact arithmetic (sympy or fractions over Q(sqrt2) after a rational change of basis, or an interval library). Check that all 6 edge lengths squared are equal and exact for each body. Enumerate lattice images within 2*circumradius. For every pair, solve a small LP for a separating plane, then re-check it exactly against the 8 vertices. Compute |det L| exactly and the density, then compare with 4000/4671 using exact rational comparison. Calibrate by rebuilding the Chen-Engel-Glotzer packing from arXiv:1001.0586 Theorem 1 and recovering 4000/4671 exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Tetrahedron_packing>

## Sources

- <https://en.wikipedia.org/wiki/Tetrahedron_packing>
- <https://arxiv.org/abs/1001.0586>
- <https://arxiv.org/abs/1008.2830>
- <https://arxiv.org/abs/0910.5226>
- <https://arxiv.org/abs/1012.5138>
- <https://arxiv.org/abs/0912.4210>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search periodic cells with 8-16 tetrahedra under exact regularity, using event-driven or ASC (adaptive shrinking cell) compression. Chen-Engel-Glotzer's 3-parameter optimum is a local maximum within dimer families only.
- Combine dimer (bipyramid) units with other face-sharing clusters (pentagonal dipyramids, icosahedral fragments) in larger cells. Quasicrystal approximants became competitive for rounded tetrahedra (Jin-Lu-Li 2015).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point overlap tests: near-face-to-face contacts make tiny overlaps look like touching, so certify with exact separating planes.
- Slightly irregular 'tetrahedra' from rational rounding are not regular: shrink them, never stretch them.
- The Haji-Akbari 0.8503 quasicrystal and the 100/117 = 0.8547 KEG packing are below the record; do not compare against them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/regular-tetrahedra-densest-packing.md
```

Already set up? Say `run V3R1T4S on regular-tetrahedra-densest-packing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `regular-tetrahedra-densest-packing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
