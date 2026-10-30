# 🧠 Neuroscience

Spike sorting, connectomics, neural imaging and brain-signal decoding benchmarks with released ground truth.

**7 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [MOABB EEG-BCI benchmark: one pipeline that beats the published best within-session score…](moabb-within-session-benchmark-cells.md) | harvest | laptop-hours per dataset (MOABB downloads each public dataset itself; Riemannian pipelines run on a CPU, deep pipelines faster on a GPU) |
| ★★★☆☆ | [FISBe (FlyLight) 3D neuron instance segmentation: beat PatchPerPix's benchmark score S =…](fisbe-flylight-neuron-instance-segmentation.md) | standard | laptop-days (completely-labelled set 7.1 GB, partly-labelled set 14.4 GB of 3-channel ~400x700x700 zarr volumes; a GPU is strongly recommended) |
| ★★★☆☆ | [SpikeForest ground-truth spike sorting: beat the best average accuracy in the SpikeForest…](spikeforest-paired-hybrid-sorter-accuracy.md) | harvest | laptop-hours per study (DANDI 000618 holds 125 NWB files, 145 GB in all; paired_boyden32c is 19 recordings of 32 channels) |
| ★★★☆☆ | [ZAPBench whole-brain zebrafish activity forecasting: beat the best released long-context…](zapbench-whole-brain-forecast-mae.md) | standard | laptop-days (trace-based models use the released ~70k-neuron traces, a few GB; the paper's trace models take about 2 h on one A100, so CPU-only is slow; video models need a cluster) |
| ★★☆☆☆ | [BCI Competition IV dataset 4 (ECoG finger flexion): beat the best published mean correlat…](bci-iv-ds4-ecog-finger-flexion-strict.md) | standard | laptop-hours (3 subjects, 62/48/64 ECoG channels, 400 s training and 200 s test each) |
| ★★☆☆☆ | [CalMS21 mouse social behaviour classification: beat the best test F1 on Task 1 (0.878), T…](calms21-mouse-social-behavior-f1.md) | harvest | laptop-hours (Task 1 pose JSON 457 MB, Task 3 556 MB; frame-level classifiers on keypoints train on a CPU) |
| ★★☆☆☆ | [Neural Latents Benchmark '21 (test data now public): beat the final EvalAI leaderboard's…](nlb21-released-test-cobps.md) | harvest | laptop-hours (each dataset is tens to hundreds of MB of binned spikes on DANDI; transformer or SSM models train in hours on one GPU, slower on CPU) |

← [All categories](../README.md)
