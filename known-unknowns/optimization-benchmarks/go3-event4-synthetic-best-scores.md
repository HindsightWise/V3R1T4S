# ARPA-E GO Competition Challenge 3 (multi-period AC unit commitment): beat the best Event 4 score on a public synthetic scenario

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (73- and 617-bus scenarios; the 4,000- to 23,643-bus ones need laptop-days and 16+ GB RAM) · open as of 2026-10-30

## The problem

Challenge 3 of the ARPA-E Grid Optimization (GO) Competition (2022-2023) posed a multi-period security-constrained AC unit commitment and market-clearing problem: commit and dispatch generators, loads and storage over 1-8 hour horizons with AC power flow, reserves, ramping, contingencies and optional line switching, maximising market surplus z. The organisers (Jesse Holzer, Stephen Elbert, Arun Veeramany and colleagues at PNNL, with Richard O'Neill, Hans Mittelmann, Carleton Coffrin and others) released the 591 synthetic Event 4 scenarios (73 to 23,643 buses; industry scenarios withheld), the official evaluator C3DataUtilities, and the full Event 4 results workbook E4LB_Master_20240506.xlsx on OEDI (DOI 10.25984/2426334, May 2024). Its per-network tabs (73, 617, 1576, 2000, 4224, 6049, 6717, 8316, 23643) give the Best Score and Best Team for every (division, model, scenario, switching) row; the 'data' tab lists every team's objective and feasibility. Best scores came from YongOptimization (most rows), GravityX, TIM-GO, The Blackouts, GOT-BSI-OPF and Artelys_Columbia, with a few rows from Occams razor, Gatorgar, LLGoMax and the ARPA-e Benchmark, all under event wall-clock limits of 600 s (D1), 7,200 s (D2) and 14,400 s (D3). Nobody has published a later best-known table, so offline computation can beat these scores; Brun, Lee, Lauinger, Chen and Sun (arXiv 2505.06211, 2025) report second-order-cone dual bounds and a 1.33% average gap for their own solutions on Challenge 3 cases, but no per-scenario objectives above the Event 4 bests. On C3E4N23643 D2 and D3 scenario 4 every team scored 0: the best feasible objectives listed are -690,443,352.45 (ARPA-e Benchmark, D2) and -2,623,296,182.38 (quasiGrad, D3).

## What counts as a win

A solution JSON for one public synthetic Event 4 scenario (a scenario_ < n > .json in one of the C3E4N*_20231002.zip files on https://data.openei.org/submissions/5997; the 6708-bus industry network is excluded) that the C3DataUtilities evaluator (https://github.com/GOCompetition/C3DataUtilities, main branch; check_data.py --problem scenario_ < n > .json --solution sol.json, with the four *_switch_*_allowed parameters set to false when the row's SW is 0) reports as feasible, with objective z strictly greater than both the Best Score in that row of the network's tab of E4LB_Master_20240506.xlsx and the largest objective of any row with feas = 1 for the same model, scenario and SW in the 'data' tab, by more than 1e-6 * max(1, |best|). Division matters only through the scenario file; time limits do not apply offline and must be reported. The evaluator must first reproduce the objective of the scenario_ < n > .json.pop_solution.json shipped with that scenario.

## Partial wins

- **p1:** An evaluator-feasible solution for C3E4N23643D2 or C3E4N23643D3 scenario 4 whose objective is greater than every feasible team objective listed for it in the 'data' tab (-690,443,352.45 for D2, -2,623,296,182.38 for D3).
- **p2:** A strict improvement, by the full-win rule, on a scenario of an earlier event (E1, E2.1 or E3.1 on the same OEDI page) over the best team objective in that event's results workbook (E1LB, E2LB or E3LB master xlsx). The Sandbox sets have no results workbook and do not count.
- **p3:** An evaluator-feasible solution within 1e-4 relative of the Best Score on 10 different Event 4 scenarios of at least 617 buses, produced by one documented pipeline (reproduction of the competition state).

## How a win is checked

Download the scenario zip and E4LB_Master_20240506.xlsx (sha256 8ae933e17368428ffdb822b3fd3b28ea2969b65a8446e4d1f35e7f8b45654ff1 on 2026-10-30) from OEDI submission 5997. pip-install C3DataUtilities and GO-3-data-model in a clean venv, run check_data.py on the shipped pop_solution.json to confirm the evaluator works, then on the claimed solution with the right switching parameters, and read feasibility and z from its summary output. Read the Best Score cell with openpyxl (data_only=True) and the 'data' tab rows for that scenario. Minutes to an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://data.openei.org/submissions/5997>

## Sources

- <https://data.openei.org/submissions/5997>
- <https://data.openei.org/files/5997/E4LB_Master_20240506.xlsx>
- <https://data.openei.org/files/5997/Challenge3_Problem_Formulation_20240122.pdf>
- <https://data.openei.org/files/5997/C3E4N00073_20231002.zip>
- <https://github.com/GOCompetition/C3DataUtilities>
- <https://arxiv.org/abs/2411.12033>
- <https://doi.org/10.25984/2426334>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the shipped pop_solution.json and the formulation PDF; the 73- and 617-bus D1 scenarios had only 600 s in the event, so a slow exact MIP (commitment) plus AC-OPF polishing per period can plausibly beat them.
- Decompose: solve a DC or copper-plate unit commitment MILP with HiGHS or SCIP, fix commitments, then solve the multi-period AC dispatch with Ipopt, and repair with the evaluator's own penalty terms in mind.
- Rows where the best and second-best teams differ by more than 0.1% signal slack.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Score is not objective: infeasible or negative-objective solutions were scored 0, so the Best Score cell can be 0 while the real bar (feasible objective) is negative; compare with both, as the criterion says.
- Switching: SW = 1 rows allow line and transformer switching, SW = 0 rows forbid it; evaluating an SW = 0 claim with default parameters lets switching in.
- Use the 20231002 Event 4 files; Event 2 2000- and 6717-bus files were replaced (C3E2.1) and the old ones fail the data checker.
- gocompetition.energy.gov served an expired TLS certificate on 2026-10-30; use OEDI and GitHub.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/go3-event4-synthetic-best-scores.md
```

Already set up? Say `run V3R1T4S on go3-event4-synthetic-best-scores`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `go3-event4-synthetic-best-scores`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
