# NASA/IBM HLS multi-temporal crop segmentation (US, CDL 2022): beat 55.1 mIoU (InstaGeo's fine-tuned Prithvi-EO-2.0-300M) on the official validation split

🌍 **Earth and sky** · standard · tractability ★★★☆☆ · compute: laptop-hours (3,854 chips of 224x224x18 at 30 m; about 10.6 GB training and 1.2 GB validation archives) · open as of 2026-10-30

## The problem

The Multi-Temporal Crop Classification dataset (Cecil, Kordi, Li, Khallaghi and Alemohammad, 2023; NASA IMPACT, IBM and Clark University; Hugging Face ibm-nasa-geospatial/multi-temporal-crop-classification, CC-BY-4.0) has 3,854 Harmonized Landsat-Sentinel S30 chips from across the contiguous US in 2022. Each chip has three growing-season observations of 6 bands (18 channels). Labels are 13 USDA Cropland Data Layer classes (natural vegetation, forest, corn, soybeans, wetlands, developed/barren, open water, winter wheat, alfalfa, fallow/idle, cotton, sorghum, other), with 0 meaning no data. Chips are randomly split 80/20 into training (3,083) and validation (771), as listed in training_data.txt and validation_data.txt. The validation split is the evaluation split used to benchmark the Prithvi foundation models. The Prithvi-EO-2.0 paper (Szwarcman et al., arXiv:2412.02732 v3, Mar 2026, Table IX) reports mIoU: U-Net 42.6, Prithvi-EO-1.0-100M 42.7, Prithvi-EO-2.0-300M 48.6, Prithvi-EO-2.0-600M 50.7. InstaGeo (Yusuf, Houndayi, Oualha, Cherif, Panford-Quainoo and colleagues, InstaDeep; arXiv 2510.05617, Oct 2025) retrains on this benchmark with its own pipeline. Prithvi-EO-1.0-100M trained on the original chips reaches 48.07 (Table 1). Vanilla fine-tuned Prithvi-EO-2.0-300M reaches 55.10 (Table 2, from the replica experiments; InstaGeo's replica of this dataset reproduces the original within 0.2 points). Its headline 60.65 comes from an expanded 14,061-chip dataset with its own test split and is a different task. A better training recipe for a public encoder therefore already clears 50.7, so the bar that counts is 55.1. The small size makes this a laptop-scale crop-type mapping benchmark. Open task: strictly above 55.1 mIoU on the official validation chips.

## What counts as a win

A trained model (code, config, weights, at least 3 seeds), trained only on the chips in training_data.txt, with any model selection done on a held-out subset of the training chips. No validation chip is used for training, early stopping or hyperparameter choice. The skeptic computes mIoU on all chips in validation_data.txt: per-class IoU from the dataset-level confusion matrix over the 13 classes, ignoring label 0, then the unweighted mean. The mean over seeds must be STRICTLY HIGHER (direction: max) than 55.1 (InstaGeo's vanilla fine-tuned Prithvi-EO-2.0-300M, arXiv 2510.05617 Table 2) by at least 0.5. It is then also above the 50.7 of Prithvi-EO-2.0-600M on this split. It must also beat any mIoU on this split published since (Prithvi-EO-2.0 v3 and InstaGeo checked on 2026-10-30; search papers using this dataset before claiming). Pretrained encoders are allowed if declared.

## Partial wins

- **p1:** Mean mIoU over 3 seeds strictly above 48.6 (Prithvi-EO-2.0-300M) with a model of under 50M parameters trained in under 12 laptop-hours.
- **p2:** Mean mIoU over 3 seeds strictly above 48.6 with no pretrained weights at all (from-scratch model), against the 42.6 U-Net baseline.
- **p3:** Mean mIoU over 3 seeds strictly above 51.2 (the 50.7 of Prithvi-EO-2.0-600M, the best value published on the official chips themselves, plus 0.5), under the same no-validation-tuning rule.

## How a win is checked

The skeptic downloads validation_chips.tgz and validation_data.txt from Hugging Face, re-runs inference from the released weights, and scores with a standalone confusion-matrix script (label 0 ignored), reporting per-class IoU. They also check the training file list against validation_data.txt for overlap. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2412.02732>

## Sources

- <https://huggingface.co/datasets/ibm-nasa-geospatial/multi-temporal-crop-classification>
- <https://arxiv.org/abs/2412.02732>
- <https://arxiv.org/abs/2510.05617>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: temporal-attention segmentation (U-TAE or TSViT-style) that treats the 18 channels as 3 dates x 6 bands rather than one stacked image.
- Fine-tune Prithvi-EO-2.0-600M or TerraMind with stronger decoders (UPerNet) and test-time augmentation. Freezing versus fine-tuning matters here.
- Cross-domain import (agronomy): add crop-calendar features (NDVI and NDWI trajectories, phenology metrics) as extra channels. Corn, soybean and sorghum separate mainly by timing.
- Cross-domain import (long-tail classification): logit adjustment or class-balanced losses for rare classes (sorghum, cotton, fallow), which dominate the mIoU gap.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- There is no separate test split. The validation split is the benchmark, so any tuning on it invalidates the claim.
- mIoU conventions differ (including or excluding class 0, per-image versus dataset-level IoU). State and use the convention above, and when comparing with 50.7, note any difference in the Prithvi config.
- CDL labels are themselves model outputs with class-dependent errors. Small gains on noisy classes may be label noise.
- Random 80/20 chip splits leave spatial autocorrelation between train and validation. Report results honestly, but do not claim generalisation beyond this split.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/hls-multitemporal-crop-cdl-miou.md
```

Already set up? Say `run V3R1T4S on hls-multitemporal-crop-cdl-miou`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hls-multitemporal-crop-cdl-miou`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
