# Matbench v0.1: beat the per-task leaderboard on a small-data task (steels, jdft2d, expt_gap, glass) with CPU-only models

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Matbench v0.1 (Alexander Dunn, Qi Wang, Alex Ganose, Daniel Dopp and Anubhav Jain, npj Comput. Mater. 6, 138, 2020) scores materials-property models by nested 5-fold cross-validation with fixed folds. Its per-task leaderboards, which include specialised algorithms that the general-purpose front-page table leaves out, list for the four smallest tasks: matbench_steels (312 compositions, yield strength) MAE 79.9468 ± 13.5883 MPa by TPOT-Mat, then AutoML-Mat 82.3043 and MODNet v0.1.12 87.7627; matbench_jdft2d (636 structures, exfoliation energy) MAE 33.1918 ± 7.3428 meV/atom by MODNet v0.1.12; matbench_expt_gap (4,604 compositions) MAE 0.2865 ± 0.0083 eV by Darwin; matbench_glass (5,680 compositions, classification) 0.9603 ± 0.0075 by MODNet v0.1.12. The glass page warns that its listed 'ROC-AUC' values were computed on predictions thresholded at 0.5, so they equal balanced accuracy. These tasks are trainable on a laptop CPU. The six medium-size tasks are a separate entry (matbench-medium-structure-tasks-cpu).

## What counts as a win

For one of matbench_steels, matbench_jdft2d, matbench_expt_gap or matbench_glass: saved code and per-fold predictions that the skeptic re-runs with the official matbench package (MatbenchBenchmark v0.1, the fixed folds, hyperparameters chosen only inside training folds, no test leakage). The mean score must be STRICTLY BETTER than the best entry on that task's live per-task leaderboard (https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_<task>/), re-fetched immediately before claiming. Better means: for the three regression tasks, mean MAE lower (direction: min); for matbench_glass, mean balanced accuracy of predictions thresholded at 0.5 higher (direction: max), which is the quantity the page's 'rocauc' column actually reports. The margin must exceed the larger of 2% relative and the best entry's fold standard deviation divided by sqrt(5). The claim must also beat every Matbench-v0.1-protocol score for that task the skeptic finds published.

## Partial wins

- **p1:** Beat the per-task leaderboard best on matbench_steels, under the full-win protocol and margin, with a model of under 10,000 learned parameters or a closed-form symbolic formula (e.g. SISSO-like).
- **p2:** One fixed method (no per-task tuning outside training folds) that, under the full-win protocol, scores better than every listed entry except the AutoML pipelines (TPOT-Mat, AutoML-Mat, AMMExpress v2020) on two of the four tasks.
- **p3:** A re-run of the top per-task entry's published code and folds that reproduces a mean score differing from the posted score by more than 2 posted fold standard deviations, with all outputs saved.

## How a win is checked

Skeptic installs matbench, runs the saved script with the official benchmark object (record per fold), recomputes the task's metric (MAE, or balanced accuracy at a 0.5 threshold for glass) from the saved per-fold predictions, compares it with the live per-task leaderboard, and audits that only training-fold data was used for tuning. 10-60 minutes on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://matbench.materialsproject.org/>

## Sources

- <https://matbench.materialsproject.org/>
- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_steels/>
- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_jdft2d/>
- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_expt_gap/>
- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_glass/>
- <https://raw.githubusercontent.com/materialsproject/matbench/main/benchmarks/matbench_v0.1_rf/results.json.gz>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: Magpie/matminer features + gradient boosting / TabPFN-style ensembles with careful inner-fold tuning.
- Conventional: metallurgy-informed features for steels (solid-solution strengthening terms, carbon equivalent, element pair interactions).
- Cross-domain import (NLP): pretrained element/composition embeddings (mat2vec) or LLM text embeddings of formulas as features.
- Cross-domain import (physics-informed ML / symbolic regression): PySR / SISSO formulae as low-variance models for 300-sample tasks.
- Cross-domain import (genomics small-n statistics): Gaussian-process regression with composition kernels and empirical-Bayes hyper-priors.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Test leakage via hyper-parameter tuning on all folds or via deduplicated-composition overlaps; only the official nested protocol counts.
- Pretrained models can leak labels: jdft2d comes from JARVIS-DFT, so models pretrained on JARVIS data are suspect there; audit the pretraining data of any pretrained component.
- Leaderboard differences within fold std are noise; the margin rule is there for that reason. For glass, the page's rocauc column is balanced accuracy, so compare like with like.
- Submitting to the leaderboard needs a GitHub PR - do not submit; claim the verified local result.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/matbench-small-data-tasks.md
```

Already set up? Say `run V3R1T4S on matbench-small-data-tasks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `matbench-small-data-tasks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
