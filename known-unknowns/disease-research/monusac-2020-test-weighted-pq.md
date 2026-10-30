# MoNuSAC 2020 nucleus segmentation and classification: beat TIA-Lab's challenge-best PQ 0.6119 on the public test set

🧬 **Disease research** · standard · tractability ★★☆☆☆ · compute: laptop-hours (a few GB of H&E regions; a small GPU or Apple MPS helps) · open as of 2026-10-30

## The problem

MoNuSAC 2020 (Multi-organ Nuclei Segmentation And Classification, ISBI 2020; Ruchika Verma, Neeraj Kumar, Amit Sethi and colleagues; post-challenge paper Verma et al., IEEE TMI 2021) asks for instance segmentation and classification of four nucleus types (epithelial, lymphocyte, neutrophil, macrophage) in H&E regions from several organs and hospitals. The testing data set, images and annotations, is now public on the challenge Data page (Google Drive), together with organiser code for mask generation and the PQ metric (github.com/ruchikaverma-iitg/MoNuSAC, PQ_metric.ipynb). The ranking metric is the weighted average of class-specific Panoptic Quality (definition in section V of the challenge document). The final leaderboard is topped by TIA-Lab (Warwick) at 0.6119, then SJTU_426 0.5793, IVG 0.5084, LSL000UD 0.4969 and Sharif HooshPardaz 0.4808; a post-challenge leaderboard lists six more teams (Amirreza Mahbod, IIAI, Sharif_HooshPardaz, Trnal, Cp&ig, Onward) without scores on the page. The gap between first and second place suggests the task is far from saturated.

## What counts as a win

Per-class instance masks for every official MoNuSAC 2020 test image, from a model trained only on the official training set (public ImageNet-pretrained backbones allowed if declared; no other annotated nuclei data; pathology foundation models reported as a separate class), frozen before any test scoring. The masks' final average PQ is computed by the skeptic with the organisers' PQ_metric code, against masks generated from the released test XML annotations, with ambiguous regions excluded as the organisers do. It must be STRICTLY HIGHER (direction: max), by at least 0.005 and as the mean over 3 training seeds, than two values. The first is 0.6119 (TIA-Lab, final leaderboard on the results page, re-fetched live immediately before claiming). The second is any weighted-average PQ on the official test set, computed with the organisers' metric, found by the NOVELTY check. That includes any scored post-challenge entry reported in Verma et al., IEEE TMI 2021.

## Partial wins

- **p1:** Final average PQ strictly above 0.5793 (second place) on the official test set, 3-seed mean, with a model trained on a laptop in under 8 hours.
- **p2:** Final average PQ strictly above 0.6119 (the challenge-best TIA-Lab entry) on the official test set, computed with the organisers' PQ_metric code, 3-seed mean, without the NOVELTY margin, with released code and weights.

## How a win is checked

Skeptic downloads the MoNuSAC test data and annotations from the Data page, generates n-ary masks with the organisers' notebook, scores the claimed masks with PQ_metric.ipynb logic, retrains one seed, and audits that no test file is read before final scoring. Minutes for scoring, hours for a retrain.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://monusac-2020.grand-challenge.org/Results/>

## Sources

- <https://monusac-2020.grand-challenge.org/Results/>
- <https://monusac-2020.grand-challenge.org/Data/>
- <https://monusac-2020.grand-challenge.org/Evaluation_Metric/>
- <https://github.com/ruchikaverma-iitg/MoNuSAC>
- <https://ieeexplore.ieee.org/abstract/document/9446924>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The rare classes dominate the weighted average; class-balanced sampling and copy-paste augmentation of rare nuclei.
- Cross-domain import (panoptic segmentation for street scenes): Mask2Former-style query heads with a nucleus-scale pixel decoder.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The colour-coded ground-truth images on the Data page are illustrative only (the page says so); generate masks from the XML annotations.
- Test annotations are public: tuning on the test set is leakage.
- Many papers evaluate MoNuSAC on their own splits or with unweighted PQ; only the official test set and the organisers' PQ compare.
- A research benchmark; not clinical diagnosis.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/disease-research/monusac-2020-test-weighted-pq.md
```

Already set up? Say `run V3R1T4S on monusac-2020-test-weighted-pq`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `monusac-2020-test-weighted-pq`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
