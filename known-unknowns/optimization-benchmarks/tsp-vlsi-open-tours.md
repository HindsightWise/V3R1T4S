# VLSI TSP collection (Bonn / Waterloo): a shorter tour for one of the 30 unsolved instances (14,233 to 744,710 cities)

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (EUC_2D, 14k-745k cities; checking a tour takes seconds) · open as of 2026-10-30

## The problem

The 102 VLSI instances were contributed by André Rohe from VLSI data of the Forschungsinstitut für Diskrete Mathematik, Universität Bonn, and are hosted by William Cook at math.uwaterloo.ca/tsp/vlsi. They range from 131 to 744,710 cities, with TSPLIB EUC_2D distances. The status page (last updated 3 May 2017; byte-identical on 2026-10-28 and 2026-10-29) lists 72 instances solved by Concorde and 30 open. Six of the open ones have Concorde lower bounds (tour/bound): xrb14233 45,462/45,450, xia16928 52,850/52,838, pjh17845 48,092/48,083, frh19289 55,798/55,791, fnc19402 59,287/59,275 and ido21215 63,517/63,501. The other 24 have no published bound (fma21553 66,527 through lrb744710 1,611,232). The record tours are by Keld Helsgaun (LKH); Hung Dinh Nguyen; Changxing Dong, Gerold Jäger, Paul Molitor and Dirk Richter; Yuichi Nagata (EAX); Kazuma Honda, Yuichi Nagata and Isao Ono; and Xavier Clarist. The instance logs date them from 2003 (xia16928 by Nguyen, lsb22777 by Helsgaun) to 16 February 2017 (lrb744710 by Clarist). For nine instances (fma21553, xrh24104, bbz25234, irx28268, icx28698, pbh30440, xib32892, fry33203 and ics39603) the summary lists a shorter tour than the instance's own log, so those records are undated. The bounds come from Concorde (Applegate, Bixby, Chvátal and Cook). Only five of the 30 record tours can be downloaded (xia16928, lsb22777, dan59296, sra104815, lrb744710); the other instance pages link older, longer tours. A search on 2026-10-29 found no shorter published tours. Find a tour strictly shorter than the listed record for any open instance.

## What counts as a win

A tour in TSPLIB TOUR_SECTION form (cities 1..n, each exactly once) for one of the 30 instances whose Gap column on https://www.math.uwaterloo.ca/tsp/vlsi/summary.html is not 'Optimal'. A standalone checker computes TSPLIB EUC_2D lengths (each edge int(sqrt(dx^2+dy^2) + 0.5)) on the instance file https://www.math.uwaterloo.ca/tsp/vlsi/ < name > .tsp (.tsp.gz for sra104815, ara238025, lra498378 and lrb744710). The closed-tour length must be strictly below the Tour column for that instance on the summary page, re-fetched immediately before claiming, and below any shorter tour found in a literature search at claim time. The checker must first reproduce posted tours exactly: xrb14233.tour gives 45,464 and dan59296.tour gives 165,371 (verified 2026-10-29). The tour file, the checker, the instance sha256 and the summary snapshot are saved together. Nothing is sent to Cook by the agent; the write-up goes to the human.

## Partial wins

- **vlsi-unposted-record-ties:** Checker-validated tours that exactly match the record length on at least three of the 25 open instances whose posted tour file is longer than the record (for example xrb14233 45,462 vs posted 45,464; fht47608 125,104 vs 125,133; lra498378 2,168,039 vs 2,169,314). This is non-trivial because those record tours are not published.

## How a win is checked

Download the .tsp file (TSPLIB NODE_COORD_SECTION, EUC_2D) and the tour. A 40-line Python checker verifies the permutation and sums the nint edge distances as TSPLIB defines them. Verified 2026-10-29: the posted xrb14233 tour gives 45,464 and the posted dan59296 tour gives 165,371, which equals the record. It takes seconds, even for lrb744710. Re-fetch summary.html and compare with the Tour column.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.math.uwaterloo.ca/tsp/vlsi/summary.html>

## Sources

- <https://www.math.uwaterloo.ca/tsp/vlsi/index.html>
- <https://www.math.uwaterloo.ca/tsp/vlsi/summary.html>
- <https://www.math.uwaterloo.ca/tsp/vlsi/xrb14233.log.html>
- <https://www.math.uwaterloo.ca/tsp/vlsi/lrb744710.log.html>
- <https://www.math.uwaterloo.ca/tsp/vlsi/dan59296.tsp>
- <https://www.math.uwaterloo.ca/tsp/vlsi/dan59296.tour>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- GA-EAX (Nagata and Kobayashi's edge assembly crossover, with the local EAX variant for 100k-city scale used by Honda, Nagata and Ono) produced the fht47608, bna56769 and icx28698 records here and the October 2025 World TSP record. Seed its population with LKH tours.
- LKH-2/LKH-3 with alpha-nearness or POPMUSIC candidate sets, many independent runs, then tour merging (Cook-Seymour branch decomposition) is the method behind most VLSI records. For 100k+ instances, partition (Karp or tour segments) and re-optimise the boundary regions, as Dong and Molitor did.
- The 24 instances without bounds are the least saturated; the largest (ara238025, lra498378, lrb744710) were last improved by Clarist between November 2012 and February 2017.
- For a cheap gap diagnosis, compute a Held-Karp 1-tree bound or a short Concorde root LP to see which instances have the largest tour-to-bound gap.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- On 25 of the 30 instance pages the 'Tour' link is an older, longer tour (xrb14233.tour is 45,464; the record is 45,462). Beating the downloadable tour is not a win.
- The summary page has not changed since 2017, so a better tour may exist in the literature; search before claiming. Cook offers to post improvements: this is a records table, not a prize challenge.
- EUC_2D rounding (nint) must match TSPLIB exactly; floats or truncation change lengths by many units.
- Four large instances are gzipped (.tsp.gz), and lrb744710 needs memory-efficient code.
- There are 30 open instances (6 with bounds plus 24 marked 'xxx'); everything up to xvb13584 is Optimal.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/tsp-vlsi-open-tours.md
```

Already set up? Say `run V3R1T4S on tsp-vlsi-open-tours`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tsp-vlsi-open-tours`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
