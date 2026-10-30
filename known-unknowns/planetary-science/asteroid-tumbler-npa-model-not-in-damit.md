# Physical model of a tumbling (non-principal-axis) asteroid from public lightcurves, beyond the tumbler models in DAMIT

🪐 **Planets and moons** · standard · tractability ★★☆☆☆ · compute: laptop-hours (ALCDEF lightcurves are KB-MB per object; NPA inversion over a period grid takes hours per object) · open as of 2026-10-30

## The problem

Most asteroids spin about their shortest axis; tumblers are in non-principal-axis (NPA) rotation, usually slow rotators whose damping time exceeds their age (Pravec et al. 2005, 2014). The Asteroid Lightcurve Database flags many objects as tumbling or possibly tumbling. Full physical NPA models (shape, the two periods, angular-momentum direction and inertia ratios) are rare. DAMIT (Durech, Sidorin and Kaasalainen 2010; run by J. Durech and V. Sidorin) holds 27,963 models of 18,033 asteroids, but on 2026-10-30 its tumbler section has 8 models of only 5 objects: 2008 TC3, (99942) Apophis, 2012 TC4, (319) Leona and (469219) Kamo'oalewa. Some other tumblers have been modelled from radar or lightcurves, e.g. (4179) Toutatis and (5247) Krylov (Lee et al. 2020). The ALCDEF database (B. D. Warner and collaborators) holds 387,503 lightcurve blocks for 24,819 objects (updated 2026-10-28), and survey photometry adds sparse points. Open task: a physical NPA model for a tumbler that DAMIT and the literature do not have.

## What counts as a win

A saved bundle (ALCDEF and other photometry with times and errors, Horizons geometry, model code, fitted parameters and residuals) where: (1) a 2D Fourier series in two frequencies (Pravec et al. 2005) of order >= 2 fits the dense lightcurves with chi^2 lower by >= 25 than the best single-period Fourier series with at least as many free parameters (period scanned over the whole plausible range), and the two frequencies are not in a ratio of small integers (up to 1:6) within their errors; (2) a physical NPA model (convex or ellipsoid shape, precession and rotation periods, angular-momentum direction, inertia ratios, epoch angles) reproduces data from >= 2 apparitions or >= 2 viewing geometries >= 20 deg apart with RMS residual <= 1.2 x the photometric noise; (3) the model is stable: >= 80% of 50 fits started from random initial angles converge to the same periods within 1% and pole within 20 deg; (4) the object is not in https://damit.cuni.cz/projects/damit/tumblers and no paper gives a physical NPA model for it (re-checked immediately before claiming).

## Partial wins

- **p1:** The pipeline reproduces DAMIT's precession and rotation periods (P_phi, P_psi) of (99942) Apophis or 2012 TC4 within 1% with a physical NPA model fitted to public photometry only, with residuals saved.
- **p2:** A new tumbling detection meeting test (1) for an asteroid with an LCDB period but no tumbling flag, without a physical model.
- **p3:** A physical NPA model meeting (2) and (4) with one apparition only and the stability test (3) passed.

## How a win is checked

Skeptic re-downloads the ALCDEF blocks by object, recomputes geometry from Horizons, refits single- and two-frequency Fourier series, reruns the NPA fit from random starts with independent code, and checks the DAMIT tumbler list. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://damit.cuni.cz/projects/damit/tumblers>

## Sources

- <https://damit.cuni.cz/projects/damit/tumblers>
- <https://damit.cuni.cz/>
- <https://alcdef.org/>
- <https://www.minorplanet.info/php/lcdb.php>
- <https://ssd.jpl.nasa.gov/horizons/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: start from LCDB objects with tumbling flags and long, dense ALCDEF coverage; 2D Fourier analysis first, physical inversion second.
- Add TESS full-frame-image photometry, whose month-long continuous coverage is ideal for slow tumblers.
- Cross-domain import (spacecraft attitude determination): tumbling-satellite lightcurve inversion uses the same torque-free Euler equations and has mature estimators (unscented filters).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Slow rotators need long nightly runs; sparse survey data alone rarely constrain an NPA model.
- Combining lightcurves from different observers needs careful zero-point handling; ALCDEF blocks often have arbitrary offsets.
- A binary asteroid with an unsynchronised secondary also shows two periods; check for mutual-event dips before calling it a tumbler.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/asteroid-tumbler-npa-model-not-in-damit.md
```

Already set up? Say `run V3R1T4S on asteroid-tumbler-npa-model-not-in-damit`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `asteroid-tumbler-npa-model-not-in-damit`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
