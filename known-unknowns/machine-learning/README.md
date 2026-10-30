# 🤖 Machine learning

Small leaderboards and efficiency records a laptop can top with open models run locally.

**27 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [Time series extrinsic regression (TSER archive): beat the best reference regressor's 30-r…](tser-beat-reference-30-resample-best-rmse.md) | harvest | laptop-hours |
| ★★★☆☆ | [OpenOOD v1.5 CIFAR-10/100: a post-hoc OOD detector on the official cross-entropy ResNet-1…](openood-v15-cifar-posthoc-near-ood-auroc.md) | standard | laptop-hours (CPU inference of a 32x32 ResNet-18 over the CIFAR training and test sets and OpenOOD's near/far-OOD test and validation sets, on the order of 10^5 images per checkpoint, for three checkpoints) |
| ★★★☆☆ | [SRBench 2025 black-box: a symbolic regressor that Pareto-dominates the best-accuracy meth…](srbench-2025-blackbox-dominate-leader.md) | harvest | laptop-hours |
| ★★★☆☆ | [Smallest neural network reaching 99% test accuracy on MNIST (record: 697 parameters)](smallest-mnist-99-percent-network.md) | harvest | laptop-hours |
| ★★★☆☆ | [TGB dynamic node affinity (tgbn-trade, genre, reddit, token): beat NAVIS's top test NDCG@…](tgb-dynamic-node-affinity-ndcg-leaderboards.md) | harvest | laptop-minutes for tgbn-trade (255 nodes); laptop-hours for genre and reddit; laptop-days for token (72M edges) |
| ★★★☆☆ | [Tourism forecasting competition (1,311 series): an out-of-sample average MAPE below N-BEA…](tourism-competition-beat-best-published-mape.md) | standard | laptop-hours (1,311 series, under 1 MB) |
| ★★★☆☆ | [UCR univariate time series classification: beat the best reference classifier's 30-resamp…](ucr-tsc-beat-reference-30-resample-best.md) | harvest | laptop-hours |
| ★★★☆☆ | [UEA multivariate time series classification: beat the best published 30-resample mean acc…](uea-multivariate-tsc-beat-published-30-resample-best.md) | harvest | laptop-hours |
| ★★★☆☆ | [fev-bench forecasting: beat the best posted scaled quantile loss on a task with locally r…](fev-bench-beat-best-task-sql.md) | harvest | laptop-hours |
| ★★☆☆☆ | [CIFAR-10 speedrun: 94% mean test accuracy on one A100 faster than Hiverge (1.98 s) and Fu…](cifar10-speedrun-94-single-a100.md) | standard | needs cluster (one rented A100 SXM4 for the timed claim; the FLOP-count partial p3 is laptop-hours on Apple silicon) |
| ★★☆☆☆ | [M3 competition (3,003 series): an out-of-sample average sMAPE below the best published 12…](m3-competition-beat-best-published-smape.md) | standard | laptop-hours (3,003 short series, a few MB) |
| ★★☆☆☆ | [TGB dynamic link prediction (tgbl-wiki-v2, review-v2, coin-v2, comment, flight-v2): beat…](tgb-dynamic-link-mrr-leaderboards.md) | harvest | laptop-hours for tgbl-wiki-v2 and tgbl-review-v2; laptop-days or more for coin, comment and flight (23M-67M edges) |
| ★★☆☆☆ | [M4 competition (100,000 series): an honestly out-of-sample point forecast with overall OW…](m4-competition-beat-nbeats-owa.md) | standard | laptop-days (100,000 series; about 270 MB of CSV in Dataset/Train and Dataset/Test; deep ensembles benefit from a GPU, statistical combinations run on CPU) |
| ★★☆☆☆ | [M5 accuracy competition (Walmart unit sales): beat the winning private WRMSSE 0.52044 wit…](m5-accuracy-beat-winner-wrmsse.md) | standard | laptop-hours to laptop-days (about 450 MB of CSV, 30,490 bottom-level series; LightGBM-style models need 16-32 GB RAM) |
| ★★☆☆☆ | [M5 uncertainty competition: beat the winning private WSPL 0.15420 for nine-quantile Walma…](m5-uncertainty-beat-winner-wspl.md) | standard | laptop-hours to laptop-days (same 450 MB M5 data; quantile models at 12 levels) |
| ★★☆☆☆ | [Modded-NanoGPT track 3 (optimization): reach 3.28 FineWeb val loss with the fixed GPT-2-s…](modded-nanogpt-track3-fewest-steps.md) | standard | needs cluster (one A100/H100 suffices because only steps count, but each run is about 1.4B tokens through a 124M model and n >= 6 runs are needed) |
| ★★☆☆☆ | [Noise: pretraining a fixed 37.7M transformer without backpropagation, below 3.338 val los…](noise-backprop-free-pretraining-records.md) | harvest | needs cluster (8x H100 node; current records take 23 s to 3 h of training, and a Mac run would take days) |
| ★★☆☆☆ | [OGB ogbl-collab: beat the leaderboard's top test Hits@50 (0.7129) for future co-authorshi…](ogbl-collab-beat-leaderboard-hits50.md) | harvest | laptop-hours (235k nodes, 1.3M edges; heuristics run in minutes on CPU) |
| ★★☆☆☆ | [TSB-AD multivariate anomaly detection: beat the leaderboard's best average VUS-PR on the…](tsb-ad-m-beat-leaderboard-vus-pr.md) | harvest | laptop-hours |
| ★★☆☆☆ | [NanoGPT Slowrun: lowest FineWeb val loss from a fixed 100M-token training set (1-hour tra…](nanogpt-slowrun-100m-token-val-loss.md) | harvest | needs cluster (8x H100 node; tiny track 15 min, main track 1 h, two-hour track 2 h, unlimited track used 80 h on 5 nodes) |
| ★★☆☆☆ | [OGB ogbg-ppa: beat the leaderboard's top test accuracy (0.8258) for classifying protein-a…](ogbg-ppa-beat-leaderboard-accuracy.md) | standard | laptop-days (158,100 graphs averaging 243 nodes and 2,266 edges; GPU strongly helpful) |
| ★★☆☆☆ | [OGB ogbl-vessel: beat the leaderboard's top test ROC-AUC (0.9838) for mouse-brain vessel…](ogbl-vessel-beat-leaderboard-roc-auc.md) | standard | laptop-hours (3.5M nodes, 5.3M edges, 3-dim spatial features; 16-32 GB RAM) |
| ★★☆☆☆ | [OGB ogbn-arxiv: beat the top no-external-data test accuracy (0.7611) for arXiv CS subject…](ogbn-arxiv-no-ext-beat-leaderboard-accuracy.md) | harvest | laptop-hours (169k nodes, 1.2M edges; CPU training of GNN/MLP+propagation models is feasible) |
| ★★☆☆☆ | [OGB ogbn-mag: beat the leaderboard's top test accuracy (0.5801) for heterogeneous-graph p…](ogbn-mag-beat-leaderboard-venue-accuracy.md) | standard | laptop-days (1.9M nodes, 21M edges; precomputed-propagation models need about 32 GB RAM, GPU helpful) |
| ★★☆☆☆ | [Parameter Golf (finished): a 16 MB language-model artifact trained in 10 min on 8xH100 th…](parameter-golf-16mb-fineweb-bpb.md) | standard | needs cluster (8x H100 SXM for the 10-minute win and in practice for the unlimited-compute p1; the Mac partial p2 is laptop-days on Apple silicon via train_gpt_mlx.py) |
| ★★☆☆☆ | [TabArena-v0.1: beat the best mean test error of all 94 leaderboard entries on one of the…](tabarena-v01-per-dataset-best-error.md) | harvest | laptop-hours per small dataset (up to 2,400 rows, 30 splits); laptop-days for the 9-split datasets up to 150k rows |
| ★☆☆☆☆ | [Modded-NanoGPT speedrun: train to 3.28 FineWeb val loss on 8xH100 faster than the 39.9 s…](modded-nanogpt-track1-wallclock-record.md) | moonshot | needs cluster (8x H100 node; each attempt costs minutes but needs several runs for p < 0.01) |

← [All categories](../README.md)
