# Receipts

Real output of `sh verify-it-yourself/run_checks.sh` from this package folder (with the date, platform, compiler and
Python version printed before it and the timing after it):

```
2026-10-24T23:39:08Z
Darwin arm64
Apple clang version 21.0.0 (clang-2100.1.1.101)
Python 3.14.7
n=33 s=48 c=18 k=3 dim_isotropic=12 dim_dual=18
{"n": 33, "s": 48, "c": 18, "k": 3, "dim_perp": 18, "dim_isotropic": 12, "D9_herm_orthogonal_to_G9": true, "rowspace_S_equals_phi_D9": true}
n=33 s=48 c=18 k=3 dim_N=18 dim_I=12 N_closed_under_w=True
kappa=9 (2*kappa == dim_N: True)
wrote verify-it-yourself/tmp_work/G9.txt
kappa=9 n=33 m=14 part=0/3 subsets=426862095 deficient=0 (expected subsets in all parts C(n,m)=818809200)
kappa=9 n=33 m=14 part=1/3 subsets=249420648 deficient=0 (expected subsets in all parts C(n,m)=818809200)
kappa=9 n=33 m=14 part=2/3 subsets=142526457 deficient=0 (expected subsets in all parts C(n,m)=818809200)
T=[0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 18, 19, 21, 22, 23, 24, 26, 28, 30, 31]
v_x=1 1 2 2 1 0 1 1 0 1 0 1 0 0 0 0 0 0 1 2 0 1 2 2 1 0 1 0 1 0 1 1 0
v_z=1 2 0 1 1 1 2 0 0 2 0 2 0 0 0 0 0 0 2 0 0 2 0 2 1 0 0 0 2 0 1 2 0
symplectic_weight=20 orthogonal_to_all_rows_of_S=True in_span_S=False support=[0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 18, 19, 21, 22, 23, 24, 26, 28, 30, 31]
GF(729) modulus u^3 + 2 u^2 + 0 u + 1 over GF(9); i = 4; 27 affine points; 288 degree-3 places
L1: rank S = 48, dim phi(C) = 18, 2n - rank S = 18, phi(C) orthogonal to S: True -> span(S)^perp = phi(C): True
L2: 9 columns unscaled by w^-1 (pattern +-++++++--+++++++-++-+++++---+++-)
L3: K = 9, rank(head) = 9 (injective: True), dim zero-tail subcode = 6, rank(tail) = 3
L4: place #265 (point x0 = 514, y0 = 536 in this GF(729) coding): head code = C_L(D_28, 4Q + -1P_inf) (dim 9), zero-tail code = C_L(D_28, 3Q + -1P_inf) (dim 6): True
L4: 1 of 288 places identify both codes
L5: Goppa bounds d(head code) >= 28 - 11 = 17, d(zero-tail code) >= 28 - 8 = 20
L6: tail code dimension 3, all 10 maximal minors nonzero: True -> d(tail) = 3
L7: d(C) >= min(20, 17 + 3) = 20, so d_EA >= 20
L8: witness weight 20, in C: True, phi(witness) orthogonal to S: True, outside span(S): True
RESULT: d_EA = 20 exactly (theorem-based; no distance search): True
ok:   parameters computed from S
ok:   computed n=33 s=48 c=18 k=3; claimed n=33 k=3 c=18
ok:   GF(9) description consistent with S
ok:   span(S)^perp is closed under w (GF(9)-linear, dimension 2 kappa)
ok:   the two parameter computations agree
ok:   all parts of the m=14 information-set test present
ok:   test run on the code recovered from S (kappa=9)
ok:   examined 818809200 of C(33,14) = 818809200 coordinate subsets
ok:   every 14 coordinates hold an information set (deficient subsets: 0), so d >= 20
ok:   witness of symplectic weight 20 outside span(S), claimed d=20
computed d=20; claimed d=20
PASS
real 2.14
user 2.05
sys 0.24
```
