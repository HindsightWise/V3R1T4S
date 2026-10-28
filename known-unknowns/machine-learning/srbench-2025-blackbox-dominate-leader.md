# SRBench 2025 black-box: a symbolic regressor that Pareto-dominates the best-accuracy method on a dataset

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

SRBench (William La Cava, Patryk Orzechowski, Bogdan Burlacu, Fabrício Olivetti de França, Marco Virgolin, Ying Jin, Michael Kommenda, Jason Moore; 2025 edition led by Guilherme Imai Aldeia, Hengzhe Zhang, Geoffrey Bomarito, Miles Cranmer, Alcides Fonseca, Bogdan Burlacu, William La Cava and Fabrício Olivetti de França) benchmarks symbolic regression. The 2025 black-box track ran 28 methods on 12 PMLB datasets with 30 fixed train/test splits each and published every returned model with its test R² and model_size (SRBench's sympy node count, or the method's own complexity where sympy parsing failed). The best median R² is often bought with very large models, e.g. 1028_SWD PS-Tree 0.380 at size 3270, 522_pm10 PS-Tree 0.301 at size 4996, 1193_BNG_lowbwt EQL 0.602 at size 188; elsewhere small models lead, e.g. 210_cloud Genetic Engine 0.8465 at size 7. Can a symbolic regression procedure beat the best median test R² on a dataset while also matching or undercutting that method's median model size?

## What counts as a win

For a named dataset D among the 12 SRBench 2025 black-box datasets: a symbolic regression procedure run on each of the 30 splits used in results.feather (train_test_split with train_size 0.75 and random_state equal to each listed seed, as in experiment/evaluate_model.py on the srbench_2025 branch, including its training subsampling rule) that returns one closed-form expression per split, such that (a) the median test R² over the 30 splits is STRICTLY GREATER (direction: max) than the highest median r2_test of any algorithm for D in https://github.com/cavalab/srbench/tree/srbench_2025/results/black-box-tuning (results.feather, re-fetched live immediately before claiming), and (b) the median complexity of the 30 expressions, computed with SRBench's own symbolic_utils.complexity, is less than or equal to that leading algorithm's median model_size. The procedure must be fixed before scoring (no per-split hand edits).

## Partial wins

- **p1:** For a dataset D, a procedure whose (median R², median complexity) point is not dominated by any algorithm's point in results.feather and strictly dominates at least one point currently on the Pareto front.
- **p2:** For a dataset D, a procedure with median complexity at most 20 whose median test R² beats every algorithm whose own median model_size is at most 20.

## How a win is checked

Download the PMLB dataset, rebuild the 30 splits from the seeds in results.feather with evaluate_model.py's code, load the saved expression for each split, evaluate test R² with numpy, compute complexity with symbolic_utils.complexity after the same sympy parsing, take medians, and compare with the medians recomputed from results.feather (excluding rows with model_size -1 only when computing sizes). Re-run the procedure on two splits to confirm it returns the saved expressions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/cavalab/srbench/tree/srbench_2025/results/black-box-tuning>

## Sources

- <https://github.com/cavalab/srbench/tree/srbench_2025/results/black-box-tuning>
- <https://github.com/cavalab/srbench>
- <https://raw.githubusercontent.com/cavalab/srbench/master/README.md>
- <https://raw.githubusercontent.com/cavalab/srbench/srbench_2025/results/README.md>
- <https://raw.githubusercontent.com/cavalab/srbench/srbench_2025/experiment/evaluate_model.py>
- <https://cavalab.org/srbench/results/>
- <https://arxiv.org/abs/2505.03977>
- <https://github.com/EpistasisLab/pmlb>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Distil a strong black-box model into a formula: fit gradient boosting or a tabular foundation model, then run symbolic regression (PySR, Operon) on its smoothed predictions with additive structure found by partial dependence, the 'symbolic distillation' idea from Cranmer's work.
- Generalised additive models from statistics: fit a GAM, then replace each shape function by a short closed form (piecewise-linear with max/min, logs) and refit constants jointly.
- Target the datasets where the leader is huge (1028_SWD, 522_pm10, 1193_BNG_lowbwt): an expression of size a few hundred only needs to edge past the leader's R² to dominate it.
- Multi-objective evolutionary search from engineering design (NSGA-II with complexity as an explicit objective) plus constant refitting with Levenberg-Marquardt, as in Operon, run with a longer budget than the benchmark's.
- Robust losses from statistics (Huber, trimmed) for noisy targets like pm10 and visualizing_environmental, since outliers dominate R².

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Split mismatch: the 30 seeds and the training subsampling in evaluate_model.py must be reproduced exactly; using different splits makes medians incomparable.
- Complexity mismatch: SRBench measures size after its own sympy parsing; an expression that looks small but expands under sympy (e.g. nested powers) may count larger. Use symbolic_utils.complexity.
- Non-symbolic models: a formula embedding a lookup table, piecewise definitions with hundreds of branches or a numeric array literal is not a closed-form expression in the benchmark's sense.
- Test-split tuning: choosing hyperparameters by test R² across the 30 splits is leakage; tune inside the training part.
- model_size is -1 for rows where SRBench failed to parse a model; exclude those only from size medians, not from R² medians, and say so.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/srbench-2025-blackbox-dominate-leader.md
```

Already set up? Say `run V3R1T4S on srbench-2025-blackbox-dominate-leader`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `srbench-2025-blackbox-dominate-leader`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
