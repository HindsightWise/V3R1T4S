# Graph-design spectra: decompose K_16 into 12 copies of a 6-vertex 10-edge graph, K_21 into 7 icosahedra, or settle another listed possible exception

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (SAT / exact cover on K_16 and K_21; larger orders by cyclic base blocks) · open as of 2026-10-30

## The problem

A G-design of order n is a decomposition of the edges of K_n into copies of a graph G. The design spectrum of G is the set of n for which one exists; Bryant and McCourt's G-designs site summarises results (last modified 2020). Recent papers leave explicit possible exceptions. (a) A. D. Forbes and T. S. Griggs (Contrib. Discrete Math. 17(2) (2022), Theorem 1.1(i); arXiv:2004.08963) show that designs exist for graphs n3, n6 and n10 (6 vertices, 10 edges) iff n = 0, 1, 5, 16 (mod 20), except n = 5 and possibly n = 16. Edge sets: n3 = {53,52,51,43,42,41,61,32,31,21}, n6 = {62,63,61,52,53,51,42,43,41,21}, n10 = {43,42,45,41,61,32,35,31,25,21}. The same order is impossible for n8 and n13. (b) Forbes and Griggs (Australas. J. Combin. 52 (2012) 215-228) show that icosahedron designs exist iff v = 1, 16, 21, 36 (mod 60), except possibly v in {21, 141, 156, 201, 261, 276}. Forbes and Rutherford (Australas. J. Combin. 91 (2025) 84-103; arXiv:2401.02846) still describe these 6 cases as unresolved. (c) Forbes and Rutherford determine the spectra of 7788 of the 7849 6-regular 12-vertex graphs (numbered by Meringer's list, K_{6,6} = 7849). For 54 graphs the order 505 remains a possible exception. Five graphs (672, 716, 6187, 6196, 7824) lack a key decomposition of the complete multipartite graph K_{18,18,18,18,18}. The two 6-chromatic graphs 703 and 7848 were not attempted. K_7-designs, i.e. S(2,7,v), are excluded here because they are covered by steiner-2-designs-block-6-undecided.

## What counts as a win

Success means an explicit decomposition, for a pair (G,n) listed in (a), (b) or (c): (n3, n6 or n10, 16); (icosahedron, v in {21,141,156,201,261,276}); (one of the 54 graphs, 505). It is given as a list of n(n-1)/(2|E(G)|) injective maps V(G) -> {0..n-1} that together cover every edge of K_n exactly once. Two independent programs must verify it. At claim time the case must still be a possible exception, checked by a fresh search of Forbes' arXiv/ORCID lists, the Bryant-McCourt site and the literature.

## Partial wins

- **p1:** A missing ingredient named in arXiv:2401.02846 (Proposition 5.3 and the closing remarks): a decomposition of the complete multipartite graph K_{18^5} (five parts of 18) into one of the graphs 672, 716, 6187, 6196 or 7824, or a decomposition of K_{6^7} (seven parts of 6) or K_{72^7} (seven parts of 72) into one of the 54 graphs with the order-505 possible exception. Graphs are taken from Meringer's list as defined in the paper; verified by two programs.
- **p2:** A machine-checked non-existence proof for K_16 into n3, n6 or n10, or for K_21 into 7 icosahedra, with a DRAT/LRAT certificate from an audited encoding.
- **p3:** A decomposition of K_73 (the smallest admissible order) into one of the 6-chromatic 6-regular 12-vertex graphs 703 or 7848, verified by two programs.

## How a win is checked

Rebuild G from its stated edge list (or Meringer's list via the paper's numbering). For each listed copy, check that the map is injective into the vertex set, map G's edges, and count: every edge of the host graph (K_n, or for p1 the complete multipartite graph, whose edges join points in different parts) must be hit exactly once, and no copy may use a pair inside one part. The number of copies must equal |E(host)|/|E(G)|. For base-block claims, expand the development with the verifier's own code. Check isomorphism of the graph used to the named graph with nauty.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2401.02846>

## Sources

- <https://cdm.ucalgary.ca/article/view/70232>
- <https://arxiv.org/abs/2004.08963>
- <https://ajc.maths.uq.edu.au/pdf/52/ajc_v52_p215.pdf>
- <https://arxiv.org/abs/2401.02846>
- <http://g-designs.smp.uq.edu.au/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- K_16 into 12 copies of a 10-edge graph is small: enumerate the labelled copies of G in K_16 (a few million) and solve exact cover with DLX or SAT, adding symmetry breaking on the first copy.
- Icosahedron of order 21: each vertex lies in exactly 4 of the 7 copies. Prescribe Z_7 or Z_3 symmetry, or a 3-orbit structure, and search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- n8 and n13 at order 16, and n13 at order 20, are proven impossible.
- Graph numbering in (c) refers to complements of Meringer's 5-regular list, as defined in arXiv:2401.02846; get the graph right before searching.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/graph-design-spectra-possible-exceptions.md
```

Already set up? Say `run V3R1T4S on graph-design-spectra-possible-exceptions`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `graph-design-spectra-possible-exceptions`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
