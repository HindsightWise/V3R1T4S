# AnuraSet neotropical frog calls: beat the best published test macro F1 (60.8, Mixture of Mixups) for 42-species multi-label classification

🐦 **Ecology and bioacoustics** · standard · tractability ★★★★☆ · compute: laptop-hours (11.4 GB zip of 93k 3-second clips; a 3M-parameter MobileNetV3 trains from scratch) · open as of 2026-10-30

## The problem

AnuraSet (Canas, Toro-Gomez, Sugai and colleagues, Scientific Data 10:771, 2023; Zenodo record 8342596, code at github.com/soundclim/anuraset) is 27 hours of passive-acoustic recordings from four Brazilian sites, annotated by herpetologists. The recordings are cut into 93,378 three-second windows, each labelled with the presence of any of 42 anuran species, and split into fixed train and test sets at recording level (about 2/3 and 1/3). The metric is macro F1 over the classes at threshold 0.5. The paper's best baseline is ResNet152 with macro F1 37.8 (frequent 68.4, common 56.8, rare 15.7). Moummad, Farrugia, Serizel, Froidevaux and Lostanlen (Mixture of Mixups, arXiv 2403.09598, EUSIPCO 2024; code at github.com/ilyassmoummad/Mix2) report 60.8 +/- 0.3 on the full 42-class task with a MobileNetV3-Large trained from scratch for 100 epochs (frequent 89.2, common 77.1, rare 51.8). Having no validation set, they did model validation on the test set, as the paper states, so 60.8 is an optimistic bar. Their reduced variants AnuraSet-36N (70.4) and AnuraSet-36 (74.2) drop classes and are separate tasks. An arXiv query on 2026-10-30 found no later paper reporting a higher full-task score. The iNatSounds paper reports AnuraSet mAP and mF1 (best mF1 37.0) only on the 25 species shared with iNatSounds, a different task.

## What counts as a win

A model trained only on the official AnuraSet training split, evaluated on the official test split of the full 42-class task with the F1 computation behind the 60.8 figure: per-class F1 at threshold 0.5 (torchmetrics MultilabelF1Score, average=None), macro-averaged as in Mix2's val.py, which follows the AnuraSet baseline evaluate.py. Any validation set must be carved from training recordings, never from test. The mean over at least 3 seeds must be STRICTLY GREATER (direction: max) than 60.8 by at least 0.6 points (twice the reported std). It must also beat any full-task macro F1 that the NOVELTY skeptic finds in a paper from the last 24 months. External pretraining is allowed if declared and if its corpus excludes the AnuraSet source recordings. Deliverables: code, seeds, per-seed saved test predictions and evaluation output.

## Partial wins

- **p1:** Mean macro F1 over 3 seeds above 51.8 on the rare-species group (fewer than 5k samples) of the full task, with overall macro F1 of at least 60.0.
- **p2:** Full-task macro F1 above 60.8 (3-seed mean) with a model of at most 1M parameters.

## How a win is checked

The skeptic downloads the Zenodo zip and checks the split column. They recompute macro F1 from the saved per-window test probabilities with Mix2's val.py logic: torchmetrics MultilabelF1Score(num_labels=42, average=None, threshold=0.5), then the plain mean of all 42 per-class values, so classes with no test positives score 0. They re-train one seed and confirm the score lands within 1 point. They audit that no test recording was used for selection or pretraining.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:AnuraSet+OR+abs:anuran&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://github.com/soundclim/anuraset>
- <https://zenodo.org/record/8342596>
- <https://doi.org/10.1038/s41597-023-02666-2>
- <https://arxiv.org/abs/2403.09598>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Pretrained bioacoustic encoders (Perch 2.0, BirdMAE, BEATs variants) fine-tuned with Mix2-style mixing.
- Cross-domain import (multi-label text classification): per-class threshold calibration learned on a hold-out of training recordings, and asymmetric losses for rare labels.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The paper reports results without a validation set; picking the epoch or the threshold on test inflates scores.
- Overlapping 3-second windows (1-second hop) mean a random window-level split leaks; split by recording.
- Four classes occur only in train and two only in test. Mix2's val.py averages over all 42 classes, so the train-only classes score 0 and cap the attainable macro F1. Use the same rule, not a 38- or 36-class average.
- Per-class thresholds tuned on held-out data can roughly double macro F1 (one public Perch-embedding repo reports 0.317 at 0.5 and 0.628 with tuned thresholds); such numbers are not comparable with the fixed-0.5 bar.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/anuraset-multilabel-macro-f1.md
```

Already set up? Say `run V3R1T4S on anuraset-multilabel-macro-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `anuraset-multilabel-macro-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
