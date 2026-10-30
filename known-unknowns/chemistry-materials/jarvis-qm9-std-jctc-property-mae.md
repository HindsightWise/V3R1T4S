# JARVIS-Leaderboard QM9 (qm9_std_jctc, 130,829 molecules): beat ALIGNN's test MAE on one of 11 quantum-chemical properties (R2 excluded)

⚗️ **Chemistry and materials** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (CPU training of a graph network on about 100k small molecules; a GPU shortens this to hours) · open as of 2026-10-30

## The problem

JARVIS-Leaderboard (Kamal Choudhary and many co-authors, npj Comput. Mater. 10, 93, 2024) scores models on the QM9 set as the JARVIS dataset qm9_std_jctc. QM9 is from Raghunathan Ramakrishnan, Pavlo Dral, Matthias Rupp and Anatole von Lilienfeld (Sci. Data 1, 140022, 2014; DFT B3LYP/6-31G(2df,p) properties of 134k small organic molecules). Each property has a fixed 110,000/10,000/10,829 train/val/test id split inside the benchmark file. The benchmark targets are standardised: on 2026-10-30 the U0, R2, ZPVE, gap and mu train targets each had mean about 0 and standard deviation about 1. The MAEs below are therefore in units of each property's standard deviation, not eV; a constant predictor scores about 0.71-0.83 on the test set. On 2026-10-30 each of the 12 pages had a single entry, alignn_model (ALIGNN; Choudhary and Brian DeCost, npj Comput. Mater. 7, 185, 2021; submitted 01-14-2023). Its test MAEs: U0 0.0146, U 0.0138, H 0.0140, G 0.0133, HOMO 0.0187, LUMO 0.0175, gap 0.0345, ZPVE 0.0019, mu 0.0248, alpha 0.0557, R2 0.6523, Cv 0.0239. The R2 row (0.6523, against 0.713 for a constant train-median predictor) is a failed run rather than a bar, so R2 is excluded. QM9 records in the literature (a few meV for U0) were obtained on other splits and in physical units and are not comparable: the bar is this fixed split in the benchmark's own standardised units.

## What counts as a win

For one property other than R2 (U0, U, H, G, HOMO, LUMO, gap, ZPVE, mu, alpha or Cv): predictions for every test id of the official benchmark (jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/qm9_std_jctc_ < prop > .json.zip) from a model fitted only on that benchmark's train ids, with the val ids used only for early stopping and tuning. The test MAE recomputed by the skeptic against the benchmark targets must be STRICTLY LOWER (direction: min) by at least 2% relative than the best entry on the live page for that property (re-fetched immediately before claiming). It must also be lower than any published MAE on the same JARVIS split that the skeptic finds. No pretraining or distillation on QM9 or on any dataset containing QM9 labels (for example models pretrained on QM9-derived sets). A skeptic retraining from the released script and seed must land within 3% of the claimed MAE and still below the bar.

## Partial wins

- **p1:** A full-win-quality result on one property from a model trained in at most 12 CPU-hours (no GPU), with the wall-clock log released.
- **p2:** One fixed architecture and hyperparameter set that meets the full-win criterion on all four thermochemical energies U0, U, H and G at once.
- **p3:** A re-run of the posted ALIGNN contribution (its run.sh and metadata.json) whose test MAE differs from the posted value by more than 10%, with all outputs saved (a reproduction audit).

## How a win is checked

pip install jarvis-leaderboard; load the benchmark json; check that the submitted csv covers exactly the test ids; recompute the MAE with the package's scoring; audit the training script for use of test ids or QM9-pretrained weights; retrain once from the seed. Hours on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qm9_std_jctc_U0/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qm9_std_jctc_U0/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qm9_std_jctc_HOMO/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/qm9_std_jctc_gap/>
- <https://github.com/usnistgov/jarvis_leaderboard/tree/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction>
- <https://www.nature.com/articles/sdata201422>
- <https://www.nature.com/articles/s41524-021-00650-1>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not compare with QM9 numbers from other splits (e.g. 110k/10k/rest); only this benchmark's test ids count.
- Unit conventions differ between QM9 releases (hartree vs eV, U0 with or without atomisation reference); fit to the benchmark file's targets, not to a re-downloaded QM9.
- R2 is excluded: alignn_model's 0.6523 is barely below the 0.713 test MAE of predicting the train median for every molecule, so beating it says nothing.
- The posted ALIGNN rows are single runs from one 2023 sweep and are far from QM9 state of the art, so the bars are soft; the 2% margin and the retrain check are what keep a win honest.
- Submitting to the leaderboard is a GitHub pull request, an action for the human; the agent claims the verified local result only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/jarvis-qm9-std-jctc-property-mae.md
```

Already set up? Say `run V3R1T4S on jarvis-qm9-std-jctc-property-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-qm9-std-jctc-property-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
