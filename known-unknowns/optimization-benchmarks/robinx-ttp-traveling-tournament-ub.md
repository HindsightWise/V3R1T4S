# Traveling Tournament Problem (RobinX repository): shorter total travel for an open NL, NFL, GAL, CIRC, SUP, BRA or CON instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The Traveling Tournament Problem (Easton, Nemhauser and Trick, 2001) asks for a double round-robin schedule minimising total team travel, with at most three consecutive home or away games and no immediate rematches. Michael Trick's original challenge page was frozen in 2022 and handed to the RobinX repository maintained by David Van Bulck (Ghent), which lists validated best upper bounds, best lower bounds and literature-only upper bounds. Many instances remain open, e.g. GAL40 (LB 227134, UB 240063), NFL32 (836031 vs 914620 in the literature), CIRC20 (1600 vs 1724), BRA24 (470496 vs 499804). Find a feasible schedule with strictly smaller total travel than both the repository's best UB and any literature UB for that instance.

## What counts as a win

A schedule (RobinX solution XML) for a classic TTP row on https://robinxval.ugent.be/RobinX/travelRepo.php (classification '2RR, C, ∅ | CA3, SE1 | TR'; not a Mirrored or other variant row) whose Best LB is below min(Best UB, Best UB literature), such that the RobinX validator and an independent checker both report a valid double round robin with no more than three consecutive home or away games, no repeaters, and total travel (each team starts and ends at home) strictly below min(Best UB, Best UB literature) for that row (a '/' entry is ignored), with the page re-fetched live immediately before claiming.

## Partial wins

- **ttp-gal-circ-improve:** Strict improvement on any GAL (12-40 teams) or CIRC (12-40 teams) instance whose literature column is empty, so the repository value is the record.
- **ttp-nl-nfl-literature-match:** A validated schedule matching or beating a literature-only UB (e.g. NL16 261687, NFL24 463657) where the repository holds only a worse validated schedule; checkable and fills a public verification gap.
- **ttp-variant-improve:** Strict improvement on the mirrored or unconstrained variant of an open instance listed on the same page (separate rows), validated with the same checker using that variant's rules.

## How a win is checked

Download instance and posted best solution XML from https://robinxval.ugent.be/validator/Repository/TravelOptimization/Instances/<name>.xml and .../Solutions/<file>. A 40-line checker (verified 2026-10-13: it reproduces GAL40_240063.xml = 240063 and CIRC20_1724.xml = 1724 exactly with 0 violations) sums distances along each team's venue sequence, starting and ending at home, and checks round-robin, at-most-three, and no-repeater rules. Cross-check with the RobinX C++ validator (github.com/Robin-X/RobinX). Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://robinxval.ugent.be/RobinX/travelRepo.php>

## Sources

- <https://robinxval.ugent.be/RobinX/travelRepo.php>
- <https://robinxval.ugent.be/validator/Repository/TravelOptimization/Instances/GAL40.xml>
- <https://robinxval.ugent.be/validator/Repository/TravelOptimization/Solutions/GAL40_240063.xml>
- <https://robinxval.ugent.be/validator/Repository/TravelOptimization/Instances/CIRC20.xml>
- <https://robinxval.ugent.be/validator/Repository/TravelOptimization/Solutions/CIRC20_1724.xml>
- <https://github.com/Robin-X/RobinX>
- <https://mat.tepper.cmu.edu/TOURN/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Simulated annealing on the classical TTP neighbourhoods (swap homes, swap rounds, swap teams, partial swap rounds/teams; Anagnostopoulos, Michel, Van Hentenryck and Vergados) with strategic oscillation between feasible and infeasible regions; the larger GAL and CIRC records were set by short SA runs and likely have slack.
- Exploit symmetry in CIRC: the circular distance instances are invariant under rotation and reflection; search only over schedules generated from structured patterns (e.g. modified canonical schedules) and lift them.
- Vehicle-routing import: each team's away trips are short tours of at most three cities; evaluate and re-optimise trips as a small set-partitioning / TSP-with-capacity problem, then repair the round robin with an exact matching model per slot.
- Astronomy/geometry import for GAL: distances come from 3-D positions of exoplanets; cluster teams by position and build trips that visit clusters, as in hierarchical clustering heuristics for the Euclidean TSP.
- Column generation over away-trip sets, followed by a CP model that assembles trips into a valid schedule, which is the structure behind the strongest published lower bounds and can also produce good upper bounds on mid-size NL/NFL instances.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Two UB columns: an improvement over 'Best UB' that is still above 'Best UB literature' (e.g. NL16: 271476 vs 261687) is not a record; criterion is strictly below both.
- Mirrored, unconstrained and incomplete variants are separate rows with different rules; they count only for the variant partial win, validated with that variant's rules; a mirrored schedule claimed against the plain TTP row, or vice versa, is invalid.
- Travel must include the final trip home after the last slot and start from home; omitting either gives artificially small totals.
- Asymmetric data handling: distance files list team1/team2 pairs; build the matrix from the file rather than assuming symmetry or a particular team order (team ids are not in city-name order).
- Some rows are closed only via the literature column (e.g. CON22, CON28, CON34, CON40 have Best LB equal to the literature UB); they cannot be improved.
- Re-fetch the repository page before claiming; it is maintained (the RobinX GitHub backup was updated on 22 Oct 2026), although the classic-row histories checked on 2026-10-28 show no change since 2024.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/robinx-ttp-traveling-tournament-ub.md
```

Already set up? Say `run V3R1T4S on robinx-ttp-traveling-tournament-ub`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `robinx-ttp-traveling-tournament-ub`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
