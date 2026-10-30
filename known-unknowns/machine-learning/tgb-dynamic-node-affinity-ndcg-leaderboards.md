# TGB dynamic node affinity (tgbn-trade, genre, reddit, token): beat NAVIS's top test NDCG@10

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-minutes for tgbn-trade (255 nodes); laptop-hours for genre and reddit; laptop-days for token (72M edges) · open as of 2026-10-30

## The problem

TGB's dynamic node property prediction track (Huang et al., NeurIPS 2023) asks, at each time step, for a ranking of a node's future interaction affinities (trade partners, music genres, subreddits, tokens), scored by NDCG@10 in a streaming setting. Simple forecasts are strong: Persistent Forecast and Moving Average (TGB team, 2023) beat learned TGN models on every dataset. NAViS (Or Feldman, Ben-Gurion University, 2025-10-20; arXiv 2510.06940), a trained state-space model, now leads all four boards by small margins: - tgbn-trade: 0.863 vs Persistent Forecast 0.855. - tgbn-genre: 0.528 vs Moving Average 0.509. - tgbn-reddit: 0.569 vs Moving Average 0.559. - tgbn-token: 0.513 vs Moving Average 0.508. TGNv2 (Benedict Aaron Tjandra, Oxford, 2024) is third on genre and reddit and fourth on trade and token. Can a method beat NAVIS on a dataset?

## What counts as a win

For a named dataset D in {tgbn-trade, tgbn-genre, tgbn-reddit, tgbn-token}: saved code and seeds such that, with the official chronological split and the tgb package's node-property Evaluator, the test NDCG@10 (mean over 5 runs if the method is stochastic, all runs reported) is STRICTLY GREATER (direction: max) than the highest 'Test NDCG@10' for D at https://tgb.complexdatalab.com/docs/leader_nodeprop/, re-fetched live immediately before claiming. TGB rules apply. Validation data only for tuning and memory. Test labels are revealed in stream order after each prediction and are never used for gradients or tuning.

## Partial wins

- **p1:** A method with no gradient-trained parameters (persistence, moving-average, exponential-smoothing or similar forecasts, with any constants tuned on validation only) whose test NDCG@10 on some dataset D is strictly above both TGB-team heuristics for D (on 2026-10-30 the better of Persistent Forecast and Moving Average is 0.855 on tgbn-trade, 0.509 on tgbn-genre, 0.559 on tgbn-reddit and 0.508 on tgbn-token), under the full-win protocol.
- **p2:** One fixed no-gradient method of the p1 kind, with one fixed validation-only tuning procedure, that achieves p1 on all four datasets.

## How a win is checked

Install tgb and re-run the saved script on D (all runs if stochastic). Recompute NDCG@10 with tgb's Evaluator. Read the code to check that each test label is used only after its prediction is made and that no tuning used test scores, then re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://tgb.complexdatalab.com/docs/leader_nodeprop/>

## Sources

- <https://tgb.complexdatalab.com/docs/leader_nodeprop/>
- <https://tgb.complexdatalab.com/docs/leader_rules/>
- <https://github.com/shenyangHuang/TGB>
- <https://arxiv.org/abs/2307.01026>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Forecasting methods from econometrics and demand planning: exponential smoothing with a tuned decay per node, Croston's method for intermittent affinities, and persistence/moving-average blends chosen on validation.
- Gravity-model features for tgbn-trade: international trade flows follow partner size and distance.
- Learn only a small correction on top of the moving-average forecast (a residual model), which keeps the strong baseline as a floor.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Using the label at time t to predict time t (an off-by-one in the stream) gives impossible scores; check the evaluation loop.
- Smoothing constants tuned on test NDCG are test tuning; tune on validation only.
- Margins at the top are 0.005-0.02; report exact unrounded scores.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/tgb-dynamic-node-affinity-ndcg-leaderboards.md
```

Already set up? Say `run V3R1T4S on tgb-dynamic-node-affinity-ndcg-leaderboards`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tgb-dynamic-node-affinity-ndcg-leaderboards`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
