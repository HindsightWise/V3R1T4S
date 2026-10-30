# IEA Wind Task 37 case study 1: a feasible 16-, 36- or 64-turbine circular-farm layout with higher AEP than every published or posted layout

🛠️ **Engineering and chips** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (one AEP evaluation is about 1 ms; multistart gradient or large-neighbourhood search) · open as of 2026-10-30

## The problem

Wind farm layout optimisation (WFLO) case study 1 is from IEA Wind Task 37 (Baker, Stanley, Thomas, Ning and Dykes, AIAA SciTech 2019-0540, BYU FLOW Lab and NREL). Turbines are IEA37 3.35 MW machines (D = 130 m). The wind speed is a constant 9.8 m/s over a 16-bin wind rose, and the wake model is the simplified Bastankhah Gaussian (k = 0.0324555, CT = 8/9) combined by root sum of squares. All hubs must lie within the boundary radius (1300, 2000 or 3000 m for 16, 36 or 64 turbines) and every pair must be at least 2D = 260 m apart. The results folder (IEAWindSystems/iea37-wflo-casestudies; byuflowlab copy archived) posts 36 layouts from 12 participants. Re-checked 2026-10-30 with an independent evaluator that reproduces all 36 posted AEPs. Best values in MWh: - 16 turbines: participant 12 posted 421561.897, 3.518 m outside the boundary (421451.07 once projected inside). Next: DPCRO-SL 419935.7905 (arXiv 2212.00742) and SNOPT+WEC 418924.4064 (Thomas and Ning, participant 4; its file is 4e-12 m outside). An open V3R1T4S claim (PR #578, unreviewed) reports a strictly feasible 424131.9503; it reproduces in an independent evaluator. - 36 turbines: participant 12 posted 882383.304, 4.9 mm outside (882382.78 once projected). Next: Perez-Rua, Stolpe and Cutululis (WES 2023), about 865 GWh; SNOPT+WEC 863676.299 (file 4e-11 m outside). - 64 turbines: participant 12 posted 1526474.802, 4.1 mm outside (1526474.68 once projected). Next: SNOPT+WEC 1513311.194 (file 1.4e-10 m outside). Valotta Rodrigues et al. (WES 2024) use a modified setup and report only normalised values. No later published absolute record was found.

## What counts as a win

A layout for the 16-, 36- or 64-turbine scenario with every hub at distance at most R from (0,0) and every pair at least 260 m apart, both checked with no tolerance in double precision. Its AEP from the official iea37-aepcalc.py model (16-bin rose, constant 9.8 m/s, iea37-335mw.yaml) must be STRICTLY GREATER (direction: max) by at least 0.01 MWh than the posted record, used as posted even though it lies outside the boundary: 421561.8972 (16), 882383.3040 (36) or 1526474.8025 (64), and also strictly greater than every CONFIRMED V3R1T4S known-known for the same scenario at claim time. Re-check the known-knowns and open claims (PR #578 reports 424131.9503 at 16) immediately before claiming; a claim must state which of them it beats.

## Partial wins

- **p1:** A feasible 36- or 64-turbine layout with AEP strictly above the best posted non-participant-12 value (SNOPT+WEC: 863676.2993 for 36, 1513311.1936 for 64) by at least 1 MWh, such that under the minimum-total-distance one-to-one matching to the participant-12 layout at least one third of the turbines are more than 50 m from their partner (an independent topology).
- **p2:** A feasible 16-turbine layout strictly above 419935.7905 MWh (DPCRO-SL, the best published value by a non-participant) such that, under the minimum-total-distance one-to-one matching, at least 6 of its 16 turbines are more than 50 m from their partner in the participant-12 layout and in every V3R1T4S known-known or open-claim layout.
- **p3:** An independent standard-library re-implementation of the wake model that reproduces all 36 posted AEP values in iea37-cs1-results to within 1e-4 MWh, plus a feasibility report (boundary excess and minimum spacing, full precision) for every posted layout.

## How a win is checked

Parse xc and yc from the claimed YAML or JSON. Check max sqrt(x^2+y^2) <= R and min pairwise distance >= 260 m exactly. Compute AEP from the wake-model equations (wind-frame rotation by 270 - theta, sigma = k*dx + D/sqrt(8), deficit (1 - sqrt(1 - CT/(8 sigma^2/D^2))) exp(-0.5 (dy/sigma)^2), RSS combination, cubic power curve between 4 and 9.8 m/s, 8760 h). First reproduce par4-opt16 = 418924.406363 and par12-opt36 = 882383.304032. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/IEAWindSystems/iea37-wflo-casestudies/tree/master/cs1-2/iea37-cs1-results>

## Sources

- <https://github.com/byuflowlab/iea37-wflo-casestudies>
- <https://github.com/IEAWindSystems/iea37-wflo-casestudies/tree/master/cs1-2/iea37-cs1-results>
- <https://docs.nrel.gov/docs/fy19osti/72935.pdf>
- <https://arxiv.org/abs/2212.00742>
- <https://wes.copernicus.org/articles/8/1453/2023/>
- <https://wes.copernicus.org/articles/9/321/2024/>
- <https://github.com/elder-plinius/V3R1T4S/pull/578>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ruin-and-recreate large-neighbourhood search with SLSQP polishing found the 16-turbine claim. Apply it to 36 and 64 turbines from random starts, not from participant 12.
- Wake expansion continuation (inflate k, then anneal to 0.0324555) with exact gradients, many starts.
- Ring-structured parameterisations (boundary ring plus inner rings with rotational offsets) searched globally, then freed for local refinement.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Participant 12's files exceed the boundary (3.5 m at 16 turbines, millimetres at 36 and 64), and the SNOPT+WEC files by 1e-12 to 1e-10 m. A layout that only beats a record inside a tolerance is not a win.
- Boundary hubs must keep full float precision: rounding to 1e-3 m can push a hub outside R.
- The 16-bin wind rose is exploited by every record. No physical or site-realism claim is part of a win.
- Do not confuse case study 1 with case studies 3 and 4 (IEA 10 MW, polygon boundaries, a different wind rose).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/iea37-cs1-circular-wind-farm-layout.md
```

Already set up? Say `run V3R1T4S on iea37-cs1-circular-wind-farm-layout`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `iea37-cs1-circular-wind-farm-layout`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
