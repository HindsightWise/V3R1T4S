# NOVELTY skeptic

context: subagent (fresh context; saw only this package and kit docs)

verdict: PASS

## Live fetches (2026-10-17T06:16:24Z, single GET each, no retries)

1. `https://api.github.com/repos/dronperminov/FastMatrixMultiplication/git/trees/master?recursive=1` — HTTP 200, sha256 `0cb3669d76a7e34604a34d2a204c0bf4e27525ba5348675bea6605d7e7032fab`. Minimum reduced addition count for `2x3x8` at rank 40: **98** (`2x3x8_m40_cr98_cn193_ZT_reduced.json`, sha256 `bc4acf2848dd1b74f6d3d4790f244d3bbfed8b5a1eba65334164ed20d5f6c1e0`, recounted by `check_slp.py` as `adds_U=13, adds_V=33, adds_W=52, adds_total=98`). Checked `reduced_known.json`, `README.md`, and `CHANGELOG.md`: no count below 98 for `2x3x8` at rank 40.
2. `https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json` — HTTP 200, sha256 `d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1`. Lists `[2, 3, 8]` with `"rank": 40`.
3. `https://fmm.univ-lille.fr/2x3x8.html` — HTTP 200, sha256 `1e98aec15a9ee7396f7e91d1c3e84a791986369dc949f429175ef71f3d40d713`. Lists `(2x3x8 : 40)` with no operation-count variant.
4. `https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md` — HTTP 200, sha256 `c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7`. Lists naive count `+190`.
5. `TROPHY_CASE.md` and `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=all&per_page=100` — HTTP 200. No open or closed pull request on `elder-plinius/V3R1T4S` claims `<2,3,8>` (or any permutation). Note that the margin is a single addition (97 vs 98).

## Comparison

Claimed: `97` reduced additions (`12 + 33 + 52`) for `<2,3,8>` at rank `40` over `Z` (`object/2x3x8_m40_cr97_ZT_reduced.json`). Live minimum in Perminov: `98` (`97 < 98` strictly).

pass: true
