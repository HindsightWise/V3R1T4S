# New pulsar candidate in public Parkes (Murriyang) search-mode archival data, detected in two independent observations and absent from all pulsar lists

🔭 **Sky archives** · standard · tractability ★★☆☆☆ · compute: laptop-days (one semester collection of a Parkes search project is a few GB to TB on the CSIRO Data Access Portal; dedispersion and folding of a few hundred beams takes days on a laptop CPU) · open as of 2026-10-30

## The problem

Search-mode data from Parkes pulsar search projects are public under CC BY 4.0 on the CSIRO Data Access Portal (DAP; a keyword query for 'pulsar survey parkes' returns 1,371 collections). One example is project P477, a deep Perseus-arm search led by A. Lyne: 2.7 GB in 13 files for semester 2009OCTS_01, published on the DAP 2026-10-22. Reprocessings of archival Parkes surveys with new methods have repeatedly found pulsars that the original searches missed. Known pulsars and survey discoveries are listed by the ATNF Pulsar Catalogue (Manchester et al. 2005; version 2.9.0) and by the Pulsar Survey Scraper (David Kaplan, after Julia Deneva; updated 2026-09), which covers ATNF, GBNCC, PALFA, CRAFTS, FAST-GPPS, TRAPUM, MWA, CHIME, CHAMPSS and others. Open task: reprocess public Parkes archival data to find a dispersed periodic signal that is confirmed in an independent archival observation and is not a known pulsar. The win is the candidate; timing confirmation needs new telescope time and is not part of the win.

## What counts as a win

A saved bundle (DAP collection DOIs and file names, processing code and parameters, candidate plots and folded archives) where: (1) folding gives S/N >= 10 at DM >= 3 pc/cm^3, the S/N-versus-DM curve peaks at the stated DM, and the DM = 0 fold has <= 50% of the peak S/N; (2) the signal is present in both halves of the band and in >= 2 independent public observations (different dates) of positions within one beam FWHM, with consistent barycentric periods (fractional difference < 1e-4, or a fitted binary/acceleration model stated) and DMs within 10%; (3) within a pointing the signal is confined to one beam or to a group of mutually adjacent beams, and is absent from every beam not adjacent to that group (RFI appears across the receiver, a sky source does not), and its period is not within 0.1% of n/m (n, m <= 16) times the period of any known pulsar within 2 deg or of a documented Parkes RFI periodicity; (4) there is no pulsar with matching period and DM within 0.5 deg in ATNF psrcat (latest version) or any Pulsar Survey Scraper survey, and no arXiv/ATel report (re-fetched immediately before claiming).

## Partial wins

- **p1:** A reproducible pipeline run on >= 200 public beams that re-detects >= 90% of the known pulsars in those beams whose predicted S/N exceeds 15, with the recovery table saved.
- **p2:** A candidate meeting (1), (3) and (4) in one observation only, with S/N >= 12.
- **p3:** A rotating-radio-transient candidate: >= 3 single pulses at a consistent DM >= 3 in >= 2 independent observations of the same position, meeting (3) and (4) for single-pulse sources (RRATalog included).

## How a win is checked

Skeptic downloads the same DAP files, refolds at the stated period, period derivative and DM with an independent tool (PRESTO prepfold or dspsr/pdmp), and queries psrcat and the Pulsar Survey Scraper. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pulsar.cgca-hub.org/>

## Sources

- <https://data.csiro.au/collection/csiro:78706>
- <https://data.csiro.au/dap/ws/v2/collections?q=pulsar%20survey%20parkes&rpp=5>
- <https://www.atnf.csiro.au/research/pulsar/psrcat/>
- <https://pulsar.cgca-hub.org/>
- <https://github.com/dlakaplan/pulsarsurveyscraper>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fast folding algorithm (FFA) searches for long-period (P > 2 s) pulsars, the class FFT searches miss.
- Acceleration or jerk searches for binary millisecond pulsars in the low-latitude beams.
- Cross-domain import (radar signal processing): matched-filter banks over (P, DM, acceleration) with an empirical background from time-scrambled data.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Mains harmonics and other RFI periods appear in all 13 beams; require absence in the beams not adjacent to the detection.
- Bright known pulsars leak into neighbouring beams and appear at harmonics; a detection in one adjacent beam is normal for a real source, a detection in distant beams is not. Check n/m ratios.
- Survey discovery lists lag behind discoveries; check the Pulsar Survey Scraper and the newest papers.
- Some DAP collections may be embargoed or need sign-in; use only files the portal serves publicly (csiro:78706 serves its 13 beam files to anonymous range requests).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/parkes-archival-new-pulsar-candidate.md
```

Already set up? Say `run V3R1T4S on parkes-archival-new-pulsar-candidate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `parkes-archival-new-pulsar-candidate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
