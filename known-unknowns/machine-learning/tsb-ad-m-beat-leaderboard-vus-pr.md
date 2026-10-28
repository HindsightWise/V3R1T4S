# TSB-AD multivariate anomaly detection: beat the leaderboard's best average VUS-PR on the evaluation set

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

TSB-AD (Qinghua Liu and John Paparrizos, NeurIPS 2024 Datasets and Benchmarks; maintained by TheDatumOrg) is a curated time-series anomaly detection benchmark with a fixed split of series into a tuning set and an evaluation set and a recommended metric, VUS-PR (volume under the precision-recall surface). The community leaderboard (open to submissions since 2026-04-01; last updated 2026-10-20, when Syntropic, CHARM (kNN/ZS), VERITY-AD and AxonAD were added) ranks methods by average VUS-PR. On the multivariate track TSB-AD-M, the pretrained CHARM (kNN) leads at 0.54, followed by AxonAD at 0.50 (the best method not marked pretrained), CHARM (ZS) at 0.46 and StreamVAE at 0.44, while the classic PCA baseline scores 0.31. On the univariate track the best is CHARM (kNN) at 0.68, then Syntropic at 0.67 and VERITY-AD at 0.61 (the best not marked pretrained). Can a method with hyperparameters chosen only on the tuning set beat the best TSB-AD-M average?

## What counts as a win

A detector whose hyperparameters and any model selection used only the TSB-AD-M tuning-set file list, run on every series in the TSB-AD-M evaluation-set file list from the repository's Datasets/File_List, with anomaly scores saved per series, such that the average VUS-PR computed by the repository's get_metrics over all evaluation series is STRICTLY GREATER (direction: max) than the highest TSB-AD-M value in https://thedatumorg.github.io/TSB-AD/static/leaderboard/TSB-AD-updated.html re-fetched live immediately before claiming, and also greater than that leader's unrounded score if the repository's benchmark results files give one. No evaluation-set labels may be used before scoring.

## Partial wins

- **p1:** Beat the best average VUS-PR on TSB-AD-M among methods marked as not pretrained on the live leaderboard (AxonAD, 0.50 on 2026-10-28) with a CPU-only method that runs on all evaluation series in under 6 hours, under the full-win protocol.
- **p2:** Beat the leaderboard's best TSB-AD-U value among methods marked as not pretrained (VERITY-AD, 0.61 on 2026-10-28) on the univariate track, under the same tuning-set-only rule.

## How a win is checked

Clone TheDatumOrg/TSB-AD, download the datasets, read the tuning/evaluation file lists, re-run the saved detector script with its fixed hyperparameters on a random 10% of evaluation series to confirm the saved scores, then compute VUS-PR with TSB_AD.evaluation.metrics.get_metrics for every saved score file and average. Inspect the script for any read of evaluation labels. Re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://thedatumorg.github.io/TSB-AD/static/leaderboard/TSB-AD-updated.html>

## Sources

- <https://thedatumorg.github.io/TSB-AD/static/leaderboard/TSB-AD-updated.html>
- <https://github.com/TheDatumOrg/TSB-AD>
- <https://raw.githubusercontent.com/TheDatumOrg/TSB-AD/main/README.md>
- <https://thedatumorg.github.io/TSB-AD/>
- <https://github.com/TheDatumOrg/TSB-AD/tree/main/Datasets/File_List/>
- <https://github.com/TheDatumOrg/VUS>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensembles of complementary detectors (reconstruction VAE, PCA residuals, isolation forest on lagged windows, matrix-profile discord scores) with rank normalisation, a standard trick in outlier-detection ensembles (Aggarwal and Sathe).
- Process-control statistics from industrial engineering: multivariate CUSUM and Hotelling T² on PCA scores with robust (MCD) covariance, tuned only on the tuning set.
- Score post-processing matters for VUS-PR: smooth scores with windows matched to the series' period and apply per-channel normalisation before aggregating.
- Spectral residual methods from computer vision saliency detection (as used in Microsoft's SR-CNN) applied per channel.
- Graph-structured models: learn a sparse dependency graph among channels on the first part of each series (unsupervised) and score residuals from graph-based predictions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Label peeking: evaluation labels are public; tuning thresholds, windows or model choice on them makes the claim void. All choices must be fixed from the tuning set, and the script must be inspected.
- Rounding: the leaderboard shows two decimals; beating '0.54' needs an exact comparison with the leader's unrounded score where available, or a margin of at least 0.005.
- Metric implementation: VUS-PR has parameters (sliding window, version); use the repository's get_metrics defaults exactly.
- Fine-tuned foundation models that were trained on data overlapping the evaluation series are leakage.
- Skipping series that crash the method lowers the denominator; every evaluation series must have a score file.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/tsb-ad-m-beat-leaderboard-vus-pr.md
```

Already set up? Say `run V3R1T4S on tsb-ad-m-beat-leaderboard-vus-pr`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tsb-ad-m-beat-leaderboard-vus-pr`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
