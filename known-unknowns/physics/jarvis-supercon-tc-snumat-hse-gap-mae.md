# JARVIS-Leaderboard frozen mid-size tasks: experimental superconducting Tc from composition (SuperCon, 16,414) or HSE06 band gap from structure (SNUMAT, 10,386): beat the best listed test MAE

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Two mid-size JARVIS-Leaderboard tasks (Kamal Choudhary et al., NIST; npj Comput. Mater. 10, 93, 2024) have fixed public splits and no entries since May 2023. supercon_chem_Tc asks for the experimental superconducting critical temperature (K) from composition alone. It uses the SuperCon-derived set of 16,414 compounds of Valentin Stanev, Corey Oses, A. Gilad Kusne, Efrain Rodriguez, Johnpierre Paglione, Stefano Curtarolo and Ichiro Takeuchi (npj Comput. Mater. 4, 29, 2018), split 13,131 train / 3,283 test with no val. Eleven entries are listed. The best MAE is 4.8511 K by matminer_rf (team UofT, 2023-05-22), then matminer_xgboost 4.9295, cfid_chem 5.0326, ElemNet2_SC 5.114 and matminer_lgbm 5.1519; the Northwestern ElemNet, BRNet and IRNet entries score 5.11-5.84. This task is distinct from the bank's jarvis-small-data-exfoliation-tc-mae, whose Tc task is the small DFT electron-phonon dft_3d_Tc_supercon set. snumat_Band_gap_HSE asks for the HSE06 band gap (eV) from crystal structure, for 10,386 materials of the hybrid-functional band-gap database of Sangtae Kim, Miso Lee, Seungwu Han and co-workers (Sci. Data 7, 387, 2020). Split 8,310/1,038/1,038. Three entries are listed: ALIGNN 0.3765 eV (2023-01-14), matminer_xgboost 0.3987 and matminer_rf 0.4367. The page header says 'ACC', but the contribution files are test-mae. Train-median predictors score 16.69 K and 1.13 eV on the two test sets. Both pages were HTTP 200 for this update.

## What counts as a win

Success means a trained model, its training script and test predictions for supercon_chem_Tc or snumat_Band_gap_HSE. The test MAE, recomputed by the checker on the official test ids of the benchmark json, must be STRICTLY LOWER (direction: min) than the best MAE on the live task page re-fetched immediately before claiming (4.8511 K and 0.3765 eV on 2026-10-28). The margin must be at least 5% relative AND exceed the half-width of a 1,000-sample paired bootstrap 90% interval of the MAE difference against the best listed predictions. Models are trained only on the train ids (plus val for SNUMAT). - SuperCon: inputs are composition only. No SuperCon/NIMS or other Tc data beyond the train labels, and no model or text embedding exposed to Tc values, may be used. - SNUMAT: inputs are the structure only. No band gap of any test material, from any database or functional, may be used directly or through a model pretrained on such labels; no DFT run on test structures is allowed; and end-to-end inference must take at most 24 CPU-core-hours. Re-running the saved model must reproduce the predictions to 1e-6. The claim must also report, and beat, any published MAE on the identical JARVIS split found by a literature search.

## Partial wins

- **p1:** The same rules on one further JARVIS AI single-property task with 2,000-60,000 entries, at least three listed entries and no entry newer than 2023, named before the run starts and checked against its live page. It must not be covered by another bank entry (so not hmof, qmof, any ocp task, or the dft_3d exfoliation or Tc tasks), and the claim must also beat any published MAE on the identical split.
- **p2:** Reproduction audit: retrain matminer_rf on supercon_chem_Tc with its published run.sh on the official split, and report a test MAE that differs from 4.8511 K by more than 5% relative, with outputs saved.

## How a win is checked

Checker, under 1 hour: download the benchmark json.zip, load compositions or structures through jarvis-tools ('supercon_chem', 'snumat'), and re-run the saved model. Recompute the MAE and the paired bootstrap against the best CSV on the page, time the SNUMAT inference, and audit the feature code for external Tc or band-gap lookups.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/supercon_chem_Tc/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/supercon_chem_Tc/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/snumat_Band_gap_HSE/>
- <https://raw.githubusercontent.com/usnistgov/jarvis_leaderboard/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/supercon_chem_Tc.json.zip>
- <https://raw.githubusercontent.com/usnistgov/jarvis_leaderboard/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/snumat_Band_gap_HSE.json.zip>
- <https://doi.org/10.1038/s41524-018-0085-8>
- <https://doi.org/10.1038/s41597-020-00723-8>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- SuperCon: family-aware models, for example a classifier into cuprate, iron-based and conventional families followed by per-family regressors, on Magpie and element-fraction features, with a log(Tc + 1) target and an MAE-matched loss.
- SNUMAT: structure features that track gap opening, such as electronegativity differences, coordination and Madelung site potentials, plus graph networks trained only on the 8,310 train structures.
- Cross-domain (tabular ML): TabPFN-style priors, stacked ensembles and quantile losses for the heavy-tailed Tc distribution.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- SuperCon contains long doping series of closely related compositions spread across a random split, which rewards memorisation. Report a family-held-out cross-validation alongside the claim; it is not required for the win.
- Formula text embeddings and LLMs can carry memorised literature Tc values or band gaps; treat them as external data.
- Most SNUMAT materials also appear in PBE databases (Materials Project, AFLOW, OQMD, JARVIS). Gap-trained pretrained models therefore leak, which is why the criterion forbids them.
- The SNUMAT page says 'ACC', but the metric is MAE in eV.
- jarvis-tools pulls datasets from figshare, which answered this update's scripted fetch with HTTP 202 and an empty body (a bot check). Use a browser session and never work around the check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/jarvis-supercon-tc-snumat-hse-gap-mae.md
```

Already set up? Say `run V3R1T4S on jarvis-supercon-tc-snumat-hse-gap-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-supercon-tc-snumat-hse-gap-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
