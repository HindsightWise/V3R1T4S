# Crossing number of the hypercube Q_n: a drawing with fewer crossings than Yang-Wang-Wang-Zhou's records (n = 5..13), or a certified lower bound for cr(Q_5)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (n = 5..9); laptop-days for n = 10..13 (up to 8192 vertices) · open as of 2026-10-30

## The problem

Erdős and Guy (1973) conjectured cr(Q_n) = (5/32)4^n - floor((n^2+1)/2) 2^(n-2), the count of the Eggleton-Guy construction. Faria, de Figueiredo, Sýkora and Vrt'o (JGT 2008) published a proof that this is an upper bound; Yang et al. claim that proof has an error. Yang, Wang, Wang and Zhou (J. Graph Theory 100(3) (2022) 389-434, doi 10.1002/jgt.22787; arXiv 1201.4700 v5, 22 Dec 2021) give drawings with fewer crossings for every n >= 7, disproving the conjectured equality. Their Table 2 lists 56, 352, 1744, 8128, 35424, 149888, 619456, 2529024 and 10238848 crossings for n = 5..13, against Erdős-Guy values 56, 352, 1760, 8192, 35712, 151040, 624128, 2547712, 10311680. Their concluding remarks say the drawing is not optimal for n >= 11. The only exact values are cr(Q_n) = 0 for n <= 3 and cr(Q_4) = cr(C_4 x C_4) = 8 (Dean-Richter 1995). The best general lower bound, Sýkora-Vrt'o's 4^n/20 - (n+1)2^(n-2), is trivial for small n. Counting the ten Q_4 subcubes of Q_5 gives cr(Q_5) >= 27 (our arithmetic: each subcube needs 8 crossings, and two distinct edges of Q_5 lie in at most 3 common Q_4 subcubes, so cr(Q_5) >= ceil(80/3) = 27). The Clancy-Haythorpe-Newcombe survey (arXiv 1901.05155 v5, Dec 2021) verified Yang et al.'s Q_7 drawing, reports finding its own Q_7 drawings below 1760 without giving a count, and states that cr(Q_n) is undetermined for n >= 5. Credit: Eggleton-Guy, Erdős-Guy, Madej, Faria-de Figueiredo-Sýkora-Vrt'o, Sýkora-Vrt'o, Yang-Wang-Wang-Zhou, Clancy-Haythorpe-Newcombe.

## What counts as a win

An explicit drawing of Q_n for some 5 <= n <= 13, given as a planarization (crossings as degree-4 dummy vertices), certified planar by two independent testers, with STRICTLY FEWER dummy vertices (direction: min) than the best known value at verification time. That value is the minimum of Yang et al. Table 2 (arXiv 1201.4700, latest version), any count in the Clancy-Haythorpe-Newcombe survey or the authors' later papers, and any value found by a fresh literature search. A drawing of Q_5 below 56 or of Q_6 below 352 would also disprove the Erdős-Guy value at those n.

## Partial wins

- **p1:** An independently checkable certificate (formal proof, or a certified ILP/SAT crossing-number lower bound with a re-derived encoding) that cr(Q_5) >= L, for an L strictly above 27 (the Q_4-subcube counting bound) and above any lower bound found by a fresh literature search (state both).
- **p2:** A drawing of Q_n for some n with 14 <= n <= 16, planarization certified planar, with fewer crossings than Yang et al.'s Theorem 1.1 formula evaluated at that n (the formula includes the lambda_n term for n >= 13).

## How a win is checked

Rebuild Q_n from binary labels. Check that the planarization's dummy-vertex paths reproduce exactly the n 2^(n-1) cube edges, that each dummy has degree 4 on two distinct edge paths, and that the graph is planar (networkx plus Boost/OGDF, with an Euler face count on the embedding). A planar planarization with k dummies proves cr(Q_n) <= k. Compare k with the table. For p1, check the formal proof, or regenerate the encoding and check its proof log.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1201.4700>

## Sources

- <https://arxiv.org/abs/1201.4700>
- <https://arxiv.org/abs/1901.05155>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Yang et al.'s recursive construction (their 'enclosed cycles' adjustment) and apply it at the places they say remain for n >= 11.
- Crossing-minimisation heuristics (OGDF planarization with edge reinsertion, QuickCross star insertion) seeded with the record drawing, run on n = 7..10.
- Exploit symmetry: restrict to drawings invariant under a subgroup of Aut(Q_n), which shrinks the search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Clancy et al. state that they found their own Q_7 drawings below 1760. Find their counts before claiming a Q_7 record below 1744.
- Counting crossings from straight-line coordinates assumes a rectilinear drawing; submit a planarization so that the count is exact.
- Edges crossing more than once, or adjacent edges crossing, are allowed in the certificate (they only inflate the count), but count every dummy vertex.
- The Q_4-subcube count already gives cr(Q_5) >= 27 by hand; a p1 bound of 27 or less is not a win.
- On 2026-10-30 the status source (arXiv v5 and the published JGT version), the survey, and Balko's Harary-Hill exposition (arXiv 2610.34444) were re-read. Web, Crossref, Semantic Scholar (papers citing Yang et al.) and DataCite searches for 2024-2026 hypercube crossing-number work found nothing that improves Table 2 or the lower bounds. arXiv 2603.04665 treats plane substructures and the maximum rectilinear crossing number, not cr(Q_n). Search again before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/hypercube-crossing-number-drawings.md
```

Already set up? Say `run V3R1T4S on hypercube-crossing-number-drawings`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypercube-crossing-number-drawings`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
