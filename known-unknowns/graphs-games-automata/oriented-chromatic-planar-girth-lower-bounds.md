# Oriented chromatic number of planar graphs by girth: an explicit planar oriented graph beating a lower bound (18..80, 11..40, 7..16, 7..11, 6..7, 5..7, 5..6)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (SAT for k <= 10 colours on a few hundred vertices; larger k is harder) · open as of 2026-10-30

## The problem

An oriented k-colouring of an oriented graph (no loops, no 2-cycles) is a homomorphism to an oriented graph on k vertices. Adjacent vertices get distinct colours, and all arcs between two colour classes point the same way. Let chi_o(P_g) be the maximum oriented chromatic number over oriented planar graphs of girth >= g. Table 1 of Das, Nandi and Sen (arXiv:2208.10188 v2, 3 Jul 2026) gives the state of the art. g=3: 18..80 (lower bound Marshall 2015, upper bound Raspaud-Sopena 1994). g=4: 11..40 (lower bound by Ochem 2004 via a computer check, upper bound Ochem-Pinlou 2013). g=5: 7..16 (Marshall 2013; Pinlou 2009). g=6: 7..11 (Marshall 2013; Borodin, Kostochka, Nešetřil, Raspaud, Sopena 1999). g=7: 6..7 (Nešetřil-Raspaud-Sopena 1997; Borodin-Ivanova 2005). g=8,9,10: 5..7. g=11: 5..6 (Ochem-Pinlou 2008). g > =12: 5 (Borodin-Ivanova-Kostochka 2007). The paper says the exact value is unknown for every g in 3..11. Most lower bounds rest on arguments that no small target graph works, not on explicit witness graphs.

## What counts as a win

Success means, for some g in {3,...,11}, an explicit oriented graph G (arc list) with (i) a planar embedding certified by an independent planarity test (for example networkx check_planarity plus a second implementation), (ii) underlying girth >= g computed by BFS, and (iii) a DRAT/LRAT-checked proof (drat-trim or cake_lpr) that G has no oriented L-colouring, where L is the current lower bound for that g. That makes chi_o(P_g) >= L+1, STRICTLY GREATER (direction: max) than the lower bound in Table 1 of arXiv:2208.10188 (latest version) and in any newer paper found by a fresh search. The CNF is the skeptic's own: colour variables x_{v,c} with exactly-one constraints, and orientation variables y_{c,d} = not y_{d,c}. Each arc u->v gets the clauses not(x_{u,c} and x_{v,c}) and (not x_{u,c} or not x_{v,d} or y_{c,d}). For g = 7 a win settles chi_o(P_7) = 7, and for g = 11 it settles chi_o(P_11) = 6.

## Partial wins

- **p1:** An explicit triangle-free planar oriented graph with a checked proof that it has no oriented 10-colouring, giving an explicit witness for chi_o(P_4) >= 11, provided no explicit witness of that size or smaller is published (fresh search).
- **p2:** An explicit planar oriented graph (any girth) with a checked proof that it has no oriented 17-colouring, giving an explicit witness for Marshall's chi_o(P_3) >= 18, under the same proviso.

## How a win is checked

Load the arc list. Check that there are no loops or 2-cycles. Run two planarity tests on the underlying graph and compute its girth by BFS from every vertex. Generate the CNF with an independent script, check the proof with drat-trim, and cross-check that the same CNF with L+1 colours is SAT when the claimant supplies such a colouring (sanity only). Then re-fetch arXiv:2208.10188 and search for newer bounds for that girth.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2208.10188>

## Sources

- <https://arxiv.org/abs/2208.10188>
- <https://arxiv.org/abs/2607.22915>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start with g = 11 (5 versus 6) and g = 7 (6 versus 7). Build large girth-g planar oriented graphs by iterated gadget gluing: whenever a SAT solver finds an oriented 5- or 6-colouring, add a gadget that kills that colouring's target tournament, and repeat (a CEGAR loop over targets).
- The number of tournaments on L vertices is small for L <= 7 (456 non-isomorphic tournaments on 7 vertices). For each, find a planar girth-g oriented graph with no homomorphism to it, then combine them by disjoint union plus connecting paths that preserve girth.
- Use the 'minimal bound' viewpoint from Das-Nandi-Sen: show by exhaustive SAT that no oriented graph on L vertices with the required extension properties exists, then extract an explicit graph from the failing cases.
- Break colour symmetry by fixing colours on a small oriented clique, which is sound, to speed up the UNSAT proof.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Oriented colouring is not proper colouring of the underlying graph. The arc-consistency condition between colour classes is essential; leaving it out makes every planar graph 4-colourable.
- Girth is measured on the underlying undirected graph and must be >= g, so a single short cycle disqualifies the graph.
- Planarity must be checked exactly. Drawing coordinates alone are not a certificate.
- Upper-bound improvements are theoretical proofs and are not covered by this target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/oriented-chromatic-planar-girth-lower-bounds.md
```

Already set up? Say `run V3R1T4S on oriented-chromatic-planar-girth-lower-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `oriented-chromatic-planar-girth-lower-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
