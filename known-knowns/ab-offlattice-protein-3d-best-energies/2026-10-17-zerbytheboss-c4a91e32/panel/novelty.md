# Panel Skeptic Audit: NOVELTY (`ab-offlattice-protein-3d-best-energies`)

- `role`: novelty
- `context`: subagent (fresh invocation)
- `target_id`: `ab-offlattice-protein-3d-best-energies`
- `audited_utc`: `2026-10-17T18:31:06Z`

## 1. Single Honest HTTP Fetch of Primary Sources (No Retries)

Using Python `urllib.request.urlopen` (single request per URL, zero retries) at `2026-10-17T18:31:06Z`:

1. **Primary Benchmark Source (`https://arxiv.org/abs/1903.01456`)**:
   - **URL**: `https://arxiv.org/abs/1903.01456` (Borko Boskovic and Janez Brest, *"Two-phase protein folding optimization on a three-dimensional AB off-lattice model"*, *Swarm and Evolutionary Computation* 57, 100711, 2020; arXiv v2)
   - **HTTP Status**: `200` (`45286` bytes, SHA-256 `1a178222fad8fef2262b7cd71c6edbaaf9534e908cf6bfefadb7b6ff4ee9d847`)
   - **Fetched UTC**: `2026-10-17T18:31:06Z`
   - **Quoted Table 10 & Table 11 Record for Crambin (`1CRN`, `L = 46`, `D = 87`)**:
     - Table 10 reports best `-E` values across three algorithms (`alg1 = 93.4525`, `alg2 = 91.6746`, `gDE = 95.3159`); the best published value is `-E = 95.3159` (`E = -95.3159`).
     - Table 11 gives the explicit 87-angle vector in degrees (rounded to 4 decimal places), which evaluates under Eq. (4) to `-E = 95.315913201680` (`E_bb = 1.740989073327`, `E_lj = -97.056902275007`, angle-space gradient norm `||grad E||_2 = 1.62e-2`).

2. **Cambridge Cluster Database Archive (`https://www-wales.ch.cam.ac.uk/~wales/CCD/Protein_AB_models_by_Istvan_Kolossvary.txt`)**:
   - **URL**: `https://www-wales.ch.cam.ac.uk/~wales/CCD/Protein_AB_models_by_Istvan_Kolossvary.txt` (Istvan Kolossvary and Kevin J. Bowers, `arXiv:1205.4705v1`, 21 May 2012)
   - **HTTP Status**: `200` (`28483` bytes, SHA-256 `7886fe931fe22ba80f2d33b8abf21e7acacbd4f9ffe3a21fc7ab7d1ea3e1b0e6`)
   - **Fetched UTC**: `2026-10-17T18:31:06Z`
   - **Scope Check**: Contains putative minimum folds for Fibonacci-length binary chains (`L = 13, 21, 34, 55, 89`) and optimal sequence design; it does not contain a `1CRN` (`L = 46`) conformation beating `95.3159`.

## 2. Literature, Trophy Case, and Pull Request Audit

1. **Last 24 Months of Literature (2024-2026)**:
   - Searched 2024-2026 literature and citations of Boskovic and Brest (`arXiv:1903.01456` / *Swarm and Evolutionary Computation* 57, 100711, 2020) for 3D AB off-lattice protein model results on `1CRN` (`L = 46`, sequence `BBAAABAAABBBBBAABAAABABAAAABBBAAAAAAAABAAABBAB`).
   - No paper in the last 24 months (or any prior publication) reports a 3D AB off-lattice energy for `1CRN` improving on `-E = 95.3159` from Table 10 of `arXiv:1903.01456`.

2. **Repository `TROPHY_CASE.md`**:
   - Inspected all 53 rows of `TROPHY_CASE.md` across the existing result families (`degree-diameter`, `constant-weight-codes`, `lehmer`, `fast-matrix-multiplication`, `sealed-envelopes/bouchaudy-cipher-machines`, `vnncomp-2026`, `robustbench-cifar100`).
   - Confirmed `0` existing entries for `ab-offlattice-protein-3d-best-energies` or `1CRN`.

3. **Open and Merged Pull Requests on `elder-plinius/V3R1T4S`**:
   - Queried `https://api.github.com/repos/elder-plinius/V3R1T4S/pulls?state=all&per_page=100` across pages 1 to 3 (300 total open/closed/merged PRs).
   - Confirmed `0` open, closed, or merged pull requests targeting `ab-offlattice-protein-3d-best-energies` or `1CRN`.

## 3. Strict Improvement Verification

- **Artifact**: `object/1CRN_L46_negE95.720530.json` (SHA-256 `d054b7b75b76901250d2498f30d4e53b374e4e7fc2e2e5db21b3fadd1cb64c00`, matching `INDEX.csv` and `the-record-we-beat/snapshot_2026-10-17.md`).
- **Published Best Record (`arXiv:1903.01456` Table 10)**: `-E = 95.3159` (unrounded Table 11 evaluation: `-E = 95.315913201680`).
- **Our Conformation Value**: `-E* = 95.720529801173` (`E* = -95.720529801173`, `E_bb = 1.626304826130`, `E_lj = -97.346834627302`), with angle-space gradient norm `||grad E||_2 = 4.72e-12` (well below `1e-8`), `||grad E||_inf = 1.52e-12` (well below `1e-8`), and maximum bond-length deviation `2.22e-16`.
- **Strict Margin**:
  - Gain over Table 10 (`95.3159`): `+0.404629801173` (`+0.404630` energy units, exceeding the `1e-3` threshold by a factor of `404.6x`).
  - Gain over unrounded Table 11 (`95.315913201680`): `+0.404616599493` energy units.
- **Partial Win `p2` Audit**: All 23 published angle vectors from Tables 11 and 12 of `arXiv:1903.01456` are independently recomputed and audited inside `object/1CRN_L46_negE95.720530.json`, documenting both the Table 2 `1PCH` sequence-length discrepancy (`L = 87, D = 169` actual vs `L = 88, D = 171` printed) and the 4-decimal rounding drift on `2EWH`.

pass: true
