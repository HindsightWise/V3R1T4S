# SteinLib PUC and I640: a cheaper Steiner tree for one of the 32 unsolved instances (hypercube, code-covering, bipartite, incidence graphs)

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days per instance (graphs of 640 to 4,096 vertices and up to 28,512 edges; checking a tree takes milliseconds) · open as of 2026-10-30

## The problem

SteinLib (Thorsten Koch, Alexander Martin, Stefan Voss, with Daniel Rehfeldt; ZIB) is the standard library for the Steiner tree problem in graphs. Its PUC set (Rosseti, de Aragao, Ribeiro, Uchoa and Werneck, 2001) holds hypercube (hc), code-covering (cc) and bipartite (bip) graphs, with unit (u) or perturbed (p) edge costs, built to defeat reductions. Re-fetched 2026-10-30, the PUC page (last update 2015-02-11) prints 29 of its 50 values in italics (optimum unknown) and the I640 page italicises i640-311 to -315. The pages are stale. hc9p was proved optimal at 30242 by Shinano, Rehfeldt and Koch (ZIB Report 18-58, CPAIOR 2019, up to 24,576 cores). The same report (Section 5.2, Table 2) lowers hc11p to 119297, with a dual bound of 117,468.85 after runs on up to 43,000 cores. i640-313 was proved optimal at 35535 by Fischetti, Leitner, Ljubic, Luipersbeck, Monaci, Resch, Salvagnin and Sinnl ('Thinning out Steiner trees', Math. Prog. Comp. 2017), so 32 instances remain open. Later work lowered many bars: the DIMACS-11 bounds file (2014-09-12); Fischetti et al. (hc12u 2256, hc11u 1144, bip52u 233, bipa2u 337, cc10-2p 35257, i640-312 35768, i640-315 35720); Braunstein and Muntoni (arXiv:1607.03866: cc11-2p 63405, cc12-2p 121056, bipa2p 35285, hc11p 119456 (beaten by the 119297 of ZIB Report 18-58), and the challenge best 236042 for hc12p by team 'polito'); and Rehfeldt and Koch, 'Implications, conflicts, and reductions for Steiner trees' (Math. Prog. 197, 2023, Table 13: hc10p 59777, dual bounds such as hc10u >= 567.89 and bip52u >= 230.58, every listed PUC instance still unsolved after 54,340 s). The bars below are the minimum over these sources.

## What counts as a win

A Steiner tree (edge list of the SteinLib .stp graph, edges matched by endpoints) that connects every terminal, is a tree, uses only graph edges, and costs STRICTLY LESS (direction: min) than the bar for that instance: bip52p 24526, bip52u 233, bip62p 22843, bip62u 219, bipa2p 35285, bipa2u 337, cc10-2p 35257, cc10-2u 342, cc11-2p 63405, cc11-2u 612, cc12-2p 121056, cc12-2u 1172, cc3-10p 12772, cc3-10u 125, cc3-11p 15582, cc3-11u 153, cc3-12p 18826, cc3-12u 185, cc7-3p 56799, cc7-3u 549, cc9-2p 17199, hc9u 292, hc10p 59777, hc10u 575, hc11p 119297, hc11u 1144, hc12p 236042, hc12u 2256, i640-311 35766, i640-312 35768, i640-314 35532, i640-315 35720. The tree must also beat any value in a later publication found at claim time. hc9p (30242) and i640-313 (35535) are proved optimal and cannot be won. A proof of optimality for a listed instance also counts if it can be checked without trusting the solver, for example a VIPR certificate from exact SCIP checked by viprchk. A solver log alone does not count.

## Partial wins

- **p1:** A certified lower bound for one listed instance strictly above the best published dual bound for it. That is the bound in Rehfeldt and Koch (Math. Prog. 2023, Table 13), or for hc11p the higher 117,468.85 in ZIB Report 18-58 (Table 2), or any higher bound found at claim time. For unit-cost instances the bound must exceed that dual bound rounded up, e.g. at least 569 for hc10u or 232 for bip52u. It must come with a certificate checked independently, such as an exact-arithmetic branch-and-bound certificate (VIPR) or an exact rational dual of a stated valid relaxation, rebuilt from the .stp file by the checker.

## How a win is checked

Download the instance from steinlib.zib.de and parse the SECTION Graph and Terminals blocks. Rebuild the edge set and check the following: each claimed edge exists, with its cost taken from the file (for parallel edges use the cheapest); the chosen edges form a connected acyclic subgraph containing every terminal; the costs sum exactly in integers. This takes milliseconds. Then re-read the SteinLib page, the DIMACS-11 bounds files, the four papers named above and ZIB Report 18-58, and search the literature after 2023 for lower values before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://steinlib.zib.de/showset.php?PUC>

## Sources

- <http://steinlib.zib.de/showset.php?PUC>
- <http://steinlib.zib.de/showset.php?I640>
- <http://steinlib.zib.de/steinlib.php>
- <https://dimacs11.zib.de/instances/bounds20140912.txt>
- <https://www.dei.unipd.it/~salvagni/pdf/Steiner.pdf>
- <https://arxiv.org/abs/1607.03866>
- <https://link.springer.com/content/pdf/10.1007/s10107-021-01757-5.pdf>
- <https://opus4.kobv.de/opus4-zib/files/7111/ZIB-Report-18-58-rev.pdf>
- <https://opus4.kobv.de/opus4-zib/frontdoor/index/index/docId/7349>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The hc and cc graphs are highly symmetric, as hypercubes and Hamming-type graphs. Use automorphisms to seed and repair trees, and orbital fixing in exact search.
- For unit-cost instances a tree with k edges has k+1 vertices, so the problem is choosing a small connected vertex set: use node-based models (Fischetti et al.) and set-covering heuristics, which produced most hc/bip improvements.
- Combine reduction-based presolve (SCIP-Jack) with long multistart local search (key-path exchange, vertex insertion/elimination) and path relinking; run many seeds in parallel.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- SteinLib's own pages have not changed since 2015 and are beaten by later papers on most open PUC and I640 instances (e.g. i640-313: page 35758, proved optimum 35535). Beating the page value is not a win; use the compiled bars and re-check the literature.
- hc9p is proved optimal at 30242 (ZIB Report 18-58) and i640-313 at 35535 (Fischetti et al. 2017); neither is a target even though both pages still print them in italics.
- hc11p: ZIB Report 18-58 (Section 5.2, Table 2) reports 119,297. Tables quoting 119,456 (Braunstein-Muntoni), 119,492 (DIMACS file, SteinLib page) or 119,854 (Rehfeldt-Koch Table 13 primal column) are stale.
- Variants with the same base names (e.g. hc10p2, cc3-12nu, bip52nu) are prize-collecting or node-weighted instances from the DIMACS challenge, not the SPG instances here; several papers tabulate both.
- The cc and bip graph files list some edges twice in some formats (|A| = 2|E| in solver tables); count each undirected edge once.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/steinlib-puc-i640-open-upper-bounds.md
```

Already set up? Say `run V3R1T4S on steinlib-puc-i640-open-upper-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `steinlib-puc-i640-open-upper-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
