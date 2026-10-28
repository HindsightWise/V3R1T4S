# TRADES MNIST white-box leaderboard (Linf 0.3): push the TRADES SmallCNN's robust accuracy below 92.46%

🛡️ **ML robustness** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Hongyang Zhang, Yaodong Yu and co-authors of TRADES (ICML 2019) published their MNIST SmallCNN checkpoint and test arrays with a white-box attack leaderboard (L-infinity epsilon 0.3, 10,000 test images). Hong Lei's ITA attack leads at 92.46% robust accuracy (2021-08-27), one image ahead of Ye Liu's EWR-PGD at 92.47% (2020-12-20), then 92.52% (EWR-PGD, first entry), Maksym Andriushchenko's Square Attack at 92.58% and Francesco Croce's FAB at 93.33%. Is there an attack that breaks at least one more image, reaching 92.45% or below? This model is not on RobustBench (which has no MNIST track), so it is separate from the RobustBench targets.

## What counts as a win

A saved mnist_X_adv.npy built from the repository's mnist_X.npy (same order) with every value in [0, 1] and max |x_adv - x| <= 0.3, for which the repository's evaluate_attack_mnist.py with model_mnist_smallcnn.pt reports a robust accuracy STRICTLY LOWER (direction: min) than the lowest 'Robust Accuracy' in the MNIST 'White-box leaderboard' table of https://raw.githubusercontent.com/yaodongyu/TRADES/master/README.md re-fetched live immediately before claiming, and lower than any figure the skeptic finds published for this exact checkpoint, budget and full test set.

## Partial wins

- **p1:** At least 5 test indices where the TRADES SmallCNN survives a fixed, saved strong baseline (AutoAttack standard plus 100-restart PGD on the CW margin, seeds saved) but you hand over a saved valid adversarial image.
- **p2:** A reproducible attack that reaches 92.50% or below on a laptop CPU in at most 12 hours, with code and seeds saved.

## How a win is checked

Download model_mnist_smallcnn.pt, mnist_X.npy and mnist_Y.npy from the README links (plain GET), load SmallCNN from models/small_cnn.py, run evaluate_attack_mnist.py on the saved adversarial array (it checks the delta and the [0,1] range), and recount errors independently from the logits on CPU. Re-fetch the README table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/yaodongyu/TRADES/master/README.md>

## Sources

- <https://raw.githubusercontent.com/yaodongyu/TRADES/master/README.md>
- <https://github.com/yaodongyu/TRADES>
- <https://raw.githubusercontent.com/yaodongyu/TRADES/master/evaluate_attack_mnist.py>
- <https://arxiv.org/abs/1901.08573>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The SmallCNN is small enough for exact methods from operations research: encode the network as a MILP (or use alpha-beta-CROWN's BaB-attack) for the lowest-margin images and let the solver either find a counterexample or prove the point safe, which shrinks the search set.
- Corner search from discrete optimisation: L-infinity optima on piecewise-linear nets tend to lie on box vertices, so run local search over pixel sign patterns (block flips, tabu lists) seeded by PGD.
- Combine the leaders' tricks (ITA, EWR-PGD reweighting, Square Attack random search, FAB minimum-norm boundary search) as a portfolio per image; since every new image counts, union the successes.
- Use an idea from the physics of glasses, parallel tempering: run several PGD chains at different step sizes and noise levels and swap states, to escape the flat loss plateaus that TRADES training creates.
- Transfer from surrogates: fine-tune a surrogate on the TRADES model's soft labels and use its adversarial directions as starting points for white-box refinement on the real model.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Range and budget: the evaluator rejects values outside [0,1] and deltas above 0.3; float32 rounding after clipping can push a delta to 0.30000001, so clip in the final dtype.
- Use the checkpoint and the arrays from the README links; retraining a TRADES model yourself gives a different, easier model.
- The CIFAR-10 TRADES WRN-34-10 model is also on RobustBench (already covered there); this target is only the MNIST SmallCNN.
- A model in train mode (dropout active) gives random errors; the evaluator must use model.eval().

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ml-robustness/trades-mnist-smallcnn-whitebox-below-leader.md
```

Already set up? Say `run V3R1T4S on trades-mnist-smallcnn-whitebox-below-leader`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `trades-mnist-smallcnn-whitebox-below-leader`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
