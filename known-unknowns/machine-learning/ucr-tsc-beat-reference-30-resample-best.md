# UCR univariate time series classification: beat the best reference classifier's 30-resample mean accuracy on a dataset

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The UCR/UEA archive (Hoang Anh Dau, Eamonn Keogh, Anthony Bagnall and colleagues) has 128 univariate classification datasets with fixed default train/test splits. The time-series machine learning group at timeseriesclassification.com (Matthew Middlehurst, Anthony Bagnall, Patrick Schäfer and others) host reference results generated with the aeon toolkit for 40 classifiers (estimators.txt; the *_accuracy.csv files cover 142 univariate datasets), including HIVE-COTE 2, MR-Hydra, QUANT, InceptionTime, WEASEL 2.0, RDST and TS-CHIEF, each on 30 resamples (resample 0 is the default split). For many datasets the best 30-resample mean accuracy is far from 100%, for example Phoneme 0.4172 (DrCIF), Haptics 0.5707 (RDST), InsectWingbeatSound 0.6669 (MR-Hydra), Worms 0.7944 (WEASEL 1.0), FiftyWords 0.8456 (MR-Hydra). Can a new classifier beat the best reference mean on some dataset?

## What counts as a win

For a named univariate dataset D: saved test predictions for all 30 resamples (resample r produced by tsml-eval's stratified resampling with random_state = r applied to the default train/test split, resample 0 = default split), each from a model fit only on that resample's training part, whose mean test accuracy over the 30 resamples is STRICTLY GREATER (direction: max) than the largest 30-resample mean for D across every *_accuracy.csv AND every *_TESTFOLDS.csv file listed at https://timeseriesclassification.com/results/ReferenceResults/classification/accuracy/ re-fetched live immediately before claiming, and greater than any credible published 30-resample mean for D (same resampling) that the skeptic finds in the literature. Missing resamples count as failures.

## Partial wins

- **p1:** On a dataset D whose reference best mean is below 0.95, beat the best reference accuracy on the default split (resample 0 column) and also beat the best reference mean over resamples 0-9.
- **p2:** One fixed classifier configuration (no per-dataset tuning outside training data) that beats the reference best mean on at least two datasets.

## How a win is checked

Rebuild the 30 resamples with tsml-eval's resampling function (stratified, random_state = resample id) from the archive's default split; check the saved predictions line up with each resample's test cases and labels; recompute mean accuracy; re-run training for two random resamples with the saved script and seed; re-download the reference CSVs and take the max mean for D.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://timeseriesclassification.com/results/ReferenceResults/classification/accuracy/>

## Sources

- <https://timeseriesclassification.com/results/ReferenceResults/classification/accuracy/>
- <https://www.timeseriesclassification.com/results.php>
- <https://timeseriesclassification.com/results/ReferenceResults/classification/estimators.txt>
- <https://github.com/time-series-machine-learning/tsml-eval>
- <https://raw.githubusercontent.com/time-series-machine-learning/tsml-eval/main/tsml_eval/utils/resampling.py>
- <https://www.cs.ucr.edu/~eamonn/time_series_data_2018/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensemble across representation families (HIVE-COTE style) but with the newest members: QUANT, MR-Hydra, RDST and WEASEL 2.0 probabilities weighted by training-set cross-validation accuracy.
- Speech-processing features for audio-derived sets (Phoneme, InsectWingbeatSound, Haptics): MFCCs, log-mel spectrogram statistics and pitch features fed to a ridge or tree classifier.
- Shape-based tricks from computer vision for outline datasets (FiftyWords, phalanx outlines): convert series to images (Gramian angular fields, recurrence plots) and use a small CNN, or use elastic shape analysis from computational anatomy.
- Semi-supervised and transductive learning from NLP: self-train on the unlabelled test series of each resample (legal, since labels are not used), which helps small-train datasets such as Worms and Beef.
- Data augmentation from audio (time warping, window slicing, mixup) for the deep models when training sets are tiny.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Default-split cherry-picking: beating the best on one split is easy noise; the record is the 30-resample mean.
- Resampling mismatch: using sklearn's train_test_split instead of tsml-eval's stratified resampler gives different resamples and is not comparable.
- Test-set leakage through z-normalisation or feature scaling fitted on train plus test is acceptable only per-series (instance-wise); fitting scalers on test labels or tuning on test accuracy is not.
- Newer published results (papers after the reference upload) may already beat the hosted maximum; the novelty check must search the literature for D, and a claim must also beat any credible published 30-resample mean for D.
- Variable-length and missing-value datasets have '_eq'/'_nmv' processed versions in the reference files; use the same version.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/ucr-tsc-beat-reference-30-resample-best.md
```

Already set up? Say `run V3R1T4S on ucr-tsc-beat-reference-30-resample-best`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ucr-tsc-beat-reference-30-resample-best`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
