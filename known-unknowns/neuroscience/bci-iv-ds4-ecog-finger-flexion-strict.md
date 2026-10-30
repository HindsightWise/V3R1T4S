# BCI Competition IV dataset 4 (ECoG finger flexion): beat the best published mean correlation (0.69, DTCNet 2025) on the official test labels under a strict no-test-tuning protocol

🧠 **Neuroscience** · standard · tractability ★★☆☆☆ · compute: laptop-hours (3 subjects, 62/48/64 ECoG channels, 400 s training and 200 s test each) · open as of 2026-10-30

## The problem

BCI Competition IV dataset 4 (Kai J. Miller and Gerwin Schalk, Washington/Albany; organised by Blankertz et al.) asks for the continuous flexion of five fingers to be predicted from ECoG. The last third of each recording is the test segment. The official measure is the correlation between true and predicted flexion, averaged over the three subjects and over fingers 1, 2, 3 and 5. The competition's true test labels are public on the BCI Competition IV results page. The winner was Nanying Liang and Laurent Bougrain (r = 0.46), then Remi Flamary and Alain Rakotomamonjy (0.42). Later work raised the number: Xie et al. 2018 (0.52), Frey et al. 2021 (0.52), Yao et al. 2022 (0.53), and FingerFlex (Vladislav Lomtev, Alexander Kovalev, Alexey Timchenko; arXiv:2211.01960), an encoder-decoder CNN. FingerFlex reports 0.67 averaged over all five fingers (0.66/0.62/0.74 per subject). Its per-finger means are thumb 0.70, index 0.72, middle 0.62, ring 0.69 and little 0.63, so the official four-finger measure is about 0.67. FingerFlex used the competition test segment as its validation set and tuned hyperparameters on subject 1's part of it. DTCNet (Fufeng Wang, Zihe Luo, Wei Lv, XiaoLin Zhu; Frontiers in Computational Neuroscience 19, July 2025, doi 10.3389/fncom.2025.1627819), a wavelet-spectrogram network with dilated and transposed convolutions, reports 0.69 over five fingers (0.71/0.59/0.77 per subject; per finger 0.70, 0.72, 0.67, 0.70, 0.65), about 0.685 on the four-finger measure. It tuned hyperparameters on one subject and does not say whether test labels were used. No result we found clears these values under a protocol that never touches test labels before scoring.

## What counts as a win

Predicted flexion for the official test segment of all three subjects, from models trained on the training data only, with every hyperparameter chosen by validation inside the training segment and frozen before the true labels (ds4/true_labels.zip) are read. The skeptic computes the official competition measure (mean Pearson r over 3 subjects and fingers 1, 2, 3 and 5, at the 25 Hz label rate, with no post-hoc smoothing fitted on test) and the five-finger mean. The official measure must be STRICTLY HIGHER (direction: max) than 0.69 and the five-finger mean STRICTLY HIGHER than 0.69 (DTCNet's values), each also above any strict-protocol value found by the NOVELTY check, by at least 0.01.

## Partial wins

- **p1:** Official four-finger measure strictly above 0.53 (Yao et al. 2022, the best pre-FingerFlex value) under the same strict protocol, with code released.
- **p2:** Under the strict protocol, strictly beat FingerFlex's per-subject five-finger mean on subject 2 (0.62) by at least 0.02.
- **p3:** Under the strict protocol, the official four-finger measure and the five-finger mean both strictly above FingerFlex's 0.67 by at least 0.01.

## How a win is checked

The competition data sits behind a terms-and-conditions checkbox at bbci.de/competition/iv (#download), which a human must accept; the true labels are a direct download at bbci.de/competition/iv/results/ds4/true_labels.zip. The skeptic retrains the declared models from the training segment only, recomputes the correlations, and audits that the hyperparameter search reads only training data. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.bbci.de/competition/iv/results/>

## Sources

- <https://www.bbci.de/competition/iv/results/>
- <https://www.bbci.de/competition/iv/>
- <https://arxiv.org/abs/2211.01960>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Wavelet or multi-band amplitude features with a temporal convolutional decoder, plus a finger-coupling prior (fingers co-flex), may beat end-to-end CNNs on only 400 s of training data.
- Pretraining on the public Miller 2019 ECoG library (not the competition subjects) before per-subject fine-tuning.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The competition measure excludes finger 4 (ring); report both the official and five-finger means.
- Hyperparameters tuned on the test segment, as FingerFlex did on subject 1, invalidate a claim.
- Flexion labels are sampled at 25 Hz; correlations at an interpolated 100 Hz or 1 kHz differ slightly.
- The Miller 2019 ECoG library comes from the same lab and may contain the competition subjects or recordings, test segment included. Exclude any overlapping subject before pretraining on it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/neuroscience/bci-iv-ds4-ecog-finger-flexion-strict.md
```

Already set up? Say `run V3R1T4S on bci-iv-ds4-ecog-finger-flexion-strict`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bci-iv-ds4-ecog-finger-flexion-strict`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
