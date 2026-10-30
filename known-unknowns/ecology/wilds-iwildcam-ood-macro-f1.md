# iWildCam2020-WILDS camera-trap species ID: beat the leaderboard's best out-of-distribution test macro F1 (52.0, AutoFT)

🐦 **Ecology and bioacoustics** · standard · tractability ★★☆☆☆ · compute: needs cluster (one GPU for 1-3 days per replicate; ~11 GB of camera-trap images via the wilds package) · open as of 2026-10-30

## The problem

iWildCam2020-WILDS (Beery et al.; packaged by the WILDS team, Koh, Sagawa, Liang and colleagues) asks for species labels for camera-trap images. Models train on one set of camera locations and are tested on held-out locations (the OOD test split, released with labels in the wilds package). The official metric is macro F1 over classes on the OOD test split, averaged over random replicates, with model selection on the OOD validation split. The WILDS leaderboard (re-fetched 2026-10-30) lists these entries without unlabeled data: AutoFT, CLIP ViT-L/14@336 (Caroline Choi, Yoonho Lee, Annie Chen, Allan Zhou, Aditi Raghunathan, Chelsea Finn; 2024-01-28) 52.0 (0.4); FLYP (Sankalp Garg) 46.0; Model Soups (Mitchell Wortsman) 43.3; ERM CLIP ViT-L 41.4. The best entry that follows the default-model guidelines (no asterisk) is ABSGD, ResNet-50 (Qi Qi), at 33.0. With unlabeled data the top entry is Connect Later, ResNet-50 (Helen Qu), at 36.8. The newest entry is COSMO (2025-02-28, 32.3). In the literature, Dual Risk Minimization (Kaican Li, Weiyan Xie and colleagues, arXiv 2411.19757) reports 51.8 with CLIP ViT-L/14@336, just under AutoFT. No 2024-2026 arXiv abstract found on 2026-10-30 claims more than 52.0. Rare classes dominate macro F1, which is why macro F1 stays far below accuracy.

## What counts as a win

Mean OOD test macro F1 (WILDS evaluator, dataset.eval on the iwildcam v2.0 'test' split) over at least 3 replicates with different seeds, each replicate selected by OOD validation macro F1 only. The mean must be STRICTLY GREATER (direction: max) than the top 'without unlabeled data' iWildCam entry on https://wilds.stanford.edu/leaderboard/, re-fetched live immediately before claiming (52.0, AutoFT, on 2026-10-30), by at least 0.5 points. It must also beat any OOD test macro F1 for iWildCam2020-WILDS that the NOVELTY skeptic finds in a 2024-2026 paper (the highest known on 2026-10-30 is DRM's 51.8). Training uses only the iWildCam train split labels. Unlabeled WILDS splits are allowed, but such a claim is then compared against both tables. Pretrained weights are allowed if declared with their training corpora, but no corpus documented to contain WCS Camera Traps or iWildCam images may be used (LILA collections, MegaDetector and other detectors trained on LILA, biology foundation-model corpora that ingested them). Web-scale corpora without a public manifest, such as OpenAI CLIP's, are allowed, as they are for the leaderboard entries. Deliverables: code, configs, seeds, per-replicate saved test predictions and the WILDS eval output.

## Partial wins

- **p1:** With an ImageNet-pretrained ResNet-50 and no extra pretraining data or auxiliary models, mean OOD test macro F1 over 3 replicates above 36.5. That is the best known such number: ERM w/ targeted augmentation (Irena Gao, asterisked) at 36.5, with DRM's ERM+LP-FT ResNet-50 baseline at 36.4 (arXiv 2411.19757 Table 12). ABSGD's 33.0 is the best entry that follows the guidelines, but it is already beaten.
- **p2:** With WILDS unlabeled data and a ResNet-50 backbone, mean OOD test macro F1 over 3 replicates above 36.8 (Connect Later).
- **p3:** With a CLIP ViT-B/16 or smaller backbone, mean OOD test macro F1 over 3 replicates above 46.0 (FLYP's ViT-L/14@336 entry).

## How a win is checked

The skeptic installs the pinned wilds version and downloads iwildcam v2.0. They load each replicate's saved OOD test predictions, recompute macro F1 with dataset.eval and check that the predictions cover every OOD test image. They re-train one replicate from the released config and confirm its score lands within 2 standard deviations. They audit that checkpoint selection used OOD validation only and that no declared pretraining corpus or auxiliary model (such as a camera-trap detector) is documented to contain iWildCam or WCS images. Finally they re-fetch the leaderboard and do the literature check.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wilds.stanford.edu/leaderboard/>

## Sources

- <https://wilds.stanford.edu/leaderboard/>
- <https://wilds.stanford.edu/datasets/>
- <https://arxiv.org/abs/2012.07421>
- <https://arxiv.org/abs/2401.10220>
- <https://arxiv.org/abs/2411.19757>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Robust fine-tuning of large vision-language models (WiSE-FT style weight interpolation, FLYP contrastive fine-tuning, learned objectives as in AutoFT, LLM-described core features as in DRM) with class-balanced losses aimed at macro F1.
- Cross-domain import (long-tail recognition): logit adjustment and decoupled classifier re-training on frozen features, since macro F1 rewards rare classes.
- Camera-trap specific: use the WILDS location and sequence metadata at train time only (sequence-consistent pseudo-labels, location-balanced sampling). MegaDetector crops are out: MegaDetector was trained on LILA camera-trap images, which the corpus rule excludes.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Using the ID validation split or the OOD test split for checkpoint or hyperparameter selection is leakage; WILDS prescribes OOD validation.
- Asterisked entries deviate from the guidelines; a claim must state which deviations it uses.
- Single-seed results are not comparable: the replicate std of iWildCam macro F1 is about 1 point.
- Pretraining corpora scraped from LILA or GBIF can contain the WCS camera-trap images used for the test locations.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/wilds-iwildcam-ood-macro-f1.md
```

Already set up? Say `run V3R1T4S on wilds-iwildcam-ood-macro-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wilds-iwildcam-ood-macro-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
