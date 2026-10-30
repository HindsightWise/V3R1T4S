# Community top-tagging dataset (Kasieczka et al.): beat OmniLearned-l's background rejection 3486 at 30% signal efficiency

💥 **Particle physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (about 1.2M training jets, 1.7 GB in all; a GPU strongly advised; external pre-training on large public jet sets is allowed for the full win but needs cluster time) · open as of 2026-10-30

## The problem

The top-tagging reference dataset (Kasieczka, Plehn, Thompson, Russell; Zenodo 2603256) has about 1.2M training, 400k validation and 404k test jets: boosted hadronic top jets against QCD jets (Pythia 8 + Delphes, 14 TeV, pT 550-650 GeV). It was set up for 'The Machine Learning Landscape of Top Taggers' (Kasieczka et al., SciPost Phys. 7, 014, 2019), and every new jet tagger reports test AUC and background rejection 1/eps_B at eps_S = 0.5 and 0.3 on it. In Table 2 of OmniLearned (Bhimji, Harris, Mikuni, Nachman, arXiv 2510.24066v2, March 2026), the best values come from foundation models fine-tuned after pre-training on other public jet sets. OmniLearned-l has AUC 0.9880 and 1/eps_B(0.3) = 3486 +- 157. At eps_S = 0.5 the best is ParT-f.t. (Qu, Li, Qian) with 691 +- 15, against OmniLearned-l's 688 +- 9. L-GATr-f.t. (Brehmer et al.) gets AUC 0.98793, 651 and 2894. Among taggers trained only on this dataset, the best at eps_S = 0.3 is PELICAN (Bogatskiy et al.): 2289 +- 204 as tabulated by OmniLearned (AUC 0.9869), while its own paper gives 0.9870 and 2250 +- 75. At 0.5 the best is L-GATr with 540 +- 20 (AUC 0.9870, 2240 at 0.3). The comparison tables of SParTA (Baruah, Mondal, Patra, Roy, arXiv 2610.27106, October 2026) and of LLoCa (Favaro et al., arXiv 2508.14898v2) list no higher value. 'The Fundamental Limit of Jet Tagging' (arXiv 2411.02628) suggests there is room above current taggers; SURF (arXiv 2511.15779) disputes how much.

## What counts as a win

A tagger evaluated on the full official test file of Zenodo 2603256 (404,000 jets), with training and model selection using only the train and validation files of that record plus optional pre-training on public datasets that do not contain these test jets. Its 1/eps_B at eps_S = 0.3 must be STRICTLY GREATER (direction: max) than 3486, the best value in Table 2 of arXiv 2510.24066v2, with AUC at least 0.9880. Both values are the mean over at least 5 independent trainings (different seeds), reported with their standard deviation. eps_B is computed by interpolating the test ROC at exactly eps_S = 0.3. Re-check arXiv listings and the status source for a higher published value immediately before claiming.

## Partial wins

- **p1:** Without any external pre-training (training only on the 1.2M official training jets), mean over 5 seeds of 1/eps_B at eps_S = 0.3 strictly above 2289 (PELICAN, the best from-scratch value in Table 2 of arXiv 2510.24066v2), with AUC at least 0.9870. An L-GATr symmetry-breaking ablation in Table 3 of arXiv 2411.00446v3 reached 2293 +- 141 over 3 seeds, but at AUC 0.9869, so it does not meet this bar.
- **p2:** Mean over 5 seeds of 1/eps_B at eps_S = 0.5 strictly above 691 (ParT-f.t., the best value at that working point), under the full-win data rules.
- **p3:** Mean test AUC over 5 seeds of at least 0.9881 (above OmniLearned's 0.9880), under the full-win data rules.

## How a win is checked

Download Zenodo 2603256, load the released model weights and inference script, and recompute predictions on the 404k test jets. Compute the AUC and the ROC-interpolated 1/eps_B at eps_S = 0.3 and 0.5 with sklearn.metrics.roc_curve. Rerun at least 2 of the 5 trainings from the released script to check the reported seed spread. Check that the pre-training sets do not overlap the test file (the dataset is Pythia/Delphes-generated; JetClass, JetClass-II and ATLAS sets are distinct) and re-read Table II of arXiv 2510.24066 plus newer arXiv results.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2510.24066v2>

## Sources

- <https://zenodo.org/records/2603256>
- <https://arxiv.org/abs/1902.09914>
- <https://arxiv.org/abs/2510.24066>
- <https://arxiv.org/abs/2610.27106>
- <https://arxiv.org/abs/2508.14898>
- <https://arxiv.org/abs/2411.00446>
- <https://arxiv.org/abs/2307.16506>
- <https://arxiv.org/abs/2202.03772>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lorentz-equivariant backbones (L-GATr, PELICAN, LLoCa) combined with large-scale pre-training: the from-scratch leaders have never been pre-trained at OmniLearned's scale.
- Ensembling several independently trained strong taggers raises tail rejection at eps_S = 0.3 more than it raises AUC.
- Knowledge distillation from a large fine-tuned teacher into an equivariant student.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rejection at eps_S = 0.3 has a seed spread of 100-200; a single lucky seed is not a win. Use the mean over 5 seeds.
- Some papers quote rejection at the nearest ROC point instead of interpolating; use interpolation at exactly 0.3.
- Pre-training sets must be public and must not contain the test jets.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/particle-physics/top-tagging-landscape-rejection-record.md
```

Already set up? Say `run V3R1T4S on top-tagging-landscape-rejection-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `top-tagging-landscape-rejection-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
