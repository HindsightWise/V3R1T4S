# V3R1T4S Reproduction Panel Audit (`reproduce.md`)

context: subagent (fresh invocation)
target_id: ab-offlattice-protein-3d-best-energies
cell: 1CRN
claimed_value: 95.720530
table_value: 95.3159

## 1. Quoted Mathematical Definition (`arXiv:1903.01456`, Eqs. 1-4)

Before reading `verify-it-yourself/check_ab_protein.py`, an independent checker was written directly from the mathematical specification in Borko Boskovic and Janez Brest (*"Two-phase protein folding optimization on a three-dimensional AB off-lattice model"*, *Swarm and Evolutionary Computation* 57, 100711, 2020; `arXiv:1903.01456`, Section 2, Eqs. 1-4):

- **Internal-to-Cartesian Coordinate Reconstruction (Eq. 1 / Eq. 3)**:
  For a chain of $L$ monomers parameterized by $D = 2L - 5$ internal angles $(\theta_1, \dots, \theta_{L-2}, \beta_1, \dots, \beta_{L-3})$:
  $$
  (x_i, y_i, z_i) = \begin{cases}
  (0, 0, 0), & i = 1 \\
  (0, 1, 0), & i = 2 \\
  (\cos\theta_1, 1 + \sin\theta_1, 0), & i = 3 \\
  (x_{i-1} + \cos\theta_{i-2}\cos\beta_{i-3}, \; y_{i-1} + \sin\theta_{i-2}\cos\beta_{i-3}, \; z_{i-1} + \sin\beta_{i-3}), & 4 \le i \le L
  \end{cases}
  $$
- **Potential Energy Function (Eqs. 2-4)**:
  $$
  E = \frac{1}{4}\sum_{i=1}^{L-2} (1 - \cos\theta_i) + 4 \sum_{i=1}^{L-2}\sum_{j=i+2}^{L} \left(r_{ij}^{-12} - c(\sigma_i, \sigma_j) r_{ij}^{-6}\right)
  $$
  where $r_{ij}$ is the Euclidean distance between monomers $i$ and $j$, and the hydrophobicity coupling coefficients (Eq. 4) are:
  $$
  c(\sigma_i, \sigma_j) = \begin{cases}
  +1, & \sigma_i = A \text{ and } \sigma_j = A \\
  +0.5, & \sigma_i = B \text{ and } \sigma_j = B \\
  -0.5, & \sigma_i \neq \sigma_j
  \end{cases}
  $$

## 2. Independent Verification Results on `object/1CRN_L46_negE95.720530.json`

1. **File Integrity & Sequence Verification**:
   - `INDEX.csv` SHA-256 matches `object/1CRN_L46_negE95.720530.json` exactly (`d054b7b75b76901250d2498f30d4e53b374e4e7fc2e2e5db21b3fadd1cb64c00`).
   - Sequence for `1CRN` is `BBAAABAAABBBBBAABAAABABAAAABBBAAAAAAAABAAABBAB` with length $L = 46$ and angle count $D = 2L - 5 = 87$ ($n_\theta = 44$, $n_\beta = 43$), matching Table 2 of `arXiv:1903.01456`.

2. **Coordinate Reconstruction & Unit Bond Lengths**:
   - Reconstructing the 46 Cartesian points in `float64` from `angles_rad` matches the stored `coordinates_xyz` array in `object/1CRN_L46_negE95.720530.json` with maximum coordinate deviation `0.0`.
   - All $L - 1 = 45$ consecutive bond lengths satisfy $\|p_{i+1} - p_i\|_2 = 1.0$ with maximum error `2.220446049250313e-16` in `float64` (well within the `1e-9` tolerance) and `2.67276e-51` in 50-digit `mpmath` arithmetic.

3. **Energy Evaluation (`float64`, 55-Digit `Decimal`, and 50-Digit `mpmath`)**:
   - Independent `float64` evaluation gives:
     - $E_{\text{bb}} = 1.626304826129858$
     - $E_{\text{LJ}} = -97.346834627302442$
     - $E^* = -95.720529801172589$ (`-E* = 95.720529801172589`, rounding to `95.720530`).
   - Independent 50-digit `mpmath` evaluation gives `-E* = 95.720529801172517389569617551`, agreeing with `float64` to `7.16e-14` (well within `1e-12`).
   - Compared against the Table 10 published best value `-E = 95.3159` (`gDE`), the improvement is `+0.404629801173` (and `+0.404616599493` over the unrounded Table 11 evaluation `95.315913201680`), exceeding the required `1e-3` threshold by a factor of `404.6x`.

4. **Stationarity & Positive-Definite Hessian (Strict Local Minimum)**:
   - Independent analytic angle-space gradient gives $\|\nabla E\|_2 = 4.703809 \times 10^{-12}$ (`4.717875e-12` in `check_ab_protein.py`) and $\|\nabla E\|_\infty = 1.518525 \times 10^{-12}$, both well below the `1e-8` stationarity requirement.
   - The $87 \times 87$ angle-space Hessian matrix $H = \nabla^2 E$ evaluated at `angles_rad` has all 87 eigenvalues strictly positive ($\lambda_{\min}(H) = 0.170707$, $\lambda_{\max}(H) = 8930.075703$), confirming a strict local minimum.

5. **Exhaustive 23-Sequence Reproduction & `1PCH` Discrepancy Audit**:
   - Independently re-evaluating all 23 published angle vectors from Tables 11 and 12 in `arXiv_1903_01456_reproduction_audit` confirms every Table 10 energy within `4.375216e-5` (under `5e-5`).
   - Verified the Table 2 vs Table 12 discrepancy for `1PCH`: the actual sequence string in Table 2 has length $L_{\text{actual}} = 87$ (printed as $L = 88$ in Table 2) and the published angle vector in Table 12 has $D_{\text{actual}} = 2(87) - 5 = 169$ angles (printed as $D = 171$ in Table 2), evaluating to `-E = 166.719373` (matching Table 10's `166.7194`).

## 3. Execution of `verify-it-yourself/run_checks.sh`

Running `sh verify-it-yourself/run_checks.sh` from the package root completed in under `0.5` seconds with exit code `0` and output:
```text
Verified 1CRN (L=46, D=87): -E* = 95.720529801173 (Table 10 = 95.3159, gain = +0.404630)
Precision check: 50-digit Decimal verified
Max bond length error: 2.220e-16 (within 1e-9)
Analytical ||grad E||_2 = 4.718e-12, ||grad E||_inf = 1.519e-12 (within 1e-8)
Numerical  ||grad E||_2 = 3.254e-09, max |g_ana - g_num| = 1.456e-09
Verified all 23 arXiv:1903.01456 Table 11/12 conformations + 1PCH L=87/D=169 discrepancy.
PASS
```

pass: true
