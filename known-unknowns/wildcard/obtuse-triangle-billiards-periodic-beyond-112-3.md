# Periodic billiard paths in obtuse triangles: extend the 112.3-degree theorem (Tokarsky-Garber-Marinov-Moore 2018)

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-days (the 112-112.3 strip alone took 118,809 codes and 27.8 million interval-checked squares; a cluster helps) · open as of 2026-10-30

## The problem

Does every triangle have a periodic billiard path? Acute triangles do (Fagnano's orthic triangle), right triangles do, and rational triangles do (Masur 1986). For obtuse triangles the question is open. Richard Schwartz (Experimental Math. 18 (2009) 137-171, McBilliards) proved by a finite computation that every triangle with largest angle at most 100 degrees has a periodic path. Patrick Hooper and Schwartz (J. Modern Dynamics 2009) handled triangles near the isosceles ones. George Tokarsky, Jacob Garber, Boyan Marinov and Kenneth Moore (arXiv 1808.06667, 2018; only v1) improved Schwartz's method. Their interval-arithmetic prover (GMP/MPFR, no division) covers the (x,y) angle plane with squares, each inside the open region of a stable orbit code (CS, OSO and OSNO codes) or handled by their triple rule. They proved the bound for largest angle up to 112.3 degrees: 2,439 codes for 105-110, 38,132 for 110-112 and 118,809 codes in 27,783,085 squares with 1,115 triples for 112-112.3. Quanta Magazine (15 Feb 2024) still calls 112.3 the state of the art. Checked 2026-10-30: arXiv 1808.06667 has no later version, and a fetch of arXiv 2605.04362 (2026, persistence of billiard orbits) shows no new threshold.

## What counts as a win

A proof that every triangle whose largest angle is at most theta has a periodic billiard path, for some theta >= 112.4 degrees (strictly beyond 112.3 by at least 0.1 degree; direction: max), and above the best threshold found by an arXiv and Google Scholar search re-run just before claiming. The certificate must contain: a finite list of orbit codes; a cover of the uncovered region {0 < x <= y, 180 - theta <= x + y <= 67.7} (angles in degrees, largest angle z = 180 - x - y) by closed squares with exact rational corners, each square proven inside one stable code's open region by outward-rounded interval evaluation of that code's defining inequalities; and, for any infinite code family used near the thin-triangle edge x -> 0, a parametric proof for all n that is symbolic or interval-checked and posted with the claim.

## Partial wins

- **p1:** A certified cover, by the same certificate rules, of every triangle with largest angle in [112.3, 113] degrees and smallest angle at least 1 degree.
- **p2:** A certified cover of any closed region of at least 1 square degree in the (x,y) angle plane where the largest angle is at least 115 degrees, at distance at least 1 degree from the isosceles line x = y. The region must not be covered by any published result found by a literature search.

## How a win is checked

Skeptic: (1) check that the squares tile the target region exactly, using rational arithmetic on the corners; (2) for each square, re-evaluate its code's inequalities, sums of +-u_i sin(m_i x + n_i y) > 0 as in Tokarsky et al. section 'The Program and Proof', with MPFR interval arithmetic and an outward-rounded enclosure of pi, and require every lower endpoint > 0; (3) for a random sample of codes, unfold the code at the centre of one of its squares and confirm in exact or high-precision arithmetic that the unfolded path closes; (4) recheck any parametric infinite-family argument. Hours to days, and the work splits into parallel chunks.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1808.06667>

## Sources

- <https://arxiv.org/abs/1808.06667>
- <https://projecteuclid.org/journals/experimental-mathematics/volume-18/issue-2/Obtuse-Triangular-Billiards-II--One-Hundred-Degrees-Worth-of/em/1259158426.pdf>
- <https://arxiv.org/abs/0807.3498>
- <https://www.quantamagazine.org/the-mysterious-math-of-billiards-tables-20240215/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Port the Tokarsky et al. prover to a GPU or SIMD interval kernel. The cost is dominated by evaluating sine sums over millions of squares, an embarrassingly parallel workload.
- Use adaptive code search: for each uncovered square, run a McBilliards-style search for short stable codes at its centre and keep the codes whose region contains the most uncovered neighbours (greedy set cover).
- Near x -> 0, look for one-parameter code families as in Schwartz's and Hooper-Schwartz's infinite patterns, and prove them with symbolic inequalities in n.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Unstable codes (CNS, ONS) cover only line segments, never area: a square cannot be certified by one.
- A pixel or sample-point check is not a proof: every square needs an interval lower bound strictly above 0 for every inequality of its code.
- Rational triangles and exactly isosceles triangles are already known to have periodic paths, so covering them adds nothing.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/obtuse-triangle-billiards-periodic-beyond-112-3.md
```

Already set up? Say `run V3R1T4S on obtuse-triangle-billiards-periodic-beyond-112-3`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `obtuse-triangle-billiards-periodic-beyond-112-3`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
