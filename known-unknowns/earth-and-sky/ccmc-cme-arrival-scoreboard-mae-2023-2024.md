# NASA CCMC CME Scoreboard: CME arrival-time forecasts for 2023-2024 with a lower mean absolute error than every scoreboard method

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: laptop-hours (scoreboard JSON via REST in seconds; DONKI CME analyses, OMNI solar wind and LASCO/STEREO coronagraph summaries are small; drag-based or ML models run on CPU) · open as of 2026-10-30

## The problem

The NASA CCMC Earth CME Scoreboard (M. Leila Mays and the CCMC team; validation by Riley et al. 2018 and Kay et al. 2024, Space Weather) archives real-time CME shock-arrival predictions from about 30 methods (WSA-ENLIL+Cone run by NASA M2M, NOAA/SWPC, Met Office, BoM and KSWC, Cone+HAF, EAM, SARM, CMEFM, ELEvo, SIDC and others) together with the observed arrival, served by a public REST API. For CMEs with cmeID dated 2023-01-01..2024-12-31 the API returns 164 closed-out CMEs with an observed arrival. 153 of them (set S) have a pre-arrival WSA-ENLIL+Cone (NASA M2M) prediction (median lead 57.8 h). Taking each method's earliest pre-arrival prediction per CME, the mean absolute arrival-time errors on S (computed 2026-10-30) are: NOAA/SWPC ENLIL 9.93 h (44 CMEs), Ensemble ENLIL (M2M) 10.18 h (51), Cone+HAF 10.20 h (42), Met Office ENLIL 10.45 h (87), M2M ENLIL 10.74 h (153), BoM 11.57 h (39), CMEFM 11.59 h (70), EAM 11.93 h (57), SARM 12.07 h (70), SIDC 15.33 h (72). In 2025 the scoreboard's 'Median of all Methods' scored 9.63 h on 50 CMEs. Errors of about 10 h have hardly moved in a decade (Riley et al. 2018 reported a similar figure). Open task: an issue-time-honest method that beats every one of these on its own CMEs.

## What counts as a win

A saved file with one predicted shock-arrival time for every CME in S, plus code that regenerates it using only data timestamped before T_c, the submission time of that CME's earliest WSA-ENLIL + Cone (NASA M2M) prediction (DONKI CME analyses, coronagraph images or catalogs, OMNI/real-time solar wind, magnetograms), with any training or tuning on CMEs before 2023-01-01 only, such that the skeptic, recomputing from https://ccmc.gsfc.nasa.gov/CMESB-Earth/WS/get/predictions (queried per year, 2023 and 2024, re-fetched live immediately before claiming), finds (a) the method's MAE over S strictly below (direction: min) the M2M ENLIL MAE on S; (b) for every scoreboard method with at least 39 CMEs in S, the method's MAE on that method's CMEs strictly below that method's MAE on the same CMEs, using each method's earliest pre-arrival prediction; and (c) a 95% paired bootstrap (resampling CMEs, 10,000 draws) interval of the MAE difference against M2M ENLIL on S whose lower bound is above 0. The MAE must also be lower than any MAE reported for the same 2023-2024 scoreboard CMEs in a paper from the last 24 months.

## Partial wins

- **p1:** MAE over S strictly below the M2M ENLIL value (10.74 h as of 2026-10-30) under the same data-cutoff and training rules, without the bootstrap condition.
- **p2:** Beat the NOAA/SWPC ENLIL MAE (9.93 h) on its 44 CMEs in S under the same rules.
- **p3:** For the 2025 CMEs, an MAE strictly below the scoreboard's 'Median of all Methods' (9.63 h on its 50 CMEs), with T_c set to the median-of-methods entry's submission time and training on CMEs before 2025-01-01.

## How a win is checked

Skeptic downloads the 2023 and 2024 predictions JSON, recomputes per-method MAEs with a 30-line script (earliest pre-arrival prediction per method per CME), regenerates the claimed predictions from code through a harness that refuses any input timestamped at or after T_c, and runs the paired bootstrap. About 1 hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ccmc.gsfc.nasa.gov/CMESB-Earth/WS/get/predictions?CMEtimeStart=2024-01-01&CMEtimeEnd=2024-12-31>

## Sources

- <https://ccmc.gsfc.nasa.gov/scoreboards/cme/earth/>
- <https://ccmc.gsfc.nasa.gov/CMESB-Earth/WS/get/predictions?CMEtimeStart=2024-01-01&CMEtimeEnd=2024-12-31>
- <https://doi.org/10.1029/2018SW001962>
- <https://doi.org/10.1029/2024SW003951>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: drag-based model (DBM) ensembles driven by DONKI speed/width, with ambient wind speed from WSA or 27-day recurrence of OMNI speed.
- Conventional: gradient boosting on CME speed, width, direction, source location and pre-event solar-wind state, trained on 2013-2022 scoreboard CMEs (CAT-PUMA style).
- Cross-domain import (forecast combination): a trimmed-mean or stacked combination of physics models whose weights are fitted on pre-2023 events only.
- Cross-domain import (travel-time estimation in logistics): quantile regression of transit time with heteroscedastic noise, then predicting the median.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The scoreboard scores only CMEs that arrived (the API skips no-arrival CMEs by default); the challenger must predict all of S and cannot skip hard events.
- Using DONKI analyses revised after T_c, or science-quality coronagraph products, leaks hindsight; keep the analysis version available before T_c.
- Methods cover different CME subsets; compare on each method's own CMEs, not pooled averages.
- Arrival times are shock arrivals at L1 as recorded by the scoreboard; do not substitute ICME-catalog leading-edge times.
- Small subsets (39-51 CMEs) make sub-hour gains statistically weak; the bootstrap condition is against M2M on all of S.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/ccmc-cme-arrival-scoreboard-mae-2023-2024.md
```

Already set up? Say `run V3R1T4S on ccmc-cme-arrival-scoreboard-mae-2023-2024`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ccmc-cme-arrival-scoreboard-mae-2023-2024`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
