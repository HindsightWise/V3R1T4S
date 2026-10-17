# Criterion Skeptic Audit (`ab-offlattice-protein-3d-best-energies`)

context: subagent (fresh invocation)
target_id: ab-offlattice-protein-3d-best-energies
confirmed_scope: An explicit 87-angle conformation and 46-residue 3D Cartesian coordinate set in object/1CRN_L46_negE95.720530.json for the standard crambin benchmark sequence 1CRN (L = 46, BBAAABAAABBBBBAABAAABABAAAABBBAAAAAAAABAAABBAB) in the 3D AB off-lattice protein model achieves energy E* = -95.720529801173 (-E* = 95.720529801173, E_bb = 1.626304826130, E_lj = -97.346834627302) verified in both float64 and 50-digit arithmetic with all 45 unit bond lengths exact within 2.22e-16 and angle-space gradient norm ||grad E||_2 = 4.72e-12 < 1e-8 (||grad E||_inf = 1.52e-12 < 1e-8), improving on the best published energy -E = 95.3159 in Table 10 of Boskovic and Brest (arXiv:1903.01456) by +0.404630 energy units alongside a complete independent reproduction and discrepancy audit of all 23 published conformations in Tables 11 and 12 (identifying the Table 2 1PCH sequence-length discrepancy L = 87, D = 169 vs printed L = 88, D = 171).

## Clause-by-Clause Verification Against `targets.json`

1. **Benchmark Sequence Identity & Angle / Coordinate Representation**:
   - The target requires bond and torsion angles (or Cartesian coordinates with all bond lengths equal to `1` within `1e-9`) for one of the 23 benchmark sequences exactly as listed in `arXiv:1903.01456` Table 2.
   - `object/1CRN_L46_negE95.720530.json` provides the exact 46-residue sequence string `BBAAABAAABBBBBAABAAABABAAAABBBAAAAAAAABAAABBAB` for `1CRN` (`L = 46`), 87 internal angles (`D = 2L - 5 = 87`: 44 bond angles `theta_i` and 43 torsion angles `beta_i` in both radians and degrees), and 46 3D Cartesian coordinates rebuilt via Eq. (3) of `arXiv:1903.01456`.
   - Maximum deviation of any of the 45 consecutive bond lengths from `1.0` is `2.220446049250313e-16`, strictly below the `1e-9` threshold.
   - Maximum discrepancy between the stored Cartesian coordinates and coordinates freshly reconstructed from `angles_rad` via Eq. (3) is below `1e-14`.

2. **Energy Formula, Sign Convention, High-Precision Confirmation, and Margin (`-E* > B + 1e-3`)**:
   - Using the exact 3D AB off-lattice energy function (`E = E_bb + E_lj` with excluded sum over `|i - j| >= 2` and coefficients `C(A,A) = 1.0`, `C(B,B) = 0.5`, `C(A,B) = C(B,A) = -0.5`), the conformation achieves `E* = -95.72052980117259` (`-E* = 95.72052980117259`) in IEEE 754 `float64`. Note: in the decomposed terms of `object/1CRN_L46_negE95.720530.json`, `E_bb = 1.626304826130` and `E_lj = -97.346834627302` sum to the exact verified total `E* = -95.720529801173`.
   - High-precision 50-digit evaluation using both 55-digit `decimal.Decimal` and `mpmath` (`mp.dps = 50`) confirms `-E* = 95.72052980117259...` with `float64` agreement within `1e-12`.
   - The largest published `-E` for `1CRN` in Table 10 of Boskovic and Brest (`arXiv:1903.01456`, *Swarm and Evolutionary Computation* 57, 100711, 2020) and in the literature for this exact model is `B = 95.3159` (`95.315913` when recomputed from the 4-decimal degree angles in Table 11).
   - The improvement is `+0.404630` energy units (`-E* - B = 0.404629801173`), exceeding the required `1e-3` threshold by a factor of `404.6x`.

3. **Strict Local Minimum in Angle Space (`||grad E|| < 1e-8`)**:
   - The analytical angle-space gradient has Euclidean norm `||grad E||_2 = 4.718e-12` and infinity norm `||grad E||_inf = 1.519e-12`, both strictly below `1e-8`.
   - Independent 4th-order Richardson central finite-difference numerical differentiation (`h = 1e-4`) confirms `||grad_num E||_2 = 3.254e-9 < 1e-8` with maximum componentwise discrepancy `1.456e-9`.
   - Furthermore, the 87x87 symmetric angle-space Hessian matrix is strictly positive-definite at this point (`lambda_min = 0.170707 > 0`, `lambda_max = 8930.075721`), certifying a true strict local minimum rather than a saddle point.

4. **Partial Win `p2` (Complete 23-Sequence Independent Reproduction & Discrepancy Audit)**:
   - All 23 published angle vectors from Tables 11 and 12 of `arXiv:1903.01456` were extracted from the primary LaTeX source (`paper.tex`) and independently evaluated under the exact Eq. (3)-(4) model, matching every Table 10 energy within `4.97e-5`.
   - The audit identifies and proves the Table 2 `1PCH` sequence-length and dimension discrepancy: Table 2 prints `L = 88, D = 171`, whereas the actual sequence string in Table 2 has `L = 87` residues and the published angle vector in Table 12 has `D = 169` angles (`85` bond + `84` torsion), which evaluates to `-E = 166.719373` matching Table 10's `166.7194`.

5. **Hidden Quantifiers, Pitfalls, and Null / Corruption Checks**:
   - All five listed pitfalls in `targets.json` were audited: 3D model without extra torsion potential, unit bond lengths exact to machine precision (`2.22e-16`), excluded pair sum strictly over `|i - j| >= 2`, exclusion of Kolossvary's incompatible CCD variant, and proper sign convention (`-E* > B + 1e-3`).
   - Running `sh verify-it-yourself/run_checks.sh` exits `0` and prints `PASS`, and corrupting a digit of the object file causes the verifier to reject the corrupted file.

pass: true
