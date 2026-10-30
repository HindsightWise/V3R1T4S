# FLIP meltome mixed split: beat the PLMFit scoreboard Spearman for melting temperature from sequence

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: laptop-days (24,817 train / 3,134 test full-length proteins; CPU embedding of long sequences dominates, small-ESM2 features are feasible) · open as of 2026-10-30

## The problem

The FLIP meltome landscape (Dallago and co-authors, NeurIPS 2021 Datasets & Benchmarks) turns the Meltome Atlas of Jarzab, Kurzawa, Hopf and co-authors (Nature Methods 17:495-503, 2020) into a sequence-to-melting-temperature regression. Sequences were clustered at 20% identity with MMseqs2 and the clusters split 80/20, so the green 'mixed' split trains on cluster members and tests on cluster representatives (the 'full' and 'clustered' variants are marked red and must not be used); 'human' (8,148/1,945) and 'human_cell' (5,792/1,366) are green restrictions of the same construction. This is thermostability prediction across the tree of life with no homology shortcut, and it stays far from saturated: the PLMFit scoreboard (Bikias, Stamkopoulos and Reddy, Briefings in Bioinformatics 26(4):bbaf381, 2025) lists Spearman 0.7232 for meltome mixed as of 2026-10-30, reached with ProGen2-xlarge and LoRA. FLIP's mixed_split.csv (27,951 rows) carries 24,817 training and 3,134 test proteins, the counts the paper's Table 1 reports, but PLMFit's pipeline loads data/meltome/meltome_data_full.csv, which its own data_parse.py builds from that same file by dropping sequences containing '*', dropping duplicate sequences and keeping only lengths <= 750: 19,003 rows, 14,781 train / 1,651 validation / 2,571 test, and the 20-750 length range Table 1 also quotes. The 2,571 test proteins are a subset of the 3,134 (the 563 that are missing are longer than 750 aa), so the 0.7232 is a 2,571-protein number and a claim here has to report both sets. The paper reports that on this task fine-tuning can improve on the baseline methods by up to 117.82% where frozen feature extraction does not. No entry exists on that scoreboard for the green human or human_cell splits.

## What counts as a win

Predicted melting temperatures for the FLIP meltome 'mixed' split, from a model fit only on rows that split marks train or validation (plus declared public pretraining corpora with no melting-point supervision), scored on BOTH released test sets and clearing the bar on each: (a) the 2,571 rows with mixed == 'test' in plmfit's data/meltome/meltome_data_full.csv at https://github.com/LSSI-ETH/plmfit/tree/main/data/meltome, which is the set the scoreboard value was measured on, and (b) all 3,134 rows with set == 'test' in mixed_split.csv inside splits.zip at https://github.com/J-SNACKKB/FLIP/tree/main/splits/meltome (24,817 train / 3,134 test). On each set the Spearman correlation recomputed by the skeptic with scipy.stats.spearmanr against that file's target column ('score' in the plmfit file, 'target' in FLIP's) must be STRICTLY HIGHER (direction: max) than the scoreboard value at https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md (0.7232 as of 2026-10-30; re-fetched live immediately before claiming) by at least 0.02, AND higher than any value for the same split found by the NOVELTY check over 2024-2026 literature, reported over at least three seeds with a bootstrap 95% interval over test proteins that excludes the bar. Red splits ('full', 'clustered') do not count.

## Partial wins

- **p1:** Beat 0.7232 by >= 0.02 on the mixed split using only CPU and a model of at most 150M parameters, with wall-clock time reported.
- **p2:** Publish reproducible reference Spearman values for the green 'human' and 'human_cell' splits (no scoreboard entry today) with seeds and bootstrap intervals, reported as baselines rather than records.
- **p3:** A released error analysis over the test clusters showing which organisms or length ranges carry the error, plus a fix that demonstrably improves the mixed-split Spearman.
- **p4:** A leakage audit of the mixed split: show, from the released cluster file, whether any test representative has a training member above a stated identity threshold, and report the Spearman restricted to the clean subset.

## How a win is checked

Skeptic downloads splits.zip and meltome_PIDE20_clusters.tsv from github.com/J-SNACKKB/FLIP/tree/main/splits/meltome, uses mixed_split.csv unchanged, checks the prediction file covers each test protein exactly once with the published 'set' column and that the counts are 24,817/3,134, recomputes Spearman, reruns the attacker's pipeline from released seeds, audits for use of the red splits or of test targets and for any melting-point-supervised pretrained checkpoint, and re-fetches the scoreboard. An hour or two plus training time.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>

## Sources

- <https://github.com/J-SNACKKB/FLIP/tree/main/splits/meltome>
- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12309243/fullTextXML>
- <https://www.nature.com/articles/s41592-020-0801-4>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Melting temperature correlates strongly with organism growth temperature and with composition (charged-residue fraction, IVYWREL); a well-regularised model on cheap global features plus small embeddings is a serious baseline that costs minutes.
- Cross-domain import (domain adaptation): the mixed split puts cluster representatives in test, so importance weighting or domain-adversarial training against cluster identity targets exactly the shift being measured.
- Length and run-level batch effects exist in the atlas; model the run as a random effect on the training side only.
- Pool per-residue embeddings with attentive statistics pooling (from speaker recognition) instead of mean pooling, which loses the local signals that set stability.
- Multi-task training with the green human and human_cell splits as auxiliary targets, which share the construction but differ in distribution.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 'full' and 'clustered' splits are red in FLIP: performance on them is not comparable and must not be quoted as the bar. splits.zip in fact ships only mixed_split.csv, human.csv and human_cell.csv.
- plmfit's data/meltome/meltome_data_full.csv is the file its loader actually reads, and data_parse.py builds it from mixed_split.csv by dropping sequences containing '*', dropping duplicate sequences and keeping lengths <= 750 (not 1,000 aa, as the plmfit data README says): 19,003 rows, 14,781 train / 1,651 validation / 2,571 test. Its test set is FLIP's 3,134 minus the 563 proteins longer than 750 aa, and 5,449 rows of the whole split exceed that length. Scoring one set against the other's bar silently changes the comparison, which is why both are required.
- Melting points in the atlas can be null and the proteinId/runName pair is not always unique; FLIP's 24,817 training rows hold only 20,206 distinct sequences (and no training sequence appears in the test set), so dropping or deduplicating rows differently from the released split changes the benchmark.
- Any pretrained model that saw melting-point labels (for example a thermostability-fine-tuned checkpoint) breaks the comparison and must be declared.
- Full-length embeddings for 28,000 proteins on CPU can take days; a claim should report compute honestly rather than silently truncating sequences, since truncation changes the test inputs.
- Scoreboard numbers come from a 6.4B-parameter model; comparing a small model against a different, self-chosen baseline is not a record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/flip-meltome-mixed-plmfit-spearman.md
```

Already set up? Say `run V3R1T4S on flip-meltome-mixed-plmfit-spearman`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `flip-meltome-mixed-plmfit-spearman`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
