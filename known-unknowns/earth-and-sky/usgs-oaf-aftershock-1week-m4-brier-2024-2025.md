# USGS operational aftershock forecasts 2024-2025: lower Brier score than USGS for 'at least one M4+ aftershock within a week'

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: laptop-hours (about 1,400 forecast JSON files and 67 regional ComCat queries; Reasenberg-Jones or ETAS fits run in seconds per sequence) · open as of 2026-10-30

## The problem

USGS publishes an operational aftershock forecast (OAF product in ComCat; Jeanne Hardebeck, Andrew Michael, Morgan Page, Nicholas van der Elst, Andrea Llenos, Michael Barall, Kevin Milner and colleagues) after M5+ earthquakes in and near the US, re-issued on a schedule. Each version gives, for 1-day, 1-week, 1-month and 1-year windows, the probability of at least one event of M3+, M4+, M5+... inside a stated circle, from Reasenberg-Jones (generic, Bayesian or sequence-specific) or, recently, ETAS. For mainshocks of M5+ between 2024-01-01 and 2025-10-01 (75 events with OAF products), all versions issued within 14 days of the mainshock with a circular region number 1,377 from 67 sequences (251 RJ generic, 990 RJ Bayesian, 57 RJ sequence-specific, 79 ETAS). Scored against live ComCat (any event other than the mainshock with magnitude >= 4.0 inside that version's own circle during the window), USGS's 1-week M4+ probabilities have Brier score 0.0778 (196 positive windows from 17 sequences; in-sample climatology 0.1221; log-loss 0.2734); 1-week M5+ 0.0367 (104 positive) and 1-day M4+ 0.0503 (146 positive) (computed 2026-10-30). Retrospective tests of operational aftershock forecasts are an active topic. Weiqiang Zhu's QuakeGen diffusion model (arXiv:2607.24109, July 2026) reports beating a reimplemented Bayesian Reasenberg-Jones baseline (opensha-oaf with generic priors) on 80 M4.5+ mainshocks of 2024-2025 in log-likelihood and spatial scores, but it does not score the issued USGS probabilities, these windows or the Brier score. No published model is shown to beat these exact USGS issues. Open task: issue-time-honest probabilities that beat them.

## What counts as a win

A saved file with a probability for every one of the scored versions (ComCat query producttype=oaf, starttime=2024-01-01, endtime=2025-10-01, minmagnitude=5; all OAF versions from includesuperseded=true with updateTime within 14 days of origin and regionType circle), for the forecast's own 1-week window and circle and the M > =4.0 bin, plus code that regenerates it using only ComCat events with origin time before min(creationTime, window timeStart) of that version, and parameters tuned only on sequences before 2024-01-01, whose Brier score is strictly lower (direction: min) than USGS's 'probability' values on the same windows (0.0778 as of 2026-10-30), both scored against outcomes from a live ComCat query re-fetched immediately before claiming (outcome 1 when any event other than the mainshock with magnitude >= 4.0 has origin time in [timeStart, timeEnd) and epicentre within that version's own circle by haversine distance), with the 95% interval of the Brier difference (USGS Brier minus claimed Brier) from a bootstrap that resamples whole sequences (10,000 draws) having a lower bound above 0.

## Partial wins

- **p1:** Brier score strictly below USGS (0.0778 as of 2026-10-30) on the 1-week M > =4 windows under the same rules, without the bootstrap condition.
- **p2:** Brier score strictly below USGS on the 1-week M > =5 windows (0.0367) and on the 1-day M > =4 windows (0.0503), both, same rules, no bootstrap.
- **p3:** Log-loss strictly below USGS's (0.2734) on the 1-week M > =4 windows (probabilities clipped to [1e-4, 1-1e-4] for both), same rules.

## How a win is checked

Skeptic re-runs the ComCat queries, downloads every forecast.json version, recomputes outcomes with a haversine distance test per window and the Brier and log-loss scores for USGS and the claim with an independent script, regenerates the claimed probabilities through a harness that drops ComCat events at or after each cutoff, and runs the sequence bootstrap. About 1-2 hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&producttype=oaf&starttime=2024-01-01&endtime=2025-10-01&minmagnitude=5>

## Sources

- <https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&producttype=oaf&starttime=2024-01-01&endtime=2025-10-01&minmagnitude=5>
- <https://earthquake.usgs.gov/data/oaf/>
- <https://earthquake.usgs.gov/fdsnws/event/1/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: sequence-specific ETAS with magnitude-of-completeness correction for early incompleteness (Omori-Utsu with time-dependent Mc), updated at each issue time.
- Conventional: Bayesian combination of generic tectonic-regime priors with sequence data, calibrated on pre-2024 sequences.
- Cross-domain import (epidemic nowcasting): renewal-process forecasts with right-truncation correction for recently detected events.
- Cross-domain import (insurance cat modelling): calibrating probabilities with isotonic regression per region type on historical sequences.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- ComCat magnitudes and small-event lists are revised after the fact; using revised pre-issue events is allowed, but post-issue events are not, and the window timeStart can precede creationTime by up to 3.4 h.
- Region centres move between versions of the same sequence (up to about 96 km, us7000pn9s; one version filed under the 2025 Kamchatka event carries a Myanmar circle); score each version against its own circle, and query ComCat per distinct circle, not once around the first centre (that undercounts M4 outcomes: 178 instead of 196 positives).
- Outside the US networks ComCat is incomplete below about M4.5, which is why M3 bins are not scored; M4 outcomes abroad can also be undercounted, so learning catalog gaps rather than seismicity is a known trap.
- Weekly re-issues of long sequences (e.g. the 2025 Kamchatka M8.8) dominate counts; the sequence bootstrap guards against one sequence carrying the result.
- A few forecast.json files contain trailing commas (Kamchatka) and some superseded products have empty contents; parse leniently instead of dropping them.
- Outcomes are any event with magnitude >= 4.0 except the mainshock itself; foreshocks or doublets inside the window count. ComCat caps a query at 20,000 events, so query outcomes at M >= 3.95, not M >= 2.95, for large sequences.
- QuakeGen (arXiv:2607.24109) was compared with a reimplemented Reasenberg-Jones baseline, not with the issued USGS products, and it conditions on data up to 1.6 h after the mainshock rather than on each version's issue time. It is not evidence that this target is solved, and its published outputs do not score as a claim without the issue-time harness.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/usgs-oaf-aftershock-1week-m4-brier-2024-2025.md
```

Already set up? Say `run V3R1T4S on usgs-oaf-aftershock-1week-m4-brier-2024-2025`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `usgs-oaf-aftershock-1week-m4-brier-2024-2025`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
