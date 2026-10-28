# SINTEF VRPTW (Gehring-Homberger, hierarchical objective): fewer vehicles, or equal vehicles and shorter distance, on a 200-1000 customer instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

SINTEF's TOP pages (maintained by Geir Hasle) list best known solutions for the 300 Gehring-Homberger VRPTW instances under the classic hierarchical objective: first minimise the number of vehicles, then total distance in double precision. Records keep moving: on the 1000-customer page (checked 2026-10-28), Seiya Takahashi, Tsubasa Kumamoto, Ryotaro Shin, Masahiro Nomura and Isao Ono (Institute of Science Tokyo, 'ISCT') set R1_10_5, R1_10_7..R1_10_10 and RC1_10_3, RC1_10_6, RC1_10_7 between 6 and 14 Sept 2026; Tobias Linke (Enpal Fulfillment, 'TL') then set R1_10_3 (91 vehicles, 44689.19) on 1 Oct 2026, and R1_10_6 (91, 46928.44) is credited to ISCT and TL independently (8 Sept / 3 Oct 2026). On the 200-customer page SINTEF noted on 22 Oct 2026 that four old MB/MB2 values not backed by detailed solutions (C1_2_10, R1_2_2, R2_2_4, RC2_2_10) were replaced by marginally higher values with checked detailed solutions from Victor Allis (Saviter, 'VAS', dated 17-19 Sept 2026), which coincide with values reported earlier by several authors. Earlier records include NVIDIA cuOpt (Jan 2024), SCR (Emapa) and CAINIAO. This is a different record set from the CVRPLIB DIMACS distance-only table (bank entry cvrplib-vrptw-gh-dimacs-bks). Find a feasible solution that is lexicographically better than the listed best for any instance.

## What counts as a win

A route file for one Gehring-Homberger instance that an independent checker confirms visits every customer exactly once, respects vehicle capacity, all time windows (service may start no earlier than ready time; waiting allowed; arrival no later than due date, including return to the depot) and the instance's vehicle limit, and that is lexicographically better than the (vehicles, distance) pair listed for that instance on the matching SINTEF page (fewer vehicles, or equal vehicles and distance lower by at least 0.01 in double precision), with the page re-fetched live immediately before claiming.

## Partial wins

- **sintef-gh-distance-improve:** Equal vehicles and strictly shorter distance on any 600-1000 customer instance, verified by the checker.
- **sintef-gh-vehicle-reduction:** One fewer vehicle on any instance (distance irrelevant), verified by the checker; the rarer and more valuable kind of improvement.
- **sintef-gh-reproduce-recent:** Independently reproducing (tying) one of the September-October 2026 1000-customer records (ISCT or TL) from scratch in under 24 laptop-hours, verified by the checker.

## How a win is checked

Instances: https://www.sintef.no/globalassets/project/top/vrptw/homberger/1000/homberger_1000_customer_instances.zip (and the 200-800 analogues linked from the size pages). Posted best solutions are linked per row (e.g. .../r1_10_3.91-44689.19.txt as of 2026-10-28). A 30-line checker computes Euclidean distances in double precision, travel time = distance, service times from the file, and checks capacity, windows, coverage and vehicle count; first confirm it reproduces the vehicles and distance of the currently posted file for the row, then run it on the claim. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.sintef.no/projectweb/top/vrptw/1000-customers/>

## Sources

- <https://www.sintef.no/projectweb/top/vrptw/1000-customers/>
- <https://www.sintef.no/projectweb/top/vrptw/>
- <https://www.sintef.no/projectweb/top/vrptw/800-customers/>
- <https://www.sintef.no/projectweb/top/vrptw/600-customers/>
- <https://www.sintef.no/projectweb/top/vrptw/400-customers/>
- <https://www.sintef.no/projectweb/top/vrptw/200-customers/>
- <https://www.sintef.no/globalassets/project/top/vrptw/homberger/1000/homberger_1000_customer_instances.zip>
- <https://www.sintef.no/contentassets/51a833740c45438b99b2935fd1c057d1/r1_10_3.91-44689.19.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Route minimisation first: the Nagata-Braysy ejection-pool heuristic with squeeze and insertion-ejection is still the strongest tool for removing a vehicle; run it for long times on instances whose vehicle count has not changed since 2018-2019 (many SCR/CAINIAO rows).
- Distance phase: EAX-based memetic algorithms (Nagata, Braysy and Dullaert) and edge-diversity variants like the 2026 Institute of Science Tokyo method; start from posted best solutions and polish.
- Seed from the CVRPLIB DIMACS-objective BKS files for the same instances: those distance-optimised solutions often use more vehicles but contain excellent route fragments for the hierarchical objective.
- Logistics-from-biology import: ant-colony pheromone matrices built from all posted best solutions across the 10 instances of a family (e.g. R1_10_1..10 share customer locations) as a prior on good edges.
- GPU import: batch evaluation of millions of 2-opt*/or-opt moves per second on a laptop GPU (Apple Metal) as in the NVIDIA cuOpt records of Jan 2024.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Hierarchical objective: a shorter distance with one more vehicle is worse; a vehicle reduction counts even with a much longer distance.
- Precision: SINTEF uses unrounded Euclidean distances; the CVRPLIB table for the same instances truncates to one decimal and ignores vehicle count, so a result must be scored against the SINTEF row only.
- Time windows include the return to the depot by its due date and service times at customers; omitting either accepts infeasible routes.
- Old table values can be infeasible: in Oct 2026 SINTEF replaced four 200-customer MB/MB2 entries that were not backed by feasible detailed solutions with slightly higher VAS values; matching an older, lower literature value is not a win unless the checker accepts the routes.
- File naming: posted solution files use inconsistent names (dots, hyphens, '-converted'); read the row's numbers from the page, not from the file name.
- Re-fetch the page before claiming; records changed repeatedly in Sept and Oct 2026 (latest 1000-customer change 3 Oct 2026; 200-customer page revised 22 Oct 2026), and independent groups have tied the same value.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/sintef-vrptw-gh-hierarchical-bks.md
```

Already set up? Say `run V3R1T4S on sintef-vrptw-gh-hierarchical-bks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sintef-vrptw-gh-hierarchical-bks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
