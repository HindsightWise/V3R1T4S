# FISBe (FlyLight) 3D neuron instance segmentation: beat PatchPerPix's benchmark score S = 0.35 on the combined test set

🧠 **Neuroscience** · standard · tractability ★★★☆☆ · compute: laptop-days (completely-labelled set 7.1 GB, partly-labelled set 14.4 GB of 3-channel ~400x700x700 zarr volumes; a GPU is strongly recommended) · open as of 2026-10-30

## The problem

FISBe (Lisa Mais, Peter Hirsch, Claire Managan, Ramya Kandarpa, Josef Lorenz Rumberger, Annika Reinke, Lena Maier-Hein, Gudrun Ihrke, Dagmar Kainmueller; CVPR 2024, arXiv:2404.00130) is the first public real-world benchmark for instance segmentation of long, thin, inter-woven neurons. It has 30 completely and 71 partly labelled 3D multicolor (MCFO) light-microscopy images of Drosophila brains from Janelia FlyLight, with about 600 expert-traced neurons, CC BY 4.0 on Zenodo (10875063). The official train/val/test sample lists ship with the data, test labels included. The ranking score is S = 0.5*avF1 + 0.5*C. avF1 is the F1 averaged over clDice thresholds 0.1-0.9 with greedy one-to-one matching, and C is the average ground-truth coverage under clPrecision. The project leaderboard invites new entries by email, and on 2026-10-30 it still lists only the paper's baselines. On the combined test set the leader is PatchPerPix with S 0.35 (avF1 0.34, C 0.35, 19 false splits, 52 false merges), then Duan et al. 0.30, FFN+partly 0.27 and FFN 0.25. On the completely-labelled test set it is PatchPerPix 0.34 (avF1 0.29, C 0.40).

## What counts as a win

Instance segmentations of every sample in the official FISBe test split (sample_list_per_split.txt), from a model trained on the official train (and val) samples only and frozen before test labels are read. The skeptic computes S = 0.5*avF1 + 0.5*C with the definitions on the FISBe project page and in the paper, using the Kainmueller-Lab/evaluate-instance-segmentation code with its FISBe (flylight) settings, calibrated on the code's own test cases and by checking that the ground-truth labels score S = 1 (no PatchPerPix FISBe checkpoints or predictions are released). S on the combined test set must be STRICTLY HIGHER (direction: max) than the leaderboard best (0.35, re-fetched from the project page immediately before claiming) and than any FISBe test value found by the NOVELTY check, by at least 0.02.

## Partial wins

- **p1:** On the completely-labelled test set, S strictly above 0.34 by at least 0.02.
- **p2:** On the combined test set, avF1 strictly above 0.34 by at least 0.02 while S is at least 0.35.
- **p3:** S at least 0.35 on the combined test set with fewer than 30 false merges (PatchPerPix has 52).

## How a win is checked

The skeptic downloads the FISBe zips from Zenodo, checks that the submitted label volumes cover exactly the test samples, computes S, avF1, C, clDiceTP, tp, FS and FM with the metric code and the paper's thresholds, and audits that test samples were not used in training or model selection. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://kainmueller-lab.github.io/fisbe/>

## Sources

- <https://kainmueller-lab.github.io/fisbe/>
- <https://zenodo.org/doi/10.5281/zenodo.10875063>
- <https://arxiv.org/abs/2404.00130>
- <https://github.com/Kainmueller-Lab/PatchPerPix>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The three color channels carry stochastic per-neuron color labels: color-aware affinity or embedding losses plus skeleton-based (topology-preserving) post-processing target the false merges that dominate PatchPerPix's errors.
- Partly-labelled volumes can be used with masked losses; FFN+partly shows that they help.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Partly-labelled test volumes only score the labelled neurons; follow the paper's handling of unlabelled foreground or the score is wrong.
- dim_neurons_val_and_test_sets.json flags dim neurons for an extended evaluation. Before scoring, check in the paper which neurons enter the main leaderboard S, and use exactly that set.
- The completely-labelled test split has only 7 volumes, so one volume moves the score noticeably; report per-volume values.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/neuroscience/fisbe-flylight-neuron-instance-segmentation.md
```

Already set up? Say `run V3R1T4S on fisbe-flylight-neuron-instance-segmentation`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fisbe-flylight-neuron-instance-segmentation`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
