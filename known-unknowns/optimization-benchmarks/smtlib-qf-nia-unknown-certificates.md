# SMT-LIB nonlinear integer arithmetic (QF_NIA): a checked answer for an unknown-status benchmark no SMT-COMP solver ever decided

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours per benchmark (cvc5, z3, Yices, local search for NIA, bit-blasting with bounds); certificate checks seconds to hours · open as of 2026-10-30

## The problem

The SMT-COMP 2026 benchmark metadata (benchmarks-2026.json.gz, SMT-COMP/smt-comp.github.io) gives SMT-LIB status 'unknown' to 5,270 QF_NIA files. Of those run in the 2026 single-query track, 287 never received a sat or unsat answer in any SMT-COMP single-query log 2018-2026, in the 2024-2026 model-validation, parallel and unsat-core logs, or in the 2024 cloud log (no 2025 or 2026 cloud log is published) (checked 2026-10-30): 243 VeryMax ITS and 23 VeryMax CInteger termination-proof constraint problems (Borralleras, Larraz, Oliveras, Rodriguez-Carbonell, Rubio, 2017), 14 mcm multiple-constant-multiplication instances (Lopes, Aksoy, Manquinho, Monteiro), 5 MathProblems (Jia, Liu, Huang, Ma, Zhang 2022: MF_04 and MF_12 magic squares of fifth powers, SF_12 semi-magic of fifth powers, SQ_05 and SQ_10 semi-magic squares of fourth powers) and 2 Ultimate Automizer ps6.c files (Heizmann). SQ_10 is already satisfied by Nicolas Rouanet's 2018 10x10 semi-magic square of 4th powers on Christian Boyer's multimagie.com (checked against all 5,070 assertions), so it is excluded, leaving 286 eligible files. QF_NRA has 26 such files (hycomp, zankl matrix interpretations, Sturm MBO), QF_IDL 31 (synthetic job-shop, ASP graph colouring, knight tour, labyrinth, solitaire), QF_LIA 2 and QF_LRA 3. The files are in the SMT-LIB 2025 release (Zenodo 16740866).

## What counts as a win

For one of the 286 eligible QF_NIA files (the 287 above minus 20220315-MathProblems/SQ_10.smt2; path under non-incremental/QF_NIA/ and SHA-256 of the unmodified file from QF_NIA.tar.zst of Zenodo record 16740866), still 'unknown' in the current SMT-COMP benchmark metadata, with no sat/unsat result in any SMT-COMP log at claim time, and with no model or proof already public (for the MathProblems files check Christian Boyer's multimagie.com tables): (a) sat, an integer assignment to every declared constant under which every assertion evaluates to true with exact big-integer arithmetic in a script independent of the solver; or (b) unsat, a proof with no trusted or hole steps accepted by an independent checker (a cvc5 CPC proof checked by Ethos, an Alethe proof that Carcara reports valid, not holey), or a self-contained mathematical certificate checked mechanically (for example a modulus m with an exhaustive check that the constraints have no solution mod m, or verified bounds plus a checked bit-blasted DRAT/LRAT proof). A file whose name matches a file decided under another family (all 14 mcm files share names with decided 20170427-VeryMax/SAT14 files) counts only if its SHA-256 differs from that file's.

## Partial wins

- **p1:** The same certificate standard for one of the 26 QF_NRA files never decided in SMT-COMP 2018-2026 (rational or real-algebraic model checked exactly, or a checked proof).
- **p2:** The same certificate standard for one of the 36 QF_IDL / QF_LIA / QF_LRA files (31 + 2 + 3) never decided in SMT-COMP 2018-2026 (Farkas/negative-cycle based proofs checked by Carcara count for unsat). A file whose name matches a file decided under another family (six 20220214-jobshop-BohanLi files match decided job_shop files) counts only if its SHA-256 differs from that file's.
- **p3:** The same certificate standard for one of the 23 QF_UFNIA files (mostly Certora verification conditions) that are unknown-status and never decided in SMT-COMP 2018-2026, with the same same-name hash check.

## How a win is checked

Download benchmarks-2026.json.gz, all results-sq-2018..2026, results-mv/parallel/uc-2024..2026 and results-cloud-2024 files from SMT-COMP/smt-comp.github.io/data; recompute that the file is unknown and never decided (match on logic, family and name, and hash-check any same-name file decided under another family). Extract the file from the SMT-LIB 2025 archive and hash it. For sat, evaluate every assertion under the model with Python integers (or exact rationals for QF_NRA). For unsat, run Ethos or Carcara on the proof against the original file and confirm there are no trust or hole steps. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/benchmarks-2026.json.gz>

## Sources

- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/benchmarks-2026.json.gz>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/results-sq-2026.json.gz>
- <https://raw.githubusercontent.com/SMT-COMP/smt-comp.github.io/master/data/results-sq-2025.json.gz>
- <https://smt-comp.github.io/2026/results/>
- <https://zenodo.org/records/16740866>
- <https://github.com/MRVAPOR/math_puzzles_smtlib_generator>
- <http://www.multimagie.com/English/SquaresOfCubes.htm>
- <http://www.multimagie.com/English/SquaresOfCubes10_11.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- VeryMax ITS/CInteger files ask for template ranking functions; most should be sat. Try NIA local search, incremental linearisation and bounded bit-blasting (a model found under bounds is still a model).
- For the magic-square files, modular arithmetic (fifth powers mod 11, mod 25 and so on) gives cheap necessary conditions and possible unsat certificates.
- mcm instances are adder-graph problems: a constructive adder graph from the MCM literature can be translated into a model.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- MF_04, MF_12 and SF_12 are open number-theory questions: Christian Boyer's multimagie.com lists 4x4 and 12x12 magic squares of fifth powers as unknown, and the smallest known semi-magic square of fifth powers is 16x16. A sat model there would be a major result and needs extra scrutiny, and unsat may be very hard.
- SQ_10 already has a published model (Rouanet 2018) and is excluded; check SQ_05 (5x5 semi-magic of fourth powers) against multimagie.com before claiming.
- A bounded search that finds no model is not an unsat proof.
- cvc5 NIA proofs may contain trusted steps; they do not count.
- Status fields change between SMT-LIB releases: re-check the latest release and SMT-COMP results before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/smtlib-qf-nia-unknown-certificates.md
```

Already set up? Say `run V3R1T4S on smtlib-qf-nia-unknown-certificates`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `smtlib-qf-nia-unknown-certificates`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
