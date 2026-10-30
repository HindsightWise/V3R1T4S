# Physlib semiformal result FXNL5: the restricted Lorentz group SO+(1,d) is connected

✅ **Formal proofs** · standard · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Physlib (leanprover-community/physlib, formerly HepLean/PhysLean, founded by Joseph Tooby-Smith; master a4f5411, 2026-10-30) lists its open formal items on its auto-generated TODO page. Its one Lean-stated 'semiformal result' is tag FXNL5 in Physlib/Relativity/LorentzGroup/Restricted/Basic.lean: `semiformal_result "FXNL5" restricted_isConnected {d : ℕ} : IsConnected (restricted d : Set (LorentzGroup d))`. Here `restricted d` is the subgroup of proper (det 1) and orthochronous (Λ₀₀ ≥ 0) Lorentz transformations. A conditional lemma in the same file, restricted_eq_identity_component_of_isConnected, already derives `restricted d = connectedComponent 1` from it. Much of the route is already formalised and sorry-free. Restricted/FromBoostRotation.lean has the homeomorphism `toBoostRotation : restricted d ≃ₜ Lorentz.Velocity d × Matrix.specialOrthogonalGroup (Fin d) ℝ` and `exists_boost_mul_rotation`, and `Lorentz.Velocity.isPathConnected` shows the velocity factor is path-connected. What is missing is connectedness of SO(d) = Matrix.specialOrthogonalGroup (Fin d) ℝ, which Mathlib (pinned 56a0058) does not have, plus the transfer from the subtype to the set. None of physlib's 69 open PRs on 2026-10-30 touches Relativity/LorentzGroup (the only Lorentz-titled one, #968, refactors the Lorentzian metric elsewhere).

## What counts as a win

Success means a sorry-free Lean proof of `IsConnected (LorentzGroup.restricted d : Set (LorentzGroup d))` for all d : ℕ. It must use physlib's definitions as they stand on live main (re-fetched immediately before claiming; statement diff-checked) and be stated as a theorem replacing the semiformal_result. It must compile with `lake build` at physlib's pinned toolchain, and `#print axioms` must show only propext/Classical.choice/Quot.sound (no native_decide, no new axiom). The FXNL5 entry must still be open on the TODO page or in the source at claim time.

## Partial wins

- **p1:** The case d = 2, `IsConnected (LorentzGroup.restricted 2 : Set (LorentzGroup 2))`, proved sorry-free as a separate theorem against physlib's definitions.
- **p2:** The case d = 3, `IsConnected (LorentzGroup.restricted 3 : Set (LorentzGroup 3))`, proved sorry-free as a separate theorem against physlib's definitions.

## How a win is checked

Clone physlib main, `lake exe cache get`, replace the semiformal_result with the theorem, `lake build`, `#print axioms`, diff the statement, and check the physlib TODO page and open PRs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://physlib.io/todo>

## Sources

- <https://physlib.io/todo>
- <https://github.com/leanprover-community/physlib/blob/master/Physlib/Relativity/LorentzGroup/Restricted/Basic.lean>
- <https://github.com/leanprover-community/physlib>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use toBoostRotation: restricted d is homeomorphic to Velocity d × SO(d), and Velocity d is already path-connected, so it suffices to prove Matrix.specialOrthogonalGroup (Fin d) ℝ connected and push connectedness through the homeomorphism and the subtype coercion.
- For SO(d): induct on d using Givens (plane) rotations, which join any element to 1 one coordinate plane at a time; or use the fibration SO(d) → S^{d-1}, A ↦ A e₁, with fibre SO(d-1). For d = 2, SO(2) is the continuous image of the circle under the rotation-matrix map.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- d = 0 is a degenerate case (restricted 0 is trivial). Make sure the proof covers it rather than adding a hypothesis.
- Physlib refactors often. Re-check the definitions of IsProper and IsOrthochronous, and the statement of toBoostRotation, on master before claiming.
- The boost-times-rotation decomposition (exists_boost_mul_rotation) and the case d = 1 (SO(1) is a single point) already follow from existing physlib code and are not wins on their own.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/physlib-restricted-lorentz-connected.md
```

Already set up? Say `run V3R1T4S on physlib-restricted-lorentz-connected`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `physlib-restricted-lorentz-connected`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
