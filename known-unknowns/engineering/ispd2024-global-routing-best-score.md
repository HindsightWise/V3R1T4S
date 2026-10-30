# ISPD 2024 large-scale global routing benchmarks: a lower official evaluator cost than the best published router

🛠️ **Engineering and chips** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for benchmarks 0-4 and 7-11 (up to 3.3M nets, 64 GB RAM helps); the 10.6M and 59.3M-net cases need a large-memory machine (needs cluster for 6 and 13) · open as of 2026-10-30

## The problem

The ISPD 2024 contest, GPU/ML-Enhanced Large Scale Global Routing, was organised by Rongjian Liang, Wen-Hao Liu and colleagues at NVIDIA. It set routing as an optimisation problem on a 3D GCell grid graph, given as a .cap resource file and a .net pin-access file. Its benchmarks are Ariane, MemPool tile, group and cluster, NVDLA, BlackParrot and TeraPool, from 0.13M to 59.3M nets, each with a sample (public) and a rank (hidden) version. The contest ended in March 2024; the hidden benchmarks were released on 2024-03-26 and the evaluator is public. Quality is a single cost: wirelength cost + via cost + an exponential overflow penalty, with unit wire, via and per-layer overflow costs read from the .cap file. The best published scores, from Xiao, Lin, Liu, Duan, Ho and Young (InstantGR, IEEE TCAD 45(1), Jan 2026, Table III, official evaluator), are the lower of HeLEM-GR and InstantGR 2.0 for benchmarks 0-13: 0 Ariane_sample 19655065, 1 MemPool-Tile_sample 15094708, 2 NVDLA_sample 47938219, 3 BlackParrot_sample 112149983, 4 MemPool-Group_sample 395530319, 5 MemPool-Cluster_sample 1615066379, 6 TeraPool-Cluster_sample 18468687634 (HeLEM-GR), 7 Ariane_rank 22481586, 8 MemPool-Tile_rank 13736300, 9 NVDLA_rank 42936806, 10 BlackParrot_rank 109588812, 11 MemPool-Group_rank 380869353, 12 MemPool-Cluster_rank 1771528815, 13 TeraPool-Cluster_rank 11970080776. The 2024 contest winner scored, for example, 22602876 on Ariane_rank. GANGR (Nov 2025, arXiv 2511.17665) builds on InstantGR 1.0 and reports scores within about 0.002% of it, none below the values above.

## What counts as a win

A global-routing solution file in the ISPD 2024 contest output format (GCell coordinates) for one of the 14 benchmarks above, as released by the organisers. The official ISPD 2024 evaluator (the contest's evaluation code, also redistributed as run/evaluator.cpp in cuhk-eda/InstantGR, compiled with g++ -O3 -std=c++17) must run to completion and print both 'Number of open nets : 0' and 'Number of incompleted nets : 0' (every net of the .net file present and connected: the evaluator still prints a cost when nets are missing from the file, so the second line is mandatory), and a total cost (wirelength cost + via cost + overflow cost) strictly below the value listed above for that benchmark. Direction: minimise. Runtime is not part of this criterion. The claim must also be below any later published value on the same benchmark found at claim time.

## Partial wins

- **p1:** A valid solution (0 open and 0 incompleted nets) for one of benchmarks 0-5 or 7-13 whose evaluator total cost is strictly below both HeLEM-GR's and InstantGR 1.0's published scores for that benchmark in InstantGR TCAD 2026 Table III (for example below 19716744 on Ariane_sample), but not below InstantGR 2.0's. On benchmark 6 HeLEM-GR's 18468687634 is itself the listed record, so this partial does not apply there.
- **p2:** A valid solution for benchmark 12 (MemPool-Cluster_rank) or 13 (TeraPool-Cluster_rank) whose total cost is strictly below the ISPD 2024 first-place team's score in the same table (1782191834 and 12528609838).

## How a win is checked

Fetch the .cap and .net files for the benchmark (Google Drive links on the ISPD24 contest page; record sha256). Compile the evaluator and run it on the claimed solution. Require 'Number of open nets : 0' and 'Number of incompleted nets : 0', then read 'total cost'. Calibrate by routing the bundled mempool_tile_rank case with InstantGR and checking the WL, via and overflow lines. For an independent re-check, re-implement the cost from evaluator.cpp: on each routing layer and GCell, demand = 2*wires + stacked vias; if capacity c > 0 add exp(0.5*(demand/2 - c)), if c = 0 and demand > 0 add exp(0.75*demand); multiply each layer's sum by that layer's overflow weight from the .cap; add wirelength times the unit length cost and vias times the unit via cost. Also check that every net of the .net file appears once with all pins connected. Compare with Table III of the TCAD paper. Minutes to an hour, depending on size.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://qqq1357962.github.io/pdf/instantgr2.0.pdf>

## Sources

- <https://github.com/liangrj2014/ISPD24_contest/blob/main/index.md>
- <https://research.nvidia.com/publication/2024-03_gpuml-enhanced-large-scale-global-routing-contest>
- <https://qqq1357962.github.io/pdf/instantgr2.0.pdf>
- <https://github.com/cuhk-eda/InstantGR>
- <https://raw.githubusercontent.com/cuhk-eda/InstantGR/main/run/evaluator.cpp>
- <https://arxiv.org/abs/2511.17665>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the open-source InstantGR solution and run long CPU rip-up-and-reroute with negotiated congestion focused on the remaining overflow, which is often 30-40% of the cost on these cases.
- Layer assignment is where HeLEM-GR and InstantGR differ (HeLEM-GR has fewer overflows, InstantGR 2.0 has fewer vias). A post-pass ILP or Lagrangian layer reassignment per 2D route can trade the two under the exact cost.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Benchmarks 0-6 are the *_sample versions and 7-13 the *_rank (hidden) versions, as numbered in InstantGR's Table I. The contest page's alpha/beta leaderboards on public benchmarks do not compare.
- The evaluator asserts that there are no open nets, but a net missing from the output file is only counted as 'incompleted' and its cost is silently left out: require both counts to be 0.
- Runtime-scaled contest scores are not comparable; use the raw total cost only.
- There may be 2026 papers newer than this check; search before claiming. Chiang et al., 'Late Breaking Results: Scalable GPU-Friendly Parallelization for Sweep-Based Maze Routing' (DAC 2025), uses the ISPD'24 benchmarks and was not checked for scores (paywalled). The ISPD 2025 contest benchmarks and its timing-weighted scores are a different problem and do not compare.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/ispd2024-global-routing-best-score.md
```

Already set up? Say `run V3R1T4S on ispd2024-global-routing-best-score`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ispd2024-global-routing-best-score`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
