# ZAPBench whole-brain zebrafish activity forecasting: beat the best released long-context (C=256) test MAE at every horizon

🧠 **Neuroscience** · standard · tractability ★★★☆☆ · compute: laptop-days (trace-based models use the released ~70k-neuron traces, a few GB; the paper's trace models take about 2 h on one A100, so CPU-only is slow; video models need a cluster) · open as of 2026-10-30

## The problem

ZAPBench (Lueckmann, Immer, Chen, Li, Petkova, Iyer, ..., Engert, Lichtman, Ahrens, Januszewski, Jain; ICLR 2025, arXiv:2503.02618) asks for forecasts of the calcium activity of about 71,700 segmented neurons across a whole larval zebrafish brain, 32 steps (about 30 s) ahead, from 4 or 256 steps of context. The data is CC-BY on the public zapbench-release bucket. Each of 9 stimulus conditions is split 70/10/20 in time into train/val/test, and the 'taxis' condition is held out entirely. The metric is MAE averaged over neurons and test windows, per horizon step. The project site's chart data gives the per-condition test MAE of every baseline for each of 3 seeds. Averaging over the 8 non-held-out conditions and the 3 seeds, the best released values come from the volumetric-video UNet (Immer et al., arXiv:2503.00073) at horizons 1/4/8/16/32. Short context: 0.01812, 0.02204, 0.02486, 0.02735, 0.02921. Long context: 0.01852, 0.02131, 0.02309, 0.02469, 0.02584. At long context the trace-based models are within 1-2% of it: time-mix 0.01891 at 1 step, tsmixer 0.02477 at 16, tide 0.02585 at 32. At short context and 32 steps, the stimulus-conditioned mean (0.03021) beats every trace model. The site still lists only the paper's initial baselines, but the short-context bar has moved outside it. Google's ERA tree-search system (Aygün et al., arXiv:2509.06503, 2025) reports C=4 trace models that beat every baseline, including the video UNet, at multi-step horizons. A separate ERA model leads at 1 step with 0.0176 against the UNet's 0.0182, as quoted in Aster (arXiv:2602.07040). ERA's other per-horizon values are given only in a figure. No published result beating the UNet at long context (C=256) has been found.

## What counts as a win

Test-set forecasts at long context (C=256) for the 8 non-held-out conditions, from a model trained on the official train split (with model selection on validation only). The skeptic computes their grand-average MAE with the zapbench evaluation code (as in colabs/train_and_evaluate.ipynb), averaged over the 8 conditions and over 3 training seeds. It must be STRICTLY LOWER (direction: min) than the best released long-context method at EACH of the horizons 1, 4, 8, 16 and 32 (0.01852, 0.02131, 0.02309, 0.02469, 0.02584 on 2026-10-30, re-fetched from the project site's chart data immediately before claiming). It must also be lower than any long-context value for the same protocol found by the NOVELTY check.

## Partial wins

- **p1:** Strictly lower 3-seed grand-average test MAE than the best released method at one of the five long-context (C=256) horizon cells listed above, by at least 0.5% relative.
- **p2:** A model whose only inputs are the released traces (plus the stimulus covariates) and that beats the video UNet's long-context 1-step value of 0.01852 by at least 0.5% relative.
- **p3:** On the held-out taxis condition (never trained on), a strictly lower 3-seed MAE than every released method at any one horizon for either context.
- **p4:** At short context (C=4) and 1 step, a 3-seed grand-average test MAE over the 8 conditions strictly below 0.0175, beating both the UNet's 0.01812 and ERA's reported 0.0176 (arXiv:2509.06503).

## How a win is checked

The skeptic downloads the traces from gs://zapbench-release/volumes/20240930/traces, retrains the submitted model for the declared seeds (or evaluates the released checkpoints), computes per-condition per-step MAE with the zapbench package, and compares it with the site's chart JSON (storage.googleapis.com/zapbench-release/figures/20250131/fluroglancer/*_mae.json). Hours for trace models.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://zapbench-release.storage.googleapis.com/landing.html>

## Sources

- <https://github.com/google-research/zapbench>
- <https://zapbench-release.storage.googleapis.com/landing.html>
- <https://arxiv.org/abs/2503.02618>
- <https://arxiv.org/abs/2503.00073>
- <https://arxiv.org/abs/2509.06503>
- <http://zapbench-release.storage.googleapis.com/volumes/README.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- At C=4, almost half of the paper's runs failed to beat the naive stimulus baseline at 32 steps. Blending a learned model with the stimulus-conditioned mean as the horizon grows is an obvious first step.
- Neuron embeddings or population conditioning (as in POCO, arXiv:2506.14957) let a univariate forecaster share information across 70k neurons cheaply.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The released numbers are per-condition means over 3 seeds; a single lucky seed does not count.
- The taxis condition is excluded from the grand average and must never be used for training.
- The site's chart data gives only horizons 1, 4, 8, 16 and 32; compare at exactly those steps.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/neuroscience/zapbench-whole-brain-forecast-mae.md
```

Already set up? Say `run V3R1T4S on zapbench-whole-brain-forecast-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `zapbench-whole-brain-forecast-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
