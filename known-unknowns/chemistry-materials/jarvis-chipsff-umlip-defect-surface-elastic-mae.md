# CHIPS-FF on JARVIS-Leaderboard: a universal force field with lower MAE than all 16 listed for vacancy energy, surface energy, C11, bulk modulus or formation energy (104 materials)

⚗️ **Chemistry and materials** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to evaluate an existing open model; needs cluster to train a new one · open as of 2026-10-30

## The problem

CHIPS-FF (Daniel Wines and Kamal Choudhary, ACS Materials Lett. 2025, doi 10.1021/acsmaterialslett.5c00093; github.com/usnistgov/chipsff) evaluates universal machine-learning force fields with fixed workflows (relaxation, vacancy and surface energies, elastic constants) against JARVIS-DFT OptB88vdW values for 104 materials common in semiconductor devices. The JARVIS-Leaderboard pages (16 models each, all dated 3-11-2025) list these best MAEs: vacancy formation energy 0.357 eV (eqV2_31M_omat_mp_salex; 48 entries); surface energy 0.1564 J/m^2 (eqV2_31M_omat_mp_salex; 85); C11 31.81 GPa (MatterSim); bulk modulus Kv 77.99 GPa (mace-alexandria); formation energy 0.0756 eV/atom (eqV2_86M_omat). Lattice constant a (0.0111) and volume (0.4171) are led by alignn_ff, which is trained on JARVIS-DFT itself. Other evaluated models include orb-v2, orb-d3-v2, mace-mpa, mace, sevennet, chgnet and matgl. Models released after March 2025 do not appear yet.

## What counts as a win

For one of vac_en, surf_en, c11, kv or form_en: per-material predictions for the benchmark's full material list, produced by the chipsff workflow with default settings and an openly released force field (weights public). The MAE recomputed by the skeptic against the benchmark json must be STRICTLY LOWER (direction: min) than the best entry on the live task page (re-fetched immediately before claiming) by at least 5% relative. The force field must not be trained or fine-tuned on JARVIS-DFT calculations of any of the 104 benchmark materials, or of their vacancy or surface supercells. The result must beat any CHIPS-FF value for that property that the skeptic finds published. A new model trained by the agent, rather than a newer third-party model, should be stated as such.

## Partial wins

- **p1:** Any openly released force field that is not yet on the leaderboard and meets the full-win criterion on one property (credit goes to the model's authors; the claim is the verified evaluation).
- **p2:** An analysis of the Kv task showing, with per-material outputs, that a stated subset of at most 5 materials accounts for more than half of the best listed model's MAE, plus a corrected workflow setting that lowers that model's MAE by 20% or more without changing its weights.

## How a win is checked

Install chipsff and jarvis-leaderboard; rerun the workflow for the claimed property with the named weights; recompute the MAE from the per-material csv against the benchmark json; check the model card's training data for JARVIS-DFT. Hours on CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_vac_en/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_surf_en/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_c11/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/dft_3d_chipsff_kv/>
- <https://pages.nist.gov/jarvis_leaderboard/Special/CHIPS_FF/>
- <https://github.com/usnistgov/chipsff>
- <https://doi.org/10.1021/acsmaterialslett.5c00093>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- JARVIS-DFT uses OptB88vdW while most universal potentials are trained on PBE(+U) data: part of the error is a functional mismatch, so a model trained on PBE has a floor.
- Kv MAEs of 78-136 GPa for every model suggest a few failed relaxations or fits dominate; inspect per-material outputs before tuning.
- The task lists hold different numbers of materials (e.g. 48 for vacancies, 85 for surfaces); score the benchmark's list, not all 104.
- Several leading checkpoints (fairchem eqV2 OMat24 models, UMA) are gated on Hugging Face behind a licence agreement. Accepting it is an action for the human, and the claim should say whether the weights it used need such a step.
- Submitting to the leaderboard is a GitHub pull request, an action for the human.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/jarvis-chipsff-umlip-defect-surface-elastic-mae.md
```

Already set up? Say `run V3R1T4S on jarvis-chipsff-umlip-defect-surface-elastic-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-chipsff-umlip-defect-surface-elastic-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
