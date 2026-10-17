# The record we beat (metadata only)

Each row is one honest GET (Python `urllib.request`, User-Agent naming V3R1T4S, no retries) made by the author. No page is copied here.

| Source | URL | UTC fetch time | HTTP | sha256 | Extracted cell |
|---|---|---|---|---|---|
| tree.json | https://api.github.com/repos/dronperminov/FastMatrixMultiplication/git/trees/master?recursive=1 | 2026-10-17T06:16:24Z | 200 | 0cb3669d76a7e34604a34d2a204c0bf4e27525ba5348675bea6605d7e7032fab | addition_reduced_ZT files for 2x3x8 rank 40: minimum cr 98 (2x3x8_m40_cr98_cn193_ZT_reduced.json) |
| reduced_known.json | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/reduced_known.json | 2026-10-17T06:16:24Z | 200 | ef67c13792b0e770578de4ff01438178ce4e6ac4efd60a3580f3131e31907a5d | no 2x3x8 rank-40 entry |
| README.md | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/README.md | 2026-10-17T06:16:24Z | 200 | 7b0761ecc0fa1988cb2ef0efeca503af974eeb6ade76d30629308ebba7e78341 | 2x3x8 rank 40 listed; no lower addition count stated |
| CHANGELOG.md | https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/CHANGELOG.md | 2026-10-17T06:16:24Z | 200 | 07fbb3249d1213b95d9a9c3069d208c0c3b4390a6b87c71325af64a2d56cd175 | no lower count for 2x3x8 |
| lille_2x3x8.html | https://fmm.univ-lille.fr/2x3x8.html | 2026-10-17T06:16:24Z | 200 | 1e98aec15a9ee7396f7e91d1c3e84a791986369dc949f429175ef71f3d40d713 | rank 40; no operation-count variant cited |
| COVERAGE.md | https://raw.githubusercontent.com/solven-eu/matmulcatalog/master/generated/COVERAGE.md | 2026-10-17T06:16:24Z | 200 | c2a9bd929b477acb44d4f92aa8055a0c26eab3c33121c0734be650c5c86254b7 | 2x3x8: best 40, adds +190 (naive count, not comparable) |
| fmm_sota.json | https://raw.githubusercontent.com/sedoglavic/fmm_digest/master/fmm_sota.json | 2026-10-17T06:16:24Z | 200 | d0da2c364dcf4d13c0721ea8b7c3dcd7fae4f6f3c843d22a714a1ccb9bd244c1 | [2, 3, 8]: rank 40 |

Compared cell: 2x3x8 at rank 40, reduced additions. Reference (minimum over Perminov's files for this format and rank): 98. This object: 97.

## Reference scheme file (not shipped: third-party data)

https://raw.githubusercontent.com/dronperminov/FastMatrixMultiplication/master/schemes/results/addition_reduced_ZT/2x3x8_m40_cr98_cn193_ZT_reduced.json (sha256 `bc4acf2848dd1b74f6d3d4790f244d3bbfed8b5a1eba65334164ed20d5f6c1e0`); running `verify-it-yourself/check_slp.py` on it reports 98 (`adds_U: 13, adds_V: 33, adds_W: 52`).

## V3R1T4S pull requests

Searched all open and closed pull requests of elder-plinius/V3R1T4S on 2026-10-17: none claims `<2,3,8>` (or any permutation).
