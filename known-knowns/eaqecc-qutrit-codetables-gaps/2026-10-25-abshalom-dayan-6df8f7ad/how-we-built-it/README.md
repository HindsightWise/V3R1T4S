# How we built it

Commands from this folder (python3 standard library and cc), in the order the object was found:

1. The two algebraic-geometry codes of the Hermitian curve y^3 + y = x^4 over GF(9), with Q the place of degree 3
   numbered 45 in deg3.py's list (arithmetic in GF(729); coordinates: the 27 affine points, then P_inf):

       python3 deg3.py code 45 4 -1 C1.code     # C(D_28, 4Q - P_inf) = [28,9], Goppa bound d >= 17
       python3 deg3.py code 45 3 -1 C2.code     # C(D_28, 3Q - P_inf) = [28,6], Goppa bound d >= 20
       python3 prep_x.py C1.code C2.code X11_q45_a4.xin    # byte-identical to the X11_q45_a4.xin here (sha256 196545d8...957f)

2. The exact maximum Hermitian hull of every Construction X code of this pair (all 2^27 head sign patterns, every
   [5,3,3] tail and every 3 x 3 gluing matrix; minimal-rank-completion bound, made exact by the rank classification of
   Hermitian forms; 50 seconds measured on one core):

       cc -O3 -o hullbound hullbound.c && ./hullbound bound < X11_q45_a4.xin    # bound_X11_q45_a4.txt: exact maximum 6

   Hull 6 is reached at exactly one head pattern (the "exact 6" line): +-++++++--+++++++-++-+++++--.
   The same pass over the seven other degree 11 > 8 pairs (place 0 and place 45, a = 1..4) gave exact maxima 4 or 5.

3. A tail and gluing matrix that reach hull 6 at that pattern (random tries, seed 1; try 1698 succeeds):

       ./hullbound real +-++++++--+++++++-++-+++++-- 1 200000 < X11_q45_a4.xin    # real_X11_q45_a4.txt

   Points 4, 8, 6, 7, 5; tail signs -+++- (columns 28 and 32 multiplied by w); M = 1,8,8,0,5,7,0,3,2.

4. The object (the X code, its Hermitian dual and S = phi(dual) over GF(3)):

       python3 build_x_lead.py 45 4 -1 4,8,6,7,5 1,8,8,0,5,7,0,3,2 +-++++++--+++++++-++-+++++---+++- out.json 20

   out.json is byte-identical to ../object/eaqecc_33_3_20_18.json (sha256 6df8f7ad...21961). It prints
   `X code [33,9] hull=6 -> [[33,3,?;18]]`. Erratum: the object's "construction" string says "rows 11..13 of the
   tail = M A" (a fixed phrase in build_x_lead.py); for this pair C2 has dimension 6, so the rows carrying M A are
   rows 6..8 (0-based) of G9. The matrices are unaffected.

- `PREREG.md`: the frozen plan of the run folder that panelled this claim (run 2026-10-24-2256), written before any of
  its checkers ran on the object. No null test: an explicit object checked by deterministic exact checkers against a
  table value.
