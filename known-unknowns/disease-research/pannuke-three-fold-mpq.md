# PanNuke pan-cancer nucleus segmentation and classification: beat the best published three-split mPQ (0.5123, PromptNucSeg-H)

🧬 **Disease research** · standard · tractability ★★☆☆☆ · compute: laptop-days (three 700 MB folds of 256x256 patches; one GPU for days is more realistic for transformer models) · open as of 2026-10-30

## The problem

PanNuke (Jevgenij Gamper, Navid Alemi Koohbanani, Ksenija Benes, Simon Graham, Mostafa Jahanifar, Syed Ali Khurram, Ayesha Azam, Katherine Hewitt, Nasir Rajpoot; ECDP 2019 and arXiv:2003.10778) is a semi-automatically generated pan-cancer set of H&E patches from 19 tissue types with five nucleus classes (neoplastic, inflammatory, connective, dead, epithelial). It is released by Warwick TIA as three folds (fold_1.zip etc., direct download, CC BY-NC-SA 4.0) with three fixed train/validation/test splits, and scored with the official PanNuke-metrics code: mPQ (PQ averaged over classes and tissues) and bPQ (all nuclei as one class, averaged over tissues), averaged over the three splits. The extension paper's HoVer-Net baseline is about 0.46 mPQ; CellViT (Fabian Hörst, Jens Kleesiek and colleagues, Medical Image Analysis 2024) reports 0.4980 mPQ; LKCell (Ziwei Cui, Jingfeng Yao, Lunbin Zeng, Juan Yang, Wenyu Liu, Xinggang Wang; arXiv:2407.18054) reports 0.5080 and CellVTA (arXiv:2504.00784) 0.506. PromptNucSeg (Zhongyi Shui, Yunlong Zhang, Kai Yao, Chenglu Zhu, Sunyi Zheng, Jingxiong Li, Honglin Li, Yuxuan Sun, Ruizhe Guo, Lin Yang; arXiv:2311.15939v4, Table 1), a prompt-driven SAM-based method, reports 0.5123 mPQ and 0.6924 bPQ for PromptNucSeg-H on the same three splits, the best value we could pin. Our 2024-2026 literature sweep was limited, so the NOVELTY check carries weight here.

## What counts as a win

Predictions (instance maps and class maps in the PanNuke-metrics format) on the test fold of each of the three official splits (split 1: train fold 1, validate fold 2, test fold 3; split 2: train 2, validate 1, test 3; split 3: train 3, validate 2, test 1, as on the Warwick page). Each split's model is trained only on its train fold and selected only on its validation fold. Public pretrained backbones are allowed if declared; no other annotated nuclei data. The mPQ averaged over the three splits, computed by the skeptic with TissueImageAnalytics/PanNuke-metrics, must be STRICTLY HIGHER (direction: max), by at least 0.005, than two values. The first is 0.5123 (PromptNucSeg-H, arXiv:2311.15939v4 Table 1, re-checked live immediately before claiming). The second is every three-split PanNuke mPQ found by the NOVELTY check (LKCell's 0.5080, CellVTA's 0.506 and later work included). bPQ must not be below 0.6924 or the best published bPQ found, whichever is higher. Where a released PromptNucSeg or LKCell checkpoint exists, the skeptic also scores it with the same code, and the claim must beat that reproduced value too.

## Partial wins

- **p1:** Three-split mPQ strictly above 0.4980 (CellViT-SAM-H as reported by Hörst et al. 2024) with a model under 50M parameters, released code and weights, computed with the official metrics code.
- **p2:** A model under 5M parameters trained on a laptop whose three-split mPQ and bPQ, computed with the official metrics code, are strictly above 0.4629 and 0.6596 (HoVer-Net as tabulated from the PanNuke extension paper).

## How a win is checked

Skeptic downloads the three folds from the Warwick PanNuke page, runs the released inference on each split's test fold, and scores with PanNuke-metrics run.py; checks fold assignments against the page's three split definitions and audits that test folds are never read in training or selection. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2311.15939>

## Sources

- <https://warwick.ac.uk/fac/cross_fac/tia/data/pannuke>
- <https://github.com/TissueImageAnalytics/PanNuke-metrics>
- <https://arxiv.org/abs/2003.10778>
- <https://arxiv.org/abs/2306.15350>
- <https://arxiv.org/abs/2407.18054>
- <https://arxiv.org/abs/2311.15939>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The dead-cell class is tiny and drags mPQ down; targeted oversampling and loss reweighting for it.
- Tissue-conditioned heads: the metric averages over 19 tissues, so per-tissue calibration helps rare tissues.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Some papers report a single split or the best split; only the three-split mean with the official folds compares.
- Published numbers for the same model differ by evaluation protocol (CellVTA, arXiv:2504.00784, reports CellViT SAM-L at 0.492 and HoVer-Net at 0.443, against 0.4980 and 0.4629 elsewhere). Score the claim and any reproducible baseline with the same official code before comparing.
- Labels are semi-automatic and noisy; tiny mPQ gains can be seed noise, so report seed variance.
- Pathology foundation models are often pretrained on TCGA, the same source as PanNuke images; declare such backbones.
- Selecting on the test fold is leakage; each split has its own validation fold, and fold 3 is the test fold of two splits.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/disease-research/pannuke-three-fold-mpq.md
```

Already set up? Say `run V3R1T4S on pannuke-three-fold-mpq`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pannuke-three-fold-mpq`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
