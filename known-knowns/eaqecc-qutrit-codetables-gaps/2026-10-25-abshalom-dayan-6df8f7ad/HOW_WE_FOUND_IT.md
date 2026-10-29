# How we found it

contributor text, unverified

An [n, kappa, d]_9 code with Hermitian hull dimension h gives an [[n, kappa - h, d; n - kappa - h]]_3 code (Luo,
Ezerman, Grassl and Ling, arXiv:2207.05647, Prop. 1). codetables.de's [33,9,20]_9 is a Construction X code built from
two algebraic-geometry codes [28,9,17] > [28,6,20] with a [5,3,3] tail (Ding, Niederreiter and Xing 2000). Ours uses
a place Q of degree 3 and the point at infinity of the Hermitian curve over GF(9). With Hermitian hull 6 it gives
[[33,3,20;18]]_3, where the qutrit table lists 19-30; the table has d = 20 at (33,3) only with 19 entangled pairs.

An earlier run of this workspace scored every Construction X family at n = 33 against the live table under the
table's own propagation rules: only the degree 11 > 8 pairs could beat a listed cell, and only with hull >= 6. The
tail of an X code only touches a 3 x 3 block of the Hermitian Gram matrix, so the hull of every X code of a pair
C1 > C2 is bounded by ranks computed from the head alone (a minimal-rank-completion bound), and the bound becomes
exact once Hermitian forms are classified by rank. An exhaustive pass over all 2^27 head sign patterns (column
scalings of norm -1) of the eight degree 11 > 8 pairs gave exact maxima 4, 5, 4, 5, 4, 5, 4 and 6: only
C(D_28, 4Q - P_inf) [28,9,17] > C(D_28, 3Q - P_inf) [28,6,20] reaches 6, at a single head pattern. Random tails at
that pattern reached 6 on try 1698. The code has d = 20 exactly.

The run that panelled it rebuilt the object byte for byte from frozen parameters, re-tested its checkers on a known
positive and a seeded negative, and found d = 20 by two exact methods that agree (a GF(9) information-set test over
all 818,809,200 sets of 14 columns; a GF(3) position-subset rank test over all 818,809,200 sets of 19 positions,
with 1330 = 1330 counts one step up), a Brouwer-Zimmermann computation, and weight-20 witnesses outside the
isotropic part.

A proof without a computer search (goppa_x.py checks every hypothesis in a second):
1. span(S)^perp = phi(C) for C = span(G9) (rank and orthogonality checks), and phi turns Hamming weight into
   symplectic weight, so d_EA >= d(C).
2. The head of C (first 28 coordinates, the scalings undone) is exactly C_L(D_28, 4Q - P_inf) for one place Q of
   degree 3, and the words with zero tail have heads forming exactly C_L(D_28, 3Q - P_inf); the head map is
   injective; the tail code is an MDS [5,3,3] code.
3. Goppa bound: a nonzero f in L(aQ + bP_inf) with z affine zeros and leading coefficient 0 at P_inf (e = 1) lies in
   L(aQ + bP_inf - zeros - e P_inf), whose degree 3a + b - z - e must be >= 0. So weights are >= 28 - 11 = 17 and
   >= 28 - 8 = 20.
4. Construction X: a nonzero word with zero tail weighs >= 20; one with a nonzero tail has a nonzero head (>= 17) and
   a nonzero tail (>= 3). So d(C) >= 20, and a weight-20 word outside span(S) gives d_EA = 20.

What failed on the way: hull 7 for this pair (exact maximum 6, so [[33,2,20;17]] is out of reach for it), the other
seven degree 11 > 8 pairs (maximum 5), and the longer-tail X families at n = 34..36.
