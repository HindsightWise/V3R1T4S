# PREREG (frozen 2026-10-24T23:02:10Z, before any checker of this run folder has been run on the object)

null_test: not needed because the claim is one explicit stabilizer matrix checked by deterministic exact checkers against a table value (no search statistic, no "beats chance" claim)

## Criterion (verbatim, bank entry eaqecc-qutrit-codetables-gaps)

Success means an explicit EAQECC with parameters [[n,k,d;c]]_3, c >= 1, given by an exact generator matrix over GF(3) (symplectic form, 2n columns) or over GF(9) (trace-Hermitian form), for a cell of the live qutrit table (https://eaqecc.codetables.de/qutrit.php, re-fetched live immediately before claiming), such that: with s independent generators on Alice's n qutrits, c = rank(S J S^T)/2 (half the rank of the symplectic commutation matrix) and k = n - s + c; the minimum distance d, computed exactly as the minimum weight of vectors in the symplectic dual of span(S) that are not in the isotropic part span(S) ∩ span(S)^perp (the EAQECC definition used by Grassl), is STRICTLY GREATER (direction: max) than the table's d_lower for that (n,k,c), and d <= d_upper. Results for c = 0 are excluded (they belong to the qudit table entry).

## Object to be judged

The Construction X lead of run 2026-10-24-1953's optimizer lens, objects/lead_33_3_20_18.json there (sha256
6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961), with C1 = C(D_28, 4Q - P_inf), C2 = C(D_28, 3Q - P_inf), Q = deg3.py place 45, tail points 4,8,6,7,5,
M = 1,8,8,0,5,7,0,3,2, columns '-' in +-++++++--+++++++-++-+++++---+++- times w. Claimed [[33,3,20;18]]_3 for the
listed cell (n,k,c) = (33,3,18). This run rebuilds it with build_x_lead.py from these frozen parameters
(build_x_lead.py 45 4 -1 4,8,6,7,5 1,8,8,0,5,7,0,3,2 +-++++++--+++++++-++-+++++---+++- out.json 20); the rebuilt JSON
must be byte-identical (same sha256) to the run-1953 file.
Replacement rule, fixed now: if a lens of this run folder produces an object at (33,3,18) with exact d >= 21 passing
every threshold below, that object is the claim instead. Objects at other cells are live leads, not claimed here (one
cell per claim).

## Statistic and checkers

- s = rank(S) over GF(3), c = rank(S J S^T)/2, k = n - s + c, computed from S alone, never copied.
- d, exact, by two independent methods that agree, none sampling:
  (A) gf9info.py + infoset.c: recover the GF(9) code C with phi(C) = span(S)^perp from S (exact GF(3) null space,
      checked closed under w), then test that every set of n - 19 = 14 coordinates carries an information set of C
      (all C(33,14) = 818809200 column subsets of a generator matrix have full rank 9 over GF(9)), which proves
      d(C) >= 20 and so d >= 20 on all of span(S)^perp; the same test at 13 coordinates must find deficient subsets
      (d(C) = 20); plus an explicit vector of span(S)^perp of symplectic weight 20 outside the isotropic part (d <= 20).
  (B) gf3prep.py + subset_ea64.c at W = d - 1 = 19: for every 19-subset T of the 33 positions, every vector of
      span(S)^perp supported inside T lies in the isotropic part (exact GF(3) ranks), all C(33,19) = 818809200
      subsets, uncapped; at W = 20 it must find subsets with a vector outside the isotropic part; plus witness.py's
      witness.
  Third, cited: bz64 (Brouwer-Zimmermann over GF(9), n <= 64) on the GF(9) generator matrix; fourth, cited:
  goppa_x.py (no-search proof from the Goppa bounds of the head and zero-tail codes).
  Both exact checkers are re-tested before they judge the object (attempts/evaluator-first/tests/validate.sh): known
  positive run 1640's E_17 object (d = 11, counts 1735, 1745, 1731 at W = 11), known negative a seeded object with a
  planted weight-3 word (W = 3 finds a subset; infoset m = 20 finds deficient subsets).

## Thresholds

1. Computed (n, k, c) = (33, 3, 18) with c >= 1.
2. d computed exactly = claimed d by (A) and (B), agreeing.
3. d > d_lower and d <= d_upper of the listed cell on a live one-GET re-read of https://eaqecc.codetables.de/qutrit.php
   right before claiming (scout: 19-30 at 2026-10-24T22:58:17Z).
4. Not implied, through the page's propagation rules, by any listed cell (teleportation cells excluded, as in runs
   1253, 1500, 1640, 1727 and 1953), any code in this repo, its open PRs (#363, #403-#405, #643, #645, #646, #651,
   #710), the literature found (already-settled lens; NOVELTY skeptic), or this workspace's other codes (E_m family,
   the packages 5713c745 [[33,7,15;12]] and 059282c3 [[33,9,14;12]], every lead). A tie is not a win.
5. One cell per claim; propagated neighbours are listed as not claimed.

## Search space record

Every search records its exact family and whether it was exhausted (uncapped) or capped. Capped or sampled searches
are never used as exclusions.
