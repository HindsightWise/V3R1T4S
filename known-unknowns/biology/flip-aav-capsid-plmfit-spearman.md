# FLIP AAV capsid fitness: beat the PLMFit scoreboard Spearman on the one-vs-rest (one_vs_many) split

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: laptop-days (82,583 sequences; the mutated region is 28 aa so one-hot or small-embedding models are cheap, full-length embeddings are not) · open as of 2026-10-30

## The problem

The FLIP AAV landscape (Dallago and co-authors, NeurIPS 2021 Datasets & Benchmarks) is built from Bryant, Bashir, Sinai, Jain, Ogden, Riley, Church, Colwell and Kelsic's deep diversification of the adeno-associated virus 2 capsid protein (UniProt P03135, 735 aa), a non-pathogenic, replication-defective gene-therapy vector: mutations are introduced in the 28-residue region 561-588 and the target is the measured packaging/viability score, averaged over synonymous variants. FLIP defines green splits des_mut, mut_des, one_vs_many, two_vs_many, seven_vs_many and low_vs_high, where 'des' are designed or library variants and 'mut' are machine-learning-designed ones; the 'sampled' split is marked orange and may not be used for comparisons. The split columns ship in FLIP's splits/aav/full_data.csv.zip (284,009 rows, of which the 82,583 'des' rows carry the one_vs_many labels) and in splits.zip; the plmfit repository ships only a subsample, data/aav/aav_data_sample.csv, not a full CSV. PLMFit (Bikias, Stamkopoulos and Reddy, Briefings in Bioinformatics 26(4):bbaf381, 2025) keeps a public scoreboard. As of 2026-10-30 it lists Spearman 0.8315 for AAV one-vs-rest (1,170 training sequences at Levenshtein distance <= 1 from the reference region, 81,413 test sequences further away; ProGen2-xlarge with LoRA) and 0.9320 for the orange sampled split. The hard, honest cell is the extrapolation one: train on near-reference variants, predict the distant library, where the paper reports feature extraction averaging about 0.44 against a roughly 0.565 baseline while fine-tuning methods reach about 0.75 on average.

## What counts as a win

Predictions for every test row of the FLIP AAV one_vs_many split (PLMFit's 'one-vs-rest': 1,170 train, 81,413 test), from a model fit only on that split's train rows plus declared public pretraining corpora, such that the Spearman correlation recomputed by the skeptic with scipy.stats.spearmanr against the split's score column is STRICTLY HIGHER (direction: max) than the scoreboard value for that split at https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md (0.8315 as of 2026-10-30; re-fetched live immediately before claiming) by at least 0.01, AND higher than any value for the same split found by the NOVELTY check over 2024-2026 literature, with three seeds (mean and standard deviation) and a bootstrap 95% interval over test sequences excluding the bar. The same Spearman must also be reported on the 81,272 test sequences that survive plmfit's own deduplication (see pitfalls), since that is the set the scoreboard value was measured on. Claims on the orange 'sampled' split do not count, and claims on a green split with no scoreboard entry belong in p3.

## Partial wins

- **p1:** Match the listed 0.8315 to within 0.01 using a model of at most 150M parameters (the scoreboard leader has 6.4B), with compute and parameter count reported.
- **p2:** Beat the attacker's own reproduced feature-extraction baseline on one_vs_many by >= 0.05 Spearman while using only CPU, with the baseline and the new pipeline both published.
- **p3:** Publish reproducible reference Spearman values for the FLIP AAV green splits with no scoreboard entry (des_mut, mut_des, two_vs_many, seven_vs_many, low_vs_high), reported as baselines, not records.
- **p4:** A released analysis of where the error concentrates (by Levenshtein distance from the reference region, by insertion/deletion presence, by stop codons) that identifies one systematic failure mode and shows a fix improving the overall Spearman.

## How a win is checked

Skeptic downloads full_data.csv.zip and splits.zip from github.com/J-SNACKKB/FLIP/tree/main/splits/aav (the plmfit repo ships only aav_data_sample.csv, which is NOT the benchmark), checks the prediction file covers each row with one_vs_many_split == 'test' exactly once with the published split membership (1,170 train / 81,413 test), recomputes Spearman against the 'score' column, reruns the attacker's script from released seeds, audits for any use of test scores or of the orange sampled split, and re-fetches the scoreboard. An hour or two plus training time.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>

## Sources

- <https://github.com/J-SNACKKB/FLIP/tree/main/splits/aav>
- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12309243/fullTextXML>
- <http://data.bioembeddings.com/public/FLIP/fasta/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Only 28 residues vary: encode the mutated region explicitly (one-hot plus insertion/deletion flags) rather than embedding the whole 735-residue capsid, which removes most of the compute and most of the noise.
- Cross-domain import (sequence alignment): the mutation mask encodes insertions and deletions, so a model over aligned region strings with gap tokens may generalise better than a fixed-width encoder.
- Rank-only objectives: Spearman rewards ordering, so train with a listwise or pairwise ranking loss on the 1,170 training points.
- Semi-supervised use of the unlabelled test sequences' identities (transductive feature normalisation) is legitimate as long as no test score is read - declare it explicitly.
- Distance-aware calibration: fit a per-Levenshtein-distance monotone recalibration on held-out training folds to counter the systematic shift away from the reference region.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The orange 'sampled' split (0.9320 on the scoreboard) is not a valid comparison target; quoting it as the bar would make this look saturated when it is not.
- The plmfit repository ships data/aav/aav_data_sample.csv, a 10,000-row subsample, and no aav_data_full.csv; scoring on the sample is not scoring on the benchmark the scoreboard value came from. Use FLIP's full_data.csv.zip or splits.zip.
- plmfit's own parser (data/aav/data_parse.py) keeps the 'des' rows, drops any sequence containing '*' and then drops duplicate full sequences, which leaves 81,272 of the 81,413 one_vs_many test sequences and 985 train plus 110 validation of the 1,170 train rows; 0.8315 was measured on that set, so a claim at the 0.01 margin must report both numbers. The parser also rescales the target to 0-1, which leaves Spearman unchanged.
- Sequences contain special characters ('*' for deletions, lower case for insertions in the mutation mask); naive tokenisation silently corrupts the test set, and full_aa_sequence lengths run from 734 to 749 because of deletions and insertions (28 des rows are 734 long; the paper's Table 1 gives the same range).
- Scores are averaged over synonymous variants in the released file; recomputing targets from the raw study data changes the benchmark.
- The scoreboard leader is a 6.4B-parameter model fine-tuned with LoRA; a CPU-only claim must still clear the same bar, not a self-chosen weaker baseline.
- Any model pretrained on data that already contains this library's measured variants (for example a checkpoint fine-tuned on AAV fitness data) breaks the extrapolation design and must be declared.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/flip-aav-capsid-plmfit-spearman.md
```

Already set up? Say `run V3R1T4S on flip-aav-capsid-plmfit-spearman`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `flip-aav-capsid-plmfit-spearman`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
