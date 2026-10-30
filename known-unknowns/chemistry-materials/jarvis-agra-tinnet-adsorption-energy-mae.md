# JARVIS-Leaderboard catalysis adsorption energies (AGRA O, OH, CO, CHO, COOH and TinNet O, OH, N): beat the best listed test MAE

⚗️ **Chemistry and materials** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

JARVIS-Leaderboard hosts eight DFT adsorption-energy tasks for heterogeneous catalysts. Five come from the AGRA dataset (Automatic Graph Representation Algorithm; Zachary Gariepy, ZhiWen Chen, Isaac Tamblyn, Chandra Veer Singh and Conrard Giresse Tetsassi Feugmo, APL Mach. Learn. 1, 036103, 2023; github.com/Feugmo-Group/AGRA). Three come from the TinNet dataset (Hongliang Xin group). Each task has a fixed split in its benchmark file (e.g. AGRA_O 800/100/100, AGRA_CO 155/19/19, tinnet_N 263/32/32). The best listed test MAEs (eV) on 2026-10-30 were: AGRA_O 0.0319 (dataset size 1,000), AGRA_OH 0.0241 (875), AGRA_CO 0.1082 (193), AGRA_CHO 0.0953 (214), AGRA_COOH 0.0383 (280), tinnet_O 0.2657 (745), tinnet_N 0.0871 (327, the plain alignn_model) and tinnet_OH 0.0843 (746). All but tinnet_N are by the problem-specific ALIGNN-atomwise models of the transferability study on Special/catalysis_mat. That study is Shih-Han Wang, Hongliang Xin, Luke Achenie and Kamal Choudhary, 'Examining generalizability of AI models for catalysis', J. Catal. 450, 116171 (2025); preprint chemRxiv 10.26434/chemrxiv-2024-hj733, posted 2024-09-25. The pages also list 'Out-...' rows, models trained on one dataset and scored on another, and zero-shot universal potentials (CHGNet, MACE, MATGL, ALIGNN-FF) with MAEs of about 2 to 44 eV. Neither kind is the bar to beat.

## What counts as a win

For one of the eight tasks: predictions for every test id of the official benchmark json (AI/SinglePropertyPrediction/ < task > .json.zip) from a model fitted only on that task's train ids, with val ids used only for tuning. The test MAE recomputed by the skeptic must be STRICTLY LOWER (direction: min) than the lowest MAE on the live task page (re-fetched immediately before claiming) by at least 5% relative, because the test sets are small. The mean over 5 training seeds must also be below the bar. No pretraining on data that contains the task's source adsorption energies (e.g. Catalysis-Hub or OC20 records of the same systems) unless those systems are removed and the removal is shown. The result must also beat any published MAE on the same JARVIS split that the skeptic finds.

## Partial wins

- **p1:** One fixed architecture and hyperparameter set that meets the full-win criterion on three of the eight tasks.
- **p2:** A model trained on the union of the five AGRA train sets that meets the full-win criterion on two AGRA tasks (a multi-adsorbate model).

## How a win is checked

Install jarvis-leaderboard, load the task json, recompute the MAE from the submitted csv over the test ids, run the 5 seeds, and audit pretraining data for overlap. Minutes to an hour on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/AGRA_O_ead/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/AGRA_O_ead/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/AGRA_CO_ead/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/tinnet_O_ead/>
- <https://pages.nist.gov/jarvis_leaderboard/Special/catalysis_mat/>
- <https://github.com/Feugmo-Group/AGRA>
- <https://doi.org/10.1063/5.0140487>
- <https://doi.org/10.1016/j.jcat.2025.116171>
- <https://doi.org/10.26434/chemrxiv-2024-hj733>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The page rows named 'Out-AI-SinglePropertyPrediction-ead- < other task > -test-mae' are cross-dataset transfer scores; the bar is the row trained on the same task (or alignn_model if lower).
- The same-task 'Out-' rows (ALIGNN-atomwise, trained on the task's own split per their config.json) score exactly the benchmark test ids. They are 1.05 to 3.6 times lower than alignn_model on the same split (tinnet_OH 0.0843 vs 0.0882; AGRA_O 0.0319 vs 0.1134), except tinnet_N, where alignn_model is lower. Their protocol is described in J. Catal. 450, 116171 (2025) (not read on 2026-10-30). The bar is still the lowest row.
- The 'Dataset size' column is the whole dataset; test sets are 19 to 100 structures, so read the split from the benchmark json.
- Universal MLIP rows predict total energies, hence MAEs of several eV; do not mistake them for weak adsorption-energy baselines.
- Submitting to the leaderboard is a GitHub pull request, an action for the human.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/jarvis-agra-tinnet-adsorption-energy-mae.md
```

Already set up? Say `run V3R1T4S on jarvis-agra-tinnet-adsorption-energy-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-agra-tinnet-adsorption-energy-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
