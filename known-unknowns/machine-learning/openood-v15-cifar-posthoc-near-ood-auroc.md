# OpenOOD v1.5 CIFAR-10/100: a post-hoc OOD detector on the official cross-entropy ResNet-18 checkpoints beating the best near-OOD AUROC

🤖 **Machine learning** · standard · tractability ★★★☆☆ · compute: laptop-hours (CPU inference of a 32x32 ResNet-18 over the CIFAR training and test sets and OpenOOD's near/far-OOD test and validation sets, on the order of 10^5 images per checkpoint, for three checkpoints) · open as of 2026-10-30

## The problem

OpenOOD v1.5 (Jingyang Zhang, Jingkang Yang, Pengyun Wang, Haoqi Wang, Yueqian Lin, Haoran Zhang, Yiyou Sun, Xuefeng Du, Yixuan Li, Ziwei Liu, Yiran Chen, Hai Li; arXiv:2306.09301, DMLR) standardises out-of-distribution detection with fixed ID/OOD test sets, OOD validation sets for hyperparameter search, a unified evaluator and released checkpoints. For CIFAR-10 the near-OOD sets are CIFAR-100 and TinyImageNet and the far-OOD sets MNIST, SVHN, Textures and Places365; for CIFAR-100 near-OOD is CIFAR-10 plus TinyImageNet. The live leaderboard (https://zjysteven.github.io/OpenOOD/, maintained by Jingyang Zhang; data in results/cifar10.csv and results/cifar100.csv on the 'leaderboard' branch of github.com/zjysteven/OpenOOD, last changed 2026-05-28 when the CORE postprocessor was added) ranks methods by near-OOD AUROC averaged over three training runs. For post-hoc methods on the three released cross-entropy ResNet-18 checkpoints (ID accuracy 95.06 on CIFAR-10, 77.25 on CIFAR-100) the best near-OOD AUROC on 2026-10-28 (board unchanged since 2026-05-28) is CombOOD (Rajasekaran et al., 2024) at 91.13 on CIFAR-10 (far-OOD 94.65; next NAC 90.93, KNN 90.64), and WeiPer+KLD (Granz, Heurich and Landgraf, NeurIPS 2024) at 81.37 on CIFAR-100 (far-OOD 79.01; next GEN 81.31, fDBD 81.26); both top rows list a standard deviation of +-0.00. GROOD (ElAraby, Sahoo, Pequignot, Novello and Paull, TMLR 2025, arXiv:2312.14427v3, Table 2) reports 91.16 near-OOD and 93.8 far-OOD on CIFAR-10 with the same checkpoints, using an OOD prototype built by manifold mixup of ID samples; it is not yet on the board. Higher numbers on these checkpoints come from protocols this target excludes: OODD (Yang, Zhu, Sun, Liu, Gu and Ye, arXiv:2503.10468, Table 1) reports 82.10 near-OOD on CIFAR-100 (90.96 on CIFAR-10) with a test-time OOD dictionary built from the stream of test images, and Novello, Prudent, Dalmau, Friedrich and Pequignot (arXiv:2407.07135, Table 1) reach up to 82.2 on CIFAR-100 by tuning detector combinations on half of the OpenOOD test data and scoring the other half; P&C (Quint, NeurIPS 2026, arXiv:2605.01632) reports 91.55 on CIFAR-10 with its own retrained ResNet-18s, not the released checkpoints. Recent per-image post-hoc methods on the released checkpoints stay below the bar (KAN detector, Canevaro et al., ICLR 2025: 90.99 / 77.17; PRO, Chen, Yeh, Mou and Gu, arXiv:2503.18784: 90.70 / 81.36; BBAS, arXiv:2603.22660: 90.76 / 80.26; ARAS, arXiv:2610.32255: 88.61 / 80.37 on one checkpoint). Methods that retrain the network rank higher (RotPred+PixMix 94.86 on CIFAR-10; OAL 82.03 and outlier-exposure OE 88.30 on CIFAR-100), but this target is the post-hoc track, where everything is per-image inference on fixed public weights. Whether a better post-hoc score exists for these checkpoints is open.

## What counts as a win

Success means a post-hoc OOD score function S (Python code plus a frozen hyperparameter file) such that the skeptic's run of the official OpenOOD v1.5 evaluator (openood.evaluation_api.Evaluator from a pinned commit of https://github.com/Jingkang50/OpenOOD, with the benchmark image lists and images that the evaluator itself downloads) on EACH of the three released cross-entropy ResNet-18 checkpoints for CIFAR-10, or for CIFAR-100, gives near-OOD AUROC values whose mean is at least 0.30 points HIGHER (direction: max) than the bar. The bar is the maximum of (i) the best near-OOD AUROC of a CrossEntropy post-hoc row in the live results/cifar10.csv or results/cifar100.csv, re-fetched immediately before claiming, and (ii) the best near-OOD AUROC that the NOVELTY skeptic finds published for a method that follows the same rules as S (below) on the same three released OpenOOD v1.5 checkpoints and the full official OpenOOD v1.5 test sets. On 2026-10-28, as far as found, the bar is 91.16 for CIFAR-10 (GROOD, arXiv:2312.14427v3 Table 2; board 91.13) and 81.37 for CIFAR-100 (WeiPer+KLD). Published numbers obtained outside these rules neither set the bar nor qualify: test-time or transductive methods that adapt to the test stream (e.g. OODD, arXiv:2503.10468: 82.10 on CIFAR-100), protocols that tune or fit on part of the OOD test sets (e.g. Novello et al., arXiv:2407.07135: up to 82.2 on CIFAR-100), and retrained or modified networks. In addition the mean far-OOD AUROC must be at least that of MSP on the same checkpoints (board: 90.73 for CIFAR-10, 77.76 for CIFAR-100). Post-hoc means: the network weights and its argmax predictions are those of the released checkpoint, unmodified (the evaluator's ID accuracy, averaged over the three checkpoints, must equal the board's CrossEntropy value within 0.10: 95.06 or 77.25); S computes each test image's score from that image alone, with no state carried between test images or batches; S may use the network's activations, logits and gradients and statistics of the ID TRAINING split only (data derived from training images, such as mixup samples, is allowed and must be declared); it may not use any other model (no CLIP or ImageNet features), outlier or auxiliary data, OOD test images, or test-set statistics; hyperparameters are fixed a priori or chosen only on OpenOOD's own ID/OOD validation splits (APS mode) and frozen before the test evaluation.

## Partial wins

- **p1:** A post-hoc score function obeying every rule of the main criterion whose mean near-OOD AUROC is at least 0.10 points above the bar AND whose mean far-OOD AUROC is at least the far-OOD AUROC of the entry that sets the bar (CIFAR-10: GROOD 93.8; CIFAR-100: WeiPer+KLD 79.01), i.e. a smaller but Pareto-better result.
- **p2:** A reproducibility finding: an independent re-run (official evaluator, the three official checkpoints, the method's own public code at a stated commit with its published hyperparameters) of one of the +-0.00 CrossEntropy rows (CIFAR-10: CombOOD 91.13 or WeiPer+KLD 90.54; CIFAR-100: WeiPer+KLD 81.37 or CombOOD 78.77) whose three-checkpoint mean near-OOD AUROC differs from the listed value by more than 0.50 points. Reported as a correction for the human to raise with the maintainers, never as a record.

## How a win is checked

Skeptic creates a fresh virtual environment, installs OpenOOD from a pinned commit (recorded), lets the evaluator download the benchmark, downloads the official v1.5 checkpoints with OpenOOD's own download script (README 'Pre-trained checkpoints'), and compares checkpoint sha256 with the claimant's manifest. They read S in full (looking for test-set or OOD-data access, extra models, label use, network modification, state kept between test images), then run Evaluator(net, id_name='cifar10' or 'cifar100', postprocessor=S, ...).eval_ood() for each checkpoint and record near-OOD AUROC, far-OOD AUROC and ID accuracy, averaging over the three. To confirm per-image scoring they re-score a random 1,000-image sample of each test set one image at a time and in shuffled order and require the same scores as in the full run (to float tolerance). They re-fetch the live CSV, compute the bar under the rules of the criterion, and search arXiv/OpenReview for newer results on the same checkpoints, recording why any higher number is or is not admissible. CPU time is roughly 10-30 minutes per checkpoint plus any hyperparameter sweep on the validation split.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://zjysteven.github.io/OpenOOD/>

## Sources

- <https://zjysteven.github.io/OpenOOD/>
- <https://raw.githubusercontent.com/zjysteven/OpenOOD/leaderboard/results/cifar10.csv>
- <https://raw.githubusercontent.com/zjysteven/OpenOOD/leaderboard/results/cifar100.csv>
- <https://github.com/Jingkang50/OpenOOD>
- <https://arxiv.org/abs/2306.09301>
- <https://arxiv.org/abs/2312.14427>
- <https://arxiv.org/abs/2503.10468>
- <https://arxiv.org/abs/2407.07135>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Combine complementary signals: the top CIFAR-10 rows rest on different evidence (combined scores for CombOOD, neuron-activation statistics for NAC, nearest-neighbour distances of penultimate features for KNN). A rank-normalised combination of feature-space distances, logit scores (energy, GEN) and activation statistics, weighted on the OOD validation split, is the obvious first attempt.
- Multi-layer class-conditional statistics from the 50k training images: per-class means with shrunk shared covariance at several depths, whitened and combined; near-OOD sets (CIFAR-100 for CIFAR-10, and the reverse) may separate better in mid-level features than in the logits.
- Gradient and perturbation scores: gradients with respect to a class or OOD prototype (as in GROOD), weight perturbations of the class projections (as in WeiPer), or the sensitivity of the logits to small input perturbations, all computed without touching OOD data.
- Report the validation-to-test gap of every configuration; a method that only wins on test after many tries is over-fitted to the test sets even if the rules were followed.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Tuning on the OOD test sets (or on near-duplicates such as other TinyImageNet images) is leakage; OpenOOD's APS mode searches only on its validation splits. The CRITERION skeptic must read the tuning code.
- Changing the classifier (e.g. ReAct, ASH or SCALE applied to the predictions as well as to the score) changes ID accuracy; the criterion pins ID accuracy to the board value.
- Reporting one checkpoint or the best of three: the criterion uses the mean over all three released checkpoints.
- Using CLIP or ImageNet-pretrained features, or outlier exposure, moves the method to another track.
- Version drift: evaluator versions and image lists can move AUROC by tenths of a point; pin the OpenOOD commit and report it.
- Downloads: the evaluator fetches OpenOOD's copies of TinyImageNet (ImageNet-derived) and Places365 from Google Drive. The human should review those datasets' terms first; if a quota or confirmation page appears, stop and let the human fetch the files.
- The +-0.00 rows may be single-run numbers; a claim must still beat the stated bar, not a re-run of it.
- Test-time and transductive scores: a dictionary, memory bank or statistics updated from the stream of test images (as in OODD), or detector combinations tuned on part of the official OOD test sets (as in Novello et al.), use OOD test data. They are excluded even when a paper calls them post-hoc, and their higher published numbers (82.10 and up to 82.2 on CIFAR-100) do not set the bar.
- Numbers on other checkpoints do not compare: P&C's 91.55 near-OOD AUROC on CIFAR-10 uses its own retrained pre-activation ResNet-18s (ID accuracy 95.59), not the released checkpoints (95.06).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/openood-v15-cifar-posthoc-near-ood-auroc.md
```

Already set up? Say `run V3R1T4S on openood-v15-cifar-posthoc-near-ood-auroc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `openood-v15-cifar-posthoc-near-ood-auroc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
