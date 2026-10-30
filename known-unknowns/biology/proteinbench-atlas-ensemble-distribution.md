# ProteinBench (ATLAS): beat the best published conformational-ensemble distribution metrics for proteins

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: needs cluster (GPU; 250 conformations for each of 82 proteins, plus metric computation) · open as of 2026-10-30

## The problem

ProteinBench (Fei Ye, Zaixiang Zheng, Dongyu Xue, Yuning Shen, Lihao Wang, Yiming Ma, Yan Wang, Xinyou Wang, Xiangxin Zhou, Quanquan Gu and co-authors, arXiv:2409.06744) includes a distribution-prediction task: predict the conformational ensemble of a protein and compare it with the ATLAS molecular-dynamics ensembles, 82 proteins with 250 sampled conformations per protein, scored by pairwise-RMSD correlation, per-target RMSF correlation, root-mean Wasserstein distance (RMWD), MD-PCA and joint-PCA Wasserstein-2 distances, plus validity checks (CA clash percentage, peptide-bond breaks); the metric suite and the 82-protein test split are those of AlphaFlow (Bowen Jing, Bonnie Berger and Tommi Jaakkola, arXiv:2402.04845). Published medians (Table 15): among the sequence-only rows ConfDiff-Open-MD leads with pairwise-RMSD r 0.59, per-target RMSF r 0.85, RMWD 2.75, MD-PCA W2 1.41 and joint-PCA W2 2.27, with CA clash 0.5 percent and peptide-bond breaks 6.5 percent; AlphaFlow-MD is close (0.53 / 0.85 / 2.64 / 1.55 / 2.29) but breaks 22.2 percent of peptide bonds, while MSA-subsampling reaches only r 0.25 and EigenFold -0.03. Two facts bound what counts as a record. First, re-evaluations of the same sequence-only models disagree with ProteinBench: BBFlow (Nicolas Wolf, Leif Seute, Vsevolod Viliuga, Simon Wagner, Jan Stuehmer and Frauke Graeter, arXiv:2503.05738) reports ConfDiff at r 0.62, RMWD 2.56 and joint-PCA W2 2.19 on the same test set, so the better of the two published numbers is the bar. Second, methods that are handed the test protein's experimental structure score far better and are a different input regime, not a bar for prediction from sequence: AlphaFlow-MD+Templates reaches r 0.94, per-target RMSF r 0.90, RMWD 1.95, MD-PCA W2 1.25 and joint-PCA W2 1.58, and backbone-conditioned BBFlow reaches 0.83 / 2.07 / 1.90. The reference rows show how much room is left in the sequence-only regime: independent MD samples score r 0.96 and joint-PCA W2 0.71, and even a short 2.5 ns MD run scores r 0.89 and joint-PCA W2 1.89, which no sequence-only learned method approaches. Data and metric code are public (ATLAS ensembles and the benchmark repository).

## What counts as a win

An ensemble of 250 conformations per protein for every protein of the ProteinBench ATLAS distribution-prediction test set (the 82-protein AlphaFlow split), generated from sequence - optionally from a declared static structure prediction of that sequence, but with no experimental structure, template or backbone of a test protein as input at any stage, and no ATLAS trajectory for a test protein used in training or selection - such that the skeptic, recomputing the benchmark's metrics with its released code, obtains on a declared metric a value STRICTLY BETTER than the better of the two published sequence-only evaluations: joint-PCA W2 below 2.19 by at least 0.05 (direction: min), or pairwise-RMSD correlation above 0.62 by at least 0.03 (direction: max), or RMWD below 2.56 by at least 0.05 (direction: min) (arXiv:2409.06744 Table 15 and arXiv:2503.05738 Table A.1, both re-fetched live immediately before claiming), and better than any later published sequence-only value for the same task found by the novelty check, while the CA clash percentage stays at or below 1.0 and peptide-bond breaks at or below 7.0 (the ConfDiff-Open-MD row's values, which several published rows fail) and the other listed metrics are all reported. Template-conditioned and backbone-conditioned rows (for example AlphaFlow-MD+Templates or BBFlow) are a different regime: they are neither the bar nor a win here, and a submission that takes any such input does not qualify. Ensembles, configs, seeds and the per-protein metric table must be published.

## Partial wins

- **p1:** Per-target RMSF correlation median strictly above 0.88 - the best published sequence-only value, ConfDiff as re-evaluated in arXiv:2503.05738 - by at least 0.02, with the validity bounds met and all other metrics reported from the same frozen model.
- **p2:** On a declared metric, a value strictly better than the 2.5 ns MD reference row (pairwise-RMSD r above 0.89, or joint-PCA W2 below 1.89, or RMWD below 2.22) on at least a pre-registered half of the 82 proteins, in the sequence-only regime, with the full-set numbers also reported.
- **p3:** A reproduction artefact: reproducing a published method's row (for example AlphaFlow-MD or ConfDiff-Open-MD) within 0.05 on joint-PCA W2 and 0.03 on pairwise-RMSD correlation with public weights and the public metric code, with runtime published.

## How a win is checked

Skeptic downloads the ATLAS test ensembles and the ProteinBench metric code, checks the submission has the required number of conformations for every test protein with correct sequences and no duplicated frames, recomputes every listed metric and the validity checks, verifies from the configs that no ATLAS trajectory of a test protein was used in training or selection (and that MD-trained variants declare their training trajectories), and re-fetches the published table. Hours of compute for scoring.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2409.06744v2>

## Sources

- <https://arxiv.org/html/2409.06744v2>
- <https://arxiv.org/abs/2402.04845>
- <https://arxiv.org/abs/2503.05738>
- <https://proteinbench.github.io/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The MD-trained variants win on distributional metrics while PDB-trained ones win on static accuracy; a two-stage model (PDB pretraining, then MD fine-tuning on non-test proteins) targets the actual metric.
- Cross-domain import (generative evaluation): the metrics are Wasserstein distances between point clouds in PCA space, so explicitly matching low-order moments of the ensemble (variance along the top MD-PCA modes) is more direct than hoping a sampler covers them.
- Cheap physics in the loop: relax sampled conformations with a short energy minimisation to fix clashes and broken peptide bonds, which protects the validity constraint that several published methods violate.
- Spend samples where the ensemble is wide: estimate flexibility first (RMSF proxy) and allocate the 250 conformations per protein non-uniformly along the predicted flexible modes.
- Report per-protein metrics, since medians over 82 proteins hide collapse on the most flexible targets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several published rows are trained on MD data; a method trained on ATLAS trajectories of test proteins is leaking, and the training trajectory list must be declared.
- Template-conditioned and backbone-conditioned models (AlphaFlow-MD+Templates, BBFlow) see the test protein's experimental structure and score far better; feeding such an input, or quoting their rows as the bar, puts a claim outside this target's regime.
- The same model scores differently in different evaluations (ProteinBench and BBFlow differ by 0.03 in pairwise-RMSD r and 0.08 in joint-PCA W2 for ConfDiff), so a claim must clear the better published number and state the metric script and version used.
- Validity metrics must be reported with the distributional ones: an ensemble that scores well while breaking 20 percent of peptide bonds is not a win, even though a published row does exactly that.
- Medians across 82 proteins are reported; mixing means and medians, or scoring a subset, breaks comparability.
- Metric values depend on the number of sampled conformations; 250 per protein is the published protocol and must be matched.
- The ATLAS ensembles are themselves finite MD samples, so the reference rows are a ceiling in practice, not ground truth; claims must stay inside the benchmark.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/proteinbench-atlas-ensemble-distribution.md
```

Already set up? Say `run V3R1T4S on proteinbench-atlas-ensemble-distribution`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `proteinbench-atlas-ensemble-distribution`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
