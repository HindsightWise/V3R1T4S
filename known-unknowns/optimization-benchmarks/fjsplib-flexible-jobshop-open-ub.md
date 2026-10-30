# Flexible job shop (FJSPLib: Brandimarte mk10, Dauzere-Peres-Paulli, Behnke-Geiger, Hurink): lower the best known makespan of an open instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

In the flexible job shop (FJSP) each operation of a job must run, in job order, on one machine chosen from an eligible set with a machine-dependent duration; minimise makespan. FJSPLib, maintained by ScheduleOpt (Diego Olivier Fernandez Pons and colleagues) at github.com/ScheduleOpt/benchmarks, keeps a best-known-bounds archive for 452 instances (solutions/bks.json, with a dated history per bound); the last commits are 2026-10-18 ('New bks, historical bks') and 2026-10-22. On 2026-10-30 the flexible and machine-independent families still open there (LB < UB) are: mk10 (189/193, UB Quintiq); 10 Dauzere-Peres-Paulli instances (e.g. dpp05a 2195/2199 and dpp06a 2164/2169 from Coupvent des Graviers, Kobrosly, Guettier and Cazenave 2025, and dpp07a 2216/2254 from Ding, Lu, Li, Shen, Xu and Glover 2019); 27 Behnke-Geiger instances (e.g. behnke7 117/124 and behnke16 392/412; UBs from OptalCP 2025, LBs from CP-SAT and DOFP2026a); and 15 Hurink instances (abz7/abz8/abz9 rdata, abz7/abz8 edata, abz8_vdata 506/507, la21-la26 and la28-la30 rdata). Earlier bounds come from Mastrolilli-Gambardella 2000, Quintiq's 2013 records, Puget's CP Optimizer 12.6 runs (2013) and Touko Ursin's 2026 issue reports. FJSPLib does not carry every published record. Zhang, Lu, Ding, Su, Li and Gao (AWLS, Engineering 50 (2025) 117-127, Table 7) report smaller makespans on eight of these instances: dpp07a 2249, dpp13a 2227, dpp16a 2224, abz8_rdata 534, abz9_rdata 535, la21_rdata 824, la23_rdata 830 and la30_rdata 1070. Find a feasible schedule for one of these open instances with makespan strictly below its best known upper bound, i.e. the smaller of the FJSPLib value and any published value.

## What counts as a win

A schedule for one instance whose bks.json entry (https://raw.githubusercontent.com/ScheduleOpt/benchmarks/main/flexible-jobshop/solutions/bks.json) has status 'open' and family mk, dpp, behnke, abz or la. Give it as one line per operation (job, operation index, machine, start time). An independent checker reads the FJSPLib text instance (flexible-jobshop/instances/fjsp/ < family folder > / < name > .txt; machines are numbered from 1, e.g. mk01.txt '2 1 5 3 4' = two eligible machines, machine 1 with duration 5 and machine 3 with duration 4). It confirms that every operation is assigned exactly once to an eligible machine with that machine's duration, that the operations of a job run in order without overlap, and that no machine runs two operations at once. The makespan must be strictly below the smallest of three values: (a) the instance's upper_bound in bks.json, (b) its README table value, and (c) any makespan published for that instance in the literature. Re-fetch (a) and (b) live immediately before claiming. Search 2024-2026 FJSP papers for (c); at minimum it includes the AWLS values of Zhang et al., Engineering 50 (2025), Table 7: dpp07a 2249, dpp13a 2227, dpp16a 2224, abz8_rdata 534, abz9_rdata 535, la21_rdata 824, la23_rdata 830 and la30_rdata 1070. yfjs and dafjs (flexible assembly) entries do not count. The agent submits nothing to the maintainers; reporting a new bound through an issue is the human's choice.

## Partial wins

- **p1:** A schedule meeting the success-criterion threshold on any open Behnke-Geiger instance (behnke7, behnke11-behnke20, behnke32, behnke34-behnke40, behnke51, behnke53-behnke59; behnke33 and behnke52 closed in October 2026; behnke29 is closed in bks.json), verified by the checker.
- **p2:** A schedule meeting the success-criterion threshold on any open Dauzere-Peres-Paulli instance (dpp05a, dpp06a, dpp07a, dpp10a-dpp13a, dpp16a-dpp18a) or on mk10, verified by the checker. For dpp07a, dpp13a and dpp16a the bar is the AWLS value (2249, 2227, 2224), not bks.json.
- **p3:** A schedule meeting the success-criterion threshold on any open Hurink instance (abz7, abz8, abz9, la21-la26 and la28-la30 rdata; abz7 and abz8 edata; abz8_vdata), verified by the checker. la27_rdata is closed. For abz8_rdata, abz9_rdata, la21_rdata, la23_rdata and la30_rdata the bar is the AWLS value (534, 535, 824, 830, 1070).

## How a win is checked

Fetch the instance text file from https://raw.githubusercontent.com/ScheduleOpt/benchmarks/main/flexible-jobshop/instances/fjsp/ < folder > / < name > .txt (first line 'jobs machines [avg]', then per job: number of operations, and per operation the number of eligible machines followed by (machine, duration) pairs with machines numbered from 1). Hurink files sit in HurinkJurischThole1994/ < edata|rdata|sdata|vdata > / < laNN|abzN > .txt. A ~60-line Python checker validates assignment, durations, job precedence and machine no-overlap and recomputes the makespan. Test it first on a schedule for a closed instance (e.g. mk01, proven 40). Then parse bks.json and the README row for the instance and compare. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/ScheduleOpt/benchmarks/main/flexible-jobshop/solutions/bks.json>

## Sources

- <https://github.com/ScheduleOpt/benchmarks/tree/main/flexible-jobshop>
- <https://scheduleopt.github.io/benchmarks/fjsplib>
- <https://raw.githubusercontent.com/ScheduleOpt/benchmarks/main/flexible-jobshop/solutions/bks.json>
- <https://raw.githubusercontent.com/ScheduleOpt/benchmarks/main/flexible-jobshop/README.md>
- <https://doi.org/10.1016/j.eng.2024.07.022>
- <https://arxiv.org/abs/2504.16106>
- <https://doi.org/10.1609/aaai.v33i01.33012262>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- CP with optional intervals per (operation, machine) plus failure-directed search seeded from a good heuristic schedule; OptalCP and CP-SAT set most 2025-2026 bounds, so long multi-worker runs with solution hints are the baseline to beat.
- Tabu search on the machine-assignment plus sequencing graph (Mastrolilli-Gambardella neighbourhoods, Ding et al. 2019 two-individual EA) run for hours, seeded with a CP-SAT incumbent.
- Large-neighbourhood search: free all operations in a time window or on a machine subset and re-solve exactly with CP-SAT.
- Gap-1 instances (abz8_vdata, la26/la28/la29_rdata) are best attacked as satisfiability searches for makespan UB-1.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- bks.json lags the literature. AWLS (Zhang et al., Engineering 2025, Table 7) beats it on dpp07a, dpp13a, dpp16a, abz8_rdata, abz9_rdata, la21_rdata, la23_rdata and la30_rdata, and that paper's own text and Tables 6 and 7 disagree on dpp16a (2228, 2226, 2224), so take the smallest, 2224. Search recent FJSP papers for the instance before claiming.
- bks.json and the README table can disagree (e.g. dafjs: README says 3 closed/27 open, bks.json lists 30 open); re-read both and use the smaller UB.
- The yfjs/dafjs flexible assembly bounds date from Birgin-Ferreira-Ronconi 2015 and may lag the literature; they are excluded from this target.
- Some UB dates in bks.json are placeholders (e.g. Quintiq values dated 2026-01-01); credit the solver field, not the date.
- Hurink instances exist in four variants (sdata/edata/rdata/vdata) with identical names; a claim must name the variant folder.
- Instances close quickly through GitHub issues: behnke33, behnke52, behnke60 and mk13 closed in October 2026 (issues #10-#13). Issue #8 (behnke29) is still open, but bks.json already lists behnke29 as closed at 117. Re-check the issue tracker as well as bks.json before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/fjsplib-flexible-jobshop-open-ub.md
```

Already set up? Say `run V3R1T4S on fjsplib-flexible-jobshop-open-ub`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fjsplib-flexible-jobshop-open-ub`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
