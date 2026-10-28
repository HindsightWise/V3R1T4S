# TPTP: prove (or refute) a problem with status Unknown/Open or rating 1.00, with an independently checked proof

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The TPTP problem library (Geoff Sutcliffe; tptp.org) is at v9.3.1, which the TPTP home page dates Fri 21 Aug 2026 (the distribution tarball was last modified 2026-09-08 and the BuggedProblems list 2026-10-21); it is still the current release on 2026-10-28. It annotates each problem with an SZS status (Theorem, Unsatisfiable, Satisfiable, CounterSatisfiable, Unknown, Open, ...) and a difficulty rating. Rating 1.00 means no system solved the problem in the rating runs. Status Unknown or Open means the library knows no proof or countermodel. These are machine-readable frontiers for automated reasoning. Can an independently verified proof, or a finite countermodel, be produced for such a problem?

## What counts as a win

For a TPTP problem whose header in the live library (https://seetptp.tptp.org/?folder=TPTPWorld/TPTP/Problems/, re-fetched immediately before claiming) shows Status Unknown or Open, or Rating 1.00, and that is not listed in BuggedProblems for that version: either (a) a saved TSTP derivation of the conjecture, or of a contradiction for CNF/unsatisfiability problems, whose every inference step is independently checked (GDV-style step verification by a different prover, or reconstruction in Isabelle/Metis or Lean), or (b) for a Satisfiable or CounterSatisfiable claim, a saved finite model checked by an independent model evaluator against all axioms and the negated conjecture. For a Rating 1.00 problem the claim counts only if no system's solution for it appears in the TSTP solution library on SeeTPTP for the current version.

## Partial wins

- **p1:** A checked proof of a rating >= 0.95 Theorem problem with a non-trivial derivation produced on a laptop in < 4 h.
- **p2:** A finite countermodel (size <= 20) for a problem with status Unknown, checked by an independent evaluator.
- **p3:** A checked proof of an Open problem in a single domain (e.g. LAT, GRP, ALG) using a lemma-discovery loop, with all lemmas also checked.

## How a win is checked

Skeptic downloads the problem file, re-runs the proof checker (e.g. GDV or re-proving each inference step with E/Vampire in a short time limit, or Isabelle reconstruction), or evaluates the model; confirms status/rating in the live header. Under 1 hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://seetptp.tptp.org/?folder=TPTPWorld/TPTP/Problems/>

## Sources

- <https://seetptp.tptp.org/?folder=TPTPWorld/TPTP/Problems/>
- <https://tptp.tptp.org/>
- <https://tptp.org/TPTP/Distribution/TPTP-v9.3.1.tgz>
- <https://tptp.org/TPTP/Distribution/BuggedProblems-v9.3.1.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: long runs of Vampire/E/iProver portfolios with tuned strategies (CASC schedules) on the 10 cores, plus Mace4/Paradox for countermodels.
- Conventional: axiom selection (SInE/premise selection) for large-theory problems that fail by timeout.
- Cross-domain import (program synthesis / AlphaProof-style): LLM-proposed intermediate lemmas, each discharged by an ATP, assembled into a checked derivation.
- Cross-domain import (computer algebra): Knuth-Bendix completion / Groebner-style rewriting for equational ALG/GRP/LAT problems (Waldmeister-style ordered completion).
- Cross-domain import (SAT solving): finite model finding by SAT encoding with symmetry breaking for countermodels.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rating 1.00 is relative to the systems in the rating runs; newer provers may already solve it - check the latest CASC results and SystemOnTPTP solutions (TSTP library) first.
- Unsound proof steps (prover bugs, mis-parsed input, axioms dropped by selection) - only an independent check counts.
- Bugged problems (BuggedProblems list) and problems with inconsistent axioms make 'proofs' trivial.
- Do not submit to TPTP/SystemOnTPTP web services; run locally.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/tptp-unknown-rating-1-problems.md
```

Already set up? Say `run V3R1T4S on tptp-unknown-rating-1-problems`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tptp-unknown-rating-1-problems`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
