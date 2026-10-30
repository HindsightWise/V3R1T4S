# Clay Class Field Theory project: Herbrand quotient of local units and unramified cohomology vanishing

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

kbuzzard/ClassFieldTheory, the repository of the 2025 Clay summer school Formalizing Class Field Theory, is an ongoing project led by Kevin Buzzard to formalise local and global class field theory, with a blueprint (main d48e8a0, 2026-10-29, Lean v4.36.0-rc2). Open PRs cover Tate cohomology shifting (#193, plp127, UpDown.lean) and inflation-restriction (#190 by Whysoserioushah, #68 by Paul-Lez). The Corestriction sorries are inside comments, and the instances in IsNonarchimedeanLocalField/Instances.lean (imported only by the root ClassFieldTheory.lean) have sorry-free replacements in Actions.lean; its lemma valuation_ringEquiv (every ring automorphism of a local field preserves the valuation) has no counterpart there. Live sorries outside those, on 2026-10-30: Rep.herbrandQuotient_isNonarchimedeanLocalField_integer_units in IsNonarchimedeanLocalField/HerbrandQuotient.lean (the Herbrand quotient of the integral units of a cyclic extension of local fields is 1, marked 'hard work' with a blueprint link); the instance Subsingleton (groupCohomology (Rep.units Gal(L/K) 𝒪[L]) q) for unramified L/K and q > 0 in UnramifiedCohomology.lean; and Algebra.unramifiedLocus_eq_univ_iff' and Algebra.isOpen_unramifiedLocus' in IsNonarchimedeanLocalField/Basic.lean (universe-polymorphic versions of Mathlib lemmas). Target: prove one.

## What counts as a win

Success means a patch replacing one live `sorry` (not one inside a comment, and not in a file touched by an open PR) on ClassFieldTheory main, re-fetched immediately before claiming, with the statement unchanged (diff-checked). `lake build` must succeed at the pinned toolchain and manifest, and `#print axioms` on the declaration must show only propext/Classical.choice/Quot.sound (no sorryAx, no native_decide, no new axiom). Declarations in Instances.lean whose sorry-free version already exists in Actions.lean do not count.

## Partial wins

- **p1:** Algebra.unramifiedLocus_eq_univ_iff' or Algebra.isOpen_unramifiedLocus' proved sorry-free with the statement unchanged (deriving them from the Mathlib versions is fine).
- **p2:** The unramified-cohomology Subsingleton instance proved sorry-free for q = 1 only, stated as a separate lemma with the same hypotheses.

## How a win is checked

Clone main, `lake exe cache get`, apply the patch, `lake build`, `#print axioms`, grep for forbidden tokens, diff the statement, and check the open PR file lists.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/kbuzzard/ClassFieldTheory>

## Sources

- <https://github.com/kbuzzard/ClassFieldTheory>
- <https://kbuzzard.github.io/ClassFieldTheory/blueprint/>
- <https://github.com/kbuzzard/ClassFieldTheory/pulls>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Herbrand quotient of units: take a finite-index open subgroup of the units that is cohomologically trivial (via the exponential or an induced module from a normal basis), then use multiplicativity of the Herbrand quotient in short exact sequences and h(finite) = 1, which the repo already has in Cohomology/FiniteCyclic/HerbrandQuotient.
- Existing formalisations to study or port, with credit, after checking the definitions match: TauCeti/NumberTheory/LocalField/UnitFiltration/HerbrandQuotient.lean (TauCeti project) and anthropics/fermats-last-theorem Theorems/Thm_M4aLocalCFT_unitsDecomp_herbrandQuotient_eq_one.lean (Apache-2.0).
- Unramified case: filter the units by 1 + 𝔪^n. The graded pieces are residue-field modules with trivial cohomology by Hilbert 90 and the additive normal basis theorem over finite fields. Pass to the limit by completeness.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several 'sorry' hits in a plain grep are inside comments (Corestriction.lean). They are not tasks.
- The instances in Instances.lean are superseded by the sorry-free Actions.lean. Proving those old copies is not a win (valuation_ringEquiv, which Actions.lean does not cover, still counts).
- Cohomology/TrivialityCriterion.lean uses δDownResIsoTate, a sorried definition in Cohomology/Functors/UpDown.lean (open PR #193). A proof routed through the triviality criterion carries sorryAx until that sorry is filled upstream, so check `#print axioms` early.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/clay-cft-local-field-sorries.md
```

Already set up? Say `run V3R1T4S on clay-cft-local-field-sorries`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `clay-cft-local-field-sorries`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
