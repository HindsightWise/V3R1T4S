# MadryLab CIFAR-10 challenge (white-box, Linf 8/255): push the secret model's accuracy below 43.95%

🛡️ **ML robustness** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The MadryLab CIFAR-10 Adversarial Examples Challenge keeps a white-box leaderboard for its adversarially trained wide ResNet (the 'secret' model, released 2017-12-10): the lowest accuracy on the 10,000 CIFAR-10 test images under an L-infinity budget of 8 on the 0-255 scale. Siyuan Yi's 'Guided Local Attack' leads at 43.95% (2021-08-02), one image ahead of Ye Liu's EWR-PGD at 43.96%, followed by Yusuke Tashiro's ODI-PGD at 43.99% and Sven Gowal's MultiTargeted at 44.03%. The last three improvements were 1-4 images each. Can any attack find a single further adversarial image that the leaders missed, reaching 43.94% or lower?

## What counts as a win

A saved attack.npy of shape (10000, 32, 32, 3) on the 0-255 scale with every value in [0, 255] and max |x_adv - x_nat| <= 8.0 exactly (not using run_attack.py's 0.0001 tolerance), in the official test order, for which the repository's run_attack.py with the 'secret' checkpoint reports an accuracy STRICTLY LOWER (direction: min) than the lowest entry in the 'White-Box Leaderboard' table of https://raw.githubusercontent.com/MadryLab/cifar10_challenge/master/README.md re-fetched live immediately before claiming, and lower than any figure the skeptic finds published for this exact model and budget on all 10,000 images.

## Partial wins

- **p1:** At least 3 test indices where the secret model survives a fixed, saved strong baseline (AutoAttack standard plus 20-restart MultiTargeted, seeds saved) but you hand over a saved valid adversarial image.
- **p2:** A fully reproducible attack reaching 44.00% or lower within 48 laptop-CPU hours with code and seeds saved.

## How a win is checked

Clone MadryLab/cifar10_challenge, fetch the secret model with fetch_model.py, check the array's shape, range and L-infinity bound in float64, run run_attack.py (TF 1.x, or a PyTorch port whose logits match the checkpoint on all clean images), and recount correct predictions. Re-fetch the README table and search for newer numbers on this exact model.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/MadryLab/cifar10_challenge/master/README.md>

## Sources

- <https://raw.githubusercontent.com/MadryLab/cifar10_challenge/master/README.md>
- <https://github.com/MadryLab/cifar10_challenge>
- <https://raw.githubusercontent.com/MadryLab/cifar10_challenge/master/run_attack.py>
- <https://raw.githubusercontent.com/MadryLab/cifar10_challenge/master/fetch_model.py>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Triage first: run cheap APGD-DLR on all 10,000 images, then spend almost all compute on the few hundred correctly classified points with the smallest worst-case margin. A record only needs one more image.
- Ensemble the published leaders' ideas (ODI starts, MultiTargeted, EWR-PGD's example-wise reweighting, Square Attack's random search) on the low-margin points, with many seeds. Their union may beat each one alone.
- Bring in a technique from numerical optimisation: run Frank-Wolfe or mirror descent with line search on the CW margin, and switch to exact coordinate search on the pixels saturated at the box boundary in the final steps.
- Black-box evolutionary search from evolutionary computation (CMA-ES in a low-frequency colour-DCT subspace, or the Parsimonious attack's lazy greedy corner search), which sidesteps any residual gradient obfuscation in this TF model.
- Use the CPU's ability to run many small processes: each core attacks a disjoint shard of the hard points with a different random portfolio, and results are merged per index.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Scale confusion: this challenge uses 0-255 pixels and epsilon 8.0; an attack built for [0,1] inputs and epsilon 8/255 must be rescaled exactly, or rounding can exceed the budget.
- Tolerance slack: run_attack.py accepts 8.0001 and 255.0001; the target requires the strict bounds.
- Only the 'secret' checkpoint counts; 'adv_trained' and 'natural' are different models.
- A PyTorch port of the TF wide ResNet (batch-norm in inference mode, padding) can differ; confirm the logits match before trusting extra errors.
- RobustBench lists a different Madry-style CIFAR-10 model; numbers from RobustBench do not transfer to this checkpoint.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ml-robustness/madry-cifar10-challenge-whitebox-below-leader.md
```

Already set up? Say `run V3R1T4S on madry-cifar10-challenge-whitebox-below-leader`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `madry-cifar10-challenge-whitebox-below-leader`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
