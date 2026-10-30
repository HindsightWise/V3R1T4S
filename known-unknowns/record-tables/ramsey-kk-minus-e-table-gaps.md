# Ramsey numbers with K_k - e: close a gap in Radziszowski's Table IIIa/IIIb (e.g. R(K4-e,K8-e) 30-32, R(K6,K5-e) 43-51, R(K8,K4-e) 36-39)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (lower bounds by local search or circulant SAT on 30-100 vertices); needs cluster for most upper bounds · open as of 2026-10-30

## The problem

R(G,H) is the least N such that every graph on N vertices contains G or its complement contains H. Radziszowski's dynamic survey DS1 (revision #18, 24 Apr 2026), Tables IIIa/IIIb, lists the known values and bounds when G and H are complete graphs or K_k minus one edge, and not both complete. Open ranges on 2026-10-30 include: R(K3,K11-e) 42-45, R(K3,K12-e) 49-53, R(K3,K13-e) 55-62, R(K3,K14-e) 61-71, R(K3,K15-e) 69-80; R(K4-e,K8-e) 30-32, R(K4-e,K9-e) 36-45, R(K4-e,K10-e) 43-57; R(K4,K7-e) 37-49, R(K4,K8-e) 52-71; R(K5-e,K8-e) 66-91; R(K5,K6-e) 43-59, R(K5,K7-e) 65-102; R(K6-e,K6-e) 45-70; R(K6,K5-e) 43-51; R(K7,K5-e) 65-79; R(K8,K4-e) 36-39, R(K9,K4-e) 41-53, R(K10,K4-e) 49-68. Since the survey, William Wesley (arXiv:2606.17021, Jun 2026) settled R(K4-e,K7) = 28. Credit: lower bounds mostly Goedgebeur and Van Overberghe (DAM 2022; constructions at github.com/Steven-VO/circulant-Ramsey), Exoo, McNamara, Radziszowski; upper bounds by Boza (BZ1-BZ4, recomputed in 2026 after Angeltveit's R(K5,K5-e) = 30), Lidicky-Pfender (flag algebras), Goedgebeur-Radziszowski and Angeltveit-McKay.

## What counts as a win

Either (a) an explicit graph G on N vertices (adjacency matrix or graph6) such that G contains no copy of the first graph and the complement contains no copy of the second (K_k or K_k - e as in the cell), checked exhaustively by two independent programs, with N+1 STRICTLY GREATER (direction: max) than the lower bound for that cell in the live DS1 (https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1, latest revision) and in any newer paper found by a fresh arXiv search for that exact cell; or (b) an upper bound STRICTLY BELOW (direction: min) the DS1 upper bound, backed by a machine-checkable certificate: a DRAT/LRAT/FRAT UNSAT proof of a stated encoding that a referee can regenerate, plus a machine-checked or fully written reduction, or an exact-rational flag-algebra certificate that an independent script verifies. Off-by-one: a graph on N vertices proves R >= N+1.

## Partial wins

- **p1:** A new lower bound for a cell that DS1 item 3.1.e lists outside Tables IIIa/IIIb (R(K4-e,K16-e) >= 82, R(K4,K12-e) >= 128, R(K14-e,K14-e) >= 2987): an explicit verified graph whose order plus one strictly exceeds the listed bound and every newer published bound.
- **p2:** An exact value: a cell of Table IIIa/IIIb settled by a verified lower-bound graph matching a verified (certificate-backed) upper bound, where both are new or one is new and the other is already published.

## How a win is checked

For a lower bound: parse the graph, confirm symmetry and order N, then search exhaustively for every forbidden subgraph in G and in its complement with (i) a bitset clique enumerator that, for K_k - e, looks for a K_{k-2} inside the common neighbourhood of every edge and non-edge as appropriate, and (ii) a SAT/CP encoding that must return UNSAT; both must agree. For an upper bound: rerun the stated encoding, check the proof with drat-trim or cake_lpr, and audit the reduction. Re-fetch DS1 and grep arXiv for the cell (e.g. "K_4-e", "K_8-e") before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/>
- <https://arxiv.org/abs/2606.17021>
- <https://github.com/Steven-VO/circulant-Ramsey>
- <https://arxiv.org/abs/1704.03592>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Block-circulant (2- and 3-block polycirculant) graphs, the method behind most Van Overberghe bounds, searched with SAT over connection sets.
- Strongly regular graphs from Brouwer's table: Van Overberghe got R(K5-e,K6-e) = 37 and R(K5-e,K7-e) = 65 from Schlafli, NO-(6,2) and VO-(6,2); try induced subgraphs of other srgs.
- One-vertex extension of known critical graphs with SAT for the new neighbourhood.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- R(K4-e,K7) is now 28 (Wesley 2026); DS1 still shows 28-29.
- Several upper bounds are trivially implied by Table Ib (classical numbers); improving them may need a new R(k,l) upper bound first.
- K_k - e versus K_k: check which side of the cell avoids which graph; the table is not symmetric in rows and columns.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/ramsey-kk-minus-e-table-gaps.md
```

Already set up? Say `run V3R1T4S on ramsey-kk-minus-e-table-gaps`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ramsey-kk-minus-e-table-gaps`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
