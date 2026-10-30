# Packing vs piercing for axis-parallel rectangles after Wegner's conjecture fell: a finite family with tau > (5/2) nu

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact nu and tau by ILP for families of a few hundred to a few thousand rectangles) · open as of 2026-10-30

## The problem

For a finite family R of closed axis-parallel rectangles in the plane, nu(R) is the largest number of pairwise disjoint members and tau(R) is the fewest points meeting every member. Wegner (1965) conjectured tau <= 2nu - 1, and Gyárfás and Lehel asked whether tau/nu is bounded by a constant. The best general upper bound was O(nu (log log nu)^2) (Correa, Feuilloley, Pérez-Lantero and Soto); Rao, Eom and Kim (arXiv:2610.16703, Oct 2026) improve the factor to log log nu * log log log nu. Earlier lower constructions: Fon-Der-Flaass and Kostochka (ratio 5/3) and Jelínek (tau = 2nu - 4). Ajwani, Gajjala, Raman and Ray, 'Counterexamples to Wegner's Conjecture for Rectangles', arXiv:2606.17854 (v2, 9 Jul 2026), disproved Wegner. Their v2 abstract gives an explicit triangle-free family of 64 rectangles with nu = 16 and tau >= 32, and triangle-free families with tau >= (5/2 - eps) nu for every eps > 0. They also proved that the clique-LP gap is at most 3 on triangle-free families. Aranya Kumar Bal, arXiv:2607.11318 (v2, 14 Jul 2026), gave a hand-checkable 64-rectangle triangle-free counterexample (nu = 16, tau >= 32) and a finite clique-LP gap of at least 73/32 (Ajwani et al.: 17891/8064). He also built recursive families P_r with tau(P_r)/nu(P_r) -> 5/2 and alpha*(P_r)/nu(P_r) -> 5/2. Adding isolated rectangles makes every rational in [1, 5/2) occur both as tau/nu and as an LP gap. Bal states that the global supremum over rectangle families remains open. No finite family with tau/nu >= 5/2 is published.

## What counts as a win

An explicit finite family of closed axis-parallel rectangles with rational coordinates whose exactly computed ratio tau(R)/nu(R) is STRICTLY GREATER than 5/2 (direction: max) and than any larger finite ratio published at verification time. Re-check the arXiv pages of 2606.17854 and 2607.11318 and any 2026 follow-up first. Both nu and tau must be certified exactly: nu by a maximum independent set of the intersection graph with an optimality proof, and tau by a minimum hitting set over a provably sufficient candidate point set with an optimality proof, each confirmed by two independent exact solvers.

## Partial wins

- **p1:** A finite family with tau(R) = (5/2) nu(R) exactly. This attains the published limit, which no finite family is known to reach.
- **p2:** A finite family whose standard clique (point) LP relaxation of maximum independent set has value alpha*(R) >= (5/2) nu(R), computed exactly in rationals. This beats every published finite gap: Bal's 73/32 and the interpolated values below 5/2.
- **p3:** A counterexample to Wegner's conjecture (a family with tau >= 2 nu) with fewer than 64 rectangles, the size of the smallest published examples (Ajwani et al. v2 and Bal).

## How a win is checked

An independent script: parse the rectangles as closed boxes [x1,x2] x [y1,y2] with exact rationals. Build the intersection graph (closed boxes intersect iff their x- and y-intervals both overlap, touching included). For tau, use the candidate points (left x of rectangle i, bottom y of rectangle j) that lie in at least one rectangle: any piercing point can be moved to such a point without leaving any rectangle. Solve both ILPs with two solvers (e.g. CBC via pulp and OR-Tools CP-SAT) to proven optimality. For p2, solve the LP over the same point set in exact rational arithmetic (or verify a rational primal and dual pair). Calibrate on Bal's 64-rectangle family: nu = 16, tau >= 32.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2607.11318>

## Sources

- <https://arxiv.org/abs/2607.11318>
- <https://arxiv.org/abs/2606.17854>
- <https://arxiv.org/abs/2610.16703>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Open versus closed rectangles changes the intersection graph: use closed rectangles, the convention of both papers.
- Ratios that only tend to a limit are not a finite family: the win needs one explicit family with exact tau and nu.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/rectangle-piercing-packing-ratio-above-5-2.md
```

Already set up? Say `run V3R1T4S on rectangle-piercing-packing-ratio-above-5-2`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rectangle-piercing-packing-ratio-above-5-2`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
