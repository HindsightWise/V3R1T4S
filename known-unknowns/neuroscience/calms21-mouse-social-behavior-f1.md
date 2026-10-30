# CalMS21 mouse social behaviour classification: beat the best test F1 on Task 1 (0.878), Task 2 (0.809) or Task 3 (0.363)

🧠 **Neuroscience** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (Task 1 pose JSON 457 MB, Task 3 556 MB; frame-level classifiers on keypoints train on a CPU) · open as of 2026-10-30

## The problem

CalMS21 (Jennifer J. Sun, Tomomi Karigo, Dipam Chakraborty, Sharada P. Mohanty, Benjamin Wild, Quan Sun, Chen Chen, David J. Anderson, Pietro Perona, Yisong Yue, Ann Kennedy; NeurIPS 2021 Datasets and Benchmarks, arXiv:2104.02710) contains MARS pose tracks of resident-intruder mouse pairs with frame-level expert annotations. It defines three tasks. Task 1 classifies attack, investigation and mount. Task 2 transfers to five other annotators' styles. Task 3 learns seven new behaviours from few examples. Train and test sets are split by animal identity, and both are public on CaltechDATA (record s0vdx-0k302, with test annotations, CC-BY), with the instruction to develop on train only and report test results over several seeds. The paper's results (mean and SD over 5 runs) put the MABe 2021 challenge top-1 at class-averaged F1 0.864 and MAP 0.914 on Task 1, F1 0.809 and MAP 0.857 on Task 2, and F1 0.319 (0.363 with threshold tuning) and MAP 0.352 on Task 3. The Task 1 and 2 entry is by Benjamin Wild (FU Berlin). The baselines are 0.793, 0.754 and 0.338. Task 1 has since moved. Weihan Li, Jingyang Ke, Qinheng Pu, Yule Wang, Chengrui Li and Anqi Wu (arXiv:2603.07279, v2 Oct 2026) report a 5-seed macro F1 of 0.878 on the official Task 1 test split, from the official MARS features fed to a BiGRU classifier (their ResiFuse 0.865, VideoPrism features 0.849; inputs subsampled 4x in time, one 3.2 s clip dropped). SciVid (Yana Hasson, Pauline Luc et al., Google DeepMind, arXiv:2507.03578) reports a Task 1 test mAP of 0.924 with a frozen V-JEPA-H video backbone (VideoPrism-g 0.915). We found no later Task 2 or Task 3 values. Task 3 remains far from solved.

## What counts as a win

For one task, frame-level predictions on the official CalMS21 test set from a model trained (and threshold-tuned) only on that task's training data plus the public unlabeled CalMS21 videos, frozen before test labels are read. The skeptic computes the class-averaged F1 over the task's behaviours (excluding 'other', annotator-averaged for Task 2) as defined in the paper and the official baseline code, as the mean over 5 training seeds. It must be STRICTLY HIGHER (direction: max) than the best value above for that task (Task 1 0.878, the MARS-feature baseline of arXiv:2603.07279; Task 2 0.809; Task 3 0.363) and than any test value for the same task found by the NOVELTY check, by at least 0.01.

## Partial wins

- **p1:** Task 3: a 5-seed mean class-averaged F1 strictly above 0.363 by at least 0.01 without per-behaviour threshold tuning on test.
- **p2:** Task 1 or 2: a 5-seed mean MAP strictly above the best published test MAP for that task (Task 1: 0.924, SciVid's frozen V-JEPA-H readout, arXiv:2507.03578; Task 2: 0.857, MABe 2021 top-1) by at least 0.005.
- **p3:** Task 3: strictly beat the top-1 per-behaviour F1 on at least 4 of the 7 new behaviours, with the mean F1 also above 0.363.

## How a win is checked

The skeptic downloads the task zip from CaltechDATA (no login), retrains the declared model for 5 seeds, computes F1 and MAP with the MABe/CalMS21 baseline evaluation code on the test JSON, and checks that test annotations are loaded only at final scoring. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2104.02710>

## Sources

- <https://data.caltech.edu/records/s0vdx-0k302>
- <https://arxiv.org/abs/2104.02710>
- <https://sites.google.com/view/computational-behavior/our-datasets/calms21-dataset>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Self-supervised pretraining on the 6 million unlabeled frames (masked keypoint modelling, as in later behaviour-representation work), then a light per-task head.
- Temporal smoothing of frame-level outputs with an HMM or segment-level loss lifts F1 on bout-structured behaviours like mount and attack.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Test annotations are public: tuning thresholds or epochs on them is leakage (the 0.363 Task 3 value used threshold tuning; say how yours was tuned).
- Single-seed numbers do not count; the paper's values are 5-run means.
- Papers that report on random frame splits rather than the animal-identity split cannot be compared.
- Aggregator pages (sota2.com, formerly wizwand) list MSGL-Transformer (arXiv:2604.07578) at F1 0.8745 on Task 1. That is a support-weighted F1 over four classes including 'other'; its class-averaged F1 over attack, investigation and mount is about 0.75. Compare class-averaged values only.
- Video encoders pretrained on outside data (V-JEPA, VideoPrism) break this entry's training-data rule for a full win, even though their published numbers still set the bars.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/neuroscience/calms21-mouse-social-behavior-f1.md
```

Already set up? Say `run V3R1T4S on calms21-mouse-social-behavior-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `calms21-mouse-social-behavior-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
