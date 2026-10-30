# M5 uncertainty competition: beat the winning private WSPL 0.15420 for nine-quantile Walmart sales forecasts

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (same 450 MB M5 data; quantile models at 12 levels) · open as of 2026-10-30

## The problem

The uncertainty track of M5 (Makridakis, Spiliotis, Assimakopoulos, Chen, Gaba, Tsetlin and Winkler; IJF 2022) asked for the 0.005, 0.025, 0.165, 0.25, 0.5, 0.75, 0.835, 0.975 and 0.995 quantiles of 28-day Walmart unit sales for all 42,840 series at 12 aggregation levels, scored by WSPL, the weighted scaled pinball loss. In the organisers' Scores and Ranks.xlsx (Uncertainty-Top50 sheets) the winner Everyday Low SPLices (described by Lainder and Wolfinger, IJF 2022) scores 0.15420, GoodsForecast - Nick Mamonov 0.15891, Ouranos 0.15893 and Marisaka Mozz 0.15958. The same public Drive folder as the accuracy track holds the evaluation-period truth, weights and the organisers' R evaluation code, and the uncertainty submissions folder holds the top-50 quantile files. Open task: a test-blind pipeline with WSPL below 0.15420.

## What counts as a win

Saved quantile forecasts at the nine official levels for all 42,840 series and 28 days d_1942-d_1969 whose WSPL, computed with the organisers' uncertainty evaluation code and weights from the M5 Drive folder, is STRICTLY LOWER (direction: min) than 0.15420 (Everyday Low SPLices, Uncertainty-Top50 (AL) sheet of Scores and Ranks.xlsx at https://github.com/Mcompetitions/M5-methods) and than any lower WSPL the skeptic finds in a credible paper for a test-blind method. LEAK RULE: a frozen, hashed script rerun in a fresh environment containing only sales_train_evaluation.csv, calendar.csv and sell_prices.csv; all tuning on folds ending by d_1941; no pretrained component trained on M5 data.

## Partial wins

- **p1:** Reproduce 0.15420 from the winner's released quantile file with the organisers' code, then score strictly below 0.15891 (2nd place) under the full-win leak rule.
- **p2:** Under the full-win leak rule, a mean scaled pinball loss over levels 10-12 strictly below the winner's (L10 0.28385, L11 0.27006, L12 0.26504; mean 0.27298) with overall WSPL no higher than 0.160.

## How a win is checked

As for the accuracy track: hash the released data, rerun the frozen script without the test file, score with the organisers' R code after confirming it reproduces 0.15420 on the winner's submission, and audit for test-tuned constants.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/Mcompetitions/M5-methods>

## Sources

- <https://github.com/Mcompetitions/M5-methods>
- <https://github.com/Mcompetitions/M5-methods/raw/master/Scores%20and%20Ranks.xlsx>
- <https://drive.google.com/drive/folders/1D6EWdVSaOtrP1LEFh1REjI3vej6iUS_4>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Quantile gradient boosting per level with augmentation over many training windows, then isotonic or conformal recalibration fitted on late training folds.
- Coherent quantiles across levels via sample-path simulation from a bottom-level count model.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The extreme quantiles (0.005, 0.995) dominate errors on intermittent bottom-level series; calibrating them on the test days is leakage.
- No 2024-2026 literature sweep could be run on 2026-10-30; check for lower published WSPL first.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/m5-uncertainty-beat-winner-wspl.md
```

Already set up? Say `run V3R1T4S on m5-uncertainty-beat-winner-wspl`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `m5-uncertainty-beat-winner-wspl`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
