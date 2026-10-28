# MOONSHOT - Equational Theories Project: settle the last 2 finite-magma implications (Eq677 ⇒ Eq255, Eq2910 ⇒ Eq47)

✅ **Formal proofs** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The Equational Theories Project dashboard (re-fetched 2026-10-28) shows the general implication graph 100% complete and the finite graph 99.99999% complete with exactly 2 implications having no proof and no conjecture. Its raw_data/finite_outcomes.json.gz marks exactly two finite implications 'unknown': Equation677 => Equation255 and Equation2910 => Equation47. Partial progress on 677 => 255 sits in open ETP issues, not yet merged: #1464 (July 2026) gives a Lean orbit lemma and 45 DRAT-certified order-10 UNSAT cases, claiming every finite counterexample has at least 11 elements; #1517 (Oct 2026) gives a Lean-checked conditional proof assuming the left translations are closed under conjugation. Settle either implication: a Lean proof that every finite magma satisfying the first law satisfies the second, or a finite magma satisfying the first and violating the second (a finite counterexample, Lean-checkable by `decide`).

## What counts as a win

Success means, for one of the implications listed with 'no proof' on https://teorth.github.io/equational_theories/dashboard/ (finite graph, re-fetched live immediately before claiming, and still 'unknown' in raw_data/finite_outcomes.json.gz): EITHER an explicit finite magma (operation table) that satisfies the hypothesis law and violates the conclusion, verified by an independent exhaustive Python check AND a Lean `decide` proof compiled in the ETP repository at its pinned toolchain; OR a Lean proof of the finite implication, sorry-free, no new axioms, `#print axioms` only propext/Classical.choice/Quot.sound.

## Partial wins

- **p1:** Exhaustive exclusion of counterexamples up to a new size bound beyond any bound documented in the ETP paper, blueprint or issues for that implication (for 677 => 255 this means excluding order 11 or more, since issue #1464 claims order 10), with a reproducible SAT/DRAT certificate per size and the symmetry-breaking argument written out.
- **p2:** A Lean proof of the implication under an additional natural hypothesis (e.g. the magma is a quasigroup, or left-cancellative) that is neither implied by nor equivalent to a hypothesis already proved in the ETP issues (e.g. the translation-conjugacy closure of issue #1517), stated as a separate theorem.

## How a win is checked

Counterexample: load the table, check the hypothesis law on all n^k assignments and find a violating assignment for the conclusion (Python, seconds); compile the `decide` proof in ETP. Proof: build in ETP checkout, `#print axioms`.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/equational_theories/dashboard/>

## Sources

- <https://teorth.github.io/equational_theories/dashboard/>
- <https://teorth.github.io/equational_theories/raw_data/finite_outcomes.json.gz>
- <https://github.com/teorth/equational_theories>
- <https://teorth.github.io/equational_theories/paper.pdf>
- <https://github.com/teorth/equational_theories/issues/1464>
- <https://github.com/teorth/equational_theories/issues/1517>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Read the ETP paper's section on 677/255 first: infinite counterexamples exist (that is why the general implication is false), so the finite question is about whether finiteness forces the conclusion; known structure results (677 magmas are quasigroup-like) narrow the search.
- SAT/SMT search for finite counterexamples with symmetry breaking (Mace4/Kissat with lex-leader constraints), pushing sizes beyond the published bound.
- Cross-domain import (coding theory): treat the operation table as a code over an alphabet of size n and use the law as parity-check constraints; algebraic constructions (linear magmas x◇y = ax+by over finite rings, then twisted versions) mirror code construction over GF(q).
- Cross-domain import (dynamical systems): finiteness arguments often come from iterating a self-map (here the left/right translations) and using pigeonhole/permutation cycle structure; model translations as permutations and look for an invariant like a conserved quantity.
- Translate the known infinite counterexample into a profinite/inverse-limit family and test whether any finite quotient survives.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The general (infinite) implication is already refuted; an infinite counterexample does not count.
- Equation numbering is ETP-specific; verify the laws by reading equations.txt, not from memory.
- Lean `decide` over large tables can be slow; native_decide is forbidden.
- The project may close these at any time; re-fetch the dashboard before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/etp-finite-magma-677-255.md
```

Already set up? Say `run V3R1T4S on etp-finite-magma-677-255`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `etp-finite-magma-677-255`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
