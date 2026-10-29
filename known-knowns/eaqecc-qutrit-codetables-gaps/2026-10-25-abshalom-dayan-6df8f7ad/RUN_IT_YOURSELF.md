# Run it yourself

From this package folder, in a fresh shell (needs python3, standard library only, and cc; no network):

    sh verify-it-yourself/run_checks.sh

Expected output (about 2 seconds with 3 free cores; 2.14 s measured, see verify-it-yourself/RECEIPTS.md):

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

What it does:
- gf3prep.py (standard library) computes s = rank(S), c = rank(S J S^T)/2, k = n - s + c, a basis of
  N = span(S)^perp and of the isotropic part I = span(S) ∩ N, from S alone.
- check_eaqecc.py prepare checks the object's GF(9) description (D9 is Hermitian-orthogonal to G9 and
  rowspace(S) = phi(D9)). Only its `prepare` mode is used here.
- gf9info.py prep checks that N is closed under multiplication by w (a primitive element of GF(9)), so
  N = phi(C) for a GF(9)-linear [33,9] code C recovered from S, and symplectic weight on N is Hamming weight on C.
  It writes a generator matrix of C.
- infoset.c examines every one of the C(33,14) = 818809200 sets of 14 coordinates and checks, by exact GF(9)
  ranks, that the columns of C's generator matrix on those coordinates have rank 9 (an information set). If every
  14 coordinates hold an information set, no nonzero word of C vanishes on 14 coordinates, so every nonzero word has
  weight >= 20, and every vector of N, inside or outside I, has symplectic weight >= 20: d >= 20.
- witness.py finds, inside the given 20 positions, a vector of N that is not in span(S) (so not in I), of
  symplectic weight 20: d <= 20.
- goppa_x.py is a second proof of d >= 20 that searches no codewords at all: it checks (with its own GF(9) and
  GF(729) arithmetic) that span(S)^perp = phi(C), that C is a Construction X code whose head code is exactly the
  algebraic-geometry code C_L(D_28, 4Q - P_inf) of the Hermitian curve for one of its 288 places Q of degree 3 and
  whose zero-tail code is exactly C_L(D_28, 3Q - P_inf), and that the tail code is an MDS [5,3,3] code. The Goppa
  bound (d >= 28 - deg) gives 17 and 20 for the two AG codes, and the Construction X lemma gives
  d(C) >= min(20, 17 + 3) = 20. Each step (L1-L8) is printed; the proof is written out in HOW_WE_FOUND_IT.md.
- verdict.py compares every computed value with the claim in the JSON.

Two checker files name files that are not shipped and not needed: goppa_x.py refers to the run's NOTES.md for the
proof steps (the proof is written out in HOW_WE_FOUND_IT.md), and check_eaqecc.py names enum_min.c, an exhaustive
enumerator used only by its `verdict` mode, which these checks do not run.

A third, independent exact check (a GF(3) position-subset rank test on S itself, which excludes the isotropic
part inside the test and shares no code with the first two; about 2-3 CPU-minutes per part measured on a shared,
loaded machine, 23:03:54Z to 23:14:41Z for all six parts run one at a time). For every set T of 19 positions it
compares, by exact GF(3) ranks, the dimension of the vectors of N supported inside T with that of the vectors of I
supported inside T. They are equal for every T, so no vector of N outside I has symplectic weight <= 19: d >= 20.

    python3 verify-it-yourself/gf3prep.py object/eaqecc_33_3_20_18.json basis.txt
    cc -O3 -o subset_ea64 verify-it-yourself/subset_ea64.c
    for p in 0 1 2; do ./subset_ea64 19 $p 3 < basis.txt & done; wait

Expected: three lines
`W=19 part=P/3 total_subsets=818809200 examined=272936400 with_vector_outside_isotropic=0` (P = 0, 1, 2).
With 20 in place of 19 the test finds 468 + 431 + 431 = 1330 sets of 20 positions that hold such a vector, as
many as the information-set test finds sets of 13 coordinates that are not information sets.

A fourth check (Brouwer-Zimmermann minimum distance of C, a few seconds):

    python3 verify-it-yourself/gf9info.py prep object/eaqecc_33_3_20_18.json G9.txt
    cc -O3 -o bz64 verify-it-yourself/bz64.c
    ./bz64 < G9.txt

Expected: a line beginning `K=9 n=33 d=20`.

Rebuild the object from scratch (how-we-built-it/README.md has the whole search):

    python3 how-we-built-it/build_x_lead.py 45 4 -1 4,8,6,7,5 1,8,8,0,5,7,0,3,2 +-++++++--+++++++-++-+++++---+++- rebuilt.json 20
    shasum -a 256 rebuilt.json object/eaqecc_33_3_20_18.json   # both 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961
