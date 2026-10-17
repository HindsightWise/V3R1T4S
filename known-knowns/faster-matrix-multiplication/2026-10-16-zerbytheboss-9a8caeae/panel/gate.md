status: CONFIRMED_SOLUTION
confirmed_scope: The ternary straight-line program object/2x3x8_m40_cr97_ZT_reduced.json computes the <2,3,8> matrix product exactly over Z at rank 40 (the best rank in fmm_sota.json) using 97 additions/subtractions under Perminov's reduced convention, strictly fewer than the 98 of the best file for 2x3x8 at rank 40 in Perminov's live addition_reduced_ZT directory on 2026-10-17, with no lower count on the Lille page or in COVERAGE.md; no claim of optimality or of other formats.
gate_utc: 2026-10-17T06:18:00.000000Z

REPRODUCE passed: all 2304 Brent equations hold, every expanded coefficient is in -1, 0, 1, count 97 (U 12, V 33, W 52), mutation tests all caught. NOVELTY passed: no <2,3,8> rank-40 scheme with 97 or fewer additions found in Perminov (min 98), fmm_sota.json, the Lille page, COVERAGE.md, V3R1T4S PRs, or recent literature. CRITERION passed: literal check of the live criterion, strictly fewer than 98, rank equals the best known rank 40.
