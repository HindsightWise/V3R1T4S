# Matbench v0.1 large tasks (mp_e_form, mp_gap, mp_is_metal): beat the best published Matbench-protocol score (JMP-L's 0.0101 eV/atom and 0.091 eV, CGCNN's 0.9520 balanced accuracy)

⚗️ **Chemistry and materials** · standard · tractability ★☆☆☆☆ · compute: needs cluster (fine-tuning a pretrained model like JMP-L over 5 nested folds of 106k-133k structures takes GPU-days); the partial wins fit laptop-days on one GPU · open as of 2026-10-30

## The problem

Matbench v0.1 (Alexander Dunn, Qi Wang, Alex Ganose, Daniel Dopp and Anubhav Jain, npj Comput. Mater. 6, 138, 2020) has three large Materials Project tasks, each with fixed 5-fold nested cross-validation. The per-task leaderboards on 2026-10-30 read: matbench_mp_e_form (132,752 structures, formation energy), MAE 0.0170 +- 0.0003 eV/atom by coGN, then coNGN 0.0178, ALIGNN 0.0215 and SchNet (kgcnn) 0.0218; matbench_mp_gap (106,113 structures, PBE band gap), MAE 0.1559 +- 0.0017 eV by coGN, then DeeperGATGNN 0.1694, coNGN 0.1697 and ALIGNN 0.1861; matbench_mp_is_metal (106,113 structures), 0.9520 +- 0.0074 by CGCNN v2019 in the column labelled rocauc (which equals balanced accuracy, as the matbench pages note for thresholded predictions), then ALIGNN 0.9128 and coGN 0.9124. coGN and coNGN are the connectivity-optimised nested graph networks of Robin Ruff, Patrick Reiser, Jan Stuehmer and Pascal Friederich (kgcnn); CGCNN is by Tian Xie and Jeffrey Grossman. Lower Matbench-protocol scores have been published off the leaderboard. JMP (Nima Shoghi, Adeesh Kolluru, John Kitchin, Zachary Ulissi, Larry Zitnick and Brandon Wood, Meta FAIR and CMU, ICLR 2024, arXiv:2310.16802 Table 4) pretrains a GemNet-OC model on OC20, OC22, ANI-1x and Transition-1x (no Materials Project data) and fine-tunes it on each fold. JMP-L (235M parameters) reports 5-fold means of 10.1 meV/atom (0.0101 eV/atom) on mp_e_form and 0.091 eV on mp_gap; JMP-S reports 0.0133 and 0.121. CrysToGraph (Hongyi Wang, Sheng Gong and co-authors, arXiv:2407.16131 v2, Table 3) reports 0.0168 and 0.1522. Some lower scores build on potentials trained on MPtrj and fall under the leakage rule, so they do not set the bar: fine-tuned MatterSim (0.12 eV) and fine-tuned ORB (about 0.10 eV) on mp_gap, both quoted in HackNIP (arXiv:2506.18497), and DenseGNN-CHGNet (arXiv:2509.05712). No published non-leaking mp_is_metal score above CGCNN's was found (CrysToGraph 0.9146). The small and medium Matbench tasks are separate entries (matbench-small-data-tasks, matbench-medium-structure-tasks-cpu).

## What counts as a win

For one of the three tasks: saved code and per-fold predictions that the skeptic re-runs with the official matbench package (MatbenchBenchmark v0.1, fixed folds, hyperparameters chosen only inside training folds). The mean score must be STRICTLY BETTER than both (a) the best entry on the live per-task leaderboard (re-fetched immediately before claiming) and (b) the best published Matbench-protocol score for that task from a model that obeys the leakage rule below. Today the binding bars are 0.0101 eV/atom for mp_e_form and 0.091 eV for mp_gap, both 5-fold means by JMP-L (arXiv:2310.16802 Table 4), lower mean MAE (direction: min). For mp_is_metal the bar is higher mean balanced accuracy of predictions thresholded at 0.5 (direction: max), which is the quantity the page's existing 'rocauc' values actually report (CGCNN v2019 0.9520). The margin must exceed the larger of 1% relative and a fold standard deviation: the bar-holder's where one is published, otherwise the claim's own. No model or pretraining whose training data includes Materials Project calculations of the test structures. That rules out off-the-shelf universal potentials trained on MPtrj, MP-ALOE, Alexandria or OMat24 unless test structures are provably excluded. The claim must also beat every other non-leaking Matbench-protocol score for that task that the skeptic finds published.

## Partial wins

- **p1:** Beat ALIGNN's per-task score on mp_gap (0.1861) or mp_e_form (0.0215) under the full protocol with a model trained on CPU only, with wall-clock logs.
- **p2:** Beat ALIGNN, the second-best entry on mp_is_metal (mean balanced accuracy 0.9128 at a 0.5 threshold), under the full protocol with any structure-based model, a step towards CGCNN's 0.9520.
- **p3:** Beat coGN's leaderboard score on mp_e_form (0.0170) or mp_gap (0.1559) by the full-win margin under the full protocol with a model that uses no pretraining and no external data of any kind.

## How a win is checked

Skeptic installs matbench, reruns the saved script for one fold to confirm the score, recomputes the task metric from all saved per-fold predictions, compares with the live per-task page and audits the training data for MP leakage. GPU-hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_mp_e_form/>

## Sources

- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_mp_e_form/>
- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_mp_gap/>
- <https://matbench.materialsproject.org/Leaderboards%20Per-Task/matbench_v0.1_matbench_mp_is_metal/>
- <https://matbench.materialsproject.org/>
- <https://arxiv.org/abs/2310.16802>
- <https://arxiv.org/abs/2407.16131>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Universal interatomic potentials and foundation models trained on MP-derived data have seen the test labels; such scores do not count.
- The binding bars for mp_e_form and mp_gap are published scores (JMP-L) that are not on the per-task page. Search papers citing JMP and Matbench for newer non-leaking scores before claiming.
- For mp_is_metal the page's existing 'rocauc' values are balanced accuracy of 0.5-thresholded predictions. The page says scoring is fixed for future submissions, so a new leaderboard score may be a true ROC-AUC that is not comparable; compare balanced accuracy only.
- Submitting to the leaderboard is a GitHub pull request, an action for the human.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/matbench-large-mp-tasks.md
```

Already set up? Say `run V3R1T4S on matbench-large-mp-tasks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `matbench-large-mp-tasks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
