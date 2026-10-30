# Hilbert numbers H(3)..H(8): a planar polynomial vector field with more limit cycles than 13, 28, 37, 53, 74 or 96

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (exact symbolic Melnikov or Lyapunov computations for degree 4-8 families) · open as of 2026-10-30

## The problem

H(d) is the maximal number of limit cycles of a planar polynomial vector field of degree d. The best explicit lower bounds for small d, from Table 1 of Chaoyang Qin and Xiaoming Sun (arXiv 2610.12218, 8 Oct 2026, whose own result improves only the asymptotic d^2 log d growth), are: H(3) >= 13 (Chengzhi Li, Changjian Liu and Jiazhong Yang, J. Differential Equations 246 (2009) 3609-3619, via Poincaré-Pontryagin-Melnikov perturbation of a cubic Hamiltonian); H(4) >= 28, H(5) >= 37, H(6) >= 53, H(7) >= 74 and H(8) >= 96 (Rafel Prohens and Joan Torregrosa, Nonlinearity 32 (2019) 331-355, perturbations of reversible centers). Torregrosa (São Paulo J. Math. Sci. 19:4, 2025) also confirms 13 as the highest known for cubic systems in a global configuration (other 13-cycle cubic configurations: Liu-Li 2014, Yang-Han-Li-Yu, Zhao).

## What counts as a win

For some d in 3..8, an explicit degree-d planar polynomial vector field, or family, with at least T(d) + 1 limit cycles, where T = (13, 28, 37, 53, 74, 96) for d = 3..8 (direction: max), also beating any later value found by a literature search re-run just before claiming. Certified either by interval-validated Poincaré return maps (one sign change of the displacement per cycle, with distinct cycles shown) or by exact-arithmetic verification of every hypothesis of a cited bifurcation theorem (Melnikov or Abelian-integral simple zeros, the Lyapunov-constant rank, averaging) giving that many limit cycles for small parameters.

## Partial wins

- **p1:** A cubic system with 13 limit cycles in which all 13 are certified simultaneously by validated numerics at one explicit rational parameter value (not only 'for epsilon small enough'), such that no such single-parameter validated certificate of 13 cubic limit cycles is found by a literature search re-run before claiming.
- **p2:** The same explicit-parameter validated certificate for a quartic system with 28 limit cycles, such that no such certificate for 28 quartic limit cycles is found by a literature search re-run before claiming.

## How a win is checked

For bifurcation certificates: recompute the first-order (or higher) Melnikov function or Lyapunov constants in exact rational or algebraic arithmetic (Sage, Singular), check the claimed number of simple zeros with Sturm sequences or the rank condition, and check that the theorem cited applies. For validated certificates: re-run an interval ODE integrator from each segment endpoint. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.12218>

## Sources

- <https://arxiv.org/abs/2610.12218>
- <https://ddd.uab.cat/pub/artpub/2025/307743/saopaujou_a2025m6v19n1p4.pdf>
- <https://doi.org/10.1088/1361-6544/aae94d>
- <https://doi.org/10.1016/j.jde.2009.01.038>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Counting limit cycles in different nests requires that the perturbation is small enough for all of them simultaneously; a certificate that treats the nests with separate small parameters proves less.
- Zeros of a Melnikov function count only if they are simple, or of certified odd multiplicity, and lie inside the period annulus.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/hilbert-numbers-degree-3-to-8-lower-bounds.md
```

Already set up? Say `run V3R1T4S on hilbert-numbers-degree-3-to-8-lower-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hilbert-numbers-degree-3-to-8-lower-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
