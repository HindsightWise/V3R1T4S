# `<2,3,8>` rank-40 matrix multiplication in 97 additions (was 98 in live table))

## What this is

A straight-line program that multiplies a 2x3 matrix `A` by a 3x8 matrix `B` over the integers using **40 scalar multiplications** (the best known rank for `<2,3,8>`) and **97 additions/subtractions** (`12` on the inputs of `A`, `33` on the inputs of `B`, `52` when assembling the entries of `C`), with all coefficients in `{-1, 0, +1}`. The live table record for `<2,3,8>` at rank 40 in Perminov's `addition_reduced_ZT` collection is **98** additions (`13 + 33 + 52`).

| Format | Rank `m` | `U` adds | `V` adds | `W` adds | Total reduced additions |
|---|---:|---:|---:|---:|---:|
| `<2,3,8>` (Perminov live `2x3x8_m40_cr98_cn193_ZT_reduced.json`) | 40 | 13 | 33 | 52 | **98** |
| `<2,3,8>` (`object/2x3x8_m40_cr97_ZT_reduced.json`) | 40 | 12 | 33 | 52 | **97** |

## Verify in 5 seconds

```sh
sh verify-it-yourself/run_checks.sh
```

Needs only `python3` (standard library). It checks the file's SHA-256 against `INDEX.csv`, expands the straight-line program, checks all `2304` Brent equations over `Z` and random integer matrix products, confirms every expanded coefficient is in `{-1, 0, 1}`, confirms the reduced addition count is `12 + 33 + 52 = 97`, and checks that flipping one sign makes both checkers fail. Output is in `verify-it-yourself/RECEIPTS.md`.

## Files

- `object/2x3x8_m40_cr97_ZT_reduced.json` — the straight-line program (Perminov JSON layout; output `C` indexed `(k, i)` as in Perminov's files).
- `INDEX.csv` — target id, cell, 97 vs 98, fetch timestamp, file path, sha256.
- `verify-it-yourself/` — two independent stdlib-only checkers (`check_slp.py`, `brent_check.py`), `run_checks.sh`, and `RECEIPTS.md`.
- `the-record-we-beat/README.md` — URLs, UTC timestamps, HTTP codes and SHA-256 hashes of the live sources fetched on 2026-10-17.
- `how-we-built-it/` — walk script (`flip4.py`), helper (`lib.py`, `mk.py`), algebraic DAG exclusive-cone reduction (`dag_cone_collapse.py`), and pre-registration note.
- `HOW_WE_FOUND_IT.md`, `RUN_IT_YOURSELF.md` — short overview and commands.
- `panel/` — outputs of the four review steps (`reproduce.md`, `novelty.md`, `criterion.md`, `gate.md`).
- `SHA256SUMS` — SHA-256 of every file in this folder.

## Not claimed

- No improvement to multiplicative rank (`40` is already the best known rank for `<2,3,8>`).
- No proof that 97 is the minimum possible addition count for `<2,3,8>` at rank 40.
- IACR ePrint 2026/849 (Mårtensson and Stankovski Wagner) could not be read by the panel or maintainers (its PDF is behind an interactive challenge page); the comparison here stands against Perminov's live repository (`98`), the Lille catalogue, and `COVERAGE.md`; note that the margin is a single addition (97 vs 98).
- Only `<2,3,8>` at rank 40 is claimed here.

## Credits

- **Contributor**: `Zerbytheboss` (GitHub account `HindsightWise` is operated by `Zerbytheboss`; submitted via the V3R1T4S contribution kit).
- **Prior work on the target and tools**:
  - **D. Perminov**, [`FastMatrixMultiplication`](https://github.com/dronperminov/FastMatrixMultiplication) (the `2x3x8_m40_cr98_cn193_ZT_reduced.json` baseline scheme and JSON format) and [`ternary_addition_reducer`](https://github.com/dronperminov/ternary_addition_reducer).
  - **A. Sedoglavic**, [`fmm_digest`](https://github.com/sedoglavic/fmm_digest) and the [Lille FMM table](https://fmm.univ-lille.fr/2x3x8.html).
  - **Solven / `matmulcatalog`**, [`COVERAGE.md`](https://github.com/solven-eu/matmulcatalog).
  - **M. Kauers and J. Moosbauer** (flip-graph method for matrix multiplication schemes, ISSAC 2023), **Boyar and Peralta** (cancellation-guided linear program search), **Bshouty / Kaminski / Kirkpatrick** (transposition principle for linear straight-line programs), and **A. Sedoglavic** (whom the Lille catalogue notes for the Kronecker product construction `<2,3,8>:40 = <2,3,4>:20 (x) <1,1,2>:2`).
