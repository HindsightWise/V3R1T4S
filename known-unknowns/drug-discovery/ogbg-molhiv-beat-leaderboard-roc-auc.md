# OGB ogbg-molhiv: beat the leaderboard's top mean test ROC-AUC under the official protocol

💊 **Drug discovery** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

ogbg-molhiv from the Open Graph Benchmark (Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, Jure Leskovec) asks whether each of 41,127 molecules inhibits HIV replication, with a fixed scaffold split, scored by test ROC-AUC averaged over 10 random seeds with model selection on validation. The leaderboard is led by 'Multi-RF Fusion + Multi-GNN' (Zacharie B., 2026-03-21) at 0.8476 ± 0.0002 (listed with 993,331,107 parameters on an NVIDIA H100), then HyperFusion (Xinwei Zhang, 2024-02-24) at 0.8475 ± 0.0003 (5.9 million parameters, RTX 3080) and PAS+FPs (Xu Wang) at 0.8420. Several top entries combine random forests over molecular fingerprints with GNNs; a fingerprint random forest on its own ('Molecular FP + Random Forest', Luca Hagemeyer, the only CPU entry in the top ten) reaches 0.8208. Can a model without external data beat 0.8476 under the rules?

## What counts as a win

Saved code, seeds and per-seed test predictions such that, using the official ogbg-molhiv scaffold split and the ogb Evaluator, the mean test ROC-AUC over 10 runs with seeds 0-9 (each run's checkpoint or ensemble chosen by validation ROC-AUC only) is STRICTLY GREATER (direction: max) than the top 'Test ROC-AUC' value among no-external-data entries in the ogbg-molhiv table of https://ogb.stanford.edu/docs/leader_graphprop/ re-fetched live immediately before claiming. Only the training split's labels may be used for fitting; no external labelled data or models pretrained on molecular property labels.

## Partial wins

- **p1:** Mean test ROC-AUC over 10 seeds strictly above the second-ranked no-external-data entry, with every component trained on the laptop CPU in under 12 hours total.
- **p2:** A model with fewer than 1 million learned parameters whose 10-seed mean test ROC-AUC beats every leaderboard entry with fewer than 10 million parameters.

## How a win is checked

Install ogb, load PygGraphPropPredDataset or the raw SMILES with the official split, re-run the saved script for 2 of the 10 seeds to confirm per-seed numbers, compute test ROC-AUC with ogb's Evaluator on the saved predictions for all 10 seeds, and check that model selection used validation only (inspect logs). Re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ogb.stanford.edu/docs/leader_graphprop/>

## Sources

- <https://ogb.stanford.edu/docs/leader_graphprop/>
- <https://ogb.stanford.edu/docs/graphprop/>
- <https://github.com/snap-stanford/ogb>
- <https://arxiv.org/abs/2005.00687>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Cheminformatics feature diversity: combine Morgan counts at several radii, MACCS, RDKit 2D descriptors, Avalon and atom-pair fingerprints in rotation forests or extremely randomised trees, then rank-average with a GNN.
- Rank-based losses from information retrieval: optimise AUC directly (LibAUC's AUC-M loss, pairwise ranking with LightGBM's lambdarank objective) since the metric is ROC-AUC.
- Scaffold-split robustness from domain adaptation: reweight training molecules to match the validation scaffold distribution (covariate-shift importance weights).
- Use self-supervision only on the unlabelled molecules of this dataset (allowed, no external labels): masked-atom pretraining or graph contrastive pretraining on the 41k SMILES before fine-tuning.
- Stacking with nested validation: train many diverse base models and fit the blender on validation predictions, then re-check that the same blender, not test-tuned weights, is used for all 10 seeds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Test-set model selection: picking epochs, blend weights or seeds by test ROC-AUC inflates scores; the rules allow validation only.
- Seed games: reporting the best 10 of 50 seeds is not the protocol; seeds 0-9 or the first 10 runs, all reported.
- External data: fingerprints are computed from the molecules themselves and are fine; models pretrained on labelled bioactivity data (ChEMBL, PCBA) count as external data and belong in a different comparison.
- ROC-AUC differences of 0.0001 are within seed noise; the claim must exceed the record mean, and the skeptic should report the standard deviation too.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/drug-discovery/ogbg-molhiv-beat-leaderboard-roc-auc.md
```

Already set up? Say `run V3R1T4S on ogbg-molhiv-beat-leaderboard-roc-auc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ogbg-molhiv-beat-leaderboard-roc-auc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
