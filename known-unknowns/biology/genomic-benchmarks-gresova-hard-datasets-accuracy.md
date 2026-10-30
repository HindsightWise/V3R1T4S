# Genomic Benchmarks (Gresova et al.): beat the best published test accuracy on Human Enhancers Cohn, Human OCR Ensembl or Drosophila Enhancers Stark

🦠 **Biology** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (small CNN/SSM from scratch on sequences of 200-4,700 bp; a fine-tuned 100M+ model needs a GPU for hours) · open as of 2026-10-30

## The problem

Genomic Benchmarks (Katarina Gresova, Vlastimil Martinek, David Cechak, Petr Simecek and Panagiotis Alexiou, BMC Genomic Data 2023; github.com/ML-Bioinfo-CEITEC/genomic_benchmarks) is a pip-installable set of nine DNA sequence-classification datasets with fixed train/test splits: human, mouse and Drosophila enhancers, open chromatin, promoters, regulatory classes and two demo tasks. The README still calls HyenaDNA the SOTA, and the experiments page lists HyenaDNA at Cohn 74.2 and OCR 80.9, but later papers have moved these cells. Best published accuracies found on 2026-10-30: Human Enhancers Cohn 0.763 (GENERator 1.2B, Wei Wu and co-authors, arXiv:2502.07272v5 Table S5, 10-fold CV), then DNABERT-2 0.759 on the official split (MxDNA paper, Lifeng Qiao and co-authors, arXiv:2412.13716) and Caduceus-PS 8M 0.749 (GENERator table). Human OCR Ensembl 0.828 (Caduceus-Ph 470k, Yair Schiff and co-authors, arXiv:2403.03234), with Caduceus-PS 0.826 (GENERator table) and DNA-xLSTM-PH 0.826 (arXiv:2411.04165). Drosophila Enhancers Stark 0.827 (Caduceus-Ph as run in GENERator Table S5; the Caduceus, JanusDNA, ConvNova and Omni-DNA papers omit this dataset). Of the six other datasets, five sit at 0.92-0.98 and mouse enhancers (0.87, high variance) is very small. Models from 0.4M to 1.2B parameters land within about two points of each other on Cohn and OCR, which suggests that label noise or the sequence-only signal is the limit, not scale. Protocols differ (official split with seeds versus cross-validation over the training data), so the criterion uses the official test split and takes the highest published number under any protocol as the bar.

## What counts as a win

Predictions for every sequence of the official test split (genomic_benchmarks package, dataset version 0) of human_enhancers_cohn, human_ocr_ensembl or drosophila_enhancers_stark, from a model trained only on that dataset's official train split (pretrained weights allowed if the corpus is declared; no test labels anywhere), whose test accuracy, recomputed by the skeptic as the mean over at least three training seeds, is STRICTLY HIGHER (direction: max) than the best published accuracy for that dataset by at least 0.01 absolute. Bars as of 2026-10-30: Cohn 0.763, OCR Ensembl 0.828, Drosophila Stark 0.827, so a win needs at least 0.773, 0.838 or 0.837. The bar must also exceed any later published value found by a novelty check immediately before claiming.

## Partial wins

- **p1:** With a model of at most 10M parameters trained from scratch (no pretraining), beat the best published accuracy of any model under 10M parameters on human_enhancers_cohn (0.749, Caduceus-PS 8M, arXiv:2502.07272 Table S5) or human_ocr_ensembl (0.828, Caduceus-Ph 470k, arXiv:2403.03234) by at least 0.01, mean of three seeds on the official test split.
- **p2:** Beat the best published accuracy on any one of the three named datasets by at least 0.005 (mean of three seeds, every seed above the bar) on the official test split.
- **p3:** A reproducible audit of human_enhancers_cohn and human_ocr_ensembl listing every train/test sequence pair at 90% or higher identity (or exact reverse-complement duplicates), with counts, and the accuracy of a stated model on the test split with those sequences removed.

## How a win is checked

Skeptic installs genomic_benchmarks, downloads the dataset's version-0 split, checks that the prediction file covers each test sequence exactly once, computes accuracy per seed, reruns one seed of the attacker's training script, and checks the training data for test sequences (exact and reverse complement). Under an hour for small models.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2502.07272>

## Sources

- <https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks>
- <https://github.com/ML-Bioinfo-CEITEC/genomic_benchmarks/tree/main/experiments>
- <https://arxiv.org/abs/2502.07272>
- <https://arxiv.org/html/2403.03234>
- <https://arxiv.org/html/2412.13716>
- <https://arxiv.org/html/2502.18538>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensemble both strands: reverse-complement averaging at inference is free, and Caduceus-PS shows that RC equivariance helps on OCR.
- Human Enhancers Cohn shows the narrowest spread across model sizes; model label noise explicitly (noise-robust loss, co-teaching) instead of adding parameters.
- Use k-mer and GC/CpG composition features with gradient-boosted trees as a strong cheap baseline and stack them with a CNN.
- Cross-domain import (tabular ML): calibrate with a held-out slice of the training split and select by a paired test across seeds, not by one lucky seed.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several papers (Caduceus, GENERator, JanusDNA) report cross-validation over the training data instead of accuracy on the official test split; numbers across protocols are not strictly comparable, so the criterion fixes the official test split.
- The README still names HyenaDNA as SOTA; that is stale, so do not use it as the bar.
- Large genomic models pretrained on the human reference saw the test regions unlabelled; this is allowed but must be declared.
- drosophila_enhancers_stark is missing from most papers' tables (its bar comes from GENERator's rerun of Caduceus-Ph), so check that any bar quoted is for that dataset.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/genomic-benchmarks-gresova-hard-datasets-accuracy.md
```

Already set up? Say `run V3R1T4S on genomic-benchmarks-gresova-hard-datasets-accuracy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `genomic-benchmarks-gresova-hard-datasets-accuracy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
