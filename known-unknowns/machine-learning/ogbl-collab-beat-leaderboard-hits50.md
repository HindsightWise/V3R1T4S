# OGB ogbl-collab: beat the leaderboard's top test Hits@50 (0.7129) for future co-authorship prediction

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (235k nodes, 1.3M edges; heuristics run in minutes on CPU) · open as of 2026-10-30

## The problem

ogbl-collab (Open Graph Benchmark, Hu et al. 2020) is a co-authorship graph of 235,868 MAG authors with 128-dim features. Edges until 2017 are for training, 2018 for validation and 2019 for test. Each true 2019 collaboration is ranked against 100,000 random negatives and scored by Hits@50, averaged over at least 10 runs. Uniquely among OGB datasets, validation edges may be used for training and as input once hyperparameters are fixed. The leaderboard (31 rows) is led by HyperFusion (Xinwei Zhang, Tsinghua, 2024-02-24) at 0.7129 +- 0.0018. Next come GIDN@YITU (Zixiao Wang, Yu Zhang, 2022) at 0.7096, PLNLP + SIGN (Liang Yao, Tencent) at 0.7087 and the CPU-trained HOP-REC (Bo-Yu Lin) at 0.7012. A parameter-free heuristic, AA-DC (Daisuke Hirota, 2026-02-07), reaches 0.6802 on CPU. Can a model beat 0.7129?

## What counts as a win

Saved code, seeds and per-run test scores such that, on the official ogbl-collab split with ogb's Evaluator (Hits@50 against the official test negatives), the mean test Hits@50 over at least 10 runs (seeds 0-9 or the first 10 runs, all reported) is STRICTLY GREATER (direction: max) than the highest 'Test Hits@50' among 'Ext. data' = 'No' rows of the ogbl-collab table at https://ogb.stanford.edu/docs/leader_linkprop/, re-fetched live immediately before claiming (0.7129 on 2026-10-30). Hyperparameters must be fixed using validation edges before those edges are added to the training graph, as the OGB rules require. No test edges may be used as input.

## Partial wins

- **p1:** A method trained and evaluated entirely on CPU (no GPU) whose 10-run mean test Hits@50 is strictly above 0.7012 (HOP-REC, Bo-Yu Lin, the best CPU-trained entry on the board on 2026-10-30), under the full-win protocol.
- **p2:** A method with no gradient-trained parameters (a deterministic graph heuristic or closed-form score) whose test Hits@50 is strictly above the best zero-parameter entry on the live board (AA-DC, 0.6802 on 2026-10-30).

## How a win is checked

Load ogbl-collab with ogb and re-run the saved script for 2 seeds. Check in the code that hyperparameters are frozen before validation edges join the graph and that test edges never enter the input. Score the saved positive and negative test scores with ogb.linkproppred.Evaluator('ogbl-collab'), and re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ogb.stanford.edu/docs/leader_linkprop/>

## Sources

- <https://ogb.stanford.edu/docs/leader_linkprop/>
- <https://ogb.stanford.edu/docs/linkprop/>
- <https://ogb.stanford.edu/docs/leader_rules/>
- <https://arxiv.org/abs/2005.00687>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Time-decayed common-neighbour and Adamic-Adar scores (recent collaborations matter more), blended with a learned model by validation tuning.
- Use the edge-year and edge-weight metadata explicitly; many GNN entries discard it.
- Recommender-systems methods (HOP-REC is one) and random-walk augmentation, both CPU-friendly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Adding validation edges before the hyperparameter search is fixed breaks the one exception the rules allow.
- Some entries report validation Hits@50 of 1.0 because validation edges were in the training graph; compare on test only.
- Duplicate (multi-year) edges inflate degree heuristics; handle the multigraph the same way for validation and test.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/ogbl-collab-beat-leaderboard-hits50.md
```

Already set up? Say `run V3R1T4S on ogbl-collab-beat-leaderboard-hits50`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ogbl-collab-beat-leaderboard-hits50`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
