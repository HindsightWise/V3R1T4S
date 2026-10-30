# SWOT correlated-error calibration data challenge 2022c (Gulf Stream OSSE): beat the leaderboard's best on-swath RMSE

🌍 **Earth and sky** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (inputs tarball 33 MB, nadirs 18 MB, maps 33 MB on the MEOM OPeNDAP server) · open as of 2026-10-30

## The problem

The 2022c SWOT error calibration data challenge (designed by Datlas with IGE, CLS and IMT-Atlantique; repository by S. Metref; funded by CNRS, CNES and the Copernicus Marine SLICING project) is an OSSE in a 10 x 10 degree Gulf Stream box. The true ocean is the NATL60 simulation. The SWOT simulator (Gaultier, Ubelmann and Fu 2016) adds spatially correlated errors to the swaths; the README names the roll and baseline-dilation errors. The task is to remove the correlated errors from cycle 13 (270 passes); all other cycles may be used to tune or train. The README holds three leaderboards. (1) On the SWOT swath, mu(RMSE) and lambda(SNR1) for SSH, geostrophic current and relative vorticity. CalCNN (Febvre, Ubelmann, Le Sommer, Fablet, arXiv:2302.04497): 0.014 / 0.076 / 0.212, current lambda 30.6 km. Projmethod: 0.037 / 0.115 / 0.271, vorticity lambda 30.6 km. CER-method: 0.074 / 0.219 / 0.261. (2) On nadir crossings: CalCNN 0.0134 m, against 0.013 for the interpolated true SWOT data. (3) On an independent nadir (Cryosat): Projmethod 0.033 m, CER 0.076; the CalCNN cell is still '?'. This challenge is distinct from the 2022a KaRIn random-noise filtering challenge, which is an existing bank entry. It is open as of 2026-10-30: the README leaderboard has not changed since 2023, and the data are live on the MEOM OPeNDAP server.

## What counts as a win

A calibrated cycle-13 SWOT NetCDF produced by saved, runnable code that never reads cycle-13 ssh_true (training or tuning on other cycles only, as the README allows). Scored with the repository's unmodified swath evaluation notebook, its SSH mu(RMSE) must be strictly lower (direction: min) than the best swath SSH entry in the README leaderboard at https://github.com/ocean-data-challenges/2022c_SWOT_error_calibration_GS (re-fetched before claiming; 0.014 for CalCNN on 2026-10-30) at the leaderboard's 3-decimal rounding, i.e. at most 0.013, with geostrophic-current mu(RMSE) no worse than 0.076 and relative-vorticity mu(RMSE) no worse than 0.212. It must also beat any number for this setup in a paper from the last 24 months found by a fresh search.

## Partial wins

- **p1:** Swath relative-vorticity mu(RMSE) strictly below 0.212, with SSH mu(RMSE) no worse than 0.014.
- **p2:** A method with no trained neural network (projection, regression or optimal-interpolation class) beating Projmethod on all three swath mu(RMSE) values (0.037, 0.115, 0.271).
- **p3:** Independent-nadir (Cryosat) SSH RMSE strictly below 0.033 m (Projmethod), from the repository's unmodified independent-nadir notebook.

## How a win is checked

Skeptic downloads the three tarballs from the MEOM OPeNDAP server, reruns the method in a sandbox where cycle-13 ssh_true has been deleted from the input files (the output must be identical), runs the unmodified evaluation notebooks and compares with the README leaderboards. About 1 hour on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/ocean-data-challenges/2022c_SWOT_error_calibration_GS>

## Sources

- <https://github.com/ocean-data-challenges/2022c_SWOT_error_calibration_GS>
- <https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2022c_SWOT_error_calibration_GS/catalog.html>
- <https://arxiv.org/abs/2302.04497>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: fit the known error modes (roll as linear in cross-track, phase per half-swath, baseline dilation as quadratic) along track with smoothness priors, then hand the residual to a small CNN.
- Use the crossing nadir tracks inside the swath as anchors (cross-calibration), as the operational SWOT XCal does.
- Cross-domain import (MRI bias-field correction): estimate a smooth multiplicative or additive field with spline regularisation, separating it from the ocean signal by spectral scale.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- ssh_true for cycle 13 ships in the same files as ssh_err; any read of it (scaling, early stopping, model selection) voids the result.
- The data URL in the README (ocean-data-challenges/2022c...) returns 404; the live copy is under MEOM/OCEAN_DATA_CHALLENGES/2022c_SWOT_error_calibration_GS.
- Leaderboard values are rounded; a tie at 3 decimals is not a win.
- Check what the 33 MB inputs tarball contains (cycle 13 only or also training cycles) before planning a learned method; the NATL60 maps tarball can provide training pseudo-swaths.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/swot-error-calibration-2022c-gulf-stream.md
```

Already set up? Say `run V3R1T4S on swot-error-calibration-2022c-gulf-stream`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `swot-error-calibration-2022c-gulf-stream`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
