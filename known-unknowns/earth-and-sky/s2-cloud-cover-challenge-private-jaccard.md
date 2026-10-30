# On Cloud N (Sentinel-2 cloud cover challenge): beat the winning 0.8974 Jaccard on the released private test split

🌍 **Earth and sky** · standard · tractability ★★☆☆☆ · compute: laptop-days (about 11.7k training and 11k test 512x512 four-band Sentinel-2 chips, tens of GB; U-Net/SegFormer training on one GPU or Apple-silicon for 1-3 days) · open as of 2026-10-30

## The problem

The 'On Cloud N: Cloud Cover Detection Challenge' (DrivenData competition 83, Dec 2021-Feb 2022, 848 participants; Radiant Earth Foundation with Microsoft AI for Earth) asked for a per-pixel cloud mask for each 512x512 Sentinel-2 L2A chip (bands B02, B03, B04, B08; extra bands from the Planetary Computer allowed). The score is the Jaccard index summed over all pixels in the scoring set (total intersection / total union, not a per-chip mean). Final private scores: 0.8974 (adityakumarsinha), 0.8972 (Team IG NB: XCZhou, cloud_killer, Sunyueming, mymoon, windandcloud), 0.8961 (Victor). Their public scores were 0.8988, 0.8986 and 0.83975. Radiant Earth released the full dataset under CC-BY-4.0 on Source Cooperative (radiantearth/cloud-cover-detection-challenge/final). It includes private/test_features and private/test_labels for all 10,980 test chips, plus private/pub_sub_idx.csv, which marks each chip as public (5,490) or private (5,490). So the official private score can be recomputed offline. Labels went through expert validation before release; label value 255 means nodata. The 1st-place code (U-Net EfficientNet-B1 and SegFormer-B1 fold ensembles) is public in drivendataorg/cloud-cover-winners, and its 1st-place README links the final weights in a public Google Drive folder (reachable on 2026-10-30). Open task: a private-split Jaccard strictly above 0.8974.

## What counts as a win

Binary masks (uint8, 0/1, 512x512) for all 5,490 chips that private/pub_sub_idx.csv marks public == FALSE. They come from a model trained only on final/public/train_features and train_labels (11,748 chips), optionally with other Sentinel-2 bands of the same chips and dates from the Planetary Computer as the challenge rules allowed. Openly available pretrained backbones with no cloud labels (ImageNet or ADE20k weights, as the winners used) are allowed. No other cloud-labelled data that overlaps the test chips may be used, and the model and threshold are frozen before any test label is read. The skeptic computes the aggregate Jaccard on those chips (total intersection / total union over all pixels, excluding pixels whose label is 255). It must be STRICTLY HIGHER (direction: max), by at least 0.002, than the larger of (a) 0.8974, the 1st-place private score in the README at https://github.com/drivendataorg/cloud-cover-winners, re-fetched immediately before claiming, and (b) the skeptic's rescoring, with the same script and chips, of the 1st-place released ensemble (weights linked from that repository's 1st-place README), if those weights can still be downloaded. The released labels were expert-validated and may differ from those scored in 2022. It must also beat any private-split Jaccard on this dataset published since.

## Partial wins

- **p1:** Re-run the 1st-place released code and weights (linked from its README) on the 5,490 private chips. Publish the standalone scoring script, the 255 handling used, the per-chip intersection and union counts, and the resulting private-split Jaccard, so that the skeptic can reproduce that number to within 0.0005.
- **p2:** Private-split Jaccard >= 0.8961 (3rd place) with a single model (no ensemble), trained in under 24 hours on one laptop or consumer GPU.
- **p3:** Whole-test (all 10,980 chips) Jaccard strictly above the skeptic's whole-test rescoring of the 1st-place released ensemble.

## How a win is checked

The skeptic downloads test_labels and pub_sub_idx.csv by plain GET from data.source.coop/radiantearth/cloud-cover-detection-challenge/final/private/ and scores the claimed masks with a standalone numpy script (total I/U over private chips, 255 excluded). As a calibration, the skeptic re-scores the 1st-place released weights the same way, and audits the training code for any read of test_labels. Scoring takes minutes; re-running the 1st-place inference takes about an hour on a GPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/drivendataorg/cloud-cover-winners>

## Sources

- <https://github.com/drivendataorg/cloud-cover-winners>
- <https://www.drivendata.org/competitions/83/cloud-cover/page/398/>
- <https://source.coop/radiantearth/cloud-cover-detection-challenge>
- <https://data.source.coop/radiantearth/cloud-cover-detection-challenge/final/private/pub_sub_idx.csv>
- <https://doi.org/10.34911/rdnt.hfq6m7>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: larger modern encoders (ConvNeXt, EfficientNetV2, SegFormer-B3+) with multi-fold ensembling and flip/rotate test-time augmentation. The top three are separated by only 0.0013, so variance reduction matters.
- Use the extra bands the rules allowed (B01, B05-B07, B8A, B09-B12 from the Planetary Computer). Cirrus-sensitive and SWIR bands separate thin cloud from bright ground better than RGB-NIR.
- Cross-domain import (noisy-label learning): labels were crowd-drawn then expert-corrected. Use loss reweighting by label confidence, or co-teaching, and check fold-level disagreement maps.
- Cross-domain import (medical image segmentation): boundary-aware losses (Lovasz-hinge, which directly optimises the Jaccard metric) and nnU-Net-style automatic configuration.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Score only the 5,490 private chips (pub_sub_idx public == FALSE) when comparing with 0.8974. Public-split or whole-test numbers are not like for like.
- The metric is aggregate over pixels, not a per-chip mean. Per-chip mean IoU numbers in papers are a different metric.
- Label value 255 is nodata in the released labels. The competition page says missing label values were set to 0 during scoring, so verify via p1 that your nodata handling reproduces the winner's score.
- Tuning thresholds or choosing checkpoints on the released test labels is leakage. Use folds of the training set.
- Margins between the top entries are around 0.001. Report several seeds.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/s2-cloud-cover-challenge-private-jaccard.md
```

Already set up? Say `run V3R1T4S on s2-cloud-cover-challenge-private-jaccard`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `s2-cloud-cover-challenge-private-jaccard`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
