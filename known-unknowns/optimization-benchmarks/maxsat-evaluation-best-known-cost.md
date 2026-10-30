# MaxSAT Evaluation benchmarks: beat the best known cost of an instance whose optimum is unknown

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours per instance (anytime MaxSAT solvers, SAT-based local search, LNS); instance archives are large (2-5 GB zips per 2026 track) · open as of 2026-10-30

## The problem

The MaxSAT Evaluations (20th edition MSE 2026 at SAT 2026; Zenodo record authors Dieter Vandesande, Christoph Jabs, Jeremias Berg, Johannes Fichte, George Katsirelos, Ruben Martins, Andre Schidler, Dominik Schreiber) keep a benchmark metadata database, meta.db in github.com/maxsat-evaluations/data (updated with the 2026 results in July 2026, repository pushed 2026-10-07), with fields optimal_cost and best_known_cost ('found during a MSE') per standardised WCNF instance, keyed by GBD hash. On 2026-10-30 it lists 798 non-disqualified instances with optimal_cost 'unknown' and a numeric best_known_cost, from families such as logistics-routing (43), decision-trees (89), interpretable-rule-based-classifiers (77), RBAC maintenance, inconsistency-measurement, optimizing-bdds, correlation-clustering, generalized-hypertree-width, Ramsey and Steiner-triple encodings. Five of them (families aes and aes-key-recovery, cipher key-recovery encodings) are outside this target, leaving 793. 247 of those were in the 2026 exact tracks, where no exact solver finished any of them in the time limit, and in the 2026 anytime tracks (300 s and 1707 s) no solver went below the stored best_known_cost. Lower it.

## What counts as a win

For one instance whose meta.db row (re-fetched from https://raw.githubusercontent.com/maxsat-evaluations/data/main/meta.db at claim time) has disqualified 'no', optimal_cost 'unknown', numeric best_known_cost B and a family other than aes or aes-key-recovery (cipher encodings are not eligible): a complete assignment to the standardised WCNF (std_wcnf output as the data README defines, GBD hash equal to the row's hash) that satisfies every hard clause and whose total weight of falsified soft clauses is strictly less than B, recomputed by an independent checker. The instance must not have a published optimum or lower cost elsewhere (MSE proceedings, solver papers). A cost on a preprocessed or re-encoded instance does not count.

## Partial wins

- **p1:** A proof of optimality of the current best_known_cost for one such instance (same family exclusion), as a VeriPB proof accepted by the VeriPB checker (or CakePB) for the PB translation of that exact WCNF.
- **p2:** A first feasible solution (all hard clauses satisfied, cost recomputed) for one of the 11 2026 exact-track instances whose row has best_known_cost and optimal_cost both 'unknown' and unsat not 'yes' (overcommitted-scheduling, bnn-verification, traveling-salesman, judgment-aggregation, minimum-weight-dominating-set).

## How a win is checked

Load meta.db (an SQL dump; sqlite3 meta.sqlite < meta.db) and query the row by hash. Obtain the instance from the MSE Zenodo archive (2026: record 21358014) or the year's benchmark archive, run std_wcnf, and confirm the GBD hash. A 30-line script parses the WCNF (new format: 'h' hard lines, weighted soft lines) and the v-line assignment, checks every hard clause and sums weights of falsified soft clauses. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/maxsat-evaluations/data/main/meta.db>

## Sources

- <https://maxsat-evaluations.github.io/2026/>
- <https://github.com/maxsat-evaluations/data>
- <https://raw.githubusercontent.com/maxsat-evaluations/data/main/meta.db>
- <https://raw.githubusercontent.com/maxsat-evaluations/data/main/metadata.md>
- <https://raw.githubusercontent.com/maxsat-evaluations/data/main/results/2026-anytime-weighted-1707s.csv>
- <https://doi.org/10.5281/zenodo.21358014>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run 2026 anytime entrants (NuWLS-c-2026, SGAT-NuWLS-c, SPB-NIM-c, Loandra, Aperture variants, BouMS) for hours instead of 1707 s, seeded with each other's best solutions.
- Instances from structured applications (logistics-routing, decision-trees, BDD optimisation) admit domain heuristics: decode the assignment, improve in the original domain, re-encode and check.
- LNS with an exact MaxSAT or CP-SAT solver on a freed neighbourhood around the best-known assignment.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Hashes refer to std_wcnf-standardised files; an older WCNF file of the same name can hash differently and have different variable numbering.
- optimal_cost 'unknown' can mean only that no MSE run proved it; check the family's proceedings description and later papers for a published optimum.
- Families that encode public library instances (miplib, capacitated-vehicle-routing, steiner-triple-systems, ramsey-numbers) may have an optimum or a better solution already known in the source library (MIPLIB, CVRPLIB, covering-design or Ramsey tables); such a cell is not eligible, and a better MaxSAT cost is a benchmark result, not a new record of the source problem.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/maxsat-evaluation-best-known-cost.md
```

Already set up? Say `run V3R1T4S on maxsat-evaluation-best-known-cost`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `maxsat-evaluation-best-known-cost`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
