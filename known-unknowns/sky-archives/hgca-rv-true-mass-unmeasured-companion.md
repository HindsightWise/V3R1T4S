# First true (dynamical) mass for an RV-detected companion from Hipparcos-Gaia accelerations plus public radial velocities

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (an orvara fit is minutes to an hour; data are KB) · open as of 2026-10-28

## The problem

Radial velocities give only m sin i. Combining public RVs with the Hipparcos-Gaia Catalog of Accelerations (HGCA; Brandt 2021) using orvara (Brandt et al. 2021) or kepmodel yields the inclination and true mass. Large applications exist (Xiao et al. 2023 for 115 substellar companions, arXiv:2303.12409; Feng et al. 2022; Piccinini et al. 2026, arXiv:2601.09401), but on 2026-10-28 the NASA Exoplanet Archive composite table (PSCompPars) still had 924 of its 6,451 planets with mass provenance pl_bmassprov = 'Msini'. Open task: produce a robust true-mass measurement for a companion whose archive entry has no published true mass and no published astrometric inclination.

## What counts as a win

A saved bundle (HGCA EDR3 row, all RV data with provenance, orvara/kepmodel config and posterior chains) for a companion whose live archive row (https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars, re-fetched immediately before claiming) has pl_bmassprov = 'Msini' (checkable with the TAP query https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,pl_bmassprov+from+pscomppars+where+pl_bmassprov='Msini'&format=csv), with: HGCA proper-motion anomaly chi^2 > 11.8 (3 sigma, 2 dof); converged chains (Gelman-Rubin < 1.01 across >= 4 independent runs); true mass with fractional 1-sigma uncertainty < 30% and inclination excluding 90 +/- 10 deg or a mass ratio that changes the object's class; no unexplained additional companion in residuals; and no prior paper (ADS/arXiv full-text search on host name with 'inclination' or 'Hipparcos-Gaia') reporting a true mass.

## Partial wins

- **p1:** A reproducible table re-deriving true masses for >= 10 companions from Xiao et al. 2023 within 1 sigma (validates the pipeline).
- **p2:** A significant (3 sigma) HGCA acceleration that is inconsistent with all known companions in the system, implying an additional unseen companion, with a mass-separation curve.
- **p3:** An archive companion with m sin i < 13 MJup shown to have true mass > 13 MJup (or > 80 MJup) at > 3 sigma, not previously reported.

## How a win is checked

Skeptic reinstalls orvara, runs the saved config on the saved RVs and HGCA row with new seeds, checks the posterior and chi^2, re-fetches the archive row and searches ADS. Under an hour per object.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars>

## Sources

- <https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars>
- <https://vizier.cds.unistra.fr/viz-bin/VizieR?-source=J/ApJS/254/42>
- <https://arxiv.org/abs/2001.05942>
- <https://arxiv.org/abs/2311.12438>
- <https://github.com/t-brandt/orvara>
- <https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,hostname,pl_bmassprov+from+pscomppars+where+pl_bmassprov='Msini'&format=csv>
- <https://arxiv.org/abs/2303.12409>
- <https://arxiv.org/abs/2601.09401>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: rank archive companions by predicted HGCA signal (m sin i, period, distance) and run orvara on those with significant proper-motion anomalies and public RVs (HARPS RVBank, published tables on VizieR).
- Add Gaia DR3 NSS acceleration or orbital solutions as a third constraint where available.
- Cross-domain import (satellite orbit determination): use a square-root information filter / batch least squares with covariance analysis to show which observations actually constrain inclination.
- Cross-domain import (structural engineering): sensitivity analysis via Sobol indices on the posterior to expose priors driving the inclination.
- Cross-domain import (election forecasting): pre-register selection rules and report all fits, not only the striking ones, to avoid a forking-paths win.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The HGCA anomaly can come from a different, wide stellar companion; check Gaia for co-moving neighbours and imaging literature.
- Archive 'Msini' flags can lag the literature; the novelty check must be a paper search, not just the archive flag.
- Poorly sampled long-period orbits give bimodal inclination posteriors; a single mode reported as a mass is a false win.
- HARPS 2015 fibre upgrade offset must be a separate instrument offset; forgetting it fakes a trend.
- Prior choice (uniform in cos i vs uniform in i) can drive results when data are weak; report prior sensitivity.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/hgca-rv-true-mass-unmeasured-companion.md
```

Already set up? Say `run V3R1T4S on hgca-rv-true-mass-unmeasured-companion`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hgca-rv-true-mass-unmeasured-companion`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
