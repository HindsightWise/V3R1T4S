# BEACON RNA benchmark: beat the best listed score on an unsaturated task (CRISPR off-target, structure-score imputation, splice sites, APA, RNA switches)

🦠 **Biology** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (most tasks are short RNA sequences with 10^3-10^5 training examples; fine-tuning a 100M RNA language model wants a GPU) · open as of 2026-10-30

## The problem

BEACON (Yuchen Ren, Zhiyuan Chen, Lifeng Qiao, Hongtai Jing, Yuchen Cai, Sheng Xu, Peng Ye, Xinzhu Ma, Siqi Sun, Hongliang Yan, Dong Yuan, Wanli Ouyang and Xihui Liu, NeurIPS 2024 Datasets and Benchmarks, arXiv:2406.10391; code and data at github.com/terry-r123/RNABenchmark, Apache-2.0) fixes 13 RNA tasks with train/validation/test splits and a common evaluation harness. It benchmarks CNN, ResNet and LSTM baselines and 14 RNA language-model variants (RNA-FM, RNABERT, RNA-MSM, three SpliceBERT, two UTR-LM, four UTRBERT, BEACON-B and BEACON-B512) over three seeds. Several tasks are far from saturated (best values in the main table, x100 where applicable): CRISPR off-target Spearman 11.50 (ResNet; the paper's literature column lists 12.6); structure-score imputation from icSHAPE R^2 42.36 (RNA-FM); splice-site ACC@K 50.55 (SpliceBERT-MS510) on 100-nt inputs (the centre 100 nt of 5,000-nt blocks, BEACON Table 1 and A.2.5) from genes on SpliceAI's test chromosomes 1, 3, 5, 7 and 9; programmable RNA switch R^2 57.72 (SpliceBERT-MS1024); alternative polyadenylation isoform R^2 72.71 (UTRBERT-4mer). This target leaves out BEACON's secondary-structure task (bpRNA), its mean-ribosome-loading task (several models in the table already exceed the literature value and RiNALMo reports a higher R^2 on a similar Optimus test set, so the table bar is not current) and its mRNA-vaccine degradation task.

## What counts as a win

Predictions for every test example of a BEACON task among CRISPR off-target (CRI-Off), structure-score imputation (SSI), splice-site prediction (SPL), programmable RNA switches (PRS) or APA isoform (APA), from a model trained only on that task's BEACON train split (validation for selection; pretrained weights allowed if declared and free of the task's test labels), whose metric, computed by the skeptic with the BEACON repository's evaluation code as the mean over at least three seeds, is STRICTLY HIGHER (direction: max) than the bar by at least 1.0 point on the x100 scale (2.0 for CRI-Off). Bars as of 2026-10-30 (max of the main table and the paper's literature column, to be re-read from arXiv:2406.10391v2 before claiming): CRI-Off 12.6, SSI 42.36, SPL 50.55, PRS 57.72, APA 72.71. The bar must also exceed any later published value on the same split found by a novelty check.

## Partial wins

- **p1:** Beat the bar by at least 0.5 points on any one of the five named tasks (mean of three seeds, every seed above the bar), computed with BEACON's code.
- **p2:** One frozen recipe (same architecture and training schedule) that beats BEACON-B's published Table 3 score on at least 8 of the 11 BEACON tasks other than secondary structure (SSP) and vaccine degradation (VDP), mean of three seeds.
- **p3:** CRISPR off-target: Spearman STRICTLY HIGHER than 12.6 by any margin with a model of at most 5M parameters, mean of three seeds.

## How a win is checked

Skeptic clones the BEACON repository, downloads the task data from its linked Google Drive, checks prediction coverage of the test split, runs the repository's metric code, reruns one seed of the attacker's training, and checks that no test sequence (exact, or at 90% or higher identity for SPL and SSI) is in training. Under an hour per task.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2406.10391>

## Sources

- <https://arxiv.org/html/2406.10391>
- <https://arxiv.org/abs/2406.10391>
- <https://github.com/terry-r123/RNABenchmark>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- CRISPR off-target: the signal is mismatch position and type between guide and site; explicit pairwise alignment features beat a language model fed concatenated sequences in most published comparisons.
- Structure-score imputation is masked-value regression; a model that predicts base-pairing probabilities (ViennaRNA) as an extra input channel is a cheap physics prior.
- Cross-domain import (recommender systems): for APA isoform usage, treat the two polyA sites as items and learn a pairwise preference, not two independent regressions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Text extraction of the main table can misalign the 'literature SOTA' row; re-read the table from the PDF before quoting a bar.
- SPL uses short windows and ACC@K on BEACON's own subset; it is not SpliceAI's full-transcript top-k accuracy, so the two cannot be compared.
- SpliceBERT and other models pretrained on genomes saw the test regions unlabelled; this is allowed but must be declared.
- Do not tune on the test split; BEACON provides a validation split for every task.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/beacon-rna-benchmark-unsaturated-tasks.md
```

Already set up? Say `run V3R1T4S on beacon-rna-benchmark-unsaturated-tasks`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `beacon-rna-benchmark-unsaturated-tasks`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
