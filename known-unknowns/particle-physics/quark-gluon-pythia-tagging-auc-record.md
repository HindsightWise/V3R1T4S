# Pythia quark-gluon jet tagging (Komiske-Metodiev-Thaler dataset): beat PELICAN's AUC 0.9252 with particle-ID inputs

💥 **Particle physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (2M jets in 20 files, about 2.1 GB; a single GPU brings training down to a few hours) · open as of 2026-10-30

## The problem

The 'Pythia8 Quark and Gluon Jets for Energy Flow' dataset (Komiske, Metodiev, Thaler; Zenodo 3164691, version without c and b quarks) has 2M anti-kT R = 0.4 jets with pT 500-550 GeV and |y| < 2: light-quark jets from Z+q against gluon jets from Z+g, with each particle's PDG ID stored. It is the standard quark-gluon benchmark. The usual split (PELICAN, ParT) takes the first 200k jets as validation, the next 200k as test and the remaining 1.6M as training. With full particle-ID inputs, the record is PELICAN (Bogatskiy, Hoffman, Miller, Offermann, Liu; arXiv 2307.16506, JHEP 03 (2024) 113, Table 4): accuracy 0.8551, AUC 0.9252, 1/eps_B = 149.8 +- 2.4 at eps_S = 0.3 and 52.3 +- 0.3 at 0.5. It is ahead of ParT-full (0.9203) and of JetClass-fine-tuned models with full PID: ParT-f.t. 0.9230 and MIParT-L-f.t. 0.9237, as tabulated in SParTA (arXiv 2610.27106, Oct 2026), whose comparison still puts PELICAN first. Without PID, the best is PELICAN at AUC 0.9076 (94.5 / 37.5), and among IRC-safe taggers PELICAN-IRC reaches 0.9056.

## What counts as a win

A classifier trained on the 1.6M training jets (jets 400,001 to 2,000,000 of the 20 no-bc files concatenated in numeric order QG_jets.npz, QG_jets_1.npz, QG_jets_2.npz, ..., QG_jets_19.npz, the order energyflow's qg_jets loader uses, not lexicographic order), selected on jets 1 to 200,000 and evaluated once on test jets 200,001 to 400,000. Inputs are constituent four-momenta plus the dataset's particle IDs; no external pre-training is used, so the comparison with PELICAN is like-for-like. The mean test AUC over at least 5 seeds must be STRICTLY GREATER than 0.9252 (direction: max), and the mean 1/eps_B at eps_S = 0.3 must be at least 149.8.

## Partial wins

- **p1:** Without particle-ID inputs (four-momenta only), under the same split and no pre-training, mean test AUC over 5 seeds strictly above 0.9076 (PELICAN without PID).
- **p2:** An IRC-safe tagger (an output provably invariant under soft and collinear splittings, e.g. an energy-weighted architecture) with mean test AUC strictly above 0.9056 (PELICAN-IRC).
- **p3:** With full PID inputs and external pre-training allowed (public datasets that do not contain these jets), mean test 1/eps_B at eps_S = 0.5 strictly above 52.3.

## How a win is checked

Download Zenodo 3164691 (QG_jets.npz to QG_jets_19.npz, no bc), rebuild the index-ordered split, run the released weights on test jets 200,001 to 400,000 and compute AUC and interpolated rejections with sklearn. Rerun at least 2 seeds from the released script. Confirm that no test jets were used for training, early stopping or calibration.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2307.16506>

## Sources

- <https://zenodo.org/records/3164691>
- <https://arxiv.org/abs/1810.05165>
- <https://arxiv.org/abs/2307.16506>
- <https://arxiv.org/abs/2610.27106>
- <https://arxiv.org/abs/2202.03772>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- PELICAN is small (209k parameters); scaling a Lorentz-invariant architecture with PID embeddings has not been reported on this dataset.
- Ensembling PELICAN-like and transformer taggers, whose errors on gluon-like quarks may differ.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Feature sets differ across papers: 'exp' (5-class) PID results (e.g. OmniLearned's 0.9162) are not comparable with full-PDG-ID results.
- Different papers use different splits; state yours exactly as above.
- The '_withbc' variant of the dataset is a different benchmark.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/particle-physics/quark-gluon-pythia-tagging-auc-record.md
```

Already set up? Say `run V3R1T4S on quark-gluon-pythia-tagging-auc-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quark-gluon-pythia-tagging-auc-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
