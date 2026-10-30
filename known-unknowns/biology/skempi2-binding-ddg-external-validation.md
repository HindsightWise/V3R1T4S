# SKEMPI 2.0 binding ddG: beat the published external-validation Pearson on the fixed S1131 and M1707 test sets

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (7,085 mutations with public complex structures; CPU-trainable graph and descriptor models) · open as of 2026-10-30

## The problem

SKEMPI 2.0 (Jankauskaite, Jimenez-Garcia, Dapkunas, Fernandez-Recio and Moal, Bioinformatics 35:462-469, 2019; life.bsc.es/pid/skempi2) is the reference database of experimentally measured changes in protein-protein binding energetics on mutation: 7,085 mutations, each with a solved complex structure, downloadable without registration together with cleaned PDB files. The community evaluates on fixed derived subsets: S1131 (non-redundant interface single-point mutations), S4169 and its reverse-augmented S8338, and M1707 (multiple mutations), either under split-by-structure cross-validation or as fixed blind test sets with training on the complementary SKEMPI subsets C5062 and C4856. IGMI (Wu, Xu, Xin, Zhang, Liu, Zhu, Wei, Zhao, Yu and Feng, Bioinformatics 42(4):btag150, published online 27 March 2026; github.com/ShiweiWu-545/IGMI with a Zenodo archive) reports the current published highs: in the blind external-validation setting Pearson 0.74 on S1131 and 0.91 on M1707, and under split-by-structure cross-validation 0.79 on S1131, 0.69 on S4169 and 0.77 with RMSE 2.08 on M1707, against GeoPPI at 0.57, 0.50 and 0.73, MutaBind2 at 0.71 and FoldX at 0.51 on M1707. Interface ddG prediction on structurally disjoint complexes is still far from solved, and all the data and splits are public.

## What counts as a win

Predicted binding ddG for every mutation in the fixed external-validation test sets (S1131 and M1707) distributed with the IGMI release, from a model trained only on the complementary SKEMPI 2.0 subsets published with that release (C5062 for S1131, C4856 for M1707) plus declared public structural pretraining that contains no binding ddG labels, such that the Pearson correlation recomputed by the skeptic is STRICTLY HIGHER (direction: max) than the published external-validation values - 0.74 on S1131 and 0.91 on M1707, from Bioinformatics 42(4):btag150 at https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13070472/fullTextXML, re-fetched live immediately before claiming - by at least 0.02 on the set being claimed, AND higher than any newer published value on the same set found by the NOVELTY check, with RMSE reported and a bootstrap 95% interval over mutations that excludes the published value.

## Partial wins

- **p1:** Beat the published split-by-structure cross-validation Pearson on S4169 (0.69, against GeoPPI 0.50) by >= 0.02 using the released split files unchanged, with per-fold numbers published.
- **p2:** Beat the published split-by-structure M1707 result on BOTH metrics (Pearson > 0.77 and RMSE < 2.08 kcal/mol) with the released splits, for multiple-mutation prediction.
- **p3:** A reproduction artefact: an end-to-end pipeline, published with code and manifest, that reproduces a documented baseline's S1131 external-validation Pearson to within 0.03 from the public SKEMPI 2.0 download - reported as a reproduction, not a record.
- **p4:** A sequence-only model (no complex structure at inference) that beats GeoPPI's published S1131 and S4169 numbers (0.57 and 0.50) under the same protocol, with prediction files published.
- **p5:** A released leakage audit of the chosen split: for every test mutation, the maximum interface similarity to any training complex (for example by iAlign or Foldseek), plus the metrics restricted to the least similar half.

## How a win is checked

Skeptic downloads SKEMPI 2.0 from life.bsc.es/pid/skempi2 (free, no registration) and the split files from the IGMI repository or its Zenodo archive, checks the prediction file covers each test mutation exactly once, recomputes Pearson, Spearman and RMSE, bootstraps over mutations, audits training membership against the test sets by complex and by mutation, checks no reverse-mutation twin of a test entry is in training, reruns the attacker's code from released seeds, and re-fetches the IGMI paper. A few hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13070472/fullTextXML>

## Sources

- <https://life.bsc.es/pid/skempi2>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13070472/fullTextXML>
- <https://github.com/ShiweiWu-545/IGMI>
- <https://doi.org/10.5281/zenodo.17563574>
- <https://doi.org/10.1093/bioinformatics/bty635>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Antisymmetry again: S8338 is S4169 plus reverse mutations, so a sign-flipping architecture gives the right inductive bias for free and prevents the common over-prediction of destabilisation.
- Cross-domain import (graph learning with structural priors): featurise only the interface neighbourhood (contacts, burial, conservation) rather than the whole complex; with a few thousand labels, small feature sets regularise better than large ones.
- Additive decomposition for M1707: predict single-mutation effects and learn a correction for the interaction between mutations, which gives an interpretable baseline that is hard to beat.
- Empirical energy terms (FoldX-style) as features inside a learned model rather than as competitors, with the weighting fitted on the training complexes only.
- Use the kinetic data in SKEMPI 2.0 (on-rates and off-rates) as auxiliary supervision for mutations where ddG is unavailable.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Mixing protocols is the main source of false records here: external-validation, split-by-structure and random-split numbers differ by 0.1 or more Pearson on the same data. State which protocol and which file.
- Reverse mutations make random splits leaky: a mutation's reverse in training all but gives away the label. Check for reverse twins explicitly.
- Homologous complexes across splits (the same interface in a different PDB entry) are the subtler leak; an interface-similarity audit is required for a credible claim.
- Several entries in SKEMPI 2.0 have corrected or duplicated measurements (the database's own news page records such fixes); recomputing the subsets from a fresh download can silently change the test set, so use the released split files.
- Published highs for IGMI on S8338 are not numerically stated in the paper's text (they appear only in a figure), so a claim must be made on a set whose number can be read literally.
- Antibody-antigen subsets of SKEMPI are used by separate antibody-specific benchmarks; comparing against those numbers is a category error.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/skempi2-binding-ddg-external-validation.md
```

Already set up? Say `run V3R1T4S on skempi2-binding-ddg-external-validation`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `skempi2-binding-ddg-external-validation`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
