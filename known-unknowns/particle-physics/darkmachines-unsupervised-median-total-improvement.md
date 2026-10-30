# Dark Machines unsupervised anomaly detection: beat the best median total improvement (15.0, spline-flow likelihood) over the 19 BSM signals

💥 **Particle physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (four channels; channel 3 has 8.5M background events; the hackathon archive is 2.1 GB) · open as of 2026-10-30

## The problem

The Dark Machines Anomaly Score Challenge (Aarrestad, van Beekveld, Bona, Boveia, Caron, Davies, De Simone, Doglioni, Duarte, Farbin, Gupta, Hendriks, Heinrich, Howarth, Jawahar, Jueid, Lastow, Leinweber, Mamuzic, Merenyi, Morandini, Moskvitina, Nellist, Ngadiuba, Ostdiek, Pierini, Ravina, Ruiz de Austri, Sekmen, Touranakou, Vaskeviciute, Vilalta, Vlimant, Verheyen, White, Wulff, Wallin, Wozniak, Zhang; SciPost Phys. 12, 043, 2022, arXiv 2105.14027) released SM background cocktails and labelled BSM signal files for four LHC final-state channels (hackathon data, Zenodo 3961917, dataset description by M. van Beekveld). Detectors are trained on background only. For each signal and channel, SI = eps_S / sqrt(eps_B) at eps_B = 1e-2, 1e-3 and 1e-4. The total improvement (TI) of a signal is its largest SI over working points and over the channels it appears in, and methods are compared by the median TI over the 19 signals. Bryan Ostdiek's results repository holds the per-signal numbers of 1040 detectors. The best median TI is 15.0 (Flow-Efficient_Likelihood, a spline autoregressive flow, minimum TI 0.9), followed by Combined-AND- and Combined-AVG-DeepSVDD-Flow at 10.0. In the repository CSV, Flow-Efficient_Likelihood's eps_S at eps_B = 1e-4 equals its eps_S at 1e-3 in all 34 signal-channel rows; none of the other 1039 detectors shows this. Its 15.0 therefore comes from the 1e-4 column (from the 1e-2 and 1e-3 points alone its median TI is 7.9), and the record is probably inflated by tied scores or a copied column. Two chargino-neutralino signals defeat every method: the best TI is 1.1 for chaneut_cha300_neut100 and 1.0 for chaneut_cha400_neut200. Later DeepSVDD, DROCC and DDD detectors on ParT backbones (Caron et al., arXiv 2406.18469) were reported as competitive with the challenge entries, not better than its best median.

## What counts as a win

An anomaly detector trained only on SM background events from the hackathon files: per channel, background events whose event ID is odd are used for training and selection, and the remaining background events plus all signal events of that channel are used for evaluation. No signal labels or signal events may be used for training or selection. Report, for all 19 signals in their channels, eps_S at eps_B = 1e-2, 1e-3 and 1e-4 in the repository's CSV format (Signal, Model, Chan, AUC, 1e-2, 1e-3, 1e-4). At each working point the score threshold must leave at most that fraction of the evaluation background events at or above it, with tied scores counted as passing. Each eps_S is rounded to two decimals, as in the record holder's CSV, before SI is computed. The median TI over the 19 signals, computed as in notebooks/04-SignificanceImprovement.ipynb, must be STRICTLY GREATER (direction: max) than 15.0, and the minimum TI must be at least 0.9.

## Partial wins

- **p1:** Under the full-win protocol, TI strictly above 1.1 for chaneut_cha300_neut100 or strictly above 1.0 for chaneut_cha400_neut200 (the best of the 1040 challenge detectors).
- **p2:** Under the full-win protocol, median TI strictly above 10.0 (the second-best value, held by Combined-AND-DeepSVDD-Flow and Combined-AVG-DeepSVDD-Flow) with minimum TI at least 0.8.
- **p3:** Under the full-win protocol, beat the best challenge TI for at least 10 of the 19 signals with a single detector.

## How a win is checked

Download the hackathon CSVs from Zenodo 3961917 and apply the odd/even event-ID split. Retrain the detector from the released code, or score with the released weights. Recompute eps_S at the three eps_B working points by counting events, unweighted (the challenge did not use event weights). Combine into TI with an independent re-implementation of the notebook formula (SI = eps_S/sqrt(eps_B), maximum over working points and channels, median over the 19 signals). Compare with the repository's DarkMachinesUnsupervisedChallenge_TotalImprovements.csv and per-method CSVs. Inspect the code for any read of signal files before scoring.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/bostdiek/DarkMachines-UnsupervisedChallenge/tree/main/data>

## Sources

- <https://arxiv.org/abs/2105.14027>
- <https://github.com/bostdiek/DarkMachines-UnsupervisedChallenge>
- <https://zenodo.org/records/3961917>
- <https://arxiv.org/abs/2406.18469>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Modern density estimators (flow matching, transformer flows) over the variable-length object lists, which the 2021 spline flow treated with fixed features.
- Score ensembles across a density estimator and a Deep SVDD in each channel: the challenge's Combined entries already show such ensembles have higher minimum TI.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Signal labels are public: any tuning on signal files voids the claim. The 2021 entries chose their own splits, so state the odd/even rule exactly.
- eps_S at eps_B = 1e-4 needs many evaluation background events. Channel 2a has only 20,005 background events, so the odd/even split leaves about 10k, and its 1e-4 working point rests on about one event.
- The 15.0 record is suspect: Flow-Efficient_Likelihood reports the same eps_S at 1e-3 and 1e-4 in every row, which tied or saturated scores can produce. A detector whose scores tie at the threshold does not reach the stated eps_B, so apply the tie rule to your own scores and do not expect an honest detector to match the record easily. p2 (above 10.0) is the realistic target.
- The secret dataset's labels are not public, so the comparison is on hackathon data only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/particle-physics/darkmachines-unsupervised-median-total-improvement.md
```

Already set up? Say `run V3R1T4S on darkmachines-unsupervised-median-total-improvement`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `darkmachines-unsupervised-median-total-improvement`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
