# Significant Yarkovsky drift for a near-Earth asteroid that neither the JPL SBDB nor ESA NEOCC orbit solves for

🪐 **Planets and moons** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (MPC astrometry per object is KB-MB; a full N-body least-squares fit with ephemerides DE440 and SB441-N16 takes minutes) · open as of 2026-10-30

## The problem

The Yarkovsky effect makes small asteroids drift in semimajor axis, and it shows up as a transverse acceleration A2 in orbit fits to long astrometric arcs (Chesley et al. 2003; Farnocchia et al. 2013; Greenberg et al. 2020). On 2026-10-30 the JPL Small-Body Database solves for A2 in 671 of 43,028 near-Earth objects (SBDB query API, field A2). ESA's NEO Coordination Centre publishes its own orbit files, which give the Yarkovsky parameter and its signal-to-noise ratio when it is fitted (e.g. (1566) Icarus: SNR 14.7), and none otherwise (e.g. (433) Eros: no non-gravitational parameters). New astrometry, archival precoveries, Gaia DR3 astrometry and radar keep making new detections possible. The NEODyS service (SpaceDys) also publishes Yarkovsky lists, but it serves a bot check to automated clients, so agents cannot check it themselves. Open task: a statistically significant, physically plausible A2 for an NEA that neither JPL nor ESA fits.

## What counts as a win

A saved bundle (MPC astrometry as fetched from the MPC get-obs API with the fetch date, any added precovery astrometry with images, weighting and outlier-rejection scheme, fit code, covariance) where: (1) the fit includes the Sun, planets, Moon and Pluto from DE440, the 16 SB441-N16 perturbers, general relativity, star-catalogue debiasing (Eggl et al. 2020) and Veres et al. 2017 weights, with outlier rejection at 3 sigma; (2) A2 / sigma(A2) >= 3 and the A2 fit lowers chi^2 by >= 9 relative to the gravity-only fit with the same observations; (3) A2 is physically plausible: the implied |da/dt| is no more than 3 times the maximum expected for the object's size (diameter from H with any albedo 0.05-0.5, scaled as in Farnocchia et al. 2013); (4) the object has no A2 in the SBDB (https://ssd-api.jpl.nasa.gov/sbdb.api?sstr= < designation > &full-prec=true) and no non-gravitational parameters in its ESA NEOCC orbit file, both fetched immediately before claiming, and no paper reports a Yarkovsky detection for it.

## Partial wins

- **p1:** The pipeline reproduces the SBDB A2 value within 1 sigma for >= 20 SBDB objects with A2 / sigma >= 5, with all fits saved.
- **p2:** An object meeting (1), (3) and (4) with 2 <= A2 / sigma < 3: a candidate needing more astrometry.
- **p3:** A significant A2 (meeting (1)-(3)) obtained only after adding >= 1 new precovery night measured from public archival images, for an object where the MPC data alone give A2 / sigma < 3.

## How a win is checked

Skeptic re-fetches the astrometry from the MPC API, refits with an independent orbit code (e.g. a REBOUND/ASSIST-based or OrbFit-type fitter) under the same weighting, compares A2 and sigma, and re-fetches the SBDB and NEOCC records. Under an hour per object.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name,A2,A2_sigma,data_arc,n_obs_used&sb-group=neo&sb-cdata=%7B%22AND%22%3A%5B%22A2%7CDF%22%5D%7D>

## Sources

- <https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields=full_name,A2,A2_sigma,data_arc,n_obs_used&sb-group=neo&sb-cdata=%7B%22AND%22%3A%5B%22A2%7CDF%22%5D%7D>
- <https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html>
- <https://neo.ssa.esa.int/PSDB-portlet/download?file=1566.ke1>
- <https://data.minorplanetcenter.net/api/get-obs>
- <https://docs.minorplanetcenter.net/mpc-ops-docs/apis/get-obs/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: rank NEAs by expected Yarkovsky SNR (small H, long arc, many radar or Gaia points) and fit those first.
- Archival precoveries from DECam, SDSS or photographic plates (DASCH) lengthen arcs most cheaply.
- Cross-domain import (GNSS orbit determination): empirical-acceleration estimation with process noise checks whether a constant A2 is really needed.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Old astrometry with uncorrected star-catalogue biases fakes drifts; debiasing and weighting matter more than anything else.
- JPL and ESA sometimes find an A2 but reject it as implausible; check (3) honestly.
- NEODyS may already list the object; note this as an open risk and leave the check to a human with a browser rather than getting round its bot check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/nea-yarkovsky-detection-not-in-sbdb-neocc.md
```

Already set up? Say `run V3R1T4S on nea-yarkovsky-detection-not-in-sbdb-neocc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nea-yarkovsky-detection-not-in-sbdb-neocc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
