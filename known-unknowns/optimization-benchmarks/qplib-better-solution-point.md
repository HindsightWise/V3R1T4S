# QPLIB: better solution point for a quadratic (including QAP-type and Max-Cut-type binary) instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

QPLIB (Furini, Traversi, Belotti, Frangioni, Gleixner, Gould, Liberti, Lodi, Misener, Mittelmann, Sahinidis, Vigerske, Wiegele; hosted at ZIB) collects 453 quadratic programming instances, many with binary variables (quadratic assignment, Max-Cut, QUBO, quadratic knapsack). Each page lists the best known solution point. The library is actively updated: new better points were added on 12 Oct 2026 (QPLIB_2880, a 25x25 quadratic assignment instance, by Yuan Wang, Shenzhen Research Institute of Big Data; its value 1167256 equals the proven optimum of QAPLIB tai25a, so it is closed), 5 Oct 2026 (QPLIB_2096, contributed by ZiYor with an exact optimality certificate, so it is closed), 14 Sept 2026 (QPLIB_2174, QPLIB_5442 by Xiang He and Shaowei Cai's Qseek), 7 Aug 2026 (QPLIB_2036, Quplane, Todd J. Hendricks) and 28 July 2026 (QPLIB_2166, 2205, 10031-10033, Qseek); no newer History entry as of 2026-10-28. QPLIB pages do not mark which points are proven optimal. Find a feasible point with strictly better objective than the listed one (impossible where the listed value is already optimal, as for QPLIB_2096 and QPLIB_2880).

## What counts as a win

A solution point for an instance listed on https://qplib.zib.de/instances.html, evaluated independently from that instance's .lp or .gms file (variables matched by name; binaries and integers exactly integral; variable bounds exactly satisfied; maximum absolute violation of linear and quadratic constraints <= 1e-9), whose objective is strictly better in the instance's sense than the 'Solution point objective value' on its QPLIB_<id>.html page by at least 1e-6 relative, with the instance page and the History section of https://qplib.zib.de/ re-fetched live immediately before claiming.

## Partial wins

- **qplib-binary-improve:** Strict improvement on any pure-binary instance (probtype whose second letter is B, e.g. QBL, QBN, LBQ) with at least 100 variables, checked by the evaluator.
- **qplib-qap-improve:** Strict improvement on any quadratic-assignment-structured instance (n^2 binaries with 2n assignment equalities) whose underlying QAPLIB instance is not marked (OPT) on the QAPLIB page, checked by the evaluator; QPLIB_2880 (tai25a, proven optimal) does not qualify.
- **qplib-optimality-certificate:** A machine-checkable optimality certificate for an instance whose current point has no proof: an exact-arithmetic certificate (e.g. VIPR from exact SCIP) checked by an independent checker, or a model file plus open-source solver log and seed that a skeptic re-runs to the same bound in a fresh session.

## How a win is checked

Download qplib.zib.de/lp/QPLIB_<id>.lp (LP-format with the quadratic objective in [ ... ]/2) and sol/QPLIB_<id>.sol. Parse the objective and constraints by variable name and evaluate. Verified 2026-10-13: parsing the .lp of QPLIB_2880 and the posted .sol by name reproduces 1167256 exactly (evaluating the .qplib file by index does not, see pitfalls). Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://qplib.zib.de/instances.html>

## Sources

- <https://qplib.zib.de/instances.html>
- <https://qplib.zib.de/>
- <https://qplib.zib.de/doc.html>
- <https://qplib.zib.de/QPLIB_2880.html>
- <https://qplib.zib.de/lp/QPLIB_2880.lp>
- <https://qplib.zib.de/sol/QPLIB_2880.sol>
- <https://qplib.zib.de/qplib/QPLIB_2880.qplib>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Recent records came from strong binary local search (Qseek; permutation-based SA for QAP); for QAP-structured instances use robust tabu search (Taillard) and Misevicius' iterated tabu / hybrid genetic algorithms, the methods behind most QAPLIB records.
- Physics import: QUBO/Max-Cut instances are Ising spin glasses; use parallel tempering, population annealing or simulated bifurcation (the quantum-inspired dynamics behind Toshiba's SQBM+) on the binary instances.
- Reformulate small-to-mid binary instances exactly as MaxSAT or pseudo-Boolean problems and run modern anytime solvers (e.g. NuWLS-style local search plus core-guided search).
- For mixed-continuous nonconvex instances, alternate between fixing the binaries and solving the continuous QP to global optimality with an open-source spatial branch-and-bound.
- Mine the History section: instances improved in 2025-2026 show where incumbent quality is weak; neighbours in the same family (same donor, same structure) are likely to have slack too.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Variable order: .sol files use GAMS names (b1..bn); the .qplib file indexes variables in a different order, so evaluating a .sol against .qplib by index gives a wrong objective (on QPLIB_2880 it gives 2892328 instead of 1167256). Evaluate by name from .lp or .gms.
- Quadratic objective scaling: the LP format writes the quadratic part as [ ... ]/2; forgetting the /2 doubles the objective.
- Objective sense: some instances maximise; check 'Objective Sense' on the page.
- QAP-structured instances are QAPLIB instances in disguise: QPLIB_2880 is tai25a (same value 1167256), which the QAPLIB page at https://coral.ise.lehigh.edu/data-sets/qaplib/qaplib-problem-instances-and-solutions/ marks (OPT), so it cannot be improved. Check the underlying QAPLIB entry (OPT or bound) before attacking any QAP-type instance.
- QPLIB pages show no dual bounds or optimality marks; many listed points are already optimal. A tolerance-exploiting point (violation above 1e-9) is not a win even if its objective is better.
- Re-fetch the History section before claiming: points were updated on 2026-10-12 and 2026-10-05; QPLIB_2096 now carries an exact optimality certificate and cannot be improved.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/qplib-better-solution-point.md
```

Already set up? Say `run V3R1T4S on qplib-better-solution-point`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `qplib-better-solution-point`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
