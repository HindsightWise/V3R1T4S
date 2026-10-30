# CHC-COMP 2026: first validated model or refutation for a Horn-clause task no solver answered and whose verdict is only a placeholder

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days per task (portfolio of Eldarica, Golem, Spacer, MuCyc and custom invariant search); validating a model or refutation takes seconds to minutes · open as of 2026-10-30

## The problem

CHC-COMP 2026 was organised by Konstantin Britikov (Lugano) and Levente Bajczi (BME). Results are at chc-comp.github.io/chc-comp-2026/tables, and the benchmarks are in chc-comp/chc-comp26-benchmarks. It ran 10,193 check-sat tasks in nine tracks with a 1800 s limit, using Eldarica, Golem, LoAT, MuCyc, PCSat, Z3/Spacer (hors concours), ThetaCHC, z4 and chococatalia. Parsing the per-track BenchExec solver tables gives 892 task files with no 'true'/'false' answer from any solver. In 617 of them the expected_verdict in the task's YAML is marked 'placeholder verdict (auto-added)', so the status is genuinely unknown. The other 275 carry a non-placeholder expected_verdict from earlier solver runs (114 with a majority_vote_verdict field, 139 with a majority-vote comment naming its supporters, 22 with a bare verdict). Placeholder tasks by track (2026-10-30): ADT-LIA 395 (mostly ringen-adt-benchmarks tip2015/isaplanner/prod and ADTRem), BV-Lin 76, LIA-Lin-Arrays 46 (quic3, llreve-bench/unsolved program-equivalence tasks), LRA-Lin 24 (vmt cav12 token_ring and transmitter, sally hacms eventclock), LIA-Arrays 23, LIA-Lin 18 (aeval-unsafe s_split, Lustre DRAGON and PRODUCER_CONSUMER, llreve digits10), BV 17 (eldarica-misc Consistency fortune/incremental and five reve *-horn-bv), LIA 16 (kind2 microwave and DRAGON, hcai svcomp) and ADT-LIA-Arrays 2. One of the BV tasks, eldarica-misc/BV/Consistency/incremental2.41-bv, was answered 'true' by Eldarica in the 2026 model track (results-BV-model table). That leaves 616 placeholder tasks with no answer in either track. The benchmarks were contributed by the Eldarica, Kind 2, Sally, VMT, HCAI, AEval, RInGen, ADTRem, llreve, quic3, rust-horn, Solidity and Ultimate projects.

## What counts as a win

Success means one eligible task, its .smt2 file from chc-comp/chc-comp26-benchmarks identified by path and SHA-256. Eligible: no 'true' or 'false' answer in its row of https://chc-comp.github.io/chc-comp-2026/tables/results- < TRACK > -solver.table.html or of https://chc-comp.github.io/chc-comp-2026/tables/results- < TRACK > -model.table.html; its YAML expected_verdict is a placeholder or absent when re-fetched; and no answer in the CHC-COMP 2025 tables (linked from https://chc-comp.github.io/2025/results.html). For SAT, a model in the CHC-COMP 2026 model format (one define-fun per predicate, using only the file's theories, no quantifiers). It must be accepted by the 2026 model-validation pipeline (chc-comp/chc-comp-2026, *-validation templates), and an independent SMT solver must prove every clause's negation unsat. For UNSAT, an explicit refutation: finitely many ground clause instances with concrete values, each constraint true, deriving false, checked by an independent evaluator. A bare solver answer does not win.

## Partial wins

- **p1:** The same certificate standard for one of the 275 tasks that no 2026 solver answered but whose YAML carries a non-placeholder expected_verdict from earlier runs. The certificate must agree with that verdict, or, if it contradicts it, come with both independent checks.

## How a win is checked

Download the .smt2 file and hash it. For a model, substitute the definitions into every clause and check validity with two SMT solvers (e.g. cvc5 and Z3), plus the CHC-COMP 2026 validator. For a refutation, parse the derivation, check that each step is an instance of a clause of the file, evaluate every constraint under exact theory semantics (bit-width-exact for BV, exact rationals for LRA) and confirm that the root is the query. Re-fetch the 2026 table row and the YAML.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://chc-comp.github.io/chc-comp-2026/tables/index.html>

## Sources

- <https://chc-comp.github.io/>
- <https://chc-comp.github.io/chc-comp-2026/>
- <https://chc-comp.github.io/chc-comp-2026/tables/index.html>
- <https://chc-comp.github.io/chc-comp-2026/tables/results-ADT-LIA-solver.table.html>
- <https://chc-comp.github.io/chc-comp-2026/tables/results-LIA-Lin-solver.table.html>
- <https://chc-comp.github.io/chc-comp-2026/tables/results-LRA-Lin-solver.table.html>
- <https://chc-comp.github.io/chc-comp-2026/tables/results-BV-Lin-solver.table.html>
- <https://github.com/chc-comp/chc-comp26-benchmarks>
- <https://github.com/chc-comp/chc-comp-2026>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The LRA-Lin and LIA-Lin tasks are transition systems (token_ring, transmitter, DRAGON, PRODUCER_CONSUMER): try k-induction with invariant strengthening and IC3 over the theory with long runs. Golem, LoAT and MuCyc did not run every track.
- llreve-bench/unsolved tasks are program-equivalence (regression verification) problems: relational invariants coupling the two programs' loop counters often suffice.
- ADT tasks from TIP/IsaPlanner are inductive theorems: a model needs a size or catamorphism abstraction, so try RInGen-style regular models or Eldarica's size-based abstractions.
- For tasks whose file name says 'unsafe' or 'invalid', search for a counterexample by bounded unrolling (BMC) with a large bound first: refutations are cheap to check.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The expected_verdict field is often a placeholder 'true' added automatically. It is not a status: eventclock4.invalid has one.
- Some task names (safe/unsafe/true-unreach-call) come from the C source and need not match the CHC encoding (BV translations can change the verdict).
- The same YAML can appear in several tracks. Identify the exact .smt2 file and track.
- Check the model-track table as well as the solver table: eldarica-misc/BV/Consistency/incremental2.41-bv has no solver-track answer but has an Eldarica 'true' in results-BV-model.
- Six placeholder tasks (e.g. eldarica-misc/BV/dillig/34.c-bv, vmt-chc-benchmarks/bv/half.c) are on chc-comp-2026 ignore.txt, which the organisers use to score a task as neither correct nor wrong. Read why before investing.
- ADT models that need recursive functions or quantifiers are outside the validator format, so check what the 2026 validator accepts before investing.
- Check CHC-COMP 2025 and earlier results and recent papers before claiming. The 2025 per-track tables are hosted on www.cip.ifi.lmu.de, which did not respond on 2026-10-30. An unreachable table is not evidence of absence.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/chc-comp-2026-unknown-status-first-solve.md
```

Already set up? Say `run V3R1T4S on chc-comp-2026-unknown-status-first-solve`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chc-comp-2026-unknown-status-first-solve`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
