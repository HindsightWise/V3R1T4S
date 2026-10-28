# Multi-activity multi-day shift scheduling (Curtois-Qu MATSP instances 1-225): beat a best known penalty

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The Shift Scheduling Benchmark site run by Tim Curtois (schedulingbenchmarks.org) hosts 225 multi-activity, multi-day retail staff-scheduling instances (Curtois and Qu; 7, 14 or 28 days, 10-150 staff, 1-19 tasks). On 1 Sept 2026 every best known solution was replaced by results from a multi-neighbourhood simulated annealing by Laszlo Kalman Trautsch and Bence Kovari (Budapest University of Technology and Economics, J. Sched. 2026); no lower bounds are published, and a command-line verifier was released on 7 Oct 2026. Checked 2026-10-28: all 225 rows still credit TRA26 and the Changes page has no multi-activity update after 7 Oct 2026 (later entries, the newest dated 21 Oct 2026, concern the separate nurse-rostering instances). Instance 5 already has best known 0 and cannot be improved. Find a solution for any instance with positive best known value whose total penalty is strictly lower than the listed best known value.

## What counts as a win

A solution in the site's XML solution format for one instance listed on https://www.schedulingbenchmarks.org/matsp/ with a positive 'Best known' value, such that an independent checker written from the published ProblemDefinition.pdf (which first reproduces penalty 889 on the site's example file 8_7_20_2.Solution.889.xml) reports all hard constraints satisfied and a total penalty strictly below that instance's 'Best known' value, with the table and https://www.schedulingbenchmarks.org/changes.html re-fetched live immediately before claiming. Cross-checking with the site's own RosterViewer or command-line verifier (closed-source binaries) is optional and done by the human, not the agent; nothing is emailed or submitted by the agent.

## Partial wins

- **matsp-small-instance-improve:** Strict improvement on any instance with at most 20 staff and positive best known value (instances 1-4, 6-10, 76-85, 151-160), checked by the independent evaluator; non-trivial because the current values are fresh 2026 SA results.
- **matsp-optimality-certificate:** A proof of optimality for any instance with positive best known penalty: an exact MIP/CP model file plus a solver log (and seed) whose matching lower bound a skeptic re-runs to the same value in a fresh session, or a VIPR-style certificate checked by an independent checker; the site lists no lower bounds, so this is new information even without a better solution.
- **matsp-independent-evaluator:** An open-source evaluator that reproduces the site's posted penalty for the example file and for a TRA26 best known solution if one is published; checkable by running it.

## How a win is checked

Download the instances (https://www.schedulingbenchmarks.org/matsp/data/instances1_225.zip, text and XML) and the formal definition (ProblemDefinition.pdf). Write an independent penalty evaluator and confirm it reproduces the penalty 889 of the site's example solution file https://www.schedulingbenchmarks.org/matsp/data/8_7_20_2.Solution.889.xml before trusting it. Evaluate the claimed solution with that evaluator. The official MATSP_Verifier and RosterViewer are closed-source binaries (MATSP_Verifier.zip); agents do not download and run them (kit/RULES.md rule 10), but the human may cross-check with them; a disagreement means the claim is not claimed. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.schedulingbenchmarks.org/matsp/>

## Sources

- <https://www.schedulingbenchmarks.org/matsp/>
- <https://www.schedulingbenchmarks.org/matsp/data/instances1_225.zip>
- <https://www.schedulingbenchmarks.org/matsp/ProblemDefinition.pdf>
- <https://www.schedulingbenchmarks.org/matsp/verify.html>
- <https://www.schedulingbenchmarks.org/matsp/MATSP_Verifier.zip>
- <https://www.schedulingbenchmarks.org/matsp/data/8_7_20_2.Solution.889.xml>
- <https://doi.org/10.1007/s10951-026-00886-z>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- All 225 records come from one method run once; a second, structurally different method is the obvious lever: column generation over individual weekly shift patterns (as in the Strandmark-Qu-Curtois work on the sibling nurse instances) with a restricted-master MIP to pick one pattern per employee.
- Small instances first: instances with 10-20 staff and 1-2 tasks (e.g. 1-10, 76-85, 151-160) are small enough for an exact CP-SAT or MIP model of the full problem; proving or improving them gives quick, checkable records.
- Large-neighbourhood search that frees all assignments of one day or one task at a time and re-solves that slice exactly with CP-SAT, keeping the rest fixed.
- Telecom / call-centre workforce management import: staffing curves per 15-minute interval are a classic set-covering problem; solve the coverage layer as a min-cost flow over time intervals first, then assign people.
- Music/sequence modelling import: treat each employee's week as a string over a small alphabet of shift/task tokens and use a learned or n-gram proposal distribution inside the annealer, so moves stay in the space of plausible rosters.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Instance numbering: files are named <id>_<days>_<staff>_<tasks> (e.g. 8_7_20_2); the example solution 8_7_20_2.Solution.889.xml (2019) is NOT the current best (763), so beating 889 is not a win.
- The closed-source verifier is a convenience, not a proof, and agents do not run it: the independent evaluator must reproduce 889 on the example file before it is trusted, and any later disagreement with the official tool (run by the human) withdraws the claim.
- Hard constraints are not penalties: a solution that trades a hard-constraint violation for a low penalty is infeasible; the checker must report hard feasibility separately.
- The nurse rostering instances 1-24 on the same site are a different problem with a different format; Instance 24's 1-unit gap (LB 40438, UB 40439) is not part of this target.
- Re-fetch the table and the Changes page right before claiming: all 225 values changed on 1 Sept 2026 and could change again.
- Instance 5 (7 days, 10 staff, 2 tasks) has best known 0: it is already optimal and cannot be improved.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/matsp-multi-activity-shift-scheduling.md
```

Already set up? Say `run V3R1T4S on matsp-multi-activity-shift-scheduling`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `matsp-multi-activity-shift-scheduling`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
