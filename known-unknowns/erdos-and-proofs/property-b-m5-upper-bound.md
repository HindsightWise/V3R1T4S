# Property B: a non-2-colourable 5-uniform hypergraph with at most 50 edges (m(5) <= 51 since 1969)

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (search; certifying a candidate takes seconds to minutes) · open as of 2026-10-30

## The problem

An n-uniform hypergraph has property B if its vertices can be 2-coloured with no monochromatic edge. m(n), the minimum number of edges in an n-uniform hypergraph without property B, is the Erdős-Hajnal problem (Erdős #901, OEIS A392185). Known values are m(1..4) = 1, 3, 7, 23. For n = 5 the upper bound 51 comes from the Abbott-Hanson-Toft recursive construction, m(5) <= 2^4 + 5 m(3). It is still listed as the current upper bound in Aglave, Amarnath, Shannigrahi and Singh (Australas. J. Combin. 76, 2020, arXiv:1602.00218 v4) and in Table 1 of Grill and Linzmayer (arXiv:2403.05674 v3, Jun 2024). Lower bounds rose from 28 to 29 (Aglave et al.) and then to 32 (Grill-Linzmayer, Theorem 1). OEIS A392185 (Kyle Wood, Jan 2026) still prints 29 <= a(5) <= 51, so its lower bound is stale but its upper bound agrees. Other upper bounds from Aglave et al.'s Table 1 and Section 4 are m(6) <= 147 (Abbott-Moser), m(7) <= 421 (Abbott-Hanson-Toft) and m(8) <= 1212 (Aglave et al., improving Mathews-Panda-Shannigrahi's 1269). No smaller explicit 5-uniform non-2-colourable hypergraph has been published. Find one.

## What counts as a win

Success means an explicit list of E distinct 5-element subsets of a finite vertex set such that the hypergraph has no proper 2-colouring. This must be certified either by exhaustive enumeration of all 2^v colourings (feasible for v <= about 34) or by an UNSAT result on the CNF (for each edge, one clause forbidding all-colour-1 and one forbidding all-colour-0), with the UNSAT proof checked by drat-trim or cake_lpr. E must be STRICTLY LESS (direction: min) than the best published upper bound on m(5) at verification time: 51 per OEIS A392185 (re-fetched before claiming), arXiv:2403.05674 v3 and arXiv:1602.00218 v4, unless a fresh search for 'property B' upper bounds over the last 24 months shows a smaller one. A hypergraph with fewer than 32 edges contradicts Grill-Linzmayer's lower bound and means a bug.

## Partial wins

- **p1:** An explicit non-2-colourable 6-uniform hypergraph with at most 146 edges (beating m(6) <= 147), certified the same way.
- **p2:** An explicit non-2-colourable 7-uniform hypergraph with at most 420 edges (beating m(7) <= 421), certified the same way.
- **p3:** An explicit non-2-colourable 8-uniform hypergraph with fewer edges than the best published upper bound on m(8) (1212 in arXiv:1602.00218 v4, or a smaller value found by a fresh search), certified the same way.

## How a win is checked

Parse the edge list. Assert that each edge has exactly n distinct vertices and that the edges are pairwise distinct, and count them. Build the 2-colouring CNF with one's own script. Run CaDiCaL with --lrat or DRAT output and check the proof with drat-trim or cake_lpr. When there are at most about 34 vertices, also enumerate all colourings directly with a bitmask in C. Then re-fetch arXiv:2403.05674 and search for newer bounds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A392185>

## Sources

- <https://oeis.org/A392185>
- <https://arxiv.org/abs/2403.05674>
- <https://arxiv.org/abs/1602.00218>
- <https://www.erdosproblems.com/901>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search over hypergraphs with a large automorphism group, for example orbits of 5-sets under a cyclic or affine group on v points, with v in the range where the lower-bound arguments force the extremal example (Grill-Linzmayer study m(5, v) for 17 <= v <= 25).
- Use local search on hypergraphs to maximise the number of edges a 2-colouring must violate, with a SAT oracle for 2-colourability, adding and removing edges as in Exoo-style Ramsey searches.
- Generalise the Abbott-Hanson-Toft and Seymour (m(4) = 23) constructions: replace the Fano-plane ingredient by other small non-2-colourable systems and SAT-search the gluing.
- Exploit the lower-bound proofs: they show an extremal 5-uniform example must have about 23 to 25 vertices with nearly regular degrees, which shrinks the search space.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Improving the lower bound (for example to m(5) >= 34) is a different and much harder problem. Only an explicit hypergraph counts here.
- Edges must be exactly 5-uniform. Adding a smaller edge, or a repeated edge, makes the claim invalid.
- Bounds from recursive formulas are not explicit hypergraphs. Expand any recursive construction fully and certify the explicit object.
- An UNSAT verdict without a checked proof is not a certificate.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/property-b-m5-upper-bound.md
```

Already set up? Say `run V3R1T4S on property-b-m5-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `property-b-m5-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
