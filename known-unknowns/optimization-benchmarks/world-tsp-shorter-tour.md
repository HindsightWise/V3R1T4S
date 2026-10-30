# MOONSHOT - World TSP (1,904,711 cities): a tour shorter than Nagata's 7,515,755,912

🚚 **Optimization benchmarks** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days to weeks (1.9M cities with the GEOM great-circle metric; 11.5 MB instance; checking a tour takes about a minute in Python) · open as of 2026-10-30

## The problem

Cook's World TSP covers all 1,904,711 populated places in the NIMA and GNIS geographic-names databases plus Antarctic research bases, with the GEOM great-circle metric in metres. The record of 7,515,755,912 was found by Yuichi Nagata on 17 October 2025. He added Keld Helsgaun's 7,515,755,956 tour (15 February 2021, LKH, started from Xavier Clarist's 7,515,767,286) to a GA-EAX population and continued the search, gaining 44 m. The Concorde lower bound of 7,512,218,268 (5 June 2007) leaves a gap under 0.0471%. The page (updated 24 October 2025, unchanged on 2026-10-29) lists the full record history since 2003 (Helsgaun, Clarist, and Nguyen, Yoshihara, Yamamori and Yasunaga) and invites improvements. Between October 2011 and June 2020 the record fell by only 7,604 m in total. Find a tour shorter than the posted record.

## What counts as a win

A tour of all 1,904,711 cities in TSPLIB TOUR_SECTION form, each city exactly once. Its length under Cook's GEOM norm on https://www.math.uwaterloo.ca/tsp/world/world.tsp.gz must be strictly below the 'best reported tour' on https://www.math.uwaterloo.ca/tsp/world/index.html, re-fetched immediately before claiming. The GEOM norm is defined at https://www.math.uwaterloo.ca/tsp/world/geom.html: coordinates are decimal degrees, and each edge costs (int)(6378388.0*atan2(sqrt(q1^2+q2^2), q5) + 1.0). The checker must first reproduce 7,515,755,912 from the posted https://www.math.uwaterloo.ca/tsp/world/world.7515755912.tour.gz (verified 2026-10-29). The tour, the checker and the page snapshot are saved together. Nothing is sent to Cook by the agent; the write-up goes to the human.

## How a win is checked

Download world.tsp.gz and the claimed tour. A Python checker implementing geom_edgelen exactly as published (double precision; M_PI = 3.14159265358979323846264) reproduced the posted record 7,515,755,912 on 2026-10-29 in about a minute. Re-fetch index.html for the current record.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.math.uwaterloo.ca/tsp/world/index.html>

## Sources

- <https://www.math.uwaterloo.ca/tsp/world/index.html>
- <https://www.math.uwaterloo.ca/tsp/world/geom.html>
- <https://www.math.uwaterloo.ca/tsp/world/world.tsp.gz>
- <https://www.math.uwaterloo.ca/tsp/world/world.7515755912.tour.gz>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Nagata's 2025 gain came from injecting the previous record into a GA-EAX population. A different strong population (several LKH-3 runs on partitions, each re-merged) fed into EAX is the closest analogue a laptop can run.
- Partition-and-repair: split the planet into overlapping regions (for example per country or per grid cell), re-optimise each region's subpath with fixed boundary cities using LKH-3 or Concorde, and accept only improvements. Most recent gains have been metres, so many small local wins add up.
- Re-run Or-opt and 3-opt sweeps with exact GEOM evaluation near the poles and the antimeridian, where earlier codes that used approximate distances may have left slack.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The GEOM norm is not TSPLIB GEO: use the published geom_edgelen with its +1.0 and integer truncation. A different rounding changes the total by thousands.
- The page's lower-bound sentence still names Helsgaun's tour; the current record is Nagata's 7,515,755,912 (October 2025).
- Memory: hold coordinates as float64 arrays and evaluate edges on the fly. A full candidate graph for 1.9M cities needs care on a laptop.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/world-tsp-shorter-tour.md
```

Already set up? Say `run V3R1T4S on world-tsp-shorter-tour`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `world-tsp-shorter-tour`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
