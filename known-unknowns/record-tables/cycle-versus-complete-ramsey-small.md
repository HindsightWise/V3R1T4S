# Cycles versus complete graphs: close R(C4,K11) 40-43, R(C4,K12) 43-51 or R(C5,K9) 33-36

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for lower bounds; needs cluster or flag algebras for upper bounds · open as of 2026-10-30

## The problem

R(C_n, K_m) is the least N such that every graph on N vertices contains an n-cycle or an independent set of size m. DS1 revision #18 (Apr 2026), Table Vb, lists the small open cases 40 <= R(C4,K11) <= 43 (Van Overberghe; Boza-Radziszowski), 43 <= R(C4,K12) <= 51 (Boza-Radziszowski 2025) and 33 <= R(C5,K9) <= 36 (Lidicky-Pfender). The Erdos-Faudree-Rousseau-Schelp conjecture R(C_n,K_m) = (n-1)(m-1)+1 for n >= m >= 3 (except n = m = 3) is still open for many small cells marked 'conj.' in the table, for example R(C9,K9) = 65 (proved for n >= 4m+2 by Nikiforov, for n >= m(m-2) by Schiermeyer, and for large n by Keevash-Long-Skokan). Erdos also asked for a proof that R(C4,K_m) < m^(2-eps). No 2026 arXiv paper found changes these cells.

## What counts as a win

Either (a) an explicit graph G on N vertices with no C_n (as a subgraph) and independence number less than m, checked by two independent exact programs, with N+1 STRICTLY GREATER (direction: max) than the DS1 lower bound for that cell and any newer published bound; or (b) an upper bound STRICTLY BELOW (direction: min) the DS1 upper bound for R(C4,K11), R(C4,K12) or R(C5,K9), backed by an exact-rational flag-algebra certificate or a DRAT/LRAT UNSAT certificate with a sound, checkable reduction. Off-by-one: a graph on N vertices proves R >= N+1.

## Partial wins

- **p1:** A machine-checked proof (Lean/Isabelle, or SAT certificates over a formalised reduction) of the conjectured value for one 'conj.' cell of Table Vb with m <= 9, such as R(C9,K9) <= 65, where no published proof exists.
- **p2:** An end-to-end certified re-verification of a published Table Vb upper bound that has no public checkable certificate, such as R(C4,K10) <= 36 [LaLR]: DRAT/LRAT proofs of a stated encoding with a checkable reduction (or an exact-rational flag-algebra certificate), released with a re-run script.

## How a win is checked

C4: check that A^2 off-diagonal entries are at most 1. C5: for each vertex v and each pair of neighbours, test for a path of length 3 avoiding v (exact search), cross-checked by a SAT encoding. Independence number: exact maximum clique of the complement with two solvers (bitset branch-and-bound and a SAT/MaxSAT query). For certificates: drat-trim/cake_lpr or an exact rational SDP checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/>
- <https://arxiv.org/abs/1704.03592>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- R(C3,K_m) is the classical R(3,m), covered by the small-ramsey-lower-bounds target; stay with n >= 4.
- Off-by-one: R(C4,K11) >= 40 is witnessed by a 39-vertex graph. A record needs a C4-free graph on 40 vertices with independence number at most 10 (R(C4,K11) >= 41). For R(C4,K12) it needs one on 43 vertices with independence number at most 11.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/cycle-versus-complete-ramsey-small.md
```

Already set up? Say `run V3R1T4S on cycle-versus-complete-ramsey-small`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cycle-versus-complete-ramsey-small`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
