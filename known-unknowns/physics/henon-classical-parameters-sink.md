# MOONSHOT - Is the Henon attractor a sink? A certified attracting periodic orbit at exactly (a, b) = (1.4, 0.3), or a sink closer than Galias-Tucker's

⚛️ **Physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (exhaustive symbol-sequence search at periods > 100 with multiprecision continuation; partial wins need laptop-days) · open as of 2026-10-30

## The problem

The Henon map is h(x,y) = (1 + y - a x^2, b x), and its classical parameters are (a,b) = (1.4, 0.3). It is not known whether the attractor seen there is strange or is a stable periodic orbit with an extremely narrow basin. Benedicks-Carleson theory covers only small b, and Anikushin and Romanov (arXiv 2503.11150, 2025) state that chaos of the classical attractor is not rigorously established. Zbigniew Galias and Warwick Tucker (Chaos 24, 013120 (2014)) proved a period-28 sink at (1.4, 0.2999999774905). In Chaos 25, 033102 (2015) they combined the Biham-Wenzel method with continuation and proved (interval Newton) 90,510 sink regions of period <= 41 in [1.3999, 1.4001] x [0.2999, 0.3001]; the closest is a period-41 window at distance < 4.728e-10. Their Theorem 1 gives a period-115 sink at a = 1.39999999999999999999968839903277301984563091568983, b = 0.29999999999999999999944845519288458244332946957783, at Euclidean distance < 6.335e-22 from (1.4, 0.3). They also prove that the period-115 sink exists at a = 1.4 exactly with b = 0.29999999999999999999927578971518934110292052859235 (|b - 0.3| < 7.243e-22). They estimate that a sink at the classical point, if one exists, would be practically impossible to see by simulation.

## What counts as a win

Main win: a period-p orbit of h at exactly a = 7/5, b = 3/10 with a computer-assisted proof of existence (interval Newton or Krawczyk on the p-periodic system) and of attraction: an interval enclosure of the monodromy matrix M (the product of the p Jacobians, with det M = (-3/10)^p exactly) satisfying |tr M| < 1 + det M, so that both eigenvalues lie strictly inside the unit circle.

## Partial wins

- **p1:** A sink certified the same way at rational parameters (a,b) whose exact Euclidean distance to (7/5, 3/10) is strictly less than 6.3347994e-22, the exact distance of Galias-Tucker 2015's Theorem 1 period-115 sink (stated there as < 6.335e-22), and less than any closer published value found by a literature search.
- **p2:** A sink certified the same way with a = 7/5 exactly and rational b with |b - 3/10| strictly less than 7.2421e-22 (closer than Galias-Tucker 2015's a = 1.4 period-115 sink at b = 0.29999999999999999999927578971518934110292052859235), and closer than any a = 1.4 sink found by a literature search.

## How a win is checked

Skeptic: from the posted p, the parameters (exact rationals), a point enclosure for each orbit point and the symbol sequence, run an independent interval Newton (or Krawczyk) step on F(z_0..z_{p-1}) = (z_{i+1} - h(z_i)) at precision at least 60 decimals per 100 periods. Then enclose M by interval matrix products and check |tr M| < 1 + det M. For p1 and p2, compute the distance in exact rational arithmetic. Minutes to hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2503.11150>

## Sources

- <https://www2.math.uu.se/~watuc425/CAPA/publications/papers/GaliasAndTucker2015>
- <https://doi.org/10.1063/1.4913945>
- <https://www2.math.uu.se/~watuc425/CAPA/publications/papers/chaossubmitted20140128.pdf>
- <https://arxiv.org/abs/2503.11150>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Galias-Tucker found that admissible sequences avoid (- - -), (+ + +), (- - +) and 28 longer forbidden blocks; enumerate only pruned sequences and continue each unstable orbit toward the classical point.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Long simulated trajectories that look periodic are not evidence: transients near (1.4, 0.3) last far beyond any feasible simulation.
- Floating-point parameters such as 1.4 are not exactly 7/5; certify with exact rationals or tight intervals around them.
- Interval wrapping over 100+ iterates explodes: use the multiple-shooting formulation, never a single long composition.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/henon-classical-parameters-sink.md
```

Already set up? Say `run V3R1T4S on henon-classical-parameters-sink`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `henon-classical-parameters-sink`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
