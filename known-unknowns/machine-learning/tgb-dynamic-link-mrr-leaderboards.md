# TGB dynamic link prediction (tgbl-wiki-v2, review-v2, coin-v2, comment, flight-v2): beat a leaderboard's top test MRR

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for tgbl-wiki-v2 and tgbl-review-v2; laptop-days or more for coin, comment and flight (23M-67M edges) · open as of 2026-10-30

## The problem

The Temporal Graph Benchmark (Shenyang Huang, Farimah Poursafaei, Jacob Danovitch, Matthias Fey, Weihua Hu, Emanuele Rossi, Jure Leskovec, Michael Bronstein, Guillaume Rabusseau, Reihaneh Rabbany; NeurIPS 2023) scores future-edge prediction on continuous-time graphs. Each true edge is ranked against pre-generated negatives and scored by MRR over 5 runs, in a streaming setting where test edges may update memory but not gradients. Live leaders on 2026-10-30: - tgbl-wiki-v2: TPNet (Xiaodong Lu, Beihang, 2025-08-14) 0.827, then a parameter-free Heuristic(LocalGlobal) by King AI Labs (2026-01-20) 0.821 and HyperEvent (Jian Gao, Xidian) 0.810. - tgbl-review-v2: GraphMixer (TGB team, 2023) 0.521, then CTAN (Alessio Gravina, Pisa, 2025) 0.405. - tgbl-coin-v2: TPNet 0.832, then a heuristic at 0.774. - tgbl-comment: TPNet 0.825, then HyperEvent 0.760. - tgbl-flight-v2: TPNet 0.884, then a heuristic at 0.878. Can a method beat a dataset's top test MRR?

## What counts as a win

For a named dataset D in {tgbl-wiki-v2, tgbl-review-v2, tgbl-coin-v2, tgbl-comment, tgbl-flight-v2}: saved code and seeds such that, with the official chronological split, the official pre-generated validation and test negatives and the tgb package's Evaluator, the mean test MRR over 5 runs (all reported) is STRICTLY GREATER (direction: max) than the highest 'Test MRR' for D at https://tgb.complexdatalab.com/docs/leader_linkprop/, re-fetched live immediately before claiming. Rules (https://tgb.complexdatalab.com/docs/leader_rules/): training edges may be used in any way. Validation edges only for hyperparameter tuning (no gradients) and memory updates. Test edges only for memory updates after each prediction batch, never for gradients or tuning.

## Partial wins

- **p1:** For some dataset D, mean test MRR over 5 runs strictly above the second-highest Test MRR for D on the live board, with all training and evaluation of the 5 runs done on CPU only (no GPU), under the full-win protocol, using a method that is not one of D's listed board entries (re-running or re-training a listed method such as TPNet on CPU does not count).
- **p2:** A method with no gradient-trained parameters whose test MRR on some dataset D is strictly above every training-free entry listed for D on the live board (rows named Heuristic(...), EdgeBank(...) or Base3; on 2026-10-30 the best are 0.821 on tgbl-wiki-v2, 0.108 on tgbl-review-v2, 0.774 on tgbl-coin-v2, 0.723 on tgbl-comment and 0.878 on tgbl-flight-v2).

## How a win is checked

pip install the pinned tgb release and load D with its official negative sampler. Re-run 2 of the 5 runs and recompute MRR with tgb's Evaluator. Read the code to confirm that test edges reach the model only after prediction and only through memory or history updates. Re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://tgb.complexdatalab.com/docs/leader_linkprop/>

## Sources

- <https://tgb.complexdatalab.com/docs/leader_linkprop/>
- <https://tgb.complexdatalab.com/docs/leader_rules/>
- <https://github.com/shenyangHuang/TGB>
- <https://arxiv.org/abs/2307.01026>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Recency and popularity blends from recommender systems (time-decayed item popularity per source node); such heuristics already sit second on wiki, coin and flight.
- tgbl-review-v2 is an outlier where one 2023 model leads by 0.12; study what GraphMixer's link encoder captures and combine it with recency features.
- Point-process ideas (Hawkes intensities per node pair) as cheap scorers or features.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Datasets were re-released as v2 with changed negatives; older v1 numbers in papers are not comparable.
- Negatives must be the official pre-generated ones; random negatives inflate MRR.
- Updating model weights on test edges breaks the streaming rules; only memory or history may change.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/tgb-dynamic-link-mrr-leaderboards.md
```

Already set up? Say `run V3R1T4S on tgb-dynamic-link-mrr-leaderboards`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tgb-dynamic-link-mrr-leaderboards`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
