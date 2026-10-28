# New microlensing event in public ZTF light curves absent from published ZTF, Gaia and OGLE/KMTNet microlensing catalogues

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to overnight (ZTF light-curve parquet files for selected fields are tens of GB) · open as of 2026-10-28

## The problem

ZTF public data releases contain light curves for over a billion objects. The latest, DR24 (IRSA, 2026 January), covers about March 2018 to July 2024 for partnership and Caltech data, plus public-survey data to 2025-10-22. Published searches are Rodriguez et al. 2022 (Galactic plane, arXiv:2112.07684), Medford et al. 2023 (60 events in ZTF DR5, arXiv:2201.08335) and Zhai et al. 2025 (ApJ 978, 76, arXiv:2311.18627: 124 high-confidence plus 54 possible events in DR17 Galactic-plane fields). Other sources are the Gaia DR3 microlensing catalogue (Wyrzykowski et al. 2023, 363 events) and Gaia Science Alerts (about 27,000 alerts; the stream ended with Gaia25aeh on 2025-01-15). Later ZTF releases add years of data that no published catalogue covers. Open task: find a microlensing event in public ZTF light curves that is in none of these catalogues or alert streams.

## What counts as a win

A saved bundle (ZTF object IDs per filter, light curves as downloaded from IRSA, fit code) where a point-source point-lens (or finite-source / parallax) model fits g and r jointly with achromatic magnification (blend fractions allowed per filter), delta chi^2 versus a constant + linear model > 500, the rise and fall are each sampled by >= 5 points, the baseline is flat (RMS < 0.05 mag) for >= 1 year either side, the event is not a CV/YSO/Be outburst (achromaticity test, no repeat in the full baseline), and no entry exists within 2 arcsec in the Gaia Science Alerts list (http://gsaweb.ast.cam.ac.uk/alerts/alerts.csv), the Gaia DR3 microlensing table, the published ZTF catalogues (arXiv:2112.07684, 2201.08335, 2311.18627), or ADS/TNS-by-coordinate literature (arXiv status query https://export.arxiv.org/api/query?search_query=abs:microlensing+AND+abs:ZTF&sortBy=submittedDate&sortOrder=descending&max_results=50 re-run immediately before claiming).

## Partial wins

- **p1:** A reproducible pipeline that recovers >= 80% of the Medford et al. 2023 events from the public light curves with < 10 false positives per recovered event after vetting.
- **p2:** A new event with Einstein time tE > 100 d showing a significant annual-parallax signal (delta chi^2 > 50), a black-hole lens candidate class.
- **p3:** A new event off the Galactic plane (|b| > 15 deg) meeting every criterion.

## How a win is checked

Skeptic re-downloads the ZTF light curves, refits with an independent microlensing code (e.g. MulensModel or pyLIMA), checks achromaticity and baseline, and cross-matches catalogues by coordinates. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:microlensing+AND+abs:ZTF&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Sources

- <https://irsa.ipac.caltech.edu/data/ZTF/docs/releases/>
- <https://irsa.ipac.caltech.edu/Missions/ztf.html>
- <http://gsaweb.ast.cam.ac.uk/alerts/alertsindex>
- <https://arxiv.org/abs/2311.18627>
- <https://arxiv.org/abs/2201.08335>
- <https://arxiv.org/abs/2112.07684>
- <https://vizier.cds.unistra.fr/viz-bin/VizieR>
- <https://export.arxiv.org/api/query?search_query=abs:microlensing+AND+abs:ZTF&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: run the Medford-style cuts (von Neumann ratio, chi^2 of flat fit, Paczynski fit) on the newest public DR light curves for epochs after the DR17 search.
- Search the outer disk and halo fields where survey teams rarely look; long-tE events give parallax and lens masses.
- Cross-domain import (particle physics): template bank of Paczynski curves in (t0, tE, u0) scanned like a trigger, with a background estimated by time-reversed or scrambled light curves.
- Cross-domain import (anomaly detection in industrial telemetry): autoencoders trained on 'normal' light curves score the symmetric single-bump shape as an anomaly class.
- Cross-domain import (medical imaging): use the g/r achromaticity test as a 'dual-energy' discriminator, analogous to separating tissue types by spectral response.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- CVs, Be stars and young stellar objects produce symmetric bumps; check colour change and repeated outbursts over the 7+ year baseline.
- ZTF ref-image changes and fields/CCD edges produce step-like artefacts; require consistency across ZTF field IDs.
- Events already reported by Gaia alerts, OGLE or KMTNet near the bulge appear under other names; cross-match by coordinates.
- Short events sampled only at peak can fit almost any bump; demand the rise/fall sampling criterion.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/ztf-microlensing-event-uncatalogued.md
```

Already set up? Say `run V3R1T4S on ztf-microlensing-event-uncatalogued`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ztf-microlensing-event-uncatalogued`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
