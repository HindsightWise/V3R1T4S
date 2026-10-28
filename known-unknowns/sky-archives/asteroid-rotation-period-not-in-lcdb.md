# Reliable rotation periods for asteroids with no entry in the Asteroid Lightcurve Database, from public survey photometry

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (per-object photometry is KB-MB; batch of thousands overnight) · open as of 2026-10-28

## The problem

The Asteroid Lightcurve Database (LCDB; Warner, Harris and Pravec) lists rotation periods with reliability codes. Its latest public release is dated 2023 October 1 (still the current release on the LCDB page, re-checked 2026-10-28). Survey photometry has been mined heavily since then: ATLAS bootstrap convex inversion (Durech, Vavra, Vanco and Erasmus 2022, Front. Astron. Space Sci. 9, 809771), Gaia DR3 spin states (Durech & Hanus 2023, J/A+A/675/A24), and Gaia DR3 light-scattering inversions for over 8,000 asteroids (MacLennan et al. 2026, J/A+A/707/A131). Durech & Hanus 2026 (A&A 714, doi:10.1051/0004-6361/202662316, arXiv:2610.06082; previewed as EPSC2026-425) combined Catalina, Mt. Lemmon, Pan-STARRS, ZTF, USNO, ATLAS, ASAS-SN, TESS and Gaia photometry with Asteroids@home into about 30,000 models, including about 22,000 unique spin-state solutions. Smaller 2026 period sets include KMTNet bulge-field periods for 96 asteroids, 84 of them new (Huang et al., arXiv:2606.26184), periods from MPC-circular photometry (Nagainis & Eglitis, arXiv:2610.13223) and early Rubin Observatory science-validation periods (Carruba et al., arXiv:2609.29841). Dense public data still exist for many objects with no published period. Open task: derive an unambiguous rotation period (LCDB quality U >= 3-equivalent) for asteroids with no LCDB entry and no published period.

## What counts as a win

For each claimed object, a saved bundle (designation, raw photometry with times, filter, observer-centric geometry from JPL Horizons, phase-angle-corrected reduced magnitudes, period-search code) in which all of the following hold. (1) The best period has a Lomb-Scargle / Fourier-series FAP < 1e-4. (2) The folded curve at P shows two maxima and two minima of amplitude > 0.1 mag. (3) The P/2 and 2P aliases are tested and rejected by chi^2 (delta chi^2 > 25). (4) The period is recovered independently, within 1%, in two separate apparitions or two separate surveys. (5) The object has no period in any of these: the LCDB release linked at https://www.minorplanet.info/php/lcdb.php (re-fetched live immediately before claiming); DAMIT; J/A+A/707/A131; J/A+A/675/A24; the ATLAS inversion catalogue of Durech et al. 2022; Durech & Hanus 2026 (arXiv:2610.06082, A&A 714) or any released model or period table from that work; arXiv:2606.26184; arXiv:2610.13223; arXiv:2609.29841; and ADS (search by number/designation).

## Partial wins

- **p1:** Ten or more new periods meeting all criteria (one is the main win; a batch shows a reusable pipeline).
- **p2:** A new very slow rotator (P > 500 h) or a new candidate binary asteroid (two-period solution, eclipse/occultation-like events) meeting all checks.
- **p3:** A demonstrable correction of an LCDB U=2 period, with the new period confirmed in two independent data sets and the LCDB value excluded at delta chi^2 > 25.

## How a win is checked

Skeptic re-queries the photometry (IRSA ZTF, TESS FFI cutouts or Gaia DR3 SSO tables), recomputes geometry from Horizons, reruns an independent periodogram, and checks the LCDB file and DAMIT. Minutes per object.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.minorplanet.info/php/lcdb.php>

## Sources

- <https://www.minorplanet.info/php/lcdb.php>
- <https://irsa.ipac.caltech.edu/Missions/ztf.html>
- <https://gea.esac.esa.int/archive/>
- <https://ssd-api.jpl.nasa.gov/sbdb.api?sstr=2412>
- <https://dc.g-vo.org/I/ivo://CDS.VizieR/J/A+A/707/A131>
- <https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-425.html>
- <https://arxiv.org/abs/2610.06082>
- <https://dc.g-vo.org/rr/q/lp/custom/CDS.VizieR/J/A+A/675/A24>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: multi-band Fourier-series fits with an H-G12 phase function on ZTF g/r forced photometry, prioritising objects with > 200 detections in one apparition.
- TESS full-frame images contain thousands of asteroids with dense 10-min or 200-s cadence; extract them with moving-aperture photometry (as in the TSSYS work of Pal et al.).
- Cross-domain import (radar/sonar): treat sparse multi-survey data with a joint likelihood over a period grid (like a matched filter across sensors) rather than separate periodograms.
- Cross-domain import (circadian biology): chronobiology's methods for noisy, unevenly sampled rhythms (JTK_CYCLE, cosinor) are robust to sparse sampling and give honest p-values.
- Cross-domain import (compressed sensing): recover periods from very sparse Gaia DR3 photometry by sparse-frequency recovery with a dictionary of physical lightcurve shapes.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Half/double-period ambiguity: a monomodal fold at P/2 is the classic false period; require bimodal shape and alias rejection.
- Sidereal/synodic and 1-day aliases from nightly sampling; check the window function.
- Phase-angle and aspect changes alter amplitude between apparitions; do not combine raw magnitudes without geometry correction.
- LCDB public release is from 2023; newer published periods exist - search ADS/DAMIT/Gaia inversion catalogue, not just LCDB.
- Blends with background stars in ZTF produce spikes; reject points near catalogued stars.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/asteroid-rotation-period-not-in-lcdb.md
```

Already set up? Say `run V3R1T4S on asteroid-rotation-period-not-in-lcdb`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `asteroid-rotation-period-not-in-lcdb`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
