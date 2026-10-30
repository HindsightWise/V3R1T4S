# SSUB experimental formation enthalpies on JARVIS-Leaderboard (1,726 compounds, composition only): beat ElemNet2-TL's test MAE of 0.0924

⚗️ **Chemistry and materials** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The JARVIS-Leaderboard task ssub_formula_energy asks for the experimental formation enthalpy of a compound from its formula alone. The data are 1,726 compounds from the SGTE substance database (SSUB, Scientific Group Thermodata Europe), with a fixed 1,381/345 train/test split in the benchmark file (no validation ids). On 2026-10-30 the page listed 11 entries (test MAE, eV/atom): ElemNet2_TL 0.0924 (Northwestern University; the ElemNet transfer-learning line of Dipendra Jha, Vishu Gupta, Ankit Agrawal and Alok Choudhary, pretrained on DFT formation energies), BRNet 0.1143, matminer_xgboost 0.1244 (UofT; the robustness study of Kangming Li, Brian DeCost, Kamal Choudhary, Michael Greenwood and Jason Hattrick-Simpers), BNet 0.1286, IRNet_EF 0.1319, matminer_lgbm 0.1441, matminer_rf 0.1468 (UofT), cfid_chem 0.1694 (JARVIS), ElemNet2_SC 0.2064, ElemNet1 0.2068 and element_fraction_desc 0.3807. The leader has stood since 01-14-2023. Experimental thermochemistry is the regime where DFT-trained models carry systematic errors, so modest data and careful transfer can matter more than model size.

## What counts as a win

Predictions for every test id of the official benchmark (AI/SinglePropertyPrediction/ssub_formula_energy.json.zip) from a model fitted only on its train ids. The benchmark has no val ids, so all tuning and early stopping must use splits of the train ids only. Pretraining on DFT formation energies (OQMD, Materials Project, JARVIS-DFT, Alexandria) is allowed. Training on any other experimental formation-enthalpy compilation is allowed only after every test formula is removed from it. The test MAE recomputed by the skeptic must be STRICTLY LOWER (direction: min) than the best entry on the live page (re-fetched immediately before claiming) by at least 3% relative (at most 0.0896 against today's 0.0924). It must also be below every published MAE on this split that the skeptic finds, and the mean over 5 seeds must stay below the bar.

## Partial wins

- **p1:** Beat ElemNet2_TL under the full-win protocol using no external data at all (train ids only, no pretraining).
- **p2:** A closed-form or symbolic model with at most 50 fitted parameters whose test MAE beats matminer_xgboost (0.1244) under the same split and leakage rules.

## How a win is checked

Install jarvis-leaderboard; recompute the MAE from the csv over the test ids; grep the training pipeline for external experimental datasets and check formula overlap with the test set; rerun 5 seeds. Under an hour on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/ssub_formula_energy/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/ssub_formula_energy/>
- <https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction>
- <https://www.nature.com/articles/s41524-023-01012-9>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Formulas repeat across experimental compilations (and across polymorphs); dedupe by reduced formula before any external fine-tuning.
- The page gives no units; the targets in the benchmark file are the reference, so check them before mixing in kJ/mol data.
- Submitting to the leaderboard is a GitHub pull request, an action for the human.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/jarvis-ssub-experimental-formation-enthalpy-mae.md
```

Already set up? Say `run V3R1T4S on jarvis-ssub-experimental-formation-enthalpy-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-ssub-experimental-formation-enthalpy-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
