# A new YORP detection: significant change in an asteroid's rotation rate measured from decades of public lightcurves

🪐 **Planets and moons** · standard · tractability ★★☆☆☆ · compute: laptop-hours (lightcurves KB-MB per object; convex inversion with a linear frequency change over a period grid takes hours) · open as of 2026-10-30

## The problem

The YORP effect changes asteroid spin rates through thermal emission, and only lightcurves spanning decades show it. Durech et al. (A&A 2022, doi:10.1051/0004-6361/202141844) measured spin-up for (10115) 1992 SK, confirmed (1685) Toro and refined (1620) Geographos (ten detections); Durech et al. (A&A 2024, doi:10.1051/0004-6361/202348350) added (2100) Ra-Shalom and (138852) 2000 WN10, bringing the total to twelve, all spinning up, and showed that a reported detection for (85989) 1999 JD6 is not statistically required. Earlier detections include (54509) YORP, (1862) Apollo, (3103) Eger, (25143) Itokawa, (161989) Cacus, (68346) 2001 KZ66 and (101955) Bennu (Lowry, Taylor, Kaasalainen, Durech, Vokrouhlicky, Pravec, Nolan and others). Feng et al. (ApJ 2025, doi:10.3847/1538-4357/addd23) reported a spin-down for (433) Eros of (-5.0 +/- 4.6) x 10^-10 rad/day^2, not significant, and Rodriguez Rodriguez et al. (PSJ 2026, doi:10.3847/PSJ/ae2d11) a possible acceleration of about 2.05 x 10^-8 rad/day^2 for (66146) 1998 TU3. Whether any asteroid is measurably spinning down remains open: theory predicts both signs. Public photometry (ALCDEF, published lightcurves, survey data) now spans 30-70 years for many NEAs and Mars-crossers. Open task: a statistically significant rotation-rate change for an asteroid with no published YORP detection or YORP value.

## What counts as a win

A saved bundle (all photometry with times and sources, Horizons geometry, inversion code, best models with and without YORP, bootstrap output) where: (1) the data cover >= 3 apparitions spanning >= 10 years, including >= 2 dense lightcurves; (2) a convex-inversion model with a linearly changing rotation rate, dw/dt = nu, beats the best constant-rate model by delta chi^2 >= 25 with the same shape resolution; (3) nu / sigma(nu) >= 3, with sigma(nu) from >= 200 bootstrap resamplings of whole lightcurves; (4) nu stays significant at >= 3 sigma when any single apparition is left out; (5) |nu| <= 1e-5 rad/day^2 (the largest measured value, for (54509) YORP, is about 3.5e-6 rad/day^2); (6) no paper, preprint or DAMIT model reports a YORP value for the object (re-checked immediately before claiming). A significant negative nu (spin-down) meets the same criterion.

## Partial wins

- **p1:** The pipeline reproduces a published YORP value (e.g. (1862) Apollo or (1620) Geographos) within 1 sigma from public photometry only, with all inputs saved.
- **p2:** An object meeting (1), (5) and (6) with 2 <= nu / sigma(nu) < 3 and test (4) passed at 2 sigma: a candidate that names the apparitions it needs next.

## How a win is checked

Skeptic re-collects the photometry from the cited sources, re-runs inversion with and without nu from independent starting poles, re-runs the bootstrap and the leave-one-apparition-out test, and searches the literature. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://api.semanticscholar.org/graph/v1/paper/DOI:10.3847/1538-4357/addd23?fields=title,abstract,year,venue>

## Sources

- <https://doi.org/10.1051/0004-6361/202141844>
- <https://doi.org/10.1051/0004-6361/202348350>
- <https://doi.org/10.3847/1538-4357/addd23>
- <https://doi.org/10.3847/PSJ/ae2d11>
- <https://api.semanticscholar.org/graph/v1/paper/DOI:10.3847/1538-4357/addd23?fields=title,abstract,year,venue>
- <https://alcdef.org/>
- <https://damit.cuni.cz/>
- <https://www.minorplanet.info/php/lcdb.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: pick NEAs with dense lightcurves from the 1970s-1990s (published in Icarus, A&A and Minor Planet Bulletin) and recent ALCDEF data.
- Gaia DR3 sparse photometry and TESS lightcurves add precise recent epochs that pin the rotation phase.
- Cross-domain import (pulsar timing): the YORP fit is a phase-coherent timing solution with a frequency derivative; pulsar-timing tools for phase connection across gaps apply directly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rotation-phase counting across long gaps is ambiguous; wrong cycle counts imitate a frequency change. Show the cycle-count solution is unique.
- Old photographic or photoelectric timings may be in local or uncorrected time; check light-time correction and time standards.
- Only twelve detections are known and the community checks candidates closely; claim nothing without (4).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/asteroid-yorp-detection-beyond-twelve.md
```

Already set up? Say `run V3R1T4S on asteroid-yorp-detection-beyond-twelve`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `asteroid-yorp-detection-beyond-twelve`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
