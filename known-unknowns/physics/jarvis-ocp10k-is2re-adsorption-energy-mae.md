# Data-efficient catalysis on Open Catalyst (JARVIS ocp10k): predict OC20 relaxed adsorption energies on the 24,943 val-ID systems from 10,000 training systems with MAE below ALIGNN's 0.7623 eV

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (CPU) or GPU-hours; 10,000 training adsorbate-slab systems of ~80 atoms · open as of 2026-10-30

## The problem

The Open Catalyst 2020 dataset (Lowik Chanussot, Abhishek Das, Siddharth Goyal, Zachary Ulissi, C. Lawrence Zitnick and co-workers; ACS Catal. 11, 6059, 2021; arXiv:2010.09990) defines IS2RE: predict the DFT (RPBE) relaxed adsorption energy of an adsorbate-surface system from its initial structure. Its official 10k training subset is the data-poor regime, where the paper's learning curves are flattest. The JARVIS-Leaderboard task ocp10k_relaxed_energy (Kamal Choudhary et al., NIST) fixes this with public labels. Train is the 10,000 OC20 IS2RE 10k systems (ids ocp-1..ocp-10000); test is the 24,943 OC20 IS2RE val_id systems (ocp-34944..ocp-59886). The benchmark's val ids (ocp-10001..ocp-34943) duplicate the test set label for label, as verified for this update, because the conversion script reads val_id twice. Live best MAE is 0.7623 eV by ALIGNN (2023-01-14), then OCP's CGCNN 0.9873 and SchNet 1.0578. Published 10k-only results on val_id are all worse: - The OCP model zoo (v0.1.0 MODELS.md) lists DimeNet++ 0.8837, CGCNN 0.9881, DimeNet 1.0117 and SchNet 1.059 eV. - Alvaro Carbonero, Alexandre Duval, Victor Schmidt, Santiago Miret and co-workers (arXiv:2310.06682, Table 2) report DimeNet++ at 0.851 eV in-domain. The companion ocp100k task (100,000 training systems, same test set) is led by ALIGNN at 0.6289 eV; the OCP zoo's 100k DimeNet++ scores 0.6388. Both pages were HTTP 200 for this update, with no entries since January 2023.

## What counts as a win

Success means a trained model, its training script and predictions for all 24,943 test ids of ocp10k_relaxed_energy. The MAE recomputed by the checker against the benchmark json must be STRICTLY LOWER (direction: min) than the best MAE on the live task page re-fetched immediately before claiming (0.7623 eV on 2026-10-28). The margin must be at least 3% relative AND exceed the half-width of a 1,000-sample paired bootstrap 90% interval of the MAE difference against the best listed predictions (the CSV linked on the page). All learned parameters must come only from the 10,000 train ids: no pretrained weights; no OC20, OC22, OC25, OC20-Dense, ODAC, OMat24, MPtrj, OMol25 or other DFT data; and no use at all of the duplicated val ids, including for early stopping. Model selection uses a held-out part of the 10,000 train ids. Physics featurisers whose parameters were not fitted to adsorbate-surface DFT data, such as GFN-xTB or GFN-FF single points of the initial structure, are allowed. Because the JARVIS split is the standard OC20 IS2RE 10k train / val_id split, the claim must also report, and beat by the same margin, every published from-scratch 10k-only val_id energy MAE found by a literature search (including the OCP model-zoo and arXiv:2310.06682 values above). Re-running the saved model must reproduce the predictions to 1e-4 eV.

## Partial wins

- **p1:** The same margin over 0.7623 eV for a model that starts from a pretrained universal potential documented to contain no adsorbate-surface systems in its training data, fine-tuned only on the 10,000 train ids. Examples are MPtrj-only or OMat24-plus-sAlex models, with training sets named in the claim; UMA and any weights trained on OC20, OC22 or OC25 are excluded.
- **p2:** The from-scratch rules on ocp100k_relaxed_energy (100,000 train ids, the same 24,943 test systems, and again a val set identical to test): beat the live best 0.6289 eV by 3% relative and beat the OCP model zoo's 100k DimeNet++ value of 0.6388 eV.

## How a win is checked

Checker, under 30 minutes plus inference time: download ocp10k_relaxed_energy.json.zip from the jarvis_leaderboard repository, take the 24,943 test ids, and recompute the MAE and the paired bootstrap against the best listed CSV. Then audit the training script for any val or test id and any external data, and re-run inference on a random 1,000-structure sample to confirm reproducibility. Structures come from the jarvis-tools 'ocp10k' dataset or directly from the OC20 IS2RE 10k and val_id LMDBs (fairchem); the LMDBs carry the same initial positions plus OC20 tags.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/ocp10k_relaxed_energy/>

## Sources

- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/ocp10k_relaxed_energy/>
- <https://pages.nist.gov/jarvis_leaderboard/AI/SinglePropertyPrediction/ocp100k_relaxed_energy/>
- <https://raw.githubusercontent.com/usnistgov/jarvis_leaderboard/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/ocp10k_relaxed_energy.json.zip>
- <https://github.com/usnistgov/jarvis_leaderboard/blob/main/jarvis_leaderboard/benchmarks/AI/SinglePropertyPrediction/ocp2jarvis1std_10k.py>
- <https://arxiv.org/abs/2010.09990>
- <https://github.com/Open-Catalyst-Project/ocp/blob/v0.1.0/MODELS.md>
- <https://arxiv.org/abs/2310.06682>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Physics priors for few-shot catalysis: binding-atom coordination, generalised coordination numbers, element-level d-band proxies and adsorbate scaling relations (O*, OH* and OOH* energies correlate) as features for a boosted model.
- Equivariant message passing restricted to the adsorbate and the top surface layer, since the OC20 subsurface atoms (tag 0) add cost but little signal at 10k.
- Delta-learning on a cheap physics baseline: a GFN-FF or GFN-xTB adsorption-energy estimate from the initial structure, with the 10,000 labels fitting the residual.
- Symmetry augmentation: equivalent adsorption sites, surface-normal rotations and periodic-image shifts.
- Cross-domain (few-shot learning): meta-learning across adsorbate types, or Gaussian-process heads on learned embeddings for calibrated small-data regression.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The val split is the test set under different ids. Using it for early stopping, hyperparameter search or ensembling is leakage; ALIGNN's own run script took its 100-structure validation set from the test rows.
- OC20 val_id labels are public in OC20 itself, and many OC20, OC22 and UMA checkpoints were trained or validated on val_id systems. Any such weights invalidate the full win and p1.
- The JARVIS structures drop OC20's adsorbate/surface/subsurface tags and fixed-atom flags. Rebuild them from the OC20 LMDBs, because element-based guesses fail on carbides, nitrides and hydrides.
- Targets are adsorption energies relative to gas-phase references, not total energies; do not mix in total-energy datasets.
- jarvis-tools downloads its datasets from figshare, which answered this update's scripted fetch with HTTP 202 and an empty body (a bot check). Fetch it honestly in a browser or use the OC20 LMDBs; never work around the check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/jarvis-ocp10k-is2re-adsorption-energy-mae.md
```

Already set up? Say `run V3R1T4S on jarvis-ocp10k-is2re-adsorption-energy-mae`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jarvis-ocp10k-is2re-adsorption-energy-mae`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
