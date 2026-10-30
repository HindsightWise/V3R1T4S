# New irregular (or small inner) satellite of Jupiter, Saturn, Uranus or Neptune in public archival images, shown bound by an orbit fit

🪐 **Planets and moons** · standard · tractability ★★☆☆☆ · compute: laptop-days (tens of GB of archival CCD frames per planet field per night; shift-and-stack over a grid of rates) · open as of 2026-10-30

## The problem

Irregular satellites are still being found in old images. The JPL list of planetary satellites (re-fetched 2026-10-30) gives Jupiter 115, Saturn 293, Uranus 29 and Neptune 16. Most of its 2025-2026 additions came from data taken years earlier: 20 Jupiter moons announced in MPECs 2025-H and 2026-F/G from 2010-2024 images (17 credited to S. S. Sheppard alone, two to Sheppard with D. J. Tholen, one of them also with C. Trujillo, and S/2010 J5 to E. J. Ashton, M. Beaudoin, B. J. Gladman and S. Deen), and 147 Saturn moons announced in MPECs 2025-E153/154/155 and 2026-F14, G68-G72, G74-G75 and M19, found in 2004-2023 data by Sheppard, Jewitt, Kleyna, Ashton, Gladman, Petit, Alexandersen, Fraser, Lawler and Kavelaars (S/2009 S2 credited to the Cassini Imaging Science Team). The other recent additions are S/2025 U1 (El Moutamid, Hedman, Showalter, Tiscareno, de Pater, Lissauer and Souami; 2025 JWST images, CBET 5593) and, from 2024, S/2023 U1 and S/2021 N1 (Sheppard, Tholen, Trujillo and Lykawka; MPEC 2024-D112). Shift-and-stack along trial satellite rates (as in Ashton, Gladman and colleagues' searches) reaches well below the single-frame limit. Deep giant-planet fields from CFHT MegaCam (CADC), Subaru Suprime-Cam/HSC (SMOKA), DECam (NOIRLab Astro Data Archive) and HST/JWST (MAST) are public after their proprietary periods. Open task: a satellite that none of these lists or announcements contain, found in public images and shown by an orbit fit to be bound to its planet.

## What counts as a win

A saved bundle (frame list with archive URLs, astrometric and photometric calibration against Gaia DR3, stacking code, stacked cutouts, ADES-format astrometry, orbit-fit code and output) where: (1) the object is detected at >= 5 sigma in stacks on >= 3 nights spanning >= 20 days, and the rate of each night's best stack matches the motion predicted by the final orbit to within 0.2 arcsec/hr; (2) an N-body fit (Sun, all giant planets from JPL DE440/Horizons) to all astrometry has RMS <= 0.3 arcsec, and >= 95% of >= 1,000 orbits sampled from the fit covariance (or MCMC) are bound to the planet (planetocentric energy < 0) with apocentre < 0.7 Hill radii; (3) at each epoch no designated satellite lies within 60 arcsec of the object, per JPL Horizons ephemerides for every satellite on https://ssd.jpl.nasa.gov/sats/discovery.html, and no known asteroid lies within 30 arcsec (IMCCE SkyBoT); (4) the object is not on the JPL discovery page, no MPEC in the MPC archive announces it, and no paper or preprint reports it (all re-fetched immediately before claiming). Reporting to the MPC is a human action and is not part of the win.

## Partial wins

- **p1:** The pipeline recovers >= 80% of the designated satellites predicted (Horizons) to lie in the processed frames with V brighter than the stacks' 5-sigma limit minus 0.5 mag, with the recovered list, missed list and limit saved.
- **p2:** A candidate meeting (3) and (4) seen at >= 5 sigma on 2 nights >= 1 day apart, with rates consistent with a bound orbit, but without the 20-day arc of (1).
- **p3:** Archival precovery astrometry (residuals <= 0.3 arcsec against the current JPL orbit) of a satellite announced in 2025-2026 that extends its observed arc, as stated in its MPEC, by >= 1 year.

## How a win is checked

Skeptic re-downloads the listed frames, re-runs the stack at the saved rates, re-measures astrometry against Gaia DR3, refits the orbit with an independent integrator, re-samples the covariance, and queries Horizons and SkyBoT for each epoch. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ssd.jpl.nasa.gov/sats/discovery.html>

## Sources

- <https://ssd.jpl.nasa.gov/sats/discovery.html>
- <https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/ssois/>
- <https://astroarchive.noirlab.edu/>
- <https://mast.stsci.edu/>
- <https://ssd.jpl.nasa.gov/horizons/>
- <https://ssp.imcce.fr/webservices/skybot/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: shift-and-stack of CFHT or Subaru frames over a rate grid around the planet's motion (Ashton and Gladman style), masking the planet's scattered light with a radial model.
- Many archival planet fields were taken for other programmes (rings, outer moons' astrometry, occultation support); SSOIS finds every frame within a few degrees of the planet.
- Cross-domain import (radar): treat the rate grid as a matched-filter bank and set the threshold from the empirical false-alarm rate in off-planet control stacks.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The JPL page's own 'last updated' line is stale; the per-satellite MPEC references are the live information.
- Discovery teams hold many unannounced candidates; a new announcement can appear at any time, so re-check MPECs before claiming.
- Stacks at the planet's rate also build up slow background TNOs and Hildas/Trojans near the field; the bound-orbit test (2) and SkyBoT check (3) are what separate them.
- Scattered light and ghosts near the planet produce coherent stack artefacts; require the detection in independent stacks of different frame subsets.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/giant-planet-satellite-archival-shift-and-stack.md
```

Already set up? Say `run V3R1T4S on giant-planet-satellite-archival-shift-and-stack`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `giant-planet-satellite-archival-shift-and-stack`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
