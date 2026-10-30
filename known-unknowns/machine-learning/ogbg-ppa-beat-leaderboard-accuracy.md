# OGB ogbg-ppa: beat the leaderboard's top test accuracy (0.8258) for classifying protein-association graphs by taxonomic group

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: laptop-days (158,100 graphs averaging 243 nodes and 2,266 edges; GPU strongly helpful) · open as of 2026-10-30

## The problem

ogbg-ppa (Open Graph Benchmark, Hu et al. 2020, built from STRING protein-protein association networks) contains 158,100 undirected graphs. Each is the neighbourhood of a protein in one of 1,581 species, with 7-dim edge features for association types and no node features. The task is to predict which of 37 taxonomic groups the species belongs to. The split is by species (test species are unseen), and the score is test accuracy over at least 10 runs. GatedGCN+ (Yuankai Luo, Lei Shi, Xiao-Ming Wu, PolyU; ICML 2025 'Can Classic GNNs Be Strong Baselines for Graph-level Tasks?'; 2025-02-13) leads at 0.8258 +- 0.0055. Behind it are PAS+F2GNN (Xu Wang, 4Paradigm, 2022) at 0.8201 and ExpC* + bag of tricks (Hao Zhang, 2021) at 0.8140. Can a model beat 0.8258?

## What counts as a win

Saved code, seeds and per-run test predictions such that, on the official ogbg-ppa split with ogb's Evaluator, the mean test accuracy over at least 10 runs (all reported; checkpoints chosen by validation accuracy only) is STRICTLY GREATER (direction: max) than the highest 'Test Accuracy' among 'Ext. data' = 'No' rows of the ogbg-ppa table at https://ogb.stanford.edu/docs/leader_graphprop/, re-fetched live immediately before claiming (0.8258 on 2026-10-30). No external protein data (sequences, other STRING releases, pretrained protein models).

## Partial wins

- **p1:** A model with fewer than 4,000,000 learned parameters whose 10-run mean test accuracy is strictly above 0.8140 (ExpC*+bag of tricks, Hao Zhang, 3,758,642 params, the best entry under 4M on 2026-10-30), under the full-win protocol.
- **p2:** A model with fewer than 1,000,000 learned parameters whose 10-run mean test accuracy is strictly above 0.7500, far above the best sub-1M entry on the board (GCN, 0.6839).

## How a win is checked

Load ogbg-ppa with ogb and re-run 2 seeds from the saved script. Score the saved predictions with ogb.graphproppred.Evaluator('ogbg-ppa'). Check validation-only selection and that nothing is downloaded from outside, count parameters, and re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ogb.stanford.edu/docs/leader_graphprop/>

## Sources

- <https://ogb.stanford.edu/docs/leader_graphprop/>
- <https://ogb.stanford.edu/docs/graphprop/>
- <https://ogb.stanford.edu/docs/leader_rules/>
- <https://arxiv.org/abs/2502.09263>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Graph-kernel and spectral features (Weisfeiler-Lehman subtree counts on edge-type-labelled graphs, Laplacian spectra) fed to gradient-boosted trees, as a CPU baseline and an ensemble member.
- Message passing that leans on edge features: nodes have no features, so the association-type vectors carry most of the signal.
- Ensembles of several seeds of a strong classic GNN with different readouts (mean, attention, virtual node).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Test species are unseen, so tuning on a random split of training graphs overestimates accuracy; use the official validation split.
- Standard deviations are about 0.005. A margin of 0.001 over the leader is within noise and should be reported as such.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/ogbg-ppa-beat-leaderboard-accuracy.md
```

Already set up? Say `run V3R1T4S on ogbg-ppa-beat-leaderboard-accuracy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ogbg-ppa-beat-leaderboard-accuracy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
