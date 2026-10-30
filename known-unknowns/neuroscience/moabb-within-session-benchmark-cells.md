# MOABB EEG-BCI benchmark: one pipeline that beats the published best within-session score on at least three datasets of a paradigm table

🧠 **Neuroscience** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours per dataset (MOABB downloads each public dataset itself; Riemannian pipelines run on a CPU, deep pipelines faster on a GPU) · open as of 2026-10-30

## The problem

MOABB (Mother of All BCI Benchmarks; Chevallier, Carrara, Aristimunha, Guetschel, Sedlar, Lopes, Velut, Khazem, Moreau, 'The largest EEG-based BCI reproducibility study for open science', arXiv:2404.15319) maintains a results page of 30 pipelines on open EEG datasets. It uses within-session cross-validation per subject and session, ROC-AUC (x100) for two-class and accuracy for multiclass, as the mean over subject-session pairs. There are paradigm tables for motor imagery left vs right hand (10 datasets), right hand vs feet (9), all classes (6), SSVEP (7) and P300/ERP (15). Some best left-vs-right values: BNCI2014_001 91.71 and BNCI2014_004 82.67 (ACM+TS+SVM, augmented covariance, Carrara and Papadopoulo); Cho2017 76.23, Lee2019_MI 84.74 and Weibo2014 85.29 (TS+EL); PhysionetMI 68.46 (FgMDM); Shin2017A 72.30 (CSP+LDA); Zhou2016 95.65 (ShallowConvNet). The low cells (PhysionetMI, Shin2017A, Cho2017) and the SSVEP table leave clear room. On SSVEP, MAMEM2 tops out at 39.36 and MAMEM3 at 42.10 (SSVEP_TS+LR), and the listed TRCA and CCA pipelines score near chance on several datasets.

## What counts as a win

One pipeline with one fixed set of hyperparameters (or a hyperparameter search nested inside MOABB's training folds), evaluated with MOABB's WithinSessionEvaluation and the settings behind the results page: same datasets, subjects, sessions and metric, with the paradigm parameters (epoch window, filter band, classes) of the benchmark described in arXiv:2404.15319 and its benchmark pipeline configs in the MOABB repository; the page itself states only the evaluation and the metric. Its mean score must be STRICTLY HIGHER (direction: max) than the best pipeline on the live results page (re-fetched immediately before claiming), by at least 1.0 point, on at least three datasets of the same paradigm table. It must also beat any within-session MOABB-protocol value for those datasets found by the NOVELTY check.

## Partial wins

- **p1:** The same pipeline rule, but on one dataset cell of any paradigm table: strictly above the page's best by at least 1.0 point.
- **p2:** On the SSVEP table, strictly beat the page's best on any two of MAMEM1, MAMEM2 and MAMEM3 by at least 2.0 points each.

## How a win is checked

The skeptic installs the current MOABB release (recording its version), runs the submitted sklearn-compatible pipeline through WithinSessionEvaluation on the claimed datasets with the paradigm parameters of the paper's benchmark (arXiv:2404.15319 and the MOABB benchmark configs), confirms a listed pipeline reproduces its page value on one claimed dataset, compares the per-dataset means with the page, and checks that any tuning is nested inside training folds. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://moabb.neurotechx.com/docs/paper_results.html>

## Sources

- <https://moabb.neurotechx.com/docs/paper_results.html>
- <https://arxiv.org/abs/2404.15319>
- <https://github.com/NeuroTechX/moabb>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Riemannian tangent-space pipelines dominate the motor-imagery tables. Filter-bank or augmented covariances with data-driven frequency bands, and Riemannian alignment across sessions, are cheap to try.
- For SSVEP, the table's SSVEP_TRCA and SSVEP_CCA rows score near chance on several datasets (TRCA 2.79 on Wang2016, 24.84 on Kalunga2016). A correctly configured TRCA or ensemble TRCA, with filter banks and the right stimulus frequencies and window, is the natural first try.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Hyperparameter search outside the CV folds (on the full session) inflates within-session scores. Nest it.
- Scores averaged over a different subject subset, or with cross-session evaluation, are not comparable with the table.
- Some datasets are large (Lee2019, Cho2017), and the first download is the slow step.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/neuroscience/moabb-within-session-benchmark-cells.md
```

Already set up? Say `run V3R1T4S on moabb-within-session-benchmark-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `moabb-within-session-benchmark-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
