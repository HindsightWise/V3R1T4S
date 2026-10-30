# FLIP GB1 fitness landscape: beat the PLMFit scoreboard Spearman on the one-vs-rest or three-vs-rest split

🦠 **Biology** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (8,733 rows, 8,705 of them test under one-vs-rest; sequences are 265 aa with only four positions varying, so one-hot features or frozen small-ESM2 embeddings train on CPU in minutes) · open as of 2026-10-30

## The problem

FLIP (Dallago, Mou, Johnston, Wittmann, Bhattacharya, Goldman, Madani and Yang, NeurIPS 2021 Datasets & Benchmarks) is a set of protein-fitness benchmarks with fixed, published train/test splits and a traffic-light marker saying which splits may be used for performance comparison. Its GB1 landscape comes from Wu, Dai, Olson, Lloyd-Smith and Sun (eLife 2016;5:e16965), a combinatorially complete assay of the four sites V39, D40, G41 and V54 of protein G domain B1. The 8,733 released rows carry the fitness value and the split columns, and every sequence is the 265-residue construct inferred from PDB 5LDE chain A with those four positions substituted, not the 56-residue domain alone. Green splits are one_vs_rest (train = wild type plus all single mutants), two_vs_rest, three_vs_rest and low_vs_high; 'sampled' is orange and must not be used for comparisons. PLMFit (Bikias, Stamkopoulos and Reddy, Briefings in Bioinformatics 26(4):bbaf381, 2025; github.com/LSSI-ETH/plmfit) publishes a scoreboard of the best setups it found. As of 2026-10-30 that scoreboard lists Spearman 0.4571 for GB1 one-vs-rest (ProGen2-small, frozen feature extraction) and 0.8791 for three-vs-rest (ProGen2-medium with adapters). The paper's Table 1 gives train/test counts 29/8,704 and 2,968/5,765. Both released files (FLIP splits.zip and plmfit's gb1_data_full.csv) instead hold 28/8,705 (one-vs-rest) and 2,990/5,743 (three-vs-rest). Of those training rows, 3 and 299 are flagged for validation (FLIP's validation column; plmfit labels them 'validation', leaving 25 and 2,691 'train'). No scoreboard value exists for two_vs_rest or low_vs_high. FLIP's repository received a FLIPv2 release in 2026-03 with new baseline code (ESM-C, Dayhoff, CARP and ESM2 zero-shot); the GB1 split files are unchanged. One-vs-rest is the unsolved cell: extrapolating from singles to doubles, triples and quadruples leaves most of the rank order unexplained, and the data are small enough to run on a laptop CPU.

## What counts as a win

Predictions for every test row of one named FLIP GB1 split that HAS a PLMFit scoreboard value - one_vs_rest or three_vs_rest, both green - from a model fit only on that split's train rows (public pretraining corpora allowed if declared; nothing derived from the test rows). The Spearman correlation, recomputed by the skeptic with scipy.stats.spearmanr against the split's target/score column, must be STRICTLY HIGHER (direction: max) by at least 0.02 than the value listed for that split at https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md (0.4571 one-vs-rest, 0.8791 three-vs-rest as of 2026-10-30; re-fetched live immediately before claiming). It must also be higher than any published value for the same split and test set found by the NOVELTY check, from any year from the 2021 FLIP paper's own baselines onward, including later FLIP releases such as the 2026 FLIPv2 baselines and 2024-2026 papers. Report the mean and standard deviation over at least three seeds, with a bootstrap 95% interval over test sequences that excludes the published bar. Split membership must be taken unchanged from one named released file (one_vs_rest.csv or three_vs_rest.csv in FLIP splits/gb1/splits.zip, or data/gb1/gb1_data_full.csv in the plmfit repo). Name that file in the claim and report the train/test/validation counts it contains. two_vs_rest and low_vs_high have no scoreboard value and cannot be claimed as a record (see p3).

## Partial wins

- **p1:** Beat the listed one-vs-rest Spearman (0.4571) by >= 0.02 with a model of at most 10M parameters, or with no pretrained language model at all, under the same split.
- **p2:** Exceed the listed three-vs-rest Spearman (0.8791) under the same split by less than the full 0.02 margin: a three-seed mean strictly above 0.8791 whose bootstrap 95% interval over test sequences excludes 0.8791, with the full prediction file published.
- **p3:** Publish reference numbers for the two FLIP GB1 green splits that currently have no scoreboard entry (two_vs_rest and low_vs_high) from a released, reproducible pipeline, with seeds and bootstrap intervals - infrastructure, reported as a baseline and not a record.
- **p4:** An ablation, reproducible from released code, isolating how much of the one-vs-rest score is explained by additive single-mutant effects alone (a site-wise linear model) versus epistatic terms, with the residual error analysed per mutation count.

## How a win is checked

Skeptic downloads splits.zip from github.com/J-SNACKKB/FLIP/tree/main/splits/gb1 (or gb1_data_full.csv from the plmfit repo), uses the exact file the claim names, checks that the submitted predictions cover each test sequence exactly once and that the train/test membership matches the published split column, recomputes Spearman with scipy, reruns the attacker's training script from the released seeds to reproduce the number within its stated standard deviation, audits the code for any read of test targets, and re-fetches the PLMFit scoreboard. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>

## Sources

- <https://github.com/J-SNACKKB/FLIP/tree/main/splits/gb1>
- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12309243/fullTextXML>
- <https://elifesciences.org/articles/16965>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- With 28 training sequences (25 if the 3 validation-flagged rows are held out), regularisation is everything: a site-wise additive model with shrinkage, or Gaussian-process regression on a mutation kernel, may beat any fine-tuned language model.
- Cross-domain import (statistical genetics): treat the four mutated sites as loci and fit an additive-plus-pairwise epistasis model with sparsity priors, the standard approach for genotype-phenotype maps.
- Zero-shot ensembling: average rank predictions from several frozen likelihood models (ESM-2 sizes, ProGen2) and calibrate the ensemble on the 28 training points only.
- Data augmentation by symmetry: all four sites are interchangeable in the encoding, so train on site-permuted copies to regularise the pairwise terms.
- Monotone calibration: the metric is rank-based, so fit the model for ranking (pairwise ranking loss) instead of squared error.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 'sampled' split is marked orange in FLIP and must never be used for a performance claim; the PLMFit scoreboard's AAV-sampled entry shows how tempting the easy splits are.
- Only one_vs_rest and three_vs_rest carry a GB1 scoreboard value; quoting a number from another split, or from another dataset's row, is a false record.
- The released sequences are the full 265-residue 5LDE construct, not the 56-residue GB1 domain; the wild type was inferred from 5LDE chain A and the original dataset never contains it, so any pipeline that trims sequences, drops special characters or mismatches lengths changes the test set.
- Counts differ between sources. The PLMFit paper's Table 1 says 29/8,704 (one-vs-rest) and 2,968/5,765 (three-vs-rest). FLIP's split files and plmfit's gb1_data_full.csv both hold 28/8,705 and 2,990/5,743, with 3 and 299 of the training rows flagged validation (FLIP's validation column, plmfit's 'validation' label, leaving 25 and 2,691 'train'). A claim must name its file and report the counts it used.
- low_vs_high exists in FLIP's splits.zip but is not a column in plmfit's gb1_data_full.csv; a pipeline that assumes the two files carry the same columns will silently score the wrong rows.
- Scoreboard values come from ProGen2 models (ProGen2-small is 151M parameters, ProGen2-medium 764M); a claim must state parameter count and compute, and must not compare a tuned model against the scoreboard entry for a different split.
- Rank metrics on thousands of near-identical variants are noisy; a single seed above the bar is not a win, hence three seeds plus a bootstrap.
- The GB1 four-site landscape also appears inside other benchmark suites (for example ProteinGym's SPG1_STRSG_Wu_2016, a larger variant set). A claim must be made on the named FLIP or plmfit split file, not on a reimplementation with different filtering, and numbers from those suites are not comparable bars.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/flip-gb1-plmfit-scoreboard-spearman.md
```

Already set up? Say `run V3R1T4S on flip-gb1-plmfit-scoreboard-spearman`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `flip-gb1-plmfit-scoreboard-spearman`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
