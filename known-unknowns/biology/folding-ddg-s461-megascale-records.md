# Single-point folding stability ddG: beat the published Pearson on the leak-controlled S461 blind set (and the Megascale split record)

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: laptop-hours for S461 inference and for training on the public ddG sets; laptop-days if the Megascale split is used for training · open as of 2026-10-30

## The problem

Predicting the change in folding free energy on a single point mutation is a long-standing benchmark with maintained public test sets. ProtDDG-Bench (Capriotti, Montanucci and Fariselli, 2023; protddg-bench.github.io and github.com/protddg-bench/protddg-bench) distributes the standard sets with fixed folds: VB1432 (1,432 variants) and S2648 (2,648) with matched 10-fold splits, Ssym (684 rows - 342 mutations and their reverses, although the repository's own README calls it 634), Broom (605), Myoglobin (134), P53 (42), PTMUL (914 multiple-site variants) and the KORPM directory, which holds s461-korpm and ssym-korpm test files plus 10-fold splits of KORPM's 2,371 training mutations. S461 is the 461-mutation subset (48 proteins) of Pancotti and co-authors' S669 blind set, built by Hernandez, Chacon and co-authors to remove erroneous entries and interaction-mediated mutations. As of 2026-10-30 the highest S461 Pearson verifiable from a primary source is 0.69, and three published methods sit on it: JanusDDG (Barducci, Rossi, Codice, Rollo, Repetto, Pancotti, Iannibelli, Sanavia and Fariselli, Communications Biology 9:494, 3 February 2026), which is sequence-only, enforces antisymmetry exactly (forward/reverse Pearson -1.00) and reaches balanced accuracy 0.75 on the stabilising/destabilising call; GeoDDG-Seq (Xu, Liu and Gong, Nature Computational Science, 2024) at Pearson 0.69 with Spearman 0.68; and DVE-stability (Briefings in Bioinformatics, 2025) at Pearson 0.69 with Spearman 0.67, the last two read from DVE-stability's Supplementary Table S1. For context, the structure-based predictors tabulated by OrgNet+ (Bioinformatics 2026) top out near 0.63 on S461 and OrgNet+ itself reaches 0.58. On the separate Megascale benchmark of Tsuboyama and co-authors, using the ThermoMPNN 8:1:1 split of Dieckhaus, Brocidiacono, Randolph and Kuhlman (PNAS 121:e2314853121), SPURS (Li and Luo, Nature Communications 17:891, 20 December 2025) reports median per-protein Spearman 0.83 against ThermoMPNN's 0.77 over 28,312 mutants in 28 proteins, while its own S461 numbers are Spearman 0.66 and Pearson 0.64.

## What counts as a win

Predicted ddG for every variant of the S461 test file s461-korpm.csv (or .tsv) in the KORPM directory of github.com/protddg-bench/protddg-bench, taken unchanged and in the released order, from a model trained only on declared public data that contains no S461 variant (same protein and position counts as leakage unless the attacker publishes the clustering showing otherwise), such that the Pearson correlation recomputed by the skeptic against the released experimental values is STRICTLY HIGHER (direction: max) than 0.69 - the S461 Pearson reported by JanusDDG at https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13056967/fullTextXML, re-fetched live immediately before claiming - by at least 0.02, AND higher than any newer published S461 value found by the NOVELTY check (including values that appear only in figures or supplementary tables, with the source stated), with a bootstrap 95% interval over variants excluding 0.69, with RMSE reported, and with the antisymmetry check on ssym-korpm reported (Pearson between forward and reverse predictions, target -1).

## Partial wins

- **p1:** Beat the Megascale-split value instead: median per-protein Spearman strictly above 0.83 - the value SPURS reports, against ThermoMPNN's 0.77 - on the ThermoMPNN 8:1:1 test split of the Tsuboyama megascale data, with the per-protein table published, the split files taken unchanged from the ThermoMPNN repository, and a NOVELTY check against 2026 hybrid models that report gains on this same split.
- **p2:** Beat 0.69 on S461 with a sequence-only model of at most 150M parameters that needs no experimental structure at inference time, with runtime reported.
- **p3:** Publish a reproducible 10-fold result on the matched VB1432/S2648 folds distributed by ProtDDG-Bench (training on one set's complement, testing on the other's fold) that beats the attacker's own reproduced baseline by >= 0.03 Pearson, with all fold files unchanged.
- **p4:** Exact antisymmetry with no loss of accuracy: Ssym forward/reverse Pearson of -1.00 together with an S461 Pearson at least equal to 0.69, demonstrated from published prediction files.
- **p5:** A multiple-mutation result on the PTMUL set from ProtDDG-Bench that beats the attacker's own reproduced single-mutation-additive baseline by >= 0.05 Pearson, with the prediction file published.

## How a win is checked

Skeptic clones github.com/protddg-bench/protddg-bench, takes the S461 (and Ssym) test files unchanged, checks the prediction file covers each variant exactly once in the released order, recomputes Pearson, Spearman, RMSE and the antisymmetry correlation, bootstraps over variants, audits the declared training data for S461 proteins and positions (by sequence clustering, not only by PDB id), reruns the attacker's inference from released weights or code, and re-fetches the JanusDDG and SPURS papers for the current bars. An hour or two.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13056967/fullTextXML>

## Sources

- <https://protddg-bench.github.io/>
- <https://github.com/protddg-bench/protddg-bench>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13056967/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12830971/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13340226/fullTextXML>
- <https://github.com/Kuhlman-Lab/ThermoMPNN>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Transfer learning from the megascale dataset to the small classical sets is what moved the field (ThermoMPNN); the remaining headroom on S461 may come from better regularisation of that transfer rather than from a bigger encoder.
- Enforce antisymmetry architecturally (predict from the mutation and its reverse with a sign-flipping head) instead of penalising it in the loss - the published leaders do this and it also removes a whole class of evaluation artefacts.
- Cross-domain import (physics-informed learning): combine a cheap empirical energy term (hydrophobic burial, hydrogen-bond counts from the structure) with the learned term as an additive, interpretable model.
- Ensemble sequence-only and structure-based predictors with a weighting fitted on the training folds only; the two families fail on different mutation classes.
- Report and exploit the reverse-mutation data: Ssym's reverse entries are free training signal for symmetry without new experiments.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- S669/S461 leakage is the classic trap: most published training sets (S2648, VB1432, FireProt, megascale) overlap S461 proteins. A claim must publish the clustering that shows the training data is clean, not just a PDB-id comparison.
- 0.69 is the best S461 Pearson verifiable from a primary source on 2026-10-30 and it is a three-way tie (JanusDDG, GeoDDG-Seq, DVE-stability), not a proven ceiling. Several 2025-2026 papers report S461 PCCs only in supplementary tables (for example Pythia with mass-balance correction in Protein Science 2025, stated in the text only as above DDGun3D's 0.62, and DVE-stability in Briefings in Bioinformatics 2025), so the bar may already have moved where a text search cannot see it.
- A June 2026 preprint (arXiv 2606.08100, Shivram, Chivukula, Gupta and Chowdhury) reports S461 Spearman 0.711 +- 0.006 by retraining the SPURS backbone with balanced-MSE, Siamese antisymmetry and OOD-margin losses against its own 0.653 baseline, and publishes no S461 Pearson. A Pearson claim anywhere near 0.69-0.71 must engage with that result and state its metric explicitly.
- Different papers report different metrics on these sets (overall Pearson, per-protein mean, Spearman, balanced accuracy, direct versus reverse, with or without conformational-ensemble augmentation); mixing protocols produces false records. State the metric and the exact file.
- Predictors that are only antisymmetric on average can score well on S669 while failing Ssym; report both.
- The Megascale split and the S461 blind set are different problems with different bars; a win must be claimed on one of them explicitly, and 2026 papers (SA-MPNN, UniStab, StrucNS) report Megascale-family numbers on subsets that are not this split.
- ddG sign conventions differ between datasets (destabilising positive or negative); a sign error turns a strong model into a negative correlation.
- This field publishes fast, so the NOVELTY check must be done immediately before claiming and must say where each competing number was read.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/folding-ddg-s461-megascale-records.md
```

Already set up? Say `run V3R1T4S on folding-ddg-s461-megascale-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `folding-ddg-s461-megascale-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
