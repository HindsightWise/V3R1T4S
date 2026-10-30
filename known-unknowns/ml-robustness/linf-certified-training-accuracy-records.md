# Deterministic Linf certified accuracy records (MNIST 0.1/0.3, CIFAR-10 2/255 and 8/255, TinyImageNet 1/255): certify more test images than the best published model

🛡️ **ML robustness** · standard · tractability ★★☆☆☆ · compute: laptop-days (MNIST cells: CPU or Apple-GPU training of a CNN7-class network with IBP-based losses, then IBP/CROWN on all 10,000 test images and alpha-beta-CROWN on the residue); needs cluster for the CIFAR-10 and TinyImageNet cells (GPU-days of training and certification) · open as of 2026-10-30

## The problem

Deterministic certified training produces networks for which a sound verifier proves, image by image, that no Linf perturbation of radius eps changes the prediction. The standard settings (Gowal et al. 2018, Shi et al. 2021, CTBench) are MNIST eps 0.1 and 0.3, CIFAR-10 eps 2/255 and 8/255, and TinyImageNet eps 1/255, scored by certified accuracy on the full test set (TinyImageNet: validation set). Best published values on 2026-10-28: MNIST 0.1: 98.53% (AD-CERT, Matteo Melis, Jesus Martinez del Rincon and Vishal Sharma, arXiv:2606.31653v2, BMVC 2026, Table 1; CNN7, alpha-beta-CROWN with 400 s branch-and-bound per image), ahead of TAPS/STAPS 98.52% (CTBench). MNIST 0.3: 94.02% (Zhaoyang Lyu, Minghao Guo, Tong Wu, Guodong Xu, Kehuan Zhang and Dahua Lin, CVPR 2021: a CROWN-IBP-trained DM-large network with ParamRamp activation, trained at eps 0.4, CROWN-LBP verified error 5.98% at eps 0.3, supplementary Table 4; listed on the SoK certified-robustness leaderboard of Linyi Li, Tao Xie and Bo Li); best ReLU network 94.00% (IBP with multi-objective hyperparameter optimisation, Konstantin Kaulen, Hadar Shavit and Holger H. Hoos, arXiv:2606.02134v2, ICML 2026, Table 2, 300 s verification cutoff), then AD-CERT 93.98%. Kaulen et al. state that, following common practice, they tuned hyperparameters on the test set (their validation-tuned fronts are strictly lower), so their values are optimistic bars. CIFAR-10 2/255: 65.20% (AD-CERT's controlled re-run in Table 2 of arXiv:2606.31653v2, clean 79.21%; its Table 1 headline is 65.08%), then MTL-IBP re-tuned by Kaulen et al. 64.61% (Table 9) and CC-DIST 64.60% (Alessandro De Palma, arXiv:2602.02626). CIFAR-10 8/255: 41.78% (SortNet trained with EDM-generated data: Thomas Altstidl, David Dobre, Arthur Kosmala, Björn Eskofier, Gauthier Gidel and Leo Schwinn, 'On the Scalability of Certified Adversarial Robustness with Generated Data', NeurIPS 2024, arXiv:2305.10388, +1.39 points over SortNet; shown as a preprint on the SoK board), SortNet alone 40.39% (Zhang, Jiang, He and Wang, NeurIPS 2022), best ReLU network 35.85% (AD-CERT, loss-ablation Table 7; Table 1 lists 35.84% and the 3-seed mean in Table 6 is 35.78 +- 0.15). TinyImageNet 1/255: 30.67% (MTL-IBP re-tuned by Kaulen et al., Table 1, 1,000 s cutoff), then AD-CERT 28.19% and CC-DIST 27.88%. The CTBench library and benchmark (Yuhao Mao, Stefan Balauca, Martin Vechev, arXiv:2406.04848, github.com/eth-sri/CTBench) provides the reference training and certification cascade (IBP, CROWN, alpha-CROWN, alpha-beta-CROWN) behind most of these numbers. The SoK board was last updated on 2024-06-12, so the 2026 records live only in the papers. Probabilistic certificates (randomized smoothing) are a separate track and do not count here. Open question per cell: can a model certify more test images?

## What counts as a win

Success means, for ONE cell, a trained classifier (weights plus a plain PyTorch or ONNX forward definition; input in [0,1] pixel space with any normalisation inside the model; deterministic, no test-time randomness or input purification) such that the skeptic's own certification of the FULL official evaluation set (MNIST and CIFAR-10: the 10,000 test images in canonical order; TinyImageNet: the 10,000 official validation images at 64x64) at the cell's Linf radius gives a certified count STRICTLY GREATER (direction: max) than the cell record by at least 10 images (0.10 points). An image is certified iff its clean argmax prediction is correct AND a sound verifier proves a lower bound >= 1e-5 on every margin z_y - z_j (j != y) over the whole box {x' : |x' - x|_inf <= eps} intersected with [0,1]^d. Accepted verifiers, all run by the skeptic: their own float64 interval bound propagation; CROWN or alpha-CROWN from a pinned auto_LiRPA release; alpha-beta-CROWN branch-and-bound from a pinned release with at most 400 s per image; for Lipschitz-by-construction architectures (l_inf-dist nets, SortNet) the closed-form certificate recomputed in float64. Attack-found counterexamples, timeouts and errors count as not certified. The record is the maximum value for that cell in the live sources, re-checked immediately before claiming (AD-CERT arXiv:2606.31653 Tables 1, 2 and 5-7, Kaulen et al. arXiv:2606.02134 Tables 1-2, the SoK leaderboard, and anything newer the NOVELTY skeptic finds); on 2026-10-28: MNIST 0.1: 98.53; MNIST 0.3: 94.02; CIFAR-10 2/255: 65.20; CIFAR-10 8/255: 41.78; TinyImageNet 1/255: 30.67. Training may use only the cell's training split, plus images from a generative model trained only on that split (declared); no test or validation images or near duplicates of them.

## Partial wins

- **p1:** ReLU record in a cell whose overall record is held by a non-ReLU architecture: a network whose only nonlinearities are ReLU (no extra or generated data) certifying at least 10 more images than the best published ReLU value, under the same checks: MNIST 0.3 above 94.00% (Kaulen et al.), or CIFAR-10 8/255 above 35.85% (AD-CERT, Table 7).
- **p2:** Pareto improvement on CIFAR-10 2/255 or TinyImageNet 1/255: certified accuracy (same checks) within 0.05 points of the live cell record or above it, together with clean accuracy at least 2.0 points above the record holder's clean accuracy (AD-CERT 79.21% on CIFAR-10 2/255; Kaulen et al.'s MTL-IBP 39.75% on TinyImageNet).

## How a win is checked

Skeptic loads the weights in a fresh environment, confirms the forward pass is deterministic and that the input domain is [0,1], computes clean accuracy, then certifies in stages with their own scripts: float64 IBP on all images (minutes for MNIST), CROWN/alpha-CROWN via a pinned auto_LiRPA on the rest, and alpha-beta-CROWN (pinned release, the claimant's YAML, at most 400 s per image) only on images still uncertified; counts certified images and checks the 1e-5 margin. Re-read the AD-CERT and Kaulen et al. arXiv pages and the SoK board for the cell record and search arXiv for 'certified training' papers newer than 2026-10-28. Read the training script for test-set use. For MNIST the total is hours to a day on CPU, dominated by branch-and-bound; CIFAR-10 and TinyImageNet need a GPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2606.31653>

## Sources

- <https://arxiv.org/abs/2606.31653>
- <https://arxiv.org/abs/2606.02134>
- <https://sokcertifiedrobustness.github.io/leaderboard/>
- <https://arxiv.org/abs/2406.04848>
- <https://github.com/eth-sri/CTBench>
- <https://arxiv.org/abs/2602.02626>
- <https://arxiv.org/abs/2305.10388>
- <https://openreview.net/forum?id=TFAG9UznPv>
- <https://arxiv.org/abs/2104.00447>
- <https://openaccess.thecvf.com/content/CVPR2021/supplemental/Lyu_Towards_Evaluating_and_CVPR_2021_supplemental.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- MNIST cells are laptop-sized: start from CTBench's IBP, SABR or MTL-IBP recipes for CNN7, then add what moved the 2026 records: adversarial distillation from a PGD-trained teacher (AD-CERT), feature distillation (CC-DIST) and multi-objective hyperparameter search (Kaulen et al. found that published configurations were under-tuned).
- Architecture width: Mao et al. (Understanding Certified Training with IBP) found that wider, not deeper, CNN7 variants improve certified accuracy (their Table 1 includes 4x-wide MNIST models); on MNIST a wider CNN7 is probably still trainable on a laptop in days.
- Make certification cheap: train so that IBP alone certifies almost everything (IBP-trained nets are nearly propagation-invariant), then spend branch-and-bound only on the few hundred hardest images; the skeptic's cost drops the same way.
- For the 8/255 and 0.3 cells, l_inf-dist nets and SortNet give exact certificates by margin; combining them with generated training data (as Altstidl et al. did) is the route to the overall record.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Certified accuracy on a subset (first 1,000 images) or on the training set is not the benchmark; the full test (TinyImageNet: validation) set is.
- Unsound shortcuts: PGD/AutoAttack accuracy is an upper bound on certified accuracy, not a certificate; verifier timeouts are uncertified; float32 bounds with zero margin can be unsound, hence the 1e-5 margin.
- Normalisation outside the model changes the perturbation set; eps is applied to [0,1] pixels.
- Model selection on the test set: choose checkpoints by validation or training-set certified accuracy and say so.
- Comparing against stale tables: the SoK board misses the 2026 records (AD-CERT, Kaulen et al.); the live record is the maximum over all sources.
- Records obtained with a non-ReLU architecture or generated data are still the overall cell record; only p1 restricts to ReLU networks.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ml-robustness/linf-certified-training-accuracy-records.md
```

Already set up? Say `run V3R1T4S on linf-certified-training-accuracy-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `linf-certified-training-accuracy-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
