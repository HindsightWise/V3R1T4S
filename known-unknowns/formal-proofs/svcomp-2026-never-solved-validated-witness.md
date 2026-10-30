# SV-COMP 2026: a doubly validated witness for a verification task that no participating verifier answered correctly

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours per task (validators run 15 min to a few hours each; ldv and coreutils tasks are large preprocessed C files) · open as of 2026-10-30

## The problem

SV-COMP, the International Competition on Software Verification (organiser Dirk Beyer, LMU Munich; sv-benchmarks contributors; verifier and validator teams), runs every participating verifier on the sv-benchmarks tasks and confirms answers by witness validation. Its 2026 edition (15th, TACAS 2026) published 52 C and Java results-verified category tables (BenchExec 3.34; 24 to 37 verifiers per C category, 11 for Java). Parsing every row on 2026-10-30 gives 1,748 task/property pairs where no verifier's result is correct or correct-unconfirmed. Two subsets are left out because other bank entries cover the same problems: c/neural-networks (441, VNN-COMP-style networks) and c/hardware-verification-bv (288, btor2c translations of HWMCC circuits). Of the other 1,019, 173 were never scored in 2026: every verifier's result there is 'invalid task' (category missing), and in 130 of them at least one verifier gave the labelled answer, so they are left out too. This removes almost all no-data-race pairs (pthread-race-challenges) and the unsolved array-fpi, argv-tasks and coreutils-v9.5-units rows. Re-reading the .yml of the remaining 846 scored pairs at sv-benchmarks main 813a819f (2026-10-29): 6 lost the property and 1 flipped its expected verdict, leaving 839 pairs, 771 in C and 68 in Java. C: unreach-call 441 expected true (95 in combinations, 80 in intel-tdx-module) and 11 false; valid-memsafety 113/105 (false mostly coreutils-v8.31, ldv-linux and memsafety-cve); no-overflow 46/23; termination 16/14; no-data-race 2 true (libvsync). Small classics include nla-digbench dijkstra-u, egcd3-ll and hard-ll, the knuth and prodbin-ll unwindbound variants, insertion_sort-2-2, recursive gcd02 and 17 recursified_nla-digbench tasks. Java: valid-assert 7/37, no-runtime-exception 23/1. The labels are known: the open part is an answer validators or a replay accept. SV-COMP 2026 validated correctness witnesses only for unreach-call, no-overflow and (demo) termination, so expected-true memsafety, data-race and Java pairs carry no win here.

## What counts as a win

Pick a task/property pair from the 2026 results-verified tables (https://sv-comp.sosy-lab.org/2026/results/results-verified/) where at least one verifier's result was scored (the row is not 'invalid task' / category missing for every verifier) and no verifier's result is in category correct or correct-unconfirmed, not under c/neural-networks/ or c/hardware-verification-bv/, whose .yml on current sv-benchmarks main (re-fetched before claiming) still carries that property with the same expected_verdict (for valid-memsafety, the same subproperty). (a) C, expected false: a violation witness (format 2.0, or 1.0 where only v1 validators handle the property, as for no-data-race) that two distinct validators from the 2026 witness-validation tables (https://sv-comp.sosy-lab.org/2026/results/results-validated/, v2 or v1) confirm in their 2026 configuration. A deterministic execution replay (CPA-witness2test, ConcurrentWitness2Test, or a Test-Comp test vector that reaches the violation when compiled with the sv-benchmarks harness) may stand in for one of the two. (b) C, expected true, property unreach-call, no-overflow or termination only: a format-2.0 correctness witness that two distinct validators from the 2026 correctness-witness v2 table confirm. Each validator run: at most 4 h CPU, 15 GB. (c) Java, expected false: a list of Verifier.nondet* return values that, returned in order by a replay version of org.sosy_lab.sv_benchmarks.Verifier with every other class unmodified, makes the program fail an assertion under java -ea or throw the uncaught runtime exception. A result contradicting the label is a label bug, not a win.

## Partial wins

- **p1:** A format-2.0 correctness witness for an in-scope expected-true C pair (unreach-call, no-overflow or termination) that exactly one SV-COMP 2026 correctness validator confirms within 4 h CPU and 15 GB, and that no other 2026 correctness validator rejects (the others time out or answer unknown).
- **p2:** A violation witness for an in-scope expected-false C pair that exactly one SV-COMP 2026 violation validator confirms, or that only a deterministic execution replay (criterion a) confirms, and that no 2026 violation validator rejects.
- **p3:** For one of the in-scope expected-true tasks nla-digbench dijkstra-u, egcd3-ll or hard-ll, or nla-digbench-scaling knuth_unwindbound5/10/50 or prodbin-ll_unwindbound50/100: a published SMT-LIB script that encodes the program's loops with the task's C integer semantics (QF_BV, or integer arithmetic with explicit range constraints for the ILP32/LP64 data model) and states loop invariants, on which z3 and cvc5 both return unsat for every initiation, consecution and assertion-implication query within 1 h each, even if no validator accepts a witness built from those invariants.

## How a win is checked

The skeptic downloads the task at the current sv-benchmarks commit and checks the property, expected verdict and (for memsafety) subproperty in the .yml. They confirm on the 2026 results-verified table that the row was scored (not 'invalid task' for every verifier) and has no correct or correct-unconfirmed entry, then run the named validators (archived 2026 versions from fm-tools / Zenodo, with the competition's BenchExec benchmark definitions and the task's data model) or the replay harness on the submitted witness or test vector. For Java they compile the task with the replay Verifier class and run it with java -ea. For p3 they read the SMT encoding against the C source and run it in z3 and cvc5. 1 to 8 hours per claim.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://sv-comp.sosy-lab.org/2026/results/results-verified/>

## Sources

- <https://sv-comp.sosy-lab.org/2026/results/results-verified/>
- <https://sv-comp.sosy-lab.org/2026/results/results-validated/>
- <https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks>
- <https://doi.org/10.1007/978-3-032-22749-2_23>
- <https://sv-comp.sosy-lab.org/2026/rules.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Small nonlinear-arithmetic loops (nla-digbench): invariant synthesis with polynomial templates or Gröbner-basis equalities, emitted as witness 2.0 invariants.
- intel-tdx-module and combinations expected-true unreach-call tasks: compositional invariants per component, exported as witness 2.0 and cross-validated.
- coreutils and memsafety-cve false tasks: run a sanitiser-guided fuzzer on the harness to find the bad input, then turn the trace into a violation witness.
- Java expected-false tasks: concolic testing (JDart/GDart style) with the Verifier stub to get concrete nondet sequences.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The unsolved list was computed from the 2026 tables; SV-COMP 2027 (spring 2027) may solve tasks, so re-check its tables when they appear.
- Rows where every verifier's result reads 'invalid task' (category missing) were never scored in 2026 and are out of scope: 173 of the 1,019 candidates, and in 130 of them some verifier already gave the labelled answer. Filter on the category, not only on the absence of 'correct'.
- Between the svcomp26 tag and main 813a819f, 6 of the 846 scored pairs lost the property and 1 flipped verdict (over all 1,019 candidates: 1 task file removed, 28 lost, 6 flipped), usually because a label was wrong. Always re-check the current .yml, and note that task files use two YAML layouts (property_file first or expected_verdict first) and both lower-case and capitalised verdicts when scripting the check.
- Validators accept witnesses under specific data-model and property options (ILP32 vs LP64, subproperty for memsafety); a mismatch gives a spurious reject.
- No SV-COMP 2026 correctness-witness validation track covered valid-memsafety or no-data-race, so expected-true pairs for those properties cannot meet criterion (b).
- The sv-benchmarks Java Verifier stub draws values from java.util.Random, so criterion (c) needs a replay stub; Java assertions only fire with -ea.
- The c/neural-networks and c/hardware-verification-bv subsets are excluded on purpose (overlap with VNN-COMP and HWMCC entries).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/svcomp-2026-never-solved-validated-witness.md
```

Already set up? Say `run V3R1T4S on svcomp-2026-never-solved-validated-witness`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `svcomp-2026-never-solved-validated-witness`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
