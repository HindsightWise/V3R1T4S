# Sartori-Buriol real-road PDPTW instances (100-5000 locations): hierarchically beat a best known solution in the live GitHub table

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (instance files carry full OSRM travel-time matrices, up to 5000 x 5000 integers) · open as of 2026-10-30

## The problem

Carlo S. Sartori and Luciana S. Buriol (Computers & Operations Research 2020) published 300 pickup-and-delivery-with-time-windows instances built from real addresses and OSRM travel times in Barcelona, Berlin, New York and Porto Alegre. There are 12 sizes (100, 200, 400, 600, 800, 1000, 1500, 2000, 2500, 3000, 4000 and 5000 locations) with 25 instances each, under CC BY 4.0 on Mendeley Data (doi 10.17632/wr2ct4r22f.2). Sartori maintains the best known solutions, each with a solution file, in github.com/cssartori/pdptw-instances (solutions/README.md and solutions/bks.dat). They are ranked hierarchically: fewer vehicles first, then lower total travel time (integer minutes). The table is live. On 2026-10-30, 270 of the 300 rows had been set by the BigThree team (Dmitriy Yampolskiy, Egor Nikolaev, Daria Savina; Smart Logistics Point) on 01-Oct-2026. One row is by Pengfei He, Zixiang Tian (spelled 'Tain' in the README), Jin-Kao Hao, Yuning Chen and Qinghua Wu (poa-n800-5, 70 vehicles / 4271, 25-Aug-2026). One is by Yuskov, Kulachenko, Kochetov, Vasilyev et al. (nyc-n100-3, 28-Apr-2025). Advantum (Churilov & Galko) holds 1 row (2025), CUHK-SZ with Huawei 2 (2024), Isaiah Reimer (RideCo) 12 (2023) and Sartori & Buriol 13 (2019). The table has no optimality column. All rows with 200 or more locations moved in 2024-2026 except ber-n200-3 (Sartori & Buriol, 2019) and ber-n200-4 (Reimer, 2023). Find a feasible solution that is hierarchically better than the listed BKS on any instance with 200 to 5000 locations, other than ber-n200-3 and ber-n200-4.

## What counts as a win

A solution file in the repository's format ('Route k : id id ...', depot 0 not listed) for one instance with 200-5000 locations, other than ber-n200-3 and ber-n200-4. It is judged by a standalone checker written from instances/how_to_read.txt, which verifies that: (a) every node 1..SIZE-1 is visited exactly once; (b) each pickup i and its delivery i+(SIZE-1)/2 are on the same route, with the pickup first; (c) the running load never exceeds CAPACITY; (d) on each route, starting at the depot at t=0, for each next node a: t += T[prev][a], t = max(t, etw_a), t <= ltw_a, then t += dur_a, and the return to the depot satisfies t <= the depot's ltw; and (e) cost = the sum of T over all arcs, the return arc included. The result must have strictly fewer routes than the instance's row in solutions/bks.dat, or the same number of routes and a strictly smaller integer cost. The bks.dat row is re-fetched live right before claiming (raw.githubusercontent.com/cssartori/pdptw-instances/master/solutions/bks.dat; 300 rows, sha256 036fd50d... on 2026-10-30). Before any claim, the same checker must reproduce the vehicles and cost in the posted BKS file name ( < instance > . < vehicles > _ < cost > .txt in solutions/files/) for that instance and for poa-n800-5 (70 / 4271, reproduced by the vetter 2026-10-30). The solution, checker, instance sha256 and bks.dat snapshot are saved together. The agent emails and submits nothing; the write-up goes to the human.

## Partial wins

- **p1:** For an instance with 1000 or more locations, a feasible solution (same checker) whose total cost is strictly below the bks.dat cost while using more vehicles than the BKS: cost-side progress that is not a hierarchical win.
- **p2:** For an instance with 1000 or more locations, a feasible solution with exactly the BKS vehicle count and cost whose undirected arc set differs from the posted BKS file's arc set in at least 10% of arcs (same checker computes the comparison): an independent alternative optimum candidate.

## How a win is checked

The skeptic downloads the size-group zip from https://data.mendeley.com/datasets/wr2ct4r22f/2 (public, CC BY 4.0) and the posted BKS file from https://github.com/cssartori/pdptw-instances/tree/master/solutions/files. It runs an independent checker (rules (a)-(e) above, written from how_to_read.txt; it need not run the repository's validator.py) on the posted file first, which must reproduce the vehicles and cost in its file name, then on the claimed file. Finally it re-fetches bks.dat and compares the instance's row hierarchically. Minutes per instance; the 5000-location matrices are about 25 million integers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/cssartori/pdptw-instances/blob/master/solutions/README.md>

## Sources

- <https://github.com/cssartori/pdptw-instances>
- <https://github.com/cssartori/pdptw-instances/blob/master/solutions/README.md>
- <https://raw.githubusercontent.com/cssartori/pdptw-instances/master/solutions/bks.dat>
- <https://github.com/cssartori/pdptw-instances/blob/master/instances/how_to_read.txt>
- <https://data.mendeley.com/datasets/wr2ct4r22f/2>
- <https://doi.org/10.1016/j.cor.2020.105065>
- <https://arxiv.org/abs/2405.00230>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Seed from the posted BKS file and run pair-aware ALNS (Ropke-Pisinger removal and insertion of whole request pairs) with a route-elimination phase (ejection pool / squeeze); vehicle count is the primary objective, so most value lies in removing one route.
- Decomposition for the 2000-5000 location instances (Hiermann & Schiffer 2024, arXiv 2405.00230, built on these instances): split by geography or time, re-optimise sub-problems, re-merge.
- Exact polishing at equal vehicle count: fix all but 3-5 neighbouring routes and solve the induced small PDPTW exactly with CP-SAT or set partitioning over enumerated routes; any strict improvement is global.
- Travel times are asymmetric road times (OSRM); neighbourhoods that assume symmetry (2-opt reversal) change cost in both directions and must be re-evaluated in full.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The repository's own validator.py checks precedence with a global visited array, so a delivery on a different route from its pickup can pass it. PDPTW requires the same route, so the independent checker must check same-route pairing explicitly.
- Ranking is hierarchical (updater.py compares vehicles first, then cost): a lower-cost solution with more vehicles is not better.
- The table moves in bursts (270 rows replaced on 2026-10-01). A win against a cached bks.dat may already be stale, so re-fetch the raw file right before claiming.
- The 100-location rows (many unchanged since 2019) and the two 200-location rows unchanged since 2019/2023 (ber-n200-3, ber-n200-4) are left out of the win condition. The table carries no optimality information, and long-unbeaten small rows may be optimal.
- SIZE counts the depot. Pickups are 1..(SIZE-1)/2, and their deliveries are offset by (SIZE-1)/2. Cost excludes service and waiting time, but both count toward time-window feasibility.
- The Mendeley 'Download All' bundle is 1.23 GB as the page reports it (the 14 files in Instances/ sum to 1.32 GB). Range-read only the size-group zip you need from the Instances folder (n800.zip is 13.35 MB; n5000.zip is 506.73 MB); the page lists them only with JavaScript, so the folder ids come from /public-api/datasets/wr2ct4r22f/folders/2.
- This target overlaps in problem class with the bank's sintef-lilim-pdptw-bks (Li & Lim instances, SINTEF table). It is a different instance library and table, so do not mix the two tables or their solution formats.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/sartori-buriol-pdptw-bks.md
```

Already set up? Say `run V3R1T4S on sartori-buriol-pdptw-bks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sartori-buriol-pdptw-bks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
