# Herculaneum 9 µm ink detection within a scroll: beat every public model's average precision on the three official ink_9um validation masks (384 px buffer rule)

🌋 **Herculaneum scrolls** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (one consumer GPU: the official aligned21_hybrid_3d2d recipe trains in about 3 h on an RTX 5090 and 9.5 h on an RTX 5070 Ti; full-canvas inference on the three segments takes minutes; pooled inputs are 1-2 GB per segment, streamed from S3) · open as of 2026-10-30

> 🔒 **Live puzzle with a living setter.** Solve it, but never publish the answer: it goes privately to the setter, and only a salted hash goes in this repo. See [DONT_SPOIL_THE_HUNT.md](../../DONT_SPOIL_THE_HUNT.md).

## The problem

The team defines its within-scroll held-out test itself. The ink_9um labels README (HF bucket scrollprize/datasets, ink_9um/, fetched 2026-10-29) states that 'the three _validation_mask.zarr segments (pherc0139-w016, pherc0814-46527, pherc1667-w029) are the online-validation cases the released checkpoints report metrics on'. The ink tutorial (scrollprize.org/tutorial5) says 'Validation regions are held out, so you can measure whether the model generalizes'. The ink_9um card publishes no metrics and still expects 'substantial gains'. LABELS: 24 aligned segments (2.399 µm volumes pooled to about 9.6 µm, 21 slices, annotated at Z=10) and 5 native 9.362 µm PHerc0139 segments. The aligned label directories were re-uploaded on 2026-08-18 after a seam-masking fix (reported in DomRusso2/ink9um-dense). PUBLISHED HELD-OUT NUMBERS. Domenico Russo's ink9um-dense (August 2026 Progress Prize for ink checkpoint benchmarking) scored all 14 released checkpoints with the team's BalancedAccuracy at threshold 0.5 and with AUC. Best released per region: w016 0.8194 / 0.9366, 0814 0.8129 / 0.8970, w029 0.8434 / 0.9334. The spread across the 14 reaches 0.14, and a dense pseudo-label model reaches 0.8539 / 0.9350 on 0814. Alex Clark's inkbench (commit a0ff572, 2026-09-07; September 2026 Progress Prize for ink ensembling) reports full-canvas average precision on the held-out pixels (0814 / w029 / w016): recommended seed42 step-075000 0.839 / 0.901 / 0.622; seed-42 10k-30k weight soup 0.841 / 0.902 / 0.808; output average of all 14 checkpoints 0.860 / 0.927 / 0.808 (mean 0.865). Some public models saw these masks' pixels through another representation of the same papyrus: TRACE (github.com/Jashann/vesuvius-scrolling, runs/trace_manifest_v3.json) trained on the native 9.362 µm renders of 20250108000004-w029 (the physical segment behind pherc0139-w016) and 20260226000000-46527_2um_try2 (behind pherc0814-46527) with the team's whole-segment 2.4 µm maps as soft targets, and for 46527_2um_try2 also with its human ink labels (ink-labels/2.399um-volume-20260309142202/20260918, in the manifest's train split); v8-in's training corpus includes 0814_46527n9, a native render of the 0814 segment; Hecate's documented supervision is the ink bucket, which holds all three segments' labels. Their scores on these masks are presumed contaminated. WHY A BUFFER: the khj1222 audit (docs/17, 2026-08-29) shows that all three masks cut through annotated regions. On w016, 99.1% of held-out pixels lie within two 128 px patches of a training pixel, and the farther ones carry no ink. 0814 is one region split internally. Only w029 has real separation. A model trained next door gains +0.14 F1 (w016) and +0.07 F1 (w029) more on adjacent pixels than on distant ones. OPEN QUESTION: genuine within-scroll generalization to unlabelled regions once adjacency is removed. That is the pseudo-labelling use case. CREDITS: the Vesuvius Challenge team (labels, ink_9um, recipe, Hecate); Domenico Russo (ink9um-dense, Reader v2, Reader V3); Alex Clark (inkbench); the khj1222 repository (scorecard and audit); Youssef Nader (v8-in); Erwin Nieuwlaar (dense-native); Jashanjot Singh Gill and Nhat Nam Tran (TRACE). DATA: CC BY-NC 4.0 plus the dl.ash2txt.org terms. A human must accept them before any download.

## What counts as a win

PROTOCOL (pinned). score_val9.py is frozen in METRIC.sha256 before any scoring. It takes a full-canvas 9.6 µm ink map per validation segment, computed from the official inputs: 2.399 µm surface volumes pooled by villa scripts/prepare_9um_isotropic_input.py at a pinned villa commit, as the ink_9um card prescribes. It computes average precision (step-wise, as in sklearn average_precision_score) of the map against inklabels > 0 on the annotated plane, over pixels with validation_mask > 0, using label files pinned by sha256 from the current HF bucket. BUFFER RULE. The buffer zone of a validation segment is every canvas pixel within 384 px (Euclidean, on the 9.6 µm label grid) of any of its validation-mask pixels. Training may use any public labels (the official ink_9um supervision, reader-v2-labels, ink9um-dense-labels, team 2.4 µm maps), but no pixel inside a buffer zone may be supervised, and no pixel of any other segment or representation (native renders, other meshes) may be supervised if its 3D position, mapped through its tifxyz mesh, lies within 75 µm of the 3D position of a buffer-zone pixel mapped through the validation segment's mesh. This excludes the native twins of the validation segments (for example 20250108000004-w029 and 20260226000000-46527_2um_try2 at 9.362 µm). No pseudo-labels, team maps or fine-tuning may supervise excluded pixels. GATE A. Under the same protocol, the scout scores all 14 ink_9um checkpoints, their 14-checkpoint output average, the seed-42 10k/20k/30k weight soup, ink9um-dense (control, all-7, w016excluded), Reader v2, Reader V3, Nieuwlaar dense-native, Hecate 9.6 µm, v8-in, TRACE sA, sB, v3A and v3B (Jashann/vesuvius-scrolling release v1.0), A-hn (Prodigle/pherc0306b-ink-ahn) and any other public 9 µm ink checkpoint found on the day the baselines are frozen, in a hash-locked BASELINES.json that also marks each baseline as presumed contaminated (trained on validation-mask pixels in any representation) or not. B_m = the best AP on mask m over all of these that are not presumed contaminated, ensembles of them included. The contaminated ones are scored and reported as references, not as B_m, because a model trained on a validation segment's own labels or maps measures memorisation, not the buffered generalisation this target asks for. GATE B. No initialisation from any checkpoint trained on supervision inside a buffer zone or its 3D exclusion: every released ink_9um, Reader, ink9um-dense, Nieuwlaar dense-native and TRACE checkpoint, Hecate, v8-in (0814_46527n9) and A-hn (fine-tuned from v8-in) are excluded. leak_audit over the label manifest proves the buffer. Validation masks are never read during training (no online validation, no best_val checkpoint). GATE C. One network, with its checkpoint sha256 declared before the first scoring; every scoring is logged. SUCCESS: AP >= B_m + 0.01 on each of the three masks, and mean AP >= the best mean of any baseline not presumed contaminated + 0.02; the claim also reports AP against every contaminated reference. This is an internal benchmark. Official credit comes only through a Progress Prize to the human.

## Partial wins

- **p1:** Distillation without the buffer. One network trained under the official rules (validation-mask pixels never supervised in any representation, no buffer, initialisation from the released ink_9um checkpoints or any other checkpoint not presumed contaminated allowed) and Gate B's selection rules (no online validation, no best_val checkpoint), whose AP on each of the three masks is >= the larger of the Gate A AP of the 14-checkpoint output average and the best Gate A AP of any single network not presumed contaminated. In inkbench, soups approach that average but do not exceed it on all three.
- **p2:** Buffered single model against released singles. One network trained under the buffer rule and Gate B whose AP on each of the three masks is >= the best of the 14 released single checkpoints, as measured in Gate A.

## How a win is checked

The skeptic: (1) downloads the three segments' label and mask zarrs and checks the pinned sha256; (2) recomputes the buffer zones from the validation masks and the 75 µm 3D exclusion through the tifxyz meshes, and checks every supervised pixel in the training manifest against both; (3) recomputes AP from the frozen maps and from two stored baseline maps with score_val9.py, requiring |difference| < 1e-6; (4) re-runs the claimed checkpoint on w029 at the declared settings (minutes on a consumer GPU) and requires Pearson r > 0.99 with the frozen map; (5) re-reads the HF ink_9um bucket README, the ink_9um card, the Reader, inkbench, TRACE and khj1222 repositories and the Hugging Face ink-model listings for newer baselines or changed labels.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/Alex55288/inkbench>

## Sources

- <https://huggingface.co/buckets/scrollprize/datasets/tree/ink_9um>
- <https://huggingface.co/scrollprize/ink_9um>
- <https://scrollprize.org/tutorial5>
- <https://github.com/DomRusso2/ink9um-dense>
- <https://github.com/Alex55288/inkbench>
- <https://github.com/khj1222/vesuvius-challenge/blob/main/docs/17_holdout_audit.md>
- <https://github.com/khj1222/vesuvius-challenge/blob/main/docs/14_ink9um_scorecard.md>
- <https://scrollprize.org/winners>
- <https://github.com/Jashann/vesuvius-scrolling/blob/main/runs/trace_manifest_v3.json>
- <https://huggingface.co/datasets/YoussefMoNader/ink-8um-v8-patchpack>
- <https://huggingface.co/scrollprize/hecate>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Distil the 14-checkpoint output average and the soup into one network on non-validation pixels (p1), then repeat the distillation under the buffer.
- Replace the deleted neighbourhood supervision with dense labels from other scrolls and from regions outside the buffer (reader-v2-labels, ink9um-dense-labels).
- Use depth-window jitter and average both layer orders, as the ink_9um card suggests. Early checkpoints generalise better: khj docs/14 shows 75k overtrains.
- Report AP by distance band from the nearest official supervision pixel (the khj docs/17 strata) to show the gain is not adjacency.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The official masks leak by adjacency. Without the buffer, wins mostly measure memorised neighbourhoods (khj docs/17).
- Balanced accuracy at 0.5 can prefer a visually worse, smeared map (ink9um-dense section 4). This target uses threshold-free AP instead.
- best_val_balanced_accuracy checkpoints and online validation select on these same masks, so both are forbidden.
- pherc0139-w028 (aligned) and w044 (native) are the same physical segment under two keys. Neither is a validation segment, but do not count them as independent evidence.
- Labels changed on 2026-08-18 with the seam fix. Pin the current files by sha256 and re-check them before claiming.
- Data terms: a human accepts the Vesuvius Challenge terms before any download. Labels and renders are never redistributed.
- A buffer drawn only on the aligned canvas misses other representations of the same papyrus: TRACE trained on the native 9.362 µm renders of the w016 and 0814 validation segments with whole-segment team maps, and v8-in on a native 0814 render. Hence the 3D exclusion and the contamination flags in Gate A.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/herculaneum-scrolls/vesuvius-ink9um-validation-masks-buffered.md
```

Already set up? Say `run V3R1T4S on vesuvius-ink9um-validation-masks-buffered`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `vesuvius-ink9um-validation-masks-buffered`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
