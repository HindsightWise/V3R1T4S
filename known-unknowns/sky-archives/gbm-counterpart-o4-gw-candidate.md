# Gamma-ray counterpart candidate in public Fermi-GBM data for an O4a/O4b gravitational-wave candidate, sub-threshold ones included

🔭 **Sky archives** · standard · tractability ★★☆☆☆ · compute: laptop-days (GBM CTIME and CSPEC daily files are tens of MB per day for about 600 days; continuous TTE is larger and needed only near candidates; each LVK candidate release with skymaps is about 1-1.5 GB) · open as of 2026-10-30

## The problem

GW170817 with GRB 170817A remains the only confirmed gravitational-wave/gamma-ray pair. The weak Fermi-GBM transient 0.4 s after GW150914 (Connaughton et al., arXiv:1602.03920, false-alarm probability 0.0022, 2.9 sigma) is contested. The LVK candidate data releases list every O4 trigger with FAR < 2/day, with times, p_astro and BAYESTAR skymaps: 1,456 for O4a (GWTC-4.1, Zenodo 20276095) and 1,886 for O4b (GWTC-5.0, Zenodo 20348004). Fermi-GBM daily CTIME, CSPEC, continuous TTE and position-history files are public at HEASARC (the O4b day 2024-12-29 was checked). For O1-O3, the GBM team ran its targeted and untargeted sub-threshold searches on the catalog events, including the GWTC-1 low-significance candidates, and found no confident counterpart other than GRB 170817A (Hamburg et al. 2020, arXiv:2001.00923; Fletcher et al. 2024, arXiv:2308.13666, jointly with Swift-BAT). Pillas, Dal Canton and collaborators (arXiv:2306.04373) cross-matched every O2 PyCBC trigger with a reanalysis of all public GBM data from that run. Perera, Zackay and Venumadhav (arXiv:2507.05739) built a time-slide sGRB search of archival GBM data that finds about 50% more short bursts than the on-board trigger, but it does not cross-match O4 GW candidates. Other published work: single-event studies such as GW230529 (Ronchini et al., arXiv:2405.10752, no detection by Swift-BAT or Fermi-GBM), a 4-OGC cross-match with GBM/BAT long GRBs (Wang, Nitz et al., arXiv:2208.03279, consistent with a null result), and a match of 13 O4-era sub-threshold short GRBs against the significant O4 public alerts (Cai et al., arXiv:2509.02995, no coincidence). As of 2026-10-28, no paper reports a systematic search of the O4 (GWTC-4.1 and GWTC-5.0) sub-threshold candidate lists against untriggered GBM data. Open task: a gamma-ray transient in public GBM data, coincident in time and sky with an O4 gravitational-wave candidate, whose association survives the full trials factor.

## What counts as a win

A saved pair, consisting of a GW candidate from the GWTC-4.1 or GWTC-5.0 candidate release (gw_name, GPS time) and a gamma-ray transient found in public Fermi-GBM data (HEASARC daily CTIME or continuous TTE files), with the search code and a pre-registered list of every GW candidate searched, such that: (1) the transient begins within [-1 s, +5 s] of the GW merger time; (2) its single-candidate false-alarm probability p, from the claimant's targeted-search statistic evaluated identically on off-source windows of the same GBM data within 3 days of the event (excluding SAA passages and known triggers; overlapping windows and inter-detector time slides are allowed), is <= 1e-4, and the off-source set holds at least 100,000 windows and at least 10/p windows, so that p is counted rather than extrapolated; (3) the GW candidate's 90% credible region from the release skymap is not entirely Earth-occulted for Fermi at that time and overlaps the transient's 90% GBM localisation, including systematic error; (4) the false-association probability, p multiplied by the number of GW candidates searched and by every timescale, spectral template and window tried, is <= 1e-3 (so the off-source set of (2) must be large enough to count a p that small); and (5) the transient is not a catalogued GBM trigger of another origin (terrestrial gamma-ray flash, magnetar burst, solar flare, particle event), and the pair is absent from GCN Circulars (https://gcn.nasa.gov/circulars) and from published GW-GRB papers, all re-fetched live immediately before claiming.

## Partial wins

- **p1:** A pair meeting every criterion except (4), with post-trials false-association probability between 1e-3 and 1e-2.
- **p2:** Method validation: run blind on public data, the same pipeline recovers GRB 170817A for GW170817 with single-candidate false-alarm probability <= 1e-4, and the GW150914 GBM transient with a false-alarm probability within a factor 3 of the published 0.0022.

## How a win is checked

Skeptic downloads the GBM CTIME/TTE and position-history files for the day, reruns the saved targeted search on the on-source window and on 10,000 freshly drawn off-source windows, recomputes the Earth occultation and the overlap with the release skymap, recounts the trials from the pre-registration, and searches the GBM trigger catalog and the GCN archive. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:GBM+AND+abs:gravitational&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://zenodo.org/records/20348004>
- <https://zenodo.org/records/20276095>
- <https://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/daily/>
- <https://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigbrst.html>
- <https://gcn.nasa.gov/circulars>
- <https://arxiv.org/abs/1602.03920>
- <https://arxiv.org/abs/2001.00923>
- <https://arxiv.org/abs/2308.13666>
- <https://arxiv.org/abs/2306.04373>
- <https://arxiv.org/abs/2405.10752>
- <https://arxiv.org/abs/2208.03279>
- <https://arxiv.org/abs/2509.02995>
- <https://arxiv.org/abs/2507.05739>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: a GBM targeted-search approach (a coherent Poisson likelihood across the detectors with spectral templates) run on CTIME data around every candidate.
- Joint-mission detection (Perera, Zackay and Venumadhav, arXiv:2609.25672): combine GBM with Swift-BAT rates to reach fainter short bursts.
- Rank GW candidates by p_BNS + p_NSBH and distance before searching, and pre-register the ranking so the trials factor stays honest.
- Cross-domain import (neutrino astronomy): unbinned stacking likelihoods over many weak candidates, for a population-level signal.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Most of the 3,342 candidates are noise; the trials factor over candidates, windows and templates dominates.
- Terrestrial gamma-ray flashes, magnetospheric particle events and solar activity make short GBM excesses; check the GBM trigger catalog and the spacecraft's geomagnetic position.
- Earth occultation and SAA passages remove large parts of the sky and of the time; a counterpart must be geometrically possible.
- Do not post GCN Circulars or contact the GBM or LVK teams; the result is a candidate in a run report only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/gbm-counterpart-o4-gw-candidate.md
```

Already set up? Say `run V3R1T4S on gbm-counterpart-o4-gw-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gbm-counterpart-o4-gw-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
