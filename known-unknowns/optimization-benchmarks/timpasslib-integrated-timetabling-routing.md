# TimPassLib: a periodic timetable with lower total passenger travel time than the best known for an open integrated timetabling-and-routing instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (instances from 32 to 21,328 events; evaluating one timetable is a series of shortest-path runs, seconds) · open as of 2026-10-30

## The problem

Integrated periodic timetabling and passenger routing: choose event times in {0..T-1} that satisfy the periodic bounds of every activity (drive, wait, change, sync, headway), then route every OD demand along shortest paths through drive, wait and change activities, a change costing its duration plus the instance's change penalty; minimise total passenger travel time. TimPassLib (Schiewe, Goerigk and Lindner, Operations Research Forum 4:64, 2023) maintains 27 instances with dated best solutions and lower bounds. Records have been set by Schiewe, Schöbel, Goerigk, Lindner, van Lieshout, Loebel and, on 31 Aug 2026, Ramos. Only toy and toy_2 are solved optimally. Current best totals (live 2026-10-30): Hamburg 140,850,920 (bound 139,892,927); Schweiz_Fernverkehr 61,855,004; Stuttgart 48,210,542,340; regional 1,827,124; grid 48,827; long-distance 66,981,422; metro 11,990,908; Erding_NDP_S020 12,228,304; Erding_NDP_S021 12,235,729; R1L1 538,536,289; R1L2 537,742,639; R1L3 537,105,340; R1L4 532,591,640; R2L1 670,939,152; R2L2 669,302,510; R2L3 667,292,632; R2L4 659,596,899; R3L1 686,543,137; R3L2 685,694,233; R3L3 683,258,276; R3L4 672,473,277; R4L1 745,524,467; R4L2 747,493,422; R4L3 742,094,966; R4L4 731,939,240.

## What counts as a win

A Timetable.csv ('event_id; time' with times in 0..T-1) for Hamburg, Schweiz_Fernverkehr, Stuttgart or one of R1L1..R4L4 from https://timpasslib.aalto.fi/data/ < instance > .zip such that every activity's periodic duration ((pi_j - pi_i - L) mod T) + L is at most U, and whose total passenger travel time, recomputed by an independent evaluator (sum over OD pairs of customers times the shortest path from any departure event at the origin to any arrival event at the destination over drive, wait and change activities, each change adding ean_change_penalty from Config.csv), is strictly below the best total shown for that instance on https://timpasslib.aalto.fi/solutions.html, re-fetched immediately before claiming. The evaluator must first reproduce the posted best total from the posted best Timetable for that instance. Nothing is submitted; the write-up goes to the human.

## Partial wins

- **p1:** The same checks and strict improvement for one of the smaller open instances regional, grid, long-distance, metro, Erding_NDP_S020 or Erding_NDP_S021.
- **p2:** For one open instance, a feasible timetable whose total ties the live best total exactly and whose periodic activity durations ((pi_j - pi_i - L) mod T) + L differ from those of the posted best timetable on at least 5% of the drive, wait and change activities (an independent alternative record, not a global time shift of the posted one; checked by direct comparison of the two duration vectors).

## How a win is checked

Read Config.csv (period_length, ean_change_penalty), Events.csv, Activities.csv, OD.csv and the timetable. Check periodic feasibility of all activities, then run Dijkstra from the set of departure events at each origin station over drive/wait/change arcs (duration, plus the penalty on change arcs) and take the cheapest arrival event at each destination; total = sum customers x distance. A 60-line Python evaluator written during vetting reproduced the posted toy optimum (21,466) and the posted Hamburg record (140,850,920) exactly. Re-fetch solutions.html and take the first (lowest) total listed for the instance.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://timpasslib.aalto.fi/solutions.html>

## Sources

- <https://timpasslib.aalto.fi/index.html>
- <https://timpasslib.aalto.fi/solutions.html>
- <https://timpasslib.aalto.fi/format.html>
- <https://doi.org/10.1007/s43069-023-00244-1>
- <https://timpasslib.aalto.fi/data/Hamburg/140850920_Timetable.zip>
- <https://arxiv.org/abs/2507.17566>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Alternate: fix passenger routes from the incumbent, solve the resulting PESP with weights = passengers per arc (modulo network simplex or sub-MIP), re-route by shortest paths, repeat; then perturb with local event shifts evaluated exactly.
- On small open instances (grid, metro, regional) a full MIP with route variables restricted to k-shortest paths per OD pair may reach or beat the records.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Periods differ by instance (Hamburg uses T=10); read period_length from Config.csv.
- Sync and headway activities must be feasible but cannot carry passengers; including them in routing gives a total that is too low.
- Solutions are listed best-first on solutions.html; bounds are listed separately and are not wins.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/timpasslib-integrated-timetabling-routing.md
```

Already set up? Say `run V3R1T4S on timpasslib-integrated-timetabling-routing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `timpasslib-integrated-timetabling-routing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
