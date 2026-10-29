# REPRODUCE skeptic verdict: [[33,3,20;18]]_3 (object/eaqecc_33_3_20_18.json)

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/

## Bottom line

**PASS.** I wrote my own checker from the definition before reading claim/checkers/ or claim/rebuild/. It works from the matrix S alone and enumerates every one of the 3^18 = 387420489 vectors of span(S)^perp, so nothing is sampled. It gives s = 48, rank(S J S^T) = 36, c = 18, k = 3 and d = 20, which matches the claimed [[33,3,20;18]]_3. The minimum is reached by 10640 vectors outside the isotropic part, on 1330 distinct supports.

I also ran the author's REPRODUCE.md steps 1-6. Every value they print matches what REPRODUCE.md says, and the outputs are the same on a second run. I did not run step 7 (the live table, d_lower = 19, d_upper = 30) or judge novelty; the other skeptics cover those.

## Definition (quoted from CLAIM.md, success criterion)

> "with s independent generators on Alice's n qutrits, c = rank(S J S^T)/2 (half the rank of the symplectic commutation matrix) and k = n - s + c; the minimum distance d, computed exactly as the minimum weight of vectors in the symplectic dual of span(S) that are not in the isotropic part span(S) ∩ span(S)^perp (the EAQECC definition used by Grassl), is STRICTLY GREATER (direction: max) than the table's d_lower for that (n,k,c), and d <= d_upper. Results for c = 0 are excluded"

Conventions, from the object JSON: rows of S are (x|z) over GF(3) with 2n columns, and <(x|z),(x'|z')> = x.z' - z.x'. The symplectic weight is the number of positions i with (x_i, z_i) != (0,0).

## What I computed and how (files in mine/)

- **mine/gf3.py** does exact GF(3) linear algebra in pure Python. It computes:
  - s = rank(S) and the 48 x 48 commutation matrix S J S^T, with its rank;
  - N = span(S)^perp, as the null space of (-S_z | S_x);
  - the isotropic part I = span(S) ∩ N, as {aS : a S J S^T = 0} (the left kernel of the commutation matrix);
  - a basis of N whose first dim I vectors span I.

  It asserts that every basis vector is orthogonal to every row of S, that every vector of I lies in span(S), and that dim I agrees with the formula dim I = s + dim N - rank(S stacked on N).
- **mine/enum_n.c** is my exhaustive enumerator. A base-3 odometer walks all 3^(dim N) coefficient vectors; each digit step adds one basis vector, so the running vector is always the exact combination. A vector is in I exactly when its coefficients on the complement part are all zero. The vectors are stored as bit-sliced GF(3) values. The program records the symplectic weight histograms of I and of N \ I, the minimum weight of N \ I, one witness, and the distinct supports at the minimum weight. It also checks that the odometer comes back to 0.
- **mine/verify_real.py** cross-checks the result:
  - the claimed n, k, c, d fields against my values;
  - the witness, re-checked against the raw rows of S;
  - MacWilliams consistency of the enumerated weight distribution;
  - the GF(9) side of the object, using my own GF(9) arithmetic built from the JSON's field convention.
- **mine/prep_real.py** writes the basis. It also builds a seeded negative: a code with a planted weight-12 vector in its dual.

Results on S (mine/scratch/enum_real.out, sha256 4da4555fe428488292a412671234726b9b946816253e9f9483545162f80ff462):

| quantity | mine | claimed |
|---|---|---|
| rows of S, s = rank(S) | 48, 48 | 48 x 66 |
| rank(S J S^T), c | 36, 18 | c = 18 |
| k = n - s + c | 33 - 48 + 18 = 3 | 3 |
| dim N, dim I, dim N - dim I | 18, 12, 6 (= 2k) | 18, 12 |
| vectors enumerated | 387420489 = 3^18 (531441 in I, 386889048 in N \ I) | - |
| min symplectic weight of N \ I | **20** (10640 vectors, 1330 distinct supports) | 20 |
| min nonzero weight inside I | 21 (48 vectors) | - |

Further results:

- **Run time and memory.** The enumeration took 2.08 s wall time with a peak memory footprint of 1163600 bytes (/usr/bin/time -l).
- **Determinism.** Three runs gave byte-identical output. The third run used the final enum_n.c build, which only adds the support dump.
- **Weight histogram of N \ I.** 20:10640 21:58616 22:188984 23:675888 24:2206904 25:6564072 26:16269632 27:33346000 28:57519768 29:79594200 30:84437624 31:65265184 32:32756744 33:7994792.
- **Witness from my enumeration.** It has symplectic weight 20, is orthogonal to all 48 rows of S, and lies outside span(S). Its support is [3,4,5,6,9,10,11,13,15,18,19,20,22,24,25,26,27,28,31,32].
- **MacWilliams check.** The q^2 = 9 transform of N's weight distribution should be the weight distribution of span(S) = N^perp. It comes out as nonnegative integers with B_0 = 1, total 3^48, and B_j >= |I_j| for every j.
- **GF(9) properties of the object.**
  - rank(G9) = 9 and rank(D9) = 24;
  - G9 is Hermitian-orthogonal to D9;
  - S = phi(D9), with the rows interleaved as r, w r;
  - phi(C) lies inside span(S)^perp and has GF(3) rank 18, so N = phi(C);
  - the Hermitian hull of C has dimension 6, so 2 x 6 = 12 = dim I.

## Tests of my checker

- **Brute-force cross-check** (mine/bruteforce_test.py): 265 small cases, **0 mismatches**, run twice, the second time with the final enumerator build. For each case, a pure brute force enumerates all of GF(3)^(2n) and all of span(S), and its s, rank(S J S^T), c, k, d and both full weight histograms must equal my pipeline's.
  - Sizes: n = 2..6, 3^4 to 3^12 vectors per case.
  - Case mix: 160 random cases, 40 planted low-weight negatives, 60 cases with a weight-1 isotropic generator, plus dependent and zero rows and full-rank cases.
  - In 20 cases I holds vectors lighter than d, which shows the exclusion of I is actually exercised.
  - 68 cases have N = I (k = 0).
- **Seeded negative at full size** (n = 33, dim N = 18). A planted vector p of weight 12 sits in the dual, outside the isotropic part, of a rebuilt S'. My checker reports min weight 12 on exactly p and -p, with the planted support (mine/scratch/enum_plant.out).
- **Seeded negative 2.** Changing a single entry of S (row 0, column 0) gives [[33,4,19;19]], so a perturbed object is rejected.

## Author's REPRODUCE.md steps 1-6

I ran them on an identical copy of claim/ (author_run/; all 16 files match by sha256). For step 4 I ran no more than 2 parts at a time.

| step | REPRODUCE.md expects | observed | match |
|---|---|---|---|
| 1 rebuild | `X code [33,9] hull=6 -> [[33,3,?;18]]  S 48x66  D9 24x33`; sha256 6df8f7ad...2421961 for both files | identical line; rebuilt.json and the object both 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961 | yes |
| 2 prep | `n=33 s=48 c=18 k=3 dim_N=18 dim_I=12 N_closed_under_w=True`, kappa=9 | identical | yes |
| 2 m=14 | deficient=0; subsets 426862095, 249420648, 142526457 (sum 818809200) | identical; sum 818809200 = C(33,14) | yes |
| 2 m=13 | deficient 617, 441, 272 (1330) | 617, 441, 272; subsets sum 573166440 = C(33,13) | yes |
| 3 gf9info witness | `weight=20 in_N=True orthogonal_to_all_rows_of_S=True in_isotropic_part=False` | identical | yes |
| 3 witness.py | `symplectic_weight=20 orthogonal_to_all_rows_of_S=True in_span_S=False` | identical; I re-checked this vector with my own code: weight 20, orthogonal, not in span(S) | yes |
| 4 prep | `n=33 s=48 c=18 k=3 dim_isotropic=12 dim_dual=18` | identical | yes |
| 4 W=19 | each part examined=272936400, with_vector_outside_isotropic=0 | 0/0/0, examined 272936400 x 3 = 818809200 (CPU 119.2, 119.3, 117.4 s user) | yes |
| 4 W=20 | 468, 431, 431 (1330) | 468, 431, 431; examined 191055480 x 3 = 573166440 | yes |
| 5 bz64 | `K=9 n=33 d=20 sets=9,9,9,5,1 maxw=5 words=2931405` + weight-20 witness | identical | yes |
| 6 goppa_x | last line `RESULT: d_EA = 20 exactly (theorem-based; no distance search): True`; bound min(28-8, 28-11+3) = 20 | identical last line; printed `d(C) >= min(20, 17 + 3) = 20` | yes |

Cross-checks between my results and the author's:

- My 1330 weight-20 supports are exactly the complements of the author's 1330 deficient 13-subsets, which I listed with `infoset 13 p 3 list 2000`.
- The three `first=` 20-subsets printed by step 4, and the step-3 witness support, are all among my 1330 supports.
- A second full run of steps 1, 2 (m=14), 3, 5 and 6 differed from the first only in the echoed file name. G9.txt and basis.txt were byte-identical across runs.

## Proof steps re-derived

- **Step 2: information sets.** A nonzero word of weight <= 19 vanishes on at least 14 positions, so it would make some 14-subset rank-deficient. Zero deficient 14-subsets therefore gives d(C) >= 20. Symplectic weight on phi(C) equals Hamming weight on C, because phi(a + bw) = (a|b), and N \ I is contained in N, so d_EA >= d(C) >= 20.
- **Step 4: subset rank test.** A non-I row that becomes dependent during the elimination restricted to the complement of T means dim N_T > dim I_T. That is exactly the condition for a vector of N \ I to be supported inside T. So 0 hits for W = 19 gives d >= 20.
- **Steps 3 and 5.** Each gives an explicit weight-20 vector outside I, so d <= 20.
- **Step 6: Construction X.** If the C1 part u is in C2, the tail is 0 and the weight is at least d2 >= 28 - 8 = 20. Otherwise the tail is nonzero, because the tail has rank 3, and the weight is at least d1 + 3 >= 17 + 3 = 20.

  I re-derived this logic, but I did not independently re-verify the identification of the head code as an AG code. My exhaustive enumeration does not depend on it.

## Notes

- CLAIM.md already acknowledges an erratum in the object's "construction" string: it says "rows 11..13", but the gluing rows are 6..8. build_x_lead.py applies the tail to rows i >= K2 = 6, which is consistent with the erratum. This does not affect S.
- The author's gf3prep.py takes the same textbook route to N and I as my gf3.py. My distance method, full enumeration of N, is different from all four of the author's methods. The two agree exactly, including the 1330 count.
- The claim/ folder was unchanged at the end, verified by sha256 of all 16 files. My scratch work is in mine/ and author_run/.

pass: true
