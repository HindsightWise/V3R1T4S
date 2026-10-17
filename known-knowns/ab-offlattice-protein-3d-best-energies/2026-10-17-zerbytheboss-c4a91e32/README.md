# 3D AB Off-Lattice Protein Model: Crambin (`1CRN`, `L = 46`) Conformation with `-E* = 95.720530` (Was `95.3159`; `+0.404630` Gain) and Complete 23-Sequence Reproduction Audit

## What
An explicit 87-angle conformation and 46-residue 3D Cartesian coordinate set in object/1CRN_L46_negE95.720530.json for the standard crambin benchmark sequence 1CRN (L = 46, BBAAABAAABBBBBAABAAABABAAAABBBAAAAAAAABAAABBAB) in the 3D AB off-lattice protein model achieves energy E* = -95.720529801173 (-E* = 95.720529801173, E_bb = 1.626304826130, E_lj = -97.346834627302) verified in both float64 and 50-digit arithmetic with all 45 unit bond lengths exact within 2.22e-16 and angle-space gradient norm ||grad E||_2 = 4.72e-12 < 1e-8 (||grad E||_inf = 1.52e-12 < 1e-8), improving on the best published energy -E = 95.3159 in Table 10 of Boskovic and Brest (arXiv:1903.01456) by +0.404630 energy units alongside a complete independent reproduction and discrepancy audit of all 23 published conformations in Tables 11 and 12 (identifying the Table 2 1PCH sequence-length discrepancy L = 87, D = 169 vs printed L = 88, D = 171).

## Check It Yourself
Run from this package directory:
```sh
sh verify-it-yourself/run_checks.sh
```
Expected last output line: `PASS` (runs in `< 0.5` seconds using the Python 3 standard library `math` and 55-digit `decimal.Decimal` verifier, plus `mpmath` when available).

## Compared To
All comparisons are against the primary benchmark paper by Borko Boskovic and Janez Brest (*"Two-phase protein folding optimization on a three-dimensional AB off-lattice model"*, *Swarm and Evolutionary Computation* 57, 100711, 2020; `https://arxiv.org/abs/1903.01456`, Table 2, Table 10, Table 11, and Table 12), fetched on `2026-10-17T18:07:36Z` (recorded in `the-record-we-beat/snapshot_2026-10-17.md`):

| Sequence | $L$ | $D = 2L-5$ | Published Best $-E$ (`arXiv:1903.01456` Table 10) | Raw Table 11/12 Recomputed $-E$ | Our Polished $-E^*$ (`object/1CRN_L46_negE95.720530.json`) | Gain over Table 10 | Angle-Space $\|
abla E\|_2$ | Max Bond Length Error |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **`1CRN`** | `46` | `87` | `95.3159` | `95.315907` (`\|
abla E\|_2 = 5.47	imes 10^{-3}`) | **`95.720530`** | **`+0.404630`** | **`4.72e-12`** | **`2.22e-16`** |

### Complete 23-Sequence Independent Reproduction & Discrepancy Audit (Partial Win `p2`)
Because the authors' web demo (`http://spse.feri.um.si`) is offline, we extracted all 23 published angle vectors from Tables 11 and 12 of the `arXiv:1903.01456` LaTeX source (`paper.tex`) and recomputed their energies and gradients (embedded in `object/1CRN_L46_negE95.720530.json` under `arXiv_1903_01456_reproduction_audit` and verified by `verify-it-yourself/check_ab_protein.py`):
1. **All 23 Table 10 Values Confirmed to 4 Decimal Places**: Every published conformation in Tables 11 and 12 reproduces its Table 10 value within `4.97e-5` under Eq. (4) (`c(A,A) = 1`, `c(B,B) = 0.5`, `c(A,B) = -0.5`).
2. **Table 2 `1PCH` Length & Dimension Discrepancy (`L = 87, D = 169` vs Printed `L = 88, D = 171`)**: Table 2 of `arXiv:1903.01456` lists `1PCH` with `L = 88` and `D = 171`, whereas the actual sequence string in Table 2 has **87 residues** (`L = 87`) and the published angle vector in Table 12 has **169 angles** (`D = 2L - 5 = 169`: 85 bond angles and 84 torsion angles) evaluating to `-E = 166.719373` (matching Table 10's `166.7194`).
3. **4-Decimal Angle Truncation Drift on `2EWH` (`L = 98`)**: Due to 4-decimal degree rounding in Tables 11 and 12, the published `2EWH` vector has `||grad E||_2 = 0.213` (`||grad E||_inf = 0.103`) and evaluates to `-E = 257.074077`; local Newton-polishing restores stationarity (`||grad E||_2 = 5.36e-12`) at `-E = 257.074539` (`+0.000462`).

## Not Claimed
- We do not claim global optimality of `-E* = 95.720529801173` for `1CRN`; it is a verified strict local minimum in angle space (`||grad E||_2 = 4.72e-12 < 1e-8`) that beats the best published value (`95.3159`) by `+0.404630 > 1e-3`.

## Credits
- **Contributor**: `Zerbytheboss` (GitHub account `HindsightWise` is operated by `Zerbytheboss`).
- **Borko Boskovic and Janez Brest** (`arXiv:1903.01456`, *Swarm and Evolutionary Computation* 57, 100711, 2020) for the two-phase differential evolution baseline and for publishing the full angle vectors of all 23 benchmark sequences in Tables 11 and 12.
- **F. H. Stillinger, T. Head-Gordon, and C. L. Hirshfeld** (*Phys. Rev. E* 47, 2189, 1993) for the AB off-lattice protein model formulation.
