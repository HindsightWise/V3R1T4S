# XHSTT high school timetabling (Post archive): beat a best known solution cost on an open XHSTT-2014 instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

XHSTT is the XML standard for (high) school timetabling instances created by Gerhard Post and colleagues. The archive at the University of Twente keeps, per instance, every submitted solution with its cost (infeasibility value, objective value) and lower bounds. The archive is live: on 2026-09-29 Dionisio Chiuratto Agourakis submitted Brazil Instance7 at 44 (with a lower bound of 40), and on 2026-10-06 Wieslaw Dudek submitted 42. The XHSTT-2014 overview (instances and best solutions, last updated 16 Nov 2022) lists these open instances as best/LB: AU-BG-98 126/0 (its instance page lists 128 as the best stored solution), DK-FG-12 1263/412, DK-HG-12 12.2330/7.0 (infeasibility 12, objective 2330), DK-VG-09 2.2323/2.0, ES-SS-08 335/334, NL-KP-03 199/0, NL-KP-05 425/89, NL-KP-09 1620/180, UK-SP-06 2.1410/0.0. Most of these bests are from the UFOP-GOAL team (George Fonseca, Haroldo Santos, Eduardo Carrano; solutions dated Dec 2016, received 17 April 2017). ES-SS-08's best is Matias Sorensen's (Jan 2016), with LB 334 from Simon Kristiansen, Sorensen and Thomas Stidsen. UK-SP-06's best is Wieslaw Dudek's (Oct 2022). Jeffrey Kingston wrote the HSEval evaluator and KHE. Costs compare hierarchically: lower infeasibility first, then lower objective. Find a solution strictly better than the best known for an open instance.

## What counts as a win

An XHSTT solution file for one instance that is open (best > LB) on https://www.utwente.nl/en/eemcs/dmmp/hstt/archives/XHSTT-2014/overview.html, whose cost, computed by an independent evaluator written from the XHSTT specification that first reproduces the cost of the best solution stored in that instance's own XML file, is hierarchically strictly lower (smaller infeasibility value, or equal infeasibility and smaller objective) than the best value on both the overview and the instance's dataset page, re-fetched live immediately before claiming. A cross-check with Kingston's HSEval is done by the human, not the agent; nothing is submitted to the archive by the agent.

## Partial wins

- **p1:** A strictly better feasible solution (infeasibility 0) for NL-KP-03, NL-KP-05, NL-KP-09, DK-FG-12 or AU-BG-98, verified by the independent evaluator.
- **p2:** For DK-HG-12 (best 12.2330, LB 7.0) or UK-SP-06 (best 2.1410, LB 0.0): a solution with lower infeasibility than the best, or equal infeasibility and lower objective. For DK-VG-09 (best 2.2323, LB (2,0)): infeasibility 2 with objective below 2323. Verified by the evaluator.
- **p3:** A strictly better solution for an instance outside XHSTT-2014 whose dataset page shows best > LB (e.g. Brazil Instance7: best 42 by Dudek on 2026-10-06 vs LB 40; Netherlands Kottenpark2008: 0.34586 vs LB 2795), verified by the evaluator.

## How a win is checked

Download the instance XML from its dataset page (e.g. https://www.utwente.nl/en/eemcs/dmmp/hstt/datasets/Netherlands/Kottenpark2009/, file 'instance and solutions'), which embeds the submitted solution groups. Write an evaluator for the constraint types present (AssignTime, AssignResource, SplitEvents, DistributeSplitEvents, PreferTimes, PreferResources, SpreadEvents, LinkEvents, OrderEvents, AvoidClashes, AvoidUnavailableTimes, LimitIdleTimes, ClusterBusyTimes, LimitBusyTimes, with Linear/Quadratic cost functions) from the specification; it must reproduce the stored best solution's (infeasibility, objective) exactly before evaluating the claim. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.utwente.nl/en/eemcs/dmmp/hstt/archives/XHSTT-2014/overview.html>

## Sources

- <https://www.utwente.nl/en/eemcs/dmmp/hstt/>
- <https://www.utwente.nl/en/eemcs/dmmp/hstt/archives/XHSTT-2014/>
- <https://www.utwente.nl/en/eemcs/dmmp/hstt/archives/XHSTT-2014/overview.html>
- <https://www.utwente.nl/en/eemcs/dmmp/hstt/datasets/>
- <https://www.utwente.nl/en/eemcs/dmmp/hstt/datasets/Brazil/Instance7/>
- <http://doi.org/10.1016/j.cor.2016.04.016>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Kottenpark instances (NL-KP-03/05/09) have the largest gaps (199/0, 425/89, 1620/180) and best values from a single 2016 method; a MIP/CP-SAT matheuristic that fixes most of the timetable and re-optimises one class or one day at a time is the natural lever.
- Two-phase: first time assignment with CP-SAT (hard constraints only), then resource assignment as a min-cost flow or small MIP.
- Kristiansen-Sorensen-Stidsen style integer programming for the Danish (Lectio) instances, where students are explicit resources.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The overview page was last updated 16 Nov 2022 and can disagree with the instance pages (AU-BG-98: overview 126, instance page 128); a claim must beat the better of the two.
- Instances were revised (e.g. Australian ones in March 2016, Brazil Instance7 in April 2015); evaluate against the current XHSTT-2014 file, not older archive versions.
- Cost is hierarchical: a solution with lower objective but higher infeasibility is worse.
- ES-SS-08 has a gap of one (335 vs LB 334), and DK-VG-09's infeasibility cannot drop below its LB of 2. Check the literature for an optimality proof before working on near-closed instances.
- Papers may report better values than the archive without submitting them; only archived values are the reference, but note any such published claim in the write-up.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/xhstt-2014-high-school-timetabling-bks.md
```

Already set up? Say `run V3R1T4S on xhstt-2014-high-school-timetabling-bks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `xhstt-2014-high-school-timetabling-bks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
