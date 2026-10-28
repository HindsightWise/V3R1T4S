# MadryLab MNIST challenge (white-box, Linf 0.3): push the secret model's accuracy below the leaderboard's best attack

🛡️ **ML robustness** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The MadryLab MNIST Adversarial Examples Challenge (Madry, Makelov, Schmidt, Tsipras, Vladu) released an adversarially trained two-conv-layer CNN (the 'secret' model, weights public since 2017-10-19) and keeps a white-box leaderboard: the lowest accuracy any attack achieves on the 10,000 MNIST test images under an L-infinity budget of 0.3. The README table, frozen since submissions closed on 2022-05-03, is led by Siyuan Yi's 'Guided Local Attack' at 88.00% (2021-08-30), ahead of Chen Wan's PCROS attack at 88.04%, Tianhang Zheng's adaptive Distributionally Adversarial Attack at 88.06%, Yusuke Tashiro's ODI-PGD at 88.13% and Francesco Croce's Square Attack at 88.25%. Since May 2018 the record has improved eight times, by 0.02-0.77 points each; the last two improvements (2020-10-28, 2021-08-30) were 0.02 and 0.04 points (2 and 4 images), and about 8,800 test points are still unbroken. Is the true robust accuracy below 88.00%? One more adversarial image is enough: 87.99% means 8,799 correct out of 10,000.

## What counts as a win

A saved attack.npy of shape (10000, 784) such that (1) every pixel lies in [0, 1] exactly and max |x_adv - x_nat| <= 0.3 exactly (no use of the 0.0001 tolerance in run_attack.py), against the challenge's own test-set ordering; (2) the repository's run_attack.py with the 'secret' checkpoint fetched by fetch_model.py reports an accuracy STRICTLY LOWER (direction: min) than the lowest accuracy in the 'White-Box Leaderboard' table of https://raw.githubusercontent.com/MadryLab/mnist_challenge/master/README.md, re-fetched live immediately before claiming; and (3) strictly lower than any figure the skeptic finds in a paper or repository for this exact secret model, the full 10,000 images and an L-infinity budget of 0.3. Submitting to MadryLab is not part of the target.

## Partial wins

- **p1:** A list of at least 5 test indices on which the secret model stays correct under a fixed, re-runnable strong baseline (AutoAttack standard version plus 100-restart PGD on the CW margin loss, seeds saved), but for which you hand over a saved valid adversarial image. Each image is checked independently.
- **p2:** A deterministic, documented attack that reaches 88.05% or lower on the full set in at most 24 hours on a laptop CPU, with code and seeds saved, so that it matches the top three entries using an attack anyone can reproduce.

## How a win is checked

Clone MadryLab/mnist_challenge, run `python fetch_model.py secret`, load the saved attack.npy, assert shape, range [0,1] and L-infinity <= 0.3 with numpy in float64, then run `python run_attack.py` (TensorFlow 1.x environment or a PyTorch port whose logits match the TF checkpoint to 1e-5 on all 10,000 clean images) and read the accuracy. Recount the correct predictions independently from the logits. Re-fetch the README table and search for later published numbers on the same model.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/MadryLab/mnist_challenge/master/README.md>

## Sources

- <https://raw.githubusercontent.com/MadryLab/mnist_challenge/master/README.md>
- <https://github.com/MadryLab/mnist_challenge>
- <https://raw.githubusercontent.com/MadryLab/mnist_challenge/master/run_attack.py>
- <https://raw.githubusercontent.com/MadryLab/mnist_challenge/master/fetch_model.py>
- <https://github.com/MadryLab/mnist_challenge_models>
- <https://arxiv.org/abs/1706.06083>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Treat it as combinatorial search, imported from SAT/MAX-SAT local search: the optimum of a piecewise-linear network inside an L-infinity box usually sits at a box corner, so run WalkSAT-style local search over sign patterns of the 784 pixel perturbations (flip blocks of pixels, accept on margin decrease), seeded from PGD solutions.
- Use a verifier as an attacker (from formal methods): run branch-and-bound with alpha-beta-CROWN or a MILP solver restricted to the roughly 1-2% of points where PGD margins are smallest; this small CNN is close to tractable, and an exact counterexample on even one point beats the record.
- Search in a compression basis (from image coding): parameterise the perturbation in a DCT or wavelet subspace and run CMA-ES or another derivative-free search, which is immune to the gradient masking that max-pooling and ReLU dead zones cause on this adversarially trained model.
- Use diverse start points: output-diversified initialisation (Tashiro), many targeted restarts on each wrong class (Gowal's MultiTargeted), and a portfolio over loss functions (CE, CW margin, DLR). Spend the CPU budget only on the low-margin points.
- Borrow the 'temperature' trick from statistical physics: anneal a smoothed surrogate (softplus ReLUs, soft max-pool), take gradients through it to reach a basin, then finish with exact-model PGD.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Tolerance exploitation: run_attack.py accepts L-infinity up to 0.3001 and pixels up to 1.0001; a 'win' that depends on that slack is not a win here. Clip in float64, then cast.
- Wrong checkpoint: the 'adv_trained' public model and the 'natural' model are easier; only the 'secret' checkpoint counts.
- Port mismatch: a PyTorch re-implementation with slightly different padding or max-pool rounding can report extra errors that the original TF model does not make; verify logits agree with the TF checkpoint on every image.
- Unrestricted attacks such as spatial transforms or structure-preserving transformations report far lower accuracy (one 2018 paper reports 9.79%) but do not respect the L-infinity 0.3 threat model and do not count.
- Index or label misalignment: the attack file must follow the official test-set order; reordering or using a subset changes the denominator.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ml-robustness/madry-mnist-challenge-whitebox-below-leader.md
```

Already set up? Say `run V3R1T4S on madry-mnist-challenge-whitebox-below-leader`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `madry-mnist-challenge-whitebox-below-leader`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
