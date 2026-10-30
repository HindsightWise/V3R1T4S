# scTab cross-tissue cell-type annotation: beat macro F1 0.8441 on the CELLxGENE donor-held-out test split (164 cell types)

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: needs cluster or a GPU workstation (22.2M cells; the processed train/val/test archive is 164 GB; inference on the 3.45M test cells fits on one GPU) · open as of 2026-10-30

## The problem

scTab (Felix Fischer, David S. Fischer, Roman Mukhin, Andrey Isaev, Evan Biederstedt, Alexandra-Chloe Villani and Fabian J. Theis, Nature Communications 15, 6611, 2024; github.com/theislab/scTab) turned the CELLxGENE census (version 2023-05-15) into a fixed annotation benchmark: 22.2 million human 10x cells from 5,052 donors and 56 tissues, 164 Cell Ontology labels, with test and validation holdouts defined by donor (15,240,192 train, 3,500,032 validation, 3,448,832 test cells), so classifiers must generalise to unseen people. A prediction counts as correct if it equals the author's label or is a descendant of it in the Cell Ontology (docs/classification-evaluation-metrics.md). The processed train/val/test archive (164 GB), a 0.5 GB minimal subset and all checkpoints (8.1 GB) are posted. Macro F1 on the donor-held-out test set in the scTab paper: scTab 0.8295 +/- 0.0007 (default size), 0.8323 +/- 0.0010 for the largest scTab variant (16.2M parameters, Fig. 2f), XGBoost 0.8127, MLP 0.7971, optimised logistic regression 0.7848, CIForm 0.766, fine-tuned scGPT 0.749, CellTypist 0.7304 and a linear probe on scGPT embeddings 0.7301; on 31 coarse labels scTab reaches 0.897. The best published value on this split found on 2026-10-30 is later: S. Cultrera di Montesano, D. D'Ascenzo, S. Raghavan, A. P. Amini, P. S. Winter and L. Crawford (Nature Computational Science 6, 243-249, 2026; github.com/microsoft/hce-classification) retrained TabNet with scTab's hyperparameters and standard cross-entropy on the same donor split and evaluation rule and report in-distribution macro F1 0.8441 (mean of four runs: 0.8453, 0.8449, 0.8430, 0.8431; Source Data Fig. 1d), with MLP 0.8213 and linear 0.7972; their hierarchical cross-entropy loss is evaluated only out of distribution. Single-cell foundation models fine-tuned on this split have so far not beaten a tabular nonlinear model, so the bar is a clean, testable claim. Credit: Fischer, Fischer, Mukhin, Isaev, Biederstedt, Villani, Theis; Cultrera di Montesano, D'Ascenzo, Raghavan, Amini, Winter, Crawford.

## What counts as a win

Cell-type predictions for every cell of the scTab test partition (merlin_cxg_2023_05_15_sf-log1p, test split as released), from a model trained only on the scTab training partition (validation for selection; pretrained single-cell models allowed only if their pretraining corpus is declared, and never with test-cell labels), whose macro F1 over the 164 labels, computed by the skeptic with scTab's evaluation code (docs/classification-evaluation-metrics.md, notebooks/model_evaluation, including its descendant-counts-correct rule), is STRICTLY HIGHER (direction: max) than 0.8441 (TabNet with standard cross-entropy, mean of four runs, Cultrera di Montesano et al., Nature Computational Science 6:243-249, 2026, Source Data Fig. 1d) by at least 0.01 (that is, at least 0.8541), as the mean over at least three seeds, and higher than any later published value on this split found by a novelty check immediately before claiming (including the scTab paper's 0.8323, Cultrera di Montesano et al. 2026 and any follow-up from github.com/microsoft/hce-classification, and Richter et al., Nature Machine Intelligence 2025 / bioRxiv 2024.02.16.580624, which uses the scTab data).

## Partial wins

- **p1:** Macro F1 STRICTLY HIGHER than 0.8441 by any margin on the scTab test partition, mean of three seeds with every seed above 0.8441.
- **p2:** A frozen single-cell foundation-model embedding (scGPT, Geneformer or another declared model) with at most a two-layer head trained on the scTab train partition that beats XGBoost's 0.8127 macro F1 on the test partition.
- **p3:** On the paper's 31 coarse labels (its published mapping), macro F1 STRICTLY HIGHER than 0.897 by at least 0.01, mean of three seeds.

## How a win is checked

Skeptic downloads the released test partition, checks that predictions cover every test cell once with labels from the 164-label vocabulary, computes macro F1 with scTab's code, reruns inference from the attacker's checkpoint, and checks the attacker's data loader reads only the train and validation partitions. Hours on one GPU for inference.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.nature.com/articles/s43588-025-00945-z>

## Sources

- <https://www.nature.com/articles/s41467-024-51059-5>
- <https://github.com/theislab/scTab>
- <https://www.nature.com/articles/s43588-025-00945-z>
- <https://github.com/microsoft/hce-classification>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Hierarchical classification over the Cell Ontology (predict the parent, then refine) can lift macro F1 on rare fine subtypes, where most of the error sits.
- Cross-domain import (long-tail vision): logit adjustment or class-balanced losses for the many rare cell types, which macro F1 weights equally.
- Ensembling scTab with XGBoost, whose errors may differ, is a cheap first experiment, using the released checkpoints.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- CELLxGENE-pretrained foundation models may have seen the test donors' expression unlabelled; declare it, and never use their labels.
- Label granularity differs across studies (B cell versus naive B cell); the benchmark's mapping is fixed, and remapping labels is not allowed. scTab's metric counts a prediction of a descendant of the author's label as correct; scores computed without that rule are not comparable.
- The minimal 0.5 GB subset is for debugging; scores on it are not comparable with the full test partition.
- The scTab paper's 0.8323 is no longer the best published value: a plain TabNet retrained in Cultrera di Montesano et al. (2026) already reaches 0.8441 on the same split, so beating 0.8323 is not new.
- On 2026-10-30 pklab.med.harvard.edu answered scripted downloads with an Imperva/Incapsula bot-check page. Do not get around it: download in a browser as a human step, or rebuild the split from CELLxGENE census 2023-05-15 (LTS) with notebooks/store_creation/01_create_train_val_test_splits.ipynb and check the 15,240,192 / 3,500,032 / 3,448,832 cell counts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/sctab-cellxgene-donor-holdout-macro-f1.md
```

Already set up? Say `run V3R1T4S on sctab-cellxgene-donor-holdout-macro-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sctab-cellxgene-donor-holdout-macro-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
