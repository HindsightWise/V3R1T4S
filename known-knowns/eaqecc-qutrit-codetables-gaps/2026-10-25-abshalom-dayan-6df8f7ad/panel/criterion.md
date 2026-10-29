# Criterion skeptic verdict: [[33,3,20;18]]_3 (target eaqecc-qutrit-codetables-gaps)

Bottom line: PASS. Read literally, the result meets the full success criterion (not a partial win). The GF(3)
matrix S (48 x 66) in claim/object/eaqecc_33_3_20_18.json has s = 48 independent rows, rank(S J S^T) = 36 so c = 18,
and k = 33 - 48 + 18 = 3. I enumerated every one of the 3^18 = 387,420,489 vectors of span(S)^perp. The minimum
symplectic weight outside the isotropic part is exactly 20. The live table cell (n,k,c) = (33,3,18) is listed as
[[33,3,19-30;18]]_3, and 19 < 20 <= 30. I found no hidden quantifier, stretched definition, sampled search or
catalytic reading. The page's own propagation rules do not already give d >= 20 in this cell.

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/

## Clause by clause

My own code is in mine/ (la3.py: exact GF(3) linear algebra on S; enum.c: exhaustive enumerator; check_witness.py;
table_check.py; propagate.py; nulltest/). None of it reuses the author's code.

1. **Explicit generator matrix over GF(3), 2n columns.** S in the object is 48 rows x 66 columns, all entries in
   {0,1,2}, rows (x|z) with <(x|z),(x'|z')> = x.z' - z.x' (la3.py asserts the shape and the entries). n = 33.
   Object sha256 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961, the same as stated in CLAIM.md.
   The author's rebuild (REPRODUCE step 1, run in mine/author_runs/) regenerates a byte-identical file (same hash).
   Met.

2. **s independent generators.** I computed rank(S) over GF(3) = 48 = number of rows, so s = 48. Met.

3. **c = rank(S J S^T)/2, c >= 1.** I computed the 48 x 48 commutation matrix and checked it is antisymmetric. Its
   rank over GF(3) is 36, so c = 18 >= 1. This is the non-catalytic count (the rank of the commutation matrix), with
   no catalytic reduction anywhere in the claim. Met.

4. **k = n - s + c.** 33 - 48 + 18 = 3, the claimed k. The code's (n,k,c) = (33,3,18) is the claimed and listed cell,
   not a different one. Met.

5. **d computed exactly as min weight of span(S)^perp \ (span(S) ∩ span(S)^perp).**
   - la3.py: N = span(S)^perp has dim 18 (kernel of [-Z | X]). Every basis vector is checked orthogonal to all 48
     rows. I = span(S) ∩ N is built from the left kernel of the commutation matrix and has dim 12 = s - 2c. It is
     checked to lie in N and in span(S), and dim(span S + N) = 54 = 48 + 18 - 12. The basis of N is written with
     I's basis first.
   - enum.c: enumerates ALL 3^18 = 387,420,489 coefficient vectors, with no subset trick, no sampling and no cap. A
     vector is in I exactly when its coefficients on the 6 non-I basis rows are all zero. Totals: |N \ I| =
     386,889,048 and |I| = 531,441, which sum to 3^18. Weight distribution of N \ I starts 20:10640, 21:58616,
     22:188984, ... and has no weight below 20. I itself (nonzero part) has minimum weight 21. So the exclusion of
     isotropic vectors does not matter here: even min weight of N \ {0} is 20, and no degeneracy question arises. All
     counts are multiples of 8, as GF(9)-linearity predicts. 10640 = 8 x 1330 matches the author's independent figure
     of 1330 weight-20 supports.
   - Witness: enum.c's minimum vector, re-checked by check_witness.py directly against S, has weight 20, is orthogonal
     to all 48 rows and is not in span(S). So d = 20 exactly. (The author's two witness tools and their bz64 and
     goppa_x checkers, run in mine/author_runs/, also print d = 20; I did not rely on them.)
   - Null model for my enumerator: nulltest/null2.py ran 14 random small EA stabilizers (n = 6, 7; d from 1 to 4).
     la3.py + enum.c agreed with a numpy brute force over all of GF(3)^(2n) in 14 of 14 cases
     (nulltest/null2_out.txt). In that brute force, span(S) membership comes from an explicit list of all 3^s span
     vectors. Peak memory of the real run was about 2.8 MB, 0.8 s wall time.
   Met: d = 20.

6. **Cell of the live table, re-fetched immediately before claiming.** I made one plain GET of
   https://eaqecc.codetables.de/qutrit.php with curl (User-Agent "V3R1T4S-research-agent (honest single fetch)"),
   no retries. Time 2026-10-24T23:59:31Z before and after (`date -u`), HTTP 200, 628039 bytes, sha256
   37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c (saved as fetched/qutrit.php with
   fetched/qutrit.headers.txt). This is byte-identical to the author's copy claim/table/qutrit.php, fetched
   2026-10-24T22:58:17Z per claim/table/RECORD.md, so the cell has not changed since the author's read. The cell,
   verbatim: `[[33,3,19-30;18]]<sub>3</sub>`, title "lengthening of [[27,3,19;18]] increasing dimension of
   [[27,2,19;17]] from arXiv:2207.05647". It is an explicitly listed cell (row n=33, k=3 lists c = 0, 3, 18, 19, 21,
   24). One limit: I can confirm the live content is unchanged now, but claim/ cannot show me when the claim itself
   was filed relative to the author's fetch. Met as far as observable.

7. **d > d_lower and d <= d_upper.** 20 > 19 and 20 <= 30. Met.

8. **Non-catalytic, c = 0 excluded.** c = 18 is the rank-based count. The page states it lists the non-catalytic
   setting, and the claim uses no c >= k reduction. Met.

## Subsumption and stretched-definition checks

- **Same cell or a cheaper cell already at d >= 20?** I parsed 3888 cells from the fetched page. No listed cell with
  n <= 33, k >= 3, c <= 18 has d_lower >= 20. The listed (33,3,19) cell (20-30) uses 19 ebits. None of the page's
  rules lowers c, so it does not imply 20 at c = 18.
- **One-step neighbours into the target under the page's rules:**
  - subcode from (33,4,18) gives 19;
  - lengthening from (32,3,18) gives 19;
  - the other four neighbours (puncturing, quantum shortening, increasing dimension, length reduction) are not listed
    cells.
- **Full closure:** I ran a fixpoint closure of the page's seven rules over all listed non-teleportation cells
  (propagate.py). My version is slightly more generous than the page's: it lifts 32 other cells above their listed
  d_lower, 28 of them k = 0 cells. It still gives exactly 19 at (33,3,18). The table's own data therefore does not
  already contain d >= 20 here.
- **Teleportation cells (c = k):** seeding them into the same closure gives 27 at the target. It also pushes 2700
  listed cells above their d_upper, for example (5,1,4) to 6 > 5. Both numbers reproduce the author's context
  statement. The page itself does not propagate them either: it lists (33,2,2) at 21 but (33,3,3) at 18. They are
  not valid sources under the page's rules, so they do not subsume the claim.
- **Open PRs listed in CLAIM.md:** none of them is at a cell that can reach (33,3,18) with d >= 20. Each has
  either c > 18 (rules never lower c) or d <= 16. I could not see the PR list itself, only CLAIM.md's account of it.
- **Partial-win confusion:** none. This is the full criterion (a lower-bound improvement), not p1 (upper bound) and
  not p2 (matching d with fewer ebits).
- No injection suspected in the page or the files.

confirmed_scope: The 48 x 66 GF(3) matrix S in claim/object/eaqecc_33_3_20_18.json (sha256 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961) has s = 48, c = rank(S J S^T)/2 = 18, k = 3 and exact EA minimum distance d = 20 by exhaustive enumeration of all 3^18 vectors of span(S)^perp, which is strictly above the d_lower = 19 (d_upper = 30) of the cell [[33,3,19-30;18]]_3 on https://eaqecc.codetables.de/qutrit.php as fetched 2026-10-24T23:59:31Z (HTTP 200, sha256 37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c).

pass: true
