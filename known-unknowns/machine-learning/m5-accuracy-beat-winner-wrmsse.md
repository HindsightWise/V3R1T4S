# M5 accuracy competition (Walmart unit sales): beat the winning private WRMSSE 0.52044 with a frozen, test-blind pipeline

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (about 450 MB of CSV, 30,490 bottom-level series; LightGBM-style models need 16-32 GB RAM) · open as of 2026-10-30

## The problem

The M5 competition (Spyros Makridakis, Evangelos Spiliotis and Vassilios Assimakopoulos with Walmart and Kaggle, 2020; IJF 2022) asked for 28-day forecasts of 42,840 hierarchical series of Walmart unit sales (3,049 products in 10 stores in 3 states, 12 aggregation levels) for days d_1942 to d_1969. The accuracy track was scored by WRMSSE: RMSSE per series, weighted by dollar sales over the last 28 training days and averaged over the 12 levels. The organisers' Scores and Ranks.xlsx (Mcompetitions/M5-methods) gives the private scores: YJ_STU (Yeonjun In) 0.52044, Matthias 0.52816, mf 0.53572, monsaraida 0.53583. Their public Google Drive folder releases sales_train_evaluation.csv (d_1 to d_1941), sales_test_evaluation.csv (the 28 scored days), calendar.csv, sell_prices.csv, weights_evaluation.csv and the R scorer (Estimate WRMSSE.R), so the private leaderboard can be recomputed exactly. Open task: a pipeline that never reads the test days and scores below 0.52044.

## What counts as a win

Saved 28-day point forecasts for all 30,490 bottom-level series (aggregated to all 12 levels as the organisers' scorer does) whose WRMSSE on d_1942-d_1969, computed with the organisers' Estimate WRMSSE.R and weights_evaluation.csv, is STRICTLY LOWER (direction: min) than 0.52044 (YJ_STU, Accuracy-Top50 (AL) sheet of https://github.com/Mcompetitions/M5-methods Scores and Ranks.xlsx) and than any lower WRMSSE that a paper or public write-up reports for a test-blind method on the same task: all 42,840 series, days d_1942-d_1969, the organisers' weights and scorer. Numbers computed with other scorers, on subsets or other windows, or without the full 12-level hierarchy (for example the 0.092-0.661 'WRMSSE' values in arXiv:2506.13036) are not comparable and are not records. LEAK RULE: a frozen, hashed script that the skeptic reruns in a fresh environment containing only sales_train_evaluation.csv, calendar.csv and sell_prices.csv (sales_test_evaluation.csv absent); all tuning, including any global multiplier, done on folds that end by d_1941; any pretrained component documented as never trained on M5 data.

## Partial wins

- **p1:** Scorer check plus a modest win: reproduce YJ_STU's 0.52044 from the organisers' released submission files, then score strictly below 0.53572 (3rd place, mf) under the full-win leak rule.
- **p2:** Under the full-win leak rule, a mean WRMSSE over the three bottom levels strictly below YJ_STU's 0.92622 (mean of L10 0.965581, L11 0.928931 and L12 0.884160 in the Accuracy-Top50 (AL) sheet), with overall WRMSSE no higher than 0.53.

## How a win is checked

Download the organisers' Dataset folder, hash the files, run the frozen script in a container without sales_test_evaluation.csv, then score with Estimate WRMSSE.R; first confirm the scorer reproduces 0.52044 on YJ_STU's released accuracy submission. Read the code for constants tuned on the test days (multipliers, day-of-week fixes).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/Mcompetitions/M5-methods>

## Sources

- <https://github.com/Mcompetitions/M5-methods>
- <https://raw.githubusercontent.com/Mcompetitions/M5-methods/master/README.md>
- <https://github.com/Mcompetitions/M5-methods/raw/master/Scores%20and%20Ranks.xlsx>
- <https://drive.google.com/drive/folders/1D6EWdVSaOtrP1LEFh1REjI3vej6iUS_4>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Store-by-department LightGBM with Tweedie loss, the winning family, plus recursive and direct horizon blends chosen on several late training folds.
- Hierarchical reconciliation (MinT or top-down from level 9) because WRMSSE averages all 12 levels equally.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Post-deadline Kaggle notebooks often tune a 'magic multiplier' or the final days against the leaked evaluation labels; any constant chosen on d_1942-d_1969 voids the claim.
- Using sales_train_validation.csv weights instead of weights_evaluation.csv changes the score.
- Some papers print M5 'WRMSSE' values far below 0.52 that are not comparable. arXiv:2506.13036 (a 2025 forecast-then-optimize survey) reports 0.092 for TimeSpeaks and 0.157 for NLinear without exogenous features, plainly a different computation. A literature search on 2026-10-30 (arXiv, IJF, Kaggle write-ups, Nixtla's M5 evaluation) found no test-blind score below 0.52044 on the official task; re-check before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/m5-accuracy-beat-winner-wrmsse.md
```

Already set up? Say `run V3R1T4S on m5-accuracy-beat-winner-wrmsse`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `m5-accuracy-beat-winner-wrmsse`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
