# JetClass 10-class jet tagging: beat L-GATr's 0.866 accuracy and 0.9885 macro AUC on the 20M-jet test set

💥 **Particle physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (100M training jets in about 152 GB of files, 190 GB with validation and test; reference models train for days on multiple GPUs) · open as of 2026-10-30

## The problem

JetClass (Qu, Li, Qian; Zenodo 6619768; 'Particle Transformer for Jet Tagging', ICML 2022) has 100M training, 5M validation and 20M test jets in 10 classes: QCD, H->bb, H->cc, H->gg, H->4q, H->lvqq', t->bqq', t->blv, W->qq' and Z->qq (MadGraph + Pythia + Delphes). It is the standard large-scale jet tagging benchmark. Metrics are overall test accuracy, macro AUC, and per-class QCD rejection at fixed signal efficiency (50% for most classes, 99% for H->lvqq', 99.5% for t->blv). ParT reached 0.861 / 0.9877 and MIParT-L 0.861 / 0.9878. The Lorentz-equivariant geometric algebra transformer L-GATr (Brehmer, Breso, de Haan, Plehn, Qu, Spinner, Thaler; arXiv 2411.00446v3, SciPost Phys. 19, 108, 2025, Table 4) holds the record at accuracy 0.866 and AUC 0.9885. Its rejections are 12987 (Hbb), 4819 (Hcc), 128 (Hgg), 2311 (H4q), 6116 (Hlvqq), 47619 (tbqq), 20408 (tblv), 588 (Wqq) and 432 (Zqq). The November 2025 comparison in 'Lorentz-Equivariance without Limitations' (Favaro et al., arXiv 2508.14898v2, Table 3) still lists L-GATr first, ahead of LLoCa-ParT and LLoCa-Transformer (both 0.864 / 0.9882). No higher full-dataset value was found in the sources checked. Results on 2M or 10M training subsets, or with reduced input features, are not comparable.

## What counts as a win

A classifier trained only on the JetClass training split (validation split allowed for model selection; no other data) and evaluated on all 20M JetClass test jets, with the full input feature set of the ParT repository (kinematics, particle ID and trajectory displacement). Its overall accuracy must be STRICTLY GREATER than 0.866 AND its macro AUC STRICTLY GREATER than 0.9885 (direction: max). The AUC follows the ParT evaluation: sklearn roc_auc_score with average='macro' and multi_class='ovo', the average over all pairwise class combinations as stated in Table 4 of arXiv 2411.00446, not one-vs-rest. Both values are rounded the same way as that table, so at least 0.867 and 0.9886. Re-check the status source and arXiv for a newer record immediately before claiming.

## Partial wins

- **p1:** Under the full-win rules, beat L-GATr's per-class rejection in at least 5 of the 9 signal classes (Table 4 values of arXiv 2411.00446) while keeping accuracy at least 0.866.
- **p2:** Under the full-win rules, macro AUC at least 0.9886 or accuracy at least 0.867, without necessarily both.
- **p3:** Under the full-win rules, accuracy at least 0.861 (ParT's value) with a model of at most 300k trainable parameters, evaluated on the full 20M test set.

## How a win is checked

Download JetClass from Zenodo 6619768, run the released checkpoint over all 20M test jets with the ParT repository's data configuration, and compute accuracy, macro AUC and per-class rejection with the ParT evaluation conventions (rejection = 1/eps_QCD at the stated signal efficiency in the signal-vs-QCD score). Inspect the training script to confirm that no test file was used, and compare with Table 4 of arXiv 2411.00446 and any newer arXiv table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2508.14898>

## Sources

- <https://zenodo.org/records/6619768>
- <https://github.com/jet-universe/particle_transformer>
- <https://arxiv.org/abs/2202.03772>
- <https://arxiv.org/abs/2411.00446>
- <https://arxiv.org/abs/2508.14898>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Scaling Lorentz-equivariant transformers (L-GATr, LLoCa) in width and depth: JetClass has not saturated with dataset size.
- Self-supervised pre-training on the JetClass training jets themselves (no outside data) before supervised training.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Subset results (2M or 10M training jets) are not comparable with the 100M-jet record.
- Use the 'full' feature set; kinematics-only or kin+PID numbers are lower by construction and not comparable.
- Accuracy is reported to 3 decimals; 0.8664 rounds to 0.866 and does not count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/particle-physics/jetclass-ten-class-accuracy-auc.md
```

Already set up? Say `run V3R1T4S on jetclass-ten-class-accuracy-auc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jetclass-ten-class-accuracy-auc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
