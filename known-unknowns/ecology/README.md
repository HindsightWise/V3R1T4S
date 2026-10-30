# 🐦 Ecology and bioacoustics

Species identification, bioacoustics, camera traps and biodiversity benchmarks with released labels.

**9 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [AnuraSet neotropical frog calls: beat the best published test macro F1 (60.8, Mixture of…](anuraset-multilabel-macro-f1.md) | standard | laptop-hours (11.4 GB zip of 93k 3-second clips; a 3M-parameter MobileNetV3 trains from scratch) |
| ★★★☆☆ | [BEANS animal-sound benchmark: beat the best published test score on one of seven freely d…](beans-animal-datasets-per-task-best.md) | harvest | laptop-hours to laptop-days per dataset (about 300 GB for all BEANS data; frozen-encoder probes run on CPU) |
| ★★★☆☆ | [NCEAS/disdat species distribution benchmark: beat the best published presence-absence AUC…](nceas-disdat-presence-only-sdm-auc.md) | standard | laptop-hours (disdat point data a few MB; optional OSF raster grids for spatial-context models) |
| ★★☆☆☆ | [SAGE global species distribution benchmark: beat the best overall test AUROC (85.9, rando…](sage-global-sdm-test-auroc.md) | standard | laptop-days (3.8 GB benchmark tar plus 10 GB of GBIF presence-only records; the paper's multi-species DeepSDM trains in about 17 GPU-minutes) |
| ★★☆☆☆ | [SatBird USA-summer bird encounter rates: one model that beats every published test metric…](satbird-usa-encounter-rates.md) | standard | needs cluster (GPU days for Sentinel-2 patch models; tabular or embedding models run on a laptop) |
| ★★☆☆☆ | [iNatSounds 2024: beat the best published test mAP (65.4) for file-level species ID across…](inatsounds-test-map.md) | standard | needs cluster (one GPU for 1-3 days; 133 GB of audio: 81 GB train, 25 GB val, 27 GB test on AWS Open Data) |
| ★★☆☆☆ | [BirdSet soundscapes: beat the best published class-mean AP (mean 0.440 over seven test si…](birdset-soundscape-cmap.md) | harvest | needs cluster (GPU days to train on Xeno-canto XCM/XCL; the seven test_5s splits total about 320k five-second segments) |
| ★★☆☆☆ | [FASD13 few-shot animal sound detection: beat DRASDIC's 5-shot event F1 averaged over the…](fasd13-few-shot-animal-sound-detection.md) | standard | laptop-days (about 16 GB of audio on Zenodo; inference-only methods run on CPU, larger models want a GPU) |
| ★★☆☆☆ | [iWildCam2020-WILDS camera-trap species ID: beat the leaderboard's best out-of-distributio…](wilds-iwildcam-ood-macro-f1.md) | standard | needs cluster (one GPU for 1-3 days per replicate; ~11 GB of camera-trap images via the wilds package) |

← [All categories](../README.md)
