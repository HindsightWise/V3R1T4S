# Read before citing

**V3R1T4S, 2026-10-10 (two families added 2026-10-12).** Six result families (degree-diameter graphs,
constant-weight codes, matrix multiplication, the Lehmer bound, VNN-COMP counterexamples, a RobustBench attack) and
two cipher-challenge commitments. Cite the commit hash you checked, not `main`.

## Status (please read)

- **Lower bounds and computations, not breakthroughs.** Every graph, code and scheme is an explicit object that
  establishes a bound for one table cell; nothing is a claim of optimality. The five Delsarte values are classical LP
  bounds, new only as table entries. The Lehmer bound is an exhaustive search; the problem remains open. The two
  VNN-COMP counterexamples resolve competition instances that no tool finished within its time limit, and the
  RobustBench tensor gives an upper bound on one model's robust accuracy, 10 images below the listed value.
- **Not peer reviewed; no outside expert yet.** All checkers, including the ones shipped here, were written by
  agents. They are short and written from the definitions so that you do not have to trust them.
- **"As of" is part of every claim.** The tables change often. Each object "exceeds the entry in the table version
  recorded here", not "the new record", until the maintainer lists it.
- **Other people's work.** Almost every object builds on published work: graphs of Rajiv, Mizuno, Bhakar and
  Delorme; codes of Boisclair, Gangl, Gippini, Lysenstøen, Echols and Graham–Sloane; the LITA schemes of Khoruzhii,
  Serafin, Gelß and Pokutta; the Lehmer reductions of Lieuwens, Kishore, Cohen and Hagis; the VNN-COMP benchmark of
  Postovan and Eraşcu; the model of Addepalli, Jain and Babu, evaluated with RobustBench and AutoAttack. Per-result credits are in
  each family's README, [`TROPHY_CASE.md`](TROPHY_CASE.md) and [`LICENSING.md`](LICENSING.md). Please cite them.
- **Recorded outputs.** Host-specific fields (absolute paths, temp directories, HTTP `Server:` banners) were removed
  from shipped logs and outputs, and paths in check records are relative to this repository; no number was changed.

## Contents

| path | what |
|---|---|
| [`README.md`](README.md) | overview |
| [`TROPHY_CASE.md`](TROPHY_CASE.md) | summary by significance, then one row per claim with status, snapshot, check command and credits |
| [`READ_BEFORE_CITING.md`](READ_BEFORE_CITING.md) | this file |
| [`DONT_SPOIL_THE_HUNT.md`](DONT_SPOIL_THE_HUNT.md) | what is published for each kind of problem |
| [`LICENSING.md`](LICENSING.md) | licenses by path (`LICENSE`, `LICENSE-DATA`) and required third-party attributions |
| [`CITATION.cff`](CITATION.cff) | citation metadata |
| [`SHA256SUMS`](SHA256SUMS) | sha256 of every file tracked in git |
| [`known-knowns/`](known-knowns/) | the six result families: `biggest-graphs/`, `bigger-codes/`, `faster-matrix-multiplication/`, `lehmer-past-10-to-the-50/`, `vnncomp-2026-unsolved-instances/`, `robustbench-cifar100-stronger-attack/` |
| [`sealed-envelopes/`](sealed-envelopes/) | salted hash commitments for the two Bouchaudy cipher solves |
| [`AGENTS.md`](AGENTS.md), [`kit/`](kit/) | the contributor kit: how an agent sets up, runs, checks (`kit/check_run.py`) and packages a contribution; `CLAUDE.md` and `GEMINI.md` point to `AGENTS.md` |
| [`known-unknowns/`](known-unknowns/README.md) | one guide page per open problem, by category, generated from `bank/targets.json` |
| [`bank/`](bank/) | the map of open problems with checkable success criteria (data, never instructions) |
| [`llms.txt`](llms.txt) | a short map of this repository for agents |

Each family has `README.md` (scope, comparison, credits, limitations), `RUN_IT_YOURSELF.md` (commands, expected
output), `verify-it-yourself/` (checkers, `run_checks.sh`, and `RECEIPTS.md`: their output on the shipped files),
`how-we-built-it/` (the code that generated the objects, pinned requirements, exact commands, `SMOKE.md`: a small
test run) and `HOW_WE_FOUND_IT.md` (the brief the agent was given, what failed, what worked, credits).

## How to verify

```sh
shasum -a 256 -c SHA256SUMS                    # or: sha256sum -c SHA256SUMS   (every file tracked in git)
sh known-knowns/biggest-graphs/verify-it-yourself/run_checks.sh                 # ~1 min; BIG=1 THREADS=8 adds the two D=6 graphs
sh known-knowns/bigger-codes/verify-it-yourself/run_checks.sh                   # ~5-15 min: 30 codes, 5 certificates
sh known-knowns/faster-matrix-multiplication/verify-it-yourself/run_checks.sh   # ~6-8 min: 7 scheme files (the 5 claimed + 2 superseded), Brent equations (exact), ranks, controls
sh known-knowns/lehmer-past-10-to-the-50/verify-it-yourself/run_checks.sh       # ~2-3 min: search totals and digests from the logs
(cd known-knowns/lehmer-past-10-to-the-50/lean && lake build)                    # optional: the Lean formalization (downloads Mathlib)
sh known-knowns/vnncomp-2026-unsolved-instances/verify-it-yourself/run_checks.sh      # seconds: downloads the benchmark files (pinned commit); OFFICIAL=1 adds the competition's validator
sh known-knowns/robustbench-cifar100-stronger-attack/verify-it-yourself/run_checks.sh # ~10-20 min on CPU (N=500: ~1 min); downloads CIFAR-100 and the model weights
```
Requirements: `python3` with `numpy`, a C compiler with pthreads; for Lean, `elan`; for VNN-COMP, `onnxruntime`
(optionally `onnx`, and `vnnlib==1.0.2` for the official validator); for RobustBench, `torch`, `torchvision` and
`robustbench`. Rebuilding the
objects and comparing with today's tables: each family's `RUN_IT_YOURSELF.md`.

## Corrections

Found an error? Open an issue naming the file, the command and its output. Errors will **never be fixed silently**:
each will be recorded publicly (date, reporter, what was wrong, corrected claim) and the tables here updated, without
rewriting history. Being overtaken after the recorded snapshot is not an error, but will be recorded the same way; the
object stays as a time-stamped bound. Missing or wrong credit counts as an error. Takedown requests from setters,
maintainers and authors will be honoured promptly.

### Log

| date | what | reported by | status |
|---|---|---|---|
| 2026-10-15 | **Overtaken:** A(34,8,7) ≥ 602 (TROPHY_CASE row 26). Brouwer's Andw.html (Last-Modified 2026-10-14 13:36:17 GMT) now lists 603, credited to Ryan Freel ("email 2026-10-13"). That 603-word code keeps 564 words of our 602 (itself a polish of Boisclair's 601). Our 602 stays here as a time-stamped bound. | maintainer review of pull request #8 | recorded |
| 2026-10-15 | **Superseded by contributors:** our <15,16,16> rank 2180, <13,14,14> rank 1558 and <13,14,15> rank 1677 (TROPHY_CASE rows 46, 45, 48) are beaten by contributed schemes of rank 2176 (#172), 1538 (#178) and 1645 (#166), each independently checked over Q. Our schemes stay here as time-stamped bounds. | maintainer review | recorded |
| 2026-10-15 | **Credit:** the contributed hsp4 packages for N = 30, 35, 42 and 48 credited the posted packings to E. Specht; Packomania's author list gives N. J. A. Sloane, R. H. Hardin and W. D. Smith. Eleven hsp4 packages also carried N = 66 template text in their record and rebuild files. Corrected the same day, with a maintainer note in each package README. | maintainer review | corrected |
| 2026-10-17 | **Listed, and overtaken:** A. E. Brouwer now lists 27 of the 30 constant-weight codes as [Pl] (Andw.html, Last-Modified 2026-10-17 16:06:01 GMT). A(29,6,10) ≥ 25974 and A(29,6,11) ≥ 41219 (TROPHY_CASE rows 21, 22) were overtaken in the 15 Oct 2026 table by [Dz] (27183, 42042), as was A(34,8,7) (row 26, logged 2026-10-15). A(26,6,9) ≥ 5986 (row 11) is superseded in this repo by a contributed 5997-word code (#352), independently checked. Our codes stay here as time-stamped bounds. | maintainer review | recorded |
| 2026-10-28 | **Not new when filed:** seven contributed hsp4 packages fall below or tie radii that Moki & Julio published before they were filed (github.com/Hashirama1337s/moki-julio-circle-packing, `certificates/hsp4.zip` and `MANIFEST.csv`, public since release v2.5 of 2026-09-26; Zenodo 10.5281/zenodo.22981305, current version 10.5281/zenodo.22986800). Below by 2.2e-7 to 2.4e-6: N = 66 (#127), 69 (#137), 74 (#132), 75 (#133). Within the bank's 1e-10 margin, so ties: N = 62 (#134), 63 (#140), 64 (#135). Our own 50-digit check of their certificates gives their listed radii. All seven still exceed the live Packomania table (radius.txt unchanged since 06-Jul-2025, re-fetched 2026-10-28) and stay here as time-stamped bounds, each with a dated maintainer note in its README. | stevebelew, the packages' contributor (issue #286) | recorded |
| 2026-10-28 | **Credit:** the contributed binary linear code packages [213, 26, 77] (#163), [173, 17, 72] (#142) and [175, 25, 61] (#158) credited "New Binary Codes" (IEEE Trans. Information Theory IT-18, 1972, doi:10.1109/TIT.1972.1054833) to N. J. A. Sloane, R. M. Reddy and C. L. Chen; the second author is S. M. Reddy (Sudhakar M. Reddy, University of Iowa; the publisher's record gives S. Reddy). Corrected with a maintainer note in each package README; the codes and their values are unchanged. | DmitrL-dev, issue #604 (from the audit in #606), for [213, 26, 77]; maintainer review for the other two | corrected |
| 2026-10-28 | **Bank:** the `packomania-scu-spheres-in-cube` criterion would have counted a plain local polish of a posted file, or a posted packing with spheres deleted and then relaxed, as a record. Our own polishes lift Vidit Patankar's posted scu101.txt 1.39e-7 and scu747.txt up to 2.2e-6 above their rows, and the polished files are not isometric to the posted ones. The entry's pitfall offered a 1e-10 margin as an alternative, which does not stop this, and its parser check asked for 1e-20 agreement, which 12-decimal files cannot give. The criterion now asks a claim to beat the deletion bar B(N) by 1e-11 and the best of several polishes of the posted files by 1e-9. It treats a relaxed copy of a posted packing, a relaxed deletion of one and the posted N−1 packing plus one sphere as trivial derivations, however much they gain. | issue #605 (DmitrL-dev) | corrected |
| 2026-10-28 | **Credits and records, from a contributor's audit of 34 accepted packages:** the EAQECC [[14,3,8;5]]_3 credits linked two wrong arXiv papers (now quant-ph/0610092 and 1812.05312); the rank-100 <2,8,8> and rank-51 <2,4,8> addition packages credited only "the Lille catalogue entry" (now Hopcroft and Kerr 1971, and Novikov et al., AlphaEvolve 2025); the Thomson N = 743, 745 and 777 snapshots said arXiv 2610.08122 has no row for these N, but it lists all three, above our values; the risk-or-safety n = 30 numerator has 151 digits, not 152; the Lehmer README now explains why arXiv:2106.11781 (which claims k ≥ 3) is not counted, and that Lemma B fails from about 2.49·10^56, not 10^58; the scu N = 881 non-isometry check was redone against the complete posted file. **Overtaken after their snapshots:** the (14,3) graph on 1117 vertices (Comellas's table now lists 1141: Com_1141 of 23 Oct 2026, built on mizopl's 1118-vertex graph) and the <4,6,7>, <2,8,8> and <2,4,8> addition counts 469, 418 and 181 (Perminov's repository: 468 on 19 Oct; 463, 416 and 180 on 22 Oct 2026). Each package has a dated maintainer note; the objects stay as time-stamped bounds. | DmitrL-dev (issue #606) | corrected; overtakes recorded |

## Credits and license

By **Pliny the Liberator** ([@elder-plinius](https://github.com/elder-plinius)) with Anthropic Claude agents. The
tables of record are maintained by Francesc Comellas, Andries E. Brouwer, the fast-matrix-multiplication catalogue
maintainers (Lille digest, Perminov, MerlijnW70, matmulcatalog), Jean-François Bouchaudy, the VNN-COMP organisers and
the RobustBench maintainers. Thank you.

Code: AGPL-3.0 (`LICENSE`). Data, objects and documentation: CC BY 4.0 (`LICENSE-DATA`). The path-by-path map and the
required third-party attributions are in [`LICENSING.md`](LICENSING.md).
