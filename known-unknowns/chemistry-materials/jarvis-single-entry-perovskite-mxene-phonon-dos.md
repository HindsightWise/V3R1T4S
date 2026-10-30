# JARVIS-Leaderboard single-entry materials tasks: halide perovskites (5 properties), MXene formation energy and phonon DOS spectra: beat the only listed model

⚗️ **Chemistry and materials** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Seven JARVIS-Leaderboard materials tasks had exactly one entry on 2026-10-30. Five use the halide perovskite dataset of Arun Mannodi-Kanakkithodi (Purdue) and Maria Chan (Energy Environ. Sci. 2022, doi 10.1039/D1EE02971A): 229 compounds, split 183/46 train/test with no val ids, each scored by alignn_model (01-14-2023) on test MAE. The five values are HSE06 band gap 0.1615, PBE band gap 0.1223, HSE decomposition energy 0.0512, PBE decomposition energy 0.0477 and refractive index 0.0233. The sixth is mxene275_formation_energy, a 2D MXene set of 274 structures split 220/27/27; the page cites the C2DB update of Morten Gjerding and co-authors, 2D Mater. 2021, doi 10.1088/2053-1583/ac1059. Its only entry is mxene_alignn at 0.0561 (team MXene_ALIGNN, 06-12-2023). The seventh is edos_pdos_ph_dos, the total phonon density of states for 14,243 JARVIS-DFT materials (split 11,395/1,424/1,424; Ramya Gurunathan, Kamal Choudhary and Francesca Tavazza, Phys. Rev. Mater. 7, 023803, 2023), scored by multi-MAE, with alignn_model at 0.05773. Single-entry tasks have soft bars, but small test sets make noise a real risk, hence the seed and margin rules.

## What counts as a win

For one of the seven tasks: predictions for every test id of the official benchmark json from a model fitted only on that task's train ids. Val ids, where the benchmark has them, are for tuning only; where it has none (the perovskite tasks), all tuning must use splits of the train ids. The metric (MAE, or multi-MAE for the phonon DOS, computed with the jarvis_leaderboard scoring code on the benchmark's test spectra) must be STRICTLY LOWER (direction: min) than the only entry on the live page (re-fetched immediately before claiming). The margin is at least 5% relative for the perovskite and MXene tasks and at least 2% for the phonon DOS. The mean over 5 seeds must also be below the bar. No pretraining on data containing the same compounds' labels at the same level of theory (for example the Mannodi perovskite set itself, C2DB labels of the MXenes, or JARVIS-DFT phonon DOS for the phonon task). The result must also beat any published value on the same split that the skeptic finds.

## Partial wins

- **p1:** One fixed model and hyperparameter set that meets the full-win criterion on three of the five halide perovskite tasks.
- **p2:** A composition-only model (no structure input) that meets the full-win criterion on the HSE06 band gap task.

## How a win is checked

Install jarvis-leaderboard; load each benchmark json; recompute the metric from the submitted csv with the package scorer; rerun 5 seeds; audit pretraining data. Minutes to hours on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/halide_peroskites_HSE_gap/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/halide_peroskites_HSE_gap/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/halide_peroskites_PBE_gap/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/halide_peroskites_HSE_decomp_energy/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/halide_peroskites_PBE_decomp_energy/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/halide_peroskites_Ref_ind/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/mxene275_formation_energy/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/Spectra/edos_pdos_ph_dos/>
- <https://doi.org/10.1039/D1EE02971A>
- <https://doi.org/10.1103/PhysRevMaterials.7.023803>
- <https://iopscience.iop.org/article/10.1088/2053-1583/ac1059>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The task slugs spell 'peroskites'; use the slug exactly when fetching the benchmark file.
- The halide_peroskites_PBE_gap page description says 'decomposition energy' (copied from the decomp page), but its benchmark targets are PBE band gaps (0.53-5.25 eV on the test ids). Trust the benchmark json, not the page text.
- The 'Dataset size' column is the whole set; perovskite and MXene test sets are only a few dozen compounds, so one outlier can move the MAE by more than 5%.
- Phonon DOS multi-MAE depends on the binning and normalisation in the benchmark file; do not re-bin.
- Submitting to the leaderboard is a GitHub pull request, an action for the human.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/jarvis-single-entry-perovskite-mxene-phonon-dos.md
```

Already set up? Say `run V3R1T4S on jarvis-single-entry-perovskite-mxene-phonon-dos`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-single-entry-perovskite-mxene-phonon-dos`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
