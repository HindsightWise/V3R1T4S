# ITC2021 sports timetabling: lower the best known penalty of an open instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The 2021 International Timetabling Competition (organised by David Van Bulck and Dries Goossens of Ghent University, Jeroen Belien of KU Leuven and Morteza Davari of SKEMA Business School) left 45 double round-robin instances (16-20 teams, Early/Middle/Late) whose live table at the RobinX repository lists the best lower and upper bound as (infeasibility, penalty). After the competition, records were lowered by Krystallidis and Musliu, Team UoS, Fonseca and Toffolo, Van Bulck and Goossens, Premananda and Muklason and others, with the newest change on 11 July 2026 (Early_1 and Late_11). On 2026-10-28 the table shows 3 instances closed (Middle_4 at 7, Late_4 and Late_15 at 0) and 42 of 45 with best known penalty above the best lower bound (e.g. Middle_3: LB 3378 vs UB 8648; Early_7: 1296 vs 4744; Late_12: 203 vs 3226). The page says submissions are open again (by email to the organisers; a human-only step). Find a feasible timetable with a strictly lower penalty.

## What counts as a win

A solution XML for an ITC2021 instance listed on https://robinxval.ugent.be/ITC2021/instances.php that the open-source RobinX/ITC2021 validator (github.com/Robin-X/RobinX) evaluates to infeasibility 0 and a penalty strictly below that instance's 'Best UB' value, also reproduced by a second, independently written evaluator, with the table and the instance's history page re-fetched live immediately before claiming.

## Partial wins

- **itc2021-middle-late-improve:** Strict improvement on any Middle or Late instance whose UB is more than 500 above its LB (e.g. Middle_1/2/3, Late_2, Late_12), validated by the RobinX validator.
- **itc2021-lower-bound-certificate:** A strictly higher lower bound for any open instance, given as a saved MIP/CP model file plus solver log and seed whose dual bound a skeptic re-runs to the same value (or better) in a fresh session; or, more strongly, a feasible timetable whose penalty equals the listed Best LB, which closes the instance and is checked by the validator alone.
- **itc2021-reproduce-validator:** Build the RobinX validator and reproduce the listed penalty of every posted best solution (45 files) exactly; a prerequisite that also catches stale table entries.

## How a win is checked

Instances: https://robinxval.ugent.be/validator/Repository/ITC2021/Instances/<name>.xml (redirect from sportscheduling.ugent.be, plain GET). Posted best solutions: .../ITC2021/Solutions/<file> (linked per row). Build RobinX with make (C++, GPL), run ./RobinX -i instance.xml -s solution.xml; first confirm it reproduces the posted best solution's penalty, then run it on the claim. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://robinxval.ugent.be/ITC2021/instances.php>

## Sources

- <https://robinxval.ugent.be/ITC2021/instances.php>
- <https://www.sportscheduling.ugent.be/ITC2021/downloads.php>
- <https://robinxval.ugent.be/validator/Repository/ITC2021/Instances/ITC2021_Middle_5.xml>
- <https://github.com/Robin-X/RobinX>
- <https://doi.org/10.1016/j.ejor.2022.11.046>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Two-phase decomposition used by strong ITC2021 entries: first fix the home/away pattern set (which teams play home in each slot) with a MIP that respects break constraints, then assign opponents with a second MIP or CP model; iterate with fix-and-optimize over windows of slots.
- Combinatorial design theory: 1-factorizations of K_n (e.g. the canonical 'circle' and its isomorphism classes) give structurally different starting timetables than random; enumerate many non-isomorphic factorizations as seeds.
- Satisfiability: encode one instance as weighted MaxSAT (hard constraints hard, soft penalties weighted) and run modern MaxSAT solvers (core-guided plus local search); Late and Middle instances with small LB/UB gaps are good first tests.
- Neural guided search import from chip placement: learn which slots/teams to free in each large-neighbourhood step from improvement history across instances (bandit or simple classifier), rather than choosing uniformly.
- Start from the posted best solutions (downloadable) rather than from scratch; the cheapest wins usually come from long polishing runs on instances whose record was set by a short competition run.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Lexicographic objective: (infeasibility, penalty). A low-penalty timetable with any hard violation is worse than every feasible one; only infeasibility 0 counts.
- Version mismatch: the instance archives exist in versions (EarlyInstances_V2/V3, TestInstances_V2/V3); validate against the exact XML linked from the live table row.
- Test instances (Test1-Test8, Demo) are not competition instances; improving them is not an ITC2021 record.
- Self-reported lower bounds are not checkable by themselves; never claim a 'gap closed' without a feasible timetable whose validated penalty equals the bound.
- Re-fetch the table and the instance's history page before claiming; records changed as recently as 11 July 2026.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/itc2021-sports-timetabling-ub.md
```

Already set up? Say `run V3R1T4S on itc2021-sports-timetabling-ub`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `itc2021-sports-timetabling-ub`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
