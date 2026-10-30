# 🛠️ Engineering and chips

Chip placement, routing and logic-synthesis benchmarks, aerodynamic, energy and structural design cases with published best results.

**8 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★☆☆ | [IEA Wind Task 37 case study 1: a feasible 16-, 36- or 64-turbine circular-farm layout wit…](iea37-cs1-circular-wind-farm-layout.md) | harvest | laptop-hours (one AEP evaluation is about 1 ms; multistart gradient or large-neighbourhood search) |
| ★★★☆☆ | [invrs-gym photonic inverse design: a manufacturable design beating the frozen invrs leade…](invrs-leaderboard-photonic-pareto.md) | harvest | laptop-hours (JAX; FMMAX RCWA or ceviche FDFD per evaluation; a GPU helps for metalens and Bayer sorter) |
| ★★☆☆☆ | [ICCAD 2022 CAD Contest Problem B (3D placement with D2D vertical connections): a shorter…](iccad2022-3d-placement-d2d-wirelength.md) | harvest | laptop-hours (2.7k to 221k cells); the evaluator runs in seconds to minutes |
| ★★☆☆☆ | [ICCAD 2023 CAD Contest Problem B (3D placement with macros): a lower HPWL + 10 x HBT scor…](iccad2023-3d-mixed-size-placement-score.md) | harvest | laptop-hours (14k to 740k instances, 6 to 34 macros); the evaluator runs in minutes |
| ★★☆☆☆ | [IEA Wind Task 37 case study 4 (Borssele III/IV, 81 x 10 MW): a feasible layout with highe…](iea37-cs4-borssele-81-turbine-layout.md) | standard | laptop-hours (vectorised AEP about 0.1 s for 81 turbines x 360 directions x 20 speeds) |
| ★★☆☆☆ | [ISPD 2024 large-scale global routing benchmarks: a lower official evaluator cost than the…](ispd2024-global-routing-best-score.md) | harvest | laptop-hours for benchmarks 0-4 and 7-11 (up to 3.3M nets, 64 GB RAM helps); the 10.6M and 59.3M-net cases need a large-memory machine (needs cluster for 6 and 13) |
| ★★☆☆☆ | [ISPD 2026 contest (post-placement buffering and sizing): a result that dominates the per-…](ispd2026-buffering-sizing-dominance.md) | standard | laptop-hours to laptop-days per design (OpenROAD global route and OpenSTA on 0.1M to 1M-instance ASAP7 designs; evaluation flows of 10 to 1,700 s) |
| ★★☆☆☆ | [ESA GTOP / GTOPX interplanetary trajectory benchmarks: beat a best-known Delta-v, mass or…](gtopx-interplanetary-trajectory-records.md) | harvest | laptop-days (millions to billions of objective evaluations; each about 10 microseconds in C) |

← [All categories](../README.md)
