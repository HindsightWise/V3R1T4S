# MMLIB / Boctor multi-mode resource-constrained project scheduling: shorter makespan for an open instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The multi-mode RCPSP lets each activity run in one of several modes (duration and renewable/non-renewable resource use). Mario Vanhoucke and Jose Coelho's SolutionsUpdate site tracks open instances in MMLIB (Van Peteghem and Vanhoucke 2014) and Boctor's sets (Boctor 1996): its MMRCPSP table (headed September 2026, re-checked 2026-10-28) gives MMLIB50 54 of 540 open, MMLIB100 114 of 540, MMLIB+ 1,965 of 3,240 (average gap 14.7%), and Boctor100 33 of 120 (average gap 14.8%). Each SolutionsUpdate dataset page (e.g. http://solutionsupdate.ugent.be/dataset/boctor100) publishes a per-instance best-known-solution CSV; recent Boctor100 bounds were submitted by Shichen Tian (June and September 2026). The MMLIB GitHub release (v2.1, published 23 June 2026; README updated 23 July 2026) contains the MMLIB50, MMLIB100 and MMLIB+ instances and an Excel file of LB-lit/UB-lit values that lags the site (on 2026-10-28 the Excel still has 82 MMLIB50 and 52 Boctor100 rows with LB-lit < UB-lit); the Boctor instances themselves are distributed by SolutionsUpdate and PSPLIB, not in that release. Find a feasible mode assignment and schedule with makespan strictly below the best known upper bound of an open instance.

## What counts as a win

A mode assignment plus start times for one MMLIB50, MMLIB100, MMLIB+ or Boctor100 instance that is open (LB < UB) on its SolutionsUpdate dataset page, that an independent checker confirms satisfies precedences, renewable capacities in every period and non-renewable totals, with makespan strictly below both that instance's value in the best-known-solution CSV linked from http://solutionsupdate.ugent.be/dataset/<mm50|mm100|mmplus|boctor100> and its UB-lit in the latest MMLIB release Excel, all re-fetched live immediately before claiming.

## Partial wins

- **mmlibplus-improve-any:** Strict UB improvement on any open MMLIB+ instance, verified by the checker.
- **mmlib100-improve-any:** Strict UB improvement on any open MMLIB100 or Boctor100 instance, verified by the checker.
- **mmlib-close-by-lb:** A schedule matching the listed lower bound of an open instance (closing it), verified by the checker.

## How a win is checked

MMLIB instances: the release at https://github.com/MarioVanhoucke/MMLIB-Multi-Mode-Resource-Constrained-Project-Library/releases/latest (MMLIB50.zip, MMLIB100.zip, MMLIB+.zip and 'MMLIB (Parameters and BKS).xlsx'). Boctor instances are not in that release: use the Boctor.zip linked from http://solutionsupdate.ugent.be/dataset/boctor100 (or the PSPLIB multi-mode data page). Current per-instance values: the *_BKS.csv linked from each SolutionsUpdate dataset page (e.g. Boctor100_0_BKS.csv, MM50_7_BKS.csv; columns ID;Type;Value;Time;Solution). The checker reads the instance (activities, modes, durations, renewable and non-renewable demands, availabilities, successors), verifies one mode per activity, total non-renewable use <= availability, precedences and per-period renewable usage, then reports makespan; first confirm it accepts a posted BKS schedule and reproduces its value. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://solutionsupdate.ugent.be/mrcpsp>

## Sources

- <http://solutionsupdate.ugent.be/mrcpsp>
- <http://solutionsupdate.ugent.be/dataset/boctor100>
- <http://solutionsupdate.ugent.be/dataset/mmplus>
- <https://github.com/MarioVanhoucke/MMLIB-Multi-Mode-Resource-Constrained-Project-Library>
- <https://www.projectmanagement.ugent.be/research/data>
- <https://www.projectmanagement.ugent.be/research/project_scheduling/multi_mode>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- CP-SAT with optional interval variables per mode (one present per activity) and cumulative plus non-renewable knapsack constraints; seed with a mode assignment from a fast non-renewable-feasibility MIP.
- Two-level search: an outer mode-assignment local search (flip one activity's mode, keep non-renewable feasibility) and an inner single-mode RCPSP solved by a fast schedule generation scheme with forward-backward improvement.
- Cloud-computing import: multi-mode activities are like jobs with alternative VM shapes; bin-packing heuristics for VM placement (best-fit decreasing on resource vectors) give good initial mode choices.
- Statistics import: fit a simple regression of makespan on instance indicators (provided in the Excel) to pick the instances whose current UB is most anomalous relative to similar instances; attack those first.
- Large-neighbourhood search that frees all activities in a time window, including their modes, and re-solves exactly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Non-renewable resources: a schedule that respects renewable capacities but overspends a non-renewable budget is infeasible; many heuristics repair this with penalties and can output infeasible incumbents.
- MMLIB+ instances use different numbers of modes and resources than MMLIB50/100; parse each file's header rather than hard-coding. Boctor files (.prb) have their own format and no non-renewable resources.
- The release Excel lags the live site (2026-10-28: 82 vs 54 open MMLIB50, 52 vs 33 open Boctor100); an instance open in the Excel may already be closed or improved on SolutionsUpdate. Compare against the dataset page's BKS CSV, re-fetched before claiming.
- The summary table and the dataset pages can differ by one (MM50 54 vs 55, MM100 114 vs 115 on 2026-10-28); the per-instance CSV value is what counts.
- PSPLIB multi-mode sets (J10-J30) and Boctor50 are all closed; they are not targets.
- Lower bounds are not mechanically checkable here; only UB improvements or LB-matching schedules count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/mmlib-multimode-rcpsp-ub.md
```

Already set up? Say `run V3R1T4S on mmlib-multimode-rcpsp-ub`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mmlib-multimode-rcpsp-ub`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
