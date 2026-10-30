# Glacier point mass balance in Norway: beat the Mass Balance Machine RMSE on the 14 withheld test glaciers

🌍 **Earth and sky** · standard · tractability ★★★★☆ · compute: laptop-minutes to laptop-hours (CSVs of about 20 MB with ERA5-Land and topographic features already joined; gradient boosting trains in minutes on CPU) · open as of 2026-10-30

## The problem

Sjursen, Bolibar, van der Meer, Andreassen, Biesheuvel, Dunse, Huss, Maussion, Rounce and Tober (The Cryosphere 19:5801, 2025, 'Machine learning improves seasonal mass balance prediction for unmonitored glaciers') trained the Mass Balance Machine (MBM, XGBoost on monthly ERA5-Land climate and OGGM topographic features) on NVE stake measurements (Elvehoy et al. 2025, doi:10.58059/sjse-6w92) from 32 glaciers in mainland Norway, 1962-2021. All measurements from 14 glaciers (RGI60-08.00434, .00449, .01013, .01026, .01258, .01286, .01484, .01598, .02384, .02650, .02916, .02918, .02920, .02969) were withheld for testing. The repository github.com/khsjursen/ML_MB_Norway (Zenodo 10.5281/zenodo.15021796) ships the feature-joined training and test CSVs, so no Copernicus account is needed. MBM test scores (notebook 3.1.1 output): annual Ba RMSE 1.00 m w.e. (n=1065), winter Bw 0.59 (n=999), summer Bs 0.70 (n=1028). On seasonal balances MBM beat GloGEM, PyGEM and OGGM. On annual point balances over the 1980-2019 common period the paper gives GloGEM 0.91 and OGGM 0.93 against MBM's 0.97, but those models are calibrated on each glacier's 2000-2019 geodetic balance, test glaciers included, so they are not independent of the test set. As of 2026-10-30 no lower RMSE on this split by a model without test-glacier observations has been found (the successor code is ODINN-SciML/MassBalanceMachine). Open task: lower test-glacier RMSE.

## What counts as a win

A saved, runnable model (code, fixed seeds) trained only on rows from the 18 training glaciers in the shipped CSVs (hyperparameters chosen by cross-validation within those glaciers only). Inputs are only the shipped features or other public static data (DEM, RGI outlines), never any mass-balance, geodetic or glacier-wide observation of a test glacier. It predicts every test-glacier point balance, and its RMSE against the observed values over the same 1065 annual, 999 winter and 1028 summer measurements must be strictly lower (direction: min), at 2-decimal rounding, than MBM's for all three: Ba <= 0.99, Bw <= 0.58 and Bs <= 0.69 m w.e. The RMSE is computed by an independent script and checked against MBM's numbers reproduced from the repository notebook. The result must also beat any RMSE on these same full test sets, by a model that uses no observation of a test glacier, in a paper from the last 24 months found by a fresh search. Numbers from models calibrated on test-glacier geodetic data (e.g. the paper's GloGEM 0.91 and OGGM 0.93 annual RMSE for 1980-2019) and numbers on sub-periods do not set the bar.

## Partial wins

- **p1:** Strictly lower test RMSE than MBM (2-decimal rounding) on any one of Ba (1.00), Bw (0.59) or Bs (0.70), with the other two no worse than MBM's.
- **p2:** A model of at most 20 fitted parameters (e.g. a calibrated temperature-index or linear model) with test Bw RMSE at most 0.59 m w.e.
- **p3:** Reproduce MBM's three test RMSEs within 0.01 m w.e. from the shipped CSVs with an independent re-implementation (validates the split and scorer).

## How a win is checked

Skeptic clones ML_MB_Norway, checks that the training code reads only rows whose RGIID is not among the 14 test glaciers (code read plus a run with test rows deleted from the training input), recomputes the test RMSEs with a 10-line script on the same measurement counts and compares with the notebook 3.1.1 output. Under an hour on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/khsjursen/ML_MB_Norway>

## Sources

- <https://tc.copernicus.org/articles/19/5801/2025/>
- <https://github.com/khsjursen/ML_MB_Norway>
- <https://doi.org/10.5281/zenodo.15021796>
- <https://github.com/ODINN-SciML/MassBalanceMachine>
- <https://doi.org/10.58059/sjse-6w92>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: monthly gradient boosting with glacier-group cross-validation, plus monotonic constraints (more snowfall raises Bw, warmer summers lower Bs).
- Hybrid physics-ML: a differentiable temperature-index model with a learned residual (as in GlaUnTI) to extrapolate to unseen glaciers.
- Cross-domain import (hydrology regionalisation): transfer parameters from donor catchments by similarity, as CAMELS ungauged-basin studies do.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The test CSV is in monthly format (24,913 rows); aggregate to point seasonal and annual balances exactly as MBM did and confirm the counts 1065/999/1028 before scoring.
- Random row-level cross-validation leaks stake-to-stake correlation within a glacier; split by glacier.
- NVE glacier-wide balances and Hugonnet geodetic rates in the repository cover the test glaciers; using them as inputs is leakage.
- Bw and Bs are missing for some stakes and years; compute each RMSE only over its own observed set.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/massbalancemachine-norway-test-glaciers-rmse.md
```

Already set up? Say `run V3R1T4S on massbalancemachine-norway-test-glaciers-rmse`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `massbalancemachine-norway-test-glaciers-rmse`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
