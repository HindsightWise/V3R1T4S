# TabArena-v0.1: beat the best mean test error of all 94 leaderboard entries on one of the 51 curated tabular datasets

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours per small dataset (up to 2,400 rows, 30 splits); laptop-days for the 9-split datasets up to 150k rows · open as of 2026-10-30

## The problem

TabArena-v0.1 (Nick Erickson, Lennart Purucker, Andrej Tschalzev, David Holzmuller, Prateek Mutalik Desai, David Salinas, Frank Hutter and contributors; arXiv 2506.16791) is a living benchmark of 51 curated IID tabular datasets. Each has fixed outer splits (30 for the 17 datasets of up to 2,400 rows, 9 for larger ones), and the metric is 1-AUC (binary), log loss (multiclass) or RMSE (regression). The full leaderboard view (models plus open-source systems, systems with LLMs and closed-source API systems; space updated 2026-10-28) has 94 entries; by Elo, Kumo-Tabular (2025), LimiX-2 (2001) and Chakra-Tab full (1961) lead. On most datasets a foundation model or a 4-hour AutoGluon system has the best mean test error, often by tiny margins. For example, on heloc (1-AUC) LimiX-2 scores 0.196859 against Kumo-Tabular's 0.196863; on Food_Delivery_Time (RMSE) Kumo-Tabular scores 7.19902 against ChimeraBoost (tuned + ensemble) at 7.19924; on hiva_agnostic tuned RandomForest and tuned ExtraTrees tie at the top (log loss 0.173849); on polish_companies_bankruptcy AutoGluon 1.5 (extreme, 4h) leads (0.003449). LimiX-2 is flagged for leakage on blood-transfusion-service-center and diabetes. Can a method beat the best entry's mean test error on a dataset?

## What counts as a win

For a named TabArena-v0.1 dataset D: saved code, seeds and per-split test predictions for every official outer split of D (TabArena's OpenML task and split definitions), each model fit only on that split's training part. The mean test error over all splits (TabArena's metric for D, computed with TabArena's scorer) must be STRICTLY LOWER (direction: min) than the lowest mean error for D among all entries not flagged for leakage on D in the full entrant view (models, open-source systems, systems with LLMs and closed-source API systems; no imputation). That bar is the POINTS 'e' values in https://huggingface.co/spaces/TabArena/leaderboard/resolve/main/data/entrants_open_llm_api/imputation_no/splits_all/tasks_all/datasets_all/per_dataset_explorer.html (94 entries on 2026-10-30), re-fetched live immediately before claiming; leakage flags are window.TABARENA_LEAKAGE in the same file. No pretrained model whose training data include D or its source may be used.

## Partial wins

- **p1:** On a dataset D, mean test error over all splits strictly below the best entry in the Tree-based, Neural Network, Baseline and Other families (no foundation models or systems) in the live full-view per-dataset data, with a model trained from scratch on each split's training data only.
- **p2:** Beat the lowest non-leakage mean error for D over the TabArena-Lite splits (as defined by the tabarena package), as listed in https://huggingface.co/spaces/TabArena/leaderboard/resolve/main/data/entrants_open_llm_api/imputation_no/splits_lite/tasks_all/datasets_all/per_dataset_explorer.html, under the same fitting rules.

## How a win is checked

Install tabarena and rebuild D's outer splits from its OpenML task. Check that the saved predictions align with each split's test indices. Recompute the metric per split with TabArena's scorer and average. Re-run fitting on 2 splits from the saved script. Check that training never touched test rows and that no pretrained model saw D, then re-fetch the full-view (entrants_open_llm_api) per-dataset explorer data and compare against the lowest non-leakage 'e' for D.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://huggingface.co/spaces/TabArena/leaderboard/resolve/main/data/entrants_open_llm_api/imputation_no/splits_all/tasks_all/datasets_all/per_dataset_explorer.html>

## Sources

- <https://huggingface.co/spaces/TabArena/leaderboard/resolve/main/data/entrants_open_llm_api/imputation_no/splits_all/tasks_all/datasets_all/per_dataset_explorer.html>
- <https://huggingface.co/spaces/TabArena/leaderboard>
- <https://github.com/autogluon/tabarena>
- <https://arxiv.org/abs/2506.16791>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Pick datasets where the leader's margin over strong trees is tiny (Food_Delivery_Time, heloc) or where trees lead (hiva_agnostic). Domain features, such as delivery distance from coordinates or monotonic constraints on credit scores, can move the last 0.1%.
- Stack locally runnable open-weight tabular foundation models with tuned GBDTs, fitting the blender on inner cross-validation only.
- Post-processing matched to the metric: temperature scaling for log-loss datasets, rank-averaging for 1-AUC.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Many datasets have public copies online, so a pretrained model or LLM that saw D is leakage (TabArena flags LimiX-2 on two datasets).
- The bar is the mean over all splits, not the best split; 30-split datasets need all 30.
- Margins are often below 0.1%, and the explorer's 'e' values are rounded to 6 significant figures; a claim must be strictly below the listed value, and a margin smaller than that rounding should be reported as unresolved.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/tabarena-v01-per-dataset-best-error.md
```

Already set up? Say `run V3R1T4S on tabarena-v01-per-dataset-best-error`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tabarena-v01-per-dataset-best-error`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
