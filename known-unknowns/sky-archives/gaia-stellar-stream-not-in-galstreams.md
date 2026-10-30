# New stellar stream in Gaia DR3 absent from the galstreams library (v1.2.1) and the STREAMFINDER atlas

🔭 **Sky archives** · standard · tractability ★★☆☆☆ · compute: laptop-days (all-sky Gaia DR3 queries with G < 20 and parallax/proper-motion cuts are tens of GB; regional searches are laptop-hours) · open as of 2026-10-30

## The problem

The galstreams library of Milky Way stellar streams (Cecilia Mateu; Mateu 2023, MNRAS 520, 5225; github.com/cmateu/galstreams) holds > 200 tracks for 141 distinct streams in v1.2 (tagged 2026 June; latest release v1.2.1, 2026-06-03). Its last major track update (2024 June) added over 80 tracks, 40 of them for new streams. The largest Gaia DR3 stream atlas is STREAMFINDER (Ibata, Malhan, Martin and collaborators; Ibata et al. 2024, ApJ 967, 89, arXiv:2311.17202: 87 thin streams, 29 of them new). Further candidates come from Via Machinae (Shih, Buckley, Necib and collaborators) and from spectroscopic surveys (S5). Open task: find a thin, kinematically coherent stellar stream in Gaia DR3 that is in neither galstreams nor those atlases nor any later paper. Gaia DR4 is due 2026 December 2; a claim based on DR3 must say so and use DR3 values throughout.

## What counts as a win

A saved bundle (ADQL, member source_ids, track fit, code) for a structure with: (1) >= 30 Gaia DR3 members (G < 20, RUWE < 1.4) along a track >= 5 deg long whose width is <= 1/10 of its length; (2) a proper-motion track that varies smoothly along the stream, with residual dispersion consistent with <= 10 km/s at the fitted distance, and parallaxes consistent with that distance (reduced chi^2 < 2); (3) members on one old metal-poor isochrone ( > = 80% within 0.15 mag in colour); (4) significance: the combined sky+proper-motion+CMD matched-filter count exceeds the mean of >= 200 control filters by >= 5 sigma of their dispersion, the controls being the same filter rotated in proper motion and shifted on the sky away from known streams, with the control distribution saved; (5) no stream track overlaps it: no galstreams track whose pole lies within 10 deg of the new pole and whose sky track covers >= 30% of the new one, and no STREAMFINDER or Via Machinae stream likewise. A globular cluster or dwarf from the LVDB at its end must be stated. No arXiv paper reports it (sources re-fetched immediately before claiming).

## Partial wins

- **p1:** Inside a declared region containing >= 5 galstreams streams with published Gaia members, the pipeline recovers >= 80% of them, with the recovered tracks compared to the galstreams tracks.
- **p2:** A new structure meeting (1)-(3) and (5) at 4-5 sigma in test (4), logged as a candidate.
- **p3:** A known galstreams stream extended by >= 5 deg beyond its galstreams end-point, with >= 15 new members meeting (2)-(3) and >= 5 sigma in test (4) for the extension.

## How a win is checked

Skeptic re-runs the ADQL on the Gaia archive, recomputes the matched filter and the control distribution, and compares the pole and track with galstreams (pip install galstreams; MWStreams summary) and the STREAMFINDER table. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/cmateu/galstreams>

## Sources

- <https://github.com/cmateu/galstreams>
- <https://raw.githubusercontent.com/cmateu/galstreams/master/README.md>
- <https://ui.adsabs.harvard.edu/abs/2023MNRAS.520.5225M>
- <https://arxiv.org/abs/2311.17202>
- <https://gea.esac.esa.int/archive/>
- <https://www.cosmos.esa.int/web/gaia/release>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search in action/angle-like coordinates, or with great-circle pole counts (GC3/mGC3, Mateu), restricted to metal-poor CMD selections.
- Cross-domain import (image processing): Hough or Radon transforms on proper-motion-filtered density maps pick up thin linear features.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Gaia scanning-law stripes produce long thin artefacts in density maps; require proper-motion coherence and check against the scanning law.
- Disc substructure and open-cluster tidal tails are not halo streams; check the CMD age and the orbit.
- galstreams lists several tracks per stream from different papers; match against all of them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/gaia-stellar-stream-not-in-galstreams.md
```

Already set up? Say `run V3R1T4S on gaia-stellar-stream-not-in-galstreams`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gaia-stellar-stream-not-in-galstreams`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
