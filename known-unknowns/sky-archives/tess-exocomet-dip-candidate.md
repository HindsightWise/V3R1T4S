# New exocomet-transit candidate (asymmetric single dip) in public TESS light curves

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (bright-star QLP/SPOC light curves for selected sectors are a few GB) · open as of 2026-10-28

## The problem

Transiting exocomets produce shallow, asymmetric dips (sharp ingress, slow egress), first seen in Kepler (Rappaport et al. 2018) and in TESS around beta Pic (Zieba et al. 2019). Norazman et al. (arXiv:2508.04673, MNRAS) searched a magnitude-limited sample in TESS Sectors 1-26. They recovered beta Pic and found 5 new candidates: TIC 280832588, 73149665 and 143152957 on the main sequence, TIC 229790952 (a giant) and TIC 110969638 (a probable supergiant). Gibson et al. (arXiv:2510.09920) found 24 exocomet transits of RZ Psc in a targeted TESS survey of extreme debris disks. Dobrycheva et al. (arXiv:2402.19075, 2602.02701) flagged 32 Sector-1 candidates with a random-forest search. No published magnitude-limited systematic search covers Sectors 27 onward. Open task: a new, vetted exocomet-like dip on a star absent from those lists.

## What counts as a win

A saved bundle (TIC ID, TESS SPOC/QLP light curves and target-pixel cutouts as downloaded, code) with a single dip of depth > 300 ppm, asymmetric by a one-sided exponential-tail model preferred over a symmetric model by delta BIC > 10, duration within the range computed for a body on a bound or parabolic orbit around the host (using the TIC mass and radius; computation included), on-target by difference-image centroids (offset < 1 pixel/3 sigma), not coincident with momentum dumps, scattered light or other stars' simultaneous dips in the same camera/CCD, and absent from arXiv:2508.04673, 2510.09920, 2402.19075, 2602.02701 and from ADS/arXiv by TIC/coordinate search (status query https://export.arxiv.org/api/query?search_query=abs:exocomet+AND+abs:TESS&sortBy=submittedDate&sortOrder=descending&max_results=50 re-run immediately before claiming).

## Partial wins

- **p1:** Recovery of every published TESS exocomet event in the searched sectors with the same pipeline, plus a quantified false-alarm rate from injection tests.
- **p2:** A second dip on one of the published candidates (Norazman 2025 list) in later sectors, meeting the asymmetry and centroid tests.
- **p3:** An occurrence-rate estimate for sectors 27+ with injection-recovery completeness, reproducible from saved code.

## How a win is checked

Skeptic re-downloads light curves and TPFs from MAST, refits asymmetric vs symmetric models, reruns centroid tests and checks the spacecraft quality flags and neighbour light curves. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:exocomet+AND+abs:TESS&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Sources

- <https://arxiv.org/abs/2508.04673>
- <https://archive.stsci.edu/>
- <https://arxiv.org/abs/2510.09920>
- <https://arxiv.org/abs/2602.02701>
- <https://arxiv.org/abs/2402.19075>
- <https://export.arxiv.org/api/query?search_query=abs:exocomet+AND+abs:TESS&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: matched filter with the Lecavelier des Etangs/Brogi exocomet profile on A/F stars brighter than T=9 in sectors 27+.
- Focus on young debris-disk stars (WISE IR excess) that earlier searches dropped for stellar activity, using GP detrending of pulsations.
- Cross-domain import (gravitational-wave glitch classification): use a Gravity-Spy-style classifier trained on known systematics (momentum dumps, scattered light) to veto dips.
- Cross-domain import (hydrology): asymmetric rise/recession of a storm hydrograph is the same shape; use recession-curve analysis to fit egress tails.
- Cross-domain import (structural health monitoring): use multi-star simultaneous events on the same CCD as a 'common-mode' signal and subtract it before searching.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Momentum dumps, scattered light and thermal events produce asymmetric dips; check quality flags and neighbours on the same CCD.
- Delta Scuti/gamma Dor pulsations in A/F stars beat to make dip-like features; detrend carefully and test injection recovery.
- Contaminating eclipsing binaries in the aperture; difference-image centroids are mandatory.
- No central catalogue exists; novelty depends on a literature search by TIC and coordinates.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/tess-exocomet-dip-candidate.md
```

Already set up? Say `run V3R1T4S on tess-exocomet-dip-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tess-exocomet-dip-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
