# Formal Conjectures WrittenOnTheWallII (Graffiti) and OEIS collections: research-solved conjectures without any Lean proof

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

FC's WrittenOnTheWallII collection (Fajtlowicz's Graffiti graph-theory conjectures) has, at commit 5a2fb85 (2026-10-28), 14 research-solved theorems ending in `sorry` with no formal_proof attribute: GraphConjecture3, 4, 5, 6, 13, 16, 17, 18, 23, 24, 25, 33, 91 and 291. Four are claimed by open FC PRs as of 2026-10-28: 5 (#6956 adds a formal_proof link), 17 (#4161 adds a formal_proof), 91 (#7394, a Lean disproof) and 291 (#7248, links a Lean refutation). That leaves 10 unclaimed: 3, 4, 6, 13, 16, 18, 23, 24, 25 and 33. The OEIS collection has 8 more (OEIS/109074, 100478, 287616, 111291, 53175, 1818, 2454 and 38552 `starkHeegner_classNumberOne`, the last a deep theorem), none touched by an open FC PR on 2026-10-28; the other research-solved OEIS items link external proofs. These were settled in papers, often by short graph-theoretic or elementary arguments. Target: prove one unclaimed item in Lean.

## What counts as a win

Success means a verbatim restatement (diffed against the live FC main branch re-fetched immediately before claiming) of one WrittenOnTheWallII or OEIS theorem tagged research solved, ending in `sorry`, with no formal_proof attribute and not the subject of any open FC pull request that proves it or links a proof (searched on GitHub immediately before claiming), proved in full. Lean's kernel is the referee: the submitted file must compile with `lake build` against the repository's pinned lean-toolchain and lake-manifest (Mathlib rev as pinned, no edits to the statement, no new `axiom`, no `sorry`/`admit`, no `native_decide`/`Lean.ofReduceBool`, no `implemented_by`/`extern` tricks, no `set_option debug.skipKernelTC`), and `#print axioms <thm>` must list only a subset of {propext, Classical.choice, Quot.sound}.

## Partial wins

- **p1:** A proof of the conjecture for all graphs with at most n vertices (n >= 7) by a kernel-checked enumeration, stated as a separate theorem (bounded verification, not a win).
- **p2:** A Lean library lemma relating FC's Graffiti invariants (e.g. independence number, residue, average distance) to Mathlib's SimpleGraph API, proved and reused by at least one closed conjecture's proof skeleton.

## How a win is checked

Clean FC checkout; compile; `#print axioms`; forbidden-token grep; diff statement vs live file.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/WrittenOnTheWallII>

## Sources

- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/WrittenOnTheWallII>
- <https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/OEIS>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Read the solved-by reference in each docstring; pick ones whose published proof is a single inequality chain on degrees/independence number.
- Bounded enumeration first (nauty geng to n=9) to make sure the FC statement agrees with the literature on small graphs before investing in a proof.
- Cross-domain import (spectral methods from physics / vibration analysis): several Graffiti invariants are eigenvalue-based; use Rayleigh-quotient bounds as the proof backbone and formalise only the variational inequality needed.
- Cross-domain import (electrical network theory): resistance-distance and average-distance invariants obey Kirchhoff/Rayleigh monotonicity; port a monotonicity argument rather than a combinatorial one.
- For OEIS items, identify a closed form or recurrence and prove it by induction with `decide` base cases.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Graffiti conjectures are often stated for connected graphs only; FC may encode connectivity differently from the paper.
- Small-graph enumeration is a sanity check, not a proof of the universal statement.
- Some 'solved' Graffiti conjectures were solved by counterexample: then the FC statement should be the negation; check the docstring.
- Mathlib's SimpleGraph API changes often; pin to FC's lake-manifest.
- Open PRs claim items quickly (on 2026-10-28: #6956 for GraphConjecture5, #4161 for 17, #7394 for 91, #7248 for 291); search the FC PR list for the file name before starting and again before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/fc-graffiti-oeis-solved-sorries.md
```

Already set up? Say `run V3R1T4S on fc-graffiti-oeis-solved-sorries`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fc-graffiti-oeis-solved-sorries`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
