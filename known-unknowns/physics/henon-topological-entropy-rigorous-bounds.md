# Topological entropy of the classical Henon map: a rigorous lower bound above 0.46469, a certified upper bound below ln 2, or periodic-orbit counts beyond period 30

⚛️ **Physics** · standard · tractability ★★★☆☆ · compute: laptop-days (interval-verified covering relations or trellis computations; orbit counts at p = 31-34 take laptop-days with pruning) · open as of 2026-10-30

## The problem

The Henon map h(x,y) = (1 + y - 1.4 x^2, 0.3 x) has numerical topological entropy (on Henon's trapping region, i.e. on the attractor A) about 0.4649-0.4651: Galias and Tucker (Chaos 25, 033102 (2015)) estimate H_p = (1/p) log(fixed points of h^p), which stabilises around 0.46493 for p up to 50, and D'Alessandro et al. get 0.4651. Rigorous lower bounds: Galias (covering relations, about 2001-2002) 0.4300; Sarah Day, Rafael Frongillo and Rodrigo Trevino (Conley index, SIAM J. Appl. Dyn. Syst. 2008) 0.4320; S. Newhouse, M. Berz, J. Grote and K. Makino (Contemp. Math. 469 (2008) 243-270, a trellis built from verified homoclinic tangles) 0.46469, cited as the lower bound by Anikushin and Romanov (arXiv 2503.11150, 2025). The rigorous upper bound cited there is ln 2 = 0.693147 (Newhouse 1988). Anikushin and Romanov's adapted-metric method gives 'robust' upper estimates of the largest uniform Lyapunov exponent, which bounds h_top from above. These estimates converge down to 0.6542706..., the exponent at the fixed point q+, which is also a lower bound for that exponent (0.6542720 after 10^6 steps). They say the estimates could potentially be made rigorous, but they are not interval-verified. Rigorous counts of all period-p orbits are published only for p <= 30 (Galias, Int. J. Bifurcation Chaos 11 (2001) 2427), as Galias-Tucker 2015 state. Their Table I gives Biham-Wenzel counts P_31..P_34 = 58,656, 90,343, 139,674 and 215,597 that are not rigorous.

## What counts as a win

Main win: a computer-assisted proof that h_top >= L with L >= 0.46470 (strictly above 0.46469; direction: max) and above any rigorous value found by a literature search re-run just before claiming. The certificate is a finite family of h-sets or boxes with covering relations, or a trellis, all verified in outward-rounded interval arithmetic. It yields an integer transition matrix A whose Perron root is certified >= e^L in exact arithmetic (for example a Collatz-Wielandt test vector), and the claim states the semiconjugacy theorem used.

## Partial wins

- **p1:** A rigorous count, with an interval-Newton existence and uniqueness certificate per orbit and a proof that no other period-p orbit exists in the trapping region, of all period-p orbits for some p in 31..34 for which no rigorous count is found by a literature search, compared with the Galias-Tucker 2015 Table I value; any difference must be explained.
- **p2:** A fully interval-verified upper bound h_top < 0.693147 (below ln 2), for example from a rigorous symbolic image (outer box covering) or an interval-checked adapted metric.
- **p3:** A fully interval-verified upper bound h_top < 0.6542706, below the uniform-Lyapunov ceiling of the adapted-metric method. This needs a method other than the largest uniform exponent.

## How a win is checked

Lower bound: re-verify each covering relation with an independent interval library (images of the box edges against the target box's sides), rebuild A, and check the Perron-root certificate exactly; hours. p1: re-run interval Newton on each listed orbit and the exclusion argument for the rest of the trapping region. p2/p3: recompute the outer image graph or the metric inequalities in interval arithmetic and the bound from them.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2503.11150>

## Sources

- <https://arxiv.org/abs/2503.11150>
- <https://www2.math.uu.se/~watuc425/CAPA/publications/papers/GaliasAndTucker2015>
- <https://home.cs.colorado.edu/~raf/media/papers/topent.pdf>
- <https://arxiv.org/abs/1001.4211>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Periodic-orbit counts alone give an entropy estimate, not a rigorous lower bound; a semiconjugacy or horseshoe argument is required.
- The Newhouse et al. trellis paper and Grote's MSU thesis may contain larger values; the thesis was access-limited when this entry was written, so search it before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/henon-topological-entropy-rigorous-bounds.md
```

Already set up? Say `run V3R1T4S on henon-topological-entropy-rigorous-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `henon-topological-entropy-rigorous-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
