# TSPTW makespan (Lopez-Ibanez collection): beat the best-known makespan 917.83 of rc_204.1, the last open makespan cell

🚚 **Optimization benchmarks** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (one 46-node asymmetric instance with 4-decimal travel times; anytime DP, beam search or LNS runs) · open as of 2026-10-30

## The problem

Manuel Lopez-Ibanez (with Christian Blum) maintains the canonical TSPTW benchmark collection at lopez-ibanez.eu/tsptw-instances. It has 467 instances, best-known permutations for the travel-time and makespan objectives, and a bounds file per objective (page last modified 30 Dec 2023, re-fetched 2026-10-30). For makespan (the return time to the depot, waiting included), Makespan_Bounds.csv still shows 5 rows with a nonzero gap against the peel-and-bound dual bounds of Isaac Rudich, Quentin Cappart and Louis-Martin Rousseau (JAIR 2023). That count is what remained after Romain Fontaine, Jilles Dibangoye and Christine Solnon (EJOR 2023) closed 7 of 12. Four of those five are now closed. F. J. Soulignac ('Beware of the Classical Benchmark Instances for the Traveling Salesman Problem with Time Windows', arXiv 2512.01064, Computers & Operations Research 2026; code and results.json at github.com/fsoulignac/tsptw-m) solved every classical instance with 50 or more customers exactly. His published optimal routes give n80w180.002 = 633, n80w200.004 = 667, n200w120.002 = 1072 and n200w140.003 = 1083, equal to the posted best-known values; the CSV has not been updated. The one remaining open makespan cell is SolomonPotvinBengio rc_204.1 (Potvin and Bengio 1996, derived from Solomon's RC2 instances; 46 nodes = depot + 45 customers; travel times with 4 decimals). Its best-known makespan is 917.83 (the posted permutation evaluates to 917.8265), from the Beam-ACO and compressed-annealing work of Lopez-Ibanez, Blum, Ohlmann and Thomas (Applied Soft Computing 2013) and later contributors credited on the page. Its Rudich bound is 915.2194. Soulignac's exact solver runs out of memory on it, and he reports that the exact methods of Rudich et al. and Fontaine et al. jointly left it unsolved within an hour. Find a feasible route with makespan below 917.83, or certify that the gap is closed.

## What counts as a win

A permutation of customers 1..45 of rc_204.1 (depot 0 excluded, as in the site's best-known files). It is evaluated by a standalone checker written from the page's format description: line 1 is n = 46; then the 46 x 46 matrix (row i = travel time i->j, with the service time of i already folded in); then 46 time windows (e_i, l_i), node 0 = depot. Start at the depot at time 0. At each next node j, t = max(t + d[i][j], e_j), and t <= l_j must hold, including on the return to the depot; use exact decimal arithmetic. The checker must report zero violations and a return time at the depot that, rounded to 2 decimals, is at most 917.82. That is strictly below the 'Best Known Solution' 917.83 in the rc_204.1 row of Makespan_Bounds.csv (direction: min). Before any claim, the same checker must reproduce the posted rc_204.1 permutation in SolomonPotvinBengio-best-known-makespan.txt (makespan 917.8265, travel time 917.7523, 0 violations; vetted 2026-10-30). The new value must not fall below the Rudich bound 915.2194, which would mean a checker bug. Right before claiming, re-fetch the CSV and the page, and search the citing works of arXiv 2512.01064 and of Fontaine et al. (EJOR 2023) for newer exact results on rc_204.1; the cell must still be open. The permutation, checker and CSV snapshot are saved together. Nothing is submitted; the write-up goes to the human.

## Partial wins

- **p1:** Close the rc_204.1 makespan gap without improving the route. This means a proof that no feasible route has makespan below 917.8265, or a proven lower bound strictly above 915.2194. It must come from an exact solver whose code is released and which the skeptic re-runs to the same result, cross-checked by a second, independently implemented exact method (for example a labelling DP over (visited set, last node) with dominance, against a MIP or decision-diagram bound).

## How a win is checked

The skeptic downloads SolomonPotvinBengio.tar.gz and SolomonPotvinBengio-best-known-makespan.txt from lopez-ibanez.eu/files/TSPTW/. It writes or reuses an independent checker of about 30 lines; the site's check_solution.cpp may be read to confirm the conventions but need not be run. The checker must first reproduce the posted rc_204.1 makespan 917.8265. Then it evaluates the claimed permutation: zero violations, makespan rounded to 2 decimals <= 917.82, and not below 915.2194. Finally the skeptic re-fetches Makespan_Bounds.csv and searches for newer exact results on rc_204.1. This takes seconds on any machine. For p1, the skeptic re-runs the released solver and the second method.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://lopez-ibanez.eu/tsptw-instances>

## Sources

- <https://lopez-ibanez.eu/tsptw-instances>
- <https://lopez-ibanez.eu/files/TSPTW/Makespan_Bounds.csv>
- <https://lopez-ibanez.eu/files/TSPTW/SolomonPotvinBengio-best-known-makespan.txt>
- <https://lopez-ibanez.eu/files/TSPTW/SolomonPotvinBengio.tar.gz>
- <https://arxiv.org/abs/2512.01064>
- <https://github.com/fsoulignac/tsptw-m>
- <https://doi.org/10.1016/j.asoc.2013.05.009>
- <https://doi.org/10.1016/j.ejor.2023.06.001>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- rc_204.1 is small (45 customers), but its windows are loose relative to the horizon, which is why exact informed searches exhaust memory on it. A labelling DP over (visited set, last node, arrival time) is the natural first try, with time-window reachability pruning, dominance and 917.83 as the incumbent. A bidirectional search may help.
- Anytime beam search for domain-independent dynamic programming (Kuroiwa and Beck, AAAI 2024), or the Fontaine-Dibangoye-Solnon anytime approach, run for hours with the best-known value as the incumbent.
- Large neighbourhood search with CP sequence variables (Delecluse et al. 2022) or decision diagrams (Gillard and Schaus 2022), seeded from the posted permutation. Re-optimise windows of 10-20 consecutive positions exactly for makespan.
- GVNS for makespan (Amghar, Cordeau and Gendron) or Beam-ACO with many seeds as a cheap restart loop.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The other four rows that still show a gap in Makespan_Bounds.csv (n80w180.002, n80w200.004, n200w120.002, n200w140.003) are closed. Soulignac's exact solver proves their posted values optimal (results.json in github.com/fsoulignac/tsptw-m), and the CSV is simply not updated. Do not chase them.
- The distance matrix already includes the service time of the origin node, so do not add service times again.
- Makespan is the arrival time back at the depot, waiting included. A tour that is shorter in travel time can be worse in makespan.
- rc_204.1 travel times have 4 decimals. Evaluate in exact decimal arithmetic and compare after rounding to 2 decimals, as the table does (917.8265 is listed as 917.83).
- Do not chase the travel-time rows that show a gap in Traveltime_Bounds.csv. Their 'Relaxed Bound' is Baldacci et al.'s reported optimum, which the maintainer says is not reliable on the canonical files.
- Use the canonical file from this page, not a recreated Potvin-Bengio instance.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/tsptw-lopez-ibanez-open-cells.md
```

Already set up? Say `run V3R1T4S on tsptw-lopez-ibanez-open-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tsptw-lopez-ibanez-open-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
