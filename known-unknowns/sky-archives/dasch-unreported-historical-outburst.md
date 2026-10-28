# Unreported historical outburst (nova, dwarf nova or large-amplitude event) in DASCH DR7 century-long plate light curves

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (API queries per field; cutouts are MB each) · open as of 2026-10-28

## The problem

DASCH Data Release 7 (Grindlay, Williams and team; released 2024 December 29) provides ~23.6 billion photometric measurements of 252 million sources from Harvard plates, ~1880-1990, via the daschlab client and public web APIs. Only a handful of DR7-era discoveries are published (e.g. a candidate 1951 superoutburst of GOTO065054+593624, arXiv:2501.11524). Open task: find a source with a significant historical outburst (>= 2 mag, on multiple plates) that is not recorded in VSX, the AAVSO International Database summary, the CBAT/Duerbeck nova lists or the literature.

## What counts as a win

A saved bundle (DASCH DR7 light curve table as returned, plate identifiers, cutouts of every outburst plate and the nearest pre/post non-detection plates, analysis code) showing an outburst of amplitude >= 2.0 mag above the quiescent median seen on >= 3 distinct plates from >= 2 different plate series (telescopes) within the event, with every outburst point passing DR7 quality flags, visual inspection of cutouts showing a stellar PSF (not a plate defect, emulsion flaw or neighbour blend), and no listing of an outburst at that epoch for that position in VSX, the Duerbeck/CBAT nova lists, or ADS full-text (status pages re-fetched live immediately before claiming).

## Partial wins

- **p1:** A new dwarf nova recurrence time measured from >= 5 DASCH outbursts for a known CV with no published recurrence time.
- **p2:** A previously unreported historical outburst of a known CV/symbiotic (object known, epoch new), on >= 3 plates from >= 2 series.
- **p3:** A published reproducible false-positive census: the fraction of DR7 'outbursts' that are plate defects, with a classifier that keeps >= 90% of known historical novae in DR7.

## How a win is checked

Skeptic re-queries the light curve and plate cutouts via daschlab, checks the flags and cutouts by eye, and searches VSX/ADS by coordinates. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://dasch.cfa.harvard.edu/dr7/>

## Sources

- <https://dasch.cfa.harvard.edu/dr7/>
- <https://dasch.cfa.harvard.edu/dr7/web-apis/>
- <https://daschlab.readthedocs.io>
- <https://arxiv.org/abs/2501.12977>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: target positions of known quiescent CVs (from the Ritter-Kolb catalogue and Gaia CV candidates) and scan their DASCH light curves for > 2 mag brightenings on multiple series.
- Blind search near the Galactic plane for single-epoch multi-plate brightenings at positions with faint Gaia counterparts (G 17-20), the regime of unrecorded classical novae.
- Cross-domain import (archival manuscript studies): codicology-style provenance checks - use plate jackets and logbook photos to rule out double exposures and plate annotations.
- Cross-domain import (fraud detection): isolation forests over per-plate residuals flag points that are anomalous relative to the plate's own calibration, separating defects from real variability.
- Cross-domain import (epidemiology): outbreak-detection CUSUM charts over the light curve give principled thresholds for 'outburst' with a controlled false-alarm rate.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Plate defects, dust and emulsion flaws masquerade as single-plate brightenings; require multiple plates from different telescopes.
- Source splitting and ATLAS-refcat2 calibration artefacts (DASCH documents 'false ATLAS trends') fake long-term changes; use the APASS-referenced light curves and read the DR7 known-issues pages.
- Blends with bright neighbours on low-resolution patrol plates; inspect cutouts.
- Known novae and CV outbursts are catalogued under historical names; search VSX and the literature by coordinates.
- The DR7 lightcurve endpoint is a read-only POST JSON query used by the official client; no account is needed, but if it ever requires registration, the target is off limits.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/dasch-unreported-historical-outburst.md
```

Already set up? Say `run V3R1T4S on dasch-unreported-historical-outburst`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dasch-unreported-historical-outburst`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
