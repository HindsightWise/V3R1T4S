# MoNuSeg 2018 multi-organ nucleus segmentation: beat the best published AJI (0.7063; challenge best 0.6907) on the public 14-image test set

🧬 **Disease research** · standard · tractability ★★☆☆☆ · compute: laptop-hours (30 training and 14 test 1000x1000 H&E tiles; a small GPU or Apple MPS helps) · open as of 2026-10-30

## The problem

MoNuSeg (Multi-Organ Nucleus Segmentation, MICCAI 2018; Neeraj Kumar, Ruchika Verma, Amit Sethi and colleagues; post-challenge paper Kumar et al., IEEE TMI 2020) asks for instance segmentation of nuclei in H&E tiles from TCGA covering several organs. The training set has 30 images with about 22,000 annotated nuclear boundaries; the test set (with about 7,000 annotated nuclei, including organs absent from training) is now public with annotations on the challenge Data page under CC BY-NC-SA 4.0. Ranking is the mean Aggregated Jaccard Index (AJI, Algorithm 1 of Kumar et al. 2017) over the 14 test images; challenge rules exclude external training data. The final results page is topped by CUHK&IMSIGHT at 0.6907, then BUPT.J.LI 0.6868, pku.hzq 0.6852, Yunzhi 0.6788 and Navid Alemi 0.6779. The best published AJI on the official 14-image test set from a model without external annotated data that we found is 0.7063: a ResUNet-101 with instance-aware self-supervised pretraining on MoNuSeg images (Xinpeng Xie, Jiawei Chen, Yuexiang Li, Linlin Shen, Kai Ma and Yefeng Zheng, MICCAI 2020, arXiv:2007.11186), above all five leaders. Results from models trained on pooled external annotated sets (e.g. 0.8042 from MoNuSeg+CPM-17+CoNSeP training, Furkan Atlan and Emrah Hancer, Turk. J. Elec. Eng. & Comp. Sci. 2025) are a different class. The organisers' evaluation code (AJI per image, mask generation from XML) is at github.com/ruchikaverma-iitg/MoNuSeg. Many later papers report Dice or IoU on MoNuSeg, AJI from cross-validation on the 30 training images, or AJI on the older 16/14 split of Kumar et al. 2017, which are different benchmarks.

## What counts as a win

Instance label maps (one unique positive integer per nucleus, 0 background) for all 14 official MoNuSeg 2018 test images, from a model trained only on the 30 official training images (public ImageNet-pretrained backbones allowed if declared; self-supervised pretraining allowed on the 30 training images only; no other annotated nuclei data; pathology foundation models reported as a separate class), frozen before any test scoring, whose mean AJI over the 14 images, computed by the skeptic with the organisers' AJI code against masks generated from the released test XML annotations, is STRICTLY HIGHER (direction: max), by at least 0.005, than every AJI on the official 14-image 2018 test set from a model without external annotated nuclei data: the results page (0.6907, re-fetched live immediately before claiming), Xie et al. 2020 (0.7063, arXiv:2007.11186), and any higher such value found by the NOVELTY check. On 2026-10-30 this means a mean of at least 0.7113 over 3 training seeds. Values from models trained with external annotated data or pathology foundation models do not set this bar and are reported separately.

## Partial wins

- **p1:** Mean AJI strictly above 0.6868 (the second-place entry) on the 14 test images, 3-seed mean, from a model under 5M parameters trained on a laptop in under 6 hours.
- **p2:** A reproducible scoring note: AJI of a released baseline (e.g. HoVer-Net or Cellpose retrained on the 30 training images) on the official test set, computed with both the organisers' MATLAB code and a Python port, agreeing to 1e-4, with the port released.

## How a win is checked

Skeptic downloads the training and test data from the MoNuSeg Data page, generates instance masks from the test XML with the organisers' code, scores the claimed label maps with Aggregated_Jaccard_Index_v1_0.m (or a port checked against it), retrains one seed from the released script, and audits that no test file is read before final scoring. Minutes for scoring, hours for a retrain.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://monuseg.grand-challenge.org/Results/>

## Sources

- <https://monuseg.grand-challenge.org/Results/>
- <https://monuseg.grand-challenge.org/Data/>
- <https://monuseg.grand-challenge.org/Evaluation/>
- <https://github.com/ruchikaverma-iitg/MoNuSeg>
- <https://ieeexplore.ieee.org/document/8880654>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Boundary-aware targets (distance maps or horizontal/vertical gradient maps as in HoVer-Net) separate touching nuclei, which is what AJI punishes most.
- Stain augmentation from the training tiles only, since the test organs and sites differ.
- Cross-domain import (cell biology): Cellpose-style flow fields trained only on the 30 tiles.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- AJI, AJI+ and PQ differ; Kumar et al.'s 2017 16/14 split (used by HoVer-Net) is not the 2018 challenge test set. Compare only mean AJI on the 14 official test images.
- Test annotations are public: picking epochs or post-processing thresholds by test AJI is leakage.
- Masks must be generated from the XML the same way the organisers did (he_to_binary_mask_final.m); a different rasterisation of overlapping nuclei shifts AJI.
- External annotated nuclei sets (Kumar, CPM, PanNuke, Lizard, MoNuSAC) overlap TCGA sources and break the challenge's no-external-data rule; report separately.
- A research benchmark; it says nothing about clinical diagnosis.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/disease-research/monuseg-2018-test-aji.md
```

Already set up? Say `run V3R1T4S on monuseg-2018-test-aji`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `monuseg-2018-test-aji`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
