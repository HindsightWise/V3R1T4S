# Smallest neural network reaching 99% test accuracy on MNIST (record: 697 parameters)

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

How few learned parameters does a network need to reach 99% accuracy on the standard 10,000-image MNIST test set? Ruslan Grimov's mnist-minimal-model project reached 99.1% with 1,936 parameters (a Keras CNN with separable convolutions and instance normalisation). Josh Warn's Parameter-Efficient-MNIST, with models contributed by Thomas Warn, lowered this to 697 parameters at 99.03% after training about 700 models with five convolution layers; the saved weights are in the repository as 697_mnist_0.9903.h5 with load_and_test_model.py. No smaller verified model is known. Can a network with 696 or fewer parameters reach 99.00%?

## What counts as a win

A saved model file plus a standalone inference script such that (1) on the official MNIST test set (10,000 images, standard order and labels), plain argmax predictions with no test-time augmentation and no ensembling give accuracy >= 99.00%; (2) the parameter count is STRICTLY LESS (direction: min) than the record stated in https://raw.githubusercontent.com/JoshWarn/Parameter-Efficient-MNIST/main/README.md re-fetched live immediately before claiming (and less than any smaller verified claim the skeptic finds); counting is conservative: every number in the forward pass that is not a universal constant counts (weights, biases, normalisation scales and runs, stored running statistics, fixed hand-designed filters, lookup tables and thresholds), whereas only architecture integers (kernel sizes, strides) and the input scaling 1/255 are free; (3) the weights were learned by a generic training procedure on the 60,000 training images only (training script and seed saved).

## Partial wins

- **p1:** A model at or below 697 counted parameters (under the conservative rule above) whose accuracy on the test set is at least 99.10%, which beats the record holder's 99.03% at equal or smaller size.
- **p2:** A model with at most 500 counted parameters reaching at least 98.80%, giving a new public point on the size-accuracy curve with reproducible training.

## How a win is checked

Load the saved weights in a fresh environment, enumerate every tensor and constant used in forward() and sum their element counts (tied tensors once), run inference on the official MNIST test set with argmax, and compare accuracy and count. Read the script for test-time augmentation, ensembling or test-set use during training. Re-run the training script with its seed to confirm a passing checkpoint is reproducible (or at least that training never touches test images).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/JoshWarn/Parameter-Efficient-MNIST/main/README.md>

## Sources

- <https://raw.githubusercontent.com/JoshWarn/Parameter-Efficient-MNIST/main/README.md>
- <https://github.com/JoshWarn/Parameter-Efficient-MNIST>
- <https://github.com/ruslangrimov/mnist-minimal-model>
- <https://raw.githubusercontent.com/ruslangrimov/mnist-minimal-model/master/README.md>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Weight sharing from signal processing: steerable or rotation-tied convolution kernels and depthwise kernels shared across layers (as in the 1,936-parameter design's shared separable block) cut counts while keeping receptive field.
- Knowledge distillation: train a large teacher, then train the tiny student on soft labels and on augmented inputs; on tiny models distillation often adds the last 0.1-0.3 points.
- Architecture search on CPU: an evolutionary search over kernel shapes (1x3/3x1 factorisation), channel counts and pooling placement, each candidate trained for a few minutes with many seeds in parallel.
- Borrow from compressed sensing and coding theory: low-rank or Kronecker-factored kernels and a final layer that is a tied, structured projection, then check exactly how the conservative rule counts each factor.
- Training-side levers that add no parameters: long schedules with cosine annealing, label smoothing, elastic-distortion augmentation of training images and stochastic weight averaging.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Free-constant smuggling: fixed Gabor or scattering filters, hard-coded normalisation statistics or lookup tables are counted under the conservative rule; a model that is small only because constants are hidden is not a win.
- Test-set selection: choosing the checkpoint or seed by test accuracy is weak evidence; report the selection on a validation split of the training set and re-check on test.
- Accuracy rounding: 98.995% is not 99%; the count of correct images must be at least 9,900.
- Test-time augmentation or ensembling of several tiny models multiplies the effective parameters and is excluded.
- Using EMNIST, QMNIST or extra digits for training changes the task; only the 60,000 MNIST training images may be used.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/smallest-mnist-99-percent-network.md
```

Already set up? Say `run V3R1T4S on smallest-mnist-99-percent-network`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `smallest-mnist-99-percent-network`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
