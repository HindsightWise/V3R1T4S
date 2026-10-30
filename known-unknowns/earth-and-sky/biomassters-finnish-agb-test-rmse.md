# BioMassters (Finnish forest biomass from Sentinel-1/2 time series): beat the best published whole-test average RMSE (27.43, TESSERA) on the released test labels

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: needs cluster (about 216 GB of training and 73 GB of test features; the winning model trained 8 days on 2 A100 GPUs, though smaller models fit one GPU workstation) · open as of 2026-10-30

## The problem

The BioMassters challenge (DrivenData competition 99, Nov 2022-Jan 2023, 976 participants; Nascetti, Yadav, Brodt, Qu, Fan, Shendryk, Shah, Chung and Lipstein, NeurIPS 2023 Datasets and Benchmarks) asks for yearly peak above-ground biomass (AGB, Mg/ha) on a 10 m grid for each 2,560 m chip in Finnish forests. Inputs are 12 monthly Sentinel-1 (4 bands) and Sentinel-2 (11 bands including cloud probability) images. Labels are LiDAR-derived AGB maps calibrated with field plots (Finnish Forest Centre). The metric is per-chip RMSE averaged over the 2,773 test chips, with zero pixels included. Private scores: 27.628 (kbrodt: tf_efficientnetv2_l U-Net encoder shared over months, self-attention aggregation), 27.68 (Team Just4Fun: qqggg, HongweiFan; SWIN UNETR), 28.04 (yurithefury; UNet++ ensemble), 31.08 (MATLAB bonus, Team D_R_K_A: kaveh9877, AZK90). The full dataset, including test_agbm.tar (730 MB of test labels), is on Hugging Face (nascetti-a/BioMassters, CC-BY-4.0, not gated). The public/private split is not published, so the honest comparison is on the whole test set. The BioMassters paper (Table 2) gives whole-test scores for the top three: 27.49 (1st place, described there as a U-TAE adaptation), 27.53 (Swin UNETR) and 27.92 (U-Net++ ensemble). The Prithvi-EO-2.0 paper (Szwarcman et al., arXiv:2412.02732 v3, Table XIII) quotes the same 27.49; its own best (Prithvi-EO-2.0-300M, 12 Sentinel-2 frames, LoRA) is 33.40. The lowest whole-test value found is 27.43 by TESSERA (Zhengpeng Feng, Srinivasan Keshav, Anil Madhavapeddy and co-authors, Cambridge, arXiv:2506.20380 v7, Table 1c): a UNet on frozen TESSERA embeddings, which are computed from the authors' own Sentinel-1/2 retrieval at the chip coordinates rather than from the official features, scored as average per-patch RMSE on the 2,773 test patches. The BioMassters cells in PANGAEA and GEO-Bench-2 use reduced protocols and are not comparable. Open task: whole-test average RMSE strictly below 27.43.

## What counts as a win

Predicted AGB GeoTIFFs (256x256, float) for all 2,773 test chips, with code and weights. The model is trained only on the official training features and train_agbm, with no test AGB used in training or model selection, and frozen before scoring. The skeptic computes RMSE per chip against test_agbm (all pixels, zeros included, as in the challenge metric) and averages over chips. The result must be STRICTLY LOWER (direction: min) than every one of: 27.43, TESSERA's whole-test average per-patch RMSE (arXiv:2506.20380 v7, Table 1c); 27.49, the winning model's whole-test RMSE in the BioMassters paper (NeurIPS 2023, Table 2) and in Prithvi-EO-2.0 (arXiv:2412.02732 v3, Table XIII); and 27.628, the 1st-place private score in the 1st-place README of https://github.com/drivendataorg/the-biomassters, re-fetched before claiming. It must also be lower than any whole-test value published since, on unclipped labels. If the 1st-place released weights (linked from its README) can still be downloaded, it must also be lower than the skeptic's whole-test rescoring of them.

## Partial wins

- **p1:** Whole-test average RMSE strictly below 27.92 (the 3rd-place U-Net++ ensemble's whole-test score in the BioMassters paper, Table 2) with a model trained in under 72 hours on a single consumer GPU.
- **p2:** Whole-test average RMSE strictly below 31.08 (MATLAB bonus winner) with no neural network, e.g. per-pixel gradient boosting on temporal composites.

## How a win is checked

The skeptic downloads test_agbm.tar from huggingface.co/datasets/nascetti-a/BioMassters, scores the claimed GeoTIFFs with a standalone numpy script implementing per-chip RMSE averaged over chips, and checks the file count (2,773) and shape. They audit the data loader for any test_agbm read, and re-run inference on a sample of chips from the released weights. Scoring takes minutes; inference takes hours, mostly I/O.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/drivendataorg/the-biomassters>

## Sources

- <https://github.com/drivendataorg/the-biomassters>
- <https://www.drivendata.org/competitions/99/biomass-estimation/page/536/>
- <https://huggingface.co/datasets/nascetti-a/BioMassters>
- <https://nascetti-a.github.io/BioMasster/>
- <https://proceedings.neurips.cc/paper_files/paper/2023/hash/40daf2a00278c4bea1b26cd4c8a654f8-Abstract-Datasets_and_Benchmarks.html>
- <https://arxiv.org/abs/2506.20380>
- <https://arxiv.org/abs/2412.02732>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: the winner's shared-encoder U-Net with month dropout. Swap in modern encoders, and add a temporal-attention decoder and test-time augmentation.
- Use fewer, better inputs: cloud-free S2 median composites plus S1 statistics shrink 12x15 bands to a laptop-sized tensor (the 3rd-place team used 6 composites per year).
- Cross-domain import (forestry allometry): predict canopy height first, then biomass through a learned allometric head. LiDAR-derived AGB is itself height-driven.
- Cross-domain import (super-resolution): treat 10 m AGB as dense regression, with losses that penalise blur (gradient losses), since RMSE is dominated by high-biomass pixels.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The metric averages per-chip RMSE; it is not a pooled pixel RMSE. These differ substantially.
- The challenge counts zero pixels whether they are true zero biomass or missing data. Do not mask them.
- Private-split scores (27.628) and whole-test scores are not identical. The winner's whole-test figure is 27.49 (BioMassters paper, Table 2), and the best whole-test figure found is TESSERA's 27.43. Compare whole-test with whole-test.
- TESSERA also reports figures with labels clipped at 500 t/ha (26.61, against 25.90 for the released winner weights). Clipped-label numbers are a different target and are not comparable.
- RMSE numbers from PANGAEA, GEO-Bench-2 or Atomizer-style benchmarks use subsets, crops or normalised targets and are not comparable.
- The data are very large (about 290 GB). Check the archive checksums, and do not let an incomplete download silently drop months.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/biomassters-finnish-agb-test-rmse.md
```

Already set up? Say `run V3R1T4S on biomassters-finnish-agb-test-rmse`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `biomassters-finnish-agb-test-rmse`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
