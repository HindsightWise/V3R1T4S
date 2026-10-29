# Novelty verdict: [[33,3,20;18]]_3, target eaqecc-qutrit-codetables-gaps

**Bottom line: novel. d = 20 is strictly above everything known at (n,k,c) = (33,3,18).** The live cell reads
[[33,3,19-30;18]]_3, so d_lower = 19 and 19 < 20 <= 30. The page's own propagation rules bring nothing above 19 into
this cell, and neither do the repo's TROPHY_CASE.md, its known-knowns/ folder, the 9 open pull requests for this
target or the literature of the last 24 months. Nothing I found gives d >= 20 at c <= 18 for n = 33, k = 3, so this is
not a tie. The classical [33,9,20]_9 code it is built from has been public since 2000 (DNX). What is new is a version of
it with Hermitian hull dimension 6. The source paper of the table only gives hull dimension 2 of that code
([[33,7,20;22]]_3).

context: subagent (Claude Agent tool, model claude-opus-5-5), given only claim/

(This is a novelty check only. I did not re-verify d = 20; other skeptics do that. I did confirm that the object states
n=33, k=3, c=18, d=20, and that its sha256 is 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961.)

## Fetch record (status source, one GET, no retries)

- URL: https://eaqecc.codetables.de/qutrit.php
- Client: curl, User-Agent "V3R1T4S-research-agent (honest single fetch)"
- UTC time (`date -u`): before 2026-10-24T23:36:33Z, after 2026-10-24T23:36:33Z (server Date header: Sat, 24 Oct 2026
  23:36:33 GMT)
- HTTP status: 200, 628039 bytes
- sha256: 37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c. This is byte-identical to
  claim/table/qutrit.php (`cmp` reports no difference), so the page has not changed since the claim's fetch.
- Page footer: "Last change: 10.07.2025"
- Saved as fetched/qutrit.php, with fetched/qutrit.headers.txt, fetched/qutrit.status.txt, fetched/qutrit.sha256.txt
  and fetched/qutrit.time_before.txt / fetched/qutrit.time_after.txt
- The cell, verbatim:
  `<TD NOWRAP bgcolor="#ff9900" class="EAQECC" title="lengthening of [[27,3,19;18]] increasing dimension of [[27,2,19;17]] from arXiv:2207.05647">[[33,3,19-30;18]]<sub>3</sub></TD>`
- Every listed cell in row n = 33, k = 3, verbatim:
  - `[[33,3,11-14;0]]` "from codetables.de"
  - `[[33,3,18-28;3]]` "using teleportation"
  - `[[33,3,19-30;18]]` (the claimed cell)
  - `[[33,3,20-30;19]]` "lengthening of [[28,3,20;19]] increasing dimension of [[28,2,20;18]] from arXiv:2207.05647"
  - `[[33,3,21-30;21]]` "subcode of [[33,4,21;21]] quantum shortening of [[34,3,22;21]] increasing dimension of [[34,0,22;18]] from arXiv:2207.05647"
  - `[[33,3,22-30;24]]` "subcode of [[33,5,22;24]] quantum shortening of [[34,4,23;24]] from arXiv:2207.05647"
- Neighbour cells (c: d_lower-d_upper):
  - (32,3): 0: 10-13; 1: 11-16; 3: 18-27 (teleportation); 18: 19-29; 19: 20-29; 21: 21-29
  - (33,4): 0: 10-13; 1: 11-16; 4: 17-26 (teleportation); 16: 18-28; 18: 19-29; 20: 20-29; 21: 21-29; 24: 22-29
  - (34,3): 0: 11-14; 3: 19-29 (teleportation); 19: 20-31; 21: 22-31; 24: 23-31
  - (34,2): 0: 11-14; 2: 22-31 (teleportation); 24: 23-32
  - (33,2): 0: 11-14; 2: 21-30 (teleportation); 24: 22-31
  - (34,0,18): 22-27

## Sources checked and what each gives at (33,3,18)

| source | best known d at (33,3,18) (or at any c <= 18 for n=33, k=3) | beats or ties 20? |
|---|---|---|
| live cell | 19 | no |
| page's colour-legend rules, propagated to a fixpoint from all 3888 listed cells | 19 | no |
| same, with every repo PR code and known-knowns code added as seeds | 19 | no |
| same, with the 19 qutrit codes of arXiv:2607.02170 (Tables V, VII) added | 19 | no |
| repo TROPHY_CASE.md | no entry for this target | no |
| repo known-knowns/eaqecc-qutrit-codetables-gaps/ | one entry only: [[14,3,8;5]]_3 | no |
| 9 open PRs for this target | nothing with d >= 20 at c <= 18 | no |
| literature, Oct 2024 to Oct 2026 | no qutrit EA code at n >= 26 found; nothing that propagates here | no |
| classical GF(9) table, [33,9] | [33,9,20]_9 (DNX), upper bound 23: context, not an EA code at c = 18 | n/a |

Details:

1. **Propagation rules (colour legend).** The legend lists subcode [[n,k-1,d;c]], lengthening [[n+1,k,d;c]],
   puncturing [[n-1,k,d-1;c]], trivial [[n,0,n+1;n]], quantum shortening [[n-1,k+1,d-1;c]], increasing dimension
   [[n,k+1,d;c+1]], length reduction [[n-1,k,d;c+1]] and teleportation [[n,k,d;k]]. I parsed all 3888 cells
   (cells.json, scripts/parse_table.py) and applied the six rules to a fixpoint, plus "an unused ebit" (c to c+1, which
   only makes the check stricter), in scripts/closure.py. The value at (33,3,18) is 19, and its derivation is the
   cell's own title. No rule lowers c and none raises d. A source for d >= 20 here would therefore need d >= 20 at
   c <= 18 (c <= 18 - (3-k) when k < 3) for n <= 33, or d >= 20 to 21 at n = 34. The only listed cell of that kind is
   [[34,0,22;18]], and it reaches (33,3,18) only as 19 (three quantum shortenings, then lengthening). The catalytic
   rule, which the page explicitly excludes, would also need [[33,4,>=20;19]], and that is not listed.
   - **Teleportation cells** (title "using teleportation") cannot be propagation sources. Seeding them into the six
     rules gives 27 at the target, but it also pushes 2700 listed cells above their own d_upper (scripts/tele_check.py).
     For example, [[8,1,6;1]] followed by length reduction three times gives (5,1,4) d = 6 > 5. This reproduces the
     claim's statement. The teleportation cell in this row, [[33,3,18;3]], gives 18 < 20 even if extra ebits are allowed.
   - **Side observations** (not this cell): the page is not fully closed under its own rules at k = 0 cells (pure
     distance: lengthening a k = 0 code is not valid, which is an artefact of my rule set) and at four k > 0 cells,
     (22,11,11), (33,2,24), (33,3,24) and (34,2,24). The last three follow from the listed [[33,1,25;24]] by lengthening
     and quantum shortening. They give exactly PR #404 [[34,2,24;24]] and PR #405 [[33,3,23;24]], so those two PRs tie
     the page's own rules. This does not affect the present claim.
2. **Repo** github.com/elder-plinius/V3R1T4S (default branch main; one GET per page; log in fetched/github/LOG.txt):
   - TROPHY_CASE.md: HTTP 200 at 2026-10-24T23:39:58Z, sha256 b946f68e...71a1. No mention of eaqecc or qutrit.
   - known-knowns/: HTTP 200. The folder eaqecc-qutrit-codetables-gaps/ holds one entry (dated 2026-10-17), and its
     INDEX.csv lists only [[14,3,d;5]]_3 = 8.
   - Open PRs: GitHub search `repo:elder-plinius/V3R1T4S is:pr is:open eaqecc-qutrit-codetables-gaps` returned HTTP
     200 at 2026-10-24T23:39:43Z with total_count 9: #363 [[33,1,31;24]], #403 [[16,4,8;4]], #404 [[34,2,24;24]],
     #405 [[33,3,23;24]], #643 [[28,5,15;11]], #645 [[28,7,14;11]], #646 [[28,6,12;6]], #651 [[28,9,11;7]],
     #710 [[33,8,16;15]]. This matches the list in CLAIM.md. A second search with the term "qutrit" returned the same 9.
     A search over all states returned 10: the extra one is #331 [[14,3,8;5]], closed and merged 2026-10-19.
   - I extracted every [[n,k,d;c]] from the PR bodies and seeded all of them, plus the claim's two unfiled
     [[33,7,15;12]] and [[33,9,14;12]]. The only codes with d >= 20 are at c = 24, and none reaches (33,3,18) above 19
     (scripts/closure_pr.py).
3. **Literature, last 24 months:**
   - arXiv:2607.02170 (Li, Ezerman, Li, Ling, Sun, v1 2 Jul 2026), the main recent qutrit EA paper. I read the PDF text
     (fetched/arxiv/2607.02170v1.txt). Its qutrit codes have lengths 7 to 25 only (Table V, "lengths 7 <= n <= 25";
     Table VII). The ones with d >= 20 are [[23,2,20;21]], [[24,2,21;22]], [[25,2,22;23]] and [[25,3,20;22]], all at
     c >= 21. Seeded into the propagation, the target stays at 19 (scripts/closure_lit.py). The paper compares against
     Grassl's tables (accessed 15 Jun 2026) and against recent records [6] Cao-Li-Zhu (IEEE TIT, Oct 2025), [10]
     arXiv:2501.04921, [26] Liu-Li-Shi (AMC 2025) and [23], [25]. The qutrit codes it cites from these are all of
     length <= 26.
   - arXiv:2501.04921 (EA concatenated codes, Jan 2025): no qutrit codes listed.
   - arXiv:2609.31300 (Sep 2026): qubit EAQECCs only.
   - arXiv:2512.17128 (Hermitian hulls of rational AG codes): MDS families only. Over GF(9) these have length <= 10.
   - arXiv:2603.03182 (EA codes outside the stabilizer framework): no parameters.
   - arXiv:2605.29204 (hull enumeration): quaternary only, no EA codes.
   - arXiv:2607.12242: stabilizer (c = 0) codes. At (33,3,0) the table's upper bound is 14, so these cannot matter.
   - arXiv:2512.12519: withdrawn, abstract only, no parameters.
   - Searches for qutrit EA codes over F_9 from quasi-twisted, quasi-cyclic, constacyclic or AG/Hermitian-curve
     constructions in 2025 and 2026 found no qutrit EA code at n = 33. The quasi-twisted EA work I found is
     maximal-entanglement (c = n - k = 30 here) or qubit.
   - The source paper arXiv:2207.05647 (v2 Sep 2022, QIP 23:4, 2024) is older than 24 months. Its results are what the
     cell already shows. At n = 33 it lists [[33,7,20;22]] directly, which is the DNX code with hull dimension 2.
4. **Classical GF(9) table:** https://www.codetables.de/BKLC/BKLC.php?q=9&n=33&k=9, one GET, HTTP 200 at
   2026-10-24T23:41:50Z, sha256 864b91c6c4e30df7896844d844dfb2237cf4e7d2a78b6e5904a3c8e8187cdc01. It reads "lower
   bound:20 upper bound:23 ... Construction type: DNX", ConstructionX of [28,9,17] and [28,6,20] AG codes with a
   [5,3,3] tail. This matches the claim's own context section. An [n,k] code over GF(9) with hull dimension h gives
   [[n, k-h, >=d; n-k-h]], and (33,3,18) forces k = 9, h = 6. No published hull-6 version of this code turned up.

## What I could not read

- The arXiv HTML of 2607.02170 was truncated by the fetch tool, so I used the PDF text instead (one fetch, a copy kept
  in fetched/arxiv/).
- Several journal versions (Cao-Li-Zhu IEEE TIT 2025, Liu-Li-Shi AMC 2025) I saw only through 2607.02170's comparison
  tables and search summaries, not in full text.
- I read PR titles and the [[...]] codes in their bodies, not every line of every body.
- No fetch was blocked. No page asked me to do anything (no injection suspected in the parts I read).

pass: true
