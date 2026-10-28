# MINLPLib: better feasible point for an open mixed-integer nonlinear instance

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

MINLPLib (Stefan Vigerske, ZIB/GAMS, with Ambros Gleixner and others; last updated 14 Sept 2026, new points added 2026-05 to 2026-09) is the standard library of 1,633 mixed-integer and continuous nonlinear programs. Each instance page lists the best known feasible point (maximum absolute constraint violation at most 1e-8) and dual bounds from global solvers. Re-checked 2026-10-28: the instance data CSV (1,633 rows) still shows 538 instances with relative gap above 1e-4 and 49 with no primal bound; the newest points are dated 2026-09-14 (nd_netgen-2000-2-5-a-a-ns_7, sporttournament48). The finance/marketing instances saa_2 and pricing050 are a separate bank target (minlplib-finance-open-instances) and are excluded here. Find a point that is feasible within the library's tolerance and has a strictly better objective than the listed primal bound.

## What counts as a win

A solution point for an instance listed on https://www.minlplib.org/instances.html, other than saa_2 and pricing050 (bank target minlplib-finance-open-instances), whose instance page shows no dual bound equal to the primal bound, such that an independent evaluation of the instance's .gms/.py/.nl model at that point (with integers exactly integral and bounds exactly satisfied) gives maximum absolute constraint violation <= 1e-8 and an objective strictly better (in the instance's objective sense) than the listed primal bound by more than 1e-6 relative, with the instance page re-fetched live immediately before claiming.

## Partial wins

- **minlplib-primal-any:** Strict primal improvement on any open instance with at least 50 variables, checked by the independent evaluator.
- **minlplib-primal-for-missing:** A feasible point (violation <= 1e-8) for an instance that currently lists no feasible point at all, checked the same way.
- **minlplib-reproduce-points:** An independent evaluator that reproduces the listed objective and violation of the posted .sol points for 20 randomly chosen instances; prerequisite and useful public check.

## How a win is checked

For the instance, download the model (gms/<name>.gms, py/<name>.py or nl/<name>.nl) and the posted best point (sol/<name>.pN.sol). Evaluate objective and constraint violations with Pyomo (py format) or the AMPL Solver Library via the .nl file, matching variables by name. First reproduce the posted best point's objective and violation; then evaluate the claimed point. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.minlplib.org/instances.html>

## Sources

- <https://www.minlplib.org/instances.html>
- <https://www.minlplib.org/instancedata.csv>
- <https://www.minlplib.org/bounddates.html>
- <https://www.minlplib.org/doc.html>
- <https://www.minlplib.org/like.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Filter for instances where all listed dual bounds are far from the primal bound and the problem is nonconvex with many continuous variables; run multistart local NLP (Ipopt, Knitro-free alternatives) from thousands of random or Latin-hypercube starts, then polish to 1e-9 violation.
- Use global solvers available for free (SCIP 9/10 with its MINLP features) with long time limits and primal heuristics emphasis on mid-size open instances; even without closing the gap they often find better incumbents than older runs.
- Chemical-process design import: many MINLPLib instances (syn*, rsyn*, water*, pooling) are flowsheet or pooling problems; known structure-specific heuristics (multi-commodity reformulations for pooling, successive linear programming) often beat generic solvers.
- Applied-physics import for the geometric instances (kall_*, pointpack*, cvxnonsep*): use the Packomania-style billiards / repulsion methods instead of MINLP solvers; but check first whether the primal value already matches a proven optimum from the packing literature.
- Rescaling trick: solve a better-scaled equivalent model, map the point back, and re-verify violation in the original formulation, since the 1e-8 tolerance is absolute.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The CSV 'gap' is not 'open': the library calls an instance solved only when 3 solvers agree, so an instance with large CSV gap may already have one solver's dual bound equal to the primal bound (e.g. like: GUROBI dual bound = primal bound), in which case no improvement exists. Read the instance page.
- Tolerance exploitation: a point with violation 1e-6 can look better than the best 1e-8 point; the library lists such points separately as 'Other points' and they do not count.
- Variable naming: .sol files are keyed by the GAMS names; evaluating them against a reordered format by index gives garbage. Always evaluate by name.
- Several instances are listed as min with a negative objective; 'better' means lower for min, higher for max; read objsense.
- Floating point: report the objective recomputed in double precision from the model, not the solver's reported value, and require the improvement to exceed 1e-6 relative to rule out round-off.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/minlplib-open-primal-bound.md
```

Already set up? Say `run V3R1T4S on minlplib-open-primal-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `minlplib-open-primal-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
