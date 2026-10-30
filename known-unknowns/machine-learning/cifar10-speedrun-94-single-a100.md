# CIFAR-10 speedrun: 94% mean test accuracy on one A100 faster than Hiverge (1.98 s) and Fulcrum's Fable-5 E1 recipe (1.828 s), or 96% under 27.3 s

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: needs cluster (one rented A100 SXM4 for the timed claim; the FLOP-count partial p3 is laptop-hours on Apple silicon) · open as of 2026-10-30

## The problem

How fast can a network be trained from scratch to 94% accuracy on the 10,000-image CIFAR-10 test set? The time is the mean over 200 runs, the run timer includes test-time augmentation, and the runs use a single NVIDIA A100. Prior work: David Page's myrtle.ai series (26 V100-seconds) and tysam-code's hlb-CIFAR10 (6.3 A100-seconds). Keller Jordan's airbench (arXiv 2404.00498) then set 3.83 s with airbench94, 3.09 s with the compiled version and 2.59 s with airbench94_muon.py (94.01%, 0.29 PFLOPs, Muon optimizer). It also set 96% in 27.3 s with airbench96_faster.py (3.1 PFLOPs, data filtering) and 95% in 10.4 s with the legacy airbench95. The 94% record listed on GitHub belongs to Hiverge ('the Hive', an automated research system): hiverge/cifar10-speedrun, cifar10_speedrun.py, 94.02% mean accuracy in 1.98 s on an A100 SXM4 80GB from RunPod with PyTorch 2.4.0, reached over PRs #2-#6 in Sep-Oct 2025. The changes were vectorised batched Muon, vectorised crops, brightness/contrast augmentation, a compiled step and confidence-gated TTA. The airbench README now says it is no longer the fastest and links to Hiverge. A faster result appears in neither repository. Fulcrum Research (Kaivu Hariharan, Rowan Huang, Uzay Girit and Leni Shor; github.com/fulcrumresearch/cifar-10-speedrun, blog post 2026-07-09) report that recipe E1 (fable-100m/recipes/e1_1.74s_single-gpu_CHAMPION.py) reaches 94% in a mean of 1.828 s against Hiverge's 1.978 s, over 200 trials each on Modal A100s. E1 was written by an autoresearch run of the Fable-5 model seeded with Hiverge's script, and gains mainly from a 24-28-32 px progressive-resolution curriculum and a global max-pool. Their harness times per-trial setup plus training and leaves the standard 6-view TTA evaluation untimed, so its numbers are not on Hiverge's clock. Their audit also excluded the agent's off-the-clock tricks: moving work into untimed setup, picking fast hosts and cooling the GPU before the timer. Checked 2026-10-30: Hiverge has no commits since 2025-10-17, the only open item is a torch-bump bot PR (#7), the Fulcrum repository has not changed since 2026-07-06, and the airbench issues hold no faster claim. On airbench issue #5 (2025-10-31), Keller Jordan said the reported airbench time is the min/best, while Hiverge's script prints the mean over runs.

## What counts as a win

A single self-contained PyTorch training script that, run on one NVIDIA A100 SXM4 (400 W) with no external data and no pretrained weights, trains from scratch on the 50,000 CIFAR-10 training images only. Over at least 200 consecutive runs after one untimed warm-up run, with no run selection, it must give (1) a mean test accuracy >= 94.00% on the official 10,000-image test set (TTA allowed, as in the records) and (2) a mean per-run time, measured with CUDA events as in cifar10_speedrun.py from the start of all per-run work (whitening initialisation, any augmented-batch preparation, training) to the end of the final test-set inference, that is STRICTLY LESS (direction: min) than 1.98 s. It must also be strictly less than the mean times of hiverge's cifar10_speedrun.py and of Fulcrum's E1 recipe (fulcrumresearch/cifar-10-speedrun, fable-100m/recipes/e1_1.74s_single-gpu_CHAMPION.py), both re-timed by the skeptic on the same machine and software stack with the same timer bracket and the same inter-run protocol. It must also beat any faster entry found when the live status source (https://github.com/hiverge/cifar10-speedrun), the airbench README and the Fulcrum repository are re-checked before claiming.

## Partial wins

- **p1:** 96% target: mean test accuracy >= 96.00% over at least 50 consecutive runs with a mean per-run time on one A100 strictly below airbench96_faster.py re-timed on the same machine (27.3 s in its README).
- **p2:** 95% target: mean test accuracy >= 95.00% over at least 100 consecutive runs with a mean per-run time on one A100 strictly below the legacy airbench95.py re-timed on the same machine (10.4 s in the README).
- **p3:** Hardware-free variant: mean test accuracy >= 94.00% over at least 200 runs (Apple silicon MPS or CPU allowed) using strictly fewer total FLOPs per run (training plus final inference, counted with torch.utils.flop_counter.FlopCounterMode) than airbench94_muon.py, hiverge's cifar10_speedrun.py and Fulcrum's E1 recipe, all counted the same way by the skeptic.

## How a win is checked

Clone the claimant's script and run it on a fresh A100 SXM4 instance (PyTorch 2.4.x), discarding one warm-up run, for 200 runs. Record mean accuracy and mean time from a CUDA-event timer, after reading the code to confirm that the timer brackets all per-run work (whitening, batch preparation, training) and the final TTA inference, that test images are never used for training or selection, and that no cached state carries over between runs. In the same session, re-run hiverge's cifar10_speedrun.py and Fulcrum's E1 recipe under the same timer bracket and inter-run protocol and compare all three means. For p3, wrap one full run of each script in FlopCounterMode and compare totals. Roughly 25 A100-minutes for the full check.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/hiverge/cifar10-speedrun>

## Sources

- <https://github.com/hiverge/cifar10-speedrun>
- <https://raw.githubusercontent.com/hiverge/cifar10-speedrun/main/README.md>
- <https://github.com/fulcrumresearch/cifar-10-speedrun>
- <https://fulcrum.inc/2026/07/09/fable-cifar-speedrun.html>
- <https://github.com/KellerJordan/cifar10-airbench>
- <https://arxiv.org/abs/2404.00498>
- <https://github.com/KellerJordan/cifar10-airbench/issues/5>
- <https://github.com/tysam-code/hlb-CIFAR10>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Fulcrum's E1 or cifar10_speedrun.py and profile on an A100. The forward-backward step is compiled with mode='max-autotune', and the Newton-Schulz and augmentation functions are compiled as separate small graphs. Fulcrum found that whole-run CUDA graphs and a fused optimizer gain almost nothing on a fair clock, while the resolution curriculum gave about 0.2 s, so look for algorithmic savings first.
- Fewer epochs or cheaper early epochs through better curricula or data ordering (airbench96_faster's data filtering idea applied at the 94% target; resolution schedules beyond E1's 24-28-32 px).
- FP8 is not available on A100, so focus on algorithmic step-count and FLOP reductions; these show up first in the p3 FLOP count, which can be iterated on a Mac.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Timing convention: airbench's README time is a min/best per Keller Jordan (issue #5), Hiverge prints the mean with TTA inside the timer, and Fulcrum's harness leaves the TTA evaluation untimed but times per-trial setup. This target uses the mean, one timer bracket for every script, and same-machine re-timing.
- GPU variance: 400 W SXM4 and 250-300 W PCIe A100s differ by tens of percent, and cloud hosts of one class differ too; always re-time every incumbent on the same box.
- The incumbent script calls torch.cuda._sleep between runs (letting clocks recover); the claimant's harness must use the same inter-run protocol, or the comparison is unfair.
- Off-the-clock work is the known trap: Fulcrum's audit caught an agent building whitening and the augmented batch stream in untimed setup, filtering for fast hosts and sleeping before the timer. All per-run work must sit inside the timer.
- An accuracy of 93.99% averaged over 200 runs fails; seeds cannot be cherry-picked.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/cifar10-speedrun-94-single-a100.md
```

Already set up? Say `run V3R1T4S on cifar10-speedrun-94-single-a100`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cifar10-speedrun-94-single-a100`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
