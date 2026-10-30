# CaFFe glacier calving fronts in SAR: beat the best published mean distance error on the out-of-sample Mapple and Columbia test set

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: laptop-days on a GPU workstation (dataset 2.7 GB of PNG SAR images; the tyrionT-GRU authors trained on 4x A100 80 GB and report inference on one 8 GB GPU; CPU-only training is impractical) · open as of 2026-10-30

## The problem

CaFFe (Gourmelon, Seehaus, Braun, Maier, Christlein; ESSD 14:4287, 2022; PANGAEA doi:10.1594/PANGAEA.940950, CC-BY-4.0) is the standard benchmark for delineating glacier calving fronts in SAR imagery. It has 681 multi-mission SAR images (ERS-1/2, RADARSAT-1, ENVISAT, ALOS PALSAR, TerraSAR-X, TanDEM-X, Sentinel-1; 1995-2020) of seven glaciers, with front labels, zone labels (glacier, rock, ocean/melange, no-information) and bounding boxes for the moving front. Five glaciers are for training. The fixed test set is all 122 images of Mapple (Antarctic Peninsula) and Columbia (Alaska). The headline metric is the mean distance error (MDE) between the predicted and the labelled front, reported with the number of test images where no front was predicted. Published state as of 2026-10-30. Single-image models: TYRION with SSL4SAR pretraining, 293 +- 54 m over 5 runs (OptTranslator; OptSimMIM 300 +- 60 m), and 5-member ensembles of 238 m (OptSimMIM) and 246 m (OptTranslator) (Gourmelon et al., IEEE TGRS 2025, arXiv:2507.01747, Table I); tyrionS 306 +- 33.5 m; reduced tyrionT at T=1, 317.4 +- 26.7 m (5-run ensemble 296.3 m); AMD-HookNet++ 367 m (Wu et al., arXiv:2512.14639). Multi-temporal models use a time series of T = 8 images of the same glacier at the same resolution (the paper does not say whether the other images precede the target). Best is tyrionT-GRU: 202.7 +- 27.6 m over 5 runs, 5-run ensemble 184.4 m, zone mIoU 82.1 +- 0.8 (ensemble 83.6), no test image missing a front (Dreier, Gourmelon, Pyles, Wu, Braun, Seehaus, Maier, Christlein; arXiv:2512.11560, Dec 2025, Tables 2-3; published in ISPRS J. Photogramm. Remote Sens. 239:276-290, 2026, whose page returned 403 on 2026-10-30 and was not read). Its code is public at github.com/ki7077/Multi-Temporal-Tyrion. Open task: a lower MDE.

## What counts as a win

A saved, runnable model (code, fixed seeds, weights) trained only on the CaFFe train folder, with model selection on a validation split of the training glaciers only, never on test labels. It is evaluated on all 122 test images with the post-processing and MDE computation of the official repository (github.com/Nora-Go/Calving_Fronts_and_Where_to_Find_Them, validate_or_test.py --mode test), and every test image must receive a predicted front (0 images without a front). Multi-temporal inputs may only be CaFFe SAR images of the same glacier (never any front or zone label of a test image). The claim states whether its time series is causal (only images acquired on or before the target date). The MDE must be strictly lower (direction: min) than 184.4 m (tyrionT-GRU 5-run ensemble, arXiv:2512.11560 / ISPRS J. Photogramm. Remote Sens. 239, 2026; re-check both versions before claiming) and lower than any CaFFe test MDE in a paper from the last 24 months found by a fresh search. A claimed ensemble is compared with ensembles. A claimed single model is reported as the mean over 5 training seeds and must also be below 184.4 m.

## Partial wins

- **p1:** A single-image model (each prediction uses only its own SAR image) whose test MDE, as the mean over 5 seeds, is strictly below 293 m (SSL4SAR TYRION, 5-run mean), or, for a 5-member single-image ensemble, strictly below 238 m (SSL4SAR TYRION OptSimMIM ensemble, arXiv:2507.01747 Table I), with 0 images without a front.
- **p2:** A multi-temporal model whose test MDE, as the mean over 5 seeds, is strictly below 202.7 m (tyrionT-GRU 5-run mean), with 0 images without a front.
- **p3:** Zone-segmentation mIoU on the 122 test images (official zone metric, 'All' column) strictly above 82.1 as the 5-seed mean, or strictly above 83.6 for a 5-member ensemble, with MDE no worse than 202.7 m (5-seed mean) and 0 images without a front.

## How a win is checked

Skeptic downloads data_raw.zip from PANGAEA, checks that the training code reads only the train folders (code read plus a run with the test label folders removed), runs inference and the official post-processing/MDE script on the 122 test images, counts images without a front and compares with the cited papers. Several GPU-hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2512.11560>

## Sources

- <https://doi.pangaea.de/10.1594/PANGAEA.940950>
- <https://doi.org/10.5194/essd-14-4287-2022>
- <https://github.com/Nora-Go/Calving_Fronts_and_Where_to_Find_Them>
- <https://arxiv.org/abs/2512.11560>
- <https://www.sciencedirect.com/science/article/pii/S092427162600300X>
- <https://github.com/ki7077/Multi-Temporal-Tyrion>
- <https://arxiv.org/abs/2507.01747>
- <https://arxiv.org/abs/2512.14639>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: stronger SAR-specific pretraining (SSL4SAR-style) of a Tyrion/HookNet backbone, then multi-temporal fusion with a GRU over the 8 previous acquisitions.
- Treat the front as a contour, not a mask: predict a signed distance field or an active-contour/snake refinement inside the bounding box, which directly targets MDE.
- Cross-domain import (medical imaging): boundary-loss and Hausdorff-distance losses used for organ contours; temporal consistency as in cine-MRI segmentation.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- MDE is averaged only over images with a predicted front, so dropping hard images lowers the MDE. Always report the count of images without a front; the criterion requires 0.
- The 38 m human figure and the 75 m ensemble figure in SSL4SAR come from a multi-annotator study, not from the full test set; they are not comparators.
- Numbers on new sites (e.g. Svalbard in arXiv:2601.21663, or the ESSD 2026 Svalbard frontal-ablation product) are out-of-distribution results, not CaFFe test results.
- Tuning post-processing thresholds on the test glaciers is leakage.
- The tyrionT code is public (github.com/ki7077/Multi-Temporal-Tyrion; its README reports training on 4x A100 80 GB), but trained weights are not stated to be released. Re-running it is possible, but the comparator remains the printed table values; check the published ISPRS version for any change from arXiv v1.
- In arXiv:2512.11560 the test time series are restricted to images of the same glacier at the same resolution; resampling across resolutions changes the inputs.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/caffe-calving-front-mean-distance-error.md
```

Already set up? Say `run V3R1T4S on caffe-calving-front-mean-distance-error`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `caffe-calving-front-mean-distance-error`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
