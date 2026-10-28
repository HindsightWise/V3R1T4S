# RCPLIB (Vanhoucke-Coelho) RG300 and DC2 resource-constrained project scheduling: shorter makespan for an open instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Mario Vanhoucke and Jose Coelho (Ghent University) maintain RCPLIB and the SolutionsUpdate site, which tracks open instances for single-mode RCPSP datasets beyond PSPLIB. On 2026-10-28 the live table (headed October 2026) reports 334 open instances out of 480 in RG300 (300 activities, Debels and Vanhoucke 2007; average gap 28.2%; newer contributions coded 4C, 4Cb and ZV) and 140 of 720 in DC2 (Vanhoucke 2010). The current RCPLIB release (v2.4, published 28 January 2026; README updated March 2026) gives per-instance best lower bound (LB-lit) and best upper bound (UB-lit). Find a feasible schedule with makespan strictly below UB-lit for an instance with LB-lit < UB-lit.

## What counts as a win

A start-time vector for one RG300 or DC2 instance (original-version Patterson .rcp file from the latest RCPLIB release) that is open (LB < UB) on its SolutionsUpdate dataset page, that an independent checker confirms satisfies all finish-to-start precedences and all renewable resource capacities at every time unit, with makespan strictly below both that instance's UB-lit in the latest RCPLIB release Excel and its value in the best-known-solution CSV linked from http://solutionsupdate.ugent.be/dataset/RG300 or http://solutionsupdate.ugent.be/dataset/DC2 (e.g. RG300_3_BKS.csv), all re-fetched live immediately before claiming.

## Partial wins

- **rg300-improve-any:** Strict UB improvement on any open RG300 instance, verified by the checker.
- **dc2-improve-any:** Strict UB improvement on any open DC2 instance, verified by the checker.
- **rcpsp-close-by-lb:** Closing an open instance by finding a schedule whose makespan equals LB-lit (proving optimality without a new bound), verified by the checker.

## How a win is checked

Download the release zip (https://github.com/MarioVanhoucke/RCPLIB-Resource-Constrained-Project-Library/releases/latest, 86 MB; contains RG/RG300.zip, DC/DC2.zip and 'RCPLIB (Parameters and BKS).xlsx', whose RG300 sheet has LB-lit in column BG and UB-lit in column BH: 347 rows with LB < UB in v2.4). Current per-instance values: the *_BKS.csv linked from the SolutionsUpdate dataset pages (columns ID;Type;Value;Time;Solution; RG300 334 open and DC2 140 open on 2026-10-28, so the site is newer than the Excel). A 40-line checker parses the Patterson file (activities, durations, renewable demands, successors), verifies precedence and per-period resource usage, and reports makespan; first confirm it accepts a posted BKS schedule with the posted value. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://solutionsupdate.ugent.be/rcpsp>

## Sources

- <http://solutionsupdate.ugent.be/rcpsp>
- <http://solutionsupdate.ugent.be/dataset/RG300>
- <http://solutionsupdate.ugent.be/dataset/DC2>
- <http://solutionsupdate.ugent.be/introduction>
- <https://www.projectmanagement.ugent.be/research/data>
- <https://github.com/MarioVanhoucke/RCPLIB-Resource-Constrained-Project-Library>
- <https://github.com/MarioVanhoucke/RCPLIB-Resource-Constrained-Project-Library/releases/download/v2.4/RCPLIBv2.4.zip>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run open CP-SAT (OR-Tools) with interval variables and cumulative constraints, warm-started from a good serial-schedule-generation-scheme solution; CP-SAT's LNS is strong on 300-activity RCPSP and the RG300 average gap of 28.2% suggests large slack.
- Forward-backward improvement (justification) plus decomposition-based GA in the spirit of Debels and Vanhoucke, but with much longer runs than the original papers' schedule limits.
- Signal processing import: treat the resource profile as a time series and use convolution-based 'peak shaving' to choose which activities to delay, as in power-grid load levelling.
- Sequence-to-schedule learning import from compiler instruction scheduling: list-scheduling priority rules learned per instance (genetic programming of priority rules, as in Luo, Vanhoucke, Coelho and Guo 2022) to seed CP search.
- Use the 'lowRU/highRD' and 'keepOPT' equivalent versions supplied in the release to search on the reduced instance, then map back and verify on the original.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Per-instance values in the Excel lag the live site (347 open in v2.4 vs 334 open live on 2026-10-28): a 'win' against UB-lit may already be matched by a newer upload; compare against the dataset page's BKS CSV before claiming.
- Instance versions: each instance comes in original, lowRU, highRD and keepOPT versions; records refer to the original version, and a makespan on a transformed version is a win only after mapping back and re-checking on the original.
- PSPLIB J120 is a separate bank target; J60/J90/J120 rows on the same page are not part of this target.
- Patterson format details: the dummy start and end activities have zero duration; resource availabilities are on the line after the activity count; misreading successor lists silently drops precedences.
- Do not count lower-bound improvements; they are not mechanically checkable from a saved object.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/rcplib-rg300-dc2-rcpsp-ub.md
```

Already set up? Say `run V3R1T4S on rcplib-rg300-dc2-rcpsp-ub`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rcplib-rg300-dc2-rcpsp-ub`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
