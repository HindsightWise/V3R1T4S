# Formal Conjectures: research-solved sorries closable by an explicit finite witness (R(5,5) > 42 graph, small Hadamard orders, ...)

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

In formal-conjectures (commit 5a2fb85, 2026-10-28, toolchain v4.33.1) a scan finds about 517 theorems tagged `research solved` outside the ErdosProblems, WrittenOnTheWallII and OEIS folders (those have their own bank entries) that still end in `sorry` with no `formal_proof` attribute. A subset are existential or finite statements whose known proof is an explicit object plus a finite check, e.g. Wikipedia/RamseyNumbers.lean `ramsey_number_five_five_lower_bound` (a graph on Fin 42 with no 5-clique and no 5-independent set; Exoo 1989). A much harder finite item is Wikipedia/Hadamard.lean `HadamardConjecture.variants.first_cases`, stated on main as `668 ≤ hadamardConstant`: a Hadamard matrix (FC's IsHadamard, defined via |det M| = n^(n/2)) must exist for every order 4k with k ≤ 166. That needs explicit matrices for all such orders, including ones that need Williamson-type or later constructions (e.g. order 428), far beyond Sylvester and Paley alone. Several earlier examples are now taken: the non-abelian Leinster group and R(3,3), R(3,4), R(3,5), R(4,4) have formal_proof links proposed in open FC PRs #6953 and #7660, and the Steiner system S(5,8,24) in #7660. Textbook-tagged items (BB(2), the irregular prime 37, OEIS textbook facts) belong to the separate textbook-sorries entry. Target: prove one in-scope research-solved finite-witness statement with kernel-checked computation.

## What counts as a win

Success means a Lean file that restates one FC theorem verbatim (diffed against the live main branch of https://github.com/google-deepmind/formal-conjectures re-fetched immediately before claiming) where that theorem is tagged research solved, lives outside FormalConjectures/ErdosProblems, WrittenOnTheWallII and OEIS, ends in `sorry`, has no `formal_proof` attribute, and is not the subject of any open FC pull request that proves it or adds a formal_proof link for it (searched on GitHub immediately before claiming), and proves it. Lean's kernel is the referee: the submitted file must compile with `lake build` against the repository's pinned lean-toolchain and lake-manifest (Mathlib rev as pinned, no edits to the statement, no new `axiom`, no `sorry`/`admit`, no `native_decide`/`Lean.ofReduceBool`, no `implemented_by`/`extern` tricks, no `set_option debug.skipKernelTC`), and `#print axioms <thm>` must list only a subset of {propext, Classical.choice, Quot.sound}. Heavy computation must go through `decide`, `Decidable` instances or proof-by-reflection checked by the kernel; `native_decide` is forbidden.

## Partial wins

- **p1:** HadamardConjecture.variants.first_cases restricted to a proved range k <= K with K >= 8 (orders up to 32), stated as a separate Lean theorem with the same IsHadamard predicate, kernel-checked.
- **p2:** A kernel-checked proof of a reusable decision procedure (e.g. a reflected clique-freeness checker for graphs on Fin n, or a Hadamard-matrix verifier) that an in-scope FC statement reduces to, plus the instance check for a smaller case (e.g. the Paley graph on 17 vertices has no 4-clique and no 4-independent set).

## How a win is checked

Same as Lean rule: compile in a clean FC checkout at the pinned toolchain with the Mathlib cache, `#print axioms`, forbidden-token grep, statement diff against live file. Kernel `decide` runs must finish within the default or an explicitly raised `maxRecDepth`/`maxHeartbeats` (raising limits is allowed; `native_decide` is not).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/formal-conjectures>

## Sources

- <https://github.com/google-deepmind/formal-conjectures>
- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/RamseyNumbers.lean>
- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/Hadamard.lean>
- <https://github.com/google-deepmind/formal-conjectures/pulls>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- R(5,5) > 42: encode Exoo's 42-vertex graph as a bit-packed adjacency Nat, prove once that a reflected checker over all 5-subsets is sound, and let the kernel run it; split the 850,668 5-subsets by first vertex to keep each `decide` within heartbeat limits.
- Cross-domain import (cryptographic proof systems / zero-knowledge 'certificate + cheap verifier'): ship a compact certificate (e.g. the Hadamard matrix as a bit-packed Nat) and a tiny verifier whose soundness is proved once; the kernel only runs the verifier.
- Cross-domain import (database query optimisation): rewrite brute-force decide checks as joins over sorted lists with proved index lemmas (merge-join instead of nested loops) so kernel reduction stays under heartbeat limits.
- Hadamard small orders (partial win p1): Sylvester doubling for powers of 2 plus Paley I/II for q = 3 mod 4 / q = 1 mod 4; proving Paley in general gives many orders at once. The full first_cases statement (`668 ≤ hadamardConstant`) needs every order up to 664 and is a long project. FC's IsHadamard is stated via the determinant; the proved direction of `isHadamard_equiv_isHadamard'` and the proof of `isHadamard_H12` on main show how to get it from M^T M = n I. Open FC PR #4900 (order 668) touches this file; do not duplicate it.
- Triage the ~517 in-scope sorries by statement shape (`∃ x, ...` over a finite type, or an equality of a computable function at a numeral) to find more finite-witness items.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- FC definitions can differ from textbook ones; a proof about the wrong definition does not count.
- `native_decide` makes huge checks easy and is forbidden; also ban `Lean.ofReduceBool` and `implemented_by`.
- Items get claimed fast: Leinster, small Ramsey numbers and S(5,8,24) were taken by open PRs within two weeks. Check open FC PRs and the formal_proof attribute on live main before claiming.
- Upper-bound Ramsey statements (e.g. R(5,5) <= 46) are not finite-witness items; they need exhaustive search certificates far beyond kernel reach.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/fc-finite-witness-sorries.md
```

Already set up? Say `run V3R1T4S on fc-finite-witness-sorries`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fc-finite-witness-sorries`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
