# New white dwarf with transiting planetary debris in public ZTF or TESS light curves

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (ZTF light curves for ~100k WDs is a few GB via the IRSA light-curve service; TESS for the brightest few thousand) · open as of 2026-10-28

## The problem

White dwarfs with transits by disintegrating planetary debris are rare: WD 1145+017 (Vanderburg et al. 2015); ZTF J0139+5245 and ZTF J0328-1219 (Vanderbosch et al. 2020/2021); the Guidry et al. 2021 systems; WD 1054-226 (Farihi et al. 2022; Korth et al. 2026, arXiv:2603.07677); SBSS 1232+563 (Hermes et al. 2025); the six Bhattacharjee et al. 2025 ZTF candidates (arXiv:2502.05502; ZTF J1944+4557 confirmed by Guidry et al. 2025, arXiv:2508.18348); and six previously non-variable white dwarfs with deep, long-lived single obscuration events found in ZTF negative alerts by van Roestel et al. 2026 (arXiv:2609.08923), which bring the confirmed count to 20. Bhattacharjee et al. searched only within 500 pc and only the top 1% most variable objects. Open task: identify a new white dwarf (Gentile Fusillo Gaia catalog) whose public ZTF and/or TESS photometry shows irregular or periodic dimming events with the depth/shape signature of debris transits, not in any published list.

## What counts as a win

A saved bundle (Gaia DR3 source_id, white-dwarf probability > 0.75 from the Gentile Fusillo catalog, raw ZTF/TESS light curves as downloaded, analysis code) showing either (a) a periodic dimming signal (FAP < 1e-3 after trials over the searched sample) with depth > 3% in >= 2 independent data sets or seasons, or (b) >= 3 aperiodic dips each > 10% deep and > 5 sigma below the local median in a single filter, confirmed in a second filter or second survey within the same epoch; plus checks excluding blending (no Gaia neighbour within 10 arcsec brighter than G+3), eclipsing-binary/companion explanations (no secondary eclipse, no ellipsoidal variation, no IR excess implying M dwarf) and instrumental flags; and the source is absent from the tables of arXiv:2502.05502 and arXiv:2609.08923, from https://en.wikipedia.org/wiki/List_of_exoplanets_and_planetary_debris_around_white_dwarfs, and from arXiv/ADS search on its Gaia/ZTF/WD name and coordinates (status query https://export.arxiv.org/api/query?search_query=abs:%22white+dwarf%22+AND+abs:debris+AND+abs:transit&sortBy=submittedDate&sortOrder=descending&max_results=50 re-run immediately before claiming).

## Partial wins

- **p1:** Extend the Bhattacharjee et al. variability-metric search beyond 500 pc (or to the 1-5% variability tail) and publish a ranked, reproducible list where every published system that falls in scope is recovered in the top N.
- **p2:** Measure a previously unreported period (FAP < 1e-3) for one of the published transit candidates that lacks a period.
- **p3:** A new candidate with a single deep (>20%) dip event confirmed in two filters, without the multiplicity required for the full criterion.

## How a win is checked

Skeptic re-downloads the ZTF light curves (IRSA) and TESS FFI/2-min data (MAST) for the source_id, re-runs the periodogram or dip detector, checks Gaia neighbours and flags, and searches ADS/arXiv for the name. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:%22white+dwarf%22+AND+abs:debris+AND+abs:transit&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Sources

- <https://en.wikipedia.org/wiki/List_of_exoplanets_and_planetary_debris_around_white_dwarfs>
- <https://irsa.ipac.caltech.edu/Missions/ztf.html>
- <https://archive.stsci.edu/>
- <https://vizier.cds.unistra.fr/viz-bin/VizieR>
- <https://arxiv.org/abs/2502.05502>
- <https://arxiv.org/abs/2609.08923>
- <https://arxiv.org/abs/2508.18348>
- <https://export.arxiv.org/api/query?search_query=abs:%22white+dwarf%22+AND+abs:debris+AND+abs:transit&sortBy=submittedDate&sortOrder=descending&max_results=50>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: compute a multi-band variability metric (Gaia flux-error excess plus ZTF g/r scatter) and box/dip searches over the full Gentile Fusillo WD sample, prioritising metal-polluted (DZ/DAZ) and IR-excess objects.
- Search beyond the 500 pc cut and in the 1-5% variability tail that earlier work left out; use TESS 200-s FFIs for the few hundred brightest WDs.
- Cross-domain import (finance): change-point and drawdown statistics from trading-risk analysis detect irregular, asymmetric dips better than periodograms for aperiodic debris.
- Cross-domain import (fault detection in machinery): use spectral-kurtosis or matrix-profile motif discovery to find repeated dip shapes at unknown period.
- Cross-domain import (epidemiology): treat each object as a 'case' and use scan statistics over time windows (Kulldorff) with a per-object background to control false alarms across 100k light curves.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Faint WDs near the ZTF limit give spurious dips from bad photometry; require catflags==0 and check the same nights on neighbouring stars.
- Eclipsing WD+M-dwarf binaries and CVs mimic periodic dimming; check for secondary eclipses, emission lines (if a public spectrum exists) and IR excess.
- Blending in crowded fields or TESS's 21-arcsec pixels attributes a neighbour's variability to the WD.
- Many candidates appear in Guidry et al. 2021, Bhattacharjee et al. 2025 or van Roestel et al. 2026 lists under ZTF names; cross-match by coordinates, not by name.
- Do not report to any agency or team; the claim is a vetted candidate.
- The Wikipedia list lags the literature (on 2026-10-28 it listed 14 transiting systems and omitted the six van Roestel et al. 2026 objects); never use it as the only novelty check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/wd-debris-transit-new-candidate.md
```

Already set up? Say `run V3R1T4S on wd-debris-transit-new-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wd-debris-transit-new-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
