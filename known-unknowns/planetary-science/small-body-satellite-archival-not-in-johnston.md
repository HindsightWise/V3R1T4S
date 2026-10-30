# New satellite of a TNO, Centaur, Jupiter Trojan or asteroid resolved in public archival HST, JWST or adaptive-optics images, absent from Johnston's Archive

🪐 **Planets and moons** · standard · tractability ★★☆☆☆ · compute: laptop-hours (HST WFC3/ACS cutouts are MB each; PSF fitting of a few thousand visits overnight) · open as of 2026-10-30

## The problem

W. R. Johnston's Asteroids with Satellites database (last updated 24 October 2026) lists 654 small bodies with companions: 113 NEAs, 36 Mars-crossers, 340 main-belt asteroids, 8 Jupiter Trojans and 157 TNOs; 122 of the TNO systems were found by space-based imaging, mostly HST. Archival discoveries continue: e.g. the satellite of (501214) 2013 TC146, found by B. Proudfoot and W. Grundy in HST images taken on 2017 Dec 13, was announced on 2026 Sep 23 (per its Johnston page), and Johnston's date-ordered list shows new systems reported every few days through September and October 2026. HST snapshot programmes have imaged hundreds of TNOs and Centaurs (Noll, Grundy, Benecchi, Parker and others), and MAST, the JWST archive and the Keck Observatory Archive make them public. Close, faint companions near the PSF core are the ones most often missed. Open task: a companion of a small body, resolved in public images, that Johnston's database does not list.

## What counts as a win

A saved bundle (MAST/KOA dataset IDs, cutouts, PSF models, fitting code, astrometry and photometry) where: (1) in >= 2 separate visits (or >= 2 HST orbits >= 3 hours apart) a two-source PSF model beats a single-source model by delta chi^2 >= 25 in each visit, with empirical or TinyTim-type PSFs validated on stars in the same images; (2) the secondary moves with the primary: between visits its offset from the primary changes by less than 10% of the primary's own sky motion over the same interval, and at each epoch no Gaia DR3 source and no source in a stack of other-epoch images lies at the secondary's sky position; (3) the flux ratio agrees between visits within 0.5 mag and the separation is < 0.3 Hill radii of the primary at its distance; (4) the primary has no companion in https://www.johnstonsarchive.net/astro/asteroidmoons.html or its date-ordered list (re-fetched immediately before claiming), and no CBET, paper or preprint reports one.

## Partial wins

- **p1:** The pipeline recovers >= 90% of the Johnston-listed binaries whose separation in the processed archival images is > 2 pixels, and on >= 50 isolated stars in the same images returns no detection meeting (1), all results saved.
- **p2:** A companion meeting (1), (3) and (4) in a single visit, with a background-source check as in (2) at that epoch.
- **p3:** A first mutual orbit for a listed binary that Johnston's database gives without orbit elements and for which no paper, preprint or CBET found by a fresh search gives an orbit, fitted to >= 5 epochs of relative astrometry with reduced chi^2 <= 2 (the mirror ambiguity stated, not necessarily resolved).

## How a win is checked

Skeptic downloads the datasets from MAST/KOA, refits single- and two-source PSF models with an independent PSF, recomputes delta chi^2, checks Gaia DR3 and other-epoch images at the secondary's position, and re-reads Johnston's lists. About an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.johnstonsarchive.net/astro/asteroidmoons.html>

## Sources

- <https://www.johnstonsarchive.net/astro/asteroidmoons.html>
- <https://www.johnstonsarchive.net/astro/asteroidmoonslist2.html>
- <https://www.johnstonsarchive.net/astro/astmoons/am-501214.html>
- <https://mast.stsci.edu/>
- <https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/ssois/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: forward-model each visit with two PSFs on a grid of separations and flux ratios, as in the HST binary surveys of Noll and Grundy.
- Search the shortest separations first: drizzled products blur close pairs, so fit the individual flt/flc frames.
- Cross-domain import (exoplanet direct imaging): reference-differential imaging with the other TNOs of the same programme as PSF references.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Cosmic rays and hot pixels in single frames make false companions; require consistency across all frames of a visit.
- Elongated primaries (contact binaries) can be fitted by two close PSFs; demand a separation > 1.5 pixels or a resolved gap.
- Several discovery teams are mining the same HST archive now; Johnston's date-ordered list shows new systems every week.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/small-body-satellite-archival-not-in-johnston.md
```

Already set up? Say `run V3R1T4S on small-body-satellite-archival-not-in-johnston`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `small-body-satellite-archival-not-in-johnston`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
