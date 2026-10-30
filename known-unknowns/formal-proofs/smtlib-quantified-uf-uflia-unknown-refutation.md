# SMT-LIB quantified UF and UFLIA: a checked refutation or model for an unknown-status benchmark never decided at SMT-COMP

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours per benchmark (cvc5/z3 quantifier instantiation, Vampire SMT-LIB mode); proof checking minutes · open as of 2026-10-30

## The problem

SMT-COMP 2026 metadata marks 3,395 UF and 2,379 UFLIA files as status 'unknown'. Of those run in the 2026 single-query track, 501 UF and 378 UFLIA files never received a sat or unsat answer in any SMT-COMP single-query log 2018-2026 nor in the 2025-2026 model-validation, parallel and unsat-core logs (checked 2026-10-30). The largest families are Isabelle Sledgehammer exports (sledgehammer/Fundamental_Theorem_Algebra, QEpres, TypeSafe, FFT, NS_Shared, Hoare, StrongNorm), Barrett/Reynolds/Blanchette cdt-cade2015 codatatype problems (UF part), and Boogie verification conditions (UFLIA). Further never-decided quantified files: UFNIA 383, UFDT 389, ALIA 257, AUFBVDTLIA 281. Contributors are named in each file's :source field; SMT-LIB is co-ordinated by Clark Barrett, Pascal Fontaine and Cesare Tinelli.

## What counts as a win

For one of the 501 UF or 378 UFLIA files (unmodified from the SMT-LIB 2025 release, Zenodo 16740866, path and SHA-256 recorded), still 'unknown' in the current SMT-COMP metadata and never decided in any SMT-COMP log at claim time: (a) unsat, an Alethe proof of the original file that `carcara check` reports as valid (not holey), run without --ignore-unknown-rules or --allowed-rules, or a cvc5 CPC proof accepted by Ethos with no trusted steps; or (b) sat, for a UF file only, a finite model (a finite universe for every uninterpreted sort and a table for every function and predicate) under which a script independent of the solver evaluates every assertion, quantifiers included, to true by exhaustive enumeration. For a UFLIA file, sat counts only if every uninterpreted function is given as a closed LIA term over its arguments (with finite tables for uninterpreted sorts) and an Alethe or CPC proof, checked as in (a), shows that the negation of the original assertions with these definitions substituted is unsatisfiable. Neither a bare solver answer nor a proof of a preprocessed or premise-selected variant counts. A file whose name matches a file decided under another family (3 UFLIA files on 2026-10-30) counts only if its SHA-256 differs from that file's.

## Partial wins

- **p1:** The same certificate standard for one never-decided unknown-status file in UFNIA, UFDT, UFDTLIA, ALIA or AUFLIA. A file whose name matches a file decided under another family (239 of the 383 UFNIA files, 32 UFDT and 16 UFDTLIA files on 2026-10-30) counts only if its SHA-256 differs from that file's.
- **p2:** An unsat proof of the original file reconstructed and checked in Isabelle/HOL or Lean from a solver's output, for one of the 879 UF/UFLIA files, where Carcara does not support a rule used.

## How a win is checked

Recompute eligibility from benchmarks-2026.json.gz and all results-*.json.gz files in SMT-COMP/smt-comp.github.io/data (match on logic, family and name, and hash-check any same-name file decided under another family). Hash the file. Run `carcara check <proof> <original.smt2 > ` and accept only a 'valid' result (not 'holey'; no --ignore-unknown-rules or --allowed-rules), or Ethos on a CPC proof with no trust steps. For a UF sat claim, run an independent evaluator on the finite model; for a UFLIA sat claim, check the substituted formula's proof the same way. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/benchmarks-2026.json.gz>

## Sources

- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/benchmarks-2026.json.gz>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/results-sq-2026.json.gz>
- <https://zenodo.org/records/16740866>
- <https://github.com/ufmg-smite/carcara>
- <https://smt-lib.org/benchmarks.shtml>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Sledgehammer exports carry hundreds of facts; relevance filtering finds a small unsat core whose refutation is then replayed on the full file (extra assertions do not break an unsat proof).
- Run Vampire and E on a TPTP translation for the proof search, then produce the checkable Alethe proof with cvc5 restricted to the found instances.
- Model finders (cvc5 finite-model-finding, Paradox-style) for the problems that look satisfiable.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Many Sledgehammer goals were proved in Isabelle by other means; that is not a certificate for the SMT file, and the file may differ from the original goal.
- Carcara does not yet support every cvc5 rule; check rule coverage before a long run.
- Some of these problems also exist in TPTP; a TPTP proof does not count unless replayed on the SMT-LIB file.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/smtlib-quantified-uf-uflia-unknown-refutation.md
```

Already set up? Say `run V3R1T4S on smtlib-quantified-uf-uflia-unknown-refutation`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `smtlib-quantified-uf-uflia-unknown-refutation`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
