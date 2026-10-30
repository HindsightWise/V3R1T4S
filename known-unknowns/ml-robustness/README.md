# 🛡️ ML robustness

Stronger attacks and soundness counterexamples on public, locally run benchmark models.

**12 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★☆☆ | [ARCH-COMP AINNCS 2D Spacecraft Docking: verify or falsify the neural controller on the fu…](arch-comp-ainncs-docking-full-initial-set.md) | standard | laptop-hours (falsification search: millions of exact closed-loop simulations per hour on CPU; sound verification by box splitting with a reachability tool or an interval certificate: hours) |
| ★★★☆☆ | [MadryLab MNIST challenge (white-box, Linf 0.3): push the secret model's accuracy below th…](madry-mnist-challenge-whitebox-below-leader.md) | harvest | laptop-hours |
| ★★★☆☆ | [RobustBench CIFAR-100 Linf (eps 8/255): lower a listed model's robust accuracy below the…](robustbench-cifar100-linf-beat-autoattack.md) | harvest | laptop-hours |
| ★★★☆☆ | [TRADES MNIST white-box leaderboard (Linf 0.3): push the TRADES SmallCNN's robust accuracy…](trades-mnist-smallcnn-whitebox-below-leader.md) | harvest | laptop-hours |
| ★★★☆☆ | [VNN-COMP 2026: a validated counterexample for a benchmark instance that no participating…](vnncomp-2026-unsolved-instance-counterexample.md) | harvest | laptop-hours |
| ★★☆☆☆ | [ARCH-COMP AINNCS CartPole (Balancing): verify or falsify 1e-3 settling of the neural cont…](arch-comp-ainncs-cartpole-full-initial-set.md) | standard | laptop-hours (falsification: fast simulation of 500 control steps per trajectory; sound verification over 10 s with a 50 Hz controller: hours to days of reachability with splitting) |
| ★★☆☆☆ | [Deterministic Linf certified accuracy records (MNIST 0.1/0.3, CIFAR-10 2/255 and 8/255, T…](linf-certified-training-accuracy-records.md) | standard | laptop-days (MNIST cells: CPU or Apple-GPU training of a CNN7-class network with IBP-based losses, then IBP/CROWN on all 10,000 test images and alpha-beta-CROWN on the residue); needs cluster for the CIFAR-10 and TinyImageNet cells (GPU-days of training and certification) |
| ★★☆☆☆ | [MadryLab CIFAR-10 challenge (white-box, Linf 8/255): push the secret model's accuracy bel…](madry-cifar10-challenge-whitebox-below-leader.md) | harvest | laptop-hours |
| ★★☆☆☆ | [RobustBench CIFAR-10 L2 (eps 0.5): lower a listed model's robust accuracy below the leade…](robustbench-cifar10-l2-beat-autoattack.md) | standard | laptop-hours |
| ★★☆☆☆ | [RobustBench CIFAR-10 Linf (eps 8/255): a stronger attack that lowers a listed model's rob…](robustbench-cifar10-linf-beat-autoattack.md) | harvest | laptop-hours |
| ★★☆☆☆ | [RobustBench ImageNet Linf (eps 4/255): lower a listed model's robust accuracy below the b…](robustbench-imagenet-linf-beat-autoattack.md) | harvest | laptop-days (ResNet-18/50-sized models on the 5,000-image evaluation set at 224 px on CPU; the large Swin/ConvNeXt entries need a GPU); the ImageNet validation set must be obtained by the human under ImageNet's terms |
| ★★☆☆☆ | [VNN-COMP verifier soundness: a validated counterexample for an instance that a participat…](vnncomp-verifier-holds-soundness-counterexample.md) | harvest | laptop-hours |

← [All categories](../README.md)
