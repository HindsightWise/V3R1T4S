# MOONSHOT - LeanAPAP: formal proof of the Kelley-Meka bound for 3AP-free sets of integers (corrected form of theorem `int`)

✅ **Formal proofs** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

Kelley and Meka (2023, arXiv 2302.05537) proved that a 3AP-free A ⊆ {1..N} has |A| ≤ N/exp(c (log N)^{1/12}). Bloom and Sisask (arXiv 2302.07211) improved the exponent to 1/9. YaelDillies/LeanAPAP (Yaël Dillies and Bhavik Mehta; master b200197, 2026-10-22, Lean v4.36.0-rc1) formalises the finite-field analogue: theorem `ff` in APAP/FiniteField.lean, with open PR #19 adding Comparator CI for it. The integer case is a bare `sorry` in APAP/Integer.lean, and as written it is false: `theorem int : ∃ c > 0, ∃ C > 0, ∀ ⦃A : Finset ℕ⦄ ⦃N : ℕ⦄, A ⊆ range N → ThreeAPFree (α := ℕ) A → #A ≤ N / exp (c * log N ^ (12⁻¹ : ℝ))` never uses C, and N = 2, A = {0, 1} gives 2 ≤ 2/exp(c (log 2)^{1/12}) < 2 for every c > 0. The intended statement has C in front of N. Issue #25 (closed 2026-09-28) reported this counterexample together with a quantifier-order bug; the fix moved the constants in front and added C but left C out of the bound. The maintainer notes that development now happens mostly in YaelDillies/mean-fourier, which has no integer theorem either. The missing mathematics is the Bohr-set version of the almost-periodicity and density-increment steps. Prerequisites are also unproved, among them Bohr set regularity (`BohrSet.regularity` in APAP/Prereqs/Bohr/Regular.lean, also a sorry in mean-fourier); the NewMarcinkiewiczZygmund sorries are in open PR #20. No Lean proof of the integer bound is in LeanAPAP, mean-fourier or Mathlib.

## What counts as a win

Success means a sorry-free Lean theorem compiling against live LeanAPAP master (re-fetched immediately before claiming) at its pinned toolchain and manifest, with `open Finset Real` as in APAP/Integer.lean and statement exactly `∃ c > 0, ∃ C > 0, ∀ ⦃A : Finset ℕ⦄ ⦃N : ℕ⦄, A ⊆ range N → ThreeAPFree (α := ℕ) A → (#A : ℝ) ≤ C * N / exp (c * log N ^ (12⁻¹ : ℝ))` (statement diff-checked). `#print axioms` on it must show only a subset of {propext, Classical.choice, Quot.sound}, with no native_decide and no new axiom. Proving `int` as currently written is impossible, because it is false.

## Partial wins

- **p1:** BohrSet.regularity in APAP/Prereqs/Bohr/Regular.lean proved sorry-free with the statement unchanged.
- **p2:** A sorry-free Lean theorem compiling against LeanAPAP of the same shape as the success statement (∃ c > 0, ∃ C > 0, (#A : ℝ) ≤ C * N / exp (c * log N ^ e)) with a fixed exponent e with 0 < e < 1/12, or the same bound with exponent 1/12 for 3AP-free subsets of ZMod N with N prime, stated as a separate theorem.

## How a win is checked

Clone LeanAPAP master, `lake exe cache get`, apply the patch, `lake build`, `#print axioms int` (or the partial-win theorem), grep for forbidden tokens, diff the statement.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/YaelDillies/LeanAPAP>

## Sources

- <https://github.com/YaelDillies/LeanAPAP>
- <https://github.com/YaelDillies/LeanAPAP/blob/master/APAP/Integer.lean>
- <https://arxiv.org/abs/2302.05537>
- <https://arxiv.org/abs/2302.07211>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Follow Bloom-Sisask section by section. The finite-field proof `ff` is a template: subspaces become regular Bohr sets, and almost periodicity is already formalised.
- An easier route to a weaker statement for p2 is to embed {1..N} in Z/pZ with p ≈ 2N and run the finite-group density increment.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- `int` as written is false at N = 2 (C is unused). A kernel-checked disproof is easy, already exists (linked from issue #25), and is not a win. Prove the corrected statement.
- Natural-number subtraction and `log` of 0 and 1 make small N degenerate; the constant C must absorb them.
- If upstream corrects `int` to a different form before the claim, the claim is still judged against the statement fixed in the success criterion.
- APAP/Prereqs/DummyPositivity.lean holds sorried dummy lemmas behind unsound `positivity` extensions (APAP/Prereqs/Convolution/Order.lean, imported by FiniteField). A proof that calls `positivity` on convolution terms can silently depend on sorryAx. Run `#print axioms` early and often, not only at the end.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/leanapap-kelley-meka-integer-bound.md
```

Already set up? Say `run V3R1T4S on leanapap-kelley-meka-integer-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `leanapap-kelley-meka-integer-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
