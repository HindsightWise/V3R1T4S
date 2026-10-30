# SatBird USA-summer bird encounter rates: one model that beats every published test metric (top-10, top-30, top-k, MAE, MSE)

🐦 **Ecology and bioacoustics** · standard · tractability ★★☆☆☆ · compute: needs cluster (GPU days for Sentinel-2 patch models; tabular or embedding models run on a laptop) · open as of 2026-10-30

## The problem

SatBird (Teng, Elmustafa, Akera, Bengio, Radi Abdelwahed, Larochelle, Rolnick; NeurIPS 2023 Datasets and Benchmarks; data at satbird.github.io, code at github.com/RolnickLab/SatBird) asks for encounter rates of 670 bird species at eBird hotspots in the USA, predicted from Sentinel-2 imagery and environmental rasters. It has fixed train/validation/test splits for USA-summer, USA-winter and Kenya. The metrics are MAE, MSE, top-10, top-30 and adaptive top-k accuracy. On USA-summer test, the best published values (checked 2026-10-30) are split between two models. MiTREE (Theresa Chen and Yao-Yi Chiang, arXiv 2412.18995) has top-10 47.38%, top-30 66.61%, top-k 67.82%, MAE 2.070e-2 and MSE 0.630e-2. An MLP on AlphaEarth embeddings (Tijunaityte, van der Plas, Belaid, Knapen, Soja, Athanasiadis; arXiv 2610.23110, Oct 2026) has top-10 49.7%, top-30 61.5%, MSE 0.58e-2 and MAE 1.93e-2. MIAM reports MAE 1.94e-2. On USA-winter, MiTREE reports top-10 51.77%, top-30 70.01%, top-k 71.40%, MAE 1.621e-2 and MSE 0.430e-2. CISO (arXiv 2508.06704) uses a songbird/non-songbird split and is not comparable.

## What counts as a win

Predicted encounter-rate vectors for every USA-summer test hotspot from one model trained on the SatBird USA-summer train split (validation for selection), scored with the SatBird repository's metric code. As means over 3 seeds, the model must SIMULTANEOUSLY beat all five current bests: top-10 > 49.7%, top-30 > 66.61% and top-k > 67.82% (direction: max), and MAE < 1.93e-2 and MSE < 0.58e-2 (direction: min). It must also beat any value for the same split and metric that the NOVELTY skeptic finds in a paper from the last 24 months. Extra public inputs (for example satellite embeddings) are allowed if declared and if they carry no eBird checklist information from test hotspots. Deliverables: code, seeds, predictions and metric output.

## Partial wins

- **p1:** On USA-summer test, top-30 above 66.61% and top-k above 67.82%, with MAE no worse than 2.070e-2 (3-seed mean).
- **p2:** On USA-winter test, one model that beats MiTREE's top-10 51.77%, top-30 70.01%, top-k 71.40% and MAE 1.621e-2, with MSE no worse than 0.430e-2 (3-seed mean). The SatBird paper's ResNet-18 winter rows report MSE only as 0.4e-2 (rounded), so MSE is not part of this win.

## How a win is checked

The skeptic downloads the SatBird release and recomputes the five metrics from the saved predictions with the repository code. They re-run one seed and check that no test-hotspot target vector, and no eBird data from test hotspots, entered training or feature construction.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:SatBird&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://satbird.github.io/>
- <https://github.com/RolnickLab/SatBird>
- <https://arxiv.org/abs/2311.00936>
- <https://arxiv.org/abs/2412.18995>
- <https://arxiv.org/abs/2610.23110>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fuse AlphaEarth-style embeddings (strong on MAE, MSE and top-10) with MiTREE-style image encoders (strong on top-30 and top-k).
- Cross-domain import (recommender systems): species co-occurrence priors and ranking losses that target top-k directly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Spatial autocorrelation: features built from neighbouring hotspots' eBird data can leak test targets.
- Papers quote MiTREE slightly differently (47.3/66.5 vs 47.38/66.61); use the higher values.
- MSE and MAE are reported in units of 1e-2; mixing units creates false records.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/satbird-usa-encounter-rates.md
```

Already set up? Say `run V3R1T4S on satbird-usa-encounter-rates`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `satbird-usa-encounter-rates`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
