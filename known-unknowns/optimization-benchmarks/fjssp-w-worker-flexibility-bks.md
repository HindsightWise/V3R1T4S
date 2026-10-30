# Flexible job shop with worker flexibility (FJSSP-W benchmark, 402 instances): lower a best known makespan

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

FJSSP-W extends the flexible job shop: each operation needs one eligible machine and one eligible worker at the same time, its duration depends on the (machine, worker) pair, and machines and workers each process one operation at a time; minimise makespan. The benchmarking environment of the Josef Ressel Centre (jrc-rodec/FJSSP-W-Benchmarking; Hutter, Steinberger and Hellwig, arXiv 2501.16159, revised May 2026) publishes 402 FJSSP-W instances derived from the classic FJSP sets (Behnke-Geiger, Brandimarte, Chambers-Barnes, Dauzere-Peres-Paulli, Fattahi, Hurink, Kacem) and a best_known.csv of UB and LB per instance, last committed 2026-04-27. The README states the values come from 20-minute runs of state-of-the-art solvers and the genetic algorithm of Hutter, Hellwig and Steinberger (CEC 2024). On 2026-10-30, 371 of the 402 instances have UB > LB, with a median gap of about 37% of the UB. Find a feasible FJSSP-W schedule with makespan strictly below the listed UB for any instance.

## What counts as a win

For one of the 402 instances in instances/Example_Instances_FJSSP-WF, an assignment of each operation to an eligible (machine, worker) pair with start times such that an independent checker written from the repository's instance format confirms job precedence, machine and worker no-overlap and the pair-specific durations, and computes a makespan strictly below that instance's UB in https://raw.githubusercontent.com/jrc-rodec/FJSSP-W-Benchmarking/main/instances/InstanceData/FJSSP-W/best_known.csv, re-fetched live immediately before claiming, with the instance-to-row mapping (e.g. Behnke10.fjs <-> behnkegeiger10) confirmed from the repository's data.csv. Nothing is submitted by the agent.

## Partial wins

- **p1:** A strictly better makespan on any Brandimarte- or Behnke-derived FJSSP-W instance with UB > LB, verified by the checker.
- **p2:** Strict improvements on at least 10 distinct FJSSP-W instances, each verified by the checker.
- **p3:** A strictly better makespan on any Hurink-, Dauzere-Peres-Paulli- or Chambers-Barnes-derived FJSSP-W instance with UB > LB, verified by the checker.

## How a win is checked

Instance file https://raw.githubusercontent.com/jrc-rodec/FJSSP-W-Benchmarking/main/instances/Example_Instances_FJSSP-WF/ < name > .fjs: first line 'jobs machines workers'; per job the number of operations, then per operation the number of machine choices and, for each machine, the number of worker choices and (worker, duration) pairs (1-based). A ~80-line Python checker validates and recomputes the makespan; test it on a hand-built schedule for a small Kacem-derived instance. Compare with best_known.csv (semicolon-separated Instance;UB;LB). Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/jrc-rodec/FJSSP-W-Benchmarking/main/instances/InstanceData/FJSSP-W/best_known.csv>

## Sources

- <https://github.com/jrc-rodec/FJSSP-W-Benchmarking>
- <https://raw.githubusercontent.com/jrc-rodec/FJSSP-W-Benchmarking/main/instances/InstanceData/FJSSP-W/best_known.csv>
- <https://raw.githubusercontent.com/jrc-rodec/FJSSP-W-Benchmarking/main/instances/InstanceData/FJSSP-W/data.csv>
- <https://arxiv.org/abs/2501.16159>
- <https://doi.org/10.1109/CEC60901.2024.10611934>
- <https://github.com/ScheduleOpt/optalcp-benchmarks/tree/main/benchmarks/flexible-jobshop-w>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- CP-SAT with optional intervals per (operation, machine, worker) triple, no-overlap per machine and per worker, run longer than 20 minutes with 10 workers; the reference values are short-run, so long runs should already improve many.
- Decompose: fix machine choice from the FJSP best schedule of the parent instance, then assign workers by a min-cost matching per time slice and repair.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The FJSSP-W instances are randomly generated from FJSP instances; regenerating them with the repository's translator gives different instances that are not comparable to best_known.csv.
- Names differ between files (Behnke10.fjs) and the CSV (behnkegeiger10); a claim on the wrong row is void.
- The CSV header was 'Instance;LB;UB' with the UB in the first column until 2026-04-27, when it was corrected to 'Instance;UB;LB'. Read columns by header and check UB >= LB on every row.
- Some UB and LB values carry floating-point noise (e.g. fattahi12 UB 414.99999995839994 means 415, hurinkrdata1 LB 42.99999999999994 means 43); durations are integers, so round each value to the nearest integer when within 1e-3 before comparing, and a claim must be at least 1 below the rounded UB.
- Some listed LBs are trivial (8 open rows have LB 0), so the gap overstates how much room there is; only UB improvements count.
- This table is newer and less studied than FJSPLib; UB improvements are expected to be easier, so tractability is high but each single win is modest.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/fjssp-w-worker-flexibility-bks.md
```

Already set up? Say `run V3R1T4S on fjssp-w-worker-flexibility-bks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fjssp-w-worker-flexibility-bks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
