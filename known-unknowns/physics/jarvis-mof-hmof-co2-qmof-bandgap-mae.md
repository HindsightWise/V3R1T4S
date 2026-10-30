# JARVIS-Leaderboard MOF tasks: beat the best test MAE for GCMC CO2 uptake in hypothetical MOFs (0.01 and 2.5 bar) or for the PBE band gap of QMOF frameworks

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (gradient boosting on pore and chemistry descriptors) to laptop-days (graph networks on 110k MOFs) · open as of 2026-10-30

## The problem

Three metal-organic-framework (MOF) tasks on the JARVIS-Leaderboard (Kamal Choudhary et al., NIST; npj Comput. Mater. 10, 93, 2024) have fixed public splits and have not moved since May 2023: - hmof_max_co2_adsp and hmof_min_co2_adsp: CO2 uptake (mol/kg) at 2.5 bar and 0.01 bar for 137,651 of the 137,953 hypothetical MOFs of Christopher Wilmer, Randall Snurr and co-workers. The labels come from GCMC isotherms (RASPA, UFF framework, TraPPE CO2) as curated in MOFX-DB (N. Scott Bobbitt, Randall Snurr and co-workers, J. Chem. Eng. Data 2023). Split 110,121/13,765/13,765. - qmof_bandgap: PBE band gaps (eV) of 20,424 frameworks from the QMOF database (Andrew Rosen, Justin Notestein, Randall Snurr and co-workers, Matter 4, 1578, 2021). Split 16,340/2,042/2,042. The pressures and the force field are documented by Kamal Choudhary, Taner Yildirim, Daniel Siderius, Gilad Kusne, Austin McDannald and Diana Ortiz-Montalvo (Comput. Mater. Sci. 210, 111388, 2022; arXiv:2112.10231). Best listed test MAE, checked live for this update: - 2.5 bar: 0.4622 mol/kg by matminer_xgboost (team UofT, 2023-05-22), then ALIGNN 0.4765 and matminer_rf 0.5233. - 0.01 bar: 0.0383 mol/kg by ALIGNN (2023-01-14), then xgboost 0.0438 and rf 0.0465. - QMOF: 0.2019 eV by ALIGNN, then xgboost 0.3421 and rf 0.3618. The QMOF page's column is headed 'ACC', but the contribution files are test-mae. The QMOF authors' benchmark page lists CGCNN at 0.270 ± 0.011 eV on QMOF v13 with an 80% training split, which is not comparable with this split. Train-median predictors score 2.22, 0.090 and 0.946 on these test sets.

## What counts as a win

Success means a trained model, its training script and test predictions for one of hmof_max_co2_adsp, hmof_min_co2_adsp or qmof_bandgap. The test MAE, recomputed by the checker on the official test ids of the benchmark json in jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/, must be STRICTLY LOWER (direction: min) than the best MAE on that task's live page re-fetched immediately before claiming. The margin must be at least 5% relative AND exceed the half-width of a 1,000-sample paired bootstrap 90% interval of the MAE difference against the best listed predictions. The model is trained only on the train (and val) ids. No external data may contain labels for the test frameworks: no MOFX-DB or hMOF isotherms, no QMOF database properties, and no checkpoints fine-tuned on either. For the two hMOF tasks, no adsorption simulation of test structures is allowed (GCMC, Widom insertion, or energy-grid Henry coefficients with any CO2 force field), and end-to-end inference on all 13,765 test MOFs must take at most 24 CPU-core-hours, timed by the checker. Re-running the saved model must reproduce the predictions to 1e-6. The claim must also report, and beat, any published MAE on the identical JARVIS split found by a literature search.

## Partial wins

- **p1:** One model architecture and feature set, changed only by refitting per task, that beats the live best on both hMOF tasks at once by at least 2% relative each, under the same rules.
- **p2:** Reproduction audit: retrain the listed best entry for one of the three tasks with its published run.sh on the official split, and report a test MAE that differs from the posted value by more than 5% relative, with all outputs saved.

## How a win is checked

Checker, under 1 hour on CPU for a boosted-tree model: download the benchmark json.zip, load structures from the jarvis-tools 'hmof' or 'qmof' dataset, and run the saved model on the test ids. Recompute the MAE and the paired bootstrap against the best CSV linked on the page, time the inference, and audit the training script and feature code for test labels or forbidden simulations.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/hmof_max_co2_adsp/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/hmof_max_co2_adsp/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/hmof_min_co2_adsp/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qmof_bandgap/>
- <https://raw.githubusercontent.com/usnistgov/jarvis_leaderboard/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/hmof_max_co2_adsp.json.zip>
- <https://raw.githubusercontent.com/usnistgov/jarvis_leaderboard/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/qmof_bandgap.json.zip>
- <https://arxiv.org/abs/2112.10231>
- <https://doi.org/10.1016/j.matt.2021.02.015>
- <https://doi.org/10.1021/acs.jced.2c00583>
- <https://github.com/Andrew-S-Rosen/QMOF/blob/main/benchmarks.md>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Pore-geometry descriptors from Zeo++ (largest cavity and pore-limiting diameters, accessible surface area, void fraction, pore-size distribution) plus revised-autocorrelation (RAC) chemistry descriptors of nodes and linkers in a gradient-boosted model. Uptake at 2.5 bar is mostly geometry plus framework charge density.
- For 0.01 bar (the Henry regime) the label tracks strong binding sites: features for open metal sites, polar functional groups (-NH2, -OH, -F) and pores near 4-5 A.
- Frozen embeddings from pretrained MOF models (MOFTransformer, PMTransformer), allowed only after an audit shows their pretraining used no hMOF or QMOF labels.
- QMOF: gaps are set by linker frontier orbitals and metal d states, so try a small graph network on the building-block (node/linker) graph or linker-level electronic descriptors.
- Cross-domain (tabular ML): heavy-tailed targets favour a log transform with Huber loss and stacked ensembles.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The geometric hMOF tasks on the same leaderboard (LCD, PLD, void fraction, surface areas) are deterministic functions of the structure that Zeo++ computes exactly, so they are excluded; only the CO2 and band-gap tasks count.
- MOFX-DB publishes the full hMOF isotherms and QMOF publishes all band gaps. Any model touching those for test ids is leaked, and text or LLM embeddings of MOF names may have memorised them.
- GCMC labels carry Monte Carlo noise (1,000 production cycles), which bounds achievable MAE at 0.01 bar; small relative gains there can be noise, hence the paired bootstrap.
- The QMOF page header says 'ACC', but the metric is MAE in eV, so lower is better.
- Structures download from figshare through jarvis-tools. If figshare shows a bot check, fetch the file in a browser and never work around the check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/jarvis-mof-hmof-co2-qmof-bandgap-mae.md
```

Already set up? Say `run V3R1T4S on jarvis-mof-hmof-co2-qmof-bandgap-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-mof-hmof-co2-qmof-bandgap-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
