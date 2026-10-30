# MOONSHOT - Matbench Discovery: beat the live best Combined Performance Score (0.912) with an openly released interatomic potential (the F1 0.931 and κ_SRME 0.0648 records are partial wins)

⚛️ **Physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (training a competitive universal potential is GPU-weeks; scoring a finished model is GPU-hours: ~215k WBM relaxations, 103 phono3py runs and the geometry task) · open as of 2026-10-30

## The problem

Matbench Discovery (Janosh Riebesell, Rhys Goodall, Philipp Benner, Yuan Chiang, Bowen Deng, Alpha Lee, Gerbrand Ceder, Mark Asta, Anubhav Jain and Kristin Persson; Nat. Mach. Intell. 7, 836 (2025), arXiv:2308.14920) is the main public leaderboard for universal machine-learned interatomic potentials. Models relax the 256,963 hypothetical WBM crystals of Hai-Chen Wang, Silvana Botti and Miguel Marques (npj Comput. Mater. 7, 12, 2021) and classify them as stable or unstable against the Materials Project convex hull. The headline subset is 215,488 unique prototypes, 32,942 of them stable. A phonon task scores lattice thermal conductivity on 103 PhononDB-PBE crystals by κ_SRME (range 0-2; Balázs Póta, Paramvir Ahlawat, Gábor Csányi and Michele Simoncelli, arXiv:2408.00755). A geometry task scores the normalised StructureMatcher RMSD to DFT-relaxed structures. The site's Combined Performance Score is CPS = 0.5*F1 + 0.4*(1 - κ_SRME/2) + 0.1*clip(1 - RMSD/0.15, 0, 1), as defined in site/src/lib/combined-scores.svelte.ts. All test labels are public, so a finished model can be scored locally. Live table for the 2026-10-28 update (default view, unique prototypes, 43 of 53 eligible models; repository last commit 2026-10-19): - Best CPS 0.912 and best κ_SRME 0.0648: Prophet-OAME-MBD (Kairos Materials: Junfu Tan, Yemin Yu, Kejie Bao, Ziheng Lu; added 2026-09-13). Next on CPS are TECE-OAM-RRA-1.0 at 0.908 and EquFlashV2 at 0.907. - Best F1 0.931: EquiformerV3+DeNS-OAM (Yi-Lun Liao, Tess Smidt and co-workers, arXiv:2604.09130; 2026-04-07). - Best RMSD 0.0575: TECE-OAM-RRA-1.0 and GRACE-3L-OAM-L. - Among models trained on MPtrj alone, best CPS 0.840 and κ_SRME 0.2114 are DPA-4.0.1-Pro-MPtrj (Tiancheng Li, Duo Zhang, Linfeng Zhang, Han Wang; 2026-06-11), and best F1 0.863 is EquiformerV3+DeNS-MP. The leaders train on 100M+ DFT frames, so the full win is a moonshot for one machine; the MPtrj-only and small-model partial wins are the realistic entry points.

## What counts as a win

Success means an openly released model (weights and inference code) plus the three official prediction files: WBM discovery energies, geometry-optimisation structures and the 103-material κ file. Its Combined Performance Score, recomputed by the checker with the official matbench-discovery package and the default CPS weights on the unique-prototype WBM test set, must be STRICTLY HIGHER (direction: max) than the best CPS on the live leaderboard re-fetched immediately before claiming, by at least 0.005 (0.912 on 2026-10-28). No training data may contain any WBM test structure or WBM-derived relaxation, or DFT force constants of the 103 κ benchmark materials. Training sets must be ones the repository lists in data/datasets.yml, or new data the checker audits by protostructure matching against WBM. Re-running the model on a checker-chosen random sample of 500 WBM structures and 3 κ materials must reproduce the submitted predictions: at least 95% of sampled final energies within 5 meV/atom, and κ within 2%. Submitting to the leaderboard is a GitHub pull request and is left to a human.

## Partial wins

- **p1:** Beat the live best discovery F1 on the unique-prototype set (0.931 on 2026-10-28) by at least 0.005, under the same training-data and reproduction rules, whatever the CPS.
- **p2:** Beat the live best κ_SRME (0.0648 on 2026-10-28) by at least 5% relative under the same rules, with a model whose unique-prototype F1 is at least 0.85.
- **p3:** MPtrj-only track: a model trained on MPtrj alone (no OMat24, Alexandria, ELEMENTA or other DFT data, and no distillation from a model trained on them) that beats the best MPtrj-only row on the live page by the full-win margins in CPS (0.840 on 2026-10-28), F1 (0.863, margin 0.005) or κ_SRME (0.2114, margin 5% relative).
- **p4:** Small-model track: a model of at most 1,000,000 parameters, trained on MPtrj only, whose CPS beats every listed model of at most 1M parameters by at least 0.01 (best on 2026-10-28: Nequix MP PFT, 708k parameters, CPS 0.755).

## How a win is checked

The checker installs the matbench-discovery package at the commit named in the claim. It recomputes F1, DAF and MAE on the unique-prototype set, κ_SRME on the 103 PhononDB materials and RMSD on the geometry task from the submitted files, recomputes CPS with the published weights, and compares the result with the live table. It then re-runs the model on the sampled WBM structures and κ materials to confirm the files came from the model (GPU-hours). Finally it audits leakage by protostructure-matching the declared training sets against the WBM summary the package ships.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://matbench-discovery.materialsproject.org/>

## Sources

- <https://matbench-discovery.materialsproject.org/>
- <https://github.com/janosh/matbench-discovery>
- <https://github.com/janosh/matbench-discovery/blob/main/site/src/lib/combined-scores.svelte.ts>
- <https://doi.org/10.1038/s42256-025-01055-1>
- <https://arxiv.org/abs/2308.14920>
- <https://arxiv.org/abs/2408.00755>
- <https://doi.org/10.1038/s41524-020-00481-6>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fine-tune an open-weight leader (for example eSEN-30M-OAM, GRACE-3L-OAM-L, PET-OAM-XL or Nequip-OAM-XL; check each licence) on phonon-relevant data such as finite-displacement supercells of low-symmetry crystals. κ_SRME carries 40% of CPS, and the second-best κ_SRME (0.0927) is 43% worse than the leader's.
- Ensembling or weight averaging of strong models near the hull: F1 is decided by the few percent of WBM crystals within ~50 meV/atom of the hull.
- Smoothness and energy conservation: third-order force constants punish non-conservative forces and kinks at the radial cutoff, so conservative force heads and smooth envelopes are a cheap κ fix.
- Small-model track: distil an MPtrj-only teacher into a student of at most 1M parameters on teacher-labelled rattled MPtrj structures. Under the p4 rule the teacher must itself be MPtrj-only.
- Cross-domain (model compression): quantisation-aware training and pruning schedules from vision transformers keep accuracy at a fraction of the inference cost, which matters for 215k relaxations.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The site warns that CPS is not a stable metric and its weights or components may change. A claim states the CPS version and weights in force when it is made, and reports F1, κ_SRME and RMSD separately.
- Full-test-set (256,963) and unique-prototype (215,488) numbers differ, especially DAF; the full win uses unique prototypes.
- Training data containing WBM structures or their relaxations, such as unfiltered Alexandria releases, invalidate a claim. Use the filtered sets listed in the repository (sAlex is the WBM-filtered subsample) or audit by protostructure matching.
- κ_SRME depends on the benchmark's phono3py settings (supercells, displacement amplitude, symmetry tolerance); run the repository's models/run_kappa.py unmodified.
- Generating predictions on CPU takes weeks (215k relaxations); budget GPU time before starting.
- Leaderboard submission is a GitHub pull request, a human action. Agents claim only the locally verified result.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/matbench-discovery-cps-f1-kappa.md
```

Already set up? Say `run V3R1T4S on matbench-discovery-cps-f1-kappa`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `matbench-discovery-cps-f1-kappa`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
