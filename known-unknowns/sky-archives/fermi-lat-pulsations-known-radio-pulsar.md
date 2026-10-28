# Gamma-ray pulsations from a known radio pulsar not yet on the public list of LAT-detected pulsars

🔭 **Sky archives** · standard · tractability ★★☆☆☆ · compute: laptop-hours (LAT weekly photon files total ~100 GB for the mission; an ROI selection is far smaller) · open as of 2026-10-28

## The problem

The public list of LAT-detected gamma-ray pulsars (created by Paul Ray, maintained with David A. Smith; content 'Updated 3 July 2025', page last edited 2025 July 16) holds 323 pulsars (83 young radio/X-ray selected, 71 young gamma selected, 159 radio-selected MSPs, 10 gamma-selected MSPs); the Third Fermi-LAT Pulsar Catalog (3PC, Smith et al. 2023) describes most of them. Hundreds of new radio pulsars (e.g. FAST GPPS and CRAFTS, MeerKAT TRAPUM, many in 4FGL unassociated sources) have published timing solutions. Open task: detect significant gamma-ray pulsations by folding public Fermi-LAT photons with a published radio ephemeris for a pulsar absent from the public LAT list and from later papers and ATels.

## What counts as a win

A saved bundle (published ephemeris .par file with citation; LAT photon selection: event class, ROI, energy range, time range; the weighted photon list; the folding code) in which: (1) the weighted H-test (de Jager; photon weights as in Kerr 2011) on photons folded with the ephemeris inside its validity span gives single-trial H > 36 (chance probability about exp(-0.4H) ~ 6e-7, about 5 sigma before trials); (2) after multiplying by the number of selection choices (ephemerides, energy cuts, ROIs, weightings) declared in advance, the post-trials significance is still >= 4 sigma; (3) the pulse profile is stable across the two halves of the data; (4) folding at slightly wrong spin parameters destroys the signal; and (5) the pulsar is absent from https://confluence.slac.stanford.edu/spaces/GLAMCOG/pages/108698084/Public+List+of+LAT-Detected+Gamma-Ray+Pulsars and from ADS/ATel (re-fetched live immediately before claiming).

## Partial wins

- **p1:** A 3-4 sigma pulsation candidate (H between 20 and 36) with consistent profiles in both data halves.
- **p2:** A reproducible pipeline that recovers pulsations for >= 20 listed LAT pulsars from their public ephemerides with the stated H thresholds.
- **p3:** A significant (> 5 sigma) gamma-ray point source, from a likelihood analysis, at the position of a new radio pulsar that is absent from 4FGL-DR4 and from the LAT FL16Y 16-year source list.

## How a win is checked

Skeptic downloads the LAT weekly photon and spacecraft files for the span, reruns the weighting (photon probabilities from a 4FGL model or simple PSF weights) and folding with PINT, and recomputes the H-test. One to a few hours on a laptop.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://confluence.slac.stanford.edu/spaces/GLAMCOG/pages/108698084/Public+List+of+LAT-Detected+Gamma-Ray+Pulsars>

## Sources

- <https://confluence.slac.stanford.edu/spaces/GLAMCOG/pages/108698084/Public+List+of+LAT-Detected+Gamma-Ray+Pulsars>
- <https://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/photon/>
- <https://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/spacecraft/>
- <https://www.atnf.csiro.au/research/pulsar/psrcat/>
- <https://fermi.gsfc.nasa.gov/ssc/data/access/lat/3rd_PSR_catalog/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: rank pulsars with published phase-connected timing (FAST, MeerKAT, Parkes papers) by spin-down flux Edot/d^2 and fold LAT photons only within each ephemeris's validity span.
- Prioritise pulsars inside 4FGL-DR4 unassociated source error ellipses (the population where radio surveys targeted gamma-ray sources).
- Cross-domain import (communications engineering): weighted H-test is a matched filter; use optimal photon weights computed from a source model (Kerr 2011 weighting), the analogue of SNR-weighted combining.
- Cross-domain import (gravitational-wave searches): semi-coherent stacking across short segments allows modest ephemeris error, recovering signal where the ephemeris drifts outside its fit span.
- Cross-domain import (pharmacology dose-response): pre-register the energy and ROI cuts to avoid trying many selections until something crosses threshold.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- ATNF catalogue ephemerides are often from short spans years before the LAT era; folding outside the validity span smears pulsations.
- Trying many energy cuts, ROIs and weightings inflates significance; count trials.
- Nearby bright gamma-ray pulsars or blazars leak into the ROI; check that the pulse profile is not from a neighbour (fold the neighbour with its own ephemeris).
- The public list may lag recent ATels/papers; search ADS and ATel before claiming novelty.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/fermi-lat-pulsations-known-radio-pulsar.md
```

Already set up? Say `run V3R1T4S on fermi-lat-pulsations-known-radio-pulsar`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fermi-lat-pulsations-known-radio-pulsar`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
