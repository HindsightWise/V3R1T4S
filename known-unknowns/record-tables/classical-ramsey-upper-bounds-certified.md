# MOONSHOT - Classical Ramsey upper bounds with machine-checkable certificates: R(3,3,3,3) <= 60, R(3,10) <= 40, R(4,6) <= 39, R(5,5) <= 45, R(3,3,5) <= 56, R(3,4,4) <= 76

📊 **Record tables** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (SAT cube-and-conquer over gluing or neighbourhood classifications; proofs of terabyte scale are possible) · open as of 2026-10-30

## The problem

Upper bounds for classical Ramsey numbers R(k1,...,kr) (no monochromatic K_{k_i} in colour i) move rarely and only by massive certified computation. Current values: R(3,3,3,3) <= 61 by Milos Tatarevic (arXiv:2610.36648, 27 Oct 2026; Lean-formalised reductions plus SAT refutations with two solvers), improving 62 of Fettes-Kramer-Radziszowski (2004); lower bound 51 (Chung). R(3,10) <= 41 (Angeltveit, E-JC 2025), lower 40. Angeltveit-McKay's 2019-2024 bounds R(4,6) <= 40, R(5,5) <= 46 (DS1 Table Ib). Three colours: R(3,3,5) <= 57, R(3,4,4) <= 77 (from the recurrence 6.1.a), R(3,3,6) <= 91, R(3,4,5) <= 157, R(4,4,4) <= 229 (Boza, arXiv:2603.10851), R(3,3,3,4) <= 149. R(3,3,4) = 30 (Codish-Frank-Itzhakov-Miller 2016) is settled. Source of the table: DS1 revision #18 (Apr 2026), Tables Ia/Ib and Section 6.1, plus the Tatarevic preprint. This target covers upper bounds only; explicit lower-bound constructions belong to small-ramsey-lower-bounds.

## What counts as a win

An upper bound STRICTLY BELOW (direction: min) the best published upper bound for one of R(3,3,3,3), R(3,10), R(4,6), R(5,5), R(3,3,5), R(3,4,4), R(3,3,6), R(3,4,5), R(4,4,4) or R(3,3,3,4) at verification time (DS1 latest revision, arXiv:2610.36648, arXiv:2603.10851 and a fresh arXiv search), backed by a certificate a stranger's computer can check end to end: every combinatorial reduction machine-checked (Lean/Isabelle/HOL4) or reduced to finite statements, and every finite case refuted by a DRAT/LRAT/FRAT proof that verifies with drat-trim, cake_lpr or an equivalent checker, or by an exact-rational LP/SDP certificate. A computation without checkable certificates is at most PROMISING.

## Partial wins

- **p1:** An independent, fully certified re-verification of a published bound whose main computation currently lacks public checkable certificates, released with the proofs and a re-run script: e.g. R(3,3,3,3) <= 61 (Tatarevic's 56,723 K61 refutations are two-solver UNSAT answers without DRAT/LRAT logs; only the 55 classification pairs are LRAT-certified), R(4,6) <= 40, R(5,5) <= 46 or R(3,10) <= 41.
- **p2:** A certified upper bound strictly below the current recurrence (6.1.a) value for a multicolour number not in the main list and not improved in any published source, such as R(3,3,4,4) <= 449 (recurrence value 450) or R(3,3,3,3,3) <= 301 (the recurrence with R(3,3,3,3) <= 61 gives 302; DS1 shows 307).

## How a win is checked

Rebuild every CNF from the stated reduction with an independent generator, check the reduction's formal proof in its proof assistant, check each SAT refutation with drat-trim/cake_lpr (LRAT preferred), and confirm the cases cover the whole space (hash the case list). For LP/SDP certificates, verify feasibility and the bound in exact rational arithmetic.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://arxiv.org/abs/2610.36648>
- <https://arxiv.org/abs/2603.10851>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- DS1 (Apr 2026) still shows R(3,3,3,3) <= 62; the live bound is 61 (Tatarevic, Oct 2026).
- With R(3,3,3,3) <= 61 the recurrence 6.1.a gives R(3,3,3,3,3) <= 302, not DS1's 307; recompute every recurrence-derived bound before calling one new.
- Upper bounds implied only by recurrences from smaller improved bounds count only if the smaller bound itself is new and certified.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/classical-ramsey-upper-bounds-certified.md
```

Already set up? Say `run V3R1T4S on classical-ramsey-upper-bounds-certified`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `classical-ramsey-upper-bounds-certified`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
