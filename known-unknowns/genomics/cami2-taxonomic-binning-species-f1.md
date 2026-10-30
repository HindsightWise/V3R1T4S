# CAMI II taxonomic binning of reads at species rank: beat ganon2's per-bin F1 on the plant-associated samples without losing accuracy

🧫 **Genomes** · standard · tractability ★★★☆☆ · compute: laptop-days (classify 21 short-read samples of about 5 Gbp each against an index of the 2019-01-08 RefSeq snapshot; 64 GB RAM helps) · open as of 2026-10-30

## The problem

Taxonomic binners label each read or contig with a taxon, which is a different output from an abundance profile. CAMI II (Meyer et al., Nature Methods 2022) scored taxonomic binning with AMBER, and the CAMI Benchmarking Portal (Meyer, Robertson, Deng et al., NAR 2025) keeps per-rank, sample-averaged tables. At species rank on short reads the per-bin scores are poor because many small false-positive species bins drag down average purity. On 2026-10-30 the live tables showed: plant-associated (21 samples), ganon2 2.1.0 with F1 (bp) 0.055 (average purity 0.029, average completeness 0.460) and accuracy (bp) 0.712, ahead of Ganon 0.3.1 (F1 0.051, accuracy 0.700) and Kraken 2.0.8 beta (0.011, 0.320); marine (10 samples), Metabuli 1.0.8 with the best F1 (bp) 0.279 at accuracy 0.390, and ganon2 2.1.0 with the best accuracy 0.901 at F1 0.221; strain-madness (100 samples), Ganon 0.1.4 at F1 0.033 and ganon2 2.1.0 at accuracy 0.850. No listed method combines high per-bin purity with high accuracy.

## What counts as a win

Read-level taxonomic binning files (CAMI binning format) for all 21 plant-associated short-read samples, produced by released deterministic code using only references frozen at or before 2019-01-08 (no database containing the CAMI II source genomes), whose sample-averaged species-rank scores, computed by AMBER with no filter and no minimum length as in the record row, have F1 score (bp) STRICTLY GREATER than 0.055 AND accuracy (bp) of at least 0.712 (both from ganon2 2.1.0; direction: max), beating every row of the live table at https://cami-challenge.org/datasets/plant-associated/avg/group_4/taxonomic_binning/species/ (re-fetched immediately before claiming) on F1 (bp). A minimum bin size, read-count or abundance cut that unassigns reads at species rank is a filter: a claim whose pipeline applies one must also report ganon2 2.1.0, rerun by the claimant on the same 2019-01-08 references with released commands and scored after the same cut, and must beat that rerun on F1 (bp) while keeping accuracy (bp) of at least 0.712.

## Partial wins

- **p1:** Marine (10 samples, averaged, species rank, unfiltered): F1 score (bp) STRICTLY GREATER than 0.279 (Metabuli 1.0.8) with accuracy (bp) of at least 0.901 (ganon2 2.1.0), dominating both leaders, under the same rules (including the ganon2-rerun rule for any size or abundance cut).
- **p2:** Strain-madness (100 samples, averaged, species rank, unfiltered): F1 score (bp) STRICTLY GREATER than 0.033 with accuracy (bp) of at least 0.850, under the same rules (including the ganon2-rerun rule for any size or abundance cut).
- **p3:** Plant-associated: F1 score (bp) of at least 0.10 at accuracy (bp) of at least 0.60, nearly doubling the listed F1 while giving up little accuracy, under the same rules (including the ganon2-rerun rule for any size or abundance cut).

## How a win is checked

Skeptic downloads the read-level gold-standard mappings for the plant-associated samples, runs AMBER in taxonomic mode on the claimed files with no filter, averages over samples as the portal does, compares F1 (bp) and accuracy (bp) with the live table, and checks the reference build date in the released code. Minutes per sample.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cami-challenge.org/datasets/plant-associated/avg/group_4/taxonomic_binning/species/>

## Sources

- <https://cami-challenge.org/datasets/plant-associated/avg/group_4/taxonomic_binning/species/>
- <https://cami-challenge.org/datasets/marine/avg/group_1/taxonomic_binning/species/>
- <https://cami-challenge.org/datasets/strain-madness/avg/group_30/taxonomic_binning/species/>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12230735/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9007738/fullTextXML>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Average purity is a per-bin mean dominated by many tiny false-positive species bins. A principled fix (calibrated per-read confidence, LCA on ambiguous hits, pushing doubtful reads up to genus) has to beat what a plain size cut already gives ganon2, as the criterion requires.
- Use profile-informed binning: first estimate which species are present, then restrict read assignment to that set.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The portal's 'Filter %' option removes small bins and inflates F1; the criterion is unfiltered.
- A minimum-bin-size or abundance cut built into the pipeline is the same filter by another name. It likely lifts average purity a lot at little accuracy cost, so it counts only against a ganon2 2.1.0 rerun given the same cut.
- Accuracy (bp) and F1 (bp) trade off; a claim must meet both bounds at once.
- Read-level and gold-standard-contig tables are different; this target is the read-level sample average.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/cami2-taxonomic-binning-species-f1.md
```

Already set up? Say `run V3R1T4S on cami2-taxonomic-binning-species-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cami2-taxonomic-binning-species-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
