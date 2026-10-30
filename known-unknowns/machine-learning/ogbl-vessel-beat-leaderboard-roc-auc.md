# OGB ogbl-vessel: beat the leaderboard's top test ROC-AUC (0.9838) for mouse-brain vessel link prediction

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: laptop-hours (3.5M nodes, 5.3M edges, 3-dim spatial features; 16-32 GB RAM) · open as of 2026-10-30

## The problem

ogbl-vessel (contributed to OGB by Johannes C. Paetzold et al., NeurIPS 2021 Datasets and Benchmarks) is the whole-mouse-brain vessel graph. Nodes are bifurcation points with (x, y, z) coordinates in Allen atlas space, and edges are vessels. Edges are split 80/10/10 at random with spatially sampled negatives, scored by test ROC-AUC. GAV (Bastian Wittmann, UZH, 2023-03-28) leads at 0.9838 +- 0.0002 with only 8,194 parameters, then SIEG(SPG) (anonymous, 2023) at 0.9687 and MLP+DiffPredictor (Chuxiong Sun) at 0.9414. Recent parameter-free CPU entries are far below: DRESS (Eduar Castrillo Velilla, 2026-04-22) at 0.7476 and the Homogeneity Index (Mehrdad Rafiepour, 2025) at 0.5460. Can a model beat 0.9838?

## What counts as a win

Saved code, seeds and per-run test scores such that, on the official ogbl-vessel split with ogb's Evaluator (ROC-AUC on the official test positives and negatives), the mean test ROC-AUC over at least 10 runs (all reported; checkpoints chosen on validation only) is STRICTLY GREATER (direction: max) than the highest 'Test ROC-AUC' among 'Ext. data' = 'No' rows of the ogbl-vessel table at https://ogb.stanford.edu/docs/leader_linkprop/, re-fetched live immediately before claiming (0.9838 on 2026-10-30). No validation or test edges may be inputs, and only data shipped by ogb for ogbl-vessel may be used.

## Partial wins

- **p1:** A model with fewer than 8,194 learned parameters (fewer than GAV) whose 10-run mean test ROC-AUC is strictly above 0.9687 (SIEG(SPG), the second-ranked entry on 2026-10-30), under the full-win protocol.
- **p2:** A method with no gradient-trained parameters whose test ROC-AUC is strictly above 0.85, beating every parameter-free entry on the live board (best: DRESS, 0.7476 on 2026-10-30).

## How a win is checked

Load ogbl-vessel with ogb and re-run 2 runs from the saved script. Score the saved test scores with ogb.linkproppred.Evaluator('ogbl-vessel'). Check that only training edges form the message-passing graph and that selection used validation, then re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ogb.stanford.edu/docs/leader_linkprop/>

## Sources

- <https://ogb.stanford.edu/docs/leader_linkprop/>
- <https://ogb.stanford.edu/docs/linkprop/>
- <https://ogb.stanford.edu/docs/leader_rules/>
- <https://github.com/jocpae/VesselGraph>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Geometry first: edge length, direction and local vessel-tree statistics from the coordinates, fed to gradient-boosted trees, then a small GNN (GAV wins with 8k parameters).
- Biological priors from vascular anatomy: bifurcation points have low degree (about 3), so score candidate edges by how they change local degree and angle distributions.
- Spatial negatives are close to positives; train with hard, spatially sampled negatives that match the evaluation sampler.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Train with negatives drawn like the official spatially sampled ones. A model trained only on uniformly random negatives separates random pairs easily but scores much lower on the official validation and test negatives.
- Only training edges may form the message-passing graph or feed degree and neighbourhood features; computing them on the full edge set leaks validation and test edges.
- The score is ROC-AUC averaged over runs; a single lucky run is not the protocol.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/ogbl-vessel-beat-leaderboard-roc-auc.md
```

Already set up? Say `run V3R1T4S on ogbl-vessel-beat-leaderboard-roc-auc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ogbl-vessel-beat-leaderboard-roc-auc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
