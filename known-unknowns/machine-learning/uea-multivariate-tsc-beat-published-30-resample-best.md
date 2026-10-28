# UEA multivariate time series classification: beat the best published 30-resample mean accuracy on a dataset

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The UEA multivariate archive (Bagnall, Dau, Lines, Flynn, Large, Bostrom, Southam, Keogh) has 26 equal-length multivariate classification datasets with default splits. Alejandro Pasos Ruiz, Michael Flynn, James Large, Matthew Middlehurst and Anthony Bagnall's multivariate bake-off (2021) and the HIVE-COTE 2 paper (Middlehurst et al. 2021) published 30-resample accuracies for about 20 classifiers, hosted at timeseriesclassification.com. Best means include Handwriting 0.6121 (DTW_D), LSST 0.6370 (HC2), FaceDetection 0.7135 (HC2), SelfRegulationSCP2 0.5369 (DTW_D), EigenWorms 0.9056 (DrCIF), Heartbeat 0.7652 (CIF). Newer methods (MR-Hydra, QUANT, convolutional transformers) have not been posted to this table. Can a new classifier beat the best published mean on some dataset?

## What counts as a win

For a named UEA multivariate dataset D: saved test predictions for all 30 resamples (tsml-eval stratified resampling with random_state = r on the default split, r = 0..29), each model fit only on that resample's training part, with mean accuracy STRICTLY GREATER (direction: max) than the largest 30-resample mean for D across every *_TESTFOLDS.csv in https://timeseriesclassification.com/results/PublishedResults/Bakeoff2021/ and https://timeseriesclassification.com/results/PublishedResults/HIVE-COTEV2/ re-fetched live immediately before claiming, and greater than any credible published 30-resample mean for D that the skeptic finds (including any multivariate files later added under ReferenceResults).

## Partial wins

- **p1:** Beat the best published accuracy on the default split (resample 0) and the best mean over resamples 0-9 for a dataset D.
- **p2:** One fixed classifier configuration that beats the best published mean on at least two datasets.

## How a win is checked

Recreate the resamples with tsml-eval's stratified resampling, align predictions and labels, recompute per-resample accuracy and the mean, re-run training for two resamples from the saved script and seed, and recompute the published maximum from the downloaded CSVs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://timeseriesclassification.com/results/PublishedResults/Bakeoff2021/>

## Sources

- <https://timeseriesclassification.com/results/PublishedResults/Bakeoff2021/>
- <https://timeseriesclassification.com/results/PublishedResults/HIVE-COTEV2/>
- <https://www.timeseriesclassification.com/results.php>
- <https://github.com/time-series-machine-learning/tsml-eval>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run the modern convolution-kernel family (MultiROCKET-Hydra, QUANT) channel-wise and jointly; these routinely beat ROCKET and HC2 on univariate data but are absent from this table.
- EEG and BCI methods for SelfRegulationSCP1/2, MotorImagery, FingerMovements: Riemannian geometry on covariance matrices (tangent-space logistic regression, minimum distance to Riemannian mean) and common spatial patterns from brain-computer-interface research.
- Astronomy features for LSST: the PLAsTiCC-challenge winners used Gaussian-process light-curve interpolation and redshift-aware features; the series here are LSST simulated light curves.
- Handwriting and gesture sets: rotation-invariant and path-signature features (rough path theory) of the 3D accelerometer trajectories.
- Channel selection (from feature selection literature) to drop noisy dimensions before the classifier, chosen by cross-validation on the training part.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The hosted table is from 2021; later papers may already report higher 30-resample means; the novelty check must search the literature for D.
- Unequal-length datasets (e.g. JapaneseVowels, CharacterTrajectories) are not in this 26-dataset set; use the equal-length versions the bake-off used.
- Default-split wins are noise on small test sets (AtrialFibrillation has 15 test cases).
- Do not tune on resample test accuracy; nest all tuning inside the training part.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/uea-multivariate-tsc-beat-published-30-resample-best.md
```

Already set up? Say `run V3R1T4S on uea-multivariate-tsc-beat-published-30-resample-best`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `uea-multivariate-tsc-beat-published-30-resample-best`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
