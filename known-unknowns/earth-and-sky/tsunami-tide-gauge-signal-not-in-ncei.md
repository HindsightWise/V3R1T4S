# Tsunami recorded on open tide-gauge data but absent (as an event or at that gauge) from the NCEI Global Historical Tsunami Database

🌍 **Earth and sky** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (1-min gauge series are KB-MB per day) · open as of 2026-10-15

## The problem

The NOAA NCEI/WDS Global Historical Tsunami Database (HazEL) lists ~1,600 confirmed events with runup and tide-gauge observations; NCEI's own completeness studies (Wright, Arcos, Varner and Stroker 2021) note that small tsunamis seen only on tide gauges can be missing. The IOC Sea Level Station Monitoring Facility serves 1-min data from 1,000+ gauges openly. Open task: find a tsunami signal (from an earthquake, landslide, volcano or meteotsunami) clearly recorded on >= 2 open tide gauges that NCEI lists neither as an event nor as a runup/gauge observation at those stations.

## What counts as a win

A saved bundle (raw IOC SLSMF series for >= 2 gauges, de-tiding code, the travel-time model code, source parameters) showing: on each gauge, a band-passed (2-120 min) signal with peak amplitude > 5x the RMS of the preceding 24 h in the same band; arrival times at all the gauges the claim names in PREREG.md before scoring (at least 2) consistent within a window W with travel times computed from the source. For an earthquake (USGS ComCat) the travel times come from the claimant's own shallow-water model, and W is fixed in PREREG.md before scoring from a held-out check of that model against NCEI tide-gauge arrival times (the NCEI rows used, which exclude the claimed event, the model's errors on them and the rule that turns them into W are recorded there), and is at most +/- 20 min. For a meteotsunami (a pressure jump with propagating-front check) the timing model (the passage of the pressure front, or a reflected branch whose source region and reflection time are taken from meteorological data) is fixed in PREREG.md from meteorological data before scoring and validated on a separate NCEI-listed event named there (for example NCEI 5483 of 2013-06-13, which Wertman et al. 2014, doi:10.1038/srep07143, timed this way), with W set from that validation and capped the same way. W is used unchanged on the control days, where the signals must be absent on the same gauges in the same hours, and in the null test (kit/RUN.md step 3b, at least 400 controls), which reruns the whole pipeline with fake origin times. And the NCEI events API (https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/tsunamis/events) and runups API, re-fetched live immediately before claiming, have no event within +/- 1 day of the source in that region (main win) or no runup row for those gauges (partial win). WORDING OF 2026-10-29 (issue #253): the window W, 'all gauges' as the gauges named before scoring, the meteotsunami timing rule and p3's denominator and terms apply to claims filed after this wording reached the bank on main; claims filed earlier (#642 and #736 among them) are judged on the wording in force when they were filed (arrival times at all gauges within +/- 10 min of the computed travel times, and p3 with no stated denominator).

## Partial wins

- **p1:** Gauge observations (amplitude, arrival) for a listed NCEI event at >= 2 gauges where NCEI has no runup rows for those stations.
- **p2:** A meteotsunami (atmospheric pressure jump with matching propagation speed) with > 0.3 m amplitude on >= 2 gauges not in NCEI.
- **p3:** A completeness map, reproducible from saved code: of the USGS ComCat M >= 6.5 earthquakes of 2015-2025 that are shallow (ComCat depth <= 70 km) and subsea (epicentre in an ETOPO1 water cell; this drops the NCEI-listed Kaikoura 2016 and Palu 2018 tsunamis, whose epicentres fall on land), the fraction with a tsunami signal on open gauges (IOC SLSMF only; a signal is the main criterion's per-gauge test with its timing window and control days), set against NCEI's listing. The fraction is over the quakes with at least one usable open 1-min gauge within a travel-time range stated before scoring, usability judged only from data availability and the pre-event reference window; the coverage count and bounds on the fraction over all qualifying quakes are reported too.

## How a win is checked

Skeptic re-downloads the IOC SLSMF series (GET service.php query=data), re-runs de-tiding and band-pass, checks the travel-time model's held-out validation and the window W recorded in PREREG.md before scoring (W at most +/- 20 min, the claimed event left out of the validation rows; for a meteotsunami a timing model fixed from meteorological data and validated on a separate listed event), reruns the claimant's frozen travel-time model from the bundle (cross-checking its times against its own bathymetry-based or simple shallow-water estimate), applies the same W to that model's times at the named gauges, on the control days and in the fake-origin null, and re-queries the NCEI API. Under an hour, plus the null rerun.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-search>

## Sources

- <https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/event-search>
- <https://www.ioc-sealevelmonitoring.org/service.php>
- <https://www.ioc-sealevelmonitoring.org/list.php>
- <https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/tsunamis/events>
- <https://www.ngdc.noaa.gov/hazel/view/hazards/tsunami/runup-search>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: for every M >= 6.0 shallow offshore earthquake (USGS ComCat) since 2010, pull gauges within 1,500 km, de-tide (UTide), band-pass and test arrivals against travel-time predictions.
- Meteotsunami hunting: match gauge oscillations with pressure jumps in open surface-pressure data and propagation speeds near sqrt(g h).
- Cross-domain import (seismology): STA/LTA triggers and array beamforming across many gauges, treating the gauge network like a seismic array.
- Cross-domain import (audio signal processing): spectrogram ratio against a station's own long-term noise spectrum (as in speech enhancement) to reveal small tsunami energy.
- Cross-domain import (astronomy transient search): difference against a same-time-of-tide 'reference' built from control days, then threshold the residual like difference imaging.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Seiches and harbour resonances ring at similar periods on most days; the control-day test is mandatory.
- Tide-gauge glitches, datum runs and data gaps produce spikes; reject series with level runs, but state before scoring how many identical minutes count as a stuck sensor and in which hours you test for them: gauges that report in 1 cm steps repeat a value for long stretches around high and low water, and during a tsunami. On 2025-07-29/30, IOC petr and nksk (Kamchatka) had 20 and 26 runs of 10 or more identical minutes in the 24 h before the M8.8 origin (the longest 48 and 63 min) and runs of 10-13 min within 6 h after it.
- Storm surges and infragravity waves during storms mimic small tsunamis; check weather.
- NCEI may list the event under a different source time or as a 'questionable' validity code; search with tolerance and all validity codes.
- Do not report to NCEI or IOC; the claim is a vetted candidate.
- A +/-10 min arrival window is tight even for real tsunamis. On NCEI's own tide-gauge rows of definite earthquake tsunamis in 2005-2025 with an NCEI travel time of 15-120 min (298 rows, 81 events), first-arrival times from NCEI's epicentre (second-order fast marching with sqrt(g h) on ETOPO1 at 2 arcmin, gauge snapped to the nearest water cell) differ from NCEI's travel time by more than 10 min for 52% of rows (95% CI 36-67%, bootstrap over events), and for 38% of rows of M < 7.5 sources; 74% are within +/-20 min, and 6 of the 44 events with two or more rows have all rows within +/-10 min. A maintainer re-implementation on 2026-10-24 (32-neighbour Dijkstra on a 3.7 km azimuthal grid, at most 1.4% slow on a flat ocean) gave 51% of 300 rows outside +/-10 min (95% CI 36-65%), 34% for M < 7.5, 75% within +/-20 min and 8 of 44 multi-row events with all rows within +/-10 min. Validate the travel-time model against NCEI arrivals and report its error before scoring.
- Model travel times depend on the solver and the coast. Grid-graph shortest paths (Dijkstra) are always too slow, by an amount that depends on direction and, on a latitude/longitude grid, on latitude: on a flat ocean over 800 km the worst direction is +8.2% for 8 neighbours and +2.7% for 16 neighbours at the equator, and +15.0% and +6.6% at 60 degrees on a 0.1 degree grid (the 16-neighbour figures were measured by walshne-mit on PR #371 and reproduced independently). Check the claimant's own solver on a flat ocean against the analytic time before scoring. At the coast, gauges snapped to cells shallower than 10 m come out late (median +13 min against NCEI), and snapping to depth >= 20 m lowers the median over all rows from +6.7 to +2.3 min; the #253 models, which treated cells shallower than 5 m as land, came out early (-1.5 to -3.5 min). Fix the solver, depth floor and snapping rule before scoring.
- Coverage for p3: of the 264 USGS ComCat M >= 6.5, depth <= 70 km earthquakes of 2015-2025 with an epicentre in an ETOPO1 water cell (2 arcmin), 6 have no IOC SLSMF station of any status within 1,500 km and 42 none within 500 km, and an epicentre-in-water rule drops NCEI-listed tsunamis whose epicentres are on land (Kaikoura 2016, Palu 2018). Count quakes without usable open gauge data explicitly.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/tsunami-tide-gauge-signal-not-in-ncei.md
```

Already set up? Say `run V3R1T4S on tsunami-tide-gauge-signal-not-in-ncei`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tsunami-tide-gauge-signal-not-in-ncei`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
