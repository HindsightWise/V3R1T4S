# ITC-2007 examination timetabling (track 1): beat the best known penalty on one of the 12 competition instances

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The ITC-2007 examination track (McCollum, McMullan, Burke, Parkes and Qu) asks for an assignment of exams to periods and rooms meeting hard constraints (no student conflicts, room capacity, period lengths, period and room hard constraints) and minimising weighted soft penalties (two in a row, two in a day, period spread, mixed durations, front load, period and room penalties). OptHub (University of Udine) keeps the uploaded solutions. On 2026-10-30 the best known values are set1 3,085, set2 380, set3 7,041, set4 10,448, set5 2,327, set6 25,120, set7 3,225, set8 7,077, set9 898, set10 12,878, set11 22,186, set12 5,095. David Van Bulck holds set1, set4, set7, set9 and set11 (files posted 2022-2023). Yuri Bykov holds set2, set3, set5, set10 and set12 (files posted 2021-12-19). The set6 (25,120) and set8 (7,077) instance pages returned HTTP 500 on 2026-10-30, but their solution files (e.g. set6_128.sol, set8_74.sol) are listed in OptHub's public storage container. Earlier records came from Bykov and Petrovic and from Battistutta, Schaerf and Urli's single-stage simulated annealing. As far as the vetters found, no ITC-2007 exam instance has a published lower bound matching its best known value. Find a feasible solution with a strictly lower penalty than OptHub's best for one of set1-set12.

## What counts as a win

A solution in the ITC-2007 exam .sol format (one line 'period, room' per exam, in exam order) for one of set1-set12, that an independent checker written from the ITC-2007 examination track specification reports as hard-feasible with total soft penalty (using the instance's own institutional weightings) strictly below the 'Best solution' for that instance on https://opthub.uniud.it/problems/timetabling/edutt/ett/itc-2007-ett, re-fetched live immediately before claiming. The checker must first reproduce the OptHub objective of that instance's posted best file (e.g. 3,085 for set1_443.sol, 5,095 for set12.sol). For set6 and set8, whose instance pages returned HTTP 500 on 2026-10-30, the checker must instead reproduce the problem-page best (25,120 and 7,077) as the minimum over the files listed at https://opthubstorage.blob.core.windows.net/opthub-data?restype=container&comp=list&prefix=timetabling/edutt/ett/itc-2007-ett/solutions/ < set > / ; an instance whose best value cannot be reproduced that way does not count. Nothing is uploaded by the agent.

## Partial wins

- **p1:** A strictly better solution for set12 (5,095, unchanged since Bykov) or set11 (22,186), verified by the checker.
- **p2:** A strictly better solution for any other set1-set10 instance, verified by the checker.
- **p3:** A strictly better solution for one of the eight Yeditepe instances on the same OptHub page (yue20011-6-450 ... yue20032-6-550), verified by the checker.

## How a win is checked

Instances: https://opthubstorage.blob.core.windows.net/opthub-data/timetabling/edutt/ett/itc-2007-ett/instances/exam/ < set > .exam; best solutions: linked from each instance page (e.g. .../solutions/set12/set12.sol). The checker parses exams with student lists, periods, rooms, period and room hard constraints and institutional weightings, verifies hard constraints, computes the seven soft components, reproduces the posted best value, then evaluates the claim. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://opthub.uniud.it/problems/timetabling/edutt/ett/itc-2007-ett>

## Sources

- <https://opthub.uniud.it/problems/timetabling/edutt/ett/itc-2007-ett>
- <https://opthub.uniud.it/problems/timetabling/edutt/ett/itc-2007-ett/instances/set1>
- <https://opthub.uniud.it/problems/timetabling/edutt/ett/itc-2007-ett/instances/set12>
- <https://doi.org/10.1287/ijoc.1090.0320>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the posted best files and apply long simulated annealing or late-acceptance hill climbing with Kempe-chain moves. set12 still has Bykov's 2021 file and is the obvious first test.
- Period-assignment as graph colouring plus room assignment as a matching; re-optimise one period block at a time with CP-SAT.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Papers sometimes report lower values without posting files. Only the OptHub value can be checked, but a claim below OptHub that is above a published (unverified) value should be reported as such.
- The Yeditepe instances (Parkes and Ozcan's conversion) are scored separately; compare them only against their own OptHub rows.
- Institutional weightings differ per instance and are read from the file header; hard-coding them breaks the checker.
- OptHub's instance pages sometimes return a server error (set6 and set8 on 2026-10-30); the best value is still on the problem page, and the solution files can be listed from the storage container (https://opthubstorage.blob.core.windows.net/opthub-data?restype=container&comp=list&prefix=timetabling/edutt/ett/itc-2007-ett/solutions/set6/), which on 2026-10-30 held exam6.sol, set6.sol, set6_20.sol, set6_128.sol for set6 and exam8.sol, set8.sol, sol8-7312.sol, sol-8-7280.sol, set8_74.sol for set8.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/itc2007-exam-timetabling-bks.md
```

Already set up? Say `run V3R1T4S on itc2007-exam-timetabling-bks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `itc2007-exam-timetabling-bks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
