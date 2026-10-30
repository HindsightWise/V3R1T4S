# First measured mass (TTV or RV, public data only) for a transiting planet whose NASA Exoplanet Archive mass still comes from a mass-radius relation

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (transit-time extraction from Kepler/TESS light curves plus TTVFast/N-body or Keplerian RV fits; data are MB per system) · open as of 2026-10-30

## The problem

On 2026-10-30 the NASA Exoplanet Archive composite table (PSCompPars) lists 6,451 planets; 3,035 of them, all transiting, have pl_bmassprov = 'M-R relationship', meaning no measured mass (2,310 Kepler, 396 K2, 326 TESS discoveries). Of these, 160 carry ttv_flag = 1 and 139 orbit stars brighter than V = 11. Public data can still yield masses: Kepler and TESS transit times (Rowe et al. 2015; Holczer et al. 2016; Hadden & Lithwick 2017 analysed the TTVs of 145 planets in 55 Kepler systems), and public radial velocities (ESO HARPS/ESPRESSO Phase 3 products, Keck KOA HIRES, the HARPS RVBank of Trifonov et al. 2020). The archive's default parameter set can lag the literature, so novelty is judged on all archive rows plus a paper search. Open task: a robust first dynamical mass for such a planet, credited to the archive team (Akeson et al. 2013; Christiansen et al. 2025) for the census.

## What counts as a win

A saved bundle (planet name, the archive rows as fetched, all transit times or RVs with provenance, model configuration, posterior chains) for a planet whose PSCompPars row has pl_bmassprov = 'M-R relationship' (TAP: select pl_name,pl_bmassprov from pscomppars where pl_bmassprov='M-R relationship') and none of whose rows in the PS table (select pl_name,pl_bmassprov,pl_refname from ps where pl_name='NAME') has a pl_bmassprov other than 'M-R relationship' or empty (so no 'Mass', 'Msini' or 'Msin(i)/sin(i)' row), both re-fetched immediately before claiming, with: (1) mass / sigma >= 3; (2) TTV route: dynamical model preferred over linear ephemerides by delta BIC > 10, at least 4 independent chains with R-hat < 1.01, the mass stable within 1 sigma under two different eccentricity priors, and the perturber identified (a known transiting planet, or a unique non-transiting solution after an alias search); RV route: K detected at the transit period and phase at >= 3 sigma, instrument offsets free, and no activity-indicator peak at that period; (3) no paper found by an ADS/arXiv search on the planet and host names with 'mass', 'TTV' or 'radial velocity' reports a measured mass.

## Partial wins

- **p1:** Reproduce at least 10 of the Hadden & Lithwick 2017 TTV masses within 1 sigma with the bundle's pipeline (validation).
- **p2:** For an eligible planet, a 99.7% upper limit on the mass below half of the archive's M-R mass, with the same data-provenance and chain rules, where no paper found by the same search reports an equal or tighter mass upper limit.
- **p3:** A unique non-transiting perturber solution (period, mass, eccentricity) explaining significant TTVs (delta BIC > 20 over linear) of an eligible planet, not in any paper found by the search.
- **p4:** Released transit times, with a significance test against a linear ephemeris, for every eligible planet with ttv_flag = 1 at claim time (160 on 2026-10-30), listing those with p < 1e-4.

## How a win is checked

Skeptic re-fetches the two archive queries, re-extracts a random subset of transit times or re-downloads the RVs, reruns the fit with new seeds and both eccentricity priors, and repeats the literature search. Under an hour per planet.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_bmassprov,count(*)+from+pscomppars+group+by+pl_bmassprov&format=csv>

## Sources

- <https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars>
- <https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_bmassprov,count(*)+from+pscomppars+group+by+pl_bmassprov&format=csv>
- <https://exoplanetarchive.ipac.caltech.edu/docs/pscp_about.html>
- <https://arxiv.org/abs/1606.01744>
- <https://arxiv.org/abs/1611.03516>
- <https://archive.stsci.edu/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: start from the 160 ttv_flag planets, measure transit times from Kepler short cadence plus TESS, and fit pairs near first-order resonance with the Lithwick-Xie-Wu analytic model before full N-body.
- Synchronous chopping signals break the mass-eccentricity degeneracy; prioritise pairs with high SNR transits.
- Cross-domain import (pulsar timing): a joint timing model with red-noise terms keeps stellar-activity timing noise from inflating TTV significance.
- Bright TESS hosts (V < 11) may have public HARPS or HIRES spectra taken for other programmes; query the ESO and KOA archives by coordinates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The composite table picks one default solution: a measured mass can exist in another PS row or in a paper the archive has not ingested.
- TTV masses are degenerate with eccentricity (Lithwick, Xie & Wu 2012); a mass that moves with the eccentricity prior is not a measurement.
- Kepler long-cadence smearing biases short-duration transit times; use short cadence where available.
- The archive's TAP service sits behind Cloudflare: a query with a subquery returned a block page on 2026-10-30. Keep queries simple and stop if blocked.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/archive-mr-mass-planet-first-dynamical-mass.md
```

Already set up? Say `run V3R1T4S on archive-mr-mass-planet-first-dynamical-mass`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `archive-mr-mass-planet-first-dynamical-mass`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
