# ARPA-E GO Competition Challenge 2 (SCOPF with switching): beat a Monarch of the Mountain best-known objective

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (617- to 31,777-bus networks with hundreds of contingencies; 16+ GB RAM for the largest) · open as of 2026-10-30

## The problem

Challenge 2 of the ARPA-E GO Competition (2020-2021) is a single-period security-constrained AC optimal power flow with transformer taps, phase shifters, switched shunts, price-responsive loads, ramp limits, fast-start unit commitment and optional line switching, maximising economic surplus over the base case and all post-contingency cases. After the Final Event, ARPA-E ran 'Monarch of the Mountain' (MotM, 2022), inviting anyone to improve the best known solutions of the 84 public synthetic Final Event scenarios (16 networks, 617 to 31,777 buses). The results workbook Challenge_2_Monarch_of_the_Mountain_Results.xlsx on OEDI (DOI 10.25984/2448433) records, in tab 'Ch2', the best Challenge 2 objective and the current best MotM objective per scenario; the last improvements are dated 26 Oct 2022. GravityX (Hassan Hijazi and colleagues) holds 74 of the 84 records, GOT-BSI-OPF 8 and Gordian Knot 2. Every record improves on the Final Event best, which GravityX held on 59 scenarios, GO-SNIP on 10, NU_Columbia_Artelys on 8, magos and Monday Mornings on 3 each and GMI-GO on 1. MotM is closed and no later table exists. Example records: C2FEN00617 scenario 5, 1,350,775.92643542 (GravityX); C2FEN03970 scenario 23, 257,435.110836647 (GOT-BSI-OPF); C2FEN31777 scenario 11, 129,394,052.138728 (GravityX).

## What counts as a win

Solution files (solution_BASECASE.txt and one solution_ < label > .txt per contingency, in the Challenge 2 output format) for one scenario listed in tab 'Ch2' of https://data.openei.org/files/6197/Challenge_2_Monarch_of_the_Mountain_Results.xlsx, using that scenario's case.raw, case.json and case.con from 'Challenge_2 _Final_Event_4_Synthetic_Data_Scenarios.zip' on https://data.openei.org/submissions/6197, that the C2DataUtilities evaluator (https://github.com/GOCompetition/C2DataUtilities, data_utilities.evaluation, line and transformer switching allowed) reports as feasible (no hard-constraint violation beyond its tolerances), with objective strictly greater than that scenario's 'Current Best data Objective' cell by more than 1e-7 * |best| (consecutive records differ by as little as 1.3e-6 relative). As a smoke test the verifier first runs the evaluator on the infeasibility solution that the repository's construct_infeasibility_solution builds for the same scenario; it must run to completion and report feasibility and an objective.

## Partial wins

- **p1:** An evaluator-feasible solution for a MotM scenario whose objective beats that scenario's 'Best Ch2 Objective' (the original competition best) but not the MotM record.
- **p2:** A documented pipeline that reaches within 1e-4 relative of the MotM record on 5 scenarios of different networks, each evaluator-feasible.

## How a win is checked

Download the Final Event synthetic zip (71.7 MB) and the MotM workbook (sha256 db04c3e5e68d27537f8d37d01c00eef4cc55659cc6a18f6f53036a972b04c579 on 2026-10-30) from OEDI submission 6197; pip-install C2DataUtilities in a clean venv; run its evaluation (switching allowed) on the claimed solution_BASECASE.txt and solution_ < label > .txt files against the scenario's case.raw, case.json and case.con; read feasibility and objective; read the record with openpyxl (data_only=True). Minutes to hours for the largest networks.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://data.openei.org/files/6197/Challenge_2_Monarch_of_the_Mountain_Results.xlsx>

## Sources

- <https://data.openei.org/submissions/6197>
- <https://data.openei.org/files/6197/Challenge_2_Monarch_of_the_Mountain_Results.xlsx>
- <https://data.openei.org/files/6197/Challenge_2_Final_Event_Results.xlsx>
- <https://data.openei.org/files/6197/Challenge_2_Problem_Formulation.pdf>
- <https://github.com/GOCompetition/C2DataUtilities>
- <https://doi.org/10.25984/2448433>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The records are near-converged on base-case dispatch; remaining gains are likely in discrete choices (switching, taps, shunts, fast-start commitment) and in contingency responses, so local search over discrete settings with an AC-OPF inner solve is the natural attack.
- Small-relative-gap records (617, 2020 buses) are cheapest to attack; start from the posted best solution if the MotM submission archives are reachable, else from GravityX-style Ipopt solves.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The objective depends on the contingency solutions (solution2); a better base case with poor contingency responses can lower the score.
- MotM rows are the 84 public synthetic scenarios; industry scenarios were never released.
- The 'Previous' and 'old' tabs hold superseded records; use 'Ch2' column 'Current Best data Objective'.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/go2-monarch-of-the-mountain-scopf.md
```

Already set up? Say `run V3R1T4S on go2-monarch-of-the-mountain-scopf`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `go2-monarch-of-the-mountain-scopf`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
