# AIICE Arctic sea-ice concentration forecasting benchmark: beat every leaderboard model in a sea and scenario

🌍 **Earth and sky** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (daily 25 km OSI-SAF grids 1979-2025 as .npy files on Hugging Face; per-sea crops are small and the reference models train on CPU or a small GPU) · open as of 2026-10-30

## The problem

AIICE (ITMO NSS team; aiice-bench 1.0.3 on PyPI; github.com/ITMO-NSS-team/Aiice; data huggingface.co/datasets/ITMO-NSS/Aiice, CC-BY-4.0, built from OSI-SAF sea-ice concentration) is a fixed benchmark for spatio-temporal sea-ice concentration forecasting. Models train on 1980-01-01 to 2020-01-01 and are scored by AIICE.bench from 2020-01-01 to the end of the dataset. Seven scenarios: daily S1 (14 days in, 7 out), S2 (60 in, 30 out) and S3 (180 in, 90 out); weekly L2 (64 in, 32 out) and L4 (104 in, 52 out); monthly L1 (12 in, 6 out) and L3 (24 in, 12 out). The leaderboard (docs/assets/leaderboard.csv; results last added 2026-05-04) covers five seas (Barents, Kara, Laptev, Chukchi, Sea of Japan) with MAE, RMSE, PSNR, SSIM, IoU and binary accuracy (SIC > 15%), for baseline_mean, baseline_repeat, conv2d, conv3d, convlstm, unet, fno and FH-Mamba. Examples: Kara L1, best bin_accuracy 0.9409 (unet) and MAE 0.0658 (fno); Kara S1, bin_accuracy 0.9824 (conv3d) and MAE 0.02464 (conv2d). The leaderboard holds only these generic baselines, which leaves room for sea-ice-specific methods. The Hugging Face data keep growing: the 2026-09-21 commits added 2025-07-02 to 2026-04-18. The leaderboard values therefore match revision dfbb874191f2 (2026-05-04), whose last file is 2025-07-01.

## What counts as a win

For one scenario: a saved, runnable PyTorch model (code, fixed seeds, weights) trained only on dates from 1980-01-01 to before 2020-01-01, with data from Hugging Face ITMO-NSS/Aiice at revision dfbb874191f279de3c9833a117eb207a62e19a20. It is evaluated with aiice-bench 1.0.3 AIICE.bench using that scenario's leaderboard config from scripts/experiments/configs (seas, pre_history_len, forecast_len, step, start_date 1980-01-01, end_date 2020-01-01) on that revision's benchmark window, 2020-01-01 to 2025-07-01. The loader reads Hugging Face 'main' by default, so the only permitted change to aiice-bench is replacing 'main' with that revision hash in the resolve/tree URLs of aiice/core/huggingface.py. In each of the five seas, the model's bin_accuracy and IoU must be strictly higher and its MAE strictly lower (directions: max, max, min) than every model's value for that sea and scenario in docs/assets/leaderboard.csv (re-fetched before claiming). The model must also beat, on each of these metrics, the leaderboard's best model for that metric when the skeptic re-runs that model's repository config on the same pinned revision and window. This guards against window drift.

## Partial wins

- **p1:** The same three-metric win (bin_accuracy, IoU, MAE all better than every leaderboard model) for a single (sea, scenario) cell.
- **p2:** A single-cell win in a long-lead scenario (L1, L3, L4 or S3) with a model of under 1 M parameters trained on CPU in under 2 hours.
- **p3:** Strictly lower MAE than every leaderboard model in all five seas for one scenario, with bin_accuracy no worse than the best leaderboard value minus 0.002 in each sea.

## How a win is checked

Skeptic installs aiice-bench 1.0.3, loads Hugging Face revision dfbb874191f2, retrains or loads the model, runs AIICE.bench for the stated scenario and seas, re-runs the repository config of the leaderboard's best model on the same revision, and checks that no file dated on or after 2020-01-01 is read during training (code read plus a run with those files removed). Hours on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/ITMO-NSS-team/Aiice/blob/main/docs/assets/leaderboard.csv>

## Sources

- <https://github.com/ITMO-NSS-team/Aiice>
- <https://github.com/ITMO-NSS-team/Aiice/blob/main/docs/assets/leaderboard.csv>
- <https://huggingface.co/datasets/ITMO-NSS/Aiice>
- <https://pypi.org/project/aiice-bench/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: a U-Net or ConvLSTM with day-of-year and climatology inputs, predicting anomalies from the 1980-2019 daily climatology instead of raw SIC.
- Physics prior: damped-persistence plus trend as a baseline, with a learned residual; at monthly leads add the sea-ice-edge reemergence memory.
- Cross-domain import (video prediction): the SimVP/Earthformer families from SEVIR nowcasting, trained per sea.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The benchmark window grows as the Hugging Face dataset is updated, and aiice-bench always reads 'main'. Scores on the current data (to 2026-04) are not comparable with the CSV. Pin revision dfbb874191f279de3c9833a117eb207a62e19a20 by editing the two URLs in aiice/core/huggingface.py, and confirm the benchmark ends on 2025-07-01.
- Normalisation statistics or climatologies computed over the full series leak the test period; compute them on 1980-2019 only.
- Later revisions flag gap-filled (interpolated) days and add land_mask.npy; mixing revisions changes both the inputs and the targets.
- The Sea of Japan crop is tiny and nearly ice-free; IoU there is very noisy.
- FNO results in the CSV use seed 42 and an internal 4-year validation hold-out inside 1980-2019; copy that practice rather than validating on 2020+ data.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/aiice-arctic-sea-ice-forecast-leaderboard.md
```

Already set up? Say `run V3R1T4S on aiice-arctic-sea-ice-forecast-leaderboard`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `aiice-arctic-sea-ice-forecast-leaderboard`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
