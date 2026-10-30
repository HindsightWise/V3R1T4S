# Moonstone lunar benchmark: beat MG-MAE on crater segmentation, mare segmentation or geologic-unit classification on the fixed split

🪐 **Planets and moons** · standard · tractability ★★☆☆☆ · compute: laptop-days (the repository's downstream scripts read patch pixels from pretraining/mmap, about 123 GB, and split metadata from benchmark/lunar_patches_v4.h5, about 75 GB: about 200 GB of downloads; one GPU recommended) · open as of 2026-10-30

## The problem

Moonstone (Ayush Prasad and Swarnalee Mazumder; ECCV 2026, arXiv:2607.03644) is a 28-channel, 128 pixel/degree global lunar data cube (LRO WAC, LOLA, Diviner, Mini-RF, Chandrayaan-1 M3, GRAIL, Lunar Prospector GRS, Clementine) with a benchmark of 16,200 patches and a fixed 70/15/15 split (11,340 / 2,430 / 2,430), released on Hugging Face (ayushprd/Moonstone, CC BY 4.0) with code (MIT). Labels: 49-class geology and 5-class age from the USGS Unified Geologic Map, mare/highland segmentation, and crater segmentation from the Robbins global crater catalogue (craters > 10 km). Table 3 of the paper gives the best test scores, all from the authors' modality-grouped masked autoencoder fine-tuned (MG-MAE): geology accuracy 56.3%, age accuracy 73.2%, crater mIoU 0.768, mare mIoU 0.936; on the geographic split of Table 6 (train within +/-60 deg latitude, test at 70-80 deg; the code's --geo-split option) geology accuracy is 51.2%. The paper says the Hugging Face dataset hosts the pretrained MG-MAE checkpoint, but on 2026-10-30 no checkpoint file was in the dataset and the GitHub repository had no releases. Two later papers (LunarFM, arXiv:2607.22408; SomBench, arXiv:2609.13277) cite it but report no results on its tasks (full texts checked 2026-10-30). Open task: beat MG-MAE on one of these tasks.

## What counts as a win

A saved bundle (code, config, seeds, weights or exact recipe, per-patch test predictions) where: (1) the model is trained only on the train and val patches of benchmark/lunar_patches_v4.h5 (the fixed split), using only the input channels of the benchmark patches and no label raster (geologic_units.tif, mare_mask.tif, crater_mask.tif or the Robbins catalogue) as input; any self-supervised pre-training may use the pretraining cube; (2) the metric is computed with the Moonstone repository's evaluation code for the task; (3) the mean over 3 seeds beats the Table 3 value for that task by the stated margin: geology accuracy >= 57.3%, age accuracy >= 74.2%, crater mIoU >= 0.778, or mare mIoU >= 0.943, or, on the geographic split, geology accuracy >= 52.2%; (4) no later paper reports a higher value on the same split (checked immediately before claiming).

## Partial wins

- **p1:** A reproduction of the MG-MAE fine-tuned crater mIoU within 0.02 of 0.768 with the released code (pre-training MG-MAE yourself, since no weights are released), all logs saved.
- **p2:** A model without any pre-training (trained from scratch on the train split only), scored as in (2) as a mean over 3 seeds, that beats the paper's vanilla-MAE baseline on one task: crater mIoU > 0.668, geology accuracy > 44.8% or age accuracy > 63.5%.

## How a win is checked

Skeptic downloads benchmark/lunar_patches_v4.h5 and the pretraining/mmap arrays the repository's downstream scripts read, runs the saved model on the test patches with the Moonstone evaluation code, recomputes the metric for each seed, and checks the inputs used. A few hours with a GPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2607.03644>

## Sources

- <https://arxiv.org/abs/2607.03644>
- <https://huggingface.co/datasets/ayushprd/Moonstone>
- <https://github.com/ayushprd/Moonstone>
- <https://arxiv.org/abs/2607.22408>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: a U-Net on elevation and slope alone is a strong crater baseline, since craters > 10 km are topographic features.
- Use the geographic split as the honest test: random patch splits let neighbouring patches share craters and units across train and test.
- Cross-domain import (Earth geology mapping): multi-scale context models used to map geologic units from DEMs and multispectral data.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Composition and cross-modal tasks use channels that are also inputs (lpgrs_feo, lpgrs_tio2, Diviner); they are left out of this target for that reason.
- Large craters cross patch boundaries; check that predictions are not scored on padded or NaN-filled regions differently from the paper.
- The repository's task scripts (downstream_dataset.py) read patch pixels from the z-scored pretraining/mmap arrays (about 123 GB) and use lunar_patches_v4.h5 only for the split and patch locations, so 'benchmark/*' alone (about 75 GB) does not run them. If you feed the h5 pixels instead, show that they match the mmap inputs patch for patch.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/moonstone-lunar-benchmark-beat-mg-mae.md
```

Already set up? Say `run V3R1T4S on moonstone-lunar-benchmark-beat-mg-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `moonstone-lunar-benchmark-beat-mg-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
