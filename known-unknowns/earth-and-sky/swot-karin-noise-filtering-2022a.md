# SWOT KaRIn noise-filtering data challenge 2022a: beat the leaderboard's best vorticity or current RMSE on cycle 13

🌍 **Earth and sky** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (dc_inputs.tar.gz is 1.69 GB: 270 passes of cycle 13) · open as of 2026-10-30

## The problem

Ocean data challenge 2022a (Datlas, IMT Atlantique and CLS, CMEMS SLICING project; experiment design by Anaelle Treboutte and Pierre Prandi, CLS) asks for filters that remove spatially uncorrelated KaRIn instrumental noise from simulated SWOT swath sea-surface height. Ground truth: the eNATL60 NEMO simulation. Evaluation inputs (ssh_karin) and noise-free targets (ssh_true) cover one orbital cycle (cycle 13, 270 passes); targets may be used only for evaluation, never for filtering or tuning. Scores: mean RMSE over the whole domain, in coastal areas ( < 200 km) and in offshore low- and high-variability regions, plus the wavelength where SNR = 1, each for SSH, geostrophic current and relative vorticity (derivatives amplify residual noise). README leaderboard (unchanged since Dec 2022, re-checked 2026-10-30). CNN (U-Net of Treboutte, Carli, Ballarotta, Carpentier, Faugere and Dibarboure, Remote Sensing 15, 2183, 2023; CLS & Datlas notebook): SSH global RMSE 0.002 m, lambda(SNR1) 10.5 km; geostrophic current global 0.055 m/s, coastal 0.068 m/s, lambda 9.4 km; relative vorticity global 0.637, coastal 0.881, offshore low/high variability 0.475/0.303, lambda 15.4 km. GOMEZ_V2 (spatially variable Gomez-Navarro-type filter): current coastal 0.065 (best in that column), vorticity global 0.65. Baselines: NO FILTER, MEDIAN, GOMEZ (Gomez-Navarro et al. 2018, 2020). Open task: a filter that beats the best leaderboard value on a headline score without losing elsewhere.

## What counts as a win

Filtered SSH files for all 270 cycle-13 passes, evaluated with the repository's own unmodified benchmark code (src/benchmark.py as in notebook/demo_benchmark_CNN.ipynb). The filter must be produced without using ssh_true, or any eNATL60 (or derived) SSH for the cycle-13 dates, in any fitting, tuning, checkpoint or selection step. Every tunable parameter is fixed by a procedure in the released code that reads only ssh_karin or independent training data the claimant generates or downloads, and that data must not cover the cycle-13 period. The results must give a relative-vorticity mu(RMSE global) of at most 0.636, strictly below the CNN's printed 0.637 by at least one unit in the last printed digit. In the same evaluation, SSH lambda(SNR1) must be at most 10.5 km and geostrophic-current mu(RMSE global) at most 0.055 m/s. Re-fetch the README leaderboard immediately before claiming and compare with its best row for each column (direction: min for all three). The result must also beat the best value for the same metric reported by any paper that scores all 270 cycle-13 passes with this repository's benchmark. Treboutte et al. 2023 was checked explicitly. Cutolo et al. 2025 (arXiv 2503.21303) uses a left/right-swath split and its own U-Net baseline, so it is not comparable, but re-check it and any newer paper for tabulated benchmark scores.

## Partial wins

- **p1:** Geostrophic-current mu(RMSE coastal) of at most 0.064 m/s (below the best printed 0.065, GOMEZ_V2), with geostrophic-current mu(RMSE global) of at most 0.056.
- **p2:** A filter using no training data at all other than the cycle-13 ssh_karin inputs (for example a self-supervised or analytic filter) that is at least as good as GOMEZ_V2 on all four relative-vorticity RMSE columns (0.65, 0.882, 0.504, 0.321) and strictly better on at least one.
- **p3:** Relative-vorticity lambda(SNR1) of at most 15.3 km (below the CNN's 15.4) with relative-vorticity mu(RMSE global) of at most 0.65.

## How a win is checked

The skeptic downloads dc_inputs.tar.gz from the MEOM THREDDS server. It gives the claimed filter a copy of the 270 input files with the ssh_true variable removed, and runs the filter end to end from a clean environment, including any training or parameter selection. It then runs the repository's benchmark code on the outputs against the original files and compares the printed table with the README leaderboard. This takes under an hour on CPU for analytic filters, plus any training time.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/ocean-data-challenges/2022a_SWOT_karin_error_filtering>

## Sources

- <https://github.com/ocean-data-challenges/2022a_SWOT_karin_error_filtering>
- <https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2022a_SWOT_karin_error_filtering/catalog.html>
- <https://github.com/ocean-data-challenges/2022a_SWOT_karin_error_filtering/blob/main/notebook/demo_benchmark_CNN.ipynb>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Self-supervised blind-spot denoising (Noise2Self / Noise2Void): the target noise is spatially uncorrelated, which is exactly what these methods assume, and they need no clean targets.
- Physics prior: penalise the Laplacian of the filtered SSH (vorticity) in a variational filter, with a regularisation weight that varies with local variance (the GOMEZ_V2 idea).
- Cross-domain import (image processing): BM3D or non-local means tuned only on noise statistics estimated from the inputs themselves.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Only the cycle-13 evaluation archive is public. The THREDDS folder holds just dc_inputs.tar.gz (1.69 GB, 270 passes with ssh_karin and ssh_true), and the README's 'Extra training data' section is empty. The CNN was trained on 2009 eNATL60-BLB002 swaths that are not posted (docs/setup_CNN.md). Plan on self-supervised or analytic filters, or on training data you simulate yourself (for example with CNES swot_simulator) from fields that do not overlap the cycle-13 dates.
- ssh_true is eNATL60 SSH on the swath. Any eNATL60 or derived SSH covering the cycle-13 dates is the target in disguise and may not be used. Cycle-13 ssh_true may not pick hyperparameters, checkpoints or the stopping epoch either.
- Leaderboard RMSE values are printed to 3 decimals (SSH 0.002 m ties several methods; GOMEZ_V2 is printed to 2 or 4 decimals in places), so SSH RMSE cannot separate entries. Use the vorticity and current columns.
- The leaderboard has not changed since Dec 2022 (last commit Sep 2023, a data-link change). A search on 2026-10-30 found one later paper using the cycle-13 data: Cutolo, Granero-Belinchon, Thiraux, Wang and Fablet (SIMPGEN, arXiv 2503.21303, 2025). It trains on the left swaths, tests on the right swaths against its own U-Net, and reports RMSE only by scale in figures. No paper with full benchmark-table scores below the leaderboard was found. Search again before claiming.
- The 2022a leaderboard is separate from the 2024b SWOT denoising challenge (real SWOT data, no numeric leaderboard) and from the SSH mapping challenges (2020a, 2021a), which are existing bank entries.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/earth-and-sky/swot-karin-noise-filtering-2022a.md
```

Already set up? Say `run V3R1T4S on swot-karin-noise-filtering-2022a`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `swot-karin-noise-filtering-2022a`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
