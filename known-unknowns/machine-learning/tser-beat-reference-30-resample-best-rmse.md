# Time series extrinsic regression (TSER archive): beat the best reference regressor's 30-resample mean RMSE on a dataset

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The Time Series Extrinsic Regression archive (Chang Wei Tan, Christoph Bergmeir, François Petitjean, Geoffrey Webb; extended by David Guijo-Rubio, Matthew Middlehurst, Anthony Bagnall and others to 63 datasets) predicts a continuous value from a whole time series. timeseriesclassification.com hosts reference RMSE results for 19 regressors (estimators.txt: 1NN/5NN-DTW and -ED, CNN, DrCIF, FCN, FPCR, FPCR-b-spline, FreshPRINCE, GridSVR, InceptionTime, RandF, ResNet, Ridge, ROCKET, RotF, SingleInceptionTime, XGBoost) over 30 resamples of all 63 datasets. Newer methods such as MultiROCKET-Hydra and QUANT are not in the reference set. tsml-eval's TSER archive-expansion results (publications/y2023/tser_archive_expansion) add MultiROCKET, TSF and an InceptionTime ensemble, which beat the reference minimum on 7 datasets (e.g. GasSensorArrayAcetone 0.1435 vs DrCIF 0.1845), so on those datasets the bar is lower than the reference files show. For many datasets the gap between the best and the second-best is several percent, for example WindTurbinePower (FreshPRINCE 44.66 vs RotF 74.25), DhakaHourlyAirQuality (1.784 vs 2.702), SodiumConcentration (DrCIF 312.8 vs GridSVR 362.6). Can a new regressor beat the best reference and published 30-resample mean RMSE on some dataset?

## What counts as a win

For a named TSER dataset D: saved test predictions for all 30 resamples (resample r from tsml-eval's regression resampling with random_state = r applied to the default split, resample 0 = default split), each from a model fit only on that resample's training part, whose mean test RMSE over the 30 resamples is STRICTLY LOWER (direction: min) than the smallest 30-resample mean for D across every *_rmse.csv file at https://timeseriesclassification.com/results/ReferenceResults/regression/rmse/ re-fetched live immediately before claiming, and below any credible published 30-resample mean for D the skeptic finds (including the TSER archive-expansion results in tsml-eval's publications/y2023/tser_archive_expansion).

## Partial wins

- **p1:** Beat the best reference RMSE on the default split (resample 0) and the best reference mean over resamples 0-9 for a dataset D.
- **p2:** One fixed regressor configuration that beats the reference best mean RMSE on at least three datasets.

## How a win is checked

Recreate the 30 resamples with tsml-eval's resampling utilities, align saved predictions with each resample's test cases, recompute RMSE per resample and the mean, re-run training on two resamples from the saved script and seed, and re-download all reference *_rmse.csv files to take the minimum mean for D.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://timeseriesclassification.com/results/ReferenceResults/regression/rmse/>

## Sources

- <https://timeseriesclassification.com/results/ReferenceResults/regression/rmse/>
- <https://timeseriesclassification.com/results/ReferenceResults/regression/>
- <https://timeseriesclassification.com/results/ReferenceResults/regression/estimators.txt>
- <https://github.com/time-series-machine-learning/tsml-eval>
- <https://www.timeseriesclassification.com/results.php>
- <https://github.com/time-series-machine-learning/tsml-eval/tree/main/tsml_eval/publications/y2023/tser_archive_expansion>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run modern convolution-kernel regressors (MultiROCKET-Hydra, QUANT with extra-trees) that are missing from the reference set, then stack them with FreshPRINCE and DrCIF using out-of-fold predictions inside each training set.
- Chemometrics for the element-concentration sets (SodiumConcentration, PotassiumConcentration and the rest): if the series are spectra, as their names suggest, PLS regression, Savitzky-Golay derivatives and multiplicative scatter correction are standard spectroscopy preprocessing and are absent from the reference methods. Check the dataset descriptions first.
- Physics-informed features for the energy and weather sets (WindTurbinePower, Solar, AustraliaRainfall): power-curve transforms of wind speed (cubic law), clear-sky normalisation, daily cycle harmonics.
- Target transforms from econometrics: model log or Box-Cox of skewed targets and correct the back-transform bias (smearing estimator) before computing RMSE.
- Gradient-boosted trees on catch22 or tsfresh summary features with monotonic constraints where domain knowledge allows.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- RMSE is scale-dependent; a mistake in un-normalising the target (fitting the scaler on all data, or forgetting the inverse transform) gives fake wins or losses.
- Default-split-only results are not the record; all 30 resamples are required.
- The reference set excludes some newer published methods; a claim must also beat the best credible published 30-resample mean for D (search Guijo-Rubio et al.'s TSER bake-off and later papers).
- Some datasets have missing values ('_nmv') or unequal lengths ('_eq'); use the same processed version as the reference files.
- Hyperparameter tuning must be nested within each resample's training data.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/tser-beat-reference-30-resample-best-rmse.md
```

Already set up? Say `run V3R1T4S on tser-beat-reference-30-resample-best-rmse`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tser-beat-reference-30-resample-best-rmse`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
