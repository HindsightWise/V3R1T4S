# SPOCK orbital-stability benchmark (Thadhani et al. 2025 cleaned data): beat SPOCK 2.0's holdout AUC for 10^9-orbit stability of compact three-planet systems

🪐 **Planets and moons** · standard · tractability ★★★☆☆ · compute: laptop-days (labels and initial conditions are a 33 MB Zenodo zip; short REBOUND integrations of ~1.3e5 systems take CPU-hours to a day; the 10^9-orbit labels are supplied) · open as of 2026-10-30

## The problem

SPOCK (Tamayo et al. 2020, PNAS 117, 18194, arXiv:2007.06521) predicts whether a compact three-planet system survives 10^9 orbits from features of a short N-body integration; Cranmer et al. 2021 (PNAS, arXiv:2101.04117) added a Bayesian neural-network instability-time regressor (holdout RMSE 1.02 dex; theoretical chaos limit about 0.43 dex). Thadhani, Ba, Rein & Tamayo 2025 (SPOCK 2.0, RNAAS 9, 27, doi:10.3847/2515-5172/adb150) found 10,984 duplicated resonant systems and 124 planet losses mislabelled stable, and released a cleaned set on Zenodo 14327471 (resonant 102,497 and random 24,941 rows with instability_time, shadow_instability_time and Stable labels, plus REBOUND initial conditions; the note quotes 127,428 systems). Training on the first 80% of the resonant rows and testing on the rest, with test systems that go unstable during the short integration excluded, they report AUC 0.9430 for the original 10^4-orbit features and 0.9502 for SPOCK 2.0 (integrating to each system's fastest secular timescale and adding it as a feature); the repository's train_spock.ipynb gets 0.9494 for the released model. The shadow-trajectory labels agree with the primary labels for 98.6% of the last 20% of resonant rows (computed 2026-10-30), so chaos leaves room above 0.95. The SPOCK changelog (v2.1.0; repository pushed 2026-09-23) lists no later stability classifier, and no 2024-2026 work citing SPOCK in OpenAlex or on arXiv reports a higher AUC on this data. Open task: a stability predictor with a strictly higher holdout AUC than SPOCK 2.0 under the same short-integration budget.

## What counts as a win

A saved bundle (frozen training code, trained model, per-system probabilities). Test set: rows 81,997-102,496 (0-based, file order; the last 20,500 rows) of dataset/resonant/sim_labels.csv in Zenodo record 14327471, minus the systems that go unstable during the short integration of the latest released SPOCK FeatureClassifier (InitialStable = False from its generate_features, run by the skeptic), as in Thadhani et al. 2025 section 2; label = column Stable. Training and tuning use only rows 0-81,996 (the rows the released SPOCK model was trained on); the random dataset is never used for training. Per-system inputs: the initial conditions plus at most one N-body integration no longer than max(10^4 innermost orbits, the system's fastest secular timescale as defined in Thadhani et al. 2025); the instability_time and shadow columns are never inputs. Win: test ROC AUC strictly greater (direction: max) than both 0.9502 and the AUC the skeptic gets from the latest released SPOCK FeatureClassifier on the identical rows, with the paired-bootstrap (2,000 resamples) 95% interval of the difference above zero; and on the random-dataset rows with instability_time >= 1e4 (17,463 systems) an AUC no more than 0.005 below SPOCK's on the same rows. Re-fetch the Zenodo record and the SPOCK changelog immediately before claiming, and beat any value on this split in later papers (ADS/arXiv search for 'SPOCK' and 'Thadhani', last 24 months).

## Partial wins

- **p1:** Reproduce SPOCK 2.0 on the defined test set: an AUC within 0.005 of 0.9502 from the bundle's own feature pipeline, trained only on rows 0-81,996 (validates the split and features).
- **p2:** Instability-time regression: on defined test-set rows with instability_time < 9.98e8, a log10-time RMSE strictly below that of the released SPOCK DeepRegressor (Cranmer et al. 2021) median predictions, recomputed by the skeptic on the same rows, under the same input budget.
- **p3:** An AUC >= 0.9502 on the defined test set with a single N-body integration of at most 10^3 innermost orbits per system (ten times shorter than SPOCK's minimum).
- **p4:** On the random-dataset rows with instability_time >= 1e4, an AUC strictly greater than the skeptic's recomputed SPOCK 2.x AUC on the same rows, while training only on resonant rows 0-81,996.

## How a win is checked

Skeptic downloads Zenodo 14327471, checks the CSV hash and row split, reruns the frozen training on rows 0-81,996 with a new seed, recomputes the test AUC and paired bootstrap, and installs the latest SPOCK release to score the identical rows. A few CPU-hours to a day.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/dtamayo/spock/blob/master/changelog.md>

## Sources

- <https://zenodo.org/records/14327471>
- <https://doi.org/10.3847/2515-5172/adb150>
- <https://github.com/dtamayo/spock>
- <https://arxiv.org/abs/2007.06521>
- <https://arxiv.org/abs/2101.04117>
- <https://zenodo.org/record/3723292>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: gradient boosting on SPOCK features plus analytic resonance-overlap and secular quantities (Tamayo et al. 2021 AnalyticalClassifier, Yang & Tamayo 2024 secular timescales).
- Sequence models (1D CNN or transformer) on the short-integration orbital-element time series, as in Cranmer et al. 2021, trained as classifiers with calibrated outputs.
- Cross-domain import (survival analysis): treat instability time as a right-censored survival target and train a discrete-time hazard model; the censored-at-1e9 structure is exactly survival data.
- Cross-domain import (weather ensembles): run two shadow short integrations per system and use their divergence (a finite-time Lyapunov proxy) as a feature.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The original 2020 Zenodo training set contains the duplicates removed in 2025; mixing it in leaks test systems into training.
- generate_FC_data.py joins features to sim_labels.csv in file order and train_spock.ipynb takes the first 80% as training: keep that order, or the split no longer matches the released model's.
- Scoring all 20,500 rows without removing the systems that go unstable during SPOCK's short integration inflates AUC (those systems are trivially unstable) and is not comparable with 0.9502.
- Different REBOUND versions give different chaotic trajectories; record the version and integrator settings in the bundle.
- Integrating longer than the allowed budget makes the problem easier and is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/spock-stability-auc-cleaned-dataset.md
```

Already set up? Say `run V3R1T4S on spock-stability-auc-cleaned-dataset`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `spock-stability-auc-cleaned-dataset`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
