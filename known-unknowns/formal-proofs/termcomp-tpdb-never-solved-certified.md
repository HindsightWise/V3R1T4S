# Termination Competition: a CeTA-certified termination or nontermination proof for a TPDB rewriting benchmark never solved at termCOMP 2023-2026

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (matrix/arctic interpretations by SAT search, dependency pairs, loop and nonloop search); CeTA checks seconds to minutes · open as of 2026-10-30

## The problem

The Termination Competition (termCOMP 2026, results at termcomp.github.io/Y2026) runs AProVE, matchbox, MnM, MU-TERM, Mint, NaTT, NaTT++ and NTI on the Termination Problem Database (TPDB 11.6); AProVE and matchbox also ran certified (CeTA) configurations. In the 2026 SRS Standard category, 61 of 1,921 string rewriting systems got no YES or NO from the virtual best solver, and in TRS Standard 86 of 1,528; none of these 147 got a YES or NO in the 2023, 2024 or 2025 tables either (the 29 CirponsMitchellSmith_25 files first appear in 2025). The SRS set includes the 29 CirponsMitchellSmith_25 files contributed by Reinis Cirpons, James D. Mitchell and Finn L. Smith (Adian rewriting systems of about 30 rules each, encoding one-relation monoid presentations such as <a,b | abaabaabaa = baaaba > ), 7 Waldmann_07_size12, 6 Waldmann_23, 3 Waldmann_19, 3 Gebhardt_06, Trafo_06/un16, Zantema_04/z079 and the one-rule system Wenzel_16 ababbbabbab -> abbabbbababbba (termination of one-rule string rewriting is a long-standing open area); the TRS set includes Transformed_CSR_04 (26), Applicative_05 (7), EEG_IJCAR_12 nonloop examples (7), Secret_05/06_TRS tpa*, Hydras (hydra_buchholz, lepper_0/1), Kaliszyk_19, Paulson_20/ackermann_iterative and Zantema_05/15. Excluded here: 11 Collatz-type encodings (Yolcu_21 collatz/mahler/farkas/michel/silva/barina, Zantema_04/syracuse, Yamada_21/collatz), whose termination is an open mathematical problem.

## What counts as a win

For one of the 136 eligible benchmarks (the 147 above minus the 11 Collatz-type files), taken from the TPDB version used by termCOMP 2026 and still unsolved (no YES/NO in the VBS column) in the latest termCOMP table for its category at claim time: a termination (YES) or nontermination (NO) proof in CPF format that the current CeTA release reports as CERTIFIED for that exact problem file. Uncertified tool output, or a proof for a modified system, does not win.

## Partial wins

- **p1:** An uncertified proof for one eligible benchmark that is independently checkable: for NO, an explicit looping (or nonloop pattern) witness verified by a short independent script; for YES, explicit interpretations or orderings whose constraints are verified by an independent script.
- **p2:** A CeTA-certified proof for one of the 51 SRS Relative or 14 TRS Relative benchmarks unsolved in termCOMP 2026.
- **p3:** A certified or independently checkable proof for one of the 65 TRS_Innermost benchmarks, or one of the 15 Integer_Transition_Systems benchmarks other than the 3 Collatz-type files (From_AProVE_2014/Collatz.jar-obl-8, From_AProVE_2014/Velroyen08-collatz.jar-obl-8, From_T2/collatz.t2_fixed), with no YES/NO in termCOMP 2026.

## How a win is checked

Fetch https://termcomp.github.io/Y2026/SRS_Standard.html or TRS_Standard.html and confirm the VBS cell for the benchmark is not YES/NO; check the 2023-2025 tables. Download the problem from TPDB (link in the table), run CeTA on the problem and the CPF proof; accept only CERTIFIED. For p1, re-run the witness check. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://termcomp.github.io/Y2026/SRS_Standard.html>

## Sources

- <https://termcomp.github.io/>
- <https://termcomp.github.io/Y2026/SRS_Standard.html>
- <https://termcomp.github.io/Y2026/TRS_Standard.html>
- <https://termcomp.github.io/Y2025/SRS_Standard.html>
- <https://termcomp.github.io/tpdb.html?ver=11.6>
- <https://isafor-ceta.uibk.ac.at/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- SAT-based search for larger matrix or arctic interpretations (dimension 5-8, wider coefficients) on the one-rule SRS, with long time limits; matchbox and MnM certify such proofs.
- For nontermination, search for nonloops (pattern rules) rather than loops; CeTA can certify some nonloop proofs.
- Hydras and Ackermann-type systems need ordinal or semantic labelling methods; check CeTA support before investing.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Collatz-type files encode open problems (Collatz, Mahler 3/2) and are excluded.
- TPDB file names and versions change; use the file linked from the 2026 table.
- A proof CeTA rejects because it uses an unsupported technique is not a win, even if correct; p1 covers independently checked uncertified proofs.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/termcomp-tpdb-never-solved-certified.md
```

Already set up? Say `run V3R1T4S on termcomp-tpdb-never-solved-certified`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `termcomp-tpdb-never-solved-certified`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
