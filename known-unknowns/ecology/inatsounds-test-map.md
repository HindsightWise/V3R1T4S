# iNatSounds 2024: beat the best published test mAP (65.4) for file-level species ID across 1,212 species of birds, frogs, insects and mammals

🐦 **Ecology and bioacoustics** · standard · tractability ★★☆☆☆ · compute: needs cluster (one GPU for 1-3 days; 133 GB of audio: 81 GB train, 25 GB val, 27 GB test on AWS Open Data) · open as of 2026-10-30

## The problem

The iNaturalist Sounds Dataset (Chasmai, Shepard, Maji, Van Horn; arXiv 2506.00343; data at github.com/visipedia/inat_sounds) has 230k recordings of 5,569 species from 27k recordists. It has fixed train (137,012 files), validation (45,698) and test (49,527 files, 1,212 evaluation species) splits, and the test labels are released. Evaluation is at file level. The primary metric is class-averaged mAP; class-averaged top-1, top-5 and mF1 are also reported. The paper's best test results are mAP 65.4 +/- 0.1 and mF1 67.9 (ViT-B/16, multi-label loss plus mean teacher). The best class-averaged top-1 is 53.6 without location (ViT-B/16) and 60.7 with a geo prior (ResNet-50). A later paper from the same group (Liu, Chasmai, Maji, Van Horn, arXiv 2605.14031, May 2026) reports test top-1 62.76 and top-5 82.58 by fine-tuning BirdMAE, but no mAP. An arXiv query on 2026-10-30 returned no other paper with iNatSounds test numbers.

## What counts as a win

A model trained on the iNatSounds train split (validation split for selection only) that outputs one score per evaluation species for every test file, from audio alone (no location or date). Its class-averaged test mAP, computed with the authors' evaluation code (github.com/cvl-umass/iNatSounds) as a mean over at least 3 seeds, must be STRICTLY GREATER (direction: max) than 65.4 by at least 0.5 points. It must also beat any iNatSounds test mAP that the NOVELTY skeptic finds in a paper from the last 24 months. Pretrained weights are allowed if declared, but their training corpus must exclude iNaturalist audio observations (the source of the test files), or the claim must show by file hash or observation id that no test recording was seen. Deliverables: code, seeds, saved per-file test scores and the evaluation output.

## Partial wins

- **p1:** Audio-only class-averaged test top-1 above 62.76 and top-5 above 82.58 (3-seed mean), under the same leakage rules.
- **p2:** Test mF1 (per-class best threshold, as the paper defines it) above 67.9 with mAP of at least 65.0 (3-seed mean).

## How a win is checked

The skeptic downloads the test annotations (md5 5482f112f05db4ba8576ba425d95d6a7) and recomputes mAP, top-1/top-5 and mF1 from the saved per-file scores with the authors' code. They re-run inference for one seed on a random 2,000-file test subset and audit the pretraining corpora for iNaturalist audio.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:iNatSounds&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://github.com/visipedia/inat_sounds>
- <https://arxiv.org/abs/2506.00343>
- <https://arxiv.org/abs/2605.14031>
- <https://github.com/cvl-umass/iNatSounds>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fine-tune BirdMAE or other large bioacoustic encoders with the multi-label plus mean-teacher recipe that gave the best mAP.
- Cross-domain import (fine-grained vision): hierarchical taxonomic losses and test-time augmentation over crops of long recordings.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Perch 2.0, AVEX, NatureLM-audio and similar encoders were trained on iNaturalist audio, which can include test recordings.
- Geo-prior results are a separate track; do not mix them with audio-only numbers.
- mF1 here picks the best threshold per species on test (optimistic); it is not a deployable threshold.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/inatsounds-test-map.md
```

Already set up? Say `run V3R1T4S on inatsounds-test-map`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `inatsounds-test-map`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
