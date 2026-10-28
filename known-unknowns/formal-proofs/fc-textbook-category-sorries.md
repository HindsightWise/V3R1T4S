# Formal Conjectures `textbook` sorries: formalise a known textbook-level result

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

FC tags textbook-level known facts with `@[category textbook]`; at commit 5a2fb85 (2026-10-28) a scan finds about 105 such theorems ending in `sorry`, about 80 of them without a `formal_proof` attribute. Examples still open on main with no formal_proof and no open PR proving them: ErdosProblems/44 `greedy_sidon_construction`, ErdosProblems/707 `erdos_707.variants.small_sidon_sets`, Wikipedia/BusyBeaver `BB_2` and `BB_3`, Wikipedia/RegularPrimes `not_isRegularPrime_37` (37 divides the numerator of B_32), OEIS/87719 `a_exists`. Items from the earlier list that are gone: Wikipedia/WolstenholmePrime `wolstenholme_theorem` now has a formal_proof link, ErdosProblems/685's trivial lower bound is proved, and Arxiv/2607.05739 `x_eq_tan_sum_arctan` is being worked on in open PR #7055. Target: prove one.

## What counts as a win

Success means a verbatim restatement (diffed against the live FC main branch re-fetched immediately before claiming) of one theorem tagged `textbook` that ends in `sorry`, has no formal_proof attribute and is not the subject of an open FC pull request proving it or linking a proof (searched on GitHub immediately before claiming), proved in full. Lean's kernel is the referee: the submitted file must compile with `lake build` against the repository's pinned lean-toolchain and lake-manifest (Mathlib rev as pinned, no edits to the statement, no new `axiom`, no `sorry`/`admit`, no `native_decide`/`Lean.ofReduceBool`, no `implemented_by`/`extern` tricks, no `set_option debug.skipKernelTC`), and `#print axioms <thm>` must list only a subset of {propext, Classical.choice, Quot.sound}. The theorem must not already exist in Mathlib under another name in a way that makes the FC sorry a one-line `exact` (if it does, that is reported as a NOTABLE cleanup, not a win).

## Partial wins

- **p1:** Wikipedia/BusyBeaver `BB_2` in the FC formulation (every 2-state 2-symbol machine either halts within the champion's step count or provably never halts), kernel-checked.
- **p2:** Two or more textbook sorries in one FC file closed, sharing one new helper lemma proved from Mathlib.

## How a win is checked

Clean FC checkout at pinned toolchain; compile; `#print axioms`; forbidden-token grep; statement diff; `exact?` probe to check the result is not already a direct Mathlib lemma.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/formal-conjectures>

## Sources

- <https://github.com/google-deepmind/formal-conjectures>
- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Rank the ~80 items by statement length and by Mathlib API proximity (Finset sums, ZMod, Nat.choose) and attack the shortest first.
- BB(2)/BB(3): encode the champion machines and the finite list of all 2-state/3-state machines up to symmetry; prove non-halting of the rest via translated-cycler / bounded-loop certificates checked by a verified decider (mirror the Coq bbchallenge deciders).
- Irregular prime 37: compute B_32 via Mathlib's `bernoulli` with a reflected rational evaluator, or use Kummer's criterion if FC defines regularity via class numbers (check the definition first).
- Cross-domain import (program synthesis / superoptimisation): run a bounded search over tactic scripts (stochastic superoptimiser style: random mutations of a tactic sequence scored by remaining goals) instead of only LLM sampling.
- Cross-domain import (structural engineering 'load path' analysis): draw the dependency DAG of the informal proof, identify the single lemma carrying most of the load, and prove it in isolation first; the rest is glue.
- Search Loogle/Mathlib for near-identical statements; many textbook items are a bridge between FC's custom definitions and existing Mathlib notions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A 'proof' that changes FC's custom definition or adds an instance assumption is not a proof of the FC statement.
- Textbook facts sometimes landed in Mathlib after FC was written; a one-line `exact Mathlib.lemma` is real but not a research win.
- Analytic items (real-number inequalities) tempt `nlinarith`/`polyrith` with external oracles; only the kernel-checked certificate counts.
- Statement-level typos in FC (off-by-one bounds) can make a textbook item false; prove the negation only as a misformalisation note, not a 'win'.
- BB(3) involves 3-state 2-symbol machines with a specific FC encoding of halting; mis-encoding the champion's step count is a common silent error.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/fc-textbook-category-sorries.md
```

Already set up? Say `run V3R1T4S on fc-textbook-category-sorries`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fc-textbook-category-sorries`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
