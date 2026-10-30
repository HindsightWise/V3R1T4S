# Papyrus fiber tracing on Scroll 1 (PHerc. Paris 4, 2.4 µm): beat the published automated fiber volume on precision against dense hand tracing with no loss of recall in the held-out band

🌋 **Herculaneum scrolls** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days at best (one consumer GPU; tracing covers five cube regions and every 512³ block of the held-out band z 45,000-48,500: about 11,000 blocks inside the mask, roughly 1.3-1.4 TB of level-0 uint8 CT to stream for a level-0 tracer (estimate from the S3 listing of z-chunk 360: 165 stored chunk rows of up to 167 chunks) and 8x (level 1) to 64x (level 2) less for a tracer that reads a coarser level; the 11.1 GB published AFV is read by HTTP range requests; the p1/p2/p3 filters and all scoring take laptop-minutes to laptop-hours) · open as of 2026-10-30

> 🔒 **Live puzzle with a living setter.** Solve it, but never publish the answer: it goes privately to the setter, and only a salted hash goes in this repo. See [DONT_SPOIL_THE_HUNT.md](../../DONT_SPOIL_THE_HUNT.md).

## The problem

Fibers give the spiral fitter its connectivity. scrollprize.org/2026_open_problems (updated 2026-10-14) asks for robust fiber tracing with an explicit preference: 'a tracer that confidently follows fewer fibers correctly is more useful than one that follows more fibers with a higher error rate.' BASELINE: the automated fiber volume fibers.afv (SQLite with rtree, 11,127,046,144 bytes, 2026-10-19) in the team's Scroll 1 spiral dataset PHercParis4/representations/spiral/20260411134726-spiral-dataset-20261019084150/. The same dataset holds eval_fibers/: 645 human-annotated fiber files, 299 MB. According to the afv-audit report, the AFV holds 931,104 fibers from the neural fiber follower checkpoint polar_tokens_a3_ms_slim_dagger_b32x2_50k/ckpt_050000.pt, traced over z 28,000-68,000 base voxels; the tracer code is in villa under vesuvius/neural_tracing/tracers/fibers. The same report says every fiber-follower config holds z 45,000-48,500 out of training (data/fibers.py training_state_allowed). Related community AFVs sit in dl.ash2txt.org/community-uploads/qual/AutomatedFiberVolumes/: Paris4_v1.afv (2026-10-05), Paris4_1mm_v2.afv and Paris4_all_v2.afv (2026-10-25/26). Judging by the handle, they come from Samir Lerognon (@qualzz), who won the September 2026 $20,000 Progress Prize for automated fiber extraction. His fiber models (huggingface.co/Qualzz20/afv_fiber_9um and _v2) are fine-tuned from scrollprize/fiber_hz_vt, which the open-problems page describes as trained on the fibers hand-traced in WebKnossos on the older 7.91 µm scans, and the lasagna-fiber card says SD2 was 'trained on S1A NML fibers registered to the PHercParis4 2.400 µm, 78 keV volume' (SD1 is a separate 's1a' run). These models descend from the fiber-skeletons NMLs that include the five cubes used below as the precision judge (SD1 presumably), so the community AFVs' in-cube precision is presumed contaminated. villa's fiber dataset config paris50.json holds out val_z [45000, 48500] and also samples two qualzz AFVs of other scrolls (0175A_5mm_v1, 1447_5mm_v1). MEASUREMENT: github.com/Rano200/afv-audit (MIT, commit e0710d2, 2026-10-21) scores an AFV two ways. (i) Precision against the five Scroll 1 cubes of the 2025 fiber-skeletons dataset: WEBKNOSSOS NMLs fibers_s1a_00497z_01497y_03997x_256_v00, fibers_s1a_00497z_02497y_02997x_256_v00, fibers_s1a_00997z_02497y_02997x_256_v00, fibers_s1a_08997z_02997y_02497x_256_v00 and fibers_s1a_10997z_02997y_02997x_256_v00, with every fiber traced (550 fibers), mapped into the 2026 frame with the volume's transform.json. AFV fibers are cut into 200-voxel windows, labelled GOOD ( > = 80% of points within tol of a hand fiber) or BAD (<= 20%). (ii) Recall on the eval_fibers stretches inside the held-out band: 375 stretches from 314 fibers, scored on windows of <= 600 voxels. RESULTS.md for the official AFV: 1,052 windows. At tol 10: GOOD 34.8%, BAD 37.9% (null 0.3% / 92.5%). At tol 20: GOOD 71.5%, BAD 17.4% (null 4.6% / 69.6%). Recall at tol 10: single-fiber median 0.94, union median 0.96, single >= 0.7 on 252/375; at tol 20, 288/375. REPORT.md adds: 110 of 138 scorable links (79.7%) join pieces of one hand fiber; following links needs 0.22 chains per 1,000 voxels of held-out human fiber (0.45 pieces without links); an in-sample length filter (L = 3,000) cut the BAD share from 18.1% to 12.2% while removing 15.7% of GOOD windows; two learned window scorers missed the pre-registered AUROC of 0.645 (0.637 and 0.599). A BAD window is an AFV fiber with no hand fiber nearby, so it is either an error or an annotator omission. CREDITS: the Vesuvius Challenge team (2.4 µm ESRF scan, spiral dataset, fiber follower, eval_fibers annotators); the 2025 fiber-skeletons annotators (cubes traced on the EduceLab-Scrolls DLS scan of Scroll 1); Samir Lerognon (automated fiber volumes); Rano200 (afv-audit). DATA: CC BY-NC 4.0, plus the dl.ash2txt.org terms and the EduceLab-Scrolls citation terms. A human must accept them before any download.

## What counts as a win

SCORER: afv-audit @ e0710d2958d792c8424b39c1058acecdaefc15f3, or the scout's re-implementation frozen in METRIC.sha256 that reproduces RESULTS.md for the official AFV exactly (1,052 windows and identical percentages and counts). SUBMISSION: one AFV in the same SQLite schema, produced by a single deterministic tracer run with identical settings over (i) the five cube regions (each cube's 2026-frame bounding box plus a 64-voxel margin) and (ii) every block in BLOCKS.json. BLOCKS.json is the scout's frozen list of 512³ level-0 blocks with z in [45,000, 48,500) that intersect the scroll mask, and each listed block is traced in full. GATE A. BASELINES.json holds afv-audit results for the official fibers.afv and for each community Paris4 AFV (Paris4_v1, Paris4_1mm_v2, Paris4_all_v2). B = the scored AFV with the largest GOOD@10 - BAD@10 among those with single >= 0.7 at tol 10 on at least 252/375 stretches whose fiber model never read the fiber-skeletons NMLs, directly or through an initialisation (today the official fibers.afv; the qualzz AFVs descend from fiber_hz_vt and are scored and reported as contaminated references, not as B). GATE B (leakage). leak_audit.py over manifests and the initialisation chain must show that the tracer's training, tuning and filtering never read the five cube NMLs or their voxelised labels, any eval_fibers file, or any CT or label with base z in [45,000, 48,500). No initialisation from, and no use on PHercParis4 data (as features, probability volumes or teacher labels) of, fiber_hz_vt, lasagna-fiber SD1/SD2, Qualzz20/afv_fiber_9um or _v2, or any other model trained, directly or through a parent checkpoint, on the fiber-skeletons dataset that includes these cubes; their outputs on other scrolls may serve as training data, as in villa's paris50.json. SUCCESS requires all of: window count inside the cubes >= 0.75 x B's; at tol 10, GOOD >= B + 12 points and BAD <= B - 10 points; at tol 20, GOOD >= B + 6 points and BAD <= B - 5 points; recall single >= 0.7 at tol 10 on at least B's count of stretches, and union median at tol 10 >= B's; nulls: shifted-hand-fiber GOOD@20 <= 10%, and shifted-stretch recall single >= 0.7 at tol 20 on <= 5/375. With the official AFV as B, the bars are GOOD@10 >= 46.8%, BAD@10 <= 27.9%, GOOD@20 >= 77.5%, BAD@20 <= 12.4% and >= 252/375 stretches. This is an internal benchmark. Official credit comes only through a Progress Prize awarded to the human.

## Partial wins

- **p1:** Filter only, no new tracing. A deterministic filter of B's fibers (CT, geometry and AFV metadata allowed), with every parameter chosen leave-one-cube-out so the held-out cube's windows are never used for its own fold. It must bring pooled out-of-fold BAD@20 to <= 12.0% while removing <= 10% of GOOD@20 windows, and keep single >= 0.7 at tol 10 on >= 240/375 held-out-band stretches.
- **p2:** Window scorer. A scorer of B's 200-voxel cube windows reaching leave-one-cube-out AUROC >= 0.70 for BAD vs GOOD at tol 20, with a block-bootstrap 95% lower bound > 0.60. afv-audit's pre-registered bar was 0.645; its two learned scorers reached 0.637 and 0.599.
- **p3:** Links. Fiber-to-fiber links, on the claimant's fibers or on B's, of which >= 90% join pieces of the same hand fiber, on >= 130 scorable links in the five cubes (B: 110/138 = 79.7%). The linked chains must not exceed 0.22 per 1,000 voxels of held-out-band human fiber.

## How a win is checked

The skeptic: (1) fetches the five NMLs (about 4.6 MB), the 2026 volume's transform.json and eval_fibers (299 MB); (2) reads the claimant's AFV and the baseline AFVs, locally or by range requests; (3) runs the pinned scorer, about 11 minutes for precision, recall and links on 4 workers; (4) checks BASELINES.json by re-scoring the official AFV, which must give identical numbers; (5) checks that every BLOCKS.json block and every cube region contains traced output; (6) re-runs the tracer on two seeded blocks and one cube region and requires >= 95% of its fiber points to lie within 2 voxels of the submitted ones; (7) runs leak_audit.py; (8) before any claim, re-lists the S3 spiral datasets and the qual uploads for newer AFVs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://vesuvius-challenge-open-data.s3.amazonaws.com/?list-type=2&prefix=PHercParis4/representations/spiral/&delimiter=/>

## Sources

- <https://scrollprize.org/2026_open_problems>
- <https://vesuvius-challenge-open-data.s3.amazonaws.com/?list-type=2&prefix=PHercParis4/representations/spiral/20260411134726-spiral-dataset-20261019084150/&delimiter=/>
- <https://github.com/Rano200/afv-audit>
- <https://github.com/Rano200/afv-audit/blob/main/RESULTS.md>
- <https://github.com/Rano200/afv-audit/blob/main/REPORT.md>
- <https://dl.ash2txt.org/datasets/fiber-skeletons/Dataset001_sk-fibers-20250124/nml/>
- <https://vesuvius-challenge-open-data.s3.amazonaws.com/PHercParis4/volumes/20260411134726-2.400um-0.2m-78keV-masked.zarr/transform.json>
- <https://dl.ash2txt.org/community-uploads/qual/AutomatedFiberVolumes/>
- <https://github.com/ScrollPrize/villa/tree/main/vesuvius/src/vesuvius/neural_tracing/tracers/fibers>
- <https://scrollprize.org/winners>
- <https://scrollprize.org/data_datasets>
- <https://huggingface.co/scrollprize/lasagna-fiber>
- <https://huggingface.co/Qualzz20/afv_fiber_9um>
- <https://github.com/ScrollPrize/villa/blob/main/vesuvius/src/vesuvius/neural_tracing/tracers/fibers/configs/datasets/paris50.json>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conservative stopping: stop or branch-check at H x V weave crossings instead of tracing through them. The masfocl-spec fiber-reconnect study found that about two thirds of real breaks sit at such crossings.
- Fit splines to H/V fiber probability volumes from a model that never saw the fiber-skeletons NMLs (not lasagna-fiber SD1/SD2, fiber_hz_vt or the Qualzz afv_fiber_9um models, which all descend from them; train one on data outside the band and the cubes), then prune short or low-contrast pieces. afv-audit notes that BAD windows sit on short fibers with lower tube contrast.
- DAgger-style training of a follower on data outside the band and the cubes, with confidence-calibrated termination at each step.
- Verify links by CT continuity along the join rather than by end angles: afv-audit found AUROC 0.66 for the angle and 0.55 for the gap.
- Report numbers per cube: for the official AFV, BAD ranges from 7.1% to 29.4% across the five cubes.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- BAD means 'unconfirmed by hand tracing', not proven false. The cubes were traced on the 2023 7.91 µm DLS grid, and per-cube offsets are 2-5 base voxels, so tol 10 is tight; report both tolerances.
- Fewer, shorter windows can inflate precision. The 0.75 x window-count rule and the band recall guard stop coverage being traded for precision.
- eval_fibers and the cube NMLs are public. Any read of them by the tracer, its training or its filter voids the attempt.
- fiber_hz_vt, lasagna-fiber SD1/SD2 ('trained on S1A NML fibers registered to the PHercParis4 2.400 µm volume') and the Qualzz afv_fiber_9um models (fine-tuned from fiber_hz_vt) all descend from these cubes' labels. They are not clean initialisations, nor clean teachers or feature extractors on PHercParis4, and Paris4 AFVs made with them are contaminated in the cubes.
- Base voxels are level-0 voxels of the 2026 2.4 µm volume (z up to 75,784). The cubes live in the 2023 frame and must go through transform.json (matrix inverted), as afv-audit does.
- Data terms: a human accepts the Vesuvius Challenge terms and the EduceLab-Scrolls citation terms before any download. AFVs and NMLs are never redistributed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/herculaneum-scrolls/vesuvius-scroll1-fiber-tracing-afv.md
```

Already set up? Say `run V3R1T4S on vesuvius-scroll1-fiber-tracing-afv`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `vesuvius-scroll1-fiber-tracing-afv`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
