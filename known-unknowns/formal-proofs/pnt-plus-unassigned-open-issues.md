# PrimeNumberTheoremAnd (PNT+): close an unassigned open formalisation issue (IK identities, Rosser-Schoenfeld prime sums, Dusart table bounds)

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The PNT+ project (AlexKontorovich/PrimeNumberTheoremAnd, toolchain v4.35.0) tracks remaining `sorry`s as GitHub issues. On 2026-10-28 there are 27 open issues, 11 of them unassigned (#1240, #1685, #1688, #1690, #1692, #1694, #1762, #1773, #1774, #1775, #1796). Several of those are already claimed. #1685 isCompletelyMultiplicative_liouville and #1690 zeta_pow_four_eq (IK 1.29) are in PR #1772. #1762 pi_inequality and #1773-#1775 (theta bounds from Dusart Table 4.2) are in PR #1799. #1688 zeta_mul_zeta_mul_zeta_mul_zeta_eq (Ramanujan identity, IK 1.28) is in open PR #1730 (Robby955, since 1 Aug 2026), and the same declaration is tracked by issue #1242, assigned to KanCup. #1240 (upstream a lemma to Mathlib) and #1796 (attribution) are not sorry-filling tasks. That leaves #1692 RS_prime.theorem_d (sum log p / p < log x for x > 1) and #1694 RS_prime.theorem_c (sum 1/p > log log x for x > 1), both in PrimeNumberTheoremAnd/IEANTN/TMEEMT.lean, as unassigned sorries with no open PR. Target: fill one such sorry.

## What counts as a win

Success means: for one issue that is still open and unassigned on https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues, whose named declaration is not targeted by any open pull request or by any other open, assigned issue (including PRs and issues that name the declaration without citing this issue number), all re-fetched live immediately before claiming, the named declaration on live main still contains `sorry`, and a patch to that declaration only (statement unchanged, diff-checked) makes the project compile with `lake build` at the pinned toolchain, with `#print axioms` on the declaration showing only propext/Classical.choice/Quot.sound (no sorryAx, no new axiom, no native_decide). No PR is opened; the claim is for the checked patch.

## Partial wins

- **p1:** RS_prime.theorem_c (#1694) or RS_prime.theorem_d (#1692) proved for all x >= X0 for an explicit X0, derived from statements already formalised in the project (Mertens-type, Rosser-Schoenfeld or Dusart bounds), with the remaining range 1 < x < X0 stated as a separate, clearly named lemma; kernel-checked, statement unchanged, if no open PR claims the declaration at verification time.
- **p2:** A kernel-checked proof (no native_decide) of the finite-range part 1 < x < X0 of RS_prime.theorem_c or RS_prime.theorem_d for an explicit X0 >= 10^4, via a reflected prime table and rational interval bounds for the logarithms, stated as a separate lemma that composes with the large-x part.

## How a win is checked

Clone PNT+ main, `lake exe cache get`, apply patch, `lake build` (or build only the affected module and dependents), `#print axioms` on the target, grep diff for forbidden tokens, confirm the statement text is unchanged.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues>

## Sources

- <https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues>
- <https://github.com/AlexKontorovich/PrimeNumberTheoremAnd>
- <https://alexkontorovich.github.io/PrimeNumberTheoremAnd/blueprint/dep_graph_document.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- RS prime-sum bounds: split into x >= X0 (from already-formalised Rosser-Schoenfeld/Dusart/Mertens-type statements in the project) and 1 < x < X0 by a kernel-checked prime table via reflection.
- Cross-domain import (numerical analysis / validated numerics in control engineering): use interval arithmetic with outward rounding encoded in rationals to certify the finite-range inequalities, the same way flight-control verification certifies polynomial bounds.
- Cross-domain import (accounting reconciliation): treat the explicit-constant chain as a ledger: tabulate every constant from the source tables with its source row and cross-foot them before formalising, catching transcription errors early.
- Check each issue's linked PRs, the open PR list and other issues naming the same declaration first: in 2026 contributors bundled several issues into single PRs (#1772, #1799), and IK 1.28 is claimed by PR #1730 and by assigned issue #1242.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Issues get assigned or closed, or bundled into other people's PRs, quickly; re-check the live issue state, open PRs and the main branch before claiming.
- Changing the declaration's statement (e.g. weakening a constant) is not a fix.
- Building all of PNT+ is long; partial module builds can miss downstream breakage: run the full `lake build` before claiming.
- Explicit constants: a misread table row (e.g. 0.78 vs 0.078) gives a false or unprovable bound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/pnt-plus-unassigned-open-issues.md
```

Already set up? Say `run V3R1T4S on pnt-plus-unassigned-open-issues`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pnt-plus-unassigned-open-issues`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
