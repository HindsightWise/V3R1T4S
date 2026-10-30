# ExoMiner++ TESS 2-minute TCE vetting benchmark: beat the published 10-fold cross-validated PR-AUC (0.976) on the 57,162 labelled SPOC TCEs with the released folds

🪐 **Planets and moons** · standard · tractability ★★☆☆☆ · compute: laptop-days (the released TFRecord inputs are 19 GB; a CNN trains in hours per fold on CPU or an Apple GPU, ten folds; or rebuild inputs from MAST SPOC DV products) · open as of 2026-10-30

## The problem

ExoMiner++ (Valizadegan, Martinho, Jenkins, Twicken, Caldwell, Maynard, Wei, Zhong, Yates, Donald, Collins, Latham et al.; AJ 170, 2025, doi:10.3847/1538-3881/ae03a4; code at github nasa/ExoMiner) classifies TESS SPOC 2-minute threshold-crossing events (sectors 1-67) as planet or non-planet. Zenodo 15466292 releases the labelled catalogue: 57,162 TCEs (KP 1,835, CP 1,846, EB 12,738, NTP 39,009, NEB 816, FP 793, NPC 93, BD 32), a fold column 0-9 grouping TCEs by target star (17,206 stars, none split), the out-of-fold score of the TESS+Kepler individual model, and 19 GB of TFRecord inputs. Recomputed on 2026-10-30 with positives = KP or CP and all other labels negative: PR-AUC 0.9704, ROC-AUC 0.9971, precision/recall 0.924/0.927 at 0.5, matching the 'TESS+Kepler, Individual' row of the paper's Table 6 (whose FP-subclass recall, 0.887, is reproduced when NEB and NPC count as FP). The best row (TESS+Kepler with multi-sector score aggregation) reports PR-AUC 0.976, ROC-AUC 0.998, precision/recall 0.933/0.951 and FP-subclass recall 0.896; the TESS-only aggregate row reports PR-AUC 0.967. ExoMiner++ 2.0 (arXiv:2601.14877, January 2026) uses a different 2-minute plus FFI set with 5 folds and reports lower values. The nasa/ExoMiner repository (pushed 2026-10-13) still names ExoMiner++ as its current 2-minute model. Open task: a vetter with a higher cross-validated PR-AUC on the same labels and folds.

## What counts as a win

A saved bundle: frozen training code, the ten fold models, and an out-of-fold score for each of the 57,162 TCEs in the labelled-TCE catalogue CSV of Zenodo 15466292 (exominerplusplus_catalog_labeled_tces_s1-s67_tess-spoc-2min_complete_1-14-2025_1039.csv; SHA-256 8c97e5bff6019cd7bd979e7ad21423448d67299bdf47a98f8510d25db4f197b2 as downloaded 2026-10-30). The score of a TCE in fold k comes from a model that never used fold k for training, validation, early stopping or normalisation statistics. Allowed inputs: public TESS photometry and SPOC DV products, Kepler data, and TIC/Gaia stellar parameters. Forbidden: TOI, CTOI or ExoFOP dispositions and comments, TFOPWG or follow-up results, and the catalogue's label and score columns. Win: average-precision PR-AUC over all 57,162 TCEs (positives = KP or CP, every other label negative) strictly greater (direction: max) than 0.9765, so above any value that rounds to the published 0.976, with ROC-AUC >= 0.9975, both recomputed by the skeptic. The result must also beat any value on this labelled set in later papers: re-fetch the Zenodo record and the nasa/ExoMiner repository and search ADS/arXiv for ExoMiner++ citations (last 24 months) before claiming.

## Partial wins

- **p1:** Out-of-fold PR-AUC strictly above 0.9704 (the released TESS+Kepler individual-model scores) without multi-sector score aggregation.
- **p2:** Trained on TESS data only (no Kepler examples), an out-of-fold PR-AUC strictly above 0.9675 (above the paper's TESS-only aggregate row, 0.967).
- **p3:** At threshold 0.5, precision >= 0.933 and recall >= 0.951 overall, together with a correctly-rejected (score <= 0.5) fraction of the FP subclass, taken as the FP, NEB and NPC labels together (1,702 TCEs, as in the paper's Table 6), strictly above 0.896 (the paper's best).
- **p4:** PR-AUC >= 0.9704 using only phase-folded flux views and scalar DV statistics (no difference images, centroids or periodograms).

## How a win is checked

Skeptic checks the catalogue hash, verifies that the fold assignment is the released one and that no fold-k TCE is in model k's training data, retrains at least two folds from the frozen code with new seeds, and recomputes PR-AUC and ROC-AUC on all out-of-fold scores. Hours for the metrics, a day or two to retrain folds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://doi.org/10.5281/zenodo.15466292>

## Sources

- <https://doi.org/10.5281/zenodo.15466292>
- <https://doi.org/10.3847/1538-3881/ae03a4>
- <https://github.com/nasa/ExoMiner>
- <https://archive.stsci.edu/tess/bulk_downloads/bulk_downloads_ffi-tp-lc-dv.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: retrain the ExoMiner++ architecture with modern augmentation (period-phase jitter, odd-even swaps) and an ensemble over seeds; ensembles alone often add a few thousandths of PR-AUC.
- Gradient-boosted trees on SPOC DV scalar statistics stacked with CNN scores; label noise in CP and NTP rewards robust losses.
- Cross-domain import (noisy-label learning in medical imaging): co-teaching or confident learning to down-weight TFOPWG labels that are likely wrong, evaluated only on out-of-fold scores.
- Multi-sector aggregation: the paper's aggregation adds about 0.006 PR-AUC; learn the aggregation rather than use the longest-run rule.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- TOI and ExoFOP dispositions are the source of the labels: any feature derived from them is leakage.
- Folds are grouped by target star; re-splitting by TCE leaks multi-sector TCEs of the same star across folds.
- The paper's negatives include NEB and NPC TCEs; dropping them raises PR-AUC (0.979 for the released scores) and is not comparable.
- PR-AUC differences of a few thousandths are within seed noise; report the spread over at least three seeds.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/planetary-science/exominerpp-tess-2min-cv-pr-auc.md
```

Already set up? Say `run V3R1T4S on exominerpp-tess-2min-cv-pr-auc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `exominerpp-tess-2min-cv-pr-auc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
