# Run It Yourself

## 1. Verify the Claimed `1CRN` Conformation (`-E* = 95.720530`) and 23-Sequence Audit
From the package root, run:
```sh
sh verify-it-yourself/run_checks.sh
```
This executes `verify-it-yourself/check_ab_protein.py` using only the Python 3 standard library (`math` and 55-digit `decimal.Decimal`, plus `mpmath` if installed) in `< 0.5` seconds, verifying:
- Exact sequence string for `1CRN` (`L = 46`, `D = 87`),
- Exact 3D coordinate reconstruction with all 45 bond lengths equal to `1.0` within `2.22e-16 < 1e-9`,
- `-E* = 95.720529801173 > 95.3159 + 1e-3` (gain `+0.404630`),
- Analytical and finite-difference gradient norms `||grad E||_2 = 4.72e-12 < 1e-8` and `||grad E||_inf = 1.52e-12 < 1e-8`,
- Complete reproduction of all 23 published conformations from Tables 11 and 12 of `arXiv:1903.01456`.

## 2. Compile the C++17 Basin-Hopping & Newton-Raphson Solver
```sh
clang++ -O3 -std=c++17 -march=native -pthread how-we-built-it/AB_Protein_Hunter.cc -o AB_Protein_Hunter
```
