# 🌋 Herculaneum scrolls

Ink detection and surface segmentation on the public Vesuvius Challenge data.

**8 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★☆☆ | [Scroll CT compression with random access: beat volcomp's rate-distortion on its 54 held-o…](vesuvius-ct-codec-random-access.md) | harvest | laptop-hours (CPU only; the held-out set is 54 raw uint8 128³ chunks, 108 MiB, read directly from the public S3 zarr) |
| ★★☆☆☆ | [Herculaneum optical-profilometry ink segmentation: beat the Sci. Rep. 2026 nnU-Net held-o…](vesuvius-profilometer-ink-dice.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Herculaneum 9 µm ink detection on a never-seen scroll: beat every public 9 µm model's AUC…](vesuvius-9um-ink-never-seen-pherc0841.md) | standard | laptop-days (one consumer GPU with 12-16 GB: a 40k-78k-iteration run of the ink_9um architecture takes about 3-10 GPU-hours; streams tens of GB of public surface volumes from S3; scoring the three segments is laptop-minutes) |
| ★★☆☆☆ | [Papyrus fiber tracing on Scroll 1 (PHerc. Paris 4, 2.4 µm): beat the published automated…](vesuvius-scroll1-fiber-tracing-afv.md) | harvest | laptop-days at best (one consumer GPU; tracing covers five cube regions and every 512³ block of the held-out band z 45,000-48,500: about 11,000 blocks inside the mask, roughly 1.3-1.4 TB of level-0 uint8 CT to stream for a level-0 tracer (estimate from the S3 listing of z-chunk 360: 165 stored chunk rows of up to 167 chunks) and 8x (level 1) to 64x (level 2) less for a tracer that reads a coarser level; the 11.1 GB published AFV is read by HTTP range requests; the p1/p2/p3 filters and all scoring take laptop-minutes to laptop-hours) |
| ★★☆☆☆ | [Papyrus surface detection: beat the released Kaggle-2026 1st-place nnU-Net (surface_m7_nn…](vesuvius-surface-topo-holdout.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Herculaneum 9 µm ink detection within a scroll: beat every public model's average precisi…](vesuvius-ink9um-validation-masks-buffered.md) | harvest | laptop-hours (one consumer GPU: the official aligned21_hybrid_3d2d recipe trains in about 3 h on an RTX 5090 and 9.5 h on an RTX 5070 Ti; full-canvas inference on the three segments takes minutes; pooled inputs are 1-2 GB per segment, streamed from S3) |
| ★★☆☆☆ | [Herculaneum fragment ink detection: beat the 2023 Kaggle winners' own weights on the rele…](vesuvius-frag4-ink-f05-holdout.md) | harvest | laptop-hours |
| ★☆☆☆☆ | [Herculaneum papyri: first legible letters in one of the 21 still-unread Vesuvius Challeng…](vesuvius-first-letters-unread.md) | standard | needs cluster |

← [All categories](../README.md)
