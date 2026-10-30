# Permutation flow shop (Taillard benchmarks): a makespan below the best known for one of the 12 open Taillard instances, with VRF instances as partial wins

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (50-200 jobs x 20 machines; VRF up to 800 x 60; one makespan evaluation takes microseconds) · open as of 2026-10-30

## The problem

Éric Taillard's 120 permutation flow-shop instances (EJOR 64(2):278-285, 1993) are the standard PFSP benchmark: minimise the makespan, with jobs in the same order on every machine. Two sources agree on 2026-10-29 that 12 instances are open: Taillard's own bounds file (best_lb_up.txt, 'Update : 03.06.2026', on the mistic.iict-heig-vd.ch domain since June 2026; its legend already cites Brunner's v10e of 2 July 2026) and Olivier Brunner's Zenodo dataset of best-known schedules (v12, 4 October 2026, the newest version, CSVs with the permutation behind every Taillard record). The open instances (LB/UB) are Ta051 3771/3846, Ta054 3635/3719, Ta055 3553/3610, Ta059 3645/3741 and Ta060 3696/3755 (50x20); Ta081 6135/6171, Ta085 6270/6277, Ta086 6311/6329, Ta087 6216/6221, Ta088 6327/6357 and Ta089 6232/6246 (100x20); and Ta102 11154/11160 (200x20). The upper bounds come from Ravetti, Riveros, Mendes, Resende and Pardalos 2012 (Ta051); Pan, Tasgetiren and Liang 2008 (Ta054, Ta059); Deroussi, Gourgand and Norre 2006 (Ta055); Jan Gmys (Ta060, Ta102); and Brunner, whose 'BRunner' tabu-type local search lowered Ta081 and Ta085-Ta089 in 2025-2026 (for example Ta088 6372 -> 6357 and Ta085 6285 -> 6277, against Gmys's 2021 table). Taillard's file credits the lower bounds of the five 50x20 instances to R. J. M. Vaessens (1995 branch-and-bound, code 'Va') and those of the seven 100x20 and 200x20 instances to Gmys, whose GPU-accelerated parallel branch-and-bound also closed many instances (INFORMS J. Comput. 34(5):2502-2522, 2022; dataset doi:10.5281/zenodo.4542886). The same dataset tracks the 480 VRF instances of Vallada, Ruiz and Framinan (EJOR 240(3):666-677, 2015). There, Brunner and J. A. Alejandro-Soto keep lowering records (Zenodo datasets 2025-2026; Alejandro-Soto, Segura and Trejo-Sanchez, Comput. Oper. Res. 191, 2026). Find a permutation with a makespan strictly below the listed UB for one of the 12 open Taillard instances.

## What counts as a win

A permutation of the jobs 1..n (1-based; the order used on every machine) for one Taillard instance listed with LB < UB in https://mistic.iict-heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/best_lb_up.txt. A standalone checker computes C[i][k] = max(C[i-1][k], C[i][k-1]) + p[i][pi_k] from the processing times in Taillard's instance file: tai50_20.txt, tai100_20.txt or tai200_20.txt in the same flowshop.dir, where each instance has a header 'n m seed UB LB' followed by m rows of n times (machine-major). The reported makespan must be strictly below both the UB in best_lb_up.txt and the UB in the newest version of Brunner's Taillard_UB_Schedules CSV (concept doi:10.5281/zenodo.16328984; v12 = https://zenodo.org/records/23138276, published 2026-10-04), both re-fetched immediately before claiming. The checker must first reproduce the listed UB from the CSV's own permutation for the claimed instance (verified 2026-10-29 for all 120 Taillard rows). The permutation, the checker, the instance file with its sha256 and both fetched tables are saved together. Nothing is sent to Taillard or Brunner by the agent; the write-up goes to the human.

## Partial wins

- **vrf-large-improve:** A makespan strictly below the UB in the newest VFRlarge_UB_Schedules CSV for a VRF-large instance (100 to 800 jobs) whose OptimalityNotRefuted flag is 0 (175 of 240 in v12). The same checker runs on that instance's file vrf/ < name > _Gap.txt from TestSolutions.zip in Zenodo 4542886 (md5 1723b5363969f7f0dea8317076d1cde3; extract with bsdtar), or on the official file from the VRF site soa.iti.es if it is reachable at claim time. Where the CSV posts a permutation, the checker must first reproduce the CSV UB from it. The VRF format is 'n m' followed by one line per job of m (machine, time) pairs, with machines numbered from 0. VFR800_60_3 to VFR800_60_9 are damaged or missing in Gmys's archive and cannot be claimed without an official file. Brunner's own campaign covers only instances with up to 100 jobs, so most records with 200-800 jobs come from Gmys (2021) or Alejandro-Soto (2025).
- **vrf-small-improve:** The same for a VRF-small instance (n <= 60) whose OptimalityNotRefuted flag is 0 (43 of 240 in v12), on vrf/ < name > _Gap.txt from the same archive. All 240 small files are present and reproduce the v12 CSV UBs.
- **vrf-unposted-schedule:** A checker-validated permutation whose makespan equals or beats the listed UB for one of the eight VRF-large rows whose Permutation field is '0' in v12 and whose instance file is in Gmys's archive: VFR600_60_9, VFR700_60_3, VFR700_60_4, VFR700_60_9, VFR700_60_10, VFR800_60_1, VFR800_60_2 and VFR800_60_10. This makes that record checkable for the first time. VFR800_60_5, VFR800_60_6 and VFR800_60_9 also lack a permutation, but their files are missing from the archive, so they are excluded.

## How a win is checked

Taillard data: https://mistic.iict-heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai50_20.txt, tai100_20.txt and tai200_20.txt. Verified 2026-10-29: these are identical to the ta051-ta060, ta081-ta090 and ta101-ta110 files in Gmys's Zenodo archive, and ta001 regenerates exactly from Taillard's published LCG with seed 873654221. Schedules: Taillard_UB_Schedules_v12.csv from https://zenodo.org/records/23138276 (semicolon-separated columns Name;n;m;LB;UB;OptimalityNotRefuted;UBFoundBy;PermutationFoundBy;Permutation; md5 9247ae984324c9e6cec389b227b18c7d). A 40-line Python checker parses the instance, checks the permutation and computes the makespan by the recurrence. On 2026-10-29 it reproduced the UB from the posted permutation for 120/120 Taillard rows, 240/240 VRF-small rows and 224/240 VRF-large rows (exceptions in pitfalls). Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mistic.iict-heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/best_lb_up.txt>

## Sources

- <https://mistic.iict-heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/best_lb_up.txt>
- <https://mistic.iict-heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/ordonnancement.html>
- <https://mistic.iict-heig-vd.ch/taillard/problemes.dir/ordonnancement.dir/flowshop.dir/tai100_20.txt>
- <https://doi.org/10.5281/zenodo.16328984>
- <https://zenodo.org/records/23138276>
- <https://zenodo.org/records/23138371>
- <https://doi.org/10.5281/zenodo.4542886>
- <https://doi.org/10.5281/zenodo.20617305>
- <https://arxiv.org/abs/2509.23512>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the posted record permutation and run long iterated-greedy or tabu searches with Taillard's acceleration for insertion neighbourhoods (Ruiz-Stützle iterated greedy and its variants). Brunner's report (Zenodo 23138371) describes what produced the 2025-2026 records: a super-prohibition tabu list, adaptive compartmental neighbourhoods with 2-closure, and vectorised makespan evaluation.
- Target the smallest gaps: Ta087 (6216/6221), Ta085 (6270/6277) and Ta102 (11154/11160). A decision search for makespan <= UB - 1 with two-machine (Johnson) lower bounds, as in Gmys's branch-and-bound, either finds a schedule or prunes most of the space.
- Physics import: replica-exchange Monte Carlo or population annealing over permutations with insertion moves. The 100x20 landscapes are glassy, which is where replica exchange helps more than plain restarts.
- The reversed instance (machine order reversed, permutation reversed) has the same optimal makespan. Alternating the search between the two directions changes the neighbourhood structure at no cost.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The header line of each instance in Taillard's files still gives the 1993 bounds (ta051: 3875 and 3480). Current bounds are only in best_lb_up.txt and Brunner's CSVs.
- On 2026-10-29 Taillard's old host mistic.heig-vd.ch timed out and the VRF site soa.iti.es returned 502. Gmys's archive (TestSolutions.zip in Zenodo 4542886, md5 1723b5363969f7f0dea8317076d1cde3) holds all the data, but macOS unzip rejects it (bsdtar extracts it), and its VRF part is truncated: VFR800_60_3 to VFR800_60_9 are missing or damaged.
- In the v12 VFRlarge CSV, VFR300_60_4's permutation is stored shifted by one (values 2..301; subtracting 1 reproduces 20114), and 11 rows have no permutation.
- 'OptimalityNotRefuted' is not a proof; Brunner says to interpret it with caution. Lower bounds also differ between sources (CSV vs Taillard's file: Ta081 6134 vs 6135, Ta088 6316 vs 6327, Ta102 11153 vs 11154), so judge claims against the UB only.
- Two groups update their records independently: Brunner went from v5 to v12 between July 2025 and October 2026, and Alejandro-Soto posted v4 in June 2026 (merged into Brunner's CSV as source 50). Beat the newest version of every source. Only permutation schedules count ('ONLY PERMUTATION SCHEDULES ALLOWED'); flowtime and non-permutation records are different problems.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/pfsp-taillard-open-makespans.md
```

Already set up? Say `run V3R1T4S on pfsp-taillard-open-makespans`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pfsp-taillard-open-makespans`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
