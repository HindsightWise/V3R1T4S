# LeanCamCombi: formal proof of the van den Berg-Kesten-Reimer inequality (card_certificator_le)

✅ **Formal proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The van den Berg-Kesten inequality says that disjoint occurrence of two events is at most as likely as their joint product. It was conjectured for all events by van den Berg and Kesten (1985) and proved by D. Reimer (2000). YaelDillies/LeanCamCombi (Yaël Dillies; master bc7d1c9, 2026-10-29, Lean v4.36.0-rc2) defines the certificator 𝒜 □ ℬ of two set families in CamCombi/PlainCombi/VanDenBergKesten.lean (a ∈ 𝒜 □ ℬ iff some complementary pair x, y witnesses membership of a in 𝒜 through a ⊓ x and in ℬ through a ⊓ y). It states the uniform-measure inequality `lemma card_certificator_le : 2 ^ Fintype.card α * #(𝒜 □ ℬ) ≤ #𝒜 * #ℬ := sorry`, tracked as issue #34 (open since 2025-01-22, unassigned, no linked PR). No Lean proof was found in Mathlib, lean-pool (project list scanned 2026-10-30) or lean-eval's problem list. The upper-set/lower-set case already follows from Mathlib's Harris-Kleitman inequality.

## What counts as a win

Success means a sorry-free proof of `Finset.card_certificator_le` exactly as stated on live LeanCamCombi master, re-fetched immediately before claiming (the statement and the certificator definition are diff-checked). Issue #34 must still be open with no PR proving the lemma. The proof must compile with `lake build` at the pinned toolchain and manifest, and `#print axioms` must show only propext/Classical.choice/Quot.sound (no native_decide, no new axiom).

## Partial wins

- **p1:** The inequality for up-sets: if 𝒜 and ℬ are both upper sets, 2^n · #(𝒜 □ ℬ) ≤ #𝒜 · #ℬ (the original van den Berg-Kesten case; IsUpperSet.certificator_eq_disjSups in the file rewrites 𝒜 □ ℬ as 𝒜 ○ ℬ), proved sorry-free as a separate lemma.

## How a win is checked

Clone master, `lake exe cache get`, apply the patch, `lake build`, `#print axioms Finset.card_certificator_le`, grep for forbidden tokens, diff the statement and definition, and check issue #34 and open PRs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/YaelDillies/LeanCamCombi/issues/34>

## Sources

- <https://github.com/YaelDillies/LeanCamCombi/blob/master/CamCombi/PlainCombi/VanDenBergKesten.lean>
- <https://github.com/YaelDillies/LeanCamCombi/issues/34>
- <https://github.com/YaelDillies/LeanCamCombi>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reimer's proof (2000) rests on his 'butterfly' lemma about the Boolean cube. Expositions include Borgs-Chayes-Randall's review of the BKR inequality and the account in Bollobás-Riordan, Percolation. Formalise the butterfly lemma first, then the reduction.
- p1: van den Berg-Kesten's original argument for increasing events, by induction on the number of coordinates (split off one coordinate and compare the conditional families).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Lean statement is for the uniform measure on subsets of a finite type. Weighted product versions are not required, and a proof for them may not specialise trivially.
- Check that IsCompl in the definition matches disjoint witness sets (it does by monotonicity). Do not change the definition.
- The case of an upper set and a lower set is not a win: it follows in two lines from IsUpperSet.certificator_eq_inter and Mathlib's IsUpperSet.card_inter_le_finset.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/leancamcombi-bkr-reimer-inequality.md
```

Already set up? Say `run V3R1T4S on leancamcombi-bkr-reimer-inequality`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `leancamcombi-bkr-reimer-inequality`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
