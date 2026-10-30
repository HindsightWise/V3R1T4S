# Imperial FLT project: fill an unclaimed Prop-valued sorry (de Smit-Lenstra representability, compact exponent-p groups, quaternion base change)

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (full FLT build is long; build the touched module and its dependents, then lake build once) · open as of 2026-10-30

## The problem

The Imperial College FLT project (ImperialCollegeLondon/FLT, led by Kevin Buzzard on the route planned with Richard Taylor; Lean v4.35.0 at main a321020, 2026-10-22) has 60 live `sorry` terms in 20 files (a plain grep finds 65 lines in 24 files, five of them docstring mentions). Tasks are GitHub issues, claimed by comment and bot-assigned; the org project board needs a GitHub sign-in to view. Most sorries are claimed or touched by open PRs: HurwitzRatHat (#1115, #1178, #1183), EllipticCurve/Torsion (#1155, #1177, #1207; #1209 points to Mathlib PR #45439), KnownIn1980s/EllipticCurves/Torsion.lean torsion_rank_two (issue #1064, claimed by CBirkbeck), TateCurve (#1109), Flat/GoodReduction (#1080), HardlyRamified Frey/Lift/ModThree/Threeadic (#761), GLnDefs (#1210), GLzero (#1155). Others sit inside definitions (weilPairing, the GLzero fields, the map field of flatFunctor in Deformations/LiftFunctor.lean) or are copies proved elsewhere (Dickson classification in KnownIn1980s/PGL2/Defs.lean, proved in PGL2/Proofs.lean). The instance IsQuaternionAlgebra E (E ⊗[F] D) in Automorphic.lean is excluded: its core (a central simple algebra tensor a simple ring is simple) is issue #631, assigned to Whysoserioushah. Two theorems are out of reach because their statements use sorried definitions, so `#print axioms` keeps sorryAx however they are proved: isCorepresentable_narrowSLiftFunctor (through flatFunctor) and B4_proof in FLT/Proof.lean (through WeierstrassCurve.galoisRep). Prop-valued sorries with no open PR and no assigned or claimed issue on 2026-10-30: Group.subsingleton_of_pow_prime_eq_one in FLT/Patching/Utils/CompactHausdorffRings.lean (a connected compact Hausdorff abelian group of exponent p is trivial); isCorepresentable_deformationFunctor (de Smit-Lenstra Prop. 2.3(1)) in FLT/Deformations/Representable.lean; cyclic_base_change in GaloisRepresentation/Automorphic.lean; and mem_isCompatible in HardlyRamified/Family.lean. A separate complete Lean proof of FLT exists (anthropics/fermats-last-theorem, Apache-2.0, unmaintained); this target is the Imperial declarations with their own definitions. Target: prove one.

## What counts as a win

Success means a patch that replaces exactly one Prop-valued `sorry` (a theorem, lemma or Prop-valued instance, never a sorry inside a def or structure) in a declaration on live FLT main, re-fetched immediately before claiming. At that moment the declaration must not be touched by any open FLT pull request, must not be named in an assigned or claimed issue, and must not already be proved in the repository under another name (as the PGL2 Defs/Proofs pair is). Its statement must not depend on a sorried definition (isCorepresentable_narrowSLiftFunctor and B4_proof do on 2026-10-30). The instance IsQuaternionAlgebra E (E ⊗[F] D) is excluded while issue #631 is open. The statement must be unchanged (diff-checked). The project must compile with `lake build` at the pinned lean-toolchain and lake-manifest. `#print axioms` on the declaration must show only a subset of {propext, Classical.choice, Quot.sound}: no sorryAx, no knownin1980s, Mazur_statement or Odlyzko_statement, no new axiom, no native_decide. No PR is opened and no issue is claimed. The claim is for the checked patch.

## Partial wins

- **p1:** Group.subsingleton_of_pow_prime_eq_one (or its additive version, which @[to_additive] generates) proved sorry-free in the FLT repo with the statement unchanged, using only Mathlib and FLT lemmas that are already sorry-free.
- **p2:** A sorry-free Lean proof, in a separate file that compiles against FLT main, of de Smit-Lenstra Prop. 2.3(1) for one explicit finite group G (e.g. G cyclic of prime order), stated through the FLT `deformationFunctor` API: the special case is corepresentable.

## How a win is checked

Clone the FLT repository at the stated commit, fetch the Mathlib cache, apply the patch and run lake build; then print the axioms of the declaration and require only the standard ones. Search the diff for sorry, admit, axiom, native_decide, implemented_by and extern, and compare the statement with the original. Check the project's open pull requests and issues for the same declaration, so the claim is not already taken.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/ImperialCollegeLondon/FLT/issues>

## Sources

- <https://github.com/ImperialCollegeLondon/FLT>
- <https://github.com/ImperialCollegeLondon/FLT/issues>
- <https://github.com/orgs/ImperialCollegeLondon/projects/102>
- <https://imperialcollegelondon.github.io/FLT/blueprint/>
- <https://github.com/ImperialCollegeLondon/FLT/blob/main/CONTRIBUTING.md>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- p1: a nontrivial compact Hausdorff abelian group has a nontrivial continuous character. The docstring says YaelDillies/mean-fourier is building this, so check whether it has landed in Mathlib or mean-fourier before building it again. An alternative route is to show that a compact Hausdorff group of exponent p is totally disconnected via the open-subgroup structure of compact groups.
- Representability: Schlessinger's criteria or the de Smit-Lenstra explicit construction (a quotient of a power series ring by the universal relations); check what the FLT Deformations folder already provides.
- anthropics/fermats-last-theorem (Apache-2.0, a complete FLT proof on a different route) contains elliptic-curve and representation-theory lemmas that may port. Credit it, and check that the definitions match before porting.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A sorry inside a def or structure field can be 'filled' with junk that type-checks, or sits under a definition other theorems use. These never count.
- Some sorried statements in Defs files are proved as copies elsewhere (PGL2/Proofs.lean). Filling a duplicate is not a new result.
- The project moves quickly and AI-assisted PRs appear weekly. Re-list open PRs and claims just before claiming.
- `knownin1980s` is an axiom: a proof that uses it does not count.
- `#print axioms` also collects axioms from the definitions in the statement. Before starting, run it on the still-sorried declaration: anything beyond sorryAx and the three standard axioms comes from the statement and cannot be removed. cyclic_base_change imports AutomorphicForm/QuaternionAlgebra/Basic.lean, where the instance isFiniteRelIndex_Δ is proved by knownin1980s; check that it does not reach the Hecke algebra in the statement.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/flt-imperial-unclaimed-prop-sorries.md
```

Already set up? Say `run V3R1T4S on flt-imperial-unclaimed-prop-sorries`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `flt-imperial-unclaimed-prop-sorries`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
