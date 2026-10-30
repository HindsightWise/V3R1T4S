# Fractional chromatic number of the plane: an explicit finite unit-distance graph with fractional chromatic number above 4 (best explicit: about 3.9898)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact LP/ILP on graphs of 1,000-20,000 vertices; exact algebraic coordinates) · open as of 2026-10-30

## The problem

Lower bounds on chi_f(R^2), the fractional chromatic number of the plane's unit-distance graph, come from finite unit-distance graphs G via chi_f(R^2) >= chi_f(G); Matolcsi, Ruzsa, Varga and Zsamboki showed the supremum over finite G equals the geometric fractional chromatic number and the Hall ratio of the plane. Explicit finite graphs climbed slowly: Moser spindle 7/2, Mahan 144/41, Fisher-Ullman 32/9, Cranston-Rabern 76/21 (2017), Bellitto-Pecher-Sedillot 3.899 (607 vertices), and unpublished computations of Jaan Parts about 3.9898 (1057 vertices, Polymath16 comment, 2022). Matolcsi, Ruzsa, Varga and Zsamboki (arXiv 2311.10069) proved chi_f(R^2) >= 4 via a 27-vertex configuration with geometric fractional chromatic number 4, noting no finite subgraph was known to reach 4. Duecz and Varga (arXiv 2606.28157, June 2026) added two vertices (G29, geometric value > 4.0007 by a rational dual) and proved that a finite unit-distance graph with independence ratio below 1/4 exists, answering Erdos's 1987 question and giving chi_f(R^2) > 4; but their finite graph is described as astronomically large and is not written down. The upper side is chi_f(R^2) <= 1/delta_Croft < 4.36 from Croft's 1967 periodic set of density 0.22936... Target: write down an explicit, checkable finite unit-distance graph with chi_f > 4.

## What counts as a win

An explicit finite graph G with vertex coordinates given exactly (integers or rationals combined with stated square roots, or minimal polynomials with isolating boxes) such that (i) every listed edge has Euclidean length exactly 1, verified by exact symbolic arithmetic (sympy or SageMath, not floating point); (ii) chi_f(G) > 4, certified by rational vertex weights y >= 0 with sum(y) > 4 and max over independent sets I of y(I) <= 1, the latter confirmed by two independent exact maximum-weight-independent-set or ILP solvers (exact rational arithmetic, e.g. SCIP exact or a clique solver on the complement). The uniform-weight special case |V|/alpha(G) > 4, with alpha certified the same way, also suffices (it implies chi_f(G) > 4 but is stronger). Listing fewer than all unit pairs is allowed (it can only lower chi_f). arXiv 2606.28157 and a literature search (OpenAlex citations of it and of arXiv 2311.10069), rerun before claiming, must show no explicit finite example with chi_f > 4 published earlier.

## Partial wins

- **p1:** An explicit finite unit-distance graph with certified chi_f(G) >= 3.99, above Parts's approximately 3.9898 (1057 vertices, unpublished, Polymath16 comment of 2022-09-21), verified as in the success criterion.
- **p2:** An explicit finite unit-distance graph with certified chi_f(G) >= 4 exactly (arXiv 2311.10069 and 2606.28157 report no finite subgraph reaching 4 before the existence proof of 2606.28157), verified as in the success criterion.
- **p3:** A finite point configuration whose geometric fractional chromatic number, in the LP framework of arXiv 2311.10069, is certified by a rational dual solution to be at least 4.001. This is above Duecz-Varga's certified 4.0007 for G29 and their unverified estimates of about 4.0009. Checked by rebuilding the LP from exact coordinates and verifying the dual in rational arithmetic.

## How a win is checked

Recompute all edge lengths symbolically; rebuild the independent-set LP/ILP from the edge list; check the rational weights and solve maximum-weight independent set exactly with two solvers. Minutes to hours for a few thousand vertices.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2606.28157>

## Sources

- <https://arxiv.org/abs/2606.28157>
- <https://arxiv.org/abs/2311.10069>
- <https://arxiv.org/abs/1501.01647>
- <https://dustingmixon.wordpress.com/2021/02/01/polymath16-seventeenth-thread-declaring-victory/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Matolcsi et al.'s G27 and Duecz-Varga's G29: their geometric (weighted, congruence-invariant) LP certificate indicates which vertex classes need many rotated/translated copies; build the finite graph by taking the Minkowski-style closure of G29 under a finite set of rotations in the Moser lattice and solving the plain fractional LP with column generation.
- Column generation: the fractional colouring LP has one column per independent set; generate columns by exact max-weight independent set (the pricing problem) and stop when no column has reduced cost below 0, as Cranston-Rabern and Bellitto et al. did.
- Graph minimisation (Parts, arXiv 2010.12665): once a large certificate is found, delete vertices while chi_f stays above 4.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point coordinates are not a proof that distances equal 1; unit-distance graphs in the Moser lattice need exact arithmetic in Q(sqrt3, sqrt11, ...).
- The geometric fractional chromatic number of a configuration is not the fractional chromatic number of a finite graph; only p3 accepts it.
- Measurable versus ordinary: m1(R^2) < 1/4 (Ambrus et al. 2023) bounds the measurable fractional chromatic number, not chi_f of a finite graph.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/fractional-plane-explicit-finite-udg-above-4.md
```

Already set up? Say `run V3R1T4S on fractional-plane-explicit-finite-udg-above-4`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fractional-plane-explicit-finite-udg-above-4`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
