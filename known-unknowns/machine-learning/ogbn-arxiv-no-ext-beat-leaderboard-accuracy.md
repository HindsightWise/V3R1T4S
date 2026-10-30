# OGB ogbn-arxiv: beat the top no-external-data test accuracy (0.7611) for arXiv CS subject classification

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (169k nodes, 1.2M edges; CPU training of GNN/MLP+propagation models is feasible) · open as of 2026-10-30

## The problem

ogbn-arxiv (Open Graph Benchmark: Weihua Hu, Matthias Fey, Marinka Zitnik, Yuxiao Dong, Hongyu Ren, Bowen Liu, Michele Catasta, Jure Leskovec) is the citation graph of 169,343 arXiv CS papers with 128-dim word2vec features. The task is the 40-way primary subject area with a time split (train before 2018, validation 2018, test 2019+), scored by test accuracy averaged over at least 10 runs, with model selection on validation. The live leaderboard (81 rows, last entry 2026-02-10) is topped by LLM-text entries marked 'Ext. data: Yes' (SimTeG+TAPE+RevGAT, Keyu Duan, 0.7803). Among entries marked 'No', the best are GIANT-XRT+DRGAT (anonymous_zhang, 0.7611 +- 0.0009, 2022-01-17), LGGNN+LabelReuse+C&S (Shichao Ma, OPPO, 0.7570) and AGDN+BoT+self-KD+C&S (Chuxiong Sun, 0.7431). The top two 'No' rows appear to rely on GIANT-XRT text-derived features: the first says so in its name, and the LGGNN row repeats, number for number, a 'Yes' row named GIANT-XRT+LGGNN+LabelReuse+C&S. The best 'No' entry that plausibly uses only the shipped inputs is therefore AGDN+BoT+self-KD+C&S at 0.7431. The best 'No' entry under 1M parameters is UniMP_v2 (Weiyue Su, PGL, 0.7397, 687,377 params; the 'Yes' row SciBERT & EHGCN reaches 0.7461 with 621,944), and the best CPU entry is PCAPass + XGBoost (Krzysztof Sadowski, Intel, 0.7187). No 'No'-marked entry has improved on 0.7611 since January 2022. Can a model that uses only the shipped ogb inputs beat it?

## What counts as a win

Saved code, seeds and per-run test predictions such that, on the official ogbn-arxiv split loaded via the ogb package and scored with ogb's Evaluator, the mean test accuracy over at least 10 runs (seeds 0-9 or the first 10 runs, all reported; each run's checkpoint chosen by validation accuracy only) is STRICTLY GREATER (direction: max) than the highest 'Test Accuracy' among rows with 'Ext. data' = 'No' in the ogbn-arxiv table at https://ogb.stanford.edu/docs/leader_nodeprop/, re-fetched live immediately before claiming (0.7611 on 2026-10-30). Inputs are limited to what the ogb package ships for ogbn-arxiv (graph, 128-dim features, years, training labels): no raw titles or abstracts, no language-model embeddings and no models pretrained on outside data. Validation labels may be used only as the OGB rules allow (hyperparameter tuning).

## Partial wins

- **p1:** Mean test accuracy over 10 runs of at least 0.7451, i.e. 0.002 above 0.7431, the best 'No'-marked entry on the live board whose name shows no GIANT-XRT or other text-derived features (AGDN+BoT+self-KD+C&S, Chuxiong Sun, 2021-07-22, on 2026-10-30), and strictly above any higher ogbn-arxiv test accuracy from a shipped-inputs-only model found by the NOVELTY check, under the full-win protocol and input restriction.
- **p2:** A model with fewer than 1,000,000 learned parameters whose 10-run mean test accuracy is strictly above every 'No'-marked entry listed with fewer than 1,000,000 parameters (UniMP_v2, 0.7397 on 2026-10-30), under the same protocol.

## How a win is checked

pip install ogb and load the official split. Re-run the saved script for 2 of the 10 seeds and confirm the per-run numbers. Score all saved test predictions with ogb.nodeproppred.Evaluator('ogbn-arxiv'). Check that the logs show checkpoint selection by validation only, grep the code for any raw-text or external-embedding download, count parameters with sum(p.numel()), and re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ogb.stanford.edu/docs/leader_nodeprop/>

## Sources

- <https://ogb.stanford.edu/docs/leader_nodeprop/>
- <https://ogb.stanford.edu/docs/nodeprop/>
- <https://ogb.stanford.edu/docs/leader_rules/>
- <https://github.com/snap-stanford/ogb>
- <https://arxiv.org/abs/2005.00687>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Label propagation tricks from semi-supervised learning: label reuse, Correct-and-Smooth and self-knowledge-distillation stacked on a strong base model. They are behind most of the top 'No' entries.
- Exploit the time split: weight training papers by year, or add year-aware features, since test papers are 2019+ (covariate shift).
- Directed-graph propagation (separate in- and out-citation operators, as in DRGAT and magnetic Laplacians) instead of symmetrising the graph.
- Gradient-boosted trees on multi-hop propagated features (SIGN-style A^k X and propagated training labels), which run on CPU.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Using raw text or LM embeddings moves the entry to the external-data comparison. The input restriction above is stricter than some 'No' labels on the board: the 0.7611 record itself uses GIANT-XRT features.
- Feeding validation labels into label propagation at test time breaks the OGB rule (validation labels only for tuning).
- Test-set checkpoint selection or best-of-many-seeds reporting is not the protocol.
- Differences of 0.001 are within run-to-run noise; report the standard deviation.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/ogbn-arxiv-no-ext-beat-leaderboard-accuracy.md
```

Already set up? Say `run V3R1T4S on ogbn-arxiv-no-ext-beat-leaderboard-accuracy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ogbn-arxiv-no-ext-beat-leaderboard-accuracy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
