# Curriculum-based course timetabling (ITC-2007 track 3, UD2): beat the best known penalty on an open comp instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

Curriculum-based course timetabling (CB-CTT; Di Gaspero and Schaerf 2002; ITC-2007 track 3) assigns lectures of courses to periods and rooms subject to conflicts, availabilities and room occupancy, minimising soft penalties for room capacity, minimum working days, isolated curriculum lectures and room stability (formulation UD2, Bonutti, De Cesco, Di Gaspero and Schaerf 2012). OptHub (Intelligent Optimization Lab, University of Udine) is the live successor of the old CB-CTT portal and lists every uploaded solution per instance. On 2026-10-29 the best known UD2 values on the 21 ITC-2007 instances include comp03 64 (Kiefer; matched by Schaerf 2026-02-20), comp05 283 (Luciano Rigolin de Almeida, 2022), comp09 96 (Lu and Hao; matched by Schaerf 2026), comp12 289 (Andrea Schaerf, 2026-02-20), comp15 62 (Alexander Kiefer), comp18 61 (Kiefer), comp21 74 (Antony Phillips). Banbara et al. (teaspoon, Ann. Oper. Res. 2019, Table 4) proved optimality in UD2 for comp02, 04, 06, 07, 08, 10, 11, 13, 14, 16, 17, 19, 20, and comp01 = 5 is known optimal; the seven instances above have no published matching lower bound as far as the vetter found. Find a feasible timetable with a strictly lower UD2 penalty than the OptHub best for one of comp03, comp05, comp09, comp12, comp15, comp18 or comp21.

## What counts as a win

A solution file (one line per lecture: course room day period) for comp03, comp05, comp09, comp12, comp15, comp18 or comp21, that an independent checker written from the UD2 definition (Bonutti et al. 2012) reports as hard-feasible (all lectures scheduled, no conflicts, availabilities respected, at most one lecture per room and period) with UD2 penalty strictly below the 'Best solution' shown for that instance on https://opthub.uniud.it/problems/timetabling/edutt/ctt/cb-ctt-ud2, re-fetched live immediately before claiming. The checker must first reproduce the OptHub objective of the current best solution file (e.g. 289 for comp12_15.sol, 283 for comp05_melhorado_luciano_almeida.sol). Nothing is uploaded by the agent.

## Partial wins

- **p1:** A strictly better UD2 solution for comp05 (283) or comp12 (289), the two instances with the largest penalties, verified by the checker.
- **p2:** A strictly better UD2 solution for comp03, comp09, comp15, comp18 or comp21, verified by the checker.
- **p3:** A strictly better UD2 solution for an erlangen2011_2 to erlangen2014_1 instance (best 4,441 to 8,813 on OptHub), verified by the checker.

## How a win is checked

Instances: https://opthubstorage.blob.core.windows.net/opthub-data/timetabling/edutt/ctt/cb-ctt-ud2/instances/ectt/ < name > .ectt. Best solution files: linked from each instance page (e.g. https://opthubstorage.blob.core.windows.net/opthub-data/timetabling/edutt/ctt/cb-ctt-ud2/solutions/comp12/comp12_15.sol). The checker computes hard violations and the four UD2 soft costs (RoomCapacity 1 per excess student, MinWorkingDays 5 per missing day, IsolatedLectures 2 each, RoomStability 1 per extra room), must reproduce the OptHub value of the posted best file, then evaluates the claim. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://opthub.uniud.it/problems/timetabling/edutt/ctt/cb-ctt-ud2>

## Sources

- <https://opthub.uniud.it/problems/timetabling/edutt/ctt/cb-ctt-ud2>
- <https://opthub.uniud.it/problems/timetabling/edutt/ctt/cb-ctt-ud2/instances/comp12>
- <https://opthub.uniud.it/problems/timetabling/edutt/ctt/cb-ctt-ud2/instances/comp05>
- <https://doi.org/10.1007/s10479-010-0707-0>
- <https://www.cs.uni-potsdam.de/wv/publications/DBLP_journals/anor/BanbaraIKOSSTW19.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fix-and-reoptimise with a MIP/CP-SAT model of UD2: free all lectures of a few curricula or a few days and re-solve exactly from the best posted file.
- Simulated annealing with Kempe-chain and swap moves (the Bellio-Ceschia-Di Gaspero-Schaerf line) tuned per instance, run for days on many seeds.
- ASP/MaxSAT (teaspoon-style) with solution hints from the posted best file.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- OptHub is a JavaScript app; read it in a browser or via its rendered page, and note the 'Created at' date of imported solutions (2021-12-07) is the import date, not the discovery date.
- Other formulations (UD1, UD3-UD5) use different penalties; only UD2 counts here.
- comp01 (5) and the UD2 instances proven optimal by Banbara et al. 2019 cannot be improved; check the literature for any later optimality proof of the seven listed instances before investing.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/cb-ctt-itc2007-comp-open-instances.md
```

Already set up? Say `run V3R1T4S on cb-ctt-itc2007-comp-open-instances`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cb-ctt-itc2007-comp-open-instances`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
