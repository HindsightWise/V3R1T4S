# Local cyclicity M(n): 13 small-amplitude limit cycles from one cubic equilibrium, or beat M(4) >= 21, M(5) >= 33, M(6) >= 48, M(7) >= 61, M(8) >= 76, M(9) >= 88

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (high-order Lyapunov constants with parallel exact arithmetic, as in Liang-Torregrosa 2015) · open as of 2026-10-30

## The problem

M(n) is the maximal number of small-amplitude limit cycles that bifurcate from one elementary monodromic equilibrium (degenerate Hopf bifurcation) of a degree-n planar polynomial vector field; clearly M(n) <= H(n). Bautin proved M(2) = 3. For cubics, Zoladek's 1995 claim of 11 had gaps; 11 was proved by Christopher (2005) and Bondar-Sadovskii (2008), and Zoladek's family was revisited by Gouveia-Torregrosa (2021) and Tian-Yu. Pei Yu and Yun Tian (CNSNS 19 (2014)) found 12 in the CD12 family, with the proof completed by Jaume Gine, Luiz Gouveia and Joan Torregrosa (J. Differential Equations 275 (2021) 309-331), whose technique also gives M(4) >= 21. Gouveia and Torregrosa (JDE 271 (2021) 447-479) proved M(5) >= 33, M(7) >= 61, M(8) >= 76 and M(9) >= 88 (and M(4) >= 20); M(6) >= 48 is due to Bastos, Buzzi and Torregrosa (CPAA 2021). Joan Torregrosa (Sao Paulo J. Math. Sci. 19:4, 2025) found two new cubic families reaching 12 via Cremona transformations and lists 12 (cubic), 21 (quartic), 48 (sextic) and 33, 61, 76, 88 (n = 5, 7, 8, 9) as the best known. Higher orders exist only over the complex numbers: Graf and Kroker (2010) found complex curves of cubic weak foci of orders 12 and 13, and Sadovskii (2020) an explicit complex cubic system with a weak focus of order 14. For Kolmogorov systems, Carvalho, Da Cruz and Gouveia (arXiv 2304.05111, 2023) gave another example with M_K(3) >= 6 and proved M_K(4) >= 13 and M_K(5) >= 22.

## What counts as a win

For some n in 3..9, a degree-n polynomial family with a center or weak focus at the origin and an exact-arithmetic certificate that at least M + 1 small-amplitude limit cycles bifurcate from it, where M = 12, 21, 33, 48, 61, 76, 88 for n = 3..9 (direction: max), also beating any value found by a literature search re-run just before claiming. The certificate gives the Lyapunov constants, or the higher-order developments in the perturbation parameters, computed in exact rational or algebraic arithmetic, and verifies the rank or degeneracy conditions of a cited theorem (for example Christopher 2005 and Gine-Gouveia-Torregrosa 2021).

## Partial wins

- **p1:** Kolmogorov systems: an exact certificate that M_K(3) >= 7, M_K(4) >= 14 or M_K(5) >= 23, beating Carvalho-Da Cruz-Gouveia 2023 and any later value found by a literature search.

## How a win is checked

Skeptic: recompute the Lyapunov constants of the posted family in an independent computer algebra system (Sage, Singular, Maple) to the stated order, check the Jacobian rank or higher-order conditions exactly, check that the unperturbed system has a center (by the posted Darboux or reversibility certificate), and check that the perturbation stays within degree n. Hours to a day.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ddd.uab.cat/pub/artpub/2025/307743/saopaujou_a2025m6v19n1p4.pdf>

## Sources

- <https://ddd.uab.cat/pub/artpub/2025/307743/saopaujou_a2025m6v19n1p4.pdf>
- <https://ddd.uab.cat/pub/artpub/2021/236645/GouTor2020a.pdf>
- <https://arxiv.org/abs/2304.05111>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Torregrosa 2025 credits the n = 6 bound of 48 and the n = 5, 7, 8, 9 bounds to Gouveia-Torregrosa 2021 and Bastos-Buzzi-Torregrosa with the citation order swapped; the JDE 271 abstract states n = 4 (20), 5, 7, 8, 9, and its introduction attributes M(6) >= 48 to Bastos-Buzzi-Torregrosa.
- A first-order rank argument can fail to give the full count when the center family is more degenerate than predicted (Zoladek's 1995 gap); high-order developments must be checked.
- Complex weak foci of high order do not count: the bifurcating cycles must be real.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/local-cyclicity-centers-m3-thirteen.md
```

Already set up? Say `run V3R1T4S on local-cyclicity-centers-m3-thirteen`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `local-cyclicity-centers-m3-thirteen`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
