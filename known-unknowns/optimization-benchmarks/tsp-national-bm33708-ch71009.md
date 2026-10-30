# National TSPs: a shorter tour for Burma (bm33708) or China (ch71009), the two unsolved Waterloo country instances

🚚 **Optimization benchmarks** · standard · tractability ★★☆☆☆ · compute: laptop-days (33,708 and 71,009 cities, EUC_2D; checking a tour takes seconds) · open as of 2026-10-30

## The problem

William Cook's national TSPs (populated places from the National Imagery and Mapping Agency geographic-names database, TSPLIB EUC_2D) complement TSPLIB. The status page (last updated 31 July 2022, unchanged on 2026-10-29) lists 27 instances, though its introduction still says 25: 25 are optimal and two are open. bm33708 (Burma) has tour 959,289 (Yuichi Nagata, 10 July 2007 per the computation log; the tour file's comment says October 7, 2007) against Concorde bound 959,011 (26 August 2001). ch71009 (China) has tour 4,566,506 (Nagata, 10 July 2007) against Concorde bound 4,565,452 (15 September 2001). The computation logs show earlier tours by Keld Helsgaun (LKH, 2001-2006) and Hung Dinh Nguyen (2003). Both records have stood for 19 years. The ch71009 instance page links Nguyen's older 4,566,563 tour, not the record. Find a shorter tour for either instance.

## What counts as a win

A tour in TSPLIB TOUR_SECTION form (cities 1..n, each exactly once) for bm33708 or ch71009. A standalone checker computes TSPLIB EUC_2D lengths (each edge int(sqrt(dx^2+dy^2) + 0.5)) on https://www.math.uwaterloo.ca/tsp/world/bm33708.tsp or https://www.math.uwaterloo.ca/tsp/world/ch71009.tsp. The closed-tour length must be strictly below the Tour column for that instance on https://www.math.uwaterloo.ca/tsp/world/summary.html, re-fetched immediately before claiming, and below any shorter tour found in a literature search. The checker must first reproduce the posted tours: bm33708.959289.tour gives 959,289 and ch71009.tour gives 4,566,563 (verified 2026-10-29). The tour, the checker, the instance sha256 and the page snapshot are saved together. Nothing is sent to Cook by the agent; the write-up goes to the human.

## Partial wins

- **ch71009-record-tie:** A checker-validated ch71009 tour of length exactly 4,566,506, matching Nagata's record, which is not posted (the posted tour is 4,566,563).

## How a win is checked

Download the .tsp file and the tour. The 40-line EUC_2D checker (TSPLIB nint per edge) reproduced 959,289 from https://www.math.uwaterloo.ca/tsp/world/bm33708.959289.tour and 4,566,563 from https://www.math.uwaterloo.ca/tsp/world/ch71009.tour on 2026-10-29. Seconds. Re-fetch summary.html and the computation logs (https://www.math.uwaterloo.ca/tsp/world/bmlog.html and https://www.math.uwaterloo.ca/tsp/world/chlog.html) before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.math.uwaterloo.ca/tsp/world/summary.html>

## Sources

- <https://www.math.uwaterloo.ca/tsp/world/summary.html>
- <https://www.math.uwaterloo.ca/tsp/world/countries.html>
- <https://www.math.uwaterloo.ca/tsp/world/bmlog.html>
- <https://www.math.uwaterloo.ca/tsp/world/chlog.html>
- <https://www.math.uwaterloo.ca/tsp/world/bm33708.tsp>
- <https://www.math.uwaterloo.ca/tsp/world/ch71009.tsp>
- <https://www.math.uwaterloo.ca/tsp/world/bm33708.959289.tour>
- <https://www.math.uwaterloo.ca/tsp/world/ch71009.tour>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- GA-EAX (Nagata and Kobayashi) set both records in 2007 and the World TSP record in 2025. A modern EAX run seeded with LKH tours, on 10 cores for days, is the most direct attack.
- LKH-3 with many trials from the posted tour, followed by tour merging of several near-record tours (Cook-Seymour branch decomposition), often finds the last few units.
- The geography concentrates difficulty in dense clusters. Fix the long inter-cluster edges of the record tour and re-solve the clusters with Concorde, iterating over overlapping windows.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The countries page still shows old gaps and 'within x% of optimal' notes, and the summary's Gap column for bm33708 (0.031%) was computed from an older tour. Use the Tour and Bound columns.
- Beating the posted ch71009 tour (4,566,563) is not enough; the record is 4,566,506.
- The bm33708 tour file's internal NAME and COMMENT say 958289 (a typo); its true length is 959,289.
- EUC_2D rounding must be TSPLIB nint; GEOM or float distances give different lengths.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/tsp-national-bm33708-ch71009.md
```

Already set up? Say `run V3R1T4S on tsp-national-bm33708-ch71009`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tsp-national-bm33708-ch71009`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
