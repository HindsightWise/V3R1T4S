# IWLS 2026 Programming Contest: an AIG off the virtual-best delay/area Pareto frontier for one of the 100 released truth tables (ex200-ex299)

⚡ **Algorithms** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours per benchmark (ABC/mockturtle/SAT-based resynthesis on 16-input-scale truth tables); exhaustive verification takes seconds · open as of 2026-10-30

## The problem

The IWLS 2026 Programming Contest (chairs Alan Mishchenko, UC Berkeley, and Attila Jurecska, Siemens EDA) asked for and-inverter graphs (AIGs) for 100 completely specified multi-output Boolean functions given as truth tables ex200..ex299 (ex200, for instance, has 16 inputs and 16 outputs). Unlike earlier years it scored a delay/area trade-off: area = number of two-input AND nodes, delay = AND logic levels (ABC print_stats 'and' and 'lev'). Scoring finished in May 2026 (scoring report dated 2026-05-24). The organisers released the truth tables, the 10,553 submitted AIGs from 12 teams (10,537 functionally correct), and, per benchmark, the virtual-best-solver (VBS) Pareto frontier formed from the union of all teams' Pareto points (results/pareto_tables, VBS AIGs in virtual_best_solver.tar.gz). Examples of VBS frontier end points (level, ANDs): ex200 (13, 7617) ... (70, 1055); ex211 (8, 251) ... (26, 154); ex265 (6, 48) ... (13, 37); ex299 (17, 153970) ... (116, 15410). Top three: JetBrains / NUP / EPFL / MBZUAI, NTHU / CUHK, Freiburg. The contest is over and the data are public, so the frontier is a fixed record table; OPEN as of 2026-10-30 (last commit 2026-06-20, no post-contest frontier updates found). The contest description says a few benchmarks may duplicate functions from earlier IWLS contests, whose released best circuits also count as bars. Cirbo (SPbSAT/cirbo, release 1.1.0 of 2026-10-13) ships ex215 circuits for metaheuristic experiments.

## What counts as a win

Success means a binary AIGER file for some benchmark exNNN (200 <= NNN <= 299) that (1) is functionally equivalent to exNNN.truth on all input vectors, and (2) has a (level L, AND count A) point that is STRICTLY BETTER than the VBS frontier in results/pareto_tables/exNNN.txt: A is strictly smaller than the minimum VBS area over all listed levels <= L (direction: min area at a given delay; if no VBS point has level <= L, any correct AIG at level L is a new frontier point). Equivalently the point is neither dominated by nor equal to any VBS point. L and A are recomputed by the verifier (AND nodes; levels = longest input-to-output path counted in AND nodes, inverters free), never taken from the filename. The point must also not be dominated by or equal to any other published AIG for the same function known at claim time: post-contest papers, the Cirbo repository, contest-repo updates, and released circuits of earlier IWLS contests whose truth table is identical. Each benchmark is a separate cell; one non-dominated point is a full win.

## Partial wins

- **p1:** A fully automatic, released synthesis script that, run from exNNN.truth alone (no submitted or VBS circuits as input), produces a functionally equivalent AIG whose AND count at some level L is at most 1.01 times the minimum VBS area over levels <= L, for at least 10 of the 100 benchmarks; the skeptic re-runs the script and checks every output.

## How a win is checked

Parse the AIGER file with an independent reader, simulate all 2^n input vectors bit-parallel and compare every output with the truth-table columns of exNNN.truth (cross-check with ABC: read_truth -xf exNNN.truth; st; &get; &cec -t cand.aig, as in the contest's evaluation_notes.md). Recompute AND count and AND-level depth (ABC read_aiger; print_stats). Compare (L, A) against every row of results/pareto_tables/exNNN.txt and any newer published point.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/alanminko/iwls2026-ls-contest/tree/main/results/pareto_tables>

## Sources

- <https://github.com/alanminko/iwls2026-ls-contest>
- <https://raw.githubusercontent.com/alanminko/iwls2026-ls-contest/main/README.md>
- <https://github.com/alanminko/iwls2026-ls-contest/tree/main/results/pareto_tables>
- <https://raw.githubusercontent.com/alanminko/iwls2026-ls-contest/main/results/evaluation_notes.md>
- <https://github.com/SPbSAT/cirbo>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the VBS AIGs (virtual_best_solver.tar.gz) and apply resubstitution, SAT-based window resynthesis and depth-aware rewriting at a fixed level budget.
- Target benchmarks whose frontier has few points or large area jumps between adjacent levels (e.g. ex210, ex275, ex285-ex294).
- Balance a minimum-area circuit to a lower level and re-minimise area under that level constraint.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Levels count AND nodes only; inverters are free. Use the verifier's recomputed level, not the filename's LLL field.
- A point equal to a VBS point, or dominated by any VBS point at a lower level, is not a record: the comparison is against the minimum area over all levels <= L.
- Benchmark descriptions are undisclosed and may be reused in future IWLS contests; publish circuits openly but do not assume a benchmark's identity.
- Check the repository and recent papers for post-contest improvements before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/iwls2026-aig-delay-area-pareto.md
```

Already set up? Say `run V3R1T4S on iwls2026-aig-delay-area-pareto`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `iwls2026-aig-delay-area-pareto`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
