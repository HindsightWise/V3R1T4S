# CRITERION skeptic

context: subagent (fresh context; saw only this package, kit/ docs and the target file known-unknowns/algorithms/fmm-additive-complexity-records.md)

## Literal check
- Format <2,3,8>: max dim <= 8. OK.
- Rank: live fmm_sota.json lists [2, 3, 8] rank 40; object has m=40. Equal, not lower. OK.
- Over Z, ternary: package check_slp.py and brent_check.py (stdlib) pass: tensor exact (output order C^T), all coefficients +-1, straight-line order, 2304 Brent equations. Negative control rejected. OK.
- Count under reduced convention: U 12 + V 33 + W 52 = 97 < 98 strictly. OK.

verdict: PASS

confirmed_scope: The ternary straight-line program object/2x3x8_m40_cr97_ZT_reduced.json computes the <2,3,8> matrix product exactly over Z at rank 40 (the best rank in fmm_sota.json) using 97 additions/subtractions under Perminov's reduced convention, strictly fewer than the 98 of the best file for 2x3x8 at rank 40 in Perminov's live addition_reduced_ZT directory on 2026-10-17, with no lower count on the Lille page or in COVERAGE.md; no claim of optimality or of other formats.

pass: true
