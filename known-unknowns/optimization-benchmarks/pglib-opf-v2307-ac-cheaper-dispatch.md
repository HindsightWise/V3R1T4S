# PGLib-OPF v23.07: an AC-feasible dispatch cheaper than the published baseline on a large case with an open relaxation gap

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (1,803- to 78,484-bus cases; multistart Ipopt or global-solver heuristics) · open as of 2026-10-30

## The problem

The Power Grid Library for AC optimal power flow (PGLib-OPF, IEEE PES Task Force on Benchmarks; curated by Carleton Coffrin, LANL) is the standard AC-OPF benchmark: 66 networks in typical (TYP), congested (API) and small-angle-difference (SAD) conditions. Its BASELINE.md for the current release v23.07 (unchanged since 24 Jul 2023) lists, per case, the AC objective from PowerModels.jl v0.19.9 + Ipopt (a local optimum) and the SOC and QC relaxation gaps. Global optimality is unknown for most large cases. On v21.07, Gopinath and Hijazi (LANL, arXiv 2203.11328, 2022) closed the gap below 1% on 85% of the open cases (SOC gap above 1%) up to 3,000 buses with SDP-RLT and bound tightening. Wang, Magron and Lasserre (EPSR 2022) certified 1% optimality on 58 of 115 hard cases (29 at first order, 29 more at order 1.5). Certified optimal-value intervals posted in Oct 2026 (pglib-opf issue #49) cover only cases up to 600 buses. In scope are the 82 cases with at least 1,000 buses and BASELINE SOC gap at least 1.00%, excluding the five networks MINLPLib also carries (case1354_pegase, case6468_rte, case6515_rte, case9241_pegase, case13659_pegase: bank target minlplib-open-primal-bound). Examples: case8387_pegase 2.7714e+06 $/h (SOC gap 64.11%), case6495_rte 3.0678e+06 (15.11%), case2742_goc__api 6.0996e+05 (22.67%), case3970_goc__api 1.7494e+06 (38.79%). A cheaper AC-feasible point would show that the published baseline is not globally optimal for that case.

## What counts as a win

For one in-scope case (listed in https://github.com/power-grid-lib/pglib-opf/blob/master/BASELINE.md for v23.07 with Nodes >= 1000 and SOC Gap >= 1.00, network not one of the five excluded), give a full AC operating point (bus voltage magnitudes and angles, generator P and Q) for the unmodified v23.07 .m file. Use the standard polar AC power-flow model with MATPOWER conventions: branch pi-model with taps and shifts, and bus shunts. Only in-service elements count, as in PowerModels: generators and branches with status 0 carry no power and stay off, and type-4 buses are dropped. The point must satisfy all of the following: every bus P and Q balance holds within 1e-6 p.u. on baseMVA; all voltage, generator and branch angle-difference bounds hold within 1e-6; every branch apparent-power flow at both ends is at most rate_a * (1 + 1e-6); and the polynomial gencost objective summed over in-service generators is below the BASELINE.md AC value times (1 - 1e-4) (the listed value has 5 significant figures). The checker must first reproduce the BASELINE AC objective within 1e-4 relative from an Ipopt solve of the same case.

## Partial wins

- **p1:** An independent AC-feasibility and cost checker (not PowerModels or MATPOWER code) that, given points from PowerModels + Ipopt solves, reproduces the BASELINE.md AC objective within 1e-4 relative and reports all residuals below 1e-6 on 20 in-scope cases.
- **p2:** For an in-scope case, two AC-feasible local optima (by the full-win checks) whose objectives differ by more than 1e-3 relative, showing a non-trivial local-optimum structure; the lower one need not beat the baseline.

## How a win is checked

Download the case from https://raw.githubusercontent.com/power-grid-lib/pglib-opf/master/ (api/ and sad/ subfolders for those conditions) at tag v23.07, parse the MATPOWER struct, recompute all injections and branch flows from the claimed voltages with a short numpy script, check every bound and the cost, and compare with the BASELINE.md row (sha256 of BASELINE.md 0634196fbf73cc0e19f6d19fa04032a26a218e42779e08e9265bc11b89dca62c on 2026-10-30). Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/power-grid-lib/pglib-opf/blob/master/BASELINE.md>

## Sources

- <https://github.com/power-grid-lib/pglib-opf>
- <https://github.com/power-grid-lib/pglib-opf/blob/master/BASELINE.md>
- <https://github.com/power-grid-lib/pglib-opf/releases/tag/v23.07>
- <https://arxiv.org/abs/1908.02788>
- <https://arxiv.org/abs/2203.11328>
- <https://doi.org/10.1016/j.epsr.2022.108683>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Multistart Ipopt from randomised voltage profiles and from SOC/QC-relaxation solutions; congested (API) cases with large gaps are the likeliest to hide better local optima.
- Fix the generator commitment pattern implied by an SDP or QC relaxation solution and re-solve AC; try spatial branch-and-bound on a reduced network around binding lines.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Most baseline points are probably near-global; a large relaxation gap usually reflects a weak relaxation, not a bad local optimum, hence the low tractability.
- Tolerance games: loosening balance or line-limit tolerances lowers cost; the checks are absolute at 1e-6 p.u.
- Out-of-service units: most in-scope cases have many status-0 generators (e.g. 782 of 1,349 in case4917_goc, 692 of 1,372 in case6495_rte) and some status-0 branches. Switching them on gives a cheaper but invalid dispatch, so they must stay off.
- rate_a = 0 would mean unlimited in MATPOWER (no in-service branch of an in-scope case uses it); angmin/angmax and gencost model 2 coefficient order must be read exactly.
- pglib-opf issue #48: the rte6xxx cases (including in-scope case6470_rte and case6495_rte) have a phase shifter in parallel with a line, probably a data error. Deleting it lowers case6495_rte's cost by about 57 $/h, but the case must be used unmodified.
- MINLPLib's acopf_* instances use a different scaling; those five networks are excluded here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/pglib-opf-v2307-ac-cheaper-dispatch.md
```

Already set up? Say `run V3R1T4S on pglib-opf-v2307-ac-cheaper-dispatch`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pglib-opf-v2307-ac-cheaper-dispatch`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
