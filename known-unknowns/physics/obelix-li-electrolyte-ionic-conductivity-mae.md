# OBELiX experimental Li solid-electrolyte ionic conductivity: beat the published best test MAE of 1.59 log10(S/cm) on the official 121-entry test split

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-minutes · open as of 2026-10-30

## The problem

OBELiX is a curated set of 599 synthesized lithium solid electrolytes with experimentally measured room-temperature ionic conductivity, composition, space group and lattice parameters, plus CIFs for 321 entries. It was built by Félix Therrien, Jamal Abou Haibeh, Divya Sharma, Rhiannon Hendley, Leah Wairimu Mungai, Sun Sun, Alain Tchagang, Jiang Su, Samuel Huberman, Yoshua Bengio, Hongyu Guo, Alex Hernández-García and Homin Shin (Mila and NRC Canada; arXiv:2502.14234 v2, 2025-10-01; Digital Discovery 2026, issue 2). It ships an official leakage-controlled split, public on GitHub: 478 train and 121 test entries, 67 of the test entries with CIFs. The metric is the MAE of log10(sigma_RT / S cm^-1). Following the package's replace_text_IC in obelix/utils.py, the 8 test labels recorded as ' < 1E-10' are scored as 1e-15, which reproduces the paper's 2.16 median-predictor baseline. Best published test MAE (Table S1 of arXiv v2) is a random forest at 1.59 on the full test set (1.85 on the CIF subset), then an MLP at 1.72. All 3D models are worse on the CIF subset, the best being pretrained CGCNN at 2.52; the others are PaiNN, SchNet, M3GNet, SO3Net, CGCNN and their pretrained or disorder-aware variants. The paper puts the experimental reproducibility floor at about 0.41, the mean absolute deviation across remeasured materials. A January 2026 follow-up (Haewon Kim, Taekgi Lee, Seongeun Hong, Kyeong-Ho Kim and Yongchul G. Chung, arXiv:2601.10997v2) reports MAE 0.543 (gradient-boosted trees) and 0.657 (fine-tuned Llama-3.1-8B), but on its own structure-labeled set of 499 entries and its own split. An ICML 2026 paper (Jiyeon Kim, Byungju Lee and Won-Yong Shin, arXiv:2605.09311, code at github.com/jykim-git/MD) reports 1.388 on OBELiX (its own random forest re-run: 1.608), using SevenNet structure embeddings and pretraining on MD-simulated Li mean-square displacements; its preprocessing keeps only the CIF test entries with numeric labels and drops all 8 ' < 1E-10' entries (all 8 have CIFs), so it scores 59 entries on a different metric and does not set the bar. No result on the official split and metric below 1.59 was found for this update; the repository README and test files are live (HTTP 200).

## What counts as a win

Success means a model trained only on the 478 official train entries, with labels converted by obelix's replace_text_IC and no other conductivity data of any kind. Hyperparameters are chosen by cross-validation inside the train set, and the final model and its hash are published before the test file is scored. Its MAE of log10 sigma on all 121 official test entries, recomputed by the checker, must be STRICTLY LOWER (direction: min) than 1.59 by at least 10% relative (MAE <= 1.431). It must also clear the half-width of a 2,000-sample paired bootstrap 90% interval of the MAE difference against the checker's re-run of the repository's benchmark/RF.py. Finally, it must beat every published MAE on the official split that a literature search finds, including the journal version's table if its numbers differ from arXiv v2.

## Partial wins

- **p1:** A structure-aware model whose input includes the atomic positions from the CIF (a graph network, a universal-potential embedding or crystal-graph features; models that use only composition, space group or lattice parameters do not count) that beats the random forest's 1.85 on the 67-entry CIF test subset by at least 10% relative (MAE <= 1.665), under the same rules.
- **p2:** A model of the p1 kind, trained only on the 254 CIF-bearing train entries, that beats the best published 3D geometric model (pretrained CGCNN, 2.52 on the 67-entry CIF test subset) by at least 20% relative (MAE <= 2.016), under the same training-data, hashing and reproduction rules. The 20% margin replaces the bootstrap, and only published 3D geometric models are compared. Composition models are excluded here because the random forest retrained on the same 254 entries already reaches 1.87 on that subset (arXiv v2, Section 4).

## How a win is checked

Checker, under 10 minutes: install obelix-data or fetch train.csv and test.csv from the repository, and convert labels with replace_text_IC. Re-run the claim's training script from scratch and confirm the model hash. Score the 121 test entries, re-run benchmark/RF.py for the paired bootstrap, and search the code for any external conductivity source (the Liverpool ionic-conductivity database, LiIonDB, Materials Project or ICSD property lookups).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/NRC-Mila/OBELiX>

## Sources

- <https://github.com/NRC-Mila/OBELiX>
- <https://arxiv.org/abs/2502.14234>
- <https://raw.githubusercontent.com/NRC-Mila/OBELiX/main/data/downloads/test.csv>
- <https://github.com/NRC-Mila/OBELiX/blob/main/obelix/utils.py>
- <https://github.com/NRC-Mila/OBELiX/blob/main/benchmark/RF.py>
- <https://pubs.rsc.org/en/content/articlelanding/2026/dd/d5dd00441a>
- <https://arxiv.org/abs/2601.10997>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Li-transport physics from the CIF: Li-Li distances, Li site fraction, bond-valence-site-energy migration barriers, anion-framework polarisability, and volume per Li.
- Composition models with chemistry-aware embeddings (CrabNet, Roost, mat2vec) and strong regularisation. The test split is leakage-controlled by composition family, so smooth chemistry generalises better than memorisation.
- Treat the detection-limited entries explicitly, for example with a classifier for insulators plus a regressor: the 8 ' < 1E-10' test entries sit at log -15 and dominate the MAE.
- Cross-domain (survival analysis): a Tobit-style censored likelihood for detection-limited labels.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The test set is tiny (121), so a 5% gain is noise; the 10% margin and the paired bootstrap are mandatory.
- Experimental conductivity compilations (the Liverpool database, LiIonDB, review tables) overlap heavily with OBELiX test materials. Any such data is leakage, and so is an LLM prompted with formula names, which may recall literature conductivities.
- The ' < 1E-10' to 1e-15 convention is part of the metric; scoring those entries at 1e-10 instead moves the median baseline from 2.16 to 1.83.
- Lower-looking numbers in the literature are on other metrics: arXiv:2605.09311's 1.388 drops the 8 detection-limited test entries (all of which sit in the 67-entry CIF subset), and arXiv:2601.10997's 0.543 is on a different dataset. Check the test set and the ' < 1E-10' handling before comparing, and note that MD-derived transport labels count as conductivity data under this criterion.
- About three quarters of the CIFs have partial occupancies, and rounding them changes compositions.
- The RSC journal page refused this update's automated fetch (HTTP 403), so the bar comes from arXiv v2. Check the journal table by hand before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/obelix-li-electrolyte-ionic-conductivity-mae.md
```

Already set up? Say `run V3R1T4S on obelix-li-electrolyte-ionic-conductivity-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `obelix-li-electrolyte-ionic-conductivity-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
