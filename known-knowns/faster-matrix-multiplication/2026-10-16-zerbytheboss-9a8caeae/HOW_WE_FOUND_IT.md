# How we found it

Contributor text, unverified.

An agent working for the contributor started from Perminov's rank-40 `<2,3,8>` scheme (`2x3x8_m40_cr98_cn193_ZT_reduced.json`, 98 reduced additions). It walked the space of rank-40 ternary schemes using flip-graph moves combined with ternary-preserving isotopy moves (elementary row and column additions/subtractions on the three factor matrices `U`, `V`, `W`), coupled with Boyar-Peralta cancellation-guided common-subexpression elimination on `U`, `V`, and `W^T` (transposed back via the transposition principle `cost(W) = cost(W^T) + r - n*p`) and canonical binary DAG exclusive-cone reduction (`dag_cone_collapse.py`), reaching **97** reduced additions (`U 12 + V 33 + W 52 = 97`).

Before claiming, Perminov's live tree listing, `reduced_known.json`, `README.md`, `CHANGELOG.md`, the Lille `<2,3,8>` page, `COVERAGE.md`, and `fmm_sota.json` were fetched once each, and all open and closed pull requests of this repository were checked.
