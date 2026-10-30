# Trastuzumab CDR-H3 variant binding (PLMFit herH3 one-vs-rest): beat the scoreboard MCC of 0.3898

🦠 **Biology** · standard · tractability ★★★★☆ · compute: laptop-hours (174 training sequences, 36,386 test; the variable region is 10 aa, so CPU-only models suffice) · open as of 2026-10-30

## The problem

Mason, Friedensohn, Weber and co-authors, with Reddy, measured antigen binding for a deep mutational library of the CDR-H3 loop of the therapeutic antibody trastuzumab (data released at github.com/dahjan/DMS_opt), a standard testbed for predicting which CDR variants keep binding their target. PLMFit (Bikias, Stamkopoulos and Reddy, Briefings in Bioinformatics 26(4):bbaf381, 2025) ships this landscape as the herH3 dataset - data/herH3/herH3_data_full.csv, 36,560 rows of 449-aa heavy chains with a binary_score column, a one_vs_rest column and ten varying positions (99-108) - and keeps a public scoreboard of the best setups found. As of 2026-10-30 the scoreboard's Trastuzumab one-vs-rest entry is the lowest value it lists: MCC 0.3898 with ProGen2-xlarge and a memory-reduced LoRA, from 174 training rows (173 train plus 1 validation, the single mutants) predicting 36,386 held-out variants, well below the 0.5545 MCC the same framework reaches on its other binary task. The split is an extrapolation design (train on the smallest edit distance, test on everything further away), the labels are binary binder/non-binder, the data and split column are public in the repository, and the sequences differ in only ten positions, so the whole experiment is a laptop job.

## What counts as a win

Binary predictions (or scores thresholded by a rule fixed on training data only) for every row with one_vs_rest == 'test' in data/herH3/herH3_data_full.csv of github.com/LSSI-ETH/plmfit (36,386 rows), from a model fit only on that split's 173 train and 1 validation rows plus declared public pretraining corpora, such that the Matthews correlation coefficient recomputed by the skeptic with sklearn.metrics.matthews_corrcoef against the file's binary_score column is STRICTLY HIGHER (direction: max) than the value listed for 'Trastuzumab - one-vs-rest' at https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md (0.3898 as of 2026-10-30; re-fetched live immediately before claiming) by at least 0.02, AND higher than any value for the same split found by the NOVELTY check over 2024-2026 literature, reported as mean and standard deviation over at least three seeds with a bootstrap 95% interval over test sequences that excludes the bar. The threshold rule must be published and fixed without any read of test labels.

## Partial wins

- **p1:** Beat 0.3898 by >= 0.02 with a model of at most 10M parameters, or with no pretrained language model at all, under the same split and threshold rule.
- **p2:** Report AUROC and average precision for the same split with a published prediction file - threshold-free numbers that nobody has posted for this cell - as a baseline rather than a record.
- **p3:** A released ablation showing how much of the achievable MCC comes from position-wise amino-acid preferences learned from the 174 training sequences versus pairwise interactions within the 10-residue loop.
- **p4:** A threshold-selection audit: show that the claimed MCC is stable under a threshold chosen only by cross-validation on the training rows, and report how much MCC a test-set-optimal threshold would have added.

## How a win is checked

Skeptic clones github.com/LSSI-ETH/plmfit, reads herH3/herH3_data_full.csv, checks the prediction file covers each test row exactly once with the published split membership, recomputes MCC with scikit-learn, reruns the attacker's script from released seeds, audits the code for any read of test labels and for any threshold tuned on test, and re-fetches the scoreboard. Well under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>

## Sources

- <https://raw.githubusercontent.com/LSSI-ETH/plmfit/main/README.md>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12309243/fullTextXML>
- <https://github.com/dahjan/DMS_opt>
- <https://github.com/LSSI-ETH/plmfit>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- 174 labelled sequences over 10 positions: a position-specific scoring matrix with shrinkage, or logistic regression on one-hot plus pairwise features with heavy regularisation, is the honest first baseline and may already be competitive.
- MCC is threshold-sensitive and the classes are imbalanced; choose the threshold by nested cross-validation on the training rows and report the rule, since much of the gap to the leader may be calibration rather than ranking.
- Cross-domain import (few-shot classification): prototype or nearest-centroid classifiers in a frozen embedding space are strong when training data are this scarce.
- Zero-shot antibody likelihoods from several frozen models, combined by rank averaging and calibrated on the 174 training points.
- Augment by sampling labelled variants' neighbourhoods under a mutation model to regularise the pairwise terms without touching the test set.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- This is binding of an antibody variant library, not developability: FLAb-style properties and ProteinGym substitution scores are different problems and their numbers are not comparable bars.
- The split is extrapolation by edit distance; shuffling the rows into a random split inflates MCC enormously and is not the benchmark.
- MCC can be gamed by tuning the decision threshold on the test labels; the threshold rule must be fixed on training data and published.
- Pretrained checkpoints fine-tuned on this very library (several antibody-specific models were trained on public DMS data) break the design and must be declared.
- The scoreboard cell is reported for one setup only; the NOVELTY check must look for higher published MCC on the same split before any claim.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/plmfit-trastuzumab-cdrh3-binding-mcc.md
```

Already set up? Say `run V3R1T4S on plmfit-trastuzumab-cdrh3-binding-mcc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `plmfit-trastuzumab-cdrh3-binding-mcc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
