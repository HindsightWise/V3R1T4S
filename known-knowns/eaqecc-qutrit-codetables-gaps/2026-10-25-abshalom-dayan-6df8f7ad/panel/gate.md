# Honesty gate (main session), run folder 2026-10-24-2256

status: CONFIRMED_SOLUTION
confirmed_scope: The 48 x 66 GF(3) matrix S in claim/object/eaqecc_33_3_20_18.json (sha256 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961) has s = 48, c = rank(S J S^T)/2 = 18, k = 3 and exact EA minimum distance d = 20 by exhaustive enumeration of all 3^18 vectors of span(S)^perp, which is strictly above the d_lower = 19 (d_upper = 30) of the cell [[33,3,19-30;18]]_3 on https://eaqecc.codetables.de/qutrit.php as fetched 2026-10-24T23:59:31Z (HTTP 200, sha256 37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c).

Claim: [[33,3,20;18]]_3 at the listed cell (n,k,c) = (33,3,18) of https://eaqecc.codetables.de/qutrit.php, object
claim/object/eaqecc_33_3_20_18.json (sha256 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961), a
Construction X code over GF(9) from the Hermitian-curve AG codes C(D_28, 4Q - P_inf) [28,9,17] > C(D_28, 3Q - P_inf)
[28,6,20] (Q a place of degree 3) with a [5,3,3] tail and a column sign pattern: [33,9,20]_9 with Hermitian hull 6.

Claim folder unchanged since the panel started: every file's sha256 equals panel/claim.sha256 (16 of 16 files OK,
checked at the gate). Self-break (self_break/verdict.md, main session, in a copy of claim/): SURVIVES.

Panel files read in full by the main session (each skeptic a fresh subagent, claude-opus-5-5, given only its own
copy of claim/, run one after another, never in parallel; started 23:18:06Z, 23:35:47Z, 23:58:52Z; verdict files
written 23:34:47Z, 23:53:17Z, 00:09:40Z UTC by file time):
- reproduce.md: own exhaustive enumeration of all 3^18 = 387420489 vectors of span(S)^perp (mine/enum_n.c, from S
  alone, written before reading the author's code): s = 48, rank(S J S^T) = 36, c = 18, k = 3, dim N = 18, dim I = 12;
  minimum symplectic weight outside I = 20 (10640 vectors, 1330 supports), minimum nonzero weight inside I = 21;
  MacWilliams check consistent; 265 brute-force cases with 0 mismatches (20 of them with lighter isotropic vectors);
  two seeded negatives caught; three byte-identical runs; the author's steps 1-6 reproduced exactly (rebuild hash,
  infoset m = 14 all 0 and m = 13 617/441/272, both witnesses, subset test W = 19 all 0 and W = 20 468/431/431,
  bz64 d = 20, goppa_x RESULT True); its 1330 supports are exactly the complements of the author's 1330 deficient
  13-subsets. pass: true.
- novelty.md: one honest GET at 2026-10-24T23:36:33Z, HTTP 200, sha256 37bbf731..., cell [[33,3,19-30;18]]_3;
  closure of all 3888 cells under the page's rules gives 19, also with every open-PR code, the workspace's unfiled
  codes and arXiv:2607.02170's qutrit codes added; teleportation seeding breaks 2700 d_upper values; TROPHY_CASE.md
  nothing; known-knowns one entry at n = 14; 9 open PRs (matching CLAIM.md), none with d >= 20 at c <= 18;
  codetables.de [33,9]_9 20-23 (DNX); the source paper uses this code only at hull 2 ([[33,7,20;22]]); literature
  2024-10 to 2026-10 nothing at this cell. pass: true.
- criterion.md: every clause with its own code (la3.py, enum.c over all 3^18 vectors: d = 20; I's minimum weight 21;
  null test of 14 random small stabilizers against numpy brute force, 14 of 14); one GET at 23:59:31Z,
  byte-identical, cell listed; 19 < 20 <= 30; c >= 1; non-catalytic; one-step neighbours give 19; full closure 19.
  pass: true.

Live re-fetch at the gate: one plain curl GET, User-Agent "V3R1T4S-research-agent (honest single fetch)", no
retries, 2026-10-25T00:13:20Z to 2026-10-25T00:13:20Z (server date: Sun, 25 Oct 2026 00:13:20 GMT), HTTP 200,
628039 bytes, sha256 37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c (unchanged since the claim's
22:58:17Z fetch), footer "Last change: 10.07.2025", cell verbatim `[[33,3,19-30;18]]<sub>3</sub>` (title "lengthening
of [[27,3,19;18]] increasing dimension of [[27,2,19;17]] from arXiv:2207.05647"). Saved in data/gate_fetch/. 20 > 19
and 20 <= 30.

Downgrade checks (none triggered): no hedging panelist; no reproduction mismatch (the author's methods A and B, bz64
and goppa_x.py, the self-break's numpy checker and Construction X bound, and two full 3^18 enumerations by the
REPRODUCE and CRITERION skeptics all give d = 20, with 1330 weight-20 supports in four independent counts); 20
strictly above the live d_lower 19; no stretched criterion or hidden quantifier; scope no wider than reproduced; no
sample presented as complete; no capped search used as an exclusion; no probable prime; the table read only by
honest single GETs. One object, one cell. Not subsumed by this workspace's other codes: the already-settled lens's
closure (attempts/already-settled/out/settled.txt) includes every E_m, the X codes and the packages 5713c745 and
059282c3, and gives 19 at (33,3,18).

Caveats carried into the package and report, not downgrades:
- The classical [33,9,20]_9 code is codetables.de's (Ding, Niederreiter, Xing 2000). Wording: "improves the table
  cell" with a hull-6 version of it, not "new technique".
- The object's construction string says the gluing matrix fills "rows 11..13 of the tail"; the rows are 6..8
  (erratum stated in claim/CLAIM.md; G9, D9 and S, which every skeptic checked, are unaffected).
- The same row lists [[33,3,20-30;19]]_3, so the gain is one entangled pair saved at d = 20. Optimality not claimed
  (d_upper 30).
- Literature: journal papers without arXiv versions (Cao-Li-Zhu IEEE TIT 2025, Liu-Li-Shi AMC 2025) judged from the
  codes arXiv:2607.02170 cites from them.
Not part of this claim: cells that follow by the table's rules, and this folder's optimizer lead [[35,7,16;14]]_3.
