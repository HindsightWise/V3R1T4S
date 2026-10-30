# FASD13 few-shot animal sound detection: beat DRASDIC's 5-shot event F1 averaged over the twelve animal datasets

🐦 **Ecology and bioacoustics** · standard · tractability ★★☆☆☆ · compute: laptop-days (about 16 GB of audio on Zenodo; inference-only methods run on CPU, larger models want a GPU) · open as of 2026-10-30

## The problem

FASD13 (Hoffman, Robinson, Miron, Baglione, Canestrari, Elias, Trapote, Effenberger, Cusimano, Hagiwara, Pietquin; arXiv 2503.00296; Zenodo 15843741; github.com/earthspecies/drasdic_api) is a public evaluation set for few-shot bioacoustic event detection: 13 datasets of 2-12 recordings each. A system sees the audio up to the 5th positive event and must predict the onsets and offsets of the remaining positive events. Scoring is F1 at IoU 0.3, following the DCASE few-shot protocol (Nolasco et al. 2023). Eleven datasets come from earlier studies (AnuraSet, Hawaiian birds, Hainan gibbon, humpback and right whales, katydids, marmosets, Powdermill birds, ruffed grouse, Rana sierrae) and two are new (carrion crow, jumping spider). The paper's per-dataset table (verified from the HTML on 2026-10-30) gives DRASDIC (116M parameters, trained on 8.8k hours of synthetic scenes) an average of 0.445 over all 13. This target uses the 12 animal datasets, leaving out GS (a gunshot set). Over those 12, DRASDIC's mean is 0.433, and the per-dataset bests over all listed models are AS 0.645, CC 0.341, HA 0.587, HG 0.242, HW 0.453, JS 0.302, KD 0.673, MS 0.831, PM 0.474, RG 0.732, RS 0.352 and RW 0.764. The ablation rows report only 13-dataset averages, the best being 0.457 (DRASDIC without pitch/time shifting), with no per-dataset breakdown, so their 12-dataset means are unknown but at most 0.4575 x 13 / 12 = 0.496. No later paper reporting FASD13 was found on arXiv on 2026-10-30.

## What counts as a win

Predicted event lists for every file of the 12 animal datasets of FASD13 (AS, CC, HA, HG, HW, JS, KD, MS, PM, RG, RS, RW), produced under the 5-shot protocol: for each file, only audio and labels up to the end of its 5th positive event may be used. Scored with the DCASE few-shot evaluation code at IoU 0.3, the unweighted mean of per-dataset F1 must be STRICTLY GREATER (direction: max) than 0.496, the largest 12-dataset mean any published DRASDIC variant can have. It must also beat the 12-dataset mean of any model with published per-dataset FASD13 scores that the NOVELTY skeptic finds. No FASD13 audio may be used for training or tuning. Deliverables: code, weights, the prediction files for each of the 12 datasets and the scorer output.

## Partial wins

- **p1:** Beat the per-dataset best listed above on any one of the 12 datasets by at least 0.02 F1, under the same 5-shot rules.
- **p2:** A system with at most 10M parameters whose 12-dataset mean exceeds 0.395 (AVES+linear, 90M parameters).
- **p3:** A 12-dataset mean strictly above 0.443 (DRASDIC's 0.433 plus 0.01), under the same rules.

## How a win is checked

The skeptic downloads the Zenodo zips and runs the claimant's inference on a fresh copy, checking that no labelled support is read beyond the end of each file's 5th positive event. They rescore with the DCASE evaluation code and recompute the 12-dataset mean.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/earthspecies/drasdic_api>

## Sources

- <https://arxiv.org/abs/2503.00296>
- <https://zenodo.org/records/15843741>
- <https://github.com/earthspecies/drasdic_api>
- <https://github.com/c4dm/dcase-few-shot-bioacoustic>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prompted foundation models (DRASDIC) combined with per-file transductive refinement on the query audio.
- Cross-domain import (keyword spotting): query-by-example with dynamic time warping on learned embeddings, tuned only on the DCASE training/validation sets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Unlabelled query audio may be used; ground-truth labels after the 5th positive event may not, so test-time label propagation that reads them is leakage.
- The DCASE validation sets share species with some FASD13 sources; declare all training data.
- Several FASD13 datasets have only 2-4 files, so per-dataset F1 is noisy.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/fasd13-few-shot-animal-sound-detection.md
```

Already set up? Say `run V3R1T4S on fasd13-few-shot-animal-sound-detection`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fasd13-few-shot-animal-sound-detection`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
