# BirdSet soundscapes: beat the best published class-mean AP (mean 0.440 over seven test sites) for multi-label bird detection

🐦 **Ecology and bioacoustics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (GPU days to train on Xeno-canto XCM/XCL; the seven test_5s splits total about 320k five-second segments) · open as of 2026-10-30

## The problem

BirdSet (Rauch, Schwinger, Wirth, Heinrich, Huseljic, Herde, Lange, Kahl, Sick, Tomforde and colleagues; ICLR 2025; HF dataset DBD-research-group/BirdSet) trains on focal Xeno-canto recordings and tests on strongly labelled passive-acoustic soundscapes from eight sites: POW (validation) and the test sites PER, NES, UHH, HSN, NBP, SSW and SNE. The metrics are class-mean average precision (cmAP), AUROC and top-1 on each test_5s split. The HF leaderboard results dataset was last updated 2024-09-30 (best mean cmAP 0.37). Perch 2.0 (van Merrienboer, Dumoulin, Hamer, Harrell, Burns, Denton; arXiv 2508.04665) tabulates the strongest published means, verified from the paper HTML on 2026-10-30: BirdMAE-L fine-tuned (Rauch, Heinrich, Moummad, Joly, Sick, Scholz; TMLR 2025) 0.440, Perch 2.0 0.431, Audio ProtoPNet-5 0.424 (0.423 in its Table 3). Audio-only per-site cmAP bests: PER 0.350 (BirdMAE-L FT as rounded in Perch 2.0; 34.64 in the Bird-MAE paper), NES 0.415 (BirdMAE-L FT, 41.50 in the Bird-MAE paper's Table 6; Perch 2.0 rounds it to 0.41), NBP 0.720 (BirdMAE-L FT as rounded in Perch 2.0; 71.69 in the Bird-MAE paper); HSN 0.555 (AudioProtoPNet-20 in Schwinger, McEwen, Kather, Heinrich, Rauch, Tomforde, arXiv 2511.08261, a class-frequency-weighted figure kept as a conservative bar; BirdMAE-L FT has 0.55 but was tuned on HSN); UHH 0.380 and SSW 0.469 (Perch 2.0 random); SNE 0.351 (Perch 2.0 phase I). The best mean AUROC is 0.908 and the best mean top-1 is 0.665 (both Perch 2.0 random). Adversarial training of AudioProtoPNet and ConvNeXt (arXiv 2507.13727) reaches mean cmAP 0.42 at best. FINCH (Ovanger, Harris, Keitt; arXiv 2602.03817) adds a metadata prior and reports UHH cmAP 0.536 on four sites only; this target is audio-only. AVEX (Miron et al., arXiv 2508.11845) and the 2026 attentive-probing study (arXiv 2605.10494) report lower BirdSet scores under probe protocols.

## What counts as a win

Predictions on the seven BirdSet test_5s splits (PER, NES, UHH, HSN, NBP, SSW, SNE), computed from the audio alone (no recording location, date or other metadata at inference), scored with the birdset package's cmAP. The model's training data must contain none of the BirdSet test soundscape recordings or their source collections. The mean cmAP over the seven sites must be STRICTLY GREATER (direction: max) than 0.440 by at least 0.005. It must also beat any audio-only mean cmAP on the same seven splits that the NOVELTY skeptic finds in a paper or on the BirdSet leaderboard. Training data must be declared (BirdSet DT/MT/LT or other public focal recordings). POW may be used for selection. Deliverables: code, weights, per-segment test scores and the metric output.

## Partial wins

- **p1:** Beat the audio-only per-site cmAP best on at least one site by 0.01 or more (PER 0.350, NES 0.415, UHH 0.380, HSN 0.555, NBP 0.720, SSW 0.469, SNE 0.351), under the same data rules.
- **p2:** Audio-only mean AUROC over the seven sites above 0.908, or mean top-1 above 0.665, under the same data rules.

## How a win is checked

The skeptic loads the HF test_5s splits with the pinned birdset version and recomputes cmAP, AUROC and top-1 from the saved scores. They re-run inference on two sites and audit the training manifest against the test soundscape sources.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:BirdSet&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://github.com/DBD-research-group/BirdSet>
- <https://huggingface.co/datasets/DBD-research-group/BirdSet>
- <https://arxiv.org/abs/2508.04665>
- <https://arxiv.org/abs/2508.11845>
- <https://huggingface.co/datasets/DBD-research-group/Leaderboard-Results>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensemble BirdMAE fine-tuning with Perch 2.0 prototype heads; they win different sites.
- Cross-domain import (speech): soundscape-style augmentation that mixes focal clips with real background noise, plus pseudo-labelling of unlabelled passive-acoustic audio.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- AVEX's training mix lists Sapsucker Woods soundscapes, the source of the SSW test site; models trained on such data are contaminated for that site.
- cmAP ignores classes absent from a split; compare only against the package's implementation.
- The HF leaderboard numbers are rounded to two decimals and older than the paper tables.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/birdset-soundscape-cmap.md
```

Already set up? Say `run V3R1T4S on birdset-soundscape-cmap`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `birdset-soundscape-cmap`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
