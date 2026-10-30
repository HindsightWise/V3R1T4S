# SAGE global species distribution benchmark: beat the best overall test AUROC (85.9, random forest) on sPlotOpen presence-absence plots

🐦 **Ecology and bioacoustics** · standard · tractability ★★☆☆☆ · compute: laptop-days (3.8 GB benchmark tar plus 10 GB of GBIF presence-only records; the paper's multi-species DeepSDM trains in about 17 GPU-minutes) · open as of 2026-10-30

## The problem

SAGE (Arens, van Tiel, Zbinden, Robert and colleagues; arXiv 2609.31082, Sept 2026; data on Zenodo 21297133, code at github.com/earens/sage-sdm-benchmark) is a sampling-aware global benchmark. Models are trained on GBIF presence-only records for 5,771 plant species and evaluated on sPlotOpen presence-absence vegetation plots. The plots are split 20% validation and 80% test, stratified so that each species keeps at least 20 test occurrences. The headline score is the mean per-species AUROC on the test plots, also reported in four quadrants of sampling effort (sparse/dense) by relative prevalence (infrequent/frequent). The paper's Table 2, mirrored on the SAGE results page (fetched 2026-10-30), lists overall AUROC as a mean over 5 seeds: RF 85.9, the tuned multi-species DeepSDM (+loss) 85.8, BRT 85.2, MaxEnt 84.5, GLM 84.0, GAM 83.8. The quadrant bests are sparse-infrequent 86.6 (RF), sparse-frequent 84.3 (RF), dense-infrequent 87.9 (DeepSDM) and dense-frequent 85.0 (RF). AUPRG values are in the paper's Appendix D.2. The maintainers add new models to the public table on request; the bank never submits.

## What counts as a win

Per-species predictions on every SAGE test plot from a model trained only on the released SAGE training data (GBIF presence-only records, pseudo-absences and predictors from the Zenodo record), scored with the official SAGE evaluation code. Validation plots may be used for model selection; test plots never. The overall mean per-species test AUROC over 5 seeds must be STRICTLY GREATER (direction: max) than the best overall AUROC on https://earens.github.io/sage/results.html, re-fetched live immediately before claiming (85.9 on 2026-10-30), by at least 0.2 points. No quadrant may fall more than 0.5 points below its best listed value. The score must also beat any overall SAGE test AUROC that the NOVELTY skeptic finds in a later paper. Deliverables: code, seeds, predictions and the species_metrics.csv that the official code writes.

## Partial wins

- **p1:** Beat the best listed value in any one of the four sampling-effort/prevalence quadrants by at least 0.3 points (5-seed mean) while keeping overall test AUROC at or above 85.5.
- **p2:** Overall test AUPRG strictly above 86.9 (Random Forest, the best overall value in the paper's Appendix D.2 Table 10), aggregated as SAGE does (median over species within each seed, then mean over 5 seeds, official code), with overall AUROC at or above 85.5.

## How a win is checked

The skeptic downloads the Zenodo record and checks SHA256SUMS. They recompute species_metrics.csv from the saved predictions with the official evaluation code, then recompute the overall and quadrant means. They re-run one seed and confirm from the code that test plots enter only the scoring step.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://earens.github.io/sage/results.html>

## Sources

- <https://arxiv.org/abs/2609.31082>
- <https://earens.github.io/sage/results.html>
- <https://doi.org/10.5281/zenodo.21297133>
- <https://github.com/earens/sage-sdm-benchmark>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensembles of the RF and the tuned DeepSDM, which win different quadrants.
- Cross-domain import (recommender systems): treat species-by-site as an implicit-feedback matrix with exposure (sampling effort) modelling.
- Effort-aware pseudo-absence weighting learned on the validation plots.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The validation and test plots come from the same sPlotOpen pool; tuning on test, or reporting the validation split as test, is invalid.
- Using sPlotOpen plots (any split) as training presences or absences leaks the evaluation data.
- GBIF snapshots change over time; train on the released record, not a fresh GBIF download.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/sage-global-sdm-test-auroc.md
```

Already set up? Say `run V3R1T4S on sage-global-sdm-test-auroc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sage-global-sdm-test-auroc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
