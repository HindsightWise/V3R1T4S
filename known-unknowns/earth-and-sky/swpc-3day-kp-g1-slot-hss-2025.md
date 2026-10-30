# NOAA SWPC 3-day forecast 2025: beat SWPC's Heidke skill for G1+ (Kp >= 5-) 3-hour slots at 1-3 day lead

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: laptop-hours (363 archived forecast text files, the GFZ Kp file and OMNI/DONKI inputs are a few MB; models train on CPU) · open as of 2026-10-30

## The problem

NOAA SWPC issues a 3-day forecast twice daily with predicted Kp for every 3-hour slot over 3 UT days; NCEI archives the texts (daily_reports/3day_forecast; 363 of the 365 00:30 UTC issues of 2025 are present, 2025-07-17 and 2025-12-17 missing). Scoring those 363 issues against GFZ Potsdam's definitive Kp (Matzka et al.; all 2025 values definitive), on slots whose UT date falls in 2025, with the G1 threshold SWPC itself uses in the forecast (Kp >= 4.67, i.e. 5-, labelled '(G1)'), SWPC's day-2 forecasts (lead 23.5-47.5 h) give Heidke skill score HSS = 0.1462 (41 hits, 128 false alarms, 192 misses, 2,896 slots) and day-3 forecasts 0.1313 (30, 79, 202; 2,888 slots). Trivial baselines are far lower: 27-day recurrence 0.073, recurrence with +/-3 h tolerance 0.098, last-slot persistence 0.077 (day 2). For G2 (Kp >= 5.67) SWPC's day-2 HSS is 0.1725 (9, 28, 51). SWPC's MAE over all slots (day 2 1.1024, day 3 1.1082) is already beaten by a linear model on past Kp alone (1.044, 1.057; computed 2026-10-30), so MAE is not the open part: predicting which slots reach storm level from CMEs and high-speed streams one to three days ahead is. Credit: SWPC forecast office; GFZ Kp service (J. Matzka, C. Stolle, Y. Yamazaki and colleagues).

## What counts as a win

A saved file of Kp forecasts for every 3-hour slot of days 2 and 3 of each 2025 00:30 UTC issue present in the NCEI archive, restricted to slots whose UT date falls in 2025 (same slots as SWPC's 'NOAA Kp index breakdown'), plus code that regenerates it using only data timestamped before 00:30 UTC of the issue day (OMNI or real-time solar wind, DONKI CME analyses, coronagraph and EUV images, past Kp), with training and tuning on data before 2025-01-01 only, such that, against GFZ definitive Kp from https://kp.gfz.de/app/files/Kp_ap_since_1932.txt, the event 'Kp >= 4.67' gives an HSS strictly greater (direction: max) than SWPC's on day 2 and on day 3, as recomputed by the skeptic from the NCEI archive https://www.ngdc.noaa.gov/stp/space-weather/swpc-products/daily_reports/3day_forecast/2025/ re-fetched live immediately before claiming (0.1462 and 0.1313 as of 2026-10-30); the 95% interval of the day-2 HSS difference from a block bootstrap with 27-day blocks must have a lower bound above 0; and the all-slot MAE on days 2 and 3 must not exceed SWPC's.

## Partial wins

- **p1:** Day-2 HSS strictly above SWPC's 0.1462 under the same rules, without the bootstrap condition.
- **p2:** Day-3 HSS strictly above SWPC's 0.1313 under the same rules, without the bootstrap condition.
- **p3:** A day-2 HSS strictly above SWPC's for the stronger event Kp >= 5.67 (G2, 6-), same slots and rules, without the bootstrap condition (SWPC: 0.1725 from 9 hits, 28 false alarms, 51 misses as of 2026-10-30, recomputed by the skeptic).

## How a win is checked

Skeptic downloads the 2025 00:30 UTC files from NCEI, parses the Kp breakdown tables, scores them and the claimed forecasts against the GFZ file with an independent 2x2-table script, regenerates the claimed forecasts through a harness that refuses inputs timestamped at or after each issue time, and runs the block bootstrap. Under 1 hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.ngdc.noaa.gov/stp/space-weather/swpc-products/daily_reports/3day_forecast/2025/>

## Sources

- <https://www.ngdc.noaa.gov/stp/space-weather/swpc-products/daily_reports/3day_forecast/>
- <https://kp.gfz.de/app/files/Kp_ap_since_1932.txt>
- <https://www.swpc.noaa.gov/products/3-day-forecast>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: CME-arrival models (drag-based, ENLIL-like) driven by DONKI analyses plus coronal-hole area and position from EUV images for high-speed-stream timing.
- Conventional: classifier per slot on recurrence features (Kp 27 and 54 days earlier with time tolerance), coronal-hole features and CME flags, then thresholded to maximise HSS on 2015-2024.
- Cross-domain import (hydrology): flood-warning style event detection with tolerance windows, mapped back to slots.
- Cross-domain import (meteorology): calibrated probabilistic forecasts thresholded at the HSS-optimal probability, chosen on pre-2025 data only.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Day 1 of the 00:30 UTC issue includes the slot in progress and SWPC's day-1 MAE is already beaten by last-slot persistence; only days 2 and 3 are scored.
- GFZ Kp is in thirds (4.667 = 5-); use >= 4.6 to avoid floating-point misses, and the same threshold for forecast and observation.
- Slots of the 30-31 December issues that fall in January 2026 are excluded; including them changes SWPC's HSS to 0.1449 (day 2) and 0.1302 (day 3).
- Choosing the decision threshold on 2025 outcomes is test-set tuning; fix it on earlier years.
- The NCEI archive has gaps before 2025 (e.g. 2023-09 to 2024-02), so pre-2025 SWPC forecasts are not a complete training reference.
- DONKI entries are revised after the fact; use only versions available before each issue time.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/swpc-3day-kp-g1-slot-hss-2025.md
```

Already set up? Say `run V3R1T4S on swpc-3day-kp-g1-slot-hss-2025`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `swpc-3day-kp-g1-slot-hss-2025`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
