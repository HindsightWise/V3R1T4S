# ARPA-E GO Competition Challenge 1 (continuous SCOPF): beat the best Final Event score on a public synthetic scenario

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (networks of a few hundred to tens of thousands of buses; contingency evaluation dominates) · open as of 2026-10-30

## The problem

Challenge 1 of the ARPA-E GO Competition (2018-2019) is the single-period security-constrained AC optimal power flow with generator response after contingencies: choose a base-case operating point (code 1, under a strict wall-clock limit) and post-contingency responses (code 2) minimising generation cost plus soft-constraint penalties. The Final Event (late 2019) scored 25 teams and the ARPA-E Benchmark on 352 scenarios in each of Division 1 (real-time data) and Division 2 (offline data), mostly 20 per network. The results workbook C1_E4_scenario_results_20200106.xlsx on OEDI (DOI 10.25984/2437761) lists, per scenario, every entrant's score and a 'best score' / 'by team' column: Division 1's 352 rows are led by Lawrence Livermore National Laboratory (226 best scores), BAT (43), Lehigh University (31), Georgia Tech (Sun) (25) and gravityx (21); Division 2's 352 rows by LLNL (182), Lehigh (110) and BAT (41). The synthetic scenarios (340 real-time and 340 offline, 17 networks) are public; the industry networks 40, 41 and 42 are not. The official Python evaluator is GOCompetition/Evaluation. The bests were obtained under event time limits and no later best-known table exists. Example: Network_02R-173 scenario 1, best score 280,109.889140951 (BAT).

## What counts as a win

Solution files (solution1.txt and solution2.txt in the Challenge 1 format) for one scenario row of the 'Division 1' or 'Division 2' tab of https://data.openei.org/files/6153/C1_E4_scenario_results_20200106.xlsx whose data (case.raw, case.rop, case.con, case.inl) is in Challenge_1_Final_Event_Real-Time_Synthetic_Scenarios.zip (Division 1) or Challenge_1_Final_Event_Offline_Synthetic_Scenarios.zip (Division 2) on https://data.openei.org/submissions/6153, that the evaluator https://github.com/GOCompetition/Evaluation (evaluation.py) scores with zero hard-constraint infeasibility and an objective strictly lower than the row's 'best score' cell by more than 1e-6 * |best|. As a smoke test the verifier first runs the evaluator on the repository's examples/case2 (sol1.txt, sol2.txt), since no team solutions are published.

## Partial wins

- **p1:** A strict improvement, by the full-win rule (evaluator-feasible, objective lower by more than 1e-6 relative), on a synthetic Trial Event 2 or 3 scenario whose data is in Challenge_1_Trial_Event_2_Used_Scenarios.zip or Challenge_1_Trial_Event_3_Scenarios.zip on OEDI 6153. The bar is the lowest team 'Score' cell for that network and scenario across the 'Division 1' to 'Division 4' tabs, and any team revision tab, of Challenge_1_Event_2_Results_Summary.xlsx or Challenge_1_Event_3_Results_Summary.xlsx; these workbooks have no 'best score' column.
- **p2:** Evaluator-feasible solutions within 1e-4 relative of the best score on 10 Final Event scenarios from at least 3 networks, from one documented pipeline.

## How a win is checked

Download the synthetic zip and the results workbook (sha256 cff10169df2cefa8d25447c6deb495ba4973e0f7038a890e363f5b5b355cf086 on 2026-10-30) from OEDI submission 6153; clone GOCompetition/Evaluation, run evaluation.py on the scenario files and the claimed solution pair in a clean venv, read infeasibility and objective; read the 'best score' cell with openpyxl (data_only=True). Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://data.openei.org/files/6153/C1_E4_scenario_results_20200106.xlsx>

## Sources

- <https://data.openei.org/submissions/6153>
- <https://data.openei.org/files/6153/C1_E4_scenario_results_20200106.xlsx>
- <https://data.openei.org/files/6153/Challenge_1_Problem_Formulation.pdf>
- <https://data.openei.org/files/6153/Challenge_1_Scoring.pdf>
- <https://github.com/GOCompetition/Evaluation>
- <https://doi.org/10.25984/2437761>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Minimisation: lower is better here, unlike Challenges 2 and 3.
- Some workbook rows are industry networks or geomean summary rows ('Network 02 Geomean'); only rows whose scenario folder is in the public synthetic zips count.
- Teams whose solutions were infeasible were scored with a slack solution ('# slacks', 'slack score' columns); the 'best score' column already takes the minimum over team scores.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/go1-final-event-scopf-best-scores.md
```

Already set up? Say `run V3R1T4S on go1-final-event-scopf-best-scores`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `go1-final-event-scopf-best-scores`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
