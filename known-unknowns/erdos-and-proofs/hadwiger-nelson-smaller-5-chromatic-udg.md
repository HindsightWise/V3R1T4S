# Hadwiger-Nelson finite witnesses (Erdos #508 context): a 5-chromatic unit-distance graph with fewer than 509 vertices

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The chromatic number of the plane (Erdos #508, Tao's constant 27a) is now known to be 6 or 7: OpenAI's preprint 'The Euclidean plane is not five-colorable' (23 Sep 2026, Lean formalisation in github.com/openai/math, linked from erdosproblems.com/508, which lists 6 <= chi <= 7) proves no proper 5-colouring exists. That proof is non-constructive (a measurable-transfer argument plus graph compactness), so it exhibits no small finite graph. The finite-witness record question for 5 colours remains: de Grey's 2018 1581-vertex graph first showed chi >= 5; Heule's SAT-based shrinking reached 553 vertices and Parts (arXiv:2010.12665) reached 509 vertices and 2442 edges, which MathWorld's de Grey graphs page (last updated 27 Oct 2026) still lists as the smallest known 5-chromatic unit-distance graph; Haugland 2026 (arXiv:2608.04542) gives a larger Moser-spindle-free example. Lower bounds on the order of such graphs are studied in arXiv:2303.14714. Target: a unit-distance graph in the plane with chromatic number 5 (not 4-colourable) and fewer vertices than the live record.

## What counts as a win

Success means an explicit graph G with exact algebraic coordinates for each vertex (in a stated number field, e.g. Q(sqrt3, sqrt5, sqrt11, ...)), such that (i) all vertices are distinct, (ii) every listed edge joins two points at distance exactly 1 (exact arithmetic), (iii) G is not 4-colourable, proven by a SAT solver's UNSAT result with a DRAT or LRAT proof checked by drat-trim or cake_lpr, and (iv) the number of vertices is STRICTLY LESS (direction: min) than the smallest 5-chromatic unit-distance graph reported on the live page https://mathworld.wolfram.com/deGreyGraphs.html, the Wikipedia Hadwiger-Nelson page, the Polymath16 wiki and any newer arXiv paper (search 'unit distance graph chromatic number 5'), all re-fetched live immediately before claiming. Graphs on a sphere or in higher dimensions do not count.

## Partial wins

- **p1:** A 5-chromatic unit-distance graph with at most 509 vertices and fewer than 2442 edges, with the same exact-coordinate and DRAT/LRAT checks.
- **p2:** An exact recount/recheck of Parts' 509-vertex graph from its published coordinates that confirms or corrects the record (replay note).

## How a win is checked

Parse coordinates as exact algebraic numbers (sympy/Sage); check pairwise distinctness and that each edge has squared length exactly 1 (and optionally add all unit pairs present, which can only help non-colourability); encode 4-colouring as CNF with symmetry breaking on a known triangle; run CaDiCaL/kissat with proof output; check the proof with drat-trim or an LRAT checker. Minutes to an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mathworld.wolfram.com/deGreyGraphs.html>

## Sources

- <https://mathworld.wolfram.com/deGreyGraphs.html>
- <https://arxiv.org/abs/2010.12665>
- <https://arxiv.org/abs/2303.14714>
- <https://en.wikipedia.org/wiki/Hadwiger%E2%80%93Nelson_problem>
- <https://www.erdosproblems.com/508>
- <https://github.com/openai/math/blob/main/lean/docs/158.md>
- <https://teorth.github.io/optimizationproblems/constants/27a.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- SAT-core shrinking with stronger tools: compute minimal unsatisfiable cores of the 4-colouring CNF of Parts' graph with modern MUS extractors and different symmetry breaking; then re-add unit pairs that appear 'for free' between remaining vertices.
- Rebuild from different spindles: Parts' method uses specific 'gadget' subgraphs forcing monochromatic pairs at certain distances; search new gadgets in other algebraic fields (e.g. involving sqrt 7 or sqrt 33).
- Cross-domain import (VLSI circuit minimisation): treat vertex removal as logic minimisation with don't-cares; iterative 'remove, re-solve, keep if still UNSAT' with learned clause reuse (incremental SAT) is how circuit minimisers scale.
- Cross-domain import (protein design / inverse folding): the graph must stay realisable while losing vertices; alternate a combinatorial step (drop a vertex set) with a continuous realisation step (keep unit edges exact via algebraic closure), like sequence-structure co-design.
- Use rotations by angles whose cosines lie in the existing field to create many new unit coincidences in a small Minkowski sum before pruning.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Numerical unit distances: an edge at distance 1 + 1e-15 is not an edge; coordinates must be exact algebraic numbers.
- Abstract vs geometric: a graph that is 4-chromatic-free as an abstract graph but not realisable as a unit-distance graph (or realisable only with coincident vertices) does not count.
- Unchecked UNSAT: the solver's verdict alone is not enough; the DRAT/LRAT proof must be verified, and the CNF must be regenerated from the coordinates by the skeptic.
- Counting the record wrongly: the record is by vertices (509); edge-count improvements are only partial win p1.
- Wrong target: since chi(R^2) >= 6 is now proved, a smaller 5-chromatic graph is a finite-witness record, not progress on the 6-vs-7 question; a 6-chromatic finite graph is a different question (see the separate Hadwiger-Nelson six-or-seven proposal).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/hadwiger-nelson-smaller-5-chromatic-udg.md
```

Already set up? Say `run V3R1T4S on hadwiger-nelson-smaller-5-chromatic-udg`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hadwiger-nelson-smaller-5-chromatic-udg`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
