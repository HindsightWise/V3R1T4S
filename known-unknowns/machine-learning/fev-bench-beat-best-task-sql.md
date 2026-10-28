# fev-bench forecasting: beat the best posted scaled quantile loss on a task with locally run open-weight models

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

fev-bench (Oleksandr Shchur, Abdul Fatir Ansari, Caner Turkmen and colleagues at AWS, with the fev library; arXiv:2509.26468) is a forecasting benchmark of 100 tasks with fixed rolling evaluation windows. Its GitHub repository stores one results CSV per model: 44 files on 2026-10-28 (iAmTime was added that day), including Chronos-2, TimesFM-2.5/3, TiRex, Toto 2.0, Moirai 2.0, TabPFN-TS, TimeH2O-v1, Timestral, t0-gamma, statistical baselines and four entries that benchmarks/fev_bench/models.yaml marks closed-api (ChakraTS, Lingjiang2.0, TimeRSI-1.0, TimeRSI-1.5). Each row gives test_error (scaled quantile loss, SQL) per task and a trained_on_this_dataset flag. Ignoring leaked rows (trained_on_this_dataset = True, mostly Moirai-2.0, TimesFM-2.5, Toto-1.0 and FlowState), closed-api systems lead 30 of the 100 tasks (TimeRSI-1.0 alone leads 20). On many tasks the best and second-best models are within 0.1%, but on others the leader is several percent ahead, e.g. rohlik_orders_1W (timeh2o-v1 1.1157 vs FlowState 1.2428), us_consumption_1Q (t0-gamma 1.5001 vs TimeRSI-1.0 1.5885), favorita_transactions_1D (Chronos-2 0.6846 vs Timestral-209M 0.7229), solar_1W (TimeRSI-1.0 0.6727; best open-weight citras-fm 0.7992). Can a locally run combination of open-weight models and classical methods beat the best posted non-leaked SQL on some task?

## What counts as a win

For a named fev-bench task T: a forecast produced by running the fev library's task definition for T (all evaluation windows, the official horizon and quantile levels) on a laptop, using only open-weight models and classical methods run locally whose training data did not include T's dataset (documented), whose fev-computed test_error (SQL) is STRICTLY LOWER (direction: min) than the minimum test_error for T over all rows with trained_on_this_dataset not True in all CSV files in https://github.com/autogluon/fev/tree/main/benchmarks/fev_bench/results, re-fetched live immediately before claiming (fetch each CSV via raw.githubusercontent.com). Closed-api rows count toward this minimum. Saved forecasts plus the script must reproduce the score.

## Partial wins

- **p1:** On a task whose non-leaked leader is a closed-api entry (one marked model_type: closed-api in benchmarks/fev_bench/models.yaml, which on 2026-10-28 lists ChakraTS, Lingjiang2.0, TimeRSI-1.0 and TimeRSI-1.5), a test_error strictly below the minimum over all non-leaked rows of the other (open-weight and classical) entries, under the same protocol as the full win.
- **p2:** A single fixed ensemble recipe that, under the full-win protocol, beats the best posted non-leaked SQL on at least three tasks.

## How a win is checked

Install the pinned fev version, load task T from the benchmark's tasks.yaml, load the saved per-window forecasts (or re-run the saved script), and compute SQL with fev's evaluator. Re-download every results CSV and take the minimum test_error for T over rows whose trained_on_this_dataset is not True. Confirm each model's training corpus documentation does not list T's dataset and that no model received future values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/autogluon/fev/tree/main/benchmarks/fev_bench/results>

## Sources

- <https://github.com/autogluon/fev/tree/main/benchmarks/fev_bench/results>
- <https://raw.githubusercontent.com/autogluon/fev/main/benchmarks/fev_bench/models.yaml>
- <https://github.com/autogluon/fev>
- <https://raw.githubusercontent.com/autogluon/fev/main/README.md>
- <https://huggingface.co/spaces/autogluon/fev-bench>
- <https://arxiv.org/abs/2509.26468>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Forecast combination from the M-competition literature: median or quantile-averaged ensembles of Chronos-2, TiRex, TimesFM-2.5 and Toto open checkpoints (quantile averaging, sometimes called Vincentization) usually beat each member on probabilistic loss.
- Weather-forecasting style post-processing: fit isotonic or EMOS-type quantile recalibration on the earlier, non-evaluated history of each series, then apply it to the final windows.
- Use covariates the zero-shot models ignore: for tasks with known dynamic columns (holidays, prices, weather), feed them to a covariate-aware model (Chronos-2 with covariates, TabPFN-TS, LightGBM quantile regression) and blend.
- Hierarchical reconciliation from official statistics (MinT) on hierarchical_sales and tourism tasks.
- Pick tasks where the leader's margin is large (several percent) rather than tasks where many models tie within 0.1%.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Leakage through pretraining: some foundation models were trained on corpora containing these datasets (GIFT-Eval, Monash, M5); using one whose training data covers T's test period is not a legitimate win.
- Window misuse: fitting or calibrating on data from later windows before forecasting earlier ones leaks the future; fev's rolling windows must be respected in order.
- Metric mismatch: SQL depends on the quantile levels and on the seasonal-naive scaling; compute it with fev, not a re-implementation.
- Per-task cherry-picking across hundreds of ensemble variants overfits the test windows; fix the recipe on validation windows carved from training history before scoring.
- Results CSVs change often (eight result additions between 2026-10-06 and 2026-10-28); re-fetch all of them right before claiming, and exclude rows flagged trained_on_this_dataset = True from the bar exactly as the criterion says.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/fev-bench-beat-best-task-sql.md
```

Already set up? Say `run V3R1T4S on fev-bench-beat-best-task-sql`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fev-bench-beat-best-task-sql`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
