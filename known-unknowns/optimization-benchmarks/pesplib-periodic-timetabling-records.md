# PESPlib periodic timetabling: lower the best known weighted slack of a railway instance R1L1..R4L4

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (instances have 2,600-8,400 events and 6,400-18,000 activities; files are a few hundred KB) · open as of 2026-10-30

## The problem

The Periodic Event Scheduling Problem (Serafini and Ukovich 1989): given events and activities (i,j) with bounds [L,U] and weights w, choose periodic event times (period T=60) so that each activity duration D, with D congruent to pi_j - pi_i mod T, lies in [L,U], minimising the weighted slack sum w(D-L). PESPlib, created by Marc Goerigk and now hosted with TimPassLib, keeps 22 instances and a dated record history. Records have been improved by Goerigk, Liebchen, Paetzold, Matos and Albino, Lindner, Roth, Bortoletto, Masing, Ebert, Gleixner, Heidemann and, in August 2026, Ramos, who lowered every instance. Current best values (live 2026-10-30): R1L1 29,824,049; R1L2 30,055,723; R1L3 28,339,653; R1L4 25,877,852; R2L1 39,943,601; R2L2 38,783,647; R2L3 36,765,606; R2L4 31,497,313; R3L1 42,089,847; R3L2 43,281,389; R3L3 37,654,146; R3L4 31,553,558; R4L1 46,345,944; R4L2 46,062,018; R4L3 43,245,224; R4L4 35,799,285 (railway set 01); BL1 6,134,104; BL2 6,282,830; BL3 6,337,431; BL4 5,775,151 (bus set 02); R1L1v 42,391,128; R4L4v 60,097,211 (variant set 03). The best lower bounds are far lower (for example 20,230,655 for R1L1; the page notes that lower bounds are not verified), so every instance is open.

## What counts as a win

A solution file ('activity; duration' lines) for one railway instance R1L1..R4L4 from https://timpasslib.aalto.fi/data/pesplib/set-01.tar.gz such that every duration lies within its activity's [L,U], the durations are periodic (event times pi in Z_60 exist with pi_j - pi_i congruent to D mod 60 for every activity, checked by propagating along a spanning forest and testing all activities), and the weighted slack sum w(D-L) is strictly below the best objective shown for that instance on https://timpasslib.aalto.fi/pesplib.html, re-fetched immediately before claiming. An independent checker must first reproduce the posted best objective from the posted .sol file. Nothing is submitted (the page takes submissions by email); the write-up goes to the human.

## Partial wins

- **p1:** The same checks for one bus instance BL1..BL4 (set-02.tar.gz): a feasible periodic solution with weighted slack strictly below the live best objective for that instance.
- **p2:** The same checks for one variant instance R1L1v or R4L4v (set-03.tar.gz): a feasible periodic solution with weighted slack strictly below the live best objective for that instance.

## How a win is checked

Parse the instance ('N; O; T; L; U; W') and the solution ('N; D'). Check that the activity sets match and that L<=D<=U, build event times by BFS over the activity graph with pi_j = pi_i + D mod 60, assert that every activity satisfies (pi_j - pi_i - D) mod 60 = 0, and sum w(D-L). A 40-line Python checker written during vetting reproduced the posted R1L1 record file R1L1-29824049.sol exactly (objective 29,824,049) in seconds. Re-fetch pesplib.html with curl and parse the last (lowest) objective listed for the instance.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://timpasslib.aalto.fi/pesplib.html>

## Sources

- <https://timpasslib.aalto.fi/pesplib.html>
- <https://timpasslib.aalto.fi/data/pesplib/set-01.tar.gz>
- <https://timpasslib.aalto.fi/data/pesplib/R1L1-29824049.sol>
- <https://doi.org/10.1016/j.cor.2012.08.018>
- <https://www.zib.de/userpage//lindner/OR_2024_paper_046.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the posted record .sol files and improve them with the modulo network simplex plus cycle-based MIP neighbourhoods (fix most periodic offsets, re-optimise a subnetwork with CP-SAT or HiGHS), the approach of the Lindner and Masing line of work.
- Concurrent heuristics: combine modulo network simplex, maximum-cut style moves and sub-MIPs over fundamental cycles, restarting from different spanning trees.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Each instance row on the page lists its history; the best value is the lowest (last) entry, not the first.
- Lower bounds on the page are marked 'not verified'; do not claim a bound improvement as a win.
- The PESPlib-derived instances inside TimPassLib (R1L1 etc.) have different activity sets and objectives; they belong to the separate TimPassLib entry.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/pesplib-periodic-timetabling-records.md
```

Already set up? Say `run V3R1T4S on pesplib-periodic-timetabling-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pesplib-periodic-timetabling-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
