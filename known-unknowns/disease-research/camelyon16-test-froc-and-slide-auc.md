# CAMELYON16 lymph-node metastasis detection: beat the best lesion-level FROC on the public 129-slide test reference

🧬 **Disease research** · standard · tractability ★★☆☆☆ · compute: needs cluster (or one GPU workstation for days; about 750 GB of whole-slide images: 220.7 GB test, 532 GB training, on the public camelyon-dataset S3 bucket) · open as of 2026-10-30

## The problem

CAMELYON16 (Babak Ehteshami Bejnordi, Mitko Veta, Jeroen van der Laak, Geert Litjens and colleagues, JAMA 2017; Computational Pathology Group, Radboud UMC, with UMC Utrecht) asks for detection of breast-cancer metastases in H&E whole-slide images of sentinel lymph nodes. The full data set is open under CC0 on the AWS Registry of Open Data (s3://camelyon-dataset/CAMELYON16, no account needed): 270 training slides (111 tumour, 159 normal) and 129 test slides (49 tumour, 80 normal; test_049 was removed as a duplicate). The bucket holds test images, test masks, lesion XML annotations, evaluation/reference.csv (labels for all 399 slides) and the organisers' evaluate.py, so both official metrics can be recomputed offline: the lesion-level FROC score (mean sensitivity at 1/4, 1/2, 1, 2, 4 and 8 false positives per slide; isolated tumour cells excluded) and the slide-level ROC AUC. The challenge results page (closed November 2016) is topped on both boards by Harvard Medical School and MIT, Method 2 (updated) (Dayong Wang, Aditya Khosla, Rishab Gargeya, Humayun Irshad, Andrew Beck): AUC 0.9935 and FROC 0.8074. After the challenge, Liu et al. (Google, arXiv:1703.02442, Table 1) report a test FROC of 0.885 for an ensemble of three models (95% CI 0.843 to 0.922), with 92.4% sensitivity at 8 FP and AUC 0.977. Both the leaderboard values and Liu et al.'s were computed on the original 130 test slides. Slide-level AUC is close to saturation; the lesion-level FROC is the less saturated number.

## What counts as a win

A detection CSV (p, x, y at level 0) for each of the 129 official test slides and a slide-level probability per slide, from a model trained only on the 270 CAMELYON16 training slides and their annotations (public pretrained backbones allowed if declared; pathology foundation models and any CAMELYON17 data are a separate comparison class, reported separately), frozen before any test scoring. The win is a FROC score, computed by the skeptic with the official CAMELYON16/evaluation/evaluate.py against the public test masks and reference.csv, that is STRICTLY HIGHER (direction: max) by at least 0.005 than the maximum of three values. The first is 0.8074 (challenge leaderboard, re-fetched live immediately before claiming). The second is 0.885 (Liu et al., arXiv:1703.02442, Table 1, ensemble-of-3, on 130 test slides). The third is any other FROC on the official CAMELYON16 test set found by the NOVELTY check. The win threshold is therefore at least 0.890.

## Partial wins

- **p1:** FROC strictly above the maximum of the challenge leaderboard's 0.8074 and any FROC on the official test set found by the NOVELTY check for a model meeting the same budget (trained in under 48 hours on one GPU, with released code and weights), on the 129-slide test reference, computed with the official evaluate.py.
- **p2:** Slide-level ROC AUC strictly above 0.9935 on the 129 test slides (labels from evaluation/reference.csv), from the same frozen model and comparison class, and above any same-class AUC on the official test set found by the NOVELTY check. Report it with a 1,000-sample bootstrap 95% interval.
- **p3:** Using only slide-level labels for training (no lesion annotations), a slide-level AUC strictly above every weakly-supervised (multiple-instance learning) AUC on the official test set found by the NOVELTY check for the same feature-extractor class (ImageNet-pretrained or pathology foundation model, stated).

## How a win is checked

Skeptic downloads CAMELYON16/images/test_*.tif, masks, annotations and evaluation/ from s3://camelyon-dataset with --no-sign-request, checks MD5s against checksums.md5, runs the official evaluate.py on the claimed detection CSVs for all 129 slides, and computes slide AUC from the claimed probabilities against reference.csv. Audits training code for any read of test files before scoring and re-runs inference from released weights on a sample of test slides. Hours for scoring, days for re-inference.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://camelyon16.grand-challenge.org/Results/>

## Sources

- <https://camelyon16.grand-challenge.org/Results/>
- <https://registry.opendata.aws/camelyon/>
- <https://camelyon-dataset.s3.us-west-2.amazonaws.com/CAMELYON16/README.md>
- <https://camelyon-dataset.s3.us-west-2.amazonaws.com/CAMELYON16/evaluation/reference.csv>
- <https://arxiv.org/abs/1703.02442>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Hard-negative mining on normal tissue that mimics tumour (germinal centres, histiocytes) is what lifted post-challenge FROC; budget training time for it.
- Multi-resolution context: pair a 40x patch classifier with a lower-magnification context branch, then turn the heatmap into detections with non-maximum suppression tuned on held-out training slides.
- Cross-domain import (astronomy source extraction): treat the probability heatmap like a sky image and use blob detection with a local-background model to place detection points.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The leaderboard was computed on 130 test slides; test_049 has since been removed as a duplicate, so the reference now has 129. State the count and recompute any baseline you compare against on 129.
- Some published FROCs also exclude test_114 (e.g. the evaluation script of NCRF, Li and Ping 2018), but test_114 is in reference.csv as a macro-metastasis slide. Compare like with like, and score claims on all 129 slides.
- Test annotations, masks and labels are public: choosing thresholds, epochs or the NMS radius by test FROC is leakage. Use a split of the training slides.
- PatchCamelyon (existing bank entry pcam-patchcamelyon-from-scratch-accuracy) is built from CAMELYON16 slides; using PCam test patches for training leaks test slides.
- Twenty training tumour slides are not exhaustively annotated (README list); treating their unannotated area as negative teaches false negatives.
- Pathology foundation models may have been pretrained on CAMELYON16 test slides; such claims must be flagged and reported in their own class.
- evaluate.py depends on ASAP's multiresolutionimageinterface and reads the masks at a fixed level; detections must be in level-0 coordinates.
- A research benchmark on curated slides; a higher FROC is not evidence of clinical readiness and must not be framed as diagnostic advice.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/disease-research/camelyon16-test-froc-and-slide-auc.md
```

Already set up? Say `run V3R1T4S on camelyon16-test-froc-and-slide-auc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `camelyon16-test-froc-and-slide-auc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
