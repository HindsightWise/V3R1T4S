# OGB ogbn-mag: beat the leaderboard's top test accuracy (0.5801) for heterogeneous-graph paper venue prediction

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: laptop-days (1.9M nodes, 21M edges; precomputed-propagation models need about 32 GB RAM, GPU helpful) · open as of 2026-10-30

## The problem

ogbn-mag (Open Graph Benchmark, Hu et al. 2020) is a heterogeneous subgraph of the Microsoft Academic Graph: 736,389 papers (128-dim word2vec features), 1,134,649 authors, 8,740 institutions and 59,965 fields of study, with four relation types. The task is the 349-way venue of each paper with a time split (train before 2018, validation 2018, test 2019+), scored by test accuracy over 10 runs. The leaderboard is still moving. HGAMLP-HOPE (Wei Zhou, HUST, 2026-01-11) leads at 0.5801 +- 0.0012, ahead of gHAWK (Bloom+TransE) (Fatima Farooq, UT Arlington, 2025-12-24) at 0.5797 +- 0.0038, HGAMLP+LP+MS with LINE embeddings (Yuxuan Liang, PKU-Tencent, 2025-05-13) at 0.5794 and LMSPS (Chao Li, HUST, 2024) at 0.5784. All four are marked 'Ext. data: No' and lie within 0.0017 of each other. Can a model beat 0.5801?

## What counts as a win

Saved code, seeds and per-run test predictions such that, on the official ogbn-mag split (ogb package) scored with ogb's Evaluator, the mean test accuracy over at least 10 runs (seeds 0-9 or the first 10 runs, all reported; checkpoints chosen by validation accuracy only) is STRICTLY GREATER (direction: max) than the highest 'Test Accuracy' among 'Ext. data' = 'No' rows of the ogbn-mag table at https://ogb.stanford.edu/docs/leader_nodeprop/, re-fetched live immediately before claiming (0.5801 on 2026-10-30). Only data shipped by ogb for ogbn-mag may be used. Structural embeddings (LINE, TransE, metapath2vec) computed from that graph alone are allowed. Validation labels only for tuning, per the OGB rules.

## Partial wins

- **p1:** A model with fewer than 8,000,000 learned parameters (structural embeddings counted as parameters) whose 10-run mean test accuracy is strictly above 0.5773 (RpHGNN+LP+CR (LINE embs), Jun Hu, 7,720,368 params, the best listed entry under 8M on 2026-10-30), under the full-win protocol.
- **p2:** A model with fewer than 5,000,000 learned parameters (structural embeddings counted as parameters) whose 10-run mean test accuracy is strictly above 0.5752 (PSHGCN, Mingguo He, 4,852,434 params, the best listed entry under 5M on 2026-10-30), under the full-win protocol.

## How a win is checked

Load ogbn-mag with ogb. Re-run 2 of the 10 seeds from the saved script, including the embedding precomputation. Score all saved predictions with ogb.nodeproppred.Evaluator('ogbn-mag'), confirm validation-only selection from the logs, count parameters including any learned embedding tables, and re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ogb.stanford.edu/docs/leader_nodeprop/>

## Sources

- <https://ogb.stanford.edu/docs/leader_nodeprop/>
- <https://ogb.stanford.edu/docs/nodeprop/>
- <https://ogb.stanford.edu/docs/leader_rules/>
- <https://arxiv.org/abs/2005.00687>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Metapath feature precomputation (SeHGNN/HGAMLP style) plus multi-stage label propagation, then ensembling diverse metapath subsets.
- Knowledge-graph embeddings (TransE, RotatE) of the full heterogeneous graph as extra features for authors and fields, which have no features of their own.
- Venue priors from author history: the share of each author's training papers per venue is a strong, cheap feature.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Leaderboard differences at the top are smaller than one standard deviation. A claim must beat the mean, and the skeptic reports the spread.
- Label-propagation features must use training labels only; validation-paper labels may not be inputs.
- Embeddings trained with any test-paper labels leak; the structural embedding objective must be label-free.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/ogbn-mag-beat-leaderboard-venue-accuracy.md
```

Already set up? Say `run V3R1T4S on ogbn-mag-beat-leaderboard-venue-accuracy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ogbn-mag-beat-leaderboard-venue-accuracy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
