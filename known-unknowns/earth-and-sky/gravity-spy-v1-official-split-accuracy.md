# Gravity Spy v1.0 LIGO glitch classification: beat the best published test accuracy on the official 22-class split

🌍 **Earth and sky** · standard · tractability ★★★☆☆ · compute: laptop-hours (the v1.0 image arrays are one 3.3 GB HDF5 file; a small CNN, or a fine-tuned pretrained model, trains on CPU or an Apple GPU) · open as of 2026-10-30

## The problem

Gravity Spy (Zevin et al. 2017; Bahaadini et al. 2018, Information Sciences 444:172-186) combines citizen-science labels with machine learning to classify transient noise (glitches) in LIGO data. The v1.0 training set released with Bahaadini, Noroozi, Rohani, Coughlin, Zevin, Smith, Kalogera and Katsaggelos (Zenodo 10.5281/zenodo.1476156) holds 8,583 O1/O2 glitches in 22 classes, each as four Omega-scan images (0.5, 1, 2 and 4 s). An official split is given in trainingset_v1d0_metadata.csv (md5 6b99210289d508696fb3feccfa7c79fc): 6,008 train, 1,288 validation and 1,287 test. Published test accuracies on this split are 97.67% (merged-view CNN) and 98.21% (four-CNN hard-fusion ensemble), both from Bahaadini et al. 2018, and 98.68% with macro-F1 97.18% for a ResNet18 trained from scratch (Fernandes, Vieira, Onofre, Calderon Bustillo, Torres-Forne and Font, arXiv:2303.13917, Table I). George, Shen and Huerta (PRD 97, 101501) report 98.84%, but on a different split with no validation set. A search of arXiv and the web on 2026-10-28 found no higher test accuracy on the official v1.0 split; later work uses other datasets (the v1d1 release of 7,966 glitches, or O3 data with more classes). Open task: a model trained only on the official training split that beats 98.68% on the official test set by a clear margin.

## What counts as a win

A saved model (code, fixed seeds, weights) trained only on the 6,008 'train' samples of Gravity Spy v1.0 (Zenodo record 1476156; labels and split from trainingset_v1d0_metadata.csv, md5 6b99210289d508696fb3feccfa7c79fc), with hyperparameters and early stopping chosen on the 1,288 'validation' samples only. No other Gravity Spy-labelled data may be used for training or pre-training: v1d1, the O1-O3 machine-learning and volunteer classification releases and the Zooniverse data contain the same glitches. Generic pretrained weights such as ImageNet are allowed. The model must satisfy: (1) top-1 accuracy on the 1,287 'test' samples (all 22 classes, every image kept, labels as released) of at least 1,273/1,287 (98.91%), strictly above (direction: max) the 98.68% of Fernandes et al. (arXiv:2303.13917) and the 98.84% of George et al. (different split); (2) macro-averaged F1 on the test set of at least 97.18%; (3) retraining from scratch with 3 further seeds gives mean test accuracy of at least 98.76% (1,271/1,287); and (4) the accuracy exceeds any test accuracy on the official v1.0 split reported in a paper up to the claim date (search arXiv and the web for Gravity Spy classification, re-fetched live immediately before claiming).

## Partial wins

- **p1:** Test accuracy above 98.21% (the Bahaadini et al. four-CNN ensemble) from a single network that sees only one time-window view (0.5, 1, 2 or 4 s), under the same training rules.
- **p2:** Test accuracy of at least 98.68% (1,270/1,287) from a model trained on CPU in under 2 hours wall-clock, under the same training rules, with a 3-seed mean of at least 98.5%.
- **p3:** Macro-F1 of at least 98.0% on the test set with accuracy of at least 98.68%, under the same training rules (the minority classes Paired_Doves, Wandering_Line, Air_Compressor and Chirp drive macro-F1).

## How a win is checked

Skeptic downloads trainingsetv1d0.h5 and the metadata CSV from Zenodo record 1476156 (checking the md5 values on the record), runs the saved inference on the 1,287 test samples, recomputes accuracy and macro-F1 with an independent 20-line script, retrains one seed from scratch to confirm the recipe reaches the reported validation accuracy, and confirms the training script never reads test samples: two deterministic CPU reruns with the same seed, one with the test images replaced by noise, must give identical weights (GPU training is often not bitwise reproducible, so this check runs on CPU). A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:%22Gravity+Spy%22&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://zenodo.org/records/1476156>
- <https://arxiv.org/abs/2303.13917>
- <https://doi.org/10.1016/j.ins.2018.02.068>
- <https://arxiv.org/abs/1711.07468>
- <https://zenodo.org/records/1476551>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: fine-tune a modern pretrained image model (ConvNeXt, EfficientNet, ViT) on the four views, stacked as channels or fused late; the ResNet18 baseline of Fernandes et al. is a strong start.
- Label smoothing for noisy citizen-science labels (Wu et al., CQG 42, 165015, found it helps on Gravity Spy O3 data).
- Cross-domain import (audio tagging): treat the Omega scans as spectrograms and fine-tune an audio-pretrained transformer (Deshmukh et al., arXiv:2601.20034, used AST on O3/O4 glitches).
- Cross-domain import (medical imaging): multi-scale view fusion with test-time augmentation limited to time shifts that keep the frequency axis fixed.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The test labels are public; using test images or labels for model selection, threshold tuning or pseudo-labelling voids the claim.
- v1d1 (Zenodo 1476551, 7,966 glitches) keeps 5,726 v1.0 ids with the same train/validation/test assignment and adds 2,240 new ones; its test split holds 853 of the 1,287 v1.0 test glitches, so training on all of v1d1 leaks them, and even its training split is Gravity Spy-labelled data the rules exclude.
- Some released spectrograms are blank (Yan et al., arXiv:2207.04001, removed them before making their own split); keep all 1,287 test samples, because dropping images changes the denominator and the comparison.
- George et al.'s 98.84% used a different split and is not directly comparable; the main bar is set above it anyway.
- Differences of 1-2 test samples are within seed noise; criterion (3)'s 3-seed mean guards against a lucky seed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/gravity-spy-v1-official-split-accuracy.md
```

Already set up? Say `run V3R1T4S on gravity-spy-v1-official-split-accuracy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gravity-spy-v1-official-split-accuracy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
